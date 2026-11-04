import PptxGenJS from "pptxgenjs";
import type { Course, HourBlock } from "@cg/core";
import { findSession, outcomeText, sentences, sortedBlocks } from "./util.js";

export interface SlideTheme {
  background: string;
  title: string;
  text: string;
  muted: string;
  accent: string;
  panel: string; // image placeholder fill
  font: string;
}

export const THEMES = {
  /** Plain white default. */
  default: { background: "FFFFFF", title: "1F2937", text: "1F2937", muted: "6B7280", accent: "2563EB", panel: "F3F4F6", font: "Calibri" },
  /** Inspired by reference/dark_theme.css (GitHub-dark palette). */
  dark: { background: "0D1117", title: "E6EDF3", text: "E6EDF3", muted: "8B949E", accent: "58A6FF", panel: "161B22", font: "Inter" },
} satisfies Record<string, SlideTheme>;

export type ThemeName = keyof typeof THEMES;
export interface SlideOptions { theme?: ThemeName | SlideTheme }

const MAX_BULLETS = 4;

/** Short slide text: whole sentence if it fits, else cut at the last clause boundary that fits (never an ellipsis; the full text is in the notes). */
function shortBullet(text: string, max: number): string {
  const t = text.trim().replace(/\.$/, "");
  if (t.length <= max) return t;
  let cut = -1;
  for (const m of t.matchAll(/,| into | and | then | with | to | so | when | where /g)) {
    if (m.index! > 20 && m.index! <= max) cut = m.index!;
  }
  if (cut > 0) return t.slice(0, cut).trim();
  const words = t.split(/\s+/);
  let out = "";
  for (const w of words) { if ((out + " " + w).trim().length > max) break; out = (out + " " + w).trim(); }
  return out;
}

/** Bullets for the slide face: the example, then the activity's sentences kept short. Full prose goes to notes. */
function faceBullets(b: HourBlock): string[] {
  const out = sentences(b.activity).map((s) => shortBullet(s, 90));
  if (b.industryExample) out.push(`In industry: ${shortBullet(b.industryExample.text, 90)}`);
  for (const q of b.check) out.push(`Check: ${shortBullet(q, 80)}`);
  return out;
}

export async function slidesExport(course: Course, planId: string, sessionId: string, opts: SlideOptions = {}): Promise<Uint8Array> {
  const { plan, session } = findSession(course, planId, sessionId);
  const t: SlideTheme = typeof opts.theme === "object" ? opts.theme : THEMES[opts.theme ?? "default"];
  const pres = new PptxGenJS();
  pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5 in
  pres.title = `${course.brief.title}: ${session.title}`;
  pres.defineSlideMaster({ title: "CG", background: { color: t.background } });

  const heading = (s: PptxGenJS.Slide, text: string) =>
    s.addText(text, { x: 0.6, y: 0.4, w: 12.1, h: 0.9, fontFace: t.font, fontSize: 30, bold: true, color: t.title });
  const footer = (s: PptxGenJS.Slide) =>
    s.addText(`${course.brief.code ?? course.brief.title} | Session ${session.index}`, { x: 0.6, y: 7.0, w: 12.1, h: 0.3, fontFace: t.font, fontSize: 10, color: t.muted });
  const bullets = (s: PptxGenJS.Slide, items: string[], w: number) =>
    s.addText(items.map((text) => ({ text, options: { bullet: true, breakLine: true } })), {
      x: 0.6, y: 1.5, w, h: 5.3, valign: "top", fontFace: t.font, fontSize: 22, color: t.text, paraSpaceAfter: 12,
    });
  const imageArea = (s: PptxGenJS.Slide) =>
    s.addText("Image area", { x: 8.2, y: 1.5, w: 4.5, h: 5.2, align: "center", valign: "middle", fontFace: t.font, fontSize: 14, color: t.muted, fill: { color: t.panel }, line: { color: t.muted, dashType: "dash", width: 1 } });

  // Title
  const title = pres.addSlide({ masterName: "CG" });
  title.addShape(pres.ShapeType.rect, { x: 0.6, y: 2.6, w: 0.15, h: 1.8, fill: { color: t.accent }, line: { color: t.accent } });
  title.addText(session.title, { x: 1.0, y: 2.5, w: 11.5, h: 1.2, fontFace: t.font, fontSize: 40, bold: true, color: t.title, valign: "top" });
  title.addText(`${course.brief.title}${course.brief.code ? ` (${course.brief.code})` : ""}`, { x: 1.0, y: 3.8, w: 11.5, h: 0.5, fontFace: t.font, fontSize: 20, color: t.muted });
  title.addText(`Session ${session.index} | ${plan.name}`, { x: 1.0, y: 4.3, w: 11.5, h: 0.5, fontFace: t.font, fontSize: 16, color: t.muted });
  title.addNotes(`Session ${session.index}: ${session.title}. ${session.minutes} minutes.`);

  // Outcomes
  const oc = pres.addSlide({ masterName: "CG" });
  heading(oc, "By the end of this session you can");
  const outcomeLines = session.sessionOutcomes.length
    ? session.sessionOutcomes.map((o) => ({ id: o.id, text: o.text }))
    : session.outcomeIds.map((id) => ({ id, text: outcomeText(course, id) }));
  bullets(oc, outcomeLines.map((o) => o.text), 12.1);
  oc.addNotes(outcomeLines.map((o) => `${o.id}: ${o.text}`).join("\n"));
  footer(oc);

  // One or more slides per block that needs slides
  for (const b of sortedBlocks(session.blocks).filter((x) => x.needsSlides)) {
    const items = faceBullets(b);
    const chunks: string[][] = [];
    for (let i = 0; i < Math.max(items.length, 1); i += MAX_BULLETS) chunks.push(items.slice(i, i + MAX_BULLETS));
    chunks.forEach((chunk, i) => {
      const s = pres.addSlide({ masterName: "CG" });
      heading(s, chunks.length > 1 ? `${b.title} (${i + 1}/${chunks.length})` : b.title);
      bullets(s, chunk, 7.3);
      imageArea(s);
      const full = b.industryExample ? `${b.activity}\n\nIndustry example (${b.industryExample.sector}): ${b.industryExample.text}` : b.activity;
      s.addNotes(i === 0 ? full : `Continued: ${b.title}.`);
      footer(s);
    });
  }

  // Recap
  const rc = pres.addSlide({ masterName: "CG" });
  heading(rc, "Recap");
  const recap = sortedBlocks(session.blocks).filter((b) => b.needsSlides && b.kind !== "hook" && b.kind !== "break").map((b) => b.title);
  bullets(rc, recap.length ? recap : session.outcomeIds.map((id) => outcomeText(course, id)), 12.1);
  rc.addNotes("Ask learners to say each point in their own words before moving on.");
  footer(rc);

  const data = await pres.write({ outputType: "uint8array" });
  return data as Uint8Array;
}
