# Session 9: Project and Risk Management
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 120 minutes (90 minutes lecture + 30 minutes discussion/Q&A)
**Approach:** Story-Based with Real-World Project Management and Risk Cases
**PPT Target:** 28-30 slides

---

## 🎯 Session Objectives (For Instructor)

By the end of this session, students will be able to:
- Understand the relationship between systems engineering and project management
- Apply technical planning processes to systems engineering projects
- Identify, assess, and manage risks in automotive systems projects
- Develop project schedules and work breakdown structures for SE projects
- Apply risk management frameworks to automotive systems development
- Understand opportunity management and resilience thinking

**Learning Outcomes Addressed:**
- **LO1:** Describe processes, methods, and practices of systems engineering (Understand/Apply)
- **LO2:** Apply systems engineering processes to automotive systems (Apply)
- **LO3:** Recognize important systems engineering and systems thinking strategies and practices (Understand/Apply)

---

## 🔗 Connection to Prior Knowledge

Building from Sessions 1-8:
- **Session 1-2:** Systems thinking and SE fundamentals provide the foundation
- **Session 4:** Requirements engineering flows into project planning
- **Session 5:** System architecture influences project structure
- **Session 7:** Functional analysis informs work breakdown structure
- **Session 8:** Integration and verification planning are key project elements

**Bridge:** "You've learned to engineer systems. Now we learn to manage the engineering process and risks."

---

## 📖 INSTRUCTOR-LED STORY ARC

### **SETUP: When Projects Go Wrong** (Slides 1-8, ~20 minutes)

**Narrative Voice:** Direct, establishing the criticality of project and risk management

---

#### Slide 1: Title Slide
**Visual:** Professional title slide with project timeline/Gantt chart overlay and risk matrix imagery

**Instructor Narration:**
> "Welcome to Session 9. Today we're talking about project management and risk management. And I know what some of you are thinking: 'This is a technical course. Why are we talking about management?'
>
> Here's why: **The best technical solution in the world is worthless if the project fails, runs out of money, misses deadlines, or encounters unforeseen risks that destroy the program.** Technical excellence and management excellence must go together. Today, you'll learn how."

**PPT Content:**
```
AUTOMOTIVE SYSTEMS ENGINEERING
AE ZG517 / AEL ZG517
Session 9: Project and Risk Management

Instructor: Sajeeth Kumar
Duration: 120 minutes

"Technical brilliance without project discipline = failure"
```

**Learning Outcomes:** Setting context for LO1, LO2, LO3

---

#### Slide 2: The Management Paradox
**Visual:** Split image showing technical work vs management overhead, with failure examples

**Instructor Narration:**
> "Engineering students often see project management as overhead. As bureaucracy getting in the way of real engineering work. But here's the paradox:
>
> **Without management discipline, your technical work never sees the light of day.** The Denver Airport baggage system? Brilliant technical design. Project management disaster. $560 million over budget, 16 months late, and eventually scrapped.
>
> The Boeing 787 Dreamliner? Revolutionary aircraft. But poor supplier project management led to 3-year delays and $50 billion in losses.
>
> **Today's lesson: Project and risk management are not overhead. They're how you ensure your technical work succeeds.**"

**PPT Content:**
```
The Project Management Paradox:

PERCEPTION:
• Project management = bureaucracy
• Takes time away from "real" engineering
• Unnecessary overhead

REALITY:
• Poor PM destroys technical excellence
• Risk management prevents disasters
• Planning enables execution

EXAMPLES OF PM FAILURES:
• Denver Airport Baggage: $560M over budget, scrapped
• Boeing 787: 3-year delay, $50B in losses
• Sydney Opera House: 10 years late, 14x over budget

→ Technical skills + Management discipline = Success
```

**Learning Outcomes:** LO3 - Understanding SE management criticality

---

#### Slide 3: Case Study Teaser - Mars Climate Orbiter
**Visual:** Image of Mars Climate Orbiter and mission failure

**Instructor Narration:**
> "September 23, 1999. NASA's Mars Climate Orbiter approaches Mars after a 9-month journey. It enters the atmosphere to begin orbital insertion. And then... nothing. Silence. The spacecraft is lost.
>
> The cause? A units conversion error. One team used metric. Another used imperial. Nobody caught it. Cost: $327.6 million. Completely preventable with basic project management and risk controls.
>
> But here's the deeper question: This wasn't just a technical error. It was a **project management failure**. No interface control document. No verification of assumptions. No risk review that caught the units mismatch. The systems engineering processes existed on paper. The project management failed to ensure they were followed.
>
> Keep this in mind as we explore project and risk management today."

**PPT Content:**
```
CASE STUDY: Mars Climate Orbiter Loss

INCIDENT (Sept 23, 1999):
• $327.6 million spacecraft lost
• Entered Mars atmosphere too low
• Burned up or skipped into space
• Root cause: Units conversion error (metric vs imperial)

THE PROJECT MANAGEMENT FAILURES:
✗ No interface control verification
✗ Inadequate communication between teams
✗ Risk of units mismatch not identified
✗ No independent verification checkpoint
✗ Assumptions not documented or validated

LESSON:
"Technical error, but fundamentally a project management
and risk management failure."

→ Brilliant engineering destroyed by poor management
```

**Learning Outcomes:** LO1, LO3 - PM/RM failures

---

#### Slide 4: Today's Learning Journey
**Visual:** Flow diagram showing session structure

**Instructor Narration:**
> "Here's our journey today. We'll start by understanding the relationship between systems engineering and project management—they're partners, not competitors.
>
> Then we dive into **technical planning**—how to plan SE projects, create work breakdown structures, develop schedules, and allocate resources.
>
> Next, we explore **risk management**—identifying, assessing, treating, and monitoring risks throughout the system lifecycle.
>
> Finally, we bring it together with **automotive applications**—how this applies to your real-world vehicle development programs.
>
> By the end, you'll understand that project and risk management aren't overhead—they're essential SE practices."

**PPT Content:**
```
Today's Journey:

1. SE & Project Management (15 min)
   • Relationship and integration
   • Technical planning vs program management

2. Technical Planning Processes (25 min)
   • Work breakdown structures
   • Scheduling and resource allocation
   • Project assessment and control

3. Risk Management (30 min)
   • Risk identification and analysis
   • Risk treatment and monitoring
   • Opportunity management

4. Automotive Applications (15 min)
   • Vehicle development programs
   • Integration with APQP/VDA-RGA

5. Discussion & Q&A (15 min)

Goal: Master project and risk management as SE practices
```

**Learning Outcomes:** LO1, LO2

---

#### Slide 5: Ground Rules for Technical Management
**Visual:** Simple text slide with guiding principles

**Instructor Narration:**
> "Before we begin, three ground rules:
>
> **First**, we're focusing on *technical planning and management*, not general program management. This is about managing the SE work—requirements, design, integration—not HR or procurement.
>
> **Second**, these aren't theoretical frameworks. We'll tie everything to ISO/IEC 15288 and automotive industry standards like APQP and VDA.
>
> **Third**, think about how these practices would have prevented the failures we've studied—Apollo 13, Therac-25, Toyota, Mars Orbiter. Management discipline prevents technical disasters.
>
> Ready? Let's build your project and risk management expertise."

**PPT Content:**
```
Ground Rules:

1. FOCUS: Technical Planning & Management
   • Not general program/business management
   • SE-specific planning, scheduling, risk management
   • How to manage the technical work of SE

2. STANDARDS-BASED APPROACH
   • ISO/IEC 15288 Technical Management Processes
   • Automotive standards (APQP, VDA-RGA, ISO 26262)
   • Industry best practices

3. PREVENTION MINDSET
   • Ask: "How would this have prevented past failures?"
   • Management prevents technical disasters
   • Discipline enables innovation

Questions to Consider:
• How does project planning enable technical work?
• What risks threaten your system success?
• How do you balance planning with execution?
```

**Learning Outcomes:** LO1, LO3 - Framework for SE management

---

#### Slide 6: The Stakes - What Poor Management Costs
**Visual:** Cost infographic showing project failures

**Instructor Narration:**
> "Let's talk stakes. What does poor project and risk management cost in automotive?
>
> **Financial**: Average automotive recall costs $500M-$1B. A single failed vehicle program can cost $5-10 billion in development plus opportunity costs.
>
> **Schedule**: Each month of delay costs millions in lost revenue and keeps your product from market while competitors advance.
>
> **Technical Debt**: Skipping planning and risk management creates technical debt—shortcuts taken that require expensive rework later.
>
> **Career Impact**: Major project failures end careers and damage reputations for years.
>
> But here's the good news: **Rigorous project and risk management dramatically improves success rates.** Studies show well-managed projects are 3-4x more likely to succeed. That's what we're learning today."

**PPT Content:**
```
THE STAKES: Cost of Poor Project/Risk Management

AUTOMOTIVE PROJECT FAILURES:
• Failed vehicle program: $5-10B in development costs
• Each month delay: $10-50M in lost revenue
• Average recall: $500M-$1B
• Technical debt: 2-5x rework costs

INDUSTRY STATISTICS:
• 70% of large projects fail to meet objectives
• Average cost overrun: 189% of budget
• Average schedule delay: 222% of timeline
• Only 2.5% of companies complete 100% of projects successfully

ROOT CAUSES OF FAILURE:
1. Poor planning and estimation (39%)
2. Inadequate risk management (28%)
3. Scope creep and change control (25%)
4. Resource constraints (21%)
5. Poor communication (19%)

THE GOOD NEWS:
• Well-managed projects: 3-4x higher success rate
• Risk management ROI: $1 spent saves $3-7 later
• Early planning reduces rework by 50-80%

→ Management discipline is professional engineering practice
```

**Learning Outcomes:** LO3 - Understanding management value

---

#### Slide 7: ISO/IEC 15288 Technical Management Processes
**Visual:** Diagram showing the four technical management processes

**Instructor Narration:**
> "ISO/IEC 15288—the systems engineering lifecycle standard we've referenced throughout this course—defines four **Technical Management Processes**. These are the management processes specifically for SE work:
>
> **1. Project Planning Process** - Define and maintain plans for SE activities
>
> **2. Project Assessment and Control Process** - Monitor progress, identify issues, take corrective action
>
> **3. Decision Management Process** - Make informed technical decisions throughout the lifecycle
>
> **4. Risk Management Process** - Identify and manage risks and opportunities
>
> Today we focus on processes 1, 2, and 4. Next session, we'll deep-dive into Decision Management and add Quality Management. But notice: these aren't separate from SE. **These ARE systems engineering processes.** Managing the work is part of doing the work."

**PPT Content:**
```
ISO/IEC 15288 TECHNICAL MANAGEMENT PROCESSES

Four Technical Management Processes:

1. PROJECT PLANNING PROCESS
   Purpose: Produce and coordinate effective plans
   • Define project scope and objectives
   • Develop schedules, budgets, resources
   • Create work breakdown structure
   • Plan integration and verification activities

2. PROJECT ASSESSMENT AND CONTROL PROCESS
   Purpose: Assess progress and control execution
   • Monitor technical progress
   • Identify deviations and issues
   • Take corrective actions
   • Report status to stakeholders

3. DECISION MANAGEMENT PROCESS (Session 10)
   Purpose: Make informed technical decisions
   • Identify decision needs
   • Analyze alternatives
   • Select preferred solutions

4. RISK MANAGEMENT PROCESS
   Purpose: Identify and manage risks/opportunities
   • Risk identification and analysis
   • Risk treatment planning
   • Monitor and control risks

→ These are not overhead. These ARE systems engineering.
```

**Learning Outcomes:** LO1 - SE management framework

---

#### Slide 8: The Integration View
**Visual:** Diagram showing how technical management integrates with technical processes

**Instructor Narration:**
> "Here's the critical insight: Technical management processes **enable and support** the technical processes we've already studied.
>
> You can't do requirements engineering without project planning—who does what, when, with what resources?
>
> You can't do system architecture without risk management—what architectural risks threaten success?
>
> You can't do integration and verification without project assessment and control—are we on track? What's blocking us?
>
> **Management and engineering are integrated, not separate.** The best systems engineers are also disciplined project and risk managers. That's what this session teaches you."

**PPT Content:**
```
INTEGRATION: Technical Management ↔ Technical Processes

TECHNICAL PROCESSES (Sessions 4-8):
• Requirements Engineering
• System Architecture
• Design and Analysis
• Integration
• Verification and Validation

Enabled and Supported by ↕

TECHNICAL MANAGEMENT PROCESSES (Today):
• Project Planning → Who, what, when, resources
• Risk Management → Threats and opportunities
• Assessment & Control → Progress monitoring, corrective action

EXAMPLES OF INTEGRATION:

Requirements Engineering needs:
→ Planning: Schedule for stakeholder engagement, analysis, validation
→ Risk: Risk that requirements are unstable or conflicting
→ Control: Track requirements completion and quality

System Architecture needs:
→ Planning: Resources for architecture development and review
→ Risk: Architectural risks (performance, safety, interfaces)
→ Control: Monitor architecture maturity and decisions

Integration/Verification needs:
→ Planning: Integration sequence, test schedules, facility allocation
→ Risk: Integration risks, test failures
→ Control: Track integration progress, test execution

→ You cannot separate technical work from technical management
```

**Learning Outcomes:** LO1, LO3 - Integrated SE approach

---

### **TRIGGER: Project Planning Process** (Slides 9-14, ~25 minutes)

**Narrative Voice:** Systematic, building practical planning skills

---

#### Slide 9: Project Planning Process - Overview
**Visual:** Flowchart of project planning activities

**Instructor Narration:**
> "Let's dive into Project Planning. The purpose of this process is simple: **Produce and maintain plans that enable the SE work to be performed effectively.**
>
> Notice what this means: You're not planning everything. You're planning the *technical work*—the systems engineering activities. You're making sure requirements engineering happens, design happens, integration happens, verification happens—on time, with the right people and resources.
>
> Project planning in SE has five key activities. Let's explore each one."

**PPT Content:**
```
PROJECT PLANNING PROCESS

PURPOSE:
"Produce and maintain plans that enable the SE work
to be performed effectively" (ISO/IEC 15288)

KEY ACTIVITIES:

1. DEFINE PROJECT SCOPE
   • Objectives and success criteria
   • System boundary and lifecycle scope
   • Stakeholder needs and expectations
   • Constraints and assumptions

2. DEVELOP WORK BREAKDOWN STRUCTURE (WBS)
   • Decompose work into manageable elements
   • Align with system architecture
   • Define deliverables and work packages

3. CREATE PROJECT SCHEDULE
   • Sequence activities
   • Estimate durations
   • Identify dependencies and critical path
   • Allocate milestones and gates

4. ALLOCATE RESOURCES
   • People (skills, roles, availability)
   • Budget and funding
   • Tools, facilities, equipment
   • Information and data

5. PLAN INTEGRATION & INFRASTRUCTURE
   • Technical planning for integration
   • V&V planning
   • Configuration management
   • Information management

→ Planning is continuous, not one-time
```

**Learning Outcomes:** LO1 - Project planning fundamentals

---

#### Slide 10: Work Breakdown Structure (WBS) - Foundation of Planning
**Visual:** Example WBS for automotive system (hierarchical structure)

**Instructor Narration:**
> "The Work Breakdown Structure is the foundation of all project planning. It's a hierarchical decomposition of the total work to be performed.
>
> Here's the key: **The WBS should align with your system architecture.** If your system has these subsystems—powertrain, chassis, body, electrical—then your WBS should reflect that structure. This creates natural alignment between what you're building and how you're organizing the work.
>
> Let me show you an automotive example. Top level: Complete vehicle system. Second level: Major subsystems. Third level: Components and assemblies. Fourth level: Work packages—the actual tasks assigned to teams.
>
> **Each WBS element should have clear deliverables, acceptance criteria, and responsible owners.** This is how you ensure nothing falls through the cracks."

**PPT Content:**
```
WORK BREAKDOWN STRUCTURE (WBS)

DEFINITION:
Hierarchical decomposition of total project work
into manageable, measurable elements

PRINCIPLES:
✓ Align with system architecture
✓ 100% rule: WBS includes 100% of work, nothing more
✓ Mutually exclusive: No overlap between elements
✓ Deliverable-oriented: Each element produces something
✓ Manageable size: Work packages 1-2 weeks effort

AUTOMOTIVE EXAMPLE: Electric Vehicle Development

Level 1: Complete EV System
├─ Level 2: Powertrain System
│  ├─ Level 3: Battery System
│  │  ├─ Level 4: Cell design & validation (Work Package)
│  │  ├─ Level 4: BMS hardware development (Work Package)
│  │  └─ Level 4: Thermal management integration (Work Package)
│  ├─ Level 3: Electric Motor System
│  └─ Level 3: Power Electronics
├─ Level 2: Chassis System
├─ Level 2: Body & Interior
└─ Level 2: Electrical/Electronic Architecture

EACH WBS ELEMENT SHOULD DEFINE:
• Deliverables (what is produced)
• Acceptance criteria (how we know it's done)
• Resources required (who, what, cost)
• Dependencies (what it needs from others)
• Owner/Responsible party

→ WBS drives scheduling, budgeting, resource allocation
```

**Learning Outcomes:** LO1, LO2 - WBS for SE projects

---

#### Slide 11: Scheduling - Sequencing and Dependencies
**Visual:** Gantt chart and network diagram showing critical path

**Instructor Narration:**
> "Once you have your WBS, you create the schedule. This means sequencing activities, estimating durations, and identifying dependencies.
>
> **Dependencies are critical.** You can't verify requirements before you've captured them. You can't integrate subsystems before they're designed. These are called precedence relationships.
>
> Three key scheduling concepts you must know:
>
> **1. Critical Path** - The longest sequence of dependent activities. This determines your minimum project duration. Delay anything on the critical path, and you delay the whole project.
>
> **2. Float/Slack** - How much an activity can be delayed without delaying the project. Activities on the critical path have zero float.
>
> **3. Milestones and Gates** - Key decision points and deliverables. In automotive, these align with APQP gates or stage-gate processes.
>
> Let me show you an example schedule for a system development."

**PPT Content:**
```
PROJECT SCHEDULING

PURPOSE:
Sequence activities, estimate durations, manage dependencies

KEY SCHEDULING CONCEPTS:

1. PRECEDENCE RELATIONSHIPS (Dependencies)
   • Finish-to-Start (FS): A must finish before B starts
   • Start-to-Start (SS): A and B start together
   • Finish-to-Finish (FF): A and B finish together
   • Start-to-Finish (SF): A must start before B finishes (rare)

2. CRITICAL PATH
   • Longest sequence of dependent activities
   • Determines minimum project duration
   • Activities with zero float/slack
   • Delays here delay entire project

3. FLOAT / SLACK
   • Time an activity can be delayed without delaying project
   • Critical path activities: 0 float
   • Non-critical activities: positive float

4. MILESTONES & GATES
   • Key decision points with no duration
   • Example automotive milestones:
     - Concept approval
     - Requirements baseline
     - PDR (Preliminary Design Review)
     - CDR (Critical Design Review)
     - Integration complete
     - Verification complete

AUTOMOTIVE SCHEDULE EXAMPLE:
Requirements Engineering (8 weeks) → [Baseline Milestone]
   ↓
System Architecture (6 weeks) → [PDR Milestone]
   ↓
Detailed Design (12 weeks, parallel subsystems)
   ↓
Component Development (16 weeks) → [CDR Milestone]
   ↓
Integration (10 weeks)
   ↓
System Verification (8 weeks) → [Verification Complete Milestone]
   ↓
Validation (6 weeks) → [Product Release]

CRITICAL PATH ANALYSIS:
• Requirements → Architecture → Design → Integration → Verification
• Any delay in this path delays product release
• Parallel work (if independent) doesn't extend critical path

SCHEDULING TOOLS:
• Gantt charts (timeline visualization)
• Network diagrams (dependency visualization)
• Critical Path Method (CPM)
• Program Evaluation and Review Technique (PERT)

→ Schedule is living document, update continuously
```

**Learning Outcomes:** LO1, LO2 - Scheduling SE work

---

#### Slide 12: Resource Allocation - People, Budget, Tools
**Visual:** Resource allocation matrix and resource leveling diagram

**Instructor Narration:**
> "You have your WBS and schedule. Now you need resources. Resources in SE include people, budget, tools, facilities, and information.
>
> **People**: What skills do you need? Systems engineers, domain experts, analysts, testers. When do you need them? For how long? You can't have 10 tasks requiring the same person simultaneously.
>
> **Budget**: Cost estimation for each WBS element. SE work costs money—labor, tools, test facilities, prototypes. You need to plan and track it.
>
> **Tools and Infrastructure**: SysML modeling tools, simulation software, test equipment, labs, integration facilities. These have lead times—you can't order a test facility the week you need it.
>
> **Information**: Requirements databases, models, test data, supplier inputs. You need to plan how information flows and is managed.
>
> Key challenge: **Resource conflicts and leveling.** What happens when three activities need the same specialist? You level resources—adjust schedule to avoid over-allocation."

**PPT Content:**
```
RESOURCE ALLOCATION

RESOURCE CATEGORIES:

1. HUMAN RESOURCES
   • Skills needed: Systems engineers, domain experts, specialists
   • Roles: Lead SE, requirements engineer, architect, integration lead
   • Availability: Full-time, part-time, when needed
   • Resource loading: Hours/week per person per task

2. FINANCIAL RESOURCES
   • Labor costs (by role, by activity)
   • Tools and software licenses
   • Test equipment and facilities
   • Prototypes and materials
   • Travel and external services
   • Contingency reserves (typically 10-20%)

3. TOOLS & EQUIPMENT
   • SysML/MBSE tools (Cameo, Rhapsody, etc.)
   • Simulation tools (MATLAB/Simulink, etc.)
   • Requirements management (DOORS, Polarion)
   • Configuration management systems
   • Test equipment and instrumentation
   • Integration and test facilities

4. FACILITIES & INFRASTRUCTURE
   • Office space and meeting rooms
   • Laboratories and test cells
   • Integration facilities
   • Environmental chambers
   • Vehicle proving grounds

5. INFORMATION & DATA
   • Requirements specifications
   • System models and architectures
   • Analysis results
   • Supplier technical data
   • Test data and reports

RESOURCE LEVELING:
Problem: Multiple tasks competing for same resource
Solution: Adjust schedule to smooth resource usage
• Delay non-critical tasks
• Reassign work to available resources
• Add resources if critical path affected
• Accept schedule extension if necessary

RESOURCE ALLOCATION MATRIX EXAMPLE:
Activity          | SE Lead | Req Eng | Architect | Integration | Hours | Cost
Requirements      |   50%   |  100%   |    25%    |      0%     |  320  | $48K
Architecture      |   75%   |   25%   |   100%    |      0%     |  240  | $42K
Integration Plan  |   50%   |    0%   |    50%    |    100%     |  160  | $28K

AUTOMOTIVE RESOURCE CONSIDERATIONS:
• Supplier resources and dependencies
• Cross-functional team coordination
• Test facility scheduling (long lead times)
• Prototype vehicle availability
• Regulatory testing requirements

→ Resources constrain schedule; plan realistically
```

**Learning Outcomes:** LO1, LO2 - Resource planning

---

#### Slide 13: Technical Planning Deliverables
**Visual:** Example table of contents for Systems Engineering Management Plan (SEMP)

**Instructor Narration:**
> "All this planning gets documented in key deliverables. The primary one is the **Systems Engineering Management Plan (SEMP)**—the master plan for how SE work will be performed.
>
> The SEMP includes your WBS, schedule, resource allocation, verification approach, risk management approach, and configuration management approach. It's the roadmap for the technical team.
>
> You also create specialized plans: Requirements Management Plan, Verification Plan, Integration Plan, Configuration Management Plan. Each addresses a specific aspect of the SE work.
>
> **These aren't bureaucratic documents gathering dust.** These are working plans that guide daily activities and get updated as the project evolves. In automotive programs, these align with APQP deliverables and project management plans.
>
> If you can't explain how the SE work will be done, you're not ready to start. Planning first, execution second."

**PPT Content:**
```
TECHNICAL PLANNING DELIVERABLES

1. SYSTEMS ENGINEERING MANAGEMENT PLAN (SEMP)
   Master plan for SE activities and processes

   Typical SEMP Contents:
   • Project scope and objectives
   • System overview and context
   • SE process tailoring
   • Organization and responsibilities
   • Work breakdown structure
   • Project schedule and milestones
   • Resource allocation and budget
   • Integration and verification approach
   • Risk management approach
   • Configuration management approach
   • Technical performance measures
   • Supplier management approach

2. SPECIALIZED SE PLANS
   • Requirements Management Plan
   • System Architecture Document (living)
   • Verification and Validation Plan
   • Integration Plan
   • Configuration Management Plan
   • Risk Management Plan
   • Interface Control Plan

3. SCHEDULES & TRACKING TOOLS
   • Integrated master schedule
   • Milestone chart
   • Gantt charts (by subsystem, by activity)
   • Resource loading charts

4. BUDGETS & COST TRACKING
   • Budget by WBS element
   • Earned Value Management (EVM) for large programs
   • Cost tracking and variance analysis

AUTOMOTIVE CONTEXT:
SEMP aligns with:
• APQP (Advanced Product Quality Planning) deliverables
• Project Management Plan
• DVP&R (Design Verification Plan & Report)
• DFMEA / PFMEA processes
• Supplier development plans

PLAN MAINTENANCE:
✓ Plans are living documents
✓ Update as project evolves
✓ Baseline major versions
✓ Communicate changes to team
✓ Keep plans realistic and useful (not shelf-ware)

→ "Proper planning prevents poor performance"
```

**Learning Outcomes:** LO1, LO2 - Planning deliverables

---

#### Slide 14: Project Assessment and Control Process
**Visual:** Control loop diagram showing plan-execute-measure-correct cycle

**Instructor Narration:**
> "Planning is not enough. You must **monitor progress and control execution**. This is the Project Assessment and Control Process.
>
> Think of it as a feedback loop: You plan, you execute, you measure actual progress against the plan, you identify deviations, and you take corrective action. Then you replan if necessary.
>
> **Key assessment techniques:**
>
> **Technical Performance Measures (TPMs)** - Quantitative metrics for critical system attributes. Example: Battery range must be 400 km. At 60% design complete, predicted range is 380 km. Red flag—we're trending below requirement.
>
> **Milestone Tracking** - Did we hit the milestone? If not, why not? What's the impact?
>
> **Earned Value Management (EVM)** - For larger programs, comparing planned value, earned value, and actual cost. Tells you if you're ahead/behind schedule and over/under budget.
>
> **Risk Reviews** - Regularly reviewing the risk register. Have risks changed? New risks emerged?
>
> When you find deviations, you take corrective action: Replan, add resources, reduce scope, escalate issues. **Control means making decisions to keep the project on track.**"

**PPT Content:**
```
PROJECT ASSESSMENT AND CONTROL PROCESS

PURPOSE:
Monitor technical progress, identify deviations,
take corrective action

THE CONTROL LOOP:
PLAN → EXECUTE → MEASURE → ANALYZE → CORRECT → REPLAN

KEY ASSESSMENT TECHNIQUES:

1. TECHNICAL PERFORMANCE MEASURES (TPMs)
   • Quantitative metrics for critical system attributes
   • Track predicted vs. required performance over time
   • Early warning of technical issues

   Example TPM for EV Battery:
   Requirement: 400 km range
   Predicted range tracked through design:
   - At concept: 420 km (green)
   - At 30% design: 410 km (green)
   - At 60% design: 380 km (yellow - trending below)
   - At 90% design: 395 km (yellow - marginal)
   → Triggers analysis and corrective action

2. MILESTONE & DELIVERABLE TRACKING
   • Was milestone achieved? (Yes/No/Partial)
   • Quality of deliverable?
   • Dependencies affected?
   • Root cause of misses?

3. SCHEDULE PERFORMANCE
   • Activities completed vs. planned
   • Critical path status
   • Schedule variance
   • Forecast completion date

4. COST/BUDGET PERFORMANCE
   • Actual cost vs. budgeted cost
   • Cost variance and trends
   • Forecast cost at completion

5. EARNED VALUE MANAGEMENT (EVM) - Large Programs
   Metrics:
   • Planned Value (PV): Budgeted cost of planned work
   • Earned Value (EV): Budgeted cost of completed work
   • Actual Cost (AC): Actual cost of completed work

   Indices:
   • Schedule Performance Index (SPI) = EV / PV
     SPI > 1: Ahead of schedule; SPI < 1: Behind schedule
   • Cost Performance Index (CPI) = EV / AC
     CPI > 1: Under budget; CPI < 1: Over budget

6. RISK REGISTER REVIEWS
   • Are risks being mitigated?
   • Have risk probabilities/impacts changed?
   • New risks identified?
   • Are triggers being monitored?

7. QUALITY METRICS
   • Requirements stability (change rate)
   • Defect rates (design, code, test)
   • Review findings and closure rates
   • Test pass/fail rates

CORRECTIVE ACTIONS:
When deviations identified:
• Root cause analysis
• Develop corrective action plan
• Reallocate resources
• Adjust schedule (if not on critical path)
• Escalate if major impact
• Update plans and baselines
• Communicate to stakeholders

REPORTING & COMMUNICATION:
• Weekly status reports (internal team)
• Monthly project reviews (management)
• Milestone reviews (gates)
• Exception reports (when thresholds exceeded)
• Dashboard visualization of key metrics

AUTOMOTIVE CONTEXT:
• Align with APQP gateway reviews
• DVP&R tracking
• Launch readiness scorecards
• Supplier performance monitoring
• Issue tracking and CAPA (Corrective/Preventive Action)

→ What gets measured gets managed
```

**Learning Outcomes:** LO1, LO2 - Project control

---

### **RISING ACTION: Risk Management Process** (Slides 15-22, ~30 minutes)

**Narrative Voice:** Analytical and proactive, building risk management discipline

---

#### Slide 15: Risk Management Process - Overview
**Visual:** ISO/IEC 15288 risk management process flow diagram

**Instructor Narration:**
> "Now we shift to Risk Management—arguably the most critical technical management process. Let me start with a definition:
>
> **Risk is the effect of uncertainty on objectives.** Notice: Risk is not just negative. Uncertainty can create threats (negative risks) or opportunities (positive risks).
>
> The Risk Management Process has four key activities: **Plan, Identify, Analyze, Treat, and Monitor.** This is a continuous cycle throughout the system lifecycle.
>
> Here's why this matters in automotive: You're developing a system that will be manufactured in millions of units, used by untrained drivers, in unpredictable conditions, for 10+ years. **Uncertainty is everywhere.** If you don't manage it proactively, it will destroy your program.
>
> Let's build your risk management expertise step by step."

**PPT Content:**
```
RISK MANAGEMENT PROCESS (ISO/IEC 15288)

PURPOSE:
Identify, analyze, treat, and monitor risks and opportunities
throughout the system lifecycle

RISK DEFINITION:
"Risk is the effect of uncertainty on objectives"
(ISO 31000, ISO/IEC 15288)

KEY CONCEPTS:
• Risk = Threat (negative) or Opportunity (positive)
• Uncertainty → variability, ambiguity, lack of knowledge
• Objectives → what you're trying to achieve (performance, cost, schedule, quality, safety)

RISK MANAGEMENT ACTIVITIES:

1. PLAN RISK MANAGEMENT
   • Define risk management approach
   • Establish risk categories and criteria
   • Define roles and responsibilities

2. IDENTIFY RISKS
   • What can go wrong? (threats)
   • What can go better than expected? (opportunities)
   • Document in risk register

3. ANALYZE RISKS
   • Assess probability and impact
   • Prioritize risks
   • Understand root causes

4. TREAT RISKS
   • Develop risk treatment plans
   • Implement risk responses
   • Allocate resources for treatment

5. MONITOR RISKS
   • Track risk status
   • Identify new risks
   • Evaluate treatment effectiveness
   • Communicate risk status

→ Risk management is continuous, not one-time

AUTOMOTIVE RISK CATEGORIES:
• Technical risks (performance, integration, technology maturity)
• Schedule risks (delays, dependencies)
• Cost risks (overruns, supplier costs)
• Safety risks (hazards, failures)
• Regulatory/Compliance risks
• Supply chain risks
• Market/Business risks
```

**Learning Outcomes:** LO1, LO3 - Risk management framework

---

#### Slide 16: Risk Identification - Finding the Threats and Opportunities
**Visual:** Mind map showing risk identification sources and techniques

**Instructor Narration:**
> "Risk identification answers one question: **What uncertainties could affect our objectives?**
>
> You identify risks using multiple techniques:
>
> **Brainstorming** with the team: 'What could go wrong? What are we worried about?'
>
> **Checklists** from past projects and lessons learned: 'What risks occurred before?'
>
> **Risk Breakdown Structure (RBS)** - Categories of risk to ensure you don't miss anything: Technical, schedule, cost, external, organizational.
>
> **Failure mode analysis** - FMEA, Fault Tree Analysis, Hazard Analysis. We covered these in safety engineering.
>
> **Assumption analysis** - Every assumption is a hidden risk. 'We assume the supplier delivers on time.' That's a risk if the assumption is wrong.
>
> **Expert judgment** - Experienced engineers who've seen similar systems.
>
> You document all identified risks in a **Risk Register**—a living database of risks tracked throughout the project. Let me show you what goes in a risk register."

**PPT Content:**
```
RISK IDENTIFICATION

GOAL:
Identify all significant threats and opportunities
that could affect project objectives

RISK IDENTIFICATION TECHNIQUES:

1. BRAINSTORMING
   • Team-based ideation
   • "What could go wrong?"
   • "What could go better than expected?"
   • Encourage diverse perspectives

2. RISK BREAKDOWN STRUCTURE (RBS)
   Systematic categories to ensure complete coverage:
   • Technical Risks
     - Requirements instability
     - Design complexity
     - Technology maturity (TRL)
     - Integration challenges
     - Performance uncertainty
   • Schedule Risks
     - Unrealistic timelines
     - Dependencies and critical path
     - Resource availability
     - Supplier delays
   • Cost Risks
     - Estimation errors
     - Scope creep
     - Commodity price volatility
   • External Risks
     - Regulatory changes
     - Market changes
     - Supplier financial health
     - Natural disasters
   • Organizational Risks
     - Skill gaps
     - Staff turnover
     - Communication breakdowns
     - Conflicting priorities

3. CHECKLISTS & LESSONS LEARNED
   • Historical risk databases
   • Previous project risk registers
   • Industry-specific risk libraries
   • Lessons learned repositories

4. FAILURE MODE ANALYSIS
   • FMEA (Failure Mode and Effects Analysis)
   • Fault Tree Analysis
   • Hazard Analysis (for safety-critical systems)
   • "What If" analysis

5. ASSUMPTION ANALYSIS
   • List all project assumptions
   • Each assumption is a potential risk
   • "What if this assumption is wrong?"

   Example Assumptions → Risks:
   - Assume supplier delivers on time → Risk: Supplier delay
   - Assume technology is mature → Risk: Technology not ready
   - Assume requirements are stable → Risk: Requirement changes

6. EXPERT JUDGMENT & INTERVIEWS
   • Consult experienced engineers
   • Domain experts
   • Supplier input
   • Customer/User insights

7. SYSTEM ANALYSIS TECHNIQUES
   • Interface analysis (interface risks)
   • Dependency analysis (dependency risks)
   • Complexity analysis (emergent behavior risks)

AUTOMOTIVE-SPECIFIC RISK SOURCES:
• New technology integration (e.g., autonomous features)
• Supply chain complexity (global, multi-tier)
• Regulatory uncertainty (evolving standards)
• Software and cybersecurity
• Validation and testing (proving grounds, scenarios)
• Manufacturing and quality (new processes)
• Warranty and field performance

RISK REGISTER:
Database tracking all identified risks

Risk Register Fields:
• Risk ID (unique identifier)
• Risk Title (brief description)
• Risk Category (from RBS)
• Risk Description (detailed)
• Risk Owner (who's responsible)
• Probability (likelihood of occurring)
• Impact (consequence if it occurs)
• Risk Score (Probability × Impact)
• Risk Response Strategy
• Trigger/Indicator (early warning signs)
• Status (open, mitigated, closed)
• Date Identified

→ Risk identification is continuous throughout project
```

**Learning Outcomes:** LO1, LO2 - Risk identification

---

#### Slide 17: Risk Analysis - Assessing Probability and Impact
**Visual:** Risk matrix (probability vs. impact) with example risks plotted

**Instructor Narration:**
> "Once you've identified risks, you analyze them. Risk analysis answers two questions:
>
> **1. How likely is this risk to occur?** (Probability)
> **2. If it occurs, how bad is the impact?** (Consequence)
>
> You assess both, then calculate a **Risk Score = Probability × Impact**. This lets you prioritize—focus on high-probability, high-impact risks first.
>
> We visualize this using a **Risk Matrix**. Probability on one axis (rare, unlikely, possible, likely, almost certain). Impact on the other axis (negligible, minor, moderate, major, catastrophic). Each risk gets plotted.
>
> Risks in the red zone (high probability, high impact) demand immediate attention. Risks in the green zone (low probability, low impact) you may accept or monitor.
>
> Let me show you an automotive example: 'Risk that battery cells don't meet range requirement.' Probability: Possible (50%). Impact: Major (significant rework, cost, schedule). Risk Score: High. Priority: Immediate treatment needed."

**PPT Content:**
```
RISK ANALYSIS

GOAL:
Assess probability and impact of each risk;
prioritize for treatment

TWO KEY QUESTIONS:
1. How likely is this risk to occur? (PROBABILITY)
2. If it occurs, how severe is the impact? (IMPACT/CONSEQUENCE)

PROBABILITY SCALE (Example):
• Almost Certain: 90-100% (5)
• Likely: 70-90% (4)
• Possible: 30-70% (3)
• Unlikely: 10-30% (2)
• Rare: 0-10% (1)

IMPACT SCALE (Example):
• Catastrophic: Program failure, safety critical (5)
• Major: Significant cost/schedule impact, major rework (4)
• Moderate: Noticeable impact, manageable rework (3)
• Minor: Small impact, easily recovered (2)
• Negligible: Minimal or no impact (1)

RISK SCORE:
Risk Score = Probability × Impact
(Scale of 1-25 in this example)

RISK MATRIX EXAMPLE:
                    IMPACT →
           Negligible Minor Moderate Major Catastrophic
           (1)        (2)   (3)      (4)   (5)
Rare (1)       1       2      3        4      5
Unlikely (2)   2       4      6        8     10
Possible (3)   3       6      9       12     15
Likely (4)     4       8     12       16     20
Almost (5)     5      10     15       20     25
Certain

RISK ZONES:
• LOW (1-5): Green zone - Accept or monitor
• MEDIUM (6-12): Yellow zone - Treat with standard approaches
• HIGH (15-25): Red zone - Immediate attention, aggressive treatment

AUTOMOTIVE RISK EXAMPLE: Battery Range

Risk: Battery cells don't meet energy density target,
      resulting in vehicle range below 400 km requirement

Analysis:
• Probability: Possible (3) - New cell chemistry, supplier track record uncertain
• Impact: Major (4) - Would require:
  - Battery redesign
  - Vehicle weight reduction (expensive)
  - Schedule delay of 6+ months
  - Cost impact $50M+
  - Customer dissatisfaction if range reduced
• Risk Score: 3 × 4 = 12 (Medium-High)
• Priority: High - Requires treatment plan

QUALITATIVE vs QUANTITATIVE ANALYSIS:

QUALITATIVE (most common):
• Use scales (Low/Med/High or 1-5)
• Faster, easier, subjective
• Suitable for most projects

QUANTITATIVE (complex/large programs):
• Use numerical probabilities (e.g., 35%)
• Use cost/schedule impacts ($, days)
• Simulation (Monte Carlo) for overall program risk
• More precise, more effort
• Example: Risk of 6-month delay has 35% probability,
  costing $12M if it occurs
  Expected Monetary Value = 0.35 × $12M = $4.2M

RISK ANALYSIS TECHNIQUES:
• Expert judgment
• Historical data analysis
• Probability distributions
• Sensitivity analysis (what-if scenarios)
• Monte Carlo simulation (for schedule/cost risk)
• Decision tree analysis

→ Analysis enables rational prioritization and resource allocation
```

**Learning Outcomes:** LO1, LO2 - Risk analysis methods

---

#### Slide 18: Risk Treatment - Response Strategies
**Visual:** Diagram showing four risk response strategies with examples

**Instructor Narration:**
> "Now you've identified and analyzed risks. Time to **treat them**—develop and implement risk responses.
>
> You have four basic strategies for **threats (negative risks)**:
>
> **1. Avoid** - Eliminate the risk entirely. Change your approach so the risk can't happen. Example: Risk of supplier delay? Avoid by bringing work in-house or dual-sourcing.
>
> **2. Mitigate** - Reduce probability or impact. Can't eliminate the risk, but you can make it less likely or less severe. Example: Battery range risk? Mitigate by testing cells early, working closely with supplier on design.
>
> **3. Transfer** - Shift the risk to another party. Insurance, contractual terms, outsourcing. Example: Transfer software development risk to a Tier 1 supplier with penalty clauses for delays.
>
> **4. Accept** - Acknowledge the risk exists, but take no proactive action. Use for low-priority risks. You may create a contingency reserve (budget/schedule buffer) in case the risk occurs.
>
> For **opportunities (positive risks)**, you have parallel strategies: Exploit, Enhance, Share, Accept.
>
> Each high-priority risk needs a documented treatment plan. Let me show you what that looks like."

**PPT Content:**
```
RISK TREATMENT

GOAL:
Develop and implement responses to address risks

FOUR STRATEGIES FOR THREATS (Negative Risks):

1. AVOID
   • Eliminate the risk entirely
   • Change plan/approach so risk cannot occur
   • Usually highest cost, but eliminates uncertainty

   Example:
   Risk: Supplier A has history of delays
   Avoidance: Don't use Supplier A; use proven Supplier B
   or bring work in-house

2. MITIGATE
   • Reduce probability of occurrence
   • Reduce impact if it occurs
   • Most common strategy

   Example:
   Risk: Battery cells may not meet energy density target
   Mitigation:
   - Early cell testing and validation (reduce probability)
   - Design vehicle with weight reduction options (reduce impact)
   - Close collaboration with cell supplier
   - Parallel development of backup cell chemistry

3. TRANSFER
   • Shift risk to another party
   • Insurance, contracts, outsourcing
   • Risk still exists, but someone else bears the consequence

   Example:
   Risk: Software development may be delayed
   Transfer:
   - Contract with Tier 1 supplier for software development
   - Include penalty clauses for late delivery
   - Supplier bears schedule/cost risk

4. ACCEPT
   • Acknowledge risk, take no proactive action
   • For low-priority risks where treatment cost exceeds benefit
   • Passive acceptance: Do nothing
   • Active acceptance: Create contingency reserve (buffer)

   Example:
   Risk: Minor component cost increase (5%)
   Acceptance: Include in budget contingency reserve

FOUR STRATEGIES FOR OPPORTUNITIES (Positive Risks):

1. EXPLOIT
   • Ensure opportunity definitely happens
   • Assign best resources, remove obstacles

   Example:
   Opportunity: New manufacturing process could reduce cost 20%
   Exploit: Invest in process development, accelerate implementation

2. ENHANCE
   • Increase probability or positive impact

   Example:
   Opportunity: Early completion could capture market window
   Enhance: Add resources to critical path, incentivize team

3. SHARE
   • Partner with others to realize opportunity

   Example:
   Opportunity: New technology platform applicable to multiple products
   Share: Joint development with another division, share costs and benefits

4. ACCEPT
   • Don't actively pursue, but be ready if it occurs

RISK TREATMENT PLAN COMPONENTS:

For each high-priority risk, document:
• Risk ID and description
• Treatment strategy (Avoid/Mitigate/Transfer/Accept)
• Specific actions to be taken
• Resources required (budget, people, time)
• Responsible person (risk owner)
• Timeline for implementation
• Success criteria (how we know it's working)
• Contingency plan (if treatment fails)

EXAMPLE RISK TREATMENT PLAN:

Risk ID: R-045
Title: Battery range below requirement
Probability: 3 (Possible) | Impact: 4 (Major) | Score: 12

Strategy: MITIGATE

Actions:
1. Conduct early cell characterization testing (Week 8-12)
   Owner: Battery Engineer
   Cost: $50K

2. Establish weekly design reviews with cell supplier (Week 6 onward)
   Owner: Chief Engineer

3. Develop lightweight vehicle design options to offset range loss (Week 10-20)
   Owner: Vehicle Architecture Team
   Cost: $200K

4. Initiate parallel development of backup cell chemistry (Week 12)
   Owner: Battery Engineer
   Cost: $300K

5. Include 5% range margin in target (400 km → 420 km target)
   Owner: Systems Engineer

Contingency Plan (if risk occurs):
• Reduce vehicle weight by 100 kg (estimated cost: $2M)
• Accept reduced range to 380 km with marketing plan
• Delay launch 3 months for battery redesign

Expected Risk Reduction:
• Probability: 3 → 2 (Unlikely)
• Impact: 4 → 3 (Moderate, due to contingency options)
• New Score: 6 (Medium)

RESIDUAL RISK:
After treatment, some risk remains (residual risk)
Monitor and manage throughout project

→ Document treatment plans; assign ownership; track execution
```

**Learning Outcomes:** LO1, LO2 - Risk treatment strategies

---

#### Slide 19: Risk Monitoring and Control
**Visual:** Risk dashboard showing risk trends and status

**Instructor Narration:**
> "Risk management doesn't end after treatment. You must **monitor risks continuously** throughout the project.
>
> **Monitor risk triggers** - Early warning indicators that a risk is materializing. Example: Battery risk trigger is 'Cell test results show energy density below target.' If you see the trigger, activate contingency plans.
>
> **Track treatment effectiveness** - Are your mitigation actions working? Is the risk score decreasing?
>
> **Identify new risks** - As the project evolves, new risks emerge. Keep identifying and adding to the risk register.
>
> **Conduct regular risk reviews** - Weekly team reviews for high risks, monthly for all risks, gate reviews for major decision points.
>
> **Update the risk register** - Close resolved risks, escalate growing risks, adjust scores as information improves.
>
> **Communicate risk status** - Dashboards, reports, escalation to management when thresholds exceeded.
>
> The risk register is a living document. It evolves as your understanding evolves. This is proactive management."

**PPT Content:**
```
RISK MONITORING AND CONTROL

GOAL:
Track risks, evaluate treatment effectiveness,
identify new risks, communicate status

MONITORING ACTIVITIES:

1. TRACK RISK TRIGGERS
   • Early warning indicators
   • When trigger observed → activate contingency

   Example Triggers:
   - Battery risk: Cell test results below target
   - Supplier risk: Supplier misses interim deliverable
   - Schedule risk: Critical path activity slips 1 week

2. EVALUATE TREATMENT EFFECTIVENESS
   • Are mitigation actions being executed?
   • Is risk score decreasing?
   • Do we need additional actions?

3. IDENTIFY NEW RISKS
   • Continuous risk identification
   • Environment changes → new risks
   • Lessons from other projects

4. UPDATE RISK SCORES
   • As information improves, reassess probability/impact
   • Risks may increase or decrease over time
   • Re-prioritize based on current scores

5. REVIEW AND ESCALATE
   • Regular risk reviews:
     - Weekly: High risks (score > 15)
     - Monthly: All active risks
     - Gate reviews: Major decision points
   • Escalate when:
     - Risk score exceeds threshold
     - Treatment not effective
     - New critical risk identified
     - Risk impacts program success

6. CLOSE RESOLVED RISKS
   • Risk no longer applicable → close
   • Document lessons learned
   • Archive for future reference

RISK COMMUNICATION:

Risk Dashboard (Example):
┌─────────────────────────────────────────┐
│ RISK STATUS SUMMARY                     │
│                                         │
│ Total Active Risks: 45                  │
│ High (15-25):  8  [↓ 2 from last month] │
│ Medium (6-14): 22 [↑ 3 from last month] │
│ Low (1-5):     15 [→ No change]         │
│                                         │
│ TOP 5 RISKS:                            │
│ 1. R-045 Battery range (Score: 12)      │
│ 2. R-102 Supplier integration (Score:15)│
│ 3. R-067 Software complexity (Score: 12)│
│ 4. R-089 Test facility delays (Score:10)│
│ 5. R-134 Regulatory approval (Score: 9) │
└─────────────────────────────────────────┘

Risk Trend Chart:
(Shows risk score over time for top risks)

Risk Reports:
• Risk register (detailed, all risks)
• Executive summary (top 10 risks, trends)
• Risk watch list (risks nearing thresholds)
• Closed risks and lessons learned

RISK REVIEW MEETINGS:

Weekly Team Risk Review:
• Focus on high risks
• 30-60 minutes
• Review triggers, treatment status
• Identify issues and actions

Monthly Program Risk Review:
• All active risks
• Trend analysis
• New risks identified
• Risk reserve status
• Management decisions on escalated risks

Gate/Milestone Risk Reviews:
• Comprehensive risk assessment
• Go/No-Go decision input
• Update risk management plan
• Approve risk reserves for next phase

AUTOMOTIVE RISK MONITORING TOOLS:
• Integrated into APQP reviews
• Launch readiness scorecard
• Supplier scorecards (for supply risks)
• Test execution tracking (for validation risks)
• Issue tracking systems (CAPA, 8D)

→ Proactive monitoring prevents surprises
```

**Learning Outcomes:** LO1, LO2 - Risk monitoring

---

#### Slide 20: Opportunity Management - The Positive Side
**Visual:** Example opportunities and how to exploit them

**Instructor Narration:**
> "So far we've focused on threats—negative risks. But remember: **Risk is uncertainty, which includes opportunities.**
>
> Opportunities are uncertain events that, if they occur, have a *positive* impact on your objectives. Early supplier delivery. New technology that improves performance. Cost reduction from design optimization.
>
> Most teams ignore opportunities—they're focused on preventing bad things. But **proactive opportunity management can significantly improve project outcomes.**
>
> **Identify opportunities** using the same techniques as threats: brainstorming, lessons learned, expert input. What could go better than planned?
>
> **Analyze opportunities** the same way: What's the probability? What's the positive impact?
>
> **Treat opportunities** using the four strategies: Exploit (make it happen), Enhance (increase probability/impact), Share (partner for mutual benefit), Accept (let it happen if it happens).
>
> Let me give you an automotive example: 'Opportunity: New battery cell chemistry could increase range by 10%.' Probability: Possible. Impact: Moderate (competitive advantage, customer delight). Strategy: Enhance—invest in early validation, collaborate with supplier, prepare production for quick adoption.
>
> **Great project managers manage both threats and opportunities.** Don't leave positive outcomes to chance."

**PPT Content:**
```
OPPORTUNITY MANAGEMENT

DEFINITION:
Opportunities are uncertain events that, if they occur,
have a POSITIVE impact on objectives

WHY MANAGE OPPORTUNITIES?
• Most teams focus only on threats
• Proactive opportunity management improves outcomes
• Competitive advantage
• Cost savings, schedule acceleration, performance improvement
• Innovation and learning

OPPORTUNITY IDENTIFICATION:

Same techniques as threats:
• Brainstorming: "What could go better than expected?"
• Technology scouting: New innovations applicable
• Lessons learned: What worked better than planned before?
• Supplier innovations: What can suppliers offer?
• Market analysis: Emerging customer needs we can address

AUTOMOTIVE OPPORTUNITY EXAMPLES:

1. TECHNICAL OPPORTUNITIES
   • New technology improves performance beyond target
   • Design optimization reduces weight/cost more than expected
   • Supplier offers better component at same cost
   • Testing reveals system exceeds requirements

2. SCHEDULE OPPORTUNITIES
   • Parallel work possible (thought to be sequential)
   • Supplier delivers early
   • Verification completes faster than planned
   • Regulatory approval faster than expected

3. COST OPPORTUNITIES
   • Commodity price reduction
   • Manufacturing process improvement reduces cost
   • Volume increase enables better supplier pricing
   • Design simplification reduces part count

4. MARKET OPPORTUNITIES
   • Competitor delay creates market window
   • Customer demand higher than expected
   • Early launch captures market share
   • New market segment identified

OPPORTUNITY ANALYSIS:

Same approach as threats:
• Probability: How likely is this opportunity?
• Impact: How beneficial if it occurs?
• Opportunity Score = Probability × Impact

Example:
Opportunity: New battery cell chemistry increases range 10%
Probability: Possible (3)
Impact: Moderate (3) - competitive advantage, customer delight
Score: 9

OPPORTUNITY TREATMENT STRATEGIES:

1. EXPLOIT
   • Ensure opportunity definitely happens
   • Invest resources, remove barriers

   Example:
   New manufacturing process could reduce cost 20%
   Exploit: Fund process development, accelerate implementation,
   allocate best engineers

2. ENHANCE
   • Increase probability or positive impact

   Example:
   Battery cell opportunity (10% range increase)
   Enhance:
   - Early validation testing with cell supplier
   - Prepare design to accommodate new cells
   - Fast-track qualification process
   - Marketing plan ready for enhanced range announcement

3. SHARE
   • Partner to realize mutual benefit

   Example:
   New autonomous driving algorithm applicable to multiple vehicles
   Share: Co-develop with another OEM, share costs and IP

4. ACCEPT
   • Don't actively pursue, but be ready if it occurs

   Example:
   Competitor delay might create market window
   Accept: Monitor competitor status, have accelerated launch plan ready

OPPORTUNITY TREATMENT PLAN EXAMPLE:

Opportunity ID: O-023
Title: New battery cell chemistry could increase range 10%
Probability: 3 (Possible) | Impact: 3 (Moderate) | Score: 9

Strategy: ENHANCE

Actions:
1. Conduct early validation testing of new cells (Week 15-20)
   Owner: Battery Engineer
   Cost: $100K

2. Engage cell supplier in joint development (Week 12 onward)
   Owner: Purchasing Manager

3. Design battery pack to accommodate new cell dimensions (Week 18-24)
   Owner: Battery Design Team
   Cost: $50K (design margin)

4. Prepare fast-track qualification plan (Week 20)
   Owner: Quality Engineer

5. Develop marketing message for enhanced range (Week 25)
   Owner: Product Planning

Expected Outcome:
• Probability: 3 → 4 (Likely) with proactive engagement
• Impact: 3 → 4 (Major) if we're ready to adopt quickly
• New Score: 16 (High positive opportunity)

Success Metric:
If cells meet targets, integrate into production within 6 months
Achieve 440 km range vs 400 km baseline

→ Don't leave positive outcomes to chance; actively pursue opportunities
```

**Learning Outcomes:** LO1, LO2, LO3 - Opportunity management

---

#### Slide 21: Risk Reserves - Planning for Uncertainty
**Visual:** Diagram showing contingency reserve and management reserve

**Instructor Narration:**
> "Here's a critical question: How do you plan for uncertainty? You can't know exactly how much a project will cost or how long it will take, because risks exist. The answer: **Risk Reserves.**
>
> Two types of reserves:
>
> **Contingency Reserve** - Budget and schedule buffer for *known risks* (the ones in your risk register). You've identified them, analyzed them, but haven't eliminated them. If they occur, you use the contingency reserve.
>
> Example: Your risk register has 10 medium-high risks with potential cost impact of $5M total. You allocate a $3M contingency reserve (60% coverage). If risks materialize, you have budget to address them.
>
> **Management Reserve** - Buffer for *unknown risks* (the 'unknown unknowns'). Things you haven't anticipated. Typically 5-15% of project budget.
>
> Automotive programs always include reserves. **A project with no reserves is a fantasy.** Reality always includes uncertainty. Reserves acknowledge that and prepare for it.
>
> Key point: **Reserves are not slush funds.** They're risk-based, justified, and controlled. You spend reserves only for identified risks or approved changes."

**PPT Content:**
```
RISK RESERVES - Planning for Uncertainty

PURPOSE:
Allocate budget/schedule to address risks
without derailing the project

TWO TYPES OF RESERVES:

1. CONTINGENCY RESERVE
   • For KNOWN RISKS (in risk register)
   • Calculated based on risk analysis
   • Controlled by project manager
   • Used when identified risks occur

   Calculation Methods:
   a) Expected Monetary Value (EMV):
      For each risk: EMV = Probability × Impact ($)
      Contingency Reserve = Sum of all EMVs

      Example:
      Risk A: 30% × $1M = $300K
      Risk B: 50% × $500K = $250K
      Risk C: 20% × $2M = $400K
      Total Contingency Reserve = $950K

   b) Percentage of Identified Risks:
      Sum worst-case impact of all medium-high risks
      Reserve = 40-80% of total (based on treatment effectiveness)

      Example:
      Total identified risk exposure: $10M
      Contingency Reserve: 50% × $10M = $5M

2. MANAGEMENT RESERVE
   • For UNKNOWN RISKS ("unknown unknowns")
   • Things not yet identified
   • Controlled by senior management
   • Typically 5-15% of project budget
   • Requires management approval to use

   Example:
   Project Budget: $100M
   Management Reserve: 10% × $100M = $10M

TOTAL PROJECT BUDGET:

Base Estimate (most likely cost)        $85M
+ Contingency Reserve (known risks)     $10M
+ Management Reserve (unknown risks)    $10M
───────────────────────────────────────
Total Project Budget                   $105M

SCHEDULE RESERVES:

Same concept applies to schedule:
• Contingency time for known schedule risks
• Management reserve time for unknowns
• Often added as buffer at milestones or end of project

RESERVE MANAGEMENT:

✓ Document basis for reserve allocation
✓ Track reserve usage against risk occurrence
✓ Update reserves as risks change
✓ Replenish if new risks identified
✓ Release unused reserves at project end

AUTOMOTIVE CONTEXT:

• APQP programs include contingency in timelines
• Launch delays always have cost/schedule buffers
• Supplier agreements include penalty clauses (risk transfer)
• Warranty reserves for post-launch quality issues

COMMON MISTAKES:

✗ No reserves ("we'll hit the estimate exactly") → Unrealistic
✗ Reserves too large (padding) → Inflated budgets, reduces efficiency
✗ Reserves used as slush fund → Poor discipline
✗ Reserves not tracked → Don't know if risk management working

BEST PRACTICES:

✓ Risk-based reserve allocation
✓ Clear approval process for reserve use
✓ Track reserves separately from base budget
✓ Review and justify reserves at gates
✓ Return unused reserves at project close

→ Reserves are acknowledgment of reality, not pessimism
```

**Learning Outcomes:** LO1, LO2 - Risk reserves

---

#### Slide 22: Resilience Thinking - Beyond Risk Management
**Visual:** Comparison of risk management vs resilience thinking

**Instructor Narration:**
> "Let me introduce a concept that's gaining traction in systems engineering: **Resilience Thinking.**
>
> Traditional risk management is about **predicting and preventing** specific risks. Resilience is about **being able to respond and adapt** when unexpected events occur—even if you didn't predict them.
>
> **Resilience is the ability of a system (or project) to absorb disturbances, adapt, and continue functioning.**
>
> In automotive, resilience thinking means:
> - Designing systems with graceful degradation (not catastrophic failure)
> - Building flexible architectures that can accommodate changes
> - Developing teams with diverse skills who can pivot
> - Creating modular systems where one failure doesn't cascade
> - Planning for adaptation, not just prevention
>
> Example: Traditional risk management says 'Identify supplier risk, mitigate with contract terms.' Resilience thinking says 'Design supply chain with multiple sources, buffer inventory, and alternative materials so we can adapt if any supplier fails.'
>
> **Risk management is essential. Resilience thinking complements it.** You do both."

**PPT Content:**
```
RESILIENCE THINKING - Beyond Risk Management

DEFINITION:
Resilience is the ability to absorb disturbances,
adapt, and continue functioning despite unexpected events

RISK MANAGEMENT vs RESILIENCE:

RISK MANAGEMENT:
• Predict specific risks
• Prevent or mitigate those risks
• Control and reduce uncertainty
• "What could go wrong, and how do we prevent it?"

RESILIENCE THINKING:
• Assume unexpected events will occur
• Build capacity to respond and adapt
• Accept uncertainty as inherent
• "How do we keep functioning when the unexpected happens?"

→ Both are necessary; they complement each other

PRINCIPLES OF RESILIENCE:

1. DIVERSITY
   • Multiple options, alternatives, approaches
   • Don't rely on single solution

   Automotive Example:
   Diverse supply base (multiple suppliers for critical components)

2. MODULARITY
   • Loosely coupled subsystems
   • Failure in one module doesn't cascade

   Automotive Example:
   Modular electrical architecture (failure of infotainment
   doesn't affect safety-critical systems)

3. REDUNDANCY
   • Backup systems and components
   • Safety margins and reserves

   Automotive Example:
   Redundant braking systems (hydraulic + electric)
   Redundant power supplies for critical ECUs

4. ADAPTABILITY
   • Ability to change and evolve
   • Flexible architectures

   Automotive Example:
   Software-defined vehicle (can update and add features post-launch)
   Over-the-air update capability

5. GRACEFUL DEGRADATION
   • System degrades gradually, not catastrophically
   • Fail-safe and fail-operational modes

   Automotive Example:
   Autonomous vehicle: If sensor fails, degrade to lower automation
   level safely, don't crash

6. RAPID FEEDBACK & LEARNING
   • Detect issues quickly
   • Learn and adapt from failures

   Automotive Example:
   Real-time monitoring of vehicle health
   Fleet data analytics to identify emerging issues

RESILIENCE IN PROJECT MANAGEMENT:

• Cross-training team members (adaptability)
• Modular work packages (can reprioritize)
• Buffer resources (reserves for adaptation)
• Frequent reviews and feedback (rapid learning)
• Flexible schedules (can adjust to changes)
• Strong communication (enables coordination)

AUTOMOTIVE RESILIENCE EXAMPLES:

1. SUPPLY CHAIN RESILIENCE
   • Multiple suppliers for critical parts
   • Regional sourcing (not all from one geography)
   • Buffer inventory for long-lead items
   • Alternative materials designed in

2. SYSTEM RESILIENCE
   • Fail-operational architectures (safety systems)
   • Graceful degradation (ADAS features)
   • Redundant communication networks (CAN, FlexRay, Ethernet)
   • Software fault tolerance (watchdogs, error handling)

3. ORGANIZATIONAL RESILIENCE
   • Cross-functional teams (diverse skills)
   • Knowledge management (don't depend on individuals)
   • Lessons learned processes (learning from failures)
   • Crisis management plans (respond to unexpected)

WHEN TO EMPHASIZE RESILIENCE:

High uncertainty environments:
• New technology domains (autonomous, electrification)
• Complex systems with emergent behaviors
• Long timelines (5+ years) with changing requirements
• Global supply chains with geopolitical risks
• Safety-critical systems (cannot tolerate failure)

COMBINING RISK MANAGEMENT & RESILIENCE:

1. Identify and mitigate known risks (Risk Management)
2. Build resilience for unknown/unpredictable events (Resilience)
3. Design systems that are both preventive and adaptive

Example: Battery Supply Risk
• Risk Mgmt: Qualify multiple cell suppliers, contract terms
• Resilience: Design battery pack to accept different cell formats,
  maintain strategic inventory, develop in-house cell expertise

→ Plan for risks you know; build resilience for what you don't know
```

**Learning Outcomes:** LO3 - Advanced risk thinking

---

### **CLIMAX: Automotive Applications** (Slides 23-26, ~15 minutes)

**Narrative Voice:** Practical, connecting to real automotive programs

---

#### Slide 23: Automotive Program Management Context
**Visual:** Typical automotive development timeline with APQP phases

**Instructor Narration:**
> "Let's bring this to your world. Automotive programs are among the most complex product development efforts—3-5 year timelines, thousands of people, billions in investment, global supply chains, and zero tolerance for safety failures.
>
> The automotive industry uses specific frameworks: **APQP (Advanced Product Quality Planning)** in North America, **VDA-RGA** in Europe. These integrate systems engineering, project management, and quality management.
>
> APQP has five phases, each with defined deliverables and gate reviews. Let me show you how the project and risk management processes we've discussed integrate into APQP.
>
> **Everything you've learned today—WBS, scheduling, risk management—maps directly to automotive program management.** This isn't academic theory. This is how real vehicle programs are managed."

**PPT Content:**
```
AUTOMOTIVE PROGRAM MANAGEMENT

APQP (ADVANCED PRODUCT QUALITY PLANNING):
North American automotive standard
Five phases with gates:

PHASE 1: PLAN AND DEFINE PROGRAM
• Concept approval
• Business case and feasibility
• Preliminary requirements
→ Gate 1: Concept Approval

PHASE 2: PRODUCT DESIGN AND DEVELOPMENT
• Requirements engineering
• System and detail design
• Design verification (DVP&R)
• DFMEA
→ Gate 2: Design Release

PHASE 3: PROCESS DESIGN AND DEVELOPMENT
• Manufacturing process design
• Process FMEA
• Control plans
→ Gate 3: Process Validation

PHASE 4: PRODUCT AND PROCESS VALIDATION
• Production trial run
• Measurement systems analysis
• Production validation testing
→ Gate 4: Production Approval

PHASE 5: LAUNCH, FEEDBACK, ASSESSMENT, CORRECTIVE ACTION
• Start of production
• Continuous improvement
• Lessons learned
→ Ongoing production monitoring

SE PROJECT MANAGEMENT INTEGRATION:

PHASE 1 (Plan & Define):
• Define project scope
• Develop preliminary WBS
• Initial risk identification
• Conceptual architecture
→ SEMP initiated

PHASE 2 (Design & Development):
• Detailed WBS aligned with system architecture
• Integrated master schedule
• Requirements management plan
• Risk management plan
• Design reviews (PDR, CDR)
• DVP&R (verification planning)
→ SEMP baseline, detailed plans active

PHASE 3 (Process Design):
• Manufacturing integration planning
• Process verification planning
• Supply chain risk management
• Production schedule development

PHASE 4 (Validation):
• Validation execution and tracking
• Issue tracking and resolution (8D, CAPA)
• Launch readiness assessment
• Risk mitigation for launch

PHASE 5 (Launch & Production):
• Production monitoring
• Field performance tracking
• Lessons learned capture
• Continuous improvement

RISK MANAGEMENT IN APQP:

Phase 1: Initial risk identification (business, technical, market)
Phase 2: Design risk management (DFMEA, system FMEA, risk register)
Phase 3: Process risk management (PFMEA, supply chain)
Phase 4: Validation risks (test failures, approval delays)
Phase 5: Launch and field risks (quality, warranty, recalls)

GATE REVIEWS = RISK-BASED DECISIONS:

Each gate review assesses:
• Are objectives met?
• Are risks acceptable?
• Are we ready for next phase?
• Go / No-Go decision

VDA-RGA (GERMAN AUTOMOTIVE):
Similar structure, different terminology
• Maturity Level Assessment (MLA)
• Risk management integrated throughout
• Strong supplier integration

→ Automotive SE is embedded in program management frameworks
```

**Learning Outcomes:** LO2, LO4 - Automotive SE integration

---

#### Slide 24: Risk Management in Automotive Systems
**Visual:** Examples of automotive-specific risks across system lifecycle

**Instructor Narration:**
> "Let me give you specific automotive risk examples across the development lifecycle.
>
> **Concept Phase Risks:** Market acceptance uncertainty, technology feasibility (e.g., new propulsion system), business case sensitivity to cost/volume assumptions.
>
> **Design Phase Risks:** Requirements instability (customer keeps changing), integration complexity (100+ ECUs networked), supplier technical capability, software complexity and verification, safety hazard analysis gaps.
>
> **Validation Phase Risks:** Test facility availability, proving ground access, scenario coverage (can't test every possible condition), regulatory approval delays, certification test failures.
>
> **Production Phase Risks:** Manufacturing process yield, supply chain disruptions, quality escapes, launch timing (missing key sales season), cost overruns.
>
> **Post-Launch Risks:** Field failures and warranty costs, recall risks, cybersecurity vulnerabilities discovered, software bugs in deployed fleet.
>
> **Every one of these is real.** Every automotive program faces them. Your job as a systems engineer is to identify, analyze, and treat these risks proactively. That's how you prevent the next major recall."

**PPT Content:**
```
AUTOMOTIVE RISK EXAMPLES

CONCEPT PHASE RISKS:

Technical Risks:
• New propulsion technology not mature (TRL < 7)
• Performance targets not achievable with current technology
• Architecture concept has integration unknowns

Market Risks:
• Customer acceptance of new technology uncertain
• Competitor actions (feature parity, pricing)
• Regulatory changes (emissions, safety standards)

Business Risks:
• Business case sensitive to cost/volume assumptions
• Investment payback timeline long (>7 years)
• Insufficient funding allocated

DESIGN PHASE RISKS:

Requirements Risks:
• Requirements unstable (high change rate)
• Conflicting requirements (performance vs cost vs safety)
• Missing critical requirements
• Stakeholder alignment gaps

Technical Risks:
• System complexity beyond verification capability
• Integration risks (interfaces, timing, emergent behavior)
• Software size and complexity (defect density)
• Supplier technical capability gaps
• Technology obsolescence (long development cycles)

Safety Risks:
• FMEA gaps (failure modes not identified)
• Hazard analysis incomplete
• Safety architecture insufficient (single point failures)
• Cybersecurity vulnerabilities

Design Process Risks:
• Design review findings not closed
• Verification planning inadequate (DVP&R gaps)
• Traceability gaps (requirements to design to tests)

VALIDATION PHASE RISKS:

Test Execution Risks:
• Test facility availability (proving grounds, labs)
• Test equipment lead times
• Scenario coverage incomplete (can't test everything)
• Environmental testing (extreme conditions)
• Durability testing (accelerated aging)

Validation Results Risks:
• Test failures (design inadequate)
• Performance shortfalls (doesn't meet targets)
• Certification test failures (regulatory)
• Reliability issues discovered late

Schedule Risks:
• Validation takes longer than planned
• Rework cycles delay completion
• Regulatory approval delays (certifications)

PRODUCTION PHASE RISKS:

Manufacturing Risks:
• Process yield issues (new processes)
• Tooling delays or quality issues
• Assembly complexity (fit, tolerance)
• Supply chain disruptions (part shortages)
• Quality escapes (defects not caught)

Launch Risks:
• Launch timing (miss key sales season)
• Ramp-up slower than planned (volume)
• Cost overruns (manufacturing not optimized)
• Training gaps (assembly workers, service technicians)

POST-LAUNCH RISKS:

Field Performance Risks:
• Reliability issues (early failures)
• Warranty costs higher than predicted
• Software bugs in deployed fleet
• Cybersecurity vulnerabilities discovered
• Recall risk (safety-critical defects)

Market Risks:
• Customer satisfaction below target
• Competitive pressure (better products launched)
• Demand different than forecast

RISK EXAMPLE: BATTERY ELECTRIC VEHICLE

Technical Risk: Battery thermal runaway
• Probability: Unlikely (2)
• Impact: Catastrophic (5) - safety, recall, brand damage
• Score: 10 (High)
• Treatment:
  - Mitigation: Rigorous FMEA, thermal testing, battery management system design
  - Mitigation: Cell-level and pack-level safety features
  - Mitigation: Abuse testing (overcharge, crush, thermal)
  - Contingency: Recall plan, field monitoring

Supply Chain Risk: Battery cell shortages
• Probability: Possible (3)
• Impact: Major (4) - production delays, cost increases
• Score: 12 (High)
• Treatment:
  - Mitigation: Multi-source strategy (2-3 cell suppliers qualified)
  - Mitigation: Long-term supply agreements with volume commitments
  - Transfer: Penalty clauses in supplier contracts
  - Accept: Strategic inventory buffer (3-month supply)

Software Risk: Over-the-air update failures
• Probability: Possible (3)
• Impact: Major (4) - customer dissatisfaction, safety if critical update
• Score: 12 (High)
• Treatment:
  - Mitigation: Robust update architecture (rollback capability)
  - Mitigation: Phased rollout (fleet segmentation)
  - Mitigation: Comprehensive testing before deployment
  - Contingency: Service center reflash capability

→ Automotive risk management is continuous, lifecycle-wide
```

**Learning Outcomes:** LO2, LO4 - Automotive risks

---

#### Slide 25: Integration with ISO 26262 Functional Safety
**Visual:** Relationship between risk management and functional safety

**Instructor Narration:**
> "If you're working on safety-critical automotive systems—and most of you will be—you need to understand the relationship between risk management and **ISO 26262 Functional Safety.**
>
> ISO 26262 is the automotive functional safety standard. It's a risk-based approach to safety—identify hazards, assess risks, implement safety measures to reduce risk to acceptable levels.
>
> Here's the key: **ISO 26262 is a specialized form of risk management focused on safety hazards.** The risk management process we discussed today is broader—it includes schedule, cost, technical, business risks. ISO 26262 focuses on risks to human safety.
>
> They integrate this way:
> - **Your general risk register** includes all project risks
> - **Hazard analysis (ISO 26262)** identifies safety-specific risks
> - **ASIL (Automotive Safety Integrity Level)** ratings drive safety requirements
> - **Safety goals and safety requirements** get traced through the system
> - **Safety validation** is part of your overall verification and validation
>
> Bottom line: If your system is safety-critical, you do both general risk management AND functional safety analysis. They're complementary, not competing."

**PPT Content:**
```
INTEGRATION: RISK MANAGEMENT & ISO 26262 FUNCTIONAL SAFETY

ISO 26262 OVERVIEW:
Automotive functional safety standard
Risk-based approach to prevent unreasonable safety risks

RELATIONSHIP TO RISK MANAGEMENT:

GENERAL RISK MANAGEMENT (ISO/IEC 15288):
• Broad scope: Technical, schedule, cost, business, safety, etc.
• All project risks
• Risk register with all identified risks

ISO 26262 FUNCTIONAL SAFETY:
• Narrow scope: Safety hazards and risks to human life
• Safety-specific risk assessment
• Hazard Analysis and Risk Assessment (HARA)
• Automotive Safety Integrity Level (ASIL) ratings

→ ISO 26262 is specialized risk management for safety

INTEGRATION POINTS:

1. HAZARD IDENTIFICATION
   General Risk ID → Identifies some safety hazards
   ISO 26262 HARA → Systematically identifies all safety hazards
   Both feed into → Comprehensive risk/hazard register

2. RISK ANALYSIS
   General Risk Analysis → Probability × Impact (cost, schedule, etc.)
   ISO 26262 HARA → Severity × Exposure × Controllability → ASIL
   Both drive → Prioritization and treatment

3. RISK TREATMENT
   General Risk → Avoid, Mitigate, Transfer, Accept
   ISO 26262 → Safety requirements, ASIL decomposition, safety mechanisms
   Both result in → Design requirements and verification

4. RISK MONITORING
   General Risk → Track risk register, evaluate treatment
   ISO 26262 → Safety validation, functional safety assessment
   Both provide → Ongoing assurance

EXAMPLE: BRAKING SYSTEM

General Risk Management:
Risk: Brake system performance below target
• Probability: Unlikely (2)
• Impact: Major (4) - rework, cost
• Score: 8
• Treatment: Early testing, design reviews

ISO 26262 Functional Safety:
Hazard: Unintended brake application during normal driving
• Severity: S3 (severe injuries possible)
• Exposure: E4 (high probability of exposure)
• Controllability: C2 (normally controllable)
• ASIL: D (highest)
• Treatment:
  - Safety goal: "Prevent unintended brake application"
  - Safety requirements: Redundant sensors, plausibility checks
  - Safety architecture: Fail-safe design
  - Verification: Fault injection testing, FMEA

BOTH PERSPECTIVES MANAGED:
• Risk register includes performance risk
• HARA and safety case address safety hazards
• Integrated verification plan covers both

PROCESS INTEGRATION:

SE Risk Management Plan includes:
• General risk identification and treatment
• Reference to ISO 26262 safety activities
• Integration of safety requirements into system requirements
• Verification of both functional and safety requirements

ISO 26262 Safety Plan includes:
• Hazard analysis and risk assessment
• ASIL determination
• Safety concept and architecture
• Verification and validation of safety
• Functional safety assessment

→ Systems Engineer coordinates both; ensures integration

KEY TAKEAWAY:
If your system is safety-critical:
✓ Do general risk management (ISO/IEC 15288)
✓ Do functional safety analysis (ISO 26262)
✓ Integrate them into a coherent approach
✓ Ensure safety risks are treated with highest rigor

→ Safety risks cannot be "accepted" like other risks
```

**Learning Outcomes:** LO2, LO4 - Safety integration

---

#### Slide 26: Case Study Integration - Mars Orbiter Lessons Applied
**Visual:** Mars Orbiter failure mapped to risk/project management gaps

**Instructor Narration:**
> "Let's come full circle. Remember the Mars Climate Orbiter from the beginning of this session? $327 million lost due to a units conversion error. Let's analyze it through the lens of project and risk management.
>
> **Project Management Failures:**
> - No interface control document between teams (planning failure)
> - Assumptions not documented (planning failure)
> - No verification checkpoint for interface data (control failure)
> - Inadequate communication between teams (organizational failure)
>
> **Risk Management Failures:**
> - Risk of units mismatch not identified (identification failure)
> - No risk review of interface assumptions (analysis failure)
> - No mitigation plan for critical interfaces (treatment failure)
>
> **How it could have been prevented:**
>
> **1. Project Planning:** WBS includes interface control document development. Schedule includes interface verification reviews. Resources allocated for independent verification.
>
> **2. Risk Management:** Risk identified: 'Interface units mismatch between Team A and Team B.' Probability: Possible. Impact: Catastrophic. Treatment: Mitigate with interface control document, verification tests, automated unit conversion checks.
>
> **3. Assessment & Control:** Track interface document completion. Review interface data at milestones. Red flag if verification not completed.
>
> **This is why we do project and risk management.** A simple, cheap process would have saved $327 million and a mission. The technical solution was brilliant. The management failed.
>
> Your takeaway: **Technical excellence without management discipline = disaster.**"

**PPT Content:**
```
CASE STUDY: MARS CLIMATE ORBITER - PM/RM ANALYSIS

INCIDENT RECAP:
• Sept 23, 1999: Spacecraft lost entering Mars orbit
• Root cause: Units conversion error (metric vs imperial)
• Cost: $327.6 million

PROJECT MANAGEMENT FAILURES:

1. PLANNING FAILURE
   ✗ No Interface Control Document (ICD) between teams
   ✗ Assumptions not explicitly documented
   ✗ Interface verification not in project plan
   ✗ Insufficient resources allocated for integration review

2. ORGANIZATIONAL FAILURE
   ✗ Teams working independently without coordination
   ✗ Communication gaps between navigation and propulsion teams
   ✗ No integration lead with authority across teams

3. CONTROL FAILURE
   ✗ No verification checkpoint for interface data
   ✗ No independent review of critical calculations
   ✗ Anomalies during trajectory not investigated thoroughly
   ✗ No technical performance measures for trajectory accuracy

RISK MANAGEMENT FAILURES:

1. RISK IDENTIFICATION FAILURE
   ✗ Risk of units mismatch NOT identified
   ✗ Interface risks not systematically analyzed
   ✗ Assumption analysis not performed

2. RISK ANALYSIS FAILURE
   ✗ No risk assessment of critical interfaces
   ✗ Interface failure impacts not evaluated
   ✗ Single points of failure not identified

3. RISK TREATMENT FAILURE
   ✗ No mitigation plan for interface verification
   ✗ No redundant calculation checks
   ✗ No automated unit conversion checks

4. RISK MONITORING FAILURE
   ✗ Trajectory anomalies not treated as risk triggers
   ✗ No risk review of navigation data quality

HOW IT COULD HAVE BEEN PREVENTED:

PROJECT PLANNING PROCESS:

WBS Element: "Interface Management"
- Deliverable: Interface Control Document (ICD) for all inter-team data
- Content: Units, coordinate systems, data formats, validation
- Owner: Integration Lead
- Timeline: Complete before detailed design
- Resources: 2 engineers, 4 weeks

Schedule Milestone: "Interface Verification Review"
- Gate before integration
- Verify all interface data exchanged
- Test interface compatibility
- Sign-off required from both teams

RISK MANAGEMENT PROCESS:

RISK IDENTIFICATION:
Risk ID: R-025
Title: Units conversion mismatch between Navigation and Propulsion teams
Category: Technical - Interface
Description: Navigation team uses metric (N·s), Propulsion team uses
imperial (lbf·s). Risk of unconverted data causing trajectory error.

RISK ANALYSIS:
Probability: Possible (3) - Different teams, different backgrounds
Impact: Catastrophic (5) - Mission loss if trajectory wrong
Risk Score: 15 (HIGH - Red Zone)
Priority: Immediate treatment required

RISK TREATMENT:
Strategy: MITIGATE (eliminate risk as much as possible)

Actions:
1. Develop Interface Control Document (ICD) specifying units
   Owner: Integration Lead | Due: Week 10 | Cost: $20K

2. Implement automated unit conversion checks in software
   Owner: Software Lead | Due: Week 20 | Cost: $50K

3. Conduct interface verification tests (data exchange validation)
   Owner: Test Engineer | Due: Week 30 | Cost: $30K

4. Independent review of all interface data before mission
   Owner: Systems Engineer | Due: Week 50 | Cost: $40K

5. Peer review of trajectory calculations by external expert
   Owner: Chief Engineer | Due: Week 52 | Cost: $25K

Total Mitigation Cost: $165K

Residual Risk:
Probability: Rare (1) - Multiple checks in place
Impact: Catastrophic (5) - Still mission-critical
Score: 5 (Medium) - Acceptable with contingency monitoring

Contingency Plan:
• Monitor trajectory accuracy throughout mission
• Trigger: Trajectory deviates >1% from prediction
• Response: Halt, investigate data, verify calculations

RISK MONITORING:
• Weekly: Review interface data quality metrics
• Monthly: Risk review of all interface risks
• Milestone: Interface verification review (gate)
• Trigger: Any trajectory anomaly → immediate investigation

COST-BENEFIT:
Prevention Cost: $165K
Mission Loss: $327.6 million
ROI: 1,990x return on risk mitigation investment

PROJECT ASSESSMENT & CONTROL:
• Technical Performance Measure (TPM): Trajectory prediction accuracy
• Measured: Predicted position vs actual position during cruise
• Target: <0.1% deviation
• Action: If deviation >0.5% → Root cause analysis and correction

LESSONS LEARNED FOR AUTOMOTIVE SE:

1. INTERFACES ARE CRITICAL
   → Develop ICDs for all system interfaces
   → Verify interface compatibility explicitly

2. ASSUMPTIONS ARE HIDDEN RISKS
   → Document all assumptions
   → Validate assumptions through analysis or test
   → Include assumption analysis in risk identification

3. VERIFICATION IS ESSENTIAL
   → Independent verification of critical data/calculations
   → Automated checks where possible
   → Multiple verification methods (analysis + test)

4. COST OF PREVENTION << COST OF FAILURE
   → $165K mitigation vs $327M loss
   → Risk management has extraordinary ROI
   → "We don't have time/budget for this" is false economy

5. MANAGEMENT DISCIPLINE PREVENTS TECHNICAL DISASTERS
   → Technical brilliance alone is insufficient
   → Planning, risk management, and control are essential
   → Systems engineering IS management + technical work

REFLECTION QUESTION:
In your automotive projects, what interfaces are you assuming will work?
Have you verified those assumptions? What risks are hidden in those interfaces?

→ This disaster was preventable with basic SE management practices
```

**Learning Outcomes:** LO1, LO2, LO3 - Integrated application

---

### **RESOLUTION: Key Takeaways & Moving Forward** (Slides 27-30, ~15 minutes)

**Narrative Voice:** Synthesizing, empowering, forward-looking

---

#### Slide 27: Key Takeaways - Session 9
**Visual:** Clean summary with key points

**Instructor Narration:**
> "Let's consolidate what you learned today. Write these down:
>
> **1. Technical management IS systems engineering.** Planning, assessment, and risk management are not overhead—they're how you execute SE work successfully.
>
> **2. Project planning provides structure.** WBS aligned with architecture, schedules with dependencies, resources allocated realistically. Without planning, you're hoping, not engineering.
>
> **3. Risk management is proactive, not reactive.** Identify, analyze, treat, and monitor risks continuously. Opportunities too. Don't leave outcomes to chance.
>
> **4. Reserves are acknowledgment of reality.** Contingency for known risks, management reserve for unknowns. Projects without reserves are fantasies.
>
> **5. Automotive programs integrate SE into APQP/VDA frameworks.** Everything you learned maps directly to real vehicle development.
>
> **6. Prevention is far cheaper than correction.** Mars Orbiter: $165K mitigation vs $327M loss. Risk management has extraordinary ROI.
>
> Master these practices, and you'll be a complete systems engineer—technical excellence with management discipline."

**PPT Content:**
```
KEY TAKEAWAYS - SESSION 9

1. TECHNICAL MANAGEMENT IS SYSTEMS ENGINEERING
   • Planning, assessment, risk management ARE SE processes
   • Not overhead; essential for execution
   • ISO/IEC 15288 Technical Management Processes

2. PROJECT PLANNING PROVIDES STRUCTURE
   • WBS aligned with system architecture
   • Schedule with dependencies and critical path
   • Resource allocation (people, budget, tools)
   • Plans are living documents, updated continuously

3. RISK MANAGEMENT IS PROACTIVE
   • Identify risks and opportunities continuously
   • Analyze probability and impact; prioritize
   • Treat with appropriate strategies (Avoid/Mitigate/Transfer/Accept)
   • Monitor and control throughout lifecycle
   • Risk register is essential tool

4. RESERVES ACKNOWLEDGE REALITY
   • Contingency reserve for known risks
   • Management reserve for unknown risks
   • Risk-based allocation, controlled use
   • Projects without reserves are unrealistic

5. RESILIENCE COMPLEMENTS RISK MANAGEMENT
   • Risk management: Predict and prevent
   • Resilience: Adapt and continue despite unexpected
   • Build diversity, modularity, redundancy, adaptability

6. AUTOMOTIVE INTEGRATION
   • SE planning integrates with APQP/VDA
   • Risk management throughout vehicle development
   • Functional safety (ISO 26262) is specialized risk management
   • Real programs use these practices daily

7. PREVENTION >> CORRECTION
   • Mars Orbiter: $165K mitigation vs $327M loss
   • Early planning prevents late chaos
   • Risk management has extraordinary ROI
   • Management discipline prevents technical disasters

→ You are now equipped for technical project and risk management
```

**Learning Outcomes:** LO1, LO2, LO3

---

#### Slide 28: Practical Application - Starting Your Risk Register
**Visual:** Template risk register with example entries

**Instructor Narration:**
> "I want you to leave today ready to apply this. Here's a practical exercise:
>
> **For your next project—class project, thesis, or at work—create a risk register.** Spend 30 minutes brainstorming risks. Use the risk breakdown structure. Identify 10-20 risks.
>
> For each risk:
> - Write a clear description
> - Assess probability and impact
> - Calculate risk score
> - Identify the owner (who's responsible)
> - Document at least one treatment action
>
> Then **review your risk register weekly**. Add new risks. Update scores. Track mitigation progress. This simple practice will transform how you manage projects.
>
> I guarantee: If you consistently use a risk register, you'll avoid 80% of project surprises. Most failures come from risks that were identifiable but not managed. Don't be that project."

**PPT Content:**
```
PRACTICAL APPLICATION: Your First Risk Register

EXERCISE: Create a Risk Register

For your next project (class, thesis, work):

STEP 1: IDENTIFY RISKS (30 minutes)
Brainstorm using Risk Breakdown Structure:
• Technical risks (5-10 risks)
• Schedule risks (2-5 risks)
• Resource risks (2-5 risks)
• External risks (2-5 risks)

Target: 10-20 risks to start

STEP 2: ANALYZE EACH RISK
For each risk:
• Probability: Rare/Unlikely/Possible/Likely/Almost Certain (1-5)
• Impact: Negligible/Minor/Moderate/Major/Catastrophic (1-5)
• Risk Score: Probability × Impact
• Priority: High (15-25), Medium (6-14), Low (1-5)

STEP 3: DOCUMENT RISK REGISTER
Use simple spreadsheet or table:

| ID  | Risk Description | Category | Prob | Impact | Score | Owner | Treatment Strategy | Actions | Status |
|-----|------------------|----------|------|--------|-------|-------|-------------------|---------|--------|
| R-01| Requirements unstable | Technical | 3 | 4 | 12 | SE Lead | Mitigate | Early stakeholder engagement, baseline control | Open |
| R-02| Test equipment delay | Schedule | 2 | 3 | 6 | Test Eng | Mitigate | Order early, backup plan | Open |

STEP 4: DEVELOP TREATMENT PLANS
For HIGH risks (score >12):
• Define specific mitigation actions
• Assign owners and deadlines
• Allocate resources (time, budget)

For MEDIUM risks (score 6-12):
• Identify treatment strategy
• Monitor triggers

For LOW risks (score <6):
• Accept or monitor

STEP 5: REVIEW WEEKLY
• 15-minute risk review each week
• Add new risks identified
• Update probability/impact as info improves
• Mark completed mitigations
• Close resolved risks

EXAMPLE RISK REGISTER FOR STUDENT PROJECT:

R-01: Requirements Unstable
• Description: Customer may change requirements mid-project
• Category: Technical - Requirements
• Probability: Possible (3)
• Impact: Major (4) - rework, schedule delay
• Score: 12 (High)
• Owner: Project Lead
• Treatment: Mitigate
  - Action 1: Baseline requirements at Week 3, change control after
  - Action 2: Weekly stakeholder check-ins to catch changes early
  - Action 3: Allocate 20% schedule buffer for requirement changes
• Status: Open - Actions in progress

R-02: Team Member Unavailable
• Description: Team member may have competing commitments (other classes, work)
• Category: Resource
• Probability: Likely (4)
• Impact: Moderate (3) - work redistribution needed
• Score: 12 (High)
• Owner: Team Lead
• Treatment: Mitigate
  - Action 1: Cross-train team members (each knows 2+ work areas)
  - Action 2: Modular work packages (can reassign easily)
  - Action 3: Weekly availability check with team
• Status: Open

R-03: Software Tool Learning Curve
• Description: Team unfamiliar with SysML tool, may take time to learn
• Category: Technical - Tools
• Probability: Possible (3)
• Impact: Minor (2) - slight schedule impact
• Score: 6 (Medium)
• Owner: Systems Engineer
• Treatment: Mitigate
  - Action 1: Complete online tutorial (Week 1)
  - Action 2: Practice model in Week 2 before real work
• Status: Open

BENEFITS YOU'LL SEE:
✓ Fewer surprises (anticipated risks)
✓ Proactive instead of reactive
✓ Clear communication of challenges
✓ Documented decision-making
✓ Reduced stress (know what could go wrong, have a plan)

TOOLS:
• Simple spreadsheet (Excel, Google Sheets)
• Project management tools (MS Project, Jira, etc.)
• Specialized risk management software (for large programs)

START SIMPLE. GROW AS NEEDED.

→ Risk register is the single most valuable PM tool you can use
```

**Learning Outcomes:** LO2 - Practical application

---

#### Slide 29: Connection to Next Session
**Visual:** Preview of Session 10 topics

**Instructor Narration:**
> "Today we covered three of the four Technical Management Processes: Project Planning, Project Assessment and Control, and Risk Management.
>
> **Next session, we complete the picture with Decision Management and Quality Management.**
>
> You'll learn how to make informed technical decisions systematically—not by gut feel, but by structured analysis. We'll cover decision analysis techniques, trade studies, and multi-criteria decision methods.
>
> And we'll explore Quality Management—how to ensure your SE work produces high-quality deliverables. Quality planning, quality assurance, quality control. The difference between verification (built it right) and validation (built the right thing).
>
> Together, Sessions 9 and 10 give you the complete technical management toolkit. You'll be able to plan SE work, manage risks, make decisions, and ensure quality. That's professional systems engineering.
>
> See you next session!"

**PPT Content:**
```
NEXT SESSION: DECISION AND QUALITY MANAGEMENT

SESSION 10 PREVIEW:

DECISION MANAGEMENT PROCESS:
• Systematic decision-making
• Trade studies and alternatives analysis
• Multi-criteria decision analysis (MCDA)
• Pugh matrices, AHP (Analytic Hierarchy Process)
• Decision documentation and traceability
• Automotive decision examples (architecture, supplier selection, technology)

QUALITY MANAGEMENT PROCESS:
• Quality planning (what quality means for SE)
• Quality assurance (process compliance)
• Quality control (deliverable verification)
• Reviews and audits
• Lessons learned and continuous improvement

INTEGRATION:
How decision and quality management integrate with:
• Project planning (from today)
• Risk management (from today)
• Requirements engineering (Session 4)
• Verification and validation (Session 8)

AUTOMOTIVE APPLICATIONS:
• Design reviews (PDR, CDR)
• Trade studies in vehicle development
• Quality gates in APQP
• Supplier quality management

COMPLETE TECHNICAL MANAGEMENT:
Session 9 + Session 10 = Full technical management capability
• Plan → Assess & Control → Manage Risks → Make Decisions → Ensure Quality

PREPARATION FOR SESSION 10:
• Review: Requirements engineering (Session 4)
• Review: Verification & Validation (Session 8)
• Think about: Decisions you've made in projects - how did you choose?
• Read: ISO/IEC 15288 Decision Management and Quality Management sections

→ Two sessions to master SE management
```

**Learning Outcomes:** LO1 - Course continuity

---

#### Slide 30: Q&A and Discussion
**Visual:** Discussion prompts

**Instructor Narration:**
> "We have about 15 minutes for questions and discussion. Here are some topics we can explore:
>
> - How to apply project planning to your specific projects
> - Risk identification techniques—what works in practice
> - How to convince teams/managers to invest in risk management
> - Automotive examples from your experience or interests
> - Integration of SE planning with agile or iterative development
> - How to start building these practices if your organization doesn't use them
>
> What questions do you have?"

**PPT Content:**
```
Q&A / DISCUSSION

Open Questions:

1. PROJECT PLANNING
   • How detailed should a WBS be?
   • How to estimate task durations realistically?
   • Agile/Scrum vs traditional planning for SE?

2. RISK MANAGEMENT
   • How to identify risks you don't know about?
   • How to get team buy-in for risk management?
   • When is risk management "enough"?

3. AUTOMOTIVE APPLICATIONS
   • Specific vehicle program experiences?
   • How do Tier 1 suppliers manage these processes?
   • Startup vs established OEM approaches?

4. PRACTICAL IMPLEMENTATION
   • Starting risk management in an organization that doesn't do it?
   • Tools and templates—what's recommended?
   • How much time to spend on planning vs doing?

5. ADVANCED TOPICS
   • Quantitative risk analysis (Monte Carlo, etc.)
   • Earned Value Management (EVM) for large programs
   • Risk in agile/iterative development
   • AI/ML for project and risk management

6. CAREER & SKILLS
   • What makes a good project/risk manager?
   • Certifications (PMP, PMI-RMP)?
   • How much management vs technical work for SE role?

What questions do you have?
```

**Learning Outcomes:** Discussion and deeper understanding

---

## 📊 PPT DESIGN GUIDANCE

### Visual Style:
- **Professional engineering aesthetic**: Clean, modern layouts
- **Color scheme**:
  - Primary: Deep blue (trust, engineering)
  - Secondary: Gray/silver (technical, structured)
  - Accent: Orange/red for risks, green for opportunities
  - Yellow for caution/medium priority
- **Typography**: Sans-serif, highly readable
- **Consistent template** with slide numbering

### Key Slides to Emphasize:
1. **Slide 3** (Mars Orbiter) - Compelling failure story
2. **Slide 10** (WBS) - Clear hierarchical diagram
3. **Slide 11** (Scheduling) - Gantt chart with critical path highlighted
4. **Slide 17** (Risk Matrix) - Visual risk plotting
5. **Slide 26** (Case Study Integration) - Comprehensive analysis
6. **Slide 27** (Key Takeaways) - Students will photograph this

### Animations:
- **Minimal and professional**
- Use **build animations** for:
  - WBS hierarchy (reveal levels)
  - Risk matrix (plot risks one by one)
  - Process flows (step-by-step)
- **Highlight/emphasis** for key terms

### Visual Elements:
- **Process diagrams**: Clear flowcharts for PM and RM processes
- **Gantt charts**: Professional timeline visualization
- **Risk matrices**: Color-coded (red/yellow/green zones)
- **Organizational charts**: Showing WBS structure
- **Example documents**: Risk register, SEMP table of contents

### Technical Diagrams:
- Clear **WBS hierarchies** (tree structure or indented list)
- **Network diagrams** for scheduling (critical path highlighted)
- **Risk breakdown structure** (categorical tree)
- **Integration diagrams** showing how PM/RM connect to technical processes

---

## 🎯 INSTRUCTOR NOTES

### Pedagogical Strategy:
This session uses **Case-Based Learning with Structured Frameworks** to:
1. **Motivate with failure** (Mars Orbiter) → Why management matters
2. **Build systematic knowledge** (ISO 15288 processes) → How to do it right
3. **Provide practical tools** (WBS, risk register) → What to use
4. **Apply to automotive** (APQP, ISO 26262) → Where it's used
5. **Integrate with case study** (Mars Orbiter revisited) → Synthesis

### Timing Breakdown (120 minutes total):
- **Setup (Slides 1-8)**: 20 minutes - Motivation and framework
- **Trigger (Slides 9-14)**: 25 minutes - Project Planning Process
- **Rising Action (Slides 15-22)**: 30 minutes - Risk Management Process
- **Climax (Slides 23-26)**: 15 minutes - Automotive Applications
- **Resolution (Slides 27-30)**: 15 minutes - Takeaways and Q&A
- **Buffer**: 15 minutes for questions/flexibility

### Common Student Questions/Challenges:

**Q: "This seems like a lot of process. Do we really need all this?"**
A: Tailor to project complexity. Small project = lightweight. Large automotive program = rigorous. But the thinking and key practices always apply.

**Q: "What if management doesn't support risk management?"**
A: Start small—personal risk register for your work. Demonstrate value with prevented issues. Build credibility. Management supports what works.

**Q: "How do I estimate probability and impact accurately?"**
A: Use historical data when available, expert judgment otherwise. Precision is less important than thoughtful analysis and consistent application. Improve estimates as you learn.

**Q: "Isn't this just for project managers, not engineers?"**
A: No—systems engineers must integrate technical and management work. You're not just designing; you're leading technical work. These are SE processes, not just PM processes.

### Engagement Strategies:

1. **During planning (Slides 9-14)**:
   - Ask students to sketch a WBS for a familiar system (their phone, laptop)
   - Identify dependencies in a simple project
   - Estimate durations for a class project

2. **During risk management (Slides 15-22)**:
   - Brainstorm risks for a hypothetical EV development program (5 min)
   - Plot 2-3 risks on a risk matrix
   - Identify treatment strategies for student-generated risks

3. **During automotive application (Slides 23-26)**:
   - Ask students with industry experience to share risk examples
   - Discuss how their organizations handle PM/RM (if applicable)
   - Mars Orbiter: "What would YOU have done differently?"

### Flexibility Options:

**If running SHORT (need to finish in 100 minutes):**
- Reduce risk monitoring detail (Slide 19)
- Shorten automotive integration (fewer examples)
- Reduce Q&A time

**If running LONG (have 140 minutes):**
- Deep dive into EVM (earned value management)
- Additional automotive risk examples
- Hands-on risk register exercise (breakout groups)
- Extended case study discussion

**Core Content (Must Cover):**
- ISO/IEC 15288 Technical Management Processes (Slide 7)
- WBS and scheduling (Slides 10-11)
- Risk identification, analysis, treatment, monitoring (Slides 16-19)
- Automotive integration (Slide 23-24)
- Mars Orbiter lessons (Slide 26)
- Key takeaways (Slide 27)

---

## ✅ Session Success Criteria

Students leave able to:
- ✓ Explain the four Technical Management Processes of ISO/IEC 15288
- ✓ Develop a work breakdown structure aligned with system architecture
- ✓ Create project schedules with dependencies and critical path
- ✓ Identify, analyze, and treat risks systematically
- ✓ Maintain a risk register for their projects
- ✓ Understand integration of SE planning with automotive programs (APQP)
- ✓ Recognize that management discipline prevents technical disasters

**Most importantly:** Students understand that **technical management IS systems engineering**, not overhead. They can plan SE work and manage risks proactively.

### Mindset Shift Achieved:
From: "Project and risk management is PM work, not engineering work"
To: "Technical management is essential SE practice; I must master both technical and management skills"

---

## 🔗 Bridge to Session 10

**Setup for Next Session:**
> "Today you learned to plan SE work and manage risks—essential for project success. Next session, we complete technical management with Decision Management and Quality Management. You'll learn to make technical decisions systematically and ensure the quality of your SE deliverables. Together, these give you the complete management toolkit for systems engineering. See you next time."

---

**End of Framework**

**Framework Summary:**
- **Total Slides:** 30
- **Story Arc:** Complete - Setup (motivation) → Trigger (planning) → Rising Action (risk) → Climax (automotive) → Resolution (synthesis)
- **Engagement:** High - Case study, practical tools, exercises
- **Learning Outcomes:** LO1, LO2, LO3 thoroughly addressed
- **Automotive Context:** Strong - APQP integration, ISO 26262, real risks

**Next Step:** Instructor develops PowerPoint slides using this framework, inserting appropriate visuals and adapting for classroom dynamics.
