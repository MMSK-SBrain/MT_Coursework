import type { z } from "zod";

/** Per-call context the runner adds to every prompt. */
export interface PromptContext {
  /** Few-shot worked examples, already rendered as text (may be empty). */
  examples: string;
}

/**
 * One versioned prompt. Bump `version` whenever `system`, `user` or `output` changes,
 * and re-run the eval set. The version is stored in every output's provenance.
 */
export interface PromptModule<I, O> {
  id: string;
  version: string;
  system: string;
  user(input: I, ctx: PromptContext): string;
  /** The JSON shape the model must return (a draft; ids and provenance are added in code). */
  output: z.ZodType<O, z.ZodTypeDef, unknown>;
}
