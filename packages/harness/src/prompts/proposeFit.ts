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
  version: "3",
  system: [
    "You are a curriculum designer comparing a course with the job roles a teacher selected.",
    "Propose 3-8 changes, each one of:",
    "- add: new content a selected role asks for that no module teaches (hoursDelta > 0)",
    "- strengthen: a module teaches it, but too thinly or only in theory (hoursDelta > 0)",
    "- trim: content the selected roles rarely ask for (hoursDelta < 0)",
    "Every change names its target module id (or \"new\"), the role ids that ask for it, and a reason that cites the role evidence given (the ESCO skills a role needs that the modules miss). Do not invent numbers or demand figures.",
    "Keep the course within its contact hours: additions should be roughly balanced by trims; net hoursDelta should stay within 10% of the contact hours.",
    "Academic requirements: if a change contradicts a handout objective or outcome (e.g. trimming content it requires), set academicConflict naming that id and why, e.g. \"LO2 requires knock diagnosis from pressure data\". Do not drop such content silently.",
    "Leave academicConflict out entirely when there is no conflict. Never write \"no conflict\" or a justification there.",
    "Refer only to objective and outcome ids that appear in the context.",
    "Order changes by importance: changes that close missing essential skills for the most selected roles first, other additions and strengthens next, trims last (least harmful trim first). Do not duplicate a change.",
    "Use add for content no module teaches yet and strengthen for content a module already teaches; the reason must not claim a module teaches something unless its title or topics say so.",
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
    context("selected roles", i.roles.map((r) => `${r.id}: ${r.title} | match ${r.moduleMatch}% | covered: ${r.matchedSkills.join(", ") || "none"} | missing: ${r.skills.filter((k) => !r.matchedSkills.includes(k)).join(", ") || "none"}`).join("\n")),
    context("standards", standardsContext()),
    'Return {"changes":[{"kind":"add|strengthen|trim","text":"","reason":"","targetModuleId":"M1|new","hoursDelta":2,"roleIds":["r1"],"academicConflict":"optional"}]}.',
  ].join("\n"),
  output,
};
