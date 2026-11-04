# SESSION-02T: Multimeter Mastery for ECU Work
## Theory Session — Day 2, Block 1

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 2 — Tools & Measurement Mastery
**Session Type:** Theory
**Duration:** 90 minutes
**Delivery Format:** Instructor-led with slides, whiteboard, and live demonstration multimeter

---

## Session Outcomes

By the end of this session, students will be able to:

- **so-2-1-1:** Select the correct multimeter setting for component-level resistance measurement on an ECU PCB
- **so-2-2-1:** Configure oscilloscope timebase, trigger, and channel coupling for ECU signals *(introduced here; deepened in SESSION-03T)*

---

## Materials & Preparation

### Instructor Needs
- Slide deck (guidance per slide below)
- Demonstrator multimeter (Fluke 87V or equivalent true-RMS unit) connected to document camera or bench camera feed
- Cheap auto-ranging meter (for comparison — e.g., a $15 unit)
- 1x PCB with visible through-hole components (damaged donor ECU or training board)
- 1x oscilloscope connected to bench camera feed
- Whiteboard or digital equivalent for live calculations
- Printed or projected multimeter comparison table (spec sheet excerpt)

### Room Setup
- All students should be able to see the camera feed clearly before the session starts
- Check projector/display resolution — multimeter LCD digits must be readable from the back row
- Have the oscilloscope powered and displaying a stable test signal by the time students enter

---

## Session Story Arc

This session has a single narrative thread: **"The ECU is not a car — it is a circuit board. Your multimeter habits from car diagnostics will give you wrong answers here."**

Open by creating discomfort (the voltage drop that was invisible). Build through three increasingly precise measurement concepts. Close with a worked example that ties all concepts together into a diagnostic decision.

---

## Timing Overview

| Block | Content | Time |
|-------|---------|------|
| Hook & framing | The invisible fault | 8 min |
| Slides 1–3 | Multimeter types and why it matters | 15 min |
| Slides 4–6 | ECU-relevant settings in depth | 20 min |
| Slides 7–9 | Probing technique and discipline | 12 min |
| Slides 10–12 | Voltage drop testing (with worked example) | 18 min |
| Slides 13–14 | 5V reference stability and in-circuit resistance | 10 min |
| Student practice problems | Seated calculation and decision tasks | 5 min |
| Wrap-up and preview | Bridge to hands-on session | 2 min |
| **Total** | | **90 min** |

**Flexibility note:** If students are experienced and the multimeter type discussion runs fast, compress Slides 1–3 to 10 minutes and use the saved time to extend the voltage drop worked example with a second scenario.

---

## Slide-by-Slide Instructor Guide

---

### HOOK — "The Invisible Fault" (8 minutes, no slide required)

**Setup:** Before showing any slides, hold up the demonstrator ECU PCB.

> "Before I put up a single slide, I want to tell you about a fault that took one of our senior technicians four hours to find. This ECU came in with an intermittent P0106 — MAP sensor range/performance. The customer had already replaced the MAP sensor twice. The wiring harness had been swapped. Sensor supply voltage at the connector measured 5.1 volts. Ground measured fine to chassis. Everything looked good."

Pause. Let that sit.

> "The fault was a 0.14-volt drop across a single 30mm PCB trace that ran from the ECU's internal 5V reference regulator to the MAP sensor supply pin. 0.14 volts. That trace had a hairline crack in the copper — not visible to the naked eye, not visible under normal light. The crack existed. The trace still conducted. But under load, with the sensor drawing current, that 0.14V drop pushed the sensor supply below the MAP sensor's minimum specification voltage."

Write on the whiteboard:

```
5.00V supply  →  0.14V drop  →  4.86V at sensor pin
```

> "The sensor was reading correctly for 4.86V. But the ECU expected a minimum of 4.95V to trust the signal. So it flagged P0106. Four hours, two sensor replacements, one harness swap — and the real answer was a voltage drop test across 30 millimetres of copper trace."

> "That is why we are spending today on the multimeter. Not because you don't know how to use one — I'm sure most of you do. But ECU repair requires a different level of precision. Let's talk about what that looks like."

---

### SLIDES 1–3: Multimeter Types — Choosing the Right Tool (15 minutes)

---

**Slide 1: The Two Choices That Actually Matter**

*PPT design:* Two-column layout. Left: photo of a Fluke 87V or similar professional unit. Right: photo of a generic auto-ranging unit. Underneath each: a short spec table with 4 rows.

*Key specs to show in the table:*

| Spec | Professional True-RMS | Cheap Auto-Ranging |
|------|-----------------------|--------------------|
| DC Voltage resolution | 0.1 mV (mV range) | 1 mV (best case) |
| True-RMS AC | Yes | No (average-responding) |
| Diode test voltage | Full forward voltage displayed | May cap or show OL incorrectly |
| Continuity threshold | Configurable / ~25 Ω | Fixed, varies by brand |

> "Auto-ranging means the meter picks the range for you. That sounds convenient — and for general diagnostics, it is. But watch what happens when I try to measure a resistance of 0.8 ohms on this cheap meter..."

**Live demo:** Place the cheap meter probes across a short piece of low-gauge wire or a through-hole resistor rated at 0.8Ω. Show the reading — it will likely show 0.0 or 1 ohm with no decimal resolution.

> "Now watch the same measurement on the Fluke..."

Show 0.8Ω or similar with decimal resolution.

> "When you're checking a PCB trace resistance or a solder joint on an ECU, the difference between 0.3 ohms and 1.1 ohms matters. You need that decimal."

---

**Slide 2: True-RMS vs Average-Responding — Why You Care**

*PPT design:* One large graphic. Split waveform diagram — left half shows a clean sine wave, right half shows a PWM square wave at 30% duty cycle. Below each waveform, show what a true-RMS meter reads vs what an average-responding meter reads.

*Numbers to show:*
- Clean sine wave at 12V peak: True-RMS reads 8.49V. Average-responding reads 8.49V. (Same — sine waves are what average-responding is calibrated for.)
- PWM square wave at 12V amplitude, 30% duty cycle: True-RMS reads 6.57V. Average-responding reads 6.37V. Error = 3%.

> "For a 12-volt battery, 3% error is acceptable. For a 5-volt reference that must be within ±0.05 volts to keep your sensor in spec, a 3% error turns a passing measurement into a failing one — or masks a real problem."

> "ECUs generate PWM signals constantly. Fuel injectors, idle air control, cooling fan drivers, EGR valves — all PWM. If you ever measure an ECU output voltage with an average-responding meter, your number is wrong. Not approximately wrong — specifically wrong in a direction that makes faults look better than they are."

> "Rule: for ECU work, true-RMS only."

**Student question to pose (not rhetorical — ask for a volunteer answer):** "What is the RMS voltage of a 5-volt square wave at 50% duty cycle?"

*Expected answer:* 5V × √0.5 = 3.54V. If no one gets it, work it on the board:

```
RMS of a square wave = Amplitude × √(duty cycle)
5V × √0.5 = 5 × 0.707 = 3.54V
```

> "If your average-responding meter reads that as 2.5V — the simple arithmetic mean — you have a 1-volt error on a 5-volt signal. That is enormous in ECU diagnostic terms."

---

**Slide 3: The Resolution Ladder — Picking the Right Meter for the Job**

*PPT design:* Vertical ladder or staircase graphic. Bottom step = battery voltage check. Middle steps = sensor supply verification, coil resistance. Top step = PCB trace resistance, voltage drop across joints.

| Task | Required Resolution | Meter Grade Needed |
|------|--------------------|--------------------|
| Battery voltage, fuse check | 0.1 V | Any meter |
| Sensor supply (5V ref) | 0.01 V (10 mV) | Mid-grade or better |
| Actuator coil resistance | 0.1 Ω | Mid-grade or better |
| PCB trace resistance | 0.01 Ω | Professional + lead null |
| Voltage drop across PCB trace | 1 mV | Professional true-RMS |

> "Every tool choice is a resolution choice. If you grab the wrong meter for the wrong job, you will not get an error message. You will get a number — and that number will look plausible. That is more dangerous than getting no reading at all."

**Transition:** "Now let's go inside the multimeter settings that you'll actually use every day on an ECU repair bench."

---

### SLIDES 4–6: ECU-Relevant Settings In Depth (20 minutes)

---

**Slide 4: DC Voltage — The Setting You'll Use Most**

*PPT design:* Large photograph of multimeter face with DC voltage range highlighted. Callout boxes pointing to relevant LCD segments.

> "DC voltage is your primary tool for ECU work. Nearly everything on a PCB is DC. The 5V reference rail. The processor supply. Logic-level signals. Pull-up resistors. You will be in DC voltage mode for the majority of your time on the bench."

**Range selection:**

> "Set your meter to the 20V DC range, or let it auto-range and verify it settled on 20V or lower. Do not measure a 5V signal on the 200V range — at 200V range, resolution is typically 100mV. You will read '5.0' with no decimal. That tells you nothing about whether the supply is 4.97V or 5.12V."

**Null / zero offset:**

> "Before measuring anything below 100mV, short your probes together and check the displayed value. A good bench meter will show 0.0mV or within 1–2mV. If it shows 8mV with probes shorted, your reading will be 8mV high. Either null it if your meter supports that, or note the offset and subtract it."

**Input impedance:**

> "10 megohms is standard. That means when you probe a 5V circuit, your meter draws 0.5 microamps. In most ECU circuits that is negligible. But if you're measuring across a very high-impedance node — like a comparator input with a 10-megohm pull-up — your meter load matters. Know your circuit before you probe."

---

**Slide 5: Resistance, Diode Test, and Continuity — The Details That Trip People Up**

*PPT design:* Three-panel layout. Each panel shows the meter function symbol (Ω, diode symbol, speaker/tone symbol), the relevant LCD icon, and a "use this for" bullet list.

**Resistance (Ω):**

> "Resistance mode on a good meter goes down to milliohm resolution on the lowest range. This is what you need for PCB work. But before you measure anything with resistance mode, you must do two things: power must be OFF — not just ignition off, battery disconnected — and you must null your lead resistance."

**Live demo:** Clip probes together in Ω mode. Show lead resistance (typically 0.2–0.5Ω on cheap leads, less on quality leads).

> "These probes have 0.3 ohms of resistance themselves. If you measure a component that should read 0.8 ohms and forget to null your leads, you'll read 1.1 ohms. You might condemn a good component. Press REL or ZERO on the meter with probes shorted — now the display reads 0.00 ohms. Every resistance reading you take in this session is lead-nulled. Every time."

**Diode test:**

> "Diode test mode sends a small test current — typically 0.5 to 1 milliamp — through whatever you're probing, and displays the forward voltage drop in volts. For a silicon diode, expect 0.55 to 0.70V forward, and OL in reverse. For a Schottky diode — common as protection devices on ECU inputs — expect 0.20 to 0.40V forward. For a TVS device in its clamping direction, you'll see its forward voltage, not its breakdown voltage."

> "If diode test forward reads OL in both directions: open diode — failed or trace break. If it reads near 0V in both directions: shorted diode — this will pull down your rail. Either way, it's a fault."

**Continuity:**

> "Continuity mode is diode test mode with a beeper added and a threshold, typically around 25–50 ohms depending on the brand. Below threshold: beep. Above threshold: silence. This is useful for quickly checking trace integrity — but notice the threshold. A connection with 30 ohms of resistance might not beep, depending on your meter. Use resistance mode to confirm anything you're unsure about after a continuity test."

---

**Slide 6: The Settings You Must NOT Use for ECU Work**

*PPT design:* Red-background slide (deliberate — this is a "stop" moment). List format with clear X markers.

1. **AC voltage mode on DC ECU signals** — "AC mode removes the DC component. You will see only the AC ripple. A healthy 5V rail with 20mV of noise will read 0.02V in AC mode. You'll think the rail is dead."

2. **Resistance mode on a live circuit** — "Your meter injects its own test voltage. You will get a false reading, and on some ECU circuits you may damage a component. Power OFF before you switch to Ω mode."

3. **High-current (A) mode with fine probes on PCB test points** — "Current mode is a near-short circuit in your meter. If you accidentally have the meter in 10A mode and probe a 5V rail, you will blow the rail, the fuse in your meter, and possibly the component you were trying to test."

4. **AC coupling on oscilloscope for a DC ECU signal** *(preview)* — "We'll cover this in the oscilloscope section, but mark it now: DC coupling only for ECU work."

> "These mistakes are common. They are not stupid mistakes — they are normal mistakes that happen when you're under time pressure. The fix is a mental habit: every time you pick up a probe, say the setting aloud before you touch the circuit."

---

### SLIDES 7–9: Probing Technique and Discipline (12 minutes)

---

**Slide 7: Test Point Identification Before You Probe**

*PPT design:* Annotated photograph of an ECU PCB. Callout arrows pointing to: a through-hole component lead, a via (small plated hole), a component pad, a dedicated test point ring (circular pad with TP marking).

> "ECU PCBs do not have the same test point markings as a bench power supply. You need to identify where to probe before you put metal on copper. A wrong probe placement can short two adjacent pads, inject current into a protected input, or simply give you a reading from the wrong node entirely."

**Four valid probe locations:**

1. **Component lead (through-hole):** "The lead of a resistor or capacitor sticking out of the PCB. Accessible, usually tinned. Safe if you're gentle and use fine-tip probes."
2. **Via:** "A small plated through-hole connecting top and bottom copper layers. Probe into it carefully — it's a valid signal access point but small."
3. **Dedicated TP pad:** "If the PCB has TP labels (TP1, TP2, TP3), use them. They're designed for probing and are mechanically robust."
4. **Connector pin:** "At the ECU connector, back-probe the connector with a fine probe. Do not pierce the wire insulation unless you have a proper back-probe pin."

> "One location you do NOT probe: directly across two adjacent SMD component pads unless you are certain of the net names. A 0402 resistor and a 0402 capacitor next to each other may share a pad connection you haven't traced — or they may be on two completely different nets. Trace the schematic first."

---

**Slide 8: Ground Reference Discipline**

*PPT design:* Circuit diagram (simple, hand-drawn style). Shows ECU with: PCB signal ground, chassis ground, battery negative. Shows how ground loops form when clip goes to chassis rather than PCB ground.

> "Your multimeter negative probe — the black one — must go to the correct ground reference. On a car, chassis ground and ECU signal ground are nominally the same because they're connected. But on a repair bench with a bare PCB, you may have only signal ground available — and if you're measuring a 5mV voltage drop, a millivolt of noise in your ground path corrupts the reading."

**Rule to state explicitly:**

> "For bench measurements on a bare ECU PCB: black probe goes to the ECU ground pin at the connector, or to the main ground pad on the PCB — wherever the manufacturer specifies signal ground. Not to the bench supply chassis. Not to earth through the scope ground clip. To the ECU's own ground reference. Every measurement in this session follows that rule."

**Ground loop explanation:**

> "A ground loop is what happens when you have two different ground paths at different potentials. Your black probe is going to one ground. Your scope probe ground clip is going to another. The difference between those two ground potentials shows up as noise in your reading. At 1V resolution it's invisible. At 1mV resolution it looks like a fault."

---

**Slide 9: Probe Pressure, Contact Quality, and Thermal Drift**

*PPT design:* Three-panel photo sequence: (1) probe barely touching a pad, (2) probe pressing firmly and perpendicular, (3) probe angled and scraping — bridging to adjacent pad.

> "Probe pressure affects your reading. Too light — intermittent contact, bouncing reading. Too heavy with an angled probe — you slide off the pad and potentially bridge to the adjacent pad. The correct technique is: place the probe tip perpendicular to the pad surface, press until you feel resistance, and hold still. Do not slide. Do not rock."

> "On SMD components below 0402 size, I recommend fine-tip probes — 1mm diameter or less. Standard probes on tiny SMD components are a short circuit waiting to happen."

**Thermal EMF — mention briefly:**

> "One more thing: the Seebeck effect. When two different metals are in contact — your copper probe tip on a tinned PCB pad — and there is a temperature difference, you get a small thermoelectric voltage. We're talking microvolts to millivolts. For most ECU measurements this is irrelevant. For milliohm-level resistance measurements, it matters. The technique: take the reading, then reverse your probes and take it again. The real resistance is the average of the two readings. The thermal EMF cancels out."

---

### SLIDES 10–12: Voltage Drop Testing (18 minutes)

---

**Slide 10: What Voltage Drop Testing Actually Is**

*PPT design:* Circuit diagram showing a power source, a resistive fault labelled "suspect joint," and a load labelled "sensor." Three probe positions shown: (A) source to load ground (normal diagnostic), (B) across the suspect joint (voltage drop test), (C) load voltage to load ground.

> "Voltage drop testing is the most powerful diagnostic technique you have for PCB-level faults, and it is consistently underused because it feels counterintuitive. Let me explain it once, clearly."

> "Normal diagnostic: you put your black probe on ground and your red probe on a wire. You read the voltage at that point. If it's 5V, you conclude the supply is good. But this tells you nothing about the resistance of the path between the source and your probe. A high-resistance joint upstream of your probe looks exactly like a good connection, as long as only a small current is flowing."

Draw on the whiteboard:

```
[5V Regulator] ---[Suspect Trace 0.14Ω]--- [Sensor Supply Pin]
                                                      |
                                              Load current = 20mA

Voltage drop = 0.14Ω × 0.020A = 2.8mV
```

> "2.8 millivolts of drop for a typical MAP sensor. That's nothing — the sensor barely notices. But let's say that trace crack gets worse under heat, and the resistance climbs to 7 ohms."

```
Voltage drop = 7Ω × 0.020A = 140mV = 0.14V
Sensor sees:  5.00V − 0.14V = 4.86V
```

> "Now the sensor is out of spec. And the drop is only visible if you put your probes ACROSS that joint — red on one side, black on the other — while current is flowing. That means the ECU is powered up, the sensor is connected, and you are measuring the potential difference across a 30mm section of PCB copper."

---

**Slide 11: Voltage Drop Testing — Step-by-Step Protocol**

*PPT design:* Numbered list with a small probe-position diagram at each step.

1. **Identify the suspect section.** "You need to know — or suspect — which trace, joint, or connector pin is the problem. Red probe goes on the upstream (source) side. Black probe goes on the downstream (load) side."

2. **Leave the circuit powered and loaded.** "Voltage drop only appears when current flows. If you power down, the drop disappears. The circuit must be in its normal operating condition while you measure."

3. **Set the meter to DC mV range.** "You're looking for 0–200mV at most. Use your finest DC voltage range."

4. **Read the value and interpret:**
   - 0 to 0.05V: joint is good — no significant resistance
   - 0.05V to 0.10V: marginal — investigate further and monitor
   - Greater than 0.10V: definitive fault — this joint or trace has excess resistance

5. **Confirm by walking your probes.** "Walk your probe positions along the trace. When you find the segment where the drop concentrates, you've found the fault location."

> "Notice what this technique does not require: a schematic. You are following voltage, not tracing a diagram. Voltage naturally concentrates across resistance. You follow the voltage."

---

**Slide 12: Worked Example — Full Diagnostic Scenario**

*PPT design:* Schematic of a simple ECU 5V reference circuit. Trace from 5V regulator output through two connector pins to sensor supply. Values labelled: source = 5.00V, measured at sensor pin = 4.84V, load current = 35mA.

> "Let's work through a complete example. The ECU 5V reference regulator output measures 5.00V at its output pad. The MAP sensor supply pin at the ECU connector measures 4.84V. That's a 160mV drop across the internal trace path. Load current is 35 milliamps — we know this from the sensor datasheet."

**Work on whiteboard in real time:**

```
Drop observed:  5.00V − 4.84V = 0.16V  (160mV)
Load current:   35mA = 0.035A

Fault resistance:  R = V ÷ I = 0.16V ÷ 0.035A = 4.57Ω

Expected resistance of a 30mm, 0.5mm wide, 35μm copper trace:
  ρ (copper)  = 1.72 × 10⁻⁸ Ω·m
  Length      = 0.030m
  Cross-section = 0.0005m × 0.000035m = 1.75 × 10⁻⁸ m²
  R = ρL/A = (1.72×10⁻⁸ × 0.030) ÷ 1.75×10⁻⁸ ≈ 0.030Ω  (30 milliohms)

Healthy trace ≈ 0.03Ω
Measured fault ≈ 4.57Ω
Ratio: 4.57 ÷ 0.03 = ~152× expected resistance  →  definitive fault
```

> "The math confirms what the voltage told us: there is catastrophic resistance in that trace. We now know exactly where to look and exactly what we're looking for."

**Student exercise (2 minutes, individual):**

> "Work this one out yourselves."

- 5V reference regulator output: 5.02V
- Sensor supply pin: 4.91V
- Sensor quiescent current: 8mA

*Question: What is the equivalent fault resistance? Is this a definitive fault or marginal?*

*Answer: Drop = 5.02 − 4.91 = 0.11V. R = 0.11 ÷ 0.008 = 13.75Ω. Definitive fault — a healthy trace at that geometry would be under 0.1Ω.*

---

### SLIDES 13–14: 5V Reference Stability and In-Circuit Resistance (10 minutes)

---

**Slide 13: The 5V Reference — Why Stability Matters**

*PPT design:* Graph: X-axis = supply voltage (4.7–5.3V), Y-axis = sensor output voltage. Two traces: normal supply curve vs shifted curve at 4.80V. Red band showing ECU acceptance window (4.95–5.05V). Yellow band showing marginal region (4.85–4.95V).

> "Your MAP sensor, TPS, and most other analog sensors work on ratiometric measurement. The sensor output voltage is a proportion of the supply voltage — not an absolute voltage. If the supply drops, the output drops proportionally, even if the actual measured parameter hasn't changed."

> "This is why the 5V reference rail must be stable within ±0.05V — that is 1% tolerance. Many OEM sensor specifications require the supply to be between 4.95V and 5.05V. Below 4.95V, sensor readings are outside calibrated range. The ECU may still accept the signal — or it may not, depending on its diagnostic threshold."

> "Your job on the bench: verify the 5V reference under load. Connect the sensor, power the circuit, and measure the reference at the regulator output — then again at the sensor connector pin. Both readings must be within 4.95–5.05V. If they differ by more than 50mV, perform a voltage drop test between those two points."

---

**Slide 14: In-Circuit Resistance Measurement — The Critical Rules**

*PPT design:* Red and green split layout. Red side labelled WRONG: probes on a live PCB, lightning bolt symbol. Green side labelled CORRECT: battery disconnected, capacitors discharged notation, probes on PCB, "leads nulled" label.

**Rule 1 — Power OFF:**

> "The circuit must be completely de-energised. Not ignition off — battery disconnected. On a bench, bench supply off. If you measure resistance with power on, your meter is injecting its own voltage into a live circuit. You'll get a wrong reading, and you may damage a component."

**Rule 2 — Capacitors discharged:**

> "ECUs have large filter capacitors. After battery disconnect, wait 30 seconds, then measure DC voltage across the main supply caps — should be below 1V before you start resistance measurements. Residual charge will corrupt your reading."

**Rule 3 — Parallel paths:**

> "On a PCB, there are almost always parallel paths between any two points. If you measure a component in-circuit, parallel resistors will show up as a lower reading than the true value. For example: a 10kΩ pull-up resistor with a 10kΩ pull-down in parallel — your meter reads 5kΩ. Both components are good, but in-circuit you see 5kΩ. Know your schematic before you interpret resistance readings."

**Rule 4 — Lead null:**

> "We covered this. Do it every time, without exception."

---

## Student Practice Problems (5 minutes)

Project these problems. Students work individually, then briefly compare with a neighbour.

**Problem 1:** You're measuring a 22Ω current-limiting resistor in-circuit. The meter reads 18.7Ω. Should you flag this as a fault?

*Expected discussion:* Possibly not — there may be a parallel path. Need to check the schematic for parallel resistors before condemning the component.

**Problem 2:** You measure a TVS diode with the meter in diode test mode. Forward reading: 0.28V. Reverse reading: OL. Is this TVS diode healthy?

*Expected answer:* Yes — 0.28V forward voltage is consistent with a Schottky-type TVS in clamping direction. OL in reverse means the reverse breakdown voltage exceeds the meter's diode test voltage (typically 3V). This is normal behaviour.

**Problem 3:** You need to check if a PCB trace has degraded. The trace carries 50mA. Your meter reads 22mV voltage drop across the trace segment. Is this a fault?

*Answer:* R = 0.022V ÷ 0.050A = 0.44Ω. For a PCB trace, 0.44Ω is excessive. A healthy 30–50mm trace should be under 0.1Ω. This is a marginal-to-definitive fault — worth investigating further.

---

## Wrap-Up and Preview (2 minutes)

> "Let me summarise what we've covered today. True-RMS meter, correct settings, lead-nulled resistance, voltage drop testing across suspect joints — these are your new baseline habits for ECU board-level work."

> "This afternoon, you will use all of this on a live bench. We'll be testing actual protection diodes, performing voltage drop tests on traces I've pre-damaged on training boards, and verifying 5V reference stability. I want you to arrive knowing which meter setting you'll start with for each task — that's your warm-up question as you walk in."

> "Before that, does anyone have questions on anything from this morning?"

*Allow 2–3 minutes for questions. Write any particularly good questions on the board and answer publicly.*

---

## Common Student Challenges

| Challenge | What You'll See | How to Handle |
|-----------|----------------|---------------|
| Forgetting to null leads before resistance measurements | Consistently reads 0.3–0.5Ω high on all Ω measurements | Walk the student through the null procedure. Have them re-measure a known resistor before and after to see the difference. |
| Confusing voltage drop test setup with normal voltage measurement | Places both probes to the suspect node and ground, not across the suspect section | Draw the circuit on paper. Ask "which two points define the voltage drop across the suspect joint?" Re-frame it as measuring the voltage across a resistor, not a voltage at a point. |
| Trusting continuity beep for trace integrity | Assumes a beep means the trace is good, missing a 40Ω high-resistance joint | Ask "what is the continuity threshold on your meter?" Then demonstrate a 40Ω fault that still beeps. Switch to resistance mode — show 40Ω. |
| Using AC voltage mode out of habit from vehicle diagnostics | Reads near-zero on DC signals, assumes circuit is dead | Ask "what mode is your meter in?" Create the habit of stating the mode aloud before probing. |
| Parallel path confusion on in-circuit resistance | Condemns a correct component based on an artificially low reading | Ask "what else is connected to those two nodes?" If they don't know, they must consult the schematic. Reinforce: in-circuit resistance is interpretation, not measurement. |

---

## PPT Design Summary

- **Slides 1–3:** Data-heavy comparison tables; photographs of real meters; clean two-column layouts.
- **Slides 4–6:** Function symbol callouts on meter photograph; three-panel layout for individual functions; red-background "stop" slide for hazardous settings.
- **Slides 7–9:** Annotated PCB photographs; circuit diagram for ground path; probe technique photo sequence.
- **Slides 10–12:** Circuit diagrams with probe positions marked A/B/C; numerical worked example with whiteboard integration; student exercise embedded in slide.
- **Slides 13–14:** Graph with tolerances clearly banded in colour; red/green split layout for the rules slide.
- **Consistent visual language:** Use the same ECU board silhouette throughout. Highlight active probe positions in orange. Fault locations in red. Good reference points in green.

---

*End of SESSION-02T Framework*
