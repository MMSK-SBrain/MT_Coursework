# Session 14: Case Study 2 - Tesla Autopilot System Analysis
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 90 minutes lecture + 30 minutes group work/discussion
**Approach:** Case-Study/Interactive with Comparative Analysis
**PPT Target:** 28-30 slides

---

## 🎯 Session Objectives (For Instructor)

By the end of this session, students will be able to:
- Analyze a complex automotive ADAS system using systems engineering frameworks
- Compare and contrast aerospace failures (Session 6: 737 MAX) with automotive failures
- Evaluate human-automation interaction design in safety-critical systems
- Apply systems safety analysis to autonomous and semi-autonomous systems
- Identify regulatory and verification challenges in novel automotive technologies
- Extract lessons learned applicable to future autonomous vehicle development
- Conduct comparative failure analysis across different transportation domains

**Mapped Learning Outcomes:**
- LO3 (Recognize important systems engineering and systems thinking strategies and practices)
- LO4 (Apply systems engineering practices and methods in automotive systems)
- LO5 (Analyse automotive systems using systems engineering approaches to increase performance)

---

## 🔗 Connection to Previous Sessions

This case study synthesizes and compares:

**Session 6 (Boeing 737 MAX):** Aerospace automation failure - we now analyze automotive equivalent
**Session 8 (Integration, V&V):** How V&V processes apply to ADAS systems
**Session 12 (Safety & Security):** ISO 26262 functional safety in practice
**Session 13 (Life Cycle Cost):** TCO implications of safety failures and recalls
**All Sessions:** Application of complete SE framework to real-world automotive system

**Today:** Second major case study, focusing on AUTOMOTIVE domain and comparing lessons across industries.

---

## 📖 INSTRUCTOR-LED STORY ARC

### **SETUP: The Autopilot Promise and Reality** (Slides 1-5, ~10 minutes)

#### Slide 1: Title
**Visual:** Split image - Tesla Autopilot marketing vs. accident investigation scene (respectful)

**Instructor Script:**
> "Welcome to Session 14, our second major case study. In Session 6, we analyzed the Boeing 737 MAX MCAS disaster - an aerospace automation failure that killed 346 people.
>
> Today, we analyze Tesla Autopilot - an AUTOMOTIVE automation system involved in multiple fatalities and hundreds of crashes.
>
> **This is not an anti-Tesla session.** Tesla pioneered advanced driver assistance in consumer vehicles. But their approach reveals critical systems engineering lessons about automation, human factors, testing, and regulation.
>
> **Our goal:** Understand what went wrong, why, and how systems engineering principles can prevent similar failures in your future work on autonomous and semi-autonomous vehicles."

**PPT Content:**
```
AUTOMOTIVE SYSTEMS ENGINEERING
AE ZG517 / AEL ZG517
Session 14: Case Study 2 - Tesla Autopilot System Analysis

Comparing Aerospace vs. Automotive Automation Failures
Learning from Incidents to Build Safer Autonomous Systems

Instructor: Sajeeth Kumar
Duration: 120 minutes
```

---

#### Slide 2: Case Study Overview - The Facts
**Visual:** Timeline of key Autopilot incidents

**Instructor Script:**
> "Let's establish the facts we'll be analyzing:
>
> **October 2015:** Tesla Autopilot launches (Version 1.0, Mobileye-based)
> **May 2016:** First fatal crash (Joshua Brown, Florida) - Autopilot fails to detect white truck against bright sky
> **October 2016:** Tesla announces 'Full Self-Driving' capability (hardware, software pending)
> **March 2018:** Walter Huang fatal crash (Mountain View, CA) - Autopilot steers into barrier
> **March 2019:** Jeremy Banner fatal crash (Florida) - Similar to 2016, truck crossing path
>
> **NHTSA Investigations (as of 2023):**
> - 40+ investigations into Tesla Autopilot crashes
> - 17+ fatalities attributed to Autopilot engagement
> - 736 crashes involving Autopilot (since 2019 data collection)
> - Pattern: Autopilot disengages seconds before impact (liability question)
>
> **Key Issues Identified:**
> - Driver monitoring inadequate (detects hands on wheel, not attention)
> - System operates outside Operational Design Domain (ODD)
> - Confusing nomenclature ('Autopilot', 'Full Self-Driving')
> - Inadequate testing and validation for edge cases
> - Regulatory gaps in ADAS oversight
>
> **Total impact:**
> - 17+ confirmed deaths (likely more)
> - Hundreds of injuries
> - Multiple NHTSA investigations
> - Recalls affecting 2+ million vehicles
> - Legal liability cases ongoing
> - Industry-wide implications for ADAS regulation
>
> **Our mission:** Analyze this through systems engineering lens and compare to 737 MAX."

---

#### Slide 3: Connection to Your Learning Journey
**Visual:** Comparison matrix: 737 MAX vs. Tesla Autopilot

**Instructor Script:**
> "Why are we studying BOTH an aerospace case (737 MAX) and automotive case (Tesla Autopilot)?
>
> **Because the systems engineering failures are remarkably similar:**
>
> | Aspect | Boeing 737 MAX | Tesla Autopilot |
> |--------|----------------|-----------------|
> | **System Type** | Flight automation | Driving automation |
> | **Failure Mode** | Single sensor dependency | Inadequate sensor fusion |
> | **Human Factors** | Pilots unaware of system | Drivers misunderstand capability |
> | **Naming** | MCAS hidden from pilots | 'Autopilot' implies full autonomy |
> | **Testing** | Inadequate failure mode testing | Inadequate edge case validation |
> | **Regulation** | FAA delegation to Boeing | NHTSA reactive, not proactive |
> | **Stakeholders** | Commercial pressure > safety | Market pressure > validation |
> | **Result** | 346 deaths | 17+ deaths, hundreds of crashes |
>
> **Same systems engineering failures, different domain.**
>
> **Today you'll learn:**
> - How SE principles apply across industries
> - Why human-automation interaction is critical
> - How to design and verify ADAS systems properly
> - Regulatory challenges for novel technologies
> - Lessons for your work on autonomous vehicles"

---

#### Slide 4: Learning Approach for Today
**Visual:** Interactive process flow

**Instructor Script:**
> "Today's structure mirrors Session 6:
>
> **Part 1 (Slides 1-10):** Case presentation - Technical system, incidents, facts
>
> **Part 2 (Slides 11-18):** Guided SE analysis - Requirements, architecture, V&V, human factors
>
> **Part 3 (Slides 19-21):** Comparative analysis - 737 MAX vs. Autopilot lessons
>
> **Part 4 (Slides 22-25):** Group work - Analyze specific aspects
>
> **Part 5 (Slides 26-28):** Synthesis - Lessons for autonomous vehicle development
>
> **Ground rules:**
> - Technical analysis, respectful to victims
> - Focus on SYSTEMS failures, not individual blame
> - Use SE frameworks from entire course
> - Compare lessons across aerospace and automotive domains"

---

#### Slide 5: What is Tesla Autopilot? - System Overview
**Visual:** Autopilot system architecture diagram

**Instructor Script:**
> "Before analyzing failures, understand what Autopilot actually is and what it claims to do.
>
> **Official Description (Tesla):**
> 'Autopilot advanced safety and convenience features are designed to assist you with the most burdensome parts of driving.'
>
> **SAE Automation Level:** Level 2 - Partial Driving Automation
> - System controls steering AND acceleration/braking
> - Driver MUST supervise at all times
> - Driver responsible for safe operation
>
> **Autopilot Features:**
> - Traffic-Aware Cruise Control (TACC)
> - Autosteer (lane keeping and following)
> - Auto Lane Change
> - Navigate on Autopilot (highway on-ramp to off-ramp)
> - Summon (parking lot maneuvering)
>
> **'Full Self-Driving' (FSD) Package (Additional $15,000):**
> - Traffic Light and Stop Sign Control
> - City street driving (beta)
> - **Still Level 2 - driver must supervise**
>
> **Key Point:** Despite name, 'Full Self-Driving' is NOT full autonomy. It's Level 2.
>
> **System Architecture (Hardware 3.0+):**
> - 8 cameras (360° coverage)
> - 12 ultrasonic sensors
> - Forward-facing radar (some versions)
> - Dual FSD Computer (redundant processing)
> - Neural network-based perception
> - No LiDAR (controversial decision)
>
> **Operational Design Domain (ODD) - Where it's SUPPOSED to work:**
> - Divided highways with clear lane markings
> - Good weather and lighting
> - Well-maintained roads
> - Driver actively supervising
>
> **Reality: System operates outside ODD because:**
> - No technical restrictions on where it activates
> - Minimal driver monitoring
> - Marketing implies broader capability
>
> This gap between designed ODD and actual use is a systems engineering failure."

---

### **TRIGGER: Understanding the Incidents** (Slides 6-10, ~15 minutes)

#### Slide 6: Incident 1 - Joshua Brown (May 2016)
**Visual:** Incident diagram showing vehicle, truck, and sensor limitations

**Instructor Script:**
> "Let's examine the first fatal crash in detail.
>
> **Date:** May 7, 2016
> **Location:** Williston, Florida (US Highway 27A)
> **Vehicle:** 2015 Tesla Model S with Autopilot 1.0 (Mobileye-based)
> **Victim:** Joshua Brown, 40, Tesla enthusiast
>
> **Sequence of Events:**
>
> **13:40:** Vehicle traveling 74 mph (9 mph over limit) with Autopilot engaged
> **13:40:05:** Tractor-trailer begins left turn across highway (crossing vehicle's path)
> **13:40:06-10:** Autopilot does NOT detect truck and does NOT brake
> - Camera fails to distinguish white truck against bright sky
> - Radar sees truck but classifies as 'overhead object' (false positive suppression)
> **13:40:10:** Vehicle collides with truck at full speed, passes underneath trailer
> **Result:** Joshua Brown dies from injuries, vehicle continues 100+ yards off road
>
> **Technical Failure Analysis:**
>
> **Sensor Failure Modes:**
> 1. **Camera:** High contrast scene (white truck, bright sky) - vision system failed to detect
> 2. **Radar:** Detected truck but classified as overhead sign/bridge (tuned to ignore)
> 3. **Sensor Fusion:** Failed - neither sensor triggered braking
>
> **Driver Monitoring Failure:**
> - Driver's hands detected on wheel periodically (satisfied monitoring)
> - Driver was watching movie (found playing on laptop after crash)
> - System did NOT detect driver's lack of visual attention
>
> **System Design Issues:**
> 1. Over-reliance on camera in challenging lighting
> 2. Radar tuned to minimize false positives (missed true positive)
> 3. Inadequate sensor fusion (should vote between sensors)
> 4. Driver monitoring only checks hands, not eyes/attention
> 5. No functional limitation on where Autopilot can engage
>
> **NHTSA Investigation Findings:**
> - Tesla's Autopilot performance 'not defective'
> - But: Recommended better driver monitoring
> - Driver misuse of system (watching video while driving)
>
> **Systems Engineering Question:** Is 'driver misuse' an acceptable answer, or a systems design failure?"

---

#### Slide 7: Incident 2 - Walter Huang (March 2018)
**Visual:** Mountain View crash scene with barrier and vehicle path

**Instructor Script:**
> "Second fatal crash reveals a DIFFERENT failure mode.
>
> **Date:** March 23, 2018
> **Location:** Mountain View, CA (US Highway 101)
> **Vehicle:** 2017 Tesla Model X with Autopilot 2.5
> **Victim:** Walter Huang, 38, Apple engineer
>
> **Sequence of Events:**
>
> **09:27:** Vehicle traveling on Highway 101 with Autopilot engaged
> **09:27:15:** Highway splits - left lanes continue 101, right exit to 85
> - Lane markings faded at gore point (triangular barrier area)
> **09:27:18:** Autopilot steers LEFT toward barrier (follows left lanes)
> - Should have detected barrier and disengaged
> **09:27:19:** Vehicle accelerates from 62 to 71 mph approaching barrier
> **09:27:20:** Autopilot disengages 1 second before impact (no driver input detected)
> **09:27:21:** Vehicle strikes barrier at 71 mph, battery fire
> **Result:** Walter Huang dies at hospital, vehicle destroyed
>
> **Critical Details:**
> - Huang had complained to family about Autopilot steering toward this same barrier previously
> - He continued using Autopilot despite known issue
> - Tesla data shows Huang's hands off wheel for 6 seconds before impact
> - Huang was likely using phone (not confirmed, device damaged in fire)
>
> **Technical Failure Analysis:**
>
> **Perception Failure:**
> 1. **Lane detection:** Confused by faded markings at gore point
> 2. **Barrier detection:** Failed to classify concrete barrier as obstacle
> 3. **Path planning:** Chose to follow lane lines (left) instead of road geometry
> 4. **Deceleration → Acceleration:** System accelerated approaching stopped traffic (trying to maintain set speed)
>
> **Driver Monitoring Failure:**
> - Hands off wheel for 6 seconds (system allows this)
> - No detection of phone use or distraction
>
> **System Design Issues:**
> 1. Autopilot operates on roads outside ODD (highway splits, gore points)
> 2. Lane-following algorithm prioritizes lane lines over obstacle detection
> 3. System disengages 1 second before crash (appears to shift liability to driver)
> 4. Inadequate driver monitoring - doesn't ensure driver ready to take over
>
> **NTSB Investigation Findings (2020):**
> - Tesla's Autopilot design 'contributed to crash'
> - Autopilot allowed use outside ODD
> - Driver monitoring insufficient
> - Driver was distracted (probable phone use)
> - Recommended: Improve driver monitoring, limit Autopilot to appropriate roads
>
> **Systems Engineering Question:** Who is responsible when automation works outside its design domain and driver doesn't supervise?"

---

#### Slide 8: Pattern Analysis - Common Failure Modes
**Visual:** Comparison table of multiple incidents

**Instructor Script:**
> "Let's look at patterns across multiple Autopilot crashes. NHTSA has investigated 40+ incidents. Common failure modes emerge:
>
> **Failure Mode 1: Stationary/Crossing Vehicle Detection (35% of crashes)**
> - Joshua Brown case: Crossing truck
> - Multiple crashes into parked emergency vehicles
> - Crashes into concrete barriers
> - **Root cause:** Perception system optimized for moving traffic, not stationary objects
>
> **Failure Mode 2: Lane Marking Confusion (25% of crashes)**
> - Walter Huang case: Gore point confusion
> - Crashes at highway exits with faded markings
> - Phantom braking due to adjacent lane markings
> - **Root cause:** Over-reliance on vision for lane detection
>
> **Failure Mode 3: Driver Inattention Not Detected (80% of crashes)**
> - Hands on wheel but eyes not on road
> - Drivers sleeping, using phone, reading
> - **Root cause:** Inadequate driver monitoring (torque sensor, not eye tracking)
>
> **Failure Mode 4: System Disengages Before Impact**
> - Pattern: Autopilot disengages 1-2 seconds before crash
> - Appears in crash data as 'driver was in control'
> - **Question:** Is this a safety feature or liability avoidance?
>
> **Failure Mode 5: Operation Outside ODD**
> - System functions on city streets (designed for highways)
> - Works in poor weather, at night, on unmarked roads
> - No geofencing or technical restrictions
> - **Root cause:** No ODD enforcement in system design
>
> **Statistical Context:**
> - Tesla claims Autopilot is safer than human driving
> - Tesla data (disputed): 1 crash per 4.85M miles with Autopilot vs. 1 per 1.5M miles US average
> - But: Confounding factors (highway vs. city, driver demographics, reporting bias)
> - NHTSA data (2023): 736 Autopilot crashes reported since 2019 (likely undercount)
>
> **The Systems Engineering Problem:** These are not random failures. They are SYSTEMATIC failures revealing gaps in requirements, design, testing, and validation."

---

### **RISING ACTION: Systematic SE Failure Analysis** (Slides 11-18, ~30 minutes)

#### Slide 9: Framework for Analysis - SE Lens
**Visual:** SE analysis framework

**Instructor Script:**
> "Now we apply our systems engineering frameworks, exactly as we did for 737 MAX.
>
> **Our Analysis Framework:**
>
> **1. Requirements Engineering Failures**
> - What requirements existed for Autopilot?
> - What requirements were missing?
> - Were they complete, verifiable, traceable?
>
> **2. System Architecture & Design**
> - Sensor architecture - redundancy and diversity
> - Perception algorithms - failure modes
> - Human-automation interaction design
>
> **3. Verification & Validation Failures**
> - What testing was done?
> - What edge cases were missed?
> - Real-world validation gaps
>
> **4. Human Factors Failures**
> - Driver understanding of system capabilities
> - Driver monitoring design
> - Naming and marketing implications
>
> **5. Regulatory and Standards Gaps**
> - How did Tesla get approval for deployment?
> - Where did oversight fail?
> - Comparison to aerospace regulation
>
> **6. Systems Thinking Failures**
> - Optimizing for feature deployment vs. safety validation
> - Fleet learning vs. individual vehicle safety
>
> **Let's work through each systematically, then compare to 737 MAX.**"

---

#### Slide 10: Analysis Part 1 - Requirements Failures
**Visual:** Requirements failure matrix

**Instructor Script:**
> "Let's analyze Tesla Autopilot through requirements engineering lens.
>
> **Critical Safety Requirements That Should Have Existed:**
>
> **SR-1: Operational Design Domain**
> ❌ **Missing:** 'Autopilot shall only operate within defined ODD (divided highways, good weather, clear markings)'
> - What exists: System can activate anywhere
> - Consequence: Operates in scenarios it wasn't designed for (city streets, poor markings, complex intersections)
>
> **SR-2: Obstacle Detection**
> ❌ **Inadequate:** 'Autopilot shall detect and avoid all obstacles in path'
> - What exists: Optimized for moving traffic, poor at stationary objects
> - Consequence: Crashes into barriers, parked vehicles, trucks
>
> **SR-3: Driver Monitoring**
> ❌ **Inadequate:** 'System shall ensure driver is attentive and ready to take control'
> - What exists: Torque sensor on steering wheel (hands on wheel)
> - Should be: Eye tracking, head pose, attention monitoring
> - Consequence: Drivers use phone, sleep, watch movies while 'supervising'
>
> **SR-4: Safe Handoff**
> ❌ **Missing:** 'System shall provide adequate time and warning for driver to resume control'
> - What exists: Disengages with minimal warning, sometimes 1 second before crash
> - Consequence: Driver cannot react in time
>
> **SR-5: Fail-Safe Behavior**
> ❌ **Inadequate:** 'System shall bring vehicle to safe stop if failure detected'
> - What exists: Disengages, expects driver to take over immediately
> - Should be: Detect driver readiness before handoff, execute safe stop if driver unresponsive
>
> **SR-6: Sensor Redundancy**
> ⚠️ **Partial:** 'Critical perception shall use diverse, redundant sensors'
> - What exists: Camera + radar + ultrasonics (but radar removed in some versions)
> - Issue: No LiDAR (single technology - vision only in newer models)
> - Consequence: Failures when vision fails (lighting, contrast, occlusion)
>
> **SR-7: System Capability Communication**
> ❌ **Absent:** 'System shall clearly communicate limitations to driver'
> - What exists: Name 'Autopilot' and 'Full Self-Driving' imply full autonomy
> - Consequence: Driver misunderstanding, over-reliance, complacency
>
> **Requirements Quality Analysis:**
>
> | Attribute | Status | Evidence |
> |-----------|--------|----------|
> | **Complete** | ❌ FAIL | Missing ODD, driver monitoring, safe handoff requirements |
> | **Verifiable** | ❌ FAIL | No clear verification criteria for 'ensure driver attention' |
> | **Traceable** | ❌ FAIL | Requirements not traced to ISO 26262 safety goals |
> | **Realistic** | ❌ FAIL | Expects driver to supervise indefinitely (not realistic) |
> | **Unambiguous** | ❌ FAIL | 'Autopilot' naming is ambiguous about capability |
>
> **Comparison to 737 MAX:**
> - Both: Missing critical safety requirements
> - Both: Inadequate requirements for human interaction
> - Both: Requirements didn't account for realistic human behavior
> - Difference: 737 MAX had aerospace standards (failed to follow), Tesla had no equivalent mandatory automotive ADAS standard"

---

#### Slide 11: Analysis Part 2 - Architecture & Design Failures
**Visual:** System architecture diagram with failure points highlighted

**Instructor Script:**
> "Now examine the system architecture through SE lens.
>
> **Sensor Architecture Analysis:**
>
> **Original Autopilot (HW1, 2015-2016):**
> - 1 forward camera (Mobileye)
> - 1 forward radar
> - 12 ultrasonic sensors
> - **Issue:** Single camera for critical perception (SPOF)
>
> **Autopilot 2.0-2.5 (2016-2019):**
> - 8 cameras (360° coverage)
> - 1 forward radar
> - 12 ultrasonic sensors
> - **Improvement:** Camera redundancy
> - **Issue:** Still relies heavily on vision, radar as secondary
>
> **Autopilot 3.0+ / FSD (2019+):**
> - 8 cameras (higher resolution)
> - No radar (removed in 2021+ models)
> - 12 ultrasonic sensors (removed in 2022+ models)
> - **Vision-only approach**
> - **Issue:** Single sensing modality (eliminates sensor diversity)
>
> **Architecture Principles Violated:**
>
> ❌ **Sensor Diversity:** Removed radar, relies only on vision
> - Industry standard: Camera + radar + LiDAR (diverse physics)
> - Tesla: Vision only (affected by lighting, weather, contrast, occlusion)
>
> ❌ **Graceful Degradation:** System disengages abruptly when confused
> - Should: Detect degradation, alert driver with adequate time, execute safe stop if needed
> - Actually: Sudden disengagement, immediate handoff to driver
>
> ❌ **Defense in Depth:** No backup safety layers
> - If vision fails, no backup (removed radar)
> - If driver not paying attention (common), no backup supervision
>
> ⚠️ **Redundancy:** Dual FSD computers (processing redundancy)
> - Good: Two independent processors
> - But: Both run same algorithms on same sensor data (common mode failure)
>
> **Perception Algorithm Design Issues:**
>
> **1. Optimized for False Positive Minimization**
> - Tuned to avoid phantom braking (customer complaints)
> - Result: Misses true positives (actual obstacles)
> - Classic SE trade-off: False negatives (misses) vs. false positives (false alarms)
>
> **2. Lane-Following vs. Obstacle Avoidance Priority**
> - System prioritizes staying in lane over avoiding obstacles
> - Walter Huang crash: Followed lane into barrier
> - Should: Obstacle avoidance overrides lane following
>
> **3. Neural Network Black Box**
> - Deep learning-based perception
> - Hard to verify all scenarios
> - No formal proof of safety
>
> **Driver Monitoring Architecture:**
>
> **Current Design:**
> - Torque sensor on steering wheel
> - Periodic checks (every 30-60 seconds)
> - Driver can satisfy by moving wheel slightly
>
> **Inadequacies:**
> - Doesn't detect visual attention (eyes on road)
> - Doesn't detect head pose (facing forward)
> - Doesn't detect drowsiness
> - Easily defeated (weights on wheel, etc.)
>
> **Industry Best Practice (e.g., GM Super Cruise):**
> - Eye tracking (infrared camera)
> - Head pose detection
> - Hands on wheel
> - Geofencing (only works on pre-mapped highways)
>
> **Comparison to 737 MAX Architecture:**
> - Both: Removed redundancy for cost/simplicity (MAX: single AOA, Tesla: removed radar)
> - Both: Inadequate human monitoring
> - Both: System can operate outside design intent
> - Difference: Tesla uses learning-based perception (harder to verify than MAX's deterministic code)"

---

#### Slide 12: Analysis Part 3 - Verification & Validation Failures
**Visual:** V-model showing V&V gaps

**Instructor Script:**
> "How was Autopilot tested and validated? Let's analyze through V&V lens.
>
> **Verification (Are we building the system right?):**
>
> **Unit Testing:**
> ✓ Individual components tested (cameras, radar, computer)
> ✓ Software modules tested in simulation
>
> **Integration Testing:**
> ⚠️ Partial - components integrated incrementally
> ❌ Issue: Limited testing of sensor fusion edge cases
>
> **System Testing:**
> ⚠️ Partial - tested on test tracks and public roads
> ❌ Issue: Edge cases (crossing trucks, faded markings, barriers) not systematically tested
>
> **Validation (Are we building the right system?):**
>
> **Does it meet stakeholder needs?**
> - ✓ Customers: Want convenience features (Yes, delivers)
> - ❌ Safety regulators: Want guaranteed safety (No, crashes occur)
> - ❌ Society: Want safe roads (No, crashes involving Autopilot)
>
> **Critical V&V Gaps:**
>
> **Gap 1: Edge Case Testing**
> - Autopilot tested in 'typical' scenarios
> - Edge cases (crossing vehicles, stationary objects, gore points) not systematically validated
> - **These edge cases are where crashes occur**
>
> **Gap 2: Real-World Operational Testing**
> - Tesla uses 'shadow mode' - system runs in background, logs what it would do
> - But: Not same as active intervention testing
> - Customers are de facto beta testers (not informed consent for safety-critical system)
>
> **Gap 3: Driver Behavior Validation**
> - System assumes driver will supervise attentively
> - Reality: Drivers become complacent, distracted
> - No validation that driver monitoring is adequate for realistic driver behavior
>
> **Gap 4: Independent Verification**
> - No independent third-party testing before deployment
> - NHTSA does not pre-approve ADAS systems (unlike FAA for aircraft)
> - Self-certification by manufacturer
>
> **Gap 5: Statistical Safety Validation**
> - How many test miles needed to prove safety?
> - Industry estimate: Billions of miles for autonomous safety proof
> - Tesla's approach: Deploy early, learn from fleet
> - **Question:** Is this ethical for safety-critical system?
>
> **Gap 6: Scenario Coverage**
> - No evidence of systematic scenario analysis (HAZOP, FMEA)
> - Crashes suggest scenarios not anticipated:
>   - Crossing vehicle in high-contrast lighting
>   - Faded lane markings at highway splits
>   - Emergency vehicles with flashing lights
>
> **Gap 7: Compliance to Standards**
> - ISO 26262 (Automotive Functional Safety) - voluntary, not mandated for ADAS in US
> - No evidence Tesla follows ISO 26262 ASIL D process
> - Contrast: Aviation follows DO-178C (mandatory)
>
> **Fleet Learning Approach (Tesla's Defense):**
>
> **Tesla argues:**
> - Fleet of 3M+ vehicles collects massive data
> - Neural networks improve with real-world data
> - Continuous improvement through OTA updates
>
> **SE Critique:**
> - Fleet learning doesn't replace systematic V&V
> - Individual vehicles are not validated before learning applied
> - Updates can introduce new failure modes
> - No safety case for each OTA update
>
> **Comparison to 737 MAX V&V:**
> - Both: Inadequate edge case testing
> - Both: Self-certification (Boeing ODA, Tesla no oversight)
> - Both: Optimistic assumptions about human behavior
> - Difference: Aerospace has mandatory standards, automotive ADAS does not (in US)"

---

#### Slide 13: Analysis Part 4 - Human Factors Catastrophic Failures
**Visual:** Human-automation interaction failure modes

**Instructor Script:**
> "This is where Tesla Autopilot most profoundly fails - human factors engineering.
>
> **Human Factors Principle:** 'Design systems for how humans actually behave, not how we wish they would behave.'
>
> **Autopilot's Human Factors Failures:**
>
> **Failure 1: Automation Complacency (Documented Phenomenon)**
>
> **Psychology of Automation:**
> - Humans are poor at sustained vigilance (monitoring tasks)
> - When automation works well, trust increases, attention decreases
> - This is not 'misuse' - it's predictable human behavior
>
> **Autopilot Design Assumes:**
> - Driver will remain attentive for entire trip
> - Driver will be ready to take over instantly
> - Driver will not become complacent
>
> **Reality:**
> - Drivers become complacent within minutes
> - Drivers use phones, eat, sleep
> - Drivers cannot resume control instantly from distraction
>
> **SE Failure:** System designed for idealized human, not actual human
>
> **Failure 2: Mode Confusion (What is the system doing?)**
>
> **Autopilot has multiple modes:**
> - TACC only (adaptive cruise, no steering)
> - Autosteer (cruise + lane keeping)
> - Navigate on Autopilot (plus lane changes)
> - Full Self-Driving (city streets)
>
> **Driver Confusion:**
> - Which mode am I in?
> - What will the system do?
> - What do I need to do?
>
> **Evidence from Crashes:**
> - Drivers unsure when Autopilot is engaged
> - Drivers unsure what Autopilot can/cannot handle
> - Mode transitions not clearly communicated
>
> **Failure 3: Misleading Nomenclature**
>
> **'Autopilot' implies:**
> - Aircraft autopilot (works without pilot intervention for extended periods)
> - Full automation
> - Can handle all situations
>
> **'Full Self-Driving' implies:**
> - Complete autonomy (SAE Level 5)
> - No driver intervention needed
>
> **Reality:**
> - Both are SAE Level 2 (partial automation)
> - Driver must supervise constantly
> - System can fail at any moment
>
> **Comparison to Aviation:**
> - Aircraft autopilot operates in controlled airspace
> - Pilots are trained professionals
> - Strict operational limitations
> - Autopilot is NOT used during critical phases (takeoff, landing)
>
> **Automotive Autopilot:**
> - Operates in uncontrolled environment (public roads)
> - Drivers are general public (untrained)
> - No operational limitations (can use anywhere)
> - Used during most critical scenarios (highway merges, intersections)
>
> **The naming is a systems engineering failure - sets wrong expectations**
>
> **Failure 4: Inadequate Driver Monitoring**
>
> **What's needed for Level 2 automation:**
> - Verify driver is visually attentive (eyes on road)
> - Verify driver is cognitively engaged (ready to intervene)
> - Provide adequate takeover time (4-7 seconds minimum)
>
> **What Tesla provides:**
> - Torque sensor (hands on wheel)
> - 30-60 second check intervals
> - 1-2 second takeover time (inadequate)
>
> **Comparison to GM Super Cruise:**
> - Eye tracking (infrared camera)
> - Head pose monitoring
> - Geofencing (only on pre-mapped highways)
> - If driver not attentive: escalating warnings → safe stop
>
> **Failure 5: Training and Education Gap**
>
> **Driver Training for Autopilot:**
> - Brief in-car tutorial
> - Written warnings in manual (most don't read)
> - On-screen disclaimers (click-through)
>
> **What's needed:**
> - Formal training (like pilot training for aircraft autopilot)
> - Testing/certification
> - Recurrent training
> - Clear operational limitations
>
> **SE Principle Violated:**
> 'Safety-critical systems require trained operators' - violated by consumer ADAS
>
> **Root Cause Analysis - Human Factors:**
>
> **Tesla optimized for:**
> - User experience (ease of use, minimal training)
> - Feature deployment speed (beat competitors)
> - Customer satisfaction (minimize false alarms)
>
> **Tesla did NOT optimize for:**
> - Realistic human behavior modeling
> - Safety margins for human error
> - Clear communication of limitations
>
> **This is the fundamental human factors systems engineering failure.**
>
> **Comparison to 737 MAX:**
> - Both: Assumed humans would perfectly supervise automation
> - Both: Inadequate human monitoring
> - Both: Insufficient training
> - Both: Marketing/naming implied more capability than existed
> - Same human factors failures, aerospace and automotive"

---

#### Slide 14: Analysis Part 5 - Regulatory and Standards Gaps
**Visual:** Comparison of regulatory frameworks

**Instructor Script:**
> "Now let's examine the regulatory environment - why did Tesla deploy this system without rigorous oversight?
>
> **Regulatory Comparison: Aerospace vs. Automotive:**
>
> | Aspect | Aerospace (FAA) | Automotive (NHTSA) |
> |--------|------------------|---------------------|
> | **Pre-Market Approval** | REQUIRED | NOT REQUIRED |
> | **Certification** | Mandatory, rigorous | Self-certification |
> | **Standards** | DO-178C (mandatory) | ISO 26262 (voluntary) |
> | **Testing Oversight** | FAA witnesses tests | No oversight |
> | **Safety Case** | Required before flight | Not required |
> | **Operational Limits** | Strictly enforced | Not enforced |
> | **Pilot/Driver Training** | Mandatory, certified | None required |
> | **Recalls** | Airworthiness Directives (mandatory) | Voluntary (mostly) |
>
> **Why the Gap?**
>
> **1. Historical Context:**
> - Aviation: Regulated heavily after crashes
> - Automotive: NHTSA created for vehicle safety, but focused on crashworthiness, not ADAS
> - ADAS is new - regulations lagging
>
> **2. Political/Economic Factors:**
> - US wants to lead in AV technology
> - Fear of over-regulation stifling innovation
> - Industry lobbying against mandatory standards
>
> **3. Regulatory Philosophy:**
> - Aviation: Prescriptive (must meet specific requirements)
> - Automotive: Performance-based (prove safety through data)
> - ADAS: Permissive (allowed unless proven unsafe)
>
> **4. Federal Preemption:**
> - NHTSA has authority, but limited resources
> - State-by-state AV laws create patchwork
> - No federal ADAS standard
>
> **Specific Regulatory Failures:**
>
> **Failure 1: No ODD Enforcement**
> - Autopilot can activate anywhere (city streets, poor weather, etc.)
> - No regulatory requirement to limit ODD
> - Contrast: Aviation autopilot has strict operational limits
>
> **Failure 2: No Driver Monitoring Standard**
> - No requirement for eye tracking or attention monitoring
> - Torque sensor (minimal) is sufficient
> - EU and China moving ahead (UN R157 requires DMS)
>
> **Failure 3: Misleading Marketing Allowed**
> - 'Autopilot' and 'Full Self-Driving' names not regulated
> - Creates false expectations
> - FTC has truth-in-advertising rules, but not enforced here
>
> **Failure 4: Reactive, Not Proactive Regulation**
> - NHTSA investigates after crashes occur
> - No pre-market safety validation
> - Contrast: FAA certifies before first flight
>
> **Recent Regulatory Actions (2023-2024):**
>
> **NHTSA Actions:**
> - Investigated 40+ Autopilot crashes
> - Issued recall for 2M+ vehicles (driver monitoring improvement)
> - Required data reporting (Standing General Order)
> - But: Still no mandatory ADAS standards
>
> **Industry Response:**
> - SAE J3016 (levels of automation) - defines terms, not safety
> - ISO 26262 (functional safety) - voluntary
> - Some manufacturers (e.g., GM) self-impose stricter requirements
>
> **International Comparison:**
>
> **Europe (UN R157):**
> - Requires driver monitoring system (DMS)
> - Requires hands on wheel AND eyes on road
> - Limits ALKS (Automated Lane Keeping) to 60 km/h
> - Type approval required before deployment
>
> **China (GB 38900):**
> - DMS required
> - AV classification system
> - Operational limits enforced
>
> **US:**
> - Voluntary guidelines only
> - No federal ADAS standard
> - State-by-state approach
>
> **The Regulatory Gap Enabled Tesla's Approach:**
> - Deploy first, iterate based on fleet data
> - Minimal driver monitoring
> - No operational restrictions
> - Limited oversight
>
> **SE Principle Violated:**
> 'Safety-critical systems require independent verification before deployment'
>
> **Comparison to 737 MAX Regulation:**
> - Both: Self-certification created conflict of interest
> - Both: Regulatory capture (FAA delegation, NHTSA permissiveness)
> - Both: Commercial pressure to deploy quickly
> - Difference: Aerospace has standards (not followed), automotive has no mandatory ADAS standard"

---

### **CLIMAX: Comparative Analysis** (Slides 19-21, ~15 minutes)

#### Slide 15: 737 MAX vs. Tesla Autopilot - Side-by-Side Comparison
**Visual:** Detailed comparison matrix

**Instructor Script:**
> "Let's now directly compare the two case studies. The parallels are striking.
>
> **Systems Engineering Failure Comparison:**
>
> | SE Area | Boeing 737 MAX MCAS | Tesla Autopilot |
> |---------|---------------------|-----------------|
> | **System Purpose** | Pitch stability augmentation | Driver assistance / partial automation |
> | **Automation Level** | Hidden from pilots | Visible but capabilities unclear |
> | **Human Role** | Pilots supervise, can override | Drivers supervise, can override |
> | **Failure Mode** | Single AOA sensor failure → nose down | Vision/radar failure → crashes into obstacles |
> | **Stakeholder Priority** | Airlines (training cost) > Safety | Market speed > Validation |
> | **Requirements** | Missing redundancy req's | Missing ODD, driver monitoring req's |
> | **Architecture** | Single sensor (SPOF) | Single modality (vision only), removed radar |
> | **Verification** | Inadequate failure mode testing | Inadequate edge case validation |
> | **Human Factors** | Pilots unaware of system | Drivers misunderstand capability |
> | **Training** | None provided | Minimal tutorial |
> | **Naming** | 'MCAS' hidden in docs | 'Autopilot', 'FSD' misleading |
> | **Regulation** | Self-certification (Boeing ODA) | No pre-market approval |
> | **Result** | 346 deaths, 2 crashes | 17+ deaths, 736+ crashes |
>
> **Commonalities - Root Causes:**
>
> **1. Commercial Pressure Over Safety:**
> - Both prioritized speed to market over thorough validation
> - Both cut corners on requirements and testing
>
> **2. Single Points of Failure:**
> - Both removed redundancy (MAX: 1 AOA sensor, Tesla: vision only)
> - Both violated defense-in-depth principles
>
> **3. Inadequate Human Factors:**
> - Both assumed perfect human supervision
> - Both provided inadequate training
> - Both had misleading nomenclature
>
> **4. Failed Verification:**
> - Both inadequately tested edge cases / failure modes
> - Both relied on self-certification
> - Both lacked independent validation
>
> **5. Regulatory Gaps:**
> - Both exploited weak regulatory oversight
> - Both self-certified safety
> - Both deployed before comprehensive safety validation
>
> **Differences:**
>
> | Aspect | 737 MAX | Tesla Autopilot |
> |--------|---------|-----------------|
> | **Domain** | Aerospace | Automotive |
> | **Standards** | Exist (DO-178C) but violated | No mandatory standard (US) |
> | **Training** | Pilots are professionals | Drivers are general public |
> | **Environment** | Controlled airspace | Uncontrolled public roads |
> | **Deployment** | Few aircraft | Millions of vehicles |
> | **Iteration** | Expensive to update | Easy OTA updates |
> | **Consequence** | Grounding possible | Recall difficult to enforce |
>
> **Key Insight:**
> Same systems engineering failures manifest across industries.
> The SE principles are universal - requirements, architecture, V&V, human factors, standards.
>
> **If automotive follows aerospace path:**
> - Current: Permissive, deploy first
> - After major disaster: Reactionary regulation
> - Future: Mandatory standards, pre-market approval
>
> **The question:** Will automotive learn from aerospace failures, or repeat them at larger scale?"

---

#### Slide 16: Lessons Learned - Comparative Analysis
**Visual:** Lessons learned matrix

**Instructor Script:**
> "What can we learn by comparing these failures?
>
> **LESSON 1: Systems Engineering Principles Are Universal**
> - Same SE failures (requirements, architecture, V&V, human factors) cause disasters in aerospace AND automotive
> - SE frameworks apply across domains
> - **Your takeaway:** SE skills transfer across industries
>
> **LESSON 2: Automation Without Human Factors is Dangerous**
> - Both cases: Assumed humans would perfectly supervise automation
> - Reality: Humans are poor at monitoring tasks
> - **Your takeaway:** Design for realistic human behavior, not idealized
>
> **LESSON 3: Single Points of Failure Are Never Acceptable**
> - MAX: Single AOA sensor
> - Tesla: Vision-only perception (removed radar)
> - **Your takeaway:** Safety-critical systems require redundancy and diversity
>
> **LESSON 4: Edge Cases and Failure Modes Must Be Systematically Tested**
> - Both missed critical edge cases in testing
> - Both deployed without comprehensive validation
> - **Your takeaway:** Use FMEA, HAZOP, systematic scenario analysis
>
> **LESSON 5: Marketing and Naming Affect Safety**
> - 'MCAS' hidden from pilots → lack of awareness
> - 'Autopilot' / 'Full Self-Driving' → over-reliance
> - **Your takeaway:** System naming and communication are SE responsibilities
>
> **LESSON 6: Self-Certification Creates Conflict of Interest**
> - Both relied on self-certification under commercial pressure
> - Both needed independent verification
> - **Your takeaway:** Independent V&V is not optional for safety-critical systems
>
> **LESSON 7: Regulations Lag Technology**
> - Aerospace: Standards existed, were circumvented
> - Automotive: Standards don't exist (for ADAS in US)
> - **Your takeaway:** Engineers must self-impose rigorous SE even when not required
>
> **LESSON 8: Incremental Deployment ≠ Safety Validation**
> - Tesla argument: Fleet learning improves safety
> - Reality: Each vehicle must be validated before deployment
> - **Your takeaway:** Data-driven improvement doesn't replace systematic V&V
>
> **LESSON 9: Cost of Failure Far Exceeds Cost of Proper SE**
> - MAX: $20B+ costs, brand damage, criminal charges
> - Tesla: Ongoing investigations, recalls, legal liability
> - **Your takeaway:** Invest in SE upfront, avoid catastrophic costs later
>
> **LESSON 10: Engineers Have Professional and Ethical Responsibility**
> - Both cases: Engineers raised concerns, were overruled
> - Both: Lives lost because safety was deprioritized
> - **Your takeaway:** Speak up when safety is compromised. It's your professional duty."

---

#### Slide 17: The Path Forward - Autonomous Vehicle Development
**Visual:** Roadmap for safe AV development

**Instructor Script:**
> "Given these lessons, how should we develop autonomous vehicles properly?
>
> **Systems Engineering Framework for Safe AV Development:**
>
> **1. Rigorous Requirements Engineering**
> ✓ Define clear Operational Design Domain (ODD)
> ✓ Specify all safety requirements (ISO 26262 ASIL D)
> ✓ Include human factors requirements
> ✓ Trace requirements to verification methods
>
> **2. Robust System Architecture**
> ✓ Sensor diversity (camera + radar + LiDAR)
> ✓ Redundancy for all safety-critical functions
> ✓ Defense in depth (multiple safety layers)
> ✓ Fail-safe and fail-operational design
>
> **3. Comprehensive V&V**
> ✓ Systematic scenario analysis (HAZOP, FMEA, fault trees)
> ✓ Simulation testing (billions of virtual miles)
> ✓ Track testing (thousands of real miles, edge cases)
> ✓ Public road testing (controlled, with safety driver)
> ✓ Independent third-party verification
>
> **4. Human-Centered Design**
> ✓ Design for realistic human behavior
> ✓ Adequate driver monitoring (eye tracking for Level 2)
> ✓ Clear mode indication and communication
> ✓ Adequate takeover time (7+ seconds)
> ✓ Safe fallback if driver unresponsive
>
> **5. Appropriate Automation Levels**
> ✓ Level 2 (partial): Strict driver monitoring, geofencing
> ✓ Level 3 (conditional): Only where validated, safe handoff
> ✓ Level 4 (high): ODD-restricted, no driver required
> ✓ Level 5 (full): Decades away, requires regulatory framework
>
> **6. Regulatory Compliance and Standards**
> ✓ Follow ISO 26262 (functional safety)
> ✓ Follow ISO/PAS 21448 (SOTIF - safety of intended functionality)
> ✓ Comply with UN R157 (DMS requirements)
> ✓ Advocate for mandatory ADAS standards
>
> **7. Transparent Communication**
> ✓ Accurate naming (not 'Autopilot', not 'Full Self-Driving' for Level 2)
> ✓ Clear capability communication to drivers
> ✓ Honest marketing of limitations
> ✓ Regular safety transparency reports
>
> **8. Continuous Improvement with Safety Validation**
> ✓ Fleet data collection for learning
> ✓ Every OTA update validated before deployment
> ✓ Safety case for each update
> ✓ Treat public roads as production, not testing environment
>
> **9. Independent Oversight**
> ✓ Third-party testing (e.g., Euro NCAP, IIHS)
> ✓ Regulatory pre-market approval
> ✓ Ongoing monitoring and audits
>
> **10. Safety Culture**
> ✓ Safety is priority #1, above schedule and cost
> ✓ Engineers empowered to stop unsafe deployment
> ✓ Lessons learned from incidents drive improvement
> ✓ Transparent about failures
>
> **This is the SE framework for safe AVs. Anything less invites disaster.**"

---

### **RESOLUTION: Group Work and Synthesis** (Slides 22-28, ~30 minutes)

#### Slide 18: Group Work Instructions
**Visual:** Activity structure

**Instructor Script:**
> "Now it's your turn. You'll work in groups to analyze specific aspects of Autopilot and propose solutions.
>
> **Group Activity (30 minutes):**
>
> **Step 1: Form groups (4-5 students)**
>
> **Step 2: Choose one topic:**
>
> **Topic 1: Requirements Rewrite**
> - Write complete safety requirements for Level 2 driving automation
> - Include: ODD, sensor requirements, driver monitoring, fail-safe behavior
> - Make them complete, verifiable, traceable
>
> **Topic 2: Architecture Redesign**
> - Propose sensor architecture with redundancy and diversity
> - Design driver monitoring system
> - Define fail-safe behaviors
>
> **Topic 3: V&V Plan**
> - Create comprehensive V&V plan for ADAS
> - Include scenario analysis (edge cases to test)
> - Define acceptance criteria
>
> **Topic 4: Human Factors Improvement**
> - Redesign driver-automation interaction
> - Propose driver training program
> - Create clear communication strategy
>
> **Topic 5: Regulatory Framework**
> - Propose mandatory ADAS standard for US
> - Compare to UN R157, ISO 26262
> - Include enforcement mechanisms
>
> **Topic 6: Comparative Analysis**
> - Compare Autopilot to GM Super Cruise, Waymo, other ADAS
> - Identify what makes a system safer
> - Propose best practices
>
> **Deliverable:** 3-minute presentation with SE-backed recommendations"

---

#### Slide 19: Group Presentations and Discussion
(Instructor facilitates presentations and synthesis)

---

#### Slide 20: Final Synthesis - Key Takeaways
**Visual:** Summary infographic

**Instructor Script:**
> "Let's synthesize what we've learned across both case studies.
>
> **Session 6 (737 MAX) + Session 14 (Autopilot) = Universal SE Lessons:**
>
> ✓ **Requirements engineering is critical** - incomplete requirements kill people
> ✓ **Human factors cannot be ignored** - design for realistic humans
> ✓ **Single points of failure are unacceptable** - redundancy saves lives
> ✓ **Verification must be independent** - self-certification fails
> ✓ **Edge cases must be systematically tested** - crashes happen at edges
> ✓ **Standards exist for a reason** - follow them rigorously
> ✓ **Commercial pressure cannot override safety** - ethical responsibility
> ✓ **Automation changes human role** - must be carefully designed
> ✓ **Naming and communication affect safety** - be accurate and honest
> ✓ **SE processes prevent disasters** - skipping them invites tragedy
>
> **For Your Career in Automotive SE:**
>
> You will work on ADAS, autonomous vehicles, connected systems. You will face:
> - Time to market pressure
> - Cost constraints
> - Cutting-edge technology
> - Regulatory uncertainty
>
> **Your responsibility:** Apply rigorous SE to save lives.
>
> **Remember:**
> - 346 people died because aerospace SE was compromised
> - 17+ people died because automotive ADAS SE was inadequate
> - Future deaths can be prevented by YOU applying SE properly
>
> **That's why you're learning this. That's why it matters.**"

---

#### Slide 21: Assignment and Next Session Preview
**Visual:** Assignment details

**Instructor Script:**
> "**Assignment (Due before Session 15):**
>
> **Comparative Case Study Analysis Paper (4-5 pages):**
>
> Choose ONE of the following:
> 1. Compare 737 MAX and Tesla Autopilot failures - identify common SE failures
> 2. Analyze another ADAS system (GM Super Cruise, Waymo, Comma.ai) - what makes it safer?
> 3. Propose comprehensive SE framework for Level 4 autonomous shuttle deployment
>
> **Required Elements:**
> - SE analysis using frameworks from Sessions 1-14
> - Requirements, architecture, V&V, human factors analysis
> - Lessons learned and recommendations
> - Professional presentation with references
>
> **Next Session (Session 15): Technical Management Processes**
> - Configuration management
> - Risk management deep dive
> - Quality assurance
> - Lessons from case studies inform technical management
>
> **Final Sessions:**
> - Session 16: Emerging Trends (AI, digital engineering, autonomous systems)
> - Session 17: Course synthesis and future of automotive SE
>
> **Questions?**"

---

## 📊 PPT DESIGN GUIDANCE

(Similar to Session 6 framework)

---

## 🎯 INSTRUCTOR NOTES

### Pedagogical Strategy:
- **Comparative case study learning:** Analyze automotive failure, compare to aerospace
- **Pattern recognition:** Same SE failures across domains
- **Application:** Students apply SE frameworks to real-world automotive system
- **Professional development:** Understand ethical responsibilities in ADAS/AV development

### Emotional Considerations:
- Respectful treatment of real tragedies
- Balance between technical analysis and human impact
- Empower students to prevent future incidents

### Timing Management:
- Core content: 60 minutes
- Group work: 30 minutes (strictly enforced)
- Presentations: 3 min per group
- Synthesis: 10 minutes

---

## ✅ Session Success Criteria

Students leave able to:
- ✓ Analyze ADAS systems using complete SE framework
- ✓ Compare aerospace and automotive automation failures
- ✓ Identify human factors failures in automation design
- ✓ Understand regulatory gaps in ADAS oversight
- ✓ Propose SE solutions for safe autonomous vehicle development
- ✓ Recognize professional responsibility in safety-critical automotive systems

**Most Importantly:**
Students understand that ADAS and AV development requires rigorous SE. Shortcuts kill people. Their future work will determine whether automotive repeats aviation's mistakes or learns from them.

---

**End of Framework**
