---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 2
week_title: "Speaking Electricity"
day_number: 10
session_title: "Starting & Charging Introduction + Week 2 Consolidation"
duration_minutes: 180
theory_practice: "35:65"
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 10: Starting & Charging Introduction + Week 2 Consolidation
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (63 min theory + 117 min practical/consolidation)
**Approach:** Applied Systems Thinking — Connect the Electrical Foundation to Real Vehicle Systems
**PPT Target:** 27 slides
**Week:** 2 of 8 — "Speaking Electricity" (Week Finale)

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Name the major components of a starter motor and describe the cranking circuit path from ignition switch to ring gear engagement
- Name the major components of an alternator and explain how it converts mechanical rotation to regulated DC voltage
- Perform a basic starting and charging test sequence (resting voltage, starter current draw, alternator output voltage)
- Connect an OBD-II scan tool to a live vehicle, read and clear DTCs, and navigate live data PIDs
- Summarize the complete Week 2 electrical knowledge arc: voltage, current, Ohm's Law, circuits, faults, components, CAN bus, diagnostics
- Score at least 7/10 on the Week 2 formative MCQ quiz

**This is the final session of Week 2.** Learners have spent four days building an electrical vocabulary. Day 10 applies that vocabulary to two systems they will encounter on every single vehicle, gives them their first real OBD-II scan tool experience, and consolidates the entire week before the shift to engine systems in Week 3.

---

## Connection to Prior Knowledge

Build from the complete Week 2 arc:
- **Day 6:** Voltage, current, resistance, Ohm's Law — the language
- **Day 7:** Series and parallel circuits, reading schematics — the grammar
- **Day 8:** Faults (open, short, high resistance), relays, fuses — the failure modes
- **Day 9:** ECUs, sensors, actuators, CAN bus, DTC codes — the communication network

**Bridge:** "You spent four days learning the language of electricity. Today you use that language for real. The starter motor and alternator are systems you will test on almost every vehicle that rolls into your bay. And for the first time, you'll plug a scan tool into a live car and talk to its brain."

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: Two Systems Every Technician Tests** (Slides 1-3, ~10 minutes)

**Narrative Voice:** Energetic, connecting. This is the week finale — learners should feel how far they have come.

---

#### Slide 1: Title & Day 10 Context
**Visual:** Split image — left side shows a starter motor engaging a flywheel ring gear with sparks of energy, right side shows an alternator with glowing output wires feeding into a battery. Banner reads "Week 2 Finale."

**Instructor Narration:**
> "Day 10. The last day of Week 2. Four days ago, you didn't know what a volt was. Today you're going to test a real starter motor, measure a real alternator's output, and plug a scan tool into a live vehicle for the first time. Two systems that every technician tests on every vehicle — starting and charging. Plus your first real OBD-II session. Let's finish this week strong."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 2: Speaking Electricity — DAY 10 (Week 2 Finale)

Starting & Charging Introduction
+ Week 2 Consolidation

Two systems you'll test on EVERY vehicle.
Your first real OBD-II scan tool session.
```

---

#### Slide 2: Where Day 10 Fits
**Visual:** Week 2 timeline with Days 6-9 shown as completed stepping stones and Day 10 as the capstone. Arrows show how each day feeds into today.

**Instructor Narration:**
> "Here's where today fits. Day 6 gave you the language — volts, amps, ohms. Day 7 taught you circuits — series, parallel, how current flows. Day 8 showed you what goes wrong — opens, shorts, high resistance, and the components that protect against them. Day 9 connected it all — ECUs reading sensors, commanding actuators, talking on CAN bus, setting fault codes.
>
> Today, we apply ALL of that to two real systems. The starter motor uses battery current through a relay, through a solenoid, to spin an electric motor — that's Day 6 through Day 8 in one circuit. The alternator charges the battery and is monitored by the ECU — that's Day 9. And when we plug in the scan tool, you're reading the codes those ECUs store. Everything connects."

**PPT Content:**
```
WEEK 2 — YOUR ELECTRICAL JOURNEY

Day 6:  Voltage, Current, Resistance — The Language
Day 7:  Circuits — Series, Parallel, Schematics
Day 8:  Faults, Relays, Fuses — What Goes Wrong
Day 9:  ECUs, Sensors, CAN Bus, DTCs — The Network

Day 10: APPLY IT ALL — Starting, Charging, OBD-II
        + Week 2 Consolidation & Quiz

Everything you learned this week comes together TODAY.
```

---

#### Slide 3: Today's Plan
**Visual:** Horizontal timeline divided into six colour-coded blocks with durations

**Instructor Narration:**
> "Here's the plan. Thirty minutes on starter and alternator theory — construction, operation, common faults. Fifteen minutes on the test sequence — what measurements tell you what. Then we go to the workshop for fifty minutes: find the starter and alternator on a real vehicle, then run the battery-starter-alternator test sequence with real meters. After that, thirty minutes of OBD-II hands-on — scan tool, live data, DTCs. Then we come back for a thirty-minute Week 2 review and quiz. Fifteen minutes to wrap up and preview Week 3. Let's go."

**PPT Content:**
```
TODAY'S PLAN (180 minutes)

THEORY 1 (30 min): Starter Motor & Alternator — How They Work
THEORY 2 (15 min): The Test Sequence — Battery > Starter > Alternator
PRACTICAL 1 (50 min): Identify & Test on a Real Vehicle
PRACTICAL 2 (30 min): OBD-II Scan Tool — DTCs & Live Data
REVIEW & QUIZ (30 min): Week 2 Consolidation — 10-Question MCQ
WRAP-UP (15 min): Week 2 Celebration + Week 3 Preview
```

---

### **DEVELOPMENT PART 1: Starter Motor & Alternator** (Slides 4-11, ~30 minutes)

**Narrative Voice:** Systematic, building from structure to operation to failure. Use the electrical language from Days 6-8 deliberately.

---

#### Slide 4: The Starter Motor — What It Is
**Visual:** Cutaway photograph of a starter motor with every major component labeled: armature (rotor), field coils or permanent magnets, solenoid with plunger, Bendix drive (overrunning clutch), pinion gear. Adjacent: a flywheel ring gear.

**Instructor Narration:**
> "The starter motor has one job: spin the engine fast enough for it to start on its own. A petrol engine needs about 200-300 RPM to fire. A diesel needs more — maybe 150-250 RPM but with much higher compression to overcome. The starter does this in two to four seconds, drawing 150 to 300 amps from the battery.
>
> Let's look inside. The armature is the spinning part — heavy copper windings on a steel core. Surrounding it are either field coils — electromagnets — or permanent magnets. When current flows through the armature, the magnetic interaction creates rotation. On top sits the solenoid — that's a big relay. It does two things: it pushes the Bendix drive forward to engage the pinion gear with the flywheel ring gear, and it closes the heavy contacts to send full battery current to the motor. The Bendix drive has an overrunning clutch — once the engine starts and spins faster than the starter, the clutch disengages to protect the motor."

**PPT Content:**
```
THE STARTER MOTOR — CONSTRUCTION

Job: Spin the engine crankshaft fast enough to start combustion
Current draw: 150-300 A (petrol), up to 500 A (diesel)
Cranking speed: 200-300 RPM

MAJOR COMPONENTS:
1. Armature (rotor) — heavy copper windings, spins
2. Field coils OR permanent magnets — create magnetic field
3. Solenoid — relay + mechanical plunger (dual function)
4. Bendix drive — overrunning clutch + pinion gear
5. Ring gear — bolted to flywheel/flexplate (engine side)

The solenoid does TWO jobs:
  • Pushes pinion into ring gear (mechanical)
  • Closes contacts to send 150-300 A to motor (electrical)
```

---

#### Slide 5: What Happens When You Turn the Key
**Visual:** Sequential circuit diagram showing the cranking circuit path: ignition switch position START, through neutral safety switch (automatic) or clutch switch (manual), to starter relay, to solenoid, to motor, to ground. Numbered steps 1-6 with current flow arrows.

**Instructor Narration:**
> "Let's trace the circuit — use the language from Day 6 and Day 8. You turn the key to START. A small current — maybe 0.5 amps — flows from the ignition switch through the neutral safety switch. This is a safety interlock: on an automatic, the car must be in Park or Neutral. On a manual, the clutch pedal must be pressed. If that switch is open, nothing happens — this is an open circuit fault we learned about on Day 8.
>
> That small current energises the starter relay — remember relays from Day 8? A small current controls a large current. The relay closes and sends about 10 amps to the solenoid. The solenoid does its two jobs: the plunger pushes the Bendix into the ring gear, and the heavy contacts close. Now full battery current — 200 amps or more — flows through the motor. The armature spins, the pinion spins the ring gear, the crankshaft turns, and the engine cranks. All of this happens in under half a second."

**PPT Content:**
```
THE CRANKING CIRCUIT — Step by Step

1. Key to START → small current (~0.5 A) flows
2. Through NEUTRAL SAFETY SWITCH (auto) or CLUTCH SWITCH (manual)
   — Safety interlock: prevents starting in gear
3. Current energises STARTER RELAY
   — Small current controls large current (Day 8!)
4. Relay sends ~10 A to SOLENOID
5. Solenoid:
   a) Pushes BENDIX/PINION into RING GEAR (mechanical)
   b) Closes HEAVY CONTACTS (electrical)
6. Full battery current (150-300 A) flows through MOTOR
   → Armature spins → Pinion spins ring gear → Engine cranks

Total time from key turn to cranking: < 0.5 seconds
```

---

#### Slide 6: Starter Motor — Common Failures
**Visual:** Three-column diagnostic table: Symptom | Likely Cause | What's Happening Electrically. Icons for each: slow clock for slow crank, single click icon, grinding gear icon.

**Instructor Narration:**
> "Three symptoms you'll see over and over. First: slow crank. The engine turns, but sluggishly. The sound is low-pitched and strained. Cause? Usually a weak battery — not enough voltage under load. Could also be high-resistance connections — corroded battery terminals, bad ground cable. Remember Day 8: high resistance means voltage drop, less current to the motor.
>
> Second: click, no crank. You hear a single loud click from the solenoid, but the engine doesn't turn. That click means the solenoid is trying — it has enough current to engage. But the heavy contacts may be burnt, or the motor itself has failed. Could also be a seized engine — the starter can't turn it.
>
> Third: grinding noise. The pinion is trying to engage the ring gear but the teeth aren't meshing properly. Worn ring gear teeth, worn pinion, or the Bendix isn't extending fully. That grinding sound is metal chewing metal — and it's expensive if you ignore it."

**PPT Content:**
```
STARTER MOTOR — COMMON FAILURES

SYMPTOM 1: SLOW CRANK (engine turns slowly)
  Causes: Weak battery, corroded terminals, bad ground
  Electrical: High resistance → voltage drop → less current

SYMPTOM 2: CLICK — NO CRANK (single click, engine silent)
  Causes: Burnt solenoid contacts, dead motor, seized engine
  Electrical: Solenoid energises but cannot pass current

SYMPTOM 3: GRINDING NOISE (metallic clash)
  Causes: Worn ring gear teeth, worn pinion, weak Bendix
  Mechanical: Pinion fails to mesh with ring gear

DIAGNOSTIC KEY:
  Slow crank → Check BATTERY and CONNECTIONS first
  Click no crank → Check SOLENOID and MOTOR
  Grinding → Check RING GEAR and BENDIX
```

---

#### Slide 7: The Alternator — What It Is
**Visual:** Cutaway photograph of a modern alternator with every major component labeled: rotor with field winding, stator with 3-phase windings, diode rectifier bridge (6 diodes), voltage regulator (IC), front bearing, rear bearing, pulley with overrunning alternator decoupler (OAD), slip rings and brushes.

**Instructor Narration:**
> "Once the engine starts, the starter's job is done. Now the alternator takes over. Its job: convert mechanical rotation into electrical energy to charge the battery and power every electrical load on the vehicle — lights, fuel pump, ignition system, ECUs, heated seats, everything.
>
> Inside, the rotor has a field winding — an electromagnet on the spinning shaft. Current reaches it through slip rings and brushes. The stator surrounds the rotor and has three sets of windings — this is a three-phase AC generator. As the rotor spins inside the stator, it induces alternating current in those three windings. But the car runs on DC. So six diodes — the rectifier bridge — convert that AC into DC. Finally, a voltage regulator controls the field current to keep output at about 14.0 to 14.8 volts regardless of engine speed or electrical load."

**PPT Content:**
```
THE ALTERNATOR — CONSTRUCTION

Job: Convert mechanical rotation to regulated DC voltage
     Charges battery + powers all electrical loads
Output: ~14.0 - 14.8 V DC (regulated)
Typical capacity: 80-200 A depending on vehicle

MAJOR COMPONENTS:
1. Rotor — field winding (electromagnet), spins with engine
2. Stator — 3-phase windings (stationary), AC is generated here
3. Slip rings + brushes — deliver current to spinning rotor
4. Diode rectifier bridge — 6 diodes convert AC → DC
5. Voltage regulator — controls field current → stable output
6. Pulley (often overrunning decoupler) — driven by serpentine belt
7. Bearings — front and rear, support rotor shaft
```

---

#### Slide 8: How the Alternator Works
**Visual:** Simplified diagram showing the energy conversion chain: Engine rotation (mechanical) -> Belt drives pulley -> Rotor spins inside stator -> 3-phase AC generated -> Diode bridge rectifies to DC -> Voltage regulator adjusts field current -> 14.2V output -> Battery and loads. Arrows show feedback loop from regulator monitoring output voltage.

**Instructor Narration:**
> "Follow the energy. The engine spins the alternator pulley through the serpentine belt. The rotor — the electromagnet — spins inside the stator windings. This induces three-phase AC voltage in the stator. The six diodes rectify it to pulsating DC. The voltage regulator monitors the output: if voltage drops below the target — say, you turn on the headlights and heated seats — the regulator increases field current to strengthen the rotor's magnetic field, which increases the output. If voltage climbs too high, the regulator reduces field current.
>
> This is a closed-loop control system — the same sensor-ECU-actuator pattern from Day 9. The voltage regulator is the controller, the output voltage is the feedback signal, and the field current is the actuator. The alternator is an ECU-controlled system, even though it has been around for decades."

**PPT Content:**
```
HOW THE ALTERNATOR WORKS

Energy conversion chain:
  Engine → Belt → Pulley → Rotor spins
  → 3-phase AC induced in Stator
  → Diode bridge rectifies AC → DC
  → Voltage regulator controls field current
  → Stable 14.0 - 14.8 V output

CLOSED-LOOP CONTROL (Day 9 pattern!):
  Sensor:    Output voltage monitoring
  Controller: Voltage regulator
  Actuator:  Field current (rotor electromagnet strength)

  Output LOW? → Increase field current → More voltage
  Output HIGH? → Decrease field current → Less voltage

Result: Stable voltage regardless of engine RPM or load
```

---

#### Slide 9: Alternator — Common Failures
**Visual:** Four-quadrant layout, each with symptom name, gauge/indicator visual, and electrical explanation. Quadrants: Undercharge, Overcharge, Bearing Noise, Whine/Ripple.

**Instructor Narration:**
> "Four things go wrong with alternators. Undercharge: the battery warning light comes on, the battery slowly goes flat, accessories dim at idle. Usually worn brushes — they lose contact with the slip rings, so no field current, no output. Or a broken belt — no spin, no generation.
>
> Overcharge: battery boils, headlights are excessively bright, you smell acid. The voltage regulator has failed in the 'full-on' position — maximum field current all the time, output climbs above 15 volts. This destroys the battery and can damage ECUs.
>
> Bearing noise: a growling or rumbling that changes with engine RPM. Worn front or rear bearing. If you ignore it, the rotor eventually seizes and snaps the belt.
>
> Whine: a high-pitched electrical whine through the speakers that rises with RPM. Usually a failing diode in the rectifier bridge. The diode lets AC ripple through instead of clean DC. We can measure this with an AC voltage test on the battery — more than about 0.5V AC ripple means a bad diode."

**PPT Content:**
```
ALTERNATOR — COMMON FAILURES

UNDERCHARGE (battery light on, battery goes flat)
  Causes: Worn brushes, broken/slipping belt, open field circuit
  Result: Little or no output voltage

OVERCHARGE (headlights too bright, battery boils, acid smell)
  Causes: Failed voltage regulator (stuck full-on)
  Result: Output > 15V → damages battery and electronics

BEARING NOISE (growl/rumble, varies with RPM)
  Causes: Worn front or rear bearing
  Risk: Bearing seizes → belt snaps → total loss of charging

WHINE / RIPPLE (electrical whine through speakers)
  Causes: Failed diode in rectifier bridge
  Test: AC voltage on battery terminals > 0.5V AC = bad diode
```

---

#### Slide 10: Starter & Alternator — Side by Side
**Visual:** Comparison table — two columns (Starter vs. Alternator) with rows for: Job, When Active, Energy Direction, Current Level, Key Internal Part, Most Common Failure, Primary Test

**Instructor Narration:**
> "Let's put them side by side. The starter and alternator are both electrical machines — windings, magnets, rotation. But they do opposite things. The starter converts electrical energy into mechanical energy — it uses the battery to spin the engine. The alternator converts mechanical energy into electrical energy — it uses the engine to charge the battery. One drains the battery, the other fills it. One works for three seconds, the other works for the entire drive. If either fails, the car doesn't go anywhere for long."

**PPT Content:**
```
STARTER vs. ALTERNATOR — COMPARISON

                  STARTER              ALTERNATOR
Job:              Crank the engine     Charge battery + power loads
When active:      2-4 seconds          Entire time engine runs
Energy flow:      Electrical → Mechanical  Mechanical → Electrical
Current:          150-300 A (draws)    80-200 A (produces)
Key component:    Solenoid + Bendix    Diode bridge + Regulator
Common failure:   Slow/no crank        Under/overcharge
Primary test:     Current draw test    Output voltage test

THEY DO OPPOSITE JOBS — but both are essential.
```

---

#### Slide 11: The Battery — The Middleman
**Visual:** Simple diagram showing the battery at the centre with arrows: Alternator charges it (input), Starter draws from it (output), All vehicle loads draw from it (output). Voltage states shown: 12.6V resting, 14.2V charging, 10.5V+ cranking.

**Instructor Narration:**
> "The battery sits between these two systems. It stores energy from the alternator and delivers it to the starter — and to every other electrical load when the alternator can't keep up. Think of it as a reservoir. The alternator fills it, the starter and accessories drain it.
>
> Three voltage states you must know. Resting voltage — engine off, no load, battery has sat for a few minutes: a healthy battery reads 12.6 volts. Charging voltage — engine running, alternator working: 14.0 to 14.8 volts at the battery terminals. Cranking voltage — while the starter is drawing 200+ amps: voltage should not drop below about 10.5 volts. If it does, the battery is too weak or the starter is drawing too much. These three numbers — 12.6, 14.2, 10.5 — you'll use every day."

**PPT Content:**
```
THE BATTERY — THREE VOLTAGE STATES

                 RESTING        CHARGING       CRANKING
Condition:       Engine off,    Engine running  Key at START,
                 no load                        starter spinning
Expected:        12.4 - 12.7 V  14.0 - 14.8 V  > 10.5 V
What it tells:   Battery state   Alternator OK   Battery + starter OK
                 of charge       and regulating   condition

QUICK RULES:
  12.6 V resting = fully charged
  12.4 V resting = ~75% charged
  12.0 V resting = ~25% charged — needs charging
  < 12.0 V resting = dead or failing battery

  > 14.8 V charging = overcharge (regulator fault)
  < 13.5 V charging = undercharge (alternator fault)
  < 10.5 V cranking = weak battery or excessive draw
```

---

### **DEVELOPMENT PART 2: The Test Sequence** (Slides 12-14, ~15 minutes)

**Narrative Voice:** Practical and procedural. Setting up what they will do in the workshop.

---

#### Slide 12: The 5-Step Starting & Charging Test Sequence
**Visual:** Numbered flowchart — 5 boxes connected by arrows: (1) Battery Resting Voltage -> (2) Starter Current Draw -> (3) Alternator Output Voltage -> (4) Alternator AC Ripple -> (5) Parasitic Drain Overview. Each box has the meter setting and what you measure.

**Instructor Narration:**
> "Here's the systematic test sequence. You don't just test one thing — you test the whole chain, in order. Start with the battery, because everything else depends on it. Then test the starter's demand on the battery. Then test the alternator's ability to replenish it. Then check for AC ripple — a sign of failing diodes. And finally, a quick overview of parasitic drain — current that flows when the car is off. We'll do the first three hands-on today. Ripple and parasitic drain you'll refine in later weeks."

**PPT Content:**
```
THE 5-STEP STARTING & CHARGING TEST SEQUENCE

STEP 1: BATTERY RESTING VOLTAGE
  Meter: DMM on DC Volts
  Where: Battery terminals, engine off, lights off
  Pass: 12.4 - 12.7 V

STEP 2: STARTER CURRENT DRAW
  Meter: DC clamp meter around battery cable
  When: During cranking (helper turns key)
  Pass: 150-250 A petrol, 200-400 A diesel

STEP 3: ALTERNATOR OUTPUT VOLTAGE
  Meter: DMM on DC Volts
  Where: Battery terminals, engine running at ~2000 RPM
  Pass: 14.0 - 14.8 V

STEP 4: ALTERNATOR AC RIPPLE
  Meter: DMM on AC Volts
  Where: Battery terminals, engine running
  Pass: < 0.5 V AC (higher = failing diode)

STEP 5: PARASITIC DRAIN (overview today, detail later)
  Meter: DMM on DC milliamps in series with battery cable
  When: Engine off, all accessories off, modules asleep
  Pass: < 50 mA after 30-minute wait
```

---

#### Slide 13: Reading the Numbers — What They Mean
**Visual:** Three scenarios shown as meter displays with green/amber/red zones: Scenario A (all normal), Scenario B (low resting + high crank draw = bad battery), Scenario C (normal resting + low alternator output = bad alternator)

**Instructor Narration:**
> "The numbers tell a story. Scenario A: resting voltage 12.6, cranking drop to 10.8 volts, running voltage 14.2. Everything normal — battery is charged, starter draws within spec, alternator is regulating properly.
>
> Scenario B: resting voltage 12.1, cranking drops to 9.5 volts, running voltage 14.3. Battery is weak — low resting voltage, excessive drop during cranking. But the alternator is fine — 14.3 volts. The battery needs charging or replacing, not the alternator.
>
> Scenario C: resting voltage 12.6, cranking normal, running voltage 12.8. Battery started out fine, starter is fine, but the alternator output is barely above resting — it's not charging. Alternator fault. See how testing in sequence tells you which component has failed? This is diagnostic thinking — and it's built on the Ohm's Law and circuit knowledge from Days 6 and 7."

**PPT Content:**
```
READING THE NUMBERS — THREE SCENARIOS

SCENARIO A — ALL NORMAL:
  Resting: 12.6V   Cranking: 10.8V   Running: 14.2V
  Diagnosis: System healthy

SCENARIO B — WEAK BATTERY:
  Resting: 12.1V   Cranking: 9.5V    Running: 14.3V
  Diagnosis: Battery weak/discharged. Alternator OK.
  Action: Charge/test battery. Replace if fails load test.

SCENARIO C — ALTERNATOR FAULT:
  Resting: 12.6V   Cranking: 10.8V   Running: 12.8V
  Diagnosis: Battery OK. Alternator not charging.
  Action: Check belt, brushes, regulator, diodes.

DIAGNOSTIC LOGIC:
  Always test BATTERY FIRST — it affects everything else.
  Compare RESTING vs. RUNNING to evaluate alternator.
  Compare RESTING vs. CRANKING to evaluate battery + starter.
```

---

#### Slide 14: OBD-II Introduction — What We'll Do
**Visual:** Photo of an OBD-II 16-pin DLC connector with pin identification, plus photo showing typical under-dash location. Inset photo of a generic scan tool home screen.

**Instructor Narration:**
> "After the starting and charging tests, we'll do something you've been waiting for — plug a scan tool into a live vehicle. The OBD-II port is a 16-pin connector, almost always under the dashboard on the driver's side, within reach of the driver's seat. Every vehicle sold in Europe since 2001 for petrol and 2004 for diesel has one.
>
> We'll plug in, read any Diagnostic Trouble Codes — DTCs — that are stored, look at live data PIDs like coolant temperature, engine RPM, battery voltage, and oxygen sensor readings. Then we'll clear the codes and rescan to see if they come back. This is what you'll do every single day as a technician. Today is your first time."

**PPT Content:**
```
OBD-II — YOUR FIRST SCAN TOOL SESSION

OBD-II (On-Board Diagnostics, version 2):
  Standard diagnostic port on ALL modern vehicles
  16-pin DLC (Data Link Connector)
  Location: Under dashboard, driver's side

WHAT WE'LL DO TODAY:
  1. Locate the OBD-II port on a real vehicle
  2. Connect the scan tool and power it on
  3. Read stored DTCs (Diagnostic Trouble Codes)
  4. View LIVE DATA PIDs:
     — Engine RPM
     — Coolant temperature
     — Battery/system voltage
     — O2 sensor voltage
  5. Clear DTCs
  6. Rescan to check for returning codes

Pin 16: Battery positive (always hot)
Pin 4:  Chassis ground
Pin 5:  Signal ground
Pin 6:  CAN-High (Day 9!)
Pin 14: CAN-Low (Day 9!)
```

---

### **PRACTICAL PART 1: Starter/Alternator Identification & Testing** (Slides 15-18, ~50 minutes)

**Narrative Voice:** Workshop guide. Hands-on, step-by-step.

---

#### Slide 15: Workshop — Component Identification
**Visual:** Two annotated photos side by side: (1) engine bay with starter motor location circled and labeled (usually low on engine, near bell housing/transmission junction), (2) engine bay with alternator location circled and labeled (usually upper front of engine, belt-driven). Arrows point to key visible features: solenoid connector, B+ terminal, belt, pulley.

**Instructor Narration:**
> "First task: find them. The starter motor is usually bolted to the bell housing where the engine meets the transmission — low down, often hard to see from the top. Look for the heavy battery cable going to its B+ terminal and the solenoid connector on top. The alternator is typically on the upper front of the engine, driven by the serpentine belt. You can see the pulley, the B+ output terminal with a heavy wire, and a multi-pin connector for the field and signal wires.
>
> Split into your pairs. Each pair goes to a vehicle. Find the starter — you may need to look from underneath. Find the alternator — trace the serpentine belt. Identify the B+ terminals and connectors on both. You have 15 minutes."

**PPT Content:**
```
PRACTICAL TASK 1: FIND THE STARTER AND ALTERNATOR (15 min)

STARTER MOTOR:
  Location: Bolted to bell housing (engine-to-transmission)
  Usually visible from underneath, sometimes from above
  Look for: Heavy battery cable to B+ terminal
             Solenoid connector (smaller wire from relay)

ALTERNATOR:
  Location: Front/top of engine, driven by serpentine belt
  Usually visible from above
  Look for: Pulley with belt
             B+ output terminal (heavy wire to battery)
             Multi-pin connector (field + signal)

YOUR TASK (in pairs):
  1. Locate the starter motor — trace the B+ cable
  2. Locate the alternator — follow the serpentine belt
  3. Identify the B+ terminal and connectors on each
  4. Note: Can you see the ring gear through any inspection hole?
```

---

#### Slide 16: Workshop — Battery Resting Voltage Test
**Visual:** Step-by-step photo sequence: (1) DMM set to DC Volts 20V range, (2) Red probe on battery positive terminal, (3) Black probe on battery negative terminal, (4) Read display — example shows 12.58V. Green zone marked 12.4-12.7V.

**Instructor Narration:**
> "Step one of the test sequence: battery resting voltage. Engine off, headlights off, doors closed. Set your DMM to DC volts. Red probe on the positive terminal, black on negative. Read the display. Write it down. This is your baseline. If it's below 12.4 volts, the battery may need charging before you test the starter and alternator — a weak battery will give you misleading results on both."

**PPT Content:**
```
TEST STEP 1: BATTERY RESTING VOLTAGE

Conditions: Engine OFF, all loads OFF, key OUT
DMM setting: DC Volts (20V range)
Connections: RED probe → Battery POSITIVE (+)
             BLACK probe → Battery NEGATIVE (-)

Read and record: __________ V

INTERPRET:
  12.6 - 12.7 V = Fully charged (GOOD)
  12.4 - 12.5 V = 75% charged (ACCEPTABLE)
  12.0 - 12.3 V = Low charge (CHARGE BEFORE TESTING)
  < 12.0 V = Dead or failing (REPLACE/CHARGE)

NOTE: Battery must rest 10+ minutes after driving for accurate reading
```

---

#### Slide 17: Workshop — Starter Current Draw Test
**Visual:** Photo sequence: (1) DC clamp meter around the battery negative cable (easier access, same current), (2) Helper at the ignition ready to crank, (3) Clamp meter display during cranking showing 185A, (4) DMM simultaneously showing cranking voltage of 10.6V. Safety note: disable fuel/ignition to prevent engine starting during extended testing.

**Instructor Narration:**
> "Step two: starter current draw. This tells you how hard the starter is working. Clamp your DC current clamp around the battery negative cable — it carries the same current as the positive side and is often easier to access. Set the clamp meter to DC amps. Have your partner crank the engine for about 5 seconds while you watch the reading. A healthy petrol engine starter draws 150 to 250 amps. Higher than that? The starter motor is dragging — worn bearings, shorted windings, or the engine has high resistance — maybe a timing issue or oil too thick.
>
> At the same time, you can monitor cranking voltage with a second DMM at the battery terminals. Voltage should stay above 10.5V. If it drops below that while current is within spec, the battery is weak. If current is too high AND voltage drops, the starter is the problem."

**PPT Content:**
```
TEST STEP 2: STARTER CURRENT DRAW

Tool: DC clamp meter (capable of 400A+ range)
Clamp around: Battery NEGATIVE cable
DMM on battery: Monitoring cranking voltage simultaneously

PROCEDURE:
  1. Clamp meter on battery negative cable — set DC Amps
  2. DMM across battery terminals — set DC Volts
  3. Partner cranks engine for ~5 seconds
  4. Record PEAK CURRENT and MINIMUM VOLTAGE during crank

INTERPRET:
  Current 150-250 A + Voltage > 10.5V = Normal (petrol)
  Current > 300 A = Excessive draw (dragging starter/engine)
  Current normal + Voltage < 10.5V = Weak battery
  Current very low + no crank = Open circuit (bad connection)

SAFETY: For extended testing, disable fuel pump fuse to prevent
        engine start. Replace fuse when done.
```

---

#### Slide 18: Workshop — Alternator Output Voltage Test
**Visual:** Photo: Engine running, DMM probes on battery terminals showing 14.28V. Second photo: RPM held at ~2000 with assistant. Third photo: Headlights turned ON — voltage still above 14.0V. All readings in green zone.

**Instructor Narration:**
> "Step three: start the engine and test the alternator output. DMM on DC volts, probes on the battery terminals. At idle, you should see between 13.8 and 14.8 volts. Rev the engine to about 2000 RPM — the voltage should be stable around 14.0 to 14.5 volts. Now turn on the headlights, blower fan on high, rear demister — load the system. Voltage should drop slightly but stay above 13.8 volts. If it drops below 13.5 under load, the alternator is struggling.
>
> For the ripple test, switch your DMM to AC volts while the engine is running. You should see less than 0.5 volts AC. If you see 1 volt or more, one or more diodes in the rectifier bridge have failed — AC is leaking through. Write down all your numbers. We'll discuss them as a group."

**PPT Content:**
```
TEST STEP 3: ALTERNATOR OUTPUT VOLTAGE

Conditions: Engine running, warmed up, ~2000 RPM
DMM setting: DC Volts across battery terminals

MEASUREMENTS:
  A. Idle, no load:         Target 13.8 - 14.8 V = ____ V
  B. 2000 RPM, no load:     Target 14.0 - 14.5 V = ____ V
  C. 2000 RPM, full load:   Target > 13.8 V     = ____ V
     (headlights + blower + rear demist ON)

INTERPRET:
  14.0 - 14.8 V = Alternator charging correctly
  > 15.0 V = Overcharging — regulator fault
  < 13.5 V under load = Undercharging — check belt, brushes

BONUS — AC RIPPLE TEST:
  DMM set to AC Volts, across battery, engine running
  Pass: < 0.5 V AC
  Fail: > 0.5 V AC = diode failure in rectifier bridge
```

---

### **PRACTICAL PART 2: OBD-II Scan Tool Session** (Slides 19-21, ~30 minutes)

**Narrative Voice:** Guided discovery. Let learners navigate the tool themselves with coaching.

---

#### Slide 19: Connecting the Scan Tool
**Visual:** Step-by-step annotated photos: (1) Locate OBD-II port under driver's dashboard, (2) Plug in 16-pin connector (keyed — only goes in one way), (3) Turn ignition to ON (not START), (4) Scan tool powers up and shows vehicle identification screen. Arrow indicates pin 16 provides power — no separate battery needed.

**Instructor Narration:**
> "Find the OBD-II port. It's under the dashboard, driver's side, usually near the steering column or behind a small cover. Plug in the scan tool connector — it's keyed, it only goes in one way, don't force it. Turn the ignition to ON but don't start the engine yet. The scan tool gets power from pin 16 of the connector — it's wired directly to the battery through a fuse. The tool should power up and ask you to select the vehicle or auto-detect it. Follow the prompts.
>
> Once connected, go to 'Read Codes' or 'DTCs.' The tool will query the ECU and display any stored trouble codes. These are the five-character codes from Day 9 — P for powertrain, B for body, C for chassis, U for network. Write down every code it shows."

**PPT Content:**
```
OBD-II — CONNECTING THE SCAN TOOL

STEP 1: Locate OBD-II port
  Under dashboard, driver's side
  May have a cover — flip it open

STEP 2: Plug in the 16-pin DLC connector
  Keyed — only fits one way. DO NOT force.

STEP 3: Turn ignition to ON (do NOT start engine)
  Scan tool powers from pin 16 (battery positive)

STEP 4: Select vehicle or let tool auto-detect
  Some tools read VIN automatically (Day 1 knowledge!)

STEP 5: Navigate to "Read DTCs" or "Trouble Codes"
  Tool queries PCM/ECM via CAN bus (Day 9!)
  Record ALL codes displayed

DTC FORMAT REMINDER (Day 9):
  P0xxx = Powertrain (generic)
  P1xxx = Powertrain (manufacturer-specific)
  B = Body, C = Chassis, U = Network
```

---

#### Slide 20: Live Data PIDs
**Visual:** Screenshot of a scan tool live data screen showing four PIDs in real time: Engine RPM (0 — engine off), Coolant Temperature (82 deg C), Battery Voltage (12.6V), O2 Sensor Bank 1 Sensor 1 (0.45V). Arrow pointing to "Start engine to see values change."

**Instructor Narration:**
> "Now navigate to 'Live Data' or 'Data Stream.' This is where it gets interesting. You're looking at what the ECU sees RIGHT NOW in real time. Find these four PIDs: Engine RPM — should show 0 with engine off, about 750 at idle. Coolant temperature — should rise as the engine warms up. Battery voltage — the ECU's measurement, should match your DMM reading closely. And Oxygen sensor voltage — the O2 sensor in the exhaust. At idle on a warm engine, it should oscillate between about 0.1 and 0.9 volts — that's the sensor switching between lean and rich.
>
> Start the engine. Watch the RPM climb to idle. Watch the coolant temperature rise. Compare the scan tool's battery voltage to your DMM reading — they should be within a couple of tenths. This is the ECU confirming what your multimeter is telling you. Two sources of truth."

**PPT Content:**
```
LIVE DATA PIDs — WHAT TO LOOK FOR

PID 1: ENGINE RPM
  Engine off: 0 RPM
  Idle: 650-850 RPM (typical)
  Rev to 2000: Should respond immediately

PID 2: COOLANT TEMPERATURE
  Cold start: Ambient temperature
  Warm: 80-100 deg C (normal operating)
  Watch it RISE as engine warms — proves sensor works

PID 3: BATTERY / SYSTEM VOLTAGE
  Engine off: ~12.6V
  Engine running: ~14.0-14.5V
  Compare to your DMM! Should match closely.

PID 4: O2 SENSOR (Bank 1, Sensor 1)
  Warm engine, idle: Oscillates 0.1V - 0.9V
  Switching = catalytic converter loop is active
  Stuck high or low = possible sensor or fuel fault

ACTIVITY: Start the engine. Watch all 4 PIDs change in real time.
```

---

#### Slide 21: Clear Codes and Rescan
**Visual:** Two-panel display: Left panel shows "DTCs Found: P0420 — Catalyst Efficiency Below Threshold." Right panel shows "Clear Codes?" confirmation dialog. Below: "After clearing — RESCAN. If code returns immediately, the fault is CURRENT."

**Instructor Narration:**
> "If you found any codes, let's clear them. Navigate to 'Clear Codes' or 'Erase DTCs.' Confirm when prompted. The tool sends a command over CAN bus to the ECU to reset the fault memory. The check engine light — if it was on — should turn off.
>
> Now here's the diagnostic thinking. Rescan immediately. If the code comes back right away, the fault is current — it's happening right now. If the code stays cleared, it was a historical fault — maybe it happened once and hasn't returned. This is the difference between a current fault and a stored/pending fault. In professional diagnostics, you never just clear codes and send the car away. You investigate why the code was there. But today, we're learning the tool. The diagnostic thinking deepens in Weeks 3 through 7."

**PPT Content:**
```
CLEAR CODES & RESCAN — DIAGNOSTIC LOGIC

STEP 1: Navigate to "Clear DTCs" / "Erase Codes"
  Confirm when prompted
  Check engine light should turn OFF

STEP 2: RESCAN immediately
  Navigate back to "Read DTCs"
  Scan again

INTERPRET:
  Code returns IMMEDIATELY → CURRENT fault (active now)
  Code stays CLEARED → HISTORICAL fault (happened before)

PROFESSIONAL RULE:
  NEVER just clear codes and send the car away!
  Always investigate WHY the code was set.
  Clearing without diagnosis = hiding the problem.

TODAY: We are learning the TOOL.
LATER: We learn the THINKING behind each code.
```

---

### **REVIEW & QUIZ: Week 2 Consolidation** (Slides 22-25, ~30 minutes)

**Narrative Voice:** Celebratory but focused. This is the Week 2 checkpoint.

---

#### Slide 22: Week 2 — The Complete Story
**Visual:** Visual summary infographic — five interconnected nodes representing Days 6-10, each with a one-line summary and key concept icon. Connecting lines show how each day built on the last.

**Instructor Narration:**
> "Let me tell you the story of your week. On Day 6, you learned the three fundamental quantities — voltage, current, and resistance — and how Ohm's Law connects them. On Day 7, you learned how components connect — series circuits share current, parallel circuits share voltage — and you read your first wiring diagrams. On Day 8, you learned what goes wrong — opens that stop current, shorts that create dangerous paths, high resistance that steals voltage — and the components that protect against these faults: fuses, relays, and circuit breakers. On Day 9, you learned how the car thinks — ECUs reading sensors, commanding actuators, talking to each other on CAN bus, and storing fault codes when something goes wrong. And today, Day 10, you applied ALL of it — the starter circuit uses everything from Days 6-8, the alternator's voltage regulation is the closed-loop system from Day 9, and the scan tool reads those DTCs over the CAN bus you learned about yesterday.
>
> You now speak the LANGUAGE of every electrical system in the car. You can measure it, trace it, understand its faults, and read what the car's own computers are telling you. That's the foundation for everything that comes next."

**PPT Content:**
```
WEEK 2 — THE COMPLETE ELECTRICAL STORY

Day 6:  THE LANGUAGE — Voltage (V), Current (A), Resistance (ohm)
        Ohm's Law: V = I x R
Day 7:  THE GRAMMAR — Series & Parallel Circuits, Schematics
        Current paths, voltage division
Day 8:  THE FAILURES — Open, Short, High Resistance
        Fuses, Relays, Circuit Protection
Day 9:  THE NETWORK — ECUs, Sensors, Actuators, CAN Bus, DTCs
        The car as a connected computer system
Day 10: THE APPLICATION — Starter, Alternator, OBD-II
        Real systems, real tests, real tools

YOU NOW SPEAK THE LANGUAGE OF EVERY SYSTEM IN THE CAR.
```

---

#### Slide 23: Formative Quiz — Questions 1-5
**Visual:** Clean quiz layout — numbered questions with multiple choice options A-D. No answers shown yet.

**Instructor Narration:**
> "Time for a quiz. Ten questions covering everything from this week. This is formative — not graded — but it tells YOU how well you've absorbed the material. Write your answers on paper. I'll reveal the answers after all ten questions. Don't worry about getting them all right — worry about understanding WHY the answer is what it is."

**PPT Content:**
```
WEEK 2 FORMATIVE QUIZ — Questions 1-5

Q1: In the sensor-ECU-actuator pattern, what does the ECU do?
  A) Generates electricity
  B) Reads sensor data and commands actuators
  C) Stores fuel
  D) Provides mechanical power

Q2: A circuit has 12V and 4 ohms resistance. What is the current?
  A) 48 A
  B) 3 A
  C) 0.33 A
  D) 16 A

Q3: In a SERIES circuit with three identical bulbs, if one burns out:
  A) The other two get brighter
  B) All three go out
  C) The other two are unaffected
  D) The circuit voltage doubles

Q4: A wire has become corroded, increasing its resistance. This is:
  A) An open circuit fault
  B) A short circuit fault
  C) A high resistance fault
  D) Normal operation

Q5: A relay allows:
  A) A small current to control a large current
  B) AC to be converted to DC
  C) Fuel to flow to the engine
  D) The battery to be charged
```

---

#### Slide 24: Formative Quiz — Questions 6-10
**Visual:** Continuation of quiz layout — questions 6-10.

**PPT Content:**
```
WEEK 2 FORMATIVE QUIZ — Questions 6-10

Q6: A 10A fuse protects a circuit that normally draws 8A.
    The fuse keeps blowing. The most likely cause is:
  A) The fuse is too large
  B) The circuit has a short circuit fault
  C) The battery voltage is too low
  D) The alternator is overcharging

Q7: A fully charged 12V car battery at rest should read approximately:
  A) 14.4 V
  B) 12.6 V
  C) 11.0 V
  D) 9.6 V

Q8: The CAN bus in a vehicle is used for:
  A) Cooling the engine
  B) Communication between ECUs
  C) Charging the battery
  D) Locking the doors mechanically

Q9: The OBD-II diagnostic port is typically located:
  A) Under the bonnet, near the battery
  B) In the boot, near the spare tyre
  C) Under the dashboard, near the driver's knee
  D) Behind the rear bumper

Q10: A properly functioning alternator should produce approximately:
  A) 12.0 V at the battery terminals
  B) 14.0 - 14.8 V at the battery terminals
  C) 18.0 V at the battery terminals
  D) 9.6 V at the battery terminals
```

---

#### Slide 25: Quiz Answers & Discussion
**Visual:** All 10 questions with correct answers highlighted in green and brief explanations. Two-column layout for space efficiency.

**Instructor Narration:**
> "Let's go through the answers. For each one, I don't just want the right letter — I want you to understand WHY.
>
> Question 1: B — the ECU reads sensor data and commands actuators. That's the pattern from Day 9.
> Question 2: B — Ohm's Law: I = V/R = 12/4 = 3 amps. Day 6 fundamentals.
> Question 3: B — series circuit: one path for current. If one bulb breaks the path, all go out. Day 7.
> Question 4: C — corrosion increases resistance without fully breaking the circuit. That's a high-resistance fault from Day 8. It causes voltage drops at the corroded point.
> Question 5: A — a relay uses a small control current to switch a large load current. Day 8.
> Question 6: B — if a correctly-rated fuse keeps blowing, excess current is flowing. A short circuit creates a low-resistance path that draws too much current. Day 8.
> Question 7: B — 12.6 volts is a fully charged 12V battery at rest. Today's lesson.
> Question 8: B — CAN bus is the communication network between ECUs. Day 9.
> Question 9: C — under the dashboard, driver's side. We literally just used it today.
> Question 10: B — 14.0 to 14.8 volts. Today's alternator lesson."

**PPT Content:**
```
QUIZ ANSWERS

Q1:  B — ECU reads sensors and commands actuators (Day 9)
Q2:  B — I = V/R = 12/4 = 3 A (Day 6, Ohm's Law)
Q3:  B — Series: one path. Break = all stop. (Day 7)
Q4:  C — Corrosion = high resistance fault (Day 8)
Q5:  A — Small current controls large current (Day 8)
Q6:  B — Correct fuse blowing = short circuit (Day 8)
Q7:  B — 12.6V = fully charged resting battery (Day 10)
Q8:  B — CAN bus = ECU communication network (Day 9)
Q9:  C — Under dashboard, driver's side (Day 10)
Q10: B — Alternator output = 14.0 - 14.8 V (Day 10)

HOW DID YOU SCORE?
  9-10: Excellent — you own this material
  7-8:  Good — review the topics you missed
  5-6:  Fair — revisit Days 6-8 notes this weekend
  < 5:  See me after class — we'll work through it
```

---

### **WRAP-UP: Week 2 Celebration & Week 3 Preview** (Slides 26-27, ~15 minutes)

---

#### Slide 26: Week 2 Achievement
**Visual:** Achievement checklist with green tick marks. Professional certificate-style border. Title: "You Now Speak Electricity."

**Instructor Narration:**
> "I want you to appreciate what you've accomplished this week. Five days ago, the word 'ohm' meant nothing to you. Now you can measure voltage, current, and resistance. You can trace a circuit on a wiring diagram. You can diagnose whether a fault is an open, a short, or a high resistance. You know what an ECU does, how CAN bus works, and what a DTC means. You've tested a real battery, a real starter circuit, a real alternator output. And you've plugged a scan tool into a live vehicle and read its codes.
>
> You now speak the language that every vehicle system uses. From Week 3 onward, when we say 'the coolant temperature sensor sends a signal to the ECU,' you'll know EXACTLY what that means — a variable resistance changing a voltage that the ECU reads on an ADC channel and compares to a lookup table. That's the power of this week. Congratulations."

**PPT Content:**
```
WEEK 2 COMPLETE — YOU NOW SPEAK ELECTRICITY

You can now:
  Measure voltage, current, and resistance with a DMM
  Apply Ohm's Law to calculate circuit values
  Identify series and parallel circuit behaviour
  Read basic wiring diagrams and schematics
  Diagnose open, short, and high-resistance faults
  Explain how fuses and relays protect and control circuits
  Describe the sensor-ECU-actuator control loop
  Explain what CAN bus does and why it matters
  Read and interpret Diagnostic Trouble Codes (DTCs)
  Identify starter and alternator components
  Perform a basic starting and charging test sequence
  Connect a scan tool, read codes, and view live data

THIS IS THE FOUNDATION FOR EVERYTHING THAT FOLLOWS.
```

---

#### Slide 27: Week 3 Preview — The Heart: Engine Systems
**Visual:** Dramatic cutaway image of a 4-cylinder engine with intake, exhaust, ignition, and fuel injection systems visible. Title overlay: "Week 3 — The Heart."

**Instructor Narration:**
> "Next week, we go inside the engine. Week 3 is called 'The Heart — Engine Systems.' You'll learn the four-stroke cycle — intake, compression, power, exhaust — and understand exactly how air, fuel, and spark come together to produce power. You'll learn about the intake system, the fuel system with injectors, the ignition system with coils and spark plugs, and the exhaust system with catalytic converters and oxygen sensors. Every one of these systems uses the electrical knowledge you built this week — sensors, ECUs, actuators, fault codes.
>
> Enjoy your weekend. Review your notes. When you come back Monday, we crack open the engine. See you then."

**PPT Content:**
```
WEEK 3 PREVIEW: THE HEART — ENGINE SYSTEMS

Day 11: The 4-Stroke Cycle — How Engines Make Power
Day 12: Air & Fuel — Intake, Injection, Combustion
Day 13: Spark & Fire — Ignition Systems
Day 14: Exhaust & Emissions — Catalysts, O2 Sensors, EGR
Day 15: Engine Diagnostics & Week 3 Consolidation

EVERY SYSTEM uses what you learned this week:
  — Sensors measure temperature, pressure, position
  — ECUs calculate fuel, timing, emissions
  — Actuators fire injectors, spark plugs, valves
  — CAN bus carries it all
  — DTCs tell you when something goes wrong

Enjoy your weekend. Review your Week 2 notes.
Monday: we crack open the engine.
```

---

## Assessment Checkpoint

**Formative (not graded):**
- 10-question MCQ quiz covering Days 6-10 content (administered during session)
- Starter/alternator component identification on live vehicle
- Battery-starter-alternator voltage test sequence with recorded measurements
- OBD-II scan tool operation: successfully read DTCs, view live data, clear codes
- Target: learners should score at least 7/10 on the MCQ

**Practical competency check:**
- Can the learner independently connect a DMM and measure battery resting voltage?
- Can the learner identify the starter motor and alternator on a vehicle?
- Can the learner connect a scan tool and navigate to DTCs and live data without step-by-step prompting?

---

## Key Takeaways

1. The starter motor converts electrical energy to mechanical rotation to crank the engine — it draws 150-300A for 2-4 seconds through a solenoid-controlled circuit
2. The alternator converts mechanical rotation to regulated DC voltage (14.0-14.8V) to charge the battery and power all electrical loads while the engine runs
3. Always test in sequence: battery first (resting voltage), then starter (current draw), then alternator (output voltage) — the battery condition affects every other reading
4. Three battery voltage states every technician must know: 12.6V resting, 14.2V charging, above 10.5V cranking
5. OBD-II is the universal diagnostic interface — every modern vehicle has one, and the scan tool is the technician's primary diagnostic weapon
6. Week 2 built the complete electrical foundation: language (V, I, R) + grammar (circuits) + failure modes (faults) + communication (CAN/DTCs) + application (starting/charging/OBD-II)

---

## Preparation for Week 3

**Instructor prep:**
- Source a cutaway or sectioned engine model (or high-quality 3D animation) showing piston, connecting rod, crankshaft, camshaft, valves, intake and exhaust ports
- Prepare a vehicle with accessible spark plugs for removal and inspection
- Obtain a timing light (if available) for ignition timing demonstration
- Print 4-stroke cycle diagrams (intake-compression-power-exhaust) as handouts
- Prepare a compression tester for Day 11 practical
- Source assorted used spark plugs showing different conditions (normal, fouled, worn, overheated) for visual diagnosis exercise
- Ensure fuel system safety equipment is available (fire extinguisher, fuel-safe containers, nitrile gloves)

**Learner prep:**
- Review Week 2 notes, especially sensor-ECU-actuator pattern (Day 9) — every engine system uses this pattern
- Look up your workshop vehicle's engine specifications: number of cylinders, displacement, fuel type, power output
- Optional: watch a slow-motion video of a 4-stroke engine cycle online
