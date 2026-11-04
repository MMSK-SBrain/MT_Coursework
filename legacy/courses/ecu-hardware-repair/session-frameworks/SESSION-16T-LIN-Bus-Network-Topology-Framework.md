# SESSION-16T — LIN Bus & Network Topology
## Day 16 Theory | Module 7: CAN Bus, LIN & Communication Diagnostics

---

**Course:** ECU Hardware Repair (ECUHR)
**Session Code:** SESSION-16T
**Day:** 16 of 20
**Type:** Theory — Lecture with waveform analysis, topology case study
**Duration:** 75 minutes
**Delivery:** Instructor-led, slide-supported, whiteboard case study

**Session Outcomes:**
- so-7-3-1: Explain LIN bus topology, frame structure, and common applications
- so-7-4-1: Use a network topology diagram to plan a systematic disconnection sequence for fault isolation

**MO Alignment:** MO 7-3 (partial), MO 7-4 (partial)
**CO Alignment:** co-1 (Diagnose ECU faults by applying knowledge of automotive-grade circuit design)

**Prerequisites:**
- SESSION-15T and SESSION-15H completed
- Students are now comfortable with CAN voltage measurement, oscilloscope capture, and scan tool network tests
- This session extends the network context to a second protocol and introduces the topology-based isolation methodology

---

## Session Overview

| Block | Time | Topic | Format |
|-------|------|-------|--------|
| Hook | 0–7 min | Opening scenario: the bus is dead — how do you find which node killed it? | Discussion |
| Block 1 | 7–32 min | LIN bus — architecture, frame structure, applications | Lecture + waveform description |
| Block 2 | 32–45 min | LIN fault patterns — what each failure looks like | Lecture + table |
| Block 3 | 45–70 min | Network topology and systematic node isolation | Case study + whiteboard exercise |
| Close | 70–75 min | Summary, preview of hands-on lab | Discussion |

---

## OPENING HOOK (0–7 minutes)

### The Scenario:

"Yesterday you found a CAN bus with a stuck dominant fault — one node was pulling the bus permanently low and killing all communication. You identified the node, you disconnected it, the bus came back.

Now here's the next level. You are on a vehicle. You have done the same oscilloscope measurement — stuck dominant. You go to disconnect the guilty node, but the trouble is: there are nine modules on this bus segment. You have no idea which one is causing the problem. Nine modules. You cannot reach most of them without removing interior panels.

How do you find the faulty node without dismantling the entire car?

Take one minute. Write down your approach. Just bullets — don't overthink it."

**Give students 60 seconds to write.**

**Take two or three responses.** Common answers will include: "start at one end and unplug each one," "use the scan tool to see which one doesn't respond," "check which one has a fault code." Acknowledge all of these.

"All of those are in the right direction. But 'start at one end and unplug each one' on a real vehicle could mean removing a door card to reach the window motor controller, then a seat to reach the seat module, then the dashboard for the climate panel — each one taking 20 minutes. In a worst case, that is a three-hour diagnostic exercise that could be done in 30 minutes if you read the topology diagram first and pick the right disconnection sequence.

This afternoon we are going to learn how to read the topology, how to pick that sequence, and how to execute the isolation efficiently. But first — LIN bus. Because not every dead network is a CAN network."

---

## BLOCK 1 — LIN Bus Architecture, Frame Structure, Applications (25 minutes)

### Slide 2: "LIN Bus — The Simpler Network for Simple Jobs"

**Script:**
"LIN stands for Local Interconnect Network. It was designed for applications where CAN is overkill — too fast, too expensive, uses too many pins. LIN uses a single wire, runs at 1 to 20 kilobits per second (compared to CAN at 500 kbps), and costs significantly less per node to implement.

The trade-off: LIN is far less robust, has no error frame mechanism, and is only used for non-safety-critical subsystems."

**Whiteboard — draw the LIN topology:**

```
        Battery+ (12V)
             │
        [1kΩ pullup resistor — inside Master]
             │
LIN Bus wire ─────────────────────────────────
             │           │           │
          [Master]    [Slave 1]   [Slave 2]  ... [Slave N]
          (Climate     (Seat      (Mirror
           panel)       heater)    fold)
```

"Key differences from CAN — write these down:

| Feature | CAN | LIN |
|---------|-----|-----|
| Wires | 2 (twisted pair) | 1 (single wire) |
| Voltage logic | Differential (0–2V) | Single-ended (0–12V) |
| Speed | Up to 1 Mbps | 1–20 kbps |
| Protocol | Multi-master | Single master, multiple slaves |
| Termination | 120Ω resistors at each end | No termination — master has internal 1kΩ pullup |
| Error mechanism | Active/Passive error frames | None — checksum mismatch, frame discarded silently |
| Use cases | Engine, ABS, transmission, safety systems | Seat, mirror, climate, sunroof, lighting |
| Safety critical | Yes | No |
"

---

### Slide 3: "LIN Signal Levels and Logic"

**Script:**
"LIN uses a single-ended signal relative to chassis ground, powered from the 12 V bus through a 1 kΩ pullup resistor inside the master.

Logic levels:
- Recessive: the bus is pulled high through the 1 kΩ resistor — approximately 12 V (battery voltage). This is the idle state.
- Dominant: a transmitting node (master or slave) pulls the wire to ground through its output transistor — approximately 0 V.

Note the difference from CAN: LIN dominant is 0 V. LIN recessive is 12 V. Do not confuse these with CAN levels.

Because the pullup is 1 kΩ rather than the 120 Ω termination resistors in CAN, the bus transitions are slower — the RC time constant of the pullup with the bus capacitance causes rounded edges on the waveform at the oscilloscope. You will see this in tomorrow's lab. A LIN waveform does not have sharp vertical transitions like CAN."

---

### Slide 4: "LIN Frame Structure"

**Script:**
"LIN communication is entirely master-controlled. The master initiates every exchange. Slaves only respond when addressed."

**Whiteboard — draw the LIN frame:**

```
| BREAK | SYNC | PROTECTED ID | RESPONSE (0–8 bytes) | CHECKSUM |
  ≥13 dom  0x55   6-bit ID       Slave transmits          1 byte
  bits              + parity      (or master, for
                    bits           command frames)
```

Walk through each part:

**BREAK field:**
"The Break field is the most recognisable feature of a LIN frame on the oscilloscope. It is at least 13 consecutive dominant bits — much longer than anything that appears inside a normal LIN data byte. The purpose is synchronisation: every device on the bus, regardless of its clock state, will recognise this break as the start of a new frame. You cannot miss it. On the oscilloscope it looks like a long low pulse, typically 1–1.5 ms wide."

**SYNC byte:**
"Immediately after the break, the master transmits the byte 0x55 — binary 01010101 — alternating ones and zeros. This byte allows every slave to measure the bit period and synchronise its internal baud rate counter to the master. This matters because LIN slaves are cheap — they use low-cost oscillators that drift slightly. The sync byte re-aligns everyone at the start of each frame."

**Protected ID (PID):**
"The Protected Identifier field is 6 bits of message ID plus 2 parity bits, making one byte. The 6-bit ID gives 64 possible message IDs per LIN bus (0–63). The parity bits allow detection of a corrupted ID byte.

The ID determines which slave should respond. The LIN network is pre-configured so each slave knows which IDs it is responsible for. When a slave sees its assigned ID in the PID field, it knows: 'that is my cue — I transmit the response.'"

**Response field:**
"The response is transmitted by the slave (for read operations) or by the master (for command/write operations). Between 1 and 8 bytes. The content — which bits mean what — is defined in the LIN Description File (LDF), analogous to a DBC file for CAN. Without the LDF, you cannot decode the payload."

**Checksum byte:**
"One byte at the end of the response. The master and all slaves independently calculate the checksum over the response bytes. If the received checksum does not match, the frame is silently discarded. There is no error frame. There is no acknowledgement. The master simply did not receive a valid response.

This is important for fault diagnosis: on LIN, faults are silent. There is no mechanism that announces an error like CAN's active error frame. You find LIN faults by looking for missing responses."

---

### Slide 5: "Common LIN Applications in Vehicles"

**Script:**
"LIN is used everywhere in vehicle comfort and convenience systems. When you open a job and see these modules involved, think LIN:

**Seating:**
- Electric seat adjustment modules (fore/aft, tilt, height, recline)
- Seat heating and ventilation controllers
- Seat memory modules
- Lumbar support motors

**Mirrors and windows:**
- Power folding mirror modules
- Mirror position memory controllers
- Some power window modules

**Steering column:**
- Multifunction switch clusters (stalk switches for wipers, indicators, cruise)
- Column adjustment motors

**Climate:**
- Blower motor controllers
- Panel/face vent actuators
- Recirculation flap motors
- A/C compressor clutch modules in some systems

**Interior lighting:**
- Footwell, door handle, ambient lighting controllers
- Interior lamp dimming modules

**Roof:**
- Sunroof and panoramic roof modules
- Convertible top control

What is NOT on LIN: engine management, ABS, transmission control, airbag, EPS, ADAS. These are CAN or FlexRay — they need the speed, the reliability, and the error handling that LIN does not provide."

---

## BLOCK 2 — LIN Fault Patterns (13 minutes)

### Slide 6: "What LIN Faults Look Like — Oscilloscope and Symptom Patterns"

**Script:**
"LIN faults present very differently from CAN faults because LIN has no error frame mechanism. Where a CAN bus-off shows up immediately on a scan tool as a missing node, a LIN fault may show up only as a symptom — the seat doesn't move, the mirror won't fold, the fan is stuck at one speed.

Let me give you the three most common LIN fault patterns and what you will see."

**Whiteboard table:**

```
FAULT: No response from slave

Symptom: Feature not working. Scan tool may show "component not responding"
         for that subsystem.

Oscilloscope: Master transmits header cleanly — break, sync, PID all visible.
              After PID field, bus returns to recessive (12V).
              No response bytes. Bus stays high until next master header.

Causes:
  1. Slave is unpowered — check supply voltage to slave module
  2. Open wire between master and slave — LIN wire broken
  3. Slave module internal failure — output driver died
  4. LIN wire shorted to battery (+12V) — bus cannot go dominant

Diagnosis: Probe LIN wire at the slave module's connector. If master header is
           visible there (break + sync + PID present), the wire is intact to that
           point and the slave itself is the likely fault.
           If master header is not visible there, the wire is broken or the master
           is not transmitting (master fault or no power to master).
```

```
FAULT: Stuck dominant (slave output shorted to ground)

Symptom: All features on that LIN bus stop working. Master cannot communicate
         with any slave.

Oscilloscope: LIN bus pulled continuously to 0V. No break, no sync, nothing.
              Bus is stuck low permanently.

Causes:
  1. One slave's output transistor has failed shorted to ground
  2. LIN wire has a hard short to chassis ground

Diagnosis: Disconnect slaves one at a time. When bus returns to 12V idle after
           disconnecting Slave X, Slave X is the fault cause.
           Verify by measuring resistance from LIN pin of Slave X to ground —
           should be high, if it reads near 0Ω the output is shorted.
```

```
FAULT: Frame error / checksum mismatch

Symptom: Intermittent feature operation. Feature works sometimes, fails
         randomly, may work on ignition cycle.

Oscilloscope: Break and sync visible. Response bytes visible but with distorted
              transitions — rounding more severe than normal, possible glitches.
              Checksum byte may be corrupted.

Causes:
  1. EMI coupling into LIN wire (usually from nearby high-current loads —
     electric fan motor, seat motor on same harness run)
  2. Poor ground connection at slave — LIN return path degraded
  3. Partially damaged slave transceiver — outputs are weak or noisy
  4. LIN wire partially open (high resistance joint, corroded connector)

Diagnosis: Inspect harness routing — is LIN wire bundled with high-current loads?
           Check ground integrity of the slave module.
           Probe LIN wire close to slave to check signal quality.
```

**Emphasise:** "You will notice that 'disconnect nodes one at a time' appears in two of those three fault patterns. On LIN, physical isolation is your primary diagnostic tool. The protocol gives you very little software-level error information."

---

## BLOCK 3 — Network Topology and Systematic Fault Isolation (25 minutes)

### Slide 7: "The Topology Diagram — Your Map Before You Start Disconnecting"

**Script:**
"In automotive diagnostics, a network topology diagram shows you:
- Every CAN and LIN bus segment in the vehicle
- Which modules are on each segment
- Where the termination resistors are physically located
- Which module is the gateway between bus segments
- Which bus segment carries which type of traffic

Before you disconnect a single module, you must understand the topology of the network. Without it, you are guessing. With it, you can plan a three-step isolation that takes 20 minutes instead of a two-hour random process."

**Draw a representative vehicle network topology on the whiteboard:**

```
                     OBD Port
                         │
                     [Gateway ECU]
                    /     │      \
                   /      │       \
      Powertrain CAN   Body CAN   Chassis CAN
      (HS-CAN 500k)   (MS-CAN 125k)  (HS-CAN 500k)
           │              │               │
    ┌──────┤        ┌─────┤         ┌─────┤
    │      │        │     │         │     │
  [ECM]  [TCM]   [BCM]  [ICC]    [ABS]  [EPS]
    │              │
    │          [LIN bus 1]──[Seat L]──[Seat R]──[Mirror L]──[Mirror R]
    │
    │          [LIN bus 2]──[Climate panel]──[Blower ctrl]──[Vent actuators x3]
    │
  [EMS]       [LIN bus 3]──[Steering col. switches]──[Wiper ctrl]
```

"This is a simplified topology but it shows the key features:
- There are three separate CAN bus segments — powertrain, body, and chassis
- They are connected only through the Gateway ECU
- Each CAN segment has its own termination
- Several LIN buses hang off the BCM, each serving a subsystem cluster
- The OBD port connects to the Gateway — your scan tool talks to the Gateway first, then the Gateway relays to other segments

Why does this matter for diagnosis?"

**Give three reasons:**

"Reason 1: A fault on one bus segment does NOT cause faults on other segments — unless the gateway itself is affected. If you have communication faults only on powertrain CAN modules, you are not looking at a problem with the body CAN or the gateway. You can narrow your search immediately.

Reason 2: The termination resistors are at physical locations on the bus. The topology diagram tells you where they are — usually at the module farthest from the gateway and at the gateway itself, or at dedicated junction boxes. Knowing where they are tells you what you expect when you measure termination resistance.

Reason 3: When you plan a systematic disconnection to find a stuck-dominant node, you want to disconnect the node that is most likely to be faulty first — based on DTC patterns, based on scan tool responses, and based on which module is physically easiest to access. The topology diagram tells you all of those things."

---

### Slide 8: "Planning a Systematic Disconnection Sequence"

**Script:**
"Here is the framework. You will apply this in the hands-on session this afternoon."

**Write on whiteboard — the isolation protocol:**

```
STEP 1: Establish what you know from the scan tool and wiring diagram
  - Which nodes are responding?
  - Which nodes are not responding (bus-off or not communicating)?
  - What DTCs are stored in the responding nodes, and do they point at a specific
    module or bus segment?

STEP 2: Measure the bus before touching anything
  - Oscilloscope: is the bus stuck dominant, stuck recessive, or active-but-faulted?
  - Multimeter: what are CANH and CANL absolute voltages?
  - If stuck dominant: you have a node pulling the bus. Proceed to Step 3.
  - If stuck recessive: you have a short between CANH and CANL.
    Measure termination resistance — if near 0Ω, the bus wires are shorted, not a node.

STEP 3: Choose your first disconnection target
  Priority order:
  a) The most recently replaced or repaired module (most common — damaged during
     service, wrongly fitted, wrong part)
  b) The module with the most relevant DTCs pointing at it
  c) The module that was last known to work (if you have service history)
  d) The module at the far end of the bus (if no other information — it is usually
     easiest to reach without disturbing the rest of the harness)

STEP 4: Disconnect and test
  - Disconnect the chosen module from the bus at its connector
  - Do NOT power-cycle yet (sometimes bus recovers immediately when node is
    physically disconnected — you will see it on the oscilloscope)
  - Observe oscilloscope: did bus recover?
  - If yes: the disconnected module was the fault source. Proceed to Step 5.
  - If no: reconnect that module, move to next candidate, repeat.

STEP 5: Root-cause the isolated module
  - With the faulty module disconnected, confirm bus is healthy
  - Inspect the module's connector: corrosion, bent pins, moisture ingress
  - Inspect harness at that module: chafing, pinching, damage near connector
  - If harness/connector is clean: fault is in the module itself
  - Classify: wiring fault / transceiver fault / internal ECU fault

STEP 6: Document everything
  - Which nodes were disconnected and in what order
  - Which disconnection restored the bus
  - Waveform before and after
  - DTCs before and after
  - Root cause determination
```

**Real-world warning — say this clearly:**
"When you disconnect a module from the CAN bus, every other module that expects to receive data from it will set a communication DTC. When you reconnect it and power-cycle, those DTCs may or may not clear automatically. Always document the DTC state before you start disconnecting, and always clear and re-verify DTCs after the repair is complete. Some customers will come back complaining about warning lights that you caused during diagnosis — documentation is your protection."

---

### Slide 9: "Case Study — Walk Through the Protocol on a Scenario"

**Present this as a guided exercise — students work through it on a worksheet while the instructor narrates:**

**Scenario:** Customer complaint: multiple warning lights including ABS, EPS, and instrument cluster. Scan tool connected. Powertrain CAN modules respond. ABS, EPS, and instrument cluster do not respond. Oscilloscope on the chassis CAN bus shows stuck dominant — bus is pulled low, no transitions.

Refer to the topology diagram drawn earlier.

"Work through Steps 1–3. Write down:
- What you know from the scan tool
- What the oscilloscope tells you
- Which module you would disconnect first, and why

You have 4 minutes."

**After 4 minutes, discuss:**

Expected reasoning:
- Step 1: Powertrain CAN is fine (engine and transmission ECUs respond). Chassis CAN is affected (ABS, EPS, cluster don't respond). Gateway is probably fine since powertrain CAN works. Fault is on the chassis CAN segment only.
- Step 2: Stuck dominant — one node on chassis CAN is pulling the bus low. Not a CANH-CANL short (that produces stuck recessive). This is a node fault.
- Step 3: Three candidates — ABS, EPS, instrument cluster. Customer said multiple warning lights started "suddenly" with no service history. Check: was any chassis work done recently? If ABS was recently replaced, start there. If no history, check which node is easiest to access. On most vehicles, the instrument cluster connector is the most accessible from the passenger compartment without lifting panels.

**Alternative scenario element — add this to deepen the discussion:**
"What if, when you check service records, you see the EPS was replaced two weeks ago? Where do you disconnect first?" (EPS — most recently replaced, highest probability of being installed incorrectly or having a transceiver damaged during fitting.)

---

## SESSION CLOSE (5 minutes)

### Summary:

"Three things from today:

One: LIN bus uses a single wire, 12 V logic, master-slave protocol, and is used for comfort and convenience systems only. Its lack of an error frame mechanism means faults are silent — you find them by measuring the wire and isolating nodes physically.

Two: LIN fault patterns — no response (slave unpowered, open wire, failed slave), stuck dominant (output shorted to ground), frame errors (noise or degraded transceiver). Disconnect nodes one at a time to isolate.

Three: CAN fault isolation on a multi-node network requires a topology diagram and a planned disconnection sequence. Use DTCs and scan tool data to rank candidates before you disconnect anything. One systematic reconnect-and-test takes 30 minutes. Random disconnection takes three hours and upsets the customer when they see new warning lights."

### Preview of hands-on:

"This afternoon: bench with a 3-node CAN network. One node has a planted fault causing the bus to fail. Your job is to isolate it using the protocol you practised today. You will also have a small LIN bench to measure healthy and faulted LIN frames. Bring your fault signatures table and your topology notes."

---

## INSTRUCTOR NOTES

**Timing risks:**
- Block 3 (topology and isolation protocol) tends to expand when students ask vehicle-specific questions. Keep the case study tight — 4 minutes for students to work independently, 5 minutes to discuss. Total Block 3 should not exceed 25 minutes.
- If the class finishes early: extend the case study to a second scenario (e.g., a LIN bus stuck dominant with 4 slaves — work through the disconnection sequence).

**Common student confusions:**
- "LIN dominant is low and recessive is high — that is the opposite of CAN?" — Yes, in terms of voltage. CAN recessive is 2.5 V (mid-rail). LIN recessive is 12 V (high rail). Different physical layers. Same naming convention: dominant wins over recessive in both protocols.
- "If LIN has no error frame, how does the scan tool know a LIN slave is missing?" — The scan tool communicates with the LIN master (e.g., the BCM). The BCM detects that the expected response from a slave did not arrive. The BCM logs a DTC internally. The scan tool reads the BCM's DTC, not the LIN bus directly.
- "Why do we bother with a topology diagram — can't we just look at the scan tool?" — The scan tool shows which nodes are responding. The topology shows WHY they are or are not responding — which bus segment they are on, what other nodes share that segment, where the power comes from, where the termination is. The scan tool gives you the symptom; the topology diagram helps you find the cause.

**LIN bus note for instructors:**
LIN is listed as MEDIUM priority in the curriculum gap analysis. The depth covered here (architecture, frame, three fault patterns, oscilloscope identification) is appropriate for a general ECU repair technician. Deep LIN diagnosis (LDF analysis, slave programming, LIN master programming) is out of scope and should be referred to module-specific courses.

**Materials:**
- Slide deck (9 slides as structured)
- Whiteboard (topology diagram must be drawn live — do not use a pre-prepared slide for this; drawing it in front of the class makes the topology legible and memorable)
- Case study worksheet (one per student — five lines: Step 1 findings, Step 2 findings, First disconnection choice, Reason, Next step if first choice wrong)
- Printed LIN-CAN comparison table (one per student — from Slide 2)

---

## PPT SLIDE GUIDE

| Slide | Title | Key Visual / Content |
|-------|-------|---------------------|
| 1 | [Blank — Opening Hook] | No text. Deliver verbal scenario. |
| 2 | LIN Bus — The Simpler Network | LIN topology diagram. CAN vs LIN comparison table. |
| 3 | LIN Signal Levels | LIN waveform diagram: recessive 12 V, dominant 0 V. Note slow transitions due to RC effect of pullup. |
| 4 | LIN Frame Structure | Frame field diagram: break, sync, PID, response, checksum. Annotate the break as the long dominant pulse. |
| 5 | LIN Applications | Categorised list: seating, mirrors, climate, steering column, lighting, roof. "What is NOT on LIN" column. |
| 6 | LIN Fault Patterns | Three-section table: fault name, oscilloscope appearance, causes, diagnosis approach. |
| 7 | Vehicle Network Topology | Topology diagram (draw on whiteboard live — this slide is a blank or a lightweight placeholder). |
| 8 | Systematic Isolation Protocol | Six-step protocol as written in Block 3. |
| 9 | Case Study Scenario | Text description of the chassis CAN stuck-dominant scenario. Students work on worksheet. |

---

*Framework prepared for ECUHR Module 7, Day 16 Theory.*
*Session outcomes: so-7-3-1, so-7-4-1*
*Date prepared: 2026-02-18*
