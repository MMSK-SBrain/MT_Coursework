// The stage runner: one narrow call -> JSON validated by zod -> retry once with errors ->
// code-checked rules -> one repair -> optional rubric review -> one repair -> warnings.
import type { z } from "zod";
import type { Generated, Provenance } from "@cg/core";
import type { HarnessConfig, ModelPair, StageName } from "./config.js";
import { chatWithFallback, type ChatClient, type ChatMessage, type ChatResult } from "./openrouter.js";
import type { PromptModule } from "./prompts/types.js";
import { reviewPrompt, rubricScore, type Rubric } from "./prompts/review.js";

export interface RunnerDeps {
  client: ChatClient;
  config: HarnessConfig;
  now?: () => Date;
}

export interface StageTrace {
  calls: number;
  /** Models that answered, in call order. */
  models: string[];
  validationRetries: number;
  ruleProblemsBefore: string[];
  ruleRepair: "none" | "accepted" | "rejected";
  rubric?: { id: string; score: number; issues: string[]; repaired: boolean };
}

export interface StageResult<T> extends Generated<T> {
  trace: StageTrace;
}

export interface StageCall<I, O> {
  stage: StageName;
  prompt: PromptModule<I, O>;
  input: I;
  builtFrom: string[];
  examples?: string;
  /** Code-checked rules. Problems trigger one repair; survivors become warnings. */
  rules?: (o: O) => string[];
  /** Checks that only warn (never trigger a repair), e.g. verbatim handout outcomes. */
  advisories?: (o: O) => string[];
  /** Rubric review for high-stakes stages. */
  rubric?: { rubric: Rubric; contextText: string };
}

export class StageValidationError extends Error {
  constructor(readonly promptId: string, readonly errors: string[], readonly raw: string) {
    super(`${promptId}: model output failed validation after retry: ${errors.slice(0, 5).join("; ")}`);
    this.name = "StageValidationError";
  }
}

/** Pull the first JSON value out of a model reply (tolerates code fences and chatter). */
export function extractJson(text: string): unknown {
  let t = text.trim();
  const fence = t.match(/```(?:json)?\s*([\s\S]*?)```/i);
  if (fence?.[1]) t = fence[1].trim();
  try {
    return JSON.parse(t);
  } catch {
    const start = t.search(/[[{]/);
    if (start < 0) throw new Error("no JSON found in reply");
    const open = t[start]!;
    const close = open === "{" ? "}" : "]";
    const end = t.lastIndexOf(close);
    if (end <= start) throw new Error("unterminated JSON in reply");
    return JSON.parse(t.slice(start, end + 1));
  }
}

export function zodErrors(e: z.ZodError): string[] {
  return e.issues.map((i) => `${i.path.length ? i.path.join(".") : "(root)"}: ${i.message}`);
}

export type Parsed<O> = { ok: true; value: O } | { ok: false; errors: string[] };

export function parseWith<O>(schema: z.ZodType<O, z.ZodTypeDef, unknown>, raw: string): Parsed<O> {
  let data: unknown;
  try {
    data = extractJson(raw);
  } catch (e) {
    return { ok: false, errors: [`invalid JSON: ${(e as Error).message}`] };
  }
  const r = schema.safeParse(data);
  return r.success ? { ok: true, value: r.data } : { ok: false, errors: zodErrors(r.error) };
}

export const fixMessage = (errors: string[]) =>
  `Your JSON did not match the required shape. Errors:\n${errors.map((e) => `- ${e}`).join("\n")}\nReturn the complete corrected JSON object only.`;

const repairMessage = (problems: string[], what: string) =>
  `${what}:\n${problems.map((p) => `- ${p}`).join("\n")}\nFix these problems and nothing else. Keep everything that was correct. Return the complete corrected JSON object only.`;

class Meter {
  cost = 0;
  calls = 0;
  models: string[] = [];
  add(r: ChatResult) {
    this.cost += r.costUsd;
    this.calls++;
    this.models.push(r.model);
  }
}

export async function runStage<I, O>(call: StageCall<I, O>, deps: RunnerDeps): Promise<StageResult<O>> {
  const { client, config } = deps;
  const models = config.models[call.stage];
  const meter = new Meter();
  const chatOpts = { temperature: config.temperature, maxTokens: config.maxTokens, json: config.jsonMode };
  const p = call.prompt;
  const base: ChatMessage[] = [
    { role: "system", content: p.system },
    { role: "user", content: p.user(call.input, { examples: call.examples ?? "" }) },
  ];

  let validationRetries = 0;
  // One attempt = a call plus one retry with the validation errors appended.
  const attempt = async (pair: ModelPair) => {
    const r1 = await chatWithFallback(client, pair, { ...chatOpts, messages: base });
    meter.add(r1);
    const p1 = parseWith(p.output, r1.content);
    if (p1.ok) return { value: p1.value, model: r1.model, convo: [...base, { role: "assistant", content: r1.content }] as ChatMessage[] };
    validationRetries++;
    const msgs: ChatMessage[] = [...base, { role: "assistant", content: r1.content }, { role: "user", content: fixMessage(p1.errors) }];
    const r2 = await chatWithFallback(client, { primary: r1.model }, { ...chatOpts, messages: msgs });
    meter.add(r2);
    const p2 = parseWith(p.output, r2.content);
    if (p2.ok) return { value: p2.value, model: r2.model, convo: [...msgs, { role: "assistant", content: r2.content }] as ChatMessage[] };
    throw new StageValidationError(p.id, p2.errors, r2.content);
  };

  let got: Awaited<ReturnType<typeof attempt>>;
  try {
    got = await attempt(models);
  } catch (e) {
    // Both tries on the primary produced invalid output: give the fallback model one full attempt.
    if (!(e instanceof StageValidationError) || !models.fallback) throw e;
    got = await attempt({ primary: models.fallback });
  }
  let { value, model, convo } = got;

  // One repair with the given problems; accepted only if valid and not worse on the rules.
  const repair = async (problems: string[], what: string): Promise<O | null> => {
    const msgs: ChatMessage[] = [...convo, { role: "user", content: repairMessage(problems, what) }];
    const r = await chatWithFallback(client, { primary: model, fallback: models.fallback }, { ...chatOpts, messages: msgs });
    meter.add(r);
    const parsed = parseWith(p.output, r.content);
    if (!parsed.ok) return null;
    convo = [...msgs, { role: "assistant", content: r.content }];
    model = r.model;
    return parsed.value;
  };

  const rules = call.rules ?? (() => []);
  const problemsBefore = rules(value);
  let ruleRepair: StageTrace["ruleRepair"] = "none";
  if (problemsBefore.length) {
    const fixed = await repair(problemsBefore, "These rule checks failed (checked in code)");
    if (fixed && rules(fixed).length < problemsBefore.length) {
      value = fixed;
      ruleRepair = "accepted";
    } else ruleRepair = "rejected";
  }

  const warnings: string[] = [];
  let rubricTrace: StageTrace["rubric"];
  if (call.rubric) {
    const review = await reviewDraft(call.rubric.rubric, call.rubric.contextText, value, deps, meter);
    rubricTrace = { id: call.rubric.rubric.id, score: review.score, issues: review.issues, repaired: false };
    if (review.score < config.rubricThreshold) {
      const issues = review.issues.length ? review.issues : ["The reviewer scored this draft below the quality bar; improve it against the rubric."];
      const fixed = await repair(issues, `A reviewer scored this draft ${review.score.toFixed(2)} against the rubric (threshold ${config.rubricThreshold}). Reviewer's issues`);
      if (fixed && rules(fixed).length <= rules(value).length) {
        value = fixed;
        rubricTrace.repaired = true;
      } else warnings.push(`Reviewer score ${review.score.toFixed(2)} is below ${config.rubricThreshold} and the automatic repair did not help.`);
    }
  }

  warnings.unshift(...rules(value), ...(call.advisories?.(value) ?? []));

  const provenance: Provenance = {
    model,
    promptId: p.id,
    promptVersion: p.version,
    costUsd: round6(meter.cost),
    createdAt: (deps.now?.() ?? new Date()).toISOString(),
    builtFrom: [...new Set(call.builtFrom)],
  };
  return {
    value,
    provenance,
    warnings,
    trace: {
      calls: meter.calls,
      models: meter.models,
      validationRetries,
      ruleProblemsBefore: problemsBefore,
      ruleRepair,
      ...(rubricTrace ? { rubric: rubricTrace } : {}),
    },
  };
}

/** Score a draft against a rubric with the reviewer model. Also used by the eval CLI. */
export async function reviewDraft(
  rubric: Rubric,
  contextText: string,
  draft: unknown,
  deps: RunnerDeps,
  meter?: { add(r: ChatResult): void },
): Promise<{ score: number; issues: string[]; costUsd: number }> {
  const { client, config } = deps;
  const msgs: ChatMessage[] = [
    { role: "system", content: reviewPrompt.system },
    { role: "user", content: reviewPrompt.user({ rubric, contextText, draft }, { examples: "" }) },
  ];
  const opts = { temperature: 0, maxTokens: 4096, json: config.jsonMode };
  let cost = 0;
  for (let i = 0; i < 2; i++) {
    const r = await chatWithFallback(client, config.models.review, { ...opts, messages: msgs });
    meter?.add(r);
    cost += r.costUsd;
    const parsed = parseWith(reviewPrompt.output, r.content);
    if (parsed.ok) return { score: rubricScore(rubric, parsed.value), issues: parsed.value.issues, costUsd: cost };
    msgs.push({ role: "assistant", content: r.content }, { role: "user", content: fixMessage(parsed.errors) });
  }
  // A broken reviewer must not block generation: treat as passing, and say so.
  return { score: 1, issues: ["reviewer output was invalid; review skipped"], costUsd: cost };
}

function round6(n: number) {
  return Math.round(n * 1e6) / 1e6;
}

/** Combine the provenance of several runner calls that make up one stage result. */
export function mergeProvenance(main: Provenance, ...others: Provenance[]): Provenance {
  return {
    ...main,
    costUsd: round6(others.reduce((a, o) => a + o.costUsd, main.costUsd)),
    builtFrom: [...new Set([main, ...others].flatMap((o) => o.builtFrom))],
  };
}
