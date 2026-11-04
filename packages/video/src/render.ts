import { execFile } from "node:child_process";
import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import type { VideoProject } from "@cg/core";
import { VideoLimitError } from "./compile.js";

export const explainrooDir = () => process.env.EXPLAINROO_DIR ?? "/Volumes/Dev/explainroo";

export class ExplainrooError extends Error {}

/** Run one explainroo CLI command with --json and parse its stdout. Failing commands still try to parse the JSON error. */
export function runExplainroo(args: string[], opts: { cwd?: string; timeoutMs?: number } = {}): Promise<any> {
  const bin = path.join(explainrooDir(), "bin", "explainroo.js");
  return new Promise((resolve, reject) => {
    execFile(process.execPath, [bin, ...args, "--json"], { cwd: opts.cwd ?? explainrooDir(), timeout: opts.timeoutMs ?? 15 * 60_000, maxBuffer: 64 * 1024 * 1024 }, (err, stdout, stderr) => {
      let json: any;
      try { json = JSON.parse(stdout); } catch { /* not json */ }
      if (err && !json) return reject(new ExplainrooError(`explainroo ${args[0]} failed: ${(stderr || err.message).slice(-800)}`));
      if (json?.error) return reject(new ExplainrooError(`explainroo ${args[0]}: ${json.error}`));
      if (err && args[0] !== "check") return reject(new ExplainrooError(`explainroo ${args[0]} failed: ${(stderr || err.message).slice(-800)}`));
      resolve(json);
    });
  });
}

/** Write a VideoProject into <dir> as an explainroo project. Asset paths must stay inside the folder. */
export async function writeProject(project: VideoProject, dir: string): Promise<void> {
  await mkdir(dir, { recursive: true });
  await writeFile(path.join(dir, "script.md"), project.scriptMd);
  await writeFile(path.join(dir, "scenes.js"), project.scenesJs);
  const files: Record<string, Uint8Array> = { ...project.assets };
  if (!files["video.json"]) files["video.json"] = new TextEncoder().encode(JSON.stringify({ theme: "clean", size: "youtube", watermark: false }, null, 2));
  for (const [rel, bytes] of Object.entries(files)) {
    const target = path.resolve(dir, rel);
    if (path.isAbsolute(rel) || (target !== path.resolve(dir) && !target.startsWith(path.resolve(dir) + path.sep))) throw new Error(`asset path "${rel}" leaves the project folder`);
    await mkdir(path.dirname(target), { recursive: true });
    await writeFile(target, bytes);
  }
}

/**
 * Render a project with explainroo. Steps: length check on the estimate, write files, voice (gives the real length,
 * checked again), check (layout errors stop the render), render. Nothing is spawned when the estimate is over maxSec.
 */
export async function renderProject(project: VideoProject, opts: { workDir: string; maxSec: number; draft?: boolean; log?: (m: string) => void }): Promise<{ mp4Path: string; durationSec: number }> {
  if (project.estimatedSec > opts.maxSec) throw new VideoLimitError(`estimated length ${project.estimatedSec.toFixed(0)} s is over the ${opts.maxSec} s limit`);
  const dir = path.resolve(opts.workDir, "project");
  const log = opts.log ?? (() => {});
  await writeProject(project, dir);
  log("voice");
  const v = await runExplainroo(["voice", dir]);
  if (typeof v.duration === "number" && v.duration > opts.maxSec) throw new VideoLimitError(`narration is ${v.duration.toFixed(0)} s, over the ${opts.maxSec} s limit`);
  log("check");
  const c = await runExplainroo(["check", dir]);
  const errors = (c.issues ?? []).filter((i: { level: string }) => i.level === "error");
  if (errors.length) throw new ExplainrooError(`explainroo check found ${errors.length} error(s):\n` + errors.map((e: { scene?: string; message: string }) => `- ${e.scene ?? ""}: ${e.message}`).join("\n"));
  log("render");
  const r = await runExplainroo(["render", dir, ...(opts.draft ? ["--draft"] : [])]);
  return { mp4Path: r.out, durationSec: r.duration };
}
