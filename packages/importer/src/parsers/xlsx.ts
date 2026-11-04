// Parser for the Reynlab "course template" workbook (sheet Course_Info + Outcomes_And_Structure).
import ExcelJS from "exceljs";

export interface TemplateOutcome { id: string; code: string; description: string; category?: string; bloom?: string; sessionType?: string; required: boolean }
export interface TemplateLesson { number: number; name: string; day?: string; moId?: string; outcomes: TemplateOutcome[] }
export interface TemplateModule {
  number: number; name: string; description?: string;
  coId?: string; // course objective in force for this module (blank cells carry down from the row above)
  lessons: TemplateLesson[];
}
export interface ModuleTemplate {
  info: { name?: string; code?: string; days?: number; description?: string };
  cos: Record<string, { id: string; code?: string; description: string; bloom?: string }>;
  mos: Record<string, { id: string; code?: string; description: string; bloom?: string; moduleNumber: number }>;
  modules: TemplateModule[];
}

const COLS = ["Module", "Module Name", "Module Desc", "Lesson", "Lesson Name", "Day", "CO ID", "CO Code", "CO Desc", "CO Category", "CO Bloom",
  "MO ID", "MO Code", "MO Desc", "MO Category", "MO Bloom", "SO ID", "SO Code", "SO Desc", "SO Category", "SO Bloom", "Session Type", "Required"] as const;

const cell = (v: unknown): string | undefined => {
  if (v === null || v === undefined) return undefined;
  const o = v as { text?: string; result?: unknown; richText?: { text: string }[] };
  const raw = typeof v === "object" ? (o.richText ? o.richText.map((r) => r.text).join("") : (o.text ?? o.result ?? "")) : v;
  const s = String(raw).replace(/\s+/g, " ").trim();
  return s === "" ? undefined : s;
};

/** Pure function over sheet rows (header row first) so it can be unit tested without a workbook. */
export function parseOutcomeRows(rows: unknown[][]): Pick<ModuleTemplate, "cos" | "mos" | "modules"> {
  const header = (rows[0] ?? []).map((h) => cell(h) ?? "");
  const ix = (name: string) => header.indexOf(name);
  const get = (r: unknown[], name: (typeof COLS)[number]) => { const i = ix(name); return i < 0 ? undefined : cell(r[i]); };

  const cos: ModuleTemplate["cos"] = {};
  const mos: ModuleTemplate["mos"] = {};
  const modules: TemplateModule[] = [];
  let mod: TemplateModule | undefined;
  let lesson: TemplateLesson | undefined;
  let coId: string | undefined;
  let moId: string | undefined;

  for (const r of rows.slice(1)) {
    const mNum = get(r, "Module");
    if (mNum) {
      mod = { number: Number(mNum), name: get(r, "Module Name") ?? `Module ${mNum}`, description: get(r, "Module Desc"), lessons: [] };
      modules.push(mod); lesson = undefined;
    }
    const co = get(r, "CO ID");
    if (co) { coId = co; cos[co] = { id: co, code: get(r, "CO Code"), description: get(r, "CO Desc") ?? "", bloom: get(r, "CO Bloom") }; }
    if (mod && !mod.coId) mod.coId = coId;
    const lNum = get(r, "Lesson");
    const mo = get(r, "MO ID");
    if (mo) { moId = mo; if (mod) mos[mo] = { id: mo, code: get(r, "MO Code"), description: get(r, "MO Desc") ?? "", bloom: get(r, "MO Bloom"), moduleNumber: mod.number }; }
    if (lNum && mod) {
      lesson = { number: Number(lNum), name: get(r, "Lesson Name") ?? `Lesson ${lNum}`, day: get(r, "Day"), moId, outcomes: [] };
      mod.lessons.push(lesson);
    }
    const so = get(r, "SO ID");
    if (so && lesson) {
      lesson.outcomes.push({
        id: so, code: get(r, "SO Code") ?? so, description: get(r, "SO Desc") ?? "", category: get(r, "SO Category"), bloom: get(r, "SO Bloom"),
        sessionType: get(r, "Session Type"), required: (get(r, "Required") ?? "Yes").toLowerCase() !== "no",
      });
    }
  }
  return { cos, mos, modules };
}

export function parseInfoRows(rows: unknown[][]): ModuleTemplate["info"] {
  const kv = new Map(rows.slice(1).map((r) => [cell(r[0]) ?? "", cell(r[1])] as const));
  const days = kv.get("Duration (Days)");
  return { name: kv.get("Course Name"), code: kv.get("Course Code"), days: days ? Number(days) : undefined, description: kv.get("Description") };
}

export async function readModuleTemplate(path: string): Promise<ModuleTemplate> {
  const wb = new ExcelJS.Workbook();
  await wb.xlsx.readFile(path);
  const rowsOf = (name: string): unknown[][] => {
    const ws = wb.getWorksheet(name);
    if (!ws) return [];
    const out: unknown[][] = [];
    ws.eachRow({ includeEmpty: false }, (row) => { out.push((row.values as unknown[]).slice(1)); });
    return out;
  };
  return { info: parseInfoRows(rowsOf("Course_Info")), ...parseOutcomeRows(rowsOf("Outcomes_And_Structure")) };
}
