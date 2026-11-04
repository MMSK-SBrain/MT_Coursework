# Situated Learning Problems
## AE ZG516: Advances in IC Engines

**Purpose:** Connect classroom learning to workplace applications through authentic, complex problems
**Format:** One workplace-connected project per module (6 total)
**Audience:** M.Tech working professionals with industry experience
**Assessment:** Technical depth + practical feasibility + workplace relevance

---

## OVERVIEW

###What is Situated Learning?
Situated learning theory posits that learning is most effective when embedded in authentic activity, context, and culture. For working professionals, this means connecting course concepts directly to workplace challenges they face or will face.

### Key Principles
1. **Authentic Context:** Real problems from students' workplaces or realistic industry scenarios
2. **Complex Challenges:** Require integration of multiple concepts from the module
3. **Practical Constraints:** Must consider cost, time, regulations, organizational factors
4. **Peer Learning:** Students present and critique each other's solutions
5. **Reflection:** Explicit connection between theory learned and practice applied

### Structure of Each Problem
- **Context Setting:** Define the workplace scenario and stakeholders
- **Problem Statement:** Clear description of the challenge or opportunity
- **Requirements:** What students must deliver (analysis, design, calculations, justification)
- **Deliverables:** Format (report, presentation, calculations)
- **Assessment Rubric:** Clear evaluation criteria
- **Timeline:** When assigned, due date, presentation schedule

---

## MODULE 1: ENGINE FOUNDATIONS
### Problem 1: Design and Justify Your Workplace Engine

**Timeline:**
- Assigned: End of Session 1
- Work Period: 1 week (Sessions 1-2 + weekend)
- Due: Before Session 3
- Presentations: Session 3 (5 min each, 2-3 students selected)

**Context:**
You are an engine design engineer tasked with specifying an engine for a specific application relevant to your organization (or your target industry). This could be:
- Commercial vehicle (delivery truck, bus, taxi, rideshare)
- Power generation (backup generator, prime power, remote location)
- Construction/agricultural equipment (excavator, tractor, harvester)
- Industrial application (pump drive, compressor, marine)
- Passenger vehicle (family sedan, performance car, SUV)

**Problem Statement:**
Your management has given you a specification document outlining the performance requirements, operating conditions, and constraints. You must select and justify all major engine design parameters to meet these requirements while optimizing for cost, reliability, fuel economy, and emissions compliance.

**Requirements:**

**Part 1: Application Analysis (20% weight)**
Define your chosen application context:
- What is the vehicle/equipment?
- What is the typical operating profile? (Duty cycle: speed range, load pattern, ambient conditions)
- What are the key performance requirements? (Power, torque, speed range, fuel economy targets)
- What are the constraints? (Packaging space, weight limits, cost target, emissions regulations, fuel availability)
- Who are the end users and what matters most to them?

**Part 2: Design Decisions (40% weight)**
Make and justify design choices for:

**Architecture:**
- SI or CI engine? Why?
- Number of cylinders? Configuration (inline, V, other)?
- Justification considering balance, packaging, cost, NVH

**Displacement & Geometry:**
- Bore and stroke dimensions (specify both)
- Calculate total displacement (liters)
- Bore/stroke ratio (oversquare, square, undersquare) - why this choice?
- Justify based on application (high RPM vs low-speed torque)

**Compression Ratio:**
- Specify compression ratio
- Justify based on: Fuel type/quality, knock/auto-ignition considerations, efficiency targets, emissions
- What is the trade-off you're managing?

**Performance Targets:**
- Target peak power (kW @ RPM)
- Target peak torque (N·m @ RPM)
- Desired torque curve shape (flat, peaky, etc.) - why?
- Calculate target BMEP (compare to typical values from Session 1)

**Breathing & Air Systems:**
- Naturally aspirated or turbocharged? Why?
- If turbo: Quick spool vs high peak flow priority?
- 2-valve or 4-valve per cylinder?
- VVT needed? What benefits justify the cost?

**Part 3: Calculations (20% weight)**
Perform and show:
- Displacement calculation (V_d = π/4 × bore² × stroke × cylinders)
- BMEP calculation at peak torque
  - BMEP = (Torque × 4π) / Displacement
  - Compare your BMEP to typical values (Session 1 notes)
- Power and torque relationship check
  - Power (kW) = Torque (N·m) × RPM / 9549
- At least one performance calculation specific to your application:
  - Gradeability calculation for truck
  - Time-to-full-power for generator
  - Acceleration estimate for vehicle
  - Pump flow rate for industrial drive

**Part 4: Trade-off Analysis & Justification (20% weight)**
Explicitly address trade-offs:
- "I chose X over Y because..." (with quantitative or qualitative reasoning)
- Examples:
  - "I selected CR = 12:1 instead of 14:1 because local fuel octane is only 91 RON, and knock would limit performance"
  - "I chose inline-4 over V6 despite slightly rougher operation because cost target is tight and application is commercial fleet"
  - "I selected turbocharging even though it adds cost because 30% power boost allows engine downsizing, saving 15% fuel over NA equivalent"
- Compare to real engines in similar applications (if you can find data)

**Deliverables:**
1. **Technical Report (3-4 pages):**
   - Application context and requirements
   - Design specifications (table format acceptable)
   - Calculations (show work)
   - Trade-off justifications
   - Comparison to actual engines (if available)

2. **Summary Slide (1 slide, if selected to present):**
   - Application + key requirements
   - Your engine specs (displacement, power, torque, CI/SI, turbo/NA, etc.)
   - One key trade-off you managed
   - How does it compare to reality?

3. **Peer Presentation (5 minutes, for selected students):**
   - "Here's my application, here's my engine, here's why I designed it this way"
   - Class provides feedback and questions

**Assessment Rubric:**

| Criterion | Excellent (90-100%) | Good (75-89%) | Adequate (60-74%) | Needs Improvement (<60%) |
|-----------|-------------------|---------------|-------------------|------------------------|
| **Application Analysis** | Comprehensive analysis of requirements, operating profile, and constraints. Clear understanding of user needs. | Good analysis with most key factors identified. Minor gaps in requirements. | Basic analysis present but missing some important constraints or operating conditions. | Incomplete or superficial analysis. Requirements unclear. |
| **Design Choices** | All major design parameters specified with strong technical justification. Clear reasoning. | Most parameters justified well. Some choices lack depth of reasoning. | Basic specifications provided. Justifications are generic or weak. | Major parameters missing or poorly justified. |
| **Calculations** | All calculations correct, clearly shown, properly interpreted. BMEP realistic. | Calculations mostly correct. Minor errors in execution or interpretation. | Calculations attempted but with significant errors or missing steps. | Calculations absent, incorrect, or not related to design. |
| **Trade-off Analysis** | Explicit identification of trade-offs with quantitative or well-reasoned qualitative analysis. Multiple trade-offs addressed. | Trade-offs identified with reasonable justifications. Could be more explicit. | Trade-offs mentioned but analysis is superficial. | No meaningful trade-off analysis. |
| **Workplace Relevance** | Clearly connected to actual workplace or realistic industry scenario. Practical constraints considered. | Good connection to practice. Some practical constraints considered. | Weak connection to real applications. Mostly theoretical. | No clear workplace relevance. |

**Learning Outcomes Addressed:**
- SO-1-1-1: Analyze engine architecture choices and their impact
- SO-1-1-2: Differentiate torque and power, calculate BMEP and efficiency
- SO-1-1-3: Apply thermodynamic cycle principles
- SO-1-2-2: Calculate and evaluate volumetric efficiency factors

**Instructor Notes:**
- Encourage students to use their actual workplace engines if relevant
- For students without direct engine exposure, provide application scenarios
- Selected presentations should cover diverse applications (truck, generator, car, etc.)
- During presentations, facilitate peer questions and discussion
- Highlight common errors: Unrealistic BMEP, inappropriate CR for fuel, mismatch between application and design

---

## MODULE 2: PERFORMANCE & CALIBRATION
### Problem 2: Optimize Performance in Your Fleet

**Timeline:**
- Assigned: End of Session 3
- Work Period: 1 week
- Due: Before Session 5
- Presentations: Session 5 (5 min each, 2-3 students selected)

**Context:**
Your organization operates a fleet of vehicles/equipment with internal combustion engines. You've identified a performance, fuel economy, or drivability issue affecting operational costs, customer satisfaction, or regulatory compliance. As the technical lead, you must diagnose the root cause and propose evidence-based solutions.

**Problem Statement:**
Identify a real or realistic performance optimization opportunity in your workplace (or target industry) and develop a data-driven solution using performance analysis and calibration principles from Module 2.

**Requirements:**

**Part 1: Problem Identification (20% weight)**
Select and describe an engine performance issue:
- **Describe the engine:** Make, model, displacement, SI/CI, turbo/NA, application
- **Define the problem:**
  - Poor fuel economy at specific operating condition?
  - Insufficient power in certain RPM range?
  - Drivability issues (hesitation, surge, poor throttle response, black smoke)?
  - Excessive emissions leading to compliance failures or DPF regeneration issues?
  - Noise, vibration, or harshness concerns?
- **Quantify the impact:** Fuel cost, downtime, customer complaints, regulatory risk
- **Specify operating conditions where problem occurs:** RPM range, load, temperature, altitude

**Part 2: Data Gathering (15% weight)**
Collect available data (real or realistic):
- Performance curves (torque, power vs RPM) - if available or estimated
- Fuel consumption data (L/100km, mpg, g/kWh, or similar)
- BSFC map or operating efficiency data - if available
- OBD-II diagnostic data (if applicable): DTCs, fuel trims, sensor readings
- Operating profiles: Where does engine spend most time? (Speed/load histogram if available)
- Any calibration or maintenance history

**Part 3: Root Cause Analysis (30% weight)**
Analyze the problem using Module 2 concepts:

**Performance Parameter Analysis:**
- What performance parameters are affected? (BMEP, thermal efficiency, VE, BSFC)
- Calculate or estimate current values and compare to typical/expected values
- Where on the torque/power curve does the problem occur?

**Diagnosis:**
- Is this a **hardware limitation** or **calibration issue**?
  - Hardware: Worn components, undersized turbo, restrictive exhaust, mechanical issues
  - Calibration: Sub-optimal maps, conservative tuning, aging sensor compensation
- **Use performance maps conceptually:**
  - If low-RPM torque issue: Is it turbo lag? Valve timing? Insufficient airflow?
  - If high fuel consumption: Where on BSFC map is operation? Could operating strategy shift to better efficiency region?
  - If drivability issue: Is it transient compensation? Boost control? Spark/injection timing?

**Evidence-based Reasoning:**
- What data or observations support your diagnosis?
- What did you rule out and why?

**Part 4: Proposed Solution (30% weight)**
Develop actionable recommendations:

**Calibration Modifications (if calibration issue):**
- **SI engines:** Spark timing adjustments? Fuel map changes? VVT strategy? Boost control?
- **CI engines:** Injection timing? Rail pressure? EGR rate? Pilot injection quantity/timing? Smoke limiter adjustment?
- **For each change:** What parameter to modify, in what direction, under what conditions
- **Predict outcomes:** How will this improve the problem? What performance metrics will change?
- **What are the trade-offs?** (Example: Advancing diesel injection reduces PM but increases NOx)

**Operational Strategy Changes:**
- Shift point optimization (for vehicles)
- Operating speed/load guidance (for stationary engines)
- Driver training or operational procedures
- Route or duty cycle optimization

**Hardware Modifications (if hardware limit):**
- Component replacement or upgrade (turbo, intercooler, exhaust, etc.)
- Cost-benefit: Is hardware change justified?

**Part 5: Validation & Implementation Plan (5% weight)**
- **How would you validate the solution?**
  - Dyno testing? Field testing? Data logging?
  - What metrics to measure before/after?
- **Success criteria:** What quantifiable improvement would confirm success?
- **Rollout strategy:** Pilot test on one unit? Phased fleet rollout?
- **Cost-benefit estimate:** Investment vs expected savings/improvement

**Deliverables:**
1. **Technical Report (4-5 pages):**
   - Problem description and impact quantification
   - Data gathered (tables, graphs)
   - Root cause analysis with reasoning
   - Proposed solution with trade-off analysis
   - Validation and implementation plan
   - Expected outcomes (quantified if possible)

2. **Summary Slide (1 slide, if presenting):**
   - Problem + impact
   - Root cause
   - Your solution
   - Expected improvement

**Assessment Rubric:**

| Criterion | Excellent (90-100%) | Good (75-89%) | Adequate (60-74%) | Needs Improvement (<60%) |
|-----------|-------------------|---------------|-------------------|------------------------|
| **Problem Identification** | Clear, specific, quantified problem with significant operational impact. Well-defined conditions. | Problem clearly stated. Some quantification. Conditions mostly defined. | Problem identified but vague or poorly quantified. | Problem unclear or trivial. |
| **Data Gathering** | Comprehensive data collection. Multiple sources. Organized presentation. | Good data gathered. Minor gaps. | Limited data. Some key information missing. | Insufficient data to support analysis. |
| **Root Cause Analysis** | Sophisticated analysis using course concepts. Evidence-based reasoning. Ruled out alternatives. | Good analysis with reasonable conclusions. Uses course concepts adequately. | Basic analysis. Some use of course concepts. Reasoning could be stronger. | Poor or absent analysis. No connection to course material. |
| **Solution Quality** | Actionable, specific solution. Trade-offs explicitly analyzed. Realistic and feasible. | Good solution with reasonable justification. Some trade-offs considered. | Generic solution lacking specifics. Weak trade-off analysis. | Solution impractical or poorly justified. |
| **Validation Plan** | Clear validation methodology. Quantified success criteria. Realistic implementation. | Reasonable validation approach. Success criteria defined. | Basic validation plan. Criteria vague. | No validation plan or unrealistic. |

**Learning Outcomes Addressed:**
- SO-2-3-1: Calculate thermal efficiency, BSFC, BMEP
- SO-2-3-2: Interpret torque and power curves
- SO-2-3-3: Analyze effects of timing, CR on performance
- SO-2-3-4: Use BSFC maps to identify efficient operating regions
- SO-2-4-1, SO-2-4-2: Apply calibration strategies
- SO-2-4-3: Evaluate calibration trade-offs
- SO-2-4-4: Diagnose drivability issues

---

## MODULE 3: AIR & FUEL SYSTEMS
### Problem 3: Breathing and Fueling System Optimization

**Timeline:**
- Assigned: End of Session 7
- Work Period: 1 week
- Due: Before Session 8
- Presentations: Session 8 (5 min each, 2-3 students selected)

**Context:**
Air and fuel delivery systems directly determine an engine's power output, efficiency, and emissions. Whether upgrading an existing engine, matching components for a new application, or troubleshooting airflow/fueling issues, understanding these systems is critical.

**Problem Statement:**
Select ONE of the following workplace-connected scenarios and develop a comprehensive technical solution:

**OPTION A: Turbocharger Matching & Boost System Design**
You need to select and specify a turbocharging system for an engine application (new design or repower/upgrade project).

**OPTION B: Fuel System Diagnosis & Optimization**
Diagnose and solve a fuel delivery or mixture quality issue affecting performance, emissions, or drivability.

**OPTION C: Intake/Exhaust Flow Optimization**
Improve volumetric efficiency through intake, exhaust, or breathing system modifications.

---

### OPTION A: Turbocharger Matching

**Scenario:**
Your organization is:
- Upgrading an NA engine to turbocharged for more power in same package, OR
- Replacing an aging turbocharger on existing turbocharged engine, OR
- Designing boost system for new application

**Requirements:**

**1. Define Application & Targets (15% weight)**
- Engine: displacement, configuration, SI/CI, current power output
- Target: Desired power output, torque curve shape, RPM range
- Operating profile: Transient response needs? Altitude? Duty cycle?
- Constraints: Cost, packaging space, existing manifold design

**2. Airflow Calculations (25% weight)**
Calculate required airflow at peak power:
- **Air mass flow rate** needed for target power:
  - For SI: ṁ_air = (Power × BSFC) / (LHV_fuel × η_comb) × (AFR)
  - Or use: ṁ_air = (Displacement × RPM × ρ_air × VE) / (2 × 60) for 4-stroke
- **VE assumptions:** Estimate realistic VE for boosted engine (100-130% typical)
- **Pressure ratio** required:
  - PR = (ṁ_air × R × T_amb) / (P_amb × Displacement × RPM / 120)
  - Or specify target boost pressure: PR = P_boost_absolute / P_atmospheric
- **Compressor outlet temperature** (estimate using isentropic efficiency ~75%):
  - T_out = T_in × [1 + (PR^((γ-1)/γ) - 1) / η_compressor]
- **Intercooler effectiveness** needed: Target charge temperature?

**3. Turbocharger Selection (25% weight)**
- **Compressor sizing:**
  - Match airflow and PR to compressor map
  - Ensure operating points avoid surge and choke lines
  - Select compressor with efficiency island covering operating range
- **Turbine sizing:**
  - Match turbine A/R and size to exhaust flow and desired spool characteristics
  - Trade-off: Small A/R (quick spool, higher backpressure) vs Large A/R (better flow, slower spool)
  - Consider VGT if applicable (diesel, high-end applications)
- **Specify:** Turbo model (if using real catalogs) or key specs (compressor diameter, turbine A/R, max airflow, max PR)

**4. Boost Control Strategy (15% weight)**
- Wastegate: Internal or external? Pneumatic or electronic control?
- Control logic: Target boost map (RPM vs boost), how to achieve it
- Safety: Overboost protection, compressor surge avoidance
- Altitude compensation if needed

**5. Supporting Components (10% weight)**
- **Intercooler:** Air-to-air or air-to-water? Sizing estimate? Acceptable pressure drop?
- **Oil supply:** Turbo lubrication and cooling requirements
- **Intake piping:** Minimize restrictions
- **Exhaust manifold:** Equal-length runners? Twin-scroll considerations?

**6. Performance Prediction & Trade-offs (10% weight)**
- Predicted power gain
- Spool characteristics: At what RPM will full boost be available?
- Fuel economy impact (positive due to downsizing or negative due to enrichment?)
- Durability considerations: Higher cylinder pressure, thermal stress
- Cost estimate

**Deliverable:** 5-6 page technical report + calculations + component specifications

---

### OPTION B: Fuel System Diagnosis

**Scenario:**
Engines in your fleet exhibit:
- Inconsistent fuel delivery causing performance variation
- Black smoke (rich) or misfire/hesitation (lean)
- Poor fuel economy
- Failed emissions test
- Long-term fuel trim errors (SI engines)
- Injection system faults (CI engines)

**Requirements:**

**1. Problem Description (15% weight)**
- Symptoms observed
- When does problem occur? (Cold/hot, low/high load, specific RPM?)
- Diagnostic data available: DTCs, fuel trims, O2 sensor readings, injection pressure, smoke levels

**2. Fuel System Analysis (25% weight)**
Analyze the fuel delivery system:
- **SI Engines:**
  - PFI or GDI? Fuel pressure (measure or specify)?
  - MAF or MAP sensor: Readings normal? Rationality?
  - Injector flow rate: Clogged? Leaking?
  - Fuel pressure regulator: Holding pressure?
  - O2 sensor: Reading rich/lean? Response time?
- **CI Engines:**
  - Common rail system: Rail pressure achieving target? Fluctuations?
  - Injector health: Leakage? Flow imbalance between cylinders?
  - Low-pressure supply: Fuel filter restriction? Air in fuel?
  - Injection timing and quantity: Commanded vs actual (if data available)?

**3. Root Cause Determination (25% weight)**
Using data and system knowledge:
- **Is it air measurement error** (MAF/MAP sensor fault causing wrong fuel calculation)?
- **Fuel delivery issue** (pump, pressure, injector flow)?
- **Control system fault** (ECU miscalculation, sensor input error)?
- **Mechanical issue** (compression loss causing apparent rich/lean)?
- Support your conclusion with evidence

**4. Solution & Validation (25% weight)**
- **If hardware:** What component to replace/clean/repair?
- **If calibration:** What adaptation/relearn procedure needed?
- **If operating condition:** What operating guidance to provide?
- **Validation:** How to test fix? Before/after measurements?
- **Predicted improvement:** Quantify expected change in fuel economy, emissions, driveability

**5. Prevention (10% weight)**
- What maintenance or monitoring would prevent recurrence?
- Fuel quality considerations?
- Injector cleaning schedules?

**Deliverable:** 4-5 page diagnostic report with fault tree analysis, test data, solution

---

### OPTION C: VE Optimization

**Scenario:**
Improve engine breathing to increase power output without forced induction, or maximize VE for boosted application.

**Requirements:**

**1. Baseline Assessment (20% weight)**
- Current engine: Displacement, valve configuration, cam timing, intake/exhaust design
- Current VE (estimated or measured): At various RPM points
- Power output: Current and target
- Where is VE limiting performance?

**2. Flow Analysis (25% weight)**
Evaluate breathing restrictions:
- **Valve flow:** Number of valves, lift, duration - adequate for target power?
- **Port design:** Intake and exhaust port flow coefficients (if available) or visual assessment
- **Manifold:** Runner length/diameter optimized for target RPM? Plenum size?
- **Exhaust backpressure:** Catalyst restriction? Muffler? Piping diameter?
- **Valve timing:** Fixed or VVT? Overlap duration? Optimal for application?

**3. Improvement Strategies (30% weight)**
Propose specific modifications (select 2-3 most impactful):
- **Head work:** Port matching, polishing, valve size increase?
- **Camshaft change:** Longer duration, more lift, more overlap for high RPM?
- **VVT addition or optimization:** Reduce overlap at low RPM, increase at high RPM?
- **Intake manifold:** Variable runner length? Resonance tuning for target RPM?
- **Exhaust:** Lower restriction (headers, high-flow cat, better muffler)?
- **For each modification:**
  - How much VE improvement expected? (estimate based on literature or experience)
  - At what RPM range?
  - What's the trade-off? (Example: Long-duration cam improves high RPM but hurts idle and low-speed torque)

**4. Calculations (15% weight)**
- **Power prediction:** If VE improves from X% to Y%, power increases proportionally (approximately)
  - Power = (ṁ_air × AFR × LHV_fuel × η_thermal) = f(VE)
- **Or:** Calculate airflow with improved VE and estimate power
- Show before/after comparison

**5. Cost-Benefit & Implementation (10% weight)**
- Cost of modifications
- Reliability impact
- Emissions impact
- Is improvement worth the investment?

**Deliverable:** 5 page technical report with flow analysis, proposed mods, calculations

---

**Assessment Rubric (All Options):**

| Criterion | Excellent (90-100%) | Good (75-89%) | Adequate (60-74%) | Needs Improvement (<60%) |
|-----------|-------------------|---------------|-------------------|------------------------|
| **Application/Problem Definition** | Clear, realistic scenario with well-defined targets/constraints. | Good definition. Minor ambiguities. | Basic definition. Some details missing. | Poorly defined or unrealistic. |
| **Technical Analysis** | Sophisticated use of module concepts. Accurate calculations. Sound reasoning. | Good technical work. Minor errors or gaps. | Basic analysis. Some errors or missing steps. | Weak analysis or major errors. |
| **Solution Development** | Comprehensive, actionable solution. Trade-offs analyzed. Feasible. | Good solution with reasonable justification. | Generic or incomplete solution. | Poor or impractical solution. |
| **Calculations & Quantification** | Accurate calculations shown. Results interpreted correctly. | Mostly correct. Minor errors. | Calculations attempted but with errors. | Missing or incorrect calculations. |
| **Workplace Relevance** | Clearly applicable to real workplace. Practical constraints considered. | Good connection to practice. | Weak connection. Mostly theoretical. | No clear relevance. |

**Learning Outcomes Addressed:**
- SO-3-5-1, SO-3-5-2, SO-3-5-3, SO-3-5-4: VE analysis, turbocharging, boosting technologies
- SO-3-6-1, SO-3-6-2, SO-3-6-3, SO-3-6-4: Fuel injection systems, mixture ratios, injection strategies
- SO-3-7-1, SO-3-7-2: Charge motion strategies (if applicable to VE optimization)

---

## MODULE 4: COMBUSTION PROCESSES
### Problem 4: Combustion Optimization & Diagnostics

**Timeline:**
- Assigned: End of Session 10
- Work Period: 1 week
- Due: Before Session 11
- Presentations: Session 11 (5 min each, 2-3 students selected)

**Context:**
Combustion is where the "magic" happens - fuel energy converts to mechanical work. But combustion problems cause knock, misfire, excessive emissions, poor efficiency, and durability issues. Optimizing combustion requires understanding SI vs CI processes, combustion phasing, and diagnostic techniques.

**Problem Statement:**
Select ONE scenario relevant to your workplace and develop a solution using combustion analysis principles:

**OPTION A: SI Engine Knock/Combustion Issues**
**OPTION B: Diesel Engine Combustion Optimization (NOx-PM-Efficiency)**
**OPTION C: Advanced Combustion Mode Implementation Feasibility**

---

### OPTION A: SI Engine Knock & Combustion Issues

**Scenario:**
SI engines in your fleet/application experience:
- Persistent knock under certain conditions (limiting performance)
- Misfire or unstable combustion
- Pre-ignition or surface ignition issues
- Inability to meet power targets without knock

**Requirements:**

**1. Problem Characterization (20% weight)**
- Engine specs: CR, turbo/NA, fuel type, ignition system
- Symptoms: When does knock occur? (RPM, load, temperature, fuel quality?)
- Knock sensor data or audible knock?
- Impact: Performance limitation? Component damage risk? Customer complaints?

**2. Knock Mechanism Analysis (25% weight)**
- **Why is this engine knocking?**
  - Compression ratio too high for available fuel?
  - Excessive boost without adequate timing retard?
  - Hot spots in combustion chamber?
  - EGR system not functioning?
  - Carbon buildup increasing effective CR?
- **End-gas conditions:** Estimate temperature and pressure of end-gas
  - High load → high pressure → high temperature → knock tendency increases
- **Octane requirement:** Does engine octane requirement exceed available fuel?

**3. Mitigation Strategies (30% weight)**
Propose solutions (select 2-3):

**Immediate/Calibration Solutions:**
- Retard spark timing in knock-prone regions (quantify: how much? at what conditions?)
  - Trade-off: Reduced power/efficiency, higher EGT
- Enrich mixture at high load (already doing this? enrich more?)
  - Trade-off: Fuel economy penalty
- Increase EGR rate (if equipped)
  - Dilution slows burn, reduces peak temperature
  - Trade-off: PM increases (if GDI), slower combustion
- Aggressive knock control strategy
  - Detect and retard cylinder-by-cylinder
  - Learn adaptation over time

**Medium-term Solutions:**
- Switch to higher octane fuel (if available and cost-acceptable)
- Clean carbon deposits (walnut blasting for GDI)
- Upgrade to colder spark plugs
- Improve cooling system (lower charge temperature)

**Long-term/Hardware Solutions:**
- Lower compression ratio (new pistons - expensive)
- Add/improve intercooling
- Implement water/methanol injection (charge cooling + octane boost)
- Redesign combustion chamber to eliminate hot spots

**4. Combustion Phasing Analysis (15% weight)**
- Ideal: 50% mass fraction burned (MFB) at 8-10° ATDC
- If knocking: MFB-50 is likely too early (too much advance) or end-gas dwelling too long
- How would you adjust combustion phasing? (timing, mixture, EGR, charge motion?)

**5. Validation & Risks (10% weight)**
- How to test solutions safely? (Dyno with knock monitoring?)
- Success criteria?
- What are failure risks? (EGT too high? Power loss? Still knocking?)

**Deliverable:** 5-6 page report with knock analysis, proposed solutions, trade-off evaluation

---

### OPTION B: Diesel Combustion Optimization

**Scenario:**
Diesel engines must balance:
- **NOx emissions** (regulatory compliance, SCR urea consumption cost)
- **PM emissions** (DPF regeneration frequency, filter life, visible smoke)
- **Fuel efficiency** (operating cost)
- **Combustion noise** (NVH, customer acceptance)

You are tasked with optimizing combustion calibration or proposing hardware changes.

**Requirements:**

**1. Current State Assessment (15% weight)**
- Engine: Type, common rail pressure, EGR system, turbo, after-treatment (DPF, SCR?)
- Current challenge: Which is the limiting factor?
  - Excessive NOx requiring frequent SCR refills or failing emissions?
  - Excessive PM causing frequent DPF regeneration or smoke?
  - Poor fuel economy?
  - Unacceptable combustion noise?
- Operating conditions where problem is worst

**2. Combustion Process Analysis (25% weight)**
Analyze the 4 phases of diesel combustion for your engine:
- **Ignition delay:** Current duration? Affected by cetane, EGR, injection pressure?
  - Long delay → more premixed combustion → high pressure rise rate → noise, NOx
  - Short delay → more mixing-controlled combustion → less noise, but diffusion flames → PM
- **Premixed combustion:** Intensity? Is this phase causing knock-like noise?
- **Mixing-controlled combustion:** Duration? Quality of mixing? PM formation regions?
- **Late combustion:** Complete burnout or PM carryover?

**3. NOx-PM Trade-off Management (30% weight)**
Propose calibration or hardware strategies:

**In-Cylinder Strategies:**
- **Injection timing:**
  - Advance → more NOx, less PM, better efficiency
  - Retard → less NOx, more PM, lower efficiency
  - Specify: SOI change and predicted impact
- **Injection pressure:**
  - Increase rail pressure → better atomization → less PM, but may increase NOx
  - Current pressure? Target pressure?
- **EGR rate:**
  - Increase → lower NOx, but more PM and slower combustion
  - Optimize EGR vs load/speed map
- **Pilot injection:**
  - Optimize quantity and timing to reduce ignition delay and noise
  - Too much pilot → wasted fuel, PM
- **Multiple injections:**
  - Shape combustion: Pilot + main + post
  - Post-injection: PM reduction (early post) or DPF regen (late post)
- **Charge motion (swirl):**
  - Increase swirl → better mixing → less PM
  - Variable swirl flaps?

**After-Treatment Strategy:**
- If NOx-PM trade-off managed by optimizing for efficiency and using SCR+DPF aggressively
- Can you calibrate for lower PM (advanced timing) and rely on SCR for NOx?
  - Trade-off: Urea consumption cost vs fuel economy gain
- Or calibrate for lower NOx (retarded timing, high EGR) and rely on DPF?
  - Trade-off: Fuel economy loss vs reduced SCR cost

**4. Quantitative Analysis (20% weight)**
- Estimate NOx-PM trade-off:
  - "If I advance SOI by 3° CA, NOx increases ~20-30%, PM decreases ~15-20%"
  - Use literature values or experience-based estimates
- Fuel economy impact estimate
- After-treatment burden: Regeneration frequency, urea consumption

**5. Implementation (10% weight)**
- What calibration parameters to modify?
- Validation testing plan
- Expected outcomes vs acceptance criteria

**Deliverable:** 6 page report with combustion analysis, NOx-PM optimization strategy, after-treatment integration

---

### OPTION C: Advanced Combustion Mode Feasibility

**Scenario:**
Your organization is evaluating advanced combustion modes for next-generation engine or retrofit:
- **HCCI** (Homogeneous Charge Compression Ignition)
- **RCCI** (Reactivity Controlled Compression Ignition)
- **PCCI** (Premixed Charge Compression Ignition)
- **Atkinson/Miller Cycle** (practical implementation via VVT)

Assess technical feasibility for your application.

**Requirements:**

**1. Application Context (10% weight)**
- Target application: What type of engine, duty cycle, power requirements?
- Why consider advanced combustion? (Efficiency target? Emissions? Performance?)

**2. Combustion Mode Deep Dive (30% weight)**
Select ONE advanced mode and explain:
- **Operating principle:** How does combustion occur differently from conventional SI/CI?
- **Efficiency mechanism:** Why is it more efficient? (Thermodynamic or practical reasons)
- **Emissions characteristics:** NOx, PM, HC, CO - better or worse than conventional?
- **Control challenges:** What makes it difficult to implement?
- **Operating range:** Load/speed envelope where it works

**Example - HCCI:**
- No spark, no injection timing control → ignition by compression auto-ignition
- Lean homogeneous mixture → low peak temperature → very low NOx, low PM
- High efficiency due to fast burn (nearly constant-volume), no throttling, lean operation
- Control problem: Cannot directly control ignition timing (dependent on charge temperature, pressure, mixture)
- Limited load range: Too low → misfire, too high → excessive pressure rise rate
- Practical only for narrow mid-load range; requires mode-switching with SI or CI

**3. Feasibility Assessment (30% weight)**
For YOUR application:
- **Technical feasibility:** Can the required hardware be integrated? (VVT for Miller? Dual fuel for RCCI? Temperature control for HCCI?)
- **Operating range match:** Does your duty cycle allow operation in the mode's viable range?
- **Control complexity:** Can your ECU handle it? Development cost?
- **Fuel requirements:** Special fuel quality? Dual fuel infrastructure?
- **Cost:** Hardware, development, validation - justified by benefits?

**4. Benefits Quantification (20% weight)**
Estimate benefits if implemented:
- Fuel economy improvement: 10-15% (HCCI), 5-8% (Miller), etc. - use literature values
- Emissions reduction
- Performance impact (if any)
- Operating cost change

**5. Recommendation (10% weight)**
- Go/No-Go decision with reasoning
- If "Go": Roadmap for implementation (development phases, testing, validation)
- If "No-Go": Why not? What would need to change to make it feasible?

**Deliverable:** 5-6 page technical feasibility study with combustion mode analysis, benefit/cost assessment, recommendation

---

**Assessment Rubric (All Options):**

| Criterion | Excellent (90-100%) | Good (75-89%) | Adequate (60-74%) | Needs Improvement (<60%) |
|-----------|-------------------|---------------|-------------------|------------------------|
| **Problem/Context Definition** | Clear, realistic, well-defined problem or feasibility question. | Good definition with minor gaps. | Basic definition. Some ambiguity. | Poorly defined. |
| **Combustion Analysis** | Sophisticated understanding of combustion processes. Correct application of module concepts. | Good combustion analysis. Minor gaps. | Basic analysis. Some errors or omissions. | Weak or incorrect analysis. |
| **Solution Development** | Comprehensive, technically sound solution. Multiple strategies considered. Trade-offs analyzed. | Good solution with reasonable justification. | Generic solution. Weak trade-off analysis. | Poor or impractical solution. |
| **Quantitative Support** | Calculations, estimates, or data used to support conclusions. Realistic values. | Some quantification. Mostly reasonable. | Limited quantitative support. | No quantification or unrealistic values. |
| **Workplace Applicability** | Clearly relevant to real applications. Practical constraints considered. | Good connection to practice. | Weak relevance. Mostly theoretical. | Not applicable to workplace. |

**Learning Outcomes Addressed:**
- SO-4-8-1, SO-4-8-2, SO-4-8-3, SO-4-8-4: SI combustion, knock, octane, advanced SI strategies
- SO-4-9-1, SO-4-9-2, SO-4-9-3, SO-4-9-4, SO-4-9-5: Diesel combustion phases, spray, NOx-PM, injection effects
- SO-4-10-1, SO-4-10-2, SO-4-10-3, SO-4-10-4: Thermodynamic cycles, Atkinson/Miller, HCCI/RCCI, VCR

---

## MODULE 5: EMISSIONS CONTROL
### Problem 5: Emissions Compliance Strategy

**Timeline:**
- Assigned: End of Session 13
- Work Period: 1 week
- Due: Before Session 14
- Presentations: Session 14 (5 min each, 2-3 students selected)

**Context:**
Emission regulations drive modern engine design. Whether meeting new standards, diagnosing emissions failures, or optimizing after-treatment systems, emissions engineering is critical for compliance and operational viability.

**Problem Statement:**
Address an emissions-related workplace challenge using integrated in-cylinder and after-treatment strategies.

**Scenarios (Select ONE):**

**OPTION A: Meeting New Emission Standard**
Your fleet/product line must comply with a newer emissions standard (e.g., BS-VI, Euro 6d, EPA Tier 3, China 6). Design the compliance strategy.

**OPTION B: Emissions Diagnostic & Repair**
Engines failing emissions tests or experiencing MIL illumination, DPF regeneration issues, or SCR faults. Diagnose and repair.

**OPTION C: After-Treatment System Optimization**
Optimize after-treatment performance to reduce operating costs (urea consumption, regeneration frequency, maintenance) while maintaining compliance.

---

### OPTION A: Compliance Strategy for New Standard

**Requirements:**

**1. Regulatory Analysis (15% weight)**
- **Define the standard:** Which regulation? (Euro 6, BS-VI, EPA Tier 3, etc.)
- **Emission limits:** NOx, PM, CO, HC (g/km, g/kWh, or mg/km) - list for your engine category
- **Test procedure:** NEDC? WLTP? RDE? Steady-state cycles for heavy-duty?
- **Previous vs new standard:** How much tighter are limits? Which pollutant is the challenge?

**2. Current Emissions Baseline (15% weight)**
- **Engine:** Type, size, current certification (if known or estimated)
- **Current emission levels:** Engine-out (before after-treatment) and tailpipe
- **Gap analysis:** How much reduction needed for each pollutant?
- **Which pollutant is hardest to meet?**

**3. In-Cylinder Strategy (25% weight)**
Propose combustion optimization:

**For SI Engines:**
- Stoichiometric operation for TWC? Or lean with LNT/SCR?
- GDI PM control: Injection strategy, piston design, GPF?
- Cold-start HC/CO: Retarded timing, secondary air, fast cat light-off?
- NOx control: EGR? Lean burn?

**For CI Engines:**
- NOx-PM optimization: Injection strategy, EGR rate, advanced combustion modes?
- Calibration for efficiency while relying on SCR for NOx?
- Or calibrate for lower engine-out NOx (retarded timing, high EGR) with less after-treatment burden?

**4. After-Treatment System Design (30% weight)**
Specify after-treatment:

**SI Engines:**
- **TWC:** Close-coupled + underfloor? Substrate volume? Precious metal loading?
- **GPF** (Gasoline Particulate Filter) needed? (Likely for GDI Euro 6d)
  - Substrate type, regeneration strategy (passive)
- **Cold-start:** Secondary air injection? Electrically heated catalyst?

**CI Engines:**
- **DOC** (Diesel Oxidation Catalyst): Specifications?
- **DPF:** Substrate material, volume, regeneration strategy (passive, active, forced - how often?)
- **SCR:** Catalyst type (Vanadia, Fe-Zeolite, Cu-Zeolite?), location (upstream or downstream of DPF?)
  - Urea dosing strategy: Dosing rate, control precision
  - Low-temp SCR performance (critical for RDE)
- **ASC** (Ammonia Slip Catalyst) needed?
- **System integration:** DOC → DPF → SCR or SCR → DPF (SCR-on-filter)?

**5. Cost-Benefit & Validation (15% weight)**
- **System cost:** Hardware, development, validation testing
- **Operating cost:** Urea consumption (if SCR), regeneration fuel penalty (if DPF), maintenance
- **Fuel economy impact:** Does compliance strategy hurt or help efficiency?
- **Validation:** Certification testing plan (lab + RDE if applicable)
- **Risk mitigation:** What if initial calibration doesn't meet limits? Backup plan?

**Deliverable:** 6-7 page compliance strategy report with regulatory analysis, in-cylinder + after-treatment design, cost estimate

---

### OPTION B: Emissions Diagnostic

**Requirements:**

**1. Fault Description (15% weight)**
- **Symptom:** MIL on? Failed I/M test? Visible smoke? DPF regeneration too frequent? High urea consumption?
- **DTCs:** List diagnostic trouble codes (real or realistic)
- **Freeze-frame data:** Operating conditions when fault occurred
- **Vehicle/engine:** Make, model, mileage, emission system configuration

**2. System Analysis (25% weight)**
Analyze the emission control system:

**For MIL / Emission Test Failure:**
- Which pollutant(s) exceeded limits? (NOx, HC, CO, PM?)
- Which monitor failed? (Catalyst efficiency, O2 sensor, EGR, EVAP?)
- **Possible causes:**
  - Failed catalyst (low efficiency)
  - O2 sensor fault (slow response, bias, failure)
  - Air leaks (false lean, rich trim, failed cat)
  - Misfire (HC spike, cat damage)
  - EGR valve stuck (too much → rich, PM; too little → NOx)
- Use diagnostic tree to narrow down

**For DPF Issues:**
- **Excessive regeneration:** Why is soot accumulation high?
  - Incomplete combustion (injector fault, low compression?)
  - Oil consumption (piston rings, turbo seals?)
  - Diesel quality (sulfur, additives?)
  - DPF not reaching regeneration temp (short trips, exhaust leak?)
- **Regeneration failure:** Exhaust temp not high enough? Post-injection not working? DPF clogged with ash?

**For SCR Issues:**
- **High NOx / Low SCR efficiency:** Urea dosing insufficient? Urea quality (frozen, contaminated)? SCR catalyst degraded? Ammonia slip?
- **Urea system fault:** Dosing pump, urea tank heater, quality sensor, lines frozen?

**3. Diagnostic Process (25% weight)**
- **Data gathering:** Scan tool live data, component tests (O2 sensor response, EGR flow, DPF pressure delta, SCR temp)
- **Component tests:**
  - O2 sensor: Switch rate test, voltage range
  - Catalyst: Monitor efficiency (upstream vs downstream O2)
  - EGR: Commanded vs actual flow
  - DPF: Pressure differential sensor, soot load estimate
  - SCR: NOx sensors upstream/downstream, urea dosing rate
- **Root cause determination:** Use logic and data to identify failed component or system

**4. Repair Solution (25% weight)**
- **What needs repair/replacement?**
- **Procedure:** Component replacement, cleaning (DPF, EGR), recalibration, relearn?
- **Validation:** Post-repair checks, drive cycle for monitor readiness, retest
- **Predicted outcome:** Will repair resolve issue? Any residual concerns?

**5. Prevention (10% weight)**
- **Maintenance recommendations:** Intervals, oil quality, fuel quality, driving style (avoid short trips for DPF)
- **Monitoring:** Proactive data logging to catch issues before MIL?

**Deliverable:** 5-6 page diagnostic report with fault tree, test data, root cause, repair procedure

---

### OPTION C: After-Treatment Optimization

**Requirements:**

**1. Current After-Treatment Performance (15% weight)**
- **System:** DOC, DPF, SCR, GPF? Configuration?
- **Operating costs:**
  - DPF regeneration frequency (if diesel): How often? Fuel penalty?
  - SCR urea consumption (L/1000 km or gallons/year): Current rate? Cost?
  - Maintenance: DPF cleaning/replacement frequency? SCR replacement?
- **Compliance status:** Meeting emissions? Margin to limits?

**2. Opportunity Identification (20% weight)**
- **Where is the inefficiency?**
  - DPF: Regenerating too often? Why? (High soot loading, low passive regen, short trips?)
  - SCR: Excessive urea consumption? Over-dosing to ensure compliance? Low SCR efficiency?
  - Maintenance: Components failing prematurely?
- **Can we optimize without compromising compliance?**

**3. Optimization Strategies (35% weight)**

**DPF Optimization:**
- **Reduce soot production (in-cylinder):**
  - Improve fuel atomization (injection pressure, nozzle condition)?
  - Optimize injection timing and swirl?
  - Higher quality fuel (cetane, additives)?
- **Increase passive regeneration:**
  - Operate at higher exhaust temps more often (avoid excessive idling?)
  - DOC catalyst performance (is it oxidizing NO to NO2 for passive regen?)
  - Use fuel-borne catalyst additives?
- **Optimize active regeneration:**
  - Trigger less frequently but more completely?
  - Improve regeneration efficiency (better post-injection timing)?
  - Minimize fuel penalty

**SCR Optimization:**
- **Improve SCR efficiency:**
  - Is catalyst at optimal temperature? (Too cold → low efficiency, must dose more urea)
  - Ammonia uniformity: Is urea mixing well or wall wetting?
  - Catalyst degraded? Replacement needed?
- **Optimize dosing strategy:**
  - Reduce over-dosing (some systems dose conservatively to ensure compliance)
  - Improve dosing precision and control
  - Model-based dosing vs simple table lookup
- **Urea quality:** Ensure DEF purity (contamination degrades performance)

**System Integration:**
- **Engine calibration + after-treatment co-optimization:**
  - Can engine be calibrated for slightly higher engine-out NOx (better fuel economy) if SCR efficiency is improved?
  - Or reduce engine-out PM to reduce DPF burden?
- **Thermal management:** Ensure after-treatment temps optimal (especially for low-temp cycles, RDE)

**4. Quantitative Analysis (20% weight)**
- **Cost savings estimate:**
  - Regeneration fuel consumption reduction: X L/1000 km saved
  - Urea consumption reduction: Y L/1000 km saved
  - Maintenance interval extension: Z$ savings per year
- **Compliance margin:** Still meet emissions with optimization?
- **Payback period:** Investment (if hardware changes) vs annual savings

**5. Implementation (10% weight)**
- **Action plan:** What to change? (Calibration, operating procedures, hardware?)
- **Testing/validation:** How to verify improvements without compromising compliance?
- **Monitoring:** Ongoing tracking of regeneration frequency, urea consumption, emissions

**Deliverable:** 5-6 page optimization study with current performance analysis, proposed changes, cost-benefit analysis

---

**Assessment Rubric (All Options):**

| Criterion | Excellent (90-100%) | Good (75-89%) | Adequate (60-74%) | Needs Improvement (<60%) |
|-----------|-------------------|---------------|-------------------|------------------------|
| **Problem Definition** | Clear, specific emissions challenge with regulatory or operational context. | Good problem description. Minor gaps. | Basic description. Some ambiguity. | Poorly defined problem. |
| **Technical Analysis** | Deep understanding of emission formation and control. Correct application of module concepts. | Good analysis with minor gaps. | Basic analysis. Some errors. | Weak or incorrect analysis. |
| **Solution Strategy** | Comprehensive integration of in-cylinder + after-treatment. Trade-offs analyzed. Realistic. | Good solution. Reasonable integration. | Basic solution. Weak integration or trade-off analysis. | Poor or impractical solution. |
| **Quantification** | Cost, emissions, performance quantified with realistic estimates. | Some quantification. Mostly reasonable. | Limited quantification. | No quantitative support. |
| **Compliance & Feasibility** | Clear path to regulatory compliance. Practical implementation. | Likely compliant. Reasonably practical. | Unclear if compliant. Questionable feasibility. | Non-compliant or impractical. |

**Learning Outcomes Addressed:**
- SO-5-11-1, SO-5-11-2, SO-5-11-3, SO-5-11-4: Emission formation mechanisms, NOx-PM trade-off
- SO-5-12-1, SO-5-12-2, SO-5-12-3, SO-5-12-4, SO-5-12-5: TWC, diesel after-treatment (DOC/DPF/SCR)
- SO-5-13-1, SO-5-13-2, SO-5-13-3, SO-5-13-4, SO-5-13-5: Regulations, OBD-II, diagnostics

---

## MODULE 6: ADVANCED TECHNOLOGIES
### Problem 6: Future Powertrain Technology Assessment

**Timeline:**
- Assigned: End of Session 15
- Final deliverable: End of course (2 weeks)
- Presentations: Optional (during final session or separate presentation day)

**Context:**
The automotive and power generation industries are in rapid transition. IC engines face competition from electrification while simultaneously evolving with advanced technologies: alternate fuels, hybridization, efficiency improvements, carbon-neutral synthetic fuels. As an engineer, you must assess emerging technologies for your organization's future strategy.

**Problem Statement:**
Conduct a comprehensive technology assessment for your organization, evaluating the technical and economic feasibility of adopting advanced IC engine technologies or transitioning to alternative powertrains.

**Requirements:**

**1. Organization & Application Context (10% weight)**
- **Your organization:** Industry sector (automotive, trucking, power gen, construction, marine, etc.)
- **Current powertrain:** Diesel, gasoline, natural gas? Fleet size or application scale?
- **Business drivers:** Why consider new technology?
  - Regulatory pressure (emissions, carbon targets)?
  - Operating cost (fuel, maintenance)?
  - Market differentiation?
  - Technology obsolescence risk?

**2. Technology Options Analysis (40% weight)**
Evaluate at least THREE technology pathways. Options include:

**Advanced IC Engine Technologies:**
- **Alternate fuels:** CNG, hydrogen, biodiesel, ethanol, e-fuels (synthetic)
- **High-efficiency engines:** Thermal efficiency >50% (advanced diesel, Miller cycle, dual-fuel, Achates opposed-piston)
- **Hybrid powertrains:** Mild hybrid, full hybrid, series hybrid, plug-in hybrid (IC engine as range extender or prime mover)
- **Thermal management & waste heat recovery:** ORC, turbocompound, electric turbo
- **Advanced combustion:** HCCI, RCCI, lean-burn SI with SCR
- **Carbon-neutral pathways:** E-fuels, bio-fuels with carbon capture

**Alternative Powertrains (for comparison):**
- **Battery Electric Vehicles (BEV):** For your application, is full electrification viable?
- **Fuel Cell Electric Vehicles (FCEV):** Hydrogen fuel cells vs hydrogen ICE?

**For EACH technology, analyze:**

**Technical Feasibility:**
- **How does it work?** (Brief technical description)
- **Maturity:** TRL (Technology Readiness Level)? Commercial availability?
- **Performance:** Power density, efficiency, emissions
- **Infrastructure:** Fuel availability? Refueling/recharging? Maintenance?
- **Integration:** Can it retrofit existing platforms or requires clean-sheet design?

**Economic Feasibility:**
- **Capital cost:** Vehicle/engine cost premium vs current technology?
- **Operating cost:** Fuel cost ($/km or $/kWh), maintenance, consumables (urea, etc.)?
- **Total Cost of Ownership (TCO):** Over 5 years, 10 years, lifetime?
- **Payback period:** How long to recover higher upfront cost through operating savings?

**Suitability for YOUR Application:**
- **Duty cycle match:** Does the technology suit your operating profile?
  - Long-haul → range critical (favors diesel, hydrogen, hybrid)
  - Urban → low emissions critical (favors electric, CNG, hybrid)
  - Remote → infrastructure critical (favors diesel, portable fuels)
  - High utilization → TCO critical (favors most efficient option)
- **Constraints:** Weight limits, space, charging/refueling downtime acceptable?

**3. Comparative Analysis (25% weight)**
Create comparison matrix:

| Technology | Efficiency | Emissions | Capital Cost | Operating Cost | TCO (10yr) | Infrastructure | Maturity | Overall Score |
|------------|-----------|-----------|--------------|----------------|------------|----------------|----------|---------------|
| Current (baseline) | X% | Baseline | $$ | $$/km | $$$ | Existing | High | - |
| Option 1: CNG | Y% | -30% NOx | +15% | -20% | $$$ | Moderate | High | ? |
| Option 2: Hybrid | Z% | -40% CO2 | +40% | -25% | $$$ | Good (elect grid) | High | ? |
| Option 3: H2 ICE | W% | Zero CO2 | +60% | +10% | $$$$ | Low | Medium | ? |

**Scoring Criteria (define your weighting based on priorities):**
- Example: Emissions 30%, TCO 40%, Infrastructure 20%, Maturity 10%
- Calculate weighted scores to rank technologies

**4. Lifecycle & Sustainability Analysis (10% weight)**
- **Well-to-wheel emissions:** Not just tailpipe! How is fuel/electricity produced?
  - Example: BEV is zero tailpipe but grid electricity may be coal-based
  - CNG: Natural gas extraction and transport emissions
  - Hydrogen: Green hydrogen (electrolysis from renewables) vs grey hydrogen (SMR from natural gas)
  - E-fuels: Carbon-neutral if CO2 captured and renewable energy used for synthesis
- **Lifecycle carbon footprint:** Which pathway achieves lowest total carbon over lifetime?
- **Circular economy:** End-of-life considerations (battery recycling, engine rebuild ability?)

**5. Recommendation & Roadmap (15% weight)**
- **Primary recommendation:** Which technology path for your organization? Why?
- **Justification:** Technical, economic, and strategic reasoning
- **Implementation roadmap:**
  - **Phase 1 (0-2 years):** Pilot testing? Small-scale deployment?
  - **Phase 2 (2-5 years):** Fleet transition plan? Infrastructure build-out?
  - **Phase 3 (5-10 years):** Full adoption target? Contingency if technology doesn't mature as expected?
- **Risk mitigation:** What are the risks? (Technology maturity, fuel availability, regulatory changes, cost volatility)
  - Backup plan?
- **Alternative scenario:** If your primary choice isn't viable, what's the fallback?

**Deliverables:**
1. **Technical Report (10-12 pages):**
   - Executive Summary (1 page): Key findings and recommendation
   - Organization context and drivers
   - Technology analysis (3 pathways minimum)
   - Comparative evaluation with scoring matrix
   - Lifecycle/sustainability analysis
   - Recommendation with roadmap
   - Risk assessment
   - References (technical literature, industry reports, regulatory documents)

2. **Presentation (if required):**
   - 10-15 minute presentation summarizing findings
   - Visual aids: Comparison charts, TCO graphs, roadmap timeline
   - Q&A session

**Assessment Rubric:**

| Criterion | Excellent (90-100%) | Good (75-89%) | Adequate (60-74%) | Needs Improvement (<60%) |
|-----------|-------------------|---------------|-------------------|------------------------|
| **Application Context** | Clear, realistic organization and application. Business drivers well-defined. | Good context. Minor gaps. | Basic context. Some ambiguity. | Poorly defined context. |
| **Technology Analysis** | Comprehensive analysis of 3+ technologies. Technical depth. Realistic data. | Good analysis of 3 technologies. Minor gaps. | Basic analysis. Some technologies superficially treated. | Weak or incomplete analysis. |
| **Economic Evaluation** | Detailed TCO analysis with reasonable assumptions. Sensitivity analysis. | Good economic evaluation. Mostly reasonable assumptions. | Basic cost analysis. Some questionable assumptions. | Poor or missing economic analysis. |
| **Comparative Evaluation** | Sophisticated comparison with weighted scoring. Clear methodology. | Good comparison. Reasonable approach. | Basic comparison. Weak methodology. | Poor or absent comparison. |
| **Sustainability Analysis** | Comprehensive well-to-wheel and lifecycle assessment. Carbon accounting. | Good lifecycle consideration. Some gaps. | Basic sustainability discussion. | Lifecycle/sustainability ignored. |
| **Recommendation Quality** | Clear, well-justified recommendation. Realistic roadmap. Risk mitigation. | Good recommendation with reasonable justification and roadmap. | Weak justification or vague roadmap. | Poor or impractical recommendation. |

**Learning Outcomes Addressed:**
- SO-6-14-1: Evaluate properties and combustion characteristics of alternate fuels
- SO-6-14-2: Assess engine modifications for alternate fuels
- SO-6-14-3: Compare lifecycle emissions and sustainability of fuel pathways
- SO-6-14-4: Analyze role of IC engines in future mobility scenarios
- SO-6-15-1, SO-6-15-2, SO-6-15-3: Thermal management, friction reduction, waste heat recovery
- SO-6-15-4: Integrate multiple technologies for system-level efficiency

---

## SUMMARY: SITUATED LEARNING PROBLEMS OVERVIEW

| Module | Problem Title | Core Challenge | Key Concepts Applied | Deliverable |
|--------|---------------|----------------|---------------------|-------------|
| **1** | Design & Justify Your Workplace Engine | Engine specification and design parameter selection | Architecture, displacement, CR, BMEP, torque/power, breathing | 3-4 page report + calculations |
| **2** | Optimize Performance in Your Fleet | Diagnose and solve performance/efficiency/drivability issue | Performance metrics, BSFC maps, calibration, root cause analysis | 4-5 page diagnostic report + solution |
| **3** | Air & Fuel System Optimization | Turbo matching, fuel system diagnosis, or VE improvement | Airflow calculations, turbocharging, fuel injection, manifold design | 5-6 page technical report |
| **4** | Combustion Optimization & Diagnostics | Knock mitigation, diesel NOx-PM optimization, or advanced combustion | Combustion processes, knock, NOx-PM trade-off, combustion modes | 5-6 page analysis report |
| **5** | Emissions Compliance Strategy | Meet new standards, diagnose emissions faults, or optimize after-treatment | Emission formation, after-treatment systems, regulations, OBD-II | 6-7 page compliance/diagnostic report |
| **6** | Future Powertrain Technology Assessment | Evaluate advanced IC technologies or alternative powertrains for adoption | Alternate fuels, hybrid, efficiency tech, TCO, sustainability, roadmap | 10-12 page technology assessment + presentation |

---

## PEDAGOGICAL NOTES FOR INSTRUCTORS

### Why Situated Learning?
- **Adult learners** (M.Tech working professionals) learn best when content connects directly to their work context
- **Transfer of learning** is higher when problems are authentic and personally relevant
- **Motivation** increases when students see immediate applicability
- **Deep processing** occurs when students must integrate multiple concepts to solve complex, realistic problems

### Implementation Tips
1. **Encourage real workplace problems:** Best learning when students tackle issues they actually face
2. **Provide scaffolding:** Give examples, templates, or sample calculations to guide students who struggle
3. **Facilitate peer learning:** Presentations and peer feedback are as valuable as instructor feedback
4. **Manage scope:** Some students will go very deep - ensure they don't spend excessive time
5. **Flexible assessment:** If a student's workplace doesn't match a problem perfectly, allow alternate scenarios
6. **Connect to theory:** In feedback, explicitly link student solutions to course concepts

### Common Challenges & Solutions
- **"My workplace doesn't use IC engines":** Provide industry scenarios or allow hypothetical applications
- **Data not available:** Allow reasonable assumptions and estimates (teach estimation skills)
- **Confidentiality:** Allow students to anonymize or generalize their workplace examples
- **Time constraints:** Problems span 1 week each - ensure realistic scope expectations

---

**Document Control:**
Version: 1.0
Created: January 2026
Author: Course Design System
Status: Ready for Instructor Review
