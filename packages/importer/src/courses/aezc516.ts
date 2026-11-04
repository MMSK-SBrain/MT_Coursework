// AEZC516 Advances in IC Engines: BITS handout (.txt) + AEZG516_Course_Template.xlsx + session templates (minute-by-minute).
import { readdirSync, readFileSync, existsSync } from "node:fs";
import { join } from "node:path";
import { Course, type Module, type Session } from "@cg/core";
import { blocksFromTimed } from "../blocks.js";
import { parseHandout } from "../parsers/handout.js";
import { parseTimedTemplates } from "../parsers/framework.js";
import { readModuleTemplate } from "../parsers/xlsx.js";
import { provenance, round1 } from "../util.js";
import { classroomPlan, makeOutcome, readText, slugOf, type ImportContext, type ImportResult } from "./common.js";

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

  const modules: Module[] = t.modules.map((m) => {
    const mos = t.modules.length ? Object.values(t.mos).filter((x) => x.moduleNumber === m.number) : [];
    const titles = m.lessons.map((l) => timed.find((s) => s.number === l.number)?.title ?? l.name);
    return {
      id: `M${m.number}`, title: m.name, hours: round1(m.lessons.length * 1.5), topics: titles, foundIn: "moduleSheet",
      note: [m.description, ...mos.map((x) => `Module outcome ${x.id}: ${x.description}`)].filter(Boolean).join(" "),
    };
  });
  const allModuleIds = modules.map((m) => m.id);
  notes.push("Modules come from the .xlsx module sheet (foundIn \"moduleSheet\"); the handout defines no modules. Module hours = 1.5 h per session (session templates are 90 min).");

  // objectives: the handout CO table is empty; the sheet carries five
  const objectives = Object.values(t.cos).map((c) => ({ id: coId(c.id), text: c.description, locked: false, provenance: provenance("import.xlsx", now) }));
  gaps.push(`${h.emptyObjectiveIds.join(", ")} are empty in the handout. The ${objectives.length} objectives imported (${objectives.map((o) => o.id).join(", ")}) come from the .xlsx sheet, not the handout.`);

  const tally = { statedMismatch: [] as string[], defaulted: [] as string[] };
  const outcomes = [
    ...h.outcomes.map((lo) => makeOutcome({ id: lo.id, text: lo.text, moduleIds: allModuleIds, now, promptId: "import.handout" }, tally)),
    ...t.modules.flatMap((m) => m.lessons.flatMap((l) => l.outcomes.map((o) =>
      makeOutcome({ id: soId(o.id), text: o.description, stated: o.bloom, moduleIds: [`M${m.number}`], objectiveIds: m.coId ? [coId(m.coId)] : [], now, promptId: "import.xlsx" }, tally)))),
  ];
  gaps.push("Handout LO1-LO5 carry no module or objective mapping; linked to all modules (core requires at least one module) and no objectives. Core change suggested: allow course-level outcomes with empty moduleIds.");
  gaps.push("No session or lesson cites LO1-LO5, so the plan leaves them uncovered (see rule warnings).");
  notes.push("objectiveIds for SO outcomes use the sheet's CO column, which is filled only on some rows; blank cells carry down from the row above (so Module 2 takes CO1).");
  if (tally.statedMismatch.length) notes.push(`Bloom taken from the leading verb; the sheet level differed for ${tally.statedMismatch.length} outcomes.`);
  if (tally.defaulted.length) gaps.push(`Bloom defaulted to "understand" (verb unknown, no stated level): ${tally.defaulted.join(", ")}`);

  const renamed: string[] = [];
  const sessions: Session[] = t.modules.flatMap((m) => m.lessons.map((l): Session => {
    const id = `S${l.number}`;
    const tpl = timed.find((s) => s.number === l.number);
    const title = tpl?.title ?? l.name;
    if (tpl && tpl.title !== l.name) renamed.push(`${l.number} ("${l.name}" -> "${tpl.title}")`);
    if (tpl && tpl.outcomeIds.join() !== l.outcomes.map((o) => o.id.toUpperCase()).join()) gaps.push(`Session ${l.number}: the template's outcome list (${tpl.outcomeIds.join(", ")}) differs from the sheet's.`);
    const style = "teaching" as const;
    const blocks = tpl ? blocksFromTimed(id, tpl, style, now) : [];
    if (!blocks.length) gaps.push(`Session ${l.number}: no timed template found.`);
    return { id, index: l.number, title, outcomeIds: l.outcomes.map((o) => soId(o.id)), style, minutes: tpl?.minutes ?? 90, video: "none", blocks, links: [], caseStudies: [], assets: [], stale: false, provenance: provenance("import.xlsx", now) };
  }));
  if (renamed.length) notes.push(`Session titles come from the session templates, whose outcome lists match the sheet's SOs; the sheet's lesson names differ for ${renamed.length} of ${sessions.length} sessions: ${renamed.join("; ")}.`);
  gaps.push(`Handout Part B lists 16 contact sessions (15 + a buffer) with a different order and titles (e.g. 1 ${h.sessions[0]?.title.trim()}, 2 ${h.sessions[1]?.title.trim()}); the plan follows the sheet/templates and the handout list is kept in brief.notes.`);
  gaps.push("Several sheet lesson names are placeholders (\"Session 16\", \"Session 17\" ...) and its Day column runs to 28; both ignored in favour of the session templates.");
  gaps.push("Evaluation scheme, experiential-learning components (AMESIM virtual lab) and credit-model hours have no home in the Course model; the lab line is kept in brief.notes.");
  gaps.push("Industry and market are not stated in the handout: industry derived from the programme name, markets defaulted to [\"India\"] (core requires at least one).");

  const course = Course.parse({
    id: slugOf(dir), slug: slugOf(dir),
    brief: {
      title: h.title ?? t.info.name ?? "Advances in IC Engines", code: t.info.code ?? h.courseNos,
      audience: `${h.programme ?? "M.Tech."} students, ${h.division ?? "BITS Pilani Work Integrated Learning Programmes"} (working professionals in the automotive industry)`,
      level: "pg", contactHours: round1(sessions.reduce((a, s) => a + s.minutes, 0) / 60), industry: "Automotive engineering (powertrain)", markets: ["India"],
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
    imported: [`${modules.length} modules`, `${objectives.length} objectives`, `${outcomes.length} outcomes (${h.outcomes.length} handout LOs + ${outcomes.length - h.outcomes.length} sheet SOs)`, `${sessions.length} sessions`, `${sessions.reduce((a, s) => a + s.blocks.length, 0)} hour blocks`],
  };
}
