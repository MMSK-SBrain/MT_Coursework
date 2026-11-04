import { describe, expect, it } from "vitest";
import { Course as CourseSchema, FurtherLink, HourBlock, hourBlockProblems, type Course, type InputFile } from "@cg/core";
import { OpenRouterStages } from "../src/stages.js";
import { ExampleStore } from "../src/examples.js";
import { FixtureOccupationSource, FixtureLinkSource } from "../src/sources/fixture.js";
import { aezc517Course, MODULES, MODULE_OUTCOMES, S3_BLOCKS, VIDEOS, PAGES } from "../src/fixtures/aezc517.js";
import { FIT_RUBRIC, OUTCOMES_RUBRIC } from "../src/prompts/review.js";
import { ScriptedClient, fixedNow, goodReview, testConfig } from "./helpers.js";

const noExamples = new ExampleStore({ coursesDir: "/nonexistent/courses", inline: [] });
const make = (client: ScriptedClient, links = new FixtureLinkSource()) =>
  new OpenRouterStages({ client, config: testConfig, roles: new FixtureOccupationSource(), links, examples: noExamples, now: fixedNow });

const draftBlocks = () => S3_BLOCKS.map(({ industryExample, ...b }) => ({
  ...b, ...(industryExample ? { industryExample: { text: industryExample.text, sector: industryExample.sector, roleIds: industryExample.roleIds, evidenceIdx: [0] } } : {}),
}));

/** A content-check reply judging every (block, SO) pair "yes". */
export const allYes = (blocks: { sessionOutcomeIds: string[] }[]) => ({
  verdicts: blocks.flatMap((b, block) => b.sessionOutcomeIds.map((so) => ({ block, so, verdict: "yes", reason: "Learners practise it." }))),
});

describe("OpenRouterStages", () => {
  const course = aezc517Course();

  it("draftHourPlan: assigns ids, maps evidence to sources, attaches provenance", async () => {
    const c = new ScriptedClient([{ blocks: draftBlocks() }, allYes(draftBlocks())]);
    const r = await make(c).draftHourPlan(course, "p1", "s3");
    expect(r.warnings).toEqual([]);
    expect(r.value.every((b) => b.kind === "break" || b.sessionOutcomeIds.length > 0)).toBe(true);
    expect(c.requests[1]!.model).toBe("test/review"); // the content check
    expect(r.value.map((b) => b.id)[0]).toBe("s3-b1");
    expect(r.value.every((b) => HourBlock.safeParse(b).success)).toBe(true);
    expect(hourBlockProblems(r.value, 120)).toEqual([]);
    const ex = r.value.find((b) => b.industryExample)!.industryExample!;
    expect(ex.sources[0]!.url).toBe(course.roles.find((x) => x.selected)!.evidence[0]!.url);
    expect(r.provenance).toMatchObject({ model: "test/draftHourPlan", promptId: "session.hourPlan", promptVersion: "3", structureVersion: 2 });
    // facts supplied: the evidence list is in the prompt
    expect(c.requests[0]!.messages[1]!.content).toContain("role evidence");
  });

  it("draftHourPlan: a timing error triggers one repair", async () => {
    const broken = draftBlocks().map((b, i) => (i === 2 ? { ...b, minutes: 20 } : b));
    const c = new ScriptedClient([{ blocks: broken }, { blocks: draftBlocks() }, allYes(draftBlocks())]);
    const r = await make(c).draftHourPlan(course, "p1", "s3");
    expect(c.requests[1]!.messages.at(-1)!.content).toMatch(/hour 1: blocks add up to 55 min, expected 60/);
    expect(r.warnings).toEqual([]);
  });

  it("findFurtherLearning: only returns supplied candidates, drops dead links", async () => {
    const dead = new Set([VIDEOS[0]!.url]);
    const c = new ScriptedClient([{ picks: [{ source: "video", idx: 0, why: "Shows requirement writing" }, { source: "page", idx: 0, why: "Reference reading" }] }]);
    const r = await make(c, new FixtureLinkSource(VIDEOS, PAGES, dead)).findFurtherLearning(course, "p1", "s3");
    const known = new Set([...VIDEOS, ...PAGES].map((x) => x.url));
    expect(r.value).toHaveLength(2);
    expect(r.value.every((l) => known.has(l.url) && !dead.has(l.url) && !l.approved && FurtherLink.safeParse(l).success)).toBe(true);
    expect(r.warnings[0]).toMatch(/did not resolve/);
  });

  it("draftOutcomes: keeps locked outcomes, runs rubric review", async () => {
    const locked = course.outcomes[0]!;
    const input: Course = CourseSchema.parse({ ...course, outcomes: [locked], objectives: course.objectives });
    const draft = {
      moduleOutcomes: Object.entries(MODULE_OUTCOMES).flatMap(([moduleId, mos]) => mos.map(({ text, bloom, outcomeIds }) => ({ moduleId, text, bloom, outcomeIds }))),
      objectives: course.objectives.map(({ id, text }) => ({ id, text })),
      outcomes: [
        { id: "LO1", text: "Rewritten by model, should be ignored.", bloom: "apply", moduleIds: ["M1"], objectiveIds: ["CO1"], roleIds: [], origin: "new" },
        ...course.outcomes.slice(1).map(({ id, text, bloom, moduleIds, objectiveIds, roleIds, origin }) => ({ id, text, bloom, moduleIds, objectiveIds, roleIds: [...roleIds, "rX"], origin })),
      ],
    };
    const keep = { ...draft, outcomes: [{ ...draft.outcomes[0]!, text: locked.text, bloom: locked.bloom, moduleIds: locked.moduleIds }, ...draft.outcomes.slice(1)] };
    const c = new ScriptedClient([draft, keep, goodReview(OUTCOMES_RUBRIC.criteria.map((x) => x.id))]);
    const r = await make(c).draftOutcomes(input);
    expect(c.requests[1]!.messages.at(-1)!.content).toMatch(/locked outcome LO1 must be returned unchanged/);
    expect(r.value.outcomes[0]).toEqual(locked);
    expect(r.value.outcomes).toHaveLength(6);
    expect(r.value.outcomes.every((o) => !o.roleIds.includes("rX"))).toBe(true);
    expect(r.value.modules.find((m) => m.id === "M7")!.outcomes.map((o) => o.id)).toEqual(["M7.MO1", "M7.MO2"]);
    expect(c.requests[2]!.model).toBe("test/review");
    expect(r.warnings).toEqual([]);
  });

  it("findRoles: takes titles and skills from ESCO, computes the match in code", async () => {
    const c = new ScriptedClient([
      { keywords: ["systems engineering", "requirements engineering", "battery management system"] },
      { roles: [{ occIdx: 0, coveredSkillIdx: [0, 1, 1] }, { occIdx: 999, coveredSkillIdx: [] }] },
      { roles: [{ occIdx: 0, coveredSkillIdx: [0, 1, 1] }] },
    ]);
    const r = await make(c).findRoles(course.brief, MODULES);
    expect(r.value.keywords).toHaveLength(3);
    expect(r.value.roles).toHaveLength(1);
    // Title, skills and match come from the occupation and are computed in code, not by the model.
    const [occ] = await new FixtureOccupationSource().search({ keywords: r.value.keywords, limit: 30 });
    expect(r.value.roles[0]).toMatchObject({ id: "r1", title: occ!.title, skills: occ!.essentialSkills, matchedSkills: occ!.essentialSkills.slice(0, 2), selected: false });
    expect(r.value.roles[0]!.moduleMatch).toBe(Math.round((2 / occ!.essentialSkills.length) * 100));
    expect(r.value.roles[0]!.evidence[0]!.url).toBe(occ!.url);
    expect(r.value.occupationsRead).toBeGreaterThan(0);
    expect(r.provenance.costUsd).toBeCloseTo(0.003);
  });

  it("proposeFit: validates targets and roles, reviews with the fit rubric", async () => {
    const changes = [
      { kind: "add", text: "Hazard analysis (HARA) and safety goals", reason: "3 of 4 roles need HARA", targetModuleId: "M7", hoursDelta: 2, roleIds: ["r3"] },
      { kind: "trim", text: "Soft-skills content in M1", reason: "Rarely asked for", targetModuleId: "M1", hoursDelta: -2, roleIds: ["r1"], academicConflict: "CO1 requires soft skills" },
    ];
    const c = new ScriptedClient([{ changes }, goodReview(FIT_RUBRIC.criteria.map((x) => x.id))]);
    const r = await make(c).proposeFit(course);
    expect(r.value.map((f) => f.id)).toEqual(["f1", "f2"]);
    expect(r.value[1]!.academicConflict).toBe("CO1 requires soft skills");
    expect(r.value.every((f) => f.decision === "pending" && f.provenance.promptId === "fit.propose")).toBe(true);
  });

  it("draftCaseStudy: 'real' without sources becomes composite", async () => {
    const c = new ScriptedClient([{
      title: "Thermal derating", background: "x".repeat(80), data: "", questions: ["What failed?", "What would you change?"],
      teachingNote: "y".repeat(40), sourceIdx: [], outcomeIds: ["LO2", "LO9"],
    }]);
    const r = await make(c, new FixtureLinkSource(VIDEOS, [])).draftCaseStudy(course, "p1", "s3", "real");
    expect(r.value.label).toBe("composite");
    expect(r.value.outcomeIds).toEqual(["LO2"]);
    expect(r.warnings[0]).toMatch(/Composite/);
  });

  it("parseInputs: reads text files, warns on formats it cannot read", async () => {
    const file = (id: string, filename: string, mime: string, text: string): InputFile => ({
      meta: { id, kind: "handout", filename, mime, storageKey: id }, bytes: new TextEncoder().encode(text),
    });
    const parsed = {
      brief: { title: "Systems Engineering", contactHours: 32 },
      modules: [{ id: "M1", title: "Systems thinking", hours: 4, topics: [], foundIn: "handout" }],
      objectives: [{ id: "CO1", text: "Build systems skills." }],
      outcomes: [{ id: "LO1", text: "Understand systems thinking.", bloom: "understand", moduleIds: [] }],
      gaps: ["CO4 is empty"],
    };
    const c = new ScriptedClient([parsed]);
    const r = await make(c).parseInputs([file("h", "handout.txt", "text/plain", "HANDOUT TEXT"), file("d", "h.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "")]);
    expect(c.requests[0]!.messages[1]!.content).toContain("HANDOUT TEXT");
    expect(r.value.outcomes[0]).toMatchObject({ origin: "handout", moduleIds: [] }); // no longer every module
    expect(r.warnings.some((w) => /h\.docx/.test(w))).toBe(true);
    expect(r.warnings.some((w) => /Handout LO1 starts with the unmeasurable verb/.test(w))).toBe(true);
    expect(r.provenance.builtFrom).toEqual(["h", "d"]);
  });
});
