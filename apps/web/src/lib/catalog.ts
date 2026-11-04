// UI copy for paths, styles and video kinds, ported from the approved prototype.
import type { EditInstruction, LearningPath, TeachingStyle, VideoKind } from "@cg/core";
import { VIDEO_BY_PATH } from "@cg/core";

export const STAGES = [
  { id: "inputs", t: "Inputs", s: "Handout and/or module sheet" },
  { id: "roles", t: "Job roles", s: "Broad search, you pick" },
  { id: "fit", t: "Course–job fit", s: "Add, change, confirm" },
  { id: "outcomes", t: "Outcomes", s: "Suggest edits, then freeze" },
  { id: "plans", t: "Learning plans", s: "Path and style" },
  { id: "build", t: "Build", s: "Slides, guides, videos" },
] as const;
export type StageId = (typeof STAGES)[number]["id"];

export const MODES: Record<LearningPath, { fam: "Live" | "Blended" | "Self-paced" | "Content"; t: string; d: string; video: VideoKind[] }> = {
  classroom: { fam: "Live", t: "Classroom lecture", d: "Instructor-led sessions, in person or on Zoom.", video: VIDEO_BY_PATH.classroom },
  lab: { fam: "Live", t: "Lab / workshop", d: "Hands-on bench or tool sessions with a short brief.", video: VIDEO_BY_PATH.lab },
  bootcamp: { fam: "Live", t: "Intensive bootcamp", d: "Full days, projects every afternoon.", video: VIDEO_BY_PATH.bootcamp },
  flipped: { fam: "Blended", t: "Flipped classroom", d: "Watch before class, apply in class.", video: VIDEO_BY_PATH.flipped },
  blended: { fam: "Blended", t: "Blended / hybrid", d: "Mix of live sessions and online modules.", video: VIDEO_BY_PATH.blended },
  cohort: { fam: "Blended", t: "Cohort-based online", d: "Weekly live call plus async work and peer review.", video: VIDEO_BY_PATH.cohort },
  elearning: { fam: "Self-paced", t: "Self-paced eLearning", d: "LMS modules with reading pages and quizzes.", video: VIDEO_BY_PATH.elearning },
  micro: { fam: "Self-paced", t: "Microlearning", d: "5-minute mobile lessons, one idea each.", video: VIDEO_BY_PATH.micro },
  youtube: { fam: "Content", t: "YouTube series", d: "6–12 minute episodes for a public audience.", video: VIDEO_BY_PATH.youtube },
  shorts: { fam: "Content", t: "Shorts / Reels", d: "Vertical 30–60 second clips.", video: VIDEO_BY_PATH.shorts },
};

export const STYLE_FAMS: Record<"Explain" | "Engage" | "Apply" | "Investigate", [TeachingStyle, string, string][]> = {
  Explain: [["teaching", "Direct teaching", "Concept, example, check"], ["worked", "Worked example", "Solve one step by step"], ["story", "Story-led", "A real programme as the thread"], ["analogy", "Analogy first", "Start from something familiar"]],
  Engage: [["discussion", "Socratic discussion", "Questions lead to the concept"], ["debate", "Debate", "Two sides argue a design choice"], ["dyk", "Did you know / viral", "Surprising fact as the hook"], ["challenge", "Gamified challenge", "Timed puzzle or quiz battle"]],
  Apply: [["case", "Case study", "Analyse a real decision"], ["pbl", "Problem-based", "Open problem first, theory as needed"], ["project", "Project-based", "Build part of the capstone"], ["lab", "Hands-on lab", "Tool or bench exercise"], ["roleplay", "Role-play / simulation", "Play the OEM, supplier, assessor"]],
  Investigate: [["teardown", "Teardown", "Take a real system apart"], ["failure", "Failure analysis", "A recall or incident, what went wrong"], ["expert", "Industry voice", "Interview or guest walkthrough"], ["retrieval", "Retrieval practice", "Quiz-led review of earlier sessions"]],
};

export const STYLES: Record<TeachingStyle | "auto", string> = {
  ...(Object.fromEntries(Object.values(STYLE_FAMS).flat().map(([k, v]) => [k, v])) as Record<TeachingStyle, string>),
  auto: "Auto (matched to outcome)",
};

export const VIDEO: Record<VideoKind, string> = {
  none: "No video", demo: "Demonstration", whiteboard: "Whiteboard animation", explainroo: "Explainroo motion", screen: "Screen / tool demo", slides: "Slides + voice-over",
};
export const VDESC: Record<VideoKind, string> = {
  none: "Skip video for this session", demo: "Instructor and bench footage with screen inserts", whiteboard: "Hand-drawn style, drawn as narrated",
  explainroo: "Motion graphics, charts and camera moves", screen: "Recorded tool walkthrough", slides: "Your slides with narration",
};

/** Sample scene plans per video kind. Replaced by @cg/video's VideoBuilder.plan() once it is wired in. */
export const SCENES: Partial<Record<VideoKind, [string, string, string][]>> = {
  explainroo: [["0:00", "Hook", "“A battery pack can push 400 V through a car. Who decided how it must never fail?”"], ["0:12", "Chart", "Requirement count per vehicle programme, 2010 → 2025, animated line."], ["0:40", "Diagram", "Stakeholder needs → system requirements → subsystem requirements, camera follows the arrows."], ["1:30", "Image", "Photo of a BMS board with labelled sensing lines (asset: upload)."], ["2:10", "Callout", "Bad vs good requirement, side by side, with the fixes highlighted."], ["3:20", "Recap", "Three rules for a verifiable requirement."]],
  whiteboard: [["0:00", "Draw", "Hand draws a car outline, then a battery pack inside it."], ["0:20", "Draw", "Stick-figure stakeholders around the car with speech bubbles."], ["1:00", "Write", "Need: “The pack shall not overheat” → rewritten as a verifiable requirement."], ["2:15", "Draw", "Arrow down to a test bench sketch."]],
  demo: [["0:00", "Camera", "Instructor at the bench, BMS evaluation board in frame."], ["0:30", "Screen", "Polarion: create a requirement and link it to a test case."], ["2:00", "Camera", "Trigger an over-temperature fault and show the trace."]],
  screen: [["0:00", "Screen", "Polarion project overview."], ["0:45", "Screen", "Create, link, and run the traceability report."]],
  slides: [["0:00", "Slide", "Title slide with voice-over."], ["0:20", "Slide", "Content slides with narration from speaker notes."]],
};

/** Rough length of a scene plan: last timecode plus a minute. */
export function sceneSeconds(kind: VideoKind): number {
  const sc = SCENES[kind];
  if (!sc?.length) return 0;
  const [m, s] = sc[sc.length - 1]![0].split(":").map(Number);
  return (m ?? 0) * 60 + (s ?? 0) + 60;
}

export const QUICK: [EditInstruction["kind"], string][] = [
  ["raiseBloom", "Raise the Bloom level"],
  ["measurable", "Make it measurable"],
  ["industryContext", "Add industry context"],
  ["shorten", "Shorten"],
  ["split", "Split into two"],
  ["matchHandout", "Match handout wording"],
];

export const AUDIENCE_VARIANTS: { id: string; label: string; variants: string[] }[] = [
  { id: "one", label: "One version", variants: [] },
  { id: "fresh-exp", label: "Freshers + experienced", variants: ["freshers", "experienced"] },
  { id: "eng-mgr", label: "Engineers + managers", variants: ["engineers", "managers"] },
];

export const cap = (s: string) => s.charAt(0).toUpperCase() + s.slice(1);
