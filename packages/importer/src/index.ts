import { existsSync, readdirSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { importVehicles } from "./courses/aelzc441.js";
import { importIceEngines } from "./courses/aezc516.js";
import { importSystemsEngineering } from "./courses/aezc517.js";
import { importWeeks } from "./courses/tuv.js";
import type { ImportResult } from "./courses/common.js";
import { detectDialect } from "./parsers/courseYaml.js";

export type { ImportResult } from "./courses/common.js";
export { parseHandout } from "./parsers/handout.js";
export { parseSeYaml, parseVehiclesYaml, parseWeeksYaml, detectDialect } from "./parsers/courseYaml.js";
export { parseOutcomeRows, parseInfoRows, readModuleTemplate } from "./parsers/xlsx.js";
export { parseFramework, parseTimedTemplates, parseObjectives, parseFrontMatter } from "./parsers/framework.js";
export { blocksFromFramework, blocksFromTimed } from "./blocks.js";
export { inferBloom } from "./util.js";
export { runRules, renderReport } from "./report.js";

/** Pick the importer from what the folder contains: an .xlsx module sheet, or the dialect of course-data.yaml. */
export async function importCourseDir(dir: string, now = new Date().toISOString()): Promise<ImportResult> {
  const abs = resolve(dir);
  const ctx = { dir: abs, now };
  if (readdirSync(abs).some((f) => /\.xlsx$/i.test(f) && !f.startsWith("~$"))) return importIceEngines(ctx);
  const y = join(abs, "course-data-fixed.yaml");
  const yaml = existsSync(y) ? y : join(abs, "course-data.yaml");
  if (!existsSync(yaml)) throw new Error(`${abs}: no course-data.yaml or .xlsx found`);
  const dialect = detectDialect(readFileSync(yaml, "utf8"));
  if (dialect === "weeks") return importWeeks(ctx);
  if (dialect === "vehicles") return importVehicles(ctx);
  if (dialect === "systems-engineering") return importSystemsEngineering(ctx);
  throw new Error(`${yaml}: unrecognised course-data.yaml layout`);
}
