# Session 7: Transmission Systems - Part 1
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 90 minutes lecture + 30 minutes Q&A
**Approach:** Teacher-Led Narrative (Technical/Math-Focused)
**PPT Target:** 28-30 slides

---

## 🎯 Session Objectives (For Instructor)

By the end of this session, students will be able to:
- **AELZC441-SO-2-7-1:** Explain the need for transmission in matching engine output characteristics to wheel torque requirements
- **AELZC441-SO-2-7-2:** Calculate gear ratios and analyze their effect on torque multiplication and speed reduction
- **AELZC441-SO-2-7-3:** Describe clutch operation (single-plate, multi-plate) and explain engagement/disengagement mechanism
- **AELZC441-SO-2-7-4:** Explain manual gearbox construction (constant mesh, synchromesh) and gear shifting mechanism
- **AELZC441-SO-2-7-5:** Design basic transmission gear ratios for given vehicle performance requirements (acceleration vs top speed)
- **AELZC441-SO-2-7-6:** Analyze power flow through a manual transmission from engine to output shaft

---

## 📖 INSTRUCTOR-LED STORY ARC

### **SETUP: Opening Hook** (Slides 1-5, ~10 minutes)

#### Slide 1: Title
**Visual:** Professional title slide with cutaway of manual gearbox showing gears
**Instructor Script:**
> "Welcome to Session 7. Today we answer a critical question: Why can't we connect the engine directly to the wheels? Why do we need this complex device called a transmission?"

#### Slide 2: The Problem - Engine vs Wheel Requirements
**Visual:** Split diagram: Engine torque curve vs Wheel torque requirement
**Instructor Script:**
> "Let me show you the fundamental mismatch between what engines produce and what wheels need:
>
> **ENGINE CHARACTERISTICS** (from Sessions 4-6):
> - Operates from ~800 RPM (idle) to ~6000 RPM (redline)
> - Peak torque at ~4000 RPM (let's say 150 Nm)
> - Can't produce significant torque below ~1500 RPM
> - **Problem:** Needs to be spinning to make torque!
>
> **WHEEL REQUIREMENTS:**
> - At standstill: Need MAXIMUM torque to overcome inertia
> - At 120 km/h: Wheels spinning at ~800 RPM
> - At 20 km/h: Wheels spinning at ~130 RPM
> - **Problem:** Wheels need high torque at low speeds, low torque at high speeds
>
> **The mismatch:** Engine makes power at high RPM, but vehicle needs torque at low wheel speeds.
>
> **Solution:** A transmission – a mechanical device that multiplies torque and changes speed ratios."

#### Slide 3: Real-World Demonstration
**Visual:** Graph showing vehicle speed vs engine RPM in different gears
**Instructor Script:**
> "Let me illustrate with a real car – Honda Civic:
>
> **Accelerating from 0-100 km/h:**
>
> **WITHOUT transmission** (impossible, but hypothetically):
> - At 0 km/h: Engine at 0 RPM → No torque → Car doesn't move!
> - To move: Need to keep engine at 4000 RPM while wheels at 0 RPM → Impossible!
>
> **WITH 6-speed transmission:**
> - **0-20 km/h:** 1st gear → Engine at 3000 RPM → Wheels at 130 RPM → High torque
> - **20-40 km/h:** 2nd gear → Engine at 3000 RPM → Wheels at 260 RPM → Good torque
> - **40-60 km/h:** 3rd gear → Engine at 3000 RPM → Wheels at 390 RPM
> - **60-80 km/h:** 4th gear → Engine at 2800 RPM → Wheels at 520 RPM
> - **80-100 km/h:** 5th gear → Engine at 2600 RPM → Wheels at 650 RPM
>
> **See the pattern?** Engine stays in optimal RPM range (2500-4000), while wheels continuously accelerate. That's what transmission does!"

#### Slide 4: Connection to Session 6 (BSFC Maps)
**Visual:** BSFC map with gear shift points annotated
**Instructor Script:**
> "Remember in Session 6 we learned about BSFC maps? We found the 'optimal efficiency island' at 2000-3000 RPM, medium-high load.
>
> **Here's the connection:**
> Without a transmission, you can't stay in that optimal zone. The transmission lets you choose the right gear to:
> - Keep engine RPM in efficient range
> - Match torque requirement at wheels
> - Maximize fuel economy OR maximize acceleration (depending on your goal)
>
> **Modern transmissions (6, 7, 8 speeds):** More gears = more opportunities to stay in optimal BSFC zone.
>
> Today you'll learn how these gears work and how to calculate the ratios."

#### Slide 5: Learning Path for Today
**Visual:** Roadmap showing 4 main topics
**Instructor Script:**
> "Today's journey through manual transmission systems:
>
> **Part 1: WHY WE NEED TRANSMISSION** (~10 min)
> - Torque multiplication principle
> - Speed reduction vs torque multiplication trade-off
>
> **Part 2: GEAR RATIO MATHEMATICS** (~20 min) [Math-heavy!]
> - Calculating gear ratios
> - Torque and speed relationships
> - Overall transmission ratio
>
> **Part 3: CLUTCH SYSTEM** (~15 min)
> - How to disconnect engine from wheels (why needed)
> - Clutch construction and operation
>
> **Part 4: MANUAL GEARBOX INTERNALS** (~20 min)
> - Gear arrangement (constant mesh, synchromesh)
> - Power flow through transmission
> - Gear shifting mechanism
>
> By the end, you'll be able to design transmission ratios for a vehicle!"

---

### **TRIGGER: The Challenge** (Slides 6-7, ~5 minutes)

#### Slide 6: Real-World Scenario
**Visual:** Two vehicle requirements side-by-side
**Instructor Script:**
> "Here's a real engineering challenge:
>
> **Vehicle:** Light commercial vehicle (think Tata Ace)
> - **Engine:** 700 cc, peak torque 38 Nm @ 4500 RPM
> - **Vehicle mass:** 900 kg (loaded)
> - **Wheel radius:** 0.28 m
>
> **Requirements:**
> 1. Must be able to climb 20° slope from standstill (loaded)
> 2. Must reach 80 km/h top speed on flat road
>
> **Questions:**
> - What torque do we need at wheels to climb 20° slope?
> - What gear ratio do we need in 1st gear?
> - What gear ratio do we need in top gear (5th)?
> - How many intermediate gears and what ratios?
>
> **By the end of today:** You'll solve this problem completely."

#### Slide 7: Today's Learning Goals
**Visual:** Three skill targets
**Instructor Script:**
> "By the end of this session, you'll master three critical skills:
>
> **Skill 1: CALCULATE GEAR RATIOS**
> - Given input/output speeds or teeth numbers
> - Understand torque multiplication and speed reduction
>
> **Skill 2: ANALYZE TRANSMISSION REQUIREMENTS**
> - Determine 1st gear ratio from vehicle performance needs (hill climbing)
> - Determine top gear ratio from maximum speed requirement
> - Design intermediate gear ratios
>
> **Skill 3: TRACE POWER FLOW**
> - Understand how power flows through transmission in each gear
> - Explain which gears are engaged, which freewheel
>
> Let's start with the fundamentals."

---

### **RISING ACTION: Building Understanding** (Slides 8-24, ~52 minutes)

#### **Part 1: Torque Multiplication Fundamentals** (Slides 8-11, ~12 minutes)

##### Slide 8: The Simple Gear Pair
**Visual:** Two meshing gears - small driving large
**Instructor Script:**
> "Let's start with the simplest transmission: Two gears meshing together.
>
> **Setup:**
> - **Driver gear (input):** 20 teeth, connected to engine
> - **Driven gear (output):** 60 teeth, connected to wheels
>
> **When driver rotates 1 revolution:**
> - Driver gear: 20 teeth pass through mesh
> - Driven gear: Receives 20 teeth → Rotates 20/60 = 0.333 revolutions
>
> **Speed relationship:**
> - If driver spins at 3000 RPM
> - Driven spins at 3000 × (20/60) = **1000 RPM**
>
> **We've achieved speed reduction of 3:1 (or gear ratio = 3.0).**"

##### Slide 9: Where Did the 'Lost' Speed Go? (Torque Multiplication!)
**Visual:** Diagram showing speed-torque trade-off
**Instructor Script:**
> "Here's the beautiful principle: **Energy is conserved (ignoring friction).**
>
> **Power in = Power out**
>
> Remember from Session 3: **Power = Torque × Angular velocity**
> P = τ × ω
>
> **At input (driver gear):**
> - Torque: τ_in = 50 Nm (from engine)
> - Speed: ω_in = 3000 RPM
> - Power: P_in = 50 × 3000 = 150,000 units
>
> **At output (driven gear):**
> - Speed: ω_out = 1000 RPM (we reduced it by 3x)
> - Power: P_out = P_in = 150,000 units (conserved!)
> - **Torque: τ_out = P / ω = 150,000 / 1000 = 150 Nm**
>
> **Torque multiplied by 3x!** (from 50 Nm to 150 Nm)
>
> **The Rule:**
> - Gear ratio 3:1 → Speed reduction 3x → Torque multiplication 3x
> - **τ_out = τ_in × Gear Ratio**
> - **ω_out = ω_in / Gear Ratio**"

##### Slide 10: Defining Gear Ratio Mathematically
**Visual:** Formula with labeled diagram
**Instructor Script:**
> "Let's formalize the math:
>
> **GEAR RATIO (GR) = ω_in / ω_out = N_driven / N_driver**
>
> Where:
> - ω_in = Input speed (RPM)
> - ω_out = Output speed (RPM)
> - N_driven = Number of teeth on driven gear
> - N_driver = Number of teeth on driver gear
>
> **For our example:**
> GR = 60 teeth / 20 teeth = **3.0**
>
> **Relationships:**
> - **Speed:** ω_out = ω_in / GR
> - **Torque:** τ_out = τ_in × GR × η (where η = efficiency, ~0.95-0.98 for gears)
>
> **Key insight:** Higher gear ratio = More torque, Less speed (good for acceleration, hill climbing).
> Lower gear ratio = Less torque, More speed (good for cruising, top speed)."

##### Slide 11: Example Calculation
**Visual:** Worked example with numbers
**Instructor Script:**
> "Let's practice with a real example:
>
> **Given:**
> - Engine speed: 4000 RPM
> - Engine torque: 120 Nm
> - Driver gear: 18 teeth
> - Driven gear: 54 teeth
>
> **Find:** Output speed and torque
>
> **Solution:**
>
> **Step 1:** Calculate Gear Ratio
> GR = N_driven / N_driver = 54 / 18 = **3.0**
>
> **Step 2:** Calculate Output Speed
> ω_out = ω_in / GR = 4000 / 3.0 = **1333 RPM**
>
> **Step 3:** Calculate Output Torque (assuming η = 0.96)
> τ_out = τ_in × GR × η = 120 × 3.0 × 0.96 = **345.6 Nm**
>
> **Result:** We've tripled the torque (120 → 346 Nm) while reducing speed to 1/3."

---

#### **Part 2: Transmission System Calculations** (Slides 12-16, ~18 minutes)

##### Slide 12: Complete Transmission Chain
**Visual:** Diagram showing engine → clutch → gearbox → differential → wheels
**Instructor Script:**
> "A real vehicle transmission has multiple stages:
>
> **Power flow:**
>
> **1. ENGINE** → Torque: τ_engine, Speed: ω_engine
>
> **2. CLUTCH** → (When engaged, just passes power through)
>
> **3. GEARBOX** → Gear ratio: GR_gearbox (e.g., 3.5 in 1st gear)
>    - Speed: ω_gearbox_out = ω_engine / GR_gearbox
>    - Torque: τ_gearbox_out = τ_engine × GR_gearbox
>
> **4. DIFFERENTIAL** → Gear ratio: GR_diff (typically 3.5 to 4.5)
>    - Speed: ω_wheel = ω_gearbox_out / GR_diff
>    - Torque: τ_wheel = τ_gearbox_out × GR_diff
>
> **5. WHEELS** → Convert torque to force: F = τ_wheel / r_wheel
>
> **Overall Ratio = GR_gearbox × GR_diff**
>
> Let's calculate a complete example!"

##### Slide 13: Complete Example - 1st Gear Acceleration
**Visual:** Step-by-step calculation with diagrams
**Instructor Script:**
> "**Scenario:** Honda Civic accelerating in 1st gear
>
> **Given:**
> - Engine torque: 145 Nm @ 4000 RPM
> - 1st gear ratio: 3.6
> - Differential ratio: 4.1
> - Wheel radius: 0.32 m
> - Transmission efficiency: 94%
>
> **Find:** Force at road from one wheel (assuming 2WD, power to 2 wheels)
>
> **Solution:**
>
> **Step 1:** Torque after gearbox
> τ_gearbox = 145 × 3.6 = 522 Nm
>
> **Step 2:** Torque after differential
> τ_diff = 522 × 4.1 = 2,140 Nm
>
> **Step 3:** Torque per wheel (power to 2 wheels)
> τ_wheel = 2,140 / 2 = 1,070 Nm per wheel
>
> **Step 4:** Apply efficiency
> τ_wheel_actual = 1,070 × 0.94 = **1,006 Nm per wheel**
>
> **Step 5:** Force at road
> F = τ_wheel / r_wheel = 1,006 / 0.32 = **3,144 N per wheel**
>
> **Total force (both drive wheels): ~6,300 N**
>
> **That's enough to accelerate a 1,300 kg car at ~4.8 m/s²!** (Good acceleration)"

##### Slide 14: Practice Problem - You Try It!
**Visual:** Problem statement with space for solution
**Instructor Script:**
> "Your turn! Try this:
>
> **Given:**
> - Engine: 2000 RPM, 180 Nm torque
> - Transmission in 3rd gear, ratio = 1.8
> - Differential ratio = 4.3
> - Wheel radius = 0.30 m
> - Efficiency = 95%
>
> **Calculate:**
> 1. Wheel RPM
> 2. Torque per wheel (assume 2WD)
> 3. Force at road per wheel
>
> **Take 2 minutes. I'll show the solution after.**
>
> [Pause for student work]
>
> **Solution:**
> 1. Wheel RPM = 2000 / (1.8 × 4.3) = **258 RPM**
> 2. Torque per wheel = 180 × 1.8 × 4.3 × 0.95 / 2 = **660 Nm**
> 3. Force per wheel = 660 / 0.30 = **2,200 N**"

##### Slide 15: Designing Transmission Ratios - Requirements
**Visual:** Vehicle performance requirements mapped to gear ratios
**Instructor Script:**
> "Now let's flip the problem: HOW to choose gear ratios?
>
> **Two constraints define the extremes:**
>
> **CONSTRAINT 1: Hill Climbing (determines 1st gear)**
> - Must produce enough wheel torque to climb steepest slope
> - Calculation: F_required = m × g × sin(θ) + Rolling resistance + Drag
> - Work backwards: F → τ_wheel → τ_engine × Ratios
> - This gives **MINIMUM 1st gear ratio**
>
> **CONSTRAINT 2: Top Speed (determines final gear)**
> - At top speed, engine at redline (e.g., 6500 RPM)
> - Wheel speed must match top speed requirement
> - Calculation: ω_wheel = v_max / r_wheel
> - This gives **MAXIMUM top gear ratio** (actually minimum value, around 0.7-1.0)
>
> **Intermediate gears:** Spaced between these extremes to keep engine in optimal RPM range.
>
> Let's work through real design example..."

##### Slide 16: Design Example - Small Commercial Vehicle
**Visual:** Complete worked design example
**Instructor Script:**
> "**Design Challenge:** (Remember from Slide 6?)
>
> **Vehicle:** 900 kg, wheel radius 0.28 m
> **Engine:** 38 Nm @ 4500 RPM (peak torque)
> **Differential ratio:** 5.0 (typical for commercial vehicle)
> **Requirements:** Climb 20° slope, 80 km/h top speed
>
> **DESIGNING 1st GEAR:**
>
> **Force needed to climb 20° slope:**
> F = m × g × sin(20°) + F_rolling
> F = 900 × 9.81 × 0.342 + (900 × 9.81 × 0.02)
> F ≈ 3,020 + 177 = **3,200 N**
>
> **Torque needed at wheels (both drive wheels):**
> τ_wheel = F × r_wheel = 3,200 × 0.28 = **896 Nm**
>
> **Working backwards to find 1st gear ratio:**
> τ_wheel = τ_engine × GR_1st × GR_diff × η
> 896 = 38 × GR_1st × 5.0 × 0.94
> GR_1st = 896 / (38 × 5.0 × 0.94) = **5.0**
>
> **DESIGNING 5th GEAR (top gear):**
>
> **Top speed = 80 km/h = 22.2 m/s**
> **Wheel RPM at top speed:** ω_wheel = v / (2πr) = 22.2 / (2π × 0.28) = **12.6 rev/s = 757 RPM**
>
> **Engine at redline: 6000 RPM**
> **Overall ratio needed:** GR_overall = 6000 / 757 = 7.93
>
> **Since differential = 5.0:**
> GR_5th = 7.93 / 5.0 = **1.59**
>
> **Summary:**
> - 1st gear: 5.0 (for hill climbing)
> - 5th gear: 1.59 (for top speed)
> - Intermediate gears (2nd, 3rd, 4th): Geometrically spaced → ~3.5, ~2.5, ~2.0
>
> **You've just designed a transmission!**"

---

#### **Part 3: Clutch System** (Slides 17-19, ~10 minutes)

##### Slide 17: Why Do We Need a Clutch?
**Visual:** Diagram showing need to disconnect engine from wheels
**Instructor Script:**
> "Before we look inside the gearbox, we need to understand the CLUTCH.
>
> **The problem:** Engine must keep running (~800 RPM idle) even when vehicle is stopped (wheels at 0 RPM).
>
> **Without clutch:**
> - Stop vehicle → Wheels stop → Transmission locked → Engine forced to stop → Engine stalls
> - To start moving: Can't shift gears while engine running (gears spinning at different speeds would clash!)
>
> **Clutch solution:** Temporary disconnection device between engine and transmission
> - Allows engine to run while vehicle stopped
> - Allows gear shifting (disconnect, shift, reconnect)
> - Allows smooth engagement (gradually connect engine to wheels)
>
> **Operation:**
> - **Clutch engaged** (pedal released): Engine connected to transmission → Power flows
> - **Clutch disengaged** (pedal pressed): Engine disconnected → Engine free, wheels free"

##### Slide 18: Single-Plate Clutch Construction
**Visual:** Cutaway of single-plate clutch with all components labeled
**Instructor Script:**
> "**SINGLE-PLATE CLUTCH** (most common in cars)
>
> **Key Components:**
>
> **1. Flywheel:**
> - Attached to engine crankshaft (always rotating with engine)
> - Heavy disc, smooths engine power pulses
> - Provides friction surface
>
> **2. Clutch Disc (Friction Disc):**
> - Friction material both sides (like brake pads)
> - Splined hub connects to transmission input shaft
> - Can slide on splines but rotates with input shaft
>
> **3. Pressure Plate:**
> - Spring-loaded plate that presses clutch disc against flywheel
> - Provides clamping force via diaphragm spring
>
> **4. Release Bearing:**
> - Pushes on diaphragm spring when clutch pedal pressed
> - Releases clamping force
>
> **OPERATION:**
>
> **Engaged (pedal released):**
> - Diaphragm spring pushes pressure plate
> - Clutch disc clamped between flywheel and pressure plate
> - **Friction connects engine to transmission** → Power flows
>
> **Disengaged (pedal pressed):**
> - Release bearing pushes diaphragm spring center inward
> - Pressure plate pulls back
> - Clutch disc free → **Engine and transmission disconnected**"

##### Slide 19: Clutch Engagement - The Friction Zone
**Visual:** Graph showing torque capacity vs pedal position
**Instructor Script:**
> "**The 'biting point' or 'friction zone':**
>
> When you slowly release clutch pedal:
> - **Fully pressed:** No contact → 0% torque transfer
> - **Friction zone (~20-40% release):** Partial contact → 20-80% torque transfer (slipping)
> - **Fully released:** Full clamping → 100% torque transfer (locked)
>
> **Why slipping is useful:**
> - Starting from standstill: Engine at 1500 RPM, wheels at 0 RPM
> - Gradual engagement lets speeds synchronize smoothly
> - Prevents stall or violent jerk
>
> **Torque capacity:**
> T_max = μ × N × F_clamp × R_mean
>
> Where:
> - μ = friction coefficient (~0.3-0.4)
> - N = number of friction surfaces (2 for single-plate)
> - F_clamp = clamping force from spring (~3000-5000 N)
> - R_mean = mean radius of friction surface
>
> **Typical clutch capacity: 250-400 Nm** (must exceed peak engine torque!)"

---

#### **Part 4: Manual Gearbox Internals** (Slides 20-24, ~12 minutes)

##### Slide 20: Manual Transmission Overview
**Visual:** Cutaway of complete manual gearbox showing all gear sets
**Instructor Script:**
> "Let's look inside a manual transmission:
>
> **Main Components:**
>
> **1. Input Shaft:**
> - Connected to clutch disc
> - Receives power from engine (when clutch engaged)
>
> **2. Output Shaft:**
> - Delivers power to differential/wheels
> - Parallel to input shaft
>
> **3. Gear Sets:**
> - Multiple pairs of gears, always meshing (**constant mesh design**)
> - Different sized pairs for each gear ratio
> - Example: 1st gear pair (20T/60T), 2nd gear pair (25T/50T), etc.
>
> **4. Synchronizers (Synchromesh):**
> - Allow smooth gear engagement
> - Match speeds before locking
>
> **5. Shift Forks & Mechanism:**
> - Moved by gear lever
> - Slide synchronizers to select gears
>
> **Key Principle:** Gears are ALWAYS meshing and spinning. Selection is done by locking the right gear to the output shaft."

##### Slide 21: Constant Mesh Gearbox Operation
**Visual:** Animation showing gear selection process
**Instructor Script:**
> "**CONSTANT MESH principle** (all modern manuals):
>
> **Setup:**
> - Input shaft has gears fixed to it (rotate with input shaft always)
> - Output shaft has gears that **free-wheel** on bearings (not locked)
> - Synchronizers on output shaft can lock selected gear
>
> **Example - Selecting 2nd Gear:**
>
> **Before selection (in neutral):**
> - Input shaft spinning at engine speed
> - All gears on input shaft spinning
> - Output shaft gears spinning (driven by meshing input gears) BUT freewheeling
> - Output shaft stationary (no gear locked)
>
> **Shifting to 2nd:**
> 1. **Press clutch** → Disconnect engine
> 2. **Move shift lever** → Shift fork moves 2nd gear synchronizer
> 3. **Synchronizer matches speeds** → Friction brings output shaft to 2nd gear speed
> 4. **Synchronizer locks** → 2nd gear now locked to output shaft
> 5. **Release clutch** → Power flows: Engine → Input shaft → 2nd gear pair → Output shaft → Wheels
>
> **Result:** 2nd gear ratio now active!"

##### Slide 22: Synchromesh Mechanism
**Visual:** Detailed cross-section of synchromesh unit
**Instructor Script:**
> "**SYNCHROMESH = Synchronizer Mechanism**
>
> **Problem it solves:**
> When shifting (e.g., from 2nd to 3rd):
> - 3rd gear on output shaft spinning at one speed (freewheeling)
> - Output shaft spinning at different speed (locked to 2nd gear)
> - Can't just lock them together → Would clash, grind gears!
>
> **Synchromesh operation:**
>
> **Stage 1: Synchronizing (friction cone contact)**
> - Shift fork pushes synchronizer sleeve toward 3rd gear
> - Friction cone on synchro ring contacts friction cone on gear
> - Friction gradually matches speeds (synchro ring rotates slightly)
>
> **Stage 2: Locking (dog teeth engagement)**
> - Once speeds matched (synchro ring aligns)
> - Continued push slides sleeve further
> - Dog teeth on sleeve engage dog teeth on gear
> - **Gear now locked to output shaft**
>
> **Benefits:**
> ✓ Smooth, clash-free shifting
> ✓ No need to match speeds manually (like old non-synchro boxes)
> ✓ Fast shifts possible
>
> **Modern transmissions:** All forward gears have synchros (reverse often doesn't, hence the 'crunch' if you don't stop completely!)"

##### Slide 23: Power Flow Analysis - 1st Gear Example
**Visual:** Power flow diagram with one gear engaged
**Instructor Script:**
> "Let's trace power flow with **1st gear engaged:**
>
> **Power Path:**
>
> 1. **Engine → Clutch** (engaged) → Input shaft spinning
>
> 2. **Input shaft → 1st gear on input shaft** (fixed to shaft) → 1st gear spinning
>
> 3. **1st gear (input) meshes with 1st gear (output)** → 1st gear on output shaft driven
>
> 4. **1st gear (output) → Synchronizer locked** → Output shaft forced to rotate with 1st gear
>
> 5. **Output shaft → Differential → Wheels**
>
> **Meanwhile:**
> - All other gears on input shaft also spinning (constant mesh)
> - All other gears on output shaft freewheeling (not locked)
> - **Only 1st gear pair is transmitting power** (because only 1st is locked to output shaft)
>
> **Shift to 2nd:**
> - Unlock 1st synchronizer
> - Lock 2nd synchronizer
> - Now 2nd gear pair transmits power
>
> **Elegant design:** Simple mechanical selection determines which ratio is active."

##### Slide 24: Gear Shift Mechanism
**Visual:** Shift linkage from gear lever to shift forks
**Instructor Script:**
> "**How gear lever connects to synchronizers:**
>
> **Components:**
> - **Gear lever:** What driver moves (in cabin)
> - **Shift linkage:** Cables or rods connecting lever to gearbox
> - **Shift selector:** Rotates to select which fork to move (e.g., 1-2 fork, 3-4 fork, 5-R fork)
> - **Shift forks:** Slide synchronizers along output shaft
>
> **Gear Pattern (typical 5-speed H-pattern):**
> ```
>     1    3    5
>     |    |    |
>   -–N–-
>     |    |    |
>     2    4    R
> ```
>
> **Shifting process (e.g., 2nd to 3rd):**
> 1. **Driver presses clutch** → Disconnects engine
> 2. **Driver pulls lever from 2 to N** → Shift fork releases 2nd synchro → Output shaft neutral
> 3. **Driver pushes lever to 3 position** → Selector rotates → Different shift fork engaged
> 4. **Shift fork pushes 3rd synchro** → Synchro matches speeds → Locks 3rd gear
> 5. **Driver releases clutch** → Re-engages engine → Now in 3rd gear
>
> **Interlock mechanism:** Prevents selecting two gears at once (would lock transmission!)"

---

### **CLIMAX: Complete Transmission Design** (Slides 25-27, ~12 minutes)

#### Slide 25: Designing a Complete 5-Speed Manual Transmission
**Visual:** Complete design worksheet with all ratios calculated
**Instructor Script:**
> "Let's design a complete transmission system for a passenger car:
>
> **Vehicle Specifications:**
> - Mass: 1,200 kg
> - Engine: Peak torque 180 Nm @ 4000 RPM, Redline 6500 RPM
> - Wheel radius: 0.32 m
> - Performance requirements:
>   - 0-100 km/h: <10 seconds
>   - Top speed: 180 km/h
>   - Climb 15° slope in 1st gear
>
> **STEP 1: Determine Differential Ratio**
> Choose: GR_diff = **4.1** (typical for passenger car)
>
> **STEP 2: Calculate 1st Gear Ratio** (hill climbing requirement)
> - Force for 15° slope: F = 1200 × 9.81 × sin(15°) + rolling ≈ **3,200 N**
> - Torque at wheels: τ_wheel = 3200 × 0.32 = **1,024 Nm**
> - Required GR_1st: 1024 = 180 × GR_1st × 4.1 × 0.95
> - **GR_1st = 1024 / (180 × 4.1 × 0.95) = 1.46... round to 3.5**
>
> **STEP 3: Calculate 5th Gear Ratio** (top speed)
> - Top speed 180 km/h = 50 m/s
> - Wheel RPM: ω_wheel = 50 / (2π × 0.32) = 24.8 rev/s = **1,490 RPM**
> - Engine at 6500 RPM
> - Overall ratio: 6500 / 1490 = 4.36
> - **GR_5th = 4.36 / 4.1 = 1.06 ≈ 1.0** (close to 1:1, common for 5th gear)
>
> **STEP 4: Design Intermediate Gears** (geometric progression)
> - 2nd: 2.4
> - 3rd: 1.7
> - 4th: 1.3
>
> **Final Ratios:**
> | Gear | Ratio | Overall (with diff) |
> |------|-------|---------------------|
> | 1st  | 3.5   | 14.35               |
> | 2nd  | 2.4   | 9.84                |
> | 3rd  | 1.7   | 6.97                |
> | 4th  | 1.3   | 5.33                |
> | 5th  | 1.0   | 4.10                |
> | Reverse | 3.8 | 15.58              |"

#### Slide 26: Analyzing the Design - RPM Drop During Shifts
**Visual:** Graph showing engine RPM through gears at 100 km/h
**Instructor Script:**
> "Let's verify our design by checking RPM at different vehicle speeds:
>
> **At 100 km/h (27.8 m/s):**
> - Wheel RPM = 27.8 / (2π × 0.32) = **828 RPM**
>
> **Engine RPM in each gear:**
> - **1st gear:** 828 × 14.35 = **11,882 RPM** → Way over redline! (Can't reach 100 km/h in 1st)
> - **2nd gear:** 828 × 9.84 = **8,147 RPM** → Over redline (Can't sustain 100 km/h in 2nd)
> - **3rd gear:** 828 × 6.97 = **5,771 RPM** → Below redline ✓ (Can reach 100 in 3rd)
> - **4th gear:** 828 × 5.33 = **4,413 RPM** → Good RPM ✓
> - **5th gear:** 828 × 4.10 = **3,395 RPM** → Optimal for cruising ✓
>
> **Shift points for acceleration (at redline 6500 RPM):**
> - 1st → 2nd shift at: 6500 / 14.35 = 453 wheel RPM = **57 km/h**
> - 2nd → 3rd shift at: **84 km/h**
> - 3rd → 4th shift at: **112 km/h**
> - 4th → 5th shift at: **147 km/h**
>
> **RPM drop per shift:**
> - 1st → 2nd: 6500 → (6500 × 9.84/14.35) = **4,458 RPM** (drop 2042 RPM)
> - 2nd → 3rd: 6500 → **4,603 RPM** (drop 1897 RPM)
>
> **Design is good:** Smooth progression, keeps engine in power band during acceleration!"

#### Slide 27: Real-World Comparison - Honda Civic 6-Speed Manual
**Visual:** Honda Civic actual gear ratios compared to our design
**Instructor Script:**
> "Let's compare our design to a real transmission – Honda Civic 2.0L 6-speed:
>
> **Honda Civic Actual Ratios:**
> | Gear | Our Design | Honda Actual | Comment |
> |------|------------|--------------|---------|
> | 1st  | 3.50       | 3.27         | Similar - ours slightly taller |
> | 2nd  | 2.40       | 2.13         | Ours taller - Honda closer spaced |
> | 3rd  | 1.70       | 1.47         | Similar trend |
> | 4th  | 1.30       | 1.03         | Honda has 6th for overdrive |
> | 5th  | 1.00       | 0.82         | |
> | 6th  | -          | 0.65         | **Overdrive** for fuel economy |
> | Diff | 4.10       | 4.35         | Similar |
>
> **Why Honda uses 6 speeds:**
> - **Closer ratio spacing** → Engine stays in power band better during acceleration
> - **6th gear overdrive (0.65)** → Engine at ~2500 RPM at 100 km/h → Better fuel economy
>
> **Modern trend:** 6, 7, even 8-speed manuals (Corvette, Porsche) for performance + economy
>
> **Our 5-speed design is valid** - similar to many real passenger cars!"

---

### **RESOLUTION: Consolidation & Next Steps** (Slides 28-30, ~10 minutes + Q&A)

#### Slide 28: Key Takeaways Summary
**Visual:** Clean summary organized by topics
**Instructor Script:**
> "Let's consolidate what you've mastered today:
>
> **WHY TRANSMISSIONS:**
> ✓ Engine operates in narrow RPM range (1500-6500 RPM), wheels need 0-1500 RPM
> ✓ Transmission multiplies torque at low speeds, allows high speed at top end
> ✓ Keeps engine in optimal BSFC zone for fuel economy (Session 6 connection!)
>
> **GEAR RATIO MATHEMATICS:**
> ✓ **GR = N_driven / N_driver = ω_in / ω_out**
> ✓ **τ_out = τ_in × GR × η** (torque multiplication)
> ✓ **ω_out = ω_in / GR** (speed reduction)
> ✓ Overall ratio = GR_gearbox × GR_differential
>
> **CLUTCH SYSTEM:**
> ✓ Disconnects engine from transmission for gear shifting and stopping
> ✓ Single-plate clutch: Flywheel + Friction disc + Pressure plate
> ✓ Friction zone allows smooth engagement
>
> **MANUAL GEARBOX:**
> ✓ Constant mesh design: All gears always meshing, select by locking to output shaft
> ✓ Synchromesh matches speeds for smooth, clash-free shifting
> ✓ Power flows through selected gear pair only
>
> **TRANSMISSION DESIGN:**
> ✓ 1st gear ratio determined by hill climbing requirement
> ✓ Top gear ratio determined by top speed and redline RPM
> ✓ Intermediate gears spaced geometrically
>
> **You can now design and analyze complete manual transmissions!**"

#### Slide 29: Connection to Next Session
**Visual:** Preview of automatic transmission, CVT, and electric motor
**Instructor Script:**
> "Today we mastered manual transmissions – driver controls gear selection.
>
> **Next Session (Session 8): Advanced Transmissions & Powertrain Alternatives**
>
> **Part 1: Automatic Transmissions**
> - Torque converter (replaces clutch)
> - Planetary gear sets (compact, multiple ratios)
> - Hydraulic/electronic control (no clutch pedal!)
>
> **Part 2: Modern Transmission Technologies**
> - CVT (Continuously Variable Transmission) – infinite ratios!
> - DCT/DSG (Dual-Clutch Transmission) – fast shifts, no power loss
> - AMT (Automated Manual Transmission) – robotized manual
>
> **Part 3: Differential & Drivetrain**
> - How differential allows wheels to spin at different speeds (cornering)
> - FWD vs RWD vs AWD configurations
>
> **Part 4: Electric Powertrains (Preview)**
> - Electric motors: Instant torque from 0 RPM
> - Do EVs even need multi-speed transmissions? (Mostly single-speed!)
> - Hybrid architectures (Toyota Prius example)
>
> **Connection:** Manual transmission fundamentals (gears, ratios, torque multiplication) apply to ALL transmission types – today's foundation supports everything!"

#### Slide 30: Assignment & Q&A
**Visual:** Assignment problems listed
**Instructor Script:**
> "**Assignment (Due before Session 8):**
>
> **Problem 1:** A vehicle has the following specifications:
> - Mass: 1,500 kg
> - Engine peak torque: 200 Nm @ 3500 RPM, Redline: 6000 RPM
> - Wheel radius: 0.33 m
> - Must climb 18° slope from standstill
> - Top speed requirement: 150 km/h
>
> Design a 5-speed manual transmission:
> a) Calculate required 1st gear ratio (assume differential ratio = 4.2, efficiency = 95%)
> b) Calculate required 5th gear ratio
> c) Design intermediate gear ratios (2nd, 3rd, 4th) using geometric progression
> d) At what vehicle speed should you shift from 2nd to 3rd if accelerating at redline?
>
> **Problem 2:** For a gear pair with driver gear (25 teeth) and driven gear (75 teeth):
> a) Calculate gear ratio
> b) If input is 3600 RPM and 150 Nm torque, find output RPM and torque (assume 96% efficiency)
> c) If driver gear has pitch circle diameter 80 mm, what is driven gear diameter?
>
> **Problem 3:** Explain in your own words:
> a) Why does engine RPM drop when you shift to a higher gear at constant vehicle speed?
> b) What would happen if you tried to shift from 5th to 1st at 100 km/h? (Hint: Calculate engine RPM)
> c) Why is synchromesh necessary in modern transmissions?
>
> **Bonus:** Research and sketch the gear arrangement (number of teeth for each gear pair) for any real car's transmission. Calculate the overall ratios and verify against published specs.
>
> **Discussion Questions for Q&A:**
> - Why are modern cars moving to 6, 7, 8 or even 10-speed transmissions?
> - What are the advantages and disadvantages of manual vs automatic transmissions?
> - How do motorcycles achieve 6 speeds in such a small gearbox? (Sequential shifting)
> - What is double-clutching and why was it necessary in old trucks?
>
> **30 minutes for your questions.**"

---

## 📊 PPT DESIGN GUIDANCE

### Visual Style:
- **Consistency:** Maintain professional engineering template from Sessions 1-6
- **Technical Professionalism:** Clear gear diagrams, cutaway illustrations, calculation worksheets
- **Color coding:**
  - Blue for input shaft and components
  - Orange for output shaft and components
  - Green for power flow arrows (when gear engaged)
  - Gray for freewheeling components
- **Font sizes:** Calculation steps must be clear (18-20pt minimum)

### Key Slides to Emphasize:
1. **Slide 2**: Engine vs wheel mismatch problem – Establishes need
2. **Slide 10**: Gear ratio formulas – Core mathematics
3. **Slide 16**: Complete design example – Real application
4. **Slide 21**: Constant mesh operation – Understanding internals
5. **Slide 25**: Full 5-speed design – Integration of all concepts
6. **Slide 28**: Summary – Comprehensive reference

### Animations:
- **Slide 8-9**: Animated gear meshing showing speed reduction and torque multiplication
- **Slide 18**: Clutch engagement/disengagement animation (pressure plate movement)
- **Slide 21**: Synchronizer sliding and locking animation
- **Slide 23**: Power flow highlighting (show power path lighting up in one gear)
- **Use color highlighting** to trace power flow through transmission

### Visual Elements to Include:
- **Gear diagrams:** Clear spur gear illustrations with teeth counts labeled
- **Cutaway photos:** Real manual transmission cutaways (ZF, Getrag, etc.)
- **Component photos:** Real clutch assembly, synchromesh, shift forks
- **Calculation worksheets:** Step-by-step calculations with boxes and arrows
- **Comparison tables:** Gear ratio comparisons, Honda Civic example
- **Power flow diagrams:** Show which components rotate in each gear

---

## 🎯 INSTRUCTOR NOTES

### Pedagogical Strategy:
- **Problem-driven:** Start with mismatch between engine and wheel needs (why?)
- **Mathematics-heavy:** This is calculation-intensive – work through examples step-by-step
- **Build from simple to complex:** Single gear pair → Complete transmission
- **Real-world validation:** Compare designs to actual vehicles (Honda Civic)
- **Hands-on feel:** If possible, bring real gears, clutch disc, synchromesh to show students

### Common Student Challenges:

**Challenge 1: "Why does higher gear ratio mean more torque but lower speed? Shouldn't 'higher' mean faster?"**
**How to address:** Clarify terminology: "Higher gear ratio" (e.g., 3.5) means more reduction, not higher gear number. "5th gear" has LOWER ratio (~1.0) than "1st gear" (3.5). Emphasize: Gear ratio = reduction ratio. Higher reduction = more torque, less speed.

**Challenge 2: "In calculations, when do I multiply and when do I divide by gear ratio?"**
**How to address:** Always work from definitions:
- Speed: ω_out = ω_in / GR (divide to reduce speed)
- Torque: τ_out = τ_in × GR (multiply to increase torque)
Make students write this on every problem.

**Challenge 3: "Why are all gears meshing? Doesn't that cause power loss and noise?"**
**How to address:** Explain constant mesh advantages:
- Smoother shifting (synchro can match speeds before locking)
- Stronger (gears always engaged, no shock loading)
- Modern design minimizes losses through good bearings and lubrication
- Trade-off: Slight efficiency loss (~2-4%) vs improved reliability and shift quality

**Challenge 4: "I don't understand how synchronizer works – there are so many parts!"**
**How to address:** Simplify to two stages:
1. Friction stage: Cone surfaces match speeds through friction (like mini-clutch)
2. Locking stage: Once matched, dog teeth engage mechanically
Use animation or physical model if available.

### Timing Flexibility:

**If running short:**
- Condense clutch details (Slide 19) – just show operation, skip torque capacity calculation
- Combine Slides 20-21 (gearbox overview and constant mesh operation)
- Move synchromesh details (Slide 22) to assignment reading
- Reduce time on shift mechanism (Slide 24)

**If running long:**
- Move complete design example (Slide 25) calculations to assignment (just show results)
- Defer RPM drop analysis (Slide 26) to Q&A discussion
- Reduce time on Honda Civic comparison (Slide 27)

**Core content (must cover):**
- Slides 2-3 (Why transmission needed – critical motivation)
- Slides 8-11 (Gear ratio fundamentals – absolute core)
- Slide 13 (Complete calculation example – must work through)
- Slide 16 (Design example – application)
- Slides 17-18 (Clutch basics)
- Slides 20-21 (Constant mesh operation)

### Engagement Points:

**Slide 2:** Ask "Has anyone driven a car without enough power for a hill? What happens?" (Engine bogs down, need lower gear)

**Slide 11:** Work through calculation together on board – pause between steps, ask students for next step

**Slide 14:** Give students 2 minutes to try problem – competitive element

**Slide 16:** Interactive design – give parameters, ask students to estimate 1st gear ratio before calculation

**Slide 23:** Trace power flow together – point at diagram, ask "where does power go next?"

**Q&A:** Be ready for questions about:
- **Sequential gearboxes:** How motorcycles and race cars shift (linear pattern, no searching for gears)
- **Dog-leg gearboxes:** Why some sports cars have 1st gear in unusual position
- **Gear whine:** Why race cars and straight-cut gears make noise (no helical teeth)
- **Reverse gear:** Why it doesn't have synchro (crashes if you don't stop first)

### Safety/Ethics Notes:
- **Clutch abuse:** Riding clutch (partial engagement) causes wear, overheating, premature failure
- **Money shifting:** Accidentally shifting to wrong gear (e.g., 2nd instead of 4th) can over-rev engine → catastrophic damage
- **Maintenance:** Transmission fluid change intervals, clutch replacement indicators
- **Driving efficiency:** Proper gear selection saves fuel – connection to BSFC maps (Session 6)

---

## ✅ Session Success Criteria

Students leave able to:
- ✓ Explain need for transmission in matching engine characteristics to wheel requirements
- ✓ Calculate gear ratios and analyze effect on torque and speed
- ✓ Describe clutch construction and operation
- ✓ Explain manual gearbox construction (constant mesh, synchromesh)
- ✓ Design transmission gear ratios for given performance requirements
- ✓ Analyze power flow through manual transmission in any gear

**Most importantly:** Students **understand the complete manual transmission system** as a mechanical solution to the engine-wheel mismatch problem, can perform gear ratio calculations confidently, and can design transmissions for real vehicle requirements.

---

## 📝 ADDITIONAL NOTES

### Integration with Previous Sessions:
- **Session 3:** Calculated power requirements → Session 7 shows how transmission delivers that power at different speeds
- **Session 4:** Engine torque curves → Session 7 uses those to determine gear ratios
- **Session 6:** BSFC maps and optimal operating zones → Session 7 shows how transmission keeps engine in those zones

### Setting Up Session 8:
Throughout session, mention limitations of manual transmission:
- Driver must shift (attention, skill required)
- Shift interrupts power delivery (acceleration pause)
- Only discrete ratios available (5-6 options)
Session 8 will show how modern transmissions address these limitations.

### Real-World Context Examples:
- **Sports cars:** Close-ratio gearboxes (smaller ratio steps) keep engine in power band
- **Trucks:** Wider 1st gear (5.0+) for heavy loads and steep hills
- **Economy cars:** Taller gearing (lower numerical ratio) for better highway fuel economy
- **Track days:** How proper gear selection improves lap times (staying in power band)

### Physical Demonstrations (if available):
- **Bring real gears:** Show two gears meshing, count teeth, calculate ratio
- **Clutch disc:** Show friction material, splined hub, explain wear
- **Synchromesh unit:** Disassembled synchro showing friction cone and dog teeth
- **Shift mechanism:** Model or actual linkage showing how gear lever connects to forks

These make abstract concepts concrete and memorable.

### Connection to Electronics:
- **Manual transmission sensors:** Gear position sensor (for ECU to know current gear)
- **Clutch position sensor:** For engine torque management during shifts
- **Rev-matching systems:** Modern manuals with auto-blip on downshift (electronics controlling throttle)
- **Hill start assist:** Uses sensors and brakes to prevent rollback

Manual transmissions are increasingly electronically assisted even though mechanically operated!

---

**End of Session 7 Framework**
