---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 2
week_title: "Speaking Electricity"
day_number: 8
session_title: "Components, Protection & Wiring Craft"
duration_minutes: 180
theory_practice: "25:75"
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 8: Components, Protection & Wiring Craft
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (45 min theory + 135 min practical)
**Approach:** Skills-Based — Learn It, Then Do It
**PPT Target:** 26-27 slides
**Week:** 2 of 8 — "Speaking Electricity"

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Explain the construction and operation of an automotive relay (coil, armature, contacts)
- Test a relay with a multimeter (coil resistance and contact continuity)
- Identify fuse types (mini blade, standard blade, maxi blade, cartridge) and read their colour codes
- Test a fuse visually and with a multimeter
- Read and interpret a vehicle fuse box diagram
- Produce a mechanically sound soldered wire-to-wire joint with heat shrink insulation
- Crimp ring, spade, and pin terminals to the correct standard and pass a pull test
- Decide when to solder vs when to crimp based on application context

**This is the most hands-on day of Week 2.** Day 7 gave learners circuit theory (V=IR, series/parallel). Day 8 puts physical components in their hands and teaches them the craft of working with wire. By the end, every learner should have produced real, testable joints.

---

## Connection to Prior Knowledge

Build from **Day 7 — Circuit Theory & Ohm's Law**:
- Learners understand voltage, current, resistance, and power
- They can calculate circuit values and predict behaviour
- They know series and parallel configurations
- They have used a multimeter for basic resistance and voltage measurements

**Bridge:** "Yesterday you learned to think about circuits. Today you learn to build and fix them. The theory told you WHY a circuit works. Today you'll meet the components that MAKE it work — and you'll learn the craft of joining wires that won't fail in a vibrating, heat-cycling, salt-sprayed vehicle."

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: From Theory to Physical Reality** (Slides 1-3, ~10 minutes)

**Narrative Voice:** Energetic, practical. Today is about getting hands dirty.

---

#### Slide 1: Title & Context
**Visual:** Split image — left side shows a neat relay/fuse box under a vehicle bonnet; right side shows a technician soldering a wiring repair under a dashboard

**Instructor Narration:**
> "You know V=IR. You can calculate current in a circuit. But a circuit isn't a diagram on paper — it's copper wire, plastic connectors, fuses that blow, and relays that click. Today we get physical. You're going to hold relays, test fuses, solder wires, and crimp terminals. This is the most hands-on day of the week, and by the end of it, you'll have real skills that you'll use on every single repair job."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 2: Speaking Electricity
Day 8: Components, Protection & Wiring Craft

Theory told you WHY. Today you learn HOW.
```

---

#### Slide 2: Why This Matters
**Visual:** Three photos stacked — (1) A melted wiring harness from a bad connection, (2) A cold solder joint that failed causing intermittent fault, (3) A properly crimped terminal with heat shrink

**Instructor Narration:**
> "Let me show you what happens when wiring work is done badly. Photo one: a melted harness. Someone bypassed a fuse with a piece of wire. The wire couldn't handle the current, it overheated, and it melted the insulation off neighbouring wires. That's a fire hazard. Photo two: a cold solder joint. It looked fine on the outside, but it had high resistance. Every time the car hit a bump, the connection broke and the headlights flickered. Took the dealer three visits to find it. Photo three: that's what good work looks like. Clean crimp, heat shrink, tested. It'll last the life of the car.
>
> The difference between those three outcomes? Skill. That's what we're building today."

**PPT Content:**
```
WHY WIRING CRAFT MATTERS

BAD connection = intermittent faults, customer comebacks, fire risk
GOOD connection = reliable, durable, professional

A technician who can't make a solid wire joint
is like a surgeon who can't tie a suture.

TODAY: You learn to do it RIGHT.
```

---

#### Slide 3: Today's Plan
**Visual:** Horizontal timeline with six blocks — colour-coded theory (blue) and practical (green), with green dominating

**Instructor Narration:**
> "Here's how the day breaks down. Short theory on relays, then short theory on fuses — then straight to the bench to test them. After that, I'll demonstrate soldering and crimping techniques, and then you'll spend the rest of the session at the wiring stations. By the end, you'll have tested relays, identified fuses, soldered five joints, crimped ten terminals, and repaired a simulated wiring fault. Let's go."

**PPT Content:**
```
TODAY'S PLAN (180 minutes)

THEORY: Relays — construction, operation, testing    (20 min)
THEORY: Fuses — types, ratings, testing              (15 min)
PRACTICAL 1: Relay testing + fuse identification      (40 min)
DEMO: Soldering & crimping techniques                 (10 min)
PRACTICAL 2: Wiring craft stations                    (70 min)
WRAP-UP: Quality check + Day 9 preview                (15 min)

Theory : Practice = 25 : 75
This is a HANDS-ON day.
```

---

### **DEVELOPMENT PART 1: Relays** (Slides 4-9, ~20 minutes)

**Narrative Voice:** Technical but accessible. Use the "invisible switch" metaphor.

---

#### Slide 4: What Is a Relay?
**Visual:** Annotated cutaway diagram of a standard automotive relay — coil winding, iron core, armature, spring, normally-open contacts, common terminal

**Instructor Narration:**
> "A relay is a switch that's operated by electricity instead of your finger. Why would you want that? Because some circuits carry high current — headlights pull 10 amps, a starter motor pulls 200 amps. You don't want 200 amps running through the ignition switch under your steering column. Instead, the ignition switch sends a tiny current — maybe half an amp — through a relay coil. That coil becomes an electromagnet, pulls an armature, and closes a set of heavy-duty contacts that carry the 200 amps to the starter. Small current controls big current. That's the relay's job."

**PPT Content:**
```
WHAT IS A RELAY?

An electrically operated switch

WHY?
Small control current (0.1 - 0.5 A) switches high load current (10 - 80 A)
Keeps high current AWAY from dashboard switches and ECUs

CONSTRUCTION:
• Coil winding (creates magnetic field when energised)
• Iron core (concentrates magnetic field)
• Armature (movable iron piece pulled by magnetic field)
• Return spring (opens contacts when coil de-energised)
• Contact set (carries the load current)
• Terminals (pins connecting to vehicle wiring)
```

---

#### Slide 5: How a Relay Works — Step by Step
**Visual:** Four-frame animation sequence — (1) Relay at rest, contacts open. (2) Current flows through coil, magnetic field forms. (3) Armature pulled down, contacts close. (4) Load circuit completes, current flows to headlight/motor.

**Instructor Narration:**
> "Let's walk through it step by step. Frame one: relay at rest. The spring holds the armature up. The contacts are open. No current flows to the load. Frame two: the ECU or switch sends current through the coil — terminals 85 and 86 on a standard ISO relay. The coil becomes a magnet. Frame three: the magnetic field pulls the armature down against the spring. The movable contact touches the fixed contact. Frame four: now terminal 30 is connected to terminal 87. The load circuit is complete. Current flows from the battery, through the relay contacts, to the headlight, and the light turns on.
>
> Release the coil current, the spring pushes the armature back, contacts open, light goes off. Simple, reliable, been used in cars for decades."

**PPT Content:**
```
HOW A RELAY WORKS

STEP 1: Relay at rest — spring holds contacts OPEN
STEP 2: Control current energises coil (terminals 85/86)
STEP 3: Coil magnetism pulls armature — contacts CLOSE
STEP 4: Load current flows (terminals 30 → 87)

RELEASE coil → spring returns → contacts OPEN → load OFF

ISO TERMINAL NUMBERING:
  85 = Coil (+)        86 = Coil (-)
  30 = Common (battery) 87 = Normally Open (load)
                         87a = Normally Closed (if changeover)
```

---

#### Slide 6: Relay Types
**Visual:** Three relay types side by side — (1) SPST-NO (4-pin), (2) SPDT changeover (5-pin), (3) Twin relay/dual output. Each with schematic symbol and pin diagram.

**Instructor Narration:**
> "There are three relay types you'll commonly see. First: the basic 4-pin relay. It's Single Pole, Single Throw, Normally Open — SPST-NO. When the coil is off, the contacts are open. Energise the coil, contacts close. This is your standard headlight relay, horn relay, fuel pump relay.
>
> Second: the 5-pin changeover relay. It has a normally-open contact AND a normally-closed contact. Terminal 87a is connected when the coil is OFF, terminal 87 is connected when the coil is ON. This type is used when you need to switch between two circuits — like switching between main beam and dipped beam.
>
> Third: you'll occasionally see dual-output or twin relays in specific applications like ABS or ECU power supply. Know the first two and you'll cover 95% of what you encounter."

**PPT Content:**
```
RELAY TYPES

1. SPST-NO (4-pin) — Most common
   Coil OFF → contacts OPEN
   Coil ON  → contacts CLOSED
   Use: Headlights, horn, fuel pump, cooling fan

2. SPDT Changeover (5-pin)
   Coil OFF → 30 connected to 87a (Normally Closed)
   Coil ON  → 30 connected to 87  (Normally Open)
   Use: Beam switching, HVAC mode selection

3. Dual / Twin (application-specific)
   Two relay circuits in one housing
   Use: ABS module, ECU power supply

YOU NEED TO KNOW: Types 1 and 2
```

---

#### Slide 7: Testing a Relay with a Multimeter
**Visual:** Step-by-step photos — (1) Multimeter on resistance mode across coil pins 85/86, display showing ~70 ohms. (2) Multimeter on continuity mode across 30/87, display showing OL (open). (3) 12V battery connected to 85/86, audible click, then multimeter across 30/87 showing 0 ohms.

**Instructor Narration:**
> "Testing a relay is one of the most common diagnostic tasks. Here's how. Step one: remove the relay from the fuse box. Set your multimeter to resistance — the omega symbol. Measure across the coil terminals, 85 and 86. A good coil reads between 50 and 120 ohms typically. If you get OL — open line — the coil winding is broken. Relay is dead.
>
> Step two: measure across the load contacts, 30 and 87. With the coil NOT energised, you should get OL — the contacts are open. If you get near zero ohms, the contacts are welded shut. That's a failure mode we see with high-current relays like starter relays.
>
> Step three: apply 12 volts to the coil — pin 85 to positive, pin 86 to negative. You should hear a click. Now measure 30 to 87 again — should read near zero ohms. Contacts closed. Remove the 12 volts, you hear another click, and the reading goes back to OL. If all three checks pass, your relay is good."

**PPT Content:**
```
TESTING A RELAY — 3-STEP METHOD

STEP 1: COIL RESISTANCE (pins 85-86)
  Multimeter → Resistance (Ω)
  Good reading: 50 - 120 Ω (typical)
  OL (open) = broken coil winding → REPLACE

STEP 2: CONTACTS AT REST (pins 30-87)
  Multimeter → Resistance (Ω)
  Good reading: OL (open) for NO relay
  Near 0 Ω at rest = welded contacts → REPLACE

STEP 3: CONTACTS ENERGISED
  Apply 12V to pins 85/86 (listen for CLICK)
  Measure pins 30-87 → should read near 0 Ω
  Remove 12V → should return to OL

ALL 3 PASS = relay is serviceable
```

---

#### Slide 8: Common Automotive Relay Applications
**Visual:** Vehicle diagram with callout boxes showing relay locations and functions — headlight relay, fuel pump relay, horn relay, starter relay, cooling fan relay, window relay

**Instructor Narration:**
> "Where do you find relays in a car? Everywhere. The headlight relay handles the high beam and low beam circuits. The fuel pump relay powers the fuel pump — the ECU controls when it runs. The horn relay — you press the horn button on the steering wheel, that sends a tiny current to the relay, and the relay switches the horn's high-current circuit. The starter relay is the biggest — it handles the massive current draw of the starter motor. Cooling fan relays switch the radiator fan on and off based on coolant temperature.
>
> Most of these live in the main fuse box under the bonnet. Some vehicles have a secondary relay box inside the cabin. Your fuse box cover diagram will show you where each relay sits."

**PPT Content:**
```
COMMON AUTOMOTIVE RELAY APPLICATIONS

Relay               Load Current    Location
─────────────────────────────────────────────
Headlight relay     10-15 A        Underbonnet fuse box
Fuel pump relay     8-12 A         Underbonnet fuse box
Horn relay          15-25 A        Underbonnet fuse box
Starter relay       80-200 A       Near battery / starter
Cooling fan relay   25-40 A        Underbonnet fuse box
A/C compressor      10-15 A        Underbonnet fuse box
Power window        20-30 A        Door module / cabin box
Wiper relay         8-15 A         Cabin fuse box

Relay location → shown on fuse box cover diagram
```

---

#### Slide 9: Relay Failure Modes
**Visual:** Three failed relays — (1) Burnt coil (discoloured, melted housing), (2) Pitted/welded contacts (macro photo), (3) Corroded terminals

**Instructor Narration:**
> "Relays fail in three ways. First: coil burnout. The coil winding breaks or shorts. The relay won't click, and you'll read OL across 85/86. Second: contact welding. High inrush currents — especially on starter relays and fuel pump relays — can cause the contacts to weld together. The load stays on permanently. This is dangerous — a welded fuel pump relay keeps the fuel pump running even with the ignition off. Third: terminal corrosion. Water ingress or condensation corrodes the pins, creating high-resistance connections that cause voltage drops and intermittent faults. Always check the relay socket as well as the relay itself."

**PPT Content:**
```
RELAY FAILURE MODES

1. COIL BURNOUT
   Symptom: Relay doesn't click
   Test: OL across pins 85/86
   Cause: Over-voltage, heat damage, age

2. CONTACT WELDING
   Symptom: Load stays ON permanently
   Test: Near 0 Ω across 30/87 even without coil energised
   Cause: High inrush current, arcing, end-of-life

3. TERMINAL CORROSION
   Symptom: Intermittent operation, voltage drop
   Test: Visual inspection, high resistance at pins
   Cause: Water ingress, condensation, poor sealing

ALWAYS inspect the relay SOCKET for corrosion too!
```

---

### **DEVELOPMENT PART 2: Fuses** (Slides 10-14, ~15 minutes)

**Narrative Voice:** Clear, safety-focused. Fuses protect people and vehicles.

---

#### Slide 10: Why Fuses Exist
**Visual:** Diagram showing a short circuit — wire touching bare metal, current spike, fuse element melting and breaking the circuit. Contrasted with "no fuse" path showing wire overheating and catching fire.

**Instructor Narration:**
> "A fuse is a sacrificial device. Its job is to die so the wiring doesn't. Here's the scenario: a wire's insulation wears through from vibration, and the bare copper touches the metal body of the car. That's a short circuit — almost zero resistance — and current surges. Without a fuse, the wire carries far more current than it was designed for. It overheats, the insulation melts, and you get a fire. With a fuse, the thin element inside the fuse melts first, breaking the circuit in milliseconds. The wire stays cool, the car doesn't burn. The fuse sacrificed itself to protect everything downstream. That's its entire purpose."

**PPT Content:**
```
FUSES — SACRIFICIAL CIRCUIT PROTECTION

Purpose: Break the circuit BEFORE the wiring overheats

HOW:
• Fuse contains a thin metal element (alloy strip)
• Element rated to carry a specific current safely
• If current exceeds rating → element melts → circuit OPEN

WITHOUT fuse: Short circuit → wire overheats → FIRE
WITH fuse:    Short circuit → fuse blows → circuit safe

A fuse is CHEAP. A wiring harness is EXPENSIVE.
A vehicle fire is CATASTROPHIC.
```

---

#### Slide 11: Fuse Types
**Visual:** Four fuse types photographed at actual size with dimensions labeled — mini blade, standard blade, maxi blade, cartridge (bolt-down). Each shown from front (element visible) and side (terminal pins).

**Instructor Narration:**
> "There are four fuse types you'll work with. Mini blade fuses — the smallest, about 11mm wide, used for low-current circuits like interior lights, sensors, and modules. Standard blade fuses — 19mm wide, the most common, used for headlights, wipers, power windows. Maxi blade fuses — large format, 30mm wide, used for high-current circuits like the blower motor, ABS pump, cooling fan. And cartridge fuses — bolt-down type, used for the highest currents like the alternator feed, main battery distribution. These last ones can handle 60 amps or more.
>
> You need to be able to identify all four on sight. More importantly, you must NEVER replace a fuse with a higher rating. A 10-amp fuse protects wiring rated for 10 amps. Put a 20-amp fuse in its place, and the fuse won't blow until the wire is already on fire."

**PPT Content:**
```
FUSE TYPES

TYPE            WIDTH    CURRENT RANGE   APPLICATION
──────────────────────────────────────────────────────
Mini blade      11 mm    2 - 30 A        Sensors, interior lights, modules
Standard blade  19 mm    3 - 40 A        Headlights, wipers, windows
Maxi blade      30 mm    20 - 100 A      Blower motor, ABS, cooling fan
Cartridge       Bolt-on  30 - 150 A      Main battery feed, alternator

CRITICAL RULE:
NEVER replace a fuse with a HIGHER rating.
Match the original rating EXACTLY.
```

---

#### Slide 12: Fuse Colour Coding
**Visual:** Complete fuse colour chart — each amperage with its standard colour, arranged from lowest to highest

**Instructor Narration:**
> "Fuses are colour-coded by amperage — this is universal across almost all vehicle manufacturers. You don't need to memorise every colour, but you should know the common ones. Grey or violet is 3 amps. Brown is 7.5. Red is 10. Blue is 15. Yellow is 20. Green is 30. The rating is also printed on top of the fuse. But in a dark engine bay, colour recognition is faster. Here's the chart — photograph it with your phone, you'll reference it regularly."

**PPT Content:**
```
FUSE COLOUR CODING (ISO 8820)

COLOUR         RATING      COMMON APPLICATION
────────────────────────────────────────────────
Grey/Violet    2-3 A       Instrument cluster, ECU keep-alive
Tan/Brown      5-7.5 A     Sensors, small actuators
Red            10 A        Tail lights, interior lights
Blue           15 A        Headlights (single), cigarette lighter
Yellow         20 A        Power windows, heated seats
Clear/White    25 A        Wiper motor, sunroof
Green          30 A        Blower motor, cooling fan
Orange/Amber   40 A        Rear window heater
Red (maxi)     50 A        ABS pump
Blue (maxi)    60 A        Main feed circuits

Rating is also PRINTED on top of the fuse body.
```

---

#### Slide 13: Testing Fuses & Reading Fuse Box Diagrams
**Visual:** Split layout — Left: two methods of testing a fuse (visual inspection showing broken element vs intact element, and multimeter continuity test). Right: example fuse box cover diagram with numbered positions, amperage, and circuit descriptions.

**Instructor Narration:**
> "Two ways to test a fuse. First: visual. Pull the fuse out and look at the element through the transparent body. A good fuse has an intact, unbroken strip. A blown fuse has a gap — you can see where the element melted. Second: multimeter. Set to continuity. Touch the probes to the two exposed test points on top of the blade fuse — you don't even need to remove it. Beep means good. No beep means blown. The multimeter method is faster and catches fuses that look good visually but have hairline fractures.
>
> Now, finding the right fuse. Every fuse box has a cover diagram — either printed on the cover or in the owner's manual. It shows the position number, amperage, and the circuit it protects. 'F22 — 15A — LH Low Beam' tells you that fuse position 22, rated at 15 amps, protects the left-hand low beam headlight. Learn to read these diagrams — they save you hours of tracing wires."

**PPT Content:**
```
TESTING FUSES

METHOD 1: VISUAL INSPECTION
  Pull fuse → look at element through body
  Intact strip = GOOD
  Broken/melted strip = BLOWN

METHOD 2: MULTIMETER (preferred — faster & more reliable)
  Set to continuity (buzzer mode)
  Touch probes to test points on TOP of blade fuse
  Beep = GOOD    No beep = BLOWN

READING A FUSE BOX DIAGRAM
  Position number → Amperage → Circuit name
  Example: F22 — 15A — LH Low Beam

  Fuse box cover or owner's manual — ALWAYS your first reference
```

---

#### Slide 14: Fusible Links & Circuit Breakers
**Visual:** Photo of a fusible link wire section in a wiring harness, and a self-resetting circuit breaker used in a power window circuit

**Instructor Narration:**
> "Two more protection devices to know about. Fusible links are special sections of wire that are intentionally thinner than the rest of the harness. They're designed to burn through and break the circuit if there's a massive overcurrent — like a battery cable short. You find them near the battery and alternator. They protect circuits that are too high-current for even a maxi fuse. If a fusible link blows, you have to cut it out and solder or crimp in a new one — they're not plug-and-play like a blade fuse.
>
> Self-resetting circuit breakers are used in circuits that might see temporary overloads — like a power window stalling against an obstacle. Instead of blowing a fuse every time, the circuit breaker trips, cools down, and resets itself. You'll find these in window and seat motor circuits."

**PPT Content:**
```
OTHER PROTECTION DEVICES

FUSIBLE LINKS
  What: Thin wire section designed to burn through
  Where: Near battery, alternator — high-current circuits
  Rating: By wire gauge (thinner = lower current rating)
  Replacement: Cut out and splice — not plug-and-play

SELF-RESETTING CIRCUIT BREAKERS
  What: Thermal switch that trips on overload, resets when cool
  Where: Power window, seat motor, roof motor circuits
  Advantage: No fuse replacement needed for temporary overload
  Note: If it keeps tripping — there IS a fault, investigate

Both are SUPPLEMENTS to fuses, not replacements.
```

---

### **PRACTICAL PART 1: Relay Testing & Fuse Identification** (Slides 15-17, ~40 minutes)

**Narrative Voice:** Station-based, clear instructions. Set expectations for outcome.

---

#### Slide 15: Station Setup — Relay Testing
**Visual:** Photo of relay testing station — workbench with 5 different relays, multimeter, 12V bench power supply, relay socket, test lead kit, data sheet showing expected coil resistances

**Instructor Narration:**
> "Here's your first practical station. Each pair gets five relays — some good, some faulty. I've deliberately included one with a burnt coil, one with welded contacts, and one with corroded pins. Your job: test all five using the three-step method from Slide 7. For each relay, record coil resistance, contact state at rest, and contact state when energised. Mark each relay as GOOD, FAULTY — COIL, FAULTY — CONTACTS, or FAULTY — CORROSION. You have 20 minutes. Go."

**PPT Content:**
```
PRACTICAL STATION 1: RELAY TESTING

Equipment per pair:
• 5 relays (mix of good and faulty)
• Digital multimeter
• 12V bench power supply
• Test leads with clips
• Recording sheet

TEST EACH RELAY:
1. Coil resistance (pins 85/86) → Record value
2. Contact state at rest (pins 30/87) → OL expected
3. Apply 12V to coil → Listen for click
4. Contact state energised (pins 30/87) → Near 0 Ω expected

VERDICT: GOOD / FAULTY-COIL / FAULTY-CONTACTS / FAULTY-CORROSION

Time: 20 minutes
```

---

#### Slide 16: Station Setup — Fuse Identification & Testing
**Visual:** Photo of fuse identification station — collection of 15-20 fuses (all four types, various ratings), a vehicle fuse box (removed from a donor car or training unit), fuse box cover diagram, multimeter

**Instructor Narration:**
> "Station two. You have a collection of fuses — all four types, various ratings. First exercise: sort them by type and rating. Call out the colour code and rating for each one. Second exercise: I've put three blown fuses in the mix. Find them using visual inspection AND the multimeter method. Third exercise: here's a fuse box from a donor vehicle, complete with its cover diagram. I'll call out a circuit — 'left dipped headlight' — and you find the correct fuse, pull it, test it, and tell me the rating. You have 20 minutes."

**PPT Content:**
```
PRACTICAL STATION 2: FUSE IDENTIFICATION & TESTING

EXERCISE A — Sort & Identify (5 min)
  Sort all fuses by TYPE (mini, standard, maxi, cartridge)
  For each fuse: state COLOUR and AMPERAGE RATING

EXERCISE B — Find the Blown Fuses (5 min)
  3 blown fuses hidden in the collection
  Method 1: Visual inspection
  Method 2: Multimeter continuity
  Record: which fuses are blown and how you identified them

EXERCISE C — Fuse Box Navigation (10 min)
  Instructor calls a circuit name
  → Find correct fuse position using cover diagram
  → Pull the fuse
  → Test it
  → State the rating

Time: 20 minutes
```

---

#### Slide 17: Practical 1 Debrief
**Visual:** Checklist format — key findings to confirm before moving on

**Instructor Narration:**
> "Let's debrief. How many pairs found all faulty relays? Good. The welded-contact relay is the dangerous one — if that's a fuel pump relay, the pump runs continuously. The burnt coil is straightforward — no click, no function. The corroded one is the sneaky one — it might work on the bench but fail in the car under vibration.
>
> Fuses: who found all three blown ones? The visual method works for obvious failures, but the multimeter catches the hairline breaks. Always use both. Now, who got the fuse box navigation exercise right on the first try? The cover diagram is your map. Learn to read it fast."

**PPT Content:**
```
PRACTICAL 1 DEBRIEF

RELAY TESTING — confirm:
✓ Normal coil resistance: 50-120 Ω
✓ Open coil: reads OL → relay is dead
✓ Welded contacts: reads 0 Ω at rest → DANGEROUS failure
✓ Corrosion: intermittent or high resistance → check socket too

FUSE TESTING — confirm:
✓ Visual: look for broken element through body
✓ Multimeter: continuity across test points (faster, catches hairlines)
✓ Fuse box diagram: position → rating → circuit name

KEY LESSON: Always test — never assume.
```

---

### **DEVELOPMENT PART 3: Soldering & Crimping Demonstration** (Slides 18-21, ~10 minutes)

**Narrative Voice:** Master craftsman demonstrating technique. Slow, deliberate, narrated.

---

#### Slide 18: Soldering Equipment & Setup
**Visual:** Labelled photo of soldering station — iron (25-60W), lead-free solder (60/40 or SAC305), flux pen, wet sponge / brass tip cleaner, heat shrink tubing (assorted sizes), heat gun, wire strippers, helping hands / vise

**Instructor Narration:**
> "Soldering. This is how you make a permanent, low-resistance electrical connection between two wires. Your equipment: a soldering iron — 25 to 60 watts for automotive wire work. Lead-free solder — environmental regulations prohibit lead solder in most applications now. A flux pen or flux-core solder — flux cleans the metal surfaces so solder can flow and bond. A wet sponge or brass cleaner for the iron tip. Wire strippers. And critically — heat shrink tubing. You slide this onto the wire BEFORE you solder, because you can't put it on after the joint is made. I've seen experienced technicians forget this and have to redo the entire joint."

**PPT Content:**
```
SOLDERING EQUIPMENT

Iron: 25-60W pencil type (temperature-controlled preferred)
Solder: Lead-free (SAC305 or 60/40 tin-lead where permitted)
Flux: Flux-core solder or separate flux pen
Tip cleaner: Wet sponge or brass wire ball
Wire strippers: Matched to wire gauge
Heat shrink tubing: Slide on BEFORE soldering!
Heat gun: For shrinking the tubing after
Helping hands / vise: Holds work steady

REMEMBER: Heat shrink goes on BEFORE the joint.
Write it on your hand if you have to.
```

---

#### Slide 19: Soldering Technique — Step by Step
**Visual:** Five sequential close-up photos — (1) Wires stripped and twisted together, (2) Iron tinned with fresh solder, (3) Iron touching joint from below, solder touching from above, solder flowing into joint, (4) Completed shiny joint, (5) Heat shrink slid over and heated

**Instructor Narration:**
> "Watch carefully — I'll do this once, then you'll do it fifty times. Step one: strip about 10mm of insulation from each wire. Twist the bare copper strands tightly. Hook the two wires together — twist or lap, depending on the joint type. Step two: tin your iron. Touch fresh solder to the hot tip until it has a thin coating — this improves heat transfer.
>
> Step three — this is the critical part. Place the iron TIP against the wire joint from one side. Hold it there for two seconds to heat the copper. Now touch the solder to the WIRE, not the iron. The wire should be hot enough to melt the solder itself. If the wire is hot enough, the solder will flow INTO the joint like water — we call this capillary action. You should see the solder wick through the twisted strands. Hold for one more second, then remove the iron.
>
> Step four: let it cool naturally. Don't blow on it, don't move it. A good joint is shiny and smooth. A bad joint — a cold joint — looks dull, grainy, or blobby. That means the copper wasn't hot enough and the solder didn't bond properly. If you get a cold joint, reheat it and add a touch more solder.
>
> Step five: slide the heat shrink over the joint, centre it, and hit it with the heat gun. The tubing shrinks down tight, waterproofing and insulating the joint. Done."

**PPT Content:**
```
SOLDERING TECHNIQUE — 5 STEPS

1. STRIP & TWIST
   Strip 10 mm insulation → twist strands tight
   Hook or lap wires together

2. TIN THE IRON
   Touch solder to hot tip → thin shiny coating
   Improves heat transfer to the joint

3. HEAT THE JOINT, NOT THE SOLDER
   Iron tip → touch WIRE → hold 2 seconds → heat the copper
   Touch solder to WIRE (opposite side from iron)
   Solder flows INTO joint by capillary action

4. COOL & INSPECT
   Remove iron → let cool naturally (don't blow)
   GOOD joint: shiny, smooth, solder wicked through
   COLD joint: dull, grainy, blobby → REDO

5. HEAT SHRINK
   Slide tubing over joint → heat gun → sealed & insulated

GOLDEN RULE: Heat the joint, not the solder.
```

---

#### Slide 20: Crimping Technique — Step by Step
**Visual:** Sequential photos — (1) Terminal types: ring, spade, pin. (2) Wire stripped to correct length (matching terminal barrel). (3) Wire inserted into terminal barrel. (4) Ratchet crimper closing on terminal. (5) Completed crimp with tug test being performed.

**Instructor Narration:**
> "Crimping is the other method. It's faster than soldering, and many manufacturers actually prefer it because a crimped connection maintains some flexibility — important in a vibrating vehicle. There are three terminal types you'll crimp: ring terminals — they bolt onto a stud. Spade terminals — they push onto a blade connector. And pin terminals — they fit into multi-pin connectors for connector repair.
>
> The technique: strip the wire to the exact length of the terminal barrel — too long and bare copper sticks out, too short and the crimp doesn't grip the conductor. Insert the wire into the barrel so the insulation just reaches the insulation grip area. Place it in the correct die of your crimper. If you're using a ratchet crimper — and you should — squeeze the handle until it releases. The ratchet won't release until the crimp is fully formed. No half-crimps.
>
> After crimping, do a pull test. Grab the wire in one hand, the terminal in the other, and pull firmly. If it comes apart, your strip length was wrong or you used the wrong die size. A good crimp will hold your entire body weight if done right — though we won't test that today."

**PPT Content:**
```
CRIMPING TECHNIQUE

TERMINAL TYPES:
  Ring terminal — bolts to a stud (ground connections, battery)
  Spade terminal — pushes onto blade (quick connect/disconnect)
  Pin terminal — inserts into connector body (connector repair)

STEPS:
1. Select terminal matched to wire gauge (colour-coded)
   Red = 22-18 AWG   Blue = 16-14 AWG   Yellow = 12-10 AWG

2. Strip wire to barrel length (not too long, not too short)

3. Insert wire — insulation reaches insulation grip area

4. Crimp with RATCHET crimper (ratchet ensures full compression)
   Use correct die size for terminal

5. PULL TEST — firm tug, terminal must NOT pull off

TOOL: Ratchet crimper preferred over basic pliers crimper.
Ratchet guarantees consistent, complete crimps.
```

---

#### Slide 21: Solder vs Crimp — When to Use Which
**Visual:** Comparison table with automotive context photos — soldered repair in engine bay, crimped terminals in door wiring

**Instructor Narration:**
> "So when do you solder and when do you crimp? Here's the practical answer. Solder when you need a permanent, low-resistance joint — especially for wire-to-wire splices in tight spaces where there's no connector. Crimp when you need a terminal that connects to something — a stud, a blade, or a connector pin. Also crimp when the manufacturer specifies it, or when the repair needs to be easily reversible.
>
> In vibration-heavy areas — like the engine bay or near the suspension — some manufacturers prefer crimping because a crimped connection has more mechanical flexibility than a soldered one. A soldered joint is rigid and can crack from repeated vibration. Add heat shrink to either method for waterproofing.
>
> Here's a rule of thumb: if you're repairing a factory connector, crimp a new pin terminal. If you're splicing two wires together mid-harness, solder and heat shrink. If the manufacturer's repair manual specifies a method, follow it. When in doubt, crimp with heat shrink."

**PPT Content:**
```
SOLDER vs CRIMP — DECISION GUIDE

USE SOLDER WHEN:
  • Wire-to-wire splice (no terminal needed)
  • Permanent, low-resistance joint required
  • Tight space with no room for a terminal
  • Repair manual specifies solder

USE CRIMP WHEN:
  • Connecting to a stud, blade, or connector
  • High-vibration area (engine bay, chassis)
  • Manufacturer specifies crimped repair
  • Repair needs to be reversible
  • Connector pin replacement

BOTH METHODS:
  • Always add heat shrink for insulation/waterproofing
  • Always perform pull test / continuity test after

WHEN IN DOUBT → CRIMP WITH HEAT SHRINK
```

---

### **PRACTICAL PART 2: Wiring Craft Stations** (Slides 22-24, ~70 minutes)

**Narrative Voice:** Workshop supervisor. Clear pass criteria. Emphasis on repetition.

---

#### Slide 22: Station A — Soldering Practice
**Visual:** Photo of soldering station with materials laid out — 10 pre-cut wire pairs, solder, iron, heat shrink, magnifying lamp. Inset: close-up of a good joint vs a cold joint for reference.

**Instructor Narration:**
> "Station A: Soldering. Each of you will solder five wire-to-wire joints. Here's the standard: the solder must wick through the twisted strands — I should not see a blob sitting on top of the wire. The joint must be shiny, not dull. The heat shrink must cover the entire exposed area with no bare copper visible. When you finish each joint, bring it to me. I'll inspect it and either pass it or tell you to redo it. Five good joints and you move on.
>
> Remember — heat shrink goes on BEFORE you solder. I guarantee at least two of you will forget. That's fine — do it again. Repetition builds habit."

**PPT Content:**
```
STATION A: SOLDERING PRACTICE

TASK: Produce 5 soldered wire-to-wire joints

REQUIREMENTS FOR EACH JOINT:
□ Wire stripped to 10 mm
□ Strands twisted tight
□ Wires hooked/lapped securely
□ Solder wicked THROUGH the strands (not blobbed on top)
□ Joint is SHINY and smooth (not cold/grainy)
□ Heat shrink covers ALL exposed copper
□ Heat shrink fully shrunk (no loose tubing)

PASS CRITERIA: Instructor inspection of each joint
FAIL: Cold joint, exposed copper, forgotten heat shrink → REDO

Time: 25 minutes (5 joints)
Target: 5 out of 5 passed
```

---

#### Slide 23: Station B — Crimping Practice
**Visual:** Photo of crimping station — wire stock (3 gauges), selection of ring/spade/pin terminals, ratchet crimper, wire strippers, pull-test jig or just firm hand-pull method

**Instructor Narration:**
> "Station B: Crimping. You'll crimp ten terminals: three ring terminals, three spade terminals, and four pin terminals. Pin terminals are the most finicky — they go into multi-pin connectors, and if the crimp isn't right, the pin won't lock into the connector housing properly.
>
> For each crimp: strip the wire to the exact barrel length. Insert it so the insulation reaches the insulation grip. Crimp with the ratchet tool. Then pull test — grab and yank. If it comes off, you stripped too short or used the wrong die. After the pull test, do a continuity check with the multimeter. A good crimp reads less than 0.1 ohms. If it reads higher, the crimp is loose and it'll cause a voltage drop in service."

**PPT Content:**
```
STATION B: CRIMPING PRACTICE

TASK: Crimp 10 terminals

3x Ring terminals (assorted sizes)
3x Spade terminals (male and female)
4x Pin terminals (for connector repair)

REQUIREMENTS FOR EACH CRIMP:
□ Wire strip length matches barrel length exactly
□ Insulation sits in insulation grip area
□ Crimped with ratchet tool (full ratchet cycle)
□ Pull test passed — terminal does NOT pull off
□ Continuity check — < 0.1 Ω through crimp

PASS CRITERIA: All 10 crimps pass pull test + continuity
FAIL: Terminal pulls off, wrong strip length, wrong die → REDO

Time: 25 minutes (10 crimps)
```

---

#### Slide 24: Station C — Simulated Wiring Fault Repair
**Visual:** Photo of the fault repair station — a wiring loom section mounted on a board with a deliberate cut wire, plus tools (strippers, solder OR crimp equipment, heat shrink, multimeter). Before/after photos of a proper repair.

**Instructor Narration:**
> "Station C: the real test. I've prepared wiring loom sections with a simulated fault — a cut wire. Your task: identify which wire is cut using the multimeter, strip the cut ends, repair the break using either solder or crimp — your choice, justified — and insulate with heat shrink. When you're done, test continuity end-to-end. The circuit must read less than 0.5 ohms across the full length including your repair.
>
> This is what you'll do on real cars. A rodent chews through a wire. A previous repair fails. An accident damages the harness. You locate the break, you fix it, you test it. This is the job. You have 20 minutes."

**PPT Content:**
```
STATION C: SIMULATED WIRING FAULT REPAIR

SCENARIO: Wiring loom section with ONE cut wire

YOUR TASK:
1. IDENTIFY the cut wire using multimeter continuity
2. LOCATE the break point
3. STRIP both cut ends (10 mm)
4. REPAIR using solder OR crimp (your choice — justify it)
5. INSULATE with heat shrink tubing
6. TEST end-to-end continuity: must read < 0.5 Ω

ASSESSMENT:
□ Correct wire identified
□ Clean strip, no nicked strands
□ Solid joint (solder or crimp — inspected)
□ Heat shrink fully sealed
□ End-to-end continuity confirmed
□ Can explain WHY you chose solder or crimp

Time: 20 minutes
```

---

### **WRAP-UP: Quality Check & Preview** (Slides 25-27, ~15 minutes)

---

#### Slide 25: Quality Inspection — Show Your Work
**Visual:** Checklist layout — each learner's work products listed with pass/fail boxes

**Instructor Narration:**
> "Tools down. Let's check your work. Lay out your five soldered joints, your ten crimped terminals, and your repaired wiring section on the bench. I'm going to walk around and do a final quality inspection. For the solder joints, I'm looking for shine, full penetration, and sealed heat shrink. For crimps, I'm doing a pull test and checking your strip lengths. For the repair, I'm testing continuity.
>
> If any of your work doesn't pass, I'll mark it. You'll have time at the start of Day 9 to redo any failed items before we move on. There's no shame in redoing work — that's how you learn craft."

**PPT Content:**
```
QUALITY INSPECTION

LAY OUT YOUR WORK:
□ 5 soldered joints — inspected for quality
□ 10 crimped terminals — pull tested
□ 1 wiring repair — continuity tested

SOLDER INSPECTION CRITERIA:
  Shiny, smooth, wicked through, heat shrink sealed

CRIMP INSPECTION CRITERIA:
  Correct strip length, full ratchet crimp, passes pull test

REPAIR INSPECTION CRITERIA:
  Correct wire identified, solid joint, < 0.5 Ω end-to-end

Any failed items → redo at start of Day 9
```

---

#### Slide 26: What You Learned Today
**Visual:** Summary with six skill icons

**Instructor Narration:**
> "Let's recap. Today you learned how a relay works and how to test one in three steps — coil, contacts at rest, contacts energised. You learned fuse types, colour codes, and how to test fuses and navigate a fuse box diagram. You learned to solder a wire joint — heat the work, not the solder, and never forget the heat shrink. You learned to crimp terminals — strip to the barrel length, use the ratchet tool, pull test every time. And you made a real wiring repair.
>
> These are core technician skills. You'll use them every week for the rest of your career. Tomorrow we go deeper into the multimeter — it's your most important tool, and Day 9 is about mastering it."

**PPT Content:**
```
DAY 8 RECAP — YOU CAN NOW:

✓ Explain relay construction and operation
✓ Test a relay with a multimeter (3-step method)
✓ Identify all fuse types and read colour codes
✓ Test a fuse visually and with a multimeter
✓ Read and navigate a fuse box diagram
✓ Solder a wire-to-wire joint with heat shrink
✓ Crimp ring, spade, and pin terminals
✓ Repair a wiring fault and verify with continuity test
✓ Decide when to solder vs when to crimp

SKILLS BUILT TODAY WILL BE USED EVERY DAY OF YOUR CAREER.
```

---

#### Slide 27: Day 9 Preview — Multimeter Mastery
**Visual:** Photo of a digital multimeter with all its modes highlighted — DC voltage, AC voltage, resistance, continuity, diode test, frequency, duty cycle, min/max

**Instructor Narration:**
> "Tomorrow is Day 9: Multimeter Mastery. You've been using the multimeter for resistance and continuity. Tomorrow you'll learn ALL of its functions — DC and AC voltage measurement, current measurement with a clamp meter, diode testing, and live circuit testing techniques. We'll also cover proper test lead connection, auto-ranging vs manual ranging, and how to avoid damaging the meter or the circuit. Bring your curiosity and your steady hands. See you tomorrow."

**PPT Content:**
```
DAY 9 PREVIEW: MULTIMETER MASTERY

Tomorrow you master your most important tool:
• DC Voltage measurement (battery, sensors, ECU feeds)
• AC Voltage measurement (alternator output, wheel speed sensors)
• Current measurement (parasitic draw, circuit load)
• Resistance — deeper (component testing, wire integrity)
• Diode testing (alternator diodes, protection diodes)
• Continuity — advanced (harness tracing, ground path testing)
• MIN/MAX hold for capturing intermittent faults

The multimeter is a technician's eyes.
Tomorrow, we sharpen your vision.
```

---

## Assessment Checkpoint

**Formative (not graded, but work quality is inspected):**

| Assessment Item | Method | Pass Standard |
|----------------|--------|---------------|
| Relay testing (5 relays) | Practical — recorded results | All 5 correctly diagnosed (GOOD / fault type) |
| Fuse identification | Practical — sort and name | All types and ratings correctly identified |
| Fuse box navigation | Practical — instructor calls circuits | Correct fuse located and tested within 60 seconds |
| Solder joints (5) | Practical — instructor inspection | Shiny, wicked-through, heat shrink sealed |
| Crimp terminals (10) | Practical — pull test + continuity | All 10 pass pull test, < 0.1 ohms |
| Wiring fault repair (1) | Practical — end-to-end test | Correct wire, solid repair, < 0.5 ohms, method justified |

**Remediation:** Any failed items can be redone at the start of Day 9 (first 10 minutes allocated as buffer).

---

## Key Takeaways

1. **Relays** are electrically operated switches — small current controls large current. Test with coil resistance, contact continuity, and 12V activation.
2. **Fuses** are sacrificial protection devices. Never uprate a fuse. Test visually AND with a multimeter. Learn to read the fuse box diagram.
3. **Soldering** requires heating the WORK, not the solder. Solder should flow into the joint by capillary action. Always add heat shrink BEFORE soldering.
4. **Crimping** requires correct strip length, correct terminal-to-wire gauge match, and a ratchet crimper. Every crimp gets a pull test.
5. **Solder vs crimp** depends on context: solder for permanent mid-harness splices, crimp for terminal connections and high-vibration areas. Follow manufacturer guidance.
6. A bad connection is worse than no connection — it causes intermittent faults, voltage drops, overheating, and fire risk. **Do it right or do it again.**

---

## Preparation for Day 9

**Instructor prep:**
- Set up multimeter training stations (one meter per learner if possible)
- Prepare live circuits on training boards: battery + resistors + LEDs for voltage measurement practice
- Prepare a vehicle or training unit with accessible test points (battery, alternator output, sensor feeds, ground points)
- Have a clamp-on current meter available for demonstration
- Print multimeter function quick-reference cards
- Prepare an intentional fault circuit (e.g., high-resistance ground) for diagnostic exercise

**Learner prep:**
- Review Ohm's Law from Day 7 (V = I x R)
- Bring any failed solder/crimp items for redo in the first 10 minutes
- Review multimeter dial positions from Day 7 notes

---

## Materials & Equipment List — Day 8

### Per Learner Pair (Relay/Fuse Stations):
- 5 assorted relays (include at least 1 with burnt coil, 1 with welded contacts, 1 with corroded pins)
- Digital multimeter with test leads
- 12V bench power supply (or a car battery with safety terminals)
- Relay socket wired to banana jacks
- 15-20 assorted fuses (all four types, include 3 intentionally blown)
- Vehicle fuse box assembly (donor unit or training board)
- Fuse box cover diagram (printed A4)
- Recording sheets

### Per Learner (Soldering Station):
- Soldering iron (25-60W, temperature-controlled preferred)
- Soldering iron stand with sponge or brass cleaner
- Lead-free solder (1mm diameter)
- Flux pen
- 10 pre-cut wire pairs (16-18 AWG, 150mm lengths, assorted colours)
- Heat shrink tubing assortment (3mm, 5mm, 8mm diameters)
- Heat gun (shared — 1 per 4 learners)
- Wire strippers
- Safety glasses (mandatory during soldering)
- Helping hands or small vise

### Per Learner (Crimping Station):
- Ratchet crimper tool
- Ring terminals — 3 sizes (matched to wire gauge)
- Spade terminals — male and female
- Pin terminals — for connector repair
- Wire stock — 3 gauges (18, 16, 14 AWG)
- Wire strippers
- Multimeter for continuity check

### Per Learner (Repair Station):
- Pre-prepared wiring loom section with one cut wire
- Full tool access (strippers, solder OR crimp kit, heat shrink, heat gun)
- Multimeter
- Inspection magnifier (optional)

### Instructor:
- Demonstration soldering station with overhead camera / magnifying display
- Sample good joints and bad joints (mounted on display board)
- Sample good crimps and bad crimps (mounted on display board)
- Printed quality inspection checklists
- Spare relays, fuses, wire, terminals for replacements
