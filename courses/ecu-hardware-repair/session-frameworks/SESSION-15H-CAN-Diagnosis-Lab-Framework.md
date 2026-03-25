# SESSION-15H — CAN Bus Diagnosis Lab
## Day 15 Hands-on | Module 7: CAN Bus, LIN & Communication Diagnostics

---

**Course:** ECU Hardware Repair (ECUHR)
**Session Code:** SESSION-15H
**Day:** 15 of 20
**Type:** Hands-on Workshop — Bench-based fault diagnosis
**Duration:** 90 minutes
**Delivery:** Students in pairs, instructor circulating

**Session Outcomes:**
- so-7-2-1: Measure CANH/CANL voltage levels and compare to specification
- so-7-2-2: Use oscilloscope to capture CAN waveform and identify a specific fault
- so-7-2-3: Measure CAN termination resistance (~60 Ω) and diagnose missing/double termination
- so-7-2-4: Use scan tool network test to identify a bus-off node

**MO Alignment:** MO 7-2
**CO Alignment:** co-1 (Diagnose ECU faults by applying knowledge of automotive-grade circuit design)

**Prerequisites:**
- SESSION-15T completed (CAN protocol theory, dominant/recessive states, frame fields, error states)
- Module 2 oscilloscope competency verified
- Students have printed CAN frame reference card and fault signatures table from 15T

---

## Lab Overview

Students work in pairs at a pre-wired CAN bench. The bench has three CAN nodes (ECU simulators or real ECUs on a bench harness). Each bench operates in four phases:

| Phase | Time | Activity | Outcome Addressed |
|-------|------|----------|-------------------|
| Setup and baseline | 0–15 min | Power up bench, verify healthy bus, record baseline measurements | so-7-2-1 |
| Oscilloscope fault capture | 15–45 min | Instructor plants one of four fault conditions; students capture and identify | so-7-2-2 |
| Termination resistance diagnosis | 45–65 min | Four termination scenarios, measure and diagnose each | so-7-2-3 |
| Scan tool network test | 65–85 min | Bus-off node identification with scan tool | so-7-2-4 |
| Debrief | 85–90 min | Whole-class discussion of findings | All |

---

## Bench Setup Specification

### Hardware Required per Bench (2 students)

**CAN Network Components:**
- 3 x CAN node units — any of the following configurations work:
  - Option A: Three Arduino-based CAN node simulators (MCP2515 + TJA1050 transceiver, built in Module 4 lab)
  - Option B: Two bench-test ECUs (engine ECU + BCM or similar) plus one CAN node simulator
  - Option C: Commercial CAN training bench (Bosch, Delphi, or equivalent)
- CAN bus backbone wiring: 1 m twisted pair, minimum 2 connection points accessible for probing between each node
- 2 x 120 Ω termination resistors, mounted on removable plugs (not soldered permanently — must be easy to add/remove)
- Additional 120 Ω resistor plug (for planted extra termination scenario)

**Power:**
- 1 x bench DC power supply (12–14 V, 5 A minimum)
- Power distribution rail to all three nodes
- Ignition line (switched 12 V) — use toggle switch on bench

**Measurement Equipment:**
- 1 x 4-channel oscilloscope (2-channel minimum acceptable)
- Oscilloscope probes: at least two with ground clips
- 1 x digital multimeter with test leads
- 1 x OBD interface cable adapted to bench connector (or CAN interface directly)
- 1 x laptop or tablet with scan tool software (VCDS, ISTA, or OBD-capable generic software)
- CAN bus test points: labelled T-junction test points accessible between each node and bus backbone, without disconnecting the node

**Fault Injection Provisions (instructor prepared before session):**
- Labelled fault switches or jumpers for each fault scenario (see below)
- Fault envelope per bench: sealed, containing one fault card (student opens at Phase 2)

**Consumables and References:**
- Printed wiring diagram for the bench topology (one per student)
- Printed CAN voltage reference card (from 15T)
- Printed fault signatures table (from 15T)
- Lab worksheet (one per student — see Assessment section)

---

### Bench Topology Diagram

Instructor must draw or print this for students:

```
  12V Supply
      │
      ├──────────────────────────────────────────────────────┐
      │                                                      │
  [Node A]        [Node B]        [Node C]            [Termination]
  (CAN Node 1)    (CAN Node 2)    (CAN Node 3)
      │                │                │
  CANH ──T1────────T2──────────T3────────── [Term R1: 120Ω]
  CANL ──T1────────T2──────────T3────────── [Term R2: 120Ω]
                                           (at far end)

  T1, T2, T3 = accessible test points (BNC or 4mm banana on each wire)
  Term R1 = removable plug at Node A end of bus
  Term R2 = removable plug at far end of bus (Node C side)

  Fault injection points:
  F1: CANH-CANL short jumper (between T2 and T3)
  F2: Node B disconnect (pull Node B off bus, leaving T2 accessible)
  F3: Termination plug sockets (add/remove termination plugs)
  F4: Node C stuck-dominant fault (fault switch on Node C transceiver enable pin)
```

**Instructor setup note:** Before the session, verify all three nodes communicate correctly with no planted faults. Confirm the scan tool can see all three nodes. Record the baseline fault-free scan as the reference.

---

## PHASE 1 — Setup and Baseline Measurement (0–15 minutes)

### Instructor Introduction (2 minutes)

"Your bench has three CAN nodes wired on a bus. Before you touch any fault, your first job is to understand what healthy looks like. You cannot identify a fault if you do not have a baseline.

Both terminators are installed. All three nodes are active. Ignition is on."

### Student Procedure — Phase 1

**Step 1.1 — Power Up**
- Set bench supply to 12.5 V
- Turn on ignition switch
- Verify all three CAN nodes show active LED or power indicator
- Note any DTCs on scan tool before measurement — record in worksheet

**Step 1.2 — Multimeter DC Voltage Measurement (Healthy Bus)**
- Set multimeter to DC voltage, 20 V range
- Probe CANH to chassis ground at test point T2 (mid-bus)
- Record voltage: expected 2.4–2.6 V (idle/recessive state)
- Probe CANL to chassis ground at T2
- Record voltage: expected 2.4–2.6 V (idle/recessive state)
- Probe CANH to CANL (differential): expected near 0 V when idle (bus recessive)

**Checkpoint 1A:** Both readings should be within 0.2 V of 2.5 V. If significantly different, call instructor before continuing.

**Step 1.3 — Oscilloscope Setup for CAN Capture**
- Channel A: probe tip to CANH at T2, ground clip to chassis ground
- Channel B: probe tip to CANL at T2, ground clip to same chassis ground
- Set both channels to 1 V/div, position CANH trace in upper half of screen, CANL trace in lower half
- Timebase: start at 500 µs/div — wide enough to see frame gaps
- Trigger: Channel A, falling edge, threshold 2.0 V
- Activate math channel: Math = Channel A minus Channel B (differential view)

**Step 1.4 — Capture Healthy Waveform**
- Once triggered and stable, zoom timebase to 50 µs/div to see individual frames clearly
- Sketch or photograph the waveform in worksheet
- Annotate: CANH trace, CANL trace, differential trace
- Record peak voltages: CANH dominant peak, CANL dominant trough, recessive level on both
- Expected: CANH dominant ~3.5 V, CANL dominant ~1.5 V, recessive both ~2.5 V, differential ~2 V dominant, ~0 V recessive

**Checkpoint 1B — Complete before Phase 2:**
- [ ] Healthy CANH voltage recorded
- [ ] Healthy CANL voltage recorded
- [ ] Healthy waveform sketch with field annotated
- [ ] Scan tool showing all three nodes, no communication DTCs

---

## PHASE 2 — Oscilloscope Fault Capture (15–45 minutes)

### Instructor Action at Start of Phase 2

"Open the fault envelope on your bench. Do not show other benches. Read the fault card. Your fault is already planted on the bench — I have set it up while you were doing baseline measurements.

Your job: use only the oscilloscope and multimeter to identify what the fault is. Do not use the scan tool yet. Do not disconnect anything yet. Measure, observe, and document what you see."

### Fault Cards — Four Variants (assign one per bench or rotate)

**Fault Card A: Dominant Stuck**
Instructor pre-action: Enable fault switch F4 on Node C. Node C's transceiver is now holding the bus permanently dominant.
What student should find: CANH stuck at ~3.5 V, CANL stuck at ~1.5 V. No transitions. Differential stuck at ~2 V. Multimeter reads ~3.5 V on CANH and ~1.5 V on CANL continuously regardless of ignition state.
Identification clue: the bus shows dominant state but there are no frame transitions — it is not a frame, it is a stuck level.

**Fault Card B: CANH to CANL Short Circuit**
Instructor pre-action: Insert jumper at F1 (CANH-CANL short between T2 and T3).
What student should find: Both CANH and CANL at ~2.5 V. No differential signal. Multimeter reads ~0 Ω between CANH and CANL. Oscilloscope shows flat lines on both channels, differential = 0 V constantly.
Identification clue: the bus cannot go dominant — it is permanently recessive. Everything looks "quiet" but nothing communicates.

**Fault Card C: One Wire Open — CANL Broken**
Instructor pre-action: Open the CANL wire at test point T3 (break the CANL connection to Node C side — use a removable link).
What student should find: CANH shows normal signal. CANL shows reduced or asymmetric signal. Differential waveform appears but is noisy and reduced amplitude. Communication is intermittent — some frames get through, many fail with CRC errors.
Identification clue: the two channels no longer mirror each other symmetrically. The differential trace is noisy and inconsistent.

**Fault Card D: Missing ACK — Nodes B and C in Bus-Off**
Instructor pre-action: Disconnect Node B and Node C from bus at T2 and T3 (pull them off physically). Only Node A is on the bus.
What student should find: Node A transmits frames. ACK slot stays recessive (no other nodes to acknowledge). Error frame follows each transmission. Node A's error counter rises. Eventually Node A goes bus-off and the bus goes quiet.
Identification clue: regular pattern of frame transmission followed by error flag pattern; then silence. On scan tool, all nodes report as not responding.

### Student Procedure — Phase 2

**Step 2.1 — Read the fault card, do not reveal to other benches**

**Step 2.2 — Oscilloscope measurement**
- Confirm oscilloscope is still set from Phase 1
- Observe the waveform. Compare to the healthy baseline.
- Record in worksheet: what has changed from the healthy waveform?
- Measure and record: CANH voltage, CANL voltage, differential amplitude, presence or absence of transitions

**Step 2.3 — Multimeter measurement**
- Bus energised (ignition on): measure CANH to ground, CANL to ground
- Record the readings
- If transitions are absent or unusual: measure CANH to CANL directly

**Step 2.4 — Diagnosis**
- Complete the fault diagnosis section of the worksheet:
  - "The oscilloscope shows..."
  - "The multimeter measures..."
  - "My diagnosis is..."
  - "The mechanism is..." (explain why this fault produces this symptom using theory from 15T)

**Checkpoint 2A:** Before calling instructor, both students must agree on the written diagnosis. Instructor verifies and confirms or redirects.

**Step 2.5 — Instructor confirms fault identity**
Instructor reveals the fault card to the bench. If the diagnosis was correct: proceed to Phase 3. If incorrect: instructor asks guided questions to redirect (see Common Mistakes below) — do not simply tell students the answer, guide them to it.

---

## PHASE 3 — Termination Resistance Diagnosis (45–65 minutes)

### Setup

Instructor resets all fault switches to healthy before this phase. All three nodes reconnected and active.

"In this phase, you will measure the CAN bus termination resistance under four scenarios. This is a measurement you will do on every CAN bus fault investigation before you start disconnecting anything."

### Critical Setup for Resistance Measurement

"Before measuring termination resistance:
1. Ignition OFF
2. Bench power supply OFF
3. Disconnect at least two nodes from the bus (remove Node A and Node B from their T-point connectors)
4. Only the bus backbone and termination resistors should remain in circuit

If you do not disconnect nodes, you will read the internal resistance of those ECUs' CAN transceivers in parallel with the bus termination — and the reading will be meaningless."

### Student Procedure — Four Termination Scenarios

Work through all four scenarios in sequence. For each: disconnect the required items, set the termination as described, measure, record, diagnose.

**Scenario T1 — Normal: Both terminators installed**
Setup: Both 120 Ω termination plugs inserted. Both nodes disconnected.
Measure: CANH to CANL resistance with multimeter in ohms mode.
Expected: 55–65 Ω (120 Ω parallel with 120 Ω = 60 Ω exactly; real-world tolerance allows ±5 Ω)
Diagnosis: Correct. Document as "Termination normal."

**Scenario T2 — Missing one termination (one side)**
Setup: Remove termination plug from Node A end. Only the far-end (Node C side) terminator installed.
Measure: CANH to CANL resistance.
Expected: ~120 Ω (only one 120 Ω resistor in circuit)
Diagnosis: One terminator missing. The bus will function with reduced noise margin. At low speed and short bus runs, communication may appear normal. At high speed or in electrically noisy environments, CRC errors will increase. Document as "One termination missing — 120 Ω read."

**Scenario T3 — No termination**
Setup: Remove both termination plugs.
Measure: CANH to CANL resistance.
Expected: Very high (megaohms) or OL (open loop)
Note: With nodes disconnected, there should be no low-resistance path between CANH and CANL. Some CAN transceivers have weak internal pulls that may give a high reading rather than open.
Diagnosis: No termination. Severe signal reflections. Communication will be unreliable or completely absent.

**Scenario T4 — Extra termination (three resistors)**
Setup: Both standard termination plugs installed PLUS one extra 120 Ω plug added at T2 (mid-bus).
Measure: CANH to CANL resistance.
Expected: ~40 Ω (three 120 Ω resistors in parallel)
Diagnosis: Over-terminated. Current draw on the bus is too high. Dominant bit voltage amplitude is reduced because the termination is too low a resistance — the CAN transceiver cannot drive the bus fully to 3.5 V / 1.5 V against a 40 Ω load. Communication may be unreliable.

**Step 3.5 — Reconnect nodes and verify**
After completing all four measurement scenarios:
- Reinstall both standard termination plugs only
- Reconnect all three nodes
- Power up bench
- Verify scan tool sees all three nodes and no DTCs

**Checkpoint 3A:** Worksheet entries for all four scenarios complete with: setup description, measured Ω, diagnosis, and expected effect on communication.

---

## PHASE 4 — Scan Tool Network Test: Finding the Bus-Off Node (65–85 minutes)

### Instructor Setup for Phase 4

Before students start: plant a bus-off condition.
Method: Enable fault switch F4 (Node C stuck dominant) briefly — 2–3 seconds while the bus is active. This will drive error counters up on the other nodes. Some simulators will go bus-off. Alternatively: briefly disconnect and reconnect Node C with its transceiver in error-inject mode.

If using real ECUs: program Node B to transmit malformed frames with a test script, then allow error counters to escalate. Power cycle once bus-off is confirmed on at least one other node.

Target state entering Phase 4: One node (Node B or Node A) is in bus-off state. Node C may or may not be active. Scan tool cannot see the bus-off node.

### Student Procedure — Phase 4

**Step 4.1 — Initial scan tool survey**
- Connect scan tool to bench OBD adapter
- Run full network scan (all modules/systems)
- Record: which nodes respond, which do not respond
- Record: any communication DTCs stored in responding nodes

**Step 4.2 — Verify power and ground on non-responding node**
Using multimeter with bench diagram:
- Probe battery supply pin of the non-responding node: expected ~12.5 V
- Probe ground pin of the non-responding node: expected <0.1 V (confirm good ground)
- Record: "ECU has power: YES/NO. ECU has ground: YES/NO."

Purpose: establish that the non-responding node is not unpowered or missing ground — those would be different faults requiring different approaches.

**Step 4.3 — Oscilloscope check of bus state**
- With all nodes powered and connected: observe bus on oscilloscope
- Is the bus: active with frames? Stuck dominant? Stuck recessive? Silent?
- Record waveform state

**Step 4.4 — Selective node disconnection**
Starting with the node that appeared most suspicious based on the initial scan:
- Disconnect Node C from the bus at its T-point connector
- Power-cycle the bench (ignition off, 10 seconds, ignition on)
- Run full network scan again
- Record: did the bus recover? Can the previously non-responding nodes now be seen?

If bus recovered after disconnecting Node C: Node C was the fault cause. Document.
If bus did not recover: reconnect Node C, disconnect Node B, power-cycle, re-test.
Continue until the fault-causing node is isolated.

**Step 4.5 — Root cause classification**
Once the fault-causing node is identified, use the oscilloscope on that node's transceiver output (probe directly at the transceiver IC output pin if accessible) to determine:
- Is the node's transceiver stuck driving dominant? (hardware transceiver failure)
- Is the node transmitting continuously with malformed frames? (software or firmware fault)
- Is the node passive and not responding but not pulling the bus down? (bus-off state — different cause required)

Document the root cause classification in the worksheet.

**Checkpoint 4A — Required before debrief:**
- [ ] Initial scan recorded with which nodes responded and which did not
- [ ] Power and ground verification on non-responding node recorded
- [ ] Bus waveform state at start of Phase 4 recorded
- [ ] Systematic disconnection sequence documented (which node disconnected first, second, result of each)
- [ ] Fault-causing node correctly identified
- [ ] Root cause classified: wiring fault / transceiver failure / ECU hardware fault

---

## DEBRIEF (85–90 minutes)

Instructor-led, whole class.

**Question 1 (Phase 2 debrief):** "How many benches diagnosed their Phase 2 fault correctly on first attempt? What measurement was the most useful — the oscilloscope or the multimeter? Why?"

**Question 2 (Phase 3 debrief):** "What resistance did you measure with no termination resistors? Why is that result significant if you measured it on a real vehicle?"
Expected answer: Very high/open. On a vehicle, a very high reading means termination resistors are missing or the bus backbone is broken — the bus wire itself is open, not just the termination.

**Question 3 (Phase 4 debrief):** "At the start of Phase 4, the non-responding node had power and ground. Does that eliminate the possibility that the ECU hardware is faulty?"
Expected answer: No — the ECU could be in bus-off (CAN controller offline, ECU itself still running), or the transceiver IC could be the failed component while the rest of the ECU operates. Hardware fault diagnosis is a separate step after confirming the bus is healthy.

**Key takeaway to state explicitly:**
"Your investigation sequence for any CAN communication fault is always the same: first, measure the bus itself — voltage levels, waveform, termination. Then use the scan tool to survey which nodes respond. Then verify power and ground on non-responding nodes. Only then start disconnecting nodes systematically. This sequence prevents you from replacing parts that were not faulty."

---

## LAB WORKSHEET

### Student Name: ________________  Partner: ________________  Bench: ______  Date: ________

**Phase 1 — Baseline**

| Measurement | Result | In Spec? (Y/N) |
|-------------|--------|----------------|
| CANH voltage (recessive/idle) | | |
| CANL voltage (recessive/idle) | | |
| CANH voltage (dominant peak) | | |
| CANL voltage (dominant trough) | | |
| Differential voltage (dominant) | | |
| Differential voltage (recessive) | | |

Healthy waveform sketch (attach oscilloscope screenshot or hand sketch):

[Space for sketch]

---

**Phase 2 — Fault Identification**

Fault card letter: ______

Oscilloscope observation (describe what changed from healthy baseline):

Multimeter reading (CANH to ground, CANL to ground, CANH to CANL):

My diagnosis (fault name): ______________________________

Mechanism explanation (why does this fault produce these symptoms):

Confirmed correct by instructor: Y / N
If incorrect, correct diagnosis was:

---

**Phase 3 — Termination Resistance**

| Scenario | Configuration | Measured Ω | Diagnosis | Effect on Bus |
|----------|---------------|-----------|-----------|---------------|
| T1 | Both terminators | | | |
| T2 | One terminator missing | | | |
| T3 | No terminators | | | |
| T4 | Three terminators | | | |

---

**Phase 4 — Bus-Off Node Identification**

Initial scan tool survey:

| Node | Responds? | DTCs stored in this node? |
|------|-----------|--------------------------|
| Node A | | |
| Node B | | |
| Node C | | |

Power and ground verification on non-responding node:
- Node: _____ Battery supply: _____ V   Ground: _____ V

Bus waveform state at start of Phase 4 (circle): Active and healthy / Stuck dominant / Stuck recessive / Silent / Other: ___________

Disconnection sequence:

| Step | Node Disconnected | Bus Recovered? | Notes |
|------|-------------------|----------------|-------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

Fault-causing node identified: _____

Root cause classification (circle one): Wiring fault  /  Transceiver failure  /  ECU hardware fault  /  Indeterminate — further investigation required

Explain how you reached this root cause classification:

---

## ASSESSMENT CRITERIA

| Criterion | Marks | Notes |
|-----------|-------|-------|
| Phase 1: Baseline measurements complete and in-spec | 10 | All 6 values recorded, CANH/CANL within 0.3 V of spec |
| Phase 1: Healthy waveform correctly annotated | 10 | CANH, CANL, and differential traces identified; dominant/recessive states labelled |
| Phase 2: Fault correctly identified with mechanism explanation | 25 | Correct fault name (15 marks); correct mechanism explanation (10 marks) |
| Phase 3: All four termination scenarios measured and diagnosed | 20 | 5 marks per scenario — correct Ω reading plus correct diagnosis |
| Phase 4: Correct node identified via systematic process | 25 | Process documented (10 marks); correct node identified (10 marks); root cause classified (5 marks) |
| Safety and instrument handling throughout | 10 | No probe damage, correct oscilloscope grounding, power off before resistance measurements |
| **Total** | **100** | Pass: 60 |

---

## EQUIPMENT LIST — Per Bench

| Item | Quantity | Notes |
|------|----------|-------|
| CAN node simulator or bench ECU | 3 | With accessible CAN transceiver output |
| 4-channel oscilloscope (2-channel minimum) | 1 | With math channel capability |
| Oscilloscope probes with ground clip | 2 | 10:1 or 1:1, both acceptable |
| Digital multimeter | 1 | With ohms range and continuity |
| Bench DC power supply (12–14 V, 5 A) | 1 | |
| OBD interface / CAN adapter for scan tool | 1 | |
| Laptop with scan tool software | 1 | |
| 120 Ω termination resistor plugs | 4 | 2 standard + 1 extra for scenario T4 + 1 spare |
| CAN bus wiring with T-point test points | 1 set | T1, T2, T3 accessible |
| Fault switches / jumpers (F1–F4) | 1 set | Pre-installed by instructor |
| Bench wiring diagram (printed) | 2 | One per student |
| CAN voltage reference card (from 15T) | 2 | One per student |
| Fault signatures table (from 15T) | 2 | One per student |
| Lab worksheet | 2 | One per student |
| Fault envelope (sealed) | 1 | Contains fault card for Phase 2 |

---

## COMMON MISTAKES AND INSTRUCTOR RESPONSES

**Mistake: Student measures CANH voltage as ~3.5 V on the multimeter and concludes the bus is dominant-stuck.**
Correction prompt: "A multimeter measures the average voltage on an AC-ish signal. On a normal active CAN bus with a 50% duty cycle of dominant/recessive frames, CANH averages somewhere between 2.5 V and 3.5 V — it will never read exactly 2.5 V on a busy bus even when healthy. What should you look at to distinguish between average voltage and stuck dominant?" (Answer: the oscilloscope, which shows whether the voltage is changing over time or fixed.)

**Mistake: Student measures resistance with the bench powered on.**
Response: Stop them immediately. "Power must be off before measuring resistance. If you apply the multimeter ohms range to a powered circuit, you will get a wrong reading and you may damage the meter. Power down, then measure."

**Mistake: Student measures 60 Ω on Scenario T2 (one terminator missing) because they forgot to disconnect one of the node ECUs.**
Correction prompt: "Check what you had disconnected when you made that measurement. Some CAN transceiver ICs have an internal termination resistor or pull — if a node was still connected, it may have added its internal resistance to your measurement."

**Mistake: Phase 4 — student disconnects all nodes at once to "clear the fault" then reconnects one by one.**
Correction prompt: "That approach works eventually, but it is not the same as systematic diagnosis — you cannot document which specific node caused the fault if you disconnected all of them simultaneously. A systematic disconnect-test-reconnect sequence gives you a document trail that a customer, workshop manager, or warranty claim can follow."

**Mistake: Student identifies the bus-off node and immediately recommends ECU replacement.**
Correction prompt: "You have confirmed which node caused the bus to fail. What are the three possible root causes for that node's behaviour? Which of those three requires replacement of the ECU itself, and which ones do not?" (Wire short, transceiver IC failure, ECU internal fault — only the third requires ECU replacement.)

---

## INSTRUCTOR TIMING GUIDE

| Time mark | Action |
|-----------|--------|
| T+0 | Brief introduction, bench check. Confirm all benches have healthy baseline. |
| T+2 | Release students to Phase 1. Circulate to verify oscilloscope setups. |
| T+15 | Distribute fault envelopes. Confirm fault switches on all benches are in correct position. Begin Phase 2. |
| T+35 | Check all benches have a diagnosis attempt in their worksheet. Confirm or redirect as needed. |
| T+45 | Call class back. Instructor resets all bench faults to healthy. Release to Phase 3. |
| T+60 | Ensure all benches have completed at least T1 and T2. Check for measurement errors. |
| T+65 | Release to Phase 4. Set up bus-off condition on each bench while students are reading the Phase 4 instructions. |
| T+82 | Call class back for debrief. |
| T+85 | Debrief discussion. |
| T+90 | End. Collect worksheets. Announce: tomorrow will cover LIN bus and multi-node isolation — review the fault signatures table tonight. |

---

*Framework prepared for ECUHR Module 7, Day 15 Hands-on.*
*Session outcomes: so-7-2-1, so-7-2-2, so-7-2-3, so-7-2-4*
*Date prepared: 2026-02-18*
