import { mkdtempSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import ExcelJS from "exceljs";
import { describe, expect, it } from "vitest";
import { blocksFromFramework, blocksFromTimed } from "../src/blocks.js";
import { detectDialect, parseSeYaml, parseVehiclesYaml, parseWeeksYaml } from "../src/parsers/courseYaml.js";
import { parseFramework, parseFrontMatter, parseObjectives, parseTimedTemplates } from "../src/parsers/framework.js";
import { parseHandout } from "../src/parsers/handout.js";
import { parseInfoRows, parseOutcomeRows, readModuleTemplate } from "../src/parsers/xlsx.js";
import { inferBloom } from "../src/util.js";

const NOW = "2026-11-04T00:00:00.000Z";

const HANDOUT_517 = `

Birla Institute of Technology & Science, Pilani
Work Integrated Learning Programmes Division
M.Tech. Automotive Engineering/Electronics
Digital Learning Handout
Part A: Content Design
Course Title
AUTOMOTIVE SYSTEMS ENGINEERING
Course No(s)
AE ZG517 / AEL ZG517
Credit Units

Credit Model
32-0-0
 (XX Hours of Class-room Instruction)
Instructors
SAJEETH KUMAR
Version No:
6.2
Date:
12-Jan-2025
Course Description:

Course Objectives
No
Course Objective
CO1
Introduce hard and soft skills
CO2
Impart the knowledge about foundations
CO3
Help engineers to learn
CO4

CO5


Text Book(s):
T1
Systems Engineering Handbook, 4th Edition, 2015.

T2


Reference Book(s) & other resources:
R1
Systems Engineering and Analysis, Blanchard
R2
Automotive Systems Engineering, Maurer
R3

Learning Outcomes: Students will be able to
LO1
Describe processes, methods, and practices of systems engineering
LO2
Develop requirements, architectures, specifications, verifications, and tests

Part B: Learning Plan
Contact Session
List of Topic Title
Sub-Topics
Reference
1
Introduction to Systems Engineering
- Engineering failures case studies  - Importance of systems engineering in avoiding failures

2
Systems Engineering Fundamentals
- INCOSE definition  - Systems thinking  - ISO/IEC 15288 life cycle processes

Experiential Learning Components:
`;

describe("handout .txt parser", () => {
  const h = parseHandout(HANDOUT_517);
  it("reads the header fields", () => {
    expect(h.title).toBe("AUTOMOTIVE SYSTEMS ENGINEERING");
    expect(h.courseNos).toBe("AE ZG517 / AEL ZG517");
    expect(h.creditModel).toBe("32-0-0");
    expect(h.version).toBe("6.2");
    expect(h.date).toBe("12-Jan-2025");
    expect(h.programme).toBe("M.Tech. Automotive Engineering/Electronics");
  });
  it("keeps filled COs and reports the empty ones", () => {
    expect(h.objectives.map((o) => o.id)).toEqual(["CO1", "CO2", "CO3"]);
    expect(h.emptyObjectiveIds).toEqual(["CO4", "CO5"]);
  });
  it("reads books and outcomes, dropping empty rows", () => {
    expect(h.textbooks).toEqual([{ id: "T1", text: "Systems Engineering Handbook, 4th Edition, 2015." }]);
    expect(h.references.map((r) => r.id)).toEqual(["R1", "R2"]);
    expect(h.outcomes[1]).toEqual({ id: "LO2", text: "Develop requirements, architectures, specifications, verifications, and tests" });
  });
  it("splits the dash-separated sub-topics of Part B", () => {
    expect(h.sessions).toHaveLength(2);
    expect(h.sessions[0]).toMatchObject({ number: 1, title: "Introduction to Systems Engineering" });
    expect(h.sessions[1]!.subTopics).toEqual(["INCOSE definition", "Systems thinking", "ISO/IEC 15288 life cycle processes"]);
  });
  it("reads the bullet layout of the AEZC516 handout", () => {
    const h2 = parseHandout(`Part B: Learning Plan
Contact Session
List of Topic Title
Sub-Topics
Reference
1
Emissions
\t•\tPollution formation, Nox, CO, HC,PM
Class Notes

2
Exhaust gas after treatment
\t•\t Catalytic converter , Particulate Traps
T1: Chapter: **
Section: **
16
Buffer Session

Class Notes
Experiential Learning Components:
`);
    expect(h2.sessions.map((s) => s.title)).toEqual(["Emissions", "Exhaust gas after treatment", "Buffer Session"]);
    expect(h2.sessions[0]!.subTopics).toEqual(["Pollution formation, Nox, CO, HC,PM"]);
    expect(h2.sessions[1]!.reference).toBeUndefined();
  });
});

describe("course-data.yaml dialects", () => {
  const SE = `
course: { title: "Automotive Systems Engineering", short_code: "AEZC517", credit_model: "32-0-0" }
objectives:
  - { id: CO1, description: "Introduce hard skills" }
learning_outcomes:
  - { id: LO1, description: "Describe processes", level: "Understand" }
modules:
  - { number: 1, title: "Foundations", sessions: [1, 2] }
sessions:
  - number: 1
    title: "Intro"
    duration: 120
    approach: "Story-Based"
    topics: ["Failures", "Systems"]
    learning_outcomes: ["LO1"]
`;
  const VEH = `
course: { name: "Automotive Vehicles", code: AELZC441, total_sessions: 20 }
course_outcomes:
  - { id: co-1, description: "Study components", bloom_level: Understand }
modules:
  - number: 1
    name: Motion
    module_outcome: { id: mo-1, description: "Apply physics", bloom_level: Apply, parent_co: co-3 }
    lessons:
      - number: 1
        name: Forces
        session_outcomes:
          - { id: so-1-1-1, code: AELZC441-SO-1-1-1, description: "Apply Newton's laws", bloom_level: Apply, session_type: lecture }
`;
  const WK = `
course: { title: "TUV", code: TUV-AST, total_hours: 165 }
weeks:
  - number: 1
    title: "Meet the Machine"
    days:
      - { day: 1, theme: "The Car", theory_practice: "40:60", topics: ["Systems"] }
`;
  it("detects the dialect", () => {
    expect(detectDialect(SE)).toBe("systems-engineering");
    expect(detectDialect(VEH)).toBe("vehicles");
    expect(detectDialect(WK)).toBe("weeks");
    expect(detectDialect("a: 1")).toBeNull();
  });
  it("parses the systems-engineering layout", () => {
    const y = parseSeYaml(SE);
    expect(y.shortCode).toBe("AEZC517");
    expect(y.modules[0]).toMatchObject({ number: 1, sessions: [1, 2] });
    expect(y.sessions[0]).toMatchObject({ duration: 120, learningOutcomes: ["LO1"], topics: ["Failures", "Systems"] });
    expect(y.outcomes[0]!.level).toBe("Understand");
  });
  it("parses the vehicles layout", () => {
    const y = parseVehiclesYaml(VEH);
    expect(y.courseOutcomes[0]).toMatchObject({ id: "co-1", bloom: "Understand" });
    expect(y.modules[0]!.moduleOutcome!.parentCo).toEqual(["co-3"]);
    expect(y.modules[0]!.lessons[0]!.outcomes[0]).toMatchObject({ code: "AELZC441-SO-1-1-1", sessionType: "lecture" });
  });
  it("parses the weeks layout", () => {
    const y = parseWeeksYaml(WK);
    expect(y.totalHours).toBe(165);
    expect(y.weeks[0]!.days[0]).toMatchObject({ day: 1, theoryPractice: "40:60", topics: ["Systems"] });
  });
});

describe("xlsx module template", () => {
  const header = ["Module", "Module Name", "Module Desc", "Lesson", "Lesson Name", "Day", "CO ID", "CO Code", "CO Desc", "CO Category", "CO Bloom",
    "MO ID", "MO Code", "MO Desc", "MO Category", "MO Bloom", "SO ID", "SO Code", "SO Desc", "SO Category", "SO Bloom", "Session Type", "Required"];
  const row = (o: Record<string, string>) => header.map((h) => o[h]);
  const rows = [
    header,
    row({ Module: "1", "Module Name": "Foundations", Lesson: "1", "Lesson Name": "Build", Day: "1", "CO ID": "co-1", "CO Desc": "Analyze engines", "MO ID": "mo-1-1", "MO Desc": "Analyze choices", "SO ID": "so-1-1-1", "SO Desc": "Analyze architecture", "SO Bloom": "Analyze", "Session Type": "lecture", Required: "Yes" }),
    row({ "SO ID": "so-1-1-2", "SO Desc": "Calculate BMEP", "SO Bloom": "Apply" }),
    row({ Module: "2", "Module Name": "Performance", Lesson: "2", "Lesson Name": "Breathing", "SO ID": "so-2-2-1", "SO Desc": "Explain VVT" }),
    row({ Module: "3", "Module Name": "Air", Lesson: "3", "Lesson Name": "Boost", "CO ID": "co-2", "CO Desc": "Design intake", "SO ID": "so-3-3-1", "SO Desc": "Design turbo" }),
  ];
  it("fills blank cells down: lessons own their SOs and modules inherit the CO in force", () => {
    const t = parseOutcomeRows(rows);
    expect(t.modules.map((m) => [m.number, m.coId])).toEqual([[1, "co-1"], [2, "co-1"], [3, "co-2"]]);
    expect(t.modules[0]!.lessons[0]!.outcomes.map((o) => o.id)).toEqual(["so-1-1-1", "so-1-1-2"]);
    expect(t.modules[0]!.lessons[0]!.moId).toBe("mo-1-1");
    expect(t.cos["co-2"]!.description).toBe("Design intake");
    expect(t.mos["mo-1-1"]!.moduleNumber).toBe(1);
  });
  it("reads Course_Info", () => {
    expect(parseInfoRows([["Field", "Value"], ["Course Name", "Advances in IC Engines"], ["Course Code", "AEZG516"], ["Duration (Days)", "15"]])).toEqual({ name: "Advances in IC Engines", code: "AEZG516", days: 15, description: undefined });
  });
  it("reads a real .xlsx file", async () => {
    const wb = new ExcelJS.Workbook();
    wb.addWorksheet("Course_Info").addRows([["Field", "Value"], ["Course Name", "X"], ["Course Code", "C1"]]);
    wb.addWorksheet("Outcomes_And_Structure").addRows(rows);
    const p = join(mkdtempSync(join(tmpdir(), "cg-xlsx-")), "t.xlsx");
    await wb.xlsx.writeFile(p);
    const t = await readModuleTemplate(p);
    expect(t.info.code).toBe("C1");
    expect(t.modules).toHaveLength(3);
    expect(t.modules[0]!.lessons[0]!.outcomes).toHaveLength(2);
  });
});

const ARC = `---
duration_minutes: 180
week_number: 1
---
# Day 1: The Car
**Duration:** 180 minutes (70 min theory + 110 min practical)
**Approach:** Discovery-Based

## 🎯 Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Name and locate all **major** vehicle systems
- Decode a Vehicle Identification Number (VIN)

**This is Day 1.**

### **SETUP: Welcome** (Slides 1-5, ~15 minutes)
### **DEVELOPMENT PART 1: Tour** (Slides 6-17, ~55 minutes)
### **PRACTICAL: Walkthrough** (Slides 18-20, ~70 minutes)
### **WRAP-UP** (Slides 21-22, ~15 minutes)
### **PART 2: TRIGGER** - "Alignment" (Slides 10-14, ~15 min)
### Timing Breakdown (120 minutes total):
`;

describe("lecture framework parser", () => {
  const fw = parseFramework(ARC);
  it("reads front matter and header", () => {
    expect(parseFrontMatter(ARC)).toMatchObject({ duration_minutes: "180" });
    expect(fw.durationMin).toBe(180);
    expect(fw.approach).toBe("Discovery-Based");
  });
  it("reads session objectives and strips markdown", () => {
    expect(parseObjectives(ARC)).toEqual(["Name and locate all major vehicle systems", "Decode a Vehicle Identification Number (VIN)"]);
  });
  it("reads phases with and without a colon, and ignores the timing summary", () => {
    expect(fw.phases.map((p) => [p.name, p.minutes, p.slides])).toEqual([
      ["SETUP", 15, "1-5"], ["DEVELOPMENT PART 1", 55, "6-17"], ["PRACTICAL", 70, "18-20"], ["WRAP-UP", 15, "21-22"], ["PART 2", 15, "10-14"],
    ]);
    expect(fw.phases[3]!.title).toBe("WRAP-UP");
  });
  it("understands \"90 minutes lecture + 30 minutes Q&A\"", () => {
    const f = parseFramework("**Duration:** 90 minutes lecture + 30 minutes Q&A\n### **SETUP: A** (Slides 1-2, ~90 minutes)\n");
    expect(f.durationMin).toBe(120);
    expect(f.qaMin).toBe(30);
  });
});

describe("hour blocks", () => {
  it("lays phases end to end and splits at the hour boundary", () => {
    const fw = parseFramework("### **SETUP: A** (Slides 1-2, ~45 minutes)\n### **RISING ACTION: B** (Slides 3-4, ~30 minutes)\n### **PRACTICAL: C** (Slides 5-6, ~45 minutes)\n");
    const b = blocksFromFramework("S1", fw, "teaching", NOW);
    expect(b.map((x) => [x.hour, x.startMin, x.minutes, x.kind])).toEqual([[1, 0, 45, "hook"], [1, 45, 15, "teach"], [2, 0, 15, "teach"], [2, 15, 45, "activity"]]);
    expect(b[3]!.style).toBe("lab");
    expect(b[0]!.provenance.model).toBe("import");
  });
  it("adds the stated Q&A as a closing block", () => {
    const fw = parseFramework("**Duration:** 90 minutes lecture + 30 minutes Q&A\n### **SETUP: A** (Slides 1-2, ~90 minutes)\n");
    const b = blocksFromFramework("S1", fw, "teaching", NOW);
    expect(b.at(-1)).toMatchObject({ hour: 2, startMin: 30, minutes: 30, title: "Q&A" });
  });
  it("parses minute-range session templates, including timed MCQ bullets", () => {
    const md = `### SESSION 1: Build Your Engine (90 min)

**Learning Outcomes:** SO-1-1-1, SO-1-1-2

**Hook [0-5 min]:**
- Show three engines

**Part 1: Architecture [5-30 min]:**
- Cylinders
- **MCQ #1 [30-32 min]:** Displacement question

**Wrap-up [32-35 min]:**
- Takeaways

**Materials Needed:**
- Slides
`;
    const [s] = parseTimedTemplates(md);
    expect(s).toMatchObject({ number: 1, title: "Build Your Engine", minutes: 90, outcomeIds: ["SO-1-1-1", "SO-1-1-2"] });
    expect(s!.blocks.map((b) => [b.title, b.startMin, b.endMin])).toEqual([["Hook", 0, 5], ["Part 1: Architecture", 5, 30], ["MCQ #1", 30, 32], ["Wrap-up", 32, 35]]);
    expect(s!.blocks[0]!.text).toBe("Show three engines");
    const blocks = blocksFromTimed("S1", s!, "teaching", NOW);
    expect(blocks.map((b) => b.kind)).toEqual(["hook", "teach", "check", "wrap"]);
  });
});

describe("Bloom inference", () => {
  it("reads the leading verb", () => {
    expect(inferBloom("Describe the V-model").bloom).toBe("understand");
    expect(inferBloom("Calculate rolling resistance").bloom).toBe("apply");
    expect(inferBloom("Apply Newton's laws").bloom).toBe("apply");
    expect(inferBloom("Develop requirements and tests").bloom).toBe("create");
    expect(inferBloom("Differentiate between swirl and tumble").bloom).toBe("analyse");
    expect(inferBloom("Safely isolate the battery").how).toBe("default");
  });
  it("falls back to the stated level, then to understand", () => {
    expect(inferBloom("Frobnicate the widget", "Analyze")).toEqual({ bloom: "analyse", how: "stated" });
    expect(inferBloom("Frobnicate the widget")).toEqual({ bloom: "understand", how: "default" });
  });
});
