# SESSION-11H: Line Tracking & Component Testing Lab
## Workshop Framework for Instructor and Students

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 5 — ECU On-Table Diagnostics
**Day:** 11 | **Session Type:** Hands-On Workshop
**Duration:** 90 minutes
**Format:** Brief Briefing → Signal Path Mapping → Supervised Independent Diagnosis → Debrief

**Session Outcomes Addressed:**
- so-5-3-2: Probe a live ECU signal line using oscilloscope, compare to expected waveform, and identify where the signal degrades | Analyze
- so-5-3-3: Use split-half fault isolation to narrow a line-tracking fault to a specific PCB stage or component | Analyze

**CO Alignment:** co-1

---

## OVERVIEW AND INTENT

This session is the direct practical application of Session 11T. Students apply the complete line tracking workflow — signal path mapping, oscilloscope probing, split-half isolation, component confirmation — to a live bench ECU with a physical fault planted on the PCB.

The fault is real. It is a physical modification to the ECU signal path, made by the instructor before the session. Students do not know where it is. They find it using the methodology taught in 11T. The process they follow is identical to what they would use in professional practice on a customer's ECU.

This session is deliberately less guided than 10H. Students are expected to apply their knowledge with the instructor present for safety oversight, equipment troubleshooting, and map sign-off — not for procedural guidance. Students who ask "what should I do next?" are redirected to their workflow and reference cards, not given the answer.

---

## EQUIPMENT LIST (Per Bench Station — 2 Students Per Station)

| Item | Specification | Notes |
|---|---|---|
| Bench ECU (fault-planted) | Same ECU type as Day 10 — fault pre-planted by instructor | Different fault variant at each bench |
| ECU wiring diagram | Printed A3 | Same as Day 10 — students should be familiar |
| ECU PCB schematic (simplified) | Printed A3 — showing the signal path under test only | Instructor prepares this; test points labelled |
| Bench power supply | Same as Day 10H — pre-configured at 12.5V | Students verify current limit before applying power |
| Bench wiring harness | Same as Day 10H | Check connections before applying power |
| Oscilloscope | 2-channel, 50MHz+ bandwidth | 1 per bench — confirmed working before session |
| Oscilloscope probes | x1 and x10 probes | Fine-tip needle-point tips for SMD component pads |
| Multimeter | Autoranging | For component confirmation measurements |
| ESR meter | In-circuit ESR measurement | For capacitor testing |
| Probe station or third-hand tool | Weighted board holder | Keeps ECU stable during fine-tip probing |
| Line tracking worksheet | 1 per student (individual, not per pair) | Template at end of this document |
| Signal path map template | Blank: boxes and arrows layout, 8 empty nodes | Students complete this from wiring diagram and PCB schematic |
| Reference card: Five fault signatures | Laminated A5 — from Session 11T Slide 13 | Posted at each bench |
| Reference card: Split-half decision flow | Laminated A5 — from Session 11T Slide 26 | Posted at each bench |
| Reference waveform sheets | Printed A4 — healthy signal captures for this ECU type/signal | Prepared by instructor from pre-fault ECU captures |
| Scan tool | Same as Day 10H | For reading the initial DTC |
| Anti-static mat and wrist straps | As per all previous sessions | |

### Instructor Pre-Preparation Checklist:
- [ ] Planted faults confirmed active on each bench ECU (scan tool shows DTC for the targeted circuit)
- [ ] Signal healthy at ECU connector pin confirmed (fault is PCB-side for this session)
- [ ] PCB schematic extract prepared — test points labelled and matched to physical board
- [ ] Reference waveform captures made from unfaulted ECU at same circuit
- [ ] Fault documentation prepared privately (see Fault Preparation section)
- [ ] Oscilloscopes confirmed functional, probes tested, ground clips verified
- [ ] ESR meters available and working

---

## FAULT PREPARATION (Instructor Only — Complete Before Session)

### Choosing the Signal Path for Each Bench:

Select a sensor input signal path that:
- Produces a DTC that students can look up and trace from the wiring diagram
- Has at least 5 accessible probe points between ECU connector pin and MCU input
- Has a clearly measurable healthy signal — slow-changing DC voltage in the 0.5–4.5V range
- The planted fault does not prevent basic ECU communication

**Recommended signal paths:** MAP sensor input, IAT sensor input, TPS signal return, coolant temperature sensor input.

### Fault Type Options (Choose One Per Bench):

**Option A — Open series resistor (simulates open-circuit trace or failed component):**
Lift one end of the series protection resistor from its pad. Signal present and correct at connector pin and up to the resistor input pad; 0V at the resistor output pad and all points onward. DTC: signal circuit low.

**Option B — Shorted bypass capacitor (simulates failed filter capacitor):**
Bridge one end of the bypass capacitor to its adjacent ground pad. Signal may appear at connector pin at reduced amplitude (voltage divider with series resistor), then drops significantly toward 0V at the capacitor node. DTC: signal circuit low.

**Option C — Added series resistor — high resistance joint (hardest variant):**
Solder an additional high-value resistor (47 kilohms to 100 kilohms) in series at a mid-path trace point. Signal is present but wrong — significantly attenuated. Requires oscilloscope interpretation, not just presence/absence detection. DTC: signal out of range.

**Option D — Scribed PCB trace (simulates physical trace crack):**
Score through the PCB trace at a chosen point between two test points. Cover with black insulating tape after scoring. Result: identical to Option A in terms of measured signal behaviour.

### Fault Documentation (Private — Not Shared with Students):

| Field | Content |
|---|---|
| Bench number | |
| Signal path under test | |
| Fault option used | A / B / C / D |
| Specific component or trace location | |
| Expected DTC | |
| Expected oscilloscope result at each test point | |
| Confirmation measurement (multimeter/ESR) | |

### Confirming Fault Before Session:
- Power each bench ECU and scan — confirm DTC is current
- Probe connector pin with oscilloscope — confirm signal is correct at the pin (fault is PCB-side)
- Confirm ECU still communicates via scan tool

---

## ACTIVITY STRUCTURE

| Phase | Duration | Activity |
|---|---|---|
| Instructor briefing | 5 min | Rules, materials, expectations — brief |
| DTC reading and circuit lookup | 10 min | Students scan ECU, identify DTC, look up circuit |
| Signal path mapping | 15 min | Students draw complete signal path map |
| Instructor map sign-off | 5 min | Hard gate — no probing without sign-off |
| Oscilloscope setup and baseline | 8 min | Configure scope, take baseline measurement |
| Line tracking with split-half | 32 min | Students trace fault; document every probe |
| Fault confirmation | 5 min | Multimeter/ESR confirmation measurement |
| Debrief | 10 min | Group discussion — findings, approaches, difficulties |

---

## PHASE 1: INSTRUCTOR BRIEFING (5 minutes)

**Deliver at the front. This is deliberately brief — students already know the procedure from 11T.**

> "This afternoon you do what you learned this morning. There is a real fault on each bench ECU. You do not know where it is. Your job is to find it.
>
> Four rules:
>
> First: you do not pick up an oscilloscope probe until I have signed off your signal path map. No map, no probing. I will enforce this.
>
> Second: every measurement you make goes on your worksheet before you make the next one. Not at the end — as you go.
>
> Third: ESD wrist straps on, ECU on the mat. Power off before switching multimeter to resistance mode.
>
> Fourth: I will not tell you where the fault is. I will answer questions about technique if you are genuinely stuck on how to apply the method. I will redirect you to your workflow and reference cards if you've stopped thinking. Ask good questions."

---

## PHASE 2: DTC READING AND CIRCUIT LOOKUP (10 minutes)

**Students work at bench stations. Instructor circulates silently — observing only.**

Students must:
1. Confirm bench PSU settings (12.5V, 2.0A limit) and apply power in correct sequence from Day 10
2. Connect scan tool and confirm communication
3. Read the DTC — record: code, status, description
4. Look up the DTC in provided service documentation — identify: which circuit, which pins, what normal voltage range
5. Confirm the DTC is current

Record all of the above in Section 1 of the line tracking worksheet before proceeding.

---

## PHASE 3: SIGNAL PATH MAPPING (15 minutes)

**Students construct the complete signal path map on the template provided.**

### Requirements for a Complete Signal Path Map:

**External path (from wiring diagram):**
- Sensor body and output type (e.g., "3-wire analog voltage sensor, 0.5–4.5V range")
- Supply wire to sensor with pin number
- Signal output wire from sensor with pin number
- Signal ground wire with pin number
- Any in-line connector in the harness with connector ID and pin number
- ECU connector pin number for the signal line

**Internal path (from PCB schematic):**
- ECU connector pin → PCB trace → series resistor (reference designator and value)
- Series resistor output → clamping diode if present, or RC filter cap
- Filter capacitor → MCU ADC input pin

**At each probe point, note:**
- Expected signal type (DC voltage, AC waveform)
- Expected signal level at current operating condition

**Minimum acceptable probe points:**
- TP1: ECU connector pin (signal line)
- TP2: Input pad of series resistor
- TP3: Output pad of series resistor
- TP4: Filter capacitor pad (if accessible)
- TP5: MCU ADC input (if accessible)

---

## PHASE 4: INSTRUCTOR MAP SIGN-OFF (5 minutes)

**Instructor reviews each bench's signal path map. Hard gate — no probing without sign-off.**

### What to Check:
- All significant probe points identified — no major gaps
- ECU connector pin correctly identified from the wiring diagram (not guessed)
- PCB test points correctly identified from the schematic — corresponding to the specific ECU
- Expected signal noted at each probe point (a number or range, not just "correct signal")
- Map flows logically from sensor to MCU

### Sign-Off Response:

**If map is complete and correct:** Sign and date. Student may now pick up oscilloscope probe.

**If map has gaps:** Return map with one specific gap noted. Do not complete the map for them.
- "Your series resistor is in the schematic between connector pin and the capacitor. Where is it on your map?"
- "What is the expected voltage at TP3? Look at the healthy reference capture."

---

## PHASE 5: OSCILLOSCOPE SETUP AND BASELINE (8 minutes)

### Oscilloscope Setup Checklist (Posted at Each Bench):
- [ ] Probe connected to CH1 — probe tip: x1 for 0–5V sensor signals
- [ ] Ground clip connected to PSU negative (confirmed with probe tip on PSU negative: reads 0V)
- [ ] Coupling: DC
- [ ] Voltage scale: 1V/div
- [ ] Timebase: 50ms/div for slow analog signals (IAT, ECT, MAP, TPS)
- [ ] Trigger: Auto, rising edge
- [ ] Probe compensation performed if x10 probe used

### Baseline Measurement Required Before Fault Tracing:

Probe the sensor supply (5V reference) at the ECU connector pin to confirm:
- 5V reference is present and stable
- Oscilloscope is reading correctly
- Ground reference is solid

Record: "5V reference at pin [X]: [value] V. Oscilloscope confirmed working."

This step prevents spending 30 minutes tracing a signal absence that turns out to be a loose ground clip.

---

## PHASE 6: LINE TRACKING WITH SPLIT-HALF (32 minutes)

**Core diagnostic exercise. Students work independently within pairs. Instructor available for questions about technique only.**

### Student Procedure:

**Step 1 — Boundary measurement: ECU connector pin**
- Probe the signal line at the ECU connector pin
- Record in Section 3 of worksheet: probe location, expected signal, measured result
- Decision: signal correct at pin?
  - YES → Fault is on PCB → proceed to PCB test points with split-half
  - NO → Fault is external → probe sensor output, then harness connector

*Instructor note: faults in this session are PCB-side. A student who concludes the fault is external should be redirected: "What does your result at the connector pin tell you? Is it consistent with a broken wire external to the ECU, or consistent with a fault inside the ECU?"*

**Step 2 — Apply split-half to PCB test points**
- From the signal path map, identify the midpoint test point between the ECU connector pin (confirmed good) and the MCU input (assumed bad — DTC still active)
- Probe the midpoint test point
- Record result in Section 3
- Split-half decision: signal present at midpoint?
  - YES → Fault in second half → probe midpoint of remaining half
  - NO → Fault in first half → probe midpoint of remaining half
- Continue until isolated to one segment between two adjacent probe points

**Step 3 — Identify the component**
- Using the PCB schematic, identify which component or trace segment lies between the last probe point with correct signal and the first probe point with wrong/absent signal
- Record in Section 4: "Fault isolated between [TP_] and [TP_]. Component in this segment: [reference designator, type, value from schematic]."

**Step 4 — Confirm with multimeter (power off required)**
- Power off bench ECU: remove KL15, wait 10 seconds, remove B+
- Using multimeter in appropriate mode:
  - Resistor: resistance mode
  - Capacitor: ESR meter across capacitor pads
  - Diode: diode mode — forward then reverse
- Record in Section 5: measured value vs expected value
- State conclusion: "Component [reference designator] reads [measured] — expected [value] — fault CONFIRMED as [open/short/high ESR]"

**Step 5 — Complete worksheet**
Before calling instructor for final check-off, confirm all sections are complete:
- Section 1: DTC and circuit identification
- Section 2: Signal path map (signed off before probing)
- Section 3: Probe log — every measurement with result and split-half decision
- Section 4: Fault isolation conclusion — component identified
- Section 5: Confirmation measurement with result and expected value
- Section 6: Proposed repair — what would you do in a professional workshop context?

---

## INSTRUCTOR CIRCULATION GUIDE

### During Signal Path Mapping Phase:
Circulate silently. Look for:
- Students referencing only the wiring diagram and omitting the PCB schematic (map ends at connector pin — incomplete)
- Students not noting expected signal values at each probe point

Ask questions:
- "Where does the signal go after it enters the ECU connector pin?"
- "What's the expected voltage at TP3 for this sensor at atmospheric pressure?"

### During Oscilloscope Setup:
Verify ground clip connection before students start tracing. A loose or wrong ground reference is the most common source of scope measurement confusion.

### During Line Tracking:
**Students probing without documented map — hard stop:**
> "Stop probing. Show me your worksheet. Where did you last record a result? Work from that point."

**Students making sequential probes instead of split-half:**
> "You've made three measurements in a row. How many would split-half have needed? Where is the midpoint of your remaining unknown range?"

**Students unable to decide which half after a probe:**
> "What did your probe show at the midpoint — signal present or absent? If present: fault is between the midpoint and the MCU. If absent: fault is between the connector pin and the midpoint. Which was it?"

**Students attempting to measure resistance with ECU powered:**
> "Resistance measurement on a live circuit is not valid. Power off before resistance mode."

**Students who have found the fault and are uncertain:**
> "You've identified a suspect. What is your confirmation step? Power off, switch to resistance mode, measure the component. What does it read? What should it read?"

**Students stuck after 20 minutes:**
> "Tell me what your last probe result was. And the one before. What does the difference tell you about where the fault is? What is the midpoint of the segment you've narrowed it to? Go there."

### Timing Checkpoints:
- 10 minutes into Phase 6: all students should have confirmed signal at connector pin and made first PCB split-half probe
- 20 minutes: all students should have applied at least 2 split-half decisions and narrowed to a segment of 2–3 test points
- 28 minutes: all students should be at or near the confirmation step
- 32 minutes: time — students who have not confirmed the fault record their progress as far as reached

---

## COMMON ERRORS AND INSTRUCTOR RESPONSES

| Error | Instructor Response |
|---|---|
| Probing from sensor end when connector pin showed correct signal | "You've confirmed the signal is correct at the connector pin. What does that tell you about the sensor and harness? Where should your next probe be?" |
| Sequential probing instead of split-half | "Count your probe points between confirmed good and confirmed bad. What is the midpoint? Go there first." |
| Scope ground clip disconnected or floating | Identify from strange readings. Probe known ground reference — if not 0V, fix ground clip before any other measurement. |
| Measuring resistance with power on | "Power off first. Resistance measurement on a live circuit is not meaningful and can damage the meter or the circuit." |
| Concluding fault without confirmation measurement | "You've narrowed it down. That's diagnosis. Now prove it. What measurement confirms your conclusion?" |
| Not recording measurements in real time | "What did you find at your last probe point? Is it on the worksheet? Go back and record it before you move forward." |
| Interpreting wrong signal without comparing to reference | "What does 'wrong' mean for this signal? What should it be? Get your reference waveform sheet and compare." |

---

## DEBRIEF (10 minutes)

**Bring students together at the front. Each bench pair reports briefly.**

### Report Format (Ask Each Bench — 90 seconds each):
1. What DTC did you start with and what circuit did it point to?
2. What did you find at the ECU connector pin?
3. How many probe measurements did it take you to isolate the fault to one segment?
4. What was the fault, and what was your confirmation measurement?
5. What would the repair be?

### Instructor Debrief Points:

**If fault found correctly:**
> "Good process. [Number] probes to isolate. Sequential probing from the connector pin would have needed [number]. Every time you used split-half correctly, you cut your remaining work in half."

**If fault not found in time:**
> "You didn't reach confirmation — that's fine. Tell me: where did the process break down? Was it the map, the scope setup, or the split-half decisions? Identifying where the process broke is as valuable as finding the fault."

**For the whole group:**
> "Every bench had the same DTC. But each bench had a different physical fault producing it. Same symptom, different root cause. That's real-world ECU diagnostics. The line tracking process found the specific cause regardless — because you measured rather than guessed."

**Preview of Day 12:**
> "Tomorrow we close Module 5 with environmental damage. Moisture, corrosion, dendritic growth. These faults sometimes produce a resistive fault — signal present but reduced — rather than a complete absence. You need everything from Day 10 and Day 11 to handle that correctly. Tomorrow also includes the Mid-Module Practical Assessment — your independent fault-finding exercise. Full details in tomorrow morning's theory session."

---

## ASSESSMENT CRITERIA

| Criterion | Competent | Not Yet Competent |
|---|---|---|
| **so-5-3-2: Probe a live ECU signal line** | Oscilloscope correctly set up; probe placed at correct points in correct sequence; result interpreted against reference waveform; documented | Scope settings incorrect; probe placed at incorrect points; result not compared to reference; no documentation |
| **so-5-3-3: Split-half fault isolation** | Split-half applied with documented midpoint decisions; fault isolated to one segment in logical sequence; method applied not sequential probing | Sequential or random probing without midpoint logic; no documented decision sequence |

**Distinction Indicator:** Student interprets the nature of the fault from the oscilloscope result — not just "signal absent" but "signal absent with floating noise — consistent with open series resistor pulling input to supply via protection diode." This level of interpretation demonstrates the Analyze level of the SO.

**Recording:** Complete practical observation record for each student during the session. A student who locates the fault by random probing (correct answer, wrong method) has not demonstrated so-5-3-3. A student who applies the correct method and runs out of time with the fault almost isolated is closer to competent.

---

## STUDENT LINE TRACKING WORKSHEET

*Print 1 per student — individual completion.*

**Student Name:** _________________________ **Bench ECU:** _________________________ **Date:** _______________

**Section 1: DTC and Circuit Identification**
- DTC Code: ___________
- DTC Status: ___________
- DTC Description: ___________
- Circuit implicated (from service documentation): ___________
- Normal signal range for this circuit: ___________
- Threshold that causes DTC to set: ___________

**Section 2: Signal Path Map**
*(Attach completed signal path map template — must be signed by instructor before probing begins)*

Instructor sign-off: _______________ Date/Time: _______________

**Section 3: Probe Log**

*Record every probe. Result before next probe. No exceptions.*

| Probe # | Location (TP ref or component pad) | Expected Signal | Measured Result | Split-Half Decision |
|---|---|---|---|---|
| Baseline | 5V ref at connector pin [___] | 5.0V DC | | n/a — scope confirmation |
| 1 | ECU connector pin [___] — boundary | | | External/Internal fault? |
| 2 | | | | Fault in first half / second half |
| 3 | | | | Fault in first half / second half |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |

**Section 4: Fault Isolation Conclusion**
- Fault isolated between: TP _____ and TP _____
- Component(s) in this segment (from PCB schematic): _____
- Reference designator: _____ | Type: _____ | Value: _____

**Section 5: Confirmation Measurement (power off before measuring)**
- Power removed: YES / NO
- Measurement type: Resistance / ESR / Diode mode
- Measured value: _____
- Expected value (from schematic or component marking): _____
- Fault CONFIRMED: YES / NO
- Fault conclusion in one sentence: _____________________________________________

**Section 6: Proposed Repair**
What would you do to repair this fault in a professional workshop? Include component specification, soldering approach, and post-repair verification step.

_______________________________________________________________________________
_______________________________________________________________________________

---

*Module 5 | Day 11 Hands-On | ECUHR | v1.0 | 2026-02-18*
