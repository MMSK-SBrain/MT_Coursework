# SESSION-09T — IC Testing, Datasheet Navigation & CAN Box Theory
## ECU Hardware Repair (ECUHR) | Module 4: PCB Repair & Soldering Skills
### Day 9 — Theory Block | Duration: 90 minutes

---

## Session Identity

| Field | Detail |
|---|---|
| Session Code | SESSION-09T |
| Module | 4 — PCB Repair & Soldering Skills |
| Day | 9 |
| Block | Theory |
| Duration | 90 minutes |
| Delivery Mode | Instructor-led, classroom/lab bench |
| Prerequisites | SESSION-08T and SESSION-08H complete; students can solder and use hot air |

---

## Learning Outcomes

By the end of this session, students will be able to:

- **so-4-3-1:** Decode IC package markings to identify manufacturer, part number, and date code; locate datasheets using manufacturer sites and lookup databases
- **so-4-3-2:** Navigate a datasheet to extract supply voltage, pin configuration, absolute maximum ratings, and electrical characteristics relevant to in-circuit testing
- **so-4-4-1:** Explain the schematic of the CAN box they will build in SESSION-09H — the function of each block: MCU, CAN transceiver IC, termination resistor, power regulator, connector

---

## Instructor Preparation

### Materials Required
- Physical IC samples: at least 3 different ICs from scrap ECU boards with readable markings — e.g., TJA1050T (NXP CAN transceiver), L7805 or similar voltage regulator, 74HC series logic gate, or automotive MOSFET driver
- Printed datasheets for the CAN box ICs (TJA1050 or SN65HVD230, MCU datasheet for the CAN box)
- CAN box schematic — printed, A3 size, one per student (or displayed full screen)
- CAN box PCB (unpopulated) — one per student for the afternoon session, also one to show during theory
- Component kit for CAN box — one sealed bag per student (delivered for the afternoon, but shown during theory)
- Laptop with internet access for live datasheet lookup demonstration
- PPT slide deck: MODULE4-09T-IC-Testing-Datasheet.pptx
- Whiteboard or flip chart for working through the datasheet analysis example
- Multimeter for in-circuit testing demonstration in Block 3

### Room Setup
- Laptop and screen connected for live internet demonstration in Block 2
- Physical IC samples on front bench in a labelled tray
- CAN box schematic poster or printed copies distributed at the start of Block 4
- Unpopulated CAN box PCB available to show during Block 4

---

## Session Story Arc

The first two days of Module 4 built the hands-on skill. Today's theory session bridges craft and engineering: students learn to identify components they encounter, find technical specifications for them, use those specifications to diagnose whether a component is faulty, and understand the circuit they are about to build. The afternoon lab session is the capstone of the module — students leave with a functioning device they built and tested.

---

## Block 1 — Reading IC Package Markings (20 minutes)

### Instructor Script — Opening

"You are at a bench with an ECU that has failed. You have identified a suspicious IC — maybe the supply voltage on its VCC pin reads 0V, or an output that should be switching is static. You need to know what that IC is. The part number is printed on the package body. Today you learn to read it."

**Slide 1:** Photograph of a CAN transceiver IC (TJA1050T) with the package markings visible. Labels pointing to each line of text.

---

### 1.1 Standard Package Marking Structure

**Script:**

"Most SMD IC packages use a three-line or four-line marking format.

Line 1: Manufacturer logo and/or part number. The part number is the most important piece of information. For the TJA1050T: 'TJA' is the NXP prefix for CAN transceiver products, '1050' is the device number, 'T' is the package variant — in this case SOT-23 surface mount.

Line 2: Date code and lot code. The date code is typically four digits — two for week, two for year. '2218' means week 22 of 2018. The lot code is a manufacturer's internal production batch identifier — not needed for repair purposes but relevant if you suspect a manufacturing defect batch.

Line 3: Country of manufacture. For your purposes, largely irrelevant — but confirms you are reading the marking correctly.

Some ICs add a line 4 for internal revision or test code. Ignore this unless investigating a specific revision-dependent fault.

The challenge: on very small packages — SOT-23, SC-70, or tiny QFN parts — the full part number does not fit. A shortened code is used. For example, an NXP TJA1050T in SOT-23 may be marked only 'A1' or a three-character internal code. This requires a lookup."

**Slide 2:** Annotated IC marking diagram — three-line structure, each line labelled: Part number / Date code + Lot code / Country. Example uses TJA1050T.

---

### 1.2 Short Marking Lookup

**Script:**

"When a short code is all you have, you need a lookup resource. Three reliable options:

One — The manufacturer's marking guide. NXP, Texas Instruments, Infineon, and most major manufacturers publish a marking lookup PDF or database on their website. Search '[manufacturer name] package marking guide' — it is usually the first result.

Two — Octopart.com or Mouser — search the short code plus the package type and pin count. These sites often have the decoded part number.

Three — IC decoder websites — smd.yooneed.one and similar. Enter the marking code, select the package type, and the site returns probable matches. These are crowdsourced and are not 100 percent reliable — always confirm the result against the manufacturer's own documentation before ordering a replacement.

Live demonstration: I'm going to look up a real short marking code now."

**Live internet demo:** Show the lookup process for a real IC from the physical sample tray. Use the manufacturer's marking guide or a lookup database. Take the students through the result.

**Slide 3:** Screenshot of a successful lookup result with the part number, manufacturer, and datasheet link highlighted.

---

### 1.3 What to Do When the Marking Is Illegible

**Script:**

"ECU boards that have been overheated, exposed to coolant, or poorly handled sometimes have IC markings that are partially or fully illegible. Options:

One — Schematic or service manual. If you have the ECU schematic, cross-reference the IC position on the board with the schematic reference designator. The schematic will name the IC.

Two — Circuit function analysis. What does the IC do in circuit? Count pins, identify package type, trace the power supply pin and ground pin. From these you can narrow the IC function and probable manufacturer. This is advanced work — we will cover it later in the course.

Three — Professional decoders. Companies specialising in ECU repair maintain private databases of IC positions per ECU part number. If you are in a specialist shop or networked with one, this is a fast route.

The rule: do not replace an IC whose identity you cannot confirm. Guessing the IC and installing the wrong part can damage the board or adjacent components on power-up."

---

## Block 2 — Datasheet Navigation (25 minutes)

### Instructor Script — Opening

"You have identified the IC. You now have a part number. The next step is the datasheet. A datasheet is the manufacturer's complete technical specification for the component. For ECU repair, you need four sections: features, pin configuration, absolute maximum ratings, and electrical characteristics."

**Slide 4:** Title — "Navigating a Datasheet for In-Circuit Diagnosis"

**Distribute** printed TJA1050 datasheet (or display on projector) — this is the IC the students will assemble in the afternoon, so the datasheet is immediately relevant.

---

### 2.1 Features Section

**Script:**

"The features section is typically the first paragraph of the datasheet. It tells you in plain language what the IC does. For the TJA1050: 'High-speed CAN transceiver, compatible with ISO 11898, 1Mbps maximum data rate, 5V supply.'

From this alone you know: it is a CAN transceiver, it operates on 5V, and it operates at up to 1Mbps. If you are testing an ECU where the CAN bus is operating at 500kbps, this IC is in range.

If the features say '3.3V supply' and you are measuring 5V at the VCC pin, you already have an answer — someone installed the wrong IC, or the power supply rail is wrong."

---

### 2.2 Pin Configuration and Description

**Script:**

"The pin configuration diagram shows you which pin number is which function. For diagnosis you need this to know where to probe.

For the TJA1050 in SO-8 package:

Pin 1 — TXD: transmit data input from the MCU
Pin 2 — GND: ground
Pin 3 — VCC: supply voltage (4.5–5.5V)
Pin 4 — RXD: receive data output to the MCU
Pin 5 — Vref: optional reference voltage output (0.5 × VCC)
Pin 6 — CANL: CAN bus low
Pin 7 — CANH: CAN bus high
Pin 8 — S: standby mode pin

You cannot probe 'the CAN bus pins' without knowing that pin 6 is CANL and pin 7 is CANH. You cannot confirm the IC is powered without knowing pin 3 is VCC. Without the pin configuration, a multimeter on a board is guesswork."

**Slide 5:** TJA1050 pin configuration diagram — SO-8 footprint with pin numbers and function labels. Annotated for: power pins (VCC, GND), bus pins (CANH, CANL), signal pins (TXD, RXD).

---

### 2.3 Absolute Maximum Ratings

**Script:**

"This section defines the limits beyond which the IC will be permanently damaged. These are not operating parameters — they are destruction thresholds.

For the TJA1050: VCC absolute maximum is 7V. Operating voltage is 4.5 to 5.5V. If VCC reaches 7V even briefly — from a surge, a wiring fault, or incorrect power supply — the IC is damaged.

Input voltage on TXD and RXD pins: absolute maximum is VCC + 0.5V. If the MCU outputs 5V logic to a TJA1050 running on 5V, the input pin sees exactly its maximum. This is a common design tension in ECUs.

Bus pins CANH and CANL: rated to ±58V for short durations. This is the fault protection spec — the transceiver is designed to survive short circuits to vehicle battery voltage.

Why does this matter for repair? If you are testing an IC and you find VCC is 6V — above the operating range but below absolute maximum — the IC may still be functioning but is running outside specification and will have reduced lifespan. The power supply rail needs investigation, not just the IC."

**Slide 6:** Absolute maximum ratings table from TJA1050 datasheet — annotated to highlight VCC max, input pin max, and bus pin max. Cross-reference with typical operating values.

---

### 2.4 Electrical Characteristics and Application Circuit

**Script:**

"The electrical characteristics table gives you the typical, minimum, and maximum values for operating parameters. This is where you find what to expect at each pin when the IC is healthy.

For diagnosis, the three most useful entries:

Supply current (ICC): the typical current drawn from VCC at idle. If you can measure supply current on the rail, a value far above typical suggests a shorted IC.

Output high and low voltage on RXD: the voltage levels the IC outputs to the MCU. If RXD should read 5V in recessive state but reads 0.3V, the output stage is damaged or the output is being pulled low by something else in circuit.

CANH and CANL voltages in recessive state: both should be approximately 2.5V (midpoint of the 5V supply). This is the first test you will perform on the CAN box in the afternoon.

The application circuit — usually near the end of the datasheet — shows the recommended external components: the decoupling capacitor on VCC, the pull-up resistor on the S pin (standby pin held high = standby mode, held low or connected to ground = normal operation), and the 120Ω termination resistor on the bus.

If you see the application circuit and compare it to the ECU board you are repairing, you can identify missing components — a decoupling capacitor that has fallen off, a missing pull-up resistor that is holding the IC in standby."

**Slide 7:** TJA1050 application circuit schematic — annotated with: decoupling cap on VCC, standby pin connection, CANH/CANL lines, 120Ω termination, MCU connections.

---

### 2.5 In-Circuit Testing Methodology

**Script:**

"Combine the pin configuration and electrical characteristics to build a logical test sequence. The sequence is always the same, regardless of which IC you are testing:

Step 1 — Power off. Check the resistance from VCC pin to ground. It should not be zero (which would indicate a dead short) and should not be open circuit (which might indicate the rail is disconnected or a trace is open). Typical resistance will reflect the combined impedance of everything connected to the rail.

Step 2 — Power on. Measure VCC pin to GND. Compare to datasheet Vcc operating range.

Step 3 — Measure outputs at idle. With no signal being sent, measure output pins and compare to datasheet idle state values.

Step 4 — Measure inputs. Verify signals are arriving at the IC input pins. Use an oscilloscope if the signal is a high-speed digital signal; a multimeter for static levels.

Step 5 — Inference. If supply is within range, inputs are present and correct, and output is incorrect — the IC is the likely fault. If supply is out of range, investigate the supply rail before replacing the IC. If inputs are absent — the fault is upstream of this IC.

The key discipline: do not replace the IC until you have confirmed the supply is correct. A new IC installed on a faulty supply rail will fail immediately. The supply problem remains — and now you have also consumed a replacement IC."

**Slide 8:** In-circuit testing flowchart — Power OFF → Resistance check → Power ON → VCC level → Output levels → Input levels → Inference table.

---

## Block 3 — CAN Box Schematic Walkthrough (20 minutes)

### Instructor Script — Opening

"This afternoon you will build a CAN box from a kit. Before you build anything, you need to understand what you are building and why. A builder who understands the schematic can troubleshoot their own assembly. A builder who does not understand the schematic has to guess."

**Distribute** printed CAN box schematic. Display on projector simultaneously.

**Slide 9:** Full CAN box schematic — complete, with all blocks visible. Do not annotate yet.

"I want you to look at this schematic for 30 seconds before I say anything. What blocks can you already identify?"

Allow 30 seconds. Take answers from students — they should be able to identify the MCU, the CAN transceiver, and the connector from their existing knowledge.

---

### 3.1 Block by Block — CAN Box Schematic

**Script:**

"Let's go through this block by block."

**Power Supply Block:**

"Top left. We have 12V entering from the vehicle connection — the OBD-II connector or the direct ECU harness connector. This feeds a 7805-type linear voltage regulator. Input: 12V. Output: 5V regulated. The 0.1µF and 10µF capacitors on the input and output are decoupling and stabilisation caps — the datasheet for the 7805 requires both. The 5V rail powers both the MCU and the CAN transceiver."

Annotate on schematic: circle the regulator block.

**Slide 10:** Power supply block schematic — isolated and enlarged. Labels: 12V input, regulator IC, filter capacitors, 5V output.

**MCU Block:**

"The microcontroller. In this kit we are using a PIC18F2580 in a DIP package — through-hole, which makes assembly easier for a first build. The MCU receives power on VCC and GND pins. It has a crystal oscillator for clock timing. It has CAN protocol logic built in — it generates and receives CAN frames internally. It communicates with the CAN transceiver on two pins: CANTX and CANRX.

The MCU also has a UART connection to the USB interface — this allows a PC to send commands and receive CAN frames from the box."

Annotate on schematic: circle MCU, label CANTX and CANRX pins, label USB interface connection.

**Slide 11:** MCU block schematic — isolated. Labels: power pins, crystal oscillator, CANTX/CANRX, USB/UART interface.

**CAN Transceiver Block:**

"The CAN transceiver — TJA1050 in SO-8 package. This is the IC whose datasheet you just read. It converts the single-ended logic signals from the MCU — CANTX and CANRX, which are standard 0V/5V digital signals — into the differential CAN bus signals, CANH and CANL.

CAN bus is differential: CANH and CANL move in opposite directions. In recessive state: both at 2.5V. In dominant state: CANH rises to approximately 3.5V, CANL falls to approximately 1.5V. The differential voltage is what carries the data. This differential architecture is why CAN bus is highly noise-immune — interference affects both lines equally and is cancelled by the receiver.

The VCC decoupling capacitor on the TJA1050 is on the schematic — 100nF between VCC and GND, physically close to the IC pin. This is mandatory — without it, the IC can produce glitches during switching transients.

The S pin — standby mode — is connected to ground via a resistor to keep the IC in normal operating mode. If you leave S floating, the IC may enter standby."

Annotate on schematic: CANTX from MCU to TXD on TJA1050, CANRX from RXD on TJA1050 to MCU, CANH and CANL to connector.

**Slide 12:** CAN transceiver block schematic — isolated. Labels: TXD, RXD, CANH, CANL, VCC decoupling cap, S pin pull-down.

**Termination Resistor:**

"The 120Ω resistor between CANH and CANL. CAN bus is a transmission line. For correct signal integrity on a real vehicle network, both ends of the CAN bus must be terminated with 120Ω. The termination resistor absorbs signal reflections that would otherwise corrupt data.

In this CAN box, the termination is built in — when you connect to a vehicle network, the box adds one termination point. The other end of the vehicle's CAN network is typically terminated inside the ECU or the gateway module.

120Ω is the value — memorise it. If you measure the resistance across CANH and CANL on a healthy, powered-down CAN network, you should read 60Ω — two 120Ω resistors in parallel, one at each end of the bus."

Annotate on schematic: circle the 120Ω termination resistor.

**Slide 13:** Termination block diagram — CAN bus line with two endpoints, each showing 120Ω termination, total measured resistance 60Ω.

**Connector Block:**

"The OBD-II or DB9 connector. This is the physical interface to the vehicle or test equipment. The CAN box can be connected to a vehicle OBD-II port, a bench CAN simulator, or another CAN-enabled device.

On the OBD-II connector: pin 6 is CANH, pin 14 is CANL. On a DB9 connector as used in some test equipment standards: pin 2 is CANL, pin 7 is CANH. If you build the kit with the wrong pin assignment on the connector, the bus will not communicate. The schematic is the authoritative reference — follow it exactly."

**Slide 14:** Connector pinout comparison — OBD-II and DB9. CANH and CANL highlighted on each.

---

### 3.2 Build Sequence — Why Order Matters

**Script:**

"One more thing before you go to the bench: the build sequence. You will solder in this order, and it matters.

First: passive components — resistors and capacitors. They are the smallest and sit flattest against the board. If you solder connectors first, the board tilts and passive component placement becomes awkward.

Second: the voltage regulator IC.

Third: the CAN transceiver IC — TJA1050 in SO-8. You know how to solder this.

Fourth: the MCU — PIC18F2580 in DIP package. Through-hole, easier to place, but its larger footprint means it must go on after the SO-8.

Fifth: the USB interface connector or Bluetooth module if included.

Sixth: connectors last — OBD-II or DB9. Connectors are mechanically robust and hold the board still during all earlier stages. Once connectors are soldered, the board is difficult to hold flat in a vice."

**Slide 15:** CAN box build order — numbered component groups on the schematic: 1 passives, 2 regulator, 3 transceiver, 4 MCU, 5 interface connector, 6 OBD/DB9 connector.

---

## Block 4 — Testing the Completed CAN Box (10 minutes)

### Instructor Script

"When you finish building and before you connect to any vehicle, you test the box on the bench with a multimeter. Three tests.

Test 1: VCC rail. Apply power. Measure the output of the regulator — the 5V rail. Should read 4.75V to 5.25V. If you read 0V, the regulator is not working or there is no input power. If you read 12V, the regulator has failed open — do not connect to CAN transceiver.

Test 2: CANH and CANL at rest. Both should read approximately 2.5V with respect to GND. This confirms the transceiver is powered and in recessive (idle) state. If one or both read 0V, the transceiver is not powered or is in standby.

Test 3: Communication test. Connect to a vehicle OBD-II port or a bench CAN bus simulator. Send a request message from the PC software. Confirm that the software receives a frame in response — either from the vehicle or echoed from the simulator.

If Tests 1 and 2 pass but Test 3 fails, the fault is either in the MCU firmware, the USB connection, or the connector pinout. Work through methodically — do not assume the IC is faulty."

**Slide 16:** CAN box test sequence — three tests with expected values and failure interpretations.

---

## Block 5 — Q&A and Session Close (5 minutes)

### Instructor Script

"This afternoon you will build the device whose schematic you now understand. You have the datasheet for the main IC. You know the build sequence and the test sequence.

Two things I want you to remember from today:

One — A datasheet tells you exactly what to measure. If you do not have the datasheet open before you start testing an unknown IC, you are guessing. The datasheet is not optional documentation — it is your test specification.

Two — The CAN box you build today is a diagnostic tool you can use on real vehicles. It is not a training exercise — it is a functional device. Build it as if it matters, because it does."

**Q&A:** Allow 5 minutes for questions. Likely questions:
- "What firmware does the MCU run?" — Confirm whether firmware is pre-loaded on the MCU in the kit, or whether students will flash it before testing.
- "Can the CAN box damage a vehicle if connected incorrectly?" — Yes, if polarity is reversed or if the voltage regulator fails with full 12V on the 5V rail. The build sequence and testing steps prevent this.

---

## Slide Deck Summary — SESSION-09T

| Slide | Title | Content Type |
|---|---|---|
| 1 | IC Package Marking Photograph | Annotated photograph |
| 2 | Package Marking Structure Diagram | Annotated diagram |
| 3 | Short Marking Lookup — Live Demo Screenshot | Screenshot |
| 4 | Navigating a Datasheet for Diagnosis | Title slide |
| 5 | TJA1050 Pin Configuration | Datasheet diagram + annotations |
| 6 | Absolute Maximum Ratings Table | Datasheet table + annotations |
| 7 | TJA1050 Application Circuit | Schematic + annotations |
| 8 | In-Circuit Testing Flowchart | Decision flowchart |
| 9 | CAN Box Full Schematic | Schematic — full |
| 10 | Power Supply Block | Schematic block — isolated |
| 11 | MCU Block | Schematic block — isolated |
| 12 | CAN Transceiver Block | Schematic block — isolated |
| 13 | Termination Resistor Diagram | Schematic + bus line diagram |
| 14 | Connector Pinout Comparison | OBD-II and DB9 pinout reference |
| 15 | Build Order | Numbered schematic overlay |
| 16 | CAN Box Test Sequence | Test procedure with expected values |

---

## Assessment — SESSION-09T

No formal assessment this session. Understanding of the CAN box schematic is assessed implicitly during SESSION-09H: students who understood the theory will troubleshoot more effectively and will correctly interpret their multimeter readings during the testing phase.

Instructor note: if any student cannot identify the VCC pin and the CANH/CANL pins on the TJA1050 schematic by the end of Block 3, provide individual clarification before the lab session. These are the two mandatory measurements in SESSION-09H.

---

## Instructor Notes

- The datasheet navigation block (Block 2) can feel abstract if the datasheet being used is for a generic example IC. Using the TJA1050 — which students will assemble in the afternoon — makes the datasheet immediately concrete and relevant. Do not switch to a different IC for the datasheet example.
- The in-circuit testing methodology in Block 2.5 is a skill that transfers beyond Module 4 to every subsequent practical session in the course. Emphasise it as a general framework, not a TJA1050-specific procedure.
- Block 3 schematic walkthrough should be interactive — ask students to identify blocks before explaining them. Students who have seen ECU schematics before can often contribute, which builds engagement.
- The firmware question (Block 5 Q&A) should be answered clearly before the lab session. If firmware is pre-loaded: say so and explain what the firmware does in plain language. If students will flash firmware: ensure the flashing procedure is documented in SESSION-09H.
- Time management: Blocks 1 and 2 are content-dense. If running behind after Block 2, the Q&A in Block 5 can be reduced to 2 minutes and the Build Sequence (Block 3.2) delivered as a briefer verbal rundown from the slide rather than a full scripted explanation.
