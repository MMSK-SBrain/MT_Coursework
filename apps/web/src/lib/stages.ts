// The app depends only on the core `Stages` and `Exporter` interfaces. This file is the single place where the
// real implementations get plugged in.
import type { Exporter, Stages } from "@cg/core";
import { mockStages } from "./mock-stages";
import { mockExporter } from "./mock-exporter";

// ============================================================================================
// PLUG-IN POINT for @cg/harness and @cg/exports.
// When they merge:
//   1. add "@cg/harness": "workspace:*" and "@cg/exports": "workspace:*" to apps/web/package.json
//      and both names to `transpilePackages` in apps/web/next.config.mjs;
//   2. replace the two return statements below, e.g.
//        import { createStages } from "@cg/harness";   return (stages ??= createStages(process.env));
//        import { exporter } from "@cg/exports";        return exporter;
//   CG_STAGES=mock keeps the mock (tests, offline dev).
// ============================================================================================
let stages: Stages | undefined;
export function getStages(): Stages {
  return (stages ??= mockStages);
}

export function getExporter(): Exporter {
  return mockExporter;
}
