---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 3
week_title: "The Heart — Engine Systems"
day_number: 13
session_title: "Diesel Fuel Delivery & Intake Control"
duration_minutes: 180
theory_practice: "55:45"
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 13: Diesel Fuel Delivery & Intake Control
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (100 min theory + 80 min practical)
**Approach:** Comparison-Driven — Build on Day 12 Gasoline Knowledge, Contrast with Diesel
**PPT Target:** 26-28 slides
**Week:** 3 of 8 — "The Heart — Engine Systems"

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Describe the complete Common Rail diesel fuel system from tank to injector
- Explain the function of the high-pressure pump, rail, pressure sensor, and pressure regulator
- Distinguish between solenoid and piezo diesel injectors
- Explain multi-injection strategy (pilot, main, post) and why it matters
- List at least five key differences between diesel and gasoline fuel systems
- Describe the purpose of glow plugs and how they differ from spark plugs
- Explain the function of swirl flaps and variable intake geometry
- Describe the EGR system — valve, cooler, purpose, carbon buildup, and testing methods
- Read diesel-specific diagnostic trouble codes on a scan tool

**Connection to Day 12:** Yesterday covered gasoline fuel delivery — port injection, direct injection, fuel pressures up to 200 bar. Today we step into an entirely different world: diesel. The pressures are ten times higher, there are no spark plugs, and the injection strategy is far more complex. Learners should constantly compare what they learned yesterday with what they learn today.

---

## Connection to Prior Knowledge

Build from Day 12 (Gasoline Fuel Delivery):
- Learners already understand fuel tanks, fuel pumps, fuel filters, and fuel rails
- They know what an injector does (spray fuel into the cylinder)
- They understand fuel pressure as a concept
- They have seen a scan tool read fuel system DTCs

**Bridge:** "Yesterday you learned how a gasoline engine gets its fuel — low-pressure pump to high-pressure pump, rail, injectors, 200 bar at most. Today we enter diesel territory. Same basic idea — get fuel from the tank into the cylinder — but the engineering is completely different. The pressures are staggering. The injection events happen multiple times per combustion cycle. And there's no spark plug at all. If you understood yesterday, today will make sense — but it will also blow your mind."

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: The Diesel Difference** (Slides 1-3, ~10 minutes)

**Narrative Voice:** Dramatic contrast. Establish that diesel is a fundamentally different engineering approach to the same problem.

---

#### Slide 1: Title & Context
**Visual:** Split-screen image — left side shows a gasoline direct injection system (from Day 12), right side shows a Common Rail diesel system with massive high-pressure pump and thick steel rail. Title overlay.

**Instructor Narration:**
> "Yesterday we explored gasoline fuel delivery. You learned about port injection, direct injection, and fuel pressures up to 200 bar. Today, forget all of that — or rather, hold it in the back of your mind, because diesel is a completely different animal. Diesel engines don't use spark plugs. They compress air so hot that fuel ignites on contact. And the pressures involved are staggering — up to 2,500 bar. That's over 36,000 PSI. It's 100 times the pressure in your car tyre. It's enough pressure to cut through steel. This is diesel."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 3: The Heart — Engine Systems
Day 13: Diesel Fuel Delivery & Intake Control

Yesterday: Gasoline — spark ignition, up to 200 bar
Today: Diesel — compression ignition, up to 2,500 bar

Same goal. Completely different engineering.
```

---

#### Slide 2: Why Diesel Exists
**Visual:** Side-by-side efficiency comparison chart — diesel vs gasoline thermal efficiency percentages. Photo of a heavy-duty truck and a diesel passenger car.

**Instructor Narration:**
> "Why do diesel engines exist? One word: efficiency. A diesel engine converts about 40-45% of the fuel's energy into useful work. A gasoline engine? About 25-35%. That difference matters when you're hauling 40 tonnes across Europe or when fuel costs are your biggest business expense. Diesel also produces more torque at lower RPM — that low-end pulling power that trucks, buses, SUVs, and agricultural equipment depend on.
>
> But efficiency comes at a cost. Diesel systems are heavier, more complex, more expensive to manufacture, and they produce NOx and particulates that require sophisticated aftertreatment. That's why modern diesel is a masterpiece of precision engineering — and why technicians who understand it are in high demand."

**PPT Content:**
```
WHY DIESEL?

Thermal efficiency:
  Diesel: 40-45%
  Gasoline: 25-35%

Torque characteristics:
  Diesel: High torque at low RPM — ideal for heavy loads
  Gasoline: Higher RPM for peak power — ideal for performance

Where you find diesel:
  Trucks, buses, commercial vehicles, SUVs, agricultural,
  marine, generators, construction equipment

Trade-offs:
  Heavier, more expensive, complex emissions aftertreatment,
  higher fuel system pressures, NOx and particulate challenges
```

---

#### Slide 3: Today's Roadmap
**Visual:** Horizontal timeline showing the four blocks of the day with duration and icons for each section.

**Instructor Narration:**
> "Here's our plan for today. First, we'll spend 40 minutes on the Common Rail system — the high-pressure pump, the rail, the injectors, and the multi-injection strategy that makes modern diesel so refined. Then 30 minutes comparing diesel and gasoline side by side, covering glow plugs, intake manifold design, and variable geometry. Then 20 minutes on EGR — Exhaust Gas Recirculation — one of the most important and most problematic systems on any diesel engine. Finally, 60 minutes of hands-on practical work with real diesel components. Let's begin."

**PPT Content:**
```
TODAY'S PLAN (180 minutes)

BLOCK 1 (40 min): Common Rail Diesel System
  — High-pressure pump, rail, injectors, multi-injection

BLOCK 2 (30 min): Diesel vs Gasoline + Intake Control
  — Compression ignition, glow plugs, swirl flaps, variable geometry

BLOCK 3 (20 min): EGR System
  — Valve, cooler, purpose, carbon buildup, testing

BLOCK 4 (60 min): Hands-On Practical
  — Component ID, injector comparison, EGR inspection, scan tool

+ 15 min wrap-up & Day 14 preview
```

---

### **DEVELOPMENT PART 1: The Common Rail Diesel System** (Slides 4-12, ~40 minutes)

**Narrative Voice:** Technical but awe-inspiring. Emphasise the extreme pressures and precision involved.

---

#### Slide 4: Common Rail System Overview
**Visual:** Complete system diagram showing: fuel tank, low-pressure pump, fuel filter with water separator, high-pressure pump (CP3/CP4), common rail with pressure sensor and pressure regulator, injectors at each cylinder, return lines. Arrows showing fuel flow direction and pressure zones (low pressure in blue, high pressure in red).

**Instructor Narration:**
> "Here's the complete Common Rail diesel fuel system. The concept is elegant: build up enormous pressure in a central reservoir — the rail — and then let the injectors draw from it independently. This decouples pressure generation from injection timing.
>
> Follow the fuel path. It starts in the tank. A low-pressure pump — usually electric, sometimes mechanical — lifts fuel through a filter and water separator to the high-pressure pump. The HP pump compresses the fuel to operating pressure — 1,600 to 2,500 bar depending on the system — and sends it into the common rail. That rail is a thick steel tube shared by all cylinders. A pressure sensor monitors rail pressure constantly, and a pressure control valve regulates it. From the rail, short high-pressure lines feed each injector. The ECU controls exactly when each injector opens, for how long, and how many times per combustion cycle."

**PPT Content:**
```
COMMON RAIL DIESEL SYSTEM — OVERVIEW

Fuel path (follow the arrows):

TANK → Low-pressure pump → Fuel filter/water separator
  → HIGH-PRESSURE PUMP (CP3/CP4)
    → COMMON RAIL (shared reservoir)
      → Injectors (one per cylinder)
        → Combustion chamber

Pressure zones:
  Low-pressure side: 3-10 bar (tank to HP pump)
  High-pressure side: 1,600-2,500 bar (HP pump to injectors)

Key principle: Pressure generation is SEPARATE from injection timing
  — The rail stores pressure
  — The ECU controls when each injector opens
```

---

#### Slide 5: The High-Pressure Pump (CP3/CP4)
**Visual:** Cutaway diagram of a Bosch CP4 pump showing the radial piston arrangement, drive shaft, inlet metering valve, and outlet to rail. Comparison inset showing CP3 (three pistons) vs CP4 (one or two pistons).

**Instructor Narration:**
> "The high-pressure pump is the workhorse of the system. It takes fuel at low pressure and compresses it to 2,000 bar or more. The two most common designs are the Bosch CP3 and CP4. The CP3 has three radial pistons and is known for reliability. The CP4 has one or two pistons and is lighter and more efficient — but it's also more vulnerable to fuel contamination.
>
> The pump is mechanically driven off the engine — usually by a belt, chain, or gear from the camshaft or crankshaft. An inlet metering valve controls how much fuel enters the pump on each stroke. This is how the ECU controls rail pressure — by regulating inlet volume. Less fuel in means less pressure out.
>
> One critical point: these pumps rely on the diesel fuel itself for lubrication. If the fuel is contaminated with water or gasoline — yes, misfuelling happens — the pump can destroy itself in minutes. That's thousands of euros in damage from one tank of wrong fuel."

**PPT Content:**
```
HIGH-PRESSURE PUMP (CP3 / CP4)

Function: Compress fuel from ~5 bar to 1,600-2,500 bar

Bosch CP3:
  — 3 radial pistons, 120 degrees apart
  — Very robust, widely used (2001+)
  — Handles fuel quality variations well

Bosch CP4:
  — 1 or 2 pistons
  — Lighter, more efficient
  — More sensitive to fuel contamination
  — Common in 2008+ vehicles

Drive: Belt, chain, or gear from engine
Lubrication: BY THE DIESEL FUEL ITSELF

Pressure control: Inlet metering valve (ECU-controlled)
  — Controls volume of fuel entering pump per stroke
  — Less fuel in = less pressure in rail

DANGER: Misfuelling (gasoline in diesel) destroys HP pump
  — No lubrication → metal-to-metal contact → catastrophic failure
```

---

#### Slide 6: Fuel Filter & Water Separator
**Visual:** Cross-section of a diesel fuel filter assembly showing the filter element, water separator bowl at the bottom with drain valve, water-in-fuel sensor, and optional fuel heater element.

**Instructor Narration:**
> "Before fuel reaches the high-pressure pump, it must be absolutely clean. Diesel fuel filters are far more critical than gasoline filters because of the extreme pressures and tiny tolerances inside the injectors. Modern diesel injectors have clearances of 1-3 microns — that's smaller than a human red blood cell. Any particle larger than that can score the injector nozzle and cause permanent damage.
>
> The filter also incorporates a water separator. Diesel fuel absorbs moisture from the atmosphere, and water in the fuel system causes corrosion, injector damage, and in extreme cases, ice crystals in cold weather. The water collects in a bowl at the bottom of the filter housing, and a sensor alerts the driver when it needs draining. Some systems include a fuel heater to prevent wax crystallisation in cold weather — diesel starts to gel below about minus 15 degrees Celsius."

**PPT Content:**
```
FUEL FILTER & WATER SEPARATOR

Why so critical in diesel?
  — HP pump and injectors have 1-3 micron clearances
  — Any contamination = expensive damage
  — Filter typically rated at 3-5 microns

Water separator:
  — Diesel absorbs moisture from atmosphere
  — Water collects in bowl at filter base
  — Water-in-fuel sensor triggers dashboard warning
  — Technician drains water bowl during service

Fuel heater (cold climate option):
  — Diesel waxes/gels below approximately -15 degrees C
  — Electric heater element in filter housing
  — Prevents fuel starvation in winter

Service interval: Typically every 30,000-60,000 km
  — ALWAYS replace at recommended intervals
  — Neglected filter = starved pump = expensive failure
```

---

#### Slide 7: The Common Rail
**Visual:** Photo and cross-section of a common rail — showing the thick-walled steel tube, threaded connections for injector feed lines, the rail pressure sensor at one end, and the pressure control valve (or pressure relief valve) at the other end.

**Instructor Narration:**
> "The common rail itself is a beautifully simple concept. It's a thick-walled steel tube — essentially an accumulator — that stores fuel at enormous pressure. Because it's shared by all injectors, the pressure is always available instantly when any injector needs to fire. This is the key advantage over older diesel systems where the pump directly drove each injection event.
>
> At one end you'll find the rail pressure sensor. This sends a real-time pressure signal to the ECU — it's one of the most critical sensor signals in the entire engine management system. At the other end, or sometimes on the pump, there's a pressure control valve or pressure relief valve. If pressure exceeds the target, this valve dumps excess fuel back to the tank.
>
> The rail must withstand extraordinary stress — pressure pulses at every injection event, thermal cycling, vibration. That's why it's forged from high-grade steel and tested to pressures well above operating maximum."

**PPT Content:**
```
THE COMMON RAIL — High-Pressure Accumulator

Construction:
  — Thick-walled forged steel tube
  — Threaded connections for each injector feed line
  — Designed to withstand 2,500+ bar with pulsating loads

Key components ON the rail:

1. RAIL PRESSURE SENSOR
   — Measures actual rail pressure in real time
   — Signal to ECU (0-5V or ratiometric)
   — ECU uses this for closed-loop pressure control
   — Failure = limp mode or no start

2. PRESSURE CONTROL VALVE / REGULATOR
   — Controls rail pressure by bleeding excess fuel to return
   — ECU-controlled (PWM solenoid)
   — Works WITH inlet metering valve for pressure regulation

3. PRESSURE RELIEF VALVE (safety)
   — Mechanical spring valve
   — Opens if pressure exceeds safe maximum
   — Protects rail and injectors from over-pressure

Rail pressure range: 250 bar (idle) to 2,500 bar (full load)
```

---

#### Slide 8: Fuel Temperature Sensor
**Visual:** Diagram showing the fuel temperature sensor location — typically on the fuel rail or on the low-pressure fuel line near the filter. Callout showing sensor connector and typical resistance-temperature curve.

**Instructor Narration:**
> "Diesel fuel changes density with temperature. Hot fuel is less dense — there's less energy per cubic centimetre. Cold fuel is more dense. The ECU needs to know fuel temperature to calculate the correct injection quantity. If it injects the same volume of hot fuel as cold fuel, the engine produces less power with the hot fuel because there's less energy in each shot.
>
> The fuel temperature sensor is usually an NTC thermistor — same type you saw with coolant temperature sensors. It's mounted on the fuel rail or on the low-pressure line near the filter. Typical operating range is minus 40 to plus 120 degrees Celsius. The ECU uses this signal to compensate injection quantity and protect the system — excessively hot fuel can damage injectors and cause vapour lock."

**PPT Content:**
```
FUEL TEMPERATURE SENSOR

Purpose: Measure fuel temperature for injection quantity correction

Why it matters:
  — Diesel density changes with temperature
  — Hot fuel = less dense = less energy per volume
  — ECU adjusts injection quantity to compensate
  — Also protects system from overheating damage

Sensor type: NTC thermistor (resistance decreases as temp rises)
Location: Fuel rail or low-pressure line near filter
Range: -40 to +120 degrees C
Signal: Resistance to ECU (voltage divider circuit)

Failure symptoms:
  — Black smoke (over-fuelling if ECU assumes cold fuel)
  — Loss of power (under-fuelling if ECU assumes hot fuel)
  — Possible DTC: P0180-P0183 (fuel temp sensor circuit)
```

---

#### Slide 9: Diesel Injectors — Solenoid Type
**Visual:** Cutaway of a solenoid diesel injector showing the solenoid coil, armature, control chamber, nozzle needle, and spray holes. Arrows showing fuel flow through the control chamber circuit.

**Instructor Narration:**
> "Now we reach the injector — the component that actually delivers fuel into the combustion chamber. Diesel injectors are marvels of precision. They have to open and close in less than a millisecond, spray fuel at pressures exceeding 2,000 bar, and do this up to five times per combustion cycle, thousands of times per minute.
>
> The solenoid injector uses an electromagnetic coil to lift an armature that controls a pilot valve. This pilot valve doesn't directly lift the nozzle needle — the pressures are too enormous for that. Instead, it controls pressure in a small control chamber above the needle. When the solenoid energises, the pilot valve opens, pressure drops in the control chamber, and the differential pressure across the needle lifts it off its seat. Fuel sprays through tiny holes — typically 6 to 8 holes, each about 150 microns in diameter. When the solenoid de-energises, the control chamber refills with pressure, and the needle slams shut."

**PPT Content:**
```
DIESEL INJECTORS — SOLENOID TYPE

Operating principle:
  1. ECU energises solenoid coil
  2. Armature lifts, opens pilot valve
  3. Pressure drops in control chamber above needle
  4. Differential pressure lifts nozzle needle
  5. Fuel sprays through nozzle holes (6-8 holes, ~150 microns each)
  6. ECU de-energises solenoid
  7. Control chamber refills, needle closes

Key specifications:
  — Opening time: < 1 millisecond
  — Spray pressure: up to 2,500 bar at nozzle tip
  — Nozzle hole diameter: ~150 microns (0.15 mm)
  — Needle lift: ~0.3 mm
  — Internal clearances: 1-3 microns

Advantages:
  — Proven technology, reliable, cost-effective
  — Good for up to ~2,000 bar systems

Limitations:
  — Slower response than piezo
  — Less precise at very small injection quantities
```

---

#### Slide 10: Diesel Injectors — Piezo Type
**Visual:** Cutaway of a piezoelectric diesel injector showing the piezo stack, coupler module, servo valve, and nozzle. Side-by-side comparison with solenoid injector highlighting the differences.

**Instructor Narration:**
> "The piezo injector takes precision to the next level. Instead of a solenoid coil and armature, it uses a stack of piezoelectric crystals. When voltage is applied, these crystals physically expand — by about 40 microns. That expansion actuates a servo valve that controls the nozzle needle, just like the solenoid version.
>
> Why go to this trouble? Speed. A piezo injector can open and close up to five times faster than a solenoid injector. This means it can inject smaller quantities more precisely, enabling more injection events per combustion cycle. The result? Quieter combustion, lower emissions, and better fuel economy. You'll find piezo injectors on premium diesel engines — BMW, Mercedes, Audi, and some Volkswagen applications.
>
> The downside? They're more expensive, more sensitive to electrical issues, and when they fail, replacement costs are significantly higher."

**PPT Content:**
```
DIESEL INJECTORS — PIEZO TYPE

Operating principle:
  1. ECU applies voltage (100-200V) to piezo crystal stack
  2. Crystals expand (~40 microns)
  3. Expansion actuates servo/coupler valve
  4. Nozzle needle lifts, fuel sprays
  5. Voltage removed, crystals contract, needle closes

Advantages over solenoid:
  — Up to 5x faster response time
  — More precise small-quantity injection
  — Enables up to 7-9 injection events per cycle
  — Quieter combustion (smoother pressure rise)
  — Better emissions control

Disadvantages:
  — More expensive (injector cost and replacement)
  — Sensitive to electrical issues
  — Requires higher-voltage driver circuits
  — More complex diagnostics

Where found:
  BMW, Mercedes-Benz, Audi, some VW applications
  Generally on premium/performance diesel engines
```

---

#### Slide 11: Multi-Injection Strategy
**Visual:** Graph showing injection events over crankshaft angle for one combustion cycle. Multiple injection pulses labeled: Pilot 1, Pilot 2, Main, After, Post. Below, a cylinder pressure vs crank angle curve showing how each injection affects combustion pressure.

**Instructor Narration:**
> "This is where diesel gets truly sophisticated. In an old diesel engine, there was one injection event — one big shot of fuel, one violent combustion event. The result? That characteristic diesel knock, high combustion noise, and a harsh pressure spike.
>
> Modern Common Rail systems inject fuel multiple times per combustion cycle. First, one or two pilot injections — tiny shots of fuel that pre-heat the combustion chamber and create initial flame kernels. This softens the pressure rise of the main injection, dramatically reducing combustion noise. That's why modern diesels are so much quieter than old ones.
>
> Then comes the main injection — the big event that produces the power. After that, you might get an after-injection that helps burn remaining soot in the cylinder. And finally, a late post-injection that injects raw fuel into the exhaust stream to heat the DPF for regeneration. We're talking about up to five or seven separate injection events in the time it takes to blink — all at 2,000 bar. The ECU orchestrates this ballet thousands of times per minute."

**PPT Content:**
```
MULTI-INJECTION STRATEGY

Injection events per combustion cycle (up to 5-7):

1. PILOT INJECTION(S) — 1 or 2 small pre-injections
   Purpose: Pre-heat combustion chamber, soften pressure rise
   Result: DRAMATICALLY reduces diesel knock/noise
   Quantity: 1-3 mm cubed per injection

2. MAIN INJECTION — the power-producing event
   Purpose: Deliver primary fuel charge for combustion
   Quantity: Varies with load demand
   Timing: Typically around TDC

3. AFTER INJECTION — shortly after main
   Purpose: Burn remaining soot, reduce particulates
   Helps with emissions compliance

4. POST INJECTION — late in exhaust stroke
   Purpose: Inject raw fuel into exhaust stream
   Heats DPF (Diesel Particulate Filter) for regeneration
   Fuel does NOT combust in cylinder

Old diesel: 1 injection = BANG = noise + smoke
Modern diesel: 5-7 injections = smooth + quiet + clean
```

---

#### Slide 12: Rail Pressure Control — Closed-Loop System
**Visual:** Control loop diagram showing: ECU target pressure, inlet metering valve on pump, rail pressure sensor feedback, pressure control valve on rail. Arrows showing the feedback loop. Graph showing rail pressure response to load changes.

**Instructor Narration:**
> "Controlling rail pressure is a closed-loop operation. The ECU has a target pressure map based on engine speed, load, and temperature. It reads the actual pressure from the rail pressure sensor and adjusts two actuators to match.
>
> The inlet metering valve on the high-pressure pump controls how much fuel enters the pump — this is the primary control. The pressure control valve on the rail bleeds excess fuel back to the tank — this is the fine-tuning control. Together, they maintain rail pressure within a few bar of the target, even during rapid load changes.
>
> If the rail pressure sensor fails, the ECU loses its feedback signal. Most systems will enter a limp mode with a fixed default pressure. If the inlet metering valve sticks, pressure can be too high or too low. Too high and the pressure relief valve opens as a safety measure. Too low and you get loss of power, rough running, or no start."

**PPT Content:**
```
RAIL PRESSURE CONTROL — CLOSED-LOOP

         ┌──────────────────────────────────┐
         │        ECU Target Pressure        │
         │ (from maps: speed + load + temp)  │
         └────────────┬─────────────────────┘
                      │
         ┌────────────v─────────────────────┐
         │  Inlet Metering Valve (on pump)  │ ← Primary control
         │  Controls fuel volume INTO pump  │
         └────────────┬─────────────────────┘
                      │
         ┌────────────v─────────────────────┐
         │     Common Rail (accumulator)     │
         └────────────┬─────────────────────┘
                      │
         ┌────────────v─────────────────────┐
         │   Rail Pressure Sensor (feedback) │ → Back to ECU
         └──────────────────────────────────┘

Secondary control: Pressure control valve on rail
  — Bleeds excess fuel to return line

Typical operating range:
  Idle: 250-400 bar
  Part load: 800-1,200 bar
  Full load: 1,600-2,500 bar
```

---

### **DEVELOPMENT PART 2: Diesel vs Gasoline + Intake Control** (Slides 13-18, ~30 minutes)

**Narrative Voice:** Comparative. Constantly reference what they learned yesterday to build context.

---

#### Slide 13: The Big Comparison — Diesel vs Gasoline
**Visual:** Large two-column comparison table with icons for each characteristic. Green highlights for diesel advantages, blue for gasoline advantages.

**Instructor Narration:**
> "Let's put it all side by side. Yesterday's engine versus today's engine. The fundamental difference: gasoline uses a spark plug to ignite a pre-mixed charge. Diesel uses compression heat to ignite fuel sprayed directly into the cylinder. Everything else flows from that single difference.
>
> Compression ratio: gasoline engines run 9 to 12 to 1. Diesel needs 16 to 22 to 1 — nearly double — to generate enough heat for auto-ignition. That means diesel engines need stronger blocks, heads, pistons, and connecting rods. They're heavier and more expensive.
>
> Fuel pressure: gasoline direct injection runs up to 200 bar. Common Rail diesel? Up to 2,500 bar — more than ten times higher. That means heavier-duty pumps, lines, and injectors.
>
> Ignition: gasoline has coils and spark plugs. Diesel has glow plugs — only for cold starting, not for ignition during running."

**PPT Content:**
```
DIESEL vs GASOLINE — THE BIG COMPARISON

                        GASOLINE           DIESEL
Ignition method:        Spark plug         Compression heat
Compression ratio:      9:1 to 12:1        16:1 to 22:1
Fuel pressure (DI):     50-200 bar         1,600-2,500 bar
Injection events:       1 per cycle         Up to 5-7 per cycle
Cold start aid:         None needed         Glow plugs
Throttle body:          Yes (controls air)  Usually no (excess air)
Air-fuel ratio:         Stoichiometric      Lean (excess air always)
                        (14.7:1)            (18:1 to 70:1)
Peak torque:            Higher RPM          Lower RPM
Thermal efficiency:     25-35%              40-45%
Exhaust aftertreatment: TWC catalyst        DOC + DPF + SCR
Engine weight:          Lighter             Heavier
Fuel cost (per litre):  Higher              Lower (most markets)
```

---

#### Slide 14: Compression Ignition Explained
**Visual:** Four-stroke diesel cycle animation stills — (1) intake stroke showing air only entering, (2) compression stroke with temperature gauge showing 600-900 degrees C, (3) injection near TDC with fuel igniting on contact, (4) power stroke. Temperature and pressure callouts at each stage.

**Instructor Narration:**
> "Let's understand compression ignition at a fundamental level. In a gasoline engine, air and fuel are mixed together before or during compression, and a spark ignites the mixture at the right moment. In a diesel engine, only air is drawn into the cylinder on the intake stroke. No fuel yet.
>
> On the compression stroke, that air is squeezed to one-sixteenth or less of its original volume. Compressing air heats it — that's basic physics. At a compression ratio of 20 to 1, the air temperature reaches 600 to 900 degrees Celsius. That's hot enough to melt aluminium.
>
> Then, near top dead centre, the injector sprays finely atomised diesel fuel into this superheated air. The fuel ignites instantly on contact — no spark needed. The combustion drives the piston down for the power stroke. This is why diesel engines are so efficient — the high compression ratio extracts more energy from each combustion event."

**PPT Content:**
```
COMPRESSION IGNITION — HOW DIESEL WORKS

Stroke 1 — INTAKE:
  Only AIR enters the cylinder (no fuel, no throttle restriction)

Stroke 2 — COMPRESSION:
  Air compressed to 16:1-22:1 ratio
  Temperature rises to 600-900 degrees C
  Pressure reaches 30-55 bar

Stroke 3 — INJECTION + COMBUSTION (POWER):
  Fuel injected at 1,600-2,500 bar near TDC
  Fuel auto-ignites on contact with superheated air
  Combustion pressure reaches 150-200 bar
  Piston driven downward

Stroke 4 — EXHAUST:
  Burned gases expelled

Key physics: Compressing gas increases its temperature
  PV = nRT (ideal gas law)
  Halving volume roughly doubles absolute temperature
```

---

#### Slide 15: Glow Plugs — Cold Start Aid
**Visual:** Cross-section of a glow plug showing the heating element, control module connection, and installation in the cylinder head pre-chamber or swirl chamber. Photo of a glow plug glowing orange-hot. Dashboard glow plug warning light symbol.

**Instructor Narration:**
> "If compression ignition works by heating air, what happens when the engine is cold? The cylinder walls, the piston, and the head are all cold. They absorb heat from the compressed air, and the temperature may not reach the auto-ignition point of diesel fuel — about 250 degrees Celsius. This is where glow plugs come in.
>
> A glow plug is an electrically heated rod that protrudes into the combustion chamber. Before you start a cold diesel engine, the glow plug control module energises the plugs for a few seconds. They heat up to 1,000 degrees Celsius or more at the tip, creating a hot spot in the combustion chamber. This ensures reliable ignition during cranking and the first few seconds of running.
>
> Once the engine is warm, glow plugs are no longer needed — the compression heat alone sustains combustion. Modern glow plugs reach operating temperature in 2-3 seconds. Older ones took 10-20 seconds — that's why older diesels had a long wait before cranking."

**PPT Content:**
```
GLOW PLUGS — DIESEL COLD START AID

Purpose: Pre-heat combustion chamber for reliable cold starting

How they work:
  — Electrically heated ceramic or metal rod
  — Tip reaches 1,000+ degrees C in 2-3 seconds (modern)
  — Creates hot spot in combustion chamber
  — Ensures fuel ignites during cranking

When they operate:
  — Pre-glow: Before cranking (2-5 seconds, dashboard light)
  — During cranking: Stays energised
  — Post-glow: Stays on 1-3 minutes after start (smooth idle)
  — NOT used during normal warm running

Glow plug control module:
  — Controls timing and duration of heating
  — Monitors glow plug resistance for diagnostics
  — Reports faults to ECU (DTC: P0380-P0384)

vs Spark plugs (gasoline):
  Spark plugs fire every combustion cycle, forever
  Glow plugs only used for cold start, then switch off
```

---

#### Slide 16: Diesel Intake Manifold & Variable Geometry
**Visual:** Cutaway of a diesel intake manifold showing swirl flap mechanism. Separate diagrams showing variable intake runner length with short and long runner configurations. Airflow visualisation showing tumble and swirl patterns in the cylinder.

**Instructor Narration:**
> "Diesel engines breathe differently from gasoline engines. Most diesel engines don't have a traditional throttle body — they always run with excess air. The load is controlled by varying fuel quantity, not air quantity. So the intake manifold design focuses on optimising airflow patterns rather than restricting volume.
>
> Two key technologies here. First, swirl flaps — small butterfly valves inside the intake ports that create a swirling motion of the incoming air. This swirl mixes the injected fuel more thoroughly with the air, improving combustion efficiency and reducing emissions. At high RPM and full load, the swirl flaps open fully for maximum airflow. At low RPM and part load, they partially close to increase swirl velocity.
>
> Second, some diesel engines use variable intake runner length — similar to gasoline engines. Short runners for high-RPM breathing, long runners for low-RPM torque. The ECU controls these based on operating conditions."

**PPT Content:**
```
DIESEL INTAKE MANIFOLD & VARIABLE GEOMETRY

Key difference from gasoline:
  — Most diesels have NO throttle body (or a very small one)
  — Load controlled by FUEL QUANTITY, not air quantity
  — Engine always breathes excess air
  — Small throttle may exist for EGR control or smooth shutdown

SWIRL FLAPS:
  — Small butterfly valves in intake ports
  — Create swirling air motion in cylinder
  — Improves fuel-air mixing at low RPM/load
  — Open fully at high RPM for maximum airflow
  — Controlled by vacuum actuator or electric servo
  — Common failure: shaft breaks, flap falls into cylinder!

VARIABLE INTAKE RUNNER LENGTH:
  — Short runners: Better filling at high RPM
  — Long runners: Better torque at low RPM
  — ECU switches via vacuum or electric actuator

TUMBLE vs SWIRL:
  — Swirl: rotation around cylinder axis (horizontal spin)
  — Tumble: rotation perpendicular to axis (barrel roll)
```

---

#### Slide 17: Swirl Flap Actuators & Intake Control Strategies
**Visual:** Detailed photos and diagrams of swirl flap actuator types — vacuum-operated diaphragm actuator and electric servo motor actuator. Linkage mechanism connecting actuator to flap shaft. Photo showing a failed swirl flap with broken shaft.

**Instructor Narration:**
> "Swirl flap actuators come in two main types. Vacuum-operated actuators use engine vacuum or a vacuum pump to move a diaphragm that rotates the flap shaft via a linkage. Electric actuators use a small DC servo motor with position feedback. The electric type is more precise and faster-responding.
>
> The ECU determines the optimal swirl flap position based on engine speed, load, air mass, and EGR rate. At idle and low load, the flaps are partially closed to create maximum swirl — this helps with combustion quality and emissions. As load increases, the flaps open progressively. At full load and high RPM, they're fully open to minimise intake restriction.
>
> Now, the cautionary tale: swirl flap failures. The flap shafts or the flaps themselves can crack and break, especially on higher-mileage engines. If a broken piece falls into the cylinder, it can cause catastrophic engine damage — scored cylinder walls, damaged pistons, bent valves. Some technicians remove swirl flaps entirely as a preventive measure, though this can affect emissions compliance."

**PPT Content:**
```
SWIRL FLAP ACTUATORS & CONTROL STRATEGIES

Vacuum-operated actuator:
  — Diaphragm + linkage mechanism
  — Controlled by ECU via vacuum solenoid
  — Simpler, less precise

Electric servo actuator:
  — DC motor with position feedback
  — Direct control by ECU (PWM signal)
  — More precise, faster response

ECU control strategy:
  Idle/low load: Flaps partially closed → maximum swirl
  Part load: Flaps intermediate → balanced swirl + flow
  Full load/high RPM: Flaps fully open → maximum airflow

COMMON FAILURE MODE:
  — Flap shaft or flap body cracks/breaks
  — Broken piece falls into combustion chamber
  — CATASTROPHIC ENGINE DAMAGE (scored bore, bent valves)
  — Symptoms: rattling noise, loss of power, engine warning light
  — Some workshops remove flaps preventively (emissions trade-off)

Diagnostic: Check flap movement with scan tool actuator test
```

---

#### Slide 18: Diesel Air Supply — Complete Picture
**Visual:** Complete intake system diagram from air filter through turbocharger (reference only), intercooler, intake manifold with swirl flaps, to cylinder head ports. EGR valve connection point shown with dashed line (preview for next section).

**Instructor Narration:**
> "Let's see the complete diesel air supply system. Air enters through the air filter — same as gasoline. On turbocharged diesels — and almost all modern diesels are turbocharged — the air is compressed by the turbo, then cooled by an intercooler to increase its density. The cooled, compressed air enters the intake manifold where swirl flaps direct its flow pattern. From there, it enters the combustion chamber through the intake valves.
>
> Notice one more connection here — marked with a dashed line. This is where the EGR system feeds exhaust gas back into the intake. We'll cover that in detail in our next section. The intake manifold is where fresh air and recirculated exhaust gas mix before entering the cylinders."

**PPT Content:**
```
DIESEL AIR SUPPLY — COMPLETE PICTURE

Air path:
  AIR FILTER → Mass air flow sensor
    → TURBOCHARGER (compressor side)
      → INTERCOOLER (charge air cooler)
        → INTAKE MANIFOLD (with swirl flaps)
          → EGR mixing point (exhaust gas added here)
            → INTAKE PORTS → COMBUSTION CHAMBER

Key sensors in the air path:
  — Mass air flow sensor (MAF): measures incoming air mass
  — Intake air temperature sensor: measures charge air temp
  — Boost pressure sensor: measures pressure after turbo
  — MAP sensor: measures intake manifold pressure

Almost all modern diesels are turbocharged:
  — Increases air density → more fuel can be burned → more power
  — Essential for meeting emissions standards
  — We will cover turbo systems in detail on Day 15
```

---

### **DEVELOPMENT PART 3: EGR System** (Slides 19-22, ~20 minutes)

**Narrative Voice:** Problem-solving focus. EGR is both essential and problematic — technicians must understand both sides.

---

#### Slide 19: EGR — Why Recirculate Exhaust Gas?
**Visual:** Combustion temperature graph showing NOx formation increasing sharply above 1,500 degrees C. Two combustion diagrams: one without EGR (high peak temperature, high NOx) and one with EGR (lower peak temperature, lower NOx). Simple formula: Higher temperature = More NOx.

**Instructor Narration:**
> "EGR stands for Exhaust Gas Recirculation. And the first question every learner asks is: why on earth would you put exhaust gas back into the engine? It seems counterintuitive. The answer is chemistry.
>
> NOx — nitrogen oxides — are formed when combustion temperatures exceed about 1,500 degrees Celsius. The hotter the combustion, the more NOx produced. NOx is a harmful pollutant that contributes to smog and acid rain. Diesel engines run very hot because of their high compression ratios, so they naturally produce a lot of NOx.
>
> EGR introduces a controlled amount of inert exhaust gas — mostly CO2 and water vapour — into the intake charge. These inert gases absorb heat during combustion, acting as a thermal buffer. The result is lower peak combustion temperatures — and dramatically less NOx. A well-functioning EGR system can reduce NOx by 50% or more. It's one of the primary emissions control strategies on every diesel engine."

**PPT Content:**
```
EGR — EXHAUST GAS RECIRCULATION

The problem: NOx formation
  — Nitrogen + Oxygen → NOx at temperatures above ~1,500 degrees C
  — Diesel combustion: very high temperatures → lots of NOx
  — NOx is a regulated pollutant (smog, acid rain, health effects)

The solution: Cool the combustion
  — Recirculate 10-30% exhaust gas back into intake
  — Exhaust gas is INERT (CO2 + H2O + N2)
  — Inert gas absorbs combustion heat without contributing energy
  — Peak combustion temperature drops 200-300 degrees C
  — NOx reduction: 50% or more

The trade-off:
  — Less NOx BUT potentially more soot/particulates
  — ECU must balance NOx reduction vs soot production
  — EGR rate varies with engine speed, load, and temperature
  — Too much EGR = rough running, smoke, power loss
  — Too little EGR = excessive NOx, emissions failure
```

---

#### Slide 20: EGR Valve Construction — Vacuum & Electric
**Visual:** Side-by-side cutaway diagrams of (1) vacuum-operated EGR valve with diaphragm, spring, pintle valve, and vacuum hose connection, and (2) electric EGR valve with DC motor, gear reduction, position sensor, and poppet valve. Both showing the gas flow path from exhaust manifold to intake manifold.

**Instructor Narration:**
> "The EGR valve is the gatekeeper — it controls how much exhaust gas flows from the exhaust manifold back into the intake. Two main types.
>
> The vacuum-operated EGR valve uses engine vacuum or an external vacuum pump acting on a diaphragm. A vacuum solenoid, controlled by the ECU, modulates the vacuum signal. More vacuum means more valve opening. It's simple but less precise.
>
> The electric EGR valve — which is now standard on most modern diesels — uses a DC motor driving the valve through a gear mechanism. A built-in position sensor tells the ECU exactly where the valve is. This allows much more precise control of EGR flow. The ECU can command any position from fully closed to fully open, and the position sensor confirms the valve actually moved where it was told.
>
> Both types live in a hostile environment — sitting right between the exhaust and intake, exposed to hot, soot-laden exhaust gases. This is why EGR valves are one of the most common failure points on diesel engines."

**PPT Content:**
```
EGR VALVE — TWO TYPES

VACUUM-OPERATED:
  — Diaphragm actuated by vacuum
  — Vacuum solenoid controlled by ECU (duty cycle)
  — Spring holds valve closed when no vacuum
  — Less precise, slower response
  — Found on older diesel engines (pre-2008)

ELECTRIC (MODERN):
  — DC motor with gear reduction
  — Built-in position sensor (potentiometer or Hall)
  — ECU commands position directly (PWM)
  — Very precise flow control
  — Faster response for transient conditions
  — Standard on most 2008+ diesel engines

Both types:
  — Located between exhaust manifold and intake manifold
  — Exposed to extreme heat and soot
  — Subject to carbon buildup and sticking
  — Typical flow path diameter: 20-35 mm
```

---

#### Slide 21: EGR Cooler & System Layout
**Visual:** Complete EGR system diagram showing exhaust manifold, EGR cooler (with coolant connections), EGR valve, intake manifold connection point. Callout showing the cooler as a small heat exchanger with coolant flowing through it. Temperature values at each stage.

**Instructor Narration:**
> "Hot exhaust gas — 600 degrees Celsius or more — flowing directly into the intake would heat the charge air too much, reducing air density and the effectiveness of the EGR. That's why modern systems include an EGR cooler. It's a small heat exchanger, similar in concept to a radiator, that uses engine coolant to cool the exhaust gas before it enters the intake.
>
> The cooler reduces exhaust gas temperature from 600-plus degrees down to 100-150 degrees. This cooled, dense exhaust gas is more effective at absorbing combustion heat — the whole point of EGR. Some systems also include an EGR cooler bypass valve that routes exhaust gas around the cooler during cold starts, when you actually want the hot gas to warm the engine faster.
>
> The EGR cooler is another failure point. Internal leaks can allow coolant to enter the exhaust system — or exhaust gas to pressurise the cooling system. If coolant level drops with no visible external leak, a cracked EGR cooler is a prime suspect."

**PPT Content:**
```
EGR COOLER & COMPLETE SYSTEM LAYOUT

System flow:
  EXHAUST MANIFOLD
    → EGR COOLER (reduces gas temp from 600+ to 100-150 degrees C)
      → EGR VALVE (controls flow volume)
        → INTAKE MANIFOLD (mixes with fresh air)

EGR Cooler:
  — Small heat exchanger (exhaust gas inside, coolant outside)
  — Reduces gas temperature by ~400-500 degrees C
  — Cooler gas = denser = more effective NOx reduction
  — Connected to engine cooling circuit

EGR Cooler Bypass (some systems):
  — Valve routes gas AROUND cooler during cold start
  — Hot EGR helps engine warm up faster
  — ECU switches to cooled EGR once engine is warm

Common EGR cooler failures:
  — Internal crack: coolant leaks into exhaust or vice versa
  — Symptoms: coolant loss without visible leak, white exhaust smoke
  — Can pressurise cooling system (blown expansion tank cap)
  — Soot accumulation reduces cooler efficiency over time
```

---

#### Slide 22: EGR Carbon Buildup — The Technician's Enemy
**Visual:** Three photos showing: (1) a clean EGR valve, (2) a moderately carbon-fouled EGR valve, (3) a heavily coked EGR valve that is nearly blocked solid. Additional photo showing carbon buildup in the intake manifold runners. Before-and-after cleaning comparison.

**Instructor Narration:**
> "This is the reality of EGR. Look at these three photos. On the left, a new EGR valve — clean, smooth, the valve moves freely. In the middle, one with moderate carbon buildup after 50,000 kilometres. On the right, one that's nearly blocked solid after 150,000 kilometres of short-trip city driving. The exhaust gas carries soot particles, and when those mix with oil vapour from the crankcase ventilation system in the intake manifold, they form a thick, tar-like carbon deposit.
>
> This carbon restricts the valve movement, reduces flow, and eventually blocks it entirely. The intake manifold runners themselves also get coated. Symptoms include loss of power, increased smoke, rough idle, and EGR-related DTCs. The EGR valve may stick open — causing rough running and excessive smoke — or stick closed — causing high NOx and emissions failure.
>
> Testing the EGR system involves using a scan tool to command the valve open and closed while monitoring engine response. A properly functioning EGR valve should cause a noticeable drop in idle RPM and a rougher idle when opened at idle — because you're replacing some of the combustible air with inert gas."

**PPT Content:**
```
EGR CARBON BUILDUP — THE TECHNICIAN'S ENEMY

Why it happens:
  — Exhaust soot + oil vapour (from PCV) = sticky carbon deposits
  — Deposits build up on valve, ports, and intake manifold
  — Worse with: short trips, city driving, low RPM operation

Progression:
  Clean → Light coating (30-50k km) → Heavy deposits (100k+ km) → Blocked

Symptoms of fouled EGR:
  — Loss of power (restricted airflow)
  — Increased smoke (incomplete combustion)
  — Rough idle (valve stuck partially open)
  — Engine warning light / EGR DTCs
  — Failed emissions test (high NOx if stuck closed)

Testing with scan tool:
  1. At idle, command EGR valve OPEN
  2. Engine should run rough / RPM should drop
  3. If no change → valve stuck closed or passage blocked
  4. Command EGR valve CLOSED
  5. If engine smooths out → valve was functioning

Common DTCs:
  P0401: EGR flow insufficient
  P0402: EGR flow excessive
  P0403: EGR control circuit
  P0404: EGR range/performance
```

---

### **PRACTICAL: Hands-On Diesel Component Work** (Slides 23-26, ~60 minutes)

**Narrative Voice:** Workshop guide. Structured practical activities with clear objectives.

---

#### Slide 23: Practical Activity 1 — Common Rail Component Identification
**Visual:** Annotated photo of a diesel engine bay with numbered callouts (unlabeled). Corresponding numbered list for learners to fill in. Timer showing 15 minutes.

**Instructor Narration:**
> "Time for hands-on work. We have a diesel engine — either in a vehicle or on a stand. Your first task: identify every Common Rail fuel system component you can see. I'll give each pair a worksheet with numbered callouts on a photo of this engine. You have 15 minutes to find and label: the high-pressure pump, the common rail, the rail pressure sensor, the pressure regulator, the injectors, the fuel filter, and the fuel return lines. Work in pairs. Compare notes when you're done."

**PPT Content:**
```
PRACTICAL 1: COMMON RAIL COMPONENT IDENTIFICATION
Time: 15 minutes | Work in pairs

Find and label on your worksheet:
  1. High-pressure pump (CP3 or CP4)
  2. Common rail
  3. Rail pressure sensor
  4. Pressure control valve / regulator
  5. Diesel injectors (count them!)
  6. High-pressure fuel lines (pump to rail, rail to injectors)
  7. Fuel filter / water separator
  8. Low-pressure fuel lines (supply and return)
  9. Fuel temperature sensor (if visible)
  10. Glow plugs (look at cylinder head)

BONUS: Identify the EGR valve and cooler

Tips:
  — Follow the fuel lines from the filter forward
  — The rail is the thick steel tube with multiple connections
  — HP lines are thick steel, LP lines are rubber or plastic
```

---

#### Slide 24: Practical Activity 2 — Injector Comparison
**Visual:** Side-by-side photos of a solenoid diesel injector and a piezo diesel injector, with key visual differences highlighted. Dimensional comparison and connector differences.

**Instructor Narration:**
> "For this activity, I have two sets of diesel injectors on the bench — solenoid and piezo types. Your task: examine both types and identify the physical differences. Look at the electrical connector — solenoid injectors typically have a two-pin connector, while piezo injectors often have a different connector type. Look at the body shape — piezo injectors tend to be slimmer. Measure the overall length with a ruler if you can.
>
> Fill in the comparison sheet I'm handing out. This isn't about memorising numbers — it's about being able to tell the difference when you see these in the real world. If you replace a piezo injector with a solenoid one, or vice versa, the engine won't run correctly."

**PPT Content:**
```
PRACTICAL 2: INJECTOR COMPARISON — SOLENOID vs PIEZO
Time: 10 minutes | Bench activity

Examine both injector types and complete the comparison:

                    SOLENOID           PIEZO
Connector type:     ___________        ___________
Number of pins:     ___________        ___________
Body diameter:      ___________        ___________
Overall length:     ___________        ___________
Weight:             ___________        ___________
Nozzle tip shape:   ___________        ___________
Manufacturer mark:  ___________        ___________

Questions to answer:
  1. Which injector feels heavier?
  2. Can you see the spray holes at the nozzle tip?
  3. Could you accidentally swap these two types?
  4. What would happen if you installed the wrong type?
```

---

#### Slide 25: Practical Activity 3 — EGR Valve Inspection
**Visual:** Step-by-step photo guide showing: (1) locating the EGR valve on the engine, (2) inspecting external condition, (3) checking electrical connector, (4) checking vacuum lines (if applicable), (5) removing valve (if permitted) and inspecting for carbon buildup. Photo of a carbon-caked valve pintle.

**Instructor Narration:**
> "Now for the most satisfying — or disgusting — part of today's practical. We're going to inspect an EGR valve. If the valve has been removed, you can handle it and look inside. If it's on the engine, we'll inspect what we can externally.
>
> Look at the valve bore and the pintle face. How much carbon do you see? Can you move the pintle by hand? On an electric valve, it should move smoothly through its full range. On a vacuum valve, with vacuum applied, the diaphragm should pull the pintle open.
>
> If you have a removed valve, try cleaning a small area with carburettor cleaner and a nylon brush. See how much carbon comes off. This gives you an appreciation for what the valve deals with every day. Document what you find — take photos if you can."

**PPT Content:**
```
PRACTICAL 3: EGR VALVE INSPECTION
Time: 15 minutes | Guided inspection

Steps:
  1. LOCATE the EGR valve on the diesel engine
     — Between exhaust and intake manifold
     — Follow the EGR pipe from exhaust side

  2. INSPECT external condition
     — Cracks, corrosion, loose connections?
     — Check electrical connector (corrosion, damage)
     — Check vacuum lines if applicable (cracks, leaks)

  3. INSPECT valve bore (if valve removed)
     — How much carbon buildup?
     — Can the pintle/valve move freely?
     — Rate the buildup: Light / Moderate / Heavy / Blocked

  4. TEST movement
     — Electric: Use scan tool actuator test
     — Vacuum: Apply vacuum with hand pump
     — Valve should move smoothly through full range

  5. DOCUMENT findings
     — Record carbon level, movement quality, any damage
     — Would you recommend cleaning or replacement?
```

---

#### Slide 26: Practical Activity 4 — Diesel DTC Reading with Scan Tool
**Visual:** Photo of a scan tool connected to a diesel vehicle's OBD-II port. Screen showing diesel-specific DTCs: P0087 (fuel rail pressure too low), P0401 (EGR insufficient flow), P0380 (glow plug circuit). Step-by-step connection guide.

**Instructor Narration:**
> "Final practical activity. Connect a scan tool to our diesel vehicle and read the DTCs. I've set up a vehicle with some faults — some real, some simulated. Your job is to connect the tool, navigate to the engine control module, read the fault codes, and interpret what each one means.
>
> Pay attention to the diesel-specific codes. P0087 relates to fuel rail pressure — too low. What could cause that? A failing high-pressure pump, a blocked filter, a leaking pressure regulator. P0401 is EGR insufficient flow — what could cause that? A stuck-closed EGR valve, blocked passage, faulty position sensor. P0380 is a glow plug circuit fault — one or more glow plugs or the control module has a problem.
>
> For each DTC, write down: the code number, the description, what system it relates to, and three possible causes. This is the diagnostic thinking we're building from Day 1."

**PPT Content:**
```
PRACTICAL 4: DIESEL DTC READING
Time: 20 minutes | Scan tool activity

Steps:
  1. Connect scan tool to OBD-II port (under dashboard, driver's side)
  2. Select vehicle make/model/engine
  3. Navigate to Engine Control Module (ECM/EDC)
  4. Read Diagnostic Trouble Codes (DTCs)
  5. Record and interpret each code

Common diesel-specific DTCs to look for:

FUEL SYSTEM:
  P0087 — Fuel rail pressure too low
  P0088 — Fuel rail pressure too high
  P0089 — Fuel pressure regulator performance
  P0093 — Fuel system large leak detected
  P0180-P0183 — Fuel temperature sensor circuit

EGR SYSTEM:
  P0401 — EGR flow insufficient
  P0402 — EGR flow excessive
  P0403 — EGR control circuit malfunction
  P0404 — EGR range/performance

GLOW PLUG SYSTEM:
  P0380 — Glow plug circuit A malfunction
  P0381 — Glow plug indicator circuit
  P0670 — Glow plug control module

For each DTC: Record code + description + 3 possible causes
```

---

### **WRAP-UP: Consolidation & Preview** (Slides 27-28, ~15 minutes)

---

#### Slide 27: What You Learned Today
**Visual:** Checklist with tick marks — mirroring the session objectives. Side illustration showing the complete Common Rail system with all components labeled.

**Instructor Narration:**
> "Let's take stock of what you've accomplished today. You walked in knowing gasoline fuel systems from yesterday. Now you can describe the entire Common Rail diesel system — from the low-pressure pump to the high-pressure pump, through the rail, to the injectors. You know the difference between solenoid and piezo injectors. You understand why modern diesels inject fuel five or seven times per combustion cycle instead of once. You can explain compression ignition and why glow plugs exist.
>
> You know what swirl flaps do, how variable intake geometry works, and why the EGR system is both essential and problematic. You've had your hands on real diesel components and you've read diesel-specific fault codes on a scan tool.
>
> Tomorrow, we shift from fuel delivery to the mechanical heart of the engine — the valve train and timing system. How does the engine know when to open and close the intake and exhaust valves? How does a timing chain or belt synchronise the crankshaft with the camshaft? And what happens when that synchronisation fails? Day 14 is going to be mechanical, precise, and critically important."

**PPT Content:**
```
DAY 13 RECAP — YOU CAN NOW:

  Name all Common Rail components and trace the fuel path
  Explain the high-pressure pump (CP3/CP4) and its role
  Describe rail pressure control (sensor + inlet metering + PCV)
  Distinguish solenoid vs piezo diesel injectors
  Explain multi-injection strategy (pilot, main, after, post)
  List 5+ differences between diesel and gasoline fuel systems
  Explain compression ignition and glow plug function
  Describe swirl flaps and variable intake geometry purpose
  Explain EGR system — valve, cooler, purpose, and carbon buildup
  Test EGR operation with a scan tool
  Read and interpret diesel-specific DTCs

TOMORROW: Valve Train & Timing Systems
```

---

#### Slide 28: Day 14 Preview — Valve Train & Timing
**Visual:** Timing chain and sprocket assembly with camshaft, crankshaft, and tensioner visible. Close-up of a camshaft lobe profile. Overlay showing the timing marks aligned.

**Instructor Narration:**
> "Day 14 is about timing — and I don't mean being punctual, though that helps. Every engine needs its valves to open and close at exactly the right moment relative to piston position. That synchronisation is maintained by a timing chain or timing belt connecting the crankshaft to the camshaft. We'll look at chain-driven and belt-driven systems, tensioners, variable valve timing, and what happens when timing goes wrong — interference engines and the costly consequences of a snapped belt. Make sure you've reviewed your four-stroke cycle notes — you'll need that foundation. See you tomorrow."

**PPT Content:**
```
DAY 14 PREVIEW: VALVE TRAIN & TIMING SYSTEMS

Topics:
  — Camshaft design and lobe profiles
  — Timing chains vs timing belts
  — Tensioners and guides
  — Timing marks and alignment
  — Variable valve timing (VVT) systems
  — Interference vs non-interference engines
  — What happens when timing fails

Bring: Your understanding of the 4-stroke cycle
Wear: Workshop-ready clothing

The engine's precision depends on perfect timing.
One tooth off = disaster.
```

---

## Assessment Checkpoint

**Formative (not graded):**
- Component identification: correctly locate and name at least 8 of 10 Common Rail components on the diesel engine
- Injector comparison: correctly identify at least 3 physical differences between solenoid and piezo injectors
- EGR inspection: correctly assess carbon buildup severity and valve movement quality
- DTC interpretation: correctly identify the system and at least 2 possible causes for each of 3 diesel DTCs
- Verbal quiz: explain in your own words why diesel engines don't need spark plugs

---

## Key Takeaways

1. Common Rail diesel separates pressure generation (pump) from injection timing (ECU + injectors) — this is the key design principle
2. Diesel fuel pressures (up to 2,500 bar) are an order of magnitude higher than gasoline — the components are engineered to an extreme level of precision
3. Multi-injection strategy (pilot, main, after, post) transforms crude diesel combustion into refined, quiet, clean operation
4. Diesel is compression ignition — no spark plugs, higher compression ratios, glow plugs only for cold start
5. EGR reduces NOx by lowering combustion temperature, but carbon buildup is the technician's constant battle
6. Swirl flaps and variable intake geometry optimise air-fuel mixing across the entire operating range

---

## Preparation for Day 14

**Instructor prep:**
- Prepare timing chain and timing belt sample assemblies (one of each)
- Have a cutaway engine or timing cover removed to show sprocket alignment
- Prepare timing mark alignment demonstration (crankshaft + camshaft marks)
- Print timing specification sheets for 2-3 common engine types
- Have photos/video ready showing the consequences of timing failure (bent valves, piston damage)
- Ensure feeler gauges and timing tools are available for valve clearance demonstration

**Learner prep:**
- Review the four-stroke cycle from Day 10
- Recall the relationship between crankshaft rotation and valve events
- Review today's notes on diesel intake manifold design (connects to valve timing discussion)
