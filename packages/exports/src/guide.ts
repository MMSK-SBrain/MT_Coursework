import {
  AlignmentType, BorderStyle, Document, ExternalHyperlink, HeadingLevel, Packer, Paragraph, Table, TableCell, TableRow, TextRun, WidthType,
} from "docx";
import { isHttpUrl, type Course } from "@cg/core";
import { approvedLinks, blockRange, findSession, outcomeText, sortedBlocks } from "./util.js";

const p = (text: string, opts: { bold?: boolean; italics?: boolean } = {}) =>
  new Paragraph({ children: [new TextRun({ text, ...opts })], spacing: { after: 120 } });
const h1 = (text: string) => new Paragraph({ text, heading: HeadingLevel.HEADING_1, spacing: { before: 280, after: 120 } });
const h2 = (text: string) => new Paragraph({ text, heading: HeadingLevel.HEADING_2, spacing: { before: 200, after: 80 } });
const bullet = (text: string) => new Paragraph({ text, bullet: { level: 0 } });
// Only http(s) links become clickable; anything else is shown as plain text.
const link = (title: string, url: string) =>
  isHttpUrl(url)
    ? new Paragraph({ children: [new ExternalHyperlink({ link: url, children: [new TextRun({ text: title, style: "Hyperlink", color: "2563EB", underline: {} })] })] })
    : new Paragraph({ children: [new TextRun({ text: title })] });

const cell = (text: string, width: number, header = false) =>
  new TableCell({
    width: { size: width, type: WidthType.PERCENTAGE },
    shading: header ? { fill: "E5E7EB" } : undefined,
    children: [new Paragraph({ children: [new TextRun({ text, bold: header, size: 20 })] })],
  });
const table = (head: string[], widths: number[], rows: string[][]) =>
  new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      new TableRow({ tableHeader: true, children: head.map((t, i) => cell(t, widths[i]!, true)) }),
      ...rows.map((r) => new TableRow({ children: r.map((t, i) => cell(t, widths[i]!)) })),
    ],
  });

const answerBox = () =>
  new Paragraph({
    children: [new TextRun({ text: "Answer:" })],
    spacing: { before: 60, after: 360 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "9CA3AF", space: 12 } },
  });

export async function instructorGuideExport(course: Course, planId: string, sessionId: string): Promise<Uint8Array> {
  const { plan, session } = findSession(course, planId, sessionId);
  const blocks = sortedBlocks(session.blocks);
  const body: (Paragraph | Table)[] = [];

  body.push(new Paragraph({ text: `Instructor guide: ${session.title}`, heading: HeadingLevel.TITLE, alignment: AlignmentType.LEFT }));
  body.push(p(`${course.brief.title}${course.brief.code ? ` (${course.brief.code})` : ""} | ${plan.name} | Session ${session.index}`, { italics: true }));

  body.push(h1("Session overview"));
  body.push(p(`Duration: ${session.minutes} minutes. Teaching style: ${session.style}. Audience: ${course.brief.audience}.`));
  body.push(p(`Learning path: ${plan.path}${plan.audienceVariant ? `, variant: ${plan.audienceVariant}` : ""}.`));

  body.push(h1("Outcomes"));
  for (const id of session.outcomeIds) {
    const o = course.outcomes.find((x) => x.id === id);
    body.push(bullet(`${id}${o ? ` (${o.bloom})` : ""}: ${outcomeText(course, id)}`));
  }

  body.push(h1("Run sheet"));
  body.push(table(["Time", "Min", "Block", "Type", "Style"], [14, 8, 42, 16, 20], blocks.map((b) => [blockRange(b), String(b.minutes), b.title, b.kind, b.style])));

  body.push(h1("Talking points"));
  for (const b of blocks) {
    body.push(h2(`${blockRange(b)}  ${b.title}`));
    body.push(p(b.activity));
    if (b.industryExample) {
      const e = b.industryExample;
      body.push(p(`Industry example (${e.sector}): ${e.text}`, { italics: true }));
      for (const s of e.sources) body.push(link(`Source: ${s.title}`, s.url));
    }
  }

  const checks = blocks.filter((b) => b.check.length);
  body.push(h1("Quick checks"));
  if (checks.length) {
    for (const b of checks) {
      body.push(h2(b.title));
      b.check.forEach((q, i) => { body.push(p(`${i + 1}. ${q}`)); body.push(answerBox()); });
    }
  } else body.push(p("No quick checks drafted."));

  body.push(h1("Case studies"));
  if (session.caseStudies.length) {
    for (const c of session.caseStudies) {
      body.push(h2(`${c.title} [${c.label === "real" ? "Real case" : "Composite case (invented for teaching)"}]`));
      body.push(p(c.background));
      if (c.data) body.push(p(c.data));
      body.push(p("Questions", { bold: true }));
      c.questions.forEach((q, i) => body.push(p(`${i + 1}. ${q}`)));
      body.push(p("Teaching note", { bold: true }));
      body.push(p(c.teachingNote));
      if (c.sources.length) {
        body.push(p("Sources", { bold: true }));
        for (const s of c.sources) body.push(link(s.title, s.url));
      }
    }
  } else body.push(p("No case studies for this session."));

  const links = approvedLinks(session);
  body.push(h1("Further learning"));
  if (links.length) {
    for (const l of links) {
      body.push(link(l.title, l.url));
      body.push(p(`${l.kind}${l.channelOrSite ? `, ${l.channelOrSite}` : ""}. ${l.why}`));
    }
  } else body.push(p("No approved links."));

  const doc = new Document({
    creator: "Course Generator",
    title: `Instructor guide: ${session.title}`,
    sections: [{ children: body }],
  });
  return new Uint8Array(await Packer.toBuffer(doc));
}
