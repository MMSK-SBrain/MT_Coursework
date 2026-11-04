import { describe, expect, it } from "vitest";
import { confirmStructure, decideFit, editOutcomeText, reopenStructure, unfreezeOutcomes } from "./course-logic";
import { markStale, staleSessionCount } from "./stale";
import { sampleCourse } from "./test-fixtures";

describe("stale marking", () => {
  it("marks nothing when nothing upstream changed", async () => {
    const { course } = await sampleCourse();
    const next = { ...course, brief: { ...course.brief, notes: "x" } };
    expect(staleSessionCount(markStale(course, next))).toBe(0);
  });

  it("marks only sessions that teach an edited outcome", async () => {
    const { course } = await sampleCourse();
    const plan = course.plans[0]!;
    const teachingLO2 = plan.sessions.filter((s) => s.outcomeIds.includes("LO2")).map((s) => s.id);
    expect(teachingLO2.length).toBeGreaterThan(0);
    const unfrozen = unfreezeOutcomes(course);
    const edited = editOutcomeText(unfrozen, "LO2", "Write verifiable requirements for a BMS.");
    const after = markStale(unfrozen, edited);
    const stale = after.plans[0]!.sessions.filter((s) => s.stale).map((s) => s.id);
    expect(stale.sort()).toEqual(teachingLO2.sort());
  });

  it("marks sessions whose outcomes sit in a module changed by a new structure", async () => {
    const { course, meta } = await sampleCourse();
    // Reopen, accept the trim on M1 that was rejected before, confirm again: M1 changes.
    let c = reopenStructure(course);
    const trim = c.fit.find((f) => f.kind === "trim")!;
    c = decideFit(c, trim.id, "accepted");
    const [confirmed] = confirmStructure(c, meta);
    expect(confirmed.structureVersion).toBe(course.structureVersion + 1);
    const after = markStale(course, confirmed);
    const onM1 = new Set(course.outcomes.filter((o) => o.moduleIds.includes("M1")).map((o) => o.id));
    for (const s of after.plans[0]!.sessions) expect(s.stale).toBe(s.outcomeIds.some((id) => onM1.has(id)));
    expect(staleSessionCount(after)).toBeGreaterThan(0);
  });

  it("keeps sessions stale until they are rebuilt", async () => {
    const { course } = await sampleCourse();
    const once = markStale(course, editOutcomeText(course, "LO1", "Describe the systems engineering life cycle."));
    const back = markStale(once, editOutcomeText(once, "LO1", course.outcomes[0]!.text));
    expect(staleSessionCount(back)).toBe(staleSessionCount(once));
  });
});
