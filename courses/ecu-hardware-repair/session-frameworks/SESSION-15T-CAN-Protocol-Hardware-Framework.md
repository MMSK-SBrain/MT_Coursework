# SESSION-15T — CAN Protocol & Hardware
## Day 15 Theory | Module 7: CAN Bus, LIN & Communication Diagnostics

---

**Course:** ECU Hardware Repair (ECUHR)
**Session Code:** SESSION-15T
**Day:** 15 of 20
**Type:** Theory — Lecture with waveform analysis and worked examples
**Duration:** 90 minutes
**Delivery:** Instructor-led, slide-supported, whiteboard annotation

**Session Outcomes:**
- so-7-1-1: Describe CAN bus differential signaling (CANH/CANL), dominant/recessive states, and why it provides noise immunity
- so-7-1-2: Identify the fields of a CAN data frame and explain each field's role
- so-7-1-3: Explain CAN bus arbitration and how message priority is determined by ID
- so-7-1-4: Explain CAN error states (error active, error passive, bus-off) and the error counter mechanism

**MO Alignment:** MO 7-1
**CO Alignment:** co-1 (Diagnose ECU faults by applying knowledge of automotive-grade circuit design)

**Prerequisites (student must have completed):**
- Module 2: Oscilloscope operation and signal capture
- Module 3: EMI/EMC filtering, common-mode chokes (so-3-3-4)
- Module 4, Lesson 4.7: CAN Box Construction — students built a CAN transceiver circuit and know what the hardware looks like

---

## Session Overview

| Block | Time | Topic | Format |
|-------|------|-------|--------|
| Hook | 0–8 min | Opening scenario: why did the car suddenly have 15 fault codes? | Discussion |
| Block 1 | 8–28 min | Physical layer — differential signaling, voltage levels, termination | Lecture + whiteboard |
| Block 2 | 28–50 min | CAN frame structure — field by field | Lecture + slide annotation |
| Block 3 | 50–70 min | Arbitration — how nodes decide who transmits | Lecture + worked example |
| Block 4 | 70–85 min | Error states — error active, passive, bus-off | Lecture + fault pattern discussion |
| Close | 85–90 min | Summary, preview of hands-on lab | Discussion |

---

## OPENING HOOK (0–8 minutes)

### The Scenario — Read this to the class, verbatim or in your own words:

"A customer drives in. Their car has just had an ABS module replaced at another workshop. When they picked it up, the dashboard was showing warning lights they didn't have before. The other technician scanned the car and found 15 fault codes across 6 different control units — the engine ECU, the instrument cluster, the BCM, the transmission control unit, the parking sensor module, and the new ABS unit itself.

The technician told the customer they needed to replace 5 more modules. The bill was going to be several thousand dollars.

The customer drove out, came to you instead, and asked you to have a look.

You plug in your scan tool. You see the same 15 codes. But before you start pricing up modules, you ask yourself: what could cause 6 different unrelated modules to all fail at the same time?

Take 30 seconds — turn to your neighbour and tell them what your first suspect would be."

**Pause for 60 seconds of discussion.**

**Then say:** "The answer is: nothing failed simultaneously. One thing failed — the CAN bus network. When one node on the network either dies or starts misbehaving, the rest of the network sets communication fault codes. It looks like mass failure. It is one fault. The technician who was going to replace 5 modules would have replaced 5 modules that were completely fine.

This session teaches you how CAN actually works — so that when you see 15 codes, you know immediately where to start, and where NOT to start."

---

## BLOCK 1 — Physical Layer: Differential Signaling, Voltage Levels, Termination (20 minutes)

### Slide 2: "Why Two Wires for One Signal?"

**Script:**
"Every CAN bus uses a twisted pair — two wires called CANH (CAN High) and CANL (CAN Low). Vehicles have kilometres of wiring, all of it in an environment full of electromagnetic interference — alternators, ignition coils, electric motors, fuel injectors switching on and off. If we ran a single signal wire, all that noise would couple directly into the signal.

CAN uses differential signaling to beat this problem. The message is not the voltage on either wire. The message is the *difference* between the two wires.

Write this down:"

**Whiteboard — draw and label:**

```
RECESSIVE STATE (Logic 1 — idle / no one driving):
  CANH = 2.5 V
  CANL = 2.5 V
  Difference = 0 V  →  Logic 1

DOMINANT STATE (Logic 0 — one or more nodes driving):
  CANH = 3.5 V
  CANL = 1.5 V
  Difference = 2 V  →  Logic 0
```

**Explain:** "When EMI noise hits both wires — and because they are twisted together it hits both simultaneously and equally — it raises CANH by, say, 0.5 V AND raises CANL by 0.5 V. The difference is still 2 V or still 0 V. The noise cancels out. This is why CAN is reliable in the automotive environment."

**Check question (ask the class):** "If CANH = 4.0 V and CANL = 2.0 V, what does the CAN controller see?"
Answer: Difference = 2 V — dominant bit, logic 0. The controller does not care about absolute voltages, only the difference.

---

### Slide 3: "Dominant and Recessive — The Key Concept for Fault Diagnosis"

**Script:**
"The words dominant and recessive are critical and must be solid in your mind before we discuss faults.

Dominant is like someone shouting. Recessive is like a whisper. If one person shouts and twenty people whisper — the shouter wins. Any node on the bus can pull the bus dominant by driving CANH high and CANL low. The recessive state only exists when *nobody* is actively driving the bus — it floats to 2.5 V through the termination resistors.

This means: one node with a fault that permanently drives the bus dominant can silence every other node on the network. Completely. All communication stops. This is one of the most common and most misdiagnosed CAN faults."

---

### Slide 4: "Termination Resistors — Why They Exist and What Goes Wrong"

**Script:**
"At each physical end of the CAN bus, there is a 120 Ω resistor connected between CANH and CANL. There are always exactly two — one at each physical end of the network.

Two reasons they are there. First: at 500 kbps, signals travel down the wire quickly, and if there is nothing at the end to absorb the signal energy, the wave reflects back up the wire. Those reflections corrupt data. The termination resistor absorbs the signal. Second: the two resistors define the recessive bus voltage — they form the path that pulls the idle bus to 2.5 V.

Two resistors of 120 Ω in parallel = 60 Ω. If you disconnect the bus from everything and measure resistance from CANH to CANL at any point on the bus, you should read approximately 60 Ω."

**Whiteboard — draw the termination fault table:**

```
Configuration                             Measured Ω    Result
─────────────────────────────────────────────────────────────────────
Both terminators present (correct)        ~60 Ω         Correct
One terminator missing                    ~120 Ω        Works but reduced noise margin;
                                                        intermittent faults more likely
Extra terminator added (3 total)          ~40 Ω         Too low — bus may not reach
                                                        dominant threshold reliably
No terminators at all                     Very high     Severe reflections; likely no
                                                        reliable communication
CANH-CANL shorted                         ~0 Ω          Bus stuck recessive; no comms
```

**Critical measurement note — say this clearly:**
"When measuring termination resistance, ignition must be off and at least two ECUs must be disconnected from the bus first. Otherwise you are measuring the termination resistors in parallel with internal resistances inside the ECUs, which gives a misleadingly low reading.

Also: some ECUs have an internal 120 Ω pull between CANH and CANL in their transceiver ICs. If one terminator is physically missing but one of those ECUs has that internal pull, you might still read near 60 Ω. Context and a topology diagram matter."

---

## BLOCK 2 — CAN Frame Structure (22 minutes)

### Slide 5: "What Does a CAN Frame Look Like?"

**Script:**
"A CAN frame is the packet of data that travels on the network. Every single message on a CAN bus is a frame. Let me show you each part."

**Draw on whiteboard — left to right across the full width:**

```
| SOF | ARBITRATION FIELD  | CONTROL  |  DATA FIELD  |  CRC FIELD   | ACK | EOF |
|  1b |  11-bit ID  | RTR  | IDE | DLC |   0–8 bytes  | 15-bit + del | 1+1 |  7b |
```

Walk through each field:

---

**SOF — Start of Frame (1 bit, always dominant)**

"One single dominant bit. Every node on the bus runs its own clock oscillator, and over time those clocks drift slightly out of phase with each other. The leading edge of the SOF bit is used by every other node to resynchronise its internal clock. One bit — one critical job. If SOF is corrupted, the entire frame is lost."

---

**Arbitration Field — Message ID (11 bits standard / 29 bits extended) + RTR bit**

"The message ID is not a destination address. There is no 'send this to ECU at address 5' instruction in CAN. The ID identifies what the *message contains* — for example, engine speed, or coolant temperature reading. Any node that wants that data listens for that ID. Multiple nodes can consume the same message simultaneously.

The ID also determines priority — we will cover this in Block 3.

The RTR bit is the Remote Transmission Request bit. A node can send a frame with RTR = 1 to ask the node that produces that message ID to transmit its data. Rarely seen in modern automotive CAN but it exists."

---

**Control Field — IDE + DLC (4 bits)**

"IDE is the Identifier Extension bit — it distinguishes standard 11-bit frames from extended 29-bit frames. DLC is the Data Length Code — a 4-bit number telling receivers how many data bytes follow. Range is 0 to 8. DLC = 0 means the frame carries no data — used as a heartbeat or event trigger signal."

---

**Data Field — 0 to 8 bytes**

"The actual payload. Engine speed might use 2 bytes. A status flag might use 1 byte. The format — which bits in the data field mean what — is defined in the vehicle manufacturer's DBC file, a database file. Without the DBC, a raw CAN frame is a sequence of numbers with no meaning. This is why factory scan tools can show you live data that generic scan tools cannot: they have the DBC and can decode the payload."

---

**CRC Field — 15-bit CRC + delimiter**

"Cyclic Redundancy Check. The transmitting node calculates a checksum over all the bits in the frame. Every receiving node independently recalculates the same checksum. If the receiver's result does not match the CRC field in the frame, the data was corrupted in transit — the receiver sends an error flag. This is the primary error detection mechanism.

On the oscilloscope, you cannot easily identify the CRC field by eye — but a high rate of CRC errors will show up as error frames following each data frame, and on the scan tool as CRC error codes."

---

**ACK Field — ACK Slot + ACK Delimiter**

"This is elegant. The transmitting node sends the ACK slot bit as recessive — then it listens. If *any* other node on the bus received the frame correctly, that node pulls the ACK slot dominant. The transmitter reads back dominant and knows: 'at least one node acknowledged this, the message was received correctly.'

If no node pulls the ACK slot dominant, the transmitter reads back its own recessive bit. Nobody acknowledged. The transmitter's error counter increments. If this continues, the node eventually goes bus-off. This is how a node ends up bus-off when the physical bus is fine but all other nodes are already off the network."

---

**EOF — End of Frame (7 recessive bits)**

"Seven consecutive recessive bits mark the end of the frame. Bit stuffing rules mean 6 consecutive identical bits normally trigger a stuff error — so 7 recessive bits in EOF cannot appear anywhere inside a valid frame. All nodes use the EOF to know the bus is free for the next transmission."

---

**Check question:** "The scan tool shows CRC error codes from multiple modules. The oscilloscope shows clean voltage levels on CANH and CANL. Where do you start looking?"
Answer: Termination — reflections from missing or wrong termination can corrupt bits without disturbing the gross voltage levels. Also consider a partially damaged transceiver IC producing slightly malformed bits.

---

### Slide 6: "The Oscilloscope View of a Healthy CAN Frame"

**Describe the waveform — students draw this in their notes:**

"Set Channel A to CANH, Channel B to CANL. Trigger on Channel A, falling edge, at about 2.0 V. Timebase: start at 100 µs/div for 500 kbps — each bit period is 2 µs. You may need to zoom in.

A healthy frame looks like this:

Before the frame: both CANH and CANL sit at 2.5 V — recessive idle. Flat lines, both channels at the same level.

Frame begins: SOF bit — CANH rises to approximately 3.5 V, CANL drops to approximately 1.5 V. The first dominant bit.

Through the frame: the two lines move in opposite directions for dominant bits (CANH up, CANL down) and return to 2.5 V together for recessive bits. The waveform looks like two opposing square waves, one above and one below 2.5 V.

On the math channel with CANH minus CANL: a clean digital square wave alternating between 0 V (recessive) and +2 V (dominant). No ringing on the leading edges. No noise above 2 V or below 0 V. Transitions are sharp.

After the frame: EOF brings both lines back to 2.5 V and they stay there until the next frame begins."

---

## BLOCK 3 — Arbitration (20 minutes)

### Slide 7: "How Does the Network Avoid Collisions?"

**Script:**
"CAN uses a protocol defined as CSMA/CD with NDA — Carrier Sense Multiple Access with Collision Detection, using Non-Destructive Arbitration. The critical difference from Ethernet is the word non-destructive.

In Ethernet, when two computers transmit simultaneously there is a collision — both messages are destroyed and both nodes back off for a random time before retrying.

CAN is smarter. When two nodes transmit simultaneously, one of them wins and its complete message is delivered without a single bit being lost."

**Whiteboard example — draw this step by step, slowly:**

"Imagine three nodes want to transmit at the same moment. They all wait until the bus is idle (recessive), then they all start transmitting their frame's ID field simultaneously, bit by bit, MSB first.

```
Node A:  ID = 0x032  binary: 0 0 0 1 1 0 0 1 0
Node B:  ID = 0x019  binary: 0 0 0 0 1 1 0 0 1
Node C:  ID = 0x016  binary: 0 0 0 0 1 0 1 1 0
```

While transmitting, each node also reads back what is on the bus. Remember: dominant overrides recessive. If any node drives dominant, the bus is dominant.

Bit 1: All three send 0 (dominant). Bus reads dominant. All three match — continue.
Bit 2: All three send 0 (dominant). Bus reads dominant. All three match — continue.
Bit 3: All three send 0 (dominant). Bus reads dominant. All three match — continue.
Bit 4: Node A sends 1 (recessive). Nodes B and C send 0 (dominant). Bus reads dominant.
  Node A reads back dominant but transmitted recessive — mismatch. Node A backs off immediately. Node A's message is not lost — it will retry after the current transmission completes.

Continuing between B and C:
Bit 5: Both B and C send 1 (recessive). Bus reads recessive. Both match — continue.
Bit 6: Node B sends 1 (recessive). Node C sends 0 (dominant). Bus reads dominant.
  Node B backs off. Node C wins.

Node C transmits its complete frame uninterrupted. No corruption. No data loss."

**Key conclusions — write these on the board:**
1. The winner is always the node with the lowest ID number.
2. A lower ID has more leading zeros in binary — more leading dominant bits — the node stays on the bus longer before being overridden.
3. Priority is designed in at system development time. Safety-critical messages get the lowest IDs.
4. Losing nodes do not lose their data — they queue and retry. This is transparent to the application.

**Real-world implication:** "A faulty node that continuously tries to transmit a very low ID message can monopolise the bus and starve other nodes. This is unusual but can happen. You would see it as: all other nodes reporting communication errors, the bus busy constantly with one message pattern, and the offending node not responding to anything else."

---

## BLOCK 4 — Error States (15 minutes)

### Slide 8: "Error Counters and Error States — The Mechanism Behind Bus-Off"

**Script:**
"Every CAN controller IC has two hardware counters — the Transmit Error Counter (TEC) and the Receive Error Counter (REC). These count upward when errors are detected and count downward when transmissions complete cleanly."

**Whiteboard — draw the state machine:**

```
Power-on
    │
    ▼
┌─────────────────────┐
│     ERROR ACTIVE    │  ← Normal operating state. TEC < 128.
│                     │    Sends Active Error Frame on error
│  TEC increments on  │    (6 dominant bits — forces all nodes to notice)
│  transmit error     │
│  TEC decrements on  │
│  clean transmission │
└─────────────────────┘
         │
         │ TEC reaches 128
         ▼
┌─────────────────────┐
│    ERROR PASSIVE    │  ← Still transmitting. TEC 128–255.
│                     │    Sends Passive Error Frame instead
│                     │    (6 recessive bits — much less disruptive)
│                     │    Node is effectively quarantined but alive.
└─────────────────────┘
         │
         │ TEC reaches 256
         ▼
┌─────────────────────┐
│      BUS-OFF        │  ← CAN controller disconnects from bus.
│                     │    Will not transmit. Will not receive.
│                     │    Scan tool: "ECU not responding."
│                     │    ECU still has power and ground.
└─────────────────────┘
         │
         │ Recovery: 128 × 11 consecutive recessive bits observed
         │ (usually requires power cycle or scan tool recovery command)
         ▼
    ERROR ACTIVE (reset)
```

**Explain each state carefully:**

**Error Active** is normal. The node participates fully. When it detects any error, it asserts an Active Error Frame — 6 consecutive dominant bits. This violates the bit-stuffing rule (which says a complementary bit must be inserted after 5 identical bits), so all other nodes immediately recognise a frame error has occurred and discard the current frame. TEC goes up by 8 for each transmit error, down by 1 for each clean frame.

**Error Passive** means TEC has reached 128. The node has been making a lot of errors. It can still transmit and receive, but instead of an Active Error Frame it sends a Passive Error Frame — 6 recessive bits. These are far less visible on the bus; other nodes may not notice the node is in trouble. The node is operating in a degraded, quarantined state.

**Bus-Off** means TEC reached 256. The node's CAN controller has disconnected itself from the bus entirely. It will not drive CANH or CANL. It will not respond to any messages. From the scan tool's perspective, the ECU does not exist.

**Say this slowly and emphasise it:**
"A bus-off ECU still has power. It still has ground. Its processor may still be running. Only its CAN controller is offline. If you go to that ECU and probe its power supply pins, you will find battery voltage. You might even find the processor is still active. The ECU is not dead — its CAN interface shut down because it encountered too many errors on the network.

This means: when a scan tool tells you an ECU is not responding, your diagnostic priority one is to find the CAN fault that drove it bus-off. Fix the bus, power-cycle the vehicle, and that ECU may come back on its own. Do not replace the ECU before you have diagnosed the bus."

---

### Slide 9: "What Triggers Error Counter Increments?"

"Five defined error types cause error counter increments:

**Bit Error:** A node transmits a recessive bit (1) but reads back dominant (0) on the bus — or vice versa during data transmission (not during arbitration, where this is expected). Indicates a node whose output is not matching the bus state.

**Stuff Error:** CAN uses bit stuffing — after 5 consecutive identical bits, the transmitter inserts one complementary bit to ensure clock synchronisation. If a receiver sees 6 consecutive identical bits, a stuff error is declared. Indicates frame corruption, usually from noise or a malfunctioning transmitter.

**CRC Error:** The receiver's independently calculated CRC does not match the CRC field in the frame. The data was corrupted in transit. Most commonly caused by noise, bad termination causing reflections, or a single wire fault.

**Form Error:** A field that must contain a fixed pattern (such as the EOF's 7 recessive bits or the ACK delimiter) does not contain that pattern. Indicates severe frame corruption.

**Acknowledgement Error:** The transmitter sent the ACK slot recessive and nobody pulled it dominant. Nobody acknowledged the frame. This happens when: all other nodes are already bus-off, the bus has a physical fault preventing dominant bits reaching the transmitter, or there are no other nodes on the bus at all."

---

### Slide 10: "Fault Signatures Reference — Oscilloscope and Scan Tool"

**Present this table and walk through each row:**

| Fault Condition | Oscilloscope Reading | Scan Tool / DTC Pattern |
|-----------------|---------------------|------------------------|
| Healthy bus | Clean CANH/CANL transitions 1.5 V / 2.5 V / 3.5 V, differential 0–2 V, no ringing | No communication DTCs |
| Dominant stuck (node pulling bus permanently) | CANH steady ~3.5 V, CANL steady ~1.5 V, no transitions at all | All nodes: "no communication from [every other node]" — complete network down |
| CANH to CANL short circuit | Both wires at ~2.5 V, no transitions | Bus permanently recessive — complete network down |
| One wire open (CANH or CANL broken) | One wire flat (at ~0 V or floating), other wire shows asymmetric signal | Intermittent comms, high error rate, gets worse with speed and noise |
| Missing ACK (all other nodes off) | Frame transmits, ACK slot stays recessive, error frame follows immediately | Transmitting node accumulates errors, rapidly reaches bus-off |
| Missing one termination resistor | Visible ringing/overshoot at end of each bit transition | Intermittent CRC errors, worse at high speeds and long bus runs |
| No termination resistors at all | Severe ringing, signal does not settle cleanly between bits | No reliable communication, possibly no communication at all |
| Extra termination (three or more) | Dominant bit voltage amplitude reduced — does not reach 3.5 V / 1.5 V cleanly | Bus may not reach dominant threshold reliably; intermittent frame losses |
| Termination measured at ~0 Ω | Cannot distinguish from CANH-CANL short | No communication |

"This table is your reference for tomorrow's lab. You will produce most of these fault conditions deliberately and identify them by measurement."

---

## SESSION CLOSE (5 minutes)

### Summary — Instructor delivers verbally:

"Five things to take away from today:

One: CAN uses differential signaling on a twisted pair. Noise affects both wires equally and cancels in the difference measurement.

Two: Dominant (CANH 3.5 V, CANL 1.5 V) drives the bus. Recessive (both 2.5 V) is the idle state. One dominant node overrides all recessive nodes.

Three: A CAN frame has seven distinct fields — SOF, Arbitration ID, Control, Data, CRC, ACK, EOF — each with a specific diagnostic role. The ACK field is particularly important for fault diagnosis.

Four: Arbitration is non-destructive. All nodes transmit simultaneously. Lowest ID wins. No data is destroyed in the process.

Five: A node that accumulates too many errors goes bus-off. It still has power and ground. Only its CAN interface is offline. Find the bus fault first before replacing any ECU."

### Preview of Day 15 hands-on:

"Tomorrow morning: bench with two or three CAN nodes. You will measure CANH and CANL voltages in healthy and faulted states, capture oscilloscope waveforms and identify planted faults, measure termination resistance and interpret the result, and use the scan tool to find a bus-off node.

Before you arrive: have the dominant and recessive voltage levels memorised. Have the 7 frame fields written in your notes. If you walk in without those, you will lose 20 minutes reconstructing them from scratch while your bench partner is already working."

---

## INSTRUCTOR NOTES

**Timing risks:**
- Block 3 (arbitration) can expand significantly if students engage with the bit-level worked example. If time is short, reduce the worked example to two nodes. The mechanism is more important than the arithmetic.
- Block 4 (error states) must not be cut. Students who do not understand bus-off routinely misdiagnose it as a dead ECU. This mistake is expensive for customers.

**Common student confusions to address explicitly:**
- "Dominant = logic 1?" — No. Dominant = logic 0. Many students assume dominant = high signal = logic 1 from digital electronics background. Reinforce this at least twice during Block 1.
- "Why does lower ID mean higher priority?" — Because the ID is transmitted MSB first. A lower number has more leading zeros. Each leading zero is a dominant bit. The node with more leading dominant bits stays on the bus longer before encountering a conflict bit.
- "Bus-off means the ECU is broken?" — No. Bus-off is a recoverable hardware state. The ECU processor is often still running normally. Demonstrate this by pointing to the bus-off state machine recovery path.

**Materials required:**
- Slide deck (11 slides as described)
- Whiteboard and markers — essential, diagrams must be drawn live as concepts are explained
- Printed CAN frame field reference card (one per student — they use this in the lab)
- Printed fault signatures table (one per student — they use this in the lab)

**Assessment alignment:**
- Module 7 quiz (end of Day 16) includes: draw dominant/recessive voltage levels; name all 7 frame fields with one-line purpose for each; explain what bus-off means and what drives a node into it.

---

## PPT SLIDE GUIDE

| Slide | Title | Key Visual / Content |
|-------|-------|---------------------|
| 1 | [Blank — Opening Hook] | No text. Deliver scenario verbally. |
| 2 | Why Two Wires for One Signal? | Differential signaling diagram. Voltage table: dominant / recessive states. Noise cancellation illustration. |
| 3 | Dominant and Recessive | Simple diagram: bus pulled dominant by one node while others are recessive. Definition text only. |
| 4 | Termination Resistors | Topology diagram: bus with two 120 Ω resistors at each end. Parallel resistance = 60 Ω. Fault table. |
| 5 | CAN Frame — Overview | Stacked bar diagram of all frame fields with bit widths labelled. |
| 6 | CAN Frame — Field by Field | One row per field: name, size in bits, purpose, diagnostic relevance. |
| 7 | Oscilloscope View of a CAN Frame | Dual-channel waveform diagram: CANH and CANL on same grid, differential math channel below. Healthy frame annotated with field boundaries. |
| 8 | CAN Arbitration | Multi-step diagram: three nodes transmitting simultaneously, bit-by-bit outcome table showing which node drops out at each step. |
| 9 | Error States — State Machine | State diagram as drawn on whiteboard. TEC thresholds labelled on each transition arrow. |
| 10 | Error Types | Five error types in bullet form: Bit, Stuff, CRC, Form, Acknowledgement. One-line description each. |
| 11 | Fault Signatures Reference Table | Full-width table from Block 4. Students photograph or receive as printed handout. |

---

*Framework prepared for ECUHR Module 7, Day 15 Theory.*
*Session outcomes: so-7-1-1, so-7-1-2, so-7-1-3, so-7-1-4*
*Date prepared: 2026-02-18*
