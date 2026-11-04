// Content check against session outcomes. One reviewer call per session (not per block) returns a
// verdict with a reason for every (block, SO) pair; blocks scoring below the threshold get one repair,
// done in a single generator call that keeps their timing, kind and SOs fixed.
import type { z } from "zod";
import type { BloomLevel } from "@cg/core";
import type { HarnessConfig, ModelPair } from "./config.js";
import { chatWithFallback, type ChatClient, type ChatMessage, type ChatResult } from "./openrouter.js";
import { fixMessage, parseWith } from "./runner.js";
import {
  VERDICT_SCORE, blockRepairPrompt, contentCheckPrompt,
  type BlockRepairOutput, type CheckedBlock, type ContentCheckInput, type ContentCheckOutput,
} from "./prompts/contentCheck.js";

export interface ContentVerdict {
  block: number;
  so: string;
  verdict: keyof typeof VERDICT_SCORE;
  reason: string;
}

export interface ContentCheckResult {
  verdicts: ContentVerdict[];
  /** Mean verdict over the SOs each block names (blocks serving no SO are left out). */
  blockScores: { block: number; score: number }[];
  /** Per SO: the best verdict any block gives it. An SO is fulfilled when some block fully builds it. */
  soFulfilment: { so: string; best: number; fulfilled: boolean }[];
  /** Mean block score, 0..1 (1 when there is nothing to judge). */
  score: number;
  /** Blocks below the threshold. */
  failing: number[];
  costUsd: number;
  calls: number;
  /** Set when the reviewer's output could not be used; the check is then skipped. */
  skipped?: string;
}

export interface ContentCheckDeps {
  client: ChatClient;
  config: HarnessConfig;
}

type Meter = { cost: number; calls: number; add(r: ChatResult): void };
const meter = (): Meter => ({ cost: 0, calls: 0, add(r) { this.cost += r.costUsd; this.calls++; } });

async function callJson<O>(
  client: ChatClient, models: ModelPair, prompt: { system: string; output: z.ZodType<O, z.ZodTypeDef, unknown> }, user: string,
  opts: { temperature: number; maxTokens: number; json: boolean }, m: Meter,
): Promise<{ ok: true; value: O } | { ok: false; errors: string[] }> {
  const msgs: ChatMessage[] = [{ role: "system", content: prompt.system }, { role: "user", content: user }];
  let last: { ok: false; errors: string[] } = { ok: false, errors: [] };
  for (let i = 0; i < 2; i++) {
    const r = await chatWithFallback(client, models, { ...opts, messages: msgs });
    m.add(r);
    const parsed = parseWith(prompt.output, r.content);
    if (parsed.ok) return parsed;
    last = parsed;
    msgs.push({ role: "assistant", content: r.content }, { role: "user", content: fixMessage(parsed.errors) });
  }
  return last;
}

/** Score the reviewer's verdicts. Pairs the reviewer skipped count as "no" (unproven). */
export function scoreVerdicts(input: ContentCheckInput, verdicts: ContentVerdict[], threshold: number): Omit<ContentCheckResult, "costUsd" | "calls"> {
  const pairs = input.blocks.flatMap((b, block) => b.sessionOutcomeIds.map((so) => ({ block, so })));
  const full: ContentVerdict[] = pairs.map(({ block, so }) =>
    verdicts.find((v) => v.block === block && v.so === so) ?? { block, so, verdict: "no", reason: "not judged by the reviewer" });
  const blockScores = input.blocks.map((b, block) => {
    const mine = full.filter((v) => v.block === block);
    return mine.length ? { block, score: mine.reduce((a, v) => a + VERDICT_SCORE[v.verdict], 0) / mine.length } : null;
  }).filter((x): x is { block: number; score: number } => !!x);
  const soFulfilment = input.sessionOutcomes.map((so) => {
    const best = full.filter((v) => v.so === so.id).reduce((a, v) => Math.max(a, VERDICT_SCORE[v.verdict]), 0);
    return { so: so.id, best, fulfilled: best >= 1 };
  });
  const score = blockScores.length ? blockScores.reduce((a, b) => a + b.score, 0) / blockScores.length : 1;
  return { verdicts: full, blockScores, soFulfilment, score, failing: blockScores.filter((b) => b.score < threshold).map((b) => b.block) };
}

/** One reviewer call for the whole session. */
export async function checkSessionContent(input: ContentCheckInput, deps: ContentCheckDeps): Promise<ContentCheckResult> {
  const m = meter();
  const opts = { temperature: 0, maxTokens: 2500, json: deps.config.jsonMode };
  const r = await callJson<ContentCheckOutput>(deps.client, deps.config.models.review, contentCheckPrompt, contentCheckPrompt.user(input, { examples: "" }), opts, m);
  if (!r.ok) {
    return { verdicts: [], blockScores: [], soFulfilment: [], score: 1, failing: [], costUsd: m.cost, calls: m.calls, skipped: `content check skipped: reviewer output was invalid (${r.errors.slice(0, 2).join("; ")})` };
  }
  return { ...scoreVerdicts(input, r.value.verdicts, deps.config.contentThreshold), costUsd: m.cost, calls: m.calls };
}

/** One generator call rewriting the failing blocks; returns content patches by block index. */
export async function repairBlocks(
  input: ContentCheckInput, check: ContentCheckResult, models: ModelPair, deps: ContentCheckDeps,
): Promise<{ patches: BlockRepairOutput["blocks"]; costUsd: number; calls: number; error?: string }> {
  const m = meter();
  const targets = check.failing.map((block) => ({
    block,
    issues: check.verdicts.filter((v) => v.block === block && v.verdict !== "yes").map((v) => `${v.so} (${v.verdict}): ${v.reason}`),
  }));
  const opts = { temperature: deps.config.temperature, maxTokens: deps.config.maxTokens, json: deps.config.jsonMode };
  const r = await callJson<BlockRepairOutput>(deps.client, models, blockRepairPrompt, blockRepairPrompt.user({ ...input, targets }, { examples: "" }), opts, m);
  if (!r.ok) return { patches: [], costUsd: m.cost, calls: m.calls, error: r.errors.slice(0, 2).join("; ") };
  const wanted = new Set(check.failing);
  return { patches: r.value.blocks.filter((b) => wanted.has(b.block)), costUsd: m.cost, calls: m.calls };
}

export function toCheckInput(
  session: { title: string; sessionOutcomes: { id: string; text: string; bloom: BloomLevel }[] },
  audience: string,
  blocks: CheckedBlock[],
): ContentCheckInput {
  return {
    sessionTitle: session.title,
    audience,
    sessionOutcomes: session.sessionOutcomes.map(({ id, text, bloom }) => ({ id, text, bloom })),
    blocks: blocks.map(({ kind, title, minutes, activity, check, sessionOutcomeIds }) => ({ kind, title, minutes, activity, check, sessionOutcomeIds })),
  };
}
