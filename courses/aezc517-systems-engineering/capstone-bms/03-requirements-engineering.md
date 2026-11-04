# Chapter 3: Requirements Engineering

> **SE Processes Applied:** System Requirements Definition (ISO/IEC 15288 §6.4.3), System Analysis — HARA (ISO 26262 Part 3)
> **AEZC517 Sessions Referenced:** Session 4 (Requirements Engineering), Session 12 (Specialty Engineering: Safety & Security)
> **Estimated Reading Time:** 35 minutes

---

## 3.1 Requirements Development Process

System requirements for the IM-e1 BMS were developed through a structured four-step process consistent with ISO/IEC 15288 §6.4.3 and ISO 26262 Part 3:

**Step 1 — Elicitation:** Stakeholder needs (SN-01 through SN-26 from Chapter 2) are the primary input. Each need is the raw material for one or more requirements.

**Step 2 — Derivation and Analysis:** Needs are elaborated into verifiable requirement statements. Safety-related needs are subjected to HARA (Hazard Analysis and Risk Assessment) per ISO 26262 to determine ASIL ratings. Derived requirements (not directly from any single SN but implied by the system context) are also captured.

**Step 3 — Documentation:** Each requirement is documented with: ID, category, statement, rationale, source (SN-ID), ASIL level, and verification method.

**Step 4 — Validation:** Requirements are reviewed by all stakeholder representatives (SH-01 through SH-08 proxies) to confirm they correctly capture needs. Conflicts identified in Chapter 2 are resolved in the requirements as documented.

---

## 3.2 System Requirements

Requirements are organized into six categories: Functional (SR-F), Performance (SR-P), Safety (SR-S), Environmental (SR-E), Communication (SR-C), and Lifecycle (SR-LC).

| Req ID | Category | Requirement Statement | Source (SN-ID) | ASIL | Verification Method |
|---|---|---|---|---|---|
| **SR-F-01** | Functional | The BMS shall estimate the State of Charge (SOC) of the battery pack with an error of ≤2% across the full SOC operating range (15%–95%) and temperature range (-10°C to +55°C). | SN-01 | ASIL-B | Test (TC-01, TC-06) |
| **SR-F-02** | Functional | The BMS shall generate a low-SOC warning signal to the VCU when SOC reaches 15% (physical), displayed as 0% on the instrument cluster. | SN-02 | ASIL-B | Test (HIL, TC-06) |
| **SR-F-03** | Functional | The BMS shall estimate the State of Health (SOH) of the battery pack with an error of ≤5% after each complete charge-discharge cycle. | SN-03, SN-25 | QM | Test (battery cycler) |
| **SR-F-04** | Functional | The BMS shall perform passive cell balancing during charging to equalize individual cell voltages to within ±10 mV across all cells in a module. | SN-03 | QM | Test (cell voltage measurement at end of charge) |
| **SR-F-05** | Functional | The BMS shall control the main positive contactor, main negative contactor, and pre-charge contactor independently. | SN-04, SN-11 | ASIL-D | Test (contactor state verification) |
| **SR-F-06** | Functional | The BMS shall monitor insulation resistance between the HV bus and vehicle chassis. Insulation resistance below 100 Ω/V (i.e., <40 kΩ for a 400V system) shall generate a fault. | SN-04, SN-15 | ASIL-B | Test (HIL with insulation fault injection) |
| **SR-F-07** | Functional | The BMS shall provide a State of Health report accessible via OBD-II UDS (ISO 14229) service $22 at any time the BMS is powered. | SN-25, SN-18 | QM | Inspection (UDS readout) |
| **SR-F-08** | Functional | The BMS shall enter a safe discharge state (contactors open, SOC recorded) upon receipt of an End-of-Life service command via UDS service $31. | SN-26 | QM | Test (UDS command, verify contactor state) |
| **SR-P-01** | Performance | The BMS shall respond to a Tier-1 fault condition (hardware comparator trigger) by opening all contactors within ≤1 ms of fault detection. | SN-04, SN-15 | ASIL-D | Test (TC-05, fault injection oscilloscope timing) |
| **SR-P-02** | Performance | The BMS shall respond to a Tier-2 fault condition (software detection) by commanding contactor open within ≤10 ms of fault detection. | SN-04, SN-15 | ASIL-D | Test (TC-04, TC-05, timing measurement) |
| **SR-P-03** | Performance | The BMS shall limit maximum discharge power to 30% of rated capacity when any cell temperature is below 0°C, and prohibit charging when any cell temperature is below -10°C. | SN-06 | ASIL-B | Test (HIL thermal simulation at -10°C) |
| **SR-P-04** | Performance | The BMS shall derate maximum discharge power by 20% per °C above 45°C cell temperature, reaching 0% at 55°C. | SN-05, SN-15 | ASIL-B | Test (HIL thermal simulation, TC-04) |
| **SR-P-05** | Performance | The BMS shall transmit all scheduled CAN messages to the VCU within ≤5 ms of their nominal transmission time under all operating conditions. | SN-07, SN-11 | ASIL-B | Test (CAN bus analyzer, message timing) |
| **SR-S-01** | Safety (ASIL-D) | The BMS shall prevent any cell voltage from exceeding 3.65V during charging by measuring each cell voltage via two independent measurement paths and triggering hardware cutoff on either path. | SN-04, SN-15, SN-16 | **ASIL-D** | Test (TC-05 — dual path fault injection) |
| **SR-S-02** | Safety (ASIL-D) | The BMS shall prevent any cell voltage from falling below 2.50V during discharge by measuring each cell voltage via two independent measurement paths and triggering hardware cutoff on either path. | SN-04, SN-15 | **ASIL-D** | Test (fault injection, under-voltage trigger) |
| **SR-S-03** | Safety (ASIL-D) | The BMS shall detect a cell temperature rise rate exceeding 2°C/second and open all contactors within 100 ms of detection. This thermal runaway detection function shall operate independently of the SOC estimation algorithm. | SN-04, SN-23 | **ASIL-D** | Test (TC-04 — thermal injection, rise rate trigger) |
| **SR-S-04** | Safety (ASIL-C) | The BMS shall prevent any cell temperature from exceeding 55°C during charging by commanding a reduction in charge current to zero within ≤10 ms of the threshold being exceeded. | SN-04, SN-15 | ASIL-C | Test (TC-04, TC-08 — thermal overtemperature) |
| **SR-S-05** | Safety (ASIL-B) | The BMS shall limit DC fast charge current when cell temperature exceeds 42°C, reducing the current limit by 10% per °C above 42°C, reaching 0A at 55°C. | SN-09 | ASIL-B | Test (TC-08 — DCFC thermal response) |
| **SR-S-06** | Safety (ASIL-B) | The BMS shall detect contactor welding fault by measuring contactor state feedback within 500 ms of each contactor command and generating a DTC if the measured state does not match the commanded state. | SN-17 | ASIL-B | Test (contactor feedback simulation, fault injection) |
| **SR-S-07** | Safety (QM) | The BMS shall enter a safe state (contactors open, low-power monitoring) within 1 second of detecting loss of CAN communication from the VCU for more than 500 ms. | SN-04 | QM | Test (TC-07 — CAN dropout) |
| **SR-E-01** | Environmental | The BMS shall operate within specification in ambient temperatures from -10°C to +55°C (cell operating range) and storage temperatures from -30°C to +60°C. | SN-05, SN-06, SN-15 | QM | Test (TC-09 — thermal chamber) |
| **SR-E-02** | Environmental | The BMS electronics enclosure shall meet IP67 protection per IEC 60529 (dusttight and immersion-protected for 30 minutes at 1 m depth). | SN-15, SN-20 | QM | Test (IP67 test per IEC 60529) |
| **SR-E-03** | Environmental | The BMS shall meet EMC requirements per CISPR 25 (radiated emissions) and ISO 11452 (immunity) as required by AIS-004. | SN-11 | QM | Test (EMC lab, ARAI) |
| **SR-C-01** | Communication | The BMS shall transmit SOC, SOH, maximum discharge power limit, maximum charge power limit, cell temperature (max and min), and fault status to the VCU via CAN-A at 500 kbps with a message cycle time of 100 ms. | SN-01, SN-07 | ASIL-B | Test (CAN analyzer, message content and timing) |
| **SR-C-02** | Communication | The BMS shall communicate with DC fast chargers using the CCS Combo 2 protocol, providing charge current limit updates at minimum 100 ms cycle time during DCFC sessions. | SN-21, SN-22 | ASIL-B | Test (TC-08 — DCFC session simulation) |
| **SR-C-03** | Communication | The BMS shall make SOH, cumulative energy throughput, and fault history data available via OBD-II UDS service $22 (Read Data By Identifier) and $19 (Read DTC Information). | SN-10, SN-18 | QM | Inspection (UDS tool readout) |
| **SR-LC-01** | Lifecycle | The BMS shall be designed for a service life of 8 years or 150,000 km (whichever occurs first), with battery SOH ≥80% at end of life under normal usage patterns. | SN-03 | QM | Analysis (degradation model, cycle life testing) |

---

## 3.3 Hazard Analysis and Risk Assessment (HARA)

The HARA is performed per ISO 26262 Part 3. For each hazardous event, three parameters are assessed:

- **Severity (S):** S0 (no injuries) → S1 (light injuries) → S2 (serious injuries) → S3 (life-threatening/fatal)
- **Exposure (E):** E0 (incredibly unlikely) → E1 (very low) → E2 (low) → E3 (medium) → E4 (high — occurs in most operating situations)
- **Controllability (C):** C0 (controllable by almost all drivers) → C1 (simply controllable) → C2 (normally controllable) → C3 (difficult to control / uncontrollable)

**ASIL = f(S, E, C)** per ISO 26262 Table 4 (S3+E4+C3 → ASIL-D, the highest).

| Hazard ID | Hazardous Event | Operational Situation | Severity | Exposure | Controllability | ASIL | Safety Goal |
|---|---|---|---|---|---|---|---|
| **H-01** | Cell voltage exceeds Vmax (overcharge: >3.65V/cell) | Charging at DCFC or OBC | S3 — lithium plating → thermal runaway → fire; fatal outcome possible | E4 — every charging session; vehicle charges daily | C3 — driver has no way to detect or prevent battery overcharge | **ASIL-D** | SG-01: BMS shall prevent any cell from being overcharged under all operating conditions, including single hardware failure |
| **H-02** | Cell voltage falls below Vmin (over-discharge: <2.50V/cell) | Highway driving at low SOC; continuous high-current discharge | S2 — irreversible cell damage → accelerated degradation; fire risk lower than overcharge | E3 — occurs multiple times per year for drivers who deplete battery | C2 — driver can respond to low-range warning if alerted | **ASIL-B** | SG-02: BMS shall prevent any cell from being over-discharged under normal and single-fault conditions |
| **H-03** | Cell temperature exceeds 55°C during charging | DCFC charging in peak Indian summer (45°C ambient) | S3 — thermal runaway onset above 60°C for LFP; fire hazard adjacent to occupied spaces | E3 — peak summer DCFC sessions, approximately 30–90 days/year in Rajasthan/Delhi | C3 — thermal runaway in charging vehicle is uncontrollable; driver may not be present | **ASIL-D** | SG-03: BMS shall prevent cell temperature from exceeding 55°C during any charging or discharging event |
| **H-04** | BMS loses CAN communication with VCU while vehicle is moving | Highway driving, BMS MCU reset or CAN bus-off event | S2 — VCU cannot enforce power limits; potential for uncontrolled acceleration or regenerative braking anomaly | E2 — low frequency event; MCU reset unlikely in normal operation | C2 — driver can apply brakes; vehicle has mechanical braking | **ASIL-B** | SG-04: BMS shall enter a defined safe state within 1 second of loss of VCU CAN communication |
| **H-05** | Contactor fails to open when commanded (contactor welding) | Following a fault event (overcharge, overtemperature) where BMS commands contactors to open | S3 — if welded contactors prevent isolation after a fault, thermal runaway can proceed unimpeded; fire/explosion risk | E2 — contactor welding is a low-frequency failure mode in normal operation | C3 — welded contactors are invisible to driver; system appears to have faulted safely but HV remains connected | **ASIL-C** | SG-05: BMS shall detect contactor welding fault and notify VCU within 500 ms of any contactor operation |
| **H-06** | BMS reports incorrect SOC (>10% error), causing unexpected range depletion | Highway driving; driver trusts SOC display; actual SOC much lower than displayed | S1 — vehicle stops unexpectedly in traffic; minor accident risk from unexpected stop | E4 — SOC is displayed every drive cycle; error could persist undetected | C2 — driver can observe vehicle slowing; applies brakes; low-speed stop likely | **ASIL-A** | SG-06: BMS shall estimate and report SOC with error ≤5% under all operating conditions (tightened to ≤2% for full requirement per SN-01) |

---

## 3.4 Safety Goals and Functional Safety Requirements

The HARA safety goals are refined into Functional Safety Requirements (FSRs) — the specific design-level requirements that realize each safety goal.

### Safety Goal SG-01 (ASIL-D): Prevent Overcharge

**Hazard:** H-01 — Cell overcharge → thermal runaway → fire

**Safety Goal:** "BMS shall prevent any cell from being overcharged under all operating conditions, including single hardware failure"

**Functional Safety Requirements derived:**

| FSR-ID | Functional Safety Requirement | ASIL |
|---|---|---|
| FSR-01-A | BMS shall measure each cell voltage using two independent measurement paths (CMC IC primary + MBMS secondary plausibility check) | ASIL-D |
| FSR-01-B | BMS shall trigger hardware contactor cutoff (Tier 1, ≤1 ms) if any cell voltage exceeds 3.65V on the primary measurement path, independent of software | ASIL-D |
| FSR-01-C | BMS shall trigger software contactor cutoff (Tier 2, ≤10 ms) if any cell voltage exceeds 3.60V on the secondary path | ASIL-D |
| FSR-01-D | Overcharge protection function shall be implemented in the ASIL-D software partition of the MBMS, with MC/DC code coverage | ASIL-D |

**Traceability:** FSR-01-A → SR-S-01; FSR-01-B → SR-P-01; FSR-01-C → SR-P-02

---

### Safety Goal SG-03 (ASIL-D): Prevent Overtemperature

**Hazard:** H-03 — Cell temperature exceeds 55°C → thermal runaway

**Safety Goal:** "BMS shall prevent cell temperature from exceeding 55°C during any charging or discharging event"

**Functional Safety Requirements derived:**

| FSR-ID | Functional Safety Requirement | ASIL |
|---|---|---|
| FSR-03-A | BMS shall monitor cell temperature from at least 2 NTC thermistors per module (8 modules = minimum 16 temperature sensors) | ASIL-C |
| FSR-03-B | BMS shall detect a cell temperature rise rate >2°C/s (thermal runaway precursor) and open contactors within 100 ms | ASIL-D |
| FSR-03-C | BMS shall command maximum coolant flow when any cell temperature exceeds 42°C | ASIL-B |
| FSR-03-D | Thermal runaway detection shall be implemented independent of the SOC estimation algorithm (separate software partition) | ASIL-D |

**Traceability:** FSR-03-A → SR-F-06 (derived); FSR-03-B → SR-S-03; FSR-03-C → SR-S-04; FSR-03-D → SW architecture (Ch 4)

---

### Full Safety Goal Chain Summary

| Safety Goal | Hazard | ASIL | Key FSR | System Requirement |
|---|---|---|---|---|
| SG-01: No overcharge | H-01 | ASIL-D | FSR-01-A/B/C/D | SR-S-01, SR-P-01, SR-P-02 |
| SG-02: No over-discharge | H-02 | ASIL-B | FSR-02-A/B | SR-S-02, SR-F-02 |
| SG-03: No overtemperature | H-03 | ASIL-D | FSR-03-A/B/C/D | SR-S-03, SR-S-04, SR-P-04 |
| SG-04: Safe comms loss | H-04 | ASIL-B | FSR-04-A | SR-S-07 |
| SG-05: Contactor welding | H-05 | ASIL-C | FSR-05-A | SR-S-06 |
| SG-06: SOC accuracy | H-06 | ASIL-A | FSR-06-A | SR-F-01 |

---

## 3.5 Requirements Quality Assessment

Requirements are assessed against six INCOSE quality attributes. Five selected requirements are evaluated below, with a before/after example for one poor requirement:

**Quality Rating Key:** ✅ Pass | ⚠️ Partial | ❌ Fail

| Req ID | Complete | Verifiable | Traceable | Unambiguous | Consistent | Feasible | Overall |
|---|---|---|---|---|---|---|---|
| SR-F-01 (SOC accuracy ≤2%) | ✅ | ✅ (test TC-01 defined) | ✅ (SN-01) | ✅ (2% is quantified) | ✅ | ✅ (EKF achievable) | ✅ **PASS** |
| SR-S-01 (No overcharge, ASIL-D) | ✅ | ✅ (TC-05 defined) | ✅ (SN-04, SN-15, SN-16) | ✅ (3.65V defined, dual path) | ✅ | ✅ (CMC IC supports) | ✅ **PASS** |
| SR-P-01 (Tier-1 fault ≤1ms) | ✅ | ✅ (oscilloscope timing) | ✅ (SN-04) | ✅ (1ms is quantified) | ✅ | ✅ (hardware comparator spec) | ✅ **PASS** |
| SR-E-02 (IP67) | ✅ | ✅ (IEC 60529 test) | ✅ (SN-15, SN-20) | ✅ (IP67 is standard-defined) | ✅ | ✅ (enclosure design) | ✅ **PASS** |
| SR-LC-01 (8 years / 80% SOH) | ⚠️ Partial | ⚠️ (analysis, not direct test) | ✅ (SN-03) | ✅ | ✅ | ⚠️ (LFP cycle life must be validated) | ⚠️ **PARTIAL** |

**Before/After Example — Improving a Poor Requirement:**

> ❌ **Poor (original draft):** "The BMS should keep the battery safe during charging."
>
> Problems: "should" (not mandatory), "safe" (unmeasurable), "during charging" (which charging type?), no ASIL, no verification method, no source.

> ✅ **Improved (SR-S-01):** "The BMS shall prevent any cell voltage from exceeding 3.65V during charging by measuring each cell voltage via two independent measurement paths and triggering hardware cutoff on either path." [Source: SN-04, SN-15, SN-16 | ASIL-D | Verification: Test TC-05]
>
> Improvements: "shall" (mandatory), 3.65V (measurable), dual-path (design-level specificity), ASIL-D assigned, TC-05 defines the test.

**Key lesson:** The word "should" in a requirement means "optional" and is almost always wrong in safety-critical engineering. Use "shall" for mandatory requirements.

---

## 3.6 Requirements Traceability Matrix (Excerpt)

The full requirements traceability matrix (RTM) spans from stakeholder need → system requirement → architecture element → verification test. An excerpt showing the most critical chain:

| SN-ID | Need Summary | SR-ID | Requirement Summary | Architecture Element (Ch 4) | Verification Test (Ch 7) |
|---|---|---|---|---|---|
| SN-01 | Accurate SOC display | SR-F-01 | SOC accuracy ≤2% | MBMS: EKF algorithm in ASW layer | TC-01 (unit), TC-06 (HIL drive cycle) |
| SN-04 (safety) | Safe charging — no fire | SR-S-01 | No overcharge, ASIL-D | MBMS: Tier-1 HW comparator + Tier-2 SW partition; dual CAN to VCU | TC-05 (HIL fault injection) |
| SN-04 (safety) | Safe charging — no fire | SR-S-03 | Thermal runaway detection | MBMS: rate-of-rise detector in ASIL-D SW partition | TC-04 (HIL thermal ramp) |
| SN-06 | Cold start at -5°C | SR-P-03 | Discharge limit at low temp | MBMS: temperature-indexed power limit table | TC-09 (thermal chamber) |
| SN-09 | DCFC longevity | SR-S-05 | DCFC current derate above 42°C | MBMS: thermal management CAN message to charger | TC-08 (DCFC session HIL) |
| SN-17 | Contactor welding detection | SR-S-06 | Welding fault detection ≤500 ms | MBMS: contactor feedback input, state machine | DTC verification test |
| SN-21 | CCS Combo 2 interface | SR-C-02 | DCFC CAN protocol compliance | MBMS: CAN-B DCFC stack | TC-08 (DCFC communication test) |
| SN-25 | SOH at EOL | SR-F-03 | SOH estimation ≤5% error | MBMS: SOH algorithm, UDS service $22 | Battery cycler validation |

---

## 3.7 SE Process Reflection

### What Requirements Were Missing from MCAS? (Session 6 Connection)

In the Boeing 737 MAX MCAS case study (Session 6), the failure analysis revealed several missing or violated requirements:

| MCAS Failure | Equivalent BMS Requirement | How We Addressed It |
|---|---|---|
| No redundant AOA sensor requirement | SR-S-01, FSR-01-A: dual independent measurement paths | We explicitly require two independent cell voltage measurement paths for ASIL-D |
| No authority limit requirement (MCAS went from 0.6° to 2.5° without re-analysis) | SR-P-01, SR-P-02: ≤1ms Tier-1, ≤10ms Tier-2 — limits are quantified | All protection thresholds are fixed and verified; any change triggers full HARA re-analysis |
| Pilots not trained on MCAS — no human factors requirement | SR-C-03, SR-C-04: UDS diagnostics, DTC requirements | Service technicians (SH-05) have explicit diagnostic requirements; fault codes are verifiable |
| No traceability when design changed | RTM in §3.6: every SR traces to SN and to verification test | Any requirement change requires RTM update — change control process (see Chapter 8) |

The MCAS disaster was, at its core, a **requirements completeness and traceability failure**. Every SR in our RTM must be verified before we certify the BMS.

### How ASIL Ratings Drive Architecture (Bridge to Chapter 4)

The ASIL ratings from the HARA are not just labels — they directly constrain the architecture:

- **ASIL-D** functions (SR-S-01, SR-S-03) → require independent hardware and software paths → drives the dual-core STM32H755 selection and hardware comparator in CMC IC
- **ASIL-D** software → requires MC/DC coverage, formal verification → drives AUTOSAR safety partition in SW architecture
- **ASIL-B** functions → single-point monitoring acceptable, software verification sufficient → drives which functions share MCU resources

Chapter 4 will show exactly how these ASIL assignments from the HARA translate into architectural decisions.

### ISO 26262 Standards Referenced

- **ISO 26262 Part 3:** Concept phase — HARA methodology used in §3.3
- **ISO 26262 Part 4:** System level — V&V requirements (applied in Chapter 7)
- **ISO 26262 Part 6:** Software level — ASIL-D code coverage requirements (applied in Chapter 4 SW architecture)

---

*Next: [Chapter 4 — System Architecture](04-system-architecture.md)*
