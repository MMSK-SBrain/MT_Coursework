# SESSION-04T: PCB Architecture, MCU & Memory
## Instructor-Led Theory Framework

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 3 — ECU Architecture, Protection & Filtering (Days 4–6)
**Session:** Day 4 — Theory
**Duration:** 90 minutes
**Format:** Instructor-led lecture with live PCB demonstration
**PPT Target:** 22–25 slides

---

## Session Outcomes

| SO ID | Description | Bloom |
|-------|-------------|-------|
| so-3-1-1 | Identify PCB layer structure and explain the purpose of each layer | Understand |
| so-3-1-2 | Locate test points, reference designators, and component silkscreen markings | Apply |
| so-3-1-3 | Explain MCU, co-processor, EEPROM, FLASH, RAM, and clock oscillator roles | Understand |
| so-3-1-4 | Explain watchdog circuit function and firmware hang recovery | Understand |

---

## Module 3 Narrative Thread

> "Module 2 gave you the measurement tools. Now you need to understand *what* you are measuring and *why* it is there. Every component on an ECU PCB has a job. If it has a job, it can fail. If it can fail, you need to be able to find it."

Day 4 sets the structural foundation: how the PCB is built in layers, what the silicon core does, and how the board keeps itself alive even when firmware crashes. Days 5 and 6 build on this to cover filtering, protection, drivers, and thermal management.

---

## INSTRUCTOR STORY ARC

### OPENING HOOK (Slides 1–4, ~10 minutes)

#### Slide 1: Title
**Visual:** High-resolution top-down photo of a real automotive ECU PCB — conformal coat removed, components visible
**Instructor Script:**
> "Good morning. Look at this board for a moment. Count what you see: capacitors, resistors, ICs, connectors, test points. Most technicians who bring an ECU to a workshop look at this and see chaos. By the end of this week, you will look at this board and see structure — every component in a category, every category with a job, every job with a failure mode you can test for.
>
> Today we start with the foundation: the physical construction of the PCB itself, and the digital heart — the processor and its memory."

#### Slide 2: Connection to Module 2
**Visual:** Three-panel image: multimeter probing a component / oscilloscope trace / PCB top view with question marks
**Instructor Script:**
> "In Module 2 you learned to use your tools. You can measure resistance, capture waveforms, trace signals. But there is a critical problem: if you do not know what a component is supposed to do, you cannot interpret what your measurement means.
>
> A capacitor measuring 0 ohms — is that a short circuit or a good capacitor? A diode measuring 0.6V forward voltage — is that right or wrong? The answer depends entirely on knowing what that component's job is.
>
> That is what Module 3 gives you: the *meaning* behind your measurements."

#### Slide 3: The ECU as a System
**Visual:** Block diagram — battery input → protection → power supply → processor + memory → I/O drivers → connectors
**Instructor Script:**
> "An ECU is not a random collection of parts. It is a system with a clear architecture. Every part of that architecture has a region on the PCB, and every region has recognisable components.
>
> By the end of Days 4, 5, and 6, you will be able to look at any automotive ECU and identify:
> - Where the power comes in and how it is protected
> - Where the processor and memory live
> - Where the filtering components are and why they are placed where they are
> - Where the output drivers are and how they switch real loads
>
> Today: PCB construction, and the processor region. Let us start at the very bottom — literally — with the board itself."

#### Slide 4: Today's Journey
**Visual:** Simple roadmap with four stops labelled
**Instructor Script:**
> "Four topics today:
>
> 1. PCB layer structure — why it is not just a flat piece of fibreglass
> 2. Reading the board — reference designators, test points, silkscreen markings
> 3. The processor region — MCU, co-processor, EEPROM, FLASH, RAM, clock
> 4. The watchdog — the circuit that reboots the ECU when firmware hangs
>
> At the end we will do a concept check before tomorrow's hands-on session."

---

### PART 1: PCB Layer Structure (Slides 5–8, ~18 minutes)

#### Slide 5: What is a PCB? — Beyond the Green Board
**Visual:** Exploded layer diagram of a 4-layer PCB — label each layer with its name and function
**Instructor Script:**
> "When you look at an ECU, you see the top surface. But an automotive ECU PCB is a multilayer sandwich — typically 4 to 6 layers, sometimes 8 for complex powertrain ECUs.
>
> The most common configuration you will encounter is 4 layers:
>
> - **Layer 1 (Top):** Component placement and signal traces — this is what you see
> - **Layer 2:** Ground plane — a solid copper layer connected to chassis ground
> - **Layer 3:** Power plane — distributes regulated supply voltage to all ICs
> - **Layer 4 (Bottom):** More signal traces and some component placement
>
> Between these copper layers is FR4 fibreglass — the insulating substrate that holds the whole structure together."

#### Slide 6: Why Multilayer — Three Engineering Problems Solved
**Visual:** Split diagram — left: single-layer with crossing traces; right: multilayer, clean routing, hidden infrastructure
**Instructor Script:**
> "The multilayer design solves three engineering problems at once:
>
> **Problem 1 — Routing space:** An ECU with 200+ pins on the MCU cannot route all those signals on one layer without traces crossing. Additional layers provide the space.
>
> **Problem 2 — Ground plane:** The solid copper ground plane on Layer 2 is critical for EMC. Every IC, every component, every connector has the shortest possible path to ground. Short return paths mean less inductance, less noise, less susceptibility to interference. We will return to this in detail on Day 5.
>
> **Problem 3 — Power distribution:** The power plane distributes regulated voltage uniformly to all ICs without long traces that would add resistance and create voltage drops under load.
>
> Diagnosis relevance: when you see a failed ECU with a burned trace on Layer 1, the damage may extend into Layer 2. You cannot assume the visible damage is the only damage."

#### Slide 7: The Ground Plane — Your Most Important Reference
**Visual:** Cross-section photo showing PCB via holes, with diagram illustrating stitching vias connecting layers
**Instructor Script:**
> "Let me spend a moment on the ground plane because it appears repeatedly in EMC, noise problems, and failure analysis.
>
> On a multilayer PCB, the ground plane is a solid copper sheet covering most of the board area. Every component has at least one via — a small plated-through hole — that connects its ground pin straight down to this plane.
>
> This is why when an ECU takes a severe load dump event, the ground plane can sometimes delaminate from the substrate. You will see it as a PCB that looks bubbled, or where traces lift when you probe them. That is board damage at the substrate level — usually beyond economic repair.
>
> Takeaway: The ground plane is infrastructure. Damage to it is as serious as damage to the main supply rail."

#### Slide 8: Vias — How Signals Move Between Layers
**Visual:** Cross-section diagram showing through-hole vias, blind vias, and buried vias with labels
**Instructor Script:**
> "Layers are connected by vias — small plated copper cylinders that pass through the board.
>
> Types you will encounter:
> - **Through-hole vias:** Go all the way through the board — visible as small circles on both sides
> - **Blind vias:** Connect Layer 1 to Layer 2 but do not go all the way through — not visible from the opposite side
> - **Buried vias:** Connect inner layers only — invisible from either surface
>
> Why does this matter for repair? When you are tracing a signal and the trace seems to disappear on the top layer, it has not ended — it has gone underground through a via. You need to look for a via and then trace the continuation on the bottom layer, or use a continuity test to follow it.
>
> Practical tip: On automotive ECUs, test points are often placed near vias specifically so technicians can probe signals that are otherwise buried inside the board."

---

### PART 2: Reading the Board (Slides 9–12, ~15 minutes)

#### Slide 9: Reference Designators — The Component Naming System
**Visual:** PCB top-down photo with callouts: R12, C45, U3, D7, L2, Q1, X1, TP4, F1
**Instructor Script:**
> "Every component on a PCB has a reference designator — a code that tells you what type of component it is and which one it is within that type.
>
> The standard system you will see on every ECU:
>
> | Prefix | Component Type |
> |--------|----------------|
> | R | Resistor |
> | C | Capacitor |
> | U or IC | Integrated circuit |
> | D | Diode (includes TVS, Zener) |
> | L | Inductor or ferrite bead |
> | Q | Transistor or MOSFET |
> | X or Y | Crystal or oscillator |
> | J or CN | Connector |
> | TP | Test point |
> | F | Fuse |
>
> These are printed on the silkscreen — the white ink layer on the PCB surface. When you have a schematic, you cross-reference the designator to find the component in the diagram. Without service data, the designator at minimum tells you the component category so you know what test approach to use."

#### Slide 10: Silkscreen Markings — What Else to Read
**Visual:** Annotated PCB photo showing component outline, reference designator, polarity marking, and Pin 1 indicator on an IC
**Instructor Script:**
> "The silkscreen also contains:
>
> **Component outlines:** The white rectangle, circle, or shape printed around where the component sits. This tells you the component's footprint and orientation.
>
> **Polarity markings:** For polarised capacitors, a '+' or striped band indicates the positive terminal. For diodes and transistors, the outline often includes a diode symbol or triangle. For ICs, a dot or notch marks Pin 1.
>
> **Value markings (sometimes):** Some manufacturers print the component value on the silkscreen for passives — for example '10k' next to a resistor, or '100n' next to a decoupling capacitor.
>
> Diagnosis application: if you are replacing a component and you cannot read the markings on the component body itself, the silkscreen polarity indicator tells you which way round it goes. Installing a polarised electrolytic capacitor backwards will destroy it within seconds of power-on."

#### Slide 11: Test Points — The Diagnostic Access Layer
**Visual:** PCB with test points circled and labelled — TP_BAT, TP_5V, TP_GND, TP_CAN_H, TP_VREF
**Instructor Script:**
> "Test points are your diagnostic entry points into the ECU. On automotive ECUs they appear as:
>
> - Small bare copper pads — no component, no solder, just exposed copper
> - Small wire loops soldered to the board
> - Exposed via pads with no solder mask over them
>
> What they give you access to:
> - **Power rails:** TP_BAT, TP_5V, TP_3V3 — measure supply voltages without probing IC pins directly
> - **Ground references:** TP_GND — confirm your ground reference before every measurement
> - **Signal lines:** CAN bus, sensor inputs, clock outputs, PWM signals
> - **Programming access:** Some ECUs expose JTAG or SPI test points for bootloader access — you will use these in Module 6
>
> Test points are labelled in the manufacturer's service documentation. Without documentation, identify them by their characteristic appearance — bare pad, no component — and then probe them to determine what signal they carry.
>
> Rule: Always establish your ground reference at TP_GND before probing anything else."

#### Slide 12: Board Orientation and Region Identification
**Visual:** ECU PCB with coloured regions highlighted: power entry, processor, communication ICs, I/O drivers, connectors
**Instructor Script:**
> "When you pick up an unknown ECU, use this systematic sequence before touching a probe to anything:
>
> **Step 1 — Identify the connectors.** This is where the harness plugs in. The connector region is always at the board edge. Everything flows inward from here.
>
> **Step 2 — Follow the power.** The high-current power connector pins will lead you toward the protection and power supply region via thick traces.
>
> **Step 3 — Find the largest IC.** On most ECUs, the MCU is the dominant component — usually a 64 to 176-pin QFP package near the centre of the board, often with a crystal oscillator placed very close to it.
>
> **Step 4 — Look for the communications region.** CAN and LIN transceivers are usually near the connector edge — they are the interface between the vehicle network and the processor.
>
> **Step 5 — Find the driver region.** Large MOSFETs, output driver ICs, and flyback diodes are typically near the output connector or at the board edge opposite the power input.
>
> In tomorrow's hands-on session, you will apply this exact sequence on a real ECU."

---

### PART 3: The Processor Region — MCU, Memory, and Clock (Slides 13–19, ~25 minutes)

#### Slide 13: The Digital Core — Five Elements
**Visual:** Block diagram of processor region — MCU connected to EEPROM (SPI), FLASH (internal or SPI), RAM (internal), clock oscillator (XTAL pins), co-processor (data bus)
**Instructor Script:**
> "The processor region of an ECU typically contains five elements working together. Understanding each one is essential because each is a distinct failure point, and each stores or processes different data.
>
> Let us go through them one by one."

#### Slide 14: The MCU — The Brain
**Visual:** Photo of a typical automotive MCU (Renesas RH850, Infineon TriCore, or NXP MPC5xxx) in QFP package, with annotated pin groups: ADC inputs, PWM outputs, CAN/LIN pins, power/ground, XTAL
**Instructor Script:**
> "The microcontroller — MCU — is the central processor. In automotive ECUs you will typically encounter:
>
> - **Renesas RH850 / V850** — common in Japanese OEM ECUs (Toyota, Honda, Denso)
> - **Infineon TriCore (TC27x, TC39x)** — common in European OEM ECUs (Bosch, Continental)
> - **NXP MPC5xxx series** — used in many North American and European applications
> - **STMicroelectronics SPC series** — another European OEM choice
>
> The MCU receives all sensor signals through its ADC (analogue-to-digital converter), executes the control software, and drives outputs through PWM outputs and serial bus interfaces.
>
> Diagnosis approach: if the MCU is completely dead — no clock activity, no communication, no outputs — the fault is either the MCU itself, its power supply, its clock oscillator, or its reset circuit. You must eliminate each candidate before condemning the MCU, because MCUs are expensive and rarely fail unless there has been an overvoltage or ESD event."

#### Slide 15: EEPROM — The Calibration and Adaptation Store
**Visual:** Small SOIC-8 chip photo labelled EEPROM, with diagram showing MCU communicating via SPI/I2C, and a list of what is stored
**Instructor Script:**
> "EEPROM — Electrically Erasable Programmable Read-Only Memory — stores data that must survive power loss but needs to be updatable during normal vehicle operation.
>
> In an ECU, EEPROM typically stores:
> - **Learned adaptations:** Idle speed trims, throttle position calibration, injector corrections
> - **Mileage and service data:** Engine operating hours, fault history timestamps
> - **Fault code history:** Permanent DTCs that survive a battery disconnect
> - **Immobilizer security data:** Coded values matched to the key transponder and immobilizer module
>
> EEPROM is electrically separate from the main FLASH. It is read and written via SPI or I2C bus by the MCU during normal operation — not just during programming sessions.
>
> Failure mode: EEPROM data corruption causes persistent fault codes that cannot be cleared, or adaptation values that jump to extreme positions on every cold start. In Module 6, you will read EEPROM directly via the SPI interface as part of programming and security recovery procedures."

#### Slide 16: FLASH — The Firmware Store
**Visual:** Diagram showing internal FLASH (embedded in MCU die) vs external FLASH IC (separate SOIC chip connected via SPI), with annotations on what each section stores
**Instructor Script:**
> "FLASH memory stores the firmware — the program the MCU executes. On modern automotive ECUs there are two physical arrangements:
>
> **Arrangement 1 — Internal FLASH:** The MCU has FLASH memory built into the same silicon die. This is standard on modern ECUs. The firmware cannot be accessed without the MCU's programming interface — JTAG, BDM, or SPI boot mode.
>
> **Arrangement 2 — External FLASH:** A separate FLASH IC connected to the MCU via SPI or parallel bus. More common on older ECUs. The technician advantage: the chip can be physically removed and read or written on a standalone programmer.
>
> What is stored in FLASH:
> - **Firmware (operating code):** The control algorithms, event handlers, communication stack
> - **Calibration tables:** Injection maps, ignition timing tables, lambda correction tables
> - **Bootloader:** A small, protected program that accepts new firmware via OBD or boot interface
>
> Diagnosis: FLASH corruption causes the ECU to boot only to bootloader mode, produce no OBD communication, or behave randomly. A corrupted FLASH is repaired by reflashing — Module 6 covers this completely."

#### Slide 17: RAM — The Working Memory
**Visual:** Diagram showing MCU with internal SRAM block labelled 'Running Data — Lost on Power Down', with arrows showing sensor values, computed outputs, and DTCs flowing through RAM
**Instructor Script:**
> "RAM — Random Access Memory — is the working scratchpad. In virtually all modern automotive ECUs, RAM is internal to the MCU. There is no separate RAM chip on the board.
>
> RAM stores:
> - Current sensor values being processed in the current control cycle
> - Intermediate calculation results
> - Current output states — PWM duty cycles, actuator positions
> - Runtime diagnostic data before it is committed to EEPROM
>
> Critical characteristic: RAM content is lost the moment power is removed. This is why battery disconnection causes some adaptations to reset — learned values held in RAM had not yet been written to EEPROM.
>
> Diagnosis: RAM failure is rare and almost always means the MCU has failed. However, RAM corruption from power supply noise can cause a running ECU to behave erratically across engine cycles. The watchdog circuit — which we cover next — is the primary defence against this."

#### Slide 18: The Clock Oscillator — The Heartbeat
**Visual:** Photo of crystal resonator placed immediately adjacent to MCU, with diagram showing squarewave clock signal entering XTAL pins and PLL multiplying to high operating frequency
**Instructor Script:**
> "The MCU is a synchronous digital device — it executes one instruction per clock cycle. It cannot function without a clock signal.
>
> On automotive ECUs, the clock source is usually one of two types:
>
> **Type 1 — Crystal resonator:** A quartz crystal placed very close to the MCU's XTAL pins — within 5 to 10mm. Typical frequencies: 8 MHz, 16 MHz, 20 MHz. The MCU's internal PLL multiplies this to its full operating frequency — often 200 MHz or higher internally.
>
> **Type 2 — Crystal oscillator module:** A pre-buffered oscillator in a small 4-pin package. More stable and easier to replace.
>
> Failure symptoms when the clock fails:
> - ECU completely dead: no OBD response, no PWM outputs, no CAN communication
> - No clock signal at XTAL pins when measured with an oscilloscope
> - MCU power supply is present and correct — but no digital activity at all
>
> Crystal failures are caused by physical damage from vibration or PCB flexing, moisture ingress that detunes the crystal, or broken traces on the very short, very sensitive XTAL trace pair.
>
> Identification on the board: Look for a small silver rectangle or cylinder placed immediately next to the MCU. The silkscreen may label it XTAL, OSC, or Y1."

#### Slide 19: The Co-Processor — When One MCU is Not Enough
**Visual:** Block diagram — main MCU connected to co-processor via SPI/I2C bus, with labels identifying what each handles
**Instructor Script:**
> "Some ECUs — particularly complex powertrain ECUs and all ISO 26262-compliant safety ECUs — use a second processor alongside the main MCU.
>
> What co-processors handle:
> - **Communication offload:** Managing the CAN bus message stack so the main MCU is not interrupted by every incoming message
> - **Safety monitoring:** On functional safety ECUs (EPS, ABS, airbag), a second MCU independently verifies the main MCU's output commands. If the two disagree beyond a defined threshold, the system enters a safe state.
> - **Specialist analogue processing:** Some ECUs use an ASIC co-processor for knock sensor signal processing or injector timing at nanosecond precision — resolution the main MCU cannot achieve while also running the full control loop
>
> Diagnosis relevance: On a two-processor ECU, the inter-processor bus uses SPI or I2C. A failure of this bus causes specific, recognisable symptoms — the ECU powers up and responds on OBD, but some subsystems are dead while others work normally.
>
> Identifying a co-processor: Look for a second, smaller IC placed close to the main MCU with a data bus visible between them. It may be a smaller QFP, or an SOIC-16 or SOIC-20 package."

---

### PART 4: The Watchdog Circuit (Slides 20–22, ~12 minutes)

#### Slide 20: Why Does an ECU Need a Watchdog?
**Visual:** Two-panel diagram — Left: healthy firmware loop with arrows cycling continuously. Right: firmware hang with arrow stuck, engine outputs frozen
**Instructor Script:**
> "Here is a scenario: The ECU is running. The firmware is executing normally. A corrupted RAM value causes the program counter to jump into an undefined region of memory. The firmware is now executing garbage instructions. The injector outputs are frozen at whatever state they were in when the crash happened.
>
> In a consumer device — a phone, a laptop — a frozen processor is an annoyance. In a vehicle travelling at 100 km/h with the throttle open and fuel injection locked on, it is a safety emergency.
>
> The watchdog circuit is the engineering answer to this problem."

#### Slide 21: How the Watchdog Works
**Visual:** Timing diagram — WDT counter counting up, periodic reset pulses from firmware kicking the counter down, then a firmware hang — no more kicks — counter reaches maximum — RESET signal asserted
**Instructor Script:**
> "The watchdog is an independent timer circuit — either a dedicated external IC or a built-in peripheral inside the MCU itself. It works like this:
>
> 1. When the ECU starts, the watchdog timer begins counting up from zero
> 2. The firmware must 'kick' or 'stroke' the watchdog before the timer reaches its threshold — this is a specific write instruction that healthy software executes in its main loop
> 3. If the firmware is running correctly, it kicks the watchdog regularly. The timer resets before it expires. Nothing happens.
> 4. If the firmware hangs, it stops kicking. The timer counts to its limit.
> 5. When the timer expires, the watchdog asserts the RESET pin of the MCU
> 6. The MCU performs a hardware reset and restarts from the beginning of the firmware
>
> On a healthy ECU, this recovery takes less than 100 milliseconds. The engine may stumble briefly. On a failing ECU with repeated firmware crashes, the watchdog fires repeatedly — producing the characteristic symptom of an ECU that keeps resetting in a loop."

#### Slide 22: Watchdog Failure Modes
**Visual:** Two-column table comparing the two failure modes with their causes and symptoms
**Instructor Script:**
> "The watchdog itself can fail in two ways:
>
> **Failure Mode 1: Watchdog stuck asserted — continuously resets the MCU**
> - Cause: WDT IC failed with output held low; shorted trace on RESET line
> - Symptom: ECU powers on but immediately resets, repeatedly. On the oscilloscope, you see the supply voltage rise, then dip, then rise again in a regular cycle. OBD connection shows the ECU briefly appearing then disappearing.
> - Test: Measure the RESET pin of the MCU. If it is toggling or held low when it should be high, the watchdog IC or its supply line is the suspect.
>
> **Failure Mode 2: Watchdog not functioning — fails to reset a hung MCU**
> - Cause: WDT IC failed open, or watchdog disabled by a firmware bug
> - Symptom: ECU locks up and does not recover without a full battery disconnect. Particularly dangerous in safety-critical applications.
> - Test: The watchdog IC can be checked for correct supply voltage and correct output logic level during normal operation. Full verification requires inducing a controlled hang.
>
> Location on board: External watchdog ICs appear as small SOIC-8 or SOT packages near the MCU, with one output connected to the MCU's RESET pin. Common watchdog ICs in automotive ECUs: TPS3813, MAX6369, and similar supervisory IC families."

---

### CLOSING: Concept Check and Session Wrap (Slides 23–25, ~10 minutes)

#### Slide 23: Concept Check — Five Questions
**Visual:** Numbered list — instructor uses these for verbal Q&A with the class
**Instructor Script:**
> "Before we close, five quick questions that directly relate to tomorrow's hands-on session.

**Question 1:** On a 4-layer PCB, which layer is typically the solid ground plane?
*(Expected answer: Layer 2)*

**Question 2:** Near the main MCU you find a small silver rectangle with two leads, placed 3mm from the MCU's corner. What is it most likely to be?
*(Expected answer: Crystal resonator — the clock source for the MCU)*

**Question 3:** A technician replaces a polarised electrolytic capacitor but installs it with the polarity reversed. What happens when power is applied?
*(Expected answer: The capacitor will fail — likely short circuit — within seconds)*

**Question 4:** The ECU powers on but immediately resets in a continuous loop. The power supply is confirmed healthy. Which circuit is the first suspect?
*(Expected answer: The watchdog circuit or the RESET line)*

**Question 5:** What data is stored in EEPROM that is NOT stored in FLASH?
*(Expected answer: Learned adaptations, mileage data, immobilizer security codes — data that changes during normal ECU operation and must survive power removal)*"

#### Slide 24: Lab Preparation — Three Things to Avoid Tomorrow
**Visual:** Plain text warning list
**Instructor Script:**
> "Tomorrow you will handle real ECUs. Three common mistakes to avoid:
>
> **Mistake 1:** Touching ICs without an ESD wrist strap properly connected. You already know from Module 1 why this destroys semiconductor junctions silently and without any visible indication.
>
> **Mistake 2:** Probing test points with the probe tip slipping onto an adjacent component. On high-density ECU boards, pads are 0.5 to 1mm apart. A slip can bridge two nets. Keep probes vertical and use fine probe tips.
>
> **Mistake 3:** Confusing a ferrite bead (L designator, looks identical to a 0402 resistor) with a resistor. Tomorrow you will see these side-by-side. A ferrite bead measures near-zero ohms DC resistance; a real resistor measures its rated value. We will practice this distinction tomorrow."

#### Slide 25: Session Summary
**Visual:** Summary table — four topics, one key takeaway per topic
**Instructor Script:**
> "Let us summarise Day 4 Theory:
>
> - **PCB layers:** Signal traces on top and bottom, ground plane on Layer 2, power plane on Layer 3. Multilayer design is about EMC and routing, not just convenience.
> - **Reading the board:** Reference designators identify component type, test points give diagnostic access without probing live IC pins, silkscreen gives polarity and orientation guidance.
> - **Processor region:** MCU executes firmware, FLASH holds firmware, EEPROM holds adaptations and security data, RAM is working memory lost on power-down, crystal provides the clock.
> - **Watchdog:** An independent timer that resets the MCU if firmware hangs. Can fail in two directions: stuck asserted (continuous reset loop) or not functioning (ECU locks up permanently).
>
> Tomorrow, Session 04H: you receive a dismantled ECU and a blank PCB map. Your task is to identify and label every region and component category you have learned today."

---

## Instructor Notes

### Preparation Required
- Source at least two real automotive ECU PCBs with conformal coat removed for physical demonstration during the lecture. Point to actual components as you name each element.
- Have a crystal oscillator, a ferrite bead, and a standard resistor available to pass around during slides 18 and 24 — these three components look nearly identical visually and students need to handle them.
- If possible, have a non-functioning ECU powered on an isolated bench supply with an oscilloscope connected to the RESET pin, to demonstrate watchdog reset toggling live during slide 21.

### Anticipated Questions

**Q: How do you tell whether FLASH is internal or external on an unknown ECU?**
A: Count the ICs near the MCU. An external FLASH chip will be a separate SOIC-8 or TSOP package connected via 4 to 6 traces. If the MCU sits alone with no nearby small IC and a bus leading to it, FLASH is almost certainly internal. The MCU datasheet confirms this.

**Q: Can you replace a failed crystal with any crystal of the same frequency from a supplier?**
A: You must also match the load capacitance specification. An incorrect load capacitance causes the oscillator to run at the wrong frequency or fail to start. The crystal datasheet and the circuit's load capacitors — the two small capacitors placed at the XTAL pins — determine the required load capacitance.

**Q: Can EEPROM be read without a schematic?**
A: Yes. Identify the chip's part number from its markings, locate the datasheet to confirm pinout, then use an SPI clip or SOIC test socket on a dedicated programmer. Module 6 covers this procedure in full.

### Timing Adjustment
- If the class is strong on electronics fundamentals, compress Part 2 (Reading the Board) to 10 minutes and expand the watchdog section with a live oscilloscope demonstration.
- The co-processor slide (19) can be condensed to 2 minutes if time is short — it is contextual knowledge, assessed indirectly rather than directly in this module.

### Assessment Alignment
- Session 04H directly assesses so-3-1-2 (practical identification of test points and markings on a real ECU)
- The concept check at slide 23 informally assesses so-3-1-1, so-3-1-3, and so-3-1-4
- Formal assessment of so-3-1-3 and so-3-1-4 occurs in the Module 3 written assessment

---

## PPT Slide Summary

| Slide | Title | Time |
|-------|-------|------|
| 1 | Title — ECU PCB Architecture | 2 min |
| 2 | Connection to Module 2 | 2 min |
| 3 | The ECU as a System | 3 min |
| 4 | Today's Journey | 3 min |
| 5 | PCB Layer Structure | 5 min |
| 6 | Why Multilayer — Three Problems Solved | 4 min |
| 7 | The Ground Plane | 4 min |
| 8 | Vias — Signals Between Layers | 5 min |
| 9 | Reference Designators | 4 min |
| 10 | Silkscreen Markings | 4 min |
| 11 | Test Points | 4 min |
| 12 | Board Orientation and Region ID | 3 min |
| 13 | The Digital Core — Five Elements | 2 min |
| 14 | The MCU — The Brain | 5 min |
| 15 | EEPROM — The Calibration Store | 5 min |
| 16 | FLASH — The Firmware Store | 5 min |
| 17 | RAM — Working Memory | 3 min |
| 18 | Clock Oscillator — The Heartbeat | 5 min |
| 19 | Co-Processor — When One is Not Enough | 3 min |
| 20 | Why Does an ECU Need a Watchdog? | 3 min |
| 21 | How the Watchdog Works | 5 min |
| 22 | Watchdog Failure Modes | 4 min |
| 23 | Concept Check — Five Questions | 6 min |
| 24 | Lab Preparation Notes | 2 min |
| 25 | Session Summary | 2 min |
| **Total** | | **~90 min** |
