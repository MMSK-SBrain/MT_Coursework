import { z } from "zod";
import type { Course, Session, VideoCandidate } from "@cg/core";
import type { PromptModule } from "./types.js";
import { JSON_RULES, FACTS_RULES, clip, context } from "./shared.js";

export interface FurtherLearningInput {
  course: Course;
  session: Session;
  videos: VideoCandidate[];
  pages: { title: string; url: string; snippet: string }[];
}

export const output = z.object({
  picks: z.array(z.object({
    source: z.enum(["video", "page"]),
    idx: z.number().int().nonnegative(),
    why: z.string().min(5).max(200),
  })).max(6),
});
export type FurtherLearningOutput = z.infer<typeof output>;

export const findFurtherLearningPrompt: PromptModule<FurtherLearningInput, FurtherLearningOutput> = {
  id: "session.furtherLearning",
  version: "1",
  system: [
    "You pick further-learning resources for one session from search results. You never write a URL: you pick candidates by their index.",
    "Pick 3-5 of the most useful candidates: on topic for the session's outcomes, right level for the audience, from credible channels or sites, not duplicates.",
    "Prefer a mix: at least one video and one page when good ones exist. Skip anything off topic, clickbait or promotional.",
    "why: one line, specific to the session (\"Shows a requirement traced to a HIL test, as in block 3\").",
    FACTS_RULES,
    JSON_RULES,
  ].join("\n"),
  user: (i) => {
    const los = i.course.outcomes.filter((o) => i.session.outcomeIds.includes(o.id));
    return [
      context("session", `${i.session.title}\nAudience: ${i.course.brief.audience} (${i.course.brief.level})\n${los.map((o) => `${o.id}: ${o.text}`).join("\n")}`),
      context("videos", i.videos.map((v, n) => `[${n}] ${v.title} | ${v.channel} | ${Math.round(v.durationSec / 60)} min | ${v.publishedAt.slice(0, 10)} | ${clip(v.description.replace(/\s+/g, " "), 160)}`).join("\n") || "(none)"),
      context("pages", i.pages.map((p, n) => `[${n}] ${p.title} | ${new URL(p.url).hostname} | ${clip(p.snippet, 160)}`).join("\n") || "(none)"),
      'Return {"picks":[{"source":"video|page","idx":0,"why":""}]}.',
    ].join("\n");
  },
  output,
};
