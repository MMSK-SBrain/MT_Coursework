// AEZC517 Automotive Systems Engineering: BITS handout (.txt) + course-data.yaml + SESSION-nn lecture frameworks.
import { Course, type Module, type Session } from "@cg/core";
import { parseHandout } from "../parsers/handout.js";
import { parseSeYaml } from "../parsers/courseYaml.js";
import { provenance, round1, titleCaseIfShouting } from "../util.js";
import { blocksFor, classroomPlan, frameworkFiles, makeOutcome, makeSO, readText, slugOf, styleFromApproach, summarize, type ImportContext, type ImportResult } from "./common.js";

export function importSystemsEngineering(ctx: ImportContext): ImportResult {
  const { dir, now } = ctx;
  const gaps: string[] = [];
  const notes: string[] = [];
  const handoutFile = readText(dir, "course-handout.txt", "course_handout.txt");
  const yamlFile = readText(dir, "course-data.yaml");
  if (!handoutFile || !yamlFile) throw new Error(`${dir}: need course-handout.txt and course-data.yaml`);
  const h = parseHandout(handoutFile.text);
  const y = parseSeYaml(yamlFile.text);
  const fws = frameworkFiles(dir, "lecture-frameworks", "SESSION");

  // modules (the handout has none; the yaml groups sessions into four modules)
  const moduleOfSession = new Map<number, string>();
  const modules: Module[] = y.modules.map((m) => {
    const id = `M${m.number}`;
    const ss = y.sessions.filter((s) => m.sessions.includes(s.number));
    m.sessions.forEach((n) => moduleOfSession.set(n, id));
    return {
      id, title: m.title, hours: round1(ss.reduce((a, s) => a + (s.duration ?? 0), 0) / 60),
      topics: ss.flatMap((s) => s.topics), outcomes: [], foundIn: "import", note: m.description,
    };
  });
  notes.push("Modules come from course-data.yaml (sessions 1-4, 5-8, 9-12, 13-16); the BITS handout does not define modules, so foundIn is \"import\". No module outcomes are stated anywhere, so Module.outcomes is empty.");

  // objectives
  const objectives = h.objectives.map((o) => ({ id: o.id, text: o.text, locked: false, provenance: provenance("import.handout", now) }));
  if (h.emptyObjectiveIds.length) gaps.push(`${h.emptyObjectiveIds.join(", ")} are empty in the handout and in course-data.yaml; not imported.`);

  // outcomes
  const tally = { statedMismatch: [] as string[], defaulted: [] as string[] };
  const outcomes = h.outcomes.map((lo) => {
    const mods = new Set<string>();
    for (const s of y.sessions) if (s.learningOutcomes.includes(lo.id)) { const m = moduleOfSession.get(s.number); if (m) mods.add(m); }
    if (!mods.size) { modules.forEach((m) => mods.add(m.id)); gaps.push(`${lo.id} is cited by no session in course-data.yaml; linked to all modules.`); }
    const stated = y.outcomes.find((o) => o.id === lo.id)?.level;
    return makeOutcome({ id: lo.id, text: lo.text, stated, moduleIds: [...mods], now, promptId: "import.handout" }, tally);
  });
  gaps.push("The handout does not link learning outcomes (LO1-LO5) to course objectives (CO1-CO3); objectiveIds left empty.");
  if (tally.statedMismatch.length) notes.push(`Bloom level taken from the leading verb; yaml disagreed for: ${tally.statedMismatch.join("; ")}.`);

  // sessions
  const sessions: Session[] = y.sessions.map((s) => {
    const id = `S${s.number}`;
    const title = h.sessions.find((x) => x.number === s.number)?.title || s.title;
    const style = styleFromApproach(s.approach);
    const fw = fws.get(s.number)?.fw;
    const blocks = blocksFor(id, fw, style, now);
    if (!blocks.length) gaps.push(`Session ${s.number}: no timed phases in a lecture framework; no blocks imported.`);
    const sessionOutcomes = (fw?.objectives ?? []).map((text, i) => makeSO({ id: `${id}.SO${i + 1}`, text, now, promptId: "import.framework" }, tally));
    if (!sessionOutcomes.length) gaps.push(`Session ${s.number}: the lecture framework states no session objectives.`);
    return { id, index: s.number, title, outcomeIds: s.learningOutcomes, sessionOutcomes, style, minutes: s.duration ?? 120, video: "none", blocks, links: [], caseStudies: [], assets: [], stale: false, provenance: provenance("import.yaml", now) };
  });
  const emptySessions = sessions.filter((s) => !s.outcomeIds.length);
  if (emptySessions.length) throw new Error(`sessions without outcomes: ${emptySessions.map((s) => s.index).join(",")}`);

  const creditHours = Number(/^(\d+)/.exec(h.creditModel ?? y.creditModel ?? "")?.[1]);
  const contactHours = creditHours > 0 ? creditHours : round1(sessions.reduce((a, s) => a + s.minutes, 0) / 60);
  gaps.push("Experiential-learning components, evaluation scheme (quiz/assignment/mid-sem/comprehensive weights) and the credit-model hour split are in the handout/yaml but have no home in the Course model; not imported.");
  notes.push("Session outcomes are the bullets under \"Session Objectives\" in each SESSION-nn framework (session 9 uses the ProjectAndRisk framework, not the DetailedGuide). The sources do not say which module outcome or block each one serves, so moduleOutcomeIds and block sessionOutcomeIds are empty.");
  gaps.push("Industry and market are not stated in the sources: industry derived from the programme name, markets not set (the teacher sets them before the job search).");

  const course = Course.parse({
    id: slugOf(dir), slug: slugOf(dir),
    brief: {
      title: y.title ?? titleCaseIfShouting(h.title ?? ""),
      code: y.shortCode ?? h.courseNos,
      audience: `${h.programme ?? "M.Tech."} students, ${h.division ?? "BITS Pilani Work Integrated Learning Programmes"} (working engineers)`,
      level: "pg", contactHours, industry: "Automotive engineering", markets: [],
      textbooks: [...h.textbooks, ...h.references].map((b) => `${b.id}: ${b.text}`),
      notes: [y.description, `Handout course no: ${h.courseNos}; credit model ${y.creditModel ?? h.creditModel}; version ${h.version} (${h.date}); instructor ${h.instructor}.`, "T-ids are textbooks, R-ids reference books."].filter(Boolean).join(" "),
    },
    sources: [
      { id: "src-handout", kind: "handout", filename: handoutFile.file, mime: "text/plain", storageKey: `courses/${slugOf(dir)}/${handoutFile.file}` },
      { id: "src-yaml", kind: "other", filename: yamlFile.file, mime: "application/yaml", storageKey: `courses/${slugOf(dir)}/${yamlFile.file}` },
    ],
    modules, objectives, outcomes, plans: [classroomPlan(sessions, "Classroom (16 contact sessions)", now)],
    createdAt: now, updatedAt: now,
  });
  return {
    course, gaps, notes,
    imported: summarize(course),
  };
}
