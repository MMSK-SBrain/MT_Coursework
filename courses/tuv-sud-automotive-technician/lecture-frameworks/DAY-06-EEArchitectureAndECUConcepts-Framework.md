---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 2
week_title: "Speaking Electricity"
day_number: 6
session_title: "Why Electronics Run the Car — E/E Architecture & ECU Concepts"
duration_minutes: 180
theory_practice: "50:50"
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 6: Why Electronics Run the Car — E/E Architecture & ECU Concepts
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (90 min theory + 90 min practical)
**Approach:** Architecture-First — See the System Before the Maths
**PPT Target:** 26-28 slides
**Week:** 2 of 8 — "Speaking Electricity"

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Explain the sensor-ECU-actuator pattern and identify it in any vehicle system
- Name and locate at least 6 major ECUs in a modern vehicle (ECM, TCU, BCM, ABS module, airbag module, instrument cluster)
- Describe why CAN bus exists and what problem it solves
- Locate the OBD-II port on a vehicle and connect a scan tool
- Read and interpret Diagnostic Trouble Codes (DTCs) and live data PIDs from a scan tool
- Distinguish between basic code readers and professional diagnostic equipment

**This is Day 1 of Week 2.** Learners completed Week 1 with mechanical orientation, safety, measurement, and fasteners. They know WHAT the car's systems are — now they discover WHO controls them. This session deliberately comes BEFORE Ohm's Law (Day 7) so that electrical theory has a concrete reason to exist.

---

## Connection to Prior Knowledge

Build from Week 1:
- Day 1: Learners identified 8 vehicle systems and saw "100+ ECUs" mentioned
- Day 1, Slide 5: "The Mechatronic Shift" introduced the idea that electronics run the modern car
- Day 1, Slide 8: The electrical/electronic system was called "The Nervous System"
- Day 4: Learners used digital instruments (multimeters, callipers) — they've already worked with electronic tools
- Day 5: Consolidation session confirmed understanding of all Week 1 content

**Bridge:** "Last week you met the car physically — you touched the engine, looked under the chassis, measured bolts. But who TELLS the engine how much fuel to inject? Who DECIDES when to shift gears? Who FIRES the airbag in a crash? This week we find out. And today, we meet the brains."

---

## Why Architecture Comes FIRST (Pedagogical Note for Instructor)

If Ohm's Law were taught on Day 6 (the first day of the "electricity week"), it would be abstract mathematics disconnected from the car. Learners would memorise V = I x R without knowing WHY it matters.

By teaching E/E architecture first, we give learners a concrete mental model:
- "There are 30+ computers in this car, all talking over a network."
- "Each one reads sensors and drives actuators."
- "I need to be able to plug in a scan tool and talk to them."

THEN, on Day 7, when we introduce Ohm's Law, voltage, current, and resistance, the learner thinks: "I need this to understand those systems I saw yesterday." Motivation precedes abstraction.

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: The Electronic Car** (Slides 1-5, ~15 minutes)

**Narrative Voice:** Revelatory, building curiosity. Frame the entire week.

---

#### Slide 1: Title & Week 2 Opening
**Visual:** A modern vehicle rendered as a transparent shell with glowing circuit traces, ECU boxes, and sensor points illuminated throughout — resembling a neural network overlaid on a car

**Instructor Narration:**
> "Welcome to Week 2. Last week was called 'Meet the Machine.' This week is called 'Speaking Electricity.' And here's why: every system you studied last week — engine, brakes, steering, transmission, HVAC — every single one of them is controlled by electronics. The mechanical car still exists under the skin. But the brain, the decision-maker, the thing that actually runs it all? That's electronic. This week, you learn to speak its language."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 2: Speaking Electricity
Day 6: Why Electronics Run the Car — E/E Architecture & ECU Concepts

"Every system is controlled by electronics.
This week, you learn to speak their language."
```

---

#### Slide 2: Week 2 Roadmap
**Visual:** Horizontal timeline showing 5 days of Week 2, Day 6 highlighted. Each day has an icon and short label.

**Instructor Narration:**
> "Here's your Week 2 at a glance. Today — Day 6 — we see the big picture: what's an ECU, how many are there, how do they talk, and how do YOU talk to them with a scan tool. Day 7, we learn the electrical fundamentals — voltage, current, resistance, Ohm's Law — because you need those to understand the circuits these ECUs live in. Day 8, wiring diagrams — reading the blueprints of the electrical system. Day 9, we do real measurements with a multimeter. Day 10, we consolidate and test everything.
>
> Notice the order: architecture FIRST, maths SECOND. By the end of today, you'll have a reason to care about Ohm's Law tomorrow."

**PPT Content:**
```
WEEK 2: SPEAKING ELECTRICITY

Day 6: E/E Architecture & ECU Concepts (TODAY)
— The brains of the car, networks, diagnostics

Day 7: Ohm's Law & Electrical Fundamentals
— Voltage, current, resistance — the language of circuits

Day 8: Wiring Diagrams & Circuit Reading
— Reading the electrical blueprints

Day 9: Electrical Measurement Practicals
— Multimeter skills on real circuits

Day 10: Consolidation & Assessment
— Putting it all together

TODAY: See the system. TOMORROW: Learn the maths behind it.
```

---

#### Slide 3: From Mechanical to Mechatronic — The Timeline
**Visual:** Horizontal timeline from 1970 to 2025 showing key milestones: first ECU (1968 VW fuel injection), OBD-I (1988), OBD-II mandatory (1996), CAN bus mandatory (2008), 100+ ECUs (2015), domain controllers (2020+)

**Instructor Narration:**
> "Let me take you through a quick history. In 1968, Volkswagen put the first electronic fuel injection controller in a production car. One ECU. Fast forward to 1996 — every car sold in the US and Europe must have an OBD-II diagnostic port. By 2008, CAN bus becomes mandatory in all new vehicles. And today? A modern luxury car can have over 150 ECUs, 5 kilometres of wiring, and more lines of software code than a fighter jet.
>
> This didn't happen because engineers love complexity. It happened because electronics can do things mechanics cannot: react in milliseconds, adapt to conditions, diagnose their own faults, and meet emissions regulations that would be physically impossible with pure mechanical control."

**PPT Content:**
```
THE ELECTRONIC EVOLUTION

1968: First production ECU (VW electronic fuel injection)
1980s: Engine management ECUs become standard
1988: OBD-I introduced (manufacturer-specific)
1996: OBD-II mandatory (standardised diagnostics)
2004: CAN bus becomes dominant in-vehicle network
2008: CAN bus mandatory in EU (Euro 5)
2015: Typical car = 70-100 ECUs
2020+: Domain controllers, Ethernet, OTA updates
2025: 150+ ECUs, 100+ million lines of code

WHY? Electronics react faster, adapt smarter, diagnose themselves.
```

---

#### Slide 4: Today's Plan
**Visual:** Four blocks arranged horizontally — Theory Block 1, Theory Block 2, Practical Block, Wrap-Up — with time allocations and icons

**Instructor Narration:**
> "Here's how today breaks down. First, we learn the fundamental pattern that drives EVERY electronic system in the car: sensor, ECU, actuator. Then we meet the major ECUs by name and location. Second, we look at how those ECUs communicate — CAN bus — and how you, the technician, access them through OBD-II. After the theory, we go hands-on: you'll hunt for ECUs on a real car, plug in a scan tool, read fault codes, and watch live data. By the end of today, you'll have talked to a car's brain."

**PPT Content:**
```
TODAY'S PLAN (180 minutes)

BLOCK 1 (35 min): The Sensor-ECU-Actuator Pattern + ECU Types
— The building block of every electronic system

BLOCK 2 (25 min): CAN Bus, OBD-II & Diagnostic Tools
— How ECUs talk and how YOU talk to them

BLOCK 3 (75 min): Hands-On Practical
— ECU location hunt, OBD-II scan tool, live data

BLOCK 4 (15 min): Wrap-Up & Day 7 Preview
— Consolidation, key takeaways, prep for Ohm's Law

+ 15 min break between theory and practical
```

---

#### Slide 5: The Question That Drives Everything
**Visual:** Three dramatic photos side by side: (1) a fuel injector firing, (2) an airbag deploying, (3) an automatic transmission shifting — each with the question "WHO decides?" overlaid

**Instructor Narration:**
> "I want you to think about three moments. A fuel injector fires for exactly 3.2 milliseconds — not 3.1, not 3.3. An airbag deploys within 30 milliseconds of a collision being detected. An automatic transmission shifts from 3rd to 4th at precisely the right engine speed, load, and throttle position. WHO decides? WHO controls the timing? WHO processes the data?
>
> Not the driver. Not a mechanical linkage. An ECU. A small computer, about the size of a paperback book, processing sensor data and commanding actuators thousands of times per second. That's what today is about."

**PPT Content:**
```
WHO DECIDES?

Who fires the fuel injector at exactly 3.2 ms?
— The Engine Control Module (ECM)

Who deploys the airbag within 30 ms of impact?
— The Airbag Control Module (ACM)

Who shifts the transmission at the perfect moment?
— The Transmission Control Unit (TCU)

The answer is always the same: AN ECU.
Electronic Control Unit — the car's brain(s).

Today you meet them.
```

---

### **DEVELOPMENT PART 1: Sensor-ECU-Actuator & ECU Types** (Slides 6-14, ~35 minutes)

**Narrative Voice:** Systematic, building from one pattern to many. Use the body analogy consistently.

---

#### Slide 6: The Fundamental Pattern — Sensor, ECU, Actuator
**Visual:** Large, clean diagram showing: SENSOR (eye icon) --signal--> ECU (brain icon) --command--> ACTUATOR (muscle icon). Arrows clearly labeled "input signal" and "output command." Below, a real-world example: throttle position sensor --> ECM --> fuel injector.

**Instructor Narration:**
> "Every electronic system in the car — every single one — follows this exact same pattern. A SENSOR measures something in the physical world: temperature, pressure, position, speed. It converts that measurement into an electrical signal. That signal goes to an ECU — an Electronic Control Unit — which is a computer. The ECU reads the signal, applies its programming, makes a decision, and sends a command to an ACTUATOR. The actuator does something physical: opens a valve, fires an injector, engages a solenoid.
>
> Sensor, ECU, actuator. Input, brain, output. This is THE building block. Once you understand this pattern, you understand the logic of every system in the car. Let me give you a concrete example."

**PPT Content:**
```
THE FUNDAMENTAL PATTERN

SENSOR ──signal──> ECU ──command──> ACTUATOR
(measures)         (decides)        (acts)

EXAMPLE: Fuel Injection
Throttle position sensor → ECM → Fuel injector
"Driver wants 50% throttle" → "Calculate fuel needed" → "Inject 3.2 ms"

EXAMPLE: ABS Braking
Wheel speed sensor → ABS module → Brake pressure modulator
"Right front locking up" → "Reduce pressure" → "Release, reapply, release..."

EXAMPLE: Cooling
Coolant temp sensor → ECM → Radiator fan relay
"Engine at 105°C" → "Too hot, activate fan" → "Fan ON"

EVERY electronic system follows this pattern.
```

---

#### Slide 7: Sensors — The Car's Senses
**Visual:** Grid of 8 common automotive sensors with photos and labels: throttle position sensor, coolant temperature sensor, MAP sensor, O2 sensor, wheel speed sensor, crankshaft position sensor, knock sensor, ambient temperature sensor

**Instructor Narration:**
> "Let's look at the input side. Sensors are the car's eyes, ears, and nerve endings. A modern car has 200 or more sensors. They measure everything: how hot the engine is, how fast each wheel is spinning, how much air is entering the intake, what position the throttle is at, whether exhaust gases are rich or lean, whether a crash just occurred.
>
> Most sensors work on simple electrical principles — which is exactly what we'll study this week. A thermistor changes resistance with temperature. A Hall effect sensor generates a voltage pulse as a magnet passes it. A piezoelectric sensor generates voltage when squeezed. Don't worry about the physics yet — that's Day 7. For now, just know: sensors convert physical reality into electrical signals."

**PPT Content:**
```
SENSORS — THE CAR'S SENSES

A modern car has 200+ sensors measuring:

Temperature: Coolant, intake air, exhaust, ambient, oil
Position: Throttle, crankshaft, camshaft, steering angle, pedal
Pressure: MAP (manifold), fuel rail, tyre (TPMS), brake
Speed: Wheel speed (x4), vehicle speed, engine RPM
Gas composition: O2 / lambda, NOx, particulate
Acceleration: Crash sensors, yaw rate, lateral G
Other: Rain, light level, seat occupancy, proximity (parking)

KEY PRINCIPLE: Sensors convert physical quantities
into electrical signals that ECUs can read.
```

---

#### Slide 8: ECUs — The Car's Brains
**Visual:** Photo of a real ECU removed from a vehicle — a metal or plastic box with a multi-pin connector. Annotated cutaway showing the circuit board inside with microprocessor, memory chips, and connector pins labeled.

**Instructor Narration:**
> "Now the brain. An ECU is a small computer. Open one up and you'll find a circuit board with a microprocessor, memory for storing its programme and calibration data, input circuits to read sensors, output circuits to drive actuators, and a communication interface to talk to other ECUs.
>
> It looks simple from the outside — just a metal box with one or two large connectors. But inside, it's processing thousands of calculations per second. The Engine Control Module alone might read 30+ sensor inputs and control 20+ actuators, recalculating fuel injection, ignition timing, and emissions parameters every single engine revolution. At 6,000 RPM, that's 100 times per second. For each cylinder."

**PPT Content:**
```
ECU — ELECTRONIC CONTROL UNIT

What's inside:
• Microprocessor (CPU) — runs the control software
• ROM/Flash — stores the programme (firmware)
• RAM — working memory for calculations
• EEPROM — stores learned values and fault codes
• Input conditioning circuits — reads sensor signals
• Output driver circuits — powers actuators
• Communication interface — CAN bus transceiver
• Power supply regulation — converts 12V to 5V/3.3V

Physical form:
• Metal or plastic housing (for heat dissipation + protection)
• One or more multi-pin connectors (20-pin to 154-pin)
• Typically sealed against moisture and vibration
• Mounted in engine bay, cabin, or near the system it controls
```

---

#### Slide 9: Actuators — The Car's Muscles
**Visual:** Grid of 6 common actuators with photos: fuel injector, ignition coil, solenoid valve, relay, electric motor (e.g., stepper motor), EGR valve

**Instructor Narration:**
> "The output side. Actuators are the muscles — they make things happen in the physical world. When the ECU decides to inject fuel, it sends an electrical pulse to the fuel injector, which opens a valve for a precise duration. When the ECU decides to spark, it triggers the ignition coil. When the ABS module needs to release brake pressure, it opens a solenoid valve in the hydraulic unit.
>
> Actuators come in many forms: solenoids that open and close, electric motors that spin or step to a position, relays that switch high-current loads, and heating elements. But they all have one thing in common: they receive an electrical command from an ECU and perform a physical action."

**PPT Content:**
```
ACTUATORS — THE CAR'S MUSCLES

Common actuator types:

Solenoid valves: Fuel injectors, EGR valve, EVAP purge valve
  — Electrically open/close a passage for fluid or gas

Ignition coils: Coil-on-plug, coil packs
  — Convert 12V to 40,000V for spark generation

Relays: Fan relay, fuel pump relay, glow plug relay
  — Low-current signal switches high-current load

Electric motors: Throttle body motor, HVAC blend doors, EPS
  — Rotate or step to a commanded position

Heating elements: O2 sensor heater, glow plugs, heated mirrors
  — Convert electrical energy to thermal energy

KEY PRINCIPLE: Actuators convert ECU commands
into physical actions.
```

---

#### Slide 10: The Pattern in Action — Complete Example
**Visual:** Full system diagram of the engine management system showing: 6-8 sensors on the left feeding into the ECM in the centre, which outputs to 4-5 actuators on the right. Each signal path labeled.

**Instructor Narration:**
> "Let me put it all together with one complete system — engine management. The ECM reads the crankshaft position sensor to know the engine's exact rotational position. It reads the throttle position sensor to know how much power the driver wants. It reads the MAP sensor for intake manifold pressure, the intake air temperature sensor, the coolant temperature sensor, and the O2 sensors in the exhaust.
>
> With all that data, the ECM calculates: how much fuel to inject, when to fire the spark, what ignition advance angle to use, whether to open the EGR valve, how far to open the idle air control. It then sends commands to each actuator — injectors, coils, EGR solenoid, idle motor — all within one engine revolution. And it does this continuously, adapting to every change in driving condition.
>
> This is the sensor-ECU-actuator pattern applied to just ONE system. Every other system in the car follows the same logic."

**PPT Content:**
```
ENGINE MANAGEMENT — THE PATTERN IN ACTION

SENSORS (Input):                ECM                  ACTUATORS (Output):
Crankshaft position  ─────>  ┌──────────┐  ─────>  Fuel injectors (x4-x8)
Camshaft position    ─────>  │  ENGINE   │  ─────>  Ignition coils (x4-x8)
Throttle position    ─────>  │  CONTROL  │  ─────>  Idle air control valve
MAP sensor           ─────>  │  MODULE   │  ─────>  EGR solenoid
Intake air temp      ─────>  │  (ECM)    │  ─────>  EVAP purge valve
Coolant temp         ─────>  │           │  ─────>  Variable valve timing
O2 sensors (x2-x4)  ─────>  │           │  ─────>  Turbo wastegate actuator
Knock sensor         ─────>  └──────────┘

Processing speed: Thousands of calculations per engine revolution
Adaptation: Continuously adjusting to speed, load, temperature, altitude
```

---

#### Slide 11: Meet the Major ECUs — Part 1
**Visual:** Vehicle outline with ECU locations highlighted and callout boxes. Focus on powertrain ECUs: ECM (engine bay), TCU (on or near transmission), PCM label if combined.

**Instructor Narration:**
> "Now let's meet them by name. The most important ECU in any car is the ECM — Engine Control Module. Also called the Engine ECU, engine computer, or Motronic if it's a Bosch unit. It controls everything related to the engine: fuel injection, ignition timing, idle speed, emissions systems, and often the electronic throttle. It's usually located in the engine bay or on the firewall.
>
> Next: the TCU — Transmission Control Unit. This controls automatic transmission shift points, shift quality, torque converter lockup, and gear selection logic. In some vehicles, the ECM and TCU are combined into a single unit called the PCM — Powertrain Control Module. Same functions, one box."

**PPT Content:**
```
MAJOR ECU #1: ECM — Engine Control Module
Also called: Engine ECU, EMS, Motronic, PCM (if combined with TCU)
Location: Engine bay, firewall, or air box area
Controls: Fuel injection, ignition, idle, emissions, throttle
Sensors: 20-40 inputs
Actuators: 15-25 outputs
Why it matters: The most complex and critical ECU in any ICE vehicle

MAJOR ECU #2: TCU — Transmission Control Unit
Also called: TCM, gearbox ECU, Mechatronic unit (in DSG/DCT)
Location: On or integrated into the transmission housing
Controls: Shift timing, shift quality, gear selection, lockup
Sensors: Input/output speed, ATF temp, selector position
Communication: Constantly exchanges data with ECM via CAN
```

---

#### Slide 12: Meet the Major ECUs — Part 2
**Visual:** Vehicle outline focusing on body and chassis ECUs: BCM (under dashboard or behind kick panel), ABS/ESC module (engine bay near brake master cylinder), airbag module (centre console area), instrument cluster (behind dashboard).

**Instructor Narration:**
> "The BCM — Body Control Module — is the housekeeper. It controls everything you think of as comfort and convenience: interior and exterior lighting, central locking, power windows, windscreen wipers, horn, heated seats, and alarm system. It's usually hidden behind the dashboard or a kick panel.
>
> The ABS module — sometimes called the ABS/ESC module or hydraulic control unit — sits in the engine bay near the brake master cylinder. It controls anti-lock braking, traction control, and electronic stability control by individually modulating brake pressure at each wheel.
>
> The airbag module — also called the SRS (Supplemental Restraint System) module or crash sensor — monitors crash sensors and decides when to fire airbags and seatbelt pretensioners. This ECU is safety-critical. It must work within 30 milliseconds or not at all.
>
> And the instrument cluster — yes, it's an ECU too. It receives data from other ECUs over CAN bus and displays speed, RPM, fuel level, temperature, and warning indicators."

**PPT Content:**
```
MAJOR ECU #3: BCM — Body Control Module
Location: Behind dashboard or kick panel
Controls: Lighting, locks, windows, wipers, horn, alarm
Characteristic: The "housekeeper" — manages comfort and convenience

MAJOR ECU #4: ABS/ESC Module
Location: Engine bay, near brake master cylinder
Controls: Anti-lock brakes, traction control, stability control
Characteristic: Modulates individual wheel brake pressure

MAJOR ECU #5: Airbag Module (SRS / ACM)
Location: Centre of cabin (under centre console or dashboard)
Controls: Airbag deployment, seatbelt pretensioners
Characteristic: Must deploy within 30 ms — safety-critical

MAJOR ECU #6: Instrument Cluster
Location: Behind dashboard, facing driver
Function: Displays data received from other ECUs via CAN bus
Characteristic: Also stores mileage (odometer)
```

---

#### Slide 13: How Many ECUs? — The Modern Car's Electronic Census
**Visual:** Infographic showing a modern premium car with 40+ ECU boxes placed at their actual locations, each labeled. A counter in the corner shows "100+ ECUs." Below, a comparison bar: economy car (~30 ECUs), mid-range car (~70 ECUs), premium car (~100-150 ECUs).

**Instructor Narration:**
> "So how many ECUs are in a modern car? An economy car: around 30. A mid-range family car: 50 to 70. A premium luxury car or a modern EV: 100 to 150 or more. Let me list some you might not expect: the seat memory module remembers your seat position. The rain/light sensor module controls automatic wipers and headlights. The tyre pressure monitoring system has a small computer in each wheel. The reversing camera has its own image processing unit. The keyless entry system, the parking sensors, the adaptive headlight levelling — each one has its own ECU.
>
> And every one of them needs to communicate. Imagine if each ECU had its own dedicated wiring to every other ECU it needed to talk to. With 100 ECUs, you'd need thousands of individual wires. That brings us to the next topic: why the CAN bus exists."

**PPT Content:**
```
HOW MANY ECUs IN A MODERN CAR?

Economy car:           ~30 ECUs
Mid-range car:         ~50-70 ECUs
Premium / EV:          ~100-150+ ECUs

ECUs you might not expect:
• Seat memory module            • Parking sensor module
• Rain/light sensor             • Rear-view camera processor
• TPMS receiver                 • Adaptive headlight module
• Keyless entry module          • Battery management (EV/hybrid)
• Trailer hitch module          • Start-stop controller
• Steering column module        • Heated steering wheel module

QUESTION: If every ECU needed its own wire to every
other ECU... how many wires would that require?
```

---

#### Slide 14: The Wiring Problem — Why Networks Exist
**Visual:** Two diagrams side by side. LEFT: "Point-to-point" wiring — a spaghetti mess of individual wires connecting 10 ECUs with 45 connections drawn. RIGHT: "Network" — the same 10 ECUs connected by a single pair of wires (a CAN bus backbone), clean and orderly. A label says "Same communication, 90% less wiring."

**Instructor Narration:**
> "Look at this. On the left, ten ECUs connected point-to-point — each one needs a dedicated wire to every other one. That's 45 connections for just ten ECUs. For 100 ECUs, it would be nearly 5,000 connections. The weight alone would be absurd, never mind the cost, complexity, and failure points.
>
> On the right, the same ten ECUs connected by ONE shared network — two wires. Every ECU connects to the same pair of wires and broadcasts its data. Other ECUs listen and grab the data they need. That's the CAN bus concept. It solved the wiring problem and made the modern electronic car possible. Let's look at how it works."

**PPT Content:**
```
THE WIRING PROBLEM

POINT-TO-POINT WIRING:
10 ECUs = 45 separate connections
50 ECUs = 1,225 connections
100 ECUs = 4,950 connections

Weight: Hundreds of kilograms of extra copper
Cost: Thousands of additional connectors
Reliability: Every connection is a potential failure point

THE SOLUTION: A SHARED NETWORK

CAN BUS (Controller Area Network):
All ECUs share TWO wires (CAN-High + CAN-Low)
Each ECU broadcasts messages with a unique ID
Other ECUs listen for the messages they need
Result: Same communication, fraction of the wiring
```

---

### **DEVELOPMENT PART 2: CAN Bus, OBD-II & Diagnostics** (Slides 15-19, ~25 minutes)

**Narrative Voice:** Practical, tool-oriented. Bring it to the technician's daily reality.

---

#### Slide 15: CAN Bus — The Car's Nervous System Network
**Visual:** Simplified CAN bus topology diagram showing a twisted pair of wires running as a backbone with multiple ECUs tapped into it. Signal waveform shown on the side — CAN-H and CAN-L mirror signals. Termination resistors (120 ohm) at each end labeled.

**Instructor Narration:**
> "CAN stands for Controller Area Network. It was invented by Bosch in 1986 and is now the most widely used in-vehicle network in the world. Here's how it works conceptually: two wires — CAN-High and CAN-Low — run through the vehicle like a backbone. Every ECU that needs to communicate taps into these two wires. When an ECU wants to send data, it puts a message on the bus with a unique ID number. Every other ECU on the bus sees the message. But only the ECUs that care about that particular ID will read and use the data.
>
> Think of it like a group radio channel. Everyone can hear everything. Each message has a subject line — the ID — and you only pay attention to the subjects relevant to your job. A modern car might have 2 to 4 separate CAN buses for different speed requirements: a high-speed powertrain CAN, a medium-speed comfort CAN, and a diagnostic CAN."

**PPT Content:**
```
CAN BUS — Controller Area Network

Invented: Bosch, 1986
Standard: ISO 11898
Physical: Two-wire twisted pair (CAN-H + CAN-L)
Speed: 125 kbps (low-speed) to 1 Mbps (high-speed)
Termination: 120 ohm resistor at each end of the bus

How it works:
1. ECU places a MESSAGE on the bus (broadcast)
2. Message has a unique ID (e.g., 0x7E0 = ECM)
3. ALL ECUs on the bus receive the message
4. Only ECUs that need that data process it
5. Priority: Lower ID number = higher priority

Typical CAN bus layout in a modern car:
• Powertrain CAN (high-speed 500 kbps): ECM, TCU, ABS
• Comfort CAN (low-speed 125 kbps): BCM, seats, mirrors
• Diagnostic CAN: Connected to OBD-II port
• Infotainment CAN: Head unit, speakers, phone interface
```

---

#### Slide 16: Beyond CAN — Other Networks (Awareness Only)
**Visual:** Layered diagram showing the hierarchy of in-vehicle networks: LIN (simple, cheap, low-speed) at the bottom, CAN in the middle, CAN FD and FlexRay above, and Automotive Ethernet at the top. Each labeled with typical use cases.

**Instructor Narration:**
> "CAN bus is the workhorse, but it's not the only network in the car. LIN — Local Interconnect Network — is a simpler, cheaper, slower network used for things like mirror adjustment motors, seat position, and rain sensors. It uses a single wire and is controlled by a CAN-connected ECU acting as a master.
>
> At the top end, newer vehicles use CAN FD — CAN with Flexible Data-rate — which is faster and carries bigger messages. Some premium vehicles used FlexRay for safety-critical systems like active suspension. And the newest frontier is Automotive Ethernet — used for high-bandwidth data like camera images for ADAS systems.
>
> You don't need to know the details of all these right now. Just be aware: CAN is the most common, but you may encounter other network types as vehicles get more advanced."

**PPT Content:**
```
IN-VEHICLE NETWORKS — THE FAMILY

LIN (Local Interconnect Network):
• Single wire, 20 kbps, cheap
• Mirrors, seats, rain sensor, interior lighting
• Master-slave: controlled by a CAN-connected ECU

CAN (Controller Area Network):
• Two wires, 125-1000 kbps
• Powertrain, chassis, body — the standard
• Most common in-vehicle network worldwide

CAN FD (CAN with Flexible Data-rate):
• Same wires, up to 5 Mbps, larger messages
• Replacing traditional CAN in newer vehicles

Automotive Ethernet (100BASE-T1):
• Single twisted pair, 100 Mbps to 1 Gbps
• Cameras, radar, ADAS, OTA updates, diagnostics

FOR NOW: Focus on CAN — you'll encounter it daily.
```

---

#### Slide 17: OBD-II — The Technician's Window Into the ECU World
**Visual:** Photo of an OBD-II port (16-pin DLC connector) with each relevant pin labeled. Photo showing the standard location under the dashboard on the driver's side. A scan tool plugged into the port.

**Instructor Narration:**
> "OBD-II. On-Board Diagnostics, version 2. This is the most important thing you'll learn today for your daily work as a technician. Since 1996, every car sold has a standardised 16-pin diagnostic connector — called the DLC, Data Link Connector — located within reach of the driver's seat, usually under the dashboard on the driver's side.
>
> When you plug a scan tool into this port, you can talk to the car's ECUs. You can read Diagnostic Trouble Codes — DTCs — which tell you what faults the ECUs have detected. You can view live data — real-time sensor readings called PIDs. You can clear fault codes after a repair. You can run actuator tests. You can check readiness monitors for emissions testing.
>
> This port is your primary access point to the electronic car. You will use it every single day of your career."

**PPT Content:**
```
OBD-II — ON-BOARD DIAGNOSTICS, VERSION 2

Standard: SAE J1962 (connector), ISO 15031 (protocol)
Mandatory: All vehicles sold in EU since 2001 (petrol) / 2004 (diesel)
Connector: 16-pin DLC (Data Link Connector)
Location: Within 60 cm of steering column, accessible from driver's seat

What you can do via OBD-II:
1. READ DTCs (Diagnostic Trouble Codes) — stored faults
2. CLEAR DTCs — after repair
3. VIEW LIVE DATA (PIDs) — real-time sensor values
4. CHECK READINESS MONITORS — emissions test preparation
5. FREEZE FRAME DATA — snapshot at time of fault
6. RUN ACTUATOR TESTS — command outputs (manufacturer-specific)

STANDARDISED DTC FORMAT:
P0301 = Powertrain / System 03 (Ignition) / Cylinder 1 Misfire
```

---

#### Slide 18: Reading DTCs — The Language of Faults
**Visual:** DTC structure breakdown diagram: First character (P/B/C/U), second character (0 = generic, 1 = manufacturer), third character (system), fourth-fifth characters (specific fault). Three example DTCs decoded below.

**Instructor Narration:**
> "Diagnostic Trouble Codes follow a standardised format. The first letter tells you the system: P for Powertrain, B for Body, C for Chassis, U for Network/Communication. The second character: 0 means it's a generic, industry-standard code — the same on every car. 1 means it's manufacturer-specific. The third character identifies the subsystem: fuel and air, ignition, emissions, speed control, transmission. The last two digits identify the specific fault.
>
> So if your scan tool shows P0300 — that's a Powertrain, Generic, Ignition system, Random/Multiple Cylinder Misfire Detected. P0171 is a Powertrain, Generic, Fuel/Air Metering, System Too Lean Bank 1. These codes don't tell you WHAT to replace — they tell you what the ECU DETECTED. Your job is to use the code as a starting point for diagnosis, not as a parts-ordering instruction."

**PPT Content:**
```
DTC STRUCTURE — DECODING FAULT CODES

Format: X 0 0 0 0
        |  | | | |
        |  | | +-+-- Specific fault number (00-99)
        |  | +------ Sub-system (1-9)
        |  +-------- 0 = Generic (SAE), 1 = Manufacturer-specific
        +----------- System: P=Powertrain, B=Body, C=Chassis, U=Network

SUB-SYSTEM CODES (for P-codes):
1/2 = Fuel & air metering
3 = Ignition / misfire
4 = Emissions controls
5 = Vehicle speed / idle
6 = Computer / output circuits
7/8 = Transmission

EXAMPLES:
P0300 = Random/multiple cylinder misfire detected
P0171 = System too lean (Bank 1)
P0420 = Catalyst system efficiency below threshold
C0035 = Left front wheel speed sensor circuit

A DTC is a STARTING POINT — not a diagnosis.
```

---

#### Slide 19: Diagnostic Equipment Overview
**Visual:** Four diagnostic tools arranged from simple to complex: (1) basic OBD-II code reader (~$30), (2) mid-range scan tool like Launch or Autel (~$500), (3) professional dealer-level tool like VCDS/ODIS/ISTA (~$2000+), (4) oscilloscope for waveform analysis. Each with a brief capability summary.

**Instructor Narration:**
> "Let me show you the tool spectrum. At the basic end, you have code readers — small handheld devices, sometimes even phone apps via a Bluetooth dongle. They read and clear generic DTCs and show basic live data. Cost: $30 to $100. Good enough for a home mechanic.
>
> Mid-range scan tools from brands like Launch, Autel, or Foxwell give you access to manufacturer-specific codes, live data graphing, actuator tests, and service resets. $300 to $1500. This is what many independent workshops use daily.
>
> Professional, dealer-level tools — VW's ODIS, BMW's ISTA, Mercedes' XENTRY — these are the full-access tools. They can code new modules, update software, perform guided fault-finding, and access every function the car has. $2000 and up, often with annual subscription fees.
>
> And finally, the oscilloscope — this shows you the actual electrical waveform of a signal over time. When a scan tool says 'sensor fault' but the code doesn't tell you enough, the oscilloscope shows you exactly what the signal looks like. We'll use oscilloscopes later in the course. Today, you'll work with a mid-range scan tool."

**PPT Content:**
```
DIAGNOSTIC TOOL SPECTRUM

LEVEL 1: Basic Code Reader ($30-$100)
• Read/clear generic DTCs
• Basic live data (RPM, coolant temp, speed)
• No manufacturer-specific access
• Good for: Quick fault check, home use

LEVEL 2: Mid-Range Scan Tool ($300-$1,500)
• Generic + manufacturer-specific DTCs
• Full live data with graphing
• Actuator tests, service resets (oil, brake pads)
• Good for: Independent workshops, daily use

LEVEL 3: Professional / Dealer Tool ($2,000+)
• Full system access, guided diagnostics
• Module coding, software updates, programming
• Brands: VCDS, ODIS (VW), ISTA (BMW), Techstream (Toyota)
• Good for: Complex diagnostics, module replacement

LEVEL 4: Oscilloscope ($500-$5,000)
• Shows actual signal waveforms over time
• Diagnoses sensor/actuator signal quality
• Essential for intermittent faults and CAN bus issues
```

---

### **PRACTICAL BLOCK: Hands-On ECU Hunt & Scan Tool** (Slides 20-24, ~75 minutes)

**Narrative Voice:** Workshop guide. Energetic, hands-on. Move between stations.

---

#### Slide 20: Practical Overview — Three Activities
**Visual:** Three station icons labeled: Station A (ECU Location Hunt), Station B (OBD-II Scan Tool), Station C (Diagnostic Tool Familiarisation). Timer showing 75 minutes total.

**Instructor Narration:**
> "Time to go hands-on. We have three practical activities. Activity 1: ECU Location Hunt — you'll work in pairs on a real vehicle and find, identify, and photograph at least 10 ECUs. I'll give you a checklist. Activity 2: OBD-II Scan Tool — you'll plug in a scan tool, read DTCs, view live data, and interpret what you see. Activity 3: Diagnostic Tool Familiarisation — I'll demo the professional tool and you'll explore its menus.
>
> We'll spend about 25 minutes on each activity, rotating between stations. Let me explain each one before we move to the workshop."

**PPT Content:**
```
PRACTICAL ACTIVITIES (75 minutes total)

ACTIVITY 1: ECU Location Hunt (25 min)
— Find and identify 10+ ECUs on a real vehicle
— Use the checklist provided
— Photograph each ECU location with your phone

ACTIVITY 2: OBD-II Scan Tool (25 min)
— Connect scan tool to OBD-II port
— Read DTCs (if any present)
— View live data PIDs: RPM, coolant temp, O2 voltage
— Clear codes (instructor guided)

ACTIVITY 3: Diagnostic Tool Familiarisation (25 min)
— Instructor demo of professional scan tool
— Explore menu structure
— View system topology (which ECUs are present)
— Introduction to actuator testing

RULES: Same as always — don't force anything, ask if unsure.
```

---

#### Slide 21: Activity 1 — ECU Location Hunt Checklist
**Visual:** Printable checklist with two columns: ECU Name and Location Found. 12 rows. Space for a photo or sketch for each. Vehicle outline diagram at the bottom for marking positions.

**Instructor Narration:**
> "Here's your ECU hunt checklist. I want you to find as many of these as you can. Some are easy — the instrument cluster is right in front of the driver. Some require you to look behind panels — the BCM is often behind the kick panel on the driver's side. The ABS module is usually in the engine bay near the brake master cylinder. The airbag module is under the centre console.
>
> Don't remove any panels unless I show you how first. Some ECUs you can identify by following wiring harnesses. Some have labels on the housing. Some you'll recognise by their connector size and location. Work in pairs. You have 25 minutes."

**PPT Content:**
```
ECU LOCATION HUNT — CHECKLIST

Find, identify, and mark the location of:

  ECU Name                           Location Found
  ─────────────────────────────────  ──────────────────
□ 1. ECM (Engine Control Module)     _________________
□ 2. TCU (Transmission Control)      _________________
□ 3. BCM (Body Control Module)       _________________
□ 4. ABS/ESC Module                  _________________
□ 5. Airbag Module (SRS)             _________________
□ 6. Instrument Cluster              _________________
□ 7. Steering Column Module          _________________
□ 8. Door Module (driver)            _________________
□ 9. Parking Assist Module           _________________
□ 10. HVAC Control Module            _________________

BONUS:
□ 11. Gateway Module                 _________________
□ 12. Headlight Control Module       _________________

Mark each location on the vehicle outline diagram.
```

**Instructor Action:** Distribute printed checklists. Assign vehicle bays to pairs. Guide learners to start at the engine bay and work methodically through the cabin. Assist with panel access if needed. Debrief after 25 minutes — which ECUs did each pair find? Which were hardest to locate?

---

#### Slide 22: Activity 2 — OBD-II Scan Tool Practical
**Visual:** Step-by-step photo sequence: (1) Locate OBD-II port, (2) Plug in scan tool, (3) Turn ignition to ON, (4) Select "Read DTCs" from menu, (5) Screen showing DTC list, (6) Select "Live Data," (7) Screen showing RPM, coolant temp, O2 voltage updating in real time.

**Instructor Narration:**
> "Now you talk to the car. Step one: find the OBD-II port. It's under the dashboard on the driver's side. Step two: plug in the scan tool — the connector only fits one way. Step three: turn the ignition to ON — you don't need to start the engine yet. Step four: on the scan tool, select 'Read DTCs.' The tool will communicate with the ECUs and retrieve any stored fault codes.
>
> If there are codes stored, write them down. We'll decode them together. Then switch to 'Live Data' and start the engine. Watch the RPM value — it should show idle speed. Watch coolant temperature — it should climb slowly from ambient toward operating temperature. Watch the O2 sensor voltage — it should oscillate between about 0.1 and 0.9 volts on a warmed-up engine. This is real-time data, straight from the ECU's sensors."

**PPT Content:**
```
OBD-II SCAN TOOL — STEP BY STEP

1. LOCATE the OBD-II port (under dashboard, driver's side)
2. PLUG IN the scan tool (connector has a key — one way only)
3. TURN IGNITION to ON (do not start engine yet)
4. SELECT "Read Fault Codes" / "Read DTCs"
5. RECORD any codes displayed (write them down)

6. SELECT "Live Data" / "Data Stream"
7. START the engine (if instructor says OK)
8. OBSERVE key PIDs:
   • Engine RPM — should read ~700-800 at idle
   • Coolant Temperature — rises from ambient to ~90°C
   • O2 Sensor Voltage — oscillates 0.1V to 0.9V
   • Intake Air Temperature — near ambient
   • Battery Voltage — should read 13.5-14.5V (engine running)

9. CLEAR CODES (only when instructor directs)

RECORD your observations on the worksheet provided.
```

**Instructor Action:** Set up one scan tool per pair. Walk learners through the first connection. Let them explore menus independently. Circulate to answer questions. If a vehicle has stored DTCs, use them as teaching moments — decode the DTC with the group. After 25 minutes, have each pair report one interesting PID reading.

---

#### Slide 23: Activity 3 — Professional Tool Demonstration
**Visual:** Screenshot of a professional diagnostic tool (e.g., VCDS or ISTA) showing the vehicle system topology screen — a graphical map of all ECUs installed, with communication status (green = OK, red = fault).

**Instructor Narration:**
> "Now I want to show you what the professional tools can do. This is [tool name — use whatever is available in your workshop]. Watch the screen as I connect. First, it automatically identifies the vehicle via the VIN. Then it scans every ECU on every network in the car and builds this topology map. Green means the ECU is communicating normally. Yellow means a warning. Red means a communication fault.
>
> I can click on any ECU and see its full fault memory, its software version, its hardware part number, and its live data. I can command actuator tests — watch, I'll cycle the radiator fan. I can view the measured values that a basic scan tool can't access — like individual cylinder fuel trim or turbo boost duty cycle.
>
> You won't need to master these tools on Day 6. But I want you to see what's possible, so you understand why learning electronics this week matters. By the end of this course, you'll be comfortable with these professional tools."

**Instructor Action:** Connect the professional tool to a vehicle. Project the screen to the class. Walk through the topology scan, selecting 3-4 ECUs and showing their data. Run one actuator test live (e.g., cycle fuel pump, flash headlights via BCM, or activate horn). Let learners ask questions. Allow those who finish Activities 1 and 2 early to explore the professional tool under guidance.

---

#### Slide 24: Practical Debrief — What Did You Find?
**Visual:** Empty table with columns: "Pair," "ECUs Found (count)," "Most Interesting DTC," "Most Interesting Live Data PID." Space for 6 pairs.

**Instructor Narration:**
> "Let's debrief. Each pair, tell me: how many ECUs did you find and identify? What was the hardest one to locate? Did your vehicle have any stored DTCs — and if so, what were they? What was the most interesting PID value you observed in live data?
>
> The point of this practical was to make the theory tangible. You now know that ECUs are real physical boxes bolted to the car. You know that you can talk to them through the OBD-II port. You know that fault codes give you a starting point for diagnosis. And you know that live data shows you what the car is actually doing right now, not just what it remembers from a past fault."

**Activity:**
- Each pair reports findings (2 min each)
- Instructor highlights interesting discoveries
- Common questions addressed:
  - "Why does one car have more ECUs than another?" (trim level, options)
  - "What if there are DTCs but the car seems fine?" (intermittent faults, pending codes)
  - "Can I damage anything with a scan tool?" (reading is safe; writing/coding requires care)

---

### **WRAP-UP: Consolidation & Day 7 Preview** (Slides 25-28, ~15 minutes)

**Narrative Voice:** Consolidating, forward-looking. Connect today to tomorrow.

---

#### Slide 25: The Big Picture — What You Learned Today
**Visual:** The sensor-ECU-actuator diagram from Slide 6 repeated at the top. Below it, a network diagram showing ECUs connected by CAN bus. Below that, an OBD-II port with a scan tool. Three layers, one story.

**Instructor Narration:**
> "Let's consolidate. Today you learned three things. First: every electronic system in the car follows the sensor-ECU-actuator pattern. Sensors measure, ECUs decide, actuators act. Second: all those ECUs communicate over a network called CAN bus — two wires carrying all the data. Third: you, the technician, access that network through the OBD-II port using a scan tool, and you read DTCs and live data to diagnose faults.
>
> That's the architecture of the electronic car. You now have a mental map of HOW the car's electronics are organised. Tomorrow, we learn the physics underneath it all."

**PPT Content:**
```
DAY 6 — THREE LAYERS OF UNDERSTANDING

LAYER 1: The Pattern
SENSOR ──> ECU ──> ACTUATOR
Every system, every time.

LAYER 2: The Network
ECU ──CAN bus──> ECU ──CAN bus──> ECU
All brains talking on shared wires.

LAYER 3: Your Access Point
OBD-II port ──> Scan tool ──> DTCs + Live Data
Your window into the electronic car.

You now understand the ARCHITECTURE.
Tomorrow you learn the PHYSICS.
```

---

#### Slide 26: Why This Matters for Your Career
**Visual:** Pie chart showing a typical modern workshop's work breakdown: 40% diagnostic/electronic, 35% mechanical repair, 15% maintenance/service, 10% bodywork/trim. The diagnostic slice is highlighted.

**Instructor Narration:**
> "Here's why today matters for your career. In a modern workshop, roughly 40% of all work involves electronics and diagnostics. That percentage grows every year. Technicians who can diagnose electronic faults are in high demand and command higher pay. Technicians who can only do mechanical work are increasingly limited in what they can handle.
>
> Everything you learn this week — architecture, Ohm's Law, wiring diagrams, measurement — is the foundation that makes you a diagnostician, not just a parts replacer. When a customer's check engine light is on, they need someone who can plug in, read the code, interpret the data, trace the circuit, and find the root cause. That's the technician you're becoming."

**PPT Content:**
```
WHY ELECTRONICS SKILLS MATTER

Modern workshop work breakdown:
• 40% — Diagnostics & electronic systems
• 35% — Mechanical repair (engine, transmission, brakes)
• 15% — Scheduled maintenance and service
• 10% — Body, trim, and accessories

TREND: Electronic work percentage grows every year.

Technician who can diagnose = HIGHER DEMAND, HIGHER PAY

This week's skills are not optional extras.
They are the core of modern automotive service.
```

---

#### Slide 27: Assessment Checkpoint
**Visual:** Clean quiz-style layout with 5 quick questions.

**Instructor Narration:**
> "Quick check. I'm going to ask five questions. Don't look at your notes — just think."

**PPT Content:**
```
CHECK YOUR UNDERSTANDING

1. What three elements make up the fundamental pattern
   of every electronic system in the car?

2. Name four major ECUs and state what each controls.

3. Why does CAN bus exist? What problem does it solve?

4. Where is the OBD-II port located in a vehicle?

5. A scan tool shows DTC P0171. What does the "P" mean?
   What does the "0" in the second position mean?

ANSWERS:
1. Sensor → ECU → Actuator
2. ECM (engine), TCU (transmission), BCM (body), ABS (brakes)
3. Replaces thousands of point-to-point wires with a shared network
4. Under the dashboard, driver's side, within 60 cm of steering column
5. P = Powertrain, 0 = Generic (industry-standard code)
```

---

#### Slide 28: Day 7 Preview — Ohm's Law & Electrical Fundamentals
**Visual:** A simple circuit diagram showing a battery, a wire, a resistor, and an ammeter — with V, I, and R labeled. The Ohm's Law triangle (V = I x R) shown prominently. A speech bubble says "Now you know WHY. Tomorrow you learn HOW."

**Instructor Narration:**
> "Tomorrow is Day 7 — Ohm's Law and Electrical Fundamentals. You'll learn about voltage, current, and resistance — the three quantities that describe every electrical circuit in the car. You'll learn Ohm's Law — V equals I times R — the single most important equation in automotive electrical work. And you'll learn about series and parallel circuits, because every wiring diagram you'll ever read is built from these two patterns.
>
> Here's what I want you to remember: today you learned that the car is full of electronic systems — sensors, ECUs, actuators, all connected by CAN bus. Tomorrow, you learn the electrical language those systems speak. Voltage is the push. Current is the flow. Resistance is the opposition. Get those three right, and every circuit in the car makes sense.
>
> Come ready to think. Bring your curiosity and a calculator."

**PPT Content:**
```
DAY 7 PREVIEW: OHM'S LAW & ELECTRICAL FUNDAMENTALS

What you'll learn:
• Voltage (V) — electrical pressure ("the push")
• Current (I) — electron flow ("the flow")
• Resistance (R) — opposition to flow ("the friction")
• Ohm's Law: V = I × R (the most important equation)
• Series circuits vs. parallel circuits
• How these concepts apply to real vehicle circuits

WHY IT MATTERS:
Today you saw the architecture.
Tomorrow you learn the physics underneath it.
Every sensor signal, every actuator command, every fault you'll
ever diagnose — they all come down to voltage, current, and resistance.

Bring: Curiosity + calculator.
```

---

## Assessment Checkpoint

**Formative (not graded):**
- ECU Location Hunt: correctly identify and locate at least 8 of 12 ECUs on the checklist
- OBD-II practical: successfully connect scan tool, read DTCs (or confirm "no faults stored"), and view at least 3 live data PIDs
- Verbal quiz (Slide 27): answer at least 3 of 5 questions correctly
- DTC decoding: given a DTC code, correctly identify the system letter (P/B/C/U) and whether it is generic or manufacturer-specific

---

## Key Takeaways

1. Every electronic system follows one pattern: SENSOR measures, ECU decides, ACTUATOR acts
2. A modern car contains 30-150+ ECUs — each a small computer controlling a specific system
3. CAN bus is a shared two-wire network that replaces thousands of individual connections
4. OBD-II gives technicians standardised access to read DTCs and live data from every vehicle
5. Diagnostic Trouble Codes are starting points for diagnosis, not parts-ordering instructions
6. Understanding the electronic architecture gives PURPOSE to the electrical theory that follows

---

## Preparation for Day 7

**Instructor prep:**
- Prepare basic circuit demonstration board (battery, switch, lamp, multimeter connections)
- Source Ohm's Law calculation worksheets with automotive examples (e.g., headlamp bulb resistance, injector coil current)
- Set up workbench with power supply, resistor kits, LED circuits, breadboards
- Print Ohm's Law reference cards for learners
- Ensure multimeters are calibrated and functional (one per pair minimum)
- Prepare "why does this matter" examples linking Day 6 architecture to Day 7 circuits (e.g., "the coolant temperature sensor is a thermistor — its resistance changes with temperature — tomorrow you'll learn what resistance means and how to measure it")

**Learner prep:**
- Review the sensor-ECU-actuator pattern — be able to draw it from memory
- Bring a calculator (phone calculator is acceptable)
- Review any DTCs recorded during today's practical — we may reference them tomorrow
