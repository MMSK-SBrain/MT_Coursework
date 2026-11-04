import { z } from "zod";
import { AUTO_STYLE, BloomLevel, PATH_FAMILY, TeachingStyle, VIDEO_BY_PATH, VideoKind, type Course, type PlanSpec } from "@cg/core";
import type { PromptModule } from "./types.js";
import { BLOOM_GUIDE, DESIGN_PRINCIPLES, JSON_RULES, FACTS_RULES, context, examplesBlock, json } from "./shared.js";

export interface DraftPlanInput {
  course: Course;
  spec: PlanSpec;
  /** Suggested session count and length, computed in code from the brief and path. */
  sessionCount: number;
  sessionMinutes: number;
}

export const output = z.object({
  name: z.string().min(2),
  sessions: z.array(z.object({
    title: z.string().min(3),
    outcomeIds: z.array(z.string()).min(1),
    style: TeachingStyle,
    minutes: z.number().int().positive(),
    video: VideoKind,
    sessionOutcomes: z.array(z.object({
      text: z.string().min(10),
      bloom: BloomLevel,
      moduleOutcomeIds: z.array(z.string()).default([]),
    })).min(1).max(5),
  })).min(1).max(60),
});
export type DraftPlanOutput = z.infer<typeof output>;

export const PATH_GUIDE: Record<string, string> = {
  classroom: "Instructor-led sessions, in person or online.",
  lab: "Hands-on bench or tool sessions with a short brief.",
  bootcamp: "Full intensive days; a project every afternoon.",
  flipped: "Learners watch a short pre-class video, then apply in class.",
  blended: "Mix of live sessions and online modules.",
  cohort: "Weekly live call plus async work and peer review.",
  elearning: "LMS modules with reading pages and quizzes; no video.",
  micro: "5-minute mobile lessons, one idea each.",
  youtube: "6-12 minute episodes for a public audience; strong hook in the title.",
  shorts: "Vertical 30-60 second clips; one surprising idea each.",
};

export const draftPlanPrompt: PromptModule<DraftPlanInput, DraftPlanOutput> = {
  id: "plan.draft",
  version: "2",
  system: [
    "You draft a learning plan: an ordered list of sessions that together teach every frozen learning outcome.",
    "Every outcome id must appear in at least one session. Sequence from foundations to higher Bloom levels; revisit key outcomes (spaced practice).",
    "Each session has one teaching style (the plan default unless another style suits the session's outcomes better) and one video kind, chosen ONLY from the allowed video kinds.",
    "Teaching styles: teaching, worked, story, analogy (explain); discussion, debate, dyk, challenge (engage); case, pbl, project, lab, roleplay (apply); teardown, failure, expert, retrieval (investigate).",
    "Each session has 1-4 session outcomes (SOs): what a learner can do at the end of THAT lesson, measurable and achievable in the session's minutes.",
    "Each SO serves one or more module outcomes (moduleOutcomeIds). Every module outcome must be served by at least one SO at the MO's Bloom level or higher, otherwise the module is not met.",
    "Lower-level SOs that build up to an MO are welcome in earlier sessions.",
    BLOOM_GUIDE,
    "Session titles are specific and learner-facing (\"From stakeholder needs to system requirements\"), not \"Session 3\".",
    DESIGN_PRINCIPLES,
    FACTS_RULES,
    JSON_RULES,
  ].join("\n"),
  user: (i, ctx) => {
    const p = i.spec.path;
    const styleNote = i.spec.style === "auto"
      ? `Auto: pick per session from the outcomes' Bloom level (${Object.entries(AUTO_STYLE).map(([b, s]) => `${b}->${s}`).join(", ")}).`
      : i.spec.style;
    return [
      examplesBlock(ctx.examples),
      context("brief", json(i.course.brief)),
      context("frozen outcomes", i.course.outcomes.map((o) => `${o.id} [${o.bloom}; ${o.moduleIds.join(",")}]: ${o.text}`).join("\n")),
      context("modules", i.course.modules.map((m) => `${m.id} (${m.hours} h): ${m.title}`).join("\n")),
      context("module outcomes", i.course.modules.flatMap((m) => m.outcomes.map((o) => `${o.id} [${o.bloom}; serves ${o.outcomeIds.join(",")}]: ${o.text}`)).join("\n") || "(none)"),
      context("plan", [
        `Learning path: ${p} (${PATH_FAMILY[p]}). ${PATH_GUIDE[p] ?? ""}`,
        `Default teaching style: ${styleNote}`,
        `Allowed video kinds: ${VIDEO_BY_PATH[p].join(", ")} (default ${VIDEO_BY_PATH[p][0]})`,
        `Aim for about ${i.sessionCount} sessions of ${i.sessionMinutes} minutes each.`,
        i.spec.audienceVariant ? `Audience variant: ${i.spec.audienceVariant}` : "",
        i.spec.name ? `Plan name: ${i.spec.name}` : "",
      ].filter(Boolean).join("\n")),
      'Return {"name":"","sessions":[{"title":"","outcomeIds":["LO1"],"style":"teaching","minutes":120,"video":"none","sessionOutcomes":[{"text":"","bloom":"apply","moduleOutcomeIds":["M1.MO1"]}]}]}.',
    ].join("\n");
  },
  output,
};
