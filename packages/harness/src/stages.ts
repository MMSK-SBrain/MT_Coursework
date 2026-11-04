// OpenRouter-backed implementation of the Stages contract from @cg/core.
import {
  CaseStudy as CaseStudySchema, FitChange as FitChangeSchema, FurtherLink as FurtherLinkSchema,
  HourBlock as HourBlockSchema, JobRole as JobRoleSchema, LearningPlan as LearningPlanSchema,
  Objective as ObjectiveSchema, Outcome as OutcomeSchema, OutcomeSuggestion as OutcomeSuggestionSchema,
  PATH_FAMILY, VIDEO_BY_PATH,
  type CaseStudy, type Course, type CourseBrief, type EditInstruction, type FitChange, type FurtherLink, type Generated,
  type HourBlock, type InputFile, type JobRole, type JobSource, type LearningPath, type LearningPlan, type LinkSource,
  type Module, type Objective, type Outcome, type OutcomeSuggestion, type ParsedInputs, type PlanSpec, type Provenance, type Stages,
} from "@cg/core";
import { loadConfig, type HarnessConfig, type StageName } from "./config.js";
import { OpenRouterClient, type ChatClient } from "./openrouter.js";
import { mergeProvenance, runStage, type StageCall, type StageResult } from "./runner.js";
import { ExampleStore } from "./examples.js";
import { fitProblems, hourPlanProblems, indexProblems, outcomeSetProblems, planProblems, suggestionProblems } from "./checks.js";
import { outcomeVerbProblem } from "@cg/core";
import { FIT_RUBRIC, OUTCOMES_RUBRIC } from "./prompts/review.js";
import { parseInputsPrompt } from "./prompts/parseInputs.js";
import { roleClusterPrompt, roleKeywordsPrompt } from "./prompts/findRoles.js";
import { proposeFitPrompt } from "./prompts/proposeFit.js";
import { draftOutcomesPrompt } from "./prompts/draftOutcomes.js";
import { suggestOutcomeEditPrompt } from "./prompts/suggestOutcomeEdit.js";
import { draftPlanPrompt } from "./prompts/draftPlan.js";
import { draftHourPlanPrompt, type EvidenceItem } from "./prompts/draftHourPlan.js";
import { findFurtherLearningPrompt } from "./prompts/findFurtherLearning.js";
import { draftCaseStudyPrompt } from "./prompts/draftCaseStudy.js";

/** Turns an uploaded file into text. The default handles text formats only (see TEXT_MIMES). */
export type TextExtractor = (f: InputFile) => Promise<string>;

const TEXT_EXT = /\.(txt|md|markdown|csv|tsv|json)$/i;

export const defaultTextExtractor: TextExtractor = async (f) => {
  if (f.meta.mime.startsWith("text/") || f.meta.mime === "application/json" || TEXT_EXT.test(f.meta.filename)) {
    return new TextDecoder("utf-8").decode(f.bytes);
  }
  throw new Error(
    `${f.meta.filename}: ${f.meta.mime} needs a text extractor (docx/pdf/xlsx). Pass extractText to OpenRouterStages, or upload .txt/.csv.`,
  );
};

export interface OpenRouterStagesOptions {
  jobs: JobSource;
  links: LinkSource;
  client?: ChatClient;
  config?: HarnessConfig;
  examples?: ExampleStore;
  extractText?: TextExtractor;
  now?: () => Date;
}

/** Session length and count suggested per learning path. */
export function sessionShape(path: LearningPath, contactHours: number, outcomeCount: number): { count: number; minutes: number } {
  const clamp = (n: number, lo: number, hi: number) => Math.max(lo, Math.min(hi, Math.round(n)));
  switch (path) {
    case "bootcamp": return { minutes: 360, count: clamp((contactHours * 60) / 360, 1, 30) };
    case "elearning": return { minutes: 30, count: clamp(outcomeCount * 2, 3, 40) };
    case "micro": return { minutes: 5, count: clamp(outcomeCount * 3, 4, 40) };
    case "youtube": return { minutes: 8, count: clamp(outcomeCount, 4, 12) };
    case "shorts": return { minutes: 1, count: clamp(outcomeCount * 2, 4, 20) };
    default: return { minutes: 120, count: clamp((contactHours * 60) / 120, 1, 60) };
  }
}

export class OpenRouterStages implements Stages {
  private readonly client: ChatClient;
  private readonly config: HarnessConfig;
  private readonly examples: ExampleStore;
  private readonly extract: TextExtractor;
  private readonly now: () => Date;
  /** Trace of the most recent runner call per stage (for the eval CLI and debugging). */
  readonly lastTrace = new Map<StageName, StageResult<unknown>["trace"]>();

  constructor(private readonly opts: OpenRouterStagesOptions) {
    this.client = opts.client ?? new OpenRouterClient();
    this.config = opts.config ?? loadConfig();
    this.examples = opts.examples ?? new ExampleStore();
    this.extract = opts.extractText ?? defaultTextExtractor;
    this.now = opts.now ?? (() => new Date());
  }

  private async run<I, O>(call: Omit<StageCall<I, O>, "examples">, exclude?: Course | CourseBrief): Promise<StageResult<O>> {
    const ex = exclude && "brief" in exclude ? { id: exclude.id, code: exclude.brief.code } : { code: exclude?.code };
    const examples = await this.examples.forStage(call.stage, { exclude: ex });
    const r = await runStage({ ...call, examples }, { client: this.client, config: this.config, now: this.now });
    this.lastTrace.set(call.stage, r.trace);
    return r;
  }

  private emptyProvenance(promptId: string, builtFrom: string[]): Provenance {
    return { model: "none", promptId, promptVersion: "0", costUsd: 0, createdAt: this.now().toISOString(), builtFrom };
  }

  // ---- Stage 1 ---------------------------------------------------------------------------------

  async parseInputs(files: InputFile[]): Promise<Generated<ParsedInputs>> {
    const warnings: string[] = [];
    const texts: { filename: string; kind: InputFile["meta"]["kind"]; text: string }[] = [];
    for (const f of files) {
      try {
        texts.push({ filename: f.meta.filename, kind: f.meta.kind, text: await this.extract(f) });
      } catch (e) {
        warnings.push((e as Error).message);
      }
    }
    if (!texts.length) throw new Error(`No readable input files. ${warnings.join(" ")}`);

    const r = await this.run({
      stage: "parseInputs",
      prompt: parseInputsPrompt,
      input: { files: texts },
      builtFrom: files.map((f) => f.meta.id),
      rules: (d) => {
        const ids = d.modules.map((m) => m.id);
        const p = ids.filter((id, i) => ids.indexOf(id) !== i).map((id) => `duplicate module id ${id}`);
        const known = new Set(ids);
        for (const o of d.outcomes) {
          const bad = o.moduleIds.filter((m) => !known.has(m));
          if (bad.length) p.push(`${o.id} names unknown module(s) ${bad.join(", ")}`);
          if (!o.moduleIds.length) p.push(`${o.id} is not mapped to any module; map it to the modules that teach it`);
        }
        return p;
      },
      // Handout wording is copied verbatim, so weak verbs only warn; they are fixed in stage 4.
      advisories: (d) => d.outcomes.map((o) => { const v = outcomeVerbProblem(o); return v ? `Handout ${o.id} ${v}` : null; }).filter((x): x is string => !!x),
    });
    const prov = r.provenance;
    const allModules = r.value.modules.map((m) => m.id);
    const value: ParsedInputs = {
      brief: r.value.brief,
      modules: r.value.modules,
      objectives: r.value.objectives.map((o) => ObjectiveSchema.parse({ ...o, provenance: prov })),
      outcomes: r.value.outcomes.map((o) => OutcomeSchema.parse({
        ...o, moduleIds: o.moduleIds.length ? o.moduleIds : allModules, origin: "handout", provenance: prov,
      })),
      gaps: r.value.gaps,
    };
    return { value, provenance: prov, warnings: [...warnings, ...r.warnings] };
  }

  // ---- Stage 2 ---------------------------------------------------------------------------------

  async findRoles(brief: CourseBrief, modules: Module[], keywords?: string[]) {
    let kwProv: Provenance | undefined;
    const warnings: string[] = [];
    if (!keywords?.length) {
      const k = await this.run({
        stage: "findRoles", prompt: roleKeywordsPrompt, input: { brief, modules }, builtFrom: modules.map((m) => m.id),
      }, brief);
      keywords = k.value.keywords;
      kwProv = k.provenance;
      warnings.push(...k.warnings);
    }
    const postings = await this.opts.jobs.search({ keywords, markets: brief.markets, days: 90, limit: 200 });
    if (!postings.length) {
      return {
        value: { keywords, roles: [], postingsRead: 0 },
        provenance: kwProv ?? this.emptyProvenance(roleClusterPrompt.id, modules.map((m) => m.id)),
        warnings: [...warnings, "No job postings found for these keywords and markets. Try broader keywords."],
      };
    }
    const sample = postings.slice(0, 80); // keep the call narrow
    const r = await this.run({
      stage: "findRoles",
      prompt: roleClusterPrompt,
      input: { brief, modules, postings: sample },
      builtFrom: modules.map((m) => m.id),
      rules: (d) => {
        const idx = d.roles.flatMap((x) => x.postingIdx);
        const p = indexProblems("posting", idx, sample.length);
        if (!d.roles.length) p.push("no roles returned although postings were supplied");
        return p;
      },
    }, brief);
    const roles: JobRole[] = r.value.roles.map((x, i) => {
      const idx = [...new Set(x.postingIdx.filter((n) => n < sample.length))];
      const ps = idx.map((n) => sample[n]!);
      return JobRoleSchema.parse({
        id: `r${i + 1}`,
        title: x.title,
        postings: ps.length, // counted in code, never taken from the model
        ...(x.experience ? { experience: x.experience } : {}),
        skills: x.skills,
        moduleMatch: Math.round(x.moduleMatch),
        evidence: ps.slice(0, 5).map((p) => ({ title: `${p.title}${p.company ? `, ${p.company}` : ""} (${p.location})`, url: p.url, source: p.source })),
      });
    }).filter((x) => x.postings > 0).sort((a, b) => b.postings - a.postings).map((x, i) => ({ ...x, id: `r${i + 1}` }));
    if (postings.length > sample.length) warnings.push(`Grouped the first ${sample.length} of ${postings.length} postings into roles.`);
    return {
      value: { keywords, roles, postingsRead: postings.length },
      provenance: kwProv ? mergeProvenance(r.provenance, kwProv) : r.provenance,
      warnings: [...warnings, ...r.warnings],
    };
  }

  // ---- Stage 3 ---------------------------------------------------------------------------------

  async proposeFit(course: Course): Promise<Generated<FitChange[]>> {
    const roles = course.roles.filter((r) => r.selected);
    if (!roles.length) throw new Error("proposeFit needs at least one selected role.");
    const r = await this.run({
      stage: "proposeFit",
      prompt: proposeFitPrompt,
      input: { course, roles },
      builtFrom: [...roles.map((x) => x.id), ...course.modules.map((m) => m.id)],
      rules: (d) => fitProblems(d.changes, course.modules, roles.map((x) => x.id), course.brief.contactHours),
      rubric: { rubric: FIT_RUBRIC, contextText: fitContext(course, roles) },
    }, course);
    const value = r.value.changes.map((c, i) => FitChangeSchema.parse({
      ...c, id: `f${i + 1}`, decision: "pending",
      provenance: { ...r.provenance, builtFrom: [...new Set([...c.roleIds, ...(c.targetModuleId === "new" ? [] : [c.targetModuleId])])], structureVersion: course.structureVersion },
    }));
    return { value, provenance: r.provenance, warnings: r.warnings };
  }

  // ---- Stage 4 ---------------------------------------------------------------------------------

  async draftOutcomes(course: Course): Promise<Generated<{ objectives: Objective[]; outcomes: Outcome[] }>> {
    const r = await this.run({
      stage: "draftOutcomes",
      prompt: draftOutcomesPrompt,
      input: { course },
      builtFrom: [...course.modules.map((m) => m.id), ...course.roles.filter((x) => x.selected).map((x) => x.id)],
      rules: (d) => {
        const p = outcomeSetProblems(d, course.modules);
        for (const lo of course.outcomes.filter((o) => o.locked)) {
          const got = d.outcomes.find((o) => o.id === lo.id);
          if (!got || got.text !== lo.text) p.push(`locked outcome ${lo.id} must be returned unchanged`);
        }
        return p;
      },
      rubric: { rubric: OUTCOMES_RUBRIC, contextText: outcomesContext(course) },
    }, course);
    const prov = { ...r.provenance, structureVersion: course.structureVersion };
    const objectives = mergeLocked(
      course.objectives,
      r.value.objectives.map((o) => ObjectiveSchema.parse({ ...o, provenance: prov })),
      "CO",
    );
    const roleIds = new Set(course.roles.map((x) => x.id));
    const outcomes = mergeLocked(
      course.outcomes,
      r.value.outcomes.map((o) => OutcomeSchema.parse({
        ...o, roleIds: o.roleIds.filter((x) => roleIds.has(x)),
        provenance: { ...prov, builtFrom: [...o.moduleIds, ...o.objectiveIds, ...o.roleIds] },
      })),
      "LO",
    );
    return { value: { objectives, outcomes }, provenance: prov, warnings: r.warnings };
  }

  async suggestOutcomeEdit(course: Course, outcomeId: string, instruction: EditInstruction): Promise<Generated<OutcomeSuggestion>> {
    const outcome = course.outcomes.find((o) => o.id === outcomeId);
    if (!outcome) throw new Error(`Unknown outcome ${outcomeId}`);
    const r = await this.run({
      stage: "suggestOutcomeEdit",
      prompt: suggestOutcomeEditPrompt,
      input: { course, outcome, instruction },
      builtFrom: [outcome.id],
      rules: (d) => suggestionProblems(d.proposed, outcome, instruction.kind),
    }, course);
    const value = OutcomeSuggestionSchema.parse({ targetId: outcome.id, proposed: r.value.proposed, reason: r.value.reason });
    return { value, provenance: r.provenance, warnings: r.warnings };
  }

  // ---- Stage 5 ---------------------------------------------------------------------------------

  async draftPlan(course: Course, spec: PlanSpec): Promise<Generated<LearningPlan>> {
    if (!course.outcomes.length) throw new Error("draftPlan needs outcomes.");
    const shape = sessionShape(spec.path, course.brief.contactHours, course.outcomes.length);
    const r = await this.run({
      stage: "draftPlan",
      prompt: draftPlanPrompt,
      input: { course, spec, sessionCount: shape.count, sessionMinutes: shape.minutes },
      builtFrom: course.outcomes.map((o) => o.id),
      rules: (d) => planProblems(d.sessions, course.outcomes, spec.path),
      advisories: (d) => {
        const fam = PATH_FAMILY[spec.path];
        const total = d.sessions.reduce((a, s) => a + s.minutes, 0);
        const target = course.brief.contactHours * 60;
        return (fam === "live" || fam === "blended") && Math.abs(total - target) > 0.1 * target
          ? [`Sessions add up to ${Math.round(total / 60)} h; the brief has ${course.brief.contactHours} contact hours.`] : [];
      },
    }, course);
    const planId = nextId("p", course.plans.map((p) => p.id));
    const prov = { ...r.provenance, structureVersion: course.structureVersion };
    const value = LearningPlanSchema.parse({
      id: planId,
      name: spec.name ?? r.value.name,
      path: spec.path,
      defaultStyle: spec.style,
      ...(spec.audienceVariant ? { audienceVariant: spec.audienceVariant } : {}),
      sessions: r.value.sessions.map((s, i) => ({
        id: `${planId}-s${i + 1}`, index: i + 1, ...s,
        video: VIDEO_BY_PATH[spec.path].includes(s.video) ? s.video : VIDEO_BY_PATH[spec.path][0],
        provenance: { ...prov, builtFrom: s.outcomeIds },
      })),
      provenance: prov,
    });
    return { value, provenance: prov, warnings: r.warnings };
  }

  // ---- Stage 6 ---------------------------------------------------------------------------------

  async draftHourPlan(course: Course, planId: string, sessionId: string): Promise<Generated<HourBlock[]>> {
    const { plan, session } = findSession(course, planId, sessionId);
    const evidence: EvidenceItem[] = course.roles.filter((x) => x.selected)
      .flatMap((role) => role.evidence.slice(0, 2).map((e) => ({ ...e, roleId: role.id })));
    const r = await this.run({
      stage: "draftHourPlan",
      prompt: draftHourPlanPrompt,
      input: { course, plan, session, evidence },
      builtFrom: session.outcomeIds,
      rules: (d) => [
        ...hourPlanProblems(d.blocks, session.minutes, session.outcomeIds),
        ...indexProblems("evidence", d.blocks.flatMap((b) => b.industryExample?.evidenceIdx ?? []).filter((v, i, a) => a.indexOf(v) === i), evidence.length),
      ],
    }, course);
    const prov = { ...r.provenance, structureVersion: course.structureVersion };
    const value = r.value.blocks.map((b, i) => {
      const { industryExample, ...rest } = b;
      return HourBlockSchema.parse({
        ...rest,
        id: `${session.id}-b${i + 1}`,
        ...(industryExample ? {
          industryExample: {
            text: industryExample.text, sector: industryExample.sector, roleIds: industryExample.roleIds,
            sources: industryExample.evidenceIdx.filter((n) => n < evidence.length).map((n) => ({ title: evidence[n]!.title, url: evidence[n]!.url })),
          },
        } : {}),
        provenance: { ...prov, builtFrom: [...b.outcomeIds, ...(industryExample?.roleIds ?? [])] },
      });
    });
    return { value, provenance: prov, warnings: r.warnings };
  }

  async findFurtherLearning(course: Course, planId: string, sessionId: string): Promise<Generated<FurtherLink[]>> {
    const { plan, session } = findSession(course, planId, sessionId);
    const query = `${session.title} ${course.brief.title}`;
    const maxDurationSec = plan.path === "shorts" || plan.path === "micro" ? 600 : 1800;
    const [videos0, pages0] = await Promise.all([
      this.opts.links.youtube({ query, maxDurationSec, limit: 8 }),
      this.opts.links.web({ query, limit: 6 }),
    ]);
    const alive = async <T extends { url: string }>(xs: T[]) =>
      (await Promise.all(xs.map(async (x) => ((await this.opts.links.isAlive(x.url)) ? x : null)))).filter((x): x is Awaited<T> => !!x);
    const [videos, pages] = await Promise.all([alive(videos0), alive(pages0)]);
    const dropped = videos0.length + pages0.length - videos.length - pages.length;
    const warnings = dropped ? [`${dropped} search result(s) did not resolve and were dropped.`] : [];
    if (!videos.length && !pages.length) {
      return { value: [], provenance: this.emptyProvenance(findFurtherLearningPrompt.id, session.outcomeIds), warnings: [...warnings, "No further-learning candidates found."] };
    }
    const r = await this.run({
      stage: "findFurtherLearning",
      prompt: findFurtherLearningPrompt,
      input: { course, session, videos, pages },
      builtFrom: session.outcomeIds,
      rules: (d) => [
        ...indexProblems("video", d.picks.filter((p) => p.source === "video").map((p) => p.idx), videos.length),
        ...indexProblems("page", d.picks.filter((p) => p.source === "page").map((p) => p.idx), pages.length),
        ...(d.picks.length ? [] : ["pick at least one candidate"]),
      ],
    }, course);
    const checkedAt = this.now().toISOString();
    const value: FurtherLink[] = [];
    for (const p of r.value.picks) {
      const id = `${session.id}-l${value.length + 1}`;
      if (p.source === "video") {
        const v = videos[p.idx];
        if (!v) continue;
        value.push(FurtherLinkSchema.parse({
          id, kind: "youtube", title: v.title, url: v.url, channelOrSite: v.channel, durationSec: v.durationSec || undefined,
          publishedAt: v.publishedAt || undefined, why: p.why, approved: false, lastCheckedAt: checkedAt, alive: true,
        }));
      } else {
        const pg = pages[p.idx];
        if (!pg) continue;
        value.push(FurtherLinkSchema.parse({
          id, kind: "article", title: pg.title, url: pg.url, channelOrSite: new URL(pg.url).hostname, why: p.why,
          approved: false, lastCheckedAt: checkedAt, alive: true,
        }));
      }
    }
    return { value, provenance: r.provenance, warnings: [...warnings, ...r.warnings] };
  }

  async draftCaseStudy(course: Course, planId: string, sessionId: string, label: CaseStudy["label"]): Promise<Generated<CaseStudy>> {
    const { session } = findSession(course, planId, sessionId);
    const warnings: string[] = [];
    let sources: { title: string; url: string; snippet: string }[] = [];
    if (label === "real") {
      const found = await this.opts.links.web({ query: `${session.title} ${course.brief.industry} case study`, limit: 6 });
      sources = (await Promise.all(found.map(async (s) => ((await this.opts.links.isAlive(s.url)) ? s : null)))).filter((s): s is NonNullable<typeof s> => !!s);
      if (!sources.length) {
        label = "composite";
        warnings.push("No checkable sources were found, so this case study is labelled Composite instead of Real.");
      }
    }
    const finalLabel = label;
    const r = await this.run({
      stage: "draftCaseStudy",
      prompt: draftCaseStudyPrompt,
      input: { course, session, label: finalLabel, sources },
      builtFrom: session.outcomeIds,
      rules: (d) => [
        ...indexProblems("source", d.sourceIdx, sources.length),
        ...(finalLabel === "real" && !d.sourceIdx.length ? ["a real case study must cite at least one source by index"] : []),
      ],
    }, course);
    const allowed = new Set(session.outcomeIds);
    const outcomeIds = r.value.outcomeIds.filter((o) => allowed.has(o));
    const value = CaseStudySchema.parse({
      id: `${session.id}-cs${session.caseStudies.length + 1}`,
      label: finalLabel,
      title: r.value.title,
      background: r.value.background,
      data: r.value.data,
      questions: r.value.questions,
      teachingNote: r.value.teachingNote,
      sources: finalLabel === "real" ? [...new Set(r.value.sourceIdx)].filter((n) => n < sources.length).map((n) => ({ title: sources[n]!.title, url: sources[n]!.url })) : [],
      outcomeIds: outcomeIds.length ? outcomeIds : session.outcomeIds,
      provenance: r.provenance,
    });
    return { value, provenance: r.provenance, warnings: [...warnings, ...r.warnings] };
  }
}

// ---- helpers ------------------------------------------------------------------------------------

export function findSession(course: Course, planId: string, sessionId: string) {
  const plan = course.plans.find((p) => p.id === planId);
  if (!plan) throw new Error(`Unknown plan ${planId}`);
  const session = plan.sessions.find((s) => s.id === sessionId);
  if (!session) throw new Error(`Unknown session ${sessionId} in plan ${planId}`);
  return { plan, session };
}

function nextId(prefix: string, taken: string[]): string {
  let n = taken.length + 1;
  while (taken.includes(`${prefix}${n}`)) n++;
  return `${prefix}${n}`;
}

/** Keep locked items exactly; add generated ones, renumbering any id that collides with a locked one. */
export function mergeLocked<T extends { id: string; text: string; locked: boolean }>(existing: T[], generated: T[], prefix: string): T[] {
  const locked = existing.filter((x) => x.locked);
  const lockedIds = new Set(locked.map((x) => x.id));
  const lockedTexts = new Set(locked.map((x) => x.text.trim()));
  const out: T[] = [...locked];
  const taken = new Set(lockedIds);
  for (const g of generated) {
    if (lockedTexts.has(g.text.trim()) || lockedIds.has(g.id)) {
      if (lockedIds.has(g.id) && !lockedTexts.has(g.text.trim())) {
        // A new item reusing a locked id: keep it under a fresh id.
        let n = 1;
        while (taken.has(`${prefix}${n}`)) n++;
        taken.add(`${prefix}${n}`);
        out.push({ ...g, id: `${prefix}${n}`, locked: false });
      }
      continue;
    }
    let id = g.id;
    if (taken.has(id)) {
      let n = 1;
      while (taken.has(`${prefix}${n}`)) n++;
      id = `${prefix}${n}`;
    }
    taken.add(id);
    out.push({ ...g, id, locked: false });
  }
  const num = (id: string) => Number(id.replace(/\D/g, "")) || 0;
  return out.sort((a, b) => num(a.id) - num(b.id));
}

function outcomesContext(c: Course): string {
  return [
    `Course: ${c.brief.title} (${c.brief.level}; ${c.brief.audience}; ${c.brief.contactHours} h; ${c.brief.industry})`,
    `Modules: ${c.modules.map((m) => `${m.id} ${m.title}`).join("; ")}`,
    `Selected roles: ${c.roles.filter((r) => r.selected).map((r) => `${r.id} ${r.title} (${r.skills.join(", ")})`).join("; ") || "none"}`,
    `Accepted fit changes: ${c.fit.filter((f) => f.decision === "accepted" || f.decision === "changed").map((f) => `${f.kind} ${f.text}`).join("; ") || "none"}`,
    `Locked outcomes: ${c.outcomes.filter((o) => o.locked).map((o) => o.id).join(", ") || "none"}`,
  ].join("\n");
}

function fitContext(c: Course, roles: JobRole[]): string {
  return [
    `Course: ${c.brief.title} (${c.brief.contactHours} contact hours)`,
    `Modules: ${c.modules.map((m) => `${m.id} ${m.title} (${m.hours} h)`).join("; ")}`,
    `Handout objectives: ${c.objectives.map((o) => `${o.id} ${o.text}`).join("; ") || "none"}`,
    `Selected roles: ${roles.map((r) => `${r.id} ${r.title}, ${r.postings} postings, skills ${r.skills.join(", ")}`).join("; ")}`,
  ].join("\n");
}
