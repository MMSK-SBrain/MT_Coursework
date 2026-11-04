// Builds a realistic course by running the mock stages end to end (no database).
import type { Course } from "@cg/core";
import { addPlan, applyFit, applyOutcomes, applyParsed, applyRoles, confirmStructure, decideFit, freezeOutcomes, newCourse } from "./course-logic";
import type { CourseMeta } from "./course-meta";
import { mockStages } from "./mock-stages";

process.env.MOCK_DELAY_MS = "0";

export async function sampleCourse(): Promise<{ course: Course; meta: CourseMeta }> {
  let c = newCourse("c-test", "u-test");
  let m: CourseMeta = {};
  const files = [
    { meta: { id: "f1", kind: "handout" as const, filename: "h.docx", mime: "x", storageKey: "k1" }, bytes: new Uint8Array() },
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
