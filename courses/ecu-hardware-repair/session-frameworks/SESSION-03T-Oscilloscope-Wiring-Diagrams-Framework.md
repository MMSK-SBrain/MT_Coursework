# SESSION-03T: Oscilloscope Waveform Analysis & Wiring Diagrams
## Theory Session — Day 3, Block 1

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 2 — Tools & Measurement Mastery
**Session Type:** Theory
**Duration:** 90 minutes
**Delivery Format:** Instructor-led with slides, live oscilloscope demonstration, and printed wiring diagram exercise sheet

---

## Session Outcomes

By the end of this session, students will be able to:

- **so-2-2-3:** Capture and compare a healthy vs degraded ECU sensor signal waveform
- **so-2-2-4:** Capture an injector drive signal and identify peak-and-hold phases and the freewheeling spike
- **so-2-3-1:** Identify connector reference numbers, pin assignments, and signal names on a wiring diagram

---

## Materials & Preparation

### Instructor Needs
- Slide deck (guidance per slide below)
- Oscilloscope with two channels, connected to document camera feed — live for the entire session
- Signal source 1: function generator set to produce a clean 5V, 100Hz sine wave (simulating a healthy VR sensor)
- Signal source 2: same function generator with clipping/distortion introduced, or a second generator producing a degraded sine (flat-topped or noisy)
- Signal source 3: pre-recorded injector waveform capture played back via a waveform generator, or a real injector driver circuit — capturing peak-and-hold pattern (peak ~65V spike, hold ~2A plateau, freewheeling spike)
- Printed wiring diagram exercise sheet — one per student (see Appendix A)
- Whiteboard for annotating circuit paths live
- Highlighter pens in 3 colours (one set per two students — distribute during wiring diagram section)

### Pre-Session Oscilloscope Setup
Arrive 15 minutes early. Verify:
- Channel 1 is connected to the healthy sine wave generator, DC coupling, 2V/div, 5ms/div, triggering cleanly
- Channel 2 is connected to the degraded sine wave generator, same settings, ready to add at the comparison slide
- Injector waveform source is connected and ready (you will switch sources mid-session)
- Screen is visible to all students from their seats

---

## Session Story Arc

This session runs two parallel narrative threads that converge at the end.

**Thread 1 — The oscilloscope as a time-domain microscope.** Yesterday we used the multimeter to see DC quantities. Today we use the oscilloscope to see how signals behave across time. A 5V reading on a multimeter tells you the average. The scope tells you the truth.

**Thread 2 — The wiring diagram as a map.** Before you can test any signal, you need to know what the signal should look like and where to find it. A wiring diagram is not optional reading — it is the tool you use before you pick up any other tool.

The threads merge in the final section: you use the wiring diagram to find the test points, and the oscilloscope to judge the signal at those points.

---

## Timing Overview

| Block | Content | Time |
|-------|---------|------|
| Hook | The waveform that looked fine on a meter | 7 min |
| Slides 1–4 | Oscilloscope configuration deep dive | 20 min |
| Slides 5–7 | Sensor waveform capture and comparison | 18 min |
| Slides 8–10 | Injector drive waveform anatomy | 18 min |
| Slides 11–14 | Wiring diagram reading — principles and practice | 20 min |
| Wrap-up | Summary and preview of hands-on session | 7 min |
| **Total** | | **90 min** |

**Flexibility note:** If the oscilloscope setup discussion is already familiar to students (good feedback from Day 2 hands-on), compress Slides 1–4 to 12 minutes and use the saved 8 minutes to extend the wiring diagram exercise with a second tracing task.

---

## Slide-by-Slide Instructor Guide

---

### HOOK — "The Waveform That Looked Fine on a Meter" (7 minutes)

**Setup:** Begin with the oscilloscope displaying the clean sine wave on channel 1. Do not reveal channel 2 yet.

> "Raise your hand if this sounds familiar: you've checked a sensor supply — 5 volts, good. Checked sensor ground — zero volts, good. Checked sensor output — 2.4 volts at idle, within range. All three measurements passed. But the car still has an intermittent misfire and a crank sensor code."

Wait for recognition.

> "What if I told you the crank sensor output looks like this..."

*Switch channel 1 display to the degraded sine wave. Describe what students see — flat-topped peaks, signal not reaching expected amplitude, possibly noisy baseline.*

> "Your multimeter read 2.4 volts because 2.4 volts is the average of this signal. The meter was telling you the truth about the average. But the ECU does not decode this signal by averaging it. The ECU looks for zero crossings — the point where the sine wave passes through zero volts on its way up and down. That is how it determines crank position."

Point to the waveform.

> "When the peaks are clipped and the baseline is noisy, those zero crossings are ambiguous. The ECU cannot reliably determine the exact crank position, so it either loses sync or assigns a position it's not confident in. Intermittent misfire. Intermittent code. All while your multimeter reads 2.4 volts — correct."

> "That is what the oscilloscope is for. It shows you the shape of the signal across time. The shape is the diagnostic information. Today we learn to read it."

---

### SLIDES 1–4: Oscilloscope Configuration Deep Dive (20 minutes)

---

**Slide 1: DC Coupling — The Non-Negotiable Setting**

*PPT design:* Two side-by-side oscilloscope screen captures of the same ECU sensor signal. Left: AC coupling — signal is centred at 0V, DC offset removed. Right: DC coupling — signal sits correctly at 2.5V DC midpoint. Label each clearly.

> "We touched on coupling in yesterday's theory. Today I want to be more explicit about why this matters for ECU signals."

> "AC coupling removes the DC component of a signal. The oscilloscope puts a capacitor in the signal path that blocks DC and passes only the AC variation. This is useful in audio electronics and RF work. It is actively harmful for ECU diagnostics."

> "Why? Because the DC level of an ECU signal carries diagnostic information. A MAP sensor output that should sit at 1.5V at atmospheric pressure and rides on a 0V baseline — if you AC-couple that, the DC level disappears. You see only the transitions. You cannot tell if the signal is at 1.5V or 4.5V — you see the same waveform shape either way."

> "DC coupling only. Every ECU signal, every time. I want this written in your notes and in your head."

**Write on whiteboard:** DC COUPLING — ECU SIGNALS ALWAYS

> "The only exception: if you are measuring a small AC ripple on a large DC supply — say you want to see 50mV of noise on a 12V rail — AC coupling removes the 12V so you can scale in on the 50mV. But you would then explicitly note that you've removed the DC reference. Not a standard ECU diagnostic procedure."

---

**Slide 2: Timebase Selection — Matching the Window to the Signal**

*PPT design:* Four oscilloscope screen captures, each showing the same CAN bus signal but at different timebases: 50ms/div (signal looks like a smear), 5ms/div (a few bits visible), 1ms/div (individual bit cells start to appear), 100μs/div (bit timing clearly visible).

> "The timebase controls how much time is represented by each horizontal division. If your timebase is too slow, you see a long smear — lots of time compressed into the screen. If your timebase is too fast, you see a tiny slice of the waveform — maybe not even one complete cycle."

**Timebase reference table to show and explain:**

| Signal Type | Typical Period or Event Duration | Recommended Starting Timebase |
|-------------|----------------------------------|-------------------------------|
| MAP / TPS sensor (static DC) | No periodic signal | 50ms/div — look for noise and step changes |
| PWM output (idle, fan, EGR) | 5–50ms period | 5ms/div |
| CAN bus data | 10–100μs bit time | 100μs/div |
| Fuel injector pulse | 2–15ms open duration | 2ms/div |
| CKP sensor (VR, idle ~800rpm) | ~75ms per tooth period | 10ms/div |
| CKP sensor (VR, 6000rpm) | ~10ms per tooth period | 1ms/div |

> "The rule of thumb: you want to see 3–5 complete cycles of a periodic signal on screen. If you can see 10 or more cycles, go faster. If you cannot see one complete cycle, go slower. Adjust by factors of 2 or 5 — those are the standard timebase steps."

> "For a one-time event — like a single injector fire — use Single Trigger mode. We'll talk about that in a moment."

---

**Slide 3: Trigger — Stabilising the Waveform**

*PPT design:* Animated sequence (or static photo sequence) showing: (1) unstable waveform drifting across screen, (2) trigger level set below signal — still unstable, (3) trigger level at mid-signal rising edge — waveform locks cleanly.

> "The trigger is what makes the oscilloscope display a stable waveform instead of a continuous scrolling stream. The scope waits until the signal meets your trigger condition — then it starts drawing the waveform from that moment. Every subsequent capture starts from the same point in the signal. That's why the waveform looks stationary."

**Three trigger settings to cover:**

**Edge trigger:**

> "Edge trigger fires when the signal crosses a set voltage level in a set direction — rising or falling. This is your default for almost all ECU work. Rising edge means the scope triggers on the signal crossing your level from below. Set the trigger level to approximately half the signal amplitude — this puts the trigger point in the middle of the waveform transition, where the signal is moving fastest and the trigger will be most consistent."

**Single-shot trigger:**

> "Single trigger mode captures one waveform and freezes it. After the trigger fires, the scope stops acquiring. This is essential for capturing one-time events: a sensor glitch, a single injector fire, a relay click. In Normal or Auto trigger mode, those events would scroll off screen before you could see them. Single trigger mode: set it up, initiate the event, review the frozen capture."

**Trigger holdoff:**

> "If your signal has a complex repeated structure — like a CKP signal with a missing tooth — the scope may trigger on different teeth each time and the waveform will appear to jitter. Trigger holdoff prevents re-arming the trigger for a set time after each capture. Adjust holdoff until you see the missing tooth in a consistent position on screen every capture. This tells you the holdoff time is close to one full engine cycle."

---

**Slide 4: Voltage Scale, Probe Factor, and Ground Reference**

*PPT design:* Checklist-style slide. Each item is a setting with a "for ECU work" recommendation and a "why" note.

| Setting | ECU Work Recommendation | Why |
|---------|------------------------|-----|
| Volts/div | 2V/div for 0–5V signals; 5V/div for 12V signals; 10V/div for injector peaks | Fills ~60–80% of the screen vertically — maximum resolution |
| Probe factor | x10 always for ECU signals | x1 probe has lower input impedance and higher capacitance — loads the circuit and distorts high-frequency edges |
| Probe compensation | Check before first measurement of the day | A mis-compensated probe gives rounded or over-shot square wave edges — calibrate with built-in square wave reference |
| Ground clip | ECU signal ground, not chassis | Ground loops corrupt measurement at mV level |
| Channel offset | Position ground reference at bottom 20% of screen for positive signals | Leaves screen real estate for the signal, not the ground line |

**Live demo — probe compensation check:**

> "Let me show you the probe compensation procedure before we go further. Every scope has a built-in 1kHz square wave reference output. Connect your probe tip to that output and the ground to its ground point..."

*Perform on live scope under document camera.*

> "A correctly compensated probe shows a flat top and sharp edges on that square wave. If the top is curved up at the corners — that's over-compensated. Curved down — under-compensated. Adjust the small screw on the probe until it's flat. This takes 10 seconds and is the first thing you do every time you pick up a new probe."

---

### SLIDES 5–7: Sensor Waveform Capture and Comparison (18 minutes)

---

**Slide 5: What a Healthy ECU Sensor Signal Looks Like**

*PPT design:* Two oscilloscope screenshots side by side — left is a healthy VR (variable reluctance) crank sensor signal (clean sinusoid with consistent amplitude and clear zero crossings), right is a healthy Hall effect sensor signal (clean square wave, 0–5V, sharp edges, consistent duty cycle). Label key features: amplitude, period, zero crossing, duty cycle.

> "There are two fundamentally different sensor types that produce electrical waveforms on an ECU: variable reluctance sensors and Hall effect sensors. They are not interchangeable in how you interpret them."

**Variable Reluctance (VR):**

> "VR sensors produce a sine wave. The amplitude of the sine wave increases with the speed of the rotating trigger wheel — at idle it may be 2–4V peak-to-peak, at high RPM it might be 20–40V. The ECU does not care about amplitude. It reads only the zero crossing — the precise moment the wave passes through 0V on its way from negative to positive. That timing is the crank position signal."

> "Diagnostic implication: if the sine wave is clean — smooth curves, consistent amplitude tooth-to-tooth, sharp zero crossings — the sensor is working. If peaks are clipped, if zero crossings are obscured by noise, if amplitude collapses on certain teeth — those are faults. And they are invisible on a multimeter."

**Hall Effect:**

> "Hall effect sensors produce a square wave — 0V low, supply voltage high (typically 5V or 12V depending on sensor type). The ECU reads the rising or falling edges. Diagnostic implication: edges should be sharp (less than 1μs rise time on a healthy signal). If edges are soft or rounded, check for excessive cable capacitance or a failing sensor driver stage."

---

**Slide 6: Recognising a Degraded Sensor Waveform**

*PPT design:* Four oscilloscope screenshots, each labelled with the fault type: (1) Noise on baseline, (2) Clipped peaks, (3) Missing tooth (amplitude dropout on one tooth period), (4) DC offset shift (entire waveform raised above 0V baseline). Each screenshot has a callout circle on the defect.

**Switch the live oscilloscope to channel 2 — the degraded signal. Students can now see both channels.**

> "Here is the comparison. Channel 1 is our reference — healthy. Channel 2 is what came off a worn sensor with a damaged air gap on the trigger wheel."

Walk through each fault type verbally:

**Noise on baseline:**
> "High-frequency noise sitting on the signal baseline. Usually caused by poor sensor grounding, a shorted shielding braid, or a PWM driver running nearby inducing interference. The zero crossings are now uncertain — the noise may create false crossings before the real one."

**Clipped peaks:**
> "The peaks are flat-topped. This usually means the sensor air gap is too large — the signal is at maximum amplitude and the sense circuit is saturating. Or it can indicate a failing sensor coil with internal short. The ECU still sees zero crossings, but the waveform is wrong — some ECUs will detect this condition."

**Missing tooth — amplitude dropout:**
> "One complete tooth period has almost no signal. Usually a chip or crack in the reluctor ring. This is actually sometimes deliberate — manufacturers use a missing tooth as the reference position. Know your specific engine. If the missing tooth is not in the expected position, or if multiple teeth are missing, that is a fault."

**DC offset shift:**
> "The entire waveform has shifted above 0V — it no longer crosses zero, it crosses at positive voltage. Usually caused by a shorted diode in the sensor interface circuit on the ECU PCB. The ECU may not decode the position at all because it never sees the zero crossing it expects."

> "Write these four patterns. They will appear in the hands-on session and in real vehicles."

---

**Slide 7: Capturing a One-Time or Intermittent Event**

*PPT design:* Step-by-step numbered graphic with scope screenshots at each step. Final screenshot shows a frozen single waveform capture.

> "Intermittent faults are the hardest. The fault happens once, then the signal returns to normal. With a scope in normal run mode, by the time you see the screen the fault is gone. This is where single trigger mode is essential."

**Procedure to teach verbally:**

1. Set scope to Single trigger mode (usually a button labelled SINGLE or RUN/STOP → SINGLE).
2. Set trigger level to just above the noise floor — below the normal signal amplitude. This ensures the scope will trigger on even a reduced-amplitude fault event.
3. Arm the trigger — scope shows READY or similar waiting state.
4. Reproduce the fault condition (wiggle harness, apply thermal stress, drive the vehicle).
5. When the fault occurs, the scope fires, captures the waveform, and freezes.
6. Examine the frozen capture. Save to USB or photograph.
7. If the fault did not occur, press Single again to re-arm and try again.

> "Single trigger mode is patient. You can leave a scope armed for 10 minutes waiting for an intermittent fault to occur. The scope will wait. When it triggers, it has your fault, frozen in time."

> "One caution: make sure your timebase is set correctly before arming. If your timebase is 50ms/div and the fault event is 500μs long, the event will appear as a tiny glitch you might not notice. Set the timebase to the expected duration of the fault — tighten it up so you can see the shape clearly."

---

### SLIDES 8–10: Injector Drive Waveform Anatomy (18 minutes)

---

**Slide 8: The Injector Driver — What Is Actually Happening**

*PPT design:* Circuit diagram of a peak-and-hold injector driver. Shows: ECU internal driver transistor, injector coil (12–16Ω), flyback/freewheeling diode across the coil, 12V battery supply. Arrows showing current flow during peak phase, hold phase, and freewheeling phase.

> "A fuel injector is a solenoid — a coil of wire that creates a magnetic field when current flows, lifting a needle valve to allow fuel to spray. Electrically, it's an inductor in series with a resistor."

> "The ECU needs to open the injector as quickly as possible — fast opening time directly affects injection accuracy. But you don't need maximum current the entire time the injector is open — you just need enough to hold the needle off its seat against the fuel pressure and return spring."

> "This is the principle behind peak-and-hold drive. Two phases:"

**Peak phase:**
> "At the moment the ECU commands the injector open, it applies full driver voltage to achieve maximum current rise rate. The coil resistance is typically 2–5Ω for a peak-and-hold injector, so peak current can reach 4–8 amps. This peak current is maintained for a very short time — perhaps 1–2 milliseconds — just long enough to physically open the valve fully."

**Hold phase:**
> "Once the valve is open, the driver reduces current — typically to 1–2 amps — using PWM chopping. This is enough to hold the needle open but uses far less power. The hold phase continues for the remainder of the injector open time."

**Freewheeling spike:**
> "When the driver switches OFF — valve closes — the inductor tries to maintain current flow. It generates a large reverse voltage spike. This spike can reach 60–80 volts, sometimes higher. The freewheeling diode (or zener clamp) across the coil limits this spike and returns the energy to the supply rail. Without this diode, the spike would destroy the driver transistor."

---

**Slide 9: Reading the Injector Waveform on Screen**

*PPT design:* Single large oscilloscope screenshot of a complete injector drive waveform. Labels pointing to: (A) injector open command — voltage drops to near 0V, (B) peak current phase — visible as initial high-current period, (C) hold phase — PWM chopping visible as ripple, (D) freewheeling spike — voltage spike above supply, (E) injector close — voltage returns to supply level.

*Switch the live oscilloscope to the injector waveform source. Students observe.*

> "Let me orient you on this waveform. The horizontal axis is time — this is at 2ms/div. The vertical axis is voltage — we're at 10V/div to capture the spike, which will reach above the screen if we're at 5V/div."

Walk through each labelled point:

> "Point A: the ECU commands the injector open. The driver transistor turns on, connecting the injector coil to ground. The voltage at the injector control terminal — where we've placed our probe — drops from 12V to near 0V. This is the beginning of the injection event."

> "The first section of the low state is the peak phase. Current is rising rapidly. We can't directly see current on a voltage probe, but we can infer it from the duration and the small voltage drop across the driver transistor."

> "Point C: notice the chopping. The voltage alternates between 0V and a partial positive value. The driver is turning on and off rapidly — this is the PWM hold current control. Each 0V period is driver-on, each positive period is driver-off with freewheeling. The current stays roughly constant at hold level."

> "Point D: the injector command ends. The driver turns off. The inductor's energy has nowhere to go — it generates the spike. The spike can be 60–80 volts on a 12V system. The freewheeling diode clamps it."

> "Point E: normal 12V supply level resumes. The injector is closed."

**Diagnostic implication to state explicitly:**

> "If the freewheeling spike is absent — flat at 12V after command-off — the freewheeling diode is shorted, clamping the spike prematurely. Or the diode may be open and the spike reaches higher than expected (check against spec — if your spec says max 80V and you see 150V, the clamp has failed). Either way, a missing or abnormal spike is a fault condition in the driver circuit."

---

**Slide 10: Peak-and-Hold vs Saturated Drive — Knowing Which You're Looking At**

*PPT design:* Two oscilloscope screenshots side by side. Left: peak-and-hold waveform with clear two-phase structure and PWM chopping visible in hold phase. Right: saturated drive waveform — single low state, no chopping, higher coil resistance, sharp freewheeling spike at end.

> "Not all injectors use peak-and-hold. High-impedance injectors — typically 12–16 ohms coil resistance — use saturated drive. The ECU simply connects the injector to ground for the entire injection duration. There is no peak phase, no hold PWM. The higher resistance limits current naturally to a safe level."

**How to tell which you have on the waveform:**
- Peak-and-hold: low-resistance injector (2–5Ω), PWM chopping visible during hold phase, peak current phase visible at beginning
- Saturated: high-resistance injector (12–16Ω), clean simple square wave, no chopping, sharp single freewheeling spike at end

> "Before you probe an injector waveform, find out which drive type the vehicle uses. It's in the service data — listed under fuel system or fuel injector specifications. If the waveform doesn't match the expected type, that itself is a fault."

> "Also: on some modern ECUs, peak-and-hold drive is implemented inside the ECU PCB with a dedicated MOSFET driver IC. If that IC fails partially, you may see a degraded peak phase — reduced peak current, longer valve opening time, fuel delivery error. The waveform shape tells you this. The multimeter tells you nothing."

---

### SLIDES 11–14: Wiring Diagram Reading (20 minutes)

---

**Slide 11: Why Technicians Skip Wiring Diagrams (and Why They Shouldn't)**

*PPT design:* Clean slide with a single quote large, centered. Then a photograph of a wiring diagram with a "where do I start?" expression annotation.

Quote to display: *"A wiring diagram is not what you consult when everything else fails. It is what you consult before you touch anything."*

> "There is a pattern I see repeatedly in ECU repair: a technician checks voltages at the ECU connector, gets confusing results, checks voltages at the sensor connector, still confused — then spends 40 minutes probing the wiring harness at random before finally pulling out the wiring diagram and finding the answer in 90 seconds. The diagram was there the whole time."

> "The reason people avoid wiring diagrams is that they look intimidating. There are symbols you don't recognise, numbering systems that seem arbitrary, and connector designations that don't match anything you can physically see. Today we fix that by learning to read a real wiring diagram systematically."

> "We will use the exercise sheet you've just been given. This is a real extracted section of an OEM wiring diagram — simplified for training but based on the actual format you'll encounter."

*Distribute the wiring diagram exercise sheets now if not already done.*

---

**Slide 12: The Anatomy of a Wiring Diagram — Connector References**

*PPT design:* Annotated wiring diagram excerpt (from the exercise sheet, projected large). Labels pointing to: connector box, connector identifier, pin number, wire colour code, signal name, component box.

> "Let's identify every element systematically. Follow along on your sheet."

**Connector identifier:**
> "Every connector in a wiring diagram has a reference identifier. In DIN/ISO format — which is used across most European and Asian OEMs — connectors are typically labelled with a letter-number combination. For example: 'X31' or 'A15' or in some formats, 'ECU-A'. The letter or first part identifies the connector housing. The number identifies the specific pin within that housing."

> "On your exercise sheet, locate the connector labelled X17. This is the ECU main connector in this diagram. Find it — it should appear as a rectangular block with numbered pin positions inside."

*Give 30 seconds for students to locate it.*

> "Notice that X17 has pins numbered 1 through 48. Each number corresponds to a physical pin in the connector. The diagram shows which circuit connects to each pin. This is your translation between the physical connector you can touch and the circuit you want to diagnose."

---

**Slide 13: Signal Names, Wire Colours, and Reading the Path**

*PPT design:* Zoomed section of the exercise sheet diagram showing a complete signal path from sensor to ECU. Labels on: wire colour designator, signal name abbreviation, earth/ground symbol, splice point, shield braid line.

> "Follow one signal path from start to end. On your sheet, find the MAP sensor. It's shown as a component box labelled 'MAP' with three connections: supply, signal, and ground."

> "The supply wire runs from the MAP sensor supply pin to a splice, then back to pin 23 of connector X17. The wire colour designation — in this diagram it's shown as GN/WH, meaning green with a white tracer — is printed along the wire. In the vehicle, you would look for the green/white wire at the connector."

> "The signal wire runs from the MAP signal pin directly back to ECU pin 22, X17. Wire colour: BL/YE — blue with yellow tracer."

> "The ground wire runs from MAP ground pin to a splice, joins the sensor ground bus, runs to ECU pin 47, X17."

**Practical exercise on the sheet — 5 minutes:**

> "On your exercise sheet: using a highlighter, trace the complete signal path for the CKP sensor — from the CKP sensor terminals, through the harness, to the ECU pins. Use one colour for signal-positive, another for signal-negative, another for shield/ground. When you're done, write the ECU connector and pin numbers for all three connections at the bottom of the sheet."

*Allow 4–5 minutes for this exercise. Walk the room and check progress.*

*Expected answers (based on exercise sheet design — instructor to confirm against actual sheet used):*
- CKP+ signal: connector X17, pin 8
- CKP- signal: connector X17, pin 9
- Shield: chassis ground splice G104

---

**Slide 14: From DTC to Wiring Diagram to Test Point — The Diagnostic Chain**

*PPT design:* Flow diagram with five steps in sequence, each step with a brief description. Arrow connecting each step to the next.

```
DTC logged
    ↓
Identify affected sensor/circuit from DTC description
    ↓
Locate sensor in wiring diagram → find connector ID and pin numbers
    ↓
Identify all test points along the signal path (supply pin, signal pin, ground pin)
    ↓
Probe those specific points with multimeter or oscilloscope
```

> "This is the diagnostic chain. Every step depends on the one before it. The DTC tells you which circuit. The wiring diagram tells you where in that circuit to look. The wiring diagram tells you which ECU pin, which harness connector, which splice. Without that information, you are probing at random."

> "Let's run through an example together. DTC P0335 — Crankshaft Position Sensor A Circuit. What does that tell us?"

Elicit from students: the CKP sensor, or the circuit between it and the ECU.

> "Good. Now we go to the wiring diagram. We find the CKP sensor — you just traced it. ECU connector X17, pins 8 and 9, shield at G104. We now know exactly where to probe. We will probe the ECU pins themselves using back-probe pins. We will look for the expected sine wave waveform on channel 1 for CKP+, channel 2 for CKP-, or differential between them if the scope has math capability."

> "We do not need to remove panels, disconnect anything, or guess. The diagram tells us. Then the scope confirms."

**Final connection — bridge to hands-on:**

> "This afternoon, you will use a wiring diagram to trace a complete signal path. You will verify supply and ground pins physically. Then you will test sensors and actuators at those specific test points, using both multimeter and oscilloscope. Everything in this morning's session feeds into that."

---

## Wrap-Up and Preview (7 minutes)

Summarise the three themes from the session:

> "Three things from this morning I want you to carry into the afternoon."

> "First: DC coupling, always. The DC level of an ECU signal carries diagnostic information. Removing it with AC coupling removes that information."

> "Second: the oscilloscope shows shape across time. Shape is the diagnostic data. An average voltage reading is an average of the shape — it hides faults within the shape."

> "Third: the wiring diagram is your first tool, not your last resort. Before you probe anything this afternoon, you will find the circuit in the diagram and identify the specific ECU pins and harness connectors for every signal you're testing."

> "Any questions before we break?"

*Allow 3–5 minutes for questions.*

*Preview of the afternoon:* "You'll be testing a TPS, a MAP sensor, a CKP sensor, and an injector coil. You'll use a wiring diagram to find the test points before you probe anything. I'll have the training ECU boards energised and ready when you arrive."

---

## Common Student Challenges

| Challenge | What You'll See | How to Handle |
|-----------|----------------|---------------|
| Cannot lock trigger on complex waveform | Waveform drifts or jitters on screen | Ask: "What is your trigger source and level?" Check coupling on trigger channel. For VR sensor signal, trigger level must be at 0V (zero crossing) not at mid-amplitude. |
| Misreads peak-and-hold vs saturated drive | Calls a saturated injector "faulty" because it has no hold PWM | Ask them to look up the injector type in the vehicle specification before making any fault conclusion. Reinforce: match waveform to spec, not to expectation. |
| Cannot find the sensor in the wiring diagram | Searches by physical location rather than component label | Show them the diagram index (most wiring diagrams have a component index page). Look up the component name — the index gives the diagram page and zone. |
| Confuses connector designator with pin number | Probes the wrong pin (e.g., probes pin X17 on connector 17, or vice versa) | Walk them through reading "connector X17, pin 8" as a two-part address: X17 = which connector housing, 8 = which pin inside that housing. |
| Misses the freewheeling spike on injector waveform | Sets volts/div too fine (2V/div) and spike goes off-screen | Ask: "Can you see the end of the injection event?" If the spike is clipped or not visible, they need to zoom out vertically. |
| Confuses VR sensor amplitude variation with a fault | Student reports "amplitude is lower at low RPM — sensor is failing" | Explain VR amplitude is speed-dependent — always has been, always will be. Lower amplitude at low RPM is correct. Fault would be amplitude lower than expected for that RPM, or zero crossings corrupted. |

---

## Appendix A — Wiring Diagram Exercise Sheet Design Brief

*(Instructor to produce or commission this sheet before the session. Specifications below.)*

**Content:** A simplified but realistic wiring diagram excerpt showing:
- ECU unit block labelled "ECU" with connector X17 (32–48 pins shown)
- MAP sensor with supply, signal, and ground connections
- TPS sensor with supply, signal, and ground connections
- CKP sensor (VR type) with CKP+, CKP−, and shield
- Injector 1 (high-side supply from relay, low-side drive from ECU)
- Sensor ground splice and chassis ground point labelled G104
- Wire colour codes on each wire (use abbreviated format: e.g., RD/WH for red/white)
- Splice nodes shown as filled circles at junction points

**Pin assignments to design in (instructor defines these for their specific exercise sheet):**
- MAP supply: X17 pin 23
- MAP signal: X17 pin 22
- MAP ground (shared sensor GND): X17 pin 47
- TPS supply: X17 pin 23 (shared splice with MAP)
- TPS signal: X17 pin 21
- TPS ground: X17 pin 47 (shared)
- CKP+: X17 pin 8
- CKP−: X17 pin 9
- Injector 1 low-side drive: X17 pin 35
- Injector power: relay output (label relay K4)

**Format:** A4 or US Letter, printed in greyscale (diagram should be readable without colour). Include a blank answer table at the bottom for students to write pin assignments during the exercise.

---

*End of SESSION-03T Framework*
