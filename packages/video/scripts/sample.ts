// pnpm --filter @cg/video sample
// Builds the AEZC517 "What a good requirement looks like" sample for every video kind into out/<kind>/,
// then renders the explainroo one (about 20 s) when explainroo's doctor says it is ready.
// Env: SAMPLE_KINDS=explainroo,whiteboard  SAMPLE_SEC=30  SAMPLE_RENDER=0|1  EXPLAINROO_DIR=...
import path from "node:path";
import { fileURLToPath } from "node:url";
import { aezc517, PLAN_FOR_KIND } from "../src/fixtures.js";
import { createVideoBuilder, runExplainroo, writeProject } from "../src/index.js";

const out = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "out");
const kinds = (process.env.SAMPLE_KINDS ?? "explainroo,whiteboard,demo,screen,slides").split(",") as (keyof typeof PLAN_FOR_KIND)[];
const targetSec = Number(process.env.SAMPLE_SEC ?? 30);
const builder = createVideoBuilder({ targetSec });

for (const kind of kinds) {
  const project = await builder.planKind(aezc517, PLAN_FOR_KIND[kind], "s3", kind);
  await writeProject(project, path.join(out, kind, "project"));
  console.log(`${kind.padEnd(11)} ${project.estimatedSec.toFixed(1)} s estimated  -> out/${kind}/project`);
}

if (process.env.SAMPLE_RENDER === "0") process.exit(0);
const renderKinds = process.env.SAMPLE_RENDER === "all" ? kinds : kinds.filter((k) => k === "explainroo");
let doctor: { ok: boolean; checks: { name: string; ok: boolean; detail: string }[] };
try {
  doctor = await runExplainroo(["doctor"]);
} catch (e) {
  console.log(`explainroo doctor could not run, skipping render: ${(e as Error).message}`);
  process.exit(0);
}
const missing = doctor.checks.filter((c) => !c.ok && ["node", "ffmpeg", "chrome", "voice model", "speech check model"].includes(c.name));
if (missing.length) {
  console.log("explainroo is not ready, skipping render. Missing: " + missing.map((m) => `${m.name} (${m.detail})`).join("; "));
  process.exit(0);
}
for (const kind of renderKinds) {
  const project = await builder.planKind(aezc517, PLAN_FOR_KIND[kind], "s3", kind);
  const t0 = Date.now();
  const r = await builder.render(project, { workDir: path.join(out, kind), maxSec: 300 });
  console.log(`${kind}: rendered ${r.mp4Path} (${r.durationSec.toFixed(1)} s) in ${((Date.now() - t0) / 1000).toFixed(0)} s`);
}
