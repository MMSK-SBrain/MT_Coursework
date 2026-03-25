---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 8
week_title: "The Complete Technician"
day_number: 38
session_title: "CAN Bus & Network Diagnostics Deep Dive"
duration_minutes: 180
theory_practice: "40:60"
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 38: CAN Bus & Network Diagnostics Deep Dive
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (70 min theory + 110 min practical)
**Approach:** Layer-by-Layer Technical Deep Dive with Hands-On Verification
**PPT Target:** 26-28 slides
**Week:** 8 of 8 — "The Complete Technician"

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Explain CAN bus differential signaling including CAN-H and CAN-L voltage levels
- Describe the structure of a CAN message frame (SOF, arbitration ID, control, data, CRC, ACK, EOF)
- Explain how message priority works on the CAN bus (lower ID = higher priority)
- Distinguish high-speed CAN (500 kbps, powertrain) from low-speed CAN (125 kbps, body)
- Explain the role of 120-ohm termination resistors and measure total bus termination at the OBD-II port
- Identify common ECU types and their network roles (ECM, TCU, BCM, ABS/ESC, airbag, instrument cluster, HVAC, steering, gateway)
- Read and interpret U-codes (network communication DTCs) using a scan tool
- Identify common CAN bus faults (shorted lines, open lines, missing termination, faulty module)
- Interpret a CAN waveform on an oscilloscope (or from captured waveform images)
- Perform a service interval reset procedure on a vehicle

**This is the deep dive that was promised on Day 6.** Learners have spent 7 weeks working with scan tools, reading DTCs, and hearing "the ECUs talk on CAN bus." Today they finally understand how that conversation works at the wire level and what happens when it breaks.

---

## Connection to Prior Knowledge

Build on these previously established concepts:
- **Day 6** (Week 1): First introduction to CAN bus as "the vehicle's nervous system network." Learners saw the OBD-II port and used a scan tool for the first time.
- **Day 8** (Week 2): Electrical fundamentals — voltage, current, resistance, Ohm's law. Learners can now understand differential signaling as two voltage measurements.
- **Day 10** (Week 2): Oscilloscope introduction — learners have basic scope skills for viewing waveforms.
- **Days 11-37**: Every system session involved scan tool communication through the CAN bus. Learners have read hundreds of DTCs, but U-codes were always deferred to "Week 8."

**Bridge:** "For seven weeks, you've been plugging into the OBD-II port and talking to the car's computers. You've seen P-codes for engine faults, B-codes for body faults, C-codes for chassis faults. But what about U-codes? Those are the network codes — they tell you when ECUs stop talking to each other. Today, we open up the network layer. You're going to understand how these computers actually communicate — at the wire level — and what to do when that communication fails."

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: From Conceptual to Wire-Level** (Slides 1-3, ~10 minutes)

**Narrative Voice:** Direct, building anticipation. This bridges beginner-level awareness to professional-level understanding.

---

#### Slide 1: Title & Callback
**Visual:** Split image — left side shows a simple CAN bus diagram from Day 6 (basic box-and-line), right side shows a real oscilloscope CAN waveform capture with voltage annotations

**Instructor Narration:**
> "Day 6. Week 1. I showed you a diagram with boxes connected by lines and said 'this is CAN bus — the ECUs talk to each other on this network.' You nodded. You had no idea what I meant. Seven weeks later, you've used the scan tool hundreds of times. Every time you read a DTC, every time you watched live data, your scan tool was sending and receiving CAN messages. Today, we pull back the curtain. You're going to understand exactly what's happening on those two wires — and more importantly, what to do when the network goes down and half the car's warning lights come on at once."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 8: The Complete Technician
Day 38: CAN Bus & Network Diagnostics Deep Dive

Day 6: "CAN bus is the vehicle's network."
Day 38: Now you learn how it actually works — and how to fix it.
```

---

#### Slide 2: Today's Plan
**Visual:** Horizontal timeline with four blocks — Theory Part 1, Theory Part 2, Practical, Wrap-Up

**Instructor Narration:**
> "Here's how today unfolds. First 30 minutes: the CAN protocol — differential signaling, message structure, bus speed, termination. Next 20 minutes: network faults, U-codes, and what a CAN waveform looks like. Then we hit the workshop for 90 minutes of hands-on work — measuring termination resistance, capturing waveforms, reading U-codes on a scan tool, and performing a service interval reset. We finish with a 15-minute wrap-up tying it all together. By the end of today, you'll be able to diagnose network faults that send other technicians in circles for hours."

**PPT Content:**
```
TODAY'S PLAN (180 minutes)

THEORY PART 1 (30 min): CAN Protocol Deep Dive
-- Differential signaling, message frames, priority, speed, termination

THEORY PART 2 (20 min): Network Faults & Oscilloscope Capture
-- U-codes, bus-off, module detection, CAN waveform analysis

PRACTICAL (90 min): Hands-On Network Diagnostics
-- Termination resistance measurement
-- Oscilloscope CAN waveform capture
-- U-code diagnosis with scan tool
-- Service interval reset procedure

WRAP-UP (15 min): Consolidation & Key Takeaways

+ 10 min buffer for questions
```

---

#### Slide 3: Why Network Diagnostics Matters
**Visual:** Photo of a dashboard lit up like a Christmas tree — multiple warning lights on simultaneously (ABS, ESC, engine, airbag, TPMS, power steering)

**Instructor Narration:**
> "Here's a scenario you'll see in the real world. A customer drives in and every warning light on the dashboard is lit. Engine, ABS, airbag, power steering, ESC — all of them. A beginner thinks five systems have failed simultaneously. That's almost never the case. What's actually happened? One thing went wrong: the CAN bus. When the network goes down, ECUs can't talk to each other. Each one thinks the others have failed, so every module sets its own fault code. You'll pull 15 DTCs — and 14 of them are symptoms, not the root cause. The technician who understands the network finds the single broken wire in 20 minutes. The technician who doesn't chases individual fault codes for days. That's the difference today makes."

**PPT Content:**
```
WHY NETWORK DIAGNOSTICS MATTERS

Scenario: Customer arrives with EVERY warning light on
-- Engine light
-- ABS light
-- Airbag light
-- Power steering light
-- ESC light
-- TPMS light

Beginner diagnosis: "Five systems failed!"
Expert diagnosis: "One CAN bus fault caused all of this."

Network faults create CASCADING symptoms.
Find the network fault = fix everything at once.
```

---

### **DEVELOPMENT PART 1: CAN Protocol Deep Dive** (Slides 4-14, ~30 minutes)

**Narrative Voice:** Precise and technical, but always anchored to physical reality. Use "what does the wire actually do?" as the guiding question.

---

#### Slide 4: CAN Bus — The Physical Layer
**Visual:** Diagram of a two-wire bus — CAN-H (red) and CAN-L (blue) as twisted pair, running between ECU nodes, with 120-ohm termination resistors at each end

**Instructor Narration:**
> "CAN bus is two wires. That's it. Two wires that connect every computer in the car. They're called CAN-High and CAN-Low — CAN-H and CAN-L. These wires are twisted together — a twisted pair — because twisting reduces electromagnetic interference. Every ECU on the network connects to these same two wires. Think of it as a party line telephone — everyone shares the same line, and there are rules about who talks when.
>
> At each end of the bus, there's a 120-ohm termination resistor. These resistors prevent electrical reflections that would corrupt the data. Two 120-ohm resistors in parallel give you 60 ohms total — and that's exactly what you should measure at the OBD-II port. Remember that number: 60 ohms. We'll measure it in the practical."

**PPT Content:**
```
CAN BUS — THE PHYSICAL LAYER

Two wires:
-- CAN-H (CAN High) — carries the "high" signal
-- CAN-L (CAN Low) — carries the "low" signal
-- Twisted pair — reduces electromagnetic interference (EMI)

Termination:
-- 120 ohm resistor at EACH END of the bus
-- Total measured at OBD-II port: ~60 ohm (two 120-ohm in parallel)
-- Without termination: signal reflections corrupt data

Connection: All ECUs connect in parallel to the same two wires
-- Like a party line: shared medium, one speaker at a time
```

---

#### Slide 5: Differential Signaling — How Bits Travel on Wire
**Visual:** Voltage diagram showing CAN-H and CAN-L signal levels. Recessive state: both at 2.5V. Dominant state: CAN-H at 3.5V, CAN-L at 1.5V. Differential voltage labeled (0V recessive, 2V dominant).

**Instructor Narration:**
> "Here's where it gets clever. CAN doesn't use a simple high-low voltage like a light switch. It uses differential signaling. Both wires sit at a resting voltage of 2.5 volts — this is the recessive state, representing a binary '1.' When a node wants to transmit a '0' — called the dominant state — CAN-H goes UP to 3.5 volts and CAN-L goes DOWN to 1.5 volts. The receiver doesn't look at either wire individually — it measures the DIFFERENCE between them.
>
> Why? Because electrical noise affects both wires equally. If a spark plug fires nearby and adds 0.5 volts of noise to both wires, the difference stays the same. The noise cancels out. That's why CAN bus is so reliable in the electrically noisy environment of a car engine bay. Two wires, moving in opposite directions. The difference is the signal."

**PPT Content:**
```
DIFFERENTIAL SIGNALING

RECESSIVE STATE (binary "1"):
   CAN-H = 2.5V       CAN-L = 2.5V
   Difference = 0V     (Bus is idle)

DOMINANT STATE (binary "0"):
   CAN-H = 3.5V       CAN-L = 1.5V
   Difference = 2.0V   (Active transmission)

Why differential?
-- Noise hits BOTH wires equally
-- Receiver measures DIFFERENCE (noise cancels out)
-- Extremely reliable in electrically noisy environments

DOMINANT always wins over RECESSIVE
-- If two nodes transmit simultaneously:
   one sends dominant (0), the other sends recessive (1)
   the bus shows dominant (0)
-- This is how arbitration works (next slide)
```

---

#### Slide 6: Dominant vs. Recessive — The Arbitration Trick
**Visual:** Timing diagram showing two ECUs transmitting simultaneously. ECU A sends a lower ID (more dominant bits early). ECU B detects it lost arbitration and stops transmitting.

**Instructor Narration:**
> "Here's the beauty of CAN bus design. What happens if two ECUs try to talk at the same time? On most networks, you get a collision and both messages are destroyed. CAN is different. It uses bitwise arbitration. Every message starts with its ID number, transmitted bit by bit. Dominant bits — zeros — overwrite recessive bits — ones — on the wire. So if ECU A is sending ID 0x100 and ECU B is sending ID 0x300, ECU A wins because its ID has more dominant bits earlier. ECU B notices its recessive bit got overwritten, realises it lost arbitration, and immediately stops transmitting. ECU A continues without ever knowing there was a conflict.
>
> The result? Lower ID number means higher priority. The engine controller with ID 0x010 will always win over the HVAC controller with ID 0x500. This is how CAN guarantees that safety-critical messages always get through."

**PPT Content:**
```
ARBITRATION — WHO GETS TO TALK?

Rule: LOWER message ID = HIGHER priority

How it works:
1. Multiple ECUs can start transmitting simultaneously
2. Each transmits its message ID bit by bit
3. Dominant (0) overwrites Recessive (1) on the wire
4. Each transmitter monitors the bus
5. If a node sends Recessive but reads Dominant:
   "Someone else has higher priority — I stop."
6. Winner continues transmitting, losers retry later

Example:
   ECU A sending ID 0x100 (00100000000) -- higher priority
   ECU B sending ID 0x300 (01100000000) -- lower priority

   At bit 2: A sends 0, B sends 1
   Bus shows 0 (dominant wins)
   B reads 0, knows it sent 1 --> B stops, A wins

NO data is lost. NO collision. NO retry delay.
```

---

#### Slide 7: CAN Message Frame Structure
**Visual:** Detailed diagram of a standard CAN 2.0A frame showing each field with bit counts: SOF (1 bit), Arbitration ID (11 bits), RTR (1 bit), Control (6 bits), Data (0-64 bits), CRC (16 bits), ACK (2 bits), EOF (7 bits)

**Instructor Narration:**
> "Let's look at what a CAN message actually contains. Every message is a frame with a very specific structure. It starts with the Start of Frame bit — SOF — a single dominant bit that tells everyone 'a message is coming.' Then comes the arbitration field — the 11-bit message ID we just discussed. This is followed by the RTR bit — Remote Transmit Request — which is almost always zero. Then control bits that tell receivers how many data bytes follow — zero to eight bytes of actual data.
>
> After the data comes a CRC — Cyclic Redundancy Check — a mathematical checksum. The receiver recomputes the CRC from the received data. If it doesn't match, the message is rejected. Then the ACK slot — every receiver that got a valid message pulls the bus dominant here, confirming receipt. Finally, End of Frame — seven recessive bits signaling the message is complete.
>
> You don't need to memorise every bit position. But you do need to understand: every CAN message is self-contained, error-checked, and acknowledged. That's why CAN is trusted in safety-critical systems."

**PPT Content:**
```
CAN MESSAGE FRAME (Standard CAN 2.0A)

SOF        | 1 bit   | Start of Frame (dominant — wakes up receivers)
ARBIT. ID  | 11 bits | Message identifier (determines priority)
RTR        | 1 bit   | Remote Transmit Request (0 = data frame)
CONTROL    | 6 bits  | Includes DLC (Data Length Code: 0-8 bytes)
DATA       | 0-64 bits | Actual payload (0 to 8 bytes)
CRC        | 16 bits | Error detection checksum
ACK        | 2 bits  | Receiver acknowledges valid receipt
EOF        | 7 bits  | End of Frame (recessive — bus returns to idle)

Key points:
-- Maximum 8 bytes of data per message
-- Every message has error checking (CRC)
-- Every message is acknowledged by receivers
-- No message needs a destination address — all nodes hear everything
-- Nodes filter by ID: "Is this message for me?"
```

---

#### Slide 8: Message Priority in Practice
**Visual:** Table showing common CAN message IDs by system — powertrain at low IDs (high priority), body at high IDs (low priority). Example: Engine Torque 0x0A0, ABS Wheel Speeds 0x0C0, Airbag Status 0x150, HVAC Request 0x400, Window Control 0x520.

**Instructor Narration:**
> "In practice, vehicle manufacturers assign message IDs based on how critical the data is. Engine torque requests get very low IDs — they need to arrive without delay. ABS wheel speed data sits close behind — it feeds into ESC calculations. Airbag status messages are medium priority. And things like HVAC temperature requests or window position signals? They get high IDs because a 10-millisecond delay in adjusting cabin temperature doesn't endanger anyone.
>
> This priority scheme means that even when the bus is heavily loaded, the most critical messages always get through first. Safety-critical data never waits behind comfort data."

**PPT Content:**
```
MESSAGE PRIORITY IN PRACTICE

Lower ID = Higher Priority = Gets transmitted first

Typical ID assignment hierarchy:
ID Range     | System              | Priority
-------------|---------------------|----------
0x000-0x0FF  | Powertrain (ECM, TCU) | HIGHEST
0x100-0x1FF  | Chassis (ABS, ESC, Steering) | HIGH
0x200-0x2FF  | Safety (Airbag, Seatbelt) | MEDIUM-HIGH
0x300-0x3FF  | Body (BCM, Lighting) | MEDIUM
0x400-0x5FF  | Comfort (HVAC, Windows, Mirrors) | LOW
0x600-0x7FF  | Diagnostics (OBD-II, Scan Tool) | LOWEST

OBD-II diagnostic messages:
   Request:  0x7DF (functional) or 0x7E0-0x7E7 (physical)
   Response: 0x7E8-0x7EF

Diagnostic messages have LOW priority by design
-- They must never interfere with safety-critical traffic
```

---

#### Slide 9: Bus Speed — High-Speed vs. Low-Speed CAN
**Visual:** Diagram showing a vehicle with two CAN buses — a high-speed backbone (500 kbps, red) connecting powertrain and chassis ECUs, and a low-speed bus (125 kbps, green) connecting body ECUs, joined by a gateway ECU

**Instructor Narration:**
> "Not all CAN buses run at the same speed. Most vehicles have at least two separate CAN networks. The high-speed CAN bus runs at 500 kilobits per second — that's 500,000 bits every second. It connects the safety-critical ECUs: engine controller, transmission controller, ABS, ESC, airbag module. These systems need fast, reliable communication.
>
> The low-speed CAN bus runs at 125 kilobits per second. It handles body electronics: central locking, window motors, mirror adjustment, interior lighting, HVAC controls. These don't need split-second response times, so a slower, cheaper bus works fine.
>
> The two buses are connected by a gateway ECU. The gateway decides which messages cross between networks. It's a firewall and a translator. If the body CAN bus fails, the powertrain CAN bus keeps working — the car still drives and brakes. The gateway isolates failures."

**PPT Content:**
```
BUS SPEED — TWO NETWORKS IN ONE CAR

HIGH-SPEED CAN (500 kbps):
-- Powertrain: ECM, TCU
-- Chassis: ABS/ESC, steering, active suspension
-- Safety: Airbag module
-- Speed: 500,000 bits/second
-- Critical: Safety and driveability functions

LOW-SPEED CAN (125 kbps):
-- Body: BCM, central locking, windows, mirrors
-- Comfort: HVAC, seat controls, interior lighting
-- Infotainment: Radio, navigation interface
-- Speed: 125,000 bits/second
-- Non-critical: Comfort and convenience functions

GATEWAY ECU:
-- Bridges high-speed and low-speed networks
-- Routes selected messages between buses
-- Isolates faults: body bus failure does not affect powertrain
-- Found in nearly all modern vehicles
```

---

#### Slide 10: Termination Resistors — Why 120 Ohms?
**Visual:** Diagram showing a CAN bus with two 120-ohm termination resistors at each end. Below: an OBD-II connector pinout highlighting pins 6 (CAN-H) and 14 (CAN-L). Multimeter shown measuring 60 ohms between these pins.

**Instructor Narration:**
> "Back to those termination resistors. CAN signals travel at nearly the speed of light along the wire. When a signal reaches the end of the bus with no termination, it bounces back — like an echo. That reflected signal interferes with the original signal and corrupts data. The 120-ohm resistor at each end absorbs the signal energy and prevents reflections.
>
> Where are these resistors? Usually built into the ECU at each physical end of the bus. One is often in the engine controller, the other in the instrument cluster or gateway — whichever ECU sits at the far end of the bus.
>
> Here's the diagnostic trick: at the OBD-II port, pins 6 and 14 are CAN-H and CAN-L. With the ignition OFF, measure resistance between them. Two 120-ohm resistors in parallel equals 60 ohms. If you read 60 ohms, termination is correct. If you read 120 ohms, one termination resistor is missing — probably a disconnected or failed ECU. If you read infinity, both are missing or the bus is open. If you read near zero, the wires are shorted together. This is your first diagnostic test for every CAN bus problem."

**PPT Content:**
```
TERMINATION RESISTORS

Why?
-- Prevent signal reflections at bus ends
-- Without them: data corruption, intermittent communication

Specification:
-- 120 ohm at EACH END of the bus
-- Total bus resistance: 60 ohm (two 120-ohm in parallel)
-- Usually integrated inside ECUs at the bus endpoints

OBD-II Port CAN Pins:
-- Pin 6 = CAN-H (High-speed CAN)
-- Pin 14 = CAN-L (High-speed CAN)

DIAGNOSTIC MEASUREMENT (ignition OFF):
Multimeter between Pin 6 and Pin 14:
   ~60 ohm  = CORRECT (both terminations present)
   ~120 ohm = ONE termination missing (ECU disconnected?)
   Infinity  = BOTH terminations missing or open bus
   ~0 ohm   = SHORT between CAN-H and CAN-L
```

---

#### Slide 11: CAN Bus Topology — Linear and Star
**Visual:** Two diagrams side by side. Left: Linear/daisy-chain topology with ECUs tapped off a single backbone. Right: Star topology with a central gateway and individual ECU connections radiating outward.

**Instructor Narration:**
> "How are the ECUs physically connected? Two main topologies. The classic CAN topology is linear — also called daisy-chain. One pair of wires runs the length of the vehicle. ECUs tap onto the bus with short stub connections. The termination resistors sit at the two physical ends.
>
> Many modern vehicles use a star topology instead. A central gateway ECU sits in the middle, and individual ECU connections radiate outward like spokes on a wheel. The advantage? If one ECU has a fault and drags the bus down, the gateway can isolate that branch. In a linear topology, one faulty ECU takes down the entire bus. The star topology gives you fault isolation — which makes your diagnostic job easier, because the gateway can tell you WHICH branch has the problem."

**PPT Content:**
```
CAN BUS TOPOLOGY

LINEAR (Daisy-Chain):
   [ECU1]--[ECU2]--[ECU3]--[ECU4]--[ECU5]
   120 ohm                          120 ohm

   + Simple wiring
   + Fewer connectors
   - One faulty ECU can take down entire bus
   - Harder to isolate faults

STAR (Central Gateway):
            [ECU1]
              |
   [ECU2]--[GATEWAY]--[ECU3]
              |
            [ECU4]

   + Gateway can isolate faulty branch
   + Easier fault diagnosis
   + Separate physical buses for different domains
   - More complex wiring
   - Gateway is single point of failure

Most modern vehicles: STAR topology with central gateway
```

---

#### Slide 12: ECU Types — The Network Residents
**Visual:** Vehicle outline with all major ECUs labeled and connected by CAN bus lines. Color-coded by bus: powertrain (red), chassis (blue), body (green). Gateway in the center.

**Instructor Narration:**
> "Let's put names to the nodes. You've met all of these ECUs individually over the past seven weeks. Now see them as a network community. The ECM — Engine Control Module — is the heart of the powertrain bus. It broadcasts engine speed, torque, throttle position, and temperature. The TCU — Transmission Control Unit — listens to the ECM and broadcasts gear position and shift commands. The ABS/ESC module broadcasts individual wheel speeds and brake pressure — data that the ECM and TCU also use.
>
> On the body bus: the BCM — Body Control Module — manages central locking, lighting, wipers, and window control. The instrument cluster receives data from nearly every other ECU to drive the gauges and warning lights. The HVAC module manages climate control. The airbag module sits on the high-speed bus for safety reasons but also communicates crash severity to the BCM for door unlocking and hazard light activation.
>
> And connecting them all: the gateway ECU. It's the central nervous system's switchboard."

**PPT Content:**
```
ECU NETWORK MAP

HIGH-SPEED CAN (Powertrain/Chassis):
-- ECM: Engine Control Module (engine speed, torque, temperature)
-- TCU: Transmission Control Unit (gear, shift commands)
-- ABS/ESC: Anti-lock Brakes / Stability Control (wheel speeds)
-- EPS: Electric Power Steering (steering torque, angle)
-- Airbag Module (crash detection, deployment)

LOW-SPEED CAN (Body/Comfort):
-- BCM: Body Control Module (lights, locks, wipers, windows)
-- Instrument Cluster (gauges, warning lights, odometer)
-- HVAC Module (temperature, fan, blend door)
-- Seat Module (position, heating, memory)
-- Infotainment (audio, navigation, phone)

GATEWAY ECU:
-- Bridges all networks
-- Routes messages between buses
-- Provides diagnostic access (OBD-II port)
-- Gateway fault = entire vehicle communication breakdown
```

---

#### Slide 13: What ECUs Share on the Network
**Visual:** Message flow diagram showing specific data shared: ECM broadcasts RPM and coolant temp; ABS broadcasts wheel speeds; instrument cluster receives from everyone; gateway routes between buses

**Instructor Narration:**
> "Why do these ECUs need to talk to each other? Because no system works in isolation. The ABS module needs engine torque data from the ECM to coordinate traction control. The transmission needs wheel speed data from the ABS to decide when to shift. The instrument cluster needs data from EVERYONE to update the driver. The airbag module needs crash deceleration AND seat position AND seatbelt status to decide how hard to deploy the airbags.
>
> Think about what happens during a simple hard braking event. The ABS module detects wheel lock-up and begins pulsing the brakes. It sends this information to the ESC module, the ECM (reduce engine torque), the brake lights (flash rapidly for emergency braking), and the instrument cluster (display ABS warning). All of that communication happens on CAN bus in milliseconds. If the bus fails, the coordination fails, and each system has to fall back to its own safe mode — which is rarely as effective."

**PPT Content:**
```
DATA SHARING ON THE NETWORK

ECM broadcasts:     Engine RPM, Coolant temp, Throttle position,
                    Engine torque, Fuel consumption
-- Used by: TCU, instrument cluster, HVAC, ESC

ABS/ESC broadcasts: Individual wheel speeds, Brake pressure,
                    Yaw rate, Lateral acceleration
-- Used by: ECM, TCU, EPS, instrument cluster

BCM broadcasts:     Door status, Light status, Ignition state,
                    Ambient temperature, Rain sensor
-- Used by: Instrument cluster, HVAC, airbag module

Instrument Cluster: RECEIVES from nearly every ECU
                    Displays everything the driver needs to see

Hard braking example — CAN messages in milliseconds:
ABS --> ECM: "Reduce torque NOW"
ABS --> BCM: "Flash brake lights"
ABS --> Cluster: "Show ABS active"
ABS --> ESC: "Wheel slip data"
```

---

#### Slide 14: CAN Protocol Summary — The Key Numbers
**Visual:** Clean summary table with all critical CAN specifications for technician reference

**Instructor Narration:**
> "Before we move to fault diagnosis, let me give you the reference card. These are the numbers you need to remember for CAN bus diagnostics. Recessive voltage: both lines at 2.5 volts. Dominant voltage: CAN-H at 3.5, CAN-L at 1.5. Termination: 60 ohms total at OBD-II port. High-speed bus: 500 kilobits per second. Low-speed bus: 125 kilobits per second. Maximum 8 bytes of data per message. OBD-II pins: 6 for CAN-H, 14 for CAN-L. Write these down. You'll use them for the rest of your career."

**PPT Content:**
```
CAN BUS REFERENCE CARD

Voltage Levels:
   Recessive:  CAN-H = 2.5V    CAN-L = 2.5V    (Diff = 0V)
   Dominant:   CAN-H = 3.5V    CAN-L = 1.5V    (Diff = 2.0V)

Termination:
   Each end: 120 ohm
   Total at OBD-II: ~60 ohm

Bus Speed:
   High-speed CAN: 500 kbps (powertrain, chassis, safety)
   Low-speed CAN:  125 kbps (body, comfort)

Message Frame:
   Max data: 8 bytes per message
   Error checking: CRC + ACK in every frame
   Priority: Lower ID = Higher priority

OBD-II Pins:
   Pin 6:  CAN-H (High-speed CAN)
   Pin 14: CAN-L (High-speed CAN)
   Pin 4:  Chassis ground
   Pin 16: Battery positive

WRITE THESE DOWN. You will use them for your entire career.
```

---

### **DEVELOPMENT PART 2: Network Faults & Oscilloscope Capture** (Slides 15-19, ~20 minutes)

**Narrative Voice:** Diagnostic and investigative. "When things go wrong on the network..."

---

#### Slide 15: U-Codes — Network Communication DTCs
**Visual:** Scan tool screen showing multiple U-codes: U0100, U0121, U0155, U0300. Each code expanded to show its meaning.

**Instructor Narration:**
> "Remember the DTC categories from Week 2? P-codes for powertrain, B-codes for body, C-codes for chassis. The fourth category — U-codes — is for network communication faults. These are the codes that appear when ECUs lose contact with each other.
>
> U0100: Lost Communication with ECM. This doesn't mean the engine controller is broken. It means the ECU that SET this code stopped receiving messages from the ECM. Maybe the ECM failed. Maybe the CAN bus has a wiring fault. Maybe the gateway failed. U-codes tell you WHICH conversation stopped, but not WHY. That's your job to figure out.
>
> Common U-codes you'll see: U0100 — lost comm with ECM. U0121 — lost comm with ABS. U0140 — lost comm with BCM. U0155 — lost comm with instrument cluster. U0300 — internal control module software incompatibility. When you see multiple U-codes across many modules, think CAN bus fault first, individual ECU fault second."

**PPT Content:**
```
U-CODES: NETWORK COMMUNICATION DTCs

Format: Uxxxx
   U = Network Communication
   Second digit: 0 = generic, 1 = manufacturer-specific

Common U-codes:
   U0100: Lost Communication with ECM/PCM
   U0101: Lost Communication with TCM
   U0121: Lost Communication with ABS
   U0122: Lost Communication with Vehicle Dynamics Control
   U0140: Lost Communication with BCM
   U0151: Lost Communication with Restraints (Airbag)
   U0155: Lost Communication with Instrument Cluster
   U0300: Internal Control Module Software Incompatibility
   U0401: Invalid Data Received from ECM/PCM

DIAGNOSTIC LOGIC:
   One U-code in one module = Possible single ECU fault
   Multiple U-codes in MANY modules = CAN bus wiring/termination fault
   U-codes after ECU replacement = Coding/programming issue
```

---

#### Slide 16: Bus-Off Condition — When an ECU Gives Up
**Visual:** Diagram showing an ECU's error counter incrementing with each transmission error. At 256 errors, the ECU enters "Bus-Off" state and disconnects from the network.

**Instructor Narration:**
> "Every CAN controller has a built-in error management system. It keeps two counters: a transmit error counter and a receive error counter. Every time a transmission fails — wrong acknowledgment, CRC mismatch, bit error — the counter increments. If the counter reaches 256, the CAN controller enters 'bus-off' state. The ECU voluntarily disconnects itself from the bus to prevent its errors from corrupting everyone else's communication.
>
> This is actually a safety feature. Imagine a faulty ECU that keeps sending corrupted messages. Without bus-off, it would drag down the entire network. With bus-off, it removes itself, and the rest of the network recovers.
>
> But from a diagnostic perspective, bus-off is serious. An ECU in bus-off state is completely silent — it can't send or receive. Your scan tool may not be able to communicate with it at all. You'll see it as a 'module not responding' error. The fix is usually: find what's causing the errors (often a wiring problem), fix it, then power-cycle the ECU to reset its error counters."

**PPT Content:**
```
BUS-OFF CONDITION

CAN Error Management:
   Every CAN controller has error counters
   Transmit Error Counter (TEC) + Receive Error Counter (REC)

Error States:
   ERROR ACTIVE:   TEC < 128, REC < 128  (normal operation)
   ERROR PASSIVE:  TEC >= 128 OR REC >= 128  (reduced participation)
   BUS-OFF:        TEC >= 256  (ECU disconnects from bus)

What causes bus-off?
   -- Wiring fault on CAN-H or CAN-L
   -- Termination problem
   -- ECU internal CAN controller fault
   -- Excessive bus load from a malfunctioning node

Diagnostic signs:
   -- Module not responding to scan tool
   -- U-codes in OTHER modules: "Lost communication with [module]"
   -- Module resets/recovers briefly after power cycle

Fix:
   1. Identify root cause of errors (usually wiring)
   2. Repair wiring fault
   3. Power cycle ECU to reset error counters
   4. Clear DTCs across all modules
```

---

#### Slide 17: Common CAN Bus Faults
**Visual:** Four fault diagrams side by side: (1) CAN-H shorted to CAN-L, (2) Open CAN-H wire, (3) Missing termination resistor, (4) Faulty ECU dragging bus voltage. Each with expected oscilloscope waveform or resistance measurement.

**Instructor Narration:**
> "Let's look at the faults you'll actually encounter. Number one: CAN-H shorted to CAN-L. The two wires touch each other — maybe a crushed connector, rodent damage, or a pinched wire. The differential voltage collapses to zero. No communication possible. You'll measure near-zero ohms between pin 6 and pin 14.
>
> Number two: Open CAN-H or CAN-L. One wire breaks — a corroded connector, a broken splice. The bus may still work partially because some nodes can fall back to single-wire mode, but communication becomes unreliable. You'll see intermittent U-codes.
>
> Number three: Missing termination. If one ECU at the bus end is disconnected or its internal termination resistor fails, you'll measure 120 ohms instead of 60. The bus may still work at low speeds but fails under heavy traffic due to signal reflections.
>
> Number four: A faulty ECU pulling the bus voltage to an incorrect level — 'dragging down the bus.' This is the sneakiest fault because it affects all communication but the guilty ECU might not set its own code. The diagnostic approach is to disconnect ECUs one by one until the bus recovers."

**PPT Content:**
```
COMMON CAN BUS FAULTS

1. CAN-H SHORTED TO CAN-L
   Cause: Crushed connector, rodent damage, pinched wire
   Symptom: Total communication loss, all warning lights
   Resistance: ~0 ohm between pin 6 and pin 14
   Waveform: Flat line, no differential signal

2. OPEN CAN-H OR CAN-L
   Cause: Corroded connector, broken splice, cut wire
   Symptom: Intermittent U-codes, partial communication
   Resistance: May read higher than 60 ohm
   Waveform: Asymmetric or absent on one channel

3. MISSING TERMINATION
   Cause: Disconnected ECU at bus end, failed internal resistor
   Symptom: Intermittent errors under heavy bus load
   Resistance: ~120 ohm (one termination missing)
   Waveform: Ringing/overshoot on signal edges

4. FAULTY ECU DRAGGING BUS DOWN
   Cause: Internal ECU CAN transceiver failure
   Symptom: Multiple U-codes, bus errors, one ECU in bus-off
   Resistance: Normal (60 ohm) — fault is active, not passive
   Diagnosis: Disconnect ECUs one by one until bus recovers
```

---

#### Slide 18: Oscilloscope CAN Capture
**Visual:** Annotated oscilloscope screenshot showing CAN-H (Channel 1, yellow) and CAN-L (Channel 2, blue) waveforms. Key voltage levels labeled: CAN-H at 3.5V dominant / 2.5V recessive, CAN-L at 1.5V dominant / 2.5V recessive. A single message frame visible with bits distinguishable.

**Instructor Narration:**
> "The oscilloscope is your most powerful tool for CAN bus diagnosis. Connect Channel 1 to CAN-H and Channel 2 to CAN-L at the OBD-II port. Set your timebase to see individual messages — typically 200 microseconds per division for high-speed CAN.
>
> A healthy CAN bus looks like this. The yellow trace is CAN-H, moving between 2.5V and 3.5V. The blue trace is CAN-L, moving between 2.5V and 1.5V — the mirror image. They move in opposite directions. When CAN-H goes up, CAN-L goes down — that's the differential signal. Between messages, both lines rest at 2.5V.
>
> What are you looking for? Clean, sharp transitions. Consistent voltage levels. Both channels present and symmetrical. If CAN-H is present but CAN-L is flat at 2.5V, you've got an open CAN-L wire. If both channels show the same voltage — moving together instead of apart — the wires are shorted. If the edges are rounded or there's ringing, suspect a termination issue. The scope tells you things the scan tool cannot."

**PPT Content:**
```
OSCILLOSCOPE CAN CAPTURE

Setup:
   Channel 1 (Yellow): CAN-H  (OBD-II Pin 6)
   Channel 2 (Blue):   CAN-L  (OBD-II Pin 14)
   Ground:             Chassis ground (OBD-II Pin 4 or 5)
   Timebase:           200 us/div for message view
                       50 us/div for bit-level view
   Voltage:            1V/div, centered at 2.5V

Healthy waveform:
   CAN-H: 2.5V (recessive) swings UP to 3.5V (dominant)
   CAN-L: 2.5V (recessive) swings DOWN to 1.5V (dominant)
   Both channels: Mirror images of each other
   Clean, sharp transitions, consistent voltage levels

What to look for:
   Missing channel = Open wire on that line
   Both channels same direction = Short between CAN-H and CAN-L
   Ringing/overshoot at edges = Termination problem
   Asymmetric voltage levels = Faulty transceiver in one ECU
   No waveform at all = Bus completely dead or shorted
```

---

#### Slide 19: Service Interval Reset — Why Electronic Reset Matters
**Visual:** Scan tool screen showing service interval menu: Oil Life, Brake Pad Wear, DPF Soot Load, Inspection Timer. Each with a reset option.

**Instructor Narration:**
> "Let me connect CAN bus knowledge to something you'll do on almost every service visit: the service interval reset. Modern cars don't just remind you to change oil every 10,000 kilometres. They calculate oil life based on actual driving conditions — temperature, RPM, load, fuel quality, short trips versus motorway driving. The ECM tracks all of this and decrements an oil life counter. When it reaches zero, the service light comes on.
>
> The same applies to brake pad wear — an actual sensor measures pad thickness and counts down. DPF soot loading — the ECM monitors pressure differential across the particulate filter. Inspection timers — the BCM counts days and kilometres since the last service reset.
>
> After you complete a service, you MUST reset these counters. If you don't, the customer drives away with the service light still on and thinks you didn't do the job. Or worse — the car enters a forced regeneration cycle or a service mode it shouldn't be in.
>
> Every reset is done through the OBD-II port, using the scan tool, talking to the ECUs over CAN bus. The tool sends a specific message to the ECM or BCM saying 'service completed, reset counter.' It's a CAN bus conversation, and now you understand what's happening when you press that button."

**PPT Content:**
```
SERVICE INTERVAL RESET

Why electronic reset?
   Modern vehicles calculate service intervals dynamically:
   -- Oil life: Based on RPM, temperature, load, fuel quality
   -- Brake pad wear: Electrical sensor measures remaining thickness
   -- DPF soot counter: Differential pressure across filter
   -- Inspection timer: Days and km since last coded reset

Resetting requires scan tool communication via CAN bus:
   Scan tool --> OBD-II port --> CAN bus --> Target ECU
   Tool sends: "Reset service counter [type]"
   ECU responds: "Counter reset confirmed"

Common resets you will perform:
   -- Oil service / oil life monitor
   -- Brake pad wear indicator
   -- DPF regeneration counter
   -- Inspection due date/km
   -- Tyre pressure sensor re-learn
   -- Battery management system (after battery replacement)

ALWAYS reset after service completion
-- Customer sees service light off = job looks professional
-- Failure to reset = customer complaint, repeat visit
```

---

### **PRACTICAL: Hands-On Network Diagnostics** (Slides 20-24, ~90 minutes)

**Narrative Voice:** Workshop instructor mode — clear, sequential, safety-aware.

---

#### Slide 20: Practical Overview & Safety
**Visual:** Workshop bench setup showing: multimeter, oscilloscope (if available), scan tool, OBD-II adapter, vehicle on level ground with ignition accessible

**Instructor Narration:**
> "We're heading to the workshop for four exercises. Exercise 1: Measure CAN bus termination resistance at the OBD-II port. Exercise 2: Capture or analyse CAN bus waveforms with an oscilloscope. Exercise 3: Read and interpret U-codes with a scan tool. Exercise 4: Perform a service interval reset on a real vehicle. Work in your pairs from this week. Each exercise takes about 20 minutes. I'll demonstrate each one first, then you perform it. Document your measurements — you'll need them for the debrief."

**PPT Content:**
```
PRACTICAL SESSION — 90 MINUTES

Exercise 1 (20 min): CAN Bus Termination Measurement
-- Measure resistance between OBD-II Pin 6 and Pin 14
-- Document: resistance value, interpretation

Exercise 2 (20 min): CAN Waveform Capture & Analysis
-- Oscilloscope on CAN-H and CAN-L (or analyse captured images)
-- Document: voltage levels, waveform quality

Exercise 3 (25 min): U-Code Diagnosis
-- Full scan (all modules) with scan tool
-- Identify and interpret all U-codes found
-- Determine: symptom codes vs. root cause

Exercise 4 (25 min): Service Interval Reset
-- Perform oil service reset
-- Perform inspection reset
-- Verify reset was successful

SAFETY:
-- Ignition OFF for resistance measurements
-- No disconnecting ECU connectors without instruction
-- Handle OBD-II connector gently — bent pins = expensive
```

---

#### Slide 21: Exercise 1 — Termination Resistance Measurement
**Visual:** Step-by-step photo sequence: (1) Locate OBD-II port, (2) Identify Pin 6 and Pin 14 on pinout diagram, (3) Set multimeter to resistance/ohms, (4) Insert probes into pins, (5) Read value, (6) Interpret result

**Instructor Narration:**
> "Exercise 1. This is the first test every network diagnostic should begin with. Turn the ignition completely OFF — this is important because powered ECUs will give you a false resistance reading. Locate the OBD-II port. Set your multimeter to the ohms range. Insert one probe into pin 6 — CAN-H. Insert the other probe into pin 14 — CAN-L. Read the value. Write it down.
>
> Expected: approximately 60 ohms. Acceptable range: 55 to 65 ohms. If you read 120 ohms, one termination resistor is missing. If you read significantly less than 60, you may have a partial short. If you read zero or near-zero, CAN-H and CAN-L are shorted together. If you read infinite resistance, the bus is open — no termination present at all.
>
> I'll demonstrate on this vehicle, then each pair does it independently."

**PPT Content:**
```
EXERCISE 1: TERMINATION RESISTANCE MEASUREMENT

Procedure:
1. Turn ignition OFF (key out, all systems powered down)
2. Locate OBD-II port (under dashboard, driver's side)
3. Identify Pin 6 (CAN-H) and Pin 14 (CAN-L)
4. Set multimeter to RESISTANCE (ohms)
5. Insert red probe into Pin 6, black probe into Pin 14
6. Read and record the value
7. Compare to expected values

Interpretation:
   55-65 ohm  = NORMAL (both terminations present)
   ~120 ohm   = ONE termination missing
   > 200 ohm  = BOTH terminations missing or open bus
   < 40 ohm   = Partial short on bus
   ~0 ohm     = CAN-H shorted to CAN-L
   OL/Infinity = Open circuit — no bus continuity

RECORD YOUR MEASUREMENT: _________ ohm
INTERPRETATION: _______________________
```

---

#### Slide 22: Exercise 2 — CAN Waveform Analysis
**Visual:** If oscilloscope available: setup photo with probes connected to OBD-II breakout. If not: printed waveform captures (healthy, shorted, open, missing termination) for comparison analysis.

**Instructor Narration:**
> "Exercise 2. If we have an oscilloscope available, connect Channel 1 to CAN-H at Pin 6 and Channel 2 to CAN-L at Pin 14. Ground clip to Pin 4 or Pin 5. Turn the ignition ON — the ECUs will start communicating. Set your timebase to 200 microseconds per division and voltage scale to 1 volt per division.
>
> You should see the mirror-image waveform we discussed: CAN-H swinging up from 2.5V to 3.5V while CAN-L swings down from 2.5V to 1.5V. The bus will be busy — you'll see continuous message traffic.
>
> If we don't have scopes for everyone, I've printed four waveform captures: a healthy bus, a shorted bus, an open CAN-L wire, and a bus with missing termination. Your job is to identify which is which and explain what voltage anomaly gives it away. Write your analysis in your notebook."

**PPT Content:**
```
EXERCISE 2: CAN WAVEFORM ANALYSIS

WITH OSCILLOSCOPE:
Setup:
   CH1 (Yellow) --> OBD-II Pin 6 (CAN-H)
   CH2 (Blue)   --> OBD-II Pin 14 (CAN-L)
   Ground       --> OBD-II Pin 4 (chassis ground)
   Timebase: 200 us/div     Voltage: 1V/div

Procedure:
   1. Connect probes with ignition OFF
   2. Turn ignition ON (engine off is fine)
   3. Observe waveform — both channels should be active
   4. Verify voltage levels match specification
   5. Capture/screenshot the waveform

WITHOUT OSCILLOSCOPE (waveform analysis exercise):
   Identify 4 printed waveforms:
   A: Healthy CAN bus
   B: CAN-H shorted to CAN-L
   C: Open CAN-L wire
   D: Missing termination (ringing on edges)

RECORD: Voltages observed or waveform identification
```

---

#### Slide 23: Exercise 3 — U-Code Diagnosis
**Visual:** Scan tool full-system scan results showing DTCs across multiple modules, with U-codes highlighted

**Instructor Narration:**
> "Exercise 3 — the one that ties theory to real diagnostic practice. Connect your scan tool to the OBD-II port. Perform a FULL SYSTEM SCAN — not just engine codes. You want to scan every module the tool can reach: ECM, TCM, ABS, BCM, airbag, instrument cluster, HVAC, steering, gateway — everything.
>
> Document every DTC you find. Pay special attention to U-codes — list them separately. For each U-code: which module set it? Which module did it lose communication with? Is the code current or stored?
>
> Now analyse the pattern. If you see U0100 in the ABS module, U0100 in the BCM, and U0100 in the instrument cluster — all saying 'lost communication with ECM' — that points to an ECM problem or a CAN bus wiring fault between the ECM and the rest of the network. If you see U-codes across every module, that's a bus-wide problem. If you see only one U-code in one module, that's likely a localised ECU issue. The pattern tells the story."

**PPT Content:**
```
EXERCISE 3: U-CODE DIAGNOSIS

Procedure:
1. Connect scan tool to OBD-II port
2. Perform FULL SYSTEM SCAN (all modules)
3. Record ALL DTCs found — every module
4. Separate U-codes from P/B/C codes
5. For each U-code, record:
   -- Which module SET the code?
   -- Which module is it ABOUT? (lost comm with ___?)
   -- Is code CURRENT or STORED/HISTORICAL?
6. Analyse the pattern

Diagnostic logic:
   PATTERN A: Same U-code in MANY modules
   --> Problem is with the MODULE they all lost contact with
       OR a bus wiring fault isolating that module

   PATTERN B: MANY DIFFERENT U-codes in MANY modules
   --> Bus-wide fault: wiring, termination, or gateway

   PATTERN C: ONE U-code in ONE module
   --> Localised: that specific module's connection or the
       target module itself

RECORD ALL FINDINGS IN YOUR NOTEBOOK
```

---

#### Slide 24: Exercise 4 — Service Interval Reset
**Visual:** Step-by-step scan tool screenshots: (1) Select vehicle, (2) Navigate to Service menu, (3) Select Oil Service Reset, (4) Confirm reset, (5) Verify cluster shows reset complete

**Instructor Narration:**
> "Exercise 4 — the skill you'll use on nearly every service visit. Using your scan tool, perform a service interval reset on the workshop vehicle. The exact menu path depends on the vehicle manufacturer and your scan tool brand, but the general procedure is: select the vehicle make and model, navigate to the Service or Maintenance menu, select the specific counter you want to reset — oil service, inspection, brake pad wear — and confirm the reset.
>
> After the reset, verify it worked. Turn the ignition on and check the instrument cluster. The service indicator should show the new interval — full oil life percentage, next service distance, or whatever the manufacturer uses. If the indicator didn't reset, something went wrong — wrong procedure, wrong module addressed, or a communication fault. Try again.
>
> I want each pair to perform at least two different resets: the oil service counter and the general inspection timer. Document the before and after readings."

**PPT Content:**
```
EXERCISE 4: SERVICE INTERVAL RESET

General procedure (varies by manufacturer and scan tool):
1. Connect scan tool to OBD-II port
2. Turn ignition ON (engine off)
3. Select vehicle: Make, Model, Year
4. Navigate to: Service / Maintenance / Reset menu
5. Select reset type:
   -- Oil Service Reset
   -- Inspection Due Reset
   -- (If available: Brake Pad, DPF, Battery)
6. Follow on-screen prompts — confirm reset
7. VERIFY: Turn ignition off, then on again
8. Check instrument cluster:
   -- Service light should be OFF
   -- Service interval should show FULL (100% or max km)

Perform at LEAST two resets:
   Reset 1: Oil service counter
   Reset 2: Inspection timer

RECORD:
   Before reset: Service indicator showed ___________
   After reset: Service indicator shows ___________

If reset fails: Note the error and try alternative procedure
```

---

### **WRAP-UP: Consolidation & Key Takeaways** (Slides 25-28, ~15 minutes)

**Narrative Voice:** Authoritative summary. Reinforce the diagnostic mindset.

---

#### Slide 25: Practical Debrief — Share Your Findings
**Visual:** Blank table template for recording group findings: termination resistance, waveform observations, U-codes found, service reset results

**Instructor Narration:**
> "Let's debrief. Each pair, report your termination resistance measurement. What did you read? What does it tell us about this vehicle's CAN bus? Now, what did you see on the waveforms — or which printed waveform did you identify as faulty and why? What U-codes, if any, did you find during the full system scan? And finally — did your service resets complete successfully? Any issues?
>
> This is important: in a real workshop, you'd be making these exact measurements and recording these exact findings on a job card. The ability to measure, interpret, and document network diagnostics separates a parts-swapper from a diagnostic technician."

**PPT Content:**
```
PRACTICAL DEBRIEF

Share your results:

TERMINATION RESISTANCE:
   Your measurement: _____ ohm
   Interpretation: ____________________

CAN WAVEFORM:
   Voltage levels observed/identified: _____________
   Healthy or faulty? If faulty, what type? _________

U-CODES FOUND:
   Module: _________ Code: _______ Meaning: __________
   Module: _________ Code: _______ Meaning: __________
   Pattern analysis: ______________________________

SERVICE INTERVAL RESET:
   Reset 1 type: _________ Result: _______________
   Reset 2 type: _________ Result: _______________
```

---

#### Slide 26: The Network Diagnostic Workflow
**Visual:** Flowchart: Multiple warning lights on --> Scan all modules --> Check for U-codes --> Measure termination (60 ohm?) --> Oscilloscope waveform --> Isolate fault (disconnect ECUs) --> Repair wiring or replace ECU --> Clear codes, retest

**Instructor Narration:**
> "Let me give you the workflow you'll follow for every CAN bus problem you encounter in your career. Step 1: Multiple warning lights on simultaneously? Think network first. Step 2: Full system scan — every module, every code. Step 3: Analyse U-codes — which modules are affected, which module is the common denominator? Step 4: Measure termination resistance at the OBD-II port — is it 60 ohms? Step 5: Oscilloscope on CAN-H and CAN-L — are the waveforms healthy? Step 6: If the bus is faulty, isolate — disconnect ECUs one at a time and recheck until the bus recovers. Step 7: Repair the wiring fault or replace the faulty ECU. Step 8: Clear all codes across all modules and road test. Follow this workflow and you'll solve network faults that stump other technicians."

**PPT Content:**
```
NETWORK DIAGNOSTIC WORKFLOW

STEP 1: Multiple warning lights?
        --> Suspect network fault before individual systems

STEP 2: Full system scan (all modules)
        --> Record ALL DTCs, focus on U-codes

STEP 3: Analyse U-code pattern
        --> One module missing = ECU or connection fault
        --> Many modules down = bus-wide fault

STEP 4: Measure termination resistance
        --> 60 ohm = OK | 120 ohm = missing termination
        --> 0 ohm = short | OL = open bus

STEP 5: Oscilloscope CAN-H and CAN-L
        --> Verify voltage levels and waveform quality

STEP 6: Isolate fault
        --> Disconnect ECUs one by one, recheck bus

STEP 7: Repair
        --> Fix wiring, replace connector, or replace ECU

STEP 8: Clear ALL codes, ALL modules, road test
        --> Verify no codes return
```

---

#### Slide 27: What You Learned Today
**Visual:** Checklist with check marks

**Instructor Narration:**
> "Let's take stock. This morning you understood CAN bus as a concept. Now you understand it at the wire level. You can explain differential signaling — what CAN-H and CAN-L do, what voltages they swing between, and why differential signaling rejects noise. You can describe a CAN message frame and explain how priority works. You know the difference between high-speed and low-speed CAN. You can measure termination resistance and interpret the result. You can read and interpret U-codes. You can recognise common CAN bus faults. And you can perform a service interval reset through the CAN network.
>
> This is professional-level network diagnostic knowledge. Most technicians in the field learned this on the job over years. You've compressed it into one session."

**PPT Content:**
```
DAY 38 RECAP — YOU CAN NOW:

-- Explain CAN differential signaling (CAN-H/CAN-L voltage levels)
-- Describe the CAN message frame structure (SOF to EOF)
-- Explain message priority (lower ID = higher priority)
-- Distinguish high-speed CAN (500 kbps) from low-speed (125 kbps)
-- Explain termination resistors and measure 60 ohm at OBD-II
-- Map ECU types across the vehicle network (ECM, TCU, BCM, ABS...)
-- Read and interpret U-codes (network communication DTCs)
-- Identify common CAN faults (short, open, missing termination)
-- Interpret CAN bus oscilloscope waveforms
-- Perform service interval resets via scan tool
-- Follow the network diagnostic workflow

Network faults create CASCADING symptoms.
You now know how to find the ONE root cause.
```

---

#### Slide 28: Day 39 Preview
**Visual:** Image of a vehicle undergoing a pre-delivery inspection — technician with checklist walking around vehicle, checking lights, tyres, fluid levels, scan tool connected

**Instructor Narration:**
> "Tomorrow, Day 39, we shift from diagnosing faults to preventing them. We're covering pre-delivery inspections, multi-point health checks, and customer handover procedures. This is the quality control process that ensures every vehicle leaving the workshop is safe, fully functional, and professionally presented. You'll combine everything you've learned over eight weeks into a structured vehicle inspection. Bring your scan tool, your multimeter, and your A-game. We're bringing it all together."

**PPT Content:**
```
DAY 39 PREVIEW: VEHICLE INSPECTION & CUSTOMER HANDOVER

-- Pre-delivery inspection (PDI) checklist
-- Multi-point health check procedure
-- Combining ALL diagnostic skills into one workflow
-- Scan tool final check: codes clear, systems operational
-- Fluid levels, tyre condition, lights, wipers
-- Professional customer handover process

Bring everything: Scan tool, multimeter, notebook

Two days left. You're almost there.
```

---

## Assessment Checkpoint

**Formative (not graded):**
- Termination resistance measurement: Correctly measure and interpret the value at the OBD-II port (target: 55-65 ohms)
- U-code interpretation: Given three U-codes from different modules, identify whether the fault is bus-wide or module-specific
- Waveform identification: Correctly identify a healthy CAN waveform versus a faulty one (shorted, open, or missing termination)
- Service interval reset: Successfully perform at least two different service counter resets and verify completion on the instrument cluster

---

## Key Takeaways

1. CAN bus uses differential signaling: CAN-H and CAN-L swing in opposite directions around 2.5V, making the system highly noise-resistant
2. Lower message ID means higher priority — safety-critical data always transmits first
3. Termination resistance at the OBD-II port should be approximately 60 ohms — this is your first diagnostic check for any network problem
4. Multiple warning lights appearing simultaneously almost always indicates a network fault, not multiple system failures
5. U-codes tell you WHICH conversation stopped, not WHY — the pattern across modules reveals the root cause
6. The oscilloscope shows you what the scan tool cannot: the actual physical health of the CAN bus wires
7. Service interval resets are CAN bus conversations between the scan tool and the ECU — understanding the network makes routine service procedures make sense

---

## Preparation for Day 39

**Instructor prep:**
- Prepare a vehicle for multi-point inspection (ideally with a few minor faults planted: low tyre, dim bulb, low washer fluid)
- Print pre-delivery inspection checklists (one per learner)
- Ensure all scan tools are charged and updated
- Prepare customer handover role-play scenario cards
- Have a clean vehicle available for handover practice (washed, vacuumed)

**Learner prep:**
- Review all diagnostic tools and their functions (scan tool, multimeter, oscilloscope)
- Bring all equipment: scan tool, multimeter, inspection torch, notebook
- Review the 8 vehicle systems from Day 1 — tomorrow you inspect all of them
