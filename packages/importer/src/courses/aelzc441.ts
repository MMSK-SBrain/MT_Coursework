// AELZC441 Automotive Vehicles: course-data.yaml (CO > MO > SO hierarchy) + requirements.md + SESSION-nn lecture frameworks.
import { Course, type Module, type Session } from "@cg/core";
import { parseVehiclesYaml } from "../parsers/courseYaml.js";
import { plain, provenance, round1 } from "../util.js";
import { blocksFor, classroomPlan, frameworkFiles, makeMO, makeOutcome, makeSO, readText, slugOf, summarize, type ImportContext, type ImportResult } from "./common.js";

const field = (md: string, label: string) => new RegExp(`\\*\\*${label}:\\*\\*\\s*(.+)`).exec(md)?.[1]?.trim();
const coId = (raw: string) => raw.replace(/^co-?/i, "CO").toUpperCase();

export function importVehicles(ctx: ImportContext): ImportResult {
  const { dir, now } = ctx;
  const gaps: string[] = [];
  const notes: string[] = [];
  const yamlFile = readText(dir, "course-data-fixed.yaml", "course-data.yaml");
  if (!yamlFile) throw new Error(`${dir}: need course-data.yaml`);
  const y = parseVehiclesYaml(yamlFile.text);
  const req = readText(dir, "requirements.md")?.text ?? "";
  const fws = frameworkFiles(dir, "lecture-frameworks", "SESSION");
  notes.push(`Read ${yamlFile.file} (course-data.yaml and course-data-fixed.yaml are byte-identical).`);

  // Course-level outcomes: the yaml's four "course_outcomes" are the only course-level statements; they become
  // both the objectives (CO1-4) and the course LOs (LO1-4), since the model's session.outcomeIds needs LO ids.
  const tally = { statedMismatch: [] as string[], defaulted: [] as string[] };
  const objectives = y.courseOutcomes.map((c) => ({ id: coId(c.id), text: c.description, locked: false, provenance: provenance("import.yaml", now) }));
  const loOf = (co: string) => `LO${coId(co).slice(2)}`;
  const moduleIdsOfCo = new Map<string, string[]>();
  for (const m of y.modules) for (const co of m.moduleOutcome?.parentCo ?? []) moduleIdsOfCo.set(coId(co), [...(moduleIdsOfCo.get(coId(co)) ?? []), `M${m.number}`]);
  const outcomes = y.courseOutcomes.map((c) => makeOutcome({
    id: loOf(c.id), text: c.description, stated: c.bloom, moduleIds: moduleIdsOfCo.get(coId(c.id)) ?? [], objectiveIds: [coId(c.id)], now, promptId: "import.yaml",
  }, tally));
  notes.push("The yaml states only four course-level outcomes (\"course_outcomes\", CO-1..4). They are imported as objectives CO1-4 and again as course LOs LO1-4 (same text, LOn linked to COn) because Session.outcomeIds requires at least one LO. Their verbs (Study, Learn, Get acquainted) are vague, so the verb rule flags them.");

  // Module outcomes: one MO per module in the yaml (module_outcome), parented to the LO of its parent_co.
  const moOf = new Map<number, string>();
  const modules: Module[] = y.modules.map((m) => {
    const mo = m.moduleOutcome;
    if (mo) moOf.set(m.number, `M${m.number}.MO1`);
    return {
      id: `M${m.number}`, title: m.name, hours: round1(m.lessons.length * 2),
      topics: m.lessons.map((l) => l.name), foundIn: "import" as const,
      outcomes: mo ? [makeMO({ id: `M${m.number}.MO1`, text: mo.description, stated: mo.bloom, outcomeIds: mo.parentCo.map(loOf), now, promptId: "import.yaml" }, tally)] : [],
      note: m.description,
    };
  });
  notes.push("Modules and their single module outcome (MO) come from course-data.yaml; MO parents are the LOs matching the yaml's parent_co. foundIn is \"import\".");

  // Session outcomes: the yaml session_outcomes, parented to their module's MO.
  const sessions: Session[] = y.modules.flatMap((m) => m.lessons.map((l): Session => {
    const id = `S${l.number}`;
    const sessionOutcomes = l.outcomes.map((o, i) => makeSO({
      id: `${id}.SO${i + 1}`, text: o.description, stated: o.bloom, moduleOutcomeIds: o.parentMo && moOf.has(m.number) ? [moOf.get(m.number)!] : [], now, promptId: "import.yaml",
    }, tally));
    const loIds = [...new Set((m.moduleOutcome?.parentCo ?? []).map(loOf))];
    const numerical = l.outcomes.filter((o) => o.sessionType === "numerical").length;
    const style = numerical * 2 >= l.outcomes.length ? "worked" : "teaching";
    const fw = fws.get(l.number)?.fw;
    const blocks = blocksFor(id, fw, style, now);
    if (!blocks.length) gaps.push(`Session ${l.number} (${l.name}): ${fws.has(l.number) ? "the lecture framework has no timed phases in the story-arc format" : "no lecture framework file exists"}; no blocks imported.`);
    return { id, index: l.number, title: l.name, outcomeIds: loIds, sessionOutcomes, style, minutes: 120, video: "none", blocks, links: [], caseStudies: [], assets: [], stale: false, provenance: provenance("import.yaml", now) };
  }));
  if (tally.statedMismatch.length) notes.push(`Bloom taken from the leading verb; the yaml level differed for ${tally.statedMismatch.length} of ${outcomes.length + sessions.reduce((a, s) => a + s.sessionOutcomes.length, 0) + modules.length} outcomes.`);
  if (tally.defaulted.length) gaps.push(`Bloom defaulted to "understand" (verb unknown, no stated level): ${tally.defaulted.join(", ")}`);
  notes.push("Session.outcomeIds = the LOs of the session's module outcome. Lecture-framework \"Session Objectives\" are not used: the yaml's session outcomes are authoritative. Block sessionOutcomeIds are empty because the frameworks do not tie phases to outcomes.");
  notes.push("Session style: \"worked\" when at least half of the session's outcomes are numerical, else \"teaching\". Session length 120 min (90 lecture + 30 Q&A) per the yaml.");
  if (sessions.length !== (y.totalSessions ?? sessions.length)) gaps.push(`yaml declares ${y.totalSessions} sessions, found ${sessions.length}.`);

  gaps.push("No textbooks or reference books are listed in the yaml, requirements.md or README; brief.textbooks is empty.");
  gaps.push("No BITS handout .txt exists for this course; code, credits and audience come from the yaml and requirements.md.");
  gaps.push("Markets are not stated in the sources: not set (the teacher sets them before the job search).");
  gaps.push("Module hours are derived as 2 h per session (the yaml gives session counts, not hours).");

  const course = Course.parse({
    id: slugOf(dir), slug: slugOf(dir),
    brief: {
      title: y.name ?? "Automotive Vehicles", code: y.code,
      audience: [field(req, "Primary Learners"), field(req, "Background")].filter(Boolean).map((s) => plain(s!)).join(" - ") || y.institution || "M.Tech. Automotive Electronics (BITS Pilani WILP)",
      level: "pg", contactHours: round1(sessions.length * 2),
      industry: field(req, "Industry/Domain") ?? "Automotive engineering", markets: [], textbooks: [],
      notes: [y.description, y.institution ? `Institution: ${y.institution}.` : "", `Credits: ${y.credits}.`, `Session length: ${y.sessionDuration}.`].filter(Boolean).join(" "),
    },
    sources: [{ id: "src-yaml", kind: "other", filename: yamlFile.file, mime: "application/yaml", storageKey: `courses/${slugOf(dir)}/${yamlFile.file}` }],
    modules, objectives, outcomes, plans: [classroomPlan(sessions, "Classroom (20 contact sessions)", now)],
    createdAt: now, updatedAt: now,
  });
  return {
    course, gaps, notes,
    imported: summarize(course),
  };
}
