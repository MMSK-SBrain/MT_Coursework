// Content check against session outcomes: the main quality gate for cheap models.
// One reviewer call per session judges every (block, SO) pair; one generator call repairs the
// blocks that fall below the threshold, keeping their timing and SOs fixed.
import { z } from "zod";
import type { BloomLevel, HourBlock } from "@cg/core";
import type { PromptModule } from "./types.js";
import { BLOOM_GUIDE, JSON_RULES, FACTS_RULES, context } from "./shared.js";

export interface CheckedBlock {
  kind: HourBlock["kind"];
  title: string;
  minutes: number;
  activity: string;
  check: string[];
  sessionOutcomeIds: string[];
}

export interface ContentCheckInput {
  sessionTitle: string;
  audience: string;
  sessionOutcomes: { id: string; text: string; bloom: BloomLevel }[];
  blocks: CheckedBlock[];
}

export const VERDICT_SCORE = { yes: 1, partly: 0.5, no: 0 } as const;

export const contentCheckOutput = z.object({
  verdicts: z.array(z.object({
    block: z.number().int().nonnegative(),
    so: z.string().min(1),
    verdict: z.enum(["yes", "partly", "no"]),
    reason: z.string().min(3).max(300),
  })),
});
export type ContentCheckOutput = z.infer<typeof contentCheckOutput>;

const renderBlocks = (blocks: CheckedBlock[]) =>
  blocks.map((b, n) => `[${n}] ${b.kind}, ${b.minutes} min, serves ${b.sessionOutcomeIds.join(", ") || "(none)"}: ${b.title}\n    activity: ${b.activity}${b.check.length ? `\n    checks: ${b.check.join(" | ")}` : ""}`).join("\n");

export const contentCheckPrompt: PromptModule<ContentCheckInput, ContentCheckOutput> = {
  id: "session.contentCheck",
  version: "1",
  system: [
    "You are a strict instructional designer checking a lesson plan written by another model.",
    "For every block [n] and every session outcome (SO) that block says it serves, judge whether the block's content, as written, would let a learner achieve that SO at its Bloom level.",
    "verdict: \"yes\" (the activity makes learners do what the SO says, at that level), \"partly\" (on topic but too shallow, too vague or too short for the SO), \"no\" (the block does not build the SO).",
    "Judge the block's own contribution; a hook only needs to set up its SO, a check block must actually test it. An apply-level SO needs learners practising, not watching.",
    "reason: one sentence naming what is missing or what works.",
    "Return one verdict per (block, SO) pair named in the plan. Skip blocks that serve no SO.",
    BLOOM_GUIDE,
    JSON_RULES,
  ].join("\n"),
  user: (i) => [
    context("session", `${i.sessionTitle}\nAudience: ${i.audience}`),
    context("session outcomes", i.sessionOutcomes.map((o) => `${o.id} [${o.bloom}]: ${o.text}`).join("\n")),
    context("blocks", renderBlocks(i.blocks)),
    'Return {"verdicts":[{"block":0,"so":"S1.SO1","verdict":"yes|partly|no","reason":""}]}.',
  ].join("\n"),
  output: contentCheckOutput,
};

export interface BlockRepairInput extends ContentCheckInput {
  targets: { block: number; issues: string[] }[];
}

export const blockRepairOutput = z.object({
  blocks: z.array(z.object({
    block: z.number().int().nonnegative(),
    title: z.string().min(2),
    activity: z.string().min(3),
    check: z.array(z.string()).default([]),
  })).min(1),
});
export type BlockRepairOutput = z.infer<typeof blockRepairOutput>;

export const blockRepairPrompt: PromptModule<BlockRepairInput, BlockRepairOutput> = {
  id: "session.blockRepair",
  version: "1",
  system: [
    "You rewrite specific blocks of a lesson plan so that each one lets learners achieve the session outcomes (SOs) it serves.",
    "A reviewer explained what is missing. Fix exactly that: make the activity concrete (materials, prompts, grouping, the output learners produce) and pitch it at the SO's Bloom level.",
    "Do not change a block's timing, kind or SOs; you only return its new title, activity and quick-check questions.",
    FACTS_RULES,
    JSON_RULES,
  ].join("\n"),
  user: (i) => [
    context("session", `${i.sessionTitle}\nAudience: ${i.audience}`),
    context("session outcomes", i.sessionOutcomes.map((o) => `${o.id} [${o.bloom}]: ${o.text}`).join("\n")),
    context("current plan", renderBlocks(i.blocks)),
    context("blocks to rewrite", i.targets.map((t) => `[${t.block}]\n${t.issues.map((x) => `- ${x}`).join("\n")}`).join("\n")),
    'Return {"blocks":[{"block":0,"title":"","activity":"","check":[""]}]} with one entry per block to rewrite.',
  ].join("\n"),
  output: blockRepairOutput,
};
