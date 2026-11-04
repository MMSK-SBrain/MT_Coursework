# SESSION-18T: EPS, ABS & ADAS Module Awareness
## Theory Session | Day 18 | Module 8: Module-Specific Repair

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 8 — Module-Specific Repair
**Day:** 18 | **Session Type:** Theory
**Duration:** 90 minutes
**CO Alignment:** co-1, co-2

---

## Session Outcomes

| ID | Outcome | Bloom's Level |
|----|---------|---------------|
| so-8-3-1 | Explain EPS module function, torque sensor interface, and common EPS failure modes | Understand |
| so-8-4-1 | Identify common ADAS modules in modern vehicles and their function | Understand |
| so-8-4-2 | Explain why ADAS modules require static and/or dynamic calibration after replacement | Understand |
| so-8-4-3 | Describe what equipment is needed for ADAS calibration and when to refer to specialist | Evaluate |

---

## Timing Overview

| Segment | Content | Duration |
|---------|---------|----------|
| 0:00–0:05 | Hook for EPS — steering pull after column work | 5 min |
| 0:05–0:25 | EPS architecture, torque sensor, and failure modes | 20 min |
| 0:25–0:35 | EPS replacement and post-replacement procedure | 10 min |
| 0:35–0:50 | ABS function, architecture, and failure modes | 15 min |
| 0:50–1:00 | ABS replacement notes and post-replacement steps | 10 min |
| 1:00–1:05 | ADAS framing statement | 5 min |
| 1:05–1:20 | ADAS module types, calibration physics, when to refer | 15 min |
| 1:20–1:30 | CLIMAX, resolution, and lab preview | 10 min |

---

## Story Arc

**HOOK for EPS (Slide 1):**
"A technician replaces an EPS motor column on a 2017 Ford Focus. The power steering works — but the car now pulls left. The steering angle sensor needs to be re-zeroed after any steering work. Without this step, the ADAS lane-keeping system is working from wrong data. This one missed step potentially creates a safety risk."

Pause.

"Today is different from yesterday. Clusters and BCMs are important modules with good repair economics. EPS and ABS are safety-critical systems. When an EPS or ABS fault is left unresolved, or a procedure is skipped after replacement, the consequence is not a customer complaint — it can be a collision. This session establishes what these modules do, how they fail, and what you must do correctly when replacing and coding them. Then we cover ADAS — because every technician in a modern workshop needs to understand it, even if ADAS calibration itself is specialist work."

**Development:** EPS architecture and torque sensor → EPS failure modes and replacement procedure → ABS function and failure modes → ABS replacement notes → ADAS module awareness → Why calibration is mandatory (the physics of mis-calibration) → Tools needed and cost → When to refer.

**CLIMAX (Slide 25):**
"ADAS is coming into every workshop whether we're ready or not. The technician who says 'I replaced the camera and it's fine' without calibration is creating a liability problem and a safety risk. Know when to refer. Know the conversation to have with the customer. That knowledge protects them and you."

**Resolution (Slide 26):** Preview of the hands-on lab where students will diagnose an EPS torque sensor fault using oscilloscope signals, diagnose an ABS fault and categorise it, then code a replacement ABS module and verify with a scan tool.

---

## Slide-by-Slide Content Plan

### SLIDE 1 — Hook: The Missed Step

- Narrative: EPS column replaced on a 2017 Ford Focus; steering pulls left; SAS calibration missed; ADAS lane-keeping working from incorrect reference data
- Instructor note: deliver this with deliberateness; this is not a horror story — it is a professional reality that every technician who works on steering or ADAS-equipped vehicles will encounter
- One image: dashboard showing EPS warning light illuminated — clean, readable, recognisable

---

### SLIDE 2 — Session Map

- Session outcomes: so-8-3-1, so-8-4-1, so-8-4-2, so-8-4-3
- Timing overview as a horizontal bar chart
- "By the end of this session you will be able to diagnose EPS and ABS failures using the correct approach, and you will know exactly when ADAS work requires specialist referral — and why."

---

### SLIDE 3 — EPS System Architecture

**What EPS does:**
Electric Power Steering replaces the hydraulic pump of conventional power steering with an electric motor that provides steering assistance calculated from driver demand, vehicle speed, and steering angle. The result is speed-progressive assistance — heavy at low speed for easy parking, progressively lighter at high speed for responsive highway feel — delivered without a hydraulic pump, improving fuel efficiency and eliminating hydraulic fluid maintenance.

**EPS configurations:**

| Type | Motor Location | Common Applications |
|------|---------------|---------------------|
| Column-assist EPS (C-EPS) | On steering column, above the universal joints | City cars and superminis: Ford Fiesta, Fiat 500, Honda Jazz, Vauxhall Corsa |
| Rack-assist EPS (R-EPS) | On the steering rack body | Mid-size to large cars and SUVs: BMW, Mercedes, Audi, Volvo |
| Pinion-assist EPS (P-EPS) | At the rack pinion directly | Some mid-size and crossover vehicles |

**EPS control unit inputs:**
- Steering torque sensor (STS) — primary demand signal: how much torque the driver is applying and in which direction
- Vehicle speed — received from ABS module via CAN; used to calculate speed-dependent assist reduction
- Steering angle sensor (SAS) — direction and rate of steering input; provides centre-point reference
- Battery voltage — EPS modulates assist downward during low battery conditions to reduce current draw

**EPS control unit output:**
- Current command to the steering motor via a MOSFET H-bridge inside the EPS ECU
- The EPS ECU calculates the required assist torque and drives the motor accordingly
- The motor applies assist torque directly to the column (C-EPS) or to the rack (R-EPS)

**Safety behaviour — fail-safe design:**
EPS is designed to fail safe. When the EPS ECU detects a fault it cannot safely manage, it reduces assist to zero and illuminates the EPS warning light — manual steering remains possible, requiring significantly more effort. A fault that causes the EPS to apply assist in the wrong direction or to apply assist without limit would be a critical failure and must never be returned to service.

---

### SLIDE 4 — The Steering Torque Sensor — Critical Input

**Physical principle:**
- A torsion bar connects the steering column upper shaft to the lower shaft (which connects to the rack pinion)
- When the driver applies force to the steering wheel, the torsion bar twists slightly — the amount of twist is proportional to the applied torque
- Two Hall-effect position sensors measure the angular displacement of the torsion bar twist — from these measurements the EPS ECU determines both the magnitude and direction of the driver's steering input

**Signal characteristics:**
- Two complementary output signals — Signal A and Signal B — both referenced to a 5V supply
- At the centre (no twist, straight ahead): both signals are approximately 2.5V
- When twisted in one direction (e.g., right turn — clockwise): Signal A rises toward 4.5V while Signal B falls toward 0.5V
- When twisted in the opposite direction (left turn): Signal A falls, Signal B rises
- Cross-check: Signal A + Signal B should always sum to approximately 5V regardless of steering position; this sum is constant because the two sensors are on opposite sides of the torsion bar

**The cross-check and its safety purpose:**
If one sensor signal wire is shorted to ground or open circuit, the sum of A + B will deviate from 5V — the EPS ECU detects this deviation immediately and logs a DTC for the affected channel. The system then reduces or removes assist rather than acting on a potentially incorrect demand signal. This is a deliberate safety design, not a coincidence.

**Torque sensor signal summary table:**

| Condition | Signal A | Signal B | Sum | EPS Response |
|-----------|----------|----------|-----|--------------|
| Centre (no torque) | ~2.5V | ~2.5V | ~5V | Normal assist |
| Right turn | ~4.0–4.5V | ~0.5–1.0V | ~5V | Normal assist |
| Left turn | ~0.5–1.0V | ~4.0–4.5V | ~5V | Normal assist |
| Signal A open circuit | 0V or 5V (stuck) | Normal | Not ~5V | DTC; assist removed |
| Signal B open circuit | Normal | 0V or 5V (stuck) | Not ~5V | DTC; assist removed |
| Signal A short to ground | 0V (stuck) | Normal | Below 5V | DTC; assist removed |

**Visual for slide:** Oscilloscope capture showing Signal A and Signal B as complementary waveforms during a left–centre–right steering sequence; both traces visible on same screen; sum visually constant.

---

### SLIDE 5 — EPS Architecture: Internal Block Diagram

Visual: EPS ECU signal-flow block diagram

```
[Torque Sensor A + B]  ──→┐
[Steering Angle Sensor] ──→│  EPS ECU
[Vehicle Speed — CAN]   ──→│  ┌─────────────────────────────────────┐
[Battery Voltage]        ──→│  │ MCU (calculates assist demand)      │──→ [MOSFET H-Bridge]──→ [EPS Motor]
                            │  │ Torque sensor input conditioning    │
                            └──│ SAS input processing                │
                               │ CAN transceiver (speed input)       │
                               │ Power stage protection and          │
                               │ motor current sensing feedback      │
                               └─────────────────────────────────────┘
```

Key: the feedback from the motor current sensor allows the EPS ECU to confirm the motor is producing the commanded torque. If current is commanded but not produced (open MOSFET) → immediate DTC. If current is produced but direction is wrong (shorted MOSFET) → immediate protection and shutdown.

---

### SLIDE 6 — EPS: Common Failure Modes

**Failure Mode 1 — Power stage MOSFET failure:**
- The EPS ECU drives the steering motor via a MOSFET H-bridge — typically 4 or 8 MOSFETs arranged to control motor current bidirectionally
- If one or more MOSFETs fail open: the motor either does not respond at all, or responds weakly in one direction only
- If one or more MOSFETs fail shorted: the H-bridge short-circuits → immediate large current → ECU protection shuts down → EPS warning light; may also damage the motor winding if the short is sustained
- Symptom: EPS warning light on; DTC for motor circuit fault (short circuit, open circuit, or overcurrent); reduced or absent steering assist
- Diagnosis: scope motor drive signals at EPS ECU connector; if MCU is commanding drive but motor current is absent or asymmetric → power stage failure confirmed; test the motor winding resistance first (shorted winding = near zero resistance — a shorted motor destroys new MOSFETs immediately)
- Repair: component-level — identify the failed MOSFET on the power stage PCB (large power packages — D2PAK or TO-263 typically); test in-circuit; replace with correct part; always confirm motor is not the root cause before replacing power stage components

**Failure Mode 2 — Torque sensor fault:**
- One or both sensor signal wires may be: open circuit from a broken wire at the column flex point; shorted to ground from wiring damage; or the Hall-effect sensor element itself may have failed internally
- Symptom: EPS warning light; DTC for torque sensor channel A or B; assist may be reduced or removed; in some vehicles steering feels heavy in one direction only if the system attempts partial operation on one channel
- Diagnosis: measure Signal A and Signal B voltage at the STS connector with ignition on; rotate steering wheel slowly by hand while measuring; a healthy channel follows the expected complementary pattern; a failed channel is stuck (static voltage) or absent; calculate A + B — deviation from ~5V confirms fault location
- Scope both signals simultaneously: the stuck channel is immediately obvious against the functioning complementary channel

**Failure Mode 3 — SAS coding loss or calibration drift:**
- After a battery disconnect, some EPS modules lose their steering angle calibration — the zero-point reference for straight-ahead position
- After any steering geometry work (wheel alignment, steering column replacement, track rod adjustment), the SAS zero-point must be re-established
- Symptom: EPS warning light after battery work or steering work; assist is available but may feel asymmetric; some vehicles will not allow lane-keeping assist to activate with an uncalibrated SAS
- This is not a hardware fault — it requires a recalibration procedure via scan tool (SAS calibration, also called SAS zero-point calibration or SAS reset)
- Procedure: drive straight ahead at low speed; centre the steering wheel; execute the SAS calibration function in the diagnostic software; many platforms complete this automatically on the first drive cycle after the procedure is initiated

**Failure Mode 4 — CAN communication loss:**
- The EPS ECU receives vehicle speed from the ABS module via CAN to calculate speed-dependent assist reduction
- If the CAN bus has a fault or the ABS module goes offline, the EPS ECU loses the speed reference
- Symptom: EPS defaults to its default assist map — this may be the low-speed (full assist) map; at highway speeds the steering may feel too light; EPS warning light may or may not illuminate depending on the platform
- Diagnosis: check CAN bus for ABS communication; confirm ABS module is online; check for CAN fault DTCs in the EPS module referencing a lost message from ABS

---

### SLIDE 7 — EPS: Post-Replacement Procedure

**Steps that cannot be skipped after replacing an EPS ECU:**

Step 1 — Variant coding:
Code the replacement EPS ECU to the vehicle using the scan tool. Most EPS ECUs require coding to accept the vehicle platform, steering ratio, and assist map profile. An uncoded EPS ECU may refuse to provide any assist or may provide incorrect assist levels.

Step 2 — Steering angle sensor calibration:
Perform SAS zero-point calibration procedure via scan tool. The replacement EPS ECU has no knowledge of the steering wheel's centre position. Until calibrated, the ECU cannot accurately calculate speed-dependent assist or provide correct reference data to lane-keeping systems. This is the step from the hook scenario — the step that is most commonly missed.

Step 3 — Confirm EPS warning light extinguished and no DTCs remain:
Read DTCs; clear; read again to confirm no stored faults; EPS warning light off.

Step 4 — Road test:
Confirm assist is symmetrical (equal effort to turn left and right), no vibration through the steering wheel at any road speed, no unexpected assist events, EPS warning light remains off during and after the road test.

**Instructor note:** The SAS calibration after steering work is the single step most commonly missed by technicians unfamiliar with EPS systems. It is also responsible for the most callbacks and the most customer complaints in this module type. Emphasise it specifically — it takes less than 5 minutes with the correct scan tool but is the exact source of the hook scenario described at session start.

---

### SLIDE 8 — ABS System Architecture

**What ABS does:**
The Anti-Lock Braking System prevents wheel lock-up during hard braking by modulating brake pressure per wheel. When a wheel begins to lock (wheel speed drops suddenly to near zero while the vehicle is still moving), the ABS ECU releases brake pressure to that wheel, allowing it to rotate again, then re-applies — this cycle repeats at approximately 10–15 times per second. The driver maintains steering control during maximum braking and stopping distances on low-friction surfaces are typically reduced.

Modern ABS systems also incorporate: ESP/ESC (electronic stability control), EBD (electronic brake force distribution), HBA (hydraulic brake assist), and HHC (hill hold control) — all managed by the same ECU.

**Physical architecture — two-component system:**

| Component | What It Contains | Replaceability |
|-----------|-----------------|----------------|
| Hydraulic Control Unit (HCU) | Solenoid valves (inlet/outlet per wheel), pump motor, accumulator | Requires brake line disconnection; must bleed brake system after replacement |
| ABS Electronic Control Unit | MCU, wheel speed sensor inputs, solenoid valve MOSFET drivers, pump motor relay | Can be unbolted from HCU body and replaced without disturbing brake lines — no brake bleed required |

**The HCU vs ECU distinction is critical:** HCU replacement involves opening the brake system (brake bleed required); ECU replacement alone does not touch the hydraulic system (no bleed required). Many technicians and customers confuse these. Be explicit about which component is being replaced and what the hydraulic implications are.

**ABS ECU inputs:**
- Four wheel speed sensors — one per wheel (active Hall-effect or passive variable reluctance)
- Brake pressure sensor — on ESP-equipped vehicles
- Yaw rate sensor and lateral acceleration sensor — on ESP systems
- Battery voltage, ignition status, brake lamp switch

**ABS ECU outputs:**
- Individual solenoid valve control: inlet valve and outlet valve for each of the four brake circuits (8 valves total on a 4-channel system)
- Pump motor relay or direct drive signal
- ABS and ESP warning lamp outputs

---

### SLIDE 9 — Wheel Speed Sensors: The Most Common ABS Fault Source

The majority of ABS warning light presentations in workshop practice are wheel speed sensor faults — not ABS ECU internal failures. Understanding wheel speed sensors is the most efficient investment in ABS diagnostic skill.

**Two sensor technologies:**

| Type | Output Signal | Identification | Testing Method |
|------|--------------|----------------|----------------|
| Passive — Variable Reluctance (VR) | AC sine wave; amplitude and frequency increase with speed; no supply voltage required | Two wires; resistance typically 800Ω–2kΩ | Resistance check (in range = winding OK); oscilloscope AC voltage probe while wheel rotating slowly |
| Active — Hall-effect | Digital square wave (0V / supply voltage); constant amplitude at all speeds; requires supply voltage | Three wires (supply, ground, signal); supply typically 12V | Confirm supply voltage present; oscilloscope signal wire while wheel rotating — should toggle cleanly between 0V and supply voltage |

**Common wheel speed sensor fault conditions:**

| Fault | Most Likely Cause | Diagnosis Approach |
|-------|------------------|--------------------|
| Signal absent at ABS ECU connector | Broken wire in flex harness near the wheel; most common at the bend point near the wheel bearing | Continuity test or oscilloscope at ECU connector; no signal despite wheel rotating |
| Erratic or noisy signal | Dirty sensor face; damaged or corroded tone ring; debris packed in teeth | Inspect sensor and tone ring visually; clean; measure air gap |
| Low-amplitude signal (VR type) | Air gap too large after wheel bearing replacement; sensor not fully seated | Measure air gap with feeler gauge (specification typically 0.5–2mm); re-seat sensor |
| No signal — active sensor | Supply voltage absent (fuse, wiring fault); or sensor internal failure | Measure supply voltage at sensor connector first; if supply is correct and signal is absent = sensor failed |

**The most important diagnostic discipline for ABS:** Read the DTC description completely — the DTC identifies which wheel position is reporting a fault. Always diagnose the specific wheel identified before drawing any conclusion about the ABS ECU. Two out of three ABS warning lights in workshop practice are resolved at the wheel speed sensor, wiring, or tone ring — not the ECU.

---

### SLIDE 10 — ABS: ECU Internal Failure Modes

When the wheel speed sensor and associated wiring have been confirmed good on the affected channel, and the fault persists, suspect the ABS ECU:

**Failure Mode 1 — Solenoid valve driver failure:**
- The ABS ECU contains individual MOSFET drivers for each solenoid valve in the HCU (typically 8 valves — one inlet and one outlet per wheel)
- A failed driver generates a DTC for a specific valve channel: e.g., "Inlet solenoid valve — left front: open circuit" or "outlet solenoid valve — right rear: short to ground"
- Diagnosis: disconnect the ECU connector and test the solenoid valve coil resistance at the HCU side of the connector — if the solenoid coil is within specification (typically 4–8Ω), the problem is the driver inside the ECU, not the solenoid itself
- Repair: component-level repair on the ABS ECU PCB — identify the MOSFET driver for the failed valve channel; test in-circuit; replace

**Failure Mode 2 — Pump motor relay or driver failure:**
- ABS pump motor circuit fault DTC; pump motor does not prime during ABS activation or ABS ECU self-test
- Test: measure pump motor resistance at HCU connector (typical: 0.5–2Ω for a healthy motor); if motor resistance is in specification, the ECU driver has failed

**Failure Mode 3 — Power supply or ground fault:**
- ABS ECU has its own dedicated fused supply (typically 30A or 40A fuse) and a dedicated ground point
- If the supply fuse is blown or the ground strap has corroded: ABS ECU loses power → no communication → multiple U-codes generated across other modules
- Symptom: ABS and ESP warning lights on; scan tool shows no communication with ABS module; other modules log U0121 (Lost Communication With ABS Control Module) or equivalent
- Diagnosis: always check the ABS ECU power supply fuse and ground continuity at the ECU connector before removing or replacing the ECU; this fault is significantly more common than ECU internal failure and the repair cost is trivial

**Failure Mode 4 — Internal memory fault or communication loss after power event:**
- ECU internal memory corruption after a sustained power surge (e.g., jump-starting with reversed polarity), or water ingress causing short circuits on the ECU PCB
- ECU communicates intermittently or not at all after ruling out power supply and wiring faults
- If supply voltage, ground continuity, and CAN bus wiring are all confirmed good and the ABS ECU still does not communicate → the ECU itself has failed internally

---

### SLIDE 11 — ABS: Post-Replacement Steps

**Steps required after replacing the ABS ECU (ECU only — HCU not disturbed):**

Step 1 — Code the replacement ECU to the vehicle:
Most modern ABS ECUs require variant coding — the ECU must be told the vehicle's tyre size, market variant, and option configuration. Plug-and-play ABS replacement without coding is the exception on vehicles built from approximately 2005 onwards.

Step 2 — Adaptation channels:
Some platforms require individual adaptation values to be set — tyre circumference (used for vehicle speed calculation and ABS activation threshold), axle load distribution, or specific country/market compliance settings. These parameters are safety-relevant — incorrect tyre circumference affects ABS activation sensitivity.

Step 3 — Brake bleed procedure:
Only required if the HCU was disturbed. If only the ECU was replaced by unbolting it from the HCU body with brake lines undisturbed, no bleed is needed — brake fluid was never opened. This is the most common misunderstanding about ABS ECU replacement.

Step 4 — Wheel speed sensor air gap check:
Required if any wheel bearing or wheel knuckle work was performed as part of the same job.

Step 5 — Road test and DTC check:
ABS self-tests when vehicle speed exceeds approximately 15–20 km/h. Drive at low speed in a safe area. Confirm ABS warning light extinguishes and no new DTCs are generated. If warning light returns → read new DTCs and diagnose.

---

### SLIDE 12 — ABS Diagnostic Discipline: Four-Step Summary

Step 1: Read DTCs fully — note the specific channel and fault type (sensor signal absent? valve driver? communication?)

Step 2: Verify power supply and ground at the ABS ECU connector before any other work; power and ground faults are common and easily corrected

Step 3: Test the externally-connected component at the connector — wheel speed sensor signal at the ABS ECU connector; solenoid valve resistance at the HCU connector; if the external component is at fault, the ABS ECU is not

Step 4: Only after externally-connected components and power supply are confirmed good — suspect the ABS ECU itself

**The diagnostic principle:** "The ABS warning light does not mean replace the ABS ECU. It means diagnose the ABS system."

---

## ADAS Module Awareness Section

### SLIDE 13 — ADAS: Framing Statement

**Instructor delivers this framing verbatim or very close before the ADAS content:**

"This section is not teaching you to perform ADAS calibration. It is teaching you that ADAS modules exist, what they do, what they require after being disturbed, and — most importantly — when you must stop and refer the job to someone with the right equipment.

As vehicles built from approximately 2018 onwards become the majority of workshop traffic over the next few years, you will encounter these systems routinely. A technician who does not know what a front radar ECU is, or does not know that windscreen replacement now requires camera calibration in most cases, is a technician who will cause harm unintentionally.

Knowing what you don't know is a professional skill. This section gives you that knowledge."

Note for instructor: this section is awareness-only. Students learn to recognise ADAS modules, understand why calibration is mandatory, and know when to refer. This is not a calibration certification session.

---

### SLIDE 14 — What ADAS Modules Are

**ADAS — Advanced Driver Assistance Systems:**
A family of systems that use sensors to monitor the vehicle's environment and either warn the driver of hazards or intervene autonomously to avoid or mitigate a collision.

**The major ADAS sensor types and their control modules:**

| Module | Sensor Technology | Physical Location | Primary Functions |
|--------|------------------|------------------|-------------------|
| Forward-facing camera ECU | Monocular or stereo camera; 60–120° field of view | Inside vehicle at windscreen top; rear-view mirror bracket or A-pillar mount | Lane departure warning, forward collision warning, AEB (camera-based), lane-keeping assist, traffic sign recognition, high-beam assist |
| Front radar ECU | 77 GHz millimetre-wave radar | Behind front bumper fascia; front grille centre | Adaptive cruise control, AEB (radar-based), forward collision mitigation |
| Rear/corner radar | 77 GHz millimetre-wave radar | Behind rear bumper corners | Blind spot monitoring, rear cross-traffic alert, rear pre-collision warning |
| Ultrasonic park assist ECU | Ultrasonic transducers | ECU in boot or rear quarter; sensors embedded in bumper | Parking distance display, parking steering assist, low-speed manoeuvre guide |
| Surround view system | 4 wide-angle cameras | Front grille, both door mirrors, rear | 360° top-down view for parking; individual cameras replaceable |

**Vehicle coverage:** From approximately 2016–2018 onwards, most new vehicles sold in Europe incorporate at least forward-facing camera ADAS as standard or near-universal option. From 2022, Euro NCAP and EU type-approval require AEB and lane-keeping systems as mandatory on new models. These vehicles are already in workshops and their numbers will grow every year.

---

### SLIDE 15 — Why ADAS Calibration Is Mandatory

**The fundamental physical problem:**

ADAS sensors — whether camera or radar — determine where objects are in the real world by calculating angles relative to the sensor's known mounting position and orientation. The sensor's internal calibration assumes it is installed at a precise angle that matches the manufacturer's specification. If the sensor is mounted even a fraction of a degree away from that specification, every calculation it makes is based on a wrong reference angle — and the error compounds with distance.

**Camera calibration — angle error and real-world consequence:**

Consider a front camera mounted at the windscreen top, calibrated for a known horizontal mounting angle. If the camera's actual angle is off by only 0.5° from the calibrated position:

| Distance from Vehicle | Lateral Position Error |
|----------------------|----------------------|
| 10 metres | ~0.09 metres (9 cm) — barely perceptible |
| 50 metres | ~0.44 metres — nearly half a standard lane width |
| 100 metres | ~0.87 metres — approaching one full lane width |

At motorway speeds of 120 km/h, 100 metres represents approximately 3 seconds of reaction time. An 0.87-metre lateral error at that range means the AEB system may not detect a stationary vehicle until it is nearly in the direct collision path, or may detect a vehicle in the adjacent lane as a threat and trigger an emergency brake activation in clear road conditions.

**Radar calibration — angle error and consequence:**

A 77 GHz radar ECU is aimed forward within a defined cone (typically ±5° to ±10° horizontal). A 1° horizontal error in the radar's aim translates to approximately 1.75 metres of lateral position offset at 100 metres range. The consequences:
- False AEB activation: radar detects a vehicle in an adjacent lane as being in the ego vehicle's lane → unexpected emergency braking → the vehicle following at motorway speed has insufficient distance to stop → rear-end collision
- AEB failure: a vehicle stopped ahead is detected as being in the adjacent lane by the offset radar → AEB does not activate → the driver has relied on AEB as a secondary safety layer → rear-end collision

**Key point for students:** "It looks fine" is not a substitute for calibration. Camera and radar mis-calibration of the scale that causes these failures is completely invisible to visual inspection and may produce no DTCs. The system appears to function — but it functions incorrectly.

---

### SLIDE 16 — ADAS Calibration: Static and Dynamic

**Static calibration:**
- Vehicle is positioned stationary on a level, flat surface in a calibration bay with clear space in front
- Calibration targets (printed patterns, reflective boards, or active LED arrays) are positioned at precisely specified distances and angles in front of and/or around the vehicle — tolerances are typically within ±10mm at several metres distance
- The diagnostic tool connects to the camera or radar ECU and initiates the calibration routine; the sensor aligns itself to the target geometry and writes new calibration coefficients to its non-volatile memory
- Setup requirements: flat, level floor (gradient tolerance typically within 0.5°), minimum 4–6 metres of clear space in front of vehicle, manufacturer-specific or universal ADAS calibration targets, ADAS-capable diagnostic tool

**Dynamic calibration:**
- Used by some camera systems (some systems require dynamic calibration following static, some use only dynamic)
- Vehicle is driven at a specified minimum speed (typically 40–80 km/h) on a road with clearly marked lane lines while the ADAS tool captures data
- The camera performs self-calibration by comparing its output against the expected appearance of lane markings
- Limitations: requires suitable road conditions; not always achievable in an urban workshop environment

**Calibration equipment cost:**
- Basic static calibration targets with a universal ADAS tool: approximately £2,000–£5,000 for a minimum viable setup
- Full professional ADAS calibration rig (supporting multiple manufacturers, with precision mounting hardware): £8,000–£15,000 or higher
- Manufacturer-specific calibration kits (BMW, Mercedes-Benz, Volvo own-brand equipment): often required for dealer-level work; cost varies
- Common tools: Autel ADAS (MaxiSys ADAS), Bosch DAS 3000, Hella gutmann, manufacturer-specific dealer tools

---

### SLIDE 17 — When to Refer Out: The Definitive List

**Always refer for ADAS calibration after any of the following:**

| Trigger Event | Reason Calibration Is Required |
|--------------|-------------------------------|
| Replacement of front camera ECU or assembly | New unit has no calibration data — must be calibrated from zero; cannot self-calibrate |
| Windscreen replacement or removal | Camera mount bracket moves with the glass — even re-clipping the camera in the same physical position does not restore calibration; the glass itself has moved |
| Front bumper removal or replacement | Front radar is mounted behind the bumper — bumper fit tolerances can shift the radar aim |
| Front subframe removal or replacement | Changes the vehicle's structural reference geometry |
| Wheel alignment adjustment (where manufacturer flags ADAS check) | Steering geometry adjustment changes the vehicle's forward travel vector relative to the sensor's assumed reference |
| Front-end collision repair involving structural work | Both radar and camera mounting geometry may be disturbed |
| Any impact to A-pillar or bonnet/hood | Camera mount reference structure may be deformed |
| Surround view camera replacement | Individual camera position must be calibrated relative to the known vehicle geometry |

**Referral not required for:**
- Parking sensor ultrasonic ECU or sensor replacement — ultrasonic systems use time-of-flight, not angle-sensitive beam geometry; they do not require optical or RF calibration
- ABS ECU replacement (no ADAS sensor mounting affected)
- BCM or instrument cluster replacement (no ADAS systems affected)
- EPS ECU replacement — SAS calibration is required (scan tool procedure, 5 minutes) but this is not ADAS calibration; it is an EPS system procedure

**How to refer correctly:**
1. Contact an ADAS calibration specialist or a manufacturer dealer with appropriate ADAS calibration equipment
2. Document in writing: what work was performed; which sensor, camera, or radar was affected or potentially disturbed
3. Advise the customer explicitly: "The ADAS system on this vehicle must not be relied upon for its normal functions until calibration is confirmed complete — specifically, do not use adaptive cruise control or automatic emergency braking until the calibration is done"
4. Do not return the vehicle to the customer with ADAS functional assumptions if calibration has not been confirmed

---

### SLIDE 18 — ADAS: Real Scenarios and Consequences

**Scenario 1 — False AEB activation:**
A vehicle has its windscreen replaced at a glass specialist. The camera is re-clipped to the windscreen bracket. The glass specialist says "the camera is back in position — it's fine." No calibration is performed. Three days later, on a clear motorway, the vehicle brakes unexpectedly with no obstacle present. The vehicle behind rear-ends it. Investigation finds the camera was 0.7° off-angle after the windscreen replacement — the AEB system was detecting the barrier on an upcoming curve as being in the vehicle's direct path.

**Scenario 2 — AEB failure:**
A vehicle has front-end collision damage repaired. The body shop replaces the front bumper. The radar behind the bumper is not recalibrated. The radar is now aimed approximately 1.5° to the left. No DTC is generated — the radar appears functional. A month later the customer is involved in a rear-end collision with a stationary vehicle. The radar had detected the stationary vehicle as being in the adjacent lane and AEB had not activated. The driver had mentioned several times to their family that their "system seemed to not warn as quickly as before" — they had noticed the change, but the vehicle had given no indication.

**Instructor note:** These scenarios are based on the type of events that have occurred and been investigated in real post-accident analysis. Use them to make the content concrete and urgent without being alarmist. The message is: calibration is not optional maintenance — it is a required functional step that directly affects safety outcomes.

---

### SLIDE 19 — ADAS Summary and Three Professional Rules

**Three rules for every technician to operate by:**

**Rule 1 — Know what you're touching:**
Before starting any job, identify whether the vehicle has ADAS systems (make, model, year, option level). If it does, identify which sensors are in the area of the work being carried out.

**Rule 2 — Know the trigger list:**
Any work that appears on the referral trigger list requires ADAS calibration. No exceptions. "It looked fine" and "I only removed the bumper for 5 minutes" are not acceptable professional positions.

**Rule 3 — Communicate clearly and early:**
Tell the customer before the job starts: "This vehicle has ADAS systems. The work you've asked for will require ADAS calibration afterward. Calibration costs approximately £X and must be done at an equipped workshop. I will arrange this as part of the job." Do not present calibration as a surprise cost after the job is complete.

---

### SLIDE 20 — Module Failure Pattern Summary: Days 17 and 18

**Building the module mental map:**

| Module | Top Failure Modes | First Diagnosis Test |
|--------|------------------|--------------------|
| Instrument Cluster | Pixel row loss; backlight failure; stepper motor fault | Oscilloscope on display driver IC output pins |
| BCM | MOSFET output failure; EEPROM corruption; water damage | Scan tool live data; visual inspection of PCB |
| EPS | Torque sensor fault; power stage MOSFET failure; SAS calibration loss | Scope Signal A and B at STS connector; calculate sum |
| ABS | Wheel speed sensor fault; solenoid valve driver failure; supply fault | Read DTC; verify WSS signal at ABS ECU connector |
| ADAS | Not a repair scope — calibration required after disturbance | Identify trigger event; refer with written documentation |

---

### SLIDE 21 — Connecting to Earlier Modules

| Today's Topic | Skills and Knowledge from Earlier Modules |
|--------------|-------------------------------------------|
| EPS torque sensor oscilloscope diagnosis | Module 3: sensor signals; Module 6: bench setup and oscilloscope technique |
| EPS power stage MOSFET diagnosis | Module 5: power stage testing; MOSFET failure modes |
| ABS wheel speed sensor signal testing | Module 3: sensor signals — passive and active sensor types |
| ABS solenoid valve driver testing | Module 5: power stage component testing methodology |
| ABS variant coding after replacement | Module 6/7: scan tool coding procedures |
| ADAS referral decision | Professional judgment and scope-of-work decisions — established throughout the course |

---

### SLIDE 22 — Instructor Checkpoint Questions

**After EPS section — ask the group:**
- "Tell me the two signals the torque sensor produces and what happens to each when you turn left." (Expected: Signal A falls toward 0.5–1V; Signal B rises toward 4–4.5V; sum remains approximately 5V)
- "EPS is showing no assist and a DTC for motor circuit. Before you replace the power stage MOSFETs, what do you check and why?" (Expected: test the motor winding resistance first — a shorted motor winding will destroy new MOSFETs immediately; confirm the root cause before replacing components)
- "What is the one step after EPS module replacement that is most often missed?" (Expected: SAS calibration — steering angle sensor zero-point calibration)

**After ABS section — ask the group:**
- "The scan tool shows a wheel speed sensor fault on the right front. Give me three possible causes that are not the ABS ECU." (Expected: any three of: broken wire in harness near wheel bearing, damaged or corroded tone ring, sensor face dirty or physically damaged, air gap too large after bearing replacement, active sensor supply voltage absent)
- "You have replaced the ABS ECU and bolted it onto the original HCU. The brake lines were not touched. Does the customer need a brake bleed?" (Expected: no — a bleed is only required when the hydraulic unit and brake lines are opened; the ECU alone is not in the fluid circuit)

**After ADAS section — ask the group:**
- "A customer brings in a car after windscreen replacement. The workshop that did the glass said the camera 'looks fine and is clipped back in exactly the same position.' What do you tell the customer?" (Expected: calibration must be performed regardless — the camera's position after windscreen replacement is not the same as the factory-calibrated position, even if it appears correct visually; calibration is required by the manufacturer for any windscreen work on ADAS-equipped vehicles)
- "What is the specific risk to other road users if a forward AEB camera is 0.5° off-angle and the vehicle brakes unexpectedly?" (Expected: the vehicle following at motorway speed has insufficient distance to stop → rear-end collision; this also creates a hazard for other lanes if the braking is unexpected in a traffic flow)

---

### SLIDE 23 — Assessment Alignment

| Session Outcome | Assessment Item | Assessment Type |
|----------------|----------------|----------------|
| so-8-3-1 | Explain EPS torque sensor signal characteristics; identify fault condition from signal values table | Written — short answer; Module 8 assessment |
| so-8-3-1 | Oral Q&A at lecture checkpoints | Formative — in-session |
| so-8-4-1 | Identify ADAS sensor type from description or photograph | Written — multiple choice; Module 8 assessment |
| so-8-4-2 | Explain why calibration is required after windscreen replacement; describe the angle-error consequence at 50 metres | Written — explanation question; Module 8 assessment |
| so-8-4-3 | Given a list of 8 repair scenarios, identify which require ADAS calibration referral and which do not | Written — applied exercise; Module 8 assessment |

---

### SLIDE 24 — CLIMAX

**Say this clearly and with conviction:**

"ADAS is coming into every workshop whether we're ready or not. The technician who says 'I replaced the camera and it's fine' without calibration is creating a liability problem and a safety risk. Know when to refer. Know the conversation to have with the customer. That knowledge protects them and you."

---

### SLIDE 25 — Lab Preview: Session 18H

**Station A — EPS Fault Diagnosis:**
- EPS module on bench harness with torque sensor simulator connected
- Read DTCs from EPS module via scan tool; note all codes
- Capture healthy torque sensor Signal A and Signal B on oscilloscope — establish baseline waveform
- Fault injection: instructor sets one of four fault conditions on the simulator without revealing which
- Diagnose: identify which channel is at fault, what type of fault, using DTC plus live data plus oscilloscope evidence
- State diagnosis with evidence before instructor reveals fault condition

**Station B — ABS Fault Categorisation and Module Coding:**
- Three scenario cards in use across the class — each group receives one scenario
- ABS module on bench harness with wheel speed sensor simulator
- Diagnose: categorise fault as hydraulic unit issue / ABS ECU electronics fault / wheel speed sensor fault
- Code replacement ABS module using scan tool per coding specification card
- Verify: confirm coding retained after power cycle, no new DTCs, correct ABS communication established

---

### SLIDE 26 — Summary and Wrap

"EPS and ABS are within your diagnostic and repair capability. They have predictable failure patterns, testable signals, and established coding procedures. Know the failure map, test in the right order, always check power and ground before condemning the ECU, and never skip the post-replacement coding and calibration steps.

ADAS is specialist territory for calibration — but it is your territory for triage. Identify what was touched, determine whether calibration is required using the trigger list, refer with written documentation, and communicate clearly with the customer before the job, not after.

In the lab in ten minutes: you diagnose an EPS torque sensor fault with oscilloscope evidence. You categorise an ABS fault from scenario data. You code a replacement ABS module and verify it. The same diagnostic discipline from today — power and supply first, external components second, ECU last — applies directly to both stations. See you there."

---

## Instructor Notes

**Delivery gravity for EPS section:**
The hook scenario should set the tone for the entire session. EPS and ABS are not body electronics — they affect vehicle control. Deliver the failure mode content with professional seriousness: "here is what goes wrong; here is exactly how to diagnose it; here is exactly what you do after replacement." Methodical, not alarming.

**Delivery gravity for ADAS section:**
The ADAS section must be delivered with calm authority. Students who work in general workshops may push back with "most people don't bother" — the response is: the vehicles are there, the legal exposure is real, and the road safety consequences are documented. Do not get into debate. Deliver the content as professional standard, not as optional awareness.

**Physical specimens for demonstration:**
- EPS ECU: show the physical unit; point to the torque sensor connector; and ideally point to the power stage area on the PCB (large MOSFETs along one edge)
- ABS module: show the ECU unbolted from a hydraulic unit — demonstrate physically that the ECU lifts away cleanly; students often assume removing the ECU means draining the brakes
- Wheel speed sensors: pass around one passive (VR) and one active (Hall-effect) — the difference in connector, cable count, and mounting is immediately apparent
- ADAS front camera: if available, show a real front camera module — students are often surprised at how small and delicate it is relative to the safety function it performs

**Time management:**
- EPS section tends to generate good discussion — build in time for questions after the torque sensor slide
- ADAS section: if behind schedule, the real scenarios (Slide 18) can be summarised verbally in 2 minutes; the trigger list (Slide 17) and three professional rules (Slide 19) are not compressible
- The CLIMAX (Slide 24) is essential — do not cut it

---

## Equipment and Resources Referenced

| Item | Purpose | Source |
|------|---------|--------|
| EPS ECU specimen (real unit, any platform) | Show physical layout of torque sensor connector and power stage area | Lab stock or sourced unit |
| ABS ECU + hydraulic unit specimen (separate) | Demonstrate ECU unbolts from HCU; show solenoid valve connectors on HCU body | Lab stock |
| Wheel speed sensor specimens (VR and Hall-effect) | Students handle and compare; explain signal difference | Lab stock |
| ADAS front camera specimen | Show scale and mounting configuration | Lab stock or sourced unit |
| Oscilloscope | Demonstrate torque sensor signal during theory session if time permits | Lab bench |
| Slide deck with real vehicle photographs | EPS column assembly, ABS HCU+ECU separation, ADAS sensor locations | Prepared slides |
| Torque sensor oscilloscope screenshot — healthy vs failed | Healthy signal (complementary) vs failed signal (one channel stuck) | Prepared screenshots |
| ADAS calibration rig photograph | Students need a visual reference for equipment scale and cost | Manufacturer or third-party rig photograph |

---

## Cross-References

- Module 3, Sessions 5T/5H: sensor signals — passive and active sensor testing methods; applied to WSS diagnosis today
- Module 5, Sessions 9T/9H: power stage testing — MOSFET failure modes; applied to EPS power stage and ABS solenoid driver diagnosis
- Module 6, Sessions 10T/10H: bench setup and powering ECUs off-vehicle; applied to EPS and ABS bench diagnosis
- Module 7, Sessions 15T/15H: CAN bus diagnostics — applied to ABS and EPS CAN communication fault diagnosis
- Module 8, Sessions 17T/17H: module-specific repair approach for instrument clusters and BCM — same framework applied to EPS and ABS today
- Module 8, Sessions 18T/18H: lab session immediately follows — all theory covered here is directly applied in the hands-on activity

---

*Module 8 | Day 18 Theory | ECUHR | v1.0 | 2026-02-18*
