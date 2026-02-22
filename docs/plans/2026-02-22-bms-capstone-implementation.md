# EV BMS SE Capstone Case Study — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Generate a 10-file modular capstone case study applying all ISO/IEC 15288 SE technical processes to an EV Battery Management System (BMS) design, stored under `courses/systems-engineering-aezc517/capstone-bms/`.

**Architecture:** Modular Markdown files — one master README + 9 chapter files, each covering 1-2 SE processes, explicitly cross-referenced to course sessions 1-16. Files are self-contained and rich enough to serve as a course capstone synthesis. No images — all architecture representations use markdown tables and ASCII lists.

**Tech Stack:** Pure Markdown. No generators, no Python scripts. Each file written directly via Write tool. All content based on design doc at `docs/plans/2026-02-22-bms-capstone-case-study-design.md`.

**Design Reference:** Always consult `docs/plans/2026-02-22-bms-capstone-case-study-design.md` before writing each chapter. The design doc is the authoritative spec for content and structure.

**Fictional scenario:** IndraMotors "IM-e1" — first mass-market EV sedan from a fictional Indian OEM. 400V / 40 kWh pack. LFP cells. Indirect liquid cooling. Indian market (45°C peak ambient, monsoon, dust, altitude to 2,500m).

---

## Dependency Order

Some chapters depend on earlier ones (IDs referenced, decisions carried forward):

```
Ch 1 (Mission) ──┐
Ch 2 (Stakeholders) ──┤
                     ↓
                 Ch 3 (Requirements) ──→ Ch 4 (Architecture) ──→ Ch 5 (Trade Studies)
                                                                         ↓
                                                                 Ch 6 (Design)
                                                                 Ch 7 (IV&V)
                                                                 Ch 9 (Risk)
                 Ch 8 (Project Plan) — loosely depends on Ch 3-4, can use design doc
                 README — must be last
```

Tasks 1-4 (setup, Ch 1, Ch 2) can be done in sequence. From Task 5 onward, Ch 8 can be parallelized with Ch 5-7 using dispatching-parallel-agents skill if desired.

---

## Task 1: Create Folder Structure

**Files:**
- Create directory: `courses/systems-engineering-aezc517/capstone-bms/`

**Step 1: Create the directory**

```bash
mkdir -p courses/systems-engineering-aezc517/capstone-bms
```

**Step 2: Verify**

```bash
ls courses/systems-engineering-aezc517/capstone-bms/
```
Expected: empty directory (no error)

**Step 3: Commit**

```bash
git add courses/systems-engineering-aezc517/capstone-bms/
git commit -m "chore: scaffold capstone-bms directory for AEZC517"
```

---

## Task 2: Chapter 1 — Mission Context & CONOPS

**Files:**
- Create: `courses/systems-engineering-aezc517/capstone-bms/01-mission-context.md`

**Step 1: Read design doc section for Ch 1**

Read `docs/plans/2026-02-22-bms-capstone-case-study-design.md` — find "Chapter 1: Mission Context & CONOPS" section. Use it as the authoritative outline.

**Step 2: Write the file**

The file must contain ALL of the following sections (in this order):

```markdown
# Chapter 1: Mission Context and Concept of Operations (CONOPS)

> **SE Processes Applied:** Business/Mission Analysis (ISO/IEC 15288 §6.4.1)
> **AEZC517 Sessions Referenced:** Session 1 (Introduction to SE), Session 2 (SE Fundamentals)
> **Estimated Reading Time:** 20 minutes

---

## 1.1 Program Context — The IndraMotors IM-e1

[Full program description: OEM, vehicle segment, market target, business motivation.
Include: vehicle specs (400V, 40 kWh, ~300 km range), target price band (₹14-18L),
competitive context (Indian EV market vs Tata Nexon EV), program timeline.]

## 1.2 Mission Statement

[Formal mission statement for the BMS. Follow INCOSE format:
"The BMS shall [function] to [outcome] for [stakeholders] under [conditions]"]

## 1.3 Concept of Operations (CONOPS)

[6 operational scenarios as subsections:]
### Scenario 1: City Commute (Normal Operation)
### Scenario 2: Highway Driving (High-Load Operation)
### Scenario 3: DC Fast Charging (150 kW)
### Scenario 4: AC Overnight Charging (7.2 kW)
### Scenario 5: Parked — Extreme Heat (45°C Ambient)
### Scenario 6: Cold Soak and Cold Start (-5°C)

[Each scenario: description, BMS functions active, critical parameters monitored,
expected BMS behaviors, potential stress conditions]

## 1.4 System Context and Boundary

[System context diagram as markdown table showing all external entities and interfaces.
Define explicitly: what IS inside BMS scope, what is NOT (battery cells, VCU, thermal pump)]

## 1.5 Operational Environment

[Full environmental characterization for Indian market:
Temperature range, humidity, altitude, dust, vibration, EMI context.
Reference specific Indian standards where applicable: BIS, AIS-048, AIS-156]

## 1.6 Success Criteria at Mission Level

[5-7 measurable success criteria that define what a "good" BMS looks like from
the IndraMotors program perspective. Not requirements yet — mission-level outcomes.
Example: "Owner experiences ≤2% SOC display error on instrument cluster during
all operational scenarios"]

## 1.7 SE Process Reflection

[Short section connecting this chapter's work to course concepts:
- How does CONOPS connect to stakeholder analysis (Session 4)?
- How does the mission statement constrain requirements (Session 4)?
- What SE processes come next? Bridge to Chapter 2.]
```

**Step 3: Verify completeness**

Read the written file and confirm:
- [ ] All 7 sections present (1.1 through 1.7)
- [ ] 6 CONOPS scenarios present and detailed
- [ ] System context shown as a table or structured list
- [ ] SE Process Reflection section connects to course sessions
- [ ] Header with SE process, sessions, and reading time present

**Step 4: Commit**

```bash
git add courses/systems-engineering-aezc517/capstone-bms/01-mission-context.md
git commit -m "feat(capstone-bms): add Ch1 mission context and CONOPS for IM-e1 BMS"
```

---

## Task 3: Chapter 2 — Stakeholder Analysis

**Files:**
- Create: `courses/systems-engineering-aezc517/capstone-bms/02-stakeholder-analysis.md`

**Step 1: Read design doc section for Ch 2**

Read `docs/plans/2026-02-22-bms-capstone-case-study-design.md` — find "Chapter 2: Stakeholder Analysis" section.

**Step 2: Write the file**

The file must contain ALL of the following sections:

```markdown
# Chapter 2: Stakeholder Analysis

> **SE Processes Applied:** Stakeholder Needs and Requirements Definition (ISO/IEC 15288 §6.4.2)
> **AEZC517 Sessions Referenced:** Session 4 (Requirements Engineering)
> **Estimated Reading Time:** 20 minutes

---

## 2.1 Stakeholder Identification

[Table of 8 stakeholders: ID, Name/Role, Organization, Relationship to BMS]

## 2.2 Stakeholder Needs Elicitation

[For each stakeholder: their needs as a table with columns:
Need ID (SN-01 to SN-XX), Need Statement, Priority (High/Med/Low), Type (Functional/Constraint/Quality/Lifecycle)]

Stakeholders to cover:
1. Vehicle Owner/Driver (end user)
2. Fleet Operator (commercial EV fleets)
3. IndraMotors Systems Engineering Team (developer)
4. ARAI / BIS Regulatory Bodies (certification authority)
5. Service Technician (field maintenance)
6. Charging Infrastructure Operator (Tata Power, EESL)
7. Insurance Company (risk assessment)
8. End-of-Life Recycling Handler

## 2.3 Power / Interest Matrix

[4-quadrant matrix as markdown table:
High Power / High Interest (Manage Closely)
High Power / Low Interest (Keep Satisfied)
Low Power / High Interest (Keep Informed)
Low Power / Low Interest (Monitor)
Place each stakeholder in correct quadrant with brief rationale]

## 2.4 Stakeholder Conflicts

[Identify at least 4 conflicts between stakeholder needs:
Conflict ID, Stakeholder A need, Stakeholder B need, Nature of conflict.
Specific conflicts to include:
- Owner max range vs. Safety engineer SOC buffer
- Fleet operator fast charging vs. Battery longevity
- Cost target (Finance) vs. Redundant sensing (Safety)
- Service technician access vs. IP67 sealing requirement]

## 2.5 Conflict Resolution Approach

[Describe the SE process for resolving conflicts:
INCOSE stakeholder hierarchy (safety > regulatory > operational > commercial)
Show how each conflict is resolved with rationale]

## 2.6 Stakeholder Need Traceability

[Table showing each SN-ID → the chapter and requirement it flows into.
Preview of how SN-01 through SN-XX connect to requirements in Chapter 3]

## 2.7 SE Process Reflection

[Connect to course content:
- How does stakeholder analysis in Session 4 apply here?
- What would have happened in Boeing 737 MAX if passengers had been in this table? (Reference Session 6)
- Bridge to Chapter 3: requirements engineering]
```

**Step 3: Verify completeness**

Read the written file and confirm:
- [ ] All 8 stakeholders present with IDs (SN-01 through SN-XX)
- [ ] Power/interest matrix present
- [ ] At least 4 conflicts with resolutions
- [ ] Traceability column shows SN-IDs flowing to Ch 3
- [ ] SE Process Reflection references Session 6 Boeing case study

**Step 4: Commit**

```bash
git add courses/systems-engineering-aezc517/capstone-bms/02-stakeholder-analysis.md
git commit -m "feat(capstone-bms): add Ch2 stakeholder analysis for IM-e1 BMS"
```

---

## Task 4: Chapter 3 — Requirements Engineering

**Files:**
- Create: `courses/systems-engineering-aezc517/capstone-bms/03-requirements-engineering.md`

**Prerequisite:** Task 3 (Chapter 2) must be complete — SN-IDs from Ch 2 are referenced here.

**Step 1: Read design doc section for Ch 3**

Read `docs/plans/2026-02-22-bms-capstone-case-study-design.md` — find "Chapter 3: Requirements Engineering" section.

**Step 2: Write the file**

The file must contain ALL of the following sections:

```markdown
# Chapter 3: Requirements Engineering

> **SE Processes Applied:** System Requirements Definition (ISO/IEC 15288 §6.4.3), System Analysis — HARA (ISO 26262)
> **AEZC517 Sessions Referenced:** Session 4 (Requirements Engineering), Session 12 (Safety & Security)
> **Estimated Reading Time:** 35 minutes

---

## 3.1 Requirements Development Process

[Brief description of the process used: elicitation from SN-IDs → derivation → analysis → documentation → validation]

## 3.2 System Requirements

[Table of ~20 requirements organized by category.
Columns: Req ID, Category, Requirement Statement, Source (SN-ID), ASIL, Verification Method]

Categories and key requirements to include:
- Functional (SOC estimation ≤2% error; cell balancing within 10mV; contactor control; fault detection)
- Performance (fault cutoff ≤10ms Tier-1; CAN latency ≤5ms; SOH estimation accuracy)
- Safety (derived from HARA — reference SR-IDs)
- Environmental (IP67; -30°C to +60°C storage; -10°C to +55°C operation; vibration per IEC 60068)
- Communication (CAN 2.0B at 500kbps; UDS diagnostics per ISO 14229)
- Lifecycle (design life 8 years / 150,000 km; EOL SOH ≥80%)

## 3.3 Hazard Analysis and Risk Assessment (HARA)

[Full HARA table per ISO 26262 Part 3.
Columns: Hazard ID, Hazardous Event, Operational Situation, Severity (S0-S3), Exposure (E0-E4),
Controllability (C0-C3), ASIL (QM to ASIL-D), Safety Goal]

Hazardous events to analyze (minimum 6):
1. Overcharge (cell voltage exceeds Vmax)
2. Over-discharge (cell voltage below Vmin)
3. Overtemperature during charging (>55°C cell temp)
4. BMS communication loss to VCU
5. Contactor welding fault (contactor fails to open)
6. Incorrect SOC reporting (driver range misjudgment)]

## 3.4 Safety Goals and Functional Safety Requirements

[From ASIL-D items in HARA → derive safety goals → derive functional safety requirements.
Show the chain: Hazard → Safety Goal → FSR.
Example chain: Overcharge → "BMS shall prevent cell voltage exceeding Vmax under all conditions" (ASIL-D) → FSR-01: "BMS shall measure each cell voltage via two independent measurement paths"]

## 3.5 Requirements Quality Assessment

[Evaluate 5 selected requirements against INCOSE quality attributes:
Complete, Verifiable, Traceable, Unambiguous, Consistent, Feasible.
Use Red/Amber/Green rating. Show one example of a poor requirement (before) and improved version (after)]

## 3.6 Requirements Traceability Matrix (Excerpt)

[Matrix excerpt showing: SN-ID → SR-ID → Architecture Element (Ch 4) → Verification Test (Ch 7)]

## 3.7 SE Process Reflection

[Connect to course:
- What requirements were missing from MCAS? (Reference Session 6 HARA analysis)
- How does ASIL rating drive architecture decisions? Bridge to Chapter 4
- Mention ISO 26262 Part 6 (SW requirements), Part 4 (system requirements)]
```

**Step 3: Verify completeness**

Read the written file and confirm:
- [ ] ≥20 requirements in table with all columns
- [ ] HARA table with ≥6 hazardous events, all columns populated
- [ ] At least one ASIL-D item present
- [ ] Safety goals derived from HARA
- [ ] Traceability matrix excerpt connects SN → SR → Architecture → Test
- [ ] Quality assessment uses Red/Amber/Green or explicit pass/fail
- [ ] SE Process Reflection references Boeing MCAS case

**Step 4: Commit**

```bash
git add courses/systems-engineering-aezc517/capstone-bms/03-requirements-engineering.md
git commit -m "feat(capstone-bms): add Ch3 requirements engineering with HARA for IM-e1 BMS"
```

---

## Task 5: Chapter 4 — System Architecture

**Files:**
- Create: `courses/systems-engineering-aezc517/capstone-bms/04-system-architecture.md`

**Prerequisite:** Task 4 (Chapter 3) must be complete — ASIL ratings drive architecture redundancy decisions.

**Step 1: Read design doc section for Ch 4**

Read `docs/plans/2026-02-22-bms-capstone-case-study-design.md` — find "Chapter 4: System Architecture" section.

**Step 2: Write the file**

The file must contain ALL of the following sections:

```markdown
# Chapter 4: System Architecture Definition

> **SE Processes Applied:** Architecture Definition (ISO/IEC 15288 §6.4.4)
> **AEZC517 Sessions Referenced:** Session 3 (Traditional vs MBSE), Session 5 (System Design and Architecture)
> **Estimated Reading Time:** 40 minutes

---

## 4.1 Architecture Development Process

[Brief description: requirements → functional decomposition → logical grouping → physical realization.
Connect to MBSE: which SysML diagrams would represent each view]

## 4.2 Functional Architecture

[6 top-level BMS functions with decomposition:
1. Monitor (cell voltage, current, temperature, insulation resistance)
2. Estimate (SOC, SOH, power capability, remaining range)
3. Protect (overcharge, over-discharge, overtemperature, overcurrent, short circuit, ground fault)
4. Balance (passive cell balancing to equalize SOC across cells)
5. Control (thermal system actuators, contactors, charging limits to OBC/DCFC)
6. Communicate (VCU, charger, diagnostics/UDS, telematics)

Present as indented list showing top-level → sub-functions.
Include a Function-to-Requirement allocation table (Function → SR-IDs it satisfies)]

## 4.3 Logical Architecture

[Master-Slave hierarchy description:
- Master BMS (MBMS): responsibilities listed
- Cell Monitoring Controllers (CMC) ×4: responsibilities listed
- Communication between MBMS and CMC (isolated SPI or LIN)

Software architecture: AUTOSAR-compliant layer diagram as markdown indented list:
- Application SW Layer (ASW): algorithm components
- Runtime Environment (RTE)
- Basic SW Layer (BSW): OS, COM, diagnostics

Redundancy design:
- Dual CAN channels MBMS↔VCU
- Dual voltage measurement paths on MBMS for ASIL-D functions
- Independent hardware watchdog]

## 4.4 Physical Architecture

[Hardware block diagram as a structured markdown table or ASCII art.
Components to include:
- Master BMS PCB: STM32H755 dual-core MCU, CAN transceivers ×2, LIN transceiver, power supply IC
- CMC ICs: TI BQ76940 (14-cell monitoring), 4 ICs per module
- Pack topology: 7S8P cells per module × 8 modules = 56S for 400V nominal
- Contactors: main+, main-, pre-charge, service plug (manual service disconnect)
- Current sensor: Hall-effect (primary) + shunt resistor (secondary/validation)
- Thermal sensors: NTC thermistors on cells, coolant in/out

Component selection rationale for key parts: Why STM32H755? Why TI BQ76940?]

## 4.5 Interface Architecture

[Interface Control Document (ICD) excerpt as table:
Columns: Interface ID, Signal/Parameter, Direction, Protocol, Voltage/Range, Update Rate, ASIL

External interfaces:
- HV Battery Pack (analog: cell voltage, temperature, current)
- VCU (CAN-A: SOC, power limits, faults)
- OBC — On-Board Charger (CAN-B: charge current limit, cell temp)
- DCFC — DC Fast Charger (CAN or CHAdeMO/CCS protocol: current limit)
- Thermal Actuators (PWM: coolant pump speed, chiller valve)
- Instrument Cluster (CAN-A: SOC%, range estimate, warning lamps)]

## 4.6 Architecture-to-Requirements Traceability

[Table showing: Architecture Element → Requirements it satisfies (SR-IDs) → ASIL it supports]

## 4.7 MBSE Perspective

[Short section: how these 4 views map to SysML diagrams.
BDD (Block Definition Diagram) → Physical architecture.
IBD (Internal Block Diagram) → Interface architecture.
Activity Diagram → Functional architecture.
State Machine Diagram → Fault state transitions.
Reference Session 3 MBSE content. Explain why a real MBSE project would use SysML tooling.]

## 4.8 SE Process Reflection

[Connect to course:
- How does architecture satisfy ASIL-D requirement for redundancy? (Reference Ch 3 HARA)
- What trade-offs remain open? Bridge to Chapter 5 (Trade Studies)
- Reference Session 5 content on architecture patterns, CONOPS-to-architecture flow]
```

**Step 3: Verify completeness**

Read the written file and confirm:
- [ ] All 4 architecture views present (functional, logical, physical, interface)
- [ ] 6 top-level functions listed with sub-functions
- [ ] Specific component part numbers present (STM32H755, BQ76940)
- [ ] ICD excerpt table with ≥6 interfaces
- [ ] MBSE section maps views to SysML diagram types
- [ ] Redundancy design explicitly tied to ASIL-D from Ch 3

**Step 4: Commit**

```bash
git add courses/systems-engineering-aezc517/capstone-bms/04-system-architecture.md
git commit -m "feat(capstone-bms): add Ch4 system architecture (4 views) for IM-e1 BMS"
```

---

## Task 6: Chapter 5 — Trade Studies

**Files:**
- Create: `courses/systems-engineering-aezc517/capstone-bms/05-trade-studies.md`

**Prerequisite:** Task 5 (Chapter 4) must be complete — architecture context informs trade study framing.

**Step 1: Read design doc section for Ch 5**

Read `docs/plans/2026-02-22-bms-capstone-case-study-design.md` — find "Chapter 5: Trade Studies" section. The design doc contains the full scoring matrices — copy them accurately.

**Step 2: Write the file**

The file must contain ALL of the following sections:

```markdown
# Chapter 5: Trade Studies

> **SE Processes Applied:** System Analysis (ISO/IEC 15288 §6.4.5), Decision Management (ISO/IEC 15288 §6.4.11)
> **AEZC517 Sessions Referenced:** Session 5 (System Design and Architecture), Session 10 (Decision and Quality Management)
> **Estimated Reading Time:** 45 minutes

---

## 5.1 Trade Study Methodology

[Describe the multi-criteria decision analysis (MCDA) process used:
1. Define decision statement
2. Identify alternatives
3. Define evaluation criteria and weights
4. Score each alternative against each criterion (1=worst, 5=best)
5. Calculate weighted total
6. Perform sensitivity analysis
7. Document recommendation with rationale

Connect to Session 10 content on decision quality management and MCDA.]

---

## Trade Study 1: Battery Cell Chemistry Selection

### 5.2 Decision Statement

[Formal: "Select the battery cell chemistry for the IM-e1 primary pack that best satisfies
program requirements for safety, performance, cost, and longevity in the Indian market context"]

### 5.3 Alternatives Considered

[Three alternatives with brief technical description:
A) NMC 811 (Lithium Nickel Manganese Cobalt Oxide, 811 cathode ratio)
B) LiFePO4 / LFP (Lithium Iron Phosphate)
C) NCA (Lithium Nickel Cobalt Aluminium Oxide)]

### 5.4 Evaluation Criteria and Weights

[Table: Criterion, Weight (%), Rationale for weight, Measurement basis
6 criteria as defined in design doc — total weights must sum to 100]

### 5.5 Scoring Matrix

[Full scoring table with scores (1-5) for each alternative × criterion, weighted scores, totals.
Use exact scores from design doc:
NMC=342, LFP=425, NCA=295]

### 5.6 Sensitivity Analysis

[Vary the weight of the two most influential criteria by ±10 percentage points.
Show: does the ranking change? At what weight threshold does NMC beat LFP?
Conclusion: LFP wins even with aggressive energy density weighting]

### 5.7 Recommendation and Rationale

[Formal recommendation statement.
Rationale: thermal stability critical in Indian climate; cost advantage; lifecycle advantage for 8-year warranty.
Range delta: quantify how much range IM-e1 loses vs NMC — and how pack sizing compensates.
Note: LFP flat OCV curve implications for SOC estimation (EKF needed — bridge to Ch 6)]

---

## Trade Study 2: Thermal Management Architecture

### 5.8 Decision Statement

[Formal: "Select the thermal management architecture for the IM-e1 battery pack that satisfies
the ASIL-D thermal protection requirement under Indian operating conditions"]

### 5.9 Alternatives Considered

[Three alternatives with brief description:
A) Air cooling (forced convection via fan)
B) Indirect liquid cooling (glycol-water coolant loop, heat exchanger)
C) Refrigerant cooling (direct expansion, refrigerant in contact with cells)]

### 5.10 Evaluation Criteria and Weights

[5 criteria as defined in design doc — total weights sum to 100.
Note: "Thermal performance at 45°C ambient" has weight 30 because of ASIL-D requirement
from HARA — this is a non-negotiable constraint from Ch 3]

### 5.11 Scoring Matrix

[Full scoring table.
Air=355, Liquid=365, Refrigerant=255 (from design doc)]

### 5.12 Sensitivity Analysis

[Key insight: even if thermal performance weight drops from 30% to 15%, air cooling barely ties liquid.
But thermal requirement is non-negotiable (ASIL-D from HARA) → air cooling eliminated as primary system.
Show the calculation that makes this explicit]

### 5.13 Recommendation and Rationale

[Formal recommendation: indirect liquid cooling.
Key rationale: HARA overtemperature hazard is ASIL-D → thermal performance criterion is a constraint,
not just a preference → air cooling cannot be selected regardless of cost savings.
Refrigerant cooling rejected: Indian service network cannot maintain refrigerant systems at scale.
Liquid cooling implementation details: glycol-water 50:50, -35°C freeze point, aluminum cold plates]

---

## 5.14 Trade Study Summary and Architecture Decisions

[Table showing: Trade Study → Decision → Impact on Architecture (Ch 4) → Impact on Design (Ch 6)
How do these two decisions lock down the design space for Chapter 6?]

## 5.15 SE Process Reflection

[Connect to course:
- How does MCDA differ from intuitive decision-making? (Reference Session 10)
- Would Boeing have selected a different MCAS architecture with a proper trade study? (Reference Session 6)
- How does sensitivity analysis reduce decision risk? (Reference Session 9 risk management preview)]
```

**Step 3: Verify completeness**

Read the written file and confirm:
- [ ] Both trade studies present with all sections (5.2-5.7, 5.8-5.13)
- [ ] Scoring matrices have all columns (weight × score = weighted score, total row)
- [ ] Totals match design doc (NMC=342, LFP=425, NCA=295; Air=355, Liquid=365, Refrigerant=255)
- [ ] Sensitivity analysis section present for both studies
- [ ] ASIL-D connection to thermal requirement explicit (it's a constraint, not a criterion)
- [ ] SE Process Reflection references Boeing MCAS

**Step 4: Commit**

```bash
git add courses/systems-engineering-aezc517/capstone-bms/05-trade-studies.md
git commit -m "feat(capstone-bms): add Ch5 trade studies (cell chemistry + thermal arch) for IM-e1 BMS"
```

---

## Task 7: Chapter 6 — Design Definition

**Files:**
- Create: `courses/systems-engineering-aezc517/capstone-bms/06-design-definition.md`

**Prerequisite:** Task 6 (Chapter 5) must be complete — trade study decisions (LFP, liquid cooling) constrain the design.

**Step 1: Read design doc section for Ch 6**

Read `docs/plans/2026-02-22-bms-capstone-case-study-design.md` — find "Chapter 6: Design Definition" section.

**Step 2: Write the file**

The file must contain ALL of the following sections:

```markdown
# Chapter 6: Design Definition

> **SE Processes Applied:** Design Definition (ISO/IEC 15288 §6.4.6)
> **AEZC517 Sessions Referenced:** Session 5 (System Design and Architecture), Session 7 (Operational and Functional Analysis)
> **Estimated Reading Time:** 40 minutes

---

## 6.1 Design Definition Process

[Brief: architecture (Ch 4) provides structure; trade studies (Ch 5) make key technology selections;
design definition elaborates HOW each function is implemented.
This chapter covers the 4 most critical BMS subsystem designs.]

---

## 6.2 SOC Estimation Design

### 6.2.1 Algorithm Selection
[Why EKF over Coulomb counting or lookup table — accuracy at temperature extremes, handles model uncertainty]

### 6.2.2 Battery Model
[2RC Thevenin equivalent circuit model: circuit description, parameters (R0, R1, C1, R2, C2, OCV curve).
Note: LFP has flat OCV curve → OCV-based SOC estimation unreliable → EKF is mandatory, not optional.
This reinforces the Trade Study 1 implication flagged in Ch 5]

### 6.2.3 EKF Implementation
[State vector definition, measurement equation, process noise, measurement noise.
No derivations needed — describe in prose with supporting equations in markdown math format.
State: x = [SOC, V_R1, V_R2]; measurement: z = [V_cell]]

### 6.2.4 Model Parameter Identification
[HPPC (Hybrid Pulse Power Characterization) test procedure at 5 temperatures (-10, 0, 15, 30, 45°C).
Parameter look-up tables indexed by SOC × Temperature.
SOH adaptation: how model parameters update as cell ages (RLS-based adaptation)]

### 6.2.5 Error Budget
[Algorithm accuracy: ≤1.5%; sensor chain: ≤0.5%; total ≤2.0% (meets SR from Ch 3)]

---

## 6.3 Cell Balancing Design

### 6.3.1 Balancing Strategy
[Passive balancing — bleed resistor per CMC channel.
Algorithm: trigger when max cell voltage >3.5V AND delta-V within module >10mV.
Note: LFP's flat OCV curve means balancing need is lower vs NMC — design rationale]

### 6.3.2 Passive Balancing Circuit
[50mA balancing current through 70Ω bleed resistor per CMC channel.
Thermal dissipation during balancing: 50mA² × 70Ω = 175mW per cell.
Limitation: charging rate derated during active balancing to manage thermal load]

### 6.3.3 Active Balancing (Not Selected)
[Brief description of active balancing (inductor-based energy transfer).
Why it was not selected for IM-e1: LFP flat OCV reduces need; cost premium not justified;
Indian service network unfamiliar with active balancing repair]

---

## 6.4 Thermal Management Control Design

### 6.4.1 Control Architecture
[Two-loop control:
- Outer loop: target cell temperature setpoint (25°C charge, 30°C discharge)
- Inner loop: PID controller on coolant pump speed to achieve coolant inlet target temperature
Chiller bypass valve: PWM-controlled, opens when ambient too hot for passive rejection]

### 6.4.2 PID Tuning Approach
[Ziegler-Nichols initial tuning; validation via HIL simulation with thermal model.
Anti-windup on integral term to prevent overshoot on startup from cold soak]

### 6.4.3 Thermal Runaway Detection
[Rate-of-rise detection: if any cell temperature increases >2°C/second → immediate contactor open + warning.
This is independent of PID loop — implemented in ASIL-D partition of MBMS SW.
Why rate-of-rise? Absolute temperature threshold too slow; thermal runaway accelerates exponentially]

### 6.4.4 Coolant System Sizing
[Simplified thermal calculation:
- Peak heat generation: C/2 rate discharge of 40 kWh pack → ~20 kW heat into pack at peak
- LFP specific heat ~1.2 kJ/kg/K; pack mass ~250 kg → thermal mass ~300 kJ/K
- Required coolant flow rate to maintain <45°C cell temp at 45°C ambient
- Pump sizing: XX lpm flow rate, XX kPa pressure drop → XX W pump power]

---

## 6.5 Fault Detection and Protection Design

### 6.5.1 Three-Tier Protection Architecture
[Tier 1 — Hardware (≤1ms): Analog comparators on CMC IC trigger directly.
Tier 2 — Software ASIL-D (≤10ms): MBMS SW monitors all measurements, commands contactor open.
Tier 3 — Vehicle Level (≤100ms): VCU receives BMS fault → vehicle safe state.

Each tier: trigger condition, response action, independence from other tiers.
Why three tiers? Single SW fault cannot disable hardware protection.]

### 6.5.2 Fault Codes and Severity Classification
[4 severity levels: Warning / Derate / Fault (non-critical) / Fault (critical — contactor open).
Example fault code table: Fault ID, Name, Severity, Tier, DTC code (per ISO 14229)]

### 6.5.3 Contactor Control State Machine
[States: OPEN, PRE-CHARGE, CLOSED, FAULT.
Transitions: normal start sequence (pre-charge → closed); fault → open; manual service disconnect.
Safety requirement: BMS must confirm contactor state via feedback before assuming state change succeeded]

---

## 6.6 Design-to-Architecture Traceability

[Table: Design Element (§6.2–6.5) → Architecture Element (Ch 4) → Requirements satisfied (SR-IDs)]

## 6.7 SE Process Reflection

[Connect to course:
- How does functional decomposition (Session 7) enable this design?
- How do trade study decisions (LFP → EKF; liquid cooling → PID thermal control) shape every design choice?
- What design elements need ASIL-D ISO 26262 Part 6 compliance? Bridge to Ch 7 V&V.]
```

**Step 3: Verify completeness**

Read the written file and confirm:
- [ ] All 4 subsystem designs present (SOC, balancing, thermal, fault detection)
- [ ] EKF state vector and measurement equation included
- [ ] Three-tier protection architecture described with timing for each tier
- [ ] Thermal sizing calculation present (even if approximate)
- [ ] Active balancing "not selected" rationale explains the decision
- [ ] Design-to-architecture traceability table present

**Step 4: Commit**

```bash
git add courses/systems-engineering-aezc517/capstone-bms/06-design-definition.md
git commit -m "feat(capstone-bms): add Ch6 design definition (SOC, balancing, thermal, faults) for IM-e1 BMS"
```

---

## Task 8: Chapter 7 — Integration, Verification & Validation Plan

**Files:**
- Create: `courses/systems-engineering-aezc517/capstone-bms/07-ivv-plan.md`

**Prerequisite:** Tasks 4, 5, 7 (Ch 3, 4, 6) must be complete — test cases reference requirements, architecture, and design.

**Step 1: Read design doc section for Ch 7**

Read `docs/plans/2026-02-22-bms-capstone-case-study-design.md` — find "Chapter 7: IV&V" section.

**Step 2: Write the file**

The file must contain ALL of the following sections:

```markdown
# Chapter 7: Integration, Verification & Validation Plan

> **SE Processes Applied:** Integration (ISO/IEC 15288 §6.4.8), Verification (§6.4.9), Validation (§6.4.10)
> **AEZC517 Sessions Referenced:** Session 8 (Integration, V&V), Session 12 (Specialty Engineering: Safety & Security)
> **Estimated Reading Time:** 35 minutes

---

## 7.1 V-Model Application

[V-model applied to IM-e1 BMS. Show full left side → right side mapping as table:
Left Side (Definition) | Right Side (Verification)
System requirements (Ch 3) | System acceptance test
Architecture definition (Ch 4) | System integration test
Subsystem design (Ch 6) | HIL + Pack-level test
Software architecture | SW integration test
Unit code (algorithm) | Unit test]

## 7.2 Integration Strategy

[Bottom-up integration sequence:
Stage 1: Unit (algorithm, SW module)
Stage 2: SW integration (MBMS SW complete, simulated CMC)
Stage 3: HIL (MBMS HW + SW, simulated pack via HIL rig)
Stage 4: Pack-level (MBMS + real CMC + real cells in controlled environment)
Stage 5: Vehicle integration (BMS in vehicle, full system)
Stage 6: Field validation (validation fleet)

For each stage: entry criteria, exit criteria, tools required]

## 7.3 Test Cases

[10 specific test cases. For each: Test ID, Name, Level (unit/HIL/pack/vehicle),
Requirement Verified (SR-ID), Test Procedure (steps), Pass/Fail Criteria, Tools Required]

Test cases to include:
TC-01: SOC algorithm unit test (inject HPPC current profile, verify SOC error ≤2%)
TC-02: CMC IC communication integrity test (SPI message loss, timeout, CRC error)
TC-03: Fault injection — ADC supply short (verify graceful degradation, no hard fault)
TC-04: Overtemperature cutoff HIL test (ramp coolant temp, verify contactor opens at threshold)
TC-05: Overcharge protection HIL test (inject false high cell voltage, verify Tier 1 + Tier 2 cutoff)
TC-06: SOC accuracy drive cycle HIL (WLTP cycle with vehicle model, verify <2% error end-to-end)
TC-07: CAN dropout test (disconnect VCU CAN, verify BMS enters safe state within timeout)
TC-08: DC fast charge response test (150 kW charge event, verify thermal limits and current limits)
TC-09: Environmental thermal shock test (-30°C to +60°C per IEC 60068, verify no function loss)
TC-10: End-of-charge validation (verify 100% SOC reached within 0.5% accuracy)]

## 7.4 Safety Verification per ISO 26262

[For ASIL-D safety goals:
- Independent verification team requirement (cannot be same team as design)
- ISO 26262 Part 4 (system level) V&V checklist items
- Fault injection requirement: every safety mechanism must be tested with fault present
- Specific coverage metrics required for ASIL-D SW (MC/DC coverage, 100% branch coverage)
- Reference TC-03, TC-04, TC-05 as safety verification test cases]

## 7.5 Validation Plan

[Operational validation:
- Validation fleet: 50 vehicles × 100 km targeted scenarios = 5,000 km total
- CONOPS coverage: every scenario from Ch 1 must appear in validation fleet routes
- Data logging: what parameters logged, at what rate, how analyzed
- Validation criteria: no safety-related faults, SOC accuracy within spec, customer range anxiety measured]

## 7.6 V&V Infrastructure Requirements

[Tools needed for V&V:
- HIL rig (dSPACE SCALEXIO with battery pack model)
- Battery cycler (cell characterization)
- Thermal chamber
- CANalyzer for CAN monitoring
- Fault injection equipment
- INCA for calibration during HIL
- ISO 26262 coverage tool (LDRA or similar)
Connect to Project Plan in Ch 8]

## 7.7 SE Process Reflection

[Connect to course:
- How does independence of verification prevent the Boeing MCAS V&V failure? (Reference Session 6)
- What is the difference between verification (did we build it right?) and validation (did we build the right thing?)
- How does ASIL-D change the V&V process vs. ASIL-B or QM systems?]
```

**Step 3: Verify completeness**

Read the written file and confirm:
- [ ] V-model table with all 5 levels present
- [ ] Integration strategy with 6 stages and entry/exit criteria
- [ ] All 10 test cases present with TC-IDs and SR-ID cross-references
- [ ] Safety verification section references ISO 26262 Part 4
- [ ] Validation fleet plan (50 vehicles, 5,000 km, CONOPS coverage)
- [ ] SE Process Reflection distinguishes verification vs. validation

**Step 4: Commit**

```bash
git add courses/systems-engineering-aezc517/capstone-bms/07-ivv-plan.md
git commit -m "feat(capstone-bms): add Ch7 IV&V plan with 10 test cases for IM-e1 BMS"
```

---

## Task 9: Chapter 8 — Project Execution Plan

**Files:**
- Create: `courses/systems-engineering-aezc517/capstone-bms/08-project-execution-plan.md`

**Prerequisite:** Task 4 (Ch 3 — requirements baseline) and Task 5 (Ch 4 — architecture) must be complete.
Note: This chapter can be written in parallel with Tasks 7-8 if using parallel agents.

**Step 1: Read design doc section for Ch 8**

Read `docs/plans/2026-02-22-bms-capstone-case-study-design.md` — find "Chapter 8: Project Execution Plan" section. The design doc contains all specific numbers (headcount, costs, milestone months) — use them exactly.

**Step 2: Write the file**

The file must contain ALL of the following sections:

```markdown
# Chapter 8: Project Execution Plan

> **SE Processes Applied:** Project Planning (ISO/IEC 15288 §6.3.1), Agreement Management (§6.3.5), Life Cycle Cost Analysis (§6.4.13)
> **AEZC517 Sessions Referenced:** Session 9 (Project and Risk Management), Session 11 (Agreement and Infrastructure Management), Session 13 (Life Cycle Cost and TCO)
> **Estimated Reading Time:** 35 minutes

---

## 8.1 Program Overview

[Summarize: IndraMotors IM-e1 BMS development program. 18-month duration.
Total budget ₹6.0 Cr. 12-person team. Governed by ISO 26262 ASIL-D requirements.
Reference: Ch 3 requirements baseline is the scope anchor for this plan.]

## 8.2 Work Breakdown Structure (WBS)

[3-level WBS:
Level 1: IM-e1 BMS Development Program
Level 2: 5 phases
Level 3: work packages within each phase

Phase 1: Concept (months 1-3)
- 1.1 Mission analysis and CONOPS development
- 1.2 Stakeholder workshops and needs capture
- 1.3 Feasibility study and initial cost estimate
- 1.4 Program kickoff and governance setup

Phase 2: Requirements (months 3-6)
- 2.1 HARA and safety goal definition
- 2.2 System requirements specification (SRS) development
- 2.3 Architecture selection (Trade Studies)
- 2.4 SRS baseline review and approval
- 2.5 Supplier identification and RFQ

Phase 3: Design (months 6-12)
- 3.1 Hardware design (MBMS PCB, CMC interface)
- 3.2 Software architecture design
- 3.3 Subsystem design (SOC, balancing, thermal, fault detection)
- 3.4 Critical Design Review (CDR)
- 3.5 Supplier award and CMC IC procurement
- 3.6 HIL rig procurement and setup

Phase 4: Implementation & Integration (months 12-16)
- 4.1 SW development and unit testing
- 4.2 PCB fabrication and bring-up
- 4.3 HIL testing (TC-01 through TC-08)
- 4.4 Pack-level integration testing
- 4.5 Vehicle integration test

Phase 5: Validation (months 16-18)
- 5.1 Environmental testing (TC-09)
- 5.2 End-of-charge validation (TC-10)
- 5.3 Validation fleet operation (50 vehicles, 5,000 km)
- 5.4 ARAI certification submission
- 5.5 Program closeout and lessons learned]

## 8.3 Resource Plan — Team Structure

[Table of 8 roles with headcount, phase allocation (which phases active), primary responsibilities.
Roles: Chief SE, HW Design Engineer ×2, Embedded SW Engineer ×3, Functional Safety Engineer,
Test & Validation Engineer ×2, Supplier Quality Engineer, Configuration Manager, Project Manager.
Total: 12 people (some part-time across phases).
Draw org chart as markdown hierarchy.]

## 8.4 Infrastructure Requirements

[Table: Item, Purpose, Phase needed, Cost estimate (₹ Lakh), Procurement lead time.

Items (use design doc numbers):
- HIL Test Rig (dSPACE SCALEXIO): BMS HIL testing, Phase 3-4, ₹45L, 16-week lead time
- Battery Cycler (Chroma 17020): Cell characterization, Phase 2-3, ₹22L
- Thermal Chamber (-40°C to +80°C): Environmental testing, Phase 5, ₹18L
- BMS Function Test Bench: Pack-level functional test, Phase 4-5, ₹12L
- CANalyzer + ETAS INCA: CAN diagnostics and calibration, Phase 3-5, ₹8L
- ISO 26262 FUSA tool (LDRA): Safety analysis + code coverage, Phase 3-4, ₹15L
Total infrastructure: ₹1.2 Cr

Note: HIL rig must be ordered at program start (month 1) due to 16-week lead time.
This is an early critical path item — connects to risk R06 in Ch 9.]

## 8.5 Schedule Summary

[Milestone table: M1 through M7 with month, description, entry criteria, exit criteria.

M1: Mission Baseline (Month 1)
M2: SRS Baseline (Month 6)
M3: Architecture Freeze / Trade Studies Complete (Month 8)
M4: Critical Design Review (Month 12)
M5: First BMS Hardware Build Complete (Month 14)
M6: Vehicle Integration Complete (Month 16)
M7: Validation Complete / Certification Submission (Month 18)

Follow with: 3 critical path items that could delay program if missed.
Connect to risk management in Ch 9.]

## 8.6 Budget Summary

[Table: Category, Budget (₹ Cr), Notes.
Personnel (12 person-years × ₹25L avg): ₹3.0 Cr
Infrastructure (one-time): ₹1.2 Cr
Component sourcing (CMC ICs, MCU, prototypes): ₹0.5 Cr
Testing & certification (ARAI, BIS fees): ₹0.3 Cr
Travel & supplier engagement: ₹0.2 Cr
Contingency (15%): ₹0.8 Cr
Total: ₹6.0 Cr

Add: Earned Value Management (EVM) approach — how cost performance will be tracked monthly.
Define: Cost Performance Index (CPI) and Schedule Performance Index (SPI) thresholds for escalation.]

## 8.7 Make vs. Buy Analysis

[Table: Item, Make or Buy, Rationale, Supplier (if Buy).
Make: BMS master SW, SOC/SOH algorithms, calibration tools, test automation scripts.
Buy: CMC ICs (TI BQ76940), safety MCU (STM32H755), CAN transceivers, current sensor, contactors.
Rationale: core IP (algorithms) retained in-house; commodity silicon sourced from established suppliers.
Reference: Session 11 content on make-vs-buy and supplier management.]

## 8.8 Configuration Management Plan

[Brief CM plan:
- Baseline control: 3 controlled baselines (SRS, CDR, Production)
- Change control: formal ECR process for any change after baseline
- Tools: Git for SW, PDM system for HW (e.g., Windchill or equivalent)
- Version naming convention: SW vX.Y.Z (Major.Minor.Patch); HW Issue letters
Connect to Session 15 content on configuration management.]

## 8.9 Life Cycle Cost Estimate (LCC)

[3-phase LCC:
- Development cost: ₹6.0 Cr (this program)
- Unit production cost per vehicle: BMS BoM (~₹18,000 per vehicle), assuming 10,000 units/year
- Support / warranty cost estimate: field failure rate × repair cost × fleet size × 8 years

Total LCC for 10,000 vehicle/year program over 8 years: provide estimate.
Reference Session 13 LCC analysis methods.]

## 8.10 SE Process Reflection

[Connect to course:
- How does WBS connect to functional decomposition? (Project structure mirrors system structure)
- Why is the HIL rig ordered in Month 1 even though it's not used until Month 14? (Long-lead procurement)
- What is earned value management and why does it matter? (Reference Session 9)
- How does make-vs-buy affect IP strategy? (Reference Session 11)]
```

**Step 3: Verify completeness**

Read the written file and confirm:
- [ ] WBS has 3 levels with all 5 phases and work packages
- [ ] Resource table has all 8 roles with headcount and phases
- [ ] Infrastructure table has all 6 items with costs summing to ₹1.2 Cr
- [ ] 7 milestones with entry/exit criteria
- [ ] Budget table has all categories summing to ₹6.0 Cr
- [ ] Make-vs-buy table present
- [ ] LCC estimate covers all 3 phases (development, production, support)
- [ ] EVM approach described

**Step 4: Commit**

```bash
git add courses/systems-engineering-aezc517/capstone-bms/08-project-execution-plan.md
git commit -m "feat(capstone-bms): add Ch8 project execution plan (WBS, resources, budget, LCC)"
```

---

## Task 10: Chapter 9 — Risk Management

**Files:**
- Create: `courses/systems-engineering-aezc517/capstone-bms/09-risk-management.md`

**Prerequisite:** Tasks 5-7 (Ch 4, 5, 6) must be complete — architecture and design inform risk identification.

**Step 1: Read design doc section for Ch 9**

Read `docs/plans/2026-02-22-bms-capstone-case-study-design.md` — find "Chapter 9: Risk Management" section. The design doc contains the full risk register table and DFMEA — use all values exactly.

**Step 2: Write the file**

The file must contain ALL of the following sections:

```markdown
# Chapter 9: Risk Management

> **SE Processes Applied:** Risk Management (ISO/IEC 15288 §6.3.4), Specialty Engineering — Safety (§6.4.12)
> **AEZC517 Sessions Referenced:** Session 9 (Project and Risk Management), Session 12 (Specialty Engineering: Safety & Security)
> **Estimated Reading Time:** 35 minutes

---

## 9.1 Risk Management Process

[Describe the risk management process used:
1. Risk identification (brainstorming, checklists, FMEA)
2. Risk analysis (probability × impact scoring)
3. Risk evaluation (scoring against thresholds)
4. Risk treatment (mitigate, transfer, accept, avoid)
5. Risk monitoring (cadence, triggers, escalation)

Risk scoring scale: Probability 1-5 (1=rare, 5=almost certain), Impact 1-5 (1=negligible, 5=catastrophic).
Risk score = P × I. Threshold: score ≥10 = High (active mitigation required), 5-9 = Medium, <5 = Low.]

## 9.2 Risk Register

[Full table of 12 risks. Columns:
Risk ID, Description, Category, Probability (1-5), Impact (1-5), Score, Mitigation, Risk Owner, Residual Score

Use exact values from design doc:
R01 through R12 as specified — all values must match design doc]

## 9.3 Risk Heatmap

[4×4 heatmap as markdown table: Probability (rows 1-5) vs Impact (cols 1-5).
Color-code zones: Low (P×I<5), Medium (5-9), High (≥10) using text labels.
Place R01-R12 in correct cells.
Discuss: which quadrant has most risks? What does this tell IndraMotors management?]

## 9.4 Risk Mitigation Plans — High Risks

[Detailed mitigation plans for R01, R02, R04, R07 (score ≥10):

For each:
- Root cause (why does this risk exist?)
- Mitigation actions (specific, actionable, with owner and due date)
- Trigger condition (what event would cause this risk to materialize?)
- Contingency plan (if mitigation fails, what happens?)
- Residual risk score after mitigation]

## 9.5 DFMEA — Design Failure Mode and Effects Analysis

[Full DFMEA table for 5 key failure modes.
Columns: Function, Failure Mode, Effect, Severity (1-10), Cause, Occurrence (1-10),
Detection (1-10), RPN (S×O×D), Recommended Action, Responsibility.

Failure modes (use design doc values):
1. CMC IC reports incorrect cell voltage
2. Contactor fails to open on command
3. SOC drift over lifetime (model parameter drift)
4. Coolant pump failure during high-load
5. BMS CAN bus silent (MCU reset or bus-off)]

## 9.6 DFMEA to Requirements Traceability

[Table showing: DFMEA Failure Mode → Recommended Action → Requirements created or updated (SR-ID)
This shows how DFMEA is not just documentation — it feeds back into requirements (iterate!)]

## 9.7 Risk Monitoring and Review

[Risk review cadence:
- Monthly: full risk register review during design phase
- Biweekly: during integration and validation phases
- Trigger-based: any risk score change ≥3 points → escalation to program manager

What to monitor: project schedule variance (SPI), component lead times, field test anomalies.
Connect to EVM from Ch 8: SPI < 0.8 triggers risk R06 review.]

## 9.8 Residual Risk Summary

[After all mitigations: no risk above score 6. Residual risk acceptance statement.
Connect to ISO 26262: residual risk at functional safety level must be accepted by IndraMotors
Chief Safety Officer and documented in Safety Case.]

## 9.9 SE Process Reflection

[Connect to course:
- How does DFMEA differ from FMEA? (Design FMEA focuses on design choices causing failures)
- How does risk management in SE connect to ISO 26262 ASIL determination? (Both are risk-based)
- What risks did Boeing NOT identify for MCAS? (Reference Session 6 — single sensor, no pilot training)
- Why is residual risk never zero — and how does the Safety Case document its acceptance?]
```

**Step 3: Verify completeness**

Read the written file and confirm:
- [ ] Risk register has all 12 risks with all columns
- [ ] Risk heatmap present with R01-R12 placed correctly
- [ ] Detailed mitigation plans for R01, R02, R04, R07 (high risks)
- [ ] DFMEA table with all 5 failure modes and RPN calculations
- [ ] DFMEA-to-requirements traceability table present
- [ ] SE Process Reflection references Boeing MCAS for risk identification failure

**Step 4: Commit**

```bash
git add courses/systems-engineering-aezc517/capstone-bms/09-risk-management.md
git commit -m "feat(capstone-bms): add Ch9 risk management with DFMEA for IM-e1 BMS"
```

---

## Task 11: README — Master Navigation Document

**Files:**
- Create: `courses/systems-engineering-aezc517/capstone-bms/README.md`

**Prerequisite:** All Tasks 2-10 must be complete — README links to all chapters and verifies cross-references.

**Step 1: Write the file**

```markdown
# IM-e1 BMS — Systems Engineering Capstone Case Study

> **Course:** Automotive Systems Engineering (AE ZG517 / AEL ZG517), BITS Pilani
> **Purpose:** Capstone synthesis — applies all 16 sessions' content to one coherent automotive problem
> **Scenario:** IndraMotors "IM-e1" EV BMS design using ISO/IEC 15288 technical processes

---

## How to Use This Case Study

[2-3 paragraphs: who this is for, how to read it, what you'll know at the end.
Recommended sequence: read all chapters in order after completing all 16 sessions.
Alternative: use as reference — jump to the chapter covering the SE process you want to review.]

## The Engineering Problem

[Brief description: IndraMotors is designing their first EV. The BMS is safety-critical.
Students take the role of the SE team. What decisions must be made? What processes must be followed?]

## Learning Objectives

[After studying this case study, students will be able to:
1. Apply all ISO/IEC 15288 technical processes to a real automotive design problem
2. Trace requirements from stakeholder needs through architecture to verification
3. Conduct quantitative trade studies using MCDA methods
4. Develop a project execution plan with WBS, resources, and risk management
5. Apply ISO 26262 HARA and DFMEA to identify and manage safety risks]

## Cross-Reference Map: Session to Chapter

[Table: Session | Topic | Capstone Chapter(s)
Session 1-2 | SE Fundamentals, ISO 15288 | Ch 1 (Mission Context)
Session 3 | MBSE | Ch 4 (Architecture — MBSE section)
Session 4 | Requirements Engineering | Ch 2 (Stakeholders), Ch 3 (Requirements)
Session 5 | System Design & Architecture | Ch 4 (Architecture), Ch 5 (Trade Studies)
Session 6 | Case Study 1 (Boeing) | Referenced in all Ch.X SE Reflections
Session 7 | Operational & Functional Analysis | Ch 6 (Design Definition)
Session 8 | Integration, V&V | Ch 7 (IV&V Plan)
Session 9 | Project & Risk Management | Ch 8 (Project Plan), Ch 9 (Risk)
Session 10 | Decision & Quality Management | Ch 5 (Trade Studies)
Session 11 | Agreement & Infrastructure | Ch 8 (Make vs Buy, CM)
Session 12 | Safety & Security | Ch 3 (HARA), Ch 7 (Safety V&V), Ch 9 (DFMEA)
Session 13 | LCC / TCO | Ch 8 (LCC Estimate)
Session 14 | Case Study 2 | This document
Session 15 | Technical Management | Ch 8 (Configuration Management)
Session 16 | Emerging Trends | Brief mention in relevant chapters]

## Chapter Index

[Linked list of all 9 chapters with one-sentence description each]

## Key Design Decisions Summary

[Quick-reference table: Decision | Choice Made | Chapter where decided | Trade Study reference
Cell chemistry: LiFePO4 (Ch 5, Trade Study 1)
Thermal management: Indirect liquid cooling (Ch 5, Trade Study 2)
SOC algorithm: Extended Kalman Filter (Ch 6)
Balancing: Passive balancing (Ch 6)
Master MCU: STM32H755 dual-core (Ch 4)
CMC IC: TI BQ76940 (Ch 4)]

## Glossary

[30+ terms: AOA, ASIL, BMS, CATL, CMC, CONOPS, DTC, EKF, FMEA, HARA, HIL, HPPC,
ICD, IP67, LCC, LFP, MBMS, MBSE, MCDA, MCU, NCA, NMC, OBC, PWM, RLS, SPI, SOC, SOH,
SRS, TCO, UDS, VCU, WBS and others as needed.
Each: acronym expansion + 1-sentence definition in BMS context]
```

**Step 2: Verify completeness**

Read the written file and confirm:
- [ ] Cross-reference map covers all 16 sessions
- [ ] Session 6 (Boeing) cross-referenced to case study chapters
- [ ] Session 14 listed as "this document"
- [ ] Key design decisions table covers all 6 major decisions
- [ ] Glossary has ≥25 terms
- [ ] Chapter links all present

**Step 3: Commit**

```bash
git add courses/systems-engineering-aezc517/capstone-bms/README.md
git commit -m "feat(capstone-bms): add README navigation for IM-e1 BMS capstone case study"
```

---

## Task 12: Final Verification

**Files:** None created. Verification only.

**Step 1: Confirm all 10 files exist**

```bash
ls courses/systems-engineering-aezc517/capstone-bms/
```

Expected:
```
README.md
01-mission-context.md
02-stakeholder-analysis.md
03-requirements-engineering.md
04-system-architecture.md
05-trade-studies.md
06-design-definition.md
07-ivv-plan.md
08-project-execution-plan.md
09-risk-management.md
```

**Step 2: Check cross-references are consistent**

For each item below, verify it's consistent across chapters:
- SN-IDs from Ch 2 are referenced in Ch 3
- SR-IDs from Ch 3 are referenced in Ch 4 (architecture traceability) and Ch 7 (test cases)
- Trade study decisions in Ch 5 (LFP, liquid cooling) are reflected in Ch 6 design
- Ch 8 infrastructure items match what Ch 7 requires for V&V
- Risk R06 (HIL rig delay) in Ch 9 references Ch 8 critical path

**Step 3: Word count check**

```bash
wc -w courses/systems-engineering-aezc517/capstone-bms/*.md
```

Expected: total word count between 18,000 and 27,000 words across all files.

**Step 4: Final commit**

```bash
git add courses/systems-engineering-aezc517/capstone-bms/
git commit -m "docs(capstone-bms): complete 10-file EV BMS SE capstone case study for AEZC517

Applies all ISO/IEC 15288 technical processes to IndraMotors IM-e1 BMS design.
Covers: mission analysis, stakeholders, HARA, 3-view architecture, 2 trade studies,
design definition, IV&V plan, project execution plan, and risk management.
Cross-references all 16 course sessions. Serves as Session 14 capstone case study.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

---

## Quick Reference: What Goes Where

| Chapter | Key Outputs | Critical Tables/Artifacts |
|---|---|---|
| 01 | CONOPS, System Boundary | 6 scenarios, context diagram |
| 02 | 8 stakeholders, SN-IDs | Power/interest matrix, conflict table |
| 03 | ~20 SR-IDs, HARA, ASIL | Requirements table, HARA table, traceability matrix |
| 04 | 4 architecture views | Functional decomposition, physical block diagram, ICD |
| 05 | 2 trade studies | Scoring matrices (with exact totals from design doc), sensitivity analysis |
| 06 | 4 subsystem designs | EKF model, 3-tier protection state machine, thermal calculation |
| 07 | V&V plan, 10 test cases | V-model table, TC table with SR cross-refs |
| 08 | WBS, resources, budget | 3-level WBS, ₹6.0 Cr budget, 7 milestones |
| 09 | 12 risks, DFMEA | Risk register, heatmap, DFMEA with RPN |
| README | Navigation, glossary | 16-session cross-reference map, decisions summary |
