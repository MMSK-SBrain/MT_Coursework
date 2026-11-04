# Session 7: Operational and Functional Analysis
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 90 minutes lecture + 30 minutes Q&A
**Approach:** Analytical/Process-Based
**PPT Target:** 28-30 slides

---

## 🎯 Session Objectives (For Instructor)

By the end of this session, students will be able to:
- Define operational scenarios and develop use cases for automotive systems
- Perform capability gap analysis to identify functional requirements
- Decompose system behavior into discrete functions
- Create functional flow block diagrams (FFBD) to model system operations
- Allocate requirements to specific functions systematically
- Develop functional architectures that bridge requirements and design
- Perform timeline analysis to validate operational feasibility
- Apply functional analysis methods to complex automotive systems (ADAS, autonomous vehicles)

**Mapped Learning Outcomes:** LO2 (Develop requirements, architectures, specifications, verifications, and tests), LO5 (Analyse automotive systems using systems engineering approaches to increase performance)

---

## 📖 INSTRUCTOR-LED STORY ARC

### **SETUP: From Architecture to Operations** (Slides 1-5, ~10 minutes)

#### Slide 1: Title
**Visual:** Professional title slide with functional flow diagram overlay
**Instructor Script:**
> "Welcome to Session 7. Today we bridge a critical gap in systems engineering: the translation from system architecture to actual operational behavior.
>
> We're going to answer the question: **'What does the system actually DO when it's operating?'**
>
> This is Operational and Functional Analysis - the systematic decomposition of system behavior into executable functions."

#### Slide 2: Connection to Session 5 - System Architecture
**Visual:** V-Model diagram highlighting progression from Session 5 to Session 7
**Instructor Script:**
> "Let's connect where we've been to where we're going:
>
> **Session 5 - System Design and Architecture**:
> - We learned how to develop system architecture
> - We defined system boundaries and context
> - We created high-level design concepts
> - We performed trade studies and alternatives analysis
>
> **What Session 5 gave us**: STRUCTURAL view of the system
> - Components: ECUs, sensors, actuators, networks
> - Interfaces: CAN bus messages, power connections, mechanical linkages
> - Static relationships: 'Radar sensor connects to ADAS ECU via CAN'
>
> **What Session 5 did NOT give us**: BEHAVIORAL view
> - What happens during a lane change?
> - How do functions coordinate during emergency braking?
> - What's the sequence of operations when cruise control engages?
>
> **Today's focus**: We add the BEHAVIORAL dimension through operational and functional analysis.
>
> **The key insight**: Architecture tells us WHAT we have. Functional analysis tells us what the system DOES."

#### Slide 3: The Critical Gap - Structure vs Behavior
**Visual:** Two-column comparison showing structural vs functional views
**Instructor Script:**
> "Let me illustrate the gap we're filling today with a real automotive example.
>
> **Adaptive Cruise Control (ACC) - Structural View** (from Session 5):
> ```
> Components:
> - Forward radar sensor
> - ACC ECU
> - Engine control ECU
> - Brake control ECU
> - Driver interface (steering wheel buttons)
> - CAN communication network
> ```
>
> This tells us the 'parts list.' But it doesn't answer operational questions:
>
> **Operational Questions (Behavioral View)**:
> - What happens when driver presses SET button?
> - How does the system respond when a vehicle cuts in front?
> - What's the sequence of actions during emergency braking?
> - How do radar detection, speed control, and braking coordinate?
> - What happens if the radar sensor fails during operation?
>
> **Functional analysis answers these questions** by decomposing behavior into:
> 1. **Operational scenarios** - How the system is used
> 2. **Functional flows** - Sequence of operations
> 3. **Function allocation** - Mapping requirements to functions
> 4. **Timeline analysis** - Temporal validation
>
> Today, you'll learn to perform this analysis systematically."

#### Slide 4: Why Functional Analysis Is Critical
**Visual:** Statistics and failure examples
**Instructor Script:**
> "Why does this matter? Let me show you what happens when we skip functional analysis.
>
> **Case 1: Tesla Autopilot Fatal Crash (2016)**
> - **Structural view**: System had camera, radar, ultrasonic sensors, powerful ECU
> - **Missing functional analysis**: What happens when camera can't distinguish white truck from bright sky?
> - **Result**: System failed to brake. Fatal accident.
> - **Root cause**: Inadequate operational scenario analysis - 'crossing traffic' scenario not fully analyzed
>
> **Case 2: Boeing 737 MAX MCAS Failures (2018-2019)**
> - **Structural view**: System had angle-of-attack sensors, flight control computer, trim actuators
> - **Missing functional analysis**: What happens when single sensor fails? How do pilot inputs interact with MCAS?
> - **Result**: 346 deaths, aircraft grounded worldwide
> - **Root cause**: Incomplete functional flow analysis - failure modes and pilot interaction scenarios not fully modeled
>
> **Common failure pattern**:
> - Engineers design components (structure)
> - Components work individually
> - But system BEHAVIOR is not analyzed
> - Result: Unexpected interactions, unhandled scenarios, failures
>
> **Statistics from NASA/DoD systems analysis**:
> - 40% of system failures trace to incomplete operational scenario analysis
> - 35% trace to missing functional requirements
> - 60% of integration problems come from interface behavior (not structure)
>
> **Today's tools prevent these failures** by forcing us to think through every operational scenario systematically."

#### Slide 5: Learning Journey for Today
**Visual:** Roadmap with 5 major sections
**Instructor Script:**
> "Today's journey has five critical parts:
>
> **Part 1: Operational Scenarios and Use Cases** (Slides 6-10)
> - How do we capture how the system will be used?
> - Developing comprehensive operational scenarios
> - Use case modeling for automotive systems
>
> **Part 2: Capability Gap Analysis** (Slides 11-13)
> - What capabilities do we need vs what we have?
> - Identifying functional requirements from gaps
>
> **Part 3: Functional Decomposition** (Slides 14-18)
> - Breaking down system behavior into discrete functions
> - Function hierarchies and decomposition strategies
>
> **Part 4: Functional Flow Block Diagrams (FFBD)** (Slides 19-23)
> - Visualizing operational sequences
> - FFBD notation and development
> - Applying FFBD to complex automotive scenarios
>
> **Part 5: Requirements Allocation and Timeline Analysis** (Slides 24-27)
> - Mapping requirements to functions
> - Validating timing and feasibility
>
> By the end, you'll be able to take a system architecture and develop a complete functional model that describes every operational behavior."

---

### **TRIGGER: The Lane Keep Assist Challenge** (Slides 6-7, ~8 minutes)

#### Slide 6: The Design Challenge
**Visual:** Lane Keep Assist system context diagram
**Instructor Script:**
> "Let me give you a real challenge from the automotive industry.
>
> **Scenario**: Your team has been assigned to develop a Lane Keep Assist (LKA) system for a new vehicle platform.
>
> **System Architecture** (already defined in Session 5):
> - Front-facing camera (lane line detection)
> - LKA ECU (processing and control)
> - Electric power steering (EPS) ECU
> - Driver display and alerts
> - CAN network
>
> **System Requirements** (defined in Session 4):
> - REQ-LKA-001: 'System shall detect lane departure and apply corrective steering'
> - REQ-LKA-002: 'System shall operate at speeds between 60-180 km/h'
> - REQ-LKA-003: 'System shall alert driver before applying steering correction'
> - REQ-LKA-004: 'System shall disengage if driver overrides'
> ... plus 50+ more requirements
>
> **The question your manager asks**:
> 'Show me exactly what happens, step-by-step, when the vehicle starts to drift out of the lane.'
>
> **Can you answer this from the architecture diagram alone?** NO.
> **Can you answer this from the requirements list alone?** NO.
>
> **You need functional analysis.**"

#### Slide 7: What We Need to Know
**Visual:** Mind map of operational questions
**Instructor Script:**
> "Here are the questions we must answer before we can design the software and integrate the system:
>
> **Operational Scenario Questions**:
> - When is LKA active vs inactive?
> - What are all the ways a driver can activate/deactivate LKA?
> - What happens during lane changes (intentional departure)?
> - What happens on curved roads vs straight roads?
> - What happens if lane lines are faded or missing?
> - What happens in construction zones with multiple lane lines?
>
> **Functional Sequence Questions**:
> - What's the step-by-step process from lane detection to steering correction?
> - How do we distinguish intentional lane change from unintentional drift?
> - What's the coordination between camera processing, decision logic, and steering actuation?
> - What's the timing - how fast must each step execute?
>
> **Failure Mode Questions**:
> - What happens if camera is blocked (rain, snow, dirt)?
> - What happens if steering system is already at maximum torque?
> - What happens if driver and system both try to steer?
>
> **Integration Questions**:
> - How does LKA interact with adaptive cruise control?
> - How does it interact with automatic emergency braking?
> - Who has priority if multiple systems request steering input?
>
> **These are operational and functional analysis questions.**
>
> Today, I'll show you systematic methods to answer every one of them."

---

### **RISING ACTION: Building the Functional Model** (Slides 8-23, ~52 minutes)

#### **Part 1: Operational Scenarios and Use Cases** (Slides 8-10, ~12 minutes)

##### Slide 8: What Is an Operational Scenario?
**Visual:** Definition and example structure
**Instructor Script:**
> "Let's start with the foundation: **Operational scenarios**.
>
> **Definition**: An operational scenario is a narrative description of how the system will be used in a specific context to achieve specific goals.
>
> **Key elements of an operational scenario**:
> 1. **Actors** - Who/what interacts with the system
> 2. **Context** - Environmental and operational conditions
> 3. **Trigger** - What initiates the scenario
> 4. **Goal** - What the actor/system wants to achieve
> 5. **Sequence** - Step-by-step description of interactions
> 6. **Outcomes** - Success criteria and possible variations
>
> **Example: Lane Keep Assist - Normal Operation Scenario**
>
> **Scenario ID**: OPS-LKA-001
> **Title**: Lane keeping on highway with clear lane markings
>
> **Actors**:
> - Driver (primary)
> - Vehicle systems (LKA, EPS, camera)
> - Environment (highway, other vehicles)
>
> **Context**:
> - Highway driving
> - Vehicle speed: 100 km/h
> - Clear weather, good visibility
> - Well-marked lanes
> - Light traffic
>
> **Trigger**: Driver activates LKA via steering wheel button
>
> **Goal**: Maintain vehicle centered in lane without driver steering input
>
> **Sequence**:
> 1. Driver presses LKA activation button
> 2. System checks preconditions (speed >60 km/h, lane lines detected)
> 3. System displays 'LKA Active' on instrument cluster (green indicator)
> 4. Camera continuously monitors lane position (20 Hz)
> 5. System calculates lateral offset from lane center
> 6. **Nominal case**: Vehicle centered, no correction needed
> 7. **Drift detected**: Vehicle drifts 0.3m toward lane edge
> 8. System calculates required steering correction (0.5° left)
> 9. System sends torque request to EPS ECU
> 10. EPS applies gentle corrective steering (0.8 Nm)
> 11. Vehicle returns to lane center
> 12. System reduces steering input as centering achieved
>
> **Outcomes**:
> - **Success**: Vehicle maintains lane position, driver informed
> - **Variation 1**: Driver overrides (hands on wheel) → system yields, remains active
> - **Variation 2**: Driver signals lane change → system disengages temporarily
>
> **This is ONE scenario. A complete LKA system needs 20-30 operational scenarios.**"

##### Slide 9: Comprehensive Scenario Development
**Visual:** Matrix of operational scenarios for LKA
**Instructor Script:**
> "How do we ensure we've captured ALL operational scenarios? Systematic enumeration.
>
> **LKA Operational Scenario Matrix**:
>
> **Dimension 1 - Operational Modes**:
> - Activation scenarios (driver-initiated, conditions met)
> - Normal operation (lane keeping)
> - Lane change scenarios (intentional departure)
> - Override scenarios (driver intervention)
> - Deactivation scenarios (driver, system, conditions)
> - Failure mode scenarios (degraded operation)
>
> **Dimension 2 - Environmental Conditions**:
> - Road type: Highway, urban, rural, construction zone
> - Weather: Clear, rain, snow, fog
> - Lighting: Day, night, dusk/dawn, tunnel
> - Lane markings: Clear, faded, absent, multiple (construction)
> - Road geometry: Straight, gentle curve, sharp curve, merging lanes
>
> **Dimension 3 - Traffic Conditions**:
> - Light traffic (free flow)
> - Heavy traffic (congestion)
> - Adjacent vehicle influence (lane change nearby)
>
> **Dimension 4 - System States**:
> - All sensors functional
> - Camera degraded (dirty, partially obscured)
> - Steering system degraded
> - Multiple systems active (LKA + ACC)
>
> **Example scenarios from matrix**:
>
> | Scenario ID | Mode | Environment | Outcome |
> |-------------|------|-------------|---------|
> | OPS-LKA-001 | Normal operation | Highway, clear, day | Maintain lane center |
> | OPS-LKA-002 | Activation | Highway, clear, day | Enable LKA successfully |
> | OPS-LKA-003 | Lane change | Highway, clear, day | Detect turn signal, allow departure |
> | OPS-LKA-004 | Override | Highway, clear, day | Yield to driver, remain ready |
> | OPS-LKA-005 | Normal operation | Highway, rain, night | Maintain function if camera sees lines |
> | OPS-LKA-006 | Degraded operation | Highway, heavy rain, night | Display 'LKA unavailable' if no lines |
> | OPS-LKA-007 | Failure handling | Highway, camera blocked | Safe transition to inactive state |
> | OPS-LKA-008 | Normal operation | Construction zone, multiple lines | Maintain on rightmost solid line |
>
> **Best practice**: For safety-critical systems (ASIL-B or higher per ISO 26262), we need 30-50 operational scenarios covering all mode combinations and failure cases.
>
> **Each scenario becomes a test case** in Session 8 (Verification & Validation)."

##### Slide 10: Use Case Modeling
**Visual:** UML use case diagram for LKA
**Instructor Script:**
> "We formalize operational scenarios using **Use Case modeling** (from UML - Unified Modeling Language).
>
> **Use Case Diagram for Lane Keep Assist System**:
>
> ```
> Actors:
> - Driver (primary)
> - Camera System (supporting)
> - EPS ECU (supporting)
>
> Use Cases (ovals):
> 1. Activate LKA
> 2. Monitor Lane Position
> 3. Detect Lane Departure
> 4. Apply Steering Correction
> 5. Handle Driver Override
> 6. Deactivate LKA
> 7. Handle System Failure
>
> Relationships:
> - «includes»: Monitor Lane Position «includes» Detect Lane Departure
> - «extends»: Handle Driver Override «extends» Apply Steering Correction
> ```
>
> **Use Case Template - Example**:
>
> **UC-LKA-003: Detect Lane Departure**
>
> **Primary Actor**: LKA System
> **Goal**: Identify when vehicle is drifting from lane center
> **Preconditions**: LKA is active, lane lines visible, speed >60 km/h
> **Trigger**: Camera provides new lane position data (every 50ms)
>
> **Main Success Scenario**:
> 1. System receives lane line positions from camera
> 2. System calculates vehicle lateral offset from lane center
> 3. System calculates lateral velocity (rate of drift)
> 4. System determines if offset exceeds threshold (0.15m)
> 5. **If threshold exceeded**: Trigger 'Apply Steering Correction' use case
> 6. **If within tolerance**: Continue monitoring
>
> **Extensions** (alternative flows):
> - 1a. Camera data invalid → Display warning, deactivate LKA
> - 4a. Lane change signal detected → Suppress departure warning, allow crossing
> - 4b. Driver hands-on-wheel detected → Reduce correction authority
>
> **Postconditions**:
> - Success: Departure detected and correction triggered
> - Failure: System transitions to safe state (inactive, driver notified)
>
> **Special Requirements**:
> - Response time: Detection to correction request ≤100ms (from REQ-LKA-015)
> - False positive rate: <1% (from REQ-LKA-022)
>
> **Notice**: Use cases connect operational scenarios to functional requirements. They're the bridge."

---

#### **Part 2: Capability Gap Analysis** (Slides 11-13, ~8 minutes)

##### Slide 11: What Is Capability Gap Analysis?
**Visual:** Gap analysis framework diagram
**Instructor Script:**
> "Now that we know HOW the system will be used (operational scenarios), we perform **Capability Gap Analysis** to identify what capabilities are required but not yet defined.
>
> **Capability Gap Analysis Process**:
>
> **Step 1: Define Required Capabilities** (from operational scenarios)
> - What must the system be able to do to execute scenarios successfully?
>
> **Step 2: Assess Current/Baseline Capabilities**
> - What can the existing system or platform do?
> - What's inherited from previous generation?
>
> **Step 3: Identify Gaps**
> - Required capabilities NOT in baseline = gaps
> - These gaps drive functional requirements
>
> **Step 4: Prioritize Gaps**
> - Critical (must have for basic operation)
> - Important (needed for full functionality)
> - Desirable (nice-to-have, future enhancement)
>
> **Example: Lane Keep Assist Capability Analysis**
>
> **Required Capabilities** (from operational scenarios OPS-LKA-001 through OPS-LKA-008):
>
> | Capability ID | Capability Description | Source Scenario |
> |---------------|------------------------|-----------------|
> | CAP-LKA-001 | Detect lane line markings in camera image | OPS-LKA-001, all |
> | CAP-LKA-002 | Calculate lateral vehicle position relative to lane center | OPS-LKA-001 |
> | CAP-LKA-003 | Predict vehicle trajectory | OPS-LKA-001 |
> | CAP-LKA-004 | Determine required steering correction | OPS-LKA-001 |
> | CAP-LKA-005 | Command electric power steering | OPS-LKA-001 |
> | CAP-LKA-006 | Detect driver turn signal activation | OPS-LKA-003 |
> | CAP-LKA-007 | Detect driver hands-on-wheel | OPS-LKA-004 |
> | CAP-LKA-008 | Distinguish faded from clear lane markings | OPS-LKA-006 |
> | CAP-LKA-009 | Detect camera sensor degradation | OPS-LKA-007 |
> | CAP-LKA-010 | Transition safely to inactive state | OPS-LKA-007 |
>
> **Baseline Capabilities** (existing in vehicle platform):
> - CAP-BASE-001: Camera can capture forward view (already exists for other ADAS)
> - CAP-BASE-002: EPS can accept external torque commands (from parking assist)
> - CAP-BASE-003: Vehicle speed available on CAN bus
> - CAP-BASE-004: Turn signal status available on CAN bus
>
> **Gap Identification**:
> - CAP-LKA-001 (lane detection): **NEW** - requires computer vision algorithm
> - CAP-LKA-002 (lateral position): **NEW** - requires geometric calculation
> - CAP-LKA-004 (steering correction): **NEW** - requires control algorithm
> - CAP-LKA-005 (steering command): **MODIFY EXISTING** - EPS interface exists but needs LKA-specific logic
>
> These gaps become **functional requirements**."

##### Slide 12: From Gaps to Functional Requirements
**Visual:** Traceability from capabilities to functions
**Instructor Script:**
> "Capability gaps directly generate functional requirements. Let me show the transformation.
>
> **Gap to Functional Requirement Mapping**:
>
> **Capability Gap**: CAP-LKA-001: 'Detect lane line markings in camera image'
> **Derived Functional Requirements**:
> - FR-LKA-VISION-001: 'System shall detect left and right lane boundary markings in camera image'
> - FR-LKA-VISION-002: 'System shall distinguish solid vs dashed lane markings'
> - FR-LKA-VISION-003: 'System shall detect lane markings with confidence level ≥80%'
> - FR-LKA-VISION-004: 'System shall detect lane markings in daylight conditions at distances up to 60m'
> - FR-LKA-VISION-005: 'System shall process camera frames at minimum 20 Hz'
>
> **Capability Gap**: CAP-LKA-004: 'Determine required steering correction'
> **Derived Functional Requirements**:
> - FR-LKA-CTRL-001: 'System shall calculate required steering torque based on lateral offset'
> - FR-LKA-CTRL-002: 'System shall limit steering torque to maximum 3.0 Nm'
> - FR-LKA-CTRL-003: 'System shall apply proportional-derivative control for smooth corrections'
> - FR-LKA-CTRL-004: 'System shall update steering commands at minimum 50 Hz'
>
> **Capability Gap**: CAP-LKA-010: 'Transition safely to inactive state'
> **Derived Functional Requirements**:
> - FR-LKA-SAFE-001: 'System shall deactivate LKA within 200ms upon detection of critical failure'
> - FR-LKA-SAFE-002: 'System shall ramp down steering torque over 500ms (no abrupt release)'
> - FR-LKA-SAFE-003: 'System shall display warning message upon failure-driven deactivation'
> - FR-LKA-SAFE-004: 'System shall log failure event with timestamp and fault code'
>
> **Key insight**: Operational scenarios → Capabilities → Functional requirements → Functions
>
> **This traceability chain** (from Session 4) ensures every function serves an operational need."

##### Slide 13: Capability Maturity Assessment
**Visual:** Capability maturity matrix
**Instructor Script:**
> "For automotive systems, we often assess capability maturity, especially when evolving systems across vehicle generations.
>
> **Capability Maturity Levels**:
>
> **Level 0 - Not Present**: Capability doesn't exist
> **Level 1 - Basic**: Capability exists but limited (e.g., lane detection in ideal conditions only)
> **Level 2 - Functional**: Capability works in most operational scenarios
> **Level 3 - Advanced**: Capability robust across all defined scenarios including edge cases
> **Level 4 - Optimized**: Capability exceeds requirements, includes predictive/adaptive features
>
> **Example: Lane Detection Capability Evolution**:
>
> | Generation | Camera | Algorithm | Maturity | Scenarios Covered |
> |------------|--------|-----------|----------|-------------------|
> | Gen 1 (2015) | VGA, 30fps | Basic Hough transform | Level 1 | Highway, clear day only |
> | Gen 2 (2018) | 720p, 60fps | CNN-based detection | Level 2 | Highway + urban, day/night |
> | Gen 3 (2021) | 1080p, 60fps | Deep learning + sensor fusion | Level 3 | All weather, construction zones |
> | Gen 4 (2024) | 4K, 120fps | Transformer networks, edge processing | Level 4 | Degraded markings, predictive |
>
> **Why this matters**:
> - **Technology roadmapping**: Plan capability evolution across vehicle platforms
> - **Risk assessment**: Lower maturity = higher development risk
> - **Requirements allocation**: Match requirements to realistic capability levels
> - **Make/buy decisions**: Build in-house vs acquire vs partner
>
> **In our LKA example**: If camera lane detection is Level 1 (basic), we cannot support construction zone scenarios (OPS-LKA-008). We must either:
> - Develop Level 3 capability (high cost, schedule risk)
> - Scope down operational scenarios (limit LKA to highways only)
> - Partner with vision technology supplier
>
> This is the trade-space analysis from Session 5 informed by capability gaps."

---

#### **Part 3: Functional Decomposition** (Slides 14-18, ~12 minutes)

##### Slide 14: What Is a Function?
**Visual:** Definition and characteristics of functions
**Instructor Script:**
> "Now we move to the core of functional analysis: **Functions**.
>
> **Definition**: A function is a specific action or task that a system must perform to achieve its purpose. Functions transform inputs to outputs.
>
> **Key characteristics of well-defined functions**:
>
> 1. **Action-oriented** - Expressed as verb + object
>    - Good: 'Detect lane markings'
>    - Bad: 'Lane marking detection module'
>
> 2. **Transformation-based** - Has inputs and outputs
>    - Input: Camera image
>    - Function: Detect lane markings
>    - Output: Lane boundary coordinates
>
> 3. **Technology-agnostic** - Doesn't specify implementation
>    - Good: 'Calculate steering correction'
>    - Bad: 'Run PID controller on lane offset'
>
> 4. **Allocatable** - Can be assigned to hardware, software, or human
>    - 'Monitor system status' → could be software monitoring or driver observation
>
> 5. **Verifiable** - Success can be tested
>    - 'Detect lane markings with ≥90% accuracy' → testable
>
> **Functions vs Requirements vs Design**:
>
> | Aspect | Requirement | Function | Design |
> |--------|-------------|----------|--------|
> | What | System shall... | Transform input to output | Algorithm/component that implements |
> | Example | 'System shall detect lane departure' | 'Detect lane markings' + 'Calculate lateral offset' | CNN algorithm + Kalman filter |
> | Level | What system must do | How system behavior decomposes | How function is implemented |
>
> **Functions sit between requirements and design** - they decompose the 'what' before we commit to 'how'."

##### Slide 15: Functional Hierarchy and Decomposition
**Visual:** Multi-level function tree for LKA
**Instructor Script:**
> "Complex systems require **functional decomposition** - breaking high-level functions into lower-level sub-functions.
>
> **Functional Hierarchy for Lane Keep Assist**:
>
> **Level 0 - System Level Function**:
> ```
> F0.0: Maintain Vehicle in Lane Center
> ```
>
> **Level 1 - Major Functions** (decomposition of F0.0):
> ```
> F1.1: Acquire Environment Data
> F1.2: Determine Vehicle Lane Position
> F1.3: Decide Steering Action
> F1.4: Execute Steering Correction
> F1.5: Monitor System Health
> F1.6: Manage Driver Interface
> ```
>
> **Level 2 - Sub-Functions** (example: decomposition of F1.2):
> ```
> F1.2: Determine Vehicle Lane Position
>   F2.2.1: Detect Lane Boundary Markings
>   F2.2.2: Identify Lane Geometry (straight, curved)
>   F2.2.3: Calculate Lateral Offset from Center
>   F2.2.4: Estimate Lateral Velocity (drift rate)
>   F2.2.5: Predict Future Vehicle Path
> ```
>
> **Level 3 - Detail Functions** (example: decomposition of F2.2.1):
> ```
> F2.2.1: Detect Lane Boundary Markings
>   F3.2.1.1: Preprocess Camera Image (filter, enhance)
>   F3.2.1.2: Apply Edge Detection Algorithm
>   F3.2.1.3: Identify Line Segments
>   F3.2.1.4: Classify Line Type (solid, dashed, yellow, white)
>   F3.2.1.5: Calculate Confidence Score
> ```
>
> **Decomposition Rules**:
>
> 1. **Completeness**: Child functions fully implement parent function
>    - F2.2.1 + F2.2.2 + F2.2.3 + F2.2.4 + F2.2.5 = F1.2
>
> 2. **Independence**: Functions minimize coupling
>    - F2.2.1 can execute independently of F2.2.4 (loose coupling)
>
> 3. **Cohesion**: Each function has single, clear purpose
>    - F2.2.1 only detects markings (doesn't calculate offset or control steering)
>
> 4. **Appropriate level**: Stop decomposing when functions map to clear design elements
>    - F3.2.1.2 'Apply Edge Detection' → maps to specific algorithm (Canny, Sobel)
>
> **Typical automotive system depth**: 3-5 levels
> - Simple functions (door locks): 2-3 levels
> - Complex ADAS (autonomous driving): 5-6 levels"

##### Slide 16: Functional Decomposition Methods
**Visual:** Comparison of decomposition approaches
**Instructor Script:**
> "How do we decompose systematically? Several proven methods:
>
> **Method 1: Process-Based Decomposition**
> - Follow the physical or logical process flow
> - Example: LKA process flow: Sense → Process → Decide → Act → Monitor
> - Good for: Real-time control systems, sequential processes
>
> **Method 2: Object-Based Decomposition**
> - Organize around data objects being manipulated
> - Example: Functions organized around 'Lane Model' object:
>   - Create lane model
>   - Update lane model
>   - Validate lane model
>   - Use lane model for control
> - Good for: Data-intensive systems, MBSE approaches
>
> **Method 3: Capability-Based Decomposition**
> - Organize around required capabilities (from gap analysis)
> - Each capability → top-level function → sub-functions
> - Good for: When capability analysis is comprehensive
>
> **Method 4: Scenario-Based Decomposition**
> - Extract functions from operational scenarios
> - Each scenario step becomes candidate function
> - Good for: User-facing systems, ensuring operational completeness
>
> **Best practice for automotive**: Hybrid approach
> - Use scenario-based to ensure completeness (capture all operational needs)
> - Use process-based for real-time control functions
> - Use object-based for data management functions
>
> **Example: LKA Function Extraction from Scenario OPS-LKA-001**:
>
> Scenario Step → Function:
> 1. 'Driver presses LKA button' → F1.6.1: Receive Driver Command
> 2. 'System checks preconditions' → F1.5.1: Verify Activation Conditions
> 3. 'System displays status' → F1.6.2: Update Driver Display
> 4. 'Camera monitors lane position' → F1.1.1: Acquire Camera Image
> 5. 'System calculates lateral offset' → F2.2.3: Calculate Lateral Offset
> 6. 'System calculates steering correction' → F1.3.1: Compute Steering Torque
> 7. 'System sends torque request' → F1.4.1: Send Steering Command
> 8. 'EPS applies steering' → F1.4.2: Execute Steering Actuation
>
> **Process ensures all scenario steps have corresponding functions.**"

##### Slide 17: Function Allocation - N² Chart
**Visual:** N² (N-squared) diagram showing function interfaces
**Instructor Script:**
> "Once functions are defined, we must understand how they interact. The **N² Chart** (N-squared diagram) shows functional interfaces.
>
> **N² Chart for LKA Functions** (Level 1):
>
> ```
>                 F1.1    F1.2    F1.3    F1.4    F1.5    F1.6
>                Acquire  Determine Decide  Execute Monitor Manage
>                Data     Position  Steering Steering Health  Interface
>
> F1.1: Acquire
>      Data         [F1.1]  →Image
>
> F1.2: Determine   ←Image
>       Position            [F1.2]  →Offset
>                                   →Velocity
>
> F1.3: Decide              ←Offset
>       Steering            ←Velocity
>                                   [F1.3]  →Torque
>                                           Cmd
>
> F1.4: Execute                     ←Torque
>       Steering                    Cmd     [F1.4] →Status
>
> F1.5: Monitor                             ←Status
>       Health                                      [F1.5] →Alerts
>
> F1.6: Manage      ←Driver                        ←Alerts
>       Interface   Cmd                                    [F1.6]
> ```
>
> **How to read N² chart**:
> - **Diagonal boxes**: Functions themselves
> - **Above diagonal**: Outputs from row function to column function
> - **Below diagonal**: Inputs from column function to row function
>
> **Example**:
> - F1.1 → F1.2: Camera image (output from F1.1, input to F1.2)
> - F1.2 → F1.3: Lateral offset and velocity (outputs from F1.2, inputs to F1.3)
>
> **Why this matters**:
> - **Interface definition**: Every arrow becomes an interface requirement
>   - Arrow 'F1.2 → F1.3: Offset' → REQ: 'F1.2 shall provide lateral offset with ±0.01m accuracy'
> - **Coupling analysis**: Functions with many interfaces are tightly coupled (integration risk)
> - **Allocation decisions**: Tightly coupled functions should be allocated to same ECU/processor
> - **Communication load**: Each interface crossing ECU boundary = CAN message (bandwidth consideration)
>
> **Automotive example**: If F1.2 and F1.3 exchange data 50 times/second, they should be in same ECU to avoid saturating CAN bus.
>
> **N² chart feeds directly into architecture refinement** (Session 5) and interface design."

##### Slide 18: Functional Architecture
**Visual:** Functional architecture diagram for LKA
**Instructor Script:**
> "The **Functional Architecture** is the complete representation of:
> - All functions
> - Function hierarchy (decomposition)
> - Function interfaces (N² chart)
> - Function allocation to system elements (physical architecture)
>
> **Functional Architecture Diagram - LKA**:
>
> ```
> [Driver] ←→ [F1.6: Manage Driver Interface]
>                          ↓ activation cmd
>              [F1.5: Monitor System Health] ←→ [F1.1: Acquire Environment Data]
>                          ↓ status                      ↓ camera image
>              [F1.2: Determine Vehicle Lane Position]
>                          ↓ offset, velocity
>              [F1.3: Decide Steering Action]
>                          ↓ torque command
>              [F1.4: Execute Steering Correction]
>                          ↓
>                     [EPS ECU]
> ```
>
> **Key elements**:
> 1. **Function blocks** - Each rectangle is a defined function
> 2. **Data flows** - Arrows show information/energy/material flow
> 3. **External interfaces** - Driver and EPS are outside functional boundary
> 4. **Control flows** - Activation and health monitoring enable/disable functions
>
> **Functional Architecture vs Physical Architecture**:
>
> | Aspect | Functional Architecture | Physical Architecture |
> |--------|------------------------|----------------------|
> | Focus | WHAT system does | WHERE functions execute |
> | Elements | Functions, data flows | ECUs, sensors, networks |
> | Example | 'Detect lane markings' | 'Front camera + LKA ECU software module' |
> | Design stage | Early (before HW/SW split) | Later (after allocation decisions) |
>
> **Allocation Matrix** - Maps functions to physical elements:
>
> | Function | Allocated To | Rationale |
> |----------|--------------|-----------|
> | F1.1: Acquire Data | Front camera + LKA ECU | Camera HW captures, ECU SW preprocesses |
> | F1.2: Determine Position | LKA ECU (SW) | Compute-intensive, needs fast processor |
> | F1.3: Decide Steering | LKA ECU (SW) | Control logic, co-located with F1.2 |
> | F1.4: Execute Steering | EPS ECU (existing) | Reuse existing EPS control |
> | F1.5: Monitor Health | LKA ECU (SW) | Access to internal state needed |
> | F1.6: Manage Interface | Instrument Cluster ECU | Reuse existing display functions |
>
> **This allocation bridges functional and physical architectures.**
>
> In MBSE (Session 3), we create this using SysML Block Definition Diagrams (structure) and Activity Diagrams (behavior)."

---

#### **Part 4: Functional Flow Block Diagrams (FFBD)** (Slides 19-23, ~12 minutes)

##### Slide 19: Introduction to FFBD
**Visual:** FFBD notation and symbols
**Instructor Script:**
> "Now we add the TIME dimension: **Functional Flow Block Diagrams (FFBD)**.
>
> **FFBD Purpose**: Show the sequence and logic of function execution over time.
>
> **Why we need FFBD**:
> - Functional architecture shows WHAT functions exist and HOW they're connected
> - FFBD shows WHEN functions execute and in what ORDER
>
> **FFBD Notation** (standard from NASA/DoD systems engineering):
>
> **Symbols**:
> 1. **Function box** - Rectangle with function ID and name
>    ```
>    ┌─────────────────┐
>    │   1.2           │
>    │ Detect Lane     │
>    │ Markings        │
>    └─────────────────┘
>    ```
>
> 2. **Flow arrow** - Shows sequence (read left-to-right, top-to-bottom)
>    ```
>    Function A ──→ Function B
>    ```
>
> 3. **AND gate** - Parallel execution (functions execute simultaneously)
>    ```
>         ──→ Function A
>    ─┬───
>     └──→ Function B
>    ```
>
> 4. **OR gate** - Conditional branching (one path executes based on condition)
>    ```
>         ──→ Function A (if condition X)
>    ─┬───
>     └──→ Function B (if condition Y)
>    ```
>
> 5. **Iteration loop** - Repeat function(s)
>    ```
>    Function A ──→ [iterate while condition] ──→ Function B
>         ↑─────────────────────────┘
>    ```
>
> 6. **Reference** - Jump to another FFBD (for hierarchical decomposition)
>    ```
>    ┌─────────────────┐
>    │   Ref: FFBD-3   │
>    │ (see detail)    │
>    └─────────────────┘
>    ```
>
> **FFBD Levels**:
> - **Level 0**: Top-level operational flow (mission/scenario level)
> - **Level 1**: System-level function flow
> - **Level 2+**: Detailed sub-function flows
>
> Each level decomposes a function from the level above."

##### Slide 20: FFBD Example - LKA Activation Sequence
**Visual:** Complete FFBD for LKA activation
**Instructor Script:**
> "Let's build an FFBD for the LKA activation scenario (OPS-LKA-002).
>
> **FFBD-LKA-ACT: Lane Keep Assist Activation Flow**
>
> ```
> Start
>   ↓
> ┌─────────────────────┐
> │  1.0                │
> │  Receive Driver     │
> │  Activation Request │
> └─────────────────────┘
>   ↓
> ┌─────────────────────┐
> │  2.0                │
> │  Check System       │
> │  Preconditions      │
> └─────────────────────┘
>   ↓
>   ├─── OR gate (Preconditions met?)
>   │
>   ├─→ YES ──→ ┌─────────────────────┐
>   │           │  3.0                │
>   │           │  Initialize LKA     │
>   │           │  Control Functions  │
>   │           └─────────────────────┘
>   │             ↓
>   │           ┌─────────────────────┐
>   │           │  4.0                │
>   │           │  Display 'LKA       │
>   │           │  Active' Status     │
>   │           └─────────────────────┘
>   │             ↓
>   │           ┌─────────────────────┐
>   │           │  5.0                │
>   │           │  Enter LKA Active   │
>   │           │  Mode               │
>   │           └─────────────────────┘
>   │             ↓
>   │           End (Success)
>   │
>   └─→ NO ──→  ┌─────────────────────┐
>               │  6.0                │
>               │  Display 'LKA       │
>               │  Unavailable' Msg   │
>               └─────────────────────┘
>                 ↓
>               ┌─────────────────────┐
>               │  7.0                │
>               │  Log Failed         │
>               │  Activation Event   │
>               └─────────────────────┘
>                 ↓
>               End (Failure)
> ```
>
> **FFBD Details**:
>
> **Function 2.0: Check System Preconditions** (decomposes to FFBD-LKA-ACT-2):
> ```
> 2.1: Read Vehicle Speed ──→ 2.2: Verify Speed >60 km/h
>                               ↓
> 2.3: Check Lane Lines Detected
>                               ↓
> 2.4: Verify Steering System Available
>                               ↓
> 2.5: Check No Critical Faults
>                               ↓
> 2.6: Return Precondition Status (Pass/Fail)
> ```
>
> **Why this matters**:
> - **Unambiguous sequence**: No confusion about order of operations
> - **Complete logic**: All paths covered (success and failure)
> - **Timing implications**: Sequential boxes = time delay, AND gates = parallel (faster)
> - **Testability**: Each path becomes test case (e.g., test activation with speed <60 km/h → expect failure path)
>
> **This FFBD directly translates to**:
> - Software state machines (in design phase)
> - Test sequences (in V&V phase)
> - Timeline analysis (next slides)"

##### Slide 21: FFBD Example - LKA Normal Operation (Continuous Loop)
**Visual:** FFBD showing continuous control loop
**Instructor Script:**
> "Now let's model the continuous operation of LKA using an iterative FFBD.
>
> **FFBD-LKA-OPS: Lane Keep Assist Operation Loop** (executes while LKA active)
>
> ```
> Entry (LKA Active Mode)
>   ↓
> ┌─────────────────────┐
> │  1.0                │ ←────────────────────┐
> │  Acquire Camera     │                      │
> │  Frame              │                      │
> └─────────────────────┘                      │
>   ↓                                          │
> ┌─────────────────────┐                      │
> │  2.0                │                      │
> │  Detect Lane        │                      │
> │  Boundaries         │                      │
> └─────────────────────┘                      │
>   ↓                                          │
>   ├─── OR gate (Lane lines detected?)       │
>   │                                          │
>   ├─→ YES ──→ ┌─────────────────────┐       │
>   │           │  3.0                │       │
>   │           │  Calculate Lateral  │       │
>   │           │  Offset & Velocity  │       │
>   │           └─────────────────────┘       │
>   │             ↓                            │
>   │             ├─── OR gate (Correction needed?) │
>   │             │                            │
>   │             ├─→ YES ──→ ┌──────────────┐│
>   │             │           │  4.0         ││
>   │             │           │  Calculate   ││
>   │             │           │  Steering    ││
>   │             │           │  Torque      ││
>   │             │           └──────────────┘│
>   │             │             ↓             │
>   │             │           ┌──────────────┐│
>   │             │           │  5.0         ││
>   │             │           │  Send Torque ││
>   │             │           │  Command to  ││
>   │             │           │  EPS         ││
>   │             │           └──────────────┘│
>   │             │             ↓             │
>   │             └─→ NO  ────→ [merge]       │
>   │                           ↓             │
>   │                         ┌──────────────┐│
>   │                         │  6.0         ││
>   │                         │  Monitor for ││
>   │                         │  Deactivation││
>   │                         └──────────────┘│
>   │                           ↓             │
>   │                           ├─ OR gate    │
>   │                           │             │
>   │                           ├─→ Continue: Loop back (iterate)
>   │                           │
>   │                           └─→ Deactivate: Exit to FFBD-LKA-DEACT
>   │
>   └─→ NO (lane loss) ──→ ┌─────────────────┐
>                          │  7.0            │
>                          │  Enter Degraded │
>                          │  Mode / Warn    │
>                          │  Driver         │
>                          └─────────────────┘
>                            ↓
>                          ┌─────────────────┐
>                          │  8.0            │
>                          │  Attempt Lane   │
>                          │  Re-acquisition │
>                          └─────────────────┘
>                            ↓
>                            Loop back to 1.0 or Exit if persistent failure
> ```
>
> **Key features of this FFBD**:
>
> 1. **Continuous loop**: Functions 1.0-6.0 repeat cyclically (every 50ms in real implementation)
>
> 2. **Conditional branching**:
>    - Lane detected? (YES → normal operation, NO → degraded mode)
>    - Correction needed? (YES → apply steering, NO → monitor only)
>
> 3. **Multiple exit conditions** (Function 6.0 checks):
>    - Driver presses cancel → Exit to deactivation flow
>    - Driver overrides steering → Exit to override handling
>    - System fault detected → Exit to fault management
>    - Continue normal operation → Loop back to 1.0
>
> 4. **Timing implications**:
>    - Total loop time: 1.0 (10ms) + 2.0 (20ms) + 3.0 (5ms) + 4.0 (8ms) + 5.0 (2ms) + 6.0 (5ms) = 50ms
>    - Loop frequency: 20 Hz (meets requirement NFR-LKA-002: minimum 20 Hz update rate)
>
> **This FFBD becomes the basis for**:
> - Software task scheduling (real-time operating system)
> - Timing analysis (worst-case execution time)
> - Safety analysis (what if function 2.0 fails?)"

##### Slide 22: FFBD for Concurrent Functions - AND Gate Example
**Visual:** FFBD with parallel execution paths
**Instructor Script:**
> "Automotive systems often have concurrent operations. FFBD uses **AND gates** to show parallel execution.
>
> **FFBD-LKA-INIT: LKA Initialization with Parallel Tasks**
>
> ```
> Start Initialization
>   ↓
> ┌─────────────────────┐
> │  1.0                │
> │  Receive Activation │
> │  Command            │
> └─────────────────────┘
>   ↓
> ┌─────────────────────┐
> │  2.0                │
> │  Verify             │
> │  Preconditions      │
> └─────────────────────┘
>   ↓
>   ─┬── AND gate (Parallel execution begins)
>    │
>    ├──→ ┌─────────────────────┐
>    │    │  3.1                │
>    │    │  Initialize Vision  │
>    │    │  Algorithm          │
>    │    └─────────────────────┘
>    │
>    ├──→ ┌─────────────────────┐
>    │    │  3.2                │
>    │    │  Initialize Control │
>    │    │  Algorithm          │
>    │    └─────────────────────┘
>    │
>    └──→ ┌─────────────────────┐
>         │  3.3                │
>         │  Initialize Driver  │
>         │  Interface          │
>         └─────────────────────┘
>    ↓
>    ─┴── AND gate (Synchronization - wait for all to complete)
>    ↓
> ┌─────────────────────┐
> │  4.0                │
> │  Verify All         │
> │  Subsystems Ready   │
> └─────────────────────┘
>   ↓
> ┌─────────────────────┐
> │  5.0                │
> │  Transition to      │
> │  Active State       │
> └─────────────────────┘
>   ↓
> End
> ```
>
> **AND gate semantics**:
> - **Fork (top AND)**: All branches execute simultaneously
>   - 3.1, 3.2, 3.3 start at the same time
> - **Join (bottom AND)**: Wait for ALL branches to complete before proceeding
>   - Function 4.0 doesn't start until 3.1 AND 3.2 AND 3.3 are done
>
> **Why parallel execution**:
> - **Faster initialization**: Serial execution would take 50ms + 30ms + 20ms = 100ms
> - **Parallel execution**: Takes max(50ms, 30ms, 20ms) = 50ms (2x faster)
>
> **Design implications**:
> - Functions 3.1, 3.2, 3.3 must be **independent** (no data dependencies)
> - Requires multi-threading or multi-core processor
> - Synchronization needed at join (barrier/semaphore in software)
>
> **Real automotive example**:
> During vehicle startup, multiple ECUs initialize in parallel:
> - Powertrain ECU initializes engine control
> - Chassis ECU initializes steering/braking
> - Body ECU initializes lighting/wipers
> All must complete before 'Vehicle Ready' state.
>
> **FFBD makes parallelism explicit** so architects can:
> - Estimate total execution time
> - Identify synchronization points
> - Allocate functions to processors"

##### Slide 23: Hierarchical FFBD Decomposition
**Visual:** Multi-level FFBD structure
**Instructor Script:**
> "Complex systems require **hierarchical FFBDs** - high-level flows decompose into detailed flows.
>
> **Three-Level FFBD Example**:
>
> **Level 0: Mission-Level FFBD** (OPS-LKA-001: Complete Highway Drive with LKA)
> ```
> 1.0: Enter Highway
>   ↓
> 2.0: Activate LKA (Ref: FFBD-LKA-ACT, Level 1)
>   ↓
> 3.0: Maintain Lane (Ref: FFBD-LKA-OPS, Level 1)
>   ↓
> 4.0: Handle Lane Change (Ref: FFBD-LKA-LC, Level 1)
>   ↓
> 5.0: Deactivate LKA (Ref: FFBD-LKA-DEACT, Level 1)
>   ↓
> 6.0: Exit Highway
> ```
>
> **Level 1: System-Level FFBD** (FFBD-LKA-OPS: Maintain Lane)
> ```
> 1.0: Acquire Camera Frame
>   ↓
> 2.0: Process Image (Ref: FFBD-LKA-OPS-2, Level 2)
>   ↓
> 3.0: Calculate Offset
>   ↓
> 4.0: Determine Steering Torque
>   ↓
> 5.0: Send Command to EPS
>   ↓
> Loop back to 1.0
> ```
>
> **Level 2: Sub-Function FFBD** (FFBD-LKA-OPS-2: Process Image)
> ```
> 2.1: Preprocess Image (denoise, enhance)
>   ↓
> 2.2: Apply Edge Detection
>   ↓
> 2.3: Identify Line Segments
>   ↓
> 2.4: Fit Lane Model (polynomial curve fit)
>   ↓
> 2.5: Validate Lane Model (confidence check)
>   ↓
> 2.6: Output Lane Boundaries
> ```
>
> **Decomposition rules**:
> 1. Each function in Level N can be expanded to full FFBD at Level N+1
> 2. 'Ref: FFBD-X' notation indicates link to detailed diagram
> 3. Inputs/outputs must match between levels
>
> **When to create new FFBD level**:
> - Function is complex (>10 sub-steps)
> - Different team responsible for implementation
> - Different timing/criticality domain
> - Safety-critical function requiring detailed analysis
>
> **Automotive practice**:
> - **Level 0**: Vehicle-level scenarios (used by system architects)
> - **Level 1**: ECU-level functions (used by software architects)
> - **Level 2**: Software module functions (used by developers)
> - **Level 3+**: Algorithm details (used by algorithm engineers)
>
> **Traceability**: Each FFBD level traces to:
> - Requirements (what must be accomplished)
> - Test cases (validation of flow)
> - Design elements (implementation)
>
> In MBSE tools (Session 3), these are Activity Diagrams in SysML, automatically traceable to requirements."

---

#### **Part 5: Requirements Allocation and Timeline Analysis** (Slides 24-27, ~8 minutes)

##### Slide 24: Requirements Allocation to Functions
**Visual:** Allocation matrix
**Instructor Script:**
> "Now we close the loop: **Allocating requirements to functions**.
>
> Remember Session 4: We defined requirements (WHAT system shall do).
> Today: We defined functions (operational decomposition of behavior).
> **Now: We map requirements → functions to ensure complete coverage.**
>
> **Requirements Allocation Matrix (RAM)**:
>
> | Requirement ID | Requirement Statement | Allocated Function(s) | Verification Method |
> |----------------|----------------------|----------------------|---------------------|
> | REQ-LKA-001 | System shall detect lane departure | F2.2.1: Detect Lane Markings<br>F2.2.3: Calculate Lateral Offset | Test (camera test rig) |
> | REQ-LKA-002 | System shall operate at 60-180 km/h | F1.5.1: Verify Activation Conditions | Test (vehicle speed sweep) |
> | REQ-LKA-003 | System shall apply steering correction within 100ms of detecting departure | F1.2: Determine Position<br>F1.3: Decide Steering<br>F1.4: Execute Steering | Test (timing analysis) |
> | REQ-LKA-015 | Detection to correction latency ≤100ms | F2.2.1 + F2.2.3 + F1.3.1 + F1.4.1 | Analysis (WCET) |
> | REQ-LKA-022 | False positive rate <1% | F2.2.1: Detect Lane Markings<br>F2.2.5: Validate Detection | Test (statistical testing) |
> | NFR-LKA-001 | Control loop rate ≥20 Hz | FFBD-LKA-OPS (entire loop) | Analysis (timing) |
> | NFR-LKA-SAFE-001 | Deactivate within 200ms upon failure | F1.5.2: Detect Failure<br>F1.5.3: Transition to Safe State | Test (fault injection) |
>
> **Allocation ensures**:
> 1. **Completeness**: Every requirement is implemented by at least one function
>    - Orphan requirement (no function) = gap in functional design
>
> 2. **Traceability**: Bidirectional links
>    - Requirement → Function (forward)
>    - Function → Requirement (backward - why does this function exist?)
>
> 3. **Verification planning**: Each requirement-function pair indicates how to verify
>    - REQ-LKA-001 + F2.2.1 → Test with camera images, measure detection accuracy
>
> 4. **Change impact**: If requirement changes, know which functions affected
>    - Change REQ-LKA-015 from 100ms to 50ms → impacts F2.2.1, F1.3.1, F1.4.1 timing
>
> **Allocation types**:
> - **1:1** - One requirement → one function (simple)
> - **1:N** - One requirement → multiple functions (requirement decomposed across functions)
> - **N:1** - Multiple requirements → one function (function satisfies multiple needs)
>
> **Example of 1:N allocation**:
> - REQ-LKA-003 'apply correction within 100ms' allocates to:
>   - F1.2 (must complete position determination in ≤40ms)
>   - F1.3 (must complete steering decision in ≤30ms)
>   - F1.4 (must complete actuation command in ≤30ms)
>   - Total budget: 40+30+30 = 100ms (meets requirement)
>
> This is **derived requirements** - allocating parent requirement creates child requirements for each function."

##### Slide 25: Timeline Analysis - Validating Temporal Feasibility
**Visual:** Timeline diagram showing function execution
**Instructor Script:**
> "**Timeline analysis** validates that functional flows can execute within timing requirements.
>
> **Timeline Diagram for FFBD-LKA-OPS** (one control cycle):
>
> ```
> Time (ms): 0    10   20   30   40   50
>            |----|----|----|----|----|
>
> F1.1: Acquire     [####]
> Camera Frame
>
> F2.2.1: Detect         [##########]
> Lane Markings
>
> F2.2.3: Calculate                [##]
> Lateral Offset
>
> F1.3.1: Compute                    [####]
> Steering Torque
>
> F1.4.1: Send                           [#]
> Steering Command
>
> Total Cycle Time: 50ms (meets 20 Hz requirement)
> ```
>
> **Timeline analysis reveals**:
>
> 1. **Critical path**: F1.1 → F2.2.1 → F2.2.3 → F1.3.1 → F1.4.1 (50ms total)
>    - Longest sequential path through FFBD
>    - Determines minimum cycle time
>
> 2. **Slack time**: Time available beyond critical path
>    - Total budget: 50ms (for 20 Hz)
>    - Critical path: 47ms
>    - Slack: 3ms (6% margin)
>    - **Risk**: Low slack = timing fragile, any delay causes violation
>
> 3. **Parallelization opportunities**:
>    - If F1.5 (Monitor Health) takes 15ms, running it serially would exceed 50ms
>    - Solution: Run F1.5 in parallel with F2.2.1 (both read-only operations)
>
> 4. **Worst-case execution time (WCET)**:
>    - Timeline shows **nominal times**
>    - Must analyze **worst-case** (complex scene, maximum compute)
>    - Example: F2.2.1 nominal 18ms, worst-case 25ms
>    - Worst-case total: 54ms → **VIOLATES 50ms requirement**
>    - **Solution**: Optimize algorithm OR relax requirement OR add faster processor
>
> **Timing requirement decomposition example**:
>
> **System requirement**: REQ-LKA-015: 'Detection to correction latency ≤100ms'
>
> **Timeline allocation**:
> - Detection (F2.2.1): allocated ≤40ms
> - Processing (F2.2.3): allocated ≤20ms
> - Decision (F1.3.1): allocated ≤25ms
> - Actuation (F1.4.1): allocated ≤10ms
> - Total: 95ms (5ms margin)
>
> **Derived requirements** (allocated to functions):
> - REQ-LKA-015.1: 'F2.2.1 shall detect lane markings with WCET ≤40ms'
> - REQ-LKA-015.2: 'F2.2.3 shall calculate offset with WCET ≤20ms'
> - etc.
>
> **Tools for timeline analysis**:
> - Spreadsheet (simple systems)
> - Timing analysis tools (MATLAB/Simulink, TargetLink)
> - RTOS analysis tools (measure actual execution times)
> - Model checking tools (formal verification of timing)"

##### Slide 26: Functional Analysis Integration - Bringing It All Together
**Visual:** Complete functional analysis workflow
**Instructor Script:**
> "Let's see how all the pieces of functional analysis integrate into a complete workflow.
>
> **Integrated Functional Analysis Process**:
>
> **Step 1: Operational Scenarios** (Part 1)
> - Define how system is used: OPS-LKA-001 through OPS-LKA-008
> - Capture all operational modes, environments, failure cases
> - **Output**: Operational scenario set
>
> **Step 2: Capability Gap Analysis** (Part 2)
> - Identify required capabilities from scenarios
> - Compare to baseline/existing capabilities
> - **Output**: Capability gaps → functional requirements
>
> **Step 3: Functional Decomposition** (Part 3)
> - Decompose system-level function into sub-functions
> - Create function hierarchy (3-4 levels deep)
> - Define function interfaces (N² chart)
> - **Output**: Functional architecture
>
> **Step 4: Functional Flow Modeling** (Part 4)
> - Develop FFBDs for each operational scenario
> - Model sequential, parallel, and conditional flows
> - Create hierarchical FFBD set
> - **Output**: Complete FFBD set
>
> **Step 5: Requirements Allocation** (Part 5)
> - Map system requirements to functions
> - Derive function-level requirements
> - **Output**: Requirements Allocation Matrix (RAM)
>
> **Step 6: Timeline Analysis** (Part 5)
> - Validate timing feasibility
> - Identify critical paths and bottlenecks
> - Allocate timing budgets to functions
> - **Output**: Validated functional timing model
>
> **Step 7: Functional to Physical Allocation** (links to Session 5)
> - Allocate functions to hardware (ECUs, sensors)
> - Allocate functions to software (modules, tasks)
> - Define implementation architecture
> - **Output**: Physical architecture with function allocation
>
> **Traceability chain**:
> ```
> Operational Scenarios → Capabilities → Functional Requirements →
> Functions → FFBDs → Design Elements → Implementation → Tests
> ```
>
> **Deliverables from functional analysis**:
> 1. Operational scenario document (20-50 scenarios for automotive ADAS)
> 2. Capability gap analysis report
> 3. Functional architecture diagram
> 4. Function hierarchy (decomposition tree)
> 5. N² chart (function interfaces)
> 6. FFBD set (10-20 diagrams, hierarchical)
> 7. Requirements Allocation Matrix (RAM)
> 8. Timeline analysis report
> 9. Function-to-physical allocation matrix
>
> **In MBSE** (Session 3):
> - Operational scenarios → Use Cases (SysML)
> - Functions → Activities (SysML Activity Diagrams)
> - FFBDs → Activity Diagrams with control/data flows
> - Allocation → Allocation Matrices in model
> - **Advantage**: All elements linked in single model, automatic consistency checking"

##### Slide 27: Real-World Example - Adaptive Cruise Control Functional Analysis
**Visual:** ACC functional analysis summary
**Instructor Script:**
> "Let me show you a complete real-world example: **Adaptive Cruise Control (ACC) functional analysis**.
>
> **System Context** (from Session 5 architecture):
> - Forward radar sensor (77 GHz, 150m range)
> - ACC ECU
> - Interfaces: Engine ECU, Brake ECU, Driver Interface, CAN bus
>
> **Operational Scenarios** (sample from 30 total):
> - OPS-ACC-001: Set speed and maintain (no lead vehicle)
> - OPS-ACC-002: Detect lead vehicle and adjust speed
> - OPS-ACC-003: Follow lead vehicle maintaining time gap
> - OPS-ACC-004: Lead vehicle decelerates - ACC brakes
> - OPS-ACC-005: Lead vehicle changes lane - ACC accelerates to set speed
> - OPS-ACC-006: Vehicle cuts in front - ACC emergency deceleration
> - OPS-ACC-015: Radar sensor degraded (rain, dirt) - fallback behavior
>
> **Capability Gaps** → **Functional Requirements**:
> - Gap: Detect and track lead vehicle → FR-ACC-RADAR-001: 'Detect vehicles up to 150m'
> - Gap: Determine safe following distance → FR-ACC-CTRL-005: 'Maintain 1.0-2.5s time gap'
> - Gap: Coordinate throttle and braking → FR-ACC-ACT-010: 'Request engine torque or brake pressure'
>
> **Top-Level Functions** (Level 1):
> 1. F1.1: Acquire Sensor Data (radar, vehicle speed, driver inputs)
> 2. F1.2: Detect and Track Vehicles (object detection, tracking)
> 3. F1.3: Determine Desired Speed (based on set speed, lead vehicle, time gap)
> 4. F1.4: Calculate Acceleration/Deceleration (control algorithm)
> 5. F1.5: Execute Speed Control (throttle/brake commands)
> 6. F1.6: Monitor System Health (sensor validation, fault detection)
> 7. F1.7: Manage Driver Interface (display, alerts)
>
> **Sample FFBD**: FFBD-ACC-FOLLOW (Following Lead Vehicle)
> ```
> 1.0: Acquire Radar Data (every 100ms)
>   ↓
> 2.0: Detect Objects
>   ↓
> 3.0: Track Lead Vehicle
>   ↓
> 4.0: Measure Distance and Relative Velocity
>   ↓
> 5.0: Calculate Desired Time Gap (1.0-2.5s based on driver setting)
>   ↓
> 6.0: Compare Actual vs Desired Gap
>   ↓
>   ├─ OR: Gap too small (collision risk)
>   │   ↓
>   │   7.1: Calculate Required Deceleration
>   │   ↓
>   │   7.2: Request Brake Pressure
>   │
>   ├─ OR: Gap acceptable
>   │   ↓
>   │   8.1: Maintain Current Speed
>   │
>   └─ OR: Gap too large
>       ↓
>       9.1: Calculate Acceleration
>       ↓
>       9.2: Request Engine Torque
>   ↓
> 10.0: Monitor for Lead Vehicle Lane Change
>   ↓
> Loop back to 1.0 (continuous 10 Hz control)
> ```
>
> **Requirements Allocation** (sample):
> - REQ-ACC-001: 'Maintain set speed ±2 km/h' → F1.3, F1.4, F1.5
> - REQ-ACC-010: 'Detect lead vehicle up to 150m' → F1.2 (sub-function F2.2.1)
> - REQ-ACC-015: 'Control loop rate ≥10 Hz' → FFBD-ACC-FOLLOW entire loop
> - REQ-ACC-SAFE-001: 'Maximum deceleration 3.5 m/s²' → F1.4.2, F1.5.1
>
> **Timeline Analysis**:
> - Control cycle budget: 100ms (for 10 Hz)
> - F1.1 (radar data): 10ms
> - F1.2 (object detection): 40ms
> - F1.3 (desired speed): 15ms
> - F1.4 (control calculation): 20ms
> - F1.5 (actuation command): 5ms
> - Total: 90ms (10ms slack, 10% margin) ✓
>
> **Function Allocation to Physical Elements**:
> - F1.1: Radar sensor (HW) + ACC ECU (SW preprocessing)
> - F1.2: ACC ECU (SW - object detection algorithm)
> - F1.3, F1.4: ACC ECU (SW - control logic)
> - F1.5: Engine ECU + Brake ECU (existing functions, ACC requests)
> - F1.6: ACC ECU (SW diagnostics)
> - F1.7: Instrument Cluster ECU (reuse existing display functions)
>
> **Result**: Complete functional model ready for detailed design (software architecture, algorithm development, integration planning)"

---

### **CLIMAX: The Power of Systematic Functional Analysis** (Slides 28, ~5 minutes)

#### Slide 28: Case Study - What Happens Without Functional Analysis
**Visual:** Tesla Autopilot failure analysis
**Instructor Script:**
> "Let me show you what happens when functional analysis is incomplete or skipped.
>
> **Case Study: Tesla Autopilot Fatal Crash - May 2016, Florida**
>
> **Background**:
> - Tesla Model S with Autopilot engaged
> - Tractor-trailer crossing highway perpendicular to vehicle path
> - White truck against bright sky
> - Autopilot failed to detect truck, did not brake
> - Fatal collision
>
> **System architecture** (structural view - was well designed):
> - Forward camera (Mobileye EyeQ3)
> - Forward radar (Bosch)
> - Sensor fusion ECU
> - Automatic emergency braking (AEB) capability
> - Components worked individually
>
> **Functional analysis gaps** (behavioral view - incomplete):
>
> **Missing Operational Scenario**:
> - OPS-AP-XXX: 'Crossing traffic (perpendicular vehicle)'
> - **Why missing**: Focus was on highway scenarios (same-direction traffic, lead vehicle following)
> - **Impact**: Functional behavior for crossing traffic never defined
>
> **Incomplete Capability Analysis**:
> - Camera: Can detect vehicles in image? YES
> - Radar: Can detect metal objects? YES
> - **Gap not identified**: 'Distinguish truck side from overhead sign'
> - Camera confused white truck with bright sky (low contrast)
> - Radar detected truck but classified as 'overhead sign' (algorithm assumption: large radar returns above road = bridge/sign, ignore to reduce false positives)
>
> **Missing Functional Flow**:
> - **Should have been**: FFBD-AP-CROSSING
>   ```
>   1.0: Detect crossing object (camera + radar fusion)
>     ↓
>   2.0: Classify object (car, truck, pedestrian, stationary)
>     ↓
>   3.0: Predict trajectory (is it entering our path?)
>     ↓
>   4.0: Calculate collision risk
>     ↓
>   5.0: If risk >threshold: Emergency brake
>   ```
> - **What was missing**: Steps 2.0 and 3.0 incomplete for perpendicular large vehicles
>
> **Requirements allocation gap**:
> - REQ-AP-SAFE-001 existed: 'System shall detect obstacles and brake'
> - **Missing derived requirement**: 'System shall detect crossing vehicles with perpendicular approach vector'
> - **Impact**: Requirement existed at system level, but no function was allocated this specific scenario
>
> **What proper functional analysis would have revealed**:
>
> 1. **Operational scenario analysis** would have identified 'crossing traffic' as critical scenario
>    - Common on non-controlled access highways
>    - High severity (T-bone collision potential)
>
> 2. **Capability gap analysis** would have identified:
>    - 'Detect large perpendicular vehicles' capability gap
>    - Sensor fusion needed (camera alone insufficient, radar alone insufficient)
>
> 3. **FFBD development** would have forced definition of:
>    - Detection logic for perpendicular objects
>    - Sensor fusion algorithm (combine camera + radar for disambiguation)
>    - Decision logic for braking
>
> 4. **Timeline analysis** would have shown:
>    - Time available from detection to collision: ~3 seconds at highway speed
>    - Required detection range: 100m minimum
>    - Processing budget: detection + decision <500ms
>
> 5. **Requirements allocation** would have created:
>    - FR-AP-DETECT-015: 'System shall detect vehicles approaching perpendicular to vehicle path'
>    - FR-AP-FUSION-003: 'System shall fuse camera and radar data to disambiguate large perpendicular objects'
>
> **Lessons learned** (NTSB investigation findings):
> - Operational scenarios must include ALL realistic use cases, not just common ones
> - Edge cases (crossing traffic on divided highway) are not 'edge' - they're CRITICAL
> - Functional analysis forces systematic thinking through scenarios
> - Skipping functional analysis creates unknown unknowns
>
> **Post-accident changes**:
> - Tesla updated Autopilot with 'crossing traffic' scenario
> - Added radar processing for perpendicular vehicles
> - Enhanced sensor fusion algorithms
> - **All changes that functional analysis would have identified BEFORE deployment**
>
> This tragedy cost a life. Proper functional analysis costs time and effort. Choose wisely."

---

### **RESOLUTION: Applying Functional Analysis in Practice** (Slides 29-30, ~5 minutes + Q&A)

#### Slide 29: Key Takeaways and Best Practices
**Visual:** Summary infographic
**Instructor Script:**
> "Let's consolidate what you've learned today about operational and functional analysis.
>
> **Core Concepts**:
>
> **1. Operational Scenarios**
> - Define HOW system will be used
> - Cover all modes, environments, failure cases
> - Use case modeling formalizes scenarios
> - 20-50 scenarios typical for automotive ADAS
>
> **2. Capability Gap Analysis**
> - Required capabilities (from scenarios) vs existing capabilities
> - Gaps drive functional requirements
> - Maturity assessment guides technology decisions
>
> **3. Functional Decomposition**
> - Break system behavior into discrete functions
> - 3-4 levels typical (system → major → sub → detail)
> - Functions are technology-agnostic transformations
> - N² chart captures function interfaces
>
> **4. Functional Flow Block Diagrams (FFBD)**
> - Add temporal dimension - WHEN functions execute
> - Show sequence, parallelism, branching, iteration
> - Hierarchical (scenarios → system → sub-functions)
> - Directly maps to software design (state machines, tasks)
>
> **5. Requirements Allocation**
> - Map system requirements → functions
> - Derive function-level requirements
> - Ensures complete coverage and traceability
> - Requirements Allocation Matrix (RAM) is key deliverable
>
> **6. Timeline Analysis**
> - Validate temporal feasibility
> - Critical path analysis
> - Worst-case execution time (WCET)
> - Timing budget allocation
>
> **The Value Proposition**:
> - **Completeness**: Systematic scenarios ensure nothing missed
> - **Traceability**: Clear chain from scenarios → functions → design → tests
> - **Communication**: FFBDs communicate behavior unambiguously
> - **Early risk identification**: Timeline/capability gaps found early
> - **Safety**: Critical for safety-critical systems (ISO 26262 requires functional analysis)
>
> **Best Practices**:
>
> ✓ **Start with operational scenarios** - Don't jump to functions
> ✓ **Use multiple sources** - User studies, field data, standards, failure analysis
> ✓ **Be systematic** - Matrix of modes × environments × states
> ✓ **Include failure modes** - Degraded operation scenarios are critical
> ✓ **Iterate** - Functional analysis is not one-and-done, refine as understanding grows
> ✓ **Use standard notation** - FFBD symbols, use case templates (aids communication)
> ✓ **Maintain traceability** - Every function traces to scenario and requirement
> ✓ **Validate timing early** - Don't wait for implementation to discover infeasibility
> ✓ **Tool support** - MBSE tools (Cameo, Enterprise Architect) for large systems
> ✓ **Review with stakeholders** - Scenarios and FFBDs are understandable to non-engineers
>
> **Common Pitfalls to Avoid**:
> ❌ Skipping operational scenarios (jumping to functions based on intuition)
> ❌ Incomplete scenario coverage (missing edge cases)
> ❌ Functions that are really design solutions (implementation bias)
> ❌ Missing failure mode scenarios (only modeling happy path)
> ❌ FFBDs without timing analysis (looks good on paper, doesn't work in practice)
> ❌ No traceability to requirements (orphan functions)
> ❌ Functional analysis separate from architecture (creates disconnect)"

#### Slide 30: Connection to Next Sessions and Practice Exercise
**Visual:** Learning journey continuation
**Instructor Script:**
> "Let's connect today's learning to the broader systems engineering process.
>
> **Today (Session 7)**: Operational and Functional Analysis
> - We learned to model system BEHAVIOR
> - We bridged requirements and design through functions
> - We validated feasibility through timeline analysis
>
> **Connection to Previous Sessions**:
>
> **Session 4 (Requirements Engineering)**:
> - Defined WHAT system shall do
> - Today: Decomposed requirements into operational functions
> - **Link**: Requirements Allocation Matrix (RAM) connects Session 4 to Session 7
>
> **Session 5 (System Architecture)**:
> - Defined system STRUCTURE (components, interfaces)
> - Today: Defined system BEHAVIOR (functions, flows)
> - **Link**: Function allocation to physical architecture (structure + behavior = complete model)
>
> **What Comes Next**:
>
> **Session 8 (Integration, Verification & Validation)**:
> - Right side of V-Model
> - How do we verify functions work? (Function-level testing)
> - How do we validate operational scenarios? (Scenario-based testing)
> - **Link**: FFBDs become test sequences, operational scenarios become validation test cases
>
> **Session 9 (Project and Risk Management)**:
> - Functional analysis informs work breakdown structure (WBS)
> - Each function = work package
> - Timeline analysis identifies schedule risks
>
> **Session 12 (Functional Safety - ISO 26262)**:
> - Functional analysis is REQUIRED by ISO 26262
> - Safety functions identified through HARA (Hazard Analysis and Risk Assessment)
> - FFBDs used to analyze failure propagation
>
> **The Thread**:
> - Session 4: Requirements (what)
> - Session 5: Architecture (structure)
> - Session 7: Functional Analysis (behavior) ← TODAY
> - Session 8: V&V (verification that we built it right, validation that we built the right thing)
>
> **In MBSE** (Session 3):
> - All of today's artifacts are SysML diagrams
> - Use Case Diagrams (scenarios)
> - Activity Diagrams (FFBDs)
> - Allocation Matrices (function to component)
> - **Single integrated model**, not separate documents
>
> ---
>
> **Practice Exercise** (Due before Session 8):
>
> You are the systems engineer for an **Automatic Emergency Braking (AEB)** system.
>
> **Given** (from previous sessions):
> - System architecture (Session 5): Forward radar, camera, AEB ECU, brake ECU
> - System requirements (Session 4): 15 requirements including detection, decision, actuation
>
> **Your Task**:
>
> **Part 1: Operational Scenario Development** (30%)
> - Define 6 operational scenarios for AEB covering:
>   - Normal operation (stationary vehicle ahead, moving vehicle ahead)
>   - Edge cases (crossing pedestrian, vehicle cutting in)
>   - Failure modes (sensor degraded, driver override)
> - Use operational scenario template from Slide 8
>
> **Part 2: Functional Decomposition** (30%)
> - Develop functional hierarchy (3 levels minimum)
>   - Level 1: Top-level functions (5-7 functions)
>   - Level 2: Decompose at least 2 Level 1 functions
>   - Level 3: Decompose at least 1 Level 2 function
> - Create N² chart for Level 1 functions showing interfaces
>
> **Part 3: Functional Flow Block Diagram** (25%)
> - Develop FFBD for one operational scenario (your choice)
> - Include sequential, conditional (OR), and parallel (AND) flows
> - Use standard FFBD notation from Slide 19
> - Annotate with estimated timing for each function
>
> **Part 4: Requirements Allocation** (15%)
> - Create Requirements Allocation Matrix (RAM)
> - Map at least 10 system requirements to your functions
> - Identify verification method for each
>
> **Deliverables**:
> - 6 operational scenarios (1 page)
> - Functional hierarchy diagram (1 page)
> - N² chart (1 page)
> - One detailed FFBD (1 page)
> - Requirements Allocation Matrix (1 page)
> - **Total: 5 pages**
>
> **Grading Criteria**:
> - Completeness of operational scenarios (cover normal, edge, failure cases)
> - Quality of functional decomposition (appropriate granularity, clear function names)
> - FFBD correctness (proper notation, complete logic, timing feasibility)
> - Requirements traceability (all requirements mapped to functions)
> - Professional presentation (clear diagrams, proper labeling)
>
> **Tips**:
> - Research real AEB systems (Euro NCAP AEB tests, UN R152 regulation)
> - Think through scenarios step-by-step (walk through mentally)
> - Functions should be verb-based ('Detect object', not 'Detection module')
> - FFBD should be readable by non-engineers (test it on a friend)
> - Timing: AEB needs <1 second from detection to braking (work backward)
>
> **Discussion Questions**:
> - How would AEB functional analysis differ for highway vs urban scenarios?
> - What happens if pedestrian detection function has 100ms latency? (timeline analysis)
> - How do you allocate functions between radar ECU and AEB ECU? (allocation strategy)
>
> **Resources**:
> - INCOSE Systems Engineering Handbook, Chapter 4.3 (Functional Analysis)
> - NASA Systems Engineering Handbook, Section 4.4 (FFBD)
> - ISO 26262-3:2018 (Functional Safety Concept)
>
> **30 minutes for your questions.**"

---

## 📊 PPT DESIGN GUIDANCE

### Visual Style:
- **Technical/analytical aesthetic**: Clean diagrams, process flows, structured charts
- **Color coding**:
  - Blue for functions and functional elements
  - Green for operational scenarios and use cases
  - Orange for timing and critical paths
  - Red for warnings, failure modes, and gaps
  - Purple for allocation and traceability links
- **Use real automotive examples**: ACC, LKA, AEB with actual sensor images and diagrams
- **Diagrams**: Professional FFBD notation, N² charts, timeline diagrams, hierarchical trees

### Key Slides to Emphasize:
1. **Slide 3** (Structure vs Behavior gap) - Core problem being solved
2. **Slide 8** (Operational scenario template) - Students will reuse this
3. **Slide 15** (Functional hierarchy) - Fundamental decomposition concept
4. **Slide 19** (FFBD notation) - Reference for all future FFBDs
5. **Slide 21** (FFBD continuous loop) - Real-world operational flow
6. **Slide 24** (Requirements allocation) - Closes traceability loop
7. **Slide 28** (Tesla case study) - Real-world consequences
8. **Slide 29** (Summary) - Students will photograph this

### Animations:
- **Slide 8**: Build operational scenario step-by-step (each element appears sequentially)
- **Slide 15**: Animate function hierarchy expanding from Level 0 → Level 1 → Level 2
- **Slide 17**: Highlight N² chart flows one-by-one to explain reading
- **Slide 20**: Animate FFBD flow execution (highlight boxes in sequence)
- **Slide 25**: Animate timeline bars appearing in sequence, highlight critical path

### Tables and Diagrams:
- **Slide 9**: Operational scenario matrix (modes × environments, 6×4 grid)
- **Slide 12**: Capability gap to requirements mapping (3-column table)
- **Slide 17**: N² chart (7×7 grid for LKA functions)
- **Slide 24**: Requirements Allocation Matrix (4-column table, 10+ rows)
- **Slide 25**: Timeline diagram (Gantt-style with millisecond scale)

### Real Examples to Include:
- Actual LKA operational videos (lane keeping, override, deactivation)
- Screenshots of SysML Activity Diagrams (FFBD equivalent in MBSE)
- Real functional architecture diagrams from automotive standards
- Timeline analysis from real ADAS development projects (if available)
- Tesla Autopilot investigation NTSB report excerpts

---

## 🎯 INSTRUCTOR NOTES

### Pedagogical Strategy:
- **Concrete → Abstract → Concrete**: Start with LKA example, teach methods, apply to ACC/AEB
- **Build complexity gradually**: Scenarios → Functions → FFBDs → Allocation → Timing
- **Use case study**: Tesla Autopilot as cautionary tale (consequences of incomplete analysis)
- **Tool exposure**: Show MBSE tools (SysML Activity Diagrams) if possible
- **Hands-on thinking**: Walk through FFBD execution mentally, timing analysis calculations

### Common Student Challenges:

**Challenge 1: "This seems like a lot of documentation for obvious behavior"**
**How to address:** Show Slide 28 (Tesla case). What seems "obvious" is often incomplete. Systematic analysis finds gaps. Ask: "Without writing it down, can you describe ALL scenarios for LKA including failures?" The answer is always no. Writing forces completeness.

**Challenge 2: "How do I know when a function is at the right level of detail?"**
**How to address:**
- Too high-level: "Process data" (not specific enough)
- Too low-level: "Multiply matrix element [3,2] by scaling factor 0.95" (implementation detail)
- Just right: "Calculate lateral offset from lane center" (clear transformation, mappable to requirement and design)
- **Rule of thumb**: Function should map to verifiable requirement AND single design element (algorithm/module)

**Challenge 3: "FFBD vs software flowchart - what's the difference?"**
**How to address:**
- FFBD: FUNCTIONAL view (what system does, technology-agnostic)
- Flowchart: IMPLEMENTATION view (how software implements)
- Example: FFBD shows "Detect lane markings" → could be implemented as neural network, classical CV, or sensor fusion
- FFBD is input to design, not design itself

**Challenge 4: "Operational scenarios vs use cases - aren't they the same?"**
**How to address:**
- **Operational scenario**: Narrative description of system use (includes context, environment, sequence)
- **Use case**: Formal model of interaction (UML/SysML, focus on actor-system interaction)
- **Relationship**: Operational scenarios are SOURCE, use cases are FORMALIZATION
- Use cases are more structured, scenarios are more descriptive

**Challenge 5: "How many scenarios do I need?"**
**How to address:** Coverage criteria:
- Every operational mode (activation, operation, deactivation, failure)
- Critical environmental conditions (weather extremes, lighting, road types)
- Failure modes (sensor degraded, actuator limited, communication loss)
- Interaction scenarios (driver override, multi-system coordination)
- **Rule of thumb**: If scenario not covered, system behavior undefined (dangerous for safety-critical)
- **Automotive ADAS**: 30-50 scenarios typical

### Timing Flexibility:

**If running short:**
- Condense Slide 11 (Capability gap analysis) - brief overview
- Reduce Slide 16 (Decomposition methods) to primary method only
- Move Slide 27 (ACC example) to backup slides
- Shorten Slide 28 case study to bullet points

**If running long:**
- Extend Slide 20-21 (FFBD) with live walkthrough exercise
- Add interactive FFBD development (students contribute steps)
- Show live MBSE tool demo (Cameo Activity Diagram)
- Deeper dive into timing analysis with real calculations

**Core content (must cover - non-negotiable):**
- Slides 8-9 (Operational scenarios)
- Slides 14-15 (Functional decomposition)
- Slides 19-21 (FFBD fundamentals and examples)
- Slide 24 (Requirements allocation)
- Slide 25 (Timeline analysis)
- Slide 28 (Case study - consequences)
- Slide 29 (Summary)

### Engagement Points:

**Slide 7**: Interactive - Ask students: "What operational questions do YOU think we need to answer for LKA?" Crowdsource list, then show comprehensive list.

**Slide 15**: Work through decomposition together - Show Level 1 function, ask students to propose Level 2 decomposition before revealing.

**Slide 20**: Walk through FFBD execution - "You are the system. What do you do first? Next? What if this condition occurs?"

**Slide 25**: Timeline calculation - Give students timing values, ask them to calculate total cycle time and identify if requirement is met.

**Slide 28**: Case study discussion - "If you were the systems engineer, at what point in functional analysis would this gap be discovered?"

### Interactive Elements:

**Quick Poll (Slide 4)**: "How many have worked on systems where unexpected behavior occurred during integration?" (Most will raise hands - validates need for functional analysis)

**Pair Exercise (Slide 9)**: Give pairs 5 minutes to identify operational scenarios for "automatic headlight control." Share and critique.

**Think-Pair-Share (Slide 21)**: "What happens if function 2.0 (lane detection) fails during execution? Where does FFBD go?" Discuss failure handling.

**Case Analysis (Slide 28)**: Small groups: "List 3 operational scenarios that would have identified the Tesla Autopilot gap." Share findings.

### Materials to Prepare:

**Before class:**
- [ ] FFBD templates (blank diagrams for students to follow along)
- [ ] Operational scenario template (from Slide 8)
- [ ] N² chart template (Excel or PowerPoint)
- [ ] Timeline analysis spreadsheet example
- [ ] MBSE tool screenshots or demo (Cameo/EA Activity Diagrams)
- [ ] Tesla Autopilot NTSB report excerpts (Slide 28 case study)

**Handouts:**
- [ ] FFBD notation reference card (symbols and meanings)
- [ ] Operational scenario template (1-page)
- [ ] Functional decomposition checklist
- [ ] Requirements allocation matrix (RAM) template (Excel)
- [ ] Timeline analysis worksheet

**Post-class:**
- [ ] Share slides
- [ ] Post exercise assignment with templates
- [ ] Post FFBD examples and notation guide
- [ ] Share links to: INCOSE Handbook Ch. 4.3, NASA SE Handbook 4.4, ISO 26262-3
- [ ] Create discussion forum: "Share an operational scenario that's often forgotten in ADAS design"

### Assessment Opportunities:

**During lecture:**
- Quick quiz (Slide 10): "Is this a good operational scenario?" (show example, students critique)
- Quick quiz (Slide 15): "At what level should this function stop being decomposed?"
- Quick quiz (Slide 19): "What does this FFBD symbol mean?"

**Exercise assessment criteria:**
- Operational scenario completeness (Did they cover failure modes? Edge cases?)
- Functional decomposition quality (Appropriate granularity? Technology-agnostic?)
- FFBD correctness (Proper notation? Logical flow? Timing realistic?)
- Requirements traceability (All requirements mapped? Bidirectional links?)
- Professional presentation (Clear diagrams? Proper labeling? Readable?)

**Common student mistakes to watch for:**
- Operational scenarios that are too vague ("System works normally")
- Functions that are really components ("Radar module" instead of "Detect objects")
- FFBDs missing failure paths (only happy path)
- Timing analysis with optimistic estimates (no margin)
- Requirements not allocated to any function (orphan requirements)

---

## ✅ Session Success Criteria

Students leave able to:
- ✓ Develop comprehensive operational scenarios for automotive systems
- ✓ Perform capability gap analysis to identify functional requirements
- ✓ Decompose system behavior into hierarchical functions
- ✓ Create functional flow block diagrams (FFBDs) using standard notation
- ✓ Model sequential, parallel, and conditional operational flows
- ✓ Allocate requirements to functions systematically
- ✓ Perform timeline analysis to validate temporal feasibility
- ✓ Understand the link between functional analysis and system architecture
- ✓ Recognize consequences of incomplete functional analysis (safety implications)

**Critical outcome:** Students can **analyze operational behavior systematically** and **create functional models** that bridge requirements and design, ensuring complete coverage of operational scenarios.

**Evidence of success:**
- Student can develop FFBD for a given automotive scenario
- Student can identify missing operational scenarios through systematic enumeration
- Student can explain how functions map to requirements and to physical architecture
- Student can perform basic timeline analysis and identify critical paths
- Student understands why Tesla Autopilot crash was a functional analysis failure

---

## 📚 Additional Resources for Students

**Standards and Guidelines:**
- INCOSE Systems Engineering Handbook v4, Chapter 4.3: Functional Analysis
- NASA Systems Engineering Handbook, Section 4.4: Functional Analysis and Allocation
- IEEE 1220-2005: Standard for Application and Management of the Systems Engineering Process (Functional Analysis)
- ISO/IEC/IEEE 15288:2015: Systems Life Cycle Processes (Functional Analysis activities)

**Automotive-Specific:**
- ISO 26262-3:2018: Road Vehicles - Functional Safety - Part 3: Concept Phase (Functional Safety Concept)
- SAE J3016: Taxonomy and Definitions for Terms Related to Driving Automation Systems (for ADAS scenarios)
- UN Regulation No. 152: Advanced Emergency Braking Systems (operational scenarios)
- Euro NCAP AEB Test Protocol (operational scenario definitions)

**FFBD and Functional Modeling:**
- "Functional Flow Block Diagrams" - NASA Technical Report (free online)
- "Activity Diagrams in SysML" - OMG SysML Specification v1.6
- "Use Case Modeling" - Alistair Cockburn (scenarios and use cases)

**Books:**
- "Systems Engineering Principles and Practice" by Alexander Kossiakoff et al. - Chapter 5 (Functional Analysis)
- "Engineering Systems Engineering" by Olivier de Weck et al. - Chapter 4 (Functional Modeling)
- "Model-Based Systems Engineering" by Tim Weilkiens - SysML Activity Diagrams

**Online Resources:**
- SEBoK (Systems Engineering Body of Knowledge): Functional Analysis section (free)
- INCOSE Functional Analysis Working Group resources
- NASA APPEL: Systems Engineering Fundamentals (functional analysis module)

---

## 🔗 Connections to Other Sessions

**Builds on:**
- **Session 2**: ISO/IEC 15288 technical processes (functional analysis is part of architecture definition)
- **Session 3**: MBSE tools represent functions using SysML Activity Diagrams
- **Session 4**: Requirements drive functional analysis; functional analysis allocates requirements
- **Session 5**: Architecture provides structure; functional analysis provides behavior

**Leads to:**
- **Session 8**: Verification tests functions; validation tests operational scenarios (V&V)
- **Session 9**: Functional decomposition informs work breakdown structure (WBS) for project planning
- **Session 12**: Functional safety (ISO 26262) requires functional safety concept and safety functions
- **Session 15**: Configuration management tracks function versions and allocation changes

**Key concept thread:**
- **Session 4**: WHAT must system do? (Requirements)
- **Session 5**: HOW is system structured? (Architecture - components, interfaces)
- **Session 7**: WHAT does system do operationally? (Functional Analysis - behavior) ← TODAY
- **Session 8**: Did we build it right? (Verification) Did we build right thing? (Validation)

**Functional analysis appears in:**
- Session 8: FFBDs become test sequences, scenarios become test cases
- Session 9: Timeline analysis identifies schedule and resource risks
- Session 12: Safety functional analysis (HARA → safety functions → safety FFBDs)
- Session 15: Technical baselines include functional architecture and FFBDs

---

## 🎬 Opening and Closing Strategies

### **Opening (First 3 minutes):**
Show LKA video (vehicle maintaining lane, correcting drift) on screen as students enter. Begin:

> "Watch this vehicle. It's keeping itself centered in the lane with no driver input. Simple, right?
>
> Now answer me this: What happens if the lane lines disappear in a construction zone? What if a vehicle cuts in front while it's correcting? What if the camera gets dirty? What's the sequence of operations - camera to decision to steering?
>
> [Pause - students realize they don't know]
>
> You just saw the system work. But could you design it? Could you test it? Could you explain every operational scenario?
>
> This is why we need Operational and Functional Analysis. We're going to learn how to systematically decompose behavior so that we FULLY understand what the system does, when it does it, and why.
>
> Welcome to Session 7 - where we make behavior explicit."

### **Closing (Last 2 minutes):**
Return to opening LKA video:

> "Remember the question I asked at the start: Could you design this lane keeping system?
>
> Now you can. You know how to:
> - Define all operational scenarios (including the edge cases that kill projects)
> - Decompose behavior into functions systematically
> - Model operational flows with FFBDs
> - Allocate requirements and validate timing
>
> You also know the consequences of skipping this work. [Show Tesla Autopilot crash image briefly] This wasn't a component failure. This was a functional analysis gap. A missing operational scenario.
>
> Your exercise is your chance to practice preventing the next tragedy. Treat it seriously.
>
> In Session 8, we'll take your functional model and verify every function works, then validate that operational scenarios execute correctly. That's the right side of the V-Model.
>
> See you then."

---

## 📈 Learning Objectives Mapping to Assessment

| Session Objective | Assessment Method | Success Criteria |
|-------------------|-------------------|------------------|
| Define operational scenarios | Exercise Part 1 | 6 scenarios covering normal, edge, failure cases; proper template use |
| Perform capability gap analysis | Conceptual understanding (in-class) | Can explain gap → functional requirement derivation |
| Decompose into functions | Exercise Part 2 | 3-level hierarchy, clear function names, appropriate granularity |
| Create FFBDs | Exercise Part 3 | Correct FFBD notation, logical flow, timing annotated |
| Allocate requirements to functions | Exercise Part 4 | All requirements mapped, RAM complete, verification method identified |
| Develop functional architectures | Exercise Part 2 (N² chart) | Complete N² chart showing function interfaces |
| Perform timeline analysis | Exercise Part 3 (FFBD timing) | Realistic timing estimates, total cycle time calculated |
| Apply to automotive systems | Overall exercise | AEB system functional model is complete and correct |

---

**End of Session 7 Framework**
**Next:** Session 8 (System Integration, Verification & Validation)
