// Contracts between the app and the AI harness. The web app depends only on these
// interfaces; @cg/harness implements them (with a mock implementation for tests and dev).
import type {
  CaseStudy, Course, CourseBrief, EditInstruction, FitChange, FurtherLink, HourBlock,
  JobRole, LearningPlan, Module, Objective, Outcome, OutcomeSuggestion, PlanSpec, Provenance, SourceFile,
} from "./model.js";

export interface Generated<T> {
  value: T;
  provenance: Provenance;
  /** Code-checked rule failures that survived the repair attempt. Shown to the teacher as warnings. */
  warnings: string[];
}

/** Raw bytes of an uploaded file plus its metadata. */
export interface InputFile {
  meta: SourceFile;
  bytes: Uint8Array;
}

export interface ParsedInputs {
  brief: Partial<CourseBrief>;
  modules: Module[];
  objectives: Objective[]; // found in the handout, may be empty
  outcomes: Outcome[]; // found in the handout, may be empty
  gaps: string[]; // e.g. "CO4 and CO5 are empty in the handout"
}

export interface Stages {
  /** Stage 1. Extract brief and modules from a handout and/or a module sheet and merge them. */
  parseInputs(files: InputFile[]): Promise<Generated<ParsedInputs>>;
  /** Stage 2. Broad role search from module keywords. Keywords are returned so the UI can show and edit them. */
  findRoles(brief: CourseBrief, modules: Module[], keywords?: string[]): Promise<Generated<{ keywords: string[]; roles: JobRole[]; postingsRead: number }>>;
  /** Stage 3. Compare modules with the selected roles and propose add/strengthen/trim changes. */
  proposeFit(course: Course): Promise<Generated<FitChange[]>>;
  /** Stage 4. Objectives, course LOs, and the modules with their drafted module outcomes (locked items kept). */
  draftOutcomes(course: Course): Promise<Generated<{ objectives: Objective[]; outcomes: Outcome[]; modules: Module[] }>>;
  /** Stage 4. One suggested edit to one outcome. */
  suggestOutcomeEdit(course: Course, outcomeId: string, instruction: EditInstruction): Promise<Generated<OutcomeSuggestion>>;
  /** Stage 5. Draft a learning plan (sessions, styles, video kinds) from frozen outcomes. */
  draftPlan(course: Course, spec: PlanSpec): Promise<Generated<LearningPlan>>;
  /** Stage 6 (free). Hour-wise blocks for one session, with industry examples and quick checks. */
  draftHourPlan(course: Course, planId: string, sessionId: string): Promise<Generated<HourBlock[]>>;
  /** Stage 6 (free). Further-learning links for one session; unapproved until the teacher approves them. */
  findFurtherLearning(course: Course, planId: string, sessionId: string): Promise<Generated<FurtherLink[]>>;
  /** Stage 6 (paid). One case study for a session. */
  draftCaseStudy(course: Course, planId: string, sessionId: string, label: CaseStudy["label"]): Promise<Generated<CaseStudy>>;
}

// ---- Data sources the harness depends on (swappable; job source is still an open decision) ----

export interface JobPosting {
  title: string;
  company?: string; // may be withheld
  location: string;
  postedAt: string;
  skills: string[];
  description: string;
  url: string;
  source: string; // e.g. "adzuna", "websearch", "fixture"
}

export interface JobSource {
  search(q: { keywords: string[]; markets: string[]; days: number; limit: number }): Promise<JobPosting[]>;
}

export interface VideoCandidate {
  title: string;
  url: string;
  channel: string;
  durationSec: number;
  publishedAt: string;
  description: string;
}

export interface LinkSource {
  youtube(q: { query: string; maxDurationSec?: number; limit: number }): Promise<VideoCandidate[]>;
  web(q: { query: string; limit: number }): Promise<{ title: string; url: string; snippet: string }[]>;
  isAlive(url: string): Promise<boolean>;
}

// ---- Exports and video (implemented by @cg/exports and @cg/video) ----

export interface Exporter {
  /** Free tier: the whole course design as markdown files, path → content. */
  markdown(course: Course): Record<string, string>;
  /** Paid. */
  slides(course: Course, planId: string, sessionId: string): Promise<Uint8Array>; // .pptx
  instructorGuide(course: Course, planId: string, sessionId: string): Promise<Uint8Array>; // .docx
}

export interface VideoProject {
  /** explainroo inputs */
  scriptMd: string;
  scenesJs: string;
  /** Uploaded or generated assets to copy into the explainroo project, path → bytes */
  assets: Record<string, Uint8Array>;
  estimatedSec: number;
}

export interface VideoBuilder {
  plan(course: Course, planId: string, sessionId: string): Promise<VideoProject>;
  render(project: VideoProject, opts: { workDir: string; maxSec: number }): Promise<{ mp4Path: string; durationSec: number }>;
}
