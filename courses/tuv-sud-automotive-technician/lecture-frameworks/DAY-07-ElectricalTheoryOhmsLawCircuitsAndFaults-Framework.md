---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 2
week_title: "Speaking Electricity"
day_number: 7
session_title: "Electrical Theory — Ohm's Law, Circuits & Faults"
duration_minutes: 180
theory_practice: "50:50"
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 7: Electrical Theory — Ohm's Law, Circuits & Faults
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (90 min theory + 90 min practical)
**Approach:** Concept-Building — Understand the Physics Before You Touch the Wire
**PPT Target:** 28 slides
**Week:** 2 of 8 — "Speaking Electricity"

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Define voltage, current, and resistance using the water pipe analogy and correct SI units
- Apply Ohm's Law (V = IR) and the power formula (P = VI) to solve basic automotive electrical calculations
- Explain the difference between series and parallel circuits, including how voltage and current behave in each
- Identify and describe three circuit fault types — open circuit, short circuit, and high resistance — and their automotive symptoms
- Recognise standard wiring diagram symbols (battery, fuse, relay, switch, ground, motor, resistor, LED) and trace current paths through a basic schematic
- Build simple circuits on a training board, measure voltage and current with a multimeter, and verify Ohm's Law experimentally

**This is Day 7.** Learners completed Day 6 (vehicle electronics overview — ECUs, sensors, actuators, CAN bus). They understand WHY electronics matter. Today they learn the PHYSICS of how electricity actually works. This is the mathematical and conceptual foundation for everything in Week 2.

---

## Connection to Prior Knowledge

Build from Day 6:
- Day 6 showed 100+ ECUs, sensors, actuators, CAN bus — the "what" of vehicle electronics
- Learners know that modern vehicles are electronic machines
- They've seen wiring harnesses and connectors but don't yet understand what flows through them

**Bridge:** "Yesterday you saw the nervous system of the car — sensors, ECUs, wiring harnesses. But what actually flows through those wires? How does a battery make a headlight glow? Why does a corroded terminal make a starter motor spin slowly? Today we answer those questions. Three letters will unlock it all: V, I, R."

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: Three Letters That Run Every Car** (Slides 1-3, ~10 minutes)

**Narrative Voice:** Energetic, grounding. Connect yesterday's big picture to today's fundamentals.

---

#### Slide 1: Title & Context
**Visual:** Title slide — image of a glowing headlight filament transitioning into a flowing river of electrons, with the letters V, I, R prominently displayed

**Instructor Narration:**
> "Yesterday you met the nervous system of the car — over 100 ECUs, thousands of sensors, kilometres of wiring. Impressive stuff. But here's the thing: none of it works unless you understand three simple letters. V. I. R. Voltage. Current. Resistance. These three quantities explain EVERYTHING electrical in a vehicle — why a headlight glows, why a fuse blows, why a corroded battery terminal kills your starter motor. Today, we learn the physics. And I promise you — it's simpler than you think."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 2: Speaking Electricity
Day 7: Electrical Theory — Ohm's Law, Circuits & Faults

Three letters. Every electrical problem solved.
V — I — R
```

---

#### Slide 2: Where We Are in Week 2
**Visual:** Week 2 daily timeline — Day 6 highlighted as complete, Day 7 highlighted as current, Days 8-10 greyed out

**Instructor Narration:**
> "Here's our Week 2 roadmap. Day 6 was the overview — you saw the whole electronic landscape of a modern vehicle. Today, Day 7, is the physics — the rules that electricity follows. Day 8, we'll look at components, protection devices, and wiring craft. Day 9, you'll learn to use a multimeter properly and read live circuits. Day 10, we bring it all together with diagnostic thinking. Each day builds on the last. Today's physics is the foundation for everything else this week."

**PPT Content:**
```
WEEK 2: SPEAKING ELECTRICITY

Day 6:  Vehicle Electronics Overview (COMPLETE)
        — ECUs, sensors, actuators, CAN bus

Day 7:  Electrical Theory (TODAY)
        — V, I, R, Ohm's Law, circuits, faults

Day 8:  Components, Protection & Wiring
        — Relays, fuses, connectors, crimping

Day 9:  Measuring Electricity
        — Multimeter mastery, live circuit testing

Day 10: Electrical Diagnostics
        — Systematic fault finding
```

---

#### Slide 3: Today's Plan
**Visual:** Horizontal timeline divided into 5 blocks with icons — lightbulb (V/I/R), calculator (Ohm's Law), circuit symbol (series/parallel), warning triangle (faults), wrench (practical)

**Instructor Narration:**
> "Here's exactly how today works. First, we learn what voltage, current, and resistance actually are — using an analogy you'll never forget. Then we learn Ohm's Law — one equation that connects all three. We'll apply it to series and parallel circuits. Then we cover the three things that go wrong — open circuits, short circuits, and high resistance faults. After theory, you build real circuits, measure them, and I'll break things for you to diagnose. Ready?"

**PPT Content:**
```
TODAY'S PLAN (180 minutes)

THEORY BLOCK 1 (40 min): V, I, R — The Big Three
— Water pipe analogy, units, Ohm's Law, Power

THEORY BLOCK 2 (25 min): Circuit Faults
— Open, short, high resistance — symptoms & examples

THEORY BLOCK 3 (15 min): Reading Wiring Diagrams
— Symbols, current paths, connector IDs

PRACTICAL (75 min): Build, Measure, Diagnose
— Breadboard circuits, multimeter intro, fault finding

WRAP-UP (15 min): Review + Day 8 preview
```

---

### **DEVELOPMENT PART 1: V, I, R — The Big Three** (Slides 4-14, ~40 minutes)

**Narrative Voice:** Patient, conceptual, rich with analogy. Build understanding layer by layer.

---

#### Slide 4: The Water Pipe Analogy
**Visual:** Side-by-side comparison — water system (tank, pipe, restriction) and electrical circuit (battery, wire, resistor). Arrows showing flow direction in both. Labels: Tank = Battery, Pipe = Wire, Valve/Restriction = Resistor, Water Flow = Current, Water Pressure = Voltage

**Instructor Narration:**
> "Here's the analogy that makes electricity click. Imagine a water tank on a hill. The height of the water creates pressure — that's VOLTAGE. Open a pipe at the bottom and water flows — that's CURRENT. Put a narrow section in the pipe and the flow slows down — that's RESISTANCE. A battery is the tank. Wires are the pipes. Components like lightbulbs and motors are the restrictions. The higher the tank — more voltage — the more water flows. The narrower the pipe — more resistance — the less water flows. That's the entire relationship. Let's put numbers on it."

**PPT Content:**
```
THE WATER PIPE ANALOGY

WATER SYSTEM              ELECTRICAL CIRCUIT
Water tank (height)    =  Battery (voltage)
Water pressure         =  VOLTAGE (V) — electrical pressure
Water flow rate        =  CURRENT (I) — flow of electrons
Narrow pipe section    =  RESISTANCE (R) — opposition to flow
Pipe                   =  Wire — the path

Higher pressure → more flow
Narrower pipe → less flow

This is the ENTIRE relationship.
```

---

#### Slide 5: Voltage (V) — Electrical Pressure
**Visual:** Battery symbol with + and - terminals. Voltage meter connected across the terminals showing 12.6V. Analogy image of water pressure gauge. Common vehicle voltages listed.

**Instructor Narration:**
> "Voltage is electrical pressure — the PUSH that makes electrons move. It's measured in Volts, symbol V, named after Alessandro Volta. Think of it as the difference in energy between two points. A car battery has about 12.6 volts when fully charged. That means there's 12.6 volts of 'push' available between the positive and negative terminals. No voltage, no push, no flow — nothing works. Important: voltage is always measured BETWEEN two points. You never measure voltage at a single point. It's always a difference — like height. You don't ask 'how tall?' without a reference point."

**PPT Content:**
```
VOLTAGE (V) — The Push

Definition: Electrical pressure difference between two points
Unit: Volt (V)
Named after: Alessandro Volta (1745-1827)
Instrument: Voltmeter (measured IN PARALLEL)

Common automotive voltages:
• Car battery (fully charged): 12.6 V
• Car battery (engine running): 13.8 - 14.4 V
• Starter motor cranking: 10.0 - 10.5 V (voltage drops under load)
• USB charger port: 5 V
• HV battery (EV/hybrid): 300 - 800 V (!)

KEY: Voltage is always measured BETWEEN two points.
It is a DIFFERENCE, not an absolute value.
```

---

#### Slide 6: Current (I) — The Flow
**Visual:** Animated-style illustration showing electrons flowing through a wire from negative to positive (conventional current arrow shown positive to negative). Ammeter in series with a circuit. Water flow analogy alongside.

**Instructor Narration:**
> "Current is the actual flow of electrons through the wire. It's measured in Amperes — or Amps for short — symbol I, from the French word 'intensite'. One amp is a LOT of electrons — about 6.2 billion billion electrons per second passing a point. But you don't need to think about individual electrons. Think about flow rate — like litres per minute through a pipe. More current means more electrons flowing. A headlight might draw 5 amps. A starter motor? 200 amps or more. That's why the starter cables are so thick — they're carrying a massive flow."

**PPT Content:**
```
CURRENT (I) — The Flow

Definition: Rate of electron flow through a conductor
Unit: Ampere / Amp (A)
Symbol: I (from French "intensite")
Instrument: Ammeter (measured IN SERIES — current flows through it)

Common automotive currents:
• Interior light:          0.5 A
• Headlight (halogen):     5 A
• Electric window motor:   10 A
• Heated rear window:      15 A
• Radiator fan:            20 A
• Fuel pump:               5-8 A
• Starter motor:           150-300 A (!)

More current = thicker wires needed
That's why starter cables are the thickest wires in the car.
```

---

#### Slide 7: Resistance (R) — The Opposition
**Visual:** Various automotive components shown as resistors — a thin filament bulb, a corroded connector, a length of thin wire. Ohm symbol. Image of a kinked garden hose restricting flow.

**Instructor Narration:**
> "Resistance is anything that opposes the flow of current. It's measured in Ohms — symbol is the Greek letter omega. Everything has resistance. A wire has a small resistance. A light bulb filament has more. A corroded connector has resistance that shouldn't be there — and that's where problems start. Good connections have very low resistance — almost zero. Bad connections have high resistance — and that high resistance converts electrical energy into HEAT instead of useful work. That's why corroded battery terminals get hot. That's why undersized wires can start fires."

**PPT Content:**
```
RESISTANCE (R) — The Opposition

Definition: Opposition to the flow of current
Unit: Ohm (symbol: omega)
Named after: Georg Simon Ohm (1789-1854)
Instrument: Ohmmeter (measured with circuit POWER OFF)

Resistance in automotive:
• Good copper wire (1m):           ~0.01 ohm
• Clean connector:                 ~0.001 ohm (near zero)
• Headlight filament:              ~2.4 ohm
• Glow plug:                       ~0.5-1.0 ohm
• Corroded battery terminal:       0.1-1.0 ohm (BAD!)
• Broken wire (open circuit):      Infinite ohm (no flow)

UNWANTED resistance = HEAT + VOLTAGE DROP = PROBLEMS
```

---

#### Slide 8: Ohm's Law — The Golden Triangle
**Visual:** The classic Ohm's Law triangle: V on top, I and R on the bottom. Three formula arrangements shown: V = IR, I = V/R, R = V/I. Each with a brief description of when to use it.

**Instructor Narration:**
> "Now we connect all three. Georg Ohm discovered this relationship in 1827, and it's still the single most important equation in electrical work. Voltage equals Current times Resistance. V = I times R. Cover V with your thumb — you get I times R. Cover I — you get V divided by R. Cover R — you get V divided by I. This triangle will be your best friend. Let's use it."

**PPT Content:**
```
OHM'S LAW — The Golden Triangle

          V
         ---
        | V |
         ---
       /     \
      /       \
   ---         ---
  | I |       | R |
   ---         ---

V = I x R     Voltage = Current x Resistance
I = V / R     Current = Voltage / Resistance
R = V / I     Resistance = Voltage / Current

Cover what you want to find.
What remains is the formula.

THIS IS THE MOST IMPORTANT EQUATION IN AUTOMOTIVE ELECTRICAL WORK.
```

---

#### Slide 9: Ohm's Law — Automotive Calculations
**Visual:** Three worked example boxes, each with a small vehicle diagram showing the component in question. Calculator icon.

**Instructor Narration:**
> "Let's do three real calculations. First: a headlight bulb has 2.4 ohms of resistance and runs on 12 volts. How much current does it draw? I = V / R = 12 / 2.4 = 5 amps. That tells us what size fuse to use — at least 5 amps, probably a 7.5 or 10 to allow some headroom.
>
> Second: a starter motor draws 200 amps from a 12-volt battery. What's its resistance? R = V / I = 12 / 200 = 0.06 ohms. Almost nothing — that's why it's essentially a short circuit that's controlled by the starter solenoid.
>
> Third: a blower motor has 1.5 ohms resistance. The battery supplies 12 volts. How much current? I = V / R = 12 / 1.5 = 8 amps. Now you know why the blower motor fuse is typically 20 or 30 amps — it needs headroom for startup surge."

**PPT Content:**
```
OHM'S LAW IN ACTION

EXAMPLE 1: Headlight current draw
Headlight resistance = 2.4 ohm, Battery = 12 V
I = V / R = 12 / 2.4 = 5 A
--> Fuse: 7.5 A or 10 A (headroom above 5 A)

EXAMPLE 2: Starter motor resistance
Starter draws 200 A from 12 V battery
R = V / I = 12 / 200 = 0.06 ohm
--> Nearly zero resistance — massive current flow

EXAMPLE 3: Blower motor current
Blower resistance = 1.5 ohm, Battery = 12 V
I = V / R = 12 / 1.5 = 8 A
--> Fuse: 20 A or 30 A (allows for startup surge)

PRACTICE: Calculate the current through a 6-ohm fog light on a 12V system.
Answer: I = 12 / 6 = 2 A
```

---

#### Slide 10: Power (P = V x I) — Where the Work Happens
**Visual:** Light bulb with wattage label, starter motor with power label. Power triangle similar to Ohm's triangle. Image showing a 55W headlight bulb.

**Instructor Narration:**
> "There's a fourth quantity you need: Power. Power is measured in Watts and tells you how much work is being done — how much energy per second is being converted. A 55-watt headlight converts 55 joules of electrical energy into light and heat every second. The formula is simple: Power = Voltage times Current. P = V times I. So our 12-volt, 5-amp headlight? P = 12 x 5 = 60 watts. Close to the rated 55 watts — the difference is because real-world voltage isn't perfectly 12 volts.
>
> You can combine this with Ohm's Law to get two more useful formulas: P = I-squared times R, and P = V-squared divided by R. But P = V times I is the one you'll use most. It's how you size wires, fuses, and alternators."

**PPT Content:**
```
POWER (P) — The Work Done

P = V x I     Power = Voltage x Current
Unit: Watt (W)

Also useful:
P = I squared x R   (when you know current and resistance)
P = V squared / R   (when you know voltage and resistance)

Automotive examples:
• Interior light:     12V x 0.5A =    6 W
• Headlight (halogen): 12V x 4.6A =  55 W
• Heated rear screen: 12V x 15A  = 180 W
• Starter motor:      12V x 200A = 2400 W (2.4 kW!)
• Alternator output:  14V x 100A = 1400 W (typical modern car)

POWER determines:
• Wire thickness needed (more power = thicker wire)
• Fuse size (protects against excess power/current)
• Alternator sizing (must supply total vehicle power demand)
```

---

#### Slide 11: Series Circuits — One Path Only
**Visual:** Simple series circuit diagram: battery -> switch -> resistor 1 -> resistor 2 -> back to battery. Voltmeter readings shown at each component. Ammeter reading shown at multiple points proving current is the same. Christmas tree lights image for analogy.

**Instructor Narration:**
> "Now let's talk about how components are connected. In a series circuit, there's only ONE path for current. Everything is connected end-to-end — like links in a chain. The key rules: current is the SAME everywhere in a series circuit. If 2 amps flows through the first component, 2 amps flows through every component. But voltage DIVIDES. Each component gets a share of the total voltage proportional to its resistance. The voltages across all components add up to the battery voltage.
>
> Christmas lights used to be wired in series. Remember what happened when one bulb blew? They ALL went out. Because with one break in the chain, there's no complete path — no current flows anywhere. That's a series circuit's weakness."

**PPT Content:**
```
SERIES CIRCUITS — One Path

Rules:
1. CURRENT is the SAME through every component
   I(total) = I(R1) = I(R2) = I(R3)

2. VOLTAGE DIVIDES across components
   V(total) = V(R1) + V(R2) + V(R3)

3. TOTAL RESISTANCE ADDS UP
   R(total) = R1 + R2 + R3

Example: Two 6-ohm resistors in series on 12V
R(total) = 6 + 6 = 12 ohm
I = V / R = 12 / 12 = 1 A (same through both)
V across each = I x R = 1 x 6 = 6V (voltage divides equally)

WEAKNESS: One break = entire circuit dead
(Old Christmas lights — one bulb out, all dark)

AUTOMOTIVE USE: Voltage drop testing uses this principle
```

---

#### Slide 12: Parallel Circuits — Multiple Paths
**Visual:** Parallel circuit diagram: battery with three branches, each containing a different load (headlight, radio, fan). Ammeters on each branch showing different currents. Voltmeter across any branch showing same voltage. Modern Christmas lights image.

**Instructor Narration:**
> "Now the way most vehicle loads are actually wired — parallel. In a parallel circuit, each component has its OWN path from battery positive to battery negative. The key rules are the opposite of series: voltage is the SAME across every branch — each component sees the full battery voltage. Current DIVIDES — each branch draws its own current based on its resistance. And the total current is the sum of all branch currents.
>
> This is why one headlight can blow and the other stays on. Each has its own path. The blown bulb's branch carries zero current, but the other branch is unaffected. This is the fundamental reason almost every load in a car is wired in parallel."

**PPT Content:**
```
PARALLEL CIRCUITS — Multiple Paths

Rules:
1. VOLTAGE is the SAME across every branch
   V(total) = V(R1) = V(R2) = V(R3)

2. CURRENT DIVIDES between branches
   I(total) = I(R1) + I(R2) + I(R3)

3. TOTAL RESISTANCE DECREASES
   1/R(total) = 1/R1 + 1/R2 + 1/R3

Example: Two 6-ohm loads in parallel on 12V
1/R(total) = 1/6 + 1/6 = 2/6 --> R(total) = 3 ohm
I(total) = 12 / 3 = 4 A
I per branch = 12 / 6 = 2 A each (adds to 4 A)

ADVANTAGE: One component fails, others keep working
This is why MOST vehicle loads are wired in parallel.

One headlight out? Other still works. Radio off? Wipers still run.
```

---

#### Slide 13: Series vs Parallel — Side by Side
**Visual:** Two-column comparison table. Left: series circuit diagram with summary rules. Right: parallel circuit diagram with summary rules. Color-coded — blue for voltage, red for current, green for resistance.

**Instructor Narration:**
> "Let me put them side by side so the difference is crystal clear. Series: one path, current same everywhere, voltage divides, resistances add up, one break kills everything. Parallel: multiple paths, voltage same everywhere, current divides, total resistance decreases, one break only affects that branch. In a real car, you'll see both — and combinations. The headlights are in parallel with each other but in series with a fuse and a switch. Understanding both is essential."

**PPT Content:**
```
SERIES vs PARALLEL — The Comparison

                    SERIES              PARALLEL
Current:            Same everywhere     Divides between branches
Voltage:            Divides across      Same across all branches
                    components
Total resistance:   R1 + R2 + R3        Less than smallest R
One component       Entire circuit      Only that branch
fails:              goes dead           is affected
Automotive use:     Fuse + switch +     Multiple loads from
                    load in one path    same supply

IN A REAL CAR:
Loads are in PARALLEL (independent operation)
But each load path has SERIES elements:
Battery -> Fuse -> Switch -> Load -> Ground
(all in SERIES within that one parallel branch)
```

---

#### Slide 14: Combination Circuits — The Real World
**Visual:** Realistic automotive circuit: battery -> main fuse -> junction box -> three parallel branches each containing a fuse in series with a load (headlight, blower motor, radio). All sharing a common ground point.

**Instructor Narration:**
> "In practice, every automotive circuit is a combination. Look at this: the battery feeds a main fuse, then a junction box that splits into parallel branches. Each branch has its own fuse in series with its load. The fuse protects that individual branch. If the blower motor shorts, its fuse blows — but the headlights and radio keep working because they're on separate parallel branches. This is the standard architecture of every vehicle electrical system. Master this concept and you'll understand every wiring diagram you ever read."

**PPT Content:**
```
COMBINATION CIRCUITS — Real Automotive Architecture

Battery (+) --> Main Fuse --> Fuse Box
                                |
                   +------------+------------+
                   |            |            |
               Fuse 1       Fuse 2       Fuse 3
                   |            |            |
              Headlight    Blower Motor    Radio
                   |            |            |
                   +------------+------------+
                                |
                            Ground (-)

Each branch: SERIES (fuse -> load)
Between branches: PARALLEL (independent)

Result:
• Each load gets full 12V (parallel advantage)
• Each load is individually protected (series fuse)
• One fault affects only one branch
```

---

### **DEVELOPMENT PART 2: Circuit Faults** (Slides 15-19, ~25 minutes)

**Narrative Voice:** Problem-focused, diagnostic. "What goes wrong and what does it look like?"

---

#### Slide 15: The Three Fault Types — Overview
**Visual:** Three columns, each with a circuit diagram showing the fault, a photo of the real-world cause, and the symptom. Open circuit = broken wire, Short circuit = bare wires touching, High resistance = corroded terminal.

**Instructor Narration:**
> "Every electrical problem in every car you will ever work on falls into one of three categories. Open circuit — the path is broken, no current flows, the component is dead. Short circuit — current takes an unintended shortcut, too much current flows, the fuse blows or something burns. High resistance — the path exists but is restricted, not enough current flows, the component works poorly. Three faults. Three patterns. Learn to recognise them and you can diagnose anything."

**PPT Content:**
```
THREE CIRCUIT FAULTS — Every Problem Is One of These

1. OPEN CIRCUIT
   Path is broken --> No current flows --> Component dead

2. SHORT CIRCUIT
   Unintended path --> Excessive current --> Fuse blows / fire risk

3. HIGH RESISTANCE
   Path is restricted --> Reduced current --> Poor performance / heat

Every electrical fault you will ever diagnose is one of these three.
Learn the symptoms. Learn to test for each one.
That is electrical diagnostics.
```

---

#### Slide 16: Open Circuit — The Broken Path
**Visual:** Circuit diagram with a gap in the wire. Real-world photos: blown fuse, broken wire end, corroded connector pulled apart with green corrosion, unplugged sensor connector. Voltmeter showing battery voltage across the open point.

**Instructor Narration:**
> "An open circuit means the path is broken somewhere. No current can flow. The component is completely dead — no partial operation, just nothing. Causes? Blown fuse, broken wire, corroded connector that's lost contact, an unplugged sensor, a burned-out bulb filament. The symptom is always the same: NOTHING happens.
>
> Here's the diagnostic clue: if you measure voltage across an open point, you'll see FULL battery voltage. Why? Because the entire voltage 'drops' across the break. There's no current flowing, so there's no voltage drop across any other component — all the voltage appears at the break. This is called 'voltage available but no current flowing' and it's the signature of an open circuit."

**PPT Content:**
```
FAULT 1: OPEN CIRCUIT — The Broken Path

What happens: Path broken, no current flows, component dead
Symptom: Component completely non-functional (not dim, not slow — DEAD)

Common causes:
• Blown fuse (designed to open = safety feature)
• Broken wire (vibration, rubbing, rodent damage)
• Corroded connector (green/white buildup breaks contact)
• Unplugged sensor or actuator
• Burned-out bulb filament
• Failed switch (internal contact broken)

Diagnostic clue:
Full battery voltage measured ACROSS the break point
(All voltage drops at the open — no current, no other drops)

Test: Check continuity with ohmmeter (power OFF)
Infinite resistance = open circuit confirmed
```

---

#### Slide 17: Short Circuit — The Unintended Path
**Visual:** Circuit diagram showing current bypassing the load through an unintended path to ground. Photos: melted wire insulation, chafed wiring harness against metal bracket, water-damaged connector with tracking. A blown fuse close-up.

**Instructor Narration:**
> "A short circuit is the opposite problem — current finds a shortcut that bypasses the load. Usually, this means a wire's insulation has been damaged and the bare copper touches the vehicle body — which is the ground path. Now current flows from battery positive through the wire directly to ground with almost no resistance. What does Ohm's Law tell us? If resistance drops to nearly zero, current goes through the roof. I = V / R = 12 / 0.01 = 1200 amps! That's why fuses exist — they blow before the wire melts and starts a fire.
>
> Causes? Chafed insulation where a harness rubs on a metal bracket. Pinched wires from improper panel installation. Water ingress creating tracking paths. A faulty component with internal short. The symptom is either a blown fuse or — if there's no fuse — smoke and fire. Never, ever bypass a fuse with wire or foil. The fuse is the last line of defence."

**PPT Content:**
```
FAULT 2: SHORT CIRCUIT — The Unintended Path

What happens: Current bypasses load via low-resistance shortcut
Symptom: Fuse blows immediately / repeatedly. Smoke. Heat. FIRE RISK.

Why it's dangerous (Ohm's Law):
If R drops from 2.4 ohm (normal) to 0.01 ohm (short):
I = 12 / 0.01 = 1,200 A (!)
Without a fuse, the wire becomes a heating element.

Common causes:
• Chafed insulation (harness rubbing on bracket or sharp edge)
• Pinched wire (door jamb, panel reinstallation)
• Water ingress (creates conductive path)
• Internal component failure
• Improper repair (wrong wire gauge, bad splice)

Protection: FUSES — designed to open before fire starts

NEVER bypass a fuse with wire, foil, or a higher-rated fuse.
Fuses are NOT inconveniences. They SAVE LIVES.
```

---

#### Slide 18: High Resistance — The Hidden Fault
**Visual:** Circuit diagram with a resistance symbol at a connector. Side-by-side photos: bright headlight vs dim headlight (high resistance in circuit). Thermal image showing a hot connector. Corroded ground strap.

**Instructor Narration:**
> "This is the sneaky one. The circuit works — kind of. But something isn't right. The headlight is dim. The starter motor cranks slowly. The window motor is sluggish. The cause? Extra resistance where there shouldn't be any. A corroded connector, a damaged wire with broken strands, a loose ground connection, oxidised terminal.
>
> What's happening electrically? The unwanted resistance creates a voltage drop BEFORE the load. If a corroded connector drops 3 volts, the headlight only gets 9 volts instead of 12. That's a 25% power reduction — the light is noticeably dimmer. And here's the dangerous part: that 3 volts dropped across the corroded connector is converted to HEAT. I've seen connectors melt through, harnesses catch fire, all from a connector that 'looked okay' from the outside.
>
> Voltage drop testing is how you find high resistance faults. We'll practice it extensively on Day 9."

**PPT Content:**
```
FAULT 3: HIGH RESISTANCE — The Sneaky One

What happens: Unwanted resistance restricts current flow
Symptom: Component works but POORLY — dim, slow, weak, hot

Common causes:
• Corroded connector (green/white oxidation)
• Loose terminal (not fully seated, backed out)
• Damaged wire (broken strands reduce cross-section)
• Corroded ground point (paint under ground bolt)
• Worn switch contacts (internal resistance increases with age)

The physics:
Normal: 12V across headlight = full brightness
With 3V lost at bad connector: 9V across headlight = dim
That missing 3V = HEAT at the connector (fire risk!)

Finding it: VOLTAGE DROP TESTING
Measure voltage across each connection while circuit is ON.
Good connection: < 0.1V drop
Bad connection: > 0.5V drop = PROBLEM

Day 9: You will master voltage drop testing.
```

---

#### Slide 19: Fault Summary — The Diagnostic Matrix
**Visual:** Table with three rows (open, short, high resistance) and columns (symptom, current flow, voltage at fault, fuse status, danger level, test method). Color coded: red for dangerous, yellow for degraded, grey for dead.

**Instructor Narration:**
> "Here's your diagnostic cheat sheet. Memorise this table. Open circuit: component dead, no current, full voltage at the break, fuse intact. Short circuit: fuse blows, excessive current, near-zero voltage at short point, fuse blown, fire danger. High resistance: component weak, reduced current, voltage dropped at the bad connection, fuse intact, heat danger. Three patterns, three sets of symptoms. On Day 10, we'll build systematic procedures to find each one."

**PPT Content:**
```
FAULT DIAGNOSTIC MATRIX

                 OPEN          SHORT           HIGH RESISTANCE
Symptom:         Dead          Fuse blows      Weak/dim/slow
Current:         Zero          Excessive       Reduced
Voltage at       Full battery  Near zero       Partial drop
fault:           voltage                       (0.5V-5V)
Fuse:            Intact        BLOWN           Intact
Danger:          None          FIRE risk       HEAT / melt
Test method:     Continuity    Resistance to   Voltage drop
                 test (ohms)   ground          test (V)

When you find an electrical problem, ask:
"Is the component dead, blown, or weak?"
Dead = open. Blown fuse = short. Weak = high resistance.
```

---

### **DEVELOPMENT PART 3: Reading Wiring Diagrams** (Slides 20-23, ~15 minutes)

**Narrative Voice:** Practical, reference-focused. "This is the language you need to read."

---

#### Slide 20: Wiring Diagram Symbols
**Visual:** Grid of common automotive electrical symbols, each with its standard symbol and name. Organized into categories: power sources, protection, switches, loads, connections.

**Instructor Narration:**
> "Wiring diagrams are the maps of the electrical system. Like any map, they use symbols. You need to recognise these instantly — they're the same across almost all manufacturers, though some have minor variations. Battery, fuse, switch, ground, relay, motor, resistor, LED, bulb, connector, splice point. Learn these and you can read any wiring diagram in any workshop manual. Don't try to memorise them all now — they'll become second nature through use."

**PPT Content:**
```
WIRING DIAGRAM SYMBOLS — The Electrical Alphabet

POWER SOURCES:              PROTECTION:
[Battery symbol]  Battery   [Fuse symbol]    Fuse
[Alternator]     Alternator [Circuit breaker] Circuit breaker

SWITCHES:                   LOADS:
[Open switch]    Switch     [Bulb symbol]    Lamp/Bulb
[Relay symbol]   Relay      [Motor symbol]   Motor
                            [Resistor]       Resistor
CONNECTIONS:                [LED]            LED
[Ground symbol]  Ground     [Heater]         Heating element
[Connector]      Connector  [Solenoid]       Solenoid/coil
[Splice]         Splice
[No connection]  Crossing wires (no connection)

These symbols are UNIVERSAL across most manufacturers.
Learn them once, read any wiring diagram.
```

---

#### Slide 21: The Relay — A Switch Controlled by a Switch
**Visual:** Relay internal diagram showing coil, contacts, terminal numbering (30, 85, 86, 87). A circuit showing a small switch controlling the relay coil, which controls a high-current load. Real relay photo with terminal numbers visible.

**Instructor Narration:**
> "The relay deserves special attention because it confuses beginners. A relay is simply a switch that's controlled by electricity instead of your finger. It has a small coil inside — when you send a small current through the coil, it creates a magnetic field that pulls a contact closed, allowing a large current to flow to the load. Why not just use a big switch? Because the dashboard switch would need thick, expensive wiring to carry 20 amps to a headlight. Instead, the thin dashboard switch controls the relay coil — maybe 0.2 amps — and the relay handles the heavy current right at the fuse box. Terminal 30 is battery power in. Terminal 87 is power out to the load. Terminals 85 and 86 are the coil control. You'll see relays everywhere."

**PPT Content:**
```
THE RELAY — A Switch Controlled By Electricity

Why: Small switch controls large current without heavy wiring to dash

How it works:
Small current through COIL (85/86) --> Magnetic field pulls CONTACTS closed
--> Large current flows from 30 to 87 --> Load operates

Terminal numbers (ISO standard):
30 = Battery power IN (always hot)
87 = Power OUT to load
85 = Coil terminal 1 (usually ground side)
86 = Coil terminal 2 (usually switched positive)
87a = Normally closed contact (some relays)

Automotive examples:
• Headlight relay (30A through relay, 0.2A through dash switch)
• Horn relay, fuel pump relay, starter relay
• Fan relay, AC compressor clutch relay

Think: "The relay is the muscle. The switch is the brain."
```

---

#### Slide 22: Reading a Simple Wiring Diagram
**Visual:** A complete but simple wiring diagram: battery positive -> fuse F12 (15A) -> headlight switch -> headlight relay coil (85/86) -> ground. Relay power side: battery -> fuse F5 (30A) -> relay 30-87 -> left headlight -> ground. Current path highlighted with arrows.

**Instructor Narration:**
> "Let's read a real diagram. Follow the current path with me. Battery positive to Fuse F12 — that protects the control circuit. Through the headlight switch on the dashboard — that's the driver's input. Through the relay coil at terminals 86 and 85 to ground. Now the relay is energised. On the power side: battery positive through Fuse F5 — a bigger fuse for the heavy current — into the relay at terminal 30, out at terminal 87, through the headlight, and back to ground. Two circuits working together — a small control circuit and a large power circuit. This is the pattern behind almost every high-current system in a car."

**PPT Content:**
```
READING A WIRING DIAGRAM — Follow the Current

CONTROL CIRCUIT (thin wires, small fuse):
Battery (+) --> Fuse F12 (15A) --> Headlight Switch
--> Relay Coil (86) --> Relay Coil (85) --> Ground (-)

POWER CIRCUIT (thick wires, large fuse):
Battery (+) --> Fuse F5 (30A) --> Relay (30)
--> Relay (87) --> Headlight --> Ground (-)

How to read ANY wiring diagram:
1. Start at Battery (+)
2. Follow the line through fuses, switches, relays
3. Through the load (component doing work)
4. Back to Ground (-) completing the circuit
5. No complete path = no current flow

CONNECTOR IDs: C101, C102... identify physical connector locations
WIRE COLOURS: BK=Black, RD=Red, GN=Green, BU=Blue, YE=Yellow, WH=White
```

---

#### Slide 23: Wiring Diagram Tips for Beginners
**Visual:** Annotated wiring diagram with callout boxes pointing to key features: connector IDs, wire colour codes, ground symbols, splice points, fuse references, component reference numbers.

**Instructor Narration:**
> "A few tips that will save you hours of frustration. First: always trace from power to ground — follow the current path. Second: connector IDs tell you where to physically find connectors on the car — C101 might be in the engine bay, C205 under the dashboard. Your workshop manual has a connector location guide. Third: wire colour codes are your friend — BK is black, RD is red, GN is green. If the diagram says there should be a red wire with a yellow stripe at connector C103, go find it. Fourth: the ground symbol tells you where the circuit returns to battery negative — and ground points are a common failure point. Corroded ground point? That's your high resistance fault."

**PPT Content:**
```
WIRING DIAGRAM TIPS

1. TRACE POWER TO GROUND
   Start at (+), follow through every component, end at (-)
   If you can't complete the path, there's a problem

2. CONNECTOR IDs (C101, C205, X422)
   Tell you WHERE to find the physical connector
   Workshop manual has connector location diagrams

3. WIRE COLOUR CODES
   BK = Black    RD = Red     GN = Green
   BU = Blue     YE = Yellow  WH = White
   BR = Brown    OG = Orange  VT = Violet
   Stripe = second colour (RD/YE = red with yellow stripe)

4. GROUND POINTS
   Marked with ground symbol on diagram
   Common failure point — always inspect ground connections

5. FUSE REFERENCE
   Diagram shows fuse number and rating
   Cross-reference to fuse box diagram for location
```

---

### **PRACTICAL: Build, Measure, Diagnose** (Slides 24-26, ~75 minutes)

**Narrative Voice:** Hands-on, coaching, encouraging experimentation.

---

#### Slide 24: Practical Activity 1 — Build & Measure (30 minutes)
**Visual:** Photo of an automotive training board or breadboard with a power supply, resistors, bulbs, switches, and a multimeter. Step-by-step instruction cards visible.

**Instructor Narration:**
> "Time to get hands-on. Each pair gets a training board, a 12-volt power supply, resistors, bulbs, switches, and a multimeter. Activity one: Build a series circuit with two resistors. Measure the current at three different points — confirm it's the same everywhere. Measure the voltage across each resistor — confirm they add up to 12 volts. Record your measurements. Then rebuild as a parallel circuit. Measure the voltage across each branch — confirm they're the same. Measure the current in each branch and the total — confirm the branch currents add up to the total. You're proving Ohm's Law with your own hands."

**PPT Content:**
```
PRACTICAL 1: BUILD & MEASURE (30 min)

Equipment per pair:
• Training board / breadboard
• 12V DC power supply
• Resistors: 100 ohm, 220 ohm, 330 ohm
• Miniature bulbs (12V)
• Switches
• Multimeter (instructor will demonstrate basic use)
• Recording worksheet

TASK A — Series Circuit:
1. Connect two resistors in SERIES with 12V supply
2. Measure current at 3 points — IS IT THE SAME?
3. Measure voltage across each resistor — DO THEY ADD TO 12V?
4. Calculate expected values using Ohm's Law — DO THEY MATCH?

TASK B — Parallel Circuit:
1. Reconnect same resistors in PARALLEL
2. Measure voltage across each — IS IT THE SAME (12V)?
3. Measure current in each branch and total
4. DO branch currents ADD UP to total?

Record ALL measurements on your worksheet.
```

---

#### Slide 25: Practical Activity 2 — Fault Simulation (30 minutes)
**Visual:** Training board with a fault introduced — one wire disconnected (open circuit), a jumper wire bypassing a load (short circuit), a high-value resistor inserted at a connector (high resistance). Instructor standing by with multimeter.

**Instructor Narration:**
> "Now the fun part. I'm going to introduce faults into your circuits — and you have to find them using your multimeter. I might disconnect a wire — open circuit. I might add a jumper that bypasses your load — short circuit simulation. I might add an extra resistor at a connector — high resistance. Your job: identify WHICH fault type it is, WHERE it is, and PROVE it with a measurement. This is what real diagnostics feels like. You have 30 minutes. I'll introduce three different faults to each pair."

**PPT Content:**
```
PRACTICAL 2: FAULT SIMULATION (30 min)

SCENARIO: Your working circuit suddenly has a problem.
The instructor has introduced a fault. Find it.

FAULT A: Component is completely dead
--> What type of fault? How do you confirm?

FAULT B: Fuse blows as soon as circuit is powered
--> What type of fault? How do you locate the short?

FAULT C: Bulb is dim / motor is slow
--> What type of fault? Where is the extra resistance?

For each fault:
1. OBSERVE the symptom
2. IDENTIFY the fault type (open / short / high resistance)
3. LOCATE the fault point using your multimeter
4. PROVE it with a measurement
5. EXPLAIN your reasoning to the instructor

This is the beginning of diagnostic thinking.
```

---

#### Slide 26: Practical Activity 3 — Wiring Diagram Tracing (15 minutes)
**Visual:** Printed wiring diagram of a simple automotive circuit (e.g., horn circuit with relay, fuse, switch, horn). Blank worksheet for learners to trace current paths and identify components.

**Instructor Narration:**
> "Final activity. Each pair gets a printed wiring diagram. Your task: trace the current path from battery positive to ground. Identify every component in the circuit by name. Write down the fuse number and rating. Identify the connector IDs. Mark where you would place a multimeter to check for each of the three fault types. This is reading comprehension for circuits — and it's a skill you'll use every single day."

**PPT Content:**
```
PRACTICAL 3: WIRING DIAGRAM TRACING (15 min)

You receive a printed wiring diagram (horn circuit).

TASK:
1. Trace the current path with a highlighter:
   Battery (+) --> ... --> ... --> Ground (-)

2. List every component by name and symbol

3. Identify:
   • Fuse number and rating
   • Relay terminals
   • Connector IDs
   • Ground point location

4. Mark on the diagram:
   • Where to test for an OPEN circuit
   • Where to test for a SHORT circuit
   • Where to test for HIGH RESISTANCE

Compare answers with your partner, then with the class.
```

---

### **WRAP-UP: Consolidation & Preview** (Slides 27-28, ~15 minutes)

---

#### Slide 27: What You Learned Today
**Visual:** Summary grid with the day's key concepts, each with a checkmark and a one-line description. The Ohm's Law triangle prominently displayed.

**Instructor Narration:**
> "Let's take stock. You walked in this morning knowing that cars have electronics. You walk out understanding the PHYSICS behind them. You know what voltage, current, and resistance are. You can use Ohm's Law to calculate any of the three. You understand how series and parallel circuits behave differently. You can name the three fault types and describe their symptoms. And you've built real circuits, measured real values, and found real faults. That's a massive step forward.
>
> Tomorrow we add components to your vocabulary — relays in detail, fuses and circuit breakers, connectors and crimping, wire types and sizing. Day 7 was the physics. Day 8 is the hardware."

**PPT Content:**
```
DAY 7 RECAP — YOU CAN NOW:

V, I, R: Define voltage, current, and resistance with correct units
Ohm's Law: Apply V = IR to calculate any value given the other two
Power: Calculate P = VI for fuse and wire sizing
Series: Explain current same, voltage divides, resistances add
Parallel: Explain voltage same, current divides, resistance decreases
Open circuit: Identify broken path, dead component, test with continuity
Short circuit: Identify unintended path, blown fuse, fire risk
High resistance: Identify restricted path, dim/slow component, voltage drop
Symbols: Recognise battery, fuse, switch, relay, motor, ground, resistor
Diagrams: Trace current path from power to ground through a schematic

TOMORROW — Day 8: Components, Protection & Wiring
Relays (deep dive), fuses, connectors, crimping, wire sizing
```

---

#### Slide 28: Day 8 Preview
**Visual:** Image of automotive electrical components laid out: assorted fuses (blade, cartridge, mega), relays, crimp terminals, wire strippers, connector housings, heat shrink tubing, wiring loom tape.

**Instructor Narration:**
> "Tomorrow is about the physical hardware — the components that make up every circuit. You'll learn how fuses are rated and sized. You'll work with relays hands-on — wiring them, testing them, understanding when and why they fail. You'll learn about different connector types and how to properly crimp a terminal that won't pull apart. And you'll understand wire sizing — why the starter cable is as thick as your finger and the interior light wire is as thin as a hair. Bring your hands — it's a practical-heavy day."

**PPT Content:**
```
DAY 8 PREVIEW: COMPONENTS, PROTECTION & WIRING

What you'll learn:
• Fuse types, ratings, and selection rules
• Relay deep-dive: wiring, testing, common failures
• Circuit breakers and fusible links
• Connector types and terminal crimping
• Wire gauges, current capacity, and insulation types
• Proper repair techniques: solder, crimp, heat shrink

What you'll do:
• Wire a relay circuit from scratch
• Crimp connectors to professional standard
• Select correct fuse and wire gauge for a given load
• Repair a damaged harness section

Bring your hands. Day 8 is workshop-heavy.
```

---

## Assessment Checkpoint

**Formative (not graded):**
- Ohm's Law calculation quiz: Given two of three values (V, I, R), calculate the third — 5 questions, automotive scenarios (headlight, starter motor, blower motor, heated seat, horn)
- Fault identification: Given three circuit symptoms, identify fault type (open, short, high resistance) and explain reasoning
- Practical measurement verification: Measured values from training board circuits compared against calculated values — within 10% tolerance
- Wiring diagram tracing: Correctly trace current path and identify at least 5 components from a printed diagram

---

## Key Takeaways

1. Voltage (V) is electrical pressure, Current (I) is electron flow, Resistance (R) is opposition — the water pipe analogy makes this intuitive
2. Ohm's Law (V = IR) and Power (P = VI) are the two equations that solve every automotive electrical calculation — fuse sizing, wire selection, fault analysis
3. Series circuits: current same, voltage divides — explains voltage drop testing
4. Parallel circuits: voltage same, current divides — explains why vehicle loads are independent
5. Every electrical fault is one of three types: open (dead), short (blown fuse/fire), or high resistance (weak/hot) — knowing this simplifies all diagnostics
6. Wiring diagrams are circuit maps — learn the symbols, trace power to ground, and you can read any vehicle schematic

---

## Preparation for Day 8

**Instructor prep:**
- Prepare relay wiring stations: 12V supply, 4-pin and 5-pin relays, wiring, fuses, loads (bulbs or small motors), terminal connectors
- Assemble crimp tool stations: wire strippers, crimpers (ratchet type preferred), assorted terminals (ring, spade, bullet, weather-pack), heat shrink tubing, heat gun
- Gather fuse samples: mini blade, standard blade, maxi/cartridge, mega fuse, fusible link — including blown examples of each
- Prepare connector samples: OEM connectors (weather-pack, Metri-Pack, Deutsch), aftermarket connectors, damaged connector examples
- Print relay wiring exercise sheets with terminal diagrams
- Prepare wire gauge demonstration: 0.5mm2 through 25mm2 samples with current capacity labels

**Learner prep:**
- Review Ohm's Law triangle — practice 5 calculations at home
- Review the three fault types and their symptoms
- Bring notebook with today's measurements for reference
