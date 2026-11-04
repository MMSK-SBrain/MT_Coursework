import { mkdtemp, readdir } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { FREE_TIER, VIDEO_BY_PATH } from "@cg/core";
import type { VideoKind } from "@cg/core";
import { aezc517, PLAN_FOR_KIND } from "./fixtures.js";
import { buildProject, createVideoBuilder, markersIn, outlineProblems, renderProject, templateOutline, VideoLimitError, VideoPlanError } from "./index.js";
import type { ScriptOutline } from "./index.js";

const KINDS = ["explainroo", "whiteboard", "demo", "screen", "slides"] as const;

/** explainroo shows the shown part of {shown|spoken}; markers and braces are not on screen. */
const plain = (md: string) => md.replace(/\[#[^\]]*\]/g, "").replace(/\{([^|}]*)\|[^}]*\}/g, "$1").replace(/\s+/g, " ");

/** A recording scene object: any method returns a box-like object, and every `at`/`out` marker is noted. */
function runScenes(scenesJs: string): Record<string, { markers: Set<string>; calls: string[] }> {
  const mod = new Function(scenesJs.replace("export default", "return"))() as Record<string, (s: unknown) => void>;
  const out: Record<string, { markers: Set<string>; calls: string[] }> = {};
  for (const [id, fn] of Object.entries(mod)) {
    const rec = { markers: new Set<string>(), calls: [] as string[] };
    const note = (v: unknown) => { if (typeof v === "string" && v.startsWith("#")) rec.markers.add(v.slice(1)); };
    const box = { x: 1, y: 1, w: 1, h: 1, left: 0, right: 1, top: 0, bottom: 1 };
    const safe = { x: 100, y: 100, w: 1700, h: 880, left: 100, top: 100, right: 1800, bottom: 980 };
    const s: any = new Proxy({ W: 1920, H: 1080, cx: 960, cy: 540, portrait: false, safe }, {
      get(t, name: string) {
        if (name in t) return (t as any)[name];
        return (...args: any[]) => {
          rec.calls.push(name);
          for (const a of args) {
            if (a && typeof a === "object") { note(a.at); note(a.out); if (Array.isArray(a)) a.forEach((i) => i && note(i.at)); }
            else note(a);
          }
          if (name === "mark") { rec.markers.add(String(args[0])); return 1; }
          if (name === "time") return typeof args[0] === "number" ? args[0] : 1;
          if (name === "row" || name === "col") return Array.from({ length: args[0] }, (_, i) => 100 * i);
          return box;
        };
      },
    });
    fn(s);
    out[id] = rec;
  }
  return out;
}

describe("plan() per video kind", () => {
  for (const kind of KINDS) {
    describe(kind, () => {
      const builder = createVideoBuilder();
      it("produces parseable scenes.js whose markers all exist in the script", async () => {
        const project = await builder.planKind(aezc517, PLAN_FOR_KIND[kind], "s3", kind);
        expect(() => new Function(project.scenesJs.replace("export default", "return"))).not.toThrow();
        const scenes = runScenes(project.scenesJs);
        const sections = project.scriptMd.split(/^## /m).slice(1);
        expect(Object.keys(scenes)).toHaveLength(sections.length);
        for (const sec of sections) {
          const id = sec.match(/^([a-z0-9-]+)/)![1]!;
          const have = new Set(markersIn(sec));
          const used = scenes[id]!.markers;
          for (const m of used) expect(have, `scene ${id} uses #${m}`).toContain(m);
          expect(scenes[id]!.calls.length).toBeGreaterThan(0);
        }
      });

      it("narration covers the session outcomes and the title", async () => {
        const project = await builder.planKind(aezc517, PLAN_FOR_KIND[kind], "s3", kind);
        const text = plain(project.scriptMd).toLowerCase();
        for (const o of aezc517.outcomes) expect(text).toContain(o.text.replace(/\.$/, "").toLowerCase().replace(/^./, (c) => c));
        expect(text).toContain("what a good requirement looks like");
      });

      it("ships video.json and stays inside the free-tier length", async () => {
        const project = await builder.planKind(aezc517, PLAN_FOR_KIND[kind], "s3", kind);
        const cfg = JSON.parse(new TextDecoder().decode(project.assets["video.json"]));
        expect(cfg.title).toBeTruthy();
        expect(project.estimatedSec).toBeGreaterThan(5);
        expect(project.estimatedSec).toBeLessThanOrEqual(FREE_TIER.videoSecondsPerMonth);
        if (kind === "whiteboard") expect(project.assets["look.json"]).toBeDefined();
      });
    });
  }

  it("whiteboard uses drawn strokes and stick figures", async () => {
    const p = await createVideoBuilder().planKind(aezc517, "p-micro", "s3", "whiteboard");
    expect(p.scenesJs).toContain("person(");
    expect(runScenes(p.scenesJs)["hook"]!.calls).toContain("line");
  });

  it("demo without supplied clips uses placeholders; supplied clips are used and copied", async () => {
    const none = await createVideoBuilder().planKind(aezc517, "p-blended", "s3", "demo");
    expect(none.scenesJs).toContain('"src":null');
    const clip = new Uint8Array([1, 2, 3]);
    const withClip = await createVideoBuilder({ media: { "assets/bench.mp4": clip } }).planKind(aezc517, "p-blended", "s3", "demo");
    expect(withClip.scenesJs).toContain("assets/bench.mp4");
    expect(withClip.assets["assets/bench.mp4"]).toBe(clip);
  });
});

describe("rules", () => {
  const builder = createVideoBuilder();

  it("plan() uses the session's own kind", async () => {
    const p = await builder.plan(aezc517, "p-youtube", "s3");
    expect(p.scenesJs).toContain("(explainroo)");
  });

  it("refuses every kind a path does not allow", async () => {
    for (const plan of aezc517.plans) {
      for (const kind of KINDS) {
        const allowed = VIDEO_BY_PATH[plan.path].includes(kind as VideoKind);
        const result = builder.planKind(aezc517, plan.id, "s3", kind);
        if (allowed) await expect(result).resolves.toBeTruthy();
        else await expect(result).rejects.toThrow(/not allowed/);
      }
    }
  });

  it("refuses sessions without video and unknown ids", async () => {
    await expect(builder.plan(aezc517, "p-classroom", "s3")).rejects.toThrow(VideoPlanError);
    await expect(builder.plan(aezc517, "nope", "s3")).rejects.toThrow(/not found/);
    await expect(builder.plan(aezc517, "p-youtube", "nope")).rejects.toThrow(/not found/);
  });

  it("trims scenes to the target and enforces the max duration", async () => {
    const full = await createVideoBuilder({ targetSec: 300 }).plan(aezc517, "p-youtube", "s3");
    const short = await createVideoBuilder({ targetSec: 22 }).plan(aezc517, "p-youtube", "s3");
    expect(short.estimatedSec).toBeLessThan(full.estimatedSec);
    expect(short.estimatedSec).toBeLessThanOrEqual(22);
    expect(short.scriptMd.split(/^## /m).length).toBeLessThan(full.scriptMd.split(/^## /m).length);
    // essential scenes survive
    expect(short.scriptMd).toContain("## hook");
    // a limit below the minimum script cannot be met
    await expect(createVideoBuilder({ maxSec: 5 }).plan(aezc517, "p-youtube", "s3")).rejects.toThrow(VideoLimitError);
  });

  it("buildProject enforces maxSec and the path rule on any outline (LLM seam)", () => {
    const outline: ScriptOutline = {
      title: "T", courseLabel: "C",
      scenes: [{ id: "hook", priority: 0, visual: { type: "hook", text: "Why?" }, narration: "[#q] " + "word ".repeat(200) }],
    };
    expect(() => buildProject(outline, { kind: "explainroo", maxSec: 60 })).toThrow(VideoLimitError);
    expect(() => buildProject(outline, { kind: "explainroo", maxSec: 600 })).not.toThrow();
    expect(() => buildProject(outline, { kind: "explainroo", path: "classroom" })).toThrow(/not allowed/);
    const bad: ScriptOutline = { ...outline, scenes: [{ ...outline.scenes[0]!, narration: "no marker" }] };
    expect(outlineProblems(bad)[0]).toMatch(/needs a \[#q\]/);
    expect(() => buildProject(bad, { kind: "explainroo" })).toThrow(VideoPlanError);
  });

  it("templateOutline output is a valid outline", () => {
    for (const kind of KINDS) expect(outlineProblems(templateOutline(aezc517, PLAN_FOR_KIND[kind], "s3", { kind, targetSec: 200 }))).toEqual([]);
  });

  it("render() refuses over-length projects before touching the disk", async () => {
    const project = await createVideoBuilder().plan(aezc517, "p-youtube", "s3");
    const workDir = await mkdtemp(path.join(os.tmpdir(), "cg-video-test-"));
    await expect(createVideoBuilder().render({ ...project, estimatedSec: 301 }, { workDir, maxSec: 300 })).rejects.toThrow(VideoLimitError);
    expect(await readdir(workDir)).toEqual([]);
    await expect(renderProject({ ...project, assets: { "../evil.txt": new Uint8Array() } }, { workDir, maxSec: 300 })).rejects.toThrow();
  });
});
