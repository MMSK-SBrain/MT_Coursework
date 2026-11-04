import { describe, expect, it } from "vitest";
import { hourBlockProblems, outcomeVerbProblem, uncoveredOutcomes, videoAllowed } from "./rules.js";
import type { HourBlock, LearningPlan, Outcome } from "./model.js";

const prov = { model: "test", promptId: "t", promptVersion: "1", costUsd: 0, createdAt: "2026-11-04T00:00:00Z", builtFrom: [] };
const block = (hour: number, startMin: number, minutes: number): HourBlock => ({
  id: `b${hour}-${startMin}`, hour, startMin, minutes, kind: "teach", title: `b${startMin}`, activity: "x",
  outcomeIds: [], sessionOutcomeIds: [], style: "teaching", check: [], needsSlides: false, provenance: prov,
});

describe("rules", () => {
  it("flags vague and wrong-level verbs", () => {
    expect(outcomeVerbProblem({ text: "Understand the V-model", bloom: "understand" })).toMatch(/unmeasurable/);
    expect(outcomeVerbProblem({ text: "Describe the V-model", bloom: "evaluate" })).toMatch(/evaluate-level/);
    expect(outcomeVerbProblem({ text: "Evaluate two BMS designs", bloom: "evaluate" })).toBeNull();
  });
  it("checks hour blocks add up", () => {
    expect(hourBlockProblems([block(1, 0, 20), block(1, 20, 40), block(2, 0, 60)], 120)).toEqual([]);
    expect(hourBlockProblems([block(1, 0, 20), block(1, 25, 30)], 60)).toHaveLength(2);
    expect(hourBlockProblems([block(1, 0, 60), block(2, 0, 30)], 90)).toEqual([]);
  });
  it("finds uncovered outcomes", () => {
    const o = (id: string) => ({ id }) as Outcome;
    const plan = { sessions: [{ outcomeIds: ["LO1"] }] } as unknown as LearningPlan;
    expect(uncoveredOutcomes({ outcomes: [o("LO1"), o("LO2")] }, plan)).toEqual(["LO2"]);
  });
  it("enforces video rules by path", () => {
    expect(videoAllowed("elearning", "explainroo")).toBe(false);
    expect(videoAllowed("classroom", "demo")).toBe(true);
    expect(videoAllowed("youtube", "whiteboard")).toBe(true);
  });
});

import { FurtherLink, isHttpUrl } from "./model.js";
describe("links", () => {
  it("accepts only http and https URLs", () => {
    expect(isHttpUrl("https://example.org/a")).toBe(true);
    expect(isHttpUrl("javascript:alert(1)")).toBe(false);
    expect(isHttpUrl("data:text/html,x")).toBe(false);
    expect(FurtherLink.safeParse({ id: "l1", kind: "other", title: "t", url: "javascript:alert(1)", why: "w" }).success).toBe(false);
  });
});

import { learningOutcomeCoverage, moduleOutcomeCoverage, sessionOutcomeProblems } from "./rules.js";
import type { Course, Session } from "./model.js";

describe("outcome hierarchy", () => {
  const p = { model: "t", promptId: "t", promptVersion: "1", costUsd: 0, createdAt: "2026-11-04T00:00:00Z", builtFrom: [] };
  const so = (id: string, text: string, bloom: "understand" | "apply" | "evaluate", mo: string[]) => ({ id, text, bloom, moduleOutcomeIds: mo, locked: false, provenance: p });
  const blk = (id: string, sos: string[], kind: "teach" | "wrap" = "teach") => ({ ...block(1, 0, 60), id, title: id, kind, sessionOutcomeIds: sos });
  const session = (sos: ReturnType<typeof so>[], blocks: ReturnType<typeof blk>[]) =>
    ({ id: "s1", index: 1, title: "S1", outcomeIds: ["LO1"], sessionOutcomes: sos, blocks, style: "teaching", minutes: 60, video: "none", links: [], caseStudies: [], assets: [], stale: false, provenance: p }) as Session;
  const course = {
    outcomes: [{ id: "LO1" }, { id: "LO2" }],
    modules: [{ id: "M1", outcomes: [
      { id: "M1.MO1", text: "Apply x", bloom: "apply", outcomeIds: ["LO1"], locked: false, provenance: p },
      { id: "M1.MO2", text: "Evaluate y", bloom: "evaluate", outcomeIds: ["LO2"], locked: false, provenance: p },
    ] }],
  } as unknown as Course;

  it("flags SOs no block serves and blocks that serve nothing", () => {
    const s = session([so("SO1", "Describe the V-model", "understand", []), so("SO2", "Apply the checks", "apply", [])], [blk("b1", ["SO1"]), blk("b2", []), blk("b3", [], "wrap")]);
    const probs = sessionOutcomeProblems(s);
    expect(probs).toContain("SO2 is not served by any block");
    expect(probs).toContain('block "b2" serves no session outcome');
    expect(probs.some((x) => x.includes("b3"))).toBe(false);
  });

  it("rolls SOs up to module and course outcomes by Bloom level", () => {
    const plan = { sessions: [session([so("SO1", "Apply x", "apply", ["M1.MO1"]), so("SO2", "Describe y", "understand", ["M1.MO2"])], [])] } as never;
    const mo = moduleOutcomeCoverage(course, plan);
    expect(mo.find((m) => m.moduleOutcomeId === "M1.MO1")?.met).toBe(true);
    expect(mo.find((m) => m.moduleOutcomeId === "M1.MO2")?.problem).toMatch(/reach understand.*needs evaluate/);
    expect(learningOutcomeCoverage(course, plan)).toEqual([
      { outcomeId: "LO1", met: true, moduleOutcomeIds: ["M1.MO1"] },
      { outcomeId: "LO2", met: false, moduleOutcomeIds: ["M1.MO2"] },
    ]);
  });
});
