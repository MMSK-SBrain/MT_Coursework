# NamTech EV Lab Course Design - Summary

**Course Name:** NamTech EV Systems - Hands-on Laboratory Training
**Course Code:** NEVLAB
**Target Audience:** UG/PG Engineering Students
**Course Type:** 100% Practical Laboratory Course
**Equipment:** 10 Major Setups
**Total Labs:** 54 Hands-on Sessions
**Total Learning Outcomes:** 88 (5 COs + 15 MOs + 68 SOs)

---

## Files Generated

| File | Description |
|------|-------------|
| `00-requirements.md` | Complete requirements gathering document with equipment details |
| `01-checklist.md` | Course design progress checklist |
| `02-course-structure.md` | Detailed learning outcomes structure (all 54 labs with descriptions) |
| `03-template-partial.xlsx` | **Excel template** (Module 1 complete + partial Module 2 as example) |
| `README.md` | This summary document |

---

## Course Structure Overview

### Module 1: Battery Systems (Days 1-6)
**Equipment:** Setup 1 (Battery Assembly), Setup 2 (BMS Analyzer), Setup 3 (Charge-Discharge Bench)

| Lab | Name | SOs |
|-----|------|-----|
| 1.1 | Battery Pack Assembly Fundamentals | 4 |
| 1.2 | BMS Integration and Testing | 4 |
| 1.3 | BMS Programming and CAN Communication | 4 |
| 1.4 | Battery Pack Load Testing | 4 |
| 1.5 | Charge-Discharge Cycle Testing | 4 |
| 1.6 | Battery Pack Capacity and Protection Analysis | 4 |

**Total:** 6 labs, 24 Session Outcomes

---

### Module 2: Motor & Drivetrain Systems (Days 7-16)
**Equipment:** Setup 4 (Hydraulic Dyno), Setup 7 (4W Drivetrain MIDC)

| Lab | Name | SOs |
|-----|------|-----|
| 2.1 | Motor Mounting and Mechanical Setup | 4 |
| 2.2 | Motor Controller Configuration | 4 |
| 2.3 | Motor Performance Testing with Hydraulic Dyno | 4 |
| 2.4 | CAN Communication and Data Logging | 4 |
| 2.5 | Field-Oriented Control (FOC) Implementation | 4 |
| 2.6 | Motor Control Tuning and Optimization | 4 |
| 2.7 | 4-Wheeler Drivetrain Integration | 4 |
| 2.8 | MIDC Driving Cycle Simulation | 4 |
| 2.9 | Regenerative Braking Analysis | 4 |
| 2.10 | Drivetrain Fault Diagnosis | 4 |

**Total:** 10 labs, 40 Session Outcomes

---

### Module 3: Charging Infrastructure (Days 17-25)
**Equipment:** Setup 6 (EV Charging Simulator CCS2)

9 labs covering:
- CCS2 protocol fundamentals
- Message exchange simulation
- Error handling
- Security (TLS)
- Grid load flow analysis
- Harmonic analysis
- Protection systems
- Smart charging
- Renewable integration

**Total:** 9 labs, 36 Session Outcomes

---

### Module 4: Vehicle Control Systems (Days 26-37)
**Equipment:** Setup 5 (VCU Developer), Setup 9 (Hybrid Platform)

12 labs covering:
- VCU hardware and interfaces
- Embedded C programming
- MATLAB/Simulink development
- HIL testing
- Functional safety
- Hybrid vehicle control strategies
- Mode switching
- Energy management

**Total:** 12 labs, 48 Session Outcomes

---

### Module 5: Complete Vehicle Integration (Days 38-54)
**Equipment:** Setup 8 (2W Assembly), Setup 10 (Research EV Car)

17 labs covering:
- 2-wheeler assembly/disassembly
- Safety and tool usage
- Research EV platform
- FOC algorithm implementation
- BMS-motor integration
- Power electronics
- Charging control
- HMI development
- Performance testing
- On-road validation

**Total:** 17 labs, 68 Session Outcomes

---

## Course Outcomes (COs)

1. **NEVLAB-CO-1:** Design, assemble, and test lithium-ion battery pack systems with integrated BMS
2. **NEVLAB-CO-2:** Configure, test, and optimize electric motor control systems and analyze drivetrain performance
3. **NEVLAB-CO-3:** Analyze EV charging protocols, simulate charging scenarios, and evaluate grid impact
4. **NEVLAB-CO-4:** Develop, program, and validate VCU algorithms for electric and hybrid vehicles
5. **NEVLAB-CO-5:** Integrate complete EV systems, perform diagnostics, and troubleshoot powertrains

---

## Excel Template Structure

The generated Excel file (`03-template-partial.xlsx`) contains:

### Sheet 1: Course_Info
- Course Name
- Course Code: NEVLAB
- Duration: 60 days
- Description
- Organization ID (needs to be updated by you)

### Sheet 2: Outcomes_And_Structure
Currently includes:
- **Module 1 (Complete):** All 6 labs with 24 Session Outcomes fully populated
- **Module 2 (Partial):** 4 representative labs to show the pattern

**Format follows the "inherit from above" pattern:**
- Empty cells inherit values from the row above
- Each Session Outcome (SO) creates a new row
- Module and Lesson information is inherited for subsequent SOs

---

## Using the Template

### Current Status
The template demonstrates:
✓ Proper hierarchy structure (CO → MO → SO)
✓ Correct ID naming (co-1, mo-1-1, so-1-1-1)
✓ Correct Code naming (NEVLAB-CO-1, NEVLAB-MO-1-1, NEVLAB-SO-1-1-1)
✓ Bloom's taxonomy levels appropriate for skills
✓ Session type (all labs)
✓ "Inherit from above" pattern

### To Complete the Template
To create the full template with all 54 labs:

1. **Open the Excel file:** `03-template-partial.xlsx`

2. **Update Organization ID:**
   - Go to Course_Info sheet
   - Replace `INSERT-YOUR-ORG-UUID-HERE` with your actual organization UUID

3. **Expand Module 2:**
   - Add remaining labs (2.2, 2.4-2.6, 2.8-2.10)
   - Follow the same pattern as shown

4. **Add Modules 3, 4, 5:**
   - Use `02-course-structure.md` as the source for all labs and SOs
   - Follow the same "inherit from above" pattern
   - Each new module starts with all columns filled
   - Each new lesson within a module inherits module info but fills lesson columns
   - Each new SO inherits lesson/module/MO info but fills SO columns

---

## Key Files for Reference

### For Learning Outcomes Details
📄 **`02-course-structure.md`**
Contains the complete specification of all 54 labs with:
- All 5 Course Outcomes with full descriptions
- All 15 Module Outcomes mapped to appropriate COs
- All 68 Session Outcomes with detailed descriptions
- Bloom's taxonomy levels for each outcome
- Category assignments (Knowledge/Skill/Attitude)

### For Equipment Mapping
📄 **`00-requirements.md`**
Contains:
- All 10 equipment setups with specifications
- Possible experiments for each equipment
- Equipment-to-module mapping

### For Template Format
📄 **`/Users/mmsk/.claude/skills/course-design-skill/references/TEMPLATE_GUIDE.md`**
Official guide explaining:
- Excel sheet structure
- "Inherit from above" pattern
- ID and Code naming conventions
- Valid values for all fields
- Common mistakes to avoid

---

## Statistics

| Metric | Count |
|--------|-------|
| Course Outcomes | 5 |
| Module Outcomes | 15 |
| Session Outcomes | 68 |
| Total Modules | 5 |
| Total Labs | 54 |
| Equipment Setups | 10 |
| Duration (Days) | 60 |

---

## Next Steps

1. **Review the Excel template** (`03-template-partial.xlsx`)
   - Verify Module 1 structure looks correct
   - Understand the "inherit from above" pattern from examples

2. **Review learning outcomes** (`02-course-structure.md`)
   - Check if all SOs align with equipment capabilities
   - Verify Bloom's levels are appropriate
   - Adjust any descriptions as needed

3. **Update Organization ID** in Course_Info sheet

4. **Decide:**
   - **Option A:** I can generate the complete Excel with all 54 labs (will be a larger file)
   - **Option B:** Use the partial template as a guide and complete it manually
   - **Option C:** Adjust any learning outcomes first, then generate complete template

---

## Questions?

- Need to modify any learning outcomes?
- Want to change the module sequencing?
- Need to adjust Bloom's taxonomy levels?
- Want me to generate the complete Excel with all modules?

Let me know how you'd like to proceed!
