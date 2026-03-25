# SESSION-10H: Bench Test Setup & ECU Scanning Lab
## Workshop Framework for Instructor and Students

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 5 — ECU On-Table Diagnostics
**Day:** 10 | **Session Type:** Hands-On Workshop
**Duration:** 90 minutes
**Format:** Instructor Demo → Supervised Practice → Independent Scanning → Debrief

**Session Outcomes Addressed:**
- so-5-1-2: Wire an ECU to bench power supply with correct current limits and simulate ignition-on state | Apply
- so-5-1-3: Connect scan tool to bench ECU via OBD adapter and verify communication | Apply
- so-5-2-2: Compare live data readings from bench ECU against expected values to identify out-of-range sensors | Analyze
- so-5-2-3: Clear DTCs, cycle ignition, and verify whether faults are confirmed or intermittent | Apply

**CO Alignment:** co-1

---

## OVERVIEW AND INTENT

This session is the direct practical application of Session 10T. Students take the bench setup procedure and DTC interpretation methodology from theory into a real diagnostic environment. By the end of the session, every student will have independently powered a real ECU, established scan tool communication, read and classified DTCs, identified live data anomalies, and performed a clear-cycle-rescan verification.

The session is structured in four phases: a brief instructor briefing, a full instructor demonstration, supervised student practice at bench stations, and a group debrief. The hands-on phase is not step-by-step guided — students are expected to apply the workflow from 10T with the instructor available for checkpoint verification, not procedural hand-holding.

---

## EQUIPMENT LIST (Per Bench Station — 2 Students Per Station)

| Item | Specification | Notes |
|---|---|---|
| Bench ECU | Communicating ECU with wiring diagram | Pre-tested; at least 2 DTCs present (1 current, 1 historical) |
| Wiring diagram for ECU | Printed A3, laminated preferred | Must match the specific ECU on the bench |
| Bench power supply | Variable 0–30V, adjustable current limit, digital display | 1 per bench |
| Bench wiring harness | Fabricated patch harness with correct ECU connector shell; banana plug ends | Pre-made by instructor; wires labelled: B+, GND-1, GND-2, GND-3, KL15 |
| OBD breakout harness | Standard OBD-II 16-pin connector; flying leads to ECU connector harness | Labelled: OBD pin 6 (CANH), pin 14 (CANL), pin 4 (GND), pin 16 (B+) |
| Scan tool | Multi-protocol — OBD-II CAN and KWP2000 | LAUNCH X431, Autel MaxiSYS, or equivalent |
| Multimeter | Standard autoranging | For voltage verification steps |
| Anti-static mat | 1 per bench | ECU stays on ESD mat at all times |
| ESD wrist strap | 1 per student | Must be worn before any ECU contact |
| Bench Setup Quick Reference card | Laminated A5 | Posted at each station |
| DTC Classification Reference card | Laminated A5 | Posted at each station |
| Student worksheet | 1 per student pair | Template at end of this document |

### Instructor Pre-Preparation Checklist:
- [ ] Each bench ECU confirmed communicating via scan tool at correct protocol
- [ ] Each bench ECU has at least 2 DTCs: 1 current, 1 historical
- [ ] Bench wiring harnesses fabricated and labelled — tested for continuity
- [ ] OBD breakout harnesses tested — CAN pins confirmed correct
- [ ] PSU units confirmed functional with accurate current display
- [ ] Wiring diagrams printed and matched to each specific bench ECU

---

## BENCH WIRING REFERENCE DIAGRAM

*The following layout should be drawn and posted at each bench station.*

```
BENCH POWER SUPPLY (PSU)
+-------------------------------------+
|  Voltage: 12.5V                     |
|  Current limit: 2.0A                |
|  [+] terminal ──────────────────────+──> B+ wire ──────────> ECU Pin [B+]
|  [-] terminal ──────────────────────+──> GND wire 1 ────────> ECU Pin [GND-1]
+-------------------------------------+    GND wire 2 ────────> ECU Pin [GND-2]
                                           GND wire 3 ────────> ECU Pin [GND-3]

IGNITION SWITCH
         PSU [+] terminal ────> KL15 wire ────> ECU Pin [KL15]
         Apply AFTER B+ and GND are stable and PSU is on

OBD BREAKOUT HARNESS
         ECU Pin [CANH] ────> OBD-II pin 6
         ECU Pin [CANL] ────> OBD-II pin 14
         OBD-II pin 4 ──────> GND (PSU negative)
         OBD-II pin 16 ─────> B+ (PSU positive)
         OBD-II connector ──> Scan tool cable

ECU sits face-up on anti-static mat
```

*For K-Line ECUs (pre-2008): connect K-Line pin from ECU connector to OBD-II pin 7.*

---

## SESSION STRUCTURE

| Phase | Duration | Activity |
|---|---|---|
| Instructor briefing | 8 min | Objectives, safety rules, equipment overview |
| Instructor demonstration | 18 min | Complete bench setup and scan — narrated, projector |
| Student practice: bench wiring | 20 min | Students wire their ECU from wiring diagram |
| Student practice: scanning | 28 min | DTCs, live data, clear-cycle-rescan |
| Debrief and discussion | 16 min | Findings, discussion, SO sign-off |

---

## PHASE 1: INSTRUCTOR BRIEFING (8 minutes)

**Deliver standing at the front with all students gathered before they approach bench stations.**

### Safety Rules:
> "Before anyone touches anything — five rules:
>
> One: ESD wrist strap on now, before you approach the bench. It stays on until you leave. No exceptions.
>
> Two: The ECU stays on the anti-static mat at all times.
>
> Three: Current limit is 2.0A before you apply power. If anyone asks me why their ECU isn't responding and their current limit is at 10A — I will not help them until they set it to 2.0A first.
>
> Four: If you see smoke, smell burning, or the current hits the limit at power-on — power off immediately. Do not increase the limit. Raise your hand.
>
> Five: You do not connect any wire until you have read the wiring diagram and identified where it goes."

### Session Objectives:
> "By the end of this session, every person at every bench will have done this: taken a real ECU, read its wiring diagram, identified all required connections, wired it to a bench power supply correctly, applied power in the correct sequence, connected a scan tool, read all DTCs with status, read live data and identified any anomalous values, cleared the codes, cycled the ignition, re-scanned, and determined which faults are current and which are historical."

---

## PHASE 2: INSTRUCTOR DEMONSTRATION (18 minutes)

**Instructor performs the complete workflow at the front bench. Projector displays everything. Students observe — no hands-on yet. Narrate every action.**

### Demo Step 1: Reading the Wiring Diagram (3 minutes)
Display the wiring diagram on the projector alongside the ECU connector.

> "Diagram first. I'm looking for four things: battery positive, all ground pins, KL15 ignition supply, and CAN bus pins. I will not touch a wire until I have found all four and marked them on my diagram."

Point to each pin on the diagram. Count the ground pins aloud.

> "Three ground pins. Not one — three. I will connect all three. If I connect only one, the ECU may appear to power on but refuse to communicate."

> "I have not touched a wire yet. I have already done the most important part of the bench setup."

### Demo Step 2: PSU Configuration (2 minutes)
Set voltage to 12.5V on screen. Set current limit to 2.0A on screen. Show both readings.

> "12.5V. 2.0A limit. PSU output is currently OFF. I'm connecting wires to an unpowered supply — safe, controlled."

### Demo Step 3: Applying Power (2 minutes)
Turn PSU output ON. Watch the current display.

> "Current reading: 0.28 amperes. That is the ECU's standby consumption. Under 0.5A — good. If it had jumped to 2A immediately, I would power off without hesitation."

### Demo Step 4: Applying Ignition (2 minutes)
Connect KL15 wire or toggle the ignition switch.

> "KL15 applied. Watch the current — [pause] — it's risen to 0.7A and is settling. The ECU is booting. I'm going to give it five seconds."

[Wait visibly and count.]

> "Now it's settled at 0.55A. The ECU is alive and ready."

### Demo Step 5: Connecting the Scan Tool (2 minutes)
Connect OBD breakout harness. Connect scan tool. Navigate to ECU communication.

> "OBD harness connected. Scan tool powered. Auto-detect protocol — [wait] — connected. CAN ISO 15765. I can see the ECU ID on screen. Communication established."

### Demo Step 6: Reading DTCs (4 minutes)
Navigate to fault codes screen.

> "DTCs. I can see four codes. Status first, then code, then description. Never code-then-description — status first, always.
>
> P0105, current. MAP sensor circuit. The ECU is detecting a circuit fault in the MAP sensor signal path right now. That's my primary investigation target.
>
> U0155, current. Lost communication with instrument cluster. We're on a bench without a cluster — this is an environment artefact. I'll note it but I won't investigate it here.
>
> P0115, historical. Coolant temp sensor circuit. Was present, not now. Possibly intermittent."

### Demo Step 7: Live Data Reading (2 minutes)
Navigate to live data stream. Scroll through values.

> "Live data — I'm looking for any values that are physically impossible. IAT 23 degrees C — reasonable for a workshop. ECT -40 degrees C — impossible for a room-temperature ECU. That -40 degrees C confirms P0115 is not truly historical: the circuit is currently open."

### Demo Step 8: Clear, Cycle, Re-scan (3 minutes)
> "I'm photographing this screen before I do anything. Then — clear all codes."

Perform clear. Toggle KL15 off, wait 10 seconds, reconnect, wait 30 seconds.

> "Re-scan. P0105 — back immediately. Current. U0155 — also back, as expected. P0115 — also back. The three codes that returned are all confirmed current faults. Now I have my diagnostic entry points."

> "That is the complete workflow. You watched me do it. Now you do it."

---

## PHASE 3: STUDENT PRACTICAL — BENCH WIRING (20 minutes)

**Students move to bench stations. Instructor circulates. Both students in each pair must participate in every step.**

### Posted Instructions (At Each Bench Station):

**STEP 1 — Read the wiring diagram: do not touch any wire yet (5 minutes)**

Using the wiring diagram for your specific ECU:
- Circle in pencil all B+ pins on the diagram
- Circle all GND pins — every single one
- Circle the KL15 ignition pin
- Circle CANH and CANL pins (or K-Line pin for pre-CAN ECUs)
- Complete the pin identification table in Section 1 of your worksheet
- Show your completed table to the instructor before proceeding

**STEP 2 — Configure the power supply (2 minutes)**
- Set voltage to 12.5V
- Set current limit to 2.0A
- Confirm PSU output switch is in the OFF position

**STEP 3 — Connect B+ and all GND wires (4 minutes)**
- Connect B+ wire from PSU positive terminal to ECU B+ pin
- Connect each GND wire from PSU negative terminal to each ECU GND pin
- Verify each connection against your wiring diagram
- Count GND connections on ECU vs count in wiring diagram — must match

**STEP 4 — Apply power (2 minutes)**
- Turn PSU output ON
- Immediately observe current display
- Record current reading on worksheet: Section 1, "Current at power-on (B+ only)"
- If current is at or above 1.8A: power off immediately and call instructor

**STEP 5 — Apply ignition (2 minutes)**
- Connect KL15 wire to PSU positive terminal (through the ignition switch provided)
- Wait 5 seconds — observe current rise and settle
- Record current after ignition-on on worksheet

**STEP 6 — Connect OBD harness and scan tool (3 minutes)**
- Connect OBD breakout harness to ECU harness at CANH/CANL pins
- Connect OBD-II cable from breakout harness to scan tool
- Power scan tool on
- Select auto-detect protocol or select the correct vehicle

**CHECKPOINT 1: Raise your hand when scan tool shows communication established. Instructor will verify before you proceed to scanning.**

---

## PHASE 4: STUDENT PRACTICAL — SCANNING (28 minutes)

**Instructor signs off on communication at each bench. No scanning begins without this sign-off.**

### Posted Instructions (Continued):

**STEP 7 — Read and record all DTCs (6 minutes)**

Navigate to fault codes / DTC screen.
- Photograph the screen
- Complete the DTC log in Section 2 of your worksheet:

| DTC Code | Status | Description | Circuit Implicated |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

For the "Circuit Implicated" column: write the circuit, not the component. Example: "MAP sensor signal circuit — sensor, wiring, ECU pin, input stage" not "MAP sensor."

**STEP 8 — Classify each DTC (4 minutes)**

For each DTC recorded:
- Write the classification: Current / Pending / Permanent / Historical
- Write what the status tells you about the fault
- For one DTC of your choice: use the wiring diagram to identify the specific connector pins and wires in the circuit. Write the pin numbers on your worksheet.

**STEP 9 — Identify out-of-range live data (6 minutes)**

Navigate to live data / data stream screen.
- Scroll through all available parameters
- Record any value that is physically impossible for the current bench environment in Section 3:

| Parameter | Observed Value | Expected Value | Circuit Fault Type That Produces This |
|---|---|---|---|
| | | | |
| | | | |

Expected value guidance: IAT and ECT should be close to room temperature (15–30 degrees C). TPS should be 0.4–0.8V (closed throttle equivalent). MAP should be 25–50 kPa. Battery voltage should be 12.3–12.7V.

**CHECKPOINT 2: Instructor reviews DTC log and live data documentation before you proceed to clearing.**

**STEP 10 — Clear, cycle, re-scan (8 minutes)**
- Photograph all DTCs again before clearing (backup evidence)
- Clear all DTCs using scan tool
- Remove KL15 (open the ignition switch) — wait 10 seconds
- Reconnect KL15 — wait 30 seconds
- Re-scan for DTCs

Complete Section 4 of worksheet:
- DTCs that returned (confirmed current): list each
- DTCs that did not return (confirmed historical): list each
- For each confirmed current DTC: write one sentence explaining what it tells you about the fault state of the ECU right now

**STEP 11 — Diagnostic entry point question (4 minutes)**

Answer Section 5 of the worksheet independently:
> "Based on your scan results, which fault would you investigate first and why? What circuit would you begin tracing, and what test equipment would you use? What do you expect to find at the ECU connector pin for that circuit?"

**CHECKPOINT 3: Worksheet complete. Instructor reviews Section 4 and Section 5 for SO sign-off.**

---

## INSTRUCTOR CHECKPOINTS AND CIRCULATION GUIDE

### During Bench Wiring Phase — verify at each station:
- Wiring diagram consulted and pin table completed before any wire connected
- ALL GND pins connected — not just one (most common error)
- PSU current limit at 2.0A — not higher, not bypassed
- Correct power-on sequence: B+/GND first, then KL15 after PSU stable
- Current draw after power-on under 1.0A settled

### Prompt questions while circulating:
- "Which pin is KL15 on this ECU? How did you find it?"
- "You've connected two ground wires. Your diagram shows three GND pins. What's missing?"
- "Current is 0.4A at power-on. What does that tell you?"
- "What would you do if the current jumped to 2.0A the moment you applied power?"

### During Scanning Phase — verify at each station:
- Students recording DTC status, not just the code
- Students can explain what circuit a DTC points to
- Students photographed DTCs before clearing
- Students performed key cycle correctly: off, wait, on, wait, re-scan

### Red Flags Requiring Immediate Intervention:
- Current limit set above 2A without instructor approval
- Student increasing limit because "the ECU isn't responding"
- ESD strap removed while ECU is on the bench
- Student cleared DTCs before recording them

---

## COMMON STUDENT ERRORS AND INSTRUCTOR RESPONSES

| Error | Instructor Response |
|---|---|
| Missing one or more GND pins (ECU won't communicate) | "Count the ground pins in your diagram. Count the ground wires you've connected. Are they the same number?" |
| KL15 not connected — ECU appears dead | "ECU is receiving power. What signal tells it the ignition key is on? Which pin? Connect it." |
| Increasing current limit to resolve "no response" | "Stop. Power off. That limit is there to tell you something is wrong, not to be overridden. Walk me through your wiring step by step." |
| Reversed CANH and CANL | "Check your OBD harness diagram. Which pin is CANH and which is CANL? Swap them and retry." |
| Recording only DTC code, not status | "What does the scan tool show next to that code? Is there a status column? That column tells you whether this is happening right now or whether it happened last week." |
| Cleared DTCs before photographing | "What were the codes before you cleared? Do you have a record? Cycle the ignition — some codes may return. Next time: photograph first." |
| Classifying all DTCs as current | "Go back to the scan tool status column. Find one that says historical or stored. What does that mean about when this fault occurred?" |

---

## DEBRIEF (16 minutes)

**Bring all students together at the front of the workshop.**

### Group Discussion Questions:

**Round 1 — Bench Setup (4 minutes):**
1. "What was your ECU drawing in current before you applied KL15? What about after?"
2. "Did anyone have a problem establishing communication? What was the cause?"
3. "How many ground pins did your ECU have? Did anyone initially only connect one?"

**Round 2 — DTC Interpretation (5 minutes):**
4. "How many DTCs did your bench ECU have? How many were current, how many historical?"
5. "Did anyone have U-codes? Why would those appear on a bench?"
6. "Which DTC would you investigate first, and why that one before the others?"

**Round 3 — Live Data and Rescan (4 minutes):**
7. "What anomalous live data values did anyone find? What circuit fault produces that specific value?"
8. "After your clear-cycle-rescan, which codes returned? Which didn't? What does that tell you?"
9. "If a code returns within five seconds of re-scanning — what does that tell you about the fault?"

**Instructor Takeaway Points (3 minutes):**
> "Three things. First: the wiring diagram is not optional paperwork — it is the foundation that makes bench testing possible.
>
> Second: current draw at power-on is diagnostic data. Write it down every time.
>
> Third: DTC status matters as much as the code. A historical P0105 and a current P0105 require completely different responses.
>
> Tomorrow, Sessions 11T and 11H build on exactly what you found today. You'll take a confirmed current DTC and a target circuit, and trace that circuit — pin by probe — until you find the specific component that has failed."

---

## ASSESSMENT CRITERIA

| Criterion | Competent Indicators | Not Yet Competent |
|---|---|---|
| **so-5-1-2: Bench wiring** | All correct pins identified from diagram before wiring; correct voltage and current limit set; correct sequence followed | Pins not verified from diagram; current limit missing or bypassed; sequence out of order |
| **so-5-1-3: Scan tool connection** | Communication established; protocol identified; can state which pins CANH/CANL go to | Cannot establish communication; cannot identify reason if communication fails |
| **so-5-2-2: Live data interpretation** | At least one out-of-range value identified; correct expected range stated; plausible circuit fault type proposed | Cannot identify anomalous values; no reference to expected ranges |
| **so-5-2-3: Clear-cycle-rescan** | DTCs photographed before clear; correct key cycle performed; clear distinction between current and historical codes | Cleared without recording; incorrect cycle procedure |

---

## STUDENT WORKSHEET TEMPLATE

*Print 1 per bench pair.*

**Student Name(s):** _________________________ **Date:** _______________
**ECU Under Test:** _________________________ **Vehicle Application:** _______________

**Section 1: Bench Setup**

Pin identification (complete from wiring diagram before wiring):

| Connection | Pin Number(s) | Signal Label on Diagram |
|---|---|---|
| Battery positive (B+) | | |
| Ground 1 (GND) | | |
| Ground 2 (GND) | | |
| Ground 3 (GND) (if applicable) | | |
| Ignition supply (KL15) | | |
| CAN high (CANH) | | |
| CAN low (CANL) | | |

PSU Settings: Voltage set: _____ V | Current limit set: _____ A

Current readings:
- Current at power-on (B+ and GND only, KL15 not yet applied): _____ A
- Current after KL15 applied (settled): _____ A

Communication confirmed? YES / NO

If NO, describe what you investigated: ___________________________

**Section 2: DTC Log**

| DTC Code | Status | Description | Circuit Implicated |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

For DTC code _________: identify specific connector pins and wire numbers for its circuit from the wiring diagram:
Signal wire: Pin _____, Wire colour/number: _____
Reference/supply wire: Pin _____, Wire colour/number: _____
Ground wire: Pin _____, Wire colour/number: _____

**Section 3: Live Data Anomalies**

| Parameter | Observed Value | Expected Value | Circuit Fault Type |
|---|---|---|---|
| | | | |
| | | | |

**Section 4: Clear-Cycle-Rescan Results**

DTCs photographed before clear: YES / NO
Key cycle: KL15 removed → waited _____ seconds → KL15 reapplied → waited _____ seconds → re-scanned

DTCs that returned (confirmed current): 1. _____ 2. _____ 3. _____
DTCs that did not return (confirmed historical): 1. _____ 2. _____

For each confirmed current DTC, write one sentence explaining what it tells you:
_____________________________________________________________________________

**Section 5: Diagnostic Entry Point**

Which fault would you investigate first, and why?
_____________________________________________________________________________

What circuit would you begin tracing?
_____________________________________________________________________________

What equipment would you use?
_____________________________________________________________________________

What would you expect to measure at the ECU connector pin for the signal line of your primary DTC?
_____________________________________________________________________________

---

*Module 5 | Day 10 Hands-On | ECUHR | v1.0 | 2026-02-18*
