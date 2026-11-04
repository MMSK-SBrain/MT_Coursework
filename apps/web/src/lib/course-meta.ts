// App-only course state that has no place in the core Course model yet.
// Stored next to the course in courses.meta (jsonb). See the final report for the core changes that would remove it.
import { z } from "zod";
import { Module, Provenance } from "@cg/core";

export const CourseMeta = z.object({
  /** Which inputs the teacher starts from (Stage 1 option buttons). */
  startMode: z.enum(["handout", "moduleSheet", "both"]).optional(),
  /** Stage 1: gaps found while reading the inputs, e.g. "CO4 and CO5 are empty in the handout". */
  inputGaps: z.array(z.string()).optional(),
  /** Stage 2: the role-search keywords and how many postings were read. */
  keywords: z.array(z.string()).optional(),
  postingsRead: z.number().optional(),
  /** Stage 3: modules as they were before the first structure confirmation; confirmations re-apply decisions onto these. */
  baseModules: z.array(Module).optional(),
  /** Stage 4: the structure version the current outcome draft was made from. */
  outcomesDraftedFor: z.number().optional(),
  /** Provenance for generated lists that carry none in the core model (modules, roles). Keyed by stage. */
  provenance: z.record(Provenance).optional(),
  /** Code-checked warnings from the last generation, keyed by stage or item path. */
  warnings: z.record(z.array(z.string())).optional(),
});
export type CourseMeta = z.infer<typeof CourseMeta>;
