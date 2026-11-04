// AEZC516 Advances in IC Engines: BITS handout (.txt) + AEZG516_Course_Template.xlsx + session templates (minute-by-minute).
import { readdirSync, readFileSync, existsSync } from "node:fs";
import { join } from "node:path";
import { Course, type Module, type Session } from "@cg/core";
import { blocksFromTimed } from "../blocks.js";
import { parseHandout } from "../parsers/handout.js";
import { parseTimedTemplates } from "../parsers/framework.js";
import { readModuleTemplate } from "../parsers/xlsx.js";
import { provenance, round1 } from "../util.js";
import { classroomPlan, makeMO, makeOutcome, makeSO, readText, slugOf, summarize, type ImportContext, type ImportResult } from "./common.js";

const coId = (raw: string) => raw.replace(/^co-?/i, "CO").toUpperCase();
const soId = (raw: string) => raw.replace(/^so-/i, "SO-");

export async function importIceEngines(ctx: ImportContext): Promise<ImportResult> {
  const { dir, now } = ctx;
  const gaps: string[] = [];
  const notes: string[] = [];
  const handoutFile = readText(dir, "course_handout.txt", "course-handout.txt");
  const xlsxName = readdirSync(dir).find((f) => /\.xlsx$/i.test(f) && !f.startsWith("~$"));
  if (!handoutFile || !xlsxName) throw new Error(`${dir}: need course_handout.txt and a module-template .xlsx`);
  const h = parseHandout(handoutFile.text);
  const t = await readModuleTemplate(join(dir, xlsxName));
  const tplPath = join(dir, "frameworks/lesson-plans/01-session-templates-all-15.md");
  const timed = existsSync(tplPath) ? parseTimedTemplates(readFileSync(tplPath, "utf8")) : [];

  const tally = { statedMismatch: [] as string[], defaulted: [] as string[] };

  // Module outcomes: the sheet gives one MO per lesson (ids mo-<module>-<n>); renumber per module as M<m>.MO<k>.
  const moIdOf = new Map<string, string>();
  const modules: Module[] = t.modules.map((m) => {
    const sheetMos = [...new Set(m.lessons.map((l) => l.moId).filter((x): x is string => !!x))];
    sheetMos.forEach((sid, k) => moIdOf.set(sid, `M${m.number}.MO${k + 1}`));
    const titles = m.lessons.map((l) => timed.find((s) => s.number === l.number)?.title ?? l.name);
    return {
      id: `M${m.number}`, title: m.name, hours: round1(m.lessons.length * 1.5), topics: titles, foundIn: "moduleSheet" as const,
      outcomes: sheetMos.flatMap((sid) => {
        const mo = t.mos[sid];
        return mo ? [makeMO({ id: moIdOf.get(sid)!, text: mo.description, stated: mo.bloom, now, promptId: "import.xlsx" }, tally)] : [];
      }),
      note: [m.description, m.coId ? `Course objective in force on the sheet: ${coId(m.coId)}.` : ""].filter(Boolean).join(" "),
    };
  });
  notes.push("Modules and module outcomes come from the .xlsx module sheet (foundIn \"moduleSheet\"); the handout defines none. The sheet has one MO per lesson, renumbered M<m>.MO<k>. Module hours = 1.5 h per session (templates are 90 min).");
  notes.push("The sheet's CO column is filled only on some rows; blank cells carry down (so Module 2 takes CO1). The model has no CO link on MOs or SOs, so the CO in force is recorded in each module's note.");

  // objectives: the handout CO table is empty; the sheet carries five
  const objectives = Object.values(t.cos).map((c) => ({ id: coId(c.id), text: c.description, locked: false, provenance: provenance("import.xlsx", now) }));
  gaps.push(`${h.emptyObjectiveIds.join(", ")} are empty in the handout. The ${objectives.length} objectives imported (${objectives.map((o) => o.id).join(", ")}) come from the .xlsx sheet, not the handout.`);

  // course LOs: the handout's five
  const outcomes = h.outcomes.map((lo) => makeOutcome({ id: lo.id, text: lo.text, moduleIds: [], now, promptId: "import.handout" }, tally));
  gaps.push("Handout LO1-LO5 carry no module, objective or session mapping; imported as course-level outcomes with no module or objective. Module outcomes therefore have no parent LO. Map them in the app.");
  const allLos = outcomes.map((o) => o.id);

  const renamed: string[] = [];
  const sessions: Session[] = t.modules.flatMap((m) => m.lessons.map((l): Session => {
    const id = `S${l.number}`;
    const tpl = timed.find((s) => s.number === l.number);
    const title = tpl?.title ?? l.name;
    if (tpl && tpl.title !== l.name) renamed.push(`${l.number} ("${l.name}" -> "${tpl.title}")`);
    if (tpl && tpl.outcomeIds.join() !== l.outcomes.map((o) => o.id.toUpperCase()).join()) gaps.push(`Session ${l.number}: the template's outcome list (${tpl.outcomeIds.join(", ")}) differs from the sheet's.`);
    const style = "teaching" as const;
    const sessionOutcomes = l.outcomes.map((o, i) => makeSO({
      id: `${id}.SO${i + 1}`, text: o.description, stated: o.bloom, moduleOutcomeIds: l.moId && moIdOf.has(l.moId) ? [moIdOf.get(l.moId)!] : [], now, promptId: "import.xlsx",
    }, tally));
    const blocks = tpl ? blocksFromTimed(id, tpl, style, now) : [];
    if (!blocks.length) gaps.push(`Session ${l.number}: no timed template found.`);
    return { id, index: l.number, title, outcomeIds: allLos, sessionOutcomes, style, minutes: tpl?.minutes ?? 90, video: "none", blocks, links: [], caseStudies: [], assets: [], stale: false, provenance: provenance("import.xlsx", now) };
  }));
  if (tally.statedMismatch.length) notes.push(`Bloom taken from the leading verb; the sheet level differed for ${tally.statedMismatch.length} outcomes.`);
  if (tally.defaulted.length) gaps.push(`Bloom defaulted to "understand" (verb unknown, no stated level): ${tally.defaulted.join(", ")}`);
  gaps.push("Session.outcomeIds (course LOs, at least one required) has no source: every session lists all five handout LOs as a placeholder. Treat it as unmapped; core change suggested: allow Session.outcomeIds to be empty.");
  notes.push("The 63 sheet SOs are session outcomes on their sessions (S<n>.SO<k>), parented to the lesson's MO. Block sessionOutcomeIds are empty: the templates tie blocks to MCQ ids, not to outcomes.");
  if (renamed.length) notes.push(`Session titles come from the session templates, whose outcome lists match the sheet's SOs; the sheet's lesson names differ for ${renamed.length} of ${sessions.length} sessions: ${renamed.join("; ")}.`);
  gaps.push(`Handout Part B lists 16 contact sessions (15 + a buffer) with a different order and titles (e.g. 1 ${h.sessions[0]?.title.trim()}, 2 ${h.sessions[1]?.title.trim()}); the plan follows the sheet/templates and the handout list is kept in brief.notes.`);
  gaps.push("Several sheet lesson names are placeholders (\"Session 16\", \"Session 17\" ...) and its Day column runs to 28; both ignored in favour of the session templates.");
  gaps.push("Evaluation scheme, experiential-learning components (AMESIM virtual lab) and credit-model hours have no home in the Course model; the lab line is kept in brief.notes.");
  gaps.push("Industry and market are not stated in the handout: industry derived from the programme name, markets not set (the teacher sets them before the job search).");

  const course = Course.parse({
    id: slugOf(dir), slug: slugOf(dir),
    brief: {
      title: h.title ?? t.info.name ?? "Advances in IC Engines", code: t.info.code ?? h.courseNos,
      audience: `${h.programme ?? "M.Tech."} students, ${h.division ?? "BITS Pilani Work Integrated Learning Programmes"} (working professionals in the automotive industry)`,
      level: "pg", contactHours: round1(sessions.reduce((a, s) => a + s.minutes, 0) / 60), industry: "Automotive engineering (powertrain)", markets: [],
      textbooks: [...h.textbooks, ...h.references].map((b) => `${b.id}: ${b.text}`),
      notes: [
        h.description, `Handout course no: ${h.courseNos}; credit units ${h.creditUnits}; version ${h.version} (${h.date}); instructor ${h.instructor}.`,
        "T-ids are textbooks, R-ids reference books.",
        "Handout Part B sessions: " + h.sessions.map((s) => `${s.number} ${s.title.trim()}`).join("; ") + ".",
        "Handout experiential component: Virtual Lab with the AMESIM software tool, 12 hours of lab lecture and 20 hours of practice.",
        "contactHours = the 15 planned 90-minute sessions; the handout's credit-model line is blank.",
      ].filter(Boolean).join(" "),
    },
    sources: [
      { id: "src-handout", kind: "handout", filename: handoutFile.file, mime: "text/plain", storageKey: `courses/${slugOf(dir)}/${handoutFile.file}` },
      { id: "src-sheet", kind: "moduleSheet", filename: xlsxName, mime: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", storageKey: `courses/${slugOf(dir)}/${xlsxName}` },
    ],
    modules, objectives, outcomes, plans: [classroomPlan(sessions, "Classroom (15 contact sessions)", now)],
    createdAt: now, updatedAt: now,
  });
  return {
    course, gaps, notes,
    imported: summarize(course),
  };
}
