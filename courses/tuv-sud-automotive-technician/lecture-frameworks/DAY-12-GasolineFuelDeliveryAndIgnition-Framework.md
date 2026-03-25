---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 3
week_title: "The Heart — Engine Systems"
day_number: 12
session_title: "Gasoline Fuel Delivery & Ignition"
duration_minutes: 180
theory_practice: "55:45"
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 12: Gasoline Fuel Delivery & Ignition
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (100 min theory + 80 min practical)
**Approach:** System Deep-Dive — Trace the Fuel and Spark Path
**PPT Target:** 26-28 slides
**Week:** 3 of 8 — "The Heart — Engine Systems"

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Compare MPFI and GDI fuel injection systems by operating principle, pressure, and injection timing
- Trace the ignition signal path from ECU through the coil-on-plug assembly to the spark plug
- Explain the purpose of the EVAP system and identify its main components
- Describe the operating principle of MAF and MAP sensors and their role in fuel metering
- Test ignition coil primary and secondary resistance with a multimeter
- Read spark plug condition and diagnose rich, lean, normal, and fouled states
- Perform a MAF sensor visual inspection and cleaning procedure

**This is Day 12 — Week 3, Day 2.** Learners completed Day 11 covering the four-stroke cycle, air and fuel paths, and the combustion overview. Today zooms in on HOW gasoline fuel is delivered and HOW the spark is created. This is component-level understanding building on yesterday's system-level picture.

---

## Connection to Prior Knowledge

Build from Day 11:
- The four-stroke cycle (intake, compression, power, exhaust)
- Air filter to intake manifold to cylinder path
- Fuel tank to fuel pump to fuel rail overview
- Basic understanding that the ECU controls injection and ignition timing

**Bridge:** "Yesterday you traced the full air and fuel path from outside the car all the way into the cylinder. Today we zoom in. How does gasoline actually get from the fuel rail into the combustion chamber? What creates the spark? And how does the ECU know how much air is coming in so it can calculate the right amount of fuel?"

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: Yesterday's Path, Today's Zoom** (Slides 1-3, ~10 minutes)

**Narrative Voice:** Focused, building curiosity. Connect yesterday's big picture to today's component detail.

---

#### Slide 1: Title & Session Context
**Visual:** Split image — left side shows the complete air-fuel path from Day 11 (greyed out), right side shows a zoomed-in, full-colour close-up of a fuel injector spraying into a cylinder with a spark plug firing above it

**Instructor Narration:**
> "Welcome back. Yesterday we followed air from the filter all the way to the exhaust pipe, and fuel from the tank to the rail. We saw the big picture. Today, we zoom in on three critical questions: How does gasoline get from the rail INTO the cylinder? What creates the spark that ignites it? And how does the ECU know how much air is flowing so it can calculate the perfect fuel amount? These are the components that make or break engine performance — and they're the components you'll diagnose and replace most often."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 3: The Heart — Engine Systems
Day 12: Gasoline Fuel Delivery & Ignition

Three questions today:
1. How does fuel enter the cylinder?
2. What creates the spark?
3. How does the ECU measure airflow?
```

---

#### Slide 2: Day 12 Roadmap
**Visual:** Horizontal timeline divided into five blocks with duration labels and icons (fuel injector, spark plug, canister, MAF sensor, wrench)

**Instructor Narration:**
> "Here's our plan. First, we compare the two main fuel injection types — port injection and direct injection. Then we trace the ignition system from the ECU signal all the way to the spark jumping the gap. After that, we cover three supporting systems: the EVAP system that captures fuel vapours, and the MAF and MAP sensors that tell the ECU how much air is coming in. Then we go hands-on — you'll test ignition coils, read spark plugs, and clean a MAF sensor. Let's get started."

**PPT Content:**
```
TODAY'S PLAN (180 minutes)

PART 1 (35 min): Fuel Injection — MPFI vs GDI
— How fuel enters the cylinder, pressure, timing, faults

PART 2 (30 min): Coil-on-Plug Ignition System
— Signal path, primary/secondary circuits, spark timing

PART 3 (25 min): EVAP System, MAF & MAP Sensors
— Vapour recovery, airflow measurement, common codes

PRACTICAL (60 min): Hands-On Component Testing
— Injector ID, coil resistance, spark plug reading, MAF cleaning

WRAP-UP (15 min): Recap + Day 13 Preview (Diesel)

Theory:Practice = 55:45
```

---

#### Slide 3: From Day 11 — Where We Left Off
**Visual:** Simplified block diagram from Day 11 showing: Air Filter → MAF → Throttle Body → Intake Manifold → Cylinder, and parallel path: Fuel Tank → Pump → Filter → Rail → Injector → Cylinder. Three circles highlight the areas being zoomed into today: the injector, the ignition coil/spark plug, and the MAF/MAP sensors

**Instructor Narration:**
> "Here's yesterday's map. Air comes in through the filter, past the MAF sensor, through the throttle body, and into the intake manifold. Fuel comes from the tank, through a pump and filter, into the rail, and out through the injectors. We drew this picture yesterday. Today, those three circled areas are where we zoom in. The injector — how does it spray? The coil and spark plug — how do they fire? The MAF and MAP — how do they measure? Let's start with the fuel."

**PPT Content:**
```
DAY 11 RECAP — THE AIR-FUEL PATH

AIR:   Filter → MAF Sensor → Throttle Body → Intake Manifold → Cylinder
FUEL:  Tank → Pump → Filter → Rail → Injector → Cylinder
SPARK: ECU → Ignition Coil → Spark Plug → Combustion

TODAY'S ZOOM AREAS:
  [1] Injector — MPFI vs GDI
  [2] Coil & Spark Plug — COP ignition
  [3] MAF & MAP — Air measurement
```

---

### **DEVELOPMENT PART 1: MPFI vs GDI Fuel Injection** (Slides 4-10, ~35 minutes)

**Narrative Voice:** Technical, comparative. Use side-by-side structures throughout to build the contrast.

---

#### Slide 4: Two Ways to Inject — The Big Picture
**Visual:** Side-by-side cross-section diagrams of MPFI and GDI. MPFI shows injector spraying into the intake port above the intake valve. GDI shows injector mounted directly in the combustion chamber spraying into the cylinder.

**Instructor Narration:**
> "There are two main ways to get gasoline into a combustion chamber in a modern engine. Multi-Point Fuel Injection — MPFI — sprays fuel into the intake port, just upstream of the intake valve. The fuel mixes with air in the port and enters the cylinder when the valve opens. Gasoline Direct Injection — GDI — skips the port entirely. The injector tip sits inside the combustion chamber and sprays fuel directly into the cylinder at very high pressure. Same goal, very different engineering. Let's compare them."

**PPT Content:**
```
TWO FUEL INJECTION STRATEGIES

MPFI (Multi-Point Fuel Injection):
• Injector in the INTAKE PORT
• Fuel mixes with air BEFORE entering cylinder
• Used since the 1990s — mature, reliable, affordable

GDI (Gasoline Direct Injection):
• Injector in the COMBUSTION CHAMBER
• Fuel sprayed DIRECTLY into cylinder
• Used increasingly since ~2010 — better efficiency, more complex

Both controlled by the ECU
Both use electromagnetic solenoid injectors (GDI also uses piezo)
```

---

#### Slide 5: MPFI — How It Works
**Visual:** Detailed cutaway of an MPFI injector showing the solenoid coil, pintle valve, spray nozzle, fuel inlet, and O-ring seals. Inset animation-style sequence: (1) ECU signal, (2) solenoid energised, (3) pintle lifts, (4) fuel sprays into port

**Instructor Narration:**
> "MPFI is straightforward. Each cylinder gets its own injector mounted in the intake manifold, pointing at the back of the intake valve. The fuel rail supplies fuel at 3 to 5 bar — that's about 45 to 75 PSI. When the ECU sends an electrical pulse, a solenoid inside the injector pulls a pintle valve off its seat. Fuel sprays out in a fine mist. The ECU controls how LONG the injector stays open — that's called the pulse width, measured in milliseconds. Longer pulse width means more fuel. Shorter means less. The ECU adjusts this hundreds of times per second based on sensor inputs."

**PPT Content:**
```
MPFI — MULTI-POINT FUEL INJECTION

Operating pressure: 3 - 5 bar (45 - 75 PSI)
Injection location: Intake port (upstream of intake valve)
Injector type: Electromagnetic solenoid, pintle-style
Control method: ECU varies PULSE WIDTH (milliseconds open time)

How it works:
1. ECU sends voltage pulse to injector solenoid
2. Magnetic field lifts pintle valve off seat
3. Fuel sprays through nozzle into intake port
4. Air-fuel mixture drawn into cylinder on intake stroke
5. ECU cuts signal → spring closes pintle → injection stops

Injection timing: Typically during intake stroke (sequential)
Pulse width at idle: ~2-4 ms
Pulse width at full load: ~8-15 ms
```

---

#### Slide 6: GDI — How It Works
**Visual:** Detailed cutaway of a GDI injector showing the multi-hole nozzle tip, high-pressure fuel inlet, and solenoid or piezo actuator. Inset showing the injector mounted through the cylinder head with its tip protruding into the combustion chamber

**Instructor Narration:**
> "GDI is the same basic idea — but taken to a different level. The injector sits inside the combustion chamber, which means it has to fight against compression pressure. That's why GDI operates at 100 to 200 bar — sometimes up to 350 bar on the latest engines. That's 40 to 70 times more pressure than MPFI. The high pressure atomises the fuel into incredibly fine droplets for better mixing.
>
> The injector design is different too. GDI injectors often have multiple holes — 6 or more — to create a precise spray pattern. Some use piezoelectric actuators instead of solenoids because piezo can open and close faster, allowing multiple injections per combustion cycle. The ECU might fire the injector two or three times in one cycle — a small injection during compression for stratified lean running, and a larger injection during intake for homogeneous charge."

**PPT Content:**
```
GDI — GASOLINE DIRECT INJECTION

Operating pressure: 100 - 200+ bar (1,450 - 2,900+ PSI)
Injection location: Directly into combustion chamber
Injector type: Multi-hole solenoid or piezoelectric
Control method: ECU varies pulse width AND injection timing

How it works:
1. High-pressure fuel pump (cam-driven) pressurises fuel to 100-200 bar
2. ECU sends signal to injector
3. Fuel sprays directly into cylinder through multi-hole nozzle
4. Ultra-fine atomisation due to extreme pressure
5. Multiple injections possible per cycle

Injection strategies:
• Homogeneous: Single injection during intake stroke (like MPFI, full power)
• Stratified: Late injection during compression (lean burn, fuel economy)
• Split: Multiple injections per cycle (best of both, reduce knock)
```

---

#### Slide 7: MPFI vs GDI — Side-by-Side Comparison
**Visual:** Comparison table with icons for each row — pressure gauge, thermometer, efficiency chart, wrench (service), warning triangle (faults)

**Instructor Narration:**
> "Let's put them side by side. MPFI runs at low pressure, is simpler, cheaper to build, and has fewer service issues. GDI runs at high pressure, gives better fuel economy and power, but is more complex and has unique service considerations — carbon buildup on intake valves is the biggest one. In MPFI, fuel washing over the intake valves keeps them clean. In GDI, fuel bypasses the valves entirely, so carbon deposits accumulate. Some manufacturers now use both — port injection for cleaning and low-load, direct injection for power — called dual injection."

**PPT Content:**
```
MPFI vs GDI — COMPARISON

                        MPFI              GDI
Fuel pressure:          3-5 bar           100-200+ bar
Pump type:              Electric in-tank   Electric + cam-driven HP
Injector location:      Intake port        Combustion chamber
Spray pattern:          Single pintle      Multi-hole
Fuel economy:           Baseline           5-15% improvement
Power output:           Baseline           3-10% improvement
Compression ratio:      ~10:1              ~12:1 (knock resistance)
Emissions (CO2):        Baseline           Lower
Particulate emissions:  Low                Higher (needs GPF)
Intake valve deposits:  Self-cleaning      Carbon buildup issue
System cost:            Lower              Higher
Service complexity:     Moderate           Higher

TREND: Many new engines use DUAL INJECTION (both MPFI + GDI)
```

---

#### Slide 8: The High-Pressure Fuel System (GDI)
**Visual:** Complete GDI fuel system diagram: electric in-tank pump (low pressure, 3-5 bar) → fuel line → high-pressure pump (cam-driven, mounted on engine) → high-pressure fuel rail (with pressure sensor) → GDI injectors. Labels show pressure at each stage.

**Instructor Narration:**
> "GDI engines need a two-stage fuel supply. The first stage is the same as MPFI — an electric pump in the fuel tank delivers fuel at 3 to 5 bar to the engine bay. But then a second pump takes over. This high-pressure pump is mechanically driven by the camshaft — it has a lobe that pushes a piston inside the pump. This pump takes the 5-bar fuel and ramps it up to 100, 150, even 200 bar. A pressure sensor on the fuel rail tells the ECU the actual rail pressure, and the ECU controls a pressure regulator to hit the target. If this high-pressure pump fails, the engine either won't start or runs very poorly."

**PPT Content:**
```
GDI HIGH-PRESSURE FUEL SYSTEM

Stage 1 — Low Pressure (same as MPFI):
Electric pump in fuel tank → 3-5 bar
Delivers fuel to engine bay

Stage 2 — High Pressure (GDI-specific):
Camshaft-driven mechanical pump → 100-200+ bar
Mounted on cylinder head, driven by camshaft lobe
Pressurises fuel in the high-pressure rail

Key components:
• Low-pressure pump (electric, in-tank)
• High-pressure pump (mechanical, cam-driven)
• High-pressure fuel rail (with pressure sensor)
• Fuel pressure regulator (ECU-controlled)
• GDI injectors (multi-hole, solenoid or piezo)

Common failures:
• HP pump failure → long crank / no start
• Pressure sensor fault → poor running, limp mode
• Injector carbon fouling → misfire, rough idle
```

---

#### Slide 9: Common MPFI and GDI Faults
**Visual:** Two-column fault table with DTC examples and diagnostic tips for each system

**Instructor Narration:**
> "Let's talk about what goes wrong. With MPFI, the most common faults are clogged injectors — fuel deposits build up on the pintle over time, especially with poor-quality fuel. You'll see rough idle, misfire codes, and a lean condition on the affected cylinder. Leaking injector O-rings are another classic — you'll smell fuel and may see a code for a rich condition.
>
> With GDI, carbon buildup on intake valves is the number one issue. Since fuel doesn't wash over the valves, crankcase vapours bake onto them over time. You get reduced airflow, misfires, and rough running. High-pressure pump failures and injector faults are also common. These are more expensive components to replace — a GDI injector can cost three to five times what a port injector costs."

**PPT Content:**
```
COMMON FUEL INJECTION FAULTS

MPFI FAULTS:
• Clogged injector → Misfire, rough idle, lean code (P0171/P0174)
• Leaking O-ring → Fuel smell, rich code (P0172/P0175)
• Dead injector (open coil) → Cylinder misfire (P030x)
• Fuel pressure low → Hard start, hesitation, lean codes
  DTC examples: P0201-P0208 (injector circuit)

GDI FAULTS:
• Carbon buildup on intake valves → Rough idle, misfire, loss of power
• HP pump failure → Long crank, no start, P0087 (fuel rail low pressure)
• Injector failure → Misfire (P030x), rough running
• Fuel rail pressure sensor → Limp mode, P0190-P0194
• Injector deposit/coking → Poor spray pattern, misfire

SERVICE NOTE:
GDI intake valve cleaning (walnut blasting) is a common service
GDI injectors: 3-5x cost of MPFI injectors
```

---

#### Slide 10: Fuel Injector Quick-Check Methods
**Visual:** Three photos: (1) Mechanic's stethoscope on an injector listening for click, (2) Noid light plugged into injector connector, (3) Multimeter measuring injector resistance

**Instructor Narration:**
> "Before we move to ignition, here are three quick injector checks you'll use in the field. First — the stethoscope test. Place a mechanic's stethoscope on each injector while the engine runs. You should hear a consistent clicking. No click means the injector isn't being pulsed or is mechanically stuck. Second — a noid light. Unplug the injector and connect this light to the harness connector. If it flashes, the ECU is sending the signal — the wiring is good, and the problem is the injector itself. Third — resistance test. With the injector unplugged and ignition off, measure resistance across the two pins. A typical MPFI injector reads 12 to 16 ohms. GDI injectors vary — check the service manual. Open circuit or very low resistance means the coil is damaged."

**PPT Content:**
```
FUEL INJECTOR QUICK-CHECK METHODS

1. STETHOSCOPE TEST (engine running):
   Place on each injector body → listen for consistent clicking
   No click = no pulse or stuck injector

2. NOID LIGHT TEST (engine cranking):
   Unplug injector → connect noid light to harness
   Flashing = ECU signal present (wiring OK)
   No flash = wiring or ECU fault

3. RESISTANCE TEST (ignition OFF, injector unplugged):
   Multimeter on ohms → measure across injector pins
   MPFI typical: 12 - 16 ohms (high impedance)
   GDI solenoid: Check service manual (varies by manufacturer)
   Open circuit (OL) = failed coil winding
   Very low (<1 ohm) = short circuit

Always compare cylinder-to-cylinder — consistency matters
```

---

### **DEVELOPMENT PART 2: Coil-on-Plug Ignition System** (Slides 11-17, ~30 minutes)

**Narrative Voice:** Systematic, tracing the signal path step by step. Emphasise the electrical chain.

---

#### Slide 11: Ignition System Overview — COP Architecture
**Visual:** Block diagram showing the complete ignition signal path: ECU → ignition driver circuit → COP connector (3-pin: power, ground, signal) → ignition coil primary winding → ignition coil secondary winding → spark plug → spark jumps gap → ground through engine block

**Instructor Narration:**
> "Now let's trace the spark. Modern gasoline engines use Coil-on-Plug ignition — COP. Each cylinder has its own ignition coil sitting directly on top of its spark plug. No distributor, no spark plug wires. The ECU controls each coil individually, deciding exactly when to fire based on crankshaft position, engine speed, load, temperature, and knock sensor feedback.
>
> Here's the signal path. The ECU sends a switching signal to the coil. The coil transforms 12 volts from the battery into 25,000 to 45,000 volts. That high voltage jumps across the spark plug gap — about 0.7 to 1.1 millimetres — creating the spark that ignites the air-fuel mixture. Simple in concept, but the precision of WHEN that spark fires is critical to engine performance."

**PPT Content:**
```
COIL-ON-PLUG (COP) IGNITION — OVERVIEW

Architecture: One coil per cylinder, mounted directly on spark plug
Replaced: Distributor systems, wasted-spark systems
Advantage: Individual cylinder control, no HV wires, compact

Signal path:
ECU → Ignition Coil Primary → Ignition Coil Secondary → Spark Plug

Voltages:
• Primary circuit: 12V battery voltage (switched by ECU)
• Secondary circuit: 25,000 - 45,000V (generated by coil)

The ECU decides WHEN to fire based on:
• Crankshaft position sensor (CKP)
• Engine speed (RPM)
• Engine load (MAF/MAP)
• Coolant temperature
• Knock sensor feedback
• Camshaft position sensor (CMP)
```

---

#### Slide 12: Inside the Ignition Coil — Primary and Secondary
**Visual:** Cutaway diagram of a COP ignition coil showing primary winding (few hundred turns of thick wire), secondary winding (tens of thousands of turns of fine wire), iron core, connector pins, and spark plug boot at the bottom

**Instructor Narration:**
> "An ignition coil is a transformer. It has two windings wrapped around an iron core. The primary winding has a few hundred turns of relatively thick wire — low resistance, typically 0.5 to 2 ohms. The secondary winding has 10,000 to 30,000 turns of very fine wire — high resistance, typically 6,000 to 15,000 ohms.
>
> Here's how it works. The ECU sends current through the primary winding, building a magnetic field in the iron core. This charging time is called dwell time — typically 2 to 4 milliseconds. When the ECU suddenly cuts the current, the magnetic field collapses. That collapsing field induces a massive voltage spike in the secondary winding — the turns ratio multiplies the voltage from 12 volts to 25,000 or more. That voltage is what jumps the spark plug gap."

**PPT Content:**
```
INSIDE THE COP IGNITION COIL

PRIMARY WINDING:
• Few hundred turns of thick wire
• Resistance: 0.5 - 2.0 ohms
• Carries battery voltage (12V)
• ECU controls current flow ON/OFF

SECONDARY WINDING:
• 10,000 - 30,000 turns of fine wire
• Resistance: 6,000 - 15,000 ohms (6k-15k)
• Produces 25,000 - 45,000V output

OPERATING PRINCIPLE:
1. ECU turns ON primary current → magnetic field builds (DWELL)
2. Dwell time: 2-4 ms (charging the coil)
3. ECU turns OFF primary current → field collapses instantly
4. Collapsing field induces HV in secondary (transformer action)
5. HV travels down coil boot to spark plug → SPARK

Turns ratio = Secondary turns / Primary turns ≈ 100:1
Voltage ratio follows turns ratio (approximately)
```

---

#### Slide 13: Dwell Time and Spark Timing
**Visual:** Oscilloscope trace showing the primary ignition waveform — dwell period (coil charging), point of trigger (spike), and spark duration. Below, a simplified crankshaft rotation diagram showing when the spark fires relative to TDC (Top Dead Centre)

**Instructor Narration:**
> "Two critical timing parameters. Dwell time is how long the ECU holds current through the primary winding before releasing it. Too short — the coil doesn't fully charge, and you get a weak spark. Too long — the coil overheats. The ECU calculates the optimum dwell based on battery voltage and engine conditions.
>
> Spark timing — also called ignition timing — is WHEN the ECU fires the coil relative to the piston position. At idle, the spark might fire 10 degrees before Top Dead Centre. At high RPM, it might fire 30 or 40 degrees before TDC — this is called advance. The mixture needs time to burn, and at higher RPM there's less time per cycle, so the ECU fires earlier. If the ECU detects knock — detonation — it retards the timing to protect the engine."

**PPT Content:**
```
DWELL TIME AND SPARK TIMING

DWELL TIME:
• Duration ECU holds primary current ON (charging the coil)
• Typical: 2-4 milliseconds
• Adjusted by ECU based on battery voltage and RPM
• Too short = weak spark → misfire
• Too long = coil overheats → damage

SPARK TIMING (Ignition Advance):
• Expressed in degrees Before Top Dead Centre (BTDC)
• Idle: ~8-15 degrees BTDC
• Cruise: ~20-35 degrees BTDC
• Full load: ~15-25 degrees BTDC (less advance to avoid knock)
• High RPM: More advance (less time per cycle)

KNOCK CONTROL:
• Knock sensor detects detonation (engine "pinging")
• ECU retards timing to eliminate knock
• Protects engine from damage
• If timing can't be retarded enough → DTC set
```

---

#### Slide 14: Spark Plug Construction and Heat Range
**Visual:** Labelled cross-section of a spark plug: terminal, insulator, shell, centre electrode, ground electrode, gap. Second diagram showing heat flow path and comparison of "hot" vs "cold" spark plug insulator nose lengths

**Instructor Narration:**
> "The spark plug is where the electrical energy becomes a physical spark. The high voltage from the coil travels down the centre electrode. It jumps the gap — 0.7 to 1.1 mm for most engines — to the ground electrode. That arc ignites the mixture.
>
> Spark plugs have a heat range — this is about how fast the plug sheds heat from its tip. A 'hot' plug has a long insulator nose that retains heat — good for low-performance engines that run cooler. A 'cold' plug has a short insulator nose that dissipates heat quickly — essential for high-performance or turbocharged engines. If you fit the wrong heat range, you get either fouling — plug too cold, or pre-ignition — plug too hot. Always match the manufacturer's specification."

**PPT Content:**
```
SPARK PLUG CONSTRUCTION

Components (top to bottom):
• Terminal nut — connects to coil boot
• Ceramic insulator — electrical isolation, withstands 45kV
• Metal shell — threads into cylinder head, provides ground path
• Centre electrode — carries HV from coil (iridium or platinum tip)
• Ground electrode — welded to shell, forms the gap
• Gap: 0.7 - 1.1 mm (check spec for each engine)

HEAT RANGE:
• HOT plug = long insulator nose → retains heat → self-cleaning
  Use: Low-load engines, city driving
• COLD plug = short insulator nose → dissipates heat fast
  Use: High-performance, turbocharged, sustained high RPM

ELECTRODE MATERIALS:
• Copper-core: Cheapest, shortest life (~30,000 km)
• Platinum: Longer life (~80,000 km)
• Iridium: Longest life (~100,000+ km), finest centre electrode
• Double precious metal: Platinum/iridium on both electrodes
```

---

#### Slide 15: Reading Spark Plug Condition
**Visual:** Four photographs of spark plugs showing: (1) Normal — tan/grey insulator, (2) Rich — black, sooty deposits, (3) Lean — white/blistered insulator, (4) Oil-fouled — wet, black, oily deposits. Each labelled with condition and likely cause.

**Instructor Narration:**
> "A spark plug is a window into the combustion chamber. Pull the plug and its appearance tells you what's happening inside. A normal plug has a light tan or grey insulator tip — this means the air-fuel mixture is correct and combustion is clean.
>
> A black, sooty plug means the mixture is too rich — too much fuel or not enough air. Common causes: leaking injector, faulty MAF sensor, or a clogged air filter. A white or blistered plug means the mixture is too lean — too little fuel or too much air. This is dangerous because lean mixtures burn hot and can damage the engine. An oil-fouled plug — wet and black — means oil is getting into the combustion chamber, usually from worn valve seals or piston rings. You'll practice reading these in the practical session."

**PPT Content:**
```
READING SPARK PLUG CONDITION

NORMAL:
• Insulator: Light tan / grey
• Electrodes: Light wear, no deposits
• Diagnosis: Correct mixture, healthy combustion

RICH (Too much fuel):
• Insulator: Black, dry soot deposits
• Cause: Leaking injector, faulty MAF, clogged air filter, stuck-open purge valve
• DTC hint: P0172 / P0175 (System Too Rich)

LEAN (Too little fuel):
• Insulator: White, blistered, may show electrode erosion
• Cause: Vacuum leak, weak fuel pump, clogged injector, faulty MAF
• DTC hint: P0171 / P0174 (System Too Lean)
• WARNING: Lean = HOT combustion → engine damage risk

OIL-FOULED:
• Insulator: Wet, black, oily deposits
• Cause: Worn valve stem seals, worn piston rings, PCV fault
• DTC hint: May see P030x (misfire) + blue exhaust smoke

CARBON-FOULED:
• Dry black deposits, fluffy texture
• Cause: Short trips, cold running, ignition fault, rich mixture
```

---

#### Slide 16: COP Ignition — Common Failures
**Visual:** Photo of a COP coil with a visible crack in the boot, alongside an oscilloscope showing a misfire pattern. Diagnostic flowchart: Misfire Code → Swap Coil → Misfire Follow? → Yes = Bad Coil / No = Check Plug/Injector

**Instructor Narration:**
> "COP coils are reliable, but they do fail. The most common symptom is a misfire on a specific cylinder — you'll get a P030x code where x is the cylinder number. P0301 means cylinder 1 misfire, P0302 means cylinder 2, and so on. The classic diagnostic trick is the coil swap test: move the suspect coil to a different cylinder. If the misfire follows the coil, you've found your problem. If it stays on the original cylinder, the fault is the spark plug, injector, or a mechanical issue.
>
> Other failure modes: cracked coil boots let moisture in and cause arcing to the valve cover. Internal winding shorts cause weak spark. And sometimes the coil driver circuit inside the ECU fails — though that's less common. Always check the spark plug condition when replacing a coil — a fouled plug could have caused the coil to overwork and fail."

**PPT Content:**
```
COP IGNITION — COMMON FAILURES

SYMPTOMS OF COP FAILURE:
• Misfire on specific cylinder (P0301, P0302, P0303, P0304...)
• Rough idle
• Engine shaking / vibration
• Flashing check engine light (catalyst-damaging misfire)
• Reduced power, hesitation

DIAGNOSTIC PROCESS — COIL SWAP TEST:
1. Read DTCs — note which cylinder misfires (P030x)
2. Swap suspect coil with a known-good coil from another cylinder
3. Clear codes, run engine
4. If misfire FOLLOWS the coil → replace coil
5. If misfire STAYS on original cylinder → check plug, injector, compression

OTHER COP FAULTS:
• Cracked rubber boot → moisture ingress → arcing
• Internal short → weak spark, intermittent misfire
• Connector corrosion → poor signal, random misfires
• Coil boot stuck on plug → boot tears during removal

ALWAYS inspect spark plug when replacing a coil
```

---

#### Slide 17: Ignition Coil Testing with Multimeter
**Visual:** Step-by-step photo sequence: (1) Coil removed from engine, (2) Multimeter set to ohms, (3) Probes on primary pins, (4) Probes on secondary terminals. Callout boxes showing expected resistance values.

**Instructor Narration:**
> "You can bench-test an ignition coil with a basic multimeter. Two tests: primary resistance and secondary resistance. For primary — set your meter to the lowest ohms range. Place your probes on the two small connector pins — usually the power and signal pins. You should read 0.5 to 2 ohms. If you read open circuit — infinity — the primary winding is broken.
>
> For secondary — place one probe on the same connector pin and the other probe inside the spark plug boot, touching the terminal contact. You should read 6,000 to 15,000 ohms — 6 to 15 kilohms. Open circuit means a broken secondary winding. Very low resistance means a short circuit. These tests don't catch every fault — a coil can pass resistance tests but fail under load — but they catch the obvious failures. You'll do this in the practical."

**PPT Content:**
```
IGNITION COIL TESTING — MULTIMETER

EQUIPMENT: Digital multimeter (DMM)
CONDITION: Ignition OFF, coil removed from engine, cool

TEST 1 — PRIMARY RESISTANCE:
• Meter setting: Ohms (lowest range, e.g., 200 ohms)
• Probes: Across the two small connector pins (power & signal)
• Expected: 0.5 - 2.0 ohms
• OL (open) = broken primary winding → REPLACE
• 0.0 ohms = short circuit → REPLACE

TEST 2 — SECONDARY RESISTANCE:
• Meter setting: Ohms (20k range)
• Probes: One on connector pin, one inside spark plug boot (HV terminal)
• Expected: 6,000 - 15,000 ohms (6k - 15k)
• OL (open) = broken secondary winding → REPLACE
• Very low = internal short → REPLACE

NOTE: Resistance test catches ~70% of failures
Remaining 30% need oscilloscope or ignition analyser (under load)
Always check manufacturer spec for exact values
```

---

### **DEVELOPMENT PART 3: EVAP System, MAF & MAP Sensors** (Slides 18-23, ~25 minutes)

**Narrative Voice:** Practical and diagnostic-focused. These are the supporting systems that complete the fuel delivery and metering picture.

---

#### Slide 18: EVAP System — Preventing Vapour Escape
**Visual:** Complete EVAP system diagram: fuel tank → vapour line → charcoal canister → purge valve (ECU-controlled) → intake manifold. Also shown: vent valve and leak detection pump (LDP). Arrows show vapour flow path during purge cycle.

**Instructor Narration:**
> "Gasoline evaporates. In a sealed tank on a hot day, pressure builds. If you just vented that to the atmosphere, you'd release hydrocarbons — a pollutant and a contributor to smog. The EVAP system — Evaporative Emission Control — captures those fuel vapours and burns them in the engine instead of releasing them.
>
> Here's how it works. Fuel vapour from the tank flows through a line into a charcoal canister. The activated charcoal adsorbs the hydrocarbons and traps them. When the engine is running and conditions are right — warmed up, not at idle, not at full load — the ECU opens a purge valve. Fresh air flows through the canister, strips the hydrocarbons off the charcoal, and carries them into the intake manifold to be burned during normal combustion. The vent valve controls the air entry side. A leak detection pump periodically pressurises the system to check for leaks."

**PPT Content:**
```
EVAP SYSTEM — EVAPORATIVE EMISSION CONTROL

PURPOSE: Capture fuel tank vapours, prevent hydrocarbon release to atmosphere
REGULATION: Required by emissions standards worldwide

COMPONENTS:
• Charcoal canister — traps fuel vapours (activated carbon)
• Purge valve (solenoid) — ECU-controlled, connects canister to intake
• Vent valve (solenoid) — controls fresh air entry to canister
• Leak detection pump (LDP) — pressurises system to find leaks
• Vapour lines — connect tank to canister and canister to intake

OPERATION:
1. Engine OFF: Vapours collect in charcoal canister
2. Engine RUNNING (warm, part load):
   ECU opens purge valve → fresh air through canister
   → carries trapped HC into intake manifold → burned in engine
3. LEAK TEST: LDP pressurises system, monitors pressure decay
   Small leak → DTC, large leak → DTC + MIL

No moving parts exposed to fuel — reliable but hoses age and crack
```

---

#### Slide 19: EVAP System — Common DTCs
**Visual:** Table of common EVAP codes (P0440-P0457) with descriptions, common causes, and diagnostic approach for each

**Instructor Narration:**
> "EVAP codes are some of the most common DTCs you'll encounter. P0440 is the general code — EVAP system malfunction. P0442 is a small leak detected. P0455 is a large leak — and the number one cause is a loose or missing fuel cap. Seriously — before you start diagnosing EVAP codes, always check the fuel cap first. P0456 is a very small leak, and P0457 specifically calls out the fuel cap.
>
> The purge valve and vent valve each have their own codes too. P0441 — incorrect purge flow — often means the purge valve is stuck open or the canister is saturated. P0446 — vent control circuit — usually points to the vent valve solenoid or its wiring. EVAP diagnosis requires a smoke machine to find small leaks — you pressurize the system with smoke and look for where it escapes."

**PPT Content:**
```
EVAP SYSTEM — COMMON DTCs

P0440 — EVAP System Malfunction (general)
P0441 — Incorrect Purge Flow
  → Purge valve stuck, canister saturated, vacuum leak
P0442 — Small Leak Detected
  → Cracked hose, loose connection, canister crack
P0443 — Purge Valve Circuit Malfunction
  → Wiring, connector, or valve solenoid failure
P0446 — Vent Control Circuit Malfunction
  → Vent valve solenoid or wiring fault
P0455 — Large Leak Detected
  → Missing/loose fuel cap, disconnected hose, cracked canister
P0456 — Very Small Leak Detected
  → Hairline crack in hose, aged O-ring, canister micro-crack
P0457 — Leak Detected (Fuel Cap)
  → Loose, damaged, or missing fuel cap

DIAGNOSTIC TIP #1: ALWAYS check fuel cap first
DIAGNOSTIC TIP #2: Smoke machine is the go-to tool for leak detection
```

---

#### Slide 20: MAF Sensor — Mass Air Flow Measurement
**Visual:** Cutaway of a hot-wire MAF sensor showing the sensing element (heated wire or film), temperature compensation resistor, intake air flow direction, and connector. Inset graph showing MAF voltage vs airflow (rising curve).

**Instructor Narration:**
> "The MAF sensor answers the most important question the ECU has: how much air is entering the engine RIGHT NOW? It uses the hot-wire principle. Inside the sensor housing, there's a thin wire or film element that's electrically heated to a constant temperature above the incoming air temperature. As air flows over it, it cools the wire down. The sensor's electronics increase the current to maintain the temperature. The amount of current needed is directly proportional to the mass of air flowing — more air, more cooling, more current.
>
> The ECU reads this as a voltage signal — typically 0.5 volts at idle up to 4.5 volts at full load — or as a frequency signal on some designs. This is the primary input for fuel calculation. If the MAF reads wrong, the fuel mixture is wrong — and you'll see driveability problems immediately."

**PPT Content:**
```
MAF SENSOR — MASS AIR FLOW

PURPOSE: Measure the mass of air entering the engine (grams/second)
LOCATION: Between air filter box and throttle body
PRINCIPLE: Hot-wire (or hot-film)

HOW IT WORKS:
1. Sensing element heated to constant temperature above intake air
2. Airflow cools the element
3. Electronics increase current to maintain temperature
4. Current required = proportional to air mass flow
5. ECU reads voltage (0.5-4.5V) or frequency signal

SIGNAL:
• Idle: ~0.8-1.2V (low airflow)
• Cruise: ~2.0-3.0V (moderate airflow)
• Full throttle: ~4.0-4.5V (maximum airflow)

WHY MASS (not volume)?
Mass accounts for temperature and pressure changes
Cold dense air = more oxygen = need more fuel
Hot thin air = less oxygen = need less fuel
MAF measures this automatically
```

---

#### Slide 21: MAF Sensor — Faults and Cleaning
**Visual:** Photo of a dirty MAF sensing element with visible contamination (oil film, dust particles). Second photo showing MAF sensor cleaner spray being applied. Third photo showing the cleaned element.

**Instructor Narration:**
> "MAF sensors are exposed to all the air entering the engine, and despite the air filter, they get dirty. Oil mist from the crankcase ventilation system is the biggest culprit — it coats the sensing wire and insulates it, making it under-read. The ECU thinks less air is coming in than actually is, so it injects less fuel. You get a lean condition, hesitation on acceleration, rough idle, and sometimes black smoke on hard acceleration when the ECU compensates.
>
> The good news: you can often fix this with MAF sensor cleaner — a specific electronics cleaner spray. Remove the sensor, spray the sensing element from a distance of 10 to 15 centimetres, let it air dry completely, reinstall. Don't touch the wire with your fingers or any tool — it's extremely delicate. Don't use carburettor cleaner or brake cleaner — they leave residue. Use ONLY MAF-specific cleaner."

**PPT Content:**
```
MAF SENSOR — FAULTS AND CLEANING

COMMON SYMPTOMS OF DIRTY / FAULTY MAF:
• Rough or unstable idle
• Hesitation on acceleration
• Black smoke under load
• Poor fuel economy
• Stalling after starting
• DTC: P0100-P0104 (MAF circuit range/performance)
• DTC: P0171/P0174 (System Too Lean — MAF under-reading)

MAF CLEANING PROCEDURE:
1. Remove MAF sensor from intake duct (usually 2 screws + connector)
2. Inspect sensing element (thin wire or film visible inside)
3. Spray with MAF SENSOR CLEANER ONLY (CRC, Wurth, etc.)
4. Spray from 10-15 cm distance, 5-10 short bursts
5. DO NOT touch the sensing element with fingers or tools
6. DO NOT use carb cleaner, brake cleaner, or compressed air
7. Let air dry completely (10-15 minutes)
8. Reinstall, clear codes, test drive

REPLACEMENT: If cleaning doesn't fix symptoms, replace sensor
Typical MAF sensor cost: moderate (manufacturer-dependent)
```

---

#### Slide 22: MAP Sensor — Manifold Absolute Pressure
**Visual:** Cutaway of a MAP sensor showing the piezoelectric/piezoresistive sensing element, reference vacuum chamber, pressure port, and connector. Diagram showing MAP sensor mounted on intake manifold with vacuum hose or direct-mount.

**Instructor Narration:**
> "The MAP sensor measures the pressure inside the intake manifold. This tells the ECU how hard the engine is working — because intake manifold pressure changes with throttle position and engine load. At idle with the throttle nearly closed, the manifold has high vacuum — low absolute pressure, around 25 to 30 kPa. At wide-open throttle, the manifold pressure approaches atmospheric — around 95 to 100 kPa. On turbocharged engines, it goes above atmospheric.
>
> Inside the sensor, a piezoresistive element flexes with pressure changes, altering its electrical resistance. The sensor outputs a voltage proportional to pressure — low voltage at idle, high voltage at full load. Some engines use the MAP sensor as the primary air measurement — this is called a speed-density system. It calculates air mass from manifold pressure plus engine RPM plus air temperature. Other engines use MAF as primary and MAP as a backup or for barometric pressure reference."

**PPT Content:**
```
MAP SENSOR — MANIFOLD ABSOLUTE PRESSURE

PURPOSE: Measure intake manifold pressure (engine load indicator)
LOCATION: On intake manifold (direct mount or via vacuum hose)
PRINCIPLE: Piezoresistive element deflects with pressure

HOW IT WORKS:
1. Manifold pressure acts on a silicon diaphragm
2. Diaphragm deflection changes resistance of piezo elements
3. Wheatstone bridge circuit converts to voltage signal
4. ECU reads voltage: low = vacuum (idle), high = pressure (load)

SIGNAL:
• Idle: ~1.0-1.5V (~25-30 kPa — high vacuum)
• Cruise: ~2.0-2.5V (~50-60 kPa — moderate vacuum)
• Wide Open Throttle: ~4.0-4.5V (~95-100 kPa — atmospheric)
• Turbocharged / boosted: >4.5V (>100 kPa — positive pressure)

KEY OFF / ENGINE OFF: Reads barometric (atmospheric) pressure
  → ECU uses this for altitude compensation

TWO AIR MEASUREMENT STRATEGIES:
• MAF-based: MAF is primary, MAP as backup / baro reference
• Speed-Density: MAP + RPM + IAT = calculated air mass (no MAF)
```

---

#### Slide 23: MAP Sensor — Faults and Diagnosis
**Visual:** Diagnostic flowchart for MAP sensor issues. Includes vacuum hose check, voltage reading at idle vs WOT, and comparison with barometric reading at key-on-engine-off.

**Instructor Narration:**
> "MAP sensor faults usually show up as poor running, hesitation, black smoke, or stalling. If the sensor is reading too high — telling the ECU the engine is under more load than it actually is — the ECU adds fuel and you get a rich condition. If it reads too low, you get lean. Common causes of MAP failure are a cracked or disconnected vacuum hose — always check the hose first — a failed sensor element, or water ingress into the sensor.
>
> Quick diagnosis: with the engine off and ignition on, the MAP should read approximately atmospheric pressure — around 4.5 volts or 95-100 kPa. Start the engine — at idle, it should drop to about 1.0-1.5 volts. Snap the throttle — it should spike up toward 4.5 volts and return. If it doesn't change, or the signal is erratic, suspect the sensor or its hose. DTCs P0105 through P0109 cover MAP circuit faults."

**PPT Content:**
```
MAP SENSOR — FAULTS AND DIAGNOSIS

COMMON SYMPTOMS:
• Rough idle, stalling
• Hesitation, poor throttle response
• Black smoke (rich if MAP reads high)
• Hard starting
• Poor fuel economy
• DTC: P0105-P0109 (MAP circuit range/performance)

DIAGNOSTIC CHECKS:
1. Vacuum hose (if fitted):
   Check for cracks, disconnection, kinks, moisture
   Hose fault = most common cause of MAP issues

2. Voltage at KOEO (Key On, Engine Off):
   Should read ~4.0-4.5V (atmospheric pressure)
   If not = sensor fault or wiring

3. Voltage at idle:
   Should read ~1.0-1.5V (manifold vacuum)
   If same as KOEO = hose disconnected or sensor stuck

4. Snap throttle test:
   Voltage should spike to ~4.0V+ and return to idle value
   No change = sensor not responding

5. Compare MAP baro reading with known altitude/weather data
```

---

### **PRACTICAL SESSION: Hands-On Component Testing** (Slides 24-25, ~60 minutes)

**Narrative Voice:** Direct, instructional. Clear safety reminders. Structured station rotation.

---

#### Slide 24: Practical — Station Setup
**Visual:** Workshop floor plan showing four stations labelled A through D, with equipment lists for each. Arrows show rotation path. Timer icon showing 15 minutes per station.

**Instructor Narration:**
> "Time to get your hands on these components. I've set up four stations. You'll rotate through all four, spending 15 minutes at each. Station A: identify MPFI and GDI components on the bench engines — point to the fuel rail, injectors, high-pressure pump on the GDI engine, and note the differences. Station B: test ignition coils with the multimeter — primary and secondary resistance. I want readings recorded on your worksheet. Station C: spark plug reading — I've laid out plugs in various conditions. Identify each as normal, rich, lean, oil-fouled, or carbon-fouled. Station D: MAF sensor inspection and cleaning — remove the sensor, inspect the element, clean it properly, and reinstall. Any questions before we start? Safety glasses on. Let's go."

**PPT Content:**
```
PRACTICAL SESSION — 4 STATIONS x 15 MINUTES

STATION A: COMPONENT IDENTIFICATION
• Bench engines: MPFI and GDI
• Identify: fuel rail, injectors, HP pump (GDI), fuel pressure sensor
• Note differences in injector mounting, fuel line routing

STATION B: IGNITION COIL TESTING
• Remove COP coil from bench engine
• Multimeter: measure primary resistance (expected: 0.5-2.0 ohms)
• Multimeter: measure secondary resistance (expected: 6k-15k ohms)
• Record readings on worksheet, compare to spec

STATION C: SPARK PLUG READING
• 8 spark plugs in various conditions
• Identify each: Normal / Rich / Lean / Oil-Fouled / Carbon-Fouled
• Record diagnosis and likely cause on worksheet

STATION D: MAF SENSOR INSPECTION & CLEANING
• Remove MAF from intake duct
• Inspect sensing element visually
• Clean with MAF sensor cleaner (proper technique)
• Reinstall and verify connector secure

SAFETY: Glasses on. No running engines. Ask before you're unsure.
```

---

#### Slide 25: Practical — Worksheets and Recording
**Visual:** Example of a filled-in worksheet showing ignition coil readings (primary and secondary), spark plug condition chart with tick boxes, and MAF inspection notes

**Instructor Narration:**
> "Use your worksheet to record everything. For the coil test, write down the actual ohm readings for primary and secondary, and mark pass or fail against the specification. For spark plug reading, sketch or describe the plug appearance and write your diagnosis. For the MAF cleaning, note the condition before and after. These worksheets become part of your portfolio — they show you can perform these tasks. I'll be circulating to check your technique. Call me over if you're stuck. Begin at your assigned station."

**PPT Content:**
```
RECORDING YOUR PRACTICAL WORK

COIL TEST WORKSHEET:
Coil #    Primary (ohms)    Spec    P/F    Secondary (ohms)    Spec    P/F
  1       ____________    0.5-2.0   __     ______________    6k-15k    __
  2       ____________    0.5-2.0   __     ______________    6k-15k    __
  3       ____________    0.5-2.0   __     ______________    6k-15k    __

SPARK PLUG READING:
Plug #   Colour/Condition     Diagnosis        Likely Cause
  1      _______________    ____________    ________________
  2      _______________    ____________    ________________
  ...

MAF INSPECTION:
Before cleaning: ____________________
Cleaning product used: _______________
After cleaning: _____________________
Technique notes: ____________________

KEEP THESE WORKSHEETS — they are portfolio evidence
```

---

### **WRAP-UP: Consolidation & Day 13 Preview** (Slides 26-28, ~15 minutes)

---

#### Slide 26: Day 12 Recap — What You Learned
**Visual:** Visual summary with icons for each topic area — fuel injector (MPFI/GDI), spark plug and coil, EVAP canister, MAF sensor, MAP sensor — arranged around a central engine diagram

**Instructor Narration:**
> "Let's consolidate. Today you learned two fuel injection strategies — MPFI at 3-5 bar spraying into the port, and GDI at 100-200 bar spraying directly into the chamber. You traced the ignition signal from the ECU through the coil-on-plug to the spark plug, and you understand dwell time and timing advance. You learned how the EVAP system captures fuel vapours and what the common codes mean. And you learned how the MAF and MAP sensors tell the ECU how much air is coming in so it can calculate the right fuel amount. On the practical side, you tested coils, read spark plugs, and cleaned a MAF sensor. That's a solid Day 12."

**PPT Content:**
```
DAY 12 RECAP — GASOLINE FUEL DELIVERY & IGNITION

FUEL INJECTION:
  MPFI: 3-5 bar, intake port, reliable, self-cleaning valves
  GDI: 100-200 bar, combustion chamber, efficient, carbon buildup risk

IGNITION:
  COP: ECU → coil primary → secondary (25-45kV) → spark plug
  Dwell time: 2-4 ms charging period
  Timing: Advances with RPM, retards for knock protection

EVAP SYSTEM:
  Charcoal canister traps vapours, purge valve sends to engine
  Common codes: P0440-P0457 (check fuel cap first!)

AIR MEASUREMENT:
  MAF: Hot-wire principle, measures air mass directly
  MAP: Piezoresistive, measures manifold pressure (engine load)

PRACTICAL SKILLS GAINED:
  Coil primary/secondary resistance testing
  Spark plug condition reading
  MAF sensor cleaning procedure
```

---

#### Slide 27: Quick Knowledge Check
**Visual:** Five numbered questions with space for discussion

**Instructor Narration:**
> "Quick check before we leave. Five questions — call out the answers. One: what pressure range does a GDI fuel system operate at? Two: what is the typical primary resistance of a COP ignition coil? Three: what is the FIRST thing you check when you see an EVAP leak code? Four: how does a hot-wire MAF sensor work — in one sentence? Five: at idle, does a MAP sensor read high voltage or low voltage? Good — if you can answer all five, you've got today's material."

**PPT Content:**
```
QUICK KNOWLEDGE CHECK

1. GDI fuel pressure range?
   → 100-200+ bar

2. Typical COP primary coil resistance?
   → 0.5 - 2.0 ohms

3. First check for an EVAP leak code (P0455)?
   → Fuel cap (loose, damaged, or missing)

4. How does a hot-wire MAF work (one sentence)?
   → Airflow cools a heated element; current needed to maintain
     temperature is proportional to air mass flow

5. MAP sensor voltage at idle — high or low?
   → LOW (~1.0-1.5V) because manifold vacuum is high
     (low absolute pressure)
```

---

#### Slide 28: Day 13 Preview — Diesel Fuel Delivery
**Visual:** Preview image showing a common-rail diesel injection system with high-pressure pump, rail, and piezo injectors — visually contrasting with today's gasoline systems

**Instructor Narration:**
> "Tomorrow we cross to the other side — diesel. Diesel engines don't use spark plugs. They ignite fuel purely by compression heat. The pressures are even higher than GDI — common-rail diesel systems run at 1,800 to 2,500 bar. We'll cover common-rail injection, glow plugs for cold starting, the diesel particulate filter, and SCR systems with AdBlue. If you thought 200 bar was high, wait until you see what diesel does. Wear your workshop gear — we'll be looking at diesel components up close. See you tomorrow."

**PPT Content:**
```
DAY 13 PREVIEW: DIESEL FUEL DELIVERY

• Compression ignition — no spark plugs
• Common-rail direct injection: 1,800 - 2,500 bar
• Glow plugs — cold start assist
• Diesel Particulate Filter (DPF) — soot management
• SCR / AdBlue — NOx reduction
• Turbocharging — why nearly all diesels are turbocharged

From gasoline's 200 bar to diesel's 2,500 bar
— the pressure game changes completely.

Wear your workshop gear. See you tomorrow.
```

---

## Assessment Checkpoint

**Formative (not graded):**
- Station B worksheet: Coil resistance readings within specification tolerance (pass/fail)
- Station C worksheet: Correctly identify at least 6 of 8 spark plug conditions
- Quick knowledge check: Answer 4 of 5 questions correctly
- Verbal spot-checks during station rotation: "What is the MAF sensing principle?" "Why does GDI cause intake valve carbon buildup?"

---

## Key Takeaways

1. MPFI sprays fuel into the intake port at low pressure (3-5 bar); GDI sprays directly into the combustion chamber at high pressure (100-200+ bar) — both have trade-offs
2. COP ignition uses one coil per cylinder; the ECU controls dwell time and spark timing for optimal combustion
3. The EVAP system is an emissions system — check the fuel cap before going deep on EVAP codes
4. MAF measures air mass directly (hot-wire principle); MAP measures manifold pressure (piezoresistive) — both help the ECU calculate fuel delivery
5. Spark plug condition is a diagnostic window into combustion health — learn to read them

---

## Preparation for Day 13

**Instructor prep:**
- Prepare diesel common-rail system display or cutaway model
- Source diesel injector cutaway or cross-section diagram
- Prepare glow plug samples (new and used/failed)
- Have DPF cutaway or diagram available
- Print diesel vs gasoline comparison worksheet
- Ensure diesel bench engine (if available) is serviceable

**Learner prep:**
- Review Day 12 notes on fuel injection pressure and ignition
- Consider: how would you ignite fuel without a spark plug?
- Bring workshop gear — Day 13 includes diesel component handling
