# SESSION-05H: Protection & Filtering Lab
## Hands-On Workshop Framework

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 3 — ECU Architecture, Protection & Filtering (Days 4–6)
**Session:** Day 5 — Hands-on
**Duration:** 90 minutes
**Format:** Structured workshop — paired stations with oscilloscope and multimeter
**Max Class Size:** 16 students (8 stations, 2 students per station)

---

## Session Outcomes

| SO ID | Description | Bloom |
|-------|-------------|-------|
| so-3-2-2 | Identify reverse polarity protection circuits and test their function with a multimeter | Apply |
| so-3-2-3 | Trace the voltage path from battery connector to main power rail, naming each protection stage | Apply |
| so-3-3-3 | Identify ferrite beads on real ECU power traces and confirm by DC resistance measurement | Apply |
| so-3-4-1 | Use oscilloscope to observe noise on a supply rail before and after a filter | Apply |

---

## Workshop Overview

Students work in pairs on one ECU (powered on bench supply) and one oscilloscope. The session has four activities that together give students practical experience tracing, identifying, and measuring every protection and filtering element covered in Session 05T. The final activity — oscilloscope noise capture before and after a filter — is the most memorable and should be protected in timing even if earlier activities run long.

---

## Equipment and Materials List

### Per Station (2 students)
- 1 x automotive ECU on bench (powered from bench supply — see power setup below)
  - Must have: accessible power entry TVS or protection diode; identifiable ferrite beads; accessible test points on the supply path; CAN transceiver with accessible supply line
  - Preferred: an ECU where the pi-filter sections are visible (not potted/underfill) and labelled on silkscreen
- 1 x bench DC power supply, 0–20V, 3A minimum, with current limiting set to 1A
- 1 x digital multimeter (Fluke 87V or equivalent) with fine probe tips
- 1 x 2-channel oscilloscope, 20MHz minimum bandwidth (50MHz preferred)
  - Channel 1: for "before filter" measurement
  - Channel 2: for "after filter" measurement
  - Both channels configured for AC coupling at start of Activity 4
- 1 x set of fine oscilloscope probe tips (standard tips — not the large automotive probe set)
- 1 x Reference Designator Quick-Reference card (laminated, from Day 4)
- 1 x Failure Mode Summary Table (from Session 05T slide 29 — printed, one per student)
- 1 x Activity Worksheet (printed, individual per student — see worksheet content below)

### Room / Shared Equipment
- ESD mats on all benches — connected and verified before session starts
- ESD wrist straps — one per student, verified working
- 1 x instructor demonstration bench (front of room) — same setup as student stations, connected to room projector for live oscilloscope display
- Anti-static component trays for loose ECUs during transit from storage
- Spare probe tips available at instructor bench

### Power Setup — Important
Each ECU must be pre-wired before the session starts:
- Battery positive (+12V) from bench supply → ECU battery pin (identified from connector pinout or silkscreen)
- Ground from bench supply → ECU ground pin
- Bench supply current limit: 1.0A (prevents damage if a wiring error is made)
- Do NOT connect ignition (IGN) line unless the specific ECU requires it to power on — for this session, the ECU only needs power; it does not need to communicate or run an engine
- Verify the ECU draws some current when powered (indicates it is live) before issuing to students

**Instructor note:** Several activities involve measuring live circuits with the ECU powered. Students must understand that they are working on a live low-voltage DC circuit. The bench current limiting at 1A provides a safety backstop. ESD protocol still applies.

---

## Session Timeline

| Time | Phase | Activity |
|------|-------|----------|
| 0:00–0:08 | Safety briefing | Live circuit protocol, ESD, probe technique |
| 0:08–0:13 | Instructor demo | Brief demo of Activity 1 on reference ECU |
| 0:13–0:30 | Activity 1 | Identify and test reverse polarity protection |
| 0:30–0:50 | Activity 2 | Trace power path from connector to MCU supply |
| 0:50–1:05 | Activity 3 | Identify and verify ferrite beads |
| 1:05–1:25 | Activity 4 | Oscilloscope — noise before and after filter |
| 1:25–1:30 | Debrief and close | Key observations, Day 6 preview |

---

## Safety Briefing Script (0:00–0:08)

> "Today's session is different from yesterday. The ECUs are powered. Before anyone touches anything, we cover live circuit safety.
>
> The bench supply is set to 12V and 1A current limit. This is low-voltage DC — the same as a car battery. It will not electrocute you. However, if you bridge two pins with a probe, you can create a short circuit that destroys a component, damages a trace, or triggers the current limit and kills power to the ECU.
>
> Three rules for working on live circuits today:
>
> Rule 1 — Ground reference first. Before every measurement, touch one probe to the known-good ground test point and verify your reading is 0V. Then probe the target point. Never guess your ground reference.
>
> Rule 2 — One probe moving at a time. When you reposition a probe on a live ECU, move one probe at a time. Both probes in the air simultaneously means no reference. One probe slipping means a potential short.
>
> Rule 3 — If in doubt, power down. If you need to reposition an ECU on the bench, access the bottom of the board, or swap connections — power down the bench supply first. It takes 3 seconds. It prevents an inadvertent short.
>
> ESD wrist straps: wear them throughout. The ECU is live but you are still connected to it through your probes. ESD protocol is not suspended because the board is powered."

---

## Instructor Demonstration (0:08–0:13)

Using the instructor reference ECU on the front bench:

1. Establish ground reference at TP_GND — show the reading (0.00V), explain why this is the first step every single time
2. Measure the battery input pin at the connector — show reading (12V from bench supply)
3. Locate the TVS diode or reverse polarity diode near the power input — point it out on the board, read its reference designator from the silkscreen
4. Perform a rapid diode test across it (ECU powered down for this step) — show the forward and reverse readings
5. Power the ECU back on
6. Briefly show what Activity 1's worksheet asks students to do

> "Everything I just did in 3 minutes is what you are doing in Activity 1. Your ECU may look different from this one but the methodology is identical. Find the connector, follow the power traces, find the first protection component, test it."

---

## Activity 1: Identify and Test Reverse Polarity Protection (0:13–0:30, 17 minutes)

**Learning focus:** so-3-2-2 — Identify reverse polarity protection circuits and test with multimeter

### Background reminder (30 seconds verbal, do not re-lecture):
> "Reverse polarity protection is the first protection component after the connector and fuse. It may be a large diode (series diode method) or a P-channel MOSFET (low-drop method). Your job is to find it, identify which method is used on your ECU, and verify it is functioning."

### Student Procedure:

**Step 1:** With ECU powered on, measure and record the voltage at the battery input connector pin. Use TP_GND as reference.
Record: Battery input voltage = ________ V

**Step 2:** Trace the thick power trace from the battery input pin. The first significant component it passes through (not a fuse) is the reverse polarity protection.
Power down the ECU before Step 3.

**Step 3:** Locate the reverse polarity protection component.
Circle which method is used on your ECU: **Series diode method** / **MOSFET method** / **Cannot determine**
Record the reference designator: ________

**Step 4:** With ECU powered down, perform a diode test across the protection component (multimeter in diode function mode):
- Forward direction (positive probe toward battery, negative toward downstream): Reading = ________ V
- Reverse direction (swap probes): Reading = ________

**Step 5:** Interpret your readings:
- Forward reading 0.5–0.7V, reverse reading OL = healthy diode/MOSFET body diode
- Forward reading near-zero in both directions = shorted (failed) protection component
- Both directions OL = open (failed) protection component

Record your assessment: **Healthy / Shorted / Open / Inconclusive**

**Step 6:** Power ECU back on. Measure voltage on both sides of the protection component:
- Before protection (battery side): ________ V
- After protection (protected rail side): ________ V
- Voltage drop across the protection: ________ V

For a series diode method: expected drop = 0.5–0.7V
For MOSFET method: expected drop = 0.1V or less

### Checkpoint for instructor at ~0:25:
- Has the student correctly identified the protection component type?
- Are both voltage measurements showing correct polarity (positive on protected side)?
- Is the voltage drop in the expected range for the method used?

**Common error:** Student cannot find the protection component because they are tracing signal traces rather than the main power trace. Prompt: "The main power trace is the thickest copper trace on the board. It comes from the highest-current pins on the connector. Follow the thick trace — not a thin one."

**Common error:** Student measures 0V drop across a MOSFET-type protection and believes it is shorted. Prompt: "A MOSFET reverse polarity protection is designed to have a very low forward drop — sometimes less than 0.1V. Near-zero drop in forward direction, combined with high reverse impedance on the diode test, indicates a healthy MOSFET protection — not a fault."

---

## Activity 2: Trace the Voltage Path — Connector to MCU Supply Rail (0:30–0:50, 20 minutes)

**Learning focus:** so-3-2-3 — Trace the voltage path from battery connector to main power rail

### Background reminder (30 seconds verbal):
> "You traced the path to the reverse polarity protection in Activity 1. Now trace the complete path from the connector through every stage to the regulated 5V supply at the MCU. You are building a map of the entire power entry section."

### Student Procedure:

Students complete a Power Path Trace Worksheet — a table with blank rows to fill in:

---
**Power Path Trace Worksheet**

Starting point: Battery connector pin (measured voltage: ________ V)

| Stage | Component Found (Reference Designator) | Voltage Before | Voltage After | Notes |
|---|---|---|---|---|
| 1 — Fuse | | | | |
| 2 — Transient protection (TVS) | | | | Diode test result: |
| 3 — Reverse polarity protection | | | | From Activity 1 |
| 4 — Bulk capacitor | | N/A | | Cap value from marking: |
| 5 — Ferrite bead (if present) | | | | |
| 6 — Voltage regulator input | | | | Regulator reference designator: |
| 7 — Voltage regulator output | | | | Measured output voltage: |
| 8 — Bypass cap at MCU VCC | | N/A | | Located within ___mm of MCU |

---

**Instructions:**

For each stage, the student must:
1. Physically locate the component on the PCB using silkscreen markings and reference designators
2. Measure the voltage at the input and output side of the component (where applicable)
3. Record the reference designator
4. Note any voltage drop that indicates the component is doing its job (or a fault)

The pathway should end at the MCU VCC pin or a test point close to it.

### Checkpoint for instructor at ~0:43:
- Has the student found the voltage regulator? (This is the stage where the voltage drops from 12V range to 5V or 3.3V — the most significant voltage change in the chain)
- Is the regulated output voltage in the expected range (4.8–5.2V for a 5V regulator)?
- Has the student noted the ferrite bead if present, and verified it shows near-zero voltage drop (confirming it is not open circuit)?

**Common error:** Student reaches the voltage regulator but does not know which side is input and which is output. Prompt: "Measure both sides. One will read close to 12V — that is the input. One will read close to 5V — that is the output. The regulator is always between the two."

**Common error:** Student cannot find the MCU supply pin because the MCU has many pins. Prompt: "Look for the VCC test point — usually labelled TP_5V or VCC near the MCU. Alternatively, find a bypass capacitor with a C reference designator within 2–3mm of the MCU and probe the pad that is not connected to ground."

---

## Activity 3: Identify and Verify Ferrite Beads (0:50–1:05, 15 minutes)

**Learning focus:** so-3-3-3 — Identify ferrite beads on real ECU power traces

### Background reminder (20 seconds verbal):
> "Ferrite beads look exactly like resistors. The only reliable way to identify them on an unknown board is: L prefix reference designator, plus DC resistance near zero. Let us find every ferrite bead on this ECU."

### Student Procedure:

**Step 1:** Power down the ECU before any resistance measurements.

**Step 2:** Starting from the power entry, trace along each supply branch and look for components with:
- An L prefix reference designator on the silkscreen
- A small rectangular body identical to a resistor in 0402 or 0603 package
- Placement in series with a power trace (both pads connect to the trace, not across it)

Record all ferrite beads found:

| Reference Designator | Location (describe: near MCU / near CAN transceiver / on main rail / other) | DC Resistance Measured |
|---|---|---|
| | | |
| | | |
| | | |

**Step 3:** For each ferrite bead found, measure DC resistance with the multimeter. Expected: 0.1 to 2 ohms.

If any bead reads OL (open circuit): flag this as a potential fault. Record it.
If any bead reads above 10 ohms but below OL: measure again — this may be an in-circuit parallel path effect. Note it for instructor review.

**Step 4:** Pick one ferrite bead that is on the supply trace feeding the MCU (or CAN transceiver). Power up the ECU and measure:
- Voltage before the ferrite bead (supply rail side): ________ V
- Voltage after the ferrite bead (IC supply side): ________ V
- Voltage drop: ________ V

Expected drop for a healthy ferrite bead: less than 0.1V (typically 0.02–0.05V at normal ECU operating current). A significant voltage drop (>0.5V) indicates the bead is degraded or a series resistance has developed.

### Checkpoint for instructor at ~1:02:
- Has the student found at least two ferrite beads?
- Are DC resistance readings in the near-zero range for all beads?
- Has the student identified whether any bead appears open or anomalous?

**Common error:** Student finds a component with an L prefix but it reads 47 ohms — this is an actual inductor or a resistor with a misread designator. Prompt: "Check the designator again carefully under the loupe. Also: is the component physically in series with a power trace, or between two signal nets? Inductors used for EMC on signal lines do have measurable resistance. The key is location — ferrite beads are on supply traces."

---

## Activity 4: Oscilloscope — Noise Before and After a Filter (1:05–1:25, 20 minutes)

**Learning focus:** so-3-4-1 (practical) — Use oscilloscope to observe noise before and after a filter

This is the signature activity of the session. Students see directly that the filtering components they have been studying are doing real work — measurable, visible work on the oscilloscope. This activity should be protected in timing.

### Background reminder (1 minute verbal with oscilloscope setup):
> "The ECU's supply rail is not clean. Even with a bench power supply, the ECU itself generates noise — every time the MCU executes an instruction, every time the CAN transceiver toggles a bit, current spikes generate noise on the rail. We are going to capture that noise with the oscilloscope and show that the ferrite bead and bypass cap are actively suppressing it."

### Oscilloscope Setup (instructor walks through this with the class before they start):
1. Set both channels to **AC coupling** — this removes the DC component (12V or 5V) and shows only the AC noise riding on the supply
2. Set timebase to 20µs/div
3. Set vertical scale to 50mV/div (start here; adjust once signal is visible)
4. Set trigger to auto — edge trigger on Channel 1

### Student Procedure:

**Step 1:** Identify a ferrite bead on the ECU that is on the MCU supply trace or a CAN transceiver supply trace — one of the ferrite beads found in Activity 3.

**Step 2:** Connect Channel 1 probe to the test point or via pad on the **supply side** of the ferrite bead (upstream of the bead, closer to the power connector).
Connect the probe ground lead to TP_GND (or nearest ground via).

**Step 3:** Connect Channel 2 probe to the test point or via pad on the **IC side** of the ferrite bead (downstream of the bead, closer to the IC).
Connect the probe ground lead to the same TP_GND.

**Step 4:** Power up the ECU. Observe both channels. Adjust the vertical scale until the noise waveform is visible on both channels.

**Step 5:** Record your observations:

Channel 1 (before filter) — approximate peak-to-peak noise voltage: ________ mV
Describe the waveform shape (random spikes / periodic oscillation / smooth ripple / other): ________

Channel 2 (after filter) — approximate peak-to-peak noise voltage: ________ mV
Is the noise reduced compared to Channel 1? **Yes / No / About the same**
Approximate noise reduction ratio (Ch1 amplitude / Ch2 amplitude): ________

**Step 6:** Sketch both waveforms in the space provided on the worksheet. Annotate with measured voltages and time scale.

**Step 7 (if time permits):** Adjust the oscilloscope to 500ns/div to look for higher-frequency noise components. What do you observe?

### Expected Observations
On a real powered ECU:
- Channel 1 (before filter): 50–300mV peak-to-peak noise, irregular waveform with spikes at MCU clock frequency harmonics and CAN transceiver switching
- Channel 2 (after filter): 10–80mV peak-to-peak noise, noticeably reduced compared to Channel 1
- Ratio: typically 3:1 to 10:1 noise reduction across a single ferrite bead + bypass cap (this is the L-filter configuration)

If a pi-filter is accessible (input cap, bead, output cap as three identifiable components), connect Channel 1 before the input cap and Channel 2 after the output cap — the noise reduction ratio will be much larger.

**Note to instructor:** Results vary significantly by ECU type, bench supply quality, and which supply rail is being measured. The key learning is not the specific numbers — it is the visual demonstration that (a) noise exists on a real supply rail, and (b) the filter components are measurably reducing it. Even a 2:1 ratio is compelling when students can see both traces simultaneously.

### Checkpoint for instructor at ~1:20:
- Do students have two traces visible on the oscilloscope?
- Is AC coupling engaged? (If DC coupling is used, the 5V or 12V DC offset makes the noise invisible at any reasonable vertical scale)
- Is there a measurable and visible difference between the two channels?
- If no visible difference: help student reposition probes — they may both be on the same side of the ferrite bead

**Common problem — no noise visible on either channel:** The bench supply itself is very clean and the ECU is in a low-activity state. Solutions: increase timebase sensitivity to 5mV/div; connect a CAN analyser tool to the ECU connector to generate CAN bus activity; or acknowledge and discuss why bench supply ECU measurements are quieter than in-vehicle.

**Common problem — both channels show the same noise:** The probes are on the same side of the ferrite bead. Verify probe placement — one must be upstream (supply side), one downstream (IC side) of the same ferrite bead.

---

## Debrief (1:25–1:30)

Address the class with four quick points:

**1. What did you find in Activity 1 and 2?**
Ask: "Did anyone find a protection component that looked suspicious — unusual diode test reading, unexpected voltage drop?" Take examples from the class. This reveals whether any training ECUs have known faults that can be discussed.

**2. The ferrite bead identification result:**
Ask: "How many ferrite beads did you find on your ECU? Where were they placed?" Compare across the class. ECUs from different manufacturers and applications will have different bead placement strategies. Discuss the pattern: beads near sensitive ICs, not near robust driver circuits.

**3. The oscilloscope result:**
This is the most impactful moment of the debrief. Ask one pair with a clear noise reduction result to display their oscilloscope traces on the projector.

> "This is what those 0402 components you nearly missed under the loupe are doing every millisecond the engine is running. The noise on the supply rail is real — you have measured it. The filter components are real — you have seen them reduce it. This is why bypass capacitors cannot be missing, and why ferrite beads cannot be open circuit."

**4. Connection to failure modes:**
Ask: "Based on what you saw today, what would happen to the oscilloscope traces if the bypass capacitor on the IC side of the ferrite bead was missing?" Expected answer: Channel 2 noise would increase significantly — the IC's VCC pin would no longer be locally bypassed, and all the noise that makes it through the ferrite bead would reach the IC directly.

---

## Common Mistakes and Instructor Responses

| Mistake | Instructor Response |
|---|---|
| Probing live ECU with both probes in the air at the same time | Remind Rule 2: one probe moving at a time. If repositioning, hold the stationary probe firmly in place first. |
| Using DC coupling on oscilloscope for Activity 4 | "Switch to AC coupling — press the channel button, navigate to coupling. The 5V DC is overwhelming the noise signal." |
| Both oscilloscope probes on the same side of the ferrite bead | "Identify the ferrite bead on the board. One probe goes here — on the trace before the bead. The other probe goes here — on the trace after the bead. They must be on opposite sides." |
| Reading voltage drop of 0.6V across a MOSFET reverse polarity protection and flagging as a diode | "That is within the expected range for a MOSFET body diode — 0.4 to 0.7V forward. The protection is likely healthy. What matters is the reverse direction — does it block?" |
| Cannot find the voltage regulator in the power path trace | "Look for an IC with a 3-pin TO-252 or SOT-23 package, or a larger IC with heat spreader — the regulator will be the component where voltage drops from 12V to 5V. That step change identifies it." |

---

## Activity Worksheet Summary

Each student completes the following during the session (printed worksheet, one per student):

- Activity 1 results: protection component identified, reference designator, diode test readings, voltage drop, health assessment
- Activity 2 results: Power Path Trace table (8 rows from connector to MCU supply)
- Activity 3 results: ferrite beads found (table with designator, location, DC resistance), voltage drop across selected bead
- Activity 4 results: noise measurements before and after filter, waveform sketches, noise reduction ratio, observations at higher timebase

Worksheets are collected at end of session and returned with instructor feedback before Day 7.

---

## Day 6 Preview (final 30 seconds)

> "Tomorrow we move from power supply and filtering to the output side of the ECU — the circuits that actually drive loads. Injectors, solenoids, relays. Low-side drivers and high-side drivers. Flyback diodes. And thermal management — why ECUs fail in summer when they worked all winter.
>
> Bring your multimeter and oscilloscope skills. We will be looking at injector drive waveforms and using a thermal camera."
