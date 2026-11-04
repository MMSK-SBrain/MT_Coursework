import { z } from "zod";
import { BloomLevel, CourseBrief, Module } from "@cg/core";
import type { PromptModule } from "./types.js";
import { JSON_RULES, FACTS_RULES, clip, context, examplesBlock } from "./shared.js";

export interface ParseInputsInput {
  files: { filename: string; kind: "handout" | "moduleSheet" | "other"; text: string }[];
}

export const output = z.object({
  brief: CourseBrief.partial(),
  modules: z.array(Module).min(1),
  objectives: z.array(z.object({ id: z.string().min(1), text: z.string().min(1) })).default([]),
  outcomes: z.array(z.object({ id: z.string().min(1), text: z.string().min(1), bloom: BloomLevel, moduleIds: z.array(z.string()).default([]) })).default([]),
  gaps: z.array(z.string()).default([]),
});
export type ParseInputsOutput = z.infer<typeof output>;

export const parseInputsPrompt: PromptModule<ParseInputsInput, ParseInputsOutput> = {
  id: "inputs.parse",
  version: "1",
  system: [
    "You extract the structure of a course from a teacher's files. You copy, you do not invent.",
    "A handout gives the brief, objectives (COs), outcomes (LOs) and modules. A module sheet gives modules and hours.",
    "When both are present, merge them into one module list: set foundIn to \"both\", \"handout\" or \"moduleSheet\",",
    "and set note to \"Not in handout\" or \"Not in sheet\" where one source lacks a module. Prefer sheet hours when they disagree, and add a gap describing the disagreement.",
    "Copy objective and outcome wording verbatim. Do not rewrite them, even if the verb is weak.",
    "List in gaps anything empty, missing or contradictory (e.g. \"CO4 and CO5 are empty in the handout\").",
    "Leave brief fields out when the files do not state them.",
    FACTS_RULES,
    JSON_RULES,
  ].join("\n"),
  user: (input, ctx) => [
    examplesBlock(ctx.examples),
    ...input.files.map((f) => context(`${f.kind}: ${f.filename}`, clip(f.text, 24_000))),
    "Return JSON of this shape:",
    `{"brief":{"title":"","code":"","audience":"","level":"school|diploma|ug|pg|professional|vocational","contactHours":0,"industry":"","markets":[""],"textbooks":[""],"notes":""},`,
    ` "modules":[{"id":"M1","title":"","hours":0,"topics":[""],"foundIn":"handout|moduleSheet|both","note":"optional"}],`,
    ` "objectives":[{"id":"CO1","text":""}],`,
    ` "outcomes":[{"id":"LO1","text":"","bloom":"remember|understand|apply|analyse|evaluate|create","moduleIds":["M1"]}],`,
    ` "gaps":[""]}`,
  ].join("\n"),
  output,
};
