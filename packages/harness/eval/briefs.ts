// Fixed test set for the eval CLI: course briefs with the facts each stage needs (modules,
// selected roles, frozen outcomes, one plan). Re-run the eval whenever a prompt changes.
import { Course as CourseSchema, type BloomLevel, type Course, type CourseBrief } from "@cg/core";
import { aezc517Course } from "../src/fixtures/aezc517.js";
import { deriveModuleOutcomes, deriveSessionOutcomes } from "../src/hierarchy.js";

const T = "2026-11-04T00:00:00.000Z";
const prov = (promptId: string) => ({ model: "eval-seed", promptId, promptVersion: "0", costUsd: 0, createdAt: T, builtFrom: [] });

interface Seed {
  id: string;
  brief: CourseBrief;
  modules: [title: string, hours: number][];
  roles: [title: string, skills: string[]][];
  outcomes: [text: string, bloom: BloomLevel, moduleIdx: number[]][];
}

function build(s: Seed): Course {
  const roles = s.roles.map(([title, skills], i) => ({
    id: `r${i + 1}`, title, skills, matchedSkills: skills.slice(0, 1), moduleMatch: Math.round(100 / skills.length), selected: true,
    evidence: [{ title: `${title} (eval seed occupation)`, url: `https://esco.example.org/eval/${s.id}/r${i + 1}`, source: "fixture" }],
  }));
  const outcomes = s.outcomes.map(([text, bloom, idx], i) => ({
    id: `LO${i + 1}`, text, bloom, moduleIds: idx.map((n) => `M${n + 1}`), objectiveIds: ["CO1"], roleIds: [], origin: "handout", locked: true, provenance: prov("seed"),
  }));
  const modules = deriveModuleOutcomes(
    s.modules.map(([title, hours], i) => ({ id: `M${i + 1}`, title, hours, topics: [], outcomes: [], foundIn: "handout" as const })),
    outcomes.map((o) => ({ ...o, bloom: o.bloom as BloomLevel, origin: "handout" as const })),
    prov("seed"),
  );
  const sessions = outcomes.map((o, i) => ({ index: i + 1, title: o.text.split(/[,.]/)[0]!, outcomeIds: [o.id] }));
  const sos = deriveSessionOutcomes({ modules, outcomes: outcomes as never }, sessions, prov("seed"));
  return CourseSchema.parse({
    id: s.id, slug: s.id, brief: s.brief,
    modules,
    roles,
    objectives: [{ id: "CO1", text: `Prepare learners for ${s.brief.industry} work in ${s.brief.title}.`, provenance: prov("seed") }],
    outcomes,
    plans: [{
      id: "p1", name: "Classroom", path: "classroom", defaultStyle: "auto", provenance: prov("seed"),
      sessions: sessions.map((x, i) => ({ id: `s${i + 1}`, ...x, sessionOutcomes: sos[i], style: "worked", minutes: 120, video: "none", provenance: prov("seed") })),
    }],
    createdAt: T, updatedAt: T,
  });
}

export const EVAL_COURSES: Course[] = [
  aezc517Course(),
  build({
    id: "ev-powertrain-diploma",
    brief: { title: "EV Powertrain Servicing", audience: "Diploma students in automobile engineering", level: "diploma", contactHours: 30, industry: "EV dealerships and service workshops", markets: ["India"], textbooks: [], notes: "" },
    modules: [["High-voltage safety and PPE", 4], ["Battery pack construction and cell chemistry", 6], ["Motors and inverters", 6], ["Charging systems", 4], ["Diagnostics with scan tools", 6], ["Thermal management", 4]],
    roles: [["EV Service Technician", ["HV isolation", "Scan tools", "Battery diagnostics"]], ["Charging Station Technician", ["AC/DC chargers", "OCPP", "Electrical safety"]]],
    outcomes: [["Demonstrate the high-voltage isolation procedure using the correct PPE.", "apply", [0]], ["Diagnose a battery pack fault from scan-tool data.", "analyse", [1, 4]], ["Explain how an inverter controls motor torque.", "understand", [2]], ["Measure charger output against the specification.", "apply", [3, 5]]],
  }),
  build({
    id: "tuv-auto-technician",
    brief: { title: "Automotive Technician Level 3", audience: "Vocational trainees, ITI background", level: "vocational", contactHours: 40, industry: "Passenger-car service workshops", markets: ["India", "Germany"], textbooks: [], notes: "70/30 practice to theory." },
    modules: [["Workshop safety and tools", 4], ["Engine systems service", 10], ["Brakes and suspension", 8], ["Electrical systems and wiring diagrams", 10], ["Customer communication and job cards", 4], ["Periodic maintenance service", 4]],
    roles: [["Automotive Service Technician", ["Periodic maintenance", "Brake service", "Electrical diagnosis"]], ["Service Advisor", ["Job cards", "Customer handling", "DMS software"]]],
    outcomes: [["Perform a periodic maintenance service following the manufacturer schedule.", "apply", [0, 5]], ["Diagnose an electrical fault using a wiring diagram and multimeter.", "analyse", [3]], ["Perform a brake pad and disc replacement to specification.", "apply", [2]], ["Write a complete job card for a customer complaint.", "apply", [4]], ["Identify engine system faults from symptoms.", "remember", [1]]],
  }),
  build({
    id: "aezc516-ice",
    brief: { title: "Internal Combustion Engines", code: "AEZC516", audience: "M.Tech WILP, working engineers", level: "pg", contactHours: 32, industry: "Automotive OEMs and engine suppliers", markets: ["India"], textbooks: ["Heywood, Internal Combustion Engine Fundamentals"], notes: "" },
    modules: [["Thermodynamic cycles", 4], ["Combustion in SI and CI engines", 6], ["Fuel injection and air handling", 6], ["Emissions and aftertreatment", 6], ["Engine testing and calibration", 6], ["Hybridisation and alternative fuels", 4]],
    roles: [["Engine Calibration Engineer", ["INCA", "Emissions calibration", "DoE"]], ["Aftertreatment Engineer", ["SCR", "DPF", "BS-VI norms"]]],
    outcomes: [["Calculate cycle efficiency for Otto, Diesel and dual cycles.", "apply", [0]], ["Analyse combustion pressure data to diagnose knock.", "analyse", [1, 4]], ["Evaluate aftertreatment options for a BS-VI diesel engine.", "evaluate", [3]], ["Explain the trade-offs of hybrid and alternative-fuel powertrains.", "understand", [2, 5]]],
  }),
  build({
    id: "mfg-quality-analytics",
    brief: { title: "Data Analytics for Manufacturing Quality", audience: "Quality engineers in automotive plants", level: "professional", contactHours: 24, industry: "Automotive component manufacturing", markets: ["India"], textbooks: [], notes: "Short professional course." },
    modules: [["Quality data and measurement systems", 4], ["Statistical process control", 6], ["Root-cause analysis with data", 6], ["Dashboards for the shop floor", 4], ["Capstone: a real plant dataset", 4]],
    roles: [["Quality Engineer", ["SPC", "8D", "MSA"]], ["Manufacturing Data Analyst", ["Python", "Power BI", "SQL"]]],
    outcomes: [["Calculate process capability from a sample dataset.", "apply", [0, 1]], ["Investigate a defect trend using Pareto and fishbone analysis.", "analyse", [2]], ["Design a shop-floor quality dashboard for a production line.", "create", [3, 4]]],
  }),
  build({
    id: "school-electrical-safety",
    brief: { title: "Electricity and Safety at Home", audience: "Class 9 students", level: "school", contactHours: 8, industry: "General public and electrical trades", markets: ["India"], textbooks: [], notes: "" },
    modules: [["Circuits, current and voltage", 2], ["Household wiring and earthing", 2], ["Electrical hazards and first response", 2], ["Saving energy", 2]],
    roles: [["Electrician (apprentice)", ["Wiring", "Safety", "Earthing"]]],
    outcomes: [["Describe how current flows in a simple circuit.", "understand", [0]], ["Identify unsafe wiring and earthing at home.", "remember", [1, 2]], ["Calculate the monthly energy cost of household appliances.", "apply", [3]]],
  }),
];
