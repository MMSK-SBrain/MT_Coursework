# Chapter 8: Project Execution Plan

> **SE Processes Applied:** Project Planning (ISO/IEC 15288 §6.3.1), Agreement Management (§6.3.5), Life Cycle Model Management (§6.3.2), Life Cycle Cost Analysis (ISO/IEC 15288 §6.4.13)
> **AEZC517 Sessions Referenced:** Session 9 (Systems Engineering Management), Session 11 (Configuration Management & Lifecycle), Session 13 (Earned Value & Project Metrics)
> **Estimated Reading Time:** 35 minutes

---

## 8.1 Program Overview

The IM-e1 BMS Development Program is a 18-month, ₹6.0 Crore engineering program to design, develop, verify, and validate the Battery Management System for IndraMotors' first mass-market electric sedan. The program runs from program kickoff to ARAI certification submission.

| Program Parameter | Value |
|---|---|
| Program Name | IM-e1 Battery Management System Development |
| Customer | IndraMotors Product Planning Division (internal) |
| Contracting Organization | IndraMotors Systems Engineering, Pune |
| Program Duration | 18 months (Month 1 = contract award) |
| Total Budget | ₹6.0 Crore |
| Program Manager | Chief Systems Engineer (dual hat until M3) |
| Life Cycle Phase | Concept → Development → Integration → Validation |
| Delivery | BMS hardware (MBMS + CMC assemblies) + verified BMS software stack + certification evidence package |

### Life Cycle Model Selection

The IM-e1 BMS program uses a **V-Model (sequential)** with a spiral risk-reduction front-end. This choice was deliberate:

| Life Cycle Option | Suitability for IM-e1 BMS |
|---|---|
| Fully sequential (Waterfall) | Too rigid — does not accommodate HARA findings updating requirements |
| Pure Agile | Inappropriate — ISO 26262 requires formal baselines; agile sprints conflict with functional safety documentation |
| **V-Model (selected)** | **Best fit** — structured decomposition/integration stages; explicit verification pairing; ASIL-D documentation compatible |
| Spiral | Could be used for software only; adds overhead for hardware-dominated program |

The spiral front-end (Concept Phase, months 1-3) allows requirements to be refined before the V-Model's structured phases lock in.

---

## 8.2 Work Breakdown Structure (WBS)

The WBS decomposes the program into manageable, assignable work packages. Three levels are defined: Program → Phase → Work Package.

```
1.0 IM-e1 BMS Development Program
│
├── 1.1 Concept Phase (Months 1–3)
│   ├── 1.1.1 Mission Analysis & CONOPS Development
│   ├── 1.1.2 Stakeholder Identification & Workshops
│   ├── 1.1.3 System Context Definition
│   └── 1.1.4 Initial Requirements Draft
│
├── 1.2 Requirements & Architecture Phase (Months 3–8)
│   ├── 1.2.1 HARA (ISO 26262 Part 3)
│   ├── 1.2.2 System Requirements Specification (SRS Baseline)
│   ├── 1.2.3 Trade Study 1 (Cell Chemistry)
│   ├── 1.2.4 Trade Study 2 (Thermal Architecture)
│   ├── 1.2.5 System Architecture Definition (4 views)
│   ├── 1.2.6 Subsystem Specifications (MBMS, CMC)
│   └── 1.2.7 Architecture Freeze Review (M3)
│
├── 1.3 Design Phase (Months 8–12)
│   ├── 1.3.1 MBMS Hardware Design (Schematic + PCB layout)
│   ├── 1.3.2 CMC Supplier Engagement (TI BQ76940 FAE coordination)
│   ├── 1.3.3 BMS Software Architecture (AUTOSAR layers)
│   ├── 1.3.4 SOC/SOH Algorithm Development (EKF + RLS)
│   ├── 1.3.5 Functional Safety Concept (FSC + FSR documentation)
│   ├── 1.3.6 DFMEA & Fault Tree Analysis
│   ├── 1.3.7 ICD Freeze with VCU Team
│   └── 1.3.8 Critical Design Review (CDR — M4)
│
├── 1.4 Implementation & Integration Phase (Months 12–16)
│   ├── 1.4.1 MBMS PCB Fabrication & Bring-Up
│   ├── 1.4.2 SW Unit Development (all AUTOSAR modules)
│   ├── 1.4.3 SW Unit Tests (TC-01, TC-02, TC-03)
│   ├── 1.4.4 HIL Rig Setup & Commissioning
│   ├── 1.4.5 HIL Integration Tests (TC-04 through TC-07)
│   ├── 1.4.6 ASIL-D Independent Verification (TC-04, TC-05 — independent team)
│   ├── 1.4.7 First Build Complete (M5)
│   └── 1.4.8 Vehicle Integration (M6)
│
└── 1.5 Validation Phase (Months 16–18)
    ├── 1.5.1 Pack-Level Testing (TC-08, TC-09, TC-10)
    ├── 1.5.2 Field Validation Fleet (50 vehicles, 5,000 km)
    ├── 1.5.3 Customer Validation (driver survey, VOB-01 to VOB-05)
    ├── 1.5.4 ARAI Type Approval Submission
    ├── 1.5.5 Certification Documentation Package
    └── 1.5.6 Validation Complete (M7)
```

### WBS Dictionary (Key Work Packages)

| WBS ID | Work Package | Responsible | Duration | Key Output |
|---|---|---|---|---|
| 1.1.2 | Stakeholder Workshops | Chief SE | 3 weeks | SN-01 to SN-26 captured |
| 1.2.1 | HARA | FUSA Engineer | 4 weeks | HARA table, ASIL ratings |
| 1.2.2 | SRS Baseline | Systems Engineering | 6 weeks | Signed-off SRS document |
| 1.3.1 | MBMS Hardware Design | HW Engineer | 10 weeks | Schematic + Gerbers |
| 1.3.4 | EKF Algorithm | SW Engineer | 8 weeks | C code + unit test results |
| 1.4.5 | HIL Integration Tests | Test Engineer | 6 weeks | TC-04 to TC-07 pass reports |
| 1.4.6 | ASIL-D Independent Verification | Independent Verification Team | 3 weeks | TC-05 signed test report |
| 1.5.2 | Field Validation Fleet | V&V Engineer | 6 months | 250,000 km fleet data |

---

## 8.3 Resource Plan

The program requires 12 people across 8 roles. Not all roles are full-time throughout; the plan shows peak FTE per phase.

### Team Structure

| Role | Name (Illustrative) | Headcount | Phase 1 FTE | Phase 2 FTE | Phase 3 FTE | Phase 4 FTE | Phase 5 FTE |
|---|---|---|---|---|---|---|---|
| Chief Systems Engineer | Program lead | 1 | 1.0 | 1.0 | 0.5 | 0.5 | 0.5 |
| Hardware Design Engineer | PCB design | 2 | 0 | 0.5 | 2.0 | 1.0 | 0.5 |
| Embedded SW Engineer | AUTOSAR + algorithm | 3 | 0 | 0.5 | 2.0 | 3.0 | 1.0 |
| Functional Safety Engineer | ISO 26262 | 1 | 0.5 | 1.0 | 1.0 | 0.5 | 0.5 |
| Test & Validation Engineer | IV&V | 2 | 0 | 0.5 | 0.5 | 1.5 | 2.0 |
| Supplier Quality Engineer | CMC + MCU suppliers | 1 | 0 | 0.5 | 1.0 | 0.5 | 0 |
| Configuration Manager | Docs + CM | 1 | 0.5 | 0.5 | 0.5 | 1.0 | 0.5 |
| Project Manager | Program management | 1 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| **Total FTE (peak)** | | **12** | **3.0** | **5.5** | **8.5** | **9.0** | **6.0** |

### Staffing Ramp

The program ramps from 3 FTE in Phase 1 (mission analysis, small core team) to 9 FTE peak in Phase 4 (implementation and integration — highest complexity). Phase 5 (validation) reduces to 6 FTE as hardware is frozen and the team shifts to test execution.

**Critical Dependencies:**
- **FUSA Engineer** must be onboard from Phase 1 (HARA is a Phase 2 deliverable; safety inputs needed from kickoff)
- **Configuration Manager** must be onboard from Phase 1 (baselining CONOPS and SRS from day one)
- **Independent Verification Team** (for ASIL-D TC-04, TC-05) is external to the program — contracted separately, engaged in Phase 4

---

## 8.4 Infrastructure Requirements

Six major infrastructure items are required. All are one-time capital expenditures except software licenses (annual).

| ID | Item | Purpose | Vendor | Qty | Unit Cost (₹L) | Total (₹L) | When Needed |
|---|---|---|---|---|---|---|---|
| INF-01 | HIL Test Rig (dSPACE SCALEXIO) | BMS SW-in-the-loop + HIL testing (TC-04 to TC-07) | dSPACE India | 1 | 45 | 45 | Month 3 (order), Month 6 (delivered) |
| INF-02 | Battery Cycler (Chroma 17020) | Cell/module characterization + HPPC data collection + TC-08, TC-10 | Chroma India | 1 | 22 | 22 | Month 6 |
| INF-03 | Thermal Chamber (-40°C to +80°C) | Environmental test (TC-09) | BINDER / Memmert | 1 | 18 | 18 | Month 10 |
| INF-04 | BMS Function Test Bench | Pack-level functional testing — custom built at IndraMotors lab | Internal build | 1 | 12 | 12 | Month 8 |
| INF-05 | CANalyzer + ETAS INCA licenses | CAN diagnostics and BMS calibration parameter management | Vector/ETAS | 3 seats | 8 | 8 | Month 3 |
| INF-06 | LDRA Tool Suite (ISO 26262 FUSA) | Code coverage analysis, MC/DC coverage, static analysis for ASIL-D | LDRA India | 1 | 15 | 15 | Month 6 |
| | | | | **Total** | | **₹1.20 Cr** | |

**Infrastructure Lead Times:**
- INF-01 (HIL rig): 12–16 week lead time — must be ordered at contract award (Month 1) to arrive by Month 6 for Phase 4 use. Risk R06 in Chapter 9 tracks this.
- INF-02 (cycler): 8–10 weeks; order at Month 4
- INF-03, INF-04: Build or procure by Month 8 (before Phase 3 design completion testing begins)

---

## 8.5 Schedule

### Milestone Schedule

| Milestone | ID | Month | Gate Criteria | Responsible |
|---|---|---|---|---|
| Mission Baseline | M1 | 1 | CONOPS approved by IndraMotors Product Planning; System boundary agreed | Chief SE |
| SRS Baseline | M2 | 6 | All SR-IDs reviewed and signed off by all stakeholders (SH-01 to SH-08 proxies); HARA complete | Chief SE + FUSA Engr |
| Architecture Freeze | M3 | 8 | Both trade studies complete; 4-view architecture documented; ICD v1.0 released to VCU team | Chief SE |
| Critical Design Review (CDR) | M4 | 12 | All hardware schematics complete; all SW module specs complete; DFMEA complete; all risks ≤ score 10 | Program Manager |
| First Build Complete | M5 | 14 | First MBMS PCB assembled; SW loaded; all unit tests (TC-01, TC-02, TC-03) passed | HW + SW Engineers |
| System Integration | M6 | 16 | BMS installed in prototype vehicle; drive-away test passed; VCU CAN integration verified; TC-04 to TC-07 passed | Test Engineer |
| Validation Complete | M7 | 18 | All 10 test cases passed; ARAI submission package delivered; field fleet >5,000 km without critical faults | V&V Engineer |

### Gantt Summary (by Phase)

```
Month:  1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18
        |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

1.1 Concept
        [=======]
        M1^

1.2 Req & Architecture
                    [===================]
                                        ^M2     ^M3

1.3 Design
                                [==========================]
                                                            ^M4

1.4 Implementation & Integration
                                            [====================]
                                                        ^M5         ^M6

1.5 Validation
                                                            [===========]
                                                                        ^M7

Field Fleet (50 vehicles)
                                                        [===============]
```

### Schedule Risk Buffer

Per the program risk register (Chapter 9), the schedule includes a 6-week buffer built into Phase 4-5 boundary. This buffer absorbs:
- HIL rig delivery delay (Risk R06): up to 4 weeks
- ASIL-D independent verification iteration: up to 3 weeks
- ARAI pre-submission comments: up to 2 weeks

Total required buffer: ~9 weeks. The 6-week explicit buffer + 4-week phase overlap design = effective 10-week contingency.

---

## 8.6 Budget Summary

### Budget Breakdown (₹ Crore)

| Category | Sub-Category | Budget (₹ Cr) | Basis |
|---|---|---|---|
| **Personnel** | Chief SE (18 months) | 0.45 | ₹30L/yr × 1.5 yr |
| | HW Engineers × 2 (12 months active) | 0.50 | ₹25L/yr × 2 × 1 yr |
| | SW Engineers × 3 (14 months active) | 0.88 | ₹25L/yr × 3 × 14/12 |
| | FUSA Engineer (18 months) | 0.38 | ₹25L/yr × 1.5 yr |
| | Test Engineers × 2 (12 months active) | 0.42 | ₹21L/yr × 2 × 12/12 |
| | Supplier QA, Config Mgr, PM × 3 (18 months) | 0.37 | ₹25L avg × 3 × 1.5 yr |
| | **Personnel Subtotal** | **3.00** | 12 person-years × ₹25L avg |
| **Infrastructure** | HIL rig, cycler, chamber, test bench, tools | 1.20 | Per INF-01 to INF-06 |
| **Prototypes & Components** | MBMS PCB (×10 proto units), CMC ICs, MCU, connectors | 0.50 | BOM × 10 prototypes |
| **Testing & Certification** | ARAI type approval fee, BIS certification, LDRA audit | 0.30 | ARAI schedule of fees |
| **Travel & Supplier Engagement** | TI FAE visits, ARAI pre-submission, field fleet coordination | 0.20 | 4 trips × 2 engineers |
| **Contingency (15%)** | Program contingency | 0.80 | 15% of ₹5.2 Cr base |
| **Total Program Cost** | | **₹6.00 Cr** | |

### Budget by Phase

| Phase | Duration | Budget (₹ Cr) | % of Total |
|---|---|---|---|
| Phase 1: Concept | Months 1–3 | 0.30 | 5% |
| Phase 2: Requirements & Architecture | Months 3–8 | 1.00 | 17% |
| Phase 3: Design | Months 8–12 | 1.50 | 25% |
| Phase 4: Implementation & Integration | Months 12–16 | 2.20 | 37% |
| Phase 5: Validation | Months 16–18 | 1.00 | 17% |
| **Total** | **18 months** | **6.00** | **100%** |

The heaviest spend is in Phase 4 (37%) — this is where hardware fabrication, SW development, and HIL testing converge. This is typical for embedded system development programs.

---

## 8.7 Earned Value Management (EVM)

EVM is used to track program health objectively. Three metrics are tracked monthly:

| Metric | Formula | Meaning |
|---|---|---|
| **Planned Value (PV)** | Budgeted cost of work scheduled | What we planned to spend by this date |
| **Earned Value (EV)** | Budgeted cost of work performed | What value we actually delivered |
| **Actual Cost (AC)** | Actual cost incurred | What we actually spent |
| **SPI** (Schedule Performance Index) | EV / PV | SPI < 1.0 = behind schedule |
| **CPI** (Cost Performance Index) | EV / AC | CPI < 1.0 = over budget |

### EVM Example: Month 10 Projection

Assume at Month 10 (end of Phase 3 design):

| Metric | Value | Interpretation |
|---|---|---|
| PV | ₹3.30 Cr | Should have delivered ₹3.30 Cr of work by now |
| EV | ₹3.00 Cr | Actually delivered ₹3.00 Cr of work |
| AC | ₹3.20 Cr | Spent ₹3.20 Cr |
| SPI | 3.00 / 3.30 = **0.91** | 9% behind schedule — CDR milestone at risk |
| CPI | 3.00 / 3.20 = **0.94** | 6% over budget — within 15% contingency threshold |
| EAC (Estimate at Completion) | 6.00 / 0.94 = **₹6.38 Cr** | Projected final cost if CPI stays constant |

**Program Response at Month 10 EVM:**
- SPI < 0.90 threshold triggers mandatory recovery plan
- CPI < 0.90 triggers contingency drawdown authorization
- EAC ₹6.38 Cr (6% over) is within contingency allocation (₹0.80 Cr headroom) — no immediate concern
- Recovery action: add 0.5 FTE SW Engineer for 2 months; adjust M4 CDR date by 3 weeks

### EVM Dashboard Tracked Monthly

| Month | PV (₹ Cr) | EV (₹ Cr) | AC (₹ Cr) | SPI | CPI | Status |
|---|---|---|---|---|---|---|
| 3 (M1 gate) | 0.30 | — | — | — | — | Baseline set |
| 6 (M2 gate) | 1.30 | ≥1.30 req. | — | ≥1.00 req. | ≥0.90 req. | Gate review |
| 8 (M3 gate) | 2.30 | ≥2.30 req. | — | ≥1.00 req. | ≥0.90 req. | Gate review |
| 12 (M4/CDR) | 3.80 | ≥3.80 req. | — | ≥1.00 req. | ≥0.90 req. | Gate review |
| 14 (M5) | 4.80 | ≥4.80 req. | — | ≥1.00 req. | ≥0.90 req. | Gate review |
| 18 (M7) | 6.00 | 6.00 req. | — | 1.00 target | ≥0.90 req. | Final |

---

## 8.8 Make vs. Buy Analysis

A formal make-vs-buy decision was made at M2 (SRS Baseline) to determine which components are sourced vs. developed in-house.

| Item | Decision | Rationale |
|---|---|---|
| **CMC IC (TI BQ76940)** | **Buy** | High-volume automotive-grade IC; ASIL-B certified by TI; no cost advantage in developing custom ASIC at 10k units/yr |
| **MCU (STM32H755)** | **Buy** | Lockstep CPU available in silicon (ASIL-D ready); significant time-to-market risk in custom MCU |
| **CAN Transceiver (TI TCAN1462)** | **Buy** | Commodity; >100 equivalent devices available; no differentiation value |
| **Hall-effect current sensor (LEM HAS-300S)** | **Buy** | Automotive-qualified, AIS-038 compliant; secondary shunt also sourced |
| **BMS Master Software (AUTOSAR stack + algorithms)** | **Make** | Core IP — EKF SOC algorithm, balancing strategy, fault logic. Differentiates IndraMotors BMS performance. Cannot outsource without IP loss |
| **SOC/SOH Estimation Library** | **Make** | Key competitive differentiator; deep EV chemistry knowledge required |
| **Calibration Tooling (offline MATLAB scripts)** | **Make** | In-house tool, no market value; custom to BQ76940 + STM32H755 combination |
| **HIL Test Models (dSPACE TargetLink)** | **Make (in-house) + Buy (tools)** | Test models are program-specific; dSPACE SCALEXIO hardware bought, model developed in-house |
| **ARAI Certification Testing** | **Buy (outsource to ARAI)** | Regulatory requirement — must be performed by accredited body |

**Core Principle:** Buy commodity components where >3 equivalent suppliers exist. Make software and algorithms that represent BMS intelligence — this is IndraMotors' competitive moat.

---

## 8.9 Configuration Management Plan

Configuration Management (CM) ensures all artifacts are controlled, baselined, and traceable throughout the program lifecycle.

### CM Items and Baselines

| Baseline | Content | When Set | Owner |
|---|---|---|---|
| **Functional Baseline (FB)** | CONOPS, System Context, Mission Statement | M1 (Month 1) | Chief SE |
| **Allocated Baseline (AB)** | SRS (all SR-IDs), HARA, Safety Goals | M2 (Month 6) | Chief SE + FUSA Engr |
| **Design Baseline (DB)** | Architecture docs, ICD, MBMS schematics, SW architecture | M3-M4 (Month 8-12) | HW + SW Engineers |
| **Product Baseline (PB)** | Final hardware Gerbers, BMS SW binary, calibration data | M7 (Month 18) | Configuration Manager |

### Version Control

| Artifact Type | Tool | Branching Strategy |
|---|---|---|
| Software source code | Git (IndraMotors internal GitLab) | Trunk-based; feature branches; release tags at each milestone |
| Hardware schematics | Altium Designer + vault | Change-controlled; ECO (Engineering Change Order) process for post-CDR changes |
| Documents (SRS, ICD, HARA) | Confluence + SharePoint | Version numbers; review workflow with mandatory approval before baseline |
| Test results | JIRA + dSPACE TestManager | Each test run linked to SW version; automated traceability |

### Change Control Process

After each baseline is established, changes require formal Engineering Change Orders (ECOs):

1. **Identify:** Engineer identifies need for change; opens ECO in JIRA
2. **Assess:** Impact analysis — which requirements, designs, tests are affected?
3. **Approve:** For ASIL-D items: three approvers (Chief SE + FUSA Engineer + Program Manager). For ASIL-B: two approvers (Chief SE + engineer lead)
4. **Implement:** Change made, document updated, regression test executed
5. **Close:** ECO closed; CM record updated; traceability database updated

**ECO Response Times:**
- Critical (safety impact): 48-hour approval cycle
- Major (schedule impact): 5-day approval cycle
- Minor (no functional impact): 10-day approval cycle

---

## 8.10 Life Cycle Cost Analysis (LCCA)

LCC extends beyond the 18-month development program to include the full 12-year vehicle life cycle.

### LCC Model

| Cost Category | Period | Basis | Amount (₹ Cr, 10,000 units) |
|---|---|---|---|
| **Development Cost** | Program (18 months) | §8.6 budget | 6.0 |
| **Tooling & NRE** | Pre-production | PCB tooling, test fixture NRE | 1.5 |
| **Unit Manufacturing Cost** | Per vehicle, 10k units | BoM ₹18,000 × 10,000 units | 18.0 |
| **Warranty Cost** | Years 1–8 | 2% warranty rate × ₹25,000 avg claim × 10,000 units | 5.0 |
| **Field Support (OTA updates)** | Years 1–8 | Software update infrastructure + 1 FTE support engineer × 8 yr | 2.0 |
| **End-of-Life** | Year 10–12 | Battery recycling compliance (Extended Producer Responsibility) | 1.0 |
| **Total LCC (10,000 units)** | | | **₹33.5 Cr** |
| **LCC per unit** | | | **₹33,500** |

### LCC Sensitivity

The development cost (₹6.0 Cr) is 18% of total LCC — significant but not dominant. Manufacturing cost (₹18.0 Cr) dominates. This reinforces the make-vs-buy decision: optimizing BMS unit cost by ₹1,000 per unit saves ₹1.0 Cr LCC — equivalent to 17% of the entire development budget. Every rupee saved in BoM at volume scales dramatically.

### LCC Reduction Opportunities

| Opportunity | LCC Impact | Trade-Off |
|---|---|---|
| Reduce BMS BoM from ₹18,000 to ₹16,000 | -₹2.0 Cr at 10k units | Requires single-supplier MCU risk; safety risk of reduced redundancy |
| Improve SOH estimation accuracy → reduce warranty rate from 2% to 1.5% | -₹1.25 Cr | Requires better EKF model; +₹0.3 Cr development cost (net: -₹0.95 Cr) |
| Extend OTA update capability → reduce field recall cost | -₹0.5 Cr | OTA server infrastructure +₹0.2 Cr |

The best LCC opportunity: **improve SOH estimation** — reduces warranty claims without safety trade-offs, net positive even accounting for additional development investment.

---

## 8.11 Agreement Management

The program involves three key external agreements:

### Agreement 1: TI BQ76940 Long-Term Agreement (LTA)

- **Supplier:** Texas Instruments India
- **Item:** BQ76940 CMC IC + BQ7694003 (second source)
- **Volume:** 10,000 units per year (40,000 ICs/year, 4 per pack)
- **LTA Duration:** 3 years (covers production ramp beyond program end)
- **Key Terms:** 18-month buffer stock at TI; IndraMotors qualified on both BQ76940 and BQ7694003 (dual-source — addresses Risk R04)
- **Quality Requirements:** PPAP Level 3 required before production release; incoming inspection waived with TI AEC-Q100 certificate

### Agreement 2: ARAI Certification Agreement

- **Body:** Automotive Research Association of India, Pune
- **Scope:** AIS-048 (EV safety), AIS-038 (Battery pack) type approval
- **Key Milestone:** Pre-submission review at Month 16 (2 months before M7) — ARAI provides preliminary feedback, reducing risk of surprise at formal submission
- **Fee:** ₹22L (within INF/certification budget)
- **IndraMotors Obligation:** Provide complete technical file 4 weeks before each test

### Agreement 3: dSPACE HIL Rig Supply Agreement

- **Supplier:** dSPACE India Pvt. Ltd., Pune
- **Item:** SCALEXIO LabBox + DS5203 FPGA board + 2-year maintenance
- **Key Risk Clause:** Delivery guarantee by Month 6 — penalty clause of ₹2L/week delay (addresses Risk R06 mitigation)
- **Training:** 3-day operator training for IndraMotors test engineers included

---

## 8.12 SE Process Reflection

### Why Project Planning is an SE Process — Not Just a Management Process

ISO/IEC 15288 places Project Planning (§6.3.1) within the *Project Processes* group — distinct from the Technical Processes we have been applying in Chapters 1-7. This reflects INCOSE's view: a systems engineer must also be a planner. The SE team owns the WBS because they understand technical dependencies; the PM manages cost and schedule against the WBS the SE team created.

The IM-e1 BMS WBS was not written by the Project Manager — it was written by the Chief Systems Engineer, because only the SE team understands:
- That the HARA (WBS 1.2.1) must precede the SRS Baseline (1.2.2) — not the other way around
- That ASIL-D independent verification (1.4.6) requires a separate team that needs to be contracted months in advance
- That CMC supplier engagement (1.3.2) must happen in Phase 3, not Phase 4 — because BQ76940 PPAP takes 12 weeks

A PM who "manages the schedule" without understanding these technical dependencies will create a schedule that looks valid but is actually impossible.

### EVM as an Early Warning System (Session 13 Connection)

Session 13 introduced EVM as the SE program's vital signs monitor. The Month 10 example in §8.7 (SPI = 0.91, CPI = 0.94) is not a crisis — it is an early warning that allows the team to respond before the situation becomes unrecoverable. Without EVM, the same situation might only become visible at Month 16 when the schedule overrun is too large to absorb.

**The MCAS Parallel:** Investigations into the Boeing 737 MAX program found that EVM was being tracked but warning signals (schedule pressure exceeding 20%) were not being escalated. The KPI existed; the response process did not. The IM-e1 BMS program specifies both: metrics (EVM table) AND response thresholds (SPI < 0.90 triggers recovery plan). Metrics without response criteria are theater.

### Configuration Management as Institutional Memory

The CM plan (§8.9) is not bureaucracy — it is the program's institutional memory. Without baselines:
- A late requirements change gets implemented in hardware but not updated in the test plan
- The HARA from Month 3 is superseded by a revised HARA from Month 7, but the SRS still references the old safety goals
- A software bug fix in Month 15 is not linked to the test case that found it — the next program cannot learn from it

The Product Baseline (set at M7) becomes the starting point for IM-e1 BMS Version 2.0. Its completeness determines how quickly IndraMotors can develop the next vehicle's BMS.

### Bridge to Chapter 9

The project execution plan and risk management plan (Chapter 9) are co-developed, not sequential. Risks R01, R04, and R06 in Chapter 9 directly drove design decisions in this chapter:
- R01 (LFP supply) → dual-source agreement in §8.11
- R04 (CMC IC shortage) → 18-month LTA with TI, buffer stock clause
- R06 (HIL rig delay) → Month 1 order placement, delivery penalty clause in §8.11
- R07 (ASIL-D capability risk) → LDRA tool in infrastructure (INF-06), FUSA engineer from Phase 1

The project plan is the risk response plan made concrete.

---

*Next: [Chapter 9 — Risk Management](09-risk-management.md)*
