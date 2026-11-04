// A small, schema-valid sample course based on AEZC517 Systems Engineering (from the approved prototype).
import { Course } from "@cg/core";

const prov = (promptId: string, builtFrom: string[] = []) => ({
  model: "fixture", promptId, promptVersion: "1", costUsd: 0, createdAt: "2026-11-04T09:00:00Z", builtFrom,
});

const raw = {
  id: "c-aezc517",
  slug: "aezc517-systems-engineering",
  brief: {
    title: "Systems Engineering",
    code: "AEZC517",
    audience: "M.Tech WILP, working automotive engineers",
    level: "pg",
    contactHours: 36,
    industry: "Automotive OEMs and Tier-1 suppliers",
    markets: ["India", "Germany"],
    textbooks: ["INCOSE Systems Engineering Handbook, 5th ed."],
    notes: "Includes an EV battery management system capstone.",
  },
  modules: [
    { id: "M1", title: "Systems thinking and the role of the systems engineer", hours: 4, topics: ["System boundaries", "Stakeholders"], outcomes: [{ id: "M1.MO1", text: "Explain system boundaries and stakeholders for a vehicle programme.", bloom: "understand", outcomeIds: ["LO1"], provenance: prov("outcomes.draft") }], foundIn: "both" },
    { id: "M2", title: "Life cycle models: V-model, agile and hybrids", hours: 4, topics: ["V-model", "ASPICE overview"], outcomes: [{ id: "M2.MO1", text: "Describe how the V-model and agile hybrids organise a programme life cycle.", bloom: "understand", outcomeIds: ["LO1"], provenance: prov("outcomes.draft") }], foundIn: "both" },
    { id: "M3", title: "Stakeholder needs and requirements engineering", hours: 6, topics: ["Needs", "Verifiable requirements", "Traceability"], outcomes: [{ id: "M3.MO1", text: "Write verifiable requirements from stakeholder needs.", bloom: "apply", outcomeIds: ["LO2"], provenance: prov("outcomes.draft") }, { id: "M3.MO2", text: "Explain why bidirectional traceability matters in an audit.", bloom: "understand", outcomeIds: ["LO2"], provenance: prov("outcomes.draft") }], foundIn: "both" },
    { id: "M4", title: "Functional and physical architecture, MBSE with SysML", hours: 6, topics: ["SysML blocks", "Allocation"], outcomes: [{ id: "M4.MO1", text: "Model a subsystem architecture in SysML.", bloom: "apply", outcomeIds: ["LO3"], provenance: prov("outcomes.draft") }], foundIn: "moduleSheet", note: "Not in handout" },
    { id: "M8", title: "Capstone: EV battery management system", hours: 4, topics: ["BMS requirements"], foundIn: "moduleSheet" },
  ],
  structureVersion: 1,
  structureConfirmedAt: "2026-11-04T09:10:00Z",
  roles: [
    { id: "r1", title: "Automotive Systems Engineer", skills: ["Requirements", "V-model", "System architecture"], matchedSkills: ["Requirements", "V-model", "System architecture"].slice(0, 2), moduleMatch: 86, selected: true, evidence: [{ title: "ESCO occupation", url: "https://esco.ec.europa.eu/en/classification/occupation_main", source: "esco" }] },
    { id: "r2", title: "Requirements Engineer", skills: ["Polarion / DOORS", "Traceability", "ASPICE SYS.2"], matchedSkills: ["Polarion / DOORS", "Traceability", "ASPICE SYS.2"].slice(0, 2), moduleMatch: 81, selected: true, evidence: [{ title: "ESCO occupation", url: "https://esco.ec.europa.eu/en/classification/occupation_main", source: "esco" }] },
    { id: "r6", title: "BMS Systems Engineer", skills: ["SOC / SOH", "Cell monitoring", "Thermal limits"], matchedSkills: ["SOC / SOH", "Cell monitoring", "Thermal limits"].slice(0, 2), moduleMatch: 72, selected: true, evidence: [{ title: "ESCO occupation", url: "https://esco.ec.europa.eu/en/classification/occupation_main", source: "esco" }] },
    { id: "r10", title: "Automotive Cybersecurity Engineer", skills: ["ISO/SAE 21434", "TARA"], matchedSkills: ["ISO/SAE 21434", "TARA"].slice(0, 2), moduleMatch: 29, selected: false, evidence: [{ title: "ESCO occupation", url: "https://esco.ec.europa.eu/en/classification/occupation_main", source: "esco" }] },
  ],
  fit: [
    { id: "f3", kind: "strengthen", text: "Hands-on requirements tool lab (Polarion or DOORS)", reason: "M3 is theory only; requirements tools are essential for Requirements Engineers.", targetModuleId: "M3", hoursDelta: 2, roleIds: ["r2"], decision: "accepted", provenance: prov("fit.propose") },
    { id: "f4", kind: "add", text: "BMS requirements: cell monitoring, SOC/SOH, thermal derating", reason: "BMS Systems Engineer: cell monitoring is an essential skill.", targetModuleId: "M8", hoursDelta: 2, roleIds: ["r6"], decision: "changed", provenance: prov("fit.propose") },
    { id: "f6", kind: "trim", text: "Soft-skills content in M1 (4 h to 2 h)", reason: "Kept by default: CO1 in the handout requires it.", targetModuleId: "M1", hoursDelta: -2, roleIds: [], academicConflict: "CO1 requires soft skills", decision: "rejected", provenance: prov("fit.propose") },
  ],
  objectives: [
    { id: "CO1", text: "Build the hard and soft skills an automotive systems engineer needs on a cross-functional programme.", locked: true, provenance: prov("outcomes.draft") },
    { id: "CO2", text: "Explain systems engineering principles, processes and methods as defined by INCOSE and ISO/IEC/IEEE 15288.", provenance: prov("outcomes.draft") },
    { id: "CO3", text: "Apply systems engineering methods to a complex automotive development, from stakeholder needs to a validated system.", provenance: prov("outcomes.draft") },
  ],
  outcomes: [
    { id: "LO1", text: "Describe the processes, methods and practices of systems engineering across a vehicle programme life cycle.", bloom: "understand", moduleIds: ["M1", "M2"], objectiveIds: ["CO2"], roleIds: ["r1"], origin: "handout", provenance: prov("outcomes.draft") },
    { id: "LO2", text: "Write verifiable system requirements with full traceability from stakeholder needs, using a requirements tool.", bloom: "apply", moduleIds: ["M3"], objectiveIds: ["CO3"], roleIds: ["r2"], origin: "fit", provenance: prov("outcomes.draft") },
    { id: "LO3", text: "Model the functional and physical architecture of an automotive subsystem in SysML.", bloom: "apply", moduleIds: ["M4"], objectiveIds: ["CO3"], roleIds: ["r1"], origin: "new", provenance: prov("outcomes.draft") },
  ],
  outcomesFrozenAt: "2026-11-04T09:30:00Z",
  plans: [
    {
      id: "p1",
      name: "Classroom, 3 h sessions",
      path: "classroom",
      defaultStyle: "teaching",
      provenance: prov("plan.draft"),
      sessions: [
        {
          id: "s3",
          index: 3,
          title: "Writing verifiable requirements",
          outcomeIds: ["LO2"],
          sessionOutcomes: [
            { id: "S3.SO1", text: "Rewrite a weak requirement so it passes the five checks.", bloom: "apply", moduleOutcomeIds: ["M3.MO1"], provenance: prov("session.outcomes") },
            { id: "S3.SO2", text: "Trace a requirement to its stakeholder need and a test case in a tool.", bloom: "apply", moduleOutcomeIds: ["M3.MO1", "M3.MO2"], provenance: prov("session.outcomes") },
          ],
          style: "worked",
          minutes: 120,
          video: "none",
          provenance: prov("plan.draft"),
          blocks: [
            { id: "b1", sessionOutcomeIds: ["S3.SO1"], hour: 1, startMin: 0, minutes: 10, kind: "hook", title: "A pack that must never fail", activity: "Show the headline requirement 'The pack shall not overheat'. Ask pairs what could go wrong when two teams read it differently. Collect three answers on the board.", outcomeIds: ["LO2"], style: "dyk", needsSlides: true, check: [], provenance: prov("hour.draft") },
            { id: "b2", sessionOutcomeIds: ["S3.SO1"], hour: 1, startMin: 10, minutes: 35, kind: "teach", title: "Anatomy of a good requirement", activity: "Introduce the five checks: necessary, unambiguous, verifiable, singular, traceable. Work one bad requirement into a good one on the board. Link the rewritten requirement to its stakeholder need to show traceability.", outcomeIds: ["LO2"], style: "worked", needsSlides: true, industryExample: { text: "A Tier-1 supplier reworked the vague requirement 'fast charging shall be supported' into three verifiable requirements, each with a test limit agreed with the OEM, and later used the same trace to settle a warranty dispute.", sector: "automotive", roleIds: ["r2"], sources: [{ title: "INCOSE Guide to Writing Requirements", url: "https://www.incose.org/products-and-publications/se-handbook" }] }, check: ["Which of the five checks does 'the system shall be user friendly' fail?"], provenance: prov("hour.draft") },
            { id: "b3", sessionOutcomeIds: ["S3.SO1"], hour: 1, startMin: 45, minutes: 15, kind: "activity", title: "Rewrite in pairs", activity: "Pairs receive four weak BMS requirements and rewrite them. Each pair swaps with another pair for a quick review against the five checks.", outcomeIds: ["LO2"], style: "challenge", needsSlides: false, check: [], provenance: prov("hour.draft") },
            { id: "b4", sessionOutcomeIds: ["S3.SO2"], hour: 2, startMin: 0, minutes: 40, kind: "activity", title: "Tool lab: trace a requirement", activity: "In Polarion (or the open-source alternative), create two requirements, link them to a stakeholder need and a test case, then run the traceability report. Instructor circulates and fixes broken links.", outcomeIds: ["LO2"], style: "lab", needsSlides: true, check: [], provenance: prov("hour.draft") },
            { id: "b5", sessionOutcomeIds: ["S3.SO1", "S3.SO2"], hour: 2, startMin: 40, minutes: 10, kind: "check", title: "Exit quiz", activity: "Three-question poll on requirement quality. Review wrong answers as a group.", outcomeIds: ["LO2"], style: "retrieval", needsSlides: false, check: ["Rewrite: 'The BMS shall respond quickly to over-temperature.'", "What does bidirectional traceability let an auditor do?"], provenance: prov("hour.draft") },
            { id: "b6", sessionOutcomeIds: ["S3.SO1", "S3.SO2"], hour: 2, startMin: 50, minutes: 10, kind: "wrap", title: "Recap and next session", activity: "Learners state the three rules for a verifiable requirement in their own words. Preview architecture modelling in the next session.", outcomeIds: ["LO2"], style: "teaching", needsSlides: true, check: [], provenance: prov("hour.draft") },
          ],
          links: [
            { id: "l1", kind: "youtube", title: "Writing good requirements in 10 minutes", url: "https://www.youtube.com/watch?v=example1", channelOrSite: "SE Basics", durationSec: 600, why: "A short walk-through of the five checks with examples.", approved: true },
            { id: "l2", kind: "article", title: "ASPICE SYS.2 explained", url: "https://example.com/aspice-sys2", channelOrSite: "example.com", why: "Shows how assessors read requirement work products.", approved: false },
          ],
          caseStudies: [
            { id: "cs1", label: "composite", title: "The ambiguous derating requirement", background: "Two teams implement 'thermal derating shall begin at high temperature' differently, and a field issue results.", data: "| Team | Threshold |\n| --- | --- |\n| Hardware | 55 C |\n| Software | 60 C |", questions: ["Which check failed?", "Rewrite the requirement."], teachingNote: "Steer learners to the missing number and unit.", sources: [], outcomeIds: ["LO2"], provenance: prov("case.draft") },
          ],
        },
        {
          id: "s4",
          index: 4,
          title: "Architecture with SysML",
          outcomeIds: ["LO3"],
          sessionOutcomes: [{ id: "S4.SO1", text: "Draw a block definition diagram of a BMS and allocate functions to blocks.", bloom: "apply", moduleOutcomeIds: ["M4.MO1"], provenance: prov("session.outcomes") }],
          style: "teaching",
          minutes: 120,
          provenance: prov("plan.draft"),
        },
      ],
    },
  ],
  createdAt: "2026-11-04T08:00:00Z",
  updatedAt: "2026-11-04T09:45:00Z",
};

export const sampleCourse: Course = Course.parse(raw);
export const SAMPLE_PLAN_ID = "p1";
export const SAMPLE_SESSION_ID = "s3";
