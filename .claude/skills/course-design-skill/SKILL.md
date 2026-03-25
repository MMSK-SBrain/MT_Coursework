---
name: course-design
description: Design high-quality vocational training courses through guided conversation with persistent storage of requirements and structured generation. Use when the user asks to create a course, design training, build a curriculum, or mentions course templates or Reynlab platform. Handles instructional design principles, learning outcomes hierarchy (CO→MO→SO), and Excel template generation for course import systems.
---

# Course Design Skill

Guide users through a structured yet conversational course design process, storing all inputs for reference, then generate a complete Excel template.

## Core Workflow

### 1. Initialize Project Structure

Create a folder for the course:
```
courses/{course-name-slug}/
├── 00-requirements.md      # All gathered requirements
├── 01-checklist.md         # Progress tracking
├── 02-course-structure.md  # Generated structure (optional)
└── 03-template.xlsx        # Final Excel template
```

### 2. Conversational Discovery

**Key Principles:**
- Ask 2-3 questions at a time, not all at once
- Save all inputs to requirements file as you go
- Update checklist to track progress
- Circle back to clarify incomplete information
- Apply instructional design principles throughout

**Discovery Phases:**

**Phase 1: Context & Audience**
- Course topic, industry/domain, duration
- Target learners, experience level, prerequisites
- Job role/aspiration after training

**Phase 2: Learning Outcomes** (Use Backward Design)
- What will learners be able to DO? (not just know)
- Critical vs nice-to-have skills
- Certification requirements (if any)

**Phase 3: Content Structure**
- Main modules/topics
- Logical sequencing
- Theory vs practice ratio
- Day-wise distribution

**Phase 4: Assessment Strategy**
- Assessment types (quiz, practical, project)
- Passing criteria
- Retake policy

**Phase 5: Constraints** (Optional but helpful)
- Equipment available
- Safety considerations
- Time or budget constraints

### 3. Generate Template

Once all requirements are gathered:
1. Review checklist for completeness
2. Summarize requirements to user for confirmation
3. Read the TEMPLATE_GUIDE.md for Excel format details
4. Generate the complete Excel template
5. Review with user and iterate

## Instructional Design Quick Reference

### Backward Design
Start with the end in mind:
1. What should learners DO? (outcomes)
2. How will we KNOW they can do it? (assessment)
3. What experiences will GET them there? (instruction)

### Bloom's Taxonomy Levels
```
Creating    ▲  Design, construct, develop
Evaluating  │  Assess, judge, recommend
Analyzing   │  Compare, examine, differentiate
Applying    │  Use, demonstrate, implement
Understanding │  Explain, describe, classify
Remembering ▼  List, identify, recall
```

**For vocational training:** Target Apply level or higher

### Cognitive Load Management
- Limit each lesson to 3-5 new concepts
- Break complex skills into sub-skills
- Introduce one concept at a time
- Use worked examples before practice

### Session Structure (Gagné's 9 Events)
1. Hook/attention grabber
2. State objectives
3. Recall prior knowledge
4. Present new content
5. Provide guidance/examples
6. Practice activity
7. Feedback
8. Assessment
9. Summary/transfer

### Spaced Practice
- Revisit key concepts across multiple days
- Interleave topics rather than blocking
- Include retrieval practice (quizzes)

## Learning Outcomes Hierarchy

The template uses a three-level hierarchy:

```
Course Outcome (CO)
├── Module Outcome (MO)
│   ├── Session Outcome (SO)
│   └── Session Outcome (SO)
└── Module Outcome (MO)
    └── ...
```

**Naming Convention:**
- CO IDs: `co-1`, `co-2`, `co-3`
- MO IDs: `mo-{module}-{seq}` (e.g., `mo-1-1`, `mo-2-1`)
- SO IDs: `so-{module}-{lesson}-{seq}` (e.g., `so-1-1-1`)

**Codes (human-readable):**
- CO Codes: `{COURSE}-CO-1` (e.g., `ECU-CO-1`)
- MO Codes: `{COURSE}-MO-1-1`
- SO Codes: `{COURSE}-SO-1-1-1`

## Domain-Specific Considerations

### Automotive/Mechanical Training
- Safety MUST come first (day 1)
- Tools before systems
- 70/30 practice-to-theory ratio is common
- Real equipment > simulations
- Emphasize troubleshooting methodology

### IT/Technology Training
- Hands-on lab time essential
- Version-specific vs conceptual balance
- Troubleshooting scenarios critical
- Documentation reading is a skill
- Technology changes fast - teach principles

### Manufacturing/Industrial
- Safety certifications may be mandatory
- Process compliance critical
- Quality standards explicit
- Equipment-specific procedures
- Assessment: Safety (100%), Process (70%), Quality checks

## File Templates

### Requirements File (00-requirements.md)

```markdown
# Course Requirements: {Course Name}

**Created:** {Date}
**Status:** {Gathering | Complete | Generating}

## 1. Course Context
- **Topic:**
- **Industry/Domain:**
- **Duration (Days):**
- **Description:**

## 2. Target Audience
- **Primary Learners:**
- **Experience Level:**
- **Prerequisites:**
- **Job Role:**

## 3. Learning Outcomes
### What learners will DO:
1.
2.

### Critical Skills:
-

### Nice-to-have:
-

## 4. Content Structure
### Main Modules:
1.

### Sequencing:
-

### Theory/Practice Ratio:
-

## 5. Assessment
- **Types:**
- **Passing Criteria:**

## 6. Constraints
- **Equipment:**
- **Safety:**
```

### Checklist File (01-checklist.md)

```markdown
# Course Design Checklist: {Course Name}

## Phase 1: Context & Audience
- [ ] Course topic defined
- [ ] Duration determined
- [ ] Target learners identified
- [ ] Prerequisites established

## Phase 2: Learning Outcomes
- [ ] 3-5 major capabilities defined
- [ ] Critical vs nice-to-have prioritized

## Phase 3: Content Structure
- [ ] Main modules identified
- [ ] Logical sequence confirmed
- [ ] Day-wise distribution planned

## Phase 4: Assessment
- [ ] Assessment types selected
- [ ] Passing criteria defined

## Phase 5: Generation
- [ ] COs drafted
- [ ] MOs created
- [ ] SOs created
- [ ] Template reviewed
- [ ] Final export
```

## Example Conversation Flow

**Opening:**
> I'd love to help you create this course! To design something effective, let's start with:
> 
> **Who will be taking this course?** Tell me about your learners - their background, goals, and starting point.

**After gathering context:**
> Let me summarize what I have so far:
> 
> | Aspect | Details |
> |--------|---------|
> | Learners | {summary} |
> | Duration | {days} |
> | Goal | {outcome} |
> 
> Before I sketch the structure, one more question:
> - **What's the theory vs practice balance?**

**Before generation:**
> Got it! Let me save this and propose a structure. Give me a moment to create your course files...

## Critical Rules

1. **Always create and update** the requirements and checklist files
2. **Reference TEMPLATE_GUIDE.md** when generating Excel templates
3. **Use active verbs** in outcome descriptions
4. **Match Bloom levels** to activities (Knowledge → Remember/Understand, Skills → Apply+)
5. **Validate hierarchy** - every MO needs a CO parent, every SO needs an MO parent
6. **Keep conversations focused** - 2-3 questions maximum per turn

## Resources

For detailed Excel template format, structure, and validation rules, see:
**references/TEMPLATE_GUIDE.md**
