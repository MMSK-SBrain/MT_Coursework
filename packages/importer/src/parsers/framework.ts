// Parsers for the lecture-framework markdown files.
//  - "story arc" frameworks: `### **SETUP: Title** (Slides 1-5, ~15 minutes)` phases laid end to end
//  - "session template" files: `**Hook [0-5 min]:**` blocks with explicit minute ranges (AEZC516)
//  - the "Session Objectives" bullet list
import { plain } from "../util.js";

export interface FrameworkPhase { name: string; title: string; minutes: number; slides?: string }
export interface Framework {
  title?: string;
  approach?: string;
  durationMin?: number; // total session length if the header states one
  qaMin?: number; // trailing Q&A minutes if the header says "90 minutes lecture + 30 minutes Q&A"
  objectives: string[];
  phases: FrameworkPhase[];
  frontMatter: Record<string, string>;
}

export function parseFrontMatter(md: string): Record<string, string> {
  const m = /^---\r?\n([\s\S]*?)\r?\n---/.exec(md);
  const out: Record<string, string> = {};
  if (!m) return out;
  for (const l of m[1]!.split(/\r?\n/)) {
    const k = /^([A-Za-z_]+):\s*"?(.*?)"?\s*$/.exec(l);
    if (k) out[k[1]!] = k[2]!;
  }
  return out;
}

export function parseObjectives(md: string): string[] {
  const lines = md.split(/\r?\n/);
  const s = lines.findIndex((l) => /^#{2,3}\s.*Objectives/i.test(l));
  if (s < 0) return [];
  const out: string[] = [];
  for (const l of lines.slice(s + 1)) {
    if (/^\s*[-*]\s+/.test(l)) out.push(plain(l.replace(/^\s*[-*]\s+/, "")));
    else if (/^#/.test(l) || /^---/.test(l)) break;
    else if (/^\*\*Mapped/.test(l)) break;
  }
  return out;
}

const PHASE_RE = /^###\s+\**\s*([^:*]+?)\s*(?::\s*(.*?))?\**\s*\(([^)]*?)~\s*(\d+)\s*min/;

export function parseFramework(md: string): Framework {
  const lines = md.split(/\r?\n/);
  const fm = parseFrontMatter(md);
  const title = lines.find((l) => /^#\s+/.test(l))?.replace(/^#\s+/, "").trim();
  const approach = /\*\*Approach:\*\*\s*(.+)/.exec(md)?.[1]?.trim();
  const dur = /\*\*Duration:\*\*\s*(.+)/.exec(md)?.[1] ?? "";
  let durationMin: number | undefined;
  let qaMin: number | undefined;
  const lecQa = /(\d+)\s*min(?:ute)?s?\s*lecture\s*\+\s*(\d+)\s*min(?:ute)?s?\s*Q&A/i.exec(dur);
  if (lecQa) { durationMin = Number(lecQa[1]) + Number(lecQa[2]); qaMin = Number(lecQa[2]); }
  else {
    const one = /(\d+)\s*min/i.exec(dur);
    if (one) durationMin = Number(one[1]);
  }
  if (fm.duration_minutes) durationMin = Number(fm.duration_minutes);

  const phases: FrameworkPhase[] = [];
  for (const l of lines) {
    const m = PHASE_RE.exec(l);
    if (!m) continue;
    const slides = /Slides?\s+([\d\-–]+)/i.exec(m[3]!)?.[1];
    phases.push({ name: plain(m[1]!), title: plain(m[2] ?? m[1]!), minutes: Number(m[4]), slides });
  }
  return { title, approach, durationMin, qaMin, objectives: parseObjectives(md), phases, frontMatter: fm };
}

// ---- Session templates with minute ranges ------------------------------------------------------------------------

export interface TimedBlock { title: string; startMin: number; endMin: number; text: string }
export interface TimedSession { number: number; title: string; minutes: number; outcomeIds: string[]; blocks: TimedBlock[] }

export function parseTimedTemplates(md: string): TimedSession[] {
  const lines = md.split(/\r?\n/);
  const sessions: TimedSession[] = [];
  let cur: TimedSession | undefined;
  let open: TimedBlock | undefined;
  const flush = () => { if (open && cur) cur.blocks.push(open); open = undefined; };
  for (const l of lines) {
    const h = /^###\s+SESSION\s+(\d+):\s*(.*?)\s*\((\d+)\s*min\)/i.exec(l);
    if (h) { flush(); cur = { number: Number(h[1]), title: plain(h[2]!), minutes: Number(h[3]), outcomeIds: [], blocks: [] }; sessions.push(cur); continue; }
    if (!cur) continue;
    const lo = /^\*\*Learning Outcomes:\*\*\s*(.+)/.exec(l);
    if (lo) { cur.outcomeIds = lo[1]!.split(/[,;]/).map((x) => x.trim()).filter(Boolean); continue; }
    // top-level block: **Title [a-b min]:**   or a nested bullet such as `- **MCQ #1 [30-32 min]:** text`
    const b = /^(?:[-*]\s+)?\*\*(.+?)\s*\[(\d+)\s*[-–]\s*(\d+)\s*min\]\s*:?\*\*:?\s*(.*)$/.exec(l);
    if (b) {
      const nested = /^[-*]\s/.test(l);
      if (nested) { // a timed bullet inside a Part: keep it as its own block, close the parent's text there
        const parent = open; flush();
        if (cur) cur.blocks.push({ title: plain(b[1]!), startMin: Number(b[2]), endMin: Number(b[3]), text: plain(b[4]!) });
        if (parent) open = undefined;
        continue;
      }
      flush();
      open = { title: plain(b[1]!), startMin: Number(b[2]), endMin: Number(b[3]), text: plain(b[4]!) };
      continue;
    }
    if (/^\*\*(Materials Needed|Delivery Notes|Key Teaching Points|Assessment Points)/i.test(l) || /^---/.test(l)) { flush(); continue; }
    if (open && /^\s*[-*]\s+/.test(l)) open.text = (open.text + " " + plain(l.replace(/^\s*[-*]\s+/, ""))).trim();
  }
  flush();
  return sessions;
}
