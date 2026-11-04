import { z } from "zod";
import type { CaseStudy, Course, Session } from "@cg/core";
import type { PromptModule } from "./types.js";
import { DESIGN_PRINCIPLES, JSON_RULES, FACTS_RULES, clip, context, examplesBlock, json } from "./shared.js";
import { standardsContext } from "./standards.js";

export interface DraftCaseStudyInput {
  course: Course;
  session: Session;
  label: CaseStudy["label"];
  /** Web search results; a "real" case study may only use facts from these. */
  sources: { title: string; url: string; snippet: string }[];
}

export const output = z.object({
  title: z.string().min(3),
  background: z.string().min(50),
  data: z.string().default(""),
  questions: z.array(z.string().min(5)).min(2).max(8),
  teachingNote: z.string().min(30),
  sourceIdx: z.array(z.number().int().nonnegative()).default([]),
  outcomeIds: z.array(z.string()).default([]),
});
export type DraftCaseStudyOutput = z.infer<typeof output>;

export const draftCaseStudyPrompt: PromptModule<DraftCaseStudyInput, DraftCaseStudyOutput> = {
  id: "session.caseStudy",
  version: "1",
  system: [
    "You write one teaching case study for a session.",
    "A REAL case study uses only facts stated in the supplied sources and cites them by index (sourceIdx, at least one). Do not add facts that are not in the sources.",
    "A COMPOSITE case study is realistic but made up: invented company and people names must be obviously fictional (e.g. \"a Tier-1 supplier, call it Veltra\"); do not attribute events to real companies.",
    "Structure: background (the situation and the decision to be made, 150-400 words), data (a small markdown table or figures the learners need; may be empty), 3-6 questions that climb Bloom levels and map to the session outcomes, and a teachingNote for the instructor (expected answers, common mistakes, timing).",
    DESIGN_PRINCIPLES,
    FACTS_RULES,
    JSON_RULES,
  ].join("\n"),
  user: (i, ctx) => {
    const los = i.course.outcomes.filter((o) => i.session.outcomeIds.includes(o.id));
    return [
      examplesBlock(ctx.examples),
      context("brief", json({ title: i.course.brief.title, audience: i.course.brief.audience, level: i.course.brief.level, industry: i.course.brief.industry })),
      context("session", `${i.session.title}\n${los.map((o) => `${o.id} [${o.bloom}]: ${o.text}`).join("\n")}`),
      context("sources", i.sources.map((s, n) => `[${n}] ${s.title} | ${s.url}\n${clip(s.snippet, 600)}`).join("\n") || "(none)"),
      context("standards", standardsContext()),
      `Label: ${i.label.toUpperCase()}`,
      'Return {"title":"","background":"","data":"","questions":[""],"teachingNote":"","sourceIdx":[0],"outcomeIds":["LO1"]}.',
    ].join("\n");
  },
  output,
};
