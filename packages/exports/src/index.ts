import type { Exporter } from "@cg/core";
import { instructorGuideExport } from "./guide.js";
import { markdownExport } from "./markdown.js";
import { slidesExport, type SlideOptions } from "./slides.js";

export { THEMES, type SlideOptions, type SlideTheme, type ThemeName } from "./slides.js";
export { sampleCourse } from "./fixture.js";

/** Create an Exporter. `slideOptions` sets the slide theme ("default" or "dark"). */
export function createExporter(slideOptions: SlideOptions = {}): Exporter {
  return {
    markdown: markdownExport,
    slides: (course, planId, sessionId) => slidesExport(course, planId, sessionId, slideOptions),
    instructorGuide: instructorGuideExport,
  };
}

export const exporter: Exporter = createExporter();
