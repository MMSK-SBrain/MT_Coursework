---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 3
week_title: "The Heart"
day_number: 11
session_title: "Air + Fuel = Combustion — The Engine's Two Inputs"
duration_minutes: 180
theory_practice: "50:50"
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 11: Air + Fuel = Combustion — The Engine's Two Inputs
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (90 min theory + 90 min practical)
**Approach:** Two-Path Tracing — Follow Air, Follow Fuel, Then Watch Them Meet
**PPT Target:** 26-28 slides
**Week:** 3 of 8 — "The Heart"
**Exam Weight:** Week 3 = 18 marks (18% of TUV SUD exam)

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Describe the complete powertrain chain from engine crankshaft to driven wheels
- Explain the four-stroke cycle for both gasoline and diesel engines, identifying the key differences in ignition and combustion
- Trace the complete air path from the air filter to the cylinder
- Trace the complete fuel path from the tank to the injector
- Explain the role of the ECU in coordinating air and fuel delivery (air-fuel ratio, lambda, fuel maps)
- Identify the major construction features of an engine block and cylinder head, including combustion chamber geometry

**This is Day 1 of Week 3 — the first system deep-dive.** Learners completed Weeks 1 (Meet the Machine) and 2 (Speaking Electricity). They know the 8 vehicle systems and can read circuits. Now they enter the engine for the first time. The goal is to build two clear mental maps — the air path and the fuel path — that every subsequent engine session this week hangs detail onto.

---

## Connection to Prior Knowledge

Build from Weeks 1-2:
- Day 1: Learners identified the engine as "System 1 — The Heart" and saw it on the lift
- Day 3: They measured voltage and resistance — the same multimeter skills apply to engine sensors
- Day 6-10: They learned about ECUs, CAN bus, and sensor/actuator loops — the ECU controlling air and fuel is the biggest example of everything they studied in Week 2

**Bridge:** "For two weeks you've been building foundations — identifying systems, learning to measure, reading circuits, understanding how ECUs think. Now we put all of that to work. This week, we go inside the engine. And we start with the simplest question: what does an engine actually need to run?"

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: The Engine's Two Inputs** (Slides 1-4, ~15 minutes)

**Narrative Voice:** Confident, energetic — this is the start of the real system deep-dives. Make it feel like a new chapter.

---

#### Slide 1: Title & Week 3 Launch
**Visual:** Hero image of a running engine on a dynamometer with intake manifold and fuel rail visible — overlay text introducing Week 3

**Instructor Narration:**
> "Welcome to Week 3. For two weeks, you've been learning the language — systems, safety, electricity, circuits, ECUs. Starting today, we use that language. Week 3 is called 'The Heart' because we're spending the entire week inside the engine. And we start with the most fundamental truth in automotive engineering: an engine needs exactly two things to run — air and fuel. Get the ratio right, ignite it at the right moment, and you have power. Get it wrong, and you have a very expensive paperweight."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 3: The Heart — Engine Systems
Day 11: Air + Fuel = Combustion

An engine needs exactly two things to run.
This week starts from that simple truth.
```

---

#### Slide 2: Week 3 Overview — The Engine Week
**Visual:** Visual timeline showing Week 3's five days — Day 11 highlighted. Icons for each day's topic.

**Instructor Narration:**
> "Here's your Week 3 roadmap. Today we trace air and fuel — the engine's two inputs. Tomorrow, we dive deep into gasoline fuel delivery and ignition systems. Day 13 covers diesel systems — injection and combustion. Day 14 is engine timing — camshafts, valve timing, and the critical relationship between piston position and valve events. Day 15, we bring it all together with a full engine inspection practical.
>
> But everything this week builds on today. Today gives you the map. The rest of the week fills in the detail."

**PPT Content:**
```
WEEK 3: THE HEART — YOUR ROADMAP

Day 11: Air + Fuel = Combustion (TODAY)
  — The engine's two inputs, four-stroke cycle, air path, fuel path

Day 12: Gasoline Fuel Delivery & Ignition
  — Injectors, fuel pressure, spark plugs, coils, ignition timing

Day 13: Diesel Injection & Combustion
  — Common rail, glow plugs, turbo integration, compression ignition

Day 14: Engine Timing & Valve Control
  — Camshafts, timing chains/belts, VVT, valve clearance

Day 15: Engine Inspection Practical
  — Compression test, leak-down, cylinder head inspection

Exam weight: Week 3 = 18 marks (18%)
```

---

#### Slide 3: The Fundamental Equation
**Visual:** Large, simple graphic: AIR + FUEL + IGNITION = POWER. Below it, a triangle diagram showing the three requirements for combustion (air, fuel, heat).

**Instructor Narration:**
> "Before we trace any pipes or identify any components, let's lock in the fundamental equation. Combustion requires three things — the fire triangle applies here just as it does in any fire: fuel, oxygen, and heat. In an engine, we supply air for the oxygen, fuel for the energy, and either a spark or compression for the heat. Remove any one of these three, and the engine stops.
>
> Today we focus on the first two — air and fuel. How they get into the engine, how the ECU controls their ratio, and where they meet inside the combustion chamber. Ignition timing gets its own days later this week."

**PPT Content:**
```
THE FUNDAMENTAL EQUATION

AIR + FUEL + IGNITION = POWER

The combustion triangle:
  1. OXYGEN (from air)    — the oxidiser
  2. FUEL (petrol/diesel) — the energy source
  3. HEAT (spark or compression) — the ignition source

Remove any one = no combustion = no power

TODAY: We trace AIR and FUEL
THIS WEEK: We add ignition, timing, and put it all together
```

---

#### Slide 4: Where Power Starts and Ends — The Powertrain Chain
**Visual:** Full powertrain diagram: Engine (crankshaft) --> Clutch/Torque Converter --> Gearbox --> Driveshaft --> Differential --> Half-shafts --> Wheels. Each stage labeled with what it does to the power.

**Instructor Narration:**
> "Before we go inside the engine, let's zoom out. Where does the power go after the engine makes it? The crankshaft spins — that's raw rotational power. It passes through a clutch or torque converter to the gearbox, which multiplies torque at the expense of speed. From the gearbox, a driveshaft carries the power to the differential, which splits it between the left and right wheels. That's the powertrain chain — engine to wheels.
>
> Why does this matter today? Because everything we study this week — air, fuel, combustion, timing — all exists to make that crankshaft spin. If you lose sight of that, the detail becomes meaningless. The crankshaft spinning is the output. Air and fuel are the inputs. Today is about the inputs."

**PPT Content:**
```
THE POWERTRAIN CHAIN — WHERE POWER STARTS AND ENDS

Engine (crankshaft)
  | — raw rotational power (torque + speed)
Clutch / Torque Converter
  | — connects/disconnects engine from drivetrain
Gearbox (manual / automatic / DCT / CVT)
  | — multiplies torque, selects ratio
Driveshaft / Propshaft
  | — transfers power to axle
Differential
  | — splits power left/right, allows speed difference in corners
Half-shafts / Axle shafts
  | — deliver power to individual wheels
Wheels
  | — convert rotation into vehicle motion

Everything this week exists to make the crankshaft spin.
```

---

### **DEVELOPMENT PART 1: The Four-Stroke Cycle and the Air Path** (Slides 5-14, ~35 minutes)

**Narrative Voice:** Methodical, building step by step. Use "trace it with me" language — you are leading them along a physical path.

---

#### Slide 5: The Four-Stroke Cycle — The Heartbeat of Every Engine
**Visual:** Four-panel animation/diagram showing all four strokes in sequence. Piston, connecting rod, crankshaft, valves, and spark plug visible. Crankshaft rotation marked (0-720 degrees).

**Instructor Narration:**
> "Every gasoline and diesel engine you will ever work on runs on the four-stroke cycle. It was invented in the 1870s, and every modern engine still uses it. Four strokes — intake, compression, power, exhaust — and two full rotations of the crankshaft to complete one cycle. Let's walk through each one.
>
> INTAKE: The piston moves down, the intake valve opens, and the cylinder fills with air — or an air-fuel mixture. COMPRESSION: Both valves close, the piston moves up, compressing the charge. POWER: The compressed charge ignites — by spark plug in gasoline, by compression heat alone in diesel — and the expanding gases force the piston down. This is the only stroke that produces power. EXHAUST: The exhaust valve opens, the piston pushes the burnt gases out. Then we start again.
>
> Four strokes. Two crankshaft revolutions. 720 degrees of rotation. This is the heartbeat of the engine."

**PPT Content:**
```
THE FOUR-STROKE CYCLE (OTTO CYCLE / DIESEL CYCLE)

STROKE 1 — INTAKE (0-180°)
  Piston moves DOWN | Intake valve OPEN | Cylinder fills with air/mixture

STROKE 2 — COMPRESSION (180-360°)
  Piston moves UP | Both valves CLOSED | Charge compressed
  Compression ratio: ~10:1 (gasoline) | ~20:1 (diesel)

STROKE 3 — POWER (360-540°)
  Charge IGNITES | Piston forced DOWN | Crankshaft receives power
  The ONLY stroke that produces useful work

STROKE 4 — EXHAUST (540-720°)
  Piston moves UP | Exhaust valve OPEN | Burnt gases expelled

= 4 strokes = 2 crankshaft revolutions = 720° per complete cycle
```

---

#### Slide 6: Gasoline vs Diesel — The Critical Differences
**Visual:** Side-by-side comparison diagram. Left: gasoline cylinder with spark plug firing. Right: diesel cylinder with injector spraying directly into highly compressed air. Key differences highlighted with callout boxes.

**Instructor Narration:**
> "The four strokes are the same in both engine types. The difference is in HOW ignition happens and HOW fuel enters. In a gasoline engine, fuel and air mix before or during the intake stroke, and a spark plug ignites the mixture at the top of compression. In a diesel engine, only air is drawn in during intake. The air is compressed to a much higher ratio — 20:1 versus about 10:1 for gasoline — and this extreme compression heats the air to over 500 degrees Celsius. Diesel fuel is then injected directly into this superheated air, and it ignites spontaneously. No spark plug needed.
>
> This single difference — spark ignition versus compression ignition — drives entirely different fuel systems, different combustion chamber shapes, different pressures, and different diagnostic approaches. You need to understand both."

**PPT Content:**
```
GASOLINE vs DIESEL — THE KEY DIFFERENCES

                    GASOLINE              DIESEL
Ignition method:    Spark plug            Compression heat
Fuel entry:         Port or direct inject Direct injection only
Compression ratio:  8:1 to 13:1          15:1 to 22:1
Compression temp:   ~400°C               ~700°C
Fuel type:          Petrol (volatile)     Diesel (less volatile)
Throttle:           Yes (controls air)    No (air unthrottled)*
Power control:      Air+fuel quantity     Fuel quantity only
Spark plug:         Yes                   No (glow plug for cold start)
Injection pressure: 3-350 bar            300-2500 bar

* Modern diesels may have a throttle for EGR control, not power control

SAME four-stroke cycle — DIFFERENT ignition and fuel delivery
```

---

#### Slide 7: The Air Path — Overview
**Visual:** Complete air path diagram from bumper intake to cylinder. Components in sequence: ram air scoop/grille opening --> air filter housing --> intake ducting --> mass air flow sensor (MAF) --> throttle body --> intake manifold plenum --> intake runners --> intake port --> intake valve --> cylinder. Each component numbered.

**Instructor Narration:**
> "Now let's trace the first input — air. Every engine needs a precise, measured quantity of clean air. The air path starts at the front of the car where ambient air enters, and ends inside the cylinder. Between those two points, the air is filtered, measured, metered, distributed, and finally drawn into the combustion chamber. Let's walk each component."

**PPT Content:**
```
THE AIR PATH — FROM ATMOSPHERE TO CYLINDER

AMBIENT AIR (outside the vehicle)
  |
  1. Air filter housing — removes dirt, debris, insects
  |
  2. Intake ducting — connects filter to throttle
  |
  3. Mass Air Flow sensor (MAF) — measures air quantity
  |
  4. Throttle body — controls air volume (gasoline engines)
  |
  5. Intake manifold plenum — collects and distributes air
  |
  6. Intake runners — individual tubes to each cylinder
  |
  7. Intake port — passage in cylinder head
  |
  8. Intake valve — opens/closes to admit air into cylinder
  |
  CYLINDER — where air meets fuel

Every component in this path affects engine performance.
A restriction ANYWHERE = less air = less power.
```

---

#### Slide 8: Air Filter — The First Line of Defence
**Visual:** Cross-section of an air filter housing showing the paper/fabric element. Inset: microscope view of filter media trapping particles. Second inset: dirty vs clean filter comparison.

**Instructor Narration:**
> "The air filter is the first component air passes through. Its job is simple but critical — remove dirt, dust, pollen, insects, and debris before they can enter the engine. Even small particles can score cylinder walls, damage valve seats, and contaminate oil.
>
> Most filters use a pleated paper or fabric element. When it gets clogged, airflow drops, the engine works harder to breathe, fuel economy decreases, and performance suffers. This is one of the most basic service items you'll handle — checking and replacing air filters. But don't underestimate it. A severely restricted filter can trigger diagnostic trouble codes and affect the entire fuel trim strategy."

**PPT Content:**
```
AIR FILTER — FIRST LINE OF DEFENCE

Job: Remove contaminants before they enter the engine

Filter media types:
  • Paper element (most common — disposable)
  • Cotton gauze (performance — reusable, oiled)
  • Foam (pre-filter or off-road applications)

Service indicators:
  • Visual inspection — hold up to light
  • Restriction sensor (some vehicles — pressure drop measurement)
  • Service interval — typically 20,000-40,000 km

What happens when clogged:
  • Reduced airflow = reduced power
  • Rich fuel mixture = increased fuel consumption
  • MAF sensor contamination (from bypass air)
  • Possible DTC: P0101 (MAF range/performance)
```

---

#### Slide 9: MAF Sensor — Measuring the Air
**Visual:** Cutaway of a hot-wire MAF sensor showing the sensing element in the airstream. Diagram showing how airflow cools the heated wire, changing its resistance.

**Instructor Narration:**
> "After the filter, air passes over the Mass Air Flow sensor — the MAF. This is the ECU's primary measurement of how much air is entering the engine. The most common type is the hot-wire MAF. It has a thin wire or film heated to a specific temperature above ambient. As air flows over it, it cools the wire. The more air, the more cooling, the more electrical current needed to maintain the temperature. The ECU reads this current and calculates the mass of air flowing — in grams per second.
>
> Why mass and not volume? Because the ECU needs to know the actual amount of oxygen entering the engine, and that depends on air density — which changes with temperature and altitude. A volume measurement would be inaccurate. Mass measurement accounts for all of that automatically.
>
> The MAF signal is one of the most important inputs to the fuel calculation. If this sensor is dirty or faulty, the fuel mixture goes wrong, and you get driveability complaints, poor fuel economy, and fault codes."

**PPT Content:**
```
MASS AIR FLOW SENSOR (MAF)

Job: Measure the MASS of air entering the engine (grams/second)

How it works (hot-wire type):
  • Heated sensing element in the air stream
  • Airflow cools the element
  • ECU measures current needed to maintain temperature
  • More air = more cooling = higher current = higher signal

Why MASS not VOLUME:
  • Mass = actual oxygen content
  • Accounts for temperature and altitude changes
  • Direct input for fuel calculation

Typical signal: 0-5V analog or digital frequency
  • Idle: ~3-5 g/s
  • Full load: ~100-200 g/s (varies by engine)

Common faults:
  • Contamination (oil film from aftermarket filter)
  • Broken wire element
  • DTC: P0100-P0104 range
```

---

#### Slide 10: Throttle Body — Controlling the Air
**Visual:** Electronic throttle body (drive-by-wire) shown from both sides. One view shows the butterfly valve, the other shows the DC motor and TPS (throttle position sensor). Diagram showing pedal position sensor --> ECU --> throttle motor.

**Instructor Narration:**
> "After the MAF, air reaches the throttle body. In a gasoline engine, this is the air metering device — the ECU controls how much air enters the engine by opening or closing a butterfly valve. In older cars, a cable connected the accelerator pedal directly to the throttle. Modern cars use drive-by-wire: the pedal has a position sensor, the ECU reads it, and an electric motor opens the throttle to the calculated position.
>
> The throttle position sensor tells the ECU exactly how far open the valve is. This feedback loop — pedal position in, throttle position out, MAF measuring the result — is the core of air control.
>
> Here's a key difference for diesel: most diesels don't use a throttle to control power. Power is controlled by fuel quantity alone. If you see a throttle on a diesel, it's usually there for EGR control or to create intake vacuum for the brake booster — not for power regulation."

**PPT Content:**
```
THROTTLE BODY — CONTROLLING AIRFLOW

Job: Regulate the volume of air entering the intake manifold
Type: Electronic (drive-by-wire) — no cable, ECU-controlled

Components:
  • Butterfly valve — opens/closes to control airflow
  • DC motor — actuates the butterfly
  • Throttle Position Sensor (TPS) — feedback to ECU
  • Return spring — fail-safe: closes throttle if motor fails

Control loop:
  Accelerator Pedal Position Sensor
    --> ECU calculates desired throttle opening
      --> DC motor opens butterfly
        --> TPS confirms actual position
          --> MAF measures resulting airflow

GASOLINE: Throttle controls power (air quantity)
DIESEL: Throttle for EGR/vacuum only (power = fuel quantity)

Common faults:
  • Carbon buildup on butterfly edge (rough idle)
  • TPS signal erratic (hesitation, surging)
  • DTC: P0120-P0124, P2111, P2112
```

---

#### Slide 11: Intake Manifold — Distributing the Air
**Visual:** Intake manifold removed from an engine, showing plenum chamber and individual runners. Cutaway view showing internal geometry. Inset: variable-length intake runner mechanism.

**Instructor Narration:**
> "After the throttle, air enters the intake manifold. Think of it as a distribution centre. The plenum is a large chamber that collects the air, and individual runners deliver air to each cylinder. The design of these runners — their length, diameter, and shape — directly affects engine performance.
>
> Many modern engines use variable-length intake runners. At low RPM, long runners improve torque by creating a ram effect. At high RPM, shorter runners flow more air for peak power. A flap or valve mechanism switches between the two. This is controlled by — you guessed it — the ECU.
>
> The manifold also contains the fuel injectors on port-injection engines, vacuum ports for brake boosters and emissions systems, and sometimes a manifold air temperature sensor. It's more than just a pipe — it's a precision-engineered air distribution system."

**PPT Content:**
```
INTAKE MANIFOLD — AIR DISTRIBUTION

Job: Distribute metered air evenly to all cylinders

Components:
  • Plenum chamber — collects air from throttle body
  • Intake runners — individual tubes to each cylinder port
  • Runner flaps (variable geometry) — optimise for low/high RPM
  • Gaskets — seal manifold to cylinder head

Design matters:
  • Long runners = better low-RPM torque (ram effect)
  • Short runners = better high-RPM airflow (power)
  • Variable length = best of both (ECU-controlled flaps)

Also found on/in the manifold:
  • Port fuel injectors (port injection engines)
  • Manifold Air Temperature (MAT/IAT) sensor
  • Vacuum ports (brake booster, PCV, EVAP purge)
  • Tumble/swirl flaps (improve air motion in cylinder)

Material: Plastic (weight saving) or aluminium (older/performance)
```

---

#### Slide 12: Into the Cylinder — Intake Port and Valve
**Visual:** Cross-section of a cylinder head showing the intake port passage, valve, valve seat, valve spring, and the opening into the combustion chamber. Arrow showing air flow path.

**Instructor Narration:**
> "The final section of the air path is inside the cylinder head itself. Air flows from the intake runner through the intake port — a carefully shaped passage cast into the head — past the intake valve, and into the combustion chamber.
>
> The intake valve is the gatekeeper. It opens during the intake stroke and closes during compression. Its timing, lift, and duration determine how much air actually fills the cylinder. Modern engines often have two intake valves per cylinder to increase flow area. The shape of the port — whether it creates tumble or swirl motion — affects how well the air mixes with fuel inside the combustion chamber.
>
> We'll study valve timing in detail on Day 14. Today, just understand: this is where the air path ends. Air has travelled from the atmosphere, through the filter, past the MAF, through the throttle, into the manifold, down the runner, through the port, past the valve, and into the cylinder. That's the complete air journey."

**PPT Content:**
```
INTO THE CYLINDER — INTAKE PORT & VALVE

Intake port:
  • Shaped passage cast into the cylinder head
  • Designed to create specific air motion:
    - Tumble (vertical rotation) — common in modern gasoline
    - Swirl (horizontal rotation) — common in diesel
  • Port shape directly affects combustion efficiency

Intake valve:
  • Opens during intake stroke, closes during compression
  • Typical: 2 intake valves per cylinder (4V total with exhaust)
  • Larger diameter than exhaust valve (engine needs more air in than out)
  • Valve seat — precision ground seal in cylinder head

Valve control:
  • Camshaft lobe pushes valve open (via lifter/rocker)
  • Valve spring pulls valve closed
  • Clearance must be correct (Day 14 topic)

THE AIR PATH IS NOW COMPLETE:
Filter → MAF → Throttle → Manifold → Runner → Port → Valve → Cylinder
```

---

#### Slide 13: Air Path Summary — The Complete Journey
**Visual:** Single clean diagram showing the entire air path from atmosphere to cylinder with all components labeled and numbered. Flow direction arrows.

**Instructor Narration:**
> "Let's lock this in. Here's the complete air path in one view. Ambient air enters through the grille area, passes through the air filter to remove contaminants, flows past the MAF sensor where its mass is measured, through the throttle body where its volume is controlled, into the intake manifold where it's distributed, down individual runners, through the intake port in the cylinder head, past the intake valve, and into the cylinder.
>
> Eight components. One path. If anything in this path is restricted, leaking, or measured incorrectly, the engine will not run properly. As a technician, when a customer complains about poor power or fuel economy, one of your first checks is this air path — end to end."

**PPT Content:**
```
THE COMPLETE AIR PATH — SUMMARY

1. AMBIENT AIR (atmosphere)
2. AIR FILTER (clean the air)
3. MAF SENSOR (measure the air — grams/second)
4. THROTTLE BODY (control the air — butterfly valve)
5. INTAKE MANIFOLD PLENUM (collect the air)
6. INTAKE RUNNERS (distribute to each cylinder)
7. INTAKE PORT (passage in cylinder head)
8. INTAKE VALVE (admit air into combustion chamber)
9. CYLINDER (destination — air meets fuel here)

KEY PRINCIPLE: Any restriction, leak, or measurement error
in this path affects engine performance.

Diagnostic approach: Check filter → Check MAF → Check throttle →
Check manifold for leaks → Check valve operation
```

---

#### Slide 14: Quick Knowledge Check — Air Path
**Visual:** Diagram of the air path with component labels removed — numbered blank boxes for learners to fill in.

**Instructor Narration:**
> "Quick check before we move to fuel. I'm putting the air path diagram on screen with the labels removed. In your notebook, number 1 through 8 and write the name of each component in the correct order. You have 2 minutes. Then we'll call them out together."

**PPT Content:**
```
KNOWLEDGE CHECK — NAME THE AIR PATH COMPONENTS

[Diagram with 8 blank numbered boxes along the air path]

1. _______________
2. _______________
3. _______________
4. _______________
5. _______________
6. _______________
7. _______________
8. _______________

Write them in order. You have 2 minutes.
```

**Activity:** Individual written recall (2 min) --> group callout to fill in the blanks on screen (3 min). Instructor corrects any errors.

---

### **DEVELOPMENT PART 2: The Fuel Path and ECU Coordination** (Slides 15-21, ~25 minutes)

**Narrative Voice:** Same methodical tracing approach as the air path. Build the parallel mental map.

---

#### Slide 15: The Fuel Path — Overview
**Visual:** Complete fuel path diagram: Fuel tank --> fuel pump (in-tank) --> fuel filter --> fuel lines --> fuel rail --> fuel pressure regulator --> injectors --> cylinder. Return line shown (older systems). Each component numbered.

**Instructor Narration:**
> "Now the second input — fuel. The fuel system's job is to store fuel safely, deliver it at the right pressure, and inject the precise quantity into each cylinder at exactly the right moment. Let's trace it from tank to injector, just like we traced air from filter to valve."

**PPT Content:**
```
THE FUEL PATH — FROM TANK TO CYLINDER

FUEL TANK (stores fuel safely)
  |
  1. Fuel pump (usually in-tank, electric) — pressurises fuel
  |
  2. Fuel filter — removes particles and water
  |
  3. Fuel lines — carry pressurised fuel to engine
  |
  4. Fuel rail — distributes fuel to all injectors
  |
  5. Fuel pressure regulator — maintains correct system pressure
  |
  6. Fuel injectors — spray precise quantity into port or cylinder
  |
  CYLINDER — where fuel meets air

GASOLINE: 3-5 bar (port injection) or 50-350 bar (direct injection)
DIESEL: 300-2500 bar (common rail direct injection)
```

---

#### Slide 16: Fuel Tank and Pump — Where It All Starts
**Visual:** Cutaway of an in-tank fuel pump module showing the electric pump, fuel level sender, strainer sock, and fuel supply/return connections. Inset: fuel tank with baffles visible.

**Instructor Narration:**
> "The fuel tank stores 40 to 80 litres of fuel in most cars. It's made of plastic — blow-moulded HDPE — and designed with internal baffles to prevent fuel sloshing during cornering and braking. Inside the tank, you'll find the fuel pump module — this is an electric pump, typically a roller-cell or turbine type, that pushes fuel through the system.
>
> Modern fuel pumps can deliver 3 to 5 bar for port injection or feed a high-pressure pump for direct injection systems. The pump runs whenever the ignition is on, and the ECU can vary its speed in some systems to match demand. At the bottom of the pump module, a strainer sock filters large debris. A separate fine fuel filter — either inline or integrated into the pump module — catches smaller particles.
>
> One thing to remember: the fuel also cools the pump. If you run a tank nearly empty regularly, the pump overheats. This is a real-world cause of fuel pump failure."

**PPT Content:**
```
FUEL TANK AND PUMP

Fuel tank:
  • Material: HDPE plastic (most modern vehicles)
  • Capacity: 40-80 litres typical
  • Internal baffles prevent fuel sloshing
  • Evaporative emissions controls (EVAP system — sealed tank)

In-tank fuel pump module:
  • Electric pump (roller-cell or turbine type)
  • Fuel level sender (float and resistor for gauge)
  • Strainer sock (coarse filtration at pump inlet)
  • Electrical connector and fuel line fittings

Fuel pressure (low-pressure circuit):
  • Port injection: 3-5 bar
  • Feed to high-pressure pump (GDI): 3-7 bar
  • Diesel feed pump: 3-10 bar

Service note: Low fuel level = pump overheating risk
  Running on empty shortens pump life
```

---

#### Slide 17: Fuel Filter and Lines — Clean Fuel Delivery
**Visual:** Inline fuel filter (cutaway showing paper element) and under-body fuel lines. Inset: comparison of clean vs contaminated fuel filter.

**Instructor Narration:**
> "Fuel filtration is critical. Even tiny particles — 10 microns or smaller — can damage injector tips, clog pintles, and cause spray pattern problems. Diesel systems are even more sensitive because of the extreme pressures in common rail injection — some systems operate at over 2000 bar. At those pressures, a speck of dirt acts like sandpaper.
>
> Some vehicles have a replaceable inline fuel filter under the body. Many modern gasoline vehicles integrate the filter into the pump module — it's a lifetime component that isn't individually serviceable. Diesel vehicles almost always have a separate replaceable filter, often with a water separator because water in diesel fuel causes corrosion and injector damage.
>
> The fuel lines themselves are steel, nylon, or reinforced rubber, routed along the underside of the vehicle and connected with quick-release fittings. Always inspect lines for corrosion, rubbing, and leaks during underbody inspection."

**PPT Content:**
```
FUEL FILTER AND LINES

Fuel filter:
  • Gasoline: Often integrated into pump module (non-serviceable)
    or inline under body (replaceable every 40,000-80,000 km)
  • Diesel: ALWAYS a serviceable filter (10,000-40,000 km interval)
    — Includes water separator (water sensor triggers warning light)
  • Filtration: 5-10 microns typical

Why filtration matters:
  • Protects injector tips from erosion
  • Prevents clogged injector spray patterns
  • Diesel: prevents rust and bacterial growth from water

Fuel lines:
  • Material: Steel, nylon, reinforced rubber/Teflon
  • Connections: Quick-release clips or threaded fittings
  • Routing: Along underbody, protected from road debris
  • Inspection: Check for corrosion, chafing, leaks, kinks
```

---

#### Slide 18: Fuel Rail and Injectors — Precision Delivery
**Visual:** Fuel rail assembly removed from engine, with injectors attached. Cutaway of a port injector showing solenoid, pintle, and spray pattern. Second cutaway of a GDI (gasoline direct injection) injector showing higher-pressure design.

**Instructor Narration:**
> "The fuel rail is a metal tube that distributes pressurised fuel evenly to all injectors. It maintains a common pressure so that each injector receives the same feed. A fuel pressure regulator — either mechanical (vacuum-referenced) on older systems or electronically controlled on newer ones — holds the rail at the target pressure.
>
> The injectors are the precision end of the fuel system. A port injector is an electromagnetic solenoid valve — the ECU sends a pulse, the solenoid lifts a pintle off its seat, and fuel sprays into the intake port. The duration of the pulse — called the injector pulse width, measured in milliseconds — determines how much fuel enters. Longer pulse = more fuel. Direct injection works the same way but operates at much higher pressure and sprays directly into the combustion chamber.
>
> This is where all the ECU's air and fuel calculations become physical. The injector is the final actuator in the fuel path."

**PPT Content:**
```
FUEL RAIL AND INJECTORS — PRECISION DELIVERY

Fuel rail:
  • Common pressure reservoir for all injectors
  • Material: Aluminium or steel
  • Contains fuel pressure sensor (ECU monitors rail pressure)
  • Fuel pressure regulator: mechanical or electronic

Fuel injectors:
PORT INJECTION                    DIRECT INJECTION (GDI)
  Sprays into intake port           Sprays into combustion chamber
  Pressure: 3-5 bar                 Pressure: 50-350 bar (gasoline)
  Solenoid-operated                 Solenoid or piezo-operated
  Simple design, reliable           Complex, higher precision
  Good fuel atomisation             Better fuel economy, more power

Injector control:
  • ECU sends voltage pulse to solenoid
  • Pulse width (ms) = fuel quantity
  • Short pulse = lean mixture | Long pulse = rich mixture
  • Timed to open during correct engine phase

Common faults: Clogged spray, leaking seat, dead coil
  DTC: P0200-P0208 range (injector circuit)
```

---

#### Slide 19: Fuel Path Summary — The Complete Journey
**Visual:** Single clean diagram showing the entire fuel path from tank to cylinder with all components labeled and numbered. Flow direction arrows.

**Instructor Narration:**
> "Let's lock in the fuel path just as we did with the air path. Fuel sits in the tank. The electric pump pressurises it and pushes it through the filter, along the fuel lines, into the rail. The rail distributes it evenly to all injectors. The pressure regulator maintains target pressure. And the injectors, commanded by the ECU, spray the precise quantity of fuel either into the intake port or directly into the cylinder.
>
> Six components. One path. Together with the air path, you now have the engine's two complete input maps."

**PPT Content:**
```
THE COMPLETE FUEL PATH — SUMMARY

1. FUEL TANK (store fuel safely)
2. FUEL PUMP (pressurise and deliver — electric, in-tank)
3. FUEL FILTER (clean the fuel — remove particles and water)
4. FUEL LINES (carry fuel from tank to engine)
5. FUEL RAIL (distribute to all injectors at common pressure)
6. FUEL PRESSURE REGULATOR (maintain target pressure)
7. FUEL INJECTORS (spray precise quantity — ECU controlled)
8. CYLINDER (destination — fuel meets air here)

KEY PRINCIPLE: Correct fuel pressure + clean fuel + precise
injector timing = proper combustion

Diagnostic approach: Check fuel pressure → Check filter condition →
Check injector spray pattern → Check fuel trim data
```

---

#### Slide 20: The ECU — Conductor of the Orchestra
**Visual:** Central ECU diagram with sensor inputs on the left (MAF, MAP, TPS, RPM, O2/lambda, coolant temp, intake air temp, crank position) and actuator outputs on the right (injectors, ignition coils, throttle motor, idle air control, EVAP purge). Fuel map 3D surface plot inset.

**Instructor Narration:**
> "You've traced both paths — air and fuel. Now, who coordinates them? The Engine Control Unit — the ECU. Remember what you learned in Week 2: the ECU reads sensors, processes data, and commands actuators. For the engine, the critical calculation is: how much fuel do I inject for the amount of air entering each cylinder?
>
> The ECU uses a fuel map — a three-dimensional lookup table stored in its memory. The axes are engine speed and engine load. For every combination, the map contains a base injector pulse width. But the ECU doesn't just use the base map — it constantly adjusts. The lambda sensor in the exhaust measures the actual air-fuel ratio of the burnt gases and sends feedback. If the mixture is too lean, the ECU adds fuel. Too rich, it reduces fuel. This is called closed-loop fuel control.
>
> The target for gasoline engines is the stoichiometric ratio — 14.7 parts air to 1 part fuel by mass. At this ratio, the catalytic converter works most efficiently. Lambda equals 1.0 at stoichiometric. Greater than 1.0 means lean. Less than 1.0 means rich. You'll use a scan tool to read these values on almost every diagnostic job."

**PPT Content:**
```
THE ECU — COORDINATING AIR AND FUEL

KEY SENSORS (inputs):                KEY ACTUATORS (outputs):
  • MAF / MAP sensor (air quantity)    • Fuel injectors (fuel quantity)
  • Throttle position sensor           • Throttle motor (air control)
  • Crankshaft position sensor (RPM)   • Ignition coils (spark timing)
  • Camshaft position sensor           • EVAP purge valve
  • Coolant temperature sensor         • Variable valve timing solenoids
  • Intake air temperature sensor      • Turbo wastegate/VGT actuator
  • Lambda / O2 sensor (exhaust)
  • Knock sensor

FUEL MAP: 3D lookup table
  X-axis: Engine speed (RPM)
  Y-axis: Engine load (air mass)
  Z-axis: Injector pulse width (ms)

CLOSED-LOOP CONTROL:
  Lambda sensor feedback --> ECU adjusts fuel trim
  Target: Lambda = 1.0 (stoichiometric = 14.7:1 air:fuel by mass)
  Lambda > 1.0 = LEAN (too much air / too little fuel)
  Lambda < 1.0 = RICH (too little air / too much fuel)
```

---

#### Slide 21: Engine Block and Cylinder Head — Where Air and Fuel Meet
**Visual:** Exploded view of engine block and cylinder head. Block showing cylinder bores, crankshaft journals, water jackets, oil galleries. Head showing combustion chambers, valve seats, ports, camshaft mounts. Assembled view showing head gasket sandwiched between.

**Instructor Narration:**
> "We've traced air and fuel to the cylinder. Now let's look at the physical structure where they meet — the engine block and cylinder head.
>
> The engine block is the foundation. It contains the cylinder bores — the precision-machined tubes the pistons slide in. Below the bores, the crankshaft rotates in main bearing journals. Cooling water jackets surround the bores, and oil galleries run through the block to lubricate everything. The block is cast iron or aluminium alloy — iron for strength and cost, aluminium for weight saving.
>
> The cylinder head bolts to the top of the block with a head gasket sealing between them. The head contains the combustion chambers — the shape of this chamber directly affects how the air-fuel mixture burns. It also houses the intake and exhaust ports, valve seats, valve guides, and the camshaft or camshaft mounts. On gasoline engines, the spark plug threads into the head. On direct injection engines, the injector also mounts in the head.
>
> The combustion chamber shape — whether it's pent-roof, hemispherical, or swirl-chamber — determines the turbulence, flame propagation, and efficiency of combustion. Different engines use different geometries depending on whether they prioritise power, efficiency, or emissions. We'll examine these up close in the practical session."

**PPT Content:**
```
ENGINE BLOCK AND CYLINDER HEAD — THE MEETING POINT

ENGINE BLOCK (lower structure):
  • Cylinder bores — pistons reciprocate here
  • Crankshaft main bearing journals
  • Water jackets — cooling passages
  • Oil galleries — lubrication passages
  • Material: Cast iron or aluminium alloy

CYLINDER HEAD (upper structure):
  • Combustion chambers — where combustion occurs
  • Intake and exhaust ports — air in, exhaust out
  • Valve seats and guides — valve sealing surfaces
  • Spark plug / injector bosses — mount into head
  • Camshaft mounts (OHC engines)

HEAD GASKET (between block and head):
  • Seals combustion pressure, coolant, and oil
  • Multi-layer steel (MLS) most common modern type
  • Failure = coolant in oil, oil in coolant, compression loss

Combustion chamber shapes:
  • Pent-roof (most common modern — good tumble motion)
  • Hemispherical (performance — large valve area)
  • Swirl chamber (older diesel — pre-chamber design)
```

---

### **PRACTICAL: Hands-On Engine Exploration** (Slides 22-25, ~75 minutes)

**Narrative Voice:** Workshop guide. Move to practical stations.

---

#### Slide 22: Practical Station Setup
**Visual:** Workshop layout diagram showing four practical stations: (1) Cutaway engine / animation station, (2) Air path tracing station, (3) Fuel path tracing station, (4) Engine block/head identification station.

**Instructor Narration:**
> "Time to get your hands involved. I've set up four stations, and you'll rotate through all of them. Each station has a specific task tied to what we just covered in theory. You'll work in pairs at each station for about 15 minutes before rotating. Station 1 is the four-stroke cycle — I have a cutaway engine and animation for you to identify each stroke. Station 2 is the air path — you'll trace every component from filter to manifold on a real engine. Station 3 is the fuel path — tank, pump, rail, injectors. Station 4 is block and head identification — cylinders, combustion chambers, valves, ports.
>
> At each station, fill in the worksheet. Every component you identify and correctly label earns a tick. Your goal: 100% of components identified correctly across all four stations. Let's go."

**PPT Content:**
```
PRACTICAL SESSION — FOUR STATIONS (75 minutes)

STATION 1: Four-Stroke Cycle (15 min)
  — Cutaway engine or animation
  — Identify each stroke, valve positions, piston movement
  — Describe gasoline vs diesel ignition difference

STATION 2: Trace the Air Path (15 min)
  — Real engine in bay
  — Start at air filter, end at intake manifold
  — Identify: filter, MAF, throttle body, manifold, runners

STATION 3: Trace the Fuel Path (15 min)
  — Identify: tank location, pump access, filter, lines, rail, injectors
  — Note fuel pressure specification from service data

STATION 4: Block & Head Identification (15 min)
  — Cylinder bores, crankshaft journals, water jackets
  — Combustion chambers, valve seats, ports, spark plug holes

Complete the worksheet at each station.
Remaining time: Group debrief and Q&A (15 min)
```

---

#### Slide 23: Station 1 — Four-Stroke Cycle Demonstration
**Visual:** Photo of a sectioned/cutaway engine on a stand, or screenshot of a detailed four-stroke animation software. Worksheet excerpt showing blank boxes for each stroke.

**Instructor Narration:**
> "At this station, use the cutaway engine to physically see the piston moving through all four strokes. Turn the crankshaft by hand — slowly — and watch the valves open and close. For each stroke, write down: which direction the piston moves, which valves are open, and what is happening to the charge inside the cylinder. Then answer: what is the key difference between the gasoline and diesel power stroke?"

**PPT Content:**
```
STATION 1: FOUR-STROKE CYCLE

Task: Rotate crankshaft by hand. Observe and record:

INTAKE STROKE:
  Piston direction: _______
  Intake valve: Open / Closed
  Exhaust valve: Open / Closed
  What happens: _______________________

COMPRESSION STROKE:
  Piston direction: _______
  Both valves: Open / Closed
  What happens: _______________________

POWER STROKE:
  Piston direction: _______
  Ignition source (gasoline): _______________
  Ignition source (diesel): _______________

EXHAUST STROKE:
  Piston direction: _______
  Exhaust valve: Open / Closed
  What happens: _______________________
```

---

#### Slide 24: Station 2 & 3 — Air and Fuel Path Tracing
**Visual:** Annotated engine bay photo with numbered callout boxes along both the air path and fuel path. Some labels visible, some blank for student identification.

**Instructor Narration:**
> "Stations 2 and 3 work the same way but for different paths. At the air path station, start at the air filter box — physically put your finger on it — and trace the path all the way to the intake manifold. At each component, write its name and function on your worksheet. At the fuel path station, locate the fuel rail and injectors on the engine, trace back to the fuel filter if visible, and note where the fuel tank and pump are located. Use the service data sheet to find the specified fuel pressure."

**PPT Content:**
```
STATION 2: TRACE THE AIR PATH (on the workshop vehicle)

Starting at the air filter, physically trace and identify:
  [ ] Air filter housing — open it, inspect the element
  [ ] Intake ducting — material? condition?
  [ ] MAF sensor — locate the connector, note the wire colours
  [ ] Throttle body — find the butterfly, find the TPS connector
  [ ] Intake manifold — count the runners, find vacuum ports

STATION 3: TRACE THE FUEL PATH

Starting at the fuel rail, trace and identify:
  [ ] Fuel rail — material? number of injector ports?
  [ ] Fuel injectors — count them, note connector type
  [ ] Fuel pressure sensor/regulator — where on the rail?
  [ ] Fuel lines — trace toward tank as far as visible
  [ ] Fuel filter — locate (under body or in-tank?)
  [ ] Look up: specified fuel pressure for this engine: ____ bar
```

---

#### Slide 25: Station 4 — Block and Head Identification
**Visual:** Photo of a cylinder head removed from a block, sitting on a workbench. Combustion chambers visible from below. Block with pistons visible from above. Key features labeled with leader lines.

**Instructor Narration:**
> "At this station, you have a cylinder head and an engine block to examine. On the block, look down into the cylinder bores — can you see the cross-hatch honing pattern? That pattern holds oil to lubricate the piston rings. Find the crankshaft bearing journals. Look for the water jacket openings and oil gallery holes in the deck surface.
>
> On the head, flip it over and look at the combustion chambers from below. Count the valves per cylinder. Identify the intake and exhaust valves — the intake valves are always larger. Find the spark plug hole. Look at the shape of the combustion chamber — is it pent-roof or hemispherical? Note the valve seat surfaces and the port entries."

**PPT Content:**
```
STATION 4: BLOCK AND HEAD IDENTIFICATION

ON THE ENGINE BLOCK:
  [ ] Cylinder bores — count cylinders, note bore condition
  [ ] Cross-hatch honing marks visible? (magnifying glass provided)
  [ ] Crankshaft main bearing journals (or caps)
  [ ] Water jacket openings on deck surface
  [ ] Oil gallery holes on deck surface
  [ ] Block material: cast iron or aluminium?

ON THE CYLINDER HEAD:
  [ ] Combustion chamber shape — pent-roof / hemispherical / other
  [ ] Valves per cylinder — count intake and exhaust
  [ ] Intake valve size vs exhaust valve size — which is larger?
  [ ] Spark plug holes — note thread angle and depth
  [ ] Intake ports — look into port from manifold side
  [ ] Exhaust ports — look into port from exhaust side
  [ ] Valve seats — note the machined contact surface

Draw and label ONE combustion chamber in your notebook.
```

---

### **WRAP-UP: Consolidation & Preview** (Slides 26-28, ~15 minutes)

---

#### Slide 26: Two Paths, One Destination
**Visual:** Split-screen diagram. Left side: complete air path (blue arrows). Right side: complete fuel path (red arrows). Both converge at the combustion chamber in the centre.

**Instructor Narration:**
> "Let's bring it all together. Today you traced two paths — air and fuel — from their starting points to the combustion chamber where they meet. Air: atmosphere through filter, MAF, throttle, manifold, port, and valve into the cylinder. Fuel: tank through pump, filter, lines, rail, and injector into the cylinder. The ECU coordinates both using sensor feedback and fuel maps. The four-stroke cycle provides the mechanical framework. And the block and head are the physical structure where it all happens.
>
> This is the foundation of everything we do this week. Tomorrow, we go deep into the gasoline fuel and ignition systems — how the fuel is pressurised, how the spark is generated, and how ignition timing works. Every detail tomorrow builds directly on the two paths you learned today."

**PPT Content:**
```
TWO PATHS — ONE DESTINATION

AIR PATH (blue):                    FUEL PATH (red):
  Atmosphere                          Fuel tank
    → Air filter                        → Fuel pump
      → MAF sensor                        → Fuel filter
        → Throttle body                     → Fuel lines
          → Intake manifold                   → Fuel rail
            → Intake runner                     → Pressure regulator
              → Intake port                       → Injector
                → Intake valve
                    ↘                           ↙
                      COMBUSTION CHAMBER
                          ↓
                    FOUR-STROKE CYCLE
                          ↓
                    CRANKSHAFT ROTATION
                          ↓
                    POWER TO WHEELS

The ECU coordinates BOTH paths using sensors and fuel maps.
```

---

#### Slide 27: What You Learned Today
**Visual:** Checklist with tick marks against each objective.

**Instructor Narration:**
> "Let's check off what you achieved today. You can now describe the complete powertrain chain from crankshaft to wheels. You can explain the four-stroke cycle and tell me how gasoline and diesel differ. You can trace the complete air path — eight components from filter to valve. You can trace the complete fuel path — seven components from tank to injector. You understand how the ECU uses the MAF, lambda sensor, and fuel maps to coordinate the mixture. And you've physically identified cylinder bores, combustion chambers, valves, and ports on real engine components.
>
> That's a full day's work. And it gives you the map that everything else this week attaches to."

**PPT Content:**
```
DAY 11 RECAP — YOU CAN NOW:

  Name the powertrain chain: engine to wheels
  Explain the four-stroke cycle (intake, compression, power, exhaust)
  Identify the gasoline vs diesel ignition difference
  Trace the COMPLETE air path (8 components)
  Trace the COMPLETE fuel path (7 components)
  Explain the ECU's role in air-fuel coordination
  Define lambda and stoichiometric ratio (14.7:1)
  Identify block and head features (bores, chambers, valves, ports)

Week 3 exam weight: 18 marks (18%)
Everything this week builds on today's two paths.
```

---

#### Slide 28: Day 12 Preview — Gasoline Fuel Delivery and Ignition
**Visual:** Close-up image of a direct injection fuel system and coil-on-plug ignition coil assembly.

**Instructor Narration:**
> "Tomorrow we go deep into gasoline systems. You'll learn how port injection differs from direct injection, how fuel pressure is regulated in each system, how the ignition system generates 40,000 volts from a 12-volt battery, and how ignition timing affects power, economy, and emissions. We'll also do a hands-on injector and spark plug inspection practical. If today was the overview, tomorrow is the close-up. See you then."

**PPT Content:**
```
DAY 12 PREVIEW: GASOLINE FUEL DELIVERY & IGNITION

Topics:
  • Port injection vs direct injection (GDI) — systems compared
  • Fuel pressure regulation — mechanical vs electronic
  • Ignition system: battery → coil → spark plug (40,000V from 12V)
  • Coil-on-plug vs distributor vs wasted spark
  • Ignition timing and knock control
  • Hands-on: Injector inspection and spark plug reading

Bring your notebook and PPE. Tomorrow we spark things up.
```

---

## Assessment Checkpoint

**Formative (not graded):**
- Quick knowledge check (Slide 14): Name all 8 air path components in order
- Practical worksheet: Correctly identify and label components at all 4 stations
- Verbal questions during stations: "What happens if this component fails?"
- Exit question: "Explain the difference between how a gasoline engine and a diesel engine ignite their fuel."

**Summative preparation (contributes to Week 3 exam — 18 marks):**
- Air path component identification (name, function, location)
- Fuel path component identification (name, function, location)
- Four-stroke cycle stroke identification with valve positions
- Gasoline vs diesel comparison (ignition method, compression ratio, fuel entry)
- Lambda / stoichiometric ratio definition

---

## Key Takeaways

1. An engine needs exactly two inputs — air and fuel — coordinated by the ECU and ignited at the right moment
2. The four-stroke cycle (intake, compression, power, exhaust) is the heartbeat of every gasoline and diesel engine — the key difference is spark ignition vs compression ignition
3. The air path has 8 components from atmosphere to cylinder — any restriction or leak in this path affects performance
4. The fuel path has 7 components from tank to cylinder — correct pressure and clean fuel are essential for proper injection
5. The ECU uses the MAF sensor, lambda sensor, and stored fuel maps to continuously calculate and adjust the air-fuel mixture
6. The engine block and cylinder head form the physical structure where air and fuel meet — combustion chamber geometry directly affects efficiency

---

## Preparation for Day 12

**Instructor prep:**
- Prepare a set of used spark plugs showing different conditions (normal, rich, lean, fouled, worn)
- Source a fuel injector test rig or demonstration injector with visible spray pattern capability
- Ensure a coil-on-plug assembly is available for hands-on inspection
- Prepare ignition system circuit diagrams for the workshop vehicle
- Have service data available showing fuel pressure specifications and ignition timing specs
- Print fuel trim and lambda data screenshots from a scan tool for classroom reference

**Learner prep:**
- Review the air path and fuel path diagrams from today — be able to draw both from memory
- Review the four-stroke cycle — know what happens at each stroke and which valves are open/closed
- Bring PPE for practical session (safety glasses, gloves)
