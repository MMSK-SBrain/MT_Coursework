# SESSION-02H: Multimeter Lab
## Hands-On Session — Day 2, Block 2

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 2 — Tools & Measurement Mastery
**Session Type:** Hands-On / Workshop Practical
**Duration:** 90 minutes
**Delivery Format:** Bench-based practical; students in pairs sharing one station

---

## Session Outcomes

By the end of this session, students will be able to:

- **so-2-1-2:** Perform diode forward-voltage and back-voltage tests on protection diodes and TVS devices
- **so-2-1-3:** Measure voltage drop across suspect PCB traces to identify high-resistance joints
- **so-2-1-4:** Use continuity mode to verify trace integrity from connector pin to component pad
- **so-2-2-2:** Capture and measure a PWM output signal (frequency, duty cycle, amplitude)

---

## Equipment and Materials List

### Per Station (pair of students)
- 1x Professional true-RMS multimeter (Fluke 87V or equivalent) with fine-tip probes and test leads
- 1x Cheap auto-ranging meter (for comparison exercises)
- 1x Training ECU board — pre-prepared with deliberate faults (see Fault Board Preparation below)
- 1x Healthy donor ECU board (for baseline reference measurements)
- 1x Bench DC power supply, adjustable 0–15V, current-limited to 500mA
- 1x Oscilloscope (at least 2-channel, 20MHz bandwidth minimum) with x10 probe
- 1x PWM signal generator (function generator or microcontroller-based trainer board producing known PWM outputs)
- 1x ESD wrist strap and mat
- 1x Magnifying loupe (5x–10x) or USB microscope
- Fine-tip probes (1mm tip or smaller) — at least 1 set per station
- Printed Station Reference Card (see appendix) — laminated, one per station

### Consumables / Shared Resources
- Spare fine-tip probe sets at instructor bench
- Isopropyl alcohol (IPA) and cotton swabs for cleaning test points
- Sticky notes and marker for labelling probe positions during measurements

### Fault Board Preparation (Instructor Task — prepare 24–48 hours before session)
Prepare one set of training boards per station with the following deliberate faults:

| Board Label | Fault Type | Location | Expected Reading |
|-------------|-----------|----------|-----------------|
| Board A | Cracked PCB trace (high-resistance joint) | 5V reference trace, 30mm section | >0.1V drop under load |
| Board B | Shorted protection diode | Input protection diode D3 | ~0V in both directions in diode test |
| Board C | Open trace (broken continuity) | Sensor ground return, via failure | OL in continuity mode |
| Board D | Degraded solder joint | ECU connector pin 14 crimp | >0.15V drop under 50mA load |

*Note: Document each fault with a photograph and the expected measurement result. Keep a sealed instructor answer sheet at your bench. Do not share fault locations with students before they complete the exercise.*

---

## Safety Briefing (5 minutes — mandatory before any probing begins)

Deliver this briefing with students standing at their benches, not seated. Eye contact and attention are required.

> "Before we touch anything, we cover safety. This is not a formality — these rules exist because people have destroyed boards, blown meters, and in one case caused a short that took out a bench supply. So listen once, and then we will not need to say it again."

**Rule 1 — ESD protection is on before power is on.**

> "Wrist strap on, mat grounded, before you pick up any board. Every time. If your wrist strap is not on, I will ask you to put it on before you continue. I will not ask twice."

**Rule 2 — Announce mode changes aloud.**

> "Before you change your meter mode — from voltage to resistance, from resistance to diode test — say it out loud. 'Switching to resistance mode.' This is not for my benefit. It is so your partner hears it, and so you hear yourself say it. It catches errors."

**Rule 3 — Resistance mode: power off, caps discharged.**

> "If you switch to resistance mode with the board live, you will corrupt your reading and may damage a component. Power off means bench supply off, not just at zero volts — switch it off. Then wait 20 seconds for capacitors to discharge. Measure supply caps before you start."

**Rule 4 — Current (A) mode is prohibited unless explicitly instructed.**

> "The current measurement jacks are not used today. Do not plug into them. If your meter has the probe in the current jack and you probe a voltage rail, you will blow your meter fuse and possibly the board. If you need to measure current for any reason, ask me first."

**Rule 5 — Fine-tip probes only on SMD components.**

> "Standard probe tips on 0402 or smaller components will bridge pads. Fine-tip probes only. They are at your station. Use them."

*Ask if there are any questions before proceeding. Allow 1–2 minutes.*

---

## Warm-Up Question (2 minutes)

Before starting the procedure, ask each pair at their station:

> "Tell me: for Task 1 — diode testing — what meter setting do you start with, and why?"

*Expected answer:* Diode test mode. Because we need to see the forward voltage drop, not resistance or continuity. The diode test mode supplies the correct test current (0.5–1mA) and reads voltage directly.

*If a pair cannot answer, have them refer to their notes from the theory session before proceeding. Do not give the answer — make them find it.*

---

## Instructor Pre-Activity Demonstration (10 minutes)

Perform this at the instructor bench with document camera feed. Students observe only — do not have them follow along yet.

**What to demonstrate:**

1. **ESD strap attachment and mat grounding check** — show the proper snap connection and briefly test the strap with a wrist strap tester if available.

2. **Lead null procedure** — short probes in Ω mode, press REL/ZERO, confirm 0.00Ω display. Then measure a known 1Ω resistor — show the reading before and after null to illustrate the difference.

3. **Diode test on a healthy diode** — probe a known-good 1N4148 signal diode. Show 0.62V forward, OL reverse. Narrate: *"0.62 volts — silicon. Forward biased. Reverse shows OL — it's not conducting in reverse. This is a healthy diode."*

4. **Voltage drop test setup** — connect the board to bench supply, identify the suspect trace section, set meter to DC mV range, place probes across the trace section (not to ground). Show a healthy trace reading (near 0mV). Then show the pre-damaged trace section — reading should jump above 100mV.

5. **Oscilloscope setup for PWM** — on the function generator set to a 500Hz, 12V amplitude, 40% duty cycle square wave. Show: connect x10 probe, set channel to DC coupling, set volts/div to 5V/div, set timebase to 500μs/div, set trigger to edge/rising/channel 1. Adjust trigger level to mid-signal. Show the stable waveform. Use cursor tools to read frequency (count one full cycle), duty cycle (measure high time ÷ period), and amplitude (count divisions × V/div).

> "That is exactly what you will do at your stations. Watch the sequence: ESD on, power on, set mode, confirm ground reference, probe, read, record. Every task follows that sequence."

---

## Student Procedure

Students work in pairs. One student operates, the other observes and records. Switch roles at the midpoint of each task.

---

### TASK 1: Protection Diode Testing (20 minutes)

**Objective:** Perform forward and reverse diode tests on protection diodes and TVS devices on the training board. Identify any faulty devices.

**Step 1:** Fit ESD wrist strap. Confirm strap indicator or tester shows OK.

**Step 2:** Ensure bench supply is OFF. Board is unpowered throughout Task 1.

**Step 3:** Set multimeter to Diode Test mode. Confirm the diode symbol is displayed on the LCD.

**Step 4:** Locate protection diodes on the training board. Use the Station Reference Card to identify diode designators (D1, D2, D3, D4 on your board).

**Step 5:** For each diode:
- Place red probe on the anode side (identified by component marking or reference card), black probe on cathode.
- Record the forward voltage reading.
- Reverse the probes (red to cathode, black to anode).
- Record the reverse reading (expect OL for silicon; if it reads a voltage, note the value).

**Step 6:** Record all results in the measurement table on your station sheet.

**Step 7:** Identify any diode that does not meet the following criteria and mark it as SUSPECT:

| Device Type | Healthy Forward Voltage | Healthy Reverse |
|-------------|------------------------|-----------------|
| Silicon signal diode (1N4148 type) | 0.55 – 0.70V | OL |
| Schottky diode | 0.20 – 0.40V | OL |
| TVS device (clamping direction) | 0.20 – 0.60V (depends on type) | OL |
| Any diode (shorted) | 0.00 – 0.05V both directions | — |
| Any diode (open) | OL both directions | — |

**Step 8:** Write your conclusion for each diode: HEALTHY, SHORTED, or OPEN.

**Instructor checkpoint:** Call instructor to check your measurement table before proceeding to Task 2. Instructor will confirm or challenge your conclusions.

*Instructor: check that lead polarity was correct, readings were recorded not estimated, and the student can explain what each reading means physically.*

---

### TASK 2: Voltage Drop Testing on PCB Traces (20 minutes)

**Objective:** Measure voltage drop across pre-damaged and healthy PCB trace sections under load. Identify the faulty section.

**Step 1:** Confirm meter is in DC voltage mode, finest available range (mV range preferred, or 200mV range).

**Step 2:** Connect the training board to the bench supply. Set supply to 5.0V, current limit to 200mA. Switch supply ON. Confirm power LED or supply current reading shows the board is drawing current.

**Step 3:** Allow 30 seconds for the board to reach thermal equilibrium (important — resistance of PCB traces changes with temperature).

**Step 4:** Using the Station Reference Card, locate the labelled trace test points: TP-A1 (upstream), TP-A2 (midpoint), TP-A3 (downstream near sensor connector).

**Step 5:** Perform voltage drop tests across each trace segment:

| Measurement | Red Probe | Black Probe | Record Reading |
|-------------|-----------|-------------|----------------|
| Segment 1 | TP-A1 | TP-A2 | _______ mV |
| Segment 2 | TP-A2 | TP-A3 | _______ mV |
| Full path | TP-A1 | TP-A3 | _______ mV |

**Step 6:** Compare your segment readings. The segment with the highest drop contains the fault. Record which segment.

**Step 7:** For the faulty segment — calculate the equivalent fault resistance.
- Note the board load current from the bench supply current display (or from the Station Reference Card if the supply does not display current).
- Apply: R = V ÷ I

**Step 8:** Compare to the full-path reading. The full-path reading should equal the sum of the two segment readings (within ±5mV). If it does not, check your probe positions.

**Step 9:** Switch supply OFF before moving probes to the next task.

**Instructor checkpoint:** Call instructor before starting Task 3. Show your recorded readings. Be prepared to answer: "Which segment failed, and how do you know?"

*Instructor: verify that students placed probes across trace segments, not to ground. Verify calculations. If a student calculated R but has no units, ask them to state the units before moving on.*

---

### TASK 3: Continuity Testing — Trace Integrity from Pin to Pad (15 minutes)

**Objective:** Use continuity mode to verify the integrity of a signal path from ECU connector pin to component pad. Identify where a traced path breaks.

**Step 1:** Bench supply OFF. Confirm board is unpowered.

**Step 2:** Wait 20 seconds. Measure voltage across main supply capacitor — confirm below 1V before proceeding.

**Step 3:** Set meter to continuity mode. Confirm the tone/speaker symbol is displayed.

**Step 4:** Short the probes together — confirm audible tone. If no tone, check probe connection and battery level.

**Step 5:** Using the Station Reference Card, locate the signal path for the sensor ground return trace: starts at connector Pin 3 (GND), runs through the board to component pad CP-17.

**Step 6:** Test continuity at each intermediate test point along the path:

| Test | Red Probe | Black Probe | Tone? | Record |
|------|-----------|-------------|-------|--------|
| Pin 3 → TP-B1 | Connector Pin 3 | TP-B1 | Y/N | |
| TP-B1 → TP-B2 | TP-B1 | TP-B2 | Y/N | |
| TP-B2 → CP-17 | TP-B2 | CP-17 | Y/N | |
| Pin 3 → CP-17 (full path) | Connector Pin 3 | CP-17 | Y/N | |

**Step 7:** Where you get no tone — switch to resistance mode. Measure resistance between that pair of test points. Record the value. This tells you whether the path is fully open (OL) or has a high but measurable resistance.

**Step 8:** Based on your results, identify the segment where the fault is located. Write one sentence explaining your reasoning.

**Step 9:** Revisit the healthy board for comparison. Run the same test sequence on the healthy board. Record the readings. Note the difference.

**Note for students:** If continuity mode gives a tone for a segment that you suspect is faulty, do not assume it is healthy — follow up with resistance mode. A 30Ω high-resistance joint may still beep on some meters.

**Instructor checkpoint:** Instructor reviews the comparison between faulty and healthy board readings. Ask student: "If continuity beeps on a segment with 30 ohms of resistance, why is that a problem for ECU sensor accuracy?"

*Expected answer: Because 30Ω of ground return resistance will create a voltage error in the sensor reading. A sensor drawing 20mA through 30Ω of ground resistance sees a 600mV ground offset — massively corrupting the analog reading.*

---

### TASK 4: Oscilloscope — Capture and Measure a PWM Signal (20 minutes)

**Objective:** Connect the oscilloscope to the PWM signal generator output, configure the scope correctly for DC ECU signals, and use cursor measurements to determine the signal's frequency, duty cycle, and amplitude.

**Step 1:** Connect the oscilloscope x10 probe to channel 1. Connect the probe ground clip to the signal generator's ground terminal.

**Step 2:** Connect the probe tip to the signal generator's output terminal. The signal generator is set to: 500Hz, 12V amplitude, variable duty cycle (your instructor will set a specific duty cycle — you will measure it, not be told it).

**Step 3:** Set the oscilloscope:
- Channel 1: DC coupling (not AC)
- Volts/div: 5V/div
- Timebase: 500μs/div
- Trigger: Edge, Rising, Channel 1, level set to approximately 6V (mid-signal)
- Probe setting: x10 (confirm in scope channel menu if available)

**Step 4:** If the waveform is not stable, adjust the trigger level until the waveform locks. Do not change the timebase to stabilise — adjust trigger only.

**Step 5:** Confirm you can see at least 2–3 complete cycles on screen. If you cannot, adjust the timebase only:
- Too slow (cycles appear compressed): decrease timebase (e.g., 200μs/div)
- Too fast (only partial cycle visible): increase timebase (e.g., 1ms/div)

**Step 6:** Use the scope cursor tools to measure:

| Measurement | Method | Your Reading |
|-------------|--------|--------------|
| Period (T) | Place vertical cursors at identical points on two consecutive rising edges | _______ ms |
| Frequency (f) | f = 1 ÷ T | _______ Hz |
| High time (t_on) | Place vertical cursors at rising edge and next falling edge | _______ ms |
| Duty cycle (D) | D = t_on ÷ T × 100% | _______ % |
| Amplitude (V_p-p) | Place horizontal cursors at top and bottom of square wave | _______ V |

**Step 7:** Ask your instructor for the signal generator's actual set values. Compare your measured values. Acceptable tolerance: ±5% for frequency, ±2% for duty cycle, ±0.5V for amplitude.

**Step 8:** Your instructor will change the duty cycle without telling you. Repeat the cursor measurements and record the new duty cycle. You have 3 minutes.

**Step 9 (extension — if time allows):** Switch channel 1 from DC coupling to AC coupling. Observe and record what changes. Then switch back to DC coupling. Write one sentence explaining why AC coupling is not appropriate for this measurement.

**Instructor checkpoint:** Review student cursor measurement screenshots (use scope save function if available, or photograph the screen). Verify DC coupling is set. Verify probe x10 setting is confirmed.

*Instructor: the most common error here is having the probe set to x1 on the scope but using an x10 probe physically — this produces readings 10x too high. If student amplitude reads 120V, that is the error. Walk them through the probe factor setting.*

---

## Instructor Checkpoint Summary

| After Task | What to Check | Pass Criterion |
|------------|--------------|----------------|
| Task 1 | Diode measurement table; student can explain shorted vs open | Correct classification of all 4 diodes; correct polarity during measurement |
| Task 2 | Voltage drop readings; R calculation with correct units | Faulty segment correctly identified; R calculation within 10% |
| Task 3 | Continuity log; resistance values at break; comparison with healthy board | Break correctly localised to one segment; explanation of why continuity beep is insufficient alone |
| Task 4 | Oscilloscope screenshot or photo; cursor readings vs generator settings | DC coupling confirmed; all three measurements within tolerance; duty cycle change captured correctly |

---

## Sign-Off Checklist (Assessment Criteria)

Instructor initials each line at the end of the session. All lines must be initialled for the student to be marked complete for this session.

**Student Name:** _____________________________ **Date:** _____________

| # | Criterion | Instructor Initials |
|---|-----------|---------------------|
| 1 | ESD wrist strap worn and tested at start of session | |
| 2 | Meter mode announced aloud at each change (observed by instructor) | |
| 3 | Diode test performed correctly — polarity correct, all 4 devices tested | |
| 4 | At least one shorted or open diode correctly identified and explained | |
| 5 | Voltage drop test probes placed across trace section (not to ground) while circuit was live | |
| 6 | Faulty trace segment correctly identified from differential drop readings | |
| 7 | Fault resistance calculated correctly with correct units (ohms) | |
| 8 | Continuity test performed at each intermediate test point (not just end-to-end) | |
| 9 | High-resistance break localised to correct segment | |
| 10 | Oscilloscope set to DC coupling (not AC) | |
| 11 | Probe x10 factor confirmed in scope settings | |
| 12 | Frequency, duty cycle, and amplitude measured using cursors — all within tolerance | |
| 13 | Duty cycle successfully re-measured after instructor changed generator setting | |

---

## Common Mistakes and How to Address Them

| Mistake | How It Manifests | Intervention |
|---------|-----------------|-------------|
| Diode tested with wrong polarity first | Student records OL as the forward reading, calls diode open | Ask: "Which probe is on the anode?" Have student verify from component marking. Redo with correct polarity. |
| Voltage drop probes placed to ground, not across the section | Both readings are nearly the same large voltage (4.9V, 4.8V) instead of millivolts | Ask: "What voltage are you trying to measure — the supply, or the drop across this trace?" Draw the probe placement on paper. |
| Continuity test performed only end-to-end | Student finds "no tone" but cannot localise the break | Ask: "Which segment caused the silence?" Require step-by-step testing at every intermediate TP. |
| Oscilloscope in AC coupling | Waveform appears correct for shape but DC offset is removed; student reads correct duty cycle but incorrect amplitude | Ask: "What is the DC level of this signal?" If they can't measure it (it reads 0V offset in AC), that reveals the problem. Switch to DC and repeat. |
| Oscilloscope probe x10 not set in scope menu | Amplitude reads 10x too high (120V instead of 12V) | Ask student to locate the probe factor setting in the scope's channel menu. Set to x10. Re-read. |
| Measuring resistance while board is powered | Reading fluctuates wildly, may read negative | Immediately ask: "Is the supply off?" Have them turn it off, wait 20 seconds, and remeasure. Discuss what they saw. |
| Not waiting for caps to discharge | Resistance reading starts high and decays visibly on screen | Use this as a teaching moment — show them the reading decaying in real time. Explain the capacitor discharge behaviour. |

---

## Debrief Questions (Last 5 minutes of session)

Bring the group together. Ask these questions to the whole group — invite responses, do not lecture.

1. "In Task 2, two of you found the fault in Segment 1, and two found it in Segment 2. What does that tell us about the fault board? Could you both be right?"
   *(Intended insight: faults can span segment boundaries; the segment with the highest reading contains most of the fault, but adjacent measurements confirm localisation.)*

2. "In Task 3, one pair found continuity tone across the broken segment. What would have happened if they'd stopped there and not followed up with resistance mode?"
   *(Intended insight: a high-resistance fault can still pass continuity beep threshold. Continuity is a screening test, not a pass/fail verdict.)*

3. "In Task 4, when you switched to AC coupling, what happened to the waveform? Why would that matter if you were trying to measure an injector enable signal?"
   *(Intended insight: AC coupling removes DC offset, so you lose the absolute voltage level. For injector signals that transition between 0V and 12V, losing the DC reference means you cannot determine whether the ECU is driving the output rail-to-rail or not.)*

4. "Which of today's four tasks do you think you will use most in actual ECU repair, and why?"
   *(Open discussion — no wrong answer. Encourage students to link back to the hook story from the theory session about the P0106 fault.)*

---

## Station Reference Card (Appendix — print and laminate one per station)

```
ECUHR MODULE 2 — STATION REFERENCE CARD

METER SETTINGS QUICK GUIDE
----------------------------
Diode test:     Diode symbol mode | Red = anode | Expect 0.2–0.7V fwd, OL rev
Voltage drop:   DC mV range | Red = upstream | Black = downstream | Live circuit
Continuity:     Tone symbol | Power OFF | Follow up with Ω if unsure
Resistance:     Ω mode | Power OFF | Caps discharged | Leads nulled first

HEALTHY DIODE REFERENCE
------------------------
Silicon (1N4148):  0.55–0.70V fwd   |  OL rev
Schottky:          0.20–0.40V fwd   |  OL rev
TVS (clamping):    0.20–0.60V fwd   |  OL rev
Shorted diode:     ~0V both ways    |  FAULT
Open diode:        OL both ways     |  FAULT

VOLTAGE DROP LIMITS (PCB TRACES)
----------------------------------
< 0.05V drop:   Good
0.05–0.10V:     Marginal — investigate further
> 0.10V drop:   Definitive fault — locate and repair

5V REFERENCE LIMITS
---------------------
Acceptable range: 4.95V – 5.05V
Below 4.95V: sensor out of calibrated range
Above 5.05V: investigate regulator or load short

OSCILLOSCOPE QUICK SETUP (ECU SIGNALS)
----------------------------------------
Coupling:      DC (never AC for ECU work)
Probe:         x10 — confirm in channel menu
Volts/div:     2V/div for 0–5V signals | 5V/div for 12V signals
Timebase:      500μs/div for 500Hz PWM | adjust per signal
Trigger:       Edge | Rising | Ch1 | Level at mid-signal

FAULT RESISTANCE FORMULA
--------------------------
R = V_drop ÷ I_load
e.g.: 0.14V drop, 35mA load → R = 0.14 ÷ 0.035 = 4.0Ω  (FAULT)
```

---

*End of SESSION-02H Framework*
