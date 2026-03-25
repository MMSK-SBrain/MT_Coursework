# SESSION-16H: LIN Bus Diagnosis & Multi-Node CAN Fault Isolation Lab
## Hands-On Session | Day 16 | Module 7: CAN Bus, LIN & Communication Diagnostics

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 7 — CAN Bus, LIN & Communication Diagnostics
**Day:** 16 | **Session Type:** Hands-On Workshop
**Duration:** 90 minutes
**CO Alignment:** co-1

---

## Session Outcomes

| ID | Outcome | Bloom's Level |
|----|---------|---------------|
| so-7-3-2 | Measure LIN bus signal using oscilloscope and identify healthy frame vs fault condition | Analyze |
| so-7-3-3 | Identify a failed LIN slave node by disconnecting nodes and observing which removal restores bus operation | Apply |
| so-7-4-2 | Isolate the fault-causing node in a 3-node bench CAN network with a planted fault by selective disconnection and bus monitoring | Analyze |
| so-7-4-3 | Document the diagnosis process and correctly identify whether root cause is wiring fault, transceiver failure, or ECU hardware fault | Evaluate |

---

## Timing Overview

| Time | Duration | Activity |
|------|----------|---------|
| 0:00 | 5 min | Briefing, equipment check, safety reminders |
| 0:05 | 35 min | Activity 1 — LIN Bus Diagnosis (two faults) |
| 0:40 | 45 min | Activity 2 — Multi-Node CAN Fault Isolation (assessed) |
| 1:25 | 10 min | Group Debrief |
| 1:35 | 5 min | Clean-up, bench reset, assessment form handover |

---

## Equipment List

### Per Workstation (groups of 2 students)

| Item | Quantity | Specification / Notes |
|------|----------|----------------------|
| Oscilloscope | 1 | 2-channel, 25MHz bandwidth minimum; suitable for both LIN (slow signal, DC to ~20kHz) and CAN (500kbps, requires bandwidth to ~5MHz for clean edge capture) |
| Oscilloscope probes | 2 | 10x probes; ground clips accessible |
| Bench LIN network | 1 | 1 LIN master + 2 slave nodes (see LIN Bench Setup Notes); power supply 12V DC; fault injection switches; accessible LIN test point and slave connector sockets |
| Bench CAN network | 1 | 3-node bench from Session-15H; confirm all fault injection switches are in OFF state at session start; unknown fault will be introduced by instructor during Activity 2 |
| Multimeter | 1 | Standard DMM; resistance and DC voltage functions |
| Scan tool | 1 | CAN network test capability; LIN diagnosis capability is optional (not all scan tools support LIN — confirm before session) |
| LIN reference waveform sheet | 1 set | Laminated — healthy LIN frame, 3 LIN fault conditions (see Appendix A) |
| CAN reference waveform sheet | 1 set | Same laminated set from Session-15H — retain at workstation |
| Topology diagram (A3 print) | 2 | CAN bench topology (3-node) for student reference during Activity 2; include node labels, segment boundaries, termination positions, test point locations |
| Activity 1 lab worksheet | 2 | One per student — LIN measurement tables and conclusion fields (see Appendix B) |
| Activity 2 assessment form | 2 | One per student — independent diagnosis form (see Appendix C); this is the primary assessment document for so-7-4-3 |
| Check-off card | 2 | One per student; all 4 SOs tracked |
| CAN test Y-cable | 1 | Allows simultaneous oscilloscope and scan tool connection to CAN bench |
| LIN test probe adapter | 1 | Single banana jack socket tapped onto LIN wire at accessible test point on bench; avoids probing bare wire |

### Instructor Station

| Item | Quantity | Notes |
|------|----------|-------|
| LIN bench master control | 1 | Controls power and fault injection for all LIN workstation benches |
| CAN bench fault injection panel | 1 | Unknown fault activated per workstation for Activity 2; can plant different faults at different workstations for variety |
| Spare TJA1020 LIN transceiver ICs | 5 | For demonstration if a bench IC has failed from wear |
| Timer / countdown display | 1 | Visible to students; used to pace Activity 2 |
| Completed assessment form examples | 1 set | Instructor reference — do not distribute to students |

---

## Safety Notes

1. **LIN bus voltage (12V):** The LIN wire operates at 12V, the same as vehicle battery voltage. This is low-voltage and does not present electrocution risk. Exercise standard ESD precautions when handling PCBs.
2. **Oscilloscope ground reference — LIN measurement:** Connect oscilloscope ground (black clip) to the CAN/LIN bench ground (supply negative). Do NOT connect oscilloscope ground to the LIN wire itself — LIN wire is a signal line at 12V; connecting your oscilloscope ground to a 12V point will short the LIN line to ground through your oscilloscope's ground path, destroying the signal and potentially damaging the bench ECU.
3. **Oscilloscope ground reference — CAN measurement:** As per Session-15H — both probe grounds to CAN network GND, not to each other's signal lines.
4. **Multimeter resistance measurement:** Always power off the bench before measuring resistance. Measuring resistance on a powered circuit gives incorrect readings and may damage the meter.
5. **Connector disconnection (Activity 2):** Students disconnect ECU connectors from bench socket posts only — not from wiring. Confirm the correct connector before disconnecting. Incorrect disconnection may interrupt power supply rather than CAN connection.
6. **Do not modify bench wiring:** Fault injection is performed via switches on the instructor's panel only. Students do not modify wiring, unplug supply leads, or operate fault injection switches without explicit instructor instruction.

---

## LIN Bench Setup Notes (Instructor Pre-Session)

### LIN Bench Architecture

```
  [12V Power Supply]
         |
  [LIN Master Module]----[LIN wire (single core)]----[LIN Slave 1]----[LIN Slave 2]
         |                          |
  (1kΩ pull-up to 12V)    [LIN test point         [Slave connector    [Slave connector
                           banana socket]           socket 1 —         socket 2 —
                           (oscilloscope here)      disconnectable]    disconnectable]
```

**LIN Master Module options:**
- Bench BCM from a scrapped vehicle that has a LIN master port (most convenient — replicates real-world conditions)
- Microcontroller development board (Arduino, STM32, or similar) with LIN transceiver shield and programmed LIN master firmware
- Dedicated automotive LIN master development module (National Instruments, Vector, or equivalent)

**LIN Slave Modules (2 required):**
- Any LIN slave module from a scrapped vehicle: seat motor controller, mirror control module, HVAC damper controller, ambient light controller
- The function of the slave does not matter for this lab — what matters is that it responds to LIN headers with data bytes and a checksum
- Confirm each slave's LIN ID assignment before the session — record on instructor reference sheet

**Fault Injection:**

| Switch | Fault | Mechanism |
|--------|-------|-----------|
| LIN Switch 1 | Slave 2 no response (power loss simulation) | Disconnects 12V supply to Slave 2 only; LIN wire remains connected |
| LIN Switch 2 | LIN wire short to ground | Connects a 10Ω resistor from LIN wire to ground, overcoming the 1kΩ pull-up and pulling the line to near 0V |

**Pre-Session LIN Check:**
- [ ] LIN master powered; confirm LIN waveform visible on oscilloscope at test point (break → sync → ID → slave data bytes)
- [ ] Both slaves responding correctly to their respective IDs (visible on scope and/or LIN diagnostic tool)
- [ ] Both fault switches confirmed in OFF position
- [ ] LIN test point banana socket accessible at each workstation
- [ ] Slave connector sockets 1 and 2 accessible and labelled clearly

### CAN Bench Setup (Refer to Session-15H setup notes)

- CAN bench networks from Session-15H are already in place
- Confirm all fault injection switches are OFF and bus is healthy (60Ω termination, clean waveform, all 3 nodes visible on scan tool)
- Do NOT reveal which fault will be planted for Activity 2 — select and note it privately on instructor sheet before session begins
- For variety across workstations, different faults may be planted at different benches — confirm the instructor panel is labelled clearly by bench number

---

## Session Briefing (5 minutes)

**Instructor delivers standing briefing before students approach workstations.**

Key points:
1. "Today's session has two parts. Part 1 is LIN — a guided activity with two faults. Part 2 is independent CAN fault isolation — this one is assessed. I will not give hints during Part 2."
2. "LIN is a single-wire bus at 12V. Your oscilloscope ground clips must go to the bench GND socket — NOT to the LIN wire. If you put a ground clip on the LIN wire, you short it to ground and you will see a very confusing waveform. Check before you probe."
3. "For Part 2 — the assessment form is your diagnostic record. Write down every measurement you take, what you observed, and why it led you to the next step. A correct conclusion with no supporting evidence scores less than a methodical process with a minor error in the conclusion."
4. "You have the topology diagram for the CAN bench on your workstation. Use it. It tells you which nodes have terminators."
5. Safety reminders — voltage levels, ground reference, no bench wiring modifications, power off before resistance measurements.

---

## Activity 1: LIN Bus Diagnosis (35 minutes)

### Overview

Two LIN faults are introduced in sequence. Students diagnose each fault using oscilloscope, multimeter, and (where applicable) physical disconnection. Each fault is followed by a checkpoint.

**Equipment for Activity 1:**
- Oscilloscope: CH1 to LIN test point (banana socket); CH2 not required (LIN is single-wire); ground clip to CAN/LIN bench GND
- Oscilloscope settings: Time/div = 2ms/div (shows 1–2 complete LIN frames at 10.4kbps); Voltage/div = 5V/div (captures 0–12V LIN swing); Trigger: falling edge on CH1 at 6V (mid-scale) for break detection
- Multimeter: set to DC volts for voltage measurement; resistance (power off) for short-circuit detection

---

### Part 1A: LIN Baseline and Slave 2 No-Response Fault (18 min)

**Step 1: Establish LIN healthy baseline (6 min)**

With all fault switches OFF (healthy operation):

a) Measure LIN wire voltage to ground (multimeter, DC volts):
- Expected: approximately 12V (bus at idle recessive) or a varying average between 0V and 12V during active communication
- Using oscilloscope: idle state between frames shows 12V; during frame bursts, voltage transitions between 0V (dominant) and 12V (recessive)
- Record: idle voltage = ___ V

b) Identify frame structure on oscilloscope:
- Break: the long period at 0V before each frame. At 10.4kbps: 13 bit periods = 13 × 96μs = 1.25ms minimum. Find this on the trace and measure its duration.
  - Expected: ≥ 1.25ms at 0V
  - Record: measured break duration = ___ ms
- Sync byte: following the break, a return to 12V (stop bit), then a series of alternating transitions (0x55 = 01010101). Count the transitions — should be 8 data bit transitions.
- ID byte: follows sync byte. One byte (8 data bits) + start bit + stop bit.
- Slave response: data bytes transmitted by the slave after the ID byte. Check waveform — are bytes present after ID? Count how many.
- Record: number of data bytes observed in response = ___

c) Sketch the waveform in the worksheet sketch box — label break, sync, ID, data bytes, checksum.

d) Checkpoint question: Instructor asks student verbally — "Which part of the frame does the slave transmit?" Student should answer: "The response — data bytes and checksum — the master transmits the break, sync byte, and ID."

**Step 2: Introduce Fault — Slave 2 No Response (12 min)**

Instructor activates LIN Switch 1 (removes power from Slave 2).

**Student observation and diagnosis sequence:**

a) Oscilloscope — still looking at LIN test point:
- Master continues to transmit headers (break + sync + ID cycles)
- LIN trace still shows break, sync byte, and ID bytes — master is working
- For some ID periods: after the ID byte, data bytes appear — these are Slave 1's responses (Slave 1 still works)
- For Slave 2's ID period: after the ID byte, the LIN wire returns to 12V and stays at 12V for the response period — no data bytes visible. This is the "no response" signature.
- Record: Does the LIN frame for Slave 1's ID show data bytes? ___. Does the frame for Slave 2's ID show data bytes? ___.

b) Voltage measurement at Slave 2 connector (without disconnecting):
- Probe the 12V supply pin at Slave 2's connector socket (refer to bench connector pinout sheet at workstation)
- Expected if Slave 2 is powered: 12V
- Actual with LIN Switch 1 active: 0V (power removed)
- Record: Slave 2 supply voltage = ___ V

c) Diagnosis conclusion:
- Slave 2 has no power. This is why it is not responding. The LIN bus is intact (master transmitting, Slave 1 responding). This is a Slave 2 power fault, not a LIN bus fault.
- Possible causes in a real vehicle: blown fuse, broken supply wire, connector corrosion at Slave 2's power pin

d) Test of isolation by disconnection:
- Disconnect Slave 2 connector from its socket post
- Observe scope: does anything change? (No — Slave 2 was already silent. Disconnecting a non-responding, non-transmitting slave does not change bus behaviour. This confirms the slave was not pulling the bus down — it was just absent.)
- Reconnect Slave 2 connector.
- Record: Effect of disconnecting Slave 2 on bus waveform: ___

### Checkpoint 1

**Instructor reviews worksheet:**
- Break duration measurement within ±20% of expected: yes / no
- Correct identification of which ID periods show no slave response: yes / no
- Slave 2 supply voltage measured and recorded: yes / no
- Diagnosis: "Slave 2 has no power / is offline — LIN bus is otherwise healthy": correct / incorrect
- Correct interpretation of why disconnecting Slave 2 had no effect: yes / no

**Sign off Checkpoint 1 on check-off card (so-7-3-2 partially satisfied — healthy vs fault waveform identified).**

---

### Part 1B: LIN Wire Short to Ground (17 min)

**Reset:** Instructor deactivates LIN Switch 1. Confirm scope returns to healthy LIN baseline. Then activates LIN Switch 2 (LIN wire short to ground via 10Ω resistor).

**Student observation and diagnosis sequence:**

**Step 1: Oscilloscope — immediate observation (4 min)**

- LIN wire voltage: approximately 0V flat trace (or very low voltage — the 10Ω short pulls the 12V pull-up to near 0V; actual voltage depends on pull-up resistor value)
- No frame structure visible — no break, no sync, no data
- The bus is completely silent at 0V
- Record: LIN wire voltage with fault active = ___ V. Frame structure visible? ___

**Step 2: Voltage measurement with multimeter (2 min)**

- Measure LIN wire to ground (multimeter DC volts, bench powered on):
- Expected with short: approximately 0V (or very low — the 10Ω short nearly pulls the line to ground)
- Record: LIN voltage = ___ V
- Compare to healthy baseline: ___ V

**Step 3: Resistance measurement — short circuit identification (4 min)**

- Power off bench
- Multimeter set to resistance
- Probe: LIN test point (banana socket) to GND
- Expected with short: low resistance (near 0Ω, or the value of the 10Ω short resistor if the fault is a resistive path)
- Expected without short (healthy): high resistance (>10kΩ — the pull-up resistor is the only path, and pull-up resistor value is 1kΩ; if measuring power off, the pull-up to 12V supply is now open-circuit → reading is pull-up resistor to ground through circuit path, typically very high)
- Record: resistance LIN to GND = ___ Ω
- Conclusion: short to ground present? yes / no

**Step 4: Isolation by node disconnection (5 min)**

Power bench back on. The fault persists (LIN wire at 0V). Student must find which node or wire is causing the short.

- Disconnect Slave 1 connector from socket post
- Measure LIN voltage: still ~0V (Slave 1 was not the short)
- Reconnect Slave 1

- Disconnect Slave 2 connector from socket post
- Measure LIN voltage: still ~0V (Slave 2 was not the short either — the fault switch is wired between test point and ground, independent of the slave connectors)

**Instructor note:** In this bench configuration, the short is at the LIN wire level (the fault switch connects the wire directly to ground, not through a slave node). This simulates a chafed wire short rather than a failed transceiver. When neither slave disconnection resolves the short, the conclusion must be: the fault is in the wiring or at a point before either slave connector — i.e., in the harness between the master and Slave 1.

- Power off bench. Measure resistance from LIN test point (master end) to ground: low (confirms short is on the main LIN wire, not inside either slave node).
- Record: after both slave disconnections, resistance LIN to GND = ___ Ω. Conclusion: fault in ___ (wiring / Slave 1 / Slave 2)?

**Step 5: Diagnosis statement (2 min)**

Student writes conclusion on worksheet:
- "LIN wire is shorted to ground. Location: between the master module and Slave 1 connector (based on fault persisting after both slave disconnections). The short is in the harness wiring, not in either slave node. In a real vehicle, inspect the LIN wire harness between the BCM [or master module] and the first LIN slave connector for chafing, pinching, or a faulty connector pin bridging to ground."

### Checkpoint 2

**Instructor reviews worksheet and diagnostic reasoning:**
- Correct oscilloscope observation: LIN stuck at 0V / no frames: yes / no
- Resistance to ground measurement performed power-off, value recorded: yes / no
- Disconnection of both slaves attempted and documented: yes / no
- Correct conclusion: wiring fault (short in harness) rather than slave node fault: yes / no
- Supporting evidence documented (voltage, resistance, disconnection results): yes / no

**Sign off Checkpoint 2 on check-off card (so-7-3-2 and so-7-3-3 satisfied).**

**Transition to Activity 2:** Students confirm CAN bench oscilloscope connections (CH1 = CANH, CH2 = CANL, both grounds to GND). Instructor activates the unknown CAN fault on each bench during the transition.

---

## Activity 2: Multi-Node CAN Fault Isolation — Independent Assessment (45 minutes)

### Purpose

This is the primary assessed activity for the session and the terminal assessment for so-7-4-3. Students work independently from this point — no instructor hints, no peer consultation during the measurement phase. The instructor observes process, not just conclusion.

**The fault is unknown.** It may be any fault type from Session-15H, or a new variant. No information about the fault type is given. Students must apply the systematic process from Session-16T theory to identify the fault independently.

### Assessment Context

- so-7-4-2 (Analyze — isolate fault-causing node): assessed through the disconnection steps and correct node identification
- so-7-4-3 (Evaluate — document process and identify root cause category): assessed through the completed assessment form
- The assessment form (Appendix C) is the primary evidence document. Quality of process documentation matters as much as the final conclusion.

### Instructor Setup

Before Activity 2 begins:
1. Select the unknown fault per workstation from this list:
   - Option 1: Fault A — CANH stuck dominant (transceiver failure)
   - Option 2: Fault B — Missing termination (one terminator removed)
   - Option 3: New fault — CANL stuck dominant (simulated by connecting CANL to a 1.5V reference via low impedance — more challenging)
   - Option 4: Fault C — CANH open circuit between two nodes
2. Note selected fault per bench on instructor sheet (for marking answer key)
3. Activate fault after confirming all students are at CAN bench workstations with scope connected and assessment form ready
4. Announce: "The fault is active. You may begin. You have 35 minutes for diagnosis and 10 minutes to complete the assessment form. Work independently."

---

### Student Independent Diagnosis Procedure

**Instructions printed at top of assessment form (Appendix C):**

> "Work through the steps below in order. Do not skip steps. Record every measurement you take — even if the measurement result seems unimportant. A well-documented diagnosis is more valuable than an undocumented correct answer. You may use: oscilloscope, multimeter, scan tool, bench CAN topology diagram. You may NOT consult your partner or the instructor during the measurement phase."

---

**Phase 1: Initial Characterization (10 min)**

**Step 1.1 — Oscilloscope: Bus Signal Quality**

Connect oscilloscope as per Session-15H training:
- CH1 to CANH test point (banana socket)
- CH2 to CANL test point (banana socket)
- Both ground clips to GND test point

Settings: 200μs/div, 1V/div, trigger Auto on CH1.

Record observations (circle all that apply and describe):

Bus activity:
- [ ] Frames visible — bus is active
- [ ] No frames — bus is dark / silent
- [ ] Error frames visible (repetitive 6-bit dominant sequences)
- [ ] Partial frames visible (frames start but don't complete)

CANH voltage:
- [ ] CANH alternates normally between ~2.5V (recessive) and ~3.5V (dominant)
- [ ] CANH appears stuck at a fixed high voltage (approximately ___ V)
- [ ] CANH appears stuck at ~2.5V (no dominant transitions)
- [ ] Other: _______________

CANL voltage:
- [ ] CANL alternates normally between ~2.5V (recessive) and ~1.5V (dominant)
- [ ] CANL appears stuck at a fixed low voltage (approximately ___ V)
- [ ] CANL appears stuck at ~2.5V (no dominant transitions)
- [ ] Other: _______________

Waveform quality (if frames visible):
- [ ] Clean edges — no ringing
- [ ] Ringing at bit transitions
- [ ] Normal waveform shape

**Step 1.1 Summary — preliminary fault hypothesis from oscilloscope alone:**
______________________________________________________________________

---

**Step 1.2 — Multimeter: Termination Resistance**

Power off bench (flip bench power switch — confirm bench LEDs off).

Measure resistance from CANH test point to CANL test point using multimeter (resistance / ohms setting).

Reading: ___ Ω

Interpretation (circle one):
- ~60Ω: Both terminators present and intact — normal
- ~120Ω: One terminator missing — which end node? To be determined
- ~40Ω: Additional terminator present — abnormal (external device or bench fault)
- Open (>10kΩ): No terminators reachable — bus open circuit or both terminator ECUs disconnected
- Near 0Ω: CANH and CANL shorted together — wiring fault

Power bench back on.

**Updated hypothesis after termination measurement:**
______________________________________________________________________

---

**Step 1.3 — Scan Tool: Network Status**

Connect scan tool via Y-cable (CAN test adapter).
Run network / module list function.

Nodes online (list each node identified): ________________________________
Nodes offline or not responding (list): _________________________________
Any DTCs generated (list U-codes if visible): __________________________

Does the scan tool show a different picture from what the oscilloscope suggested?
______________________________________________________________________

**Updated hypothesis after scan tool network status:**
______________________________________________________________________

---

**Phase 2: Systematic Disconnection (if required) (15 min)**

If the fault has NOT been definitively identified from Phase 1 measurements alone, proceed with selective node disconnection.

If the fault IS clear from Phase 1 (for example: CANH stuck at 3.5V + termination 60Ω + all nodes offline = likely transceiver failure), you may proceed directly to Phase 3 with the reasoning documented.

**Disconnection sequence — consult topology diagram:**

Using the 3-node bench topology diagram, identify:
- Node with terminator at left end: _______
- Node without terminator (middle): _______
- Node with terminator at right end: _______
- Which node to disconnect first (based on findings — most likely culprit, or start at one end): _______

**Disconnection 1:**
- Node disconnected: _______
- Method: pull ECU connector from socket post on bench
- After disconnection — oscilloscope (frames resumed? bus still stuck?): _______
- After disconnection — termination measurement (power off first): ___ Ω
- After disconnection — scan tool (which nodes now visible?): _______
- Bus restored? YES / NO
- If YES: record — "Bus restored after disconnecting [Node X]. This node is the source of the fault."
- If NO: reconnect node; proceed to Disconnection 2.

**Disconnection 2 (if needed):**
- Node disconnected: _______
- After disconnection — oscilloscope: _______
- After disconnection — termination: ___ Ω
- After disconnection — scan tool: _______
- Bus restored? YES / NO
- If YES: record — "Bus restored after disconnecting [Node X]. This node is the source of the fault."

**Disconnection 3 (if needed):**
- Node disconnected: _______
- After disconnection — oscilloscope: _______
- After disconnection — termination: ___ Ω
- If bus did not restore after disconnecting all nodes: fault is in the wiring (the CANH or CANL wire itself) rather than in any node.

---

**Phase 3: Root Cause Identification (10 min)**

Based on all measurements and disconnection results:

**3.1 Fault Location**

The fault is located in (circle one):
- Node A | Node B | Node C | The wiring / harness between nodes | Cannot determine

Evidence for this location:
______________________________________________________________________

**3.2 Fault Category**

Select the most appropriate root cause category and justify:

**Option 1 — Wiring fault:**
- Description: physical damage to CANH or CANL wire, connector pin damage, short circuit between wires or to ground/supply
- Evidence would include: fault persists after all nodes disconnected; resistance measurement showing short or open; fault location isolated to a specific harness segment
- My evidence for / against this category: ________________________________

**Option 2 — Transceiver failure:**
- Description: CAN transceiver IC (e.g., TJA1050) in a specific ECU has failed — output driver permanently active (stuck dominant), or receiver damaged
- Evidence would include: fault resolves after disconnecting a specific node; oscilloscope shows stuck-dominant condition that clears when culprit node is removed; bus voltage returns to normal after disconnection
- My evidence for / against this category: ________________________________

**Option 3 — ECU hardware fault (beyond transceiver):**
- Description: ECU's CAN controller or MCU has failed internally; ECU no longer transmitting correctly or is generating malformed frames
- Evidence would include: node absent from bus (bus-off), or node transmitting but messages are corrupted; other nodes' communication is relatively unaffected
- My evidence for / against this category: ________________________________

**3.3 Final Diagnosis Statement**

Write one clear diagnostic conclusion:

> "The CAN bus fault is caused by ______________________ in/at ______________________. Evidence: ______________________. The recommended repair is ______________________."

---

**Phase 4: Confidence and Limitations (5 min)**

**4.1** How confident are you in your diagnosis? (circle) Low / Medium / High

**4.2** What additional information or measurements would increase your confidence?
______________________________________________________________________

**4.3** If this were a real vehicle (not a bench), what additional risks or complications would you anticipate in following this same diagnostic process?
______________________________________________________________________

**4.4** If you had a full OEM topology diagram for a real 11-node vehicle with this same fault, how would your disconnection strategy change (if at all)?
______________________________________________________________________

---

### Checkpoint 3 — Assessment (Instructor Marks Assessment Form)

**Assessment Criteria and Marking:**

| Criterion | Full Credit (4 pts) | Partial Credit (2 pts) | Minimal (1 pt) | No Credit (0 pts) |
|-----------|--------------------|-----------------------|----------------|-------------------|
| Oscilloscope observations (Step 1.1) | Correct bus state, CANH, CANL all described accurately | Two of three correctly described | One correctly described | Not completed or entirely incorrect |
| Termination measurement (Step 1.2) | Correct value measured and correctly interpreted | Value measured; interpretation incorrect | Value stated but not measured correctly | Not completed |
| Scan tool findings (Step 1.3) | Nodes online/offline correctly recorded; DTCs noted | Partially correct; one node misidentified | Scan tool used but findings not recorded | Not used or not recorded |
| Disconnection process (Phase 2) | Logical sequence; each step documented; hypothesis updated after each step | Logical sequence; documentation incomplete | Disconnection performed; no documentation | Not performed when required, or no documentation |
| Fault location identified (Step 3.1) | Correct node or wiring segment identified with supporting evidence | Correct node identified; evidence not documented | Correct general area (correct segment) but wrong node | Incorrect |
| Root cause category (Step 3.2) | Correct category selected with clear supporting evidence | Correct category; evidence weak or incomplete | Adjacent category (transceiver vs ECU hardware confusion) | Incorrect category |
| Final diagnosis statement (Step 3.3) | Clear, specific, actionable; includes location, cause, and repair recommendation | Correct conclusion but vague or incomplete | Partially correct | Incorrect or absent |
| Confidence and limitations (Phase 4) | Thoughtful answers showing awareness of diagnostic limits | Answers present but superficial | Minimal answers | Not completed |

**Maximum score: 32 points. Pass threshold: 20 points (63%).**

**Sign off Checkpoint 3 on check-off card (so-7-4-2 and so-7-4-3 satisfied where pass threshold met).**

**Feedback approach:** Do not reveal the correct answer immediately after collecting the assessment form. Reveal and discuss during the debrief so all students benefit simultaneously. Students who have scored below pass threshold will be offered a second attempt on a different fault type during a designated catch-up session.

---

## Group Debrief (10 minutes)

Reconvene at front of room. Instructor reveals the planted fault for each workstation.

**Debrief Structure:**

**1. Reveal and compare (3 min)**
- "Workstation 1: the fault was ___. How many of you correctly identified it?" (show of hands)
- Do not focus on who got it wrong — focus on the process. "What was the most diagnostic measurement for this fault?"

**2. Discussion Questions (5 min)**

**Q1: "What was the most diagnostic single measurement — scope, meter, or scan tool?"**
- Expected answers vary by fault:
  - Stuck dominant: scope (immediate visual; CANH or CANL at fixed voltage)
  - Missing termination: meter (termination reading is definitive; scope shows subtle ringing that is easy to miss)
  - Open circuit: scan tool + scope together (node absent on scan tool; scope shows healthy bus with one node missing)
  - Node offline: scan tool (most direct indicator of a node going silent)
- Key point: different faults are most efficiently identified by different tools. A technician who only uses one tool will miss some faults.

**Q2: "If you had to design a 5-minute CAN screening protocol — three measurements in the right order — what would they be?"**
- Suggested answer: (1) Scope — is the bus stuck? (2) Meter — what is the termination? (3) Scan tool — which nodes respond?
- This sequence catches the majority of faults without disconnecting anything.

**Q3: "When did you realise you needed to disconnect a node — what measurement triggered the decision?"**
- Expected: scope showing stuck-dominant + all nodes offline on scan tool → disconnection needed to locate which node is causing it

**Q4: "How would your approach change if you had to diagnose this in a real car with the customer waiting?"**
- Answer should include: customer communication, risk of making things worse by incorrect disconnection, need for topology diagram, cost of time vs part replacement risk
- This builds professional practice context around the technical skill

**3. Preview of Module 8 (2 min)**

> "You now understand CAN and LIN diagnostics at the hardware and protocol level. Module 8 moves into ECU power supply faults — supply voltage requirements, inrush current, voltage supervisor ICs, and the relationship between supply quality and communication faults. Because a CAN bus fault is sometimes not a CAN fault — it's a supply problem that looks like a communication fault. More on that next session."

---

## Common Problems and Solutions

| Problem | Likely Cause | Solution |
|---------|-------------|---------|
| LIN oscilloscope shows flat 0V even in healthy state | Oscilloscope ground clip connected to LIN test point (shorts it) | Move ground clip to GND banana socket immediately; LIN test point is signal only |
| LIN waveform shows correct break and sync but no slave data bytes | Slave power not confirmed; LIN fault switches may be in incorrect state | Check fault switches are all OFF for baseline; confirm slave supply voltage |
| LIN break duration measured as shorter than expected | Oscilloscope time/div too large — break not fully resolved | Reduce time/div to 200μs/div; zoomed view shows break more clearly |
| CAN scope shows no waveform in Activity 2 | Oscilloscope trigger not set; CAN network not powered | Set trigger to Auto; confirm CAN bench power switch is ON |
| Termination reads wrong value at start of Activity 2 | Bench power not switched off before measurement | Always power off before ohms measurement; switch is on front of bench |
| Student confused about which node to disconnect first | Skipped topology diagram consultation | Direct student to topology diagram — "which end nodes have terminators?" |
| Assessment form incomplete — measurements not recorded | Student ran short on time | Remind at 20-minute mark to complete recordings; incomplete measurement records limit score even if conclusion is correct |
| Bus does not restore after disconnecting all nodes | Fault is in the wiring, not a node — fault injection switch may be wired independently | Student should reach this conclusion from their documentation: "bus fault persists after all nodes disconnected; fault is in wiring" |
| Both partners working together during assessed phase | Misunderstanding of independent requirement | Separate partners to different sides of workstation; each student completes their own assessment form independently |

---

## Appendix A: LIN Reference Waveform Sheet (Print and Laminate)

**Waveform 1 — Healthy LIN Frame**
- Description: 12V idle. Frame burst begins with break (≥1.25ms at 0V). Brief return to 12V (stop bit of break). Then sync byte (0x55 — 10 alternating transitions). Then ID byte. Then slave response (data bytes). Then return to 12V idle.
- Annotation points: "Break — ≥13 bit periods at 0V"; "Sync — 0x55 = 01010101"; "ID byte"; "Slave data bytes"; "Checksum"; "Return to idle (12V)"
- Time/div: 2ms/div. Voltage/div: 5V/div.

**Waveform 2 — No Slave Response**
- Description: Master header visible (break + sync + ID). After ID byte — LIN wire returns to 12V and stays there for the full response period. No data bytes. Return to 12V idle.
- Annotation: "Master header present"; "Expected response period — slave not responding (12V throughout)"

**Waveform 3 — LIN Stuck at 0V (Short to Ground)**
- Description: Flat 0V trace. No frame structure. No transitions.
- Annotation: "LIN wire held to ground — short circuit; pull-up cannot overcome fault"

**Waveform 4 — LIN Open Circuit (from master end)**
- Description: Flat 12V trace. No frame structure visible at the probe point if probing past the open. At master end: may show master frame attempts (transitions visible) that do not propagate to slave side.
- Annotation: "LIN wire at 12V (pull-up active); no transitions reaching slave — open circuit"

---

## Appendix B: Activity 1 Lab Worksheet

**Student Name:** _________________________ **Date:** _______________ **Workstation:** ____

**Partner Name:** _________________________ **Bench ECU Type:** ___________________

---

**LIN Healthy Baseline**

| Measurement | Expected | Your Reading |
|-------------|----------|-------------|
| LIN wire voltage at idle (V) | ~12V | |
| Break duration (ms) | ≥1.25ms | |
| Sync byte visible? (Y/N) | Y | |
| Slave data bytes present? (Y/N) | Y | |
| Number of data bytes in Slave 1 response | (depends on bench) | |

**Waveform sketch (label break, sync, ID, data bytes, checksum):**

```
[Sketch box — 15cm × 7cm]
```

---

**Part 1A: Slave 2 No-Response Fault**

LIN wire voltage during fault (V): _____ Slave 2 supply voltage at connector (V): _____

Oscilloscope — which ID period shows no slave response? _____________________________

Scope observation during Slave 2's ID frame: ______________________________________

Effect of disconnecting Slave 2 on bus waveform: ____________________________________

**Conclusion (circle):** Slave 2 hardware fault / Slave 2 power fault / LIN wire fault / Master fault

**Reasoning:** __________________________________________________________________

---

**Part 1B: LIN Short to Ground**

LIN wire voltage with fault active (V): _____ Frames visible? (Y/N) _____

Resistance LIN to GND (power off): _____ Ω

After disconnecting Slave 1 — LIN resistance: _____ Ω Bus restored? Y/N

After disconnecting Slave 2 — LIN resistance: _____ Ω Bus restored? Y/N

**Fault location (circle):** Slave 1 node / Slave 2 node / LIN wire harness / Master module

**Reasoning:** __________________________________________________________________

**Recommended repair in a real vehicle:**
______________________________________________________________________________

---

## Appendix C: Activity 2 Assessment Form

*(Full independent diagnosis form — text is reproduced in the Activity 2 section above under "Student Independent Diagnosis Procedure." Print this section as a standalone double-sided A4 form with the assessment criteria summary removed — criteria are for instructor use only.)*

**Header block on printed form:**

**Student Name:** ___________________________ **Date:** _________________

**Workstation Number:** _______ **Assessment Submission Time:** _______________

**Assessor signature (instructor):** _________________________ **Score:** ___ / 32

**Pass / Refer:** _______ **Re-assessment required:** Y / N

---

## Check-Off Card (Summary)

| SO | Checkpoint | Activity | Criterion | Date | Instructor |
|----|-----------|---------|-----------|------|-----------|
| so-7-3-2 | CP1 | 1A — Healthy baseline + Slave 2 fault | Healthy vs fault waveform correctly identified; break duration measured | | |
| so-7-3-2 | CP2 | 1B — LIN short to ground | Stuck-dominant LIN waveform identified; distinguished from no-response | | |
| so-7-3-3 | CP2 | 1B — Node disconnection | Correct isolation of shorted node vs wiring fault by disconnection | | |
| so-7-4-2 | CP3 | Activity 2 — Assessment form Phase 2 | Logical disconnection sequence; correct node isolated | | |
| so-7-4-3 | CP3 | Activity 2 — Assessment form overall | Process documented; root cause category correctly identified; score ≥20/32 | | |

**Module completion sign-off:**
All 4 SOs for Module 7 Days 15–16 signed off: YES / NO
If NO — outstanding SOs: _____________________
Re-assessment plan: ___________________________

---

*Module 7 | Day 16 Hands-On | ECUHR | v1.0 | 2026-02-18*
