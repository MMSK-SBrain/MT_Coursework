# Session 10: Decision and Quality Management
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 90 minutes lecture + 30 minutes Q&A
**Approach:** Decision-Science/Quality-Focused
**PPT Target:** 28-30 slides

---

## 🎯 Session Objectives (For Instructor)

By the end of this session, students will be able to:
- Apply systematic decision analysis techniques to engineering trade-offs
- Use multi-criteria decision analysis (MCDA) for complex automotive decisions
- Distinguish between Quality Assurance (QA) and Quality Control (QC)
- Implement critical parameter management in automotive systems
- Define and track meaningful metrics and KPIs for systems engineering
- Recognize common decision-making pitfalls and quality management failures
- Select appropriate decision frameworks for different problem types

**Mapped Learning Outcomes:** LO4 (Apply systems engineering practices and methods in automotive systems), LO5 (Analyse automotive systems using systems engineering approaches to increase performance)

---

## 📖 INSTRUCTOR-LED STORY ARC

### **SETUP: The Decision Dilemma** (Slides 1-5, ~10 minutes)

#### Slide 1: Title
**Visual:** Professional title slide with decision tree and quality metrics dashboard
**Instructor Script:**
> "Welcome to Session 10. Today we tackle two interconnected disciplines that separate successful systems engineering from failed projects: **Decision Management** and **Quality Management**.
>
> These aren't separate topics - they're two sides of the same coin. Good decisions lead to quality outcomes. Quality metrics inform better decisions."

#### Slide 2: Connection to Previous Sessions
**Visual:** Progression diagram showing Sessions 1→9→10
**Instructor Script:**
> "Let's connect where we've been:
>
> **Session 4**: We learned to write requirements - but what if stakeholders want contradictory things? (Decision needed)
>
> **Session 5**: We learned architecture - but how do we choose between competing designs? (Decision needed)
>
> **Session 8**: We learned verification and validation - but how do we ensure quality throughout? (Quality management)
>
> **Session 9**: We learned risk management - risks inform decisions about what to prioritize
>
> Today's focus: **How do we make systematic, defensible decisions? How do we ensure quality at every step?**"

#### Slide 3: Why Decision and Quality Management Are Critical
**Visual:** Statistics showing project outcomes based on decision quality
**Instructor Script:**
> "Let me show you sobering data:
>
> **Decision-making failures:**
> - 72% of major projects exceed budget due to poor early decisions (McKinsey)
> - Average cost of poor technical decision: $2.5M in automotive programs
> - 40% of product recalls trace to decisions made under uncertainty without systematic analysis
>
> **Quality management impact:**
> - Cost of quality (prevention + appraisal + failure) = 15-25% of total project cost
> - Cost to fix defects grows 10x at each lifecycle stage (requirements → design → test → production)
> - Toyota's quality culture saves estimated $1B+ annually compared to competitors
>
> **Key insight**: You WILL face decisions with incomplete information, conflicting objectives, and high stakes. How you decide determines success or failure."

#### Slide 4: Real-World Example - Boeing 737 MAX Decision Failure
**Visual:** Boeing 737 MAX with decision timeline
**Instructor Script:**
> "Boeing 737 MAX: 346 deaths, $20B+ in losses, 20-month grounding. Let's analyze the decision failures:
>
> **Decision Point 1: Engine placement**
> - **Trade-off**: Fuel efficiency vs flight characteristics
> - **Decision made**: Place larger engines forward and higher (efficiency priority)
> - **Consequence**: Changed aircraft pitch behavior
>
> **Decision Point 2: How to address pitch change**
> - **Options**:
>   - A) Redesign landing gear (expensive, time-consuming)
>   - B) Software solution (MCAS system - cheap, fast)
> - **Decision made**: Option B (software fix)
> - **Analysis used**: Cost and schedule only - safety not weighted properly
>
> **Decision Point 3: Pilot training requirements**
> - **Trade-off**: Safety (extensive training) vs marketability (no training difference from 737NG)
> - **Decision made**: Minimize training differences
> - **Consequence**: Pilots unaware of MCAS system
>
> **Quality management failure**:
> - Single point of failure (one AoA sensor)
> - Inadequate testing of failure modes
> - No critical parameter monitoring for sensor disagreement
>
> **Root cause**: Decisions optimized for cost/schedule without systematic multi-criteria analysis including safety. Quality gates failed to catch the gaps.
>
> Today, I'll show you how to avoid these catastrophic decision failures."

#### Slide 5: Learning Journey for Today
**Visual:** Roadmap with 6 key stops
**Instructor Script:**
> "Today's journey covers six critical areas:
>
> **Part 1**: Decision Analysis Fundamentals - Frameworks for systematic decisions
> **Part 2**: Multi-Criteria Decision Analysis (MCDA) - Handling conflicting objectives
> **Part 3**: Trade-off Analysis - Engineering the right compromises
> **Part 4**: Quality Assurance vs Quality Control - Prevention vs detection
> **Part 5**: Critical Parameter Management - Tracking what matters
> **Part 6**: Metrics and KPIs - Measuring systems engineering effectiveness
>
> By the end, you'll have systematic approaches to make and defend decisions under uncertainty, and ensure quality throughout the lifecycle."

---

### **TRIGGER: The Impossible Choice** (Slides 6-7, ~5 minutes)

#### Slide 6: The Battery Selection Challenge
**Visual:** Table showing three battery technology options
**Instructor Script:**
> "You're the systems engineer for a new electric vehicle. Your manager says:
>
> **'Select the battery technology for our new EV. Decision needed by Friday.'**
>
> You have three options:
>
> **Option A: Lithium Iron Phosphate (LFP)**
> - Cost: $90/kWh (lowest)
> - Energy density: 160 Wh/kg (lowest)
> - Safety: Excellent (most stable chemistry)
> - Lifespan: 3,000+ cycles (longest)
> - Charging speed: Moderate
> - Cold weather: Poor performance below -10°C
> - Supply chain: China-dependent (90% production)
>
> **Option B: NMC (Nickel Manganese Cobalt)**
> - Cost: $140/kWh (medium)
> - Energy density: 250 Wh/kg (highest)
> - Safety: Good (requires thermal management)
> - Lifespan: 1,500-2,000 cycles (medium)
> - Charging speed: Fast
> - Cold weather: Good performance
> - Supply chain: Cobalt sourcing concerns
>
> **Option C: Solid-State (Emerging)**
> - Cost: $250/kWh (highest, projected to decrease)
> - Energy density: 400+ Wh/kg (future potential)
> - Safety: Excellent (non-flammable)
> - Lifespan: Unknown (new technology)
> - Charging speed: Very fast (potential)
> - Cold weather: Excellent (projected)
> - Supply chain: Limited production capacity
>
> **How do you decide?** Each stakeholder wants something different:
> - Finance: Choose LFP (lowest cost)
> - Marketing: Choose solid-state (best specs for brochure)
> - Engineering: Choose NMC (proven, balanced)
> - Safety: Choose LFP or solid-state (safest)
> - Product planning: Depends on target market (range vs price)
>
> **This is exactly what systematic decision analysis solves.**"

#### Slide 7: What Happens Without Systematic Analysis
**Visual:** Decision-making gone wrong scenarios
**Instructor Script:**
> "Let me show you what happens when we DON'T use systematic decision methods:
>
> **Scenario 1 - HiPPO Decision** (Highest Paid Person's Opinion)
> - CEO heard about solid-state at a conference
> - 'Use solid-state batteries!'
> - Result: Technology not production-ready, program delayed 2 years, $300M overrun
>
> **Scenario 2 - Analysis Paralysis**
> - Team can't agree, keep analyzing
> - Missed decision deadline
> - Result: Competitor launches first, market share lost
>
> **Scenario 3 - Single-Criterion Optimization**
> - Finance drives decision on cost alone (LFP)
> - Result: Vehicle has poor cold-weather performance, customers complain, brand damage in northern markets
>
> **Scenario 4 - Gut Feel Decision**
> - 'I think NMC is the safe choice'
> - No documented rationale
> - Result: When battery performance issues arise 2 years later, no one can explain why this choice was made
>
> **What we need**:
> - Systematic evaluation across ALL criteria
> - Transparent weighting of stakeholder priorities
> - Documented, defensible decision rationale
> - Risk-aware trade-off analysis
>
> This is what professional decision management delivers."

---

### **RISING ACTION: Building the Decision and Quality Framework** (Slides 8-24, ~52 minutes)

#### **Part 1: Decision Analysis Fundamentals** (Slides 8-10, ~8 minutes)

##### Slide 8: The Decision Analysis Process
**Visual:** Process flow diagram with 7 steps
**Instructor Script:**
> "Systematic decision-making follows a proven process. This is the foundation:
>
> **Step 1: Frame the decision**
> - What exactly are we deciding?
> - What is the scope? (Battery chemistry only, or entire energy storage system?)
> - What is NOT being decided?
> - Example: 'Select battery chemistry for 75 kWh passenger EV with 400 km range target'
>
> **Step 2: Identify objectives**
> - What do we want to achieve?
> - Fundamental objectives (ends) vs means objectives
> - Example objectives: Minimize cost, maximize safety, maximize range, ensure supply chain resilience
>
> **Step 3: Create alternatives**
> - What are ALL viable options?
> - Don't eliminate prematurely
> - Include hybrid approaches
> - Example: Pure LFP, pure NMC, solid-state, LFP+NMC hybrid, defer decision (wait for solid-state maturity)
>
> **Step 4: Establish evaluation criteria**
> - How will we measure each objective?
> - Must be measurable, objective where possible
> - Example: $/kWh (cost), Wh/kg (energy density), cycles to 80% capacity (lifespan)
>
> **Step 5: Evaluate alternatives**
> - Score each alternative against each criterion
> - Use data, analysis, simulation, testing
> - Document assumptions
>
> **Step 6: Make decision**
> - Apply decision method (we'll cover several)
> - Consider uncertainty and risk
> - Document rationale
>
> **Step 7: Implement and monitor**
> - Execute decision
> - Track performance vs predictions
> - Be ready to adapt if conditions change
>
> **Key principle: The process is as important as the outcome.** Traceable decisions that can be explained years later."

##### Slide 9: Decision Types and Appropriate Methods
**Visual:** Decision matrix showing types vs methods
**Instructor Script:**
> "Not all decisions are equal. Different types need different approaches:
>
> **Type 1: Simple decisions (Low stakes, clear criteria)**
> - Example: Which supplier for standard bolts?
> - Method: Simple comparison table, lowest cost with quality threshold
> - Time investment: Minutes to hours
>
> **Type 2: Complicated decisions (Multiple criteria, quantifiable)**
> - Example: Battery chemistry selection
> - Method: Multi-criteria decision analysis (MCDA)
> - Time investment: Days to weeks
>
> **Type 3: Complex decisions (High uncertainty, many unknowns)**
> - Example: Invest in hydrogen vs battery technology for 2030?
> - Method: Scenario analysis, real options analysis, decision trees
> - Time investment: Weeks to months
>
> **Type 4: Wicked decisions (Ill-defined problem, conflicting values)**
> - Example: Autonomous vehicle ethical dilemmas (trolley problem)
> - Method: Stakeholder deliberation, value-focused thinking
> - Time investment: Months, ongoing
>
> **Common automotive examples:**
>
> | Decision | Type | Appropriate Method |
> |----------|------|-------------------|
> | Supplier selection for seats | Simple | Weighted scoring |
> | Powertrain architecture (ICE/Hybrid/BEV) | Complicated | MCDA (AHP, TOPSIS) |
> | Platform strategy for next generation | Complex | Scenario planning + MCDA |
> | ADAS feature prioritization | Complicated | Trade-off analysis + MCDA |
> | Autonomous safety policies | Wicked | Value-focused thinking |
>
> **Today's focus**: Types 2 and 3 - systematic methods for complicated and complex decisions."

##### Slide 10: Decision-Making Under Uncertainty
**Visual:** Uncertainty matrix (known-unknown)
**Instructor Script:**
> "Real engineering decisions are made with incomplete information. We must account for uncertainty:
>
> **Types of uncertainty:**
>
> **1. Parameter uncertainty** (We know what matters, but not exact values)
> - Example: 'Battery cost in 2027 will be $80-150/kWh'
> - Approach: Sensitivity analysis, Monte Carlo simulation
>
> **2. Model uncertainty** (We're not sure of the relationships)
> - Example: 'How does battery degradation relate to fast-charging frequency?'
> - Approach: Multiple models, expert judgment, testing
>
> **3. Scenario uncertainty** (Future states of the world)
> - Example: 'Will governments mandate solid-state batteries by 2030?'
> - Approach: Scenario planning, decision trees
>
> **4. Unknown unknowns** (Things we don't know we don't know)
> - Example: Unforeseen battery chemistry breakthrough
> - Approach: Robustness analysis (choose options that work across many scenarios)
>
> **Decision under uncertainty framework:**
>
> - **Known knowns**: Use deterministic analysis
> - **Known unknowns**: Use probabilistic analysis (expected value, decision trees)
> - **Unknown unknowns**: Use robust decision-making (choose options that don't fail catastrophically)
>
> **Automotive example - Range uncertainty:**
> You're designing for 400 km range, but actual range depends on:
> - Temperature (-20°C to +40°C) - known distribution
> - Driving style (aggressive vs eco) - statistical data available
> - Future regulation (unknown)
> - Battery degradation over 10 years (model uncertainty)
>
> **Approach**:
> - Model parameter uncertainty (Monte Carlo)
> - Design for 90th percentile worst case (robustness)
> - Plan for future regulation scenarios
> - Include margin for degradation uncertainty
>
> This leads to decisions that are defensible even when inputs are uncertain."

---

#### **Part 2: Multi-Criteria Decision Analysis (MCDA)** (Slides 11-14, ~12 minutes)

##### Slide 11: What is MCDA and Why It Matters
**Visual:** Comparison of single-criterion vs multi-criterion decision
**Instructor Script:**
> "Most engineering decisions involve MULTIPLE, CONFLICTING objectives. This is where MCDA shines.
>
> **Traditional approach** (single criterion):
> - 'Minimize cost' → Choose cheapest option
> - Problem: Ignores safety, quality, performance, schedule, risk
>
> **MCDA approach** (multiple criteria):
> - Explicitly consider ALL important criteria
> - Weight criteria based on stakeholder priorities
> - Calculate overall score for each alternative
> - Make transparent, defensible decisions
>
> **When to use MCDA:**
> - Multiple objectives that conflict (can't optimize all simultaneously)
> - Stakeholders with different priorities
> - Need documented, traceable rationale
> - High-stakes decisions (regulatory scrutiny, safety-critical)
>
> **Automotive applications:**
> - Architecture selection (ICE vs Hybrid vs BEV)
> - Supplier selection (not just lowest cost)
> - Feature prioritization (which ADAS features for next release?)
> - Platform decisions (develop new platform or adapt existing?)
> - Technology roadmap (which technologies to invest in?)
>
> **Key benefit**: MCDA forces EXPLICIT discussion of values and trade-offs. No hidden assumptions."

##### Slide 12: MCDA Method 1 - Weighted Sum Model (WSM)
**Visual:** Step-by-step WSM calculation example
**Instructor Script:**
> "The simplest and most common MCDA method: **Weighted Sum Model (WSM)**.
>
> **Process:**
>
> **Step 1: Define criteria and weights**
> - List all evaluation criteria
> - Assign weights (must sum to 1.0 or 100%)
> - Weights reflect relative importance
>
> **Step 2: Score each alternative**
> - Rate each alternative on each criterion
> - Use common scale (e.g., 1-10 or 0-100)
> - Based on data, analysis, or expert judgment
>
> **Step 3: Calculate weighted score**
> - Multiply score × weight for each criterion
> - Sum across all criteria
> - Alternative with highest total score wins
>
> **Example: Battery selection with WSM**
>
> **Criteria and weights:**
> | Criterion | Weight | Rationale |
> |-----------|--------|-----------|
> | Cost | 0.25 | Important but not sole driver |
> | Energy Density | 0.20 | Affects vehicle range and mass |
> | Safety | 0.30 | Critical for liability and brand |
> | Lifespan | 0.15 | Warranty cost impact |
> | Technology Maturity | 0.10 | Risk consideration |
> | **Total** | **1.00** | |
>
> **Scoring (1-10 scale, higher is better):**
>
> | Criterion | Weight | LFP Score | LFP Weighted | NMC Score | NMC Weighted | Solid-State Score | SS Weighted |
> |-----------|--------|-----------|--------------|-----------|--------------|-------------------|-------------|
> | Cost | 0.25 | 9 | 2.25 | 6 | 1.50 | 2 | 0.50 |
> | Energy Density | 0.20 | 5 | 1.00 | 9 | 1.80 | 10 | 2.00 |
> | Safety | 0.30 | 10 | 3.00 | 7 | 2.10 | 10 | 3.00 |
> | Lifespan | 0.15 | 9 | 1.35 | 6 | 0.90 | 4 | 0.60 |
> | Maturity | 0.10 | 10 | 1.00 | 10 | 1.00 | 3 | 0.30 |
> | **TOTAL** | | | **8.60** | | **7.30** | | **6.40** |
>
> **Result: LFP wins** with this weighting scheme (8.60 vs 7.30 vs 6.40)
>
> **Key insight**: If we change weights (e.g., energy density becomes 0.35, cost becomes 0.15), NMC might win. This shows how **values drive decisions**.
>
> **Sensitivity analysis**: Test how decision changes with different weights. If decision is stable across reasonable weight variations → robust decision."

##### Slide 13: MCDA Method 2 - Analytic Hierarchy Process (AHP)
**Visual:** AHP hierarchy structure and pairwise comparison
**Instructor Script:**
> "**Analytic Hierarchy Process (AHP)** - developed by Thomas Saaty, widely used in automotive and aerospace.
>
> **Key difference from WSM**: AHP derives weights through **pairwise comparisons** rather than assigning them directly.
>
> **Process:**
>
> **Step 1: Build hierarchy**
> - Goal (top level): Select battery technology
> - Criteria (middle): Cost, safety, performance, etc.
> - Alternatives (bottom): LFP, NMC, Solid-State
>
> **Step 2: Pairwise comparison of criteria**
> - Compare each criterion to every other
> - Use Saaty's 1-9 scale:
>   - 1 = Equal importance
>   - 3 = Moderate importance
>   - 5 = Strong importance
>   - 7 = Very strong importance
>   - 9 = Extreme importance
>
> **Example comparison**:
> 'How much more important is Safety compared to Cost?'
> → Answer: Safety is moderately to strongly more important = 4
>
> **Step 3: Calculate criteria weights**
> - Build pairwise comparison matrix
> - Calculate eigenvector (mathematical process)
> - Normalized eigenvector = criteria weights
>
> **Step 4: Check consistency**
> - AHP includes consistency ratio (CR)
> - CR < 0.10 means judgments are consistent
> - CR > 0.10 means revisit pairwise comparisons (judgments are contradictory)
>
> **Step 5: Repeat for alternatives**
> - For each criterion, compare alternatives pairwise
> - Calculate scores for each alternative on each criterion
>
> **Step 6: Synthesize**
> - Combine criteria weights and alternative scores
> - Calculate overall priority for each alternative
>
> **Example pairwise comparison matrix (criteria):**
>
> |  | Cost | Safety | Energy Density | Lifespan |
> |--|------|--------|----------------|----------|
> | Cost | 1 | 1/4 | 2 | 2 |
> | Safety | 4 | 1 | 5 | 5 |
> | Energy Density | 1/2 | 1/5 | 1 | 2 |
> | Lifespan | 1/2 | 1/5 | 1/2 | 1 |
>
> **Derived weights** (after eigenvector calculation):
> - Safety: 0.52 (dominant)
> - Cost: 0.23
> - Energy Density: 0.14
> - Lifespan: 0.11
>
> **Advantage**: Weights emerge from explicit comparisons, easier for stakeholders than directly assigning percentages.
>
> **Disadvantage**: Time-consuming for many criteria (n criteria requires n×(n-1)/2 comparisons).
>
> **Tool support**: Expert Choice, Super Decisions, online AHP calculators."

##### Slide 14: MCDA Method 3 - TOPSIS
**Visual:** TOPSIS concept diagram with ideal and anti-ideal solutions
**Instructor Script:**
> "**TOPSIS** (Technique for Order Preference by Similarity to Ideal Solution) - elegant method used in automotive engineering.
>
> **Core concept**:
> - Best alternative is closest to the **ideal solution** (best score on all criteria)
> - Best alternative is farthest from the **anti-ideal solution** (worst score on all criteria)
>
> **Process:**
>
> **Step 1: Create decision matrix**
> - Rows = alternatives
> - Columns = criteria
> - Cells = scores
>
> **Step 2: Normalize scores**
> - Convert to common scale (0-1)
> - Accounts for different units (cost in $, weight in kg, etc.)
>
> **Step 3: Apply weights**
> - Multiply normalized scores by criterion weight
>
> **Step 4: Identify ideal and anti-ideal solutions**
> - **Ideal**: Best score on each criterion
> - **Anti-ideal**: Worst score on each criterion
>
> **Step 5: Calculate distances**
> - Euclidean distance from each alternative to ideal
> - Euclidean distance from each alternative to anti-ideal
>
> **Step 6: Calculate relative closeness**
> - Closeness = Distance to anti-ideal / (Distance to ideal + Distance to anti-ideal)
> - Range: 0 to 1 (higher is better)
>
> **Step 7: Rank alternatives**
> - Highest closeness score wins
>
> **Example (battery selection):**
>
> Assume normalized, weighted scores:
>
> | Alternative | Cost | Safety | Energy | Lifespan | Sum to Ideal | Sum to Anti-Ideal | Closeness |
> |-------------|------|--------|--------|----------|--------------|-------------------|-----------|
> | LFP | 0.23 | 0.30 | 0.10 | 0.14 | 0.15 | 0.42 | 0.74 |
> | NMC | 0.15 | 0.21 | 0.18 | 0.09 | 0.23 | 0.31 | 0.57 |
> | Solid-State | 0.05 | 0.30 | 0.20 | 0.06 | 0.28 | 0.25 | 0.47 |
>
> **Result: LFP wins** (closeness = 0.74, closest to ideal, farthest from anti-ideal)
>
> **Advantages**:
> - Mathematically rigorous
> - Handles any number of alternatives and criteria
> - Clear visual interpretation (geometric distance)
>
> **When to use**:
> - Large number of alternatives (e.g., supplier selection from 20 candidates)
> - Quantitative criteria dominate
> - Need defensible, objective ranking
>
> **Automotive applications**: Material selection, supplier scoring, architecture ranking, technology selection."

---

#### **Part 3: Trade-off Analysis** (Slides 15-17, ~10 minutes)

##### Slide 15: Understanding Trade-offs
**Visual:** Pareto frontier diagram
**Instructor Script:**
> "In engineering, we rarely optimize a single objective. We TRADE OFF between competing goals.
>
> **Classic automotive trade-offs:**
> - Performance vs Fuel Efficiency (power vs consumption)
> - Safety vs Weight (crashworthiness adds mass)
> - Cost vs Quality (cheaper materials may compromise durability)
> - Features vs Complexity (more features = more failure modes)
> - Development Speed vs Robustness (fast development may skip testing)
>
> **The Pareto Frontier concept:**
>
> A solution is **Pareto optimal** (or Pareto efficient) if you can't improve one objective without worsening another.
>
> **Example: Range vs Cost trade-off in EVs**
>
> | Battery Size | Range (km) | Cost ($) | Pareto Optimal? |
> |--------------|------------|----------|-----------------|
> | 50 kWh | 300 | $20,000 | Yes (cheapest) |
> | 60 kWh | 360 | $23,000 | Yes |
> | 75 kWh | 450 | $27,000 | Yes |
> | 90 kWh | 540 | $32,000 | Yes |
> | 65 kWh | 350 | $26,000 | **No** (dominated by 75 kWh - less range, more expensive) |
>
> **All Pareto-optimal solutions lie on the Pareto frontier.** Choice among them depends on stakeholder values.
>
> **Trade-off analysis process:**
> 1. Identify conflicting objectives
> 2. Generate design alternatives
> 3. Evaluate each on both objectives
> 4. Plot trade-off curve (Pareto frontier)
> 5. Eliminate dominated solutions
> 6. Apply decision criteria to choose from Pareto set
>
> **Visual**: [Show graph with Cost on X-axis, Range on Y-axis, Pareto frontier curve]
>
> **Key insight**: Don't waste time analyzing dominated solutions. Focus on Pareto frontier."

##### Slide 16: Trade-off Analysis Methods
**Visual:** Trade-off analysis toolkit
**Instructor Script:**
> "How do we systematically analyze trade-offs? Multiple methods:
>
> **Method 1: Parametric Trade Studies**
> - Vary design parameters, observe impact on objectives
> - Example: Vary battery size from 40-100 kWh, plot range vs cost vs weight
> - Tools: Excel, MATLAB, Python, design exploration software
>
> **Method 2: Utility Theory**
> - Convert multiple objectives to single 'utility' value
> - Reflect stakeholder preferences mathematically
> - Example: Utility = w1×Range + w2×(1/Cost) + w3×(1/Weight)
> - Choose design with maximum utility
>
> **Method 3: Design Space Exploration (DSE)**
> - Generate large number of design alternatives (1000s)
> - Evaluate all on multiple objectives
> - Visualize in multi-dimensional space
> - Filter to Pareto frontier
> - Tools: ModelCenter, Isight, MOEA (Multi-Objective Evolutionary Algorithms)
>
> **Method 4: Sensitivity Analysis**
> - How sensitive is the decision to changes in parameters or weights?
> - Example: If battery cost drops 20%, does the decision change?
> - Identifies critical assumptions and uncertainties
>
> **Method 5: Knee of the Curve Analysis**
> - On trade-off curve, find the 'knee' point
> - Point of diminishing returns
> - Example: 75 kWh battery at knee - going to 90 kWh adds 20% range but 35% cost
>
> **Automotive example - Aerodynamics vs Cooling trade-off:**
>
> **Problem**: Smaller grille improves aerodynamics (lower drag, better efficiency) but reduces radiator airflow (cooling performance)
>
> **Trade study approach:**
> 1. Parametric variation: Grille sizes from 1000 cm² to 3000 cm²
> 2. CFD analysis: Drag coefficient (Cd) vs cooling air mass flow
> 3. System simulation: Vehicle performance in hot conditions
> 4. Identify Pareto frontier: Designs that balance Cd and cooling
> 5. Apply decision criteria: Choose based on target market (hot climate → larger grille; cold climate → smaller grille)
>
> **Result**: Document WHY specific grille size was chosen, including trade-offs accepted.
>
> This becomes critical when, 2 years later, someone asks: 'Why didn't we make the grille smaller for better efficiency?'"

##### Slide 17: Real Automotive Case - Tesla Model 3 Trade-offs
**Visual:** Model 3 design trade-off decisions
**Instructor Script:**
> "Let's examine real trade-off decisions from Tesla Model 3 development:
>
> **Trade-off 1: Glass Roof vs Traditional Roof**
>
> **Objectives in conflict:**
> - Aesthetics / Differentiation (glass roof = premium feel)
> - Weight (glass heavier than stamped steel + insulation)
> - Cost (glass roof more expensive)
> - Thermal management (glass increases solar heat gain → larger AC required)
> - Crash safety (roof strength requirements)
>
> **Tesla's decision**: Glass roof standard
> **Rationale**:
> - Differentiation value outweighs cost/weight (~15 kg penalty)
> - UV-filtering glass mitigates thermal issue
> - Single-piece glass simplifies manufacturing (assembly cost offset)
> - Brand positioning (premium EV)
>
> **Trade-off accepted**: Higher weight and thermal load for aesthetic/brand value
>
> **Trade-off 2: Minimalist Interior (No Instrument Cluster)**
>
> **Objectives in conflict:**
> - Cost reduction (eliminate instrument cluster = $150-200 savings)
> - User experience (drivers expect instrument cluster)
> - Safety (eyes off road to check center screen)
> - Differentiation (unique Tesla interface)
>
> **Tesla's decision**: Center screen only, no instrument cluster
> **Rationale**:
> - Cost savings
> - Simpler manufacturing
> - Software flexibility (all UI updates via OTA)
> - Brand differentiation
>
> **Trade-off accepted**: User experience concerns for cost/simplicity
> **Market result**: Polarizing - some love it, some hate it (design risk accepted)
>
> **Trade-off 3: Range vs Affordability (Battery Size)**
>
> **Objectives**:
> - Range (more range needs bigger battery)
> - Affordability (target $35k base price)
> - Profitability (larger battery reduces margin)
>
> **Tesla's approach**: Multiple variants
> - Standard Range: 50 kWh, 260 km, $35k (later discontinued - unprofitable)
> - Long Range: 75 kWh, 520 km, $46k (Pareto optimal - good range, acceptable cost)
> - Performance: 75 kWh, 480 km, $56k (range traded for acceleration)
>
> **Decision**: Optimize product portfolio across Pareto frontier to serve different customer values
>
> **Lessons learned:**
> 1. Trade-offs must align with brand positioning
> 2. Different customers value objectives differently → multiple variants
> 3. Document trade-off rationale for future reference
> 4. Some trade-offs create risk (minimalist interior) - accept knowingly
> 5. Quantify trade-offs where possible (weight, cost, range all measurable)"

---

#### **Part 4: Quality Assurance vs Quality Control** (Slides 18-20, ~8 minutes)

##### Slide 18: QA vs QC - The Critical Distinction
**Visual:** Two-column comparison with process diagrams
**Instructor Script:**
> "One of the most misunderstood distinctions in engineering: **Quality Assurance vs Quality Control**. They're complementary but fundamentally different.
>
> **Quality Assurance (QA) - PREVENTION**
> - **Definition**: Process-focused activities to prevent defects
> - **Timing**: Throughout development, before defects occur
> - **Approach**: Design processes, standards, training, reviews
> - **Question**: 'Are we building quality IN?'
> - **Responsibility**: Everyone (QA team facilitates)
>
> **Quality Control (QC) - DETECTION**
> - **Definition**: Product-focused activities to identify defects
> - **Timing**: During and after development, after defects exist
> - **Approach**: Testing, inspection, measurement, validation
> - **Question**: 'Are we finding defects OUT?'
> - **Responsibility**: QC/Test team (dedicated)
>
> **Simple analogy:**
> - **QA**: Installing guardrails on a mountain road (prevents cars from going off cliff)
> - **QC**: Inspecting cars after they've crashed (detecting damage)
>
> **You want both, but QA is more cost-effective.**
>
> **Automotive examples:**
>
> | Activity | QA or QC? | Rationale |
> |----------|-----------|-----------|
> | Design FMEA workshop | QA | Prevents defects by identifying failure modes in design phase |
> | Final vehicle inspection before delivery | QC | Detects defects after production |
> | Supplier development program | QA | Prevents defects by improving supplier processes |
> | Software code review | QA | Prevents defects by catching errors before code is compiled |
> | Dynamometer testing | QC | Detects performance defects through testing |
> | ISO 26262 compliance process | QA | Prevents safety issues through systematic process |
> | X-ray inspection of welds | QC | Detects weld defects after welding |
>
> **Cost comparison** (Automotive Industry Action Group data):
> - Prevention (QA): $1 per unit
> - Appraisal (QC during production): $10 per unit
> - Internal failure (found before delivery): $100 per unit
> - External failure (found by customer): $1,000+ per unit
> - Recall: $10,000+ per unit
>
> **Key principle**: Shift left - invest in QA to prevent defects rather than relying on QC to catch them."

##### Slide 19: Quality Management Systems (QMS)
**Visual:** QMS framework pyramid
**Instructor Script:**
> "A **Quality Management System (QMS)** integrates QA and QC into organizational processes.
>
> **QMS purpose:**
> - Ensure consistent quality
> - Meet regulatory requirements
> - Enable continuous improvement
> - Provide objective evidence of quality
>
> **Key QMS standards in automotive:**
>
> **1. ISO 9001 - General Quality Management**
> - Applicable to all industries
> - Process approach, risk-based thinking
> - Customer focus, continual improvement
> - Required for most automotive suppliers
>
> **2. IATF 16949 - Automotive Quality Management**
> - Built on ISO 9001, adds automotive-specific requirements
> - Mandatory for automotive OEM suppliers
> - Emphasizes defect prevention, variation reduction
> - Includes customer-specific requirements (GM, Ford, VW, etc.)
> - Core tools: APQP, PPAP, FMEA, SPC, MSA
>
> **3. ISO 26262 - Functional Safety**
> - Quality management for safety-critical systems
> - V-model process, safety lifecycle
> - Required for ASIL-rated automotive systems
>
> **4. ASPICE - Automotive SPICE (Software Process Improvement and Capability Determination)**
> - Process assessment model for automotive software
> - Capability levels 0-5 (similar to CMMI)
> - Many OEMs require suppliers to achieve Level 2 or 3
>
> **QMS structure:**
>
> **Level 1: Quality Policy and Objectives**
> - Top management commitment
> - Example: 'Zero defects, first-time quality, continuous improvement'
>
> **Level 2: Quality Manual**
> - How organization meets QMS standard
> - Process map, responsibilities
>
> **Level 3: Procedures**
> - How specific processes are executed
> - Example: Design review procedure, change control procedure
>
> **Level 4: Work Instructions**
> - Detailed step-by-step instructions
> - Example: How to perform specific test
>
> **Level 5: Records**
> - Evidence that processes were followed
> - Example: Test reports, inspection records, meeting minutes
>
> **Automotive QMS in practice:**
> - Design reviews at phase gates (prevent design defects)
> - Supplier audits (prevent supply chain defects)
> - Production Part Approval Process (PPAP) - verify production readiness
> - Control plans (ensure process capability)
> - Reaction plans (contain defects quickly)
> - Lessons learned (prevent recurrence)
>
> **Certification**: Third-party audits verify QMS compliance (e.g., TÜV, BSI, DNV)"

##### Slide 20: Quality Gates and Phase Reviews
**Visual:** V-model with quality gates marked
**Instructor Script:**
> "**Quality gates** are decision points where projects must demonstrate quality criteria before proceeding.
>
> **Purpose:**
> - Prevent defects from propagating to next phase
> - Ensure readiness before major investment
> - Provide management visibility
> - Enforce disciplined process
>
> **Typical automotive quality gates (aligned with V-model):**
>
> **Gate 0: Concept Approval**
> - Entry criteria: Market analysis, business case, preliminary requirements
> - Quality checks: Requirements completeness, stakeholder alignment, feasibility
> - Exit criteria: Approved concept, funded program, assigned team
>
> **Gate 1: Requirements Review**
> - Entry criteria: Complete stakeholder requirements, system requirements
> - Quality checks: Requirements quality attributes (clear, verifiable, traceable), RTM completeness
> - Exit criteria: Baselined requirements, approved for design
>
> **Gate 2: Design Review**
> - Entry criteria: System architecture, subsystem designs, interface definitions
> - Quality checks: Design FMEA complete, design verification plan, traceability to requirements
> - Exit criteria: Approved design, released for implementation
>
> **Gate 3: Implementation Review**
> - Entry criteria: Prototype/software complete, unit tested
> - Quality checks: Code reviews, unit test results, integration test plan
> - Exit criteria: Ready for integration testing
>
> **Gate 4: Verification Review**
> - Entry criteria: System integrated, test results available
> - Quality checks: Requirements verification complete, test coverage, defect resolution
> - Exit criteria: Verified system, ready for validation
>
> **Gate 5: Validation Review (Production Readiness)**
> - Entry criteria: Validation testing complete, PPAP submitted
> - Quality checks: Customer acceptance, manufacturing process capability (Cpk ≥ 1.33), regulatory compliance
> - Exit criteria: Approved for production launch
>
> **Gate 6: Launch Review**
> - Entry criteria: Initial production complete, field monitoring data
> - Quality checks: Zero major defects, process stability, customer satisfaction
> - Exit criteria: Ramp-up to full production
>
> **Gate criteria example (Requirements Review):**
>
> ✓ All stakeholder needs documented
> ✓ System requirements complete (100% of needs traced)
> ✓ Requirements quality checked (0 ambiguous requirements, 100% verifiable)
> ✓ Requirements Traceability Matrix complete
> ✓ Regulatory requirements identified and mapped
> ✓ Requirements baseline established in configuration management
> ✓ Stakeholder sign-off obtained
> ✓ Design FMEA initiated
>
> **Gate governance:**
> - **Go**: Criteria met, proceed to next phase
> - **Conditional Go**: Minor issues, proceed with documented actions
> - **No-Go**: Significant gaps, do not proceed until resolved
>
> **Key principle**: Quality gates are non-negotiable. Never skip gates under schedule pressure - that's when defects escape."

---

#### **Part 5: Critical Parameter Management** (Slides 21-22, ~6 minutes)

##### Slide 21: What Are Critical Parameters?
**Visual:** Pyramid showing parameter criticality levels
**Instructor Script:**
> "Not all parameters are created equal. **Critical parameters** are the few vital characteristics that determine system success.
>
> **Definition**: Critical parameters are characteristics that:
> 1. Significantly affect customer satisfaction or safety
> 2. Have narrow acceptable tolerances
> 3. Require special controls to ensure conformance
> 4. Can cause system failure or major defect if out of spec
>
> **Categories:**
>
> **Critical-to-Quality (CTQ) Parameters**
> - Directly impact customer-perceived quality
> - Example: Brake pedal feel, 0-100 km/h acceleration time
>
> **Critical-to-Safety (CTS) Parameters**
> - Affect occupant or pedestrian safety
> - Example: Airbag deployment time, ABS response time
>
> **Critical-to-Function (CTF) Parameters**
> - Essential for system to perform intended function
> - Example: Battery voltage range, sensor accuracy
>
> **Critical-to-Process (CTP) Parameters**
> - Manufacturing process variables that affect quality
> - Example: Welding current, paint booth temperature
>
> **Example - Electric Vehicle Battery System:**
>
> | Parameter | Type | Specification | Why Critical | Control Method |
> |-----------|------|---------------|--------------|----------------|
> | Cell voltage | CTF, CTS | 2.5-4.2V | Over-voltage = fire risk, under-voltage = damage | 100% monitoring, BMS cutoff |
> | Temperature | CTS | -20 to +60°C | Thermal runaway risk | Thermal sensors, active cooling |
> | State of Charge (SOC) accuracy | CTQ | ±3% | Range anxiety if inaccurate | Kalman filter, calibration |
> | Isolation resistance | CTS | >100 Ω/V | Electrical shock hazard | Pre-drive check, ISO monitoring |
> | Crash deformation limit | CTS | <15mm intrusion | Prevents cell puncture | FEA analysis, crash testing |
>
> **Critical parameter characteristics:**
> - Measurable (quantitative specification)
> - Controlled (monitoring, process controls, inspection)
> - Documented (control plan, work instructions)
> - Traceable (linked to requirements and risks)
>
> **Pareto principle (80/20 rule)**:
> - 20% of parameters cause 80% of defects
> - Identify and control the critical 20%"

##### Slide 22: Critical Parameter Management Process
**Visual:** CPM process flowchart
**Instructor Script:**
> "Systematic **Critical Parameter Management (CPM)** ensures vital characteristics are controlled:
>
> **Step 1: Identify Critical Parameters**
> - Sources:
>   - Requirements analysis (safety, performance requirements)
>   - FMEA (high RPN failure modes)
>   - Historical warranty data (known problem areas)
>   - Regulatory requirements (crash, emissions, safety)
>   - Customer complaints (VOC - Voice of Customer)
> - Tool: Critical Parameter Identification Matrix
>
> **Step 2: Classify and Prioritize**
> - Rate by criticality (CTS > CTQ > CTF > CTP)
> - Rate by risk (probability × severity)
> - Focus control effort on highest priority
>
> **Step 3: Define Specifications**
> - Nominal value and tolerances
> - Based on capability studies and margin analysis
> - Example: Battery SOC accuracy = 50% ± 3% (nominal ± tolerance)
>
> **Step 4: Establish Control Methods**
>
> **Prevention controls (QA)**:
> - Design for robustness (parameter insensitive to variation)
> - Process capability studies (Cpk ≥ 1.33 for critical params)
> - Poka-yoke (error-proofing)
>
> **Detection controls (QC)**:
> - 100% inspection for safety-critical parameters
> - Statistical Process Control (SPC) for process parameters
> - Automated monitoring (sensors, BMS)
>
> **Step 5: Document in Control Plan**
> - Control plan lists all critical parameters
> - For each: specification, measurement method, frequency, reaction plan
>
> **Example Control Plan (Battery Assembly):**
>
> | Parameter | Spec | Measure Method | Frequency | Reaction if OOS |
> |-----------|------|----------------|-----------|-----------------|
> | Cell voltage | 3.6±0.1V | Digital voltmeter | 100% | Reject cell, investigate supplier |
> | Torque (busbars) | 8±1 Nm | Torque wrench | 100% | Rework, retorque |
> | Isolation resistance | >500 kΩ | Megohmmeter | 100% | Do not ship, investigate |
> | Leak test (pass/fail) | Pass | Helium leak detector | 100% | Rework seals, retest |
>
> **Step 6: Monitor and React**
> - Real-time monitoring where possible
> - Immediate reaction if out-of-spec
> - Root cause analysis for any critical parameter excursion
>
> **Step 7: Continuous Improvement**
> - Track trends over time
> - Reduce variation (Six Sigma approach - Cpk ≥ 2.0 target)
> - Update control methods based on lessons learned
>
> **Tools:**
> - Control charts (SPC)
> - Process capability studies (Cp, Cpk)
> - Measurement System Analysis (MSA) - ensure measurement accuracy
> - Reaction plans (immediate containment)
>
> **Automotive standard**: AIAG Control Plan methodology, PPAP requirements"

---

#### **Part 6: Metrics and KPIs** (Slides 23-24, ~8 minutes)

##### Slide 23: Systems Engineering Metrics and KPIs
**Visual:** Balanced scorecard showing metric categories
**Instructor Script:**
> "**'You can't manage what you don't measure.'** - Peter Drucker
>
> Systems engineering effectiveness must be measured. But measure the RIGHT things.
>
> **Metric vs KPI:**
> - **Metric**: Any quantitative measurement
> - **KPI (Key Performance Indicator)**: Metric that's critical to success, tracked by management
>
> **Categories of SE metrics:**
>
> **1. Product Quality Metrics**
> - Defect density (defects per 1000 requirements or KLOC)
> - Defect escape rate (defects found by customer vs total)
> - Mean Time Between Failures (MTBF)
> - Warranty claims per 1000 vehicles (CPV - Claims Per Vehicle)
>
> **2. Process Performance Metrics**
> - Requirements volatility (% requirements changed after baseline)
> - Requirements test coverage (% requirements with test cases)
> - Design review effectiveness (defects found in reviews vs testing)
> - Phase containment (% defects found in phase where introduced)
>
> **3. Schedule Metrics**
> - Schedule variance (actual vs planned)
> - Milestone achievement rate (% milestones met on time)
> - Cycle time (time from concept to production)
>
> **4. Cost Metrics**
> - Cost variance (actual vs budget)
> - Cost of quality (prevention + appraisal + failure costs)
> - Rework cost as % of total development cost
>
> **5. Productivity Metrics**
> - Requirements developed per engineer-month
> - Test cases executed per week
> - Defect closure rate (defects fixed per week)
>
> **Example KPIs for automotive program:**
>
> | KPI | Target | Actual (Month 6) | Status |
> |-----|--------|------------------|--------|
> | Requirements stability | <5% change/month | 3.2% | ✓ Green |
> | Test coverage | 100% | 94% | ⚠ Yellow |
> | Defect density | <0.5 def/req | 0.7 def/req | ❌ Red |
> | Schedule variance | ±5% | -8% (behind) | ❌ Red |
> | Defect escape rate | <5% | 3% | ✓ Green |
> | Design review participation | >90% | 85% | ⚠ Yellow |
>
> **Balanced scorecard approach**: Don't optimize one metric at expense of others
> - Optimizing schedule only → quality suffers
> - Optimizing cost only → safety compromised
> - Balance across quality, cost, schedule, innovation"

##### Slide 24: Implementing Effective Metrics Programs
**Visual:** Metrics implementation framework
**Instructor Script:**
> "Metrics programs often fail. Here's how to make them effective:
>
> **Principles of good metrics:**
>
> **1. SMART criteria:**
> - **S**pecific: Clear definition, no ambiguity
> - **M**easurable: Objective, quantifiable
> - **A**chievable: Realistic targets
> - **R**elevant: Tied to objectives
> - **T**imely: Measured frequently enough to enable action
>
> **2. Actionable**:
> - Bad metric: 'Customer satisfaction = 7.5/10' (What do you do with this?)
> - Good metric: '23% of customers dissatisfied with cruise control response time (target <10%)' (Clear action: improve response time)
>
> **3. Leading vs Lagging:**
> - **Lagging indicators**: Tell you what happened (defects found, schedule variance)
> - **Leading indicators**: Predict future performance (requirements review completion, test case development rate)
> - Use both: Leading indicators enable proactive management
>
> **4. Goal alignment:**
> - Metrics should drive desired behavior
> - Bad metric: Lines of code per day (encourages bloated code)
> - Good metric: Defects per KLOC (encourages quality)
>
> **Common metric pitfalls:**
>
> **Pitfall 1: Metric gaming**
> - Example: Measure defect closure rate → Engineers close defects as 'not reproducible' to hit targets
> - Solution: Measure multiple related metrics (closure rate + customer-found defects)
>
> **Pitfall 2: Vanity metrics**
> - Metrics that look good but don't drive improvement
> - Example: 'We wrote 5,000 requirements!' (Quantity ≠ quality)
> - Solution: Focus on outcome metrics (% requirements verified, defect rate)
>
> **Pitfall 3: Too many metrics**
> - Tracking 50+ metrics → analysis paralysis
> - Solution: 5-7 KPIs for executive dashboard, detailed metrics for working level
>
> **Pitfall 4: No action on metrics**
> - Collecting data but not using it for decisions
> - Solution: Establish review cadence and decision triggers
>
> **Automotive metrics program structure:**
>
> **Daily metrics** (working level):
> - Test execution status
> - Build success rate
> - Critical defects open
>
> **Weekly metrics** (team level):
> - Test coverage progress
> - Defect inflow/outflow
> - Schedule variance
>
> **Monthly metrics** (program management):
> - KPI dashboard (5-7 key indicators)
> - Trend analysis
> - Risk exposure
>
> **Quarterly metrics** (executive level):
> - Program health (RAG status - Red/Amber/Green)
> - Cost/schedule/quality summary
> - Strategic decisions needed
>
> **Tools:**
> - Dashboards (PowerBI, Tableau)
> - Automated data collection (from ALM tools, JIRA, DOORS)
> - Trend charts
> - Statistical process control charts
>
> **Example decision trigger:**
> - KPI: Defect density target <0.5 def/req
> - Actual: 0.7 def/req (Red status)
> - **Triggered action**: Mandatory root cause analysis, additional design reviews, extended testing phase
>
> **Key principle**: Metrics are a means to improvement, not an end. Measure to manage, not to punish."

---

### **CLIMAX: Decision and Quality Failures** (Slides 25-27, ~12 minutes)

#### Slide 25: Case Study - GM Ignition Switch Decision Failure
**Visual:** Timeline of GM ignition switch scandal
**Instructor Script:**
> "Let's analyze a catastrophic failure of both decision-making and quality management: GM ignition switch (2003-2014).
>
> **Background:**
> - 124 deaths, 275 injuries
> - 30 million vehicles recalled
> - $4.1B in costs and settlements
> - Criminal charges against GM
>
> **The problem:**
> Ignition switch could move from 'Run' to 'Accessory' or 'Off' if bumped or with heavy keychain
> → Engine shuts off while driving
> → Power steering and brakes lose assist
> → Airbags disabled (key not in 'Run' position)
>
> **Decision failure #1: Component selection (2002)**
>
> **Trade-off**: Ignition switch torque spec
> - Higher torque = harder to turn, safer (won't slip)
> - Lower torque = easier to turn, more comfortable
>
> **Decision made**: Spec = 15±5 cN·m (very wide tolerance, lower end = 10 cN·m)
> **Decision method**: Supplier recommendation, no systematic MCDA
> **What was missed**: No safety analysis of low torque scenario (FMEA failure)
>
> **Result**: Switches produced at 10 cN·m (low end) → too easy to move accidentally
>
> **Quality failure #1: Inadequate testing**
> - QC testing did not include 'bump' scenario or heavy keychain
> - No validation of worst-case conditions (low torque + vibration + keychain weight)
>
> **Decision failure #2: Engineering change (2006)**
>
> Engineer discovered problem in 2005, authorized supplier to change switch design (increase torque) WITHOUT:
> - Formal change control process
> - New part number (unauthorized, against QMS)
> - Notification to manufacturing or service
>
> **Why this decision was made**: Avoid paperwork and documentation
> **Consequence**: Mix of old (defective) and new (fixed) switches in field, impossible to identify which vehicles have which
>
> **Quality failure #2: No critical parameter management**
> - Ignition switch torque was NOT identified as critical parameter
> - No 100% testing of torque value
> - No statistical process control
>
> **Should have been CTS (Critical-to-Safety)** with tight control and 100% inspection
>
> **Decision failure #3: Response to field reports (2003-2013)**
>
> **Timeline**:
> - 2004: First crash report (airbag didn't deploy)
> - 2005-2007: Multiple reports of stalling, moving ignition
> - 2010: Internal committee reviewed issue → **Decided NOT to recall**
>
> **Trade-off in 2010 decision:**
> - Recall cost: ~$100M (estimated)
> - Liability risk: Unknown
> - Brand reputation: Negative publicity
>
> **Decision made**: Do nothing (no recall)
> **Decision method**: Cost minimization, no systematic risk analysis
> **What was missed**:
> - Safety consequence severely underestimated
> - Liability and brand damage severely underestimated
> - Ethical dimension ignored
>
> **Actual cost**: $4.1B (41× more than recall would have cost)
>
> **Quality failure #3: Metrics didn't surface the problem**
> - Warranty data showed stalling issues, but not aggregated
> - No KPI for 'airbag non-deployment in crashes' (should have been critical safety metric)
> - Data siloed in different departments
>
> **Root causes:**
>
> **Decision-making:**
> - No systematic decision framework (MCDA, risk analysis)
> - Cost prioritized over safety in trade-offs
> - Individual decisions, no oversight or challenge process
> - No documentation of decision rationale
>
> **Quality management:**
> - Critical parameter (ignition torque) not identified
> - QMS violated (unauthorized change, no part number change)
> - Quality gates failed (issue known but not escalated)
> - Metrics didn't track safety-critical parameters
>
> **What should have been done:**
>
> **2002 (Original design):**
> - FMEA identifying low-torque risk
> - Ignition torque designated as CTS parameter
> - Tighter specification (15±2 cN·m)
> - 100% torque testing
>
> **2006 (Change):**
> - Formal ECN (Engineering Change Notice)
> - New part number
> - Field campaign to replace defective switches
>
> **2010 (Field reports):**
> - Systematic decision analysis:
>   - Criteria: Safety, cost, liability, reputation
>   - Weight safety as primary
>   - Decision: Immediate recall
>
> **Lessons learned:**
> 1. Safety must be weighted explicitly in trade-off decisions
> 2. Critical parameters must be identified and controlled
> 3. QMS is non-negotiable - no shortcuts
> 4. Metrics must surface safety issues
> 5. Decision rationale must be documented
> 6. Cost of prevention << cost of failure"

#### Slide 26: Common Decision and Quality Pitfalls
**Visual:** Warning signs with icons
**Instructor Script:**
> "Let me show you the systematic failures to avoid:
>
> **Decision-making pitfalls:**
>
> **Pitfall 1: HiPPO decisions** (Highest Paid Person's Opinion)
> - Senior executive overrides systematic analysis based on intuition
> - Example: 'I drove a competitor's car, we need to match their feature'
> - Fix: Require data-driven justification for overriding analysis
>
> **Pitfall 2: Analysis paralysis**
> - Endless analysis, no decision
> - Fear of making wrong decision → make no decision
> - Fix: Set decision deadlines, 'good enough' threshold
>
> **Pitfall 3: Sunk cost fallacy**
> - 'We've already invested $10M in this architecture, we can't change now'
> - Past costs shouldn't drive future decisions
> - Fix: Evaluate based on future costs/benefits only
>
> **Pitfall 4: Confirmation bias**
> - Seeking data that supports preferred option, ignoring contradictory data
> - Example: Testing scenarios where Option A wins, avoiding scenarios where it fails
> - Fix: Red team review, devil's advocate, pre-commit to decision criteria
>
> **Pitfall 5: Groupthink**
> - Team converges on consensus without critical analysis
> - No one challenges assumptions
> - Fix: Assign explicit challenger role, encourage dissent
>
> **Pitfall 6: Optimizing single criterion**
> - 'Minimize cost' without considering quality, safety, schedule
> - GM ignition switch optimized cost → catastrophe
> - Fix: Multi-criteria decision analysis (MCDA)
>
> **Pitfall 7: Not documenting rationale**
> - Decision made, but reasoning not recorded
> - 2 years later: 'Why did we choose this?'
> - Fix: Decision log with criteria, alternatives, rationale
>
> **Quality management pitfalls:**
>
> **Pitfall 8: Inspection over prevention**
> - Rely on testing to find defects rather than preventing them
> - 'We'll test quality in'
> - Fix: Shift to QA (prevention) - FMEA, design reviews, process improvement
>
> **Pitfall 9: Quality is QA team's job**
> - Engineers think: 'I design, QA ensures quality'
> - Result: Defects designed in, expensive to fix
> - Fix: Quality is everyone's responsibility
>
> **Pitfall 10: Ignoring non-functional requirements**
> - Focus on functional testing, neglect performance, reliability, safety
> - Example: Feature works in ideal conditions, fails in extreme temps
> - Fix: NFR test coverage equal to functional test coverage
>
> **Pitfall 11: No critical parameter identification**
> - Treating all parameters equally
> - Result: Critical safety parameters not controlled
> - Fix: Systematic CPM process (FMEA-driven)
>
> **Pitfall 12: Metrics without action**
> - Dashboards show red KPIs, but no response
> - 'That's just how our metrics always look'
> - Fix: Define triggers and mandatory actions for out-of-spec KPIs
>
> **Pitfall 13: Gaming metrics**
> - Optimizing metric instead of actual quality
> - Example: Closing bugs as 'not reproducible' to hit closure targets
> - Fix: Multiple complementary metrics, audit sample of closed bugs
>
> **Pitfall 14: No lessons learned**
> - Same mistakes repeated across programs
> - No institutional memory
> - Fix: Formal lessons learned process, searchable database, design reviews reference previous failures"

#### Slide 27: Best Practices Summary
**Visual:** Comprehensive checklist
**Instructor Script:**
> "Professional decision and quality management excellence checklist:
>
> **Decision Management Best Practices:**
>
> ✓ **Use systematic decision frameworks**
> - Simple decisions: Weighted scoring
> - Complex decisions: MCDA (AHP, TOPSIS)
> - High uncertainty: Decision trees, scenario analysis
>
> ✓ **Explicitly identify and weight criteria**
> - Include all stakeholder perspectives
> - Safety always weighted significantly
> - Document weighting rationale
>
> ✓ **Generate multiple alternatives**
> - Don't settle for first option
> - Include hybrid approaches
> - Consider 'do nothing' or 'defer' as alternatives
>
> ✓ **Quantify where possible**
> - Use data, simulation, analysis
> - Express uncertainty (ranges, probabilities)
> - Document assumptions
>
> ✓ **Perform sensitivity analysis**
> - Test decision robustness to weight changes
> - Identify critical assumptions
> - Understand decision boundaries
>
> ✓ **Document decision rationale**
> - Decision log: alternatives, criteria, weights, scores, rationale
> - Traceable to requirements and stakeholder needs
> - Reviewable years later
>
> ✓ **Include risk in decision analysis**
> - Probability × impact for uncertain scenarios
> - Risk mitigation options for chosen alternative
> - Contingency plans
>
> ✓ **Use decision governance**
> - Clear decision authority (who decides?)
> - Review and challenge process
> - Escalation path for high-stakes decisions
>
> **Quality Management Best Practices:**
>
> ✓ **Implement QMS** (ISO 9001, IATF 16949)
> - Document processes
> - Train personnel
> - Conduct internal audits
> - Maintain certification
>
> ✓ **Emphasize prevention over detection** (QA > QC)
> - FMEA in design phase
> - Design reviews before implementation
> - Process capability studies
> - Supplier development
>
> ✓ **Identify and control critical parameters**
> - Use FMEA to identify CTS, CTQ, CTF parameters
> - Define specifications with margin
> - Implement control plan (100% inspection or SPC)
> - Monitor trends
>
> ✓ **Implement quality gates**
> - Define entry/exit criteria for each phase
> - Non-negotiable (no gate skipping)
> - Multi-disciplinary review teams
> - Go/Conditional-Go/No-Go decisions
>
> ✓ **Establish effective metrics and KPIs**
> - Leading and lagging indicators
> - SMART criteria
> - Balanced across cost/schedule/quality
> - Actionable decision triggers
>
> ✓ **Create quality culture**
> - Top management commitment
> - Everyone responsible for quality
> - Empowerment to stop production for quality issues
> - Recognition for quality improvements
>
> ✓ **Conduct lessons learned**
> - Formal reviews at phase closures
> - Document failure modes and root causes
> - Share across organization
> - Update standards and processes
>
> ✓ **Maintain traceability**
> - Requirements → Design → Implementation → Tests
> - Critical parameters → Control methods → Records
> - Decisions → Rationale → Outcomes
>
> **Integration of decision and quality:**
> - Quality metrics inform decisions (data-driven)
> - Decisions affect quality outcomes (architecture, supplier, process choices)
> - Both require systematic, documented processes
> - Both require management commitment and cultural support"

---

### **RESOLUTION: Consolidation and Practice** (Slides 28-30, ~8 minutes + Q&A)

#### Slide 28: Key Takeaways
**Visual:** Summary with visual icons
**Instructor Script:**
> "Let's consolidate what you've learned today:
>
> **1. Systematic Decision-Making**
> - Use structured frameworks (MCDA, trade-off analysis)
> - Explicitly identify criteria and weights
> - Document rationale for traceability
> - Consider uncertainty and risk
>
> **2. Multi-Criteria Decision Analysis**
> - WSM: Simple weighted scoring
> - AHP: Pairwise comparisons for weight derivation
> - TOPSIS: Distance to ideal solution
> - Choose method based on decision complexity
>
> **3. Trade-off Analysis**
> - Engineering involves conflicting objectives
> - Pareto frontier identifies optimal solutions
> - Choice among Pareto options depends on values
> - Document trade-offs accepted
>
> **4. Quality Assurance vs Quality Control**
> - QA = Prevention (design it in)
> - QC = Detection (test it out)
> - QA is more cost-effective (10:1 or better)
> - Both are necessary
>
> **5. Critical Parameter Management**
> - Identify vital few (CTS, CTQ, CTF)
> - Define specifications with margin
> - Implement controls (prevention + detection)
> - Monitor and react to excursions
>
> **6. Metrics and KPIs**
> - Measure to manage, not to punish
> - Leading + lagging indicators
> - Balanced scorecard (cost/schedule/quality)
> - Define action triggers
>
> **7. Integration**
> - Good decisions lead to quality outcomes
> - Quality metrics inform better decisions
> - Both require systematic processes and culture
>
> **Remember**: Boeing 737 MAX and GM ignition switch failures weren't due to technical inability - they were failures of decision-making and quality management. You now have the tools to prevent these catastrophes."

#### Slide 29: Connection to Other Sessions and Systems Engineering
**Visual:** Integration diagram with SE processes
**Instructor Script:**
> "Let's place today's learning in the systems engineering context:
>
> **Today (Session 10)**: Decision and Quality Management
>
> **Connections to previous sessions:**
>
> **Session 4 (Requirements):**
> - When stakeholder needs conflict → Decision analysis to prioritize
> - Requirements quality attributes → Quality management
> - Critical requirements → Critical parameters
>
> **Session 5 (Architecture):**
> - Multiple architecture alternatives → MCDA to choose
> - Architecture trade-offs → Pareto analysis
> - Design decisions → Documented rationale
>
> **Session 8 (V&V):**
> - Verification = Quality control (detecting defects)
> - Test coverage = Quality metric
> - Quality gates at each V-model phase
>
> **Session 9 (Risk Management):**
> - Risk informs decisions (uncertain scenarios)
> - FMEA identifies critical parameters
> - Risk metrics = KPIs for program health
>
> **What comes next:**
>
> **Session 11 (Agreement and Infrastructure Management):**
> - Supplier selection = MCDA application
> - Make-vs-buy decisions
> - Supplier quality management
>
> **Session 12 (Safety and Security):**
> - Safety is critical decision criterion
> - Safety integrity levels → Critical parameters
> - Functional safety = Quality management for safety
>
> **Session 15 (Technical Management):**
> - Configuration management supports quality
> - Measurement and analysis = Metrics programs
> - Decision management as technical process
>
> **Throughout SE lifecycle:**
> - Every technical process involves decisions
> - Quality must be managed at every phase
> - Metrics track progress and inform decisions
> - Critical parameters flow from requirements through validation
>
> **Key integration point**: Decision and quality management are ENABLING processes that support all technical processes."

#### Slide 30: Practice Exercise & Q&A
**Visual:** Exercise description
**Instructor Script:**
> "**Practical Exercise (Due before Session 11):**
>
> You are the systems engineer for a new **Advanced Driver Assistance System (ADAS)** that combines Adaptive Cruise Control (ACC) and Lane Keeping Assist (LKA).
>
> **Part 1: Decision Analysis (40%)**
>
> **Scenario**: You must select the primary sensor architecture from three alternatives:
>
> **Option A: Camera-only**
> - Cost: $150 per vehicle
> - Range: 100m
> - Weather performance: Poor (rain/fog degrades)
> - Object classification: Excellent (can read signs, detect pedestrians)
> - Redundancy: Single sensor
>
> **Option B: Radar-only**
> - Cost: $200 per vehicle
> - Range: 200m
> - Weather performance: Excellent (unaffected)
> - Object classification: Poor (detects objects, can't classify type)
> - Redundancy: Single sensor
>
> **Option C: Camera + Radar fusion**
> - Cost: $350 per vehicle
> - Range: 200m (radar determines)
> - Weather performance: Good (radar compensates for camera in bad weather)
> - Object classification: Excellent (camera provides)
> - Redundancy: Dual sensor
>
> **Your task:**
> 1. Define decision criteria (minimum 5)
> 2. Assign weights to criteria (justify based on stakeholder needs)
> 3. Score each alternative on each criterion (1-10 scale, document rationale)
> 4. Calculate using WSM (Weighted Sum Model)
> 5. Perform sensitivity analysis (test 2 different weighting schemes)
> 6. Make recommendation with documented rationale
>
> **Part 2: Trade-off Analysis (20%)**
>
> For your chosen architecture, analyze the trade-off between:
> - System cost (sensor + processing)
> - Performance (detection range, weather capability)
>
> 1. Create trade-off table showing 5 design points
> 2. Plot Pareto frontier
> 3. Explain which point you would select and why
>
> **Part 3: Critical Parameter Management (40%)**
>
> 1. Identify 5 critical parameters for the ADAS system
>    - Classify each as CTS, CTQ, or CTF
>    - Justify criticality (link to safety or performance requirements)
>
> 2. For the TOP 2 critical parameters:
>    - Define specification (nominal ± tolerance)
>    - Describe control method (prevention + detection)
>    - Define monitoring approach and reaction plan if out-of-spec
>
> 3. Define 3 KPIs for tracking ADAS system quality during development
>    - Each must be SMART
>    - Define target value and decision trigger
>
> **Grading Criteria:**
> - Decision analysis: Criteria completeness, weight justification, scoring rationale
> - Trade-off analysis: Correct Pareto identification, clear selection rationale
> - Critical parameters: Appropriate identification, realistic specs, comprehensive controls
> - KPIs: SMART criteria, actionability, alignment with quality objectives
> - Professional presentation: Clarity, formatting, traceability
>
> **Submission**:
> - Part 1: Decision matrix + sensitivity analysis (2 pages)
> - Part 2: Trade-off plot + analysis (1 page)
> - Part 3: Critical parameter table + KPI definitions (2 pages)
> - Total: 5 pages maximum
>
> **Tips:**
> - Research real ADAS systems (Tesla, GM Super Cruise, Mercedes Drive Pilot)
> - Consider ISO 26262 (functional safety) requirements
> - Think about regulatory requirements (Euro NCAP, NHTSA)
> - Reference Session 9 (FMEA) for critical parameter identification
> - Use real data where possible (sensor costs, performance specs)
>
> **Discussion Questions:**
> - How would your decision change if target market is Arizona (sunny) vs Norway (dark, snowy)?
> - What if regulatory requirements mandate redundant sensors for Level 3 autonomy?
> - How do you handle the cost vs safety trade-off?
> - What metrics would indicate your chosen architecture is failing during validation?
>
> **30 minutes for your questions.**"

---

## 📊 PPT DESIGN GUIDANCE

### Visual Style:
- **Professional analytical aesthetic**: Clean, data-driven, decision-oriented
- **Color coding**:
  - Blue for Decision Analysis
  - Green for Quality Assurance (prevention)
  - Orange for Quality Control (detection)
  - Red for critical parameters and warnings
  - Purple for metrics/KPIs
- **Use real automotive examples**: Photos of decision boards, quality control stations, dashboards
- **Diagrams**: Decision trees, Pareto frontiers, control charts, KPI dashboards

### Key Slides to Emphasize:
1. **Slide 4** (Boeing 737 MAX) - Grabs attention with real consequences
2. **Slide 8** (Decision process) - Systematic framework
3. **Slide 12** (WSM example) - Practical application students will use
4. **Slide 15** (Pareto frontier) - Core trade-off concept
5. **Slide 18** (QA vs QC) - Critical distinction
6. **Slide 21** (Critical parameters) - Automotive application
7. **Slide 25** (GM ignition switch) - Comprehensive failure analysis
8. **Slide 28** (Summary) - Students will photograph this

### Animations:
- **Slide 6**: Build battery options table row by row
- **Slide 12**: Highlight each criterion, then show weighted calculation step-by-step
- **Slide 15**: Animate Pareto frontier curve, highlight dominated solutions
- **Slide 18**: Split-screen animation showing QA (prevention) vs QC (detection) timeline
- **Slide 25**: Timeline animation of GM ignition switch decision points and consequences

### Tables and Templates:
- **Slide 6**: Battery comparison table (complete with real specs)
- **Slide 12**: Full WSM calculation example (3 alternatives × 5 criteria)
- **Slide 22**: Control plan example (automotive battery assembly)
- **Slide 23**: KPI dashboard with RAG status

### Real Examples to Include:
- Actual MCDA studies from automotive industry (if public)
- ISO 9001/IATF 16949 certification audit checklists
- Real control plans from PPAP submissions
- Actual automotive KPI dashboards (anonymized)
- Cost of quality data from automotive industry

---

## 🎯 INSTRUCTOR NOTES

### Pedagogical Strategy:
- **Start with crisis (Boeing 737 MAX), show systematic solution, return to preventing crisis**
- **Balance theory (MCDA methods) with practice (worked examples)**
- **Emphasize decision documentation and traceability**
- **Connect decision quality to system quality**
- **Use automotive examples throughout**

### Common Student Challenges:

**Challenge 1: "Why not just use intuition for decisions?"**
**How to address:** Show Slide 4 (Boeing) and Slide 25 (GM) - intuition failed catastrophically. Emphasize: Intuition for simple decisions is fine; complex multi-stakeholder decisions need systematic analysis. Systematic doesn't mean slow - WSM takes 30 minutes for a well-scoped decision.

**Challenge 2: "MCDA seems complicated and time-consuming"**
**How to address:** Show Slide 12 (WSM) - simple spreadsheet, 1-2 hours for important decision. Compare to cost of wrong decision (GM: $4.1B). Frame as insurance. Not every decision needs MCDA - use for Type 2/3 decisions (Slide 9).

**Challenge 3: "How do we decide the weights in MCDA?"**
**How to address:** Weights reflect stakeholder values. Use AHP (pairwise comparison) if direct weighting is difficult. Show sensitivity analysis - if decision is same across reasonable weight ranges, weights don't matter much. If decision flips with small weight changes, need careful stakeholder negotiation.

**Challenge 4: "QA sounds good, but we don't have time for prevention"**
**How to address:** Show cost multipliers (Slide 18): Prevention $1, Appraisal $10, Failure $100, Recall $10,000. Ask: "Can you afford NOT to do prevention?" QA is faster than fixing defects later. FMEA takes 2 days, but prevents 6 months of rework.

**Challenge 5: "We track metrics but nothing changes"**
**How to address:** Slide 24 - metrics without action are waste. Define triggers and mandatory actions. Example: Defect density >0.5 → trigger additional design review. Make metrics part of governance, not just dashboards.

### Timing Flexibility:

**If running short:**
- Condense Slide 13 (AHP) - mention it exists, focus on WSM
- Reduce Slide 14 (TOPSIS) to brief overview
- Move some trade-off examples to backup slides

**If running long:**
- Extend Slide 12 (WSM) with live calculation exercise (students participate)
- Add interactive exercise: Give students a simple decision, have them do WSM
- Show actual MCDA software demo (Expert Choice, AHP-OS)

**Core content (must cover - non-negotiable):**
- Slides 8-12 (Decision process, types, MCDA/WSM)
- Slides 15-17 (Trade-offs and Pareto)
- Slides 18-20 (QA vs QC, QMS, quality gates)
- Slides 21-22 (Critical parameters)
- Slide 23 (Metrics and KPIs)
- Slides 25-26 (Failure case studies and pitfalls)
- Slide 28 (Summary)

### Engagement Points:

**Slide 6**: Interactive - poll students: "Which battery would you choose?" before showing analysis. See how many choose differently and why.

**Slide 12**: Work through WSM together - have students suggest criteria and weights, calculate together.

**Slide 18**: Quick quiz - show 5 activities, ask students to classify as QA or QC.

**Slide 25**: Case study discussion - "At what point should GM have recalled? What decision framework would have led to the right choice?"

**Slide 27**: Pair exercise - give pairs 3 minutes to identify which pitfalls their organization/project exhibits. Share anonymously.

### Interactive Elements:

**Quick Poll (Slide 3)**: "How many have seen important decisions made without systematic analysis?" (normalize the problem)

**Decision Exercise (Slide 12)**: Give students battery decision, 5 minutes to score one alternative, compare results, discuss variance.

**QA vs QC Quiz (Slide 18)**: Present 6 activities, students vote QA or QC, discuss.

**Metrics Design (Slide 24)**: Small groups design 2 KPIs for a given system, share, critique.

### Materials to Prepare:

**Before class:**
- [ ] WSM calculation spreadsheet template (for students)
- [ ] Example AHP pairwise comparison matrix
- [ ] Real control plan example (anonymized)
- [ ] KPI dashboard template
- [ ] Decision log template

**Handouts:**
- [ ] Decision analysis process checklist
- [ ] WSM template (Excel)
- [ ] Critical parameter identification worksheet
- [ ] QA vs QC comparison table
- [ ] SMART KPI criteria checklist

**Post-class:**
- [ ] Share slides
- [ ] Post exercise assignment with templates
- [ ] Post WSM and AHP templates
- [ ] Share links to: ISO 9001, IATF 16949, AIAG FMEA handbook
- [ ] Create discussion forum: "Share a bad decision you've witnessed and how MCDA would have helped"

### Assessment Opportunities:

**During lecture:**
- Quick quiz (Slide 9): "What decision method for supplier selection with 15 candidates and 8 criteria?"
- Quick quiz (Slide 18): "Is FMEA a QA or QC activity? Why?"

**Exercise assessment criteria:**
- Decision analysis: Are criteria comprehensive? Weights justified? Scores documented? Sensitivity analysis performed?
- Trade-off analysis: Correct Pareto identification? Clear selection rationale?
- Critical parameters: Appropriately identified? Linked to FMEA/requirements? Realistic control methods?
- KPIs: Meet SMART criteria? Actionable? Aligned with objectives?

**Common student mistakes to watch for:**
- Assigning weights without justification
- Not documenting scoring rationale
- Confusing dominated solutions with Pareto optimal
- Identifying too many parameters as "critical" (critical means vital few, not everything)
- Defining vanity metrics instead of actionable KPIs
- Not linking critical parameters to requirements or FMEA

---

## ✅ Session Success Criteria

Students leave able to:
- ✓ Apply systematic decision analysis to engineering trade-offs
- ✓ Use Weighted Sum Model (WSM) for multi-criteria decisions
- ✓ Identify and visualize trade-offs using Pareto frontier
- ✓ Distinguish between QA (prevention) and QC (detection)
- ✓ Identify critical parameters for automotive systems
- ✓ Define SMART KPIs for systems engineering programs
- ✓ Recognize decision and quality management failures
- ✓ Document decision rationale for traceability

**Critical outcome:** Students can **make and defend complex engineering decisions** using systematic methods and **implement quality management** to prevent defects, not just detect them.

**Evidence of success:**
- Student can perform WSM calculation for multi-criteria decision
- Student can explain why QA is more cost-effective than QC
- Student can identify critical parameters from FMEA and define control methods
- Student can define actionable KPIs with decision triggers
- Student understands that decision quality and product quality are interlinked

---

## 📚 Additional Resources for Students

**Standards and Guidelines:**
- ISO 9001:2015: Quality Management Systems - Requirements
- IATF 16949:2016: Automotive Quality Management System Requirements
- ISO 26262-8:2018: Functional Safety - Supporting Processes
- AIAG FMEA Handbook (5th Edition)
- AIAG PPAP Manual (Production Part Approval Process)

**Decision Analysis:**
- Keeney, R.L. & Raiffa, H.: "Decisions with Multiple Objectives: Preferences and Value Trade-offs"
- Saaty, T.L.: "Decision Making with the Analytic Hierarchy Process"
- Triantaphyllou, E.: "Multi-Criteria Decision Making Methods: A Comparative Study"

**Quality Management:**
- Juran's Quality Handbook (7th Edition)
- "Out of the Crisis" by W. Edwards Deming
- "The Toyota Way" by Jeffrey Liker
- ASQ Certified Quality Engineer Handbook

**Automotive-Specific:**
- APQP Manual (Advanced Product Quality Planning) - AIAG
- ASPICE (Automotive SPICE) - Process Assessment Model
- VDA 6.3 - Process Audit

**Online Tools:**
- AHP-OS (free online AHP calculator)
- Super Decisions (free AHP software)
- Minitab / JMP (statistical analysis for quality metrics)

---

## 🔗 Connections to Other Sessions

**Builds on:**
- **Session 4**: Requirements provide criteria for decisions; quality requirements drive critical parameters
- **Session 5**: Architecture selection is MCDA application; design quality gates
- **Session 8**: V&V is quality control; traceability enables quality management
- **Session 9**: Risk analysis informs decisions; FMEA identifies critical parameters

**Leads to:**
- **Session 11**: Supplier selection uses MCDA; supplier quality management
- **Session 12**: Safety is critical decision criterion; safety = quality for life-critical systems
- **Session 15**: Configuration management supports quality; measurement = metrics implementation

**Key concept thread:**
- **Session 9**: HOW do we manage risk? (FMEA, risk analysis)
- **Session 10**: HOW do we make decisions and ensure quality? (This session)
- **Session 11**: HOW do we manage agreements and infrastructure? (Supplier/resource decisions)
- **Session 15**: HOW do we manage information and configuration? (Technical management)

**Decision-making appears in:**
- Session 5 (Architecture selection)
- Session 11 (Make-vs-buy, supplier selection)
- Session 13 (Life cycle cost trade-offs)
- Every session implicitly (engineering is decision-making)

**Quality management appears in:**
- Session 8 (V&V processes)
- Session 12 (Functional safety quality requirements)
- Session 15 (Quality of technical management processes)

---

## 🎬 Opening and Closing Strategies

### **Opening (First 2 minutes):**
Start with Boeing 737 MAX image on screen as students enter. Begin:

> "Before we start, look at this aircraft. Boeing 737 MAX. 346 people died. $20 billion in losses. 20-month grounding.
>
> This wasn't a technology failure. Boeing knows how to build aircraft. This was a failure of decision-making and quality management.
>
> Today, we're going to learn how to make systematic, defensible decisions and how to build quality in from the start. Because in automotive, the stakes are just as high - and you will be making these decisions.
>
> Welcome to Session 10: Decision and Quality Management."

### **Closing (Last 2 minutes):**
Return to the opening images (Boeing and GM):

> "We started with two catastrophic failures: Boeing 737 MAX and GM ignition switch. Both resulted from failures you now know how to prevent:
>
> - You can make systematic decisions using MCDA
> - You can analyze trade-offs and choose from Pareto frontier
> - You can distinguish QA from QC and emphasize prevention
> - You can identify and control critical parameters
> - You can define metrics that drive improvement
>
> The exercise I've given you is your chance to practice. When you're faced with a real decision - sensor architecture, supplier selection, architecture choice - you'll have systematic methods.
>
> Quality and decisions aren't separate from engineering - they ARE engineering. Make them count.
>
> See you in Session 11, where we'll apply these decision methods to supplier selection and make-vs-buy decisions."

---

## 📈 Learning Objectives Mapping to Assessment

| Session Objective | Assessment Method | Success Criteria |
|-------------------|-------------------|------------------|
| Apply decision analysis techniques | Exercise Part 1 | Correctly applies WSM with documented criteria, weights, scores |
| Use MCDA for complex decisions | Exercise Part 1 | Complete decision matrix with sensitivity analysis |
| Distinguish QA vs QC | In-class quiz + conceptual understanding | Can classify activities correctly; explains prevention vs detection |
| Implement critical parameter management | Exercise Part 3 | Identifies appropriate critical parameters linked to FMEA/requirements; defines realistic controls |
| Define metrics and KPIs | Exercise Part 3 | KPIs meet SMART criteria; actionable decision triggers defined |
| Recognize decision/quality failures | Case study discussion | Can analyze GM/Boeing cases; identifies root causes |
| Select appropriate decision frameworks | Exercise Part 1 + in-class discussion | Chooses method appropriate to decision type; justifies choice |

---

**End of Session 10 Framework**
**Next:** Session 11 (Agreement and Infrastructure Management)
