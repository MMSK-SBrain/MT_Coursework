import { readdirSync, readFileSync, existsSync } from "node:fs";
import { join } from "node:path";
import type { Course, LearningPlan, ModuleOutcome, Outcome, SessionOutcome, TeachingStyle } from "@cg/core";
import { blocksFromFramework } from "../blocks.js";
import { parseFramework, type Framework } from "../parsers/framework.js";
import { inferBloom, normBloom, provenance } from "../util.js";

export interface ImportResult {
  course: Course;
  gaps: string[]; // things the sources do not contain (reported, never invented)
  notes: string[]; // decisions and mappings worth knowing
  imported: string[]; // one line per kind of content imported
}

export interface ImportContext { dir: string; now: string }

export function slugOf(dir: string): string {
  return dir.replace(/\/+$/, "").split("/").pop()!;
}

export function readText(dir: string, ...names: string[]): { text: string; file: string } | null {
  for (const n of names) {
    const p = join(dir, n);
    if (existsSync(p)) return { text: readFileSync(p, "utf8"), file: n };
  }
  return null;
}

/** Framework files by session/day number, e.g. SESSION-04-...-Framework.md or DAY-04-...-Framework.md */
export function frameworkFiles(dir: string, folder: string, prefix: "SESSION" | "DAY"): Map<number, { file: string; fw: Framework }> {
  const root = join(dir, folder);
  const out = new Map<number, { file: string; fw: Framework }>();
  if (!existsSync(root)) return out;
  const re = new RegExp(`^${prefix}-(\\d+)-.*Framework(-Part1)?\\.md$`);
  for (const f of readdirSync(root).sort()) {
    const m = re.exec(f);
    if (!m) continue;
    const n = Number(m[1]);
    if (out.has(n)) continue;
    out.set(n, { file: f, fw: parseFramework(readFileSync(join(root, f), "utf8")) });
  }
  return out;
}

export function styleFromApproach(approach?: string): TeachingStyle {
  const a = (approach ?? "").toLowerCase();
  if (/case/.test(a)) return "case";
  if (/story/.test(a)) return "story";
  if (/lab|practical|hands-on/.test(a)) return "lab";
  return "teaching";
}

export function makeOutcome(p: {
  id: string; text: string; stated?: string; moduleIds: string[]; objectiveIds?: string[]; now: string; promptId: string;
}, tally: { statedMismatch: string[]; defaulted: string[] }): Outcome {
  const g = inferBloom(p.text, p.stated);
  if (g.how === "default") tally.defaulted.push(p.id);
  const stated = normBloom(p.stated);
  if (g.how === "verb" && stated && stated !== g.bloom) tally.statedMismatch.push(`${p.id} (source says ${stated}, verb says ${g.bloom})`);
  return {
    id: p.id, text: p.text, bloom: g.bloom, moduleIds: p.moduleIds, objectiveIds: p.objectiveIds ?? [], roleIds: [],
    origin: "handout", locked: false, provenance: provenance(p.promptId, p.now),
  };
}

export function classroomPlan(sessions: LearningPlan["sessions"], name: string, now: string): LearningPlan {
  return { id: "classroom", name, path: "classroom", defaultStyle: "teaching", sessions, provenance: provenance("import.plan", now) };
}

export function blocksFor(sessionId: string, fw: Framework | undefined, style: TeachingStyle, now: string) {
  return fw ? blocksFromFramework(sessionId, fw, style, now) : [];
}

export interface Tally { statedMismatch: string[]; defaulted: string[] }

function bloomOf(id: string, text: string, stated: string | undefined, tally: Tally) {
  const g = inferBloom(text, stated);
  if (g.how === "default") tally.defaulted.push(id);
  const st = normBloom(stated);
  if (g.how === "verb" && st && st !== g.bloom) tally.statedMismatch.push(id);
  return g.bloom;
}

/** Module outcome (MO). `outcomeIds` are the parent course LOs, only where a source states the link. */
export function makeMO(p: { id: string; text: string; stated?: string; outcomeIds?: string[]; now: string; promptId: string }, tally: Tally): ModuleOutcome {
  return { id: p.id, text: p.text, bloom: bloomOf(p.id, p.text, p.stated, tally), outcomeIds: p.outcomeIds ?? [], locked: false, provenance: provenance(p.promptId, p.now) };
}

/** Session outcome (SO). `moduleOutcomeIds` are the parent MOs, only where a source states the link. */
export function makeSO(p: { id: string; text: string; stated?: string; moduleOutcomeIds?: string[]; now: string; promptId: string }, tally: Tally): SessionOutcome {
  return { id: p.id, text: p.text, bloom: bloomOf(p.id, p.text, p.stated, tally), moduleOutcomeIds: p.moduleOutcomeIds ?? [], locked: false, provenance: provenance(p.promptId, p.now) };
}

export function summarize(c: Course): string[] {
  const sessions = c.plans[0]?.sessions ?? [];
  const blocks = sessions.flatMap((s) => s.blocks);
  return [
    `${c.modules.length} modules`, `${c.objectives.length} objectives (CO)`, `${c.outcomes.length} course outcomes (LO)`,
    `${c.modules.reduce((a, m) => a + m.outcomes.length, 0)} module outcomes (MO)`, `${sessions.reduce((a, s) => a + s.sessionOutcomes.length, 0)} session outcomes (SO)`,
    `${sessions.length} sessions`, `${blocks.length} hour blocks (${blocks.filter((b) => b.sessionOutcomeIds.length).length} linked to a session outcome)`,
  ];
}
