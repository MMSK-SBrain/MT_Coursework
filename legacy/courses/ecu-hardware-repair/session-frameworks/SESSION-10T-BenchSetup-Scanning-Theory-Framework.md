# SESSION-10T: Bench Test Setup & ECU Scanning Fundamentals
## Instructor-Led Story Framework for PPT Preparation

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 5 — ECU On-Table Diagnostics
**Day:** 10 | **Session Type:** Theory
**Duration:** 90 minutes
**Approach:** Instructor-Led Narrative with Worked Examples
**PPT Target:** 28–32 slides

**Session Outcomes Addressed:**
- so-5-1-1: Identify required connections (battery positive, ground, ignition, CAN, K-Line) for bench testing a specific ECU from its wiring diagram | Apply
- so-5-2-1: Read DTC codes from a bench ECU, classify them as current/permanent/pending, and identify the circuit each code points to | Analyze

**CO Alignment:** co-1

---

## INSTRUCTOR-LED STORY ARC

---

### SETUP: Opening Hook (Slides 1–4, ~10 minutes)

**Narrative Voice:** Grounded and practical. Students have spent nine days learning how ECUs are built, how components fail, and how to solder. Today that knowledge is deployed for the first time in a diagnostic context. The tone shifts: from understanding circuits to finding what is wrong with them.

#### Slide 1: Title Slide
**Visual:** Photo of a real bench diagnostic setup — ECU sitting face-up on an anti-static mat, wiring harness running to a bench power supply, oscilloscope probe touching a connector pin, scan tool laptop open with a DTC list visible on screen.
**Instructor Script:**
> "This is what Module 5 is about. An ECU removed from a vehicle — no longer connected to anything — sitting on a bench. And from this setup, we can power it, communicate with it, read every fault it has stored, examine every sensor reading it sees, and eventually pinpoint the component that has failed. This is the professional ECU diagnostic workflow. Today I'm going to teach you step one and step two: getting the ECU alive, and reading what it tells you."

#### Slide 2: The Scenario That Drives This Session
**Visual:** An image of an ECU in a cardboard box with a handwritten note taped to it: "Astra 2012 — engine cuts out randomly — tried new ECU from dealer — same problem — sending original back for testing."
**Instructor Script:**
> "This is a real-world situation. A vehicle develops an intermittent cut-out. The dealership condemns the ECU and fits a new one. The problem persists. The old ECU gets sent to a repair workshop for bench testing. Now the question is: what is actually wrong with it?
>
> Without a systematic approach to bench testing, this ECU gets opened, stared at, and either declared faulty or declared fine — based on nothing more than a visual inspection and guesswork. With the approach you'll learn today, we can power the ECU correctly, communicate with it, read its exact fault history, examine the sensor data it was seeing when the problem occurred, and form a specific hypothesis about what failed and where.
>
> The difference between those two outcomes is what you're learning in Module 5."

#### Slide 3: Where We Are in the Diagnostic Workflow
**Visual:** A clean left-to-right workflow diagram:
`Read Wiring Diagram → Bench Power → Communication → Scan/DTC → Live Data → Line Trace → Component Test → Fault Confirmed`
First three stages highlighted in amber; remainder greyed out.
**Instructor Script:**
> "This is the complete on-table diagnostic workflow. By the end of Module 5 — Days 10, 11, and 12 — you will have worked through every stage. Today, we cover the first three: power, communication, and scanning. These three steps alone will tell you whether an ECU has a genuine internal fault or whether the problem is external to it."

#### Slide 4: Two Skills You Build Today
**Visual:** Two clean columns.
Left: "BENCH SETUP: Getting the ECU alive and communicating"
Right: "SCANNING: Reading and interpreting what it tells you"
**Instructor Script:**
> "Two skills. First: how to connect a removed ECU to a bench power supply correctly — using the wiring diagram to identify exactly which pins need power, ground, and ignition — so that the ECU behaves exactly as it would in the vehicle. Second: how to read the fault codes and live data the ECU reports, understand what each piece of information means, and use it to direct the diagnostic investigation.
>
> Neither skill is intuitive. Both are systematic. Let's begin."

---

### TRIGGER: Why Getting This Wrong Is Expensive (Slides 5–7, ~8 minutes)

#### Slide 5: Three Ways to Wreck the Bench Test Before It Starts
**Visual:** Three side-by-side diagrams of incorrect bench setups:
Diagram 1 — Missing one ground pin. Annotation: "ECU appears partially alive — communication fails."
Diagram 2 — No ignition supply connected. Annotation: "ECU stays in sleep mode — no DTCs, no live data."
Diagram 3 — Battery positive connected to a pin that is NOT B+. Annotation: "ECU damaged instantly — permanent fault."
**Instructor Script:**
> "These are three mistakes that look simple but destroy the diagnostic result — or destroy the ECU. None of them require the wrong voltage. They are configuration errors: wrong pins, missing connections.
>
> Missing one ground pin: most ECUs have multiple ground pins, not one. Miss any of them and you get partial function — the ECU may boot but refuse to communicate. People mistake this for an internal fault.
>
> No ignition supply: the ECU sits in key-off standby mode. The scan tool says 'no ECU detected.' The technician assumes the ECU is dead. It isn't — it's asleep.
>
> Wrong pin: 12V applied to the wrong connector pin can destroy an ECU in milliseconds. The wiring diagram prevents all three mistakes. This is why we read it first, always."

#### Slide 6: The DTC Misunderstanding That Costs Real Money
**Visual:** Large DTC displayed: `P0105 — MAP Sensor Circuit Malfunction`
Below it, four interpretations — three crossed out in red, one with green tick:
- "Replace the MAP sensor" — crossed out
- "Replace the ECU" — crossed out
- "Clear the code — probably nothing" — crossed out
- "The ECU detected an out-of-range condition in the MAP sensor circuit. Investigate the circuit." — green tick
**Instructor Script:**
> "P0105 does not mean the MAP sensor has failed. It means the ECU detected something wrong in the MAP sensor circuit. That circuit consists of: the MAP sensor itself, the three wires connecting it to the ECU, the connector at both ends, the PCB trace from the connector pin to the signal conditioning stage, and the components in that stage. Any one of those elements could be the fault.
>
> The DTC is the starting point of an investigation. It is never the conclusion. Understanding this distinction is the most important thing you take from today."

#### Slide 7: Live Data — The Second Diagnostic Language
**Visual:** Scan tool screenshot showing a live data stream. Three parameters highlighted in red: IAT reading 152 degrees C, coolant temperature reading -40 degrees C, TPS reading 4.8V at idle.
**Instructor Script:**
> "Alongside fault codes, a running ECU streams live data — every sensor value it is currently reading, updated several times per second. When sensors fail or circuits break, the ECU often continues reading them and reporting impossible values: an intake air temperature of 152 degrees C in a workshop, a coolant temperature of -40 degrees C on a warm engine, a throttle position of 97% at idle with nothing pressing the pedal.
>
> These impossible values are fault signatures. They appear in live data sometimes before a DTC is set, and they give you additional information about the nature of the fault."

---

### RISING ACTION Part 1: Bench Setup (Slides 8–20, ~38 minutes)

#### Slide 8: Section Header — BENCH SETUP
**Visual:** Section divider with a wiring diagram fragment in the background.
**Instructor Script:**
> "Bench setup begins before you touch a single wire. It begins with the wiring diagram. The sequence is: diagram first, connections second, power last. This order is not optional."

#### Slide 9: Why the Wiring Diagram Is Mandatory — Every Time
**Visual:** Two-panel comparison. Panel A: technician connecting wires without a diagram. Panel B: same ECU with smoke rising. Caption: "Familiarity is not the same as knowledge of this specific ECU."
**Instructor Script:**
> "You may have bench-tested ECUs before. You may believe you know where B+ goes on a 'typical' ECU. The problem is that every ECU is different. Pin 1 on a Bosch ME7 is B+. Pin 1 on a Siemens SID is not. A Delphi unit may have its ground pins spread across two connectors. An older Magneti Marelli unit may have the ignition supply on an entirely separate flying lead.
>
> The wiring diagram removes all assumption. It tells you exactly which pin carries which signal, for this specific ECU, from this specific vehicle."

#### Slide 10: Finding the Right Wiring Diagram
**Visual:** Flowchart: Vehicle identification (VIN or make/model/year) → Manufacturer workshop information system → ECU-specific connector diagram → Signal names and pin assignments.
**Instructor Script:**
> "For diagnostic workshops, the primary source is the vehicle manufacturer's workshop information system: ELSA for VAG, ETIS for Ford, WIS for Mercedes, TIS for Toyota. Alldata and Haynes Pro aggregate many of these.
>
> What you need: the connector diagram for your specific ECU, with all pin numbers and the signal name assigned to each pin. From that, you identify the four groups of connections needed for bench testing."

#### Slide 11: The Five Essential Connection Groups
**Visual:** Table with five rows.

| Connection | Typical Label | How to Identify | If Omitted |
|---|---|---|---|
| Battery positive | B+, KL30, VBAT | Main supply; usually largest wire gauge; connected to battery direct | ECU completely dead |
| All ground pins | GND, KL31, SGND | Multiple pins — must connect all of them | Communication failure; erratic readings |
| Ignition supply | IGN, KL15 | Switched supply; active only with key on | ECU in standby — no comms, no DTCs |
| Main relay output (some ECUs) | KL87, VBAT_SW | ECU-controlled relay output | ECU has voltage but cannot self-power its supply rail |
| Communication lines | CANH, CANL or K-Line | Protocol-specific; from wiring diagram | No scan tool communication |

**Instructor Script:**
> "Five connection groups. Battery positive is obvious — no power. But the grounds are where people go wrong. An ECU may have three, four, or five separate ground pins. Some are power grounds for output drivers. Some are signal grounds for sensors. If any is missing, you get voltage offsets, communication failures, or the ECU reports wrong values on every sensor simultaneously.
>
> Ignition supply is critical and commonly forgotten. Without KL15 active, the ECU detects a key-off state and enters standby. No DTCs are available. No live data. The scan tool cannot connect."

#### Slide 12: Reading the Wiring Diagram — Connector View Convention
**Visual:** Side-by-side of the same connector: front view (harness side) and PCB/rear view — pins mirror-reversed. Large caption: "Wiring diagrams always show FRONT VIEW (harness side). Check before you wire."
**Instructor Script:**
> "Here is a mistake I have seen experienced technicians make. The wiring diagram shows connectors from the front — the side the harness plugs into. But when you are holding an ECU face-up on the bench, you are looking at the connector from the rear — the PCB side. The pin numbering appears mirror-reversed.
>
> Before connecting any wire, hold the ECU so that you are looking at it from the front and check that your pin numbering matches the diagram."

#### Slide 13: Bench Power Supply — Setup and Safety
**Visual:** Photo of a bench power supply with annotations: "Voltage: 12.5V" and "Current limit: 2.0A." Separate diagram showing ECU connected to PSU, current display reading 0.3A — annotation: "Normal."
**Instructor Script:**
> "Set voltage to 12.5V — this simulates a charged resting battery. Current limit: start at 2.0A. A healthy ECU at bench power-on typically draws between 0.1A and 0.5A before ignition is applied. When ignition is applied and the processor boots, current may briefly rise to 0.8–1.2A, then settle. A 2.0A limit allows this normal behaviour while providing a firm cutoff if a shorted component tries to draw more.
>
> If you apply power and the current immediately clamps at 2.0A — do not increase the current limit. Power off, disconnect, investigate."

#### Slide 14: Power-On Sequence — Order Matters
**Visual:** Step-by-step vertical sequence diagram:
```
Step 1: Connect B+ and ALL GND wires (PSU output OFF)
Step 2: Apply PSU power — observe current reading — should be < 0.5A
Step 3: Connect IGN/KL15 wire — observe current rise — wait 3–5 seconds for ECU init
Step 4: Connect scan tool / OBD adapter
Step 5: Verify communication before scanning
```
**Instructor Script:**
> "Follow this sequence every time. Ground and battery positive first — with the PSU output still off. Then apply power and watch the current. Apply ignition by connecting KL15 to battery positive through a switch or jumper. Watch the current — it will briefly rise and settle. Give the ECU three to five seconds. It is running its initialisation routine: checking internal memories, running self-tests, initialising communication controllers.
>
> Only after this initialisation period do you connect the scan tool. Connecting the scan tool during initialisation can cause the ECU to abort the boot sequence on some platforms."

#### Slide 15: Current Limit as a Diagnostic Tool
**Visual:** Three-row table:

| Current at Power-On | What It Means | Action |
|---|---|---|
| 0.1–0.5A (IGN off) | Normal standby consumption | Continue with ignition step |
| 0.5–1.5A (after IGN on, settled) | Normal operating current | Continue — ECU is alive |
| Immediately clamps at limit | Shorted component in ECU or bench harness | Power off. Disconnect. Investigate. |

**Instructor Script:**
> "Your current display is not just a safety indicator — it is your first diagnostic data point. Write down the current reading at each stage on your worksheet. A healthy ECU has a predictable current profile. An ECU with an internal component short will reveal itself immediately when you try to power it."

#### Slide 16: CAN Bus on the Bench — The Isolation Problem
**Visual:** Two diagrams side by side. Left: vehicle CAN network — five ECUs connected. Right: same ECU on a bench — alone, other ECUs replaced by question marks.
**Instructor Script:**
> "Here is a challenge specific to bench testing. In the vehicle, your ECU under test was one node on a CAN network with multiple other ECUs. It expected to receive messages from those ECUs. On the bench, those modules are not present.
>
> This causes two effects. First: the ECU will set CAN communication fault codes for every missing network partner. These codes are artefacts of the bench environment — not genuine faults in the ECU under test. You must be able to recognise them.
>
> The rule: treat U-codes (network communication faults) with caution on the bench. Focus first on P-codes relating to sensors and actuators internal to the ECU's own operation."

#### Slide 17: K-Line Protocol — When CAN Is Not There
**Visual:** Comparison table:

| Feature | CAN (ISO 15765) | K-Line (ISO 9141 / KWP2000) |
|---|---|---|
| Wires | 2 — CANH + CANL, differential | 1 wire (K-Line) + optional L-Line |
| OBD connector pin | 6 (CANH), 14 (CANL) | 7 (K-Line) |
| Speed | Up to 1 Mbit/s | 10.4 kbaud typical |
| Vehicles | 2006+ (mandatory from 2008) | Pre-2008 predominantly |
| Bench connection | CANH/CANL from ECU connector | K-Line from ECU connector to OBD pin 7 |

**Instructor Script:**
> "Before approximately 2008, most vehicles used K-Line as the OBD diagnostic protocol — also referred to as KWP2000 or ISO 14230. K-Line is a single-wire protocol running at 12V.
>
> For bench testing older ECUs, you must identify the K-Line pin from the wiring diagram and connect it to pin 7 of your OBD breakout harness. Not all scan tools support K-Line — confirm before you start. If your tool supports only CAN and you have a K-Line ECU, you will get no communication regardless of how correctly the ECU is powered."

#### Slide 18: Worked Example — Bosch ME7 Bench Setup
**Visual:** Annotated wiring diagram excerpt for a Bosch ME7 engine management ECU. Two connectors shown (55-pin and 60-pin). Key pins highlighted in colour: B+ pins (amber), GND pins — all three (red), KL15 pin (green), CANH and CANL pins (blue).
**Instructor Script:**
> "Let's apply this to a real ECU. The Bosch ME7 is one of the most commonly encountered engine ECUs in European repair workshops — found in VAG, BMW, and several other platforms.
>
> On the 55-pin connector: pins 1 and 2 are B+ (both must be connected). Pins 3, 4, and 5 are ground (all three required). Pin 6 is KL15.
>
> On the 60-pin connector: the CAN pins vary by application and will be identified on the specific vehicle wiring diagram.
>
> Before I touch a single wire: I have identified six connections — two B+, three GND, one KL15. I know my bench setup completely. Now I can connect, in the correct sequence, with confidence."

#### Slide 19: Common Bench Setup Mistakes — Reference Card
**Visual:** Red-bordered slide with table.

| Mistake | Consequence |
|---|---|
| Connected only one of multiple GND pins | ECU powers but won't communicate; voltage measurements appear shifted |
| Forgot KL15 — no ignition supply | ECU in standby — scan tool shows no ECU found |
| Read connector from PCB side instead of harness side | Wired to wrong pins — may damage ECU if B+ lands on signal pin |
| Set current limit to 5A or 10A for "safety" | No overcurrent protection — shorted ECU component not detected |
| Connected scan tool before ECU finished initialising | Some ECUs abort boot sequence; shows as no communication |
| Reversed CANH and CANL | CAN bus won't communicate — differential voltage inverted |
| Did not confirm K-Line support on scan tool | No communication on pre-2008 ECU regardless of correct wiring |

**Instructor Script:**
> "Put this on the wall. Every one of these mistakes produces a result that looks like the ECU is dead or faulty. Every one of them is something you did — not a fault in the ECU. Before you conclude the ECU cannot be diagnosed, eliminate every item on this list."

#### Slide 20: Discussion Checkpoint
**Visual:** Pause icon. Question: "You power up a bench ECU and the current immediately clamps at 2.0A. After 3 seconds it hasn't settled. What are the possible causes and what do you do next?"
**Instructor Script:**
> "Sixty seconds. Discuss with the person next to you.
>
> [Wait]
>
> Possible causes: shorted bypass capacitor on the power rail; shorted TVS diode; reverse protection diode shorted; damaged power stage MOSFET with drain-source short; error in bench wiring — two pins that should not be connected are bridged.
>
> What you do: power off. Do not increase the limit. Disconnect the bench harness from the ECU. Apply power to bench harness alone — if current clamps, the short is in your harness. If not, reconnect the ECU without IGN first. Isolate systematically."

---

### RISING ACTION Part 2: Scanning and DTC Interpretation (Slides 21–28, ~25 minutes)

#### Slide 21: Section Header — SCANNING AND DTC INTERPRETATION
**Visual:** Scan tool screen showing a list of DTCs — a mix of current, historical, and pending codes in different status colours.
**Instructor Script:**
> "You have a live ECU on the bench. The scan tool says connected. Now you read what the ECU has to say — and you read it correctly. DTCs are structured data. They have a format, a classification system, and a status. All of those matter."

#### Slide 22: Anatomy of a DTC
**Visual:** DTC code broken down character by character with annotations:
```
P  0  1  0  5

P  = Powertrain (B = Body, C = Chassis, U = Network)
0  = SAE/generic (1 = manufacturer-specific)
1  = Subsystem: Fuel and Air Metering
05 = Specific fault: MAP sensor circuit
```
**Instructor Script:**
> "Every OBD-II DTC follows this structure. The letter identifies the system. P is powertrain. B is body. C is chassis. U is network — module-to-module communications.
>
> The first digit identifies whether the code is standardised across all manufacturers (0) or manufacturer-specific (1, 2, or 3). P0 codes have the same meaning in every vehicle. P1 codes mean different things on a Ford than on a BMW.
>
> The remaining three digits specify the exact circuit and fault type. P0105: powertrain, generic, fuel and air metering subsystem, MAP sensor circuit. Note: circuit. Not sensor."

#### Slide 23: The Four DTC Status Types
**Visual:** Four colour-coded panels:
- CURRENT / ACTIVE (solid red): Fault present right now — circuit test failed on last drive cycle
- PENDING (amber): Detected once — needs confirmation on another drive cycle to set MIL
- PERMANENT (solid orange): Confirmed fault stored in non-volatile memory — cannot be cleared without actual repair + drive cycle
- HISTORICAL / STORED (grey): Was present; no longer active — may be intermittent or already resolved
**Instructor Script:**
> "Status matters as much as the code itself. Current means the fault exists at this moment. The circuit test fails every time the ECU runs it. This is the most actionable status.
>
> Pending means the ECU detected the fault once but has not confirmed it on two consecutive drive cycles.
>
> Permanent is a feature added in later OBD-II implementations. Once a fault is confirmed, it is written to permanent memory and cannot be cleared with a scan tool's clear codes function. It can only be extinguished by the fault actually being repaired and the ECU running through the relevant monitor successfully.
>
> Historical means the fault was detected and confirmed but is no longer present. This is your intermittent fault category."

#### Slide 24: What Circuit Does the DTC Point To?
**Visual:** Wiring diagram fragment for MAP sensor circuit, fully annotated with sensor body, 5V reference wire, signal output wire, signal ground wire, in-line connector mid-harness, ECU connector pin, PCB trace, series protection resistor, input filter capacitor, ADC input.
**Instructor Script:**
> "Once you have a DTC and you know its status, the next step is to identify exactly what circuit it refers to. From the workshop manual or scan tool's diagnostic procedure, you identify which pins are involved, what the normal operating range is, and what specific thresholds cause the fault to set.
>
> From that information, you go to the wiring diagram and trace the circuit. For P0105: the 5V reference from the ECU to the sensor, the signal output from the sensor back to the ECU, and the signal ground. The DTC has taken you from 'something is wrong' to 'one of these specific paths has a problem.' That is enormous progress."

#### Slide 25: Reading Multiple DTCs — Finding the Pattern
**Visual:** Example DTC list: P0105 Current (MAP sensor circuit low), P0115 Current (coolant temp sensor circuit), P0130 Current (O2 sensor circuit), U0100 Current (lost communication with ECM/PCM), U0155 Current (lost communication with instrument cluster).
Pattern annotations shown.
**Instructor Script:**
> "When you see multiple simultaneous DTCs, look for patterns before investigating individual codes. Multiple sensor faults all active at the same time — MAP, coolant temp, throttle, O2 all showing circuit faults simultaneously — does not mean four sensors failed at once. This pattern almost always means a common power or ground supply has failed.
>
> Multiple U-codes on a bench without the full CAN network present are expected. Treat them as environment artefacts. Focus on the P-codes and C-codes that relate to internal ECU functions."

#### Slide 26: Freeze Frame Data — The Operating Context
**Visual:** Freeze frame data table: Engine speed: 3,450 RPM | Coolant temp: 88 degrees C | Battery voltage: 9.2V | Throttle position: 27% | MAP value: 94 kPa.
**Instructor Script:**
> "When a DTC sets, most ECUs simultaneously capture and store a snapshot of other sensor values at that exact moment. This is freeze frame data.
>
> Look at this example. The MAP fault set at 3,450 RPM — fault occurs under load. Battery voltage was 9.2V at the moment — suggests this may have occurred during hard acceleration with a struggling charging system. Freeze frame transforms a DTC from 'there was a problem' to 'there was a problem under these specific conditions.' This is how you find intermittent faults."

#### Slide 27: Live Data — Identifying Out-of-Range Sensors
**Visual:** Split-screen scan tool live data. Left — healthy values: IAT 22 degrees C, ECT 88 degrees C, TPS 0.52V, MAP 38 kPa. Right — faulty values: IAT 152 degrees C, ECT -40 degrees C, TPS 4.85V, MAP 0 kPa.
**Instructor Script:**
> "IAT at 152 degrees C indoors: the intake air temperature signal wire is shorted to a voltage source. The sensor input reads maximum voltage, which maps to maximum temperature.
>
> Coolant temp at -40 degrees C: the signal wire is open circuit. With no sensor connected, the ADC input floats low or reads 0V. The ECU maps 0V to the lowest calibrated temperature value.
>
> TPS at 4.85V at idle: the throttle sensor signal is shorted to a voltage source. The ECU thinks the throttle is fully open.
>
> MAP at 0 kPa: the MAP signal is shorted to ground or the signal wire is open and the input pulls low. 0 kPa is physically impossible. This is a circuit fault signature."

#### Slide 28: Clear, Cycle, Re-scan — The Confirmation Step
**Visual:** Decision tree diagram:
```
Record all DTCs → Clear all DTCs → Cycle ignition (off then on) → Wait 30 seconds → Re-scan

DTC returns immediately → CURRENT fault (condition still present)
DTC does not return → HISTORICAL fault (was present, not now)
Some DTCs return, some don't → Mixed: current and historical faults
```
**Instructor Script:**
> "Once you have read and photographed all DTCs, use the clear-and-rescan technique to determine which faults are current. Clear everything. Cycle the ignition: remove KL15, wait 10 seconds, reconnect KL15, wait 30 seconds. Re-scan.
>
> Any DTC that returns immediately is a current fault. Any DTC that does not return is historical.
>
> Write down everything before you clear. Some ECUs have permanent memory that cannot be cleared. Note those specifically — they are confirmed faults that require actual repair to extinguish, not just a clear command."

---

### CLIMAX: The Diagnostic Entry Point (Slides 29–30, ~8 minutes)

#### Slide 29: The Complete Bench Scanning Workflow
**Visual:** Complete annotated step-by-step process — build progressively:
```
1.  Identify ECU type → locate wiring diagram
2.  Identify all B+, GND, KL15, CAN/K-Line pins from connector diagram
3.  Set PSU: 12.5V, 2.0A limit
4.  Connect B+ and all GND wires (PSU off)
5.  Apply PSU power → observe current draw → should be < 0.5A
6.  Apply KL15 → wait 5 seconds for ECU initialisation
7.  Connect CAN adapter / OBD harness
8.  Open scan tool → verify communication → record protocol detected
9.  Read ALL DTCs → record status (current/pending/permanent/historical)
10. Read freeze frame for each current DTC → record operating conditions
11. Read live data → identify any out-of-range values → document
12. Clear DTCs → cycle ignition (off then on) → wait 30 seconds → re-scan
13. Record which DTCs returned (current) and which did not (historical)
14. Identify target circuit from confirmed current DTC
15. Proceed to line tracking (Day 11)
```
**Instructor Script:**
> "This is the complete workflow. You follow it every single time — with every ECU, regardless of what anyone tells you is wrong with it. By step 14 of this workflow, you know: which circuit is involved, whether the fault is reproducible right now, what the operating conditions were when it set, and whether there are additional faults that might share a common root cause. You have your diagnostic entry point."

#### Slide 30: What Scanning Can and Cannot Tell You
**Visual:** Two-column table:

| Scanning CAN tell you | Scanning CANNOT tell you alone |
|---|---|
| Which circuits are suspect | Which specific component failed |
| Whether the fault is current or historical | Whether the fault is in the harness or on the PCB |
| The operating conditions when the fault set | Whether the ECU itself is the faulty item |
| Whether the fault is reproducible now | What repair is needed |

**Instructor Script:**
> "Understand the limits. Scanning gives you the circuit and the context. It does not give you the component. Some technicians expect the scan tool to tell them what to replace. It doesn't. It tells you where to look. The investigation that comes after scanning — line tracking and component testing — gives you the answer.
>
> This distinction is what separates a diagnostic professional from someone who replaces parts until the problem goes away."

---

### RESOLUTION: Consolidation (Slides 31–32, ~7 minutes)

#### Slide 31: Summary Reference Cards
**Visual:** Two clean reference cards on one slide.

Card 1 — Bench Setup Rules:
- Wiring diagram before any connection — always
- Connect ALL ground pins
- B+ and GND first; KL15 second, after PSU power confirmed
- Current limit: 2.0A — do not bypass it
- Wait 3–5 seconds after KL15 before connecting scan tool
- Know whether ECU uses CAN, K-Line, or both

Card 2 — DTC Reading Rules:
- Record status before anything else: current/pending/permanent/historical
- Read freeze frame for each current DTC
- Multiple simultaneous codes: look for patterns
- U-codes on bench: likely environment artefacts — investigate P-codes first
- Read live data: impossible values are circuit failure signatures
- Clear, cycle, re-scan: confirms which faults are current
- DTC points to a circuit, not a component

#### Slide 32: Preview of Day 10H and Day 11
**Visual:** Left panel — bench setup activity. Right panel — oscilloscope probing on PCB test point.
**Instructor Script:**
> "This afternoon you do this yourselves. You'll each receive a real ECU and its wiring diagram. You'll identify the required connections, wire the bench harness, apply power, connect the scan tool, read the DTCs, classify them, read the live data, clear them, cycle, and re-scan. You'll document everything on your worksheet.
>
> Tomorrow, Session 11T teaches line tracking — how to follow a signal from the sensor all the way into the ECU and find exactly where it breaks. Session 11H is an independent fault-finding exercise on a live ECU with a planted fault.
>
> Questions before we move to the workshop?"

---

## PPT DESIGN GUIDANCE

### Visual Style:
- Dark professional theme: charcoal background with amber/orange accent — consistent with Module 4 sessions
- Clean sans-serif body font (Inter or Roboto); monospace for DTC codes, pin references, and terminal labels (KL30, KL15)
- Annotated diagrams from real ECU wiring diagrams where possible — Bosch ME7 is an excellent teaching example
- Scan tool screenshots from real equipment — students must recognise the tools they will use
- Photographs over illustrations wherever possible — this course is vocational

### Key Slides to Emphasise:
- Slide 11 (Five Essential Connections): reference card quality — students will photograph this before every bench session
- Slide 12 (Connector view convention): safety-critical — mirrored pin numbering causes permanent damage
- Slide 13 (PSU setup): pause for questions — current limit concept is not intuitive to all students
- Slide 23 (Four DTC status types): most important conceptual slide — colour coded, reveal individually
- Slide 29 (Complete workflow): build progressively — students should recognise this as the procedure they will follow this afternoon

### Animations:
- Slide 23 (DTC status): reveal each panel individually — do not show all four simultaneously
- Slide 25 (Multiple DTCs pattern): reveal U-codes and P-codes separately
- Slide 29 (Complete workflow): build step by step — pause at each step for instructor comment
- Slide 19 (Common mistakes): reveal each row as a mistake + consequence pair

---

## INSTRUCTOR NOTES

### Pedagogical Strategy:
This session uses the narrative + worked example model:
1. Motivate the skill before teaching it — the Astra scenario establishes why precision matters
2. Build bench setup knowledge from diagram outward — diagram first, connections second, power last
3. Teach DTC interpretation through specific concrete examples, not abstract definitions
4. Deliver a complete reference workflow before the hands-on session

### Prerequisite Check:
Students should be comfortable reading wiring diagrams from Module 2 (Day 3). If there is uncertainty in the room, spend additional time on Slides 9–12. Wiring diagram competency is the prerequisite for everything that follows in Module 5.

### Managing Student Experience Variation:
Some students will have used scan tools before and may be dismissive of DTC status classification. Address this when you reach Slide 23. The four-status classification, particularly the difference between pending and permanent, is not commonly taught in basic automotive training. Frame it as precision professional practice.

### Timing Management:
- If running short: compress Slide 17 (K-Line) — note the topic, provide the reference card, move on
- If running long: Slide 26 (freeze frame) can be reduced to one example
- Core content never to skip: Slides 9, 11, 13, 23, 28, 29

### Lab Preparation Note for 10H:
Each bench must have a communicating ECU with wiring diagram, bench PSU, pre-fabricated bench harness labelled at all connection points, OBD breakout harness, scan tool with correct protocol support. Confirm before students arrive that all bench ECUs are communicating and have some DTCs present.

---

## SESSION SUCCESS CRITERIA

Students leave this session able to:
- Read a wiring diagram for an unfamiliar ECU and identify all required bench connections
- State the correct bench PSU voltage and initial current limit and explain the reasoning for each
- Describe the correct power-on sequence and explain why KL15 is applied after B+ and GND
- Classify a DTC as current, pending, permanent, or historical from scan tool output
- Explain the difference between a pending and a permanent fault status
- Identify which circuit a DTC points to — not which component
- Identify a physically impossible live data value and propose the circuit fault type that would produce it
- Describe the clear-cycle-rescan procedure and explain what conclusion it enables

**Most importantly:** Students understand that the scan tool is an entry point, not a conclusion.

---

*Module 5 | Day 10 Theory | ECUHR | v1.0 | 2026-02-18*
