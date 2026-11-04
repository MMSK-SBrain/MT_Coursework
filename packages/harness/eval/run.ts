// Eval CLI: runs the fixed course briefs through chosen stages for a list of models, scores each
// output with the rubric reviewer plus the code-checked rules, and writes JSON + markdown tables
// to packages/harness/eval-results/ (gitignored).
//
//   pnpm --filter @cg/harness eval -- --models qwen/...,z-ai/... --stages draftOutcomes,proposeFit
//   options: --models a,b   --stages s1,s2   --briefs id1,id2   --judge model   --out dir
import { pathToFileURL } from "node:url";
import type { Course, HourBlock, LearningPlan } from "@cg/core";

const round2 = (n: number) => Math.round(n * 100) / 100;
import { DEFAULT_CONFIG, loadConfig, type HarnessConfig, type StageName } from "../src/config.js";
import { OpenRouterClient, type ChatClient } from "../src/openrouter.js";
import { OpenRouterStages } from "../src/stages.js";
import { reviewDraft } from "../src/runner.js";
import { rollUp } from "../src/checks.js";
import { checkSessionContent, toCheckInput } from "../src/contentCheck.js";
import { FixtureOccupationSource, FixtureLinkSource } from "../src/sources/fixture.js";
import { ExampleStore } from "../src/examples.js";
import { FIT_RUBRIC, HOURPLAN_RUBRIC, OUTCOMES_RUBRIC, PLAN_RUBRIC, type Rubric } from "../src/prompts/review.js";
import { EVAL_COURSES } from "./briefs.js";

export const EVAL_STAGES = ["draftOutcomes", "proposeFit", "draftPlan", "draftHourPlan", "suggestOutcomeEdit"] as const;
export type EvalStage = (typeof EVAL_STAGES)[number];

const RUBRICS: Record<EvalStage, Rubric | null> = {
  draftOutcomes: OUTCOMES_RUBRIC, proposeFit: FIT_RUBRIC, draftPlan: PLAN_RUBRIC, draftHourPlan: HOURPLAN_RUBRIC, suggestOutcomeEdit: null,
};

export interface EvalRow {
  brief: string;
  stage: EvalStage;
  model: string;
  ok: boolean;
  error?: string;
  rubricScore: number | null;
  /** draftHourPlan: share of session outcomes some block fully builds (judge's content check on the final blocks). */
  soFulfilment: number | null;
  /** draftHourPlan: mean block score from the judge's content check, 0..1. */
  contentScore: number | null;
  /** draftPlan: share of module outcomes met by the plan's session outcomes (core roll-up rule). */
  moRollup: number | null;
  /** draftPlan: share of course LOs whose module outcomes are all met. */
  loRollup: number | null;
  ruleWarnings: number;
  warnings: string[];
  calls: number;
  costUsd: number;
  judgeCostUsd: number;
  latencyMs: number;
}

export interface EvalArgs {
  models: string[];
  stages: EvalStage[];
  briefs: string[];
  judge: string;
  outDir: string;
}

export function parseArgs(argv: string[], cfg: HarnessConfig = DEFAULT_CONFIG): EvalArgs {
  const get = (k: string) => {
    const i = argv.indexOf(`--${k}`);
    return i >= 0 ? argv[i + 1] : undefined;
  };
  const list = (v: string | undefined) => v?.split(",").map((s) => s.trim()).filter(Boolean);
  const candidates = [...new Set(Object.entries(cfg.models).filter(([k]) => k !== "review").flatMap(([, m]) => [m.primary, m.fallback].filter((x): x is string => !!x)))];
  const stages = (list(get("stages")) ?? ["draftOutcomes", "proposeFit", "draftHourPlan"]) as EvalStage[];
  const bad = stages.filter((s) => !EVAL_STAGES.includes(s));
  if (bad.length) throw new Error(`unknown stage(s) ${bad.join(", ")}; choose from ${EVAL_STAGES.join(", ")}`);
  return {
    models: list(get("models")) ?? candidates,
    stages,
    briefs: list(get("briefs")) ?? EVAL_COURSES.map((c) => c.id),
    judge: get("judge") ?? cfg.models.review.primary,
    outDir: get("out") ?? decodeURIComponent(new URL("../eval-results/", import.meta.url).pathname),
  };
}

/** Clear the downstream data a stage would produce, so it is generated fresh. */
function inputFor(stage: EvalStage, c: Course): Course {
  if (stage === "draftOutcomes") return { ...c, objectives: [], outcomes: [], outcomesFrozenAt: undefined, modules: c.modules.map((m) => ({ ...m, outcomes: [] })) };
  if (stage === "draftPlan") return { ...c, plans: [] };
  return c;
}

async function runOne(stages: OpenRouterStages, stage: EvalStage, c: Course) {
  const input = inputFor(stage, c);
  switch (stage) {
    case "draftOutcomes": return { r: await stages.draftOutcomes(input), course: input };
    case "proposeFit": return { r: await stages.proposeFit(input), course: input };
    case "draftPlan": return { r: await stages.draftPlan(input, { path: "classroom", style: "auto" }), course: input };
    case "draftHourPlan": {
      const p = input.plans[0]!;
      const s = p.sessions[Math.min(2, p.sessions.length - 1)]!;
      return { r: await stages.draftHourPlan(input, p.id, s.id), course: input };
    }
    case "suggestOutcomeEdit": return { r: await stages.suggestOutcomeEdit(input, input.outcomes[0]!.id, { kind: "measurable", note: "" }), course: input };
  }
}

export async function runEval(args: EvalArgs, deps: { client: ChatClient; env?: Record<string, string | undefined>; log?: (s: string) => void }): Promise<EvalRow[]> {
  const log = deps.log ?? console.log;
  const rows: EvalRow[] = [];
  const courses = EVAL_COURSES.filter((c) => args.briefs.includes(c.id));
  const examples = new ExampleStore();
  for (const model of args.models) {
    const base = loadConfig(deps.env ?? {});
    const config: HarnessConfig = {
      ...base,
      models: Object.fromEntries(Object.keys(base.models).map((k) => [k, k === "review" ? { primary: args.judge } : { primary: model }])) as HarnessConfig["models"],
    };
    const stages = new OpenRouterStages({ client: deps.client, config, roles: new FixtureOccupationSource(), links: new FixtureLinkSource(), examples });
    for (const c of courses) {
      for (const stage of args.stages) {
        const t0 = Date.now();
        const row: EvalRow = { brief: c.id, stage, model, ok: false, rubricScore: null, soFulfilment: null, contentScore: null, moRollup: null, loRollup: null, ruleWarnings: 0, warnings: [], calls: 0, costUsd: 0, judgeCostUsd: 0, latencyMs: 0 };
        try {
          const { r, course } = await runOne(stages, stage, c);
          row.latencyMs = Date.now() - t0;
          row.ok = true;
          row.warnings = r.warnings;
          row.ruleWarnings = r.warnings.length;
          row.costUsd = r.provenance.costUsd;
          row.calls = stages.lastTrace.get(stage as StageName)?.calls ?? 0;
          if (stage === "draftPlan") {
            const ru = rollUp(course, r.value as LearningPlan);
            row.moRollup = ru.moTotal ? round2(ru.moMet / ru.moTotal) : null;
            row.loRollup = ru.loTotal ? round2(ru.loMet / ru.loTotal) : null;
          }
          if (stage === "draftHourPlan") {
            const p = course.plans[0]!;
            const session = p.sessions[Math.min(2, p.sessions.length - 1)]!;
            const check = await checkSessionContent(toCheckInput(session, course.brief.audience, r.value as HourBlock[]), { client: deps.client, config });
            row.judgeCostUsd += check.costUsd;
            if (!check.skipped) {
              row.contentScore = round2(check.score);
              row.soFulfilment = check.soFulfilment.length ? round2(check.soFulfilment.filter((x) => x.fulfilled).length / check.soFulfilment.length) : null;
            }
          }
          const rubric = RUBRICS[stage];
          if (rubric) {
            const ctx = `Course: ${course.brief.title} (${course.brief.level}, ${course.brief.contactHours} h)\nModules: ${course.modules.map((m) => `${m.id} ${m.title}`).join("; ")}\nOutcomes: ${course.outcomes.map((o) => `${o.id} ${o.text}`).join("; ")}\nRoles: ${course.roles.filter((x) => x.selected).map((x) => x.title).join("; ")}`;
            const review = await reviewDraft(rubric, ctx, r.value, { client: deps.client, config });
            row.rubricScore = Math.round(review.score * 100) / 100;
            row.judgeCostUsd += review.costUsd;
          }
        } catch (e) {
          row.latencyMs = Date.now() - t0;
          row.error = (e as Error).message.slice(0, 300);
        }
        rows.push(row);
        log(`${row.ok ? "ok  " : "FAIL"} ${model} ${stage} ${c.id} score=${row.rubricScore ?? "-"} warnings=${row.ruleWarnings} cost=$${row.costUsd.toFixed(5)}${row.error ? ` (${row.error})` : ""}`);
      }
    }
  }
  return rows;
}

export function toMarkdown(rows: EvalRow[], args: EvalArgs, at: string): string {
  const groups = new Map<string, EvalRow[]>();
  for (const r of rows) {
    const k = `${r.stage}\u0000${r.model}`;
    groups.set(k, [...(groups.get(k) ?? []), r]);
  }
  const mean = (xs: number[]) => (xs.length ? xs.reduce((a, b) => a + b, 0) / xs.length : NaN);
  const fmt = (n: number, d = 2) => (Number.isFinite(n) ? n.toFixed(d) : "-");
  const lines = [
    `# Harness eval ${at}`,
    "",
    `Judge: \`${args.judge}\` · Briefs: ${args.briefs.length} · Stages: ${args.stages.join(", ")}`,
    "",
    "## Summary (per stage and model)",
    "",
    "| Stage | Model | OK | Rubric (0-1) | SO fulfilment | Block content | MO roll-up | LO roll-up | Rule warnings | Cost USD (total) | Rubric per cent | Mean latency s |",
    "|---|---|---|---|---|---|---|---|---|---|---|---|",
  ];
  for (const [k, rs] of [...groups].sort()) {
    const [stage, model] = k.split("\u0000");
    const okRows = rs.filter((r) => r.ok);
    const score = mean(okRows.filter((r) => r.rubricScore !== null).map((r) => r.rubricScore!));
    const cost = rs.reduce((a, r) => a + r.costUsd, 0);
    const perCent = cost > 0 && Number.isFinite(score) ? score / (cost * 100 / rs.length) : NaN;
    const m = (k: "soFulfilment" | "contentScore" | "moRollup" | "loRollup") => fmt(mean(okRows.filter((r) => r[k] !== null).map((r) => r[k]!)));
    lines.push(`| ${stage} | \`${model}\` | ${okRows.length}/${rs.length} | ${fmt(score)} | ${m("soFulfilment")} | ${m("contentScore")} | ${m("moRollup")} | ${m("loRollup")} | ${fmt(mean(okRows.map((r) => r.ruleWarnings)), 1)} | ${cost.toFixed(4)} | ${fmt(perCent)} | ${fmt(mean(rs.map((r) => r.latencyMs / 1000)), 1)} |`);
  }
  lines.push("", "## Detail", "", "| Brief | Stage | Model | OK | Rubric | SO fulfilment | MO roll-up | Warnings | Calls | Cost USD | Error |", "|---|---|---|---|---|---|---|---|---|---|---|");
  for (const r of rows) {
    lines.push(`| ${r.brief} | ${r.stage} | \`${r.model}\` | ${r.ok ? "yes" : "no"} | ${r.rubricScore ?? "-"} | ${r.soFulfilment ?? "-"} | ${r.moRollup ?? "-"} | ${r.ruleWarnings} | ${r.calls} | ${r.costUsd.toFixed(5)} | ${(r.error ?? "").replace(/\|/g, "/")} |`);
  }
  lines.push("", "Human review is still required: read a sample of outputs for each winning model before changing `src/config.ts`.");
  return lines.join("\n") + "\n";
}

export async function main(argv: string[], env: Record<string, string | undefined> = process.env, deps: { client?: ChatClient; log?: (s: string) => void; err?: (s: string) => void } = {}): Promise<number> {
  const log = deps.log ?? console.log;
  const err = deps.err ?? console.error;
  if (!deps.client && !env.OPENROUTER_API_KEY) {
    err("eval: OPENROUTER_API_KEY is not set. The eval calls real models on OpenRouter, so it needs a key.\n" +
      "Set it (export OPENROUTER_API_KEY=sk-or-...) and re-run. Nothing was run.");
    return 2;
  }
  let args: EvalArgs;
  try {
    args = parseArgs(argv, loadConfig(env));
  } catch (e) {
    err(`eval: ${(e as Error).message}`);
    return 1;
  }
  const client = deps.client ?? new OpenRouterClient({ apiKey: env.OPENROUTER_API_KEY });
  log(`eval: ${args.models.length} model(s) x ${args.stages.length} stage(s) x ${args.briefs.length} brief(s); judge ${args.judge}`);
  const rows = await runEval(args, { client, env, log });
  const fs = await import("node:fs/promises");
  const path = await import("node:path");
  await fs.mkdir(args.outDir, { recursive: true });
  const at = new Date().toISOString();
  const stamp = at.replace(/[:.]/g, "-");
  const jsonPath = path.join(args.outDir, `eval-${stamp}.json`);
  const mdPath = path.join(args.outDir, `eval-${stamp}.md`);
  await fs.writeFile(jsonPath, JSON.stringify({ at, args, rows }, null, 2));
  await fs.writeFile(mdPath, toMarkdown(rows, args, at));
  log(`eval: wrote ${jsonPath}\neval: wrote ${mdPath}`);
  return rows.some((r) => r.ok) ? 0 : 1;
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  main(process.argv.slice(2)).then((code) => process.exit(code), (e) => {
    console.error(`eval: ${(e as Error).stack ?? e}`);
    process.exit(1);
  });
}
