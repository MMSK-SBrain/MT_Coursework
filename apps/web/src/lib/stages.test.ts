import {
  CaseStudy, Course, FitChange, FurtherLink, HourBlock, JobRole, LearningPlan, OutcomeSuggestion, hourBlockProblems, outcomeVerbProblem,
  uncoveredOutcomes,
} from "@cg/core";
import { MockStages, OpenRouterStages } from "@cg/harness";
import { strToU8, unzipSync, zipSync } from "fflate";
import { describe, expect, it } from "vitest";
import { acceptSuggestion, allFitDecided, applyHourPlan, applyOutcomes, confirmStructure, newCourse, setLocked } from "./course-logic";
import { createStages, getExporter } from "./stages";
import { mockStages, sampleCourse } from "./test-fixtures";

describe("stage wiring", () => {
  it("uses the harness mock without an OpenRouter key and the real stages with one", () => {
    expect(createStages({})).toBeInstanceOf(MockStages);
    expect(createStages({ OPENROUTER_API_KEY: "sk-test" })).toBeInstanceOf(OpenRouterStages);
  });
});

describe("the stages return schema-valid data the app can apply", () => {
  it("runs the whole flow into a valid Course", async () => {
    const { course } = await sampleCourse();
    expect(() => Course.parse(course)).not.toThrow();
    expect(course.modules.length).toBeGreaterThan(0);
    expect(course.roles.every((r) => JobRole.safeParse(r).success)).toBe(true);
    expect(course.fit.every((f) => FitChange.safeParse(f).success)).toBe(true);
    expect(course.structureVersion).toBe(2);
    expect(course.outcomes.map((o) => outcomeVerbProblem(o))).toEqual(course.outcomes.map(() => null));
    expect(LearningPlan.safeParse(course.plans[0]).success).toBe(true);
    expect(uncoveredOutcomes(course, course.plans[0]!)).toEqual([]);
  });

  it("stores the module outcomes drafted with the outcomes", async () => {
    const { course } = await sampleCourse();
    expect(course.modules.every((m) => m.outcomes.length > 0)).toBe(true);
  });

  it("hour-wise plans add up and drafting one clears the stale flag", async () => {
    const { course } = await sampleCourse();
    const plan = course.plans[0]!;
    for (const s of plan.sessions) {
      const g = await mockStages.draftHourPlan(course, plan.id, s.id);
      expect(g.value.every((b) => HourBlock.safeParse(b).success)).toBe(true);
      expect(hourBlockProblems(g.value, s.minutes)).toEqual([]);
    }
    const stale = { ...course, plans: [{ ...plan, sessions: plan.sessions.map((s) => ({ ...s, stale: true })) }] };
    const g = await mockStages.draftHourPlan(stale, plan.id, plan.sessions[0]!.id);
    expect(applyHourPlan(stale, plan.id, plan.sessions[0]!.id, g.value).plans[0]!.sessions[0]!.stale).toBe(false);
  });

  it("links, case studies and suggestions are valid", async () => {
    const { course } = await sampleCourse();
    const plan = course.plans[0]!, s = plan.sessions[0]!;
    const links = await mockStages.findFurtherLearning(course, plan.id, s.id);
    expect(links.value.every((l) => FurtherLink.safeParse(l).success && !l.approved)).toBe(true);
    for (const label of ["real", "composite"] as const) {
      const cs = await mockStages.draftCaseStudy(course, plan.id, s.id, label);
      expect(CaseStudy.safeParse(cs.value).success).toBe(true);
      if (label === "real") expect(cs.value.sources.length).toBeGreaterThan(0);
    }
    const lo = course.outcomes[1]!;
    for (const kind of ["raiseBloom", "measurable", "industryContext", "shorten", "split", "matchHandout", "free"] as const) {
      const g = await mockStages.suggestOutcomeEdit(course, lo.id, { kind, note: "focus on the BMS capstone" });
      expect(OutcomeSuggestion.safeParse(g.value).success).toBe(true);
    }
    const split = await mockStages.suggestOutcomeEdit(course, lo.id, { kind: "split", note: "" });
    const after = acceptSuggestion(course, split.value, split.provenance);
    if (split.value.proposed.length > 1) expect(after.outcomes.map((o) => o.id)).toContain(`${lo.id}b`);
    expect(() => Course.parse(after)).not.toThrow();
  });

  it("suggests edits for module outcomes and objectives through the LO-only contract", async () => {
    const { course } = await sampleCourse();
    const mo = course.modules[0]!.outcomes[0]!;
    const g = await mockStages.suggestOutcomeEdit(course, mo.id, { kind: "measurable", note: "" });
    expect(g.value.targetId).toBe(mo.id);
    const after = acceptSuggestion(course, g.value, g.provenance);
    expect(after.modules[0]!.outcomes[0]!.text).toBe(g.value.proposed[0]!.text);
    expect(after.outcomes).toHaveLength(course.outcomes.length); // the shim LO never reaches the stored course
    const co = course.objectives[0]!;
    const gc = await mockStages.suggestOutcomeEdit(course, co.id, { kind: "shorten", note: "" });
    expect(acceptSuggestion(course, gc.value, gc.provenance).objectives[0]!.text).toBe(gc.value.proposed[0]!.text);
  });

  it("keeps locked outcomes and module outcomes when redrafting", async () => {
    const { course, meta } = await sampleCourse();
    const lo = course.outcomes[2]!, mo = course.modules[0]!.outcomes[0]!;
    let c = { ...course, outcomes: course.outcomes.map((o) => (o.id === lo.id ? { ...o, text: "Model it my way." } : o)) };
    c = { ...c, modules: c.modules.map((m, i) => (i === 0 ? { ...m, outcomes: m.outcomes.map((o) => (o.id === mo.id ? { ...o, text: "Explain it my way." } : o)) } : m)) };
    c = setLocked(setLocked(c, lo.id, true), mo.id, true);
    const [after] = applyOutcomes(c, meta, (await mockStages.draftOutcomes(c)).value);
    expect(after.outcomes.find((o) => o.id === lo.id)!.text).toBe("Model it my way.");
    expect(after.modules[0]!.outcomes.find((o) => o.id === mo.id)!.text).toBe("Explain it my way.");
  });

  it("refuses to confirm the structure until every change is decided", async () => {
    const { course: sample } = await sampleCourse();
    const course = { ...newCourse("x", "u"), fit: sample.fit.map((f) => ({ ...f, decision: "pending" as const })) };
    expect(allFitDecided(course)).toBe(false);
    expect(() => confirmStructure(course, {})).toThrow(/Decide/);
  });
});

describe("exports (@cg/exports)", () => {
  it("markdown export includes session outcomes and zips", async () => {
    let { course } = await sampleCourse();
    const plan = course.plans[0]!;
    for (const s of plan.sessions) course = applyHourPlan(course, plan.id, s.id, (await mockStages.draftHourPlan(course, plan.id, s.id)).value);
    const files = getExporter().markdown(course);
    const all = Object.values(files).join("\n");
    for (const so of plan.sessions.flatMap((s) => s.sessionOutcomes)) expect(all).toContain(so.id);
    for (const mo of course.modules.flatMap((m) => m.outcomes)) expect(all).toContain(mo.id);
    const zip = zipSync(Object.fromEntries(Object.entries(files).map(([k, v]) => [k, strToU8(v)])));
    expect(Object.keys(unzipSync(zip))).toHaveLength(Object.keys(files).length);
  });

  it("exports slides and the instructor guide as Office files", async () => {
    let { course } = await sampleCourse();
    const plan = course.plans[0]!, s = plan.sessions[0]!;
    course = applyHourPlan(course, plan.id, s.id, (await mockStages.draftHourPlan(course, plan.id, s.id)).value);
    const pptx = await getExporter().slides(course, plan.id, s.id);
    const docx = await getExporter().instructorGuide(course, plan.id, s.id);
    for (const f of [pptx, docx]) expect([...f.slice(0, 2)]).toEqual([0x50, 0x4b]); // zip container
  }, 30000);
});
