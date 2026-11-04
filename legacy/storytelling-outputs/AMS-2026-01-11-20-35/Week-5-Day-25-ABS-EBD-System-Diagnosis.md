# Week 5, Day 25: ABS/EBD System Diagnosis

## Metadata
- **Module:** Week 5 - Chassis, Suspension & Brakes
- **Day:** 25 of 30
- **Target Audience:** Entry-level automotive technicians, age 16-30, foundation level
- **Cultural Context:** India-specific (ABS becoming standard in BS6 vehicles)
- **Target Medium:** PowerPoint/Presentations (instructor-led, 3-hour theory session)
- **Learning Outcomes Covered:** AMS-SO-5-4-3
- **Storytelling Technique Used:** Mystery/Detective Story

---

## Session Outcome: AMS-SO-5-4-3

### Learning Outcome Details
- **Code:** AMS-SO-5-4-3
- **Description:** Diagnose ABS/EBD faults using scan tool; test wheel speed sensors (resistance, AC voltage output); inspect tone rings for damage; understand ABS hydraulic unit operation; bleed ABS system using scan tool activation.
- **Category:** Skill
- **Bloom's Level:** Analyze
- **Session Type:** Lecture + Diagnostic demonstration
- **Parent MO:** AMS-MO-5-4 (Brake Systems)

### Storytelling Approach
- **Technique:** Mystery/Detective Story
- **Rationale:** ABS diagnosis involves investigation—gathering evidence (DTCs, wheel speed sensor data), testing components, analyzing patterns. Character (Suresh) solves ABS warning light mystery using systematic diagnostic approach. Detective narrative builds analytical thinking for Analyze-level outcomes.

---

## Story Framework - Mystery/Detective Story

### Character: Suresh
- Age: 27, 4 years experience, specializes in electronic diagnostics
- Vehicle: Hyundai Creta 1.6, ABS+EBD warning lights on, 95,000 km
- Customer: Mrs. Iyer, concerned about safety (monsoon season approaching)

---

## Story Beats

### Act 1: The Case (20 minutes)

**The Complaint:**
"My ABS and EBD warning lights came on yesterday. Brakes still work, but I'm worried. Monsoon is coming—I need ABS functional."

Suresh connected scan tool.

**DTCs Found:**
- **C1234:** Left front wheel speed sensor circuit malfunction
- **C2145:** Right rear wheel speed sensor intermittent signal

**Freeze Frame:**
- Vehicle speed: 45 km/h (when fault occurred)
- All wheel speeds: FL 45, FR 45, RL 0, RR 45 km/h

"Interesting. Right rear showing 0 km/h while vehicle moving. That's my first clue."

---

### Act 2: The Investigation (50 minutes)

**Clue #1: Wheel Speed Sensor Testing**

**Right Rear Sensor (Primary Suspect):**

1. **Resistance test:**
   - Disconnected sensor connector
   - Measured resistance: 1.2 kΩ (spec: 0.9-1.3 kΩ) ✓
   - **Conclusion:** Sensor coil intact

2. **AC Voltage test:**
   - Reconnected sensor
   - Raised vehicle, spun wheel by hand
   - Measured AC voltage output: **0V** (spec: >0.3V when spinning)
   - **Clue:** Sensor produces no signal despite intact coil

**Clue #2: Tone Ring Inspection**

Suresh inspected the tone ring (toothed ring on hub that sensor reads).

**Finding:** Two teeth **broken off** (damaged, likely from pothole impact).

"There's my answer. Sensor is fine, but tone ring damaged. Sensor has nothing to read."

**Clue #3: Left Front Sensor (Secondary Fault)**

Why left front code if right rear is the problem?

**Testing:**
- Resistance: 1.1 kΩ ✓
- AC Voltage: 0.4V (marginal, spec >0.5V = good)
- **Diagnosis:** Sensor weak (contamination or internal wear), will fail soon

**Physical Inspection:**
- Sensor gap: 1.5mm (spec: 0.5-1.0mm = too large)
- **Cause:** Sensor loose (mounting bolt not torqued)

---

### Act 3: The Solution (40 minutes)

**Repairs:**
1. Replaced right rear hub assembly (includes tone ring): ₹4,500
2. Repositioned and torqued left front sensor: ₹0 (warranty labor)
3. Cleared fault codes
4. Test drive: ABS self-test passed, warning lights off

**Mrs. Iyer:** "Thank you. I feel safe now. Monsoon driving is dangerous without ABS."

---

## Technical Deep Dive

### How Wheel Speed Sensors Work

**Two Types:**
1. **Passive (magnetic):** Generates AC voltage as tone ring teeth pass (older vehicles)
2. **Active (Hall-effect):** Requires power, generates digital signal (modern vehicles)

**Testing:**
- Passive: Measure resistance + AC voltage output
- Active: Check power/ground + signal voltage with scan tool

### ABS Hydraulic Unit

**Components:**
- Pump motor (builds pressure)
- Solenoid valves (control pressure to each wheel)
- Accumulator (stores pressurized fluid)

**Operation:**
- Wheel locks → Sensor detects → ECU opens valve → Pressure released → Wheel rotates
- Rapid cycling (10-15 times/second) = ABS pulse felt in pedal

---

## Assessment

**Q1:** Right rear wheel speed sensor shows 0 km/h while vehicle moving at 60 km/h. Most likely cause?

A) Sensor failed
B) Tone ring damaged
C) ABS module failed
D) Brake caliper seized

**Answer:** B) Tone ring damaged
**Explanation:** If sensor reads 0 while others read 60, sensor has no signal input. Tone ring damaged (broken teeth, rust buildup) is most common cause. Sensor resistance test would verify sensor intact.

---

## Lesson Summary

- **Session Outcome:** 1 (SO-5-4-3)
- **Technique:** Mystery/Detective Story
- **Character:** Suresh (diagnostic specialist, solves ABS warning light mystery)
- **Vehicle:** Hyundai Creta (damaged tone ring + loose sensor)
- **Key Concept:** Wheel speed sensor diagnosis requires testing sensor AND tone ring
- **Duration:** 3 hours
- **Slides:** 45-50

---

**Framework Status:** ✅ Complete
**Generated:** 2026-01-12
