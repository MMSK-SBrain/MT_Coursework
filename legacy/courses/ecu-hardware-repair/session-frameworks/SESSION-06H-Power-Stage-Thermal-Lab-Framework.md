# SESSION-06H: Power Stage & Thermal Lab
## Hands-On Workshop Framework

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 3 — ECU Architecture, Protection & Filtering (Days 4–6)
**Session:** Day 6 — Hands-on
**Duration:** 90 minutes
**Format:** Structured workshop — paired stations, oscilloscope capture analysis and thermal camera investigation
**Max Class Size:** 16 students (8 stations, 2 students per station)

---

## Session Outcomes

| SO ID | Description | Bloom |
|-------|-------------|-------|
| so-3-5-3 | Analyse an oscilloscope capture of an injector drive signal and identify anomalies | Analyze |
| so-3-5-4 | Test a suspected failed output driver IC using multimeter resistance measurements | Apply |
| so-3-6-2 | Use a thermal camera to identify hot components on a powered ECU and rank them by thermal risk | Apply |
| so-3-6-3 | Inspect thermal paste/pad application on an ECU power stage and assess adequacy | Evaluate |

---

## Workshop Overview

This session has four activities. Activities 1 and 2 focus on the driver circuit and waveform analysis. Activities 3 and 4 focus on thermal inspection. The session is the capstone practical for Module 3 — it draws on knowledge from all three days and produces a diagnostic outcome that mirrors real workshop practice.

Activity 1 (waveform analysis) uses printed captures rather than live signals — this ensures consistency across all stations and allows carefully selected fault signatures to be examined. Activity 3 (thermal camera) uses the workshop thermal camera shared across stations, so the instructor must manage station rotation for that activity.

---

## Equipment and Materials List

### Per Station (2 students)
- 1 x multimeter (Fluke 87V or equivalent) with fine probe tips
- 1 x ECU on bench supply (12V, 1A limit) — powered on
  - Required: visible output driver section (MOSFETs or driver IC with accessible test points)
  - Required: accessible power stage with thermal paste/pad visible (housing partially removed or a section of the power stage is exposed)
  - Preferred: ECU with a known failed output driver for Activity 2 testing (one channel shorted, one channel open — pre-tested by instructor)
- 1 x set of printed Waveform Analysis worksheets for Activity 1 (printed on A4, 1 per student — see below)
- 1 x Activity Worksheet for Activities 2–4 (printed, 1 per student)
- 1 x fine dental pick or scribe tool (for inspecting thermal paste coverage)

### Shared Room Equipment
- 1 x FLIR E5 or equivalent thermal camera (class shares — instructor manages rotation)
  - Alternatively: FLIR ONE Pro smartphone attachment on a fixed stand showing live feed
  - Minimum specification: 80×60 pixel thermal resolution; temperature range 0–250°C; ±2°C accuracy
- 1 x powered reference ECU for thermal camera demonstration (instructor bench — different ECU from student bench ECUs, with clearly visible hotspots)
- 1 x projector connection for oscilloscope or thermal camera display (used for instructor demo and selected student result sharing at debrief)

---

## Session Timeline

| Time | Phase | Activity |
|------|-------|----------|
| 0:00–0:07 | Safety briefing and setup | Live circuit protocol review, thermal camera safety |
| 0:07–0:15 | Instructor demo | Activity 2 walkthrough on reference ECU |
| 0:15–0:40 | Activity 1 | Injector waveform analysis — four captures |
| 0:40–0:55 | Activity 2 | Driver IC resistance testing with multimeter |
| 0:55–1:15 | Activity 3 | Thermal camera scan — station rotation |
| 1:15–1:25 | Activity 4 | Thermal paste/pad inspection |
| 1:25–1:30 | Debrief and Module 3 close | Key findings, Module 4 preview |

---

## Safety Briefing Script (0:00–0:05)

> "Quick briefing before we start. Three points:
>
> Point 1 — live circuits. The ECUs are powered today, same as yesterday. Same rules: ground reference first, one probe moving at a time, power down before repositioning the board.
>
> Point 2 — thermal camera. The ECUs we scan today may have components operating at 80 to 120°C. If you touch the power stage of a hot ECU, you will burn your finger. We do not touch components on a powered ECU that may be hot. We use the thermal camera to look, not our fingers. Before touching any component during Activity 4, power down the ECU and wait 60 seconds.
>
> Point 3 — ESD. Wrist straps on, connected. Still applies even though the ECU is powered."

---

## Instructor Demonstration (0:05–0:15)

### Part A — Activity 2 preview (resistance testing) on reference ECU:
Using the instructor reference ECU (powered down), demonstrate:
1. Locate the output driver IC or MOSFET on the board using silkscreen reference designator
2. Identify the drain, source, and gate pins from the package orientation and datasheet pin diagram (projected on screen)
3. Perform resistance measurement in diode test mode: drain-to-source, source-to-drain, gate-to-source
4. Show what a healthy MOSFET reads vs what a shorted MOSFET reads (use a pre-failed MOSFET for comparison)

> "In Activity 2, your ECU has one healthy output driver channel and one that has been pre-failed. Your job is to find the failed channel using exactly this technique. I am showing you what healthy looks like — you determine what the fault signature is."

### Part B — Thermal camera overview (2 minutes):
Power on the instructor reference ECU. Allow 3 minutes to warm up while doing the Part A demonstration. Then:
1. Show the thermal camera display projected on screen
2. Identify the hottest components — name them
3. Show how to read the temperature scale and identify the colour coding
4. Show how to use the camera's spot measurement function to read a specific component's temperature

---

## Activity 1: Injector Waveform Analysis (0:15–0:40, 25 minutes)

**Learning focus:** so-3-5-3 — Analyse oscilloscope captures and identify fault signatures

### Overview
Students receive four printed oscilloscope capture sheets. Each sheet shows one complete injector drive cycle. Students analyse each capture, answer questions, and make a diagnostic conclusion.

**This activity does not require a live oscilloscope.** Students work from printed captures to ensure all students analyse the same signals and to allow precisely controlled fault signatures.

---

### Waveform Capture Descriptions (for instructor to source or create)

**Capture A — Healthy peak-and-hold injector:**
- X-axis: 0 to 10ms total; injector ON for 5ms
- Y-axis: 0 to 50V
- Phase 1 (0–1.5ms): voltage drops from 12V to near 0V as driver turns ON; current rises rapidly (current trace if dual-channel) to ~8A peak
- Phase 2 (1.5–5ms): driver PWM switching visible as rapid transitions; current holds at ~2A
- Phase 3 (5ms): driver turns OFF; voltage spike to ~14V (supply + diode drop), then decays
- Freewheeling plateau: visible at ~14V for ~2ms before decaying to 0V

**Capture B — Missing flyback diode:**
- Same injector pulse structure
- Phase 3 (turn-off): voltage spikes sharply to 80–120V with no freewheeling plateau — spike decays immediately to 0V
- No controlled freewheeling period visible
- Diagnostic finding: flyback diode missing or failed open

**Capture C — Overcurrent / shorted coil:**
- Injector turns ON normally
- Peak current is reached in approximately half the expected time (fast current rise due to lower coil resistance)
- Driver current-limits and goes into fault mode — PWM switching stops abruptly partway through the injection period
- Diagnostic finding: injector coil resistance lower than specification (windings shorted), driver overcurrent protection activated

**Capture D — Open circuit injector / broken harness:**
- Driver commands output (gate signal visible if dual-channel)
- Output voltage remains near supply voltage (+12V) — does not drop to near 0V
- No current flows (no current trace activity)
- No freewheeling event at turn-off
- Diagnostic finding: open circuit in load path — injector coil open, connector not engaged, or broken wire

---

### Student Waveform Analysis Worksheet

For each capture (A through D), students complete:

**Capture: ____**

1. Is a freewheeling plateau visible after the driver turns off? **Yes / No**

2. What is the peak voltage reached at driver turn-off?
________ V

3. Is the freewheeling voltage at approximately (supply voltage + 0.7V)? **Yes / No / Not applicable**

4. Does the output voltage drop to near 0V when the driver is commanded ON? **Yes / No**

5. Is the peak current phase followed by a reduced-current hold phase (peak-and-hold pattern)? **Yes / No / Cannot determine**

6. Diagnosis — circle the most likely fault:
**Healthy** / **Missing flyback diode** / **Shorted coil / overcurrent** / **Open circuit (no load current)**

7. In one sentence, explain the evidence that led to your diagnosis:
_______________________________________________

8. What is the recommended next action for this vehicle?
_______________________________________________

---

### Instructor Answers (not given to students until debrief):

| Capture | Diagnosis | Key Evidence |
|---|---|---|
| A | Healthy | Freewheeling plateau at ~14V, normal peak-and-hold current profile |
| B | Missing flyback diode | Voltage spike to 80–120V at turn-off, no controlled freewheeling plateau |
| C | Shorted injector coil / overcurrent | Fast current rise, driver fault mode mid-cycle |
| D | Open circuit load | Output voltage stays at supply voltage throughout; no current; no freewheeling |

### Checkpoint for instructor at ~0:32:
- Has each student completed all four captures?
- Are the diagnoses for B and D correct? (These are the two unambiguous captures — if a student cannot diagnose these, they need a prompt)
- Are students able to identify the freewheeling plateau on Capture A vs the spike on Capture B?

**Common difficulty — Capture C:** Students often misread the overcurrent capture. The key is to look at the shape of the current trace or the abrupt change in driver switching behaviour mid-cycle. Prompt: "Compare the turn-on behaviour in Capture C to Capture A. How quickly does the current reach peak? What does that tell you about the coil resistance?"

---

## Activity 2: Driver IC Resistance Testing (0:40–0:55, 15 minutes)

**Learning focus:** so-3-5-4 — Test a suspected failed output driver IC

### Overview
Students use the multimeter to test the output driver section on their bench ECU. The ECU has been pre-prepared with one healthy channel and one failed channel (instructor selects and marks these before the session — the student must find which is which).

**Power down the ECU before Activity 2 begins.**

### Student Procedure:

**Step 1:** With ECU powered down, identify the output driver stage. Locate the driver MOSFETs (Q prefix or the driver IC with separate power transistors — U prefix with MOSFET external components).

For each accessible output channel, complete the test table:

**Multimeter Settings:** Diode test function for Steps 2–4. Resistance (200Ω range) for Step 5.

| Measurement | Channel 1 Reading | Channel 2 Reading |
|---|---|---|
| Drain-to-source (positive probe to drain, negative to source) | | |
| Source-to-drain (reverse probes) | | |
| Gate-to-source (positive probe to gate, negative to source) | | |
| Source-to-drain resistance (ohms mode) | | |

**Expected readings for a healthy N-channel MOSFET (unpowered, gate undriven):**
- Drain-to-source (forward diode test): ~0.5–0.7V (body diode forward)
- Source-to-drain (reverse diode test): OL (blocking)
- Gate-to-source: OL (gate oxide — very high impedance)
- Source-to-drain resistance: OL or very high (hundreds of kΩ to MΩ)

**Expected readings for a shorted MOSFET (failed drain-source short):**
- Drain-to-source: near 0V (very low forward voltage — shorted junction)
- Source-to-drain: near 0V (shorted in both directions)
- Gate-to-source: may also read low if gate oxide has failed
- Source-to-drain resistance: 0.1 to 10 ohms

**Expected readings for an open MOSFET (failed open drain-source):**
- Drain-to-source: OL (body diode also open — uncommon but possible)
- Source-to-drain: OL
- Source-to-drain resistance: OL

**Step 2:** Based on your measurements, complete the assessment:

| Channel | Assessment (Healthy / Shorted / Open / Cannot Determine) |
|---|---|
| Channel 1 | |
| Channel 2 | |

**Step 3:** If a shorted channel is identified, describe what the vehicle symptom would be for this output channel. (Refer to your knowledge of low-side vs high-side driver operation — is this channel low-side or high-side? What load does it drive?)

Vehicle symptom: _______________________________________________

**Step 4:** If you were repairing this ECU, what is the minimum complete repair action required?
(Think: is replacing the MOSFET sufficient, or is there a root cause that must also be addressed?)

Minimum repair: _______________________________________________

### Checkpoint for instructor at ~0:50:
- Has the student correctly identified which channel has the fault?
- Are the measurements internally consistent? (A shorted MOSFET should read near-zero in both diode test directions, not just one)
- Has the student identified the correct repair action — not just replacing the MOSFET, but also investigating whether the flyback diode needs to be verified or replaced?

**Common error:** Student reads a healthy body diode forward voltage (0.6V) and flags it as a fault. Prompt: "What is the expected forward voltage of a diode? 0.5 to 0.7V is completely normal. A shorted MOSFET reads near-zero in the diode test direction — the junction conducts so easily that there is almost no forward voltage. 0.6V in one direction and OL in the other is healthy."

**Common error:** Student cannot identify which pins are drain, source, and gate. Prompt: "Look up the package type in the datasheet — the package outline diagram will label D, S, G. Alternatively: for a D2PAK package, the large central tab is always the drain (connected to the heatsink pad); the remaining pins are gate and source."

---

## Activity 3: Thermal Camera Investigation (0:55–1:15, 20 minutes)

**Learning focus:** so-3-6-2 — Use a thermal camera to identify hot components and rank them by thermal risk

### Rotation Setup
The thermal camera is shared across 8 stations. Manage two parallel rotations:
- **Stations 1–4:** Perform Activity 3 first (0:55–1:05), then Activity 4 (1:05–1:15)
- **Stations 5–8:** Perform Activity 4 first (0:55–1:05), then Activity 3 (1:05–1:15)

Each station has 10 minutes with the thermal camera. During the other 10 minutes, they perform the thermal paste inspection (Activity 4).

If a FLIR ONE or fixed-mount thermal camera is available on each bench (e.g. via a laptop connection), all stations can perform Activity 3 simultaneously.

### Student Procedure:

**Step 1:** Before using the thermal camera, allow the powered ECU to reach thermal steady state — the ECU should have been powered on for at least 5 minutes before being scanned. If not, wait.

**Step 2:** Set the thermal camera to the following settings (instructor demonstrates on the FLIR unit):
- Temperature range: 20°C to 150°C (auto-range if manual range is not available)
- Emissivity: 0.95 (suitable for most PCB materials, black plastic components, and anodised aluminium)
- Colour palette: iron palette or rainbow — provides best contrast for identifying temperature gradients

**Step 3:** Hold the camera 20–25cm above the ECU surface. Scan the entire board surface. Identify all visible hotspots.

For each hotspot found, complete the Thermal Scan Record:

| Component (Reference Designator or Location Description) | Temperature Reading (°C) | What Type of Component (MOSFET / regulator / resistor / IC / other) | Thermal Risk Assessment |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

**Thermal Risk Assessment Guide:**

| Temperature | Assessment |
|---|---|
| Below 60°C | Low risk — normal operation |
| 60–85°C | Moderate — monitor; acceptable at low ambient |
| 85–110°C | Elevated — investigate if ambient is low; calculate Tj |
| Above 110°C | High risk — component may be near or exceeding junction temperature limit |
| Above 130°C | Critical — component is almost certainly near failure threshold |

**Step 4:** Rank the three hottest components in order from hottest to coolest. Record the reference designator and temperature for each:

| Rank | Component | Temperature |
|---|---|---|
| 1 (hottest) | | |
| 2 | | |
| 3 | | |

**Step 5:** For the hottest component, calculate the estimated junction temperature:

- Measured surface temperature (approximately equal to case temperature): ________ °C
- Look up Rθjc for this component package type (use the package type reference chart provided):
  - D2PAK: Rθjc approximately 1–3°C/W
  - TO-252: Rθjc approximately 2–5°C/W
  - SOIC-8: Rθjc approximately 30–50°C/W
  - SOT-223: Rθjc approximately 10–15°C/W
- Estimate power dissipation from the thermal rise: if no current measurement available, use component type typical: power MOSFET: 0.5–2W, LDO regulator: 0.5–1.5W
- Estimated Tj = Tc + (Rθjc × P) = ________ + (________ × ________) = ________ °C

**Step 6:** Compare the estimated junction temperature to the component's maximum rated junction temperature (typically 150°C for automotive grade). Is there adequate thermal margin?

Thermal margin = Tj_max − Tj_estimated = ________ °C
Assessment: **Adequate (>30°C margin) / Marginal (10–30°C) / Insufficient (<10°C)**

### Checkpoint for instructor at ~1:08 (during rotation):
- Is the student finding temperature differences across the board, or reading a uniform temperature? (If uniform, the ECU has not been powered long enough — or the camera is not calibrated)
- Are reference designators being recorded (not just locations)?
- Is the thermal risk assessment column being used with reasoning, or just filled in without thought?

**Common problem — thermal camera showing uniform colour across the board:** ECU has not reached steady state. Allow 3 more minutes. Alternatively, the ECU current draw is very low (key-on without any load activation). Ask the student to command an output channel on via scan tool if available, or accept the result with a note.

**Common problem — student reads very high temperature on a resistor that appears to be a load resistor:** Some ECUs have current sense resistors in series with output channels. These are deliberately designed to dissipate power and will show as hot. This is correct operation — discuss with the student.

---

## Activity 4: Thermal Paste / Pad Inspection (1:15–1:25, 10 minutes)

**Learning focus:** so-3-6-3 — Inspect thermal paste/pad application and assess adequacy

### Overview
Students inspect the thermal interface material between the power stage components and the ECU housing (heatsink). On many automotive ECUs, the power stage MOSFET or driver IC package sits directly on the internal aluminium housing or a heatsink plate, with thermal paste or pad providing the thermal interface. This section of the ECU is typically accessible when the housing is partially disassembled (which the training ECU should be).

### Student Procedure:

**Power down the ECU for this activity. Wait 60 seconds before touching the power stage area.**

**Step 1:** Identify the thermal interface area on the ECU. This is typically:
- Between the power stage MOSFET package (D2PAK or TO-252 package with heat-spreader pad) and the aluminium ECU housing
- Between a separate power stage PCB and the housing
- Between individual components and a thermal spreader plate

**Step 2:** Visually assess the thermal paste or pad:

| Assessment Criterion | Observation | Good / Acceptable / Poor |
|---|---|---|
| Coverage — does the paste/pad cover the full mating surface? | | |
| Thickness — is the paste layer thin and even (not thick and lumpy)? | | |
| Colour and texture — is the paste still soft/pliable, or is it dried/cracked/discoloured? | | |
| Air voids — are there any visible bubbles, gaps, or areas where paste has not contacted both surfaces? | | |
| Squeeze-out — is there excess paste squeezed out beyond the component boundary? | | |

**Step 3:** If thermal paste (not a pad) is present, use the dental pick to gently probe the paste consistency at the edge of the component:
- **Fresh and effective paste:** Still soft, tacky, pliable — fills micro-gaps
- **Aged and degraded paste:** Hard, cracked, powdery, or separated from one surface — air gaps present

**Step 4:** Assess the overall thermal interface quality:

Circle the assessment that best describes the thermal interface on your ECU:

**Good** — full coverage, thin and even, paste still pliable, no visible voids
**Acceptable** — mostly good, minor thin areas, paste still functional
**Degraded** — paste has dried, cracked, or separated; air voids visible; thermal performance is reduced
**Failed** — paste completely absent or solid with large air voids; thermal resistance is significantly higher than designed

**Step 5:** Based on your assessment, recommend the action:
- Good: No action required
- Acceptable: Monitor; re-paste at next opportunity or if thermal fault occurs
- Degraded: Re-paste before returning to service
- Failed: Must be re-pasted before returning to service; thermal failure risk is present

**Step 6:** If the thermal interface is Degraded or Failed on your ECU, calculate the impact on junction temperature:

A degraded thermal interface can increase Rθcs from 0.5°C/W (fresh paste) to 5°C/W (dry, air voids). For a component dissipating 1.5W:
- With fresh paste: ΔT across interface = 0.5 × 1.5 = 0.75°C additional rise
- With degraded paste: ΔT across interface = 5.0 × 1.5 = 7.5°C additional rise

In hot ambient conditions (85°C), this 6.75°C additional rise could be the difference between passing and failing the junction temperature limit.

Record your calculation:
ΔT with fresh paste = ________ × ________ = ________ °C
ΔT with degraded paste = ________ × ________ = ________ °C
Additional junction temperature from degraded interface = ________ °C

---

## Debrief (1:25–1:30)

**Waveform analysis (Activity 1):**
Project Capture B and Capture C on screen. Ask two students to explain their diagnosis of each. Confirm or correct. Emphasis: "Capture B — the missing flyback diode — is the most common cause of repeated driver failure in the workshop. If you repair an ECU with a dead output driver and do not check the flyback diode condition, you are 90% likely to see the same ECU back on your bench within months."

**Driver testing (Activity 2):**
Ask: "How many stations found the failed channel on the first attempt?" Discuss any cases where the failed channel was initially misidentified. Reinforce: "The measurement is clear — near-zero ohms in both diode test directions means the drain-source is shorted. That cannot be misread."

**Thermal camera (Activity 3):**
Ask: "What was the hottest component temperature you recorded? On which component?" Compare across the class. Discuss any components with temperatures above 100°C — these warrant further investigation using the Tj calculation.

**Thermal paste (Activity 4):**
Ask: "How many ECUs had degraded or failed thermal interfaces?" This is often the majority of training ECUs, because they are older units. Emphasise the practical point: "Every time you re-house an ECU after repair, you should re-paste the thermal interface. It costs 30 seconds and it is the difference between a repair that lasts and one that fails in six months."

**Module 3 closing statement:**
> "You have completed Module 3. Three days ago you could look at an ECU PCB and see components. Now you can look at it and see a system: the layers, the processor region, the protection stages, the filtering architecture, the output drivers, and the thermal design. Every component has a job, every job has a failure mode, and every failure mode has a test.
>
> In Module 4, we pick up a soldering iron. The knowledge from this module tells you what you are replacing and why. The skills in Module 4 teach you how to replace it correctly."

---

## Common Mistakes and Instructor Responses

| Mistake | Instructor Response |
|---|---|
| Activity 1: Diagnosing Capture A (healthy) as having a fault because the freewheeling spike looks abnormal to them | "The freewheeling plateau sits at supply voltage + 0.7V — that is correct. It is not a spike; it is a controlled clamping event. The decay is the current running out through the freewheeling path. This is exactly what you want to see." |
| Activity 2: Measuring a healthy body diode forward voltage (0.6V) and classifying it as a fault | "0.6V in one direction and OL in the other direction is the signature of a healthy MOSFET body diode. A shorted MOSFET reads near-zero in *both* directions. The asymmetry is what tells you the junction is healthy." |
| Activity 3: Thermal camera reading appears uniform / no hotspots visible | "Has the ECU been powered for at least 5 minutes? If not, wait. If yes, adjust the camera's temperature range — set the minimum to match the ambient temperature and the maximum to 150°C. This widens the colour range and makes small temperature differences visible." |
| Activity 4: Student classifies dried paste as 'Acceptable' to avoid reporting a fault | "Handle the paste with the dental pick — if it crumbles or does not flex, it is Degraded or Failed. The visual assessment alone is not sufficient. The paste must still be pliable to be classified as Acceptable or Good." |

---

## Assessment Criteria — Module 3 Capstone Observation

Activity 1 (waveform analysis) and Activity 2 (driver testing) are the primary formative assessment for this session. Collect activity worksheets at the end. Grade against the following:

| Criterion | Marks | Notes |
|---|---|---|
| Activity 1: All four captures diagnosed correctly | 16 | 4 marks per capture: 2 for correct diagnosis, 2 for correct evidence/reasoning |
| Activity 2: Failed channel correctly identified | 8 | 4 marks for correct identification; 4 marks for correct repair recommendation |
| Activity 3: Thermal scan completed with correct temperature readings and risk assessment | 6 | 2 marks per rank-ordered hotspot entry |
| Activity 4: Thermal interface assessment completed with correct assessment category and calculation | 6 | 3 marks for correct assessment category; 3 marks for calculation |
| ESD and live circuit safety observed throughout | 4 | Instructor observation |
| **Total** | **40** | |

---

## Module 3 Completion Summary

All six session frameworks for Module 3 (Days 4–6) are now complete. The following SOs have been addressed:

| SO ID | Session Delivered | Assessment |
|---|---|---|
| so-3-1-1 | 04T | Module 3 written assessment |
| so-3-1-2 | 04T + 04H | 04H worksheet |
| so-3-1-3 | 04T | Module 3 written assessment |
| so-3-1-4 | 04T | Module 3 written assessment |
| so-3-2-1 | 05T | Module 3 written assessment |
| so-3-2-2 | 05H | 05H activity worksheet |
| so-3-2-3 | 05H | 05H activity worksheet |
| so-3-3-1 | 05T | Module 3 written assessment |
| so-3-3-2 | 05T | Module 3 written assessment |
| so-3-3-3 | 05T + 05H | 05H activity worksheet |
| so-3-3-4 | 05T | Module 3 written assessment |
| so-3-3-5 | 05T | Module 3 written assessment |
| so-3-4-1 | 05T + 05H | 05H activity worksheet |
| so-3-4-2 | 05T | Module 3 written assessment |
| so-3-4-3 | 05T | Module 3 written assessment |
| so-3-5-1 | 06T | Module 3 written assessment |
| so-3-5-2 | 06T | Module 3 written assessment |
| so-3-5-3 | 06T + 06H | 06H worksheet Activity 1 |
| so-3-5-4 | 06H | 06H worksheet Activity 2 |
| so-3-6-1 | 06T | Module 3 written assessment |
| so-3-6-2 | 06H | 06H worksheet Activity 3 |
| so-3-6-3 | 06H | 06H worksheet Activity 4 |
