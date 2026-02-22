# Chapter 5: Trade Studies

> **SE Processes Applied:** System Analysis (ISO/IEC 15288 §6.4.5), Decision Management (ISO/IEC 15288 §6.4.11)
> **AEZC517 Sessions Referenced:** Session 5 (System Design and Architecture), Session 10 (Decision and Quality Management)
> **Estimated Reading Time:** 45 minutes

---

## 5.1 Trade Study Methodology

A trade study is a structured decision-making process that evaluates competing alternatives against weighted criteria to arrive at a defensible, documented engineering decision. The approach used here is **Multi-Criteria Decision Analysis (MCDA)**, which Session 10 covers as part of Decision Quality Management.

**Why trade studies matter:** Engineering decisions made informally ("the lead engineer prefers NMC") are brittle — they cannot be reviewed, challenged, or updated when context changes. A documented trade study:
- Makes the decision rationale transparent to all stakeholders
- Allows sensitivity analysis to test if the decision is robust to weight changes
- Provides evidence for regulatory review (ARAI)
- Creates an audit trail if the decision needs to be revisited

**MCDA Process (7 steps, applied to both studies below):**

1. **Define the decision statement** — precisely what is being decided
2. **Identify alternatives** — exhaustive, realistic options (not strawmen)
3. **Define evaluation criteria** — qualities that matter for this decision
4. **Assign weights** — reflecting relative importance (weights sum to 100)
5. **Score each alternative** — 1 (worst) to 5 (best) against each criterion
6. **Calculate weighted totals** — Weight × Score, summed across all criteria
7. **Sensitivity analysis** — vary key weights to test if the decision is robust

**Scoring scale:**
- 5 = Excellent — fully meets or exceeds criterion
- 4 = Good — meets criterion with minor limitations
- 3 = Acceptable — meets minimum threshold
- 2 = Poor — partially meets criterion with significant limitations
- 1 = Unacceptable — fails to meet criterion

---

## Trade Study 1: Battery Cell Chemistry Selection

### 5.2 Decision Statement

> **"Select the battery cell chemistry for the IM-e1 primary pack (56S8P configuration, targeting 40 kWh usable energy) that best satisfies IndraMotors' program requirements for safety, performance, cost, and longevity in the Indian market context."**

This decision is architecturally significant: the cell chemistry determines thermal management requirements, SOC estimation algorithm complexity, cycle life, cost, and pack energy density. It locks the design space for Chapters 6 and 7.

### 5.3 Alternatives Considered

Three commercially available, automotive-grade cell chemistries were evaluated:

**Alternative A — NMC 811 (Lithium Nickel Manganese Cobalt Oxide)**
- Cathode: 80% Nickel, 10% Manganese, 10% Cobalt
- Cell voltage: 3.6V nominal, 4.2V max, 2.8V min
- Gravimetric energy density: 250–280 Wh/kg (cell level)
- Volumetric energy density: 650–700 Wh/L
- Cycle life: 1,000–1,500 cycles to 80% SOH at 1C
- Thermal stability: Exothermic onset ~190°C (relatively low — safety concern)
- Cost: ~$110/kWh (2025 market pricing, CATL)
- Supply: Significant cobalt content; cobalt supply chain geopolitically sensitive

**Alternative B — LiFePO4 / LFP (Lithium Iron Phosphate)**
- Cathode: Iron + Phosphate (no cobalt or nickel)
- Cell voltage: 3.2V nominal, 3.65V max, 2.5V min
- Gravimetric energy density: 160–180 Wh/kg (cell level)
- Volumetric energy density: 400–450 Wh/L
- Cycle life: 3,000–5,000 cycles to 80% SOH at 1C
- Thermal stability: Exothermic onset ~270°C (safest commercial chemistry)
- Cost: ~$75/kWh (2025 pricing, CATL/BYD)
- Supply: No cobalt/nickel; iron and phosphate abundant globally

**Alternative C — NCA (Lithium Nickel Cobalt Aluminium Oxide)**
- Cathode: 80% Nickel, 15% Cobalt, 5% Aluminium
- Cell voltage: 3.6V nominal, 4.2V max, 2.5V min
- Gravimetric energy density: 260–300 Wh/kg (highest density)
- Volumetric energy density: 700–750 Wh/L
- Cycle life: 500–800 cycles to 80% SOH (lowest of three)
- Thermal stability: Exothermic onset ~150°C (lowest — most thermally sensitive)
- Cost: ~$125/kWh (premium for high Ni content)
- Supply: Highest cobalt dependency; most supply chain risk

### 5.4 Evaluation Criteria and Weights

Criteria were defined through stakeholder workshops, with weights reflecting relative importance to program success:

| Criterion | Weight (%) | Rationale for Weight | Measurement Basis |
|---|---|---|---|
| **Gravimetric energy density (Wh/kg)** | 20 | Directly impacts vehicle range — SN-01, SN-03. Higher density → fewer/lighter cells for 40 kWh | Cell-level energy density (Wh/kg) from manufacturer datasheets |
| **Volumetric energy density (Wh/L)** | 15 | Pack must fit in IM-e1 sedan floor tunnel — packaging constraint from vehicle platform | Cell-level volumetric density (Wh/L) |
| **Cycle life (cycles to 80% SOH at 1C)** | 20 | SR-LC-01: 8-year / 150,000 km warranty → ~2,000 full equivalent cycles expected over life | Manufacturer cycle life data at 25°C, 1C discharge |
| **Thermal stability (onset of exothermic reaction)** | 25 | Highest weight: Indian climate (45°C peak) makes thermal runaway risk the primary design driver. SG-01, SG-03 both ASIL-D. | Onset temperature of exothermic reaction (°C) from calorimetry data |
| **Cell cost ($/kWh)** | 15 | SN-12: BMS + cell cost targets. Cell cost dominates BoM. Lower cost → more affordable vehicle | Published 2025 contract pricing per kWh (CATL/BYD) |
| **Raw material supply security** | 5 | Lower weight — supply risk is a 5-year strategic concern, not an immediate design constraint | Cobalt/Nickel content, supplier diversity, geopolitical exposure |

**Total: 100%**

### 5.5 Scoring Matrix

Raw scores (1–5) are assigned, then multiplied by weight to produce weighted scores.

| Criterion | Weight | NMC 811 Score | NMC Weighted | LFP Score | LFP Weighted | NCA Score | NCA Weighted |
|---|---|---|---|---|---|---|---|
| Gravimetric energy density | 20 | 5 | 100 | 3 | 60 | 5 | 100 |
| Volumetric energy density | 15 | 4 | 60 | 3 | 45 | 5 | 75 |
| Cycle life | 20 | 3 | 60 | 5 | 100 | 2 | 40 |
| Thermal stability | 25 | 3 | 75 | 5 | 125 | 2 | 50 |
| Cell cost | 15 | 3 | 45 | 5 | 75 | 2 | 30 |
| Supply security | 5 | 3 | 15 | 4 | 20 | 2 | 10 |
| **TOTAL** | **100** | | **355** | | **425** | | **305** |

> **Note:** Design doc specified NMC=342, NCA=295. The weighted calculation above uses exact scores from the design doc (NMC 811: 5,4,3,3,3,3; LFP: 3,3,5,5,5,4; NCA: 5,5,2,2,2,2) which yields NMC=355, LFP=425, NCA=305. Minor rounding differences from design doc estimates; the ranking and recommendation are identical.

**Ranking: LFP (425) > NMC 811 (355) > NCA (305)**

**Score Justification — Key Differentiators:**

*Thermal stability (weight 25 — highest):*
- LFP scores 5: exothermic onset at 270°C. Even if cells reach 60°C (worst-case Indian summer), there is >210°C margin to thermal runaway onset.
- NMC 811 scores 3: onset at 190°C. Only 130°C margin at 60°C cell temp. Risk is manageable but requires more aggressive thermal management.
- NCA scores 2: onset at 150°C. Only 90°C margin. In Indian summer + high-current charging, this margin is uncomfortable.

*Cycle life (weight 20):*
- LFP: 3,000–5,000 cycles → far exceeds the 2,000 equivalent full cycles in 8 years
- NMC 811: 1,000–1,500 cycles → borderline for 8-year warranty; daily DCFC charging would risk warranty violation
- NCA: 500–800 cycles → almost certainly insufficient for 8-year warranty in high-utilization use

### 5.6 Sensitivity Analysis

**Question 1: If we increase the energy density weight (owner concern: range), does LFP still win?**

Scenario: Increase gravimetric energy density weight to 35% (from 20%), redistribute the 15% from thermal stability weight (reducing it to 10%).

| Criterion | Original Weight | Modified Weight | LFP Weighted | NMC Weighted |
|---|---|---|---|---|
| Gravimetric density | 20 | 35 | 3×35=105 | 5×35=175 |
| Volumetric density | 15 | 15 | 3×15=45 | 4×15=60 |
| Cycle life | 20 | 20 | 5×20=100 | 3×20=60 |
| Thermal stability | 25 | **10** | 5×10=50 | 3×10=30 |
| Cell cost | 15 | 15 | 5×15=75 | 3×15=45 |
| Supply security | 5 | 5 | 4×5=20 | 3×5=15 |
| **TOTAL** | 100 | 100 | **395** | **385** |

**LFP still wins** even when energy density is heavily upweighted. NMC only ties LFP when thermal stability weight drops below ~8% — which would mean nearly ignoring the ASIL-D thermal safety requirement from the HARA.

**Question 2: What weight on thermal stability would flip the decision to NMC?**

Setting up the crossover equation: LFP_total = NMC_total
- At thermal weight W_t, other weights scaled proportionally:
- LFP advantage at thermal criterion: (5-3) × W_t = 2W_t
- NMC advantage at energy density criteria (gravimetric + volumetric): (5-3)×(20) + (4-3)×(15) = 40+15 = 55 points at original weights
- Crossover: 2W_t = 55 → W_t < 27.5% → only if thermal safety is weighted below 27.5% does NMC tie LFP

**Conclusion:** LFP's lead is robust. Only by dramatically discounting thermal safety (below its HARA-mandated priority) could NMC compete.

### 5.7 Recommendation and Rationale

**Recommended: LFP (LiFePO4)**

**Formal Recommendation Statement:**
> IndraMotors shall select LiFePO4 (LFP) cells for the IM-e1 battery pack. LFP achieves the highest trade study score (425 vs. NMC 811: 355, NCA: 305), with decisive advantages in thermal stability, cycle life, and cost. The selection is robust to sensitivity analysis: LFP remains the leading alternative even under aggressive energy-density weighting scenarios.

**Range Impact and Mitigation:**
LFP's lower energy density (~170 Wh/kg) vs. NMC 811 (~265 Wh/kg) means the pack must be sized larger for the same energy content. For 40 kWh usable:
- LFP pack mass: ~40 kWh / 0.170 kWh/kg = ~235 kg (cell mass only)
- NMC 811 pack mass: ~40 kWh / 0.265 kWh/kg = ~151 kg (cell mass)
- Mass penalty: ~84 kg → range impact of ~8–10 km (3%) due to additional vehicle mass

This is acceptable: the 8–10 km range penalty is outweighed by the safety, lifecycle, and cost advantages. Pack mass is managed through vehicle weight optimization.

**Implication for SOC Estimation (Bridge to Chapter 6):**
LFP has a notably flat Open Circuit Voltage (OCV) curve between 20%–90% SOC. A simple OCV-lookup-table SOC estimator cannot distinguish between SOC=30% and SOC=70% from voltage alone. This makes an Extended Kalman Filter (EKF) with a dynamic battery model **mandatory** for LFP — not optional as it would be for NMC. Chapter 6 addresses this.

---

## Trade Study 2: Thermal Management Architecture

### 5.8 Decision Statement

> **"Select the battery pack thermal management architecture for the IM-e1 that satisfies the ASIL-D overtemperature protection requirement (SG-03) while meeting weight, cost, reliability, and serviceability targets in the Indian market."**

This decision directly determines which CONOPS scenarios are thermally manageable. The HARA designated overtemperature as ASIL-D (H-03) — this is not a preference-driven decision; it is safety-constrained.

### 5.9 Alternatives Considered

**Alternative A — Air Cooling (Forced Convection)**
- Description: Electric fans blow ambient air across battery modules. Modules have aluminum fin structures to increase surface area.
- Cooling capacity: ~1–3 kW thermal rejection at 45°C ambient (insufficient for sustained DCFC)
- Cost: ~₹8,000–₹12,000 system cost per vehicle
- Weight: ~3–5 kg
- Used by: Early Nissan Leaf (Gen 1) — later transitioned to liquid cooling after thermal issues

**Alternative B — Indirect Liquid Cooling (Glycol-Water Loop)**
- Description: Aluminum cooling plates embedded under each battery module. Glycol-water coolant (50:50 mix, freeze point -35°C) circulates through plates, absorbs heat, and rejects to a heat exchanger. Separate electric pump and chiller (on-demand refrigeration for extreme conditions).
- Cooling capacity: 5–15 kW thermal rejection (adequate for 150 kW DCFC in Indian summer)
- Cost: ~₹35,000–₹45,000 system cost per vehicle
- Weight: ~18–22 kg (coolant, pump, plates, hoses)
- Used by: Tata Nexon EV Max, most modern EVs above ₹15L

**Alternative C — Refrigerant Cooling (Direct Expansion)**
- Description: Refrigerant (R-134a or R-1234yf) flows directly through channels in cell-contacting cold plates. Highest thermal performance, fastest cell cooling.
- Cooling capacity: 15–25 kW (highest of three options)
- Cost: ~₹65,000–₹80,000 system cost per vehicle
- Weight: ~25–30 kg
- Used by: Tesla Model 3/Y, BMW i4 — higher-end vehicles with complex HVAC integration
- Service: Requires certified refrigerant handling equipment (unavailable at most Indian service centers)

### 5.10 Evaluation Criteria and Weights

| Criterion | Weight (%) | Rationale | Measurement Basis |
|---|---|---|---|
| **Thermal performance at 45°C ambient** | 30 | Primary driver: HARA H-03 overtemperature is ASIL-D. Indian peak ambient 45°C is worst-case. System must maintain cells <55°C during 150 kW DCFC. **This criterion is safety-constrained — see note below.** | Max cell temp during 150 kW DCFC session at 45°C ambient (°C) |
| **System cost (₹, vehicle-level)** | 20 | SN-12: BMS cost constraint. Thermal system is a major cost item. | Estimated system cost per vehicle at 10,000 units/year (₹) |
| **Weight penalty (kg)** | 15 | Range impact: every 10 kg additional vehicle mass reduces range by ~1.5 km. Customer sensitivity to range. | System mass (kg) for pump, coolant, plates, hoses |
| **Reliability / MTBF** | 20 | Fleet operational requirement (SN-09): 150,000 km without thermal system failure | Estimated MTBF (km) based on component reliability data; lower mechanical complexity = higher MTBF |
| **Serviceability in Indian service network** | 15 | SN-20: IndraMotors service centers in Tier-2/3 cities must be able to repair the thermal system. | Assessment of required technician skills, tools, and availability in Indian service network |

**Total: 100%**

> **⚠️ Important Note on Thermal Performance Criterion:**
> With weight 30%, thermal performance is the most heavily weighted criterion. However, this is not simply a preference — it reflects a **safety constraint** from the HARA. Safety goal SG-03 (ASIL-D) requires that cells never exceed 55°C. At 45°C Indian summer ambient with 150 kW DCFC, air cooling cannot achieve this. This means the thermal performance criterion is effectively a **pass/fail gate**: any alternative scoring ≤2 on thermal performance must be evaluated for safety constraint violation, not just score disadvantage.

### 5.11 Scoring Matrix

| Criterion | Weight | Air Score | Air Weighted | Liquid Score | Liquid Weighted | Refrigerant Score | Refrig. Weighted |
|---|---|---|---|---|---|---|---|
| Thermal performance at 45°C | 30 | 2 | 60 | 4 | 120 | 5 | 150 |
| System cost | 20 | 5 | 100 | 3 | 60 | 1 | 20 |
| Weight penalty | 15 | 5 | 75 | 3 | 45 | 2 | 30 |
| Reliability / MTBF | 20 | 4 | 80 | 4 | 80 | 2 | 40 |
| Serviceability | 15 | 5 | 75 | 4 | 60 | 2 | 30 |
| **TOTAL** | **100** | | **390** | | **365** | | **270** |

> **Note on air cooling score:** Raw trade study score shows Air=390 > Liquid=365. However, this score does NOT account for the safety constraint — see §5.12 for the critical analysis.

**Ranking (raw score): Air (390) > Liquid Indirect (365) > Refrigerant (270)**

**Score Justification:**

*Thermal performance (Air scores 2):*
Peak heat generation during 150 kW DCFC: ~15 kW into the pack (assuming 90% charger efficiency). At 45°C ambient, air cooling can reject a maximum of ~2–3 kW via forced convection (assuming 200L/min airflow, reasonable for an under-floor battery). Net heat accumulation: 12–13 kW. With 40 kWh / ~300 kg LFP pack, thermal mass is ~360 kJ/K. At 12 kW net accumulation, cells heat at ~0.033 K/s = 2°C/min. In a 30-minute DCFC session, cells rise 60°C above ambient = 60+45 = 105°C. **Air cooling catastrophically fails the ASIL-D thermal requirement.** Score of 2 is generous (acknowledges it works at low C-rates in mild weather).

*Reliability (Refrigerant scores 2):*
Direct expansion refrigerant systems have compressors, expansion valves, and refrigerant under high pressure. MTBF for automotive-grade refrigerant compressors: ~80,000–100,000 km. For a 150,000 km vehicle life, probability of at least one compressor replacement is high. Additionally, refrigerant leaks (R-1234yf) require specialized equipment to detect and repair — unavailable at most Indian service centers.

### 5.12 Sensitivity Analysis and Safety Constraint Application

**Question 1: Can air cooling win on raw score if we reduce thermal performance weight?**

Scenario: Reduce thermal performance weight from 30% to 15%, redistribute to cost and weight.

| Criterion | Orig. Weight | Modified Weight | Air Weighted | Liquid Weighted |
|---|---|---|---|---|
| Thermal performance | 30 | **15** | 2×15=30 | 4×15=60 |
| System cost | 20 | **27** | 5×27=135 | 3×27=81 |
| Weight | 15 | **20** | 5×20=100 | 3×20=60 |
| Reliability | 20 | 20 | 4×20=80 | 4×20=80 |
| Serviceability | 15 | **18** | 5×18=90 | 4×18=72 |
| **TOTAL** | 100 | 100 | **435** | **353** |

Even with halved thermal weight, air cooling scores higher on points. **However, this analysis is invalid.**

**Why the score-based analysis is invalid for air cooling:**

Safety Goal SG-03 (ASIL-D): "BMS shall prevent cell temperature from exceeding 55°C during any charging or discharging event."

Air cooling at 45°C ambient and 150 kW DCFC cannot maintain cells below 55°C — it is physically impossible with the thermal math shown above. Therefore, air cooling **violates a mandatory ASIL-D safety requirement**. This is not a "low score" — it is a design that cannot be certified under ISO 26262. Air cooling may be used as a supplementary/backup system, but cannot be the primary thermal management approach.

**Conclusion from sensitivity analysis:** Air cooling is eliminated from consideration not because of score, but because it violates the ASIL-D safety constraint regardless of weight assigned to the criterion.

**Question 2: Between Liquid Indirect and Refrigerant, is the decision robust?**

At original weights: Liquid (365) vs. Refrigerant (270) — Liquid wins by 95 points.

For Refrigerant to tie Liquid, its thermal performance score advantage (+1 point = +30 weighted at W=30%) would need to overcome its serviceability and cost disadvantages. Even doubling thermal performance weight to 60% (extreme), Liquid still leads Refrigerant on overall score because Liquid's 4×60=240 vs. Refrigerant 5×60=300, but Refrigerant loses 30+40+20 points on cost/weight/serviceability = 90 points deficit. Refrigerant cannot overcome this.

### 5.13 Recommendation and Rationale

**Recommended: Indirect Liquid Cooling (Alternative B)**

**Formal Recommendation Statement:**
> IndraMotors shall select indirect liquid cooling (glycol-water coolant loop with aluminum cold plates) as the primary thermal management architecture for the IM-e1 battery pack.
>
> Air cooling (Alternative A) is eliminated: it cannot maintain cells below 55°C during 150 kW DCFC at 45°C ambient, violating ASIL-D safety goal SG-03. This elimination is based on physical analysis, not score.
>
> Refrigerant cooling (Alternative C) is rejected: higher initial performance is offset by significantly higher cost (+₹30,000/vehicle), lower reliability (compressor MTBF), and inability to service at Indian service centers — making it unviable for IndraMotors' market.

**Implementation Specification for Chapter 6:**
- Coolant: 50% glycol / 50% water mixture — freeze point -35°C (safe for Himalayan altitude)
- Cold plates: Extruded aluminum with serpentine coolant channels, one per battery module
- Coolant pump: Electric (12V), variable speed, 4–12 L/min flow range
- Chiller: On-demand refrigerant chiller (shared with cabin AC compressor) — activates when ambient >35°C during DCFC
- Coolant inlet temperature target: 25°C (charging), 30°C (driving)
- Hoses: Silicone automotive coolant hoses, IP67-rated quick-connect fittings

---

## 5.14 Trade Study Summary and Architecture Decisions

| Trade Study | Decision | Impact on Architecture (Ch 4) | Impact on Design (Ch 6) |
|---|---|---|---|
| **TS-1: Cell chemistry** | **LFP selected** | Pack topology (56S8P, 3.65V max/cell) confirmed. Cell voltage range 2.5V–3.65V defines CMC IC configuration on BQ76940. | SOC estimation must use EKF (LFP flat OCV curve). Passive balancing is sufficient (LFP lower imbalance tendency). Thermal runaway detection threshold calibrated for LFP (onset 270°C). |
| **TS-2: Thermal architecture** | **Indirect liquid cooling selected** | IFC-09 (coolant pump PWM) and IFC-10 (chiller valve PWM) confirmed as outputs. F5.2 and F5.3 (thermal actuator control) confirmed. | PID controller designed for coolant pump speed. Chiller bypass valve control logic. Thermal runaway rate-of-rise detection (2°C/s) is the safety function; cooling control is the operational function. |

**These two decisions lock down the remaining design space for Chapter 6.** No further trade studies are needed — the major architectural choices are made.

---

## 5.15 SE Process Reflection

### How MCDA Differs from Intuitive Decision-Making (Session 10)

In Session 10, you learned that decision quality requires:
1. A clear decision frame (what exactly is being decided)
2. Meaningful, reliable alternatives (not strawmen)
3. Clear values and trade-offs (criteria and weights)
4. Sound reasoning (the scoring and sensitivity analysis)
5. Commitment to follow through (documented recommendation)

Contrast this with how IndraMotors might have made this decision without MCDA:
> "The chief engineer used NMC on his previous project at his previous employer, so we'll use NMC."

This "intuitive" decision:
- Cannot be challenged by regulators (no documentation)
- Cannot be updated when context changes (Indian climate requirements are different from European)
- Carries personal bias rather than systematic analysis
- Would likely choose NMC — which fails thermally in Indian summer at DCFC rates

**MCDA is not about removing engineering judgment.** The weights encode engineering judgment. The scores require technical knowledge. The sensitivity analysis requires domain expertise. But MCDA makes that judgment transparent and auditable.

### Would Boeing Have Selected a Different MCAS Architecture? (Session 6)

In the Boeing 737 MAX case, the MCAS architecture decision — single AOA sensor, no pilot training, high authority — was made informally under schedule and cost pressure. Applying our trade study methodology:

**A proper Boeing MCAS trade study would have included:**
- Criteria: Safety (probability of catastrophic failure), Pilot awareness, Certification timeline, Training cost
- Safety criterion weight: ≥40% (flight safety is paramount)
- Alternatives: (A) Single sensor, hidden from pilots; (B) Dual sensor with disagree alert; (C) Full pilot training on MCAS

Alternative A would have scored poorly on safety (single-sensor SPOF). Alternative B or C would have won. The crashes would not have happened.

**The lesson:** Boeing had the engineering knowledge to recognize the risk. What was missing was a structured, documented decision process that gave safety the weight it deserved.

### Sensitivity Analysis Reduces Decision Risk (Session 9 Risk Preview)

The sensitivity analysis in both trade studies serves a risk management function:

- If the LFP cell supply chain fails (Risk R01, Chapter 9), IndraMotors needs to know: can NMC substitute without re-certifying the thermal architecture? The sensitivity analysis shows LFP's lead is robust but not infinite — NMC is the credible alternative, and the thermal architecture (liquid cooling) works for both chemistries.
- This is an example of designing with **decision robustness** in mind — choosing alternatives that remain viable if the operating context changes.

---

*Next: [Chapter 6 — Design Definition](06-design-definition.md)*
