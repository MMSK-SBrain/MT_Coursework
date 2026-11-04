# Chapter 9: Risk Management

> **SE Processes Applied:** Risk Management (ISO/IEC 15288 §6.3.4), Specialty Engineering — Functional Safety (ISO 26262), Quality Management
> **AEZC517 Sessions Referenced:** Session 9 (Risk & Opportunity Management), Session 12 (Functional Safety — FMEA & FTA)
> **Estimated Reading Time:** 30 minutes

---

## 9.1 Risk Management Process

The IM-e1 BMS program applies the ISO/IEC 15288 Risk Management process, structured as a continuous cycle:

```
IDENTIFY → ANALYZE → PLAN TREATMENT → IMPLEMENT → MONITOR
    ↑                                                   |
    └───────────────── Residual Risks ─────────────────┘
```

### Risk Scoring Framework

Risks are scored using a **Probability × Impact (P×I)** matrix. Both dimensions are rated 1–5.

**Probability Scale:**

| Score | Probability | Likelihood |
|---|---|---|
| 1 | Very Low | <5% — would be surprised if this occurred |
| 2 | Low | 5–25% — unlikely but plausible |
| 3 | Medium | 25–50% — roughly even odds |
| 4 | High | 50–75% — more likely than not |
| 5 | Very High | >75% — expected to occur |

**Impact Scale:**

| Score | Impact | Description |
|---|---|---|
| 1 | Negligible | No material effect on schedule, cost, or safety |
| 2 | Minor | <2-week schedule impact OR <5% cost increase |
| 3 | Moderate | 2–6 week schedule impact OR 5–15% cost increase |
| 4 | Major | 6–12 week schedule impact OR 15–25% cost increase, or safety concern requiring rework |
| 5 | Critical | >12 weeks OR >25% cost, OR functional safety compromise requiring redesign |

**Risk Thresholds:**

| Score Range | Classification | Management Response |
|---|---|---|
| ≥ 12 | **HIGH** | Active mitigation plan required; tracked at program director level |
| 6–11 | **MEDIUM** | Mitigation plan required; tracked by Chief SE monthly |
| ≤ 5 | **LOW** | Monitor only; reviewed quarterly |

---

## 9.2 Risk Register

All 12 program risks are documented with probability, impact, raw score, mitigation strategy, and residual score post-mitigation.

| Risk ID | Risk Title | Category | P | I | Score | Mitigation Owner | Residual Score |
|---|---|---|---|---|---|---|---|
| **R01** | LFP cell supply disruption | Supply Chain | 3 | 5 | **15** | Procurement Lead | 6 |
| **R02** | SOC algorithm underperforms at cold soak | Technical | 3 | 4 | **12** | SW Lead | 6 |
| **R03** | Thermal runaway event during validation testing | Safety | 2 | 5 | **10** | FUSA Engineer | 4 |
| **R04** | CMC IC supply shortage (semiconductor market) | Supply Chain | 3 | 4 | **12** | Procurement Lead | 6 |
| **R05** | ARAI certification delayed due to IS standard gap | Regulatory | 2 | 4 | **8** | Chief SE | 4 |
| **R06** | HIL test rig delivery delayed | Schedule | 2 | 3 | **6** | Program Manager | 3 |
| **R07** | ISO 26262 ASIL-D SW not achievable with current team capability | Technical | 2 | 5 | **10** | Chief SE + FUSA Engr | 5 |
| **R08** | Vehicle CAN conflicts with BMS message IDs | Integration | 3 | 3 | **9** | SW Lead | 3 |
| **R09** | Battery warranty claims exceed SOH prediction model | Commercial | 2 | 4 | **8** | Chief SE | 4 |
| **R10** | Key person departure (Chief SE or FUSA engineer) | Organizational | 2 | 4 | **8** | Program Manager | 4 |
| **R11** | Monsoon-related corrosion failures in field | Environmental | 2 | 3 | **6** | HW Engineer | 3 |
| **R12** | Cost overrun >20% due to scope creep | Cost | 2 | 3 | **6** | Program Manager | 3 |

---

## 9.3 Risk Heat Map

The heat map plots all 12 risks before mitigation (◆) and after mitigation (○) on the P×I grid.

```
          IMPACT →
          1           2           3           4           5
P    ┌───────────┬───────────┬───────────┬───────────┬───────────┐
R  5 │           │           │           │           │           │
O    ├───────────┼───────────┼───────────┼───────────┼───────────┤
B  4 │           │           │           │           │           │
A    ├───────────┼───────────┼───────────┼───────────┼───────────┤
B  3 │           │           │  R08◆     │  R02◆,R04◆│  R01◆     │
I    ├───────────┼───────────┼───────────┼───────────┼───────────┤
L  2 │           │           │  R06◆,R11◆│  R05◆,R09◆│  R03◆,R07◆│
I    │           │           │  R12◆     │  R10◆     │           │
T    ├───────────┼───────────┼───────────┼───────────┼───────────┤
Y  1 │           │           │           │           │           │
     └───────────┴───────────┴───────────┴───────────┴───────────┘

After mitigation (residual positions):
─────────────────────────────────────────────────────────────────
          1           2           3           4           5
     3 │           │           │  R01○,R02○│           │           │
       │           │           │  R04○     │           │           │
     2 │           │           │           │  R07○     │           │
     1 │           │           │  R03○,R05○│           │           │
       │           │           │  R06○,R08○│           │           │
       │           │           │  R09○,R10○│           │           │
       │           │           │  R11○,R12○│           │           │

◆ = Pre-mitigation   ○ = Post-mitigation (residual)
```

**Heat Map Analysis:**
- Pre-mitigation: 4 HIGH risks (R01, R02, R04, R07: scores ≥ 12); 4 MEDIUM risks; 4 LOW risks
- Post-mitigation: 0 HIGH risks; 1 MEDIUM risk (R07, score 5, borderline); 11 LOW risks
- Most impactful mitigation: R01 (15 → 6) via dual-source supply agreement

---

## 9.4 High-Risk Treatment Plans

Full mitigation plans for the four HIGH-scoring risks (R01, R02, R04, R07):

---

### R01: LFP Cell Supply Disruption

**Risk Statement:** IndraMotors is a new EV OEM without established battery cell contracts. A single-supplier LFP cell dependency leaves the program vulnerable to geopolitical supply disruption (e.g., China export controls on lithium), manufacturing defects, or allocation shortfalls during semiconductor-style supply crunches.

**Root Causes:**
- LFP cell market is dominated by Chinese manufacturers (CATL, BYD, SVOLT — collectively >65% of global LFP supply)
- IndraMotors has no existing battery supply relationships (first EV program)
- 10,000 units/year demand is below the MOQ threshold for priority allocation from Tier-1 suppliers

**Impact if Realized:**
- Program halt: no cells → no prototypes → validation schedule impossible
- Production delay: 6–12 months to qualify alternate supplier (PPAP + validation drive cycle)
- Commercial: IndraMotors misses market window; SOP delayed; competitor advantage

**Mitigation Strategy:**

| Action | Owner | Timeline | Success Criterion |
|---|---|---|---|
| Qualify CATL LFP as primary supplier | Procurement Lead | Month 3 | LOI signed; NDA executed |
| Qualify BYD LFP as secondary supplier (same cell chemistry, compatible dimensions) | Procurement Lead | Month 6 | Technical equivalence validated against BMS parameters |
| Sign 3-year supply agreement with 6-month buffer stock clause | Procurement Lead | Month 6 | Contract executed; 6-month buffer stock obligation written in |
| Validate BMS performance with both CATL and BYD cells | SW Lead | Month 10 | SOC estimation error ≤2% with both cell types confirmed |
| Monitor cell market monthly (price index, geopolitical news) | Procurement Lead | Ongoing | Escalation triggered if >20% price increase or allocation warning |

**Residual Risk:** Score 6 (P=3, I=2) — dual-sourced but geopolitical risk cannot be fully eliminated. Buffer stock reduces production halt from months to weeks.

---

### R02: SOC Algorithm Underperforms at Cold Soak (-5°C)

**Risk Statement:** The EKF SOC estimation algorithm (Chapter 6, §6.1) relies on a 2RC Thevenin model parameterized at five temperatures. LFP cells exhibit significantly different internal resistance and OCV behavior at temperatures below 0°C. If the cold-temperature model parameters are inaccurate, SOC error may exceed 2% at -5°C, violating SR-F-01 and causing driver range misjudgment.

**Technical Background:**
- LFP OCV-SOC curve is flat between 20%–80% SOC at all temperatures, making SOC estimation dependent on current integration and model accuracy
- At -5°C, LFP internal resistance increases 3–5× compared to 25°C (lithium-ion diffusion rate drops sharply with temperature)
- The EKF process noise covariance (Q matrix) must be tuned differently at low temperatures; a single Q matrix tuned for 25°C will over-smooth at -5°C, causing slow convergence

**Impact if Realized:**
- SR-F-01 violation (SOC ≤2% error): requires algorithm rework in Phase 4
- Driver impact: range estimate at cold start unreliable — customer complaint driver
- Commercial: warranty claims if driver runs out of charge due to inaccurate SOC

**Mitigation Strategy:**

| Action | Owner | Timeline | Success Criterion |
|---|---|---|---|
| Collect HPPC data at -10°C, -5°C, 0°C, 10°C, 25°C, 40°C (6 temperature points, not 5) | SW Lead + Test Engr | Month 8 | Parameter tables populated at all 6 temperatures |
| Implement temperature-adaptive Q matrix in EKF (Q = f(temperature)) | SW Lead | Month 10 | EKF convergence time ≤10 min at -10°C in simulation |
| Validate at -10°C on battery cycler with real CATL LFP cells in thermal chamber | Test Engineer | Month 12 | SOC error ≤3% at -10°C; ≤2% at -5°C and above |
| Add SOC confidence flag in BMS CAN message: flag = 0 when temperature < 0°C and time since last charge < 15 min | SW Lead | Month 11 | Flag implemented; VCU displays "initializing" to driver |

**Residual Risk:** Score 6 (P=3, I=2) — algorithm rework is high effort but low probability of impasse given mitigation. Additional temperature points and adaptive Q matrix reduce technical risk substantially.

---

### R04: CMC IC Supply Shortage

**Risk Statement:** The BQ76940 CMC IC is sourced from Texas Instruments. The 2020-2022 semiconductor shortage demonstrated that automotive-grade ICs can face 52+ week lead times, with allocation prioritized to larger OEM customers. IndraMotors, as a new OEM, has no allocation history with TI.

**Impact if Realized:**
- Prototype shortage: Phase 4 cannot begin without CMC ICs (no BMS hardware)
- Production delay: equivalent to R01 — 6–12 months to qualify alternate device
- Additional risk: BQ76940 alternate sources (Analog Devices ADBMS6815, Renesas ISL94212) require BMS hardware redesign (different pinout, communication protocol)

**Mitigation Strategy:**

| Action | Owner | Timeline | Success Criterion |
|---|---|---|---|
| Sign 18-month LTA (Long-Term Agreement) with TI India for BQ76940 | Procurement Lead | Month 2 | LTA executed; annual volume committed |
| Qualify TI BQ7694003 as second-source (pin-compatible with BQ76940; same TI family) | HW Engineer | Month 9 | BQ7694003 characterization complete; schematic updated for compatibility |
| Order 6-month prototype buffer (250 ICs) at LTA signing | Procurement Lead | Month 2 | ICs on hand before Month 8 |
| Monitor TI allocation health monthly; escalate if lead time >16 weeks | Procurement Lead | Ongoing | Trigger alternate source qualification if lead time exceeds threshold |

**Residual Risk:** Score 6 (P=3, I=2) — LTA plus same-family second source dramatically reduces supply risk. Pin-compatible second source avoids hardware redesign (the critical cost of R04 impact).

---

### R07: ISO 26262 ASIL-D Software Development Capability Gap

**Risk Statement:** ASIL-D software development imposes stringent process requirements: MISRA-C compliance, MC/DC code coverage (Modified Condition/Decision Coverage, the most stringent coverage criterion), formal review checklists, and independence requirements. The IM-e1 BMS embedded software team (3 engineers) may not have prior ASIL-D experience. If the team cannot achieve ASIL-D compliance, the overcharge protection software cannot be certified, blocking ARAI approval.

**What ASIL-D Software Demands (That Standard SW Does Not):**
- 100% statement coverage + MC/DC coverage (not just branch coverage)
- Formal SW unit test plan reviewed and approved before implementation
- Independence: test engineer must not be the implementer
- Tool qualification: all software tools (compiler, IDE) must be qualified per ISO 26262-8
- Documented traceability from every line of safety code to the FSR that requires it

**Impact if Realized:**
- Overcharge protection (TC-05) cannot be independently verified → ARAI will not certify
- Requires complete safety SW redesign + re-verification: estimated 4–6 month program delay
- Cost: ₹0.8–1.2 Cr additional (contingency consumption + additional engineers)

**Mitigation Strategy:**

| Action | Owner | Timeline | Success Criterion |
|---|---|---|---|
| Engage external FUSA consulting firm for ASIL-D SW process setup | Chief SE | Month 2 | Contract signed; process workshop completed by Month 3 |
| Deploy LDRA Tool Suite (INF-06) from Month 3 — enforce from first safety-critical module | FUSA Engineer | Month 3 | LDRA integrated into CI pipeline; MC/DC reports generated per build |
| Assign dedicated FUSA Engineer 100% to safety SW review from Phase 3 | Program Manager | Month 6 | FUSA Engineer formally assigned as Safety SW Assessor in project plan |
| Conduct ASIL-D SW process audit at Month 9 (mid-design) | External auditor | Month 9 | No critical findings; all open findings with closure plans |
| Train all 3 SW engineers on MISRA-C and MC/DC testing principles | Chief SE | Month 3 | Training complete; engineers pass MISRA-C certification exam |

**Residual Risk:** Score 5 (P=1, I=5) — probability reduced significantly (experienced FUSA consultant + early tooling). Impact unchanged (ASIL-D failure remains critical if it occurs). This is the only residual risk above 4 — it is tracked at program director level throughout.

---

## 9.5 Medium-Risk Summaries

Risks R03, R05, R08, R09, R10, R11, R12 scored 6–10 before mitigation. Key mitigations:

| Risk ID | Risk Title | Pre Score | Key Mitigation | Post Score |
|---|---|---|---|---|
| R03 | Thermal runaway in validation testing | 10 | Fire suppression in test lab; CO₂ inert atmosphere during nail penetration tests; liability insurance; all cell-level thermal tests performed behind blast shield per UN 38.3 protocol | 4 |
| R05 | ARAI certification delayed | 8 | Pre-submission review at Month 16 (2 months before formal submission); IndraMotors liaison officer assigned to ARAI Pune; test plan shared with ARAI at M3 for early feedback | 4 |
| R08 | VCU CAN message ID conflicts | 9 | ICD freeze with VCU team at Month 6 (M3 output); CAN matrix review checklist at CDR; automated CAN ID conflict detection in CANalyzer test suite | 3 |
| R09 | Warranty claims exceed prediction | 8 | Conservative SOC window (15%–95%); temperature-derated DCFC; OTA SOH model updates; warranty analysis reviewed at 6-month intervals against field data | 4 |
| R10 | Key person departure | 8 | Knowledge management plan: pair-engineering on all ASIL-D modules; design documentation as deliverable (not optional); succession plan written and reviewed at M2 | 4 |
| R11 | Monsoon corrosion failures | 6 | IP67 testing at ARAI test facility; conformal coating (Electrolube HPA) on all PCBs; validation fleet includes 20 vehicles in Mumbai monsoon zone | 3 |
| R12 | Cost overrun from scope creep | 6 | Formal ECO change control (§8.9); scope baseline locked at M2; monthly EVM; contingency drawdown requires PM + Director approval | 3 |

---

## 9.6 Risk Review Cadence

Risk management is not a one-time activity — risks are living items that change as the program matures.

| Review Type | Frequency | Attendees | Triggers |
|---|---|---|---|
| Risk Register Review | Monthly | Chief SE, PM, FUSA Engineer | Standard cadence; review all open risks |
| Emergency Risk Review | Ad hoc | Program Director + Risk Owner | New risk score ≥ 12 OR realized risk event |
| Phase Gate Risk Review | At each milestone (M1–M7) | Full program team + IndraMotors Product Planning | Gate criterion: no unmitigated HIGH risks before phase entry |
| Independent Safety Assessment | At M4 (CDR) and M7 | External FUSA assessor | ISO 26262 Part 2 §6.4.8 independence requirement |

### Risk Closure Criteria

A risk is closed (removed from active register) when:
1. The risk event can no longer occur (e.g., supplier contract signed → R01 probability reduced; risk not closed but reclassified to LOW)
2. The program phase that created the risk has passed (e.g., after ARAI submission, R05 closes)
3. The mitigation has been fully implemented and verified effective

Closed risks are archived in the CM system (not deleted) — they serve as lessons learned for future programs.

---

## 9.7 Design Failure Mode and Effects Analysis (DFMEA)

DFMEA complements the HARA (Chapter 3) by analyzing failure modes at the hardware/software design level — not the hazard level. Where HARA asks "what hazardous events can occur in operation?", DFMEA asks "how can each design element fail, and what is the effect?"

**Severity / Occurrence / Detection Scale (1–10):**
- **Severity (S):** Effect of failure on end user: 1 = negligible, 10 = catastrophic injury/fire
- **Occurrence (O):** Likelihood failure mode occurs over design life: 1 = extremely unlikely, 10 = almost certain
- **Detection (D):** Ability to detect failure before it reaches the end user: 1 = always detected, 10 = undetectable

**Risk Priority Number (RPN) = S × O × D** — higher = more critical

### DFMEA Table

| ID | Function | Failure Mode | Failure Effect | S | Cause | O | Current Detection Control | D | RPN | Recommended Action |
|---|---|---|---|---|---|---|---|---|---|---|
| FM-01 | Measure cell voltage (CMC) | CMC IC reports incorrect voltage (latch-up) | Incorrect SOC calculated → undetected overcharge | 9 | CMC IC latch-up from transient ESD event | 3 | SW plausibility check: CMC reading vs. string voltage sum | 5 | **135** | Dual measurement path (BQ76940 HW comparator + MBMS SW); CMC latch-up detection via communication timeout → DTC P1B03 |
| FM-02 | Control contactor (MBMS) | Contactor fails to open on command (welded) | Overcharge or overdischarge continues uncontrolled | 10 | Main contactor contact welding due to high-current interrupt | 2 | Contactor state feedback (auxiliary contact) read by MBMS | 4 | **80** | Hardware watchdog: if contactor open commanded AND feedback shows closed for >100ms → escalate to Tier 3 (VCU). DTC P1B01. Add pre-charge contactor as independent current-limit path. |
| FM-03 | Estimate SOC (EKF algorithm) | SOC drift accumulates over lifetime | Customer range anxiety; underreported SOC → potential overdischarge | 7 | EKF model parameter drift as cells age (capacity fade not tracked) | 4 | SOH estimation divergence check (EKF vs. Coulomb count integral) | 6 | **168** | Periodic OTA model update (SN-14 requirement). Add RLS SOH adaptation: Qmax updated online as cell ages. Drift check: if EKF and CC disagree by >5% over 3 cycles → DTC P1B04 (model drift warning). |
| FM-04 | Cool battery pack (thermal system) | Coolant pump failure (no flow) | Cell temperature rises unchecked → thermal runaway risk | 10 | Coolant pump bearing failure (MTTF ~60,000 hrs) | 2 | Coolant flow sensor (turbine type) + cell temperature rate-of-rise | 3 | **60** | Rate-of-rise detection (>2°C/s) triggers emergency contactor open (independent of pump fault detection — defense in depth). DTC P1B05. Coolant flow sensor cross-checked against temperature rise model. |
| FM-05 | Communicate BMS faults to VCU (CAN) | BMS CAN bus silent (bus-off state) | VCU cannot manage power; vehicle enters uncontrolled state | 8 | MBMS MCU bus-off error counter exceeds limit due to CAN transceiver fault or line short | 3 | VCU heartbeat timeout (200ms): VCU detects BMS CAN silence within 200ms | 4 | **96** | Dual CAN bus architecture (CAN-A primary + CAN-B secondary). If CAN-A fails, BMS switches to CAN-B within 100ms. Limp-home mode maintained on CAN-B. DTC P1B06 on secondary bus. |

### DFMEA Action Summary

| FM ID | Current RPN | Target RPN (After Action) | Action Status |
|---|---|---|---|
| FM-03 | 168 | ≤60 | Action: RLS SOH + OTA updates (planned in Ch6 §6.1) |
| FM-01 | 135 | ≤45 | Action: Dual path (implemented in architecture Ch4 + design Ch6) |
| FM-05 | 96 | ≤32 | Action: Dual CAN bus (implemented in architecture Ch4) |
| FM-02 | 80 | ≤30 | Action: Contactor feedback + HW watchdog (implemented in Ch6 §6.4) |
| FM-04 | 60 | ≤24 | Action: Rate-of-rise detection (implemented in Ch6 §6.3) |

**DFMEA Closure Criterion:** All FM actions implemented and verified before CDR (M4). Target RPN must be achieved before pack-level testing begins.

---

## 9.8 Fault Tree Analysis (FTA) — Overcharge Event

DFMEA analyzes individual failure modes (bottom-up). FTA analyzes catastrophic top-level events (top-down): "What combination of failures leads to a battery fire?"

The top-level undesired event for the IM-e1 BMS:

**TOP: Cell voltage exceeds 3.80V (thermal runaway onset)**

```
TOP: Cell voltage > 3.80V
│
└─── AND Gate: All three protection tiers fail simultaneously
      │
      ├─── Tier 1 FAILS: BQ76940 HW comparator does not assert OV pin
      │     └── Cause: CMC IC latch-up (FM-01) AND CMC redundancy path also failed
      │
      ├─── Tier 2 FAILS: MBMS SW does not open contactor within 10ms
      │     ├── Cause A: MBMS MCU hung (stuck in interrupt loop)
      │     └── Cause B: SW plausibility check passes despite fault (FM-01 — undetected)
      │
      └─── Tier 3 FAILS: VCU does not enter safe state
            ├── Cause A: BMS CAN silent (FM-05) — VCU loses BMS data
            └── Cause B: VCU itself has a fault (out of BMS scope)
```

**FTA Conclusion:** Thermal runaway from overcharge requires ALL THREE protection tiers to fail simultaneously. The three tiers are designed to be independent (hardware, software, vehicle) — simultaneous failure requires independent rare events to co-occur. This architecture provides defense-in-depth per ISO 26262 Part 5 §7.4.4 (multiple independent protection layers).

**Probability Estimate:**
- P(Tier 1 fail) = 10⁻⁴ per operating hour (CMC latch-up rate, AEC-Q100 data)
- P(Tier 2 fail | Tier 1 fail) = 10⁻³ per operating hour (SW fault, independent of CMC)
- P(Tier 3 fail | Tier 1+2 fail) = 10⁻² per operating hour (VCU independent failure)
- P(TOP event) = 10⁻⁴ × 10⁻³ × 10⁻² = **10⁻⁹ per operating hour**

This meets the ISO 26262 ASIL-D requirement: random hardware failure rate < 10⁻⁸/hour for safety goal violations.

---

## 9.9 Opportunity Register

Risk management also includes **opportunities** — positive uncertainties that, if realized, benefit the program. ISO/IEC 15288 §6.3.4 explicitly includes opportunity management.

| Opp ID | Opportunity | Probability | Benefit | Action to Exploit |
|---|---|---|---|---|
| O01 | LFP cell prices continue to fall (trend: -8%/yr) | High | ₹2–4L reduction per 1,000 units if cells are priced at contract renewal (Month 18) | Include price adjustment clause in supply agreement; renegotiate at 12-month mark |
| O02 | STM32H755 successor (STM32H7R) offers 50% more flash — enables OTA model complexity | Medium | Can deploy more complex SOC algorithm post-launch without hardware change | Maintain software architecture compatibility with next-gen MCU from design start |
| O03 | Early ARAI engagement accelerates certification timeline | Medium | 4–6 week schedule reduction at M7 | Pre-submission review at Month 16 (already in plan, §8.11) |
| O04 | Fleet operator (Ola/Uber) interested in bulk IM-e1 purchase | Low | 10,000 unit order in Year 2 would fund program extension for IM-e2 BMS | Provide fleet telematics demo at Month 17 using validation fleet data |

---

## 9.10 SE Process Reflection

### Risk Management as a Technical Process — Not Just Administrative Overhead

Students sometimes view risk registers as paperwork — something to satisfy an auditor, not something that changes engineering decisions. The IM-e1 BMS program illustrates how risk management directly shaped technical design choices:

- **R01 (cell supply) → dual-source supply agreement** — a procurement decision driven by a risk score
- **R02 (cold SOC) → six temperature HPPC points instead of five** — a test plan decision driven by technical risk analysis
- **R04 (CMC supply) → pin-compatible second source qualification** — a hardware architecture decision to ensure BQ7694003 compatibility from the start
- **R07 (ASIL-D capability) → LDRA tool and FUSA consultant from Month 2** — a staffing and tooling decision driven by capability risk

None of these decisions appear "in the design" in the traditional sense. But all of them determine whether the program succeeds. **Risk management is the invisible architecture of the program.**

### DFMEA vs. HARA: Complementary, Not Duplicate

HARA (Chapter 3) and DFMEA (this chapter) both analyze failures — why have both?

| | HARA (Chapter 3) | DFMEA (Chapter 9) |
|---|---|---|
| **Perspective** | Top-down: starts from operational hazards | Bottom-up: starts from design failure modes |
| **Question** | What hazardous events can harm users? | How can each component fail? |
| **Output** | Safety goals, ASIL ratings, FSRs | RPN scores, design improvements |
| **ISO Standard** | ISO 26262 Part 3 | ISO 26262 Part 7 / AIAG DFMEA |
| **When Done** | Before architecture (Month 3–5) | During design (Month 9–11) |

They cross-reference each other: HARA identifies that overcharge is ASIL-D → DFMEA FM-01 must have actions to drive RPN ≤ 45 for the voltage measurement function. One feeds requirements to the other.

### The Boeing Parallel: Risk Without Response

The Boeing 737 MAX program had a risk management system. MCAS was identified as a concern during development. But the risk was not escalated — it was documented and set aside because addressing it conflicted with the "no retraining" commercial commitment to airlines.

The IM-e1 BMS risk register has a similar tension: R03 (Safety: P=2, I=5, Score=10) and R07 (Technical: P=2, I=5, Score=10) both scored 10 pre-mitigation. Both received active mitigation plans. Neither was "managed" by noting it and moving on.

**The lesson**: a risk register without mitigation ownership and review cadence is worse than no risk register — it creates the illusion of control while the risks remain unaddressed. Every risk in the IM-e1 register has an owner, a deadline, and a success criterion for mitigation completion.

---

*Next: [README — Navigation Guide](README.md)*
