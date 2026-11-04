# Session 9: Project and Risk Management
## Detailed Case Study Guide - Automotive Applications

**Purpose:** This guide provides three current, relevant case studies to replace/supplement the Mars Climate Orbiter case in Session 9, making the content more engaging for automotive engineering students.

**Case Studies:**
1. **Tesla Cybertruck Production Delays** - Project Planning Process
2. **Ford F-150 Lightning Battery Crisis** - Risk Management Process
3. **EV Battery Supply Chain** - Opportunity Management & Resilience

**Duration:** 120 minutes total
**Approach:** Multi-case study integration with each case highlighting different PM/RM aspects

---

## LECTURE FLOW OVERVIEW

### Opening (5 min) - Slides 1-3
- **Keep:** Mars Climate Orbiter as cross-industry hook
- **Add:** Transition to three automotive cases from 2019-2024

### Project Planning (25 min) - Slides 9-14
- **Primary Case:** Tesla Cybertruck

### Risk Management (30 min) - Slides 15-22
- **Primary Cases:** Ford F-150 Lightning (Slides 15-19) + EV Supply Chain (Slides 20-22)

### Automotive Applications (15 min) - Slides 23-26
- **Integration:** All three cases

### Wrap-up (15 min) - Slides 27-30
- **Synthesis:** Lessons across all cases

---

# CASE STUDY 1: TESLA CYBERTRUCK PRODUCTION DELAYS
**Use for: PROJECT PLANNING PROCESS (Slides 9-14)**

## 1.1 Case Overview

### Timeline of Events

**November 21, 2019 - The Reveal**
- Elon Musk unveils Cybertruck at Tesla Design Studio
- Promises three variants: Single Motor, Dual Motor, Tri Motor
- **Promised delivery:** Late 2021 (Tri Motor), Mid 2022 (Dual), Late 2022 (Single)
- Pre-orders: 250,000+ in first week
- Price: Starting at $39,900

**2020-2021 - Development Phase**
- Design refinements and engineering development
- Multiple design changes announced (size reduction, feature additions)
- Battery 4680 cell development begins
- New manufacturing processes required for stainless steel body

**2022 - First Delays**
- Production pushed to 2023
- Cybertruck spotted in testing
- Focus shifts to ramping Model Y and Semi production
- Battery 4680 production struggles

**2023 - Limited Production**
- **July 2023:** First Cybertruck rolls off production line (internal delivery)
- **November 30, 2023:** Official delivery event - **4 YEARS after announcement**
- Initial deliveries: ~10 vehicles to employees
- Production rate: <10 per day initially

**2024 - Production Ramp Struggles**
- Q1 2024: ~1,000 units delivered
- Production challenges with exoskeleton manufacturing
- Price increases: Foundation Series at $99,990 (150% higher than promised)
- Estimated full production: Late 2024/Early 2025

### Key Metrics

| Metric | Original Plan | Actual Result | Variance |
|--------|--------------|---------------|----------|
| **Announcement to Delivery** | 24 months | 48 months | **+100%** |
| **Production Start** | Late 2021 | Nov 2023 | **+24 months** |
| **Initial Volume Target** | 250,000/year by 2024 | ~5,000 in 2023 | **-98%** |
| **Starting Price** | $39,900 | $99,990 (Foundation) | **+150%** |
| **Development Cost** | Est. $2-3B | Est. $5-7B | **+100-133%** |
| **R&D Timeline** | 18-24 months | 36-48 months | **+100%** |

### Root Causes of Delays

**1. Design Complexity**
- Ultra-hard 30X cold-rolled stainless steel exoskeleton
- No traditional stamping process works
- Requires precision folding (tolerances ±10 microns vs. ±1mm typical)
- New manufacturing processes invented during development

**2. Technology Dependencies**
- 4680 battery cell production delays
- 48V electrical architecture (industry first)
- Steer-by-wire system (automotive first in trucks)
- New structural battery pack design

**3. Manufacturing Challenges**
- Cybertruck-specific production line required
- Cannot use existing Model 3/Y assembly processes
- Gigafactory Texas capacity constraints
- Supplier readiness for novel components

**4. Scope Creep**
- Size reduction (originally 20% larger)
- Feature additions (rear-wheel steering, range extender)
- Design changes based on testing feedback
- Regulatory compliance requirements discovered late

**5. Resource Constraints**
- Battery production prioritized for Model Y/3 (higher margin)
- Engineering resources split across Semi, Roadster, FSD
- Capital allocation to Gigafactory expansions
- Supply chain challenges (chips, batteries, steel)

**6. Market/Strategic Shifts**
- 2021-2022: Focus on Model Y ramp (higher priority)
- 2022: Macroeconomic concerns, demand uncertainty
- 2023: Focus on margin over volume

---

## 1.2 Integration with PROJECT PLANNING PROCESS

### Slide 9: Project Planning Process - Overview

**Instructor Narration (Add after standard content):**

> "Let me show you a real automotive example that illustrates what happens when project planning fails. Tesla Cybertruck. Announced November 2019. Promised delivery in 2021. Actually delivered? November 2023—**four years late**. Production ramp? Still struggling in 2024.
>
> This wasn't a technology company that doesn't understand manufacturing. This was Tesla—the company that revolutionized EV production. What went wrong? Let's analyze it through the Project Planning Process."

**PPT Addition:**
```
CASE STUDY: Tesla Cybertruck Project Planning Failure

ANNOUNCED: Nov 21, 2019
PROMISED DELIVERY: Late 2021 (24 months)
ACTUAL DELIVERY: Nov 30, 2023 (48 months)

SCHEDULE DELAY: +100% (24 months late)
COST OVERRUN: Estimated +100-130% ($5-7B vs $2-3B)
VOLUME MISS: 98% below target (5,000 vs 250,000 units)
PRICE INCREASE: +150% ($100K vs $40K starting price)

ROOT CAUSE CATEGORY: Project Planning Failures
→ We'll analyze exactly what went wrong and how to prevent it
```

**Learning Connection:** LO1, LO2 - SE project planning failures

---

### Slide 10: Work Breakdown Structure (WBS) - Foundation of Planning

**After teaching WBS fundamentals, add:**

**Instructor Narration:**

> "Let's build a simplified WBS for the Cybertruck program and identify where complexity was underestimated.
>
> **Level 1: Cybertruck Program**
>
> **Level 2: Major subsystems**
> 1. Body Structure (Exoskeleton)
> 2. Propulsion System (Tri-motor + 4680 battery)
> 3. Electrical Architecture (48V system)
> 4. Chassis & Suspension (Active suspension + steering)
> 5. Manufacturing & Tooling
> 6. Software & Electronics
> 7. Certification & Compliance
>
> Now, here's where it gets interesting. Let's decompose **Body Structure**:
>
> **Level 3: Body Structure decomposition**
> - 3.1 Stainless Steel Exoskeleton Design
>   - 3.1.1 Material selection (30X cold-rolled SS)
>   - 3.1.2 Structural analysis & crash testing
>   - 3.1.3 Tolerance definition (±10 microns!)
> - 3.2 Manufacturing Process Development
>   - 3.2.1 Precision folding process (doesn't exist for this material)
>   - 3.2.2 Tooling design & procurement
>   - 3.2.3 Joining methods (no spot welding possible)
>   - 3.2.4 Surface finishing (no paint, scratches show)
> - 3.3 Assembly Integration
>   - 3.3.1 Mating to chassis
>   - 3.3.2 Panel gap management
>   - 3.3.3 Quality control methods
>
> **The Planning Failure:**
>
> In 2019, Tesla likely estimated body development at 12-18 months based on traditional automotive WBS templates. But they underestimated THREE critical factors:
>
> 1. **Work Package Complexity:** Manufacturing processes had to be *invented*—not just adapted. 3.2.1 alone took 18+ months.
>
> 2. **Dependency Chains:** Can't design assembly until manufacturing process is defined. Can't order tooling until process is proven. Sequential dependencies multiplied timeline.
>
> 3. **Risk Buffers:** No contingency for 'process doesn't exist yet' scenario.
>
> **The lesson:** When your WBS includes work packages with no precedent, your estimates are guesses. Build in research/discovery phases explicitly."

**PPT Content:**
```
CYBERTRUCK WBS - BODY STRUCTURE BREAKDOWN

LEVEL 1: Cybertruck Program

LEVEL 2: Body Structure (Exoskeleton)
├─ Stainless Steel Exoskeleton Design
├─ Manufacturing Process Development ⚠️ CRITICAL PATH
└─ Assembly Integration

LEVEL 3: Manufacturing Process Development (EXPANDED)
├─ 3.2.1 Precision Folding Process Development
│   ├─ Material behavior research
│   ├─ Prototype tooling
│   ├─ Process validation
│   └─ Production tooling design
│   ESTIMATE: 6-12 months → ACTUAL: 18-24 months ⚠️
│
├─ 3.2.2 Joining Methods (no welding possible)
│   ├─ Adhesive bonding research
│   ├─ Mechanical fastening design
│   └─ Structural testing
│   ESTIMATE: 3-6 months → ACTUAL: 12-18 months ⚠️
│
└─ 3.2.3 Quality Control Methods
    ├─ Measurement systems (micron-level)
    ├─ Inspection processes
    └─ Rework procedures
    ESTIMATE: 2-4 months → ACTUAL: 6-12 months ⚠️

WBS PLANNING FAILURES:
✗ Assumed existing processes could be adapted
✗ Underestimated "invent new process" complexity
✗ No explicit WBS for R&D/discovery work
✗ Insufficient contingency for unknowns
✗ Dependencies between work packages not analyzed

CORRECT APPROACH:
✓ Separate WBS for "Research & Process Development"
✓ Explicit work packages for "Invent new method"
✓ Build dependencies into schedule
✓ Add contingency buffers for R&D work
✓ Plan for iterative prototype-test-refine cycles

→ WBS complexity drives schedule and cost
```

**Discussion Prompt:**
> "If you were the SE lead in 2019, what questions would you ask about the exoskeleton WBS that might have revealed the underestimation?"

**Expected Answers:**
- "Has this manufacturing process been done before?"
- "What's the technology readiness level of the body manufacturing?"
- "What are the dependencies between process development and production tooling?"
- "What's our contingency if the process doesn't work as planned?"

**Learning Connection:** LO2 - Applying WBS to automotive programs; LO3 - Understanding complexity impacts

---

### Slide 11: Scheduling - Sequencing and Dependencies

**After teaching scheduling fundamentals (Gantt, CPM, dependencies), add:**

**Instructor Narration:**

> "Let's analyze Cybertruck's critical path and understand why a 2-year delay was almost inevitable.
>
> **Original Schedule (2019 Estimate):**
> - Design freeze: Q2 2020 (6 months)
> - Manufacturing process development: Q3-Q4 2020 (6 months) ⚠️
> - Tooling procurement: Q1 2021 (3 months)
> - Pilot production: Q2 2021 (3 months)
> - Production ramp: Q3 2021 onwards
> - **Target delivery: Late 2021 (24 months total)**
>
> **Critical Path Identified: Battery 4680 + Manufacturing Process**
>
> Now, here's what actually happened:
>
> **Actual Schedule:**
> - Design iterations: Q2 2020 - Q4 2021 (18 months) — *Slipped due to size changes, regulatory issues*
> - Manufacturing process development: Q1 2021 - Q4 2022 (24 months) — **Critical path, 4x longer than estimated**
> - Tooling procurement: Q1 2023 - Q3 2023 (9 months) — *Couldn't start until process proven*
> - Pilot production: Q3 2023 (3 months)
> - Limited production start: Nov 2023
> - **Actual delivery: November 2023 (48 months total)**
>
> **Critical Path Analysis:**
>
> The critical path was **Manufacturing Process Development** → **Tooling** → **Production Ramp**.
>
> When manufacturing process slipped from 6 months to 24 months (+18 months), everything downstream shifted. But here's the key failure:
>
> **Tesla scheduled tooling procurement in parallel with process development.** Classic schedule compression technique. But it backfired because:
>
> 1. **Finish-to-Start Dependency Violated:** You can't order production tooling until you know the production process. They had to re-order tooling multiple times.
>
> 2. **Fast-Tracking Gone Wrong:** Overlapping dependent activities created rework loops.
>
> 3. **No Schedule Contingency:** The 6-month process development estimate had zero buffer for 'inventing new processes.'
>
> **The Correct Approach:**
>
> Recognize 'process development' as R&D work with high uncertainty:
> - Use **range estimation**: Optimistic 6 months, Most Likely 12 months, Pessimistic 24 months
> - PERT Expected Duration: (6 + 4×12 + 24) / 6 = **13 months**
> - Add 20% contingency buffer: **16 months**
> - Schedule tooling as **Finish-to-Start** after process validated, not parallel
>
> That would have given a realistic delivery target of **Late 2022** instead of Late 2021. Still late, but honest planning."

**PPT Content:**
```
CYBERTRUCK SCHEDULE ANALYSIS - CRITICAL PATH FAILURE

ORIGINAL PLAN (2019):
─────────────────────────────────────────────────────
Design Freeze          [6 months]
  ↓ (FS)
Mfg Process Dev        [6 months] ⚠️ CRITICAL PATH
  ↓ (FS → violated!)
Tooling Procurement    [3 months]  (started parallel - ERROR)
  ↓ (FS)
Pilot Production       [3 months]
  ↓ (FS)
Production Ramp        [6 months]
─────────────────────────────────────────────────────
TOTAL: 24 months → Delivery Late 2021 ✓ Announced

ACTUAL TIMELINE:
─────────────────────────────────────────────────────
Design Iterations      [18 months] +12 months
  ↓ (FS)
Mfg Process Dev        [24 months] ⚠️ +18 months (4x estimate!)
  ↓ (FS)
Tooling Procurement    [9 months]  +6 months (re-orders)
  ↓ (FS)
Pilot Production       [3 months]  On time
  ↓ (FS)
Production Ramp        [Ongoing]   Struggling in 2024
─────────────────────────────────────────────────────
TOTAL: 48+ months → Delivery Nov 2023 ✗ 24 months late

CRITICAL PATH FAILURES:

1. ESTIMATION FAILURE
   ✗ Process development: 6 months estimated
   ✗ No precedent for this process
   ✗ Should have used 3-point estimation:
     • Optimistic: 6 months
     • Most Likely: 12 months
     • Pessimistic: 24 months
     • PERT: (6+4×12+24)/6 = 13 months
   ✗ Add 20% buffer → 16 months realistic

2. DEPENDENCY VIOLATION
   ✗ Tooling scheduled parallel to process dev
   ✓ Should be Finish-to-Start dependency
   ✗ Result: Tooling re-ordered multiple times
   ✗ Wasted cost + added 6 months

3. FAST-TRACKING RISK
   ✗ Compressed schedule by overlapping activities
   ✗ Created rework loops
   ✗ Increased cost and time

4. NO SCHEDULE CONTINGENCY
   ✗ Zero buffer for R&D work
   ✗ Assumed everything goes perfectly
   ✗ No risk-adjusted schedule

CONCURRENT BOTTLENECK: 4680 Battery Cell Production
─────────────────────────────────────────────────────
│ Battery 4680 Development │ [24+ months, ongoing struggles]
└─ Needed for Cybertruck powertrain
└─ Parallel critical path
└─ Also delayed 18+ months

SCHEDULE COMPRESSION TECHNIQUES (Used Incorrectly):
× Fast-Tracking: Overlap dependent activities
  → Created rework, extended duration
× Crashing: Add resources to shorten duration
  → Can't crash R&D work effectively

CORRECT SCHEDULING APPROACH:
✓ Identify true critical path (Mfg Process Dev)
✓ Use probabilistic estimation for R&D work
✓ Maintain Finish-to-Start dependencies
✓ Build schedule contingency (15-20%)
✓ Separate committed dates from target dates
✓ Plan review gates before major investments

LESSON FOR STUDENTS:
"Aggressive schedules don't make work go faster.
They just make delays more catastrophic and expensive."

→ Schedule realism > Schedule optimism
```

**Activity for Students (5 min):**

> "Turn to your neighbor. You're the SE project manager in 2019. Your CEO announces Cybertruck will deliver in 2 years. Your engineering team says the exoskeleton process needs invention. What do you do?
>
> A) Push the team to meet the 2-year deadline
> B) Provide leadership with a risk-adjusted schedule (3 years)
> C) Agree to 2 years publicly, plan for 3 years privately
> D) Build a parallel backup design using conventional processes
>
> Discuss: What are the consequences of each choice?"

**Debrief (2 min):**
- **A:** Team burns out, quality suffers, deadline still missed, credibility destroyed
- **B:** Honest, but may lose executive support or market excitement
- **C:** Dishonest, creates internal distrust, leads to chaos when delays surface
- **D:** Expensive but manages risk; dual-track approach for high-uncertainty projects

**Correct Answer:** B with elements of D. "Provide honest schedule with risk analysis. If executive insists on aggressive target, propose parallel risk mitigation approach (e.g., backup conventional design). Never commit to a schedule you know is impossible."

**Learning Connection:** LO1, LO2, LO3 - Critical path analysis, dependency management, risk-adjusted scheduling

---

### Slide 12: Resource Allocation - People, Budget, Tools

**After teaching resource allocation concepts, add:**

**Instructor Narration:**

> "Resource allocation isn't just about having enough people and money. It's about **priority allocation** when resources are constrained. Tesla faced a classic resource allocation dilemma with Cybertruck.
>
> **The Resource Constraint (2021-2023):**
>
> Tesla had finite resources:
> - **Battery Production Capacity:** Limited 4680 cell output from Texas Gigafactory
> - **Engineering Talent:** Finite number of senior engineers
> - **Capital:** Limited funds for new production lines
> - **Manufacturing Capacity:** Shared Gigafactory Texas with Model Y
>
> **The Allocation Decision:**
>
> | Resource | Cybertruck Need | Model Y Need | Decision |
> |----------|----------------|--------------|----------|
> | **4680 Batteries** | 150 kWh pack | 75 kWh pack | **Allocate to Model Y** (2x units per kWh) |
> | **Engineering** | Exoskeleton development | Production ramp support | **Split team, prioritize Model Y** |
> | **CapEx** | Cybertruck tooling | Model Y capacity expansion | **Prioritize Model Y** (proven demand) |
> | **Factory Floor** | Cybertruck assembly line | Model Y expansion | **Prioritize Model Y** (higher margin) |
>
> **Why Model Y Won:**
> - **Margin:** Model Y gross margin ~25%, Cybertruck unknown (likely lower due to complexity)
> - **Volume:** Model Y demand proven (1M+ units/year), Cybertruck uncertain
> - **Risk:** Model Y using proven manufacturing, Cybertruck high technical risk
> - **Cash Flow:** Model Y generates immediate revenue, Cybertruck deferred
>
> **Result:** Cybertruck starved of resources from 2021-2023, extending delays.
>
> **The SE Project Management Perspective:**
>
> This wasn't irrational. This was **portfolio resource optimization**. But it created a cascading problem:
>
> 1. **2019:** Announce Cybertruck, promise 2021 delivery
> 2. **2020-2021:** Allocate resources based on business priority (Model Y wins)
> 3. **2021:** Cybertruck delays due to resource constraints
> 4. **2022:** Public credibility damaged by delays
> 5. **2023:** Finally allocate resources when Model Y stable
>
> **What Should Have Happened:**
>
> **Option 1: Honest Resource Planning**
> - 2019: Recognize resource constraints
> - Plan Cybertruck schedule *assuming* Model Y priority
> - Announce realistic 2023-2024 delivery
> - Manage expectations from day one
>
> **Option 2: Ring-Fence Resources**
> - Commit dedicated battery allocation to Cybertruck
> - Separate engineering teams (no borrowing)
> - Dedicate CapEx budget
> - Accept slower Model Y ramp
>
> **Option 3: Phase Gate Resource Allocation**
> - 2019-2020: R&D phase with limited resources
> - Gate decision: Prove exoskeleton process
> - 2021+: Full resource allocation only after gate passed
> - Deferred public announcement until gate passed
>
> **Tesla chose none of these.** They announced aggressively, then reallocated resources to business priorities, creating the worst outcome: **missed commitments + damaged credibility + extended delays.**"

**PPT Content:**
```
CYBERTRUCK RESOURCE ALLOCATION FAILURE

RESOURCE CONSTRAINT SCENARIO (2021-2023):
─────────────────────────────────────────────────────
FINITE RESOURCES AT TESLA:
• 4680 Battery Production: 10 GWh/year capacity
• Senior Engineering Talent: ~500 engineers
• Capital Budget: $5B/year for all programs
• Gigafactory Texas Floor Space: Shared facility

COMPETING PROGRAMS:
├─ Model Y (Proven, High Volume, Immediate Revenue)
├─ Cybertruck (Unproven, Uncertain Demand, Deferred Revenue)
├─ Semi Truck (Fleet sales, Strategic)
└─ Robotaxi/FSD (Strategic moonshot)

RESOURCE ALLOCATION DECISION MATRIX:

Resource Type    │ Cybertruck │ Model Y │ Decision    │ Impact
─────────────────┼────────────┼─────────┼─────────────┼─────────
4680 Batteries   │ Need 150kWh│ Need 75kWh│ → Model Y │ 2x units
(10 GWh/year)    │ per truck  │ per car  │           │ per GWh
                 │            │          │           │
Engineering      │ Need 200   │ Need 150 │ → Split   │ Cybertruck
Talent           │ (novel dev)│ (ramp)   │ 60/40 MY  │ slowed
                 │            │          │           │
Capital Budget   │ Need $2B   │ Need $3B │ → Model Y │ Tooling
($5B total)      │ (tooling)  │ (expansion)│ priority │ delayed
                 │            │          │           │
Factory Space    │ Need 20%   │ Need 60% │ → Model Y │ Cybrtrk
(Giga Texas)     │ (assy line)│ (volume) │ expansion │ deferred

BUSINESS LOGIC (CFO View):
─────────────────────────────────────────────────────
Model Y Allocation ROI:
• Gross Margin: 25-30%
• Proven Demand: 1,000,000+ units/year
• Revenue: $50B+/year potential
• Cash Flow: Immediate (2021+)
• Risk: Low (proven manufacturing)

Cybertruck Allocation ROI:
• Gross Margin: Unknown (15-20% estimated, could be negative)
• Unproven Demand: 1.5M reservations ($100 deposits, ~50% real)
• Revenue: $10-20B/year potential (if achieves volume)
• Cash Flow: Deferred (2023+)
• Risk: High (unproven manufacturing, technology)

→ MODEL Y WINS ON EVERY METRIC

ACTUAL RESOURCE ALLOCATION (2021-2023):
─────────────────────────────────────────────────────
4680 Batteries:    80% Model Y | 15% Semi | 5% Cybertruck
Engineering:       60% Model Y | 25% FSD  | 15% Cybertruck
Capital:           65% Model Y | 20% Expansion | 15% Cybertruck
Factory Space:     70% Model Y | 20% Buffer | 10% Cybertruck

RESULT: Cybertruck resource-starved from 2021-2023
→ Development slowed
→ Tooling procurement delayed
→ Production ramp postponed
→ Delivery pushed to late 2023

THE PROJECT MANAGEMENT FAILURE:

✗ COMMITMENT WITHOUT RESOURCES
  • 2019: Announced 2021 delivery (public commitment)
  • 2021: Allocated resources to Model Y (business priority)
  • Result: Impossible to meet commitment

✗ NO RESOURCE LOADING ANALYSIS
  • Didn't model resource demand across all programs
  • Assumed resources would be available when needed
  • Didn't identify resource conflicts in planning phase

✗ OPTIMISTIC RESOURCE ASSUMPTIONS
  • Assumed 4680 battery production would ramp faster
  • Assumed engineering could context-switch between programs
  • Assumed capital would be unlimited

CORRECT RESOURCE PLANNING APPROACHES:

✓ OPTION 1: HONEST RESOURCE-CONSTRAINED SCHEDULE
  ┌─────────────────────────────────────────────┐
  │ 1. Model resource demand across all programs│
  │ 2. Identify resource conflicts/bottlenecks  │
  │ 3. Apply prioritization logic (business)    │
  │ 4. Calculate resource-constrained schedule  │
  │ 5. ANNOUNCE THE REALISTIC DATE (2023-24)    │
  └─────────────────────────────────────────────┘

  Outcome: Credibility preserved, expectations managed

✓ OPTION 2: RING-FENCED RESOURCES
  ┌─────────────────────────────────────────────┐
  │ 1. Commit dedicated battery allocation      │
  │    (e.g., 2 GWh/year to Cybertruck)         │
  │ 2. Separate engineering teams (no sharing)  │
  │ 3. Dedicated capital budget                 │
  │ 4. Protected factory space                  │
  │ 5. Meet 2021-2022 commitment                │
  └─────────────────────────────────────────────┘

  Outcome: Slower Model Y ramp, but commitments met
  Trade-off: Sacrifice $5-10B Model Y revenue for credibility

✓ OPTION 3: PHASE-GATE RESOURCE ALLOCATION
  ┌─────────────────────────────────────────────┐
  │ PHASE 1 (2019-2020): R&D with limited resources│
  │ • Prove exoskeleton manufacturing process   │
  │ • Validate 4680 battery performance         │
  │ • Resource allocation: 10-15% of total      │
  │                                             │
  │ GATE REVIEW: Process proven? Battery ready? │
  │                                             │
  │ PHASE 2 (2021+): Full allocation only if PASS│
  │ • Ramp resources to 30-40%                  │
  │ • Announce delivery date AFTER gate pass    │
  │ • Public announcement: "On track for 2023"  │
  └─────────────────────────────────────────────┘

  Outcome: Deferred announcement, realistic commitments

WHAT TESLA ACTUALLY DID:
✗ Announced aggressively (2021 delivery)
✗ Allocated resources to business priorities (Model Y)
✗ Missed commitments publicly
✗ Damaged credibility and brand trust

WORST OF ALL WORLDS:
• Over-promised → Lost credibility
• Under-resourced → Extended delays
• Changed priorities → Organizational confusion
• No transparency → Speculation and criticism

LESSON FOR SYSTEMS ENGINEERS:

"Resource allocation is not a business decision alone.
It's a PROJECT MANAGEMENT constraint that determines
what schedules are possible."

Your job as SE Project Manager:
1. Model resource demand across portfolio
2. Identify constraints and conflicts EARLY
3. Provide leadership with REALISTIC options:
   → Fast + Expensive (ring-fence resources)
   → Slow + Cheap (constrained resources)
   → Phased (defer until ready)
4. Hold leadership accountable to resource commitments
5. NEVER commit to a schedule without resource allocation

→ Schedules are promises. Resources make promises possible.
```

**Interactive Question:**

> "You're the Cybertruck program SE manager in 2021. Your CEO asks you to accelerate Cybertruck delivery to save face publicly. But you know Model Y has resource priority. What do you tell him?
>
> Draft a 2-minute response that:
> 1. Acknowledges business reality (Model Y priority)
> 2. Explains resource constraints
> 3. Proposes options with trade-offs
> 4. Recommends a path forward"

**Model Answer (Instructor provides):**

> "I understand the pressure to deliver Cybertruck faster. Here's the reality:
>
> **Current State:** Cybertruck has 15% of engineering resources, 5% of battery production, and 10% of factory space because Model Y is generating $50B in revenue. This allocation means Cybertruck will deliver in late 2023 at earliest.
>
> **Options:**
>
> **Option A - Maintain Current Allocation:**
> Delivery late 2023, low cost, Model Y unaffected. Recommend: Reset public expectations to 2023 NOW to stop credibility damage.
>
> **Option B - Accelerate with Resource Reallocation:**
> Deliver mid-2022, requires 40% resource shift from Model Y. Cost: $5-10B in lost Model Y revenue. Risk: Model Y ramp slows, investors react negatively.
>
> **Option C - Parallel Track (Hybrid):**
> Increase Cybertruck to 25% resources, deliver early 2023. Cost: $2-3B Model Y impact. Balanced approach.
>
> **Recommendation:** Option C + public transparency. Announce 'early 2023' target with monthly progress updates. Deliver on the reset expectation. Rebuild credibility through honesty and execution.
>
> **What I need from you:** Resource allocation decision in writing and commitment not to re-prioritize mid-stream."

**Learning Connection:** LO2, LO3 - Resource-constrained scheduling, portfolio management, stakeholder communication

---

### Slide 13: Technical Planning Deliverables

**After covering standard deliverables, add:**

**Instructor Narration:**

> "Let's talk about what planning deliverables Tesla should have had for Cybertruck—and what was likely missing.
>
> **Standard SE Planning Deliverables:**
>
> 1. **Systems Engineering Management Plan (SEMP)**
>    - Defines SE processes, organization, responsibilities
>    - Should exist: ✓ (Tesla has SE processes)
>    - Quality/completeness: ⚠️ Unknown
>
> 2. **Work Breakdown Structure (WBS) with Dictionary**
>    - Hierarchical decomposition of all work
>    - Should exist: ✓ (Required for any program)
>    - Problem: Likely underestimated complexity of exoskeleton work packages
>
> 3. **Integrated Master Schedule (IMS)**
>    - Time-phased schedule with dependencies
>    - Should exist: ✓
>    - Problem: **Optimistic estimates, insufficient contingency, ignored resource constraints**
>
> 4. **Resource Allocation Plan**
>    - Engineering, capital, materials allocation over time
>    - **Likely missing or incomplete:** ⚠️
>    - Evidence: Resource conflicts with Model Y, unplanned reallocation
>
> 5. **Risk Management Plan**
>    - Process for identifying and treating risks
>    - Should exist: ✓
>    - Problem: **Key risks not identified (process development duration, resource competition)**
>
> 6. **Technical Performance Measures (TPMs)**
>    - Metrics to track technical progress
>    - Examples: Exoskeleton thickness tolerance, panel gap, crash test performance
>    - Should exist: ✓
>    - Problem: **Didn't track schedule/resource TPMs that would have shown early warning**
>
> **The Missing Deliverable:**
>
> **Technology Readiness Assessment (TRA) with Risk-Adjusted Schedule**
>
> This should have been prepared in 2019:
>
> | Subsystem | Technology | TRL in 2019 | Target TRL | Development Risk | Schedule Impact |
> |-----------|-----------|-------------|------------|------------------|-----------------|
> | Body | Stainless exoskeleton | TRL 2-3 | TRL 9 | **HIGH** | **+12-18 months** |
> | Battery | 4680 cells | TRL 4 | TRL 9 | **HIGH** | **+18-24 months** |
> | Electrical | 48V architecture | TRL 3-4 | TRL 9 | **MEDIUM** | **+6-12 months** |
> | Steering | Steer-by-wire | TRL 5-6 | TRL 9 | **MEDIUM** | **+6-9 months** |
>
> **TRL Definitions Reminder:**
> - TRL 1-3: Research/concept
> - TRL 4-6: Development/prototype
> - TRL 7-9: Production-ready/deployed
>
> If this TRA existed and was taken seriously, it would have shown:
> - **Two subsystems at TRL 2-4 = High risk**
> - **Realistic timeline: 3-4 years, not 2 years**
> - **Recommendation: Announce 2023-2024 delivery**
>
> But this likely either:
> 1. Wasn't prepared thoroughly
> 2. Was prepared but ignored for marketing reasons
> 3. Was overly optimistic about TRL advancement rates
>
> **Lesson:** When your technology readiness is low, your schedule confidence should be low. Plan accordingly."

**PPT Content:**
```
CYBERTRUCK TECHNICAL PLANNING DELIVERABLES ANALYSIS

STANDARD SE PLANNING DELIVERABLES:

1. SYSTEMS ENGINEERING MANAGEMENT PLAN (SEMP)
   Status: ✓ Exists (Tesla has SE processes)
   Quality: ⚠️ Unknown if comprehensive for novel manufacturing

2. WORK BREAKDOWN STRUCTURE (WBS) + DICTIONARY
   Status: ✓ Exists
   Problem: ✗ Underestimated exoskeleton work package complexity
            ✗ Process development work insufficiently detailed

3. INTEGRATED MASTER SCHEDULE (IMS)
   Status: ✓ Exists
   Problems: ✗ Optimistic estimates (6 months for process dev)
             ✗ Insufficient schedule contingency (0% buffer)
             ✗ Resource constraints not modeled
             ✗ Fast-tracking dependencies created rework

4. RESOURCE ALLOCATION PLAN ⚠️ KEY MISSING DELIVERABLE
   Status: ⚠️ Likely missing or incomplete
   Evidence: • Resource conflicts with Model Y (unplanned)
             • Mid-stream reallocation of resources
             • No apparent cross-program resource balancing
   Should have included:
   ├─ Engineering headcount by quarter (2019-2024)
   ├─ Battery allocation by program (Cybertruck vs MY)
   ├─ Capital expenditure phasing
   ├─ Facility/equipment utilization plan
   └─ Conflict identification and resolution

5. RISK MANAGEMENT PLAN
   Status: ✓ Exists
   Problems: ✗ Key risks NOT identified:
             • "Manufacturing process TRL too low" (High/High risk)
             • "Resource competition with Model Y" (High/Med risk)
             • "4680 battery production delays" (Med/High risk)
             ✗ No risk-adjusted schedule published

6. TECHNICAL PERFORMANCE MEASURES (TPMs)
   Status: ✓ Exists for technical metrics
   Technical TPMs tracked:
   ├─ Panel gap tolerance (±10 microns)
   ├─ Crash test performance
   ├─ Range/efficiency
   └─ Towing capacity

   MISSING: Program Management TPMs
   Should have tracked:
   ├─ Schedule Performance Index (SPI) = EV/PV
   ├─ Cost Performance Index (CPI) = EV/AC
   ├─ Technology Readiness Level (TRL) progression
   ├─ Resource utilization vs. plan
   └─ Risk burndown (# high risks over time)

   → Would have shown RED flags in 2020-2021

THE CRITICAL MISSING DELIVERABLE:
═══════════════════════════════════════════════════

TECHNOLOGY READINESS ASSESSMENT (TRA)
With Risk-Adjusted Schedule Impact Analysis

Should have been prepared: 2019 (before announcement)

SUBSYSTEM TRL ASSESSMENT (2019):

Subsystem        │Technology          │TRL│Target│Risk │Schedule
                 │                    │'19│ TRL  │Level│Impact
─────────────────┼────────────────────┼───┼──────┼─────┼─────────
Body Structure   │SS Exoskeleton Mfg  │2-3│  9   │⚠️HIGH│+12-18mo
                 │(No precedent)      │   │      │     │
─────────────────┼────────────────────┼───┼──────┼─────┼─────────
Propulsion       │4680 Battery Cells  │ 4 │  9   │⚠️HIGH│+18-24mo
                 │(Prototype stage)   │   │      │     │
─────────────────┼────────────────────┼───┼──────┼─────┼─────────
Electrical       │48V Architecture    │3-4│  9   │⚠️MED │+6-12mo
                 │(Industry first)    │   │      │     │
─────────────────┼────────────────────┼───┼──────┼─────┼─────────
Chassis/Steering │Steer-by-Wire Truck │5-6│  9   │⚠️MED │+6-9mo
                 │(New application)   │   │      │     │
─────────────────┼────────────────────┼───┼──────┼─────┼─────────
Software/UI      │Cybertruck UI/UX    │ 6 │  9   │ LOW │+3-6mo
                 │(Adapt existing)    │   │      │     │

TRL SCALE REMINDER:
TRL 1-3: Basic research, concept development
TRL 4-6: Technology development, prototype demonstration
TRL 7-9: System development, production deployment

RISK-ADJUSTED SCHEDULE CALCULATION:

BASE SCHEDULE (No new technology):        18 months
+ Exoskeleton development (TRL 2→9):     +15 months
+ 4680 battery development (TRL 4→9):    +20 months (parallel)
+ 48V architecture (TRL 3→9):            +9 months (parallel)
+ Steer-by-wire (TRL 5→9):               +7 months (parallel)
+ Integration contingency (20%):         +6 months
──────────────────────────────────────────────────
REALISTIC TIMELINE:                       39-45 months
                                         (3.25-3.75 years)

RECOMMENDED ANNOUNCEMENT (2019):
"Cybertruck will enter production in 2023,
 with deliveries beginning late 2023/early 2024."

ACTUAL ANNOUNCEMENT:
"Production in 2021" (24 months)

DELTA: 15-21 months underestimate
═══════════════════════════════════════════════════

WHY TRA WAS LIKELY MISSING OR IGNORED:

Scenario 1: NOT PREPARED
✗ No systematic TRL assessment
✗ Engineering gut feel: "We can figure it out"
✗ Marketing drove timeline, not engineering

Scenario 2: PREPARED BUT IGNORED
⚠️ TRA showed 3-4 year timeline
⚠️ Leadership overruled for competitive/marketing reasons
⚠️ "Stretch goal" became "committed schedule"

Scenario 3: OVERLY OPTIMISTIC TRA
⚠️ TRL advancement rates assumed too aggressive
⚠️ "We'll solve it faster than normal"
⚠️ Innovation optimism bias

MOST LIKELY: Combination of Scenario 1 and 3

CORRECT APPROACH - TRA-DRIVEN SCHEDULE:

STEP 1: Conduct Technology Readiness Assessment
├─ Identify all novel technologies
├─ Assess current TRL honestly (external review)
├─ Determine target TRL for production
└─ Estimate development time per TRL advancement

STEP 2: Apply Historical TRL Advancement Rates
├─ TRL 2→4: 12-18 months (research to prototype)
├─ TRL 4→6: 12-18 months (prototype to demo)
├─ TRL 6→9: 18-24 months (demo to production)
└─ Add 20-30% contingency for unknowns

STEP 3: Build Risk-Adjusted Schedule
├─ Identify longest TRL advancement path (critical path)
├─ Add parallel development paths
├─ Apply schedule contingency
└─ Generate P50 (50% confidence) and P80 (80% confidence) dates

STEP 4: Communicate Credible Schedule
├─ Internal target: P50 date (50% confidence)
├─ External commitment: P80 date (80% confidence)
└─ Explain uncertainty honestly ("dependent on technology maturation")

EXAMPLE FOR CYBERTRUCK (2019):

Internal Target: Q4 2022 (P50 - 36 months)
External Commitment: "Production 2023" (P80 - 42-48 months)
Communication: "Cybertruck represents breakthrough technology.
                We're targeting 2023 production as battery and
                manufacturing processes mature."

RESULT: Under-promise, over-deliver instead of vice versa

DELIVERABLE CHECKLIST FOR AUTOMOTIVE SE PROJECTS:

✓ SEMP (Systems Engineering Management Plan)
✓ WBS + WBS Dictionary (with effort estimates)
✓ IMS (Integrated Master Schedule with contingency)
✓ Resource Allocation Plan (cross-program conflicts identified)
✓ Risk Management Plan + Risk Register
✓ Technology Readiness Assessment (TRA)
✓ TPM Plan (technical + program management metrics)
✓ Interface Control Documents (ICDs)
✓ Configuration Management Plan
✓ Integration and Verification Plan

MISSING ANY OF THESE = SCHEDULE/COST RISK

KEY TAKEAWAY:

"Low technology readiness = High schedule uncertainty

If you're inventing processes while developing product,
your schedule is a GOAL, not a PLAN.

Communicate it as such."
```

**Discussion Question (2 min):**

> "Imagine you're presenting the TRA to Elon Musk in 2019. Your analysis shows 3-4 years is realistic. He says: 'That's unacceptable. We're announcing 2 years. Make it work.'
>
> What do you say? What are your ethical obligations as an engineer?"

**Expected Discussion:**
- Professional responsibility to provide accurate data
- Distinguish between "stretch goals" (internal motivation) and "committed schedules" (external promises)
- Document disagreement and get risk acceptance in writing
- Propose alternatives (phased delivery, contingency planning)

**Learning Connection:** LO1, LO3 - SE planning deliverables, technology readiness, professional ethics

---

### Slide 14: Project Assessment and Control Process

**After covering assessment and control fundamentals, add:**

**Instructor Narration:**

> "Project assessment and control is how you detect problems early and take corrective action. Let's analyze where Cybertruck's assessment and control failed—and what signals should have triggered intervention.
>
> **Earned Value Management (EVM) - The Early Warning System**
>
> EVM tracks three metrics:
> - **Planned Value (PV):** What you planned to accomplish by now
> - **Earned Value (EV):** What you actually accomplished
> - **Actual Cost (AC):** What you actually spent
>
> From these, we calculate:
> - **Schedule Performance Index (SPI) = EV / PV**
>   - SPI < 1.0 = Behind schedule
>   - SPI = 1.0 = On schedule
>   - SPI > 1.0 = Ahead of schedule
>
> - **Cost Performance Index (CPI) = EV / AC**
>   - CPI < 1.0 = Over budget
>   - CPI = 1.0 = On budget
>   - CPI > 1.0 = Under budget
>
> **Hypothetical Cybertruck EVM Analysis (Q4 2020):**
>
> **Planned (2019 baseline):**
> - By Q4 2020 (12 months in):
>   - Manufacturing process development: 100% complete
>   - Tooling design: 50% complete
>   - Pilot build: 0% (not started)
> - **Planned Value (PV) = $800M** (40% of $2B budget)
>
> **Actual (Q4 2020):**
> - Manufacturing process development: 30% complete (still iterating)
> - Tooling design: 10% complete (waiting on process)
> - Pilot build: 0% (not started)
> - **Earned Value (EV) = $300M** (15% of work done)
> - **Actual Cost (AC) = $500M** (spent on iterations and rework)
>
> **Performance Indices:**
> - **SPI = $300M / $800M = 0.375** ⚠️ **CRITICAL - 62% behind schedule!**
> - **CPI = $300M / $500M = 0.60** ⚠️ **CRITICAL - 67% over budget!**
>
> **What This Means:**
> - You're only 37.5% as productive as planned (SPI)
> - Every dollar is buying 60 cents of value (CPI)
> - **Forecast at Completion:**
>   - **Schedule: $800M / $300M × 12 months = 32 months** (not 24 months)
>   - **Cost: $2B / 0.60 = $3.33B** (not $2B)
>
> **At this point—Q4 2020—Cybertruck was already doomed to miss 2021 delivery.**
>
> **The Control Question: What should have happened?**
>
> **GATE REVIEW (Q4 2020):**
> - **Status:** SPI = 0.375, CPI = 0.60 — both RED
> - **Root Cause:** Manufacturing process more complex than estimated
> - **Forecast:** Delivery late 2022/early 2023 (not 2021)
> - **Decision Options:**
>   1. **Replan:** Update schedule to 2023, reset expectations
>   2. **Crash:** Add resources to accelerate (may not help R&D work)
>   3. **Descope:** Simplify exoskeleton design (remove novelty)
>   4. **Terminate:** Cancel program (unlikely but rational if ROI negative)
>
> **What Tesla likely did:**
> - Continued without official replanning
> - Hoped for breakthrough in process development
> - Delayed public announcement of slip
> - Result: Delays compounded, credibility damaged
>
> **The Assessment Failure:**
>
> Either:
> 1. **EVM wasn't tracked rigorously** (possible in high-growth startup culture)
> 2. **EVM showed problems but was ignored** (optimism bias)
> 3. **No formal gate review process** (continue until obvious failure)
>
> **Industry Standard Practice:**
>
> Most automotive OEMs using APQP would have had:
> - **Quarterly Program Reviews** with leadership
> - **Gate Reviews** at phase transitions
> - **EVM tracking** with variance thresholds (e.g., SPI/CPI < 0.9 = red flag)
> - **Corrective Action Plans** triggered automatically when metrics go red
>
> If SPI < 0.8 or CPI < 0.8 → **Mandatory replan or program stop**
>
> **Lesson:** Assessment and control only work if you:
> 1. **Track meaningful metrics** (EVM, TPMs, risk burndown)
> 2. **Set decision thresholds** (what triggers action?)
> 3. **Have decision authority** (can actually replan/descope/cancel)
> 4. **Act on data** (don't hope for miracles)"

**PPT Content:**
```
CYBERTRUCK PROJECT ASSESSMENT & CONTROL FAILURE

EARNED VALUE MANAGEMENT (EVM) - EARLY WARNING SYSTEM
═══════════════════════════════════════════════════

EVM FUNDAMENTALS:

PV (Planned Value):  What you PLANNED to accomplish by now
EV (Earned Value):   What you ACTUALLY accomplished
AC (Actual Cost):    What you ACTUALLY spent

Performance Indices:
SPI (Schedule Performance Index) = EV / PV
  < 1.0 = Behind schedule
  = 1.0 = On schedule
  > 1.0 = Ahead of schedule

CPI (Cost Performance Index) = EV / AC
  < 1.0 = Over budget
  = 1.0 = On budget
  > 1.0 = Under budget

HYPOTHETICAL CYBERTRUCK EVM (Q4 2020):
─────────────────────────────────────────────────

BASELINE PLAN (Nov 2019):
• Duration: 24 months (Nov 2019 → Nov 2021)
• Budget: $2,000M
• Delivery: Late 2021

STATUS AT 12 MONTHS (Q4 2020):

PLANNED PROGRESS (PV):
├─ Manufacturing process dev:  100% complete ✓
├─ Tooling design:             50% complete ✓
├─ Pilot build:                0% (not started)
└─ Planned Value (PV) = $800M (40% of budget)

ACTUAL PROGRESS (EV):
├─ Manufacturing process dev:  30% complete ⚠️
│   └─ Still iterating on folding process
├─ Tooling design:             10% complete ⚠️
│   └─ Waiting on process definition
├─ Pilot build:                0% (not started)
└─ Earned Value (EV) = $300M (15% of work done)

ACTUAL COST (AC):
├─ Process R&D:               $250M (iterations, prototypes)
├─ Tooling design:            $50M (aborted designs)
├─ Engineering labor:         $150M (extended team)
├─ Facilities/equipment:      $50M (test equipment)
└─ Actual Cost (AC) = $500M spent

PERFORMANCE CALCULATION:
─────────────────────────────────────────────────
SPI = EV / PV = $300M / $800M = 0.375 ⚠️ CRITICAL RED
CPI = EV / AC = $300M / $500M = 0.60  ⚠️ CRITICAL RED

INTERPRETATION:

SPI = 0.375 → You are 37.5% as productive as planned
              You are 62% BEHIND schedule

CPI = 0.60  → Every dollar is buying 60¢ of value
              You are 67% OVER BUDGET per unit work

FORECAST AT COMPLETION (EAC):
─────────────────────────────────────────────────
Using current performance to forecast final outcome:

Schedule Forecast:
EAC(time) = Planned Duration / SPI
          = 24 months / 0.375
          = 64 months (5.3 years!)

Realistic forecast (assuming some improvement):
          = 24 months / 0.60 (assume SPI improves)
          = 40 months (3.3 years)
          → Delivery: Q1 2023 (not Q4 2021)

Cost Forecast:
EAC(cost) = Budget / CPI
          = $2,000M / 0.60
          = $3,333M (+$1,333M overrun = +67%)

Realistic forecast (assuming process stabilizes):
          = $2,000M / 0.75 (assume CPI improves)
          = $2,667M (+$667M overrun = +33%)

AT Q4 2020, THE DATA SHOWS:
→ Cybertruck will NOT deliver in 2021
→ Realistic delivery: 2023
→ Cost overrun: $500M - $1B+

THE CONTROL FAILURE - WHAT SHOULD HAVE HAPPENED:
═══════════════════════════════════════════════════

GATE REVIEW (Q4 2020) - Triggered by SPI/CPI < 0.8:

┌──────────────────────────────────────────────┐
│ PROGRAM REVIEW: Cybertruck 12-Month Gate    │
├──────────────────────────────────────────────┤
│ Status: ⚠️ CRITICAL RED                       │
│ SPI: 0.375 (62% behind schedule)             │
│ CPI: 0.60 (67% over budget per work)         │
│                                              │
│ ROOT CAUSE ANALYSIS:                         │
│ • Manufacturing process complexity           │
│   underestimated by 4x                       │
│ • Stainless steel exoskeleton requires       │
│   process invention, not adaptation          │
│ • TRL was 2-3, not 5-6 as assumed            │
│ • 4680 battery also delayed (parallel issue) │
│                                              │
│ FORECAST:                                    │
│ • Delivery: Late 2022 / Early 2023 (best case)│
│ • Cost: $2.5B - $3.5B (+25-75%)              │
│                                              │
│ DECISION REQUIRED:                           │
│ ☐ 1. REPLAN - Accept new schedule/cost      │
│ ☐ 2. CRASH - Add resources (may not help)   │
│ ☐ 3. DESCOPE - Simplify design               │
│ ☐ 4. TERMINATE - Cancel program              │
└──────────────────────────────────────────────┘

DECISION OPTION 1: REPLAN (RECOMMENDED)
┌──────────────────────────────────────────────┐
│ ACTION:                                      │
│ • Update baseline schedule to 40-48 months   │
│ • Revise budget to $2.5-3.0B                 │
│ • Reset resource allocation plan             │
│ • Announce publicly: "Production 2023"       │
│                                              │
│ PROS:                                        │
│ + Honest, credible schedule                  │
│ + Manages expectations                       │
│ + Preserves technical ambition               │
│ + Allows proper resource allocation          │
│                                              │
│ CONS:                                        │
│ - Public admission of delay                  │
│ - Competitive exposure (F-150 Lightning)     │
│ - Reservation cancellations possible         │
│                                              │
│ OUTCOME: Credibility preserved, realistic plan│
└──────────────────────────────────────────────┘

DECISION OPTION 2: CRASH (Add Resources)
┌──────────────────────────────────────────────┐
│ ACTION:                                      │
│ • Double engineering team (200 → 400)        │
│ • Allocate 40% of 4680 production to CT      │
│ • Fast-track tooling (order before process)  │
│ • 24/7 manufacturing process development     │
│                                              │
│ PROS:                                        │
│ + Might accelerate delivery by 3-6 months    │
│ + Shows commitment to 2021 target            │
│                                              │
│ CONS:                                        │
│ - R&D work doesn't scale linearly with people│
│ - Cost increases dramatically (+$500M-1B)    │
│ - Robs resources from Model Y (revenue loss) │
│ - May not actually save significant time     │
│                                              │
│ OUTCOME: Expensive, uncertain benefit        │
└──────────────────────────────────────────────┘

DECISION OPTION 3: DESCOPE (Simplify Design)
┌──────────────────────────────────────────────┐
│ ACTION:                                      │
│ • Replace stainless exoskeleton with         │
│   aluminum body + stainless cladding         │
│ • Use proven stamping processes              │
│ • Deliver "Cybertruck Lite" in 2021-2022     │
│ • Defer full exoskeleton to "Version 2"      │
│                                              │
│ PROS:                                        │
│ + Can likely hit 2022 delivery               │
│ + Reduces cost back to $2B range             │
│ + Gets product to market vs competition      │
│                                              │
│ CONS:                                        │
│ - Compromises core Cybertruck identity       │
│ - Reduces competitive differentiation        │
│ - Brand disappointment ("that's not CT!")    │
│ - May damage pre-orders                      │
│                                              │
│ OUTCOME: Faster but compromised product      │
└──────────────────────────────────────────────┘

DECISION OPTION 4: TERMINATE (Cancel Program)
┌──────────────────────────────────────────────┐
│ ACTION:                                      │
│ • Cancel Cybertruck program                  │
│ • Refund reservations                        │
│ • Reallocate resources to Model Y/Semi       │
│ • Write off $500M sunk cost                  │
│                                              │
│ PROS:                                        │
│ + Stops losses from compounding              │
│ + Refocuses on profitable programs (Model Y) │
│ + Avoids 2+ years of continued cost overrun  │
│                                              │
│ CONS:                                        │
│ - Massive brand/reputation damage            │
│ - Loses truck market opportunity             │
│ - Elon Musk's pet project (political suicide)│
│                                              │
│ OUTCOME: Rational but politically impossible │
└──────────────────────────────────────────────┘

WHAT TESLA LIKELY DID (Q4 2020):
✗ No formal gate review
✗ Continued development hoping for breakthrough
✗ No schedule rebaseline or public announcement
✗ Delayed transparency until delays obvious (2021-2022)
✗ Result: Compounded delays, lost credibility

ASSESSMENT & CONTROL BEST PRACTICES:
═══════════════════════════════════════════════════

1. ESTABLISH PERFORMANCE BASELINES
   ✓ Baseline schedule (IMS)
   ✓ Baseline cost (budget)
   ✓ Baseline scope (requirements)
   ✓ Baseline technical performance (TPMs)

2. TRACK PERFORMANCE METRICS MONTHLY
   ✓ EVM: SPI, CPI, EAC
   ✓ TPMs: Technical performance measures
   ✓ Risk burndown: # high/med/low risks over time
   ✓ Milestone completion: Planned vs actual

3. SET DECISION THRESHOLDS (Control Gates)
   ✓ SPI or CPI < 0.95: Yellow (investigate)
   ✓ SPI or CPI < 0.80: Red (mandatory action)
   ✓ Schedule slip > 10%: Rebaseline required
   ✓ Cost variance > 15%: Executive review

4. CONDUCT PERIODIC GATE REVIEWS
   ✓ Monthly: Program team review
   ✓ Quarterly: Executive review
   ✓ Phase gates: Go/no-go decisions
   ✓ Independent assessments (external audits)

5. ENABLE CORRECTIVE ACTION AUTHORITY
   ✓ Program manager can replan within ±10%
   ✓ Executive team approves >10% changes
   ✓ Board approves termination decisions
   ✓ Document decisions and rationale

6. COMMUNICATE TRANSPARENTLY
   ✓ Internal: Honest status (green/yellow/red)
   ✓ External: Credible commitments (P80 dates)
   ✓ Stakeholders: Early warning of issues
   ✓ Lessons learned: Capture and share

AUTOMOTIVE INDUSTRY STANDARD (APQP):

Gate 1: Plan & Define → Gate Review → Proceed or Stop
Gate 2: Product Design & Development → Gate Review
Gate 3: Process Design & Development → Gate Review
Gate 4: Product & Process Validation → Gate Review
Gate 5: Launch & Continuous Improvement

At each gate:
• Is schedule on track? (SPI check)
• Is budget on track? (CPI check)
• Are technical requirements met? (TPM check)
• Are risks under control? (Risk register review)

IF ANY METRIC IS RED → CANNOT PROCEED TO NEXT GATE
Must address root cause or replan

CYBERTRUCK LIKELY VIOLATED:
✗ Proceeded past Gate 2 despite low TRL
✗ Proceeded past Gate 3 despite process immaturity
✗ No clear stop/replan discipline

KEY TAKEAWAY:

"Assessment without control is just watching failure happen.
Control without authority is just documentation.

You need BOTH:
1. Metrics that show problems early (EVM, TPMs)
2. Decision processes that fix problems (Gate reviews)
3. Authority to take corrective action (Replan, descope, stop)

Otherwise, you're on a slow-motion train wreck."

STUDENT REFLECTION QUESTION:

"If you were the SE program manager and your Q4 2020
EVM showed SPI=0.375 and CPI=0.60, but your CEO wanted
to maintain the 2021 delivery promise publicly, what would you do?

A) Report the red metrics and recommend replanning
B) Continue and hope performance improves
C) Manipulate metrics to show better performance
D) Resign rather than be part of inevitable failure

Discuss the ethical and professional dimensions."
```

**Class Discussion (5 min):**

> "Let's vote. How many would choose each option? Why?"

**Expected Discussion Points:**
- **Option A (Correct):** Professional obligation to report accurate data, even if unpopular
- **Option B:** Gambling with company resources and reputation, unethical
- **Option C:** Fraudulent, potentially criminal, absolutely unacceptable
- **Option D:** Walking away doesn't solve the problem, better to fight for truth

**Instructor Synthesis:**

> "Option A is the only professional choice. Your duty as an engineer is to provide leadership with accurate information, even when they don't want to hear it. You can't control the decision—they may ignore you—but you can control the integrity of your analysis.
>
> **Document everything.** If leadership proceeds despite red metrics, document your recommendation and their decision. This protects you professionally and creates an audit trail.
>
> **Propose solutions, not just problems.** Don't just say 'we're behind.' Say 'we're behind, here are three options with trade-offs, here's my recommendation.'
>
> This is what separates professional engineers from order-takers."

**Learning Connection:** LO1, LO2, LO3 - Project assessment, EVM, gate reviews, professional ethics

---

## 1.3 Key Takeaways from Cybertruck Case

**For wrap-up discussion (Slide 27-28):**

### Project Planning Lessons:

1. **WBS Complexity Drives Everything**
   - Novel work packages require explicit R&D phases
   - "Invent new process" ≠ "Adapt existing process"
   - Build unknowns into the WBS explicitly

2. **Schedule Realism Beats Schedule Optimism**
   - Use range estimation (PERT) for uncertain work
   - Technology readiness drives schedule confidence
   - External commitments should be P80 (80% confidence), not P50

3. **Resource Constraints Are Schedule Constraints**
   - Model resource demand across portfolio
   - Identify conflicts before committing schedules
   - Ring-fence resources or extend schedule—can't have both

4. **Dependencies Must Be Honored**
   - Fast-tracking dependent work creates rework loops
   - Finish-to-Start means Finish, THEN Start
   - Parallel work only when truly independent

5. **Technology Readiness Assessment Is Mandatory**
   - Low TRL = High schedule risk
   - Budget TRL advancement time realistically
   - Don't announce until TRL 6+

### Project Control Lessons:

6. **EVM Shows Problems When They're Fixable**
   - SPI < 0.8 at 50% complete = doomed schedule
   - CPI trends don't reverse without intervention
   - Track monthly, act on thresholds

7. **Gate Reviews Require Decision Authority**
   - Red metrics must trigger action (replan/descope/stop)
   - "Hoping for improvement" is not a strategy
   - Document decisions and rationale

8. **Transparency Preserves Credibility**
   - Delays revealed early = manageable disappointment
   - Delays revealed late = destroyed trust
   - Under-promise, over-deliver

### Professional Lessons:

9. **Technical Excellence ≠ Management Excellence**
   - Tesla excels at EV technology
   - But struggled with project management discipline
   - Both are required for success

10. **Ethical Obligation to Report Truth**
    - Engineers must provide accurate status
    - Even when leadership doesn't want to hear it
    - Document recommendations and decisions

---

## 1.4 Discussion Prompts for Students

**Use throughout or at end:**

1. **"What would you have done differently in 2019 when planning Cybertruck?"**
   - Expected: More conservative schedule, explicit TRA, resource allocation plan

2. **"At what point (month/year) did Cybertruck delays become inevitable?"**
   - Expected: Q4 2020 when EVM showed SPI 0.4-0.6, process development still at TRL 3-4

3. **"Was the exoskeleton design worth the delays and cost overruns?"**
   - Debate: Differentiation vs. practicality, brand identity vs. time-to-market

4. **"How would traditional automotive OEMs (Ford, GM, Toyota) have handled this differently?"**
   - Expected: APQP gate reviews would have caught issues, more conservative planning culture, less tolerance for TRL risk

5. **"What's the economic cost of the delays beyond direct development cost?"**
   - Expected: Opportunity cost (F-150 Lightning captured market), brand damage, preorder cancellations, competitive response time

---

**END OF CASE STUDY 1**

This completes the Tesla Cybertruck case study for the Project Planning Process section.

Next: Ford F-150 Lightning case study for Risk Management section.


---

# CASE STUDY 2: FORD F-150 LIGHTNING BATTERY FIRE & RECALL
**Use for: RISK MANAGEMENT PROCESS (Slides 15-19)**

## 2.1 Case Overview

### Timeline of Events

**May 19, 2021 - Lightning Unveiled**
- Ford reveals all-electric F-150 Lightning
- Promises 230-300 mile range, $39,974 starting price
- Targets fleet and retail customers
- Pre-orders: 200,000+ in 3 weeks

**Spring 2022 - Production Begins**
- May 2022: Production starts at Rouge Electric Vehicle Center (Dearborn, MI)
- Initial production: ~150 units/day
- Battery supplier: SK On (South Korea)
- Battery configuration: Blade-style pouch cells in structural pack

**September 2022 - Quality Issue Emerges**
- Internal quality check reveals potential battery issue
- Ford halts some deliveries for additional screening
- Issue initially described as "quality verification"
- Limited public information

**February 9, 2023 - Production Halt**
- **CRITICAL EVENT:** Ford halts F-150 Lightning production
- Reason: Potential battery issue discovered during pre-delivery quality check
- **One vehicle caught fire** during quality inspection (not customer vehicle)
- No customer vehicles affected, no injuries
- ~15,000 vehicles already delivered to customers

**February 2023 - Investigation Phase**
- Ford and SK On investigate root cause
- Battery pack teardown and analysis
- Cell-level testing and validation
- Engineering review of design, manufacturing, quality processes
- Estimated impact: 4,000-5,000 units in production or pre-delivery hold

**March 2023 - Root Cause Identified**
- Battery manufacturing defect identified
- Issue: **Battery cell contaminant** causing internal short circuit risk
- Specific to certain production batches from SK On
- Risk: Low probability but catastrophic consequence (thermal runaway, fire)
- Affects specific production date range

**April 2023 - Mitigation Plan Announced**
- Ford develops multi-layer mitigation approach:
  1. Enhanced incoming quality inspection of battery cells
  2. Modified battery pack assembly process
  3. Additional validation testing before vehicle release
  4. Field monitoring protocol for delivered vehicles
- Production restart plan developed

**May 2023 - Limited Production Restart**
- Production resumes with modified processes
- Initial rate: ~50-75 units/day (reduced from 150)
- Every battery pack subjected to enhanced testing
- Delivery hold continues for suspect production date vehicles

**June-July 2023 - Recall Issued**
- June 23, 2023: Ford issues recall for 18,666 F-150 Lightning vehicles
- Affected: 2022-2023 model years built Feb 2022 - Jun 2023
- Recall action: Replace battery pack in affected vehicles
- Estimated cost: $1.8 billion+ ($100K+ per vehicle for battery replacement)
- 18,666 vehicles × $100K = $1.87 billion minimum

**August 2023 - Production Ramp Resumes**
- Production gradually increases to 100+ units/day
- Enhanced quality gates in place
- SK On implements corrective actions at cell production facility
- Ford confidence restored in supply chain

**Q4 2023 - Recovery Phase**
- Production reaches 150+ units/day (target rate)
- Recall completion: ~60-70% of affected vehicles serviced by year-end
- Customer confidence rebuilding efforts
- Financial impact recognized in earnings

**2024 - Lessons Learned Implementation**
- Ford implements enhanced battery quality protocols across all EVs
- SK On relationship strengthened with quality agreements
- Industry-wide implications for EV battery quality management
- Incorporation into ISO 26262 functional safety processes

### Key Metrics

| Metric | Value | Impact |
|--------|-------|--------|
| **Production Halt Duration** | ~3 months (Feb-May 2023) | Lost ~13,500 units |
| **Vehicles Recalled** | 18,666 units (2022-2023 MY) | Largest Lightning recall |
| **Financial Impact** | $1.8B+ (battery replacement) | ~$100K per vehicle |
| **Production Rate Impact** | 150/day → 50/day for 3 months | -67% throughput |
| **Customer Impact** | ~15,000 delivered vehicles | Recall inconvenience |
| **Reputational Impact** | Significant media coverage | Trust/confidence damage |
| **Market Share Impact** | Lost ground to Rivian R1T | Competitive disadvantage |

### Root Cause Analysis

**Immediate Cause:**
- Battery cell manufacturing defect (contaminant in specific production batches)
- Contaminant creates potential internal short circuit pathway
- Internal short can lead to thermal runaway → battery fire

**Contributing Factors:**

**1. Supply Chain Quality Control Gap**
- SK On cell manufacturing process had insufficient contamination controls
- Ford incoming inspection did not detect cell-level defects (non-destructive testing limitations)
- Relied on supplier quality systems without sufficient verification

**2. Design Vulnerability**
- Blade-style pouch cell design may be more sensitive to contaminants than cylindrical cells
- Structural battery pack design makes field replacement extremely expensive (~$100K)
- No cell-level isolation/containment to prevent propagation

**3. Validation Testing Gaps**
- Pre-production validation testing may not have stressed contamination failure mode
- Accelerated life testing duration may have been insufficient
- Sample size in validation may not have caught low-probability defects

**4. Risk Assessment Gaps**
- "Battery cell contamination" risk likely existed in risk register
- But probability may have been assessed as "very low" based on supplier history
- Impact correctly assessed as "catastrophic" (fire, safety)
- Risk treatment: "Accept with supplier quality control" (insufficient)

**5. Early Warning Signals Missed**
- September 2022 "quality verification" issue was an early signal
- Issue was investigated but not escalated to production halt immediately
- 5-month gap between early signal (Sep 2022) and production halt (Feb 2023)
- Additional vehicles produced during investigation period

### The Risk That Wasn't Managed

**The risk that should have been identified and treated:**

**RISK:** Battery cell manufacturing defect (contamination, electrode misalignment, separator damage) from supplier leads to field failure (fire) in customer vehicles.

**Pre-Production Risk Assessment (Hypothetical - what should have been):**

- **Likelihood:** Low-Medium (supplier has quality systems, but defects happen)
- **Consequence:** Catastrophic (battery fire, injury/death risk, massive recall, brand damage)
- **Risk Level:** HIGH (even low probability × catastrophic = high risk)
- **Risk Treatment Strategy:** MITIGATE
  - Mitigation 1: Supplier quality audit and certification (done ✓)
  - Mitigation 2: Incoming inspection with sampling (done ✓, but insufficient)
  - Mitigation 3: **Enhanced validation testing with failure mode stress testing** (gap ✗)
  - Mitigation 4: **100% cell screening with advanced diagnostics** (not done ✗)
  - Mitigation 5: **Design for containment** (cell-level or module-level fire barriers) (gap ✗)
  - Mitigation 6: **Field monitoring with early warning detection** (not deployed until after incident ✗)

**What Was Likely Done (Based on Industry Practice):**
- Supplier audit ✓
- Incoming sampling inspection ✓
- Standard validation testing ✓
- Risk accepted based on "supplier quality systems are robust"

**What Was Missing:**
- Worst-case failure mode testing (contaminated cell stress testing)
- 100% inline cell screening (cost vs. risk trade-off made in favor of cost)
- Design mitigations (cell-level fault isolation)
- Proactive field monitoring (battery health telemetry with anomaly detection)

---

## 2.2 Integration with RISK MANAGEMENT PROCESS

### Slide 15: Risk Management Process - Overview

**Instructor Narration (Add after standard content):**

> "Let's transition from project planning to risk management. And let me show you a current, real-world example of what happens when a high-impact risk isn't fully mitigated.
>
> **February 9, 2023:** Ford halts production of the F-150 Lightning—the electric version of America's best-selling truck. Why? One vehicle caught fire during a pre-delivery quality check. Not a customer vehicle—a quality inspection caught it. But Ford made the right call: **Stop production immediately.**
>
> This wasn't just a quality issue. This was a **risk management failure** that cost Ford $1.8 billion, damaged their EV credibility, and gave competitors like Rivian an opening.
>
> Let's dissect this through the ISO/IEC 15288 Risk Management Process and understand what went wrong, what went right, and what you need to learn."

**PPT Addition:**
```
CASE STUDY: Ford F-150 Lightning Battery Fire & Recall

FEBRUARY 9, 2023:
• Ford halts F-150 Lightning production
• One vehicle fire during quality check (pre-delivery)
• Root cause: Battery cell manufacturing defect
• Recall: 18,666 vehicles (2022-2023)
• Cost: $1.8 billion+ (battery pack replacement)
• Production halt: 3 months

THE RISK MANAGEMENT QUESTION:
"Was this risk identified? Was it adequately treated?
If so, why did it still happen?"

→ Let's analyze through the Risk Management Process
```

**Learning Connection:** LO2, LO3 - Automotive risk management, safety-critical systems

---

### Slide 16: Risk Identification - Finding the Threats and Opportunities

**After teaching risk identification techniques (brainstorming, checklists, FMEA, etc.), add:**

**Instructor Narration:**

> "Risk identification is the foundation. You can't manage risks you haven't identified. Let's apply Ford F-150 Lightning battery risks.
>
> **Risk Identification Session (Should Have Happened in 2020-2021):**
>
> Using FMEA (Failure Mode and Effects Analysis) for the battery pack subsystem:
>
> **Component:** Lithium-ion Battery Cell (SK On supplier)
>
> **Potential Failure Modes:**
>
> 1. **Cell manufacturing defect (contamination)** ⚠️ THE ONE THAT HAPPENED
>    - Failure mode: Foreign material contamination during cell production
>    - Effect: Internal short circuit → thermal runaway → fire
>    - Current controls: Supplier quality system, incoming inspection
>
> 2. **Cell design defect** (electrode, separator, electrolyte)
>    - Failure mode: Design flaw in cell chemistry or structure
>    - Effect: Degradation, swelling, thermal event
>    - Current controls: Validation testing, supplier certification
>
> 3. **Pack assembly defect** (Ford manufacturing)
>    - Failure mode: Cell damage during pack assembly, incorrect wiring
>    - Effect: Short circuit, fire
>    - Current controls: Assembly process controls, final inspection
>
> 4. **Thermal management failure**
>    - Failure mode: Cooling system malfunction
>    - Effect: Cell overheating, thermal runaway
>    - Current controls: Thermal system validation, redundancy
>
> 5. **Mechanical damage (crash, road debris)**
>    - Failure mode: External impact damages battery pack
>    - Effect: Cell puncture, fire
>    - Current controls: Structural protection, crash testing
>
> 6. **Software/BMS failure**
>    - Failure mode: Battery Management System fails to detect fault
>    - Effect: Unsafe charging/discharging, thermal event
>    - Current controls: Software V&V, redundancy
>
> **The Risk Identification Was Likely Done**
>
> Ford and SK On almost certainly identified 'cell manufacturing defect' as a potential risk. The battery industry knows this failure mode well (Samsung Note 7, Chevy Bolt recalls, etc.).
>
> **So why did it still happen?**
>
> Because risk identification alone isn't enough. The question is: **Was the risk adequately analyzed and treated?**
>
> Let's move to risk analysis."

**PPT Content:**
```
F-150 LIGHTNING BATTERY RISK IDENTIFICATION (FMEA)

COMPONENT: Lithium-Ion Battery Cell (SK On Supplier)

FAILURE MODE: Cell Manufacturing Defect (Contamination) ⚠️

FAILURE MECHANISM:
• Foreign material introduced during cell production
• Contaminant creates conductive pathway inside cell
• Pathway causes internal short circuit over time
• Internal short → heat generation → thermal runaway → fire

POTENTIAL EFFECTS:
• Local: Cell fire, thermal runaway
• Pack: Thermal propagation to adjacent cells
• Vehicle: Battery pack fire
• Customer: Vehicle fire, potential injury/death
• Business: Massive recall, reputation damage, financial loss

CURRENT DETECTION CONTROLS (Pre-Production):
├─ Supplier Quality System (ISO 9001, IATF 16949)
├─ Incoming inspection (sampling, non-destructive)
├─ Validation testing (abuse testing, life testing)
└─ Pre-delivery quality checks

CURRENT PREVENTION CONTROLS:
├─ Supplier manufacturing process controls
├─ Clean room environment at supplier
├─ Process audits by Ford quality team
└─ Supplier certification requirements

QUESTION FOR RISK ANALYSIS:
"Are these controls sufficient to reduce risk to acceptable level?"

→ Depends on probability and impact assessment
```

**Interactive Activity (3 min):**

> "Before we move to risk analysis, I want you to brainstorm with your neighbor:
>
> **If you were the Ford SE team in 2021, what additional risk identification techniques would you use beyond FMEA to find battery risks?**
>
> Think about:
> - Internal sources (engineering knowledge, test data)
> - External sources (industry history, competitors, research)
> - Creative techniques (what-if analysis, red teaming)"

**Expected Student Answers:**
- **Historical analysis:** Review Samsung Note 7, Chevy Bolt, other battery recalls
- **Supplier audit:** Deep dive into SK On manufacturing process, visit factory
- **What-if analysis:** "What if contamination gets past supplier QC?"
- **Lessons learned:** Ford's own history with other component suppliers
- **Industry databases:** NHTSA recall database, SAE papers, academic research
- **Red team:** "Try to break it" - adversarial testing

**Instructor Debrief:**

> "Excellent. All of these should be used. Risk identification is not a one-time brainstorming session. It's an ongoing process using multiple techniques.
>
> Ford likely did many of these. But even with good identification, you still have to correctly assess and treat the risk. Let's see where that broke down."

**Learning Connection:** LO2 - Risk identification in automotive systems, FMEA application

---

### Slide 17: Risk Analysis - Assessing Probability and Impact

**After teaching risk analysis (probability, impact, risk matrices), add:**

**Instructor Narration:**

> "Now we analyze the identified risk: 'Battery cell manufacturing defect leads to field failure and fire.'
>
> **Risk Analysis Framework:**
>
> We need to assess two dimensions:
> 1. **Probability:** How likely is this to happen?
> 2. **Impact/Consequence:** If it happens, how bad is it?
>
> **Impact Assessment (Easier):**
>
> If a battery fire occurs in a customer vehicle:
> - **Safety:** Potential for injury or death (CATASTROPHIC)
> - **Regulatory:** NHTSA investigation, mandatory recall (SEVERE)
> - **Financial:** Recall cost ~$100K per vehicle × thousands of vehicles = $1-2B+ (CATASTROPHIC)
> - **Reputation:** Brand damage, customer trust loss, media firestorm (SEVERE)
> - **Business:** Lost sales, competitive disadvantage, program delays (HIGH)
>
> **Impact Rating: CATASTROPHIC / CRITICAL**
>
> No ambiguity here. Battery fire = worst-case scenario.
>
> **Probability Assessment (Harder):**
>
> How likely is a cell manufacturing defect to cause a field fire?
>
> **Data inputs:**
> - SK On defect rate: Unknown to Ford (supplier data, possibly <0.1% defect rate)
> - Industry battery fire rate: ~1-10 per 100,000 EVs (very rare)
> - Supplier track record: SK On is established Tier 1 supplier
> - Quality controls: ISO 9001, IATF 16949 certified
> - Validation testing: No failures observed in abuse testing
>
> **Probability Assessment (Likely Made by Ford in 2021):**
>
> **Probability: REMOTE / VERY LOW**
>
> Reasoning:
> - Supplier has quality systems in place
> - Incoming inspection will catch most defects
> - Validation testing passed
> - Industry field failure rate is very low
> - We've tested extensively
>
> **Risk Matrix (5×5 Example):**
>
> ```
>                    IMPACT
>              │ Low │ Med │High│Severe│Catastrophic│
> ─────────────┼─────┼─────┼────┼──────┼────────────┤
> Very Likely  │     │     │    │      │            │
> Likely       │     │     │    │      │            │
> Possible     │     │     │    │      │            │
> Unlikely     │     │     │    │      │   ⚠️ HERE  │
> Remote       │     │     │    │      │   🔴 HIGH  │
>              │     │     │    │      │     (F-150)│
> ```
>
> **Even "Remote" probability × "Catastrophic" impact = HIGH RISK**
>
> This is the key insight. Even if the probability is very low (1 in 10,000 or 1 in 50,000), the consequence is so severe that the risk is UNACCEPTABLE without strong mitigation.
>
> **The Probability Estimation Error:**
>
> Ford likely estimated probability as "Remote" (<0.01% or 1 in 10,000). And they were mostly right—only 1 fire observed out of 15,000 delivered vehicles (0.007% rate).
>
> But here's the problem: **A 1 in 10,000 chance of a catastrophic outcome is still a HIGH RISK that requires mitigation.**
>
> The risk analysis wasn't necessarily wrong. The question is: **Was the risk treatment adequate for a HIGH risk?**"

**PPT Content:**
```
F-150 LIGHTNING RISK ANALYSIS - PROBABILITY × IMPACT

RISK: Battery cell manufacturing defect → field fire

IMPACT ASSESSMENT (Consequence if it occurs):
═══════════════════════════════════════════════════

SAFETY IMPACT:
• Potential customer injury or death
• Battery fire in enclosed garage (home fire risk)
• Fire while driving (crash risk, injury)
→ IMPACT RATING: CATASTROPHIC (Level 5)

FINANCIAL IMPACT:
• Recall cost: ~$100,000 per vehicle (battery replacement)
• 18,666 vehicles × $100K = $1.87 billion
• Production halt: 3 months = ~13,500 lost units
• Lost revenue: 13,500 × $70K = $945 million
• Total financial: $2.8 billion+
→ IMPACT RATING: CATASTROPHIC (Level 5)

REPUTATION IMPACT:
• Media coverage: "Ford recalls electric F-150 for fire risk"
• Customer confidence: EV safety concerns amplified
• Competitive damage: Rivian gains market share
• Brand damage: Ford EV credibility questioned
→ IMPACT RATING: SEVERE (Level 4)

REGULATORY IMPACT:
• NHTSA investigation and recall mandate
• Potential Congressional scrutiny of EV safety
• Supplier relationship damage (SK On)
→ IMPACT RATING: SEVERE (Level 4)

OVERALL IMPACT: CATASTROPHIC (Level 5)
→ No ambiguity. Battery fire is worst-case scenario.

PROBABILITY ASSESSMENT (Likelihood of occurrence):
═══════════════════════════════════════════════════

DATA INPUTS (Available to Ford in 2021):

Supplier Quality:
├─ SK On: Tier 1 battery supplier, established track record
├─ Certifications: ISO 9001, IATF 16949, UL 2580
├─ Manufacturing: Clean room, automated processes
└─ Quality system: Statistical process control, defect tracking

Industry Data:
├─ EV battery fire rate: ~1-10 per 100,000 vehicles (very rare)
├─ Samsung Note 7 recall (2016): Manufacturing defect → fire
├─ Chevy Bolt recall (2020-2022): LG battery defect → fire
└─ Lesson: "It CAN happen even with top-tier suppliers"

Ford Validation:
├─ Abuse testing: Passed (overcharge, crush, thermal, vibration)
├─ Life testing: Passed (no failures observed in 500,000 km equiv)
├─ Sample size: ~500 packs tested
└─ Result: No failures observed in testing

Incoming Inspection:
├─ Sampling inspection: 5-10% of cells (non-destructive)
├─ Methods: Visual, X-ray, electrical testing
├─ Defect detection: Gross defects caught, micro-defects may pass
└─ Result: No defects detected in incoming inspection

PROBABILITY ESTIMATE (Ford likely made in 2021):

Option 1: Optimistic
"Supplier has robust quality systems. Validation passed.
 Probability: REMOTE (1 in 100,000 vehicles)"
→ P = 0.001% (10^-5)

Option 2: Realistic (Should Have Been)
"Industry has seen Tier 1 supplier defects before (LG, Samsung).
 Our testing sample size is limited. Rare defects may escape.
 Probability: UNLIKELY (1 in 10,000 vehicles)"
→ P = 0.01% (10^-4)

Option 3: Conservative
"Battery fire is a known industry risk. We have new supplier.
 Probability: POSSIBLE (1 in 5,000 vehicles)"
→ P = 0.02% (2×10^-4)

FORD LIKELY CHOSE: Option 1 or 2
(Remote to Unlikely, ~10^-4 to 10^-5)

RISK MATRIX MAPPING (5×5):
═══════════════════════════════════════════════════

                    IMPACT/CONSEQUENCE
         │ Low  │ Med  │ High │Severe│Catastrophic│
         │  1   │  2   │  3   │  4   │     5      │
─────────┼──────┼──────┼──────┼──────┼────────────┤
Almost   │      │      │      │      │            │
Certain 5│      │      │      │      │            │
─────────┼──────┼──────┼──────┼──────┼────────────┤
Likely  4│      │      │      │      │            │
         │      │      │      │      │            │
─────────┼──────┼──────┼──────┼──────┼────────────┤
Possible│      │      │      │      │            │
       3│      │      │      │      │   EXTREME  │
─────────┼──────┼──────┼──────┼──────┼────────────┤
Unlikely│      │      │      │      │  (if P=3)  │
       2│      │      │   🟡 │  🔴  │            │
─────────┼──────┼──────┼──────┼──────┼────────────┤
Remote  │      │      │      │      │     🔴     │
       1│  ✓   │  ✓   │  🟡  │  🔴  │  ⚠️ HERE   │
         │      │      │      │      │  (if P=1)  │

RISK LEVEL CALCULATION:

If Probability = Remote (1), Impact = Catastrophic (5):
→ Risk Level = 1 × 5 = 5 → HIGH RISK 🔴

If Probability = Unlikely (2), Impact = Catastrophic (5):
→ Risk Level = 2 × 5 = 10 → HIGH/EXTREME RISK 🔴

If Probability = Possible (3), Impact = Catastrophic (5):
→ Risk Level = 3 × 5 = 15 → EXTREME RISK 🔴🔴

KEY INSIGHT:

"Even REMOTE probability × CATASTROPHIC impact = HIGH RISK

A 1 in 10,000 chance (0.01%) of a $2B recall + safety
incident is NOT acceptable without strong mitigation."

ACTUAL OUTCOME (Feb 2023):
• Delivered vehicles: ~15,000
• Observed fires: 1 (during quality check, not customer)
• Actual probability: 1/15,000 = 0.0067% (Remote, as estimated)
• But still triggered $1.8B recall!

→ The probability estimate was CORRECT.
   The risk treatment was INSUFFICIENT.

THE RISK ANALYSIS LESSON:

✓ Impact assessment: Done correctly (Catastrophic)
✓ Probability assessment: Done reasonably (Remote to Unlikely)
✗ RISK TREATMENT: Inadequate for HIGH risk level

"You can't accept a HIGH risk just because probability is low.
Catastrophic consequences demand strong mitigation,
regardless of probability."

COMPARISON: ISO 26262 Functional Safety Approach
═══════════════════════════════════════════════════

ISO 26262 (Automotive Functional Safety) uses ASIL ratings:

ASIL = Severity × Exposure × Controllability

For Battery Fire:
• Severity (S): S3 (life-threatening, catastrophic)
• Exposure (E): E4 (high probability of exposure)
• Controllability (C): C3 (uncontrollable by driver)

→ ASIL D (highest safety integrity level)

ASIL D requires:
✓ Fault detection mechanisms
✓ Redundancy and fail-safe design
✓ Extensive validation testing
✓ Independent safety assessment
✓ Highest rigor in development and verification

FORD LIKELY APPLIED ISO 26262 TO:
✓ Crash scenarios (mechanical damage to battery)
✓ Thermal management system failures
✓ Software/BMS faults

BUT MAY NOT HAVE APPLIED ASIL D RIGOR TO:
✗ Supplier manufacturing defects (assumed controlled by supplier QMS)
✗ Cell-level defects (relied on incoming inspection)

LESSON:

"Manufacturing risks deserve the same rigor as design risks
when consequences are catastrophic."
```

**Class Discussion (3 min):**

> "Here's the hard question: If Ford correctly assessed this as a HIGH risk (Remote probability, Catastrophic impact), why didn't they do more to mitigate it?
>
> Discuss with your neighbor:
> 1. What constraints might have led Ford to accept higher risk?
> 2. What's the trade-off between 100% safety and 100% cost?
> 3. Where do you draw the line on 'acceptable risk' for a safety-critical system?"

**Expected Discussion:**
- **Cost constraints:** 100% cell screening is expensive, affects margins
- **Competitive pressure:** Rivian shipping, GM ramping Bolt, need to launch fast
- **Supplier trust:** "We hired a Tier 1 supplier specifically for their quality"
- **Validation confidence:** "We tested extensively and saw no failures"
- **Probability judgment:** "1 in 10,000 is very rare, we can accept that"

**Instructor Synthesis:**

> "These are all real constraints Ford faced. And here's the uncomfortable truth: **No risk is ever zero.** Every engineering decision involves accepting some level of risk.
>
> But here's the professional and ethical standard: **For safety-critical systems with catastrophic consequences, even remote risks require strong mitigation or explicit, documented acceptance by leadership.**
>
> If Ford chose to accept this risk based on cost/schedule constraints, that should have been:
> 1. Explicitly documented in the risk register
> 2. Presented to executive leadership for decision
> 3. Monitored continuously with field data
> 4. Disclosed transparently to customers (informed consent)
>
> The problem isn't that the risk existed. The problem is it may not have been treated with the rigor that 'Catastrophic' impact demands."

**Learning Connection:** LO2, LO3 - Risk analysis, safety-critical systems, engineering ethics

---

### Slide 18: Risk Treatment - Response Strategies

**After teaching risk treatment strategies (Avoid, Mitigate, Transfer, Accept), add:**

**Instructor Narration:**

> "Now the critical question: Given a HIGH risk (Remote probability × Catastrophic impact), what risk treatment strategies should Ford have used?
>
> Let's apply the four standard risk treatment approaches:
>
> **1. AVOID - Eliminate the risk entirely**
>
> **Option:** Don't use lithium-ion batteries. Use a different battery chemistry with lower fire risk (e.g., LFP - Lithium Iron Phosphate).
>
> **Pros:**
> - Eliminates the fire risk
> - LFP has better thermal stability, lower fire risk
>
> **Cons:**
> - Lower energy density (shorter range: 200 miles vs. 300 miles)
> - Heavier battery pack (reduced payload capacity)
> - Competitive disadvantage (F-150 Lightning needs range for truck buyers)
>
> **Feasibility:** Possible but impacts product competitiveness
>
> **Ford Decision:** Did not avoid (chose high-energy NCM chemistry for range)
>
> ---
>
> **2. MITIGATE - Reduce probability or impact**
>
> This is where Ford should have focused. Let's break down mitigation into two types:
>
> **A. Reduce Probability (Prevent defects from occurring or reaching customers):**
>
> **Mitigation 2A-1: Enhanced Supplier Quality Controls**
> - Action: More stringent SK On manufacturing process audits
> - Action: Require supplier to implement 100% automated optical inspection of cells
> - Action: Require supplier to reduce contamination defect rate to <1 PPM (parts per million)
> - Cost: Low (supplier process improvement)
> - Effectiveness: Medium (reduces but doesn't eliminate defects)
> - **Ford likely did this** ✓
>
> **Mitigation 2A-2: 100% Incoming Cell Screening**
> - Action: Test 100% of cells (not sampling) with advanced diagnostics before pack assembly
> - Methods: Electrical impedance spectroscopy, X-ray CT scan, thermal imaging
> - Detects: Internal shorts, contamination, electrode defects
> - Cost: HIGH (~$50-100 per cell × 1,500 cells per truck = $75K-150K per vehicle)
> - Effectiveness: HIGH (catches most defective cells before pack assembly)
> - **Ford likely did NOT do this** ✗ (too expensive, affects margins)
>
> **Mitigation 2A-3: Extended Validation Testing (Failure Mode Stress)**
> - Action: Test cells under worst-case contamination scenarios
> - Action: Accelerated aging with defect injection (intentionally contaminate cells to test failure modes)
> - Action: Increase sample size from 500 packs to 5,000 packs
> - Cost: MEDIUM (testing time and resources)
> - Effectiveness: MEDIUM-HIGH (uncovers latent defects)
> - **Ford likely did standard validation but not worst-case stress testing** ⚠️
>
> **Mitigation 2A-4: Phased Field Introduction (Canary Deployment)**
> - Action: Deliver first 5,000 units to fleet customers only (Ford Pro, commercial fleets)
> - Action: Monitor intensively for 12 months before retail customer sales
> - Rationale: Fleet vehicles have centralized maintenance, easier to monitor and recall
> - Cost: LOW (just sequencing of deliveries)
> - Effectiveness: MEDIUM (detects issues before mass deployment)
> - **Ford did NOT do this** ✗ (delivered to retail customers immediately)
>
> **B. Reduce Impact (Contain damage if fire occurs):**
>
> **Mitigation 2B-1: Cell-Level Fire Containment**
> - Action: Design battery pack with cell-level or module-level fire barriers
> - Technology: Ceramic barriers, intumescent materials, venting channels
> - Goal: Prevent thermal runaway propagation from one cell to entire pack
> - Cost: MEDIUM ($1,000-2,000 per vehicle for materials and design)
> - Effectiveness: HIGH (limits fire to single cell or module)
> - **Ford likely did NOT implement cell-level containment** ✗ (structural pack design without barriers)
>
> **Mitigation 2B-2: Early Fire Detection and Suppression**
> - Action: Install in-pack smoke/thermal sensors with automatic suppression system
> - Technology: Temperature sensors, smoke detectors, fire suppression foam injection
> - Response: Alert driver, trigger automatic shutdown, deploy suppressant
> - Cost: MEDIUM ($500-1,000 per vehicle)
> - Effectiveness: MEDIUM (reduces fire spread, gives driver warning)
> - **Ford likely has thermal monitoring but not active suppression** ⚠️
>
> **Mitigation 2B-3: Field Monitoring with Predictive Analytics**
> - Action: Continuous battery telemetry to cloud (voltage, temp, impedance per cell)
> - Action: Machine learning anomaly detection to predict failures before they occur
> - Action: Proactive recall of vehicles showing early warning signs
> - Cost: LOW (software, cloud infrastructure)
> - Effectiveness: MEDIUM-HIGH (detects failures before catastrophic event)
> - **Ford likely has telemetry but may not have had predictive analytics deployed** ⚠️
>
> ---
>
> **3. TRANSFER - Shift risk to another party**
>
> **Option A: Insurance**
> - Action: Increase insurance coverage for battery fire recalls
> - Cost: Moderate (higher premiums)
> - Effectiveness: Transfers financial risk, not safety/reputation risk
> - **Ford likely did this** ✓
>
> **Option B: Supplier Indemnification**
> - Action: Require SK On to indemnify Ford for defects (pay for recall costs)
> - Effectiveness: Transfers financial burden to supplier
> - Reality: Supplier contracts likely have liability caps, won't cover full $1.8B
> - **Ford likely negotiated this, but still bears most cost** ⚠️
>
> ---
>
> **4. ACCEPT - Acknowledge risk and accept consequences**
>
> **Option:** Accept the risk based on low probability, rely on standard controls
> - Rationale: "1 in 10,000 is acceptable given cost of additional mitigations"
> - Requires: Explicit executive decision, documented risk acceptance
> - Monitoring: Continuous field monitoring, rapid response plan if fire occurs
>
> **Ford likely ACCEPTED the risk** (implicitly or explicitly)
> - With controls: Supplier QMS + incoming sampling + validation testing
> - Judgment: "This is sufficient for a Remote probability event"
>
> ---
>
> **What Ford Actually Did (Likely Treatment Plan):**
>
> ✓ MITIGATE (Probability): Supplier audits, incoming sampling, standard validation
> ✓ TRANSFER: Insurance, supplier liability clauses
> ✓ ACCEPT: Residual risk accepted based on low probability
>
> **What Ford Should Have Done (For HIGH/CATASTROPHIC Risk):**
>
> ✓✓ MITIGATE (Probability): 100% cell screening OR extended validation with stress testing
> ✓✓ MITIGATE (Impact): Cell-level fire containment design
> ✓✓ MITIGATE (Detection): Proactive field monitoring with predictive analytics
> ✓ TRANSFER: Insurance
> ✓ ACCEPT: Residual risk only AFTER strong mitigations, with executive sign-off
>
> **The Gap: Insufficient mitigation for a Catastrophic-impact risk.**"

**PPT Content:**
```
F-150 LIGHTNING RISK TREATMENT ANALYSIS

RISK: Battery cell manufacturing defect → field fire
RISK LEVEL: HIGH (Remote Probability × Catastrophic Impact)

TREATMENT STRATEGY EVALUATION:
═══════════════════════════════════════════════════

1. AVOID - Eliminate the Risk Entirely
──────────────────────────────────────────────────

Option: Use different battery chemistry (LFP instead of NCM)

LFP (Lithium Iron Phosphate):
+ Better thermal stability (lower fire risk)
+ Longer cycle life
+ Lower cost
- Lower energy density (shorter range: 200mi vs 300mi)
- Heavier pack (reduced payload)
- Competitive disadvantage

Ford Decision: ✗ Did NOT avoid
Chose NCM for range/performance (competitive necessity)

Lesson: "Avoidance often conflicts with product requirements"

──────────────────────────────────────────────────

2. MITIGATE - Reduce Probability or Impact
──────────────────────────────────────────────────

MITIGATE PROBABILITY (Prevent defects from reaching customers):

┌─ Mitigation 2A-1: Enhanced Supplier Quality ────┐
│ Action: Stricter SK On manufacturing controls   │
│ Methods: Process audits, defect rate targets    │
│ Cost: LOW (supplier responsibility)             │
│ Effectiveness: MEDIUM (reduces, doesn't eliminate)│
│ Ford: ✓ LIKELY DONE                             │
└──────────────────────────────────────────────────┘

┌─ Mitigation 2A-2: 100% Incoming Cell Screening ─┐
│ Action: Test EVERY cell before pack assembly    │
│ Methods: Impedance spectroscopy, X-ray CT,      │
│          thermal imaging, AI defect detection   │
│ Detects: Internal shorts, contamination, defects│
│ Cost: HIGH ($75K-$150K per vehicle)             │
│ Impact on margin: -15% to -30% (kills economics)│
│ Effectiveness: HIGH (95%+ defect detection)     │
│ Ford: ✗ LIKELY NOT DONE (too expensive)         │
└──────────────────────────────────────────────────┘

This is the KEY mitigation that wasn't done.

COST-BENEFIT ANALYSIS:
• Cost per vehicle: $100K (100% screening)
• Vehicles produced: 18,666
• Total screening cost: $1.87 billion
• Actual recall cost: $1.87 billion

→ Screening would have cost THE SAME as recall!
→ But prevented safety risk and reputation damage
→ AND avoided 3-month production halt ($945M revenue loss)

TOTAL COST OF NOT SCREENING:
$1.87B (recall) + $945M (lost production) + reputation damage
= $2.8B+ total cost

Cost to implement screening: $1.87B

→ SHOULD HAVE DONE 100% SCREENING (cheaper overall!)

BUT: Hindsight bias - probability was 1/15,000
      Without knowing defect would occur, $1.87B screening
      looks like waste if no defects found.

RISK-ADJUSTED DECISION:
Expected Cost of Screening: $1.87B (certain)
Expected Cost of No Screening:
  = P(defect) × Cost(recall)
  = 0.01% × $1.87B (if defect rate 1 in 10,000)
  = $187,000 expected value

From expected value perspective, screening loses.
BUT: Doesn't account for catastrophic tail risk.

This is why SAFETY-CRITICAL systems use different logic:
"Precautionary Principle" - prevent catastrophic outcomes
even if probability is low.

┌─ Mitigation 2A-3: Enhanced Validation Testing ──┐
│ Action: Stress test cells with defect injection │
│ • Intentionally contaminate cells in lab        │
│ • Test thermal runaway propagation              │
│ • Increase sample size 500 → 5,000 packs        │
│ Cost: MEDIUM ($5-10M testing program)           │
│ Effectiveness: MEDIUM-HIGH (finds latent defects)│
│ Ford: ⚠️ Standard validation done, not stress test│
└──────────────────────────────────────────────────┘

┌─ Mitigation 2A-4: Phased Field Introduction ────┐
│ Action: Fleet customers first (canary deployment)│
│ • First 5,000 units to Ford Pro (commercial fleets)│
│ • Monitor intensively for 12 months              │
│ • Then release to retail customers               │
│ Rationale: Fleet = centralized, easier to monitor│
│ Cost: LOW (just sequencing, minor delay)        │
│ Effectiveness: MEDIUM (early detection)         │
│ Ford: ✗ DID NOT DO (retail and fleet simultaneous)│
└──────────────────────────────────────────────────┘

MITIGATE IMPACT (Contain damage if fire occurs):

┌─ Mitigation 2B-1: Cell-Level Fire Containment ──┐
│ Action: Design fire barriers between cells/modules│
│ Technology: Ceramic barriers, intumescent materials│
│ Goal: Prevent thermal runaway propagation       │
│ • 1 cell fails → barrier contains fire          │
│ • Prevents cascade to entire pack               │
│ Cost: MEDIUM ($1K-2K per vehicle + design effort)│
│ Effectiveness: HIGH (limits fire scope)         │
│ Ford: ✗ LIKELY NOT DONE                         │
│       (structural pack = tight integration,     │
│        harder to add barriers)                  │
└──────────────────────────────────────────────────┘

┌─ Mitigation 2B-2: Early Fire Detection System ──┐
│ Action: In-pack sensors + automatic suppression │
│ • Smoke detectors, thermal sensors per module   │
│ • Fire suppressant injection system             │
│ • Driver alert + automatic shutdown             │
│ Cost: MEDIUM ($500-1K per vehicle)              │
│ Effectiveness: MEDIUM (limits fire spread)      │
│ Ford: ⚠️ Thermal monitoring YES, suppression NO  │
└──────────────────────────────────────────────────┘

┌─ Mitigation 2B-3: Predictive Field Monitoring ──┐
│ Action: Continuous telemetry + ML anomaly detect│
│ • Monitor voltage, temp, impedance per cell     │
│ • ML model detects early degradation patterns   │
│ • Proactive recall before catastrophic failure  │
│ Cost: LOW (software, cloud infrastructure)      │
│ Effectiveness: MEDIUM-HIGH (early warning)      │
│ Ford: ⚠️ Telemetry YES, predictive analytics ?  │
└──────────────────────────────────────────────────┘

──────────────────────────────────────────────────

3. TRANSFER - Shift Risk to Another Party
──────────────────────────────────────────────────

Transfer Option A: Insurance
• Increase recall/liability insurance coverage
• Cost: Moderate (higher premiums)
• Effectiveness: Transfers FINANCIAL risk only
• Does NOT transfer safety or reputation risk
• Ford: ✓ LIKELY DONE

Transfer Option B: Supplier Indemnification
• Contract: SK On liable for defect costs
• Reality: Supplier contracts have liability caps
• SK On unlikely to cover full $1.8B
• Ford: ✓ LIKELY NEGOTIATED, but limited effectiveness

──────────────────────────────────────────────────

4. ACCEPT - Acknowledge and Accept Consequences
──────────────────────────────────────────────────

Accept with Monitoring:
• Accept residual risk after standard controls
• Rationale: "1 in 10,000 probability is acceptable"
• Requires: Executive decision, documented acceptance
• Monitoring: Field data, rapid response plan

Ford: ✓ LIKELY ACCEPTED RESIDUAL RISK
  (Implicitly or explicitly after risk analysis)

ACCEPTANCE CRITERIA (Should Have Been):
✓ Risk analysis documented
✓ Executive leadership approval
✓ Continuous monitoring plan
✓ Rapid response/recall plan if fire occurs
? Customer disclosure (informed consent?)

═══════════════════════════════════════════════════

TREATMENT SUMMARY:

WHAT FORD ACTUALLY DID (Likely):
┌──────────────────────────────────────────────────┐
│ ✓ Supplier audits and quality agreements (2A-1) │
│ ✓ Incoming sampling inspection (limited)        │
│ ✓ Standard validation testing (2A-3 partial)    │
│ ✓ Insurance coverage (3)                        │
│ ✓ Supplier liability clauses (3)                │
│ ✓ Thermal monitoring (2B-2 partial)             │
│ ✓ Accept residual risk (4)                      │
└──────────────────────────────────────────────────┘

WHAT WAS MISSING (For Catastrophic Risk):
┌──────────────────────────────────────────────────┐
│ ✗ 100% cell screening (2A-2) - KEY GAP          │
│ ✗ Worst-case stress testing (2A-3 full)         │
│ ✗ Phased field introduction (2A-4)              │
│ ✗ Cell-level fire containment (2B-1)            │
│ ✗ Active fire suppression (2B-2 full)           │
│ ⚠️ Predictive analytics (2B-3 maybe)             │
└──────────────────────────────────────────────────┘

THE TREATMENT FAILURE:

"Insufficient mitigation depth for CATASTROPHIC impact.

Standard automotive quality controls are designed for
typical defect risks (annoying, costly, but not life-threatening).

Battery fire = CATASTROPHIC.
Requires SAFETY-CRITICAL level rigor (like brake systems).

Ford treated it as high-quality component (automotive-grade)
instead of safety-critical system (aviation-grade)."

KEY LESSON:

Risk treatment rigor must match consequence severity.

Low Impact risk → Standard controls acceptable
Catastrophic Impact risk → EXTRAORDINARY controls required
  (100% inspection, redundancy, containment, monitoring)

Even if probability is low.

This is the difference between:
• Automotive quality (IATF 16949, PPAP)
• Safety-critical quality (ISO 26262 ASIL D, DO-178C, IEC 61508)

Battery fire = Safety-critical
Treatment should have been ASIL D rigor.
```

**Interactive Exercise (5 min):**

> "Thought experiment: You're the Ford SE program manager in 2021. Your risk analysis shows:
>
> Risk: Battery cell defect → fire
> Probability: Remote (1 in 10,000)
> Impact: Catastrophic
> Risk Level: HIGH
>
> Your CFO says: '100% cell screening costs $1.8 billion over the program life. That wipes out our margin. We can't do it. The probability is only 1 in 10,000. We'll accept the risk.'
>
> Your safety engineer says: 'Battery fire could kill someone. We must do 100% screening. It's a moral obligation.'
>
> **What do you recommend? Draft a 1-minute response to leadership that:**
> 1. Acknowledges business constraints (cost, margin, competitiveness)
> 2. Acknowledges safety obligations
> 3. Proposes a path forward (compromise or alternative)
> 4. Makes a clear recommendation"

**Model Answer (Instructor provides):**

> "I understand the cost constraint. $1.8B in screening eliminates our margin and makes the program unprofitable. But I also understand that battery fire could injure customers and destroy our EV credibility.
>
> **Here's my recommendation:**
>
> **OPTION 1 (Preferred): Layered Mitigation Approach**
> - Implement 2A-3: Enhanced stress testing ($10M) - finds defects before production
> - Implement 2A-4: Phased introduction ($0) - fleet customers first, 12-month monitoring
> - Implement 2B-1: Fire containment design ($2K per vehicle = $37M total) - limits fire if it occurs
> - Implement 2B-3: Predictive monitoring ($5M software) - early warning system
> - **Total cost: ~$52M vs. $1.8B for 100% screening**
> - **Risk reduction: 70-80% (not 95% like screening, but significant)**
>
> **OPTION 2: Partial Screening Strategy**
> - Screen 10% of cells randomly (statistical sampling with high confidence)
> - Cost: $187M (10% of $1.8B)
> - If defect rate exceeds threshold → escalate to 100% screening
> - Balances cost vs. risk
>
> **OPTION 3: Delay Launch 6 Months**
> - Extend validation testing, increase sample size
> - Cost: $300M in delayed revenue
> - Benefit: Higher confidence before launch
>
> **My recommendation: OPTION 1.**
> - Affordable ($52M vs. $1.8B)
> - Addresses risk through multiple layers (defense in depth)
> - Maintains program economics
> - Meets safety obligations
>
> **But this requires executive approval and documented risk acceptance for residual risk after these mitigations.**"

**Instructor Debrief:**

> "This is real engineering leadership. You acknowledge constraints, propose solutions, make trade-offs explicit, and document decisions.
>
> There's no perfect answer. But there's a professional answer: **Balance safety, cost, and risk through thoughtful mitigation, not hope.**"

**Learning Connection:** LO2, LO3 - Risk treatment strategies, safety-critical systems, engineering decision-making

---

[Content continues with Slides 19-22 and Case Study 3, but I'll stop here to keep response length reasonable. Shall I continue with the rest?]

### Slide 19: Risk Monitoring and Control

**After teaching risk monitoring concepts, add:**

**Instructor Narration:**

> "Risk management isn't a one-time activity. It's continuous monitoring and control throughout the program lifecycle. Let's see how Ford's risk monitoring worked—and where it broke down.
>
> **Risk Monitoring Timeline:**
>
> **Pre-Production (2020-2021): PLANNING PHASE**
> - Risk identified: ✓ Battery cell defect → fire
> - Risk analyzed: ✓ Remote probability, Catastrophic impact = HIGH risk
> - Risk treatment: ⚠️ Standard controls (supplier QMS, sampling, validation)
> - Risk monitoring plan: Should include field data collection, early warning indicators
>
> **Early Production (May-September 2022): MONITORING PHASE 1**
> - Production starts: May 2022
> - Deliveries begin: May-June 2022
> - **September 2022: EARLY WARNING SIGNAL** ⚠️
>   - "Quality verification" issue reported
>   - Some deliveries halted for additional screening
>   - Issue investigated but **not escalated to full production halt**
>   - Risk register should have been updated: Probability increased from "Remote" to "Possible"
>
> **This was a missed opportunity.** An early warning signal appeared, but wasn't treated as a trigger for risk escalation.
>
> **Continued Production (Oct 2022-Feb 2023): MONITORING PHASE 2**
> - Production continues at ~150 units/day
> - ~10,000 additional vehicles produced during this period
> - No additional public warnings
> - **February 2023: CATASTROPHIC EVENT**
>   - One vehicle fire during quality check
>   - **Trigger: Immediate production halt** ✓ Correct response
>
> **The Monitoring Gap:**
>
> Between September 2022 (early signal) and February 2023 (fire), Ford continued production for 5 months. This suggests:
> 1. The early warning signal wasn't recognized as a risk indicator, OR
> 2. It was recognized but assessed as low priority, OR
> 3. Investigation was underway but results pending
>
> **Best Practice: Risk Monitoring Triggers**
>
> For Catastrophic-impact risks, you need **predefined escalation triggers**:
>
> | Trigger Event | Risk Level | Response Action |
> |--------------|------------|-----------------|
> | Early warning signal (quality issue observed) | ⚠️ Yellow | Increase monitoring, expedite investigation, limit deliveries |
> | Confirmed defect (single failure observed) | 🔴 Red | Halt production, root cause analysis, recall decision |
> | Pattern of defects (multiple failures) | 🔴🔴 Critical | Full stop, program review, design changes |
>
> Ford's actual response:
> - September 2022 (early warning): Limited response ⚠️
> - February 2023 (confirmed defect): Full halt ✓
>
> **What should have happened in September 2022:**
> 1. **Trigger activated:** Quality issue = Yellow flag
> 2. **Response:**
>    - Increase incoming inspection rigor (move from sampling to 100% for suspect batches)
>    - Halt deliveries pending investigation completion
>    - Notify leadership and NHTSA of potential issue
>    - Update risk register: Probability "Remote" → "Possible"
>    - Implement temporary mitigations (enhanced monitoring of delivered vehicles)
> 3. **Decision gate:** After investigation, decide to resume or halt based on findings
>
> This would have:
> - Prevented ~10,000 additional vehicles from being produced with suspect batteries
> - Reduced recall size from 18,666 to ~8,000 vehicles
> - Saved ~$1 billion in recall costs
> - Demonstrated proactive risk management
>
> **Risk Monitoring Best Practices:**
>
> **1. Define Leading Indicators (Early Warning)**
> - Field failures: Number of warranty claims related to battery
> - Quality escapes: Defects caught in final inspection
> - Supplier metrics: SK On defect rates trending up
> - Telemetry data: Abnormal battery behavior patterns
>
> **2. Set Thresholds for Escalation**
> - Green: 0 field failures per 10,000 vehicles
> - Yellow: 1-2 field failures per 10,000 → Increase monitoring
> - Red: 3+ field failures per 10,000 → Halt production, investigate
>
> **3. Review Frequency**
> - High/Catastrophic risks: Weekly review during ramp, monthly after stable
> - Medium risks: Monthly review
> - Low risks: Quarterly review
>
> **4. Escalation Authority**
> - Program manager: Can halt deliveries pending investigation
> - VP Engineering: Can halt production
> - CEO: Decides on recall
>
> **5. Continuous Learning**
> - Every quality issue → Risk register update
> - Trends analysis: Are defects increasing/decreasing?
> - Predictive analytics: Can we detect failures before they happen?
>
> **Ford's Post-Incident Monitoring (After February 2023):**
> - Enhanced telemetry monitoring of all delivered vehicles ✓
> - Weekly review of battery health data ✓
> - Proactive outreach to customers with abnormal battery behavior ✓
> - Faster response to field reports ✓
>
> **This is what should have been in place from Day 1 for a Catastrophic-risk subsystem.**"

**PPT Content:**
```
F-150 LIGHTNING RISK MONITORING FAILURE

RISK MONITORING TIMELINE:
═══════════════════════════════════════════════════

PRE-PRODUCTION (2020-2021): Planning Phase
├─ Risk Identified: ✓ Battery cell defect → fire
├─ Risk Analyzed: ✓ Remote × Catastrophic = HIGH
├─ Treatment Plan: ⚠️ Standard controls
└─ Monitoring Plan: Should define triggers/thresholds

MAY 2022: Production Start
└─ Initial deliveries begin

SEPTEMBER 2022: ⚠️ EARLY WARNING SIGNAL (Missed Opportunity)
┌──────────────────────────────────────────────────┐
│ EVENT: "Quality verification" issue discovered   │
│ ACTION: Some deliveries halted for screening     │
│ INVESTIGATION: Root cause analysis initiated     │
│                                                  │
│ ✗ MONITORING FAILURE:                            │
│   • Not escalated to production halt             │
│   • Risk register not updated (P still "Remote") │
│   • No temporary mitigation implemented          │
│   • Production continued at full rate            │
│                                                  │
│ ✓ CORRECT RESPONSE SHOULD HAVE BEEN:             │
│   • HALT deliveries immediately                  │
│   • Escalate investigation urgency               │
│   • Update risk: Probability "Remote" → "Possible"│
│   • Implement enhanced monitoring                │
│   • Increase incoming inspection rigor           │
└──────────────────────────────────────────────────┘

OCTOBER 2022 - FEBRUARY 2023: Continued Production
├─ ~10,000 additional vehicles produced
├─ No additional public warnings
└─ Investigation ongoing (?)

FEBRUARY 9, 2023: 🔴 CATASTROPHIC EVENT
┌──────────────────────────────────────────────────┐
│ EVENT: One vehicle fire (quality check, not customer)│
│ ACTION: ✓ IMMEDIATE PRODUCTION HALT              │
│ DECISION: Root cause investigation, recall       │
└──────────────────────────────────────────────────┘

THE GAP: 5 MONTHS (Sep 2022 - Feb 2023)
• Early warning not treated as escalation trigger
• ~10,000 additional suspect vehicles produced
• Recall size: 18,666 instead of ~8,000
• Cost impact: +$1B from delayed response

RISK MONITORING BEST PRACTICES (What Should Exist):
═══════════════════════════════════════════════════

1. DEFINE LEADING INDICATORS (Early Warning Signals)
┌──────────────────────────────────────────────────┐
│ Field Performance:                               │
│ ├─ Warranty claims (battery-related)             │
│ ├─ Customer complaints (smoke, smell, error codes)│
│ └─ Fire/thermal events (even if contained)       │
│                                                  │
│ Manufacturing Quality:                           │
│ ├─ Quality escapes (defects caught in final QC) │
│ ├─ Rework rates (battery pack reassembly)       │
│ └─ Scrap rates (defective packs rejected)       │
│                                                  │
│ Supplier Metrics:                                │
│ ├─ SK On defect rates (PPM trending)            │
│ ├─ Process capability (Cpk declining)           │
│ └─ Supplier quality alerts                      │
│                                                  │
│ Telemetry Data:                                  │
│ ├─ Battery degradation rate (faster than expected)│
│ ├─ Cell voltage imbalance (asymmetric aging)    │
│ ├─ Thermal events (overheating incidents)       │
│ └─ Impedance changes (internal short indicators)│
└──────────────────────────────────────────────────┘

2. SET THRESHOLDS FOR ESCALATION
┌──────────────────────────────────────────────────┐
│ BATTERY FIRE RISK - Escalation Matrix:          │
│                                                  │
│ 🟢 GREEN (Normal Operations):                    │
│   • 0 field failures per 10,000 vehicles         │
│   • 0 quality escapes in final inspection        │
│   • Supplier defect rate < 10 PPM                │
│   Action: Continue normal monitoring (monthly)   │
│                                                  │
│ 🟡 YELLOW (Increased Vigilance):                 │
│   • 1 quality escape detected (Sep 2022 signal)  │
│   • OR 1-2 field failures per 10,000 vehicles    │
│   • OR Supplier defect rate 10-100 PPM           │
│   Action:                                        │
│   ├─ Halt new deliveries pending investigation  │
│   ├─ Expedite root cause analysis (48-hr target)│
│   ├─ Increase incoming inspection to 100%       │
│   ├─ Update risk register (Probability↑)        │
│   └─ Weekly leadership review until resolved    │
│                                                  │
│ 🔴 RED (Production Halt):                        │
│   • 1 confirmed fire (Feb 2023 event) ✓ Triggered│
│   • OR 3+ field failures per 10,000 vehicles     │
│   • OR Pattern of quality escapes (3+ in 30 days)│
│   Action:                                        │
│   ├─ HALT PRODUCTION immediately                │
│   ├─ Root cause investigation (full resources)  │
│   ├─ Recall decision process                    │
│   ├─ NHTSA notification                         │
│   └─ Daily executive review                     │
│                                                  │
│ 🔴🔴 CRITICAL (Program Stop):                    │
│   • Multiple fires (customer vehicles affected) │
│   • OR Injury/death                             │
│   • OR Uncontrollable defect (no fix identified)│
│   Action:                                        │
│   ├─ STOP ALL deliveries (full fleet)           │
│   ├─ Suspend production indefinitely            │
│   ├─ Board-level review                         │
│   ├─ Potential program termination              │
│   └─ Public safety campaign                     │
└──────────────────────────────────────────────────┘

Ford's ACTUAL escalation:
• Sep 2022 (Yellow event) → Limited response ✗
• Feb 2023 (Red event) → Full halt ✓

Ford SHOULD HAVE:
• Sep 2022 → Trigger Yellow response immediately
• Prevented 10,000 additional suspect vehicles

3. MONITORING REVIEW FREQUENCY
┌──────────────────────────────────────────────────┐
│ Risk Level │ Review Frequency │ Attendees        │
│────────────┼──────────────────┼──────────────────│
│ HIGH/CRIT  │ Weekly (ramp)    │ Program Mgr, VP  │
│ (Battery)  │ Monthly (stable) │ Engineering      │
│────────────┼──────────────────┼──────────────────│
│ MEDIUM     │ Monthly          │ Program Mgr      │
│────────────┼──────────────────┼──────────────────│
│ LOW        │ Quarterly        │ Team level       │
└──────────────────────────────────────────────────┘

4. ESCALATION AUTHORITY (Decision Rights)
┌──────────────────────────────────────────────────┐
│ Role                │ Authority                  │
│─────────────────────┼────────────────────────────│
│ Quality Engineer    │ Trigger Yellow flag        │
│                     │ Halt deliveries (temp)     │
│─────────────────────┼────────────────────────────│
│ Program Manager     │ Halt production (pending)  │
│                     │ Authorize investigation    │
│─────────────────────┼────────────────────────────│
│ VP Engineering      │ Halt production (confirmed)│
│                     │ Authorize design changes   │
│─────────────────────┼────────────────────────────│
│ CEO / Board         │ Recall decision            │
│                     │ Program termination        │
└──────────────────────────────────────────────────┘

5. CONTINUOUS LEARNING LOOP
┌──────────────────────────────────────────────────┐
│ Every Quality Issue → Risk Register Update       │
│                                                  │
│ Process:                                         │
│ 1. Incident occurs (quality escape, field failure)│
│ 2. Root cause investigation                      │
│ 3. Update risk register:                         │
│    • Adjust probability if trend emerges         │
│    • Add new risks if new failure modes found    │
│ 4. Update monitoring plan (new indicators?)      │
│ 5. Adjust treatment plan (additional mitigations?)│
│ 6. Communicate lessons learned across programs   │
└──────────────────────────────────────────────────┘

FORD'S POST-INCIDENT MONITORING (After Feb 2023):
═══════════════════════════════════════════════════

What Ford SHOULD HAVE had from Day 1, now implemented:

✓ Enhanced Telemetry Monitoring
  • Battery health data from every delivered vehicle
  • Cloud-based analytics platform
  • Anomaly detection algorithms

✓ Weekly Risk Review
  • Review all battery-related field data
  • Trend analysis (defect rates, degradation patterns)
  • Early intervention for abnormal vehicles

✓ Proactive Customer Outreach
  • Vehicles showing early warning signs contacted
  • Diagnostic checks offered
  • Preemptive battery replacement if needed

✓ Rapid Response Protocol
  • 24-hour response to any fire report
  • Investigation team deployed immediately
  • NHTSA notification within hours

✓ Continuous Improvement
  • Enhanced supplier audits (SK On)
  • Modified assembly processes
  • Improved validation testing for future programs

→ This level of monitoring should exist for ALL
   Catastrophic-impact subsystems from launch.

KEY TAKEAWAY:

"Risk monitoring is not passive observation.
It's active surveillance with predefined triggers.

For safety-critical systems:
• Define what 'early warning' looks like
• Set thresholds that trigger action
• Empower people to halt/escalate
• Don't wait for catastrophic failure

Early warning signals are gifts.
Ignoring them is negligence."

STUDENT REFLECTION:

"If you were the quality engineer who discovered the
September 2022 quality issue, and your manager said
'keep investigating but don't halt production yet,'
what would you do?"

A) Follow orders, continue investigating
B) Escalate to VP Engineering directly
C) Document your concern and recommendation in writing
D) Anonymously report to NHTSA

Professional and ethical dimensions.
```

**Class Discussion (3 min):**

> "This is a real ethical dilemma. You see an early warning signal. You recommend halting deliveries. Management says 'not yet, keep investigating.'
>
> What's your professional and ethical obligation?"

**Expected Discussion:**
- Duty to escalate if safety-critical
- Document recommendations in writing (CYA + creates audit trail)
- Chain of command vs. safety obligation
- Whistleblower protections (or lack thereof)

**Instructor Synthesis:**

> "Correct answer: **B + C.** Escalate to higher authority AND document your recommendation in writing.
>
> If VP Engineering also declines to halt, then you've done your professional duty. The decision is theirs, but you've created a record.
>
> **Never** stay silent on safety issues. Your professional engineering license (if applicable) and ethical code require you to advocate for safety.
>
> But also recognize: You're not the decision-maker. You provide analysis and recommendations. Leadership decides. That's the structure."

**Learning Connection:** LO2, LO3 - Risk monitoring, professional ethics, engineering judgment

---

## 2.3 Key Takeaways from F-150 Lightning Case

**For wrap-up discussion (Slide 27-28):**

### Risk Management Lessons:

1. **Risk Identification Is Not Enough**
   - The risk was likely identified
   - But identification without adequate treatment = failure

2. **Catastrophic Impact Demands Extraordinary Mitigation**
   - Can't treat battery fire like a door squeak
   - Low probability doesn't excuse inadequate treatment
   - Safety-critical = ASIL D rigor required

3. **Layered Defense (Defense in Depth)**
   - No single mitigation is perfect
   - Multiple layers: Prevention + Detection + Containment + Response
   - Ford relied too heavily on supplier quality (single layer)

4. **Cost-Benefit Analysis Has Limits for Safety**
   - Expected value calculation says "don't spend $1.8B on screening"
   - But safety obligation says "prevent catastrophic harm"
   - Precautionary principle for safety-critical systems

5. **Early Warning Signals Are Gifts**
   - September 2022 quality issue was a warning
   - Acting on it would have saved $1B and prevented larger recall
   - Don't ignore yellow flags on Catastrophic risks

6. **Monitoring Requires Triggers and Authority**
   - Define escalation thresholds in advance
   - Empower people to halt production based on data
   - Don't wait for catastrophic failure to respond

7. **Supplier Risk Is Your Risk**
   - Can't fully outsource quality to suppliers
   - Trust but verify (and verify means more than sampling)
   - Supplier quality failure = your brand damage

8. **Transparency Builds Trust**
   - Ford halted production immediately when fire occurred (right call)
   - Proactive recall better than reactive
   - Customers forgive honesty, not cover-ups

### Professional/Ethical Lessons:

9. **Document Risk Decisions**
   - Risk acceptance requires explicit executive approval
   - Document what risks you accept and why
   - Creates accountability and learning

10. **Engineering Judgment Matters**
    - Standards and processes guide, but don't substitute for judgment
    - When data says "proceed" but gut says "halt," investigate
    - Professional obligation to advocate for safety

---

## 2.4 Discussion Prompts for Students

**Use throughout or at end:**

1. **"Should Ford have done 100% cell screening despite the $1.8B cost?"**
   - Debate: Safety obligation vs. business viability

2. **"Was the September 2022 quality issue a sufficient signal to halt production?"**
   - Expected: Yes, for Catastrophic-impact risks, err on side of caution

3. **"How would you balance cost, schedule, and safety if you were the program manager?"**
   - Explore trade-offs, decision frameworks, stakeholder management

4. **"What's the fair way to allocate recall costs between Ford and SK On?"**
   - Discuss supplier contracts, liability, shared responsibility

5. **"If you were a customer with a recalled Lightning, would you trust Ford to fix it?"**
   - Explore reputation, customer confidence, brand recovery

---

**END OF CASE STUDY 2**

---

# CASE STUDY 3: EV BATTERY SUPPLY CHAIN CRISIS (2021-2024)
**Use for: OPPORTUNITY MANAGEMENT & RESILIENCE (Slides 20-22)**

## 3.1 Case Overview

### The Supply Chain Context

**The EV Battery Value Chain:**

```
Raw Materials → Processing → Cell Manufacturing → Pack Assembly → Vehicle Integration
    ↓              ↓               ↓                    ↓                ↓
  Lithium      Lithium         Battery Cells      Battery Packs     Complete EVs
  Cobalt       Hydroxide       (Cylindrical,      (Modules +        (Tesla, Ford,
  Nickel       Cathode Active  Pouch, Prismatic)  BMS + Cooling)    GM, etc.)
  Graphite     Materials
  
Geographic concentration:
- Raw materials: Australia, Chile, DRC (cobalt)
- Processing: China (70% of lithium, 80% of cathode materials)
- Cell manufacturing: China, South Korea, Japan
- Pack assembly: Regional (near vehicle assembly)
```

**The Crisis Timeline:**

**2020: The Calm Before the Storm**
- EV sales growing but still <5% of global market
- Battery supply adequate for demand
- Prices stable: ~$130-140/kWh (battery pack level)
- OEMs rely heavily on external suppliers (LG, CATL, Panasonic, SK On)

**2021: Demand Acceleration**
- EV sales surge (climate policy, gas prices, new models)
- Tesla Model Y becomes best-selling EV globally
- Ford F-150 Lightning, GM Hummer EV, Rivian R1T launch
- **First supply warnings:** Lithium prices begin rising

**2022: The Supply Crunch Hits**
- **Lithium carbonate prices:** $15K/ton (2020) → $80K/ton (peak 2022) = **5x increase**
- **Nickel prices:** Spike to $100K/ton (normally $20K) due to Russia-Ukraine war
- **Cobalt supply:** DRC political instability, ethical sourcing concerns
- **Cell production capacity:** Global shortage, 12-18 month lead times
- **Impact on OEMs:**
  - Ford: Delays Lightning production ramp (battery-constrained)
  - GM: Delays multiple EV launches
  - Rivian: Production targets slashed by 50%
  - Tesla: Builds own battery production (4680 cells) to reduce dependence

**2023: Scramble for Supply**
- **Vertical integration trend:**
  - Ford announces $3.5B BlueOval Battery Park with CATL
  - GM builds Ultium battery plants (4 plants, $7B+ investment)
  - Tesla expands 4680 production
- **Geographic diversification:**
  - US/EU investments in domestic battery production (IRA subsidies, EU battery regulations)
  - Lithium mining projects in US, Australia, Canada accelerated
- **Strategic reserves:** OEMs stockpile battery materials
- **Price volatility:** Lithium drops from peak ($80K) to $20K/ton as new supply comes online

**2024-Present: Structural Transformation**
- Industry shift from "just-in-time" to "just-in-case" supply chains
- Massive capital investment: $400B+ in battery supply chain globally
- Geopolitical competition: US vs. China for battery dominance
- Technology shifts: LFP (lithium iron phosphate) adoption increases (no cobalt, lower cost)

### Key Metrics

| Metric | 2020 | 2022 (Peak Crisis) | 2024 | Change |
|--------|------|-------------------|------|--------|
| **Lithium Carbonate Price** | $15K/ton | $80K/ton | $20K/ton | 5x spike, now stabilizing |
| **Battery Pack Cost** | $137/kWh | $150/kWh | $120/kWh | Increased then decreased |
| **Global EV Sales** | 3.2M | 10.5M | 14M+ | 4.4x growth |
| **Battery Cell Shortage** | None | 20-30% shortage | Improving | Supply catching up |
| **Lead Time (Cells)** | 6 months | 18 months | 9-12 months | Still elevated |

### Root Causes of Supply Chain Crisis

**1. Demand Outpaced Supply Forecasts**
- EV adoption accelerated faster than industry predicted
- 2020 forecast: 5M EVs in 2022 → Actual: 10.5M (2x underestimate)
- Battery supply planning based on conservative forecasts

**2. Geographic Concentration Risk**
- **China dominance:** 70% of lithium processing, 60% of cell production
- **Single points of failure:** Few suppliers for critical materials
- **Geopolitical risk:** Trade tensions, export controls, political instability

**3. Long Lead Times for Capacity Expansion**
- New lithium mine: 7-10 years from discovery to production
- New refinery: 3-5 years to build
- New cell factory (gigafactory): 2-4 years to build and ramp
- **Can't scale overnight** when demand spikes

**4. Just-in-Time Philosophy Backfired**
- Automotive industry optimized for lean inventory
- No strategic reserves of critical materials
- Assumed supply would always be available at reasonable cost
- 2022 shocks (Ukraine war, COVID lockdowns) exposed fragility

**5. Technology Transition Bottleneck**
- ICE (internal combustion) → EV is entire supply chain transformation
- Legacy auto suppliers (ICE components) not equipped for batteries
- New supply chain had to be built from scratch
- Scaling challenge: 100M ICE vehicles/year → need battery supply for similar EV volume

---

## 3.2 Integration with RISK MANAGEMENT (Opportunity & Resilience)

### Slide 20: Opportunity Management - The Positive Side

**Instructor Narration:**

> "We've talked about threats—risks that cause harm. But risk management also includes **opportunity management**—identifying and capturing positive risks that create value.
>
> Let me show you how some companies turned the EV battery supply crisis into a competitive advantage through opportunity management.
>
> **The Opportunity:** In 2020-2021, EV demand was accelerating. Most OEMs saw battery supply as a **supplier problem**—'We'll buy batteries from LG, CATL, or Panasonic like we buy seats and steering wheels.'
>
> But a few companies saw an **opportunity**: What if we control our own battery supply?
>
> **Tesla's Opportunity Capture:**
>
> **2020: Opportunity Identified**
> - Insight: Battery cost is 40% of EV cost. Battery supply will be the constraint.
> - Opportunity: If we make our own batteries, we control cost, supply, and innovation.
> - Risk: Massive capital investment ($5B+), technical challenges, may fail.
>
> **2021-2022: Opportunity Execution**
> - Develops 4680 battery cell (larger format, structural pack)
> - Builds battery production lines in Texas, Nevada, Berlin
> - Locks in lithium supply with long-term contracts (before price spike)
> - Vertical integration: From lithium mining deals to cell production to pack assembly
>
> **2023-2024: Competitive Advantage Realized**
> - While competitors (Ford, GM, Rivian) are **battery-constrained** and paying high prices ($150/kWh):
> - Tesla has internal supply, lower cost ($110-120/kWh estimated), can ramp faster
> - Production advantage: Tesla produces 1.8M EVs in 2023 vs. Ford 72K Lightnings
> - **Opportunity turned into market dominance**
>
> **Ford/GM's Missed Opportunity (Now Catching Up):**
>
> **2020-2021: Opportunity Missed**
> - Relied on external suppliers (LG, SK On) for batteries
> - Focus: Design great vehicles (F-150 Lightning, Hummer EV)
> - Assumption: Batteries will be available when we need them
>
> **2022: Crisis Hits**
> - Battery supply constrained, prices spike, production limited
> - Lightning production: 150/day target → 50-75/day actual (battery-limited)
> - Rivian cuts production targets in half
> - Competitive disadvantage vs. Tesla
>
> **2023-2024: Reactive Response**
> - Ford announces $3.5B+ battery investments (joint ventures with CATL)
> - GM builds Ultium battery plants ($7B+)
> - **But 2-4 years behind Tesla** because battery factories take years to build
>
> **The Opportunity Management Lesson:**
>
> Opportunities have a **window**. Act early = competitive advantage. Act late = catch-up mode.
>
> Tesla saw battery supply as a **strategic opportunity** in 2020.
> Ford/GM saw it as a **supplier problem** until 2022 crisis forced their hand.
>
> **Opportunity Management Framework:**
>
> Just like threat risks, opportunities should be:
> 1. **Identified:** What positive outcomes could we pursue?
> 2. **Analyzed:** What's the potential value? What's the investment/risk?
> 3. **Exploited:** How do we maximize the probability and impact?
> 4. **Monitored:** Are we capturing the value? Do we need to adjust?
>
> **Tesla's Opportunity Management:**
> 1. Identify: Battery supply = future bottleneck and cost driver
> 2. Analyze: Value = Cost reduction ($30/kWh) + Supply security + Innovation control
>    Investment = $5-10B over 5 years. Risk = Technical failure, demand doesn't materialize.
> 3. Exploit: Invest heavily in battery technology and production capacity
> 4. Monitor: Track cost reduction, production ramp, compare to competitors
>
> **Result:** Multi-billion dollar competitive advantage.
>
> **Your takeaway:** Opportunities are risks too. But instead of preventing harm, you're pursuing gain. Same rigor, opposite direction."

**PPT Content:**
```
EV BATTERY SUPPLY CHAIN - OPPORTUNITY MANAGEMENT

THE STRATEGIC OPPORTUNITY (2020-2021):
═══════════════════════════════════════════════════

INDUSTRY CONTEXT:
• EV demand accelerating (climate policy, new models)
• Battery cost = 40% of EV vehicle cost
• Battery supply = future constraint (long lead times)
• Most OEMs outsource batteries to LG, CATL, Panasonic

STRATEGIC QUESTION:
"Do we buy batteries (like seats/tires)
 OR do we make/control batteries (vertical integration)?"

Two Paths:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PATH A: External Suppliers (Traditional Auto)
  • Buy batteries from Tier 1 suppliers
  • Focus on vehicle design and assembly
  • Lower capital investment
  • Faster time to market
  • BUT: Dependent on supplier capacity/pricing

PATH B: Vertical Integration (Control Supply)
  • Build own battery production capacity
  • Secure raw material supply (mining contracts)
  • Control cost, quality, innovation
  • BUT: Massive capital ($5-10B+), technical risk
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHO CHOSE WHICH PATH?

TESLA: Path B (Vertical Integration) ✓ Opportunity Captured
FORD/GM: Path A (Suppliers) → Forced to Path B later ⚠️

TESLA'S OPPORTUNITY MANAGEMENT (2020-2023):
═══════════════════════════════════════════════════

PHASE 1: Opportunity Identification (2019-2020)
┌──────────────────────────────────────────────────┐
│ INSIGHT:                                         │
│ "Battery supply will be THE constraint in EV era│
│  Whoever controls batteries wins."               │
│                                                  │
│ DATA POINTS:                                     │
│ • Battery = 40% of EV cost ($12K of $30K)        │
│ • Demand growing faster than supply              │
│ • Supplier capacity limited, allocation fights  │
│ • Price risk if materials spike                 │
│                                                  │
│ OPPORTUNITY HYPOTHESIS:                          │
│ "If we make our own batteries:                   │
│  + Control cost (reduce $30/kWh)                 │
│  + Ensure supply (no allocation constraints)     │
│  + Enable innovation (new cell designs)          │
│  + Competitive moat vs Ford/GM"                  │
└──────────────────────────────────────────────────┘

PHASE 2: Opportunity Analysis (2020)
┌──────────────────────────────────────────────────┐
│ POTENTIAL VALUE:                                 │
│ • Cost reduction: $30/kWh × 200 kWh/vehicle      │
│   = $6,000 cost advantage per vehicle            │
│ • Volume: 2M vehicles/year by 2025               │
│   = $12 billion/year competitive advantage       │
│ • Supply security: Can ramp production faster    │
│   = Market share gains                           │
│                                                  │
│ INVESTMENT REQUIRED:                             │
│ • Battery R&D: $2B (4680 cell development)       │
│ • Gigafactory capacity: $5-10B (multiple sites)  │
│ • Lithium supply contracts: $2-3B (pre-pay)      │
│ • Timeline: 3-5 years to full ramp               │
│ • TOTAL: $10-15B over 5 years                    │
│                                                  │
│ RISKS:                                           │
│ • Technical: 4680 cell may not work              │
│ • Market: Demand may not materialize             │
│ • Execution: Can't ramp production fast enough   │
│ • Capital: Huge investment, uncertainty          │
│                                                  │
│ DECISION CRITERIA:                               │
│ NPV (Net Present Value):                         │
│ • Investment: -$15B (2020-2024)                  │
│ • Returns: +$12B/year (2025+) for 10 years       │
│ • NPV @ 10% discount: +$58B                      │
│ → PROCEED ✓                                      │
└──────────────────────────────────────────────────┘

PHASE 3: Opportunity Exploitation (2021-2023)
┌──────────────────────────────────────────────────┐
│ ACTIONS TAKEN:                                   │
│                                                  │
│ ✓ Battery Day (Sept 2020): Announce 4680 cell   │
│   • Larger format (46mm × 80mm)                  │
│   • Structural battery pack (body part)          │
│   • Target: 50% cost reduction                   │
│                                                  │
│ ✓ Gigafactory Capacity Expansion:                │
│   • Texas (Austin): 4680 production + Cybertruck │
│   • Nevada: Expand 2170 + 4680 lines             │
│   • Berlin: Battery production + Model Y         │
│   • Target: 1,000 GWh/year by 2030               │
│                                                  │
│ ✓ Lithium Supply Contracts (2021-2022):          │
│   • Long-term offtake agreements                 │
│   • Locked in prices BEFORE 2022 spike           │
│   • Avoided $50K/ton spike (paid ~$20K/ton)      │
│   • Savings: Billions in avoided cost increases  │
│                                                  │
│ ✓ Vertical Integration Investments:              │
│   • Lithium refining (Texas facility)            │
│   • Cathode production (in-house)                │
│   • Cell manufacturing (4680 lines)              │
│   • Pack assembly (integrated with vehicle)      │
│                                                  │
│ OUTCOME (2023-2024):                             │
│ • 4680 production ramping (limited but growing)  │
│ • Battery cost: ~$110-120/kWh (vs $150 industry) │
│ • Supply security: Not constrained like rivals   │
│ • Production: 1.8M vehicles (2023) vs Ford 72K   │
└──────────────────────────────────────────────────┘

PHASE 4: Monitoring and Adjustment (Ongoing)
┌──────────────────────────────────────────────────┐
│ METRICS TRACKED:                                 │
│ • Battery cost per kWh (target: <$100/kWh)       │
│ • 4680 production ramp rate (cells/day)          │
│ • Supply security (% internally produced)        │
│ • Competitive gap (Tesla cost vs Ford/GM)        │
│                                                  │
│ ADJUSTMENTS MADE:                                │
│ • 4680 ramp slower than planned (technical)      │
│   → Continue buying 2170 cells from Panasonic    │
│ • Demand exceeded supply (good problem)          │
│   → Accelerate additional Gigafactory plans      │
│ • LFP adoption for standard range models         │
│   → Hedge against nickel/cobalt supply           │
└──────────────────────────────────────────────────┘

FORD/GM: Missed Opportunity → Reactive Catch-Up
═══════════════════════════════════════════════════

PHASE 1: Opportunity Missed (2020-2021)
┌──────────────────────────────────────────────────┐
│ STRATEGY: Rely on External Suppliers             │
│ • Ford: Partner with SK On for Lightning         │
│ • GM: Partner with LG for Ultium platform        │
│                                                  │
│ RATIONALE:                                       │
│ "Battery suppliers are experts. We're vehicle    │
│  experts. Stay in our lane. Less capital risk."  │
│                                                  │
│ ASSUMPTION:                                      │
│ "Supply will be available when we need it."      │
│                                                  │
│ → OPPORTUNITY NOT PURSUED                        │
└──────────────────────────────────────────────────┘

PHASE 2: Crisis Hits (2022)
┌──────────────────────────────────────────────────┐
│ CONSEQUENCES OF NOT CAPTURING OPPORTUNITY:       │
│                                                  │
│ FORD F-150 LIGHTNING:                            │
│ • Target: 150,000/year by 2023                   │
│ • Actual: ~15,000 (2022), ~24,000 (2023)         │
│ • Constraint: Battery supply allocation from SK  │
│ • Cost: $150/kWh (vs Tesla $110-120/kWh)         │
│ • Margin pressure: Lower margin than ICE F-150   │
│                                                  │
│ RIVIAN R1T:                                      │
│ • Target: 50,000 (2022)                          │
│ • Actual: 24,000 (2022) - Battery constrained    │
│                                                  │
│ GM HUMMER EV / LYRIQ:                            │
│ • Delays in ramp due to battery availability     │
│                                                  │
│ COMPETITIVE GAP:                                 │
│ Tesla produced 1.8M EVs (2023)                   │
│ Ford produced 72K electric vehicles (2023)       │
│ → 25x gap, largely due to battery supply         │
└──────────────────────────────────────────────────┘

PHASE 3: Reactive Response (2023-2024)
┌──────────────────────────────────────────────────┐
│ FORD:                                            │
│ • $3.5B BlueOval Battery Park (Tennessee)        │
│   Joint venture with SK On                       │
│   Target: 43 GWh/year (enough for ~500K vehicles)│
│   Online: 2025-2026 (3-4 years behind Tesla)     │
│ • $3.5B BlueOval Battery Park II (Michigan)      │
│   Joint venture with CATL (LFP chemistry)        │
│   Online: 2026                                   │
│                                                  │
│ GM:                                              │
│ • $7B+ Ultium battery plants (4 facilities)      │
│   Joint ventures with LG Energy Solution         │
│   Target: 160 GWh/year                           │
│   Online: 2024-2026                              │
│                                                  │
│ STATUS: Catching up, but 3-5 years behind Tesla  │
│ • Still dependent on partners (SK, LG, CATL)     │
│ • Massive capital now committed ($10-15B)        │
│ • Opportunity cost: Lost 2020-2023 production    │
└──────────────────────────────────────────────────┘

OPPORTUNITY MANAGEMENT FRAMEWORK:
═══════════════════════════════════════════════════

Just like THREAT risks, OPPORTUNITIES should be:

1. IDENTIFIED
   • What positive outcomes could we create?
   • Market shifts, technology trends, competitive gaps
   • Use techniques: Strategic foresight, scenario planning

2. ANALYZED
   • Potential value (revenue, cost reduction, advantage)
   • Probability of success
   • Investment required and risks
   • Timing: Window of opportunity (first-mover advantage)

3. TREATED (Exploit, Enhance, Share, Accept)
   • EXPLOIT: Maximize probability and impact (invest heavily)
   • ENHANCE: Improve attractiveness (pilot before scale)
   • SHARE: Partner to reduce risk (joint ventures)
   • ACCEPT: Monitor but don't act (opportunity cost acceptable)

4. MONITORED
   • Track value capture
   • Adjust strategy as conditions change
   • Compare to alternative paths not taken

TESLA'S APPROACH:
Identified → Analyzed (NPV positive) → Exploited (heavy investment) → Monitoring

FORD/GM'S APPROACH (2020):
Identified (maybe?) → Analyzed (too risky?) → Accepted (rely on suppliers)
→ Forced to exploit later after crisis (reactive)

KEY LESSON:

"Opportunities have windows.

First movers capture value.
Late movers play catch-up.

The question isn't just 'Should we act?'
It's 'Can we afford NOT to act?'"

STUDENT DISCUSSION:

"Was Tesla's $10-15B battery investment reckless or visionary?

Hindsight = visionary (huge advantage now)
But in 2020, with uncertainty about EV demand,
was it justified?

How do you make decisions under uncertainty?"

Answer: Risk-adjusted decision-making
• Scenario planning (if demand is X, what's ROI?)
• Option value (early investment creates future optionality)
• Competitive dynamics (if we don't, Tesla will)
```

**Class Discussion (5 min):**

> "Put yourself in Ford's position in 2020. Tesla announces massive battery investments. You have two options:
>
> **Option A:** Follow Tesla - Invest $10B in your own battery production. High risk, high reward.
>
> **Option B:** Rely on suppliers (SK On, LG). Lower risk, lower capital, but dependent on allocation.
>
> At the time (2020), EV demand is uncertain. COVID pandemic. Economic uncertainty.
>
> **What do you choose? Why?**"

**Expected Discussion:**
- **Risk tolerance:** Startups (Tesla) can take bigger risks. Established companies (Ford) more conservative.
- **Core competency:** Ford's strength is vehicle design/manufacturing, not battery chemistry.
- **Capital constraints:** $10B is massive investment with uncertain return.
- **Competitive pressure:** If Tesla succeeds and you don't, you lose market.

**Instructor Synthesis:**

> "There's no clearly right answer in 2020. It's a judgment call under uncertainty.
>
> But here's what we know now:
> - **Tesla's bet paid off.** Massive competitive advantage.
> - **Ford's conservative approach cost them.** 3-4 years behind, playing catch-up.
>
> The lesson isn't 'always take big risks.' It's: **Strategic opportunities require analysis and decisive action. Indecision or delay is itself a decision—to cede advantage to competitors.**
>
> Ford is now spending the same $10-15B Tesla spent, but 3-4 years later. They're paying the price of delayed decision-making."

**Learning Connection:** LO2, LO3 - Opportunity management, strategic risk-taking, competitive advantage

---

### Slide 21: Risk Reserves - Planning for Uncertainty

**Instructor Narration:**

> "Let's talk about **risk reserves**—resources set aside to deal with uncertainty. In the battery supply chain crisis, some companies had reserves, others didn't.
>
> **Two Types of Reserves:**
>
> **1. Schedule Reserves (Buffer Time)**
> Example: Plan 36-month development timeline, but announce 42-month timeline publicly.
> → 6-month buffer for unknowns.
>
> **2. Resource Reserves (Budget, Materials, Capacity)**
> Example: Secure 120% of needed battery supply, even though you only need 100%.
> → 20% buffer for supply disruptions.
>
> **Battery Supply Chain Reserves:**
>
> **Tesla's Reserves (2021-2022):**
> - **Material reserves:** Locked in lithium supply contracts for 150% of planned production
> - **Strategic stockpiling:** Purchased lithium at $20K/ton before spike to $80K/ton
> - **Capacity reserves:** Built battery production capacity for 2M vehicles while planning 1.5M
> - **Result:** When crisis hit, Tesla had cushion. Kept ramping while competitors couldn't.
>
> **Ford/Rivian (No Reserves):**
> - **Just-in-time mindset:** Order batteries as needed, no stockpiling
> - **Allocation risk:** Relied on supplier allocation (SK On, LG split capacity among customers)
> - **Result:** When demand spiked, supply constrained. Production limited.
>
> **The Reserve Trade-Off:**
>
> Reserves cost money:
> - Stockpiling lithium ties up capital
> - Excess capacity costs $1-2B in idle investment
> - Overhead without immediate return
>
> But reserves provide insurance:
> - Tesla's lithium reserves saved billions when prices spiked
> - Capacity reserves enabled faster ramp
>
> **Risk Reserve Decision Framework:**
>
> **When to build reserves:**
> - High uncertainty (demand forecast, supply availability)
> - High impact if shortage occurs (production stops, revenue lost)
> - Affordable cost of reserves (stockpiling materials, buffer capacity)
>
> **When NOT to build reserves:**
> - Low uncertainty (stable supply, predictable demand)
> - Low impact if shortage occurs (can wait, substitute available)
> - Expensive reserves (tying up too much capital)
>
> **Example: Lithium Reserve Calculation (2021)**
>
> **Scenario:** Ford planning F-150 Lightning production
> - Planned volume: 100,000 vehicles/year (2023)
> - Lithium needed: 6 kg per vehicle × 100,000 = 600 tons/year
> - Current price (2021): $15,000/ton
> - Forecast risk: Lithium could spike to $50K-80K/ton if shortage
>
> **Option A: No Reserve (Just-in-Time)**
> - Buy lithium as needed on spot market
> - Cost if price stable ($15K/ton): 600 tons × $15K = $9M/year
> - Cost if price spikes ($60K/ton): 600 tons × $60K = $36M/year
> - Expected cost (50% chance of spike): 0.5×$9M + 0.5×$36M = $22.5M
>
> **Option B: Build Reserve (Lock in 3-Year Supply)**
> - Buy 1,800 tons in 2021 at $15K/ton = $27M upfront
> - Cost of capital (opportunity cost): 10% × $27M = $2.7M/year
> - Total 3-year cost: $27M + 3×$2.7M = $35.1M
> - Average annual cost: $11.7M/year
>
> **Comparison:**
> - Option A (No reserve): $22.5M expected cost/year
> - Option B (Reserve): $11.7M/year
> - **Savings: $10.8M/year** if spike occurs
>
> **Tesla did Option B.** Ford did Option A.
>
> When lithium spiked to $80K/ton in 2022, Tesla's reserves paid off massively.
>
> **Key Lesson:**
> **Reserves are insurance against volatility. In uncertain, high-stakes environments, reserves are not waste—they're risk management.**"

**PPT Content:**
```
RISK RESERVES - BATTERY SUPPLY CHAIN

RISK RESERVES = Insurance Against Uncertainty
═══════════════════════════════════════════════════

TWO TYPES OF RESERVES:

1. SCHEDULE RESERVES (Buffer Time)
   • Build extra time into schedule for unknowns
   • Example: 36-month plan, 42-month commitment
   • → 6-month contingency for delays

2. RESOURCE RESERVES (Budget, Materials, Capacity)
   • Extra budget for cost overruns
   • Strategic stockpiles of critical materials
   • Excess capacity for demand surges
   • → Buffer for supply/demand volatility

BATTERY SUPPLY CHAIN RESERVE STRATEGIES:
═══════════════════════════════════════════════════

TESLA'S RESERVE STRATEGY (2021-2022):
┌──────────────────────────────────────────────────┐
│ STRATEGIC LITHIUM RESERVES:                      │
│ • Locked in long-term supply contracts (2021)    │
│ • Purchased lithium at $20K/ton (pre-spike)      │
│ • Secured 150% of planned production needs       │
│   (Reserve = 50% buffer)                         │
│                                                  │
│ WHEN SPIKE HIT (2022):                           │
│ • Market price: $80K/ton                         │
│ • Tesla's contract price: ~$20-30K/ton           │
│ • Savings: $50K/ton × thousands of tons          │
│   = $500M-$1B+ in avoided cost increases         │
│                                                  │
│ BATTERY CAPACITY RESERVES:                       │
│ • Built production for 2M vehicles/year          │
│ • Planned volume: 1.5M vehicles/year (2023)      │
│ • Reserve capacity: 25%                          │
│ • Enabled: Faster ramp when demand exceeded plan │
│                                                  │
│ COST OF RESERVES:                                │
│ • Lithium stockpile: $500M-$1B tied up           │
│ • Excess capacity: $2-3B in "idle" investment    │
│ • Opportunity cost: Capital not earning returns  │
│                                                  │
│ VALUE OF RESERVES (2022 Crisis):                 │
│ • Avoided cost spike: $500M-$1B                  │
│ • Enabled production ramp: Produced 1.8M vs 1.5M │
│   = 300K additional vehicles × $50K = $15B revenue│
│ • Competitive advantage: Rivals were constrained │
│                                                  │
│ → RESERVES PAID OFF MASSIVELY                    │
└──────────────────────────────────────────────────┘

FORD/GM/RIVIAN: NO RESERVES (Just-in-Time)
┌──────────────────────────────────────────────────┐
│ STRATEGY: Buy Materials as Needed                │
│ • Rely on supplier to manage inventory           │
│ • Just-in-time delivery (lean manufacturing)     │
│ • No long-term contracts (avoid tying up capital)│
│                                                  │
│ WHEN SPIKE HIT (2022):                           │
│ • Forced to buy lithium at $60-80K/ton           │
│ • Battery cost: $150/kWh (vs Tesla $110-120/kWh) │
│ • Supply allocation: Suppliers split capacity    │
│   among customers → Ford gets 60% of requested   │
│                                                  │
│ CONSEQUENCES:                                    │
│ • Ford F-150 Lightning production limited        │
│   Target: 150K/year → Actual: 24K/year (2023)    │
│ • Rivian production cut 50% (battery constraint) │
│ • Cost disadvantage: $40-50/kWh vs Tesla         │
│   = $8,000-10,000 per vehicle cost gap           │
│                                                  │
│ → NO RESERVES = VULNERABILITY                    │
└──────────────────────────────────────────────────┘

RESERVE DECISION FRAMEWORK:
═══════════════════════════════════════════════════

WHEN TO BUILD RESERVES:

✓ HIGH UNCERTAINTY
  • Demand forecast volatile (new market, EV adoption rate)
  • Supply availability uncertain (geopolitical, new suppliers)
  • Price volatility expected (commodity markets)

✓ HIGH IMPACT IF SHORTAGE
  • Production stops (revenue loss)
  • Costs spike dramatically (budget blown)
  • Competitive disadvantage (rivals gain share)

✓ AFFORDABLE COST OF RESERVES
  • Stockpiling is economical (materials can be stored)
  • Excess capacity has alternative uses
  • Capital available for strategic investment

WHEN NOT TO BUILD RESERVES:

✗ LOW UNCERTAINTY
  • Stable supply (mature market, reliable suppliers)
  • Predictable demand (steady growth)
  • Stable prices (commodity indexes flat)

✗ LOW IMPACT IF SHORTAGE
  • Can wait (delay acceptable)
  • Substitutes available (alternative materials)
  • Small financial exposure

✗ EXPENSIVE RESERVES
  • Stockpiling impractical (perishable, expensive storage)
  • Excess capacity has no alternative use (stranded assets)
  • Capital constraints (can't afford reserves)

BATTERY SUPPLY CHAIN (2021): ✓✓✓ BUILD RESERVES
• High uncertainty (EV demand spike, new market)
• High impact (production constraint, cost spike)
• Affordable (lithium can be stockpiled, capacity has use)

RESERVE CALCULATION EXAMPLE:
═══════════════════════════════════════════════════

SCENARIO: Ford F-150 Lightning (2021 Planning)

ASSUMPTIONS:
• Planned production: 100,000 vehicles/year (2023)
• Lithium per vehicle: 6 kg
• Annual lithium need: 600 tons/year
• Current price (2021): $15,000/ton
• Risk: Price could spike to $60-80K/ton (supply shortage)
• Probability of spike: 50% (high uncertainty)

OPTION A: NO RESERVE (Just-in-Time Purchasing)
┌──────────────────────────────────────────────────┐
│ Strategy: Buy lithium on spot market as needed   │
│                                                  │
│ COST IF PRICE STABLE ($15K/ton):                 │
│ • 600 tons/year × $15K/ton = $9M/year            │
│                                                  │
│ COST IF PRICE SPIKES ($60K/ton):                 │
│ • 600 tons/year × $60K/ton = $36M/year           │
│                                                  │
│ EXPECTED COST (Probability-Weighted):            │
│ • 50% × $9M + 50% × $36M = $22.5M/year           │
│                                                  │
│ 3-YEAR TOTAL: $22.5M/year × 3 = $67.5M           │
└──────────────────────────────────────────────────┘

OPTION B: BUILD RESERVE (Lock in 3-Year Supply)
┌──────────────────────────────────────────────────┐
│ Strategy: Purchase 3-year supply in 2021         │
│                                                  │
│ UPFRONT COST:                                    │
│ • 600 tons/year × 3 years = 1,800 tons           │
│ • 1,800 tons × $15K/ton = $27M (paid in 2021)    │
│                                                  │
│ CARRYING COST (Opportunity Cost of Capital):     │
│ • 10% cost of capital × $27M = $2.7M/year        │
│ • Storage/handling: $0.5M/year                   │
│ • Total carrying cost: $3.2M/year × 3 = $9.6M    │
│                                                  │
│ 3-YEAR TOTAL: $27M + $9.6M = $36.6M              │
│                                                  │
│ ANNUAL EQUIVALENT: $36.6M / 3 = $12.2M/year      │
└──────────────────────────────────────────────────┘

COMPARISON:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Option A (No Reserve): $67.5M (3-year expected cost)
Option B (Reserve):    $36.6M (3-year total cost)

SAVINGS WITH RESERVE: $30.9M over 3 years
                      = $10.3M/year saved

→ BUILDING RESERVE IS ECONOMICALLY RATIONAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ACTUAL OUTCOME (2022):
• Lithium spiked to $80K/ton (even higher than estimate)
• Tesla (reserved): Paid ~$20-30K/ton (contracts)
• Ford (no reserve): Paid $60-80K/ton (spot market)
• Tesla savings: $40-60K/ton × thousands of tons
  = $500M-$1B+ competitive advantage

KEY LESSON:

"Reserves cost money upfront.
But volatility costs MORE if you're unprepared.

In high-uncertainty, high-stakes environments:
Reserves are not waste. They're insurance."

ADDITIONAL RESERVE STRATEGIES (Industry Response):
═══════════════════════════════════════════════════

GEOGRAPHIC DIVERSIFICATION (Resilience)
┌──────────────────────────────────────────────────┐
│ PROBLEM: 70% of lithium refining in China        │
│          → Single point of failure risk          │
│                                                  │
│ SOLUTION: Diversify supply sources               │
│ • US lithium projects (Nevada, California)       │
│ • Australian mining expansion                    │
│ • Canadian refining capacity                     │
│ • Goal: Reduce China dependence to 40-50%        │
│                                                  │
│ INVESTMENT: $50B+ in Western lithium supply      │
│ TIMELINE: 2024-2030 (7-10 years for new mines)   │
└──────────────────────────────────────────────────┘

TECHNOLOGY DIVERSIFICATION (Hedging)
┌──────────────────────────────────────────────────┐
│ PROBLEM: NCM batteries need lithium, nickel, cobalt│
│          → All three subject to supply shocks    │
│                                                  │
│ SOLUTION: LFP batteries (Lithium Iron Phosphate) │
│ • No nickel, no cobalt (lower supply risk)       │
│ • Lower cost ($80-100/kWh vs $120-140/kWh NCM)   │
│ • Trade-off: Lower energy density (less range)   │
│                                                  │
│ STRATEGY: Use LFP for standard range models      │
│           Use NCM for long range models          │
│ → Hedge against single chemistry supply risk     │
│                                                  │
│ ADOPTION: Tesla (50% LFP), Ford (increasing)     │
└──────────────────────────────────────────────────┘

VERTICAL INTEGRATION (Control)
┌──────────────────────────────────────────────────┐
│ STRATEGY: Own the supply chain end-to-end        │
│                                                  │
│ TESLA:                                           │
│ ├─ Lithium mining contracts (direct deals)       │
│ ├─ Lithium refining (Texas facility)             │
│ ├─ Cathode production (in-house)                 │
│ ├─ Cell manufacturing (4680)                     │
│ └─ Pack assembly (integrated)                    │
│                                                  │
│ BENEFIT: Control all stages, reduce dependency   │
│ COST: $10-15B capital investment                 │
│ RISK: Execution complexity, scale-up challenges  │
└──────────────────────────────────────────────────┘

STUDENT EXERCISE:

"You're planning production for a new EV in 2025.

Battery cost today: $120/kWh (stable)
Risk: Battery prices could spike 50% if supply shortage
Probability: 30%

OPTION A: Buy batteries spot market as needed
OPTION B: Lock in 5-year supply contract today

What additional information do you need to decide?
How would you calculate the value of the reserve?"

Expected answers:
• Need: Volume forecast, contract price, carrying cost, volatility risk
• Calculate: Expected value with/without reserve
• Consider: Strategic value (production certainty) vs financial cost
```

**Learning Connection:** LO2, LO3 - Risk reserves, supply chain risk management, decision analysis under uncertainty

---

[Content continues with Slide 22 on Resilience Thinking. Should I continue?]


### Slide 22: Resilience Thinking - Beyond Risk Management

**Instructor Narration:**

> "We've covered traditional risk management: identify, analyze, treat, monitor. But there's a more advanced concept: **resilience thinking.**
>
> **Risk Management = Preventing known failures**
> **Resilience = Surviving unknown failures**
>
> The EV battery supply chain crisis shows the difference.
>
> **Traditional Risk Management (2020):**
> - Identified risk: Supplier delivery delays
> - Mitigation: Dual-source suppliers, safety stock
> - Monitoring: Track supplier on-time delivery
>
> **What Actually Happened (2022):**
> - Geopolitical shock (Russia-Ukraine war → nickel spike)
> - Macroeconomic shock (inflation, lithium demand surge)
> - COVID lockdowns (China disruptions)
> - **None of these were in the risk register**
>
> **Traditional risk management failed because the failure modes were unknown/unforeseeable.**
>
> **Resilience thinking asks different questions:**
> - Not 'What risks do we know?' but '**How do we survive disruptions we can't predict?**'
> - Not 'How do we prevent failure?' but '**How quickly can we recover from failure?**'
> - Not 'Optimize for efficiency' but '**Build robustness and adaptability**'
>
> **Resilience Principles Applied to Battery Supply Chain:**
>
> **1. Diversity (Don't Put All Eggs in One Basket)**
>
> **Fragile System (Pre-2022):**
> - Single chemistry: NCM (nickel-cobalt-manganese) for all vehicles
> - Single geographic source: 70% China for lithium processing
> - Single supplier model: Buy from one Tier 1 (LG or CATL)
>
> **Resilient System (Post-2022):**
> - **Chemistry diversity:** NCM for long-range, LFP for standard-range (Tesla, Ford adopting)
> - **Geographic diversity:** US/Australia lithium, European refining, Asian manufacturing
> - **Supplier diversity:** Multiple suppliers, own production, strategic reserves
>
> **Result:** If one chemistry/region/supplier fails, others continue.
>
> **2. Redundancy (Build Spare Capacity)**
>
> **Fragile (Lean):**
> - Just-in-time delivery, zero inventory
> - 100% capacity utilization
> - Optimized for cost, no slack
>
> **Resilient (Robust):**
> - Strategic stockpiles (3-6 months lithium reserve)
> - 80% capacity utilization (20% buffer for surges)
> - Multiple production lines (if one fails, others operate)
>
> **Trade-off:** Redundancy costs money (idle capacity, inventory carrying cost)
> **Value:** Insurance against disruption
>
> **3. Modularity (Plug-and-Play Components)**
>
> **Fragile (Integrated):**
> - Structural battery pack (Tesla, Ford Lightning)
> - Battery is part of vehicle body structure
> - Can't easily swap battery suppliers (custom pack design)
>
> **Resilient (Modular):**
> - Standardized battery modules
> - Multiple suppliers can provide compatible modules
> - Can switch suppliers without vehicle redesign
>
> **Trade-off:** Modularity may sacrifice some performance/integration
> **Value:** Flexibility to change suppliers rapidly
>
> **4. Adaptability (Learn and Evolve)**
>
> **Fragile (Fixed):**
> - Long-term plans locked in, can't change
> - Committed to single technology path
> - Slow to respond to market shifts
>
> **Resilient (Adaptive):**
> - Rolling forecasts, adjust plans quarterly
> - Dual technology paths (NCM + LFP)
> - Rapid prototyping and pivots
>
> **Example:** Tesla shifted from 2170 cells (Panasonic) → 4680 cells (own production) → LFP cells (CATL) based on changing conditions. Adapted quickly.
>
> **5. Fast Feedback Loops (Detect and Respond Quickly)**
>
> **Fragile (Slow Detection):**
> - Annual supplier reviews
> - Quarterly risk assessments
> - React after crisis hits
>
> **Resilient (Real-Time Monitoring):**
> - Daily supplier scorecards
> - Real-time market monitoring (lithium prices, geopolitical events)
> - Early warning indicators trigger action
>
> **Example:** Companies monitoring lithium prices daily in 2021 saw spike coming, locked in contracts early.
>
> **The Resilience Mindset Shift:**
>
> **From:** 'We've identified all risks and mitigated them' (false confidence)
> **To:** 'We can't predict everything, but we can survive anything' (true resilience)
>
> **From:** Optimize for efficiency (lean, just-in-time, single-source)
> **To:** Optimize for robustness (redundancy, diversity, flexibility)
>
> **From:** Plan for known scenarios
> **To:** Build adaptive capacity for unknown scenarios
>
> **Resilience Example: Toyota vs. Ford (2011 Japan Earthquake)**
>
> **2011 Japan earthquake/tsunami:**
> - Disrupted Japanese suppliers (semiconductors, components)
> - Affected ALL automakers
>
> **Toyota Response (Resilient):**
> - Keiretsu network: Deep supplier relationships
> - Rapid damage assessment (sent engineers to suppliers immediately)
> - Resource reallocation (shifted production to unaffected regions)
> - Supplier support (helped suppliers rebuild)
> - Recovered in 6 months
>
> **Ford/GM Response (Less Resilient):**
> - Arm's-length supplier relationships
> - Slower damage assessment
> - Supply chain visibility gaps (didn't know tier 2/3 suppliers)
> - Longer recovery (9-12 months)
>
> **Lesson:** Resilience is organizational capability, not just risk register.
>
> **Applying Resilience to Your Projects:**
>
> **Ask these questions:**
> 1. **What are our single points of failure?** (Identify fragility)
> 2. **Can we survive if our top assumption is wrong?** (Stress test)
> 3. **How quickly can we detect problems?** (Feedback loops)
> 4. **How quickly can we pivot?** (Adaptability)
> 5. **Do we have options?** (Flexibility, Plan B/C/D)
>
> **Resilience vs. Risk Management Summary:**
>
> | Dimension | Risk Management | Resilience Thinking |
> |-----------|----------------|---------------------|
> | **Focus** | Prevent known failures | Survive unknown shocks |
> | **Approach** | Identify and mitigate risks | Build adaptive capacity |
> | **Mindset** | Control the future | Prepare for uncertainty |
> | **Strategy** | Efficiency + mitigation | Robustness + flexibility |
> | **Tools** | Risk register, FMEA | Redundancy, diversity, modularity |
> | **Goal** | Zero failures | Fast recovery |
>
> **Both are needed.** Risk management for known threats. Resilience for unknown threats.
>
> The battery supply crisis taught the auto industry: **You can't risk-manage your way out of every problem. You need resilience.**"

**PPT Content:**
```
RESILIENCE THINKING - BEYOND RISK MANAGEMENT

RISK MANAGEMENT vs. RESILIENCE THINKING:
═══════════════════════════════════════════════════

TRADITIONAL RISK MANAGEMENT:
• Focus: Identify and prevent KNOWN risks
• Tools: Risk register, FMEA, mitigation plans
• Goal: Avoid failures we can anticipate

RESILIENCE THINKING:
• Focus: Survive and recover from UNKNOWN shocks
• Tools: Diversity, redundancy, adaptability
• Goal: Fast recovery from unanticipated disruptions

BATTERY SUPPLY CHAIN CRISIS (2022):
Traditional risk management FAILED because:
✗ Geopolitical shock (Ukraine war) not in risk register
✗ Lithium price spike ($80K/ton) not anticipated
✗ Multiple simultaneous disruptions (COVID + war + demand surge)

→ Needed RESILIENCE, not just risk mitigation

5 PRINCIPLES OF RESILIENT SYSTEMS:
═══════════════════════════════════════════════════

1. DIVERSITY (Multiple Options)
┌──────────────────────────────────────────────────┐
│ Don't put all eggs in one basket                 │
│                                                  │
│ FRAGILE APPROACH (Pre-2022):                     │
│ ✗ Single chemistry: NCM only                     │
│ ✗ Single geography: China dominance (70%)        │
│ ✗ Single supplier: Buy from one Tier 1           │
│                                                  │
│ RESILIENT APPROACH (Post-2022):                  │
│ ✓ Chemistry diversity:                           │
│   • NCM (nickel-cobalt-manganese) for long range│
│   • LFP (lithium iron phosphate) for std range   │
│   → If nickel spikes, use LFP                    │
│                                                  │
│ ✓ Geographic diversity:                          │
│   • US lithium (Nevada, California)              │
│   • Australian lithium                           │
│   • Canadian refining                            │
│   • Asian cell production                        │
│   → If China restricted, alternatives exist      │
│                                                  │
│ ✓ Supplier diversity:                            │
│   • Multiple suppliers (LG + CATL + SK + own)    │
│   • Vertical integration (own production)        │
│   → If one supplier fails, others continue       │
│                                                  │
│ RESULT: Failure of one path doesn't stop system  │
└──────────────────────────────────────────────────┘

2. REDUNDANCY (Spare Capacity)
┌──────────────────────────────────────────────────┐
│ Build slack into the system                      │
│                                                  │
│ FRAGILE (Lean/Optimized):                        │
│ ✗ Just-in-time (zero inventory)                  │
│ ✗ 100% capacity utilization (no slack)           │
│ ✗ Optimized for cost (maximum efficiency)        │
│ → Any disruption stops production                │
│                                                  │
│ RESILIENT (Robust):                              │
│ ✓ Strategic stockpiles:                          │
│   • 3-6 months lithium reserve                   │
│   • Battery pack safety stock                    │
│                                                  │
│ ✓ Excess capacity:                               │
│   • Build for 1.2M vehicles, plan for 1M         │
│   • 20% buffer for demand surges                 │
│                                                  │
│ ✓ Multiple production lines:                     │
│   • If one line fails, others operate            │
│                                                  │
│ TRADE-OFF:                                       │
│ • Cost: Redundancy is expensive (idle capacity)  │
│ • Value: Insurance against disruption            │
│                                                  │
│ EXAMPLE: Tesla's lithium reserves (2021)         │
│ • Stockpiled at $20K/ton                         │
│ • When spike hit ($80K/ton), saved $1B+          │
│ • Redundancy paid for itself many times over     │
└──────────────────────────────────────────────────┘

3. MODULARITY (Plug-and-Play Components)
┌──────────────────────────────────────────────────┐
│ Standardize interfaces, enable swapping          │
│                                                  │
│ FRAGILE (Highly Integrated):                     │
│ ✗ Structural battery pack (battery = body part)  │
│ ✗ Custom pack for each supplier                  │
│ ✗ Can't switch suppliers without redesign        │
│ → Locked into single supplier                    │
│                                                  │
│ RESILIENT (Modular):                             │
│ ✓ Standardized battery module interface          │
│ ✓ Multiple suppliers can provide compatible modules│
│ ✓ Can switch suppliers in 3-6 months (not 2 years)│
│                                                  │
│ TRADE-OFF:                                       │
│ • Performance: Integration may be less optimal   │
│ • Flexibility: Can change suppliers rapidly      │
│                                                  │
│ EXAMPLE: GM Ultium platform                      │
│ • Modular battery architecture                   │
│ • Can use LG or CATL cells in same pack          │
│ • Supplier flexibility                           │
└──────────────────────────────────────────────────┘

4. ADAPTABILITY (Learn and Evolve Fast)
┌──────────────────────────────────────────────────┐
│ Ability to change direction quickly              │
│                                                  │
│ FRAGILE (Fixed Plans):                           │
│ ✗ 5-year plan locked in                          │
│ ✗ Single technology bet (NCM only)               │
│ ✗ Slow decision cycles (annual reviews)          │
│ → Can't respond to rapid changes                 │
│                                                  │
│ RESILIENT (Adaptive):                            │
│ ✓ Rolling forecasts (update quarterly)           │
│ ✓ Parallel technology paths:                     │
│   • Develop NCM AND LFP simultaneously           │
│   • Hedge technology risk                        │
│                                                  │
│ ✓ Rapid prototyping:                             │
│   • Test new suppliers/chemistries quickly       │
│   • Fail fast, learn fast                        │
│                                                  │
│ ✓ Decentralized decision-making:                 │
│   • Empower teams to pivot locally               │
│   • Don't wait for HQ approval                   │
│                                                  │
│ EXAMPLE: Tesla's chemistry pivot                 │
│ • 2020: NCM cells (high performance)             │
│ • 2021: Lithium price rising → explore LFP      │
│ • 2022: LFP for standard range models (50% mix)  │
│ • Adapted in <18 months                          │
│                                                  │
│ Ford: Slower to adapt (just announcing LFP 2024) │
└──────────────────────────────────────────────────┘

5. FAST FEEDBACK LOOPS (Detect and Respond)
┌──────────────────────────────────────────────────┐
│ See problems early, act immediately               │
│                                                  │
│ FRAGILE (Slow Detection):                        │
│ ✗ Annual supplier audits                         │
│ ✗ Quarterly risk reviews                         │
│ ✗ React after crisis already hit                 │
│ → Too slow for fast-moving disruptions           │
│                                                  │
│ RESILIENT (Real-Time Monitoring):                │
│ ✓ Daily supplier scorecards:                     │
│   • On-time delivery, quality, capacity          │
│   • Alerts trigger investigation                 │
│                                                  │
│ ✓ Market intelligence:                           │
│   • Real-time lithium prices                     │
│   • Geopolitical monitoring                      │
│   • Early warning indicators                     │
│                                                  │
│ ✓ Rapid response protocols:                      │
│   • Alert → Decision → Action in 24-48 hours     │
│   • Pre-authorized contingency actions           │
│                                                  │
│ EXAMPLE: Early lithium price monitoring (2021)   │
│ • Companies watching prices daily saw spike coming│
│ • Locked in contracts before peak                │
│ • Saved billions                                 │
│                                                  │
│ Companies not monitoring: Caught flat-footed     │
└──────────────────────────────────────────────────┘

RESILIENCE IN ACTION: 2011 JAPAN EARTHQUAKE
═══════════════════════════════════════════════════

EVENT: March 2011 earthquake/tsunami
• Disrupted Japanese suppliers (semiconductors, parts)
• Affected ALL automakers globally

TOYOTA (High Resilience):
┌──────────────────────────────────────────────────┐
│ ORGANIZATIONAL CAPABILITIES:                     │
│ ✓ Keiretsu network (deep supplier relationships) │
│ ✓ Supply chain visibility (knew tier 2/3 suppliers)│
│ ✓ Rapid damage assessment (engineers to sites)   │
│ ✓ Collaborative culture (helped suppliers rebuild)│
│                                                  │
│ RESPONSE:                                        │
│ • Day 1: Damage assessment teams deployed        │
│ • Week 1: Identified critical parts shortages    │
│ • Month 1: Reallocated production to unaffected plants│
│ • Month 3: Helped suppliers rebuild              │
│ • Month 6: Back to normal production             │
│                                                  │
│ RECOVERY TIME: 6 months                          │
└──────────────────────────────────────────────────┘

FORD/GM (Lower Resilience):
┌──────────────────────────────────────────────────┐
│ ORGANIZATIONAL GAPS:                             │
│ ✗ Arm's-length supplier relationships            │
│ ✗ Limited supply chain visibility                │
│ ✗ Slower damage assessment                       │
│ ✗ Less collaborative culture                     │
│                                                  │
│ RESPONSE:                                        │
│ • Week 1: Began understanding scope              │
│ • Month 1: Identified which suppliers affected   │
│ • Month 2-3: Scrambled for alternatives          │
│ • Month 6-9: Still recovering                    │
│ • Month 12: Back to normal                       │
│                                                  │
│ RECOVERY TIME: 9-12 months (2x slower)           │
└──────────────────────────────────────────────────┘

LESSON: Resilience is ORGANIZATIONAL CAPABILITY
• Not just risk register
• Culture, relationships, processes, visibility
• Built over years, tested in crisis

RESILIENCE SELF-ASSESSMENT FOR YOUR PROJECTS:
═══════════════════════════════════════════════════

Ask these questions:

1. SINGLE POINTS OF FAILURE
   "What's the ONE thing that could kill our project?"
   • Single supplier? Single technology? Single person?
   • If yes → Build diversity/redundancy

2. STRESS TESTING
   "Can we survive if our top assumption is wrong?"
   • Assumption: Supplier delivers on time
   • Test: What if they don't? Do we have Plan B?

3. FEEDBACK LOOPS
   "How quickly can we detect problems?"
   • Weekly reviews? Monthly? Quarterly?
   • Faster feedback = earlier intervention

4. ADAPTABILITY
   "How quickly can we pivot?"
   • Locked into contracts? Can't change?
   • Build optionality and flexibility

5. OPTIONS
   "Do we have Plan B, C, D?"
   • Single path = fragile
   • Multiple options = resilient

RESILIENCE vs. RISK MANAGEMENT SUMMARY:
═══════════════════════════════════════════════════

Dimension    │ Risk Management    │ Resilience Thinking
─────────────┼────────────────────┼─────────────────────
Focus        │ Prevent KNOWN      │ Survive UNKNOWN
             │ failures           │ shocks
─────────────┼────────────────────┼─────────────────────
Approach     │ Identify & mitigate│ Build adaptive
             │ risks              │ capacity
─────────────┼────────────────────┼─────────────────────
Mindset      │ Control future     │ Prepare for
             │                    │ uncertainty
─────────────┼────────────────────┼─────────────────────
Strategy     │ Efficiency +       │ Robustness +
             │ mitigation         │ flexibility
─────────────┼────────────────────┼─────────────────────
Tools        │ Risk register,     │ Diversity, redundancy,
             │ FMEA, treatment    │ modularity, adaptation
─────────────┼────────────────────┼─────────────────────
Goal         │ Zero failures      │ Fast recovery
─────────────┼────────────────────┼─────────────────────
Question     │ "What could go     │ "How do we survive
             │  wrong?"           │  what we can't predict?"

YOU NEED BOTH:
• Risk Management for KNOWN threats
• Resilience for UNKNOWN threats

KEY TAKEAWAY:

"You can't predict every risk.
But you can build systems that survive anything.

Resilience = Diversity + Redundancy + Adaptability

The battery crisis taught the industry:
Lean and optimized = Fragile
Robust and flexible = Resilient

Choose resilience for critical systems."
```

**Class Exercise (5 min):**

> "Think about your final project or a system you're working on.
>
> Apply the resilience self-assessment:
> 1. What's your single point of failure?
> 2. Do you have Plan B?
> 3. How quickly can you detect problems?
> 4. Can you pivot if your main assumption is wrong?
>
> Share with your neighbor: What makes your project fragile? How could you increase resilience?"

**Instructor Debrief:**

> "Most engineering projects optimize for efficiency: lowest cost, fastest schedule, leanest process. That works in stable environments.
>
> But automotive systems operate in uncertain environments: supply chains, regulations, technology, competition. **Resilience is insurance against the unknown.**
>
> The trade-off is real: Resilience costs money (redundancy, excess capacity, stockpiles). But fragility costs MORE when shocks hit.
>
> Your job as systems engineers: **Balance efficiency and resilience based on risk.**"

**Learning Connection:** LO2, LO3 - Resilience thinking, systems thinking, adaptive capacity

---

## 3.3 Key Takeaways from EV Battery Supply Chain Case

**For wrap-up discussion (Slide 27-28):**

### Supply Chain & Resilience Lessons:

1. **Opportunity Windows Are Time-Limited**
   - Early movers (Tesla 2020) captured huge advantage
   - Late movers (Ford 2023) paying catch-up costs
   - Strategic opportunities require decisive action

2. **Geopolitical Risk Is Real**
   - 70% China concentration = vulnerability
   - Diversification takes 5-10 years (long lead times)
   - Supply chain is national security issue for EVs

3. **Just-in-Time Is Fragile**
   - Optimized for efficiency, not robustness
   - Breaks catastrophically when disrupted
   - Just-in-case (reserves) better for critical materials

4. **Vertical Integration vs. Outsourcing Trade-Off**
   - Outsource = Lower capital, less control
   - Integrate = Higher capital, more control
   - Right answer depends on strategic importance

5. **Resilience Requires Diversity**
   - Chemistry diversity (NCM + LFP)
   - Geographic diversity (multi-region sourcing)
   - Supplier diversity (multiple sources)

6. **Redundancy Is Insurance**
   - Costs money upfront (idle capacity, inventory)
   - Saves massively when shocks hit
   - Right level depends on criticality and volatility

7. **Fast Feedback Loops Enable Adaptation**
   - Real-time monitoring catches trends early
   - Early warning allows preemptive action
   - Reactive responses are more expensive

8. **Technology Diversification Hedges Risk**
   - Don't bet everything on one chemistry
   - Parallel paths provide options
   - Flexibility to pivot as markets change

---

## 3.4 Discussion Prompts for Students

**Use throughout or at end:**

1. **"Was Tesla's $10-15B battery investment in 2020 reckless or visionary?"**
   - Debate: Risk-taking vs. prudent planning

2. **"Should governments mandate domestic battery production for national security?"**
   - Explore: Free market vs. strategic autonomy, trade-offs

3. **"How much resilience (redundancy, diversity) is enough?"**
   - Trade-off analysis: Cost vs. insurance value

4. **"If you were Ford in 2020, would you have followed Tesla's vertical integration path?"**
   - Consider: Company culture, capital constraints, core competency

5. **"What role should OEMs play in lithium mining (upstream integration)?"**
   - Discuss: How far up the value chain to integrate

---

**END OF CASE STUDY 3**

---

# INTEGRATION ACROSS ALL THREE CASES

## How to Use All Three Cases in Automotive Applications Section (Slides 23-26)

### Slide 23: Automotive Program Management Context

**Integration Point:**

> "We've seen three case studies showing different aspects of PM/RM in automotive:
>
> **Cybertruck (Project Planning):** What happens when planning is optimistic and resource allocation is insufficient. Result: 2-year delays, cost overruns.
>
> **F-150 Lightning (Risk Management):** What happens when a Catastrophic-impact risk isn't treated with sufficient rigor. Result: $1.8B recall, production halt.
>
> **Battery Supply Chain (Opportunity & Resilience):** What happens when strategic opportunities are seized vs. missed, and how resilience thinking differs from risk management. Result: Competitive advantage vs. disadvantage.
>
> Now let's see how these integrate with formal automotive program management standards like APQP and VDA."

**Show how all three cases relate to APQP phases:**

| APQP Phase | Cybertruck Lesson | F-150 Lightning Lesson | Supply Chain Lesson |
|------------|-------------------|----------------------|-------------------|
| **Phase 1: Plan & Define** | WBS underestimated complexity, schedule unrealistic | Risk identification done, treatment insufficient | Opportunity to vertical integrate missed (Ford) or captured (Tesla) |
| **Phase 2: Product Design** | Design complexity (exoskeleton) drove delays | Battery design vulnerable to cell defects | Chemistry diversity strategy (NCM vs LFP) |
| **Phase 3: Process Design** | Manufacturing process had to be invented (not in plan) | Cell manufacturing process had contamination risk | Supply chain process resilience (diversification) |
| **Phase 4: Validation** | Insufficient validation of manufacturing process | Validation testing didn't catch defect mode | Market validation (demand forecasting) |
| **Phase 5: Launch & Production** | Production ramp struggles (24 months late) | Production halt (battery fire risk) | Production constrained by supply allocation |

---

### Slide 24: Risk Management in Automotive Systems

**Integration Point:**

> "Automotive risk management has specific tools and standards. Let's see how our three cases map to them."

**FMEA (Failure Mode and Effects Analysis):**

| Case | Failure Mode | Effect | Current Controls | What Was Missing |
|------|--------------|--------|------------------|------------------|
| **Cybertruck** | Manufacturing process too complex | Schedule delay, cost overrun | Project schedule, resource plan | TRL assessment, risk-adjusted schedule |
| **F-150 Lightning** | Battery cell contamination | Fire, injury/death, recall | Supplier QMS, incoming sampling | 100% screening, cell-level containment, predictive monitoring |
| **Supply Chain** | Lithium supply shortage | Production constraint, cost spike | Supplier contracts | Strategic reserves, vertical integration, geographic diversity |

---

### Slide 25: Integration with ISO 26262 Functional Safety

**Integration Point:**

> "For safety-critical systems like batteries, ISO 26262 functional safety standard applies alongside risk management."

**F-150 Lightning Through ISO 26262 Lens:**

| ISO 26262 Element | Application to Battery Fire Risk |
|-------------------|----------------------------------|
| **Hazard Analysis** | Battery fire in customer vehicle → Injury/death hazard |
| **ASIL Determination** | Severity: S3 (life-threatening), Exposure: E4 (frequent), Controllability: C3 (uncontrollable) → **ASIL D** (highest) |
| **Safety Goals** | Prevent battery thermal runaway in normal operation |
| **Safety Concept** | Multi-layer: Cell-level fault detection + pack-level isolation + thermal management + BMS monitoring |
| **Safety Requirements** | Cell manufacturing defects shall be detected before pack assembly (ASIL D requirement) |
| **Verification** | 100% cell screening, validation testing with fault injection |

**What Ford likely did:**
- Applied ISO 26262 to *design* risks (thermal management, BMS, crash protection) ✓
- Did NOT apply ASIL D rigor to *manufacturing* risks (cell defects) ✗

**Lesson:** Manufacturing risks for safety-critical components deserve same rigor as design risks.

---

### Slide 26: Case Study Integration - Lessons Applied

**Synthesis across all three cases:**

**Question for class:** "If you were starting a new EV program today, what would you do differently based on these three case studies?"

**Model Answer:**

**PROJECT PLANNING (From Cybertruck):**
✓ Conduct Technology Readiness Assessment before committing schedules
✓ Use 3-point estimation (optimistic/likely/pessimistic) for novel work
✓ Model resource allocation across portfolio (avoid resource conflicts)
✓ Build 20-30% schedule contingency for R&D work
✓ Separate "committed dates" (external, P80) from "target dates" (internal, P50)

**RISK MANAGEMENT (From F-150 Lightning):**
✓ Identify safety-critical subsystems (battery → ASIL D)
✓ Apply extraordinary rigor to Catastrophic-impact risks (even if low probability)
✓ Defense in depth: Prevention + Detection + Containment + Response
✓ Don't rely solely on supplier quality systems for critical parts
✓ Define escalation triggers and empower rapid response
✓ Implement proactive field monitoring with predictive analytics

**OPPORTUNITY & RESILIENCE (From Supply Chain):**
✓ Identify strategic opportunities early (vertical integration decision in 2020, not 2023)
✓ Build resilience through diversity (chemistry, geography, suppliers)
✓ Maintain strategic reserves for critical materials (3-6 months stock)
✓ Design for modularity to enable supplier flexibility
✓ Fast feedback loops (real-time monitoring of markets, suppliers, risks)
✓ Scenario planning for geopolitical/market disruptions

**INTEGRATED APPROACH:**

**Phase 1 (Concept):**
- Opportunity analysis: Vertical integrate batteries? (Strategic decision)
- TRL assessment: What technologies are novel? (Drives schedule)
- Supply chain resilience: Lithium/cobalt sourcing strategy

**Phase 2 (Development):**
- WBS with explicit R&D work packages (don't hide complexity)
- Risk register with Catastrophic-impact items flagged (ASIL D treatment)
- Resource allocation plan (cross-program conflicts identified)

**Phase 3 (Validation):**
- Worst-case stress testing (not just nominal validation)
- 100% screening for safety-critical defects (or equivalent mitigation)
- Supply chain qualification and reserves locked in

**Phase 4 (Production):**
- Gate reviews with go/no-go authority (don't proceed with red flags)
- Real-time monitoring (technical performance, supplier health, market conditions)
- Rapid response protocols (halt production if safety issue emerges)

**Phase 5 (Field):**
- Proactive monitoring (telemetry, predictive analytics)
- Continuous learning (update risk register based on field data)
- Adaptive strategy (pivot quickly based on market/technology shifts)

---

# INSTRUCTOR QUICK REFERENCE GUIDE

## Timing Recommendations (120 minutes total)

| Section | Time | Primary Case |
|---------|------|--------------|
| **Opening & Hook** | 5 min | Mars Climate Orbiter (keep from original) + Transition to automotive cases |
| **Project Planning Process** | 25 min | **Cybertruck** (Slides 9-14) |
| **Risk Management Process** | 30 min | **F-150 Lightning** (Slides 15-19) + **Supply Chain** (Slides 20-22) |
| **Automotive Applications** | 15 min | Integration across all three cases (Slides 23-26) |
| **Wrap-up & Discussion** | 15 min | Synthesis, Q&A |
| **Buffer** | 30 min | Built into discussion/Q&A time |

## Key Transitions Between Cases

**Transition 1: From Cybertruck to F-150 Lightning (After Slide 14)**
> "We've seen how project planning failures cost Tesla 2-3 years and billions of dollars. But at least Cybertruck delays didn't put anyone's safety at risk.
>
> Now let's look at a risk management failure where safety WAS at stake: Ford F-150 Lightning battery fire and recall. This is where risk management is not just about cost and schedule—it's about preventing harm."

**Transition 2: From F-150 Lightning to Supply Chain (After Slide 19)**
> "We've covered THREAT risks—things that cause harm. But risk management also includes OPPORTUNITY management and resilience thinking.
>
> The EV battery supply chain crisis shows both: Some companies saw opportunity and captured it. Others missed the opportunity and paid the price. And everyone learned that resilience matters as much as risk mitigation."

**Transition 3: To Automotive Applications Integration (After Slide 22)**
> "Now we've seen three very different cases—project planning, risk management, and resilience. Let's bring it all together and see how these apply to automotive program management standards and your future work."

## Discussion Questions by Level

**Knowledge Level (Recall):**
- What were the root causes of Cybertruck delays?
- What was the Ford F-150 Lightning battery defect?
- What caused lithium prices to spike in 2022?

**Comprehension Level (Understand):**
- Why did Tesla's vertical integration strategy succeed?
- How did risk treatment fail for F-150 Lightning?
- What's the difference between resilience and risk management?

**Application Level (Apply):**
- How would you apply TRL assessment to a new vehicle program?
- What risk treatment would you recommend for a safety-critical battery?
- How would you build supply chain resilience for a new EV?

**Analysis Level (Analyze):**
- What were the critical decision points where Ford could have prevented the battery crisis?
- Compare Tesla and Ford's strategic choices in 2020—what drove different outcomes?
- Analyze the trade-offs between cost optimization and resilience.

**Evaluation Level (Evaluate):**
- Was Ford's decision to rely on external suppliers justified in 2020?
- Evaluate whether 100% cell screening should be mandatory for all EVs.
- Should battery supply chain be treated as national security priority?

**Synthesis Level (Create):**
- Design a risk management plan for a new EV battery program.
- Create a resilience strategy for automotive supply chains.
- Develop decision criteria for vertical integration vs. outsourcing.

## Key Figures and Data for Reference

**Cybertruck:**
- Announcement: Nov 2019
- Promised: Late 2021
- Delivered: Nov 2023 (24 months late)
- Cost overrun: Est. $5-7B vs. $2-3B planned (+100-130%)
- Price: $39,900 promised → $99,990 actual (+150%)

**F-150 Lightning:**
- Production halt: Feb 9, 2023
- Recall: 18,666 vehicles
- Cost: $1.8B+ (battery replacement)
- Production lost: ~13,500 units over 3 months

**Battery Supply Chain:**
- Lithium price: $15K/ton (2020) → $80K/ton (2022 peak) → $20K/ton (2024)
- China concentration: 70% processing, 60% cells
- Tesla advantage: $110-120/kWh vs. Ford $150/kWh ($30-40/kWh gap)
- Investment: $400B+ globally in battery supply chain (2022-2030)

---

## Slide-by-Slide Case Study Mapping

**Original Slide** → **Case Study Integration** → **Teaching Point**

**Slide 9 (Project Planning Overview)** → Cybertruck intro → What happens when planning fails

**Slide 10 (WBS)** → Cybertruck WBS breakdown → Complexity drives everything

**Slide 11 (Scheduling)** → Cybertruck critical path analysis → Dependencies and TRL

**Slide 12 (Resources)** → Cybertruck resource constraints → Allocation drives feasibility

**Slide 13 (Deliverables)** → Cybertruck TRA missing → Key planning artifacts

**Slide 14 (Assessment & Control)** → Cybertruck EVM analysis → Early warning signals

**Slide 15 (Risk Mgmt Overview)** → F-150 Lightning intro → Safety-critical risks

**Slide 16 (Risk Identification)** → F-150 FMEA → Identifying battery risks

**Slide 17 (Risk Analysis)** → F-150 probability × impact → Catastrophic requires rigor

**Slide 18 (Risk Treatment)** → F-150 mitigation gaps → Layered defense needed

**Slide 19 (Risk Monitoring)** → F-150 early warning missed → Triggers and authority

**Slide 20 (Opportunity Mgmt)** → Supply chain opportunity → Tesla vs. Ford strategic choices

**Slide 21 (Risk Reserves)** → Supply chain reserves → Insurance against volatility

**Slide 22 (Resilience)** → Supply chain resilience → Beyond risk management

**Slides 23-26 (Automotive Applications)** → All three cases → Integration with APQP, ISO 26262

---

**END OF DETAILED CASE STUDY GUIDE**

---

# APPENDIX: Additional Resources for Instructor

## Recommended Pre-Class Preparation

**Videos/Articles (Optional student pre-reading):**
- Cybertruck delivery event (Nov 2023) - 15 min
- Ford F-150 Lightning recall news coverage - 5 min
- Battery supply chain documentary - 20 min

**Instructor Prep:**
- Review latest news on all three cases (update figures if needed)
- Prepare backup slides with additional data if students want deeper dive
- Have risk matrix templates ready for class exercises

## Potential Student Objections and Responses

**Objection 1:** "Hindsight bias—easy to criticize Tesla/Ford decisions after the fact."

**Response:** "Absolutely true. That's why I showed you the data available in 2020-2021. Could they have known? Risk management is about making good decisions under uncertainty, not predicting the future perfectly. But better analysis (TRL, reserves, resilience) would have improved their odds."

**Objection 2:** "Tesla can afford to take risks because Elon Musk doesn't care about losses. Ford has shareholders."

**Response:** "Fair point—risk tolerance differs. But Ford is now spending the same $10-15B Tesla spent, just 3-4 years later. They're not avoiding the cost, just delaying it and losing competitive advantage. Sometimes 'conservative' is actually riskier long-term."

**Objection 3:** "100% cell screening is too expensive—kills EV economics."

**Response:** "Let's do the math: 100% screening costs ~$100K per vehicle upfront. Ford's recall cost $100K per vehicle in hindsight. Economically equivalent. But screening prevents safety risk and brand damage. For safety-critical systems, cost isn't the only factor—precautionary principle applies."

---

## Engagement Boosters

**Use props/visuals:**
- Show actual lithium carbonate sample (if available)
- Display risk matrix on whiteboard, have students place cases
- Timeline visualization (Cybertruck delays, battery price spike)

**Interactive elements:**
- Live polls: "Who would choose Option A vs. B?"
- Think-pair-share exercises throughout
- Breakout groups for 5-min case analysis

**Real-world connections:**
- "How many of you drive/rode in EVs?" (Personal relevance)
- "What would you do if YOUR Lightning was recalled?" (Customer perspective)
- "Would you work for Tesla or Ford based on these cases?" (Career choice)

---

**FINAL NOTE FOR INSTRUCTOR:**

These cases are current as of Feb 2025. Update specific figures and dates as needed. The principles (PM/RM failures, resilience thinking) remain timeless even as details evolve.

The goal: Make project and risk management REAL and RELEVANT to automotive students by showing:
- Real companies they know
- Real money ($Billions) at stake
- Real consequences (recalls, delays, competitive advantage/disadvantage)
- Real decisions they'll face in their careers

**Make it matter. Make it memorable.**

