# SESSION-11T: ECU Line Tracking & Component Testing Theory
## Instructor-Led Story Framework for PPT Preparation

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 5 — ECU On-Table Diagnostics
**Day:** 11 | **Session Type:** Theory
**Duration:** 90 minutes
**Approach:** Instructor-Led Narrative with Worked Diagnostic Scenarios
**PPT Target:** 28–32 slides

**Session Outcomes Addressed:**
- so-5-3-1: Use wiring diagram to identify complete signal path for a DTC, from sensor output through harness to ECU processing stage | Analyze
- so-5-3-2: Probe a live ECU signal line using oscilloscope, compare to expected waveform, identify where signal degrades | Analyze
- so-5-3-3: Use split-half fault isolation to narrow a line-tracking fault to a specific PCB stage or component | Analyze

**CO Alignment:** co-1

---

## INSTRUCTOR-LED STORY ARC

---

### SETUP: Opening Hook (Slides 1–4, ~10 minutes)

**Narrative Voice:** Precise and methodical. Students now have a confirmed current DTC and a target circuit from Day 10. Today they learn what to do next: follow the circuit physically and systematically until the fault is found. The tone is confident — this is a skill that eliminates guessing.

#### Slide 1: Title Slide
**Visual:** Split image. Left: scan tool showing P0105 MAP sensor circuit low. Right: oscilloscope screen showing signal present then dropping to 0V partway across the screen — an annotated "fault point" arrow at the drop. A connecting arrow: "From DTC — to exact fault location."
**Instructor Script:**
> "Yesterday you got a DTC. Today you learn what to do with it. The scan tool told you which circuit to investigate. Your job now is to follow that circuit — from the sensor, through the wiring harness, into the ECU connector, across the PCB traces, through the input conditioning components, and into the microcontroller input — using measurement at each point to find exactly where the signal fails. This is line tracking. When you do it correctly, it eliminates guessing entirely. You don't replace parts. You find the fault."

#### Slide 2: The Cost of Not Tracking — A Real Scenario
**Visual:** Timeline with four entries and price tags:
- Day 1: P0105. Technician replaces MAP sensor — 45 pounds. Code returns.
- Day 3: Workshop replaces MAP sensor wiring harness section — 120 pounds. Code returns.
- Day 6: Workshop fits reconditioned ECU — 280 pounds. Code returns.
- Day 8: Line tracking performed. Fault found: open-circuit series resistor on ECU PCB — component cost under 1 pound. Repair time 20 minutes.

Caption: "Total wasted expenditure: 445 pounds. Total correct repair: under 1 pound and 20 minutes."

**Instructor Script:**
> "This is not a hypothetical. This scenario happens in automotive repair workshops every week. The DTC said MAP sensor circuit. The technician interpreted 'sensor' and replaced the sensor. It came back. The next technician replaced the harness. It came back. A third ECU was fitted. Still back.
>
> The fault? A 1 kilohm resistor on the PCB input conditioning circuit had gone open circuit. No current could flow through the signal path. The ECU saw no signal — P0105. Three expensive interventions missed what a 30-minute systematic line trace would have found.
>
> Line tracking is the protection against wasted money — yours and the customer's."

#### Slide 3: Line Tracking Defined
**Visual:** Annotated signal path diagram:
`[Sensor] → [Signal wire] → [Inline connector] → [ECU connector pin] → [PCB trace] → [Series resistor] → [Filter cap] → [MCU ADC input]`
Title: "The Complete Signal Path."
**Instructor Script:**
> "Line tracking is the systematic process of following a signal from its origin — the sensor — to its destination — the microcontroller input — and finding the point on that path where the signal stops being correct. Every ECU signal has a complete path. That path has a beginning, multiple intermediate stages, and an end. A fault is simply the point where the signal changes from correct to incorrect.
>
> Your tools are: a wiring diagram to know the path, a PCB schematic to extend that path from the connector pin into the board, an oscilloscope to measure signal behaviour at each point, and a systematic method to find the fault efficiently."

#### Slide 4: Three Skills for Today
**Visual:** Three numbered steps:
1. Mapping the Signal Path — extracting the complete path from DTC to MCU input
2. Probing the Path — measuring at each point with the oscilloscope, interpreting what you find
3. Split-Half Isolation — finding the fault in the minimum number of measurements
**Instructor Script:**
> "Three skills. They build in sequence. You cannot probe without a map. You cannot split-half efficiently without knowing what you're looking for. Each relies on the previous one."

---

### TRIGGER: From DTC to Signal Path Map (Slides 5–8, ~12 minutes)

#### Slide 5: Step One — Extract the Circuit from the DTC
**Visual:** Three-step process: DTC code (P0105) → Workshop manual / scan tool diagnostic procedure → Circuit identification (MAP sensor circuit: 5V reference, signal return, signal ground, ECU pin 13).
**Instructor Script:**
> "The DTC gives you a circuit name. The workshop manual or scan tool's built-in diagnostic procedure gives you the details: which specific pins, which wires, what normal voltage range, what threshold causes the DTC to set.
>
> Find it. Read it. Write it down before you pick up a probe. The time spent in documentation pays back in not probing the wrong circuit."

#### Slide 6: Step Two — Trace the Wiring Diagram
**Visual:** Wiring diagram section for MAP sensor circuit, fully labelled:
- Sensor body (MAP sensor, 3-wire)
- Wire 1: 5V reference from ECU (ECU pin 22, wire YE/BR)
- Wire 2: Signal output from sensor to ECU (ECU pin 13, wire GN/WH)
- Wire 3: Signal ground from ECU to sensor (ECU pin 5, wire BK)
- In-line connector C107 in engine harness
- ECU 55-pin connector face
**Instructor Script:**
> "From the workshop manual, you have the pin numbers. From the wiring diagram, you trace those wires from the sensor to the ECU connector. Note every intermediate point: in-line connectors, junction boxes, splices. Each is a potential fault location.
>
> For the MAP sensor: three wires, one intermediate connector. I have four probe-accessible points before I even open the ECU connector: sensor output, sensor side of C107, ECU side of C107, and ECU connector pin."

#### Slide 7: Step Three — Extend the Path Into the PCB
**Visual:** PCB schematic fragment for the MAP sensor input circuit:
ECU connector pin 13 → PCB trace → Series resistor R142 (4.7 kilohms) → Node A → Clamping diode D31 (to ground) → Clamping diode D32 (to 5V) → RC filter capacitor C88 → MCU pin PA12 (ADC input).
Test points labelled: TP1 at connector pin 13, TP2 at R142 input pad, TP3 at R142 output pad / Node A, TP4 at C88 pad, TP5 at MCU pin PA12.
**Instructor Script:**
> "Once the signal enters the ECU at the connector pin, it travels through the PCB input conditioning circuit. This is where 40% of the component-level faults live — not in the sensor, not in the harness, but in these input circuit components.
>
> The typical analog sensor input conditioning circuit has: a series protection resistor (limits current to protect the ADC input), clamping diodes (prevent voltage exceeding the ADC input range), an RC filter (removes high-frequency noise before the ADC samples), and the MCU ADC input pin itself.
>
> Each component can fail. The series resistor can go open circuit. The clamping diode can short to ground. The filter capacitor can fail. Knowing this circuit lets you probe at each component."

#### Slide 8: Drawing Your Signal Path Map
**Visual:** Completed example signal path map:
```
[MAP Sensor output]
    ↓ (Wire GN/WH, ECU pin 13 signal)
[Inline connector C107, pin B]
    ↓
[ECU Connector, pin 13]     <- TP1: First probe point
    ↓
[PCB trace]
    ↓
[Series resistor R142, input pad]    <- TP2
    ↓
[Series resistor R142, output pad]   <- TP3 (Node A)
    ↓
[RC filter cap C88 top pad]         <- TP4
    ↓
[MCU ADC input PA12]                <- TP5
```
Expected signal at each point noted: "1.4V DC (MAP at atmospheric pressure, workshop bench)"

**Instructor Script:**
> "Before you probe, you draw this map. It takes three to five minutes. It tells you where every probe point is, what order to visit them, and what you expect to find at each one.
>
> Working without this map is like navigating a city without a street plan. The map is the plan. Work from the plan.
>
> In the hands-on session this afternoon, you will draw this map before the instructor signs off on your readiness to begin probing. No map — no probing."

---

### RISING ACTION Part 1: Probing the Signal Path (Slides 9–19, ~35 minutes)

#### Slide 9: Section Header — PROBING THE SIGNAL PATH
**Visual:** Clean section divider. Background: oscilloscope screen showing a healthy MAP sensor signal — steady DC at approximately 1.4V with minor ambient noise.
**Instructor Script:**
> "Map drawn, probe points identified, expected signals noted. Now you measure. The primary tool for signal line probing is the oscilloscope — not the multimeter. I'm going to explain why that matters before we look at how to set it up."

#### Slide 10: Oscilloscope Not Multimeter — For Signal Lines
**Visual:** Side-by-side comparison.
Left: Multimeter display showing 2.3V. Caption: "Stable reading — appears fine."
Right: Oscilloscope showing same signal — frequent intermittent dropouts to 0V, each lasting 2–8ms. Caption: "Intermittent dropouts every 400ms — failed connector contact."
**Instructor Script:**
> "A multimeter computes an average. If a signal drops to 0V for 5 milliseconds every 400 milliseconds, the multimeter integrates over its measurement window and shows approximately 2.3V — which looks fine. Meanwhile, the ECU samples the ADC input every millisecond, sees the 0V dropout, and logs an out-of-range condition. The DTC sets. The multimeter told you nothing.
>
> The oscilloscope shows you time. It shows you what the signal is doing at every instant. A 5ms dropout is invisible to a multimeter and completely visible on an oscilloscope with a 500ms timebase.
>
> For static power supply voltages — B+ rail, 5V reference level, ground — use the multimeter. It's faster and accurate enough. For signal lines: oscilloscope, always."

#### Slide 11: Oscilloscope Setup for Sensor Signal Probing
**Visual:** Oscilloscope screen with settings annotated:
- Channel: CH1, DC coupling
- Voltage scale: 1V per division (full display 10V — captures 0–5V sensor range)
- Timebase: 50ms per division (for slow analog signals like MAP, ECT, TPS)
- Trigger: Auto, rising edge, level at mid-scale
- Ground clip: connected to PSU negative (bench chassis ground)
- Probe: x1 for 0–5V signals
**Instructor Script:**
> "DC coupling for all sensor signal work — we want the true DC level. Voltage scale: start at 1V per division with a 10V window. This puts the full 0–5V sensor range in the lower half of the screen.
>
> Timebase: 50ms per division for slow-changing signals. If you're looking at crankshaft signals, you need much faster — 1ms or less.
>
> Ground clip: to PSU negative. Not floating. Not to a chassis point you're unsure about. A floating ground reference produces garbage measurements that look meaningful but are not."

#### Slide 12: Reference Waveforms — What Healthy Looks Like
**Visual:** Four oscilloscope captures:
1. MAP sensor at idle — steady DC approximately 1.4V, small ripple
2. TPS during throttle sweep — clean linear ramp from 0.5V to 4.5V
3. Coolant temperature — very slowly rising DC
4. Crankshaft sensor — regular square pulse train, consistent amplitude
**Instructor Script:**
> "You need to know what correct looks like before you can recognise wrong. These four are healthy signals. Notice the common characteristics: consistent amplitude, no dropouts to zero, no sustained flat-lining at rail voltage, signal matches what the sensor should be measuring.
>
> These are your baseline references. Memorise the patterns."

#### Slide 13: Five Fault Signatures — The Pattern Library
**Visual:** Five oscilloscope captures, each with annotations:
1. Signal stuck at 0V — flat line at 0V. Caption: "Open circuit in signal path or short to ground"
2. Signal stuck at 5V (rail) — flat line at maximum. Caption: "Signal wire shorted to voltage source"
3. Intermittent dropouts to 0V — mostly correct signal with periodic drops. Caption: "Intermittent open circuit — connector corrosion, damaged wire, cold solder joint"
4. High-frequency noise riding on correct signal. Caption: "Failed bypass/filter capacitor"
5. Signal present at connector pin, absent at PCB test point. Caption: "Open circuit on PCB — trace break or open series resistor"
**Instructor Script:**
> "Five fault signatures. Memorise these. Each one tells you something specific.
>
> Stuck at 0V: either the signal wire has broken and the ECU input is floating low, or the signal wire is physically shorted to ground.
>
> Stuck at rail: the signal wire has contacted a voltage source — most commonly the 5V reference line running alongside it.
>
> Intermittent dropouts: this is the classic intermittent connector fault. The contact resistance in a corroded or fretting connector pin goes intermittently very high.
>
> Noise on correct signal: the bypass capacitor in the sensor input RC filter has failed open. It is no longer shunting high-frequency noise to ground.
>
> Signal present at connector, absent at test point: an open circuit exists on the PCB between those two probe points. A trace break, a lifted pad, an open series resistor."

#### Slide 14: The Boundary Measurement — ECU Connector Pin
**Visual:** Diagram showing probe tip at ECU connector pin. Arrow indicating "External circuit (sensor + harness)" on the left, "Internal circuit (PCB)" on the right.
**Instructor Script:**
> "Your first probe point is always the ECU connector pin — the exact pin that carries the signal you are investigating. This measurement is the diagnostic fulcrum. It divides your search space in half.
>
> If the signal is correct at the ECU connector pin — the fault is internal. The sensor works, the harness works. Something inside the ECU is stopping the signal from reaching the MCU.
>
> If the signal is absent or wrong at the ECU connector pin — the fault is external. The ECU input circuit may be perfectly fine.
>
> One measurement. Two halves of the search space."

#### Slide 15: Decision Tree — External vs Internal
**Visual:** Binary decision tree:
```
Probe ECU connector pin for signal line

Signal CORRECT at connector pin?
    YES → Fault is on PCB
          → Probe PCB test points (split-half method)
    NO  → Fault is external
          → Probe sensor output directly
          → Probe harness connector at mid-point
          → Find: last point with correct signal
```
**Instructor Script:**
> "After the connector pin measurement, you know which direction to investigate. If the signal is correct at the pin — everything external is eliminated. You go into the PCB with confidence. If the signal is wrong at the pin — you don't touch the PCB. You trace backward toward the sensor.
>
> In the hands-on session today, the faults are all planted on the PCB side. So after confirming the signal is correct at the connector pin — which you should find it is — you'll turn your attention to the PCB test points."

#### Slide 16: Probing on the PCB — Test Points and Component Leads
**Visual:** PCB photograph with annotations:
- Dedicated test point pads (labelled TP14, TP15, etc.): "Use first — designed for probing"
- SMD resistor lead pad: "Can probe here — steady hand required"
- SMD capacitor pad: "Can probe here — fine probe tip for small components"
- IC pin: "Probe here last — highest risk of slip and accidental short"
**Instructor Script:**
> "When the fault is on the PCB, you probe at test points — dedicated pads or identified component pads. Use test points first if the ECU has them. If no dedicated test points, probe at component leads.
>
> Practical tip: use a piece of insulating tape over adjacent pads when probing a specific IC pin. The tape prevents accidental bridging. Remove it after probing."

#### Slide 17: Expected Signals at Each PCB Stage
**Visual:** Signal path diagram with expected measurements at each stage for a MAP sensor input (1.4V DC from sensor):

| Probe Point | Expected Signal | If Different — Possible Cause |
|---|---|---|
| Connector pin 13 (TP1) | 1.4V DC, low noise | Signal absent: external fault. If OK: continue to PCB |
| Series resistor R142 input (TP2) | 1.4V DC (same as TP1) | Open in PCB trace between connector and resistor |
| Series resistor R142 output (TP3) | 1.4V DC (minimal drop) | Open resistor — 0V at TP3 despite signal at TP2 |
| RC filter capacitor pad (TP4) | 1.4V DC, very low noise | Shorted cap pulls to 0V; open cap increases noise |
| MCU ADC input PA12 (TP5) | 1.4V DC, filtered | Signal here but DTC still set: check ADC or MCU |

**Instructor Script:**
> "In this example, the sensor is producing 1.4V DC. That voltage should travel through the PCB input circuit essentially unchanged — the series resistor has negligible drop when the ADC input draws microamps, and the RC filter affects only noise frequencies.
>
> So you expect 1.4V at every probe point from connector pin to MCU input. If any point shows something different, the fault is between the last point that showed 1.4V and this point showing something else."

#### Slide 18: When the Signal Is Degraded, Not Absent
**Visual:** Three oscilloscope captures:
1. Signal at 0.8V instead of expected 1.4V — reduced amplitude. Caption: "High-resistance joint in series — voltage divider effect"
2. Correct DC level (1.4V) but noise amplitude of 0.4V. Caption: "Failed bypass cap — EMI noise coupling to ADC"
3. Signal intermittently switching between 1.4V and 0V. Caption: "Intermittent connection — connector fretting corrosion"
**Instructor Script:**
> "Not every fault produces a completely absent signal. Some produce a degraded signal that is present but wrong.
>
> A reduced amplitude suggests a resistive fault in the signal path — a partial contact resistance or a high-value component accidentally in parallel has created a voltage divider.
>
> Noise on the signal but correct DC level points directly at the filter capacitor.
>
> Intermittent switching between correct and zero is the classic connector diagnosis: corrosion or fretting wear on a connector pin."

#### Slide 19: In-Circuit Component Testing — The Confirmation Step
**Visual:** Four component test scenarios:
1. Resistor — multimeter resistance mode, both leads. Note: lift one end if in-circuit parallel paths confuse reading.
2. Capacitor (ESR meter) — ESR meter probes across capacitor. Power off. Expected: ESR under 1 ohm for good electrolytics.
3. Diode (multimeter, diode mode) — forward: 0.5–0.7V expected. Reverse: OL expected.
4. MOSFET — gate-source resistance (power off): megaohm range. Drain-source: high resistance; body diode forward in one direction.
**Instructor Script:**
> "Once the oscilloscope has pointed you to a specific component — the fault is between TP2 and TP3, so the component is series resistor R142 — you confirm the fault with the multimeter or ESR meter. Power off the ECU before switching to resistance or diode measurement.
>
> For resistors: measure in-circuit first. If the reading is dramatically different from the marked value — open or very high resistance — the resistor is suspect. Lift one end from its pad and measure again out of circuit to confirm definitively.
>
> For capacitors: the ESR meter is your friend. A failed electrolytic capacitor often shows correct capacitance but very high ESR. An ESR of 5–20 ohms on a bypass capacitor that should be 0.1–0.5 ohms is a failed cap.
>
> For diodes and clamping diodes: diode mode. Forward: 0.5–0.7V. Reverse: OL. Both ways low = shorted. Both ways OL = open.
>
> For MOSFETs: gate-source in resistance mode should be very high (megaohms). Drain-source body diode shows correct forward voltage in one direction. Drain-source resistance near zero in both directions = shorted MOSFET."

---

### RISING ACTION Part 2: Split-Half Fault Isolation (Slides 20–26, ~22 minutes)

#### Slide 20: Section Header — THE SPLIT-HALF METHOD
**Visual:** Signal path with eight numbered test points in a line. The midpoint (test point 4) is highlighted with a bracket over it.
**Instructor Script:**
> "You now have a map with probe points. Before you start probing, I want to give you a method for deciding which probe point to visit first. This method — split-half isolation — is the single biggest time-saver in complex fault diagnosis. It comes from computer science: the same principle as a binary search algorithm."

#### Slide 21: The Split-Half Principle
**Visual:** Sequential demonstration:
Step 0: Known good at TP1. Known bad at TP8. Fault somewhere in path. 7 segments to check.
Step 1: Probe TP4 (midpoint). Signal absent. Fault in first half: TP1–TP4. Eliminated: TP4–TP8.
Step 2: Probe TP2 (midpoint of remaining TP1–TP4). Signal present. Fault in second half of remainder: TP2–TP4.
Step 3: No more midpoints — fault between TP2 and TP3.
Result: Fault isolated in 3 measurements.
**Instructor Script:**
> "The principle is simple. I know the signal is good at TP1. I know it's bad at TP8. The fault is somewhere in those seven segments. Instead of probing sequentially, I probe the midpoint.
>
> First probe: TP4, the midpoint. Signal absent. The fault is in the first half — TP1 to TP4. The second four segments are eliminated. One measurement, half the search space gone.
>
> Second probe: TP2, midpoint of the remaining section. Signal present. Fault is between TP2 and TP4.
>
> Third probe: TP3. Signal absent. Fault between TP2 and TP3. One segment. Done.
>
> Three measurements. Not seven."

#### Slide 22: The Mathematics of Split-Half
**Visual:** Comparison table:

| Signal Path Segments | Sequential Probing (worst case) | Split-Half (always) |
|---|---|---|
| 4 | 4 | 2 |
| 8 | 8 | 3 |
| 16 | 16 | 4 |
| 32 | 32 | 5 |

Formula: Number of measurements = log₂(N) where N = number of segments.

**Instructor Script:**
> "The mathematics: log₂ of N gives the number of measurements needed by split-half, regardless of where the fault is — not worst-case, always.
>
> For our 8-segment example: log₂(8) = 3 measurements. Always exactly 3. Sequential probing can take anywhere from 1 to 8 depending on where the fault is.
>
> For a complex PCB with 32 identifiable test points: split-half takes 5 measurements. Sequential could take 32. This is the difference between a 10-minute trace and a 45-minute one."

#### Slide 23: Worked Example — Split-Half on MAP Sensor PCB Path
**Visual:** ECU PCB schematic for MAP sensor input with 6 test points (TP1–TP6). Initial conditions annotated:
- TP1 (connector pin 13): Signal confirmed present — 1.4V
- TP6 (MCU ADC PA12): Signal confirmed absent — 0V
- Fault somewhere between TP1 and TP6.

Three measurement steps:
Step 1: Probe TP3 (midpoint of 6). Result: Signal absent — 0V. Fault in first half: TP1–TP3.
Step 2: Probe TP2 (midpoint of TP1–TP3). Result: Signal present — 1.4V. Fault in second half of remaining: TP2–TP3.
Step 3: Component between TP2 and TP3 = Series resistor R142. Confirm (power off) with ohmmeter → OL (open). Fault confirmed.

**Instructor Script:**
> "Let's trace this with split-half. Signal present at TP1. Signal absent at TP6.
>
> First probe: TP3, the midpoint. Signal absent. Fault is in the first half — between TP1 and TP3.
>
> Second probe: TP2. Signal present. The fault is between TP2 and TP3.
>
> What's between TP2 and TP3? Series resistor R142. Power off. Switch to resistance mode. Probe across R142 in-circuit. Reading: OL — open circuit. Expected value: 4.7 kilohms. Fault confirmed. Two oscilloscope measurements. One multimeter confirmation. Fault found."

#### Slide 24: When Split-Half Has Limits
**Visual:** Three cases where split-half is constrained:
1. Only two accessible probe points: connector pin and MCU pin. No midpoints — inspect all components in the segment.
2. Intermittent fault: signal changes between measurements. Fault must be triggered (tap, flex, thermal) while probing.
3. No labelled test points: probe at component lead pads — method is identical.
**Instructor Script:**
> "Split-half is powerful but it works on what is physically accessible. If you have only the connector pin and the MCU pin accessible — no midpoints — you can't split. You know the fault is in that segment. You then inspect every component in the segment methodically.
>
> For intermittent faults: tap the connector while watching the scope — does the signal drop? Flex the PCB gently. Use a hot-air gun at low temperature on a suspected component.
>
> On ECUs without dedicated test points: probe at component pads. The method is identical."

#### Slide 25: Documenting Line Tracking — Why Every Measurement Goes on Paper
**Visual:** Completed line tracking worksheet showing probe path map with all probe points, each result recorded, split-half decision log, fault location circled, confirmation measurement, one-sentence conclusion.
**Instructor Script:**
> "Write everything down as you go. Not when you've finished — as you go. Two reasons. First: you will not remember which test points showed what result when you've been concentrating on a complex split-half sequence. Your documentation is your external memory.
>
> Second: this documentation is evidence. It shows the customer what was done, how the fault was found, and what the root cause is. It protects you professionally.
>
> In the hands-on session, every probe point goes on the worksheet. Every result gets recorded. The fault confirmation measurement gets recorded. The final conclusion is one clear sentence."

#### Slide 26: The Complete Line Tracking Decision Flow
**Visual:** Full decision flow diagram:
```
START: DTC identified, circuit named
    Identify circuit in service documentation
    → which pins, signal type, normal range
    ↓
Draw signal path map: sensor → harness → ECU pin → PCB → MCU input
    → Label every accessible probe point
    → Note expected signal at each point
    ↓
Set up oscilloscope: DC coupling, 1V/div, appropriate timebase
    ↓
PROBE 1: ECU connector pin (boundary measurement)
    Signal CORRECT at pin → Fault INTERNAL (PCB)
    Signal WRONG/ABSENT at pin → Fault EXTERNAL (sensor/harness)
    ↓
INTERNAL: Apply split-half to PCB test points
    Probe midpoint of known-good to known-bad range
    Signal at midpoint?
        YES → Fault in second half → halve, repeat
        NO  → Fault in first half → halve, repeat
    ↓
Fault isolated to one segment (two adjacent TPs)
    Identify component from PCB schematic
    ↓
POWER OFF. Confirm with multimeter:
    Resistor: measure value
    Capacitor: ESR measurement
    Diode: diode mode forward/reverse
    MOSFET: gate-source and drain-source resistance
    ↓
Fault confirmed → Document → Plan repair
```
**Instructor Script:**
> "This is the complete workflow — from DTC to confirmed fault component. Print this. Put it on your bench. Follow it every time.
>
> Notice it has no random steps. No 'replace this and see.' Every step produces information that directs the next step. Every measurement eliminates half or more of the remaining possibilities. This is the structure of systematic diagnosis."

---

### CLIMAX: The Professional Standard (Slides 27–28, ~8 minutes)

#### Slide 27: Amateur vs Professional Diagnostic Approach
**Visual:** Two-column contrast table:

| Amateur Approach | Professional Approach |
|---|---|
| Reads DTC description. Replaces the component named. | Reads DTC, identifies circuit, draws signal path map. |
| Guesses based on experience with similar symptoms. | Probes systematically. Measures before concluding. |
| Uses only multimeter — averages hide intermittency. | Uses oscilloscope — sees what the signal actually does. |
| Probes randomly. | Probes from plan. First measurement is the connector pin boundary. |
| Replaces part. If not fixed, replaces another. | One trace. One confirmation. One repair. |
| No documentation. | Full record: path map, every probe result, fault conclusion. |

**Instructor Script:**
> "These two columns represent the difference in outcome between shops that make money on ECU repair and shops that don't. The professional approach is not harder — it's actually faster because it eliminates all the time spent replacing parts that aren't faulty.
>
> The professional approach requires three things: the workflow (which you now have), the tools (oscilloscope, multimeter, ESR meter — all available on the bench), and discipline — the discipline to draw the map first and not pick up the probe until you have a plan."

#### Slide 28: When Line Tracking Reaches Its Limits
**Visual:** Four cases annotated as beyond line tracking scope:
1. MCU internal fault — signal path confirmed good to MCU pin; MCU outputs wrong value. Conclusion: MCU replacement.
2. BGA component fault — component under investigation is a BGA IC with no accessible pins. Requires X-ray or reballing equipment.
3. Encrypted ECU — requires programming tools before diagnosis is meaningful.
4. Long-duration intermittent — requires in-vehicle extended logging rather than bench diagnosis.
**Instructor Script:**
> "Know the limits of the tool. Line tracking finds faults in the signal path: wires, PCB traces, passive components, protection diodes, driver ICs with accessible pins. It does not diagnose inside a microcontroller die.
>
> If you've correctly traced the signal path to an MCU pin, confirmed all external components are correct, and the MCU is still outputting wrong data — the MCU is the fault. The line trace has done its job: it eliminated everything else. Replacement is the next step. That's a valid diagnostic conclusion reached by a valid process."

---

### RESOLUTION: Consolidation (Slides 29–32, ~10 minutes)

#### Slide 29: Summary Card — Signal Path Mapping
**Visual:** Clean reference card:
- Start from DTC → service documentation → identify circuit (pins, wires, signal type)
- Trace wiring diagram: sensor → harness → inline connectors → ECU connector pin
- Extend from ECU connector pin into PCB schematic: trace → series resistor → clamp diodes → filter cap → MCU input
- Draw the map with all probe points labelled and expected signal at each
- Map must be completed and reviewed before probing begins

#### Slide 30: Summary Card — Oscilloscope Probing
**Visual:** Clean reference card:
- DC coupling for all sensor signal work
- 1V/div for 0–5V sensor signals
- Timebase: 50ms/div for slow analog; 1ms or less for fast digital
- Ground clip to PSU GND — confirmed reference
- First probe: ECU connector pin — boundary measurement (external/internal decision)
- Five fault signatures: stuck at 0V, stuck at rail, intermittent dropouts, noise on correct signal, signal present at connector but absent on PCB

#### Slide 31: Summary Card — Split-Half Method
**Visual:** Clean reference card:
- Probe midpoint of unknown range first
- Signal present at midpoint → fault in second half
- Signal absent at midpoint → fault in first half
- Halve and repeat until isolated to one segment
- Maximum measurements needed: log₂(N) where N = number of segments
- When isolated to one segment: identify component from schematic → confirm with multimeter (power off)

#### Slide 32: Preview of Day 11 Hands-On
**Visual:** Photo of oscilloscope probe on PCB test point, signal visible on scope screen.
**Instructor Script:**
> "This afternoon you apply everything from today. Each bench has a live ECU with a fault planted somewhere in a specific signal path — somewhere between the ECU connector pin and the MCU input. You will scan the DTC, look up the circuit, draw your signal path map, get it signed off, configure your oscilloscope, make your boundary measurement at the connector pin, and use split-half to isolate the fault. Then you'll confirm it with the multimeter and write your conclusion.
>
> Two rules for this afternoon: no probing without a signed-off signal path map. Everything you measure goes on the worksheet before you make your next measurement.
>
> Questions before we head to the workshop?"

---

## PPT DESIGN GUIDANCE

### Visual Style:
- Maintain the dark professional theme with amber accents — consistent across Module 5
- Oscilloscope screenshots: real captures where possible. Generated waveforms are unconvincing to students who have used real oscilloscopes.
- Signal path diagrams: left-to-right flow. External circuit in blue. ECU connector in grey. PCB internal in amber. MCU in a distinct colour.
- Split-half diagrams: use bold brackets or coloured highlight boxes to show which half is under investigation.

### Key Slides to Emphasise:
- Slide 8 (signal path map): print-quality. Students will replicate this format in the lab.
- Slide 13 (five fault signatures): students photograph this every time. Display it on the projector during 11H.
- Slide 14 (boundary measurement): the most important single concept — emphasise explicitly.
- Slide 26 (complete decision flow): the master reference. Print and post at every bench for 11H.

### Animations:
- Slide 21 (split-half principle): animate each step individually. Show TP1 (good), TP8 (bad), then reveal TP4 probe and result, then TP2, then TP3. Do not show the complete sequence before walking through it.
- Slide 23 (worked example): animate each probe step — pause after each and ask "which half do we investigate next?" before revealing.
- Slide 27 (amateur vs professional): reveal rows one pair at a time.
- Slide 13 (fault signatures): reveal each capture individually with explanation.

---

## INSTRUCTOR NOTES

### Pedagogical Strategy:
This session uses progressive complexity with worked examples that directly mirror the lab:
1. Establish the complete signal path concept before introducing measurement technique
2. Build oscilloscope confidence through healthy-signal baselines before fault patterns
3. Introduce split-half as an efficiency tool after students understand what they're looking for
4. Reinforce with worked examples that directly mirror the hands-on activity

### Common Misconceptions to Address:
- "The scan tool tells me what's broken — I just need to replace it." Address on Slides 2 and 27.
- "I can use my multimeter instead of the scope." Address on Slide 10 with the intermittent dropout example.
- "I'll start probing from the sensor end and work inward." Address on Slide 22 with the efficiency comparison.

### Connection to Hands-On Session (11H):
- All worked examples in theory must use the same ECU and circuit as the lab session planted faults where possible
- The signal path map format introduced in Slide 8 is exactly the format students will complete in 11H
- Display Slides 13 (fault signatures) and 26 (decision flow) on the workshop projector during 11H

### Timing Flexibility:
- If running short: compress Slide 24 (split-half limits) — mention briefly, refer to reference card
- If running long: Slide 19 (in-circuit component testing) can be reduced to the table only
- Core content never to skip: Slides 8, 10, 13, 14, 21, 26

---

## SESSION SUCCESS CRITERIA

Students leave this session able to:
- Given a DTC, locate the relevant circuit in a wiring diagram and draw the complete signal path from sensor to MCU input with all probe points labelled
- Set up an oscilloscope correctly for probing a sensor signal line (DC coupling, correct scale, correct timebase, correct ground reference)
- Describe five fault signature patterns visible on an oscilloscope and state the circuit condition each indicates
- State where to make the first probe and explain what decision it enables (external vs internal fault)
- Apply the split-half method to a signal path with a given number of test points
- State how many measurements split-half requires for 4, 8, and 16 test-point paths
- Document line tracking results in a structured format: signal path map, probe log, fault conclusion

**Most importantly:** Students understand that line tracking is a systematic process that eliminates sections of the circuit with each measurement — and that the decision flow is followed without skipping steps.

---

*Module 5 | Day 11 Theory | ECUHR | v1.0 | 2026-02-18*
