// Local stand-in for @cg/harness until it merges. Returns schema-valid data built from the prototype's sample course
// (AEZC517 Automotive Systems Engineering). No model calls; every item is labelled model "mock".
import {
  AUTO_STYLE, BLOOM_ORDER, BLOOM_VERBS, PATH_FAMILY, VIDEO_BY_PATH,
  type BloomLevel, type CaseStudy, type Course, type EditInstruction, type FitChange, type FurtherLink, type Generated,
  type HourBlock, type InputFile, type JobRole, type LearningPlan, type Module, type Objective, type Outcome,
  type OutcomeSuggestion, type ParsedInputs, type PlanSpec, type Provenance, type Session, type SessionOutcome, type Stages, type TeachingStyle,
  type VideoKind,
} from "@cg/core";
import { findSession } from "./course-logic";

const prov = (promptId: string, builtFrom: string[] = [], structureVersion?: number): Provenance => ({
  model: "mock", promptId, promptVersion: "0", costUsd: 0, createdAt: new Date().toISOString(), builtFrom, structureVersion,
});
const gen = <T>(value: T, provenance: Provenance, warnings: string[] = []): Generated<T> => ({ value, provenance, warnings });
const delay = () => new Promise((r) => setTimeout(r, Number(process.env.MOCK_DELAY_MS ?? 400)));

// ---- Sample data (from the prototype) ------------------------------------------------

const MODULES: (Pick<Module, "id" | "title" | "hours" | "note"> & { src: "both" | "excel" | "handout" })[] = [
  { id: "M1", title: "Systems thinking and the role of the systems engineer", hours: 4, src: "both" },
  { id: "M2", title: "Life cycle models: V-model, agile and hybrids", hours: 4, src: "both" },
  { id: "M3", title: "Stakeholder needs and requirements engineering", hours: 6, src: "both" },
  { id: "M4", title: "Functional and physical architecture, MBSE with SysML", hours: 6, src: "excel", note: "Not in handout" },
  { id: "M5", title: "Interface management and system integration", hours: 4, src: "both" },
  { id: "M6", title: "Verification and validation", hours: 4, src: "both" },
  { id: "M7", title: "Technical management: risk, configuration, trade studies", hours: 4, src: "handout", note: "Not in sheet" },
  { id: "M8", title: "Capstone: EV battery management system", hours: 4, src: "excel" },
];

/** Module outcomes (MOs) per module: [id, text, bloom, parent LO ids]. */
const MOS: Record<string, [string, string, BloomLevel, string[]][]> = {
  M1: [["M1.MO1", "Explain the role of the systems engineer on a cross-functional vehicle programme.", "understand", ["LO1"]]],
  M2: [["M2.MO1", "Compare the V-model, agile and hybrid life cycles for a vehicle programme.", "understand", ["LO1"]]],
  M3: [["M3.MO1", "Write verifiable system requirements traced to stakeholder needs.", "apply", ["LO2"]]],
  M4: [["M4.MO1", "Model the functional architecture of a subsystem in SysML.", "apply", ["LO3"]]],
  M5: [["M5.MO1", "Plan the interface and integration steps for a subsystem.", "analyse", ["LO4"]]],
  M6: [["M6.MO1", "Plan verification and validation across SIL, HIL and vehicle tests.", "analyse", ["LO4"]]],
  M7: [
    ["M7.MO1", "Perform a hazard analysis and derive safety goals under ISO 26262.", "apply", ["LO5"]],
    ["M7.MO2", "Evaluate design alternatives with a structured trade study.", "evaluate", ["LO6"]],
  ],
  M8: [["M8.MO1", "Evaluate BMS design options against thermal and SOC/SOH requirements.", "evaluate", ["LO6"]]],
};

const KEYWORDS = ["systems engineering", "requirements engineering", "V-model", "SysML / MBSE", "interface management", "verification and validation", "HIL / SIL", "DFMEA", "trade study", "battery management system"];

const ROLES: [string, string, number, number, string, string[]][] = [
  ["r1", "Automotive Systems Engineer", 312, 86, "2–8 yrs", ["Requirements", "V-model", "System architecture"]],
  ["r2", "Requirements Engineer", 247, 81, "1–6 yrs", ["Polarion / DOORS", "Traceability", "ASPICE SYS.2"]],
  ["r3", "Functional Safety Engineer (ISO 26262)", 241, 58, "3–10 yrs", ["HARA", "Safety goals", "FMEA / FTA"]],
  ["r4", "MBSE / SysML Architect", 133, 74, "5–12 yrs", ["SysML", "Cameo / Capella", "Variant modelling"]],
  ["r5", "V&V Engineer (HIL / SIL)", 198, 69, "1–6 yrs", ["Test planning", "dSPACE / NI HIL", "Test automation"]],
  ["r6", "BMS Systems Engineer", 176, 72, "2–8 yrs", ["SOC / SOH", "Cell monitoring", "Thermal limits"]],
  ["r7", "ECU Integration Engineer", 119, 63, "1–5 yrs", ["CAN / UDS", "Integration testing", "Flashing"]],
  ["r8", "ADAS Systems Engineer", 204, 55, "2–8 yrs", ["SOTIF", "Sensor fusion", "Scenario testing"]],
  ["r9", "ASPICE Process Consultant", 88, 52, "6–15 yrs", ["ASPICE assessments", "Process improvement"]],
  ["r10", "Automotive Cybersecurity Engineer", 109, 29, "3–8 yrs", ["ISO/SAE 21434", "TARA"]],
  ["r11", "Product Owner, Vehicle Software", 142, 41, "5–12 yrs", ["Backlog", "SAFe", "Stakeholder management"]],
  ["r12", "NPD Programme Engineer", 160, 38, "3–10 yrs", ["Gateways", "APQP", "Risk tracking"]],
];
const PRESELECTED = new Set(["r1", "r2", "r3", "r6"]);

const FIT: [string, FitChange["kind"], string, string, string, number, string[], string?][] = [
  ["f1", "add", "Hazard analysis (HARA) and safety goals under ISO 26262", "Asked for by 3 of 4 selected roles · 241 postings", "M7", 2, ["r1", "r3", "r6"]],
  ["f2", "add", "ASPICE SYS.1–SYS.5 work products and how assessors read them", "Requirements Engineer, Systems Engineer · 188 postings", "M2", 1, ["r1", "r2"]],
  ["f3", "strengthen", "Hands-on requirements tool lab (Polarion or DOORS)", "M3 is theory only; tools named in 64% of Requirements Engineer postings", "M3", 2, ["r2"]],
  ["f4", "add", "BMS requirements: cell monitoring, SOC/SOH, thermal derating", "BMS Systems Engineer · 176 postings", "M8", 2, ["r6"]],
  ["f5", "strengthen", "HIL test-case design from requirements", "Systems Engineer, BMS Systems Engineer", "M6", 1, ["r1", "r6"]],
  ["f6", "trim", "Soft-skills content in M1 (4 h → 2 h)", "Rarely asked for by the selected roles. Kept by default: CO1 in the handout requires it.", "M1", -2, ["r1"], "CO1 in the handout requires soft skills"],
];

const COS: [string, string][] = [
  ["CO1", "Build the hard and soft skills an automotive systems engineer needs on a cross-functional programme."],
  ["CO2", "Explain systems engineering principles, processes and methods as defined by INCOSE and ISO/IEC/IEEE 15288."],
  ["CO3", "Apply systems engineering methods to a complex automotive development, from stakeholder needs to a validated system."],
];

const LOS: [string, string, BloomLevel, string[], string[], Outcome["origin"], string[]][] = [
  ["LO1", "Describe the processes, methods and practices of systems engineering across a vehicle programme life cycle.", "understand", ["M1", "M2"], ["r1"], "handout", ["CO2"]],
  ["LO2", "Write verifiable system requirements with full traceability from stakeholder needs, using a requirements tool.", "apply", ["M3"], ["r2"], "fit", ["CO3"]],
  ["LO3", "Model the functional and physical architecture of an automotive subsystem in SysML.", "apply", ["M4"], ["r1"], "new", ["CO3"]],
  ["LO4", "Plan verification and validation for a subsystem, choosing between SIL, HIL and vehicle-level tests.", "analyse", ["M5", "M6"], ["r6"], "handout", ["CO3"]],
  ["LO5", "Perform a hazard analysis and derive safety goals following ISO 26262 Part 3.", "apply", ["M7"], ["r3"], "fit", ["CO1", "CO3"]],
  ["LO6", "Evaluate design alternatives for an EV battery management system with a structured trade study.", "evaluate", ["M7", "M8"], ["r6"], "handout", ["CO3"]],
];

/** [title, LO ids, style, minutes, video, MO ids the session outcomes serve] */
const PRESET_SESSIONS: Partial<Record<string, [string, string[], TeachingStyle, number, VideoKind, string[]][]>> = {
  classroom: [
    ["Why systems engineering? Systems thinking in a vehicle programme", ["LO1"], "discussion", 120, "none", ["M1.MO1"]],
    ["Life cycle models: V-model, ASPICE and agile", ["LO1"], "teaching", 120, "none", ["M2.MO1"]],
    ["From stakeholder needs to system requirements", ["LO2"], "worked", 120, "demo", ["M3.MO1"]],
    ["Requirements traceability in Polarion", ["LO2"], "lab", 120, "demo", ["M3.MO1"]],
    ["Functional architecture with SysML", ["LO3"], "teaching", 120, "demo", ["M4.MO1"]],
    ["Hazard analysis and ISO 26262 safety goals", ["LO5"], "failure", 120, "none", ["M7.MO1"]],
    ["Planning V&V for a BMS", ["LO4"], "case", 120, "none", ["M5.MO1", "M6.MO1"]],
    ["BMS trade study", ["LO6"], "project", 120, "none", ["M7.MO2", "M8.MO1"]],
  ],
  youtube: [
    ["Why a car has 100 million lines of code and who keeps it sane", ["LO1"], "dyk", 6, "explainroo", ["M1.MO1"]],
    ["The V-model in one drawing", ["LO1"], "teaching", 8, "whiteboard", ["M2.MO1"]],
    ["What a “good” requirement looks like", ["LO2"], "dyk", 7, "explainroo", ["M3.MO1"]],
    ["Tracing a requirement to a test in Polarion", ["LO2"], "worked", 9, "screen", ["M3.MO1"]],
  ],
};

// ---- Helpers -----------------------------------------------------------------

const capFirst = (s: string) => s.charAt(0).toUpperCase() + s.slice(1);
const lowerFirst = (s: string) => s.charAt(0).toLowerCase() + s.slice(1);
const stripDot = (s: string) => s.trim().replace(/\.$/, "");

function rewriteVerb(text: string, to: BloomLevel): string {
  const words = text.trim().split(" ");
  return [capFirst(BLOOM_VERBS[to][0]!), ...words.slice(1)].join(" ");
}

/** Split `total` minutes into integer parts by weight; parts are ≥ 1 and sum exactly to total. */
function split(total: number, weights: number[]): number[] {
  let ws = [...weights];
  while (ws.length > 1 && total < ws.length * 3) ws = ws.slice(0, -1);
  const sum = ws.reduce((a, b) => a + b, 0);
  const parts = ws.map((w) => Math.max(1, Math.round((total * w) / sum)));
  const diff = total - parts.reduce((a, b) => a + b, 0);
  parts[parts.length - 1]! += diff;
  while (parts.length > 1 && parts[parts.length - 1]! < 1) {
    const last = parts.pop()!;
    parts[parts.length - 1]! += last;
  }
  return parts;
}

/**
 * Session outcomes for a drafted session: one per module outcome it serves (named, or found through the session's LOs).
 * Without module outcomes, one per LO so the lesson still has measurable targets.
 */
function sessionOutcomesFor(course: Course, sessionId: string, loIds: string[], moIds: string[] | undefined, p: Provenance): SessionOutcome[] {
  const all = course.modules.flatMap((m) => m.outcomes);
  let mos = moIds ? all.filter((mo) => moIds.includes(mo.id)) : [];
  if (!mos.length) mos = all.filter((mo) => mo.outcomeIds.some((l) => loIds.includes(l)));
  const src = mos.length
    ? mos.map((mo) => ({ text: mo.text, bloom: mo.bloom, moduleOutcomeIds: [mo.id] }))
    : course.outcomes.filter((o) => loIds.includes(o.id)).map((o) => ({ text: o.text, bloom: o.bloom, moduleOutcomeIds: [] as string[] }));
  return src.map((x, i) => ({ id: `${sessionId}.SO${i + 1}`, ...x, locked: false, provenance: p }));
}

// ---- The mock --------------------------------------------------------------------

export const mockStages: Stages = {
  async parseInputs(files: InputFile[]) {
    await delay();
    const hasHandout = files.some((f) => f.meta.kind === "handout");
    const hasSheet = files.some((f) => f.meta.kind === "moduleSheet");
    const p = prov("inputs.parse", files.map((f) => f.meta.id));
    const modules: Module[] = MODULES.filter((m) => (hasHandout && m.src !== "excel") || (hasSheet && m.src !== "handout")).map((m) => ({
      id: m.id, title: m.title, hours: m.hours, topics: [],
      // A handout states module outcomes; a module sheet alone does not.
      outcomes: hasHandout ? (MOS[m.id] ?? []).map(([id, text, bloom, outcomeIds]) => ({ id, text, bloom, outcomeIds, locked: false, provenance: p })) : [],
      foundIn: hasHandout && hasSheet ? (m.src === "excel" ? "moduleSheet" : m.src === "handout" ? "handout" : "both") : hasHandout ? "handout" : "moduleSheet",
      note: hasHandout && hasSheet ? m.note : undefined,
    }));
    const objectives: Objective[] = hasHandout ? COS.map(([id, text]) => ({ id, text, locked: false, provenance: p })) : [];
    const value: ParsedInputs = {
      brief: {
        title: "AEZC517 Automotive Systems Engineering", code: "AEZC517", audience: "M.Tech WILP, working engineers", level: "pg",
        contactHours: 32, industry: "Automotive OEMs and Tier-1 suppliers", markets: ["India", "Germany"],
        ...(hasHandout ? { textbooks: ["Systems Engineering Handbook, INCOSE, 5th ed.", "Kossiakoff et al., Systems Engineering Principles and Practice"] } : {}),
      },
      modules, objectives, outcomes: [],
      gaps: hasHandout ? ["CO4, CO5 and LO4 are empty in the source"] : [],
    };
    return gen(value, p);
  },

  async findRoles(_brief, modules, keywords) {
    await delay();
    const kw = keywords?.length ? keywords : KEYWORDS;
    const roles: JobRole[] = ROLES.map(([id, title, postings, moduleMatch, experience, skills]) => ({
      id, title, postings, moduleMatch, experience, skills, evidence: [], selected: PRESELECTED.has(id), addedByUser: false,
    }));
    return gen({ keywords: kw, roles, postingsRead: 412 }, prov("roles.search", modules.map((m) => m.id)));
  },

  async proposeFit(course: Course) {
    await delay();
    const mods = new Set(course.modules.map((m) => m.id));
    const roleIds = new Set(course.roles.filter((r) => r.selected).map((r) => r.id));
    const changes: FitChange[] = FIT.map(([id, kind, text, reason, target, hoursDelta, roles, academicConflict]) => ({
      id, kind, text, reason, targetModuleId: mods.has(target) ? target : "new", hoursDelta,
      roleIds: roles.filter((r) => roleIds.has(r)), academicConflict, decision: "pending",
      provenance: prov("fit.propose", [...roleIds], course.structureVersion),
    }));
    return gen(changes, prov("fit.propose", [...roleIds], course.structureVersion));
  },

  async draftOutcomes(course: Course) {
    await delay();
    const p = prov("outcomes.draft", course.modules.map((m) => m.id), course.structureVersion);
    const modIds = new Set(course.modules.map((m) => m.id));
    const selected = new Set(course.roles.filter((r) => r.selected).map((r) => r.id));
    const firstMod = course.modules[0]?.id ?? "M1";
    const objectives: Objective[] = (course.objectives.length ? course.objectives.map(({ id, text }) => [id, text] as [string, string]) : COS)
      .map(([id, text]) => ({ id, text, locked: false, provenance: p }));
    const outcomes: Outcome[] = LOS.map(([id, text, bloom, moduleIds, roleIds, origin, objectiveIds]) => {
      const mids = moduleIds.filter((m) => modIds.has(m));
      return {
        id, text, bloom, moduleIds: mids.length ? mids : [firstMod], objectiveIds,
        roleIds: roleIds.filter((r) => selected.has(r)).length ? roleIds.filter((r) => selected.has(r)) : roleIds,
        origin, locked: false, provenance: p,
      };
    });
    return gen({ objectives, outcomes }, p);
  },

  async suggestOutcomeEdit(course: Course, outcomeId: string, ins: EditInstruction) {
    await delay();
    const o = course.outcomes.find((x) => x.id === outcomeId);
    const co = course.objectives.find((x) => x.id === outcomeId);
    const mo = course.modules.flatMap((m) => m.outcomes).find((x) => x.id === outcomeId);
    if (!o && !co && !mo) throw new Error(`No outcome, objective or module outcome ${outcomeId}`);
    const text = (o ?? mo ?? co)!.text;
    const bloom: BloomLevel = o?.bloom ?? mo?.bloom ?? "understand";
    const role = o ? course.roles.find((r) => o.roleIds.includes(r.id))?.title ?? "industry" : "industry";
    let value: OutcomeSuggestion;
    const one = (t: string, b: BloomLevel, reason: string): OutcomeSuggestion => ({ targetId: outcomeId, proposed: [{ text: t, bloom: b }], reason });
    switch (ins.kind) {
      case "raiseBloom": {
        const next = BLOOM_ORDER[Math.min(BLOOM_ORDER.indexOf(bloom) + 1, BLOOM_ORDER.length - 1)]!;
        value = one(rewriteVerb(text, next), next, `Raised from ${capFirst(bloom)} to ${capFirst(next)}.`);
        break;
      }
      case "measurable":
        value = one(`${stripDot(text)}, given a real programme document, scored against the session rubric.`, bloom, "Added a condition and a criterion so it can be assessed.");
        break;
      case "industryContext":
        value = one(`${stripDot(text)}, using templates and tools from an OEM or Tier-1 programme.`, bloom, `Linked to what ${role} postings ask for.`);
        break;
      case "shorten":
        value = one(`${stripDot(text.split(",")[0]!)}.`, bloom, "Cut to the core verb and object.");
        break;
      case "split": {
        const [head, ...rest] = text.split(",");
        const second = rest.join(",").trim();
        value = {
          targetId: outcomeId,
          proposed: [
            { text: `${stripDot(head!)}.`, bloom },
            { text: second ? `${capFirst(BLOOM_VERBS.apply[0]!)} ${lowerFirst(stripDot(second))}.` : "Apply this to the capstone system.", bloom: "apply" },
          ],
          reason: "Two outcomes, each assessable on its own.",
        };
        break;
      }
      case "matchHandout":
        value = one(text.replace("vehicle programme", "system").replace("automotive ", ""), bloom, "Aligned with the wording in the course handout.");
        break;
      default:
        value = one(`${stripDot(text)}${ins.note ? ` — revised for: ${ins.note}` : ""}.`, bloom, ins.note ? `Your instruction: “${ins.note}”` : "Rewritten.");
    }
    return gen(value, prov(`outcomes.edit.${ins.kind}`, [outcomeId]));
  },

  async draftPlan(course: Course, spec: PlanSpec) {
    await delay();
    const p = prov("plans.draft", course.outcomes.map((o) => o.id), course.structureVersion);
    const known = new Set(course.outcomes.map((o) => o.id));
    const allowed = VIDEO_BY_PATH[spec.path];
    const pickStyle = (bloom: BloomLevel, preset?: TeachingStyle): TeachingStyle =>
      spec.style === "auto" ? preset ?? AUTO_STYLE[bloom] : spec.style;
    const fam = PATH_FAMILY[spec.path];
    const preset = PRESET_SESSIONS[spec.path]?.filter(([, los]) => los.every((l) => known.has(l)));
    let sessions: Session[];
    if (preset?.length) {
      sessions = preset.map(([title, outcomeIds, st, minutes, v, moIds], i) => ({
        id: `s${i + 1}`, index: i + 1, title, outcomeIds, sessionOutcomes: sessionOutcomesFor(course, `s${i + 1}`, outcomeIds, moIds, p),
        style: spec.style === "auto" ? st : spec.style, minutes,
        video: allowed.includes(v) ? v : allowed[0]!, blocks: [], links: [], caseStudies: [], assets: [], stale: false, provenance: p,
      }));
    } else {
      sessions = course.outcomes.map((o, i) => ({
        id: `s${i + 1}`, index: i + 1, title: stripDot(o.text.split(",")[0]!), outcomeIds: [o.id],
        sessionOutcomes: sessionOutcomesFor(course, `s${i + 1}`, [o.id], undefined, p), style: pickStyle(o.bloom),
        minutes: fam === "content" ? 8 : spec.path === "micro" ? 5 : 60, video: allowed[0]!,
        blocks: [], links: [], caseStudies: [], assets: [], stale: false, provenance: p,
      }));
    }
    const plan: LearningPlan = {
      id: `p-${Date.now().toString(36)}${Math.random().toString(36).slice(2, 6)}`,
      name: spec.name ?? `New ${spec.path} plan${spec.audienceVariant ? ` (${spec.audienceVariant})` : ""}`,
      path: spec.path, defaultStyle: spec.style, audienceVariant: spec.audienceVariant, sessions, provenance: p,
    };
    return gen(plan, p);
  },

  async draftHourPlan(course: Course, planId: string, sessionId: string) {
    await delay();
    const { session } = findSession(course, planId, sessionId);
    const p = prov("build.hourPlan", session.outcomeIds, course.structureVersion);
    const hours = Math.ceil(session.minutes / 60);
    const blocks: HourBlock[] = [];
    // The opening block and the teaching/case blocks serve every SO; the rest take turns; wrap-ups and breaks serve none.
    const soIds = session.sessionOutcomes.map((so) => so.id);
    const servedBy = (kind: HourBlock["kind"], first: boolean, i: number): string[] =>
      kind === "wrap" || kind === "break" ? [] : first || kind === "teach" || kind === "case" ? soIds : soIds.length ? [soIds[i % soIds.length]!] : [];
    const example = {
      text: `How an OEM BMS team handles “${session.title}” on a live programme, with the templates they use.`,
      sector: "automotive", roleIds: course.roles.filter((r) => r.selected).map((r) => r.id).slice(0, 2),
      sources: [{ title: "INCOSE Systems Engineering Handbook", url: "https://www.incose.org/publications/se-handbook" }],
    };
    for (let h = 1; h <= hours; h++) {
      const len = h < hours ? 60 : session.minutes - 60 * (hours - 1);
      const plan: [HourBlock["kind"], string, string, number][] = h === 1
        ? [["hook", "Hook", "Open with a question or surprising fact tied to the session.", 1], ["teach", "Core idea", "Explain the concept with one worked example.", 3], ["activity", "Apply it", "Pairs apply the idea to the capstone BMS.", 2], ["check", "Quick check", "Three questions, answers discussed.", 1]]
        : [["case", "Industry case", "Read and discuss a short programme case.", 2], ["activity", "Practice", "Small groups extend the capstone artefact.", 2], ["check", "Quick check", "Exit questions.", 1], ["wrap", "Wrap-up", "Summary and link to the next session.", 1]];
      const mins = split(len, plan.map((x) => x[3]));
      let start = 0;
      mins.forEach((m, i) => {
        const [kind, title, activity] = plan[i]!;
        blocks.push({
          id: `${session.id}-h${h}-b${i + 1}`, hour: h, startMin: start, minutes: m, kind, title: `${title}: ${session.title}`.slice(0, 120),
          activity, outcomeIds: session.outcomeIds, sessionOutcomeIds: servedBy(kind, blocks.length === 0, i), style: session.style,
          industryExample: kind === "teach" || kind === "case" ? example : undefined,
          check: kind === "check" ? [`What is the key idea of “${session.title}”?`, "Where would you see this on a vehicle programme?", "What would go wrong if it were skipped?"] : [],
          needsSlides: kind === "teach", provenance: p,
        });
        start += m;
      });
    }
    return gen(blocks, p);
  },

  async findFurtherLearning(course: Course, planId: string, sessionId: string) {
    await delay();
    const { session } = findSession(course, planId, sessionId);
    const q = encodeURIComponent(session.title);
    const links: FurtherLink[] = [
      { id: `${session.id}-l1`, kind: "youtube", title: `Search: ${session.title}`, url: `https://www.youtube.com/results?search_query=${q}`, channelOrSite: "YouTube", why: "Short talks and demos to watch before the session.", approved: false, alive: true },
      { id: `${session.id}-l2`, kind: "article", title: "INCOSE Systems Engineering Handbook", url: "https://www.incose.org/publications/se-handbook", channelOrSite: "incose.org", why: "The reference for the processes taught in this course.", approved: false, alive: true },
      { id: `${session.id}-l3`, kind: "standard", title: "ISO 26262-3:2018 Concept phase", url: "https://www.iso.org/standard/68385.html", channelOrSite: "iso.org", why: "The hazard analysis and safety goal clauses.", approved: false, alive: true },
    ];
    return gen(links, prov("build.links", session.outcomeIds));
  },

  async draftCaseStudy(course: Course, planId: string, sessionId: string, label: CaseStudy["label"]) {
    await delay();
    const { session } = findSession(course, planId, sessionId);
    const p = prov("build.caseStudy", session.outcomeIds, course.structureVersion);
    const cs: CaseStudy = {
      id: `${session.id}-cs-${Date.now().toString(36)}`, label,
      title: label === "real" ? "Thermal runaway recalls and the requirements behind them" : "VoltDrive’s missed BMS derating requirement",
      background: label === "real"
        ? "Several EV makers have recalled vehicles over battery fire risk. Public recall notices describe the defect and the remedy, which lets learners trace each one back to a requirement that was missing or unverified."
        : "VoltDrive (a composite Tier-1 supplier) shipped a BMS whose thermal derating started 8 °C too late. The requirement existed but was never linked to a HIL test.",
      data: "| Item | Value |\n|---|---|\n| Cells | 96s2p |\n| Derating start (spec) | 45 °C |\n| Derating start (built) | 53 °C |",
      questions: ["Which requirement failed, and at which V-model level should it have been caught?", "Write the missing verification case.", "Who in the programme should have owned the trace?"],
      teachingNote: "Run as a 20-minute group exercise; steer learners from blaming the test team to the missing trace link.",
      sources: label === "real" ? [{ title: "NHTSA recalls search", url: "https://www.nhtsa.gov/recalls" }] : [],
      outcomeIds: session.outcomeIds, provenance: p,
    };
    return gen(cs, p);
  },
};
