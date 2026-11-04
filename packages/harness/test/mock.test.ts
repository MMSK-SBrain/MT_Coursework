import { describe, expect, it } from "vitest";
import {
  CaseStudy, Course as CourseSchema, FitChange, FurtherLink, HourBlock, JobRole, LearningPlan, Objective, Outcome, OutcomeSuggestion,
  hourBlockProblems, outcomeVerbProblem, uncoveredOutcomes, videoAllowed, type LearningPath,
} from "@cg/core";
import { MockStages } from "../src/mock.js";
import { aezc517Course, MODULES } from "../src/fixtures/aezc517.js";
import { EVAL_COURSES } from "../eval/briefs.js";

const m = new MockStages();

describe("MockStages", () => {
  const course = aezc517Course();

  it("produces schema-valid AEZC517 data for stages 1-4", async () => {
    const p = await m.parseInputs([{ meta: { id: "h", kind: "handout", filename: "h.docx", mime: "x", storageKey: "h" }, bytes: new Uint8Array() }]);
    expect(p.value.modules).toHaveLength(8);
    p.value.outcomes.forEach((o) => Outcome.parse(o));
    const roles = await m.findRoles(course.brief, MODULES);
    roles.value.roles.forEach((r) => JobRole.parse(r));
    expect(roles.value.postingsRead).toBe(412);
    const fit = await m.proposeFit(course);
    fit.value.forEach((f) => FitChange.parse(f));
    expect(fit.value.some((f) => f.academicConflict)).toBe(true);
    const oc = await m.draftOutcomes(course);
    oc.value.objectives.forEach((o) => Objective.parse(o));
    oc.value.outcomes.forEach((o) => {
      Outcome.parse(o);
      expect(outcomeVerbProblem(o)).toBeNull();
    });
  });

  it("suggestions pass the verb rules for every instruction kind", async () => {
    for (const kind of ["raiseBloom", "measurable", "industryContext", "shorten", "split", "matchHandout", "free"] as const) {
      for (const o of course.outcomes) {
        const s = await m.suggestOutcomeEdit(course, o.id, { kind, note: "for freshers" });
        OutcomeSuggestion.parse(s.value);
        for (const p of s.value.proposed) expect(outcomeVerbProblem(p), `${kind} ${o.id}: ${p.text}`).toBeNull();
        if (kind === "split") expect(s.value.proposed).toHaveLength(2);
      }
    }
  });

  it("plans cover every outcome and obey video rules for every path", async () => {
    const paths: LearningPath[] = ["classroom", "lab", "bootcamp", "flipped", "blended", "cohort", "elearning", "micro", "youtube", "shorts"];
    for (const path of paths) {
      const plan = (await m.draftPlan(course, { path, style: "auto" })).value;
      LearningPlan.parse(plan);
      expect(uncoveredOutcomes(course, plan), path).toEqual([]);
      for (const s of plan.sessions) expect(videoAllowed(path, s.video), `${path} ${s.video}`).toBe(true);
    }
  });

  it("hour plans add up for every session of every eval course, plus links and case studies", async () => {
    for (const c of [course, ...EVAL_COURSES]) {
      for (const path of ["classroom", "youtube", "shorts", "bootcamp"] as LearningPath[]) {
        const plan = (await m.draftPlan(c, { path, style: "auto" })).value;
        const withPlan = CourseSchema.parse({ ...c, plans: [plan] });
        for (const s of plan.sessions.slice(0, 3)) {
          const blocks = (await m.draftHourPlan(withPlan, plan.id, s.id)).value;
          blocks.forEach((b) => HourBlock.parse(b));
          expect(hourBlockProblems(blocks, s.minutes), `${c.id} ${path} ${s.id}`).toEqual([]);
        }
      }
    }
    const links = await m.findFurtherLearning(course, "p1", "s3");
    links.value.forEach((l) => FurtherLink.parse(l));
    for (const label of ["real", "composite"] as const) {
      const cs = (await m.draftCaseStudy(course, "p1", "s3", label)).value;
      CaseStudy.parse(cs);
      expect(cs.label).toBe(label);
      if (label === "real") expect(cs.sources.length).toBeGreaterThan(0);
    }
  });

  it("is deterministic and costs nothing", async () => {
    const a = await m.draftHourPlan(course, "p1", "s3");
    const b = await new MockStages().draftHourPlan(course, "p1", "s3");
    expect(a).toEqual(b);
    expect(a.provenance).toMatchObject({ model: "mock", costUsd: 0, promptId: "session.hourPlan" });
  });
});
