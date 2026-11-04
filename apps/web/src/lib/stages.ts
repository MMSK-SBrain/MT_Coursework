// The app depends only on the core `Stages` and `Exporter` interfaces; this file picks the implementations.
//   OPENROUTER_API_KEY set  -> @cg/harness OpenRouterStages (real models)
//   otherwise               -> @cg/harness MockStages (deterministic, network-free)
// Exports always come from @cg/exports (markdown, .pptx, .docx).
import type { Exporter, Stages } from "@cg/core";
import { exporter } from "@cg/exports";
import { EscoOccupationSource, FixtureLinkSource, MockStages, OpenRouterClient, OpenRouterStages, YouTubeLinkSource, loadConfig } from "@cg/harness";

let stages: Stages | undefined;

export function createStages(env: Record<string, string | undefined> = process.env): Stages {
  if (!env.OPENROUTER_API_KEY) {
    return new MockStages({ now: () => new Date(), delayMs: env.NODE_ENV === "development" ? 400 : 0 });
  }
  return new OpenRouterStages({
    client: new OpenRouterClient({ apiKey: env.OPENROUTER_API_KEY, appTitle: "Course Generator" }),
    config: loadConfig(env),
    // Roles come from ESCO occupations and their essential skills (public API, no key). No job postings, no demand figures.
    roles: new EscoOccupationSource(),
    links: env.YOUTUBE_API_KEY ? new YouTubeLinkSource({ apiKey: env.YOUTUBE_API_KEY }) : new FixtureLinkSource(),
  });
}

export function getStages(): Stages {
  return (stages ??= createStages());
}

export function getExporter(): Exporter {
  return exporter;
}

/** Shown in the top bar while generation is mocked. */
export const usingMockStages = () => getStages() instanceof MockStages;
