# Storytelling Framework Generator - Skill Specification

**Version:** 1.0
**Date:** 2026-01-02
**Purpose:** Generate storytelling frameworks from learning outcomes to create engaging educational content (videos, PPTs, scripts)

---

## Overview

This Claude skill reads learning outcomes from a template file, analyzes the target audience, domain, and depth, then generates storytelling frameworks that achieve each learning outcome. The frameworks can be used to develop video scripts, presentations, or other instructional materials.

---

## Core Skill Logic

### Input
- Path to Excel template (learning outcomes structure)
- Optional parameters:
  - Audience override
  - Technique preference
  - Output folder path
  - Target medium (video/PPT/other)

### Processing Flow

**PHASE 0: Requirements Gathering**
1. Read Excel template (Course_Info, Outcomes_And_Structure sheets)
2. Extract available information:
   - Course details (name, description, duration, target audience)
   - Module/Lesson/Outcome hierarchy
   - Bloom levels, categories, session types
3. Present extracted information to user for confirmation
4. Ask guided questions for missing information:
   - **Audience Details:** Age group (Juvenile 8-17 / Adult 18-54 / Senior 55+), Tech proficiency (Non-Tech / Basic / Intermediate / Advanced)
   - **Cultural Context:** Region-specific requirements, language preferences
   - **Organization Requirements:** Company-specific examples needed, brand/tone guidelines
   - **Marketing Strategy:** Hooks for follow-on courses, teaser topics
   - **Output Format:** Primary medium (video/PPT/interactive), duration constraints, accessibility needs
   - **Delivery Constraints:** Platform requirements, resource limitations
4. Generate requirements file (requirements.md or .yaml)
5. Show to user for approval/edits
6. Save for use throughout generation process

**PHASE 1: Analysis & Planning**
1. Parse complete module/lesson/outcome structure from Excel
2. Analyze each learning outcome:
   - Category (Knowledge/Skill/Attitude)
   - Bloom level (Remember → Create)
   - Session type (lecture/quiz/practical/mixed)
   - Content complexity
   - Relationship to other outcomes
3. Apply grouping rules to determine story granularity (see Grouping Rules section)
4. Select storytelling techniques using rotation matrix (see Technique Selection section)
5. Generate comprehensive TODO list:
   - Module-level overview tasks (if user wants module arcs)
   - Lesson-level story generation tasks
   - Include estimated scope for each task
6. Present plan as table showing:
   - Module > Lesson > Outcomes
   - Proposed storytelling technique for each
   - Grouping decisions (which SOs combined)
   - Rationale for choices
7. **Wait for user approval** - allow overrides to technique selections
8. Update plan based on user feedback

**PHASE 2: Story Generation (Sequential, per TODO item)**
For each lesson:
1. Mark TODO as in_progress
2. Retrieve all Session Outcomes (SOs) for the lesson
3. For each SO or SO group:
   a. Confirm storytelling technique (show to user if override requested)
   b. Generate story framework using appropriate template
   c. Include all required components (see Story Framework Structure)
   d. Generate assessment content if applicable
   e. Add medium-specific adaptations based on requirements
4. Combine into lesson .md file
5. Check line count:
   - If >1000 lines, split into Part-1, Part-2, etc.
   - Split at logical breakpoints (between outcomes, between story sections)
6. Save file to output folder
7. Mark TODO as completed
8. **Show progress to user** (lesson completed, X of Y remaining)
9. Move to next lesson

**PHASE 3: Review & Finalization**
1. Generate module-level overview files (if requested)
2. Create navigation index file:
   - Table of contents
   - Module/lesson structure
   - Quick reference to storytelling techniques used
   - Links to all generated files
3. Cross-check technique rotation across course
4. Generate summary report:
   - Files created
   - Techniques used (distribution)
   - Warnings/notes for user review
5. Present final output to user

---

## Storytelling Technique Selection

### Technique Mapping Matrix

| Learning Context | Default Technique | Alternatives | Rationale |
|------------------|-------------------|--------------|-----------|
| **Knowledge: Remember/Understand (Technical)** | Problem-Framing Only | Discovery Pattern, Helper's Journey | Technical concepts need clarity over narrative |
| **Knowledge: Understand (Conceptual)** | Analogy-Based Explanation | Discovery Pattern | Analogies help with abstract concepts |
| **Skill: Apply** | Scenario-Based Learning | Character-Driven, Hero's Journey | Skills need practice in realistic contexts |
| **Skill: Analyze/Evaluate** | Mystery/Detective Story | Conflict-Resolution Arc | Analysis requires investigation mindset |
| **Attitude: Understand/Apply** | Character Transformation | Relational Journey | Attitudes change through emotional connection |
| **Attitude: Create** | Empowerment Arc | Mentor-Apprentice | Creation requires confidence building |
| **Safety/Security Topics** | Cautionary Tale + Triumph | Real Victim Story + Resolution | Safety requires emotional impact + empowerment |

### Rotation Strategy
- Track last 3 techniques used within current module
- Avoid same technique in consecutive lessons (unless overridden)
- Prefer variety within module (max 2 uses of same technique per module)
- Track across entire course for global distribution analysis
- **Override mechanism:**
  - User can specify technique in natural language ("Use a mystery story here")
  - OR select from predefined list when prompted
  - Claude asks for clarification if ambiguous

### Available Storytelling Techniques

1. **Problem-Framing Only** - No narrative, clear problem statement and solution
2. **Scenario-Based Learning** - Realistic situation character must navigate
3. **Hero's Journey** - Character overcomes obstacles to master skill
4. **Character Transformation** - Emotional arc showing attitude change
5. **Mystery/Detective Story** - Character investigates and solves problem
6. **Cautionary Tale + Triumph** - Warning story followed by success story
7. **Discovery Pattern** - Character explores and learns through experimentation
8. **Conflict-Resolution Arc** - Character faces dilemma and resolves it
9. **Empowerment Arc** - Character gains confidence and agency
10. **Mentor-Apprentice** - Character learns from guide/expert
11. **Relational Journey** - Character's relationships change through learning
12. **Analogy-Based Explanation** - Abstract concept explained through familiar comparison

---

## Grouping Rules (Adaptive Granularity)

### When to Group Multiple SOs into One Story

1. **Sequential Bloom Levels** (Remember → Understand → Apply on same topic)
   - **Action:** Group into one progressive story
   - **Example:** Define AI → Identify AI examples → Explain how AI learns

2. **Same Category + Related Content**
   - **Action:** Group if content builds cohesively
   - **Example:** Multiple skill SOs about same tool (Configure WhatsApp privacy → Enable 2FA → Set forwarding rules)

3. **Different Categories** (e.g., Knowledge + Attitude)
   - **Action:** Usually separate, unless attitude directly supports knowledge
   - **Exception:** Integrate if attitude provides motivation for knowledge

4. **Technical + Practical**
   - **Action:** Separate for complex technical, integrate for simple technical
   - **Rule:** If technical SO is >5 steps, separate with problem-framing
   - **Rule:** If technical SO is ≤5 steps, integrate into larger story

5. **Different Session Types**
   - **lecture + lecture:** Can group
   - **lecture + practical:** Can integrate (story + practice segment)
   - **quiz:** Always separate (assessment only, not part of story)
   - **mixed:** Analyze content, apply other rules

6. **Technical Content Decision Tree**
   - **Highly procedural (Remember level):** Problem-framing only, separate
   - **Requires behavior change (Apply level):** Lightweight scenario, can group
   - **Safety/critical skill:** Full story, separate for emphasis

### When to Create Module-Level Story Arc

- **User Choice:** Ask in Phase 0 requirements whether user wants module-level continuity
- **If Yes:**
  - Same protagonist across lessons in module
  - Escalating challenges (lesson 1 = basic problem, lesson 3 = complex problem)
  - Callbacks to previous lessons
  - Module conclusion shows character mastery
- **If No:**
  - Independent lesson stories
  - Thematic consistency but different characters
  - Each lesson is self-contained

---

## Story Framework Structure

### File Organization

**Output Directory Structure:**
```
[PROJECT_ROOT]/
  └── storytelling-outputs/
      └── [COURSE-CODE]-[TIMESTAMP]/
          ├── requirements.md                       # Generated in Phase 0
          ├── index.md                              # Navigation/TOC
          ├── Module-1-Overview.md                  # Module-level arc (if requested)
          ├── Module-1-Lesson-1.md                  # Lesson 1 stories
          ├── Module-1-Lesson-2.md                  # Lesson 2 stories
          ├── Module-2-Lesson-1-Part-1.md           # Split if >1000 lines
          ├── Module-2-Lesson-1-Part-2.md
          └── ...
```

**Directory Naming Convention:**
- Base directory: `storytelling-outputs/` (created in project root if not exists)
- Sub-directory: `[COURSE-CODE]-[TIMESTAMP]/`
  - Example: `AISC-2026-01-02-09-30/`
  - Allows multiple runs without overwriting previous outputs
  - Easy to compare different iterations

**Default Output Path:**
- If user doesn't specify output folder, use: `./storytelling-outputs/[COURSE-CODE]-[TIMESTAMP]/`
- If user specifies custom path, use that instead (but still create timestamped subfolder)
- Always inform user where files will be saved at start of Phase 0

### Lesson File Structure

```markdown
# Lesson [X]: [Lesson Name]

## Metadata
- **Module:** [Module Number] - [Module Name]
- **Day:** [Day Number]
- **Target Audience:** [From requirements]
- **Cultural Context:** [From requirements]
- **Target Medium:** [Video/PPT/Other]
- **Learning Outcomes Covered:** [List of SO codes]
- **Storytelling Techniques Used:** [List with rationale]

## Module-Level Context (if applicable)
[Brief summary of where this lesson fits in module arc]
[References to previous/next lessons if connected]

---

## Session Outcome: [SO-CODE]

### Learning Outcome Details
- **Code:** [SO-CODE]
- **Description:** [SO Description from Excel]
- **Category:** [Knowledge/Skill/Attitude]
- **Bloom Level:** [Remember/Understand/Apply/Analyze/Evaluate/Create]
- **Session Type:** [lecture/quiz/practical/mixed]

### Storytelling Approach
- **Technique:** [Selected Technique]
- **Rationale:** [Why this technique for this LO - based on category, Bloom level, content type]
- **Grouping:** [Standalone / Grouped with SO-X-X-X because...]

### Story Framework

#### Characters (if applicable)
- **Name:** [Minimal - name, age, one-line description]
- **Tech Level:** [From requirements - matches target audience]
- **Relevance:** [Why this character works for this LO]

#### Story Beats (Outline/Blueprint Level)

**Setup:**
[Brief description of initial situation, character's current state]
[Learning gap/problem identified]

**Trigger:**
[What prompts the learning journey - problem, opportunity, challenge]

**Rising Action:**
[Key steps in learning process]
[Attempts, obstacles, insights]

**Climax:**
[Aha moment / successful application]
[Demonstration of learning outcome achieved]

**Resolution:**
[Mastery demonstrated, reflection, connection to next learning]

#### Learning Integration Points
- **Setup:** [What concept/skill is introduced here]
- **Rising Action:** [Where practice/exploration happens]
- **Climax:** [Where assessment/demonstration occurs]
- **Resolution:** [Where mastery is confirmed]

#### Emotional Beats
[Map emotional journey: Confusion → Curiosity → Frustration → Insight → Confidence]
[Note: Emotional hooks relevant to target audience]

### Assessment Content

#### Quiz Questions (if applicable)
[Generate 3-5 questions that assess this LO]
[Include answer key]

#### Hands-On Exercise (if applicable)
[Step-by-step practice activity]
[Expected outcome/success criteria]

#### Discussion Prompts (if applicable)
[Questions to facilitate reflection/sharing]

### Medium-Specific Adaptations

#### For Video:
- **Estimated Duration:** [X minutes]
- **Shot Suggestions:** [Close-up, screen recording, B-roll ideas]
- **Visual Cues:** [What to show on screen at each beat]
- **Voiceover Notes:** [Tone, pacing, emphasis points]
- **Transition Cues:** [How to move between story beats]

#### For PPT:
- **Slide Count:** [Estimated number]
- **Slide Breakdown:** [One slide per beat, or grouped]
- **Visual Suggestions:** [Images, icons, diagrams needed]
- **Speaker Notes:** [What presenter should emphasize]
- **Interaction Points:** [Where to pause for questions/discussion]

#### For Interactive/Other:
[Format-specific notes based on requirements]

### Cultural & Contextual Customization

#### Generic Version:
[Story with placeholder variables]
- **[FESTIVAL_NAME]:** [Example: Diwali, Holi, Pongal]
- **[REGIONAL_APP]:** [Example: Paytm, PhonePe, specific regional services]
- **[LOCAL_EXAMPLE]:** [Example: specific government schemes, local news]

#### For [ORGANIZATION_NAME] (if specified in requirements):
**Customization Notes:**
- Replace generic examples with: [Organization-specific examples from requirements]
- Character works at: [Organization context]
- Use cases specific to: [Organization's industry/domain]

### Marketing Integration Points

#### Explicit Hooks:
[Placeholder for promotional messages]
- "After mastering [THIS SKILL], you'll be ready for our [ADVANCED_COURSE] on [TOPIC]"
- "This is just the beginning - explore [RELATED_TOPIC] in our next course"

#### Teaser Endings:
[Subtle hints at advanced topics]
- Story ending shows character curious about [ADVANCED_TOPIC]
- Unresolved question that leads to next course
- Character mentions wanting to learn [NEXT_SKILL]

---

[Repeat structure for each Session Outcome in lesson]

---

## Lesson Summary
- **Total Session Outcomes:** [Count]
- **Story Frameworks Generated:** [Count - some may be grouped]
- **Assessment Items:** [Count of quizzes/exercises/discussions]
- **Estimated Total Duration:** [If video - sum of all durations]
- **Next Steps:** [What lesson/module comes next, what to prepare]

```

---

## Problem-Framing Template (for Technical Topics)

When storytelling is not appropriate (highly procedural, Remember level, pure technical):

```markdown
## Session Outcome: [SO-CODE]

### Learning Outcome Details
[Same as story framework]

### Teaching Approach
- **Method:** Problem-Framing (No narrative story)
- **Rationale:** [Technical/procedural content - clarity prioritized over story]

### Framework

#### 1. Real-World Problem Statement
[Clear, relatable problem the learner faces]
[Concrete example from target audience's life]

#### 2. Why It Matters
[Consequences of not solving this problem]
[Benefits of solving it - tied to audience values]

#### 3. Current State vs Desired State
**Current:** [What learner can't do now]
**Desired:** [What learner will be able to do]
**Gap:** [Specific skill/knowledge needed]

#### 4. Solution Overview
[What tool/technique/skill solves this]
[High-level explanation of how it works]

#### 5. Step-by-Step Application
1. [Step 1 - clear, actionable]
2. [Step 2]
3. [Step 3]
...
[Include screenshots/visual aids suggestions if video/PPT]

#### 6. Verification
[How to know you succeeded]
[What success looks like - specific observable outcome]

#### 7. Troubleshooting
**Common Issue 1:** [Problem] → [Solution]
**Common Issue 2:** [Problem] → [Solution]

#### 8. Practice Exercise
[Hands-on activity to confirm mastery]
[Expected result]

### Assessment Content
[Same structure as story framework]

### Medium-Specific Adaptations
[Same structure as story framework]
```

---

## Audience Personalization Framework

### Age-Based Adaptations

**Juvenile (8-17 years):**
- **Characters:** Relatable teens, school contexts, peer dynamics
- **Narratives:** Game-like, adventure, discovery, competition
- **Language:** Energetic, casual, modern references
- **Pacing:** Fast, engaging, varied
- **Hooks:** Achievement, social connection, fun

**Adult (18-54 years):**
- **Characters:** Working professionals, parents, varied backgrounds
- **Narratives:** Work scenarios, family situations, efficiency/productivity themes
- **Language:** Professional yet accessible, practical
- **Pacing:** Moderate, goal-oriented
- **Hooks:** Career advancement, time-saving, problem-solving

**Senior Citizens (55+):**
- **Characters:** Retirees, grandparents, varied tech comfort levels
- **Narratives:** Family connection, independence, safety, everyday life
- **Language:** Respectful, patient, clear, no jargon (unless explained)
- **Pacing:** Slower, with repetition, step-by-step
- **Hooks:** Safety, family communication, maintaining independence, avoiding scams

### Tech Proficiency Adaptations

**Non-Tech:**
- Extensive use of analogies from non-digital life
- Every technical term explained with familiar comparison
- Step-by-step with screenshots/visuals
- Reassurance and encouragement built into story
- Characters who are also non-tech, learning together

**Basic:**
- Some tech familiarity assumed (knows what apps are, uses smartphone)
- Technical terms introduced with brief explanation
- Focus on practical application over theory
- Characters with basic tech use, learning to do more

**Intermediate:**
- Comfortable with common tools, learning advanced features
- Technical explanations can be more detailed
- Focus on efficiency and optimization
- Characters exploring new capabilities

**Advanced:**
- Technical depth welcome
- Focus on customization, integration, edge cases
- Characters are power users, learning expert techniques

### Cultural Context Variables

Use placeholders that can be customized per region/organization:

- **[FESTIVAL_NAME]** - Regional festivals
- **[LOCAL_FOOD]** - Food references in analogies
- **[REGIONAL_APP]** - Popular regional services/apps
- **[GOVERNMENT_SCHEME]** - Relevant government programs
- **[LOCAL_NEWS_TOPIC]** - Recent events for context
- **[CULTURAL_PRACTICE]** - Traditions, norms, values
- **[LANGUAGE_REFERENCE]** - Mention of regional languages
- **[ORGANIZATION_NAME]** - If B2B client, their company
- **[INDUSTRY_EXAMPLE]** - Sector-specific use cases

---

## Quality Assurance Checks

Before marking lesson as completed, Claude should verify:

1. **Technique Rotation:** Has this technique been used in last 3 lessons?
2. **Audience Alignment:** Does story match target audience profile from requirements?
3. **Learning Outcome Coverage:** Does story framework actually address the SO?
4. **Assessment Quality:** Do quiz/exercise questions actually test the LO?
5. **Cultural Sensitivity:** Are examples appropriate for cultural context?
6. **File Size:** Is file under 1000 lines (if not, split)?
7. **Completeness:** All required sections present?
8. **Medium Alignment:** Does adaptation match target medium from requirements?

If any check fails, flag for user review or auto-correct if possible.

---

## User Interaction Points

### Phase 0:
- Confirm extracted information from Excel
- Answer guided questions about requirements
- Approve/edit generated requirements file

### Phase 1:
- Review complete plan (table of techniques and groupings)
- Override any technique selections
- Approve plan before execution

### Phase 2 (Optional, as needed):
- Confirm technique selection for specific SO if user wants to intervene mid-generation
- Review and approve lesson file before moving to next (if user requests checkpoints)

### Phase 3:
- Review final output and summary report
- Request regeneration of specific lessons if needed

---

## Error Handling

**If Excel file not found:**
- Ask user to provide correct path
- List .xlsx files in current directory

**If Excel structure doesn't match expected format:**
- Show what was found vs what was expected
- Ask user to confirm sheet names and column headers

**If requirements gathering interrupted:**
- Save partial requirements
- Resume from last completed question

**If story generation fails for an SO:**
- Log the error
- Skip to next SO
- Flag in summary report for user review
- Continue with rest of generation

**If file split needed:**
- Find logical breakpoint (between SOs, between story sections)
- Maintain continuity references across split files
- Update TODO and index to reflect split

---

## Extensibility

### Adding New Storytelling Techniques
- Add to technique mapping matrix
- Define template for new technique
- Update rotation tracking

### Supporting New Output Mediums
- Add medium-specific adaptation template
- Update requirements gathering questions
- Add to medium-specific sections in lesson files

### Supporting New Cultural Contexts
- Add new placeholder variables
- Update cultural adaptation section
- Expand character/scenario libraries

---

## Success Criteria

The skill is successful if:
1. ✅ All Session Outcomes have story frameworks or problem-framing
2. ✅ Technique rotation avoids monotony (no more than 2 consecutive same techniques)
3. ✅ Stories align with target audience profile
4. ✅ Assessment content actually tests the learning outcomes
5. ✅ Files are properly organized and <1000 lines
6. ✅ User is engaged and approves at each phase
7. ✅ Output is ready for downstream script/PPT development
8. ✅ Cultural customization placeholders allow easy adaptation
9. ✅ Marketing hooks are integrated appropriately

---

## Example Execution Flow

```
User: Generate storytelling frameworks for my course
Claude: Reading Excel template... Found "Essential AI Skills for Senior Citizens"
Claude: [Shows extracted course info]
Claude: Let me gather additional requirements...

[Phase 0 - Requirements Gathering]
Claude: I found the target audience is "Senior Citizens (55+), India". Is this correct?
User: Yes
Claude: What's your primary output format? Video, PPT, or other?
User: Video
Claude: Any organization-specific examples needed?
User: Yes, for Tata Motors employees
[... more questions ...]
Claude: [Generates requirements.md, shows to user]
User: Looks good, approved

[Phase 1 - Planning]
Claude: [Shows table of all lessons and proposed techniques]
Claude: Module 1, Lesson 1 (3 SOs about defining AI) - I propose grouping into one "Discovery Pattern" story. Agree?
User: Yes, but use "Analogy-Based" instead
Claude: Updated! [Shows revised plan]
User: Approved, proceed

[Phase 2 - Generation]
Claude: [Marks "Module 1 - Lesson 1" as in_progress]
Claude: Generating story framework for SO-1-1-1, SO-1-1-2, SO-1-1-3 (grouped)...
Claude: [Generates lesson file]
Claude: ✅ Module 1 - Lesson 1 complete (847 lines). Moving to Lesson 2... (1 of 15 lessons done)
[... continues through all lessons ...]

[Phase 3 - Finalization]
Claude: All 15 lessons completed! Generating index and summary...
Claude: [Shows summary report]
Claude: Files created: 18 total (15 lessons, 2 module overviews, 1 index)
Claude: Techniques used: Scenario-Based (5), Cautionary Tale (4), Analogy (3), Problem-Framing (3)
Claude: Ready for review!
```

---

**End of Specification**
