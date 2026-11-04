# IM-e1 BMS — Systems Engineering Capstone Case Study

**Course:** Automotive Systems Engineering (AEL ZG517 / AE ZG517)
**Program:** BITS Pilani — Work Integrated Learning Programmes (WILP)
**Purpose:** Capstone synthesis applying all ISO/IEC 15288 technical processes to a real-world EV design problem
**Scenario:** IndraMotors (fictional Indian OEM) designs the Battery Management System for their first electric sedan

---

## What This Case Study Is

This is a 9-chapter technical case study that walks through a complete systems engineering project from mission analysis to risk management. You take the role of the systems engineering team at **IndraMotors**, tasked with designing the BMS for the **IM-e1** — a 400V / 40 kWh electric sedan targeting India's mass market (₹14–18 lakh price band).

Every chapter applies one or more SE processes from ISO/IEC 15288 to real design decisions. Every chapter traces back to sessions you have already studied in AEZC517. Nothing here is abstract — the tools, the component names, the regulatory standards, and the engineering trade-offs are representative of what real automotive SE teams deal with.

**How to use this document:**
- Read sequentially to follow the full SE project lifecycle
- Jump to any chapter using the index below if you want to study a specific process
- Use the cross-reference map (§2) to connect each chapter to the course sessions it demonstrates
- Use the glossary (§4) when you encounter an unfamiliar term

---

## Chapter Index

| # | File | Title | SE Process(es) | Reading Time |
|---|---|---|---|---|
| 1 | [`01-mission-context.md`](01-mission-context.md) | Mission Context & CONOPS | Business/Mission Analysis | 20 min |
| 2 | [`02-stakeholder-analysis.md`](02-stakeholder-analysis.md) | Stakeholder Analysis | Stakeholder Needs & Requirements Definition | 20 min |
| 3 | [`03-requirements-engineering.md`](03-requirements-engineering.md) | Requirements Engineering | System Requirements Definition + HARA | 35 min |
| 4 | [`04-system-architecture.md`](04-system-architecture.md) | System Architecture | Architecture Definition | 30 min |
| 5 | [`05-trade-studies.md`](05-trade-studies.md) | Trade Studies | System Analysis + Decision Management | 30 min |
| 6 | [`06-design-definition.md`](06-design-definition.md) | Design Definition | Design Definition | 35 min |
| 7 | [`07-ivv-plan.md`](07-ivv-plan.md) | Integration, Verification & Validation | Integration + Verification + Validation | 30 min |
| 8 | [`08-project-execution-plan.md`](08-project-execution-plan.md) | Project Execution Plan | Project Planning + Agreement Mgmt + LCC | 35 min |
| 9 | [`09-risk-management.md`](09-risk-management.md) | Risk Management | Risk Management + DFMEA + FTA | 30 min |

**Total estimated reading time:** ~4.5 hours (complete sequential read)

---

## Session Cross-Reference Map

Each chapter connects to specific AEZC517 sessions. Use this to review course material alongside the case study, or to find which chapter demonstrates the processes you studied in a particular session.

| AEZC517 Session | Session Topic | Primary Chapter | Secondary Chapter |
|---|---|---|---|
| Session 1 | Introduction to Systems Engineering | Ch 1 (Mission Context) | — |
| Session 2 | Systems Thinking & CONOPS | Ch 1 (CONOPS, success criteria) | — |
| Session 3 | MBSE and Architecture Frameworks | Ch 4 (MBSE note, SysML mapping) | — |
| Session 4 | Requirements Engineering | Ch 2 (stakeholder needs), Ch 3 (SRS) | — |
| Session 5 | System Design & Trade-Off Analysis | Ch 4 (architecture), Ch 5 (trade studies) | Ch 6 |
| Session 6 | Case Studies — Boeing 737 MAX | Ch 2 (§2.7 Boeing parallel) | Ch 7 (§7.1) |
| Session 7 | Detailed Design & Design Reviews | Ch 6 (EKF, balancing, fault protection) | Ch 8 (CDR milestone) |
| Session 8 | Verification & Validation | Ch 7 (V-model, TC-01 to TC-10) | — |
| Session 9 | SE Management & Risk | Ch 8 (WBS, EVM, schedule) | Ch 9 (risk register) |
| Session 10 | Decision Analysis | Ch 5 (MCDA scoring matrices) | — |
| Session 11 | Configuration Management & Lifecycle | Ch 8 (§8.9 CM plan, baselines) | — |
| Session 12 | Functional Safety (ISO 26262) | Ch 3 (HARA, ASIL ratings) | Ch 7 (ASIL-D V&V), Ch 9 (DFMEA) |
| Session 13 | Earned Value & Project Metrics | Ch 8 (§8.7 EVM worked example) | — |
| Session 14 | Specialty Engineering (EMC, Thermal) | Ch 6 (§6.3 thermal control design) | — |
| Session 15 | Supplier & Agreement Management | Ch 8 (§8.11 three agreements) | — |
| Session 16 | Synthesis & Capstone Review | All chapters (full lifecycle) | — |

---

## Key Design Decisions Summary

Five decisions shaped the entire IM-e1 BMS design. Understanding these decisions and their rationale is the fastest way to understand the system.

### Decision 1: LFP Cell Chemistry (Chapter 5, Trade Study 1)

**Decision:** Use LiFePO₄ (LFP) cells, not NMC 811 or NCA.
**Rationale:** LFP's superior thermal stability (onset of exothermic reaction at 270°C vs. NMC's 210°C) is critical for India's 45°C peak ambient temperature. Thermal stability received the highest weight (25%) in the MCDA because the overtemperature hazard is ASIL-D. LFP scored 425/500 vs. NMC 355/500.
**Consequence that flows through every subsequent chapter:** LFP's flat OCV-SOC curve between 20%–80% SOC makes simple voltage-based SOC lookup unreliable → mandates Extended Kalman Filter for SOC estimation (Ch 6, §6.1) → requires HPPC test data at multiple temperatures (Ch 7, TC-01) → cold-temperature algorithm performance is a top risk (Ch 9, R02).

### Decision 2: Indirect Liquid Thermal Management (Chapter 5, Trade Study 2)

**Decision:** Use glycol-water indirect liquid cooling, not air cooling or refrigerant cooling.
**Rationale:** Air cooling initially scored higher (355 raw vs. liquid's 365 raw) — but a thermal physics calculation showed air cooling cannot maintain cell temperature below 55°C at 45°C ambient + 150kW DCFC, violating the ASIL-D overtemperature safety goal. Safety constraints function as pass/fail gates, overriding raw scores. Refrigerant cooling was eliminated by Indian service network serviceability concerns.
**Key lesson:** MCDA scores are inputs to judgment, not outputs. A safety constraint eliminated the highest-scoring alternative.

### Decision 3: Passive Cell Balancing (Chapter 6, §6.2)

**Decision:** Use passive balancing (50mA resistive dissipation) rather than active balancing (bidirectional DC-DC).
**Rationale:** Active balancing adds ₹4,000–₹6,000 to BoM and significant software complexity. LFP cells have a naturally flat OCV curve, which reduces the severity of SOC imbalance between cells (a 10mV voltage difference across the plateau corresponds to a very small SOC difference). Passive balancing is sufficient to maintain cell balance within the 10mV SR-F-04 requirement.
**Consequence:** Thermal dissipation during balancing (0.15W per cell, 8.4W total) limits charge rate during final CV phase. This is a known design constraint documented in §6.2.

### Decision 4: STM32H755 Dual-Core ASIL-D Architecture (Chapter 4, §4.3)

**Decision:** Use STM32H755 (Cortex-M7 + Cortex-M4 in lockstep configuration) partitioned between ASIL-D and ASIL-B functions.
**Rationale:** ISO 26262 Part 4 requires independence between ASIL-D and lower-ASIL functions. Running thermal runaway detection (ASIL-D, Core 0) and SOC estimation (ASIL-B, Core 1) on separate cores with MPU enforcement satisfies the "Freedom from Interference" requirement without adding a second MCU (cost constraint SN-12).
**Trade-off acknowledged:** Real-time partitioning adds software complexity and requires AUTOSAR OS multi-core configuration.

### Decision 5: Three-Tier Fault Protection (Chapter 6, §6.4)

**Decision:** Hardware comparator (≤1ms) → Software ASIL-D (≤10ms) → Vehicle VCU (≤100ms) — three independent tiers.
**Rationale:** ASIL-D overcharge protection (SG-01) requires that no single failure can prevent contactor opening. Three independent tiers — hardware (in CMC IC silicon), software (on MCU Core 0), and vehicle-level (VCU) — provide defense-in-depth. The FTA (Chapter 9, §9.8) demonstrates that all three tiers must fail simultaneously for a thermal runaway event, producing a top-event probability of 10⁻⁹/hour — meeting ISO 26262 ASIL-D.

---

## How SE Processes Connect

The nine chapters are not nine independent documents. They are the outputs of nine interdependent SE processes, each feeding the next:

```
Mission (Ch 1) ──► Stakeholder Needs (Ch 2) ──► Requirements (Ch 3)
                                                       │
                                               Architecture (Ch 4)
                                                       │
                                              Trade Studies (Ch 5)
                                                       │
                                              Design Definition (Ch 6)
                                                       │
                                                  IV&V (Ch 7)
                                                       │
                                    ┌──────────────────┤
                                    │                  │
                             Project Plan (Ch 8)  Risk Mgmt (Ch 9)
```

Every chapter references IDs from previous chapters:
- Ch 2 stakeholder needs (SN-01 to SN-26) → become the "Source" column in Ch 3 requirements
- Ch 3 requirements (SR-F-01, SR-S-01...) → allocated to architecture elements in Ch 4
- Ch 4 architecture decisions → constrain design options in Ch 5 and Ch 6
- Ch 6 design → defines what must be tested in Ch 7
- Ch 7 test cases → appear as schedule milestones in Ch 8
- Ch 9 risk register → drove design decisions in Ch 4, 6, and 8

**This is traceability in practice.** Every requirement has a source; every design decision has a rationale; every test case has a requirement it verifies. No artifact is orphaned.

---

## Glossary

### A

**ASIL (Automotive Safety Integrity Level):** ISO 26262's classification for the risk reduction required of a safety function. Ranges from QM (no safety requirement) to ASIL-D (most stringent). Determined by Severity × Exposure × Controllability in HARA.

**AUTOSAR (AUTomotive Open System ARchitecture):** A standardized software architecture for automotive ECUs. Layers: Basic Software (BSW, hardware abstraction) → Runtime Environment (RTE, middleware) → Application Software (ASW, application logic). Used in the MBMS for ISO 26262 compliance.

**AIS-048:** India's EV safety standard (Automotive Industry Standard), derived from UNECE GTR-20. Mandates electrical safety, overcharge/overdischarge protection, and thermal runaway requirements for EVs sold in India. Enforced by ARAI during type approval.

### B

**BMS (Battery Management System):** The electronic control system responsible for monitoring, protecting, estimating, balancing, controlling, and communicating the state of a battery pack. The subject of this capstone.

**BQ76940:** Texas Instruments' automotive-grade Cell Monitoring Controller IC. Monitors up to 15 series cells, measures voltage (±1.5mV accuracy), temperature, and provides hardware over/undervoltage comparators. Used as the CMC IC in the IM-e1 BMS.

### C

**CAN (Controller Area Network):** The primary communication bus in automotive applications. CAN 2.0B supports up to 1 Mbit/s. The BMS communicates with the VCU, OBC, and DCFC on CAN at 500 kbps.

**CC-CV (Constant Current — Constant Voltage):** Standard Li-ion / LFP charging profile. Charge at constant current until cell reaches voltage limit (3.65V for LFP), then hold constant voltage until current drops below cutoff (C/20).

**CCS Combo 2 (Combined Charging System):** The DC fast charging connector standard used in Europe and India. Combines AC (Type 2) and DC pins. The IM-e1 uses CCS Combo 2 for DCFC sessions at up to 150kW.

**CDR (Critical Design Review):** The formal design review milestone (M4, Month 12) at which hardware schematics and software architecture are complete and frozen. After CDR, design changes require formal ECO approval.

**CMC (Cell Monitoring Controller):** The slave node in the BMS master-slave hierarchy. Each CMC IC (TI BQ76940) monitors up to 14 series cells in one battery module. Four CMCs cover the full 56-cell pack.

**CONOPS (Concept of Operations):** A document describing how a system will be used in its operational environment. Chapter 1 defines six CONOPS scenarios for the IM-e1 BMS.

**Coulomb Counting:** SOC estimation by integrating current over time: ΔSOC = ∫I dt / Qmax. Simple but accumulates error with sensor offsets and Qmax uncertainty. Used as a reference in TC-01 and TC-06, not as the primary SOC algorithm.

### D

**DCFC (DC Fast Charging):** High-power charging (typically 50–350kW) using DC current injected directly into the battery pack via the CCS Combo 2 connector. The IM-e1 supports up to 150kW DCFC.

**DFMEA (Design Failure Mode and Effects Analysis):** Bottom-up reliability analysis. Identifies how each design element can fail, the effect of that failure, and the current detection controls. Scored using RPN = Severity × Occurrence × Detection.

**DTC (Diagnostic Trouble Code):** Standardized fault codes stored in the BMS and retrievable via OBD-II using the UDS protocol (ISO 14229). The IM-e1 BMS defines DTCs P1B00–P1B08 for BMS-specific faults.

### E

**EKF (Extended Kalman Filter):** A recursive Bayesian state estimator for nonlinear systems. Used for SOC estimation in the IM-e1 BMS because LFP's flat OCV-SOC curve prevents simple voltage lookup. The EKF estimates SOC (and polarization voltages) from the 2RC Thevenin battery model.

**EVM (Earned Value Management):** Project performance measurement comparing Planned Value (PV), Earned Value (EV), and Actual Cost (AC). Schedule Performance Index (SPI) = EV/PV; Cost Performance Index (CPI) = EV/AC.

**ECO (Engineering Change Order):** The formal change control mechanism for modifying baselined artifacts after a program milestone. Required for all post-CDR design changes.

### F

**FTA (Fault Tree Analysis):** Top-down failure analysis. Starts from an undesired top-level event (e.g., cell overcharge) and decomposes into combinations of lower-level failures using AND/OR gates. Used in Chapter 9 (§9.8) to verify the 3-tier protection architecture achieves 10⁻⁹/hour failure probability.

**FSR (Functional Safety Requirement):** Requirements derived from safety goals that must be implemented to prevent hazardous events. FSRs are ASIL-rated and flow from HARA → safety goals → FSRs → architecture allocation.

**Freedom from Interference:** ISO 26262 requirement that ASIL-D functions cannot be corrupted by lower-ASIL functions sharing the same processor. Achieved in the IM-e1 BMS via MPU partitioning of Core 0 (ASIL-D) and Core 1 (ASIL-B) on the STM32H755.

### H

**HARA (Hazard Analysis and Risk Assessment):** ISO 26262 Part 3 process for identifying hazardous events, rating their Severity (S), Exposure (E), and Controllability (C), and deriving ASIL ratings. Chapter 3 (§3.3) contains the full IM-e1 BMS HARA with six hazardous events.

**HIL (Hardware-in-the-Loop):** Test environment where real hardware (MBMS PCB) interfaces with a real-time simulation of the surrounding system (battery pack, vehicle, charger). The IM-e1 BMS HIL rig uses dSPACE SCALEXIO.

**HPPC (Hybrid Pulse Power Characterization):** Battery test protocol for identifying equivalent circuit model parameters. A series of charge/discharge pulses of specific magnitude and duration are applied, and the voltage response is used to fit R₀, R₁, C₁, R₂, C₂ for the 2RC Thevenin model.

### I

**ICD (Interface Control Document):** Document defining all interfaces between system elements: signal name, type, protocol, voltage range, update rate, and ASIL level. The BMS ICD (Chapter 4, §4.4) defines 13 interfaces (IFC-01 to IFC-13).

**IP67:** Ingress Protection rating per IEC 60529. "6" = dust-tight; "7" = immersion in up to 1m of water for 30 minutes. Mandatory for the IM-e1 BMS enclosure per AIS-048.

**isoSPI:** Texas Instruments' isolated SPI variant used for daisy-chain communication between BQ76940 CMC ICs. Provides galvanic isolation (up to 1000V) for the high-voltage daisy-chain communication path.

**ISO 26262:** International standard for functional safety of road vehicles. Consists of 12 parts covering the entire safety lifecycle from concept (Part 3) through hardware (Part 5), software (Part 6), and validation (Part 4). The IM-e1 BMS follows ISO 26262 for all safety-classified functions.

### L

**LFP (LiFePO₄ — Lithium Iron Phosphate):** The cell chemistry selected for the IM-e1 (Trade Study 1, Chapter 5). Key properties: thermal runaway onset at ~270°C (safest of common chemistries), flat OCV-SOC curve (challenging for SOC estimation), 3,000–4,000 cycle life, lower energy density than NMC, no cobalt (supply security).

**LCC (Life Cycle Cost):** Total cost of a system across its full life, from development through disposal. The IM-e1 BMS LCC is ₹33,500 per unit over a 12-year vehicle life, dominated by manufacturing cost (₹18,000 BoM), not development cost (₹6.0 Cr program / 10,000 units = ₹6,000/unit).

**LDRA:** A software verification tool suite that measures code coverage (statement, branch, MC/DC) and enforces MISRA-C rules. Required for ASIL-D software development (INF-06 in the infrastructure plan).

### M

**MBMS (Master Battery Management System):** The central processing node in the BMS hierarchy. Runs SOC/SOH algorithms, issues contactor commands, manages fault arbitration, and communicates with the VCU. Implemented on the STM32H755 dual-core MCU.

**MBSE (Model-Based Systems Engineering):** Systems engineering approach using formal models (SysML diagrams) rather than text documents as primary artifacts. Chapter 4 (§4.5) maps the 4-view architecture to SysML diagram types.

**MC/DC (Modified Condition/Decision Coverage):** The most stringent software test coverage criterion, required for ASIL-D software per ISO 26262 Part 6. Each condition in every decision must independently affect the decision outcome. Harder to achieve than branch coverage; requires systematic test case design.

**MCDA (Multi-Criteria Decision Analysis):** Structured decision method assigning weights to criteria and scoring alternatives. Used for both trade studies in Chapter 5. Produces a weighted score for each alternative; highest score wins (subject to constraint filters).

**MISRA-C:** A subset of C programming language designed for safety-critical embedded systems. Prohibits dynamic memory allocation, unrestricted recursion, and other constructs that reduce code safety and analysability. Required for all ASIL-rated software in the IM-e1 BMS.

**MPU (Memory Protection Unit):** Hardware unit in the STM32H755 that enforces memory access boundaries between software partitions. Prevents Core 1 (ASIL-B) software from corrupting Core 0 (ASIL-D) memory — implementing "Freedom from Interference."

### O

**OBC (On-Board Charger):** The AC charging unit mounted in the vehicle. Converts AC grid power (Type 2 connector, up to 11kW in the IM-e1) to DC for pack charging. The BMS communicates with the OBC via CAN to set charging current limits.

**OCV (Open-Circuit Voltage):** Battery terminal voltage measured after sufficient rest (typically >2 hours) with no current flowing. The OCV-SOC curve maps OCV to SOC. For LFP, this curve is nearly flat between 20%–80% SOC, making OCV-based SOC estimation unreliable in that region.

**OTA (Over-the-Air update):** Software update delivered wirelessly via the vehicle's telematics module. The IM-e1 BMS supports OTA updates for SOC/SOH algorithm improvements post-launch (SN-14 from Chapter 2).

### P

**Passive Balancing:** Cell balancing method that dissipates excess energy from higher-SOC cells as heat through bleed resistors, until all cells reach the same voltage. Simpler and cheaper than active balancing; selected for IM-e1 due to LFP flat OCV curve reducing balancing urgency.

**PPAP (Production Part Approval Process):** Supplier qualification standard (AIAG) ensuring production parts meet engineering requirements before volume production begins. Required at Level 3 for the TI BQ76940 CMC IC supply.

**PID (Proportional-Integral-Derivative):** Classic feedback control algorithm. The IM-e1 BMS thermal control system uses nested PID loops: outer loop controls cell temperature setpoint; inner loop controls coolant pump speed.

### R

**RLS (Recursive Least Squares):** Adaptive algorithm that updates model parameters in real-time using incoming measurements. Used to update the 2RC Thevenin model's Qmax (capacity) parameter as the LFP cells age, keeping the EKF SOC estimate accurate over time.

**RPN (Risk Priority Number):** DFMEA metric = Severity × Occurrence × Detection. Higher = more critical. Chapter 9 (§9.7) uses RPN to prioritize design improvements.

### S

**SOC (State of Charge):** Estimate of remaining energy in the battery, expressed as a percentage of current capacity (0% = fully discharged, 100% = fully charged). The primary information displayed to the driver. SR-F-01 requires SOC accuracy ≤2%.

**SOH (State of Health):** Estimate of battery capacity relative to its original capacity. SOH = 100% when new; design life requires SOH ≥80% after 8 years. Estimated by the RLS algorithm tracking Qmax degradation.

**STM32H755:** STMicroelectronics dual-core MCU (ARM Cortex-M7 at 480 MHz + Cortex-M4 at 240 MHz). Selected as the MBMS MCU for its ASIL-D certification support, dual-core partitioning capability, and rich peripheral set (CAN-FD, SPI, LIN, Ethernet).

### T

**Thevenin Equivalent Circuit (2RC model):** Electrical model of a battery cell consisting of: Voc (OCV source) + R₀ (ohmic resistance) + two parallel RC branches (R₁C₁, R₂C₂) modelling diffusion dynamics. The state variables of this model (along with SOC) form the EKF state vector.

**Thermal Runaway:** Exothermic self-heating cascade in a Li-ion cell. Once cell temperature exceeds the threshold for electrolyte decomposition (~150°C for LFP, ~210°C for NMC), the reaction accelerates faster than heat can be dissipated → cell venting, fire, or explosion. The BMS's most critical safety function is preventing thermal runaway.

### U

**UDS (Unified Diagnostic Services):** ISO 14229 diagnostic protocol used for reading DTCs, live data, and programming over OBD-II. Service technicians use UDS tools (e.g., ETAS INCA, Autel Scanner) to access BMS fault codes without opening the enclosure.

### V

**V-Model:** Systems engineering lifecycle model in which each decomposition stage on the left side of the "V" is paired with a verification activity on the right side. Unit code (left bottom) → Unit test (right bottom); System requirements (left top) → System validation (right top).

**VCU (Vehicle Control Unit):** The central controller of the electric vehicle that orchestrates torque commands, charging sessions, and thermal management. The BMS is a slave to the VCU for operational commands; the VCU receives SOC, fault status, and current limits from the BMS via CAN.

### W

**WBS (Work Breakdown Structure):** Hierarchical decomposition of program work into manageable packages. The IM-e1 BMS WBS has three levels: Program → Phase → Work Package. Used as the basis for schedule, resource, and cost planning (Chapter 8, §8.2).

---

## Recommended Study Sequence

**For a first read (complete case study, ~4.5 hours):**
Ch 1 → Ch 2 → Ch 3 → Ch 4 → Ch 5 → Ch 6 → Ch 7 → Ch 8 → Ch 9

**For a focused SE processes review (~2 hours):**
Ch 3 (Requirements + HARA) → Ch 5 (Trade Studies) → Ch 7 (IV&V) → Ch 9 (Risk + DFMEA)

**For a functional safety deep dive (~2 hours):**
Ch 3 §3.3–3.4 (HARA → Safety Goals → FSRs) → Ch 6 §6.4 (3-tier protection) → Ch 7 §7.6 (ISO 26262 V&V) → Ch 9 §9.7–9.8 (DFMEA + FTA)

**For project management focus (~1.5 hours):**
Ch 8 (full — WBS, EVM, LCC, CM) → Ch 9 §9.1–9.5 (Risk Register + mitigations)

---

*This case study was developed for AEL ZG517 / AE ZG517 Automotive Systems Engineering, BITS Pilani WILP. All companies, products, and individuals named are fictional. Technical specifications are illustrative and based on publicly available data for representative components.*
