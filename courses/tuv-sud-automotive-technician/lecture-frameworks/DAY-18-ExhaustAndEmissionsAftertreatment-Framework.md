---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 4
week_title: "Keep It Alive — Lubrication, Cooling, Exhaust"
day_number: 18
session_title: "Exhaust & Emissions Aftertreatment"
duration_minutes: 180
theory_practice: "50:50"
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 18: Exhaust & Emissions Aftertreatment
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (90 min theory + 90 min practical)
**Approach:** System-Tracing — Follow the Gas From Cylinder to Tailpipe
**PPT Target:** 27-28 slides
**Week:** 4 of 8 — "Keep It Alive — Lubrication, Cooling, Exhaust"

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Trace the complete exhaust path from manifold through aftertreatment to tailpipe
- Explain the function and operating principle of a three-way catalytic converter (gasoline) and oxidation catalyst (diesel)
- Describe how narrowband and wideband O2/lambda sensors work and what data they provide to the ECU
- Explain DPF construction, soot loading, passive vs. active regeneration, and forced regeneration procedures
- Describe the SCR system including DEF/AdBlue dosing, urea injector, heated tank, and NOx sensors
- Identify emission-related DTCs (P0420, P2002, P2463) and interpret related live sensor data on a scan tool

**Connection to prior days:** Day 16 taught lubrication — oil protects the engine's moving parts. Day 17 taught cooling — coolant carries away excess heat. Day 18 completes the trio: the exhaust system removes waste combustion gases and cleans them before they reach the atmosphere. Together, these three systems keep the engine alive and legal.

---

## Connection to Prior Knowledge

Build from:
- Day 11-12: Four-stroke cycle — learners understand what comes out of the cylinder (exhaust gases: CO2, H2O, CO, HC, NOx, PM)
- Day 13: Fuel injection — learners know air-fuel ratio and how the ECU controls it
- Day 16: Oil system — exhaust valves and turbo bearings were mentioned as heat-stressed areas
- Day 17: Cooling system — EGT sensors share the concept of monitoring thermal conditions

**Bridge:** "Day 16 showed you how oil protects the engine. Day 17 showed you how coolant keeps it cool. Today, we follow the waste — the exhaust gas. It's hot, it's toxic, and it's your job to make sure it leaves the vehicle clean enough to meet emissions law. Modern diesel aftertreatment is more complex than the engine itself."

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: Two Jobs, One System** (Slides 1-3, ~10 minutes)

**Narrative Voice:** Direct, attention-grabbing. Frame the exhaust system as both a plumbing challenge and a chemistry challenge.

---

#### Slide 1: Title & Context
**Visual:** Split image — left side shows glowing red exhaust manifold on a running engine; right side shows the clean tailpipe tip of a modern diesel with almost invisible emissions

**Instructor Narration:**
> "Day 16: oil protects. Day 17: coolant cools. Day 18: exhaust removes and cleans. The exhaust system does two jobs that most people never think about. Job one: get extremely hot, toxic waste gas out of the engine safely and quietly. Job two — and this is the hard one — clean that gas before it reaches the air you and I breathe. Catalytic converters, particulate filters, urea injection, oxygen sensors — modern exhaust aftertreatment is a miniature chemical plant bolted to the underside of the car. Let's trace the path."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 4: Keep It Alive — Lubrication, Cooling, Exhaust
Day 18: Exhaust & Emissions Aftertreatment

Day 16: Oil PROTECTS
Day 17: Coolant COOLS
Day 18: Exhaust REMOVES & CLEANS

Two jobs:
1. Remove hot waste gas — safely and quietly
2. Clean toxic emissions — before they reach the atmosphere
```

---

#### Slide 2: What Comes Out of the Cylinder?
**Visual:** Diagram of a combustion chamber with arrows pointing out of the exhaust valve, labeled with the main exhaust gas constituents and their approximate percentages

**Instructor Narration:**
> "Before we talk about cleaning the exhaust, you need to know what's in it. When fuel burns perfectly — which it never does — you get CO2 and water. That's it. But combustion is never perfect. You get carbon monoxide — CO — from incomplete combustion. You get unburned hydrocarbons — HC — fuel that didn't fully burn. You get nitrogen oxides — NOx — formed when nitrogen in the air reacts with oxygen at high temperatures. And in diesel engines especially, you get particulate matter — PM — tiny soot particles.
>
> CO is a poisonous gas. HC contributes to smog. NOx causes acid rain and respiratory problems. Particulate matter penetrates deep into your lungs. Every one of these must be reduced to near zero before the gas leaves the tailpipe. That's what aftertreatment does."

**PPT Content:**
```
WHAT COMES OUT OF THE CYLINDER?

Perfect combustion: Fuel + Air → CO2 + H2O
Real combustion: Fuel + Air → CO2 + H2O + BAD STUFF

The "bad stuff":
• CO  (Carbon Monoxide)      — Poisonous gas
• HC  (Unburned Hydrocarbons) — Smog, carcinogenic
• NOx (Nitrogen Oxides)       — Acid rain, respiratory harm
• PM  (Particulate Matter)    — Soot, lung penetrating (diesel)

GASOLINE engines: mainly CO, HC, NOx
DIESEL engines: mainly NOx, PM (plus some CO, HC)

Aftertreatment goal: reduce ALL of these to near zero
```

---

#### Slide 3: Today's Plan
**Visual:** Horizontal timeline showing the four session blocks with clock icons

**Instructor Narration:**
> "Here's how today flows. First, we'll trace the exhaust path from manifold to tailpipe — every component. Then we'll go deep into the chemistry — catalytic converters and oxygen sensors. After that, diesel-specific aftertreatment — DPF, SCR, AdBlue, EGR. Then we go hands-on in the workshop: identify components on a real vehicle, read live O2 sensor data, check DPF soot loading on a scan tool, and inspect the AdBlue system. Let's start at the beginning — where exhaust gas is born."

**PPT Content:**
```
TODAY'S PLAN (180 minutes)

SETUP (10 min):
— What's in exhaust gas, why it must be cleaned

DEVELOPMENT Part 1 (35 min):
— Exhaust path: manifold → catalytic converter → tailpipe
— O2/lambda sensors: narrowband, wideband, fuel trim

DEVELOPMENT Part 2 (30 min):
— DPF: soot loading, passive/active/forced regeneration
— SCR & AdBlue: urea dosing, NOx sensors
— EGR revisited (gasoline & diesel)

PRACTICAL (75 min):
— Trace exhaust on undercar view
— Identify cat, DPF, SCR on diesel vehicle
— Read O2 sensor live data, check DPF soot load
— Inspect AdBlue components

WRAP-UP (15 min):
— Emission DTCs, Day 19 preview (turbocharger)
```

---

### **DEVELOPMENT PART 1: The Exhaust Path & Catalytic Converters** (Slides 4-13, ~35 minutes)

**Narrative Voice:** Systematic, tracing the gas flow component by component. Use the analogy of a river flowing through treatment plants before reaching the ocean.

---

#### Slide 4: The Complete Exhaust Path
**Visual:** Full-length side-view diagram of a vehicle underside with the exhaust system highlighted and every major component labeled in sequence from engine to tailpipe

**Instructor Narration:**
> "Let's trace the entire path. Exhaust gas leaves the cylinder through the exhaust valve and enters the exhaust manifold — or headers. The manifold collects gas from all cylinders into one or two pipes. Next comes a flex joint — a flexible section that absorbs engine movement and vibration so the rest of the exhaust doesn't crack. The downpipe carries gas toward the catalytic converter — your first treatment plant. After the cat, the gas may pass through a DPF on diesels, then an SCR catalyst. Then it enters the muffler — also called a silencer — which reduces noise. A resonator fine-tunes the sound. Finally, the tailpipe exits at the rear.
>
> On a modern diesel, from manifold to tailpipe, you might have six or seven major aftertreatment components. On a gasoline car, it's simpler — but still critical."

**PPT Content:**
```
THE COMPLETE EXHAUST PATH

ENGINE → Exhaust Manifold / Headers
  → Flex Joint (absorbs vibration)
    → Downpipe (connects to aftertreatment)
      → Catalytic Converter (chemical cleaning — Stage 1)
        → DPF — Diesel Particulate Filter (diesel only — Stage 2)
          → SCR Catalyst (diesel only — Stage 3)
            → Muffler / Silencer (noise reduction)
              → Resonator (sound tuning)
                → Tailpipe (exit)

GASOLINE: Manifold → Cat → Muffler → Tailpipe
DIESEL:   Manifold → Oxidation Cat → DPF → SCR → Muffler → Tailpipe

Temperature at manifold: 400-900 C
Temperature at tailpipe: 50-150 C
```

---

#### Slide 5: Exhaust Manifold & Flex Joint
**Visual:** Close-up photo of a cast-iron exhaust manifold with heat shield, plus a photo of a stainless-steel flex joint showing the braided mesh

**Instructor Narration:**
> "The manifold is the first component. It's typically cast iron or stainless steel. Each cylinder has its own runner that merges into a collector. On performance vehicles, you'll see tubular headers instead of a cast manifold — they improve flow but cost more.
>
> The flex joint sits just after the manifold. The engine rocks on its mounts — especially under load. Without a flex joint, that movement would crack the downpipe or break the manifold stud. It's a braided stainless mesh section that allows a few degrees of flex. When you hear a loud exhaust on a car, the flex joint is one of the first places to check — they fatigue and split over time."

**PPT Content:**
```
EXHAUST MANIFOLD & FLEX JOINT

Exhaust Manifold:
• Collects exhaust from all cylinders into one or two pipes
• Material: Cast iron (common) or stainless steel (performance)
• Operates at 400-900 C — often has a heat shield
• Gasket between head and manifold — common leak point
• Headers = tubular performance alternative

Flex Joint (Flex Pipe):
• Braided stainless steel bellows section
• Absorbs engine rocking and vibration
• Prevents cracking of downstream rigid pipe
• Common failure: fatigue cracks → loud exhaust noise
• Inspection: look for soot stains indicating leaks

TECHNICIAN TIP: Exhaust leaks before the O2 sensor
cause false lean readings and driveability issues
```

---

#### Slide 6: Catalytic Converter — Three-Way (Gasoline)
**Visual:** Cutaway diagram of a three-way catalytic converter showing the ceramic honeycomb substrate coated with precious metals, plus a chemical equation diagram showing the three reactions

**Instructor Narration:**
> "The catalytic converter is where chemistry meets exhaust plumbing. On gasoline engines, you have a three-way catalytic converter — called 'three-way' because it treats three pollutants simultaneously. It oxidizes CO into CO2. It oxidizes HC into CO2 and water. And it reduces NOx back into nitrogen and oxygen.
>
> Inside the converter is a ceramic honeycomb substrate — thousands of tiny channels. The surface is coated with precious metals: platinum, palladium, and rhodium. These metals act as catalysts — they speed up chemical reactions without being consumed. The converter needs to be hot to work — at least 250 to 300 degrees Celsius. Below that temperature, it does nothing. We call that the light-off temperature.
>
> Here's the critical point: a three-way cat only works properly when the engine runs at stoichiometric ratio — 14.7 to 1 air-fuel ratio. Too lean, and it can't reduce NOx. Too rich, and it can't oxidize CO and HC. That's why the oxygen sensor is so important — it keeps the mixture right at that sweet spot."

**PPT Content:**
```
THREE-WAY CATALYTIC CONVERTER (Gasoline)

Three reactions, one device:
1. OXIDATION: CO + O2 → CO2 (removes carbon monoxide)
2. OXIDATION: HC + O2 → CO2 + H2O (removes hydrocarbons)
3. REDUCTION: NOx → N2 + O2 (removes nitrogen oxides)

Construction:
• Ceramic honeycomb substrate (cordierite)
• ~400-900 cells per square inch
• Coated with precious metals: Platinum (Pt), Palladium (Pd), Rhodium (Rh)
• Catalyst = speeds reaction without being consumed

Operating requirements:
• Light-off temperature: 250-300 C (below this, no conversion)
• Stoichiometric A/F ratio: 14.7:1 (lambda = 1.00)
• Three-way cat ONLY works in a narrow A/F window

Common failure: Catalyst degradation (reduced efficiency over time)
DTC: P0420 — Catalyst System Efficiency Below Threshold
```

---

#### Slide 7: Catalytic Converter — Diesel Oxidation Catalyst
**Visual:** Comparison diagram showing a gasoline three-way cat vs. a diesel oxidation catalyst (DOC), with the different chemical reactions highlighted

**Instructor Narration:**
> "Diesel engines are different. They run lean — always more air than the minimum needed. That means a three-way cat won't work because it can't reduce NOx in a lean environment. So diesels use a different approach — multiple aftertreatment stages.
>
> The first stage is the Diesel Oxidation Catalyst — the DOC. It handles CO and HC through oxidation, same as the gasoline cat. But it doesn't touch NOx or soot. Those need separate treatment — the DPF for soot and the SCR for NOx. The DOC also raises exhaust gas temperature, which helps the DPF regenerate. Think of it as the warm-up act for the harder chemistry downstream."

**PPT Content:**
```
DIESEL OXIDATION CATALYST (DOC)

Two reactions (oxidation only — no NOx reduction):
1. CO + O2 → CO2
2. HC + O2 → CO2 + H2O

Why not three-way?
• Diesel runs LEAN (excess oxygen) — lambda > 1
• Three-way cat needs stoichiometric (lambda = 1.00)
• Cannot reduce NOx in oxygen-rich exhaust

DOC additional function:
• Raises exhaust temperature (exothermic reactions)
• This heat helps DPF regeneration downstream

DOC does NOT handle:
• NOx → needs SCR system
• Particulate Matter → needs DPF

DIESEL AFTERTREATMENT = DOC + DPF + SCR
(Three separate devices, three separate jobs)
```

---

#### Slide 8: Oxygen / Lambda Sensors — Overview
**Visual:** Diagram of an exhaust pipe with two O2 sensors marked — one upstream (before the cat) and one downstream (after the cat), with labels showing their different roles

**Instructor Narration:**
> "The oxygen sensor — also called a lambda sensor — is the ECU's eyes into the exhaust stream. There are always at least two: one upstream of the catalytic converter, and one downstream.
>
> The upstream sensor tells the ECU what the air-fuel mixture actually is, so the ECU can adjust fuel injection — that's fuel trim. The downstream sensor monitors catalyst efficiency — if the cat is healthy, the downstream signal should be nearly flat because the cat is consuming the oxygen variation. If the downstream sensor looks the same as the upstream, the cat has failed. That's your P0420 code.
>
> There are two types of sensors you need to know: narrowband and wideband."

**PPT Content:**
```
OXYGEN / LAMBDA SENSORS — OVERVIEW

Two positions, two jobs:

UPSTREAM (before catalytic converter):
• Measures exhaust O2 content
• ECU uses it for FUEL TRIM — adjusts injector pulse width
• Fast-switching signal — the ECU chases lambda = 1.00

DOWNSTREAM (after catalytic converter):
• Monitors CATALYST EFFICIENCY
• Healthy cat: downstream signal is nearly flat (steady ~0.6-0.7V)
• Failed cat: downstream signal mirrors upstream (oscillating)
• Triggers P0420 if cat efficiency drops

Minimum: 2 sensors per catalyst (upstream + downstream)
V6/V8 with dual exhaust: 4 sensors (2 per bank)

Sensor types:
• Narrowband (switching) — common downstream
• Wideband (linear) — common upstream on modern vehicles
```

---

#### Slide 9: Narrowband O2 Sensor (Switching Type)
**Visual:** Cross-section diagram of a thimble-type zirconia O2 sensor, plus a graph showing the characteristic 0-1V switching signal oscillating between rich and lean

**Instructor Narration:**
> "The narrowband sensor is the original oxygen sensor. It's built around a zirconia ceramic element that generates a voltage based on the difference in oxygen concentration between the exhaust gas and the outside air.
>
> Here's the key: it only tells you rich or lean — it doesn't tell you how rich or how lean. The output swings between about 0.1 volts for lean and 0.9 volts for rich. There's a sharp transition right at stoichiometric — lambda 1.00. The ECU watches this switching and constantly adjusts the fuel injectors — a little more fuel, a little less fuel — hunting back and forth across that stoichiometric point. You'll see this oscillation on your scan tool — the signal should switch between 0.1 and 0.9 volts several times per second.
>
> All O2 sensors have a heater circuit. The zirconia element needs to be at 300 degrees or more to work. The heater gets it there quickly after a cold start. If the heater fails, the sensor takes too long to activate and you'll get a heater circuit DTC."

**PPT Content:**
```
NARROWBAND O2 SENSOR (Switching / Thimble Type)

Construction:
• Zirconia (ZrO2) ceramic element
• Platinum electrodes (inner + outer)
• Inner surface exposed to outside air (reference)
• Outer surface exposed to exhaust gas

Output signal:
• Lean (excess O2):  ~0.1V
• Rich (low O2):     ~0.9V
• Switches sharply at lambda = 1.00 (~0.45V crossover)
• Normal switching frequency: 1-5 times per second

Limitations:
• Only tells RICH or LEAN — not how much
• Cannot measure precise lambda value
• Useless below 300 C (needs heater)

Heater circuit:
• Internal resistance heater (12V, 8-15 ohms typical)
• Gets sensor to operating temp in 15-30 seconds
• DTC: P0135 (Bank 1 Sensor 1 heater circuit malfunction)

Signal voltage: 0 - 1 V range
```

---

#### Slide 10: Wideband O2 Sensor (Linear Type)
**Visual:** Cross-section diagram of a wideband (planar) O2 sensor showing the Nernst cell and pump cell, plus a graph showing the linear 0-5V output across a wide lambda range

**Instructor Narration:**
> "The wideband sensor is the modern evolution. Instead of just switching between rich and lean, it gives you a precise, linear measurement of the actual air-fuel ratio. The output is typically 0 to 5 volts, and it maps directly to lambda values from about 0.7 to well beyond 2.0.
>
> Inside, it has two cells — a Nernst cell and a pump cell. The Nernst cell works like a narrowband sensor. The pump cell actively pumps oxygen in or out of a measurement chamber to maintain a reference point. The amount of current the pump cell needs to do this tells you the exact lambda value.
>
> On your scan tool, a wideband sensor at stoichiometric reads about 3.3 volts — depending on the manufacturer. Rich goes below that, lean goes above. The signal is smooth and linear, not oscillating like a narrowband.
>
> Modern gasoline engines use a wideband sensor upstream and a narrowband downstream. That gives the ECU precise control of the mixture and accurate monitoring of the cat."

**PPT Content:**
```
WIDEBAND O2 SENSOR (Linear / Planar / AFR Sensor)

Construction:
• Planar (flat) design — zirconia layers
• Two cells: Nernst cell + Pump cell
• Internal reference chamber
• Integrated heater (reaches temp faster)

Output signal:
• Linear output: 0 - 5V range
• At stoichiometric (lambda 1.00): ~3.3V (varies by manufacturer)
• Lean (lambda > 1): voltage INCREASES
• Rich (lambda < 1): voltage DECREASES
• Can measure precise lambda from 0.7 to 2.0+

Advantages over narrowband:
• Precise A/F ratio (not just rich/lean)
• Faster response time
• Works across wider range (gasoline AND lean-burn/diesel)

Typical modern gasoline setup:
• UPSTREAM: Wideband (precise fuel control)
• DOWNSTREAM: Narrowband (catalyst monitoring)

Signal voltage: 0 - 5 V range (linear)
```

---

#### Slide 11: How the ECU Uses O2 Sensors — Fuel Trim
**Visual:** Block diagram showing upstream O2 sensor signal flowing to the ECU, which adjusts injector pulse width; then downstream O2 sensor providing catalyst monitoring. Include a scan tool screenshot showing short-term and long-term fuel trim values.

**Instructor Narration:**
> "Here's where it all connects. The ECU reads the upstream O2 sensor and compares the actual lambda to the target. If the exhaust is lean, the ECU adds fuel — increases injector on-time. If rich, it reduces fuel. This correction is called short-term fuel trim — STFT. It's a moment-to-moment adjustment, and you'll see it bouncing between maybe minus five percent and plus five percent on your scan tool.
>
> If the ECU has to consistently add or subtract fuel over time, it learns that offset and stores it as long-term fuel trim — LTFT. Normal LTFT should be within plus or minus five percent. If you see LTFT at plus fifteen percent, it means the engine is consistently running lean and the ECU is adding a lot of extra fuel to compensate. That's telling you there's a vacuum leak, a weak fuel pump, or a dirty injector.
>
> The downstream sensor doesn't control fuel. It monitors the cat. A healthy cat absorbs oxygen variation, so the downstream signal should be relatively flat. If it starts oscillating like the upstream sensor, the cat's efficiency has dropped. That's P0420."

**PPT Content:**
```
FUEL TRIM — HOW THE ECU USES O2 SENSOR DATA

UPSTREAM SENSOR → FUEL CONTROL
• ECU reads exhaust lambda
• Adjusts injector pulse width to maintain lambda = 1.00
• Short-Term Fuel Trim (STFT): instant correction (±5% normal)
• Long-Term Fuel Trim (LTFT): learned correction (±5% normal)

Fuel trim diagnostics:
• LTFT > +10%: Engine running LEAN (vacuum leak? weak fuel pump?)
• LTFT < -10%: Engine running RICH (leaking injector? high fuel pressure?)
• STFT swinging wildly: possible O2 sensor response problem

DOWNSTREAM SENSOR → CATALYST MONITORING
• Healthy cat: downstream signal is nearly flat (~0.6-0.7V)
• Failed cat: downstream mirrors upstream (oscillating)
• P0420: Catalyst System Efficiency Below Threshold (Bank 1)
• P0430: Same for Bank 2

SCAN TOOL CHECK:
• Display upstream + downstream O2 sensor simultaneously
• Compare waveform patterns
```

---

#### Slide 12: O2 Sensor Failure Modes & DTCs
**Visual:** Table showing common O2 sensor failure modes, symptoms, and associated DTCs with scan tool waveform examples for each

**Instructor Narration:**
> "O2 sensors don't last forever. The zirconia element degrades with heat exposure and contamination — especially from oil burning or coolant leaks into the combustion chamber. A slow sensor takes too long to switch, so the ECU can't track the mixture properly. A biased sensor reads consistently high or low, pushing fuel trim in one direction.
>
> Common DTCs: P0130 through P0167 cover oxygen sensor circuit faults for banks 1 and 2, sensors 1 and 2. P0135 and P0155 are heater circuit faults. And P0420 and P0430 are catalyst efficiency codes triggered by the downstream sensor comparison. When you see P0420, don't rush to replace the cat — first check that the upstream and downstream sensors are working correctly. A lazy upstream sensor can cause a false P0420."

**PPT Content:**
```
O2 SENSOR FAILURE MODES & DTCs

Common failures:
• Slow response (lazy sensor) — degraded zirconia element
• Biased high (always reads rich) — contamination
• Biased low (always reads lean) — air leak at sensor, cracked element
• Heater failure — open or short in heater circuit
• Wiring damage — heat, corrosion, rodent chew

Key DTCs:
P0130: O2 Sensor Circuit (Bank 1, Sensor 1)
P0131: O2 Sensor Low Voltage (B1S1) — stuck lean
P0132: O2 Sensor High Voltage (B1S1) — stuck rich
P0133: O2 Sensor Slow Response (B1S1)
P0135: O2 Sensor Heater Circuit (B1S1)
P0136-P0141: Bank 1, Sensor 2 (downstream) equivalents
P0150-P0161: Bank 2 equivalents

P0420: Catalyst Efficiency Below Threshold (Bank 1)
P0430: Catalyst Efficiency Below Threshold (Bank 2)

DIAGNOSTIC TIP: Always check O2 sensor operation
BEFORE condemning the catalytic converter
```

---

#### Slide 13: Quick Knowledge Check — Part 1
**Visual:** Four multiple-choice questions on screen

**Instructor Narration:**
> "Let's pause and check. Four quick questions — shout out the answers. One: what three pollutants does a three-way cat treat? Two: what voltage does a narrowband sensor output when the mixture is rich? Three: what does the downstream O2 sensor monitor? Four: if long-term fuel trim is at plus fifteen percent, is the engine running rich or lean?"

**PPT Content:**
```
KNOWLEDGE CHECK — PART 1

1. A three-way catalytic converter treats which three pollutants?
   a) CO, HC, NOx
   b) CO2, H2O, N2
   c) PM, NOx, CO2

2. A narrowband O2 sensor reads ~0.9V. The mixture is:
   a) Lean
   b) Rich
   c) Stoichiometric

3. The DOWNSTREAM O2 sensor monitors:
   a) Air-fuel ratio for fuel trim
   b) Catalytic converter efficiency
   c) Exhaust gas temperature

4. Long-term fuel trim at +15% means the engine is running:
   a) Rich — ECU is removing fuel
   b) Lean — ECU is adding extra fuel
   c) Normal — no correction needed

ANSWERS: 1-a, 2-b, 3-b, 4-b
```

---

### **DEVELOPMENT PART 2: DPF, SCR, and Diesel Aftertreatment** (Slides 14-21, ~30 minutes)

**Narrative Voice:** Shift to diesel-specific complexity. Acknowledge that this is the most technically dense part of the day. Use the analogy: "The diesel aftertreatment system is a chemical plant on wheels."

---

#### Slide 14: Diesel Particulate Filter — Construction
**Visual:** Cutaway diagram of a DPF showing the wall-flow honeycomb structure with alternately plugged channels, plus a magnified view of soot particles trapped in the porous ceramic walls

**Instructor Narration:**
> "The DPF is the diesel engine's soot trap. Inside is a ceramic honeycomb — but unlike the catalytic converter where gas flows straight through, the DPF channels are alternately plugged. Gas enters an open channel, is forced through the porous ceramic wall into the adjacent channel, and exits. The soot particles are too large to pass through the wall, so they get trapped.
>
> The substrate is typically cordierite or silicon carbide. Silicon carbide handles higher temperatures and is more common on modern vehicles. Over time, soot accumulates and the filter becomes restricted. If you don't clean it, back-pressure builds, the engine loses power, and eventually you can damage the turbo or engine. That's why regeneration exists."

**PPT Content:**
```
DIESEL PARTICULATE FILTER (DPF) — CONSTRUCTION

Design: Wall-flow honeycomb filter
• Channels alternately plugged at inlet and outlet ends
• Exhaust gas forced THROUGH porous ceramic walls
• Soot particles trapped (too large to pass)
• Clean gas exits through adjacent channels

Substrate materials:
• Cordierite — lower cost, lower temperature limit
• Silicon Carbide (SiC) — higher temp tolerance, more common today

Specifications:
• Filtration efficiency: >95% of particulate matter
• Cell density: 100-300 cells per square inch
• Soot capacity: 6-10 grams per litre of filter volume
• Location: downstream of DOC (uses DOC heat)

What happens when it fills up?
→ Back-pressure increases
→ Engine power drops
→ Turbo stress increases
→ MUST BE REGENERATED
```

---

#### Slide 15: DPF Regeneration Strategies
**Visual:** Three-panel diagram — left panel shows passive regeneration (normal driving), center shows active regeneration (ECU-triggered), right shows forced regeneration (technician-initiated via scan tool)

**Instructor Narration:**
> "There are three regeneration strategies, and you need to know all of them. Passive regeneration happens naturally during highway driving. When exhaust temperature exceeds about 350 degrees, the soot oxidizes — burns off — with help from the DOC catalyst upstream. If you drive long distances at steady speed, the DPF may never need active help.
>
> Active regeneration is triggered by the ECU when the soot loading reaches a threshold — typically measured by a differential pressure sensor across the DPF. The ECU commands late fuel injection, which creates unburned fuel that oxidizes in the DOC, raising exhaust temperature to 550-600 degrees. This burns the soot off. You might notice the cooling fan running higher, idle speed slightly elevated, and a slight smell. Active regen takes about 10 to 30 minutes.
>
> Forced regeneration is what you do in the workshop when the DPF is so loaded that the ECU can't perform active regen during normal driving — typically in vehicles used for short urban trips. You connect a scan tool, command a stationary regeneration, and the ECU runs a controlled burn at the programmed temperature. The vehicle must be stationary, the engine at operating temperature, and you must monitor it throughout. Never walk away during a forced regen — exhaust temperatures exceed 600 degrees."

**PPT Content:**
```
DPF REGENERATION — THREE STRATEGIES

1. PASSIVE REGENERATION (automatic, driver unaware)
   • Occurs during sustained highway driving
   • Exhaust temp naturally > 350 C
   • Soot oxidizes with help from DOC catalyst (NO2)
   • Best for vehicles with regular long-distance use

2. ACTIVE REGENERATION (ECU-triggered)
   • ECU detects high soot loading via differential pressure sensor
   • Commands LATE fuel injection (post-injection)
   • Unburned fuel oxidizes in DOC → raises temp to 550-600 C
   • Burns soot in DPF over 10-30 minutes
   • Signs: higher idle, fan running, slight smell
   • DO NOT turn off engine during active regen!

3. FORCED REGENERATION (technician-initiated)
   • Performed via scan tool command in workshop
   • Used when active regen keeps failing (short-trip driving)
   • Vehicle stationary, engine at operating temp
   • Monitor throughout — exhaust temps > 600 C
   • NEVER leave vehicle unattended during forced regen

DPF soot loading limit: ~45 g/L → forced regen or replacement
```

---

#### Slide 16: DPF Sensors — Differential Pressure & EGT
**Visual:** Diagram showing the DPF with its differential pressure sensor (two hoses — one before, one after the DPF) and two EGT sensors (pre-DPF and post-DPF), with signal flow arrows to the ECU

**Instructor Narration:**
> "The ECU needs to know two things about the DPF: how much soot is in it, and how hot it is. The differential pressure sensor answers the first question. It has two ports — one sampling pressure before the DPF and one after. The difference tells the ECU how restricted the filter is. Higher differential pressure means more soot. The ECU combines this with exhaust flow rate to estimate soot loading in grams.
>
> Exhaust Gas Temperature sensors — EGT sensors — answer the second question. There's typically one before the DPF and one after. During regeneration, the pre-DPF sensor monitors the incoming temperature, and the post-DPF sensor confirms that the burn is happening — you should see the post-DPF temperature rise as soot oxidizes. These sensors are also critical for protecting the DPF from overheating — if the temperature exceeds about 700 degrees, the ECU aborts the regeneration to prevent substrate damage."

**PPT Content:**
```
DPF MONITORING SENSORS

DIFFERENTIAL PRESSURE SENSOR:
• Measures pressure drop across DPF
• Two sampling hoses: pre-DPF and post-DPF
• Higher delta-P = more soot loading
• ECU calculates soot mass (grams) using delta-P + flow rate
• Normal: 2-10 kPa (varies by vehicle/load)
• Regen trigger: typically 15-20 kPa

DTC: P2463 — DPF Soot Accumulation (above threshold)
DTC: P2002 — DPF Efficiency Below Threshold

EXHAUST GAS TEMPERATURE (EGT) SENSORS:
• Thermocouple or NTC/PTC type
• Location: PRE-DPF (EGT1) and POST-DPF (EGT2)
• Monitor regen temperature (target: 550-600 C)
• Protect DPF from overheating (abort if > 700 C)
• Also used for DOC light-off monitoring

EGT sensor values (typical during active regen):
• Pre-DPF: 500-650 C
• Post-DPF: 550-700 C (rises as soot burns)
```

---

#### Slide 17: SCR & DEF/AdBlue — Overview
**Visual:** Full SCR system diagram showing the AdBlue tank with heater and level sensor, the dosing module/pump, the urea injector spraying into the exhaust pipe before the SCR catalyst, and the SCR catalyst brick

**Instructor Narration:**
> "The DPF catches soot. But what about NOx? Diesel engines produce a lot of it because they run hot and lean. The solution is Selective Catalytic Reduction — SCR. Here's how it works: a liquid called DEF — Diesel Exhaust Fluid, trade name AdBlue — is injected into the exhaust stream before the SCR catalyst. AdBlue is a 32.5 percent solution of urea in deionized water. When it hits the hot exhaust, the water evaporates and the urea decomposes into ammonia. That ammonia reacts with NOx on the SCR catalyst surface, converting it into harmless nitrogen and water.
>
> The system has several components you need to know. The AdBlue tank — usually 15 to 25 litres, with a heater because urea freezes at minus 11 degrees. A dosing module or pump that pressurizes the AdBlue. An injector that sprays it into the exhaust. And a decomposition tube or mixer that ensures even distribution before the SCR catalyst."

**PPT Content:**
```
SCR — SELECTIVE CATALYTIC REDUCTION

The chemistry:
• AdBlue (DEF) = 32.5% urea + 67.5% deionized water
• Urea decomposes in hot exhaust:
  (NH2)2CO → 2NH3 + CO2 (ammonia + carbon dioxide)
• Ammonia reacts with NOx on SCR catalyst:
  4NH3 + 4NO + O2 → 4N2 + 6H2O
• Result: NOx converted to nitrogen (N2) + water (H2O)

System components:
• AdBlue tank (15-25 L, blue filler cap)
  — Level sensor
  — Heater (AdBlue freezes at -11 C)
  — Temperature sensor
  — Quality sensor (some vehicles)
• Dosing module / supply pump
• Urea injector (sprays into exhaust pipe)
• Decomposition tube / mixer
• SCR catalyst brick

NOx reduction efficiency: up to 95%
```

---

#### Slide 18: NOx Sensors & SCR Control
**Visual:** Diagram of the SCR system with NOx sensor positions marked (pre-SCR and post-SCR), plus a scan tool screenshot showing NOx values in ppm before and after the SCR catalyst

**Instructor Narration:**
> "Just like the O2 sensor tells the ECU about the catalytic converter, NOx sensors tell it about the SCR system. There's typically one before the SCR catalyst and one after. The pre-SCR sensor measures how much NOx is coming from the engine — that tells the ECU how much AdBlue to inject. The post-SCR sensor verifies that the SCR catalyst is actually converting the NOx. If post-SCR NOx is still high despite dosing, the system has a problem — maybe the catalyst is degraded, the injector is blocked, or someone filled the tank with water instead of AdBlue.
>
> The ECU's dosing strategy is sophisticated. It factors in exhaust temperature, exhaust flow, NOx concentration, and SCR catalyst temperature. If the catalyst is too cold — below about 200 degrees — it stops dosing because the ammonia won't react and will slip through as white smoke with a sharp smell. That's called ammonia slip."

**PPT Content:**
```
NOx SENSORS & SCR SYSTEM CONTROL

NOx sensor positions:
• PRE-SCR (upstream): Measures engine-out NOx
  — ECU uses this to calculate AdBlue dosing quantity
  — Typical engine-out NOx: 200-800 ppm

• POST-SCR (downstream): Monitors SCR efficiency
  — Target: < 30 ppm after SCR catalyst
  — If high: catalyst degraded, dosing fault, wrong fluid

ECU dosing control factors:
• Engine-out NOx level (from pre-SCR sensor)
• Exhaust gas temperature (SCR needs > 200 C)
• Exhaust mass flow rate
• SCR catalyst temperature
• AdBlue tank level and quality

Ammonia slip:
• Overdosing or low SCR temp → unreacted ammonia exits
• White smoke, sharp pungent smell at tailpipe
• Post-SCR NOx sensor can detect ammonia (cross-sensitivity)

AdBlue consumption: ~3-5% of diesel fuel consumption
(~1L AdBlue per 600-1000 km typical)
```

---

#### Slide 19: AdBlue System — Practical Details
**Visual:** Photos of the AdBlue filler cap (blue), tank location under the vehicle, dosing module, and a crystallized/blocked urea injector tip

**Instructor Narration:**
> "Let's talk practical. The AdBlue tank has a blue cap — always blue, never confused with diesel. It's usually located under the vehicle near the fuel tank, or in the boot area. The tank has a heater because AdBlue crystallizes at minus 11 degrees — in cold climates, the system heats the tank and lines before the engine can inject.
>
> Common problems: the urea injector tip crystallizes and blocks — you'll see white deposits. The dosing lines can crack from heat cycling. The tank heater can fail, causing winter DTCs. And customers sometimes let the AdBlue run dry, which triggers a power limitation and eventually prevents restart — by law, the vehicle must derate and eventually refuse to start if the SCR system is inoperative. Never top up with anything other than AdBlue — water, windscreen washer fluid, or diesel will destroy the SCR catalyst."

**PPT Content:**
```
AdBlue SYSTEM — PRACTICAL DETAILS FOR TECHNICIANS

Identification:
• Blue filler cap (ISO standard)
• Separate from diesel filler
• Tank: 15-25 L, often under vehicle or in boot area

Common service issues:
• Crystallization at injector tip → white crusty deposits
  — Clean or replace injector
• Dosing line cracks → leaks, underdosing
• Tank heater failure → cold weather DTCs
• Level sensor failure → incorrect level reading
• Quality sensor fault → wrong AdBlue concentration detected

WARNING — WRONG FLUID:
• Water → no NOx reduction, sensor DTCs
• Diesel → DESTROYS SCR catalyst (very expensive)
• Washer fluid → catalyst damage
• Only use ISO 22241 certified AdBlue/DEF

Vehicle behavior if AdBlue empty:
1. Warning light and countdown message
2. Power limitation (derated mode)
3. Eventually: vehicle will not restart after ignition off
(Legal requirement — EU6, EPA Tier 4)
```

---

#### Slide 20: EGR System — Revisited (Gasoline & Diesel)
**Visual:** Side-by-side diagrams — left shows a gasoline EGR valve with vacuum actuator or electronic stepper motor; right shows a diesel EGR with cooler, showing the flow path from exhaust manifold back to intake

**Instructor Narration:**
> "We touched on EGR earlier in the course, but let's revisit it in the context of emissions. Exhaust Gas Recirculation takes a small portion of exhaust gas and feeds it back into the intake. This dilutes the fresh air charge, lowers combustion temperature, and reduces NOx formation. It attacks the problem at the source — before the exhaust even leaves the cylinder.
>
> On gasoline engines, EGR is used mainly at part-load to reduce pumping losses and lower NOx. On diesel engines, EGR is far more critical — it's one of the primary NOx control strategies, working alongside SCR.
>
> Diesel EGR systems often include an EGR cooler — a small heat exchanger that cools the recirculated gas for even greater NOx reduction. But cooled EGR creates a problem: soot and oil vapor in the recirculated gas mix with condensation in the cooler and form a thick, tar-like sludge that blocks the EGR valve and intake manifold. Diesel EGR system cleaning is one of the most common workshop jobs you'll do."

**PPT Content:**
```
EGR — EXHAUST GAS RECIRCULATION (Revisited)

Purpose: Reduce NOx by lowering combustion temperature
Method: Recirculate a portion of exhaust gas back to intake

GASOLINE EGR:
• Used at part-load cruising
• Vacuum or electronic EGR valve
• Reduces pumping losses + NOx
• Relatively clean exhaust gas — fewer deposits

DIESEL EGR:
• Heavy use across operating range
• EGR COOLER reduces gas temperature further
• More effective NOx reduction when gas is cooled
• PROBLEM: Soot + oil + condensation = carbon sludge
  — Blocks EGR valve (stuck open or closed)
  — Blocks intake manifold ports
  — Common workshop job: EGR system cleaning

EGR + SCR together = dual NOx reduction strategy (modern diesel)

Common DTCs:
P0401: EGR Insufficient Flow
P0402: EGR Excessive Flow
P0404: EGR Control Circuit Range/Performance
```

---

#### Slide 21: The Complete Diesel Aftertreatment — Summary
**Visual:** Full flow diagram of a modern Euro 6 diesel exhaust system from engine to tailpipe, showing DOC, DPF, SCR, and all sensors (O2, EGT x2, differential pressure, NOx x2) in their correct positions

**Instructor Narration:**
> "Here's the full picture for a modern Euro 6 diesel. Exhaust leaves the engine, passes through the DOC — which oxidizes CO and HC and generates heat. Then the DPF — which traps soot, monitored by the differential pressure sensor and EGT sensors. AdBlue is injected after the DPF, and the gas enters the SCR catalyst where NOx is converted. NOx sensors before and after the SCR confirm the system is working. Finally, the cleaned gas passes through the muffler and out the tailpipe.
>
> Count the sensors: two EGT sensors, one differential pressure sensor, two NOx sensors, and potentially an O2 sensor. Plus the AdBlue tank with its level, temperature, and quality sensors. That's easily ten or more sensors just for the aftertreatment system. When I said this is more complex than the engine itself — I wasn't exaggerating."

**PPT Content:**
```
COMPLETE DIESEL AFTERTREATMENT — EURO 6 SUMMARY

                    AdBlue
                    Injector ↓
ENGINE → DOC → DPF ——→ SCR → Muffler → Tailpipe
         |      |              |
     O2 sensor  |           NOx sensors
              EGT1    EGT2   (pre & post)
              Delta-P sensor

Component count:
• DOC (Diesel Oxidation Catalyst)    — 1
• DPF (Diesel Particulate Filter)    — 1
• SCR (Selective Catalytic Reduction) — 1
• Muffler                            — 1

Sensor count:
• EGT sensors                        — 2 (pre & post DPF)
• Differential pressure sensor       — 1 (across DPF)
• NOx sensors                        — 2 (pre & post SCR)
• O2 / lambda sensor                 — 1 (or more)
• AdBlue: level + temp + quality     — 3

TOTAL: 4 aftertreatment components + 9+ sensors
"More complex than the engine itself"
```

---

### **PRACTICAL: Workshop Activities** (Slides 22-25, ~75 minutes)

**Narrative Voice:** Hands-on guide. Transition from classroom to workshop floor. Safety-conscious, methodical.

---

#### Slide 22: Practical 1 — Trace the Exhaust Path (Undercar)
**Visual:** Photo of a vehicle on a lift with the exhaust system visible from below, with numbered stations along the exhaust from front to rear

**Instructor Narration:**
> "Vehicle's on the lift. I want each group to walk the exhaust system from front to back and identify every component. Start at the exhaust manifold, follow the pipe, and call out each component as you pass it. I'll give you a blank diagram — fill in what you see. Pay attention to hangers, clamps, and heat shields too. Those are service items that fail and cause rattles."

**PPT Content:**
```
PRACTICAL 1: TRACE THE EXHAUST PATH (20 min)

Task: Walk the exhaust system front-to-rear on the lift

Identify and mark on your diagram:
□ Exhaust manifold
□ Flex joint / flex pipe
□ Downstream pipe / downpipe
□ Catalytic converter (note size and position)
□ DPF (diesel vehicles — larger brick)
□ SCR catalyst (diesel — look for AdBlue injector)
□ Muffler / silencer
□ Resonator (if present)
□ Tailpipe exit
□ Exhaust hangers (rubber mounts)
□ Heat shields
□ Sensor locations (note wire connectors)

LOOK FOR: Rust, soot stains (leak indicators),
cracked flex joints, damaged heat shields
```

---

#### Slide 23: Practical 2 — Identify Aftertreatment on Diesel Vehicle
**Visual:** Annotated photo of a modern diesel exhaust system showing the DOC, DPF canister, AdBlue injector location, and SCR canister with labels

**Instructor Narration:**
> "Now let's focus on the diesel vehicle. I want you to identify the DOC — it's usually the first canister after the manifold. Then the DPF — typically the largest canister, with the differential pressure sensor hoses visible. Find the AdBlue injector — it's between the DPF and SCR, usually with a small mixer pipe. And the SCR catalyst — the last major canister before the muffler. Also locate the AdBlue tank — follow the blue filler cap to the tank underneath or in the boot."

**PPT Content:**
```
PRACTICAL 2: IDENTIFY DIESEL AFTERTREATMENT (15 min)

On the diesel vehicle, locate and physically touch:

□ DOC (Diesel Oxidation Catalyst)
  — First canister, closest to engine

□ DPF (Diesel Particulate Filter)
  — Largest canister, two hoses to differential pressure sensor

□ AdBlue injector
  — Small injector between DPF and SCR, with electrical connector

□ SCR catalyst
  — After AdBlue injection point

□ AdBlue tank
  — Follow blue filler cap, find tank and heater connector

□ EGT sensors (if accessible)
  — Threaded into exhaust pipe, wiring connector

□ NOx sensors (if accessible)
  — Larger than EGT, usually pre- and post-SCR

SKETCH the layout in your notebook
```

---

#### Slide 24: Practical 3 — O2 Sensor Live Data on Scan Tool
**Visual:** Scan tool screenshot showing live O2 sensor data — upstream wideband reading in lambda and voltage, downstream narrowband voltage, STFT and LTFT values, all on one screen

**Instructor Narration:**
> "Connect your scan tool to the gasoline vehicle. Navigate to live data — engine data — oxygen sensors. Start the engine and let it reach operating temperature. I want you to observe four things. First, the upstream O2 sensor — is it a wideband or narrowband? What does the signal look like? Second, the downstream sensor — is it flat or oscillating? Third, short-term fuel trim — is it bouncing between positive and negative? Fourth, long-term fuel trim — what's the number? Record all four observations. We'll compare results as a group."

**PPT Content:**
```
PRACTICAL 3: O2 SENSOR LIVE DATA (20 min)

Connect scan tool → Live Data → O2 / Lambda Sensors

Observe and record:

1. UPSTREAM O2 SENSOR:
   □ Type: Wideband (0-5V) or Narrowband (0-1V)?
   □ Signal behavior: Smooth (wideband) or switching (narrowband)?
   □ At idle: what is the reading?

2. DOWNSTREAM O2 SENSOR:
   □ Signal: Flat/stable (~0.6-0.7V) = healthy cat
   □ Signal: Oscillating like upstream = degraded cat

3. SHORT-TERM FUEL TRIM (STFT):
   □ Value at idle: _______%
   □ Is it bouncing? (normal: ±5%)

4. LONG-TERM FUEL TRIM (LTFT):
   □ Value: _______%
   □ Normal: ±5%. Above ±10% = investigate

Compare with your partner.
What does your data tell you about this engine?
```

---

#### Slide 25: Practical 4 & 5 — DPF Soot Load & AdBlue Inspection
**Visual:** Split screen — left shows scan tool reading DPF soot loading in grams and differential pressure in kPa; right shows hands inspecting AdBlue filler cap, tank, and dosing components under the vehicle

**Instructor Narration:**
> "On the diesel vehicle, connect the scan tool and find DPF data. Look for soot loading — it may be displayed in grams or as a percentage. Find differential pressure — the live reading across the DPF. Check how many kilometers since last regeneration and how many regenerations have occurred total. This tells you the DPF's health history.
>
> Then move to the AdBlue system. Open the filler cap — it should be blue. Check the fluid level on the scan tool and visually if the tank is translucent. Look at the dosing lines for white crystallization. Check the injector tip if accessible. And verify the tank heater connector is intact — critical for vehicles operating in cold climates."

**PPT Content:**
```
PRACTICAL 4: DPF SOOT LOAD CHECK (10 min)

Connect scan tool → Diesel Particulate Filter data

Record:
□ Soot loading: _______ grams (or _____ %)
□ Differential pressure: _______ kPa
□ Distance since last regen: _______ km
□ Total regen count: _______
□ DPF status: Normal / Regen Needed / Critical

Is the DPF healthy based on these numbers?


PRACTICAL 5: AdBlue SYSTEM INSPECTION (10 min)

Visual and scan tool checks:

□ AdBlue filler cap present and blue
□ Fluid level (scan tool): _______ %
□ Fluid level (visual if tank accessible)
□ Dosing lines: any white crystal deposits?
□ Injector tip: clean or crystallized?
□ Tank heater connector: plugged in, no corrosion?
□ Any AdBlue-related DTCs stored?

NOTE: Do NOT taste or smell AdBlue unnecessarily.
It is a mild irritant — wash hands after contact.
```

---

### **WRAP-UP: Emission DTCs, Consolidation & Day 19 Preview** (Slides 26-28, ~15 minutes)

---

#### Slide 26: Emission-Related DTCs — Summary Table
**Visual:** Clean table listing the key emission DTCs covered today with their descriptions, affected systems, and typical root causes

**Instructor Narration:**
> "Let's consolidate the diagnostic trouble codes we've discussed today. These are codes you will see regularly in the workshop. P0420 is the most common catalytic converter code — but remember, always check the sensors before condemning the cat. P2002 and P2463 are the DPF codes — one for efficiency, one for soot accumulation. NOx-related codes often point to the SCR system or AdBlue quality. And the heater circuit codes for O2 and NOx sensors are some of the most frequent winter failures due to thermal cycling."

**PPT Content:**
```
EMISSION DTCs — KEY CODES FOR TECHNICIANS

CATALYTIC CONVERTER:
P0420: Catalyst Efficiency Below Threshold (Bank 1)
P0430: Catalyst Efficiency Below Threshold (Bank 2)
→ Check O2 sensors FIRST before condemning cat

O2 / LAMBDA SENSORS:
P0130-P0167: O2 sensor circuit faults (voltage, response, heater)
P0135/P0155: O2 sensor heater circuit (Bank 1/Bank 2, Sensor 1)

DPF (DIESEL PARTICULATE FILTER):
P2002: DPF Efficiency Below Threshold
P2463: DPF Soot Accumulation
→ Check differential pressure sensor, attempt forced regen

SCR / AdBlue:
P20EE: SCR NOx Catalyst Efficiency Below Threshold
P2BAD: NOx Exceeds Threshold (post-SCR)
P2047: AdBlue Injector Circuit
→ Check AdBlue level, quality, injector, NOx sensors

EGR:
P0401: EGR Insufficient Flow
P0402: EGR Excessive Flow
→ Carbon buildup, stuck valve, blocked passages
```

---

#### Slide 27: Day 18 Recap
**Visual:** Checklist with tick marks, matching the session objectives

**Instructor Narration:**
> "Let's recap what you've accomplished today. You can now trace the complete exhaust path from manifold to tailpipe. You understand how a three-way catalytic converter treats CO, HC, and NOx. You know the difference between a narrowband and wideband O2 sensor and how the ECU uses them for fuel trim and catalyst monitoring. You understand DPF construction, soot loading, and all three regeneration strategies. You can describe the SCR system and how AdBlue converts NOx to harmless nitrogen. And you've read real live data from O2 sensors and DPF on an actual vehicle.
>
> Day 16 gave you oil. Day 17 gave you coolant. Day 18 gave you exhaust. Tomorrow — Day 19 — we go back to the air side and cover the turbocharger. Turbochargers use exhaust energy to force more air into the engine, and they're now fitted to almost every new vehicle, gasoline and diesel. They're fast, fragile, and fascinating."

**PPT Content:**
```
DAY 18 RECAP — YOU CAN NOW:

[ ] Trace the complete exhaust path (manifold → tailpipe)
[ ] Explain three-way catalytic converter operation (CO, HC, NOx)
[ ] Describe diesel oxidation catalyst vs. three-way cat
[ ] Explain narrowband O2 sensor (0-1V switching)
[ ] Explain wideband O2 sensor (0-5V linear)
[ ] Describe how ECU uses O2 data for fuel trim
[ ] Explain DPF construction and soot trapping
[ ] Describe passive, active, and forced regeneration
[ ] Identify DPF sensors (differential pressure, EGT)
[ ] Explain SCR system and AdBlue dosing
[ ] Identify NOx sensor function (pre and post SCR)
[ ] Read O2 sensor live data on scan tool
[ ] Check DPF soot loading via scan tool
[ ] Recognize key emission DTCs (P0420, P2002, P2463)

WEEK 4 SO FAR:
Day 16: Oil PROTECTS — Day 17: Coolant COOLS — Day 18: Exhaust CLEANS
```

---

#### Slide 28: Day 19 Preview — Turbocharger & Forced Induction
**Visual:** Cross-section image of a turbocharger showing the turbine (exhaust side) and compressor (intake side) with arrows showing airflow

**Instructor Narration:**
> "Tomorrow is turbochargers. The turbo sits right where the exhaust manifold meets the downpipe — it's powered by the exhaust gas you learned about today. The turbine wheel spins at up to 250,000 RPM, driving a compressor wheel that forces more air into the engine. More air means more fuel, which means more power from a smaller engine. That's why almost every new car has a turbo — it's how manufacturers meet emissions targets while keeping performance acceptable.
>
> But turbos are demanding. They need clean oil at full pressure — remember Day 16? They generate enormous heat — remember Day 17? And they're in the exhaust stream — that's Day 18. Everything you've learned this week comes together inside that turbocharger. Bring your notebook."

**PPT Content:**
```
DAY 19 PREVIEW: TURBOCHARGER & FORCED INDUCTION

What you'll learn:
• How a turbocharger works (turbine + compressor)
• Wastegate and boost control
• Variable geometry turbo (VGT)
• Intercooler — why compressed air must be cooled
• Turbo failure modes and oil starvation
• Boost pressure sensor and MAP sensor data

Why it matters:
• >80% of new vehicles are turbocharged
• Turbo connects exhaust (Day 18), oil (Day 16), and cooling (Day 17)
• Common failure item — high repair cost

Bring your notebook. Wear clothes for the workshop.
```

---

## Assessment Checkpoint

**Formative (not graded):**
- Verbal knowledge check (Slide 13): four questions on catalytic converter, O2 sensors, and fuel trim
- Practical exhaust path trace: correctly identify and sequence all major exhaust components
- O2 sensor live data reading: correctly identify sensor type and interpret fuel trim values
- DPF scan tool check: correctly read and interpret soot loading and differential pressure
- Component identification: correctly locate DOC, DPF, SCR, AdBlue tank, and associated sensors on a diesel vehicle

---

## Key Takeaways

1. The exhaust system has two jobs: remove waste gas quietly and clean it chemically
2. A three-way catalytic converter treats CO, HC, and NOx — but only works at stoichiometric (lambda = 1.00)
3. The upstream O2 sensor controls fuel trim; the downstream monitors catalyst health
4. Narrowband sensors switch 0-1V (rich/lean); wideband sensors give linear 0-5V (precise lambda)
5. DPF traps diesel soot and must regenerate — passive, active, or forced
6. SCR + AdBlue converts NOx to nitrogen and water — the most effective diesel NOx solution
7. Modern diesel aftertreatment has more sensors and components than the engine itself
8. Always check sensors before condemning expensive aftertreatment components

---

## Preparation for Day 19

**Instructor prep:**
- Prepare a cutaway or sectioned turbocharger for demonstration (if available)
- Ensure a turbocharged vehicle (gasoline or diesel) is available with scan tool access to boost pressure data
- Prepare intercooler piping for inspection (check for oil residue, loose clamps)
- Print wastegate and VGT diagrams for reference
- Prepare boost leak testing equipment if available

**Learner prep:**
- Review Day 18 exhaust path — the turbo sits at the junction of exhaust and intake
- Review Day 16 oil system — turbo bearings are oil-lubricated
- Review Day 17 cooling — some turbos are water-cooled
- Wear workshop-appropriate clothing
