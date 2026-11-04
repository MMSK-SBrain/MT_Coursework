# Session 17: HVAC Systems
## Instructor-Led Story Framework for PPT Preparation

**Course:** Automotive Vehicles (AEL ZC441)
**Module 5:** Vehicle Architecture & Comfort
**Session 17 of 20**
**Duration:** 90 minutes lecture + 30 minutes Q&A
**Total Time:** 2 hours
**Approach:** Teacher-Led Narrative (System Understanding/Thermodynamics Focus)
**PPT Target:** 30 slides

---

## SESSION OVERVIEW

### Context in Course Journey
- **Previous Sessions:** Students have studied engine cooling system (Session 5), complete electrical architecture (Session 13), and chassis integration (Session 16)
- **This Session:** HVAC systems for cabin comfort - refrigeration thermodynamics, component operation, and climate control
- **Next Session:** Passive safety systems (airbags, seatbelts, crash structures)

### Session Learning Outcomes (from course-structure.md)

| SO Code | Description | Bloom Level | Type |
|---------|-------------|-------------|------|
| **AELZC441-SO-5-17-1** | Explain HVAC system fundamentals and cabin comfort requirements | Understand | Lecture |
| **AELZC441-SO-5-17-2** | Describe refrigeration thermodynamic cycle (compression, condensation, expansion, evaporation) with P-h diagram | Understand | Lecture |
| **AELZC441-SO-5-17-3** | Identify HVAC components (compressor, condenser, evaporator, expansion valve, refrigerant) and explain their operation | Understand | Lecture |
| **AELZC441-SO-5-17-4** | Compare compressor types (fixed displacement, variable displacement, electric compressor) and control mechanisms | Understand | Lecture |
| **AELZC441-SO-5-17-5** | Explain heating system operation and integration with engine cooling system (heater core) | Understand | Lecture |
| **AELZC441-SO-5-17-6** | Describe automatic climate control systems, multi-zone temperature management, cabin air quality control | Understand | Lecture |

---

## 🎬 SESSION STORY ARC

This session uses a **Teacher-Led Narrative** approach to guide students through HVAC systems - from understanding human comfort requirements to complete automatic climate control systems.

### Story Flow Summary

```
SETUP → TRIGGER → RISING ACTION → CLIMAX → RESOLUTION
Comfort  Refrigeration  HVAC          Heating &    Automatic
Needs    Cycle         Components    Integration  Control
```

**Narrative Thread:**
"Today we're going to explore one of the most important comfort systems in a vehicle - the HVAC system. I'll start by explaining what makes a cabin comfortable, then we'll dive into the fascinating physics of refrigeration. We'll build up the complete air conditioning system component by component, integrate it with the engine's heating system, and finally see how modern vehicles automatically manage climate control across multiple zones. By the end, you'll understand the complete thermal management of the passenger cabin."

---

## PART 1: SETUP - "Cabin Comfort Requirements"
**Slides 1-6 | Duration: ~12 minutes | Energy Level: High (Opening)**

**Story Purpose:** Establish why HVAC matters and define comfort parameters
**Teaching Mode:** Interactive questioning + real-world examples
**Connection to Prior Knowledge:** None required (universal human experience)

---

### SLIDE 1: Title Slide
**Visual:** Vehicle cabin interior with climate control display, temperature zones visualization
**Timing:** 1 minute

**Instructor Narrative:**
"Welcome to Session 17. Today we're tackling the HVAC system - Heating, Ventilation, and Air Conditioning. Now, I know what some of you might be thinking: 'It's just the AC, right? Turn it on when it's hot, turn on the heater when it's cold.' But I'm going to show you that automotive climate control is actually a sophisticated thermal management system with some fascinating thermodynamics. By the end of today, you'll understand the refrigeration cycle, identify every major component, and appreciate how modern automatic climate control works. Let's dive in."

**PPT Content:**
```
SESSION 17: HVAC SYSTEMS
Heating, Ventilation, and Air Conditioning

Module 5: Vehicle Architecture & Comfort
Automotive Vehicles (AEL ZC441)
```

**Outcomes Addressed:** Setting context for SO-5-17-1

---

### SLIDE 2: What Makes a Cabin Comfortable?
**Visual:** Human thermal comfort zone diagram, showing temperature and humidity ranges
**Timing:** 2 minutes

**Instructor Narrative:**
"Let me start with a question: What makes you comfortable inside a car? Temperature, obviously. But it's not just about temperature. It's about humidity - ever notice how 30°C feels different in Mumbai versus Delhi? It's about air quality - stale air makes you drowsy. It's about air velocity - a gentle breeze feels nice, but a blast from the vent can be annoying. And believe it or not, even noise matters for comfort.

So when we design an HVAC system, we're not just cooling or heating air. We're managing multiple parameters to keep occupants in their comfort zone. For most people, that's around 22-25°C cabin temperature, 40-60% relative humidity, fresh air circulation every few minutes, and gentle, quiet airflow. That's our design target."

**PPT Content:**
```
CABIN COMFORT PARAMETERS

1. Temperature: 22-25°C (ideal cabin temp)
2. Humidity: 40-60% relative humidity
3. Air Quality: Fresh air circulation, no odors/pollutants
4. Air Velocity: 0.2-0.5 m/s (gentle breeze)
5. Noise: <50 dB (quiet blower operation)

HUMAN THERMAL COMFORT ZONE
[Diagram: Temperature vs Humidity comfort envelope]
Too hot, humid → discomfort
Too cold, dry → discomfort
Comfort zone → 22-25°C, 40-60% RH
```

**Technical Details:**
- Comfort zone based on ASHRAE standards (American Society of Heating, Refrigerating and Air-Conditioning Engineers)
- Automotive adjustments: seated posture, low activity, varied clothing
- Thermal sensation scale: -3 (cold) to +3 (hot), 0 is neutral comfort

**Outcomes Addressed:** SO-5-17-1 (comfort requirements)

---

### SLIDE 3: Automotive HVAC Challenges
**Visual:** Split diagram showing summer (hot cabin) and winter (cold cabin) conditions
**Timing:** 2 minutes

**Instructor Narrative:**
"Now here's the challenge: Unlike your home AC, which operates in a relatively stable environment, automotive HVAC has to deal with extreme variability. In summer, you might park your car in the sun - cabin temperature can hit 60-70°C! That's oven-level heat. Then you start the car and expect it to cool down to 24°C in a few minutes.

In winter, it's the opposite - you start with a freezing cabin at maybe -10°C in northern regions, and you want warmth immediately. Plus, the outside ambient temperature keeps changing as you drive, from shaded areas to sunny highways. You might have one passenger who's too hot and another who's too cold. Solar radiation through the windshield heats the dashboard but not the rear seat. And all of this needs to work efficiently without draining too much engine power or battery charge.

So automotive HVAC is actually a very demanding thermal management problem."

**PPT Content:**
```
AUTOMOTIVE HVAC CHALLENGES

Summer Scenario:
• Parked in sun: Cabin temp → 60-70°C
• Soaked heat in seats, dashboard, glass
• Need rapid cooldown to 24°C in <5 minutes
• High cooling load initially

Winter Scenario:
• Cold start: Cabin temp → -10°C to 0°C
• Need rapid warmth for comfort & defogging
• Windshield defrost critical for visibility
• Limited heat available until engine warms up

Variable Conditions:
• Changing ambient temperature (0-45°C)
• Solar radiation through glass (1000 W/m²)
• Multiple occupants with different preferences
• Humidity management (prevent fogging)
• Efficiency requirement (minimize engine load/fuel penalty)
```

**Real-World Examples:**
- Black car parked in Mumbai summer: cabin can reach 70°C
- Cold start in Delhi winter: condensation on windshield is safety issue
- Highway driving: solar load through windshield heats front passengers more than rear

**Outcomes Addressed:** SO-5-17-1 (system fundamentals, challenges)

---

### SLIDE 4: HVAC System Functions
**Visual:** Three-column layout: Heating | Ventilation | Air Conditioning
**Timing:** 2 minutes

**Instructor Narrative:**
"So let's break down HVAC into its three core functions. H is for Heating - we need to raise cabin air temperature in cold conditions. That's actually the easiest part in conventional vehicles because we have waste heat from the engine that we can use. We'll see exactly how later.

V is for Ventilation - that means bringing in fresh air from outside, filtering it, and distributing it throughout the cabin. Even with windows closed, you need fresh air circulation to remove CO₂, odors, and humidity that passengers exhale. Typically we aim for about 10-15 liters per second of fresh air per person.

A is for Air Conditioning - the big one. This means cooling and dehumidifying the air. Unlike heating, cooling requires active energy input because we're moving heat against its natural flow - from the cool cabin to the hot outside. This is where thermodynamics and refrigeration come in, which we'll explore in detail in a few minutes."

**PPT Content:**
```
HVAC SYSTEM FUNCTIONS

HEATING (H)
• Raise cabin air temperature
• Source: Engine waste heat (conventional vehicles)
• Component: Heater core (small radiator in cabin)
• Winter comfort & windshield defrost

VENTILATION (V)
• Fresh air circulation from outside
• Remove CO₂, odors, humidity
• Air filtration (cabin air filter)
• Flow rate: 10-15 L/s per occupant

AIR CONDITIONING (A)
• Cool and dehumidify cabin air
• Requires active refrigeration system
• Components: Compressor, condenser, evaporator, expansion valve
• Removes ~2-5 kW heat from cabin (typical)

COMPLETE HVAC = H + V + A
All three functions integrated in one system
```

**Technical Note:**
- Cooling load calculation example: 1500 kg sedan, 70°C cabin → 24°C, ~15 kW initial load, ~3 kW steady-state
- Dehumidification is critical: moisture removal prevents window fogging

**Outcomes Addressed:** SO-5-17-1 (system fundamentals)

---

### SLIDE 5: Energy Flow: Cooling vs Heating
**Visual:** Two Sankey diagrams showing energy flow for cooling and heating
**Timing:** 2 minutes

**Instructor Narrative:**
"Before we dive into components, I want you to understand the energy flow difference between cooling and heating. This is fundamental.

For heating, we're lucky - the engine is producing massive waste heat anyway. Only about 30% of fuel energy becomes useful mechanical work; the rest is heat. Some goes out the exhaust, but about 30-40% goes into the engine coolant. So we just tap into that hot coolant, run it through a small radiator inside the cabin - called the heater core - and blow cabin air over it. Free heating! Well, free in the sense that the heat was already being generated and rejected anyway.

But for cooling, we don't have any 'free' cold source. We need to actively move heat from the cabin (cool place) to the outside (hot place), which violates the natural direction of heat flow. To do this, we need a refrigeration system that consumes mechanical power from the engine - typically 2 to 5 horsepower. This is why turning on the AC noticeably reduces engine performance in small cars and increases fuel consumption by about 10-20%.

Understanding this asymmetry is key: heating is 'free' waste heat recovery, cooling requires active power input."

**PPT Content:**
```
ENERGY FLOW: HEATING vs COOLING

HEATING (Winter Mode)
Engine → Hot Coolant (90°C) → Heater Core → Cabin Air (warm)
↑ 'Free' waste heat recovery
Fuel Energy: 100%
  → Mechanical Work: ~30%
  → Coolant Heat: ~30-40% ← WE USE THIS
  → Exhaust Heat: ~30%

COOLING (Summer Mode)
Engine → Mechanical Power → Compressor → Refrigeration Cycle
                                          ↓
Cabin Heat (removed) → Refrigerant → Outside (rejected)
↑ Active power consumption: 2-5 hp (1.5-3.5 kW)

COMPARISON
Heating: Uses waste heat (no extra fuel penalty)
Cooling: Requires mechanical work (10-20% fuel penalty when AC is on)

ELECTRIC VEHICLES
Heating: No waste heat! Must use electric heater (heat pump more efficient)
Cooling: Electric compressor (direct from battery)
Both heating & cooling reduce driving range
```

**Technical Details:**
- AC compressor power: 1.5-3.5 kW depending on cooling load
- Fuel penalty with AC on: city driving +15-20%, highway +10% (smaller % at higher speeds)
- Electric vehicle challenge: both heating and cooling drain battery (no free waste heat)

**Outcomes Addressed:** SO-5-17-1 (system fundamentals), building foundation for SO-5-17-5 (heating integration)

---

### SLIDE 6: Session Roadmap
**Visual:** Flowchart showing session structure with 5 story arc parts
**Timing:** 1 minute

**Instructor Narrative:**
"Okay, here's our roadmap for today. We've just established why HVAC matters and what challenges we face. Next, I'm going to take you through the thermodynamics of refrigeration - how we can make something cold by moving heat around. This is the core physics principle.

Then we'll build up the air conditioning system component by component: compressor, condenser, expansion valve, evaporator. You'll see how refrigerant circulates through the system, changing state from gas to liquid and back again.

After that, we'll integrate the heating side, showing how the heater core connects to the engine cooling system you studied in Session 5. We'll also compare different types of compressors - fixed, variable, and electric.

Finally, we'll see how modern vehicles use automatic climate control with multiple sensors and an ECU to manage all of this intelligently, including multi-zone temperature control and air quality management.

Let's start with the fascinating physics of refrigeration."

**PPT Content:**
```
TODAY'S ROADMAP

✓ Part 1: Cabin Comfort Requirements (Now)
  → What makes a cabin comfortable
  → Automotive HVAC challenges
  → Heating vs cooling energy flow

→ Part 2: Refrigeration Thermodynamics (Next)
  → How refrigeration works
  → P-h diagram and thermodynamic cycle
  → Refrigerant properties

→ Part 3: HVAC Components
  → Compressor, condenser, evaporator, expansion valve
  → Refrigerant circuit flow
  → Component integration

→ Part 4: Heating & Complete System
  → Heater core and engine cooling integration
  → Compressor types comparison
  → Air distribution system

→ Part 5: Automatic Climate Control
  → Sensors and ECU control
  → Multi-zone systems
  → Air quality management
```

**Outcomes Addressed:** Setting roadmap for all SOs

---

## PART 2: TRIGGER - "Refrigeration Thermodynamics"
**Slides 7-13 | Duration: ~25 minutes | Energy Level: High (Core Physics)**

**Story Purpose:** Explain the refrigeration cycle - the "magic" behind air conditioning
**Teaching Mode:** Concept explanation + thermodynamic visualization
**Connection to Prior Knowledge:** Basic thermodynamics (heat transfer, phase change)

---

### SLIDE 7: The Refrigeration Challenge
**Visual:** Diagram showing heat naturally flows hot→cold, but AC needs cold→hot
**Timing:** 2 minutes

**Instructor Narrative:**
"Alright, let's tackle the fundamental challenge of refrigeration. We know from basic thermodynamics that heat naturally flows from hot to cold. If you put a hot cup of coffee in a room, it cools down. Heat flows from the coffee to the room, never the reverse.

But in air conditioning, we want to do the opposite - we want to take heat from the cool cabin and move it to the hot outside environment. This is 'unnatural' - it requires work input. It's like pushing water uphill instead of letting it flow downhill.

So how do we do this? The answer is the refrigeration cycle, which uses a special fluid called refrigerant that can evaporate and condense at convenient temperatures. By carefully controlling where the refrigerant evaporates and where it condenses, we can move heat from inside the cabin to outside.

Here's the key insight: when a liquid evaporates, it absorbs heat. When a vapor condenses, it releases heat. We evaporate the refrigerant inside the cabin - it absorbs cabin heat, cooling the air. We condense it outside - it releases that heat to the atmosphere. Brilliant, right?"

**PPT Content:**
```
THE REFRIGERATION CHALLENGE

Natural Heat Flow:
HOT → COLD (spontaneous, no work required)
Example: Hot coffee cools in a room

Air Conditioning Requirement:
COOL CABIN → HOT OUTSIDE (against natural flow!)
Requires WORK INPUT (compressor)

Solution: REFRIGERATION CYCLE
Use a working fluid (refrigerant) that:
• Evaporates at low temperature → Absorbs heat
• Condenses at high temperature → Releases heat

Key Principle:
Evaporation (liquid → gas): Absorbs heat (endothermic)
Condensation (gas → liquid): Releases heat (exothermic)

Example:
Water evaporating from your skin → You feel cool (heat absorbed)
Steam condensing on mirror → Mirror gets hot (heat released)

Refrigeration Cycle Insight:
Evaporate refrigerant INSIDE cabin → Absorbs cabin heat → Cooling
Condense refrigerant OUTSIDE vehicle → Releases heat to atmosphere
```

**Analogy:**
"Think of the refrigerant as a heat courier. It picks up heat inside the cabin during evaporation, carries it outside, and drops it off during condensation. Then it returns inside to pick up more heat. It's a continuous cycle."

**Outcomes Addressed:** SO-5-17-2 (refrigeration cycle principles)

---

### SLIDE 8: The Refrigeration Cycle Overview
**Visual:** Circular flow diagram showing 4 processes: Compression → Condensation → Expansion → Evaporation
**Timing:** 3 minutes

**Instructor Narrative:**
"Now let me show you the complete refrigeration cycle. It has four key processes that repeat continuously.

First: Compression. We take low-pressure refrigerant vapor and compress it using a compressor driven by the engine. Compression raises both the pressure and temperature of the refrigerant. This is where we put work into the system.

Second: Condensation. The hot, high-pressure vapor flows through the condenser - a heat exchanger at the front of the vehicle. Ambient air flowing over the condenser cools the refrigerant below its boiling point at this high pressure, so it condenses into a liquid. Heat is released to the outside air during this phase change.

Third: Expansion. The high-pressure liquid then passes through an expansion valve, which is basically a controlled restriction. As the liquid squeezes through, its pressure drops dramatically. This is called throttling. The temperature also drops due to the pressure reduction.

Fourth: Evaporation. The low-pressure, low-temperature liquid enters the evaporator - a heat exchanger inside the cabin. Cabin air blown over the evaporator heats the refrigerant, causing it to evaporate back into a vapor. This evaporation absorbs heat from the cabin air, which is how we get cooling!

Then the cycle repeats: the low-pressure vapor goes back to the compressor, and around we go again."

**PPT Content:**
```
THE REFRIGERATION CYCLE (4 Processes)

     ┌──────────────────────────────────────┐
     │                                      │
  Compressor                            Evaporator
     │                                      ↑
     ↓                                      │
  Condenser ─────→ Expansion Valve ─────────┘

1. COMPRESSION (Compressor)
   Low-pressure vapor → High-pressure vapor
   Work input: ~2-4 kW (from engine/electric motor)
   Temperature rises: ~60°C → ~80-90°C
   Pressure rises: 2-3 bar → 12-18 bar

2. CONDENSATION (Condenser)
   High-pressure vapor → High-pressure liquid
   Heat rejection: Released to outside air (~3-6 kW)
   Temperature drops: ~80°C → ~50-60°C (ambient + margin)
   Phase change: Gas → Liquid

3. EXPANSION (Expansion Valve)
   High-pressure liquid → Low-pressure liquid
   Throttling process (isenthalpic)
   Pressure drops: 12-18 bar → 2-3 bar
   Temperature drops: ~50°C → ~5°C

4. EVAPORATION (Evaporator)
   Low-pressure liquid → Low-pressure vapor
   Heat absorption: Absorbs cabin heat (~2-5 kW)
   Temperature rises slightly: ~5°C → ~10°C
   Phase change: Liquid → Gas

Then back to compressor → Cycle repeats
```

**Teaching Tip:**
"I'll often use the analogy of a heat pump. We're pumping heat uphill from the cool cabin to the hot outside, just like a water pump pushes water uphill."

**Outcomes Addressed:** SO-5-17-2 (refrigeration cycle description)

---

### SLIDE 9: Pressure-Enthalpy (P-h) Diagram
**Visual:** P-h diagram for R134a refrigerant showing the 4 processes
**Timing:** 4 minutes

**Instructor Narrative:**
"Now I want to show you the professional way to visualize the refrigeration cycle: the Pressure-Enthalpy diagram, or P-h diagram. This might look intimidating at first, but it's actually an incredibly useful tool. Let me walk you through it.

The vertical axis is pressure in bar - notice it's a log scale. The horizontal axis is specific enthalpy in kJ/kg, which is essentially the energy content of the refrigerant per unit mass.

You see these dome-shaped lines? The one on the left is the saturated liquid line, the one on the right is the saturated vapor line. Inside the dome, you have a mixture of liquid and vapor - two-phase region. To the left of the dome is pure liquid, to the right is superheated vapor.

Now, let's plot our refrigeration cycle on this diagram. We start at Point 1: low pressure, low temperature vapor coming from the evaporator.

The compressor raises the pressure and temperature - we move upward vertically (actually slightly to the right due to entropy increase) to Point 2: high pressure, high temperature vapor.

In the condenser, the vapor cools and condenses at constant high pressure, moving leftward along a horizontal line from Point 2 to Point 3. We cross the two-phase dome and end up with high-pressure liquid.

The expansion valve throttles the liquid - pressure drops rapidly, moving downward to Point 4. This is approximately a constant enthalpy process (vertical drop on P-h diagram).

Finally, in the evaporator, the liquid absorbs heat and evaporates at constant low pressure, moving rightward along a horizontal line back to Point 1.

The area enclosed by this cycle represents the cooling effect. The height of the cycle represents the pressure lift the compressor must provide. It's all there in one elegant diagram."

**PPT Content:**
```
PRESSURE-ENTHALPY (P-h) DIAGRAM

[Diagram showing P-h plot with 4 processes marked]

Axes:
• Vertical: Pressure (bar) - Log scale
• Horizontal: Specific Enthalpy (kJ/kg) - Energy content

Key Lines:
• Saturated liquid line (left dome edge)
• Saturated vapor line (right dome edge)
• Two-phase region (inside dome): Mix of liquid + vapor
• Subcooled liquid (left of dome)
• Superheated vapor (right of dome)

REFRIGERATION CYCLE on P-h Diagram:

Point 1 (Evaporator exit): P_low = 2-3 bar, T ≈ 5-10°C, vapor
  ↓ COMPRESSION (compressor work input)
Point 2 (Compressor exit): P_high = 15 bar, T ≈ 80-90°C, superheated vapor
  ↓ CONDENSATION (heat rejection, constant pressure)
Point 3 (Condenser exit): P_high = 15 bar, T ≈ 50°C, subcooled liquid
  ↓ EXPANSION (throttling, isenthalpic)
Point 4 (Expansion valve exit): P_low = 2-3 bar, T ≈ 5°C, two-phase mixture
  ↓ EVAPORATION (heat absorption, constant pressure)
Point 1 (back to start)

Cooling Effect (Q_evap):
Enthalpy increase in evaporator = h1 - h4 (kJ/kg)

Work Input (W_comp):
Enthalpy increase in compressor = h2 - h1 (kJ/kg)

COP (Coefficient of Performance):
COP = Q_evap / W_comp = (h1 - h4) / (h2 - h1)
Typical automotive AC: COP ≈ 2-3
```

**Teaching Note:**
- Students don't need to memorize exact values, but should understand the shape and flow
- Emphasize: High pressure in condenser, low pressure in evaporator
- Phase changes occur at constant pressure (horizontal lines)

**Outcomes Addressed:** SO-5-17-2 (P-h diagram, thermodynamic cycle)

---

### SLIDE 10: Refrigerant Properties
**Visual:** Comparison table of R134a vs R1234yf refrigerants
**Timing:** 3 minutes

**Instructor Narrative:**
"Now, what exactly is this refrigerant we keep talking about? It's a special chemical compound chosen for very specific thermodynamic properties. For decades, automotive air conditioning used R12 (dichlorodifluoromethane), but that was phased out in the 1990s because it damages the ozone layer.

It was replaced by R134a (tetrafluoroethane), which became the industry standard from the mid-1990s to around 2015. R134a has good thermodynamic properties - it boils at -26°C at atmospheric pressure, which means at cabin pressure of 2-3 bar, it boils at around 0-10°C, perfect for air conditioning. It's also non-toxic and non-flammable, which is critical for safety.

However, R134a has a high Global Warming Potential - if it leaks, it's 1,430 times worse than CO₂ as a greenhouse gas over 100 years. So European regulations pushed for a replacement.

Enter R1234yf (tetrafluoropropene), which has been mandatory in new EU vehicles since 2017. Its GWP is only 4 - essentially equivalent to CO₂. The thermodynamic properties are very similar to R134a, so the same system architecture works. The main differences are cost - R1234yf is more expensive - and a slight flammability concern, though in practice the risk is very low.

The key point is that the refrigeration cycle and components remain essentially the same regardless of which refrigerant you use. The refrigerant is just the working fluid."

**PPT Content:**
```
REFRIGERANT PROPERTIES

Historical Evolution:
R12 (CFC) → Phased out 1990s (ozone depletion)
R134a (HFC) → Industry standard 1995-2017
R1234yf (HFO) → EU mandatory since 2017 (low GWP)

R134a (Tetrafluoroethane) - Legacy Standard
• Chemical formula: CH₂FCF₃
• Boiling point at 1 atm: -26.3°C
• Operating pressure range: 2-18 bar (typical AC cycle)
• Global Warming Potential (GWP): 1,430 (high!)
• Ozone Depletion Potential (ODP): 0 (safe for ozone)
• Safety: Non-toxic, non-flammable
• Cost: Moderate (₹300-500/kg)

R1234yf (Tetrafluoropropene) - Current Standard
• Chemical formula: CF₃CF=CH₂
• Boiling point at 1 atm: -29.5°C
• Operating pressure range: 2-18 bar (similar to R134a)
• Global Warming Potential (GWP): <1 (very low!)
• Ozone Depletion Potential (ODP): 0
• Safety: Non-toxic, mildly flammable (low risk)
• Cost: High (₹2,000-3,000/kg) - patent-protected

Key Requirements for Automotive Refrigerant:
✓ Suitable boiling point for AC temperature range
✓ High latent heat of vaporization (more cooling per kg)
✓ Safe (non-toxic, low flammability)
✓ Chemically stable (won't decompose)
✓ Compatible with lubricants and materials
✓ Low environmental impact (GWP, ODP)

System Design:
Same components work for both R134a and R1234yf
Refrigerant charge quantity: ~400-800 grams (typical sedan)
```

**Real-World Context:**
- EU Directive 2006/40/EC mandated GWP <150 for new vehicles from 2017
- India mostly still uses R134a (as of 2024), gradual transition to R1234yf
- System must be designed to minimize leaks (both for performance and environment)

**Outcomes Addressed:** SO-5-17-2 (refrigerant properties), SO-5-17-3 (component identification prep)

---

### SLIDE 11: Phase Change and Cooling Effect
**Visual:** Molecular-level animation showing liquid evaporation absorbing energy
**Timing:** 3 minutes

**Instructor Narrative:**
"I want to zoom in on why evaporation cools. This is fundamental to understanding the evaporator.

At the molecular level, temperature is just the average kinetic energy of molecules. In a liquid, molecules are bonded together weakly. To break free and become a gas, a molecule needs energy - specifically, the latent heat of vaporization.

When refrigerant evaporates inside the evaporator, each molecule that escapes the liquid phase must absorb energy to overcome the intermolecular forces. Where does this energy come from? From the cabin air blowing over the evaporator!

This is the cooling effect: the refrigerant steals energy from the cabin air as it evaporates. The cabin air loses energy, so its temperature drops - you feel cold air from the vents.

For R134a, the latent heat is about 217 kJ/kg at typical evaporator conditions. That means for every kilogram of refrigerant that evaporates, we remove 217 kilojoules of heat from the cabin. If we circulate, say, 10 grams per second of refrigerant through the system, that's 217 × 0.01 = 2.17 kW of cooling. That's enough to cool a small sedan in steady-state conditions.

The beauty of using phase change is that we get a large amount of cooling (latent heat) at a nearly constant temperature. That's why refrigeration is so effective compared to just blowing air over ice, for example."

**PPT Content:**
```
PHASE CHANGE & COOLING EFFECT

Molecular View of Evaporation:
Liquid molecules: Weakly bonded, vibrating
→ Energy input: Overcome intermolecular forces
→ Gas molecules: Free to move, high kinetic energy

Latent Heat of Vaporization:
Energy required to change phase (liquid → gas) at constant temperature
R134a: ΔH_vap ≈ 217 kJ/kg (at evaporator conditions)
This is MUCH larger than specific heat (sensible cooling)

Cooling Effect Calculation:
Q_cooling = ṁ × ΔH_vap
Where:
• Q_cooling = Cooling power (kW)
• ṁ = Refrigerant mass flow rate (kg/s)
• ΔH_vap = Latent heat of vaporization (kJ/kg)

Example:
Refrigerant flow rate: ṁ = 0.01 kg/s (10 g/s)
Latent heat: ΔH_vap = 217 kJ/kg
Cooling power: Q = 0.01 × 217 = 2.17 kW ✓

Comparison:
Latent heat (phase change): 217 kJ/kg
Sensible heat (temperature change): ~1.4 kJ/(kg·°C)
→ Phase change gives ~150x more cooling per degree!

Why This Matters:
Evaporator absorbs LARGE amounts of heat with SMALL temperature change
→ Efficient, compact cooling
```

**Visual Aid:**
Show animation of molecules escaping liquid surface, with "energy arrows" being absorbed from surroundings.

**Outcomes Addressed:** SO-5-17-2 (thermodynamic cycle), foundation for SO-5-17-3 (evaporator operation)

---

### SLIDE 12: Compression Work and COP
**Visual:** Energy flow diagram showing compressor work input vs cooling output
**Timing:** 3 minutes

**Instructor Narrative:**
"Now let's talk about efficiency. We put work into the compressor - that's energy we're spending, either from the engine or the battery in an EV. In return, we get cooling. How efficient is this process?

The metric we use is called COP - Coefficient of Performance. It's simply the ratio of cooling output to work input. For automotive air conditioning, COP is typically around 2 to 3. That means for every 1 kW of compressor work, we get 2-3 kW of cooling.

Wait, you might think - that's more than 100% efficient! How is that possible? The key is that we're not creating cold energy, we're moving heat. The compressor work helps move heat from inside to outside. The total heat rejected to the condenser is actually the cabin heat we absorbed PLUS the compressor work. Energy is conserved, don't worry.

A COP of 3 means we remove 3 kW of cabin heat by putting in 1 kW of compressor work. We dump 4 kW to the condenser. From the cabin's perspective, we got 3 kW of cooling benefit for 1 kW of cost - that's why COP is a useful metric.

Now, COP is not constant. It depends on operating conditions. If the outside temperature is very high, the condenser has to work harder, and COP drops. If you're asking for extremely cold cabin air, the evaporator temperature drops, pressure ratio increases, and COP drops. Optimal COP is when temperature difference between inside and outside is moderate."

**PPT Content:**
```
COMPRESSION WORK & COP

Compressor Work:
W_comp = ṁ × (h2 - h1)
Where:
• h2 = Enthalpy after compression (kJ/kg)
• h1 = Enthalpy before compression (kJ/kg)
• ṁ = Refrigerant mass flow rate (kg/s)

Typical compressor power: 2-4 kW (automotive AC)

Cooling Effect:
Q_evap = ṁ × (h1 - h4)
Typical cooling power: 3-8 kW (depends on conditions)

COP (Coefficient of Performance):
COP = Q_evap / W_comp = Cooling Output / Work Input

Typical automotive AC COP: 2.0 - 3.0

Example:
Compressor work: W = 2 kW
Cooling output: Q = 5 kW
COP = 5 / 2 = 2.5 ✓

Energy Balance (Conservation):
Heat rejected at condenser: Q_cond = Q_evap + W_comp
Example: Q_cond = 5 + 2 = 7 kW
This 7 kW is dumped to outside air via condenser

Factors Affecting COP:
• Outside temperature ↑ → COP ↓ (harder to reject heat)
• Desired cabin temp ↓ → COP ↓ (larger temperature lift)
• Compressor efficiency (mechanical losses reduce COP)
• Refrigerant charge level (undercharged or overcharged reduces COP)

Comparison to Home AC:
Home AC COP: 3-4 (higher, more stable conditions)
Automotive AC COP: 2-3 (lower, variable conditions, size constraints)
```

**Teaching Note:**
COP > 1 is normal for heat pumps/refrigeration because we're moving heat, not creating it. Don't confuse with thermal efficiency (η < 1 always).

**Outcomes Addressed:** SO-5-17-2 (refrigeration cycle, thermodynamic understanding)

---

### SLIDE 13: Summary: Refrigeration Cycle
**Visual:** Integrated diagram with all 4 processes, P-h plot, and energy flows
**Timing:** 2 minutes

**Instructor Narrative:**
"Let's recap the refrigeration thermodynamics before we move to components. The refrigeration cycle has four processes:

Compression - we put work in to raise pressure and temperature of refrigerant vapor. This is the energy input to the system.

Condensation - the hot vapor releases heat to the outside air and condenses into liquid at high pressure. This is where we dump the cabin heat.

Expansion - the high-pressure liquid throttles through a valve, dropping in pressure and temperature.

Evaporation - the cold liquid absorbs heat from the cabin air and evaporates back into vapor. This is where the cooling happens.

The P-h diagram shows us the cycle visually. The refrigerant properties determine the specific pressures and temperatures. And the COP tells us how efficiently we're moving heat.

Now that you understand the thermodynamics, we can move to the actual hardware that makes this happen."

**PPT Content:**
```
REFRIGERATION CYCLE SUMMARY

4 Processes:
1. COMPRESSION (Compressor) - Work input, pressure ↑, temp ↑
2. CONDENSATION (Condenser) - Heat rejection, gas → liquid
3. EXPANSION (Expansion valve) - Pressure ↓, temp ↓
4. EVAPORATION (Evaporator) - Heat absorption, liquid → gas

P-h Diagram:
Visualizes the cycle: High-pressure side (condenser) vs Low-pressure side (evaporator)
Phase changes at constant pressure

Refrigerant:
Working fluid: R134a (legacy) or R1234yf (current)
Latent heat provides large cooling effect

Efficiency:
COP = Cooling / Work ≈ 2-3 (typical automotive)

Next: Let's see the actual components!
```

**Outcomes Addressed:** SO-5-17-2 (complete)

---

## PART 3: RISING ACTION - "HVAC Components"
**Slides 14-19 | Duration: ~20 minutes | Energy Level: Medium (Building Complexity)**

**Story Purpose:** Identify each component and understand its operation
**Teaching Mode:** Component-by-component explanation with visuals
**Connection to Prior Knowledge:** Refrigeration cycle from Part 2

---

### SLIDE 14: HVAC System Layout
**Visual:** Complete automotive HVAC schematic showing all components and refrigerant flow
**Timing:** 3 minutes

**Instructor Narrative:**
"Alright, now let's see the complete HVAC system layout. This is what you'd find under the hood and inside the cabin of a modern car.

Starting at the engine, we have the compressor - usually belt-driven from the engine crankshaft, though newer cars may use an electric compressor. The compressor pumps refrigerant vapor and sends it through a high-pressure line to the condenser.

The condenser sits at the very front of the vehicle, right ahead of the engine radiator. It's a large heat exchanger that looks like a radiator. As you drive, ram air flows through the condenser fins, cooling the hot refrigerant. When you're stationary, a cooling fan forces air through it.

From the condenser, high-pressure liquid refrigerant flows through the liquid line to the expansion valve, which is usually located near the evaporator inside the cabin.

The evaporator is hidden inside the HVAC module behind the dashboard. It's another heat exchanger, but this time cabin air is blown over it by the blower motor. The cold evaporator surface cools and dehumidifies the air, which then comes out through your vents.

Finally, low-pressure vapor exits the evaporator and returns to the compressor through the suction line, completing the loop.

Notice there are two sides to this system: the high-pressure side from compressor discharge to expansion valve, and the low-pressure side from expansion valve through evaporator back to compressor suction. We'll examine each component in detail now."

**PPT Content:**
```
HVAC SYSTEM LAYOUT

[Complete schematic diagram showing]

COMPONENTS:

HIGH-PRESSURE SIDE (Hot, 12-18 bar):
1. Compressor (engine-driven or electric)
2. Discharge line (high-pressure vapor)
3. Condenser (front of vehicle, with cooling fan)
4. Receiver-dryer (filter/moisture removal)
5. Liquid line (high-pressure liquid)

LOW-PRESSURE SIDE (Cold, 2-3 bar):
6. Expansion valve (TXV or orifice tube)
7. Evaporator (inside cabin HVAC module)
8. Suction line (low-pressure vapor)
9. Back to compressor

ADDITIONAL COMPONENTS:
• Blower motor (cabin air circulation)
• Cabin air filter
• Blend door (temperature control)
• Mode doors (vent direction control)
• Heater core (heating function)

REFRIGERANT FLOW PATH:
Compressor → Condenser → Receiver-dryer → Expansion valve
→ Evaporator → Compressor (loop)

PHYSICAL LOCATIONS:
• Engine bay: Compressor, condenser, receiver-dryer
• Inside cabin (behind dashboard): Evaporator, expansion valve, HVAC module
• Throughout vehicle: Refrigerant lines (insulated)

Pressures:
High side: 12-18 bar (depends on ambient temp, ~15 bar typical)
Low side: 2-3 bar (depends on evaporator temp, ~2.5 bar typical)
```

**Safety Note:**
High-pressure refrigerant lines are labeled with warning stickers. System must be professionally serviced - releasing refrigerant is illegal and harmful to environment.

**Outcomes Addressed:** SO-5-17-3 (component identification, system overview)

---

### SLIDE 15: Component 1 - Compressor
**Visual:** Cutaway view of automotive AC compressor with labeled parts
**Timing:** 3 minutes

**Instructor Narrative:**
"Let's start with the heart of the system: the compressor. Its job is simple - take low-pressure refrigerant vapor from the evaporator and compress it to high pressure. But the implementation is quite sophisticated.

Most traditional cars use a belt-driven compressor connected to the engine crankshaft via an accessory belt - the same belt system that drives the alternator. But unlike the alternator which always runs when the engine runs, the compressor has an electromagnetic clutch. When you press the AC button, the clutch engages and couples the compressor pulley to the compressor shaft. When you turn AC off, the clutch disengages - the pulley keeps spinning but the compressor shaft stops, saving engine power.

Inside the compressor, you typically find multiple pistons arranged radially or axially. As the shaft rotates, these pistons reciprocate, drawing in low-pressure vapor through inlet valves, compressing it, and pushing it out through discharge valves. It's similar in principle to an engine, but in reverse - we're putting work in, not getting work out.

The compressor also contains oil for lubrication. This oil circulates with the refrigerant throughout the system, which is why you must use refrigerant-compatible oil.

Compressor power consumption varies with load. At maximum cooling demand - hot day, cabin temperature high - the compressor might draw 3-4 kW from the engine. In mild conditions with the cabin already cool, it might cycle on and off, averaging maybe 1-2 kW.

We'll compare different compressor types in a later slide."

**PPT Content:**
```
COMPONENT 1: COMPRESSOR

Function:
Compress low-pressure vapor → high-pressure vapor
Provides pressure lift for refrigerant circulation
Work input to the refrigeration cycle

Location: Engine bay, belt-driven from crankshaft

Key Components:
• Compressor pulley (always rotating with belt)
• Electromagnetic clutch (engages/disengages compressor)
• Compressor shaft
• Pistons (reciprocating or scroll mechanism)
• Inlet and discharge valves
• Oil sump (lubrication)

Operation:
1. AC button pressed → Clutch engages
2. Pulley couples to compressor shaft
3. Shaft rotation → Pistons compress refrigerant
4. Low-pressure inlet: ~2-3 bar, ~10°C vapor
5. High-pressure discharge: ~15 bar, ~80°C vapor
6. AC button off → Clutch disengages, compressor stops

Types (Overview - details later):
• Fixed displacement (piston type)
• Variable displacement (swash plate angle varies)
• Scroll compressor (spiral compression)
• Electric compressor (no belt, motor-driven)

Power Consumption:
• Maximum load: 3-4 kW
• Moderate load: 1.5-2.5 kW
• Cycles on/off or varies displacement based on demand

Clutch Cycling:
When cabin reaches target temp → Compressor clutch disengages → Saves fuel
If temp rises → Clutch re-engages
Cycling frequency: Every 30-60 seconds (typical)
```

**Real-World Example:**
"When you're idling at a traffic light with AC on in a small car, you can actually feel the engine load change when the compressor clutch engages - RPM might drop slightly, and you hear the click of the clutch."

**Outcomes Addressed:** SO-5-17-3 (compressor identification and operation)

---

### SLIDE 16: Component 2 - Condenser
**Visual:** Condenser heat exchanger with airflow diagram
**Timing:** 3 minutes

**Instructor Narrative:**
"After the compressor, hot high-pressure vapor flows to the condenser. The condenser's job is to reject heat to the outside air and condense the vapor into liquid.

The condenser is always located at the very front of the vehicle, ahead of the engine's radiator. Why? Because it needs maximum airflow. When you're driving, ram air flows through the condenser - this is forced convection cooling. The condenser fins increase surface area to maximize heat transfer.

When you're stopped in traffic, there's no ram air. So there's a dedicated condenser fan (or the radiator fan also serves the condenser) that switches on to force airflow. This is why you sometimes hear a fan running even when the engine is off but AC was recently on - the system is still rejecting heat.

The condenser is essentially a long tube with fins, arranged in a serpentine pattern. Hot refrigerant vapor enters at the top. As it flows through the tube with outside air flowing over the fins, it loses heat. First it cools as superheated vapor, then it reaches the saturation temperature and starts condensing - this is where most of the heat rejection happens because latent heat is released. By the time it exits at the bottom, it's subcooled liquid, a few degrees below the condensation temperature.

Typical heat rejection at the condenser is 3-7 kW depending on cooling load. That's a lot of heat! On a hot day with AC running full blast, the air coming off the condenser can be 10-15°C hotter than ambient."

**PPT Content:**
```
COMPONENT 2: CONDENSER

Function:
Reject heat from refrigerant to outside air
Condense high-pressure vapor → high-pressure liquid
Phase change: Gas → Liquid

Location: Front of vehicle (ahead of radiator)

Construction:
• Aluminum tubes (refrigerant flow path)
• Aluminum fins (increase surface area)
• Multi-pass serpentine layout
• Inlet: Top (hot vapor)
• Outlet: Bottom (subcooled liquid)

Heat Transfer Process:
1. Inlet: Superheated vapor (~80-90°C, 15 bar)
2. Desuperheating: Vapor cools to saturation temp (~55°C)
3. Condensation: Vapor → Liquid at constant temp (MAJOR heat release)
4. Subcooling: Liquid cools below saturation (~50°C)
5. Outlet: Subcooled liquid ready for expansion valve

Heat Rejection:
Q_cond = Q_evap + W_comp (energy balance)
Typical: 4-8 kW (varies with conditions)

Airflow:
• Moving vehicle: Ram air (natural convection)
• Stationary: Condenser fan (forced convection)
• Airflow rate: ~2000-5000 m³/hr
• Air temp rise across condenser: +10-15°C

Why Front Location?
• Maximum airflow when driving
• First heat exchanger (cleanest air)
• Trade-off: Exposed to road debris, impacts

Failure Modes:
• Fin damage from rocks/debris → Reduced heat rejection
• Internal corrosion → Leaks
• Blockage → High pressure, poor cooling
```

**Visual Note:**
Show thermal image of condenser - hot inlet at top, progressively cooler toward bottom.

**Outcomes Addressed:** SO-5-17-3 (condenser identification and operation)

---

### SLIDE 17: Component 3 - Expansion Valve
**Visual:** Thermostatic expansion valve (TXV) cross-section and operation
**Timing:** 3 minutes

**Instructor Narrative:**
"Now we come to a small but critical component: the expansion valve. This is the device that creates the pressure drop between the high-pressure liquid from the condenser and the low-pressure liquid entering the evaporator.

There are two common types in automotive systems. The traditional one is the Thermostatic Expansion Valve, or TXV. The modern alternative is a simple Orifice Tube.

Let's talk about the TXV first. It's a spring-loaded valve with a temperature-sensing bulb. The bulb is attached to the evaporator outlet and senses the temperature of the vapor leaving the evaporator - this is called the superheat. The valve automatically adjusts its opening to maintain a specific superheat, typically 5-10°C.

Here's why that matters: we want the refrigerant to completely evaporate inside the evaporator - we don't want liquid droplets reaching the compressor because liquids don't compress, they can damage the compressor. But we also don't want too much superheat because that means we're not using the full evaporator surface for phase change cooling. The TXV finds the perfect balance.

When the superheat is too low - meaning we're almost sending liquid to the compressor - the valve closes slightly, reducing refrigerant flow to the evaporator. When superheat is too high - meaning we're wasting evaporator capacity - the valve opens more. It's a mechanical feedback control.

The orifice tube, on the other hand, is just a fixed restriction - a small hole. It's simpler and cheaper, but it doesn't adapt to varying conditions. Cars with orifice tubes typically use an accumulator after the evaporator to trap any liquid refrigerant before it reaches the compressor.

Either way, the result is the same: high-pressure liquid suddenly expands through a restriction, pressure drops from 15 bar to 2-3 bar, and temperature drops from 50°C to about 5°C. The refrigerant is now a cold, low-pressure mixture of liquid and vapor, ready to enter the evaporator."

**PPT Content:**
```
COMPONENT 3: EXPANSION VALVE

Function:
Create pressure drop from high-pressure to low-pressure side
Meter refrigerant flow to evaporator
Control superheat to protect compressor

Location: Just before evaporator (inside cabin HVAC module)

TYPE 1: Thermostatic Expansion Valve (TXV)

Construction:
• Valve body with inlet (high P) and outlet (low P)
• Needle valve and seat (variable orifice)
• Sensing bulb attached to evaporator outlet
• Spring opposing bulb pressure

Operation:
1. Sensing bulb monitors evaporator outlet temperature
2. Bulb contains refrigerant that expands when warm
3. Bulb pressure pushes needle open
4. Spring pressure pushes needle closed
5. Valve modulates to maintain target superheat (~5-10°C)

Superheat Control:
Superheat = T_outlet - T_saturation
Too low (<3°C) → Risk of liquid to compressor → Valve closes
Too high (>15°C) → Wasted evaporator capacity → Valve opens
TXV automatically balances

TYPE 2: Orifice Tube (Fixed Orifice)

Construction:
• Simple fixed-size orifice (hole)
• Filter screen
• No moving parts

Operation:
• Fixed restriction, no modulation
• Simpler, cheaper, more reliable
• Requires accumulator after evaporator to trap liquid

Thermodynamic Process:
Process: Throttling (isenthalpic expansion)
P_in: ~15 bar (high-pressure liquid)
T_in: ~50°C
P_out: ~2.5 bar (low-pressure two-phase)
T_out: ~5°C
Enthalpy: h_in = h_out (no heat exchange, no work)
Result: Pressure drop causes temperature drop

Why Pressure Drop = Temperature Drop?
As pressure decreases, some liquid flashes to vapor (evaporates)
Evaporation absorbs energy from remaining liquid
→ Bulk temperature drops
```

**Analogy:**
"Think of shaking a can of compressed air and feeling it get cold. Same principle - rapid pressure drop causes cooling."

**Outcomes Addressed:** SO-5-17-3 (expansion valve identification and operation)

---

### SLIDE 18: Component 4 - Evaporator
**Visual:** Evaporator core with airflow and condensate drainage
**Timing:** 3 minutes

**Instructor Narrative:**
"Finally we reach the evaporator - the component you actually feel the benefit from. The evaporator is where the magic happens: cold refrigerant absorbs heat from cabin air, giving you that blessed cool breeze on a hot day.

The evaporator is located inside the HVAC module behind the dashboard. You can't see it without disassembling the dash, but it's there - a compact heat exchanger about the size of a car radiator but smaller.

It looks similar to the condenser but works in reverse. Cold, low-pressure refrigerant enters at the bottom as a mixture of liquid and vapor. As it flows through the evaporator tubes, cabin air blown by the blower motor passes over the fins. Heat transfers from the warm cabin air to the cold refrigerant.

This heat causes the liquid refrigerant to evaporate - phase change from liquid to gas. Remember, evaporation absorbs latent heat. By the time the refrigerant exits at the top, it should be fully vaporized plus a bit of superheat. Typical evaporator outlet temperature is around 5-10°C.

The cabin air, meanwhile, is cooled. Air enters the evaporator at maybe 30-35°C and exits at 8-12°C. That's a 20°C+ temperature drop!

But cooling isn't the only benefit. The evaporator also dehumidifies. When warm, humid air contacts the cold evaporator surface below the dew point, water vapor condenses into liquid droplets - just like moisture forming on a cold drink glass. This moisture drips off the evaporator fins and drains out through a tube under the car - that's why you see water puddles under parked cars with AC running.

Dehumidification is crucial for comfort and for defogging windows. Removing moisture prevents that clammy feeling and improves visibility."

**PPT Content:**
```
COMPONENT 4: EVAPORATOR

Function:
Absorb heat from cabin air
Evaporate low-pressure liquid → low-pressure vapor
Cool and dehumidify cabin air

Location: Inside HVAC module (behind dashboard)

Construction:
• Aluminum tubes (refrigerant flow)
• Aluminum fins (air-side heat transfer)
• Inlet: Bottom (low-pressure two-phase mixture)
• Outlet: Top (low-pressure vapor, slightly superheated)
• Condensate drain tube (remove water)

Refrigerant-Side Process:
1. Inlet: Two-phase mixture (~5°C, 2.5 bar, ~30% vapor)
2. Evaporation: Liquid → Vapor as heat absorbed
3. Outlet: Superheated vapor (~10°C, 2.5 bar, 100% vapor)
4. Heat absorbed: Q_evap = ṁ × ΔH_vap (~3-6 kW)

Air-Side Process:
1. Inlet: Warm cabin air (~30-35°C, relative humidity ~50-70%)
2. Cooling: Air temperature drops to ~8-12°C
3. Dehumidification: Water vapor condenses on cold fins
4. Outlet: Cool, dry air to cabin vents

Dehumidification:
When air temp drops below dew point → Moisture condenses
Condensate drips to drain pan → Drains outside vehicle
Dehumidification rate: ~100-300 ml/hr (typical)
Benefits:
  • Prevents clammy/sticky feeling
  • Defogs windshield (dry air prevents condensation)
  • Improves perceived cooling (dry air feels cooler)

Evaporator Temperature Control:
Must stay above freezing (~3-5°C minimum)
If too cold → Ice forms on fins → Blocks airflow
Cycling clutch or variable compressor prevents ice formation

Cooling Capacity:
Typical sedan: 3-5 kW steady-state
Initial cool-down: 6-8 kW peak
Dependent on:
  • Refrigerant flow rate
  • Evaporator surface area
  • Air flow rate (blower speed)
  • Temperature difference
```

**Real-World Note:**
"That water dripping under your parked car? It's from the evaporator condensate. Completely normal. If you DON'T see it on a humid day with AC running, your drain might be clogged."

**Outcomes Addressed:** SO-5-17-3 (evaporator identification and operation)

---

### SLIDE 19: Refrigerant Circuit Integration
**Visual:** Complete circuit diagram with pressures, temperatures, and phase states labeled
**Timing:** 3 minutes

**Instructor Narrative:**
"Let's bring it all together. Here's the complete refrigerant circuit with all the key parameters labeled at each point.

Starting at the compressor inlet: we have low-pressure vapor at about 2.5 bar and 10°C coming from the evaporator. The compressor compresses it to high-pressure, high-temperature vapor - 15 bar, 85°C.

This hot vapor flows to the condenser where it cools and condenses. At the condenser outlet, we have high-pressure liquid at about 15 bar and 50°C - subcooled a bit below the condensation temperature.

This liquid then throttles through the expansion valve. Pressure drops from 15 bar to 2.5 bar, temperature drops from 50°C to 5°C, and we get a two-phase mixture.

Finally, this cold mixture enters the evaporator. It absorbs cabin heat and fully evaporates, exiting as low-pressure vapor at 10°C, which returns to the compressor.

Notice the refrigerant is always moving in one direction, driven by the compressor. The high-pressure side runs from compressor discharge through condenser to expansion valve - these lines are warm or hot to touch. The low-pressure side runs from expansion valve through evaporator back to compressor - these lines are cold.

If you ever see an automotive AC system, you can identify the high and low sides by line diameter too - the low-pressure suction line is larger diameter because vapor is less dense than liquid, so you need a bigger pipe for the same mass flow.

This is your complete vapor compression refrigeration cycle in an automobile."

**PPT Content:**
```
REFRIGERANT CIRCUIT INTEGRATION

COMPLETE CYCLE with State Points:

Point 1 (Compressor Inlet):
• State: Low-pressure vapor (superheated)
• Pressure: 2-3 bar
• Temperature: 5-10°C
• Location: Evaporator outlet / Suction line

Point 2 (Compressor Outlet):
• State: High-pressure vapor (superheated)
• Pressure: 12-18 bar
• Temperature: 70-90°C
• Location: Discharge line

Point 3 (Condenser Outlet):
• State: High-pressure liquid (subcooled)
• Pressure: 12-18 bar
• Temperature: 45-55°C
• Location: Liquid line

Point 4 (Expansion Valve Outlet):
• State: Low-pressure two-phase mixture
• Pressure: 2-3 bar
• Temperature: 3-7°C
• Quality: ~20-40% vapor
• Location: Evaporator inlet

Pressure-Temperature Relationship:
High-side pressure varies with ambient temp:
• 25°C ambient → ~12 bar
• 35°C ambient → ~15 bar
• 45°C ambient → ~18 bar

Low-side pressure varies with evaporator temp:
• Warmer evap (10°C) → ~3.5 bar
• Cooler evap (5°C) → ~2.5 bar
• Near freezing (0°C) → ~2.0 bar (risk of icing)

Line Identification:
Suction line: Large diameter, cold, insulated (vapor, low density)
Discharge line: Medium diameter, hot (vapor, high density)
Liquid line: Small diameter, warm (liquid, high density)

Refrigerant Charge:
Typical sedan: 400-800 grams total refrigerant
Distributed: ~60% in condenser, ~30% in evaporator, ~10% in lines/compressor

System Service Ports:
High-side port (blue cap): For gauges, larger fitting
Low-side port (red cap): For gauges, smaller fitting
Used for pressure diagnosis and refrigerant charging
```

**Teaching Tip:**
Show photo of actual engine bay pointing out compressor, lines, condenser, and service ports.

**Outcomes Addressed:** SO-5-17-3 (complete component integration)

---

## PART 4: CLIMAX - "Heating & Complete System"
**Slides 20-26 | Duration: ~20 minutes | Energy Level: High (Integration Point)**

**Story Purpose:** Integrate heating function and compare compressor technologies
**Teaching Mode:** System integration + technology comparison
**Connection to Prior Knowledge:** Engine cooling system (Session 5)

---

### SLIDE 20: Heating System Integration
**Visual:** Engine coolant circuit showing heater core branch
**Timing:** 3 minutes

**Instructor Narrative:**
"Now let's talk about the other side of HVAC: heating. In a conventional internal combustion engine vehicle, heating is almost trivially simple because we have abundant waste heat.

Remember from Session 5 that the engine cooling system circulates coolant through the engine to absorb combustion heat. That coolant, at around 85-95°C, flows to the radiator to reject heat to the outside. But before it goes to the radiator, we branch off a small flow to the heater core.

The heater core is essentially a miniature radiator located inside the cabin HVAC module, right next to the evaporator. Hot engine coolant flows through the heater core tubes. When you want cabin heating, the blend door inside the HVAC module directs cabin air to flow over the heater core instead of the evaporator. The air is heated by the hot coolant and comes out warm through the vents.

The beauty of this system is that it's parasitic-free - the engine is generating this heat anyway, so using it for cabin heating costs essentially nothing. There's a tiny bit of extra pumping power for the coolant, but it's negligible.

You control heating by adjusting the blend door position. Fully closed - all air bypasses the heater core, you get maximum cooling. Fully open - all air goes through the heater core, you get maximum heating. Partial positions blend cold air from the evaporator with hot air from the heater core to achieve your desired temperature.

This is why conventional cars can provide instant heating as long as the engine is warm, but electric vehicles struggle with heating efficiency - EVs don't have waste heat, they need to use battery energy to run an electric heater or heat pump."

**PPT Content:**
```
HEATING SYSTEM INTEGRATION

Heat Source: Engine waste heat (conventional vehicles)

Engine Coolant Circuit:
Engine → Water pump → Coolant passages (absorb heat)
→ Thermostat → Splits:
  Path 1: Radiator (main heat rejection)
  Path 2: Heater core (cabin heating) ← WE USE THIS
→ Return to engine

Heater Core:
• Small heat exchanger (~15 cm × 20 cm)
• Located inside HVAC module (next to evaporator)
• Hot coolant flows through tubes: 85-95°C
• Cabin air blown over fins
• Heat transfer: Coolant → Air (~3-5 kW heating capacity)

Blend Door Control:
Position 1 (Max Cool): Air bypasses heater core → Only through evaporator
Position 2 (Blend): Partial airflow through heater core, partial through evaporator
Position 3 (Max Heat): All air through heater core → No evaporator

Temperature Control:
Move blend door to mix cold (evaporator) and hot (heater core) air
Achieve any desired cabin temperature between extremes
Controlled by: Manual dial or automatic climate control ECU

Coolant Flow Control:
Older vehicles: Heater control valve (shuts off coolant to heater core when not needed)
Modern vehicles: Continuous flow, temperature controlled by blend door only

Heating Performance:
Available heat: Essentially unlimited (engine generates 30-50 kW waste heat)
Heating capacity: ~3-6 kW (limited by heater core size and airflow)
Warm-up time: Depends on engine warm-up (~3-5 min cold start)

Integration with Engine Cooling:
Heater core acts as auxiliary radiator
Using cabin heating helps cool engine (useful if engine overheating)
Winter: Opening heater core load helps engine reach operating temp faster

ELECTRIC VEHICLE CHALLENGE:
No engine waste heat → Must use:
  Option 1: Resistive electric heater (inefficient, ~1 kW per 1 kW heat)
  Option 2: Heat pump (efficient, ~3 kW heat per 1 kW electric, but complex)
Heating in EVs reduces driving range significantly
```

**Real-World Example:**
"On a cold winter morning, your car's heater won't blow warm air immediately because the engine coolant hasn't warmed up yet. You need to wait 2-3 minutes for the engine to generate enough heat. Auxiliary electric heaters can help in some cars."

**Outcomes Addressed:** SO-5-17-5 (heating system, engine cooling integration)

---

### SLIDE 21: Complete HVAC Module
**Visual:** HVAC module cutaway showing evaporator, heater core, blend door, mode doors, blower
**Timing:** 3 minutes

**Instructor Narrative:**
"Let me show you the complete HVAC module - this is the unit hidden behind your dashboard that ties everything together.

At the core, you have two heat exchangers sitting side by side: the evaporator and the heater core. The evaporator is for cooling, the heater core is for heating.

Air enters the module through the cabin air filter, which removes dust, pollen, and pollutants. The blower motor - a multi-speed fan - forces this air into the module.

The air first encounters the evaporator. Even if you're in heating mode, the air often passes through or near the evaporator to dehumidify it, which is important for defrosting windows.

Then comes the blend door. This is a pivoting flap controlled by a servo motor. If you want cold air, the blend door blocks the heater core and directs all air to bypass it. If you want hot air, the blend door forces all air through the heater core. For a comfortable temperature, the door is partially open, blending some cold air with some heated air.

After the blend door, the air is at your desired temperature. But where does it go? That's determined by mode doors. There are several vents in the car: face vents on the dashboard, floor vents at your feet, and defrost vents aimed at the windshield. Mode doors direct air to whichever vents you select on the control panel - face mode, feet mode, defrost mode, or combinations.

So the HVAC module is doing three things simultaneously: temperature control via blend door, airflow distribution via mode doors, and fan speed control via the blower. All of this is managed either by manual controls or by an automatic climate control ECU."

**PPT Content:**
```
COMPLETE HVAC MODULE

Location: Behind dashboard (center of vehicle)

Key Components:

1. EVAPORATOR
   • Cooling heat exchanger
   • Connected to AC refrigeration circuit
   • Cools and dehumidifies air

2. HEATER CORE
   • Heating heat exchanger
   • Connected to engine coolant circuit
   • Heats air

3. BLOWER MOTOR & FAN
   • Multi-speed electric fan
   • Forces air through system
   • Speeds: Low, Medium, High (or variable)
   • Airflow: 200-600 m³/hr (typical)

4. CABIN AIR FILTER
   • Removes dust, pollen, pollutants
   • Located at fresh air inlet
   • Should be replaced annually

5. BLEND DOOR (Temperature Control)
   • Pivoting door controlled by servo motor
   • Positions:
     - Full cold: Air bypasses heater core
     - Full hot: All air through heater core
     - Blend: Partial mix for intermediate temp
   • Controlled by temperature dial or auto climate ECU

6. MODE DOORS (Airflow Distribution)
   • Direct air to selected vents:
     - FACE: Dashboard vents (cooling)
     - FEET: Floor vents (heating)
     - DEFROST: Windshield vents (defogging)
     - BILEVEL: Face + Feet combination
   • Multiple doors operate simultaneously

7. RECIRCULATION DOOR
   • Fresh air mode: Outside air inlet (default)
   • Recirculation mode: Cabin air recirculates
   • Recirc benefits: Faster cooling, less pollution ingress
   • Recirc drawback: CO₂ buildup, humidity increase

Air Flow Path:
Outside Air (or Recirculated Air)
→ Cabin Filter
→ Blower Fan
→ Evaporator (cooling/dehumidification)
→ Blend Door (temperature control)
→ Heater Core (if blend door directs air there)
→ Mode Doors (distribution)
→ Vents (face/feet/defrost)
→ Cabin

Controls:
Manual: Mechanical cables or electric switches
Automatic: Climate control ECU with servo motors
```

**Visual Aid:**
Show 3D exploded view of HVAC module with all components labeled and airflow arrows.

**Outcomes Addressed:** SO-5-17-5 (complete heating integration), SO-5-17-6 (distribution system)

---

### SLIDE 22: Defrost and Dehumidification
**Visual:** Windshield defrost airflow pattern and moisture removal process
**Timing:** 2 minutes

**Instructor Narrative:**
"Let me quickly highlight one critical HVAC function: windshield defrosting. This is actually a safety feature, not just comfort.

In cold, humid conditions, your breath and body moisture raise cabin humidity. When this humid air contacts the cold windshield, moisture condenses - you get fogging. You can't see through a fogged windshield, which is dangerous.

The defrost mode does two things simultaneously. First, it directs airflow to vents aimed at the windshield - strong airflow across the glass. Second - and this is clever - it usually runs the AC compressor even in cold weather. Why? Because passing the air through the cold evaporator removes moisture before the air is reheated by the heater core. So you get warm, dry air blasting the windshield.

The warm air heats the windshield glass above the dew point so moisture evaporates. The dry air absorbs that moisture without re-condensing. Together, you get rapid defogging.

This is why the AC light sometimes comes on automatically when you select defrost mode, even in winter. It's intentional dehumidification."

**PPT Content:**
```
DEFROST & DEHUMIDIFICATION

Problem: Windshield Fogging
Cause: Humid cabin air contacts cold glass → Condensation
Risk: Visibility loss (safety hazard)

Defrost Mode Operation:
1. Airflow directed to windshield defrost vents
2. AC compressor runs (even in cold weather!)
3. Air cooled by evaporator → Moisture condenses, drains out
4. Dry air then heated by heater core
5. Warm, dry air blows on windshield

Why This Works:
• Warm air → Raises glass temperature above dew point
• Dry air → Absorbs moisture without re-condensing
• High airflow → Rapid evaporation

Typical Defrost Performance:
Fogged windshield → Clear visibility in 1-3 minutes

Controls:
Defrost button → Activates:
  ✓ Defrost mode doors (air to windshield)
  ✓ AC compressor (dehumidification)
  ✓ High blower speed
  ✓ Blend door to warm position

Rear Window Defrost:
Electric resistance heating grid embedded in glass
~100-150 W power consumption
Timer: Auto shutoff after 10-15 minutes
```

**Outcomes Addressed:** SO-5-17-5 (heating integration), SO-5-17-6 (air quality, dehumidification)

---

### SLIDE 23: Compressor Type 1 - Fixed Displacement
**Visual:** Fixed displacement piston compressor cross-section
**Timing:** 3 minutes

**Instructor Narrative:**
"Now let's dive into compressor technologies. I mentioned earlier that there are different types. Let's compare them, starting with the traditional fixed displacement compressor.

A fixed displacement compressor has a fixed swept volume per revolution. For example, a 7-piston radial compressor might have 120 cc displacement. Every time the shaft makes one full rotation, it pumps exactly 120 cc of refrigerant vapor.

This means the compressor's output is directly proportional to engine RPM. If the engine doubles its speed, the compressor flow doubles, and cooling capacity roughly doubles (assuming the system can handle it).

The problem is that you don't always need maximum cooling. Once the cabin is cool, continuing to run the compressor at full capacity would overcool and waste energy. The solution is clutch cycling. When the evaporator temperature drops to a set threshold - say 3°C, to avoid icing - the compressor clutch disengages. The compressor stops. Temperature starts rising. When it reaches maybe 8°C, the clutch re-engages. The compressor restarts.

This on-off cycling happens every 30-60 seconds in moderate conditions. You can sometimes feel it in small cars - a slight surge when the clutch engages, slight relief when it disengages.

The advantage of fixed displacement is simplicity and cost. It's durable, proven technology. The disadvantage is that cycling causes temperature fluctuations and isn't the most efficient because you're either at 100% capacity or 0%, nothing in between."

**PPT Content:**
```
COMPRESSOR TYPE 1: FIXED DISPLACEMENT

Design:
• Fixed piston stroke and cylinder count
• Displacement: Constant (e.g., 120 cc/rev)
• Output proportional to engine RPM
• Electromagnetic clutch for on/off control

Common Configurations:
• Radial piston: 4-7 pistons arranged radially
• Axial piston: Pistons parallel to shaft axis
• Reciprocating motion driven by wobble plate or swash plate

Operation:
• Clutch engaged: Full cooling capacity
• Clutch disengaged: No cooling (compressor off)

Capacity Control: Clutch Cycling
• Evaporator reaches low temp (3°C) → Clutch disengages
• Temperature rises (8°C) → Clutch re-engages
• Cycling frequency: ~30-60 seconds
• Controlled by pressure switch or temperature sensor

Advantages:
✓ Simple, robust design
✓ Low cost
✓ Proven reliability
✓ Easy to service

Disadvantages:
✗ On-off cycling → Temperature fluctuations
✗ Less efficient (always 100% or 0%)
✗ Mechanical wear from clutch cycling
✗ Noticeable engine load changes

Typical Applications:
• Entry-level and mid-range vehicles
• Older vehicle models (pre-2000s dominant)

Cooling Capacity:
Depends on engine RPM and displacement
Example: 150 cc compressor at 2000 RPM
→ Flow rate: ~10-15 g/s refrigerant
→ Cooling: ~3-4 kW
```

**Real-World Note:**
"Most cars built before 2010 use fixed displacement compressors. They're still common in budget vehicles today."

**Outcomes Addressed:** SO-5-17-4 (compressor types comparison)

---

### SLIDE 24: Compressor Type 2 - Variable Displacement
**Visual:** Variable swash plate mechanism diagram showing angle adjustment
**Timing:** 3 minutes

**Instructor Narrative:**
"The next evolution is the variable displacement compressor. This is a smarter design that can adjust its output capacity continuously without cycling on and off.

The key innovation is a variable-angle swash plate. In a fixed displacement compressor, the swash plate - the angled disc that converts rotary motion to piston reciprocation - is at a fixed angle. In a variable compressor, this angle can change.

When the swash plate is at maximum angle, the pistons have maximum stroke, so you get maximum displacement per revolution - full cooling capacity. When the angle decreases, the piston stroke shortens, displacement drops, and cooling capacity reduces. At minimum angle, the stroke is almost zero - compressor is barely pumping.

Here's the clever part: the swash plate angle is controlled automatically by a pressure-sensing mechanism built into the compressor. If the evaporator pressure is high - meaning cooling demand is high - the mechanism increases the swash plate angle for more capacity. If evaporator pressure is low - cabin is cool, low demand - the angle decreases.

This happens continuously and smoothly, with no clutch cycling. The compressor runs all the time when AC is on, but it only produces as much cooling as needed. It's like a variable-speed drive.

The advantages are significant: no temperature fluctuations, better efficiency because you're not wasting energy at times of low demand, smoother engine operation because load changes are gradual. The clutch still exists but rarely cycles - it stays engaged as long as AC is on.

The disadvantage is cost and complexity. Variable displacement compressors are more expensive to manufacture and slightly more complex mechanically. But they're now standard in most mid-range and premium vehicles."

**PPT content:**
```
COMPRESSOR TYPE 2: VARIABLE DISPLACEMENT

Design:
• Variable-angle swash plate mechanism
• Displacement varies: 5% - 100% capacity
• Clutch remains engaged; capacity modulates internally
• Self-regulating based on system pressure

Swash Plate Angle Control:
• Maximum angle → Maximum piston stroke → Max capacity
• Minimum angle → Minimum piston stroke → Min capacity (idle)
• Angle adjusted by pressure-sensing valve (crankcase pressure control)

Capacity Control Mechanism:
1. High cooling demand → Evaporator pressure high
2. Control valve increases swash plate angle
3. Displacement increases → More cooling
4. Cabin cools → Evaporator pressure drops
5. Control valve decreases swash plate angle
6. Displacement decreases → Less cooling
7. Continuous, automatic modulation

Operation:
• Clutch engages when AC turned on
• Compressor runs continuously
• Capacity varies smoothly from 5% to 100%
• No cycling (clutch stays engaged)

Advantages:
✓ Smooth, continuous capacity control
✓ No temperature fluctuations
✓ Better efficiency (matches demand)
✓ Reduced engine load variations
✓ Quieter operation
✓ Faster cool-down (can run at max initially)

Disadvantages:
✗ Higher cost (~30-50% more than fixed)
✗ More complex mechanism
✗ Slightly less efficient at full load (internal losses)

Typical Applications:
• Mid-range to premium vehicles
• Modern vehicles (2000s onward)
• Systems with precise climate control

Capacity Range:
Same compressor, different operating points:
• Minimum: 5-10% → ~0.5 kW cooling
• Maximum: 100% → ~5 kW cooling
• Continuously variable in between

Control Signal:
Older: Mechanical pressure sensing (internal)
Modern: May include external electronic control
```

**Visual Aid:**
Show animation of swash plate angle changing and corresponding piston stroke variation.

**Outcomes Addressed:** SO-5-17-4 (compressor types comparison)

---

### SLIDE 25: Compressor Type 3 - Electric Compressor
**Visual:** Electric compressor with integrated motor and inverter
**Timing:** 3 minutes

**Instructor Narrative:**
"The latest evolution, essential for electric and hybrid vehicles, is the electric compressor. Instead of being belt-driven from the engine, this compressor has an integrated electric motor powered directly from the vehicle's high-voltage battery.

For fully electric vehicles, this is mandatory because there's no engine to drive a belt. But even some high-end conventional and hybrid vehicles now use electric compressors because of the control flexibility they offer.

The electric compressor uses a brushless DC motor, typically running on the vehicle's high-voltage system - 200 to 400 volts. An inverter converts DC battery power to three-phase AC to drive the motor. The motor directly drives the compressor scroll or rotors.

The huge advantage is complete speed independence from the engine. The compressor can run at any speed from 0 to maximum - typically 6000 to 8000 RPM - regardless of engine speed or even whether the engine is running. This means you can have AC while parked with the engine off, which is great for waiting in the car or for camping.

Speed control also means precise capacity control, similar to a variable displacement compressor but even better. If you need 30% cooling capacity, you just run the compressor at 30% speed. Infinitely variable, very efficient.

In hybrid vehicles, the electric compressor allows the engine to shut off during idle stops (start-stop system) while maintaining AC cooling. Without it, you'd lose AC every time the engine stops.

The disadvantages are cost - electric compressors are expensive, easily $500-1000 compared to $200-300 for a conventional one - and the need for high-voltage electrical infrastructure. You also need a dedicated controller to manage the inverter.

But for EVs, there's no choice, and the trend in premium conventional vehicles is moving this direction for the control benefits."

**PPT Content:**
```
COMPRESSOR TYPE 3: ELECTRIC COMPRESSOR

Design:
• Integrated electric motor (no belt drive)
• Brushless DC motor (BLDC)
• High-voltage power: 200-400 VDC (from HV battery)
• Inverter: DC → 3-phase AC motor drive
• Scroll or rotary compressor mechanism
• No clutch (speed control provides on/off and modulation)

Operation:
• Powered directly from vehicle HV battery
• Speed controlled by inverter: 0-8000 RPM (typical)
• Capacity proportional to speed (variable)
• Independent of engine speed or engine running

Speed Control:
• Low cooling demand → Low speed (e.g., 2000 RPM)
• High cooling demand → High speed (e.g., 7000 RPM)
• Continuous variable control
• ECU commands inverter based on cabin temperature

Advantages:
✓ Engine-independent operation (AC while parked, engine off)
✓ Precise capacity control (infinitely variable)
✓ Essential for electric vehicles (no engine to drive belt)
✓ Enables engine start-stop in hybrids (AC continues during engine-off)
✓ Optimal efficiency (run at exact speed needed)
✓ Quiet operation (smooth, no mechanical clutch)
✓ Fast response (instant speed change)

Disadvantages:
✗ High cost ($500-1000+ vs $200-300 conventional)
✗ Requires high-voltage electrical system
✗ Complex power electronics (inverter, controller)
✗ Additional failure modes (electronics)
✗ High current draw from battery (1-3 kW electric power)

Typical Applications:
• Fully electric vehicles (BEVs) - MANDATORY
• Plug-in hybrid vehicles (PHEVs)
• Full hybrids with engine start-stop
• High-end conventional vehicles (some luxury models)

Power Consumption:
Mechanical power: 1-4 kW (varies with speed/load)
Electrical power: 1.2-5 kW (including inverter losses ~80-90% efficiency)
Battery current: 5-15 A at 300V (example)

Impact on Electric Vehicles:
AC power draw reduces driving range
Example: 2 kW AC load on 60 kWh battery
→ ~3.3% battery capacity per hour of AC use
→ Range reduction: ~10-15% with AC on

Control Integration:
Controlled by climate control ECU
Communication via CAN bus
Inputs: Cabin temp sensor, ambient temp sensor, user settings
Output: Speed command to inverter (PWM or digital control)
```

**Real-World Examples:**
- Tesla Model 3: Electric compressor, ~2-3 kW typical draw
- Nissan Leaf: Electric compressor, range impact ~15-20% with AC
- Toyota Prius (modern): Electric compressor to support engine start-stop

**Outcomes Addressed:** SO-5-17-4 (compressor types comparison, control mechanisms)

---

### SLIDE 26: Compressor Comparison Summary
**Visual:** Comparison table of all three compressor types
**Timing:** 2 minutes

**Instructor Narrative:**
"Let me summarize the three compressor types so you can see the evolution and trade-offs clearly.

Fixed displacement is the legacy technology - simple, cheap, reliable, but inefficient due to on-off cycling. Still used in budget vehicles.

Variable displacement is the middle ground - continuously variable capacity, smooth operation, better efficiency, but higher cost. Standard in most modern conventional vehicles.

Electric compressor is the premium and EV-mandatory option - complete speed independence, essential for electric vehicles, excellent control, but expensive and requires high-voltage systems.

The trend is clearly toward electric compressors as vehicles electrify, but you'll still see all three types on the road for years to come."

**PPT Content:**
```
COMPRESSOR COMPARISON SUMMARY

| Feature | Fixed Displacement | Variable Displacement | Electric Compressor |
|---------|-------------------|----------------------|---------------------|
| **Drive** | Engine belt + clutch | Engine belt + clutch | Electric motor (HV) |
| **Capacity Control** | On/Off (clutch cycling) | Continuous (swash plate angle) | Continuous (motor speed) |
| **Speed** | Proportional to engine RPM | Proportional to engine RPM | Independent (0-8000 RPM) |
| **Efficiency** | Moderate (cycling losses) | Good (matches demand) | Excellent (optimized speed) |
| **Temperature Stability** | Fluctuates (cycling) | Stable (continuous) | Very stable (precise control) |
| **Engine Load** | Sudden changes | Gradual changes | Independent |
| **AC When Engine Off** | ✗ No | ✗ No | ✓ Yes |
| **Cost** | Low ($200-300) | Medium ($300-500) | High ($500-1000+) |
| **Complexity** | Simple | Moderate | Complex |
| **Typical Application** | Budget vehicles, older cars | Mid-range, modern conventional | EVs, hybrids, premium cars |
| **Maintenance** | Clutch wear | Moderate | Electronics, motor |

TECHNOLOGY EVOLUTION:
1980s-2000s: Fixed displacement dominant
2000s-2010s: Variable displacement becomes standard
2010s-present: Electric compressor for EVs/hybrids
Future: Electric compressor likely to dominate (vehicle electrification trend)

SELECTION CRITERIA:
• Budget vehicle, conventional: Fixed displacement
• Modern conventional, good climate control: Variable displacement
• Electric or hybrid vehicle: Electric compressor (mandatory)
• Premium conventional with start-stop: Electric compressor
```

**Outcomes Addressed:** SO-5-17-4 (complete comparison of compressor types)

---

## PART 5: RESOLUTION - "Automatic Climate Control"
**Slides 27-30 | Duration: ~13 minutes | Energy Level: Medium-High (Bringing It Together)**

**Story Purpose:** Show how modern systems automatically manage HVAC with sensors and ECU
**Teaching Mode:** System-level integration + control logic
**Connection to Prior Knowledge:** ECU and sensors from Session 14

---

### SLIDE 27: Automatic Climate Control Overview
**Visual:** Block diagram showing sensors → Climate ECU → Actuators
**Timing:** 3 minutes

**Instructor Narrative:**
"We've seen all the hardware components. Now let's talk about automatic climate control - how modern vehicles manage all of this intelligently without you constantly adjusting knobs.

In a manual HVAC system, you set the temperature dial, fan speed, and mode yourself. You're the control system. If it gets too cold, you manually turn up the temperature. If the sun comes out and heats the cabin, you manually adjust again.

Automatic climate control replaces you with an ECU - a dedicated computer for the HVAC system. You simply tell it your desired cabin temperature - say, 22°C - and the system automatically manages compressor operation, blend door position, fan speed, and airflow distribution to maintain that temperature regardless of external conditions.

The ECU uses multiple sensors to understand the thermal state of the cabin and the environment. It knows the cabin temperature, the outside temperature, the sun's intensity, and even the evaporator temperature to prevent icing. Based on all these inputs and your target temperature, it calculates the required cooling or heating and adjusts the actuators accordingly.

This is a classic feedback control system. The cabin temperature is your process variable, your target setting is the setpoint, the difference is the error, and the ECU is the controller. It modulates the compressor, blend door, and fan to drive the error to zero.

The result is set-and-forget comfort. You tell the car '22 degrees,' and it maintains 22 degrees whether you're driving through a tunnel, in bright sun, in traffic, or on the highway."

**PPT Content:**
```
AUTOMATIC CLIMATE CONTROL OVERVIEW

Manual vs Automatic HVAC:

MANUAL HVAC:
• User sets: Temperature dial, fan speed, mode
• Fixed settings until user changes them
• User must adjust for changing conditions
• Simple, cheap, no complex electronics

AUTOMATIC CLIMATE CONTROL:
• User sets: Desired temperature (e.g., 22°C)
• System automatically adjusts all parameters
• Maintains temperature regardless of external changes
• Requires sensors, ECU, actuators

AUTOMATIC CLIMATE CONTROL SYSTEM:

┌──────────────┐
│   SENSORS    │───┐
└──────────────┘   │
                   ↓
┌──────────────────────────┐
│   CLIMATE CONTROL ECU    │
│  (Controller/Computer)   │
└──────────────────────────┘
                   ↓
┌──────────────┐
│  ACTUATORS   │
└──────────────┘

Inputs (Sensors):
• Cabin temperature
• Outside ambient temperature
• Solar radiation (sun load)
• Evaporator temperature
• Humidity (advanced systems)
• Occupant presence (advanced systems)

Processing (ECU Logic):
• Calculate temperature error: Error = Target - Actual
• Determine required cooling/heating power
• Control strategy: Compressor speed, blend door position, fan speed
• Prevent icing (evaporator temp > 3°C)
• Optimize efficiency and comfort

Outputs (Actuators):
• Compressor clutch or speed control
• Blend door servo motor (temperature control)
• Mode door servo motors (air distribution)
• Blower motor speed (fan control)
• Recirculation door (air source)

Control Type: Closed-Loop Feedback
Setpoint: User-selected temperature (20-28°C typical range)
Process Variable: Actual cabin temperature
Controller: PID or fuzzy logic (ECU algorithm)
Actuators: Modulate to drive error → 0
```

**Analogy:**
"It's like cruise control for temperature. You set the target, the system maintains it automatically."

**Outcomes Addressed:** SO-5-17-6 (automatic climate control systems)

---

### SLIDE 28: Sensors for Climate Control
**Visual:** Car diagram showing sensor locations
**Timing:** 3 minutes

**Instructor Narrative:**
"Let's look at the key sensors in an automatic climate control system.

First, the cabin temperature sensor. This is usually located in the dashboard near the climate control vents, behind a small grille. It's often a thermistor - a temperature-sensitive resistor. Some systems have multiple cabin sensors to measure temperature at different zones.

Second, the ambient temperature sensor. This measures outside air temperature and is typically located behind the front bumper where it gets good airflow but is protected from direct sun and engine heat. It tells the system what it's up against - if it's 40°C outside, the system knows it needs maximum cooling initially.

Third, the solar radiation sensor or sun load sensor. This is a photodiode or photodetector mounted on top of the dashboard, usually near the windshield. It measures sunlight intensity. Why does this matter? Because even if the cabin air temperature is 22°C, if the sun is blasting through the windows, your skin feels hot. The solar sensor detects this and tells the system to increase cooling or shift airflow to compensate.

Fourth, the evaporator temperature sensor. This is a thermistor attached to the evaporator fins. Its job is to prevent the evaporator from freezing. If the evaporator drops below about 3°C, ice can form on the fins, blocking airflow. The ECU monitors this sensor and cycles the compressor off or reduces capacity if icing is detected.

Advanced systems might also have humidity sensors to optimize dehumidification, CO₂ sensors to determine when fresh air is needed, and even occupancy sensors to detect which zones are occupied in multi-zone systems.

All these sensors feed data to the climate control ECU dozens of times per second, allowing it to respond quickly to changing conditions."

**PPT Content:**
```
SENSORS FOR CLIMATE CONTROL

1. CABIN TEMPERATURE SENSOR
   • Type: Thermistor (NTC - Negative Temperature Coefficient)
   • Location: Dashboard, behind vent grille (aspirated by fan)
   • Range: -40°C to +80°C
   • Accuracy: ±0.5°C
   • Purpose: Measure actual cabin air temperature (feedback)
   • Multi-zone systems: Multiple sensors (driver, passenger, rear)

2. AMBIENT TEMPERATURE SENSOR
   • Type: Thermistor or RTD (Resistance Temperature Detector)
   • Location: Behind front bumper, shielded from sun/engine
   • Range: -40°C to +60°C
   • Purpose: Measure outside air temperature
   • Usage: Initial cooling/heating demand calculation, display to driver

3. SOLAR RADIATION SENSOR (Sun Load Sensor)
   • Type: Photodiode or photodetector array
   • Location: Top of dashboard (near windshield)
   • Output: Voltage proportional to light intensity (W/m²)
   • Range: 0-1200 W/m² (full sunlight ~1000 W/m²)
   • Purpose: Detect radiant heat from sun
   • Advanced: Multi-axis sensors detect sun angle for left/right zone compensation

4. EVAPORATOR TEMPERATURE SENSOR
   • Type: Thermistor
   • Location: Attached to evaporator fins
   • Range: -10°C to +20°C
   • Purpose: Prevent evaporator icing (monitor evap temp > 3°C)
   • Usage: Compressor cycling control or capacity reduction

5. HUMIDITY SENSOR (Advanced Systems)
   • Type: Capacitive or resistive humidity sensor
   • Location: Cabin air intake or HVAC module
   • Range: 0-100% relative humidity
   • Purpose: Optimize dehumidification, prevent fogging

6. CABIN AIR QUALITY SENSOR (Premium Systems)
   • Type: VOC (Volatile Organic Compound) sensor, CO₂ sensor
   • Location: Cabin air intake
   • Purpose: Detect pollutants, automatically switch to recirculation in tunnels/traffic
   • Auto recirc: Close outside air when pollution detected

Sensor Communication:
• Analog signals: Voltage (0-5V) or resistance (thermistors)
• Converted by ECU analog-to-digital converter (ADC)
• Sampling rate: 10-100 Hz (depends on sensor type)
• Some sensors on LIN bus (digital communication)
```

**Teaching Note:**
Emphasize that sensors provide situational awareness - the ECU can't control what it can't measure.

**Outcomes Addressed:** SO-5-17-6 (automatic climate control, sensors)

---

### SLIDE 29: Multi-Zone Climate Control
**Visual:** Vehicle interior showing driver, passenger, and rear zones with independent controls
**Timing:** 3 minutes

**Instructor Narrative:**
"One of the coolest features in modern premium vehicles is multi-zone climate control. Instead of one temperature for the entire cabin, you can have independent temperature settings for different zones - typically driver, passenger, and rear.

How is this possible when there's only one evaporator and one heater core? The secret is multiple blend doors and independent zone controls.

The HVAC module has separate air channels for each zone. After the air passes through the evaporator and heater core, it splits into zone-specific ducts. Each zone has its own blend door, controlled by its own servo motor. So the driver might have their blend door set to 40% heater core (warm), while the passenger has their blend door set to 10% heater core (cool).

Each zone also has its own temperature sensor. The climate control ECU runs independent control loops for each zone, adjusting each zone's blend door to maintain that zone's target temperature.

The compressor and fan speed are set to handle the maximum demand across all zones. If the driver wants 18°C (maximum cooling) and the passenger wants 28°C (warm), the system runs the compressor hard to provide maximum cooling, then reheats the passenger side air with the heater core.

This is obviously less efficient than single-zone - you're cooling air and then reheating it - but the comfort benefit is huge. The driver and passenger can each be comfortable without compromise.

Luxury vehicles may have three or even four zones: driver, front passenger, left rear, right rear. The principle is the same - multiple blend doors and temperature sensors, centralized compressor and heater core.

This requires significantly more hardware - extra servo motors, sensors, and complex ductwork - which is why it's typically a premium feature."

**PPT Content:**
```
MULTI-ZONE CLIMATE CONTROL

Concept:
Independent temperature settings for different cabin areas
Typical configurations:
• 2-zone: Driver, Passenger
• 3-zone: Driver, Passenger, Rear
• 4-zone: Driver, Passenger, Left Rear, Right Rear

How It Works:

SHARED COMPONENTS:
• Single evaporator (cooling for all zones)
• Single heater core (heating for all zones)
• Single blower motor (main airflow)

ZONE-SPECIFIC COMPONENTS:
• Separate blend doors per zone
• Independent servo motors per blend door
• Separate temperature sensors per zone
• Dedicated ductwork per zone
• Individual mode doors (some systems)

Control Strategy:
1. User sets target temperature per zone
   Example: Driver 20°C, Passenger 24°C, Rear 22°C

2. ECU reads temperature sensor for each zone

3. ECU calculates required blend door position per zone
   Example: Driver zone → Blend door 20% heater core (cool bias)
            Passenger zone → Blend door 60% heater core (warm bias)

4. ECU commands servo motors to position each blend door

5. Air splits after evaporator/heater core:
   → Driver duct → Driver blend door → Driver vents
   → Passenger duct → Passenger blend door → Passenger vents
   → Rear duct → Rear blend door → Rear vents

Compressor & Fan Control:
• Set to meet MAXIMUM cooling demand across all zones
• Example: If driver wants max cool (18°C) and passenger wants warm (26°C):
  → Compressor runs at full capacity (coldest evaporator)
  → Driver gets full cold air
  → Passenger air is reheated via heater core (blend door open)

Efficiency Trade-off:
• Less efficient than single zone (simultaneous cooling + heating)
• Energy penalty: ~10-20% higher consumption
• Comfort benefit: Personalized temperature zones

Typical Applications:
• Premium sedans (3-series BMW, Audi A4, Mercedes C-class)
• Luxury SUVs (Range Rover, Lexus RX)
• Full-size sedans and SUVs

User Interface:
• Driver control panel: Temperature setting (L/R or driver/passenger)
• Passenger control panel: Independent temperature control
• Rear control panel (optional): Rear zone temperature, fan speed
• Display shows all zone target temperatures
```

**Real-World Example:**
"In a family road trip, dad (driver) might want 20°C, mom (passenger) wants 24°C, and kids in the rear want 22°C. Multi-zone makes everyone happy without arguments."

**Outcomes Addressed:** SO-5-17-6 (multi-zone temperature management)

---

### SLIDE 30: Summary & Integration
**Visual:** Complete HVAC system diagram with all components, controls, and airflow
**Timing:** 2 minutes

**Instructor Narrative:**
"Let's wrap up. We started today by understanding cabin comfort requirements - temperature, humidity, air quality. We learned that automotive HVAC faces unique challenges with varying loads and conditions.

We then dove into refrigeration thermodynamics. You now understand the vapor compression cycle: compression, condensation, expansion, evaporation. You can read a P-h diagram and understand why evaporation cools - latent heat absorption.

We identified all the key components: compressor driven by engine or electric motor, condenser rejecting heat to outside air, expansion valve dropping pressure and temperature, and evaporator absorbing cabin heat. We saw how refrigerant circulates through this closed loop.

We integrated heating by tapping engine waste heat through the heater core. We compared compressor technologies: fixed displacement with clutch cycling, variable displacement with continuous capacity control, and electric compressors for hybrids and EVs.

Finally, we saw how automatic climate control uses sensors and an ECU to maintain your desired temperature automatically, and how multi-zone systems provide personalized comfort for different passengers.

The HVAC system is a beautiful example of thermodynamics, fluid mechanics, heat transfer, controls, and mechanical design all working together. It's one of the most power-hungry systems in the vehicle, but it's also one of the most important for comfort and safety - remember, defrosting is critical for visibility.

You now have a complete understanding of automotive HVAC from the physics to the components to the control systems."

**PPT Content:**
```
SESSION 17 SUMMARY

✓ Cabin Comfort Requirements
  • Temperature, humidity, air quality, airflow
  • Automotive challenges: Variable loads, rapid response

✓ Refrigeration Thermodynamics
  • Vapor compression cycle: 4 processes
  • P-h diagram visualization
  • Refrigerant: R134a → R1234yf (low GWP)
  • Phase change: Evaporation cools, condensation heats

✓ HVAC Components
  • Compressor: Pressure & temperature boost (work input)
  • Condenser: Heat rejection to outside (phase change: gas → liquid)
  • Expansion valve: Pressure drop (throttling)
  • Evaporator: Heat absorption from cabin (phase change: liquid → gas)

✓ Heating Integration
  • Heater core: Engine coolant waste heat
  • Blend door: Temperature control (cold/hot air mix)
  • Free heating in conventional vehicles
  • Challenge for EVs: No waste heat

✓ Compressor Technologies
  • Fixed displacement: On/off cycling, simple, budget
  • Variable displacement: Continuous capacity, smooth, modern
  • Electric compressor: Speed-independent, EVs/hybrids, premium

✓ Automatic Climate Control
  • Sensors: Cabin temp, ambient temp, solar, evaporator temp
  • Climate ECU: Feedback control, maintains target temperature
  • Actuators: Compressor, blend doors, fan, mode doors
  • Multi-zone: Independent zone temperatures (driver, passenger, rear)

Key Takeaway:
HVAC is an integrated thermal management system combining refrigeration (cooling), waste heat recovery (heating), airflow distribution, and intelligent control to maintain cabin comfort across all driving conditions.

Next Session: Passive Safety Systems
• Crash structures, seatbelts, airbags
• Occupant protection strategies
• Safety testing standards
```

**Outcomes Addressed:** All SOs (complete summary)

---

## POST-SESSION ACTIVITIES & ASSESSMENT ALIGNMENT

### Learning Outcome Achievement Verification

| SO Code | Coverage | Verification Method |
|---------|----------|---------------------|
| SO-5-17-1 | Slides 2-6 | Explain comfort parameters, HVAC challenges, system functions |
| SO-5-17-2 | Slides 7-13 | Describe refrigeration cycle, P-h diagram, thermodynamic processes |
| SO-5-17-3 | Slides 14-19 | Identify and explain all HVAC components and refrigerant flow |
| SO-5-17-4 | Slides 23-26 | Compare compressor types (fixed, variable, electric) |
| SO-5-17-5 | Slides 20-22 | Explain heater core and integration with engine cooling |
| SO-5-17-6 | Slides 27-30 | Describe automatic climate control, multi-zone systems |

### Q&A Session Guidance (30 minutes)

**Expected Student Questions:**

1. **"Why does AC reduce fuel economy?"**
   - Answer: Compressor requires 2-4 kW mechanical power from engine. At city speeds (~30 kW engine output), this is 10-15% power consumption → 10-15% fuel penalty.

2. **"Can you run AC with engine off?"**
   - Conventional: No (belt-driven compressor needs engine running)
   - Electric compressor: Yes (draws from battery, limited duration)

3. **"Why does my car's AC take time to get cold?"**
   - Answer: System must build pressure, refrigerant must circulate, evaporator must cool down. Initial cool-down 1-2 minutes. Cabin cool-down depends on cabin temperature and insulation.

4. **"What's the difference between 'Max AC' and normal AC?"**
   - Answer: Max AC = Recirculation mode (recirculates cabin air instead of outside air). Cools faster because starting with cooler cabin air. But can't use indefinitely (CO₂ buildup, humidity).

5. **"Why run AC in winter for defrost?"**
   - Answer: Dehumidification. Evaporator removes moisture, then air is reheated. Dry warm air prevents windshield fogging better than just warm air.

**Recommended Q&A Topics:**
- COP calculation examples
- Refrigerant safety and environmental concerns
- HVAC maintenance (cabin filter replacement, refrigerant recharge)
- Electric vehicle HVAC challenges and solutions (heat pumps)

### Suggested Assignments

**Assignment 1: HVAC Cooling Capacity Calculation**
- Given: Vehicle cabin volume, initial temperature, target temperature, cool-down time
- Calculate: Required cooling power, refrigerant mass flow rate
- Reinforces: Thermodynamics, energy balance

**Assignment 2: Compressor Selection**
- Scenario: Design HVAC for city car vs. luxury SUV vs. electric vehicle
- Task: Select compressor type, justify based on cost, performance, efficiency
- Reinforces: SO-5-17-4 (compressor comparison)

**Assignment 3: Multi-Zone Climate Control Analysis**
- Given: 3-zone system with different target temperatures
- Task: Determine blend door positions, estimate efficiency penalty
- Reinforces: SO-5-17-6 (multi-zone systems)

### Connection to Next Session

**Session 18 Preview:**
"In the next session, we'll shift focus from comfort to safety - specifically passive safety systems. We'll explore crash structures, seatbelts, airbags, and how vehicles protect occupants during collisions. You'll learn about the airbag control unit (ACU), which has similarities to the climate control ECU we discussed today - both use sensors and actuators for critical functions. See you next time!"

---

## INSTRUCTOR NOTES

### Timing Checkpoints
- 30 min: Should be finishing Part 2 (Refrigeration Thermodynamics)
- 60 min: Should be finishing Part 3 (HVAC Components)
- 75 min: Should be finishing Part 4 (Heating & Complete System)
- 90 min: Finish Part 5 (Automatic Climate Control)

### Energy Management
- **High energy:** Part 2 (core thermodynamics - keep students engaged)
- **Medium energy:** Part 3 (component description - visual aids help)
- **High energy:** Part 4 (integration point - emphasize connections)
- **Medium energy:** Part 5 (control systems - technical but important)

### Common Student Difficulties
1. **P-h Diagram:** Students find it abstract. Use animated visualization showing refrigerant moving through cycle.
2. **Why COP > 1:** Clarify we're moving heat, not creating cold. Use heat pump analogy.
3. **Evaporator vs. Condenser Confusion:** Both are heat exchangers. Emphasize: Evaporator INSIDE cabin (cooling), Condenser OUTSIDE vehicle (heat rejection).

### Demonstration Opportunities
- Show actual compressor (cutaway model if available)
- Demonstrate refrigerant pressure with gauge set (if safe setup available)
- Show HVAC module components (evaporator, blend door) from salvage unit

### Safety Reminders
- Emphasize: NEVER release refrigerant to atmosphere (illegal, environmental harm)
- High-pressure refrigerant can cause frostbite injuries
- HV systems in electric compressors are dangerous (200-400V)
- Professional service required for refrigerant work

---

**END OF SESSION 17 FRAMEWORK**
