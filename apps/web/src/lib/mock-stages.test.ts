import {
  CaseStudy, Course, FitChange, FurtherLink, HourBlock, JobRole, LearningPlan, OutcomeSuggestion, hourBlockProblems, outcomeVerbProblem,
  uncoveredOutcomes,
} from "@cg/core";
import { unzipSync, strToU8, zipSync } from "fflate";
import { describe, expect, it } from "vitest";
import { acceptSuggestion, allFitDecided, applyHourPlan, applyOutcomes, confirmStructure, newCourse, setLocked } from "./course-logic";
import { mockExporter } from "./mock-exporter";
import { mockStages } from "./mock-stages";
import { sampleCourse } from "./test-fixtures";

describe("mock stages return schema-valid data", () => {
  it("runs the whole flow into a valid Course", async () => {
    const { course } = await sampleCourse();
    expect(() => Course.parse(course)).not.toThrow();
    expect(course.modules).toHaveLength(8);
    expect(course.roles.every((r) => JobRole.safeParse(r).success)).toBe(true);
    expect(course.fit.every((f) => FitChange.safeParse(f).success)).toBe(true);
    expect(course.structureVersion).toBe(2);
    expect(course.outcomes.map((o) => outcomeVerbProblem(o))).toEqual(course.outcomes.map(() => null));
    expect(LearningPlan.safeParse(course.plans[0]).success).toBe(true);
    expect(uncoveredOutcomes(course, course.plans[0]!)).toEqual([]);
  });

  it("hour-wise plans add up for every session length", async () => {
    const { course } = await sampleCourse();
    for (const minutes of [5, 8, 45, 60, 90, 120, 150]) {
      const plan = course.plans[0]!;
      const c = { ...course, plans: [{ ...plan, sessions: plan.sessions.map((s, i) => (i === 0 ? { ...s, minutes } : s)) }] };
      const g = await mockStages.draftHourPlan(c, plan.id, plan.sessions[0]!.id);
      expect(g.value.every((b) => HourBlock.safeParse(b).success)).toBe(true);
      expect(hourBlockProblems(g.value, minutes)).toEqual([]);
    }
  });

  it("drafting the hour plan clears the stale flag", async () => {
    const { course } = await sampleCourse();
    const plan = course.plans[0]!;
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
    const kinds = ["raiseBloom", "measurable", "industryContext", "shorten", "split", "matchHandout", "free"] as const;
    for (const kind of kinds) {
      const g = await mockStages.suggestOutcomeEdit(course, "LO1", { kind, note: "focus on the BMS capstone" });
      expect(OutcomeSuggestion.safeParse(g.value).success).toBe(true);
    }
    const up = await mockStages.suggestOutcomeEdit(course, "LO1", { kind: "raiseBloom", note: "" });
    expect(up.value.proposed[0]!.bloom).toBe("apply");
    const split = await mockStages.suggestOutcomeEdit(course, "LO2", { kind: "split", note: "" });
    const after = acceptSuggestion(course, split.value, split.provenance);
    expect(after.outcomes.map((o) => o.id)).toContain("LO2b");
    expect(() => Course.parse(after)).not.toThrow();
  });

  it("keeps locked outcomes when redrafting", async () => {
    const { course, meta } = await sampleCourse();
    const locked = setLocked({ ...course, outcomes: course.outcomes.map((o) => (o.id === "LO3" ? { ...o, text: "Model it my way." } : o)) }, "LO3", true);
    const [c] = applyOutcomes(locked, meta, (await mockStages.draftOutcomes(locked)).value);
    expect(c.outcomes.find((o) => o.id === "LO3")!.text).toBe("Model it my way.");
  });

  it("refuses to confirm the structure until every change is decided", async () => {
    const c = newCourse("x", "u");
    const fit = (await mockStages.proposeFit({ ...c, modules: [] })).value;
    const course = { ...c, fit };
    expect(allFitDecided(course)).toBe(false);
    expect(() => confirmStructure(course, {})).toThrow(/Decide/);
  });

  it("exports markdown files that zip", async () => {
    const { course } = await sampleCourse();
    const files = mockExporter.markdown(course);
    expect(Object.keys(files)).toEqual(expect.arrayContaining(["README.md", "modules.md", "outcomes.md"]));
    expect(Object.keys(files).filter((f) => f.startsWith("plans/")).length).toBe(course.plans[0]!.sessions.length + 1);
    const zip = zipSync(Object.fromEntries(Object.entries(files).map(([k, v]) => [k, strToU8(v)])));
    expect(Object.keys(unzipSync(zip))).toHaveLength(Object.keys(files).length);
    await expect(mockExporter.slides(course, "p", "s")).rejects.toThrow(/@cg\/exports/);
  });
});
