// Turn framework timings into core HourBlocks (split at hour boundaries). Nothing is invented: a block exists only
// where the framework states minutes, so the core `hourBlockProblems` rule can (and does) flag gaps and overruns.
import type { HourBlock, TeachingStyle } from "@cg/core";
import type { Framework, TimedSession } from "./parsers/framework.js";
import { provenance } from "./util.js";

type Kind = HourBlock["kind"];

interface Span { startAbs: number; minutes: number; kind: Kind; title: string; activity: string; style: TeachingStyle }

export function kindFromName(name: string): Kind {
  const n = name.toUpperCase();
  if (/BREAK/.test(n)) return "break";
  if (/SETUP|TRIGGER|HOOK|WELCOME|OPENING/.test(n)) return "hook";
  if (/RESOLUTION|WRAP|CLOSE|CLOSING|SUMMARY|TAKEAWAY/.test(n)) return "wrap";
  if (/MCQ|QUIZ|CHECK|RECALL|OBJECTIVES/.test(n)) return "check";
  if (/CASE/.test(n)) return "case";
  if (/PRACTICAL|CLIMAX|EXERCISE|ACTIVITY|INTERACTIVE|LAB|STATION|CHALLENGE/.test(n)) return "activity";
  return "teach";
}

function place(sessionId: string, spans: Span[], outcomeIds: string[], now: string, promptId: string): HourBlock[] {
  const out: HourBlock[] = [];
  let n = 0;
  for (const s of spans) {
    let start = s.startAbs;
    let left = s.minutes;
    while (left > 0) {
      const hour = Math.floor(start / 60) + 1;
      const startMin = start - (hour - 1) * 60;
      const m = Math.min(left, 60 - startMin);
      n += 1;
      out.push({
        id: `${sessionId}-B${n}`, hour, startMin, minutes: m, kind: s.kind, title: s.title, activity: s.activity, outcomeIds: [],
        style: s.style, check: [], needsSlides: false, provenance: provenance(promptId, now),
      });
      start += m; left -= m;
    }
  }
  void outcomeIds;
  return out;
}

const cap = (s: string) => s.charAt(0).toUpperCase() + s.slice(1).toLowerCase();

/** Story-arc frameworks: phases are laid end to end; a stated trailing Q&A becomes a closing block. */
export function blocksFromFramework(sessionId: string, fw: Framework, style: TeachingStyle, now: string): HourBlock[] {
  if (!fw.phases.length) return [];
  const spans: Span[] = [];
  let cursor = 0;
  for (const p of fw.phases) {
    const kind = kindFromName(/^PART\s*\d+$/i.test(p.name) ? p.title : p.name);
    const practical = /PRACTICAL|LAB/i.test(p.name);
    const named = p.title.toLowerCase() !== p.name.toLowerCase();
    spans.push({
      startAbs: cursor, minutes: p.minutes, kind, title: named ? `${cap(p.name)}: ${p.title}` : cap(p.name),
      activity: `Instructor-led ${p.name.toLowerCase()} phase${p.slides ? ` (slides ${p.slides})` : ""}${named ? `: ${p.title}` : ""}`,
      style: practical ? "lab" : style,
    });
    cursor += p.minutes;
  }
  if (fw.qaMin) spans.push({ startAbs: cursor, minutes: fw.qaMin, kind: "wrap", title: "Q&A", activity: "Questions and answers after the lecture", style: "discussion" });
  return place(sessionId, spans, [], now, "import.framework");
}

/** Session templates with explicit [a-b min] ranges (AEZC516). */
export function blocksFromTimed(sessionId: string, s: TimedSession, style: TeachingStyle, now: string): HourBlock[] {
  const spans: Span[] = s.blocks
    .filter((b) => b.endMin > b.startMin)
    .map((b) => ({
      startAbs: b.startMin, minutes: b.endMin - b.startMin, kind: kindFromName(b.title), title: b.title,
      activity: (b.text || b.title).slice(0, 400), style: /MCQ/i.test(b.title) ? "retrieval" : style,
    }));
  return place(sessionId, spans, [], now, "import.timed-template");
}
