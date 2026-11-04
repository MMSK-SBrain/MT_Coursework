// Builds a realistic course by running the harness MockStages end to end (no database, no network).
import type { Course } from "@cg/core";
import { MockStages } from "@cg/harness";
import { addPlan, applyFit, applyOutcomes, applyParsed, applyRoles, confirmStructure, decideFit, freezeOutcomes, newCourse } from "./course-logic";
import type { CourseMeta } from "./course-meta";

export const mockStages = new MockStages({ now: () => new Date() });

export async function sampleCourse(): Promise<{ course: Course; meta: CourseMeta }> {
  let c = newCourse("c-test", "u-test");
  let m: CourseMeta = {};
  const files = [
    { meta: { id: "f1", kind: "handout" as const, filename: "h.txt", mime: "text/plain", storageKey: "k1" }, bytes: new Uint8Array() },
    { meta: { id: "f2", kind: "moduleSheet" as const, filename: "m.xlsx", mime: "x", storageKey: "k2" }, bytes: new Uint8Array() },
  ];
  const p = await mockStages.parseInputs(files);
  [c, m] = applyParsed(c, m, p.value, p.provenance);
  const r = await mockStages.findRoles(c.brief, c.modules);
  [c, m] = applyRoles(c, m, r.value, r.provenance);
  c = applyFit(c, (await mockStages.proposeFit(c)).value);
  for (const f of c.fit) c = decideFit(c, f.id, f.kind === "trim" ? "rejected" : "accepted");
  [c, m] = confirmStructure(c, m);
  [c, m] = applyOutcomes(c, m, (await mockStages.draftOutcomes(c)).value);
  c = freezeOutcomes(c);
  c = addPlan(c, (await mockStages.draftPlan(c, { path: "classroom", style: "auto" })).value);
  return { course: c, meta: m };
}
