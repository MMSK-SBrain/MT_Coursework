import { Course, learningOutcomeCoverage, moduleOutcomeCoverage, outcomeVerbProblem, sessionOutcomeProblems } from "@cg/core";
import { describe, expect, it } from "vitest";
import { acceptSuggestion, addPlan, applyHourPlan, editOutcomeText, setLocked } from "./course-logic";
import { mockStages } from "./mock-stages";
import { markStale } from "./stale";
import { sampleCourse } from "./test-fixtures";

/** The sample course with an hour-wise plan drafted for every session of every plan. */
async function fullyBuilt(paths: ("classroom" | "youtube" | "flipped" | "micro")[] = ["classroom"]) {
  let { course } = await sampleCourse();
  for (const path of paths.filter((p) => p !== "classroom")) course = addPlan(course, (await mockStages.draftPlan(course, { path, style: "auto" })).value);
  for (const plan of course.plans) {
    for (const s of plan.sessions) course = applyHourPlan(course, plan.id, s.id, (await mockStages.draftHourPlan(course, plan.id, s.id)).value);
  }
  return course;
}

describe("LO > MO > SO hierarchy in the sample course", () => {
  it("every module has module outcomes with measurable verbs, linked to known LOs", async () => {
    const { course } = await sampleCourse();
    const los = new Set(course.outcomes.map((o) => o.id));
    for (const m of course.modules) {
      expect(m.outcomes.length, m.id).toBeGreaterThan(0);
      for (const mo of m.outcomes) {
        expect(outcomeVerbProblem(mo), mo.id).toBeNull();
        expect(mo.outcomeIds.length).toBeGreaterThan(0);
        expect(mo.outcomeIds.every((id) => los.has(id))).toBe(true);
      }
    }
  });

  it("passes sessionOutcomeProblems with no problems, for every path and session length", async () => {
    const course = await fullyBuilt(["classroom", "youtube", "flipped", "micro"]);
    expect(() => Course.parse(course)).not.toThrow();
    for (const plan of course.plans) {
      for (const s of plan.sessions) {
        expect(s.sessionOutcomes.length, `${plan.path}/${s.id}`).toBeGreaterThan(0);
        expect(sessionOutcomeProblems(s), `${plan.path}/${s.id}`).toEqual([]);
      }
    }
  });

  it("every module outcome and learning outcome is met by the classroom plan", async () => {
    const course = await fullyBuilt();
    const plan = course.plans[0]!;
    expect(moduleOutcomeCoverage(course, plan).filter((m) => !m.met)).toEqual([]);
    expect(learningOutcomeCoverage(course, plan).every((l) => l.met)).toBe(true);
  });

  it("editing a module outcome marks the sessions whose SOs serve it stale", async () => {
    const course = await fullyBuilt();
    const edited = editOutcomeText(course, "M3.MO1", "Write requirements for a BMS.");
    expect(edited.modules.find((m) => m.id === "M3")!.outcomes[0]!.text).toBe("Write requirements for a BMS.");
    const after = markStale(course, edited);
    const serving = course.plans[0]!.sessions.filter((s) => s.sessionOutcomes.some((so) => so.moduleOutcomeIds.includes("M3.MO1"))).map((s) => s.id);
    expect(serving.length).toBeGreaterThan(0);
    expect(after.plans[0]!.sessions.filter((s) => s.stale).map((s) => s.id).sort()).toEqual(serving.sort());
  });

  it("module outcomes lock, and accept suggested rewrites (including splits)", async () => {
    const { course } = await sampleCourse();
    const locked = setLocked(course, "M4.MO1", true);
    expect(editOutcomeText(locked, "M4.MO1", "Changed.").modules.find((m) => m.id === "M4")!.outcomes[0]!.text).toBe(course.modules[3]!.outcomes[0]!.text);
    const g = await mockStages.suggestOutcomeEdit(course, "M7.MO1", { kind: "split", note: "" });
    const after = acceptSuggestion(course, g.value, g.provenance);
    expect(after.modules.find((m) => m.id === "M7")!.outcomes.map((o) => o.id)).toEqual(["M7.MO1", "M7.MO1b", "M7.MO2"]);
    expect(() => Course.parse(after)).not.toThrow();
  });
});
