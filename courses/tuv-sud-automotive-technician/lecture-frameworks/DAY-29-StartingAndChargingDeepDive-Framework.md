---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 6
week_title: "Power Delivery — Transmission & Charging"
day_number: 29
session_title: "Starting & Charging — The Deep Dive"
duration_minutes: 180
theory_practice: "35:65"
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 29: Starting & Charging — The Deep Dive
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (65 min theory + 115 min practical)
**Approach:** Systematic Disassembly & Professional Test Sequence
**PPT Target:** 26-28 slides
**Week:** 6 of 8 — "Power Delivery — Transmission & Charging"

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Identify and explain the function of every internal component of a starter motor (armature, commutator, brushes, field coils/permanent magnets, solenoid with pull-in and hold-in windings, Bendix drive/overrunning clutch)
- Trace the complete starter circuit from ignition switch through neutral safety switch, starter relay, solenoid, to motor and ground
- Identify and explain every internal component of an alternator (rotor with field winding, stator with 3-phase winding, diode rectifier bridge, voltage regulator, pulley type)
- Perform a complete professional starting and charging system test sequence: battery SOH, cranking voltage, starter current draw, alternator output voltage, AC ripple, parasitic drain
- Execute voltage drop testing at each connection point in the starter circuit
- Systematically diagnose slow crank, no-crank, undercharge, and overcharge conditions

**Connection to Day 10:** Day 10 introduced starting and charging as part of the overall electrical system survey. Day 29 is the full professional deep dive — complete construction details, operational theory, and the test sequences you will use every working day.

---

## Connection to Prior Knowledge

Build from:
- Day 10: Starting and charging system overview — battery, starter, alternator basics
- Day 7-8: Multimeter operation, voltage measurement, circuit fundamentals
- Day 9: Ohm's Law, series/parallel circuits, voltage drop concepts
- Day 11: Wiring diagrams and circuit tracing
- Day 28: Transmission systems — understanding mechanical engagement and drive mechanisms

**Bridge:** "On Day 10, you met the starting and charging system. You learned that the starter spins the engine and the alternator charges the battery. That was the introduction. Today, we take both of them apart, learn exactly how they work inside, and then you'll run the same test sequence that a master technician uses to diagnose every starting and charging complaint that rolls into the shop."

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: From Introduction to Mastery** (Slides 1-3, ~10 minutes)

**Narrative Voice:** Direct, professional, building anticipation. This is a transition from survey knowledge to diagnostic competence.

---

#### Slide 1: Title & Day 10 Callback
**Visual:** Split image — left side shows a simple starter-battery-alternator triangle diagram from Day 10; right side shows a cutaway starter motor with every internal component visible, plus an oscilloscope waveform showing alternator AC ripple.

**Instructor Narration:**
> "Day 10. Remember this triangle? Battery powers the starter, starter cranks the engine, alternator charges the battery. That was the overview. You understood the WHAT. Today is the HOW. We're going to physically take a starter motor apart and an alternator apart. You're going to hold the armature, touch the brushes, count the diodes. And then we're going to the car, and you'll run a complete professional test sequence — the same one that separates a parts-swapper from a real diagnostician."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 6: Power Delivery — Transmission & Charging
Day 29: Starting & Charging — The Deep Dive

Day 10 was the introduction.
Day 29 is the mastery session.

Today: Full construction, operation, and professional testing.
```

---

#### Slide 2: Why This Matters
**Visual:** Three workshop scenario photos — (1) customer car that won't start on a Monday morning, (2) battery warning light illuminated on dashboard, (3) dead battery found after overnight park.

**Instructor Narration:**
> "Starting and charging complaints are some of the most common jobs you'll see. 'My car won't start.' 'My battery keeps going flat.' 'The battery light came on.' Every one of these requires you to test systematically. Swap a starter without testing the circuit, and you'll put in a new starter that also won't work — because the real problem was a corroded ground cable with a 2-volt drop. Swap an alternator without checking AC ripple, and you'll throw away a good alternator when the real fault was a single failed diode. The test sequence is everything."

**PPT Content:**
```
WHY STARTING & CHARGING DIAGNOSTICS MATTER

Top 10 most common workshop complaints:
#2: "My car won't start"
#5: "My battery keeps going flat"
#7: "Battery light is on"

The WRONG approach:
Guess → Swap parts → Hope it works → Lose money

The RIGHT approach:
Test → Measure → Isolate → Fix the actual fault → Profit

Today you learn the RIGHT approach.
```

---

#### Slide 3: Today's Plan
**Visual:** Horizontal four-block timeline — Setup, Theory (Starter + Alternator), Practical (Disassembly + Vehicle Testing), Wrap-Up.

**Instructor Narration:**
> "Here's the plan. First 45 minutes: I'll teach you the construction and operation of the starter motor and alternator in full detail — every component, every circuit path. Then we move to the bench. You'll disassemble a starter motor and an alternator, identify every part. After that, we go to the car. You'll run a complete starting and charging test sequence: battery state of health, cranking voltage, starter current draw, alternator output, AC ripple, and parasitic drain. Finally, voltage drop testing across the entire starter circuit. By the end of today, you own this system."

**PPT Content:**
```
TODAY'S PLAN (180 minutes)

SETUP (10 min): Day 10 to Day 29 — from overview to mastery

THEORY (45 min): Starter motor & alternator — full construction,
operation, and circuit detail

PRACTICAL (95 min):
  Station 1: Starter motor disassembly & component ID
  Station 2: Alternator disassembly & component ID
  Station 3: Complete vehicle test sequence
  Station 4: Voltage drop testing — starter circuit

WRAP-UP (15 min): Fault isolation flowcharts + consolidation

+ 15 min buffer/Q&A throughout
```

---

### **DEVELOPMENT PART 1: The Starter Motor — Complete Construction & Operation** (Slides 4-11, ~25 minutes)

**Narrative Voice:** Methodical, building from the outside in. Take them through every layer of the starter motor.

---

#### Slide 4: Starter Motor — External Overview
**Visual:** Annotated photograph of a complete starter motor showing the solenoid mounted on top, the main body (housing), the drive end with Bendix visible, and the terminal connections (B terminal, S terminal, M terminal, ground through housing).

**Instructor Narration:**
> "Before we open it, let's look at the outside. The starter motor has two main sections: the solenoid on top, and the motor body below. At the drive end, you can see the Bendix gear — that's what engages with the engine's ring gear. On the solenoid, you have three connections: the B terminal comes directly from the battery positive through a heavy cable. The S terminal is the signal wire from the ignition switch circuit. And the M terminal connects internally to the motor. The housing itself is the ground path — bolted to the engine block.
>
> When you turn the key, a small current flows through the S terminal. That energises the solenoid, which does two jobs simultaneously: it slides the Bendix gear forward to engage the ring gear, AND it closes a heavy-duty contact that sends full battery current from B terminal through to the motor. The motor spins, the engine cranks. Release the key, and everything disengages."

**PPT Content:**
```
STARTER MOTOR — EXTERNAL VIEW

Two main sections:
1. SOLENOID (top) — electromagnetic switch + gear engagement
2. MOTOR BODY (below) — DC motor that does the cranking

External connections:
• B terminal — Battery positive (heavy cable, 4-6 AWG)
• S terminal — Signal from ignition switch circuit (small wire)
• M terminal — Internal connection to motor windings
• Ground — Through housing → engine block → battery negative

When you turn the key:
1. Small current flows to S terminal
2. Solenoid engages Bendix gear with ring gear
3. Solenoid closes heavy contact (B → M)
4. Full battery current flows through motor
5. Motor spins → engine cranks
```

---

#### Slide 5: Inside the Motor — Armature & Commutator
**Visual:** Cutaway diagram and bench photo of a starter motor armature showing the laminated iron core, copper wire windings in the slots, and the commutator segments at one end. Close-up inset of commutator showing individual copper segments separated by mica insulation.

**Instructor Narration:**
> "Let's go inside. The armature is the rotating part — the heart of the motor. It has a laminated iron core with slots, and heavy copper wire is wound through those slots. When current flows through these windings, they create an electromagnetic field that interacts with the field around the housing, and the armature spins.
>
> At one end of the armature is the commutator — a ring of copper segments separated by thin strips of mica insulation. The commutator is the switching mechanism. As the armature rotates, each segment contacts the carbon brushes in sequence, reversing the current direction in the windings at exactly the right moment to keep the armature spinning in the same direction. Without the commutator, the motor would just oscillate back and forth. The commutator is what turns it into continuous rotation.
>
> When you inspect a commutator, you're looking for: scoring or grooves from brush wear, burned segments from arcing, and mica insulation that's flush with the copper — it should be undercut below the surface."

**PPT Content:**
```
ARMATURE & COMMUTATOR

ARMATURE (the rotating part):
• Laminated iron core — reduces eddy current losses
• Copper windings in core slots — create electromagnetic field
• Shaft — supported by bearings at each end
• Commutator at one end

COMMUTATOR:
• Ring of copper segments separated by mica insulation
• Each segment connects to a section of armature winding
• Acts as rotary switch — reverses current direction
  as armature spins → continuous rotation in one direction

INSPECTION POINTS:
• Scoring/grooves from brush wear → resurface or replace
• Burned/blackened segments → excessive arcing, failing brushes
• Mica insulation level → must be UNDERCUT below copper surface
• Out-of-round → causes intermittent contact, rough cranking
```

---

#### Slide 6: Inside the Motor — Field Coils, Permanent Magnets & Brushes
**Visual:** Cross-section diagram showing field coils wound around pole shoes inside the housing (series-wound type), with an alternative showing permanent magnets (PMGR type). Separate photo of carbon brushes — new vs. worn — with brush springs.

**Instructor Narration:**
> "The armature sits inside the housing, surrounded by the field system. In older and heavy-duty starters, you'll find field coils — copper wire wound around iron pole shoes bolted to the inside of the housing. These are wired in series with the armature, which is why we call it a series-wound DC motor. Series winding gives maximum torque at low speed — exactly what you need to crank an engine from standstill.
>
> In modern, lighter starters — particularly the gear-reduction type — the field coils are replaced by permanent magnets. These are called PMGR starters — Permanent Magnet Gear Reduction. Simpler, lighter, fewer things to fail. But they can't be rewound — if the magnets crack or lose magnetism, you replace the starter.
>
> The brushes are the electrical connection between the stationary housing and the spinning commutator. Carbon brushes pressed by springs against the commutator surface. They carry hundreds of amps. They wear down over time — brush length is a critical inspection measurement. Too short, and the springs can't maintain contact. You get intermittent cranking, then no cranking at all."

**PPT Content:**
```
FIELD SYSTEM & BRUSHES

FIELD COILS (older / heavy-duty starters):
• Copper wire wound around iron pole shoes
• Series-wound with armature → maximum starting torque
• Can be rewound (specialist job)

PERMANENT MAGNETS (modern PMGR starters):
• Rare-earth magnets bonded to housing
• Lighter, simpler, more reliable
• NOT serviceable — replace if damaged

BRUSHES:
• Carbon blocks pressed against commutator by springs
• Carry 150-300+ amps during cranking
• WEAR ITEM — check length against specification
• New brush: typically 12-15 mm
• Replace when: worn to 6-7 mm (manufacturer spec)

Brush failure symptoms:
• Intermittent cranking → slow → no crank
• Brush dust contamination → shorts between segments
```

---

#### Slide 7: The Solenoid — Pull-In and Hold-In Windings
**Visual:** Cutaway diagram of a starter solenoid showing the two coil windings (pull-in winding and hold-in winding) wrapped around the plunger, the plunger itself, the return spring, the contact disc, and the B and M terminals. Electrical schematic showing both windings and their circuit paths.

**Instructor Narration:**
> "The solenoid is the most clever part of the starter. It does two jobs with one action: it engages the drive gear, and it switches heavy current to the motor. And it uses a trick with two windings to do it efficiently.
>
> When you first energise the S terminal, current flows through TWO windings simultaneously. The pull-in winding is a heavy winding that creates a strong magnetic field — strong enough to overcome the return spring and pull the plunger forward. This forward motion does two things: through a lever, it pushes the Bendix drive gear forward to mesh with the ring gear. And the plunger's contact disc bridges the B and M terminals, sending full battery current to the motor.
>
> Here's the clever part. The pull-in winding is wired from S terminal through the winding, then out to the M terminal — which means it has battery voltage on BOTH ends once the contact disc closes. Equal voltage on both ends means zero current through the pull-in winding. It switches itself off. Now only the hold-in winding — a lighter winding from S terminal to ground — keeps the plunger in position. This reduces current draw on the ignition switch circuit from about 40 amps down to about 10 amps.
>
> Why does this matter for diagnosis? If your battery is marginal, you might have enough power to pull in but not enough to hold in AND crank. The solenoid chatters — rapid clicking. That clicking is the solenoid engaging, battery voltage dropping under motor load, solenoid releasing, battery recovering, engaging again. Classic symptom of a weak battery."

**PPT Content:**
```
STARTER SOLENOID — TWO WINDINGS, TWO JOBS

PULL-IN WINDING (heavy wire):
• Path: S terminal → winding → M terminal
• Creates STRONG magnetic field
• Pulls plunger forward against return spring
• Engages Bendix with ring gear via lever
• Plunger contact disc bridges B to M (motor powered)
• Self-cancelling: once B=M voltage, no current flows
• Draw: ~30-40 amps (brief)

HOLD-IN WINDING (lighter wire):
• Path: S terminal → winding → ground
• Maintains plunger in engaged position
• Lower current draw (~8-12 amps)
• Stays energised as long as key held at START

TWO MECHANICAL ACTIONS:
1. Lever pushes Bendix drive forward → gear engagement
2. Contact disc closes B-to-M → motor receives full current

DIAGNOSTIC CLUE:
Rapid clicking (chatter) = solenoid engaging/disengaging
repeatedly → battery cannot sustain voltage under load
```

---

#### Slide 8: Bendix Drive & Overrunning Clutch
**Visual:** Exploded view of a Bendix drive assembly showing the pinion gear, the overrunning clutch (roller type), the drive sleeve, and the helical spline on the armature shaft. Cross-section showing roller clutch engaged vs. overrunning.

**Instructor Narration:**
> "The Bendix drive is the engagement mechanism — how the starter's motor connects to the engine's flywheel ring gear. The pinion gear on the starter is tiny — maybe 9 to 11 teeth. The ring gear on the flywheel has over 100 teeth. That gear ratio — typically around 10:1 to 15:1 — multiplies the starter motor's torque to crank the engine.
>
> But here's the problem. The moment the engine starts, it accelerates quickly. If the starter pinion stayed engaged, the engine would spin the starter motor at 10 to 15 times engine speed — it would destroy the armature. So the Bendix drive includes an overrunning clutch. In one direction — starter driving engine — the clutch locks. In the other direction — engine driving starter — the clutch freewheels. The rollers inside the clutch wedge into tapered chambers when driving, and roll free when overdriven.
>
> On the older inertia-type Bendix, the pinion rides on a helical thread. When the motor starts spinning, inertia causes the heavy pinion to slide forward on the thread and engage. When the engine starts, the pinion is spun faster than the thread and screws back out of engagement. You'll still see these on some older vehicles and industrial applications.
>
> The modern pre-engaged starter uses the solenoid lever to push the pinion forward BEFORE the motor spins. This is quieter, more controlled, and less prone to the grinding noise you get when an inertia Bendix doesn't engage cleanly."

**PPT Content:**
```
BENDIX DRIVE & OVERRUNNING CLUTCH

PURPOSE: Engage starter pinion with flywheel ring gear,
then disengage automatically when engine starts

GEAR RATIO:
• Starter pinion: 9-11 teeth
• Ring gear: 110-130+ teeth
• Ratio: 10:1 to 15:1 → torque multiplication

OVERRUNNING CLUTCH (roller type):
• Locks in drive direction (starter → engine)
• Freewheels in overrun direction (engine → starter)
• Rollers wedge in tapered chambers when driving
• Rollers roll free when overdriven
• Prevents engine from spinning starter to destruction

TWO ENGAGEMENT TYPES:
1. INERTIA (Bendix) — pinion slides on helical thread by inertia
   • Older vehicles, some industrial
   • Can cause grinding on engagement

2. PRE-ENGAGED — solenoid pushes pinion before motor spins
   • Modern standard
   • Quieter, more controlled engagement
   • Solenoid lever mechanism
```

---

#### Slide 9: The Complete Starter Circuit
**Visual:** Full circuit diagram from battery positive → fusible link → ignition switch → neutral safety switch (automatic) or clutch switch (manual) → starter relay → solenoid S terminal → solenoid internal → motor → ground → battery negative. Each connection point numbered for voltage drop testing reference.

**Instructor Narration:**
> "Now let's trace the complete circuit. Starting from the battery positive terminal: a heavy cable goes to the starter solenoid B terminal — sometimes through a fusible link. That's the power side, and it's always live — any time the battery is connected, there's full battery voltage sitting on that B terminal. Respect that.
>
> The control side starts at the ignition switch. When you turn the key to START — or press the start button — the ignition switch sends voltage through the neutral safety switch on an automatic, or the clutch switch on a manual. This is a safety interlock — the engine won't crank unless the transmission is in Park or Neutral, or the clutch pedal is pressed. From there, the signal goes to a starter relay in the fuse box. The relay's purpose is to handle the solenoid current so the ignition switch doesn't have to carry it directly. The relay output goes to the solenoid S terminal.
>
> Every connection point in this circuit is a potential failure point. Corrosion, loose terminals, damaged wires, failed switches — any of these can prevent cranking. This is why we do voltage drop testing at every connection. We'll do exactly that in the practical session."

**PPT Content:**
```
COMPLETE STARTER CIRCUIT — TRACE THE PATH

POWER SIDE (always live when battery connected):
Battery (+) → Heavy cable → Fusible link → Solenoid B terminal
⚠ B TERMINAL IS ALWAYS HOT — disconnect battery before service

CONTROL SIDE (active only at START):
Ignition switch (START) →
  Neutral safety switch (auto) / Clutch switch (manual) →
    Starter relay (in fuse box) →
      Solenoid S terminal

INTERNAL (solenoid closed):
B terminal → Contact disc → M terminal → Motor windings →
  Brushes → Ground (housing) → Engine block → Battery (-)

VOLTAGE DROP TEST POINTS (numbered):
① Battery (+) post to cable end
② Cable end to solenoid B terminal
③ Solenoid B to solenoid M (internal contact)
④ Motor ground to engine block
⑤ Engine block to battery (-) post

Total circuit voltage drop should be < 0.5V
```

---

#### Slide 10: Starter Motor Specifications & Normal Values
**Visual:** Table showing typical starter specifications for 4-cylinder petrol, 6-cylinder petrol, and diesel engines — cranking current, free-running current, minimum cranking speed, cranking voltage.

**Instructor Narration:**
> "Before you can diagnose a fault, you need to know what normal looks like. A healthy 4-cylinder petrol engine starter draws 150 to 200 amps during cranking. A 6-cylinder draws 200 to 250. A diesel — because of higher compression — draws 250 to 350 amps, sometimes more. If you measure 400 amps on a 4-cylinder petrol, that's excessive — something is binding or the starter is failing internally.
>
> Cranking voltage — what the battery drops to during cranking — should stay above 9.6 volts for a 12-volt system. If it drops below that, your battery can't sustain the load. The engine needs to crank at about 200 RPM minimum to start. Below that, the fuel and ignition systems can't function properly.
>
> Free-running current — starter spinning with no load — should be 60 to 100 amps. If it's pulling 150 amps with no load, you've got internal friction — worn bushings, dragging armature, or a shorted winding."

**PPT Content:**
```
STARTER MOTOR — NORMAL VALUES

                    4-CYL PETROL   6-CYL PETROL   DIESEL
Cranking current:   150-200A       200-250A        250-350A
Free-running:       60-80A         60-100A         80-120A
Cranking speed:     200+ RPM       200+ RPM        200+ RPM
Cranking voltage:   >9.6V          >9.6V           >9.6V

DIAGNOSTIC THRESHOLDS:
• Current HIGHER than spec → mechanical resistance or internal fault
• Current LOWER than spec → poor connections (voltage drop)
• Cranking voltage <9.6V → weak battery or excessive draw
• Free-running current high → worn bushings, shorted windings
• Cranking speed low → weak battery, worn starter, engine issue

Always check battery FIRST before condemning the starter.
```

---

#### Slide 11: Starter Motor Failure Modes
**Visual:** Four photos showing common starter failures — (1) worn brushes at minimum length, (2) burned commutator segments, (3) damaged ring gear teeth, (4) solenoid contact disc burned/pitted.

**Instructor Narration:**
> "What goes wrong with starters? Most failures come down to four things. Worn brushes — they're the main wear item, and once they're too short, you lose contact. Burned commutator — from excessive arcing, usually caused by worn brushes or a short in the windings. Solenoid contact disc — the contact disc that bridges B to M carries hundreds of amps; over time it pits and burns, creating high resistance. And damaged ring gear teeth — if the starter doesn't engage cleanly, the teeth get chewed up. You hear a horrible grinding noise.
>
> The key point: most starter problems are actually circuit problems, not motor problems. Before you pull a starter, test the circuit. Voltage drops, relay operation, neutral safety switch, ground connections. Test first. Remove last."

**PPT Content:**
```
STARTER MOTOR — COMMON FAILURE MODES

1. WORN BRUSHES
   Symptom: Intermittent crank → slow crank → no crank
   Test: Measure brush length against spec

2. BURNED COMMUTATOR
   Symptom: Rough/uneven cranking, excessive current draw
   Test: Visual inspection, armature continuity test

3. SOLENOID CONTACT DISC
   Symptom: Click but no crank (solenoid engages, no current to motor)
   Test: Voltage at M terminal while cranking — should be >10V

4. RING GEAR DAMAGE
   Symptom: Grinding noise on engagement, starter spins but engine
   doesn't crank (missing teeth)
   Test: Visual through starter mounting hole, rotate engine

REMEMBER: Test the CIRCUIT before blaming the MOTOR
80% of "starter problems" are actually circuit problems
```

---

### **DEVELOPMENT PART 2: The Alternator — Complete Construction & Operation** (Slides 12-18, ~20 minutes)

**Narrative Voice:** Same methodical approach. Outside in, then the electrical theory of generation.

---

#### Slide 12: Alternator — External Overview & Pulley Types
**Visual:** Annotated photo of a complete alternator showing the drive pulley, front housing, rear housing, B+ output terminal, field connector, and ventilation openings. Inset comparison of three pulley types: solid, overrunning alternator pulley (OAP), and overrunning alternator decoupler (OAD).

**Instructor Narration:**
> "The alternator converts mechanical energy from the engine's drive belt into electrical energy to charge the battery and power all the vehicle's electrical systems. Let's start with the outside.
>
> At the front, the drive pulley connects to the engine via a serpentine belt. Modern alternators often use an overrunning alternator pulley — OAP — or an overrunning alternator decoupler — OAD. These have a one-way clutch built into the pulley. When the engine decelerates suddenly — like when you snap off the throttle — the alternator's rotor has inertia and wants to keep spinning. Without a decoupler, this puts enormous strain on the belt. The OAP/OAD lets the rotor freewheel during deceleration, extending belt life and reducing vibration and noise. You can test these with a special tool — if the pulley spins freely in both directions, the one-way clutch has failed and the pulley must be replaced.
>
> At the rear, you have the B+ terminal — the main output. This connects via a heavy wire to the battery positive through a fuse or fusible link. The field connector provides the control signal — either from an external voltage regulator or, on most modern vehicles, directly from the ECU."

**PPT Content:**
```
ALTERNATOR — EXTERNAL VIEW

DRIVE END (front):
• Pulley — connected to engine via serpentine belt
  - Solid pulley (older vehicles)
  - OAP (Overrunning Alternator Pulley) — one-way clutch
  - OAD (Overrunning Alternator Decoupler) — clutch + spring
  - OAP/OAD test: should lock in drive direction,
    freewheel in reverse
• Front bearing — supports rotor shaft
• Fan — internal airflow for cooling

OUTPUT END (rear):
• B+ terminal — main charging output to battery (heavy cable)
• Field connector — regulator control signal
• Rectifier cover — protects diode bridge
• Rear bearing — supports rotor shaft
• Brush holder — contains brushes contacting slip rings
```

---

#### Slide 13: Inside the Alternator — The Rotor
**Visual:** Alternator rotor removed from housing — photo and diagram showing the rotor shaft, slip rings at one end, the field winding coil visible through the claw-pole fingers, and the interlocking claw-pole halves (north and south poles).

**Instructor Narration:**
> "The rotor is the spinning part inside the alternator, and it's an electromagnet. A coil of wire — the field winding — is wrapped around an iron core. When current flows through this winding, it creates a magnetic field. Wrapped around this coil are two claw-pole halves that interlock like fingers. One half becomes north poles, the other becomes south poles. As the rotor spins, these alternating poles sweep past the stator windings and induce an alternating current.
>
> The field winding gets its current through two slip rings — smooth copper rings on the rotor shaft. Carbon brushes ride on these rings, providing the electrical connection to the stationary part of the alternator. Unlike the commutator on a starter, these slip rings are smooth and continuous — they're not switching anything, just providing a constant connection to a spinning coil.
>
> The voltage regulator controls how much current flows through the field winding. More field current means a stronger magnetic field, which means more output voltage. Less field current means less output. That's how the system maintains a steady 14 volts regardless of engine speed or electrical load. This is the key concept: the alternator doesn't regulate output directly — it regulates the input to the field winding."

**PPT Content:**
```
ALTERNATOR ROTOR — THE SPINNING ELECTROMAGNET

CONSTRUCTION:
• Iron core with field winding (coil of copper wire)
• Two claw-pole halves interlock around the coil
  - One half = North poles
  - Other half = South poles
  - Typically 6-8 pole pairs (12-16 total fingers)
• Slip rings (2) at shaft end — smooth copper rings
• Connect field winding to brushes (stationary)

HOW IT CREATES VOLTAGE:
1. Current flows through field winding via brushes/slip rings
2. Field winding creates electromagnet
3. Claw poles create alternating N-S-N-S pattern
4. Rotor spins inside stator
5. Alternating magnetic field induces AC voltage in stator

KEY CONCEPT:
Voltage regulator controls FIELD CURRENT
→ More field current = stronger magnetic field = more output
→ Less field current = weaker field = less output
→ This is how charging voltage stays at 13.8-14.8V
```

---

#### Slide 14: Inside the Alternator — The Stator
**Visual:** Photo and diagram of a stator assembly — the laminated iron ring with three sets of windings visible. Diagrams showing star (Y) connection and delta connection configurations, with the 3-phase output waveform.

**Instructor Narration:**
> "The stator is the stationary part — it sits around the rotor. It's a ring of laminated iron with slots, and three separate windings are placed in those slots. Three windings, equally spaced — that gives us a 3-phase AC output. Just like a power station. Three phases are more efficient than a single phase because the power delivery is smoother — there's always at least one phase near its peak output.
>
> The three windings can be connected in two ways. Star connection — also called Y connection — joins one end of each winding to a common neutral point. This gives you higher voltage at low RPM, which means better charging at idle. Delta connection connects the windings in a triangle. This gives you higher current output at high RPM. Most passenger car alternators use star connection. Some high-output alternators for vehicles with heavy electrical loads use delta.
>
> The output from the stator is AC — alternating current. But your car runs on DC. That's where the diode bridge comes in."

**PPT Content:**
```
ALTERNATOR STATOR — THE 3-PHASE GENERATOR

CONSTRUCTION:
• Laminated iron ring (reduces eddy currents)
• Three separate windings placed 120° apart in slots
• Produces 3-PHASE AC output

WINDING CONFIGURATIONS:
STAR (Y) CONNECTION:
• One end of each winding joined at neutral point
• Better voltage output at LOW RPM (idle)
• Most common in passenger vehicles

DELTA CONNECTION:
• Windings connected end-to-end in triangle
• Higher current output at HIGH RPM
• Used in high-output alternators (heavy electrical loads)

3-PHASE ADVANTAGE:
• Smoother power delivery than single phase
• At least one phase always near peak output
• Higher total power for given alternator size

Output is AC — must be rectified to DC for vehicle use
```

---

#### Slide 15: The Diode Rectifier Bridge
**Visual:** Diagram of a 6-diode full-wave rectifier bridge — three positive diodes mounted in positive heat sink, three negative diodes mounted in negative heat sink. 3-phase AC input waveform on the left, rectified DC output waveform on the right. Bonus: diagram showing a failed diode and the resulting AC ripple visible on the DC output.

**Instructor Narration:**
> "The rectifier bridge converts the 3-phase AC from the stator into DC for the vehicle. It uses six diodes — two for each phase. Three diodes are mounted in the positive heat sink and connect to the B+ output. Three are mounted in the negative heat sink and connect to ground. A diode is a one-way valve for electricity — it only allows current to flow in one direction.
>
> Here's the beauty of full-wave rectification with three phases. Each phase contributes during its positive half AND its negative half. The result is a DC output with very little ripple — almost perfectly smooth.
>
> Now, what happens when one diode fails? A diode can fail open or fail shorted. If it fails open, you lose one path of rectification. The output drops by about one-third, and a noticeable AC ripple appears on the DC output. If it fails shorted, it creates a direct path that can overheat the stator winding and cause further damage.
>
> This is why AC ripple testing is part of your professional test sequence. A healthy alternator shows less than 0.5 volts AC ripple on the DC output. A failed diode shows 1 volt or more of AC ripple. You can catch a failing alternator BEFORE the customer gets stranded — just by checking AC ripple."

**PPT Content:**
```
DIODE RECTIFIER BRIDGE — AC TO DC CONVERSION

6 DIODES — FULL-WAVE RECTIFICATION:
• 3 positive diodes → mounted in + heat sink → B+ output
• 3 negative diodes → mounted in - heat sink → ground
• Each diode = one-way valve for current

HOW IT WORKS:
Each phase passes through 2 diodes:
  Positive half-cycle → through positive diode to B+
  Negative half-cycle → through negative diode from ground
Result: Nearly smooth DC output

WHEN A DIODE FAILS:
Open circuit:
  → Output drops ~33%
  → AC ripple appears on DC output (1V+ AC)
  → Battery warning light may illuminate

Short circuit:
  → Stator winding overheats
  → Alternator may burn out completely
  → Possible blown fuse on B+ line

DIAGNOSTIC KEY:
AC ripple test on B+ output:
  < 0.5V AC = healthy
  > 0.5V AC = diode failure — replace rectifier or alternator
```

---

#### Slide 16: Voltage Regulator — Internal & ECU-Controlled
**Visual:** Two diagrams side by side: (1) traditional internal voltage regulator integrated into brush holder assembly, with simple control schematic showing field current switching, (2) modern ECU-controlled alternator with LIN/PWM signal from engine management ECU to field driver transistor.

**Instructor Narration:**
> "The voltage regulator keeps the charging voltage in the sweet spot — 13.8 to 14.8 volts regardless of engine speed or electrical load. In a traditional internal regulator, a solid-state circuit constantly monitors the B+ output voltage. When it drops below the setpoint, the regulator increases field current. When it rises above, it reduces field current. It's switching the field winding on and off many times per second — pulse-width modulation.
>
> Modern vehicles have moved to ECU-controlled charging. The engine management or body control module sends a PWM signal — often over a LIN bus — to a field driver transistor in the alternator. This allows the ECU to implement smart charging strategies. For example, during braking and deceleration, the ECU increases alternator output to capture regenerative energy. During acceleration, it reduces output to lessen engine load and improve fuel economy. Some systems even vary the setpoint based on battery temperature — higher voltage in cold weather when the battery is less efficient.
>
> This is why you might see a perfectly healthy alternator putting out only 12.8 volts during a road test. The ECU has intentionally reduced the charge rate to save fuel. You need to understand the system before you condemn the component."

**PPT Content:**
```
VOLTAGE REGULATOR

TRADITIONAL INTERNAL REGULATOR:
• Solid-state circuit integrated into brush holder
• Monitors B+ voltage continuously
• PWM switches field current on/off (many times per second)
• More field current = more output voltage
• Less field current = less output voltage
• Setpoint: 13.8-14.8V (temperature compensated)

ECU-CONTROLLED ALTERNATOR (modern):
• ECU sends PWM/LIN signal to field driver in alternator
• ECU controls charging strategy:
  - Deceleration → increase output (regen energy capture)
  - Acceleration → decrease output (reduce engine load)
  - Cold weather → higher setpoint (battery less efficient)
  - Battery fully charged → reduce to float voltage
• CAN/LIN communication with alternator

⚠ DIAGNOSTIC CAUTION:
ECU-controlled alternator may intentionally output <14V
Check OBD data for alternator command % before condemning
```

---

#### Slide 17: The Complete Charging Circuit
**Visual:** Full circuit diagram: battery → alternator B+ terminal → alternator internal (rotor, stator, diodes, regulator) → back to battery. Including the charge warning light circuit — light connected between ignition feed and alternator L terminal; light illuminates when no alternator output, extinguishes when alternator output matches ignition voltage.

**Instructor Narration:**
> "Let's trace the complete charging circuit. The alternator B+ terminal connects via a heavy wire — often through a fusible link — directly to the battery positive. That's the output path. Current flows from the alternator into the battery and to all the vehicle's electrical consumers.
>
> The charge warning light on the dashboard is part of the circuit. It connects between the ignition feed and the alternator's L terminal. When the engine is off and ignition is on, there's voltage on the ignition side but not on the alternator side — the light illuminates. When the alternator is producing voltage, both sides are equal — the light goes out. If the alternator fails while driving, the alternator side loses voltage and the light comes on again.
>
> Interestingly, the warning light also serves a critical function during starting: it provides the initial excitation current to the field winding. Without this initial current, the alternator can't start generating. This is why a burned-out dashboard bulb can prevent the alternator from charging — no initial excitation. On modern vehicles with LEDs and ECU control, this is handled electronically."

**PPT Content:**
```
COMPLETE CHARGING CIRCUIT

OUTPUT PATH:
Alternator B+ → Fusible link/fuse → Battery positive
(also supplies all vehicle electrical loads)

FIELD EXCITATION:
Ignition ON → Warning light → L terminal → Field winding →
Regulator → Ground

CHARGE WARNING LIGHT OPERATION:
Engine OFF, ignition ON:
  Ignition voltage on one side, no alternator voltage on other
  → LIGHT ON (voltage difference across bulb)

Engine running, alternator charging:
  Equal voltage on both sides
  → LIGHT OFF (no voltage difference)

Alternator fails while driving:
  → LIGHT ON (voltage difference returns)

⚠ CRITICAL: Warning light provides initial field excitation
Burned-out bulb can prevent alternator from charging
(older systems with bulb excitation)
```

---

#### Slide 18: Alternator Failure Modes & Diagnostic Clues
**Visual:** Summary table of alternator failures — diode failure (AC ripple), regulator failure (over/undercharge), bearing failure (noise), brush wear (intermittent charging), belt/pulley issues (squealing, intermittent).

**Instructor Narration:**
> "What goes wrong with alternators? Diode failure — you'll catch it with AC ripple testing. Voltage regulator failure — shows as overcharging above 15 volts, which boils the battery, or undercharging below 13 volts, which slowly drains it. Bearing failure — you'll hear it before you measure it. Grinding or whining noise that varies with engine RPM. Brush wear — similar to starter brushes, but carrying much less current. Intermittent charging, flickering dash light. Belt or pulley issues — a slipping belt squeals under load, and a failed decoupler pulley causes belt flutter.
>
> Overcharging is particularly dangerous. Voltage above 15 volts creates excessive gassing in the battery — hydrogen gas. It can damage electronic modules designed for 14 volts. And it can shorten the life of every bulb in the car. If a customer says their headlight bulbs keep blowing, check the charging voltage."

**PPT Content:**
```
ALTERNATOR — FAILURE MODES & SYMPTOMS

DIODE FAILURE:
  Symptom: Reduced output, AC ripple >0.5V, possible battery drain
  Test: AC voltage on DC output (set meter to AC)

REGULATOR FAILURE — OVERCHARGE:
  Symptom: Voltage >15V, battery gassing/smell, bulbs blowing
  Test: Voltmeter at battery with engine running
  ⚠ DANGEROUS — can damage ECUs, boil battery

REGULATOR FAILURE — UNDERCHARGE:
  Symptom: Voltage <13.5V, battery slowly drains, warning light
  Test: Voltmeter at battery with engine running + load

BEARING FAILURE:
  Symptom: Grinding/whining noise varying with RPM
  Test: Stethoscope, remove belt and spin by hand

BRUSH WEAR:
  Symptom: Intermittent charging, flickering warning light
  Test: Measure brush length, check slip ring condition

BELT/PULLEY:
  Symptom: Squealing under load, belt flutter
  Test: Inspect belt condition, test OAP/OAD with special tool
```

---

### **PRACTICAL: Disassembly & Professional Test Sequence** (Slides 19-25, ~95 minutes)

**Narrative Voice:** Workshop leader. Clear instructions, safety emphasis, step-by-step guidance.

---

#### Slide 19: Practical Overview — Four Stations
**Visual:** Workshop floor plan showing four stations laid out: Station 1 (bench with starter motor, tools, and ID worksheet), Station 2 (bench with alternator, tools, and ID worksheet), Station 3 (vehicle with multimeter, clamp meter, and test checklist), Station 4 (vehicle with multimeter for voltage drop testing). Rotation arrows showing learner flow.

**Instructor Narration:**
> "Here's how the practical works. Four stations, rotating in pairs. Station 1: starter motor disassembly — take it apart, identify every component on your worksheet, reassemble. Station 2: alternator disassembly — same process. Station 3: the complete vehicle test sequence — battery SOH, cranking voltage, starter current draw, alternator output, AC ripple, and parasitic drain. Station 4: voltage drop testing across the entire starter circuit. Each station is 20 to 25 minutes. I'll circulate and check your work. Let's get to it."

**PPT Content:**
```
PRACTICAL SESSION — FOUR STATIONS (Rotate in pairs)

STATION 1: Starter Motor Disassembly (20 min)
  → Disassemble, identify all components, complete worksheet
  → Armature, commutator, brushes, field coils/magnets,
    solenoid, Bendix drive

STATION 2: Alternator Disassembly (20 min)
  → Disassemble, identify all components, complete worksheet
  → Rotor, stator, diode bridge, regulator, brushes,
    slip rings, pulley

STATION 3: Complete Vehicle Test Sequence (25 min)
  → Battery SOH → Cranking voltage → Starter current draw
  → Alternator output voltage → AC ripple → Parasitic drain

STATION 4: Voltage Drop Testing — Starter Circuit (20 min)
  → Battery post → cable → solenoid B → solenoid M
  → Ground path → battery negative

⚠ Safety: Disconnect battery before disassembly.
  Reconnect ONLY for vehicle testing under supervision.
```

---

#### Slide 20: Station 1 — Starter Motor Disassembly Guide
**Visual:** Step-by-step photo sequence: (1) remove through-bolts, (2) separate drive end housing, (3) remove armature from field housing, (4) inspect brushes and brush holder, (5) separate solenoid from housing, (6) remove Bendix drive from armature shaft with snap ring.

**Instructor Narration:**
> "Station 1. The starter motor is on the bench, already removed from the vehicle. Your job is to disassemble it following the steps on your worksheet. Remove the through-bolts — usually two long bolts that hold the end frames to the housing. Slide the drive end off carefully. Extract the armature. Now inspect the brushes — note the length, check the springs. Remove the solenoid — usually two or three screws. The Bendix drive comes off the armature shaft — there's a snap ring or clip holding it. Be careful not to lose it.
>
> As you identify each component, mark it on your worksheet. Measure the brush length with calipers and record it. Check the commutator for scoring. Spin the Bendix — it should lock in one direction and freewheel in the other. Reassemble in reverse order when done."

**PPT Content:**
```
STATION 1: STARTER MOTOR DISASSEMBLY

PROCEDURE:
1. Note orientation before disassembly (mark housing to end caps)
2. Remove through-bolts (2 long bolts)
3. Separate drive end housing
4. Withdraw armature from field housing
5. Inspect brushes — measure length with calipers
6. Remove solenoid (2-3 mounting screws)
7. Remove Bendix from shaft (snap ring/clip)

IDENTIFY & RECORD:
□ Armature (laminated core + windings)
□ Commutator (copper segments, mica insulation)
□ Brushes (carbon blocks — measure length: ___mm)
□ Brush springs (check tension)
□ Field coils OR permanent magnets (note which type)
□ Solenoid (pull-in & hold-in windings visible through casing)
□ Bendix drive (pinion gear + overrunning clutch)
□ Test overrunning clutch: locks one way, freewheels other ✓/✗

REASSEMBLE when complete. All parts accounted for.
```

---

#### Slide 21: Station 2 — Alternator Disassembly Guide
**Visual:** Step-by-step photo sequence: (1) remove pulley using impact or holding tool, (2) remove through-bolts and separate halves, (3) extract rotor, (4) inspect stator windings, (5) examine diode rectifier plate, (6) remove brush holder/regulator assembly, (7) inspect slip rings.

**Instructor Narration:**
> "Station 2. The alternator disassembly. Start by removing the pulley — you'll need either an impact gun or the specific holding tool for OAP/OAD pulleys. Never use the rotor as a vice — you'll damage the bearings. Remove the through-bolts and carefully separate the front and rear halves. The rotor comes out with the front half. The stator and diode bridge stay in the rear half.
>
> Examine the rotor. Note the claw poles — count them. Look at the slip rings — they should be smooth and shiny, not grooved or blackened. Check the brushes in the brush holder — measure their length. Examine the stator windings for discolouration, which indicates overheating. Look at the diode rectifier — any signs of heat damage or cracked solder joints. Note the regulator type — integrated with the brush holder, or separate.
>
> Record everything on your worksheet. This is the last time you'll see these components in isolation — from now on, you'll be diagnosing them while they're still in the car."

**PPT Content:**
```
STATION 2: ALTERNATOR DISASSEMBLY

PROCEDURE:
1. Remove pulley (impact tool or specific holding tool)
   ⚠ Never clamp rotor in vice — damages bearings
2. Remove through-bolts (3-4 long bolts)
3. Separate front housing (with rotor) from rear housing
4. Extract rotor from front bearing
5. Examine stator in rear housing
6. Remove brush holder / regulator assembly
7. Examine diode rectifier plate

IDENTIFY & RECORD:
□ Rotor — count claw poles: ___ pairs
□ Slip rings — condition: smooth / grooved / burned
□ Field winding (inside claw poles)
□ Stator — winding configuration: Star / Delta
□ Stator condition: clean / discoloured (overheating)
□ Diode rectifier bridge — count diodes: ___ (should be 6+)
□ Voltage regulator — type: internal / separate
□ Brushes — measure length: ___mm
□ Bearings — spin by hand, check for roughness/noise
□ Pulley type: solid / OAP / OAD

REASSEMBLE when complete.
```

---

#### Slide 22: Station 3 — Complete Vehicle Test Sequence
**Visual:** Flowchart showing the professional test sequence: Step 1 Battery SOH → Step 2 Cranking Voltage → Step 3 Starter Current Draw → Step 4 Alternator Output Voltage → Step 5 AC Ripple Test → Step 6 Parasitic Drain Test. Each step shows the meter setup, connection points, and pass/fail values.

**Instructor Narration:**
> "Station 3 is the money station. This is the test sequence you'll use on every starting and charging complaint for the rest of your career. Six tests, in order. Each one builds on the last. Skip a step, and you'll misdiagnose the problem.
>
> Step 1: Battery state of health. Use the battery tester — electronic conductance test or load test. A bad battery makes everything else look bad. Step 2: Cranking voltage. Connect your meter to the battery terminals and crank the engine. Watch the minimum voltage — it must stay above 9.6 volts. Step 3: Starter current draw. Clamp your amp clamp around the battery positive cable. Crank the engine. Read the peak current — compare to specification. Step 4: Start the engine. Read battery voltage — should be 13.8 to 14.8 volts. Step 5: Switch your meter to AC volts. With the engine running, read AC ripple at the battery — should be under 0.5 volts. Over 0.5 means a diode is failing. Step 6: Parasitic drain. Turn everything off, close all doors, connect your meter in series with the battery negative cable, wait 30 minutes for modules to go to sleep, read the drain — should be under 50 milliamps."

**PPT Content:**
```
STATION 3: PROFESSIONAL TEST SEQUENCE

STEP 1 — BATTERY SOH:
  Tool: Electronic battery tester / conductance tester
  Result: GOOD / MARGINAL / REPLACE
  → If REPLACE: stop. Fix battery first.

STEP 2 — CRANKING VOLTAGE:
  Tool: Voltmeter across battery terminals
  Action: Crank engine (disable ignition to prevent start if needed)
  PASS: Minimum voltage > 9.6V
  FAIL: <9.6V → weak battery or excessive starter draw

STEP 3 — STARTER CURRENT DRAW:
  Tool: Inductive amp clamp on battery positive cable
  Action: Crank engine
  PASS: 150-300A typical (check vehicle spec)
  FAIL: Excessive = internal fault; Low = poor connections

STEP 4 — ALTERNATOR OUTPUT VOLTAGE:
  Tool: Voltmeter across battery terminals, engine running
  PASS: 13.8V - 14.8V (may vary with ECU-controlled systems)
  FAIL: <13.5V = undercharge; >15.0V = overcharge

STEP 5 — AC RIPPLE TEST:
  Tool: Voltmeter set to AC, across battery terminals, engine running
  PASS: < 0.5V AC
  FAIL: > 0.5V AC = diode failure in alternator

STEP 6 — PARASITIC DRAIN:
  Tool: Ammeter in series with battery negative cable
  Wait: 30 minutes for modules to sleep
  PASS: < 50 mA
  FAIL: > 50 mA → pull fuses one at a time to isolate circuit
```

---

#### Slide 23: Station 4 — Voltage Drop Testing
**Visual:** Diagram of the starter circuit with a voltmeter shown connected across each test point. Color-coded: green connections = acceptable drop (<0.2V), red connections = excessive drop (>0.5V). Includes both positive side and ground side testing.

**Instructor Narration:**
> "Station 4. Voltage drop testing is THE diagnostic technique for high-current circuits. Here's the principle: you're measuring the voltage lost across each connection and cable while current is flowing. You can't find a bad connection by measuring resistance with the circuit off — the resistance might be only 0.1 ohms, which your meter shows as zero. But at 200 amps, that 0.1 ohms drops 20 volts. You need current flowing to see the problem.
>
> Connect your voltmeter across each connection point — battery post to cable end, cable end to solenoid B terminal, solenoid B to M terminal internally, then the ground side: motor housing to engine block, engine block to battery negative post. While your partner cranks the engine, read the voltage across each point. Each connection should show less than 0.2 volts. The total positive side should be under 0.5 volts. The total ground side should be under 0.3 volts.
>
> If you find a connection dropping 1 volt or more, you've found your problem. Clean it, tighten it, replace it. This test alone will solve more no-crank and slow-crank complaints than any other single technique."

**PPT Content:**
```
STATION 4: VOLTAGE DROP TESTING — STARTER CIRCUIT

PRINCIPLE: Measure voltage LOST across each connection
           while CURRENT IS FLOWING (during cranking)

POSITIVE SIDE TESTS (meter positive lead upstream, negative downstream):
① Battery (+) post to cable clamp: < 0.2V
② Cable to solenoid B terminal: < 0.2V
③ Solenoid B to M terminal: < 0.2V (internal contact)
④ Total positive side: < 0.5V

GROUND SIDE TESTS (meter positive lead downstream, negative upstream):
⑤ Starter housing to engine block: < 0.2V
⑥ Engine block to battery (-) cable: < 0.2V
⑦ Battery (-) cable to battery post: < 0.2V
⑧ Total ground side: < 0.3V

HOW TO TEST:
1. Connect voltmeter across the connection being tested
2. Have partner crank engine (brief cranking only)
3. Read voltage during cranking
4. Move to next connection point
5. Record all readings

HIGH READING = HIGH RESISTANCE = FOUND YOUR PROBLEM
Clean, tighten, or replace the faulty connection
```

---

#### Slide 24: Parasitic Drain Isolation — Pulling Fuses
**Visual:** Photo of a fuse box with an ammeter in series with battery cable, and a fuse being pulled. Decision flowchart: drain >50mA → pull fuse 1 → reading drops? → YES: circuit identified → trace that circuit. NO: replace fuse, pull next.

**Instructor Narration:**
> "When your parasitic drain test shows more than 50 milliamps after the sleep period, you need to find the circuit that's drawing the current. The technique is simple but requires patience. With your ammeter still in series, start pulling fuses one at a time. When you pull a fuse and the reading drops significantly, you've identified the circuit. Now look at the fuse chart — what does that fuse supply? Interior lights? Radio? A specific module?
>
> Common culprits: a boot light that stays on because the boot switch is misadjusted. A glove box light that stays on because the latch is worn. An aftermarket stereo with a constant live feed wired incorrectly. A failing control module that never goes to sleep.
>
> Two critical rules. First: wait the full 30 minutes before testing. Modern vehicles have dozens of modules that need time to enter sleep mode. Testing too early gives false readings. Second: don't break the circuit to insert your meter — use a switch tool or a fuse adapter that lets you insert the meter without disconnecting the battery, because disconnecting and reconnecting wakes up all the modules and resets your timer."

**PPT Content:**
```
PARASITIC DRAIN ISOLATION

WHEN DRAIN > 50 mA:

PROCEDURE:
1. Ammeter in series with battery negative (use bypass switch tool)
2. All doors closed, key out, wait 30 MINUTES minimum
3. Read total parasitic drain
4. If > 50 mA: begin fuse isolation

FUSE PULL SEQUENCE:
→ Pull one fuse at a time
→ Note ammeter reading change
→ If significant drop: that circuit is the source
→ Identify circuit from fuse chart
→ Trace and inspect components on that circuit
→ Replace fuse before pulling next one

COMMON PARASITIC DRAIN SOURCES:
• Boot/trunk light (switch misadjusted)
• Glove box light (latch worn)
• Aftermarket accessories wired to constant power
• Failing module not entering sleep mode
• Relay stuck closed (clicking test — listen with engine off)

⚠ DO NOT disconnect battery to insert meter
   → Use bypass tool or fuse adapter
   → Disconnecting resets all module sleep timers
```

---

#### Slide 25: Systematic Fault Isolation Flowcharts
**Visual:** Four diagnostic flowcharts in quadrants — (1) Slow Crank: Battery OK? → YES: Voltage drop test → High drop? → Fix connection / Low drop? → Starter draw test → High draw? → Starter fault / Engine mechanical. (2) No Crank: Relay clicking? → Check neutral switch, relay, solenoid, motor. (3) Undercharge: Belt OK? → Regulator? → Wiring? → Diode? (4) Overcharge: Regulator failure → check regulator → ECU command?

**Instructor Narration:**
> "Here are your four diagnostic flowcharts. These are systematic — follow the steps, and you'll find the fault every time.
>
> Slow crank. First, is the battery good? Test SOH and cranking voltage. If the battery is good, do voltage drop testing across the circuit. A corroded cable connection or ground strap will cause slow cranking even with a perfect battery and starter. If voltage drops are clean, check starter current draw — excessive draw means the starter itself has an internal problem, or the engine has a mechanical issue making it hard to turn.
>
> No crank. Nothing happens when you turn the key. Start at the switches. Does the dash illuminate? Is the neutral safety switch or clutch switch functioning? Can you hear the relay click in the fuse box? If the relay clicks, move to the solenoid — can you hear or feel the solenoid engage? If the solenoid engages but the motor doesn't spin, the solenoid contact disc is probably burned, or the motor has failed.
>
> Undercharge. Belt slipping or broken? Check tension and condition. Belt OK? Check alternator output voltage and AC ripple. Low output with normal ripple points to the regulator. Normal output at the alternator but low at the battery points to wiring or connection issues.
>
> Overcharge. Almost always a regulator failure. On ECU-controlled systems, check the ECU command signal before replacing the alternator — the ECU might be commanding high output due to a faulty battery temperature sensor."

**PPT Content:**
```
SYSTEMATIC FAULT ISOLATION

SLOW CRANK:
Battery SOH → OK? →
  Voltage drop test → Excessive? → Fix connection
  Normal drops → Starter current draw → High? → Starter/engine fault
  Low current → Poor connections (voltage drop missed)

NO CRANK (nothing happens):
Dash lights ON? → YES → Neutral/clutch switch OK? →
  Relay clicking? → YES → Solenoid engaging? →
    YES → Motor fault (brushes, commutator, windings)
    NO → Solenoid fault or B terminal connection
  NO → Relay fault or control circuit open
NO dash lights → Battery disconnected / main fuse blown

UNDERCHARGE (<13.5V):
Belt condition/tension → OK? →
  Alternator B+ voltage → Low? → Check regulator, field circuit
  Normal at alternator → Wiring/connection to battery
  AC ripple >0.5V → Diode failure

OVERCHARGE (>15.0V):
Regulator failure → Check/replace regulator
ECU-controlled? → Check ECU command signal
  → Faulty battery temp sensor can command overcharge
```

---

### **WRAP-UP: Consolidation & Preview** (Slides 26-28, ~15 minutes)

---

#### Slide 26: The Professional Test Sequence — One Page Summary
**Visual:** Clean, printable one-page summary card of the complete 6-step test sequence with pass/fail values. Formatted as a wallet reference card.

**Instructor Narration:**
> "This is your reference card. Six tests, in order, every time. Battery SOH first — always. Then cranking voltage, starter draw, alternator output, AC ripple, and parasitic drain. Print this, laminate it, keep it in your toolbox. After you've done it a hundred times, you won't need the card anymore. But until then, follow the sequence. It's the difference between guessing and knowing."

**PPT Content:**
```
STARTING & CHARGING — PROFESSIONAL TEST CARD

1. BATTERY SOH           Tool: Electronic tester
   PASS: Good / Serviceable    FAIL: Replace

2. CRANKING VOLTAGE       Tool: Voltmeter at battery
   PASS: > 9.6V               FAIL: < 9.6V

3. STARTER CURRENT DRAW   Tool: Amp clamp on B+ cable
   PASS: 150-300A (per spec)   FAIL: Outside range

4. ALTERNATOR OUTPUT      Tool: Voltmeter at battery, running
   PASS: 13.8 - 14.8V         FAIL: Outside range

5. AC RIPPLE              Tool: AC voltmeter at battery, running
   PASS: < 0.5V AC            FAIL: > 0.5V AC

6. PARASITIC DRAIN        Tool: Ammeter in series, all off
   PASS: < 50 mA (after 30 min) FAIL: > 50 mA

TEST IN ORDER. ALWAYS START WITH BATTERY.
```

---

#### Slide 27: What You Learned Today
**Visual:** Checklist with tick marks, organized by theory and practical competencies.

**Instructor Narration:**
> "Let's take stock. This morning, you knew the starter cranks the engine and the alternator charges the battery. Now you can identify every internal component of both. You can trace the complete starter circuit from battery to ground and name every connection point. You understand how the solenoid's two windings work and why the Bendix freewheels. You know how three-phase AC becomes DC through six diodes and why a failed diode shows up as AC ripple. And most importantly, you've run a professional test sequence on a real vehicle and performed voltage drop testing on a real starter circuit.
>
> Tomorrow we finish Week 6 with driveline integration — how the engine, transmission, and all the supporting systems work together as a complete powertrain. Then Week 7 takes us into the future: hybrid, EV, and advanced vehicle systems."

**PPT Content:**
```
DAY 29 RECAP — YOU CAN NOW:

THEORY:
✅ Identify every component inside a starter motor
✅ Explain pull-in vs. hold-in solenoid windings
✅ Describe Bendix drive engagement and overrunning clutch
✅ Trace the complete starter circuit (power + control)
✅ Identify every component inside an alternator
✅ Explain 3-phase generation and 6-diode rectification
✅ Describe voltage regulation (internal and ECU-controlled)

PRACTICAL:
✅ Disassemble and reassemble a starter motor
✅ Disassemble and reassemble an alternator
✅ Perform complete 6-step starting & charging test sequence
✅ Execute voltage drop testing across starter circuit
✅ Isolate parasitic drain by fuse pulling
✅ Apply systematic fault isolation flowcharts

TOMORROW: Driveline Integration — The Complete Powertrain
```

---

#### Slide 28: Day 30 Preview & Preparation
**Visual:** Image of a complete drivetrain laid out on a workshop floor — engine, transmission, driveshaft, differential, axles — connected as a chain from front to rear.

**Instructor Narration:**
> "Day 30 is driveline integration day. We bring together everything from this week — transmission, clutch, differential, starting, charging — and look at how the complete powertrain functions as a system. We'll cover driveline vibration diagnosis, NVH basics, and the pre-delivery inspection sequence that ties every system together. Come ready to think about the whole car, not just individual components. See you tomorrow."

**PPT Content:**
```
DAY 30 PREVIEW: DRIVELINE INTEGRATION

• Complete powertrain as a system
  — Engine → Transmission → Driveshaft → Differential → Wheels
• Driveline vibration diagnosis
• NVH (Noise, Vibration, Harshness) basics
• Pre-delivery inspection: the complete vehicle check

Prepare:
• Review Week 6 notes (transmission, clutch, starting, charging)
• Bring your professional test card from today
• Wear workshop clothing — we'll be under the car again
```

---

## Assessment Checkpoint

**Formative (not graded):**
- Component identification during disassembly — correctly identify and name all starter and alternator components on the worksheet (minimum 8/10 per unit)
- Vehicle test sequence — complete all 6 tests and record values within 10% of instructor baseline readings
- Voltage drop testing — correctly identify which connection point has excessive voltage drop in a prepared fault vehicle (if available)
- Fault isolation — given a symptom description (slow crank, no crank, undercharge, overcharge), correctly trace the diagnostic flowchart to the most likely root cause

---

## Key Takeaways

1. The starter motor is a series-wound DC motor with a solenoid that provides both gear engagement and heavy current switching — two functions in one device
2. The solenoid's pull-in winding self-cancels once the contact disc closes, leaving only the hold-in winding energised — this explains chattering with a weak battery
3. The overrunning clutch in the Bendix drive prevents the engine from destroying the starter after ignition — it must lock in one direction and freewheel in the other
4. The alternator generates 3-phase AC and rectifies it to DC through a 6-diode bridge — a single diode failure reduces output by one-third and creates measurable AC ripple
5. The voltage regulator controls the alternator by varying field current, not by restricting output — modern ECU-controlled systems vary the setpoint for fuel economy
6. The professional test sequence is: Battery SOH first, then cranking voltage, starter draw, alternator output, AC ripple, parasitic drain — always in this order
7. Voltage drop testing under load is the definitive method for finding high-resistance connections that cause slow crank, no crank, and undercharge conditions

---

## Preparation for Day 30

**Instructor prep:**
- Prepare a complete vehicle for driveline inspection (on lift, running condition)
- Gather NVH diagnostic tools — stethoscope, vibration meter if available
- Prepare pre-delivery inspection checklist forms
- Review Week 6 integration points across all four days (transmission, clutch, differential, starting/charging)
- Have starter and alternator test results from today available for comparison discussion

**Learner prep:**
- Review Week 6 notes covering all powertrain components
- Bring the professional test card from Day 29
- Wear workshop-appropriate clothing
- Review the 8 major vehicle systems from Day 1 — Day 30 ties them all together
