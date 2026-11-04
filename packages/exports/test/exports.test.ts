import { inflateRawSync } from "node:zlib";
import { describe, expect, it } from "vitest";
import { createExporter } from "../src/index.js";
import { SAMPLE_PLAN_ID as P, SAMPLE_SESSION_ID as S, sampleCourse as course } from "../src/fixture.js";

/** Minimal zip reader: file name → text, via the central directory. */
function unzip(buf: Uint8Array): Record<string, string> {
  const b = Buffer.from(buf);
  expect(b.subarray(0, 2).toString()).toBe("PK");
  let eocd = b.length - 22;
  while (eocd >= 0 && b.readUInt32LE(eocd) !== 0x06054b50) eocd--;
  const count = b.readUInt16LE(eocd + 10);
  let p = b.readUInt32LE(eocd + 16);
  const files: Record<string, string> = {};
  for (let i = 0; i < count; i++) {
    const method = b.readUInt16LE(p + 10);
    const csize = b.readUInt32LE(p + 20);
    const nlen = b.readUInt16LE(p + 28), elen = b.readUInt16LE(p + 30), clen = b.readUInt16LE(p + 32);
    const local = b.readUInt32LE(p + 42);
    const name = b.subarray(p + 46, p + 46 + nlen).toString();
    const data = b.subarray(local + 30 + b.readUInt16LE(local + 26) + b.readUInt16LE(local + 28));
    const comp = data.subarray(0, csize);
    files[name] = (method === 0 ? comp : inflateRawSync(comp)).toString("utf8");
    p += 46 + nlen + elen + clen;
  }
  return files;
}

const ex = createExporter();

describe("markdown", () => {
  const md = ex.markdown(course);

  it("writes the expected files", () => {
    expect(Object.keys(md).sort()).toEqual([
      "README.md", "outcomes.md", "plans/p1/README.md", "plans/p1/session-03.md", "plans/p1/session-04.md",
    ]);
  });

  it("README has brief, modules, selected roles and confirmed changes only", () => {
    const r = md["README.md"]!;
    expect(r).toContain("# Systems Engineering (AEZC517)");
    expect(r).toContain("M3");
    expect(r).toContain("BMS Systems Engineer");
    expect(r).not.toContain("Cybersecurity");
    expect(r).toContain("Hands-on requirements tool lab");
    expect(r).not.toContain("Soft-skills content"); // rejected
  });

  it("outcomes.md has Bloom, modules and roles", () => {
    const o = md["outcomes.md"]!;
    expect(o).toContain("| LO2 |");
    expect(o).toContain("Apply");
    expect(o).toContain("Requirements Engineer");
  });

  it("session page has timed table, examples, checks, approved links", () => {
    const s = md["plans/p1/session-03.md"]!;
    expect(s).toContain("| 0:10-0:45 | 35 | Anatomy of a good requirement |");
    expect(s).toContain("## Industry examples");
    expect(s).toContain("INCOSE Guide to Writing Requirements");
    expect(s).toContain("## Quick checks");
    expect(s).toContain("Writing good requirements in 10 minutes");
    expect(s).not.toContain("ASPICE SYS.2 explained"); // unapproved
  });

  it("outcomes.md shows hierarchy and roll-up with reasons", () => {
    const o = md["outcomes.md"]!;
    expect(o).toContain("## Outcome hierarchy");
    expect(o).toContain("**M3.MO1** Write verifiable requirements");
    expect(o).toContain("## Roll-up: Classroom, 3 h sessions");
    expect(o).toContain("| M3.MO1 | S3.SO1, S3.SO2 | Met |");
    expect(o).toContain("| M1.MO1 | none | Not met: no session outcome serves it |");
    expect(o).toContain("| LO2 | M3.MO1, M3.MO2 | Met |");
    expect(o).toContain("| LO1 | M1.MO1, M2.MO1 | Not met:");
  });

  it("session file lists SOs and block SO ids", () => {
    const s = md["plans/p1/session-03.md"]!;
    expect(s).toContain("## Session outcomes");
    expect(s).toContain("| S3.SO2 | Trace a requirement");
    expect(s).toContain("| Apply | M3.MO1, M3.MO2 |");
    expect(s).toContain("serves: S3.SO1, S3.SO2*");
    expect(s).toContain("| Exit quiz | check | retrieval | S3.SO1, S3.SO2 |");
  });

  it("excludes case study content, keeps only the count", () => {
    const all = Object.values(md).join("\n");
    expect(all).toContain("1 case study available");
    expect(all).not.toContain("ambiguous derating");
    expect(all).not.toContain("Steer learners");
    expect(all).not.toContain("55 C");
  });
});

describe("slides", () => {
  it("is a valid pptx with expected text and notes", async () => {
    const files = unzip(await ex.slides(course, P, S));
    const slides = Object.keys(files).filter((n) => /^ppt\/slides\/slide\d+\.xml$/.test(n));
    // title + outcomes + b1 + b2 (5 bullets, 2 slides) + b4 + b6 + recap
    expect(slides.length).toBe(8);
    const text = slides.map((n) => files[n]).join("\n");
    expect(text).toContain("Writing verifiable requirements");
    expect(text).toContain("Anatomy of a good requirement");
    expect(text).toContain("Image area");
    expect(text).not.toContain("Rewrite in pairs"); // needsSlides false
    const notes = Object.keys(files).filter((n) => n.startsWith("ppt/notesSlides/") && n.endsWith(".xml")).map((n) => files[n]).join("\n");
    expect(notes).toContain("Introduce the five checks");
    // outcomes slide shows session outcomes, not LOs
    expect(text).toContain("Rewrite a weak requirement");
    expect(text).not.toContain("Write verifiable system requirements");
    expect(notes).toContain("S3.SO1: Rewrite a weak requirement");
  });

  it("keeps long industry examples whole in notes and short on the slide", async () => {
    const files = unzip(await ex.slides(course, P, S));
    const slideText = Object.keys(files).filter((n) => /^ppt\/slides\/slide\d+\.xml$/.test(n)).map((n) => files[n]).join("\n");
    const notes = Object.keys(files).filter((n) => n.startsWith("ppt/notesSlides/") && n.endsWith(".xml")).map((n) => files[n]).join("\n");
    expect(slideText).toContain("In industry:");
    expect(slideText).not.toContain("…");
    expect(slideText).not.toContain("warranty dispute");
    expect(notes).toContain("later used the same trace to settle a warranty dispute");
  });

  it("falls back to LOs when a session has no session outcomes", async () => {
    const files = unzip(await ex.slides(course, P, "s4"));
    expect(Object.values(files).join("\n")).toContain("Model the functional and physical architecture");
  });

  it("supports the dark theme", async () => {
    const files = unzip(await createExporter({ theme: "dark" }).slides(course, P, S));
    expect(Object.values(files).join("\n")).toContain("0D1117");
  });
});

describe("instructor guide", () => {
  it("is a valid docx with the expected sections", async () => {
    const files = unzip(await ex.instructorGuide(course, P, S));
    const doc = files["word/document.xml"]!;
    for (const t of ["Session overview", "Outcomes", "Run sheet", "Talking points", "Quick checks", "Answer:", "Case studies", "Composite case", "Further learning", "Anatomy of a good requirement"]) {
      expect(doc).toContain(t);
    }
    expect(doc).toContain("Session outcomes");
    expect(doc).toContain("S3.SO2");
    expect(doc).toContain(">SOs<");
    expect(doc).toContain("The ambiguous derating requirement");
    expect(doc).not.toContain("ASPICE SYS.2 explained");
  });

  it("throws on an unknown session", async () => {
    await expect(ex.instructorGuide(course, P, "nope")).rejects.toThrow(/Session not found/);
  });
});
