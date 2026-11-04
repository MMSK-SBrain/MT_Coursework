# Chapter 1: Mission Context and Concept of Operations (CONOPS)

> **SE Processes Applied:** Business/Mission Analysis (ISO/IEC 15288 §6.4.1)
> **AEZC517 Sessions Referenced:** Session 1 (Introduction to SE), Session 2 (SE Fundamentals)
> **Estimated Reading Time:** 20 minutes

---

## 1.1 Program Context — The IndraMotors IM-e1

**IndraMotors Private Limited** is a fictional Indian automotive OEM headquartered in Pune, Maharashtra. Having manufactured ICE vehicles for 35 years, IndraMotors has decided to launch its first purpose-built battery electric vehicle — the **IM-e1** — to capture share in India's rapidly growing EV market.

### Vehicle Specifications

| Parameter | Specification |
|---|---|
| Vehicle Segment | Mid-size electric sedan (C-segment) |
| Wheelbase | 2,650 mm |
| Battery Pack Voltage | 400V nominal (336V–420V range) |
| Battery Pack Energy | 40 kWh usable (43 kWh gross) |
| Cell Chemistry | LiFePO4 (LFP) — selected via Trade Study (see Chapter 5) |
| Pack Configuration | 56S8P (448 cells total, 8 modules of 7S8P) |
| Target Range | ~300 km (ARAI cycle) / ~260 km (real-world mixed) |
| Charging: AC | 7.2 kW on-board charger (Type 2 connector, CCS Combo 2 port) |
| Charging: DC | 150 kW peak DC fast charge (CCS Combo 2) |
| Target Price Band | ₹14–18 lakh ex-showroom |
| Target Launch | 18 months from program kickoff |

### Business Motivation

The Indian passenger EV market is growing at >60% CAGR. Key competitors include Tata Nexon EV (₹14.5–19.5L) and MG ZS EV (₹21–25L). IndraMotors must enter this segment with a competitive offer — or cede the market to competitors and erode their dealer network.

The IM-e1 program is structured around three business imperatives:
1. **Safety first:** A BMS-related thermal event would destroy IndraMotors' EV credibility before the brand is established
2. **Cost competitiveness:** BMS cost target is ₹18,000 per vehicle at 10,000 units/year volume
3. **Indian-market fit:** The system must work reliably in Indian conditions — 45°C peak summer, monsoon humidity, dusty roads, Himalayan altitude

### The BMS Role in the IM-e1

The Battery Management System (BMS) is the central intelligence of the battery pack. It is:
- The **primary safety system** for overcharge, over-discharge, overtemperature, and short circuit protection
- The **estimation engine** for State of Charge (SOC) and State of Health (SOH)
- The **communication gateway** between the battery pack and the rest of the vehicle
- The **thermal manager** controlling coolant flow to keep cells in their optimal temperature window

The BMS is a safety-critical system requiring ISO 26262 compliance at ASIL-D for its highest-criticality functions.

---

## 1.2 Mission Statement

Following the INCOSE format for mission statements:

> **"The IM-e1 Battery Management System shall monitor, protect, estimate, balance, and control the 40 kWh LFP battery pack to ensure safe energy delivery and maximum system availability for vehicle owner/operators and fleet customers, under all operational conditions encountered in the Indian market across an 8-year / 150,000 km service life."**

**Mission decomposed into five sub-missions:**

| Sub-Mission | Description | Primary Beneficiary |
|---|---|---|
| **Protect** | Prevent cell damage and safety hazards from overcharge, over-discharge, overcurrent, and overtemperature | Passengers, public, IndraMotors liability |
| **Estimate** | Provide accurate SOC and SOH to maximize usable energy and predict remaining range | Vehicle owner, fleet operator |
| **Monitor** | Continuously measure all cell voltages, temperatures, and pack current | Safety system, diagnostics |
| **Control** | Manage thermal system and contactors to maintain cells in optimal operating window | Battery longevity, performance |
| **Communicate** | Interface reliably with VCU, charger, and diagnostics systems | All downstream vehicle systems |

---

## 1.3 Concept of Operations (CONOPS)

The CONOPS defines how the BMS operates across the full range of scenarios it will encounter during vehicle service. Six primary operational scenarios are identified:

---

### Scenario 1: City Commute (Normal Operation)

**Description:** Vehicle used for daily urban driving in Pune/Bengaluru/Delhi. Stop-and-go traffic. Trips of 20–60 km. Ambient temperature 25–42°C.

**BMS Functions Active:**
- Continuous cell voltage monitoring (every 10ms via CMC ICs)
- SOC estimation running at 100ms update rate
- Thermal monitoring — passive heat rejection to coolant
- Fault detection (all tiers active)
- CAN transmission of SOC, power limits, and temperature to VCU every 100ms

**Critical Parameters Monitored:**
- Cell voltage: 2.5V (min) to 3.65V (max) per LFP cell
- Cell temperature: target 20–40°C
- Pack current: up to 200A continuous discharge at 40 kWh / 200V = ~40 kW

**Expected BMS Behaviors:**
- SOC displayed on instrument cluster, updated every 1 second
- BMS reports remaining range estimate to cluster via VCU
- No active balancing required (cells equalized during overnight charging)
- Thermal system: coolant pump at low speed, chiller bypass closed

**Potential Stress Conditions:**
- Extended low-SOC operation (driver ignores range warning)
- Elevated ambient: city heat soak increases cell temperature
- Frequent regenerative braking cycles — current reversal every 30–60 seconds

---

### Scenario 2: Highway Driving (High-Load Operation)

**Description:** Sustained high-speed driving at 90–120 km/h on expressways. Extended trip duration (2–4 hours). Ambient 35–45°C.

**BMS Functions Active:**
- High discharge current management (150–250A sustained)
- Active thermal control: coolant pump at high speed; chiller valve modulated
- Power limit reporting to VCU (derate as cell temperature rises)
- SOH-based capacity tracking

**Critical Parameters Monitored:**
- Pack temperature: rise rate monitored per cell; thermal derate threshold 45°C
- Pack current: continuous high-current measurement for coulomb counting
- Individual cell voltage spread: must remain <50mV across all 448 cells

**Expected BMS Behaviors:**
- Thermal derate: if any cell exceeds 45°C, BMS reduces maximum discharge power by 20% per °C above threshold
- Power limit CAN message updated every 100ms to VCU
- Contactor state: CLOSED throughout (no interruptions)

**Potential Stress Conditions:**
- Cell temperature approaching thermal derate boundary
- Long sustained discharge depleting SOC to near minimum (15% SOC)
- Combination of high ambient + high load = maximum thermal stress

---

### Scenario 3: DC Fast Charging (150 kW)

**Description:** Vehicle connected to DCFC charger at highway rest stop. 15–30 minute charging session. Charger communicates with BMS via CCS Combo 2 / CAN.

**BMS Functions Active:**
- Charge current limit calculation and communication to charger (updated every 100ms)
- Aggressive thermal management: chiller active, maximum coolant flow
- Cell balancing: passive balancing active during charging
- SOC estimation during charging (challenging due to flat LFP OCV curve)
- Contactor management: pre-charge sequence before charger energizes

**Critical Parameters Monitored:**
- Individual cell voltages during charging (must not exceed 3.65V per cell)
- Cell temperatures: must not exceed 45°C during charging
- Charging current: charger commanded based on BMS current limit request

**Expected BMS Behaviors:**
- CC-CV charging profile communicated to charger: constant current until any cell reaches 3.60V, then constant voltage taper
- Thermal protection: if any cell exceeds 42°C, reduce charge current by 50%
- Charging terminated by BMS when: all cells reach 3.65V, or SOC = 100%, or any fault condition

**Potential Stress Conditions:**
- Maximum thermal stress scenario (high power input + Indian summer ambient)
- Cell voltage imbalance amplified at high SOC
- Charger communication failure mid-session (BMS must detect and safely terminate charge)

---

### Scenario 4: AC Overnight Charging (7.2 kW)

**Description:** Vehicle plugged into home/office AC charger overnight. 6–8 hour session. Gentle charge rate (~C/5).

**BMS Functions Active:**
- Gentle thermal monitoring (low heat generation at C/5 rate)
- Active cell balancing (passive bleed balancing — primary use case)
- Top-balancing to full 100% SOC
- SOH tracking update after full charge-discharge cycle

**Critical Parameters Monitored:**
- Cell voltage convergence (balancing effectiveness tracked)
- Battery temperature: should remain near ambient — failure to cool is a fault signal

**Expected BMS Behaviors:**
- Full charge to 100% SOC (100% available for overnight AC charging; 80% recommended for daily use but not enforced)
- Balancing completes: all cell voltages within 10mV at end of charge
- BMS sends "charge complete" signal to VCU/telematics

**Potential Stress Conditions:**
- Charging in high-ambient environment without coolant (charging in Indian summer with no vehicle HVAC)
- Cell at very low SOC (<5%) — slow first charge phase, risk of under-voltage during initial current application

---

### Scenario 5: Parked — Extreme Heat (45°C Ambient)

**Description:** Vehicle parked outdoors in Indian summer (Rajasthan, Delhi NCR). No charging. Ambient temperature up to 47°C. Vehicle in direct sunlight — underbody temperature may reach 55°C.

**BMS Functions Active:**
- Low-power monitoring mode (vehicle off): cell voltage measured every 60 seconds
- Thermal monitoring: if cell temperature rises above 50°C, BMS wakes up coolant pump
- Self-discharge monitoring over extended park periods

**Critical Parameters Monitored:**
- Cell temperature: critical threshold 55°C (hardware cutoff) — must not be reached while parked
- Cell voltage: self-discharge tracking over days/weeks

**Expected BMS Behaviors:**
- BMS in sleep mode: standby current <5mA (12V battery preservation)
- Thermal wake event: BMS activates coolant pump if cell temp >48°C, runs until <42°C, then sleeps again
- If cell temperature reaches 55°C despite cooling: BMS sends high-priority CAN alert to telematics

**Potential Stress Conditions:**
- 12V battery depletion due to BMS wakeup cycles in extreme heat
- Extended park (3+ weeks): deep self-discharge may bring cells to minimum SOC
- No external power available for thermal management

---

### Scenario 6: Cold Soak and Cold Start (-5°C)

**Description:** Vehicle parked overnight in Northern India/Himalayan region. Cell temperature at -5°C at start. Owner attempts to drive immediately.

**BMS Functions Active:**
- Cold-start power limiting: max discharge current severely limited at <0°C
- Cell pre-heating request: BMS signals VCU to activate cell heaters (if equipped) or requests driver to charge first
- SOC estimation under cold conditions: EKF uses temperature-indexed model parameters

**Critical Parameters Monitored:**
- Cell temperature: minimum allowed discharge at -10°C (absolute minimum)
- SOC estimation accuracy: LFP OCV curve shifts at low temperature — EKF model must compensate

**Expected BMS Behaviors:**
- Below 0°C: maximum discharge power reduced to 30% of rated
- Below -10°C: charging disabled (lithium plating risk on LFP at sub-zero temperatures)
- BMS communicates thermal limitation to VCU → VCU shows "Battery Cold — Performance Limited" warning
- SOC estimate accuracy maintained via temperature-indexed EKF model (see Chapter 6)

**Potential Stress Conditions:**
- Owner attempts DC fast charging with cold cells — BMS must refuse or severely limit charge current
- SOC estimation error at cold temperatures — risk of unexpected range loss

---

## 1.4 System Context and Boundary

### System Context — External Entities and Interfaces

| External Entity | Interface Type | What BMS Receives | What BMS Sends | Direction |
|---|---|---|---|---|
| **HV Battery Pack** (cells, module hardware) | Analog/Direct | Cell voltages (per CMC IC), temperatures (NTC thermistors), pack current (Hall sensor) | Contactor control signals, balancing commands | Bidirectional |
| **Vehicle Control Unit (VCU)** | CAN-A (500 kbps) | Ignition state, gear request, regenerative braking torque request | SOC, SOH, max discharge/charge power limits, cell temperature, fault status | Bidirectional |
| **On-Board Charger (OBC)** | CAN-B (500 kbps) | Charge enable signal | Charge current limit, cell temperature, charge status | Bidirectional |
| **DC Fast Charger (DCFC)** | CAN via CCS Combo 2 | Charger ready signal, available charge power | Charge current limit, cell voltage/temp, BMS status | Bidirectional |
| **Thermal Management System** (pump, chiller, valves) | PWM output | [coolant flow feedback from flow sensor] | Coolant pump speed command (PWM), chiller valve command (PWM) | BMS outputs |
| **Instrument Cluster** | CAN-A (via VCU) | — | SOC%, range estimate, warning lamps (indirect, via VCU) | BMS → VCU → Cluster |
| **Telematics Unit** | CAN or OBD-II | — | Cell temperatures, SOC, fault codes (for remote monitoring) | BMS → Telematics |
| **Service Diagnostic Tool** | OBD-II / ISO 14229 UDS | Diagnostic requests, calibration commands | DTC responses, live data, calibration acknowledgement | Bidirectional |

### System Boundary Definition

**INSIDE BMS scope (BMS owns these functions):**
- All electronics on the MBMS PCB and CMC ICs
- SOC/SOH estimation algorithms
- Fault detection logic and contactor control decisions
- Thermal control algorithm (PID loops)
- Cell balancing control
- CAN communication stack

**OUTSIDE BMS scope (BMS interfaces with but does not control):**
- Battery cells and modules (physical chemistry, capacity)
- Contactors (physical relays — BMS sends commands, contactors are separate hardware)
- Coolant pump and chiller (physical actuators — BMS commands PWM, hardware executes)
- 12V power supply to BMS (provided by vehicle 12V battery)
- VCU decision-making (VCU decides vehicle behavior based on BMS data)

---

## 1.5 Operational Environment

The Indian operational environment is demanding and must be fully characterized to set correct requirements.

| Environmental Parameter | Specification | Standard Reference |
|---|---|---|
| **Operating Temperature (cells)** | -10°C to +55°C | AIS-048 (Indian EV safety standard) |
| **Storage Temperature** | -30°C to +60°C | IEC 62619 |
| **Ambient Humidity** | 5% to 95% RH (non-condensing) | AIS-048 |
| **Monsoon / Rain Ingress** | IP67 (BMS enclosure must withstand 30 min immersion at 1m) | IEC 60529 |
| **Dust Ingress** | IP6X (dusttight) | IEC 60529 |
| **Altitude** | Up to 2,500 m (Manali, Ladakh routes) | — |
| **Vibration** | IEC 60068-2-6: Sine sweep 10–500 Hz, 2g | IEC 60068-2-6 |
| **Shock** | IEC 60068-2-27: 30g half-sine, 11ms | IEC 60068-2-27 |
| **EMI/EMC** | CISPR 25 (vehicle EMC), ISO 11452 (immunity) | AIS-004 |
| **Road Conditions** | Unpaved roads, speed bumps, potholes (high vibration/shock) | Indian market characterization |

**Indian-Market-Specific Considerations:**

1. **Peak summer heat (45-47°C ambient):** Cell temperatures can reach 55–60°C without active cooling. The BMS thermal control system must handle this as a primary design requirement, not an edge case.

2. **Monsoon flooding:** Vehicles may wade through standing water. IP67 is mandatory — not just IP54. Service technicians may not be familiar with HV safety precautions.

3. **Altitude (Himalayan routes):** At 2,500 m, air pressure is ~74% of sea level. Air-cooled electronics run hotter. Coolant boiling point changes. BMS must function correctly at altitude.

4. **Dust (Rajasthan, rural roads):** Fine dust ingress into electronics enclosures is a failure mode — IP6X sealing is mandatory.

5. **Power grid quality:** AC charging from Indian grid (230V, 50Hz) with frequent voltage fluctuations. OBC handles this, but BMS must tolerate OBC ripple currents.

---

## 1.6 Success Criteria at Mission Level

The following mission-level success criteria define what "good" looks like for the IM-e1 BMS. These are not yet requirements — they are the measurable outcomes that requirements must achieve.

| SC-ID | Success Criterion | Measurement Method | Target |
|---|---|---|---|
| SC-01 | Owner experiences accurate SOC display | Compare instrument cluster SOC% to independently measured SOC via coulomb counter | ≤2% error across all CONOPS scenarios |
| SC-02 | No battery-related thermal incidents in first 3 years of fleet operation | Field incident reporting system | Zero events involving thermal runaway or contactor welding |
| SC-03 | Battery pack retains ≥80% of original capacity at warranty end | Periodic SOH measurement via BMS | SOH ≥80% at 8 years / 150,000 km |
| SC-04 | Owner never experiences unexpected range loss >10% vs. BMS prediction | Fleet telematics: compare predicted range at start of trip vs. actual achieved | ≤10% prediction error in 95th percentile of trips |
| SC-05 | Service technician can diagnose BMS fault within 30 minutes using OBD-II tool | Timed service technician test on production vehicle | 90% of faults diagnosable in ≤30 minutes |
| SC-06 | BMS certification obtained from ARAI on schedule | ARAI certification received before SOP | Certification letter received by Month 18 |
| SC-07 | BMS unit production cost at target volume | BoM cost analysis at 10,000 units/year | ≤₹18,000 per vehicle |

---

## 1.7 SE Process Reflection

### How CONOPS Connects to Stakeholder Analysis (Session 4)

The six CONOPS scenarios are not invented arbitrarily — they emerge directly from **stakeholder needs**. The vehicle owner (Scenario 1, 2) drives the performance scenarios. Fleet operators drive the high-utilization scenario (fast charging, Scenario 3). Regulatory bodies drive the environmental extremes (Scenarios 5, 6 represent edge cases ARAI will test). The connection:

> **CONOPS → Stakeholder Scenarios → Stakeholder Needs → Requirements**

This traceability chain begins here. Every need we identify in Chapter 2 should trace back to at least one CONOPS scenario.

### How the Mission Statement Constrains Requirements (Session 4)

The mission statement is deliberately broad — it says *what* the BMS must do, not *how*. But it establishes critical constraints that cascade into requirements:

- "...8-year / 150,000 km service life" → lifecycle requirement, drives cycle life specification
- "...all operational conditions encountered in the Indian market" → the 6 CONOPS scenarios define what "all" means
- "...safe energy delivery" → safety must be the highest-priority requirement category

In Session 4, you learned that **requirements must be traceable to mission objectives**. This mission statement is the anchor for that traceability chain throughout the case study.

### What SE Processes Come Next?

The Business/Mission Analysis process (§6.4.1) we applied in this chapter feeds directly into:

1. **Stakeholder Needs and Requirements Definition (§6.4.2)** — Chapter 2 identifies *who* has a stake in each CONOPS scenario, and *what* they need
2. **System Requirements Definition (§6.4.3)** — Chapter 3 converts stakeholder needs into verifiable system requirements

The CONOPS also directly informs architecture (Chapter 4) — the system context diagram we drew becomes the starting point for interface architecture definition.

---

*Next: [Chapter 2 — Stakeholder Analysis](02-stakeholder-analysis.md)*
