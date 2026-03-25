---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 4
week_title: "Keep It Alive — Lubrication, Cooling, Exhaust & Forced Induction"
day_number: 19
session_title: "Turbocharger & Intercooler — Exhaust Energy to Intake Boost"
duration_minutes: 180
theory_practice: "45:55"
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 19: Turbocharger & Intercooler — Exhaust Energy to Intake Boost
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (80 min theory + 100 min practical)
**Approach:** Energy Recovery Narrative — Follow the Energy from Exhaust to Intake
**PPT Target:** 26-28 slides
**Week:** 4 of 8 — "Keep It Alive — Lubrication, Cooling, Exhaust & Forced Induction"

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Explain how a turbocharger converts exhaust energy into intake boost pressure
- Identify the turbine side, compressor side, centre bearing housing, and wastegate on a physical turbocharger
- Describe how a wastegate regulates boost pressure (internal vs external, mechanical vs electronic)
- Explain how Variable Geometry Turbo (VGT/VNT) vanes adjust exhaust flow and the common failure of stuck vanes
- Differentiate between air-to-air and air-to-water intercoolers and explain their purpose
- Identify the boost pressure sensor (MAP) and exhaust gas temperature (EGT) sensor and their roles in turbo monitoring
- Explain turbo lag and why it occurs
- Perform a boost leak diagnosis using a smoke tester or boost pressure gauge
- Check turbo shaft play (radial and axial) and assess turbo health
- Link the turbocharger into the complete air path from Week 3: air filter, turbo compressor, intercooler, throttle body, intake manifold

**Connection to Day 18:** Yesterday covered the exhaust system — catalytic converters, DPF, mufflers, sensors. Today the turbocharger sits at the junction where exhaust energy is recovered before it exits the system. The turbine wheel lives in the exhaust stream; the compressor wheel feeds the intake. One device, two worlds.

---

## Connection to Prior Knowledge

Build from:
- **Day 11 (Air + Fuel = Combustion):** Learners know the naturally aspirated air path — air filter to intake manifold. Today we insert the turbocharger and intercooler into that path.
- **Day 13 (Diesel Fuel Delivery & Intake):** Diesel engines almost universally use turbocharging. Learners saw boost pressure referenced during diesel fuel system theory.
- **Day 18 (Exhaust Systems):** Learners know exhaust gas flow from manifold to tailpipe. The turbo turbine sits right after the exhaust manifold, before the catalytic converter.
- **Day 9 (Multimeter Mastery):** Electrical testing skills for boost pressure sensor and EGT sensor diagnosis.

**Bridge:** "Yesterday you traced exhaust gas from the engine all the way out the tailpipe. But what if I told you there's a device that intercepts that hot, fast-moving exhaust gas and uses its energy to force more air into the engine? That device is the turbocharger — and it's one of the most elegant engineering solutions in the entire car."

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: Recovering Wasted Energy** (Slides 1-3, ~10 minutes)

**Narrative Voice:** Curious, building intrigue. Frame the turbocharger as an ingenious energy recovery device.

---

#### Slide 1: Title & Day Connection
**Visual:** Split image — left side shows glowing red exhaust manifold with gas rushing out; right side shows a cutaway turbocharger with arrows showing exhaust gas spinning the turbine and compressed air leaving the compressor side. A subtle visual line connects Day 18's exhaust to Day 19's turbo.

**Instructor Narration:**
> "Yesterday we followed exhaust gas from the combustion chamber to the tailpipe. We talked about how exhaust carries heat energy, chemical energy, and kinetic energy — and most of it just gets dumped into the atmosphere. What a waste.
>
> What if you could capture some of that energy and put it back to work? That's exactly what a turbocharger does. It sits right at the junction of the exhaust system and the intake system — one foot in each world. Today, we're going to take it apart, understand every piece, and learn how to diagnose it when it goes wrong."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 4: Keep It Alive
Day 19: Turbocharger & Intercooler

Yesterday: Exhaust gas exits the engine — wasted energy
Today: The turbocharger captures that energy and forces more air in

One device. Two systems. Exhaust meets intake.
```

---

#### Slide 2: The Problem — Why Naturally Aspirated Isn't Enough
**Visual:** Diagram comparing a naturally aspirated engine (air passively entering through intake vacuum) vs a turbocharged engine (compressed air being forced in). Include a bar chart showing power output difference — same displacement engine, NA vs turbo.

**Instructor Narration:**
> "A naturally aspirated engine — that's what we covered in Week 3 — relies on the piston moving down to create a vacuum that sucks air in. But that vacuum is weak. At best, you're getting about 1 bar of atmospheric pressure into the cylinder.
>
> Now think about combustion: more air means you can burn more fuel, which means more power. So how do you get more air in? You force it. You compress the intake air above atmospheric pressure. A 1.5-litre turbocharged engine can breathe like a 2.5-litre naturally aspirated engine. Same size, more power, better fuel economy at cruise. That's why nearly every new car sold today — petrol or diesel — has a turbocharger."

**PPT Content:**
```
THE PROBLEM: ATMOSPHERIC PRESSURE IS THE LIMIT

Naturally Aspirated (NA):
— Piston creates vacuum, air flows in passively
— Maximum ~1.0 bar (atmospheric pressure)
— Power limited by engine displacement

Turbocharged:
— Compressor forces air in above atmospheric pressure
— Typical boost: 0.5–2.5 bar above atmospheric
— Same displacement = significantly more power

Example:
1.5L Turbo (150 kW) vs 2.5L NA (130 kW)
Smaller engine, MORE power, BETTER fuel economy at cruise
```

---

#### Slide 3: Today's Plan
**Visual:** Horizontal timeline of the session — four blocks: Theory (turbo principles, wastegate, VGT, intercooler), then Practical (examine turbo, shaft play check, intercooler/piping inspection, boost leak test, scan tool data).

**Instructor Narration:**
> "Here's how today works. First, theory — we'll cover the turbocharger in detail: turbine side, compressor side, bearing housing, wastegate, variable geometry turbos, and intercoolers. Then we move to the workshop for hands-on work. You'll examine a real turbocharger, check shaft play, inspect charge piping, perform a boost leak test with a smoke tester, and read live boost and EGT data on the scan tool.
>
> By the end of today, you'll understand the complete boosted air path and know how to find a leak anywhere in the system."

**PPT Content:**
```
TODAY'S PLAN (180 minutes)

THEORY (80 min):
— Turbocharger principles: turbine, compressor, bearing housing
— Wastegate: internal vs external, mechanical vs electronic
— Variable Geometry Turbo (VGT/VNT)
— Intercooler types: air-to-air vs air-to-water
— Boost control sensors: MAP sensor, EGT sensor
— Common turbo failures and symptoms

PRACTICAL (100 min):
1. Examine a turbocharger — identify all components
2. Check turbo shaft play (radial and axial)
3. Inspect intercooler and charge piping
4. Boost leak test (smoke tester / pressure gauge)
5. Read boost pressure & EGT data on scan tool
```

---

### **DEVELOPMENT: Turbo Principles, Boost Control & Intercooling** (Slides 4-16, ~55 minutes)

**Narrative Voice:** Technical but visual. Always trace the energy path. Use the exhaust-to-intake narrative as a constant thread.

---

#### Slide 4: The Turbocharger — Big Picture
**Visual:** Cutaway turbocharger with the three main sections clearly colour-coded — red for turbine housing (exhaust side), blue for compressor housing (intake side), grey/silver for centre bearing housing. Arrows show exhaust gas entering turbine, spinning the shaft, and compressed air exiting the compressor. Label the shaft connecting both wheels.

**Instructor Narration:**
> "Here it is — the turbocharger. Three sections, one shaft. On the left — the turbine housing. This sits bolted directly to the exhaust manifold. Hot exhaust gas — 800 to 1000 degrees Celsius — rushes in, hits the turbine wheel, and spins it. That wheel is connected by a shaft to the compressor wheel on the other side. The compressor wheel sits in the intake path. As it spins, it draws in ambient air and compresses it — pushing it toward the engine at higher than atmospheric pressure.
>
> Between the two is the centre bearing housing. This contains the bearings that support the shaft, and it's where oil and coolant flow through to keep everything lubricated and cool. That shaft can spin at 150,000 RPM or more. Let that sink in — 150,000 revolutions per minute. That's 2,500 revolutions per second."

**PPT Content:**
```
THE TURBOCHARGER — THREE SECTIONS, ONE SHAFT

TURBINE SIDE (EXHAUST):
— Turbine housing bolted to exhaust manifold
— Turbine wheel spun by exhaust gas energy
— Operating temperature: 800–1050 degC
— Material: Inconel (nickel-based superalloy)

COMPRESSOR SIDE (INTAKE):
— Compressor housing connected to air intake path
— Compressor wheel draws in and compresses ambient air
— Outputs pressurised air (boost) above atmospheric
— Material: Aluminium alloy (lighter, cooler side)

CENTRE BEARING HOUSING:
— Journal bearings support the shaft
— Oil-fed (engine oil supply and return lines)
— Often water-cooled (coolant lines)
— Shaft speed: 80,000–250,000 RPM
```

---

#### Slide 5: The Exhaust-Driven Turbine
**Visual:** Close-up of the turbine side — show exhaust gas entering the scroll (volute), hitting the turbine wheel blades at an angle, and exiting through the centre toward the catalytic converter. Include a temperature gradient overlay (hottest at entry, cooler at exit).

**Instructor Narration:**
> "Let's zoom into the turbine side. Exhaust gas enters the turbine housing through a scroll — that snail-shell shape. The scroll accelerates the gas and directs it onto the turbine blades at the optimal angle. The energy transfer is almost entirely kinetic — the gas hits the blades, pushes them, and the wheel spins. After giving up its energy, the exhaust exits out the centre and continues downstream to the catalytic converter and the rest of the exhaust system we covered yesterday.
>
> The turbine wheel is made from Inconel — a nickel-based superalloy that can survive sustained temperatures above 1000 degrees. This is aerospace-grade material in your car. It's also incredibly precisely balanced. Even a tiny imbalance at 150,000 RPM would tear itself apart."

**PPT Content:**
```
TURBINE SIDE — DRIVEN BY EXHAUST

Gas flow path:
Exhaust manifold → Turbine scroll (volute) → Turbine wheel → Outlet to catalytic converter

How it works:
— Scroll shape accelerates and directs exhaust gas
— Gas strikes turbine blades at optimal angle
— Kinetic energy transfers to wheel rotation
— Spent gas exits to downstream exhaust

Key facts:
— Exhaust gas temperature at entry: 800–1050 degC
— Turbine wheel material: Inconel (nickel superalloy)
— Wheel must be precision-balanced (< 0.01g tolerance)
— Turbine converts ~30% of exhaust energy to shaft work
```

---

#### Slide 6: The Compressor — Forcing Air In
**Visual:** Close-up of the compressor side — show ambient air entering axially (from the centre), hitting the spinning compressor wheel blades, being flung outward into the diffuser, and exiting the scroll at higher pressure. Include a pressure gradient overlay (low pressure at entry, high pressure at exit).

**Instructor Narration:**
> "On the other end of the shaft, the compressor wheel is doing the opposite job. Ambient air enters from the front — axially, right through the centre. The spinning compressor blades grab that air and fling it outward — centrifugally. As the air moves outward into the diffuser and the compressor scroll, it slows down. And when air slows down, its pressure increases. That's the boost pressure you hear about.
>
> The compressor wheel is aluminium — lighter than the turbine wheel because it's working in cooler air. But here's a side effect: compressing air heats it up. Air entering at 25 degrees can leave the compressor at 150 degrees or more. Hot air is less dense — which means fewer oxygen molecules per litre. That's a problem we'll solve with the intercooler in a few slides."

**PPT Content:**
```
COMPRESSOR SIDE — FORCING AIR INTO THE ENGINE

Air flow path:
Air filter → Compressor inlet (axial) → Compressor wheel → Diffuser → Charge pipe to intercooler

How it works:
— Air enters axially (through the centre)
— Spinning blades fling air outward (centrifugal force)
— Diffuser slows the air and converts velocity to pressure
— Compressed air exits through the scroll at higher pressure

Key facts:
— Compressor wheel material: Aluminium alloy
— Outlet air temperature: 100–200 degC (depending on boost)
— Boost pressure: typically 0.5–2.5 bar above atmospheric
— Hot compressed air is less dense — needs cooling (intercooler)
```

---

#### Slide 7: The Centre Bearing Housing — Keeping It Alive
**Visual:** Cross-section of the centre bearing housing showing the shaft, journal bearings (floating type), oil inlet and outlet passages, and coolant jacket. Annotate oil film thickness and flow direction. Show the thrust bearing controlling axial movement.

**Instructor Narration:**
> "This is arguably the most critical part of the turbocharger for longevity — the centre bearing housing. The shaft spins at up to 250,000 RPM in some applications. What keeps it alive? A thin film of oil. Most turbochargers use floating journal bearings — the shaft rides on a film of pressurised engine oil just thousandths of a millimetre thick. There's also a thrust bearing that controls axial movement — preventing the shaft from sliding back and forth.
>
> Oil enters from the engine's pressurised oil gallery — the same oil that lubricates your crankshaft and camshaft. It flows through the bearing housing, absorbs heat, and drains back to the sump by gravity through a return line. Many modern turbos also have coolant passages in the bearing housing. After you shut the engine off, coolant can thermosiphon through the housing to prevent heat soak — that's when residual heat cooks the oil into carbon deposits.
>
> This is why oil quality and oil change intervals matter so much on turbocharged engines. Starve this bearing of oil for even a few seconds, and you'll hear the turbo screaming — and then you'll hear silence as it destroys itself."

**PPT Content:**
```
CENTRE BEARING HOUSING — OIL-COOLED, OFTEN WATER-COOLED

Bearings:
— Floating journal bearings (shaft rides on oil film)
— Oil film thickness: ~0.02–0.05 mm
— Thrust bearing controls axial shaft movement

Oil supply:
— Fed from engine oil gallery (pressurised)
— Oil lubricates AND cools the bearings
— Returns to sump via gravity drain line
— Oil return line must be unrestricted (no kinks, no blockage)

Water cooling (most modern turbos):
— Coolant jacket surrounds bearing housing
— Prevents heat soak after engine shutdown
— Thermosiphon effect continues cooling with engine off

CRITICAL: Oil starvation = bearing failure = destroyed turbo
```

---

#### Slide 8: The Wastegate — Controlling Boost Pressure
**Visual:** Diagram showing an internal wastegate — a flap valve inside the turbine housing that bypasses exhaust gas around the turbine wheel. Show it in closed position (all gas hits turbine = max boost building) and open position (some gas bypasses turbine = boost limited). Include the actuator arm and pressure line.

**Instructor Narration:**
> "If the turbo just kept spinning faster and faster with no limit, it would over-boost the engine — too much pressure in the cylinders, leading to detonation, blown head gaskets, or worse. You need a way to limit boost pressure. That's the wastegate.
>
> The most common type is an internal wastegate — a small flap valve built right into the turbine housing. When boost pressure reaches the target, the wastegate opens and diverts some exhaust gas around the turbine wheel. Less gas hitting the turbine means it stops accelerating and boost pressure stabilises.
>
> The simplest wastegates are mechanically actuated — a spring-loaded diaphragm connected to a boost pressure line. When boost pressure overcomes the spring, the valve opens. More sophisticated systems use an electronic solenoid that the ECU controls — this allows the ECU to vary target boost based on load, temperature, altitude, and other conditions."

**PPT Content:**
```
WASTEGATE — THE BOOST PRESSURE REGULATOR

Purpose: Prevent over-boost by bypassing exhaust around the turbine

INTERNAL WASTEGATE (most common):
— Flap valve inside the turbine housing
— Opens to divert exhaust gas past the turbine wheel
— Closed: all gas hits turbine → boost builds
— Open: gas bypasses turbine → boost stabilises

EXTERNAL WASTEGATE (high-performance):
— Separate housing mounted on exhaust manifold
— Diverts gas before it reaches the turbo
— Larger flow capacity, more precise control

Actuation:
— Mechanical: Spring-loaded diaphragm + boost pressure line
  (Opens at a fixed boost level set by spring rate)
— Electronic: ECU-controlled solenoid modulates actuator
  (Variable boost targets — adapts to conditions)
```

---

#### Slide 9: Electronic Boost Control — The ECU in Command
**Visual:** System diagram showing the boost control loop — boost pressure sensor (MAP) sends data to ECU, ECU compares to target boost map, ECU drives electronic wastegate solenoid (or VGT actuator), wastegate position changes, boost pressure adjusts. Closed-loop feedback arrows.

**Instructor Narration:**
> "In a modern engine, the ECU is in total command of boost pressure. Here's the control loop. The MAP sensor — Manifold Absolute Pressure sensor — measures actual boost pressure in the intake manifold and sends that data to the ECU. The ECU compares actual boost to its target boost map — which varies based on throttle position, engine RPM, intake air temperature, coolant temperature, altitude, and even fuel quality.
>
> If actual boost is below target, the ECU keeps the wastegate closed — letting the turbo spool up. If actual boost reaches target, the ECU starts opening the wastegate via a pulse-width-modulated solenoid. This gives incredibly precise control — the ECU can adjust boost pressure dozens of times per second.
>
> When we look at scan tool data later, you'll see the target boost and actual boost as live parameters. They should track closely. If they diverge — actual boost too low or too high — that's a diagnostic clue."

**PPT Content:**
```
ELECTRONIC BOOST CONTROL — ECU-MANAGED

Control loop:
1. MAP sensor reads actual intake manifold pressure
2. ECU compares actual vs target boost (from calibration map)
3. ECU adjusts wastegate position via solenoid
4. Boost pressure changes → MAP sensor reads new value
5. Repeat — closed-loop control, many times per second

Target boost varies with:
— Throttle position (driver demand)
— Engine RPM
— Intake air temperature
— Coolant temperature
— Barometric pressure (altitude compensation)
— Fuel quality (knock detection feedback)

Diagnostic clue:
— Actual boost matches target → system healthy
— Actual boost below target → leak, stuck wastegate, turbo wear
— Actual boost above target → stuck wastegate (closed), solenoid fault
```

---

#### Slide 10: Variable Geometry Turbo (VGT / VNT)
**Visual:** Cutaway of a VGT turbocharger showing the movable guide vanes around the turbine wheel. Two positions illustrated side by side — vanes closed (narrow gap, high velocity, low-RPM response) and vanes open (wide gap, high-RPM flow capacity). Show the unison ring and electronic actuator.

**Instructor Narration:**
> "The wastegate is one way to control boost. But there's a more elegant solution — the Variable Geometry Turbocharger, or VGT. You'll also hear it called VNT — Variable Nozzle Turbine. Same thing, different brand name.
>
> Instead of bypassing exhaust gas, VGT adjusts how the gas hits the turbine wheel. A ring of movable guide vanes surrounds the turbine wheel. At low RPM — when exhaust flow is weak — the vanes close to a narrow angle. This accelerates the small amount of exhaust gas to a higher velocity before it hits the turbine blades. Result: the turbo spools up faster at low RPM. Less lag.
>
> At high RPM — when exhaust flow is strong — the vanes open wide. This prevents the turbo from over-speeding and allows the large volume of gas to flow through without excessive back-pressure.
>
> VGT is almost universal on diesel engines because diesel exhaust is cooler and the soot levels are manageable with modern designs. On petrol engines, the extreme exhaust temperatures make VGT more challenging — but it's appearing on more and more direct-injection petrol turbos."

**PPT Content:**
```
VARIABLE GEOMETRY TURBO (VGT / VNT)

Instead of bypassing gas (wastegate), VGT changes HOW gas hits the turbine

Movable guide vanes around the turbine wheel:

VANES CLOSED (narrow angle):
— Gas accelerated to high velocity
— Small gas volume spins turbine effectively
— Used at LOW engine RPM → reduces turbo lag
— Like putting your thumb over a garden hose nozzle

VANES OPEN (wide angle):
— Gas flows freely at lower velocity
— Handles large gas volumes at high RPM
— Prevents over-boost and excessive back-pressure

Actuation:
— Unison ring moves all vanes simultaneously
— Electronic actuator controlled by ECU
— Position feedback sensor for closed-loop control

Common on: Almost all modern diesel engines
Growing on: Direct-injection petrol engines
```

---

#### Slide 11: VGT — Common Faults: Stuck Vanes
**Visual:** Photo of a VGT mechanism with carbon-fouled vanes — show the black soot deposits binding the vanes in position. Include a second photo of a clean VGT mechanism for contrast. Diagram of the symptom chain: stuck vanes, loss of boost control, limp mode, MIL illumination.

**Instructor Narration:**
> "Here's the most common VGT failure you'll encounter — stuck vanes. On diesel engines, exhaust gas contains soot. Over time, that soot builds up on the vane pivots and the unison ring. Eventually, the vanes stick — either partially closed or partially open.
>
> Stuck closed: excessive boost at high RPM, possible over-boost fault code, engine enters limp mode.
>
> Stuck open: poor boost at low RPM, sluggish acceleration, under-boost fault code, black smoke under load because the ECU adds fuel expecting boost that never arrives.
>
> Stuck mid-position: poor performance across the range, hunting or oscillating boost pressure.
>
> Sometimes you can free stuck vanes with a careful cleaning — removing the turbo, soaking the vane mechanism in solvent, working each vane by hand. Other times, the pivot pins are corroded beyond recovery and the turbo needs replacement. This is one of the most common reasons diesel turbos get replaced — not bearing failure, but carbon-locked vanes."

**PPT Content:**
```
VGT COMMON FAULT: STUCK VANES (CARBON BUILD-UP)

Cause:
— Diesel exhaust soot deposits on vane pivots and unison ring
— Gradual build-up over 80,000–150,000 km
— Worsened by: short trips, low-quality fuel, EGR issues, infrequent oil changes

Symptoms by stuck position:
STUCK CLOSED → Over-boost at high RPM, limp mode, DTC for boost deviation
STUCK OPEN → Under-boost, sluggish acceleration, black smoke, DTC
STUCK MID → Inconsistent boost, hunting/surging, poor overall performance

Diagnosis:
— Scan tool: Read VGT position commanded vs actual
— Actuator test: Command vanes open/closed, listen and feel for movement
— Visual: Remove turbo, inspect vane movement by hand

Repair options:
— Clean and free vanes (if pivot pins are not corroded)
— Replace VGT actuator (if mechanism is free but actuator failed)
— Replace turbocharger (if vanes/pivots are seized)
```

---

#### Slide 12: The Intercooler — Cooling the Boost
**Visual:** Diagram showing the complete boosted air path: compressor outlet (hot compressed air, shown in red/orange) flowing through charge pipe to intercooler (colour transition from hot to cool), then to throttle body and intake manifold (shown in blue). Include a temperature callout: air enters intercooler at ~150 degrees C, exits at ~40-50 degrees C.

**Instructor Narration:**
> "Remember what I said about compressing air — it heats up. Air leaving the compressor can be 150 degrees or hotter. Hot air is less dense, which means fewer oxygen molecules in each gulp the engine takes. That defeats the purpose of boosting in the first place.
>
> The solution is the intercooler — a heat exchanger that sits between the turbo compressor outlet and the intake manifold. It cools the compressed air before it enters the engine. Cooler air is denser, which means more oxygen per unit volume, which means more complete combustion, more power, and lower risk of detonation.
>
> Think of it like this: the turbo compresses the air to get more volume in, but the intercooler cools it to get more mass in. Volume alone doesn't make power — mass of oxygen does."

**PPT Content:**
```
THE INTERCOOLER — COOLING THE COMPRESSED AIR

Why it's needed:
— Compression heats the air (thermodynamics)
— Compressor outlet: 100–200 degC
— Hot air is LESS DENSE = fewer O2 molecules
— Cooler air is MORE DENSE = more O2 = more power

Purpose:
— Cool compressed air before it enters the engine
— Increase air density (more oxygen per litre)
— Reduce risk of detonation (knock)
— Improve combustion efficiency

Typical temperature drop:
— Inlet: ~150 degC
— Outlet: ~40–50 degC
— Efficiency: 70–80% temperature reduction

Boosted air path:
Air filter → Compressor → Charge pipe → INTERCOOLER → Throttle body → Intake manifold
```

---

#### Slide 13: Intercooler Types — Air-to-Air vs Air-to-Water
**Visual:** Side-by-side comparison. Left: air-to-air intercooler — large front-mounted radiator-style core with fins, charge pipes running from turbo to intercooler and from intercooler to intake. Right: air-to-water intercooler — compact heat exchanger mounted directly on the intake manifold with a separate coolant circuit (low-temperature circuit with its own pump and radiator).

**Instructor Narration:**
> "There are two main intercooler designs. The most common is air-to-air. It works just like a radiator — hot compressed air flows through tubes inside the intercooler core, and ambient air passing over the fins carries the heat away. You'll usually find these mounted at the front of the vehicle behind the bumper, or sometimes on top of the engine.
>
> The second type is air-to-water. Instead of ambient air cooling the charge air directly, a liquid coolant circuit does the job. The intercooler core is much more compact — sometimes integrated right into the intake manifold. A separate low-temperature coolant circuit with its own pump and small radiator carries the heat away. Air-to-water intercoolers respond faster and work better in stop-and-go traffic where there's limited airflow across a front-mounted unit.
>
> You'll see air-to-air on most standard vehicles and air-to-water on premium turbocharged engines, especially direct-injection petrols that are sensitive to intake temperature."

**PPT Content:**
```
INTERCOOLER TYPES

AIR-TO-AIR (most common):
— Large core with fins, similar to a radiator
— Ambient air flowing over the core removes heat
— Usually front-mounted (behind bumper/grille)
— Simple: no coolant circuit, no pump
— Limitation: depends on vehicle speed for airflow
— Used on: most turbocharged vehicles

AIR-TO-WATER (compact, premium):
— Compact core cooled by liquid coolant
— Separate low-temperature coolant circuit
— Own electric pump and small radiator
— Can be integrated into intake manifold
— Faster response, works better in traffic
— More complex: additional pump, hoses, radiator
— Used on: BMW, Audi, Mercedes turbo petrols, some Ford EcoBoost

Both use charge pipes/couplers to connect:
Turbo compressor outlet → Charge pipe → Intercooler → Charge pipe → Throttle body
```

---

#### Slide 14: Charge Piping and Couplers
**Visual:** Photo of the complete charge piping system under a bonnet — rigid aluminium pipes, flexible silicone couplers with clamps, and the intercooler connections. Annotate common leak points: coupler joints, intercooler end tanks, cracked pipes, and blow-off valve connections.

**Instructor Narration:**
> "The charge piping is the plumbing that carries pressurised air from the turbo compressor to the intercooler and from the intercooler to the intake manifold. It's a mix of rigid aluminium or plastic pipes and flexible silicone or rubber couplers held on with clamps.
>
> This system is under positive pressure — unlike the vacuum side of a naturally aspirated intake. That means any gap, crack, loose clamp, or perished rubber coupling will leak pressurised air. And a boost leak is one of the most common causes of low power on turbocharged engines.
>
> Common leak points: coupler connections at the turbo and intercooler, intercooler end tanks that crack from vibration, plastic charge pipes that become brittle with heat and age, and the blow-off valve or recirculating valve if fitted. We'll test for these leaks in the practical session."

**PPT Content:**
```
CHARGE PIPING AND COUPLERS

Components:
— Rigid pipes (aluminium or reinforced plastic)
— Flexible couplers (silicone or rubber, T-bolt clamps)
— Intercooler connections (push-fit or clamped)
— Blow-off valve / diverter valve (releases excess pressure)

System is under POSITIVE PRESSURE (0.5–2.5 bar)
— Any gap = boost leak = lost power

Common leak points:
1. Coupler joints at turbo compressor outlet
2. Coupler joints at intercooler inlet/outlet
3. Intercooler end tanks (cracked from vibration)
4. Plastic charge pipes (brittle with age/heat)
5. Blow-off valve / diverter valve seal
6. Intake manifold gasket (post-throttle)

Symptom of boost leak:
— Loss of power under load
— Hissing or whistling sound under boost
— Under-boost DTC on scan tool
— Black smoke (diesel — ECU adds fuel expecting boost)
```

---

#### Slide 15: Boost Pressure Sensor (MAP) and EGT Sensor
**Visual:** Left: MAP sensor mounted on the intake manifold with its electrical connector and location highlighted. Right: EGT sensor (thermocouple type) screwed into the exhaust manifold or turbo inlet pipe. Include a scan tool screenshot showing live MAP and EGT data.

**Instructor Narration:**
> "Two critical sensors monitor the turbo system. The first is the MAP sensor — Manifold Absolute Pressure. This sits on the intake manifold and measures the actual air pressure inside it. Before boost builds, it reads atmospheric or slightly below. Under boost, it reads above atmospheric. This is the ECU's primary feedback for the boost control loop we discussed earlier.
>
> The second is the EGT sensor — Exhaust Gas Temperature. This thermocouple is mounted in the exhaust stream, usually pre-turbo. It tells the ECU how hot the exhaust gas is entering the turbine. If EGT gets too high — above the turbine's material limit — the ECU will reduce fuelling, retard timing, or open the wastegate to protect the turbocharger. On diesel engines with DPF, the EGT sensor also plays a role in regeneration management.
>
> Both sensors are critical for turbo health monitoring. A faulty MAP sensor means the ECU can't control boost properly. A faulty EGT sensor means the ECU can't protect the turbo from overheating."

**PPT Content:**
```
TURBO MONITORING SENSORS

MAP SENSOR (Manifold Absolute Pressure):
— Location: Intake manifold (post-intercooler, post-throttle)
— Measures: Actual intake pressure (absolute)
— Range: ~0.2 bar (decel vacuum) to ~3.5 bar (full boost)
— Signal: Analogue voltage (0.5–4.5V) or digital
— Role: Primary feedback for boost control loop
— Fault: Erratic boost, limp mode, over/under-boost DTCs

EGT SENSOR (Exhaust Gas Temperature):
— Location: Exhaust manifold or turbo inlet pipe (pre-turbo)
— Also: Post-turbo, pre-DPF, post-DPF on diesel
— Measures: Exhaust gas temperature (degC)
— Range: 100–1050 degC
— Signal: Thermocouple voltage (mV range) or NTC resistance
— Role: Turbo protection, DPF regeneration management
— Fault: Turbo overheating risk, failed DPF regen, DTC
```

---

#### Slide 16: Turbo Lag — Why There's a Delay
**Visual:** Graph showing engine RPM on x-axis and boost pressure on y-axis. Show the naturally aspirated torque curve flat, then the turbocharged curve rising sharply but with a visible gap at low RPM before boost builds — label this gap as "turbo lag." Annotate the factors that contribute: turbine and compressor wheel inertia, exhaust gas volume at low RPM.

**Instructor Narration:**
> "You've probably heard the term 'turbo lag.' It's the delay between pressing the accelerator and feeling the boost kick in. Why does it happen?
>
> At low RPM, the engine produces a small volume of exhaust gas. That small volume doesn't have enough energy to spin the turbine wheel quickly. The turbine and compressor wheels have mass — they have inertia. It takes time for the exhaust energy to accelerate them from idle speed to full boost speed. That time is the lag.
>
> Engineers fight lag in several ways: smaller turbos that spool faster, VGT vanes that close at low RPM to accelerate what little gas there is, twin-scroll turbo housings that separate exhaust pulses for better energy delivery, and electric turbo assist motors that spin the compressor at low RPM.
>
> For you as a technician, understanding lag matters because customers will sometimes complain about 'no power at low revs' — and that may be normal turbo lag, not a fault. But it could also be a stuck VGT, a boost leak, or a failing turbo. Knowing the difference is what makes you a good diagnostician."

**PPT Content:**
```
TURBO LAG — THE DELAY BEFORE BOOST

What it is:
— Delay between throttle application and boost pressure build-up
— Felt as hesitation or flat spot at low RPM

Why it happens:
— Low RPM = low exhaust gas volume and velocity
— Turbine and compressor wheels have rotational inertia (mass)
— Takes time for exhaust energy to accelerate the turbo assembly
— Typical lag: 0.5–2.0 seconds on older designs

How engineers reduce lag:
— Smaller turbo (spools faster, but limits top-end power)
— VGT (closes vanes to accelerate low-volume gas)
— Twin-scroll turbo (separates exhaust pulses for better energy)
— Electric turbo assist (e-compressor spins at low RPM)
— Twin-turbo / sequential turbo (small turbo for low RPM, large for high)

Technician note:
Some lag is NORMAL — don't diagnose normal behaviour as a fault
Compare to manufacturer specifications for boost build time
```

---

### **PRACTICAL: Turbo Examination, Shaft Play, Leak Testing & Scan Tool** (Slides 17-24, ~85 minutes)

**Narrative Voice:** Workshop guide. Hands-on, step-by-step, safety-aware.

---

#### Slide 17: Practical Overview & Safety
**Visual:** Photo of a turbocharger removed from a vehicle on a clean workbench, alongside safety equipment — heat-resistant gloves, safety glasses, and a fire extinguisher (turbo components retain extreme heat).

**Instructor Narration:**
> "Time to get hands-on. We have five activities today. First — examine a removed turbocharger and identify every component we've discussed. Second — check turbo shaft play. Third — inspect the intercooler and charge piping on a vehicle. Fourth — perform a boost leak test. Fifth — read live boost and EGT data on the scan tool.
>
> Safety reminder: if a turbocharger has been recently removed from a running engine, it retains extreme heat for a long time. Never touch a turbo that hasn't fully cooled. Use heat-resistant gloves if there's any doubt. Also, when performing a boost leak test with a smoke tester, you're pressurising the intake system — never exceed the manufacturer's specified test pressure, and keep clear of hose connections that could blow off under pressure."

**PPT Content:**
```
PRACTICAL SESSION — 5 ACTIVITIES (85 min)

1. Examine a turbocharger (15 min)
   — Identify turbine, compressor, bearing housing, wastegate/VGT

2. Check turbo shaft play (15 min)
   — Radial and axial play assessment

3. Inspect intercooler and charge piping (15 min)
   — Visual inspection for cracks, loose clamps, oil residue

4. Boost leak test (25 min)
   — Smoke tester or boost pressure gauge method

5. Scan tool — boost and EGT data (15 min)
   — Live data: actual vs target boost, EGT readings

SAFETY:
— Turbo components retain extreme heat — let them cool fully
— Boost leak test: do not exceed specified test pressure
— Safety glasses and gloves for all activities
```

---

#### Slide 18: Activity 1 — Examine a Turbocharger
**Visual:** Annotated photo of a turbocharger laid on a workbench — labels pointing to: turbine housing, turbine wheel, compressor housing, compressor wheel, centre bearing housing, oil inlet fitting, oil return flange, coolant inlet/outlet fittings, wastegate flap (or VGT actuator), wastegate actuator arm and linkage.

**Instructor Narration:**
> "I have a turbocharger here on the bench. Your first job is identification. Come around and I'll point out each component, then I want each of you to identify them independently.
>
> Here — the turbine housing. See how the scroll narrows toward the turbine wheel? That's the nozzle effect that accelerates the gas. Here's the turbine wheel — look at those curved blades. They're shaped to extract maximum energy from the gas flow.
>
> Opposite end — the compressor housing. Notice the inlet is a straight bore — air comes in axially. The compressor wheel has backward-curved blades designed to fling air outward.
>
> In the middle — the bearing housing. Here's the oil inlet — usually a banjo bolt on top. The oil return — a larger flange on the bottom for gravity drain. Coolant connections — smaller than the oil ports, often on the side.
>
> And here — the wastegate. On this unit it's internal. See this flap? When it opens, exhaust gas bypasses the turbine. The actuator arm connects to a diaphragm actuator — boost pressure pushes against the spring to open the flap. If this turbo had VGT instead, you'd see the actuator motor and linkage to the unison ring."

**PPT Content:**
```
ACTIVITY 1: EXAMINE A TURBOCHARGER (15 min)

Identify these components by sight and touch:

TURBINE SIDE:
[ ] Turbine housing (scroll shape)
[ ] Turbine wheel (Inconel, curved blades)
[ ] Exhaust inlet flange
[ ] Exhaust outlet

COMPRESSOR SIDE:
[ ] Compressor housing (scroll shape)
[ ] Compressor wheel (aluminium, backward-curved blades)
[ ] Air inlet bore
[ ] Compressed air outlet

CENTRE:
[ ] Bearing housing
[ ] Oil inlet (banjo bolt or fitting, top)
[ ] Oil return (large flange, bottom)
[ ] Coolant connections (if equipped)

BOOST CONTROL:
[ ] Wastegate flap (or VGT vane mechanism)
[ ] Actuator (mechanical diaphragm or electronic motor)
[ ] Actuator linkage / arm
```

---

#### Slide 19: Activity 2 — Check Turbo Shaft Play
**Visual:** Two diagrams showing shaft play measurement. Left: radial play — hand pushing compressor wheel up/down, showing gap between wheel tip and housing (acceptable: 0.03-0.08 mm). Right: axial play — hand pushing shaft in/out, showing fore-aft movement (acceptable: 0.02-0.05 mm). Photo of a dial indicator positioned to measure radial play on the compressor end.

**Instructor Narration:**
> "Turbo shaft play is the first check when diagnosing a turbo complaint. There are two directions: radial — side to side — and axial — in and out along the shaft axis.
>
> With the turbo accessible — either removed or with the intake pipe disconnected so you can reach the compressor wheel — gently push the compressor wheel up and down. That's radial play. New turbo: you'll feel almost nothing. A tiny bit of play is normal — the bearings are designed with clearance for the oil film. But if you can feel the wheel contacting the housing, or if movement is more than about a tenth of a millimetre, the bearings are worn.
>
> Next, push and pull the shaft along its axis. That's axial play. Again, very slight movement is normal. Excessive axial play means the thrust bearing is worn.
>
> If you have a dial indicator, you can measure precisely. But for a quick field assessment, the finger test tells you a lot. Scoring on the compressor wheel tips or the turbine housing bore confirms contact from excessive play."

**PPT Content:**
```
ACTIVITY 2: CHECK TURBO SHAFT PLAY (15 min)

ACCESS:
— Remove intake pipe at compressor inlet (or examine removed turbo)
— Reach in and grip the compressor wheel nut or blade tips gently

RADIAL PLAY (side-to-side):
— Push wheel up and down perpendicular to shaft axis
— Acceptable: 0.03–0.08 mm (barely perceptible by hand)
— Excessive: wheel tips contact housing (scraping = replacement needed)
— Dial gauge method: position indicator on wheel, rock shaft

AXIAL PLAY (in-and-out):
— Push and pull shaft along its axis
— Acceptable: 0.02–0.05 mm
— Excessive: clunking feel, thrust bearing worn

VISUAL INSPECTION:
— Scoring on compressor wheel blade tips → housing contact
— Oil residue in compressor housing → seal leak (often from excess play)
— Cracked or chipped blades → FOD or fatigue (replace turbo)

Result: PASS (minimal play, no scoring) or FAIL (excessive play, damage)
```

---

#### Slide 20: Activity 3 — Inspect Intercooler and Charge Piping
**Visual:** Photo of a front-mounted intercooler visible through the bumper grille, with charge pipes running to and from it. Annotate inspection points: intercooler fins (bent/blocked), end tanks (cracks), charge pipe connections (loose clamps, perished rubber), oil contamination inside pipes (indicates turbo seal leaking).

**Instructor Narration:**
> "With the vehicle on the lift or with the undertray removed, inspect the intercooler and all charge piping. Start at the turbo compressor outlet and trace every pipe all the way to the throttle body.
>
> What are you looking for? First — physical damage. Intercooler fins bent from road debris, end tanks cracked from vibration or impact, pipes cracked or split, couplers bulging or perished.
>
> Second — connection integrity. Every clamp should be tight. Every coupler should be fully seated. Squeeze each rubber section — it should be firm and flexible, not soft and spongy or hard and brittle.
>
> Third — oil contamination. If you disconnect a charge pipe and find the inside coated with oil, that's a sign of turbo compressor seal leakage. A small amount of oil mist is normal on high-mileage vehicles. A heavy coating indicates the turbo seals are failing — which often comes with excessive shaft play.
>
> Fourth — check the blow-off or recirculating valve if fitted. Make sure it moves freely and seals properly."

**PPT Content:**
```
ACTIVITY 3: INSPECT INTERCOOLER & CHARGE PIPING (15 min)

INSPECTION PATH: Trace from turbo compressor outlet to throttle body

INTERCOOLER:
[ ] Fins: bent, blocked with debris, corrosion
[ ] End tanks: cracks, stone damage, weeping
[ ] Mounting brackets: secure, not vibrating loose

CHARGE PIPES:
[ ] Rigid pipes: cracks, splits, heat damage
[ ] Flexible couplers: bulging, perished, soft, split
[ ] Clamps: tight, correct torque, not corroded

CONNECTIONS:
[ ] All joints fully seated and clamped
[ ] No audible hissing under boost (road test or pressure test)

OIL CONTAMINATION (inside pipes):
— Light oil mist film: often normal at high mileage
— Heavy oil coating: turbo compressor seal leaking
— Correlate with shaft play check from Activity 2

BLOW-OFF / DIVERTER VALVE:
[ ] Moves freely when actuated by hand
[ ] Seals properly (no boost leak when closed)
```

---

#### Slide 21: Activity 4 — Boost Leak Test: The Method
**Visual:** Diagram showing a boost leak test setup. Method A: smoke tester connected to the intake path (throttle body side sealed, smoke pumped in at regulated pressure — leaks visible as smoke escaping from joints). Method B: pressure gauge connected to intake, system pressurised with regulated air, gauge monitored for pressure drop.

**Instructor Narration:**
> "This is the definitive test for boost leaks. There are two methods.
>
> Method one — the smoke tester. Seal the turbo inlet and the throttle body. Connect the smoke tester to the charge system and pump in smoke at a regulated pressure — usually 1 to 1.5 bar. Watch for smoke escaping from any joint, crack, or damaged component. Where you see smoke, you've found your leak. It's visual, it's definitive, and it shows you the exact location.
>
> Method two — pressure test with a gauge. Same sealing setup, but instead of smoke, you pressurise the system with clean air and watch the gauge. If pressure drops, you have a leak. Then you use soapy water or your hand to find it. Less definitive than smoke but works in a pinch.
>
> The key is sealing the system properly. Block the turbo inlet (compressor entry) and the throttle body or intake manifold entry. Some technicians use purpose-made adapter plates. You're only testing the pressurised side — from compressor outlet through charge pipes, intercooler, and up to the throttle body."

**PPT Content:**
```
ACTIVITY 4: BOOST LEAK TEST (25 min)

SETUP (both methods):
— Seal turbo compressor INLET (block plate or plug)
— Seal intake manifold / throttle body entry
— You are testing: compressor outlet → charge pipes → intercooler → to throttle

METHOD A — SMOKE TEST (preferred):
1. Connect smoke tester to charge system
2. Set regulated pressure: 1.0–1.5 bar (check manufacturer spec)
3. Pump smoke into sealed system
4. Watch for smoke escaping at joints, cracks, seals
5. Smoke location = leak location

METHOD B — PRESSURE GAUGE:
1. Connect regulated air supply with gauge
2. Pressurise to 1.0–1.5 bar
3. Monitor gauge for pressure drop over 60 seconds
4. If pressure drops: spray soapy water on connections
5. Bubbles = leak location

COMMON LEAK SOURCES FOUND:
— Loose or cracked coupler at turbo outlet
— Cracked intercooler end tank
— Split charge pipe
— Faulty blow-off / diverter valve
— Intercooler core puncture (stone damage)
```

---

#### Slide 22: Activity 4 (Continued) — Interpreting Boost Leak Test Results
**Visual:** Decision tree / flowchart. Start: "Pressure holds?" — Yes: system sealed, no leak. No: "Where is the leak?" Branch into turbo outlet coupler, charge pipe, intercooler, diverter valve, intake manifold gasket. Each branch shows typical repair action.

**Instructor Narration:**
> "Once you've found the leak, the next step is determining the repair. If it's a loose clamp — tighten it and retest. If it's a perished silicone coupler — replace it. If it's a cracked intercooler — replacement, because intercooler repairs rarely hold under boost pressure.
>
> Here's a diagnostic tip: if the customer complains of low power but your boost leak test shows no leaks, the problem might be upstream of your test area. Check the turbo itself — shaft play, wastegate operation, VGT vane movement. Or it could be downstream — a leak in the intake manifold or a fault in the boost control solenoid. The boost leak test only covers the pressurised charge path from compressor to throttle body. Think systematically."

**PPT Content:**
```
INTERPRETING BOOST LEAK TEST RESULTS

PRESSURE HOLDS (no drop in 60 sec):
→ Charge system is sealed — leak is elsewhere
→ Check: turbo itself, wastegate, VGT, post-throttle intake, boost solenoid

PRESSURE DROPS — LEAK FOUND:

Location: Coupler at turbo outlet
→ Repair: Re-seat coupler, tighten/replace clamp

Location: Charge pipe crack
→ Repair: Replace pipe (do not tape or glue — it won't hold under boost)

Location: Intercooler end tank or core
→ Repair: Replace intercooler

Location: Blow-off / diverter valve
→ Repair: Replace valve or reseat/replace seal

Location: Intake manifold gasket
→ Repair: Replace gasket (this is post-throttle — separate test may be needed)

ALWAYS RETEST after repair to confirm the fix
```

---

#### Slide 23: Activity 5 — Scan Tool: Boost and EGT Data
**Visual:** Scan tool screenshot showing live data PIDs: "Boost Pressure Actual" (1.45 bar), "Boost Pressure Target" (1.50 bar), "MAP Sensor Voltage" (3.2V), "Turbo VGT Position Commanded" (45%), "Turbo VGT Position Actual" (44%), "EGT Bank 1 Sensor 1" (623 degC), "EGT Bank 1 Sensor 2" (412 degC). Highlight the comparison between actual and target values.

**Instructor Narration:**
> "Our final activity uses the scan tool to read live turbo data. Connect the scan tool, go to the engine live data menu, and look for these parameters.
>
> Boost pressure actual vs boost pressure target. These should track closely — within about 5% of each other under steady-state conditions. If actual is consistently below target, you've got a leak, a worn turbo, or a stuck wastegate/VGT issue. If actual is above target, the wastegate may be stuck closed or the boost control solenoid may be faulty.
>
> VGT position commanded vs actual — on vehicles with variable geometry turbos, you'll see these two values. They should match. If commanded is 30% but actual reads 5% or doesn't change, the vanes may be stuck.
>
> EGT readings — check pre-turbo temperature under load. Typical diesel values are 400 to 700 degrees Celsius. Petrol can be higher. Abnormally high EGT suggests a lean condition, retarded timing, or exhaust restriction. Abnormally low EGT can indicate a misfiring cylinder not contributing exhaust energy.
>
> Record these values. They're your baseline for comparison when a customer returns with a turbo complaint."

**PPT Content:**
```
ACTIVITY 5: SCAN TOOL — BOOST & EGT DATA (15 min)

Connect scan tool → Engine live data → Select turbo parameters

KEY PARAMETERS TO MONITOR:

Boost Pressure:
— Actual boost (bar or kPa) vs Target boost
— Should match within ~5% at steady state
— Deviation = diagnostic clue (leak, turbo wear, actuator fault)

VGT Position (diesel with VGT):
— Commanded position (%) vs Actual position (%)
— Should match — if not, vanes may be stuck
— Command a sweep test if available in bi-directional controls

EGT — Exhaust Gas Temperature:
— Pre-turbo (Bank 1 Sensor 1): 400–700 degC diesel, 600–950 degC petrol
— Post-turbo (Bank 1 Sensor 2): lower than pre-turbo
— Abnormally HIGH: lean condition, timing issue, exhaust restriction
— Abnormally LOW: misfire, injector fault

Record values as BASELINE for future comparison
```

---

#### Slide 24: Common Turbo Failures — Recognition Guide
**Visual:** Grid layout with 6 common turbo failures — each with a photo and brief description: (1) oil starvation — scored bearings, blue/gold heat discolouration on shaft, (2) bearing wear — excessive shaft play, oil in compressor housing, (3) compressor wheel damage — chipped/bent blades from foreign object, (4) wastegate failure — stuck open or stuck closed, (5) VGT stuck vanes — carbon-locked mechanism, (6) cracked turbine housing — thermal fatigue cracks.

**Instructor Narration:**
> "Let's consolidate the common turbo failures you'll see in the field.
>
> One — oil starvation. The number one turbo killer. Causes: blocked oil feed line, low oil level, wrong oil viscosity, extended oil change intervals. The bearing surfaces score and overheat. You'll see blue or gold heat discolouration on the shaft. The turbo gets noisy, then fails completely.
>
> Two — bearing wear. The natural end of life for a high-mileage turbo. Excessive radial and axial play. Oil leaks past the seals into the compressor or turbine housing. Smoke from the exhaust — blue/white.
>
> Three — compressor wheel damage. A foreign object — a piece of broken air filter, a bolt left in the intake, even a small stone — hits the compressor wheel at 150,000 RPM. Blades chip or bend, causing catastrophic imbalance. You'll hear a screaming or grinding noise.
>
> Four — wastegate failure. Stuck closed: over-boost, limp mode. Stuck open: no boost, sluggish performance. Actuator rod disconnected: no boost control at all.
>
> Five — VGT stuck vanes. Carbon build-up on diesel engines. We covered this in detail earlier.
>
> Six — cracked turbine housing. Thermal cycling over hundreds of thousands of kilometres can fatigue-crack the cast iron housing. Exhaust leak at the turbo, audible hissing under load."

**PPT Content:**
```
COMMON TURBO FAILURES — RECOGNITION GUIDE

1. OIL STARVATION (most common cause of failure)
   Cause: Blocked feed line, low oil, wrong viscosity, long oil changes
   Signs: Scored bearings, heat discolouration on shaft, noise
   Prevention: Correct oil, regular changes, prime oil system after install

2. BEARING WEAR (end-of-life)
   Cause: High mileage, accumulated wear
   Signs: Excessive shaft play, oil in compressor housing, blue exhaust smoke
   Action: Replace turbo, check oil supply/return

3. COMPRESSOR WHEEL DAMAGE (FOD — Foreign Object Damage)
   Cause: Debris entering intake (broken filter, loose bolt, stone)
   Signs: Chipped/bent blades, imbalance noise, catastrophic failure
   Prevention: Always check intake path is clear before starting engine

4. WASTEGATE FAILURE
   Signs: Over-boost (stuck closed) or no boost (stuck open)
   Check: Actuator rod free movement, solenoid operation

5. VGT STUCK VANES (diesel)
   Signs: Poor boost, limp mode, erratic boost, DTC
   Check: Commanded vs actual position on scan tool

6. CRACKED TURBINE HOUSING
   Cause: Thermal fatigue over high mileage
   Signs: Exhaust leak at turbo, hissing under load
   Action: Replace turbo
```

---

### **WRAP-UP: Consolidation & Day 20 Preview** (Slides 25-28, ~15 minutes)

---

#### Slide 25: The Complete Boosted Air Path
**Visual:** Full system diagram showing the complete air path for a turbocharged engine — from air filter, through MAF sensor, to turbo compressor inlet, through compressor, out charge pipe, through intercooler, out to throttle body, into intake manifold, through intake valves, into combustion chamber. Then exhaust out through exhaust valve, exhaust manifold, into turbo turbine, out turbine to catalytic converter and beyond. The complete circle of air flow. Colour-coded: blue for intake side, red for exhaust side, with the turbo at the junction.

**Instructor Narration:**
> "Let's put it all together. Here's the complete air path for a turbocharged engine — and this connects everything from Week 3 and Week 4.
>
> Start at the air filter. Clean air passes through the MAF sensor into the turbo compressor. The compressor forces it through the charge pipe to the intercooler, which cools it. Cooled, dense air passes through the throttle body into the intake manifold and into the cylinders.
>
> Inside the cylinder — combustion. The exhaust gas exits through the exhaust valve, collects in the exhaust manifold, and hits the turbo turbine. The turbine extracts energy, spins the shaft, drives the compressor on the other side, and the spent exhaust gas continues downstream through the catalytic converter, DPF, muffler, and out the tailpipe.
>
> That's a complete circle. Exhaust energy drives intake boost. Nothing is wasted. This is the elegant engineering I talked about at the start of today."

**PPT Content:**
```
THE COMPLETE BOOSTED AIR PATH — FULL CIRCLE

INTAKE SIDE (blue):
Air filter → MAF sensor → Turbo COMPRESSOR → Charge pipe →
Intercooler → Throttle body → Intake manifold → Cylinder

COMBUSTION (inside cylinder)

EXHAUST SIDE (red):
Cylinder → Exhaust manifold → Turbo TURBINE → Catalytic converter →
DPF (diesel) → Muffler → Tailpipe

THE TURBO CONNECTS BOTH SIDES:
— Turbine driven by exhaust (Day 18)
— Compressor feeds intake (Day 11)
— Intercooler cools the boost (Day 19)
— Wastegate/VGT controls the pressure (Day 19)

Exhaust energy → Shaft rotation → Intake compression → More power
```

---

#### Slide 26: Turbo Health — Quick Reference Diagnostic Checklist
**Visual:** One-page diagnostic checklist formatted as a technician's quick-reference card — organised by symptom with diagnostic steps.

**Instructor Narration:**
> "Here's a quick-reference checklist you can keep in your toolbox. When a customer comes in with a turbo-related complaint, start here. Match the symptom to the diagnostic steps. Work systematically — don't just throw parts at it. A boost leak test costs nothing but time. A new turbocharger costs the customer a lot of money. Make sure you've eliminated the cheap and common causes first."

**PPT Content:**
```
TURBO DIAGNOSTIC QUICK REFERENCE

SYMPTOM: Low power / sluggish acceleration
→ Boost leak test (smoke or pressure)
→ Check turbo shaft play
→ Scan tool: actual vs target boost
→ VGT: commanded vs actual position
→ Check charge piping and intercooler

SYMPTOM: Excessive exhaust smoke
→ Blue/white smoke: oil burning — check turbo seals and shaft play
→ Black smoke (diesel): over-fuelling — check boost level
→ Check oil level (dropping = turbo consuming oil)

SYMPTOM: Whining / screaming noise from turbo area
→ Check shaft play (bearing wear)
→ Check for FOD (compressor wheel damage)
→ Check oil supply to turbo (feed line restriction)

SYMPTOM: Limp mode / boost-related DTC
→ Read DTC — over-boost or under-boost?
→ Over-boost: wastegate stuck closed, solenoid fault
→ Under-boost: wastegate stuck open, boost leak, VGT stuck
→ Check actuator operation (mechanical linkage or electronic)

SYMPTOM: Exhaust leak at turbo
→ Inspect turbine housing for cracks
→ Check exhaust manifold to turbo gasket
→ Check turbo to downpipe gasket/flange
```

---

#### Slide 27: What You Learned Today
**Visual:** Checklist with tick marks — session achievements.

**Instructor Narration:**
> "Let's recap what you've accomplished today. You now understand how a turbocharger converts exhaust energy into intake boost. You can identify every part of a turbo — turbine, compressor, bearing housing, wastegate, VGT mechanism. You know how boost is controlled electronically and why the intercooler is essential. You've checked shaft play, inspected charge piping, performed a boost leak test, and read live turbo data on the scan tool.
>
> Most importantly, you can now trace the complete air path of a turbocharged engine from air filter to tailpipe — and you understand the turbo's role at the junction of exhaust and intake. That understanding connects everything we've covered in Weeks 3 and 4."

**PPT Content:**
```
DAY 19 RECAP — YOU CAN NOW:

[x] Explain how a turbocharger converts exhaust energy to intake boost
[x] Identify turbine, compressor, bearing housing, wastegate, and VGT
[x] Describe how wastegate and VGT control boost pressure
[x] Differentiate air-to-air and air-to-water intercoolers
[x] Explain turbo lag and why it occurs
[x] Check turbo shaft play (radial and axial)
[x] Inspect intercooler and charge piping for damage and leaks
[x] Perform a boost leak test with smoke tester or pressure gauge
[x] Read boost pressure and EGT data on the scan tool
[x] Trace the complete boosted air path from air filter to tailpipe
[x] Recognise common turbo failures and their symptoms
```

---

#### Slide 28: Day 20 Preview — Thermal & Emissions Diagnostics
**Visual:** Image showing a technician using an emissions analyser at the tailpipe, alongside a thermal imaging camera pointed at an engine bay. A scan tool displays live lambda and catalyst efficiency data.

**Instructor Narration:**
> "Tomorrow is Day 20 — the last day of Week 4. We bring together everything from this week: lubrication, cooling, exhaust, and forced induction. We'll focus on thermal diagnostics — using temperature data to diagnose cooling system and exhaust issues. And emissions diagnostics — understanding what the exhaust gas tells you about combustion health. We'll use the scan tool, an emissions analyser, and if available, a thermal imaging camera.
>
> It's a consolidation day — the goal is to connect all the systems from this week into a coherent diagnostic approach. Bring your scan tool skills and your curiosity. See you tomorrow."

**PPT Content:**
```
DAY 20 PREVIEW: THERMAL & EMISSIONS DIAGNOSTICS

Week 4 consolidation — bringing it all together:

— Thermal diagnostics: Using temperature data to find faults
  (Coolant flow patterns, EGT analysis, thermal imaging)

— Emissions diagnostics: What exhaust gas tells you
  (Lambda/O2 analysis, CO/HC/NOx interpretation, smoke opacity)

— Scan tool integration: Live data approach to engine health
  (Coolant temp, oil temp, EGT, boost, lambda, fuel trims)

— Connecting Week 4 systems:
  Lubrication (Day 16) + Cooling (Day 17) + Exhaust (Day 18)
  + Turbo/Intercooler (Day 19) = Complete engine support systems

Bring your diagnostic thinking. Tomorrow we connect the dots.
```

---

## Assessment Checkpoint

**Formative (not graded):**
- Component identification: correctly name all major turbocharger components on a physical unit or diagram (turbine, compressor, bearing housing, wastegate/VGT, oil/coolant connections)
- Shaft play check: demonstrate correct technique for assessing radial and axial play and state pass/fail criteria
- Boost leak test: successfully set up and perform a smoke test or pressure test on the charge system, identify any leak source
- Scan tool data: read and interpret boost pressure actual vs target, identify a healthy vs faulted system from live data
- Verbal quiz: explain the difference between a wastegate and VGT, and when each is used

---

## Key Takeaways

1. The turbocharger sits at the junction of exhaust and intake — it recovers exhaust energy to compress intake air
2. Three sections: turbine (exhaust-driven), compressor (forces air in), centre bearing housing (oil-cooled, often water-cooled shaft support)
3. Boost pressure is controlled by either a wastegate (bypasses exhaust) or VGT (changes exhaust flow angle) — both can be ECU-controlled
4. The intercooler is essential — compressing air heats it, and hot air is less dense; cooling restores density
5. Boost leaks are the most common turbo-related complaint — a smoke test finds them quickly and definitively
6. Oil quality and oil change intervals directly determine turbo longevity — oil starvation is the number one turbo killer
7. VGT stuck vanes from carbon build-up is the most common diesel turbo failure mode
8. The scan tool comparison of actual vs target boost is the starting point for any turbo diagnostic

---

## Preparation for Day 20

**Instructor prep:**
- Prepare emissions analyser (4-gas or 5-gas) and verify calibration
- If available, set up a thermal imaging camera (FLIR or similar)
- Prepare a vehicle with a known minor cooling or exhaust fault for diagnostic exercise
- Prepare scan tool with live data templates for coolant temp, oil temp, EGT, boost, lambda, and fuel trim PIDs
- Print Week 4 system interconnection diagram (lubrication, cooling, exhaust, turbo/intercooler)
- Prepare a short written quiz covering Week 4 topics (Days 16-19) for end-of-week assessment

**Learner prep:**
- Review notes from Days 16-19 (lubrication, cooling, exhaust, turbo/intercooler)
- Be ready to use the scan tool independently for live data reading
- Think about how the four systems covered this week interact with each other
