// Rubric review: a reviewer model scores a draft against a stage rubric.
import { z } from "zod";
import type { PromptModule } from "./types.js";
import { BLOOM_GUIDE, JSON_RULES, context } from "./shared.js";

export interface RubricCriterion {
  id: string;
  description: string;
}

export interface Rubric {
  id: string;
  version: string;
  criteria: RubricCriterion[];
}

export const OUTCOMES_RUBRIC: Rubric = {
  id: "rubric.outcomes",
  version: "1",
  criteria: [
    { id: "measurable", description: "Each outcome starts with one measurable verb and names an observable performance someone could assess." },
    { id: "bloomFit", description: "Bloom levels match the verbs and the audience (apply or higher for vocational/professional learners), and the set climbs sensibly." },
    { id: "coverage", description: "Every module is covered; outcomes map to objectives; nothing important in the modules or accepted fit changes is missing." },
    { id: "specific", description: "Outcomes are specific to this course and its industry (tools, documents, standards from the context), not generic templates." },
    { id: "atomic", description: "One outcome = one skill. No chains of unrelated skills joined by 'and'. 4-10 outcomes in total." },
    { id: "grounded", description: "No invented facts, standards or tools that are not in the supplied context; locked items unchanged." },
  ],
};

export const FIT_RUBRIC: Rubric = {
  id: "rubric.fit",
  version: "2",
  criteria: [
    { id: "evidence", description: "Each change is justified by the selected roles' ESCO skills (covered or missing) as given; no invented numbers or demand claims." },
    { id: "specific", description: "Change text is a concrete topic or activity, not a generic theme." },
    { id: "targeted", description: "Each change targets the right module and its kind (add/strengthen/trim) fits what the module already teaches." },
    { id: "balance", description: "Hours stay realistic: additions are balanced by trims; the course still fits its contact hours." },
    { id: "academic", description: "Changes that conflict with the handout's objectives are flagged as academic conflicts, not silently made." },
    { id: "priority", description: "The changes that matter most to the selected roles come first; no trivial or duplicated changes." },
  ],
};

/** Used by the eval CLI (not reviewed inline, to keep stage 5-6 cheap). */
export const PLAN_RUBRIC: Rubric = {
  id: "rubric.plan",
  version: "1",
  criteria: [
    { id: "coverage", description: "Every outcome is taught; key outcomes are revisited." },
    { id: "sequence", description: "Sessions move from foundations to higher Bloom levels in a sensible order." },
    { id: "styleFit", description: "Teaching styles and video kinds suit each session's outcomes and the learning path." },
    { id: "specific", description: "Session titles are specific and learner-facing." },
  ],
};

export const HOURPLAN_RUBRIC: Rubric = {
  id: "rubric.hourPlan",
  version: "1",
  criteria: [
    { id: "runnable", description: "A teacher could run each block as written: concrete activities, materials, grouping and outputs." },
    { id: "alignment", description: "Activities and checks practise and assess the session outcomes at their Bloom level." },
    { id: "flow", description: "Follows hook, objectives, present, guided practice, independent practice, check, wrap; sensible timing and breaks." },
    { id: "industry", description: "Industry examples are relevant to the selected roles and do not invent facts." },
    { id: "checks", description: "Quick-check questions are clear and diagnostic." },
  ],
};

export interface ReviewInput {
  rubric: Rubric;
  /** The facts the draft was built from, as text. */
  contextText: string;
  draft: unknown;
}

export const output = z.object({
  scores: z.array(z.object({
    criterion: z.string(),
    score: z.number().min(1).max(5),
    comment: z.string().default(""),
  })).min(1),
  issues: z.array(z.string()).default([]),
});
export type ReviewOutput = z.infer<typeof output>;

export const reviewPrompt: PromptModule<ReviewInput, ReviewOutput> = {
  id: "review.rubric",
  version: "1",
  system: [
    "You are a strict, experienced instructional designer reviewing a draft produced by another model.",
    "Score each rubric criterion from 1 (poor) to 5 (excellent). Be calibrated: 5 means a senior designer would ship it unchanged.",
    "issues: a list of concrete, actionable fixes (\"LO3 chains two skills; split it\"), most important first. Empty if none.",
    BLOOM_GUIDE,
    JSON_RULES,
  ].join("\n"),
  user: (i) => [
    context("rubric", i.rubric.criteria.map((c) => `${c.id}: ${c.description}`).join("\n")),
    context("facts the draft was built from", i.contextText),
    context("draft", JSON.stringify(i.draft, null, 1)),
    'Return {"scores":[{"criterion":"<id>","score":1,"comment":""}],"issues":[""]}.',
  ].join("\n"),
  output,
};

/** Mean score mapped to [0, 1]. Missing criteria count as 1 (the lowest score). */
export function rubricScore(rubric: Rubric, r: ReviewOutput): number {
  const by = new Map(r.scores.map((s) => [s.criterion, s.score]));
  const vals = rubric.criteria.map((c) => by.get(c.id) ?? 1);
  return vals.reduce((a, b) => a + (b - 1) / 4, 0) / vals.length;
}
