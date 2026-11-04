import { z } from "zod";
import { BloomLevel, type Course } from "@cg/core";
import type { PromptModule } from "./types.js";
import { BLOOM_GUIDE, DESIGN_PRINCIPLES, JSON_RULES, FACTS_RULES, context, examplesBlock, json } from "./shared.js";
import { standardsContext } from "./standards.js";
import { maxBloomForHours } from "../hierarchy.js";

export interface DraftOutcomesInput {
  course: Course;
}

export const output = z.object({
  objectives: z.array(z.object({ id: z.string().min(1), text: z.string().min(10) })).min(1).max(8),
  outcomes: z.array(z.object({
    id: z.string().min(1),
    text: z.string().min(10),
    bloom: BloomLevel,
    moduleIds: z.array(z.string()).default([]),
    objectiveIds: z.array(z.string()).default([]),
    roleIds: z.array(z.string()).default([]),
    origin: z.enum(["handout", "fit", "new"]),
  })).min(1).max(16),
  moduleOutcomes: z.array(z.object({
    moduleId: z.string().min(1),
    text: z.string().min(10),
    bloom: BloomLevel,
    outcomeIds: z.array(z.string()).default([]),
  })).min(1).max(60),
});
export type DraftOutcomesOutput = z.infer<typeof output>;

export const draftOutcomesPrompt: PromptModule<DraftOutcomesInput, DraftOutcomesOutput> = {
  id: "outcomes.draft",
  version: "2",
  system: [
    "You write the outcome hierarchy for a confirmed course structure: course objectives (COs), course learning outcomes (LOs) and module outcomes (MOs).",
    "Objectives: 2-5 broad statements of what the course develops. LOs: 4-10 specific, assessable statements.",
    "Module outcomes: for EVERY module, 1-3 MOs saying what that module must achieve. Each MO serves one or more LOs (outcomeIds) and every LO is served by at least one MO.",
    "An MO's Bloom level must not exceed what the module's hours can support (the cap is given per module). Together, a LO's MOs should reach the LO's level.",
    "Items marked LOCKED (objectives, outcomes or module outcomes) must be returned unchanged, with the same id and text.",
    "Every module must be covered by at least one outcome (moduleIds). Every outcome links to at least one objective (objectiveIds) and, where relevant, to the job roles (roleIds) it serves.",
    "origin: \"handout\" if it keeps a handout outcome's intent, \"fit\" if it comes from an accepted course-job fit change, \"new\" otherwise.",
    "One outcome = one verb + one object (+ condition or standard). No \"and\" chains of unrelated skills.",
    "Industry context is welcome when it comes from the roles or fit changes given (\"using a requirements tool\", \"following ISO 26262 Part 3\"). Name only standards from the standards list.",
    BLOOM_GUIDE,
    DESIGN_PRINCIPLES,
    FACTS_RULES,
    JSON_RULES,
  ].join("\n"),
  user: (i, ctx) => {
    const c = i.course;
    const accepted = c.fit.filter((f) => f.decision === "accepted" || f.decision === "changed");
    return [
      examplesBlock(ctx.examples),
      context("brief", json(c.brief)),
      context("confirmed modules", c.modules.map((m) => `${m.id} (${m.hours} h, Bloom cap ${maxBloomForHours(m.hours)}): ${m.title}${m.topics.length ? ` [${m.topics.join("; ")}]` : ""}`).join("\n")),
      context("selected roles", c.roles.filter((r) => r.selected).map((r) => `${r.id}: ${r.title} | skills: ${r.skills.join(", ")}`).join("\n") || "(none)"),
      context("accepted fit changes", accepted.map((f) => `${f.kind} -> ${f.targetModuleId}: ${f.text} (roles ${f.roleIds.join(", ")})`).join("\n") || "(none)"),
      context("existing objectives",
        c.objectives.map((o) => `${o.locked ? "LOCKED " : ""}${o.id}: ${o.text}`).join("\n") || "(none)"),
      context("existing outcomes",
        c.outcomes.map((o) => `${o.locked ? "LOCKED " : ""}${o.id} [${o.bloom}; ${o.moduleIds.join(",")}]: ${o.text}`).join("\n") || "(none)"),
      context("existing module outcomes",
        c.modules.flatMap((m) => m.outcomes.map((o) => `${o.locked ? "LOCKED " : ""}${m.id}: ${o.text} [${o.bloom}; serves ${o.outcomeIds.join(",")}]`)).join("\n") || "(none)"),
      context("standards", standardsContext()),
      'Return {"objectives":[{"id":"CO1","text":""}],"outcomes":[{"id":"LO1","text":"","bloom":"apply","moduleIds":["M1"],"objectiveIds":["CO1"],"roleIds":["r1"],"origin":"handout|fit|new"}],"moduleOutcomes":[{"moduleId":"M1","text":"","bloom":"apply","outcomeIds":["LO1"]}]}.',
    ].join("\n");
  },
  output,
};
