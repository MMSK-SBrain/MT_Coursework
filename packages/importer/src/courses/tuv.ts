// TUV SUD Automotive Service Technician: course-data.yaml (weeks/days) + DAY-nn lecture frameworks (session objectives, phase timings).
import { Course, type Module, type Session, type TeachingStyle } from "@cg/core";
import { parseWeeksYaml } from "../parsers/courseYaml.js";
import { provenance, round1 } from "../util.js";
import { blocksFor, classroomPlan, frameworkFiles, makeOutcome, readText, slugOf, type ImportContext, type ImportResult } from "./common.js";

const pad = (n: number) => String(n).padStart(2, "0");

export function importWeeks(ctx: ImportContext): ImportResult {
  const { dir, now } = ctx;
  const gaps: string[] = [];
  const notes: string[] = [];
  const yamlFile = readText(dir, "course-data.yaml");
  if (!yamlFile) throw new Error(`${dir}: need course-data.yaml`);
  const y = parseWeeksYaml(yamlFile.text);
  const fws = frameworkFiles(dir, "lecture-frameworks", "DAY");

  const modules: Module[] = y.weeks.map((w) => ({
    id: `M${w.number}`, title: w.title, hours: round1(w.days.length * 3), topics: w.days.map((d) => d.theme), foundIn: "import",
    note: [w.subtitle, w.stage ? `Stage: ${w.stage}.` : "", w.story].filter(Boolean).join(" "),
  }));
  notes.push("Modules are the 11 weeks of course-data.yaml (weeks 9-11 are the optional extension); 3 h per day. foundIn is \"user\" (no handout or module sheet exists).");

  const tally = { statedMismatch: [] as string[], defaulted: [] as string[] };
  const outcomes = [] as ReturnType<typeof makeOutcome>[];
  const sessions: Session[] = [];
  for (const w of y.weeks) {
    for (const d of w.days) {
      const fwEntry = fws.get(d.day);
      const objs = fwEntry?.fw.objectives ?? [];
      if (!objs.length) gaps.push(`Day ${d.day}: no "Session Objectives" in a lecture framework; day skipped.`);
      const ids = objs.map((text, i) => {
        const id = `D${pad(d.day)}-O${i + 1}`;
        outcomes.push(makeOutcome({ id, text, moduleIds: [`M${w.number}`], now, promptId: "import.framework" }, tally));
        return id;
      });
      const practical = Number(d.theoryPractice?.split(":")[1] ?? 0);
      const style: TeachingStyle = practical >= 60 ? "lab" : "teaching";
      const id = `S${d.day}`;
      const blocks = blocksFor(id, fwEntry?.fw, style, now);
      if (!blocks.length) gaps.push(`Day ${d.day}: no timed phases found; no blocks imported.`);
      const minutes = Number(fwEntry?.fw.durationMin) || 180;
      sessions.push({ id, index: d.day, title: d.theme, outcomeIds: ids, style, minutes, video: "none", blocks, links: [], caseStudies: [], assets: [], stale: false, provenance: provenance("import.yaml", now) });
    }
  }
  const usable = sessions.filter((s) => s.outcomeIds.length);
  notes.push("Outcomes are the bullet lists under \"Session Objectives (For Instructor)\" in each DAY framework (5-11 per day); they are lecture-framework objectives, not handout text. ids D<day>-O<n>; origin is still marked \"handout\" as instructed.");
  notes.push("Session style: \"lab\" when the yaml practical share (T:P) is 60% or more, else \"teaching\". Session length from the framework front matter (180 min).");
  if (tally.defaulted.length) gaps.push(`Bloom defaulted to "understand" (verb not recognised): ${tally.defaulted.length} outcomes, e.g. ${tally.defaulted.slice(0, 5).join(", ")}`);

  gaps.push("No course objectives (CO) exist anywhere in the sources; objectives is empty. Outcomes have no objectiveIds.");
  gaps.push("No handout or module sheet: program-level outcomes are absent. The 55 question banks (question-banks/DAY-nn-questions.json) and exam-weight marks per week are outside the Course model; not imported.");
  gaps.push("Audience, industry and market are not stated as fields: audience from the design philosophy, industry derived from the certification name, markets not set (the teacher sets them before the job search).");

  const course = Course.parse({
    id: slugOf(dir), slug: slugOf(dir),
    brief: {
      title: y.title ?? "TUV SUD Automotive Service Technician", code: y.code,
      audience: "Learners with zero automotive background, taken to TUV SUD certification readiness",
      level: "vocational", contactHours: y.totalHours ?? round1(sessions.reduce((a, s) => a + s.minutes, 0) / 60),
      industry: "Automotive service and repair (workshop technicians)", markets: [], textbooks: [],
      notes: [y.description, y.programDuration ? `Programme: ${y.programDuration}.` : "", y.format ? `Format: ${y.format}.` : "", y.certification ? `Certification: ${y.certification}.` : "", y.examFormat ? `Exam: ${y.examFormat}.` : "", `Version ${y.version} (${y.date}).`].filter(Boolean).join(" "),
    },
    sources: [{ id: "src-yaml", kind: "other", filename: yamlFile.file, mime: "application/yaml", storageKey: `courses/${slugOf(dir)}/${yamlFile.file}` }],
    modules, objectives: [], outcomes, plans: [classroomPlan(usable, "Classroom (55 days x 3 h)", now)],
    createdAt: now, updatedAt: now,
  });
  return {
    course, gaps, notes,
    imported: [`${modules.length} modules`, "0 objectives", `${outcomes.length} outcomes`, `${usable.length} sessions`, `${usable.reduce((a, s) => a + s.blocks.length, 0)} hour blocks`],
  };
}
