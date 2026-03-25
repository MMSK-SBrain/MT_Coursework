# Course Import Template Guide

A comprehensive guide for filling out the Excel template to bulk-create courses with modules, lessons, and learning outcomes.

---

## Table of Contents

1. [Overview](#overview)
2. [Template Structure](#template-structure)
3. [Sheet 1: Course_Info](#sheet-1-course_info)
4. [Sheet 2: Outcomes_And_Structure](#sheet-2-outcomes_and_structure)
5. [The "Inherit From Above" Pattern](#the-inherit-from-above-pattern)
6. [Learning Outcomes Hierarchy](#learning-outcomes-hierarchy)
7. [Valid Values Reference](#valid-values-reference)
8. [Step-by-Step Example](#step-by-step-example)
9. [Do's and Don'ts](#dos-and-donts)
10. [Common Mistakes](#common-mistakes)
11. [Validation Rules](#validation-rules)

---

## Overview

This template allows you to define an entire course structure in a single Excel file:

- **Course metadata** (name, code, duration)
- **Modules** (logical groupings of related lessons)
- **Lessons** (daily teaching sessions)
- **Learning Outcomes** at three levels:
  - **Course Outcomes (CO)** - What students can do after completing the course
  - **Module Outcomes (MO)** - What students can do after completing a module
  - **Session Outcomes (SO)** - What students can do after a specific lesson
- **Sessions** (activities like lectures, quizzes, labs)

---

## Template Structure

The Excel file has two main sheets:

| Sheet | Purpose |
|-------|---------|
| `Course_Info` | Basic course metadata |
| `Outcomes_And_Structure` | Complete hierarchical structure |

There's also a `Reference` sheet with valid values for dropdowns.

---

## Sheet 1: Course_Info

This sheet contains basic course information in a two-column format.

### Format

| Field | Value |
|-------|-------|
| Course Name | [Your course name] |
| Course Code | [Unique code] |
| Duration (Days) | [Number] |
| Description | [Optional description] |
| Organization ID | [UUID from database] |

### Example

| Field | Value |
|-------|-------|
| Course Name | ECU Tuning & Diagnostics |
| Course Code | ECU |
| Duration (Days) | 5 |
| Description | Comprehensive course on Engine Control Unit programming and diagnostics for automotive technicians |
| Organization ID | a1b2c3d4-e5f6-7890-abcd-ef1234567890 |

### Field Requirements

| Field | Required | Rules |
|-------|----------|-------|
| Course Name | Yes | Any text, max 255 characters |
| Course Code | Yes | Unique within organization, uppercase, no spaces (e.g., ECU, HVS, BTF) |
| Duration (Days) | Yes | Positive integer, must match or exceed max lesson day |
| Description | No | Any text |
| Organization ID | Yes | Valid UUID from the database |

---

## Sheet 2: Outcomes_And_Structure

This is the main sheet containing the hierarchical course structure. It uses a wide format with many columns.

### Column Groups

The columns are organized into logical groups:

#### Module Columns (Define the module)
| Column | Description |
|--------|-------------|
| Module | Module sequence number (1, 2, 3...) |
| Module Name | Name of the module |
| Module Desc | Description of the module |

#### Lesson Columns (Define lessons within modules)
| Column | Description |
|--------|-------------|
| Lesson | Lesson sequence number within module (1, 2, 3...) |
| Lesson Name | Name of the lesson |
| Day | Which day of the course (1 to Duration) |

#### Course Outcome Columns (Top-level competencies)
| Column | Description |
|--------|-------------|
| CO ID | Unique identifier (e.g., co-1, co-2) |
| CO Code | Human-readable code (e.g., ECU-CO-1) |
| CO Desc | Description of the outcome |
| CO Category | Knowledge, Skill, or Attitude |
| CO Bloom | Bloom's Taxonomy level |

#### Module Outcome Columns (Module-level skills)
| Column | Description |
|--------|-------------|
| MO ID | Unique identifier (e.g., mo-1-1, mo-1-2) |
| MO Code | Human-readable code (e.g., ECU-MO-1-1) |
| MO Desc | Description of the outcome |
| MO Category | Knowledge, Skill, or Attitude |
| MO Bloom | Bloom's Taxonomy level |

#### Session Outcome Columns (Lesson-level objectives)
| Column | Description |
|--------|-------------|
| SO ID | Unique identifier (e.g., so-1-1-1) |
| SO Code | Human-readable code (e.g., ECU-SO-1-1-1) |
| SO Desc | Description of the outcome |
| SO Category | Knowledge, Skill, or Attitude |
| SO Bloom | Bloom's Taxonomy level |

#### Session Columns (Activities)
| Column | Description |
|--------|-------------|
| Session Type | lecture, quiz, lab, practical, or mixed |
| Required | Yes or No |

---

## The "Inherit From Above" Pattern

**This is the most important concept to understand.**

In the `Outcomes_And_Structure` sheet, empty cells inherit values from the row above. This allows you to define hierarchical data in a flat table format.

### How It Works

```
Row 1: [1] [Module 1] [Desc] [1] [Lesson 1] [1] [co-1] [...] [mo-1-1] [...] [so-1-1-1] [...] [lecture] [Yes]
       ↓     ↓         ↓     ↓      ↓       ↓    ↓            ↓             ↓
Row 2: [ ] [  empty  ] [ ]  [ ] [  empty ] [ ] [empty]  [empty]      [so-1-1-2] [...] [quiz]    [Yes]
       ↑ These empty cells INHERIT from Row 1
```

**Row 2 is interpreted as:**
- Module: 1 (inherited)
- Module Name: Module 1 (inherited)
- Lesson: 1 (inherited)
- Lesson Name: Lesson 1 (inherited)
- Day: 1 (inherited)
- CO ID: co-1 (inherited)
- MO ID: mo-1-1 (inherited)
- SO ID: so-1-1-2 (NEW - this row defines a new session outcome)
- Session Type: quiz (NEW)

### Visual Example

```
| Module | Module Name    | Lesson | Lesson Name     | Day | CO ID | MO ID   | SO ID     | Session Type |
|--------|----------------|--------|-----------------|-----|-------|---------|-----------|--------------|
| 1      | Intro to ECU   | 1      | ECU Basics      | 1   | co-1  | mo-1-1  | so-1-1-1  | lecture      |
|        |                |        |                 |     |       |         | so-1-1-2  | quiz         |  ← New SO, same everything else
|        |                |        |                 |     |       | mo-1-2  | so-1-2-1  | lecture      |  ← New MO, same module/lesson/CO
|        |                | 2      | ECU Software    | 2   |       |         | so-1-2-2  | lecture      |  ← New lesson, same module/CO/MO
| 2      | Diagnostics    | 1      | OBD-II Basics   | 3   | co-2  | mo-2-1  | so-2-1-1  | lab          |  ← New module starts fresh
```

### When to Leave Cells Empty

| Scenario | What to fill | What to leave empty |
|----------|--------------|---------------------|
| Adding a new SO to the same lesson | SO columns, Session columns | Module, Lesson, CO, MO columns |
| Adding a new MO to the same module/lesson | MO columns, SO columns, Session columns | Module, Lesson, CO columns |
| Adding a new lesson to the same module | Lesson columns, MO, SO, Session | Module columns, CO columns |
| Adding a new module | ALL columns | Nothing |

### When to Fill Cells

| Start a new... | Fill these columns |
|----------------|-------------------|
| Module | Module, Module Name, Module Desc (and all downstream) |
| Lesson | Lesson, Lesson Name, Day (and all downstream) |
| Course Outcome | CO ID, CO Code, CO Desc, CO Category, CO Bloom |
| Module Outcome | MO ID, MO Code, MO Desc, MO Category, MO Bloom |
| Session Outcome | SO ID, SO Code, SO Desc, SO Category, SO Bloom |
| Session | Session Type, Required |

---

## Learning Outcomes Hierarchy

Learning outcomes form a three-level hierarchy:

```
Course Outcome (CO)
└── What can the student DO after completing the COURSE?
    │
    ├── Module Outcome (MO)
    │   └── What can the student DO after completing this MODULE?
    │       │
    │       ├── Session Outcome (SO)
    │       │   └── What can the student DO after this LESSON?
    │       │
    │       └── Session Outcome (SO)
    │           └── What can the student DO after this LESSON?
    │
    └── Module Outcome (MO)
        └── ...
```

### Relationships

| Parent | Child | Relationship |
|--------|-------|--------------|
| Course | CO | A course has multiple course outcomes |
| CO | MO | Each CO is achieved through multiple MOs |
| MO | SO | Each MO is achieved through multiple SOs |
| Lesson | SO | A lesson can address multiple SOs |
| SO | Session | Each SO can be delivered/assessed via multiple sessions |

### ID Naming Convention

Use a consistent naming pattern for IDs:

| Level | Pattern | Examples |
|-------|---------|----------|
| Course Outcome | `co-{seq}` | co-1, co-2, co-3 |
| Module Outcome | `mo-{module}-{seq}` | mo-1-1, mo-1-2, mo-2-1 |
| Session Outcome | `so-{module}-{lesson}-{seq}` | so-1-1-1, so-1-1-2, so-1-2-1 |

### Code Naming Convention

Use course-prefixed codes for human readability:

| Level | Pattern | Examples |
|-------|---------|----------|
| Course Outcome | `{COURSE}-CO-{seq}` | ECU-CO-1, ECU-CO-2 |
| Module Outcome | `{COURSE}-MO-{module}-{seq}` | ECU-MO-1-1, ECU-MO-1-2 |
| Session Outcome | `{COURSE}-SO-{module}-{lesson}-{seq}` | ECU-SO-1-1-1, ECU-SO-1-1-2 |

---

## Valid Values Reference

### Categories

| Value | Description | Use When... |
|-------|-------------|-------------|
| Knowledge | Facts, concepts, theories | Student needs to remember/understand information |
| Skill | Practical abilities | Student needs to do something physical/procedural |
| Attitude | Values, mindsets, behaviors | Student needs to demonstrate professional behavior |

### Bloom's Taxonomy Levels

Listed from lowest to highest cognitive level:

| Level | Description | Example Verbs |
|-------|-------------|---------------|
| Remember | Recall facts | Define, list, identify, name, recall |
| Understand | Explain concepts | Explain, describe, summarize, interpret |
| Apply | Use in new situations | Apply, demonstrate, use, implement |
| Analyze | Break down, examine | Analyze, compare, contrast, examine |
| Evaluate | Make judgments | Evaluate, assess, judge, recommend |
| Create | Produce new work | Create, design, develop, construct |

### Session Types

| Type | Description | Use For... |
|------|-------------|------------|
| lecture | Instructor-led teaching | Theory, concepts, demonstrations |
| quiz | Written/digital assessment | Testing knowledge recall |
| lab | Hands-on practical work | Supervised skill practice |
| practical | Independent practical work | Skill demonstration/assessment |
| mixed | Combination of types | Complex sessions with multiple activities |

### Required Field

| Value | Meaning |
|-------|---------|
| Yes | Student must complete this session to pass |
| No | Optional session, not required for completion |

---

## Step-by-Step Example

Let's create a 3-day course on "Battery Safety" with proper structure.

### Step 1: Fill Course_Info

| Field | Value |
|-------|-------|
| Course Name | Battery Safety & Handling |
| Course Code | BSH |
| Duration (Days) | 3 |
| Description | Essential safety training for handling high-voltage batteries |
| Organization ID | your-org-uuid-here |

### Step 2: Plan Your Structure

Before filling the sheet, plan:

```
Module 1: Battery Fundamentals (Day 1)
  - Lesson 1.1: Battery Chemistry Basics
    - SO: Identify battery types
    - SO: Explain energy storage
  - Lesson 1.2: Voltage & Current
    - SO: Measure battery voltage

Module 2: Safety Protocols (Day 2-3)
  - Lesson 2.1: PPE Requirements
    - SO: Select appropriate PPE
  - Lesson 2.2: Emergency Procedures
    - SO: Execute emergency shutdown
    - SO: Perform first aid
```

### Step 3: Define Course Outcomes

What can students do after completing the entire course?

- CO-1: Safely handle high-voltage batteries (Skill, Apply)
- CO-2: Respond to battery emergencies (Skill, Apply)

### Step 4: Fill the Sheet

Here's the complete `Outcomes_And_Structure` sheet:

```
| Module | Module Name          | Module Desc                           | Lesson | Lesson Name          | Day | CO ID | CO Code  | CO Desc                              | CO Cat    | CO Bloom  | MO ID   | MO Code    | MO Desc                           | MO Cat    | MO Bloom  | SO ID      | SO Code      | SO Desc                          | SO Cat    | SO Bloom  | Session Type | Required |
|--------|----------------------|---------------------------------------|--------|----------------------|-----|-------|----------|--------------------------------------|-----------|-----------|---------|------------|-----------------------------------|-----------|-----------|------------|--------------|----------------------------------|-----------|-----------|--------------|----------|
| 1      | Battery Fundamentals | Understanding battery basics          | 1      | Battery Chemistry    | 1   | co-1  | BSH-CO-1 | Safely handle high-voltage batteries | Skill     | Apply     | mo-1-1  | BSH-MO-1-1 | Identify battery types and specs  | Knowledge | Remember  | so-1-1-1   | BSH-SO-1-1-1 | Identify common battery types    | Knowledge | Remember  | lecture      | Yes      |
|        |                      |                                       |        |                      |     |       |          |                                      |           |           |         |            |                                   |           |           | so-1-1-2   | BSH-SO-1-1-2 | Explain energy storage principle | Knowledge | Understand| lecture      | Yes      |
|        |                      |                                       |        |                      |     |       |          |                                      |           |           |         |            |                                   |           |           |            |              |                                  |           |           | quiz         | Yes      |
|        |                      |                                       | 2      | Voltage & Current    | 1   |       |          |                                      |           |           | mo-1-2  | BSH-MO-1-2 | Measure electrical properties     | Skill     | Apply     | so-1-2-1   | BSH-SO-1-2-1 | Measure battery voltage safely   | Skill     | Apply     | lecture      | Yes      |
|        |                      |                                       |        |                      |     |       |          |                                      |           |           |         |            |                                   |           |           |            |              |                                  |           |           | lab          | Yes      |
| 2      | Safety Protocols     | Critical safety procedures            | 1      | PPE Requirements     | 2   | co-2  | BSH-CO-2 | Respond to battery emergencies       | Skill     | Apply     | mo-2-1  | BSH-MO-2-1 | Select and use PPE correctly      | Skill     | Apply     | so-2-1-1   | BSH-SO-2-1-1 | Select appropriate PPE           | Skill     | Apply     | lecture      | Yes      |
|        |                      |                                       |        |                      |     |       |          |                                      |           |           |         |            |                                   |           |           |            |              |                                  |           |           | practical    | Yes      |
|        |                      |                                       | 2      | Emergency Procedures | 3   |       |          |                                      |           |           | mo-2-2  | BSH-MO-2-2 | Execute emergency protocols       | Skill     | Apply     | so-2-2-1   | BSH-SO-2-2-1 | Execute emergency shutdown       | Skill     | Apply     | lab          | Yes      |
|        |                      |                                       |        |                      |     |       |          |                                      |           |           |         |            |                                   |           |           | so-2-2-2   | BSH-SO-2-2-2 | Perform first aid for shocks     | Skill     | Apply     | practical    | Yes      |
```

### Reading the Example

**Row 1:**
- Creates Module 1, Lesson 1
- Creates CO-1 (Safely handle batteries)
- Creates MO-1-1 (Identify battery types)
- Creates SO-1-1-1 (Identify common types)
- Creates a lecture session

**Row 2:**
- Same Module 1, Lesson 1, CO-1, MO-1-1 (all inherited - cells empty)
- Creates new SO-1-1-2 (Explain energy storage)
- Creates a lecture session

**Row 3:**
- Same everything (all inherited)
- No new SO (SO columns empty)
- Creates a quiz session for SO-1-1-2 (the last SO from context)

**Row 4:**
- Same Module 1 (inherited)
- Creates new Lesson 2 (Voltage & Current)
- Same CO-1 (inherited)
- Creates new MO-1-2 (Measure electrical properties)
- Creates SO-1-2-1
- Creates a lecture session

---

## Do's and Don'ts

### DO's

| Do | Why |
|----|-----|
| Use consistent ID patterns | Makes tracking and debugging easier |
| Start each module on a new row with all fields filled | Ensures clean hierarchy |
| Plan your structure before filling | Reduces errors and rework |
| Use active verbs in outcome descriptions | Makes outcomes measurable |
| Match Bloom levels to the activity | Knowledge outcomes need Remember/Understand, Skills need Apply+ |
| Run dry-run before actual import | Catches errors without database changes |
| Keep outcome descriptions concise | Max 500 characters, be specific |
| Use the course code as prefix in outcome codes | Makes codes globally unique and traceable |

### DON'TS

| Don't | Why |
|-------|-----|
| Don't leave SO ID empty if you want a new session outcome | Empty SO means inherit from above |
| Don't create orphan MOs without a parent CO | Validation will fail |
| Don't create orphan SOs without a parent MO | Validation will fail |
| Don't use Day numbers > Duration | Validation will fail |
| Don't duplicate IDs within the same level | co-1 can only appear once |
| Don't duplicate codes within the same level | BSH-CO-1 can only appear once |
| Don't use Session Type without an SO context | Every session must have an associated SO |
| Don't skip sequence numbers | Use 1, 2, 3 not 1, 3, 5 |
| Don't use special characters in IDs | Stick to letters, numbers, and hyphens |
| Don't mix up ID and Code columns | ID is internal (co-1), Code is display (BSH-CO-1) |

---

## Common Mistakes

### Mistake 1: Forgetting to Inherit

**Wrong:**
```
| Module | Module Name | Lesson | Lesson Name | SO ID     |
|--------|-------------|--------|-------------|-----------|
| 1      | Intro       | 1      | Basics      | so-1-1-1  |
| 1      | Intro       | 1      | Basics      | so-1-1-2  |  ← Filled unnecessarily
```

**Correct:**
```
| Module | Module Name | Lesson | Lesson Name | SO ID     |
|--------|-------------|--------|-------------|-----------|
| 1      | Intro       | 1      | Basics      | so-1-1-1  |
|        |             |        |             | so-1-1-2  |  ← Empty cells inherit
```

### Mistake 2: Missing Parent Outcome

**Wrong:**
```
| CO ID | MO ID   | MO Desc            |
|-------|---------|-------------------|
|       | mo-1-1  | Some skill        |  ← No CO defined, MO has no parent!
```

**Correct:**
```
| CO ID | CO Desc              | MO ID   | MO Desc            |
|-------|----------------------|---------|-------------------|
| co-1  | Main competency      | mo-1-1  | Some skill        |  ← MO inherits co-1 as parent
```

### Mistake 3: Invalid Bloom Level

**Wrong:**
```
| SO Bloom  |
|-----------|
| Memorize  |  ← Not a valid Bloom level!
```

**Correct:**
```
| SO Bloom  |
|-----------|
| Remember  |  ← Correct Bloom level
```

### Mistake 4: Day Exceeds Duration

If your course is 3 days:

**Wrong:**
```
| Day |
|-----|
| 5   |  ← Exceeds 3-day duration!
```

**Correct:**
```
| Day |
|-----|
| 3   |  ← Within duration
```

### Mistake 5: Duplicate IDs

**Wrong:**
```
| MO ID   |
|---------|
| mo-1-1  |
| mo-1-1  |  ← Duplicate!
```

**Correct:**
```
| MO ID   |
|---------|
| mo-1-1  |
| mo-1-2  |  ← Unique
```

### Mistake 6: Session Without Context

**Wrong:**
```
| SO ID | Session Type |
|-------|--------------|
|       | quiz         |  ← No SO defined or inherited!
```

**Correct:**
```
| SO ID     | Session Type |
|-----------|--------------|
| so-1-1-1  | lecture      |  ← SO defined
|           | quiz         |  ← Inherits so-1-1-1 from above
```

---

## Validation Rules

The import tool validates these rules. All errors are reported at once.

### Course Info Validation

| Rule | Error if violated |
|------|-------------------|
| Course Name is required | "Course Name is required" |
| Course Code is required | "Course Code is required" |
| Duration must be positive | "Duration must be a positive number" |
| Organization ID is required | "Organization ID is required" |
| Course Code must be unique | "Course with code X already exists" |
| Organization must exist | "Organization with ID X not found" |

### Structure Validation

| Rule | Error if violated |
|------|-------------------|
| Day must be ≤ Duration | "Lesson X has day Y which exceeds duration" |
| Day must be ≥ 1 | "Lesson X has invalid day Y" |

### Outcome Validation

| Rule | Error if violated |
|------|-------------------|
| MO must reference existing CO | "Module Outcome X references undefined Course Outcome Y" |
| SO must reference existing MO | "Session Outcome X references undefined Module Outcome Y" |
| No duplicate CO IDs | "Duplicate Course Outcome ID: X" |
| No duplicate MO IDs | "Duplicate Module Outcome ID: X" |
| No duplicate SO IDs | "Duplicate Session Outcome ID: X" |
| No duplicate CO Codes | "Duplicate Course Outcome code: X" |
| No duplicate MO Codes | "Duplicate Module Outcome code: X" |
| No duplicate SO Codes | "Duplicate Session Outcome code: X" |
| Category must be valid | "Invalid Category: X. Valid: Knowledge, Skill, Attitude" |
| Bloom must be valid | "Invalid Bloom Level: X. Valid: Remember, Understand, ..." |
| Session Type must be valid | "Invalid Session Type: X. Valid: lecture, quiz, ..." |

### Warnings (Non-blocking)

| Condition | Warning |
|-----------|---------|
| No Course Outcomes defined | "Consider adding at least one course-level outcome" |
| Module has no lessons | "Module X has no lessons defined" |
| SO has no quiz session | "Session Outcome X has no quiz session for formal assessment" |

---

## Quick Reference Card

### Outcome Hierarchy
```
CO (Course) → MO (Module) → SO (Session) → Sessions
```

### ID Patterns
```
co-{n}           → co-1, co-2
mo-{mod}-{n}     → mo-1-1, mo-1-2, mo-2-1
so-{mod}-{les}-{n} → so-1-1-1, so-1-2-1
```

### Valid Categories
```
Knowledge | Skill | Attitude
```

### Valid Bloom Levels
```
Remember | Understand | Apply | Analyze | Evaluate | Create
```

### Valid Session Types
```
lecture | quiz | lab | practical | mixed
```

### Empty Cell Rule
```
Empty cell = Use value from the row above
```

---

## Checklist Before Import

Before running the import, verify:

- [ ] Course_Info sheet has all required fields
- [ ] Course Code is unique (not already in database)
- [ ] Organization ID is valid
- [ ] All days are within course duration
- [ ] Every MO has a CO defined above it
- [ ] Every SO has a MO defined above it
- [ ] No duplicate IDs at any level
- [ ] All Bloom levels are spelled correctly
- [ ] All Categories are spelled correctly
- [ ] All Session Types are spelled correctly
- [ ] Run `--dry-run` first to validate

---

## Getting Help

If you encounter issues:

1. Check the error message - it includes row numbers
2. Verify the row against this guide
3. Run with `--dry-run` to get a full validation report
4. All errors are reported at once - fix them all before re-importing

For questions about the platform, consult the main project documentation.
