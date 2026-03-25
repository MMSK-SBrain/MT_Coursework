# REVISED Course Structure: Advances in IC Engines (AE ZG516)

**Design Philosophy (Updated):**
- **Start with engaging fundamentals** - gamified "Build an Engine" approach
- Foundation → Performance → Air/Fuel → Combustion → Emissions → Future
- Emissions as "the constraint that defines modern engine design"
- Each session connects to workplace reality
- 2-3 MCQs embedded per session + situated learning per module

---

## 🎮 Module 1: Engine Foundations - Build Your Engine (2 sessions)
**Theme:** "Design your engine from the ground up - make smart trade-offs"

### **Session 1: Build Your Engine - Architecture & Power Fundamentals**
**Gamification Hook:** *"You're designing an engine for a specific application (delivery truck / sports car / generator). What choices will you make?"*

**Content:**
- **Engine architecture choices:** Inline vs V-configuration, number of cylinders
- **Displacement, bore, stroke:** Trade-offs and selection criteria
- **Torque vs Power:** What's the difference? Which matters more for YOUR application?
  - Torque curves vs power curves
  - Why diesel engines are "torquey"
  - BMEP as a performance metric
- **Compression ratio:** Impact on efficiency and power
- **Key components overview:** Block, head, pistons, crankshaft, connecting rods, valvetrain

**Interactive Element:**
- Students make design decisions for their workplace engine type
- Calculate basic performance parameters (displacement, BMEP)
- Compare torque/power requirements for different applications

**MCQs (2-3):**
1. For a delivery truck requiring low-speed pulling power, which is more critical: high peak power or high low-end torque?
2. Calculate: An engine with 500mm bore, 600mm stroke, and 6 cylinders has what displacement?
3. If you increase compression ratio, what happens to thermal efficiency (all else equal)?

**Learning Outcomes (SOs):**
- SO-1-1-1: Differentiate between torque and power and select appropriate targets for specific applications
- SO-1-1-2: Analyze engine architecture choices and their impact on packaging, weight, and performance
- SO-1-1-3: Calculate basic engine parameters (displacement, BMEP, compression ratio)

---

### **Session 2: Build Your Engine - Breathing & Control Systems**
**Gamification Hook:** *"Your engine needs to breathe and think. How will you make it efficient and smart?"*

**Content:**
- **4-stroke cycle review:** Intake → Compression → Power → Exhaust (high-level, visual)
- **Volumetric efficiency:** Why it matters, what affects it
  - Valve timing and lift
  - Flow restrictions
  - Temperature and pressure effects
- **Engine control fundamentals:**
  - What does an ECU/ECM do?
  - Key sensors: MAP, MAF, TPS, O2 sensor, knock sensor, crank/cam position
  - Key actuators: Fuel injectors, ignition coils, throttle, VVT
  - Closed-loop control concept
- **High-level system overview:** How air, fuel, combustion, and control work together

**Interactive Element:**
- Analyze a simple engine control loop (e.g., air-fuel ratio control)
- Identify what sensor/actuator failures would cause specific symptoms
- Trade-off: Valve overlap vs low-speed torque vs emissions

**MCQs (2-3):**
1. If volumetric efficiency is 85%, what does that mean?
2. Which sensor is critical for closed-loop air-fuel ratio control?
3. Increasing valve overlap typically improves high-speed breathing but hurts ___?

**Learning Outcomes (SOs):**
- SO-1-2-1: Explain the 4-stroke cycle and identify factors affecting volumetric efficiency
- SO-1-2-2: Describe the role of engine control systems and identify key sensors and actuators
- SO-1-2-3: Analyze basic control loops and predict effects of component failures

**Situated Learning Problem (Module 1):**
*"Design Your Workplace Engine"*
- What application? (urban delivery, highway transport, construction equipment, etc.)
- Key performance requirements? (torque curve, power, efficiency, packaging)
- Make architecture choices: cylinders, displacement, bore/stroke, compression ratio
- Justify your decisions with calculations and trade-off analysis
- Present to class: "Here's my engine and why I made these choices"

---

## 🎯 Module 2: Performance & Calibration Excellence (2 sessions)
**Theme:** "Now optimize your engine to meet real-world targets"

### **Session 3: Performance Metrics & Operating Characteristics**
**Hook:** *"What makes one engine great and another mediocre? How do you measure success?"*

**Content:**
- **Performance parameters deep dive:**
  - Indicated vs brake power, friction losses
  - Thermal efficiency, mechanical efficiency, volumetric efficiency
  - Specific fuel consumption (BSFC)
  - Torque and power curves - interpretation and analysis
- **Operating characteristics:**
  - Effect of spark timing on SI engine performance
  - Effect of injection timing on CI engine performance
  - Compression ratio trade-offs (efficiency vs knock vs NOx)
  - Load and speed effects on efficiency map
- **Engine design parameters:** How bore/stroke ratio, valve timing, and CR affect performance

**MCQs (2-3):**
1. If indicated power is 100 kW and brake power is 85 kW, what is mechanical efficiency?
2. Advancing spark timing too far causes ___ and reduces power
3. Which operating condition typically gives best BSFC: full load, part load, or idle?

**Learning Outcomes (SOs):**
- SO-2-3-1: Calculate and interpret performance parameters (BMEP, efficiencies, BSFC)
- SO-2-3-2: Analyze torque and power curves to identify engine characteristics
- SO-2-3-3: Evaluate the effect of operating parameters (timing, CR, load) on performance

---

### **Session 4: Engine Calibration Strategies**
**Hook:** *"You've built an engine. Now make it sing - balancing performance, emissions, and drivability."*

**Content:**
- **What is engine calibration?** The art and science of optimization
- **SI engine calibration:**
  - Spark timing maps (speed vs load)
  - Fuel injection maps (open loop vs closed loop)
  - VVT strategies for torque and efficiency
  - Trade-offs: Performance vs emissions vs fuel economy
- **CI engine calibration:**
  - Injection timing and pressure
  - EGR rate calibration
  - Multi-pulse injection strategies (pilot, main, post)
- **Calibration process:** Dyno testing, DoE methods, automated calibration tools
- **Drivability considerations:** Transient response, tip-in/tip-out, NVH

**MCQs (2-3):**
1. Why do SI engines typically run rich at full load?
2. In a diesel engine, advancing injection timing typically increases NOx but reduces ___
3. What is the purpose of pilot injection in modern diesel engines?

**Learning Outcomes (SOs):**
- SO-2-4-1: Apply spark timing and fuel calibration strategies for SI engines
- SO-2-4-2: Apply injection timing and EGR strategies for CI engines
- SO-2-4-3: Evaluate calibration trade-offs between performance, emissions, and drivability

**Situated Learning Problem (Module 2):**
*"Optimize Performance in Your Fleet"*
- Select an engine from your workplace (or the one you "designed" in Module 1)
- Identify performance issue: poor fuel economy, lack of power, drivability concerns
- Propose calibration changes (timing, fueling, VVT, EGR)
- Predict outcomes using performance principles
- Estimate improvement potential and validation approach

---

## 💨 Module 3: Air & Fuel Systems - The Foundation of Good Combustion (3 sessions)
**Theme:** "You can't have good combustion without good air-fuel preparation"

**Pedagogical Note:** Air/fuel systems BEFORE combustion because:
- Follows physical sequence (intake → combustion)
- Students understand the INPUT before the PROCESS
- When they learn combustion, they'll understand mixture quality and charge motion context
- Logical: "How do we get air and fuel IN?" before "What happens when they burn?"

---

### **Session 5: Air Intake, Exhaust, & Boosting Systems**
**Hook:** *"Your engine needs to breathe. How do you help it inhale more air?"*

**Content:**
- **Volumetric efficiency deep dive:**
  - Definition and factors affecting VE
  - Flow through valves (valve lift, duration, flow coefficients)
  - Port design and flow optimization
  - Intake and exhaust manifold design
  - Temperature and resonance effects
- **Turbocharging fundamentals:**
  - Why boost? Pressure ratio and mass flow increase
  - Compressor and turbine matching
  - Wastegate control and boost pressure regulation
  - Intercooling benefits
  - Turbo lag and mitigation strategies
- **Supercharging:** Mechanical vs turbo, trade-offs

**MCQs (2-3):**
1. If atmospheric pressure is 100 kPa and boost pressure is 150 kPa absolute, what is the pressure ratio?
2. What is the primary purpose of an intercooler?
3. Which has better transient response: turbocharger or supercharger? Why?

**Learning Outcomes (SOs):**
- SO-3-5-1: Analyze factors affecting volumetric efficiency and valve flow characteristics
- SO-3-5-2: Design turbocharging systems and evaluate boost control strategies
- SO-3-5-3: Compare boosting technologies for specific applications

---

### **Session 6: Fuel Injection Systems & Mixture Formation**
**Hook:** *"Air is in the cylinder. Now how do you deliver the right amount of fuel, at the right time, in the right form?"*

**Content:**
- **SI engine fuel systems:**
  - Port fuel injection (MPFI) vs Gasoline Direct Injection (GDI)
  - Fuel pressure requirements and injector characteristics
  - Stoichiometric vs lean vs rich mixture - when and why?
  - Air flow measurement: MAF vs MAP (speed-density)
  - Cold start enrichment, transient compensation
- **CI engine fuel systems:**
  - Common rail diesel injection
  - Injection pressure (1500-2500 bar modern systems)
  - Injector nozzle design (holes, spray angle)
  - Multiple injection strategies (pilot, main, post)
- **Fuel properties:** Octane rating (SI), cetane rating (CI)

**MCQs (2-3):**
1. GDI allows stratified charge operation, which enables ___
2. Why do common rail diesel systems use such high injection pressure?
3. Lambda = 1 means what air-fuel ratio for gasoline?

**Learning Outcomes (SOs):**
- SO-3-6-1: Compare fuel injection technologies (MPFI, GDI, common rail) and select for applications
- SO-3-6-2: Calculate mixture ratios and evaluate mixture requirements for different operating modes
- SO-3-6-3: Analyze fuel metering strategies and transient compensation methods

---

### **Session 7: Charge Motion & In-Cylinder Flow Dynamics**
**Hook:** *"It's not enough to get air and fuel in - they need to MOVE the right way for good combustion."*

**Content:**
- **In-cylinder flow types:**
  - **Swirl:** Rotation around cylinder axis (especially CI engines)
  - **Tumble:** End-over-end rotation (especially SI engines)
  - **Squish:** High-velocity flow during compression from piston crown shape
- **Why charge motion matters:**
  - Enhances mixing (especially for diesel spray)
  - Increases flame speed in SI engines
  - Reduces cycle-to-cycle variation
  - Enables lean combustion and stratified charge
- **How to create charge motion:**
  - Port design (helical ports, directional ports)
  - Valve deactivation or masking
  - Piston bowl shape and squish area
  - Tumble flaps and variable geometry intakes
- **Unwanted flows:**
  - Crevice flows and their effect on HC emissions
  - Blow-by and ring pack design

**MCQs (2-3):**
1. Which charge motion is most important for diesel engine mixing: swirl or tumble?
2. Squish is created by the interaction of ___ and ___ near TDC
3. What is the primary source of HC emissions from crevice volumes?

**Learning Outcomes (SOs):**
- SO-3-7-1: Differentiate between swirl, tumble, and squish and explain their benefits
- SO-3-7-2: Design charge motion strategies for SI and CI engines
- SO-3-7-3: Analyze the impact of crevice flows and blow-by on emissions

**Situated Learning Problem (Module 3):**
*"Improve Air-Fuel System Performance"*
- Identify air or fuel system limitation in your workplace engine
  - Low volumetric efficiency?
  - Poor mixture quality?
  - Turbo lag issues?
  - Inadequate charge motion?
- Analyze root cause using principles from Module 3
- Propose hardware or calibration solution (port mod, turbo upgrade, injector change, etc.)
- Estimate performance improvement (power, efficiency, emissions)
- Cost-benefit analysis and implementation plan

---

## 🔥 Module 4: Combustion Processes - Where the Magic Happens (3 sessions)
**Theme:** "Understanding what happens when air and fuel burn - the heart of the engine"

### **Session 8: Combustion in SI Engines**
**Hook:** *"A flame front racing across the cylinder at 10-30 m/s. How do we control it?"*

**Content:**
- **SI combustion process:**
  - Ignition and flame kernel formation
  - Flame structure (preheat zone, reaction zone, post-flame zone)
  - Flame propagation speed - what affects it?
  - Turbulence and charge motion effects (connection to Session 7!)
  - Mass burn rate and 50% burn location (MBT timing)
- **Ignition system fundamentals:**
  - Spark plug design and placement
  - Ignition energy requirements
  - Multi-spark and lean burn ignition
- **Knock phenomenon:**
  - What is knock? End-gas auto-ignition
  - Factors promoting knock (compression ratio, timing, temperature, fuel octane)
  - Detection (knock sensor) and mitigation (timing retard, enrichment)
  - Fuel octane rating and anti-knock additives
- **Advanced SI combustion:**
  - Lean burn and stratified charge (GDI)
  - EGR in SI engines
  - Cycle-to-cycle variation

**MCQs (2-3):**
1. What is the primary factor that causes engine knock?
2. Why does tumble enhance flame speed?
3. If knock occurs, which calibration changes would mitigate it? (Select all that apply)

**Learning Outcomes (SOs):**
- SO-4-8-1: Analyze SI combustion process and flame propagation characteristics
- SO-4-8-2: Diagnose and mitigate knock using fuel quality, timing, and mixture strategies
- SO-4-8-3: Evaluate advanced SI combustion strategies (lean burn, stratified charge)

---

### **Session 9: Combustion in CI Engines**
**Hook:** *"No spark plug. Fuel ignites on its own. How do we control THAT?"*

**Content:**
- **CI combustion process phases:**
  - Ignition delay period (physical + chemical delay)
  - Premixed combustion phase (rapid pressure rise)
  - Mixing-controlled combustion phase (diffusion flame)
  - Late combustion and soot oxidation
- **Fuel spray behavior:**
  - Spray penetration, atomization, and evaporation
  - Air entrainment and mixing
  - Role of swirl in air utilization (connection to Session 7!)
  - Spray-wall interaction and piston bowl design
- **Direct injection vs Indirect injection:**
  - IDI: Swirl chamber, glow plug assist
  - DI: Higher efficiency, modern standard
- **In-cylinder emission control:**
  - NOx-PM trade-off (temperature vs mixing)
  - Multiple injection strategies:
    - Pilot injection: Reduce noise and premixed burn
    - Main injection: Power delivery
    - Post injection: DPF regeneration, after-treatment support
  - EGR effects on combustion
- **Diesel fuel properties:** Cetane rating, viscosity, volatility

**MCQs (2-3):**
1. What causes the NOx-PM trade-off in diesel combustion?
2. What is the purpose of pilot injection in modern diesel engines?
3. High swirl in diesel engines improves ___ but may increase ___

**Learning Outcomes (SOs):**
- SO-4-9-1: Analyze CI combustion phases and fuel spray behavior
- SO-4-9-2: Evaluate injection strategies to optimize NOx-PM trade-off
- SO-4-9-3: Apply piston bowl and swirl design to improve diesel combustion efficiency

---

### **Session 10: Advanced Engine Cycles & Combustion Modes**
**Hook:** *"The Otto and Diesel cycles are just the beginning. What's next?"*

**Content:**
- **Thermodynamic cycle review (contextual, NOT standalone theory):**
  - Otto cycle (SI engines)
  - Diesel cycle (CI engines)
  - Why real engines differ from ideal cycles
- **Advanced thermodynamic cycles:**
  - **Atkinson/Miller cycle:**
    - Over-expansion for efficiency
    - Implementation: Late intake valve closing or early closing
    - Applications: Hybrid powertrains
  - **HCCI (Homogeneous Charge Compression Ignition):**
    - Promise: SI efficiency + CI fuel economy
    - Challenge: Combustion timing control
    - Operating range limitations
  - **RCCI, PCCI, GDCI:** Advanced low-temperature combustion modes
- **Compression ratio vs expansion ratio:** Decoupling for efficiency
- **Variable compression ratio engines:** Infiniti VC-Turbo case study

**MCQs (2-3):**
1. Miller/Atkinson cycle achieves higher thermal efficiency by ___
2. What is the primary challenge with HCCI engines?
3. In a Miller cycle engine with late intake valve closing, effective compression ratio is ___ than geometric CR

**Learning Outcomes (SOs):**
- SO-4-10-1: Compare thermodynamic cycles (Otto, Diesel, Atkinson, Miller) and their applications
- SO-4-10-2: Evaluate advanced combustion modes (HCCI, RCCI) and their limitations
- SO-4-10-3: Analyze strategies for improving thermal efficiency through cycle modification

**Situated Learning Problem (Module 4):**
*"Diagnose & Optimize Combustion in Your Engine"*
- Identify combustion-related issue in workplace:
  - SI: Knock, poor fuel economy, rough idle, misfire
  - CI: Excessive smoke, noise, poor combustion efficiency, PM issues
- Use available diagnostic data:
  - Performance data (power, BSFC)
  - Visual inspection (smoke color, deposits)
  - Diagnostic codes if available
- Analyze root cause using combustion principles
- Propose solution: Calibration, fuel quality, hardware change?
- Validation plan and success metrics

---

## 🌍 Module 5: Emissions - The Constraint That Defines Modern Engine Design (3 sessions)
**Theme:** "Performance is important, but emissions compliance is mandatory. How do we win at both?"

### **Session 11: Emission Formation Mechanisms**
**Hook:** *"Every time fuel burns, we create pollutants. Understanding WHY is the first step to controlling them."*

**Content:**
- **The four horsemen: NOx, CO, HC, PM**
- **NOx (Nitrogen Oxides) formation:**
  - Thermal NOx mechanism (Zeldovich)
  - Why high temperature and oxygen availability matter
  - Peak cylinder temperature zones
  - Trade-off with efficiency (hotter = more efficient but more NOx)
  - Mitigation: EGR, water injection, SCR
- **CO (Carbon Monoxide) formation:**
  - Incomplete combustion - lack of oxygen
  - Rich mixture conditions
  - Quench layers and crevices
  - Mitigation: Stoichiometric or lean operation, oxidation catalysts
- **HC (Hydrocarbons - Unburned fuel) sources:**
  - Crevice volumes (ring pack, gasket areas)
  - Quench layers on cool walls
  - Liquid fuel films (especially GDI wall wetting)
  - Oil consumption
  - Mitigation: Minimize crevices, optimize mixture, oxidation catalysts
- **PM (Particulate Matter) in diesel:**
  - Soot formation in fuel-rich zones
  - Insufficient air-fuel mixing
  - Soot oxidation vs formation balance
  - Mitigation: High injection pressure, EGR, DPF
- **In-cylinder vs after-treatment strategies**

**MCQs (2-3):**
1. NOx formation increases with ___ and ___
2. Which emission is primarily caused by rich combustion in SI engines?
3. What is the dominant source of HC emissions: crevice volumes, or bulk gas quenching?

**Learning Outcomes (SOs):**
- SO-5-11-1: Analyze formation mechanisms for NOx, CO, HC, and PM
- SO-5-11-2: Identify emission sources for different engine operating conditions
- SO-5-11-3: Evaluate in-cylinder strategies to reduce emission formation

---

### **Session 12: Exhaust Gas After-Treatment Systems**
**Hook:** *"Can't prevent all emissions in-cylinder? Clean them up in the exhaust!"*

**Content:**
- **SI engine after-treatment:**
  - **Three-way catalytic converter (TWC):**
    - Simultaneous NOx reduction, CO and HC oxidation
    - Requires stoichiometric operation (lambda = 1)
    - Catalyst materials (platinum, palladium, rhodium)
    - Light-off temperature and warm-up strategies
  - Oxygen sensors and closed-loop control
  - Catalyst aging and poisoning
- **CI engine after-treatment:**
  - **Diesel Oxidation Catalyst (DOC):** CO and HC oxidation, NO to NO2 conversion
  - **Diesel Particulate Filter (DPF):**
    - Traps PM mechanically
    - Regeneration strategies (passive, active, fuel post-injection)
    - Ash accumulation and cleaning
  - **Selective Catalytic Reduction (SCR):**
    - NOx reduction using urea (AdBlue/DEF)
    - Ammonia as reducing agent
    - Temperature window for effectiveness
  - **System integration:** DOC + DPF + SCR sequencing
- **LNT (Lean NOx Trap):** Alternative to SCR
- **Particulates in GDI engines:** GPF (Gasoline Particulate Filter)

**MCQs (2-3):**
1. Why must TWC operate at stoichiometric air-fuel ratio?
2. What triggers active DPF regeneration?
3. What chemical is injected upstream of SCR catalyst?

**Learning Outcomes (SOs):**
- SO-5-12-1: Design three-way catalyst systems for SI engines with closed-loop control
- SO-5-12-2: Design integrated after-treatment systems for diesel engines (DOC, DPF, SCR)
- SO-5-12-3: Evaluate regeneration and urea dosing strategies for DPF and SCR systems

---

### **Session 13: Regulations, Compliance, OBD & Diagnostics**
**Hook:** *"Meeting regulations isn't optional. How do we prove compliance - on the dyno AND on the road?"*

**Content:**
- **Global emission regulations:**
  - India: BS-VI evolution
  - Europe: Euro 6 and beyond
  - US: EPA Tier 3
  - China: China 6
  - Real Driving Emissions (RDE) testing
- **Test cycles:**
  - NEDC vs WLTP (why the change?)
  - FTP, SFTP cycles
  - Real-world vs lab compliance gap
- **On-Board Diagnostics (OBD-II):**
  - **Purpose:** Monitor emission control system effectiveness
  - **MIL (Check Engine Light):** When it illuminates
  - **Diagnostic Trouble Codes (DTCs):**
    - P-codes (powertrain), types: P0xxx (generic), P1xxx (manufacturer)
  - **Monitored systems:**
    - Catalyst efficiency
    - Oxygen sensor response
    - Evaporative emissions
    - EGR system
    - Misfire detection
  - **Readiness monitors and I/M programs**
- **Fault diagnosis workflow:**
  - Read codes → Analyze freeze frame data → Test components → Root cause → Fix → Clear codes → Validate
- **OBD regulations and compliance:** Must detect faults before emissions exceed 1.5x limits

**MCQs (2-3):**
1. What is the purpose of RDE (Real Driving Emissions) testing?
2. What does a P0420 code typically indicate?
3. OBD systems must illuminate MIL when emissions exceed ___x the standard

**Learning Outcomes (SOs):**
- SO-5-13-1: Compare global emission regulations and test cycles (BS-VI, Euro 6, EPA)
- SO-5-13-2: Diagnose emission system faults using OBD codes and data
- SO-5-13-3: Evaluate OBD monitoring strategies for emission control system components

**Situated Learning Problem (Module 5):**
*"Achieve Emission Compliance in Your Fleet"*
- Select emission challenge from workplace:
  - Failing emission test (NOx, PM, HC?)
  - OBD fault codes appearing
  - Customer complaints about MIL
  - Upcoming regulation change (BS-VI, Euro 6)
- Diagnose root cause:
  - In-cylinder issue (combustion, calibration)?
  - After-treatment issue (catalyst, DPF, SCR)?
  - Sensor/control issue?
- Propose mitigation strategy:
  - Calibration update?
  - Hardware retrofit?
  - Maintenance protocol?
- Cost-benefit analysis and regulatory validation plan

---

## 🚀 Module 6: Advanced Technologies & Future Directions (2 sessions)
**Theme:** "The IC engine is evolving. Where is it going?"

### **Session 14: Alternate Fuels & Energy Transition**
**Hook:** *"Gasoline and diesel won't last forever - or be allowed forever. What are the alternatives?"*

**Content:**
- **Natural gas (CNG, LNG):**
  - Properties: High octane, gaseous at atmospheric pressure
  - Combustion characteristics: Slower flame speed than gasoline
  - Engine modifications: Compression ratio increase potential
  - Emissions benefits: Lower CO2, near-zero PM, lower NOx (if lean)
  - Infrastructure challenges
  - Applications: Transit buses, trucks, stationary power
- **Alcohol fuels (Methanol, Ethanol):**
  - Properties: High octane, high heat of vaporization
  - Combustion benefits: Knock resistance, charge cooling
  - Challenges: Lower energy density, corrosion, cold start
  - Flex-fuel systems and blend sensing
  - Brazil ethanol case study
- **Hydrogen as IC engine fuel:**
  - Properties: Wide flammability limits, very fast flame speed
  - Combustion: Can run very lean for efficiency
  - Challenges: Abnormal combustion (pre-ignition, backfire), NOx at high load
  - Storage challenges (compressed gas, liquid, hydrides)
  - Applications: Heavy duty, off-road, hydrogen economy vision
- **Biodiesel and renewable diesel:**
  - Production from vegetable oils, animal fats
  - Properties similar to diesel but lower PM, higher NOx potential
  - Blend levels (B5, B20, B100)
- **Synthetic fuels (e-fuels):** Carbon-neutral potential
- **IC engines in electrified powertrains:** Range extenders, series hybrids

**MCQs (2-3):**
1. Why does CNG have good knock resistance?
2. What is the primary combustion challenge with hydrogen in IC engines?
3. Ethanol's high heat of vaporization provides what benefit?

**Learning Outcomes (SOs):**
- SO-6-14-1: Evaluate properties and combustion characteristics of alternate fuels (CNG, hydrogen, alcohols)
- SO-6-14-2: Assess engine modifications required for alternate fuel operation
- SO-6-14-3: Analyze the role of IC engines in future electrified and low-carbon powertrains

---

### **Session 15: Thermal Management, Friction Reduction & System Integration**
**Hook:** *"Every wasted Joule is lost efficiency. How do we recover heat and reduce losses?"*

**Content:**
- **Engine heat transfer:**
  - Heat flow paths: Combustion chamber → coolant → radiator
  - Intake and exhaust heat transfer
  - Heat transfer correlations (Woschni, etc.)
  - Effect on efficiency: Heat loss reduces work output
  - Thermal barrier coatings
- **Cooling system design:**
  - Coolant flow paths and thermostat control
  - Radiator and fan sizing
  - High-temperature cooling for efficiency
  - EGR cooling strategies
- **Friction and mechanical losses:**
  - Sources: Piston rings, bearings, valvetrain, accessories
  - FMEP (Friction Mean Effective Pressure)
  - Lubrication regimes: Hydrodynamic, boundary, mixed
  - Friction reduction strategies:
    - Low-tension piston rings
    - Roller followers in valvetrain
    - Low-viscosity oils (0W-20, 0W-16)
    - Surface coatings (DLC, etc.)
- **Lubrication system:**
  - Oil properties: Viscosity, additives
  - Oil consumption and PM emissions link
  - Variable displacement oil pumps
- **Waste heat recovery:**
  - Turbocompound systems
  - Organic Rankine Cycle (ORC)
  - Thermoelectric generators
- **System-level efficiency optimization:** Balancing all subsystems

**MCQs (2-3):**
1. What percentage of fuel energy is typically lost as heat in the coolant? (rough order)
2. Low-viscosity engine oils reduce friction but may increase ___
3. What is the purpose of a turbocompound system?

**Learning Outcomes (SOs):**
- SO-6-15-1: Analyze heat transfer paths and evaluate thermal management strategies
- SO-6-15-2: Evaluate friction reduction strategies and lubrication system design
- SO-6-15-3: Assess waste heat recovery technologies for efficiency improvement

**Situated Learning Problem (Module 6):**
*"Evaluate Future Technology for Your Application"*
- Select an advanced technology or alternate fuel for evaluation:
  - CNG or hydrogen conversion
  - Advanced combustion cycle (Atkinson, Miller)
  - Waste heat recovery
  - Friction reduction package
  - Electrification/hybridization
- Context: Your workplace application and constraints
- Technical assessment:
  - Performance impact
  - Emissions impact
  - Reliability and durability
- Business case:
  - Cost (capital, operating)
  - Payback period
  - Infrastructure requirements
  - Regulatory incentives/mandates
- Implementation roadmap: Pilot, validation, rollout

---

## 📊 Revised Module Summary

| Module | Sessions | Theme | Key Question | Situated Learning |
|--------|----------|-------|--------------|-------------------|
| **1. Foundations** | 1-2 | Build an Engine (Gamified) | "What makes an engine tick?" | Design your workplace engine |
| **2. Performance** | 3-4 | The Optimization Goal | "How do we make it perform?" | Optimize fleet performance |
| **3. Air & Fuel** | 5-7 | The Input Systems | "How do we get air & fuel in right?" | Improve air-fuel efficiency |
| **4. Combustion** | 8-10 | The Chemical Process | "What happens when it burns?" | Diagnose combustion issues |
| **5. Emissions** | 11-13 | The Design Constraint | "How do we meet regulations?" | Achieve emission compliance |
| **6. Advanced** | 14-15 | The Future | "Where are we going?" | Evaluate new technology |

**Total: 15 Sessions**

---

## 🎯 Pedagogical Flow - Why This Sequence?

### Phase 1: Foundation (Sessions 1-2)
**Gamified foundation** - Engaging, decision-making, builds intuition
- Students "build" an engine, understand components and fundamentals
- Torque/power, volumetric efficiency, control systems covered contextually
- Sets stage for all modules to follow

### Phase 2: The Goal (Sessions 3-4)
**Performance & Calibration** - What we're trying to achieve
- Now that they know engine basics, learn what "good" looks like
- Performance metrics, calibration strategies
- Creates motivation: "I want my engine to perform like this!"

### Phase 3: The Inputs (Sessions 5-7)
**Air & Fuel Systems** - How we enable good combustion
- Logical sequence: Intake → Fuel → Charge motion
- Builds from "getting air in" to "making it move right"
- Sets up combustion module: "Now we know what's in the cylinder and how it's moving"

### Phase 4: The Process (Sessions 8-10)
**Combustion** - What happens when mixture burns
- Students now understand inputs (air/fuel quality, charge motion)
- Can appreciate how those inputs affect combustion
- SI → CI → Advanced cycles (simple to complex)

### Phase 5: The Constraint (Sessions 11-13)
**Emissions** - The reality that shapes modern design
- "Everything we've learned is now constrained by emissions"
- Formation → After-treatment → Regulations
- Emphasizes: Emissions compliance is NOT optional
- MID-TERM after Session 13 (covers Modules 1-4 + emissions basics)

### Phase 6: The Future (Sessions 14-15)
**Advanced Technologies** - Where the industry is going
- Students have complete foundation to evaluate new tech
- Alternate fuels, efficiency technologies
- Prepares them for evolving industry

---

## 🔍 Key Design Decisions - Rationale

### 1. Air/Fuel BEFORE Combustion
**Why:**
- Follows physical sequence (intake → compression → combustion → exhaust)
- Students understand mixture preparation before chemical reaction
- Charge motion concepts (swirl, tumble) make more sense when they then learn about flame propagation and diesel spray mixing
- Easier cognitive progression: Physical → Chemical

**Alternative considered:** Combustion first to create "need to know"
**Rejected because:** Combustion is complex; without understanding mixture quality and charge motion context, it feels abstract

### 2. Gamified Foundation Sessions
**Why:**
- Students hate boring theory (especially thermodynamics)
- "Build an engine" creates engagement through decision-making
- Covers necessary fundamentals but in active, applied context
- Students use their workplace as design context → immediate relevance

### 3. Emissions as Module 5 (not earlier)
**Why:**
- Instructor insight: "Emissions define engine design in the real world"
- Placed after fundamentals so students understand what CAUSES emissions
- Before advanced topics so students see emissions as THE constraint for future tech
- Reinforces: Modern engine design = performance WITH compliance

### 4. Situated Learning Per Module (not per session)
**Why:**
- M.Tech working professionals - leverage workplace as learning lab
- One meaty problem per module more valuable than many shallow ones
- Allows depth, analysis, and peer learning
- Builds portfolio of workplace solutions through the course

### 5. 2-3 MCQs Embedded Per Session
**Why:**
- Formative assessment - check understanding in real-time
- Embedded in slides (not end-of-session quiz) → Active learning
- Mix of recall, application, analysis
- Low-stakes, immediate feedback

---

## Next Steps for Finalization

1. ✅ Module structure defined (6 modules, 15 sessions)
2. ✅ Session themes and content outlined
3. ✅ Pedagogical flow rationale documented
4. ⏳ **Need your approval on:**
   - Is the Air/Fuel before Combustion sequence correct?
   - Do the gamified foundation sessions cover what you need?
   - Is Module 5 placement (Emissions as design constraint) appropriate?
5. ⏳ Define detailed Session Outcomes (2-3 SOs per session)
6. ⏳ Draft sample MCQs for each session
7. ⏳ Detail situated learning problems with rubrics
8. ⏳ Update Course Objectives (COs) to align with new structure
9. ⏳ Build complete CO → MO → SO traceability matrix
10. ⏳ Generate Excel template

---

**Ready for your feedback!**
Once you approve this structure, I'll proceed to create the detailed learning outcomes hierarchy and generate the final Excel template.
