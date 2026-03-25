# Week 2, Day 9: Diesel Service & Overhaul

## Metadata
- **Module:** Week 2 - Advanced Engine Technologies
- **Day:** 9 of 30
- **Target Audience:** Entry-level automotive technicians, age 16-30, foundation level (completed Day 8 diesel injection)
- **Cultural Context:** India-specific (BS4/BS6 standards, Innova/Scorpio diesel vehicles)
- **Target Medium:** PowerPoint/Presentations (instructor-led, 3-hour theory session)
- **Learning Outcomes Covered:** AMS-SO-2-3-2, AMS-SO-2-3-3
- **Storytelling Technique Used:** Scenario-Based Learning

---

## Session Outcome 1: AMS-SO-2-3-2

### Learning Outcome Details
- **Code:** AMS-SO-2-3-2
- **Description:** Service diesel particulate filter (DPF) including cleaning and forced regeneration; replace fuel filters using proper bleeding procedure; service air filter and intake system; check and adjust injection timing (mechanical systems).
- **Category:** Skill
- **Bloom's Level:** Apply
- **Session Type:** Lecture + Service demonstration
- **Parent MO:** AMS-MO-2-2 (Diesel Engine Systems)

---

## Session Outcome 2: AMS-SO-2-3-3

### Learning Outcome Details
- **Code:** AMS-SO-2-3-3
- **Description:** Perform compression test on diesel engine and interpret results; measure cylinder bore wear accounting for higher compression ratios; inspect and measure diesel-specific components (glow plugs, injector seats, piston bowl condition); understand diesel head gasket considerations.
- **Category:** Skill
- **Bloom's Level:** Apply, Analyze
- **Session Type:** Lecture + Diagnostic demonstration
- **Parent MO:** AMS-MO-2-2 (Diesel Engine Systems)

### Storytelling Approach
- **Technique:** Scenario-Based Learning
- **Rationale:** Diesel service involves multiple real-world scenarios technicians encounter regularly: DPF clogged (requires regeneration), high-mileage diesel overhaul (requires compression testing and component inspection), fuel filter replacement (common maintenance). Scenario-based narrative shows how character (Anjali) applies procedures in realistic service center context, building confidence and procedural knowledge.
- **Grouping:** Grouped (both SOs involve diesel-specific service and diagnostic procedures)

---

## Story Framework - Scenario-Based Learning

### Narrative Voice
- **Perspective:** Third-person narrative following character Anjali
- **Character:** Anjali, 22-year-old technician with 1.5 years experience, recently trained on diesel systems
- **Setting:** Authorized Tata service center, Mumbai, busy service day
- **Tone:** Practical, procedural, confidence-building

### Story Beats (Scenario Structure)

#### Scenario 1: DPF Regeneration Service (40 minutes)
**"Customer complains: 'DPF warning light on, loss of power.' Anjali must diagnose and perform forced regeneration."**

**Morning, 9:00 AM - Customer Arrival:**

Anjali checked the service schedule. First job: Tata Harrier diesel, 85,000 km, DPF warning light illuminated, customer reports power loss.

She connected the scan tool and read the DTC: **P2002 - Diesel Particulate Filter Efficiency Below Threshold (Bank 1)**.

Freeze frame data:
- Soot Load: 92% (specification: Maximum 75% before regeneration required)
- Exhaust Back Pressure: 2.8 bar (normal: <1.5 bar)
- DPF Inlet Temperature: 340°C

**Diagnosis:** DPF clogged with soot, requires regeneration.

**Understanding DPF (Quick Review):**

The diesel particulate filter traps soot particles from exhaust to meet BS6 emission standards. Over time, soot accumulates. Normal operation: ECU triggers automatic regeneration (burns off soot at 600°C) during highway driving.

**Problem:** City driving (frequent stops, low exhaust temps) prevents automatic regeneration. Soot builds up, clogs filter, triggers warning light.

**Anjali's Service Procedure:**

**Step 1: DPF Inspection (Visual)**
- Removed plastic cover to access exhaust system
- Inspected DPF housing for cracks, leaks (none found)
- Checked exhaust back pressure using pressure gauge: 2.7 bar (confirms blockage)

**Step 2: Forced Regeneration Decision**
- Soot load 92%: Regeneration possible (if >95%, cleaning or replacement required)
- Exhaust system intact: Safe to regenerate
- Fuel level: 3/4 tank (regeneration consumes extra fuel, requires >1/4 tank)

Decision: Proceed with forced regeneration using scan tool.

**Step 3: Forced Regeneration Procedure**
1. Ensured vehicle in safe location (well-ventilated area, away from flammable materials)
2. Connected scan tool, navigated to DPF service functions
3. Selected "Forced Regeneration" command
4. Followed on-screen prompts:
   - Engine must be at operating temperature (check: 92°C ✓)
   - Parking brake engaged ✓
   - Transmission in neutral ✓
   - All electrical loads off (A/C, lights) ✓
5. Initiated regeneration sequence
6. ECU increased exhaust temperature by:
   - Post-injection (injecting fuel after combustion to raise exhaust temp)
   - Increasing idle speed to 1500 RPM
   - Closing EGR valve (prevents cooling of exhaust gases)

**Monitoring Progress:**
- DPF inlet temp: 350°C → 580°C → 620°C (soot ignition temperature reached)
- Soot load: 92% → 75% → 52% → 28% → 15% (soot burning off)
- Duration: 22 minutes

**Step 4: Verification**
- Regeneration complete (scan tool message: "Regeneration Successful")
- Soot load: 15% (normal operating range)
- Back pressure: 1.2 bar (normal)
- DTC P2002 cleared
- DPF warning light off

**Customer Education:**

Anjali explained to the customer: "Your DPF was 92% full of soot because you drive mostly in city traffic. I've regenerated it—burned off the soot. To prevent this, drive on the highway for 20 minutes every two weeks at 60-80 km/h. This allows the system to regenerate automatically."

**Cost:** ₹1,200 (forced regeneration labor). Alternative if ignored: DPF replacement ₹65,000.

---

#### Scenario 2: High-Mileage Diesel Overhaul (70 minutes)
**"Mahindra Scorpio 2.2L diesel, 250,000 km, excessive smoke and oil consumption. Anjali performs compression test and inspects engine for overhaul decision."**

**Afternoon, 2:00 PM - Diagnostic Challenge:**

Customer complaint: Blue-gray smoke from exhaust, engine consuming 1 liter of oil every 1,000 km, loss of power.

Anjali suspected piston ring wear or cylinder bore wear—classic high-mileage diesel symptoms.

**Step 1: Compression Test (Diesel-Specific Procedure)**

**Diesel vs. Petrol Compression Test Differences:**
- **Diesel:** Compression ratio 16:1 to 20:1 (much higher than petrol 9:1 to 11:1)
- **Normal diesel compression:** 28-35 bar (vs. petrol 10-14 bar)
- **Test procedure:** Crank engine with glow plugs or injectors removed

**Anjali's Procedure:**
1. Warmed engine to operating temperature (80°C+)
2. Disabled fuel injection (disconnected injector harness)
3. Removed glow plugs from all 4 cylinders
4. Installed compression gauge adapter in Cylinder 1 glow plug hole
5. Cranked engine for 5-6 compression strokes (battery fully charged, important)
6. Recorded peak pressure: **24 bar**
7. Repeated for Cylinders 2, 3, 4

**Results:**

| Cylinder | Compression (bar) | Specification | Assessment |
|----------|-------------------|---------------|------------|
| 1 | 24 | 30-35 bar | ✗ Low (71% of spec) |
| 2 | 26 | 30-35 bar | ✗ Low (76% of spec) |
| 3 | 32 | 30-35 bar | ✓ Within spec |
| 4 | 33 | 30-35 bar | ✓ Within spec |

**Analysis:**
- Cylinders 1 and 2 significantly low (indicating worn rings or cylinder bore wear)
- Cylinders 3 and 4 normal
- Variation between cylinders: 9 bar (>15% variation = problem confirmed)

**Step 2: Wet Compression Test (Confirms Ring Wear)**

To confirm piston ring wear vs. valve sealing issue:
1. Squirted 10 ml of engine oil into Cylinder 1 through glow plug hole
2. Cranked engine again, measured compression: **30 bar** (increased from 24 bar)

**Interpretation:** Oil temporarily sealed worn piston rings, compression increased. Confirms piston ring wear.

**Step 3: Cylinder Bore Measurement (Disassembly Required)**

For accurate overhaul decision, Anjali recommended engine disassembly and bore measurement:
- Customer approved teardown estimate: ₹8,000 (labor)

After disassembly:
- Measured cylinder bore wear using bore gauge (from Week 1 training):
  - Cylinder 1: 87.08mm (spec: 87.00-87.02mm, Max taper 0.05mm)
  - Taper (top - bottom): 0.11mm (exceeds spec by 2×)
- Conclusion: Cylinders 1 and 2 require reboring to 0.50mm oversize

**Step 4: Diesel-Specific Component Inspection**

**Glow Plugs:**
- Tested resistance: 0.8-1.2 ohms (normal)
- Visual: Tips carbon-fouled but intact
- Decision: Clean and reuse (new glow plugs ₹600 each, not necessary)

**Injector Seats:**
- Inspected seats in cylinder head for erosion (high-pressure fuel spray can erode aluminum)
- Cylinder 3 seat showed minor erosion (pitting)
- Decision: Machine seat to restore sealing surface

**Piston Bowls (Combustion Chamber in Piston Crown):**
- Diesel pistons have bowl-shaped combustion chamber
- Inspected for cracks, carbon buildup, erosion
- Found heavy carbon deposits (cleaned with wire wheel)
- No cracks (common failure in overheated diesels)

**Head Gasket Condition:**
- Diesel head gaskets are multi-layer steel (MLS) due to high cylinder pressure
- Inspected for:
  - Compression leaks between cylinders (water jacket staining)
  - Coolant leaks (external coolant residue)
- Found minor coolant seepage between Cylinders 1-2
- Decision: Replace head gasket (₹3,500 MLS gasket)

**Step 5: Overhaul Recommendation and Estimate**

Anjali prepared comprehensive estimate:

**Required Repairs:**
- Rebore cylinders 1 and 2 to 0.50mm oversize: ₹12,000
- 0.50mm oversize pistons (2 units): ₹8,000
- Piston ring sets (4 cylinders): ₹4,500
- Head gasket (MLS): ₹3,500
- Machine injector seat (Cyl 3): ₹2,000
- Valve stem seals (16 valves): ₹1,200
- Timing belt kit (due at 250K km): ₹6,500
- Engine assembly labor: ₹18,000
- Oil and filter: ₹4,200
- **Total: ₹59,900**

**Customer Decision:** Approved (alternative: ₹1,80,000 replacement engine)

**Anjali's Professional Insight:**

"Sir, your Scorpio has 250,000 km. This overhaul will restore compression, stop oil consumption, and eliminate smoke. With proper maintenance after rebuild, you can expect another 150,000-200,000 km. Diesel engines are built to last if serviced correctly."

---

#### Scenario 3: Preventive Fuel Filter Service (20 minutes)
**"Routine 40,000 km service on Innova Crysta - fuel filter replacement with proper bleeding."**

**Anjali's Quick Service Procedure:**

**Step 1: Fuel Filter Replacement**
- Placed drip pan under filter housing
- Opened bleed screw, drained fuel
- Replaced filter element (₹1,100 OEM)
- Filled filter housing with clean diesel (priming)
- Installed new filter bowl O-ring

**Step 2: Bleeding (Procedure from Day 8)**
- Low-pressure bleeding: Hand primer pump, 40 strokes, no air bubbles from bleed screw
- High-pressure bleeding: Cranked engine with injector return fittings loosened
- Verified: Engine started normally, smooth idle, no air in system

**Time:** 25 minutes. **Customer happy:** No issues, preventive maintenance completed.

---

## Assessment Content

### Quiz Questions (5 Questions)

**Question 1: DPF Regeneration (Apply Level)**
A scan tool shows DPF soot load at 88%. What is the correct service action?

A) Replace DPF immediately
B) Perform forced regeneration using scan tool
C) Clean DPF manually with compressed air
D) Ignore warning, automatic regeneration will handle it

**Answer:** B) Perform forced regeneration using scan tool
**Explanation:** Soot load 75-95% can be cleared by forced regeneration. Above 95%, DPF requires manual cleaning or replacement. Forced regeneration burns off soot at 600°C. Never use compressed air (damages DPF structure).

---

**Question 2: Compression Test Interpretation (Analyze Level)**
Diesel compression test results: Cyl 1: 26 bar, Cyl 2: 32 bar, Cyl 3: 33 bar, Cyl 4: 31 bar (Spec: 30-35 bar). What action is required?

A) No action, all cylinders within specification
B) Investigate Cylinder 1 (low compression, perform wet test)
C) Replace head gasket (variation between cylinders)
D) Adjust valve clearances

**Answer:** B) Investigate Cylinder 1 (low compression, perform wet test)
**Explanation:** Cylinder 1 at 26 bar is below spec (30 bar minimum) and shows 19% variation from highest cylinder (33 bar). Variation >15% indicates problem. Wet test determines if rings or valves are cause.

---

**Question 3: DPF Service (Understand Level)**
Why does city driving prevent automatic DPF regeneration?

A) City traffic consumes too much fuel for regeneration
B) Low exhaust temperatures in stop-and-go traffic don't reach 600°C soot ignition point
C) ECU disables regeneration below 60 km/h
D) DPF system only works on highways

**Answer:** B) Low exhaust temperatures in stop-and-go traffic don't reach 600°C soot ignition point
**Explanation:** Regeneration requires exhaust temperature above 600°C to burn soot. City driving (idling, low load) produces ~300-400°C exhaust. Highway driving (sustained load, higher RPM) reaches 550-650°C, allowing automatic regeneration. ECU doesn't disable by speed, it's purely temperature-driven.

---

**Question 4: Diesel Overhaul (Analyze Level)**
A diesel engine shows 24 bar compression (spec 30-35 bar). After adding oil to cylinder, compression increases to 30 bar. What is the diagnosis?

A) Worn valve seats (valves not sealing)
B) Blown head gasket between cylinders
C) Worn piston rings (oil temporarily seals rings)
D) Incorrect compression gauge reading

**Answer:** C) Worn piston rings (oil temporarily seals rings)
**Explanation:** Wet compression test: If compression increases after adding oil, piston rings are worn (oil fills gaps, improves sealing). If compression doesn't increase, valves are cause (oil doesn't help valve sealing). This is classic ring wear diagnosis.

---

**Question 5: Safety - DPF Regeneration (Apply Level)**
Before performing forced DPF regeneration, what safety check is critical?

A) Disconnect battery negative terminal
B) Ensure vehicle in well-ventilated area away from flammable materials
C) Remove DPF from vehicle
D) Drain diesel fuel tank to prevent fire

**Answer:** B) Ensure vehicle in well-ventilated area away from flammable materials
**Explanation:** Forced regeneration raises DPF temperature to 600-700°C. Exhaust system is extremely hot and can ignite flammable materials (oil spills, rags, grass). Always regenerate outdoors or in well-ventilated shop away from combustibles. Never near fuel tanks, solvents, or paper.

---

### Hands-On Exercise Preview (Afternoon Practical - 3 Hours)

**Exercise:** DPF Forced Regeneration, Diesel Compression Test, Fuel Filter Replacement + Bleeding

**Success Criteria:**
- DPF regeneration completed successfully using scan tool (soot load reduced to <20%)
- Compression test performed correctly, data interpreted accurately (identify low cylinder)
- Fuel filter replaced and system bled properly (engine starts smoothly)

---

## Medium-Specific Adaptations

### PowerPoint Slides (40-45 slides)

**Key Segments:**
1. DPF service overview (function, regeneration process, forced regen procedure) - 15 slides
2. Compression testing (diesel-specific, wet test, interpretation) - 12 slides
3. Diesel overhaul components (glow plugs, injector seats, piston bowls, head gasket) - 10 slides
4. Fuel filter service (quick review from Day 8) - 5 slides
5. Assessment and practical prep - 5 slides

---

## Cultural & Contextual Customization

**Indian Vehicles:**
- Tata Harrier diesel (DPF-equipped, BS6)
- Mahindra Scorpio 2.2L diesel (high-mileage overhaul scenario)
- Toyota Innova Crysta (routine maintenance)

**Indian Context:**
- City traffic prevents DPF auto-regen (Mumbai, Delhi stop-and-go)
- High-mileage diesels common (250K+ km on Scorpio, built to last)
- Diesel overhaul economics: ₹60K overhaul vs. ₹1.8L replacement engine

**Costs:**
- DPF replacement: ₹65,000 (aftermarket ₹40,000)
- Forced regen labor: ₹1,200
- Diesel overhaul: ₹60,000 (complete)

---

## Lesson Summary

- **Total Session Outcomes:** 2 (AMS-SO-2-3-2, AMS-SO-2-3-3)
- **Technique Used:** Scenario-Based Learning (Anjali performs DPF regen, diesel overhaul diagnosis, fuel filter service)
- **Assessment Items:** 5 quiz questions, 1 comprehensive hands-on exercise
- **Indian Context:** Tata, Mahindra, Toyota diesels; BS6 DPF systems; realistic Indian service scenarios
- **Next Steps:** Day 10 - Turbocharger systems (many Indian diesels combine common rail + turbo)

---

**Framework Status:** ✅ Complete
**Generated:** 2026-01-11
**Technique Used:** Scenario-Based Learning
**Character:** Anjali (22, technician, 1.5 years experience)
**Ready for:** PowerPoint development and instructor delivery
