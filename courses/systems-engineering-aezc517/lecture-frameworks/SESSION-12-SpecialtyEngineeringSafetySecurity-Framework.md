# Session 12: Specialty Engineering - Safety & Security
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 90 minutes lecture + 30 minutes Q&A
**Approach:** Safety/Security-Focused
**PPT Target:** 28-30 slides

---

## 🎯 Session Objectives (For Instructor)

By the end of this session, students will be able to:
- Apply safety analysis methods to identify hazards in automotive systems
- Conduct Hazard Analysis and Risk Assessment (HARA) per ISO 26262
- Understand functional safety requirements and ASIL classification
- Apply cybersecurity principles to automotive systems
- Define interoperability requirements for connected vehicles
- Incorporate human factors engineering in system design
- Integrate safety and security requirements into systems engineering processes

**Mapped Learning Outcomes:** LO4 (Apply systems engineering practices and methods in automotive systems), LO5 (Analyse automotive systems using systems engineering approaches to increase performance)

---

## 📖 INSTRUCTOR-LED STORY ARC

### **SETUP: The Critical Intersection** (Slides 1-5, ~10 minutes)

#### Slide 1: Title
**Visual:** Professional title slide with overlapping shield icons representing safety and security
**Instructor Script:**
> "Welcome to Session 12. Today we tackle a critical reality of modern automotive systems engineering: Safety and Security are no longer separate concerns - they are deeply intertwined.
>
> Get safety wrong, and people die. Get security wrong, and your safe system becomes a weapon. Today, we learn how to engineer both simultaneously."

#### Slide 2: Connection to Previous Sessions
**Visual:** Progression diagram showing Sessions 1→4→8→9→12
**Instructor Script:**
> "Let's connect our journey to where we are today:
>
> **Session 1**: We learned from engineering failures. Many were safety failures - Therac-25, Toyota unintended acceleration.
>
> **Session 4**: We learned requirements engineering. Safety and security requirements need EXTRA rigor.
>
> **Session 8**: We learned verification and validation. Safety-critical systems require specialized V&V approaches.
>
> **Session 9**: We learned risk management and DFMEA. Today, we go deeper into safety-specific risk analysis.
>
> Today's focus: **Specialty Engineering - the disciplines that keep systems safe, secure, and usable.**"

#### Slide 3: Why Safety & Security Engineering Is Critical
**Visual:** Statistics and timeline showing automotive incidents
**Instructor Script:**
> "Let me show you the stakes we're dealing with:
>
> **Safety Statistics:**
> - 1.19 million road traffic deaths globally per year (WHO)
> - 10-30% of crashes involve system/component failures
> - Average recall cost: $300M+ for major OEMs
> - Legal liability: Multi-billion dollar settlements
>
> **Security Incidents:**
> - 2015: Jeep Cherokee hacked remotely, 1.4M vehicles recalled
> - 2016: Tesla Model S hacked via browser exploit
> - 2020: Mercedes E-Class encryption broken
> - 2022: Toyota production halted due to supplier cyberattack
>
> **The convergence:**
> - Modern vehicles: 100+ ECUs, 100M+ lines of code
> - Connected vehicles: Remote attack surface
> - Autonomous vehicles: Safety + Security + AI uncertainty
>
> **Key insight**: A cybersecurity breach can CAUSE safety failures. These disciplines must be integrated.
>
> This is why specialty engineering is not optional - it's fundamental to modern automotive systems engineering."

#### Slide 4: Real-World Example - The Jeep Cherokee Hack
**Visual:** Jeep Cherokee with timeline of 2015 hack and recall
**Instructor Script:**
> "Remember this case: July 2015, security researchers Charlie Miller and Chris Valasek demonstrated:
>
> **The attack:**
> - Remote access via cellular connection
> - Exploited vulnerability in Uconnect infotainment system
> - Gained control of steering, brakes, transmission
> - Attack possible from anywhere in the US (cellular network)
>
> **The impact:**
> - 1.4 million vehicles recalled
> - $1.4 billion settlement fund
> - NHTSA investigation and new regulations
> - Fundamental shift in automotive cybersecurity awareness
>
> **What failed:**
> - **Security failure**: Infotainment system connected to CAN bus without isolation
> - **Safety failure**: No defense-in-depth - single exploit compromised safety-critical functions
> - **Interoperability failure**: Mixing security zones (entertainment + safety-critical)
> - **Human factors failure**: No driver indication of compromise
>
> **This demonstrates why we need INTEGRATED specialty engineering.**
>
> Today, I'll show you how to prevent this through systematic safety and security engineering."

#### Slide 5: Learning Journey for Today
**Visual:** Roadmap with 6 key stops
**Instructor Script:**
> "Today's journey covers six critical specialty engineering disciplines:
>
> **Part 1**: Safety Analysis Methods - FTA, FMEA, HAZOP
> **Part 2**: HARA and ISO 26262 - Functional safety framework
> **Part 3**: Cybersecurity in Automotive - Threat modeling, defense-in-depth
> **Part 4**: Interoperability Engineering - Connecting systems safely
> **Part 5**: Human Factors Engineering - Designing for humans
> **Part 6**: Integration - Bringing it all together
>
> By the end, you'll understand how to systematically engineer safety, security, and usability into automotive systems.
>
> These are the disciplines that separate professional automotive systems engineers from amateurs."

---

### **TRIGGER: The Engineering Challenge** (Slides 6-7, ~5 minutes)

#### Slide 6: A Deceptively Complex System
**Visual:** Simple box with text "Design an Adaptive Cruise Control (ACC) system"
**Instructor Script:**
> "Let me give you a challenge. Your manager says:
>
> **'Design an Adaptive Cruise Control system with automatic emergency braking.'**
>
> From Session 4, you know how to write requirements. But now, consider the specialty engineering questions:
>
> **Safety Questions:**
> - What if the radar sensor fails? (Safety hazard)
> - What if the system brakes when it shouldn't? (False positive - safety risk)
> - What if it doesn't brake when it should? (False negative - safety critical)
> - What's the acceptable failure rate? (Quantitative safety requirement)
> - What safety integrity level is required? (ASIL classification)
>
> **Security Questions:**
> - Can an attacker spoof the radar? (Sensor security)
> - Can someone remotely disable emergency braking? (System security)
> - Can they cause unintended braking? (Safety through security)
> - How do we authenticate sensor data? (Secure communication)
>
> **Human Factors Questions:**
> - Will drivers understand when the system is active? (Situational awareness)
> - Will they over-rely on it? (Automation complacency)
> - Can they override it in emergencies? (Human-in-the-loop)
> - Is the interface intuitive under stress? (Cognitive load)
>
> **Suddenly, our 'simple' ACC is a complex specialty engineering challenge.**"

#### Slide 7: What Could Go Wrong?
**Visual:** Fault tree showing failure scenarios
**Instructor Script:**
> "Here's what happens without systematic safety and security engineering:
>
> **Scenario 1 - Tesla Autopilot Crashes (Multiple incidents)**
> - Drivers over-relied on Level 2 automation (human factors failure)
> - System didn't detect stationary objects in certain scenarios (safety analysis gap)
> - Inadequate driver monitoring (human factors + safety failure)
>
> **Scenario 2 - Toyota Unintended Acceleration (from Session 4)**
> - Software failures in throttle control (safety)
> - No independent safety mechanism (defense-in-depth failure)
> - 89 deaths, $1.2B settlement
>
> **Scenario 3 - Jeep Cherokee Hack (just discussed)**
> - Remote exploitation of connected system (security)
> - Compromised safety-critical functions (safety through security)
> - 1.4M recalls
>
> **The common thread:**
> - Inadequate hazard analysis (didn't identify all failure modes)
> - Missing security threat modeling (didn't consider attack vectors)
> - Poor human factors analysis (didn't account for human behavior)
>
> **This is why we need systematic specialty engineering methods.**
>
> Today, I'll show you exactly how professionals handle these challenges."

---

### **RISING ACTION: Building the Specialty Engineering Framework** (Slides 8-24, ~52 minutes)

#### **Part 1: Safety Analysis Methods** (Slides 8-11, ~12 minutes)

##### Slide 8: Safety Analysis - The Systematic Approach
**Visual:** Overview diagram showing safety analysis lifecycle
**Instructor Script:**
> "Safety engineering is NOT about testing more. It's about ANALYZING systematically to identify what could go wrong BEFORE it happens.
>
> **The safety analysis process:**
>
> **Step 1: Hazard Identification**
> - What can go wrong? (Brainstorming, historical data, standards)
> - Example: 'Vehicle accelerates when driver didn't command it'
>
> **Step 2: Risk Analysis**
> - How likely? (Probability)
> - How severe? (Consequence)
> - Risk = Severity × Probability
>
> **Step 3: Risk Evaluation**
> - Is this risk acceptable?
> - What's our risk tolerance?
> - Automotive: ISO 26262 defines acceptability criteria
>
> **Step 4: Risk Treatment**
> - Eliminate (design out the hazard)
> - Mitigate (reduce probability or severity)
> - Accept (if below threshold)
> - Transfer (insurance, contractual)
>
> **Step 5: Verification**
> - Prove the risk has been adequately addressed
> - Safety testing, analysis, review
>
> **Three powerful methods we'll explore:**
> 1. Fault Tree Analysis (FTA) - Top-down
> 2. Failure Mode and Effects Analysis (FMEA) - Bottom-up
> 3. HAZOP (Hazard and Operability Study) - Systematic deviation analysis
>
> Let me show you each."

##### Slide 9: Fault Tree Analysis (FTA)
**Visual:** Example fault tree diagram for ACC system
**Instructor Script:**
> "**Fault Tree Analysis (FTA)** is a TOP-DOWN deductive method.
>
> **How it works:**
>
> **1. Start with top event** (hazardous situation):
> - Example: 'Vehicle fails to brake for obstacle'
>
> **2. Work backward** - what could cause this?
> - Radar sensor failure OR
> - ECU processing failure OR
> - Brake actuator failure OR
> - Software algorithm failure
>
> **3. Continue decomposing** each cause:
> - Radar sensor failure caused by:
>   - Power supply failure AND
>   - No backup sensor available
>
> **4. Use logic gates:**
> - **AND gate**: All inputs must occur (Power fail AND no backup)
> - **OR gate**: Any input causes event (Sensor OR ECU OR actuator fail)
>
> **5. Calculate probability:**
> - If each component has known failure rate
> - AND gate: P(A AND B) = P(A) × P(B)
> - OR gate: P(A OR B) = P(A) + P(B) - P(A)×P(B)
>
> **Real automotive example - Brake System FTA:**
>
> Top Event: 'Loss of braking function'
> ├─ OR ─ Hydraulic failure
> │   ├─ AND ─ Master cylinder leak
> │   │   ├─ Seal degradation
> │   │   └─ No brake fluid level warning
> │   └─ OR ─ Brake line rupture
> ├─ OR ─ Electronic control failure
> │   ├─ AND ─ ECU failure
> │   │   ├─ Software bug
> │   │   └─ Watchdog timer disabled
> │   └─ OR ─ Sensor failure
> └─ OR ─ Driver input failure
>     └─ Pedal mechanism broken
>
> **FTA benefits:**
> - Visual representation of failure paths
> - Quantitative risk assessment
> - Identifies single points of failure
> - Shows where redundancy is needed
>
> **FTA limitations:**
> - Time-consuming for complex systems
> - Requires knowing all failure modes upfront
> - Complement with bottom-up methods (FMEA)"

##### Slide 10: Failure Mode and Effects Analysis (FMEA)
**Visual:** FMEA table template with automotive examples
**Instructor Script:**
> "**FMEA** is a BOTTOM-UP inductive method. We looked at this in Session 9 for design. Now we apply it specifically for safety.
>
> **FMEA Process:**
>
> **1. Identify components/functions**
> - Example: ACC radar sensor, ECU, brake actuator
>
> **2. For each component, ask:**
> - What are the possible failure modes? (How can it fail?)
> - What are the effects? (What happens when it fails?)
> - What are the causes? (Why does it fail?)
> - How do we detect it? (How do we know it failed?)
>
> **3. Rate each failure mode:**
> - **Severity (S)**: 1-10 (1=no effect, 10=catastrophic)
> - **Occurrence (O)**: 1-10 (1=rare, 10=frequent)
> - **Detection (D)**: 1-10 (1=certain detection, 10=no detection)
> - **RPN (Risk Priority Number)**: S × O × D
>
> **4. Prioritize actions:**
> - High RPN = high priority for mitigation
>
> **Automotive example - ACC Radar Sensor FMEA:**
>
> | Component | Failure Mode | Effect | S | Cause | O | Detection | D | RPN | Action |
> |-----------|--------------|--------|---|-------|---|-----------|---|-----|--------|
> | Radar sensor | No output signal | Loss of ACC/AEB function | 9 | Power supply failure | 3 | Self-diagnostic detects | 2 | 54 | Add redundant power, driver warning |
> | Radar sensor | False object detection | Unintended braking | 8 | Rain/snow interference | 5 | Plausibility check with camera | 4 | 160 | Sensor fusion, false positive filtering |
> | Radar sensor | Degraded range | Reduced reaction time | 7 | Sensor blockage (dirt) | 6 | Range monitoring | 3 | 126 | Sensor cleaning system, blockage detection |
> | ECU | Processing delay >100ms | Late braking response | 9 | CPU overload | 2 | Watchdog timer | 2 | 36 | Task prioritization, WCET analysis |
> | Brake actuator | Stuck inactive | No emergency braking | 10 | Mechanical jam | 1 | Actuation monitoring | 3 | 30 | Regular maintenance, redundancy |
>
> **ISO 26262 enhancement:**
> - In functional safety FMEA, we add **ASIL** (Automotive Safety Integrity Level)
> - ASIL A (lowest) to ASIL D (highest)
> - Determines required safety measures and verification rigor
>
> **Key difference from Session 9:**
> - Design FMEA: Focus on design robustness
> - Safety FMEA: Focus on hazardous failures with **safety consequences**
> - Safety FMEA feeds into HARA (next section)
>
> **FMEA benefits:**
> - Systematic, comprehensive
> - Quantitative prioritization
> - Cross-functional team exercise
>
> **FMEA limitations:**
> - Doesn't capture combinations of failures (use FTA for that)
> - Time-intensive
> - Quality depends on team expertise"

##### Slide 11: HAZOP (Hazard and Operability Study)
**Visual:** HAZOP guide words and example application
**Instructor Script:**
> "**HAZOP** is a structured brainstorming method using **guide words** to systematically explore deviations.
>
> **HAZOP Guide Words:**
> - **NO/NOT**: Complete negation (e.g., no braking)
> - **MORE**: Quantitative increase (e.g., more braking force)
> - **LESS**: Quantitative decrease (e.g., less braking force)
> - **AS WELL AS**: Qualitative addition (e.g., braking + steering)
> - **PART OF**: Qualitative decrease (e.g., only front brakes)
> - **REVERSE**: Opposite (e.g., acceleration instead of braking)
> - **OTHER THAN**: Complete substitution (e.g., steering instead of braking)
>
> **HAZOP Process:**
>
> **1. Define system and boundaries**
> - Example: ACC with AEB system
>
> **2. Break into nodes/sections**
> - Node 1: Object detection (radar + camera)
> - Node 2: Decision logic (ECU)
> - Node 3: Brake actuation
>
> **3. For each node, apply guide words:**
> - Design intent: 'Radar detects obstacle at 150m range'
> - NO: Radar detects NO obstacle → Missed detection → Collision
> - MORE: Radar range MORE than 150m → Earlier braking → False positives
> - LESS: Radar range LESS than 150m → Late detection → Insufficient stopping distance
> - REVERSE: Radar reports object moving toward instead of away → Wrong TTC calculation
>
> **4. Analyze each deviation:**
> - Is it hazardous?
> - What are the causes?
> - What are the consequences?
> - What safeguards exist?
> - What actions are needed?
>
> **Example HAZOP for ACC 'Set Speed' function:**
>
> | Parameter | Guide Word | Deviation | Cause | Consequence | Safeguard | Action |
> |-----------|------------|-----------|-------|-------------|-----------|--------|
> | Speed | NO | No speed set | Switch failure | No ACC activation | Driver awareness | Add diagnostic check |
> | Speed | MORE | Speed set higher than current | Sensor error | Sudden acceleration | Speed limit check | Add plausibility check |
> | Speed | LESS | Speed set lower than current | Software bug | Hard braking | Deceleration rate limit | Code review, testing |
> | Speed | REVERSE | Speed increases when should decrease | Control logic inversion | Dangerous acceleration | Independent safety monitor | Add inverse logic check |
>
> **HAZOP benefits:**
> - Catches creative failure modes
> - Good for complex interactions
> - Team-based (different perspectives)
>
> **HAZOP limitations:**
> - Requires experienced facilitator
> - Can be exhaustive (time-consuming)
> - Qualitative (not quantitative like FTA/FMEA)
>
> **Automotive application:**
> - HAZOP used in early design phases
> - FMEA used for detailed component analysis
> - FTA used for critical hazard investigation
> - **All three are complementary - use together for comprehensive safety analysis**"

---

#### **Part 2: HARA and ISO 26262 Functional Safety** (Slides 12-15, ~12 minutes)

##### Slide 12: ISO 26262 - The Automotive Functional Safety Standard
**Visual:** ISO 26262 V-Model and part structure
**Instructor Script:**
> "**ISO 26262** is the international standard for functional safety in automotive electrical/electronic systems. It's based on IEC 61508 but tailored for automotive.
>
> **What is Functional Safety?**
> - 'Absence of unreasonable risk due to hazards caused by malfunctioning behavior of E/E systems'
> - Focus: Safety failures caused by SYSTEM MALFUNCTIONS (not physical crashes, driver error, etc.)
>
> **ISO 26262 Structure (12 parts):**
> - Part 1: Vocabulary
> - Part 2: Management of functional safety
> - Part 3: Concept phase (← HARA is here)
> - Part 4: Product development - System level
> - Part 5: Product development - Hardware level
> - Part 6: Product development - Software level
> - Part 7: Production and operation
> - Part 8: Supporting processes
> - Part 9: ASIL-oriented and safety-oriented analyses
> - Part 10: Guidelines
> - Part 11: Semiconductors
> - Part 12: Motorcycles
>
> **Key concepts:**
>
> **1. Safety Lifecycle** (V-Model for safety):
> - Concept phase → System development → Hardware/Software development → Integration → Testing → Operation
> - Each phase has safety requirements, activities, and work products
>
> **2. ASIL (Automotive Safety Integrity Level):**
> - ASIL A (lowest) → B → C → ASIL D (highest)
> - Determines rigor of safety requirements and verification
> - Higher ASIL = more stringent methods, more verification, more independence
>
> **3. Safety Mechanisms:**
> - Technical measures to detect/control faults
> - Examples: Watchdog timers, CRC checks, redundancy, diverse programming
>
> **4. Traceability:**
> - Every safety requirement must trace to hazard
> - Every safety requirement must be verified
> - Bidirectional traceability (remember Session 4!)
>
> **ISO 26262 is MANDATORY for new vehicle developments in most markets.**
>
> Let me show you the critical starting point: HARA."

##### Slide 13: HARA - Hazard Analysis and Risk Assessment
**Visual:** HARA process flowchart with automotive examples
**Instructor Script:**
> "**HARA** is the foundation of ISO 26262. It determines WHAT safety measures are needed and HOW rigorous they must be.
>
> **HARA Process (4 steps):**
>
> **Step 1: Hazard Identification**
> - Systematically identify hazards (What can go wrong at vehicle level?)
> - Focus on E/E system malfunctions
> - Sources: Brainstorming, FTA, FMEA, historical data, standards
>
> **Example hazards for ACC/AEB:**
> - Unintended braking (false positive)
> - Failure to brake (false negative)
> - Insufficient braking force
> - Delayed braking response
> - Loss of ACC function
>
> **Step 2: Situational Analysis**
> - In what driving situations can this hazard occur?
> - **Operational situations:** Highway, urban, parking, off-road
>
> **Example:**
> - Hazard: 'Unintended full braking'
> - Situation 1: Highway at 120 km/h
> - Situation 2: Urban at 50 km/h
> - Situation 3: Parking lot at 10 km/h
>
> **Step 3: Risk Classification (The core of HARA)**
>
> For each hazard + situation, rate three parameters:
>
> **a) Severity (S)** - Consequence of hazard:
> - **S0**: No injuries
> - **S1**: Light to moderate injuries
> - **S2**: Severe/life-threatening injuries (survival probable)
> - **S3**: Life-threatening/fatal injuries (survival uncertain)
>
> **b) Exposure (E)** - Probability of operational situation:
> - **E0**: Incredible (<0.1% of operating time)
> - **E1**: Very low probability (0.1%-1%)
> - **E2**: Low probability (1%-10%)
> - **E3**: Medium probability (10%-50%)
> - **E4**: High probability (>50%)
>
> **c) Controllability (C)** - Can driver/others avoid harm?
> - **C0**: Controllable in general
> - **C1**: Simply controllable (>99% of drivers)
> - **C2**: Normally controllable (>90% of drivers)
> - **C3**: Difficult/uncontrollable (<90% of drivers)
>
> **Step 4: ASIL Determination**
> - Combine S + E + C using ISO 26262 table
> - Result: ASIL QM (no safety requirements) or ASIL A/B/C/D
>
> **ASIL Table (simplified):**
>
> | Severity | Exposure | Controllability | ASIL |
> |----------|----------|-----------------|------|
> | S3 | E4 | C3 | **ASIL D** (Highest) |
> | S3 | E3 | C3 | ASIL D |
> | S3 | E4 | C2 | ASIL C |
> | S2 | E4 | C3 | ASIL C |
> | S3 | E2 | C2 | ASIL B |
> | S2 | E3 | C2 | ASIL B |
> | S1 | E4 | C2 | ASIL A |
> | S1 | E2 | C1 | QM (Quality Management) |
>
> Let me show you a real example."

##### Slide 14: HARA Example - Adaptive Cruise Control
**Visual:** Complete HARA table for ACC system
**Instructor Script:**
> "Let's work through a complete HARA for an ACC system.
>
> **HARA Example - ACC System:**
>
> | ID | Hazard | Situation | S | E | C | ASIL | Rationale |
> |----|--------|-----------|---|---|---|------|-----------|
> | H-ACC-01 | Unintended full braking | Highway 120 km/h, dry road, following vehicle | S3 | E3 | C2 | **C** | S3: Rear-end collision likely fatal<br>E3: ACC used 20% on highway<br>C2: Most drivers can steer to shoulder |
> | H-ACC-02 | Unintended full braking | Urban 50 km/h, intersection | S2 | E2 | C1 | **A** | S2: Rear-end at lower speed<br>E2: ACC rarely used in urban<br>C1: Driver easily stops/steers |
> | H-ACC-03 | Failure to brake for stopped vehicle | Highway 120 km/h, lead vehicle emergency stops | S3 | E4 | C3 | **D** | S3: Fatal collision likely<br>E4: Common scenario<br>C3: Insufficient time to react |
> | H-ACC-04 | Insufficient braking force | Highway 100 km/h, lead vehicle decelerates | S2 | E4 | C2 | **B** | S2: Minor collision possible<br>E4: Common scenario<br>C2: Driver can brake manually |
> | H-ACC-05 | Late braking response (>500ms delay) | Highway 120 km/h, lead vehicle brakes | S3 | E3 | C2 | **C** | S3: Collision likely severe<br>E3: Moderate frequency<br>C2: Driver can react if alerted |
> | H-ACC-06 | Loss of ACC function | Highway cruising | S0 | E4 | C0 | **QM** | S0: No safety impact (driver takes over)<br>E4: N/A<br>C0: Normal driving |
>
> **What this tells us:**
>
> **ASIL D** (H-ACC-03: Failure to brake for stopped vehicle):
> - **Highest rigor required**
> - Independent safety element required
> - Extensive verification (fault injection, statistical testing)
> - Tool qualification for software tools
> - Hardware random failure metrics (PMHF <10 FIT)
> - Software development per ASIL D (defensive programming, diverse implementation)
>
> **ASIL C** (H-ACC-01, H-ACC-05):
> - High rigor (but less than D)
> - Safety mechanisms required
> - Comprehensive testing
>
> **ASIL B** (H-ACC-04):
> - Moderate rigor
> - Basic safety mechanisms
> - Standard testing
>
> **ASIL A** (H-ACC-02):
> - Low rigor
> - Best practices
>
> **QM** (H-ACC-06):
> - Quality management (no safety requirements)
> - Standard development process
>
> **Key insight:**
> - Different hazards → Different ASIL → Different development effort
> - ASIL D functions may require **10x more effort** than ASIL A
> - Architecture must consider ASIL decomposition (break ASIL D into multiple lower ASIL)"

##### Slide 15: Safety Concept and Requirements
**Visual:** Flow from HARA to safety goals to safety requirements
**Instructor Script:**
> "After HARA, we develop the **Safety Concept** - HOW we'll address each hazard.
>
> **From HARA to Implementation:**
>
> **1. Safety Goals** (Top-level)
> - One safety goal per hazard
> - Inherits ASIL from hazard
>
> **Example (H-ACC-03: Failure to brake):**
> - **SG-ACC-03**: 'Prevent collision with stopped vehicle ahead' [ASIL D]
>
> **2. Functional Safety Requirements (FSR)**
> - Decompose safety goal into specific requirements
> - Allocate to vehicle functions
>
> **Example FSRs for SG-ACC-03:**
> - FSR-ACC-03.1: 'Detect stopped vehicles at ≥150m range with 99.9% probability' [ASIL D]
> - FSR-ACC-03.2: 'Calculate time-to-collision (TTC) with ≤50ms latency' [ASIL D]
> - FSR-ACC-03.3: 'Initiate emergency braking when TTC <2.5s' [ASIL D]
> - FSR-ACC-03.4: 'Achieve minimum deceleration of 6 m/s² within 300ms' [ASIL D]
> - FSR-ACC-03.5: 'Provide independent monitoring of braking function' [ASIL D]
>
> **3. Technical Safety Requirements (TSR)**
> - Allocate FSRs to system architecture
> - Hardware + Software + Safety Mechanisms
>
> **Example TSRs:**
> - TSR-ACC-HW-01: 'Radar sensor shall have dual-channel processing' [ASIL D]
> - TSR-ACC-SW-01: 'Object detection algorithm shall use sensor fusion (radar + camera)' [ASIL D]
> - TSR-ACC-SW-02: 'Software shall implement E2E (end-to-end) protection for CAN messages' [ASIL D]
> - TSR-ACC-SM-01: 'Independent safety monitor shall check TTC calculation with diverse algorithm' [ASIL D]
>
> **4. Safety Mechanisms (Examples for ASIL D):**
> - **Hardware level:**
>   - Dual-core lockstep processor (detects transient faults)
>   - ECC (Error Correcting Code) memory
>   - Watchdog timer with windowed monitoring
>   - Voltage/clock monitoring
> - **Software level:**
>   - Plausibility checks (range, rate-of-change)
>   - Defensive programming (assertions, boundary checks)
>   - Control flow monitoring
>   - CRC for data integrity
>   - E2E protection for communication
> - **System level:**
>   - Sensor fusion (radar + camera)
>   - Diverse redundancy (different algorithms)
>   - Safe state transition (warn driver, gradual degradation)
>
> **Verification per ASIL D:**
> - Back-to-back testing (compare diverse implementations)
> - Fault injection (test safety mechanisms)
> - Requirements coverage analysis
> - Code coverage (MC/DC for ASIL D)
> - Independent safety assessment
>
> **Traceability (critical for ISO 26262):**
> Hazard → Safety Goal → FSR → TSR → Implementation → Test Cases
>
> **Key takeaway:**
> ISO 26262 provides a SYSTEMATIC framework from hazard identification to verified safe system. It's not bureaucracy - it's disciplined engineering that saves lives."

---

#### **Part 3: Cybersecurity in Automotive Systems** (Slides 16-19, ~12 minutes)

##### Slide 16: The Cybersecurity Imperative
**Visual:** Attack surface evolution - 1990s car vs modern connected vehicle
**Instructor Script:**
> "Modern vehicles are **computers on wheels** - and computers can be hacked.
>
> **The evolution of automotive attack surface:**
>
> **1990s vehicle:**
> - Standalone ECUs, no external connectivity
> - Physical access required for any attack
> - Attack surface: ~1 (diagnostic port)
>
> **2010s vehicle:**
> - 100+ ECUs, connected via CAN/LIN/FlexRay
> - Cellular (telematics), WiFi, Bluetooth
> - Attack surface: ~10-20 entry points
>
> **2020s+ vehicle:**
> - Vehicle-to-Everything (V2X) communication
> - Over-the-air (OTA) updates
> - Cloud connectivity, mobile apps
> - Third-party app integration
> - Attack surface: **100+ potential entry points**
>
> **Why cybersecurity is critical:**
>
> **1. Safety impact:**
> - Jeep Cherokee: Hacked steering/brakes (safety-critical)
> - Tesla: Hacked via browser, could control vehicle
> - Attack on safety function = SAFETY FAILURE
>
> **2. Privacy impact:**
> - Vehicles collect location, driving behavior, personal data
> - GDPR and privacy regulations
> - Data breach liability
>
> **3. Business impact:**
> - Recalls (1.4M Jeep vehicles)
> - Brand reputation damage
> - Legal liability
>
> **4. Regulatory drivers:**
> - **UN R155 (Cybersecurity)**: Mandatory for new vehicle types (2024+)
> - **UN R156 (Software Updates)**: Mandatory for OTA updates
> - **SAE J3061**: Cybersecurity guidebook
> - **ISO/SAE 21434**: Automotive cybersecurity standard (2021)
>
> **The convergence of safety and security:**
> - Cybersecurity vulnerability can CAUSE safety hazard
> - Example: Disable AEB via remote exploit → Collision
> - ISO 26262 + ISO 21434 must be integrated
>
> This is why we need **systematic cybersecurity engineering** - not just penetration testing."

##### Slide 17: ISO/SAE 21434 - Automotive Cybersecurity Standard
**Visual:** ISO 21434 process overview and lifecycle
**Instructor Script:**
> "**ISO/SAE 21434** (published 2021) is to cybersecurity what ISO 26262 is to functional safety.
>
> **Cybersecurity Engineering Lifecycle:**
>
> **1. Concept Phase:**
> - **Asset identification**: What are we protecting? (Data, functions, vehicle control)
> - **Threat modeling**: What attacks are possible? (STRIDE, attack trees)
> - **Risk assessment**: TARA (Threat Analysis and Risk Assessment)
> - **Cybersecurity goals**: What must be protected and to what level?
>
> **2. Product Development:**
> - **Cybersecurity requirements**: Derived from cybersecurity goals
> - **Design**: Security architecture, defense-in-depth
> - **Implementation**: Secure coding, cryptography, key management
> - **Verification**: Penetration testing, fuzz testing, vulnerability scanning
>
> **3. Production:**
> - Secure manufacturing (prevent supply chain attacks)
> - Key injection and provisioning
>
> **4. Operations:**
> - Vulnerability monitoring (CVE databases)
> - Incident response
> - Security updates (OTA)
>
> **5. Decommissioning:**
> - Secure data deletion
> - Certificate revocation
>
> **Key concepts:**
>
> **CAL (Cybersecurity Assurance Level):**
> - Similar to ASIL for safety
> - CAL 1 (low) → CAL 4 (high)
> - Determined by attack feasibility and impact
> - Higher CAL = more rigorous security measures
>
> **TARA (Threat Analysis and Risk Assessment):**
> - Parallel to HARA for safety
> - Identify assets → Threats → Attack paths → Risk rating → Cybersecurity goals
>
> Let me show you how TARA works."

##### Slide 18: TARA - Threat Analysis and Risk Assessment
**Visual:** TARA process flow with ACC/AEB example
**Instructor Script:**
> "**TARA** is the cybersecurity equivalent of HARA. It identifies threats and determines required security levels.
>
> **TARA Process (5 steps):**
>
> **Step 1: Asset Identification**
> - **Assets**: What has value and must be protected?
>
> **Example (ACC/AEB system):**
> - **Asset 1**: Vehicle control (braking, acceleration)
> - **Asset 2**: Driver personal data (location, routes, behavior)
> - **Asset 3**: Vehicle identity (VIN, authentication credentials)
> - **Asset 4**: Software/firmware integrity
>
> **Step 2: Threat Scenario Identification**
> - Use **STRIDE** model or attack libraries
>
> **STRIDE Model:**
> - **S**poofing (fake identity)
> - **T**ampering (modify data/code)
> - **R**epudiation (deny actions)
> - **I**nformation disclosure (data leak)
> - **D**enial of service (make unavailable)
> - **E**levation of privilege (gain unauthorized access)
>
> **Example threats for ACC:**
> - **T1**: Spoof radar sensor data (S - Spoofing)
> - **T2**: Tamper with ECU software to disable AEB (T - Tampering)
> - **T3**: Intercept and modify CAN messages (T - Tampering)
> - **T4**: Denial of service on brake control (D - DoS)
> - **T5**: Extract encryption keys from ECU (I - Information disclosure)
>
> **Step 3: Attack Path Analysis**
> - How can attacker achieve threat?
> - **Attack vector**: Entry point (cellular, OBD-II, Bluetooth, etc.)
> - **Attack feasibility**: How difficult?
>
> **Example (T2: Tamper with ECU software):**
> - **Attack path**:
>   1. Exploit vulnerability in infotainment system (cellular connection)
>   2. Pivot to internal vehicle network (CAN bus)
>   3. Send malicious CAN messages to ACC ECU
>   4. Exploit buffer overflow in ECU to inject code
>   5. Modify safety-critical braking function
>
> **Attack Feasibility Rating (per ISO 21434):**
> - **Elapsed time**: Minutes to months
> - **Specialist expertise**: Layman to expert
> - **Knowledge of system**: Public to confidential
> - **Window of opportunity**: Unlimited to limited
> - **Equipment**: Standard to bespoke
>
> **Feasibility**: Very High / High / Medium / Low / Very Low
>
> **Step 4: Impact Rating**
> - **Safety impact**: Could cause injury/death? (S0-S3, like HARA)
> - **Financial impact**: Cost of attack
> - **Operational impact**: Vehicle unusable?
> - **Privacy impact**: Data exposure
>
> **Step 5: Risk Determination**
> - Combine **Attack Feasibility** + **Impact**
> - Result: **CAL (Cybersecurity Assurance Level)** 1-4
>
> **Risk Matrix (simplified):**
>
> | Impact | Attack Feasibility | CAL |
> |--------|--------------------|-----|
> | Severe (Safety) | High | **CAL 4** |
> | Severe (Safety) | Medium | CAL 3 |
> | Major (Operational) | High | CAL 3 |
> | Moderate | Medium | CAL 2 |
> | Minor | Low | CAL 1 |
>
> **Example TARA for ACC:**
>
> | Threat ID | Threat | Attack Feasibility | Impact | CAL | Cybersecurity Goal |
> |-----------|--------|--------------------|--------|-----|---------------------|
> | T1 | Spoof radar sensor data | Medium (requires RF equipment) | Severe (false braking or no braking) | **CAL 3** | CG-1: Protect sensor data integrity |
> | T2 | Tamper with ECU software | High (remote via cellular) | Severe (disable AEB) | **CAL 4** | CG-2: Prevent unauthorized software modification |
> | T3 | Modify CAN messages | High (access via OBD-II) | Severe (vehicle control) | **CAL 4** | CG-3: Authenticate and protect CAN messages |
> | T4 | DoS on brake control | Medium (requires CAN access) | Severe (loss of braking) | **CAL 3** | CG-4: Ensure availability of safety functions |
> | T5 | Extract encryption keys | Low (requires physical access + expert) | Major (enables other attacks) | CAL 2 | CG-5: Protect cryptographic material |
>
> **From cybersecurity goals to requirements (like safety):**
>
> **CG-2: Prevent unauthorized software modification [CAL 4]**
> → **CSR-2.1**: 'ECU shall implement secure boot with cryptographic verification of firmware integrity'
> → **CSR-2.2**: 'Software updates shall be authenticated using asymmetric cryptography (RSA-2048 or ECC-256)'
> → **CSR-2.3**: 'ECU shall detect tampering attempts and enter secure mode within 500ms'
>
> **Key takeaway:**
> TARA provides systematic framework to identify threats, assess risk, and determine cybersecurity requirements - parallel to HARA for safety."

##### Slide 19: Cybersecurity Architecture - Defense in Depth
**Visual:** Layered security architecture diagram for automotive system
**Instructor Script:**
> "The key principle of cybersecurity architecture is **Defense in Depth** - multiple layers of protection.
>
> **Layered Security Architecture for Automotive:**
>
> **Layer 1: Perimeter Security**
> - **Goal**: Prevent unauthorized external access
> - **Mechanisms**:
>   - Firewall between external interfaces (cellular, WiFi) and vehicle network
>   - Intrusion Detection System (IDS) monitoring network traffic
>   - Whitelisting of allowed communication patterns
> - **Example**: Gateway ECU filters all external-to-CAN traffic
>
> **Layer 2: Network Security**
> - **Goal**: Protect communication between ECUs
> - **Mechanisms**:
>   - Network segmentation (separate safety-critical from infotainment)
>   - Message Authentication Code (MAC) on CAN messages
>   - End-to-End (E2E) protection (crypto + sequence counter)
>   - Encrypted communication for sensitive data
> - **Example**: ACC ECU verifies MAC on all received CAN messages
>
> **Layer 3: ECU Security**
> - **Goal**: Protect individual ECUs from compromise
> - **Mechanisms**:
>   - **Secure boot**: Verify firmware integrity before execution (cryptographic signature)
>   - **Runtime integrity**: Monitor for code tampering
>   - **Memory protection**: Isolate safety-critical code (MPU - Memory Protection Unit)
>   - **Secure storage**: Encrypted key storage (HSM - Hardware Security Module)
> - **Example**: ACC ECU uses secure boot - won't execute unsigned firmware
>
> **Layer 4: Application Security**
> - **Goal**: Prevent exploitation of software vulnerabilities
> - **Mechanisms**:
>   - **Secure coding**: MISRA C, buffer overflow protection
>   - **Input validation**: Sanitize all external inputs
>   - **Least privilege**: Functions run with minimum necessary permissions
>   - **Sandboxing**: Isolate untrusted code
> - **Example**: Radar processing validates all sensor data ranges before use
>
> **Layer 5: Data Security**
> - **Goal**: Protect confidential and personal data
> - **Mechanisms**:
>   - Encryption at rest (stored data)
>   - Encryption in transit (transmitted data)
>   - Access control (who can read what)
>   - Data anonymization
> - **Example**: Driver location data encrypted using AES-256
>
> **Layer 6: Monitoring and Response**
> - **Goal**: Detect attacks and respond
> - **Mechanisms**:
>   - **IDS (Intrusion Detection)**: Detect anomalous behavior
>   - **Logging**: Record security events
>   - **Incident response**: Automated reaction to attacks
>   - **OTA updates**: Patch vulnerabilities
> - **Example**: Vehicle logs all authentication failures, reports to cloud for analysis
>
> **Real Architecture Example - ACC/AEB System:**
>
> ```
> External Interface (Cellular/WiFi)
>     ↓
> [Firewall/IDS in Gateway ECU] ← Layer 1
>     ↓
> CAN Bus with MAC/E2E ← Layer 2
>     ↓
> [ACC ECU with Secure Boot + HSM] ← Layer 3
>     ↓
> [Safety-Critical Software with Input Validation] ← Layer 4
>     ↓
> [Encrypted Data Storage] ← Layer 5
>     ↓
> [Anomaly Detection + Logging] ← Layer 6
> ```
>
> **Security Mechanisms Mapped to CAL:**
>
> **CAL 4** (highest): All 6 layers required
> - Secure boot + HSM mandatory
> - E2E protection on all messages
> - Independent security monitoring
> - Penetration testing by external experts
>
> **CAL 3**: Layers 1-5 required
> - Secure boot recommended
> - MAC on critical messages
> - Code review and static analysis
>
> **CAL 2**: Layers 1-4 required
> - Basic authentication
> - Input validation
>
> **CAL 1**: Layers 1-3 required
> - Basic firewall
> - Standard secure coding
>
> **Integration with Safety:**
> - Safety-critical functions (ASIL D) typically also CAL 3-4
> - Security failure → Safety failure
> - Example: If attacker disables AEB (security breach), collision occurs (safety hazard)
> - **ASIL D + CAL 4 = Maximum rigor**
>
> **Key principle:**
> No single layer is perfect - assume each can be breached. Defense in depth ensures attacker must breach MULTIPLE layers."

---

#### **Part 4: Interoperability Engineering** (Slides 20-21, ~8 minutes)

##### Slide 20: Interoperability - Connecting Systems Safely
**Visual:** Connected vehicle ecosystem diagram
**Instructor Script:**
> "Modern vehicles don't operate in isolation - they're part of a complex ecosystem. **Interoperability** is the ability of systems to work together.
>
> **The Interoperability Challenge:**
>
> **Internal interoperability** (within vehicle):
> - 100+ ECUs from multiple suppliers
> - Different communication protocols (CAN, LIN, FlexRay, Ethernet)
> - Mixed criticality (ASIL D + QM on same network)
> - Different update cycles (infotainment changes yearly, powertrain lasts 10+ years)
>
> **External interoperability** (beyond vehicle):
> - **V2V (Vehicle-to-Vehicle)**: Collision avoidance, platooning
> - **V2I (Vehicle-to-Infrastructure)**: Traffic lights, road signs, tolling
> - **V2P (Vehicle-to-Pedestrian)**: Smartphone detection
> - **V2N (Vehicle-to-Network)**: Cloud services, OTA updates
> - Collectively: **V2X (Vehicle-to-Everything)**
>
> **Interoperability Requirements:**
>
> **1. Protocol Compatibility**
> - Standards-based communication (IEEE 802.11p, C-V2X, DSRC)
> - Consistent message formats (SAE J2735 for V2X messages)
>
> **2. Semantic Interoperability**
> - Same meaning of data across systems
> - Example: What is 'vehicle speed'? GPS speed? Wheel speed? CAN speed?
> - Coordinate systems: Different ECUs may use different reference frames
>
> **3. Timing and Synchronization**
> - Critical for distributed control
> - Example: Sensor fusion requires synchronized timestamps
> - IEEE 1588 (Precision Time Protocol) for automotive Ethernet
>
> **4. Security Interoperability**
> - Trust across organizations (OEM ↔ Infrastructure provider)
> - PKI (Public Key Infrastructure) for authentication
> - Certificate management (issuance, revocation, renewal)
>
> **5. Safety Interoperability**
> - Fail-safe behavior across systems
> - Example: If V2I signal is lost, vehicle must degrade gracefully
>
> **Real-world example - V2X for Emergency Braking:**
>
> **Scenario**: Lead vehicle emergency brakes, sends V2V alert
>
> **Interoperability requirements:**
> - **Protocol**: Both vehicles use same V2V protocol (C-V2X)
> - **Message**: Standard 'Emergency Electronic Brake Lights' message (SAE J2735)
> - **Timing**: Message received within 100ms (latency requirement)
> - **Security**: Message authenticated (prevent spoofing)
> - **Safety**: Receiving vehicle verifies with onboard sensors (defense in depth)
> - **Human factors**: Driver alerted appropriately (avoid distraction)
>
> **Standards enabling interoperability:**
> - **SAE J2735**: Message set dictionary for V2X
> - **SAE J2945**: Dedicated Short Range Communications (DSRC) applications
> - **3GPP C-V2X**: Cellular V2X communication
> - **ISO 20077**: Extended Vehicle (ExVe) - standardized data exchange
> - **AUTOSAR**: Standardized software architecture for ECUs
>
> **Challenges:**
> - **Fragmentation**: Different regions use different standards (US vs EU vs China)
> - **Legacy compatibility**: New vehicles must work with old infrastructure
> - **Graceful degradation**: System must work even if interoperability fails
>
> **Key design principle:**
> - **Don't rely solely on external systems for safety**
> - Example: V2V alert is supplementary; onboard sensors are primary
> - This is defense in depth applied to interoperability"

##### Slide 21: AUTOSAR - Automotive Open System Architecture
**Visual:** AUTOSAR layered architecture diagram
**Instructor Script:**
> "**AUTOSAR** (Automotive Open System Architecture) is a key enabler of interoperability within vehicles.
>
> **What is AUTOSAR?**
> - Standardized software architecture for automotive ECUs
> - Developed by OEMs and suppliers (partnership)
> - Goal: Portability, reusability, interoperability
>
> **AUTOSAR Layered Architecture:**
>
> **Layer 1: Application Layer**
> - Software components (SWCs)
> - Business logic (e.g., cruise control algorithm)
> - **Standardized interfaces** (ports)
>
> **Layer 2: Runtime Environment (RTE)**
> - Communication abstraction
> - SWCs communicate via RTE (don't know about hardware)
>
> **Layer 3: Basic Software (BSW)**
> - **Services**: Operating system, communication, diagnostics, memory
> - **ECU Abstraction**: Hides hardware details
> - **Microcontroller Abstraction**: Driver layer
>
> **Layer 4: Microcontroller**
> - Hardware (CPU, peripherals)
>
> **Benefits for interoperability:**
>
> **1. Supplier independence:**
> - SWCs are portable across different ECU hardware
> - Example: ACC algorithm from Supplier A runs on ECU from Supplier B
>
> **2. Standardized communication:**
> - CAN, LIN, FlexRay, Ethernet handled by BSW
> - Application layer doesn't need to know protocol details
>
> **3. Configuration over coding:**
> - System integration via configuration files (ARXML)
> - Less error-prone than manual coding
>
> **4. Diagnostics and calibration:**
> - Standardized diagnostic services (UDS - Unified Diagnostic Services)
> - Standardized calibration interfaces (XCP, CCP)
>
> **AUTOSAR for Safety (AUTOSAR Safety Extensions):**
> - **E2E protection**: End-to-end communication safety
> - **Timing protection**: OS-level monitoring of task execution
> - **Memory protection**: MPU configuration
> - Supports ISO 26262 compliance
>
> **AUTOSAR Adaptive (for high-performance ECUs):**
> - Service-oriented architecture (SOA)
> - Dynamic configuration
> - POSIX OS (e.g., Linux)
> - For ADAS, autonomous driving, high-performance compute
>
> **Real impact:**
> - Without AUTOSAR: Every OEM-supplier pair has custom integration (N×M problem)
> - With AUTOSAR: Standardized interfaces (N+M problem)
> - **Reduces integration effort by orders of magnitude**
>
> **Interoperability enabled:**
> - ECUs from different suppliers work together
> - Software reusable across vehicle platforms
> - Faster time-to-market, lower cost
>
> AUTOSAR is foundational to modern automotive systems engineering - not just for interoperability, but for managing complexity."

---

#### **Part 5: Human Factors Engineering** (Slides 22-23, ~8 minutes)

##### Slide 22: Human Factors - Designing for Real Humans
**Visual:** Examples of good vs poor automotive HMI design
**Instructor Script:**
> "We've engineered safety and security. But if humans can't use the system correctly, all that engineering is wasted.
>
> **Human Factors Engineering** (also called Ergonomics or Human-Machine Interface design) ensures systems are:
> - **Usable**: Humans can operate them effectively
> - **Safe**: Humans don't make dangerous errors
> - **Efficient**: Humans can perform tasks quickly
> - **Satisfying**: Users have positive experience
>
> **Why human factors matter in automotive:**
>
> **Failure cases:**
> - **Tesla Autopilot crashes**: Drivers misunderstood automation level (thought it was Level 4 when it's Level 2)
> - **NHTSA study**: 94% of crashes involve human error
> - **Toyota unintended acceleration**: Pedal misapplication (human error) + poor floor mat design (design error)
>
> **The challenge:**
> - Drivers have **limited attention**
> - Drivers have **limited training** (no engineering degree required!)
> - Drivers operate under **stress** (emergencies)
> - Drivers have **diverse capabilities** (young, elderly, disabled)
> - Drivers **over-trust** automation (complacency)
> - Drivers **under-trust** automation (disuse)
>
> **Key human factors principles for automotive:**
>
> **1. Situational Awareness**
> - Driver must understand system state at all times
> - **Example**: Is ACC active? What speed is set? Is AEB enabled?
> - **Design**: Clear visual indicators, consistent location
>
> **2. Mode Confusion Prevention**
> - Different modes must be visually distinct
> - **Bad example**: Autopilot icon looks similar whether active or standby
> - **Good example**: Active = green border + animation, Inactive = gray icon
>
> **3. Attention Management**
> - Don't overload driver with information
> - Prioritize critical information
> - **Example**: Collision warning gets central display + sound + haptic, non-critical info on side screen
>
> **4. Affordances and Mappings**
> - Controls should suggest their function
> - **Example**: Steering wheel buttons for speed control (intuitive location)
> - **Bad example**: Touchscreen-only controls (no tactile feedback, requires looking away)
>
> **5. Error Tolerance**
> - System should prevent/recover from human errors
> - **Example**: If driver accidentally presses SET while speeding, system limits to legal maximum
> - **Example**: Confirmation required for critical actions
>
> **6. Feedback and Transparency**
> - System provides clear feedback for user actions
> - **Example**: Audible beep when cruise speed is set, visual confirmation on display
>
> Let me show you specific examples."

##### Slide 23: Human Factors Analysis - Automation Levels
**Visual:** SAE J3016 automation levels with human factors considerations
**Instructor Script:**
> "One of the most critical human factors issues in modern automotive: **Understanding automation levels.**
>
> **SAE J3016 - Levels of Driving Automation:**
>
> **Level 0 - No Automation**
> - Human does everything
> - Human factors: Traditional vehicle ergonomics
>
> **Level 1 - Driver Assistance**
> - System: Either steering OR speed control (not both)
> - Example: Traditional cruise control, lane keeping assist
> - Human: Monitors environment, ready to take over immediately
> - **Human factors challenge**: Knowing when system is active
>
> **Level 2 - Partial Automation**
> - System: Both steering AND speed control simultaneously
> - Example: Tesla Autopilot, GM Super Cruise, ACC with lane centering
> - Human: MUST monitor environment constantly, hands on wheel
> - **Human factors challenge**: Over-reliance, distraction, 'it's driving itself' misconception
> - **Critical requirement**: Driver monitoring system (camera watching driver)
>
> **Level 3 - Conditional Automation**
> - System: Full driving in specific conditions (e.g., highway traffic jam)
> - Human: Can disengage (look at phone) but must respond to takeover request
> - Example: Audi A8 Traffic Jam Pilot (limited deployment)
> - **Human factors challenge**: Transition time - how long does driver need to regain situational awareness?
> - **Design requirement**: Minimum takeover time (typically 10+ seconds)
>
> **Level 4 - High Automation**
> - System: Full driving in defined conditions, no human intervention needed
> - Human: Passenger (can sleep)
> - Fallback: System handles emergencies (e.g., pulls over safely)
> - Example: Waymo robotaxis (geo-fenced areas)
> - **Human factors challenge**: What happens at boundary of operational design domain (ODD)?
>
> **Level 5 - Full Automation**
> - System: Drives anywhere, anytime
> - Human: Just a passenger
> - **Not yet available**
>
> **The Level 2-3 Transition Problem:**
>
> **Level 2**: Driver MUST monitor constantly
> **Level 3**: Driver CAN disengage but must respond to takeover
>
> **Human factors issue:**
> - Humans are TERRIBLE at vigilance tasks (monitoring with no action)
> - After 10-20 minutes of no intervention, driver attention drifts
> - Studies show takeover performance degrades severely after distraction
>
> **Design solutions:**
> - **Driver monitoring**: Eye tracking, head position, steering wheel sensors
> - **Escalating warnings**: Visual → Audible → Haptic (seat vibration) → Automatic pullover
> - **Clear mode indication**: Large, central, unambiguous display of automation level
> - **Training**: Educate drivers on system capabilities and limitations
>
> **Real example - GM Super Cruise:**
> - Level 2 system
> - **Human factors engineering:**
>   - Eye tracking camera on steering column (monitors driver attention)
>   - Light bar on steering wheel (green = hands-free OK, red = hands required)
>   - Escalating alerts if driver not attending
>   - Automatic pullover if driver unresponsive
>   - Geo-fenced to mapped highways only (clear ODD)
>   - Name avoids 'autopilot' misconception
>
> **Key human factors requirements for ADAS:**
>
> **1. Mode awareness:**
> - REQ-HF-01: 'System shall display automation level on primary instrument cluster with ≥99% visibility'
>
> **2. Attention management:**
> - REQ-HF-02: 'Level 2 system shall monitor driver attention with ≤2s detection latency'
> - REQ-HF-03: 'System shall issue escalating alerts if driver attention not detected for >5s'
>
> **3. Takeover performance:**
> - REQ-HF-04: 'System shall provide ≥10s warning before requiring driver takeover'
> - REQ-HF-05: 'Takeover request shall use multi-modal alert (visual + audible + haptic)'
>
> **4. Transparency:**
> - REQ-HF-06: 'System shall explain limitations and operational design domain in owner's manual and in-vehicle tutorial'
>
> **5. Error tolerance:**
> - REQ-HF-07: 'If driver fails to respond to takeover request, system shall execute safe stop maneuver'
>
> **Human factors engineering is NOT an afterthought - it must be integrated from concept phase.**
>
> NHTSA and Euro NCAP now include human factors assessment in safety ratings."

---

#### **Part 6: Integration - Bringing It All Together** (Slide 24, ~4 minutes)

##### Slide 24: Integrated Specialty Engineering Process
**Visual:** Process flow showing integration of safety, security, interoperability, and human factors
**Instructor Script:**
> "We've covered safety, security, interoperability, and human factors. In practice, these MUST be integrated - not siloed.
>
> **The Integrated Specialty Engineering Process:**
>
> **Concept Phase (Parallel Activities):**
> - **Safety**: HARA → Safety goals → ASIL classification
> - **Security**: TARA → Cybersecurity goals → CAL classification
> - **Interoperability**: Identify interfaces, define standards compliance
> - **Human factors**: User research, task analysis, use cases
>
> **Integration point**: Identify conflicts
> - Example: Security encryption adds latency → May impact safety real-time requirement
> - Example: Safety requires redundant sensors → Interoperability challenge (sensor fusion)
>
> **System Design (Unified Architecture):**
> - **Safety architecture**: Redundancy, fail-safe, safety mechanisms
> - **Security architecture**: Defense in depth, secure boot, E2E protection
> - **Interoperability architecture**: Standard interfaces, AUTOSAR, V2X protocols
> - **Human factors**: HMI design, automation level, driver monitoring
>
> **Integration point**: Shared components
> - Example: Gateway ECU handles BOTH safety (CAN routing) AND security (firewall)
> - Example: Driver display shows BOTH safety status (AEB active) AND security status (OTA update)
>
> **Requirements Development:**
> - Safety requirements (FSR with ASIL)
> - Security requirements (CSR with CAL)
> - Interoperability requirements (protocol compliance)
> - Human factors requirements (usability, mode awareness)
>
> **Integration point**: Traceability
> - All specialty requirements trace to system requirements (Session 4)
> - RTM includes ASIL + CAL columns
>
> **Verification and Validation:**
> - **Safety V&V**: Fault injection, ASIL-specific testing, independent assessment
> - **Security V&V**: Penetration testing, fuzz testing, vulnerability scanning
> - **Interoperability V&V**: Protocol conformance testing, plugfests
> - **Human factors V&V**: Usability testing, cognitive workload assessment, driver-in-loop simulation
>
> **Integration point**: Combined scenarios
> - Example: Test scenario with sensor failure (safety) during cyberattack (security) with distracted driver (human factors)
>
> **Real example - ACC with AEB System:**
>
> **Integrated requirements:**
> - **FR-ACC-001**: 'System shall maintain following distance of 1.0-2.5s' [Functional]
> - **FSR-ACC-005**: 'System shall detect sensor failure within 100ms' [Safety, ASIL D]
> - **CSR-ACC-010**: 'System shall authenticate radar sensor data using MAC' [Security, CAL 3]
> - **IOP-ACC-015**: 'System shall use SAE J2735 message format for V2V communication' [Interoperability]
> - **HF-ACC-020**: 'System shall display ACC status with ≥10mm icon height in primary view' [Human Factors]
>
> **Integrated architecture:**
> ```
> Radar Sensor (with authentication) ← Security
>     ↓ (E2E protected CAN) ← Safety + Security
> [ACC ECU with secure boot + dual-core lockstep] ← Security + Safety
>     ↓ (Plausibility check + Watchdog) ← Safety
> [Brake ECU] ← Safety
>     ↓
> [Driver Display + Monitoring] ← Human Factors
> ```
>
> **Integrated testing:**
> - Inject sensor spoofing attack (security) → Verify plausibility check detects (safety) → Verify driver alert (human factors)
>
> **Standards supporting integration:**
> - **ISO 26262** (safety) has cybersecurity considerations annex
> - **ISO 21434** (security) has safety interaction guidelines
> - **ISO 20077** (extended vehicle) addresses interoperability
> - **ISO 26262-8** includes human factors in supporting processes
>
> **Key takeaway:**
> Specialty engineering is NOT separate departments working independently. It's an INTEGRATED discipline where safety, security, interoperability, and human factors must be co-designed from day one.
>
> This is systems engineering in practice."

---

### **CLIMAX: Real-World Integration Case Study** (Slides 25-26, ~8 minutes)

#### Slide 25: Case Study - Designing a Secure, Safe, Usable ACC System
**Visual:** End-to-end case study flow
**Instructor Script:**
> "Let's walk through a complete example integrating everything we've learned.
>
> **Project**: Design an Adaptive Cruise Control (ACC) system with Automatic Emergency Braking (AEB) for a passenger vehicle.
>
> **Step 1: Hazard and Threat Analysis (Parallel)**
>
> **HARA (Safety):**
> - Hazard: 'Failure to brake for stopped vehicle' → ASIL D
> - Hazard: 'Unintended braking at high speed' → ASIL C
> - Hazard: 'Insufficient braking force' → ASIL B
>
> **TARA (Security):**
> - Threat: 'Remote attacker disables AEB' → CAL 4
> - Threat: 'Attacker spoofs radar sensor' → CAL 3
> - Threat: 'Attacker causes false braking' → CAL 3
>
> **Human Factors Analysis:**
> - Use case: Highway driving, driver partially attentive (Level 2)
> - Risk: Driver over-relies on system, doesn't monitor
> - Risk: Driver doesn't understand when system is active
>
> **Interoperability Analysis:**
> - Interface: CAN bus to brake ECU (existing vehicle network)
> - Interface: V2V communication (future capability)
> - Constraint: Must work with existing vehicle architecture
>
> **Step 2: Goals and Requirements**
>
> **Safety Goal [ASIL D]:**
> - SG-ACC-01: 'Prevent collision with stopped or slow-moving vehicle ahead'
>
> **Cybersecurity Goal [CAL 4]:**
> - CG-ACC-01: 'Prevent unauthorized modification of braking function'
>
> **Human Factors Goal:**
> - HFG-ACC-01: 'Enable driver to maintain situational awareness of system state and limitations'
>
> **Interoperability Goal:**
> - IOP-ACC-01: 'Integrate with existing vehicle CAN network without disrupting other functions'
>
> **Derived Requirements (integrated):**
>
> **Detection & Decision:**
> - REQ-ACC-010: 'System shall detect stopped vehicles at ≥150m with 99.9% probability' [ASIL D, Functional]
> - REQ-ACC-011: 'Radar sensor data shall be authenticated using AES-128 MAC' [CAL 4, Security]
> - REQ-ACC-012: 'System shall use sensor fusion (radar + camera) with diverse algorithms' [ASIL D, Safety]
>
> **Braking:**
> - REQ-ACC-020: 'System shall command braking within 200ms of detecting collision risk' [ASIL D, Safety]
> - REQ-ACC-021: 'Brake commands shall use E2E protection per AUTOSAR' [ASIL D + CAL 3, Safety + Security]
>
> **Fail-Safe:**
> - REQ-ACC-030: 'Upon sensor failure, system shall transition to safe state within 300ms' [ASIL D, Safety]
> - REQ-ACC-031: 'System shall detect firmware tampering at boot using secure boot' [CAL 4, Security]
>
> **Driver Interface:**
> - REQ-ACC-040: 'System shall display ACC status on instrument cluster with ≥12mm icon' [Human Factors]
> - REQ-ACC-041: 'System shall monitor driver eye gaze every 500ms' [Level 2, Human Factors]
> - REQ-ACC-042: 'If driver not attending for >10s, system shall issue escalating alerts' [Safety + Human Factors]
>
> **Interoperability:**
> - REQ-ACC-050: 'System shall communicate via CAN FD at 2 Mbps per ISO 11898-1' [Interoperability]
> - REQ-ACC-051: 'System shall support future V2V using SAE J2735 message set' [Interoperability]
>
> **Step 3: Architecture (Integrated)**
>
> ```
> [External: V2V (future)] ← Interoperability
>     ↓
> [Gateway ECU with Firewall + IDS] ← Security Layer 1
>     ↓
> [CAN FD Bus with E2E Protection] ← Safety + Security Layer 2
>     ↓
> ┌─────────────────────────────────────┐
> │ ACC ECU (ASIL D + CAL 4)            │ ← Integrated Safety + Security
> │ - Dual-core lockstep CPU            │ ← Safety (ASIL D)
> │ - HSM (Hardware Security Module)    │ ← Security (CAL 4)
> │ - Secure Boot                        │ ← Security (CAL 4)
> │ - Watchdog Timer                     │ ← Safety (ASIL D)
> │ - Sensor Fusion Algorithm (diverse) │ ← Safety (ASIL D)
> │ - Plausibility Checks                │ ← Safety + Security
> └─────────────────────────────────────┘
>     ↓ (authenticated messages)
> [Radar Sensor] [Camera Sensor] ← Safety (redundancy)
>     ↓
> [Brake ECU] ← Safety (ASIL D)
>     ↓
> ┌─────────────────────────────────────┐
> │ Driver Interface                     │ ← Human Factors
> │ - Instrument Cluster (ACC status)    │
> │ - Eye Tracking Camera                │
> │ - Audible + Haptic Alerts            │
> └─────────────────────────────────────┘
> ```
>
> **Step 4: Verification (Integrated Testing)**
>
> **Safety Testing:**
> - Fault injection: Simulate sensor failures, verify safe state transition
> - Edge cases: Test at ASIL D coverage (MC/DC code coverage)
> - Independent assessment: External safety auditor
>
> **Security Testing:**
> - Penetration testing: Try to remotely disable AEB
> - Fuzz testing: Send malformed CAN messages, verify robustness
> - Secure boot verification: Attempt to load unsigned firmware
>
> **Interoperability Testing:**
> - CAN conformance: Verify message timing, format per ISO 11898
> - Integration testing: Test with actual brake ECU from vehicle
>
> **Human Factors Testing:**
> - Usability study: 50 drivers, measure comprehension of system state
> - Cognitive workload: Assess driver attention during ACC operation
> - Takeover testing: Measure response time to alerts
>
> **Integrated Scenario Testing:**
> - Scenario: Cyberattack attempts to spoof radar sensor (security) during actual stopped vehicle ahead (safety) with distracted driver (human factors)
> - **Expected result**:
>   1. MAC verification detects spoofed data (security defense)
>   2. Plausibility check flags inconsistency (safety + security)
>   3. Camera sensor provides redundant detection (safety)
>   4. System brakes based on camera data (safety)
>   5. Driver monitoring detects inattention, issues alert (human factors)
>   6. Attack logged for incident response (security)
>
> **This is integrated specialty engineering in action - safety, security, interoperability, and human factors working together, not in silos.**"

#### Slide 26: Lessons Learned - Specialty Engineering Best Practices
**Visual:** Checklist and key principles
**Instructor Script:**
> "Let me give you the professional's checklist for specialty engineering excellence:
>
> **Safety Engineering Best Practices:**
>
> ✓ **Start early**: HARA in concept phase, not after design is done
> ✓ **Use multiple methods**: FTA + FMEA + HAZOP are complementary
> ✓ **Involve experts**: Cross-functional teams (safety, design, testing)
> ✓ **Trace everything**: Hazard → Safety goal → FSR → TSR → Design → Test
> ✓ **Independent assessment**: External safety auditor for ASIL C/D
> ✓ **Document rationale**: Why this ASIL? Why this safety mechanism? (for audits)
> ✓ **Conservative assumptions**: When in doubt, choose higher ASIL
>
> **Security Engineering Best Practices:**
>
> ✓ **Threat model early**: TARA in concept phase
> ✓ **Defense in depth**: Never rely on single security measure
> ✓ **Secure by design**: Security is not a feature added later
> ✓ **Assume breach**: Design for what happens WHEN (not if) attacker gets in
> ✓ **Crypto correctly**: Use established libraries, don't invent crypto
> ✓ **Monitor and respond**: Security is ongoing (vulnerability monitoring, OTA updates)
> ✓ **Red team testing**: Hire hackers to attack your system
>
> **Interoperability Best Practices:**
>
> ✓ **Use standards**: Don't invent proprietary protocols
> ✓ **Design for evolution**: Systems will be updated at different rates
> ✓ **Graceful degradation**: Work even if interoperability fails
> ✓ **Conformance testing**: Test against reference implementations
> ✓ **Document interfaces**: Clear API specifications
>
> **Human Factors Best Practices:**
>
> ✓ **User research**: Observe real drivers, don't assume
> ✓ **Iterate**: Prototype → Test → Refine → Repeat
> ✓ **Diverse users**: Test with elderly, novice, expert, distracted drivers
> ✓ **Multi-modal feedback**: Visual + audible + haptic for critical alerts
> ✓ **Simplicity**: Complex interfaces lead to errors
> ✓ **Training**: Educate users on system capabilities and limitations
>
> **Integration Best Practices:**
>
> ✓ **Early integration**: Don't wait until end to integrate safety + security + HF
> ✓ **Unified architecture**: Single architecture addresses all specialty concerns
> ✓ **Shared traceability**: One RTM with ASIL, CAL, and HF requirements
> ✓ **Cross-discipline reviews**: Safety engineer reviews security design and vice versa
> ✓ **Integrated testing**: Test scenarios combining safety, security, and human factors
> ✓ **Regulatory alignment**: ISO 26262 + ISO 21434 + UN R155/156 + type approval
>
> **Common pitfalls to avoid:**
>
> ❌ **Safety without security**: Safe system can be made unsafe via cyberattack
> ❌ **Security without usability**: Users will circumvent security if it's too hard
> ❌ **Isolated disciplines**: Safety team doesn't talk to security team → gaps
> ❌ **Late integration**: Discovering conflicts at integration phase is expensive
> ❌ **Checkbox compliance**: Following standard without understanding why
> ❌ **Over-reliance on testing**: Testing doesn't prove absence of hazards (use analysis)
>
> **Remember:**
> - **Safety**: Prevents harm from malfunctions
> - **Security**: Prevents harm from malicious actors
> - **Interoperability**: Enables systems to work together
> - **Human Factors**: Ensures humans can use systems safely and effectively
>
> **All four are essential. None are optional.**
>
> These disciplines are what distinguish professional automotive systems engineers from amateurs."

---

### **RESOLUTION: Consolidation and Practice** (Slides 27-30, ~8 minutes + Q&A)

#### Slide 27: Key Takeaways
**Visual:** Summary with visual metaphors
**Instructor Script:**
> "Let's consolidate what you've learned today:
>
> **1. Safety Analysis Methods**
> - **FTA** (top-down): Start with hazard, find causes
> - **FMEA** (bottom-up): Start with components, find effects
> - **HAZOP**: Systematic deviation analysis
> - Use all three for comprehensive safety analysis
>
> **2. ISO 26262 and HARA**
> - HARA: Hazard + Situation → Severity + Exposure + Controllability → ASIL
> - ASIL (A-D) determines rigor of safety engineering
> - Safety goals → FSR → TSR → Implementation → Verification
> - Traceability is mandatory
>
> **3. Cybersecurity**
> - TARA: Assets → Threats → Attack paths → Risk → CAL
> - Defense in depth: Multiple layers of security
> - Security failure can cause safety failure
> - ISO 21434 provides systematic framework
>
> **4. Interoperability**
> - Modern vehicles are part of ecosystem (V2X)
> - Standards enable interoperability (AUTOSAR, SAE, ISO)
> - Design for graceful degradation
> - Interoperability ≠ safety (verify with onboard sensors)
>
> **5. Human Factors**
> - Design for real human capabilities and limitations
> - Automation levels (SAE J3016) have different human factors needs
> - Level 2: Driver monitoring essential
> - Mode awareness, attention management, error tolerance
>
> **6. Integration**
> - Safety + Security + Interoperability + Human Factors must be co-designed
> - Unified architecture and requirements
> - Integrated testing scenarios
>
> **Remember**: These specialty engineering disciplines are not bureaucracy - they are life-saving, systematic approaches that prevent disasters like Toyota unintended acceleration and Jeep Cherokee hacks."

#### Slide 28: Connection to Systems Engineering V-Model
**Visual:** V-Model with specialty engineering activities highlighted
**Instructor Script:**
> "Let's place specialty engineering in the systems engineering context.
>
> **Left side of V-Model (Development):**
>
> **Concept Phase:**
> - **Safety**: HARA, safety goals
> - **Security**: TARA, cybersecurity goals
> - **Human Factors**: User research, task analysis
> - **Interoperability**: Interface identification
>
> **System Requirements (Session 4):**
> - Integrate safety (FSR with ASIL), security (CSR with CAL), HF, and interoperability requirements
> - Traceability to hazards and threats
>
> **System Design (Session 5):**
> - Architecture addresses safety (redundancy, fail-safe), security (defense in depth), interoperability (standards), HF (interface design)
>
> **Implementation:**
> - Safety mechanisms, secure coding, AUTOSAR integration, HMI implementation
>
> **Right side of V-Model (Verification & Validation):**
>
> **Component Testing:**
> - Unit tests with safety and security coverage
>
> **Integration Testing:**
> - Interoperability testing, fault injection, penetration testing
>
> **System Testing:**
> - ASIL-specific testing, CAL-specific testing, usability testing
>
> **Validation:**
> - Prove safety goals met, cybersecurity goals met, user needs met
>
> **Throughout lifecycle (Session 9, 15):**
> - **Configuration management**: Baseline safety and security requirements
> - **Change management**: Impact analysis for safety and security
> - **Measurement**: Safety metrics (residual risk), security metrics (vulnerabilities found), HF metrics (usability scores)
>
> **Specialty engineering is NOT a separate process - it's integrated into the systems engineering lifecycle at every phase.**"

#### Slide 29: Connection to Other Sessions
**Visual:** Session map showing connections
**Instructor Script:**
> "Today's session connects to many others:
>
> **Builds on:**
> - **Session 1**: Failures (Therac-25, Toyota) were specialty engineering failures
> - **Session 4**: Requirements engineering - specialty requirements need extra rigor
> - **Session 8**: V&V - specialty engineering requires specialized verification
> - **Session 9**: Risk management and FMEA - HARA extends these concepts for safety
>
> **Leads to:**
> - **Session 13**: Life cycle cost analysis includes cost of safety/security failures
> - **Session 14**: Case study 2 will apply specialty engineering concepts
> - **Session 15**: Technical management includes safety and security configuration management
>
> **Integration points:**
> - **MBSE (Session 3)**: SysML has safety and security extensions
> - **Architecture (Session 5)**: Safety and security drive architecture decisions
> - **Quality (Session 10)**: Safety and security are quality attributes
> - **Agreements (Session 11)**: Supplier contracts must address safety and security responsibilities
>
> **Key concept thread:**
> - **Session 4**: WHAT requirements are needed (including safety/security)
> - **Session 9**: HOW to analyze risk (DFMEA → HARA)
> - **Session 12** (today): HOW to systematically engineer safety, security, interoperability, human factors
> - **Session 8**: HOW to verify specialty requirements
>
> Specialty engineering is foundational to modern automotive systems engineering."

#### Slide 30: Practice Exercise & Q&A
**Visual:** Exercise description
**Instructor Script:**
> "**Practical Exercise (Due before Session 13):**
>
> You are the systems engineer for a **Level 2 Autonomous Lane Keeping Assist (LKAS)** system for a highway vehicle.
>
> **Part 1: Safety Analysis (30%)**
> - Identify at least 5 hazards
> - Conduct HARA for each (Severity, Exposure, Controllability → ASIL)
> - For the highest ASIL hazard, create an FMEA table (minimum 5 failure modes)
> - Define safety goal and 3 functional safety requirements
>
> **Part 2: Security Analysis (25%)**
> - Identify at least 3 assets
> - Conduct TARA for at least 3 threats
> - Determine CAL for each threat
> - Define cybersecurity goal and 3 cybersecurity requirements
>
> **Part 3: Human Factors Analysis (25%)**
> - Define the automation level (per SAE J3016)
> - Identify 3 human factors risks (e.g., mode confusion, over-reliance)
> - Define 3 human factors requirements to mitigate these risks
> - Sketch HMI mockup showing system status
>
> **Part 4: Integration (20%)**
> - Create integrated architecture diagram showing safety mechanisms, security layers, and HMI
> - Create traceability matrix: Hazards/Threats → Goals → Requirements (Safety + Security + HF)
> - Define 1 integrated test scenario combining safety, security, and human factors
>
> **Grading Criteria:**
> - Correct application of HARA methodology
> - Correct application of TARA methodology
> - Quality of safety and security requirements (clear, verifiable, traced)
> - Human factors analysis depth
> - Integration and traceability
> - Professional formatting
>
> **Submission**:
> - Part 1: 2 pages (HARA table + FMEA + safety requirements)
> - Part 2: 1.5 pages (TARA table + security requirements)
> - Part 3: 1.5 pages (HF analysis + requirements + HMI sketch)
> - Part 4: 2 pages (Architecture diagram + traceability matrix + test scenario)
> - Total: 7 pages
>
> **Tips:**
> - Research real LKAS systems (Euro NCAP requirements, Tesla, GM Super Cruise)
> - Use ISO 26262 ASIL table correctly (don't guess S/E/C)
> - Consider realistic attack vectors (cellular, OBD-II, sensor spoofing)
> - Think about driver monitoring (how do you ensure driver is attentive?)
>
> **Discussion Questions:**
> - How would ASIL change if this was Level 3 (conditional automation) instead of Level 2?
> - What's the relationship between safety ASIL and security CAL for the same function?
> - How do you prevent drivers from over-relying on a Level 2 system?
> - What interoperability standards would be needed if this system used V2V data?
>
> **30 minutes for your questions.**"

---

## 📊 PPT DESIGN GUIDANCE

### Visual Style:
- **Professional safety/security aesthetic**: Clean, technical, serious tone
- **Color coding**:
  - Red for hazards and threats
  - Blue for safety measures and requirements
  - Green for security measures
  - Orange for human factors
  - Purple for integration points
- **Use real automotive examples**: Photos of ACC systems, HMI interfaces, attack demonstrations
- **Diagrams**: HARA tables, TARA tables, FTA/FMEA, architecture diagrams

### Key Slides to Emphasize:
1. **Slide 4** (Jeep Cherokee hack) - Real-world consequences
2. **Slide 9-11** (Safety analysis methods) - Core techniques
3. **Slide 13** (HARA process) - Foundation of ISO 26262
4. **Slide 18** (TARA process) - Foundation of ISO 21434
5. **Slide 19** (Defense in depth) - Security architecture
6. **Slide 23** (Automation levels + HF) - Critical for modern vehicles
7. **Slide 25** (Integrated case study) - Putting it all together
8. **Slide 27** (Summary) - Students will photograph this

### Animations:
- **Slide 9**: Build fault tree from top event downward
- **Slide 13**: Step-by-step HARA process with example values appearing
- **Slide 18**: Step-by-step TARA process
- **Slide 19**: Layer-by-layer defense in depth (reveal each layer sequentially)
- **Slide 24**: Integration flow showing parallel to convergence
- **Slide 25**: Case study flow with requirements appearing in stages

### Tables and Templates:
- **Slide 10**: FMEA table template (automotive example)
- **Slide 13**: ASIL determination table (ISO 26262)
- **Slide 14**: Complete HARA example (ACC system)
- **Slide 18**: TARA table with attack feasibility rating
- **Slide 25**: Integrated requirements table (ASIL + CAL columns)

### Real Examples to Include:
- Jeep Cherokee hack details (2015)
- Tesla Autopilot crashes (human factors)
- ISO 26262 ASIL table (actual standard)
- ISO 21434 attack feasibility table
- GM Super Cruise driver monitoring (good HF example)
- AUTOSAR architecture diagram
- SAE J3016 automation levels

---

## 🎯 INSTRUCTOR NOTES

### Pedagogical Strategy:
- **Start with real failure (Jeep hack), show systematic methods, return to how methods prevent failure**
- **Parallel structure**: Safety (HARA) and Security (TARA) taught in parallel to show similarities
- **Integration emphasis**: Constantly reinforce that these disciplines must work together
- **Industry standards focus**: ISO 26262, ISO 21434, SAE J3016 - use actual standards terminology
- **Hands-on mindset**: Students should be able to conduct HARA and TARA after today

### Common Student Challenges:

**Challenge 1: "Why do we need both safety AND security engineering?"**
**How to address:** Use Jeep Cherokee example - security breach CAUSED safety failure. Modern vehicles are connected, so security vulnerabilities create safety hazards. They are no longer separate concerns.

**Challenge 2: "HARA and TARA seem complicated - can't we just test more?"**
**How to address:** Testing can only find what you think to test. HARA/TARA systematically identify hazards/threats you didn't think of. Show Toyota example - inadequate hazard analysis led to missing critical failure modes. Analysis PRECEDES testing.

**Challenge 3: "How do I determine ASIL or CAL accurately?"**
**How to address:** Use ISO 26262 tables exactly as specified - don't guess. Severity, Exposure, Controllability have defined criteria. When uncertain, consult with safety experts, use conservative (higher) rating. Show worked examples (Slides 13-14).

**Challenge 4: "This seems like it adds a lot of development cost"**
**How to address:** Compare cost of HARA (maybe 40 hours of engineering time = $5K) vs cost of recall (1.4M vehicles = $1.4B). Prevention is 1000x cheaper than failure. Also, ISO 26262 and UN R155 are MANDATORY - not optional. Frame as risk reduction investment.

**Challenge 5: "How do safety and security requirements interact?"**
**How to address:** Use Slide 24 integrated example. Some requirements address both (e.g., E2E protection provides safety integrity AND security authentication). Some conflict (e.g., encryption latency vs real-time safety). Architecture must resolve conflicts through design (e.g., dedicated safety channel).

### Timing Flexibility:

**If running short:**
- Condense Slide 11 (HAZOP) - brief overview, details in reading
- Reduce Slide 20-21 (interoperability) to overview only
- Move some FMEA examples to backup slides

**If running long:**
- Extend Slide 25 (case study) with more detailed walkthrough
- Add live demo of HARA/TARA worksheet
- Show video of GM Super Cruise or Tesla Autopilot HMI

**Core content (must cover - non-negotiable):**
- Slides 8-10 (Safety analysis methods: FTA, FMEA)
- Slides 12-14 (ISO 26262 and HARA)
- Slides 16-18 (Cybersecurity and TARA)
- Slide 19 (Defense in depth)
- Slide 23 (Automation levels and human factors)
- Slide 25 (Integrated case study)
- Slide 27 (Summary)

### Engagement Points:

**Slide 4**: Ask "Has anyone experienced a software bug in a vehicle?" (normalize the issue)

**Slide 7**: Interactive - "What could go wrong with ACC?" - let students brainstorm hazards before showing analysis

**Slide 13**: Work through HARA together - give a hazard, have students rate S/E/C before revealing ASIL

**Slide 18**: Work through TARA together - identify attack path for one threat

**Slide 23**: Poll - "How many would trust Level 2 automation on a highway?" (segue to human factors discussion)

### Interactive Elements:

**Quick Exercise (Slide 14)**: Give students a new hazard for ACC (e.g., "Vehicle accelerates instead of braking"), have them determine S/E/C/ASIL in pairs (3 minutes), then discuss.

**Group Discussion (Slide 19)**: "If you could only implement 3 of the 6 security layers, which would you choose and why?" (trade-off thinking)

**Case Analysis (Slide 26)**: "What would you do differently in the Toyota case?" (apply lessons learned)

### Materials to Prepare:

**Before class:**
- [ ] ISO 26262-3 ASIL table (official or recreated)
- [ ] ISO 21434 attack feasibility table
- [ ] HARA worksheet template
- [ ] TARA worksheet template
- [ ] SAE J3016 summary (automation levels)
- [ ] Jeep Cherokee hack case study materials
- [ ] Example FMEA for automotive component

**Handouts:**
- [ ] HARA worksheet template (Excel/PDF)
- [ ] TARA worksheet template
- [ ] FTA symbols reference
- [ ] FMEA template
- [ ] SAE J3016 one-pager
- [ ] Defense in depth checklist

**Post-class:**
- [ ] Share slides
- [ ] Post exercise assignment with templates
- [ ] Post ISO 26262 and ISO 21434 overview documents
- [ ] Post links to UN R155 (cybersecurity regulation), UN R156 (software updates)
- [ ] Create discussion forum: "Share safety or security analysis examples"

### Assessment Opportunities:

**During lecture:**
- Quick quiz (Slide 14): "What ASIL would you assign to this hazard?"
- Quick quiz (Slide 18): "What's the attack feasibility for this threat?"

**Exercise assessment criteria:**
- HARA correctness (Did they apply S/E/C criteria correctly?)
- TARA correctness (Did they identify realistic threats and attack paths?)
- Requirements quality (Traceable to hazards/threats? Verifiable? Include ASIL/CAL?)
- Integration (Is architecture coherent? Does traceability matrix connect everything?)

**Common student mistakes to watch for:**
- Confusing ASIL with CAL
- Guessing S/E/C values instead of using criteria
- Writing safety/security requirements without traceability to hazards/threats
- Treating safety and security independently (not integrating)
- Forgetting human factors entirely

---

## ✅ Session Success Criteria

Students leave able to:
- ✓ Apply FTA, FMEA, HAZOP methods to identify hazards
- ✓ Conduct HARA per ISO 26262 and determine ASIL
- ✓ Conduct TARA per ISO 21434 and determine CAL
- ✓ Design defense-in-depth security architecture
- ✓ Define interoperability requirements using standards
- ✓ Apply human factors principles to automation systems
- ✓ Integrate safety, security, interoperability, and human factors into unified system design
- ✓ Understand that specialty engineering is systematic, not ad-hoc

**Critical outcome:** Students understand that **safety, security, interoperability, and human factors are not add-ons - they are foundational to automotive systems engineering** and must be integrated from concept phase.

**Evidence of success:**
- Student can conduct HARA and determine correct ASIL
- Student can conduct TARA and identify realistic threats
- Student can explain why security failures cause safety failures
- Student can design architecture integrating safety mechanisms and security layers
- Student understands SAE automation levels and associated human factors risks

---

## 📚 Additional Resources for Students

**Standards and Guidelines:**
- ISO 26262:2018: Road Vehicles - Functional Safety (Parts 1-12)
- ISO/SAE 21434:2021: Road Vehicles - Cybersecurity Engineering
- SAE J3061: Cybersecurity Guidebook for Cyber-Physical Vehicle Systems
- SAE J3016: Taxonomy and Definitions for Terms Related to Driving Automation Systems
- UN Regulation No. 155: Cyber Security and Cyber Security Management System
- UN Regulation No. 156: Software Update and Software Updates Management System

**Safety Analysis:**
- IEC 61025: Fault Tree Analysis (FTA)
- IEC 60812: Failure Mode and Effects Analysis (FMEA and FMECA)
- IEC 61882: Hazard and Operability Studies (HAZOP)

**Interoperability:**
- AUTOSAR (Automotive Open System Architecture) specifications
- SAE J2735: Dedicated Short Range Communications (DSRC) Message Set Dictionary
- ISO 20077: Extended Vehicle (ExVe) - Standardized access to data

**Books:**
- "ISO 26262 - A Practical Guide" by Jürgen Mottok
- "Automotive Cybersecurity Engineering Handbook" by Dr. Ahmad MK Nasser
- "The Car Hacker's Handbook" by Craig Smith (security perspective)
- "Introduction to Human Factors and Ergonomics" by Robert Bridger (HF fundamentals)

**Online Resources:**
- NHTSA Cybersecurity Best Practices
- SAE International webinars on functional safety
- ISO 26262 training courses (TÜV, SGS)
- MISRA C coding guidelines (secure coding)

---

## 🔗 Connections to Other Sessions

**Builds on:**
- **Session 1**: Engineering failures (Therac-25, Toyota) were specialty engineering failures
- **Session 2**: ISO/IEC 15288 life cycle includes specialty engineering processes
- **Session 4**: Requirements engineering - safety/security requirements need traceability
- **Session 8**: V&V - specialty engineering requires specialized verification methods
- **Session 9**: Risk management and DFMEA - HARA extends FMEA for safety

**Leads to:**
- **Session 13**: LCC/TCO includes cost of safety/security failures and recalls
- **Session 14**: Case Study 2 will apply safety, security, and human factors analysis
- **Session 15**: Technical management includes safety/security configuration management

**Key concept thread:**
- **Session 9**: Risk management basics (DFMEA)
- **Session 12** (today): Specialty engineering for safety, security, interoperability, human factors
- **Session 15**: Technical processes supporting specialty engineering

**Specialty engineering appears in:**
- Session 5 (architecture driven by safety/security)
- Session 8 (safety/security verification)
- Session 10 (quality includes safety/security)
- Session 13 (cost of safety/security failures)

---

## 🎬 Opening and Closing Strategies

### **Opening (First 2 minutes):**
Start with image of Jeep Cherokee on screen as students enter. Begin:

> "Before we start, look at this vehicle. In July 2015, security researchers remotely took control of its steering, brakes, and transmission. 1.4 million vehicles recalled. $1.4 billion settlement.
>
> The attack was possible because safety and security were engineered separately. The infotainment system had no firewall to the safety-critical CAN bus. One exploit, total vehicle control.
>
> Today, we learn how to prevent this through integrated specialty engineering: safety, security, interoperability, and human factors.
>
> Welcome to Session 12: Specialty Engineering - Safety & Security."

### **Closing (Last 2 minutes):**
Return to the opening image:

> "We started with the Jeep Cherokee - a catastrophic failure of integrated specialty engineering. You now have the knowledge to prevent this:
>
> - You can conduct HARA to systematically identify safety hazards and determine ASIL
> - You can conduct TARA to identify security threats and determine CAL
> - You can design defense-in-depth architectures integrating safety and security
> - You understand that human factors and interoperability must be engineered, not assumed
>
> The exercise I've given you is your chance to practice integrated specialty engineering. Imagine you're the engineer responsible for a Level 2 LKAS system. Lives depend on getting safety, security, and human factors right.
>
> Because in automotive, specialty engineering is not optional. It's the difference between life and death.
>
> See you in Session 13, where we'll analyze the cost of getting this wrong."

---

## 📈 Learning Objectives Mapping to Assessment

| Session Objective | Assessment Method | Success Criteria |
|-------------------|-------------------|------------------|
| Apply safety analysis methods | Exercise Part 1 (HARA + FMEA) | Correctly applies S/E/C criteria, determines ASIL, creates FMEA with RPN |
| Conduct HARA per ISO 26262 | Exercise Part 1 | At least 5 hazards identified, correct ASIL determination, safety requirements traced |
| Apply cybersecurity principles | Exercise Part 2 (TARA) | Identifies realistic threats, correct attack feasibility rating, determines CAL |
| Define interoperability requirements | Discussion + exercise integration | Mentions standards (AUTOSAR, V2X), defines interface requirements |
| Incorporate human factors | Exercise Part 3 | Identifies HF risks, defines HF requirements, creates HMI mockup |
| Integrate specialty engineering | Exercise Part 4 | Unified architecture, integrated traceability matrix, combined test scenario |

---

**End of Session 12 Framework**
**Next:** Session 13 (Life Cycle Cost and Total Cost of Ownership)
