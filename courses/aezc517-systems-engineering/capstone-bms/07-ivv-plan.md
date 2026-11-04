# Chapter 7: Integration, Verification & Validation

> **SE Processes Applied:** Integration (ISO/IEC 15288 §6.4.8), Verification (§6.4.9), Validation (§6.4.10)
> **AEZC517 Sessions Referenced:** Session 8 (Verification & Validation), Session 12 (Functional Safety V&V)
> **Estimated Reading Time:** 30 minutes

---

## 7.1 IV&V Strategy Overview

Integration, Verification, and Validation (IV&V) are three distinct but related processes:

| Process | Question Answered | Standard | IM-e1 BMS Application |
|---|---|---|---|
| **Integration** | "Does this assembly work together?" | ISO/IEC 15288 §6.4.8 | Incrementally assembling CMC → MBMS → Pack → Vehicle |
| **Verification** | "Did we build the system right?" (vs. requirements) | ISO/IEC 15288 §6.4.9 | Demonstrating all SR-IDs are met by test, analysis, or inspection |
| **Validation** | "Did we build the right system?" (vs. stakeholder needs) | ISO/IEC 15288 §6.4.10 | Confirming real-world performance matches SN-IDs from Chapter 2 |

The distinction matters: a system can pass all verification tests (requirements met) but fail validation (stakeholder needs not truly satisfied). The Boeing 737 MAX MCAS system arguably passed verification — MCAS worked as specified — but failed validation because the specification was wrong.

### IV&V Independence Requirements

Per ISO 26262 Part 2 §6.4.8 (Independence of Safety Lifecycle Activities):

| ASIL Level | Minimum Test Independence |
|---|---|
| ASIL-D | Independent test team — must not be the implementer |
| ASIL-B | Independence recommended (different engineer, same team acceptable) |
| ASIL-A / QM | No formal independence requirement |

For the IM-e1 BMS:
- **Overcharge protection (SR-S-01, ASIL-D):** Verified by IndraMotors Functional Safety Verification team — separate from the design team
- **Thermal runaway detection (SR-S-04, ASIL-D):** Verified by external ARAI test facility
- **All other ASIL-B requirements:** Verified by V&V engineering team (different engineers from design)

---

## 7.2 V-Model Application

The V-Model maps each decomposition activity on the left side to a verification/validation activity on the right side. Every left-side artifact has a corresponding right-side test activity that verifies it.

```
DECOMPOSITION (Left Side)              VERIFICATION (Right Side)
─────────────────────────────────      ─────────────────────────────────────

System Requirements (Ch 3)    ─────────────────────────────────► System Validation
(SRS Baseline, M2)                                               (Field fleet, M7)

 Subsystem Specifications     ─────────────────────────────► Pack-Level Verification
 (MBMS spec, CMC spec)                                      (TC-06 to TC-09, M7)

  SW Architecture Spec   ──────────────────────────► HIL Integration Test
  (AUTOSAR layers)                                   (TC-04, TC-05, TC-07, M6)

   Software Unit Spec   ──────────────────────────► SW Integration Test
   (EKF module, FDD)                                (TC-02, TC-03, M5)

    Code Units          ────────────────────────► Unit Tests
    (C modules)                                  (TC-01, M4)
```

### V-Model Stage Details

| Stage | Left-Side Input | Right-Side Activity | Test Environment | Exit Criteria |
|---|---|---|---|---|
| **L1/R1: Unit** | Code units (C functions per AUTOSAR ASW module) | Unit test per module; LDRA code coverage | PC simulation, MISRA-C analysis | Statement coverage ≥100%, branch coverage ≥95% |
| **L2/R2: SW Integration** | AUTOSAR BSW/RTE/ASW integration | SW integration tests; CAN stack, fault handler | MBMS development board | All inter-module interfaces pass protocol test |
| **L3/R3: HIL Integration** | Full BMS SW on MCU + HIL plant model | Hardware-in-the-loop; inject fault scenarios | dSPACE SCALEXIO HIL rig | All TC-01 to TC-07 pass |
| **L4/R4: Pack-Level** | BMS hardware + battery module (real cells) | Functional tests on actual LFP pack | Battery lab with safety enclosure | All TC-08 to TC-09 pass |
| **L5/R5: Vehicle Integration** | BMS installed in IM-e1 prototype vehicle | Drive cycle tests; OBD-II diagnostics | Proving ground | CAN integration, DTC readback verified |
| **L6/R6: Field Validation** | Full production-intent BMS in 50 prototype vehicles | 5,000 km validation fleet | Public roads + structured test | SN-01 to SN-26 stakeholder needs confirmed |

---

## 7.3 Integration Strategy

### Integration Sequence

Integration follows a bottom-up, incremental strategy. Each stage integrates one additional assembly level and runs a regression test suite before proceeding.

```
Stage 1: CMC IC Bench Test
└── TI BQ76940 on bench → verify voltage measurement accuracy (±2mV)
    → verify SPI communication to MBMS development board

Stage 2: CMC-to-MBMS Integration
└── All 4 CMC ICs connected to MBMS development board
    → verify 56-cell data collection at 10ms cycle
    → verify isoSPI chain integrity (daisy-chain fault isolation)

Stage 3: BMS Hardware-in-the-Loop
└── MBMS PCB connected to dSPACE SCALEXIO
    → real-time plant model simulates 40 kWh LFP pack
    → BMS SW runs on target MCU (STM32H755)
    → HIL injects voltage, current, temperature profiles

Stage 4: BMS + Module Integration (Real Cells)
└── MBMS connected to one real battery module (7S8P, 14 cells monitored by 1 CMC)
    → charge/discharge cycling at 0.5C, 1C, 2C rates
    → verify SOC estimation accuracy against lab Coulomb counter reference

Stage 5: Full Pack Integration
└── All 8 modules + MBMS assembled into battery pack housing
    → contactor sequencing, pre-charge verification
    → IP67 seal inspection before environmental tests

Stage 6: Vehicle Integration
└── Battery pack installed in IM-e1 prototype
    → VCU CAN integration, OBC interface verification
    → Drive-away test: verify no contactor fault on key-on
```

### Integration Issue Handling

For any anomaly discovered during integration:

1. Raise a Problem Report (PR) in the change management system
2. Classify severity: Critical (blocks integration) / Major (degrades function) / Minor (cosmetic)
3. Root cause analysis per 8D process
4. Corrective action verified before re-integration
5. All PRs tracked in the IV&V traceability database

---

## 7.4 Verification Test Cases

Ten verification test cases cover the critical requirements. Each test case includes: objective, setup, procedure, expected result, and the SR-ID it verifies.

---

### TC-01: SOC Algorithm Unit Test

| Field | Detail |
|---|---|
| **Test ID** | TC-01 |
| **Type** | Unit Test (Software) |
| **Requirement Verified** | SR-F-01 (SOC accuracy ≤2%), SR-F-02 (Low SOC alert) |
| **ASIL** | ASIL-B |
| **Test Environment** | PC simulation (Python test harness with LFP cell model) |
| **Objective** | Verify EKF SOC estimation algorithm maintains ≤2% error across a representative drive cycle |

**Procedure:**
1. Load LFP cell OCV-SOC curve and 2RC Thevenin model parameters from HPPC data (25°C baseline)
2. Inject synthetic current profile: 150A discharge (0→50% SOC), 2-hour rest, 50A charge (50→95% SOC)
3. Compare EKF SOC estimate against reference Coulomb-counter SOC at each time step
4. Measure peak absolute error and RMS error over full profile
5. Repeat with 5% initial SOC initialization error to verify convergence within 10 minutes

**Expected Results:**

| Metric | Requirement | Test Pass Threshold |
|---|---|---|
| Peak SOC error (steady state) | ≤2.0% | ≤1.8% (design margin) |
| SOC error convergence after init error | ≤10 minutes | ≤8 minutes |
| Low SOC alert trigger point | 15% SOC | 15.0% ± 0.5% SOC |

**Pass/Fail Criterion:** All three metrics within thresholds → PASS

---

### TC-02: CMC SPI Communication Integrity Test

| Field | Detail |
|---|---|
| **Test ID** | TC-02 |
| **Type** | SW Integration Test |
| **Requirement Verified** | SR-C-01 (CAN latency ≤5ms), IFC-04 (CMC isoSPI interface) |
| **ASIL** | ASIL-B |
| **Test Environment** | MBMS development board + 4× BQ76940 CMC ICs on bench |
| **Objective** | Verify isoSPI communication across all 4 CMC ICs with fault injection |

**Procedure:**
1. Configure CMC daisy chain: MBMS → CMC1 → CMC2 → CMC3 → CMC4
2. Command 100 sequential voltage measurement cycles; log all responses
3. Inject single-bit error on isoSPI line (hardware fault injection) during cycle 50
4. Verify error is detected (CRC fail), fault logged (DTC P1B03), and measurement retried within one 10ms cycle
5. Restore communication; verify normal measurement resumes within 20ms

**Expected Results:**
- Zero undetected CRC errors in 100 normal cycles
- Injected error detected on same cycle (within 10ms)
- DTC P1B03 logged correctly with timestamp
- Communication restored and normal within 20ms after fault cleared

---

### TC-03: ADC Supply Fault Graceful Degradation Test

| Field | Detail |
|---|---|
| **Test ID** | TC-03 |
| **Type** | Fault Injection Test (SW Integration) |
| **Requirement Verified** | SR-S-01 (overcharge — dual measurement path), SR-S-06 (fault detection) |
| **ASIL** | ASIL-D |
| **Test Environment** | MBMS development board, bench power supply |
| **Objective** | Verify that a partial sensor failure causes graceful degradation (fail-safe), not hard fault crash |

**Procedure:**
1. Normal BMS operation: all 56-cell voltages within normal range
2. Software command to simulate ADC channel 1 failure on MBMS (primary measurement path)
3. Verify BMS transitions from dual-path measurement to single-path mode
4. Verify DTC P1B07 (measurement path degraded) raised at Severity 2 (warning)
5. Verify BMS does NOT open contactors in this scenario (single-path still operational)
6. Then simulate ADC channel 2 failure (secondary path)
7. Verify BMS immediately opens contactors and raises DTC P1B07 at Severity 3 (protection active)

**Expected Results:**
- Single-path failure → Warning only, continued operation
- Dual-path failure → Contactors open within 10ms, ASIL-D protection active
- No MCU crash (hard fault) in either scenario — BMS transitions gracefully

---

### TC-04: Overtemperature Contactor Cutoff — HIL Test

| Field | Detail |
|---|---|
| **Test ID** | TC-04 |
| **Type** | HIL Integration Test |
| **Requirement Verified** | SR-S-03 (stop charging above 55°C cell temp), SR-S-04 (thermal runaway detection) |
| **ASIL** | ASIL-D |
| **Test Environment** | dSPACE SCALEXIO HIL rig + MBMS PCB (production-intent hardware) |
| **Objective** | Verify temperature-triggered contactor opening meets timing requirement (≤10ms for Tier 2) |

**Procedure:**
1. HIL model simulates normal pack operation at 1C charge rate, 40°C coolant inlet
2. HIL injects temperature ramp: cell 32 temperature rises 0.5°C/step every 100ms
3. Record exact timestamp when cell temperature crosses 55°C threshold
4. Record exact timestamp when contactor open command issued by BMS SW
5. Measure elapsed time: threshold crossing → contactor command
6. Separately, inject rate-of-rise: cell temperature increases at 3°C/s (>2°C/s thermal runaway threshold)
7. Verify thermal runaway detection triggers within 2 seconds of rate-of-rise onset

**Expected Results:**

| Scenario | Requirement | Pass Threshold |
|---|---|---|
| Overtemperature cutoff (55°C) | Contactor open ≤10ms | ≤10ms (Tier 2 SW) |
| Thermal runaway detection (>2°C/s) | Alert + contactor open | Within 3 seconds of onset |

**Independence Note:** This ASIL-D test executed by Functional Safety Verification team, not the BMS design team.

---

### TC-05: Overcharge Protection — HIL Fault Injection Test

| Field | Detail |
|---|---|
| **Test ID** | TC-05 |
| **Type** | HIL Integration Test |
| **Requirement Verified** | SR-S-01 (no cell exceeds 3.65V), SR-S-02 (hardware cutoff ≤1ms) |
| **ASIL** | ASIL-D |
| **Test Environment** | dSPACE SCALEXIO HIL + MBMS PCB + CMC ICs connected to HIL voltage simulation |
| **Objective** | Verify Tier 1 (hardware) AND Tier 2 (software) overcharge protection respond within spec |

**Procedure:**
1. HIL simulates all 56 cells at 3.55V (normal high-SOC)
2. Inject fault: HIL commands cell 12 voltage to ramp from 3.55V to 3.70V over 500ms (simulates charger malfunction)
3. **Tier 1 test:** Measure time from cell 12 crossing 3.65V to hardware comparator output (BQ76940 OV pin assertion) — must be ≤1ms
4. **Tier 2 test:** Verify MBMS software also detects fault and issues contactor open ≤10ms
5. Verify DTC P1B00 (cell overvoltage) logged with cell ID = 12
6. Verify that removing the fault condition does NOT automatically reset — manual reset or OBD-II command required (Safety Goal 1 from HARA)

**Expected Results:**
- Tier 1 hardware response: ≤1ms
- Tier 2 SW response: ≤10ms
- DTC P1B00 logged with correct cell ID
- No auto-reset: BMS stays in FAULT state until cleared

**Independence Note:** ASIL-D — executed by independent test team.

---

### TC-06: SOC Accuracy — WLTP Drive Cycle HIL Test

| Field | Detail |
|---|---|
| **Test ID** | TC-06 |
| **Type** | System-Level HIL Test |
| **Requirement Verified** | SR-F-01 (SOC accuracy ≤2% throughout cycle) |
| **ASIL** | ASIL-B |
| **Test Environment** | dSPACE SCALEXIO HIL + full IM-e1 vehicle model (powertrain + BMS plant model) |
| **Objective** | Verify SOC estimation accuracy across a realistic urban/highway drive profile |

**Procedure:**
1. Load WLTP Class 3 drive cycle into HIL vehicle model (1,800-second cycle, max speed 131 km/h)
2. HIL model computes pack current and temperature profiles from speed/torque demand
3. BMS SW estimates SOC in real time; HIL model tracks reference Coulomb-counter SOC
4. Log absolute SOC error at 100ms intervals throughout cycle
5. At end of cycle, compute: peak error, RMS error, mean error

**Expected Results:**

| Metric | Requirement | Pass Threshold |
|---|---|---|
| Peak absolute SOC error | ≤2.0% | ≤2.0% |
| RMS error (full cycle) | — | ≤1.2% |
| Mean error (bias) | — | ≤0.5% |

**Note:** LFP OCV flatness makes this test especially challenging between 20%–80% SOC. The EKF must rely on current integration and model dynamics (not OCV lookup) through this plateau region.

---

### TC-07: CAN Dropout Safe-State Test

| Field | Detail |
|---|---|
| **Test ID** | TC-07 |
| **Type** | HIL Integration Test |
| **Requirement Verified** | SR-C-01 (CAN 2.0B communication), SR-S-05 (VCU comms loss → safe state within 500ms) |
| **ASIL** | ASIL-B |
| **Test Environment** | dSPACE HIL with VCU simulation + BMS HIL |
| **Objective** | Verify BMS enters defined safe state when VCU CAN communication is lost |

**Procedure:**
1. Normal operation: HIL simulates VCU sending heartbeat on CAN-A (0x1A0) every 20ms
2. At T=10 seconds, disconnect CAN-A (software-simulated bus-off)
3. Measure time from last valid VCU message to BMS safe-state entry
4. Verify BMS behavior in safe state: contactors remain closed (vehicle can coast), torque limit command sent, DTC P1B06 raised
5. Restore CAN-A after 30 seconds; verify BMS resumes normal operation without manual reset

**Expected Results:**
- Safe state entered within 500ms of last valid VCU message
- Contactors remain closed (vehicle can coast to safety — do not strand driver)
- DTC P1B06 logged and visible on backup CAN-B
- Normal operation resumes within 200ms of CAN restoration

---

### TC-08: DC Fast Charge BMS Response Test

| Field | Detail |
|---|---|
| **Test ID** | TC-08 |
| **Type** | Pack-Level Functional Test (Real Cells) |
| **Requirement Verified** | SR-S-05 (temperature-derated DCFC), SR-C-02 (CCS Combo 2 communication) |
| **ASIL** | ASIL-B |
| **Test Environment** | Battery lab: 7S8P LFP module + MBMS + DCFC simulation (Chroma 17020 bidirectional) |
| **Objective** | Verify BMS correctly negotiates and limits charging current during a simulated 150kW DCFC event |

**Procedure:**
1. Start: module at 30% SOC, cell temperatures 28°C
2. Command DCFC at 150kW (375A at 400V pack voltage)
3. Monitor: cell temperatures, BMS current limit commands, SOC progression
4. After 10 minutes, heat cells to 38°C using external heater (simulating ambient condition)
5. Verify BMS reduces current setpoint per thermal derate curve (target: reduce by ≥15% at 38°C)
6. Continue charge to 95% SOC; verify charge termination at 3.65V/cell

**Expected Results:**

| Event | Expected BMS Response |
|---|---|
| Charge start at 30% SOC, 28°C | Accept 375A (150kW) |
| Cell temperature reaches 38°C | Reduce current ≥15% (≤319A) |
| Cell temperature reaches 45°C | Reduce current ≥40% (≤225A) |
| Any cell reaches 3.65V | Stop charging within 1 second |
| Charge complete at 95% SOC | Open contactors, report 100% on display |

---

### TC-09: Environmental Thermal Shock Test

| Field | Detail |
|---|---|
| **Test ID** | TC-09 |
| **Type** | Environmental / Pack-Level |
| **Requirement Verified** | SR-E-01 (operating range -10°C to +55°C), SR-E-02 (storage range -30°C to +60°C) |
| **ASIL** | QM |
| **Test Environment** | Thermal chamber (−40°C to +80°C), ARAI Environmental Test Facility |
| **Objective** | Verify BMS hardware and software function correctly after extreme temperature cycling |

**Procedure:**
1. Pre-condition BMS at 25°C for 2 hours
2. Thermal shock cycle ×5:
   - Ramp from +25°C to -30°C in 30 minutes (IEC 60068-2-14)
   - Soak at -30°C for 2 hours
   - Ramp to +60°C in 30 minutes
   - Soak at +60°C for 2 hours
3. At end of each thermal cycle: power-on BMS, measure SOC accuracy (TC-01 abbreviated), read DTC log
4. After 5 cycles: measure insulation resistance (>100MΩ per AIS-038 Annex F)

**Expected Results:**
- No loss of function after any thermal cycle
- No new DTCs raised during temperature cycling (temperature out-of-range alerts expected but not faults)
- Insulation resistance >100MΩ at all temperatures
- SOC accuracy maintained within 3% at -10°C (degraded performance at cold is acceptable; must not exceed 3%)

---

### TC-10: End-of-Charge Accuracy Validation

| Field | Detail |
|---|---|
| **Test ID** | TC-10 |
| **Type** | Pack-Level Functional Test |
| **Requirement Verified** | SR-F-01 (SOC ≤2% error), SR-F-02 (charge complete display) |
| **ASIL** | ASIL-B |
| **Test Environment** | Battery lab: full 40 kWh pack + MBMS + Chroma 17020 cycler |
| **Objective** | Verify BMS declares charge complete within 0.5% SOC accuracy of true full charge |

**Procedure:**
1. Discharge pack to 20% SOC using constant 1C current
2. Charge at 0.5C (constant current) until any cell reaches 3.65V, then CC-CV until current drops below C/20
3. When BMS declares "charge complete" (SOC = 100%), record pack energy input (Chroma internal kWh counter)
4. Compare actual energy to theoretical pack capacity (40 kWh × 0.95 = 38 kWh usable)
5. Compute actual SOC at BMS "charge complete" declaration

**Expected Results:**
- BMS declares 100% SOC within ±0.5% of true full charge
- No cell voltage exceeded 3.65V at any time
- Charge complete declaration occurs within 5 minutes of actual CV cutoff

---

## 7.5 Verification Traceability Matrix

This matrix ensures every system requirement has a designated verification method.

| Req ID | Requirement Summary | Verification Method | Test Case | IV&V Level |
|---|---|---|---|---|
| SR-F-01 | SOC accuracy ≤2% | Test | TC-01, TC-06, TC-10 | HIL + Pack |
| SR-F-02 | Low-SOC alert at 15% | Test | TC-01 | Unit |
| SR-F-03 | SOH estimation ≥±3% | Analysis + Test | TC-06 extended | Pack |
| SR-P-01 | Tier-1 cutoff ≤1ms | Test | TC-05 | HIL (independent) |
| SR-P-02 | Tier-2 SW cutoff ≤10ms | Test | TC-04, TC-05 | HIL (independent) |
| SR-P-03 | Cold start at -10°C | Test | TC-09 | Environmental |
| SR-S-01 | No cell exceeds 3.65V | Test (ASIL-D, independent) | TC-05 | HIL |
| SR-S-02 | Hardware cutoff ≤1ms | Test (ASIL-D, independent) | TC-05 | HIL |
| SR-S-03 | Stop charging above 55°C | Test | TC-04 | HIL |
| SR-S-04 | Thermal runaway detection >2°C/s | Test (ASIL-D, independent) | TC-04 | HIL |
| SR-S-05 | Temperature-derated DCFC | Test | TC-08 | Pack |
| SR-S-06 | Contactor fault detection | Test | TC-03 | SW Integration |
| SR-S-07 | EOL safe discharge state | Analysis + Inspection | — | Design review |
| SR-E-01 | Operating temp -10°C to +55°C | Test | TC-09 | Environmental |
| SR-E-02 | Storage temp -30°C to +60°C | Test | TC-09 | Environmental |
| SR-E-03 | IP67 ingress protection | Inspection + Test | ARAI facility | Pack |
| SR-C-01 | CAN 2.0B at 500kbps ≤5ms | Test | TC-07 | HIL |
| SR-C-02 | CCS Combo 2 communication | Test | TC-08 | Pack |
| SR-C-03 | Telematics CAN message | Inspection + Test | TC-07 extended | HIL |
| SR-LC-01 | ≥80% SOH at 8 years | Analysis | Cycle life model + TC-06 | Analytical |

---

## 7.6 ISO 26262 Safety V&V

### Functional Safety Verification Plan (Part 4)

ISO 26262 Part 4 (§6.4 System Design Verification) requires that each safety goal is verified by test, analysis, or a combination. For the IM-e1 BMS:

| Safety Goal | ASIL | Verification Approach | Evidence |
|---|---|---|---|
| SG-01: No cell overcharge under all conditions | ASIL-D | Fault injection test (TC-05) + FMEA analysis | Test report + DFMEA (Chapter 9) |
| SG-02: No cell over-discharge under all conditions | ASIL-D | Fault injection (TC-05 variant) + analysis | Test report |
| SG-03: Prevent thermal runaway propagation | ASIL-D | Rate-of-rise test (TC-04) + calorimetry | Test report + thermal runaway propagation test per UL 9540A |
| SG-04: Safe state on communication loss | ASIL-B | Test (TC-07) | Test report |

### Functional Safety Concept Verification

Per ISO 26262 Part 3 §7.4.10, the functional safety concept (FSC) must be verified before architecture freeze (M3):

1. **FSC Completeness Check:** All safety goals covered by at least one functional safety requirement — verified by traceability matrix (Chapter 3, §3.4 FSR chain)
2. **FSC Consistency Check:** No FSR contradicts another — verified by INCOSE requirements quality assessment (Chapter 3, §3.5)
3. **FSC Independence Check:** ASIL-D functions (thermal runaway detection on Core 0) verified to be independent of ASIL-B functions (SOC estimation on Core 1) — demonstrated by MPU configuration review and inter-core communication analysis

### Safety Analysis Linkage

The HARA (Chapter 3, §3.3) → Safety Goals → FSRs chain must be verified end-to-end. The verification evidence for ASIL-D items:

```
H-01 (Overcharge, ASIL-D)
  └─► SG-01: No cell overcharge
        └─► FSR-01-A: Dual measurement path (HW + SW)
              └─► Architecture: BQ76940 HW comparator + MBMS SW voltage check
                    └─► Test: TC-05 (independent test team)
                          └─► Evidence: TC-05 test report, signed by FUSA engineer
```

---

## 7.7 Validation Plan

Validation confirms that the system serves its actual purpose in the real world — not just that it meets written requirements.

### Validation Objectives

Derived from stakeholder needs (Chapter 2), validation must confirm:

| Validation Objective | Stakeholder Need | Acceptance Criterion |
|---|---|---|
| VOB-01: Driver trusts SOC display | SN-01 (driver range anxiety) | >90% of validation drivers agree SOC matches driving expectation (survey) |
| VOB-02: Fleet operator data quality | SN-07 (fleet telematics) | Telematics API delivers SOH data for 100% of fleet vehicles within 5-minute latency |
| VOB-03: DCFC daily usability | SN-09 (fleet DCFC) | 30→80% SOC in ≤35 minutes at 45°C ambient without thermal shutdown |
| VOB-04: Cold weather start | SN-06 (cold start) | Vehicle driveable within 2 minutes of key-on at -5°C |
| VOB-05: Monsoon survivability | SN-05 (IP67) | Zero BMS faults after 3 months of monsoon operation in 50-vehicle fleet |

### Field Validation Fleet Plan

| Parameter | Value |
|---|---|
| Fleet size | 50 prototype vehicles |
| Validation distance per vehicle | 5,000 km (minimum) |
| Total fleet distance | 250,000 km |
| Duration | 6 months (parallel with vehicle integration, months 13–18) |
| Locations | Mumbai (coastal, humidity), Jaipur (desert, 45°C peak), Manali (altitude 2,050m, cold) |
| Fleet mix | 20 privately operated vehicles (VOB-01, VOB-04, VOB-05), 30 fleet-operated (VOB-02, VOB-03) |

### Validation Data Collection

All 50 validation vehicles transmit telematics data to the IndraMotors data lake:
- 1-Hz: cell voltages (min/max/avg), pack temperature, current, SOC, SOH
- Event-driven: all DTCs with timestamp and GPS location
- Weekly: SOH estimation report per vehicle

Validation engineers review:
- Anomaly rate (unexpected DTCs per 1,000 km) — target: <0.1 per vehicle per 1,000 km
- SOC display accuracy surveys — quarterly driver questionnaire
- Thermal event log — target: zero thermal runaway events in 250,000 km

---

## 7.8 SE Process Reflection

### What Makes IV&V Expensive — and Why It's Worth It

Students are often surprised by the resources allocated to IV&V: the 18-month IM-e1 program allocates months 12–18 — one-third of the entire program — to integration and testing. The infrastructure alone (HIL rig, battery cycler, thermal chamber) costs ₹1.2 Cr. Why?

Because the alternative is discovering faults in the field. A BMS field recall costs 100× more than a test rig. A thermal runaway event costs reputationally far more. The V-Model explicitly front-loads the cost of verification by catching errors at the cheapest possible level (unit test catches algorithm bugs for ₹0; field recall catches them for ₹Cr).

### Verification vs. Validation: The Critical Distinction

Session 8 draws this distinction sharply:

- **Verification** (Chapter 7 test cases) confirms the system meets *SR-F-01, SR-S-01...* — the written requirements
- **Validation** (fleet plan, §7.7) confirms drivers trust the SOC display, fleets can operate daily — the *real purpose*

The Boeing MCAS case is again instructive: MCAS software was verified (it operated as specified). It was not validated — because no simulation or test captured "pilot does not know MCAS exists and cannot counteract it." The IM-e1 BMS validation fleet explicitly captures "does the driver trust what the BMS tells them?" (VOB-01) — a validation question that no specification can fully capture.

### Bridge to Chapter 8

The IV&V plan connects to the Project Execution Plan (Chapter 8) through:
- **Resource dependencies:** Test engineers (2 FTE) and FUSA verification engineer (0.5 FTE) appear in the resource plan
- **Schedule gates:** TC-05 must pass before M6 (System Integration); all TCs must pass before M7 (Validation Complete)
- **Infrastructure requirements:** HIL rig (₹45L), cycler (₹22L), and thermal chamber (₹18L) appear in the infrastructure budget

---

*Next: [Chapter 8 — Project Execution Plan](08-project-execution-plan.md)*
