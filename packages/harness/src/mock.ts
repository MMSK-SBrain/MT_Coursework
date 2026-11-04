// MockStages: deterministic, network-free Stages for the web app's dev mode and for tests.
// Returns schema-valid data based on the AEZC517 Systems Engineering example; for other courses it
// derives plausible, rule-passing data from the course's own modules and outcomes.
import {
  AUTO_STYLE, BLOOM_ORDER, BLOOM_VERBS, VIDEO_BY_PATH, editTarget,
  CaseStudy as CaseStudySchema, FitChange as FitChangeSchema, FurtherLink as FurtherLinkSchema, HourBlock as HourBlockSchema,
  LearningPlan as LearningPlanSchema, Objective as ObjectiveSchema, Outcome as OutcomeSchema,
  type BlockKind, type CaseStudy, type Course, type CourseBrief, type EditInstruction, type FitChange, type FurtherLink,
  type Generated, type HourBlock, type InputFile, type JobRole, type LearningPlan, type Module, type Objective, type Outcome,
  type OutcomeSuggestion, type ParsedInputs, type PlanSpec, type Provenance, type Stages, type TeachingStyle,
} from "@cg/core";
import type { z } from "zod";
import {
  BRIEF, CLASSROOM_SESSIONS, FIT, FIXTURE_TIME, KEYWORDS, MODULES, MODULES_WITH_MOS, OBJECTIVES, OUTCOMES, PAGES, ROLES, S3_BLOCKS,
  S3_OUTCOMES, VIDEOS, YOUTUBE_SESSIONS,
} from "./fixtures/aezc517.js";
import { findSession, mergeLocked, sessionShape, type DraftOutcomesValue } from "./stages.js";
import { deriveModuleOutcomes, deriveSessionOutcomes } from "./hierarchy.js";
import { parseInputsPrompt } from "./prompts/parseInputs.js";
import { roleMatchPrompt } from "./prompts/findRoles.js";
import { proposeFitPrompt } from "./prompts/proposeFit.js";
import { draftOutcomesPrompt } from "./prompts/draftOutcomes.js";
import { suggestOutcomeEditPrompt } from "./prompts/suggestOutcomeEdit.js";
import { draftPlanPrompt } from "./prompts/draftPlan.js";
import { draftHourPlanPrompt } from "./prompts/draftHourPlan.js";
import { findFurtherLearningPrompt } from "./prompts/findFurtherLearning.js";
import { draftCaseStudyPrompt } from "./prompts/draftCaseStudy.js";

type BlockKindT = z.infer<typeof BlockKind>;

export interface MockStagesOptions {
  /** Defaults to the fixed fixture time so output is fully deterministic. */
  now?: () => Date;
  /** Simulated latency in ms (dev mode only; 0 in tests). */
  delayMs?: number;
}

export class MockStages implements Stages {
  constructor(private readonly opts: MockStagesOptions = {}) {}

  private prov(p: { id: string; version: string }, builtFrom: string[] = []): Provenance {
    return {
      model: "mock", promptId: p.id, promptVersion: p.version, costUsd: 0,
      createdAt: this.opts.now ? this.opts.now().toISOString() : FIXTURE_TIME, builtFrom: [...new Set(builtFrom)],
    };
  }

  private async ok<T>(value: T, provenance: Provenance, warnings: string[] = []): Promise<Generated<T>> {
    if (this.opts.delayMs) await new Promise((r) => setTimeout(r, this.opts.delayMs));
    return { value, provenance, warnings };
  }

  async parseInputs(files: InputFile[]): Promise<Generated<ParsedInputs>> {
    const prov = this.prov(parseInputsPrompt, files.map((f) => f.meta.id));
    const handout = OUTCOMES.filter((o) => o.origin === "handout");
    return this.ok({
      brief: BRIEF,
      modules: MODULES,
      objectives: OBJECTIVES.map((o) => ({ ...o, provenance: prov })),
      outcomes: handout.map((o) => ({ ...o, provenance: prov })),
      gaps: ["CO4, CO5 and LO4 are empty in the handout", "M4 is in the module sheet but not in the handout", "M7 is in the handout but not in the module sheet"],
    }, prov);
  }

  async findRoles(_brief: CourseBrief, modules: Module[], keywords?: string[]) {
    const prov = this.prov(roleMatchPrompt, modules.map((m) => m.id));
    const roles: JobRole[] = ROLES.map((r) => ({ ...r }));
    return this.ok({ keywords: keywords?.length ? keywords : KEYWORDS, roles, occupationsRead: ROLES.length }, prov);
  }

  async proposeFit(course: Course): Promise<Generated<FitChange[]>> {
    const selected = course.roles.filter((r) => r.selected);
    const modIds = new Set(course.modules.map((m) => m.id));
    const roleIds = new Set(selected.map((r) => r.id));
    const prov = this.prov(proposeFitPrompt, [...roleIds, ...modIds]);
    const fixtureFits = FIT.every((f) => modIds.has(f.targetModuleId) && f.roleIds.some((r) => roleIds.has(r)));
    const value = fixtureFits
      ? FIT.map((f) => ({ ...f, roleIds: f.roleIds.filter((r) => roleIds.has(r)), provenance: { ...prov, builtFrom: [...f.roleIds, f.targetModuleId] } }))
      : selected.slice(0, 4).map((r, i) => FitChangeSchema.parse({
        id: `f${i + 1}`,
        kind: i === 0 ? "add" : "strengthen",
        text: `${r.skills[0] ?? r.title} applied to ${course.modules[i % course.modules.length]?.title ?? "the course"}`,
        reason: `${r.title} needs ${r.skills.filter((k) => !r.matchedSkills.includes(k)).slice(0, 2).join(" and ") || r.skills[0] || "this skill"} (ESCO essential skills)`,
        targetModuleId: course.modules[i % course.modules.length]?.id ?? "new",
        hoursDelta: 1,
        roleIds: [r.id],
        provenance: { ...prov, builtFrom: [r.id] },
      }));
    return this.ok(value, prov);
  }

  async draftOutcomes(course: Course): Promise<Generated<DraftOutcomesValue>> {
    const prov = { ...this.prov(draftOutcomesPrompt, course.modules.map((m) => m.id)), structureVersion: course.structureVersion };
    const isFixture = isFixtureCourse(course);
    const roleIds = new Set(course.roles.map((r) => r.id));
    const objectives: Objective[] = isFixture
      ? OBJECTIVES.map((o) => ({ ...o, locked: false, provenance: prov }))
      : [ObjectiveSchema.parse({ id: "CO1", text: `Apply the methods of ${course.brief.title} to realistic ${course.brief.industry} work.`, provenance: prov })];
    const outcomes: Outcome[] = isFixture
      ? OUTCOMES.map((o) => ({ ...o, locked: false, roleIds: o.roleIds.filter((r) => roleIds.has(r)), provenance: { ...prov, builtFrom: [...o.moduleIds, ...o.roleIds] } }))
      : course.modules.map((m, i) => OutcomeSchema.parse({
        id: `LO${i + 1}`,
        text: `Apply the core methods of ${lowerFirst(m.title)} to a realistic ${course.brief.industry} task.`,
        bloom: "apply", moduleIds: [m.id], objectiveIds: ["CO1"], origin: "new",
        provenance: { ...prov, builtFrom: [m.id] },
      }));
    const finalOutcomes = mergeLocked(course.outcomes, outcomes, "LO");
    const drafted = isFixture
      ? MODULES_WITH_MOS.map((m) => ({ ...m, outcomes: m.outcomes.map((mo) => ({ ...mo, provenance: { ...prov, builtFrom: [m.id, ...mo.outcomeIds] } })) }))
      : deriveModuleOutcomes(course.modules.map((m) => ({ ...m, outcomes: [] })), finalOutcomes, prov);
    // Locked MOs are kept; drafted ones fill in around them.
    const modules = course.modules.map((m) => {
      const fresh = drafted.find((d) => d.id === m.id)?.outcomes ?? [];
      return { ...m, outcomes: mergeLocked(m.outcomes, fresh, `${m.id}.MO`) };
    });
    return this.ok({ objectives: mergeLocked(course.objectives, objectives, "CO"), outcomes: finalOutcomes, modules }, prov);
  }

  async suggestOutcomeEdit(course: Course, outcomeId: string, instruction: EditInstruction): Promise<Generated<OutcomeSuggestion>> {
    const o = editTarget(course, outcomeId); // LO, MO or CO
    const prov = this.prov(suggestOutcomeEditPrompt, [o.id]);
    return this.ok({ targetId: o.id, ...mockSuggestion(o, instruction) }, prov);
  }

  async draftPlan(course: Course, spec: PlanSpec): Promise<Generated<LearningPlan>> {
    const prov = { ...this.prov(draftPlanPrompt, course.outcomes.map((o) => o.id)), structureVersion: course.structureVersion };
    const known = new Set(course.outcomes.map((o) => o.id));
    const fixture = !isFixtureCourse(course) ? null : spec.path === "classroom" ? CLASSROOM_SESSIONS : spec.path === "youtube" ? YOUTUBE_SESSIONS : null;
    const covers = (ss: { outcomeIds: string[] }[]) => {
      const taught = new Set(ss.flatMap((s) => s.outcomeIds));
      return course.outcomes.every((o) => taught.has(o.id)) && ss.every((s) => s.outcomeIds.every((x) => known.has(x)));
    };
    const shape = sessionShape(spec.path, course.brief.contactHours, course.outcomes.length);
    const sessions = fixture && covers(fixture)
      ? fixture.map((s) => ({ ...s, outcomeIds: [...s.outcomeIds] }))
      : course.outcomes.map((o) => ({
        title: `${o.text.split(/[,.]/)[0]}`,
        outcomeIds: [o.id],
        style: (spec.style === "auto" ? AUTO_STYLE[o.bloom] : spec.style) as TeachingStyle,
        minutes: shape.minutes,
        video: VIDEO_BY_PATH[spec.path][0]!,
      }));
    const planId = `p${course.plans.length + 1}`;
    const indexed = sessions.map((s, i) => ({ ...s, index: i + 1 }));
    const sos = deriveSessionOutcomes(course, indexed, prov);
    // The classroom fixture uses the hand-written s3 outcomes when the course has the fixture's MOs.
    const moIds = new Set(course.modules.flatMap((m) => m.outcomes.map((o) => o.id)));
    const usedFixture = spec.path === "classroom" && !!fixture && covers(fixture);
    if (usedFixture && S3_OUTCOMES.every((so) => so.moduleOutcomeIds.every((id) => moIds.has(id))) && /requirement/i.test(indexed[2]?.title ?? "")) {
      sos[2] = S3_OUTCOMES.map((so) => ({ ...so, provenance: { ...prov, builtFrom: so.moduleOutcomeIds } }));
    }
    const value = LearningPlanSchema.parse({
      id: planId,
      name: spec.name ?? (spec.path === "classroom" && fixture ? "BITS WILP classroom" : `${course.brief.title}: ${spec.path} plan`),
      path: spec.path,
      defaultStyle: spec.style,
      ...(spec.audienceVariant ? { audienceVariant: spec.audienceVariant } : {}),
      sessions: sessions.map((s, i) => ({
        id: `${planId}-s${i + 1}`, index: i + 1, ...s, sessionOutcomes: sos[i] ?? [],
        video: VIDEO_BY_PATH[spec.path].includes(s.video) ? s.video : VIDEO_BY_PATH[spec.path][0],
        provenance: { ...prov, builtFrom: s.outcomeIds },
      })),
      provenance: prov,
    });
    return this.ok(value, prov);
  }

  async draftHourPlan(course: Course, planId: string, sessionId: string): Promise<Generated<HourBlock[]>> {
    const { session } = findSession(course, planId, sessionId);
    const prov = { ...this.prov(draftHourPlanPrompt, session.outcomeIds), structureVersion: course.structureVersion };
    const soIds = session.sessionOutcomes.map((so) => so.id);
    const useFixture = session.minutes === 120 && S3_OUTCOMES.every((so) => soIds.includes(so.id)) && /requirement/i.test(session.title);
    const drafts = useFixture
      ? S3_BLOCKS.map((b) => ({ ...b, outcomeIds: b.outcomeIds.filter((x) => session.outcomeIds.includes(x)) }))
      : genericBlocks(session.minutes, session.outcomeIds, soIds, session.style, session.title, course);
    const value = drafts.map((b, i) => HourBlockSchema.parse({ ...b, id: `${session.id}-b${i + 1}`, provenance: { ...prov, builtFrom: b.outcomeIds } }));
    return this.ok(value, prov);
  }

  async findFurtherLearning(course: Course, planId: string, sessionId: string): Promise<Generated<FurtherLink[]>> {
    const { session } = findSession(course, planId, sessionId);
    const prov = this.prov(findFurtherLearningPrompt, session.outcomeIds);
    const n = session.index % VIDEOS.length;
    const vids = [VIDEOS[n]!, VIDEOS[(n + 1) % VIDEOS.length]!];
    const page = PAGES[session.index % PAGES.length]!;
    const value: FurtherLink[] = [
      ...vids.map((v, i) => FurtherLinkSchema.parse({
        id: `${session.id}-l${i + 1}`, kind: "youtube", title: v.title, url: v.url, channelOrSite: v.channel,
        durationSec: v.durationSec, publishedAt: v.publishedAt, why: `Reinforces "${session.title}" with a short worked explanation.`,
        lastCheckedAt: prov.createdAt,
      })),
      FurtherLinkSchema.parse({
        id: `${session.id}-l3`, kind: "article", title: page.title, url: page.url, channelOrSite: new URL(page.url).hostname,
        why: "A reference to read after the session.", lastCheckedAt: prov.createdAt,
      }),
    ];
    return this.ok(value, prov);
  }

  async draftCaseStudy(course: Course, planId: string, sessionId: string, label: CaseStudy["label"]): Promise<Generated<CaseStudy>> {
    const { session } = findSession(course, planId, sessionId);
    const prov = this.prov(draftCaseStudyPrompt, session.outcomeIds);
    const value = CaseStudySchema.parse({
      id: `${session.id}-cs${session.caseStudies.length + 1}`,
      label,
      title: label === "real" ? "What systems engineering is for: the INCOSE view" : "Thermal derating at a Tier-1 BMS supplier (call it Veltra)",
      background: label === "real"
        ? "INCOSE describes systems engineering as an interdisciplinary approach to enable the realisation of successful systems. Learners read the source and decide which of the course's processes a small EV programme team should adopt first, given a fixed budget and a launch date."
        : "Veltra, a fictional Tier-1 supplier, is six months from start of production on a 400 V battery management system. A field test shows the pack hitting its thermal limit on a hill climb at 40 °C ambient. The OEM wants a fix without a hardware change. The team must decide between a stricter derating curve, a revised cooling request to the OEM, or a software change to cell balancing.",
      data: label === "real" ? "" : "| Option | Peak cell temp (°C) | Range impact | Change cost |\n|---|---|---|---|\n| Stricter derating | 52 | -4% | Low |\n| More cooling (OEM) | 49 | 0% | High |\n| Balancing change | 55 | -1% | Medium |",
      questions: [
        "Which stakeholder needs are in conflict here?",
        "Write one verifiable requirement that captures the thermal limit.",
        "Evaluate the three options with a weighted trade study and justify your choice.",
      ],
      teachingNote: "Run in groups of three for 30 minutes. Expect learners to jump to a solution; push them to state the requirement first. A strong answer weights safety and range above change cost and names how the choice will be verified on HIL.",
      sources: label === "real" ? [{ title: PAGES[0]!.title, url: PAGES[0]!.url }] : [],
      outcomeIds: session.outcomeIds,
      provenance: prov,
    });
    return this.ok(value, prov);
  }
}

/** The AEZC517 fixture course (same modules), whose hand-written data the mock may reuse. */
function isFixtureCourse(course: Pick<Course, "modules">): boolean {
  return course.modules.length === MODULES.length && course.modules.every((m, i) => m.id === MODULES[i]!.id && m.title === MODULES[i]!.title);
}

function lowerFirst(s: string) {
  return s.charAt(0).toLowerCase() + s.slice(1);
}

/** Deterministic edit that passes the core verb rules. */
export function mockSuggestion(o: Outcome, ins: EditInstruction): Omit<OutcomeSuggestion, "targetId"> {
  const words = o.text.trim().split(/\s+/);
  const rest = words.slice(1).join(" ").replace(/\.$/, "");
  const verb = (b: Outcome["bloom"]) => cap(BLOOM_VERBS[b][0]!);
  switch (ins.kind) {
    case "raiseBloom": {
      const next = BLOOM_ORDER[Math.min(BLOOM_ORDER.indexOf(o.bloom) + 1, BLOOM_ORDER.length - 1)]!;
      const b = next === o.bloom ? o.bloom : next;
      return { proposed: [{ text: `${verb(b)} ${rest}.`, bloom: b }], reason: `Raised from ${o.bloom} to ${b}.` };
    }
    case "measurable":
      return { proposed: [{ text: `${o.text.replace(/\.$/, "")}, given a real programme document, scored against the session rubric.`, bloom: o.bloom }], reason: "Added a condition and a criterion so it can be assessed." };
    case "industryContext":
      return { proposed: [{ text: `${o.text.replace(/\.$/, "")}, using templates and tools from an OEM or Tier-1 programme.`, bloom: o.bloom }], reason: "Linked to the essential skills of the selected roles." };
    case "shorten": {
      const cut = o.text.split(",")[0]!.replace(/\.$/, "");
      const short = cut.length < o.text.length - 1 ? cut : words.slice(0, Math.max(3, words.length - 3)).join(" ").replace(/\.$/, "");
      return { proposed: [{ text: `${short}.`, bloom: o.bloom }], reason: "Cut to the core verb and object." };
    }
    case "split": {
      const [a, ...b] = o.text.split(",");
      const first = `${a!.replace(/\.$/, "")}.`;
      const second = b.length ? `${verb(o.bloom)} ${b.join(",").trim().replace(/^(using|with|and)\s+/i, "").replace(/\.$/, "")}.` : `${verb("apply")} this to the capstone system.`;
      return { proposed: [{ text: first, bloom: o.bloom }, { text: second, bloom: b.length ? o.bloom : "apply" }], reason: "Two outcomes, each assessable on its own." };
    }
    case "matchHandout":
      return { proposed: [{ text: o.text.replace("vehicle programme", "system").replace("automotive ", ""), bloom: o.bloom }], reason: "Aligned with the handout wording." };
    default:
      return { proposed: [{ text: `${o.text.replace(/\.$/, "")}${ins.note ? `, revised for: ${ins.note}` : ""}.`, bloom: o.bloom }], reason: ins.note ? `Your instruction: “${ins.note}”` : "Rewritten." };
  }
}

function cap(s: string) {
  return s.charAt(0).toUpperCase() + s.slice(1);
}

type BlockDraft = Omit<HourBlock, "id" | "provenance">;

/** Blocks that satisfy hourBlockProblems for any session length. */
export function genericBlocks(minutes: number, outcomeIds: string[], sessionOutcomeIds: string[], style: TeachingStyle, title: string, course: Course): BlockDraft[] {
  const hours = Math.ceil(minutes / 60);
  const out: BlockDraft[] = [];
  const role = course.roles.find((r) => r.selected);
  for (let h = 1; h <= hours; h++) {
    const m = h < hours ? 60 : minutes - 60 * (hours - 1);
    const first = h === 1, last = h === hours;
    let plan: [BlockKindT, number][] = [];
    if (first) plan.push(["hook", 1]);
    if (!first && minutes > 90 && h === 2) plan.push(["break", 1]);
    plan.push(["teach", 3], ["activity", 3]);
    if (last) plan.push(["check", 1], ["wrap", 1]);
    if (m < plan.length * 2) plan = [["teach", 1]];
    const total = plan.reduce((a, [, w]) => a + w, 0);
    let cursor = 0;
    plan.forEach(([kind, w], i) => {
      const len = i === plan.length - 1 ? m - cursor : Math.max(1, Math.floor((m * w) / total));
      const b: BlockDraft = {
        hour: h, startMin: cursor, minutes: len, kind, title: blockTitle(kind, title),
        activity: blockActivity(kind, title),
        outcomeIds: kind === "break" ? [] : [...outcomeIds],
        sessionOutcomeIds: kind === "break" ? [] : [...sessionOutcomeIds],
        style, check: kind === "check" || kind === "wrap" ? [`What is the one idea from "${title}" you would use at work?`] : [],
        needsSlides: kind === "teach",
        ...(kind === "teach" && role && h === 1 ? { industryExample: { text: `${role.title}s need ${role.skills.slice(0, 2).join(" and ")}; show where this session's idea appears in that work.`, sector: course.brief.industry, roleIds: [role.id], sources: role.evidence.slice(0, 1).map((e) => ({ title: e.title, url: e.url })) } } : {}),
      };
      out.push(b);
      cursor += len;
    });
  }
  return out;
}

function blockTitle(kind: BlockKindT, title: string) {
  return ({ hook: "Hook", teach: `Core idea: ${title}`, activity: "Practice in groups", case: "Case", check: "Quick check", wrap: "Wrap", break: "Break" } as const)[kind];
}

function blockActivity(kind: BlockKindT, title: string) {
  return ({
    hook: `Open with a short real-world question about ${title}; collect answers from the room.`,
    teach: `Present the core idea of ${title} with one worked example, then pause for questions.`,
    activity: "Learners work in groups of three on a short task and present their output.",
    case: "Groups analyse a short case and report a decision.",
    check: "Three quick-check questions, answered on cards.",
    wrap: "Summarise the key points and preview the next session.",
    break: "Break.",
  } as const)[kind];
}
