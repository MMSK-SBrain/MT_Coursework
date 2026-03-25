# SESSION-18H: EPS & ABS Module Repair Lab
## Hands-On Session | Day 18 | Module 8: Module-Specific Repair

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 8 — Module-Specific Repair
**Day:** 18 | **Session Type:** Hands-On Workshop
**Duration:** 90 minutes
**CO Alignment:** co-1, co-2

---

## Session Outcomes

| ID | Outcome | Bloom's Level |
|----|---------|---------------|
| so-8-3-2 | Diagnose an EPS fault by scanning DTCs, testing the torque sensor signal, and identifying the faulty stage | Analyze |
| so-8-3-3 | Diagnose an ABS module fault — identify whether fault is in hydraulic unit, control electronics, or wheel speed sensor interface | Analyze |
| so-8-3-4 | Perform coding and adaptation for a replacement ABS module and verify with scan tool | Apply |

**Prerequisite:** SESSION-18T must be completed before entering this workshop.

---

## Workshop Overview

Two parallel stations run simultaneously. Groups of 2 students rotate through both stations within the session.

| Time Block | Group A | Group B |
|-----------|---------|---------|
| 0:00–0:05 | Joint safety briefing — all students together | |
| 0:05–0:47 | Station A — EPS Fault Diagnosis | Station B — ABS Fault Categorisation and Module Coding |
| 0:47–0:50 | Rotation and station handover | |
| 0:50–1:25 | Station B — ABS Fault Categorisation and Module Coding | Station A — EPS Fault Diagnosis |
| 1:25–1:35 | Joint debrief and check-off card completion | |

The instructor circulates between stations with a priority weighting toward Station B during the ABS coding phase — coding errors on an ABS module have safety implications that warrant closer instructor oversight. Where class size permits, appoint one student per station as station lead to manage procedure flow and flag checkpoints.

---

## Pre-Session Instructor Setup

### Station A — EPS (prepare before session)

- [ ] EPS ECU or column unit mounted on bench harness; all connectors labelled
- [ ] Torque sensor simulator connected to torque sensor input on bench harness
- [ ] Simulator confirmed in "Healthy" position before session starts
- [ ] Bench supply set to 12.0V; current limit 10A (EPS motor draw can be significant at power-on)
- [ ] OBD2 interface connected to CAN-H and CAN-L on bench harness; scan tool laptop on bench
- [ ] Oscilloscope with two probes on bench; both probes at bench supply ground reference
- [ ] Reference waveform card printed — shows healthy Signal A + B capture; also shows expected outputs for each fault condition (cards are anonymous — no fault label visible until reveal)
- [ ] EPS torque sensor signal reference card on bench (shows normal signal voltages, fault conditions, sum calculation)
- [ ] Planted fault conditions available on simulator — instructor confirms all four fault positions work before session
- [ ] Student job sheet at station: one per student

### Station B — ABS (prepare before session)

- [ ] ABS module on bench harness with all connectors labelled; wheel speed sensor simulator connected on all four channels
- [ ] Hydraulic unit specimen on bench (without ECU bolted on) with solenoid valve test connector available
- [ ] Replacement ABS ECU (known-good, uncoded or differently coded) available
- [ ] Bench supply set to 12.0V; current limit 5A
- [ ] OBD2 interface connected to ABS module CAN harness; scan tool laptop on bench with ABS coding capability confirmed working
- [ ] Three scenario cards prepared and laminated (one per group; assign before session so all three are covered across cohort)
- [ ] Coding specification card prepared — specifies the variant coding values and any adaptation channels to set for the replacement ABS ECU
- [ ] LED indicators installed on solenoid output pins in bench harness (at least the affected channel for Scenario B-3) — without these, the output test for solenoid driver fault cannot be observed
- [ ] Pre-fault for Scenario B-3: DTC for solenoid driver fault pre-loaded in ABS ECU before session (instructor activates by commanding output test against open circuit, stores DTC, then reconnects)
- [ ] ABS fault categorisation worksheet printed — one per student
- [ ] Student job sheet at station: one per student

---

## Safety Briefing (Joint — 0:00 to 0:05)

**Instructor delivers the following points to all students before any station work begins. This briefing is not optional.**

**EPS motor safety:**
The EPS ECU at Station A is connected to a motor circuit. The power stage can source significant current. Do not insert probes or fingers into live connectors unless directed by the procedure. Do not bypass the bench harness fuse. If the EPS column unit is mounted and the motor activates, the column will rotate — do not put hands or tools in the rotation path when Terminal 15 is switched on. When performing oscilloscope measurements, connect your probes before applying power — do not probe live connectors while the ECU is running.

**ABS solenoid outputs:**
The ABS ECU at Station B controls solenoid valve outputs. On the bench harness, there is no hydraulic system — the outputs drive only LED indicators. However, do not command output tests that the instructor has not cleared. The coding procedure writes to the ECU — do not initiate a write without instructor confirmation that the connection is stable.

**Bench supply safety:**
Bench supplies are set at the correct voltage and current limit. Do not modify supply settings. If you smell burning from any bench component, switch off the bench supply immediately — do not disconnect wires first.

**Probe safety — oscilloscope:**
When probing the EPS torque sensor simulator, probe outputs only. Do not probe inside the EPS ECU connector with the ECU powered. Do not short probe tips together on a powered circuit.

**ESD protocol:**
Wear ESD wrist straps when handling ABS ECU or EPS ECU PCBs outside their housings.

---

## Station A: EPS Fault Diagnosis

### Equipment at Station A

| Item | Quantity | Notes |
|------|----------|-------|
| EPS ECU or column unit on bench harness | 1 | Pre-wired; torque sensor simulator connected |
| Bench power supply | 1 | 12.0V / 10A minimum |
| Bench harness (pre-wired) | 1 | Terminal 30, Terminal 15, CAN, torque sensor connector, motor connector — all labelled |
| Torque sensor fault simulator | 1 | Selectable: Healthy, Signal A open, Signal B open, Signal A short to ground, Signal A+B sum deviation |
| Oscilloscope (2-channel minimum) | 1 | |
| Oscilloscope probes | 2 | |
| Multimeter | 1 | For static voltage measurements |
| Station laptop with diagnostic software | 1 | Confirmed communicating with EPS module |
| OBD2 interface cable | 1 | |
| EPS torque sensor signal reference card | 1 per student | Signal A/B normal values; fault conditions table; sum calculation instructions |
| Reference waveform card | 1 per station | Shows healthy Signal A + B oscilloscope capture (unlabelled fault captures not provided until after diagnosis) |
| Student job sheet — EPS diagnosis | 1 per student | Records DTCs, live data values, oscilloscope observations, fault conclusion |
| ESD mat + wrist strap | 1 mat; 1 per student | |

---

### Station A Procedure

#### Phase A1 — Bench Setup Verification (5 minutes)

Before applying power, verify the bench harness setup. Do not assume connections are correct.

**Step A1.1 — Visual inspection of harness connections:**
- Confirm Terminal 30 (battery permanent supply) is connected to the supply positive terminal
- Confirm Terminal 15 (ignition-switched supply) is connected and its switch is in the OFF position
- Confirm ground connection is made — verify with multimeter: continuity between bench harness ground and bench supply negative terminal should read <0.5Ω
- Confirm CAN-H and CAN-L are routed from the bench harness to the OBD2 interface cable
- Confirm the torque sensor simulator is connected to the torque sensor connector on the EPS ECU harness

**Step A1.2 — Simulator initial position:**
- Confirm the torque sensor simulator is in the "Healthy" position (default)
- Both Signal A and Signal B outputs should be active and will show approximately 2.5V when the ECU is powered

**Step A1.3 — Connect scan tool:**
- Confirm OBD2 interface cable is connected to the station laptop
- Open the diagnostic software and confirm it is ready (no "interface not found" errors)

**Step A1.4 — Set bench supply:**
- Bench power supply: 12.0V; current limit 10A
- Do not enable the supply output yet — the first step with power is the DTC scan (Phase A2)

---

**INSTRUCTOR CHECKPOINT A0:** Confirm each group has a correctly verified harness before power is applied. Review: Terminal 30 connected? Terminal 15 switch in OFF? Ground confirmed? CAN cables seated? Simulator in Healthy position?

---

#### Phase A2 — Initial DTC Scan (5 minutes)

**Step A2.1 — Power on and initialise:**
- Switch on Terminal 15 on the bench harness
- Allow the EPS ECU 10–15 seconds to initialise — do not attempt scan tool connection immediately
- Enable bench supply output (Terminal 30 should already be connected)

**Step A2.2 — Scan tool connection:**
- Open the diagnostic software on the station laptop
- Connect to the EPS module (platform-specific address — listed on the bench harness label or station setup card)
- If the EPS module does not respond: check Terminal 15 supply voltage with multimeter; check CAN-H and CAN-L signal is present at the OBD2 connector pins; confirm scan tool interface is correct for this EPS ECU platform

**Step A2.3 — Read DTCs:**
- Navigate to: Read Fault Codes (or equivalent in the diagnostic software)
- Record all stored and pending DTCs on the job sheet — include the full DTC description, not just the code number
- Note which system or channel each DTC references

**Step A2.4 — Read live data:**
- Navigate to: Measuring Blocks / Live Data
- Locate and record the following on the job sheet:
  - Torque Sensor Signal A voltage (V)
  - Torque Sensor Signal B voltage (V)
  - Torque Sensor demand value (Nm) if available
  - EPS assist status (active/inactive)
  - Vehicle speed input value (should be 0 on bench)

With simulator in the "Healthy" position and the column at rest, both signals should read approximately 2.5V. The EPS assist status may show inactive until the system confirms a valid torque sensor reading and completes its initialisation cycle.

---

**INSTRUCTOR CHECKPOINT A1:** Each group should have established scan tool communication, read DTCs, and be reading live data with no unexplained communication errors before proceeding to oscilloscope work. A scan tool that shows the EPS ECU but cannot read live data indicates a software configuration issue — resolve before proceeding.

---

#### Phase A3 — Healthy Signal Capture on Oscilloscope (10 minutes)

This step establishes the reference baseline. Students must capture and understand the healthy signal before any fault is injected. The baseline capture is the reference against which they will identify the fault.

**Step A3.1 — Connect oscilloscope probes:**
- Connect Channel 1 probe tip to the Signal A output wire at the torque sensor simulator output connector
- Connect Channel 1 ground clip to bench harness ground
- Connect Channel 2 probe tip to the Signal B output wire at the torque sensor simulator output connector
- Both channel ground clips should reference the same bench ground point

**Step A3.2 — Configure oscilloscope:**
- Both channels: 1V per division, DC coupling
- Timebase: 100ms per division (adjust if needed — the goal is to see both channels in motion)
- Trigger: Channel 1, rising edge, approximately 2.5V trigger level
- Auto-scale if available to confirm signals are visible before manual adjustment

**Step A3.3 — Capture healthy signal:**
- With the simulator in "Healthy" mode, slowly rotate the simulator input dial from full left position to full right position and back to centre
- Observe both channels simultaneously while rotating:
  - Does Signal A rise when rotating in one direction?
  - Does Signal B move in the opposite direction simultaneously?
  - Do both signals appear to sum to approximately 5V across all positions?
- Pause the oscilloscope capture with both signals visible in a characteristic position (e.g., one channel high, the other low)
- Sketch both waveforms on the job sheet — label: "Signal A — healthy", "Signal B — healthy"; mark the approximate voltage at left turn, centre, and right turn positions

**Discussion prompt:** "Without the oscilloscope, could a multimeter show you the same information?"
Expected: yes, a multimeter can show static voltage values — but only the oscilloscope shows both signals simultaneously as a continuous trace during movement; this makes the complementary relationship and any asymmetry immediately apparent.

Record the oscilloscope observations on the job sheet before proceeding to fault injection.

---

#### Phase A4 — Fault Injection and Diagnosis (15 minutes)

**How the fault injection exercise works:**
The instructor or station supervisor sets one of the four fault conditions on the simulator without informing the students which fault is active. Students must diagnose the fault condition from DTC evidence, live data values, and oscilloscope observations — then state their diagnosis with supporting evidence before the instructor reveals the fault.

**Available fault conditions on the torque sensor simulator:**

| Simulator Position | Fault Injected | Expected DTC | Expected Live Data | Expected Oscilloscope |
|-------------------|----------------|-------------|-------------------|-----------------------|
| Healthy | None | No torque sensor DTCs | A ~2.5V, B ~2.5V at rest; complementary motion when rotated | Both channels move oppositely during rotation |
| Fault 1 | Signal A — open circuit | STS Signal A: implausible value / open circuit | Signal A: 0V or 5V (stuck); Signal B: normal motion | Channel 1 static; Channel 2 moves normally |
| Fault 2 | Signal B — open circuit | STS Signal B: implausible value / open circuit | Signal A: normal motion; Signal B: 0V or 5V (stuck) | Channel 1 moves normally; Channel 2 static |
| Fault 3 | Signal A — short to ground | STS Signal A: short to ground | Signal A: 0V (stuck); sum of A + B < 5V | Channel 1 at 0V; Channel 2 moves normally; sum not constant |
| Fault 4 | Signal A + B sum deviation | STS: implausible signal combination | Sum of A + B deviates significantly from 5V | Both channels show output but sum is not ~5V |

**Student procedure:**

Step A4.1 — Instructor sets the fault condition (unknown to students); instructor does not confirm which fault has been set.

Step A4.2 — Power cycle the EPS ECU:
- Switch Terminal 15 OFF; wait 10 seconds; switch Terminal 15 ON
- This forces the EPS ECU to re-evaluate its inputs with the new fault condition active and store DTCs if applicable

Step A4.3 — Read DTCs from the EPS module via scan tool:
- Record all new DTCs on the job sheet
- Note: which channel does the DTC reference? Signal A or Signal B? What is the fault type stated?

Step A4.4 — Read live data:
- Read Signal A voltage; read Signal B voltage
- Calculate: Signal A + Signal B = ?
- Record both values and the sum on the job sheet
- Is the sum approximately 5V? If not, by how much does it deviate?

Step A4.5 — Oscilloscope capture with fault active:
- With both probes still connected to Signal A and Signal B
- Slowly rotate the simulator dial while observing both channels
- Which channel moves during rotation? Which channel is static?
- Does one channel show a fixed voltage that does not change regardless of simulator position?
- Capture (pause or sketch) the oscilloscope trace showing the fault condition — label clearly on job sheet

Step A4.6 — State the diagnosis:
Write the diagnosis on the job sheet before the instructor reveals the fault:
- Which channel is at fault? Signal A, Signal B, or both?
- What type of fault? Open circuit, short to ground, or implausible combination?
- What is your evidence? List: DTC description; measured voltage values; sum calculation result; oscilloscope observation

Step A4.7 — Instructor reveals the fault condition:
- Compare student diagnosis to the actual fault
- If the diagnosis was correct: confirm the evidence chain that led to it
- If the diagnosis was incorrect: identify which evidence was misread or which step was missed; this is the teaching moment

---

**INSTRUCTOR CHECKPOINT A2:** Students must state their diagnosis with written evidence before the instructor reveals the fault. A verbal guess without documented evidence is not accepted — redirect: "What does the DTC say specifically? What does the sum of A + B tell you? What does the oscilloscope show for Channel 1?" The aim is evidence-based diagnosis, not correct-answer guessing.

---

#### Phase A5 — EPS Coding Awareness (5 minutes — discussion only)

No coding changes are performed on the EPS ECU at Station A. The coding procedure requires vehicle-specific data that is not available in the bench context without a full calibration workflow. This section is a guided discussion only.

**Step A5.1 — Open the coding screen:**
- In the diagnostic software, navigate to the EPS module coding section
- Read the current coding — do not change any values

**Step A5.2 — Discussion questions for the group:**
- What parameters are typically coded in an EPS ECU? (Expected: vehicle type, steering ratio, assist map profile, speed-dependent assist curves)
- What would happen if the steering angle sensor calibration was not performed after EPS ECU replacement? (Expected: EPS may work mechanically but SAS has no zero-point reference; ADAS lane-keeping uses the SAS data; incorrect reference may cause ADAS to operate from a wrong baseline — the hook scenario from the theory session)
- Which scan tool would be used for SAS calibration on the vehicle platform at this station? (Platform-specific — VCDS for VW Group, ISTA for BMW, IDS for Ford, etc.)

Record the coding parameters observed on the job sheet. No changes made.

Sign off so-8-3-2 on the check-off card.

---

## Station B: ABS Fault Categorisation and Module Coding

### Equipment at Station B

| Item | Quantity | Notes |
|------|----------|-------|
| ABS module on bench harness | 1 | All scenario DTCs loadable; wheel speed sensor simulator connected |
| ABS hydraulic unit specimen (ECU removed) | 1 | For solenoid valve resistance testing in Scenario B-3 |
| Wheel speed sensor simulator | 1 | Generates square-wave signals on all 4 channels; allows per-channel fault injection |
| Replacement ABS ECU (known-good, uncoded or different coding) | 1 | For coding exercise in Phase B2 |
| Bench power supply | 1 | 12.0V / 5A |
| ABS bench harness (pre-wired) | 1 | Terminal 30, Terminal 15, CAN, WSS simulation inputs — all labelled; LED indicators on solenoid output pins |
| Multimeter | 1 | For solenoid valve resistance measurement and supply voltage check |
| Oscilloscope | 1 | Optional: can be used to verify WSS signal at ABS ECU connector |
| Station laptop with diagnostic software | 1 | ABS coding capability confirmed working |
| OBD2 interface cable | 1 | |
| ABS fault categorisation worksheet | 1 per student | Table with columns: Fault Observed / Evidence / Category / Next Action |
| Coding specification card | 1 | Instructor-prepared; specifies all coding values for replacement ABS ECU |
| Printed ABS coding workflow card | 1 per student | Six-step procedure from theory session |
| Student job sheet | 1 per student | Records DTCs, categorisation decision, coding before/after values |
| ESD mat + wrist strap | 1 mat; 1 per student | |

---

### Station B Procedure

#### Phase B0 — Station Safety Briefing (2 minutes — additional to joint briefing)

Before work begins at Station B, the instructor or station lead delivers:

"The ABS ECU at this station controls solenoid valve outputs. On this bench harness, the outputs drive LED indicators — there is no hydraulic system. However, work methodically. Do not command output tests unless the procedure directs you to. The coding exercise at the end of this station will write to the ABS ECU — do not initiate a coding write without instructor confirmation that the scan tool connection is stable. Any questions?"

---

#### Phase B1 — Fault Categorisation Exercise (20 minutes)

**How the scenario exercise works:**
Each group receives one scenario card. Three different scenario cards are used across the class. After each group completes their scenario, groups share their conclusions in the debrief and compare the three different fault categories. Each group should experience their own scenario fully rather than hearing the answer from another group before working.

---

**Scenario Card B-1: The Communication Fault**

*Customer complaint: ABS warning light on, traction control warning light on, vehicle will not pass scan tool DTC check. No symptoms felt while driving. ABS has not activated abnormally.*

*Pre-set fault condition on bench harness:* ABS ECU supply voltage deliberately reduced by adding a series resistor in the Terminal 30 supply line — voltage present at ECU but at approximately 10.5V rather than 12V.

**Student procedure for Scenario B-1:**

Step 1: Connect scan tool; attempt communication with ABS module.

Step 2: If communication is intermittent, slow, or fails: do not immediately condemn the ABS ECU; this is the most common incorrect first response.

Step 3: Measure Terminal 30 supply voltage at the ABS ECU supply pin on the bench harness using a multimeter. Record the measured voltage.

Step 4: Compare measured voltage to specification: ABS ECUs typically require 10.5–16V for reliable operation; note whether the measured voltage is at the low boundary of this range or below it.

Step 5: Consider: if the vehicle equivalent had a high-resistance connection in the ABS fused supply circuit (corroded fuse holder, loose terminal), this voltage drop would appear. It is not an ABS ECU failure — it is a supply issue.

Step 6: Complete the categorisation worksheet:
- Fault observed: [describe what was seen]
- Evidence: [supply voltage measured; communication failure; DTC if any]
- Category: Hydraulic Unit fault / ABS ECU Electronics fault / Supply or Wiring fault (circle one)
- Correct next action: [state what should be done on the actual vehicle]

Expected conclusion: Supply or Wiring fault — investigate Terminal 30 supply circuit; do not replace ABS ECU.

**Instructor note for B-1:** This scenario teaches the single most important lesson of the session: always verify the supply before condemning the ECU. Students who immediately classify this as an ABS ECU failure have not applied the correct diagnostic sequence. Redirect: "What does the voltmeter show at the ECU supply pin?"

---

**Scenario Card B-2: The Wheel Speed Sensor Fault**

*Customer complaint: ABS warning light appeared after wheel bearing replacement on right front. No abnormal ABS activation during normal driving. Vehicle drives normally.*

*Pre-set fault condition on bench harness:* Wheel speed sensor simulator with Channel 1 (right front) output disabled — no signal present on that channel at the ABS ECU connector.

**Student procedure for Scenario B-2:**

Step 1: Connect scan tool; read DTCs from ABS module; record full DTC description including which wheel position.

Expected DTC: Wheel speed sensor — right front: signal absent / open circuit (or equivalent for this ABS platform).

Step 2: Navigate to live data in the diagnostic software; view all four wheel speed channels simultaneously (or as available).
- Right front channel: should show 0 km/h or dashes at all times
- All other three channels: should show the speed value output from the simulator

Step 3: Record live data values — all four channels — on the categorisation worksheet.

Step 4: Use oscilloscope (optional but recommended): probe the WSS input signal wire for the right front channel at the ABS ECU connector — confirm whether a signal is present or absent at the ECU connector itself.

Step 5: Interpret the evidence:
- Single channel affected while three channels operate correctly → the fault is isolated to the right front WSS circuit, not the ECU
- DTC is specific to one wheel position → this matches a sensor or wiring fault, not an ECU internal failure
- The fault appeared after wheel bearing replacement → the bearing replacement may have disturbed the WSS cable, or the air gap may have changed

Step 6: Complete the categorisation worksheet:
- Fault observed; Evidence; Category: Wheel Speed Sensor / Wiring fault; Correct next action

Expected conclusion: Wheel Speed Sensor / Wiring fault — inspect right front WSS cable and connector; check air gap after bearing replacement; do not replace ABS ECU.

---

**Scenario Card B-3: The Solenoid Valve Driver Fault**

*Customer complaint: ABS warning light on. Brake pedal behaviour felt slightly abnormal during one ABS activation event — pulled slightly to the left during a hard stop.*

*Pre-set fault condition:* ABS ECU pre-loaded with a stored DTC for "inlet valve — left front: open circuit" (stored by instructor before session by commanding an output test against an open circuit, then reconnecting the channel).

**Student procedure for Scenario B-3:**

Step 1: Connect scan tool; read DTCs from ABS module; record the full DTC description.

Expected DTC: Solenoid valve — left front inlet: open circuit (or equivalent for this ABS platform).

Step 2: Navigate to output tests in the diagnostic software (may be labelled: Actuator Tests, Component Tests, or Output Tests).

Step 3: Command the solenoid valve output test for the affected channel (left front inlet valve).

Step 4: Observe the LED indicator on the bench harness for that channel:
- If the LED illuminates: the ECU driver is outputting a command signal — the driver itself is functional; the fault may be in the external solenoid wiring or solenoid
- If the LED does not illuminate when commanded: the ECU's driver for that channel has failed internally

Step 5: Confirm by testing the hydraulic unit solenoid valve resistance:
- On the bench, a resistor representing the solenoid load (approximately 4–8Ω) is wired to the solenoid test connector
- Measure resistance with multimeter: value is within specification
- Interpretation: if the external solenoid load is in specification but the ECU driver does not activate the output → the fault is internal to the ABS ECU electronics

Step 6: Complete the categorisation worksheet:
- Fault observed; Evidence (DTC, output test result, solenoid resistance measurement); Category: ABS ECU Electronics fault; Correct next action

Expected conclusion: ABS ECU Electronics fault (solenoid valve driver failure) — component-level repair (replace solenoid driver MOSFET on ABS ECU PCB) or replace ABS ECU if component repair is not feasible.

---

**After all scenario work — group comparison (3 minutes):**

If two or more groups have completed different scenarios, have them share their conclusions before proceeding to coding. Establish:
- Scenario B-1: supply fault — no ECU replacement; cost of repair = supply circuit investigation
- Scenario B-2: sensor/wiring fault — no ECU replacement; cost of repair = sensor or cable
- Scenario B-3: ECU electronics fault — ECU replacement or component repair

"In each scenario, the ABS warning light was on. In two of the three cases, the ABS ECU was not at fault. This is the normal distribution in real practice — most ABS lights are not ABS ECU failures."

---

**INSTRUCTOR CHECKPOINT B1:** Confirm each group has a correctly completed fault categorisation worksheet with evidence recorded before proceeding to coding. A conclusion without evidence is not accepted. If a group has reached the wrong conclusion, review their evidence chain with them — where did the diagnostic sequence break down?

---

#### Phase B2 — ABS Module Coding and Adaptation (15 minutes)

For this section, the instructor provides the replacement ABS ECU. The original faulted ABS ECU remains connected to the harness until this phase begins — do not disconnect it until directed.

**Step B2.1 — Connect the replacement ABS ECU:**
- Disconnect the original ABS ECU from the bench harness
- Connect the replacement ABS ECU to the bench harness
- Ensure all connector pins are fully seated

**Step B2.2 — Power on and establish communication:**
- Enable bench supply (12.0V)
- Switch Terminal 15 ON
- Open the diagnostic software; connect to the ABS module
- Confirm communication is established — the replacement ECU should respond
- Read controller identification: note part number, hardware version, software version — record on job sheet

**Step B2.3 — Read and record current coding on replacement ECU:**
- Navigate to coding screen in diagnostic software
- Read the current variant coding or adaptation channel values
- Record every parameter that will be changed in the "Before Coding" column on the job sheet
- This record is essential — if coding produces unexpected results, the "Before" values allow rollback

**Step B2.4 — Apply coding from the specification card:**
The instructor coding specification card lists all required coding values for the scenario vehicle. Apply each value:

For each coding parameter to change:
- Record the current value in "Before" column (if not already recorded)
- Enter the new value from the specification card
- Confirm the entry before writing

Typical parameters on the specification card (platform-dependent):
- Country/market variant coding
- Tyre circumference or tyre size code (safety-relevant: affects ABS activation sensitivity and vehicle speed calculation)
- Trailer stability assist: enable/disable if fitted
- Off-road mode: enable/disable if applicable
- Any additional platform-specific adaptation channels specified

**Step B2.5 — Write the coding:**
- In the diagnostic software: click "Do It!", "Apply", or "Write Coding" (software-dependent)
- Confirm no error message is returned (an error may indicate security access was not completed — re-enter security access code if required and apply coding again)
- Do not disconnect the scan tool or disturb the power supply during the write operation

**Step B2.6 — Power cycle:**
- Switch Terminal 15 OFF; wait 10 seconds; switch Terminal 15 ON
- Allow the ABS ECU to reinitialise

**Step B2.7 — Verify coding was retained:**
- Return to coding screen in diagnostic software
- Read the current coding values
- Confirm each value from the specification card is present in the readback — compare systematically, not just visually
- Record the "After" coding values in the job sheet "After Coding" column
- Each specified value should match — any mismatch indicates the write was not accepted for that parameter

**Step B2.8 — Read DTCs after coding:**
- Read all stored and pending DTCs from the ABS module
- Expected: possible DTCs related to disconnected WSS simulator channels or other bench-specific conditions; no coding-related fault codes
- Unexpected: a DTC referencing a specific adaptation channel or coding byte that is out of range → this indicates a coding error in that parameter; review the specification card value and re-apply
- Clear all DTCs
- Read DTCs a second time — confirm no new faults were generated by the coding process

Record all DTC findings on the job sheet.

---

**INSTRUCTOR CHECKPOINT B2 (after ABS coding):** Review the job sheet with each group:
- "Before" values recorded before any coding change was made?
- All specified coding values applied and confirmed on readback?
- Power cycle performed?
- Post-coding DTC read and clear completed?
- No unexplained faults remaining?

Sign off so-8-3-3 and so-8-3-4 on the check-off card.

---

#### Phase B3 — Adaptation Channels (5–8 minutes if time permits after B2)

Some ABS platforms expose individual settable adaptation channels in addition to the main variant coding block. These are single parameters that can be adjusted independently.

**Step B3.1 — Navigate to adaptation channels:**
- In the diagnostic software, navigate to Adaptation (may also be labelled: Measuring Value Blocks — Write, or Learned Values)
- Read all available adaptation channels; record their names and current values on the job sheet

**Step B3.2 — Apply any adaptation channels specified on the coding specification card:**
For each channel specified:
- Record current value; enter new value; write adaptation; confirm acceptance

**Step B3.3 — Discussion question:**
"Identify one adaptation channel on this ABS module that, if set incorrectly, would have a safety or driveability consequence."

Expected answer (if tyre circumference is an available adaptation): if set too high, the ABS ECU calculates lower wheel speed than actual → ABS activates earlier than it should (nuisance activations on dry road); if set too low, ABS may not activate until the wheel has already locked further than the design threshold. This is a safety-relevant parameter, not a preference setting.

---

## Rotation (0:47 to 0:50)

**Departing students confirm before leaving their station:**
- [ ] All job sheet content up to current checkpoint recorded
- [ ] Oscilloscope captures sketched or photographed for job sheet reference
- [ ] All files and notes saved; laptop screen not in a state that will confuse the incoming group
- [ ] Station left tidy — tools returned to tray, no loose wires across the bench

**Arriving students at each station:**
- [ ] Read the station setup card before touching any equipment
- [ ] Do not assume the previous group left the equipment in the correct state — verify bench supply voltage and harness connections
- [ ] Arriving at Station A: simulator should be in "Healthy" position; confirm before powering ECU

**Station A handover note:** If the previous group's fault diagnosis exercise is complete, the arriving group repeats the procedure from Phase A2 (DTC scan) with a fresh fault condition set by the instructor. Each group should experience their own diagnostic exercise, not continue the previous group's.

**Station B handover note:** Arriving group at Station B should read the previous group's scenario card to understand which scenario was completed, then proceed with their own assigned scenario card.

---

## Debrief (Joint — 1:25 to 1:35)

Bring all students together. Instructor leads; students respond.

**Discussion questions:**

1. "Station A — what was the definitive piece of evidence that told you which torque sensor channel was at fault? Could you have reached the same conclusion with a multimeter alone, without the oscilloscope?"

Expected: the oscilloscope confirmed the static (non-responding) signal by showing no change during simulator rotation — both channels visible simultaneously makes the asymmetry immediately obvious. A multimeter static reading can confirm an open circuit (if the channel is stuck at 0V or 5V, multimeter shows it); but the scope shows both signals simultaneously and makes the complementary relationship and any deviation from it unmistakable.

2. "What is the significance of the sum calculation (Signal A + Signal B)? Why does the EPS ECU use this?"

Expected: the sum should always be approximately 5V regardless of steering position because the two sensors are on opposite sides of the torsion bar; any deviation from 5V is impossible in normal operation — so any deviation is unambiguous evidence of a fault on one channel; the EPS ECU uses this as a self-checking mechanism that cannot produce a false negative.

3. "Station B — all three scenario cards showed ABS warning lights. How many of them actually required ABS ECU replacement or electronics repair?"

Expected: only Scenario B-3 was an ABS ECU electronics fault; B-1 was a supply fault, B-2 was a sensor/wiring fault. Two out of three ABS warning light presentations were not ECU failures. This is consistent with real workshop statistics — confirm this for the group.

4. "You've coded the replacement ABS ECU. The customer asks if the brakes work normally and if they can drive away immediately. What do you tell them?"

Expected: basic braking function is not affected by ABS ECU coding; however, a short road test is required to confirm the ABS ECU self-test passes (no warning light above 15–20 km/h), and if any hydraulic work was done, a brake pedal check first; the customer should be told what was done and what was confirmed before driving away.

5. "A customer asks you to also look at the ADAS on their car after you've replaced the ABS ECU. The ABS ECU replacement involved no mechanical work — just unbolting the ECU from the HCU. Does the ABS ECU replacement require ADAS calibration?"

Expected: no — ABS ECU replacement alone does not disturb any ADAS sensor mounting; ADAS calibration would only be triggered if accompanying work affected camera or radar mounting (windscreen, bumper, front subframe, wheel alignment); the SAS calibration that may be required after EPS work is different from ADAS calibration.

**Key takeaways to close:**
- EPS diagnosis: DTC tells you which channel; oscilloscope confirms which channel and what type of fault; the sum calculation is the self-check
- ABS diagnosis: power supply first; external components second; ECU last; most ABS warning lights are not ECU failures
- Never skip post-replacement coding on ABS — tyre size and market variant are safety-relevant parameters
- ADAS calibration triggers are a separate knowledge area — today's work (EPS and ABS ECU) does not trigger ADAS calibration requirements

---

## Common Problems Reference Table

| Problem | Station | Likely Cause | Resolution |
|---------|---------|-------------|-----------|
| EPS ECU not communicating on bench | A | Terminal 15 not switched on; CAN cables not seated; incorrect module address in scan tool | Check Terminal 15 supply voltage; reseat CAN cables; confirm module address |
| Oscilloscope shows only one channel (both appear to read the same signal) | A | Both probes accidentally connected to the same simulator output wire | Verify probe tip locations — one on Signal A wire, one on Signal B wire |
| Signal A and Signal B both show exactly 2.5V without movement during rotation | A | Simulator still in "Healthy" position — fault was not injected; or simulator connection not made | Confirm fault injection was made; verify simulator connector is fully seated |
| Student guesses fault category without evidence | B | Diagnostic shortcut — jumping to conclusion | "What does the DTC description say specifically? What did the live data show? What did the multimeter read?" Redirect to evidence |
| ABS ECU does not communicate after connecting replacement unit | B | Harness connector not fully seated; ECU not compatible with bench harness | Check connector seating; verify replacement ECU part number compatibility with bench harness |
| Coding write returns error message | B | Security access not unlocked before coding; or connection instability | Re-enter security access code; confirm stable CAN connection; retry coding |
| Post-coding DTC check shows new faults related to coding | B | One or more coding values outside the acceptable range for this ECU | Review specification card values; re-read the parameter that generated the DTC; correct and re-apply |
| Adaptation channel "write" not accepted (returns to previous value) | B | Security access not maintained; or channel is read-only on this platform | Re-enter security access; confirm adaptation channel is writeable on this software version |
| EPS torque sensor sum calculation does not equal ~5V with healthy simulator | A | Simulator supply voltage not at 5V; probe ground reference not correct | Measure simulator supply voltage with multimeter; confirm both probe ground clips are on the same ground reference |

---

## Equipment List — Full Session

### Station A (per station, supports 2 students)

| Item | Specification | Quantity |
|------|--------------|----------|
| EPS ECU or column unit on bench harness | Pre-wired; torque sensor simulator connected; motor connector present | 1 |
| Bench power supply | 0–30V, 0–10A, digital display, current limitable | 1 |
| Bench harness — EPS | Vehicle-specific connector; Terminal 30, 15, CAN, torque sensor, motor — all labelled | 1 |
| Torque sensor fault simulator | Rotary input; 5 selectable states: Healthy + 4 fault conditions | 1 |
| Oscilloscope | 2-channel minimum; 25MHz minimum bandwidth; 100ms/div timebase capability | 1 |
| Oscilloscope probes (x2) | Standard 1x/10x probes | 2 |
| Multimeter | Auto-ranging | 1 |
| Station laptop | Windows 10+; diagnostic software installed; OBD2 interface driver installed | 1 |
| OBD2 interface cable | Compatible with diagnostic software and EPS ECU platform | 1 |
| EPS torque sensor signal reference card | Normal values, fault conditions, sum calculation — one per student | 1 per student |
| Reference waveform card | Healthy signal A + B oscilloscope capture (laminated; no fault labels) | 1 |
| Student job sheet — EPS | DTC, live data, oscilloscope sketch, diagnosis conclusion fields | 1 per student |
| ESD mat + wrist strap | | 1 mat; 1 per student |

### Station B (per station, supports 2 students)

| Item | Specification | Quantity |
|------|--------------|----------|
| ABS module on bench harness | Pre-faulted per scenario; WSS simulator connected; LED indicators on solenoid outputs | 1 |
| ABS hydraulic unit specimen (no ECU) | Solenoid valve test connector accessible; resistive solenoid load fitted | 1 |
| Wheel speed sensor simulator | 4-channel; individually switchable; square wave output per channel | 1 |
| Replacement ABS ECU | Same platform as bench harness; blank or different coding | 1 |
| Bench power supply | 0–30V, 0–5A, digital display, current limitable | 1 |
| Bench harness — ABS | Vehicle-specific multipin connector; Terminal 30, 15, CAN, all WSS channels — labelled | 1 |
| Multimeter | Auto-ranging | 1 |
| Oscilloscope (optional but recommended) | For WSS signal verification | 1 |
| Station laptop | Windows 10+; diagnostic software with ABS coding capability; OBD2 driver installed | 1 |
| OBD2 interface cable | Compatible with diagnostic software and ABS ECU platform | 1 |
| Scenario cards (B-1, B-2, B-3) | Laminated; assigned to groups before session | 1 per group |
| Coding specification card | Instructor-prepared; all required coding values listed | 1 |
| ABS fault categorisation worksheet | Columns: Fault Observed / Evidence / Category / Next Action | 1 per student |
| ABS coding workflow card | Six-step procedure from theory session | 1 per student |
| Student job sheet — ABS | DTC, categorisation, coding before/after fields | 1 per student |
| ESD mat + wrist strap | | 1 mat; 1 per student |

---

## Student Check-Off Card

*To be completed by student and signed by instructor at each checkpoint. Submit at end of session.*

**Student Name:** ______________________________
**Date:** ______________________________
**Group (A first / B first):** ______________________________

| Checkpoint | Description | Student Confirms | Instructor Initials |
|------------|-------------|-----------------|-------------------|
| A0 | Bench harness verified; simulator in Healthy position; power and CAN connections confirmed | [ ] | |
| A1 | Scan tool communicating with EPS ECU; live data reading Signal A and Signal B correctly | [ ] | |
| A2 | Fault diagnosed with written evidence before fault condition was revealed; diagnosis correct | [ ] | |
| A-SO | so-8-3-2 signed off: EPS fault diagnosed by DTC, live data, and oscilloscope signal analysis | [ ] | |
| B0 | Station safety briefing acknowledged; correct connector seating verified | [ ] | |
| B1 | Fault categorisation worksheet completed with evidence for assigned scenario; conclusion correct | [ ] | |
| B2 | Replacement ABS ECU coded per specification card; coding verified on readback; post-coding DTC check completed | [ ] | |
| B-SO | so-8-3-3 and so-8-3-4 signed off: ABS fault categorised correctly; replacement ABS module coded and verified | [ ] | |

---

## Module 8 Completion Check

At the end of Session 18H, Module 8 is complete. Before students leave, the instructor confirms:

- [ ] All students have completed job sheets for both stations on both days (17H and 18H)
- [ ] All EEPROM binary files from Day 17 are saved with correct naming conventions (confirm on the lab laptops)
- [ ] Any student who did not complete a station due to time constraints has a catch-up plan noted
- [ ] Module 8 written assessment date is confirmed with the full group

**Module 8 written assessment topics — advise students to review:**
- Cluster failure mode identification from photographs and symptom descriptions
- Legal and ethical context of odometer EEPROM access
- BCM EEPROM data content and BCM replacement programming workflow
- Torque sensor signal characteristics — normal values, fault conditions, sum calculation
- ABS fault categorisation methodology — hydraulic / electronics / sensor
- ADAS calibration requirement triggers and referral criteria

---

## Instructor Notes

**EPS torque sensor simulator build:**
If a commercial torque sensor simulator is not available, a reliable simulator can be built from: a pair of complementary potentiometers ganged to a common shaft (both wipers driven from a 5V regulated supply, one wiper in reverse — so as one rises the other falls); with a 4-position rotary switch to disconnect or short Signal A or Signal B for fault injection. The sum of A + B from a correctly built simulator will remain at 5V across the full rotation in the Healthy position. Build and test the simulator before the session to confirm it produces the correct healthy signal and the expected fault states.

**ABS bench harness LED indicators:**
Install one LED (with appropriate series resistor for 12V — approximately 470Ω for a standard LED) on each solenoid output pin of the bench harness. Without these, the output test component of Scenario B-3 cannot be demonstrated. The LED indicators also make the output test for Phase B2 coding verification visible without requiring the student to use a separate meter on each output.

**Scenario card assignment:**
Assign scenario cards to groups before the session starts. Use a rotation system so that across the full cohort, each scenario is experienced by approximately equal numbers of students. Do not allow students to choose their scenario — control the distribution to ensure all three scenarios are covered and the debrief comparison works as intended.

**Managing the ABS coding exercise:**
Walk the station during Phase B2 coding, particularly during the write step. A coding write that is interrupted by a dropped scan tool connection or a power supply interruption can leave the ABS ECU in a partially coded state that may require a full recoding or, in rare cases, ECU recovery. Confirm the scan tool connection is stable before the student initiates the write.

**Debrief timing:**
The debrief question about "two out of three ABS warning lights were not ECU failures" is the most important takeaway from Station B. Allocate at least 2 minutes to this discussion. The statistical reality — that most ABS warning lights in practice are sensor or wiring faults, not ECU failures — is counterintuitive to students who associate the warning light with the module it names.

---

*Module 8 | Day 18 Hands-On | ECUHR | v1.0 | 2026-02-18*
