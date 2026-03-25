---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 7
week_title: "The Future & The Comfort"
day_number: 31
session_title: "Hybrid Architectures & EV Components"
duration_minutes: 180
theory_practice: "55:45"
exam_weight_marks: 16
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 31: Hybrid Architectures & EV Components
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (100 min theory + 80 min practical)
**Approach:** Architecture-First — Understand the Layout Before You Touch It
**PPT Target:** 26-28 slides
**Week:** 7 of 8 — "The Future & The Comfort"
**Exam Weight:** 16 marks

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Distinguish between series, parallel, series-parallel, PHEV, and full BEV architectures and explain the energy flow in each
- Identify the function of PMSM and induction motors in electric drivetrains
- Explain the role of the inverter, DC-DC converter, and on-board charger
- Describe HV battery pack construction: cell chemistry (NMC vs LFP), cell formats (pouch, prismatic, cylindrical), modules, and pack assembly
- Explain BMS functions: voltage/temperature/SOC monitoring, cell balancing, and contactor control
- Identify the pre-charge circuit purpose and operation
- Locate and identify HV components on a training vehicle or diagram, including the service disconnect

**Week 7 opens the electrification chapter.** Learners have spent six weeks on conventional ICE systems. This session bridges their mechanical knowledge into the high-voltage world. The goal is ARCHITECTURE UNDERSTANDING before tomorrow's HV safety protocols. They must know what the components ARE before learning how to work around them safely.

---

## Connection to Prior Knowledge

Build from:
- Week 3: Engine operation (ICE fundamentals — now the ICE becomes a generator in hybrids)
- Week 6: Transmission and power delivery (now electric motors deliver torque)
- Week 2: Electrical fundamentals (DC, AC, voltage, current — now at 400V+)
- Day 1: The 8 major vehicle systems (now adding a 9th: the HV powertrain)

**Bridge:** "You've spent six weeks learning how an engine makes power and how it gets to the wheels. This week, we add a second power source — electricity. And not the 12 volts you've been working with. We're talking 400 volts or more. By the end of today, you'll understand every component in a hybrid or electric drivetrain. Tomorrow, we learn how to stay alive while working near them."

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: The Electrification Imperative** (Slides 1-4, ~15 minutes)

**Narrative Voice:** Forward-looking, urgent, grounding. This is the future of their career.

---

#### Slide 1: Title & Week 7 Opening
**Visual:** Split image — left side shows a conventional engine bay, right side shows an EV motor compartment with orange HV cables. Week 7 banner across the top.

**Instructor Narration:**
> "Welcome to Week 7. This is the week everything changes. For six weeks, you've been learning the car as it has been for over a century — internal combustion, hydraulic systems, 12-volt electrics. This week, we step into the car as it will be for the next century. High voltage. Electric motors. Battery packs the size of a dining table. Climate systems that must work without engine heat. Safety systems getting smarter every year.
>
> The car of today and tomorrow. High voltage demands new respect. Climate control demands precision. Safety systems are getting smarter. Let's begin."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 7: The Future & The Comfort
Day 31: Hybrid Architectures & EV Components

"The car of today and tomorrow."

High voltage demands new respect.
Climate control demands precision.
Safety systems are getting smarter.
```

---

#### Slide 2: Why Electrification Matters — Now
**Visual:** Timeline graphic showing EU emissions regulations — 2020 (95 g/km CO2 fleet target), 2030 (55% reduction), 2035 (zero-emission new car sales). Include global EV sales growth chart.

**Instructor Narration:**
> "This isn't a future trend — it's happening right now. The European Union mandates that by 2035, all new cars sold must be zero-emission. That's nine years from today. Manufacturers are already shifting. In 2025, roughly one in four new cars sold in Europe was either a plug-in hybrid or a full EV.
>
> What does this mean for you? It means that within five years of starting your career, the majority of vehicles coming into your workshop will have a high-voltage system. You cannot be a technician in 2030 without understanding this technology. Today, we build that understanding."

**PPT Content:**
```
THE ELECTRIFICATION TIMELINE

2020: EU fleet target 95 g/km CO2
2025: ~25% of new EU car sales are PHEV or BEV
2030: 55% CO2 reduction target (EU)
2035: Zero-emission new car sales mandate (EU)

WHAT THIS MEANS FOR YOU:
- Hybrid/EV work is NOT optional — it's the default
- HV competence will be REQUIRED for technician certification
- Your career depends on mastering this technology
- Today = Day 1 of your EV education
```

---

#### Slide 3: The Electrification Spectrum
**Visual:** Horizontal spectrum bar from left to right: ICE (conventional) -> Mild Hybrid (48V) -> Full Hybrid (HEV) -> Plug-in Hybrid (PHEV) -> Battery Electric (BEV) -> Fuel Cell (FCEV). Each labeled with a representative vehicle image.

**Instructor Narration:**
> "Electrification is not all-or-nothing. It's a spectrum. On the left, the conventional petrol or diesel car you already know. Move right, and you add increasing amounts of electric power. A mild hybrid adds a small 48-volt motor-generator that assists the engine. A full hybrid can drive short distances on electricity alone. A plug-in hybrid has a bigger battery you can charge from the wall — 50 to 80 kilometres of pure electric range. Then the full battery electric vehicle — no engine at all. And at the far end, the fuel cell vehicle, which generates electricity from hydrogen.
>
> Today, we focus on the core architectures: series hybrid, parallel hybrid, series-parallel hybrid, PHEV, and BEV. These five cover over 95 percent of what you'll encounter."

**PPT Content:**
```
THE ELECTRIFICATION SPECTRUM

ICE -----> Mild Hybrid -----> Full Hybrid (HEV)
  Pure combustion    48V assist        Can drive on
  No electric drive  Belt starter-     electricity briefly
                     generator (BSG)   (1-3 km)

-----> Plug-in Hybrid (PHEV) -----> BEV -----> FCEV
  Larger battery           No engine       Hydrogen fuel cell
  EV range 50-80 km       100% electric   generates electricity
  External charging        200-600 km      Water is only emission
                           range

TODAY'S FOCUS: Series / Parallel / Series-Parallel / PHEV / BEV
```

---

#### Slide 4: Today's Plan
**Visual:** Three-block horizontal timeline: THEORY (100 min) — PRACTICAL (80 min). Theory split into "Hybrid Architectures" and "EV Components Deep Dive."

**Instructor Narration:**
> "Here's how today runs. First, we study the five hybrid and EV architectures — how energy flows in each one. Then we go deep into the key components: electric motors, inverter, DC-DC converter, on-board charger, and the battery pack with its BMS. After the theory, we go hands-on: identifying every HV component on a training vehicle or detailed diagram, mapping their locations, and dissecting a battery pack cutaway. By the end of today, you will know what every orange cable connects to and why."

**PPT Content:**
```
TODAY'S PLAN (180 minutes)

BLOCK 1 — THEORY (100 min)
  Part A: Hybrid Architectures (50 min)
    Series, Parallel, Series-Parallel, PHEV, BEV
  Part B: EV Component Deep Dive (50 min)
    Motors, Inverter, DC-DC, Charger, Battery Pack, BMS

BLOCK 2 — PRACTICAL (80 min)
  (1) HV component identification on training vehicle/diagram
  (2) HV component location mapping exercise
  (3) Battery pack cutaway/diagram analysis

+ 15 min wrap-up & Day 32 preview (HV Safety Protocols)
```

---

### **DEVELOPMENT PART A: Hybrid Architectures** (Slides 5-11, ~50 minutes)

**Narrative Voice:** Systematic, building from simplest to most complex. Use energy flow diagrams throughout.

---

#### Slide 5: Architecture 1 — Series Hybrid
**Visual:** Energy flow diagram: Fuel Tank -> ICE -> Generator -> Inverter -> Electric Motor -> Wheels. Battery shown as a buffer connected between Generator/Inverter and Motor. All mechanical connections as solid arrows, electrical as orange dashed arrows. Example vehicle: Nissan e-Power.

**Instructor Narration:**
> "Let's start with the simplest concept. In a series hybrid, the engine NEVER drives the wheels directly. The engine's only job is to turn a generator that produces electricity. That electricity either goes straight to the electric motor that drives the wheels, or it charges the battery for later use. The wheels are always driven by the electric motor.
>
> Think of it like a diesel-electric locomotive. The diesel engine doesn't connect to the wheels — it runs a generator, and the electric motors do the driving. Nissan's e-Power system works exactly this way. The advantage? The engine can run at its most efficient speed all the time, because it's mechanically decoupled from the wheels. The disadvantage? All the energy goes through two conversions — mechanical to electrical to mechanical — so there are efficiency losses at higher speeds.
>
> Series hybrids are excellent in city driving where stop-start traffic means the electric motor's instant torque and regenerative braking shine."

**PPT Content:**
```
ARCHITECTURE 1: SERIES HYBRID

Energy flow:
FUEL -> ENGINE -> GENERATOR -> [BATTERY] -> INVERTER -> MOTOR -> WHEELS

Key principle: Engine NEVER drives wheels directly
- Engine runs generator only
- Electric motor is the SOLE drive source
- Battery acts as energy buffer

Example: Nissan e-Power

ADVANTAGES:
+ Engine runs at optimal RPM (best efficiency point)
+ Smooth, EV-like driving experience
+ Excellent in city/stop-start traffic
+ Simple — no mechanical connection engine-to-wheels

DISADVANTAGES:
- Double energy conversion losses at highway speed
- Engine must be large enough to sustain highway cruising
- Less efficient than direct drive at constant high speed
```

---

#### Slide 6: Architecture 2 — Parallel Hybrid
**Visual:** Energy flow diagram: ICE and Electric Motor both connected to the transmission via a clutch or coupling device, then to Wheels. Battery charges from motor (regen) and can power motor to assist engine. Example vehicle: Honda IMA (Integrated Motor Assist).

**Instructor Narration:**
> "Now the opposite approach. In a parallel hybrid, both the engine AND the electric motor can drive the wheels. They work in parallel — side by side. The motor is typically sandwiched between the engine and the gearbox. At low load, the engine might switch off and the motor drives alone. Under heavy acceleration, both work together — the motor adds torque on top of the engine.
>
> Honda's Integrated Motor Assist is the classic example. A thin electric motor sits directly on the crankshaft, between the engine and the transmission. It can assist during acceleration, provide regenerative braking when slowing down, and act as the starter motor.
>
> The advantage of parallel is simplicity and efficiency at highway speed — the engine drives the wheels directly with no conversion losses. The disadvantage is that the engine speed is tied to the wheel speed through the gearbox, so it can't always run at its most efficient point."

**PPT Content:**
```
ARCHITECTURE 2: PARALLEL HYBRID

Energy flow:
ENGINE ──┐
         ├──> TRANSMISSION -> WHEELS
MOTOR  ──┘
         ^
     BATTERY

Key principle: Engine AND motor can BOTH drive wheels
- Motor assists engine under load
- Motor can drive alone at low speed (if battery allows)
- Engine drives directly at highway speed
- Regen braking recovers energy through motor

Example: Honda IMA (Integrated Motor Assist)

ADVANTAGES:
+ Direct mechanical drive — efficient at highway speed
+ Simple single-motor design
+ Motor assists during acceleration (torque fill)
+ Engine directly drives wheels — minimal conversion loss

DISADVANTAGES:
- Engine speed coupled to wheel speed (via gearbox)
- Limited EV-only range (small motor/battery)
- Engine cannot always run at optimal efficiency point
```

---

#### Slide 7: Architecture 3 — Series-Parallel / Power-Split
**Visual:** Energy flow diagram showing Toyota Synergy Drive: Engine connects to a planetary gear set. Motor-Generator 1 (MG1) connects to sun gear, Engine to carrier, Motor-Generator 2 (MG2) to ring gear which connects to wheels. Battery bidirectionally connected to both MGs through inverter. Show multiple operating modes: EV-only, engine-only, combined, charging.

**Instructor Narration:**
> "Now the clever one. Toyota's Synergy Drive — also called the power-split architecture — combines series and parallel in one system. The secret is a planetary gear set. Remember from Week 6, a planetary gear has a sun gear, planet gears on a carrier, and a ring gear. Toyota connects the engine to the carrier, a small motor-generator — called MG1 — to the sun gear, and a larger motor-generator — MG2 — to the ring gear, which drives the wheels.
>
> This is brilliant because the system can operate in multiple modes simultaneously. At low speed, the engine might be off and MG2 drives the wheels — pure EV mode. At cruise, the engine drives the wheels directly through the ring gear while MG1 generates electricity. Under hard acceleration, the engine AND MG2 both drive the wheels. The planetary gear set continuously varies the ratio between engine and electric drive — there is no conventional gearbox.
>
> This is the most common hybrid architecture in the world. Toyota, Lexus, Ford, and others use it. It gives you the best of both series and parallel."

**PPT Content:**
```
ARCHITECTURE 3: SERIES-PARALLEL / POWER-SPLIT

The Toyota Synergy Drive (THS / HSD)

PLANETARY GEAR SET:
  Sun gear    --> MG1 (Motor-Generator 1: starter/generator)
  Carrier     --> ENGINE
  Ring gear   --> MG2 (Motor-Generator 2: main drive motor) -> WHEELS

  BATTERY <--> INVERTER <--> MG1 / MG2

OPERATING MODES:
1. EV only: Engine off, MG2 drives wheels from battery
2. Engine only: Engine drives wheels, MG1 charges battery
3. Combined: Engine + MG2 both drive wheels (max power)
4. Charging: Engine drives MG1 as generator at standstill
5. Regen: MG2 acts as generator during braking

NO CONVENTIONAL GEARBOX — planetary gear set acts as eCVT

Examples: Toyota Prius/Corolla/RAV4 Hybrid, Lexus range, Ford Escape
```

---

#### Slide 8: Architecture 4 — Plug-In Hybrid (PHEV)
**Visual:** PHEV diagram — essentially the same as series-parallel but with a significantly larger battery pack, a charge port on the vehicle body, and an on-board charger. Show dual-zone: EV range zone (50-80 km) and hybrid range zone (extending total range). Example vehicles: Toyota RAV4 Prime, BMW 330e, Mitsubishi Outlander PHEV.

**Instructor Narration:**
> "A plug-in hybrid is any hybrid architecture — series, parallel, or power-split — with a LARGER battery that you can charge from an external source. The key difference from a regular hybrid is the battery size and the charge port. A standard hybrid might have a 1.5 kilowatt-hour battery. A PHEV has 10 to 25 kilowatt-hours. That gives you 50 to 80 kilometres of pure electric driving before the engine needs to start.
>
> The idea is simple: for your daily commute — which for most Europeans is under 50 kilometres — you run on pure electricity charged overnight from your home socket. For the weekend road trip, you have the engine as a range extender. You get the best of both worlds — if you actually plug it in. And that's the controversy with PHEVs: real-world data shows many owners never plug them in, so they end up worse than a conventional hybrid because they're carrying the weight of a large battery they never charge.
>
> From a technician's perspective, a PHEV has ALL the components of a conventional car PLUS all the HV components. It's the most complex architecture to service."

**PPT Content:**
```
ARCHITECTURE 4: PLUG-IN HYBRID (PHEV)

= Any hybrid architecture + LARGER BATTERY + CHARGE PORT

Regular Hybrid battery: ~1-2 kWh
PHEV battery: ~10-25 kWh
EV-only range: 50-80 km (real-world)

ADDITIONAL COMPONENTS vs standard hybrid:
+ Larger HV battery pack
+ Charge port (Type 2 / CCS)
+ On-board charger (AC -> DC conversion)
+ Charge management ECU

OPERATING STRATEGY:
1. Short trips: Pure EV (charged from wall socket)
2. Long trips: Hybrid mode (engine + motor)
3. Battery depleted: Operates as standard hybrid

TECHNICIAN NOTE:
PHEV = MOST COMPLEX to service
Has ALL conventional systems + ALL HV systems

Examples: Toyota RAV4 Prime, BMW 330e, VW Golf GTE
```

---

#### Slide 9: Architecture 5 — Battery Electric Vehicle (BEV)
**Visual:** Clean BEV layout diagram: Large floor-mounted battery pack -> Inverter -> Electric motor(s) -> Reduction gear -> Wheels. DC-DC converter (HV to 12V), On-board charger, Thermal management system. NO engine, exhaust, fuel system, or conventional transmission. Example vehicles: Tesla Model 3, VW ID.4, Hyundai Ioniq 5.

**Instructor Narration:**
> "And now the full commitment — the Battery Electric Vehicle. No engine. No exhaust. No fuel tank. No conventional gearbox. Just a battery, an inverter, a motor, and a single-speed reduction gear. It is mechanically the simplest drivetrain ever put in a car. An electric motor has one moving part — the rotor. Compare that to the hundreds of moving parts in an engine and gearbox.
>
> The battery pack sits in the floor — a flat slab that lowers the centre of gravity and improves handling. The motor connects through a simple reduction gear, usually around 9:1 ratio, directly to the drive axle. Some BEVs have two motors — one per axle — giving all-wheel drive with no driveshaft.
>
> Range depends on battery size: typically 200 to 600 kilometres on a full charge. Charging happens through AC (home charger, on-board charger converts to DC) or DC fast charging (bypasses on-board charger, charges battery directly). We'll cover charging infrastructure in more detail later this week."

**PPT Content:**
```
ARCHITECTURE 5: BATTERY ELECTRIC VEHICLE (BEV)

Energy flow:
BATTERY PACK -> INVERTER -> ELECTRIC MOTOR -> REDUCTION GEAR -> WHEELS

What's GONE:
  X  Engine, exhaust system, fuel tank, fuel lines
  X  Conventional multi-speed gearbox
  X  Starter motor, alternator
  X  Engine cooling (replaced by battery/motor cooling)

What's NEW:
  +  Large HV battery pack (40-100+ kWh)
  +  Inverter (DC -> 3-phase AC)
  +  Electric motor (PMSM or Induction)
  +  Single-speed reduction gear (~9:1)
  +  DC-DC converter (400V -> 12V)
  +  On-board charger (AC wall -> DC battery)
  +  Battery thermal management system

Range: 200-600 km (depending on battery size)
Examples: Tesla Model 3, VW ID.4, Hyundai Ioniq 5, BMW iX
```

---

#### Slide 10: Architecture Comparison Summary
**Visual:** Comparison table with all five architectures side by side. Columns: Architecture, Engine drives wheels?, Motor drives wheels?, Battery size, EV range, Complexity, Best suited for. Include small energy flow diagram icon for each.

**Instructor Narration:**
> "Let's put them all side by side. In a series hybrid, only the motor drives the wheels. In a parallel hybrid, both engine and motor can drive the wheels. In a power-split, a planetary gear set blends them continuously. A PHEV adds a big battery and charge port to any of these. And a BEV eliminates the engine entirely.
>
> For the exam, you need to be able to identify each architecture from a diagram and explain the energy flow. Let me test you — if I describe a car where the engine only runs a generator and the wheels are always driven by an electric motor, which architecture is that?"

**PPT Content:**
```
ARCHITECTURE COMPARISON

              Series    Parallel  Power-Split  PHEV      BEV
Engine drives   NO       YES       YES         YES       N/A
  wheels?
Motor drives    YES      YES       YES         YES       YES
  wheels?
Battery size    Small    Small     Small       Large     Very Large
                (~1 kWh) (~1 kWh)  (~1-2 kWh)  (10-25)   (40-100+)
EV range        Limited  Very      1-3 km      50-80 km  200-600 km
                         limited
Charge port?    No       No        No          YES       YES
Complexity      Medium   Low-Med   High        Highest   Low
Best for        City     Highway   All-round   Commute   All-round
                driving  cruising  efficiency   + trips   electric

EXAM TIP: Be able to draw the energy flow for each architecture
```

---

#### Slide 11: Energy Flow Quick-Check
**Visual:** Four unlabeled simplified energy flow diagrams. Learners must match each to its architecture name. Interactive quiz format.

**Instructor Narration:**
> "Quick check before we move on. On screen, I have four energy flow diagrams with no labels. Look at each one. Identify: is this a series, parallel, power-split, or BEV? Talk to your neighbour. You have two minutes."

**PPT Content:**
```
ENERGY FLOW QUICK-CHECK

Diagram A: Engine -> Generator -> Motor -> Wheels
           [Battery as buffer]

Diagram B: Engine -+-> Transmission -> Wheels
           Motor  -+
           [Battery]

Diagram C: Engine -> Planetary Gear -> Wheels
           MG1 -> [Inverter/Battery] -> MG2 -> Planetary Gear

Diagram D: Battery -> Inverter -> Motor -> Reduction Gear -> Wheels

Match each diagram to its architecture:
1. Series Hybrid
2. Parallel Hybrid
3. Power-Split (Series-Parallel)
4. BEV
```

**Activity:** Pair discussion (2 min) -> cold-call answers -> instructor confirms: A=Series, B=Parallel, C=Power-Split, D=BEV.

---

### **DEVELOPMENT PART B: EV Component Deep Dive** (Slides 12-22, ~50 minutes)

**Narrative Voice:** Technical but accessible. Build each component's story: what it is, why it exists, how it works.

---

#### Slide 12: Electric Motors — PMSM
**Visual:** Cutaway diagram of a Permanent Magnet Synchronous Motor (PMSM). Show stator windings (3-phase), rotor with embedded permanent magnets, position sensor (resolver), cooling jacket. Label each component.

**Instructor Narration:**
> "The heart of every EV is the electric motor. The most common type in automotive is the PMSM — Permanent Magnet Synchronous Motor. Let's break that name down. 'Permanent Magnet' — the rotor contains powerful rare-earth magnets, usually neodymium. 'Synchronous' — the rotor spins at exactly the same speed as the rotating magnetic field created by the stator. 'Motor' — it converts electrical energy to mechanical rotation.
>
> The stator has three sets of copper windings — three phases. The inverter feeds alternating current into these windings in a precise sequence, creating a rotating magnetic field. The permanent magnets on the rotor are attracted to this field, so the rotor spins. Control the frequency of the AC, and you control the motor speed. Control the amplitude, and you control the torque.
>
> The PMSM is compact, efficient — typically over 95 percent — and delivers maximum torque from zero RPM. That's why EVs feel so quick off the line. The downside? Those permanent magnets use rare-earth materials, which are expensive and have supply chain concerns."

**PPT Content:**
```
ELECTRIC MOTOR: PMSM
(Permanent Magnet Synchronous Motor)

CONSTRUCTION:
- Stator: 3-phase copper windings (fixed, outer ring)
- Rotor: Permanent magnets (neodymium, spinning, inner)
- Resolver: Position sensor on rotor (tells inverter exact angle)
- Cooling jacket: Liquid-cooled for sustained performance

HOW IT WORKS:
1. Inverter feeds 3-phase AC to stator windings
2. Rotating magnetic field is created
3. Rotor magnets follow the field -> rotation
4. Frequency controls speed, amplitude controls torque

ADVANTAGES:
+ High efficiency (>95%)
+ High power density (compact)
+ Maximum torque at 0 RPM
+ Smooth, quiet operation

DISADVANTAGE:
- Rare-earth magnets (cost, supply chain)

Most common in: BMW, VW, Hyundai, most automotive EVs
```

---

#### Slide 13: Electric Motors — Induction Motor
**Visual:** Cutaway of an induction motor. Show stator windings (3-phase), squirrel-cage rotor (aluminium or copper bars), no permanent magnets. Highlight the air gap between stator and rotor.

**Instructor Narration:**
> "The other major type is the induction motor — also called an asynchronous motor. Tesla famously used these in the Model S and Model 3 rear drive unit. The construction is different: the rotor has no magnets at all. Instead, it has a 'squirrel cage' — aluminium or copper bars arranged in a cylinder, shorted at both ends.
>
> How does it work without magnets? The stator creates a rotating magnetic field, just like the PMSM. But instead of magnets following it, the rotating field induces electrical currents in the rotor bars — Faraday's law, from Week 2. Those induced currents create their own magnetic field, which interacts with the stator field and produces torque.
>
> The key difference: the rotor must spin SLOWER than the stator field for current to be induced. That difference in speed is called 'slip.' That's why it's called asynchronous — the rotor is not synchronised with the field.
>
> Induction motors are cheaper — no rare-earth magnets — and very robust. But they're slightly less efficient than PMSM, especially at partial load. Many modern EVs use a PMSM on one axle and an induction motor on the other to get the best of both."

**PPT Content:**
```
ELECTRIC MOTOR: INDUCTION (ASYNCHRONOUS)

CONSTRUCTION:
- Stator: 3-phase copper windings (same as PMSM)
- Rotor: Squirrel-cage (aluminium/copper bars) — NO MAGNETS
- Air gap between stator and rotor
- Liquid cooling

HOW IT WORKS:
1. Stator creates rotating magnetic field
2. Field INDUCES current in rotor bars (Faraday's law)
3. Induced current creates rotor magnetic field
4. Interaction produces torque
5. Rotor must spin SLOWER than field = "slip"

ADVANTAGES:
+ No rare-earth magnets (cheaper, no supply risk)
+ Very robust and reliable
+ Inherent field-weakening at high speed

DISADVANTAGES:
- Slightly lower efficiency than PMSM (especially at partial load)
- More heat generated in rotor

Used in: Tesla (Model S/3/X/Y rear motor), some Audi e-tron
```

---

#### Slide 14: The Inverter — DC to AC and Back
**Visual:** Block diagram of an inverter: DC bus from battery on one side, 3-phase AC output to motor on the other. Show IGBT/MOSFET switching bridge (6 switches in H-bridge configuration). Include regenerative braking reverse flow. Show cooling plate underneath.

**Instructor Narration:**
> "The inverter is the brain of the electric drivetrain. The battery stores DC — direct current. The motor needs AC — three-phase alternating current. The inverter converts DC to AC. It uses six high-power semiconductor switches — IGBTs or silicon carbide MOSFETs — arranged in three pairs, one pair per motor phase.
>
> These switches turn on and off thousands of times per second, using a technique called Pulse Width Modulation, to create a synthetic AC waveform. By varying the switching pattern, the inverter precisely controls the motor's speed and torque.
>
> But here's the clever part: the inverter works in BOTH directions. When you lift off the accelerator, the motor becomes a generator — kinetic energy flows backward through the inverter, is converted from AC to DC, and recharges the battery. This is regenerative braking. It's why EVs are so efficient in city driving — every time you slow down, you recover energy.
>
> The inverter generates significant heat, so it has its own liquid cooling circuit. If the inverter fails, the car cannot move — and it cannot perform regen braking."

**PPT Content:**
```
THE INVERTER — Heart of the HV System

JOB: Convert DC (battery) <-> 3-phase AC (motor)

CONSTRUCTION:
- 6 power switches (IGBT or SiC MOSFET)
- Arranged as 3 half-bridges (one per motor phase)
- Gate driver circuits (control switching)
- DC-link capacitor (smooths voltage ripple)
- Liquid cooling plate (dissipates heat)

DRIVE MODE (motoring):
Battery DC -> Inverter switches -> 3-phase AC -> Motor spins

REGEN MODE (braking):
Motor generates AC -> Inverter rectifies -> DC -> Battery charges

CONTROL:
- PWM (Pulse Width Modulation) — switches ON/OFF thousands of times/sec
- Frequency controls motor speed
- Current amplitude controls motor torque
- Motor position sensor (resolver) provides feedback

FAILURE = No drive AND no regen braking
```

---

#### Slide 15: DC-DC Converter — Two Voltage Worlds
**Visual:** Diagram showing the HV system (400V battery, inverter, motor) on one side and the 12V system (12V battery, lights, wipers, ECUs, infotainment) on the other, connected by the DC-DC converter. Arrows show power flow from HV to 12V.

**Instructor Narration:**
> "Every hybrid and EV has TWO electrical systems running simultaneously. The high-voltage system at 400 volts — or 800 volts in newer vehicles — powers the drivetrain. But the car still needs 12 volts for everything else: headlights, wipers, window motors, the instrument cluster, the radio, all the ECUs, the horn, the door locks.
>
> In a conventional car, the alternator charges the 12-volt battery. In an EV, there is no alternator. Instead, the DC-DC converter steps the 400-volt supply down to 12 volts and charges the 12-volt battery. It's essentially a very efficient transformer for DC.
>
> If the DC-DC converter fails, the 12-volt battery drains, and ALL the conventional systems stop working — including the control electronics that manage the HV system. The car becomes undriveable even though the HV battery may be fully charged. This is a common failure mode technicians encounter."

**PPT Content:**
```
DC-DC CONVERTER — Bridging Two Worlds

JOB: Step down HV battery voltage to 12V for conventional systems

HV SYSTEM (400V / 800V)          12V SYSTEM
  HV Battery                       12V Battery
  Inverter                         Headlights, wipers
  Electric motor                   ECUs, infotainment
  On-board charger                 Horn, central locking
  A/C compressor                   Window motors
          |                              |
          +------- DC-DC CONVERTER ------+
               400V DC -> 12V DC

REPLACES: The alternator in conventional vehicles
TYPICAL OUTPUT: 1.5 - 3.0 kW continuous

FAILURE MODE:
DC-DC fails -> 12V battery drains -> ALL conventional systems die
-> HV system control electronics lose power -> Car undriveable
-> Even though HV battery is fully charged!

TECHNICIAN NOTE: A dead 12V battery in an EV is often DC-DC failure
```

---

#### Slide 16: On-Board Charger (OBC)
**Visual:** Diagram showing the charging path: Wall socket (AC mains) -> Charge cable -> Vehicle inlet -> On-board charger (AC-to-DC conversion) -> HV Battery. Separate path shown for DC fast charging that bypasses the OBC. Label power levels: AC slow (3.7 kW), AC fast (7-22 kW), DC fast (50-350 kW).

**Instructor Narration:**
> "When you plug an EV into a home wall socket or a public AC charger, the electricity coming in is alternating current. But the battery stores direct current. Something has to convert AC to DC — that's the on-board charger, or OBC.
>
> The OBC is built into the vehicle. It takes single-phase or three-phase AC from the charging inlet and converts it to the correct DC voltage and current for the battery. Typical power levels are 7 to 22 kilowatts for AC charging. At 7 kW, a 60 kWh battery takes about 9 hours to fully charge — perfect for overnight at home.
>
> DC fast charging is different. The conversion happens OUTSIDE the vehicle, in the charging station itself. DC goes straight into the battery, bypassing the OBC entirely. That's how you get 50 to 350 kilowatts charging power and an 80 percent charge in 20 to 40 minutes.
>
> Every EV has an OBC. Its size and power rating directly affect AC charging speed."

**PPT Content:**
```
ON-BOARD CHARGER (OBC)

JOB: Convert AC from wall/charger to DC for battery

AC CHARGING PATH:
Wall socket -> Cable -> Vehicle inlet -> OBC -> HV Battery
                                     (AC to DC)
Power: 3.7 kW (1-phase) to 22 kW (3-phase)
Time for 60 kWh battery: ~3 to 9 hours

DC FAST CHARGING PATH (bypasses OBC):
DC Station -> Cable -> Vehicle inlet -> DIRECTLY to HV Battery
Power: 50 kW to 350 kW
Time for 10-80%: 20 to 40 minutes

OBC SPECIFICATIONS:
- Typical power: 7-22 kW (varies by vehicle)
- Efficiency: ~93-95%
- Liquid cooled
- Integrated PFC (Power Factor Correction)

TECHNICIAN NOTE: AC charge speed is LIMITED by the OBC rating
Even on a 22 kW charger, a car with 7 kW OBC charges at 7 kW
```

---

#### Slide 17: HV Battery Pack — The Big Picture
**Visual:** Exploded view of an EV battery pack showing the layers: individual cells -> module assembly -> complete pack in floor. Show pack casing, coolant lines, BMS boards, wiring harness, contactors, service disconnect. Label dimensions and weight (e.g., 400 kg, 2m x 1.5m).

**Instructor Narration:**
> "The battery pack is the single most expensive component in an EV — typically 30 to 40 percent of the vehicle's total cost. And it's the one that defines range, performance, charging speed, and vehicle weight. Let's look at how it's built, from the smallest cell to the complete pack.
>
> A battery pack is a large, flat assembly that sits in the floor of the vehicle, between the front and rear axles. It's structural — it adds rigidity to the body. It weighs 300 to 700 kilograms. And it operates at 400 to 800 volts. Inside, you'll find hundreds or thousands of individual cells, assembled into modules, connected in series and parallel, managed by a Battery Management System, protected by contactors, and cooled by a dedicated thermal management system.
>
> Let's go layer by layer."

**PPT Content:**
```
HV BATTERY PACK — OVERVIEW

LOCATION: Vehicle floor (between axles)
WEIGHT: 300-700 kg (typically)
VOLTAGE: 400V or 800V nominal
CAPACITY: 40-100+ kWh
COST: 30-40% of total vehicle cost

CONSTRUCTION (inside out):
CELLS -> MODULES -> PACK

PACK CONTAINS:
- Hundreds/thousands of individual cells
- Module assemblies (cells grouped and framed)
- Battery Management System (BMS) — the brain
- Contactors — HV switches (main +, main -, pre-charge)
- Service disconnect / manual disconnect plug (MSD)
- Coolant lines (liquid thermal management)
- Wiring harness (HV busbars + LV signal wires)
- Structural casing (aluminium, sealed, crash-protected)

The pack is STRUCTURAL — adds body rigidity
The pack is SEALED — IP67 waterproofing
```

---

#### Slide 18: Cell Chemistry — NMC vs LFP
**Visual:** Side-by-side comparison of NMC and LFP cells. Show radar/spider chart comparing: energy density, cycle life, thermal stability, cost, charging speed. Include chemical formulas and common vehicle applications.

**Instructor Narration:**
> "Not all battery cells are created equal. Two chemistries dominate the automotive market. NMC — Nickel Manganese Cobalt — and LFP — Lithium Iron Phosphate.
>
> NMC has higher energy density — more kilowatt-hours per kilogram. That means longer range for the same weight. It's been the go-to chemistry for premium EVs. But it's more expensive, uses cobalt which has ethical supply chain issues, and is more sensitive to thermal runaway — overheating can lead to fire.
>
> LFP has lower energy density — you need a heavier pack for the same range. But it's cheaper, uses abundant materials, lasts significantly longer — often over 3,000 charge cycles versus 1,000 to 1,500 for NMC — and is much more thermally stable. It's virtually impossible to cause thermal runaway in an LFP cell under normal failure conditions. Tesla, BYD, and others have shifted standard-range models to LFP.
>
> As a technician, you'll see both. The cell chemistry affects charging profiles, thermal management requirements, and safety characteristics."

**PPT Content:**
```
CELL CHEMISTRY: NMC vs LFP

NMC (Nickel Manganese Cobalt — LiNiMnCoO2)
- Energy density: HIGH (~250 Wh/kg)
- Cycle life: 1,000-1,500 cycles
- Thermal stability: Moderate (runaway risk at ~200C)
- Cost: Higher (cobalt is expensive)
- Used in: BMW, VW, Hyundai premium models

LFP (Lithium Iron Phosphate — LiFePO4)
- Energy density: LOWER (~160 Wh/kg)
- Cycle life: 3,000-5,000+ cycles
- Thermal stability: EXCELLENT (runaway >300C, very resistant)
- Cost: Lower (abundant iron, no cobalt)
- Used in: Tesla Standard Range, BYD, many Chinese EVs

TECHNICIAN IMPLICATIONS:
- NMC: More aggressive thermal management, tighter voltage windows
- LFP: Flatter voltage curve (harder to read SOC from voltage)
- LFP: Needs periodic 100% charge for BMS calibration
- Both: Different charging profiles and temperature limits
```

---

#### Slide 19: Cell Formats — Pouch, Prismatic, Cylindrical
**Visual:** Three photos/diagrams side by side: pouch cell (flat, flexible, like a foil packet), prismatic cell (rectangular metal can), cylindrical cell (like a large AA battery — 2170/4680 format). Show dimensions, typical capacity, and which manufacturers use each. Below, show how each assembles into modules.

**Instructor Narration:**
> "Cells come in three physical formats. Pouch cells are flat, flexible packages — like a thick foil sachet. They're space-efficient and can be shaped to fit the available space, but they need external compression and structural support. GM and Hyundai use pouch cells.
>
> Prismatic cells are rectangular metal cans. They're rigid, easy to stack, and common in European and Chinese EVs. BMW and BYD use prismatic cells.
>
> Cylindrical cells look like large AA batteries. Tesla pioneered the 2170 format and now uses the larger 4680 format. Cylindrical cells are cheap to mass-produce, mechanically strong, and excellent at thermal management because the round shape allows cooling channels between cells.
>
> Each format has trade-offs. No single format has won — the market uses all three. As a technician, you'll encounter all of them."

**PPT Content:**
```
CELL FORMATS

POUCH                   PRISMATIC              CYLINDRICAL
Flat, flexible foil     Rectangular metal can   Round, like large battery
Needs compression       Self-supporting         Self-supporting
Space efficient         Easy to stack           Easy to cool (gaps)
Swelling risk           Rigid, robust           Very consistent quality

Used by: GM, Hyundai,   Used by: BMW, BYD,     Used by: Tesla, BMW
Nissan, Kia             CATL, Samsung SDI       (46mm series)

Typical sizes:          Typical sizes:          Typical sizes:
~300x100x10 mm          ~150x100x30 mm          18650, 2170, 4680
~40-80 Ah               ~50-200+ Ah             ~5-26 Ah per cell

MODULE ASSEMBLY:
Cells connected in SERIES (voltage adds up)
and PARALLEL (capacity adds up)
Example: 96 cells in series = 96 x 3.7V = ~355V nominal
```

---

#### Slide 20: The BMS — Battery Management System
**Visual:** Block diagram of BMS architecture: Cell Monitoring Units (CMUs) connected to each cell group, measuring voltage and temperature. Central BMS controller receiving data from all CMUs. BMS outputs: contactor control, cooling control, SOC calculation, CAN communication to vehicle ECU. Show balancing circuit (passive — resistor bleeder, and active — charge shuttle).

**Instructor Narration:**
> "The Battery Management System is the brain of the battery pack. Its job is to keep every cell safe, healthy, and performing optimally. Remember — a pack might have 96 cells in series. If ANY single cell fails, the entire pack is compromised. The BMS monitors every cell individually.
>
> Three primary functions. First, MONITORING: the BMS measures voltage, temperature, and current for every cell or cell group, typically every 10 to 100 milliseconds. From these measurements, it calculates State of Charge — SOC — which is the battery equivalent of a fuel gauge. It also tracks State of Health — SOH — the battery's degradation over time.
>
> Second, BALANCING: cells are never perfectly identical. Over time, some cells charge faster or hold slightly more energy. If you don't balance them, the weakest cell limits the entire pack. The BMS performs cell balancing — either passive, where it bleeds excess energy from strong cells through a resistor, or active, where it transfers energy from strong cells to weak cells.
>
> Third, PROTECTION: the BMS controls the main contactors. If it detects overvoltage, undervoltage, overcurrent, or overtemperature on any cell, it opens the contactors and isolates the pack. The BMS is the pack's safety guardian."

**PPT Content:**
```
BATTERY MANAGEMENT SYSTEM (BMS)

THE BRAIN OF THE BATTERY PACK

FUNCTION 1: MONITORING
- Cell voltage: every cell, every 10-100 ms
- Cell temperature: thermistors throughout pack
- Pack current: hall-effect sensor
- Calculates: SOC (State of Charge) = "fuel gauge"
              SOH (State of Health) = degradation tracking

FUNCTION 2: CELL BALANCING
- Passive balancing: Bleed excess energy via resistors (heat)
  (Simple, cheap, wastes energy)
- Active balancing: Transfer energy between cells
  (Complex, efficient, expensive)
- Purpose: Prevent weakest cell from limiting whole pack

FUNCTION 3: PROTECTION
- Controls main contactors (connect/disconnect HV)
- Monitors for: Overvoltage, Undervoltage, Overcurrent,
  Overtemperature, Isolation fault
- Fault detected -> Contactors OPEN -> Pack ISOLATED

COMMUNICATES VIA CAN BUS: SOC, power limits, fault codes
```

---

#### Slide 21: Contactors and Pre-Charge Circuit
**Visual:** Schematic showing the HV battery internal circuit: Battery cells -> Main Negative Contactor -> Main Positive Contactor -> HV output to vehicle. Pre-charge relay and pre-charge resistor shown in parallel with Main Positive Contactor. Service disconnect (MSD) shown in series. Sequence diagram showing startup: (1) Main Negative closes, (2) Pre-charge closes, (3) Capacitors charge through resistor, (4) Main Positive closes, (5) Pre-charge opens.

**Instructor Narration:**
> "Inside every HV battery pack, there are contactors — heavy-duty electromagnetic switches that connect or disconnect the high-voltage supply. There are typically three: the main negative contactor, the main positive contactor, and the pre-charge contactor.
>
> Why pre-charge? The inverter contains large capacitors on its DC bus. When the capacitors are empty and you suddenly connect 400 volts, an enormous inrush current flows — potentially thousands of amps for a fraction of a second. That current can weld the main contactor shut and damage the capacitors. The pre-charge circuit prevents this.
>
> Here's the startup sequence. Step one: the BMS closes the main negative contactor. Step two: instead of closing the main positive contactor, the BMS closes the pre-charge contactor, which has a resistor in series — typically 50 to 150 ohms. Current flows through the resistor, slowly charging the capacitors over about one to two seconds. Step three: once the capacitor voltage reaches about 90 percent of battery voltage, the BMS closes the main positive contactor. Step four: the pre-charge contactor opens — its job is done.
>
> The service disconnect — also called the Manual Service Disconnect or MSD — is a physical plug that breaks the series connection in the middle of the battery pack. A technician removes this plug before any HV work to ensure the pack cannot output full voltage. We'll cover the full HV safety procedure tomorrow."

**PPT Content:**
```
CONTACTORS & PRE-CHARGE CIRCUIT

HV BATTERY INTERNAL CIRCUIT:
Cells(-) -> [MAIN NEG CONTACTOR] -> External HV Negative
Cells(+) -> [MAIN POS CONTACTOR] -> External HV Positive
            [PRE-CHARGE CONTACTOR + RESISTOR] in parallel
            [SERVICE DISCONNECT / MSD] in series with cells

STARTUP SEQUENCE:
1. Main Negative contactor CLOSES
2. Pre-charge contactor CLOSES (through resistor ~50-150 ohm)
3. Inverter DC-link capacitors charge slowly (~1-2 sec)
4. Capacitor voltage reaches ~90% of battery voltage
5. Main Positive contactor CLOSES
6. Pre-charge contactor OPENS

WHY PRE-CHARGE?
Without it: Empty capacitors = near-short-circuit
-> Thousands of amps inrush current
-> Contactor welding, capacitor damage, arc flash risk

SERVICE DISCONNECT (MSD):
- Physical plug removed by technician
- Breaks series connection mid-pack
- Prevents full pack voltage at output
- ALWAYS removed before HV work (Day 32 protocol)
```

---

#### Slide 22: HV System Overview — All Components Connected
**Visual:** Complete HV system architecture diagram showing every component discussed, all connected with orange HV cables. Battery Pack (with BMS, contactors, MSD) -> Inverter -> Motor -> Reduction gear -> Wheels. DC-DC converter branching to 12V system. On-board charger connected to charge inlet. HV A/C compressor shown. Orange cable routing highlighted. Ground fault monitoring shown.

**Instructor Narration:**
> "Let's put everything together. Here's the complete HV architecture of a typical BEV. The battery pack in the floor connects through orange high-voltage cables to the inverter, which drives the motor. The DC-DC converter taps the HV bus to supply the 12-volt system. The on-board charger connects from the charge inlet to the battery. And an HV air conditioning compressor runs directly from the HV bus — because there's no engine to drive a belt-driven compressor.
>
> Notice the orange cables. Every high-voltage cable in a hybrid or EV is orange. This is a universal colour code. If you see an orange cable, it carries potentially lethal voltage. You never cut, disconnect, or even touch an orange cable without following the HV safety protocol we'll learn tomorrow.
>
> The system also includes isolation monitoring — a ground fault detector that continuously checks whether any HV conductor has an unintended path to the vehicle body. If isolation is lost, the system raises a warning and may disconnect the pack.
>
> This diagram is your reference. By the end of today's practical, you should be able to point to every one of these components on a real vehicle."

**PPT Content:**
```
COMPLETE HV SYSTEM ARCHITECTURE

                    CHARGE INLET
                         |
                   ON-BOARD CHARGER (AC->DC)
                         |
+-------------------------------------------------------+
|                    HV BATTERY PACK                     |
| Cells -> MSD -> Contactors -> BMS                     |
| (400V/800V)                                           |
+-------+-------------------+---------------------------+
        |                   |
   DC-DC CONVERTER     INVERTER (DC<->3ph AC)
        |                   |
   12V BATTERY         ELECTRIC MOTOR
   12V Systems              |
                      REDUCTION GEAR
                            |
                         WHEELS

Additional HV consumers:
- HV A/C Compressor (electric, replaces belt-driven)
- HV PTC Heater (cabin heating without engine)

ALL HV CABLES ARE ORANGE — universal colour code
ISOLATION MONITORING: Continuous ground fault detection
```

---

### **PRACTICAL: HV Component Identification** (Slides 23-26, ~80 minutes)

**Narrative Voice:** Workshop guide. Structured, safety-aware, hands-on.

---

#### Slide 23: Practical 1 — HV Component Identification (30 min)
**Visual:** Annotated photo or diagram of a hybrid/EV training vehicle (or detailed technical poster) with numbered callouts for each HV component. Blank worksheet for learners.

**Instructor Narration:**
> "Workshop time. We're going to the training vehicle — or using the detailed component diagram if the vehicle isn't available. Your task: identify and label every high-voltage component. I want you to find seven items: the battery pack, the inverter, the electric motor, the DC-DC converter, the on-board charger, the service disconnect, and the orange HV cables.
>
> Work in pairs. Use the worksheet. For each component, write: its name, its location on the vehicle, its function in one sentence, and what connects to it. You have 30 minutes. Safety reminder: this is a TRAINING exercise. Do NOT touch any orange cables or HV components. Observe and identify only."

**PPT Content:**
```
PRACTICAL 1: HV COMPONENT IDENTIFICATION
Time: 30 minutes | Pairs

FIND AND LABEL THESE 7 HV COMPONENTS:
1. HV Battery Pack — where is it mounted?
2. Inverter — where is it relative to the motor?
3. Electric Motor — front, rear, or both axles?
4. DC-DC Converter — where is it located?
5. On-Board Charger — where is the charge inlet?
6. Service Disconnect (MSD) — how do you access it?
7. Orange HV Cables — trace the routing

FOR EACH COMPONENT, RECORD:
- Name
- Location on vehicle
- Function (one sentence)
- What connects to it (inputs/outputs)

SAFETY: OBSERVE ONLY — do NOT touch HV components
```

**Activity:** Pairs work around the training vehicle or detailed diagram. Instructor circulates, asking guiding questions. Debrief as a group after 30 minutes — instructor confirms correct identifications.

---

#### Slide 24: Practical 2 — HV Component Location Mapping (20 min)
**Visual:** Blank vehicle outline (top view and side view) on a worksheet. Learners draw and label component locations.

**Instructor Narration:**
> "Now that you've found everything, let's create a map. On your worksheet, you have a blank vehicle outline — top view and side view. Draw the location of every HV component you identified. Use orange for HV cables, label each component, and draw the connections between them. This map will be your study reference for the rest of Week 7.
>
> Think about WHY things are where they are. The battery is in the floor — why? Low centre of gravity and crash protection. The inverter is close to the motor — why? Short HV cable runs reduce losses. The DC-DC converter is near the 12V battery — why? Short 12V cable runs. Engineering is about trade-offs and placement logic."

**PPT Content:**
```
PRACTICAL 2: HV COMPONENT LOCATION MAPPING
Time: 20 minutes | Individual

ON YOUR BLANK VEHICLE OUTLINE:
1. Draw the battery pack location (floor area)
2. Mark the inverter position
3. Mark the electric motor position
4. Mark the DC-DC converter
5. Mark the on-board charger and charge inlet
6. Mark the service disconnect access point
7. Draw HV cable routing in ORANGE
8. Draw 12V connections from DC-DC converter
9. Label the HV A/C compressor if visible

THINK ABOUT PLACEMENT LOGIC:
- Why is the battery in the floor?
- Why is the inverter close to the motor?
- Why is the charge inlet where it is?
```

**Activity:** Individual drawing exercise. Instructor reviews maps, corrects misconceptions. Best maps can be shared with the class.

---

#### Slide 25: Practical 3 — Battery Pack Analysis (30 min)
**Visual:** Battery pack cutaway photograph or detailed exploded diagram. Numbered callouts pointing to: individual cells (showing cell format), module frame, BMS circuit board, cell voltage sense wires, temperature sensors, busbar connections, main contactors (pos/neg/pre-charge), pre-charge resistor, coolant channels, service disconnect plug, HV output terminals, low-voltage connector (CAN bus to vehicle).

**Instructor Narration:**
> "Final practical. We're looking inside the battery pack — either a physical cutaway training unit or this detailed exploded diagram. The battery pack is the most complex single assembly in an EV. Your task: identify every internal component.
>
> Start with the cells. What format are they — pouch, prismatic, or cylindrical? How are they arranged — how many in series, how many in parallel? Find the module boundaries. Find the BMS board — it's the circuit board with all the thin sense wires going to each cell. Find the temperature sensors — small thermistors attached to cell surfaces.
>
> Now find the contactors. How many are there? Which one has the pre-charge resistor? Find the service disconnect plug — it should be accessible from outside the pack or through a cover.
>
> Finally, find the coolant connections. How is the pack cooled — plates between modules, channels around cells, or a cold plate on the bottom? Trace the coolant path if you can.
>
> Record everything on your worksheet. This exercise is worth practising — battery pack identification appears on the TUV SUD exam."

**PPT Content:**
```
PRACTICAL 3: BATTERY PACK CUTAWAY ANALYSIS
Time: 30 minutes | Small groups (3-4)

IDENTIFY INSIDE THE BATTERY PACK:

CELLS & MODULES:
- Cell format: Pouch / Prismatic / Cylindrical?
- Cell arrangement: How many in series? Parallel?
- Module boundaries: How many modules in the pack?

BMS COMPONENTS:
- BMS main board (controller)
- Cell voltage sense wires
- Temperature sensors (thermistors)
- Current sensor (hall-effect, on main busbar)

CONTACTORS & SAFETY:
- Main negative contactor
- Main positive contactor
- Pre-charge contactor + resistor
- Service disconnect plug (MSD)

THERMAL MANAGEMENT:
- Coolant inlet and outlet
- Cooling plates or channels
- How is heat moved away from cells?

HV CONNECTIONS:
- HV output terminals (to vehicle harness)
- LV connector (CAN bus communication)

EXAM NOTE: Battery pack identification is exam content
```

**Activity:** Small groups examine the cutaway or diagram. Each group presents one section of findings. Instructor fills gaps and corrects errors. Emphasis on safety — even cutaway packs may retain residual voltage.

---

#### Slide 26: Practical Debrief
**Visual:** Summary checklist — "Components I Can Now Identify" with tick boxes for all HV components.

**Instructor Narration:**
> "Let's debrief. Show of hands — who can now identify all seven external HV components on a vehicle? Good. Who can identify at least five internal battery pack components? Excellent. Who can explain the pre-charge sequence? Let me hear it.
>
> You've done something important today. You've built a mental map of the entire HV system. You know what each component does, where it sits, and how it connects to the others. This is the foundation for everything else this week — HV safety protocols tomorrow, charging systems, and HV service procedures."

**PPT Content:**
```
PRACTICAL DEBRIEF — CAN YOU NOW IDENTIFY:

EXTERNAL HV COMPONENTS:
[ ] HV Battery Pack
[ ] Inverter
[ ] Electric Motor (PMSM or Induction)
[ ] DC-DC Converter
[ ] On-Board Charger
[ ] Service Disconnect (MSD)
[ ] Orange HV Cable Routing

INTERNAL BATTERY PACK:
[ ] Individual cells and cell format
[ ] Module assemblies
[ ] BMS board and sense wires
[ ] Temperature sensors
[ ] Main contactors (positive, negative, pre-charge)
[ ] Pre-charge resistor
[ ] Coolant channels/plates
[ ] HV output terminals
```

---

### **WRAP-UP: Consolidation & Day 32 Preview** (Slides 27-28, ~15 minutes)

---

#### Slide 27: What You Learned Today
**Visual:** Visual summary — five architecture diagrams across the top, six component icons across the bottom, all connected by a flow line.

**Instructor Narration:**
> "Let's recap what you've covered today. You can now distinguish five electrified architectures — series, parallel, power-split, PHEV, and BEV — and explain the energy flow in each one. You understand two types of electric motors and why each is used. You know what the inverter, DC-DC converter, and on-board charger do. And you've looked inside a battery pack and identified cells, modules, BMS, contactors, and the pre-charge circuit.
>
> That's a lot of new knowledge in one session. Review your notes tonight. Look at your component map. Tomorrow builds directly on today — we learn the HV safety protocols that keep you alive when working near these systems. Everything you identified today becomes a potential hazard tomorrow."

**PPT Content:**
```
DAY 31 RECAP — YOU CAN NOW:

ARCHITECTURES:
[x] Explain series hybrid energy flow (engine -> generator -> motor)
[x] Explain parallel hybrid (engine + motor both drive wheels)
[x] Explain power-split / Toyota Synergy Drive (planetary gear)
[x] Explain PHEV (larger battery + charge port + any architecture)
[x] Explain BEV (battery + inverter + motor, no engine)

COMPONENTS:
[x] Describe PMSM and induction motor differences
[x] Explain inverter function (DC <-> AC) and regen braking
[x] Explain DC-DC converter (400V -> 12V)
[x] Explain on-board charger (AC -> DC for battery)
[x] Describe HV battery pack construction and cell chemistry
[x] Explain BMS functions: monitoring, balancing, protection
[x] Explain pre-charge circuit purpose and sequence
[x] Identify service disconnect purpose

EXAM WEIGHT: 16 marks — this content WILL be on the exam
```

---

#### Slide 28: Day 32 Preview — HV Safety Protocols
**Visual:** Image of HV-rated insulating gloves (Class 0, rated to 1000V AC), a lockout/tagout kit, an HV multimeter, and a warning triangle with a lightning bolt.

**Instructor Narration:**
> "Tomorrow is the most important safety session of the entire program. You now know what's inside a hybrid or EV. Tomorrow, you learn how to work near it without getting killed. We'll cover the HV safety protocol step by step: vehicle immobilisation, service disconnect removal, waiting times for capacitor discharge, voltage verification with a CAT III meter, and lockout/tagout procedures.
>
> You'll learn about HV-rated PPE — those orange gloves are rated to 1000 volts AC, and they must be tested before every use. You'll learn the rescue protocol if a colleague contacts a live HV source. And you'll practise the full de-energisation procedure on a training vehicle.
>
> Come prepared. This is not optional knowledge — without HV safety certification, you cannot legally touch an HV system in a workshop. Tomorrow earns that certification."

**PPT Content:**
```
DAY 32 PREVIEW: HV SAFETY PROTOCOLS

- HV dangers: Electrocution, arc flash, chemical burns
- The 5-step safe working procedure
- Vehicle immobilisation and service disconnect
- Capacitor discharge and waiting times
- Voltage verification (CAT III rated meter)
- Lockout / Tagout procedure
- HV-rated PPE: Class 0 gloves (1000V AC), face shield
- Emergency rescue protocol
- Practical: Full de-energisation procedure on training vehicle

THIS SESSION IS MANDATORY FOR HV WORK CERTIFICATION
Wear closed-toe shoes. Bring your full PPE kit.
```

---

## Assessment Checkpoint

**Formative (not graded, exam preparation):**
- Energy flow diagram quiz: correctly identify architecture from diagram (4 scenarios)
- Component identification: locate and name 7 HV components on training vehicle or diagram
- Battery pack analysis: identify 5+ internal components from cutaway
- Pre-charge sequence: describe the 4-step sequence from memory
- Quick-fire: "What does the inverter do? What does the DC-DC converter replace? Why pre-charge?"

**Summative alignment (16 exam marks):**
- Architecture identification and energy flow explanation (~6 marks)
- Component function and location (~6 marks)
- Battery pack construction, BMS function, and safety features (~4 marks)

---

## Key Takeaways

1. Electrification is a spectrum — from mild hybrid to full BEV — and technicians must understand all architectures
2. Series hybrids decouple the engine from the wheels; parallel hybrids couple them; power-split does both
3. The PMSM is the dominant automotive motor; induction motors offer a magnet-free alternative
4. The inverter is the bridge between DC battery and AC motor — and enables regenerative braking
5. The DC-DC converter replaces the alternator; its failure kills the entire 12V system
6. Battery packs are built from cells (NMC or LFP, in pouch/prismatic/cylindrical formats) assembled into modules and managed by the BMS
7. The BMS monitors every cell, balances charge, and controls contactors for safety
8. The pre-charge circuit protects against inrush current to inverter capacitors
9. Orange cables = high voltage. NEVER touch without following HV safety protocol.
10. Tomorrow's HV safety session is the gateway to legal HV work certification

---

## Preparation for Day 32

**Instructor prep:**
- Prepare HV safety demonstration kit: Class 0 insulating gloves (with leather outers), HV-rated insulating mat, CAT III multimeter, lockout/tagout padlock set, warning signs
- Ensure training vehicle HV system is in known safe state (de-energised and verified)
- Print HV safe working procedure flowchart (laminated, one per learner)
- Prepare HV rescue demonstration equipment (insulating hook, first aid kit)
- Verify all learners have appropriate PPE (closed-toe shoes minimum; provide safety glasses)
- Review local regulatory requirements for HV competence certification

**Learner prep:**
- Review today's notes: architectures, component functions, battery pack construction
- Memorise the five hybrid/EV architecture energy flow diagrams
- Bring full PPE kit (closed-toe shoes, safety glasses)
- Review Week 2 electrical safety basics (voltage, current, resistance, Ohm's law)
- Read the pre-charge circuit sequence until you can recite it from memory
