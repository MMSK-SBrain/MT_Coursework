// Outcome hierarchy: SO repair in hour plans, the per-session content check and its block repair,
// and the MO roll-up repair in draftPlan. All model calls are scripted; no network.
import { describe, expect, it } from "vitest";
import { Course as CourseSchema, sessionOutcomeProblems } from "@cg/core";
import { OpenRouterStages } from "../src/stages.js";
import { ExampleStore } from "../src/examples.js";
import { FixtureOccupationSource, FixtureLinkSource } from "../src/sources/fixture.js";
import { aezc517Course, S3_BLOCKS } from "../src/fixtures/aezc517.js";
import { scoreVerdicts } from "../src/contentCheck.js";
import { maxBloomForHours } from "../src/hierarchy.js";
import { moduleOutcomeDraftProblems } from "../src/checks.js";
import { ScriptedClient, fixedNow, testConfig } from "./helpers.js";

const noExamples = new ExampleStore({ coursesDir: "/nonexistent/courses", inline: [] });
const make = (client: ScriptedClient) =>
  new OpenRouterStages({ client, config: testConfig, roles: new FixtureOccupationSource(), links: new FixtureLinkSource(), examples: noExamples, now: fixedNow });

const draftBlocks = () => S3_BLOCKS.map(({ industryExample: _x, ...b }) => ({ ...b }));
const allYes = (blocks: { sessionOutcomeIds: string[] }[]) => ({
  verdicts: blocks.flatMap((b, block) => b.sessionOutcomeIds.map((so) => ({ block, so, verdict: "yes", reason: "Learners practise it." }))),
});

describe("hour plan against session outcomes", () => {
  const course = aezc517Course();

  it("repairs blocks that leave an SO unserved (sessionOutcomeProblems)", async () => {
    const broken = draftBlocks().map((b) => ({ ...b, sessionOutcomeIds: b.sessionOutcomeIds.map(() => "S3.SO1") }));
    const c = new ScriptedClient([{ blocks: broken }, { blocks: draftBlocks() }, allYes(draftBlocks())]);
    const r = await make(c).draftHourPlan(course, "p1", "s3");
    expect(c.requests[1]!.messages.at(-1)!.content).toMatch(/S3\.SO2 is not served by any block/);
    const session = { ...course.plans[0]!.sessions[2]!, blocks: r.value };
    expect(sessionOutcomeProblems(session)).toEqual([]);
    expect(r.warnings).toEqual([]);
  });

  it("content check: one reviewer call per session; a failing block gets one repair", async () => {
    const blocks = draftBlocks();
    const verdicts = allYes(blocks).verdicts.map((v) => (v.block === 2 ? { ...v, verdict: "no", reason: "Learners only read the requirements; they never rewrite one." } : v));
    const patch = { blocks: [{ block: 2, title: "Rewrite five bad requirements", activity: "Each trio rewrites five flawed BMS requirements into verifiable ones, names the verification method for each, and swaps with another trio to critique.", check: ["Which rewrite is still ambiguous, and why?"] }] };
    const c = new ScriptedClient([{ blocks }, { verdicts }, patch]);
    const stages = make(c);
    const r = await stages.draftHourPlan(course, "p1", "s3");

    expect(c.requests).toHaveLength(3);
    expect(c.requests[1]!.model).toBe("test/review");
    expect(c.requests[1]!.messages[1]!.content).toContain("S3.SO2 [apply]");
    expect(c.requests[2]!.model).toBe("test/draftHourPlan");
    expect(c.requests[2]!.messages[1]!.content).toContain("they never rewrite one");
    expect(r.value[2]!.activity).toMatch(/swaps with another trio/);
    expect(r.value[2]!.sessionOutcomeIds).toEqual(["S3.SO2"]); // timing and SOs kept
    expect(r.value[2]!.minutes).toBe(blocks[2]!.minutes);
    expect(stages.lastContentCheck.get("s3")).toMatchObject({ repaired: [2], check: { failing: [2] } });
    expect(r.provenance.costUsd).toBeCloseTo(0.003);
    expect(r.warnings).toEqual([]);
  });

  it("content check: warns when the block repair fails", async () => {
    const blocks = draftBlocks();
    const verdicts = allYes(blocks).verdicts.map((v) => (v.block === 4 ? { ...v, verdict: "partly", reason: "No test case is written." } : v));
    const c = new ScriptedClient([{ blocks }, { verdicts }, "not json", "still not json"]);
    const r = await make(c).draftHourPlan(course, "p1", "s3");
    expect(r.warnings.some((w) => /Trace a need to a test/.test(w) && /No test case is written/.test(w))).toBe(true);
  });

  it("scores verdicts: skipped pairs count as no, SO fulfilment needs a full yes", () => {
    const input = {
      sessionTitle: "t", audience: "a",
      sessionOutcomes: [{ id: "SO1", text: "Explain x", bloom: "understand" as const }, { id: "SO2", text: "Apply y", bloom: "apply" as const }],
      blocks: [
        { kind: "teach" as const, title: "b0", minutes: 20, activity: "x", check: [], sessionOutcomeIds: ["SO1"] },
        { kind: "activity" as const, title: "b1", minutes: 30, activity: "y", check: [], sessionOutcomeIds: ["SO1", "SO2"] },
        { kind: "break" as const, title: "b2", minutes: 10, activity: "z", check: [], sessionOutcomeIds: [] },
      ],
    };
    const s = scoreVerdicts(input, [{ block: 0, so: "SO1", verdict: "yes", reason: "ok" }, { block: 1, so: "SO2", verdict: "partly", reason: "thin" }], 0.75);
    expect(s.blockScores).toEqual([{ block: 0, score: 1 }, { block: 1, score: 0.25 }]);
    expect(s.failing).toEqual([1]);
    expect(s.soFulfilment).toEqual([{ so: "SO1", best: 1, fulfilled: true }, { so: "SO2", best: 0.5, fulfilled: false }]);
  });
});

describe("draftPlan roll-up", () => {
  const base = aezc517Course();
  const course = CourseSchema.parse({ ...base, plans: [] });
  const goodSessions = base.plans[0]!.sessions.map(({ title, outcomeIds, style, minutes, video, sessionOutcomes }) => ({
    title, outcomeIds, style, minutes, video,
    sessionOutcomes: sessionOutcomes.map(({ text, bloom, moduleOutcomeIds }) => ({ text, bloom, moduleOutcomeIds })),
  }));
  // M3.MO1 (apply) is only served at "understand": the module is not met.
  const weak = goodSessions.map((s, i) => (i === 2 ? { ...s, sessionOutcomes: s.sessionOutcomes.filter((so) => so.bloom !== "apply") } : s));

  it("an unmet module outcome triggers one repair", async () => {
    const c = new ScriptedClient([{ name: "Classroom", sessions: weak }, { name: "Classroom", sessions: goodSessions }]);
    const r = await make(c).draftPlan(course, { path: "classroom", style: "auto" });
    expect(c.requests[1]!.messages.at(-1)!.content).toMatch(/module outcome M3\.MO1 is not met: session outcomes reach understand, the module outcome needs apply/);
    expect(r.value.sessions[2]!.sessionOutcomes.map((so) => so.id)).toEqual(["S3.SO1", "S3.SO2"]);
    expect(r.warnings.some((w) => /M3\.MO1|LO2/.test(w))).toBe(false);
  });

  it("anything still unmet after the repair becomes a warning, with the LO it blocks", async () => {
    const c = new ScriptedClient([{ name: "Classroom", sessions: weak }, { name: "Classroom", sessions: weak }]);
    const r = await make(c).draftPlan(course, { path: "classroom", style: "auto" });
    expect(r.warnings.some((w) => /module outcome M3\.MO1 is not met/.test(w))).toBe(true);
    expect(r.warnings.some((w) => /learning outcome LO2 is not met/.test(w))).toBe(true);
  });
});

describe("module outcome checks", () => {
  it("caps Bloom level by module hours and requires every LO to be served", () => {
    expect(maxBloomForHours(1)).toBe("understand");
    expect(maxBloomForHours(4)).toBe("create");
    const modules = [{ id: "M1", title: "x", hours: 1, topics: [], outcomes: [], foundIn: "handout" as const }];
    const p = moduleOutcomeDraftProblems([{ moduleId: "M1", text: "Design a BMS architecture.", bloom: "create", outcomeIds: ["LO1"] }], modules, ["LO1", "LO2"]);
    expect(p).toContain("M1 module outcome 1 is at create, but 1 h can support at most understand");
    expect(p).toContain("learning outcome(s) LO2 are served by no module outcome");
  });
});

describe("plan text checks", () => {
  it("flags durations longer than the block and 'no conflict' in academicConflict", async () => {
    const { hourPlanProblems, fitProblems } = await import("../src/checks.js");
    const b = { hour: 1, startMin: 0, minutes: 5, title: "Break", activity: "A 10-minute break.", outcomeIds: ["LO1"] };
    expect(hourPlanProblems([b], 5, ["LO1"]).some((x) => /says 10 minutes/.test(x))).toBe(true);
    expect(hourPlanProblems([{ ...b, activity: "Take a 5 min break." }], 5, ["LO1"]).some((x) => /says/.test(x))).toBe(false);
    const ch = { kind: "add" as const, targetModuleId: "M1", hoursDelta: 1, roleIds: ["r1"], academicConflict: "No conflict: LO1 is unaffected." };
    expect(fitProblems([ch], [{ id: "M1" } as never], ["r1"], 30).some((x) => /academicConflict/.test(x))).toBe(true);
    expect(fitProblems([{ ...ch, academicConflict: "LO2 requires knock diagnosis" }], [{ id: "M1" } as never], ["r1"], 30).some((x) => /academicConflict/.test(x))).toBe(false);
  });
});
