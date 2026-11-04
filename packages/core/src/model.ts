// The course model: the one shape every package reads and writes.
// A course is stored as a single JSON document (Postgres jsonb in the app, course.json in the repo).
import { z } from "zod";

export const Id = z.string().min(1);

/** Who/what produced a piece of content. Every generated item carries one. */
export const Provenance = z.object({
  model: z.string(), // e.g. "qwen/qwen3-235b-a22b" or "human" or "import"
  promptId: z.string(), // stage prompt id, e.g. "outcomes.draft"
  promptVersion: z.string(), // e.g. "3"
  costUsd: z.number().nonnegative().default(0),
  createdAt: z.string(), // ISO 8601
  builtFrom: z.array(Id).default([]), // ids of items this was generated from (outcomes, roles, ...)
  structureVersion: z.number().int().nonnegative().optional(),
});
export type Provenance = z.infer<typeof Provenance>;

export const SourceFile = z.object({
  id: Id,
  kind: z.enum(["handout", "moduleSheet", "other"]),
  filename: z.string(),
  mime: z.string(),
  storageKey: z.string(), // object-storage key or repo-relative path
});
export type SourceFile = z.infer<typeof SourceFile>;

export const CourseBrief = z.object({
  title: z.string(),
  code: z.string().optional(), // e.g. "AEZC517"
  audience: z.string(), // e.g. "M.Tech WILP, working engineers"
  level: z.enum(["school", "diploma", "ug", "pg", "professional", "vocational"]),
  contactHours: z.number().positive(),
  industry: z.string(), // e.g. "Automotive OEMs and Tier-1 suppliers"
  markets: z.array(z.string()).min(1), // e.g. ["India", "Germany"]
  textbooks: z.array(z.string()).default([]),
  notes: z.string().default(""),
});
export type CourseBrief = z.infer<typeof CourseBrief>;

export const Module = z.object({
  id: Id, // "M1"
  title: z.string(),
  hours: z.number().nonnegative(),
  topics: z.array(z.string()).default([]),
  foundIn: z.enum(["handout", "moduleSheet", "both", "fit", "user"]),
  note: z.string().optional(), // e.g. "Not in handout"
});
export type Module = z.infer<typeof Module>;

export const JobRole = z.object({
  id: Id,
  title: z.string(),
  postings: z.number().int().nonnegative(),
  experience: z.string().optional(), // "2–8 yrs"
  skills: z.array(z.string()),
  moduleMatch: z.number().min(0).max(100), // % overlap with the modules
  evidence: z.array(z.object({ title: z.string(), url: z.string().url(), source: z.string() })).default([]),
  selected: z.boolean().default(false),
  addedByUser: z.boolean().default(false),
});
export type JobRole = z.infer<typeof JobRole>;

export const FitChange = z.object({
  id: Id,
  kind: z.enum(["add", "strengthen", "trim"]),
  text: z.string(),
  reason: z.string(),
  targetModuleId: Id.or(z.literal("new")),
  hoursDelta: z.number(),
  roleIds: z.array(Id),
  academicConflict: z.string().optional(), // set when the change conflicts with the handout, e.g. "CO1 requires soft skills"
  decision: z.enum(["pending", "accepted", "changed", "rejected"]).default("pending"),
  provenance: Provenance,
});
export type FitChange = z.infer<typeof FitChange>;

export const BloomLevel = z.enum(["remember", "understand", "apply", "analyse", "evaluate", "create"]);
export type BloomLevel = z.infer<typeof BloomLevel>;

export const Objective = z.object({
  id: Id, // "CO1"
  text: z.string(),
  locked: z.boolean().default(false),
  provenance: Provenance,
});
export type Objective = z.infer<typeof Objective>;

export const Outcome = z.object({
  id: Id, // "LO1"
  text: z.string(),
  bloom: BloomLevel,
  moduleIds: z.array(Id).min(1),
  objectiveIds: z.array(Id).default([]),
  roleIds: z.array(Id).default([]),
  origin: z.enum(["handout", "fit", "new", "user"]),
  locked: z.boolean().default(false),
  provenance: Provenance,
});
export type Outcome = z.infer<typeof Outcome>;

export const EditInstruction = z.object({
  kind: z.enum(["raiseBloom", "measurable", "industryContext", "shorten", "split", "matchHandout", "free"]),
  note: z.string().default(""), // the teacher's own words for kind "free" (optional otherwise)
});
export type EditInstruction = z.infer<typeof EditInstruction>;

export const OutcomeSuggestion = z.object({
  targetId: Id,
  proposed: z.array(z.object({ text: z.string(), bloom: BloomLevel })).min(1), // 2 entries when split
  reason: z.string(),
});
export type OutcomeSuggestion = z.infer<typeof OutcomeSuggestion>;

// ---- Learning plans ---------------------------------------------------------

export const LearningPath = z.enum([
  "classroom", "lab", "bootcamp", // live
  "flipped", "blended", "cohort", // blended
  "elearning", "micro", // self-paced
  "youtube", "shorts", // content
]);
export type LearningPath = z.infer<typeof LearningPath>;

export const TeachingStyle = z.enum([
  // Explain
  "teaching", "worked", "story", "analogy",
  // Engage
  "discussion", "debate", "dyk", "challenge",
  // Apply
  "case", "pbl", "project", "lab", "roleplay",
  // Investigate
  "teardown", "failure", "expert", "retrieval",
]);
export type TeachingStyle = z.infer<typeof TeachingStyle>;

export const VideoKind = z.enum(["none", "demo", "whiteboard", "explainroo", "screen", "slides"]);
export type VideoKind = z.infer<typeof VideoKind>;

export const BlockKind = z.enum(["hook", "teach", "activity", "case", "check", "wrap", "break"]);

export const IndustryExample = z.object({
  text: z.string(),
  sector: z.string(), // e.g. "automotive"
  roleIds: z.array(Id).default([]),
  sources: z.array(z.object({ title: z.string(), url: z.string().url() })).default([]),
});
export type IndustryExample = z.infer<typeof IndustryExample>;

export const HourBlock = z.object({
  id: Id,
  hour: z.number().int().positive(), // 1-based hour within the session
  startMin: z.number().int().nonnegative(), // minutes from the start of that hour
  minutes: z.number().int().positive(),
  kind: BlockKind,
  title: z.string(),
  activity: z.string(), // what the teacher and learners do
  outcomeIds: z.array(Id).default([]),
  style: TeachingStyle,
  industryExample: IndustryExample.optional(),
  check: z.array(z.string()).default([]), // quick-check questions
  needsSlides: z.boolean().default(false),
  provenance: Provenance,
});
export type HourBlock = z.infer<typeof HourBlock>;

export const FurtherLink = z.object({
  id: Id,
  kind: z.enum(["youtube", "article", "standard", "other"]),
  title: z.string(),
  url: z.string().url(),
  channelOrSite: z.string().optional(),
  durationSec: z.number().int().positive().optional(),
  publishedAt: z.string().optional(),
  why: z.string(), // one line: why this helps the session
  approved: z.boolean().default(false),
  lastCheckedAt: z.string().optional(),
  alive: z.boolean().default(true),
});
export type FurtherLink = z.infer<typeof FurtherLink>;

export const CaseStudy = z.object({
  id: Id,
  label: z.enum(["real", "composite"]), // never unlabelled
  title: z.string(),
  background: z.string(),
  data: z.string().default(""), // tables or figures as markdown
  questions: z.array(z.string()).min(1),
  teachingNote: z.string(),
  sources: z.array(z.object({ title: z.string(), url: z.string().url() })).default([]), // required when label = real
  outcomeIds: z.array(Id).default([]),
  provenance: Provenance,
});
export type CaseStudy = z.infer<typeof CaseStudy>;

export const AssetRef = z.object({
  kind: z.enum(["slides", "instructorGuide", "video"]),
  storageKey: z.string(),
  status: z.enum(["queued", "rendering", "ready", "failed"]),
  provenance: Provenance,
});
export type AssetRef = z.infer<typeof AssetRef>;

export const Session = z.object({
  id: Id,
  index: z.number().int().positive(),
  title: z.string(),
  outcomeIds: z.array(Id).min(1),
  style: TeachingStyle,
  minutes: z.number().int().positive(),
  video: VideoKind.default("none"),
  blocks: z.array(HourBlock).default([]),
  links: z.array(FurtherLink).default([]),
  caseStudies: z.array(CaseStudy).default([]),
  assets: z.array(AssetRef).default([]),
  stale: z.boolean().default(false), // set when an upstream item changed
  provenance: Provenance,
});
export type Session = z.infer<typeof Session>;

export const PlanSpec = z.object({
  path: LearningPath,
  style: TeachingStyle.or(z.literal("auto")),
  audienceVariant: z.string().optional(), // e.g. "freshers"
  name: z.string().optional(),
});
export type PlanSpec = z.infer<typeof PlanSpec>;

export const LearningPlan = z.object({
  id: Id,
  name: z.string(),
  path: LearningPath,
  defaultStyle: TeachingStyle.or(z.literal("auto")),
  audienceVariant: z.string().optional(),
  sessions: z.array(Session),
  provenance: Provenance,
});
export type LearningPlan = z.infer<typeof LearningPlan>;

// ---- The course aggregate ---------------------------------------------------

export const Course = z.object({
  id: Id,
  slug: z.string(),
  ownerId: Id.optional(),
  brief: CourseBrief,
  sources: z.array(SourceFile).default([]),
  modules: z.array(Module),
  structureVersion: z.number().int().nonnegative().default(1),
  structureConfirmedAt: z.string().optional(),
  roles: z.array(JobRole).default([]),
  fit: z.array(FitChange).default([]),
  objectives: z.array(Objective).default([]),
  outcomes: z.array(Outcome).default([]),
  outcomesFrozenAt: z.string().optional(),
  plans: z.array(LearningPlan).default([]),
  createdAt: z.string(),
  updatedAt: z.string(),
});
export type Course = z.infer<typeof Course>;

// ---- Feedback ---------------------------------------------------------------

export const Feedback = z.object({
  id: Id,
  userId: Id.optional(),
  courseId: Id.optional(),
  targetPath: z.string().optional(), // JSON path of the item, e.g. "outcomes[LO3]" or "plans[p1].sessions[s2].blocks[b4]"
  scope: z.enum(["item", "site"]),
  rating: z.enum(["up", "down"]).optional(),
  category: z.enum(["inaccurate", "lowQuality", "notRelevant", "wrongLevel", "missing", "bug", "feature", "other"]).optional(),
  text: z.string().default(""),
  model: z.string().optional(), // copied from the item's provenance
  promptId: z.string().optional(),
  promptVersion: z.string().optional(),
  createdAt: z.string(),
});
export type Feedback = z.infer<typeof Feedback>;
