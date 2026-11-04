# All Session Templates
## AE ZG516: Advances in IC Engines

**Purpose:** Quick-reference templates for all 15 sessions with timing, key points, and delivery notes
**Usage:** Use alongside detailed session coverage document and lesson plan framework
**Format:** Concise, action-oriented templates for efficient lesson delivery

---

## HOW TO USE THESE TEMPLATES

Each session template includes:
- **Learning Outcomes:** What students will achieve
- **Time-Blocked Structure:** Minute-by-minute breakdown
- **Key Teaching Points:** Must-cover content with emphasis areas
- **Delivery Notes:** Pedagogical tips, common student questions, warnings
- **Assessment Points:** When to use MCQs and exercises
- **Materials Needed:** Slides, props, calculations prepared

---

## MODULE 1: ENGINE FOUNDATIONS - BUILD YOUR ENGINE

### SESSION 1: Build Your Engine - Architecture, Power, Thermodynamics (90 min)

**Learning Outcomes:** SO-1-1-1, SO-1-1-2, SO-1-1-3, SO-1-1-4

**Hook [0-5 min]:**
- *Gamification intro:* "You're an engine designer. Here's the spec: Design an engine for [delivery truck / sports car / generator]. What choices will you make?"
- Show 3 contrasting engine images: Formula 1 V6 turbo, heavy-duty diesel truck, industrial generator
- Ask: "What makes these engines different? By end of session, you'll know how to design for each application."

**Objectives & Recall [5-10 min]:**
- State 4 session outcomes clearly
- Activate prior knowledge: "What do you already know about engines from undergrad or work?"
- Session roadmap: Architecture → Performance metrics → Thermodynamics → Components → Design exercise

**Part 1: Engine Architecture & Configuration [10-30 min]:**
- **Cylinder arrangement (5 min):**
  - Inline, V, opposed, radial - show visuals
  - Trade-offs table: Balance, packaging, cost, NVH
  - *Why question:* "Why V8 for trucks but inline-4 for economy cars?"
- **Bore & stroke (7 min):**
  - Define oversquare, square, undersquare with diagrams
  - Effect on piston speed, breathing, torque character
  - Show diesel (undersquare) vs F1 (oversquare) comparison
  - **Calculation demo:** Displacement = π/4 × bore² × stroke × cylinders
- **Compression ratio (8 min):**
  - Define, show diagram with clearance volume
  - CR range: SI (10-13:1), CI (15-20:1) - why the difference (knock vs auto-ignition)
  - Effect on efficiency (preview Otto cycle equation)
  - Modern trends: GDI enables higher CR
- **MCQ #1 [30-32 min]:** Displacement calculation question (Q1-1-3 from MCQ bank)

**Part 2: Torque, Power & Performance Metrics [32-57 min]:**
- **Torque vs Power (10 min):**
  - Critical distinction: Torque = force, Power = rate of work
  - Formula: Power (kW) = Torque (N·m) × RPM / 9549
  - **Why both matter:** Show truck (flat torque at low RPM) vs sports car (power at high RPM) curves
  - *Interactive:* Ask students: "For city bus, prioritize torque or power?"
- **BMEP (8 min):**
  - Best metric for comparison (displacement-independent)
  - Formula: BMEP = (Brake power × 120) / (Displacement × RPM × 2)
  - Typical values: 10-15 bar (NA SI), 20-30 bar (turbo)
  - **Worked example:** Calculate BMEP for given engine
- **Efficiencies (7 min):**
  - Thermal efficiency: Brake power / Fuel energy input
  - Mechanical efficiency: Brake / Indicated
  - BSFC: Lower is better (200-220 g/kWh excellent)
- **MCQ #2 [57-59 min]:** Torque characteristic question (Q1-1-1)

**Part 3: Thermodynamic Cycles (Contextual) [59-79 min]:**
- **Otto cycle (7 min):**
  - P-V diagram with annotation
  - Efficiency formula: η = 1 - (1/CR^(γ-1))
  - Higher CR → higher efficiency
  - **Demo calculation:** Efficiency at CR=10 vs CR=12
- **Diesel cycle (5 min):**
  - Constant pressure heat addition vs Otto's constant volume
  - Higher CR possible (no knock limit)
  - P-V diagram comparison
- **Real vs Ideal (5 min):**
  - Heat loss, friction, pumping, incomplete combustion
  - Indicator diagram (real P-V trace)
  - Gap between theoretical and actual efficiency
- **MCQ #3 [79-81 min]:** CR effect on efficiency (Q1-1-2)

**Part 4: Engine Components Overview [81-86 min]:**
- **Speed walkthrough (5 min):**
  - Block, head, crankshaft, piston, connecting rod, valvetrain
  - Show cutaway diagram or physical components if available
  - Combustion chamber design: SI (pent-roof), CI (bowl-in-piston)
- Emphasize: Details in later sessions, now just big picture

**Interactive Design Exercise [86-91 min]:**
- **Scenario:** "Design engine for 10-ton delivery truck operating in city"
- Given: Torque target 500 N·m @ 1500 RPM, packaging limit
- Students decide (quick think-pair-share):
  - SI or CI?
  - Cylinders?
  - Turbo?
  - Estimate displacement needed
- Call on 2-3 students for answers, brief discussion of trade-offs

**Wrap-up [91-93 min]:**
- Key takeaways (show on slide):
  1. Architecture choices → performance characteristics
  2. Torque, power, BMEP are the performance language
  3. CR drives efficiency but has limits
  4. Real engines far from ideal cycles
- Preview Session 2: Breathing & control
- **Assignment:** Module 1 SLP assigned - design your workplace engine (due before Session 3)

**Materials Needed:**
- Slides with engine images, P-V diagrams, torque/power curves
- Physical props (optional): Piston, crankshaft section
- Calculator for demos
- MCQ delivery system (poll or slides)
- SLP handout

**Delivery Notes:**
- Keep thermodynamics light - context only, not heavy derivations
- Emphasize decision-making and trade-offs throughout
- Gamification: Repeatedly ask "For YOUR engine, what would you choose?"
- Expect questions on: CR limits, why diesel can't use higher RPM, turbo vs NA

---

### SESSION 2: Build Your Engine - Breathing & Control Systems (90 min)

**Learning Outcomes:** SO-1-2-1, SO-1-2-2, SO-1-2-3, SO-1-2-4

**Hook [0-5 min]:**
- "Your engine from Session 1 needs to breathe and control itself. How do we optimize the 4-stroke cycle?"
- Show video: High-speed intake valve motion (30 sec) - "Air flow is pulsating, not steady!"

**Objectives & Recall [5-8 min]:**
- Recall Session 1: We designed engine architecture. Now: How does it actually run?
- Today: 4-stroke cycle → VE → VVT → Control systems

**Part 1: 4-Stroke Cycle Deep Dive [8-28 min]:**
- Each stroke (5 min each): Intake, compression, power, exhaust
  - Describe what's happening
  - Valve position, pressure in cylinder
  - Energy flow (negative work on compression, positive on power)
- **Valve overlap (5 min):**
  - Both valves open near TDC - why?
  - Benefits: Scavenging, reduced pumping
  - Drawbacks: Low-speed torque loss, HC emissions
  - VVT optimizes across RPM range
- **MCQ #1 [28-30 min]:** Valve overlap effects (Q1-2-3)

**Part 2: Volumetric Efficiency [30-55 min]:**
- **Definition (5 min):**
  - VE = Actual air mass / Theoretical air mass
  - Typical: 75-95% NA, >100% with boost/tuning
  - **Calculation demo**
- **Factors affecting VE (15 min):**
  - Valve flow: Size, lift, duration, # of valves
  - Port design: Smooth flow vs charge motion trade-off
  - Manifold: Runner length/diameter tuning
  - Temperature: Cooler = denser
  - Speed: VE vs RPM curve (peaks then drops)
- **Improving VE (5 min):**
  - Larger valves, 4-valve, VVT, tuned manifolds, forced induction
- **MCQ #2 [55-57 min]:** VE calculation (Q1-2-1)

**Part 3: Variable Valve Timing [57-72 min]:**
- **Why VVT (3 min):** Optimize valve timing across RPM/load
- **Technologies (7 min):**
  - Cam phasing (most common)
  - Dual VVT, profile switching (VTEC), variable lift
  - Benefits at each condition: Low RPM (reduce overlap), high RPM (increase overlap), part load (late closing for Atkinson effect)
- **Cylinder deactivation (5 min):** Shut off cylinders at light load → improve BSFC

**Part 4: Engine Control Systems [72-87 min]:**
- **ECU architecture (5 min):**
  - Inputs (sensors) → Processing (maps, calculations) → Outputs (actuators)
- **Key sensors (4 min):**
  - MAF, MAP, TPS, O2, knock, temp, crank/cam position
  - Show physical sensors if available
- **Key actuators (3 min):**
  - Injectors, ignition coils, VVT solenoids, throttle
- **Control loops (3 min):**
  - Open loop vs closed loop
  - **Example:** AFR control using O2 sensor feedback
- **MCQ #3 [87-89 min]:** O2 sensor for closed-loop control (Q1-2-2)

**Interactive Diagnostic Exercise [89-92 min]:**
- **Scenario:** Engine runs rough, poor fuel economy, black smoke. MAF reading high, O2 sensor shows rich.
- **Question:** What failed?
- **Answer:** MAF over-reading → ECU adds too much fuel
- Brief discussion

**Wrap-up [92-93 min]:**
- Breathing + control = performance
- Module 1 complete: You can now design an engine (architecture + breathing + control)
- **Reminder:** SLP due before Session 3 - peer presentations will happen

**Materials:** Slides, sensor/actuator images, MAF sensor (if available), diagnostic scan tool data screenshot

**Delivery Notes:**
- VE is abstract - use lots of visuals (valve flow, manifold tuning animations)
- Control systems: Don't get lost in sensor details - focus on system thinking
- Link back to Session 1: "This is how your designed engine actually breathes"

---

## MODULE 2: PERFORMANCE & CALIBRATION

### SESSION 3: Performance Analysis & Operating Characteristics (90 min)

**Learning Outcomes:** SO-2-3-1, SO-2-3-2, SO-2-3-3, SO-2-3-4

**Hook [0-5 min]:**
- **Peer presentations:** 2-3 students present Module 1 SLP (5 min total, very brief)
- **Provocative question:** "Two engines, same displacement. One makes 150 hp, other 300 hp. What's different? Which is 'better'?"

**Objectives [5-7 min]:**
- Today: Go deep into performance metrics, understand what makes engines different
- Outcomes: Calculate efficiency/BSFC, interpret curves, analyze timing/CR effects, use BSFC maps

**Part 1: Performance Parameters Deep Dive [7-32 min]:**
- **Power & Torque revisited (5 min):**
  - Indicated vs brake, friction power
  - Dynamometer measurement
- **Thermal efficiency (8 min):**
  - η_th = Brake power / (Fuel mass flow × LHV)
  - **Worked example:** Calculate efficiency given fuel flow, power, LHV
  - Modern best: 40-42% SI, 45-50% CI
- **BSFC (7 min):**
  - BSFC = Fuel mass flow / Brake power (g/kWh)
  - Lower = better
  - BSFC map: Contour plot, "island of efficiency"
  - Hybrid/CVT operates in this island
- **Specific outputs (5 min):**
  - kW/L, N·m/L
  - Typical values for NA vs turbo, SI vs CI
- **MCQ #1 [32-34 min]:** Thermal efficiency interpretation (Q2-3-1)

**Part 2: Torque & Power Curves [34-54 min]:**
- **Curve interpretation (10 min):**
  - Flat torque vs peaky torque
  - Peak torque RPM vs peak power RPM
  - **Show 3 real curves:** Diesel truck, gasoline sedan, turbocharged sports car
  - What does shape tell us about application?
- **What affects curve shape (10 min):**
  - Displacement, CR, valve timing, turbo, fuel type
  - **Interactive:** "If we add a turbo to this NA engine, how does curve change?"
- **MCQ #2 [54-56 min]:** Torque curve interpretation (Q2-3-2)

**Part 3: Operating Parameters [56-86 min]:**
- **Spark timing - SI (12 min):**
  - MBT timing, knock-limited timing
  - Advancing vs retarding - effects
  - Spark map: RPM × load → timing
  - Factors: Load, RPM, temperature, octane, EGR
- **Injection timing - CI (10 min):**
  - Advancing → efficiency, NOx; Retarding → lower NOx, PM
  - Injection pressure effects
  - Multi-pulse injection
- **Compression ratio (4 min):**
  - Higher CR → higher efficiency
  - Limits: Knock (SI), mechanical (CI)
  - Modern trends
- **Efficiency maps (4 min):**
  - BSFC map analysis
  - Sweet spot: Mid-RPM, high load
  - Part-load efficiency: SI throttling loss
- **MCQ #3 [86-88 min]:** Spark timing too advanced (Q2-3-3)

**Interactive Exercise [88-91 min]:**
- Given BSFC map + two driving cycles (city vs highway)
- Students identify operating regions and efficiency
- Discuss how hybrid could help

**Wrap-up [91-93 min]:**
- Performance is multi-dimensional: Power, torque, efficiency, BSFC
- Maps are the language of performance
- Next: How to calibrate these maps (Session 4)

**Materials:** Real performance curves, BSFC maps, driving cycle data

**Delivery Notes:**
- Use LOTS of real data - makes it concrete
- BSFC maps are hard for students - spend time explaining axes and contours
- Connect efficiency to cost: "1% fuel economy = $X million for a fleet"

---

### SESSION 4: Engine Calibration Strategies (90 min)

**Learning Outcomes:** SO-2-4-1, SO-2-4-2, SO-2-4-3, SO-2-4-4

**Hook [0-5 min]:**
- "You've designed great hardware. But without calibration, it's expensive metal. Calibration makes it sing - or cry."
- Show before/after dyno runs: Same engine, bad cal vs good cal (torque curves)

**Objectives [5-7 min]:**
- What is calibration, why it matters, how to do it for SI and CI

**Part 1: Calibration Basics [7-22 min]:**
- **Definition (5 min):** Optimizing ECU maps to meet targets (performance, emissions, efficiency, drivability)
- **Parameters (5 min):** Hundreds! Fuel, timing, VVT, boost, EGR, lambda, transients, diagnostics
- **Challenge (5 min):** Cannot optimize all simultaneously - trade-offs
  - Triangle of doom: Power, emissions, fuel economy
  - Must prioritize

**Part 2: SI Calibration [22-57 min]:**
- **Spark timing cal (10 min):**
  - Base map, MBT vs knock-limited regions
  - Knock control strategy
  - Other adjustments: Cold start, tip-in
- **Fuel metering (12 min):**
  - Target λ: Stoich (TWC), rich (WOT cooling), lean (GDI stratified)
  - Base fuel map, closed-loop correction (STFT, LTFT)
  - Transient compensation (tip-in, wall wetting)
  - Cold start enrichment
- **VVT calibration (5 min):**
  - Intake/exhaust cam phasing maps
  - Low RPM vs high RPM vs part load strategies
- **Idle & throttle (3 min):**
  - Idle speed control
  - Electronic throttle pedal maps
- **MCQ #1 [57-59 min]:** Rich mixture at WOT (Q2-4-1)

**Part 3: CI Calibration [59-84 min]:**
- **Injection timing & pressure (8 min):**
  - SOI map, rail pressure map
  - Trade-off: Advance vs retard
- **Pilot injection (5 min):**
  - Reduces ignition delay and noise
  - Timing and quantity calibration
- **Post injection (4 min):**
  - DPF regen, SCR heating
- **EGR calibration (5 min):**
  - EGR rate map: Mid-load high, idle/high-load low
  - NOx-PM trade-off management
- **Boost control (3 min):**
  - Target boost map, wastegate/VGT control
- **MCQ #2 [84-86 min]:** Injection timing trade-off (Q2-4-2)

**Part 4: Trade-offs & Tools [86-89 min]:**
- Drivability, durability, market-specific calibration

**Interactive Case Study [89-92 min]:**
- Turbocharged SI engine: "Sluggish at low RPM, great at highway"
- Diagnose: Turbo lag
- Propose calibration solutions: Boost map, timing, anti-lag

**MCQ #3 [92-93 min]:** Pilot injection purpose (Q2-4-3)

**Wrap-up:**
- Module 2 SLP assigned: Performance optimization in your fleet (due before Session 5)
- Next module: Air & fuel systems (how air and fuel get to combustion chamber)

**Materials:** Calibration maps (spark, fuel, injection), dyno data, case study details

**Delivery Notes:**
- Calibration is vast - focus on principles and key maps
- Emphasize multi-objective optimization - no perfect calibration
- Students with calibration experience can share insights

---

## MODULE 3: AIR & FUEL SYSTEMS

### SESSION 5: Air Intake, Exhaust & Boosting (90 min)

**Learning Outcomes:** SO-3-5-1, SO-3-5-2, SO-3-5-3, SO-3-5-4

**Hook [0-5 min]:**
- "Engine is an air pump. More air = more power. How do we maximize breathing?"
- Show: NA engine vs turbocharged - power density comparison

**Part 1: VE Deep Dive [5-30 min]:**
- VE definition, flow through valves, port design, manifold tuning
- Temperature and altitude effects
- VE vs RPM curve
- **MCQ #1 [30-32 min]:** Manifold runner length (Q3-5-1)

**Part 2: Turbocharging [32-62 min]:**
- Why turbo, components (turbine, compressor, CHRA, wastegate)
- Performance parameters (PR, boost, efficiency, temp rise)
- Turbo matching, boost control, intercooling
- Turbo lag and mitigation
- **MCQ #2 [62-64 min]:** Boost pressure calculation (Q3-5-2)

**Part 3: Advanced Boosting [64-79 min]:**
- VGT, twin-scroll, sequential, twin-turbo, electric turbo
- Supercharging: Types, pros/cons vs turbo
- Twincharging
- **MCQ #3 [79-81 min]:** Supercharger vs turbo (Q3-5-3)

**Part 4: Exhaust System [81-84 min]:**
- Headers, catalysts, mufflers, backpressure

**Exercise [84-88 min]:**
- Turbo selection for 2.0L SI engine targeting 300 hp
- Calculate airflow, choose between small vs large turbo

**Wrap-up [88-90 min]:**
- Breathing determines power potential
- Next: How we deliver fuel to that air

**Materials:** Turbo cutaway (physical or video), compressor maps, airflow calculations

**Delivery Notes:**
- Turbo matching is complex - focus on concepts, not detailed map reading
- Use videos: Turbo operation, compressor surge, etc.
- Many students excited about turbos - channel that energy!

---

### SESSION 6: Fuel Injection & Mixture Formation (90 min)

**Learning Outcomes:** SO-3-6-1, SO-3-6-2, SO-3-6-3, SO-3-6-4

**Hook [0-5 min]:**
- "Air is in. Now: How much fuel? When? In what form?"
- Show high-speed video: GDI spray vs port injection

**Part 1: Fuel Properties & Mixtures [5-20 min]:**
- Stoichiometric AFR, lambda definition
- Why different mixtures: Stoich, rich, lean
- Octane (SI) and cetane (CI) ratings

**Part 2: SI Fuel Injection [20-50 min]:**
- **PFI (10 min):** System, components, advantages, disadvantages
- **GDI (15 min):** System, homogeneous vs stratified modes, advantages (charge cooling, lean burn), disadvantages (PM, carbon buildup)
- **Air flow measurement (5 min):** MAF vs MAP/speed-density
- **MCQ #1 [50-52 min]:** GDI stratified mode benefit (Q3-6-1)

**Part 3: CI Fuel Injection [52-82 min]:**
- **Common rail (15 min):** Why high pressure, system components, piezo injectors, pressure control
- **Multiple injections (8 min):** Pilot, main, post - purposes and effects
- **Nozzle design (4 min):** Holes, spray penetration, targeting
- **Other systems (3 min):** Unit injector, distributor pump
- **MCQ #2 [82-84 min]:** Common rail high pressure purpose (Q3-6-2)

**Part 4: Fuel System Dynamics [84-87 min]:**
- Transients, cold start, altitude, fuel quality adaptation

**Exercise [87-90 min]:**
- GDI homogeneous vs stratified comparison: Which mode when? Why?

**MCQ #3 [90 min]:** Lambda definition (Q3-6-3)

**Materials:** Injector cutaways, spray visualization videos, fuel system diagrams

**Delivery Notes:**
- GDI stratified is complex - use animations
- Common rail: Emphasize pressure → atomization → PM reduction link
- Fuel quality variations affect calibration - real-world relevance

---

### SESSION 7: Charge Motion & In-Cylinder Flow (90 min)

**Learning Outcomes:** SO-3-7-1, SO-3-7-2, SO-3-7-3, SO-3-7-4

**Hook [0-5 min]:**
- "Air and fuel are in cylinder. But if they just sit there, combustion is slow. We need MOTION."
- Show CFD video: Swirl and tumble in cylinder

**Part 1: Types of Charge Motion [5-30 min]:**
- **Swirl (8 min):** Definition, how to create, diesel applications, benefits/drawbacks
- **Tumble (8 min):** Definition, how to create, SI applications, benefits/drawbacks
- **Squish (5 min):** High-velocity flow near TDC, piston design, benefits
- **Turbulence (4 min):** Small-scale eddies, sources, benefits
- **MCQ #1 [30-32 min]:** Swirl for diesel (Q3-7-1)

**Part 2: SI Charge Motion Strategy [32-52 min]:**
- Primary goal: Enhance flame propagation
- Tumble → turbulence breakdown → faster flame
- GDI stratified: Guide fuel cloud to spark plug
- Trade-offs: Charge motion vs VE
- **MCQ #2 [52-54 min]:** Tumble and flame speed (Q3-7-2)

**Part 3: CI Charge Motion Strategy [54-74 min]:**
- Primary goal: Air-fuel mixing
- Swirl + squish, piston bowl design (re-entrant bowl)
- Fuel spray and swirl interaction
- Variable swirl control

**Part 4: Unwanted Flows [74-84 min]:**
- **Crevice flows (5 min):** Piston ring pack, HC emissions source
- **Blow-by (3 min):** Gas leakage past rings
- **Reverse flow (2 min):** Valve overlap backflow
- **MCQ #3 [84-86 min]:** Crevice volume HC emissions (Q3-7-3)

**Part 5: CFD & Experimental Methods [86-88 min]:**
- How to study flow: CFD, PIV, flow benches

**Exercise [88-91 min]:**
- Design charge motion for: 1) High-RPM SI engine, 2) Heavy-duty diesel
- Students identify: Swirl/tumble/squish combination, piston bowl shape
- Brief discussion

**Wrap-up [91-93 min]:**
- Module 3 complete: Air in, fuel in, mixed well → ready for combustion
- Module 3 SLP assigned: Air/fuel system optimization (due before Session 8)
- Next module: Combustion - where the magic happens

**Materials:** CFD videos, piston cross-sections, bowl geometry diagrams

**Delivery Notes:**
- Flow is invisible - heavy reliance on animations and CFD
- Swirl vs tumble: SI prefers tumble, CI prefers swirl - make this distinction clear
- Crevice flows are often overlooked - emphasize HC emissions connection

---

## MODULE 4: COMBUSTION PROCESSES

### SESSION 8: Combustion in SI Engines (90 min)

**Learning Outcomes:** SO-4-8-1, SO-4-8-2, SO-4-8-3, SO-4-8-4

**Hook [0-5 min]:**
- Show high-speed combustion video (SI flame propagation)
- "Combustion takes 40-60° of crank angle. What's happening during those milliseconds?"

**Part 1: SI Flame Propagation [5-30 min]:**
- Flame development, propagation, termination
- Laminar vs turbulent flame, flame speed factors
- **MCQ #1 [30-32 min]:** SI flame propagation process (Q4-8-1)

**Part 2: Engine Knock [32-57 min]:**
- Knock mechanism: End-gas auto-ignition
- Knock factors: CR, timing, temperature, octane
- Knock detection and mitigation
- **MCQ #2 [57-59 min]:** Knock mechanism (Q4-8-2)

**Part 3: Octane Rating & Knock Resistance [59-79 min]:**
- Octane definition, RON/MON/AKI
- Higher octane → higher CR or boost possible
- Fuel effects on combustion
- **MCQ #3 [79-81 min]:** Octane rating function (Q4-8-3)

**Part 4: Advanced SI Strategies [81-86 min]:**
- Lean burn, stratified charge, EGR
- Benefits and challenges

**Exercise [86-90 min]:**
- Knock mitigation scenario: Persistent knock at high load
- Students propose solutions (timing retard, fuel change, EGR, etc.)
- Discuss trade-offs

**Materials:** High-speed combustion videos, P-V diagrams, heat release rate plots

**Delivery Notes:**
- Combustion is fast and invisible - videos are essential
- Knock is common student question - spend adequate time
- Connect knock to real failures (piston melting, ring damage)

---

### SESSION 9: Combustion in CI Engines (90 min)

**Learning Outcomes:** SO-4-9-1, SO-4-9-2, SO-4-9-3, SO-4-9-4, SO-4-9-5

**Hook [0-5 min]:**
- "Diesel combustion is completely different. No spark. Multiple injection events. NOx-PM trade-off. Let's dive in."
- Show diesel spray and combustion video (if available)

**Part 1: Four Phases of Diesel Combustion [5-30 min]:**
- Ignition delay, premixed, mixing-controlled, late combustion
- What happens in each phase
- **MCQ #1 [30-32 min]:** Ignition delay definition (Q4-9-1)

**Part 2: Fuel Spray Behavior [32-52 min]:**
- Atomization, penetration, air entrainment
- Effect of injection pressure
- **MCQ #3 [52-54 min]:** Injection pressure and spray penetration (Q4-9-3)

**Part 3: NOx-PM Trade-off [54-79 min]:**
- Why trade-off exists
- In-cylinder strategies: Timing, pressure, EGR
- Modern approach: Optimize for efficiency, use after-treatment
- **MCQ #2 [79-81 min]:** NOx-PM trade-off explanation (Q4-9-2)

**Part 4: DI vs IDI, Injection Effects [81-86 min]:**
- Direct injection benefits
- Cetane rating, multiple injections

**Exercise [86-90 min]:**
- Given diesel combustion issue: Excessive smoke
- Diagnose: Injection pressure? Spray penetration? Air motion?
- Propose solution

**Materials:** Diesel combustion videos, spray visualization, NOx-PM curves

**Delivery Notes:**
- NOx-PM trade-off is THE central diesel challenge - emphasize
- Four phases: Use heat release rate plot to show
- Injection pressure → atomization → PM reduction is key takeaway

---

### SESSION 10: Advanced Cycles & Combustion Modes (90 min)

**Learning Outcomes:** SO-4-10-1, SO-4-10-2, SO-4-10-3, SO-4-10-4

**Hook [0-5 min]:**
- "Otto and Diesel cycles are 100+ years old. Can we do better? Yes - but with challenges."

**Part 1: Thermodynamic Cycles Comparison [5-30 min]:**
- Otto, Diesel, Dual cycles review
- Real engines vs ideal
- **MCQ #1 [30-32 min]:** Atkinson vs Otto cycle (Q4-10-1)

**Part 2: Atkinson/Miller Cycles [32-57 min]:**
- Expansion ratio > compression ratio
- Implementation via late IVC (Miller) or early IVC (Atkinson)
- Efficiency gain, power density loss
- Hybrid application (Prius)
- **MCQ #2 [57-59 min]:** Variable compression ratio benefit (Q4-10-3)

**Part 3: Advanced Combustion Modes [59-84 min]:**
- **HCCI (10 min):** Principle, benefits (efficiency, low NOx/PM), challenges (control, load range)
- **RCCI (5 min):** Dual fuel, reactivity control
- **PCCI (3 min):** Premixed diesel
- Why limited adoption: Control difficulty
- **MCQ #3 [84-86 min]:** HCCI control challenge (Q4-10-2)

**Part 4: Variable Compression Ratio [86-89 min]:**
- VCR technology, benefits, complexity

**Exercise [89-92 min]:**
- Assess HCCI feasibility for student's application
- Quick think-pair-share

**Wrap-up [92-93 min]:**
- Module 4 complete: Combustion is where fuel energy converts to work
- Module 4 SLP assigned: Combustion optimization (due before Session 11)
- Next: Emissions - the constraint that defines everything

**Materials:** P-V diagrams for various cycles, HCCI combustion videos, VCR mechanism videos

**Delivery Notes:**
- Advanced combustion modes are future-looking - manage expectations
- Atkinson/Miller is practical (hybrids use it) - emphasize this success story
- HCCI control problem is fundamental physics/chemistry - not just engineering

---

## MODULE 5: EMISSIONS CONTROL

### SESSION 11: Emission Formation Mechanisms (90 min)

**Learning Outcomes:** SO-5-11-1, SO-5-11-2, SO-5-11-3, SO-5-11-4

**Hook [0-5 min]:**
- "Emissions regulations define modern engine design. Everything we've learned is constrained by: NOx, PM, CO, HC."
- Show emissions limits progression: Euro 1 → Euro 7 (dramatic tightening)

**Part 1: NOx Formation [5-30 min]:**
- Thermal NOx (Zeldovich mechanism)
- High temperature + oxygen → NOx
- Formation factors, mitigation strategies
- **MCQ #1 [30-32 min]:** NOx formation mechanism (Q5-11-1)

**Part 2: CO Formation [32-47 min]:**
- Incomplete combustion, insufficient O2 or time
- Rich mixture, quench, poor mixing
- **MCQ #2 [47-49 min]:** CO formation (Q5-11-2)

**Part 3: HC Formation [49-64 min]:**
- Crevice volumes (primary source in SI)
- Quench layers, oil films, misfires
- SI vs CI HC sources

**Part 4: PM/Soot Formation [64-84 min]:**
- Fuel-rich zones, nucleation, growth, oxidation
- Net PM = formation - oxidation
- Better mixing → less PM
- **MCQ #3 [84-86 min]:** Diesel PM formation (Q5-11-3)

**Part 5: NOx-PM Trade-off [86-89 min]:**
- Why trade-off exists
- In-cylinder can't solve alone → need after-treatment

**Exercise [89-92 min]:**
- Given operating condition, identify which pollutant will be highest
- Propose in-cylinder reduction strategy

**Wrap-up:**
- Formation mechanisms understood → now we control them (Session 12-13)

**Materials:** Chemical equations (simplified), formation zone diagrams, emission trends over time

**Delivery Notes:**
- Chemistry light - focus on conditions that promote formation
- NOx-PM trade-off is critical - will come up again in Session 12
- Connect formation to after-treatment needs

---

### SESSION 12: After-Treatment Systems (90 min)

**Learning Outcomes:** SO-5-12-1, SO-5-12-2, SO-5-12-3, SO-5-12-4, SO-5-12-5

**Hook [0-5 min]:**
- "In-cylinder optimization isn't enough. We need after-treatment to meet regulations."
- Show modern diesel after-treatment system (DOC-DPF-SCR assembly)

**Part 1: Three-Way Catalyst (SI) [5-25 min]:**
- TWC reactions: NOx reduction, CO/HC oxidation
- Stoichiometric operation requirement (λ=1)
- Light-off temperature, catalyst efficiency vs λ
- Cold-start challenge
- **MCQ #1 [25-27 min]:** TWC operation (Q5-12-1)

**Part 2: Diesel After-Treatment System Design [27-62 min]:**
- **DOC (8 min):** Oxidizes CO, HC, NO→NO2
- **DPF (15 min):** Traps PM, regeneration (passive/active/forced), soot/ash, backpressure
- **SCR (12 min):** NOx reduction using urea/ammonia, catalyst types, efficiency, low-temp challenge
- **MCQ #2 [62-64 min]:** DPF regeneration purpose (Q5-12-2)
- **MCQ #3 [64-66 min]:** SCR urea function (Q5-12-3)

**Part 3: System Integration [66-81 min]:**
- DOC→DPF→SCR sequence
- SCR-on-filter (integrated)
- Thermal management for low-temp operation
- After-treatment technology comparison

**Exercise [81-88 min]:**
- Design after-treatment for diesel engine to meet Euro 6d
- Students specify: DOC, DPF (substrate, regen strategy), SCR (type, location)

**Wrap-up [88-90 min]:**
- After-treatment enables compliance
- Next: Regulations, OBD, diagnostics

**Materials:** After-treatment cutaways, regeneration temperature curves, SCR efficiency vs temp

**Delivery Notes:**
- DPF regeneration is practical concern - students will face this
- SCR urea consumption is operating cost - emphasize
- System integration: Temperature management is key

---

### SESSION 13: Regulations, Compliance, OBD & Diagnostics (90 min)

**Learning Outcomes:** SO-5-13-1, SO-5-13-2, SO-5-13-3, SO-5-13-4, SO-5-13-5

**Hook [0-5 min]:**
- "Regulations drive billions in R&D. OBD ensures compliance in real-world. Diagnostics is where you troubleshoot."
- Show RDE testing video (PEMS on vehicle)

**Part 1: Global Emission Regulations [5-30 min]:**
- Euro 6/7, EPA Tier 3, BS-VI, China 6
- Emission limits comparison
- Test cycles: NEDC, WLTP, RDE
- Real Driving Emissions importance
- **MCQ #1 [30-32 min]:** RDE testing purpose (Q5-13-1)

**Part 2: OBD-II Systems [32-57 min]:**
- Purpose: Monitor emission systems, ensure compliance
- Architecture: Monitors, readiness, malfunction thresholds
- MIL illumination logic
- Freeze frame, DTCs
- **MCQ #2 [57-59 min]:** MIL illumination criteria (Q5-13-2)

**Part 3: Diagnostic Process [59-84 min]:**
- DTCs: What they mean (circuit fault, not necessarily component)
- Scan tool data: Live data, freeze frame, readiness monitors
- Diagnostic workflow: DTC → possible causes → tests → root cause → repair
- **Case study:** P0420 (Catalyst efficiency low) - multiple possible causes
- **MCQ #3 [84-86 min]:** DTC function (Q5-13-3)

**Part 4: Emission Diagnostic Examples [86-89 min]:**
- O2 sensor fault diagnosis
- DPF regeneration failure
- SCR NOx sensor fault

**Exercise [89-92 min]:**
- Given DTC P0171 (System too lean Bank 1)
- Students list possible causes
- Describe diagnostic tests

**Wrap-up [92-93 min]:**
- Module 5 complete: Emissions form → after-treatment controls → regulations enforce → diagnostics troubleshoot
- Module 5 SLP assigned: Emissions compliance strategy (due before Session 14)
- Next module: Future technologies

**Materials:** Emission regulation comparison table, OBD-II scan tool screenshots, diagnostic flow charts

**Delivery Notes:**
- Regulations are dry - keep it practical (cost, compliance challenges)
- OBD-II diagnostics is where students engage - use real DTCs
- Emphasize: DTC ≠ failed part, it's a starting point

---

## MODULE 6: ADVANCED TECHNOLOGIES & FUTURE

### SESSION 14: Alternate Fuels & Energy Transition (90 min)

**Learning Outcomes:** SO-6-14-1, SO-6-14-2, SO-6-14-3, SO-6-14-4

**Hook [0-5 min]:**
- "IC engines face existential challenge: Electrification. But IC isn't dead. Alternate fuels, e-fuels, hybrid. What's the future?"
- Show slide: IC engines in 2050 - where will they remain?

**Part 1: Alternate Fuel Properties [5-35 min]:**
- CNG, hydrogen, ethanol, biodiesel
- Combustion characteristics, octane/cetane, energy density
- Engine modifications needed
- **MCQ #1 [35-37 min]:** Hydrogen combustion characteristics (Q6-14-1)

**Part 2: Fuel Lifecycle Analysis [37-62 min]:**
- Well-to-wheel emissions
- CNG: Extraction emissions
- Hydrogen: Green vs grey
- E-fuels: Carbon-neutral if renewable energy + captured CO2
- **MCQ #2 [62-64 min]:** E85 octane benefit (Q6-14-2)

**Part 3: IC Engines in Future Mobility [64-84 min]:**
- Where IC persists: Long-haul, aviation, off-highway
- Hybridization strategies
- Synthetic fuels for carbon neutrality
- **MCQ #3 [84-86 min]:** IC engine future applications (Q6-14-3)

**Exercise [86-90 min]:**
- Assess alternate fuel for student's application
- Quick evaluation: Technical, economic, infrastructure

**Wrap-up:**
- IC engines will evolve, not disappear
- Next session: Efficiency technologies, then final SLP

**Materials:** Fuel property comparison table, well-to-wheel diagrams, hydrogen infrastructure photos

**Delivery Notes:**
- Avoid hype or doom - balanced, data-driven discussion
- Hydrogen enthusiasm is high - manage expectations (storage, production challenges)
- Carbon-neutral fuels are bridge to future - realistic option

---

### SESSION 15: Thermal Management, Friction Reduction & System Integration (90 min)

**Learning Outcomes:** SO-6-15-1, SO-6-15-2, SO-6-15-3, SO-6-15-4

**Hook [0-5 min]:**
- "We've covered engine fundamentals, performance, air/fuel, combustion, emissions, future fuels. Now: How do we squeeze out every last percent of efficiency?"
- Show efficiency breakdown pie chart: 40% useful work, 30% coolant, 30% exhaust - "Can we recover the 60% waste?"

**Part 1: Heat Transfer & Thermal Management [5-30 min]:**
- Heat transfer mechanisms: Conduction, convection, radiation
- Where heat is lost: Coolant, exhaust, oil, radiation
- Strategies to reduce heat loss: Insulated combustion chamber, thermal barrier coatings
- **MCQ #1 [30-32 min]:** Waste heat recovery (Q6-15-1)

**Part 2: Friction Reduction [32-57 min]:**
- Friction sources: Piston/rings, bearings, valvetrain, accessories
- Friction increases with speed²
- Reduction strategies: Low-viscosity oils, coatings, roller followers, reduced tension rings
- Trade-offs: Adequate lubrication vs friction
- **MCQ #2 [57-59 min]:** Low-viscosity oil trade-off (Q6-15-2)

**Part 3: Waste Heat Recovery Technologies [59-79 min]:**
- **Turbocompound:** Extract work from exhaust after turbo
- **ORC (Organic Rankine Cycle):** Use exhaust heat to drive secondary power cycle
- **TEG (Thermoelectric Generator):** Convert heat to electricity
- Efficiency gains: 3-5% for turbocompound, 2-4% for ORC
- Cost-benefit: Best for steady-state, high-utilization applications (long-haul trucks)

**Part 4: System Integration & Downsizing [79-84 min]:**
- **Engine downsizing:** Smaller displacement + turbo = better part-load efficiency
- **Hybridization:** IC engine operates at optimal efficiency, electric fills gaps
- **Cylinder deactivation, start-stop, sailing**
- **Multiple technologies combined:** Downsizing + direct injection + VVT + turbo + mild hybrid
- **MCQ #3 [84-86 min]:** Downsizing strategy (Q6-15-3)

**Part 5: Course Synthesis [86-91 min]:**
- **Journey recap (5 min):**
  - Module 1: Designed engine architecture and breathing
  - Module 2: Analyzed performance and calibration
  - Module 3: Optimized air/fuel delivery
  - Module 4: Mastered combustion processes
  - Module 5: Controlled emissions
  - Module 6: Explored future technologies
- **Key takeaway:** IC engine design is a multi-objective optimization problem constrained by physics, chemistry, economics, and regulations
- **Where to go from here:**
  - Specialized courses: Combustion modeling, after-treatment design, hybrid powertrains
  - Industry certifications
  - Continuous learning (SAE papers, conferences)

**Course Wrap-up & Final Assignment [91-93 min]:**
- **Module 6 SLP assigned:** Future powertrain technology assessment (due end of course, 2 weeks)
  - This is the capstone: Comprehensive technology evaluation for organization
  - Expect 10-12 page report + presentation (if scheduled)
- **Course evaluation:** Encourage honest feedback for improvement
- **Final words:** "You now have the tools to design, optimize, diagnose, and future-proof IC engines. Go apply this knowledge to make real-world impact."

**Materials:** Efficiency breakdown charts, friction Stribeck curves, waste heat recovery system diagrams, downsizing performance comparisons

**Delivery Notes:**
- Last session - balance technical content with synthesis and inspiration
- Efficiency improvements are incremental - set realistic expectations
- System thinking: Integration of multiple technologies is more powerful than any single technology
- End on optimistic note: IC engines have a future if designed sustainably

---

## INSTRUCTOR CUSTOMIZATION GUIDE

### Adapting Templates to Your Context

**1. Industry Focus:**
- **Automotive:** Use passenger car examples, WLTP/RDE testing, Euro/EPA regulations
- **Heavy-Duty Trucking:** Long-haul diesel examples, BS-VI/EPA regulations, TCO emphasis
- **Power Generation:** Stationary engine examples, emissions compliance, efficiency optimization
- **Off-Highway:** Construction/agricultural equipment, durability, fuel flexibility
- **Marine:** Large diesel engines, IMO regulations, fuel oil properties

**2. Time Adjustments:**
- Sessions run long? Trim:
  - Reduce MCQ discussion time (but keep MCQs)
  - Shorten exercises or make them homework
  - Move some content to supplementary readings
- Sessions run short? Expand:
  - Add more worked examples
  - Include additional case studies
  - Extend exercise time for deeper exploration

**3. Assessment Modifications:**
- **If institutional requirements include final exam:**
  - Reduce SLP weight
  - Use MCQs for exam questions (expand bank)
  - Add comprehensive problems
- **If no SLPs feasible (students lack workplace access):**
  - Provide detailed case study scenarios
  - Use industry examples as SLP substitutes
  - Group projects instead of individual

**4. Guest Speakers & Lab Sessions:**
- **Guest speakers from industry (optional):**
  - Session 4: Calibration engineer
  - Session 9: Diesel engine engineer
  - Session 12: After-treatment engineer
  - Session 14: Alternative fuels researcher
- **Lab sessions (if available):**
  - Engine dyno demonstration (performance testing)
  - Teardown session (physical components)
  - OBD-II diagnostic workshop
  - Emission analyzer demonstration

**5. Supplementary Resources:**
- **Textbook alignment:** If using Heywood, Pulkrabek, or Stone, align session readings
- **SAE papers:** Assign 1-2 papers per module for advanced students
- **Videos:** Collect YouTube videos for each topic (combustion, turbo operation, etc.)
- **Simulations:** If GT-Power or WAVE available, demo and assign exercises

---

## DELIVERY CHECKLIST (Per Session)

### Before Class:
- [ ] Review session template and content outline
- [ ] Prepare slides with visuals, diagrams, videos
- [ ] Load MCQs into delivery system (polls, slides, etc.)
- [ ] Prepare worked example calculations
- [ ] Set up exercise materials (worksheets if needed)
- [ ] Test videos and animations
- [ ] Bring physical props (if using)
- [ ] Review previous session's minute papers (if collected)

### During Class:
- [ ] Start with hook - capture attention immediately
- [ ] State learning objectives clearly
- [ ] Activate prior knowledge (recall session)
- [ ] Deliver content in ~15 min chunks
- [ ] Use MCQs after each major part
- [ ] Discuss wrong answers (address misconceptions)
- [ ] Run interactive exercise
- [ ] Debrief exercise with students
- [ ] Summarize key takeaways
- [ ] Preview next session
- [ ] Remind about assignments (SLP due dates)

### After Class:
- [ ] Review MCQ responses (any patterns? Common errors?)
- [ ] Read minute papers or exit tickets (if collected)
- [ ] Note what worked well / what to adjust
- [ ] Prepare for next session based on student performance
- [ ] Grade or review SLP submissions (if due)
- [ ] Post slides or supplementary materials to LMS

---

## COMMON STUDENT QUESTIONS & SUGGESTED RESPONSES

### Technical Questions:

**Q: "Why can't we just use higher compression ratios to get better efficiency?"**
A: Great question. Higher CR does improve efficiency (Otto cycle equation), BUT we hit limits:
- **SI engines:** Knock. Higher CR → higher temperature and pressure → end-gas auto-ignites before flame arrives → engine damage. Limited by fuel octane.
- **CI engines:** Mechanical stress. Also, modern CI engines use lower CR (16-18) than older diesels (22+) because better fuel injection (high pressure, multiple injections) allows adequate ignition even with moderate CR.
- **Future:** Variable CR technology can optimize: High CR at light load (efficiency), lower CR at high load (avoid knock, allow more boost).

**Q: "If diesels are more efficient, why do we still use gasoline engines?"**
A: Diesel advantages: Higher CR, no throttling, leaner operation → 20-30% better fuel economy than equivalent gasoline.
But trade-offs:
- **Cost:** Diesel engines more expensive (higher strength, complex fuel injection, extensive after-treatment)
- **Emissions:** NOx and PM require DPF+SCR, adding cost and complexity
- **Power density:** Diesels limited in RPM (long stroke, high stress) → lower specific power
- **NVH:** Diesel combustion noisier, vibration higher
- **Application match:** Gasoline suits passenger cars (cost, refinement). Diesel suits trucks/off-highway (efficiency, torque, durability).

**Q: "Will electric vehicles kill IC engines?"**
A: EVs will dominate light-duty passenger vehicles in many markets. But IC engines persist where:
- **Long range needed:** Heavy-duty trucking, long-haul transport
- **High utilization:** Commercial vehicles where downtime for charging is costly
- **Remote locations:** Infrastructure doesn't support charging
- **Aviation, marine, off-highway:** Battery energy density insufficient
- **Carbon-neutral pathways:** E-fuels or biofuels with IC engines can be carbon-neutral if done right
IC engines won't disappear but will evolve and occupy niches where they offer advantages.

**Q: "What's the most important efficiency improvement technology?"**
A: No single "silver bullet." Modern high-efficiency engines integrate MANY technologies:
1. **Turbocharging + downsizing:** 15-20% fuel economy improvement
2. **Direct injection:** Enables higher CR and lean/stratified operation → 5-10%
3. **Variable valve timing:** Optimizes across operating range → 3-8%
4. **Friction reduction:** Low-viscosity oils, coatings → 2-5%
5. **Thermal management:** Waste heat recovery (ORC, turbocompound) → 3-5%
6. **Hybridization:** Operate IC engine at optimal efficiency points → 20-40% in real-world driving
The key: **System integration.** Combining these technologies compounds benefits.

### Pedagogical Questions:

**Q: "Do we need to memorize all these formulas?"**
A: Emphasis on understanding concepts and how to apply formulas, not rote memorization. For assessments:
- MCQs: Concepts and interpretation, not complex calculations
- SLPs: Formulas provided or you look them up (like real engineering)
- Key formulas to internalize (because you'll use them often):
  - Power = Torque × RPM / 9549
  - BMEP calculation
  - Displacement = π/4 × bore² × stroke × cylinders
  - VE definition
  - Efficiency = Output / Input

**Q: "How much detail do we need in SLP reports?"**
A: Focus on **quality of reasoning** more than length. A good SLP report includes:
- Clear problem statement
- Sufficient data/context to understand the situation
- Technical analysis using course concepts
- Calculations shown (doesn't have to be perfect, but show your thinking)
- Trade-off analysis (this is critical - engineering is about trade-offs)
- Realistic solution with justification
Rubrics weight analysis and reasoning (60-70%) more than just getting "right answer."

**Q: "I don't work with engines. Can I still do the SLPs?"**
A: Yes! Options:
1. Use a hypothetical scenario from your target industry
2. Choose a case study provided by instructor
3. Research a real-world engine/application and use that as your context
4. Team up with classmate who has engine access (if allowed)
The goal is to apply concepts to realistic problems, not necessarily YOUR personal workplace.

---

## CONTINUOUS IMPROVEMENT

### Collecting Feedback:
- **Minute papers:** End of session, 2-minute reflection
- **Mid-module surveys:** After Module 3, brief survey on pacing and difficulty
- **Course evaluation:** Standard institutional evaluation
- **SLP quality analysis:** Are students applying concepts correctly? Where are gaps?
- **MCQ performance patterns:** Which concepts need more time or different explanation?

### Iterating for Next Offering:
- **Content adjustments:** Add/remove topics based on student interest and time
- **Example updates:** Replace outdated examples with current industry cases
- **MCQ refinement:** Replace ambiguous questions, add new ones where students struggled
- **SLP rubric tuning:** Adjust weights based on what you want to emphasize
- **Technology integration:** Try new tools (simulations, better polling, videos)

---

**Document Control:**
Version: 1.0
Created: January 2026
Author: Course Design System
Status: Ready for Instructor Delivery

**Next Steps for Instructors:**
1. Review all 15 session templates above
2. Customize examples to your industry context
3. Develop slides using content outlines
4. Prepare MCQs for delivery (poll system or slides)
5. Gather videos, animations, and props
6. Set up LMS with SLP assignments and due dates
7. Conduct first session and collect feedback
8. Iterate based on student performance and engagement
