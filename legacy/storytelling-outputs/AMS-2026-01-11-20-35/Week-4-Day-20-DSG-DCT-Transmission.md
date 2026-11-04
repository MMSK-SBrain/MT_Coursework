# Week 4, Day 20: DSG/DCT Transmission

## Metadata
- **Module:** Week 4 - Transmission & Drivetrain Systems
- **Day:** 20 of 30
- **Target Audience:** Entry-level automotive technicians, age 16-30, foundation level
- **Cultural Context:** India-specific (VW Polo DSG, Skoda Rapid DSG)
- **Target Medium:** PowerPoint/Presentations (instructor-led, 3-hour theory session)
- **Learning Outcomes Covered:** AMS-SO-4-3-3
- **Storytelling Technique Used:** Scenario-Based Learning

---

## Session Outcome: AMS-SO-4-3-3

### Learning Outcome Details
- **Code:** AMS-SO-4-3-3
- **Description:** Service DSG/DCT (Dual-Clutch Transmission) including oil and filter change; perform DSG adaptation and clutch learn procedure using scan tool; understand DCT operating principle (two clutches, odd/even gears); diagnose common DSG faults (mechatronic unit, clutch wear).
- **Category:** Skill
- **Bloom's Level:** Apply, Analyze
- **Session Type:** Lecture + Service demonstration
- **Parent MO:** AMS-MO-4-3 (Automatic Transmission Systems)

### Storytelling Approach
- **Technique:** Scenario-Based Learning
- **Rationale:** DSG service requires systematic procedure and scan tool operation. Character (Priya) services VW Polo DSG following proper sequence, demonstrating realistic workshop scenario. Scenario-based narrative builds procedural confidence for Apply-level skill, shows professional service approach, emphasizes critical adaptation procedure.

---

## Story Framework - Scenario-Based Learning

### Character Profile: Priya

**Background:**
- Age: 26 years old
- Experience: 3 years as technician, recently certified on VW/Skoda DSG systems
- Strengths: Detail-oriented, excellent with scan tools, systematic approach
- Challenge: First DSG service at new workshop (previously worked on conventional automatics)
- Motivation: Wants to establish expertise in premium brand servicing

**Assignment:**
- Vehicle: VW Polo 1.0 TSI DSG (7-speed dry clutch DSG)
- Service Due: 60,000 km DSG oil and filter service
- Customer: Mr. Kapoor, software professional, drives in Bangalore traffic daily
- Additional Complaint: Slight jerking during 1st→2nd gear shift (cold engine)

---

## Story Beats

### Setup: The DSG Service (20 minutes)

**Monday Morning, 10:00 AM - Volkswagen Authorized Workshop, Bangalore**

Priya reviewed the service schedule for the VW Polo DSG. This was her first DSG service at this workshop, and she wanted to demonstrate her expertise.

**The Customer's Concerns:**

Mr. Kapoor: "I'm here for the 60,000 km service. Also, lately there's a slight jerk when shifting from 1st to 2nd gear—only when the car's cold. Once it warms up, it's smooth. Is that normal?"

Priya noted it down. "I'll check that after the service. DSG transmissions need adaptation after oil changes, which may also resolve the jerk. Let me start with the scheduled service."

**Understanding DSG (Quick Review):**

Priya's training:
- **DSG = Direct-Shift Gearbox** (Volkswagen name for DCT - Dual-Clutch Transmission)
- **Two clutches:** Clutch 1 (odd gears: 1, 3, 5, 7 + reverse), Clutch 2 (even gears: 2, 4, 6)
- **Pre-selection:** While driving in 3rd gear, 4th gear is already engaged but clutch 2 is open. When you accelerate, clutch 1 releases, clutch 2 engages—instant shift (0.04 seconds)
- **Mechatronic unit:** Integrated control module + hydraulics (controls clutches and gear selection)

**Two DSG Types in Indian Market:**
1. **DQ200 (7-speed dry clutch):** VW Polo, Vento 1.0 TSI; Skoda Rapid 1.0 TSI
2. **DQ250 (6-speed wet clutch):** VW Tiguan, Skoda Octavia (premium models)

Mr. Kapoor's Polo has **DQ200 (dry clutch).**

---

### Rising Action: The Service Procedure (50 minutes)

**Step 1: Pre-Service Inspection (10:15 AM - 10:30 AM)**

**Scan Tool Initial Check:**

Priya connected VW-specific scan tool (ODIS or equivalent).

**Transmission Data:**
- Clutch 1 wear: 65% (specification: Replace at <20% remaining)
- Clutch 2 wear: 70% (OK)
- Mechatronic temperature: 42°C (normal)
- Fault codes: None stored
- Adaptation status: Last adaptation 15,000 km ago

"Clutch wear is acceptable. 65-70% remaining life is normal for 60,000 km. No faults stored. I'll proceed with oil service and then perform adaptation."

---

**Step 2: DSG Oil and Filter Change (10:30 AM - 11:15 AM)**

**Why DSG Oil Service is Critical:**

"DSG mechatronic unit uses transmission oil for:
1. **Hydraulic pressure** (operates clutches and shift forks)
2. **Cooling** (wet-clutch DSG only; dry-clutch DSG has minimal cooling needs)
3. **Lubrication** (gear meshes and bearings)

Degraded oil → erratic shifts, clutch slip, mechatronic failure."

**Oil Specification:**
- DQ200 (7-speed dry): VW G 052 182 A2 (specific synthetic ATF)
- **Capacity:** 1.7 liters (small capacity, critical not to overfill)

**Procedure:**

**1. Raise vehicle:**
- Lifted Polo on hoist
- Ensured level (oil level check requires vehicle level)

**2. Drain old oil:**
- Located DSG oil drain plug (underneath, similar to engine oil drain)
- Removed drain plug with 8mm hex socket
- Drained approximately 1.5 liters (some oil remains in mechatronic)

**3. Replace filter (internal):**
- Removed DSG oil pan (10 bolts, torque-to-spec: 8 Nm)
- Exposed internal filter and mechatronic unit
- Removed old filter (two clips)
- Installed new filter (VW part number 02E 305 051 C)
- Inspected oil pan for metal particles:
  - **Finding:** Slight metallic residue (normal wear for 60,000 km)
  - **If excessive:** Indicates clutch or gear wear, requires further diagnosis

**4. Clean and reinstall oil pan:**
- Cleaned pan with brake cleaner
- Installed new gasket (reusable multi-layer gasket, but VW recommends replacement)
- Torqued bolts: 8 Nm in crisscross pattern

**5. Refill with new DSG oil:**
- Located DSG oil fill plug (side of transmission case, requires vehicle level)
- Used fluid pump to inject new oil through fill plug
- Filled until oil started dripping from fill hole (indicates correct level)
- Installed fill plug, torqued to 25 Nm

**6. Level verification:**
- Engine running, transmission in Park
- Oil at operating temp (35-45°C for DQ200)
- Removed fill plug briefly—oil should just drip out slowly
- "Perfect level."

---

**Step 3: DSG Adaptation (11:15 AM - 11:45 AM)**

**Why Adaptation is Mandatory:**

"After oil change, the mechatronic unit must relearn clutch bite points and pressure characteristics. Without adaptation:
- Harsh shifts
- Clutch slip
- Premature clutch wear
- Possible fault codes"

**Adaptation Procedure (VW ODIS):**

1. **Connected scan tool:**
   - Selected "Transmission Electronics" (module 02)
   - Navigated to "Basic Settings"
   - Selected "Channel 001 - Quick Test"

2. **Pre-adaptation checks:**
   - Engine at operating temp: 90°C ✓
   - Battery voltage >12.5V ✓
   - Transmission oil temp 35-45°C ✓
   - All electrical loads off (A/C, lights, radio) ✓

3. **Adaptation sequence:**
   - Scan tool initiated adaptation
   - ECU cycled through gears (Priya heard mechanical clicks from transmission)
   - Duration: 8 minutes (automatic procedure, do not interrupt)
   - Clutch 1 adaptation: Complete ✓
   - Clutch 2 adaptation: Complete ✓

**Progress on Scan Tool:**
```
Channel 001 - Quick Test
Adaptation Status: Running...
Clutch 1: Learning bite point...
Clutch 1: 100% Complete
Clutch 2: Learning bite point...
Clutch 2: 100% Complete
Gear Selection: Verifying...
Adaptation: SUCCESSFUL
```

**4. Post-adaptation verification:**
   - Cleared adaptation counters
   - Read fault memory: No faults ✓
   - Checked clutch wear values (unchanged: 65%, 70%)

"Adaptation successful. Now for the test drive."

---

### Climax: Test Drive and Diagnosis (40 minutes)

**Test Drive 1: Warm Engine (11:50 AM - 12:10 PM)**

Priya drove the Polo on her standard DSG test route (city traffic + highway).

**Observations:**
- **1st→2nd shift:** Smooth, no jerk (even better than before service)
- **All other shifts:** Seamless, instant (typical DSG performance)
- **Reverse:** Engaged smoothly
- **Stop-and-go traffic:** No shudder, no harsh engagement

"Warm engine shifts are perfect now. But Mr. Kapoor complained about cold-start jerk. Let me replicate that."

---

**Test Drive 2: Cold Engine (Next Morning, 9:00 AM)**

Priya arrived early the next day to test the Polo with cold engine (overnight soak).

**Cold Start Test:**
- Started engine (15°C ambient, Bangalore winter morning)
- Shifted to D, drove gently
- **1st→2nd shift:** Slight jerk felt ✓ (replicated customer complaint)
- After 5 minutes of driving (oil warmed to 30°C): Jerk disappeared

**Diagnosis:**

"This is characteristic of DQ200 (dry-clutch DSG) in cold conditions. Let me explain to Mr. Kapoor."

---

### Resolution: Customer Explanation (30 minutes)

**Priya's Explanation to Mr. Kapoor (12:30 PM):**

"Mr. Kapoor, your DSG service is complete. I also diagnosed the cold-start jerk. Let me explain what's happening."

**The Technical Explanation (Simplified):**

"Your Polo has a **dry-clutch DSG**. Unlike wet-clutch transmissions, the clutches aren't bathed in oil. They operate in air, like a manual transmission clutch.

**When Cold:**
- Clutch friction material is stiff
- Engagement is slightly abrupt
- You feel a small jerk during 1st→2nd shift

**When Warm:**
- Clutch material reaches operating temperature
- Engagement becomes smooth

**Is This Normal?**

Yes. VW acknowledges this behavior in DQ200 transmissions, especially in stop-and-go traffic when cold. It's not a defect—it's a characteristic of dry-clutch design."

**The Trade-Off:**

"Dry-clutch DSG has advantages:
- **Lighter** (better fuel economy)
- **Faster shifts** (less hydraulic lag)
- **Lower cost** (simpler design)

But the trade-off:
- **Cold-start jerk** (slight)
- **More sensitive to clutch wear** (requires proper driving habits)

Wet-clutch DSG (like in Tiguan, Octavia) is smoother cold, but heavier and more expensive."

**Driving Tips to Minimize Jerk:**

"To reduce cold-start jerk:
1. **Let engine idle 30 seconds after cold start** (allows some warm-up)
2. **Drive gently first 2-3 km** (avoid hard acceleration until warm)
3. **Avoid stop-and-go immediately after start** (if possible)
4. **In traffic, use manual mode temporarily** (hold in 2nd gear, reduce shift frequency)

After service and adaptation, your shifts will be as smooth as possible. But some cold jerk is normal for this transmission type."

**Mr. Kapoor's Reaction:**

"Thank you for explaining. The previous service center never told me this. I thought something was wrong. Now I understand it's just how this transmission works when cold. Your service made the warm shifts even smoother—I appreciate the thoroughness."

**Service Summary:**

- DSG oil and filter change: ₹4,500 (₹2,800 parts + ₹1,700 labor)
- Adaptation procedure: Included
- Test drives: Included
- **Outcome:** Optimal DSG performance, customer educated, trust built

---

**What Priya Demonstrated:**

1. **Proper DSG service procedure** (oil, filter, adaptation)
2. **Scan tool proficiency** (adaptation using VW-specific software)
3. **Diagnostic approach** (replicated customer complaint, identified cause)
4. **Customer education** (explained technical details simply)
5. **Professional service** (test drives, verification, documentation)

**Priya's Reputation:**

Mr. Kapoor became a regular customer and referred colleagues. "Priya understands DSG transmissions—she doesn't just change oil, she explains what's happening."

---

## Technical Deep Dive

### DSG Operating Principle

**Dual-Clutch Concept:**
- **Clutch 1:** Gears 1, 3, 5, 7, Reverse
- **Clutch 2:** Gears 2, 4, 6

**Pre-Selection:**
- Driving in 3rd gear (clutch 1 engaged, clutch 2 open)
- 4th gear already engaged (but clutch 2 open, so no power transmitted)
- When ECU decides to shift: Clutch 1 opens, Clutch 2 closes simultaneously
- Result: Instant shift, no power interruption

---

### Service Intervals

**VW/Skoda DSG:**
- **DQ200 (7-speed dry):** 60,000 km or 4 years
- **DQ250 (6-speed wet):** 60,000 km or 4 years
- **Severe duty (city traffic):** 40,000 km

---

### Common DSG Faults

1. **Mechatronic unit failure:** Erratic shifts, limp mode (common DQ200 issue 80,000-120,000 km)
2. **Clutch wear:** Slipping, shuddering (aggressive driving accelerates wear)
3. **Oil degradation:** Harsh shifts, fault codes (neglected service intervals)
4. **Cold-start jerk:** Normal for DQ200 dry-clutch (not a fault)

---

## Assessment

### Quiz Questions

**Q1:** After DSG oil change, what procedure is mandatory?

A) Reset service interval
B) Perform adaptation using scan tool
C) Test drive 100 km
D) No additional procedure needed

**Answer:** B) Perform adaptation using scan tool
**Explanation:** Adaptation relearns clutch bite points after oil change. Without it, shifts harsh, clutch may slip.

---

**Q2:** VW Polo TSI DSG (DQ200) has slight jerk during 1st→2nd shift when cold. What is the diagnosis?

A) Clutch worn, needs replacement
B) Mechatronic unit failed
C) Normal characteristic of dry-clutch DSG
D) Oil level low

**Answer:** C) Normal characteristic of dry-clutch DSG
**Explanation:** DQ200 dry-clutch shows slight cold-start jerk (friction material stiff when cold). Normal behavior, not a fault. Smooths out when warm.

---

## Cultural Context

**India-Specific:**
- VW Polo, Vento, Skoda Rapid popular in premium hatchback/sedan segment
- DSG marketed as performance feature (faster shifts)
- Customer awareness growing (initial DQ200 reliability concerns now addressed in newer revisions)
- Authorized service critical (requires VW-specific scan tool for adaptation)

---

## Lesson Summary

- **Session Outcome:** 1 (SO-4-3-3)
- **Technique:** Scenario-Based Learning
- **Character:** Priya (26, certified DSG technician)
- **Vehicle:** VW Polo 1.0 TSI 7-speed DSG (DQ200)
- **Service:** Oil/filter change + adaptation + cold-start jerk diagnosis
- **Key Concept:** DSG adaptation mandatory after service; cold jerk normal for dry-clutch
- **Duration:** 3 hours
- **Slides:** 45-50

---

**Framework Status:** ✅ Complete
**Generated:** 2026-01-12
**Ready for:** PowerPoint development
