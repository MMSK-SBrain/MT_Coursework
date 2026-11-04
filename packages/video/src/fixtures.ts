// Sample content from the coursesmith prototype: AEZC517 Systems Engineering, "What a good requirement looks like".
import type { Course, HourBlock, LearningPath, Session } from "@cg/core";

const provenance = { model: "fixture", promptId: "fixture", promptVersion: "1", costUsd: 0, createdAt: "2026-11-04T00:00:00Z", builtFrom: [] };

const block = (id: string, hour: number, startMin: number, minutes: number, kind: HourBlock["kind"], title: string, activity: string, extra: Partial<HourBlock> = {}): HourBlock => ({
  id, hour, startMin, minutes, kind, title, activity, outcomeIds: ["LO2"], style: "dyk", check: [], needsSlides: false, provenance, ...extra,
});

const blocks: HourBlock[] = [
  block("b1", 1, 0, 10, "hook", "A battery pack can push 400 V through a car", "Ask who decided how the pack must never fail.", {
    industryExample: { roleIds: [], sources: [], sector: "automotive", text: "A BMS requirement that says the pack shall be safe cannot be tested, so the supplier and the OEM argue at integration" },
  }),
  block("b2", 1, 10, 20, "teach", "Needs, requirements and what makes one verifiable", "A requirement is verifiable when a test can show it passes or fails. Compare a vague need with a testable statement."),
  block("b3", 1, 30, 15, "case", "Rewrite a bad requirement", "Learners rewrite the pack shall not overheat into a measurable statement with a limit and a condition.", {
    industryExample: { roleIds: [], sources: [], sector: "automotive", text: "The pack shall disconnect the contactors within 100 ms when any cell is above 60 degrees Celsius" },
    check: ["Which number in this requirement could a test bench check?"],
  }),
  block("b4", 1, 45, 10, "activity", "Trace the requirement to a test", "Link the rewritten requirement to one HIL test case in the requirements tool."),
  block("b5", 1, 55, 5, "wrap", "Three rules for a good requirement", "One sentence recap."),
];

const session = (id: string, index: number, video: Session["video"]): Session => ({
  id, index, title: "What a good requirement looks like", outcomeIds: ["LO2"], style: "dyk", minutes: 60, video, blocks, links: [], caseStudies: [], assets: [], stale: false, provenance,
});

const plan = (id: string, path: LearningPath, video: Session["video"]) => ({
  id, name: `${path} plan`, path, defaultStyle: "dyk" as const, sessions: [session("s3", 3, video)], provenance,
});

export const aezc517: Course = {
  id: "c-aezc517",
  slug: "aezc517",
  brief: { title: "Automotive Systems Engineering", code: "AEZC517", audience: "M.Tech WILP, working engineers", level: "pg", contactHours: 32, industry: "Automotive OEMs and Tier-1 suppliers", markets: ["India", "Germany"], textbooks: [], notes: "" },
  sources: [],
  modules: [{ id: "M3", title: "Stakeholder needs and requirements engineering", hours: 6, topics: [], foundIn: "both" }],
  structureVersion: 1,
  roles: [],
  fit: [],
  objectives: [],
  outcomes: [
    { id: "LO2", text: "Write verifiable system requirements with full traceability from stakeholder needs, using a requirements tool.", bloom: "apply", moduleIds: ["M3"], objectiveIds: [], roleIds: [], origin: "fit", locked: true, provenance },
  ],
  plans: [
    plan("p-youtube", "youtube", "explainroo"),
    plan("p-micro", "micro", "whiteboard"),
    plan("p-flipped", "flipped", "slides"),
    plan("p-blended", "blended", "demo"),
    plan("p-classroom", "classroom", "none"),
  ],
  createdAt: "2026-11-04T00:00:00Z",
  updatedAt: "2026-11-04T00:00:00Z",
};

/** plan ids that allow each kind, for the sample and the tests */
export const PLAN_FOR_KIND = { explainroo: "p-youtube", whiteboard: "p-micro", slides: "p-flipped", demo: "p-blended", screen: "p-youtube" } as const;
