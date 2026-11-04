import { Course, learningOutcomeCoverage, moduleOutcomeCoverage, outcomeVerbProblem, sessionOutcomeProblems } from "@cg/core";
import { describe, expect, it } from "vitest";
import { acceptSuggestion, addPlan, applyHourPlan, confirmStructure, courseForSuggestion, editOutcomeText, reopenStructure, setLocked } from "./course-logic";
import { mockStages } from "./test-fixtures";
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
    // A module outcome that some session outcome serves.
    const target = course.modules.flatMap((m) => m.outcomes).find((mo) => course.plans[0]!.sessions.some((s) => s.sessionOutcomes.some((so) => so.moduleOutcomeIds.includes(mo.id))))!;
    const edited = editOutcomeText(course, target.id, "Write requirements for a BMS.");
    expect(edited.modules.flatMap((m) => m.outcomes).find((o) => o.id === target.id)!.text).toBe("Write requirements for a BMS.");
    const after = markStale(course, edited);
    const serving = course.plans[0]!.sessions.filter((s) => s.sessionOutcomes.some((so) => so.moduleOutcomeIds.includes(target.id))).map((s) => s.id);
    expect(serving.length).toBeGreaterThan(0);
    expect(after.plans[0]!.sessions.filter((s) => s.stale).map((s) => s.id).sort()).toEqual(serving.sort());
  });

  it("module outcomes lock, and accept suggested rewrites (including splits)", async () => {
    const { course } = await sampleCourse();
    const mod = course.modules.find((m) => m.outcomes.length > 0)!;
    const mo = mod.outcomes[0]!;
    const locked = setLocked(course, mo.id, true);
    expect(editOutcomeText(locked, mo.id, "Changed.").modules.find((m) => m.id === mod.id)!.outcomes[0]!.text).toBe(mo.text);
    const g = await mockStages.suggestOutcomeEdit(courseForSuggestion(course, mo.id), mo.id, { kind: "split", note: "" });
    const after = acceptSuggestion(course, g.value, g.provenance);
    const ids = after.modules.find((m) => m.id === mod.id)!.outcomes.map((o) => o.id);
    expect(ids.slice(0, g.value.proposed.length)).toEqual(g.value.proposed.map((_, i) => (i === 0 ? mo.id : `${mo.id}${String.fromCharCode(97 + i)}`)));
    expect(() => Course.parse(after)).not.toThrow();
  });

  it("re-confirming the structure keeps the module outcomes", async () => {
    const { course, meta } = await sampleCourse();
    const before = course.modules.map((m) => m.outcomes.map((o) => o.id));
    const [again] = confirmStructure(reopenStructure(course), meta);
    expect(again.modules.map((m) => m.outcomes.map((o) => o.id))).toEqual(before);
  });
});
