import { z } from "zod";
import type { Course, JobRole } from "@cg/core";
import type { PromptModule } from "./types.js";
import { JSON_RULES, FACTS_RULES, context, examplesBlock, json } from "./shared.js";
import { standardsContext } from "./standards.js";

export interface ProposeFitInput {
  course: Course;
  roles: JobRole[]; // selected roles only
}

export const output = z.object({
  changes: z.array(z.object({
    kind: z.enum(["add", "strengthen", "trim"]),
    text: z.string().min(5),
    reason: z.string().min(5),
    targetModuleId: z.string().min(1),
    hoursDelta: z.number(),
    roleIds: z.array(z.string()).default([]),
    academicConflict: z.string().optional(),
  })).min(1).max(10),
});
export type ProposeFitOutput = z.infer<typeof output>;

export const proposeFitPrompt: PromptModule<ProposeFitInput, ProposeFitOutput> = {
  id: "fit.propose",
  version: "1",
  system: [
    "You are a curriculum designer comparing a course with the job roles a teacher selected.",
    "Propose 3-8 changes, each one of:",
    "- add: new content a selected role asks for that no module teaches (hoursDelta > 0)",
    "- strengthen: a module teaches it, but too thinly or only in theory (hoursDelta > 0)",
    "- trim: content the selected roles rarely ask for (hoursDelta < 0)",
    "Every change names its target module id (or \"new\"), the role ids that ask for it, and a reason that cites the role evidence given (posting counts, skills). Do not invent numbers.",
    "Keep the course within its contact hours: additions should be roughly balanced by trims; net hoursDelta should stay within 10% of the contact hours.",
    "Academic requirements: if a change contradicts the handout's objectives or outcomes (e.g. trimming content an objective requires), set academicConflict explaining which objective, e.g. \"CO1 requires soft skills\". Do not drop such content silently.",
    "Write change text as a short, specific topic (\"Hazard analysis (HARA) and safety goals under ISO 26262\"), not a generic theme.",
    "Only name standards from the standards list.",
    FACTS_RULES,
    JSON_RULES,
  ].join("\n"),
  user: (i, ctx) => [
    examplesBlock(ctx.examples),
    context("brief", json(i.course.brief)),
    context("modules", i.course.modules.map((m) => `${m.id} (${m.hours} h): ${m.title}${m.topics.length ? ` [${m.topics.join("; ")}]` : ""}`).join("\n")),
    context("handout objectives and outcomes (academic requirements)",
      [...i.course.objectives.map((o) => `${o.id}: ${o.text}`), ...i.course.outcomes.map((o) => `${o.id}: ${o.text}`)].join("\n") || "(none given)"),
    context("selected roles", i.roles.map((r) => `${r.id}: ${r.title} | ${r.postings} postings | match ${r.moduleMatch}% | skills: ${r.skills.join(", ")}`).join("\n")),
    context("standards", standardsContext()),
    'Return {"changes":[{"kind":"add|strengthen|trim","text":"","reason":"","targetModuleId":"M1|new","hoursDelta":2,"roleIds":["r1"],"academicConflict":"optional"}]}.',
  ].join("\n"),
  output,
};
