import { z } from "zod";
import type { CourseBrief, JobPosting, Module } from "@cg/core";
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
  version: "1",
  system: [
    "You turn a course's modules into job-search keywords.",
    "Stay broad: include the core discipline, the methods and tools the modules teach, and neighbouring roles a graduate could move into.",
    "Use terms that appear in real job postings (e.g. \"requirements engineering\", \"HIL testing\"), 2-4 words each, 6-12 keywords.",
    JSON_RULES,
  ].join("\n"),
  user: (i) => [
    context("course", json({ title: i.brief.title, industry: i.brief.industry, markets: i.brief.markets, level: i.brief.level })),
    context("modules", i.modules.map((m) => `${m.id}: ${m.title}${m.topics.length ? ` (${m.topics.join(", ")})` : ""}`).join("\n")),
    'Return {"keywords":["..."]}.',
  ].join("\n"),
  output: keywordsOutput,
};

// ---- Cluster: postings -> roles -------------------------------------------------------------

export interface ClusterInput {
  brief: CourseBrief;
  modules: Module[];
  postings: JobPosting[];
}

export const clusterOutput = z.object({
  roles: z.array(z.object({
    title: z.string().min(2),
    postingIdx: z.array(z.number().int().nonnegative()).min(1),
    experience: z.string().optional(),
    skills: z.array(z.string()).min(1).max(8),
    moduleMatch: z.number().min(0).max(100),
  })).max(15),
});
export type ClusterOutput = z.infer<typeof clusterOutput>;

export const roleClusterPrompt: PromptModule<ClusterInput, ClusterOutput> = {
  id: "roles.cluster",
  version: "1",
  system: [
    "You group job postings into distinct job roles for a teacher deciding what a course should prepare learners for.",
    "Each posting has an index [n]. A role lists the indexes of the postings that belong to it (postingIdx). A posting belongs to at most one role.",
    "skills: the 3-6 skills most often asked for across that role's postings, using the postings' own words.",
    "experience: the typical range stated in the postings, e.g. \"2-8 yrs\"; leave it out if the postings do not say.",
    "moduleMatch: 0-100, how much of what the role asks for the listed modules teach. Be honest; neighbouring roles score low.",
    "Order roles by number of postings, most first. Skip postings unrelated to the course.",
    FACTS_RULES,
    JSON_RULES,
  ].join("\n"),
  user: (i, ctx) => [
    examplesBlock(ctx.examples),
    context("modules", i.modules.map((m) => `${m.id}: ${m.title}`).join("\n")),
    context("postings", i.postings.map((p, n) =>
      `[${n}] ${p.title} | ${p.location} | skills: ${p.skills.join(", ")} | ${clip(p.description.replace(/\s+/g, " "), 280)}`).join("\n")),
    'Return {"roles":[{"title":"","postingIdx":[0,3],"experience":"2-8 yrs","skills":[""],"moduleMatch":0}]}.',
  ].join("\n"),
  output: clusterOutput,
};
