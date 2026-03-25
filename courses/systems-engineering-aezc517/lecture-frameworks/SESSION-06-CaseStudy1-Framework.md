# Session 6: Case Study 1 - Boeing 737 MAX MCAS System
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 90 minutes lecture + 30 minutes group work/discussion
**Approach:** Case-Study/Interactive with Guided Analysis
**PPT Target:** 28-30 slides

---

## 🎯 Session Objectives (For Instructor)

By the end of this session, students will be able to:
- Analyze a real-world complex system failure using systems engineering principles
- Identify requirements engineering failures and their cascading consequences
- Apply root cause analysis using SE frameworks (stakeholder analysis, V&V, traceability)
- Evaluate design decisions against systems thinking principles
- Recognize the critical importance of systems-level thinking in safety-critical systems
- Extract actionable lessons learned for future engineering practice
- Conduct collaborative technical analysis and present findings effectively

**Mapped Learning Outcomes:**
- LO3 (Recognize important systems engineering and systems thinking strategies and practices)
- LO4 (Apply systems engineering practices and methods in automotive systems)
- LO5 (Analyse automotive systems using systems engineering approaches to increase performance)

---

## 🔗 Connection to Previous Sessions

This case study synthesizes ALL concepts from Sessions 1-5:

**Session 1 (Introduction):** Real-world engineering failures - we now analyze one in depth
**Session 2 (SE Fundamentals):** ISO/IEC 15288 processes - we'll see what happens when they break
**Session 3 (Traditional vs MBSE):** Systems complexity management - failure to manage complexity
**Session 4 (Requirements Engineering):** Stakeholder needs, requirements quality - critical failures here
**Session 5 (System Design):** Architecture, CONOPS, trade studies - flawed design decisions

**Today:** We put it ALL together in a real-world tragedy that cost 346 lives.

---

## 📖 INSTRUCTOR-LED STORY ARC

### **SETUP: The Tragedy** (Slides 1-5, ~10 minutes)

#### Slide 1: Title
**Visual:** Split image - Boeing 737 MAX in flight (professional) + memorial for victims (respectful)
**Instructor Script:**
> "Welcome to Session 6. Today's session is different. We're not learning new concepts. Instead, we're applying everything you've learned in Sessions 1-5 to analyze one of the most significant aerospace engineering failures of the 21st century.
>
> The Boeing 737 MAX MCAS system failure resulted in 346 deaths across two crashes. This is not an academic exercise - these were real people. As engineers, we have a profound responsibility to learn from this tragedy so it never happens again.
>
> Today, we honor those lives by understanding EXACTLY what went wrong from a systems engineering perspective."

#### Slide 2: Connection to Your Learning Journey
**Visual:** Timeline showing Sessions 1-5 leading to Session 6
**Instructor Script:**
> "Over the past five sessions, you've built a comprehensive systems engineering toolkit:
>
> ✓ **Session 1**: Why SE matters - we saw failures in hindsight
> ✓ **Session 2**: SE processes and the V-model framework
> ✓ **Session 3**: MBSE and managing complexity
> ✓ **Session 4**: Requirements engineering fundamentals
> ✓ **Session 5**: System architecture and design principles
>
> **Today**: You'll use EVERY one of these tools to conduct a professional-grade failure analysis.
>
> By the end of this session, you'll understand how systems engineering principles - properly applied - could have prevented this disaster. More importantly, you'll develop the critical thinking skills to recognize similar risks in your own work."

#### Slide 3: Case Study Overview - The Facts
**Visual:** Timeline of key events
**Instructor Script:**
> "Here are the facts we'll be analyzing:
>
> **October 29, 2018 - Lion Air Flight 610**
> - Boeing 737 MAX 8, 13 minutes after takeoff
> - Crashed into Java Sea, Indonesia
> - 189 fatalities (all aboard)
>
> **March 10, 2019 - Ethiopian Airlines Flight 302**
> - Boeing 737 MAX 8, 6 minutes after takeoff
> - Crashed near Bishoftu, Ethiopia
> - 157 fatalities (all aboard)
>
> **March 13, 2019 - Global Grounding**
> - All 737 MAX aircraft grounded worldwide
> - Grounding lasted 20 months (lifted Dec 2020)
>
> **Investigations identified:**
> - MCAS (Maneuvering Characteristics Augmentation System) as primary cause
> - Multiple systems engineering process failures
> - Organizational and regulatory failures
>
> **Total impact:**
> - 346 lives lost
> - $20+ billion in costs to Boeing
> - Criminal charges against Boeing
> - FAA certification process reforms
> - Permanent damage to Boeing's reputation
>
> **Our mission today:** Understand the SE failures that led to this tragedy."

#### Slide 4: Learning Approach for Today
**Visual:** Interactive process flow diagram
**Instructor Script:**
> "Today's session is structured differently. This is an ACTIVE learning experience:
>
> **Part 1 (Slides 1-12):** I'll present the case - technical background, what happened, initial facts
>
> **Part 2 (Slides 13-20):** Guided analysis - We'll systematically analyze failures using SE frameworks you've learned
>
> **Part 3 (Slides 21-24):** Group work (30 min) - You'll work in teams to analyze specific aspects
>
> **Part 4 (Slides 25-28):** Group presentations and synthesis - Teams share findings
>
> **Part 5 (Slides 29-30):** Lessons learned - What this means for your career
>
> **You will need:** Your notes from Sessions 1-5, pen and paper, critical thinking caps on.
>
> **Ground rules:**
> - This is a technical analysis, conducted with respect for victims
> - Focus on SYSTEMS FAILURES, not individual blame
> - Use SE frameworks we've learned
> - Ask questions anytime"

#### Slide 5: Case Study Objectives - What We're Analyzing
**Visual:** Analysis framework diagram
**Instructor Script:**
> "Specifically, we're investigating these systems engineering questions:
>
> **1. Stakeholder Analysis:** Who were the stakeholders, and whose needs were prioritized? Whose needs were ignored?
>
> **2. Requirements Engineering:** What requirements failures occurred? Were requirements complete, verifiable, traceable?
>
> **3. System Architecture:** How did design choices create single points of failure? Where did the architecture violate SE principles?
>
> **4. Verification & Validation:** What V&V processes failed? How did testing miss critical failure modes?
>
> **5. Human Factors:** How did the system design ignore human-system integration?
>
> **6. Systems Thinking:** Where did component-level optimization harm system-level safety?
>
> By the end, you'll have concrete answers to each question, backed by evidence."

---

### **TRIGGER: Understanding the Technical System** (Slides 6-9, ~12 minutes)

#### Slide 6: Technical Background - The 737 MAX Design Challenge
**Visual:** Comparison diagram of 737 NG vs 737 MAX
**Instructor Script:**
> "To understand what went wrong, we need to understand the engineering problem Boeing faced.
>
> **The Business Context:**
> - 2010: Airbus launches A320neo with more efficient engines → threatens Boeing's market share
> - Boeing's options:
>   - Option 1: Design clean-sheet new aircraft (10+ years, $15+ billion)
>   - Option 2: Re-engine existing 737 with modern engines (4-5 years, $2-3 billion)
>
> **Boeing chose Option 2: The 737 MAX**
>
> **The Engineering Challenge:**
> The new LEAP-1B engines were larger and more efficient, but created a physical problem:
>
> - New engines: 69.4 inches diameter (vs 61.6 inches on 737 NG)
> - Ground clearance issue: Engines had to be mounted further forward and higher
> - **Consequence:** Changed aircraft aerodynamics and pitch behavior
>
> **Specific aerodynamic change:**
> - At high angles of attack (nose-up attitude), the forward engine placement created additional LIFT at the engine nacelles
> - This additional lift created nose-UP pitching moment
> - Result: Aircraft had tendency to pitch nose-up more aggressively at high angles of attack
> - **This violated FAA certification requirements** for handling characteristics similar to previous 737 variants
>
> **Boeing's solution:** MCAS - Maneuvering Characteristics Augmentation System
>
> **Critical decision:** Make MCAS transparent to pilots so MAX could be certified as variant, not new aircraft (avoiding expensive pilot retraining)"

#### Slide 7: What is MCAS? - System Overview
**Visual:** MCAS system architecture diagram showing inputs, processing, outputs
**Instructor Script:**
> "Let me explain what MCAS actually does:
>
> **MCAS Purpose (Official):**
> 'Provide pitch stability augmentation to meet regulatory requirements for handling characteristics'
>
> **MCAS Function (Plain English):**
> When aircraft nose is too high (high angle of attack), automatically push nose down to prevent stall
>
> **MCAS System Architecture:**
>
> **Inputs:**
> - Angle of Attack (AOA) sensor (measures how high nose is relative to airflow)
> - Flaps position (MCAS only active when flaps up = cruise configuration)
> - Airspeed
> - Altitude
>
> **Processing:**
> - Flight Control Computer (FCC)
> - MCAS software algorithm
>
> **Output:**
> - Horizontal stabilizer trim commands (pushes nose down)
>
> **Design Parameters (as originally certified):**
> - Activation threshold: AOA > specific value (depends on speed/altitude)
> - Authority: 0.6 degrees of stabilizer movement
> - Activation: One time per high-AOA event
> - Pilot override: Trim switches
>
> **This sounds reasonable, right? So what went catastrophically wrong?**
>
> Let's look at what ACTUALLY shipped on the aircraft."

#### Slide 8: The Fatal Design Changes - What Actually Shipped
**Visual:** Side-by-side comparison table: Original Design vs Final Design
**Instructor Script:**
> "Here's where the systems engineering failures begin. Compare original MCAS design to what actually flew:
>
> | Design Aspect | Original Certification | Final Production Version | Impact |
> |---------------|----------------------|-------------------------|---------|
> | **Authority (movement range)** | 0.6 degrees | **2.5 degrees** (4x increase) | Can overpower pilot inputs |
> | **Activation frequency** | Once per event | **Repeatedly** (every 5 seconds) | Relentless nose-down commands |
> | **AOA sensors used** | Designed for two | **Single sensor** (no redundancy) | Single point of failure |
> | **Pilot training** | Comprehensive | **None** (not in manual) | Pilots unaware of system |
> | **Pilot notification** | AOA disagree alert | **Optional extra** ($80,000 feature) | Pilots flew blind to sensor failure |
> | **V&V testing** | Full envelope | **Limited scenarios** | Didn't catch failure modes |
>
> **Read that table again carefully.**
>
> **Key observation:** The system that crashed two aircraft was FUNDAMENTALLY DIFFERENT from the system that was originally certified. These changes happened incrementally during development.
>
> **Systems engineering question:** How did these changes get approved without triggering re-certification or safety analysis?"

#### Slide 9: The Accident Sequence - What Happened
**Visual:** Timeline diagram showing sequence of events in both crashes
**Instructor Script:**
> "Let me walk you through what happened in both crashes. The sequence is remarkably similar:
>
> **Lion Air Flight 610 - October 29, 2018:**
>
> **0:00** - Takeoff, Jakarta
> **0:01** - Left AOA sensor fails (reports 20° high - FALSE reading due to damage)
> **0:02** - MCAS activates based on faulty sensor → pushes nose down
> **0:02** - Pilots pull nose up using control column
> **0:02** - MCAS reactivates after 5 seconds → pushes nose down again
> **0:03-0:13** - Pilots fight MCAS over 20 times, not understanding what's happening
> **0:11** - Pilots try electric trim cutoff (good instinct) but re-enable it (attempting to use electric trim)
> **0:13** - Aircraft exceeds structural limits, crashes into Java Sea
> **Result:** 189 deaths
>
> **Ethiopian Airlines Flight 302 - March 10, 2019:**
>
> **0:00** - Takeoff, Addis Ababa
> **0:01** - Left AOA sensor fails (reports erroneous high angle)
> **0:01** - MCAS activates → nose down
> **0:02** - Pilots fight MCAS, check emergency procedures
> **0:03** - Pilots disable electric trim (correct procedure)
> **0:04** - At high speed, cannot manually trim due to aerodynamic forces
> **0:05** - Pilots re-enable electric trim to attempt recovery
> **0:05** - MCAS reactivates immediately
> **0:06** - Loss of control, crash near Bishoftu
> **Result:** 157 deaths
>
> **Critical observation:**
> Ethiopian pilots DID follow the emergency procedure Boeing issued after Lion Air. They disabled electric trim. But they were in an impossible situation - couldn't manually trim at high speed, and re-enabling electric trim also re-enabled MCAS.
>
> **This was a systems engineering failure, not pilot error.**"

---

### **RISING ACTION: Systematic SE Failure Analysis** (Slides 10-20, ~35 minutes)

#### Slide 10: Framework for Our Analysis - The SE Lens
**Visual:** Analysis framework showing SE process areas
**Instructor Script:**
> "Now we're going to put on our systems engineering analyst hat. I'll guide you through a systematic analysis using the frameworks you learned in Sessions 1-5.
>
> **Our Analysis Framework:**
>
> **1. Stakeholder Analysis** (Session 4)
> - Who were the stakeholders?
> - Whose needs were prioritized?
> - Whose needs were ignored?
>
> **2. Requirements Engineering Failures** (Session 4)
> - What requirements existed?
> - What requirements were missing?
> - Were requirements verifiable, traceable, complete?
>
> **3. System Architecture & Design Failures** (Session 5)
> - Single points of failure
> - Design principles violated
> - Trade study failures
>
> **4. Verification & Validation Failures** (Session 2)
> - What testing was done?
> - What testing was missed?
> - V-model process breakdowns
>
> **5. Systems Thinking Failures** (Session 1-2)
> - Component vs system optimization
> - Emergent behavior not anticipated
> - Organizational boundaries affecting technical decisions
>
> Let's work through each systematically."

#### Slide 11: Analysis Part 1 - Stakeholder Failures
**Visual:** Stakeholder power/interest matrix
**Instructor Script:**
> "Let's start with stakeholder analysis, exactly as we learned in Session 4.
>
> **Stakeholders in 737 MAX Development:**
>
> | Stakeholder | Needs/Interests | Power/Influence | How They Were Treated |
> |-------------|-----------------|-----------------|----------------------|
> | **Passengers** | Safety, survival | Low (indirect) | ❌ **IGNORED** - Never consulted, needs deprioritized |
> | **Pilots** | Situational awareness, controllability, training | Medium | ❌ **EXCLUDED** - Not told about MCAS, no training |
> | **Airlines** | Low training costs, fleet commonality | HIGH | ✅ **PRIORITIZED** - Got what they wanted (no retraining) |
> | **Boeing shareholders** | Profit, market share, fast delivery | HIGH | ✅ **PRIORITIZED** - Fast to market, low cost |
> | **FAA (regulator)** | Safety, regulatory compliance | HIGH | ⚠️ **COMPROMISED** - Delegated authority to Boeing |
> | **Maintenance crews** | Diagnosability, safety alerts | Low | ❌ **IGNORED** - AOA disagree alert was optional |
>
> **Systems Engineering Principle Violated:**
> 'A system must balance the needs of ALL stakeholders, with safety-critical stakeholders having priority.'
>
> **What Actually Happened:**
> Commercial interests (airlines, shareholders) were prioritized over safety-critical stakeholders (passengers, pilots).
>
> **Key Decision Point:**
> The decision to hide MCAS from pilots was driven by airline customer demand to avoid pilot retraining costs ($1M+ per airline). This saved airlines money but removed pilot awareness of a critical system.
>
> **Question for reflection:** Who should have been at the requirements review meetings but wasn't?"

#### Slide 12: Analysis Part 2 - Requirements Engineering Failures
**Visual:** Requirements failure matrix
**Instructor Script:**
> "Now let's analyze this through a requirements engineering lens - Session 4 material.
>
> **Critical Requirements That Should Have Existed:**
>
> **Safety Requirements (Missing or Inadequate):**
>
> ❌ **SR-1:** 'MCAS shall use redundant AOA sensors with disagree logic'
> - What existed: Used single sensor
> - Consequence: Single point of failure
>
> ❌ **SR-2:** 'MCAS authority shall be limited such that pilots can override with normal control inputs'
> - What existed: 2.5° authority could overpower pilots
> - Consequence: Pilots couldn't override
>
> ❌ **SR-3:** 'MCAS shall activate maximum once per high-AOA event'
> - What existed: Repeated activation every 5 seconds
> - Consequence: Relentless nose-down commands
>
> ❌ **SR-4:** 'Pilots shall be alerted to AOA sensor disagreement'
> - What existed: Alert was optional extra feature
> - Consequence: Pilots unaware of sensor failure
>
> ❌ **SR-5:** 'MCAS operation shall be documented in pilot training materials'
> - What existed: Not mentioned in manuals
> - Consequence: Pilots couldn't diagnose or respond
>
> **Requirements Quality Failures:**
>
> Let's evaluate existing requirements against attributes from Session 4:
>
> | Requirement Attribute | Status | Evidence |
> |----------------------|--------|----------|
> | **Complete** | ❌ FAILED | Missing redundancy, pilot notification, authority limits |
> | **Verifiable** | ❌ FAILED | No verification that pilots could handle MCAS failures |
> | **Traceable** | ❌ FAILED | Changes to MCAS authority not traced to safety analysis |
> | **Unambiguous** | ⚠️ PARTIAL | Authority limits were ambiguous during development |
> | **Consistent** | ❌ FAILED | MCAS contradicted principle that pilots are final authority |
>
> **The Traceability Failure:**
> When MCAS authority was increased from 0.6° to 2.5°, this change was NOT traced back to:
> - Safety requirements
> - Hazard analysis (FMEA, FTA)
> - Pilot training materials
> - Certification basis
>
> This is a TEXTBOOK requirements traceability failure."

#### Slide 13: Analysis Part 3 - System Architecture Failures
**Visual:** Architecture diagram highlighting single points of failure
**Instructor Script:**
> "Now let's look at system architecture - Session 5 concepts.
>
> **Architecture Principle from Session 5:**
> 'Safety-critical systems require redundancy to eliminate single points of failure'
>
> **737 MAX MCAS Architecture - Single Points of Failure:**
>
> **1. AOA Sensor - SINGLE POINT OF FAILURE**
> - 737 MAX has TWO AOA sensors (left and right)
> - MCAS used input from ONLY ONE (alternated per flight)
> - No comparison logic between sensors
> - **Why this is catastrophic:** If active sensor fails, MCAS gets false data with no way to detect error
>
> **Compare to industry standard:**
> - Airbus A320: Uses 3 AOA sensors, voting logic
> - Boeing 777: Uses 2 AOA sensors, disagree logic
> - **737 MAX MCAS:** Used 1 sensor - UNPRECEDENTED for critical flight control
>
> **2. MCAS Software - SINGLE POINT OF FAILURE**
> - No independent verification of MCAS logic
> - No backup mode if MCAS malfunctions
> - Disabling electric trim also disabled pilot's electric trim (needed at high speed)
>
> **3. Pilot Awareness - SINGLE POINT OF FAILURE**
> - Only one way for pilots to know about MCAS: read about 'runaway stabilizer' in emergency procedures
> - No dedicated MCAS warning
> - No indication that MCAS was active
>
> **Architecture Principles Violated:**
>
> ❌ **Defense in Depth:** No multiple layers of protection
> ❌ **Redundancy:** Critical sensors not redundant
> ❌ **Fail-Safe Design:** Failures led to catastrophic outcomes, not safe states
> ❌ **Human-Centered Design:** Pilots excluded from system awareness
>
> **The Design Trade-Off Failure:**
> Boeing made a conscious trade-off:
> - **Benefit:** Avoid pilot retraining (save airlines money, faster certification)
> - **Cost:** Reduced pilot awareness and control authority
>
> **Question:** Was there a proper trade study? Was safety quantified? Were alternatives analyzed?
> **Answer:** No evidence of systematic trade study using methods from Session 5."

#### Slide 14: Analysis Part 4 - Verification & Validation Failures
**Visual:** V-model diagram showing where V&V failed
**Instructor Script:**
> "Let's analyze through the V-model lens from Session 2.
>
> **Recall the V-Model:**
> - Left side: Requirements → Design → Implementation
> - Right side: Unit testing → Integration testing → System testing → Validation
> - **Critical principle:** Each level on left must be VERIFIED by corresponding level on right
>
> **MCAS V&V Failures:**
>
> **1. Requirements Verification - FAILED**
> - **Question:** Did testing verify that pilots could safely handle MCAS failures?
> - **Answer:** No. Failure scenarios with faulty AOA sensor were not thoroughly tested with pilots
>
> **2. Integration Testing - FAILED**
> - **Question:** Was MCAS tested integrated with all conditions (high speed, low altitude, pilot actions)?
> - **Answer:** Limited. Testing focused on normal operations, not edge cases
>
> **3. System Testing - FAILED**
> - **Question:** Were failure modes tested in realistic operational scenarios?
> - **Answer:** No. The scenario of 'repeated MCAS activation with pilots fighting it' was not tested in simulator
>
> **4. Validation - CATASTROPHICALLY FAILED**
> - **Question:** Did the system meet stakeholder needs (pilots, passengers)?
> - **Answer:** No pilots were asked 'Can you safely handle this failure mode?'
>
> **Specific V&V Gaps:**
>
> | V&V Activity | What Should Have Happened | What Actually Happened | Consequence |
> |--------------|---------------------------|------------------------|-------------|
> | **Hazard Analysis** | Identify 'AOA sensor failure' as critical hazard | Categorized as less severe | Insufficient mitigations |
> | **Failure Modes Testing** | Test repeated MCAS activation with pilots | Not tested in realistic scenarios | Failure mode undiscovered |
> | **Pilot-in-Loop Testing** | Pilots test MCAS failures in simulator | Limited pilot testing of failures | Pilots couldn't respond |
> | **Certification Testing** | Independent FAA testing | FAA delegated to Boeing (self-certification) | Conflict of interest |
>
> **The Self-Certification Problem:**
> FAA had delegated certification authority to Boeing through ODA (Organization Designation Authorization) program.
>
> **Result:** Boeing employees, under schedule and cost pressure, certified their own design.
>
> **Systems Engineering Question:** What verification principle does this violate?
> **Answer:** Independence of verification - 'Test your own homework' doesn't work."

#### Slide 15: Analysis Part 5 - Systems Thinking Failures
**Visual:** Systems thinking diagram showing interconnected failures
**Instructor Script:**
> "Finally, let's examine this through systems thinking - the overarching framework from Sessions 1 and 2.
>
> **Systems Thinking Principle:**
> 'The system is more than the sum of its parts. Optimizing components individually can harm overall system performance.'
>
> **How This Manifests in 737 MAX:**
>
> **Component-Level Optimization (Locally Optimal):**
>
> ✓ **Engineering:** MCAS solved aerodynamic issue elegantly with software
> ✓ **Certification:** Avoided lengthy recertification as 'new aircraft'
> ✓ **Training:** No pilot retraining required
> ✓ **Manufacturing:** Minimal changes to production line
> ✓ **Sales:** Fast to market, beat Airbus competition
> ✓ **Cost:** Saved billions vs clean-sheet design
>
> **System-Level Result (Globally Catastrophic):**
>
> ❌ **Safety:** Introduced single-point-of-failure in critical flight control
> ❌ **Resilience:** Pilots couldn't diagnose or recover from failures
> ❌ **Robustness:** System fragile to sensor failures (common occurrence)
> ❌ **Transparency:** Pilots unaware of system fighting them
> ❌ **Outcome:** 346 deaths, 20-month grounding, $20B+ cost
>
> **Each department optimized their part:**
> - Engineering optimized for technical elegance
> - Certification optimized for speed
> - Training optimized for cost
> - Management optimized for profit
>
> **But no one optimized for SYSTEM SAFETY.**
>
> **The Organizational Systems Failure:**
>
> Organizational boundaries became technical boundaries:
>
> - **Flight controls team:** Designed MCAS, focused on handling characteristics
> - **Training team:** Developed pilot materials, wasn't told about MCAS scope
> - **Certification team:** Certified based on incomplete hazard analysis
> - **Safety team:** Relied on data from flight controls team
>
> **No one had complete system picture.**
>
> **This is why we study systems engineering:** To see the WHOLE system, not just our component."

#### Slide 16: The Root Cause - Synthesis
**Visual:** Root cause fishbone diagram
**Instructor Script:**
> "Let's synthesize our analysis. Using a fishbone diagram, we can map root causes:
>
> **EFFECT: 346 Deaths, Two 737 MAX Crashes**
>
> **ROOT CAUSES (Categories):**
>
> **1. TECHNICAL DESIGN:**
> - Single AOA sensor dependency
> - Excessive MCAS authority (2.5°)
> - Repeated activation design
> - No pilot notification
>
> **2. REQUIREMENTS ENGINEERING:**
> - Incomplete safety requirements
> - Missing redundancy requirements
> - No pilot awareness requirements
> - Failed traceability when design changed
>
> **3. VERIFICATION & VALIDATION:**
> - Inadequate failure mode testing
> - No pilot-in-loop testing of failures
> - Self-certification conflict of interest
> - Hazard analysis underestimated severity
>
> **4. SYSTEMS THINKING:**
> - Component optimization over system safety
> - Organizational silos
> - No one owned complete system safety
>
> **5. STAKEHOLDER MANAGEMENT:**
> - Commercial interests prioritized over safety
> - Pilots excluded from design decisions
> - Passengers never considered
>
> **6. ORGANIZATIONAL/CULTURAL:**
> - Schedule pressure (beat Airbus to market)
> - Cost pressure (avoid expensive retraining)
> - Culture shift from 'engineering first' to 'profit first'
> - Management override of engineering concerns
>
> **THE FUNDAMENTAL ROOT CAUSE:**
>
> Systems engineering processes existed at Boeing. They weren't followed or were deliberately circumvented when they conflicted with schedule and cost goals.
>
> **This is a failure of engineering integrity and organizational culture, enabled by inadequate regulatory oversight.**"

#### Slide 17: What Could Have Prevented This? - Counterfactual Analysis
**Visual:** Decision tree showing alternative paths
**Instructor Script:**
> "Let's do a thought experiment: What systems engineering practices could have prevented these crashes?
>
> **Preventive Measure #1: Proper Requirements Engineering**
>
> IF Boeing had written complete safety requirements:
> - **Requirement:** 'Flight critical systems shall use redundant sensors with disagree logic'
> - **Verification:** Design review would catch single-sensor MCAS
> - **Result:** MCAS redesigned with dual-sensor voting logic
> - **Outcome:** Sensor failures detected, MCAS doesn't activate on false data → **Crashes prevented** ✓
>
> **Preventive Measure #2: Independent Verification**
>
> IF FAA had not delegated certification to Boeing:
> - Independent FAA test pilots test MCAS failures in simulator
> - They discover pilots can't recover from repeated MCAS activation
> - Design changes required before certification
> - **Outcome:** Unsafe design caught before production → **Crashes prevented** ✓
>
> **Preventive Measure #3: Pilot Training**
>
> IF pilots had been trained on MCAS:
> - Pilots understand system behavior
> - Emergency procedures specifically address MCAS failures
> - Pilots recognize symptoms immediately
> - **Outcome:** Even with design flaws, pilots could have recovered → **Crashes likely prevented** ✓
>
> **Preventive Measure #4: Proper Trade Study**
>
> IF Boeing had conducted systematic trade study (Session 5):
> - Alternative A: Hide MCAS from pilots (chosen path)
> - Alternative B: Train pilots on MCAS (rejected due to cost)
> - Alternative C: Redesign aircraft physically (rejected due to cost/schedule)
>
> Trade study would quantify safety risk:
> - Alternative A: Risk = P(sensor failure) × P(pilot can't recover) = HIGH
> - Alternative B: Risk = P(sensor failure) × P(trained pilot can't recover) = LOW
> - **Outcome:** Alternative B selected → **Crashes prevented** ✓
>
> **Preventive Measure #5: Systems Thinking Culture**
>
> IF Boeing had maintained systems-level safety review:
> - Chief Systems Engineer reviews complete system
> - Asks: 'What happens if AOA sensor fails?'
> - Simulation shows catastrophic outcome
> - Design change mandated
> - **Outcome:** System-level hazard identified → **Crashes prevented** ✓
>
> **The Tragic Reality:**
> Any ONE of these standard systems engineering practices, properly applied, could have prevented 346 deaths.
>
> **All of them were skipped or compromised.**"

#### Slide 18: Lessons Learned - For Your Career
**Visual:** Lessons learned summary with actionable insights
**Instructor Script:**
> "What can you, as future automotive systems engineers, learn from this tragedy?
>
> **LESSON 1: Requirements Are Non-Negotiable**
> - Never skip requirements phase, even under schedule pressure
> - Safety requirements must be complete, verified, traced
> - When design changes, update requirements and re-verify
> - **Action:** Always ask 'What are the safety requirements?' before designing
>
> **LESSON 2: Redundancy Is Not Optional for Safety-Critical Systems**
> - Single points of failure are NEVER acceptable in safety-critical functions
> - If your design has SPOF, redesign or add mitigations
> - **Action:** In your designs, identify all SPOFs and eliminate them
>
> **LESSON 3: Testing Must Include Failure Modes**
> - Testing happy paths is not enough
> - Must test: What happens when things break?
> - Use FMEA, FTA systematically
> - **Action:** For every sensor, ask 'What if this fails?'
>
> **LESSON 4: Humans Are Part of the System**
> - Never design systems that fight the human operator
> - Pilots/drivers must understand what automation is doing
> - Situational awareness is a requirement, not a nice-to-have
> - **Action:** Include human factors in requirements from day 1
>
> **LESSON 5: Stakeholder Prioritization Matters**
> - Commercial pressures exist, but safety stakeholders must have priority
> - When business goals conflict with safety, safety wins
> - **Action:** If asked to compromise safety for cost/schedule, document your concerns
>
> **LESSON 6: Independence of Verification Is Critical**
> - You cannot objectively verify your own design
> - Independent review is not bureaucracy - it's essential
> - **Action:** Seek independent review, even informally
>
> **LESSON 7: Systems Thinking Prevents Emergent Failures**
> - Optimizing parts doesn't optimize the system
> - Someone must own complete system safety
> - **Action:** Always ask 'How does my component affect the total system?'
>
> **LESSON 8: Engineering Integrity Is Your Professional Responsibility**
> - You will face pressure to cut corners
> - Your job is to speak up when safety is compromised
> - 346 people died because engineers didn't say 'no'
> - **Action:** Be prepared to escalate safety concerns, even if unpopular
>
> **The Bottom Line:**
> Systems engineering processes exist to prevent tragedies like this. When we skip them, people die. When we follow them, we save lives.
>
> **That's why you're learning this.**"

#### Slide 19: Regulatory and Industry Changes - What Changed After
**Visual:** Timeline of changes post-grounding
**Instructor Script:**
> "This disaster did result in significant changes. Let's see what the industry and regulators learned:
>
> **FAA Reforms:**
>
> ✓ **Reduced delegation:** Critical systems no longer self-certified by manufacturers
> ✓ **Human factors review:** Mandatory pilot review of automation systems
> ✓ **Safety assessment changes:** More rigorous hazard analysis required
> ✓ **Whistleblower protection:** Engineers can report safety concerns without retaliation
>
> **Boeing Changes (Mandated):**
>
> ✓ **MCAS redesign:** Now uses dual AOA sensors with disagree logic
> ✓ **MCAS authority limited:** Cannot override pilot inputs
> ✓ **MCAS activation:** Single activation per event, not repeated
> ✓ **Pilot training:** Mandatory training on MCAS for all 737 MAX pilots
> ✓ **Alerts:** AOA disagree alert now standard, not optional
> ✓ **Transparency:** Complete documentation of flight control systems
>
> **Industry-Wide Changes:**
>
> ✓ **EASA (Europe):** Independent certification, doesn't automatically accept FAA certification
> ✓ **Other manufacturers:** Review of automation vs pilot authority principles
> ✓ **Systems engineering focus:** Renewed emphasis on SE processes in aerospace
>
> **What This Means for Automotive:**
>
> The same pressures exist in automotive:
> - Time to market pressure
> - Cost optimization pressure
> - Complexity of systems (ADAS, autonomous driving)
> - Software-driven functionality
>
> **ISO 26262 (Automotive Functional Safety) exists to prevent this in cars.**
>
> **Your responsibility:** Ensure automotive industry doesn't repeat aerospace mistakes as vehicles become more automated."

#### Slide 20: Transition to Group Work - Your Turn to Analyze
**Visual:** Group work instructions
**Instructor Script:**
> "You've now seen the complete analysis. Now it's your turn to apply these skills.
>
> You'll work in groups to analyze specific aspects in depth, then present findings. This simulates real engineering work - collaborative technical analysis.
>
> Let me explain the group activity."

---

### **CLIMAX: Group Analysis Activity** (Slides 21-24, ~30 minutes)

#### Slide 21: Group Work Instructions - Overview
**Visual:** Activity structure and expectations
**Instructor Script:**
> "Here's how the next 30 minutes will work:
>
> **Step 1: Form Groups (2 minutes)**
> - Groups of 4-5 students
> - Choose a group leader (presents findings)
>
> **Step 2: Select Topic (3 minutes)**
> - Each group chooses ONE analysis topic (next slide)
> - No two groups should choose same topic
>
> **Step 3: Analysis (20 minutes)**
> - Use frameworks from Sessions 1-5
> - Answer specific questions for your topic
> - Prepare 3-minute presentation
>
> **Step 4: Presentation (5 minutes)**
> - Each group presents findings (3 min)
> - Class discussion (2 min)
>
> **Deliverable:**
> - Key findings (3-5 points)
> - Systems engineering principles that were violated
> - Specific recommendations that could have prevented failure
>
> **You may use:**
> - Your notes from Sessions 1-5
> - Course textbooks
> - Discussion with your group
>
> Let's see the topics."

#### Slide 22: Group Work Topics - Choose One Per Group
**Visual:** Table of analysis topics
**Instructor Script:**
> "Here are the six analysis topics. Each group chooses one:
>
> **TOPIC 1: Stakeholder Analysis Deep Dive**
> - Create complete stakeholder map for 737 MAX development
> - Identify stakeholder conflicts (whose needs conflicted?)
> - Propose stakeholder engagement strategy that would have surfaced safety concerns
> - **Use:** Session 4 stakeholder analysis framework
>
> **TOPIC 2: Requirements Engineering Failure Analysis**
> - Write 5 safety requirements that should have existed for MCAS
> - Evaluate each requirement using quality attributes (complete, verifiable, traceable, etc.)
> - Create requirements traceability matrix showing requirements → design → verification
> - **Use:** Session 4 requirements engineering framework
>
> **TOPIC 3: System Architecture Redesign**
> - Identify all single points of failure in MCAS architecture
> - Propose redundant architecture design using aerospace standards
> - Create system architecture diagram showing your proposed design
> - **Use:** Session 5 architecture principles
>
> **TOPIC 4: Verification & Validation Plan**
> - Create V&V plan for MCAS using V-model
> - Identify specific test cases for failure modes (at least 5)
> - Propose independent verification approach
> - **Use:** Session 2 V-model, Session 8 preview (V&V methods)
>
> **TOPIC 5: Human Factors Analysis**
> - Analyze human-system interaction failures
> - Propose pilot training requirements
> - Design cockpit alerts/indications that would have helped pilots
> - **Use:** Systems thinking from Session 1-2, human-centered design principles
>
> **TOPIC 6: Trade Study - Alternative Solutions**
> - Conduct trade study comparing 3 alternatives for handling 737 MAX aerodynamics
>   - Alternative 1: MCAS as designed (what happened)
>   - Alternative 2: MCAS with full pilot training
>   - Alternative 3: Physical redesign (no MCAS)
> - Use trade study methodology: criteria, weighting, scoring
> - **Use:** Session 5 trade study methods
>
> **Choose your topic now and begin analysis!**"

#### Slide 23: Analysis Guidance - Key Questions for Each Topic
**Visual:** Detailed questions for each topic
**Instructor Script:**
> "Here are specific questions to guide each topic:
>
> **For All Topics:**
> - What systems engineering principles were violated?
> - What specific practices could have prevented the failures?
> - How would you verify your recommendations work?
>
> **TOPIC 1 (Stakeholder) - Specific Questions:**
> - Which stakeholders had their needs prioritized? Which were ignored?
> - What conflicts existed between stakeholder groups?
> - How would you resolve these conflicts using SE methods?
>
> **TOPIC 2 (Requirements) - Specific Questions:**
> - For each requirement you write, identify verification method
> - How would requirements traceability have caught authority increase (0.6° → 2.5°)?
> - What requirements attributes were violated in actual MCAS requirements?
>
> **TOPIC 3 (Architecture) - Specific Questions:**
> - How many single points of failure can you identify?
> - What redundancy approach would you use (voting, backup, fail-safe)?
> - How does your architecture handle sensor failures gracefully?
>
> **TOPIC 4 (V&V) - Specific Questions:**
> - What failure modes should have been tested?
> - What verification methods would you use (test, analysis, inspection, demo)?
> - How would you ensure independence of verification?
>
> **TOPIC 5 (Human Factors) - Specific Questions:**
> - What information did pilots need but didn't have?
> - How would you design pilot-automation interaction?
> - What training would enable pilots to handle failures?
>
> **TOPIC 6 (Trade Study) - Specific Questions:**
> - What criteria matter for this decision (safety, cost, schedule, etc.)?
> - How would you weight safety vs. commercial criteria?
> - What would a proper trade study have revealed?
>
> **You have 20 minutes. Use your SE tools!**"

#### Slide 24: Group Work - Time for Analysis
**Visual:** Timer and key reminders
**Instructor Script:**
> "You have 20 minutes starting now.
>
> **Reminders:**
> - Focus on applying SE frameworks, not just opinions
> - Be specific - give examples, not generalities
> - Think like a systems engineer, not just a component designer
> - Prepare to explain your reasoning
>
> **I'll circulate to answer questions.**
>
> [Instructor facilitates group work, provides guidance as needed]
>
> **At 15 minutes:** 'You have 5 minutes remaining. Start preparing your presentation.'
>
> **At 20 minutes:** 'Time's up. Let's hear your findings.'"

---

### **RESOLUTION: Synthesis and Integration** (Slides 25-28, ~20 minutes)

#### Slide 25: Group Presentations - Share Your Findings
**Visual:** Presentation order and format
**Instructor Script:**
> "Let's hear what you've discovered. Each group gets 3 minutes to present, then 2 minutes for class questions.
>
> **Presentation Format:**
> 1. State your topic and key question
> 2. Present 3-5 key findings
> 3. Explain SE principles involved
> 4. Give specific recommendations
>
> **Class:** Listen critically. Think about how each analysis connects to others.
>
> Let's begin with Topic 1: Stakeholder Analysis."

[Instructor facilitates presentations]

**After each presentation, instructor provides bridging commentary:**

> "Excellent analysis. Notice how [Group X's] findings about [topic] connect directly to [previous group's] findings about [other topic]. This is systems thinking - everything is interconnected."

**After all presentations:**

> "Let's look at what we've learned collectively."

#### Slide 26: Synthesis - Connecting the Analyses
**Visual:** Network diagram showing interconnected findings
**Instructor Script:**
> "Look at what you've discovered as groups. Let me show you how it all connects:
>
> **From Stakeholder Analysis (Topic 1):**
> You identified that commercial stakeholders were prioritized over safety stakeholders.
>
> **This led to Requirements Failures (Topic 2):**
> Because safety stakeholders (pilots, passengers) weren't involved, critical safety requirements weren't written.
>
> **Which resulted in Architecture Failures (Topic 3):**
> Without proper safety requirements, the architecture had single points of failure.
>
> **Which V&V couldn't catch (Topic 4):**
> Because requirements didn't exist, there was nothing to verify against. Self-certification had conflict of interest.
>
> **Creating Human Factors Disasters (Topic 5):**
> Pilots fighting an undocumented system they didn't understand.
>
> **Which a proper Trade Study would have revealed (Topic 6):**
> Systematic analysis would have shown the safety risks outweighed schedule/cost benefits.
>
> **This is SYSTEMS THINKING:**
>
> You cannot fix one part in isolation. Failures cascade through the system. Similarly, applying SE principles at any point could have broken the failure chain.
>
> **This is why we study systems engineering as an integrated discipline, not separate topics.**"

#### Slide 27: The Professional Imperative - Your Responsibility
**Visual:** Professional engineering code of ethics
**Instructor Script:**
> "Before we close, I want to talk about professional responsibility.
>
> **Boeing had systems engineers. They had SE processes. They had safety engineers.**
>
> So why did 346 people die?
>
> Because when those engineers raised concerns, they were overruled by schedule and cost pressures. Some engineers did speak up. They were ignored.
>
> **From Congressional testimony and investigations:**
>
> - Boeing engineers raised concerns about MCAS design → management proceeded anyway
> - Test pilots noted MCAS was 'egregious' → concerns not addressed
> - FAA engineers questioned certification approach → were sidelined
>
> **The lesson:** Having SE knowledge is not enough. You must have the courage to use it.
>
> **Your Professional Responsibility (From Engineering Codes of Ethics):**
>
> 1. **Hold paramount the safety and welfare of the public**
> 2. **Perform services only in areas of competence**
> 3. **Issue public statements only in objective and truthful manner**
> 4. **Act for each employer as faithful agents or trustees**
> 5. **Avoid deceptive acts**
> 6. **Conduct themselves honorably and ethically**
>
> **When safety conflicts with business goals, safety must win.**
>
> **In the automotive industry, you'll face similar pressures:**
> - Launch deadlines for new models
> - Cost targets that squeeze safety margins
> - Pressure to 'just ship it'
>
> **Your job is to be the voice for the people who will depend on your system working safely.**
>
> 346 people are dead because engineers didn't have the final say on safety.
>
> **Don't let that be you.**"

#### Slide 28: Moving Forward - Applying This to Automotive SE
**Visual:** Automotive analogies to 737 MAX failures
**Instructor Script:**
> "Let's bring this home to automotive systems engineering.
>
> **Automotive Systems with Similar Risks:**
>
> **Autonomous Emergency Braking (AEB):**
> - Like MCAS, can override driver
> - What if sensor fails and brakes activate unnecessarily?
> - Do drivers understand when/how system intervenes?
>
> **Adaptive Cruise Control (ACC):**
> - Can accelerate/decelerate automatically
> - What if radar sensor fails?
> - Are there redundant sensors with voting logic?
>
> **Lane Keeping Assist (LKA):**
> - Can steer vehicle
> - What if camera misreads lane markings?
> - Can driver override? Is override authority always available?
>
> **Battery Management System (BMS) in EVs:**
> - Controls high-voltage systems
> - What if temperature sensor fails?
> - Single point of failure could cause thermal runaway
>
> **Autonomous Driving Systems:**
> - Highest complexity, highest stakes
> - Multiple sensors, multiple failure modes
> - Human handover challenges (like MCAS, pilots fighting automation)
>
> **For Each of These, Ask the MCAS Questions:**
>
> 1. ✓ Are safety requirements complete?
> 2. ✓ Are critical sensors redundant?
> 3. ✓ Are failure modes thoroughly tested?
> 4. ✓ Do human operators understand system behavior?
> 5. ✓ Can humans override when necessary?
> 6. ✓ Is verification independent?
> 7. ✓ Are all stakeholders considered?
>
> **If you can't answer 'yes' to all seven questions, you have SE work to do.**
>
> **ISO 26262 exists to prevent automotive MCAS disasters. Learn it. Use it. Insist on it.**"

---

### **CONCLUSION: Takeaways and Next Steps** (Slides 29-30, ~5 minutes)

#### Slide 29: Key Takeaways - What You've Learned Today
**Visual:** Summary infographic
**Instructor Script:**
> "Let's summarize what you've accomplished today:
>
> **✓ Knowledge:** You can now analyze complex system failures using SE frameworks
>
> **✓ Skills:** You've practiced:
> - Stakeholder analysis
> - Requirements failure analysis
> - Architecture evaluation
> - V&V gap analysis
> - Root cause analysis
> - Systems thinking
>
> **✓ Application:** You can apply these same methods to automotive systems
>
> **✓ Professional Development:** You understand engineering responsibility and ethics
>
> **Most Importantly:**
>
> You've seen what happens when systems engineering principles are ignored. 346 people died because:
> - Requirements were incomplete
> - Stakeholders were ignored
> - Single points of failure existed
> - Verification was inadequate
> - Systems thinking was absent
> - Business pressure overruled safety
>
> **Every one of these failures violated principles you learned in Sessions 1-5.**
>
> **Going Forward:**
>
> When you're designing automotive systems:
> - Remember MCAS
> - Apply SE principles rigorously
> - Speak up when you see safety compromised
> - Be the systems engineer who prevents the next disaster
>
> **That's why you're here. That's why this matters.**"

#### Slide 30: Next Session Preview & Assignment
**Visual:** Session 7 preview + assignment details
**Instructor Script:**
> "**Next Session (Session 7): Operational and Functional Analysis**
>
> We'll learn systematic methods for:
> - Operational scenarios and use cases
> - Functional decomposition
> - Functional flow block diagrams (FFBD)
> - Requirements allocation to functions
>
> This is how you prevent the requirements and architecture failures we saw today.
>
> **Assignment for Next Class:**
>
> **Individual Written Analysis (Due before Session 7):**
>
> Choose ONE of the following automotive systems:
> 1. Adaptive Cruise Control (ACC)
> 2. Automatic Emergency Braking (AEB)
> 3. Battery Management System (BMS) for EV
> 4. Electronic Stability Control (ESC)
>
> **Your task:**
> Conduct a MCAS-style failure analysis:
>
> **Part 1:** Identify potential failure modes (what could go wrong?)
> **Part 2:** Analyze using SE frameworks:
> - Stakeholder impact
> - Requirements that should exist
> - Architecture considerations (redundancy, fail-safe)
> - V&V approaches to catch failures
>
> **Part 3:** Propose design safeguards to prevent failures
>
> **Format:** 3-4 pages, use SE frameworks from Sessions 1-5
>
> **Purpose:** Apply today's lessons to automotive systems
>
> **Grading criteria:**
> - Systematic application of SE frameworks (40%)
> - Depth of failure analysis (30%)
> - Practical recommendations (20%)
> - Professional presentation (10%)
>
> **This is your chance to demonstrate you can think like a systems safety engineer.**
>
> **Questions about the assignment or today's session?**
>
> **We have time for final Q&A.**"

---

## 📊 PPT DESIGN GUIDANCE

### Visual Style:
- **Professional and Respectful:** This is about a real tragedy - avoid sensationalism
- **Color Scheme:**
  - Blues and grays (professional, trustworthy)
  - Red for failures/warnings
  - Green for corrections/lessons learned
- **Imagery:** Use aircraft images respectfully, technical diagrams, avoid graphic crash imagery

### Key Slides to Emphasize:
1. **Slide 3** (Timeline of facts) - Set factual foundation
2. **Slide 8** (Design changes table) - The critical evidence
3. **Slide 12** (Requirements failures) - Core SE lesson
4. **Slide 16** (Root cause synthesis) - The "aha" moment
5. **Slide 18** (Lessons learned) - What matters for their careers
6. **Slide 27** (Professional responsibility) - Ethical foundation

### Animations:
- Use builds to reveal information progressively
- Highlight connections between concepts
- In comparison tables, highlight differences
- For failure sequences, use timeline animations

### Technical Diagrams Needed:
- MCAS system architecture (inputs/processing/outputs)
- 737 MAX vs 737 NG physical differences
- V-model showing V&V failures
- Stakeholder map
- Root cause fishbone diagram
- Requirements traceability matrix example

### Group Work Materials:
- Provide handout with topic details, questions, frameworks
- Include reference to Sessions 1-5 materials
- Provide template for presentations

---

## 🎯 INSTRUCTOR NOTES

### Pedagogical Strategy:
This session uses **Case-Study Interactive Learning** to:
1. **Apply knowledge:** Students use all tools from Sessions 1-5
2. **Develop critical thinking:** Analyze complex real-world failure
3. **Practice collaboration:** Group work simulates real engineering
4. **Build professional identity:** Understand ethical responsibilities

### Emotional Considerations:
- **This is a real tragedy:** Maintain respectful tone throughout
- **Students may be emotionally affected:** Acknowledge the human cost
- **Focus on learning, not blame:** Emphasize systems failures, not individuals
- **Empower students:** They can prevent future tragedies

### Common Student Questions (Be Prepared):
- **"Was this criminal?"** → Yes, Boeing faced criminal charges, paid $2.5B settlement
- **"Why didn't engineers stop it?"** → Some tried, were overruled - discuss engineering culture
- **"Is 737 MAX safe now?"** → After redesign and training, yes (explain changes)
- **"Could this happen in automotive?"** → Yes, if SE principles ignored - that's why we study this
- **"What happened to the people responsible?"** → CEO resigned, some engineers testified in Congress

### Timing Management:
- **Core content (Slides 1-20):** ~57 minutes - MUST COVER
- **Group work:** 30 minutes - DO NOT SKIP (essential learning)
- **Presentations:** Strictly enforce 3 min per group
- **If running short:** Reduce instructor analysis depth, keep group work
- **If running long:** Reduce some technical details in Slides 10-15

### Facilitation Tips for Group Work:
- **Circulate actively:** Visit each group, ask probing questions
- **Guide, don't solve:** Help them apply frameworks, don't give answers
- **Watch for struggles:** If group is stuck, provide example to get them started
- **Encourage depth:** Push beyond surface-level analysis
- **Connect to course materials:** Remind them of specific Sessions/frameworks

### Assessment During Session:
- **Observe group discussions:** Are they using SE terminology correctly?
- **Listen to presentations:** Do they demonstrate understanding?
- **Note quality of questions:** Insightful questions indicate engagement
- **This informs future sessions:** Adjust if concepts aren't landing

### Managing Sensitive Discussion:
- **If students become upset:** Acknowledge emotions are valid, refocus on learning
- **If debate gets heated:** Redirect to evidence-based SE analysis
- **If blame-focused:** Emphasize systems thinking, not individual fault
- **Keep it professional:** Technical analysis with empathy

---

## ✅ Session Success Criteria

Students leave able to:
- ✓ Conduct systematic failure analysis using SE frameworks
- ✓ Identify stakeholder, requirements, architecture, V&V failures in complex systems
- ✓ Apply root cause analysis to real-world engineering failures
- ✓ Connect technical decisions to safety outcomes
- ✓ Recognize similar risks in automotive systems
- ✓ Understand professional and ethical responsibilities
- ✓ Work collaboratively on complex technical analysis

**Most Importantly:**
Students internalize that **systems engineering is not academic theory - it's life-and-death practice.** When we skip SE processes, people die. When we apply them rigorously, we save lives.

**Behavioral Outcome:**
In future work, when facing pressure to cut corners, students remember 346 people who died and choose to do engineering right.

---

## 📚 Additional Resources for Instructor

### Recommended Background Reading:
- **"Flying Blind"** by Peter Robison (detailed Boeing culture investigation)
- **House Committee Report:** "The Boeing 737 MAX: Examining the Federal Aviation Administration's Oversight of the Aircraft's Certification" (Sept 2020)
- **JATR Report:** Joint Authorities Technical Review of Boeing 737 MAX (Oct 2019)
- **Indonesian KNKT Report:** Aircraft Accident Investigation Report, Lion Air Flight 610
- **Ethiopian AAIC Report:** Aircraft Accident Investigation Bureau Interim Report, Ethiopian Airlines Flight 302

### Technical References:
- **ISO/IEC 15288:** Systems and software engineering - System life cycle processes
- **SAE ARP4754A:** Guidelines for Development of Civil Aircraft and Systems
- **ISO 26262:** Road vehicles - Functional safety (automotive parallel)
- **FAA AC 25.1309-1A:** System Design and Analysis

### Video Resources (if time permits):
- Congressional testimony excerpts (powerful for showing real-world impact)
- Simulator recreation of accidents (if used, brief and respectful)
- 60 Minutes investigation (search "Boeing 737 MAX 60 Minutes")

---

## 🔄 Connection to Future Sessions

**This case study will be referenced in:**

- **Session 7 (Operational/Functional Analysis):** "How functional decomposition could have revealed MCAS risks"
- **Session 8 (Integration, V&V):** "V&V methods that should have been applied to MCAS"
- **Session 9 (Risk Management):** "FMEA/FTA analysis of MCAS failure modes"
- **Session 12 (Safety & Security):** "ISO 26262 ASIL ratings and how they apply"
- **Session 14 (Case Study 2):** "Compare/contrast automotive case study to aerospace"

**Encourage students to reference MCAS throughout course:** "What would the MCAS engineers have done differently if they'd used [this session's topic]?"

---

**End of Framework**

**Instructor Final Note:** This is the most emotionally challenging session in the course. It's also potentially the most impactful. Students will remember this session for the rest of their careers. Deliver it with the gravity and professionalism it deserves. You're teaching them to save lives.

---

**Next:** Generate framework for Session 7 (Operational and Functional Analysis)
