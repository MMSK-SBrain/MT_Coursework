# Session 4: Requirements Engineering
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 90 minutes lecture + 30 minutes Q&A
**Approach:** Process-Based/Practical
**PPT Target:** 28-30 slides

---

## 🎯 Session Objectives (For Instructor)

By the end of this session, students will be able to:
- Distinguish between stakeholder needs and system requirements
- Identify and analyze stakeholders systematically
- Classify requirements into functional, non-functional, and constraint categories
- Apply requirements quality attributes (verifiable, traceable, clear, unambiguous)
- Create and use a requirements traceability matrix
- Recognize common requirements engineering pitfalls and anti-patterns
- Select appropriate requirements management tools and processes

**Mapped Learning Outcomes:** LO2 (Develop requirements, architectures, specifications, verifications, and tests), LO4 (Apply systems engineering practices and methods in automotive systems)

---

## 📖 INSTRUCTOR-LED STORY ARC

### **SETUP: The Critical Foundation** (Slides 1-5, ~10 minutes)

#### Slide 1: Title
**Visual:** Professional title slide with pyramid showing requirements as foundation
**Instructor Script:**
> "Welcome to Session 4. Today we tackle what many consider the MOST critical process in systems engineering: Requirements Engineering.
>
> Get requirements wrong, and everything that follows is built on a faulty foundation. Get them right, and you've set yourself up for success."

#### Slide 2: Connection to Previous Sessions
**Visual:** Progression diagram showing Sessions 1→2→3→4
**Instructor Script:**
> "Let's connect the journey we've been on:
>
> **Session 1**: We learned WHY systems engineering matters through failure cases. Poor requirements were at the root of many disasters.
>
> **Session 2**: We learned the SE framework - ISO/IEC 15288 technical processes. The FIRST technical process? Stakeholder needs and requirements definition.
>
> **Session 3**: We explored Traditional vs MBSE approaches. Both start with the same thing: defining requirements.
>
> Today's focus: **How do we actually DO requirements engineering in practice?**"

#### Slide 3: Why Requirements Engineering Is Critical
**Visual:** Statistics showing project failure causes
**Instructor Script:**
> "Let me show you some sobering data from the Standish Group's CHAOS Report:
>
> **Top causes of project failure:**
> - 37% - Incomplete requirements
> - 28% - Lack of user involvement (stakeholder engagement)
> - 19% - Lack of resources
> - 16% - Unrealistic expectations (poor requirements management)
>
> **Over 65% of failures trace back to requirements issues.**
>
> **In automotive systems:**
> - Average cost to fix a requirements defect found in design: $1,000
> - Average cost if found in testing: $10,000
> - Average cost if found after production: $100,000+
> - Recalls due to requirements failures: Millions of dollars
>
> This is why we spend today mastering this discipline."

#### Slide 4: Real-World Example - The Mars Climate Orbiter
**Visual:** Mars Climate Orbiter with timeline of failure
**Instructor Script:**
> "Remember this from Session 1? The $327 million Mars Climate Orbiter lost because one team used metric units, another used imperial.
>
> **Requirements failure analysis:**
> - **Root cause**: Interface requirement didn't specify units
> - **What was missing**: 'The navigation software shall output thrust values in Newtons (N)'
> - **What was assumed**: Teams made different assumptions
>
> A single missing word - the UNIT of measurement - destroyed the mission.
>
> **This is the power and precision requirements engineering demands.**"

#### Slide 5: Learning Journey for Today
**Visual:** Roadmap with 6 key stops
**Instructor Script:**
> "Today's journey takes us through six critical areas:
>
> **Part 1**: Stakeholder Identification - Who matters and why?
> **Part 2**: Needs vs Requirements - Understanding the distinction
> **Part 3**: Types of Requirements - Functional, non-functional, constraints
> **Part 4**: Requirements Attributes - What makes a good requirement?
> **Part 5**: Traceability - Connecting requirements to verification
> **Part 6**: Tools and Pitfalls - Practical application
>
> By the end, you'll be able to write, analyze, and manage requirements for automotive systems professionally."

---

### **TRIGGER: The Requirements Challenge** (Slides 6-7, ~5 minutes)

#### Slide 6: A Deceptively Simple Task
**Visual:** Simple box with text "Design a cruise control system"
**Instructor Script:**
> "Let me give you a challenge. Your manager says:
>
> **'Design a cruise control system for our new vehicle.'**
>
> Sounds simple, right? Let me show you what happens when you skip requirements engineering.
>
> **Scenario 1 - Engineering student approach:**
> 'Okay, cruise control maintains constant speed. I'll write code that keeps throttle position constant.'
> **Result**: Vehicle slows down on hills, speeds up downhill. FAILED.
>
> **Scenario 2 - Better attempt:**
> 'Cruise control maintains speed using feedback control. I'll adjust throttle based on speed sensor.'
> **Result**: Works on flat roads. But what about:
> - Driver hits brake? (Should cruise disengage)
> - Steep downhill? (Should engine brake be used?)
> - Speed limit changes? (Should there be limits?)
> - Sudden obstacle? (How does it interact with collision avoidance?)
> - Clutch pressed? (Manual transmission considerations)
>
> **Suddenly, 'simple' cruise control has dozens of requirements across multiple systems.**"

#### Slide 7: What We're Really Building
**Visual:** System context diagram showing cruise control interfaces
**Instructor Script:**
> "Here's what a real automotive cruise control system must interface with:
>
> **Inputs:**
> - Driver controls (set, resume, cancel buttons)
> - Brake pedal position
> - Accelerator pedal position
> - Clutch position (manual transmission)
> - Wheel speed sensors
> - Engine RPM
> - Gear position
> - Collision detection system
> - Speed limit signs (if adaptive)
>
> **Outputs:**
> - Throttle actuator commands
> - Engine torque requests
> - Transmission shift requests
> - Driver displays (status indicators)
> - Diagnostic messages
>
> **This is why we need systematic requirements engineering.**
>
> Today, I'll show you how professionals handle this complexity."

---

### **RISING ACTION: Building the Requirements Framework** (Slides 8-24, ~52 minutes)

#### **Part 1: Stakeholder Identification and Analysis** (Slides 8-11, ~10 minutes)

##### Slide 8: Who Are the Stakeholders?
**Visual:** Network diagram showing stakeholder ecosystem
**Instructor Script:**
> "First principle: **A system serves stakeholders. We must know who they are and what they need.**
>
> For our cruise control system, who are the stakeholders?
>
> [Pause - let students think]
>
> Here's the complete list:
>
> **Primary Stakeholders:**
> - **Drivers**: Want convenient speed control, ease of use, safety
> - **Vehicle OEM**: Wants reliability, cost-effectiveness, regulatory compliance
> - **Safety engineers**: Want fail-safe operation, no unintended acceleration
>
> **Secondary Stakeholders:**
> - **Service technicians**: Want diagnosability, easy calibration
> - **Regulators**: Want compliance with FMVSS, ISO 26262 (functional safety)
> - **Other ECU teams**: Integration with powertrain, brakes, ADAS
> - **Testing team**: Want verifiable, testable requirements
> - **Marketing**: Want competitive features (adaptive cruise, traffic assist)
>
> **Tertiary Stakeholders:**
> - **Insurance companies**: Want proven safety record
> - **Fleet operators**: Want fuel efficiency data
> - **End-of-life recyclers**: Want material identification
>
> Notice: It's not just 'the customer.' Each group has DIFFERENT needs."

##### Slide 9: Stakeholder Analysis Matrix
**Visual:** Table showing stakeholder analysis framework
**Instructor Script:**
> "We analyze stakeholders systematically using this matrix:
>
> | Stakeholder | Interest | Influence | Priority | Engagement Strategy |
> |-------------|----------|-----------|----------|---------------------|
> | Driver | High | Medium | Critical | User studies, focus groups |
> | Safety Engineer | High | High | Critical | Requirements reviews, FMEA |
> | Regulator | Medium | High | High | Standards compliance verification |
> | Service Tech | Medium | Low | Medium | Service manual, diagnostics |
>
> **Interest**: How much does the system affect them?
> **Influence**: How much power do they have over the system?
> **Priority**: How important are they to success?
> **Engagement**: How do we gather their input?
>
> **Automotive example - Real case:**
> Tesla initially ignored service technician stakeholders when designing Model S battery packs. Result: Battery replacement required lifting entire vehicle, 6+ hour procedure. Later redesigned after technician feedback.
>
> **Lesson**: Identify ALL stakeholders early."

##### Slide 10: Eliciting Stakeholder Needs
**Visual:** Process diagram showing elicitation techniques
**Instructor Script:**
> "How do we extract what stakeholders actually need? Six proven techniques:
>
> **1. Interviews** (One-on-one or small groups)
> - Best for: Deep understanding, clarification
> - Example: Interview experienced drivers about cruise control usage patterns
>
> **2. Surveys** (Questionnaires)
> - Best for: Quantitative data from many stakeholders
> - Example: 'How often do you use cruise control?' (Daily/Weekly/Rarely/Never)
>
> **3. Observation** (Watch users in context)
> - Best for: Understanding actual behavior vs stated preferences
> - Example: Observe drivers on highway to see when they engage/disengage cruise
>
> **4. Workshops** (Facilitated group sessions)
> - Best for: Resolving conflicts, building consensus
> - Example: Joint session with powertrain, brakes, and safety teams to define interfaces
>
> **5. Prototyping** (Show early concepts)
> - Best for: Getting concrete feedback
> - Example: Simulator with cruise control to test driver reactions
>
> **6. Document Analysis** (Review existing systems, standards)
> - Best for: Baseline requirements, regulatory compliance
> - Example: Analyze FMVSS 126 (Electronic Stability Control) for related requirements
>
> **Best practice**: Use MULTIPLE techniques. Different stakeholders respond to different approaches."

##### Slide 11: From Stakeholder Needs to Requirements
**Visual:** Transformation diagram showing needs → requirements
**Instructor Script:**
> "Stakeholders express NEEDS in their language. We must transform these into REQUIREMENTS.
>
> **Example transformation:**
>
> **Driver need (in their words):**
> 'I want cruise control that doesn't freak out when I'm going downhill and makes me speed.'
>
> **Translation process:**
> - **Implied need**: System should not allow speed to exceed set speed significantly
> - **Technical requirement**: 'The cruise control system shall maintain vehicle speed within ±3 km/h of the set speed under grade conditions from -10% to +10%.'
>
> **Another example:**
>
> **Safety engineer need:**
> 'The system must be safe even if sensors fail.'
>
> **Requirements (multiple):**
> - REQ-CC-001: 'The system shall detect wheel speed sensor failures within 100ms.'
> - REQ-CC-002: 'Upon detection of sensor failure, the system shall transition to fail-safe state (cruise disabled) within 200ms.'
> - REQ-CC-003: 'The system shall alert the driver of cruise control unavailability via dashboard indicator.'
>
> **Key insight**: One stakeholder need often generates MULTIPLE technical requirements.
>
> This translation is the art and science of requirements engineering."

---

#### **Part 2: Needs vs Requirements - The Critical Distinction** (Slides 12-14, ~8 minutes)

##### Slide 12: Understanding the Difference
**Visual:** Two-column comparison table
**Instructor Script:**
> "This is foundational: **Needs and requirements are NOT the same thing.**
>
> **NEEDS:**
> - Stakeholder desires and goals
> - Expressed in stakeholder language
> - Often vague, subjective, negotiable
> - Answer: 'What problem are we solving?'
> - Example: 'I need a comfortable driving experience on long trips'
>
> **REQUIREMENTS:**
> - Specific, measurable system capabilities
> - Expressed in engineering language
> - Precise, objective, verifiable
> - Answer: 'What must the system do?'
> - Example: 'The cruise control system shall maintain speed with maximum throttle variation of ±5% when operating on grades ≤8%'
>
> **The V-Model connection** (from Session 2):
> - **Left side top**: Stakeholder NEEDS → System REQUIREMENTS
> - **Right side top**: Validation tests verify we met NEEDS
> - **Right side lower**: Verification tests verify we met REQUIREMENTS
>
> Needs define SUCCESS. Requirements define IMPLEMENTATION."

##### Slide 13: The Requirements Hierarchy
**Visual:** Pyramid showing requirement levels
**Instructor Script:**
> "Requirements exist at multiple levels. Understanding this hierarchy is critical:
>
> **Level 1 - Stakeholder Requirements (SR)**
> - High-level capabilities from stakeholder perspective
> - Example: 'SR-001: The vehicle shall provide driver-assisted speed control on highways'
>
> **Level 2 - System Requirements (SysR)**
> - System-level functional and performance requirements
> - Example: 'SysR-CC-015: The cruise control system shall maintain set speed within ±2 km/h in steady-state conditions'
>
> **Level 3 - Subsystem Requirements (SSR)**
> - Allocated to specific subsystems/components
> - Example: 'SSR-CC-ECU-042: The cruise control ECU shall read wheel speed sensor data at minimum 50 Hz'
>
> **Level 4 - Component Requirements (CR)**
> - Detailed design requirements for components
> - Example: 'CR-CC-SW-128: The speed calculation algorithm shall use floating-point arithmetic with minimum 32-bit precision'
>
> **Traceability flows DOWN** (allocation): SR → SysR → SSR → CR
> **Verification flows UP**: Component test → Subsystem test → System test → Validation
>
> This is the left side of the V-Model in practice."

##### Slide 14: Automotive Industry Standard - Requirements Layers
**Visual:** Automotive-specific requirement structure (per ISO 26262)
**Instructor Script:**
> "In automotive, we follow additional structure from ISO 26262 (Functional Safety):
>
> **Customer Requirements (Market)**
> ↓
> **Vehicle Level Requirements** (Vehicle attributes)
> ↓
> **System Requirements** (e.g., Cruise Control System)
> ↓
> **Hardware/Software Requirements** (ECU, sensors, actuators)
> ↓
> **Component Requirements** (Microcontroller, algorithms)
>
> **Real example - Adaptive Cruise Control (ACC):**
>
> - **Customer**: 'I want hands-free highway driving'
> - **Vehicle**: 'Vehicle shall provide Level 2 autonomous capability per SAE J3016'
> - **System**: 'ACC system shall maintain time gap of 1.0-2.5 seconds to lead vehicle'
> - **HW/SW**: 'Radar sensor shall detect vehicles up to 150m with ±0.5m range accuracy'
> - **Component**: 'Radar processing FPGA shall execute object tracking algorithm at 20 Hz'
>
> Each level adds specificity and enables different teams to work in parallel."

---

#### **Part 3: Types of Requirements** (Slides 15-18, ~12 minutes)

##### Slide 15: The Three Categories
**Visual:** Venn diagram showing requirement categories
**Instructor Script:**
> "All requirements fall into three categories. Master these and you'll capture complete system behavior.
>
> **1. Functional Requirements (FR)**
> - WHAT the system shall do
> - Describes behavior, inputs, outputs, operations
> - Example: 'The system shall activate cruise control when driver presses SET button'
>
> **2. Non-Functional Requirements (NFR)**
> - HOW WELL the system shall perform
> - Quality attributes, performance, reliability, usability
> - Example: 'The system shall respond to SET button within 200ms'
>
> **3. Constraints (CON)**
> - Design restrictions and boundaries
> - Technology, standards, regulations, interfaces
> - Example: 'The system shall comply with ISO 26262 ASIL-B requirements'
>
> **Common mistake**: Forgetting non-functional requirements. A system that does everything functionally but is too slow, unreliable, or unusable is still a failure.
>
> Let me show you detailed examples from automotive cruise control."

##### Slide 16: Functional Requirements Examples
**Visual:** Table with structured FR examples
**Instructor Script:**
> "**Functional Requirements** define system behavior. Here are real examples:
>
> **Basic Control Functions:**
> - FR-CC-001: 'The system shall engage cruise control when driver presses SET button while vehicle speed is between 30-180 km/h'
> - FR-CC-002: 'The system shall set target speed to current vehicle speed when SET button is pressed'
> - FR-CC-003: 'The system shall increase target speed by 1 km/h for each RES+ button press'
> - FR-CC-004: 'The system shall decrease target speed by 1 km/h for each SET- button press'
>
> **Deactivation Functions:**
> - FR-CC-010: 'The system shall disengage cruise control when driver presses CANCEL button'
> - FR-CC-011: 'The system shall disengage cruise control when brake pedal is depressed >10%'
> - FR-CC-012: 'The system shall disengage cruise control when clutch pedal is depressed (manual transmission)'
>
> **Speed Maintenance:**
> - FR-CC-020: 'The system shall modulate throttle position to maintain target speed'
> - FR-CC-021: 'The system shall request engine torque reduction when speed exceeds target by >5 km/h on descents'
>
> **Notice the structure**: Each requirement specifies a clear input condition and system response. No ambiguity."

##### Slide 17: Non-Functional Requirements Examples
**Visual:** Quality attribute categories with examples
**Instructor Script:**
> "**Non-Functional Requirements** define quality attributes. These are often forgotten but equally critical.
>
> **Performance:**
> - NFR-CC-001: 'The system shall achieve steady-state speed accuracy within ±2 km/h within 5 seconds of engagement'
> - NFR-CC-002: 'The control loop shall execute at minimum 20 Hz update rate'
>
> **Reliability:**
> - NFR-CC-010: 'The system shall achieve ASIL-B rating per ISO 26262'
> - NFR-CC-011: 'The system shall have failure rate <10 FIT (Failures In Time per billion hours)'
>
> **Usability:**
> - NFR-CC-020: 'Driver shall be able to engage cruise control with single button press (no menu navigation)'
> - NFR-CC-021: 'System status shall be visible on instrument cluster within driver's primary field of view'
>
> **Maintainability:**
> - NFR-CC-030: 'The system shall log fault codes per SAE J1979 OBD-II standard'
> - NFR-CC-031: 'Calibration parameters shall be modifiable via diagnostic tool without ECU replacement'
>
> **Safety:**
> - NFR-CC-040: 'The system shall transition to safe state within 200ms upon detection of critical sensor failure'
>
> **Environmental:**
> - NFR-CC-050: 'The ECU shall operate in temperature range -40°C to +85°C'
>
> These are often harder to specify but critical to user satisfaction and system success."

##### Slide 18: Constraints Examples
**Visual:** Constraint categories
**Instructor Script:**
> "**Constraints** limit design freedom. They come from regulations, standards, existing architecture, and business decisions.
>
> **Regulatory Constraints:**
> - CON-CC-001: 'The system shall comply with FMVSS 126 (Electronic Stability Control)'
> - CON-CC-002: 'The system shall meet Euro NCAP 5-star safety assessment requirements'
>
> **Standards Constraints:**
> - CON-CC-010: 'The system shall implement ISO 26262 safety life cycle processes'
> - CON-CC-011: 'Communication shall use CAN 2.0B protocol per ISO 11898'
>
> **Interface Constraints:**
> - CON-CC-020: 'The system shall interface with existing vehicle CAN bus (500 kbps)'
> - CON-CC-021: 'The system shall use existing steering wheel switch inputs (resistive ladder, 0-5V)'
>
> **Technology Constraints:**
> - CON-CC-030: 'The ECU shall use existing platform microcontroller (Infineon AURIX TC39x)'
> - CON-CC-031: 'Software shall be written in MISRA C:2012 compliant code'
>
> **Business Constraints:**
> - CON-CC-040: 'ECU unit cost shall not exceed $45 at 100k volume'
> - CON-CC-041: 'Development shall reuse existing powertrain control algorithms (≥70% reuse)'
>
> **Constraints often drive architecture decisions.** You design AROUND constraints; you design TO requirements."

---

#### **Part 4: Requirements Attributes - What Makes a Good Requirement?** (Slides 19-21, ~10 minutes)

##### Slide 19: The Quality Framework
**Visual:** Checklist of requirement attributes
**Instructor Script:**
> "A requirement can be technically correct but still be useless. Why? Because it lacks critical quality attributes.
>
> A GOOD requirement is:
>
> 1. **Clear** - Unambiguous, single interpretation
> 2. **Concise** - Succinct, no unnecessary words
> 3. **Verifiable** - Can be tested/proven
> 4. **Feasible** - Technically and economically achievable
> 5. **Traceable** - Linked to source (needs) and destination (tests)
> 6. **Necessary** - Actually needed (not nice-to-have masquerading as requirement)
> 7. **Complete** - Includes all needed information
> 8. **Consistent** - Doesn't contradict other requirements
> 9. **Unambiguous** - Only ONE possible interpretation
>
> Let me show you good vs bad examples for each attribute."

##### Slide 20: Good vs Bad Requirements Examples
**Visual:** Side-by-side comparison table
**Instructor Script:**
> "Let's analyze requirements through these quality attributes:
>
> **BAD: Ambiguous**
> ❌ 'The cruise control system shall be fast'
> - What is 'fast'? Response time? Processing speed? Acceleration?
>
> **GOOD: Clear and Verifiable**
> ✓ 'The cruise control system shall engage within 500ms of SET button press'
> - Specific metric, testable, no ambiguity
>
> ---
>
> **BAD: Not Verifiable**
> ❌ 'The system shall be user-friendly'
> - How do you test 'user-friendly'? Subjective.
>
> **GOOD: Verifiable**
> ✓ 'The system shall enable driver to set target speed with maximum 3 button presses'
> - Countable actions, testable, objective
>
> ---
>
> **BAD: Contains Design (Should Be Requirement)**
> ❌ 'The system shall use PID controller with Kp=0.5, Ki=0.1, Kd=0.05 to maintain speed'
> - This is design solution, not requirement
>
> **GOOD: Design-Free**
> ✓ 'The system shall maintain speed within ±2 km/h with settling time ≤5 seconds'
> - Specifies WHAT, not HOW. Allows engineers to choose best controller.
>
> ---
>
> **BAD: Incomplete**
> ❌ 'The system shall disengage when driver brakes'
> - Missing: How much brake pressure? What's the timing?
>
> **GOOD: Complete**
> ✓ 'The system shall disengage cruise control within 100ms when brake pedal is depressed >10% of travel'
> - Includes threshold and timing
>
> ---
>
> **BAD: Multiple Requirements**
> ❌ 'The system shall maintain speed and disengage on brake press and display status'
> - Three requirements in one (violates 'atomic' principle)
>
> **GOOD: Atomic (Single Requirement)**
> ✓ Split into three:
> - 'The system shall maintain target speed within ±2 km/h'
> - 'The system shall disengage when brake pedal is depressed >10%'
> - 'The system shall display engagement status on instrument cluster'
>
> Each can be verified independently."

##### Slide 21: Requirements Writing Best Practices
**Visual:** Template and guidelines
**Instructor Script:**
> "Professional requirements follow standard structure. Here's the template:
>
> **Standard Structure:**
> '[System] shall [action] [object] [qualifier] [condition]'
>
> **Examples:**
> - 'The cruise control system shall maintain vehicle speed within ±2 km/h when operating on grades ≤8%'
>   - System: cruise control system
>   - Action: maintain
>   - Object: vehicle speed
>   - Qualifier: within ±2 km/h
>   - Condition: when operating on grades ≤8%
>
> **Key writing rules:**
>
> 1. **Use 'shall' for requirements**
>    - 'shall' = mandatory requirement
>    - 'should' = guidance/goal (not a requirement)
>    - 'will' = statement of fact
>    - 'may' = permission/option
>
> 2. **Avoid weak words**: 'adequate', 'sufficient', 'good', 'user-friendly', 'fast', 'reliable'
>    - Replace with specific, measurable criteria
>
> 3. **Be specific about conditions**: Don't say 'when appropriate' or 'as needed'
>    - Specify exact conditions: 'when vehicle speed exceeds 30 km/h'
>
> 4. **Quantify everything possible**:
>    - Not: 'quickly' → 'within 500ms'
>    - Not: 'accurately' → 'with ±2% error'
>    - Not: 'most of the time' → '99.9% of operational time'
>
> 5. **One requirement per statement** (atomic)
>    - If you can split it with 'and', it's probably multiple requirements
>
> **Automotive standard reference**: Many companies use IEEE 29148 (Requirements Engineering) or EARS (Easy Approach to Requirements Syntax)."

---

#### **Part 5: Requirements Traceability** (Slides 22-23, ~8 minutes)

##### Slide 22: Why Traceability Matters
**Visual:** Traceability chain diagram
**Instructor Script:**
> "Traceability is the ability to follow a requirement through the entire life cycle.
>
> **Why it's critical:**
>
> 1. **Impact Analysis**: If a stakeholder need changes, what requirements are affected? What components? What tests?
>
> 2. **Verification Coverage**: Are all requirements tested? Are there orphan tests (tests with no requirement)?
>
> 3. **Regulatory Compliance**: ISO 26262, ASPICE, DO-178C all REQUIRE traceability
>
> 4. **Change Management**: Understanding ripple effects of changes
>
> 5. **Project Visibility**: What's implemented? What's tested? What's validated?
>
> **Traceability links:**
>
> **Forward traceability** (downstream):
> Stakeholder Need → System Requirement → Subsystem Requirement → Design Element → Code Module → Test Case
>
> **Backward traceability** (upstream):
> Test Result → Test Case → Requirement → Stakeholder Need
>
> **Bi-directional traceability**: Ability to navigate both directions
>
> Let me show you how we implement this."

##### Slide 23: Requirements Traceability Matrix (RTM)
**Visual:** Example RTM spreadsheet
**Instructor Script:**
> "The primary tool is the **Requirements Traceability Matrix (RTM)**.
>
> **Example RTM for Cruise Control:**
>
> | Stakeholder Need | System Req | Subsystem Req | Design | Implementation | Test Case | Status |
> |------------------|------------|---------------|--------|----------------|-----------|--------|
> | SN-001: Driver wants hands-free highway speed control | SR-CC-001 | SSR-CC-ECU-010, SSR-CC-SW-005 | DD-CC-SpeedControl | SW-Module-CC-001 | TC-CC-045 | Verified |
> | SN-002: System must be safe even with sensor failures | SR-CC-020 | SSR-CC-ECU-025, SSR-CC-Diag-003 | DD-CC-FailSafe | SW-Module-CC-FailSafe | TC-CC-078, TC-CC-079 | Verified |
>
> **What this shows:**
> - Every stakeholder need maps to one or more system requirements
> - System requirements decompose to subsystem requirements
> - Design elements implement requirements
> - Test cases verify requirements
> - Status tracking: Not Started / In Progress / Implemented / Verified / Validated
>
> **Red flags the RTM catches:**
> - **Orphan requirements**: Requirement with no test case (Can't verify!)
> - **Orphan tests**: Test with no requirement (Testing what?)
> - **Uncovered needs**: Stakeholder need with no requirements (Gap!)
> - **Unimplemented requirements**: Requirement with no design element (Missed!)
>
> **Tool support**: IBM DOORS, Jama, PTC Integrity, Siemens Polarion, or even Excel for small projects.
>
> **Automotive reality**: On a complete vehicle program, RTMs have 10,000+ rows. Tool support is essential."

---

#### **Part 6: Requirements Management Tools and Processes** (Slides 24, ~4 minutes)

##### Slide 24: Requirements Management Tools Landscape
**Visual:** Tool comparison matrix
**Instructor Script:**
> "How do we manage thousands of requirements? We need tools.
>
> **Industry-Standard Tools:**
>
> **1. IBM DOORS (Dynamic Object-Oriented Requirements System)**
> - Most widely used in aerospace/automotive
> - Powerful traceability, change tracking, baseline management
> - Steep learning curve, expensive
> - Used by: GM, Ford, Boeing, Airbus
>
> **2. Jama Connect**
> - Modern web-based interface
> - Good collaboration features
> - Integration with JIRA, testing tools
> - Used by: Tesla, NASA, medical device companies
>
> **3. PTC Integrity (formerly MKS)**
> - Integrated ALM (Application Lifecycle Management)
> - Strong in automotive (ASPICE compliance)
> - Used by: Continental, Bosch
>
> **4. Siemens Polarion**
> - Modern, integrated platform
> - Good for Agile + requirements
> - MBSE integration
>
> **5. Atlassian Jira (with plugins)**
> - Lightweight option
> - Good for software-heavy projects
> - Limited traceability compared to dedicated tools
>
> **6. Excel/Google Sheets**
> - Don't laugh - still used for small projects
> - Benefits: Everyone knows it, no licensing cost
> - Drawbacks: No automation, error-prone, doesn't scale
>
> **MBSE Tools** (from Session 3):
> - Cameo Systems Modeler (SysML)
> - Enterprise Architect
> - Embedded requirements directly in models
>
> **Key capabilities to look for:**
> - Traceability automation
> - Change impact analysis
> - Baseline and version management
> - Review and approval workflows
> - Integration with testing tools
> - Reporting and metrics
> - Import/export (Excel, ReqIF)
>
> **Automotive standard**: ReqIF (Requirements Interchange Format) - ISO standard for exchanging requirements between tools."

---

### **CLIMAX: Requirements Engineering Pitfalls** (Slides 25-27, ~12 minutes)

#### Slide 25: The Seven Deadly Sins of Requirements
**Visual:** Warning signs with examples
**Instructor Script:**
> "Let me show you the most common requirements engineering failures. Learn to recognize these anti-patterns.
>
> **Sin #1: Ambiguity**
> ❌ Example: 'The system shall provide adequate performance'
> - What's 'adequate'? Different stakeholders have different interpretations
> - **Fix**: 'The system shall accelerate from 50-100 km/h in ≤8 seconds'
>
> **Sin #2: Gold Plating (Unnecessary Features)**
> ❌ Example: 'The cruise control shall display average fuel economy'
> - Nice feature, but is it NEEDED for cruise control? (Instrument cluster does this)
> - **Impact**: Adds cost, complexity, testing burden
> - **Fix**: Challenge every requirement - trace to stakeholder need
>
> **Sin #3: Scope Creep**
> - Requirements continuously added without formal change process
> - **Example**: Mid-development: 'Oh, let's also add traffic sign recognition'
> - **Impact**: Schedule delays, budget overruns, quality issues
> - **Fix**: Formal change control board, impact analysis before accepting changes
>
> **Sin #4: Implementation Bias**
> ❌ Example: 'The system shall use a Kalman filter to estimate vehicle speed'
> - This specifies HOW (Kalman filter) not WHAT (accurate speed estimation)
> - **Fix**: 'The system shall estimate vehicle speed with ±1 km/h accuracy'
> - Let designers choose the best algorithm (might be Kalman, might not)
>
> **Sin #5: Missing Non-Functionals**
> - Specifying all functional behavior but forgetting performance, safety, reliability
> - **Example**: Having 100 functional requirements but zero reliability requirements
> - **Impact**: System works but is unusable (too slow, unreliable, unsafe)
> - **Fix**: Systematically review NFR categories (performance, reliability, safety, usability, maintainability, security)
>
> **Sin #6: Inconsistency**
> ❌ Example:
> - REQ-001: 'System shall operate in -20°C to +70°C'
> - REQ-045: 'Display shall use LCD screen' (LCDs typically fail below -10°C)
> - **Fix**: Requirements review, consistency checking (tools help)
>
> **Sin #7: Weak Traceability**
> - Can't answer: 'Which test verifies REQ-CC-042?'
> - Can't answer: 'If we change this need, what's impacted?'
> - **Impact**: Requirements not verified, changes cause unintended consequences
> - **Fix**: Maintain RTM religiously, use tools
>
> Every project I've seen fail had at least 3 of these sins."

#### Slide 26: Real Automotive Example - Unintended Acceleration
**Visual:** Toyota case study analysis
**Instructor Script:**
> "Let's apply what we've learned to a real disaster: Toyota unintended acceleration (2009-2011).
>
> **Background**:
> - 89 deaths, millions of vehicles recalled
> - $1.2B settlement
> - Root cause: Software failures in Electronic Throttle Control System (ETCS)
>
> **Requirements Engineering Failures:**
>
> **1. Incomplete Safety Requirements**
> - Missing requirement: 'System shall prevent simultaneous conflicting commands (accelerator + brake)'
> - Missing requirement: 'System shall default to brake priority in conflict scenarios'
>
> **2. Inadequate Failure Mode Requirements**
> - Didn't specify behavior for all sensor failure combinations
> - Didn't require testing of bit-flip errors in memory
>
> **3. Poor Traceability**
> - NASA analysis found: Many safety requirements were NOT traced to test cases
> - Orphan code: Functions that weren't tied to any requirement
>
> **4. Ambiguous Requirements**
> - Example found in investigation: 'Throttle shall respond appropriately to pedal input'
> - What's 'appropriately'? Different interpretations led to unsafe behavior
>
> **5. Missing Non-Functional Requirements**
> - No requirement for maximum task blocking time in RTOS
> - No requirement for stack overflow detection
> - Result: Software tasks could block critical safety functions
>
> **What proper requirements engineering would have prevented:**
>
> **Functional Requirements (missing):**
> - FR-ETCS-SAFE-001: 'If brake pedal is depressed >20% while accelerator is >50%, system shall reduce throttle to idle within 100ms'
>
> **Non-Functional Requirements (missing):**
> - NFR-ETCS-SAFE-010: 'Maximum task blocking time shall not exceed 10ms'
> - NFR-ETCS-SAFE-011: 'System shall detect and respond to stack overflow within one task cycle'
>
> **Constraints (missing):**
> - CON-ETCS-SAFE-020: 'Software shall comply with MISRA C safety guidelines'
>
> **Lessons learned:**
> - Safety requirements need extra rigor
> - Traceability to tests is non-negotiable
> - Non-functional requirements are NOT optional
> - External review of requirements catches gaps
>
> This cost 89 lives and $1.2B. Requirements engineering is not bureaucracy - it's life-saving discipline."

#### Slide 27: Best Practices Summary
**Visual:** Checklist infographic
**Instructor Script:**
> "Let me give you the professional's checklist for requirements engineering excellence:
>
> **During Requirements Development:**
>
> ✓ **Identify ALL stakeholders** (use stakeholder analysis matrix)
> ✓ **Use multiple elicitation techniques** (interviews, observation, workshops, prototypes)
> ✓ **Distinguish needs from requirements** (needs = why, requirements = what)
> ✓ **Categorize systematically** (functional, non-functional, constraints)
> ✓ **Write using standard structure** ('system shall...' with quantification)
> ✓ **Avoid design in requirements** (specify what, not how)
> ✓ **Make every requirement verifiable** (how will you test this?)
> ✓ **Include non-functional requirements** (don't forget quality attributes!)
>
> **During Requirements Management:**
>
> ✓ **Assign unique identifiers** (REQ-CC-001, REQ-CC-002, etc.)
> ✓ **Maintain traceability** (needs → requirements → design → test)
> ✓ **Use tools** (DOORS, Jama, Polarion - don't rely on email and Word)
> ✓ **Baseline requirements** (version control, change management)
> ✓ **Conduct reviews** (peer review, stakeholder review, safety review)
> ✓ **Track status** (proposed → approved → implemented → verified → validated)
> ✓ **Perform impact analysis** (before accepting changes)
> ✓ **Measure metrics** (requirements volatility, test coverage, defect density)
>
> **Quality Gates:**
>
> ✓ **Requirements Review Checklist**:
> - Are all stakeholders identified?
> - Is every requirement clear, verifiable, and traceable?
> - Are non-functionals included?
> - Are there conflicts or inconsistencies?
> - Is every requirement necessary (traced to a need)?
> - Can every requirement be tested?
>
> ✓ **Don't proceed to design until requirements are baselined and approved**
>
> **Automotive-specific:**
> ✓ Comply with ASPICE (Automotive SPICE) process framework
> ✓ Follow ISO 26262 requirements for safety-critical systems
> ✓ Use ReqIF for supplier/OEM requirements exchange"

---

### **RESOLUTION: Consolidation and Practice** (Slides 28-30, ~8 minutes + Q&A)

#### Slide 28: Key Takeaways
**Visual:** Summary with visual metaphors
**Instructor Script:**
> "Let's consolidate what you've learned today:
>
> **1. Stakeholder-Driven Process**
> - Systems serve stakeholders - identify them ALL
> - Elicit needs systematically (interviews, observation, workshops)
> - Transform needs into requirements
>
> **2. Needs ≠ Requirements**
> - Needs: Stakeholder desires (why)
> - Requirements: System capabilities (what)
> - Design: Implementation solution (how)
>
> **3. Three Requirement Types**
> - Functional: What system does
> - Non-functional: How well it performs
> - Constraints: Design limitations
>
> **4. Quality Attributes**
> - Clear, concise, verifiable, traceable, complete, consistent
> - Use 'shall' structure with quantification
> - Avoid ambiguity and design bias
>
> **5. Traceability is Essential**
> - Needs → Requirements → Design → Implementation → Tests
> - Use RTM and tools (DOORS, Jama, etc.)
> - Ensures nothing falls through cracks
>
> **6. Common Pitfalls to Avoid**
> - Ambiguity, gold plating, scope creep, implementation bias
> - Missing non-functionals, inconsistency, weak traceability
>
> **Remember**: Poor requirements are the #1 cause of project failure. Master this, and you're already ahead of most engineers."

#### Slide 29: Connection to V-Model and Next Sessions
**Visual:** V-Model with requirements highlighted
**Instructor Script:**
> "Let's place today's learning in the bigger systems engineering context.
>
> **Today (Session 4)**: We're at the TOP LEFT of the V-Model
> - Stakeholder needs and requirements definition
> - This is the FOUNDATION of everything else
>
> **What comes next:**
>
> **Session 5 - System Design and Architecture**:
> - How do we transform requirements into architecture?
> - How do we allocate requirements to subsystems?
> - How do we define interfaces?
> - Moving down the left side of the V
>
> **Session 7 - Operational and Functional Analysis**:
> - How do we analyze operational scenarios?
> - How do we allocate requirements to functions?
> - Functional flow block diagrams
>
> **Session 8 - Integration, Verification & Validation**:
> - Right side of the V-Model
> - How do we verify requirements? (Did we build it right?)
> - How do we validate against needs? (Did we build the right thing?)
> - Requirements traceability to tests
>
> **The thread:**
> - Session 4: Define requirements
> - Session 5: Architect the solution
> - Session 7: Analyze functions and operations
> - Session 8: Verify requirements are met
>
> **Key connection**: The requirements you write today MUST be verifiable in Session 8. Always write requirements with testing in mind.
>
> In Session 3, we learned MBSE. In MBSE tools (SysML), requirements are embedded directly in models, enabling automatic traceability and consistency checking. Same principles, different representation."

#### Slide 30: Practice Exercise & Q&A
**Visual:** Exercise description
**Instructor Script:**
> "**Practical Exercise (Due before Session 5):**
>
> You are the systems engineer for an **Automatic Emergency Braking (AEB)** system for a passenger vehicle.
>
> **Part 1: Stakeholder Analysis** (30%)
> - Identify at least 6 stakeholder groups
> - Create stakeholder analysis matrix (Interest, Influence, Priority, Engagement Strategy)
> - List 2-3 needs per stakeholder
>
> **Part 2: Requirements Development** (50%)
> Write at least 15 system-level requirements:
> - Minimum 8 functional requirements
> - Minimum 4 non-functional requirements (including performance, safety, usability)
> - Minimum 3 constraints (regulatory, interface, technology)
>
> Each requirement must:
> - Follow 'shall' structure
> - Be clear, verifiable, and complete
> - Include unique identifier (REQ-AEB-XXX)
> - Be traceable to a stakeholder need
>
> **Part 3: Traceability Matrix** (20%)
> - Create RTM mapping stakeholder needs → requirements
> - Identify at least one test approach for each requirement
>
> **Grading Criteria:**
> - Completeness of stakeholder identification
> - Quality of requirements (clear, verifiable, unambiguous)
> - Proper categorization (FR/NFR/CON)
> - Traceability
> - Professional formatting
>
> **Submission**: 1-page stakeholder analysis + 2-page requirements list + 1-page RTM (4 pages total)
>
> **Tips:**
> - Research real AEB systems (Euro NCAP requirements, SAE standards)
> - Think about failure modes and safety
> - Consider regulatory requirements (UN R152, FMVSS)
> - Don't specify implementation (no 'use radar' - instead specify detection requirements)
>
> **Discussion Questions:**
> - How would requirements differ for AEB in a passenger car vs a heavy truck?
> - What are the ethical requirements for AEB? (e.g., prioritizing pedestrians vs occupants)
> - How do you handle conflicting stakeholder needs?
>
> **30 minutes for your questions.**"

---

## 📊 PPT DESIGN GUIDANCE

### Visual Style:
- **Professional engineering aesthetic**: Clean, technical, data-driven
- **Color coding**:
  - Blue for Functional Requirements
  - Green for Non-Functional Requirements
  - Orange for Constraints
  - Red for anti-patterns and warnings
- **Use real automotive examples**: Photos of actual cruise control systems, driver interfaces
- **Diagrams**: Professional process flows, RTM tables, stakeholder networks

### Key Slides to Emphasize:
1. **Slide 3** (Why Requirements Engineering Is Critical) - Statistics that grab attention
2. **Slide 11** (Needs → Requirements transformation) - Core concept
3. **Slide 15** (Three requirement types) - Fundamental categorization
4. **Slide 20** (Good vs Bad requirements) - Practical examples students will reference
5. **Slide 23** (RTM) - Industry-standard tool
6. **Slide 26** (Toyota case study) - Real-world consequences
7. **Slide 28** (Summary) - Students will photograph this

### Animations:
- **Slide 7**: Animate system context diagram connections appearing one by one
- **Slide 11**: Animate transformation from need → requirement with visual flow
- **Slide 13**: Build requirements hierarchy pyramid from bottom to top
- **Slide 23**: Highlight RTM traceability links with animated arrows
- **Slide 26**: Timeline animation showing Toyota unintended acceleration investigation

### Tables and Templates:
- **Slide 9**: Stakeholder analysis matrix (use real cruise control example)
- **Slide 20**: Good vs bad requirements comparison table
- **Slide 23**: Full RTM example (6-8 rows minimum for clarity)
- **Slide 24**: Tool comparison matrix with features

### Real Examples to Include:
- Use actual automotive requirements from public sources (SAE standards, Euro NCAP, FMVSS)
- Screenshots of DOORS or Jama (if licensing permits, otherwise mockups)
- Real cruise control system diagrams from service manuals
- Actual requirements statements from ISO 26262 examples

---

## 🎯 INSTRUCTOR NOTES

### Pedagogical Strategy:
- **Start concrete (cruise control), expand abstract (principles), return concrete (exercise)**
- **Use real failure case (Toyota) to drive home consequences**
- **Emphasize practical skills**: Students should be able to write requirements after today
- **Industry-standard terminology**: Use same terms as INCOSE, IEEE, ISO
- **Tool exposure**: Show actual tools, not just theory

### Common Student Challenges:

**Challenge 1: "Why can't we just say 'make it work well'?"**
**How to address:** Show Slide 4 (Mars Climate Orbiter) - ambiguity costs $327M. Show Slide 20 - translate vague statement to verifiable requirement. Emphasize: If you can't test it, it's not a requirement.

**Challenge 2: "Non-functional requirements seem less important than functional"**
**How to address:** Use examples: A car that drives (functional) but catches fire (reliability NFR failure) is useless. A system that works but takes 5 minutes to respond (performance NFR failure) won't be used. NFRs define QUALITY.

**Challenge 3: "This seems like a lot of bureaucracy"**
**How to address:** Show Slide 3 statistics - 65% of projects fail due to requirements issues. Show Slide 26 - Toyota's $1.2B lesson. Ask: "Is traceability bureaucracy or insurance?" Frame requirements engineering as RISK REDUCTION.

**Challenge 4: "How do I know when I have enough requirements?"**
**How to address:** Coverage criteria:
- Every stakeholder need has ≥1 requirement
- Every operational scenario is covered
- All interfaces defined
- All failure modes addressed
- All regulatory requirements mapped
- Every requirement is verifiable
- Use reviews and checklists (Slide 27)

**Challenge 5: "What if stakeholders want contradictory things?"**
**How to address:** This is NORMAL. Systems engineering is about trade-offs. Example: Marketing wants 200 km/h top speed, Safety wants governor at 180 km/h. Solution: Negotiate, analyze risk, escalate to decision authority. Document rationale. This leads to Session 10 (Decision Management).

### Timing Flexibility:

**If running short:**
- Condense Slide 10 (elicitation techniques) - brief overview, details in reading
- Reduce Slide 24 (tools) to 2-3 tools only
- Move some good/bad examples from Slide 20 to backup slides

**If running long:**
- Extend Slide 26 (Toyota case) with more forensic details
- Add interactive exercise: Give students a vague requirement, have them improve it
- Show live demo of DOORS or Jama tool

**Core content (must cover - non-negotiable):**
- Slides 8-11 (stakeholders and needs)
- Slides 12-14 (needs vs requirements)
- Slides 15-18 (requirement types)
- Slides 19-21 (quality attributes and writing)
- Slides 22-23 (traceability and RTM)
- Slide 26 (Toyota case study)
- Slide 28 (summary)

### Engagement Points:

**Slide 6**: Interactive - pause after showing cruise control challenge. Ask: "What could go wrong if we don't specify requirements?" Let students call out scenarios.

**Slide 11**: Work through transformation together - show a raw stakeholder quote, have students help translate to requirement.

**Slide 20**: For each bad requirement, ask students: "What's wrong with this?" before revealing the answer.

**Slide 23**: Walk through RTM together - trace one requirement from need to test.

**Slide 26**: This should be a mini-case study discussion. Ask: "What specific requirement would have prevented this?"

### Interactive Elements:

**Quick Poll (Slide 3)**: "How many have worked on projects that failed due to unclear requirements?" (Show of hands - normalizes the problem)

**Pair Exercise (Slide 21)**: Give pairs 3 minutes to write one requirement for "vehicle shall have good fuel economy." Then critique together using quality attributes.

**Case Analysis (Slide 26)**: Small groups discuss: "If you were the requirements engineer, what would you have done differently?"

### Materials to Prepare:

**Before class:**
- [ ] Real RTM example (anonymized from industry project if possible)
- [ ] Screenshots or demo of DOORS/Jama
- [ ] Printed requirement quality checklist (1-page handout)
- [ ] Case study materials for Toyota unintended acceleration
- [ ] Exercise assignment handout with rubric

**Handouts:**
- [ ] Requirements writing template (Slide 21 format)
- [ ] Quality attributes checklist
- [ ] Stakeholder analysis matrix template
- [ ] RTM template (Excel)
- [ ] List of automotive standards (ISO 26262, ASPICE, FMVSS, Euro NCAP)

**Post-class:**
- [ ] Share slides
- [ ] Post exercise assignment with due date
- [ ] Post requirements writing template and examples
- [ ] Post links to IEEE 29148, INCOSE requirements guide
- [ ] Create discussion forum: "Share a bad requirement you've encountered and how to fix it"

### Assessment Opportunities:

**During lecture:**
- Quick quiz (Slide 14): "What's the difference between a need and a requirement?"
- Quick quiz (Slide 18): "Classify this requirement: FR, NFR, or CON?"

**Exercise assessment criteria:**
- Stakeholder completeness (Did they identify non-obvious stakeholders?)
- Requirement quality (Verifiable? Clear? Properly structured?)
- Traceability (Is RTM complete and consistent?)
- Professional formatting (Industry-standard presentation?)

**Common student mistakes to watch for:**
- Writing implementation as requirements
- Forgetting non-functional requirements
- Ambiguous language
- Missing traceability
- Copy-pasting requirements from internet without understanding

---

## ✅ Session Success Criteria

Students leave able to:
- ✓ Identify stakeholders systematically for automotive systems
- ✓ Distinguish between stakeholder needs and system requirements
- ✓ Categorize requirements as functional, non-functional, or constraints
- ✓ Write clear, verifiable, traceable requirements using standard structure
- ✓ Recognize good vs bad requirements using quality attributes
- ✓ Create and interpret requirements traceability matrices
- ✓ Identify common requirements engineering pitfalls
- ✓ Understand tool landscape for requirements management

**Critical outcome:** Students can **write professional-quality requirements** for an automotive system and understand that requirements engineering is a **systematic discipline** with proven methods, not ad-hoc documentation.

**Evidence of success:**
- Student can take a vague stakeholder statement and convert it to a verifiable requirement
- Student can critique a requirement using quality attributes framework
- Student understands traceability chain from need to test
- Student can explain why Toyota unintended acceleration was a requirements failure

---

## 📚 Additional Resources for Students

**Standards and Guidelines:**
- IEEE 29148-2018: Systems and Software Engineering - Life Cycle Processes - Requirements Engineering
- ISO/IEC/IEEE 15288:2015: Systems and Software Engineering - System Life Cycle Processes
- INCOSE Systems Engineering Handbook, Chapter 4: Requirements Analysis
- EARS (Easy Approach to Requirements Syntax) - Rolls-Royce method

**Automotive-Specific:**
- ISO 26262-8:2018: Road Vehicles - Functional Safety - Part 8: Supporting Processes (Requirements specification)
- Automotive SPICE (ASPICE) v3.1: SYS.3 System Requirements Analysis
- SAE J3061: Cybersecurity Guidebook for Cyber-Physical Vehicle Systems

**Books:**
- "Requirements Engineering Fundamentals" by Klaus Pohl & Chris Rupp
- "Writing Effective Use Cases" by Alistair Cockburn (for scenario-based requirements)
- "Software Requirements" by Karl Wiegers (applicable to systems too)

**Online Tools and Templates:**
- Jama Software: Free requirements training modules
- IBM DOORS tutorials (YouTube)
- ReqIF format specification (for tool interoperability)

---

## 🔗 Connections to Other Sessions

**Builds on:**
- **Session 1**: Failures often traced to requirements issues
- **Session 2**: Requirements definition is first technical process in ISO/IEC 15288
- **Session 3**: MBSE embeds requirements in models (SysML requirements diagrams)

**Leads to:**
- **Session 5**: How do we transform requirements into architecture and design?
- **Session 7**: How do we allocate requirements to functions using operational analysis?
- **Session 8**: How do we verify requirements? (Right side of V-Model - testing)
- **Session 9**: How do we manage requirements changes? (Change control, configuration management)
- **Session 12**: How do we specify safety requirements? (ISO 26262 safety requirements)

**Key concept thread:**
- **Session 2**: WHAT is systems engineering? (Framework)
- **Session 3**: HOW do we implement it? (Traditional vs MBSE)
- **Session 4**: HOW do we capture requirements? (This session)
- **Session 5**: HOW do we design solutions? (Architecture)
- **Session 8**: HOW do we verify we met requirements? (V&V)

**Requirements traceability appears in:**
- Session 8 (test traceability)
- Session 9 (configuration management)
- Session 12 (safety requirements traceability per ISO 26262)
- Session 15 (measurement and traceability metrics)

---

## 🎬 Opening and Closing Strategies

### **Opening (First 2 minutes):**
Start with the Mars Climate Orbiter image on screen as students enter. Begin:

> "Before we start, I want you to look at this image. This is a $327 million spacecraft that was destroyed because of a single missing word in a requirement. One. Word.
>
> Today, we're going to learn how to write requirements so precisely, so carefully, that this never happens on your projects. Because in automotive, instead of losing a spacecraft, we could lose lives.
>
> Welcome to Session 4: Requirements Engineering - the most critical skill in systems engineering."

### **Closing (Last 2 minutes):**
Return to the opening image:

> "We started with a $327 million failure caused by poor requirements. You now have the knowledge to prevent this:
>
> - You can identify stakeholders systematically
> - You can write clear, verifiable requirements
> - You can build traceability from needs to tests
> - You know the pitfalls and how to avoid them
>
> The exercise I've given you is your chance to practice these skills. Treat it seriously - imagine you're the requirements engineer and 89 lives depend on your work. Because someday, they might.
>
> See you in Session 5, where we'll transform these requirements into system architecture."

---

## 📈 Learning Objectives Mapping to Assessment

| Session Objective | Assessment Method | Success Criteria |
|-------------------|-------------------|------------------|
| Distinguish needs from requirements | Exercise Part 2 | Correctly categorizes stakeholder statements as needs; derives requirements from them |
| Identify and analyze stakeholders | Exercise Part 1 | Identifies ≥6 diverse stakeholder groups; complete analysis matrix |
| Classify requirement types | Exercise Part 2 | Correctly labels ≥8 FR, ≥4 NFR, ≥3 CON |
| Apply quality attributes | Exercise Part 2 | All requirements follow 'shall' structure, are verifiable, clear |
| Create traceability matrix | Exercise Part 3 | Complete RTM with needs→reqs→tests mappings |
| Recognize pitfalls | In-class discussion + exercise quality | Avoids ambiguity, design bias, missing NFRs |
| Select tools | Knowledge check (Q&A) | Can name 2-3 tools and their use cases |

---

**End of Session 4 Framework**
**Next:** Session 5 (System Design and Architecture)
