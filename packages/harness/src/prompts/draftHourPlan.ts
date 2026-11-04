import { z } from "zod";
import { BlockKind, TeachingStyle, type Course, type LearningPlan, type Session } from "@cg/core";
import type { PromptModule } from "./types.js";
import { DESIGN_PRINCIPLES, JSON_RULES, FACTS_RULES, context, examplesBlock, json } from "./shared.js";
import { standardsContext } from "./standards.js";

export interface EvidenceItem {
  title: string;
  url: string;
  source: string;
  roleId: string;
}

export interface DraftHourPlanInput {
  course: Course;
  plan: LearningPlan;
  session: Session;
  /** Role evidence (ESCO occupation pages) for the selected roles, citable by index. */
  evidence: EvidenceItem[];
}

export const output = z.object({
  blocks: z.array(z.object({
    hour: z.number().int().positive(),
    startMin: z.number().int().nonnegative(),
    minutes: z.number().int().positive(),
    kind: BlockKind,
    title: z.string().min(2),
    activity: z.string().min(3),
    outcomeIds: z.array(z.string()).default([]),
    sessionOutcomeIds: z.array(z.string()).default([]),
    style: TeachingStyle,
    industryExample: z.object({
      text: z.string().min(10),
      sector: z.string(),
      roleIds: z.array(z.string()).default([]),
      evidenceIdx: z.array(z.number().int().nonnegative()).default([]),
    }).optional(),
    check: z.array(z.string()).default([]),
    needsSlides: z.boolean().default(false),
  })).min(1).max(40),
});
export type DraftHourPlanOutput = z.infer<typeof output>;

export const draftHourPlanPrompt: PromptModule<DraftHourPlanInput, DraftHourPlanOutput> = {
  id: "session.hourPlan",
  version: "4",
  system: [
    "You plan one session hour by hour, in timed blocks a teacher can run as written.",
    "Timing rules (checked in code): hours are numbered from 1. Within each hour, blocks start at minute 0 and follow each other with no gaps or overlaps (startMin of the next block = startMin + minutes of the previous one).",
    "Every full hour adds up to exactly 60 minutes; the last hour adds up to the remaining minutes of the session.",
    "Block kinds: hook, teach, activity, case, check, wrap, break. Open with a hook, state the outcomes, end with a wrap. Insert one break block with minutes: 10 in sessions over 90 minutes.",
    "Any duration written inside a block's title or activity must agree with that block's minutes. Prefer not to restate durations at all.",
    "For an apply-level (or higher) SO, follow the worked example with a short individual practice block before any group task, so each learner tries it alone first.",
    "activity says what the teacher and the learners do, concretely (materials, prompts, grouping, output).",
    "Give at least one block an industryExample tied to the selected roles. Cite role evidence by index (evidenceIdx) when you use it. Never name a company or figure that is not in the context.",
    "check: 1-3 quick-check questions on check and wrap blocks. Write each as \"Question? Expected: <model answer or marking point>\" so the check is diagnostic. needsSlides: true for teach blocks that need visuals.",
    "Activity text is read by teachers and learners: never paste index tags such as [0] or role ids into it; say the idea in plain words.",
    "outcomeIds may only use the session's course outcomes (LO ids).",
    "sessionOutcomeIds: the session outcomes (SO ids) each block serves. Every SO must be served by at least one block; every block except break and wrap serves at least one SO.",
    "The content of a block must actually let a learner achieve the SOs it names, at their Bloom level: an apply-level SO needs practice, not just explanation. A reviewer checks this block by block.",
    DESIGN_PRINCIPLES,
    FACTS_RULES,
    JSON_RULES,
  ].join("\n"),
  user: (i, ctx) => {
    const los = i.course.outcomes.filter((o) => i.session.outcomeIds.includes(o.id));
    return [
      examplesBlock(ctx.examples),
      context("brief", json({ title: i.course.brief.title, audience: i.course.brief.audience, level: i.course.brief.level, industry: i.course.brief.industry })),
      context("session", [
        `Plan: ${i.plan.name} (path ${i.plan.path})`,
        `Session ${i.session.index}: ${i.session.title}`,
        `Length: ${i.session.minutes} minutes (${Math.ceil(i.session.minutes / 60)} hour block(s))`,
        `Teaching style: ${i.session.style}`,
      ].join("\n")),
      context("course outcomes for this session", los.map((o) => `${o.id} [${o.bloom}]: ${o.text}`).join("\n")),
      context("session outcomes (SOs)", i.session.sessionOutcomes.map((o) => `${o.id} [${o.bloom}]: ${o.text}`).join("\n") || "(none)"),
      context("selected roles", i.course.roles.filter((r) => r.selected).map((r) => `${r.id}: ${r.title} | ${r.skills.join(", ")}`).join("\n") || "(none)"),
      context("role evidence", i.evidence.map((e, n) => `[${n}] (${e.roleId}) ${e.title} - ${e.source}`).join("\n") || "(none)"),
      context("standards", standardsContext()),
      'Return {"blocks":[{"hour":1,"startMin":0,"minutes":10,"kind":"hook","title":"","activity":"","outcomeIds":["LO1"],"sessionOutcomeIds":["S1.SO1"],"style":"teaching","industryExample":{"text":"","sector":"","roleIds":["r1"],"evidenceIdx":[0]},"check":[""],"needsSlides":false}]}.',
    ].join("\n");
  },
  output,
};
