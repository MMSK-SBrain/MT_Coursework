// Worked examples for few-shot prompts, loaded from courses/*/course.json at the repo root.
// Tolerates a missing directory, unreadable files and files that fail the Course schema;
// falls back to one small inline AEZC517 example so prompts and tests always have one.
import { Course as CourseSchema, type Course } from "@cg/core";
import type { StageName } from "./config.js";
import { aezc517Course } from "./fixtures/aezc517.js";

export interface ExampleStoreOptions {
  /** Directory holding <slug>/course.json. Default: CG_COURSES_DIR or <repo>/courses. */
  coursesDir?: string;
  /** Used when no course files load. Default: the inline AEZC517 example. */
  inline?: Course[];
}

/** CG_COURSES_DIR, else the `courses` folder beside the nearest pnpm-workspace.yaml above the working directory. */
export async function defaultCoursesDir(): Promise<string | undefined> {
  if (typeof process === "undefined") return undefined;
  if (process.env.CG_COURSES_DIR) return process.env.CG_COURSES_DIR;
  const fs = await import("node:fs");
  const path = await import("node:path");
  for (let dir = process.cwd(); ; dir = path.dirname(dir)) {
    if (fs.existsSync(path.join(dir, "pnpm-workspace.yaml"))) return path.join(dir, "courses");
    if (path.dirname(dir) === dir) return undefined;
  }
}

export async function loadCourseFiles(dir: string): Promise<{ courses: Course[]; skipped: string[] }> {
  const courses: Course[] = [];
  const skipped: string[] = [];
  let fs: typeof import("node:fs/promises");
  let path: typeof import("node:path");
  try {
    fs = await import("node:fs/promises");
    path = await import("node:path");
  } catch {
    return { courses, skipped: ["node:fs unavailable"] };
  }
  let entries: string[];
  try {
    entries = (await fs.readdir(dir, { withFileTypes: true })).filter((e) => e.isDirectory()).map((e) => e.name).sort();
  } catch {
    return { courses, skipped }; // directory missing: fine
  }
  for (const name of entries) {
    const file = path.join(dir, name, "course.json");
    let text: string;
    try {
      text = await fs.readFile(file, "utf8");
    } catch {
      continue; // a course folder without course.json
    }
    try {
      const parsed = CourseSchema.safeParse(JSON.parse(text));
      if (parsed.success) courses.push(parsed.data);
      else skipped.push(`${name}: ${parsed.error.issues[0]?.path.join(".")} ${parsed.error.issues[0]?.message}`);
    } catch (e) {
      skipped.push(`${name}: ${(e as Error).message}`);
    }
  }
  return { courses, skipped };
}

export class ExampleStore {
  private cache?: Promise<Course[]>;
  skipped: string[] = [];

  constructor(private readonly opts: ExampleStoreOptions = {}) {}

  courses(): Promise<Course[]> {
    this.cache ??= (async () => this.opts.coursesDir ?? (await defaultCoursesDir()))()
      .then((dir) => (dir ? loadCourseFiles(dir) : { courses: [], skipped: ["no courses directory found"] }))
      .then(({ courses, skipped }) => {
      this.skipped = skipped;
        return courses.length ? courses : this.opts.inline ?? [aezc517Course()];
      });
    return this.cache;
  }

  /**
   * Rendered few-shot text for a stage. `exclude` is the course being generated (by id or code),
   * so a course is never its own example; if every example is excluded, none is used.
   */
  async forStage(stage: StageName, opts: { exclude?: { id?: string; code?: string }; max?: number } = {}): Promise<string> {
    const max = opts.max ?? 1;
    const all = await this.courses();
    const picked = all
      .filter((c) => !(opts.exclude && ((opts.exclude.id && c.id === opts.exclude.id) || (opts.exclude.code && c.brief.code === opts.exclude.code))))
      .map((c) => renderExample(stage, c))
      .filter((s): s is string => !!s)
      .slice(0, max);
    return picked.join("\n\n");
  }
}

const mods = (c: Course) => c.modules.map((m) => `${m.id} (${m.hours} h): ${m.title}`).join("; ");

/** One course rendered as an input -> output example for a stage, or null if the course lacks that data. */
export function renderExample(stage: StageName, c: Course): string | null {
  const head = `Example course: ${c.brief.code ?? ""} ${c.brief.title} (${c.brief.level}, ${c.brief.contactHours} h, ${c.brief.industry})`;
  switch (stage) {
    case "findRoles": {
      if (!c.roles.length) return null;
      return `${head}\nModules: ${mods(c)}\nRoles: ${JSON.stringify(c.roles.slice(0, 5).map((r) => ({ title: r.title, skills: r.skills, matchedSkills: r.matchedSkills, moduleMatch: r.moduleMatch })))}`;
    }
    case "proposeFit": {
      if (!c.fit.length) return null;
      return `${head}\nModules: ${mods(c)}\nOutput: ${JSON.stringify({ changes: c.fit.slice(0, 5).map(({ kind, text, reason, targetModuleId, hoursDelta, roleIds, academicConflict }) => ({ kind, text, reason, targetModuleId, hoursDelta, roleIds, ...(academicConflict ? { academicConflict } : {}) })) })}`;
    }
    case "draftOutcomes":
    case "suggestOutcomeEdit": {
      if (!c.outcomes.length) return null;
      return `${head}\nModules: ${mods(c)}\nOutput: ${JSON.stringify({
        objectives: c.objectives.map(({ id, text }) => ({ id, text })),
        outcomes: c.outcomes.slice(0, 8).map(({ id, text, bloom, moduleIds, objectiveIds, roleIds, origin }) => ({ id, text, bloom, moduleIds, objectiveIds, roleIds, origin })),
        moduleOutcomes: c.modules.flatMap((m) => m.outcomes.slice(0, 2).map((mo) => ({ moduleId: m.id, text: mo.text, bloom: mo.bloom, outcomeIds: mo.outcomeIds }))).slice(0, 10),
      })}`;
    }
    case "draftPlan": {
      const p = c.plans[0];
      if (!p) return null;
      return `${head}\nPath: ${p.path}, default style ${p.defaultStyle}\nOutput: ${JSON.stringify({ name: p.name, sessions: p.sessions.slice(0, 8).map(({ title, outcomeIds, style, minutes, video, sessionOutcomes }) => ({ title, outcomeIds, style, minutes, video, sessionOutcomes: sessionOutcomes.map(({ text, bloom, moduleOutcomeIds }) => ({ text, bloom, moduleOutcomeIds })) })) })}`;
    }
    case "draftHourPlan": {
      const s = c.plans.flatMap((p) => p.sessions).find((x) => x.blocks.length);
      if (!s) return null;
      return `${head}\nSession: ${s.title} (${s.minutes} min, style ${s.style})\nSession outcomes: ${s.sessionOutcomes.map((o) => `${o.id} [${o.bloom}] ${o.text}`).join("; ") || "(none)"}\nOutput: ${JSON.stringify({ blocks: s.blocks.map(({ hour, startMin, minutes, kind, title, activity, outcomeIds, sessionOutcomeIds, style, check, needsSlides, industryExample }) => ({ hour, startMin, minutes, kind, title, activity, outcomeIds, sessionOutcomeIds, style, check, needsSlides, ...(industryExample ? { industryExample: { text: industryExample.text, sector: industryExample.sector, roleIds: industryExample.roleIds } } : {}) })) })}`;
    }
    case "draftCaseStudy": {
      const cs = c.plans.flatMap((p) => p.sessions).flatMap((s) => s.caseStudies)[0];
      if (!cs) return null;
      return `${head}\nOutput: ${JSON.stringify({ title: cs.title, background: cs.background, data: cs.data, questions: cs.questions, teachingNote: cs.teachingNote })}`;
    }
    case "parseInputs":
      return `${head}\nModules extracted: ${mods(c)}`;
    default:
      return null;
  }
}
