---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 8
week_title: "The Complete Technician"
day_number: 39
session_title: "Cross-System Diagnostic Scenarios"
duration_minutes: 180
theory_practice: "20:80"
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 39: Cross-System Diagnostic Scenarios
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (35 min theory/demonstration + 145 min practical scenarios)
**Approach:** Immersive Scenario-Based — The Real World Doesn't Tell You Which Chapter the Fault Is In
**PPT Target:** 22-25 slides (light on slides, heavy on scenarios)
**Week:** 8 of 8 — "The Complete Technician"

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Apply a structured 7-step diagnostic workflow to any vehicle complaint
- Diagnose faults that cross multiple vehicle systems simultaneously
- Interpret DTCs, freeze frame data, and live data in combination to isolate root causes
- Distinguish between primary faults and secondary/consequential faults
- Research Technical Service Bulletins (TSBs) and known issues as part of diagnostic process
- Document diagnostic findings using a professional repair order format
- Verify repairs completely: clear codes, road test, re-scan, confirm no new faults
- Explain the purpose and procedure of a Pre-Delivery Inspection (PDI)

**This is Day 39 of 40 — the MOST practical day of the entire program.** For 7 weeks learners studied individual systems. Today, the walls between systems come down. Faults do not respect chapter boundaries. A misfire might be a network fault. A battery drain might be a body module that refuses to sleep. An ABS light might kill cruise control and corrupt the speedometer. Today, learners stop being students and start being diagnosticians.

---

## Connection to Prior Knowledge

This session connects to EVERYTHING taught across 7 weeks:
- **Week 1:** Vehicle systems overview, multimeter basics, wiring diagrams
- **Week 2:** Electrical fundamentals, circuit types, CAN bus communication
- **Week 3:** Engine management, sensors, actuators, ignition and fuel systems
- **Week 4:** Cooling, lubrication, exhaust and emissions
- **Week 5:** Suspension, steering, brakes, ABS, ESC
- **Week 6:** Transmission, charging systems, hybrid/EV high-voltage
- **Week 7:** HVAC, airbags, body electronics, ADAS
- **Week 8 (Days 33-38):** Component testing, scan tool mastery, service procedures

**Bridge:** "For 7 weeks, I taught you systems one at a time. I gave you neat categories. The real world is not neat. Today, a customer walks in with a complaint. They don't say 'I have a CAN bus communication fault.' They say 'my car feels weird.' Your job is to turn 'feels weird' into a repaired vehicle. Let's begin."

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: The Shift from Student to Diagnostician** (Slides 1-4, ~10 minutes)

**Narrative Voice:** Direct, serious, motivating. This is the culmination of everything. Treat learners as colleagues now.

---

#### Slide 1: Title & The Moment of Transition
**Visual:** Split image — left side shows a textbook open to a chapter on engine management; right side shows a real workshop bay with a customer vehicle on the lift, scan tool plugged in, diagnostic report on screen. A clear visual line divides "learning" from "doing."

**Instructor Narration:**
> "Day 39. One day before your final review. And this is the day that matters most. Not because of an exam — because of what happens after. When you walk into a workshop as a qualified technician, nobody is going to hand you a textbook and say 'the fault is in Chapter 7.' A customer will walk in and say 'my engine light is on and my car shakes.' Or 'my brakes feel soft and something smells hot.' Or 'my battery died overnight for the third time.'
>
> Your job is to figure it out. Systematically. Efficiently. Without guessing, without throwing parts at the problem, and without missing something that kills the car — or worse, hurts someone. Today, you stop being a student and start being a diagnostician."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 8: The Complete Technician
Day 39: Cross-System Diagnostic Scenarios

"The real world doesn't tell you which chapter the fault is in."
```

---

#### Slide 2: Why Cross-System Thinking Matters
**Visual:** Diagram showing a single wheel speed sensor connected by lines to: ABS module, ESC module, speedometer, cruise control, transmission shift logic, and trip computer. One sensor, six systems affected.

**Instructor Narration:**
> "Here's a wheel speed sensor. Just one sensor, bolted to the hub. If it fails, what happens? ABS stops working — ABS warning light. ESC stops working — ESC warning light. The speedometer reads zero — because it gets speed from the ABS module. Cruise control disengages — because it needs vehicle speed. The transmission may shift erratically — because shift logic uses wheel speed data. The trip computer shows wrong fuel economy — because it calculates using distance.
>
> One sensor. Six symptoms across four different systems. If you diagnose each symptom individually, you'll waste hours. If you think cross-system, you find the common thread in five minutes. That's the difference between a parts-changer and a diagnostician."

**PPT Content:**
```
ONE FAULT, MANY SYMPTOMS

A single wheel speed sensor failure causes:
  ABS warning light              (Brake system)
  ESC/TCS warning light          (Stability system)
  Speedometer reads zero         (Instrument cluster)
  Cruise control inoperative     (Drivetrain management)
  Erratic transmission shifts    (Transmission system)
  Incorrect trip computer data   (Body electronics)

THINK CROSS-SYSTEM.
Find the common thread, not the individual symptoms.
```

---

#### Slide 3: The 7-Step Diagnostic Workflow
**Visual:** Vertical flowchart with 7 numbered steps, each in a distinct colour block. Arrows connect them sequentially but a looping arrow from Step 5 returns to Step 4 (indicating iterative testing). Step 7 has a bold border labelled "NEVER SKIP THIS."

**Instructor Narration:**
> "Before we touch a single scenario, burn this into your memory. Seven steps. Every time. No shortcuts.
>
> Step 1: Verify the complaint. Don't trust what the customer said — confirm it yourself. Road test. Demonstrate the fault. If you can't reproduce it, you can't diagnose it.
>
> Step 2: Check for DTCs. And I don't mean just the engine module. Scan ALL modules — engine, transmission, ABS, airbag, body, HVAC, all of them. A fault in one module often stores a code in three.
>
> Step 3: Analyse the data. DTCs give you a direction, not an answer. Look at freeze frame data — what were the conditions when the code set? Look at live data — what's happening right now? Compare what you see to what the specification says.
>
> Step 4: Research. Before you pick up a single tool, check TSBs — Technical Service Bulletins. Has the manufacturer already identified this problem? Check known issues, wiring diagrams, forum experience. Five minutes of research saves an hour of guessing.
>
> Step 5: Test and isolate. Now you use your tools — multimeter, oscilloscope, pressure gauge, whatever the fault demands. The goal is to pinpoint the exact faulty component. Not the system. Not the area. The component.
>
> Step 6: Repair. Replace, repair, reprogram, recalibrate — whatever it takes to fix the root cause.
>
> Step 7: Verify the repair. This is where amateurs stop and professionals continue. Clear all codes. Road test. Re-scan — are codes pending? Confirmed? Are there NEW codes you accidentally introduced? Monitor. Confirm. Document. Done."

**PPT Content:**
```
THE 7-STEP DIAGNOSTIC WORKFLOW

Step 1: VERIFY the customer complaint
        (Road test, demonstrate, reproduce)

Step 2: CHECK for DTCs
        (Scan ALL modules, not just engine)

Step 3: ANALYSE DTCs + freeze frame + live data
        (Direction, not answer)

Step 4: RESEARCH — TSBs, known issues, wiring diagrams
        (5 minutes of research saves 1 hour of guessing)

Step 5: TEST and ISOLATE
        (Pinpoint the faulty component)

Step 6: REPAIR
        (Fix the root cause, not the symptom)

Step 7: VERIFY the repair
        (Clear, road test, re-scan, confirm, document)

NEVER SKIP STEP 7.
```

---

#### Slide 4: Today's Plan — 6 Diagnostic Stations
**Visual:** Workshop floor plan diagram showing 6 numbered stations arranged around the workshop, each with a vehicle icon and a colour-coded symptom card. A rotation arrow shows the path between stations. A clock shows 20 minutes per station.

**Instructor Narration:**
> "Here's how today works. First, I'm going to walk you through two complex case studies as a class. I'll demonstrate cross-system thinking live. That's about 25 minutes.
>
> Then you rotate through 6 diagnostic stations. Twenty minutes per station, all 6. At each station you'll find a symptom card — just like a customer complaint on a repair order. You read it, you think, you test, you diagnose, you document. No help from me unless you're stuck. I'll circulate, observe, and coach — but this is YOUR diagnosis, not mine.
>
> Station 1: Misfire diagnosis. Station 2: Electrical drain. Station 3: Brake and ABS complaint. Station 4: HVAC performance. Station 5: Transmission shift quality. Station 6: Warning light investigation. Six real-world scenarios. Two hours of pure diagnostic work. Let's go."

**PPT Content:**
```
TODAY'S PLAN (180 minutes)

SETUP (10 min): The shift from student to diagnostician

DEVELOPMENT (25 min): 2 complex case studies — worked as class
  Case Study A: Misfire that's actually a network fault
  Case Study B: Battery drain from a body module not sleeping

PRACTICAL (120 min): 6 DIAGNOSTIC STATIONS — 20 min each
  Station 1: Misfire Diagnosis
  Station 2: Electrical Drain
  Station 3: Brake / ABS Complaint
  Station 4: HVAC Performance
  Station 5: Transmission Shift Quality
  Station 6: Warning Light Investigation

  Each station: Symptom card -> Think -> Test -> Diagnose -> Document

WRAP-UP (15 min): Verification best practices + Day 40 preview

NO SHORTCUTS. NO GUESSING. DIAGNOSE.
```

---

### **DEVELOPMENT: Complex Case Studies — Worked as Class** (Slides 5-12, ~25 minutes)

**Narrative Voice:** Methodical, investigative. Walk through each case study step by step, modelling the 7-step workflow in real time. Ask the class at each decision point before revealing the answer.

---

#### Slide 5: Case Study A — The Misfire That Isn't
**Visual:** Customer repair order card with handwritten complaint: "Engine shakes at idle, check engine light on. Started 2 days ago. No recent work done."

**Instructor Narration:**
> "Case Study A. The customer says: engine shakes at idle, check engine light is on, started two days ago. No recent service. What does your gut say? Misfire, right? Spark plug, ignition coil, injector — engine system stuff. Let's follow the workflow and see where it actually leads.
>
> Step 1: Verify. We start the engine. Yes — rough idle. Noticeable vibration. Check engine light is on, steady. Complaint confirmed.
>
> Step 2: Scan ALL modules. Not just the engine — I said ALL. Who wants to guess what we find?"

**PPT Content:**
```
CASE STUDY A: "Engine Shakes at Idle, Check Engine Light On"

STEP 1 — VERIFY:
  Engine started. Rough idle confirmed. CEL on (steady).
  Complaint verified.

STEP 2 — SCAN ALL MODULES:
  What do we expect to find?

  [Pause — ask the class]
```

---

#### Slide 6: Case Study A — The DTC Surprise
**Visual:** Scan tool screen showing multiple DTCs across two modules: ECM shows P0300 (Random/Multiple Cylinder Misfire), P0301 (Cylinder 1 Misfire), and U0100 (Lost Communication with ECM); the BODY MODULE shows U0100 (Lost Communication with ECM) and B1234 (CAN Bus Communication Fault).

**Instructor Narration:**
> "Here's what the scan tool shows. The ECM has P0300 — random misfire — and P0301 — cylinder 1 misfire. That's what we expected. But look — there's also a U-code. U0100: Lost Communication with ECM. And the body module ALSO has U0100 and a CAN bus communication fault.
>
> U-codes are NETWORK codes. They mean modules are losing communication with each other. Why would the ECM lose communication? And why would THAT cause a misfire?
>
> Think about it. The camshaft position sensor on this vehicle reports to a secondary module that feeds data to the ECM via CAN bus. If that CAN line has a fault — a broken wire, a corroded pin, a faulty termination resistor — the ECM loses cam position data. Without cam position, it can't synchronise injector timing properly. Random misfire. But the ROOT CAUSE isn't the engine — it's the network.
>
> If you replaced the spark plug on cylinder 1, what would happen? Nothing. The misfire would continue. You'd waste money and time. This is why you scan ALL modules and pay attention to U-codes."

**PPT Content:**
```
CASE STUDY A — DTC RESULTS:

ECM (Engine Control Module):
  P0300 — Random/Multiple Cylinder Misfire Detected
  P0301 — Cylinder 1 Misfire Detected
  U0100 — Lost Communication with ECM

BODY MODULE:
  U0100 — Lost Communication with ECM
  B1234 — CAN Bus Communication Fault

KEY INSIGHT:
  U-codes = NETWORK problem
  The misfire is a SYMPTOM of lost CAN communication
  ECM can't receive cam position data -> can't synchronise injection

  ROOT CAUSE: CAN bus wiring fault, NOT engine components

  Replacing spark plugs would fix NOTHING.
```

---

#### Slide 7: Case Study A — Root Cause and Resolution
**Visual:** Wiring diagram excerpt showing the CAN-High and CAN-Low lines running from a cam sensor sub-module to the ECM, with a red X marking a corroded connector at an inline splice behind the engine.

**Instructor Narration:**
> "Step 4: Research. TSB check shows the manufacturer has a known issue with this connector — water ingress from a faulty bonnet seal corrodes the CAN bus splice connector behind the engine. Step 5: Test. We measure CAN-High and CAN-Low resistance at the ECM connector — out of specification. We trace the wiring to the splice, find the corroded connector. Step 6: Repair the connector, seal the wiring. Step 7: Clear all codes. Start the engine — smooth idle. Road test — no misfire. Re-scan — zero DTCs in all modules. Repair complete. Document everything.
>
> What did this case teach us? Never assume a misfire is an engine fault. Scan everything. U-codes are your best friend — they point to the real story."

**PPT Content:**
```
CASE STUDY A — RESOLUTION:

STEP 3 — ANALYSE: U-codes point to CAN bus communication loss
STEP 4 — RESEARCH: TSB found — known connector corrosion issue
                    behind engine (water ingress from bonnet seal)
STEP 5 — TEST: CAN bus resistance at ECM connector: OUT OF SPEC
                Traced to corroded inline splice connector
STEP 6 — REPAIR: Clean connector, repair wiring, seal against water
STEP 7 — VERIFY: Clear all codes. Start engine — smooth idle.
                  Road test — no misfire. Re-scan — 0 DTCs.

LESSON: A "misfire" was actually a NETWORK fault.
        Scan ALL modules. U-codes reveal the real story.
```

---

#### Slide 8: Case Study B — The Battery That Dies Overnight
**Visual:** Customer repair order card: "Battery dead every morning. New battery fitted last week — same problem. Car is 3 years old. No aftermarket accessories."

**Instructor Narration:**
> "Case Study B. Battery dead every morning. Customer already replaced the battery — didn't help. No aftermarket radio, no dashcam, no phone charger left plugged in. Three-year-old car, still under extended warranty.
>
> Step 1: Verify. We charge the battery fully and let the car sit overnight in the workshop. Next morning — battery at 10.8 volts. Dead. Complaint verified.
>
> Now, what kills a battery overnight? A parasitic draw. Something is staying awake and draining current when the car should be sleeping. A healthy car in sleep mode draws 20 to 50 milliamps. If something is drawing 500 milliamps, it drains a 60-amp-hour battery in about 5 days — faster if the battery is already partially discharged.
>
> Step 2: Scan all modules. No DTCs stored. Interesting — no fault codes at all. So this isn't a sensor failure or a hard fault. It's a BEHAVIOUR fault. Something is doing its job correctly — but at the wrong time."

**PPT Content:**
```
CASE STUDY B: "Battery Dead Every Morning"

STEP 1 — VERIFY:
  Battery charged to 12.7V. Car locked and left overnight.
  Next morning: 10.8V. Complaint verified.

STEP 2 — SCAN ALL MODULES:
  No DTCs stored in any module.

  No codes = no hard fault
  This is a BEHAVIOUR problem — a module not sleeping.

Normal parasitic draw: 20-50 mA
Excessive draw: anything above 80 mA after 30-min sleep cycle

QUESTION: How do we find out WHAT is drawing the current?
```

---

#### Slide 9: Case Study B — Parasitic Draw Testing
**Visual:** Step-by-step parasitic draw test procedure: multimeter in series with battery negative terminal, set to amps (DC), fuse-pulling method illustrated with a fuse box diagram showing each circuit labelled.

**Instructor Narration:**
> "Step 5: Test. Here's the parasitic draw test procedure. Disconnect the battery negative cable. Connect your multimeter in series — red lead to the cable, black lead to the battery post, set to DC amps, 10-amp range to start. Close all doors, lock the car, and WAIT. This is critical — you must wait for all modules to enter sleep mode. Some cars take 20 to 45 minutes.
>
> Once the car is asleep, read the current. On this car, we see 480 milliamps. That's ten times what it should be. Something is wide awake.
>
> Now the detective work. We go to the interior fuse box and start pulling fuses one at a time while watching the ammeter. When we pull fuse number 23, the draw drops from 480 milliamps to 35 milliamps. Fuse 23 feeds the body control module — the BCM.
>
> The BCM is not sleeping. Why? Research shows this vehicle has a known software bug — after a specific infotainment update, the BCM fails to enter sleep mode because the infotainment system sends a periodic CAN wake-up message every 30 seconds. The BCM hears it, stays awake, and drains the battery.
>
> The fix? A BCM software re-flash. Not a new battery. Not a new alternator. A software update. This is the modern car."

**PPT Content:**
```
CASE STUDY B — PARASITIC DRAW TEST:

PROCEDURE:
  1. Disconnect battery negative cable
  2. Multimeter in SERIES (10A DC range)
  3. Close all doors, lock car, WAIT 20-45 minutes
     (All modules must enter sleep mode)
  4. Read current: 480 mA (should be <50 mA)
  5. Pull fuses one at a time, watching ammeter
  6. Fuse #23 pulled -> draw drops to 35 mA
  7. Fuse #23 = Body Control Module (BCM)

ROOT CAUSE: BCM not entering sleep mode
  Software bug: infotainment sends CAN wake-up every 30 sec
  BCM stays awake -> drains battery

FIX: BCM software re-flash (not new battery, not new alternator)

LESSON: Battery drain diagnostics require PATIENCE and METHOD.
        The fault was SOFTWARE, not hardware.
```

---

#### Slide 10: Multi-System Faults — More Examples
**Visual:** Four panels, each showing a different multi-system scenario with interconnection arrows:
1. ABS sensor fault affecting speedometer + cruise control
2. HVAC blend door fault causing engine to run rich
3. Transmission fault caused by a throttle position sensor
4. Airbag light caused by a seat occupancy sensor under a wet floor mat

**Instructor Narration:**
> "Before we go to the stations, let me give you four more examples of cross-system faults. These are the kinds of things that make experienced technicians valuable.
>
> First: An ABS light comes on. The customer also mentions the speedometer sometimes drops to zero and cruise control stopped working. One wheel speed sensor — three symptoms across three systems. The wheel speed sensor feeds the ABS module, which shares vehicle speed data with the instrument cluster and the engine management system for cruise control. Fix the sensor, all three problems disappear.
>
> Second: An HVAC blend door actuator is stuck, locking the heater on full. The cabin gets unbearably hot. But the engine also runs slightly rich. Why? Because on this car, the engine coolant temperature sensor is shared between the ECM and the HVAC controller. The stuck blend door causes excessive heat extraction from the coolant. The ECM reads a lower coolant temperature than actual and enriches the fuel mixture to compensate. HVAC fault causing an engine symptom.
>
> Third: A transmission that won't shift above third gear. The scan tool shows the transmission module is in limp mode. But the DTC points to a throttle position sensor signal fault. The transmission module uses throttle position to determine shift points. If the signal is implausible, the TCM protects the transmission by locking it in third gear. Root cause is in the engine system — symptom is in the transmission.
>
> Fourth: An airbag warning light. The DTC says passenger seat occupancy sensor fault. The technician pulls the seat out, checks the connector, finds — a soaking wet floor mat that's been leaking water into the seat connector for months, corroding the pins. A leaking windscreen seal dripped water onto the floor, which wicked up into the connector. Body fault causing a safety system fault.
>
> The lesson in all of these: follow the data, not the symptom."

**PPT Content:**
```
MULTI-SYSTEM FAULT EXAMPLES:

1. ABS light + speedometer zero + cruise control dead
   ROOT: Wheel speed sensor failure
   Systems: Brakes, instrument cluster, drivetrain management

2. HVAC stuck on hot + engine running rich
   ROOT: Blend door actuator stuck — shared coolant temp sensor
   Systems: HVAC, engine management

3. Transmission locked in 3rd gear (limp mode)
   ROOT: Throttle position sensor signal fault
   Systems: Engine management, transmission

4. Airbag warning light
   ROOT: Water ingress from windscreen seal corroding
         seat occupancy sensor connector
   Systems: Body, SRS (airbag)

THE LESSON: Follow the DATA, not the symptom.
```

---

#### Slide 11: The Power of Freeze Frame Data
**Visual:** Scan tool freeze frame display showing: RPM 2,200, Vehicle Speed 95 km/h, Engine Coolant Temp 104 C, Intake Air Temp 42 C, Fuel Trim +18%, Engine Load 78%, Time Since Start 22 min, DTC Trigger: P0171 System Too Lean. Key values highlighted with annotations.

**Instructor Narration:**
> "When a DTC sets, the ECU captures a snapshot of operating conditions at that exact moment. This is freeze frame data, and it is incredibly valuable.
>
> Look at this example. P0171 — System Too Lean. The freeze frame shows it happened at 2,200 RPM, 95 km/h, engine temp 104 degrees — so it's warmed up, on the highway, under load. The fuel trim is +18% — the ECU is adding 18% extra fuel to compensate for a lean condition, and it's still not enough. Engine load is 78%.
>
> This tells me the lean condition happens under LOAD at highway speed, not at idle. That rules out a vacuum leak at the intake manifold — that would show up at idle. This points to a fuel delivery problem under load — a weak fuel pump, a clogged fuel filter, or a failing fuel pressure regulator. The freeze frame just narrowed my search area by 80%.
>
> Always read freeze frame data. It tells you WHEN and HOW the fault occurs, not just WHAT the code is."

**PPT Content:**
```
FREEZE FRAME DATA — THE "WHEN" AND "HOW"

DTC: P0171 — System Too Lean (Bank 1)

FREEZE FRAME SNAPSHOT:
  RPM:                2,200
  Vehicle Speed:      95 km/h       <- Highway cruising
  Engine Coolant:     104 C         <- Fully warmed up
  Intake Air Temp:    42 C          <- Normal
  Fuel Trim (LTFT):   +18%          <- ECU adding 18% extra fuel
  Engine Load:        78%           <- Under significant load
  Time Since Start:   22 min        <- Not a cold-start issue

ANALYSIS:
  Lean under LOAD at highway speed (not at idle)
  Rules out: intake vacuum leaks (would show at idle)
  Points to: fuel delivery problem under demand
  - Weak fuel pump?
  - Clogged fuel filter?
  - Failing fuel pressure regulator?

  Freeze frame narrowed the search by 80%.
```

---

#### Slide 12: Post-Repair Verification — The Professional Standard
**Visual:** Checklist styled as a professional verification form: Clear codes, Start engine, Road test (minimum 15 minutes, all driving conditions), Re-scan all modules, Check for pending codes, Check for confirmed codes, Check for new codes, Verify original complaint resolved, Document findings. A red stamp at the bottom reads "REPAIR COMPLETE" with date and technician signature lines.

**Instructor Narration:**
> "Step 7 is what separates a professional technician from everyone else. I've seen technicians replace a part, see the light go off, and hand the keys back. Three days later, the customer returns with the same problem — or worse, a new one the repair caused.
>
> Here's the professional standard. Clear all DTCs from all modules. Start the engine. Road test for a minimum of 15 minutes, including city driving, highway if possible, stops and starts, hard acceleration, and braking. Come back, plug in the scan tool, and re-scan ALL modules. Look for three things: pending codes, confirmed codes, and — critically — NEW codes that were not there before.
>
> A pending code means the ECU has seen the fault condition once but hasn't confirmed it yet. Give it another drive cycle. If it becomes confirmed, your repair didn't work. If it clears, you're good.
>
> New codes mean your repair may have disturbed something else — a connector left unplugged, a hose left disconnected, a sensor knocked loose.
>
> Document everything. What the customer complained about. What you found. What you did. What the verification showed. This is your professional record. If there's ever a warranty claim or a legal question, your documentation is your defence."

**PPT Content:**
```
POST-REPAIR VERIFICATION — THE PROFESSIONAL STANDARD

After EVERY repair:

  1. Clear ALL DTCs from ALL modules
  2. Start engine, check for immediate warning lights
  3. Road test — minimum 15 minutes
     - City driving (stops, starts, turns)
     - Highway speed (if accessible)
     - Hard acceleration and braking
  4. Return to workshop, re-scan ALL modules
  5. Check for:
     PENDING codes    -> Fault seen once, not yet confirmed
     CONFIRMED codes  -> Fault still present (repair failed?)
     NEW codes        -> Something disturbed during repair?
  6. Verify original complaint is resolved
  7. Document: Complaint -> Found -> Caused -> Corrected -> Verified

  NEVER hand keys back without Step 7 complete.
```

---

### **PRACTICAL: 6 Diagnostic Scenario Stations** (Slides 13-19, ~120 minutes)

**Narrative Voice:** Brief station setup instructions only. The slides are reference cards displayed at each station. Learners work independently or in pairs. Instructor circulates, coaches, observes.

**Logistics:** 6 stations, 20 minutes each. Learners rotate through ALL 6 stations. Use a visible timer. Sound a horn or bell at each 20-minute mark. Each station has a laminated symptom card, the necessary tools, and a diagnostic worksheet to complete.

---

#### Slide 13: Station Rotation Overview
**Visual:** Large visible timer graphic with 6 colour-coded station numbers. Clear rotation path. Bold text: "20 MINUTES PER STATION. ALL 6 STATIONS. DOCUMENT EVERYTHING."

**Instructor Narration:**
> "Listen up. Six stations. Twenty minutes each. When the horn sounds, you move to the next station regardless of whether you've finished. This is real-world pressure — in a workshop, you don't have unlimited time on a job. You need to be efficient.
>
> At each station, you'll find a symptom card. Read it carefully. Apply the 7-step workflow. Use the tools provided. Document your findings on the diagnostic worksheet. I'm circulating but not rescuing — this is your diagnosis.
>
> If you get completely stuck, raise your hand and I'll give you one hint. One. After that, it's on you. Ready? Station 1 — go."

**PPT Content:**
```
6 DIAGNOSTIC STATIONS — ROTATION RULES

TIME: 20 minutes per station (hard stop at horn)
STATIONS: Complete ALL 6
TOOLS: Provided at each station
DOCUMENTATION: Fill in diagnostic worksheet at each station

AT EACH STATION:
  1. Read the symptom card (customer complaint)
  2. THINK — what systems could be involved?
  3. TEST — use the 7-step workflow and tools provided
  4. DIAGNOSE — identify the root cause
  5. DOCUMENT — complaint, findings, root cause, repair plan

ONE HINT per station if completely stuck. That's it.

MOVE WHEN THE HORN SOUNDS.
```

---

#### Slide 14: Station 1 — Misfire Diagnosis
**Visual:** Station card format — red header "STATION 1: MISFIRE DIAGNOSIS." Vehicle photo with bonnet open. Tool list on the side.

**Instructor Narration (pre-brief only, not during station):**
> "Station 1: Misfire. The symptom card describes a rough idle with a flashing check engine light. Your job is to determine which cylinder is misfiring and why. Is it ignition? Fuel? Compression? Or something else entirely? Use the scan tool, check live misfire counters, perform a relative compression test if available, inspect ignition components. The answer may not be what you expect."

**PPT Content (displayed at station):**
```
STATION 1: MISFIRE DIAGNOSIS

CUSTOMER COMPLAINT:
"Car shakes at idle and the engine light is flashing.
It's worse when it's cold. I smell fuel sometimes."

VEHICLE: [As configured by instructor]

TOOLS PROVIDED:
  - Scan tool
  - Spark plug socket and ratchet
  - Ignition coil puller
  - Multimeter
  - Inspection mirror and light

YOUR TASK:
  1. Scan for DTCs — which cylinder(s)?
  2. Check live data — misfire counters per cylinder
  3. Inspect ignition components (plugs, coils, wiring)
  4. Determine: Ignition fault? Fuel fault? Mechanical fault?
  5. Identify root cause and document repair plan

DOCUMENT YOUR FINDINGS ON THE WORKSHEET.

Time: 20 minutes
```

**Instructor Setup Notes (NOT on slide):**
- Pre-configure a deliberate fault: disconnect one ignition coil connector, or install a fouled/worn spark plug, or create a vacuum leak on one cylinder with a loosened hose.
- For advanced challenge: create a misfire caused by a jumped timing chain or low compression (if vehicle available with pre-existing condition).
- Ensure scan tool is pre-configured and ready at the station.

---

#### Slide 15: Station 2 — Electrical Drain (Parasitic Draw)
**Visual:** Station card format — orange header "STATION 2: ELECTRICAL DRAIN." Image of a multimeter connected in series at the battery. Tool list on the side.

**PPT Content (displayed at station):**
```
STATION 2: ELECTRICAL DRAIN (PARASITIC DRAW)

CUSTOMER COMPLAINT:
"My battery is dead every Monday morning after the weekend.
I just bought a new battery two weeks ago. The alternator
tested fine at the parts store."

VEHICLE: [As configured by instructor]

TOOLS PROVIDED:
  - Multimeter (10A DC range)
  - Fuse puller
  - Fuse map / circuit identification chart
  - Test leads with alligator clips
  - Timer (for module sleep cycle)

YOUR TASK:
  1. Connect multimeter in series with battery negative
  2. Close all doors, lock vehicle
  3. Wait for modules to sleep (observe current drop)
  4. Record total parasitic draw in milliamps
  5. If excessive: pull fuses one at a time to isolate the circuit
  6. Identify the module or circuit causing the drain
  7. Document: Draw amount, circuit identified, probable cause

REMEMBER: Normal = 20-50 mA. Problem = >80 mA after sleep.

DOCUMENT YOUR FINDINGS ON THE WORKSHEET.

Time: 20 minutes
```

**Instructor Setup Notes (NOT on slide):**
- Pre-configure a parasitic draw: leave a boot/trunk light switch stuck closed, or place a relay that stays energised (a relay buzzer box works for simulation), or leave a module connector partially engaged to prevent sleep.
- If time does not allow a full 30-minute sleep cycle, pre-set the vehicle to an already-sleeping state with the multimeter already in series, and have the learner measure and pull fuses.
- Provide a labelled fuse box diagram for the specific vehicle.

---

#### Slide 16: Station 3 — Brake / ABS Complaint
**Visual:** Station card format — yellow header "STATION 3: BRAKE / ABS COMPLAINT." Image of a brake caliper with a scan tool showing ABS DTCs.

**PPT Content (displayed at station):**
```
STATION 3: BRAKE / ABS COMPLAINT

CUSTOMER COMPLAINT:
"My ABS light is on, and I noticed the speedometer
sometimes flickers. The car also feels like it pulls
slightly to the left when braking."

VEHICLE: [As configured by instructor]

TOOLS PROVIDED:
  - Scan tool (with ABS module access)
  - Multimeter
  - Inspection mirror and light
  - Wheel speed sensor specifications (printed)
  - Torque wrench (for wheel nuts)

YOUR TASK:
  1. Scan ABS module for DTCs — which sensor / circuit?
  2. Check live data — wheel speed sensor readings at all 4 wheels
  3. Compare: Do all sensors read consistently? Any erratic signals?
  4. Visual inspection: sensor wiring, sensor gap, reluctor ring
  5. Measure sensor resistance and compare to specification
  6. Inspect brake components for pull cause (pad wear, caliper slide)
  7. Identify root cause — is the ABS light and the pull related?

NOTE: The speedometer + cruise control may also be affected.
      Think CROSS-SYSTEM.

DOCUMENT YOUR FINDINGS ON THE WORKSHEET.

Time: 20 minutes
```

**Instructor Setup Notes (NOT on slide):**
- Pre-configure: disconnect one wheel speed sensor connector, or damage/increase the sensor air gap with a shim, or apply a small magnet near the reluctor ring to create erratic signal.
- For the brake pull: pre-create a sticking caliper slide pin (leave one caliper bolt deliberately tight or contaminate a slide pin with incorrect grease) or have uneven pad wear visible.
- Ensure learners can access wheel speed sensor live data on the scan tool.

---

#### Slide 17: Station 4 — HVAC Performance
**Visual:** Station card format — green header "STATION 4: HVAC PERFORMANCE." Image of HVAC vent with a thermometer inserted. Blend door actuator visible in cutaway.

**PPT Content (displayed at station):**
```
STATION 4: HVAC PERFORMANCE

CUSTOMER COMPLAINT:
"The air conditioning works, but the air on the driver's
side is warm and the passenger side is cold. I turned the
temperature all the way down on both sides."

VEHICLE: [As configured by instructor]

TOOLS PROVIDED:
  - Scan tool (with HVAC module access)
  - Digital thermometer / IR temperature gun
  - Flashlight
  - HVAC actuator location diagram (printed)
  - Multimeter

YOUR TASK:
  1. Verify: Measure vent temperatures both sides (driver vs passenger)
  2. Scan HVAC module for DTCs
  3. Check live data — blend door positions, temperature commands
  4. Does the blend door actuator respond to commands? (bi-directional test)
  5. Listen for actuator motor clicking (failed motor or stripped gear)
  6. Check: Is this HVAC-only, or does it affect any other system?
  7. Identify root cause and document repair plan

THINK: Could a stuck blend door affect engine performance
       on a vehicle with a shared coolant temp sensor?

DOCUMENT YOUR FINDINGS ON THE WORKSHEET.

Time: 20 minutes
```

**Instructor Setup Notes (NOT on slide):**
- Pre-configure: disconnect the driver-side blend door actuator connector (simulates stuck blend door), or if an older vehicle with cable-operated blend door, physically block the blend door lever.
- If the vehicle has dual-zone climate control, this fault produces the classic "one side hot, one side cold" complaint.
- For advanced: set up a scenario where the stuck heater increases coolant heat extraction, slightly affecting engine temp readings.

---

#### Slide 18: Station 5 — Transmission Shift Quality
**Visual:** Station card format — blue header "STATION 5: TRANSMISSION SHIFT QUALITY." Image of a gear selector with a scan tool showing transmission DTCs and gear state live data.

**PPT Content (displayed at station):**
```
STATION 5: TRANSMISSION SHIFT QUALITY

CUSTOMER COMPLAINT:
"The car feels sluggish and won't shift past 3rd gear.
There's a warning light on the dashboard that looks
like a gear with an exclamation mark."

VEHICLE: [As configured by instructor]

TOOLS PROVIDED:
  - Scan tool (with TCM access)
  - Multimeter
  - Transmission fluid dipstick or inspection plug tools
  - Wiring diagram excerpt (TCM inputs)
  - Throttle position sensor specifications (printed)

YOUR TASK:
  1. Scan TCM (Transmission Control Module) for DTCs
  2. Check: Is the transmission in LIMP MODE? What triggered it?
  3. Check live data — current gear, requested gear, TPS signal
  4. Scan ECM as well — are there engine codes related to TPS/APP?
  5. Inspect transmission fluid level and condition (if accessible)
  6. Trace the DTC to its root cause: Is this a transmission fault
     or an INPUT SIGNAL fault from another system?
  7. Identify root cause and document repair plan

THINK: The transmission module makes decisions based on
       data it RECEIVES from other systems.

DOCUMENT YOUR FINDINGS ON THE WORKSHEET.

Time: 20 minutes
```

**Instructor Setup Notes (NOT on slide):**
- Pre-configure: introduce a throttle position sensor signal fault — either disconnect the TPS connector, or insert a resistance to create an implausible signal. This will cause the TCM to enter limp mode (3rd gear lock) as a protective measure.
- Alternatively: if a vehicle with low or degraded transmission fluid is available, use that as the scenario (different root cause, same symptom).
- Ensure learners can access both TCM and ECM data on the scan tool to discover the cross-system relationship.

---

#### Slide 19: Station 6 — Warning Light Investigation
**Visual:** Station card format — purple header "STATION 6: WARNING LIGHT INVESTIGATION." Image of a dashboard with multiple warning lights illuminated: check engine, ABS, airbag, tyre pressure.

**PPT Content (displayed at station):**
```
STATION 6: WARNING LIGHT INVESTIGATION

CUSTOMER COMPLAINT:
"I have three or four warning lights on my dashboard.
They all came on at the same time about a week ago.
The car drives fine otherwise."

VEHICLE: [As configured by instructor]

TOOLS PROVIDED:
  - Scan tool (full system scan capability)
  - Multimeter
  - Wiring diagrams (CAN bus topology)
  - Module location chart (printed)
  - Battery tester (if available)

YOUR TASK:
  1. Note exactly which warning lights are on
  2. Scan ALL modules — list every DTC in every module
  3. Look for PATTERNS — are multiple modules reporting U-codes?
  4. Identify: Is there a COMMON CAUSE for multiple lights?
  5. Check battery voltage and ground connections
  6. Check for CAN bus communication faults (U-codes)
  7. Determine: Is this multiple faults or ONE fault with
     multiple symptoms?

KEY QUESTION:
  What single failure could illuminate multiple warning lights
  simultaneously?

DOCUMENT YOUR FINDINGS ON THE WORKSHEET.

Time: 20 minutes
```

**Instructor Setup Notes (NOT on slide):**
- Pre-configure: create a low battery voltage condition (partially discharged battery or introduce resistance in a main ground cable) that causes multiple modules to lose communication or report under-voltage faults. This produces multiple warning lights from a single root cause.
- Alternatively: disconnect one CAN bus connection at a critical node, causing multiple U-codes across several modules.
- This station is designed to test the learner's ability to find ONE root cause behind MANY symptoms — the ultimate cross-system diagnostic skill.

---

### **WRAP-UP: Verification, PDI, and Consolidation** (Slides 20-24, ~15 minutes)

**Narrative Voice:** Reflective, professional, forward-looking. Bring the group back together after station rotations.

---

#### Slide 20: Station Debrief — What Did You Find?
**Visual:** Six columns, one per station, with space for learner-reported findings. Blank template for instructor to fill in live during debrief.

**Instructor Narration:**
> "Everyone back together. Let's debrief. Station by station — who wants to share what they found? Station 1 first: what was the misfire cause?"

**Instructor Action:** Go through each station rapidly (2 minutes per station). Ask a different learner for each station. Confirm the correct root cause. Highlight any group that found a cross-system connection. Praise systematic approach. Challenge anyone who jumped to conclusions.

**PPT Content:**
```
STATION DEBRIEF

Station 1 — Misfire:       Root cause: _______________
Station 2 — Elec. Drain:   Root cause: _______________
Station 3 — Brake/ABS:     Root cause: _______________
Station 4 — HVAC:          Root cause: _______________
Station 5 — Transmission:  Root cause: _______________
Station 6 — Warning Lights: Root cause: _______________

QUESTIONS:
  - Which station had a cross-system root cause?
  - Which station's fault would have been MISSED by scanning
    only the "obvious" module?
  - Which station required the most patience?
```

---

#### Slide 21: DTC Status — Pending vs. Confirmed vs. History
**Visual:** Three-row table showing DTC lifecycle stages with colour coding. Green = History/Stored (fault occurred in the past, not currently active). Yellow = Pending (fault seen once, awaiting confirmation). Red = Confirmed/Active (fault currently present and verified by ECU across multiple drive cycles). Arrows show progression between stages.

**Instructor Narration:**
> "A quick but critical topic before we close. Not all DTCs are equal. When a fault first occurs, the ECU stores it as a PENDING code. It's seen the fault once. After the next drive cycle, if the fault occurs again, the code becomes CONFIRMED — the ECU is sure now, and the warning light illuminates.
>
> After you repair the fault and clear the codes, the ECU starts fresh. On the next drive cycle, it runs its monitors. If the monitor passes — no fault detected — the code stays clear. If the fault reappears, you get a new pending code, and you know your repair didn't work.
>
> HISTORY codes are past faults that have self-cleared — the ECU detected the fault but then the problem went away. These are valuable for intermittent faults. Always check history codes — they tell you what the car has experienced in the past.
>
> When you do your post-repair verification, you want to see: ZERO confirmed codes, ZERO pending codes, and no NEW codes that weren't there before."

**PPT Content:**
```
DTC STATUS — KNOW THE DIFFERENCE

PENDING (Yellow):
  Fault detected ONCE. Awaiting second drive cycle confirmation.
  Warning light NOT yet illuminated.
  Action: Monitor — will it confirm or clear?

CONFIRMED / ACTIVE (Red):
  Fault verified across multiple drive cycles.
  Warning light ON.
  Action: Diagnose and repair.

HISTORY / STORED (Green):
  Fault occurred in the past but is not currently active.
  May have self-cleared or been intermittent.
  Action: Investigate — intermittent faults return.

AFTER REPAIR:
  Clear all codes -> Drive -> Re-scan
  Target: 0 confirmed, 0 pending, 0 new codes
```

---

#### Slide 22: Pre-Delivery Inspection (PDI) Awareness
**Visual:** Checklist-style graphic showing a new car being inspected by a technician at a dealership. Sections labelled: Fluid Levels, Tyre Pressures, Body/Paint Condition, All Electronics Function Test, Warning Lights Clear, Road Test, Documentation Complete.

**Instructor Narration:**
> "One more topic you'll encounter in the workshop: the Pre-Delivery Inspection, or PDI. When a new vehicle arrives at a dealership from the factory, it's not immediately ready for the customer. A technician performs a PDI to confirm the vehicle is in perfect condition before handover.
>
> You check every fluid level — oil, coolant, brake fluid, washer fluid. You verify tyre pressures match the door jamb specification. You inspect the entire body for shipping damage — scratches, dents, paint chips. You turn on every electronic system — lights, wipers, windows, mirrors, climate control, infotainment, parking sensors, cameras. You scan for DTCs — a brand-new car should have ZERO codes. And you road test: does it drive properly, shift smoothly, brake evenly, steer straight?
>
> PDI is one of the first tasks you may be assigned as a junior technician. It exercises every skill you've learned in this program. You're checking every system in the car, just like we did today."

**PPT Content:**
```
PRE-DELIVERY INSPECTION (PDI) — NEW VEHICLE CHECK

A PDI verifies a factory-new vehicle is ready for customer delivery.

CHECKLIST:
  FLUIDS:
    Engine oil level and condition
    Coolant level
    Brake fluid level
    Washer fluid level
    Transmission fluid (if accessible)

  TYRES:
    Pressures match door jamb specification (all 4 + spare)
    Visual inspection for shipping damage

  BODY & PAINT:
    Full walk-around: scratches, dents, chips, overspray
    Panel gaps even
    All trim secure

  ELECTRONICS FUNCTION TEST:
    All lights (headlights, brake, indicators, interior)
    Wipers all speeds + washer
    Windows, mirrors, central locking
    HVAC — heat and A/C both functional
    Infotainment — power on, sound, display
    Parking sensors / cameras (if equipped)
    Scan ALL modules: target = ZERO DTCs

  ROAD TEST:
    Engine starts and idles smoothly
    Transmission shifts properly (all gears)
    Brakes even, no pull, no noise
    Steering straight, no vibration
    No unusual noises

  DOCUMENTATION:
    PDI form completed and signed
    Odometer reading recorded
    Keys, manuals, spare wheel verified
```

---

#### Slide 23: The Complete Diagnostic Technician
**Visual:** A central figure of a technician surrounded by 8 spokes, each representing a skill area: Systems Knowledge, Electrical Skills, Scan Tool Mastery, Wiring Diagram Reading, Research & TSBs, Systematic Workflow, Repair Execution, Verification & Documentation. All spokes connect to the centre.

**Instructor Narration:**
> "Look at what you have now. Eight weeks ago, you couldn't name the eight vehicle systems. Today, you just diagnosed faults that cross three systems simultaneously using a structured workflow, a scan tool, live data, freeze frames, wiring knowledge, and research skills.
>
> You can read a wiring diagram. You can use a multimeter and a scan tool. You know the 7-step workflow. You know why you scan all modules, not just the one you suspect. You know the difference between a pending code and a confirmed code. You know that a misfire can be a network fault, a battery drain can be a software bug, and a transmission problem can be caused by a throttle sensor.
>
> That's not a student. That's a diagnostic technician."

**PPT Content:**
```
THE COMPLETE DIAGNOSTIC TECHNICIAN

You now have:

  SYSTEMS KNOWLEDGE — All 8 vehicle systems, how they interact
  ELECTRICAL SKILLS — Voltage, resistance, current, circuits
  SCAN TOOL MASTERY — DTCs, freeze frame, live data, bi-directional
  WIRING DIAGRAM READING — Trace circuits, find connectors, verify
  RESEARCH SKILLS — TSBs, known issues, specifications
  SYSTEMATIC WORKFLOW — 7 steps, every time, no shortcuts
  REPAIR EXECUTION — Component replacement, adjustment, programming
  VERIFICATION — Clear, road test, re-scan, document

  These skills work TOGETHER.
  No single skill is enough.
  ALL of them together = DIAGNOSTIC TECHNICIAN.
```

---

#### Slide 24: Day 40 Preview — Final Review & Exam Preparation
**Visual:** Image of a neat study desk with organised notes, a practice exam paper, a scan tool, and a cup of coffee. Calendar showing "Day 40" circled. Text: "Review. Prepare. Certify."

**Instructor Narration:**
> "Tomorrow is Day 40 — the final day. Here's what happens. We do a comprehensive review of the entire 8-week program. I'll highlight the topics most likely to appear on the TUV SUD certification exam. We'll do a practice exam under timed conditions. We'll review answers as a group. And I'll answer every single question you have left.
>
> Tonight, here's what I want you to do. Review the 7-step diagnostic workflow — write it from memory. Review DTC types — P-codes, B-codes, C-codes, U-codes. Review the systems you found hardest. Get a good night's sleep. Eat breakfast. Show up ready.
>
> You've done the work. Thirty-nine days of learning, practising, and building. Tomorrow we sharpen the edge. Then you certify."

**PPT Content:**
```
DAY 40 PREVIEW: FINAL REVIEW & EXAM PREPARATION

WHAT WE'LL DO:
  - Comprehensive review of all 8 weeks
  - Key topics for the TUV SUD certification exam
  - Practice exam under timed conditions
  - Group answer review
  - Open Q&A — ask anything

TONIGHT — PREPARE:
  Write the 7-step diagnostic workflow from memory
  Review DTC code types: P, B, C, U
  Revisit your weakest topic — give it 30 minutes
  Get a good night's sleep

39 days of building.
Day 40: sharpen and certify.
```

---

## Assessment Checkpoint

**Formative (during session):**
- Case Study A participation: Can the learner identify that U-codes indicate a network fault, not an engine fault?
- Case Study B participation: Can the learner describe the parasitic draw test procedure?
- Station diagnostic worksheets: Did the learner follow the 7-step workflow and correctly identify root causes?
- Station documentation quality: Are findings clear, logical, and complete?

**Assessment Criteria for Station Worksheets:**
| Criterion | Competent | Developing | Not Yet |
|-----------|-----------|------------|---------|
| Followed 7-step workflow | All steps documented | Some steps skipped | No structure visible |
| Scanned all relevant modules | Multi-module scan attempted | Only one module scanned | No scan performed |
| Correct root cause identified | Root cause matches setup | Close but incomplete | Wrong system targeted |
| Cross-system connections noted | Identified system interactions | Partially identified | Treated as single-system |
| Repair plan documented | Clear, specific, actionable | Vague or incomplete | Missing |
| Verification steps planned | Full verification described | Partial verification | Not mentioned |

---

## Key Takeaways

1. The 7-step diagnostic workflow is non-negotiable — follow it every time, on every job
2. Always scan ALL modules, not just the one you suspect — U-codes reveal hidden connections
3. Freeze frame data tells you WHEN and HOW a fault occurs — use it to narrow your search
4. Multi-system thinking is the difference between a parts-changer and a diagnostician
5. Post-repair verification (Step 7) is what separates professionals from amateurs — clear, drive, re-scan, document
6. A single component failure can produce symptoms across multiple systems — find the common thread
7. Patience in diagnostics saves time and money — five minutes of research prevents an hour of guessing
8. Document everything — your repair order is your professional record and your legal protection

---

## Preparation for Day 40

**Instructor prep:**
- Prepare comprehensive review slide deck covering all 8 weeks
- Print practice exam papers (timed format matching TUV SUD certification structure)
- Prepare answer key and review materials
- Have scan tool available for any live demonstrations during review
- Prepare a "top 20 most tested topics" summary handout
- Ensure exam logistics are confirmed: date, time, location, required ID, format

**Learner prep:**
- Review the 7-step diagnostic workflow — write it from memory without notes
- Review DTC code categories: P (powertrain), B (body), C (chassis), U (network)
- Revisit the system or topic they found most challenging — spend 30 minutes reviewing
- Bring all notes and worksheets from the 8-week program
- Get adequate rest before exam preparation day
