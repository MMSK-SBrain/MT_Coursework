import type { Course, HourBlock, Session } from "@cg/core";
import { approvedLinks, blockRange, outcomeText, pad2, sortedBlocks } from "./util.js";

const cell = (s: string) => s.replace(/\|/g, "\\|").replace(/\s*\n\s*/g, " ");
const cap = (s: string) => s.charAt(0).toUpperCase() + s.slice(1);

function table(head: string[], rows: string[][]): string {
  return [
    `| ${head.join(" | ")} |`,
    `| ${head.map(() => "---").join(" | ")} |`,
    ...rows.map((r) => `| ${r.map(cell).join(" | ")} |`),
  ].join("\n");
}

function readme(course: Course): string {
  const b = course.brief;
  const out: string[] = [];
  out.push(`# ${b.title}${b.code ? ` (${b.code})` : ""}`, "");
  out.push("## Course brief", "");
  out.push(
    `- **Audience:** ${b.audience}`,
    `- **Level:** ${b.level}`,
    `- **Contact hours:** ${b.contactHours}`,
    `- **Industry:** ${b.industry}`,
    `- **Markets:** ${b.markets.join(", ")}`,
  );
  if (b.textbooks.length) out.push(`- **Textbooks:** ${b.textbooks.join("; ")}`);
  if (b.notes) out.push(`- **Notes:** ${b.notes}`);
  out.push("", "## Modules", "");
  out.push(table(["Module", "Title", "Hours", "Topics"], course.modules.map((m) => [m.id, m.title + (m.note ? ` (${m.note})` : ""), String(m.hours), m.topics.join("; ")])));
  const roles = course.roles.filter((r) => r.selected);
  out.push("", "## Target job roles", "");
  if (roles.length) {
    out.push(table(["Role", "Postings read", "Experience", "Module match", "Key skills"], roles.map((r) => [r.title, String(r.postings), r.experience ?? "", `${r.moduleMatch}%`, r.skills.join(", ")])));
  } else out.push("No roles selected.");
  const fit = course.fit.filter((f) => f.decision === "accepted" || f.decision === "changed");
  out.push("", "## Confirmed changes from job-fit review", "");
  if (fit.length) {
    for (const f of fit) {
      const h = f.hoursDelta ? ` (${f.hoursDelta > 0 ? "+" : ""}${f.hoursDelta} h)` : "";
      out.push(`- **${cap(f.kind)}** in ${f.targetModuleId}: ${f.text}${h}. ${f.reason}`);
    }
  } else out.push("No changes confirmed.");
  out.push("", "## Contents", "", "- [Objectives and outcomes](outcomes.md)");
  for (const p of course.plans) out.push(`- [${p.name}](plans/${p.id}/README.md)`);
  return out.join("\n") + "\n";
}

function outcomes(course: Course): string {
  const out: string[] = ["# Objectives and outcomes", ""];
  out.push("## Course objectives", "");
  if (course.objectives.length) for (const o of course.objectives) out.push(`- **${o.id}** ${o.text}`);
  else out.push("None defined.");
  out.push("", "## Learning outcomes", "");
  const roleTitle = (id: string) => course.roles.find((r) => r.id === id)?.title ?? id;
  out.push(table(
    ["Id", "Outcome", "Bloom", "Modules", "Objectives", "Roles"],
    course.outcomes.map((o) => [o.id, o.text, cap(o.bloom), o.moduleIds.join(", "), o.objectiveIds.join(", "), o.roleIds.map(roleTitle).join(", ")]),
  ));
  if (course.outcomesFrozenAt) out.push("", `Outcomes frozen on ${course.outcomesFrozenAt.slice(0, 10)}.`);
  return out.join("\n") + "\n";
}

function planReadme(course: Course, planId: string): string {
  const p = course.plans.find((x) => x.id === planId)!;
  const out: string[] = [`# ${p.name}`, ""];
  out.push(`- **Path:** ${p.path}`, `- **Default style:** ${p.defaultStyle}`);
  if (p.audienceVariant) out.push(`- **Audience variant:** ${p.audienceVariant}`);
  out.push("", "## Sessions", "");
  out.push(table(["#", "Session", "Style", "Minutes", "Outcomes"], p.sessions.map((s) => [
    String(s.index), `[${s.title}](session-${pad2(s.index)}.md)`, s.style, String(s.minutes), s.outcomeIds.join(", "),
  ])));
  return out.join("\n") + "\n";
}

function blockMd(b: HourBlock): string[] {
  return [`### ${b.title}`, "", `*${b.kind}, ${b.minutes} min, style: ${b.style}${b.outcomeIds.length ? `, outcomes: ${b.outcomeIds.join(", ")}` : ""}*`, "", b.activity, ""];
}

function sessionMd(course: Course, planName: string, s: Session): string {
  const out: string[] = [`# Session ${s.index}: ${s.title}`, "", `Plan: ${planName} | ${s.minutes} minutes | style: ${s.style}`, ""];
  out.push("## Outcomes", "");
  for (const id of s.outcomeIds) out.push(`- **${id}** ${outcomeText(course, id)}`);
  if (s.stale) out.push("", "> Note: an upstream item changed after this session was drafted. Review before use.");
  const blocks = sortedBlocks(s.blocks);
  out.push("", "## Hour-wise plan", "");
  if (blocks.length) {
    out.push(table(["Time", "Min", "Block", "Type", "Style"], blocks.map((b) => [blockRange(b), String(b.minutes), b.title, b.kind, b.style])));
    out.push("");
    for (const b of blocks) out.push(...blockMd(b));
  } else out.push("No hour plan drafted yet.", "");
  const examples = blocks.filter((b) => b.industryExample);
  if (examples.length) {
    out.push("## Industry examples", "");
    for (const b of examples) {
      const e = b.industryExample!;
      out.push(`- **${b.title}** (${e.sector}): ${e.text}`);
      for (const src of e.sources) out.push(`  - Source: [${src.title}](${src.url})`);
    }
    out.push("");
  }
  const checks = blocks.filter((b) => b.check.length);
  if (checks.length) {
    out.push("## Quick checks", "");
    for (const b of checks) {
      out.push(`**${b.title}**`, "");
      b.check.forEach((q, i) => out.push(`${i + 1}. ${q}`));
      out.push("");
    }
  }
  const links = approvedLinks(s);
  if (links.length) {
    out.push("## Further learning", "");
    for (const l of links) {
      const where = l.channelOrSite ? `, ${l.channelOrSite}` : "";
      const dur = l.durationSec ? `, ${Math.round(l.durationSec / 60)} min` : "";
      out.push(`- [${l.title}](${l.url}) (${l.kind}${where}${dur}): ${l.why}`);
    }
    out.push("");
  }
  const n = s.caseStudies.length;
  out.push("## Case studies", "", n ? `${n} case stud${n === 1 ? "y" : "ies"} available for this session (paid feature, not included in this export).` : "No case studies for this session.", "");
  return out.join("\n");
}

export function markdownExport(course: Course): Record<string, string> {
  const files: Record<string, string> = { "README.md": readme(course), "outcomes.md": outcomes(course) };
  for (const p of course.plans) {
    files[`plans/${p.id}/README.md`] = planReadme(course, p.id);
    for (const s of p.sessions) files[`plans/${p.id}/session-${pad2(s.index)}.md`] = sessionMd(course, p.name, s);
  }
  return files;
}
