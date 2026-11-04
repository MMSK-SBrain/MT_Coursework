// Parsers for the three course-data.yaml dialects found in courses/.
import { parse } from "yaml";

type Obj = Record<string, unknown>;
const obj = (v: unknown): Obj => (v && typeof v === "object" && !Array.isArray(v) ? (v as Obj) : {});
const arr = (v: unknown): Obj[] => (Array.isArray(v) ? v.map(obj) : []);
const str = (v: unknown): string | undefined => (v === undefined || v === null ? undefined : String(v).replace(/\s+/g, " ").trim());
const strs = (v: unknown): string[] => (Array.isArray(v) ? v.map((x) => str(x) ?? "").filter(Boolean) : []);
const num = (v: unknown): number | undefined => (typeof v === "number" ? v : undefined);

export type YamlDialect = "systems-engineering" | "vehicles" | "weeks";

export function detectDialect(text: string): YamlDialect | null {
  const d = obj(parse(text));
  if (Array.isArray(d.weeks)) return "weeks";
  if (Array.isArray(d.course_outcomes)) return "vehicles";
  if (Array.isArray(d.sessions) && Array.isArray(d.modules)) return "systems-engineering";
  return null;
}

// ---- AEZC517 style: objectives / learning_outcomes / modules (by session number) / sessions ----------------------

export interface SeYaml {
  title?: string; code?: string; shortCode?: string; creditModel?: string; version?: string; date?: string;
  instructor?: string; description?: string;
  objectives: { id: string; description: string }[];
  outcomes: { id: string; description: string; level?: string }[];
  textbooks: { id: string; title: string; authors?: string; edition?: string; year?: number }[];
  references: { id: string; title: string; authors?: string; edition?: string; year?: number }[];
  modules: { number: number; title: string; description?: string; sessions: number[] }[];
  sessions: { number: number; title: string; duration?: number; approach?: string; topics: string[]; learningOutcomes: string[]; references: string[] }[];
}

export function parseSeYaml(text: string): SeYaml {
  const d = obj(parse(text));
  const c = obj(d.course);
  const book = (o: Obj) => ({ id: str(o.id) ?? "", title: str(o.title) ?? "", authors: str(o.authors), edition: str(o.edition), year: num(o.year) });
  return {
    title: str(c.title), code: str(c.code), shortCode: str(c.short_code), creditModel: str(c.credit_model), version: str(c.version),
    date: str(c.date), instructor: str(c.instructor), description: str(c.description),
    objectives: arr(d.objectives).map((o) => ({ id: str(o.id) ?? "", description: str(o.description) ?? "" })),
    outcomes: arr(d.learning_outcomes).map((o) => ({ id: str(o.id) ?? "", description: str(o.description) ?? "", level: str(o.level) })),
    textbooks: arr(d.textbooks).map(book),
    references: arr(d.references).map(book),
    modules: arr(d.modules).map((m) => ({
      number: num(m.number) ?? 0, title: str(m.title) ?? "", description: str(m.description),
      sessions: Array.isArray(m.sessions) ? (m.sessions as unknown[]).filter((x): x is number => typeof x === "number") : [],
    })),
    sessions: arr(d.sessions).map((s) => ({
      number: num(s.number) ?? 0, title: str(s.title) ?? "", duration: num(s.duration), approach: str(s.approach),
      topics: strs(s.topics), learningOutcomes: strs(s.learning_outcomes), references: strs(s.references),
    })),
  };
}

// ---- AELZC441 style: course_outcomes / modules[].lessons[].session_outcomes[] -----------------------------------

export interface VehiclesYaml {
  name?: string; code?: string; credits?: number; totalSessions?: number; sessionDuration?: string; institution?: string;
  description?: string;
  courseOutcomes: { id: string; code?: string; description: string; bloom?: string }[];
  modules: {
    number: number; name: string; description?: string; durationSessions?: number;
    moduleOutcome?: { id: string; description: string; bloom?: string; parentCo: string[] };
    lessons: {
      number: number; name: string; day?: number;
      outcomes: { id: string; code?: string; description: string; bloom?: string; sessionType?: string; parentMo?: string }[];
    }[];
  }[];
}

export function parseVehiclesYaml(text: string): VehiclesYaml {
  const d = obj(parse(text));
  const c = obj(d.course);
  return {
    name: str(c.name), code: str(c.code), credits: num(c.credits), totalSessions: num(c.total_sessions),
    sessionDuration: str(c.session_duration), institution: str(c.institution), description: str(c.description),
    courseOutcomes: arr(d.course_outcomes).map((o) => ({ id: str(o.id) ?? "", code: str(o.code), description: str(o.description) ?? "", bloom: str(o.bloom_level) })),
    modules: arr(d.modules).map((m) => {
      const mo = obj(m.module_outcome);
      const pc = mo.parent_co;
      return {
        number: num(m.number) ?? 0, name: str(m.name) ?? "", description: str(m.description), durationSessions: num(m.duration_sessions),
        moduleOutcome: m.module_outcome
          ? { id: str(mo.id) ?? "", description: str(mo.description) ?? "", bloom: str(mo.bloom_level), parentCo: Array.isArray(pc) ? strs(pc) : pc ? [String(pc)] : [] }
          : undefined,
        lessons: arr(m.lessons).map((l) => ({
          number: num(l.number) ?? 0, name: str(l.name) ?? "", day: num(l.day),
          outcomes: arr(l.session_outcomes).map((o) => ({
            id: str(o.id) ?? "", code: str(o.code), description: str(o.description) ?? "", bloom: str(o.bloom_level),
            sessionType: str(o.session_type), parentMo: str(o.parent_mo),
          })),
        })),
      };
    }),
  };
}

// ---- TUV SUD style: stages / weeks[].days[] ----------------------------------------------------------------------

export interface WeeksYaml {
  title?: string; code?: string; version?: string; date?: string; programDuration?: string; format?: string;
  totalDays?: number; totalHours?: number; certification?: string; examFormat?: string; description?: string; designPhilosophy?: string;
  stages: { name: string; weeks: number[]; description?: string }[];
  weeks: {
    number: number; title: string; subtitle?: string; stage?: string; examWeightMarks?: number; story?: string;
    days: { day: number; theme: string; theoryPractice?: string; topics: string[] }[];
  }[];
}

export function parseWeeksYaml(text: string): WeeksYaml {
  const d = obj(parse(text));
  const c = obj(d.course);
  return {
    title: str(c.title), code: str(c.code), version: str(c.version), date: str(c.date), programDuration: str(c.program_duration),
    format: str(c.format), totalDays: num(c.total_days), totalHours: num(c.total_hours), certification: str(c.certification),
    examFormat: str(c.exam_format), description: str(c.description), designPhilosophy: str(c.design_philosophy),
    stages: arr(d.stages).map((s) => ({ name: str(s.name) ?? "", weeks: Array.isArray(s.weeks) ? (s.weeks as number[]) : [], description: str(s.description) })),
    weeks: arr(d.weeks).map((w) => ({
      number: num(w.number) ?? 0, title: str(w.title) ?? "", subtitle: str(w.subtitle), stage: str(w.stage), examWeightMarks: num(w.exam_weight_marks), story: str(w.story),
      days: arr(w.days).map((x) => ({ day: num(x.day) ?? 0, theme: str(x.theme) ?? "", theoryPractice: str(x.theory_practice), topics: strs(x.topics) })),
    })),
  };
}
