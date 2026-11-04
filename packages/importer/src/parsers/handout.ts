// Parser for the BITS Pilani "Digital Learning Handout" exported as plain text (Part A content design, Part B learning plan).
// The export puts every table cell on its own line, so the parser is a small line-oriented state machine.

export interface HandoutItem { id: string; text: string }
export interface HandoutSession { number: number; title: string; subTopics: string[]; reference?: string }

export interface Handout {
  programme?: string; // e.g. "M.Tech. Automotive Engineering/Electronics"
  division?: string;
  title?: string;
  courseNos?: string;
  creditUnits?: string;
  creditModel?: string;
  instructor?: string;
  version?: string;
  date?: string;
  description?: string;
  objectives: HandoutItem[]; // empty rows (CO4, CO5 ...) are dropped and listed in emptyObjectiveIds
  emptyObjectiveIds: string[];
  textbooks: HandoutItem[];
  references: HandoutItem[];
  outcomes: HandoutItem[];
  sessions: HandoutSession[];
}

const FIELD_LABELS: Record<string, keyof Handout> = {
  "course title": "title",
  "course no(s)": "courseNos",
  "credit units": "creditUnits",
  "credit model": "creditModel",
  "instructors": "instructor",
  "version no:": "version",
  "date:": "date",
  "course description:": "description",
};

const clean = (s: string) => s.replace(/\t/g, " ").replace(/\s+/g, " ").trim();
const isPlaceholder = (s: string) => /^[\s*]*$/.test(s) || /Chapter:\s*\*\*|Section:\s*\*\*/.test(s);

/** Collect "ID, text" pairs from a table where each id (T1, CO2, LO3 ...) sits on its own line followed by the text line(s). */
function pairs(lines: string[], idRe: RegExp): { items: HandoutItem[]; emptyIds: string[] } {
  const items: HandoutItem[] = [];
  const emptyIds: string[] = [];
  let cur: { id: string; parts: string[] } | null = null;
  const flush = () => {
    if (!cur) return;
    const text = clean(cur.parts.join(" "));
    if (text) items.push({ id: cur.id, text });
    else emptyIds.push(cur.id);
    cur = null;
  };
  for (const raw of lines) {
    const l = clean(raw);
    if (idRe.test(l)) { flush(); cur = { id: l, parts: [] }; continue; }
    if (cur && l) cur.parts.push(l);
  }
  flush();
  return { items, emptyIds };
}

function sliceBetween(lines: string[], start: RegExp, end: RegExp): string[] {
  const s = lines.findIndex((l) => start.test(clean(l)));
  if (s < 0) return [];
  let e = lines.length;
  for (let i = s + 1; i < lines.length; i++) if (end.test(clean(lines[i]!))) { e = i; break; }
  return lines.slice(s + 1, e);
}

function splitSubTopics(line: string): string[] {
  const t = clean(line.replace(/^\s*[•\-–]\s*/, ""));
  // "- A  - B  - C" exports as one line separated by " - "; bullets ("•") are one topic per line.
  return t.split(/\s+-\s+/).map(clean).filter(Boolean);
}

export function parseHandout(text: string): Handout {
  const lines = text.split(/\r?\n/);
  const out: Handout = { objectives: [], emptyObjectiveIds: [], textbooks: [], references: [], outcomes: [], sessions: [] };

  // Header block (before "Part A"): programme lines
  const partA = lines.findIndex((l) => /^Part A/i.test(clean(l)));
  const head = lines.slice(0, partA < 0 ? 0 : partA).map(clean).filter(Boolean);
  out.division = head.find((l) => /Work Integrated Learning/i.test(l));
  out.programme = head.find((l) => /^M\.?\s?Tech/i.test(l));

  // Labelled fields: value = lines until the next known label / section
  const endOfFields = lines.findIndex((l) => /^Course Objectives/i.test(clean(l)));
  const fieldLines = lines.slice(0, endOfFields < 0 ? lines.length : endOfFields);
  let label: keyof Handout | null = null;
  const vals: Partial<Record<keyof Handout, string[]>> = {};
  for (const raw of fieldLines) {
    const l = clean(raw);
    const k = FIELD_LABELS[l.toLowerCase()];
    if (k) { label = k; vals[k] = []; continue; }
    if (label && l) vals[label]!.push(l);
  }
  for (const k of Object.values(FIELD_LABELS)) {
    const v = vals[k];
    if (v && v.length) (out as unknown as Record<string, string>)[k] = k === "creditModel" ? v[0]! : v.join(" ");
  }

  const objs = pairs(sliceBetween(lines, /^Course Objectives/i, /^Text Book/i), /^CO\d+$/);
  out.objectives = objs.items; out.emptyObjectiveIds = objs.emptyIds;
  out.textbooks = pairs(sliceBetween(lines, /^Text Book/i, /^Reference Book/i), /^T\d+$/).items;
  out.references = pairs(sliceBetween(lines, /^Reference Book/i, /^Learning Outcomes/i), /^R\d+$/).items;
  out.outcomes = pairs(sliceBetween(lines, /^Learning Outcomes/i, /^Part B/i), /^LO\d+$/).items;

  // Part B: rows start with a bare session number
  const rows = sliceBetween(lines, /^Part B/i, /^Experiential Learning/i);
  let cur: HandoutSession | null = null;
  let seenHeader = false;
  for (const raw of rows) {
    const l = clean(raw);
    if (!seenHeader) { if (/^Reference$/i.test(l)) seenHeader = true; continue; }
    if (/^\d+$/.test(l)) { if (cur) out.sessions.push(cur); cur = { number: Number(l), title: "", subTopics: [] }; continue; }
    if (!cur || !l) continue;
    if (!cur.title) { cur.title = l; continue; }
    if (/^[\t ]*[•\-–]/.test(raw)) { cur.subTopics.push(...splitSubTopics(raw)); continue; }
    if (isPlaceholder(l) || /^Class Notes$/i.test(l)) continue;
    cur.reference = cur.reference ? `${cur.reference}; ${l}` : l;
  }
  if (cur) out.sessions.push(cur);
  return out;
}
