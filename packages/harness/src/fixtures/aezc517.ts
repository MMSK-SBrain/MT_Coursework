// AEZC517 Systems Engineering sample data, taken from the prototype the user approved
// (coursesmith.html). Used by MockStages, the fixture sources, the inline worked example and tests.
import {
  Course as CourseSchema,
  type Course, type CourseBrief, type FitChange, type HourBlock, type JobPosting, type JobRole, type Module,
  type Objective, type Outcome, type Provenance, type VideoCandidate,
} from "@cg/core";

export const FIXTURE_TIME = "2026-11-04T00:00:00.000Z";

export const fixtureProv = (promptId: string, builtFrom: string[] = []): Provenance => ({
  model: "fixture", promptId, promptVersion: "0", costUsd: 0, createdAt: FIXTURE_TIME, builtFrom,
});

export const BRIEF: CourseBrief = {
  title: "Systems Engineering",
  code: "AEZC517",
  audience: "M.Tech WILP, working engineers",
  level: "pg",
  contactHours: 32,
  industry: "Automotive OEMs and Tier-1 suppliers",
  markets: ["India", "Germany"],
  textbooks: ["INCOSE Systems Engineering Handbook, 5th ed.", "Kossiakoff et al., Systems Engineering Principles and Practice"],
  notes: "16 sessions of 2 hours.",
};

export const MODULES: Module[] = [
  { id: "M1", title: "Systems thinking and the role of the systems engineer", hours: 4, topics: ["systems thinking", "soft skills"], foundIn: "both" },
  { id: "M2", title: "Life cycle models: V-model, agile and hybrids", hours: 4, topics: ["V-model", "agile", "ASPICE"], foundIn: "both" },
  { id: "M3", title: "Stakeholder needs and requirements engineering", hours: 6, topics: ["stakeholder analysis", "requirements", "traceability"], foundIn: "both" },
  { id: "M4", title: "Functional and physical architecture, MBSE with SysML", hours: 6, topics: ["SysML", "MBSE"], foundIn: "moduleSheet", note: "Not in handout" },
  { id: "M5", title: "Interface management and system integration", hours: 4, topics: ["interfaces", "integration"], foundIn: "both" },
  { id: "M6", title: "Verification and validation", hours: 4, topics: ["V&V", "HIL", "SIL"], foundIn: "both" },
  { id: "M7", title: "Technical management: risk, configuration, trade studies", hours: 4, topics: ["risk", "configuration", "trade study"], foundIn: "handout", note: "Not in sheet" },
  { id: "M8", title: "Capstone: EV battery management system", hours: 4, topics: ["BMS"], foundIn: "moduleSheet" },
];

export const KEYWORDS = [
  "systems engineering", "requirements engineering", "V-model", "SysML / MBSE", "interface management",
  "verification and validation", "HIL / SIL", "DFMEA", "trade study", "battery management system",
];

const role = (id: string, title: string, postings: number, moduleMatch: number, experience: string, skills: string[], selected: boolean): JobRole => ({
  id, title, postings, moduleMatch, experience, skills, selected, addedByUser: false,
  evidence: [{ title: `${title} (sample posting)`, url: `https://jobs.example.org/aezc517/${id}-1`, source: "fixture" }],
});

export const ROLES: JobRole[] = [
  role("r1", "Automotive Systems Engineer", 312, 86, "2–8 yrs", ["Requirements", "V-model", "System architecture"], true),
  role("r2", "Requirements Engineer", 247, 81, "1–6 yrs", ["Polarion / DOORS", "Traceability", "ASPICE SYS.2"], true),
  role("r3", "Functional Safety Engineer (ISO 26262)", 241, 58, "3–10 yrs", ["HARA", "Safety goals", "FMEA / FTA"], true),
  role("r4", "MBSE / SysML Architect", 133, 74, "5–12 yrs", ["SysML", "Cameo / Capella", "Variant modelling"], false),
  role("r5", "V&V Engineer (HIL / SIL)", 198, 69, "1–6 yrs", ["Test planning", "dSPACE / NI HIL", "Test automation"], false),
  role("r6", "BMS Systems Engineer", 176, 72, "2–8 yrs", ["SOC / SOH", "Cell monitoring", "Thermal limits"], true),
  role("r7", "ECU Integration Engineer", 119, 63, "1–5 yrs", ["CAN / UDS", "Integration testing", "Flashing"], false),
  role("r8", "ADAS Systems Engineer", 204, 55, "2–8 yrs", ["SOTIF", "Sensor fusion", "Scenario testing"], false),
  role("r9", "ASPICE Process Consultant", 88, 52, "6–15 yrs", ["ASPICE assessments", "Process improvement"], false),
  role("r10", "Automotive Cybersecurity Engineer", 109, 29, "3–8 yrs", ["ISO/SAE 21434", "TARA"], false),
  role("r11", "Product Owner, Vehicle Software", 142, 41, "5–12 yrs", ["Backlog", "SAFe", "Stakeholder management"], false),
  role("r12", "NPD Programme Engineer", 160, 38, "3–10 yrs", ["Gateways", "APQP", "Risk tracking"], false),
];

/** Two synthetic postings per role, deterministic. */
export const POSTINGS: JobPosting[] = ROLES.flatMap((r, i) => [0, 1].map((k): JobPosting => ({
  title: r.title,
  location: BRIEF.markets[(i + k) % BRIEF.markets.length]!,
  postedAt: `2026-10-${String(10 + ((i * 2 + k) % 18)).padStart(2, "0")}`,
  skills: r.skills,
  description: `${r.title} (${r.experience}). Work on vehicle programmes with ${r.skills.join(", ")}. Sample posting for tests and dev.`,
  url: `https://jobs.example.org/aezc517/${r.id}-${k + 1}`,
  source: "fixture",
})));

const fit = (id: string, kind: FitChange["kind"], text: string, reason: string, targetModuleId: string, hoursDelta: number, roleIds: string[], academicConflict?: string): FitChange => ({
  id, kind, text, reason, targetModuleId, hoursDelta, roleIds, decision: "pending",
  ...(academicConflict ? { academicConflict } : {}),
  provenance: fixtureProv("fit.propose", roleIds),
});

export const FIT: FitChange[] = [
  fit("f1", "add", "Hazard analysis (HARA) and safety goals under ISO 26262", "Asked for by 3 of 4 selected roles · 241 postings", "M7", 2, ["r1", "r3", "r6"]),
  fit("f2", "add", "ASPICE SYS.1–SYS.5 work products and how assessors read them", "Requirements Engineer, Systems Engineer · 188 postings", "M2", 1, ["r1", "r2"]),
  fit("f3", "strengthen", "Hands-on requirements tool lab (Polarion or DOORS)", "M3 is theory only; tools named in 64% of Requirements Engineer postings", "M3", 2, ["r2"]),
  fit("f4", "add", "BMS requirements: cell monitoring, SOC/SOH, thermal derating", "BMS Systems Engineer · 176 postings", "M8", 2, ["r6"]),
  fit("f5", "strengthen", "HIL test-case design from requirements", "Systems Engineer, BMS Systems Engineer", "M6", 1, ["r1", "r6"]),
  fit("f6", "trim", "Soft-skills content in M1 (4 h → 2 h)", "Rarely asked for by the selected roles. Kept by default: CO1 in the handout requires it.", "M1", -2, ["r1", "r2", "r3", "r6"], "CO1 requires soft skills"),
];

export const OBJECTIVES: Objective[] = [
  { id: "CO1", text: "Build the hard and soft skills an automotive systems engineer needs on a cross-functional programme.", locked: false, provenance: fixtureProv("outcomes.draft") },
  { id: "CO2", text: "Explain systems engineering principles, processes and methods as defined by INCOSE and ISO/IEC/IEEE 15288.", locked: false, provenance: fixtureProv("outcomes.draft") },
  { id: "CO3", text: "Apply systems engineering methods to a complex automotive development, from stakeholder needs to a validated system.", locked: false, provenance: fixtureProv("outcomes.draft") },
];

const lo = (id: string, text: string, bloom: Outcome["bloom"], moduleIds: string[], objectiveIds: string[], roleIds: string[], origin: Outcome["origin"]): Outcome => ({
  id, text, bloom, moduleIds, objectiveIds, roleIds, origin, locked: false, provenance: fixtureProv("outcomes.draft", [...moduleIds, ...roleIds]),
});

export const OUTCOMES: Outcome[] = [
  lo("LO1", "Describe the processes, methods and practices of systems engineering across a vehicle programme life cycle.", "understand", ["M1", "M2"], ["CO1", "CO2"], ["r1"], "handout"),
  lo("LO2", "Write verifiable system requirements with full traceability from stakeholder needs, using a requirements tool.", "apply", ["M3"], ["CO3"], ["r2"], "fit"),
  lo("LO3", "Model the functional and physical architecture of an automotive subsystem in SysML.", "apply", ["M4"], ["CO3"], ["r1"], "new"),
  lo("LO4", "Plan verification and validation for a subsystem, choosing between SIL, HIL and vehicle-level tests.", "analyse", ["M5", "M6"], ["CO3"], ["r6"], "handout"),
  lo("LO5", "Perform a hazard analysis and derive safety goals following ISO 26262 Part 3.", "apply", ["M7"], ["CO3"], ["r3"], "fit"),
  lo("LO6", "Evaluate design alternatives for an EV battery management system with a structured trade study.", "evaluate", ["M7", "M8"], ["CO3"], ["r6"], "handout"),
];

export const CLASSROOM_SESSIONS: { title: string; outcomeIds: string[]; style: Course["plans"][number]["sessions"][number]["style"]; minutes: number; video: "none" | "demo" }[] = [
  { title: "Why systems engineering? Systems thinking in a vehicle programme", outcomeIds: ["LO1"], style: "discussion", minutes: 120, video: "none" },
  { title: "Life cycle models: V-model, ASPICE and agile", outcomeIds: ["LO1"], style: "teaching", minutes: 120, video: "none" },
  { title: "From stakeholder needs to system requirements", outcomeIds: ["LO2"], style: "worked", minutes: 120, video: "demo" },
  { title: "Requirements traceability in Polarion", outcomeIds: ["LO2"], style: "lab", minutes: 120, video: "demo" },
  { title: "Functional architecture with SysML", outcomeIds: ["LO3"], style: "teaching", minutes: 120, video: "demo" },
  { title: "Hazard analysis and ISO 26262 safety goals", outcomeIds: ["LO5"], style: "failure", minutes: 120, video: "none" },
  { title: "Planning V&V for a BMS", outcomeIds: ["LO4"], style: "case", minutes: 120, video: "none" },
  { title: "BMS trade study", outcomeIds: ["LO6"], style: "project", minutes: 120, video: "none" },
];

export const YOUTUBE_SESSIONS = [
  { title: "Why a car has 100 million lines of code and who keeps it sane", outcomeIds: ["LO1"], style: "dyk" as const, minutes: 6, video: "explainroo" as const },
  { title: "The V-model in one drawing", outcomeIds: ["LO1"], style: "teaching" as const, minutes: 8, video: "whiteboard" as const },
  { title: "What a “good” requirement looks like", outcomeIds: ["LO2"], style: "dyk" as const, minutes: 7, video: "explainroo" as const },
  { title: "Tracing a requirement to a test in Polarion", outcomeIds: ["LO2"], style: "worked" as const, minutes: 9, video: "screen" as const },
];

export const VIDEOS: VideoCandidate[] = [
  { title: "The V-model explained for automotive engineers", url: "https://www.youtube.com/watch?v=fixture-vmodel", channel: "Fixture Channel", durationSec: 540, publishedAt: "2025-03-01T00:00:00Z", description: "Left side, right side, and why every requirement needs a test." },
  { title: "Writing good requirements: INCOSE rules in practice", url: "https://www.youtube.com/watch?v=fixture-reqs", channel: "Fixture Channel", durationSec: 780, publishedAt: "2024-11-12T00:00:00Z", description: "Ambiguity, verifiability and traceability with examples." },
  { title: "SysML block definition diagrams in 10 minutes", url: "https://www.youtube.com/watch?v=fixture-sysml", channel: "Fixture Channel", durationSec: 600, publishedAt: "2025-06-20T00:00:00Z", description: "Blocks, parts and ports for a simple subsystem." },
  { title: "HIL testing a battery management system", url: "https://www.youtube.com/watch?v=fixture-hil", channel: "Fixture Channel", durationSec: 1020, publishedAt: "2025-01-15T00:00:00Z", description: "Bench set-up, fault injection and test reports." },
  { title: "ISO 26262 HARA walk-through", url: "https://www.youtube.com/watch?v=fixture-hara", channel: "Fixture Channel", durationSec: 900, publishedAt: "2024-09-02T00:00:00Z", description: "Hazards, ASIL determination and safety goals." },
];

export const PAGES: { title: string; url: string; snippet: string }[] = [
  { title: "INCOSE: What is systems engineering?", url: "https://www.incose.org/about-systems-engineering", snippet: "An interdisciplinary approach to enable the realisation of successful systems." },
  { title: "Guide to writing requirements (fixture)", url: "https://docs.example.org/se/writing-requirements", snippet: "Characteristics of well-formed requirements and sets of requirements." },
  { title: "Trade study method (fixture)", url: "https://docs.example.org/se/trade-studies", snippet: "Criteria, weights, sensitivity analysis and how to present a recommendation." },
];

/** Hand-written hour plan for session s3 ("From stakeholder needs to system requirements", 120 min). */
export const S3_BLOCKS: Omit<HourBlock, "id" | "provenance">[] = [
  { hour: 1, startMin: 0, minutes: 10, kind: "hook", title: "The pack that must never overheat", activity: "Show the stakeholder need \"The battery shall not overheat\". Ask pairs: how would you test this? Collect answers on the board.", outcomeIds: ["LO2"], style: "worked", check: [], needsSlides: true },
  { hour: 1, startMin: 10, minutes: 25, kind: "teach", title: "From needs to verifiable requirements", activity: "Walk through stakeholder needs -> system requirements -> subsystem requirements for a BMS. Introduce the properties of a good requirement: necessary, unambiguous, verifiable, traceable.", outcomeIds: ["LO2"], style: "worked", check: [], needsSlides: true,
    industryExample: { text: "Requirements Engineer postings ask for traceability in Polarion or DOORS and ASPICE SYS.2 work products; show how one BMS need becomes three traced system requirements.", sector: "automotive", roleIds: ["r2"], sources: [{ title: "Requirements Engineer (sample posting)", url: "https://jobs.example.org/aezc517/r2-1" }] } },
  { hour: 1, startMin: 35, minutes: 25, kind: "activity", title: "Rewrite five bad requirements", activity: "Groups of three get five flawed BMS requirements and rewrite each to be verifiable, naming the test that would verify it. Two groups present.", outcomeIds: ["LO2"], style: "worked", check: [], needsSlides: false },
  { hour: 2, startMin: 0, minutes: 10, kind: "break", title: "Break", activity: "Break.", outcomeIds: [], style: "worked", check: [], needsSlides: false },
  { hour: 2, startMin: 10, minutes: 30, kind: "activity", title: "Trace a need to a test", activity: "Each group takes one stakeholder need, derives two system requirements, and links each to a test case in a shared traceability table.", outcomeIds: ["LO2"], style: "worked", check: [], needsSlides: false },
  { hour: 2, startMin: 40, minutes: 10, kind: "check", title: "Quick check", activity: "Three-question quiz on requirement quality, answered on cards.", outcomeIds: ["LO2"], style: "retrieval", check: ["Which word makes \"The BMS shall respond quickly\" unverifiable?", "What links a system requirement to its stakeholder need?", "Name one test method for a thermal derating requirement."], needsSlides: false },
  { hour: 2, startMin: 50, minutes: 10, kind: "wrap", title: "Wrap and bridge to the tool lab", activity: "Summarise the three rules for a verifiable requirement; preview next session's Polarion lab.", outcomeIds: ["LO2"], style: "worked", check: ["What will you check first in a requirement you review at work?"], needsSlides: false },
];

/** A complete AEZC517 course, outcomes frozen, with one classroom plan (session s3 has an hour plan). */
export function aezc517Course(): Course {
  return CourseSchema.parse({
    id: "aezc517",
    slug: "aezc517-systems-engineering",
    brief: BRIEF,
    modules: MODULES,
    structureVersion: 2,
    structureConfirmedAt: FIXTURE_TIME,
    roles: ROLES,
    fit: FIT.map((f) => ({ ...f, decision: f.id === "f6" ? "rejected" : "accepted" })),
    objectives: OBJECTIVES,
    outcomes: OUTCOMES.map((o) => ({ ...o, locked: true })),
    outcomesFrozenAt: FIXTURE_TIME,
    plans: [{
      id: "p1",
      name: "BITS WILP classroom",
      path: "classroom",
      defaultStyle: "teaching",
      sessions: CLASSROOM_SESSIONS.map((s, i) => ({
        id: `s${i + 1}`, index: i + 1, ...s,
        blocks: i === 2 ? S3_BLOCKS.map((b, n) => ({ ...b, id: `s3-b${n + 1}`, provenance: fixtureProv("session.hourPlan", ["LO2"]) })) : [],
        links: [], caseStudies: [], assets: [], stale: false,
        provenance: fixtureProv("plan.draft", s.outcomeIds),
      })),
      provenance: fixtureProv("plan.draft", OUTCOMES.map((o) => o.id)),
    }],
    createdAt: FIXTURE_TIME,
    updatedAt: FIXTURE_TIME,
  });
}
