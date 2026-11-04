# Design: EV Battery Management System — SE Capstone Case Study
**Date:** 2026-02-22
**Course:** Automotive Systems Engineering (AE ZG517 / AEL ZG517)
**Status:** Approved

---

## Overview

A standalone, self-contained capstone case study in Markdown format for the systems engineering course. The document applies all ISO/IEC 15288 technical processes to the design of an EV Battery Management System (BMS), serving as a synthesis artifact that connects all 16 course sessions.

**Scenario:** IndraMotors (fictional Indian OEM) commissions an SE team to design the BMS for their first mass-market electric sedan, "IM-e1". Students take the role of the SE team.

**Primary purpose:** Course capstone — students study this after completing all 16 sessions to see how SE processes integrate into a coherent engineering project.

---

## Output Location

```
courses/systems-engineering-aezc517/capstone-bms/
├── README.md
├── 01-mission-context.md
├── 02-stakeholder-analysis.md
├── 03-requirements-engineering.md
├── 04-system-architecture.md
├── 05-trade-studies.md
├── 06-design-definition.md
├── 07-ivv-plan.md
├── 08-project-execution-plan.md
└── 09-risk-management.md
```

---

## Chapter Design

### README.md
- Navigation index with purpose, learning objectives, cross-reference map (chapter → session)
- How to use the document (recommended reading sequence)
- Glossary of BMS-specific terms

### Chapter 1: Mission Context & CONOPS (`01-mission-context.md`)
**SE Processes:** Business/Mission Analysis
**Sessions Referenced:** 1, 2

**Content:**
- IndraMotors IM-e1 program description: 400V / 40 kWh mid-size electric sedan, targeting Indian mass market (price band ₹14–18L ex-showroom)
- Mission statement: "Provide safe, reliable, and intelligent energy management for the IM-e1 battery pack across its full operational lifetime"
- CONOPS: 6 operational scenarios — city commute, highway driving, DC fast charging, AC overnight charging, parked in extreme heat (45°C), cold soak (-5°C)
- System context diagram: BMS interfaces with battery pack, Vehicle Control Unit (VCU), thermal system, on-board charger, DC fast charger, and instrument cluster
- System boundary definition: what BMS controls vs. what it monitors/reports only
- Operational environment: 45°C peak ambient, monsoon humidity (95% RH), dust ingress (IP67), altitude up to 2,500m (Himalayan routes)
- Success criteria at mission level (what "good" BMS looks like from the vehicle program perspective)

---

### Chapter 2: Stakeholder Analysis (`02-stakeholder-analysis.md`)
**SE Processes:** Stakeholder Needs and Requirements Definition
**Sessions Referenced:** 4

**Content:**
- 8 stakeholders identified with roles:
  1. Vehicle owner/driver (end user)
  2. Fleet operator (commercial EV fleets)
  3. IndraMotors Systems Engineering team (developer)
  4. ARAI / BIS regulatory bodies (certification)
  5. Service technician (field maintenance)
  6. Charging infrastructure operator (Tata Power, EESL, etc.)
  7. Insurance company (risk assessment)
  8. End-of-life recycling handler
- Stakeholder needs elicitation table: need description, priority, type (functional/constraint/quality)
- Power / Interest matrix visualization (markdown table)
- Stakeholder conflicts identified:
  - Owner wants maximum range → Safety engineer mandates 20% SOC buffer
  - Fleet operator wants aggressive fast charging → Battery longevity constraints
  - Cost target (IndraMotors finance) vs. redundant sensing (safety engineer)
- Conflict resolution approach: use INCOSE stakeholder hierarchy (safety > regulatory > operational > commercial)
- Traceability: each need tagged (SN-01 through SN-XX) → carried through to requirements chapter

---

### Chapter 3: Requirements Engineering (`03-requirements-engineering.md`)
**SE Processes:** System Requirements Definition, System Analysis (HARA)
**Sessions Referenced:** 4, 12

**Content:**

**Section A — System Requirements (~20 key requirements)**
- Functional requirements: SOC estimation accuracy (≤2% error), SOH estimation, cell balancing (within 10mV), thermal control (cell temp 15–45°C during operation), contactor control, fault detection and protection
- Performance requirements: response time for fault cutoff (≤10ms for tier-1 faults), communication latency on CAN (≤5ms)
- Safety requirements: derived from HARA — see below
- Environmental requirements: IP67, -30°C to +60°C storage, -10°C to +55°C operation, vibration per IEC 60068
- Communication requirements: CAN 2.0B at 500kbps, UDS diagnostics (ISO 14229)
- Each requirement: ID, statement, rationale, source (stakeholder need), verification method, ASIL level

**Section B — HARA (Hazard Analysis & Risk Assessment per ISO 26262)**
- 6 hazardous events analyzed:
  1. Overcharge (cell voltage exceeds Vmax)
  2. Over-discharge (cell voltage below Vmin)
  3. Overtemperature during charging
  4. BMS communication loss to VCU
  5. Contactor welding fault
  6. Incorrect SOC reporting
- For each: Severity (S0-S3), Exposure (E0-E4), Controllability (C0-C3) → ASIL rating (QM to ASIL-D)
- Safety goals derived from ASIL-D items → propagated to functional safety requirements
- Example: Overcharge protection → ASIL-D → dual-channel voltage measurement required

**Section C — Requirements Quality Assessment**
- Each requirement evaluated against INCOSE quality attributes: complete, verifiable, traceable, unambiguous, consistent, feasible
- Requirements traceability matrix (excerpt): SN-XX → SR-XX → Architecture Element → Verification Test

---

### Chapter 4: System Architecture (`04-system-architecture.md`)
**SE Processes:** Architecture Definition
**Sessions Referenced:** 3, 5

**Content:**

**View 1 — Functional Architecture**
- 6 top-level functions with decomposition:
  1. Monitor (cell voltage, current, temperature, insulation)
  2. Estimate (SOC, SOH, power capability, remaining range)
  3. Protect (overcharge, over-discharge, overtemperature, overcurrent, short circuit)
  4. Balance (passive cell balancing to equalize SOC across cells)
  5. Control (thermal system, contactors, charging limits)
  6. Communicate (VCU, charger, diagnostics, telematics)
- Functional block diagram (ASCII art table representation)
- Function-to-requirement allocation matrix

**View 2 — Logical Architecture**
- Master-Slave hierarchy: Master BMS (MBMS) + 4× Cell Monitoring Controllers (CMC)
- MBMS responsibilities: SOC/SOH algorithms, fault arbitration, VCU comms, contactor control
- CMC responsibilities: cell voltage measurement, temperature measurement, local balancing, reporting to MBMS
- Redundancy design: dual CAN channels MBMS↔VCU, dual voltage measurement paths on MBMS
- Software architecture: AUTOSAR-compliant layering (BSW / RTE / ASW), safety partition for ASIL-D functions

**View 3 — Physical Architecture**
- Hardware block diagram:
  - Master BMS PCB: STM32H755 dual-core MCU (ASIL-D split between cores), CAN transceivers ×2, LIN transceiver, Ethernet (optional OTA), power supply
  - CMC ICs: TI BQ76940 (14-cell monitoring), 4 ICs per module = 56 cells monitored
  - Pack topology: 7S8P (56 cells per module), 8 modules = 56S configuration for 400V (nominal 201.6V per string × 2 strings)
  - Contactors: main+ and main- contactors, pre-charge contactor, service plug
  - Current sensor: Hall-effect sensor (primary) + shunt resistor (secondary, validation)
- Interface table: all signals, protocols, voltage levels

**View 4 — Interface Architecture**
- External interfaces: HV battery pack, VCU (CAN), OBC (CAN), DCFC (CAN), thermal actuators (PWM), instrument cluster (CAN)
- Internal interfaces: MBMS↔CMC (isolated SPI or LIN), MBMS↔contactor drivers
- Interface Control Document (ICD) excerpt: signal name, type, range, update rate, ASIL

**MBSE Note**
- Explanation of how these views map to SysML diagrams (Block Definition Diagram for physical, Internal Block Diagram for interfaces, Activity Diagram for functions) — consistent with Session 3 MBSE content

---

### Chapter 5: Trade Studies (`05-trade-studies.md`)
**SE Processes:** System Analysis, Decision Management
**Sessions Referenced:** 5, 10

**Content:**

#### Trade Study 1: Battery Cell Chemistry Selection
**Decision:** Which cell chemistry for the IM-e1 primary pack?
**Alternatives:** (A) NMC 811, (B) LiFePO4 (LFP), (C) NCA

**Criteria and weights (total = 100):**
| Criterion | Weight | Rationale |
|---|---|---|
| Gravimetric energy density (Wh/kg) | 20 | Range directly impacts customer value |
| Volumetric energy density (Wh/L) | 15 | Packaging constraint in sedan floor |
| Cycle life (cycles to 80% SOH) | 20 | 8-year warranty requirement |
| Thermal stability (onset of exothermic reaction °C) | 25 | Critical for Indian climate safety |
| Cell cost ($/kWh) | 15 | BOM target |
| Raw material supply security | 5 | Supply chain risk |

**Scoring matrix (1=worst, 5=best):**
| Criterion | Weight | NMC 811 | LFP | NCA |
|---|---|---|---|---|
| Energy density (gravimetric) | 20 | 5 | 3 | 5 |
| Energy density (volumetric) | 15 | 4 | 3 | 5 |
| Cycle life | 20 | 3 | 5 | 2 |
| Thermal stability | 25 | 3 | 5 | 2 |
| Cell cost | 15 | 3 | 5 | 2 |
| Supply security | 5 | 3 | 4 | 2 |
| **Weighted Total** | **100** | **342** | **425** | **295** |

**Sensitivity analysis:** LFP wins even if energy density weight increased to 35%.
**Recommendation:** LFP — superior thermal stability in Indian climate (peak ambient 45°C), lower cost, longer lifecycle aligns with warranty; range delta compensated by pack sizing.

---

#### Trade Study 2: Thermal Management Architecture
**Decision:** How to manage battery pack temperature?
**Alternatives:** (A) Air cooling (forced convection), (B) Indirect liquid cooling (glycol-water), (C) Refrigerant cooling (direct expansion)

**Criteria and weights:**
| Criterion | Weight | Rationale |
|---|---|---|
| Thermal performance at 45°C ambient | 30 | Indian climate requirement |
| System cost (₹ lakh, system level) | 20 | BOM target |
| Weight penalty (kg) | 15 | Range impact |
| Reliability / MTBF | 20 | Fleet operational target 150k km |
| Serviceability in Indian service network | 15 | Field maintenance capability |

**Scoring matrix:**
| Criterion | Weight | Air | Liquid (indirect) | Refrigerant |
|---|---|---|---|---|
| Thermal performance at 45°C | 30 | 2 | 4 | 5 |
| System cost | 20 | 5 | 3 | 1 |
| Weight | 15 | 5 | 3 | 2 |
| Reliability | 20 | 4 | 4 | 2 |
| Serviceability | 15 | 5 | 4 | 2 |
| **Weighted Total** | **100** | **355** | **365** | **255** |

**Sensitivity analysis:** Air cooling wins if thermal weight drops below 15% — but thermal requirement is non-negotiable per HARA (overtemperature = ASIL-D).
**Recommendation:** Indirect liquid cooling — marginal score advantage, but the HARA-driven thermal requirement makes air cooling unacceptable as primary system. Refrigerant cooling adds unjustifiable complexity for Indian service network.

---

### Chapter 6: Design Definition (`06-design-definition.md`)
**SE Processes:** Design Definition
**Sessions Referenced:** 5, 7

**Content:** Four subsystem design descriptions:

**6.1 SOC Estimation**
- Algorithm: Extended Kalman Filter (EKF) on 2RC Thevenin equivalent circuit model
- Inputs: cell voltage, current (Hall sensor), temperature
- States estimated: SOC, polarization voltages
- Model parameters: identified via HPPC test data at 5 temperatures
- Error budget: algorithm ≤1.5%, sensor chain ≤0.5%, total ≤2% (meets SR requirement)
- Degradation path: as SOH decreases, model parameters updated via RLS adaptation

**6.2 Cell Balancing**
- Method: Passive balancing (resistive dissipation)
- Trigger: max cell voltage >3.5V AND delta-V within string >10mV
- Balancing current: 50mA through 70Ω bleed resistor per CMC channel
- Limitations acknowledged: thermal dissipation during balancing limits charge rate
- Alternative (active balancing) not selected per Trade Study 1 rationale (LFP flat OCV curve reduces balancing need)

**6.3 Thermal Management Control**
- Control architecture: PID controller on coolant pump speed; PWM-controlled valve for chiller bypass
- Setpoints: charge mode target 25°C, discharge mode target 30°C
- Thermal runaway detection: rate-of-rise threshold (>2°C/s) → immediate contactor open + warning
- Coolant flow calculations with LFP thermal properties

**6.4 Fault Detection & Protection**
- Three-tier protection:
  - Tier 1 (hardware): analog comparators on CMC IC for over/undervoltage → immediate hardware cutoff (≤1ms, independent of software)
  - Tier 2 (software, ASIL-D): MBMS software checks all measurements at 10ms cycle → contactor open command
  - Tier 3 (vehicle level): VCU receives BMS fault → vehicle safe state
- Fault coding: DTC structure per ISO 14229, 4 severity levels

---

### Chapter 7: Integration, Verification & Validation (`07-ivv-plan.md`)
**SE Processes:** Integration, Verification, Validation
**Sessions Referenced:** 8, 12

**Content:**

**V-Model Application**
- Left side (decomposition): System requirements → Subsystem specs → Software specs → Unit code
- Right side (verification): Unit test → SW integration → HIL test → Pack-level test → Vehicle integration → Field validation
- Each left-side element explicitly paired with right-side verification activity

**Test Levels (10 specific test cases)**
1. SOC algorithm unit test: inject simulated current profile, verify SOC error ≤2%
2. CMC IC communication test: SPI message integrity, timeout handling
3. Fault injection test: short ADC supply → verify graceful degradation (not hard fault)
4. Overtemperature cutoff HIL test: ramp coolant temp, verify contactor opens at threshold
5. Overcharge protection HIL test: inject false high cell voltage → verify Tier 1 + Tier 2 cutoff
6. SOC accuracy drive cycle test (HIL with vehicle model): WLTP cycle, verify accuracy
7. CAN dropout test: disconnect VCU CAN → verify BMS enters safe state
8. Fast charge BMS response test: 150kW DCFC charge event, verify thermal + current limits
9. Environmental test: thermal shock -30°C to +60°C, verify no function loss
10. End-of-charge validation: verify pack reaches 100% SOC within 0.5% accuracy

**Safety Verification**
- Each ASIL-D safety goal verified by independent test team
- ISO 26262 Part 4 (System level V&V) checklist
- Functional safety concept verification: fault injection confirms all protection tiers work as designed

**Validation Criteria**
- Operational validation: 5,000 km validation fleet (50 vehicles × 100 km) covering all CONOPS scenarios
- Customer validation: driver experience panel confirms SOC display accuracy matches expectation

---

### Chapter 8: Project Execution Plan (`08-project-execution-plan.md`)
**SE Processes:** Project Planning, Agreement Management, Life Cycle Cost Analysis
**Sessions Referenced:** 9, 11, 13

**Content:**

**Work Breakdown Structure (WBS)**
- Level 1: IM-e1 BMS Development Program
- Level 2 (5 phases):
  1. Concept Phase (months 1-3): Mission analysis, CONOPS, stakeholder workshops, requirements draft
  2. Requirements Phase (months 3-6): HARA, SRS baseline, architecture selection, Trade Studies
  3. Design Phase (months 6-12): Hardware design, SW architecture, CMC supplier engagement, design reviews
  4. Implementation & Integration (months 12-16): SW development, PCB fabrication, HIL rig setup, integration testing
  5. Validation Phase (months 16-18): Pack-level testing, vehicle integration, field validation, certification

**Resource Plan**
- Team (8 roles):
  | Role | Headcount | Phase Allocation |
  |---|---|---|
  | Chief Systems Engineer | 1 | All phases |
  | Hardware Design Engineer | 2 | Phases 2-4 |
  | Embedded SW Engineer | 3 | Phases 3-4 |
  | Functional Safety Engineer | 1 | All phases |
  | Test & Validation Engineer | 2 | Phases 4-5 |
  | Supplier Quality Engineer | 1 | Phases 3-4 |
  | Configuration Manager | 1 | All phases |
  | Project Manager | 1 | All phases |

**Infrastructure Requirements**
| Item | Purpose | Cost Estimate |
|---|---|---|
| HIL Test Rig (dSPACE SCALEXIO) | BMS software-in-the-loop & HIL testing | ₹45L |
| Battery Cycler (Chroma 17020) | Cell and module characterization | ₹22L |
| Thermal Chamber (-40°C to +80°C) | Environmental testing | ₹18L |
| BMS Function Test Bench | Pack-level functional testing | ₹12L |
| CANalyzer + ETAS INCA licenses | CAN diagnostics and calibration | ₹8L |
| ISO 26262 FUSA tool (LDRA) | Safety analysis and code coverage | ₹15L |
| **Total Infrastructure** | | **₹1.2 Cr** |

**Schedule Summary (18 months)**
| Milestone | Month | Description |
|---|---|---|
| M1: Mission Baseline | 1 | CONOPS and scope agreed |
| M2: SRS Baseline | 6 | Requirements signed off by all stakeholders |
| M3: Architecture Freeze | 8 | Design freeze on architecture (no more trade studies) |
| M4: Design Review (CDR) | 12 | Critical Design Review — hardware + SW design complete |
| M5: First Build Complete | 14 | First BMS hardware assembled and bench-tested |
| M6: System Integration | 16 | BMS integrated into vehicle |
| M7: Validation Complete | 18 | All test cases passed, certification documents submitted |

**Budget Summary (₹ Crore)**
| Category | Budget (₹ Cr) |
|---|---|
| Personnel (12 person-years × 25L avg) | 3.0 |
| Infrastructure (one-time) | 1.2 |
| Component sourcing (CMC ICs, MCU, prototypes) | 0.5 |
| Testing & certification (ARAI, BIS fees) | 0.3 |
| Travel & supplier engagement | 0.2 |
| Contingency (15%) | 0.8 |
| **Total Program Cost** | **₹6.0 Cr** |

**Make vs. Buy Decisions**
- Buy: CMC ICs (TI BQ-series), safety MCU, CAN transceivers, current sensors
- Develop in-house: BMS master software, SOC/SOH algorithms, calibration tools, test automation scripts
- Rationale: core IP (algorithms) stays in-house; commodity silicon sourced from established suppliers

---

### Chapter 9: Risk Management (`09-risk-management.md`)
**SE Processes:** Risk Management, Specialty Engineering (Safety)
**Sessions Referenced:** 9, 12

**Content:**

**Risk Register (12 risks)**

Top risks with full treatment:

| Risk ID | Risk Description | Category | Probability (1-5) | Impact (1-5) | Score | Mitigation | Residual Score |
|---|---|---|---|---|---|---|---|
| R01 | LFP cell supply disruption (geopolitical, single supplier) | Supply Chain | 3 | 5 | 15 | Dual-source cells (CATL + BYD), 6-month buffer stock | 6 |
| R02 | SOC algorithm underperforms in -5°C cold soak | Technical | 3 | 4 | 12 | Temperature-dependent model parameter tables; validation at -10°C | 6 |
| R03 | Thermal runaway event during validation testing | Safety | 2 | 5 | 10 | Fire suppression in test facility, test with CO2 inert atmosphere, insurance | 4 |
| R04 | CMC IC supply shortage (semiconductor market) | Supply Chain | 3 | 4 | 12 | 18-month LTA with TI, second-source TI BQ7694003 | 6 |
| R05 | ARAI certification delayed due to IS standard gap | Regulatory | 2 | 4 | 8 | Early engagement with ARAI, pre-submission review | 4 |
| R06 | HIL test rig delivery delayed | Schedule | 2 | 3 | 6 | Order at contract award (month 1), track lead time | 3 |
| R07 | ISO 26262 ASIL-D SW not achievable with team | Technical | 2 | 5 | 10 | Engage functional safety consultant, LDRA tool from month 3 | 5 |
| R08 | Vehicle CAN conflicts with BMS message IDs | Integration | 3 | 3 | 9 | Early ICD freeze by month 6, CAN matrix review at CDR | 3 |
| R09 | Battery warranty claims exceed prediction | Commercial | 2 | 4 | 8 | Conservative SOC window (15%–95%), temperature-derated charging | 4 |
| R10 | Key person departure (Chief SE or FUSA engineer) | Organizational | 2 | 4 | 8 | Knowledge management plan, pair programming for critical SW | 4 |
| R11 | Monsoon-related corrosion failures in field | Environmental | 2 | 3 | 6 | IP67 testing at ARAI, conformal coating on PCBs | 3 |
| R12 | Cost overrun > 20% due to scope creep | Cost | 2 | 3 | 6 | Formal change control process, monthly EVM tracking | 3 |

**DFMEA (5 Key Failure Modes)**
| Function | Failure Mode | Effect | Severity | Cause | Occurrence | Detection | RPN | Action |
|---|---|---|---|---|---|---|---|---|
| Measure cell voltage | CMC IC reports incorrect voltage | Incorrect SOC → overcharge risk | 9 | CMC IC latch-up | 3 | Plausibility check against string voltage | 5 | Dual measurement path + Tier 1 HW protection |
| Control contactor | Contactor fails to open on command | Overcharge/overdischarge continues | 10 | Driver circuit failure | 2 | Contactor state feedback signal | 4 | Independent hardware watchdog |
| Estimate SOC | SOC drift over lifetime | Customer range anxiety; warranty claim | 7 | Model parameter drift | 4 | SOH estimation divergence check | 6 | Periodic OTA model update |
| Cool pack | Coolant pump failure | Overtemperature → thermal runaway | 10 | Pump bearing failure | 2 | Coolant flow sensor + temp rise rate | 3 | Thermal runaway rate-of-rise detection → emergency cutoff |
| Communicate to VCU | CAN bus silent (BMS fault) | Vehicle unable to manage power | 8 | MCU reset or bus-off | 3 | VCU heartbeat timeout | 4 | BMS enters limp-home mode, transmit fault on secondary CAN |

**Risk Summary**
- High risks (score ≥10): R01, R02, R04, R07 — all have active mitigation plans with owners assigned
- After mitigation: no risk above score 6
- Risk review cadence: monthly during design phase, biweekly during validation

---

## Cross-Reference Map

| Chapter | SE Process | ISO/IEC 15288 Clause | AEZC517 Sessions |
|---|---|---|---|
| 1 | Business/Mission Analysis | 6.4.1 | 1, 2 |
| 2 | Stakeholder Needs Definition | 6.4.2 | 4 |
| 3 | System Requirements Definition | 6.4.3 | 4, 12 |
| 4 | Architecture Definition | 6.4.4 | 3, 5 |
| 5 | System Analysis / Decision Mgmt | 6.4.5 / 6.4.11 | 5, 10 |
| 6 | Design Definition | 6.4.6 | 5, 7 |
| 7 | Integration / Verification / Validation | 6.4.8-10 | 8, 12 |
| 8 | Project Planning / Agreement / LCC | 6.3.1 / 6.3.5 / 6.4.13 | 9, 11, 13 |
| 9 | Risk Management / Specialty Eng | 6.3.4 / 6.4.12 | 9, 12 |

---

## Implementation Notes

- Each chapter file should begin with a standard header: SE processes applied, sessions referenced, estimated reading time
- Tables should be rich but scannable — use ≤6 columns where possible
- Architecture diagrams represented as ASCII/markdown tables and lists (no image files)
- Real component part numbers used for credibility (TI BQ76940, STM32H755, etc.)
- All cost figures in INR to match Indian market context
- Document length estimate: README (~500 words) + 9 chapters (~1,500–3,000 words each) = ~18,000–27,000 words total
- Chapter 5 (Trade Studies) is the richest — full scoring matrices, sensitivity analysis, and design rationale
- Chapter 8 (Project Execution Plan) includes WBS, resource plan, infrastructure table, schedule, and budget

---

## Next Step

Invoke `superpowers:writing-plans` skill to create a detailed implementation plan for generating all 10 files.
