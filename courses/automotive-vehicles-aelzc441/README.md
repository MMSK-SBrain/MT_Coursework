# Automotive Vehicles (AELZC441) - Learning Outcomes Documentation

**Course:** Automotive Vehicles
**Code:** AEL ZC441
**Institution:** BITS Pilani - M.Tech. Automotive Electronics
**Generated:** 2026-01-03
**Approach:** Physics & Math Foundation First (for students with NO automotive background)

---

## 📋 Overview

This folder contains complete learning outcomes documentation for the Automotive Vehicles course, **revised with a pedagogical approach that builds confidence through familiar physics and mathematics before introducing complex automotive systems**.

### **Key Innovation: Foundation-First Approach**

Traditional automotive courses start with vehicle architecture and dive into thermodynamics. This revised approach:
- **Starts with familiar physics** (forces, friction, power calculations)
- **Builds confidence** with math-heavy problem-solving (Sessions 1-3)
- **Introduces engines simply** (no thermodynamics initially)
- **Places tires early** (Session 2) as foundation for all dynamics
- **Groups related topics** (cooling/lubrication right after engines)

---

## 📁 Files in This Folder

### **Active Files (4):**

| File | Purpose | Size |
|------|---------|------|
| **course-data.yaml** | Single source of truth - All learning outcomes (CO→MO→SO) | 47 KB |
| **README.md** | Complete documentation and usage guide | 12 KB |
| **requirements.md** | Course requirements, pedagogical approach, target audience | 14 KB |
| **course-structure.md** | Detailed structure with all 120 Session Outcomes by module | 30 KB |

### **Archive Folder:**

All historical files moved to `archive/` subdirectory for reference:
- Original course files (pre-revision)
- Previous YAML and Excel templates
- Proposal and checklist documents

### **Lecture Frameworks Folder:**

Professional instructor-led story frameworks for PPT preparation in `lecture-frameworks/`:
- **SESSION-01-Forces-Framework.md** - Complete framework for Session 1
- **SESSION-02-Tires-Framework.md** - Complete framework for Session 2
- **SESSION-03-Power-Framework.md** - Complete framework for Session 3
- **TEMPLATE-Session-Framework.md** - Universal template for Sessions 4-20
- **README.md** - Complete guide to using frameworks

These frameworks provide:
- ✅ Professional teacher-led narratives for all 20 sessions
- ✅ Slide-by-slide PPT preparation guidance
- ✅ Technical content with engaging delivery structure
- ✅ Balance of storytelling and engineering rigor

### **Common Scripts:**

Python conversion scripts moved to `/Volumes/Dev/Course_Generator/scripts/`:
- **yaml_to_excel.py** - Generic YAML to Excel converter (works for any course)
- **archive/** - Previous course-specific conversion scripts

---

## 🎯 Course Structure Summary

### **Total Content:**
- **4 Course Outcomes (CO)**
- **6 Module Outcomes (MO)**
- **120 Session Outcomes (SO)** - 6 per session
- **20 Sessions** × 2 hours = 40 contact hours

### **Bloom's Taxonomy Distribution:**

| Level | Count | % | Notes |
|-------|-------|---|-------|
| **Remember** | 10 | 8.3% | Basic definitions, classifications |
| **Understand** | 68 | 56.7% | Primary focus - explanations, comparisons |
| **Apply** | 34 | **28.3%** ⭐ | **Much higher than traditional** - calculations, problem-solving |
| **Analyze** | 8 | 6.7% | System analysis, trade-offs |
| **Evaluate** | 0 | 0% | N/A for this course |
| **Create** | 0 | 0% | N/A for this course |

### **Category Distribution:**

| Category | Count | % |
|----------|-------|---|
| Knowledge | 76 | 63.3% |
| Skill | 44 | 36.7% |
| Attitude | 0 | 0% |

### **Session Types:**

| Type | Count | % |
|------|-------|---|
| Lecture | 88 | 73.3% |
| Numerical (Lecture + Problems) | 32 | 26.7% |

---

## 📚 Module Breakdown

### **Module 1: Vehicle Motion Fundamentals (Sessions 1-3)** ⭐ NEW!

**Philosophy:** Build confidence with familiar physics and math

- **Session 1:** Forces Acting on a Moving Vehicle
  - Newton's laws, resistance forces, performance metrics
  - Heavy calculation focus

- **Session 2:** Tires & Friction Fundamentals
  - Tire construction, friction principles, friction circle
  - Foundation for all future dynamics

- **Session 3:** From Forces to Power Requirements
  - Force → Torque → Power calculations
  - Performance calculations (acceleration, gradeability, top speed)
  - **Transition:** "Now we know HOW MUCH power. Next: HOW to generate it?"

---

### **Module 2: Powertrain Systems (Sessions 4-8)**

**Philosophy:** Simplified introduction, support systems immediately after

- **Session 4:** Introduction to IC Engines (Simplified)
  - Engine as torque generator (NO thermodynamics!)
  - Basic mechanical components

- **Session 5:** Engine Support - Cooling & Lubrication ⭐ RIGHT AFTER ENGINES
  - Why cooling/lubrication needed
  - System components and operation

- **Session 6:** Engine Performance & Fuel Systems
  - Performance maps, fuel delivery
  - Basic emissions overview

- **Session 7-8:** Transmission Systems
  - Gear ratios, manual/automatic transmissions
  - Differential, final drive
  - Brief intro to electric powertrains

---

### **Module 3: Chassis Dynamics & Control (Sessions 9-12)** ⭐ MATH-HEAVY

**Philosophy:** Apply Sessions 1-3 foundation to chassis systems

- **Session 9:** Vehicle Dynamics Fundamentals
  - Longitudinal dynamics, load transfer calculations

- **Session 10:** Braking Systems
  - Friction calculations, stopping distance
  - Hydraulic systems, ABS

- **Session 11:** Steering Systems
  - Ackermann geometry, turning radius calculations
  - Power steering

- **Session 12:** Suspension Systems
  - Spring-mass-damper physics
  - Suspension types and trade-offs

---

### **Module 4: Electrical & Control (Sessions 13-15)**

- **Session 13:** Electrical Architecture
- **Session 14:** Vehicle Control Systems (ECU, sensors, actuators)
- **Session 15:** Communication Networks (CAN, LIN, OBD-II)

---

### **Module 5: Architecture & Comfort (Sessions 16-18)**

- **Session 16:** Chassis & Body Architecture
- **Session 17:** HVAC Systems (thermodynamics introduced HERE)
- **Session 18:** Passive Safety Systems

---

### **Module 6: Active Safety & Future (Sessions 19-20)**

- **Session 19:** Active Safety & Vehicle Stability (ESC, TCS)
- **Session 20:** Introduction to ADAS & Future Mobility (brief overview only)

---

## 🔑 Key Pedagogical Decisions

### **1. Foundation-First Approach**

**Problem:** Students with no automotive background feel overwhelmed by complex systems

**Solution:** Start with physics they already know
- Session 1: Basic force calculations
- Session 2: Friction (foundation for everything)
- Session 3: Power requirements (sets up engine discussion)

### **2. Simplified Engine Introduction**

**Problem:** Thermodynamics in Session 4 is intimidating

**Solution:** Introduce engine as "torque-generating device"
- Focus on mechanical function first
- Thermodynamics only appears in Session 17 (HVAC - refrigeration cycle)

### **3. Early Tire Introduction**

**Problem:** Tires are critical to dynamics, braking, steering, but often taught late

**Solution:** Dedicated tire session (Session 2)
- Provides foundation for Sessions 9-12 (dynamics/chassis)
- Students understand friction before learning braking/steering

### **4. Logical Topic Grouping**

**Problem:** Cooling/lubrication separated from engines breaks learning flow

**Solution:** Session 5 immediately follows engine introduction
- "You learned engines generate heat → Now learn how to cool them"
- "You learned moving parts → Now learn how to lubricate them"

### **5. Math-Heavy Clusters**

**Problem:** Math scattered throughout doesn't build problem-solving confidence

**Solution:** Heavy numerical focus in:
- Sessions 1-3 (foundation calculations)
- Sessions 9-12 (chassis dynamics calculations)
- Total: 32 numerical outcomes (26.7%)

---

## 🎓 Target Audience

### **Student Profile:**

✅ **M.Tech. Automotive Electronics students**
✅ **NO automotive background assumed**
✅ **NO mechanical engineering background assumed**
✅ **May come from electronics/software/electrical engineering**

### **Prerequisites Required:**

- Basic physics (Newton's laws, forces, friction)
- Basic mathematics (algebra, trigonometry, basic calculus)
- Basic electrical knowledge (circuits)
- **NO thermodynamics required initially**

### **Job Roles After Course:**

- Automotive Electronics Engineer
- Vehicle Control Systems Engineer
- ADAS/Autonomous Vehicle Engineer
- Powertrain Systems Engineer

---

## 📊 Assessment Strategy

| Type | Weight | Focus |
|------|--------|-------|
| Quiz | 10% | Basic calculations (forces, torque, power, ratios) |
| Assignment | 20% | Vehicle performance calculations, system analysis |
| Mid-term | 30% | Modules 1-3 (Foundation + Powertrain + Dynamics) |
| Final | 40% | All modules (comprehensive) |

**Assessment Distribution:**
- 40% Numerical problems and calculations
- 40% Conceptual understanding
- 20% System analysis and trade-offs

---

## 🚀 How to Use These Files

### **For Instructors:**

1. **Start with `requirements.md`**
   - Understand pedagogical approach
   - Review target audience (NO automotive background)
   - Review module structure and sequencing

2. **Review `course-structure.md`**
   - See all 120 Session Outcomes
   - Understand progression within each module
   - Note which sessions are math-heavy

3. **Generate Excel template when needed:**
   ```bash
   python scripts/yaml_to_excel.py courses/automotive-vehicles-aelzc441/course-data.yaml
   ```
   - Use generated `course-template.xlsx` for LMS import
   - Share with students or for syllabus creation

4. **Keep `course-data.yaml` as master**
   - Single source of truth
   - Human-readable, easy to edit
   - Regenerate Excel after any changes

### **For Curriculum Designers:**

1. **Review historical changes:**
   - Check `archive/` folder for original files
   - Compare original vs revised approaches

2. **Adapt for your context:**
   - Edit `course-data.yaml` to modify outcomes
   - Regenerate Excel using generic script
   - Adjust module durations as needed

### **For Students:**

1. **Review `course-structure.md`**
   - See what you'll learn session-by-session
   - Understand progression (easy → complex)
   - Note math-heavy sessions for extra preparation

---

## 🔄 Updating Learning Outcomes

If you need to modify outcomes:

1. **Edit the YAML file:**
   ```bash
   cd /Volumes/Dev/Course_Generator
   vi courses/automotive-vehicles-aelzc441/course-data.yaml
   ```

2. **Regenerate Excel template:**
   ```bash
   python scripts/yaml_to_excel.py courses/automotive-vehicles-aelzc441/course-data.yaml
   ```
   Output: `courses/automotive-vehicles-aelzc441/course-template.xlsx`

3. **Review changes:**
   - Check Excel file for correctness
   - Update `course-structure.md` if needed

---

## 📈 Course Progression Philosophy

```
WHY? (Sessions 1-3)
  ↓ "Why do vehicles need power?"
  ↓ Physics and math calculations

HOW? (Sessions 4-8)
  ↓ "How do we generate that power?"
  ↓ Engines and transmissions (simplified)

CONTROL? (Sessions 9-12)
  ↓ "How do we control vehicle motion?"
  ↓ Dynamics, braking, steering, suspension (math-based)

MANAGE? (Sessions 13-15)
  ↓ "How do we manage systems electronically?"
  ↓ Electrical architecture and control

INTEGRATE? (Sessions 16-20)
  ↓ "How does everything work together?"
  ↓ Complete vehicle + safety + future
```

---

## ✅ Validation Checklist

Before delivering this course, ensure:

- [ ] Students have basic physics background (forces, friction, rotational motion)
- [ ] Students have basic math skills (algebra, trigonometry)
- [ ] Numerical problem sets prepared for Sessions 1-3, 9-12
- [ ] Sample calculations ready for every math-heavy session
- [ ] Real vehicle data available (mass, Cd, tire specs, gear ratios)
- [ ] Visual aids prepared (force diagrams, free-body diagrams, torque curves)

---

## 📞 Contact & Support

- **Instructor:** Sajeeth Kumar
- **Institution:** BITS Pilani - Work Integrated Learning Programmes
- **Course Code:** AEL ZC441
- **Generated using:** Claude Code course-design-skill

---

## 📝 Version History

| Date | Version | Changes |
|------|---------|---------|
| 2026-01-03 | 1.0 (Original) | Traditional automotive course structure |
| 2026-01-03 | 2.0 (REVISED) | Physics/math foundation-first approach for students with NO automotive background |
| 2026-01-03 | 2.1 (Cleanup) | Folder restructure: Clean naming, common scripts, archive old files |

---

**Status:** ✅ COMPLETE - Ready for delivery
**Approach:** Physics & Math Foundation First
**Target:** Students with NO automotive/mechanical background
**Structure:** Clean folder with 4 active files + archive
