# Chapter 6: Design Definition

> **SE Processes Applied:** Design Definition (ISO/IEC 15288 §6.4.6)
> **AEZC517 Sessions Referenced:** Session 5 (System Design and Architecture), Session 7 (Operational and Functional Analysis)
> **Estimated Reading Time:** 40 minutes

---

## 6.1 Design Definition Process

Architecture definition (Chapter 4) established the structure: what components exist and how they connect. Trade studies (Chapter 5) made two key technology selections: LFP cells and indirect liquid cooling. Design definition now elaborates **how** each function is implemented within that architecture.

This chapter covers the four most critical BMS subsystem designs:

| Subsystem | Key Design Challenge | Trade Study Impact |
|---|---|---|
| SOC Estimation (§6.2) | LFP flat OCV curve makes simple algorithms fail | LFP selection makes EKF mandatory |
| Cell Balancing (§6.3) | Equalize 448 cells with minimal cost and thermal load | LFP lower imbalance tendency → passive balancing sufficient |
| Thermal Management Control (§6.4) | Maintain cells 15–45°C at 45°C Indian ambient + 150 kW DCFC | Liquid cooling selection → PID-controlled pump/chiller |
| Fault Detection & Protection (§6.5) | ASIL-D protection with ≤1ms hardware response | Architecture's 3-tier protection realized in design |

Each design includes: algorithm description, key parameters, error budget or sizing calculation, and traceability to requirements.

---

## 6.2 SOC Estimation Design

### 6.2.1 Algorithm Selection

State of Charge (SOC) is the most important BMS output — it drives the range display, low-battery warnings, charge control, and power limits. The requirement is SR-F-01: ≤2% error across all temperatures and SOC values.

Three candidate algorithms were evaluated:

| Algorithm | Principle | LFP Suitability | Accuracy at -10°C |
|---|---|---|---|
| **Coulomb Counting** | Integrate current over time: SOC = SOC₀ − ∫I·dt / Q_nom | Poor — accumulates drift; no correction mechanism | Poor — current sensor drift magnified |
| **OCV Lookup Table** | Measure resting voltage → map to SOC via OCV-SOC curve | **Very poor for LFP** — flat OCV curve (3.2V–3.3V spans 20%–90% SOC) → ±30% error from voltage alone | Usable only after 2-hour rest (impractical) |
| **Extended Kalman Filter (EKF)** | Fuses current integration with voltage-based correction using a battery model | **Excellent for LFP** — EKF corrects drift; handles flat OCV via state estimation | Good with temperature-indexed model parameters |

**Selection: Extended Kalman Filter (EKF)**

The LFP OCV curve plateau (Fig. notional: OCV is virtually flat from 20%–90% SOC) is the defining design constraint. Coulomb counting alone drifts over time with no correction. OCV lookup requires extended rest periods unsuitable for a vehicle application. EKF combines both — using current integration as the process model and cell voltage as the measurement — and achieves the required ≤2% accuracy even over the flat OCV region because the Kalman gain correctly handles low-information measurements.

### 6.2.2 Battery Model — 2RC Thevenin Equivalent Circuit

The EKF requires a dynamic model of cell behavior. The 2RC Thevenin equivalent circuit model is used:

```
        R0          R1          R2
 +──────[R0]──┬────[R1]──┬────[R2]──┬──── V_terminal
              │    C1    │    C2    │
 V_OCV(SOC,T)  ─[C1]─  ─[C2]─
              │          │          │
 ─────────────┴──────────┴──────────┴────
```

**Circuit Parameters:**

| Parameter | Symbol | Description | Value Range (LFP, 25°C) |
|---|---|---|---|
| Open Circuit Voltage | V_OCV | Equilibrium voltage — function of SOC and temperature. Flat in 20%–90% SOC for LFP | 2.50V (0% SOC) – 3.65V (100% SOC); plateau 3.20–3.32V (20%–90%) |
| Series Resistance | R0 | Ohmic resistance — causes instantaneous voltage drop on current step | 0.8–1.5 mΩ (cell level) |
| First RC Pair | R1, C1 | Short-time-constant diffusion (τ1 = R1×C1 ≈ 20–100s) | R1: 0.5–1.2 mΩ, C1: 50–200 kF |
| Second RC Pair | R2, C2 | Long-time-constant diffusion (τ2 = R2×C2 ≈ 500–2000s) | R2: 0.3–0.8 mΩ, C2: 200–1000 kF |

**Critical Note for LFP:** The V_OCV vs. SOC relationship is nearly constant from 20%–90% SOC (the "flat plateau"). This means ∂V_OCV/∂SOC ≈ 0.001 V/% SOC in this region — the Kalman gain for the SOC state is very small during the plateau. The EKF still converges, but relies more heavily on current integration during plateau operation and corrects primarily at the end-of-discharge tail and end-of-charge shoulder where the OCV curve has higher slope.

### 6.2.3 EKF Implementation

The EKF maintains a state vector and covariance matrix, updated at each timestep (100ms cycle):

**State Vector:** `x = [SOC, V_R1, V_R2]ᵀ`
- SOC: State of charge (0.0 to 1.0)
- V_R1: Voltage across first RC pair (V)
- V_R2: Voltage across second RC pair (V)

**Process Model (Prediction Step):**

```
SOC(k+1)   = SOC(k) − (η · I(k) · Δt) / Q_nom
V_R1(k+1)  = V_R1(k) · exp(−Δt / τ1) + R1 · I(k) · (1 − exp(−Δt / τ1))
V_R2(k+1)  = V_R2(k) · exp(−Δt / τ2) + R2 · I(k) · (1 − exp(−Δt / τ2))
```

Where: η = Coulombic efficiency (≈ 0.998 for LFP), I(k) = pack current (A, positive = discharge), Δt = 0.1s, Q_nom = nominal capacity (Ah)

**Measurement Model (Update Step):**

```
V_predicted = V_OCV(SOC, T) − V_R1 − V_R2 − R0 · I
Innovation  = V_measured − V_predicted
```

The Kalman gain K adjusts how much the innovation (prediction error) corrects the state estimate. During the OCV plateau, K for SOC is small (low observability from voltage alone), so SOC relies more on current integration. At the OCV curve shoulders, K for SOC is larger (high observability).

**Process Noise (Q matrix):** Tuned to trust the model moderately — not too stiff (ignores sensor noise) or too loose (drifts with current sensor errors).

**Measurement Noise (R matrix):** Set to reflect CMC IC voltage measurement noise (±1.5 mV, from BQ76940 spec) plus ADC quantization.

### 6.2.4 Model Parameter Identification

Model parameters (R0, R1, C1, R2, C2, and V_OCV curve) depend on temperature and SOC. Parameters are identified from **Hybrid Pulse Power Characterization (HPPC)** tests:

**HPPC Test Procedure:**
1. Charge cell to 100% SOC; rest 2 hours
2. Discharge 10% SOC (at 1C); rest 1 hour (measure V_OCV)
3. Apply 30-second 2C discharge pulse; rest 40 seconds; apply 30-second C/2 charge pulse
4. Measure voltage response → fit 2RC model to transient
5. Repeat steps 2–4 until SOC = 0%
6. Repeat entire procedure at 5 temperatures: -10°C, 0°C, 15°C, 30°C, 45°C

**Output: Parameter Lookup Table**

Parameters are stored as indexed tables in MBMS non-volatile memory (NVRAM). EKF interpolates between table entries at runtime.

| Temperature | R0 (mΩ) | R1 (mΩ) | τ1 (s) | R2 (mΩ) | τ2 (s) |
|---|---|---|---|---|---|
| -10°C | 3.2 | 2.8 | 85 | 1.5 | 1200 |
| 0°C | 2.0 | 1.8 | 65 | 1.0 | 900 |
| 15°C | 1.4 | 1.2 | 45 | 0.7 | 700 |
| 30°C | 1.1 | 0.9 | 32 | 0.5 | 550 |
| 45°C | 0.9 | 0.7 | 25 | 0.4 | 420 |

**SOH Adaptation (Recursive Least Squares):**
As the cell ages, Q_nom decreases (capacity fade) and R0 increases (power fade). The EKF model must track this. After each completed charge-discharge cycle, a Recursive Least Squares (RLS) algorithm updates Q_nom and R0 in the NVRAM parameter table. This keeps the SOC estimate accurate as the cell ages without requiring a full re-characterization.

### 6.2.5 Error Budget

The SR-F-01 requirement is ≤2.0% SOC error. The error budget allocates this across contributing sources:

| Error Source | Contributor | Error Budget (% SOC) |
|---|---|---|
| EKF algorithm convergence error | Model parameter uncertainty, filter tuning | ≤1.0% |
| Cell voltage measurement noise | CMC IC BQ76940 (±1.5 mV) + ADC quantization | ≤0.3% |
| Current measurement error | LEM HAB Hall sensor (±0.5% full scale at 250A = ±1.25A) | ≤0.5% |
| Temperature sensor error | NTC thermistor (±0.5°C) → model parameter interpolation error | ≤0.2% |
| **Total (RSS)** | Root Sum Square of all contributors | **≤1.2%** |
| **Total (Worst Case)** | Linear sum (all errors maximum simultaneously) | ≤2.0% |

The error budget meets SR-F-01 even in the worst-case scenario. The RSS estimate of ≤1.2% provides design margin.

---

## 6.3 Cell Balancing Design

### 6.3.1 Balancing Strategy

Over time, individual cells in the 56S8P pack develop small differences in SOC due to manufacturing tolerances in capacity and self-discharge rate. If uncorrected, the weakest cell limits the pack — the BMS must cut off when the lowest-SOC cell reaches minimum, even if other cells still have charge remaining.

**Selected strategy: Passive (Dissipative) Balancing**

Trigger conditions (both must be true):
1. Any cell voltage > 3.50V (approaching end-of-charge — balancing only meaningful at high SOC)
2. Maximum delta-V within any module > 10 mV (imbalance exists — balancing is needed)

When triggered, the CMC IC activates a bleed resistor for the highest-voltage cells, converting excess energy to heat until all cells in the module are within 10 mV.

**Why passive balancing is appropriate for LFP:**
- LFP self-discharge rate is extremely low (~1–3% per month) — cells stay balanced naturally between charges
- LFP flat OCV curve means small voltage differences correspond to larger SOC differences during plateau — but at the charge shoulders (where balancing activates), the OCV slope is steeper and voltage-based balancing is effective
- The typical per-cell imbalance in a well-manufactured LFP pack after 1 year: 5–15 mV → correctable in a single overnight charge session

### 6.3.2 Passive Balancing Circuit

Each CMC IC channel (14 channels per BQ76940) has an internal balancing MOSFET that switches an external bleed resistor:

**Circuit Parameters:**
- Balancing current: 50 mA per cell
- Bleed resistor value: R_bleed = V_cell / I_balance = 3.2V / 0.050A = **64Ω** (use standard value 68Ω → 47mA actual)
- Power dissipated per cell during balancing: P = I² × R = (0.047A)² × 68Ω = **0.15 W per cell**
- Maximum simultaneous balancing cells per module: 6 (out of 14 — limited by CMC IC thermal rating)
- Maximum thermal dissipation per module during balancing: 6 × 0.15W = **0.9 W** (easily managed by module enclosure)

**Thermal limitation during balancing:**
If balancing is active during charging, the combination of charging heat + balancing dissipation must not cause cell temperature to exceed 42°C (the thermal derate threshold). BMS monitors cell temperature continuously and suspends balancing if any cell temperature exceeds 40°C.

**Duration estimate:**
For a typical end-of-charge imbalance of 30 mV across 7S cells in a module:
- Energy difference per cell ≈ C_cell × ΔV / 2 = (nominal 50Ah × 3.6V) × 0.030V / 3.2V ≈ 1.7 Wh
- Balancing power: 0.15W
- Time to balance: 1.7 Wh / 0.15W = 11.3 hours

This confirms that balancing must run during overnight AC charging (Scenario 4) — not during short DCFC sessions. The BMS schedules balancing accordingly: balancing only activates when charging power is available (not during driving).

### 6.3.3 Active Balancing (Not Selected)

Active balancing transfers charge between cells using inductors or capacitors rather than dissipating it as heat, achieving >90% energy transfer efficiency versus ~0% for passive balancing.

**Why active balancing was not selected for IM-e1:**

1. **LFP reduces the need:** LFP cells have lower self-discharge variation and more predictable aging than NMC, resulting in smaller imbalance over time. The 11-hour passive balancing time fits within overnight charging — active balancing's speed advantage is not needed.

2. **Cost:** Active balancing circuits (one inductor + driver per cell) add ₹3,000–₹6,000 per vehicle. This exceeds the BMS cost budget impact justified by the marginal improvement.

3. **Indian service network:** Active balancing circuits are unfamiliar to most Indian EV service technicians. A failure in the active balancing hardware would be difficult to diagnose in a Tier-2 city service center.

4. **Complexity and ASIL:** Active balancing adds software and hardware complexity. If the active balancing circuit malfunctions (e.g., transfers charge to an already full cell), it becomes a new fault mode requiring ASIL analysis.

Active balancing remains the better choice for NMC or NCA batteries with higher self-discharge variability, or for high-cycling fleet applications. IndraMotors will evaluate for the IM-e2 (longer range, higher-cycling use case).

---

## 6.4 Thermal Management Control Design

### 6.4.1 Control Architecture

The thermal management system has two control objectives, implemented as nested loops:

**Outer Loop — Cell Temperature Setpoint Control**
- Goal: Maintain cell temperature at setpoint
- Setpoints: 25°C during charging (lower → less thermal stress during charge), 30°C during driving (slightly higher allowed → reduces pump energy)
- Input: Maximum cell temperature (from hottest NTC thermistor in pack)
- Output: Target coolant inlet temperature

**Inner Loop — Coolant Temperature Control**
- Goal: Achieve target coolant inlet temperature
- Input: Coolant inlet temperature (from NTC on coolant supply pipe)
- Output: Coolant pump speed (PWM duty cycle, 0–100%) + chiller bypass valve position

```
Cell Temp        Coolant Temp       Pump Speed
Setpoint ──►[Outer PID]──► Setpoint ──►[Inner PID]──► PWM to Pump
    ▲                           ▲
Measured                   Measured                   ──► Chiller Valve
Cell Temp                Coolant Inlet
(from CMC)               (from NTC)
```

**Chiller Bypass Valve Logic:**
- If coolant outlet temperature (after pack) > coolant inlet setpoint + 5°C AND ambient temperature > 35°C → open chiller bypass valve (engage refrigerant chiller)
- If coolant outlet temperature < coolant inlet setpoint − 2°C → close chiller bypass (passive heat rejection sufficient)
- The chiller shares the vehicle cabin AC compressor — cabin AC is temporarily limited when battery chiller is at maximum demand

### 6.4.2 PID Controller Design

Both loops use discrete-time PID controllers implemented in the ASIL-B SW partition of the MBMS:

**PID Control Law (position form):**
```
u(k) = Kp·e(k) + Ki·Ts·Σe(j) + Kd·(e(k)−e(k−1))/Ts
```
Where: e(k) = setpoint − measured temperature, Ts = sample period (200ms for thermal loop)

**Initial Tuning (Ziegler-Nichols open-loop step response method):**

Step test: Apply 50% pump speed step; record coolant temperature response; measure:
- Process gain K_p ≈ 0.8°C per % pump speed
- Dead time L ≈ 15 seconds (transport delay in coolant loop)
- Time constant τ ≈ 120 seconds (thermal inertia of pack)

Ziegler-Nichols PI tuning (thermal process — derivative not needed):
- Kp = 0.9 × τ / (K_p × L) = 0.9 × 120 / (0.8 × 15) = **9.0**
- Ki = Kp / (3.33 × L) = 9.0 / (3.33 × 15) = **0.18 per second**

These are initial values; final tuning is performed via HIL simulation with a validated thermal model of the pack (see Chapter 7, TC-04).

**Anti-Windup:** The integral term is clamped when the pump speed output saturates (0% or 100%). Without anti-windup, the integrator winds up during saturation, causing sluggish recovery when the setpoint becomes achievable — a significant issue during cold start (pump at 0%, integrator accumulates large negative error).

### 6.4.3 Thermal Runaway Detection

Thermal runaway is qualitatively different from normal overtemperature — it is a self-accelerating exothermic reaction that, once started, cannot be stopped by the cooling system. Detection must be fast enough to open contactors before the reaction propagates to adjacent cells.

**Detection Mechanism: Rate-of-Rise (RoR)**

```
If [dT_cell/dt > 2°C/second] for any cell → THERMAL RUNAWAY DETECTED
→ Open all contactors immediately (≤100ms per SR-S-03)
→ Transmit thermal runaway fault on CAN (priority message)
→ Activate maximum coolant flow
→ Log event with cell ID, temperature, and timestamp to NVRAM
```

**Why rate-of-rise, not absolute temperature?**
- Absolute threshold (e.g., 55°C cutoff) triggers only when cells are already dangerously hot
- LFP thermal runaway onset is ~270°C — but propagation to that temperature from a localized failure occurs in 10–60 seconds
- The rate-of-rise precursor (dT/dt > 2°C/s) is detectable ~30–120 seconds before runaway onset
- At normal DCFC rates, maximum cell temperature rise rate is ~0.5°C/s — the 2°C/s threshold has 4× headroom from normal operation

**Implementation independence from SOC algorithm:**
SR-S-03 requires this function to be independent of the SOC estimation algorithm. The rate-of-rise detector runs in the ASIL-D safety partition (Core 0) with a dedicated temperature array updated directly from CMC IC data — it does not share state variables with the EKF running in Core 1. A single MCU reset on Core 1 cannot disable the Core 0 rate-of-rise detector.

### 6.4.4 Coolant System Sizing

A simplified thermal calculation validates that indirect liquid cooling can maintain cells below 45°C during peak DCFC at 45°C ambient:

**Heat Generation During DCFC:**
- Charger input: 150 kW at 90% efficiency → 135 kW to battery, 15 kW waste heat
- Cell internal heat generation rate: P_heat = I² × R_internal_total
  - Pack current at 150 kW charging: I = 150,000W / 360V ≈ 417A (at 360V pack voltage)
  - Total internal resistance (56S, 1 cell = 1.1mΩ at 30°C): R_total = 56 × 1.1mΩ / 8 (parallel) = 7.7 mΩ
  - Heat generated: P = I² × R = (417)² × 0.0077 = **1,340W = 1.34 kW**

> Note: The 15 kW figure cited above includes charger electronics waste heat; the battery pack itself generates ~1.34 kW from cell resistance during DCFC at 417A. The remaining charger heat is in the OBC unit, not the pack.

**Cooling Capacity Required:**
To maintain pack temperature at 45°C cell (worst case, 45°C ambient — zero temperature gradient between cell and ambient with no cooling):
- Required heat rejection: ≥1.34 kW (cell resistive heat) + any ambient heat soaked through pack enclosure (estimated ~0.5 kW) = **~1.84 kW**

**Coolant Flow Rate Calculation:**
- Coolant: 50% glycol-water, specific heat C_p ≈ 3.5 kJ/kg/K, density ≈ 1.07 kg/L
- Target coolant temperature rise across pack (ΔT_coolant): 5°C (inlet 25°C → outlet 30°C)
- Required mass flow: ṁ = Q / (C_p × ΔT) = 1840W / (3500 J/kg/K × 5K) = 0.105 kg/s = 5.9 L/min
- **Selected pump sizing: 8 L/min at maximum speed** (provides 35% design margin)
- Pump power: At 8 L/min and ~30 kPa system pressure drop: P_pump = (8/60 L/s × 0.001 m³/L × 30,000 Pa) / 0.6 efficiency = **67W** (acceptable parasitic load)

**Conclusion:** Indirect liquid cooling at 8 L/min with a chiller providing additional cooling when needed is thermally adequate. This validates the trade study decision in Chapter 5.

---

## 6.5 Fault Detection and Protection Design

### 6.5.1 Three-Tier Protection Architecture

The HARA identified overcharge and overtemperature as ASIL-D hazards — meaning a single failure must not cause the protection to fail. This drives a three-tier independence architecture:

```
TIER 1 — HARDWARE (≤1ms response)
┌─────────────────────────────────────────────────────────────────┐
│ CMC IC BQ76940 hardware OV/UV comparator                        │
│ Trigger: Cell voltage > 3.65V (OV) or < 2.50V (UV)             │
│ Response: GPIO interrupt to MBMS → MBMS contactor driver fires  │
│ Independence: Entirely hardwired; CMC IC firmware not involved  │
│ No MBMS software involved — completely hardware path            │
└─────────────────────────────────────────────────────────────────┘
         ↓ (independent of Tier 1)
TIER 2 — SOFTWARE ASIL-D (≤10ms response)
┌─────────────────────────────────────────────────────────────────┐
│ MBMS Core 0 ASIL-D SW partition                                 │
│ Trigger: Cell voltage > 3.60V OR cell temp > 55°C OR            │
│          rate-of-rise > 2°C/s (checked every 10ms)             │
│ Response: Software command to open contactors via MBMS driver   │
│ Independence: Runs on Core 0; protected by MPU from Core 1 SW   │
└─────────────────────────────────────────────────────────────────┘
         ↓ (independent of Tiers 1 and 2)
TIER 3 — VEHICLE LEVEL (≤100ms response)
┌─────────────────────────────────────────────────────────────────┐
│ VCU vehicle-level safe state                                    │
│ Trigger: BMS Fault_Status CAN message (IFC-05) set to CRITICAL  │
│ Response: VCU implements vehicle safe state (motor off,          │
│           hazard lights, driver notification)                   │
│ Independence: VCU is an independent ECU from BMS                │
└─────────────────────────────────────────────────────────────────┘
```

**Why three tiers?**
- A single SW bug in Core 0 cannot disable Tier 1 (hardware path is independent)
- A CMC IC power supply failure cannot disable Tier 2 (MBMS has independent supply)
- A BMS ECU failure cannot disable Tier 3 (VCU monitors BMS CAN heartbeat and implements safe state on timeout)

Each tier provides a fail-safe fallback. This is defense-in-depth for safety-critical systems.

### 6.5.2 Fault Codes and Severity Classification

All BMS faults are classified into four severity levels with defined responses:

| Severity | Level | Response | DTC Set | Contactor Action | Example Faults |
|---|---|---|---|---|---|
| **Level 1 — Warning** | Informational | Alert driver via instrument cluster | Yes (non-latching) | None — continue normal operation | Cell temperature >40°C (early warning), SOC <25% |
| **Level 2 — Derate** | Performance limited | Reduce max power; alert driver | Yes (non-latching) | None — reduce power limits only | Cell temperature >45°C → power derate; SOC <15% |
| **Level 3 — Fault (Non-Critical)** | System fault | Stop charging or driving; service required | Yes (latching — requires technician reset) | None immediately (safe to park) | Contactor welding (detected after event); insulation resistance low |
| **Level 4 — Fault (Critical)** | Immediate shutdown | Open all contactors immediately | Yes (latching) | **Open all contactors** | Cell voltage >3.65V; cell temp >55°C; thermal runaway detected |

**DTC Code Structure (per ISO 14229 / ISO 15031-6):**

| DTC ID | Name | Severity | Tier | Description |
|---|---|---|---|---|
| P1B00 | BMS_OV_CELL | Level 4 | Tier 1+2 | Cell overvoltage — hardware and software triggered |
| P1B01 | BMS_UV_CELL | Level 4 | Tier 1+2 | Cell undervoltage — hardware and software triggered |
| P1B02 | BMS_OT_CELL | Level 4 | Tier 2 | Cell overtemperature >55°C |
| P1B03 | BMS_TR_DETECT | Level 4 | Tier 2 | Thermal runaway rate-of-rise detected |
| P1B04 | BMS_CONT_WELD | Level 3 | Tier 2 | Contactor welding fault — feedback mismatch |
| P1B05 | BMS_INSUL_LOW | Level 3 | Tier 2 | Insulation resistance <40 kΩ |
| P1B06 | BMS_CAN_LOSS | Level 2 | Tier 2 | VCU CAN communication lost >500ms |
| P1B07 | BMS_CELL_IMB | Level 1 | Tier 2 | Cell voltage imbalance >50mV (needs balancing) |
| P1B08 | BMS_SOC_LOW | Level 2 | Tier 2 | SOC <15% physical (displayed as 0% to driver) |

### 6.5.3 Contactor Control State Machine

The contactor control function (F5.1) manages the three contactors (Main+, Main−, Pre-charge) through a defined state machine to prevent inrush current damage and ensure safe isolation:

```
                    ┌──────────┐
     Power-on ───►  │  OPEN   │◄──── Critical fault (P1B00-P1B03)
                    │Main+: OFF│◄──── Manual service disconnect
                    │Main−: OFF│◄──── CAN loss >500ms (Level 2+)
                    │PreChg:OFF│
                    └────┬─────┘
                         │ VCU: IgnitionON received
                         ▼
                    ┌──────────┐
                    │PRE-CHARGE│  Pre-charge contactor closes first
                    │Main+: OFF│  Current through R_precharge (~100Ω)
                    │Main−: ON │  charges inverter capacitors slowly
                    │PreChg: ON│  (prevents inrush current spike)
                    └────┬─────┘
                         │ Inverter capacitor voltage ≥ 90% pack voltage
                         │ (detected via voltage sensor on inverter rail)
                         │ AND time ≥ 500ms
                         ▼
                    ┌──────────┐
                    │  CLOSED  │  Normal vehicle operation
                    │Main+: ON │  Pre-charge contactor opens after
                    │Main−: ON │  Main+ closes (parallel path to small R)
                    │PreChg:OFF│
                    └────┬─────┘
                         │ IgnitionOFF or Level 3/4 fault
                         ▼
                    ┌──────────┐
                    │  FAULT   │  Latching state for Level 3/4 faults
                    │Main+: OFF│  Requires OBD-II technician reset
                    │Main−: OFF│  (DTC must be investigated before reset)
                    │PreChg:OFF│
                    └──────────┘
```

**Safety requirement for state feedback (SR-S-06):**
After each contactor command, MBMS reads the contactor state feedback GPIO within 500ms. If feedback does not match command (e.g., Main+ commanded OFF but feedback = ON → welded contactor), DTC P1B04 is set, Level 3 fault logged. On next fault event requiring contactor open, if Main+ is welded, MBMS activates a secondary isolation path (service disconnect relay if equipped) and flags unrecoverable fault.

---

## 6.6 Design-to-Architecture Traceability

| Design Element | Architecture Element (Ch 4) | Requirements Satisfied (SR-IDs) |
|---|---|---|
| EKF SOC estimator (§6.2) | MBMS Core 1 ASW — ASIL-B partition | SR-F-01 (SOC ≤2%), SR-C-01 (SOC to VCU) |
| 2RC Thevenin model + HPPC parameters | NVRAM (STM32H755 flash) | SR-F-01 (accuracy across temperature) |
| Passive balancing algorithm + bleed circuit | CMC IC BQ76940 balancing drivers + external resistors | SR-F-04 (balance within 10mV) |
| PID thermal control (§6.4.1, 6.4.2) | MBMS Core 1 ASW — ASIL-B partition + PWM outputs (IFC-09, IFC-10) | SR-S-04 (temp <55°C charging), SR-S-05 (DCFC derate) |
| Thermal runaway rate-of-rise (§6.4.3) | MBMS Core 0 ASIL-D partition (independent of Core 1) | SR-S-03 (≤100ms cutoff, ASIL-D) |
| Tier-1 HW protection (§6.5.1) | CMC IC BQ76940 hardware comparator → GPIO → contactor driver | SR-P-01 (≤1ms), SR-S-01, SR-S-02 (ASIL-D) |
| Tier-2 SW protection (§6.5.1) | MBMS Core 0 ASIL-D → contactor control state machine | SR-P-02 (≤10ms), SR-S-01, SR-S-02 (ASIL-D) |
| Contactor state machine (§6.5.3) | MBMS Core 0 + contactor feedback GPIO | SR-F-05 (contactor control), SR-S-06 (welding detection) |
| DTC fault logging (§6.5.2) | MBMS NVRAM + UDS service $19 | SR-C-03 (OBD-II diagnostics), SN-10 (remote diagnosis) |

---

## 6.7 SE Process Reflection

### How Functional Decomposition Enables This Design (Session 7)

Session 7 covered operational and functional analysis — the process of decomposing system functions into implementable sub-functions. This chapter demonstrates that decomposition at work:

- F1.2 (Measure module temperatures) → decomposed in §6.4.3 into: NTC sample rate (10ms), temperature array data structure, rate-of-rise calculation algorithm, and independence from SOC EKF
- F3.1 (Overcharge protection) → decomposed into three tiers in §6.5.1, each with its own hardware/software element, timing requirement, and independence property

Without functional decomposition, it would be easy to write "protect against overcharge" and then design a single software check — missing the ASIL-D independence requirement entirely.

### How Trade Study Decisions Shape Every Design Choice

The chain from Chapter 5 decisions to Chapter 6 designs is direct and traceable:

| TS Decision | Design Impact | Specific Section |
|---|---|---|
| **LFP selected (TS-1)** | OCV curve is flat → EKF is mandatory, not optional | §6.2.1 Algorithm Selection |
| **LFP selected (TS-1)** | Lower self-discharge variability → passive balancing sufficient | §6.3.1 Balancing Strategy |
| **LFP selected (TS-1)** | Thermal runaway onset at 270°C → rate-of-rise threshold set at 2°C/s with large margin | §6.4.3 Thermal Runaway Detection |
| **Liquid cooling selected (TS-2)** | PID controls coolant pump, not fan → two-loop control architecture | §6.4.1 Control Architecture |
| **Liquid cooling selected (TS-2)** | Coolant flow rate, heat capacity → sizing calculation possible | §6.4.4 Coolant System Sizing |

This demonstrates the principle from Session 5: **design decisions are not independent.** Each trade study decision constrains and informs downstream design choices. Changing a trade study decision requires revisiting all downstream designs — which is exactly why trade studies are locked before design definition begins.

### What Design Elements Require ISO 26262 Part 6 Compliance (Bridge to Ch 7)

ISO 26262 Part 6 governs software-level requirements. ASIL-D software (Core 0 — fault management, contactor control, thermal runaway detection) requires:
- **MC/DC code coverage:** Every branch and condition in safety-critical code must be tested independently
- **No dynamic memory allocation:** malloc() is prohibited in ASIL-D code (unpredictable timing)
- **Formal code review:** Two-person review of all ASIL-D code modules
- **LDRA or equivalent:** Automated static analysis and coverage measurement
- **Traceability:** Every line of ASIL-D code traceable to a functional safety requirement (FSR-XX)

Chapter 7 defines the V&V plan for verifying all of these design properties.

---

*Next: [Chapter 7 — Integration, Verification & Validation Plan](07-ivv-plan.md)*
