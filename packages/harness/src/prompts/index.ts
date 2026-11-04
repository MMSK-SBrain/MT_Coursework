export type { PromptModule, PromptContext } from "./types.js";
export { parseInputsPrompt } from "./parseInputs.js";
export { roleKeywordsPrompt, roleClusterPrompt } from "./findRoles.js";
export { proposeFitPrompt } from "./proposeFit.js";
export { draftOutcomesPrompt } from "./draftOutcomes.js";
export { suggestOutcomeEditPrompt } from "./suggestOutcomeEdit.js";
export { draftPlanPrompt } from "./draftPlan.js";
export { draftHourPlanPrompt } from "./draftHourPlan.js";
export { findFurtherLearningPrompt } from "./findFurtherLearning.js";
export { draftCaseStudyPrompt } from "./draftCaseStudy.js";
export { reviewPrompt, rubricScore, OUTCOMES_RUBRIC, FIT_RUBRIC, type Rubric } from "./review.js";
export { STANDARDS } from "./standards.js";

import { parseInputsPrompt } from "./parseInputs.js";
import { roleClusterPrompt, roleKeywordsPrompt } from "./findRoles.js";
import { proposeFitPrompt } from "./proposeFit.js";
import { draftOutcomesPrompt } from "./draftOutcomes.js";
import { suggestOutcomeEditPrompt } from "./suggestOutcomeEdit.js";
import { draftPlanPrompt } from "./draftPlan.js";
import { draftHourPlanPrompt } from "./draftHourPlan.js";
import { findFurtherLearningPrompt } from "./findFurtherLearning.js";
import { draftCaseStudyPrompt } from "./draftCaseStudy.js";
import { reviewPrompt } from "./review.js";
import { blockRepairPrompt, contentCheckPrompt } from "./contentCheck.js";

/** Every prompt id -> version, for feedback grouping and change tracking. */
export const PROMPT_VERSIONS: Record<string, string> = Object.fromEntries(
  [parseInputsPrompt, roleKeywordsPrompt, roleClusterPrompt, proposeFitPrompt, draftOutcomesPrompt, suggestOutcomeEditPrompt,
    draftPlanPrompt, draftHourPlanPrompt, findFurtherLearningPrompt, draftCaseStudyPrompt, reviewPrompt, contentCheckPrompt, blockRepairPrompt].map((p) => [p.id, p.version]),
);
export { contentCheckPrompt, blockRepairPrompt } from "./contentCheck.js";
