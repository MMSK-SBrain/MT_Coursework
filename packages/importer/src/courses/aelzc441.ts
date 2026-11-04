// AELZC441 Automotive Vehicles: course-data.yaml (CO > MO > SO hierarchy) + requirements.md + SESSION-nn lecture frameworks.
import { Course, type Module, type Session } from "@cg/core";
import { parseVehiclesYaml } from "../parsers/courseYaml.js";
import { plain, provenance, round1 } from "../util.js";
import { blocksFor, classroomPlan, frameworkFiles, makeOutcome, readText, slugOf, type ImportContext, type ImportResult } from "./common.js";

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

  const modules: Module[] = y.modules.map((m) => ({
    id: `M${m.number}`, title: m.name, hours: round1(m.lessons.length * 2),
    topics: m.lessons.map((l) => l.name), foundIn: "user",
    note: [m.description, m.moduleOutcome ? `Module outcome ${m.moduleOutcome.id.toUpperCase()}: ${m.moduleOutcome.description}` : ""].filter(Boolean).join(" "),
  }));
  notes.push("Modules come from course-data.yaml; the module outcomes (MO) have no slot in the model and are kept in each module's note. foundIn is \"user\".");

  const objectives = y.courseOutcomes.map((c) => ({ id: coId(c.id), text: c.description, locked: false, provenance: provenance("import.yaml", now) }));

  const tally = { statedMismatch: [] as string[], defaulted: [] as string[] };
  const outcomes = y.modules.flatMap((m) =>
    m.lessons.flatMap((l) =>
      l.outcomes.map((o) =>
        makeOutcome({
          id: (o.code ?? o.id).replace(/^[A-Z0-9]+-(?=SO-)/, ""), text: o.description, stated: o.bloom, moduleIds: [`M${m.number}`],
          objectiveIds: (m.moduleOutcome?.parentCo ?? []).map(coId), now, promptId: "import.yaml",
        }, tally))));
  if (tally.statedMismatch.length) notes.push(`Bloom taken from the leading verb; the yaml level differed for ${tally.statedMismatch.length} of ${outcomes.length} session outcomes (first: ${tally.statedMismatch.slice(0, 3).join("; ")}).`);
  if (tally.defaulted.length) gaps.push(`Bloom defaulted to "understand" (verb unknown, no stated level): ${tally.defaulted.join(", ")}`);
  notes.push("Outcomes are the yaml session outcomes (SO). objectiveIds come from the module outcome's parent_co in the yaml.");

  const sessions: Session[] = y.modules.flatMap((m) => m.lessons.map((l): Session => {
    const id = `S${l.number}`;
    const ids = l.outcomes.map((o) => (o.code ?? o.id).replace(/^[A-Z0-9]+-(?=SO-)/, ""));
    const numerical = l.outcomes.filter((o) => o.sessionType === "numerical").length;
    const style = numerical * 2 >= l.outcomes.length ? "worked" : "teaching";
    const fw = fws.get(l.number)?.fw;
    const blocks = blocksFor(id, fw, style, now);
    if (!blocks.length) gaps.push(`Session ${l.number} (${l.name}): ${fws.has(l.number) ? "the lecture framework has no timed phases in the story-arc format" : "no lecture framework file exists"}; no blocks imported.`);
    return { id, index: l.number, title: l.name, outcomeIds: ids, style, minutes: 120, video: "none", blocks, links: [], caseStudies: [], assets: [], stale: false, provenance: provenance("import.yaml", now) };
  }));
  notes.push("Session style: \"worked\" when at least half of the session's outcomes are numerical, else \"teaching\". Session length 120 min (90 lecture + 30 Q&A) per the yaml.");
  if (sessions.length !== (y.totalSessions ?? sessions.length)) gaps.push(`yaml declares ${y.totalSessions} sessions, found ${sessions.length}.`);

  gaps.push("No textbooks or reference books are listed in the yaml, requirements.md or README; brief.textbooks is empty.");
  gaps.push("No BITS handout .txt exists for this course; code, credits and audience come from the yaml and requirements.md.");
  gaps.push("Markets are not stated in the sources: defaulted to [\"India\"] (core requires at least one).");
  gaps.push("Module hours are derived as 2 h per session (the yaml gives session counts, not hours).");

  const course = Course.parse({
    id: slugOf(dir), slug: slugOf(dir),
    brief: {
      title: y.name ?? "Automotive Vehicles", code: y.code,
      audience: [field(req, "Primary Learners"), field(req, "Background")].filter(Boolean).map((s) => plain(s!)).join(" - ") || y.institution || "M.Tech. Automotive Electronics (BITS Pilani WILP)",
      level: "pg", contactHours: round1(sessions.length * 2),
      industry: field(req, "Industry/Domain") ?? "Automotive engineering", markets: ["India"], textbooks: [],
      notes: [y.description, y.institution ? `Institution: ${y.institution}.` : "", `Credits: ${y.credits}.`, `Session length: ${y.sessionDuration}.`].filter(Boolean).join(" "),
    },
    sources: [{ id: "src-yaml", kind: "other", filename: yamlFile.file, mime: "application/yaml", storageKey: `courses/${slugOf(dir)}/${yamlFile.file}` }],
    modules, objectives, outcomes, plans: [classroomPlan(sessions, "Classroom (20 contact sessions)", now)],
    createdAt: now, updatedAt: now,
  });
  return {
    course, gaps, notes,
    imported: [`${modules.length} modules`, `${objectives.length} objectives`, `${outcomes.length} outcomes`, `${sessions.length} sessions`, `${sessions.reduce((a, s) => a + s.blocks.length, 0)} hour blocks`],
  };
}
