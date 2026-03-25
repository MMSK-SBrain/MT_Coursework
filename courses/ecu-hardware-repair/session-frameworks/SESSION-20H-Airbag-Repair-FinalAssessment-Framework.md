# SESSION-20H: Airbag Hardware Repair Lab & Final Practical Assessment
## Hands-On Session | Day 20 | Module 9: Security & Safety Systems + Final Assessment

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 9 — Security & Safety Systems + Final Assessment
**Day:** 20 | **Session Type:** Hands-On Workshop + Final Assessment
**Duration:** 3 hours (extended session — Final Assessment)
**CO Alignment:** co-4, co-1, co-2, co-3 (Final Assessment covers all COs)

---

## Session Outcomes — Airbag Repair (Part 1)

| Code | Outcome | Bloom's Level |
|------|---------|---------------|
| so-9-3-4 | Diagnose and repair a hardware fault on an SRS PCB (capacitor, resistor, or driver IC) using soldering skills | Apply |
| so-9-4-1 | Perform a crash data reset on an SRS module and verify successful reset with re-scan | Apply |
| so-9-4-2 | Program a replacement SRS module and verify all SRS components fault-free after programming | Apply |
| so-9-4-3 | Demonstrate and explain all post-repair safety verification steps before returning vehicle | Evaluate |

## Final Assessment Outcomes (All Course Outcomes — co-1 through co-4)

| Assessment Element | CO | Description |
|-------------------|----|-------------|
| Bench setup and communication | co-1 | Establish correct ECU bench setup from wiring diagram |
| Systematic diagnostic approach | co-1 | Apply fault isolation methodology — not random probing |
| Correct fault identification | co-1, co-2 | Diagnose fault with supporting measurement evidence |
| Repair or programming procedure | co-2, co-3 | Execute or propose correct procedure for identified fault |
| Safety practices | co-1–co-4 | ESD, SRS protocols, professional conduct throughout |

---

## Session Structure Overview

| Time | Activity | Format |
|------|----------|--------|
| 0:00–0:10 | Safety protocol check; SRS module distribution; Part 1 briefing | Whole class |
| 0:10–1:00 | Part 1: Airbag hardware repair lab | Pairs |
| 1:00–1:05 | Part 1 debrief; break | Whole class |
| 1:05–1:15 | Final assessment setup: ECU distribution; rules read-out | Individual |
| 1:15–3:00 | Part 2: Final Practical Assessment (105 minutes, timed) | Individual |
| 3:00 onwards | Assessment collection; debrief; course close | Whole class |

**Timing note:** The session is structured as: 60-minute airbag lab + 15-minute break/transition + 105-minute final assessment. The airbag lab can be compressed to 50 minutes if necessary by abbreviating Activity 3 (crash data reset demo) to observation only. The assessment window must not be shorter than 90 minutes; 105 minutes is preferred. Do not sacrifice assessment time for lab activities.

---

## Part 1 — Airbag Hardware Repair Lab

**Duration:** 60 minutes
**Format:** Pair work
**Target SOs:** so-9-3-4, so-9-4-1, so-9-4-2, so-9-4-3

---

### Safety Protocol Verification — First 10 Minutes (Mandatory)

Before any SRS module is placed in a student's hands, the mandatory safety protocol is verbally confirmed by every student.

**Procedure:**

Instructor addresses the whole class:

"Before any SRS module is issued, I want to hear the five safety protocol steps from you. Verbally, in order."

Nominate students to provide each step. If any step is missing or misstated, correct it and repeat the question. Do not distribute any equipment until the full class can collectively state the complete protocol correctly:

1. Disconnect battery negative terminal
2. Wait — minimum 60 seconds; check OEM specification; may be up to 10 minutes
3. Disable HV system if hybrid/electric (not required for conventional vehicles)
4. After work complete: squib resistance check with high-impedance meter before reconnecting battery (normal range: 2–3Ω)
5. Reconnect battery; observe warning lamp during self-test; full scan tool SRS scan

"Good. This protocol is in effect from this moment. For the entire time you are working on SRS components today, this protocol governs your actions. Before you touch any SRS connector — including any connector in the squib circuit wiring, the clock spring connector, and any pre-tensioner connector — you will have completed Steps 1 and 2.

The bench power supply at your station is your 'battery.' When I say battery disconnect, I mean bench supply off. When I say 60-second wait, I mean 60 seconds minimum after turning the bench supply off, before touching any SRS component.

Any student who touches an SRS component without completing this protocol will be stopped. We will reset, complete the protocol correctly, and only then continue. This is not a recoverable mistake — I am telling you the consequence in advance so it does not happen."

Equipment is now distributed.

---

### Instructor Preparation for Part 1

**Fault A — Degraded Backup Capacitor:**

The backup energy storage capacitor on the SRS ACU PCB is typically a large electrolytic (10–47µF, 16–25V, 105°C automotive grade). Prepare donor SRS modules where this capacitor has been replaced with a deliberately out-of-specification component.

Method 1 (preferred): Replace the original capacitor with one of significantly lower capacitance value (1–2µF instead of the specified 10–47µF). The ACU self-test detects the inadequate backup energy storage and logs a power fault.

Method 2 (simulated degradation): Solder a 10–15Ω series resistance in one leg of the capacitor circuit (representing high ESR). The increased ESR causes the backup power self-test to fail.

Confirm the fault symptom on each module before the session: ACU communicates on CAN; logs a power supply or backup capacitor fault DTC; DTC is soft (clearable after repair); no deployment record present.

**Fault B — Failed CAN Transceiver IC:**

Prepare donor SRS modules where the CAN transceiver IC has been disabled.

Method 1: Solder a 150–470Ω resistor across the CANH and CANL output lines of the CAN transceiver IC (between the IC's bus-side pins and the module connector pins). This defeats the differential drive capability without causing a hard bus short.

Method 2: Break the connection between the CAN transceiver's TX input and the MCU's TX output (open a small PCB trace or remove a series resistor in the TX path).

Confirm the fault symptom: scan tool cannot communicate with the ACU; other modules can be communicated with; no crash data present.

**Crash data reset module (Activity 2):**

Prepare a separate SRS module with only soft fault DTCs present — clock spring open circuit (simulated by leaving a high-value resistor in series with a squib loop pin), or squib resistance fault — confirmed not having any deployment record. The fault should be clearable with a standard DTC clear command after the underlying condition is removed.

**Replacement module programming (Activity 3):**

Prepare a replacement SRS module of the same type as the crash data reset module. Confirm your scan tool can access and program/code this module type. Have the VIN or coding data ready.

**Pre-session verification checklist:**
- [ ] All donor SRS modules for Part 1 confirmed: soft fault present, no deployment record, correct DTC logged
- [ ] All donor modules: squib connector pins confirmed NOT connected to any actual squib device — dummy resistive loads only (see safety note below)
- [ ] Crash data reset module confirmed: soft DTC only, clearable
- [ ] Replacement module confirmed: scan tool programming/coding procedure verified
- [ ] Bench harnesses prepared: correct power connectors for each module type
- [ ] Dummy squib loads prepared: resistors simulating 2–3Ω squib resistance at each squib connector pin
- [ ] High-impedance multimeters (>10MΩ) confirmed available at each station
- [ ] ESR meters available for Fault A stations

**CRITICAL SAFETY NOTE — Squib connections in the lab:**

Under no circumstances should any actual squib device (live airbag module, live pre-tensioner assembly, or any unfired pyrotechnic component) be connected to the bench power harness or to any powered circuit in this lab. All squib circuit connections must terminate in dummy resistive loads simulating the 2–3Ω squib resistance. Instructor must verify this before the session begins. The consequence of a live squib being energised on a bench is immediate deployment.

---

### Activity 1 — SRS Hardware Fault Diagnosis (30 minutes)

**Objective:** Students diagnose a planted hardware fault on an SRS ACU PCB using scan tool DTCs and component-level measurements. They identify the specific faulty component before any repair is attempted.

**SO target:** so-9-3-4 (diagnostic component)

**Equipment at each station:**
- SRS ACU donor module with planted fault (Fault A or Fault B)
- Dummy resistive loads on all squib connector pins (NOT real squibs)
- Bench power supply with module connection cable
- High-impedance multimeter (>10MΩ)
- Oscilloscope (Fault B stations)
- Scan tool with SRS module access
- ESR meter (Fault A stations)
- Anti-static mat and wrist straps

---

#### Step A1-1: Safety Protocol Execution Before Touching Any Module

Before the donor SRS module is connected to anything:

1. Verify bench power supply is OFF
2. State aloud: "Bench supply disconnected — confirmed"
3. Set a 60-second timer
4. Timer expires: only then connect the module to the bench harness

This step is observed by the instructor for each student pair on the first day they handle SRS modules. Document compliance on the checkpoint card.

---

#### Step A1-2: Connect Module and Apply Power

1. Confirm all squib connector pins are terminated in dummy resistive loads — not open circuit, not real squibs
2. Connect module to bench power supply harness
3. Connect scan tool via OBD connector on bench harness
4. Apply bench power (12V)
5. Confirm scan tool can detect and communicate with the SRS module

---

#### Step A1-3: Read DTCs — Record Before Any Action

Read all SRS DTCs. Record every code before any other action:

```
DTC 1: ___________________________ Status: _______________
DTC 2: ___________________________ Status: _______________
DTC 3: ___________________________ Status: _______________
```

Classify each DTC:
- Is any DTC flagged as non-erasable / deployment record?
  ```
  Crash data present? YES / NO
  ```
- If YES: stop immediately. Call instructor. This module should not be repaired — something is wrong with the module preparation. Do not proceed.
- If NO (all DTCs are soft fault codes): proceed to component-level diagnosis.

---

#### Step A1-4: Component-Level Fault Diagnosis

**For Fault A — Power Supply / Capacitor Fault DTC:**

1. Identify the DTC description. It will indicate a power supply or backup energy fault.
2. Locate the backup capacitor on the PCB: largest electrolytic component on the board, positioned near the power supply section.
3. With bench power OFF and 60-second wait observed: measure the capacitor:
   - Using ESR meter: attach ESR meter probes to capacitor terminals in-circuit. Normal ESR for a 47µF automotive capacitor: below 1Ω. A reading above 5Ω indicates significant degradation. The deliberately out-of-spec planted component may read 10–15Ω or more.
   - Using multimeter (capacitance mode if available): measure capacitance in-circuit. Planted fault may show 1–2µF where 47µF is expected.
   - Using multimeter (resistance mode): in-circuit resistance across capacitor terminals should initially read low then rise as the capacitor charges from the meter current. A reading that stays permanently low (10–15Ω, not rising) indicates a very low capacitance or a parallel resistance (planted resistor).
4. Record measurements:
   ```
   ESR measured: _____________ Ω (normal: <1Ω)
   Capacitance measured: _________ µF (confirm against PCB spec or component marking)
   Resistance: stays low? YES / NO (rising to high = capacitor charging = capacitor present)
   Fault conclusion: _______________________________
   ```
5. Confirm: faulty component is the backup capacitor. Identify the component completely:
   - Reference designator from PCB silkscreen: _______________
   - Component marking: _______________
   - Correct replacement value needed: _______________

**For Fault B — CAN Communication / No Communication DTC:**

1. The DTC (or lack of scan tool communication) indicates the ACU cannot communicate on the CAN bus.
2. Apply bench power to the module. Connect oscilloscope to CANH and CANL pins on the bench harness OBD connector.
3. Observe CAN bus behaviour:
   - If other CAN nodes are present on the bench harness (or a CAN bus emulator): observe whether ACU frames appear. Normal: differential CAN transitions visible from the ACU node. Fault: no frames from ACU; bus may show activity from other nodes.
   - If no other CAN nodes: observe CANH and CANL voltage levels. ACU attempting to transmit should show CAN high at ~3.5V (dominant) and CAN low at ~1.5V (dominant) periodically. If both lines sit at ~2.5V with no transitions: transceiver not driving the bus.
4. With bench power OFF and 60-second wait observed: measure resistance from CANH pin to CANL pin at the SRS module connector (not at the OBD connector — at the module connector directly):
   - Normal: high resistance or open circuit (transceiver presents high impedance when unpowered in a correctly functioning module)
   - Fault planted with series resistor across bus: will read 150–470Ω between CANH and CANL
   - Fault planted with TX path open: CANH to CANL will read high impedance, but no transmission observed on scope
5. Record measurements:
   ```
   CANH voltage: _________ V | CANL voltage: _________ V
   CANH to CANL resistance (module unpowered): _________
   CAN frames from ACU visible on scope? YES / NO
   Fault conclusion: _______________________________
   ```
6. Confirm: faulty component is the CAN transceiver IC. Identify:
   - Reference designator from PCB silkscreen: _______________
   - Component marking (top line, IC body): _______________
   - Replacement part: TJA1040 / TJA1050 / equivalent as stocked

---

### Checkpoint 1 — Fault Diagnosis

Instructor sign-off before any repair begins:
- Student correctly identified the faulty component
- Supporting measurements are recorded and support the conclusion
- Safety protocol was observed correctly during diagnosis

```
Checkpoint 1 — PASS / RETRY
Fault identified correctly? YES / NO
Measurements recorded and support conclusion? YES / NO
Safety protocol observed? YES / NO
Instructor initials: _______
Notes: _________________________________
```

---

### Activity 2 — SRS PCB Repair (20 minutes)

**Objective:** Students replace the identified faulty component. Verify the repair resolves the fault DTC.

**SO target:** so-9-3-4 (repair component)

**Equipment added to station:** Soldering station, flux, solder, solder wick, isopropyl alcohol, cotton swabs, replacement capacitor (correct value) or replacement CAN transceiver IC (TJA1040/TJA1050 or equivalent).

---

#### Step A2-1: Pre-Repair Checks

1. Confirm bench power is OFF and 60-second wait has been observed since last power-down.
2. Confirm anti-static wrist strap is worn.
3. Confirm replacement component is the correct value and grade:
   - For capacitor: correct µF value, correct voltage rating (must exceed operating voltage), 105°C temperature grade
   - For CAN transceiver: correct package (SOIC-8), confirmed compatible part number
4. Note the component polarity or orientation before removal:
   - Capacitor: note the + terminal marking or the stripe indicating negative
   - CAN transceiver IC: note the pin 1 indicator (dot on body, silkscreen triangle)

---

#### Step A2-2: Component Removal

**Capacitor (through-hole or SMD):**
- Through-hole capacitor: heat each leg with the soldering iron while gently pulling the component from the opposite side; or use solder wick to clear the through-hole pads before removing
- SMD capacitor (uncommon on SRS PCBs but possible): hot air station at 280–300°C, medium airflow, move in circles above the component; remove with tweezers when solder liquefies

**CAN transceiver IC (SOIC-8):**
- Apply fresh flux to all 8 pins
- Hot air station at 320–340°C, medium-low airflow; hold nozzle approximately 10mm above the IC
- Heat with circular motion until solder liquefies on all 8 pins simultaneously
- Remove IC with ceramic tweezers — do not apply downward force, just lift when the IC releases
- Clean all 8 pads with solder wick; inspect under magnification for residue or damaged pads
- If a pad is lifted: call the instructor before proceeding

---

#### Step A2-3: Component Installation

**Capacitor:**
- Insert replacement capacitor with correct polarity (double-check the + terminal orientation)
- Solder both legs; inspect joints under magnification — smooth, shiny, fully wetted cone shape
- Trim excess lead length
- Clean with isopropyl alcohol

**CAN transceiver IC:**
- Place replacement IC on cleaned pads with pin 1 aligned to the silkscreen indicator
- Apply a small amount of flux to all pads
- Tack pin 1 and pin 8 (opposite corners) to hold the IC in position; check alignment under magnification
- Solder remaining pins using drag technique or individual pin technique with fine solder
- Inspect all 8 pins under magnification: no bridges between adjacent pins; no lifted pads; fully wetted joints on all pins
- Clean with isopropyl alcohol and cotton swab; re-inspect after cleaning

---

#### Step A2-4: Post-Repair Verification

1. Perform squib resistance check before reconnecting bench power:
   - Measure all dummy squib load connectors: confirm reading 2–3Ω (or whatever the dummy load was specified at)
   - This verifies no new squib circuit issues were introduced during repair
   ```
   Squib circuit resistance (all channels): _____________ Ω
   Within 2–3Ω range? YES / NO
   ```
2. Reconnect bench power supply (12V).
3. Observe: for Fault A — note whether the ACU powers on without the power fault DTC; for Fault B — verify scan tool can now communicate with the module.
4. Connect scan tool. Read all DTCs:
   ```
   Post-repair DTC scan result: _______________________________
   Fault DTC resolved? YES (DTC absent or now clearable)
   ```
5. If the specific fault DTC is absent or now clears cleanly: repair is successful. Proceed to Checkpoint 2.
6. If the fault DTC persists: re-examine the repair. Check component orientation and solder joint quality. Call instructor if fault persists after a confirmed correct repair.

---

### Checkpoint 2 — Repair Verified

```
Checkpoint 2 — PASS / RETRY
Component replaced correctly? YES / NO
Squib resistance check performed before power-on? YES / NO
Post-repair DTC scan confirms fault resolved? YES / NO
Instructor initials: _______
Notes: _________________________________
```

---

### Activity 3 — Crash Data Reset Demo and Replacement Module Programming (10 minutes)

**Objective:** Students observe the crash data reset procedure and module programming workflow. They are not performing these independently — they observe and answer debrief questions. This confirms so-9-4-1, so-9-4-2, and so-9-4-3 via observed knowledge and verbal confirmation.

**Format:** Instructor demonstration with student observation; debrief questions at the end.

---

**Instructor demonstration — Crash Data Reset:**

1. Connect the prepared SRS module (with soft fault DTCs only, no deployment record) to the bench setup.
2. Connect scan tool. Read DTCs aloud — show students the DTC list and status.
3. Attempt standard DTC clear: DTCs clear (this is a soft fault module — they should clear and not return).
4. Show students: "If this were a module with crash data — a deployment record — the DTCs would return immediately after clearing. That return is your confirmation of a hard fault."
5. Now demonstrate with the crash data reset tool (specialist tool — AirBag Reset Tool, Autel MaxiSYS with crash reset function, or equivalent): show the pre-reset DTC list, perform the reset, show the post-reset scan.
6. State explicitly: "I am demonstrating this on a module with only soft fault codes — confirmed before this session. The crash data reset function exists and some tools support it. For modules from genuine crash events where airbags deployed, using this tool to return the module to a vehicle is not legitimate repair. Understand the distinction."

---

**Instructor demonstration — Replacement Module Programming:**

1. Connect the replacement SRS module to the bench harness.
2. Connect scan tool. Show students the initial state — module communicates but may show configuration or VIN mismatch DTCs.
3. Navigate to Module Programming → SRS Module → Code/Program.
4. Enter the vehicle VIN or follow the coding wizard.
5. After coding complete: cycle ignition. Read all SRS DTCs.
6. Show expected result: no active SRS DTCs; airbag warning lamp (simulated) would extinguish.

---

**Debrief questions (ask each student pair verbally):**

"Without looking at any reference: describe the complete post-repair safety verification sequence before you return a vehicle that has had its SRS module replaced."

Expected answer includes all of:
- Squib resistance check on all disturbed circuits (2–3Ω normal range)
- Clock spring centring confirmed (if steering wheel was removed)
- Battery reconnected
- First power-on observed: warning lamp self-test then extinguishes
- Full SRS scan: no active DTCs
- Module programming/coding completed and confirmed
- All SRS connectors visually confirmed seated
- Work record documenting all actions completed
- Customer advised of work performed; any pre-existing conditions documented

---

### Checkpoint 3 — Post-Repair Safety Verification

```
Checkpoint 3 — PASS / RETRY
Student correctly describes full post-repair verification sequence? YES / NO
All 7+ elements of the sequence correctly stated? YES / NO
Instructor initials: _______
Notes: _________________________________
```

---

## Practical Check-Off Card — Day 20H (Airbag Repair Component)

**Student name:** _________________________
**Student pair:** _________________________
**Date:** _________________________

| Check Item | Pass | Instructor Initials |
|-----------|------|---------------------|
| Safety protocol verbally confirmed before any SRS module issued | | |
| Safety protocol executed correctly before first bench power application | | |
| SRS fault correctly diagnosed with supporting measurements | | |
| Faulty component correctly identified (reference designator and part value stated) | | |
| Squib resistance check performed before power reconnection | | |
| Component replaced using correct soldering technique | | |
| Post-repair DTC scan confirms fault DTC resolved | | |
| Post-repair safety verification sequence correctly described (Checkpoint 3) | | |

**SO Check-Offs:**

| SO | Status |
|----|--------|
| so-9-3-4 | [ ] Pass [ ] Retry needed |
| so-9-4-1 | [ ] Pass (observed) [ ] Not observed |
| so-9-4-2 | [ ] Pass (observed) [ ] Not observed |
| so-9-4-3 | [ ] Pass (verbal) [ ] Retry needed |

---

## Part 2 — Final Practical Assessment

**Duration:** 105 minutes timed (plus up to 10 minutes setup and briefing)
**Format:** Individual work — no collaboration from the moment assessment ECUs are distributed
**Scope:** All course outcomes co-1 through co-4; fault types from across all 9 modules

---

### Assessment Overview and Philosophy

This assessment determines whether the student can function as an independent ECU repair technician on an unseen fault. The fault has been planted by the instructor and is unknown to the student. The student has access to all standard workshop tools, the wiring diagram for the specific ECU type, and all skills developed over 20 days.

This is not a knowledge recall test. There are no written questions to answer from memory. The student diagnoses a real fault on real hardware and demonstrates the complete diagnostic and repair process under time pressure. The competency the course was designed to build is the competency being assessed.

**Assessment principle:** A student who correctly identifies the fault with full supporting evidence but does not complete the physical repair within the time limit should score comparably to a student who executes the repair without clearly documenting the reasoning. Evidence-based systematic diagnosis is the core competency. Repair execution confirms it.

---

### Assessment Criteria

| Criterion | Points | What Is Assessed |
|-----------|--------|-----------------|
| Bench setup and communication | 10 | Correct ECU bench connections derived from wiring diagram; communication established or correctly documented as absent |
| Systematic diagnostic approach | 20 | Logical sequence: DTC reading → hypothesis → measurement → conclusion; written reasoning on assessment form; no random probing |
| Correct fault identification with evidence | 30 | Fault correctly identified; supporting measurements (voltage, resistance, scope) recorded; root cause clearly stated |
| Correct repair or documented repair plan | 30 | Repair executed and verified, or — if parts unavailable — correct procedure documented with all steps, tools, and verification method |
| Safety practices throughout | 10 | ESD protocol maintained; SRS protocol if applicable; current limits observed; no unsafe actions |
| **Total** | **100** | |
| **Pass mark** | **70** | |

---

### Fault Types Prepared

**Fault Type A — Shorted Bypass Capacitor on 5V Reference Rail:**

A resistor (10–22Ω) or forward-biased small-signal diode is soldered between the 5V reference output and the ground plane, loading the 5V rail below its correct operating voltage.

Symptom: MAP sensor reads low in live data even with ignition on but engine not running. IAT or TPS may also read low if they share the 5V reference. DTC: P0107 (MAP circuit low input), P0122 (TPS low input), or manufacturer equivalent.

Expected diagnostic path: DTC reading → live data shows multiple sensors reading low → 5V reference voltage measurement at sensor connector confirms low voltage → ECU supply confirmed at 12V (fault is not in supply) → trace 5V reference fault to ECU origin → component-level measurement identifies the shorted bypass capacitor.

Repair: Remove planted resistor/diode. Verify 5V reference returns to 4.95–5.05V. Confirm DTCs clear.

---

**Fault Type B — Failed Low-Side Injector Driver (Open Circuit):**

The low-side driver for injector 2 (or equivalent — injector driver IC output or MOSFET) is disconnected from the injector connector pin. Method: cut a small PCB trace (restorable by bridging with solder) in the injector 2 drive path.

Symptom: Injector 2 DTC (P0202 or equivalent — open circuit). All other injectors operate normally. On oscilloscope: injector 2 connector shows no switching waveform while injectors 1, 3, 4 show normal peak-and-hold patterns.

Expected diagnostic path: DTC → injector 2 → injector coil resistance at connector is normal (9–16Ω, confirming the injector is intact) → oscilloscope on injector connector: no switching waveform on injector 2 ground side → other injectors switch normally → fault is in ECU driver path → trace from connector back to ECU → open circuit in PCB trace.

Repair: Bridge the cut trace with solder. Verify injector 2 switching waveform appears on oscilloscope. Confirm DTC clears.

---

**Fault Type C — Corrupted Firmware (Boot Mode Recovery Required):**

The ECU FLASH has been partially corrupted. Method: write a firmware file of incorrect length to the ECU, or write all-zeros to the first 4KB of FLASH, corrupting the bootloader jump table.

Symptom: No OBD communication on any protocol. Scan tool cannot detect the ECU. ECU receives power (bench supply current is normal). No CAN transmission from the ECU visible on oscilloscope.

Expected diagnostic path: No communication → verify bench setup is correct (all wiring diagram connections made; power supply current confirmed appropriate for powered-but-not-communicating ECU) → CAN bus oscilloscope: bus is physically intact; other nodes communicate; no frames from ECU node → conclude ECU firmware is non-functional → identify boot mode access pins from wiring diagram or Module 6 reference → access boot mode via SPI, BDM, or JTAG → read FLASH to confirm corruption → write correct firmware file → verify OBD communication restored after power cycle.

Repair: Boot mode firmware recovery (Module 6 skills). Verify scan tool communication after reflash.

---

**Fault Type D — Failed CAN Transceiver on BCM (Bus Remains Active):**

The BCM's CAN transceiver IC has been disabled. Method: solder a 470Ω resistor across CANH and CANL output lines of the transceiver (defeats differential drive capability without hard-shorting the bus), or open the TX path from MCU to transceiver.

Symptom: Communication DTCs for BCM in engine ECU and other modules. BCM does not respond to scan tool. CAN bus oscilloscope shows normal differential activity from other nodes but no frames from the BCM node ID. Bus termination resistance measures ~60Ω (correct — BCM is not a termination node). Bus voltage levels are normal.

Expected diagnostic path: Communication DTC in other modules → scan tool cannot connect to BCM → BCM power and ground confirmed present (measurement at BCM connector) → scope CAN bus: active traffic from other nodes, no BCM frames → distinguish BCM hardware fault from wiring fault → if BCM power is present and CAN bus is active, fault is inside BCM — CAN transceiver → component-level diagnosis on BCM PCB.

Repair: Replace CAN transceiver IC on BCM PCB. Verify BCM reappears on network. Confirm scan tool can now communicate with BCM.

---

**Fault Type E — Immobilizer / ECU Mismatch (All-Keys-Lost Scenario):**

An ECU-immobilizer assembly has been prepared where the immobilizer EEPROM has had its key slots cleared, or the immobilizer has been replaced with a non-matched donor unit.

Symptom: Engine cranks normally but does not start. DTC: P0513, B2799, or manufacturer-equivalent anti-theft code. Crank-and-stall pattern: RPM briefly appears on scan tool then drops to zero. No injector DTCs. No ignition system DTCs. All sensor live data reads normally.

Expected diagnostic path: No-start complaint → crank-and-stall confirmed → DTC confirms immobilizer fault → confirm transponder responds correctly (using key programmer to read the key) → confirm immobilizer communicates on CAN bus → determine whether mismatch is key-to-immobilizer or immobilizer-to-ECU → propose correct matching procedure. Using the PIN provided in the assessment materials: demonstrate the correct key addition or matching procedure.

Repair: Re-match the immobilizer to the ECU using the scan tool with the provided PIN, or perform EEPROM-based matching as appropriate to the planted fault configuration.

---

### Assessment Fault Preparation — Instructor Checklist

Complete the following at least the day before the assessment:

- [ ] All fault ECUs prepared and bench-tested: confirm each fault is present and diagnosable within 30 minutes using the expected diagnostic path
- [ ] Wiring diagram for each ECU type printed and sealed in envelope; envelope labelled with ECU type only (not fault type)
- [ ] Assessment scoring form printed — one per student
- [ ] Assessment rules sheet printed — one per student
- [ ] Countdown timer confirmed visible to all students
- [ ] All bench equipment confirmed working: scan tools charged, oscilloscopes calibrated, multimeters with fresh batteries, power supplies tested
- [ ] Different fault types assigned to adjacent students — confirm no two adjacent students have the same fault type
- [ ] Assessment answer key prepared (one entry per fault type) — instructor use only; not distributed
- [ ] Boot mode access tools available for Fault C students (EEPROM programmer, BDM probe, or equivalent)
- [ ] Key programmer available for Fault E students; PIN for the Fault E module included in the sealed assessment envelope

---

### Assessment Administration — Setup (10 minutes)

1. Distribute one fault ECU per student. Students must not inspect or connect anything until instructed.
2. Distribute assessment scoring form and rules sheet.
3. Instructor reads the rules aloud:

"This is the final practical assessment for ECU Hardware Repair.

You have 105 minutes. The rules are:

One: this is individual work from this moment. No communication with other students about the fault, the ECU, or your approach. Any collaboration between students results in disqualification of both parties.

Two: you may use any tool at your station. You may use the wiring diagram in the sealed envelope. You may use any reference materials you personally prepared: printed notes, the procedure cards from previous sessions, your own notebook. You may NOT use any internet-connected device.

Three: write your reasoning at every step on the scoring form. The criteria reward documented systematic process — a student who shows clear, evidenced reasoning and runs out of time before completing the physical repair will score better than a student who makes an unsupported guess that happens to be correct. Write as you work.

Four: if you complete the repair before time is called, perform the full post-repair verification sequence and document it on the form. Do not sit idle — use remaining time to confirm your documentation is complete.

Five: when time is called, stop immediately. Put your tools down. Do not continue writing. The form is assessed as it stands at that moment.

Questions about the rules only — not about the ECU or the fault?"

4. Take questions about rules only.
5. Distribute sealed wiring diagram envelopes. Students open envelopes.
6. Set countdown timer to 105 minutes, visible to all.
7. "You may begin."

---

### Instructor Role During the Assessment

The instructor is present throughout the 105-minute period. Role:

- Walk the room continuously; observe safety practice, professional tool handling, and general diagnostic approach
- Do NOT assist with fault diagnosis or suggest approaches; answer only equipment malfunction questions (not technique questions)
- Note observations for each student on a private pad — these inform the safety criterion score (10 points)
- Call time at exactly 105 minutes

**Safety intervention:** If any student performs an unsafe action (ESD breach on a sensitive component, unsafe power supply use, or — if Fault E scenario is on an SRS-adjacent bench — any failure of SRS protocol), intervene immediately and note the incident. Document on the private observation pad.

**Single hint provision (instructor discretion):**

If a student is visibly stuck — has made multiple diagnostic attempts with documented reasoning but has not progressed toward the fault after 75 minutes — a single directional hint (not the answer) may be provided at instructor discretion. A hint is: "Consider what the DTC is telling you about which circuit to measure" or "Have you confirmed the bench setup connections match the wiring diagram exactly?" — not "The fault is on the CAN transceiver."

If a hint is provided, note it on the student's scoring form. Apply a proportional adjustment (typically -5 points) to the systematic approach criterion, since the student required external direction to progress.

---

### Assessment Scoring Form

*Reproduce on A4 — one per student. Front and back if needed.*

---

**ECU HARDWARE REPAIR — FINAL PRACTICAL ASSESSMENT**
**ECUHR Module 9 | Day 20 | v1.0**

```
Student Name: _________________________________ Date: _____________
Fault ECU ID/Label: ____________________________ Start Time: ________
Assessor: _____________________________________ End Time: _________

---

SECTION 1 — BENCH SETUP
Record every connection made and how you verified it.

Connection              | Expected          | Measured/Confirmed  | Result
________________________|___________________|_____________________|________
Battery supply (B+):    | 12V               | _________ V         | PASS/FAIL
Battery ground (B-):    | Continuity        | ___________________  | PASS/FAIL
Ignition (switched):    | 12V key-on        | _________ V         | PASS/FAIL
CAN High (if applicable)| Connected OBD     | Scan tool detect:   | PASS/FAIL
CAN Low (if applicable) | Connected OBD     | ___________________  | PASS/FAIL
Other: ________________ | _________________  | ___________________  | PASS/FAIL

ECU supply current at power-on: __________ mA / A
Communication confirmed by: _____________________________________________

---

SECTION 2 — INITIAL DTC SCAN
Record before any action.

DTC Code       | Description / Interpretation          | Status (Current/Stored/Permanent)
_______________|_______________________________________|___________________________________
_______________|_______________________________________|___________________________________
_______________|_______________________________________|___________________________________
_______________|_______________________________________|___________________________________

---

SECTION 3 — DIAGNOSTIC REASONING
Write your reasoning at each step. What did you observe? What does it mean? What do you test next?

Step:        Observation: _______________________________________________
             Conclusion / Hypothesis: ___________________________________
             Next test: ________________________________________________
             Result: ___________________________________________________

Step:        Observation: _______________________________________________
             Conclusion / Hypothesis: ___________________________________
             Next test: ________________________________________________
             Result: ___________________________________________________

Step:        Observation: _______________________________________________
             Conclusion / Hypothesis: ___________________________________
             Next test: ________________________________________________
             Result: ___________________________________________________

Step:        Observation: _______________________________________________
             Conclusion / Hypothesis: ___________________________________
             Next test: ________________________________________________
             Result: ___________________________________________________

(Continue on reverse if needed)

---

SECTION 4 — FAULT IDENTIFICATION

Root cause fault — be specific (component, location, fault mechanism):
___________________________________________________________________________
___________________________________________________________________________

Supporting evidence:
Evidence 1 (measurement/DTC): _____________________________________________
Evidence 2 (measurement/observation): ______________________________________
Evidence 3 (measurement/observation): ______________________________________

---

SECTION 5 — REPAIR PROCEDURE
List all steps performed or proposed.

Step 1: ___________________________________________________________________
Step 2: ___________________________________________________________________
Step 3: ___________________________________________________________________
Step 4: ___________________________________________________________________
Step 5: ___________________________________________________________________
Tool(s) used: ______________________________________________________________

---

SECTION 6 — POST-REPAIR VERIFICATION

Post-repair DTC scan result: _______________________________________________
Communication confirmed after repair: YES / NO
Fault DTC cleared and did not return: YES / NO / NOT APPLICABLE (reason: ___)

Verification steps completed:
[ ] ESD protocols maintained throughout
[ ] Squib resistance checked (if SRS circuit disturbed)
[ ] Power reconnected correctly after repair
[ ] Scan tool re-scan confirms no active faults (or documented exceptions)
[ ] All connectors reseated; wiring confirmed correct

---

SECTION 7 — SAFETY PRACTICES (self-declaration)

ESD wrist strap worn throughout: YES / NO / LAPSE (describe: _______________)
Components stored on ESD-safe surface when not in use: YES / NO
Power supply current limit set appropriately: YES / NO
Any other safety observations: _____________________________________________

---

FOR ASSESSOR USE ONLY

Criterion 1 — Bench setup:                   ______ / 10
Criterion 2 — Systematic diagnostic approach: ______ / 20
Criterion 3 — Fault identified + evidence:    ______ / 30
Criterion 4 — Repair / repair plan:           ______ / 30
Criterion 5 — Safety practices:               ______ / 10

TOTAL:                                         ______ / 100

RESULT: PASS (70+) / FAIL (<70) / REFER (borderline)

Hint provided? YES / NO   Points adjustment applied: _______

Assessor: _____________________________ Signature: ________ Date: _______

Assessor notes:
___________________________________________________________________________
___________________________________________________________________________
```

---

### Assessment Grading Rubric — Detailed

**Criterion 1: Bench Setup and Communication (10 points)**

| Score | Evidence Required |
|-------|-------------------|
| 9–10 | Every connection derived from wiring diagram and recorded with verification. ECU communicates, or student documents correctly that communication is absent and explains why (e.g., Fault C: firmware corrupted; scan tool connection documented as expected non-functional). |
| 6–8 | Setup substantially correct. One minor connection omission or delayed self-correction. Communication established. |
| 3–5 | Setup generally correct but student cannot articulate which connection achieves what, or takes extended time without reference to wiring diagram. |
| 0–2 | Setup significantly incorrect. Multiple connections wrong or missing. Student could not establish communication without instructor guidance. |

**Criterion 2: Systematic Diagnostic Approach (20 points)**

| Score | Evidence Required |
|-------|-------------------|
| 17–20 | Documented logical sequence visible on form: DTC reading → hypothesis formed from DTCs → measurement targeted at hypothesis → measurement result either confirms or eliminates hypothesis → next hypothesis → eventually reaches correct fault. No random probing. Split-half or systematic exclusion logic visible. |
| 12–16 | Mostly systematic. One or two steps not clearly reasoned in writing. General direction correct and reaches correct area. |
| 7–11 | Mix of systematic and opportunistic testing. Some reasoning present. Reached correct area but through partially random process. |
| 3–6 | Largely random testing. Limited written reasoning. Some measurements taken without clear prior hypothesis. |
| 0–2 | No systematic approach. Random component testing. No written reasoning connecting observations to tests. |

**Criterion 3: Correct Fault Identified with Evidence (30 points)**

| Score | Evidence Required |
|-------|-------------------|
| 26–30 | Fault correctly identified with specific component, location, and fault mechanism stated. Evidence includes: correct DTC interpretation, at least two supporting measurements (voltage, resistance, waveform) that confirm the stated root cause. Evidence is unambiguous and would stand as a workshop repair record. |
| 20–25 | Fault correctly identified. Evidence present but one measurement missing or not fully interpreted in writing. |
| 12–19 | Fault partially identified — correct system and module but wrong component, or correct component but incorrect fault mechanism. Evidence supports the partial identification. |
| 5–11 | Identified wrong system or wrong fault type but demonstrated some measurement-based reasoning that moved toward the correct area. |
| 0–4 | Fault not correctly identified. No supporting measurement evidence. Conclusion appears to be a guess. |

**Criterion 4: Correct Repair or Documented Repair Plan (30 points)**

| Score | Evidence Required |
|-------|-------------------|
| 26–30 | Correct repair fully executed and post-repair verification confirms fault resolved. DTC does not return. OR: for parts-unavailable faults, a complete documented repair procedure with every step, required tools, verification method, and expected outcome — procedure is correct for the identified fault. |
| 20–25 | Repair executed and substantially correct. Minor execution error self-identified and corrected. Post-repair verification attempted. OR: procedure documented with one minor omission. |
| 12–19 | Repair procedure generally correct but missing one or two steps. Executed without full verification. OR: procedure documents high-level intent correctly but lacks specifics. |
| 5–11 | Repair attempted with significant errors, or proposed procedure contains significant errors. Some evidence of correct intent. |
| 0–4 | Incorrect repair proposed or executed. No procedure documented. Repair executed without verification. |

**Criterion 5: Safety Practices (10 points)**

| Score | Evidence Required |
|-------|-------------------|
| 9–10 | ESD wrist strap worn throughout entire assessment. ECU handled by board edges. ESD-sensitive components on anti-static mat when not in active use. Power supply current limit set appropriately and confirmed before power-on. No unsafe actions observed. |
| 7–8 | ESD protocols mostly observed. One minor lapse (brief component placement on non-ESD surface) noted but corrected. No dangerous incidents. |
| 4–6 | ESD wrist strap worn but one notable uncorrected lapse. No dangerous incidents. |
| 1–3 | Multiple ESD lapses. No instructor intervention required but practices consistently below professional standard. |
| 0 | ESD wrist strap not worn for significant portion of assessment, OR dangerous tool use observed, OR instructor intervention required for safety. Student cannot pass this criterion regardless of total score. |

---

### Assessment Moderation Guidance

**Borderline cases (65–74 points):**

Review the scoring form in detail. A student who demonstrated clearly systematic diagnostic reasoning and correctly identified the fault (potential for 50 points from Criteria 2+3 combined) can pass even with incomplete repair execution. Ensure Criteria 2 and 3 have been fully credited before concluding a student has failed.

**Safety criterion: zero score implications:**

A student who receives zero for Criterion 5 (Safety Practices) cannot pass the assessment, regardless of total score. ECU repair without ESD discipline does not meet the minimum professional standard for this course. This student is offered a reassessment opportunity with specific briefing on safety protocols.

**Hint provision adjustment:**

Where a hint was provided and documented, reduce Criterion 2 (Systematic Approach) by 5 points maximum. Do not reduce other criteria. The hint indicates the student required external direction to progress — the systematic approach criterion appropriately reflects this.

**Appeals procedure:**

All assessment scoring forms are retained for minimum 6 months. Students may request a scoring review within 14 days of receiving their result. The assessor's written notes on the scoring form constitute the record for any review.

**Resit policy:**

Students scoring below 70 points are offered one reassessment attempt using a different fault type from the remaining prepared pool. The resit window is within 30 days of the original assessment date. The same full assessment format applies.

---

## Debrief and Course Close

### Immediate Post-Assessment Debrief (10 minutes)

Do not reveal individual results immediately.

"Assessment complete. Before I collect the forms, I want to say something about the last 105 minutes.

Every fault type in this assessment was designed to be diagnosable using the framework we established on Day 5: bench setup first, communication second, DTCs third, measurement-based hypothesis testing, isolation, repair, verify. The students who applied that framework — even those who ran short of time — will have produced a diagnostic record that is coherent, defensible, and representative of professional ECU repair.

The students who jumped to component replacement without measurement evidence may have found the right component by chance. Or they may not have. In the real workshop, you will not always guess correctly. The process is the protection.

Without telling me the answer: what fault type do you think you had? Take a moment."

Allow 30 seconds of silence.

"Who wants to tell me?"

Take 3–4 responses. Then reveal the five fault types that were in use. Ask: how many correctly identified their fault type? (Show of hands.) For those who did not: what would you do differently in the first 10 minutes of the diagnostic process?

Take 3–4 responses. Use these to reinforce the systematic approach — not to evaluate individuals publicly.

---

### Course Close (5 minutes)

"Day 20. The final session.

Twenty days ago, most of you could use a scan tool and had a basic understanding of ECU function. Where you are now is a different place.

You can set up a bench ECU correctly from a wiring diagram. You can solder SMD components under magnification and know the difference between a good joint and a cold one. You can read a CAN bus waveform on an oscilloscope and tell whether it is dominant, recessive, or corrupted. You can extract a EEPROM, recover a firmware, diagnose an injector driver fault, and programme an immobilizer. And you understand that SRS work requires a protocol that is not negotiable — and why.

What the course cannot give you is hours. That comes from the work. Every unusual fault will add to your diagnostic pattern library. Every time your first hypothesis is wrong, you learn something more valuable than a correct first guess would have given you.

The one principle I want you to take from this course above everything else: protect the information that already exists before you change anything. Read the DTC before you clear it. Save the EEPROM before you write it. Note the connector position before you remove it. The data that is already there is almost always the most useful information you have.

You have the foundation. Go build the hours."

---

## Equipment and Materials

### Airbag Repair Lab (Part 1)

**Per student pair station:**
- Donor SRS ACU module with planted fault (Fault A or Fault B) — 1 per pair
- Dummy resistive loads for all squib connector pins — must simulate 2–3Ω; NEVER real squibs
- High-impedance multimeter (input impedance >10MΩ) — 1 per station
- Oscilloscope with CAN probes (Fault B stations)
- ESR meter (Fault A stations)
- Bench power supply with correct module connector cable
- Scan tool with SRS module access (Autel MaxiSYS, Launch X431, or equivalent)
- Soldering station (temperature-controlled)
- Hot air station
- Flux, solder, solder wick, IPA, cotton swabs
- Anti-static mat and wrist strap
- Magnifying loupe or USB microscope
- Replacement capacitor (correct µF, voltage, 105°C rating) — Fault A stations
- Replacement CAN transceiver IC (TJA1040/TJA1050 SOIC-8) — Fault B stations
- Checkpoint card — 1 per student pair

**For Crash Data Reset Demo and Module Programming (Activity 3):**
- Prepared SRS module with soft fault DTCs only (pre-verified no deployment record)
- Crash data reset tool (AirBag Reset Tool, Autel MaxiSYS with IMMO/SRS function, or equivalent)
- Replacement SRS module of same type for programming demonstration
- Scan tool with SRS module coding capability

### Final Assessment (Part 2)

**Per student:**
- Fault ECU of assigned type — verified working fault
- Wiring diagram for the ECU type — in sealed envelope labelled with ECU type only
- Assessment scoring form — 1 per student
- Assessment rules sheet — 1 per student
- Bench power supply
- Multimeter
- Oscilloscope
- Scan tool — charged and with correct vehicle coverage for the fault ECU type
- Anti-static mat and wrist strap
- Soldering station and hot air (available at station; not pre-required)
- EEPROM programmer with boot mode access tools (available for Fault C and Fault E)
- Key programmer (available for Fault E)
- Countdown timer — clearly visible to all students from their seated position

---

## Safety Notes — Complete Session

### SRS Specific (Part 1)
- **Mandatory and non-negotiable:** Bench supply off + 60-second minimum wait before any SRS module is touched
- **No real squibs or pyrotechnic components under any circumstances in this lab.** All squib circuit connections terminate in dummy resistive loads (2–3Ω resistors). Instructor must physically verify this for every station before power is applied to any module.
- **Squib resistance measurement tool:** High-impedance multimeter only (>10MΩ). No test lights, no buzzers, no low-impedance resistance measurement on squib circuit pins.
- **If any student handles SRS component without completing the protocol:** Stop the session immediately. Address the behaviour directly. Reset the protocol and restart the sequence. This is a hard stop — not a verbal reminder and continue.
- **Student-to-instructor ratio:** Maximum 6:1 during Part 1 SRS work. If class size exceeds this ratio, an assistant instructor must be present.

### General Lab (Parts 1 and 2)
- ESD wrist straps worn at all times when handling PCBs and ECU modules
- Bench power supply current limits set before powering any module
- No student-to-student assistance or discussion on fault diagnosis once the assessment begins
- All bench areas cleared of non-relevant components before assessment ECUs are issued

---

## Instructor Notes — Managing Day 20

**The dual structure challenge:**

Day 20 is the highest-intensity day of the course. The session runs from morning theory through a 3-hour hands-on lab and assessment. The typical instructor day for Day 20:

- SESSION-20T theory: 60 minutes on feet, delivering dense content
- Break: 10 minutes
- Part 1 SRS lab: 60 minutes on feet, circulating continuously
- Break/transition: 5 minutes
- Assessment setup: 10 minutes
- Part 2 assessment: 105 minutes on feet, observing continuously
- Debrief and course close: 15 minutes

This is approximately 4.5–5 hours of active, high-attention instruction. Prepare accordingly.

**On the SRS safety protocol:**

If any student treats the safety protocol as procedural overhead rather than protective engineering, stop and address it in the moment. Do not let it pass with a correction-and-continue. The wait period is not optional. Real workshop injuries involving SRS capacitor discharge have occurred. Students must leave Day 20 with a genuine respect for this work — not fear, but the kind of disciplined respect that makes every step of the protocol automatic and non-negotiable.

**On the Final Assessment:**

Students will vary widely in how quickly they proceed. Some will identify the fault and complete the repair in 45–60 minutes. Some will use the full 105 minutes and not complete the physical repair. This variation is expected and is not a grading consideration in itself — the assessment is not a speed test. The student who takes 90 minutes to correctly and completely identify and document the fault will score better than the student who makes an unsupported guess and replaces the wrong component in 20 minutes.

**On written feedback:**

Within 24 hours of the assessment (same day if class size and time permit), provide each student with written individual feedback:
- What was done well — be specific ("Your bench setup section was complete and your 5V reference voltage measurement directly confirmed the fault location")
- One specific area for improvement — not generic ("Consider recording your hypothesis explicitly before each measurement — it strengthens the reasoning trail")
- Grade and pass/fail status

Students in this course have invested significant time and in most cases significant money. They deserve honest, specific, constructive feedback — not generic praise. Generic praise is not feedback.

---

## Assessment Alignment — Complete Session

| SO | Assessment Method | Evidence |
|----|------------------|---------|
| so-9-3-4 | Checkpoints 1 and 2 | Fault diagnosed with measurements; faulty component correctly identified; component replaced; DTC resolved post-repair |
| so-9-4-1 | Checkpoint 3 observation | Student observes crash data reset demonstration; correctly explains the hard/soft fault distinction in debrief |
| so-9-4-2 | Checkpoint 3 observation | Student observes replacement module programming; correctly describes coding and verification steps in debrief |
| so-9-4-3 | Checkpoint 3 verbal | Student correctly lists all post-repair safety verification steps without reference material |
| Final Assessment SOs (co-1 to co-4) | Assessment scoring form + assessor observation | Scored against rubric criteria 1–5; assessor notes supplement written evidence |

---

*Module 9 | Day 20 Hands-On + Final Assessment | ECUHR | v1.0 | 2026-02-18*
