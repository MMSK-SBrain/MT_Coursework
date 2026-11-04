import { mkdirSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { createExporter } from "../src/index.js";
import { SAMPLE_PLAN_ID, SAMPLE_SESSION_ID, sampleCourse } from "../src/fixture.js";

const out = join(dirname(fileURLToPath(import.meta.url)), "..", "out");
const write = (rel: string, data: string | Uint8Array) => {
  const path = join(out, rel);
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, data);
  console.log("wrote", path);
};

const ex = createExporter();
for (const [path, content] of Object.entries(ex.markdown(sampleCourse))) write(join("markdown", path), content);
write("session-03-slides.pptx", await ex.slides(sampleCourse, SAMPLE_PLAN_ID, SAMPLE_SESSION_ID));
write("session-03-slides-dark.pptx", await createExporter({ theme: "dark" }).slides(sampleCourse, SAMPLE_PLAN_ID, SAMPLE_SESSION_ID));
write("session-03-instructor-guide.docx", await ex.instructorGuide(sampleCourse, SAMPLE_PLAN_ID, SAMPLE_SESSION_ID));
