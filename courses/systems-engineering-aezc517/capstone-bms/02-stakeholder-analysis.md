# Chapter 2: Stakeholder Analysis

> **SE Processes Applied:** Stakeholder Needs and Requirements Definition (ISO/IEC 15288 §6.4.2)
> **AEZC517 Sessions Referenced:** Session 4 (Requirements Engineering)
> **Estimated Reading Time:** 20 minutes

---

## 2.1 Stakeholder Identification

A stakeholder is any individual, organization, or group with an interest in the BMS — whether they interact with it directly or are affected by its outcomes. The INCOSE guide defines stakeholders as "those that have a right, share, claim, or interest in a system or in its possession of characteristics that meet their needs and expectations."

For the IM-e1 BMS, we identified eight primary stakeholders through structured workshops involving IndraMotors' systems engineering, product planning, after-sales, and legal teams.

| Stakeholder ID | Role / Title | Organization | Relationship to BMS | Interaction Type |
|---|---|---|---|---|
| **SH-01** | Vehicle Owner / Driver | General public — individual EV buyer | Primary end user; drives the vehicle daily | Direct (sees SOC display, experiences performance) |
| **SH-02** | Fleet Operator | Commercial EV fleet (cab aggregators, delivery companies) | Manages 50–500 IM-e1 vehicles; monitors battery health via telematics | Direct (fleet management software, charging scheduling) |
| **SH-03** | IndraMotors Systems Engineering Team | IndraMotors R&D, Pune | Designs, integrates, and validates the BMS | Direct (designs and owns the system) |
| **SH-04** | ARAI / BIS Regulatory Bodies | Automotive Research Association of India; Bureau of Indian Standards | Certifies the vehicle including BMS safety compliance (AIS-048, AIS-038) | Indirect (reviews documentation, conducts type approval tests) |
| **SH-05** | Service Technician | IndraMotors authorized service centers | Maintains and repairs the BMS in the field using diagnostic tools | Direct (OBD-II access, physical service) |
| **SH-06** | Charging Infrastructure Operator | Tata Power EV Charging, EESL, Ather Grid | Operates DCFC stations that communicate with BMS during fast charging | Direct (CAN communication via CCS Combo 2 during DCFC) |
| **SH-07** | Insurance Company | General insurers covering EV policies | Assesses thermal runaway / fire risk for underwriting; reviews incident data | Indirect (incident reports, warranty data) |
| **SH-08** | End-of-Life Recycling Handler | Battery recycling companies (e.g., Attero Recycling) | Receives battery pack at vehicle end-of-life; needs SOH data for safe dismantling | Indirect (SOH report, residual capacity data at EOL) |

---

## 2.2 Stakeholder Needs Elicitation

For each stakeholder, needs were captured through interviews, workshops, and review of existing requirements from comparable EV programs. Each need is tagged with a unique ID (SN-01 through SN-26) for traceability to requirements in Chapter 3.

### SH-01: Vehicle Owner / Driver

| Need ID | Need Statement | Priority | Type |
|---|---|---|---|
| SN-01 | I need to know how much charge I have left at all times, accurately | High | Functional |
| SN-02 | I need the vehicle to warn me before I run out of charge, with enough range to reach a charger | High | Functional |
| SN-03 | I need the battery to retain at least 80% of its original range after 8 years of daily use | High | Quality / Lifecycle |
| SN-04 | I need fast charging to be safe — no battery fires while I wait at a charger | High | Safety |
| SN-05 | I need the vehicle to perform normally in Indian summer heat (45°C ambient) without unexpected shutdowns | Medium | Performance |
| SN-06 | I need the vehicle to start and drive in cold conditions (Shimla in winter, -5°C) | Medium | Performance |

### SH-02: Fleet Operator

| Need ID | Need Statement | Priority | Type |
|---|---|---|---|
| SN-07 | I need real-time battery health data for my entire fleet via telematics | High | Functional |
| SN-08 | I need to be able to schedule charging at lowest electricity tariff hours (off-peak) without harming battery | Medium | Functional |
| SN-09 | I need DC fast charging to be available daily without significantly degrading battery over 3 years | High | Quality / Lifecycle |
| SN-10 | I need clear fault codes when a vehicle's BMS has an issue, so my technicians can diagnose remotely | High | Functional |

### SH-03: IndraMotors Systems Engineering Team

| Need ID | Need Statement | Priority | Type |
|---|---|---|---|
| SN-11 | The BMS must be certifiable under AIS-048 and ISO 26262 without major redesign | High | Constraint |
| SN-12 | BMS unit cost must not exceed ₹18,000 at 10,000 units/year | High | Constraint |
| SN-13 | The BMS must be developable and validated within 18 months | High | Constraint |
| SN-14 | The BMS software must support over-the-air (OTA) updates for algorithm improvements post-launch | Medium | Functional |

### SH-04: ARAI / BIS Regulatory Bodies

| Need ID | Need Statement | Priority | Type |
|---|---|---|---|
| SN-15 | The BMS must meet all AIS-048 (EV safety) requirements for overcharge, over-discharge, and thermal protection | High | Constraint / Safety |
| SN-16 | The BMS must provide documented evidence of ISO 26262 compliance for all ASIL-D functions | High | Constraint |
| SN-17 | The BMS must prevent contactor welding from becoming an undetected, uncorrected fault | High | Safety |

### SH-05: Service Technician

| Need ID | Need Statement | Priority | Type |
|---|---|---|---|
| SN-18 | I need to diagnose BMS faults using standard OBD-II tools without proprietary equipment | High | Functional |
| SN-19 | I need clear DTC (Diagnostic Trouble Code) descriptions that guide repair actions | Medium | Functional |
| SN-20 | I need to safely access the BMS for physical inspection — IP67 must not require full pack disassembly | Low | Constraint |

### SH-06: Charging Infrastructure Operator

| Need ID | Need Statement | Priority | Type |
|---|---|---|---|
| SN-21 | The BMS must communicate reliably with our DCFC stations using standard CCS Combo 2 protocol | High | Functional |
| SN-22 | The BMS must not damage our chargers by requesting current beyond the charger's rated capacity | High | Safety / Constraint |

### SH-07: Insurance Company

| Need ID | Need Statement | Priority | Type |
|---|---|---|---|
| SN-23 | The BMS must have documented thermal runaway prevention mechanisms for risk assessment | High | Safety |
| SN-24 | In the event of a thermal event, the BMS must have logged data to reconstruct the sequence of events | Medium | Quality |

### SH-08: End-of-Life Recycling Handler

| Need ID | Need Statement | Priority | Type |
|---|---|---|---|
| SN-25 | I need a reliable SOH report from the BMS at vehicle end-of-life to assess residual capacity for second-life reuse | Medium | Functional |
| SN-26 | I need the BMS to enter a safe discharge state before we dismantle the pack (contactor open, cells at storage SOC 30%) | High | Safety |

---

## 2.3 Power / Interest Matrix

Stakeholders are mapped on a Power (ability to influence project decisions) vs. Interest (degree of personal stake in the outcome) grid. This determines the engagement strategy for each stakeholder.

| | **Low Interest** | **High Interest** |
|---|---|---|
| **High Power** | **KEEP SATISFIED** | **MANAGE CLOSELY** |
| | SH-04: ARAI/BIS (regulatory power but engagement is formal/periodic) | SH-03: IndraMotors SE Team (owns the program) |
| | SH-07: Insurance Company (can affect product launch; low day-to-day interest) | SH-01: Vehicle Owner (market success depends on their satisfaction) |
| **Low Power** | **MONITOR** | **KEEP INFORMED** |
| | SH-08: EOL Recycling Handler (end-of-life, low leverage during design) | SH-02: Fleet Operator (high interest, but B2B — lower power than regulators) |
| | | SH-05: Service Technician (important for field support, consulted on serviceability) |
| | | SH-06: Charging Infrastructure Operator (interface standards must align) |

**Engagement Strategy by Quadrant:**
- **Manage Closely (High Power, High Interest):** SH-01 (owner needs drive product requirements), SH-03 (internal — daily management). These stakeholders attend requirements reviews.
- **Keep Satisfied (High Power, Low Interest):** SH-04 (ARAI) — monthly compliance updates, formal pre-submission reviews; SH-07 (insurance) — design documentation shared proactively.
- **Keep Informed (Low Power, High Interest):** SH-02, SH-05, SH-06 — consulted at major design reviews; receive interface specifications.
- **Monitor (Low Power, Low Interest):** SH-08 — EOL requirements captured once, minimal ongoing engagement.

---

## 2.4 Stakeholder Conflicts

During workshops, four significant conflicts were identified where one stakeholder's need directly contradicts another's:

| Conflict ID | Stakeholder A | SH-A Need | Stakeholder B | SH-B Need | Nature of Conflict |
|---|---|---|---|---|---|
| **SC-01** | SH-01 (Owner) | SN-03: Maximum usable range — wants BMS to use 100% of battery capacity (0%–100% SOC window) | SH-03 (SE Team / Safety) | SN-15: Safety buffer — ISO 26262 and AIS-048 require minimum SOC buffer to prevent over-discharge damage | Using full capacity maximizes range; safety buffer reduces available energy. Tension: owner wants more range, safety requires reserve. |
| **SC-02** | SH-02 (Fleet Operator) | SN-09: Daily DC fast charging at 150 kW rate — maximum throughput for high-utilization fleets | SH-01 (Owner) / SH-03 (SE Team) | SN-03: Battery must last 8 years — daily DCFC degrades LFP cells faster than AC charging | Frequent DCFC at maximum rate reduces battery cycle life by ~15–20% vs. AC-only charging. Fleet needs throughput; longevity requirement conflicts. |
| **SC-03** | SH-03 Finance (Cost target) | SN-12: BMS cost ≤₹18,000 — cost reduction pressure to use single-sensor measurement paths | SH-03 Safety (ASIL-D) | SN-16: ISO 26262 ASIL-D for overcharge protection requires redundant measurement paths | Redundant sensing adds ₹2,500–₹4,000 to BMS BoM. Finance wants lowest cost; ASIL-D mandates redundancy. |
| **SC-04** | SH-05 (Service Technician) | SN-20: Easy physical access to BMS for inspection and repair in field conditions | SH-04 (ARAI) / Environment | SN-15: IP67 sealing — sealed enclosure required for monsoon resistance | IP67 sealing makes the BMS enclosure difficult to open without voiding the seal. Serviceability and ingress protection are in direct tension. |

---

## 2.5 Conflict Resolution Approach

**SE Process Used:** INCOSE stakeholder hierarchy — when stakeholder needs conflict, resolve using this priority order:

> **Safety > Regulatory Compliance > Operational Effectiveness > Commercial Optimization**

Applying this hierarchy to each conflict:

**SC-01 Resolution (Range vs. Safety Buffer):**
- Safety wins. BMS will enforce a **15%–95% usable SOC window** (leaving 5% at bottom for over-discharge protection, 5% at top for overcharge margin). Owner effectively has 80% of 40 kWh = 32 kWh usable.
- Mitigation: SOC display calibrated to show 0% at 15% physical SOC, 100% at 95% physical SOC. Owner sees a "full" range experience within the safe window.
- Residual tension: owner notices shorter range than spec sheet — managed through clear communication in user manual.

**SC-02 Resolution (Fast Charging vs. Battery Longevity):**
- Operational effectiveness wins over commercial pressure, but with constraints.
- BMS implements **temperature-derated fast charging**: if cell temperature rises above 35°C, DCFC current is progressively limited. This extends cycle life while maintaining throughput.
- Fleet operators receive a telematics dashboard showing projected SOH trajectory — this enables informed charging policy decisions.

**SC-03 Resolution (Cost vs. Redundancy):**
- Safety and regulatory compliance win. ASIL-D cannot be achieved without redundant measurement paths — this is a regulatory requirement, not a preference.
- Cost mitigation: redundancy is achieved by using the BQ76940 CMC IC's built-in secondary measurement path (already in IC silicon) rather than adding external hardware. Cost impact minimized to ~₹1,200 per unit.

**SC-04 Resolution (Serviceability vs. IP67):**
- Regulatory and safety win (IP67 is AIS-048 mandatory).
- Design mitigation: BMS enclosure uses standardized IP67 M12 connector ports for diagnostic interface. Service technicians connect OBD-II via sealed connector without opening the enclosure. Physical inspection requires authorized workshop with proper re-sealing tools and training.

---

## 2.6 Stakeholder Need Traceability

Each stakeholder need flows into one or more system requirements in Chapter 3. This table previews the traceability chain:

| Need ID | Need Summary | Flows Into | Chapter 3 Requirement Category |
|---|---|---|---|
| SN-01 | Accurate SOC display | SR-F-01 | Functional — SOC accuracy ≤2% |
| SN-02 | Low-SOC warning | SR-F-02 | Functional — Low SOC alert at 15% SOC |
| SN-03 | 80% SOH at 8 years | SR-LC-01 | Lifecycle — design life requirement |
| SN-04 | Safe fast charging | SR-S-01 through SR-S-04 | Safety — overcharge, overtemperature protection |
| SN-05 | Indian summer performance | SR-E-01, SR-E-02 | Environmental — operating temperature range |
| SN-06 | Cold start capability | SR-P-03 | Performance — cold start power limit |
| SN-07 | Fleet telematics data | SR-C-03 | Communication — telematics CAN message |
| SN-09 | DCFC longevity | SR-S-05 | Safety — thermal derate during fast charging |
| SN-10 | Remote fault diagnosis | SR-C-04 | Communication — DTC over CAN |
| SN-11 | AIS-048 / ISO 26262 compliance | SR-S-01 to SR-S-06 | Safety — all ASIL-rated requirements |
| SN-12 | Cost ≤₹18,000 | SC-03 resolution — design constraint | Constraint (not a verifiable requirement; tracked as design constraint) |
| SN-13 | 18-month development | See Chapter 8 (Project Plan) | Project constraint |
| SN-15 | AIS-048 safety requirements | SR-S-01 through SR-S-06 | Safety requirements (HARA-derived) |
| SN-16 | ISO 26262 ASIL-D compliance | SR-S-01, SR-S-02 | Safety — ASIL-D designation on critical SRs |
| SN-17 | Contactor welding detection | SR-S-06 | Safety — contactor fault detection |
| SN-18 | OBD-II diagnostics | SR-C-04 | Communication — UDS over OBD-II |
| SN-21 | CCS Combo 2 communication | SR-C-02 | Communication — DCFC interface |
| SN-23 | Thermal runaway prevention | SR-S-04 | Safety — thermal runaway detection |
| SN-25 | SOH report at EOL | SR-F-03 | Functional — SOH estimation and reporting |
| SN-26 | Safe EOL discharge state | SR-S-07 | Safety — EOL safe state capability |

---

## 2.7 SE Process Reflection

### Stakeholder Analysis in Session 4: Applied Here

Session 4 taught that requirements engineering begins with stakeholder analysis — you cannot write good requirements without knowing *whose* needs you are satisfying. This chapter demonstrates exactly that process:

- We identified 8 stakeholders, not just the obvious one (owner)
- We elicited 26 distinct needs from structured workshops
- We found 4 significant conflicts and resolved them using the INCOSE hierarchy
- We created SN-IDs that will appear in Chapter 3 as the "Source" column of every requirement

The key lesson: **requirements without stakeholder traceability are guesses.** Every requirement in Chapter 3 traces back to a stakeholder need in this chapter.

### What Would Have Happened in Boeing 737 MAX? (Session 6 Connection)

Recall the Boeing 737 MAX MCAS case study from Session 6. The stakeholder analysis failure was profound:

- **Passengers** (the most safety-critical stakeholder) were not on the stakeholder list
- **Pilots** (the human operators) were explicitly excluded from the MCAS design decisions to save training costs
- **Airlines** (commercial customers) were over-weighted: their need for "no retraining" drove a design that hid MCAS from pilots

Now look at the IM-e1 BMS stakeholder table. We have:
- SH-01 (Owner) — equivalent to the passenger — is in the "Manage Closely" quadrant
- SH-05 (Service Technician) — the human who interacts with the system physically — has needs SN-18, SN-19, SN-20 directly in our requirements pipeline
- Conflict SC-03 (cost vs. safety redundancy) was **resolved in favor of safety** — the opposite of Boeing's choice

**The lesson:** Inclusive stakeholder analysis, with conflicts resolved through a principled hierarchy, is what prevents MCAS-type failures.

### Bridge to Chapter 3

The 26 stakeholder needs captured here are the raw material for system requirements in Chapter 3. The process:

1. Each SN-ID becomes the "Source" for one or more requirements
2. Needs are elaborated into verifiable, unambiguous requirement statements
3. Safety-related needs (SN-04, SN-15, SN-16, SN-17, SN-23) are analyzed through the HARA process to determine ASIL ratings

The critical transition: **needs are qualitative** ("I need safe fast charging") — **requirements are quantitative and verifiable** ("BMS shall open contactors within 10ms when any cell temperature exceeds 55°C").

---

*Next: [Chapter 3 — Requirements Engineering](03-requirements-engineering.md)*
