// Model configuration for every stage. This is the ONLY place model ids live.
//
// !!! The defaults below are PLACEHOLDERS, TO BE CHOSEN BY EVAL (`pnpm --filter @cg/harness eval`).
// !!! They are plausible cheap OpenRouter candidates (Qwen and GLM families), not a decision.
// !!! Check the ids against https://openrouter.ai/models before relying on them, and replace
// !!! them with the per-stage winners on quality per unit of cost.
//
// Every value can be overridden from the environment:
//   CG_MODEL_DEFAULT="primary[,fallback]"        applies to every stage without its own override
//   CG_MODEL_<STAGE>="primary[,fallback]"        e.g. CG_MODEL_DRAFT_OUTCOMES, CG_MODEL_REVIEW
//   CG_RUBRIC_THRESHOLD=0.75                     reviewer score (0..1) below which one repair runs
//   CG_CONTENT_THRESHOLD=0.75                    content-check score (0..1) below which a block gets one repair
//   CG_TEMPERATURE=0.3

export type StageName =
  | "parseInputs" | "findRoles" | "proposeFit" | "draftOutcomes" | "suggestOutcomeEdit"
  | "draftPlan" | "draftHourPlan" | "findFurtherLearning" | "draftCaseStudy"
  /** The rubric reviewer: a stronger, still cheap, model. */
  | "review";

export const STAGE_NAMES: StageName[] = [
  "parseInputs", "findRoles", "proposeFit", "draftOutcomes", "suggestOutcomeEdit",
  "draftPlan", "draftHourPlan", "findFurtherLearning", "draftCaseStudy", "review",
];

export interface ModelPair {
  primary: string;
  fallback?: string;
}

export interface HarnessConfig {
  models: Record<StageName, ModelPair>;
  /** Score in [0, 1]; below it, a reviewed stage gets one automatic repair. */
  rubricThreshold: number;
  /** Content check: a block scoring below this (0..1, mean verdict over its SOs) gets one repair. */
  contentThreshold: number;
  temperature: number;
  /** Ask OpenRouter for `response_format: json_object`. Turn off for models that reject it. */
  jsonMode: boolean;
  maxTokens: number;
}

// TO BE CHOSEN BY EVAL. Placeholders only.
const CANDIDATE_QWEN = "qwen/qwen3-235b-a22b-2507";
const CANDIDATE_GLM = "z-ai/glm-4.6";
const CANDIDATE_QWEN_SMALL = "qwen/qwen3-30b-a3b";

export const DEFAULT_CONFIG: HarnessConfig = {
  models: {
    parseInputs: { primary: CANDIDATE_QWEN, fallback: CANDIDATE_GLM },
    findRoles: { primary: CANDIDATE_QWEN_SMALL, fallback: CANDIDATE_QWEN },
    proposeFit: { primary: CANDIDATE_QWEN, fallback: CANDIDATE_GLM },
    draftOutcomes: { primary: CANDIDATE_QWEN, fallback: CANDIDATE_GLM },
    suggestOutcomeEdit: { primary: CANDIDATE_QWEN_SMALL, fallback: CANDIDATE_QWEN },
    draftPlan: { primary: CANDIDATE_QWEN, fallback: CANDIDATE_GLM },
    draftHourPlan: { primary: CANDIDATE_QWEN, fallback: CANDIDATE_GLM },
    findFurtherLearning: { primary: CANDIDATE_QWEN_SMALL, fallback: CANDIDATE_QWEN },
    draftCaseStudy: { primary: CANDIDATE_GLM, fallback: CANDIDATE_QWEN },
    review: { primary: CANDIDATE_GLM, fallback: CANDIDATE_QWEN },
  },
  rubricThreshold: 0.75,
  contentThreshold: 0.75,
  temperature: 0.3,
  jsonMode: true,
  maxTokens: 4096,
};

function envKey(stage: StageName): string {
  return "CG_MODEL_" + stage.replace(/([a-z])([A-Z])/g, "$1_$2").toUpperCase();
}

export function parseModelPair(v: string): ModelPair {
  const [primary, fallback] = v.split(",").map((s) => s.trim()).filter(Boolean);
  if (!primary) throw new Error(`empty model setting "${v}"`);
  return fallback ? { primary, fallback } : { primary };
}

/** Build the config: defaults, then `overrides`, then environment variables. */
export function loadConfig(
  env: Record<string, string | undefined> = typeof process !== "undefined" ? process.env : {},
  overrides: Partial<HarnessConfig> = {},
): HarnessConfig {
  const cfg: HarnessConfig = {
    ...DEFAULT_CONFIG,
    ...overrides,
    models: { ...DEFAULT_CONFIG.models, ...overrides.models },
  };
  const all = env.CG_MODEL_DEFAULT;
  for (const s of STAGE_NAMES) {
    const v = env[envKey(s)] ?? (s === "review" ? undefined : all);
    if (v) cfg.models[s] = parseModelPair(v);
  }
  if (env.CG_RUBRIC_THRESHOLD) cfg.rubricThreshold = Number(env.CG_RUBRIC_THRESHOLD);
  if (env.CG_CONTENT_THRESHOLD) cfg.contentThreshold = Number(env.CG_CONTENT_THRESHOLD);
  if (env.CG_TEMPERATURE) cfg.temperature = Number(env.CG_TEMPERATURE);
  if (env.CG_JSON_MODE) cfg.jsonMode = env.CG_JSON_MODE !== "0" && env.CG_JSON_MODE !== "false";
  return cfg;
}

export { envKey as modelEnvKey };
