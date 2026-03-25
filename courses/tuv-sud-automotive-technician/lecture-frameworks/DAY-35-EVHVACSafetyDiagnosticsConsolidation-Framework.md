---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 7
week_title: "The Future — EV, HVAC & Safety"
day_number: 35
session_title: "EV, HVAC & Safety Diagnostics Consolidation"
duration_minutes: 180
theory_practice: "40:60"
exam_weight_marks: 16
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 35: EV, HVAC & Safety Diagnostics Consolidation
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (70 min theory/case study + 110 min practical/quiz)
**Approach:** Diagnostic Consolidation — Bring It All Together
**PPT Target:** 25-28 slides
**Week:** 7 of 8 — "The Future — EV, HVAC & Safety" (Week Finale)
**Exam Weight:** 16 marks

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Apply a structured diagnostic process to fault scenarios across hybrid/EV, HVAC, and safety systems
- Diagnose HV system isolation faults using insulation monitoring device (IMD) data and isolation resistance measurements
- Troubleshoot hybrid mode engagement failures by systematically evaluating HV battery SOC, contactors, inverter status, and motor readiness
- Diagnose HVAC faults including no-cooling, hot-on-one-side, and compressor non-engagement using a logical elimination sequence
- Identify root causes for airbag warning illumination including clock spring, connector, crash sensor, and module faults
- Explain why ADAS recalibration is mandatory after windscreen replacement and distinguish static from dynamic calibration
- Diagnose ACC malfunction caused by radar obstruction and apply the correct remedial action
- Complete 10 formative MCQs covering all Week 7 material with 70% or higher accuracy

**This is the final session of Week 7.** Learners have covered hybrid/EV architecture (Day 31), HV safety (Day 32), HVAC and emissions (Day 33), and safety systems/ADAS (Day 34). Today consolidates all four days through diagnostic reasoning. The emphasis is application, not new content.

---

## Connection to Prior Knowledge

Build from the complete Week 7 sequence:
- **Day 31:** Hybrid/EV architectures, PMSM motors, inverters, regenerative braking, HV battery packs
- **Day 32:** HV safety — 50V threshold, orange cables, LOTO procedure, HV PPE (Class 0 gloves), service disconnect, IMD
- **Day 33:** Refrigeration cycle (compressor-condenser-expansion valve-evaporator), blend doors, DPF vs catalytic converter, cabin filtration
- **Day 34:** Airbag system architecture, clock spring, SRS control module, seatbelt pretensioners, AEB, ACC, LKA, static vs dynamic calibration

**Bridge:** "This week you learned four massive technology areas — EV powertrains, HV safety, climate systems, and intelligent safety. Each day gave you the theory. Today you prove you can use it. A technician who knows facts but cannot diagnose is an encyclopedia, not a professional. Today you become the professional."

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: The Diagnostic Mindset** (Slides 1-4, ~10 minutes)

**Narrative Voice:** Direct, challenging, motivating. This is the week finale — raise the bar.

---

#### Slide 1: Title & Week 7 Finale
**Visual:** Split-screen image — left side shows an EV on a lift with orange HV cables visible; right side shows a diagnostic scan tool displaying multiple fault codes. Bold "WEEK 7 FINALE" banner across the top.

**Instructor Narration:**
> "Day 35. The last day of Week 7. This has been the most technically demanding week of the program. On Monday you learned how electric motors and inverters create silent torque. Tuesday, you learned that the same systems can kill you if you don't follow HV safety procedures. Wednesday, you tackled the refrigeration cycle and emissions control. Thursday, you met airbags, ADAS cameras, and radar.
>
> Today is different. Today there is no new theory. Today, I give you broken vehicles and you tell me what's wrong. This is diagnostics day — and it separates technicians from parts-changers."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 7 FINALE: EV, HVAC & Safety Diagnostics Consolidation
Day 35 of 40

"Theory tells you what SHOULD happen.
 Diagnostics tells you what DID happen — and why."

Exam weight: 16 marks
```

---

#### Slide 2: Week 7 Recap — What You've Learned
**Visual:** Four-quadrant diagram representing Days 31-34, each quadrant with an icon and key takeaway: EV powertrain, HV safety, HVAC/emissions, safety systems/ADAS.

**Instructor Narration:**
> "Let's ground ourselves. Day 31 — you learned that a hybrid has two power sources and an EV has one, that PMSM motors give maximum torque from zero RPM, and that the inverter converts DC battery power to AC motor power. Day 32 — you learned that anything above 50 volts AC or 60 volts DC can kill, that LOTO is non-negotiable, and that Class 0 gloves protect to 1,000 volts. Day 33 — compressor, condenser, expansion valve, evaporator — the refrigeration cycle. And DPF versus catalytic converter for emissions. Day 34 — airbag deployment in 30 milliseconds, clock springs that fail when you don't expect it, and ADAS cameras that go blind after a windscreen replacement.
>
> Four days of dense content. Now I want to see what stuck."

**PPT Content:**
```
WEEK 7 — YOUR KNOWLEDGE BASE

DAY 31: Hybrid & EV Powertrains
  Series | Parallel | Series-Parallel | BEV
  PMSM motors, inverters, HV battery, regen braking

DAY 32: HV Safety
  50V AC / 60V DC lethal threshold
  LOTO, service disconnect, Class 0 gloves (1,000V)
  Insulation Monitoring Device (IMD)

DAY 33: HVAC & Emissions
  Compressor -> Condenser -> Expansion Valve -> Evaporator
  Blend doors, cabin temp sensors, dual-zone control
  DPF (diesel), TWC (petrol), SCR (AdBlue)

DAY 34: Safety Systems & ADAS
  SRS: airbags, pretensioners, clock spring, crash sensors
  ADAS: AEB, ACC, LKA — camera + radar fusion
  Static vs dynamic calibration after component replacement
```

---

#### Slide 3: The Diagnostic Process — Your Weapon
**Visual:** Flowchart showing the structured diagnostic process: Customer Complaint -> Verify Symptom -> Read DTCs -> Analyse Data -> Form Hypothesis -> Test Hypothesis -> Confirm Fix -> Clear Codes -> Verify Repair

**Instructor Narration:**
> "Before we dive into cases, let me remind you of the process. Every diagnosis follows the same path. It starts with the customer complaint — what did they notice? Then you verify the symptom yourself. Never trust the description alone — check it with your own eyes and instruments. Next, read DTCs — the computer's version of events. Analyse the data — freeze frame, live data, known issues. Form a hypothesis — what do you think is wrong? Test it — measure, inspect, swap. Confirm the fix. Clear codes. Verify the repair under the same conditions that caused the complaint.
>
> Skip any step, and you're guessing. Guessing costs money, reputation, and sometimes safety."

**PPT Content:**
```
THE DIAGNOSTIC PROCESS — EVERY TIME, EVERY FAULT

1. CUSTOMER COMPLAINT — What did they experience?
2. VERIFY SYMPTOM — Can you reproduce it?
3. READ DTCs — What does the ECU say?
4. ANALYSE DATA — Freeze frame, live data, TSBs
5. FORM HYPOTHESIS — What could cause this?
6. TEST HYPOTHESIS — Measure, inspect, isolate
7. CONFIRM FIX — Does the repair resolve the fault?
8. CLEAR CODES — Reset all stored DTCs
9. VERIFY REPAIR — Drive/operate under fault conditions

SKIP A STEP = GUESS
GUESS = WRONG PART, WASTED TIME, UNHAPPY CUSTOMER
```

---

#### Slide 4: Today's Plan
**Visual:** Horizontal timeline showing four blocks: Case Studies (25 min), Diagnostic Stations (70 min), Week 7 Review & Quiz (30 min), Wrap-Up & Week 8 Preview (15 min). A small clock icon beside each block.

**Instructor Narration:**
> "Here's the plan. First, I walk you through four diagnostic case studies — one from each Day this week. I'll show you how an experienced technician thinks through each fault. Then you go to the workshop floor where I've set up four diagnostic scenario stations — you rotate through each one in teams. After that, we come back for the Week 7 review and 10 quiz questions covering everything from Monday through today. Finally, a preview of Week 8 — your final week."

**PPT Content:**
```
TODAY'S PLAN — 180 MINUTES

BLOCK 1 (25 min): Diagnostic Case Studies x 4
  — HV isolation fault
  — Hybrid mode not engaging
  — HVAC not cooling / hot one side
  — Airbag light ON + ADAS after windscreen

BLOCK 2 (70 min): Diagnostic Scenario Stations
  — 4 stations, 4 teams, 15-17 min per station + rotation

BLOCK 3 (30 min): Week 7 Review + 10 MCQs (formative)

BLOCK 4 (15 min): Wrap-Up + Week 8 Preview
```

---

### **DEVELOPMENT: Diagnostic Case Studies** (Slides 5-16, ~25 minutes)

**Narrative Voice:** Methodical, detective-like. Walk through each case as a reasoning exercise, not a lecture. Pause and ask learners to guess before revealing answers.

---

#### Slide 5: Case Study 1 — HV Isolation Fault
**Visual:** Dashboard photo showing a red HV warning triangle illuminated, alongside a diagram of the IMD (Insulation Monitoring Device) connected between the HV bus and vehicle chassis. A simplified HV circuit shows HV battery positive, HV battery negative, and chassis ground with insulation resistance measured between each bus and chassis.

**Instructor Narration:**
> "Case one. A customer brings in a 2023 BEV. The dashboard shows a high-voltage warning — a red triangle with a lightning bolt. The car has entered reduced power mode. They drove through deep water yesterday. What do you do?
>
> First — verify the symptom. Warning is still on, confirmed. Read DTCs — the scan tool shows a fault from the Insulation Monitoring Device: 'HV system isolation resistance below threshold.' The IMD continuously measures the resistance between the HV bus and the vehicle chassis. A healthy system reads above 500 ohms per volt — for a 400V system, that's at least 200 kilohms. This car is reading 35 kilohms. Something is leaking current to chassis.
>
> Now — where is the fault? This is where you think. Water ingress is the clue. The most common water entry points in the HV system are: the HV battery pack seals, the charge port connector, and the wiring harness connectors running underneath the vehicle. We check each one.
>
> Visual inspection reveals moisture inside the charge port connector housing. The seal has degraded. Water bridging the HV pins to the metal housing reduces insulation resistance. Replace the seal, dry the connector, retest. Isolation resistance returns to 620 kilohms. Fault cleared."

**PPT Content:**
```
CASE STUDY 1: HV ISOLATION FAULT

VEHICLE: 2023 BEV, 400V system
COMPLAINT: HV warning light, reduced power
HISTORY: Drove through deep water yesterday

DTC: "HV insulation resistance below minimum"
IMD READING: 35 kohm (minimum: 200 kohm for 400V system)
RULE: Minimum isolation = 500 ohm/V

DIAGNOSTIC PATH:
1. Confirm warning light active — YES
2. Read DTC — IMD isolation fault
3. Check IMD live data — 35 kohm (FAIL)
4. History: water event — suspect water ingress
5. Inspect HV water entry points:
   [ ] HV battery pack seals
   [ ] Charge port connector seal
   [ ] Underbody harness connectors
6. FOUND: Moisture in charge port — degraded seal
7. REPAIR: Replace seal, dry connector, retest
8. POST-REPAIR: 620 kohm — PASS

KEY PRINCIPLE: IMD protects you by detecting current leakage
to chassis BEFORE it becomes a shock hazard
```

---

#### Slide 6: Case Study 1 — IMD Explained
**Visual:** Diagram showing an IMD circuit: two resistive measurement paths from HV+ and HV- to chassis, with a switch alternating between them. Resistance values shown: healthy (>500 kohm) vs faulty (35 kohm). A callout explains: "The IMD pulses a test voltage between HV bus and chassis, measuring the return current to calculate insulation resistance."

**Instructor Narration:**
> "Let me make sure you understand the IMD. It works by injecting a small, safe test signal between the high-voltage bus and the vehicle chassis. If the insulation is perfect, no current flows — infinite resistance. As insulation degrades — moisture, chafed cable, damaged connector — current starts to leak through to chassis, and the measured resistance drops. Below the threshold, the IMD triggers a warning and the system may limit power or shut down entirely.
>
> Why does this matter? Because if a person touches the chassis while current is leaking from the HV bus, they become the path to ground. The IMD catches the problem before the person does. It is a safety system — treat it like one."

**PPT Content:**
```
INSULATION MONITORING DEVICE (IMD) — HOW IT WORKS

         HV Battery
         +  |  -
         |  |  |
    [HV+ bus] [HV- bus]
         |       |
    [IMD measures resistance to chassis]
         |       |
    -----+---+---+-----
             |
          CHASSIS (ground reference)

HEALTHY:  >500 ohm per volt = PASS
  400V system: >200 kohm
  800V system: >400 kohm

FAULTY:   Below threshold = WARNING
  Causes: Water ingress, chafed cable, damaged connector,
          cracked potting compound, contaminated HV component

IMD runs CONTINUOUSLY — even when vehicle is parked (some systems)
```

---

#### Slide 7: Case Study 2 — Hybrid Mode Not Engaging
**Visual:** Dashboard of a hybrid vehicle showing engine running but electric motor icon greyed out. A diagnostic tree diagram showing the four main checkpoints: HV Battery SOC, Contactor Status, Inverter Status, Motor Status.

**Instructor Narration:**
> "Case two. A parallel hybrid comes in. The customer says it never runs on electric anymore — the petrol engine starts immediately every time, even at low speed in the city where it should be in EV mode. The fuel consumption has increased noticeably.
>
> Verify the symptom. Start the vehicle — engine fires immediately. At low speed, the electric motor does not engage. Confirmed. Read DTCs — no stored fault codes. Interesting. No DTC means no hard failure — the system is choosing not to use the electric motor. Why?
>
> Check HV battery SOC. Live data shows SOC at 12%. The hybrid control module requires at least 20% SOC to permit EV mode. The battery never charges above 15% — even during deceleration when regenerative braking should be replenishing it. Now you follow the energy chain backwards. Is the motor generating during regen? Is the inverter commanding regeneration? Is the HV battery accepting charge?
>
> Battery temperature data shows 2 degrees Celsius. It's winter. The battery management system is protecting the cells by limiting charge acceptance at low temperatures. Additionally, the auxiliary cabin heater has been drawing significant power because the customer always runs maximum heat. The battery drains faster than it regenerates.
>
> This is not a defect. This is normal operation at the limits of the system's capability. The fix? Educate the customer. Pre-condition the cabin while plugged in. Expect reduced EV range in cold weather. Check that the battery cooling/heating system is functioning correctly — in this case, the battery heater is operational but the customer's usage pattern exceeds the system's capacity in extreme cold."

**PPT Content:**
```
CASE STUDY 2: HYBRID MODE NOT ENGAGING

VEHICLE: Parallel hybrid (HEV)
COMPLAINT: Never runs in EV mode, fuel consumption high
DTC: None stored

DIAGNOSTIC PATH:
1. Verify: Engine starts immediately, no EV mode — CONFIRMED
2. DTCs: None — system is CHOOSING not to use EV mode
3. Check HV battery SOC: 12% (minimum for EV mode: 20%)
4. Check regen braking: Functional but limited
5. Check battery temperature: 2°C — BMS limiting charge rate
6. Check auxiliary power draw: Max cabin heat = high drain
7. Battery heater: Operational but insufficient for conditions

ROOT CAUSE: Low ambient temperature + high cabin heat demand
  -> Battery SOC cannot maintain above EV mode threshold
  -> System defaults to engine-only operation (NORMAL BEHAVIOR)

RESOLUTION:
  - Customer education on cold-weather HEV limitations
  - Recommend pre-conditioning while plugged in (PHEV)
  - Verify battery heater function — OK
  - NOT A DEFECT — operating as designed
```

---

#### Slide 8: Case Study 2 — The Hybrid Decision Logic
**Visual:** Flowchart showing the hybrid control module decision tree: SOC check (>20%?) -> Battery temp check (>5C?) -> Motor temp check (OK?) -> Inverter ready? -> Driver demand low enough? -> ENGAGE EV MODE. Any "No" branch leads to "ENGINE MODE — EV NOT AVAILABLE."

**Instructor Narration:**
> "This is critical to understand. The hybrid control module makes a decision every fraction of a second: can I use the electric motor right now? It checks SOC, battery temperature, motor temperature, inverter readiness, and driver demand. If ANY condition fails, the system defaults to engine mode. There is no single fault — it's a chain of conditions.
>
> A good diagnostician doesn't just read codes. They understand decision logic. If there's no DTC, you must think like the control module. What data is it seeing? What thresholds is it applying? That's the difference between a parts-changer and a technician."

**PPT Content:**
```
HYBRID CONTROL MODULE — DECISION LOGIC

START: Can I use EV mode?
  |
  +--> HV Battery SOC > 20%? --NO--> ENGINE MODE
  |    YES
  +--> Battery temp > 5°C? --NO--> ENGINE MODE (charge limited)
  |    YES
  +--> Motor temp OK? --NO--> ENGINE MODE (motor protection)
  |    YES
  +--> Inverter ready? --NO--> ENGINE MODE (inverter fault)
  |    YES
  +--> Driver demand < EV power limit? --NO--> ENGINE + MOTOR
  |    YES
  +--> ENGAGE EV MODE

KEY INSIGHT: No DTC does NOT mean no problem
  It may mean the system is working correctly
  under conditions the customer doesn't understand
```

---

#### Slide 9: Case Study 3 — AC Not Cooling
**Visual:** A diagnostic decision tree for "AC blows warm air" with four branches: Compressor not engaging, Refrigerant low/empty, Condenser blocked, Blend door stuck on hot. Each branch shows the test method.

**Instructor Narration:**
> "Case three. Customer complaint: AC blows warm air. This is one of the most common HVAC complaints you'll see. Let's work through it systematically.
>
> Step one — verify. Turn AC on, max cold, blower on high. Feel the air from the vents. Warm. Confirmed. Now — four main possibilities. The compressor isn't engaging. The refrigerant is low or gone. The condenser is blocked and can't reject heat. Or the blend door is stuck on the hot position, mixing heater core air into the AC output.
>
> Check the compressor first. Engine running, AC on — look at the compressor clutch. Is it spinning? In this case, it is NOT engaging. The clutch just sits there. Why? Two common reasons: low refrigerant pressure has tripped the low-pressure cut-out switch, or there is an electrical fault to the clutch.
>
> Check refrigerant pressure with manifold gauges. Low side reads nearly zero, high side reads nearly zero. The system is empty. Refrigerant has leaked out. The low-pressure switch correctly prevents the compressor from running on an empty system — running it dry would destroy the compressor.
>
> Now find the leak. UV dye inspection reveals a leak at the condenser — a stone chip has punctured a tube. Replace the condenser, replace the receiver-drier, evacuate the system, leak-test under vacuum, recharge with the correct weight of R-1234yf per spec sheet, add UV dye, test. Cold air from the vents. Done."

**PPT Content:**
```
CASE STUDY 3: AC NOT COOLING

VEHICLE: 2021 sedan
COMPLAINT: AC blows warm air
CONDITIONS: Ambient 32°C, blower working, engine running

DIAGNOSTIC PATH:
1. Verify: AC on, max cold, blower high — warm air CONFIRMED
2. Visual: Compressor clutch NOT engaging
3. Check refrigerant pressures:
   Low side: ~0 bar | High side: ~0 bar = SYSTEM EMPTY
4. Low-pressure switch: Open (correct behavior — protects compressor)
5. UV dye inspection: Leak at condenser — stone damage

REPAIR SEQUENCE:
  1. Replace condenser (stone chip damage)
  2. Replace receiver-drier (always with condenser)
  3. Evacuate system (vacuum pump, 30 min minimum)
  4. Leak test under vacuum (hold test)
  5. Recharge: 550g R-1234yf (per vehicle spec)
  6. Add UV dye for future leak detection
  7. Verify: Vent temperature 4-8°C at center vent

REFRIGERATION CYCLE REMINDER:
Compressor -> Condenser -> Expansion Valve -> Evaporator
(compress)   (reject heat) (pressure drop)  (absorb heat)
```

---

#### Slide 10: Case Study 3B — HVAC Blowing Hot on One Side
**Visual:** Dual-zone HVAC diagram showing left and right blend door actuators, left and right temperature sensors, and the HVAC control module. The left side is marked "COLD OK" and the right side is marked "HOT — FAULT."

**Instructor Narration:**
> "Quick bonus case — same family, different symptom. Customer says the driver side blows cold as set, but the passenger side blows hot regardless of the temperature setting. Dual-zone climate control vehicle.
>
> In dual-zone systems, each side has its own blend door actuator — a small electric motor that positions a flap to mix hot air from the heater core with cold air from the evaporator. Each side also has its own cabin temperature sensor.
>
> Diagnostic steps: command the passenger side to full cold via the scan tool. Listen for the actuator — can you hear it moving? In this case, no movement. Check the actuator electrically — power and ground present, but the motor does not turn. The blend door actuator on the passenger side has failed mechanically — the internal gears have stripped. The door is stuck in the full-hot position.
>
> Replace the passenger blend door actuator. Recalibrate the HVAC system — most systems require a calibration routine after actuator replacement so the control module learns the full range of travel. Test — both sides now respond independently. Done."

**PPT Content:**
```
CASE STUDY 3B: HVAC HOT ON ONE SIDE (DUAL-ZONE)

VEHICLE: Dual-zone climate control
COMPLAINT: Passenger side blows hot regardless of setting
DRIVER SIDE: Works correctly

DIAGNOSTIC PATH:
1. Command passenger side to full cold via scan tool
2. Listen for blend door actuator movement — NONE
3. Check actuator electrical supply — power + ground OK
4. Actuator motor: No rotation — MECHANICAL FAILURE
5. Inspect: Internal gear teeth stripped — door stuck HOT

REPAIR:
  1. Replace passenger blend door actuator
  2. Perform HVAC calibration routine (scan tool)
  3. Verify: Both zones respond independently

KEY LESSON: Dual-zone = two independent actuators
  If one side fails, the other usually works fine
  Scan tool bidirectional control is essential for testing
```

---

#### Slide 11: Case Study 4A — Airbag Warning Light ON
**Visual:** Instrument cluster showing the airbag (SRS) warning light illuminated. Below it, a diagram of the SRS circuit showing the control module, driver airbag (clock spring connection), passenger airbag, side airbags, crash sensors, and seatbelt pretensioners. Callout boxes highlight common failure points: clock spring, under-seat connector, crash sensor, control module.

**Instructor Narration:**
> "Case four. The airbag warning light is on. The customer noticed it after having the steering wheel removed to replace the indicator stalk. This is a strong clue.
>
> Read the DTCs. The scan tool shows: 'Driver airbag — circuit resistance high.' That tells us the SRS module sees excessive resistance in the path to the driver's airbag. Think of it as a chain: the SRS module sends a monitoring signal through wiring, through the clock spring in the steering column, through the connector to the driver airbag inflator, and back. If resistance is too high, the module cannot guarantee it can fire the airbag in a crash.
>
> The history says the steering wheel was removed. What lives between the steering column and the steering wheel? The clock spring — that coiled ribbon cable that allows electrical connection while the wheel rotates. If the clock spring was not centred before the steering wheel was reinstalled, or if the connector was not fully seated, you get high resistance.
>
> Inspection reveals the clock spring connector is not fully latched. Reseat the connector — click it into place. Clear the DTC, turn the ignition off and on, and the airbag light is off. But — important — if the clock spring was rotated beyond its limit during removal, it may be internally damaged even if the connector is good. Always verify by checking resistance across the clock spring with the steering at full lock both ways."

**PPT Content:**
```
CASE STUDY 4A: AIRBAG WARNING LIGHT ON

VEHICLE: 2020 sedan
COMPLAINT: Airbag light on after steering wheel removal/reinstall
DTC: "Driver airbag — circuit resistance high"

SRS CIRCUIT: Module -> Wiring -> Clock Spring -> Airbag Inflator

CLOCK SPRING — The Critical Link:
  A coiled flat cable inside the steering column
  Allows electrical connection while steering wheel rotates
  MUST be centred during installation
  Exceeding rotation limit = internal damage

DIAGNOSTIC PATH:
1. DTC points to driver airbag circuit — high resistance
2. History: steering wheel recently removed
3. Suspect: clock spring connector or clock spring itself
4. Inspect: Connector not fully latched — FOUND
5. Reseat connector (ensure full click)
6. Clear DTC, cycle ignition
7. Airbag light OFF — RESOLVED
8. VERIFY: Measure clock spring resistance at full lock L/R
   (resistance should remain constant through full steering range)

CAUTION: Always disconnect 12V battery and wait 60 seconds
         minimum before working near airbag components
```

---

#### Slide 12: Case Study 4A — Other SRS Failure Points
**Visual:** Three photos arranged horizontally: (1) An under-seat SRS connector with corrosion visible on pins, (2) A front crash sensor mounted behind the bumper beam showing physical damage, (3) An SRS control module removed from under the centre console. Each photo has a brief label describing the failure mode.

**Instructor Narration:**
> "The clock spring is the most common SRS fault after steering work, but it is not the only one. Under-seat connectors are another frequent culprit. The seat moves constantly — forward, backward, reclined — and the SRS connector underneath can work loose or corrode. DTC will say 'side airbag circuit resistance high' or 'occupant classification sensor fault.' Inspect the yellow SRS connector under the seat. Unplug, check for corrosion or bent pins, reseat.
>
> Crash sensors mounted behind the bumper beam can suffer physical damage in minor collisions that don't deploy the airbags — a parking lot bump that dents the bumper but shifts the sensor. The module itself can fail, though this is rare and usually only after a flood or major electrical event.
>
> The golden rule: SRS faults always come with a DTC. The DTC tells you which circuit is affected. Follow the circuit — connector by connector — until you find the resistance fault."

**PPT Content:**
```
OTHER COMMON SRS FAILURE POINTS

1. UNDER-SEAT CONNECTOR
   Symptom: Side airbag or seat occupancy fault
   Cause: Connector loosened by seat movement, corrosion
   Fix: Inspect, clean, reseat — replace if damaged

2. CRASH SENSOR (bumper-mounted)
   Symptom: Front/rear crash sensor circuit fault
   Cause: Minor impact shifted sensor, water ingress
   Fix: Inspect mounting, check resistance, replace if damaged

3. SRS CONTROL MODULE
   Symptom: Multiple SRS faults, internal module error
   Cause: Water damage (floor flooding), internal failure
   Fix: Replace module, configure VIN, calibrate

4. SEATBELT PRETENSIONER CONNECTOR
   Symptom: Pretensioner circuit fault
   Cause: Connector not seated after seat removal/carpet work
   Fix: Reseat connector

RULE: SRS faults ALWAYS have a DTC
      The DTC tells you WHICH circuit — follow it
```

---

#### Slide 13: Case Study 4B — ADAS Malfunction After Windscreen Replacement
**Visual:** Photo of a forward-facing ADAS camera mounted behind the rear-view mirror on the interior of a windscreen, with alignment target boards visible through the windscreen in a workshop setting. A warning message on the instrument cluster reads: "Front Assist not available — system calibration required."

**Instructor Narration:**
> "Case four, part B. A customer had their windscreen replaced after a stone chip turned into a crack. The replacement was done at a glass specialist. Two days later, the customer notices multiple warnings: 'Front Assist not available,' 'Lane Assist not available,' 'Traffic sign recognition inactive.' All ADAS functions using the forward camera are offline.
>
> This is a textbook scenario. The forward-facing camera is bonded to the inside of the windscreen. When the windscreen is replaced, the camera is removed and remounted. Even a fraction of a degree of angular difference changes where the camera 'looks' — and at highway speeds, that fraction of a degree translates to metres of error at 100 metres distance.
>
> The camera MUST be recalibrated after windscreen replacement. There are two methods: static calibration uses a precisely positioned target board in a controlled workshop environment — specific distance from the front axle, level floor, centred on the vehicle axis. Dynamic calibration requires driving the vehicle at a specific speed on a road with clear lane markings while the system self-corrects.
>
> Some vehicles require both — static first, then dynamic to fine-tune. The glass specialist should have known this. The fix: perform the appropriate calibration procedure using the manufacturer's scan tool and calibration equipment. Once complete, all ADAS functions return."

**PPT Content:**
```
CASE STUDY 4B: ADAS MALFUNCTION AFTER WINDSCREEN REPLACEMENT

VEHICLE: 2022 with front camera ADAS suite
COMPLAINT: AEB, LKA, traffic sign recognition all unavailable
HISTORY: Windscreen replaced 2 days ago

ROOT CAUSE: Forward camera not recalibrated after replacement
  Camera bonded to windscreen — removed and reinstalled
  Even <1° angular error = metres of targeting error at distance

CALIBRATION METHODS:

STATIC CALIBRATION:
  - Target board positioned precisely in front of vehicle
  - Controlled environment: level floor, specific distance
  - Scan tool commands calibration routine
  - Takes 20-40 minutes

DYNAMIC CALIBRATION:
  - Drive at specified speed (typically 60-100 km/h)
  - Clear lane markings required
  - System self-adjusts using real-world references
  - Takes 15-30 minutes of driving

SOME VEHICLES REQUIRE BOTH (static then dynamic)

FIX: Perform static + dynamic calibration per manufacturer procedure
RESULT: All ADAS functions restored
```

---

#### Slide 14: Case Study 4C — ACC Not Maintaining Distance
**Visual:** Photo of a vehicle front bumper with the radar sensor location marked. Inset photo shows dirt, ice, and road salt accumulated over the radar sensor area behind the bumper cover. A second inset shows the dashboard message: "ACC temporarily unavailable."

**Instructor Narration:**
> "One more quick ADAS scenario. Customer says ACC works sometimes, but intermittently shows 'ACC temporarily unavailable.' No consistent pattern — some days it works, some days it doesn't.
>
> ACC relies on a forward-facing radar sensor, typically mounted behind the front bumper cover or in the grille area. The radar emits microwave pulses and measures reflections to detect vehicles ahead. Anything that blocks or attenuates the radar signal will cause intermittent faults.
>
> The most common cause? Dirt, ice, or salt buildup on the bumper cover directly in front of the radar. In winter, this happens constantly. Some vehicles are more sensitive than others depending on bumper material and radar frequency.
>
> The diagnostic? Clean the bumper cover area in front of the radar sensor. If the fault clears, educate the customer: keep that area clean, especially in winter. If the fault persists after cleaning, check for physical damage to the bumper cover — even a minor deformation can affect radar transmission. Check the radar sensor mounting bracket for damage. And finally, check if the radar requires calibration — which is mandatory after front-end collision repair, bumper replacement, or sensor replacement.
>
> This is a five-minute diagnosis that saves the customer hundreds in unnecessary sensor replacement."

**PPT Content:**
```
CASE STUDY 4C: ACC NOT MAINTAINING DISTANCE

VEHICLE: 2021 SUV with adaptive cruise control
COMPLAINT: ACC intermittently unavailable — no pattern
DTC: "ACC radar signal quality insufficient" (intermittent)

RADAR SENSOR: Behind front bumper cover
  Emits microwave pulses, measures reflections
  ANYTHING blocking the signal = intermittent fault

MOST COMMON CAUSE: Dirt / ice / salt on bumper cover
  Especially in winter / wet conditions
  Some bumper materials more transparent to radar than others

DIAGNOSTIC PATH:
1. Clean bumper area in front of radar sensor
2. Clear DTC, test ACC — RESOLVED? -> Customer education
3. If persistent: Check bumper cover for damage/deformation
4. Check radar sensor mounting bracket alignment
5. Check if calibration needed (after front-end work)

CALIBRATION REQUIRED AFTER:
  - Front-end collision repair
  - Bumper cover replacement
  - Radar sensor replacement
  - Suspension height change (lowering/lifting)

COST OF MISDIAGNOSIS: $1,500+ radar sensor
COST OF CORRECT DIAGNOSIS: $0 (clean the bumper)
```

---

#### Slide 15: Diagnostic Case Studies — Summary
**Visual:** Table summarizing all four case studies in columns: Case, System, Root Cause, Key Diagnostic Step, Resolution. Clean, scannable layout for quick reference.

**Instructor Narration:**
> "Four cases, four different systems, four different root causes. Notice the pattern: every single one started with verifying the symptom and reading DTCs. Every one required understanding how the system works — not just what the parts are called. And in two cases — the hybrid and the ACC — the fix was not a part replacement at all. One was customer education, the other was cleaning the bumper.
>
> A good technician saves money by diagnosing correctly. A bad technician costs money by replacing parts until the symptom goes away. The exam will test your diagnostic reasoning. Let's put it into practice."

**PPT Content:**
```
DIAGNOSTIC CASE STUDY SUMMARY

CASE 1: HV Isolation Fault
  System: HV Battery / IMD
  Root Cause: Water ingress at charge port
  Key Step: IMD reading + visual inspection
  Fix: Replace seal, dry connector

CASE 2: Hybrid Mode Not Engaging
  System: Hybrid control / HV battery
  Root Cause: Low SOC due to cold + high heater demand
  Key Step: Live data — SOC, battery temp, power draw
  Fix: Customer education (not a defect)

CASE 3: AC Not Cooling / Hot One Side
  System: HVAC refrigeration / blend door
  Root Cause: Refrigerant leak (condenser) / actuator failure
  Key Step: Pressure check / scan tool actuator test
  Fix: Replace condenser + recharge / replace actuator

CASE 4: Airbag Light + ADAS Faults
  System: SRS / ADAS camera / radar
  Root Cause: Clock spring connector / calibration / dirt
  Key Step: DTC circuit ID / calibration check / visual
  Fix: Reseat connector / calibrate / clean bumper
```

---

#### Slide 16: Transition to Practical
**Visual:** Photo of a workshop with four clearly marked diagnostic stations, each with a different vehicle or simulation setup. Station numbers 1-4 are visible on floor stands. Learners in PPE are visible in the background.

**Instructor Narration:**
> "Time to apply what you've learned. I've set up four diagnostic stations in the workshop. Each station presents a fault scenario from this week's content. You'll work in teams of three or four. At each station, you'll find a scenario card describing the customer complaint, a vehicle or simulation setup, and the tools you need. Your job is to follow the diagnostic process, identify the root cause, and document your findings on the worksheet.
>
> You have 15 to 17 minutes per station, then you rotate. I'll be circulating to guide and challenge your thinking. Let's go."

**PPT Content:**
```
DIAGNOSTIC SCENARIO STATIONS — YOUR TURN

STATION 1: HV System — Insulation resistance measurement
  Tools: Insulation tester (simulated), scan tool
  Task: Identify which HV component has low isolation

STATION 2: Hybrid / EV Powertrain
  Tools: Scan tool with live data
  Task: Determine why EV mode is not engaging

STATION 3: HVAC Diagnostics
  Tools: Manifold gauges (simulated), scan tool
  Task: Diagnose no-cooling and/or one-side-hot fault

STATION 4: SRS + ADAS
  Tools: Scan tool, SRS circuit diagram
  Task: Identify airbag fault source + determine ADAS cal need

TIME: 15-17 minutes per station | ROTATE on instructor signal
DOCUMENT: Record findings on station worksheet
```

---

### **PRACTICAL: Diagnostic Scenario Stations** (Slides 17-18, ~70 minutes)

**Narrative Voice:** Coaching, Socratic questioning. Let teams struggle before guiding. Ask "Why?" frequently.

---

#### Slide 17: Station Rotation Schedule
**Visual:** Grid showing Teams A-D on rows and Stations 1-4 on columns, with time slots. Arrows show rotation direction. A countdown timer graphic indicates 17-minute windows.

**Instructor Narration:**
> "Here's your rotation. Team A starts at Station 1, Team B at Station 2, and so on. When I call 'rotate,' you move clockwise to the next station. At each station, read the scenario card first — don't touch anything until you've read it and discussed your diagnostic plan with your team. Then execute. Document your findings.
>
> Go."

**PPT Content:**
```
STATION ROTATION SCHEDULE

         Station 1    Station 2    Station 3    Station 4
         HV System    Hybrid/EV    HVAC         SRS/ADAS
Round 1  Team A       Team B       Team C       Team D
Round 2  Team D       Team A       Team B       Team C
Round 3  Team C       Team D       Team A       Team B
Round 4  Team B       Team C       Team D       Team A

TIME PER STATION: ~17 minutes
TOTAL PRACTICAL TIME: ~70 minutes (including transitions)

AT EACH STATION:
  1. READ the scenario card (2 min)
  2. DISCUSS diagnostic plan with team (2 min)
  3. EXECUTE diagnostics (10 min)
  4. DOCUMENT findings on worksheet (3 min)
```

**Instructor Notes:**
- Circulate between stations
- Ask probing questions: "Why did you check that first?" "What would you check next if this was normal?" "How does this connect to what we learned on Day 32?"
- If a team is stuck, guide with questions rather than answers
- Note common errors for the debrief

---

#### Slide 18: Station Debrief
**Visual:** Four-quadrant layout with space for instructor to write key findings from each station. "What went well" and "What to improve" columns for each.

**Instructor Narration:**
> "Everyone back to seats. Let's debrief. Station by station — what did you find, and what challenged you?"

**Instructor Action:**
- Call on one team per station to present their findings (2 minutes each)
- Correct any misunderstandings
- Highlight common errors observed during circulation
- Reinforce: "The diagnostic process works if you follow it. Every shortcut is a potential misdiagnosis."

**PPT Content:**
```
STATION DEBRIEF

Station 1 — HV System:
  Common finding: ________________________________
  Common error: __________________________________

Station 2 — Hybrid/EV:
  Common finding: ________________________________
  Common error: __________________________________

Station 3 — HVAC:
  Common finding: ________________________________
  Common error: __________________________________

Station 4 — SRS/ADAS:
  Common finding: ________________________________
  Common error: __________________________________

KEY TAKEAWAY: Follow the process. Check data before parts.
```

---

### **REVIEW & QUIZ: Week 7 Consolidation** (Slides 19-24, ~30 minutes)

**Narrative Voice:** Energetic review pace. Keep it moving. Build confidence before the quiz.

---

#### Slide 19: Week 7 Review — Hybrid & EV Powertrains
**Visual:** Comparison table of hybrid architectures: Series (engine drives generator only), Parallel (engine and motor both drive wheels), Series-Parallel (combines both modes), BEV (battery only). Each with a simple power flow diagram.

**Instructor Narration:**
> "Quick-fire review. Hybrid types. Series hybrid — the engine NEVER drives the wheels directly. It spins a generator that makes electricity. The electric motor alone drives the wheels. Think of a diesel-electric locomotive. Parallel hybrid — the engine AND the motor can BOTH drive the wheels. They share the same mechanical path. Series-parallel — does both, depending on conditions. Toyota's Synergy Drive is the classic example. BEV — no engine at all. Battery, inverter, motor, wheels. Done.
>
> PMSM motor — Permanent Magnet Synchronous Motor — the dominant EV traction motor. Why? High torque density, high efficiency, compact size, and it delivers maximum torque from zero RPM. No waiting for revs to build like a combustion engine.
>
> The inverter converts DC from the battery to three-phase AC for the motor. It also controls motor speed and torque by varying the frequency and amplitude of the AC waveform. Without the inverter, the motor is just an expensive paperweight."

**PPT Content:**
```
WEEK 7 REVIEW — HYBRID & EV POWERTRAINS

SERIES HYBRID:
  Engine -> Generator -> Electricity -> Motor -> Wheels
  Engine NEVER drives wheels directly

PARALLEL HYBRID:
  Engine -+-> Wheels
  Motor --+
  Both can drive wheels simultaneously or independently

SERIES-PARALLEL:
  Switches between series and parallel modes
  Most efficient but most complex

BEV (Battery Electric Vehicle):
  Battery -> Inverter -> Motor -> Wheels
  No engine, no exhaust, no gearbox (usually)

PMSM (Permanent Magnet Synchronous Motor):
  Max torque from 0 RPM | High efficiency | Compact
  Dominant EV traction motor technology

INVERTER: Converts DC battery -> AC motor
  Controls speed (frequency) and torque (amplitude)
```

---

#### Slide 20: Week 7 Review — HV Safety
**Visual:** Infographic showing the HV safety hierarchy: lethal voltage threshold, orange cable identification, LOTO procedure steps (1-Inform, 2-Identify, 3-Isolate, 4-Lock, 5-Prove dead, 6-Earth), HV glove classification table showing Class 00 through Class 4 with voltage ratings.

**Instructor Narration:**
> "HV safety — non-negotiable. The lethal threshold is 50 volts AC or 60 volts DC. Most EV systems operate at 400V to 800V. That is instantly lethal.
>
> Orange cables mean high voltage — never cut, probe, or disconnect them without following the LOTO procedure. LOTO: Lockout-Tagout. Inform colleagues, identify the energy source, isolate using the service disconnect, lock the disconnect in the open position with YOUR personal lock, prove the system is dead with a CAT III rated multimeter, and earth/ground the system where applicable.
>
> HV gloves: Class 0 is rated to 1,000V AC — this is the standard for most automotive HV work. They must be inspected before every use — inflate them, check for pinholes, check the date stamp. Expired gloves are not PPE, they're false confidence. Always wear leather over-gloves to protect the rubber from puncture."

**PPT Content:**
```
WEEK 7 REVIEW — HV SAFETY

LETHAL THRESHOLD: 50V AC / 60V DC
  Most EVs: 400V - 800V = INSTANTLY LETHAL

ORANGE CABLES = HIGH VOLTAGE — NEVER cut/probe/disconnect
  without full LOTO procedure

LOTO PROCEDURE:
  1. INFORM — Tell colleagues you're working on HV
  2. IDENTIFY — Locate all HV energy sources
  3. ISOLATE — Remove service disconnect (MSD)
  4. LOCK — Apply YOUR personal padlock
  5. PROVE DEAD — Measure with CAT III multimeter
  6. EARTH — Ground the system (where applicable)

HV GLOVE RATINGS:
  Class 00: 500V AC    Class 0: 1,000V AC (AUTOMOTIVE STANDARD)
  Class 1: 7,500V AC   Class 2: 17,000V AC
  Class 3: 26,500V AC  Class 4: 36,000V AC

  INSPECT BEFORE EVERY USE — inflate, check, verify date
  ALWAYS wear leather over-gloves for puncture protection
```

---

#### Slide 21: Week 7 Review — HVAC & Emissions
**Visual:** Left side: the refrigeration cycle as a loop diagram with state changes labeled (high-pressure gas, high-pressure liquid, low-pressure liquid, low-pressure gas). Right side: comparison of DPF vs catalytic converter with function descriptions.

**Instructor Narration:**
> "Refrigeration cycle — four components, four state changes. The compressor pressurises the refrigerant gas — it gets hot. The condenser, at the front of the car, rejects that heat to the outside air — the gas condenses into a high-pressure liquid. The expansion valve drops the pressure — the liquid becomes very cold. The evaporator, inside the dashboard, absorbs heat from the cabin air — the cold liquid evaporates back into a gas. And the cycle repeats.
>
> Key point: the refrigerant does not 'make cold.' It MOVES heat from inside the cabin to outside. That's all air conditioning is — a heat pump.
>
> Emissions: the DPF — Diesel Particulate Filter — traps soot particles from diesel exhaust and periodically burns them off in a process called regeneration. The catalytic converter — on petrol engines — uses precious metals to chemically convert CO, HC, and NOx into CO2, H2O, and N2. Different systems, different purposes, both legally required."

**PPT Content:**
```
WEEK 7 REVIEW — HVAC & EMISSIONS

REFRIGERATION CYCLE:
  Compressor (pressurize gas — gets hot)
       |
  Condenser (reject heat — gas becomes liquid)
       |
  Expansion Valve (drop pressure — liquid gets cold)
       |
  Evaporator (absorb cabin heat — liquid becomes gas)
       |
  -> Back to Compressor

AC moves heat OUT of the cabin — it does NOT "make cold"

DPF (Diesel Particulate Filter):
  Traps soot particles from diesel exhaust
  Regeneration: burns trapped soot at 600°C+
  Blocked DPF = limp mode, high exhaust backpressure

CATALYTIC CONVERTER (Three-Way — Petrol):
  CO  -> CO2  (carbon monoxide to carbon dioxide)
  HC  -> H2O  (hydrocarbons to water)
  NOx -> N2   (nitrogen oxides to nitrogen)
  Uses platinum, palladium, rhodium as catalysts
```

---

#### Slide 22: Week 7 Review — Safety Systems & ADAS
**Visual:** Left side: airbag system architecture showing SRS module, clock spring, driver/passenger/side/curtain airbags, crash sensors, seatbelt pretensioners. Right side: ADAS sensor suite showing front camera, front radar, rear radar, ultrasonic sensors with their respective functions labeled.

**Instructor Narration:**
> "Airbag system — the clock spring is the electrical connection between the rotating steering wheel and the fixed steering column wiring. It's a coiled flat ribbon cable that winds and unwinds as you steer. It carries the driver airbag circuit, the horn, and sometimes steering wheel button signals. It fails from wear, over-rotation during steering component work, or connector issues. Always centre it during installation.
>
> ADAS — the forward camera handles lane keeping assist, traffic sign recognition, and provides visual input for AEB. The radar handles adaptive cruise control and provides range/speed data for AEB. They fuse together for automatic emergency braking. After windscreen replacement, the camera needs static calibration — target board at precise position. Some also need dynamic calibration — a drive on marked roads. Static versus dynamic — the exam will ask you the difference."

**PPT Content:**
```
WEEK 7 REVIEW — SAFETY SYSTEMS & ADAS

AIRBAG CLOCK SPRING:
  Coiled ribbon cable in steering column
  Connects: Airbag, horn, steering buttons
  Fails from: Wear, over-rotation, connector issues
  ALWAYS centre during installation

SRS DEPLOYMENT: ~30 milliseconds from crash detection
  Crash sensors -> SRS module -> Igniter -> Gas generator -> Bag

ADAS SENSOR TYPES:
  Camera: Lane lines, signs, pedestrians, vehicles (visual)
  Radar: Distance, speed, closing rate (microwave)
  Ultrasonic: Close-range parking assistance (sound)
  Lidar: 3D mapping (laser — premium vehicles)

CALIBRATION AFTER REPLACEMENT:
  STATIC: Target board in workshop, precise positioning
    Used for: Camera after windscreen replacement
  DYNAMIC: Driving at specified speed, clear lane markings
    Used for: Fine-tuning after static calibration

  Some vehicles REQUIRE BOTH — always check procedure
```

---

#### Slide 23: Week 7 Formative Assessment — 10 MCQs
**Visual:** Clean quiz slide with "WEEK 7 QUIZ" header and "10 Questions / 2 minutes each / Total: 20 minutes" subtitle. Instructions: select one answer per question.

**Instructor Narration:**
> "Quiz time. Ten multiple-choice questions covering everything from this week. You have about 2 minutes per question. Read carefully — some questions are deliberately tricky. Write your answers on the sheet I'm handing out. We'll mark them together afterwards. This is formative — it doesn't count toward your final grade, but it tells you exactly where you need to study before the exam. Ready? Question one."

**PPT Content — Questions displayed one at a time or as a printed handout:**

```
WEEK 7 FORMATIVE ASSESSMENT — 10 MCQs

Q1. In a SERIES hybrid, the internal combustion engine:
    A) Drives the wheels directly at highway speed
    B) Drives a generator that produces electricity for the motor
    C) Is only used for cabin heating
    D) Operates in parallel with the electric motor

Q2. The primary advantage of a PMSM motor in EV applications is:
    A) It is cheaper than an induction motor
    B) It requires no inverter to operate
    C) It delivers maximum torque from zero RPM
    D) It does not require cooling

Q3. The function of the inverter in an EV powertrain is to:
    A) Step up the 12V battery to high voltage
    B) Convert DC from the HV battery to AC for the traction motor
    C) Convert AC from the generator to DC for the battery
    D) Regulate the charging current from the wall outlet

Q4. The voltage threshold above which electric shock
    is considered potentially lethal is:
    A) 12V DC
    B) 24V AC
    C) 50V AC / 60V DC
    D) 120V AC / 200V DC

Q5. During a Lockout-Tagout (LOTO) procedure on an EV,
    the step "Prove Dead" requires:
    A) Visually confirming the service disconnect is removed
    B) Measuring 0V with a CAT III rated multimeter at the HV bus
    C) Waiting 10 minutes for capacitors to discharge
    D) Checking that the 12V battery is disconnected

Q6. Class 0 HV-rated insulating gloves are rated for
    a maximum working voltage of:
    A) 500V AC
    B) 1,000V AC
    C) 7,500V AC
    D) 17,000V AC

Q7. In the refrigeration cycle, the correct sequence of
    components the refrigerant passes through is:
    A) Evaporator -> Compressor -> Expansion Valve -> Condenser
    B) Compressor -> Condenser -> Expansion Valve -> Evaporator
    C) Condenser -> Compressor -> Evaporator -> Expansion Valve
    D) Compressor -> Evaporator -> Condenser -> Expansion Valve

Q8. The DPF (Diesel Particulate Filter) differs from a
    catalytic converter in that the DPF:
    A) Chemically converts exhaust gases
    B) Physically traps soot particles and burns them off
    C) Reduces nitrogen oxide emissions using AdBlue
    D) Is only used on petrol engines

Q9. The airbag clock spring in the steering column serves to:
    A) Provide a spring return force for the steering wheel
    B) Maintain an electrical connection between the rotating
       steering wheel and the fixed column wiring
    C) Deploy the driver airbag in a collision
    D) Monitor the steering angle for ESC

Q10. After a windscreen replacement on a vehicle with a
     forward-facing ADAS camera, STATIC calibration
     differs from DYNAMIC calibration in that static:
     A) Requires driving at highway speed with clear lane markings
     B) Uses a precisely positioned target board in the workshop
     C) Is performed automatically by the vehicle overnight
     D) Only applies to radar sensors, not cameras
```

---

#### Slide 24: MCQ Answers & Discussion
**Visual:** Answer key displayed with correct answers highlighted in green. Brief explanation for each answer shown alongside.

**Instructor Narration:**
> "Let's go through the answers. Swap papers with your neighbour for marking.
>
> Question 1 — B. In a series hybrid, the engine drives a generator only. It never connects mechanically to the wheels. All wheel drive comes from the electric motor.
>
> Question 2 — C. PMSM delivers maximum torque from zero RPM. That's the killer advantage for vehicle traction — instant response from standstill.
>
> Question 3 — B. The inverter converts DC from the high-voltage battery to three-phase AC for the traction motor. It's the brain that controls motor speed and torque.
>
> Question 4 — C. 50 volts AC or 60 volts DC. This is the universally accepted threshold in automotive HV safety standards.
>
> Question 5 — B. Prove dead means physically measuring zero volts at the HV bus with a CAT III rated multimeter. Visual confirmation alone is not sufficient — you must measure.
>
> Question 6 — B. Class 0 gloves are rated to 1,000 volts AC. This is the standard class for automotive HV work on 400V-800V systems.
>
> Question 7 — B. Compressor, condenser, expansion valve, evaporator. Compress, condense, expand, evaporate. The refrigerant changes state at each stage.
>
> Question 8 — B. The DPF physically traps soot particles and periodically burns them off through regeneration. The catalytic converter chemically converts gases. Different mechanisms, different purposes.
>
> Question 9 — B. The clock spring maintains an electrical connection between the rotating steering wheel and the fixed steering column wiring. It carries the airbag circuit, horn, and steering wheel buttons.
>
> Question 10 — B. Static calibration uses a precisely positioned target board in the workshop. Dynamic calibration requires driving. Know the difference — the exam tests this."

**PPT Content:**
```
WEEK 7 QUIZ — ANSWERS

Q1:  B — Engine drives generator only (series hybrid)
Q2:  C — Maximum torque from zero RPM
Q3:  B — Converts DC (battery) to AC (motor)
Q4:  C — 50V AC / 60V DC
Q5:  B — Measure 0V with CAT III multimeter
Q6:  B — 1,000V AC (Class 0)
Q7:  B — Compressor -> Condenser -> Exp. Valve -> Evaporator
Q8:  B — Traps soot particles, burns off (regeneration)
Q9:  B — Electrical connection: rotating wheel to fixed column
Q10: B — Target board in workshop (static); driving (dynamic)

SCORING:
  9-10: Excellent — you're exam-ready on Week 7 material
  7-8:  Good — review the topics you missed
  5-6:  Needs work — revisit Days 31-34 notes this weekend
  <5:   See instructor for a targeted study plan
```

---

### **WRAP-UP: Consolidation & Week 8 Preview** (Slides 25-27, ~15 minutes)

**Narrative Voice:** Reflective, encouraging, forward-looking.

---

#### Slide 25: What You Accomplished This Week
**Visual:** Checklist with tick marks representing all five days of Week 7. Each day's key skill is summarized in one line.

**Instructor Narration:**
> "Let's take stock. On Monday you could not explain how an electric vehicle works. Today you diagnosed an HV isolation fault, reasoned through why a hybrid wouldn't engage EV mode, traced an HVAC refrigerant leak, identified a clock spring connector issue from a DTC, and explained why ADAS calibration is mandatory after windscreen replacement. In five days, you've covered technology that didn't exist in mainstream vehicles ten years ago.
>
> This week tested your ability to learn new and complex systems quickly. That's the reality of being an automotive technician in 2026 — the technology changes every model year, and you need to keep up. If you can handle Week 7, you can handle anything this industry throws at you."

**PPT Content:**
```
WEEK 7 COMPLETE — WHAT YOU CAN NOW DO:

Day 31: Explain hybrid architectures and EV powertrain operation
Day 32: Follow HV safety procedures including LOTO
Day 33: Describe the refrigeration cycle and emissions systems
Day 34: Identify SRS components and ADAS calibration requirements
Day 35: Diagnose faults across ALL Week 7 systems

5 DAYS — FROM ZERO EV KNOWLEDGE TO DIAGNOSTIC CAPABILITY

This week's technology didn't exist in mainstream vehicles
10 years ago. You just learned it in one week.
That adaptability IS the job.
```

---

#### Slide 26: Week 8 Preview — The Complete Technician
**Visual:** Image of a professional automotive workshop with a technician using a scan tool, another performing a road test, and a third completing paperwork at a service desk. Title overlay: "Week 8: The Complete Technician."

**Instructor Narration:**
> "Week 8 is your final week. It's called 'The Complete Technician' because it brings EVERYTHING together. You'll cover scheduled service procedures — the actual service checklists manufacturers use. Vehicle inspection and pre-delivery checks. Professional documentation and reporting — because a diagnosis you can't communicate is worthless. Customer communication skills — explaining technical issues in plain language. And most importantly — exam preparation and mock exams.
>
> Week 8 is where you stop being a learner and start becoming a professional. Come ready to work. The TUV SUD certification exam is close. You're closer to ready than you think."

**PPT Content:**
```
WEEK 8 PREVIEW: THE COMPLETE TECHNICIAN

Day 36: Scheduled Service Procedures
  — Manufacturer service checklists, intervals, fluid specs

Day 37: Vehicle Inspection & Pre-Delivery
  — Systematic inspection, road test, PDI process

Day 38: Documentation & Customer Communication
  — Job cards, technical reports, customer explanations

Day 39: Exam Preparation & Mock Exam 1
  — Full mock exam under timed conditions

Day 40: Final Review & Mock Exam 2
  — Targeted review, final mock, exam readiness check

THE EXAM IS COMING. YOU ARE READY. LET'S FINISH STRONG.
```

---

#### Slide 27: Weekend Study Guide
**Visual:** Clean, actionable study checklist organized by topic area with estimated study time for each.

**Instructor Narration:**
> "Before you leave — your weekend study priorities. If you scored below 8 on today's quiz, spend extra time on the areas you missed. Review your notes from each day this week. Pay special attention to the HV safety procedures and the refrigeration cycle sequence — these are high-value exam topics. If you have access to a scan tool simulator, practice reading DTCs and interpreting live data. Rest well. Monday starts your final push."

**PPT Content:**
```
WEEKEND STUDY PRIORITIES

HYBRID / EV (Day 31): 30 minutes
  - Draw the power flow for series, parallel, and BEV
  - List 3 advantages of PMSM motors
  - Explain what the inverter does in one sentence

HV SAFETY (Day 32): 30 minutes
  - Write out the LOTO procedure from memory (6 steps)
  - State the lethal voltage threshold
  - Name the correct HV glove class for automotive work

HVAC & EMISSIONS (Day 33): 30 minutes
  - Draw the refrigeration cycle with all 4 components
  - Explain DPF regeneration in 2 sentences
  - Describe how a blend door controls cabin temperature

SAFETY / ADAS (Day 34): 30 minutes
  - Describe the clock spring's function and failure modes
  - Explain static vs dynamic ADAS calibration
  - List 3 ADAS functions that use the front camera

DIAGNOSTICS (Day 35): 20 minutes
  - Review the 9-step diagnostic process
  - Re-read today's 4 case studies

TOTAL: ~2.5 hours — spread over Saturday and Sunday
```

---

## Assessment Checkpoint

**Formative (not graded — diagnostic feedback):**
- 10 MCQs covering all Week 7 topics (scored and discussed in class)
- Diagnostic station worksheets (reviewed by instructor for reasoning quality)
- Verbal responses during case study discussions

**Scoring Guidance:**
- 9-10 correct: Excellent command of Week 7 material; exam-ready
- 7-8 correct: Solid understanding; review missed topics
- 5-6 correct: Gaps present; focused study required over weekend
- Below 5: Schedule one-on-one review session with instructor

**Exam Weight Note:** Week 7 contributes 16 marks to the final TUV SUD certification exam. Topics most likely to appear: HV safety procedures (LOTO), hybrid architecture differences, refrigeration cycle sequence, airbag clock spring function, ADAS calibration requirements.

---

## Key Takeaways

1. Diagnostics is a PROCESS — verify symptom, read DTCs, analyse data, form hypothesis, test, confirm. Skip a step and you guess.
2. The IMD protects lives by detecting HV insulation degradation before it becomes a shock hazard — understand what it measures and why.
3. "No DTC" does not mean "no problem" — it may mean the system is operating correctly at the limits of its design (hybrid cold weather case).
4. HVAC diagnostics follow a logical elimination: compressor engagement, refrigerant pressure, condenser airflow, blend door position.
5. SRS faults always produce a DTC that identifies the affected circuit — follow the circuit connector by connector.
6. ADAS calibration is MANDATORY after windscreen replacement, bumper repair, or sensor replacement — there is no shortcut.
7. The simplest fix is often the correct one — a dirty bumper cover causes the same ACC warning as a failed radar sensor.

---

## Preparation for Week 8 (Day 36)

**Instructor prep:**
- Prepare manufacturer service schedule examples (at least 2 brands — e.g., VW and Toyota)
- Print sample service checklists showing interval-based items (oil, filters, brakes, fluids)
- Prepare fluid specification lookup exercise (engine oil grade, coolant type, brake fluid type per VIN)
- Set up a vehicle for a complete scheduled service walkthrough
- Ensure torque wrench sets are calibrated and available
- Print service record/history documentation examples

**Learner prep:**
- Review weekend study guide from Slide 27
- Bring all Week 7 notes for reference during Week 8
- Wear workshop-appropriate clothing and PPE from Day 36 onward — every remaining session involves hands-on work
- Review the 8-system overview from Day 1 — Week 8 ties everything together

---

## Slide Index

| Slide | Title | Duration | Type |
|-------|-------|----------|------|
| 1 | Title & Week 7 Finale | 3 min | Setup |
| 2 | Week 7 Recap | 3 min | Setup |
| 3 | The Diagnostic Process | 2 min | Setup |
| 4 | Today's Plan | 2 min | Setup |
| 5 | Case Study 1: HV Isolation Fault | 3 min | Development |
| 6 | IMD Explained | 3 min | Development |
| 7 | Case Study 2: Hybrid Mode Not Engaging | 4 min | Development |
| 8 | Hybrid Decision Logic | 2 min | Development |
| 9 | Case Study 3: AC Not Cooling | 4 min | Development |
| 10 | Case Study 3B: Hot One Side | 3 min | Development |
| 11 | Case Study 4A: Airbag Light ON | 3 min | Development |
| 12 | Other SRS Failure Points | 2 min | Development |
| 13 | Case Study 4B: ADAS After Windscreen | 3 min | Development |
| 14 | Case Study 4C: ACC Radar Blocked | 2 min | Development |
| 15 | Case Study Summary | 2 min | Development |
| 16 | Transition to Practical | 2 min | Transition |
| 17 | Station Rotation Schedule | 70 min | Practical |
| 18 | Station Debrief | 8 min | Practical |
| 19 | Review: Hybrid & EV | 4 min | Review |
| 20 | Review: HV Safety | 4 min | Review |
| 21 | Review: HVAC & Emissions | 4 min | Review |
| 22 | Review: Safety & ADAS | 4 min | Review |
| 23 | Quiz: 10 MCQs | 15 min | Assessment |
| 24 | Quiz Answers & Discussion | 8 min | Assessment |
| 25 | Week 7 Accomplishments | 3 min | Wrap-up |
| 26 | Week 8 Preview | 3 min | Wrap-up |
| 27 | Weekend Study Guide | 2 min | Wrap-up |
