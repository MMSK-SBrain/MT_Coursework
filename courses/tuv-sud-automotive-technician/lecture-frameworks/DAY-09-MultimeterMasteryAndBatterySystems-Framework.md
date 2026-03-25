---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 2
week_title: "Speaking Electricity"
day_number: 9
session_title: "Multimeter Mastery & Battery Systems"
duration_minutes: 180
theory_practice: "30:70"
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 9: Multimeter Mastery & Battery Systems
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (55 min theory + 125 min practical)
**Approach:** Tool-First — Put the Instrument in Their Hands
**PPT Target:** 26-28 slides
**Week:** 2 of 8 — "Speaking Electricity"

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Safely operate a digital multimeter in all primary modes (DC voltage, AC voltage, resistance, continuity)
- Explain CAT ratings and select the correct meter safety category for automotive work
- Perform a voltage drop test across a connection or cable
- Measure alternator AC ripple to assess diode health
- Describe the internal construction of lead-acid, AGM, and EFB batteries
- Interpret resting voltage to estimate battery state of charge
- Perform a CCA test using an electronic battery tester
- Execute a safe battery replacement procedure including terminal sequence
- Explain why battery registration/coding is required on modern vehicles

**Connection to Day 8:** Yesterday learners built wiring skills — crimping, soldering, reading diagrams, and identifying components. Today they pick up the diagnostic tool that validates every electrical connection they will ever make, and they learn about the component that powers it all: the battery.

---

## Connection to Prior Knowledge

Build from:
- Day 6: Ohm's Law, voltage, current, resistance fundamentals
- Day 7: Series and parallel circuits, fuse protection, relay operation
- Day 8: Wiring construction, connector types, reading circuit diagrams
- General experience: Jump-starting a car, changing a battery (some learners)

**Bridge:** "You've learned to read circuits, build wiring, and calculate values on paper. Today we stop calculating and start measuring. The multimeter turns theory into reality — it shows you exactly what the electricity is doing, right now, in the wire you're touching."

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: The Technician's Stethoscope** (Slides 1-3, ~10 minutes)

**Narrative Voice:** Confident, practical. This tool will be with them every day of their career.

---

#### Slide 1: Title & Context
**Visual:** Close-up photo of a technician's hands holding a quality automotive DMM (Fluke 87V or equivalent), probing a connector on a live vehicle engine bay

**Instructor Narration:**
> "Good morning. Yesterday you built wiring — crimped terminals, soldered joints, traced circuits on paper. Today, you pick up the single most important diagnostic tool in your career. This is the digital multimeter — the DMM. A doctor has a stethoscope. A technician has a multimeter. By the end of today, it will feel natural in your hand. And you'll also understand the thing that powers the entire vehicle electrical system: the battery."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 2: Speaking Electricity
Day 9: Multimeter Mastery & Battery Systems

"The multimeter is the technician's stethoscope."
```

---

#### Slide 2: Day 9 Plan
**Visual:** Horizontal timeline divided into 6 blocks with icons — meter icon, circuit board icon, battery icon, wrench icon

**Instructor Narration:**
> "Here's our day. We start with the multimeter — every mode, every safety rule. Then you go to the training boards and make 10 real measurements. After the break, we cover battery construction and testing. Then you test real batteries, practise a battery replacement, and learn a proper jump start. By the end, you'll be confident with both the meter and the battery."

**PPT Content:**
```
TODAY'S PLAN (180 minutes)

BLOCK 1 (10 min):  Setup — Why the multimeter matters
BLOCK 2 (25 min):  DMM Theory — Modes, safety, technique
BLOCK 3 (50 min):  PRACTICAL 1 — 10 measurements on training board
BLOCK 4 (20 min):  Battery Theory — Construction, types, testing
BLOCK 5 (55 min):  PRACTICAL 2 — Battery testing & replacement
BLOCK 6 (15 min):  Wrap-up & Day 10 preview

Theory:Practice = 30:70
```

---

#### Slide 3: Why Measuring Beats Guessing
**Visual:** Split image — LEFT: technician replacing a perfectly good alternator with caption "Guessed: wrong part, 2 hours wasted." RIGHT: technician measuring voltage drop with caption "Measured: found corroded ground, 15-minute fix."

**Instructor Narration:**
> "Let me tell you a real workshop story. A car comes in — battery keeps going flat. The previous shop replaced the alternator. Didn't fix it. Then they replaced the battery. Still dying. Two expensive parts, no solution. A technician with a multimeter measured parasitic drain — found a glove box light staying on due to a broken switch. A 3-euro part. That's the difference between guessing and measuring. You never guess. You measure."

**PPT Content:**
```
GUESSING vs. MEASURING

Guessing:
✗ Replace parts until it works
✗ Expensive, slow, unprofessional
✗ Customer loses trust

Measuring:
✓ Test → Diagnose → Confirm → Fix
✓ Accurate, fast, professional
✓ Customer trusts your skills

RULE: Never replace a part you haven't tested.
```

---

### **DEVELOPMENT PART 1: Digital Multimeter Proficiency** (Slides 4-11, ~25 minutes)

**Narrative Voice:** Methodical, safety-conscious. Teach each mode as a separate skill.

---

#### Slide 4: Anatomy of a Digital Multimeter
**Visual:** Annotated photograph of a quality automotive DMM — display, rotary dial, input jacks (COM, V/Ohm, mA, 10A), hold button, min/max button, backlight, range button

**Instructor Narration:**
> "Let's look at the meter itself. Every DMM has these elements. The display — where you read the value. The rotary dial — where you select what you're measuring. And the input jacks — this is critical. The COM jack is always your black lead. The V/Ohm jack is for voltage and resistance — your red lead goes here for most measurements. The mA and 10A jacks are for current measurement — and they have internal fuses for protection. Put your red lead in the wrong jack and you can blow a fuse inside the meter, or worse."

**PPT Content:**
```
ANATOMY OF A DMM

DISPLAY: Shows measured value + units
ROTARY DIAL: Selects measurement mode
  DC V — Direct current voltage
  AC V — Alternating current voltage
  Ω   — Resistance (Ohms)
  ))) — Continuity (beep test)
  A   — Current (Amps)

INPUT JACKS (bottom of meter):
  COM      — Common (BLACK lead — ALWAYS here)
  V/Ω     — Voltage & Resistance (RED lead — most measurements)
  mA       — Low current (RED lead — milliamp measurements, fused)
  10A/20A  — High current (RED lead — starter draw, fused)

⚠ WRONG JACK = BLOWN FUSE OR DAMAGED METER
```

---

#### Slide 5: Meter Safety — CAT Ratings
**Visual:** Diagram showing CAT I through CAT IV with automotive application highlighted at CAT III. Include image of CAT III rating printed on a meter body.

**Instructor Narration:**
> "Before you measure anything, you need to understand meter safety ratings. CAT ratings — Category ratings — tell you how much fault energy the meter can safely handle. CAT I is for low-energy electronics. CAT II is for household outlets. CAT III is for distribution-level circuits — this is what you need for automotive work. Why? Because the battery in a car can deliver hundreds of amps into a short circuit. A cheap CAT I meter from a discount shop can literally explode in your hands if it experiences a fault during automotive measurement. Always use a CAT III rated meter with fused inputs."

**PPT Content:**
```
METER SAFETY — CAT RATINGS

CAT I:   Low-energy electronics (phone chargers)
CAT II:  Household outlets (appliances)
CAT III: Distribution level — AUTOMOTIVE MINIMUM ✓
CAT IV:  Utility supply (mains panels)

WHY CAT III FOR AUTOMOTIVE?
• Car battery: 12V but up to 1,000A short-circuit current
• Hybrid/EV systems: 48V to 800V+
• Fault energy can vaporize cheap meter leads

ALWAYS CHECK:
✓ CAT III rating on meter body
✓ CAT III rating on test leads
✓ Fused current inputs
✓ Silicone-insulated leads (heat resistant)

⚠ CHEAP METERS KILL — invest in quality
```

---

#### Slide 6: DC Voltage Measurement
**Visual:** Step-by-step diagram showing DMM set to DC V, red on positive, black on COM, probing across a battery and then across a sensor connector

**Instructor Narration:**
> "DC voltage is your most common measurement. Set the dial to DC V. Red lead to V/Ohm jack, black to COM. Touch the red probe to the point closest to positive, black to the closest ground. The meter reads the potential difference between those two points.
>
> Battery voltage: touch positive terminal, touch negative terminal. A healthy charged battery reads 12.6 volts. A sensor signal: red probe on the signal wire, black probe on the sensor ground. You might see 0.5 to 4.5 volts depending on what the sensor is reading.
>
> Voltage drop testing is a special technique — you measure across a connection or wire while current is flowing. A good connection drops less than 0.1 volts. More than 0.5 volts? You've found resistance — corrosion, loose terminal, damaged wire. This is the single most powerful diagnostic technique you will learn."

**PPT Content:**
```
DC VOLTAGE MEASUREMENT

Setup: Dial → DC V | Red → V/Ω jack | Black → COM

Technique: Measure IN PARALLEL (across the component)

COMMON AUTOMOTIVE MEASUREMENTS:
• Battery voltage: 12.6V = fully charged
• Sensor signals: 0.5V – 4.5V typical (5V ref circuits)
• Injector supply: ~12V with ignition on
• Ground integrity: 0V to chassis = good ground

VOLTAGE DROP TESTING (critical skill):
Measure ACROSS a connection WHILE CURRENT FLOWS
• < 0.1V = good connection
• 0.2V – 0.5V = suspect — investigate
• > 0.5V = high resistance — repair needed

Voltage drop finds what visual inspection cannot.
```

---

#### Slide 7: AC Voltage Measurement
**Visual:** Diagram showing DMM set to AC V, probing alternator output terminal, with oscilloscope trace showing clean AC ripple vs. failed diode ripple

**Instructor Narration:**
> "AC voltage measurement in automotive has one primary application: alternator ripple testing. Your alternator produces AC electricity internally, then rectifies it to DC through a diode bridge. If a diode fails, AC ripple leaks into the DC system. Set your meter to AC V and probe the alternator output terminal to battery negative. At idle, a healthy alternator shows less than 0.5 volts AC ripple. More than 0.5 volts? You have a failed diode. More than 1 volt? Multiple diodes — alternator replacement needed. This is a quick, powerful test that most technicians forget to do."

**PPT Content:**
```
AC VOLTAGE MEASUREMENT

Setup: Dial → AC V | Red → V/Ω jack | Black → COM

PRIMARY AUTOMOTIVE USE: Alternator Ripple Test

Test procedure:
1. Engine running at idle
2. Red probe on alternator B+ output terminal
3. Black probe on battery negative terminal
4. Read AC voltage

Results:
• < 0.3V AC = Healthy alternator ✓
• 0.3V – 0.5V AC = Monitor, early diode wear
• > 0.5V AC = Failed diode — investigate ✗
• > 1.0V AC = Multiple diode failure — replace ✗

WHY THIS MATTERS:
AC ripple causes erratic sensor readings,
flickering lights, and premature battery failure.
```

---

#### Slide 8: Resistance (Ohms) Measurement
**Visual:** DMM set to Ohms, probing across a disconnected sensor. Important callout box: "CIRCUIT MUST BE DE-ENERGIZED"

**Instructor Narration:**
> "Resistance measurement tells you about a component's internal condition. Is this ignition coil good? Check its resistance — the spec sheet says 0.5 to 1.5 ohms primary, 6,000 to 12,000 ohms secondary. Is this wire broken? Measure end-to-end resistance — should be near zero ohms. Is this sensor in range? Measure across its terminals.
>
> Here's the critical rule: NEVER measure resistance on a live circuit. The meter sends a tiny current through the component to measure resistance. If the circuit is already powered, you'll get a garbage reading at best and damage the meter at worst. Always disconnect the component or turn off the circuit before measuring ohms. I see technicians make this mistake all the time."

**PPT Content:**
```
RESISTANCE (Ω) MEASUREMENT

Setup: Dial → Ω | Red → V/Ω jack | Black → COM

⚠ CRITICAL RULE: CIRCUIT MUST BE OFF / COMPONENT DISCONNECTED
   Measuring resistance on a live circuit = garbage reading + meter damage

Technique: Measure ACROSS the component (in isolation)

COMMON AUTOMOTIVE MEASUREMENTS:
• Ignition coil primary: 0.5 – 1.5 Ω (typical)
• Ignition coil secondary: 6,000 – 12,000 Ω (typical)
• Fuel injector: 12 – 16 Ω (high impedance)
• Temperature sensor: varies with temp (NTC: high cold, low hot)
• Wire continuity: < 0.5 Ω end-to-end = good

READINGS EXPLAINED:
• 0 Ω (or very low) = Short circuit
• Expected value = Component OK
• OL (Over Limit) = Open circuit (broken)
```

---

#### Slide 9: Continuity Testing
**Visual:** DMM set to continuity (diode/beep symbol), probing both ends of a wire in a harness. Speaker icon showing beep. Second image: testing a switch — open vs. closed.

**Instructor Narration:**
> "Continuity is the simplest test but one of the most useful. It answers one question: is there a complete path from point A to point B? Set the meter to continuity — the symbol looks like a sound wave or diode symbol with a speaker. Touch both ends of a wire. If the path is complete, the meter beeps. If not — silence. It's instant, no reading numbers needed.
>
> Use it for: tracing wires through a harness, checking if a fuse is good, testing switches (should beep when closed, silence when open), and verifying ground connections. Touch your probe to a chassis ground point and the battery negative — beep means good ground."

**PPT Content:**
```
CONTINUITY TESTING

Setup: Dial → ))) (continuity/beep) | Red → V/Ω jack | Black → COM

⚠ CIRCUIT MUST BE OFF (same rule as resistance)

Result:
• BEEP = Complete path (continuity exists) ✓
• SILENCE = Open circuit (break in path) ✗

COMMON USES:
• Wire tracing: beep = wire goes from A to B
• Fuse testing: beep = fuse is good
• Switch testing: beep when ON, silence when OFF
• Ground verification: probe to chassis, probe to battery (-)
• Connector pin check: is this pin connected to that pin?

SPEED TIP: Touch leads together first — confirm meter beeps.
If no beep with leads together, check battery or lead connections.
```

---

#### Slide 10: Clamp Current Measurement
**Visual:** Photo of a clamp-on current probe attached to a DMM, clamped around a single wire. Diagram showing parasitic drain test setup with negative cable disconnected and meter in series.

**Instructor Narration:**
> "Current measurement tells you how much electricity is flowing. In automotive, you'll use it primarily for two things: parasitic drain testing and starter draw awareness.
>
> A clamp meter clips around a wire without breaking the circuit — it measures the magnetic field the current creates. For parasitic drain testing, clamp around the negative battery cable with everything off. A healthy car draws 20 to 50 milliamps at rest. More than 80 milliamps? Something is staying on that shouldn't be.
>
> For inline current measurement — connecting the meter IN the circuit — you must use the correct fused input jack. The 10A or 20A jack for high current, the mA jack for small currents. Never exceed the fuse rating. And never try to measure starter current with an inline meter — that's 200+ amps and will destroy the meter. Use a clamp meter for that."

**PPT Content:**
```
CURRENT MEASUREMENT

CLAMP METHOD (non-invasive, preferred):
• Clamp around a SINGLE wire
• Reads magnetic field — no circuit break needed
• Good for: parasitic drain, charging current, circuit loads

INLINE METHOD (meter in series):
• Red lead in mA or 10A jack (FUSED)
• Break the circuit, meter becomes part of it
• ⚠ Never exceed fuse rating (typically 10A or 20A)

PARASITIC DRAIN TEST:
1. Key off, doors closed, wait 20 min (modules sleep)
2. Clamp around battery negative cable
3. Read current
• 20–50 mA = Normal (clock, alarm, modules)
• 50–80 mA = Borderline — investigate
• > 80 mA = Excessive drain — find the circuit

⚠ NEVER measure starter draw with inline meter
   Starter current: 150–300A (use clamp only!)
```

---

#### Slide 11: Common Multimeter Mistakes
**Visual:** Grid of four photos showing common errors — (1) measuring resistance on live circuit, (2) red lead in wrong jack, (3) probing through insulation with sharp probes leaving holes, (4) using a cheap uncertified meter

**Instructor Narration:**
> "Let me save you from the mistakes I've seen technicians make — and the mistakes I made when I was learning. Number one: measuring resistance on a live circuit. The reading is meaningless and you risk damaging the meter. Number two: red lead in the amp jack when measuring voltage. This creates a short circuit through the meter's low-resistance current shunt — the fuse blows, or worse. Number three: puncturing wire insulation with sharp probe tips. Yes, you get a reading, but you've now created a point where water can wick in and cause corrosion. Use back-probing or breakout connectors. Number four: using a cheap, unrated meter. For professional automotive work, invest in a quality CAT III meter. Your life depends on it when you start working on hybrid systems."

**PPT Content:**
```
COMMON MULTIMETER MISTAKES

1. MEASURING Ω ON A LIVE CIRCUIT
   Result: Wrong reading + possible meter damage
   Fix: Always disconnect or power off first

2. RED LEAD IN WRONG JACK
   Result: Blown internal fuse or dead short
   Fix: Check jack BEFORE connecting to circuit

3. PIERCING WIRE INSULATION
   Result: Moisture entry → corrosion → future fault
   Fix: Use back-probes, breakout boxes, or T-pins

4. USING A CHEAP / UNRATED METER
   Result: Inaccurate readings or catastrophic failure
   Fix: CAT III minimum, known brand (Fluke, Klein, Autel)

5. WRONG RANGE SELECTION
   Result: "OL" or no reading
   Fix: Start on highest range, work down (or use auto-range)
```

---

### **PRACTICAL PART 1: Multimeter Circuit Board — 10 Measurements** (Slides 12-14, ~50 minutes)

**Narrative Voice:** Coach mode. Walk the room, observe technique, correct in real time.

---

#### Slide 12: Practical 1 — Station Setup
**Visual:** Photo of training measurement boards with labelled test points (TP1-TP10). Workbench layout showing DMM, leads, recording sheet, and training board.

**Instructor Narration:**
> "Time to use the meter. Each station has a training board with 10 numbered test points. Your job is to make all 10 measurements, record the value, and identify whether the reading is correct or indicates a fault. Some measurements are on healthy circuits — some have intentional faults built in. You have your DMM and a recording sheet. Work in pairs — one measures, one records, then switch. I'll circulate to check your technique."

**PPT Content:**
```
PRACTICAL 1: MULTIMETER CIRCUIT BOARD (50 minutes)

STATION SETUP:
• Training measurement board with test points TP1–TP10
• Digital multimeter + test leads
• Recording sheet

10 MEASUREMENTS:
TP1:  DC voltage across power supply output
TP2:  DC voltage at a resistor divider midpoint
TP3:  Voltage drop across a good connection
TP4:  Voltage drop across a corroded connection (fault)
TP5:  Resistance of a known-good resistor
TP6:  Resistance of an open-circuit component (fault)
TP7:  Continuity of a complete wire path
TP8:  Continuity of a broken wire path (fault)
TP9:  Resistance of a simulated temp sensor (NTC)
TP10: DC voltage of a simulated sensor signal

RECORD: Value + Mode Used + Good/Fault assessment
```

---

#### Slide 13: Measurement Technique Checklist
**Visual:** Infographic checklist — 6 steps in order, with hand position photos for correct probe technique

**Instructor Narration:**
> "Before you start, here's your measurement procedure. Every time. Step one: identify what you're measuring — voltage, resistance, or continuity. Step two: set the dial to the correct mode. Step three: confirm your leads are in the correct jacks. Step four: if measuring resistance or continuity, verify the circuit is de-energized. Step five: make solid contact with both probes. Step six: read and record the value. Follow this every time and you'll never damage a meter or get a false reading."

**PPT Content:**
```
MEASUREMENT PROCEDURE — EVERY TIME

Step 1: IDENTIFY what you need to measure
        (Voltage? Resistance? Continuity?)

Step 2: SET the rotary dial to correct mode
        (DC V, AC V, Ω, ))) )

Step 3: CHECK your lead jacks
        (Black → COM, Red → V/Ω for most measurements)

Step 4: VERIFY circuit state
        (Resistance/Continuity: circuit OFF)
        (Voltage: circuit ON)

Step 5: CONTACT — firm probe contact on clean metal
        (Both probes must touch simultaneously)

Step 6: READ and RECORD the value with units
        (12.6V not just "12.6")

PRACTICE THIS SEQUENCE UNTIL IT'S AUTOMATIC.
```

---

#### Slide 14: Practical 1 — Expected Results & Debrief
**Visual:** Table with TP1-TP10 showing expected values, acceptable ranges, and fault indicators

**Instructor Narration:**
> "Let's compare your results. TP1 should have read approximately 12 volts — that's the power supply. TP3 — the good connection — should have shown less than 0.1 volts drop. TP4 — the corroded connection — should have shown 0.5 volts or more. That's the difference between good and bad. TP6 showed OL on your meter — that component is open circuit. TP8 — no beep — that wire is broken. How many of you identified all four faults? Good. That's diagnostic thinking."

**Instructor Action:** Walk through each test point. Ask learners to call out their readings. Discuss any discrepancies. Highlight the diagnostic logic: "What does this reading TELL you about the circuit?"

**PPT Content:**
```
PRACTICAL 1 — RESULTS REVIEW

TP   | Mode     | Expected Value       | Fault?
-----|----------|---------------------|--------
TP1  | DC V     | 12.0 – 12.6V        | No
TP2  | DC V     | ~6.0V (divider)      | No
TP3  | DC V     | < 0.1V (voltage drop) | No
TP4  | DC V     | > 0.5V (voltage drop) | YES — high resistance
TP5  | Ω        | 470Ω ± 5%            | No
TP6  | Ω        | OL (open)            | YES — open component
TP7  | )))      | BEEP                 | No
TP8  | )))      | SILENCE              | YES — broken wire
TP9  | Ω        | Varies (NTC sensor)  | No
TP10 | DC V     | 0.5V – 4.5V          | No

4 FAULTS TOTAL — DID YOU FIND THEM ALL?
```

---

### **DEVELOPMENT PART 2: Automotive Battery Systems** (Slides 15-21, ~20 minutes)

**Narrative Voice:** Structured, factual. Build from construction to testing to replacement.

---

#### Slide 15: Lead-Acid Battery Construction
**Visual:** Cutaway diagram of a conventional flooded lead-acid battery showing 6 cells, positive/negative plates, separators, electrolyte, terminal posts, and vent caps

**Instructor Narration:**
> "The 12-volt car battery is actually six 2.1-volt cells connected in series. Each cell contains positive plates made of lead dioxide and negative plates made of sponge lead, separated by insulating separators, all immersed in electrolyte — a mixture of sulphuric acid and water. When the battery discharges, a chemical reaction converts both plate materials to lead sulphate and the electrolyte becomes weaker. When you charge it, the reaction reverses.
>
> Six cells times 2.1 volts equals 12.6 volts — that's a fully charged battery. If you measure 12.4, you're at about 75%. At 12.2, you're at 50%. At 12.0 volts, you're at 25% — the battery is struggling. Below 11.8 volts, it's effectively dead."

**PPT Content:**
```
LEAD-ACID BATTERY CONSTRUCTION

6 cells in series × 2.1V per cell = 12.6V (fully charged)

INSIDE EACH CELL:
• Positive plates: Lead dioxide (PbO₂) — brown
• Negative plates: Sponge lead (Pb) — grey
• Separators: Insulate plates, allow electrolyte flow
• Electrolyte: Sulphuric acid (H₂SO₄) + water (H₂O)

CHEMICAL REACTION (simplified):
Discharge →  Plates convert to lead sulphate (PbSO₄)
              Electrolyte weakens (more water)
Charge    →  Plates restored, electrolyte strengthens

VOLTAGE vs. STATE OF CHARGE (at rest, no load):
12.6V  = 100%    ✓ Fully charged
12.4V  = 75%     ✓ Good
12.2V  = 50%     ⚠ Needs charging
12.0V  = 25%     ✗ Deeply discharged
< 11.8V = Dead   ✗ May not recover
```

---

#### Slide 16: AGM Batteries
**Visual:** Side-by-side cutaway — flooded battery (liquid electrolyte visible) vs. AGM battery (glass mat between plates, sealed construction). Highlight "no free liquid" and "sealed valve-regulated" labels.

**Instructor Narration:**
> "AGM — Absorbed Glass Mat. Instead of liquid electrolyte sloshing around, the acid is absorbed into fibreglass mats between the plates. This means the battery is sealed — no maintenance, no topping up, and it can be mounted in any position without leaking. The glass mats also hold the plates under compression, which makes AGM batteries much more resistant to vibration damage.
>
> AGM batteries handle deeper cycling better than standard flooded batteries. They recover from discharge faster and they can deliver higher current. That's why you find them in vehicles with start-stop systems, regenerative braking, and heavy electrical loads. They cost more — typically 2 to 3 times a standard battery — but they last longer in the right application."

**PPT Content:**
```
AGM — ABSORBED GLASS MAT BATTERY

Construction difference:
• Electrolyte absorbed into fibreglass mats (no free liquid)
• Sealed, valve-regulated (VRLA) — maintenance free
• Plates compressed by mats — vibration resistant

ADVANTAGES over standard flooded:
✓ Deeper cycling capability (handles repeated discharge)
✓ Faster recharge acceptance
✓ Higher cold cranking amps (CCA) per size
✓ Mount in any position (no leak risk)
✓ Lower self-discharge rate
✓ Longer service life

FOUND IN:
• Start-stop vehicles
• Vehicles with regenerative braking
• Premium/luxury vehicles with high electrical loads
• Vehicles with battery in boot/under seat

COST: 2-3× standard battery
⚠ Requires AGM-compatible charger — never use a standard fast charger
```

---

#### Slide 17: EFB Batteries
**Visual:** Comparison table showing Standard Flooded vs. EFB vs. AGM — construction, cycling ability, cost, typical application

**Instructor Narration:**
> "EFB — Enhanced Flooded Battery — sits between standard flooded and AGM. It's still a flooded design with liquid electrolyte, but the plates are thicker, the active material is improved, and there's often a scrim or polyester fleece on the positive plate to hold the material in place during cycling. EFBs are designed for basic start-stop vehicles — those without regenerative braking. They handle more cycles than a standard battery but fewer than AGM. They're cheaper than AGM, so manufacturers use them where AGM isn't strictly necessary. Important rule: if a vehicle came with an AGM, you MUST replace it with an AGM. Never downgrade. You can upgrade from EFB to AGM, but never the reverse."

**PPT Content:**
```
EFB — ENHANCED FLOODED BATTERY

Construction:
• Flooded (liquid electrolyte) — but improved
• Thicker plates with enhanced active material
• Polyester scrim on positive plate (holds material)

COMPARISON:
Feature         | Standard  | EFB       | AGM
----------------|-----------|-----------|----------
Cycling ability  | Low       | Medium    | High
Start-stop      | No        | Basic     | Full
Regen braking   | No        | No        | Yes
Vibration resist | Low       | Medium    | High
Cost (relative)  | 1×        | 1.5×      | 2-3×
Typical vehicle  | Older/base| Entry S/S | Premium S/S

REPLACEMENT RULES:
✓ Standard → Standard, EFB, or AGM (upgrade OK)
✓ EFB → EFB or AGM (upgrade OK)
✓ AGM → AGM ONLY (never downgrade)

⚠ NEVER put a standard or EFB battery in an AGM vehicle
```

---

#### Slide 18: Battery Testing Procedures
**Visual:** Four-quadrant diagram showing: (1) resting voltage test with DMM, (2) electronic CCA tester connected to battery, (3) load tester with carbon pile, (4) smart charger connected with display showing charge stage

**Instructor Narration:**
> "Four tests you need to know. First: resting voltage. Simple DMM across the terminals with no load and the car off for at least 30 minutes. You already know the voltage-to-charge table. Second: CCA testing with an electronic battery tester. These devices send a small AC signal through the battery and measure internal resistance. They calculate CCA and give you a pass/fail result. This is the modern standard — fast, non-destructive, and accurate even on a discharged battery.
>
> Third: load testing with a carbon pile tester — the old school method. Apply a load equal to half the CCA rating for 15 seconds. Voltage should stay above 9.6 volts at room temperature. Below that, the battery is weak. Fourth: charging with a smart charger. A smart charger adjusts voltage and current automatically through stages — bulk, absorption, float. It won't overcharge, and it can desulphate neglected batteries. Always use a smart charger — never a dumb charger that just blasts current."

**PPT Content:**
```
BATTERY TESTING — 4 KEY TESTS

1. RESTING VOLTAGE (DMM):
   • Key off, no load, wait 30 min minimum
   • 12.6V = 100% | 12.4V = 75% | 12.2V = 50% | 12.0V = 25%

2. CCA TEST (Electronic Tester):
   • Connect tester to terminals
   • Enter battery rating (CCA from label)
   • Tester sends AC signal, measures internal resistance
   • Result: GOOD / RECHARGE & RETEST / REPLACE
   • Non-destructive, works on discharged batteries

3. LOAD TEST (Carbon Pile — older method):
   • Load = 50% of rated CCA for 15 seconds
   • Voltage must stay above 9.6V at 20°C
   • Below 9.6V = battery failing

4. CHARGING (Smart Charger):
   • Bulk stage: high current, battery fills
   • Absorption stage: voltage held, current tapers
   • Float stage: maintains full charge
   • ⚠ Use AGM mode for AGM batteries
```

---

#### Slide 19: Battery Replacement — The Safe Sequence
**Visual:** Step-by-step illustrated guide showing disconnect sequence (negative first) and reconnect sequence (positive first), with hand positions and tool usage

**Instructor Narration:**
> "Battery replacement has a specific order and there's a safety reason for it. When disconnecting: always remove the NEGATIVE terminal first. Why? Because the entire car body is connected to negative. If you remove positive first and your spanner touches any metal part of the car, you create a short circuit — sparks, heat, potentially an explosion from battery gases. But if you disconnect negative first, the circuit is already broken — touching the body with your tool does nothing.
>
> Reconnecting is the reverse: connect POSITIVE first, then negative. Same logic — positive is safe to connect first because there's no ground path to short against until you connect negative.
>
> Memory saver devices can maintain ECU settings during the swap, but many shops just let the car relearn. The critical thing on modern vehicles is battery registration."

**PPT Content:**
```
BATTERY REPLACEMENT — SAFE SEQUENCE

DISCONNECTING:
1. Turn off ignition and all accessories
2. Remove NEGATIVE (-) terminal FIRST
   → Why? Prevents short circuit if tool touches body
3. Remove POSITIVE (+) terminal second
4. Remove hold-down clamp
5. Lift out battery (caution: heavy, 15-25 kg)

RECONNECTING:
1. Place new battery, secure hold-down clamp
2. Connect POSITIVE (+) terminal FIRST
   → Apply terminal grease (anti-corrosion)
3. Connect NEGATIVE (-) terminal last
4. Tighten both terminals firmly (no play, no over-torque)
5. Verify: start engine, check charging voltage (13.8-14.4V)

REMEMBER: "Negative First Off, Positive First On"

⚠ Wear safety glasses — battery acid risk
⚠ No smoking — hydrogen gas explosion risk
⚠ Remove metal watches/rings — short circuit risk
```

---

#### Slide 20: Battery Registration & Coding
**Visual:** Screenshot of a diagnostic tool showing battery registration screen (BMW ISTA or VCDS/ODIS style), with fields for battery type, capacity, serial number

**Instructor Narration:**
> "On modern vehicles — especially BMW, Volkswagen, Audi, Mercedes — replacing the battery isn't just a physical job. The Battery Management System needs to know that a new battery has been installed. This is called battery registration or battery coding. The BMS tracks the battery's age, charging history, and capacity. If you put in a new battery and don't register it, the BMS still thinks the old, degraded battery is installed. It will undercharge the new battery, reducing its lifespan by years.
>
> On BMW, you need ISTA or an aftermarket tool that can perform battery registration. On VAG vehicles, you use ODIS or VCDS. You enter the new battery's part number, capacity, and serial number. The BMS resets its charge strategy for the fresh battery. If you skip this step, the customer will be back in 18 months with a failed battery that should have lasted five years. This is one of those hidden steps that separates a professional technician from someone who just swaps parts."

**PPT Content:**
```
BATTERY REGISTRATION / CODING

WHY REQUIRED?
• BMS (Battery Management System) tracks battery condition
• Old battery profile ≠ new battery = incorrect charging
• Without registration: new battery charged as if old → short life

WHICH VEHICLES?
• BMW: All models from ~2007+ (ISTA / Carly / Bimmerlink)
• VAG (VW/Audi/Skoda/SEAT): Most from ~2010+ (ODIS / VCDS)
• Mercedes: Most from ~2010+ (Xentry / Autel)
• Others: Increasing requirement across all makes

REGISTRATION PROCESS:
1. Install new battery physically
2. Connect diagnostic tool to OBD-II port
3. Navigate to Battery Registration function
4. Enter: Battery type (AGM/EFB), Capacity (Ah), CCA, Part Number
5. Confirm registration — BMS resets charge strategy

⚠ SKIPPING THIS STEP = PREMATURE BATTERY FAILURE
   Professional technicians ALWAYS register.
```

---

#### Slide 21: Jump Start Procedure
**Visual:** Step-by-step diagram showing two cars with colour-coded jumper cables — red cable: dead positive to donor positive, black cable: donor negative to engine ground bolt on dead car (NOT to dead battery negative). Numbered sequence 1-4.

**Instructor Narration:**
> "Jump starting seems simple, but the sequence matters. Get it wrong and you can damage ECUs, trigger airbag faults, or create a spark near a battery that's been outgassing hydrogen — which can cause an explosion. Here's the correct sequence. Cable one — red — from dead battery positive to donor battery positive. Cable two — black — from donor battery negative to an engine ground bolt on the dead car — NOT to the dead battery's negative terminal. Why? Because connecting to the battery terminal can create a spark right next to a battery that may be producing hydrogen gas. By connecting to the engine block instead, any spark happens away from the battery.
>
> Start the donor vehicle first. Let it run for a few minutes to partially charge the dead battery. Then start the dead vehicle. Remove cables in reverse order — black from dead car engine ground first, then black from donor, then red from donor, then red from dead car."

**PPT Content:**
```
JUMP START PROCEDURE — CORRECT SEQUENCE

CONNECTING (in this order):
1. RED cable: Dead battery (+) → Donor battery (+)
2. BLACK cable: Donor battery (-) → Engine ground bolt on DEAD car
   ⚠ NOT to dead battery (-) — spark + hydrogen = explosion risk

3. Start DONOR vehicle, run 2-3 minutes
4. Start DEAD vehicle

DISCONNECTING (reverse order):
1. BLACK from dead car engine ground
2. BLACK from donor battery (-)
3. RED from donor battery (+)
4. RED from dead car battery (+)

SAFETY RULES:
• Both vehicles OFF during cable connection
• Ensure cables don't touch each other or moving parts
• Never lean over a battery during connection
• Safety glasses recommended

AFTER JUMP START:
• Drive for minimum 20-30 minutes to recharge
• Test battery within 24 hours — jump-needed may = battery failed
```

---

### **PRACTICAL PART 2: Battery Testing & Replacement** (Slides 22-25, ~55 minutes)

**Narrative Voice:** Hands-on supervisor. Safety-first, step-by-step.

---

#### Slide 22: Practical 2 — Station Descriptions
**Visual:** Workshop floor plan showing three stations with equipment lists

**Instructor Narration:**
> "We have three stations for the battery practical. Station A: battery testing — you'll measure resting voltage on three batteries in different states of charge, then use the electronic CCA tester to evaluate each one. Station B: battery replacement — we have a vehicle with the bonnet open. You'll practise the disconnection and reconnection sequence. I'll walk you through it the first time, then you do it. Station C: jump start — two vehicles nose-to-nose. You'll connect and disconnect jump cables in the correct sequence. Each pair spends about 18 minutes per station. Let's rotate."

**PPT Content:**
```
PRACTICAL 2: BATTERY STATIONS (55 minutes)

STATION A — Battery Testing (18 min):
Equipment: 3 batteries (various conditions), DMM, electronic CCA tester
Tasks:
  1. Measure resting voltage on all 3 batteries
  2. Estimate state of charge from voltage
  3. Perform CCA test on all 3 batteries
  4. Record results and give pass/fail verdict

STATION B — Battery Replacement (18 min):
Equipment: Vehicle with battery accessible, safety glasses, tools
Tasks:
  1. Disconnect battery (correct terminal sequence)
  2. Remove hold-down clamp and battery
  3. Install replacement battery
  4. Reconnect (correct terminal sequence)
  5. Verify with voltage check: engine running = 13.8–14.4V

STATION C — Jump Start Procedure (18 min):
Equipment: Two vehicles, jumper cables, safety glasses
Tasks:
  1. Position vehicles, identify terminals
  2. Connect cables in correct sequence (talk through each step)
  3. Simulate start sequence
  4. Disconnect cables in correct reverse sequence

ROTATE EVERY 18 MINUTES — I will call time.
```

---

#### Slide 23: Station A — Battery Testing Detail
**Visual:** Photo of three batteries labelled A, B, C on a bench with a DMM and electronic tester. Recording sheet template visible.

**Instructor Narration:**
> "At Station A, you have three batteries in different conditions. One is fully charged, one is partially discharged, and one is a failed battery. I want you to find out which is which using only your meter and the electronic tester. Start with resting voltage — write down the voltage for each. Then use the electronic tester — enter the battery's rated CCA from the label, let the tester run its analysis, and record the result. By the end of this station, you should be able to look at a battery and its test results and say with confidence: 'This one's good, this one needs charging, this one needs replacing.'"

**Instructor Action:** Ensure three batteries are prepared in advance — one fully charged (12.6V+), one at approximately 50% (12.2V), one with a dead cell or very low CCA (will fail electronic test). Label them A, B, C without revealing their condition.

---

#### Slide 24: Station B — Battery Replacement Detail
**Visual:** Overhead photo of engine bay with battery location highlighted, tools laid out (10mm socket, 13mm for hold-down, terminal brush, anti-corrosion spray)

**Instructor Narration:**
> "At Station B, you'll perform a complete battery swap. First person talks through the procedure and does it with my supervision. Second person does it independently while the first person observes and checks. Remember: negative first off, positive first on. Don't rush. Check your terminal tightness — a loose terminal causes all sorts of intermittent electrical faults. After reconnecting, start the engine and measure charging voltage at the battery terminals — you should see 13.8 to 14.4 volts, confirming the alternator is working. If you see battery voltage only — around 12.6 — the alternator isn't charging."

**Instructor Action:** Supervise first removal closely. Ensure safety glasses are worn. Check terminal torque after reconnection. Verify charging voltage measurement.

---

#### Slide 25: Station C — Jump Start Detail
**Visual:** Two vehicles positioned nose-to-nose with bonnets open, jumper cables coiled on the bench, engine ground bolt highlighted on the "dead" car

**Instructor Narration:**
> "At Station C, you'll connect and disconnect jump cables. I want you to talk through each step OUT LOUD as you do it — this forces you to think about the sequence rather than just grabbing cables. 'Step one: red cable, dead positive to donor positive. Step two: black cable, donor negative to engine ground bolt on dead car.' Talk it through. If your partner hears a mistake, they stop you. After connection, simulate the start — don't actually start the vehicles unless I'm supervising. Then disconnect in reverse order, talking through each step."

**Instructor Action:** Identify the engine ground bolt on the "dead" car in advance and mark it with a tag. Ensure learners can distinguish positive from negative terminals by colour and markings.

---

### **WRAP-UP: Consolidation & Day 10 Preview** (Slides 26-28, ~15 minutes)

---

#### Slide 26: Day 9 Recap — Skills Inventory
**Visual:** Two-column checklist — Multimeter Skills on left, Battery Skills on right, all with tick boxes

**Instructor Narration:**
> "Let's take stock of what you can do now. On the multimeter side: you can measure DC voltage, AC voltage, resistance, and continuity. You can perform a voltage drop test — the single most powerful diagnostic technique. You understand meter safety and CAT ratings. You know the common mistakes and how to avoid them. On the battery side: you know the construction of lead-acid, AGM, and EFB batteries. You can test a battery using resting voltage and an electronic CCA tester. You can replace a battery safely. You know about battery registration on modern vehicles. And you can perform a proper jump start. That's a full day's work — and these are skills you'll use every single day of your career."

**PPT Content:**
```
DAY 9 RECAP — YOUR NEW SKILLS

MULTIMETER MASTERY:                BATTERY SYSTEMS:
✅ DC Voltage measurement           ✅ Lead-acid construction
✅ AC Voltage (alternator ripple)    ✅ AGM vs. EFB vs. Standard
✅ Resistance measurement            ✅ Voltage ↔ State of Charge
✅ Continuity testing                ✅ CCA testing (electronic)
✅ Voltage drop testing              ✅ Battery replacement sequence
✅ Current awareness (clamp)         ✅ Battery registration/coding
✅ CAT III safety ratings            ✅ Jump start procedure
✅ Common mistakes to avoid          ✅ Charger types (smart vs. dumb)

THESE ARE DAILY-USE SKILLS — not exam-only knowledge.
```

---

#### Slide 27: Key Takeaways
**Visual:** Five numbered takeaway statements in a clean infographic layout

**Instructor Narration:**
> "Five things to remember from today. One: the multimeter is your most important diagnostic tool — learn it so well it becomes automatic. Two: always check your meter's safety rating and lead connections before measuring. Three: voltage drop testing is the most powerful technique — it finds what eyes cannot see. Four: battery voltage tells you charge state — memorize the numbers. Five: on modern vehicles, battery replacement is a physical AND electronic job — always register the new battery."

**PPT Content:**
```
5 KEY TAKEAWAYS — DAY 9

1. THE DMM IS YOUR #1 TOOL
   Master it — it's the difference between guessing and knowing

2. METER SAFETY IS NON-NEGOTIABLE
   CAT III minimum, correct jacks, correct mode

3. VOLTAGE DROP TESTING = DIAGNOSTIC SUPERPOWER
   < 0.1V good | > 0.5V problem | Finds invisible resistance

4. BATTERY VOLTAGE = STATE OF CHARGE
   12.6V = 100% | 12.4V = 75% | 12.2V = 50% | 12.0V = 25%

5. MODERN BATTERIES NEED REGISTRATION
   Physical swap + electronic coding = complete job
```

---

#### Slide 28: Day 10 Preview
**Visual:** Image of a diagnostic scan tool (OBD-II reader) connected to a vehicle's diagnostic port, with fault codes visible on screen. Second image: oscilloscope trace of an injector signal.

**Instructor Narration:**
> "Tomorrow is the last day of Week 2 — Speaking Electricity. We bring everything together. You'll use a diagnostic scan tool for the first time — reading live data, pulling fault codes, understanding what the car's computers are telling you. We'll also look at basic oscilloscope patterns — seeing what electrical signals actually look like over time. If the multimeter is your stethoscope, the scan tool is your X-ray machine. Get a good night's rest — tomorrow is where diagnostics begins. See you in the morning."

**PPT Content:**
```
DAY 10 PREVIEW: DIAGNOSTIC TOOLS & LIVE DATA

Week 2, Day 5 — "Speaking Electricity" Finale

• OBD-II Diagnostic Scan Tool:
  - Reading and clearing fault codes (DTCs)
  - Live data streams (RPM, coolant temp, O2 sensors)
  - Freeze frame data (snapshot at fault moment)

• Basic Oscilloscope Awareness:
  - What a waveform tells you
  - Injector patterns, sensor signals

• Week 2 Consolidation:
  - From Ohm's Law to diagnostic tools in 5 days

Bring everything you've learned this week.
Day 10 connects it all.
```

---

## Assessment Checkpoint

**Formative (not graded):**
- Multimeter circuit board: correctly measure and record all 10 test points, identifying at least 3 of 4 faults
- Battery testing: correctly assess state of charge and CCA test result for at least 2 of 3 test batteries
- Battery replacement: demonstrate correct disconnect/reconnect sequence without prompting
- Jump start: verbally describe and physically demonstrate correct cable connection and disconnection sequence

**Diagnostic Skills Check (instructor observation):**
- Learner sets correct mode before probing
- Learner checks lead jack placement before connecting
- Learner does not attempt resistance measurement on a live circuit
- Learner can explain what a voltage drop reading means

---

## Key Takeaways

1. The digital multimeter is the most frequently used diagnostic tool in automotive — master it early and thoroughly
2. Meter safety (CAT III, fused inputs, correct lead placement) is non-negotiable for professional work
3. Voltage drop testing is the single most powerful electrical diagnostic technique — it reveals resistance invisible to the eye
4. Battery resting voltage directly correlates to state of charge and is the first test in any electrical diagnosis
5. Modern vehicles require electronic battery registration after physical replacement — skipping it causes premature failure

---

## Preparation for Day 10

**Instructor prep:**
- Ensure OBD-II scan tools are charged and functional (one per pair minimum)
- Prepare a vehicle with at least 2-3 stored DTCs for live demonstration
- If available, set up a basic oscilloscope or PC-based scope with automotive probes
- Prepare a "live data challenge" — a vehicle with a known condition (e.g., slightly misfiring cylinder, coolant temp sensor offset) that learners must identify through scan tool data
- Print OBD-II Mode/PID reference sheets

**Learner prep:**
- Review all Week 2 concepts: Ohm's Law, series/parallel circuits, wiring, components, multimeter, battery
- Bring their notes from Days 6-9
- Be prepared for a hands-on diagnostic challenge using everything learned this week

---

## Station Equipment Checklist

**PRACTICAL 1 — Multimeter Training Boards:**
- [ ] Training measurement boards (1 per pair) with 10 labelled test points
- [ ] Intentional faults wired into boards (corroded connection, open component, broken wire, NTC sensor)
- [ ] Digital multimeters (1 per pair) — CAT III rated
- [ ] Test leads in good condition (no damaged insulation)
- [ ] Recording sheets printed (1 per learner)
- [ ] Spare fuses for meters (in case of incorrect jack usage)

**PRACTICAL 2 — Station A (Battery Testing):**
- [ ] 3 batteries in varying conditions (fully charged, partially discharged, failed)
- [ ] Battery labels visible showing rated CCA and Ah
- [ ] Digital multimeters (1 per pair)
- [ ] Electronic battery/CCA tester (Midtronics, CTEK, or equivalent)
- [ ] Recording sheets

**PRACTICAL 2 — Station B (Battery Replacement):**
- [ ] Vehicle with easily accessible battery
- [ ] 10mm and 13mm sockets/spanners for terminal bolts and hold-down
- [ ] Terminal cleaning brush
- [ ] Anti-corrosion terminal spray or grease
- [ ] Safety glasses (1 per learner)
- [ ] Replacement battery (same spec as original)
- [ ] DMM for post-installation charging voltage check

**PRACTICAL 2 — Station C (Jump Start):**
- [ ] Two vehicles positioned nose-to-nose
- [ ] Quality jumper cables (minimum 25mm², 3m length)
- [ ] Engine ground bolt identified and tagged on "dead" vehicle
- [ ] Safety glasses (1 per learner)
- [ ] Procedure card at station for reference
