import { z } from "zod";
import type { CourseBrief, Module, Occupation } from "@cg/core";
import type { PromptModule } from "./types.js";
import { JSON_RULES, FACTS_RULES, clip, context, examplesBlock, json } from "./shared.js";

// ---- Keywords: modules -> a broad search ------------------------------------------------------

export interface KeywordsInput {
  brief: CourseBrief;
  modules: Module[];
}

export const keywordsOutput = z.object({ keywords: z.array(z.string().min(2)).min(3).max(15) });

export const roleKeywordsPrompt: PromptModule<KeywordsInput, z.infer<typeof keywordsOutput>> = {
  id: "roles.keywords",
  version: "2",
  system: [
    "You turn a course's modules into search terms for an occupation classification (ESCO).",
    "Stay broad: include the core discipline, the methods and tools the modules teach, and neighbouring roles a graduate could move into.",
    "Mix occupation names (e.g. \"systems engineer\", \"automotive engineer\") with discipline terms (e.g. \"requirements engineering\", \"battery\"), 1-3 plain words each, 6-12 keywords. Avoid acronyms and brand names.",
    JSON_RULES,
  ].join("\n"),
  user: (i) => [
    context("course", json({ title: i.brief.title, industry: i.brief.industry, markets: i.brief.markets, level: i.brief.level })),
    context("modules", i.modules.map((m) => `${m.id}: ${m.title}${m.topics.length ? ` (${m.topics.join(", ")})` : ""}`).join("\n")),
    'Return {"keywords":["..."]}.',
  ].join("\n"),
  output: keywordsOutput,
};

// ---- Match: ESCO occupations -> roles ---------------------------------------------------------

export interface MatchInput {
  brief: CourseBrief;
  modules: Module[];
  occupations: Occupation[];
}

export const matchOutput = z.object({
  roles: z.array(z.object({
    occIdx: z.number().int().nonnegative(),
    coveredSkillIdx: z.array(z.number().int().nonnegative()),
  })).max(15),
});
export type MatchOutput = z.infer<typeof matchOutput>;

export const roleMatchPrompt: PromptModule<MatchInput, MatchOutput> = {
  id: "roles.match",
  version: "1",
  system: [
    "You pick the occupations a course could prepare learners for, and say which of each occupation's essential skills the modules teach.",
    "Each occupation has an index [n]; its essential skills are numbered s0, s1, ... A role is {occIdx, coveredSkillIdx}.",
    "coveredSkillIdx: the skill numbers a module clearly teaches (by title or topics). Be strict: related is not covered.",
    "Keep occupations a graduate of this course could realistically hold, up to 12. Skip unrelated ones.",
    FACTS_RULES,
    JSON_RULES,
  ].join("\n"),
  user: (i, ctx) => [
    examplesBlock(ctx.examples),
    context("course", json({ title: i.brief.title, level: i.brief.level, industry: i.brief.industry })),
    context("modules", i.modules.map((m) => `${m.id}: ${m.title}${m.topics.length ? ` (${m.topics.join(", ")})` : ""}`).join("\n")),
    context("occupations", i.occupations.map((o, n) =>
      `[${n}] ${o.title}: ${clip(o.description.replace(/\s+/g, " "), 200)}\n  essential: ${o.essentialSkills.map((s, k) => `s${k} ${s}`).join("; ")}`).join("\n")),
    'Return {"roles":[{"occIdx":0,"coveredSkillIdx":[0,3]}]}.',
  ].join("\n"),
  output: matchOutput,
};
