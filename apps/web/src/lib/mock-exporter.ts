// Local stand-in for @cg/exports until it merges: a minimal markdown export (free tier).
// The paid .pptx and .docx exports are not available until @cg/exports is plugged in (see ./stages.ts).
import { uncoveredOutcomes, type Course, type Exporter } from "@cg/core";

const slug = (s: string) => s.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 60) || "item";
const list = (xs: string[]) => xs.map((x) => `- ${x}`).join("\n");
const mmss = (m: number) => String(m).padStart(2, "0");

export class NotAvailableError extends Error {}

export const mockExporter: Exporter = {
  markdown(course: Course) {
    const b = course.brief;
    const files: Record<string, string> = {};
    const roleTitle = (id: string) => course.roles.find((r) => r.id === id)?.title ?? id;

    files["README.md"] = [
      `# ${b.title}`, "",
      b.code ? `Code: ${b.code}  ` : "", `Audience: ${b.audience}  `, `Level: ${b.level}  `, `Contact hours: ${b.contactHours}  `,
      `Industry: ${b.industry}  `, `Job markets: ${b.markets.join(", ")}`, "",
      b.textbooks.length ? `## Textbooks\n\n${list(b.textbooks)}\n` : "",
      `Course structure v${course.structureVersion}${course.structureConfirmedAt ? `, confirmed ${course.structureConfirmedAt.slice(0, 10)}` : " (not confirmed)"}.  `,
      `Outcomes ${course.outcomesFrozenAt ? `frozen ${course.outcomesFrozenAt.slice(0, 10)}` : "not frozen"}.`, "",
      "## Files", "", list(["modules.md", "job-roles.md", "course-job-fit.md", "outcomes.md", ...course.plans.map((p) => `plans/${slug(p.name)}/README.md`)]),
    ].filter((l) => l !== "").join("\n") + "\n";

    files["modules.md"] = `# Modules\n\n| # | Module | Hours | Found in |\n|---|---|---|---|\n${course.modules
      .map((m) => `| ${m.id} | ${m.title}${m.topics.length ? `<br>${m.topics.join("; ")}` : ""} | ${m.hours} | ${m.foundIn}${m.note ? ` (${m.note})` : ""} |`)
      .join("\n")}\n`;

    const sel = course.roles.filter((r) => r.selected);
    files["job-roles.md"] = `# Job roles\n\n${sel.length ? sel.map((r) => `## ${r.title}\n\n${r.postings} postings · ${r.experience ?? ""} · module match ${r.moduleMatch}%\n\nSkills: ${r.skills.join(", ") || "-"}\n`).join("\n") : "No roles selected.\n"}`;

    files["course-job-fit.md"] = `# Course–job fit\n\n${course.fit
      .map((f) => `- **${f.kind}** ${f.text} → ${f.targetModuleId} (${f.hoursDelta > 0 ? "+" : ""}${f.hoursDelta} h): ${f.decision}. ${f.reason}${f.academicConflict ? ` _Academic requirement: ${f.academicConflict}_` : ""}`)
      .join("\n") || "No changes proposed."}\n`;

    files["outcomes.md"] = [
      "# Course objectives", "", ...course.objectives.map((o) => `- **${o.id}** ${o.text}`), "",
      "# Learning outcomes", "",
      ...course.outcomes.map((o) => `- **${o.id}** (${o.bloom}; ${o.moduleIds.join(", ")}${o.roleIds.length ? `; ${o.roleIds.map(roleTitle).join(", ")}` : ""}) ${o.text}`),
      "",
    ].join("\n");

    for (const p of course.plans) {
      const dir = `plans/${slug(p.name)}`;
      const unc = uncoveredOutcomes(course, p);
      files[`${dir}/README.md`] = [
        `# ${p.name}`, "", `Path: ${p.path} · default style: ${p.defaultStyle}${p.audienceVariant ? ` · audience: ${p.audienceVariant}` : ""}`, "",
        "| # | Session | Outcomes | Style | Minutes | Video |", "|---|---|---|---|---|---|",
        ...p.sessions.map((s) => `| ${s.index} | ${s.title}${s.stale ? " (out of date)" : ""} | ${s.outcomeIds.join(", ")} | ${s.style} | ${s.minutes} | ${s.video} |`),
        "", unc.length ? `Not covered: ${unc.join(", ")}` : "Every outcome is covered.", "",
      ].join("\n");
      for (const s of p.sessions) {
        const blocks = [...s.blocks].sort((a, b) => a.hour - b.hour || a.startMin - b.startMin);
        files[`${dir}/${String(s.index).padStart(2, "0")}-${slug(s.title)}.md`] = [
          `# Session ${s.index}: ${s.title}`, "", `Outcomes: ${s.outcomeIds.join(", ")} · style: ${s.style} · ${s.minutes} min · video: ${s.video}`, "",
          s.stale ? "> This session is out of date: an outcome or the course structure changed after it was built.\n" : "",
          "## Hour-wise plan", "",
          blocks.length ? blocks.map((x) => `### H${x.hour} ${mmss(x.startMin)}–${mmss(x.startMin + x.minutes)} · ${x.kind} · ${x.title}\n\n${x.activity}${x.industryExample ? `\n\n_Industry example:_ ${x.industryExample.text}` : ""}${x.check.length ? `\n\nQuick check:\n${list(x.check)}` : ""}\n`).join("\n") : "Not drafted yet.\n",
          "## Further learning", "",
          s.links.filter((l) => l.approved).map((l) => `- [${l.title}](${l.url}) — ${l.why}`).join("\n") || "No approved links yet.", "",
          ...s.caseStudies.map((c) => `## Case study (${c.label === "real" ? "real, sourced" : "composite"}): ${c.title}\n\n${c.background}\n\n${c.data}\n\n${list(c.questions)}\n\n_Teaching note:_ ${c.teachingNote}\n${c.sources.length ? `\nSources:\n${list(c.sources.map((x) => `[${x.title}](${x.url})`))}\n` : ""}`),
        ].join("\n");
      }
    }
    return files;
  },
  async slides() {
    throw new NotAvailableError("Slide export (.pptx) is not connected yet: it arrives with @cg/exports.");
  },
  async instructorGuide() {
    throw new NotAvailableError("Instructor guide export (.docx) is not connected yet: it arrives with @cg/exports.");
  },
};
