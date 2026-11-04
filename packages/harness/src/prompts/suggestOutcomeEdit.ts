import { z } from "zod";
import { BloomLevel, type Course, type EditInstruction, type Outcome } from "@cg/core";
import type { PromptModule } from "./types.js";
import { BLOOM_GUIDE, JSON_RULES, FACTS_RULES, context, json } from "./shared.js";

export interface SuggestEditInput {
  course: Course;
  outcome: Outcome;
  instruction: EditInstruction;
}

export const output = z.object({
  proposed: z.array(z.object({ text: z.string().min(5), bloom: BloomLevel })).min(1).max(2),
  reason: z.string().min(3),
});
export type SuggestEditOutput = z.infer<typeof output>;

export const INSTRUCTION_TEXT: Record<EditInstruction["kind"], string> = {
  raiseBloom: "Raise the Bloom level by one or two levels, keeping the same subject. Change the verb and the task so the higher level is real, not just a new verb.",
  measurable: "Make it measurable: add a condition (given ...) and/or a criterion (to ... standard) so it can be assessed.",
  industryContext: "Add industry context drawn from the selected roles (tools, documents, standards they name).",
  shorten: "Shorten it to the core verb, object and essential condition. Keep the Bloom level.",
  split: "Split it into exactly two outcomes, each assessable on its own.",
  matchHandout: "Match the wording of the handout outcome it came from as closely as possible while keeping a measurable verb.",
  free: "Follow the teacher's instruction.",
};

export const suggestOutcomeEditPrompt: PromptModule<SuggestEditInput, SuggestEditOutput> = {
  id: "outcomes.suggestEdit",
  version: "1",
  system: [
    "You suggest one edit to one learning outcome. The teacher sees your suggestion next to the original before anything is replaced.",
    "Return one proposed outcome (two when splitting) and a one-sentence reason.",
    BLOOM_GUIDE,
    FACTS_RULES,
    JSON_RULES,
  ].join("\n"),
  user: (i) => [
    context("brief", json({ title: i.course.brief.title, audience: i.course.brief.audience, level: i.course.brief.level, industry: i.course.brief.industry })),
    context("modules", i.course.modules.filter((m) => i.outcome.moduleIds.includes(m.id)).map((m) => `${m.id}: ${m.title}`).join("\n")),
    context("roles", i.course.roles.filter((r) => r.selected).map((r) => `${r.id}: ${r.title} | ${r.skills.join(", ")}`).join("\n") || "(none)"),
    context("outcome", `${i.outcome.id} [${i.outcome.bloom}]: ${i.outcome.text}`),
    `Edit: ${INSTRUCTION_TEXT[i.instruction.kind]}`,
    i.instruction.note ? `Teacher's note: ${i.instruction.note}` : "",
    'Return {"proposed":[{"text":"","bloom":"apply"}],"reason":""}.',
  ].filter(Boolean).join("\n"),
  output,
};
