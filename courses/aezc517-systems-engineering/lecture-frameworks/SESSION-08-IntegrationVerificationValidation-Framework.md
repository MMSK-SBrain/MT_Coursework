# Session 8: System Integration, Verification & Validation
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 90 minutes lecture + 30 minutes Q&A
**Approach:** Process-Focused/Technical
**PPT Target:** 28-30 slides

---

## 🎯 Session Objectives (For Instructor)

By the end of this session, students will be able to:
- Distinguish between verification and validation
- Select appropriate integration strategies (big bang vs incremental)
- Develop comprehensive V&V plans aligned with requirements
- Apply the four verification methods: test, analysis, inspection, demonstration
- Design test strategies for different levels: unit, integration, system, acceptance
- Create test coverage matrices with traceability to requirements
- Recognize common V&V pitfalls and best practices

**Mapped Learning Outcomes:** LO2 (Develop requirements, architectures, specifications, verifications, and tests), LO4 (Apply systems engineering practices and methods in automotive systems)

**Note:** This is Session 8 - the final session before mid-semester exam. This session includes comprehensive review connections to Sessions 1-7.

---

## 📖 INSTRUCTOR-LED STORY ARC

### **SETUP: The Moment of Truth** (Slides 1-6, ~12 minutes)

#### Slide 1: Title
**Visual:** Title slide with V-Model diagram highlighting the right side (verification & validation)
**Instructor Script:**
> "Welcome to Session 8: System Integration, Verification & Validation. This is where the rubber meets the road in systems engineering.
>
> We've spent 7 sessions learning to define, design, and decompose systems. Today: How do we prove our system actually works?"

**PPT Content:**
```
SESSION 8: SYSTEM INTEGRATION, VERIFICATION & VALIDATION
Testing, Proving, and Delivering Systems That Work

Module 2: System Design and Analysis
Automotive Systems Engineering (AE ZG517 / AEL ZG517)
```

**Outcomes Addressed:** Setting context for LO2, LO4

---

#### Slide 2: Connection to Sessions 1-7 (Mid-Semester Review)
**Visual:** Journey map showing Sessions 1-7 leading to Session 8
**Instructor Script:**
> "Before we dive in, let's see how everything connects. This is your mid-semester integration point:
>
> **Session 1**: Learned WHY SE matters - failures like Apollo 13, Therac-25
> **Session 2**: Learned SE fundamentals - ISO/IEC 15288, V-Model, systems thinking
> **Session 3**: Traditional vs MBSE - modern approaches to complexity
> **Session 4**: Requirements Engineering - defining WHAT the system must do
> **Session 5**: Architecture & Design - HOW the system is structured
> **Session 6**: Case Study 1 - Boeing 737 MAX failure analysis
> **Session 7**: Functional Analysis - decomposing system behaviors
>
> **Session 8 (Today)**: Proving the system meets requirements - closing the V-Model
>
> Everything we've learned culminates in V&V. Without verification and validation, we have no proof our system works."

**PPT Content:**
```
THE SYSTEMS ENGINEERING JOURNEY SO FAR

Sessions 1-3: Foundation
  • Why SE matters (failures)
  • SE processes & frameworks
  • MBSE evolution

Sessions 4-5: Requirements & Design
  • Requirements engineering
  • System architecture

Sessions 6-7: Analysis & Case Study
  • Real-world failure analysis
  • Functional decomposition

Session 8: Proving It Works ← TODAY
  • Integration, verification, validation
```

---

#### Slide 3: The V-Model Right Side
**Visual:** V-Model with left side (decomposition) grayed out, right side (integration/V&V) highlighted
**Instructor Script:**
> "Remember the V-Model from Session 2? We've been working down the left side:
>
> - Requirements → High-level design
> - Architecture → Detailed design
> - Functions → Implementation
>
> **Today we climb back up the right side:**
>
> - Unit testing → Integration testing
> - System testing → Acceptance testing
>
> **Key insight**: Each level on the left has a corresponding verification level on the right.
>
> Requirements defined in Session 4? Validated in acceptance testing.
> Architecture designed in Session 5? Verified in integration testing.
> Functions from Session 7? Tested in unit and integration tests.
>
> **This is called bidirectional traceability.**"

**PPT Content:**
```
THE V-MODEL: CLIMBING BACK UP

Left Side (Done):          Right Side (Today):
  Requirements    ←————→    Acceptance Testing
  Architecture    ←————→    System Testing
  Design          ←————→    Integration Testing
  Implementation  ←————→    Unit Testing

Each decomposition step has a corresponding verification step
```

---

#### Slide 4: Why Integration and V&V Matter - Real Costs
**Visual:** Statistics on V&V failures and costs
**Instructor Script:**
> "Let me show you why today's topic is critical:
>
> **Industry data on V&V:**
> - 40-50% of project budgets go to testing and V&V
> - 70% of defects found in testing were preventable with better V&V planning
> - Cost multiplier: 1x (requirements) → 10x (design) → 100x (testing) → 1000x (field)
>
> **Automotive examples:**
> - Toyota unintended acceleration (Session 6 case): Inadequate testing of ETCS
> - Takata airbag recall: $10 billion, inadequate validation of propellant aging
> - Tesla Autopilot incidents: Insufficient scenario coverage in validation
>
> **The paradox**: V&V is expensive, but NOT doing it properly is catastrophically more expensive."

**PPT Content:**
```
WHY V&V MATTERS: THE COST OF FAILURE

Industry Statistics:
  • 40-50% of project budget goes to V&V
  • Defect cost multiplier: 1x → 10x → 100x → 1000x
  • 70% of defects preventable with better V&V planning

Automotive Recalls (V&V Failures):
  • Takata airbags: $10B, 100M vehicles
  • GM ignition switch: $4.1B, 124 deaths
  • Toyota ETCS: $1.2B, inadequate software testing

**V&V is expensive. Not doing it is catastrophic.**
```

---

#### Slide 5: The Three Critical Questions
**Visual:** Three question marks with automotive system (AEB) in center
**Instructor Script:**
> "Every V&V strategy must answer three fundamental questions:
>
> **Question 1: Did we build the system right?** (VERIFICATION)
> - Does the system meet its specifications?
> - Are all requirements implemented correctly?
> - Does the design match the architecture?
>
> **Question 2: Did we build the right system?** (VALIDATION)
> - Does the system solve the customer's problem?
> - Does it meet stakeholder needs?
> - Will it work in the real operational environment?
>
> **Question 3: How do we know?** (EVIDENCE)
> - What tests prove it?
> - What analysis supports it?
> - What documentation demonstrates it?
>
> **Example: Adaptive Cruise Control (ACC)**
> - Verification: Does ACC maintain the specified 2-second gap? (Specification)
> - Validation: Does ACC make drivers feel safe and comfortable? (Need)
> - Evidence: Test reports, data logs, customer feedback
>
> These questions guide everything we do today."

**PPT Content:**
```
THREE CRITICAL V&V QUESTIONS

1. Did we build the system RIGHT? → VERIFICATION
   • Meets specifications
   • Requirements implemented correctly
   • Conforms to design

2. Did we build the RIGHT system? → VALIDATION
   • Solves customer problem
   • Meets stakeholder needs
   • Works in real environment

3. How do we KNOW? → EVIDENCE
   • Test results
   • Analysis data
   • Documentation

**All three must be answered with traceable evidence**
```

---

#### Slide 6: Learning Journey for Today
**Visual:** Roadmap with 6 key areas
**Instructor Script:**
> "Today's journey covers six critical areas:
>
> **Part 1**: Verification vs Validation - The critical distinction
> **Part 2**: Integration Strategies - Big bang vs incremental approaches
> **Part 3**: Verification Methods - Test, analysis, inspection, demonstration
> **Part 4**: Testing Levels - Unit, integration, system, acceptance
> **Part 5**: V&V Planning - Test strategies and coverage
> **Part 6**: Traceability - Connecting tests to requirements
>
> By the end, you'll be able to plan and execute comprehensive V&V for automotive systems."

**PPT Content:**
```
TODAY'S V&V ROADMAP

Part 1: Verification vs Validation (The Distinction)
Part 2: Integration Strategies (How to Build)
Part 3: Verification Methods (How to Prove)
Part 4: Testing Levels (Where to Test)
Part 5: V&V Planning (Test Strategy)
Part 6: Traceability (Evidence Management)

**Outcome: Complete V&V competency for automotive SE**
```

---

### **TRIGGER: The Integration Challenge** (Slides 7-8, ~8 minutes)

#### Slide 7: The Lane Keep Assist Integration Problem
**Visual:** LKA system block diagram with 8 components
**Instructor Script:**
> "Let's start with a real challenge. You're the integration lead for a Lane Keep Assist (LKA) system with these components:
>
> **8 Components to integrate:**
> 1. Forward camera (lane detection)
> 2. Image processing ECU
> 3. Lane detection algorithm
> 4. Control ECU
> 5. Steering torque actuator
> 6. Vehicle CAN bus
> 7. HMI warning system
> 8. Driver monitoring system
>
> **The challenge**: How do you integrate these? What's your strategy?
>
> **Two extreme approaches:**
>
> **Approach A - 'Big Bang'**: Get all 8 components, connect them all at once, power on, hope it works
>
> **Approach B - 'Incremental'**: Integrate components step-by-step, testing each integration point
>
> Which would you choose? Why?
>
> **Think about what could go wrong with each approach.**"

**PPT Content:**
```
INTEGRATION CHALLENGE: LANE KEEP ASSIST (LKA)

System Components (8):
  1. Forward camera
  2. Image processing ECU
  3. Lane detection algorithm
  4. Control ECU
  5. Steering actuator
  6. CAN bus interface
  7. HMI warning display
  8. Driver monitoring

Question: How do you integrate 8 components with 12+ interfaces?

Option A: Big Bang (all at once)
Option B: Incremental (step-by-step)

**What are the risks and benefits of each?**
```

---

#### Slide 8: What Usually Happens (The Failure Mode)
**Visual:** Timeline showing "big bang" integration disaster
**Instructor Script:**
> "Here's what typically happens with big bang integration:
>
> **Week 1**: Assemble all components, power on system
> **Result**: Doesn't work. Multiple failures.
>
> **Week 2**: Debug. Is it the camera? The ECU? The algorithm? The CAN bus? All of the above?
>
> **Problem**: With 8 components and 12 interfaces, you have:
> - 8 × 7 / 2 = 28 possible pairwise interactions
> - Hundreds of possible fault combinations
> - No idea where to start debugging
>
> **Real example - Tesla Autopilot early integration:**
> - 2015: Integrated camera, radar, ultrasonic, GPS all at once
> - Result: Sensor conflicts, phantom braking, weeks of debugging
> - Lesson: Switched to incremental integration with Hardware-in-the-Loop (HIL) testing
>
> **This is why integration strategy matters.**
>
> We need a systematic approach. That's what we'll learn today."

**PPT Content:**
```
BIG BANG INTEGRATION: WHAT GOES WRONG

Timeline:
  Week 1: Integrate all components → System fails
  Week 2: Debug → Can't isolate root cause
  Week 3: Still debugging → Multiple interacting faults
  Week 4: Project delay

With 8 components:
  • 28 pairwise interactions
  • 100+ fault combinations
  • Impossible to isolate failures

**Real Example: Early Tesla Autopilot**
  Integrated all sensors at once → sensor conflicts
  Switched to incremental + HIL testing

**Lesson: Integration strategy is critical**
```

---

### **RISING ACTION Part 1: Verification vs Validation - The Critical Distinction** (Slides 9-11, ~10 minutes)

#### Slide 9: Defining Verification and Validation
**Visual:** Split screen with verification (blueprint vs house) and validation (house vs family needs)
**Instructor Script:**
> "Let's nail down the most important distinction in V&V:
>
> **VERIFICATION**: 'Are we building the product right?'
> - Confirms product meets specifications
> - Objective, measurable criteria
> - Based on requirements and design documents
> - Question: Does it match what we specified?
>
> **VALIDATION**: 'Are we building the right product?'
> - Confirms product meets user needs
> - Subjective, user-centered evaluation
> - Based on stakeholder expectations and operational environment
> - Question: Does it solve the real problem?
>
> **House analogy:**
> - Verification: Does the house match the blueprint? (measurements, materials, code compliance)
> - Validation: Does the house meet the family's needs? (comfortable, functional, suitable)
>
> **You can have perfect verification and still fail validation.**
>
> Example: A house built exactly to spec (verified) but family hates the layout (not validated)."

**PPT Content:**
```
VERIFICATION vs VALIDATION: THE DISTINCTION

VERIFICATION: "Building the product RIGHT"
  • Meets specifications
  • Objective criteria
  • Based on requirements
  • Question: Does it match specs?

VALIDATION: "Building the RIGHT product"
  • Meets user needs
  • Subjective evaluation
  • Based on stakeholder expectations
  • Question: Does it solve the problem?

**House Analogy:**
  Verification → Matches blueprint?
  Validation → Family happy with it?

**You can verify perfectly but still fail to validate**
```

---

#### Slide 10: Automotive Example - Verification vs Validation
**Visual:** Automatic Emergency Braking (AEB) system with verification and validation scenarios
**Instructor Script:**
> "Let's make this concrete with Automatic Emergency Braking (AEB):
>
> **VERIFICATION Activities:**
> - Test: AEB activates when closing speed > 40 km/h and TTC < 1.5s (requirement AEB-FR-012)
> - Test: Braking deceleration = 6 m/s² ± 0.5 m/s² (requirement AEB-FR-018)
> - Inspection: CAN message ID 0x234 transmitted every 10ms (requirement AEB-IF-003)
> - Analysis: Brake response time < 150ms (requirement AEB-NFR-001)
>
> **These verify the system meets its specifications.**
>
> **VALIDATION Activities:**
> - Real-world testing: Does AEB prevent crashes in actual traffic?
> - User studies: Do drivers trust and accept AEB interventions?
> - Scenario testing: Works in rain, fog, night conditions?
> - Field trials: Reduces rear-end collisions in fleet data?
>
> **These validate the system solves the safety problem.**
>
> **Key insight**: You can perfectly verify AEB (all specs met) but if drivers disable it because they don't trust it, you've failed validation.
>
> **Both are required for success.**"

**PPT Content:**
```
AUTOMOTIVE EXAMPLE: AEB VERIFICATION vs VALIDATION

VERIFICATION (Meets Specs):
  ✓ Activation threshold: TTC < 1.5s, speed > 40 km/h
  ✓ Brake deceleration: 6 m/s² ± 0.5 m/s²
  ✓ CAN timing: 10ms message period
  ✓ Response time: < 150ms

VALIDATION (Meets Needs):
  ✓ Prevents crashes in real traffic?
  ✓ Drivers trust interventions?
  ✓ Works in rain/fog/night?
  ✓ Reduces fleet collision rates?

**Success = Verification AND Validation**

**Failure mode:** Perfect specs, but users disable feature
```

---

#### Slide 11: When to Verify vs Validate
**Visual:** Timeline showing verification (continuous) vs validation (gates)
**Instructor Script:**
> "**When do we do verification vs validation?**
>
> **VERIFICATION**: Throughout development
> - Requirements phase: Verify requirements are complete, consistent
> - Design phase: Verify design implements requirements
> - Implementation: Verify code implements design
> - Integration: Verify interfaces work correctly
> - System test: Verify all requirements met
>
> **Continuous activity at every stage.**
>
> **VALIDATION**: At key milestones
> - Concept validation: Does concept meet needs? (Before detailed design)
> - Design validation: Will design solve problem? (Before implementation)
> - System validation: Does system work in real environment? (Before production)
> - Operational validation: Meets needs in service? (After deployment)
>
> **Gate-based activity at decision points.**
>
> **In practice**: Verification is more frequent, validation is more expensive and time-consuming.
>
> **Automotive standard (ISO 26262)**: Validation required at phase transitions."

**PPT Content:**
```
WHEN TO VERIFY vs VALIDATE

VERIFICATION: Throughout Development
  • Requirements → Design → Code → Integration → Test
  • Continuous activity
  • Frequent, incremental
  • Lower cost per activity

VALIDATION: At Key Milestones
  • Concept → Design → System → Operations
  • Gate-based activity
  • Infrequent, comprehensive
  • Higher cost per activity

**ISO 26262 Requirement:**
  Validation at each phase transition

**Practical Rule:**
  Verify often (daily/weekly)
  Validate at gates (monthly/quarterly)
```

---

### **RISING ACTION Part 2: Integration Strategies** (Slides 12-15, ~12 minutes)

#### Slide 12: Integration Strategy Options
**Visual:** Four integration strategies visualized
**Instructor Script:**
> "Now let's address the integration challenge from Slide 7. There are four main integration strategies:
>
> **1. Big Bang Integration**
> - Integrate all components at once
> - Pros: Fast if it works
> - Cons: Debugging nightmare, high risk
> - When to use: Simple systems (<5 components), well-tested components
>
> **2. Bottom-Up Integration**
> - Start with lowest-level components, build up
> - Pros: Early hardware testing, realistic performance
> - Cons: No system-level view until late, requires test drivers
> - When to use: Hardware-dependent systems
>
> **3. Top-Down Integration**
> - Start with high-level control, stub lower components
> - Pros: Early system-level behavior, validates architecture
> - Cons: Stubs may not represent real performance
> - When to use: Software-intensive systems, architecture validation
>
> **4. Sandwich/Hybrid Integration**
> - Top-down for control logic, bottom-up for hardware
> - Pros: Best of both worlds
> - Cons: More complex to manage
> - When to use: Complex automotive systems (most cases)
>
> **Automotive standard**: Most OEMs use sandwich with HIL testing."

**PPT Content:**
```
INTEGRATION STRATEGIES: FOUR OPTIONS

1. Big Bang
   • All at once
   • Fast but risky

2. Bottom-Up
   • Start with hardware
   • Realistic performance

3. Top-Down
   • Start with control logic
   • Early system validation

4. Sandwich/Hybrid ← AUTOMOTIVE STANDARD
   • Combination approach
   • Best for complex systems

**Selection criteria:** System complexity, hardware dependencies, schedule
```

---

#### Slide 13: Bottom-Up Integration Example (LKA)
**Visual:** LKA integration sequence from hardware up
**Instructor Script:**
> "Let's see bottom-up integration for our LKA system:
>
> **Integration Sequence:**
>
> **Step 1**: Test camera hardware standalone
> - Verify camera captures images
> - Verify CAN interface works
> - Test with known patterns
>
> **Step 2**: Integrate camera + image processing ECU
> - Verify image data transfer
> - Check processing latency
> - Test with real road images
>
> **Step 3**: Add lane detection algorithm
> - Verify lane line detection accuracy
> - Check processing time < 50ms
> - Test various lighting conditions
>
> **Step 4**: Integrate control ECU
> - Verify control calculations
> - Test steering torque commands
> - Validate safety limits
>
> **Step 5**: Add steering actuator
> - Verify actual steering response
> - Measure end-to-end latency
> - Test force limits
>
> **Steps 6-8**: Add CAN bus, HMI, driver monitoring
>
> **Benefit**: At each step, only ONE new component. If something breaks, you know what caused it.
>
> **Drawback**: Don't see complete system behavior until Step 8."

**PPT Content:**
```
BOTTOM-UP INTEGRATION: LKA EXAMPLE

Step 1: Camera (standalone)
  ↓
Step 2: + Image Processing ECU
  ↓
Step 3: + Lane Detection Algorithm
  ↓
Step 4: + Control ECU
  ↓
Step 5: + Steering Actuator
  ↓
Step 6-8: + CAN, HMI, Driver Monitor

At each step:
  ✓ Test ONE new component
  ✓ Easy to isolate failures
  ✗ No system-level view until late

**Best for: Hardware-intensive systems**
```

---

#### Slide 14: Top-Down Integration with Stubs
**Visual:** Top-down integration with stub components
**Instructor Script:**
> "Top-down integration works differently. We start with the system-level controller and 'stub' the components:
>
> **Step 1**: Implement main control ECU with ALL components stubbed
> - Stub camera: Returns simulated lane lines
> - Stub actuator: Logs steering commands (doesn't move)
> - Validates overall control logic and state machine
>
> **Step 2**: Replace camera stub with real camera
> - Now using real image data
> - Control logic unchanged
> - Validates camera integration
>
> **Step 3**: Replace actuator stub with real actuator
> - Now producing real steering
> - Validates safety-critical path
>
> **Steps 4-8**: Replace remaining stubs one by one
>
> **Benefit**: See system-level behavior from Day 1. Validates architecture early.
>
> **Drawback**: Stubs may not capture real timing, performance issues. Can give false confidence.
>
> **Automotive use case**: Software-in-the-Loop (SIL) testing uses stubbed sensors/actuators extensively."

**PPT Content:**
```
TOP-DOWN INTEGRATION: WITH STUBS

Step 1: Control ECU + ALL STUBS
  • Stub camera → simulated data
  • Stub actuator → log commands
  • Validate control logic
  ↓
Step 2: Replace camera stub → REAL camera
  ↓
Step 3: Replace actuator stub → REAL actuator
  ↓
Steps 4-8: Replace remaining stubs

Benefits:
  ✓ Early system-level validation
  ✓ Architecture validation from Day 1
  ✗ Stubs may not capture real performance

**Best for: Software-intensive systems, early integration**
```

---

#### Slide 15: Sandwich Integration (Automotive Standard)
**Visual:** Sandwich integration combining top-down and bottom-up
**Instructor Script:**
> "In practice, automotive systems use **sandwich integration**:
>
> **Top layer** (Top-Down):
> - System controller
> - State machine
> - High-level decision logic
> - Validated early with SIL (Software-in-the-Loop)
>
> **Bottom layer** (Bottom-Up):
> - Sensors (camera, radar, lidar)
> - Actuators (steering, braking)
> - CAN communication
> - Validated early with HIL (Hardware-in-the-Loop)
>
> **Middle layer** (Last):
> - Sensor fusion algorithms
> - Control algorithms
> - Integrated after top and bottom layers proven
>
> **Timeline for LKA**:
> - Weeks 1-4: Top layer SIL + Bottom layer HIL (parallel)
> - Weeks 5-8: Integrate middle layer algorithms
> - Weeks 9-12: Full system integration and validation
>
> **Why this works**:
> - Reduces integration risk
> - Parallel development (software + hardware teams)
> - Early detection of interface issues
> - Industry standard approach (Tesla, BMW, Toyota all use variations)
>
> **This is what you'll use in practice.**"

**PPT Content:**
```
SANDWICH INTEGRATION: AUTOMOTIVE STANDARD

TOP LAYER (Top-Down):
  System controller, state machine
  Validated: SIL (Software-in-Loop)

MIDDLE LAYER (Last):
  Algorithms, sensor fusion
  Integrated: After top/bottom proven

BOTTOM LAYER (Bottom-Up):
  Sensors, actuators, CAN
  Validated: HIL (Hardware-in-Loop)

Timeline:
  Weeks 1-4: Top SIL + Bottom HIL (parallel)
  Weeks 5-8: Middle layer integration
  Weeks 9-12: Full system validation

**Industry standard for ADAS/autonomous systems**
```

---

### **RISING ACTION Part 3: Verification Methods** (Slides 16-18, ~8 minutes)

#### Slide 16: The Four Verification Methods
**Visual:** 2x2 matrix of verification methods
**Instructor Script:**
> "ISO/IEC 15288 and IEEE 15288 define FOUR verification methods. Every requirement must specify which method(s) will be used:
>
> **1. TEST (Most common)**
> - Stimulate system with inputs, measure outputs
> - Pros: High confidence, finds integration issues
> - Cons: Expensive, time-consuming
> - Examples: Road testing, HIL testing, EMC testing
> - **Use when**: Safety-critical functions, customer-facing features
>
> **2. ANALYSIS (Mathematical/simulation)**
> - Mathematical proof, simulation, modeling
> - Pros: Early feedback, explores parameter space
> - Cons: Only as good as model assumptions
> - Examples: Thermal analysis, stress analysis, timing analysis, simulation
> - **Use when**: Physical properties, performance prediction
>
> **3. INSPECTION (Visual/manual)**
> - Visual examination, code review, document review
> - Pros: Low cost, simple
> - Cons: Subjective, may miss issues
> - Examples: Code review, design review, drawing inspection
> - **Use when**: Qualitative requirements, documentation
>
> **4. DEMONSTRATION (Show it works)**
> - Demonstrate functionality in realistic scenario
> - Pros: Convincing, user-focused
> - Cons: May not cover edge cases
> - Examples: Customer demo, pilot program, trade show
> - **Use when**: User acceptance, stakeholder confidence
>
> **Automotive**: Typically 70% test, 20% analysis, 8% inspection, 2% demonstration."

**PPT Content:**
```
FOUR VERIFICATION METHODS (ISO/IEC 15288)

1. TEST
   • Stimulate inputs, measure outputs
   • High confidence, expensive
   • Example: Road testing, HIL

2. ANALYSIS
   • Mathematical/simulation
   • Early feedback, model-dependent
   • Example: Thermal, timing, stress

3. INSPECTION
   • Visual/manual examination
   • Low cost, subjective
   • Example: Code review, drawing check

4. DEMONSTRATION
   • Show it works in scenario
   • Convincing, may miss edge cases
   • Example: Customer demo

**Automotive typical: 70% test, 20% analysis, 8% inspect, 2% demo**
```

---

#### Slide 17: Verification Method Selection (AEB Example)
**Visual:** AEB requirements with verification methods mapped
**Instructor Script:**
> "Let's see how to select verification methods for AEB requirements:
>
> **Requirement AEB-FR-001**: 'System shall detect vehicles ahead within 150m range'
> - **Verification method**: TEST
> - **Rationale**: Safety-critical, must prove in real conditions
> - **Test**: Place target vehicle at 140m, 150m, 160m. Verify detection.
>
> **Requirement AEB-NFR-002**: 'System response time shall be < 150ms from detection to brake command'
> - **Verification method**: ANALYSIS + TEST
> - **Rationale**: Timing analysis can predict, test confirms
> - **Analysis**: WCET analysis of software timing
> - **Test**: Measure actual response time with oscilloscope
>
> **Requirement AEB-IF-005**: 'CAN message format shall comply with J1939 standard'
> - **Verification method**: INSPECTION + TEST
> - **Rationale**: Standards compliance check + functional test
> - **Inspection**: Review CAN database file
> - **Test**: CAN bus analyzer capture and decode
>
> **Requirement AEB-SAF-010**: 'System shall meet ISO 26262 ASIL-B'
> - **Verification method**: INSPECTION + DEMONSTRATION
> - **Rationale**: Process compliance + assessment
> - **Inspection**: Review safety artifacts (FMEA, FTA, safety case)
> - **Demonstration**: Present safety case to assessor
>
> **Notice**: Most requirements use MULTIPLE methods for higher confidence."

**PPT Content:**
```
VERIFICATION METHOD SELECTION: AEB EXAMPLE

Req ID          | Requirement                    | Method(s)
----------------|--------------------------------|------------------
AEB-FR-001      | Detect vehicles within 150m   | TEST
AEB-NFR-002     | Response time < 150ms          | ANALYSIS + TEST
AEB-IF-005      | CAN format per J1939           | INSPECTION + TEST
AEB-SAF-010     | Meet ISO 26262 ASIL-B          | INSPECTION + DEMO

**Key Insight:** Most requirements need MULTIPLE methods

**ISO 26262 guidance:** Safety requirements require at minimum:
  • Analysis (FMEA/FTA)
  • Test (functional + fault injection)
  • Inspection (safety case review)
```

---

#### Slide 18: Verification Traceability Matrix
**Visual:** Requirements traceability matrix showing verification methods
**Instructor Script:**
> "Every requirement must be traceable to its verification. This is the **Requirements Verification Traceability Matrix (RVTM)**:
>
> **RVTM Structure:**
> - Requirement ID
> - Requirement text
> - Verification method(s)
> - Test case ID / Analysis ID / Inspection ID
> - Verification status
> - Pass/Fail result
> - Evidence (test report reference)
>
> **Example RVTM for AEB (5 requirements shown)**:
>
> | Req ID | Requirement | Method | Test ID | Status | Result | Evidence |
> |--------|-------------|--------|---------|--------|--------|----------|
> | AEB-FR-001 | Detect vehicle 150m | Test | TC-AEB-001 | Complete | Pass | TR-2024-01 |
> | AEB-FR-002 | Brake if TTC<1.5s | Test | TC-AEB-002 | Complete | Pass | TR-2024-02 |
> | AEB-NFR-001 | Response <150ms | Analysis+Test | AN-001, TC-003 | Complete | Pass | AR-2024-01 |
> | AEB-IF-001 | CAN per J1939 | Inspect+Test | IN-001, TC-004 | Complete | Pass | IR-2024-01 |
> | AEB-SAF-001 | ASIL-B | Inspect+Demo | IN-002, DM-001 | In Progress | - | Pending |
>
> **Key benefits**:
> - Every requirement has verification plan
> - Traceability from requirement → test → evidence
> - Status tracking for program management
> - Compliance evidence for assessors (ISO 26262, Automotive SPICE)
>
> **Tools**: IBM DOORS, Jama Connect, Polarion, Excel (for small projects)
>
> **This matrix is your V&V roadmap.**"

**PPT Content:**
```
REQUIREMENTS VERIFICATION TRACEABILITY MATRIX (RVTM)

Columns:
  • Requirement ID
  • Requirement Text
  • Verification Method(s)
  • Test/Analysis/Inspection ID
  • Status (Not Started / In Progress / Complete)
  • Result (Pass / Fail / Pending)
  • Evidence Reference

Benefits:
  ✓ Every requirement has verification plan
  ✓ Traceability: Req → Test → Evidence
  ✓ Status tracking
  ✓ Compliance documentation

**RVTM = Your V&V roadmap and proof of completion**

Tools: DOORS, Jama, Polarion, Excel
```

---

### **RISING ACTION Part 4: Testing Levels** (Slides 19-22, ~12 minutes)

#### Slide 19: The Four Testing Levels
**Visual:** Pyramid showing four testing levels
**Instructor Script:**
> "Testing happens at FOUR levels, corresponding to the V-Model:
>
> **Level 1: UNIT TESTING** (Bottom of V)
> - Test: Individual software modules, hardware components
> - Scope: Single function, single file, single component
> - Who: Developers
> - Coverage: 80-100% code coverage target
> - Examples: Test lane detection algorithm function, test CAN driver module
>
> **Level 2: INTEGRATION TESTING** (Lower-middle of V)
> - Test: Interfaces between components
> - Scope: 2-5 components interacting
> - Who: Integration engineers
> - Coverage: All interface scenarios
> - Examples: Camera + image processing, Control ECU + actuator
>
> **Level 3: SYSTEM TESTING** (Upper-middle of V)
> - Test: Complete system against requirements
> - Scope: All components integrated
> - Who: Test engineers
> - Coverage: All system requirements
> - Examples: Full LKA system on test bench, HIL testing
>
> **Level 4: ACCEPTANCE TESTING** (Top of V)
> - Test: System in operational environment
> - Scope: Real-world usage scenarios
> - Who: Validation engineers + customers
> - Coverage: User needs and expectations
> - Examples: Road testing, beta fleet, customer validation
>
> **Key**: Each level builds on the previous. Don't skip levels."

**PPT Content:**
```
FOUR TESTING LEVELS (V-Model Alignment)

Level 4: ACCEPTANCE TESTING ← Validates needs
         Real-world scenarios
         Who: Validation + Customer

Level 3: SYSTEM TESTING ← Verifies requirements
         Complete system
         Who: Test engineers

Level 2: INTEGRATION TESTING ← Verifies interfaces
         Component interactions
         Who: Integration engineers

Level 1: UNIT TESTING ← Verifies implementation
         Individual modules
         Who: Developers

**Test Pyramid:** More unit tests, fewer acceptance tests
```

---

#### Slide 20: Unit Testing - Software and Hardware
**Visual:** Unit test examples for software and hardware
**Instructor Script:**
> "Unit testing for automotive systems includes BOTH software and hardware:
>
> **SOFTWARE UNIT TESTING:**
>
> Example: Testing `calculateSteeringTorque()` function in LKA controller
>
> **Test cases:**
> - TC-UT-001: Lane offset = 0.0m → Torque = 0.0 Nm (centered)
> - TC-UT-002: Lane offset = 0.3m right → Torque = +2.5 Nm (correct left)
> - TC-UT-003: Lane offset = 0.3m left → Torque = -2.5 Nm (correct right)
> - TC-UT-004: Lane offset = 1.0m → Torque clamped to ±8.0 Nm (safety limit)
> - TC-UT-005: No lane detected → Torque = 0.0 Nm (safe fallback)
>
> **Tool**: Unit test framework (Google Test, CUnit, VectorCAST)
> **Coverage**: Statement coverage 100%, branch coverage 95%+
>
> **HARDWARE UNIT TESTING:**
>
> Example: Testing camera module standalone
>
> **Test cases:**
> - TC-HW-001: Power supply 12V ± 1V → Camera outputs video
> - TC-HW-002: CAN bus 500 kbps → Camera sends frame data
> - TC-HW-003: Temperature -40°C to +85°C → Camera operates
> - TC-HW-004: Lens obstruction → Camera reports fault code
>
> **Tool**: Bench test setup, oscilloscope, CAN analyzer
>
> **Automotive standard (ASPICE)**: Unit testing is a MANDATORY practice."

**PPT Content:**
```
UNIT TESTING: SOFTWARE + HARDWARE

SOFTWARE UNIT TEST:
  Function: calculateSteeringTorque()

  Test Cases:
    • Lane centered → 0 Nm
    • 0.3m offset → ±2.5 Nm
    • 1.0m offset → clamp to ±8 Nm
    • No lane → 0 Nm (safe)

  Coverage: 100% statement, 95%+ branch

HARDWARE UNIT TEST:
  Component: Camera module

  Test Cases:
    • Power 12V±1V → video output
    • CAN 500kbps → frame data
    • Temp -40 to +85°C → operates
    • Lens blocked → fault code

**ASPICE Requirement: Unit testing mandatory**
```

---

#### Slide 21: Integration Testing - Interface Focus
**Visual:** Integration test showing component interfaces
**Instructor Script:**
> "Integration testing focuses on INTERFACES between components. This is where many automotive defects hide.
>
> **Integration Test Example: Camera → Image Processing ECU**
>
> **Test Scenario 1: Data Transfer**
> - TC-IT-001: Camera sends 1280x720 frame at 30 fps
> - Verify: ECU receives all frames, no data loss
> - Verify: Frame timestamps correct
> - Verify: No CAN bus overrun errors
>
> **Test Scenario 2: Timing**
> - TC-IT-002: Measure end-to-end latency camera → ECU
> - Verify: Latency < 50ms (requirement)
> - Verify: Jitter < 5ms
>
> **Test Scenario 3: Error Handling**
> - TC-IT-003: Camera sends corrupted frame
> - Verify: ECU detects checksum error
> - Verify: ECU requests retransmission
> - Verify: ECU continues operation (graceful degradation)
>
> **Test Scenario 4: Fault Injection**
> - TC-IT-004: Disconnect camera CAN cable
> - Verify: ECU detects timeout (within 100ms)
> - Verify: ECU sets DTC (Diagnostic Trouble Code)
> - Verify: ECU reports fault to vehicle supervisor
>
> **Why integration testing matters:**
> - 40% of automotive defects found at integration level
> - Interface specifications often ambiguous
> - Timing issues only appear when components interact
>
> **Tool**: HIL (Hardware-in-the-Loop) simulators (dSPACE, Vector, National Instruments)"

**PPT Content:**
```
INTEGRATION TESTING: INTERFACE FOCUS

Test: Camera → Image Processing ECU

Scenarios:
  1. Data Transfer
     • 1280x720 @ 30fps
     • Verify: No frame loss, correct timing

  2. Latency
     • Measure end-to-end < 50ms
     • Jitter < 5ms

  3. Error Handling
     • Corrupted frame → detect & recover

  4. Fault Injection
     • Disconnect → timeout, DTC, report

**40% of automotive defects found at integration level**

Tools: HIL (dSPACE, Vector, NI)
```

---

#### Slide 22: System and Acceptance Testing
**Visual:** Test track with vehicle performing system tests
**Instructor Script:**
> "The top two testing levels validate the complete system:
>
> **SYSTEM TESTING (Level 3)**
>
> **Purpose**: Verify ALL system requirements in controlled environment
>
> **LKA System Test Examples**:
> - TC-ST-001: Verify LKA keeps vehicle centered in lane on straight road
> - TC-ST-002: Verify LKA handles curves (radius > 250m)
> - TC-ST-003: Verify LKA disengages if driver overrides steering
> - TC-ST-004: Verify HMI warnings display correctly
> - TC-ST-005: Verify system works 10°C to 40°C
> - TC-ST-020: Verify emergency scenarios (brake during LKA, sudden lane change)
>
> **Environment**: Test track, proving ground, HIL simulator
> **Coverage**: 100% of system requirements
> **Tools**: Test vehicles, data logging, automated test scripts
>
> **ACCEPTANCE TESTING (Level 4)**
>
> **Purpose**: Validate system meets user needs in REAL operational environment
>
> **LKA Acceptance Test Examples**:
> - Field testing: 100,000 km on public roads
> - Weather conditions: Rain, snow, fog, night
> - Road types: Highway, city, rural, construction zones
> - Driver variability: Different driving styles
> - User feedback: Surveys, interviews, usability studies
>
> **Environment**: Real roads, real traffic, real customers
> **Coverage**: Operational scenarios and stakeholder needs
> **Duration**: Months (beta fleets, pilot programs)
>
> **Acceptance testing answers**: 'Does this solve the customer's problem?'
>
> **This is validation, not just verification.**"

**PPT Content:**
```
SYSTEM TESTING (Level 3): Verify Requirements

Environment: Controlled (test track, HIL)
Coverage: 100% system requirements
Examples:
  • LKA keeps centered in lane
  • Handles curves, disengages on override
  • HMI warnings correct
  • Temperature 10-40°C

Tools: Test vehicles, data logging, automation

ACCEPTANCE TESTING (Level 4): Validate Needs

Environment: Real-world (public roads)
Coverage: Operational scenarios
Examples:
  • 100,000 km field testing
  • Rain, snow, fog, night
  • Highway, city, rural
  • User feedback surveys

Duration: Months (beta fleets)

**Acceptance = Does it solve the customer problem?**
```

---

### **RISING ACTION Part 5: V&V Planning** (Slides 23-24, ~8 minutes)

#### Slide 23: V&V Plan Structure
**Visual:** V&V plan document outline
**Instructor Script:**
> "Every automotive system needs a comprehensive V&V Plan. Here's the standard structure:
>
> **Section 1: Introduction**
> - System overview
> - V&V objectives
> - Scope and boundaries
> - References (requirements, standards)
>
> **Section 2: V&V Strategy**
> - Verification approach (methods: test, analysis, inspection, demo)
> - Validation approach (field testing, user studies)
> - Integration strategy (big bang / bottom-up / top-down / sandwich)
> - Test levels (unit / integration / system / acceptance)
>
> **Section 3: Test Environment**
> - Test facilities (track, lab, HIL)
> - Test equipment (sensors, data acquisition, CAN tools)
> - Test vehicles
> - Environmental conditions
>
> **Section 4: Test Cases and Procedures**
> - Requirements Verification Traceability Matrix (RVTM)
> - Detailed test procedures for each test case
> - Pass/fail criteria
> - Expected results
>
> **Section 5: Test Schedule**
> - Timeline for each test level
> - Dependencies and sequencing
> - Resource allocation
> - Milestones
>
> **Section 6: Roles and Responsibilities**
> - Test manager, test engineers, developers
> - Approval authorities
> - Escalation procedures
>
> **Section 7: Risks and Mitigation**
> - Test environment unavailability
> - Schedule delays
> - Resource constraints
> - Contingency plans
>
> **Section 8: Reporting and Documentation**
> - Test reports format
> - Defect tracking process
> - Configuration management
> - Compliance evidence
>
> **Automotive standards**: ISO 26262 mandates V&V plan for ASIL B+ systems."

**PPT Content:**
```
V&V PLAN STRUCTURE (ISO 26262 Compliant)

1. Introduction (system, objectives, scope)
2. V&V Strategy (methods, levels, integration)
3. Test Environment (facilities, equipment, vehicles)
4. Test Cases & Procedures (RVTM, detailed tests)
5. Test Schedule (timeline, dependencies, milestones)
6. Roles & Responsibilities (team, approvals)
7. Risks & Mitigation (environment, schedule, resources)
8. Reporting & Documentation (reports, defects, evidence)

**ISO 26262:** V&V plan mandatory for ASIL B+

**Typical size:** 50-200 pages for ADAS system

**Tools:** DOORS, Jama (requirements trace), JIRA (defect tracking)
```

---

#### Slide 24: Test Coverage - How Much Is Enough?
**Visual:** Coverage pyramid showing different coverage types
**Instructor Script:**
> "One of the most common questions: 'How much testing is enough?' Let's look at coverage metrics:
>
> **SOFTWARE CODE COVERAGE:**
>
> **Statement Coverage**: Every line of code executed?
> - Target: 100% for safety-critical (ISO 26262 ASIL C/D)
> - Target: 80-90% for ASIL A/B
> - Tool: VectorCAST, LDRA, Cantata
>
> **Branch Coverage**: Every decision (if/else) tested both ways?
> - Target: 95%+ for safety-critical
> - More rigorous than statement coverage
>
> **Path Coverage**: Every execution path tested?
> - Target: Infeasible for large systems (combinatorial explosion)
> - Focus on critical paths
>
> **REQUIREMENTS COVERAGE:**
>
> **Functional Coverage**: Every requirement has passing test?
> - Target: 100% (non-negotiable)
> - Tracked in RVTM
>
> **Scenario Coverage**: Operational scenarios tested?
> - Target: Cover normal, boundary, exceptional cases
> - Example AEB: 30 km/h, 50 km/h, 80 km/h, 120 km/h (speed range)
> - Example AEB: Dry, wet, snow, ice (surface conditions)
>
> **INTERFACE COVERAGE:**
>
> **Message Coverage**: Every CAN message sent/received?
> - Target: 100% of defined messages
> - Tool: CANoe, CANalyzer
>
> **Fault Coverage**: Error scenarios tested?
> - Target: All single-point failures
> - Example: Sensor failures, communication timeouts, invalid data
>
> **Automotive Standard (ISO 26262)**:
> - ASIL A: 80% statement + branch coverage
> - ASIL B: 90% statement + branch coverage
> - ASIL C: 95% statement + branch + MC/DC coverage
> - ASIL D: 100% statement + branch + MC/DC coverage
>
> **Reality**: 100% coverage doesn't guarantee zero defects. But it's a necessary baseline."

**PPT Content:**
```
TEST COVERAGE: HOW MUCH IS ENOUGH?

CODE COVERAGE:
  • Statement: Every line executed
  • Branch: Every decision both ways
  • Path: Every execution path

  ISO 26262 Targets:
    ASIL A: 80% | ASIL B: 90% | ASIL C: 95% | ASIL D: 100%

REQUIREMENTS COVERAGE:
  • Functional: Every requirement tested → 100%
  • Scenario: Normal + boundary + exceptional

INTERFACE COVERAGE:
  • Message: Every CAN message → 100%
  • Fault: All single-point failures

**100% coverage ≠ zero defects, but it's the baseline**

Tools: VectorCAST, LDRA, CANoe
```

---

### **RISING ACTION Part 6: Traceability and Evidence** (Slide 25, ~5 minutes)

#### Slide 25: End-to-End Traceability
**Visual:** Traceability chain from stakeholder need → requirement → design → code → test → evidence
**Instructor Script:**
> "The final piece: bidirectional traceability. This is your proof that the system works.
>
> **FORWARD TRACEABILITY** (Left to Right on V-Model):
>
> Stakeholder Need → System Requirement → Subsystem Requirement → Design → Code → Build
>
> **Example for AEB:**
> - Stakeholder Need (SN-001): 'Reduce rear-end collisions'
> - System Requirement (SR-012): 'System shall detect vehicles ahead within 150m'
> - Subsystem Req (SSR-045): 'Radar shall detect targets at 5-150m range'
> - Design (DS-023): 'Use 77 GHz FMCW radar with ±45° FOV'
> - Code (radar_driver.c): Implementation of radar interface
> - Build (ECU-AEB-v2.3.1): Binary with radar driver
>
> **BACKWARD TRACEABILITY** (Right to Left on V-Model):
>
> Test Evidence → Test Case → Requirement → Stakeholder Need
>
> **Example for AEB:**
> - Test Evidence (TR-2024-056): Test report showing vehicle detected at 145m
> - Test Case (TC-AEB-012): 'Verify detection at 150m range'
> - System Requirement (SR-012): 'System shall detect vehicles ahead within 150m'
> - Stakeholder Need (SN-001): 'Reduce rear-end collisions'
>
> **BIDIRECTIONAL = Complete Chain**:
>
> Need ↔ Req ↔ Design ↔ Code ↔ Test ↔ Evidence
>
> **Why it matters:**
> - Impact analysis: If requirement changes, know what tests to rerun
> - Compliance: ISO 26262, Automotive SPICE demand traceability
> - Coverage: Ensure every need has verification
> - Root cause: Trace defects back to requirements
>
> **Tools**: IBM DOORS, Jama Connect, Polarion ALM
>
> **Without traceability, you have no proof your system works.**"

**PPT Content:**
```
END-TO-END BIDIRECTIONAL TRACEABILITY

FORWARD (Decomposition):
  Stakeholder Need → System Req → Subsystem Req
    → Design → Code → Build

BACKWARD (Verification):
  Test Evidence → Test Case → Requirement
    → Stakeholder Need

BIDIRECTIONAL (Complete):
  Need ↔ Req ↔ Design ↔ Code ↔ Test ↔ Evidence

Why Critical:
  ✓ Impact analysis (change management)
  ✓ Compliance (ISO 26262, ASPICE)
  ✓ Coverage assurance
  ✓ Root cause analysis

**No traceability = No proof**

Tools: DOORS, Jama, Polarion
```

---

### **CLIMAX: V&V in Practice - Real Case** (Slides 26-27, ~8 minutes)

#### Slide 26: Tesla Model S Autopilot Crash - V&V Failure Analysis
**Visual:** Timeline of 2016 Tesla Model S fatal crash in Florida
**Instructor Script:**
> "Let's examine a tragic V&V failure: the 2016 Tesla Model S Autopilot crash in Florida.
>
> **Incident Overview:**
> - May 7, 2016: Model S in Autopilot mode
> - White tractor-trailer crossing highway
> - Autopilot failed to detect trailer
> - Driver failed to take control
> - Fatal collision
>
> **V&V Failure Analysis:**
>
> **1. Incomplete Scenario Coverage**
> - **What was tested**: Standard vehicle detection (cars, trucks on same lane)
> - **What wasn't tested**: Perpendicular white vehicles against bright sky
> - **Gap**: Cross-traffic scenarios not in test suite
> - **Lesson**: Validation must include operational context, not just requirements
>
> **2. Sensor Fusion Validation Inadequate**
> - Camera: Detected trailer but classified as overhead sign (white + high)
> - Radar: Detected metal but classified as overhead structure
> - Fusion logic: Both sensors agreed 'not a vehicle' → ignored
> - **Gap**: No validation of conflicting sensor interpretations
> - **Lesson**: Integration testing must stress-test fusion logic with ambiguous inputs
>
> **3. Human Factors Validation Missing**
> - System name 'Autopilot' implied full autonomy
> - Users treated it as self-driving (validation gap)
> - No adequate driver monitoring
> - **Gap**: Validation of human-system interaction inadequate
> - **Lesson**: Validate system in realistic usage, not just ideal usage
>
> **4. Edge Case Testing Insufficient**
> - White vehicle + bright sky = unusual scenario
> - But not impossible or unforeseeable
> - Should have been in acceptance test scenarios
> - **Gap**: Edge case identification incomplete
> - **Lesson**: Validation must explore 'rare but possible' scenarios
>
> **NTSB Findings:**
> - 'Tesla's validation process did not account for driver misuse scenarios'
> - 'System tested primarily in highway scenarios with conventional vehicles'
> - 'Inadequate testing of perception system in unusual lighting conditions'
>
> **What should have been tested** (but wasn't):
> - Cross-traffic scenarios
> - White vehicles in high-contrast lighting
> - Driver monitoring effectiveness
> - Realistic driver behavior (not just attentive drivers)
>
> **Result**: Tesla added cross-traffic detection, improved driver monitoring, clarified Autopilot limitations."

**PPT Content:**
```
CASE STUDY: 2016 TESLA MODEL S AUTOPILOT CRASH

Incident: Autopilot failed to detect white trailer crossing highway

V&V FAILURES IDENTIFIED:

1. Incomplete Scenario Coverage
   ✗ Cross-traffic not tested
   Lesson: Validate operational context

2. Sensor Fusion Validation Inadequate
   ✗ Ambiguous input cases not tested
   Lesson: Stress-test fusion logic

3. Human Factors Validation Missing
   ✗ Realistic usage not validated
   Lesson: Test actual user behavior

4. Edge Case Testing Insufficient
   ✗ Rare scenarios not covered
   Lesson: Explore 'possible but unusual'

**NTSB: "Validation did not account for real usage scenarios"**

Changes: Added cross-traffic detection, driver monitoring
```

---

#### Slide 27: Key V&V Lessons from Automotive Failures
**Visual:** Compilation of automotive V&V lessons
**Instructor Script:**
> "Let's synthesize V&V lessons from multiple automotive failures:
>
> **Lesson 1: Verification ≠ Validation** (Toyota ETCS)
> - Toyota verified ETCS met all specifications (passed all tests)
> - But didn't validate that specifications were complete and correct
> - Missing scenarios: floor mat interference, concurrent inputs
> - **Takeaway**: Don't just verify specs, validate that specs are right
>
> **Lesson 2: 100% Code Coverage ≠ 100% Tested** (Therac-25)
> - All code paths tested, but not all race conditions
> - Timing-dependent bugs missed
> - **Takeaway**: Coverage metrics are necessary but not sufficient
>
> **Lesson 3: Simulator ≠ Reality** (Early autonomous vehicles)
> - Systems perfect in simulation, fail on real roads
> - Simulator didn't model: dirty sensors, unusual objects, edge cases
> - **Takeaway**: Simulation + real-world testing both required
>
> **Lesson 4: Test What You Fly, Fly What You Test** (Mars Climate Orbiter)
> - Software tested in metric units
> - Flight software used imperial units
> - Test environment ≠ flight environment
> - **Takeaway**: Test with actual flight configuration
>
> **Lesson 5: Edge Cases Are Not 'Edge Cases'** (Tesla, Uber crashes)
> - 'Rare' scenarios happen millions of times across vehicle fleet
> - 1-in-million scenario × 1M vehicles = happens every day
> - **Takeaway**: Test edge cases as thoroughly as normal cases
>
> **Lesson 6: Human Element Is Part of the System** (Multiple)
> - Systems designed for perfect drivers fail with real drivers
> - Must validate human-system interaction
> - **Takeaway**: Include human factors in validation
>
> **Lesson 7: Field Data Is Gold** (All OEMs)
> - Real-world failures reveal scenarios designers never imagined
> - Fleet data identifies validation gaps
> - **Takeaway**: Use field data to improve V&V for next generation
>
> **For your career**: Apply these lessons to EVERY automotive system you work on."

**PPT Content:**
```
KEY V&V LESSONS FROM AUTOMOTIVE FAILURES

1. Verification ≠ Validation
   Verify specs are met AND validate specs are right

2. 100% Coverage ≠ 100% Tested
   Metrics necessary but not sufficient

3. Simulator ≠ Reality
   Simulate AND test in real world

4. Test What You Fly, Fly What You Test
   Verify actual configuration, not test config

5. Edge Cases Aren't 'Edge'
   Rare × fleet size = happens often

6. Human Element Is Part of System
   Validate human-system interaction

7. Field Data Is Gold
   Learn from real-world failures

**Apply these lessons to EVERY system you work on**
```

---

### **RESOLUTION: Putting It All Together** (Slides 28-30, ~12 minutes)

#### Slide 28: V&V Best Practices Summary
**Visual:** Checklist of V&V best practices
**Instructor Script:**
> "Let's consolidate the best practices for automotive V&V:
>
> **Planning Phase:**
> ✓ Create V&V plan early (during requirements phase)
> ✓ Select verification methods for each requirement
> ✓ Build Requirements Verification Traceability Matrix (RVTM)
> ✓ Define test coverage targets (ISO 26262 compliance)
> ✓ Plan integration strategy (sandwich recommended)
>
> **Execution Phase:**
> ✓ Start testing early (unit tests during development)
> ✓ Test at all four levels (unit → integration → system → acceptance)
> ✓ Use multiple verification methods (test + analysis + inspection)
> ✓ Automate regression testing
> ✓ Document evidence for every test
>
> **Quality Phase:**
> ✓ Achieve code coverage targets (80-100% per ASIL)
> ✓ Ensure 100% requirements coverage
> ✓ Test edge cases and fault scenarios
> ✓ Validate human-system interaction
> ✓ Conduct real-world field testing
>
> **Documentation Phase:**
> ✓ Maintain bidirectional traceability
> ✓ Generate test reports with pass/fail evidence
> ✓ Track and close all defects
> ✓ Create safety case (ISO 26262)
> ✓ Archive configuration and test data
>
> **Continuous Improvement:**
> ✓ Analyze field failures
> ✓ Update test cases based on field data
> ✓ Improve V&V process each iteration
> ✓ Share lessons learned across projects
>
> **Follow these practices, and your V&V will be robust.**"

**PPT Content:**
```
V&V BEST PRACTICES CHECKLIST

PLANNING:
  ✓ V&V plan early (requirements phase)
  ✓ Verification methods per requirement
  ✓ Build RVTM
  ✓ Define coverage targets (ISO 26262)
  ✓ Integration strategy (sandwich)

EXECUTION:
  ✓ Test early (unit tests in development)
  ✓ All four levels (unit → accept)
  ✓ Multiple methods (test + analysis)
  ✓ Automate regression
  ✓ Document evidence

QUALITY:
  ✓ Code coverage (80-100%)
  ✓ 100% requirements coverage
  ✓ Edge cases + faults
  ✓ Human factors validation
  ✓ Real-world field testing

DOCUMENTATION:
  ✓ Bidirectional traceability
  ✓ Test reports
  ✓ Defect closure
  ✓ Safety case
  ✓ Archive data
```

---

#### Slide 29: Connection to Remaining Sessions and Mid-Semester Review
**Visual:** Course roadmap showing Sessions 1-8 complete, Sessions 9-16 ahead
**Instructor Script:**
> "Session 8 completes our first half. Let's connect everything and preview what's ahead:
>
> **Sessions 1-8 Completed:**
>
> **Module 1: Foundations** (Sessions 1-4)
> - Session 1: Why SE matters (failures)
> - Session 2: SE fundamentals (ISO/IEC 15288, V-Model)
> - Session 3: Traditional vs MBSE
> - Session 4: Requirements Engineering
>
> **Module 2: Design & Analysis** (Sessions 5-8)
> - Session 5: System Architecture
> - Session 6: Case Study 1 (Boeing 737 MAX)
> - Session 7: Functional Analysis
> - Session 8: Integration & V&V ← TODAY
>
> **You now know**:
> - How to define systems (requirements)
> - How to design systems (architecture)
> - How to analyze systems (functional decomposition)
> - How to verify and validate systems (V&V)
>
> **This is the core SE lifecycle.**
>
> **Sessions 9-16 Ahead:**
>
> **Module 3: Management** (Sessions 9-12)
> - Session 9: Project & Risk Management
> - Session 10: Decision & Quality Management
> - Session 11: Agreement & Infrastructure Management
> - Session 12: Specialty Engineering (Safety & Security)
>
> **Module 4: Lifecycle & Trends** (Sessions 13-16)
> - Session 13: Life Cycle Cost (LCC) & TCO
> - Session 14: Case Study 2
> - Session 15: Technical Management & Enabling Processes
> - Session 16: Emerging Trends in SE
>
> **Coming up**: Management processes that enable successful SE execution.
>
> **Mid-semester exam** covers Sessions 1-8. Use this session as your integration point."

**PPT Content:**
```
MID-SEMESTER CHECKPOINT: SESSIONS 1-8 COMPLETE

MODULE 1: Foundations (Sessions 1-4)
  ✓ Why SE matters
  ✓ SE fundamentals
  ✓ Traditional vs MBSE
  ✓ Requirements engineering

MODULE 2: Design & Analysis (Sessions 5-8)
  ✓ System architecture
  ✓ Case study 1
  ✓ Functional analysis
  ✓ Integration & V&V ← TODAY

**Core SE Lifecycle Complete**

AHEAD: Modules 3-4 (Sessions 9-16)
  • Management (project, risk, quality)
  • Lifecycle cost
  • Emerging trends

**Mid-semester exam: Sessions 1-8**
```

---

#### Slide 30: Key Takeaways and Practice Exercise
**Visual:** Key takeaways with practice assignment
**Instructor Script:**
> "Let's lock in the key takeaways from Session 8:
>
> **Key Takeaway 1**: Verification asks 'Did we build it right?' (meets specs), Validation asks 'Did we build the right thing?' (meets needs). Both required.
>
> **Key Takeaway 2**: Integration strategy matters. Use sandwich integration (top-down + bottom-up) for automotive systems. Avoid big bang.
>
> **Key Takeaway 3**: Four verification methods (test, analysis, inspection, demonstration). Use multiple methods for safety-critical requirements.
>
> **Key Takeaway 4**: Test at four levels (unit, integration, system, acceptance). Each level serves a purpose. Don't skip levels.
>
> **Key Takeaway 5**: Coverage is necessary but not sufficient. Achieve 100% requirements coverage and ISO 26262 code coverage targets.
>
> **Key Takeaway 6**: Bidirectional traceability from need → requirement → design → code → test → evidence is your proof.
>
> **Key Takeaway 7**: Validation must include edge cases, human factors, and real-world scenarios. Simulator alone is insufficient.
>
> **PRACTICE EXERCISE**: Develop V&V Plan for Adaptive Cruise Control (ACC)
>
> **Assignment**:
> Create a 5-8 page V&V plan for an Adaptive Cruise Control system covering:
> 1. V&V Strategy (integration approach, verification methods)
> 2. Test Levels (unit, integration, system, acceptance examples)
> 3. Requirements Verification Traceability Matrix (RVTM) for 10 ACC requirements
> 4. Test Coverage Plan (code, requirements, scenarios)
> 5. Test Schedule (timeline for 12-week V&V program)
>
> **Deliverables**:
> - V&V Plan document (follow structure from Slide 23)
> - RVTM with 10 requirements mapped to test cases
> - Integration test sequence diagram (show order of component integration)
>
> **Due**: One week before mid-semester exam
>
> **Grading**:
> - V&V strategy completeness (30%)
> - RVTM quality (30%)
> - Test coverage plan (20%)
> - Integration sequence (10%)
> - Professional formatting (10%)
>
> **This exercise prepares you for the mid-semester exam and real-world V&V planning.**"

**PPT Content:**
```
SESSION 8 KEY TAKEAWAYS

1. Verification (right) vs Validation (right thing) → Both needed
2. Sandwich integration (top + bottom) for automotive
3. Four verification methods → Use multiple for safety
4. Four test levels (unit → accept) → Don't skip
5. 100% requirements coverage + ISO 26262 targets
6. Bidirectional traceability = proof
7. Validate edge cases + human factors + real-world

PRACTICE EXERCISE: ACC V&V Plan

Create 5-8 page V&V plan covering:
  • V&V strategy (integration, methods)
  • Test levels (examples for each)
  • RVTM (10 requirements)
  • Coverage plan (code, req, scenarios)
  • Test schedule (12-week timeline)

Due: 1 week before mid-semester
Grading: Strategy 30%, RVTM 30%, Coverage 20%

**Prepares you for exam and real-world V&V**
```

---

## 📝 INSTRUCTOR NOTES

### Pedagogical Strategy

**Approach: Process-Focused/Technical**
This session requires balancing theoretical V&V concepts with practical automotive application. The pedagogy emphasizes:

1. **Clear Distinctions**: Verification vs validation is foundational. Use multiple examples to cement this.
2. **Practical Integration**: Sandwich integration is industry standard. Show why through LKA example.
3. **Real Consequences**: Use Tesla, Toyota cases to show V&V failures have real costs.
4. **Comprehensive Coverage**: Four methods × four levels = complete V&V framework.
5. **Traceability Emphasis**: This is what separates amateur from professional V&V.

**Mid-Semester Integration**: This session serves as the capstone for Sessions 1-7. Explicitly connect V&V back to requirements (S4), architecture (S5), and functional analysis (S7).

### Common Student Challenges

**Challenge 1**: "Isn't verification just testing?"
**Response**: No. Testing is ONE verification method. Analysis (simulation, math), inspection (review), and demonstration are equally valid. Show examples where testing is insufficient (timing analysis, thermal analysis).

**Challenge 2**: "Why is integration so complicated? Just connect everything."
**Response**: Use the LKA debugging nightmare example (Slide 8). When 8 components have 28 interactions, big bang fails. Show how sandwich systematically reduces debug complexity.

**Challenge 3**: "100% code coverage means zero bugs, right?"
**Response**: No. Coverage metrics tell you what you tested, not what you didn't test. Therac-25 example: all paths tested, but race condition timing not tested. Coverage is necessary, not sufficient.

**Challenge 4**: "Validation seems subjective. How do we measure it?"
**Response**: Validation IS more subjective than verification, but still measurable: user surveys, field trial data, incident rates, customer acceptance criteria. Show AEB example: measure actual collision reduction in fleet.

### Timing Management

**Critical timing considerations**:
- **Part 3 (Verification Methods)** can run long if you demo tools. Limit tool demos to 2 minutes each, focus on concepts.
- **Part 4 (Testing Levels)** is the most detailed. Budget full 12 minutes. Students need concrete examples at each level.
- **Case Study (Slide 26-27)** can generate extensive discussion. Set 8-minute timer, defer detailed debate to case study session.
- **Reserve 5 minutes** at end for Q&A on mid-semester exam scope.

**If running short on time**:
- Condensed: Combine Slides 12-15 into high-level integration overview (5 min instead of 12 min)
- Skip: Slide 18 (RVTM details) can be assigned as reading

**If extra time**:
- **Tool demonstration**: Show actual DOORS/Jama traceability or CANoe integration test
- **V&V plan review**: Walk through real automotive V&V plan (if available)
- **Extended case discussion**: Tesla Autopilot regulatory response

### Engagement Points

1. **Slide 7**: Poll students - "Who would choose big bang? Who incremental?" Show of hands before revealing answer.

2. **Slide 10**: Interactive question - "Is AEB verification or validation?" Have students argue both sides.

3. **Slide 16**: Quick exercise - "For this requirement (provide example), which verification method?" Students vote.

4. **Slide 22**: "What scenarios should we test for LKA acceptance?" Brainstorm as group, capture on whiteboard.

5. **Slide 26**: "What V&V would have prevented Tesla crash?" Small group discussion (3 minutes).

### Materials Preparation

**Before class**:
- [ ] Load Tesla Autopilot crash video (2-3 minute clip)
- [ ] Prepare V-Model diagram animation showing bidirectional flow
- [ ] Print sample RVTM for handout reference
- [ ] Load CANoe or similar tool for optional integration test demo
- [ ] Prepare ACC V&V plan template for exercise

**Optional materials**:
- Real automotive V&V plan (redacted) for show-and-tell
- ISO 26262 Part 4 (V&V requirements) excerpt
- Test reports from automotive projects (sanitized)

### Assessment Opportunities

**Formative Assessment** (During Session):
- Quick check after Slide 11: "Give me one verification example and one validation example for your car's ABS"
- Quick check after Slide 19: "At which test level would you find this defect?" (provide scenario)
- Quick check after Slide 25: "If requirement SR-045 changes, what must you update?" (test traceability)

**Summative Assessment** (Exercise):
- ACC V&V Plan development (detailed in Slide 30)
- Graded against professional V&V plan standards
- Provides mid-semester exam preparation

**Mid-Semester Exam Coverage**:
Session 8 contributes 15-20% of mid-semester exam questions:
- Verification vs validation distinction (definition question)
- Integration strategy selection (scenario question)
- Verification method selection for requirements (application question)
- Test level identification (case-based question)
- RVTM interpretation (analysis question)

### Success Criteria

Students successfully understand Session 8 if they can:

1. **Define** verification and validation, giving automotive examples of each
2. **Select** appropriate integration strategy for a given system
3. **Choose** verification methods for different requirement types
4. **Design** test cases at all four test levels
5. **Calculate** test coverage and identify gaps
6. **Create** traceability matrix linking requirements to tests
7. **Analyze** V&V failures in case studies and propose improvements

### Connections to Other Sessions

**Backward Links**:
- **Session 2**: V-Model right side connects to Session 2's V-Model introduction
- **Session 4**: Requirements from Session 4 must have verification methods
- **Session 5**: Architecture from Session 5 drives integration strategy
- **Session 7**: Functions from Session 7 are verified at unit/integration levels

**Forward Links**:
- **Session 9**: V&V risks are managed through risk management processes
- **Session 10**: V&V is a key quality management activity
- **Session 12**: Safety V&V (ISO 26262) is covered in specialty engineering
- **Session 14**: Case Study 2 will apply V&V analysis to another failure

### Additional Resources

**Standards**:
- ISO/IEC/IEEE 15288:2023 (Systems and software engineering - System life cycle processes)
- ISO 26262:2018 Part 4 (Product development at the system level - V&V)
- Automotive SPICE v3.1 (SWE.4: Software Unit Verification, SWE.5: Software Integration)

**Tools**:
- VectorCAST (code coverage)
- IBM DOORS / Jama Connect (requirements traceability)
- CANoe / CANalyzer (integration testing)
- dSPACE / ETAS (HIL testing)

**Further Reading**:
- "Software Testing" by Ron Patton (Chapter 3: Test Levels)
- "Systems Engineering Handbook" INCOSE (Chapter 7: Verification and Validation)
- ISO 26262 Part 4 (full standard for automotive safety V&V)

---

## END OF SESSION 8 FRAMEWORK

**Prepared for**: Automotive Systems Engineering (AE ZG517 / AEL ZG517)
**Session**: 8 of 16
**Status**: Ready for PPT Development
**Estimated PPT Slides**: 28-30
**Total Instructor Preparation Time**: 3-4 hours
