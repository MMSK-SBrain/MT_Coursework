// pnpm --filter @cg/importer run import <course-dir> [--now <iso>]   (or --all to import every folder under courses/)
import { existsSync, readdirSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { importCourseDir, renderReport, runRules } from "./index.js";

const argv = process.argv.slice(2);
const nowIx = argv.indexOf("--now");
const now = nowIx >= 0 ? argv[nowIx + 1] : undefined;
const positional = argv.filter((a, i) => !a.startsWith("--") && argv[i - 1] !== "--now");

async function one(dir: string) {
  const abs = resolve(process.env.INIT_CWD ?? process.cwd(), dir);
  const r = await importCourseDir(abs, now);
  const w = runRules(r.course);
  writeFileSync(join(abs, "course.json"), JSON.stringify(r.course, null, 2) + "\n");
  writeFileSync(join(abs, "IMPORT-REPORT.md"), renderReport(r, w));
  console.log(`${r.course.slug}: ${r.imported.join(", ")}; warnings: ${w.verb.length} verbs, ${w.hours.length} hour-block sessions, ${w.uncovered.length} uncovered outcomes`);
}

async function main() {
  let dirs = positional;
  if (argv.includes("--all")) {
    const root = resolve(process.env.INIT_CWD ?? process.cwd(), positional[0] ?? "courses");
    dirs = readdirSync(root).map((d) => join(root, d)).filter((d) => existsSync(join(d, "course-data.yaml")) || (existsSync(d) && readdirSync(d).some((f) => /\.xlsx$/i.test(f))));
  }
  if (!dirs.length) { console.error("usage: import <course-dir> [--now <iso>] | --all [courses-root]"); process.exit(2); }
  for (const d of dirs) await one(d);
}

main().catch((e) => { console.error(e instanceof Error ? e.message : e); process.exit(1); });
