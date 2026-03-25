---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 7
week_title: "The Future — EV, HVAC & Safety"
day_number: 34
session_title: "Vehicle Safety Systems & ADAS"
duration_minutes: 180
theory_practice: "50:50"
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 34: Vehicle Safety Systems & ADAS
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (90 min theory + 90 min practical)
**Approach:** Dual-Lens — Passive Safety (survive the crash) + Active Safety (prevent the crash)
**PPT Target:** 27-28 slides
**Week:** 7 of 8 — "The Future — EV, HVAC & Safety"

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Name and describe the function of all passive safety systems (airbags, seatbelts with pretensioners, crumple zones, safety cell)
- Explain the deployment sequence of an airbag system from crash sensor to inflation
- Identify the clock spring and explain its role and common failure symptoms
- Distinguish between active safety and passive safety with clear examples
- Name the five core ADAS systems (AEB, LKA, ACC, BSM, RCTA) and describe how each works
- Identify and describe the four ADAS sensor types (radar, lidar, ultrasonic, camera) and their operating principles
- Explain the difference between static and dynamic ADAS sensor calibration
- List the circumstances that mandate ADAS recalibration and the consequences of skipping it

**Week 7 context:** Days 31-33 covered electric vehicles, high-voltage safety, and HVAC systems. Day 34 shifts focus to the systems that protect and assist the driver. This session bridges the mechanical world (pyrotechnic devices, structural engineering) with the sensor-driven electronic world (radar, cameras, software). It is one of the most commercially relevant sessions — ADAS calibration is a growing revenue stream for workshops, and airbag system diagnosis is a daily task.

---

## Connection to Prior Knowledge

Build from:
- **Day 2:** Workshop safety and PPE — airbags are explosive devices requiring safe handling procedures
- **Day 9-12:** Electrical fundamentals — crash sensors, squib circuits, and CAN bus communication
- **Day 24:** Brakes and ESC — ESC is the foundation of all electronic stability-based ADAS functions
- **Day 31-33:** EV and HV safety — understanding high-voltage disconnect in a crash, and how ADAS systems apply to EVs identically

**Bridge:** "For the last three days, we've been working with the future of powertrains — electric vehicles. Today we stay in the future, but we change focus. Instead of how the car moves, we look at how the car protects you and how it tries to prevent the accident from happening in the first place. Two completely different philosophies of safety, both essential, both part of every modern vehicle you will service."

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: Two Philosophies of Safety** (Slides 1-3, ~10 minutes)

**Narrative Voice:** Direct, slightly serious. Safety systems are life-and-death technology. Set the tone accordingly.

---

#### Slide 1: Title & Session Context
**Visual:** Split-screen image — left half shows a frontal crash test with airbags deployed, right half shows an ADAS-equipped car with sensor overlay visualisation (radar cones, camera field of view) avoiding a pedestrian

**Instructor Narration:**
> "Today we talk about the systems that save lives. Not the engine, not the transmission — the systems that determine whether the driver and passengers walk away from an accident, or whether the accident happens at all. This is arguably the most important technology in the entire car."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 7: The Future — EV, HVAC & Safety
Day 34: Vehicle Safety Systems & ADAS

Two approaches. One goal: nobody gets hurt.
```

---

#### Slide 2: The Two Philosophies
**Visual:** Diagram with two columns — "Passive Safety" (shield icon, activated DURING a crash) and "Active Safety" (eye icon, activated BEFORE a crash), with a timeline arrow showing pre-crash, crash, and post-crash phases

**Instructor Narration:**
> "There are two completely different approaches to vehicle safety, and every modern car uses both. Passive safety is designed to protect you DURING a crash. Airbags, seatbelts, crumple zones — they don't prevent the accident, they minimise the injury when it happens. Active safety tries to prevent the crash entirely — or at least reduce its severity. Electronic Stability Control, Automatic Emergency Braking, Lane Keep Assist — these systems intervene before impact.
>
> Think of it this way: passive safety is the helmet; active safety is the guardrail. You want both. A car with only airbags and no AEB still crashes. A car with AEB but no airbags is unprotected when the system can't prevent the impact. Modern safety engineering combines both."

**PPT Content:**
```
TWO PHILOSOPHIES OF VEHICLE SAFETY

PASSIVE SAFETY — "Survive the crash"
  Activated: DURING the impact
  Goal: Minimise injury severity
  Examples: Airbags, seatbelts, crumple zones, safety cell

ACTIVE SAFETY / ADAS — "Prevent the crash"
  Activated: BEFORE the impact
  Goal: Avoid collision or reduce impact speed
  Examples: AEB, LKA, ACC, ESC, blind spot monitoring

Modern vehicles combine BOTH approaches
Every crash avoided = passive safety never tested
Every passive system = admission that active safety has limits
```

---

#### Slide 3: Today's Plan
**Visual:** Horizontal timeline with four blocks — Setup, Passive Safety, Active Safety/ADAS, Practical

**Instructor Narration:**
> "Here's how we'll spend the next three hours. First, passive safety — the crash survival systems. Airbags, seatbelts, structural design. Then, active safety and ADAS — the crash prevention systems. Sensors, cameras, calibration. After the theory, we go hands-on: locate every safety component on a real vehicle, scan for airbag DTCs, and examine a calibration setup. Let's start with what happens when the crash has already begun."

**PPT Content:**
```
TODAY'S PLAN (180 minutes)

BLOCK 1 (30 min): Passive Safety Systems
  — Airbags, seatbelts, crumple zones, safety cell

BLOCK 2 (35 min): Active Safety & ADAS
  — AEB, LKA, ACC, sensors, calibration

BLOCK 3 (75 min): Practical Workshop
  — Component identification, scan tool diagnostics,
    calibration awareness

BLOCK 4 (15 min): Wrap-up & Day 35 preview

+ 25 min transitions and Q&A throughout
```

---

### **DEVELOPMENT PART 1: Passive Safety Systems** (Slides 4-12, ~30 minutes)

**Narrative Voice:** Technical and precise. These are pyrotechnic systems — the language must convey the seriousness of the components.

---

#### Slide 4: The Crash Timeline
**Visual:** Horizontal timeline showing a 150-millisecond crash event — 0 ms (impact begins), 10 ms (crash sensors detect), 15 ms (airbag control module decides), 20 ms (squib fires), 40 ms (airbag fully inflated), 70 ms (occupant contacts airbag), 120 ms (airbag deflates), 150 ms (vehicle comes to rest)

**Instructor Narration:**
> "Before we look at the individual components, understand the timeline. A frontal crash at 50 km/h takes about 150 milliseconds — that's one-sixth of a second. The airbag must detect the crash, decide to deploy, fire the inflator, and be fully inflated before your head reaches it. That entire sequence takes about 40 milliseconds. There is zero room for error. Every component in this system must work perfectly, first time, every time. There is no second attempt.
>
> This is why airbag systems have their own dedicated control module, their own sensors, their own wiring, and their own diagnostic protocols. Nothing in this system is shared with anything non-critical."

**PPT Content:**
```
THE CRASH TIMELINE — 150 MILLISECONDS

0 ms    Impact begins — vehicle structure starts deforming
10 ms   Crash sensors (accelerometers) detect rapid deceleration
15 ms   Airbag Control Module (ACM) evaluates sensor data
        — Crash severity? Which airbags? Seatbelt status? Seat position?
20 ms   Squib/initiator fires — ignites pyrotechnic gas generator
25 ms   Airbag inflates with nitrogen gas
40 ms   Airbag FULLY INFLATED — ready for occupant contact
70 ms   Occupant's head/chest contacts airbag
80 ms   Airbag begins deflating through vent holes
        — Controlled energy absorption
120 ms  Airbag mostly deflated
150 ms  Vehicle at rest

TOTAL DECISION + DEPLOYMENT TIME: ~40 ms
Human reaction time to ANY stimulus: ~250 ms

The system is faster than you can blink.
```

---

#### Slide 5: Airbag System Architecture
**Visual:** Vehicle diagram showing all airbag locations (driver frontal, passenger frontal, side torso x2, curtain x2, knee x2) connected by wiring to a central Airbag Control Module (ACM), with crash sensors at front corners, B-pillars, and centre tunnel. Include the clock spring at the steering column.

**Instructor Narration:**
> "Let's map the complete system. The brain is the Airbag Control Module — also called the SRS module or ACM. It sits in the centre of the vehicle, usually under the centre console or behind the dashboard. It receives signals from multiple crash sensors — accelerometers that detect sudden deceleration. Front-mounted sensors catch frontal and offset impacts. Side-mounted sensors in the B-pillars or doors catch side impacts.
>
> The ACM decides which airbags to fire based on crash direction, severity, seatbelt status, seat position, and sometimes occupant weight sensors. A minor fender bender? No deployment. A high-speed frontal? Driver and passenger frontal, both knee bags, and possibly curtains. A side impact? Side torso and curtain on the impacted side only.
>
> Every airbag module contains a squib — a small pyrotechnic initiator — connected to the ACM by a dedicated hardwired circuit. Not CAN bus. Direct copper wire. The ACM fires the squib by sending an electrical pulse. The squib ignites a solid propellant that generates nitrogen gas. The gas inflates the fabric bag in about 20 milliseconds."

**PPT Content:**
```
AIRBAG SYSTEM ARCHITECTURE

BRAIN: Airbag Control Module (ACM / SRS Module)
  Location: Centre tunnel or under dashboard
  Function: Receives crash data, decides deployment, fires squibs
  Contains: Internal accelerometer + processing logic

SENSORS: Crash Sensors (Accelerometers)
  Front left & right (bumper area) — frontal/offset detection
  B-pillar or door-mounted — side impact detection
  Centre tunnel — rollover & severity calibration
  Measure: Rapid deceleration (g-force)

AIRBAG MODULES (typical modern vehicle — 6 to 10):
  Driver frontal (steering wheel)
  Passenger frontal (dashboard)
  Side torso x2 (in seats or door panels)
  Curtain x2 (roof rail — covers side windows)
  Knee x2 (under dashboard — protects lower legs)
  Some vehicles: rear curtain, centre airbag (between front seats)

CONNECTION: Hardwired squib circuits — NOT CAN bus
  Direct electrical firing circuit for maximum reliability
```

---

#### Slide 6: The Squib / Initiator — Pyrotechnic Heart
**Visual:** Cross-section diagram of an airbag inflator module showing the squib (electrical bridge wire), solid propellant charge, and gas generant pellets. Inset showing the electrical circuit — ACM provides firing current through a dedicated loop.

**Instructor Narration:**
> "The squib is a small electrically-fired pyrotechnic device. Think of it as a tiny, very fast explosive. When the ACM sends a precise electrical current — typically 1 to 2 amps — through the squib's bridge wire, the wire heats and ignites a primary charge. That primary charge ignites the gas generant — a solid chemical that rapidly produces nitrogen gas. The gas fills the fabric bag.
>
> This is a one-shot device. Once fired, the entire module — bag, inflator, squib — must be replaced. You cannot repack an airbag. And here's the critical safety point for technicians: the squib is an explosive. If you accidentally apply voltage to the squib circuit — from a test lamp, a short, or static electricity — you fire the airbag. On a bench, that's a serious injury. In a vehicle with someone working near the steering wheel, it could be fatal.
>
> This is why you ALWAYS disconnect the battery and wait a minimum of two minutes — some manufacturers say five or even ten — before working anywhere near an airbag circuit. The ACM has a backup capacitor that holds enough energy to fire the squibs even with the battery disconnected. You wait for that capacitor to discharge."

**PPT Content:**
```
THE SQUIB / INITIATOR — PYROTECHNIC DEVICE

How it works:
1. ACM sends firing current (1-2 A) through dedicated wire
2. Bridge wire heats and ignites primary charge
3. Primary charge ignites gas generant (solid propellant)
4. Gas generant produces nitrogen gas at high pressure
5. Nitrogen inflates airbag fabric in ~20 ms
6. Vent holes in bag allow controlled deflation

ONE-SHOT DEVICE — cannot be reloaded or reused
After deployment: replace entire module (bag + inflator)

TECHNICIAN SAFETY — CRITICAL:
  ALWAYS disconnect battery before working on SRS circuits
  WAIT minimum 2 minutes (check manufacturer spec — up to 10 min)
  Reason: ACM backup capacitor stores energy to fire squibs
  NEVER probe squib circuits with a test lamp or powered meter
  NEVER apply any external voltage to squib connectors
  Store undeployed airbag modules face UP, away from heat
  Treat as EXPLOSIVE DEVICE at all times
```

---

#### Slide 7: The Clock Spring
**Visual:** Exploded diagram of a steering column showing the clock spring (spiral ribbon cable) between the steering column and the steering wheel. Show the ribbon coiled inside the housing. Include a photo of a failed clock spring and the resulting dashboard warning light.

**Instructor Narration:**
> "Here's a component that causes a lot of workshop visits: the clock spring. Think about the problem: the steering wheel rotates. The car's body doesn't. But you need a permanent electrical connection between the steering wheel — where the driver airbag, horn, and steering wheel controls live — and the vehicle's wiring harness, which is fixed to the column. How do you maintain an electrical connection through continuous rotation?
>
> The clock spring. It's a flat ribbon cable wound in a spiral inside a plastic housing, mounted between the steering column and the steering wheel hub. As the wheel turns, the ribbon uncoils or coils, maintaining continuous contact. Typical clock springs allow about 5 full turns in each direction.
>
> When the clock spring fails — and they do, from wear or from the ribbon cracking — you lose the connection to the driver airbag, the horn, and any steering wheel-mounted controls. The most common symptom? The airbag warning light comes on, and the horn stops working. Both at the same time. That's a clock spring until proven otherwise. It's also a common failure after steering or suspension work if the clock spring wasn't centred properly before the steering wheel was refitted."

**PPT Content:**
```
THE CLOCK SPRING (Spiral Cable / Contact Reel)

PROBLEM: Steering wheel rotates. Wiring harness doesn't.
  Need continuous electrical connection through rotation.

SOLUTION: Flat ribbon cable wound in spiral inside plastic housing
  Mounted between steering column and steering wheel
  Allows ~5 turns in each direction (lock to lock)
  Carries circuits for: driver airbag, horn, steering wheel
  buttons (audio, cruise, phone)

FAILURE SYMPTOMS (very common workshop visit):
  Airbag warning light ON (airbag circuit open)
  + Horn does not work
  + Steering wheel buttons intermittent or dead
  = CLOCK SPRING until proven otherwise

TECHNICIAN NOTES:
  Must be CENTRED during installation
  — Turn full lock one direction, count turns, go to midpoint
  — If not centred: ribbon will break when steering reaches lock
  Common failure after: steering rack replacement, column work,
  suspension geometry changes, steering wheel removal
```

---

#### Slide 8: Seatbelts — Pretensioners and Load Limiters
**Visual:** Cutaway diagram of a modern seatbelt retractor showing: (1) the normal inertia reel mechanism, (2) the pyrotechnic pretensioner (gas generator + piston that pulls the belt webbing), and (3) the load limiter (torsion bar that allows controlled extension). Include a before/during/after crash sequence showing belt tightening then yielding.

**Instructor Narration:**
> "The seatbelt is the single most effective safety device in the car. More lives saved than airbags, ABS, and ESC combined. But a modern seatbelt is not just a strap. It has two critical sub-systems that work together during a crash.
>
> First, the pretensioner. In the first few milliseconds of a crash, the pretensioner fires — yes, it's another pyrotechnic device, just like the airbag squib. A small explosive charge drives a piston or rotates a gear that pulls the belt webbing tight against your body. This removes all the slack — maybe 100 to 150 millimetres of belt slack that exists during normal driving. By the time your body starts moving forward, the belt is already skin-tight.
>
> Then, the load limiter. After the pretensioner has tightened the belt, your body decelerates against it. The forces on your chest can be enormous — enough to cause rib fractures and internal injuries from the belt alone. The load limiter is a torsion bar or a fold in the belt webbing that allows the belt to extend slightly under a controlled force — typically around 4 to 6 kilonewtons. This reduces the peak force on the chest.
>
> So the sequence is: pretensioner pulls belt TIGHT, then load limiter lets belt extend SLIGHTLY under controlled load. Tight first, then yield. It's counterintuitive, but it's engineered. And both components are one-shot — after a crash deployment, the entire seatbelt assembly is replaced."

**PPT Content:**
```
MODERN SEATBELT SYSTEMS

BASIC FUNCTION: Three-point inertia reel
  Normal driving: belt extends and retracts freely
  Sudden deceleration: inertia locks the reel, belt holds

PRETENSIONER (pyrotechnic — fires in crash):
  Trigger: Signal from ACM in first ~15 ms of crash
  Action: Explosive charge drives piston that PULLS belt tight
  Removes: 100-150 mm of slack from normal belt fit
  Result: Belt is skin-tight BEFORE body moves forward
  One-shot device — replace after deployment

LOAD LIMITER (mechanical — activates after pretensioner):
  Trigger: Belt force exceeds threshold (~4-6 kN)
  Action: Torsion bar or fold allows CONTROLLED belt extension
  Purpose: Reduces peak chest force to prevent rib fractures
  Allows: ~40-50 mm of controlled yielding

CRASH SEQUENCE:
  1. Pretensioner fires → belt pulled tight (removes slack)
  2. Body decelerates against tight belt
  3. Load limiter yields → controlled extension (reduces chest load)
  4. Airbag deploys → cushions head and upper body

TECHNICIAN NOTE:
  Pretensioners are pyrotechnic — same safety rules as airbags
  After deployment: replace entire seatbelt retractor assembly
  Check: pretensioner connector during any dashboard removal
```

---

#### Slide 9: Crumple Zones and the Safety Cell
**Visual:** Top-down and side-view diagram of a unibody vehicle structure showing: front crumple zone (green, designed to collapse), rear crumple zone (green), and rigid passenger safety cell (red, designed to NOT collapse). Include arrows showing energy absorption and force distribution paths. Inset photo of a crash-tested vehicle showing controlled deformation.

**Instructor Narration:**
> "Now the structural side. The car's body is not uniformly strong. It's engineered with two very different zones. The front and rear are crumple zones — they are designed to collapse in a controlled, progressive manner during a crash. The key word is 'controlled.' The metal doesn't just crumple randomly. Engineers design specific folding patterns, weakened sections, and energy-absorbing structures that convert the kinetic energy of the crash into deformation energy. The longer the crumple zone crushes, the more time the deceleration takes, and the lower the peak g-force on the occupants.
>
> In the middle is the safety cell — the passenger compartment. This is designed to be as rigid as possible. High-strength steel, ultra-high-strength boron steel in the B-pillars, reinforcement beams in the doors. The safety cell should NOT deform. Its job is to maintain a survival space around the occupants while the crumple zones absorb the energy.
>
> This is why repair work on structural components is so critical. If you straighten a crumple zone member incorrectly, or replace a structural panel with the wrong grade of steel, you change the crash performance. Some structural members are specifically marked as 'replace only' — no straightening, no welding. The manufacturer's repair procedures must be followed exactly."

**PPT Content:**
```
CRUMPLE ZONES & SAFETY CELL

CRUMPLE ZONES (Front and Rear):
  Purpose: Absorb crash energy through CONTROLLED deformation
  Material: Mild steel, designed crush patterns
  Principle: Longer deformation time = lower peak g-force on occupants
  Front: Engine subframe, longitudinal rails, bumper beam
  Rear: Rear rails, floor pan extensions, bumper beam

SAFETY CELL (Passenger Compartment):
  Purpose: Maintain survival space — MUST NOT deform
  Material: High-strength steel (HSS), ultra-high-strength steel (UHSS)
  Key areas:
    A-pillars (windscreen frame)
    B-pillars (between front and rear doors) — often boron steel
    Roof rails
    Floor tunnel
    Door reinforcement beams (side impact bars)

PHYSICS: F = ma
  Longer crush distance = longer deceleration time
  Longer time = lower deceleration force
  Lower force = survivable crash

TECHNICIAN WARNING:
  Structural repairs affect crash performance
  Some members: REPLACE ONLY (no straightening, no heat, no welding)
  Wrong steel grade = compromised safety cell
  ALWAYS follow manufacturer repair procedures for structural work
```

---

#### Slide 10: Passive Safety — The Complete System
**Visual:** Full-vehicle transparent diagram showing all passive safety systems working together: crumple zones deforming, safety cell intact, seatbelt pretensioners fired, all airbags deployed, head restraints in position. Include a numbered sequence showing the order of activation.

**Instructor Narration:**
> "Let's see how all of these work together in a real crash. Impact occurs — the front crumple zone begins collapsing, absorbing energy. Within 10 milliseconds, the crash sensors detect the deceleration and report to the ACM. At 15 milliseconds, the ACM evaluates the data: frontal crash, moderate to severe. It fires the seatbelt pretensioners first — both front seats. Belts go tight. At 20 milliseconds, it fires the driver and passenger frontal airbags, and possibly the knee airbags. If the crash has a lateral component, side airbags and curtains fire too.
>
> By 40 milliseconds, airbags are fully inflated. The occupants' bodies are now decelerating against tight seatbelts and inflated airbags, inside a rigid safety cell, while the crumple zone continues absorbing energy. By 80 milliseconds, the airbags are deflating through their vent holes. By 150 milliseconds, the vehicle is at rest.
>
> Every single component played its role. Remove any one of them and the outcome changes dramatically. This is why you never disable an airbag warning light without diagnosing the fault. That warning light means the system will NOT deploy in a crash."

**PPT Content:**
```
PASSIVE SAFETY — THE COMPLETE SYSTEM IN ACTION

SEQUENCE (frontal crash, 50 km/h):
  0 ms    Impact → crumple zone begins absorbing energy
  10 ms   Crash sensors detect deceleration → signal to ACM
  15 ms   ACM evaluates: crash type, severity, occupant status
  15 ms   ACM fires seatbelt pretensioners → belts pulled tight
  20 ms   ACM fires frontal airbags → squibs ignite gas generants
  25 ms   Load limiters engage → controlled belt yielding begins
  40 ms   Airbags FULLY INFLATED
  70 ms   Occupant contacts airbag → head/chest cushioned
  80 ms   Airbags deflate through vent holes
  100 ms  Crumple zone fully crushed → safety cell intact
  150 ms  Vehicle at rest → door unlocks, fuel pump shuts off

ALL SYSTEMS WORK TOGETHER:
  Crumple zones: absorb energy, extend deceleration time
  Safety cell: maintains survival space
  Pretensioners: remove belt slack before body moves
  Load limiters: reduce peak chest force
  Airbags: cushion head and torso against steering wheel/dashboard
  Head restraints: prevent whiplash (rear impact)

NEVER clear an airbag warning light without diagnosis
  Warning light ON = system WILL NOT deploy in a crash
```

---

#### Slide 11: Airbag System DTCs and Diagnostics
**Visual:** Screenshot of a scan tool showing typical airbag DTCs — B0001 (driver frontal deployment loop resistance high), B0051 (crash sensor communication), B0081 (driver seatbelt pretensioner circuit). Include the airbag warning light symbol.

**Instructor Narration:**
> "The airbag system performs continuous self-diagnostics. Every time you start the car, the ACM checks every squib circuit, every sensor connection, and its own internal accelerometer. If anything is out of range — a squib resistance too high or too low, a sensor signal missing, a wiring fault — the ACM sets a DTC and turns on the airbag warning light.
>
> Common DTCs you'll see: high resistance in a squib circuit — often a corroded connector or damaged wire. Clock spring open circuit — the ribbon cable has cracked. Crash sensor communication lost — CAN bus fault to an external sensor. Occupant classification fault — the passenger seat weight sensor has failed.
>
> Here's the important part: when the airbag light is on, the ACM may disable some or all airbag deployment. The system knows it has a fault, so rather than risk partial or incorrect deployment, it disables itself. This means the vehicle's occupants are unprotected. It's not just a warning light — it's a safety-critical fault."

**PPT Content:**
```
AIRBAG DIAGNOSTICS

SELF-CHECK: ACM tests all circuits at every ignition on
  Squib loop resistance: typically 1.5-3.5 ohms
  Too high = open circuit (broken wire, corroded connector)
  Too low = short circuit (damaged wiring, water ingress)
  Sensor communication: CAN bus signals from external crash sensors

COMMON DTCs:
  B0001 / B0100: Driver frontal deployment loop — resistance high/open
  B0002 / B0101: Passenger frontal deployment loop
  B0051: Front crash sensor — communication lost
  B0081: Driver seatbelt pretensioner circuit
  B0090: Passenger occupant classification — sensor fault
  B0095: Clock spring / spiral cable — circuit open

AIRBAG WARNING LIGHT ON = SYSTEM COMPROMISED
  ACM may disable deployment of affected or ALL airbags
  Occupants are UNPROTECTED
  Must diagnose and repair — never just clear the code

CRASH DATA (Event Data Recorder):
  ACM stores crash data: g-force, deployment status, belt status
  Data is LOCKED after deployment — cannot be erased
  Used by insurance, police, accident investigators
```

---

#### Slide 12: Passive Safety Recap
**Visual:** Summary table of all passive safety components with their function, location, and one-sentence description

**Instructor Narration:**
> "Let's lock in the passive safety systems before we move to active safety. You should be able to name every component, explain what it does, and describe how it's activated. Quick fire — I'll name the component, you tell me the function. Ready?"

**PPT Content:**
```
PASSIVE SAFETY — SUMMARY

COMPONENT              FUNCTION                     ACTIVATION
Frontal airbags        Cushion head/chest           Pyrotechnic (ACM fires squib)
Side torso airbags     Protect torso in side impact  Pyrotechnic
Curtain airbags        Protect head, cover windows   Pyrotechnic
Knee airbags           Protect lower legs/femur      Pyrotechnic
Seatbelt pretensioner  Remove belt slack instantly    Pyrotechnic
Seatbelt load limiter  Reduce peak chest force        Mechanical (torsion bar)
Clock spring           Electrical link through        Passive (always connected)
                       steering rotation
Crumple zones          Absorb crash energy           Structural deformation
Safety cell            Maintain survival space        Rigid structure (no deformation)
Head restraints        Prevent whiplash (rear crash)  Passive positioning
Door side impact beams Resist door intrusion         Structural
```

**Activity:** Rapid verbal quiz — instructor names component, learners state function. 2 minutes.

---

### **DEVELOPMENT PART 2: Active Safety & ADAS** (Slides 13-22, ~35 minutes)

**Narrative Voice:** Forward-looking, technically precise. Emphasise that ADAS is the fastest-growing area of workshop technology and a major revenue opportunity.

---

#### Slide 13: Active Safety — From ESC to Full ADAS
**Visual:** Timeline showing the evolution of active safety: ABS (1985) -> Traction Control (1990) -> ESC (2000) -> ACC (2005) -> LKA (2010) -> AEB (2014) -> Full ADAS suites (2020+). Show how each system builds on the previous one.

**Instructor Narration:**
> "Active safety didn't start with cameras and radar. It started with ABS in the 1980s — preventing wheel lock-up so the driver could steer while braking hard. Then came Traction Control — preventing wheelspin on acceleration. Then ESC in the 2000s — the game changer. ESC selectively brakes individual wheels to keep the car stable when it starts to slide.
>
> ESC is the foundation. Remember Day 24? ESC uses wheel speed sensors, a steering angle sensor, and a yaw rate sensor to compare where the driver wants to go with where the car is actually going. If there's a mismatch, it brakes individual wheels to correct the car's path. Every ADAS system that involves braking — AEB, ACC, collision avoidance — uses the ESC hydraulic unit to apply the brakes. ESC is the muscle that ADAS systems command.
>
> What changed after ESC is the addition of environmental perception. The car started looking outward. Radar, cameras, lidar, ultrasonic — these sensors gave the car the ability to see the road, detect obstacles, read signs, and monitor traffic. That's what ADAS is: the car's ability to perceive its environment and act on that perception."

**PPT Content:**
```
ACTIVE SAFETY EVOLUTION

1985: ABS — Prevent wheel lock-up during braking
1990: Traction Control (ASR) — Prevent wheelspin on acceleration
2000: ESC — Selective braking to maintain stability
        ↓
     ESC = FOUNDATION OF ALL ADAS
     Uses: Wheel speed sensors, steering angle sensor, yaw rate sensor
     Controls: Hydraulic brake unit (applies brakes to individual wheels)
        ↓
2005: Adaptive Cruise Control (ACC) — Radar + ESC braking
2010: Lane Keep Assist (LKA) — Camera + EPS steering
2014: AEB mandatory in Euro NCAP 5-star rating
2020+: Full ADAS suites — multiple sensors fused together

KEY INSIGHT: ADAS = Environmental Perception + Existing Actuators
  Perception: Radar, camera, lidar, ultrasonic
  Action: ESC (braking), EPS (steering), engine/motor (speed)
  Brain: ADAS control module (sensor fusion + decision logic)
```

---

#### Slide 14: AEB — Automatic Emergency Braking
**Visual:** Three-phase diagram showing AEB operation: Phase 1 (radar/camera detects obstacle, calculates time to collision), Phase 2 (visual and audible warning to driver), Phase 3 (if no driver response — autonomous full braking). Include a distance/time chart showing how AEB reduces impact speed.

**Instructor Narration:**
> "AEB is the single most important ADAS system in terms of lives saved. It works in three phases. Phase one: the forward-facing radar and camera continuously scan the road ahead. They detect vehicles, pedestrians, cyclists, and sometimes animals. The ADAS control module calculates the time to collision — how many seconds until impact at current closing speed.
>
> Phase two: if time to collision drops below a threshold — typically 2 to 3 seconds — the system alerts the driver. Visual warning on the instrument cluster, audible alarm, sometimes a brief brake pulse you can feel through the pedal. This is the 'wake up' call.
>
> Phase three: if the driver does not respond — no braking, no steering — and impact is imminent, the system applies full autonomous braking. It commands the ESC hydraulic unit to apply maximum braking force to all four wheels. At 50 km/h, AEB can often bring the car to a complete stop. At 80 km/h, it may not prevent the crash entirely, but it can reduce the impact speed by 30 to 40 km/h — and crash severity increases with the square of the speed, so even a modest speed reduction dramatically reduces injury."

**PPT Content:**
```
AEB — AUTOMATIC EMERGENCY BRAKING

PHASE 1: Detection (continuous)
  Sensors: Forward radar + forward camera (fused data)
  Detects: Vehicles, pedestrians, cyclists, (some systems) animals
  Calculates: Time to collision (TTC) and closing speed

PHASE 2: Warning (~2-3 seconds before potential impact)
  Visual: Warning icon on instrument cluster / head-up display
  Audible: Alert tone / chime
  Haptic: Brief brake pulse felt through pedal (some systems)

PHASE 3: Autonomous braking (if driver does not respond)
  Commands: ESC hydraulic unit — full braking force, all wheels
  At 50 km/h: Can often achieve full stop before impact
  At 80 km/h: Reduces impact speed by 30-40 km/h

  Impact energy = 1/2 * m * v²
  Reducing speed from 80 to 40 km/h = 75% less impact energy

AEB LIMITATIONS:
  Heavy rain/snow may reduce sensor range
  Stationary objects at high speed (some systems limited)
  Sensor blocked by dirt, ice, or stickers on windscreen
  System can be overridden by driver pressing accelerator
```

---

#### Slide 15: Lane Keep Assist (LKA)
**Visual:** Forward camera view showing detected lane markings (highlighted in green), with steering correction arrows showing the EPS applying gentle corrective steering. Include the LKA icon from a typical instrument cluster.

**Instructor Narration:**
> "Lane Keep Assist uses a forward-facing camera — usually mounted behind the windscreen near the rear-view mirror — to detect lane markings. The camera identifies the solid and dashed lines on both sides of the lane and calculates the vehicle's position within the lane.
>
> If the vehicle starts to drift toward a lane marking without the turn signal being activated — suggesting the driver is drifting unintentionally — the system responds. Basic Lane Departure Warning simply vibrates the steering wheel or sounds an alert. Full Lane Keep Assist goes further: it applies a gentle corrective steering torque through the Electric Power Steering motor to guide the car back toward the centre of the lane.
>
> This is not autonomous steering. The system applies a gentle nudge — maybe 2 to 3 Newton-metres of torque. The driver can easily override it by holding the steering wheel. And if the system detects that the driver is not holding the wheel at all — hands-off detection — it will alert and eventually disengage.
>
> LKA limitations: it needs visible lane markings. Worn markings, snow-covered roads, construction zones with temporary lines, or roads with no markings at all — the system cannot function. The camera also struggles in heavy rain, fog, or direct glare."

**PPT Content:**
```
LKA — LANE KEEP ASSIST

SENSOR: Forward-facing camera (windscreen-mounted)
  Detects: Lane markings (solid, dashed, road edges)
  Calculates: Vehicle position within lane

OPERATION:
  1. Camera continuously tracks lane boundaries
  2. Vehicle drifts toward marking WITHOUT turn signal active
  3. System response (varies by level):

  Lane Departure WARNING (LDW):
    Vibrates steering wheel / sounds alert
    No steering correction

  Lane Keep ASSIST (LKA):
    Applies gentle corrective steering via EPS motor
    Torque: ~2-3 Nm (driver easily overrides)

  Lane CENTRING (some premium systems):
    Actively keeps vehicle centred in lane
    Works with ACC for semi-autonomous highway driving

LIMITATIONS:
  Requires VISIBLE lane markings
  Fails: worn markings, snow-covered, no markings
  Reduced: heavy rain, fog, low sun angle (glare)
  Disengages: if driver removes hands from wheel (hands-off detection)
```

---

#### Slide 16: Adaptive Cruise Control (ACC)
**Visual:** Top-down view showing ACC operation: lead vehicle detected by forward radar, following distance maintained, ACC vehicle automatically adjusting speed. Show the transition from set speed (no car ahead) to following mode (car detected, speed reduced to maintain gap).

**Instructor Narration:**
> "Adaptive Cruise Control builds on conventional cruise control by adding radar. You set your desired speed and a following distance — usually represented as a time gap in seconds. The forward-facing radar continuously measures the distance and relative speed of the vehicle ahead.
>
> If the road is clear, ACC maintains your set speed — just like conventional cruise control. When a slower vehicle enters your lane, ACC detects it and gradually reduces speed to maintain your chosen following distance. If that vehicle speeds up or moves out of your lane, ACC accelerates back to your set speed.
>
> Modern full-speed-range ACC works from highway speed all the way down to standstill. In stop-and-go traffic, it will bring the car to a complete stop behind the vehicle ahead and resume when traffic moves. The braking is done through the ESC unit, and the acceleration is done through the engine or electric motor management.
>
> ACC does NOT detect stationary objects like parked cars or barriers at high speed on most systems. It's designed for following moving traffic. This is an important limitation to understand."

**PPT Content:**
```
ACC — ADAPTIVE CRUISE CONTROL

SENSOR: Forward-facing long-range radar (+ camera on some systems)
  Measures: Distance to vehicle ahead + relative speed (Doppler)
  Range: Up to 200 metres ahead

OPERATION:
  Driver sets: Desired speed + following distance (time gap, e.g., 2 sec)

  NO vehicle ahead: Maintains set speed (like conventional cruise)
  Slower vehicle detected:
    1. Reduces engine/motor power
    2. If needed: applies brakes via ESC
    3. Maintains chosen following distance
  Vehicle ahead accelerates/moves: ACC accelerates back to set speed

  Full-speed-range ACC: Works 0-200+ km/h including stop-and-go
  Stop & Go: Brings car to complete stop, resumes when traffic moves

ACTUATORS USED:
  Engine/motor management (acceleration)
  ESC hydraulic unit (braking)
  Transmission (gear selection — some systems)

LIMITATIONS:
  May NOT detect stationary objects at high speed
  Designed for MOVING traffic following
  Cut-in vehicles (suddenly entering lane) may cause late reaction
  Heavy rain/snow can reduce radar range
```

---

#### Slide 17: Additional ADAS Systems
**Visual:** Vehicle top-down view showing sensor coverage zones for: blind spot monitoring (rear quarter radar cones), rear cross-traffic alert (rear corner radar cones sweeping perpendicular), and surround-view cameras (four wide-angle cameras stitched into a bird's-eye view)

**Instructor Narration:**
> "Beyond the big three — AEB, LKA, and ACC — modern vehicles have a suite of additional ADAS systems. Blind Spot Monitoring uses short-range radar in the rear bumper corners to detect vehicles in your blind spot. When a car is alongside, a warning light appears in or near the side mirror. If you activate the turn signal toward the occupied blind spot, the warning escalates — flashing light, audible alert, and some systems will apply corrective steering.
>
> Rear Cross-Traffic Alert uses those same rear corner radars, but when you're reversing out of a parking space. It detects vehicles approaching from the sides — vehicles you can't see because the cars parked next to you are blocking your view. If a vehicle is approaching, it warns you and can apply autonomous braking.
>
> Surround-view cameras use four wide-angle cameras — front, rear, and both side mirrors — to create a synthesised bird's-eye view of the vehicle and its immediate surroundings. This is a parking aid, not a crash prevention system, but it dramatically improves the driver's spatial awareness."

**PPT Content:**
```
ADDITIONAL ADAS SYSTEMS

BLIND SPOT MONITORING (BSM):
  Sensors: Short-range radar in rear bumper corners
  Detects: Vehicles alongside in adjacent lanes
  Warning: Light in/near side mirror; escalates if turn signal activated
  Some systems: Apply corrective steering if driver merges toward vehicle

REAR CROSS-TRAFFIC ALERT (RCTA):
  Sensors: Same rear corner radars as BSM
  Active: When reversing out of parking space
  Detects: Vehicles approaching from sides (perpendicular)
  Warning: Visual + audible; some apply autonomous braking

SURROUND-VIEW CAMERA SYSTEM:
  Sensors: 4 wide-angle cameras (front, rear, left mirror, right mirror)
  Output: Stitched bird's-eye view on infotainment screen
  Purpose: Parking aid — spatial awareness, not crash prevention

ALSO COMMON:
  Traffic Sign Recognition (camera reads speed limit signs)
  Driver Attention Monitoring (camera watches driver's face/eyes)
  Automatic High Beam (camera detects oncoming headlights)
  Park Assist (ultrasonic + steering automation for parallel parking)
```

---

#### Slide 18: ADAS Sensors — The Four Types
**Visual:** Four-quadrant diagram, one quadrant per sensor type. Each quadrant shows: the sensor, its physical principle, its detection range and field of view, and its strengths/weaknesses. RADAR (top-left), LIDAR (top-right), Camera (bottom-left), Ultrasonic (bottom-right).

**Instructor Narration:**
> "ADAS systems are only as good as their sensors. There are four types, and each has different strengths. Radar sends out radio waves and measures the reflection. It's excellent at measuring distance and speed — the Doppler effect tells you whether the target is moving toward or away from you and how fast. Radar works in rain, fog, and darkness. Long-range forward radar reaches 200 metres or more. Short-range corner radar covers the blind spots.
>
> Lidar uses laser light pulses instead of radio waves. Each pulse reflects off surfaces and returns, and the time-of-flight gives extremely precise distance. A spinning or solid-state lidar creates a detailed 3D point cloud of the environment. It's incredibly precise but expensive, and it struggles in heavy rain and snow because the laser light scatters off water droplets. Lidar is currently used mainly on premium and autonomous development vehicles.
>
> Cameras are the most versatile sensor. A monocular camera behind the windscreen detects lane markings, traffic signs, and objects. Add a second camera for stereo vision, and you can calculate depth — distance to objects — from the parallax between the two images. Cameras provide colour and texture information that radar and lidar cannot. But cameras struggle in low light, direct glare, and heavy precipitation — just like human eyes.
>
> Ultrasonic sensors are the simplest. They send out sound pulses and measure the echo. Short range — typically 0.2 to 3 metres. They're your parking sensors. Cheap, reliable, but only useful at very close range."

**PPT Content:**
```
ADAS SENSORS — FOUR TYPES

RADAR (Radio Detection and Ranging):
  Principle: Radio waves — measures reflection time + Doppler shift
  Range: Long-range 200+ m (forward), Short-range 30 m (corners)
  Strengths: Works in rain, fog, darkness; measures speed directly
  Weakness: Limited detail (cannot read signs or detect lane markings)
  Location: Front bumper (long-range), rear corners (short-range)

LIDAR (Light Detection and Ranging):
  Principle: Laser pulses — time-of-flight measurement
  Range: Up to 250 m; creates 3D point cloud
  Strengths: Extremely precise distance; high-resolution 3D mapping
  Weakness: Expensive; struggles in heavy rain/snow (laser scatters)
  Location: Roof, front bumper, or behind windscreen

CAMERA (Monocular and Stereo):
  Principle: Image processing — pattern recognition, machine learning
  Range: Up to 150 m (depends on resolution and object size)
  Strengths: Colour, texture, sign reading, lane marking detection
  Weakness: Struggles in low light, glare, heavy precipitation
  Location: Behind windscreen (forward); in mirrors (surround-view)

ULTRASONIC:
  Principle: Sound pulses — echo time measurement
  Range: 0.2-3 m (very short range)
  Strengths: Cheap, reliable, works in all weather at close range
  Weakness: Very short range; no speed/direction information
  Location: Front and rear bumpers (parking sensors)
```

---

#### Slide 19: Sensor Fusion — Why One Sensor Is Not Enough
**Visual:** Venn diagram showing the overlap of radar, camera, and lidar capabilities. The centre (all three overlap) is labeled "highest confidence." Show a scenario where radar sees a vehicle, camera confirms it's a car (not a sign), and lidar maps its exact shape.

**Instructor Narration:**
> "No single sensor is perfect. Radar can see through rain but can't read a speed limit sign. Cameras can read signs but fail in dense fog. Lidar creates precise 3D maps but is expensive and weather-sensitive. This is why modern ADAS systems use sensor fusion — combining data from multiple sensors to create a more reliable picture than any single sensor could provide alone.
>
> The ADAS control module receives data from all available sensors and cross-references them. Radar says there's an object 50 metres ahead and it's closing. Camera confirms: it's a vehicle, specifically a truck. Lidar adds: here's its exact shape and lateral position. With all three sources agreeing, the system has high confidence. If one sensor disagrees or provides no data, the system reduces its confidence level and may adjust its response — perhaps warning the driver instead of applying autonomous braking.
>
> This is also why sensor calibration matters so much. If the camera is aimed 2 degrees off centre, it may see the lane markings in the wrong position. If the radar beam is tilted, it may not detect a vehicle that's actually there. Every sensor must be precisely aligned to the vehicle's centreline and reference plane."

**PPT Content:**
```
SENSOR FUSION — COMBINING MULTIPLE INPUTS

WHY FUSION:
  No single sensor is perfect in all conditions
  Each has unique strengths and weaknesses
  Combining them = more reliable perception

HOW IT WORKS:
  ADAS control module receives data from ALL sensors simultaneously
  Cross-references: "Radar sees object at 50 m, camera confirms it's a car"
  Confidence level: Higher when multiple sensors agree

EXAMPLE SCENARIOS:
  Clear day: Camera (strong) + Radar (strong) + Lidar (strong) = HIGH confidence
  Heavy rain: Camera (weak) + Radar (strong) + Lidar (weak) = MEDIUM confidence
  Night: Camera (moderate with IR) + Radar (strong) + Lidar (strong) = HIGH
  Dense fog: Camera (fail) + Radar (strong) + Lidar (weak) = LOWER confidence

SYSTEM ADAPTS: Adjusts response based on confidence
  High confidence → full AEB authority
  Lower confidence → earlier warning, reduced autonomous action
  Sensor failure → system degraded, driver notified

THIS IS WHY CALIBRATION IS CRITICAL
  Misaligned sensor = incorrect fusion = wrong response
```

---

#### Slide 20: ADAS Sensor Calibration — Static vs Dynamic
**Visual:** Two photographs side by side. Left: Static calibration setup — a vehicle positioned precisely on a flat surface in front of a calibration target board mounted on a stand at a specific distance and height, with alignment tools visible. Right: Dynamic calibration — a vehicle driving on a marked road with an on-screen display showing "calibration in progress."

**Instructor Narration:**
> "Calibration is the process of aligning each sensor's field of view to the vehicle's centreline and reference plane. There are two methods.
>
> Static calibration is done in the workshop. The vehicle is positioned on a level surface with specific alignment to a calibration target board — usually a board with a precise geometric pattern that the camera recognises. The target must be at an exact distance from the vehicle, at an exact height, and perfectly square to the vehicle's centreline. Some radar calibrations use a reflector target. The scan tool initiates a calibration routine, the sensor 'learns' its correct aim point relative to the target, and stores the calibration values.
>
> This is demanding work. The floor must be level. The vehicle must be at correct ride height — tyres inflated to spec, no heavy loads in the boot. The target must be positioned with millimetre precision. Some manufacturers require specific equipment that costs thousands — even tens of thousands — of dollars.
>
> Dynamic calibration is done by driving the vehicle. The scan tool puts the sensor into calibration mode, and the driver follows a specific procedure — typically driving at a set speed on a road with clear lane markings and a minimum of traffic. The camera or radar observes the road environment and self-calibrates based on what it sees. Dynamic calibration can take 10 to 30 minutes of driving.
>
> Some sensors require static only, some accept dynamic only, and some need both. Always check the manufacturer procedure."

**PPT Content:**
```
ADAS SENSOR CALIBRATION

STATIC CALIBRATION (Workshop):
  Setup: Vehicle on level floor, precise position relative to target
  Target: Specific pattern board or radar reflector at exact distance/height
  Tool: Scan tool initiates calibration routine
  Sensor: Learns correct aim point and stores values
  Requirements:
    Level floor (within manufacturer tolerance)
    Correct tyre pressures (affects ride height)
    No extra load in vehicle
    Target at EXACT distance (measured with tape or laser)
    Target square to vehicle centreline
    Adequate lighting (for camera calibration)

DYNAMIC CALIBRATION (Driving):
  Setup: Scan tool puts sensor in calibration mode
  Procedure: Drive at set speed (e.g., 60-100 km/h)
  Road: Clear lane markings, minimal traffic, straight or gentle curves
  Duration: 10-30 minutes of driving
  Sensor: Self-calibrates from observed road environment

WHICH METHOD?
  Forward camera: Usually static OR dynamic (manufacturer-dependent)
  Forward radar: Usually static (target or reflector)
  Corner radars: Static (target positioning) or dynamic
  Surround cameras: Static (target boards around vehicle)
  Always check manufacturer procedure — no guessing
```

---

#### Slide 21: When Is Calibration Mandatory?
**Visual:** List of common workshop scenarios with check marks indicating "calibration required." Include photos of: a cracked windscreen being replaced, a bumper removed for body repair, a vehicle on a wheel alignment rack, and a suspension component being replaced.

**Instructor Narration:**
> "This is where the money is for modern workshops, and where the danger is if you get it wrong. ADAS sensors must be recalibrated whenever their position relative to the vehicle's centreline or road surface has changed. That means:
>
> Windscreen replacement. The forward camera is mounted to the windscreen. Remove the windscreen, and the camera mounting angle changes. Even a fraction of a degree matters at 150 metres. Calibration is mandatory — no exceptions.
>
> Front bumper removal or replacement. The forward radar is mounted in or behind the front bumper. Any body repair that involves bumper removal requires radar recalibration.
>
> Suspension work that changes ride height. Springs, shock absorbers, air suspension recalibration — anything that changes the vehicle's relationship to the road surface changes the vertical aim of every sensor. Calibration required.
>
> Wheel alignment. If the thrust angle changes, the vehicle's direction of travel changes relative to where the sensors are pointed. Calibration may be required.
>
> Any structural repair. If the body structure has been pulled or straightened, sensor mounting points may have shifted.
>
> The consequences of NOT calibrating are serious. A forward camera aimed 1 degree to the right will see the lane markings 2.6 metres off-centre at 150 metres. Lane Keep Assist will steer the car into oncoming traffic. AEB may brake for a phantom target or fail to detect a real one. A radar aimed slightly downward may see the road surface as an obstacle and trigger braking on a perfectly clear road."

**PPT Content:**
```
WHEN IS ADAS CALIBRATION MANDATORY?

ALWAYS REQUIRED AFTER:
  Windscreen replacement (forward camera mounting changes)
  Front bumper removal/replacement (radar mounting affected)
  Rear bumper removal/replacement (corner radar mounting)
  Suspension work that changes ride height (springs, shocks, air susp.)
  Wheel alignment (thrust angle changes vehicle direction)
  Steering angle sensor replacement or reset
  ADAS sensor replacement (camera, radar, lidar)
  Structural/body repair affecting sensor mounting points
  Airbag module replacement (some vehicles link calibration)

CONSEQUENCES OF SKIPPING CALIBRATION:

  Forward camera off by 1 degree:
    At 150 m: Lane markings detected 2.6 m off-centre
    LKA may steer INTO oncoming traffic

  Forward radar off by 1 degree:
    At 200 m: Detection area shifted 3.5 m to the side
    AEB may miss a vehicle directly ahead

  REAL-WORLD RESULT:
    AEB brakes for wrong target (bridge, sign, parked car)
    AEB fails to brake for actual obstacle
    LKA steers toward barrier or oncoming lane
    ACC follows vehicle in adjacent lane instead of lead vehicle

  THIS IS A SAFETY-CRITICAL PROCEDURE — NOT OPTIONAL
```

---

#### Slide 22: Active Safety & ADAS Recap
**Visual:** Summary table listing all ADAS systems covered, their primary sensor, their primary actuator, and their function

**Instructor Narration:**
> "Let's consolidate. Every ADAS system is a combination of perception — sensors that see the environment — and action — actuators that control the car. The ADAS control module is the bridge between them. As a technician, you need to know: which sensors feed which system, and what happens when a sensor fails or is miscalibrated. Let me quiz you before we go to the workshop."

**PPT Content:**
```
ACTIVE SAFETY & ADAS — SUMMARY

SYSTEM    PRIMARY SENSOR       ACTUATOR         FUNCTION
ESC       Wheel speed +        ESC hydraulic    Maintain vehicle
          yaw rate + steer     unit             stability
          angle

AEB       Radar + camera       ESC hydraulic    Prevent/reduce
                               unit             frontal collision

LKA       Camera               EPS motor        Keep vehicle
                                                in lane

ACC       Radar (+ camera)     ESC + engine/    Maintain following
                               motor mgmt       distance

BSM       Short-range          Warning light    Detect vehicles
          corner radar         + alert          in blind spot

RCTA      Corner radar         Warning +        Detect cross-
                               auto braking     traffic reversing

Surround  4 wide-angle         Display          Bird's-eye
View      cameras                               parking view

SENSORS           WHAT THEY MEASURE       RANGE
Radar             Distance + speed        30-200+ m
Lidar             Distance (3D cloud)     Up to 250 m
Camera            Image (objects, signs)  Up to 150 m
Ultrasonic        Distance (echo)         0.2-3 m
```

**Activity:** Quick verbal quiz — instructor names an ADAS system, learners state the primary sensor and actuator. 3 minutes.

---

### **PRACTICAL: Workshop Session** (Slides 23-26, ~75 minutes)

**Narrative Voice:** Hands-on instruction. Move to the workshop floor. Safety briefing first — airbag components are pyrotechnic.

---

#### Slide 23: Practical Session Overview & Safety Briefing
**Visual:** Workshop layout showing four stations marked with numbers. Include a safety warning box: "AIRBAG COMPONENTS ARE PYROTECHNIC DEVICES — FOLLOW ALL SAFETY PROTOCOLS"

**Instructor Narration:**
> "We're heading to the workshop. Today's practical has four stations. You'll rotate through each one in groups of three or four. Before we go — a safety reminder specific to today's session.
>
> Station 1 involves identifying airbag modules and crash sensors. These are installed on a vehicle with the battery DISCONNECTED. Do not reconnect the battery. Do not probe any airbag connectors with any tool. Treat every yellow connector you see as a potential pyrotechnic circuit. You'll look, identify, and note locations — you will not disconnect anything.
>
> Station 2 is ADAS sensor identification — radar, cameras, ultrasonic. These are not pyrotechnic, but they are expensive and delicate. Do not touch the sensor faces or camera lenses.
>
> Station 3 is scan tool diagnostics — reading airbag DTCs and crash data. Purely electronic — plug in, read, interpret.
>
> Station 4 is calibration awareness — I've set up a static calibration target board. You'll see the setup, understand the positioning requirements, and measure the distances involved."

**PPT Content:**
```
PRACTICAL SESSION — 4 STATIONS (75 minutes total)

STATION 1: Airbag Component Identification (20 min)
  Locate: All airbag modules, crash sensors, ACM, clock spring
  Vehicle: Battery DISCONNECTED
  RULE: Do NOT probe yellow connectors. Look, identify, note.

STATION 2: ADAS Sensor Identification (15 min)
  Locate: Forward radar, forward camera, corner radars,
          ultrasonic sensors, surround cameras
  RULE: Do NOT touch sensor faces or camera lenses

STATION 3: Scan Tool — Airbag Diagnostics (20 min)
  Read: Airbag DTCs, crash data record, system status
  Tool: OBD-II scan tool with SRS module access

STATION 4: Static Calibration Awareness (20 min)
  Examine: Calibration target board setup
  Measure: Target distance from vehicle, height, alignment
  Discuss: What happens if these measurements are wrong

SAFETY: Airbag components = pyrotechnic devices
  Battery must be disconnected when near SRS components
  Yellow connectors = airbag circuits — do not probe
```

---

#### Slide 24: Station 1 — Airbag Component Identification
**Visual:** Annotated vehicle diagram showing the location of every airbag component: driver frontal (steering wheel), passenger frontal (dashboard), side torso (seat bolster or door), curtain (roof rail), knee (under dashboard), crash sensors (front bumper area, B-pillars, centre tunnel), ACM (centre console area), clock spring (steering column). Include yellow connector identification.

**Instructor Narration:**
> "At this station, you'll work through a checklist. Find and identify each component on the actual vehicle. The driver airbag is in the steering wheel — look for the 'SRS' or 'AIRBAG' marking on the cover. The passenger airbag is behind a panel in the upper dashboard — you'll see a 'PASSENGER AIRBAG' label. Side airbags are in the outboard seat bolsters or in the door trim — look for a tag sewn into the seat fabric.
>
> Curtain airbags are hidden behind the roof headliner, running from the A-pillar to the C-pillar. You won't see them directly, but you'll see the deployment seam in the headliner — a stitched line where the fabric tears when the curtain deploys.
>
> Crash sensors are small units bolted to the front bumper beam area and the B-pillars. They'll have a yellow or orange connector — the universal colour code for SRS circuits. The ACM is usually under the centre console between the front seats or behind the centre stack. The clock spring is at the top of the steering column, behind the steering wheel.
>
> Record the location of each component on your worksheet."

**PPT Content:**
```
STATION 1: AIRBAG COMPONENT IDENTIFICATION

Find and record the location of:

AIRBAG MODULES:
  [ ] Driver frontal — steering wheel centre
  [ ] Passenger frontal — upper dashboard (look for label)
  [ ] Side torso left — seat bolster or door (look for fabric tag)
  [ ] Side torso right — seat bolster or door
  [ ] Curtain left — roof rail A-pillar to C-pillar (find deployment seam)
  [ ] Curtain right — roof rail
  [ ] Knee left — under dashboard (driver side)
  [ ] Knee right — under dashboard (passenger side, if equipped)

SENSORS & CONTROL:
  [ ] Front crash sensor left — front bumper beam area
  [ ] Front crash sensor right — front bumper beam area
  [ ] Side crash sensor left — B-pillar
  [ ] Side crash sensor right — B-pillar
  [ ] Airbag Control Module (ACM) — centre tunnel / console
  [ ] Clock spring — steering column (behind steering wheel)

IDENTIFICATION TIP:
  Yellow/orange connectors = SRS (airbag) circuit
  Look for SRS, AIRBAG, or airbag symbol labels
  Deployment seams in headliner = curtain airbag path
```

---

#### Slide 25: Station 2 & 3 — ADAS Sensors and Scan Tool Diagnostics
**Visual:** Split slide. Left half: Vehicle exterior showing ADAS sensor locations — forward camera (behind windscreen), forward radar (front grille/bumper), corner radars (rear bumper corners), ultrasonic sensors (front and rear bumpers — small circular sensors), surround-view cameras (front grille, rear plate area, side mirrors). Right half: Scan tool screenshot showing the SRS/Airbag module with DTC list and crash event data.

**Instructor Narration:**
> "Station 2: locate every ADAS sensor on the vehicle. The forward camera is behind the windscreen, near the rear-view mirror — you'll see a bracket and a small camera unit looking forward through the glass. The forward radar is behind the manufacturer's badge or a panel in the centre of the front bumper or grille — it may not be visible without removing a cover. Corner radars are behind the rear bumper corners. Ultrasonic sensors are the small circular discs in the bumper faces — typically four front and four rear. Surround-view cameras are tiny — check behind the front badge, under the side mirrors, and near the rear number plate.
>
> Station 3: plug the scan tool into the OBD-II port and access the SRS module. Read stored DTCs. You may see codes for occupant classification sensors, seatbelt buckle switches, or clock spring circuits — these are common on vehicles that haven't been in a crash. Check if the vehicle has any stored crash event data — some ACMs record a limited crash record including g-force readings, belt status, and deployment decisions. This data is valuable for understanding how the system works."

**PPT Content:**
```
STATION 2: ADAS SENSOR IDENTIFICATION

Find and record the location of:
  [ ] Forward camera — behind windscreen near rear-view mirror
  [ ] Forward radar — centre of front bumper/grille (may be hidden)
  [ ] Corner radar left — rear bumper corner
  [ ] Corner radar right — rear bumper corner
  [ ] Ultrasonic sensors front — small discs in front bumper (count them)
  [ ] Ultrasonic sensors rear — small discs in rear bumper (count them)
  [ ] Surround camera front — behind front badge or grille
  [ ] Surround camera rear — near number plate
  [ ] Surround camera left — under/on side mirror
  [ ] Surround camera right — under/on side mirror

STATION 3: SCAN TOOL — AIRBAG DIAGNOSTICS

Steps:
  1. Connect scan tool to OBD-II port
  2. Select SRS / Airbag module
  3. Read DTCs — record all codes with descriptions
  4. Check crash event data (if accessible)
  5. Read system status (all sensors communicating?)
  6. Check occupant classification status (front passenger)
  7. DO NOT clear codes without instructor approval

Common codes you may find:
  Occupant classification mat fault (seat pressure sensor)
  Seatbelt buckle switch (intermittent contact)
  Clock spring (open circuit — if steering wheel was removed)
```

---

#### Slide 26: Station 4 — Static Calibration Awareness
**Visual:** Photograph of a proper static calibration setup: vehicle centred on a level floor, calibration target board on an adjustable stand at a measured distance in front of the vehicle, laser alignment tools visible, scan tool connected. Include dimension callouts showing typical requirements (e.g., "target centre at vehicle centreline," "distance: 2.5 m from front axle," "target height: 700 mm from floor").

**Instructor Narration:**
> "At this station, I've set up a forward camera static calibration target board. Look at what's required. The vehicle is parked on a level floor. The target board is positioned at an exact distance from the vehicle — this manufacturer specifies 2.5 metres from the front axle centreline. The target must be at a specific height — in this case, 700 millimetres from the floor to the target centre. And the target must be perfectly square to the vehicle's centreline — not rotated, not tilted.
>
> Take a tape measure and verify these distances yourself. Now imagine this: what if the floor is sloped 1 degree? What if the target is 200 millimetres too far away? What if the vehicle has a heavy toolbox in the boot changing the ride height? Each of these errors translates to a calibration error that the camera will carry into every driving situation. AEB braking at the wrong distance. LKA steering toward the wrong lane position.
>
> This is precision work. It's not glamorous, but it is safety-critical and it is the growing area of workshop revenue. Every windscreen replacement on an ADAS-equipped vehicle requires this procedure."

**PPT Content:**
```
STATION 4: STATIC CALIBRATION AWARENESS

EXAMINE THE SETUP:
  Vehicle positioned on LEVEL floor
  Target board at EXACT distance (manufacturer-specified)
  Target height MEASURED from floor
  Target CENTRED on vehicle centreline
  Scan tool connected and calibration routine ready

YOUR TASK:
  1. Measure the distance from front axle to target — record it
  2. Measure the target height from floor — record it
  3. Check the target alignment to vehicle centreline
  4. Identify what could go wrong:
     — Floor not level?
     — Wrong tyre pressures (ride height change)?
     — Heavy load in boot?
     — Target not square to vehicle?
     — Dirty windscreen in front of camera?

TYPICAL SPECIFICATIONS (vary by manufacturer):
  Target distance: 1.5 - 3.5 m from front axle (model-dependent)
  Target height: 500 - 900 mm (model-dependent)
  Floor level tolerance: < 1 degree slope
  Tyre pressures: MUST be at specification

WORKSHOP BUSINESS REALITY:
  Forward camera calibration: 30-60 min labour
  Every ADAS-equipped windscreen replacement needs this
  Growing from ~10% of vehicles (2020) to ~90% (2030)
  Workshops without calibration equipment will lose this work
```

---

### **WRAP-UP: Consolidation & Day 35 Preview** (Slides 27-28, ~15 minutes)

---

#### Slide 27: What You Learned Today
**Visual:** Two-column summary — Passive Safety (left) and Active Safety/ADAS (right) — with key terms from the session

**Instructor Narration:**
> "Let's pull today together. You now understand two fundamentally different approaches to vehicle safety. Passive systems — airbags, seatbelts with pretensioners and load limiters, crumple zones, and the safety cell — protect you when a crash occurs. They're pyrotechnic, structural, and one-shot. Active systems — AEB, LKA, ACC, BSM — try to prevent the crash or reduce its severity. They use radar, cameras, lidar, and ultrasonic sensors, and they act through the ESC and EPS systems you already know.
>
> You can now identify every airbag component and every ADAS sensor on a vehicle. You understand why calibration is mandatory and what happens when it's skipped. And you've seen a real calibration setup and measured the critical dimensions.
>
> Tomorrow is our last day of Week 7. We'll bring together everything from this week — EV technology, HV safety, HVAC, and safety systems — in a practical review session. It's a good day to consolidate before Week 8's exam preparation."

**PPT Content:**
```
DAY 34 RECAP — YOU CAN NOW:

PASSIVE SAFETY:
  Name all airbag types and their deployment mechanism
  Explain the squib/initiator firing sequence
  Describe clock spring function and common failure symptoms
  Explain seatbelt pretensioner and load limiter operation
  Describe crumple zone and safety cell engineering

ACTIVE SAFETY / ADAS:
  Name the 5 core ADAS systems (AEB, LKA, ACC, BSM, RCTA)
  Explain how each system works (sensor + decision + actuator)
  Describe the 4 ADAS sensor types (radar, lidar, camera, ultrasonic)
  Distinguish static vs dynamic calibration
  List when calibration is mandatory
  Explain consequences of skipping calibration

PRACTICAL:
  Identify airbag components on a real vehicle
  Identify ADAS sensors on a real vehicle
  Read airbag DTCs with a scan tool
  Understand static calibration setup requirements
```

---

#### Slide 28: Day 35 Preview
**Visual:** Image showing a workshop with multiple workstations set up — suggesting a practical review/consolidation day. Include icons for EV, HV safety, HVAC, and safety systems.

**Instructor Narration:**
> "Tomorrow is Day 35 — the last day of Week 7 and our final session before exam preparation begins in Week 8. We'll run a Week 7 practical consolidation: EV component identification, HV safety procedures, HVAC system diagnosis, and safety system checks — all in a rotation format. It's your chance to cement everything from this week before we shift into review mode.
>
> Come prepared. Wear your PPE. Bring your notes from Days 31 through today. I'll be testing your hands-on skills as well as your knowledge. See you tomorrow."

**PPT Content:**
```
DAY 35 PREVIEW: WEEK 7 PRACTICAL CONSOLIDATION

Rotation through 4 workshop stations:
  Station A: EV component identification & HV safety procedures
  Station B: HVAC system — pressure readings & diagnostics
  Station C: Airbag & seatbelt system — identification & scan tool
  Station D: ADAS sensor identification & calibration awareness

BRING:
  PPE (safety glasses, gloves, closed-toe shoes)
  Notes from Days 31-34
  Your curiosity and questions

Week 8 begins after tomorrow — EXAM PREPARATION
Everything you've learned in 7 weeks comes together.
```

---

## Assessment Checkpoint

**Formative (not graded):**
- Verbal quiz during passive safety section: name all airbag types and their locations
- Component identification at Station 1: correctly locate at least 10 of 14 airbag components
- ADAS sensor identification at Station 2: correctly locate at least 8 of 10 sensors
- Calibration awareness: correctly measure target distance within 5 mm at Station 4
- Scan tool: successfully read and interpret at least 2 airbag DTCs

---

## Key Takeaways

1. Passive safety (airbags, seatbelts, crumple zones) protects DURING a crash; active safety (ADAS) prevents the crash
2. Airbag deployment is pyrotechnic, one-shot, and happens in 40 milliseconds — there is zero margin for error
3. The clock spring is the most common airbag-related workshop visit — airbag light plus horn failure is the signature symptom
4. Seatbelt pretensioners fire pyrotechnically to remove slack; load limiters then yield to reduce chest force
5. ESC is the foundation of all ADAS braking functions — AEB commands ESC to apply the brakes
6. ADAS uses four sensor types (radar, lidar, camera, ultrasonic) with different strengths and ranges
7. Sensor fusion combines multiple sensors for higher confidence than any single sensor alone
8. ADAS calibration is mandatory after windscreen replacement, bumper work, suspension changes, and alignment
9. Skipping calibration can cause AEB to brake for phantom targets or LKA to steer into oncoming traffic
10. ADAS calibration is a growing and essential workshop revenue stream

---

## Preparation for Day 35

**Instructor prep:**
- Set up four rotation stations for Week 7 consolidation practical
- Prepare station checklists covering EV, HV safety, HVAC, and safety systems
- Ensure all vehicles have batteries reconnected for HVAC and scan tool stations
- Prepare a brief Week 7 knowledge quiz (10-15 questions covering Days 31-34)
- Print rotation schedules and station worksheets for each learner group

**Learner prep:**
- Review notes from Days 31-34 (EV, HV safety, HVAC, safety systems)
- Wear full PPE: safety glasses, closed-toe shoes, workshop-appropriate clothing
- Bring workshop notebook with completed station worksheets from this week
