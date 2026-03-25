# MCQ Assessment Bank
## AE ZG516: Advances in IC Engines

**Purpose:** Formative assessment to reinforce learning and check understanding
**Usage:** 2-3 questions embedded throughout each 90-minute lecture
**Total Questions:** 45 MCQs (3 per session × 15 sessions)
**Format:** Multiple choice with single correct answer
**Delivery:** Present after relevant content parts, not all at end

---

## MODULE 1: ENGINE FOUNDATIONS (Sessions 1-2)

### SESSION 1: Build Your Engine - Architecture, Power & Thermodynamics

**Q1-1-1: Engine Configuration Selection**
A delivery truck needs strong low-speed pulling power for urban deliveries and highway hauling. Which characteristic is MOST important?

A) High peak power at 6000 RPM
B) High torque at 1500-2500 RPM ✓
C) High compression ratio
D) Oversquare bore/stroke ratio

**Answer: B**
**Explanation:** Delivery trucks operate primarily at low-medium engine speeds (1500-2500 RPM) and need strong pulling power for loads and grades. Torque at this RPM range directly translates to pulling capability. High-RPM power (A) is irrelevant for truck operations. While high compression ratio (C) helps efficiency, it doesn't specifically address low-speed torque needs. Oversquare designs (D) favor high-RPM operation, opposite of truck requirements.

**Bloom Level:** Analyze
**Learning Outcome:** SO-1-1-1 (Analyze engine architecture choices and their impact on performance)

---

**Q1-1-2: Compression Ratio Effects**
If you increase compression ratio from 10:1 to 12:1 in an SI engine (ignoring knock limitations), thermal efficiency will:

A) Decrease
B) Stay the same
C) Increase ✓
D) Depend only on fuel type

**Answer: C**
**Explanation:** Otto cycle efficiency η = 1 - (1/CR^(γ-1)). As compression ratio (CR) increases, the denominator becomes larger, making the subtracted term smaller, thus efficiency increases. Higher CR extracts more work from the same fuel energy. The caveat "ignoring knock" is important because real SI engines are knock-limited. Fuel type (D) affects knock tendency but doesn't change the thermodynamic relationship.

**Bloom Level:** Apply
**Learning Outcome:** SO-1-1-3 (Apply thermodynamic cycle principles to explain CR effects)

---

**Q1-1-3: Displacement Calculation**
An engine has 86mm bore, 86mm stroke, and 4 cylinders. Its displacement is approximately:

A) 1.0 liter
B) 2.0 liters ✓
C) 2.5 liters
D) 3.0 liters

**Answer: B**
**Explanation:** Displacement V_d = (π/4) × bore² × stroke × cylinders
= (π/4) × (0.086m)² × 0.086m × 4
= 0.785 × 0.007396 × 0.086 × 4
= 0.001998 m³ ≈ 2.0 liters
This is a "square" engine (bore = stroke), typical of balanced designs. Such calculations are fundamental for engine sizing and comparison.

**Bloom Level:** Apply
**Learning Outcome:** SO-1-1-1 (Calculate and analyze engine architecture parameters)

---

### SESSION 2: Build Your Engine - Breathing & Control Systems

**Q1-2-1: Volumetric Efficiency Calculation**
If an engine has actual inducted air mass of 0.85 kg and theoretical air mass (based on displacement at atmospheric conditions) of 1.0 kg, what is volumetric efficiency?

A) 70%
B) 85% ✓
C) 100%
D) 115%

**Answer: B**
**Explanation:** VE = (Actual air mass) / (Theoretical air mass) × 100%
= (0.85 kg / 1.0 kg) × 100% = 85%
This is typical for a naturally aspirated engine with good breathing design. Values above 100% (D) are possible with forced induction or intake tuning effects. This metric directly affects power output since more air allows more fuel combustion.

**Bloom Level:** Apply
**Learning Outcome:** SO-1-2-2 (Calculate volumetric efficiency and evaluate factors affecting airflow)

---

**Q1-2-2: Closed-Loop Control**
Which sensor is CRITICAL for closed-loop air-fuel ratio control in a gasoline engine with a three-way catalyst?

A) Knock sensor
B) Mass airflow sensor
C) Oxygen sensor ✓
D) Throttle position sensor

**Answer: C**
**Explanation:** The oxygen (lambda) sensor in the exhaust measures actual AFR and provides feedback to the ECU, enabling closed-loop control to maintain stoichiometric ratio (λ=1) required for three-way catalyst efficiency. While MAF (B) measures airflow for feedforward control, only the O2 sensor provides the feedback necessary for closed-loop correction. Knock sensor (A) is for ignition timing protection. TPS (D) indicates driver demand but doesn't measure combustion results.

**Bloom Level:** Understand
**Learning Outcome:** SO-1-2-4 (Explain closed-loop control systems and their components)

---

**Q1-2-3: Valve Overlap Effects**
Increasing valve overlap (both intake and exhaust valves open near TDC) typically:

A) Improves low-speed torque
B) Increases HC emissions ✓
C) Reduces high-speed power
D) Decreases VE at high RPM

**Answer: B**
**Explanation:** Valve overlap allows some exhaust gas to flow back into the intake (internal EGR) and some fresh charge to escape directly to exhaust, especially at low RPM when flow velocities are low. This unburned fuel exiting directly to exhaust increases HC emissions. At high RPM (C, D), overlap actually helps scavenging and improves VE. It typically hurts low-speed torque (A) due to charge dilution. This is why VVT reduces overlap at low speeds and increases it at high speeds.

**Bloom Level:** Analyze
**Learning Outcome:** SO-1-2-1 (Analyze valve timing effects on engine breathing)

---

## MODULE 2: PERFORMANCE & CALIBRATION (Sessions 3-4)

### SESSION 3: Performance Analysis & Operating Characteristics

**Q2-3-1: Thermal Efficiency Interpretation**
A modern turbocharged diesel engine achieves 45% thermal efficiency at its best operating point. This means:

A) 45% of fuel energy is lost as heat
B) 45% of fuel energy is converted to useful work ✓
C) The engine is 55% efficient overall
D) Mechanical efficiency is 45%

**Answer: B**
**Explanation:** Thermal efficiency = (Brake power output) / (Fuel energy input rate). 45% efficiency means 45% of the fuel's chemical energy is converted to useful mechanical work at the crankshaft. The remaining 55% is lost as heat (exhaust, coolant, friction, radiation). This is excellent for a diesel engine - among the best achievable. Mechanical efficiency (D) is different: it's the ratio of brake to indicated power, typically 85-95%.

**Bloom Level:** Understand
**Learning Outcome:** SO-2-3-1 (Calculate and interpret thermal efficiency from performance data)

---

**Q2-3-2: Torque Curve Interpretation**
A diesel truck engine shows peak torque at 1400 RPM and peak power at 2200 RPM. This curve shape indicates:

A) Poor engine design
B) Optimized for low-speed pulling and drivability ✓
C) Better suited for racing applications
D) Requires higher compression ratio

**Answer: B**
**Explanation:** Peak torque at low RPM (1400) with a relatively flat torque curve is ideal for trucks: strong pulling power where the engine operates most (1000-2500 RPM), good drivability without constant shifting, excellent gradeability. Power peaks later as P = T × RPM. This is deliberate design (not poor, A), using long stroke, high CR, and appropriate turbo matching. Racing engines (C) have torque rising with RPM and peak at 6000+ RPM. The CR (D) is already optimized for diesel operation.

**Bloom Level:** Analyze
**Learning Outcome:** SO-2-3-2 (Interpret torque and power curves to identify engine characteristics)

---

**Q2-3-3: Spark Timing Effects**
Advancing spark timing too far beyond MBT (Maximum Brake Torque) timing in an SI engine causes:

A) Knock and potential engine damage ✓
B) Increased fuel economy
C) Lower exhaust gas temperature
D) Slower combustion rate

**Answer: A**
**Explanation:** Excessive spark advance causes combustion to occur too early, creating peak pressure well before TDC. This can trigger knock (uncontrolled auto-ignition of end-gas), causing extremely high pressure spikes that damage pistons, rings, and gaskets. It also produces less torque than MBT timing (not more economy, B). EGT may actually be higher or lower depending on how far beyond MBT. Combustion rate (D) isn't necessarily slower. MBT timing is the optimal balance; advancing beyond it enters the knock-limited region.

**Bloom Level:** Analyze
**Learning Outcome:** SO-2-3-3 (Analyze effects of spark timing on performance and durability)

---

### SESSION 4: Engine Calibration Strategies

**Q2-4-1: Rich Mixture at Full Load**
Why do SI engines typically run rich (λ < 1) at full load / wide-open throttle?

A) Better fuel economy
B) Component cooling and maximum power ✓
C) Lower emissions
D) Faster catalyst light-off

**Answer: B**
**Explanation:** At WOT, the engine operates at its thermal and mechanical limits. Enrichment (λ ≈ 0.90-0.95) provides: 1) Charge cooling from excess fuel evaporation, lowering combustion temperatures and protecting valves, pistons, and turbocharger; 2) Maximum power (slightly rich of stoichiometric produces peak power). This sacrifices fuel economy (A) and increases emissions (C) but is necessary for component protection. Catalyst light-off (D) uses retarded timing and slightly rich mixture, but that's a different operating condition (cold start).

**Bloom Level:** Understand
**Learning Outcome:** SO-2-4-1 (Apply fuel metering strategies for different operating conditions)

---

**Q2-4-2: Diesel Injection Timing Trade-off**
In a diesel engine, advancing main injection timing typically:

A) Increases NOx, decreases PM ✓
B) Decreases NOx, increases PM
C) Increases both NOx and PM
D) Decreases both NOx and PM

**Answer: A**
**Explanation:** This is the fundamental NOx-PM trade-off in diesels. Advancing injection → fuel burns earlier in cycle → higher peak combustion temperature → more thermal NOx formation. But it also → better fuel-air mixing time → more complete combustion → less PM (soot). Retarding injection does the opposite (B): lower peak temp (less NOx), but less mixing time (more PM). Modern after-treatment systems (SCR, DPF) allow optimization for efficiency while controlling both pollutants downstream.

**Bloom Level:** Analyze
**Learning Outcome:** SO-2-4-2 (Apply injection timing strategies and understand emissions trade-offs)

---

**Q2-4-3: Pilot Injection Purpose**
What is the primary purpose of pilot injection in modern common rail diesel engines?

A) Increase power output
B) Reduce combustion noise and pressure rise rate ✓
C) Regenerate the DPF
D) Improve cold start only

**Answer: B**
**Explanation:** Pilot injection (small fuel quantity 10-25° before main injection) pre-conditions the cylinder: raising temperature and pressure slightly. This shortens the ignition delay of the main injection, resulting in more gradual pressure rise ("soft" combustion) rather than abrupt bang. Benefits: quieter operation, reduced NVH, lower peak pressure (less mechanical stress), and slightly lower NOx. It doesn't significantly increase power (A) - that's the main injection's job. DPF regeneration (C) uses post-injection. While it helps at all conditions (D), it's not just for cold start.

**Bloom Level:** Understand
**Learning Outcome:** SO-2-4-2 (Apply multiple injection strategies in diesel calibration)

---

## MODULE 3: AIR & FUEL SYSTEMS (Sessions 5-7)

### SESSION 5: Air Intake, Exhaust & Boosting Systems

**Q3-5-1: Intake Runner Length Effect**
If an intake manifold has long, narrow runners, it is optimized for:

A) High RPM power
B) Low RPM torque ✓
C) Maximum VE at all engine speeds
D) Reduced emissions only

**Answer: B**
**Explanation:** Long runners create resonance tuning effects (pressure wave reflections) that arrive back at the intake valve at the right time for LOW RPM operation, improving cylinder filling and VE in that range. The downside: at high RPM, long narrow runners create excessive restriction, limiting flow and VE. Short, wide runners (A) favor high RPM flow. You cannot optimize for all speeds with fixed geometry (C), which is why variable-geometry intakes exist. Emissions (D) are not the primary driver of runner design.

**Bloom Level:** Analyze
**Learning Outcome:** SO-3-5-1 (Analyze factors affecting volumetric efficiency)

---

**Q3-5-2: Boost Pressure Calculation**
An engine operating at sea level (100 kPa atmospheric pressure) with 1.5 bar gauge boost has what absolute intake pressure?

A) 1.5 bar
B) 2.0 bar
C) 2.5 bar ✓
D) 150 kPa

**Answer: C**
**Explanation:** Absolute pressure = Atmospheric pressure + Gauge boost
= 1.0 bar + 1.5 bar = 2.5 bar absolute (or 250 kPa absolute)
Gauge pressure measures above atmospheric. Absolute pressure is referenced to vacuum. Engine calculations (compressor maps, density, etc.) use absolute pressure. This is a common error point: confusing gauge and absolute pressures. Answer D (150 kPa = 1.5 bar) is the gauge pressure, not absolute.

**Bloom Level:** Apply
**Learning Outcome:** SO-3-5-4 (Calculate pressure ratios and airflow requirements)

---

**Q3-5-3: Supercharger vs Turbocharger**
Compared to a turbocharger, a supercharger has:

A) Better fuel efficiency
B) Instant throttle response ✓
C) No parasitic losses
D) Higher peak boost capability

**Answer: B**
**Explanation:** Superchargers are mechanically driven by the crankshaft, so boost is immediate and proportional to engine speed - no lag. This gives instant throttle response, highly valued in performance applications. However, they consume engine power to drive them (parasitic loss, so C is wrong), reducing overall efficiency compared to turbos that recover waste exhaust energy (A is wrong). Peak boost (D) depends on design; turbos can achieve very high boost with appropriate matching. Trade-off: Response vs efficiency.

**Bloom Level:** Evaluate
**Learning Outcome:** SO-3-5-3 (Compare boosting technologies and select for applications)

---

### SESSION 6: Fuel Injection Systems & Mixture Formation

**Q3-6-1: GDI Stratified Mode Benefit**
Gasoline Direct Injection (GDI) in stratified lean mode (late injection, lean overall mixture):

A) Increases fuel consumption
B) Improves part-load efficiency ✓
C) Eliminates knock completely
D) Reduces particulate matter emissions

**Answer: B**
**Explanation:** Stratified operation injects fuel late in compression, creating a rich cloud near the spark plug while the rest of the cylinder contains air. Global λ can be 1.5-2.0 (lean), reducing fuel consumption and improving part-load efficiency by reducing throttling losses. However, this mode increases PM emissions (not D) due to fuel-rich zones and incomplete mixing, requiring GPF. It doesn't eliminate knock (C) though the charge cooling helps. This is only used at light load where efficiency matters most.

**Bloom Level:** Evaluate
**Learning Outcome:** SO-3-6-1 (Evaluate fuel injection technologies and their advantages)

---

**Q3-6-2: Common Rail High Pressure Purpose**
Modern common rail diesel systems use injection pressures of 1500-2500 bar primarily to:

A) Increase power output directly
B) Improve fuel atomization and reduce PM ✓
C) Reduce injection system cost
D) Increase fuel economy directly

**Answer: B**
**Explanation:** High injection pressure forces fuel through tiny nozzle holes at extreme velocity, creating fine atomization (smaller droplet size). Smaller droplets → faster evaporation → better mixing with air → less fuel-rich zones → dramatically reduced PM formation. This is the primary driver. It enables higher power (A) indirectly by allowing more fuel to be burned completely, but that's secondary. Cost (C) actually increases (high-pressure pumps, robust injectors). Fuel economy (D) improves slightly but mainly through emissions compliance allowing better calibration.

**Bloom Level:** Understand
**Learning Outcome:** SO-3-6-3 (Analyze multiple injection strategies and their effects)

---

**Q3-6-3: Lambda Definition**
An SI engine operates at λ = 0.90. This means:

A) The mixture is 90% stoichiometric
B) The mixture is lean
C) The mixture is rich ✓
D) 90% combustion efficiency

**Answer: C**
**Explanation:** λ (lambda) = (Actual AFR) / (Stoichiometric AFR)
- λ = 1.0: Stoichiometric (ideal ratio for complete combustion)
- λ < 1.0: Rich (excess fuel, less air than needed)
- λ > 1.0: Lean (excess air, more air than needed)
λ = 0.90 means 90% of stoichiometric AFR, or 10% excess fuel - a rich mixture used for WOT cooling and maximum power. It's not about efficiency (D) or percent stoichiometric (A).

**Bloom Level:** Understand
**Learning Outcome:** SO-3-6-2 (Calculate and interpret mixture ratios)

---

### SESSION 7: Charge Motion & In-Cylinder Flow Dynamics

**Q3-7-1: Swirl vs Tumble Application**
Which charge motion is most important for air-fuel mixing in direct injection diesel engines?

A) Tumble
B) Swirl ✓
C) Squish only
D) None - mixing is purely from high injection pressure

**Answer: B**
**Explanation:** Diesel engines rely on swirl (rotation around cylinder axis) to entrain air into the fuel spray jets. Fuel is injected into swirling air → spray breaks up and mixes → fast combustion, low PM. Swirl is generated by helical intake ports and matched with piston bowl geometry. Tumble (A) is preferred in SI engines for flame propagation. Squish (C) helps but isn't sufficient alone. High injection pressure (D) atomizes fuel, but swirl is essential for mixing that atomized fuel with the available air.

**Bloom Level:** Analyze
**Learning Outcome:** SO-3-7-1 (Differentiate between charge motion types and their applications)

---

**Q3-7-2: Tumble in SI Engines**
Tumble in SI engines breaks down into small-scale turbulence near TDC, which:

A) Slows down flame propagation
B) Increases flame speed and combustion efficiency ✓
C) Has no effect on combustion
D) Only reduces VE with no combustion benefit

**Answer: B**
**Explanation:** Tumble (end-over-end rotation) breaks down into intense small-scale turbulence as the piston approaches TDC. This turbulence "wrinkles" the flame front, dramatically increasing its surface area and propagation speed. Faster flame → shorter combustion duration → closer to constant-volume ideal → higher efficiency. It also enables lean burn and reduces cycle-to-cycle variation. The VE penalty (D) is real but acceptable given combustion benefits. Turbulence definitely increases flame speed (not slows, A).

**Bloom Level:** Analyze
**Learning Outcome:** SO-3-7-2 (Design charge motion strategies for SI engines)

---

**Q3-7-3: Crevice Volume Impact**
The piston ring pack crevice volume is a significant source of:

A) NOx emissions
B) CO emissions
C) HC emissions ✓
D) PM emissions

**Answer: C**
**Explanation:** During compression, unburned air-fuel mixture is pushed into crevices (especially top land above the top ring). During expansion, this mixture flows back out, but some HC remains trapped and exits as unburned hydrocarbons. Crevices account for 50%+ of engine-out HC emissions in SI engines. They don't significantly affect NOx (A) which forms at high temperatures in the main charge, or CO (B) which is from incomplete combustion, or PM (D) which is primarily a diesel/GDI issue related to fuel-rich zones.

**Bloom Level:** Understand
**Learning Outcome:** SO-3-7-4 (Identify unwanted flows and evaluate their impact)

---

## MODULE 4: COMBUSTION PROCESSES (Sessions 8-10)

### SESSION 8: Combustion in SI Engines

**Q4-8-1: SI Flame Propagation**
In a spark-ignition engine, the flame propagation process:

A) Occurs instantaneously throughout the chamber
B) Propagates as a flame front from spark plug outward ✓
C) Is initiated simultaneously at multiple locations
D) Starts at the cylinder wall and moves inward

**Answer: B**
**Explanation:** SI combustion begins with spark ignition at a single point (spark plug) and propagates as a turbulent flame front outward through the combustion chamber at 10-40 m/s (depending on mixture, turbulence, pressure). This sequential burning (not instantaneous, A) takes finite time (~40-60° crank angle), which is why ignition timing is advanced before TDC. Diesel combustion (C) has multiple ignition points. Starting from walls (D) would be abnormal (surface ignition/pre-ignition).

**Bloom Level:** Understand
**Learning Outcome:** SO-4-8-1 (Explain the SI combustion process including flame propagation)

---

**Q4-8-2: Engine Knock Mechanism**
Engine knock in SI engines is caused by:

A) Spark plug misfiring
B) Too low compression ratio
C) Auto-ignition of end-gas ahead of the flame front ✓
D) Excessive valve overlap

**Answer: C**
**Explanation:** Knock occurs when the unburned mixture ahead of the flame front ("end-gas") reaches its auto-ignition temperature and ignites spontaneously before the flame arrives. This creates extremely rapid, uncontrolled pressure rise (shock waves) - the "knock" sound. Knock is promoted by: high temperature, high pressure, long ignition delay (too much advance), low octane fuel, hot spots. It's not misfire (A), not from low CR (B - higher CR increases knock tendency), and overlap (D) doesn't directly cause knock.

**Bloom Level:** Analyze
**Learning Outcome:** SO-4-8-2 (Analyze engine knock and mitigation strategies)

---

**Q4-8-3: Octane Rating Function**
Higher octane fuel allows:

A) Higher engine RPM only
B) Higher compression ratio or boost without knock ✓
C) Lower fuel consumption directly
D) Faster flame propagation

**Answer: B**
**Explanation:** Octane rating measures fuel's resistance to auto-ignition (knock resistance). Higher octane fuels can withstand higher temperatures and pressures before auto-igniting. This allows: 1) Higher compression ratios (more efficiency), 2) Higher boost pressure (more power), 3) More advanced spark timing (better performance), all without knock. It doesn't directly affect RPM (A) - that's a mechanical design limit. Fuel economy (C) may improve if the engine can use higher CR or more optimal timing. Flame speed (D) is actually slightly slower for high-octane fuels.

**Bloom Level:** Evaluate
**Learning Outcome:** SO-4-8-3 (Evaluate relationship between octane, CR, and knock)

---

### SESSION 9: Combustion in CI Engines

**Q4-9-1: Diesel Combustion Phases**
The "ignition delay" phase in diesel combustion is:

A) The time for fuel to vaporize after injection
B) The period between start of injection and start of combustion ✓
C) The duration of the power stroke
D) Only important at cold temperatures

**Answer: B**
**Explanation:** Ignition delay is the time (or crank angle degrees) between SOI (start of injection) and SOC (start of combustion), during which fuel atomizes, vaporizes, mixes with air, and undergoes pre-combustion reactions until auto-ignition. Typical: 5-15° CA. Shorter delay → smoother combustion. Longer delay → more fuel injected before ignition → rapid premixed burn → combustion noise. Delay affected by: cetane number, temperature, pressure, EGR. It's critical at all conditions (not just cold, D), affecting noise, NOx, and combustion phasing.

**Bloom Level:** Understand
**Learning Outcome:** SO-4-9-1 (Explain the four phases of diesel combustion)

---

**Q4-9-2: NOx-PM Trade-off**
In diesel engines, the NOx-PM trade-off exists because:

A) Both increase with higher injection pressure
B) Conditions that reduce NOx (lower temp) tend to increase PM ✓
C) They are chemically identical pollutants
D) Modern engines have eliminated this trade-off

**Answer: B**
**Explanation:** NOx forms at high temperatures (>1800K) in oxygen-rich zones. PM (soot) forms in fuel-rich, oxygen-deficient zones. Strategies that reduce peak temperature (retarded timing, EGR) → lower NOx BUT worse mixing → more fuel-rich zones → more PM. Conversely, better mixing or advanced timing → less PM but higher NOx. Higher injection pressure (A) actually reduces both (better mixing, lower PM, plus lower temp combustion). They're different pollutants (C). Modern after-treatment (SCR + DPF) manages both downstream (D), allowing in-cylinder optimization for efficiency.

**Bloom Level:** Evaluate
**Learning Outcome:** SO-4-9-3 (Evaluate the NOx-PM trade-off)

---

**Q4-9-3: Fuel Spray Penetration**
If diesel injection pressure is increased from 1500 to 2000 bar, spray penetration:

A) Decreases significantly
B) Remains unchanged
C) Increases ✓
D) Depends only on nozzle hole size

**Answer: C**
**Explanation:** Higher injection pressure → higher spray velocity → greater momentum → longer spray penetration into the combustion chamber. This must be matched with chamber geometry: adequate penetration to utilize available air, but not so much that spray hits piston bowl walls (causing PM). Penetration is determined by: injection pressure, nozzle hole diameter, ambient density, and injection duration. Higher pressure also improves atomization (smaller droplets). Bowl design must account for expected penetration length. Nozzle size (D) affects penetration but pressure is equally important.

**Bloom Level:** Apply
**Learning Outcome:** SO-4-9-2 (Analyze fuel spray behavior)

---

### SESSION 10: Advanced Engine Cycles & Combustion Modes

**Q4-10-1: Atkinson vs Otto Cycle**
The Atkinson cycle achieves higher efficiency than Otto cycle by:

A) Using higher compression ratio
B) Having longer expansion stroke than compression stroke ✓
C) Operating at lower temperatures
D) Eliminating heat losses

**Answer: B**
**Explanation:** Atkinson cycle has expansion ratio > compression ratio, extracting more work from the same compressed charge. Implementation: late intake valve closing (LIVC) during compression stroke effectively reduces compression stroke length while expansion stroke remains full length. Benefits: Higher thermal efficiency (~15% more than equivalent Otto). Drawbacks: Lower power density, lower low-end torque. Ideal for hybrid vehicles (Prius) where engine operates at optimal efficiency points. It's not from higher CR (A) - CR is actually effectively lower. Temperature and heat loss effects (C, D) are secondary.

**Bloom Level:** Analyze
**Learning Outcome:** SO-4-10-2 (Analyze Atkinson/Miller cycle principles)

---

**Q4-10-2: HCCI Combustion Challenge**
The main challenge preventing widespread adoption of HCCI (Homogeneous Charge Compression Ignition) is:

A) Lower efficiency than conventional engines
B) Difficulty controlling combustion timing and load range ✓
C) Higher emissions than diesel engines
D) Excessive noise and vibration

**Answer: B**
**Explanation:** HCCI has no direct combustion initiation (no spark, no injection event). Ignition timing is controlled by chemical kinetics and in-cylinder conditions (temperature, pressure, mixture composition). This makes it very sensitive to operating conditions and difficult to control across wide RPM and load ranges. Load is limited (too low → misfire, too high → excessive pressure rise rate). Efficiency (A) is actually excellent. Emissions (C) show very low NOx and PM but higher HC/CO. NVH (D) can be managed with proper combustion phasing. Control remains the key barrier.

**Bloom Level:** Evaluate
**Learning Outcome:** SO-4-10-3 (Evaluate advanced combustion modes and their challenges)

---

**Q4-10-3: Variable Compression Ratio Benefit**
Variable compression ratio technology would allow an engine to:

A) Operate at optimal CR for different loads and fuels ✓
B) Eliminate the need for turbocharging
C) Run without a cooling system
D) Achieve unlimited power output

**Answer: A**
**Explanation:** VCR allows real-time adjustment: High CR (13-14:1) at light load for efficiency, lower CR (8-10:1) at high load to prevent knock and allow more boost. Also adapt to fuel quality (regular vs premium). Benefits: 15-20% efficiency improvement potential, better low-end torque, fuel flexibility. Complexity and cost have limited adoption (Infiniti VC-Turbo is production example). Turbocharging (B) is complementary, not replaced. Cooling (C) is always needed. Power (D) still limited by mechanical strength and thermal limits.

**Bloom Level:** Evaluate
**Learning Outcome:** SO-4-10-4 (Assess variable compression ratio technology)

---

## MODULE 5: EMISSIONS (Sessions 11-13)

### SESSION 11: Emission Formation Mechanisms

**Q5-11-1: NOx Formation Mechanism**
Thermal NOx (Zeldovich mechanism) formation is primarily dependent on:

A) Fuel sulfur content
B) High combustion temperature and oxygen availability ✓
C) Engine speed only
D) Particulate matter concentration

**Answer: B**
**Explanation:** Thermal NOx forms when N₂ and O₂ in air react at temperatures above ~1800K through the Zeldovich mechanism. Formation is exponentially dependent on temperature and requires oxygen. Conditions promoting NOx: High peak combustion temperature, lean mixtures (excess O₂), high pressure. Mitigation: EGR (lower O₂, lower temp), retarded timing (lower peak temp), rich operation (less O₂). Fuel sulfur (A) affects SOx, not NOx. Speed (C) affects time available but temperature is dominant. PM (D) is separate; NOx and PM have inverse relationship in diesels.

**Bloom Level:** Understand
**Learning Outcome:** SO-5-11-1 (Explain NOx formation mechanism)

---

**Q5-11-2: CO Formation**
Carbon monoxide (CO) emissions result from:

A) Excessive air in the mixture
B) Incomplete combustion due to insufficient oxygen or time ✓
C) High combustion temperatures
D) Sulfur in diesel fuel

**Answer: B**
**Explanation:** CO forms when fuel oxidation is incomplete: insufficient oxygen (rich mixture, locally rich zones), insufficient time (quench near cold walls, rapid expansion), or poor mixing. Complete oxidation: HC → CO → CO₂. If oxidation stops at CO → CO emission. Common in: Rich SI engines, cold start, transients, diesel locally rich zones. Excessive air (A) promotes complete combustion to CO₂. High temperature (C) actually helps oxidize CO to CO₂. Sulfur (D) creates SOx, not CO.

**Bloom Level:** Understand
**Learning Outcome:** SO-5-11-1 (Explain CO formation mechanism)

---

**Q5-11-3: Diesel PM Formation**
Particulate matter (soot) in diesel engines forms primarily in:

A) Oxygen-rich, high-temperature zones
B) Fuel-rich zones with insufficient oxygen ✓
C) The exhaust manifold during cooling
D) Evenly throughout the combustion chamber

**Answer: B**
**Explanation:** Soot formation requires fuel-rich conditions where carbon atoms from fuel molecules cluster together forming particles (nucleation → growth → agglomeration). This occurs in the core of diesel fuel sprays where local λ << 1. Soot oxidizes if it later encounters high temperature + oxygen (burnout phase). Net PM = soot formed - soot oxidized. Oxygen-rich zones (A) oxidize soot. Exhaust formation (C) is minor. Distribution (D) is very non-uniform in diesel, which is the challenge. Better mixing (high injection pressure, swirl) reduces fuel-rich zones → less PM.

**Bloom Level:** Understand
**Learning Outcome:** SO-5-11-1 (Explain PM formation and oxidation)

---

### SESSION 12: Exhaust Gas After-Treatment Systems

**Q5-12-1: Three-Way Catalyst Operation**
A Three-Way Catalyst (TWC) can simultaneously reduce NOx, CO, and HC ONLY when:

A) Operating at lean conditions (λ > 1)
B) Operating at stoichiometric conditions (λ ≈ 1) ✓
C) Operating at rich conditions (λ < 1)
D) Exhaust temperature exceeds 800°C

**Answer: B**
**Explanation:** TWC performs three reactions: 1) NOx reduction (needs reducing agents: CO, HC, H₂), 2) CO oxidation (needs O₂), 3) HC oxidation (needs O₂). At λ=1, there's just enough O₂ for oxidation and just enough CO/HC for NOx reduction, achieving >95% conversion of all three. Lean (A): excess O₂, cannot reduce NOx. Rich (C): insufficient O₂, cannot oxidize CO/HC. This is why SI engines with TWC must maintain tight λ=1 control via O2 sensor feedback. Temperature (D) must be adequate (>300°C light-off) but stoichiometric operation is the key requirement.

**Bloom Level:** Understand
**Learning Outcome:** SO-5-12-1 (Explain Three-Way Catalyst operation and requirements)

---

**Q5-12-2: DPF Regeneration Purpose**
The primary purpose of DPF (Diesel Particulate Filter) regeneration is to:

A) Reduce NOx emissions
B) Burn accumulated soot to prevent filter clogging ✓
C) Cool the exhaust gas
D) Improve fuel economy

**Answer: B**
**Explanation:** DPF traps PM (soot) with >95% efficiency, but accumulates over time. Regeneration burns the trapped soot (600-650°C) to prevent excessive backpressure and filter failure. Types: Passive (continuous, during normal high-temp operation), Active (periodic, using post-injection or fuel dosing to raise EGT), Forced (stationary, when passive/active insufficient). NOx (A) is handled by SCR, not DPF. Cooling (C) is incorrect - regeneration increases temperature. Fuel economy (D) is slightly reduced during active regeneration.

**Bloom Level:** Understand
**Learning Outcome:** SO-5-12-3 (Analyze DPF regeneration strategies)

---

**Q5-12-3: SCR System Function**
In an SCR (Selective Catalytic Reduction) system for diesel engines, urea (DEF/AdBlue) is injected to:

A) Improve fuel combustion
B) Reduce NOx by providing ammonia as reductant ✓
C) Regenerate the DPF
D) Neutralize sulfur in the fuel

**Answer: B**
**Explanation:** SCR uses aqueous urea solution (32.5% urea in water, called DEF or AdBlue) injected into hot exhaust. Urea thermally decomposes to ammonia (NH₃). Ammonia reacts with NOx over SCR catalyst to form N₂ + H₂O. Achieves 90-95% NOx reduction. This allows diesel engines to be calibrated for efficiency (which produces more NOx) while meeting regulations downstream. Doesn't affect combustion (A), doesn't regenerate DPF (C) - that's done by oxidation, and sulfur (D) is addressed by ultra-low sulfur diesel fuel.

**Bloom Level:** Understand
**Learning Outcome:** SO-5-12-4 (Evaluate SCR systems and NOx reduction efficiency)

---

### SESSION 13: Regulations, Compliance, OBD & Diagnostics

**Q5-13-1: Real Driving Emissions (RDE) Testing**
Real Driving Emissions (RDE) testing was introduced in regulations to:

A) Replace all laboratory emissions testing
B) Verify emissions performance under actual on-road conditions ✓
C) Reduce testing costs for manufacturers
D) Only test cold-start emissions

**Answer: B**
**Explanation:** RDE addresses the gap between laboratory test cycles (controlled, repeatable but not representative of real driving) and actual on-road emissions. Uses PEMS (Portable Emissions Measurement System) during real driving (various speeds, loads, temperatures, altitudes). Euro 6d and later require RDE compliance with conformity factors. Defeats the "defeat devices" that optimized only for test cycles. Lab testing (A) still required - RDE is supplementary. Cost (C) is actually higher. Tests full range of conditions (D), not just cold start.

**Bloom Level:** Analyze
**Learning Outcome:** SO-5-13-1 (Compare emission regulations and explain RDE testing)

---

**Q5-13-2: OBD-II MIL Illumination**
The OBD-II system illuminates the Malfunction Indicator Lamp (MIL/Check Engine Light) when:

A) Any sensor reading is outside normal range
B) Emissions exceed 1.5x certification limits (typically) ✓
C) Oil change is due
D) Only when catalyst is completely failed

**Answer: B**
**Explanation:** MIL illuminates when a fault is detected that causes emissions to exceed regulatory thresholds (typically 1.5x FTP limits for passenger cars). Not every sensor anomaly triggers MIL (A) - system uses rationality checks and impact assessment. Oil change (C) may trigger maintenance light, not MIL. Catalyst monitoring (D) triggers MIL when efficiency drops below threshold, not just complete failure. OBD-II also stores DTC (Diagnostic Trouble Code) and freeze-frame data for diagnosis. Two-trip logic prevents nuisance illumination.

**Bloom Level:** Understand
**Learning Outcome:** SO-5-13-2 (Explain OBD-II architecture and malfunction detection)

---

**Q5-13-3: Diagnostic Trouble Code (DTC) Function**
When diagnosing an emission-related fault, the DTC (Diagnostic Trouble Code):

A) Identifies the exact failed component requiring replacement
B) Indicates which circuit or system has exceeded thresholds ✓
C) Provides repair instructions
D) Can be ignored if the vehicle drives normally

**Answer: B**
**Explanation:** DTCs indicate which circuit, sensor, or system detected an out-of-range condition or exceeded malfunction threshold. Example: P0420 = "Catalyst System Efficiency Below Threshold Bank 1" - indicates catalyst monitoring detected low efficiency, but could be failed catalyst, O2 sensor fault, exhaust leak, or engine misfire damaging catalyst. Diagnostic process uses DTC as starting point, then tests components using scan tool data, sensor checks, and logic. DTCs don't give exact part (A) or repair steps (C). Should never be ignored (D) - emissions compliance and potential damage issues.

**Bloom Level:** Analyze
**Learning Outcome:** SO-5-13-3 (Diagnose emission system faults using diagnostic data)

---

## MODULE 6: ADVANCED TECHNOLOGIES (Sessions 14-15)

### SESSION 14: Alternate Fuels & Energy Transition

**Q6-14-1: Hydrogen as Engine Fuel**
Hydrogen used in IC engines offers:

A) Higher energy density than gasoline per unit volume
B) Zero carbon emissions but challenges with NOx ✓
C) Lower flame speed requiring advanced ignition timing
D) Easier storage than gasoline

**Answer: B**
**Explanation:** Hydrogen combustion produces zero CO₂, CO, HC, or PM (no carbon in fuel). However, combustion still involves air (N₂ + O₂) at high temperature → thermal NOx formation. Challenges: Very low energy density per volume (A wrong) requiring high-pressure (700 bar) or cryogenic storage (D wrong - much harder than gasoline). Extremely wide flammability limits, very high flame speed (C wrong - can pre-ignite), very low ignition energy. Can run lean for efficiency but NOx remains issue. Best suited for fuel cells, but IC engine use is possible.

**Bloom Level:** Evaluate
**Learning Outcome:** SO-6-14-1 (Evaluate properties and combustion characteristics of alternate fuels)

---

**Q6-14-2: E85 Fuel Characteristics**
E85 (85% ethanol, 15% gasoline) allows higher compression ratios than gasoline primarily because:

A) It has higher energy content
B) It has much higher octane rating (knock resistance) ✓
C) It burns at lower temperatures
D) It has lower emissions

**Answer: B**
**Explanation:** Ethanol has very high octane rating (~110 RON for E85 vs ~95 for premium gas), allowing CR of 13-14:1 without knock. Also has high heat of vaporization (charge cooling effect). Energy content (A) is actually lower (~66% of gasoline per volume, requiring ~30% more fuel for same power). Combustion temperature (C) is similar or slightly higher. Emissions (D) can be lower for some pollutants but that's not why higher CR is possible. Flex-fuel vehicles detect ethanol content and adjust timing and fueling accordingly.

**Bloom Level:** Evaluate
**Learning Outcome:** SO-6-14-2 (Assess engine modifications for alternate fuel operation)

---

**Q6-14-3: IC Engine Role in Future Mobility**
In future mobility scenarios with increasing electrification, IC engines are most likely to remain in:

A) All passenger vehicles indefinitely
B) Long-haul trucking, aviation, off-highway applications ✓
C) Urban delivery and taxi services
D) None - complete electrification is inevitable

**Answer: B**
**Explanation:** Battery energy density limitations make full electrification challenging for: long-haul heavy-duty (range, charging time, payload penalty), aviation (weight critical), off-highway/construction (remote locations, high-duty cycles). These applications likely to use: advanced diesel, hydrogen engines, e-fuels (synthetic fuels made with renewable energy), or hybrids. Urban passenger transport (C) is rapidly electrifying (shorter range, charging infrastructure). Complete electrification (D) faces physics and infrastructure barriers for certain applications. Long-term IC engines likely niche, high-value applications with carbon-neutral fuels.

**Bloom Level:** Analyze
**Learning Outcome:** SO-6-14-4 (Analyze role of IC engines in future mobility scenarios)

---

### SESSION 15: Thermal Management, Friction Reduction & System Integration

**Q6-15-1: Waste Heat Recovery Technology**
Turbocompound waste heat recovery improves engine efficiency by:

A) Reducing coolant heat rejection
B) Extracting additional work from exhaust gas energy ✓
C) Eliminating the need for a radiator
D) Increasing boost pressure

**Answer: B**
**Explanation:** Turbocompounding adds a power turbine downstream of the turbocharger turbine to extract energy from still-hot exhaust gas. This turbine mechanically (geared to crankshaft) or electrically (generator) returns power to the drivetrain, recovering 3-5% of fuel energy otherwise lost. Similar concept: ORC (Organic Rankine Cycle) using exhaust heat to drive secondary power cycle. Doesn't reduce coolant heat rejection (A) - that's a separate thermal path. Doesn't eliminate radiator (C). Doesn't affect boost (D) - that's upstream turbocharger's job. Best suited for steady-state high-load applications (long-haul trucks).

**Bloom Level:** Evaluate
**Learning Outcome:** SO-6-15-3 (Assess waste heat recovery technologies)

---

**Q6-15-2: Low-Viscosity Oil Trade-off**
Using lower-viscosity engine oil (e.g., 0W-20 instead of 10W-30) primarily:

A) Increases engine power at high RPM
B) Reduces friction losses especially during warm-up ✓
C) Improves heat transfer
D) Eliminates wear completely

**Answer: B**
**Explanation:** Lower viscosity reduces fluid friction losses in: bearings, piston rings, oil pump power. Benefits greatest during cold start and warm-up when oil is thickest. Can improve fuel economy 1-3%. Modern engines designed for low-viscosity oils with tighter tolerances, improved materials, reduced bearing clearances. Trade-offs: Adequate oil film thickness must be maintained to prevent wear - engineering balance. Doesn't significantly affect power at high RPM (A) - friction is relatively small compared to other losses. Heat transfer (C) slightly affected but not primary. Wear (D) still occurs but is minimized with proper design.

**Bloom Level:** Evaluate
**Learning Outcome:** SO-6-15-2 (Evaluate friction reduction strategies and trade-offs)

---

**Q6-15-3: Engine Downsizing Strategy**
Engine downsizing (smaller displacement with turbocharging) improves fuel economy by:

A) Reducing maximum power capability
B) Operating at higher load points with better efficiency during normal driving ✓
C) Eliminating the need for emissions equipment
D) Allowing lower quality fuel use

**Answer: B**
**Explanation:** Downsizing strategy: Replace large NA engine with smaller turbocharged engine of equal peak power. During normal driving (part load), smaller engine operates at higher load percentage → better thermal and mechanical efficiency (avoid low-load throttling losses and friction). Turbo provides power when needed (WOT). Net: 10-20% fuel economy improvement in real-world driving cycles. Peak power (A) is maintained, not reduced. Still needs emissions equipment (C) - often more complex. Fuel quality (D) may actually require higher octane for high specific output. Works best with efficient turbocharging, direct injection, variable valve timing.

**Bloom Level:** Analyze
**Learning Outcome:** SO-6-15-4 (Integrate multiple technologies for system-level efficiency)

---

## ASSESSMENT STATISTICS

**Total Questions:** 45 MCQs
**Distribution by Module:**
- Module 1 (Foundations): 6 questions
- Module 2 (Performance & Calibration): 6 questions
- Module 3 (Air & Fuel): 9 questions
- Module 4 (Combustion): 9 questions
- Module 5 (Emissions): 9 questions
- Module 6 (Advanced): 6 questions

**Bloom's Taxonomy Distribution:**
- Remember: 0 (0%)
- Understand: 16 (36%)
- Apply: 6 (13%)
- Analyze: 16 (36%)
- Evaluate: 7 (16%)
- Create: 0 (0%)

**Note:** Distribution emphasizes Understand and Analyze levels appropriate for M.Tech students learning complex technical material, with significant Evaluate component for engineering judgment.

---

## USAGE GUIDELINES FOR INSTRUCTORS

### Timing and Delivery
- **Embed throughout lecture:** Present MCQs immediately after covering the relevant content part
- **Not all at session end:** Avoids cognitive overload and provides immediate reinforcement
- **2-3 minutes per question:** Allow 60 seconds thinking time, 30-60 seconds discussion, 30 seconds explanation
- **Interactive format:** Use classroom response systems (clickers) or show-of-hands if available

### Pedagogical Notes
- **Formative, not summative:** Purpose is learning reinforcement, not grading
- **Encourage discussion:** After answering, ask students to explain why wrong answers are incorrect
- **Address misconceptions:** Wrong answer explanations reveal common errors - address explicitly
- **Just-in-time feedback:** Immediate correction is more effective than delayed

### Adaptation
- **Adjust difficulty:** If class struggles, add hint or simplify. If too easy, add complexity in discussion
- **Context modifications:** Adapt examples to local industry (automotive, power generation, marine)
- **Language:** Modify terminology if needed for international students
- **Supplementary questions:** Use wrong answer options as discussion prompts

---

**Document Control:**
Version: 1.0
Created: January 2026
Author: Course Design System
Status: Ready for Instructor Review
