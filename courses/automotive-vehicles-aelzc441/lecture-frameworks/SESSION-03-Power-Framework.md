# Session 3: From Forces to Power Requirements
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 90 minutes lecture + 30 minutes Q&A
**Approach:** Teacher-Led Narrative - The Culmination
**PPT Target:** 26-30 slides

---

## 🎯 Session Objectives (For Instructor)

By the end of this session, students will be able to:
- Convert linear force to torque using wheel radius
- Calculate wheel torque requirements for various conditions
- Apply rotational motion equations to convert torque to power
- Calculate vehicle performance metrics (0-100 km/h, gradeability, top speed)
- Understand the complete force → torque → power chain

---

## 📖 INSTRUCTOR-LED STORY ARC

### **SETUP: The Journey So Far** (Slides 1-3, ~8 minutes)

#### Slide 1: Title
**Visual:** Professional title slide showing force/torque/power progression
**Instructor Script:**
> "Welcome to Session 3. Today is special. Today, everything we've learned comes together, and you'll understand exactly how engineers size powertrains."

#### Slide 2: The Story So Far
**Visual:** Visual timeline of Sessions 1-2
**Instructor Script:**
> "Let me tell you where we've been:
>
> **Session 1**: We calculated the forces resisting vehicle motion
> - Rolling resistance
> - Aerodynamic drag
> - Gradient resistance
> - You can now tell me exactly how much force any vehicle needs in any scenario.
>
> **Session 2**: We learned how tires generate force
> - F = μN (the friction equation)
> - Friction circle
> - You understand the maximum force tires can provide.
>
> But we left a critical question unanswered..."

#### Slide 3: The Missing Link
**Visual:** Engine → ? → Wheel Force (question mark emphasized)
**Instructor Script:**
> "Engines don't produce force - they produce **torque** (rotational force).
> Wheels need **force** (linear force) to push the vehicle.
>
> **Today's question**: How do we connect these? How much engine torque do we need? How much power?
>
> By the end of today, you'll be able to specify engine requirements for any vehicle. That's the power of what we're learning."

---

### **TRIGGER: The Challenge** (Slides 4-5, ~5 minutes)

#### Slide 4: Real-World Design Problem
**Visual:** Blank vehicle spec sheet
**Instructor Script:**
> "Here's a real engineering challenge. You're designing a new SUV:
> - Mass: 2,000 kg
> - Top speed target: 180 km/h
> - 0-100 km/h target: 8 seconds
> - Must climb 15% grade at 60 km/h
>
> **Question**: How much power does the engine need?
>
> Today, I'm going to show you how to calculate the exact answer. No guessing, no rules of thumb - just physics and math."

#### Slide 5: Why This Matters
**Visual:** Images of different powertrain options
**Instructor Script:**
> "Understanding force-torque-power relationships lets you:
> - Size engines correctly (not over-powered, not under-powered)
> - Predict vehicle performance before building
> - Optimize for efficiency vs performance
> - Understand why electric motors behave differently
>
> This is practical engineering. Let's begin."

---

### **RISING ACTION: Building the Chain** (Slides 6-24, ~55 minutes)

#### **Part 1: Force to Torque Conversion** (Slides 6-10, ~15 minutes)

##### Slide 6: Understanding Torque
**Visual:** Wheel with force and radius labeled
**Instructor Script:**
> "First, let's be clear about what torque is. You know force (F, in Newtons). Torque (τ, tau) is **force applied at a distance from rotation point**.
>
> **Torque = Force × Distance**
>
> Or more specifically for wheels:
> **τ = F × r**
>
> Where:
> - τ = torque (N⋅m)
> - F = force at tire contact patch (N)
> - r = wheel radius (m)
>
> Let me show you why this matters."

##### Slide 7: The Wheel as a Lever
**Visual:** Free body diagram of wheel
**Instructor Script:**
> "Think of the wheel as a lever. The axle applies torque at the center. This creates force at the circumference (where tire touches road).
>
> [Show diagram]:
> - Torque at axle (τ)
> - Radius (r)
> - Force at contact patch (F)
>
> **Relationship**: F = τ/r
>
> Or rearranged: **τ = F × r**
>
> Bigger wheel (larger r) needs more torque for same force. That's why off-road trucks with huge tires need more torque."

##### Slide 8: Example - Calculating Required Wheel Torque
**Visual:** Honda Civic at 100 km/h, flat road
**Instructor Script:**
> "Back to our Honda Civic from Session 1. Remember:
> - At 100 km/h on flat road: F_total = 465 N (rolling + drag)
> - Wheel radius: r = 0.32 m (typical for 16" wheel + tire)
>
> **Required torque at ONE wheel** (4-wheel drive):
> τ = F × r = (465/4) × 0.32 = **37.2 N⋅m per wheel**
>
> **For rear-wheel drive** (power to 2 wheels):
> τ = (465/2) × 0.32 = **74.4 N⋅m per rear wheel**
>
> This is the wheel torque needed to maintain 100 km/h."

##### Slide 9: Practice Calculation
**Visual:** Different scenario
**Instructor Script:**
> "Your turn. Calculate wheel torque for:
> - Vehicle mass: 1,500 kg
> - Climbing 5% grade at constant 80 km/h
> - 4-wheel drive
> - Wheel radius: 0.35 m
> - Assume: F_rolling = 180 N, F_drag = 200 N, F_gradient = 736 N
>
> [Pause for calculation]
>
> **Solution**:
> - F_total = 180 + 200 + 736 = 1,116 N
> - τ per wheel = (1,116/4) × 0.35 = **97.7 N⋅m per wheel**
>
> Good. Now let's connect this to engine torque."

##### Slide 10: Transmission Multiplies Torque
**Visual:** Engine → Gearbox → Wheel diagram with gear ratios
**Instructor Script:**
> "Here's the key: Engine doesn't directly drive wheels. Transmission sits in between and **multiplies torque**.
>
> **Simple relationship**:
> τ_wheel = τ_engine × G_total
>
> Where G_total = gear ratio × final drive ratio
>
> Example: If G_total = 10:
> - Engine torque = 200 N⋅m
> - Wheel torque = 200 × 10 = 2,000 N⋅m
>
> We'll cover transmissions in detail in Sessions 7-8. For now, know that we can multiply engine torque through gearing.
>
> **Implication**: Smaller engines can move heavy vehicles if transmission ratios are right."

---

#### **Part 2: Torque to Power Conversion** (Slides 11-16, ~20 minutes)

##### Slide 11: What is Power?
**Visual:** Definition with units
**Instructor Script:**
> "Torque tells us force capability at a wheel. But torque doesn't include speed. That's where power comes in.
>
> **Power = How fast you can do work**
>
> In rotational systems:
> **P = τ × ω**
>
> Where:
> - P = power (Watts)
> - τ = torque (N⋅m)
> - ω (omega) = angular velocity (rad/s)
>
> Or, if you have RPM instead:
> **P = (τ × N) / 9,549**
>
> Where N = rotational speed in RPM
>
> Let me show you why this matters."

##### Slide 12: Understanding the Power Equation
**Visual:** Graph showing power vs RPM for constant torque
**Instructor Script:**
> "Look at this graph. If engine maintains 200 N⋅m of torque:
> - At 1,000 RPM: P = (200 × 1,000) / 9,549 = **20.9 kW**
> - At 3,000 RPM: P = (200 × 3,000) / 9,549 = **62.8 kW**
> - At 5,000 RPM: P = (200 × 5,000) / 9,549 = **104.7 kW**
>
> **Same torque, different power!**
>
> This is why:
> - High RPM = high power (sports cars)
> - High torque at low RPM = good for acceleration (diesel engines, electric motors)
>
> Power and torque are related but different."

##### Slide 13: Converting Linear to Rotational Terms
**Visual:** Conversion table
**Instructor Script:**
> "We need to connect linear motion (vehicle speed) to rotational motion (wheel speed).
>
> **Linear velocity to angular velocity**:
> ω = v / r
>
> Where:
> - v = linear velocity (m/s)
> - r = wheel radius (m)
> - ω = angular velocity (rad/s)
>
> **Example**: 100 km/h (27.8 m/s) with 0.32 m radius wheel:
> ω = 27.8 / 0.32 = **86.9 rad/s** = **830 RPM** (at the wheel)
>
> If transmission ratio is 5:1, engine spins at 4,150 RPM."

##### Slide 14: Power Requirement Calculation
**Visual:** Complete example with steps
**Instructor Script:**
> "Let's calculate power needed for our Honda Civic at 100 km/h:
>
> **Given**:
> - F_total = 465 N (from Session 1)
> - v = 27.8 m/s (100 km/h)
>
> **Method 1 - Direct**:
> P = F × v
> P = 465 × 27.8 = **12,927 W = 12.9 kW**
>
> **Method 2 - Through torque**:
> τ_wheel = 465 × 0.32 = 148.8 N⋅m (for RWD)
> ω_wheel = 27.8 / 0.32 = 86.9 rad/s
> P = τ × ω = 148.8 × 86.9 = **12,933 W ≈ 12.9 kW**
>
> Both methods give the same answer (as they must!).
>
> **This is the power just to maintain 100 km/h**. To accelerate, we need more."

##### Slide 15: Accounting for Losses
**Visual:** Power flow diagram showing losses
**Instructor Script:**
> "Real-world complication: Not all engine power reaches the wheels.
>
> **Drivetrain losses**:
> - Transmission friction: ~5-15%
> - Differential friction: ~2-5%
> - Total losses: ~15-20% for manual, ~20-25% for automatic
>
> **Efficiency factor** (η):
> P_engine = P_wheel / η
>
> For our Civic (manual transmission, η = 0.85):
> P_engine = 12.9 kW / 0.85 = **15.2 kW**
>
> So we need ~15 kW of engine power just to cruise at 100 km/h on flat road."

##### Slide 16: Why Cars Have Much More Power
**Visual:** Comparison table
**Instructor Script:**
> "If we only need 15 kW to cruise, why do cars have 80-150 kW engines?
>
> Because we also need power for:
> - **Acceleration** (much higher forces)
> - **Hill climbing** (gradient resistance)
> - **Passing maneuvers** (quick acceleration at highway speeds)
> - **Air conditioning** (can use 2-5 kW)
> - **Reserve** (don't want to run engine at 100% continuously)
>
> Let me show you acceleration calculations."

---

#### **Part 3: Performance Calculations** (Slides 17-24, ~20 minutes)

##### Slide 17: Acceleration Performance
**Visual:** Force diagram during acceleration
**Instructor Script:**
> "During acceleration, we need force for:
> 1. Overcoming resistance (rolling + drag)
> 2. Accelerating the mass (F = ma)
>
> **Total force needed**:
> F_total = F_resistance + ma
>
> Where:
> - m = vehicle mass (kg)
> - a = desired acceleration (m/s²)
>
> Higher acceleration = more force = more torque = more power."

##### Slide 18: Example - 0-100 km/h Calculation
**Visual:** Step-by-step calculation
**Instructor Script:**
> "Let's calculate 0-100 km/h time for Honda Civic (simplified):
>
> **Assumptions**:
> - Mass: 1,300 kg
> - Available power: 80 kW
> - Ignore changing resistance (simplification)
> - Assume average force during acceleration
>
> **Step 1**: Convert speed
> v_final = 100 km/h = 27.8 m/s
>
> **Step 2**: Calculate average power during acceleration
> Assuming average speed = 50 km/h = 13.9 m/s
> F_available = P / v_avg = 80,000 / 13.9 = 5,755 N
>
> **Step 3**: Account for resistance (estimate)
> F_resistance_avg = 250 N
> F_net = 5,755 - 250 = 5,505 N
>
> **Step 4**: Calculate acceleration
> a = F/m = 5,505 / 1,300 = 4.23 m/s²
>
> **Step 5**: Calculate time
> t = v / a = 27.8 / 4.23 = **6.6 seconds**
>
> Real-world: ~8-9 seconds (our simplifications were optimistic). But this shows the method!"

##### Slide 19: Maximum Gradeability
**Visual:** Vehicle on steep incline
**Instructor Script:**
> "Another performance metric: **Gradeability** - steepest hill the vehicle can climb.
>
> **At the limit**:
> F_available = F_rolling + F_gradient (ignore drag at low speed)
>
> For maximum grade:
> F_gradient = F_available - F_rolling
> mg sin(θ_max) = (P/v) - C_rr × mg
>
> **Example** (Civic at 60 km/h = 16.7 m/s):
> F_available = 80,000 / 16.7 = 4,790 N
> F_rolling = 0.012 × 12,753 = 153 N
> F_gradient = 4,790 - 153 = 4,637 N
>
> sin(θ_max) = 4,637 / 12,753 = 0.364
> θ_max = **21.3 degrees = 39% grade**
>
> That's steep! Real-world lower due to other factors, but shows potential."

##### Slide 20: Maximum Speed Calculation
**Visual:** Graph of power vs speed
**Instructor Script:**
> "Top speed occurs when all available power is consumed by resistance:
>
> **P_available = F_total × v_max**
>
> Where F_total = F_rolling + F_drag (ignore gradient on flat road)
>
> **Problem**: F_drag depends on v² which we're solving for!
>
> **Solution**: Iterative or algebraic solving.
>
> For our Civic with 80 kW power (simplified):
> [Show iterative approach or use quadratic solution]
>
> **Result**: v_max ≈ **185 km/h**
>
> (Real Honda Civic: ~195 km/h - our assumptions were conservative)"

##### Slide 21: Power-to-Weight Ratio
**Visual:** Comparison of different vehicles
**Instructor Script:**
> "A useful metric: **Power-to-Weight Ratio** (kW/kg or hp/ton)
>
> **Honda Civic**: 80 kW / 1,300 kg = **0.062 kW/kg = 62 W/kg**
>
> **Comparison**:
> - Economy car: 40-60 W/kg
> - Sports car: 100-150 W/kg
> - Supercar: 200-300 W/kg
> - Formula 1: 800+ W/kg
>
> Higher ratio = better acceleration, higher top speed.
>
> Quick estimate: For every 10 W/kg increase, 0-100 km/h improves by ~0.5-1 second."

##### Slide 22: Electric vs IC Engine Power Delivery
**Visual:** Torque curves comparison
**Instructor Script:**
> "Quick note on electric motors vs IC engines:
>
> **IC Engine**:
> - Torque peaks at specific RPM
> - Must use gears to match torque to speed
>
> **Electric Motor**:
> - Maximum torque from 0 RPM
> - Constant power across wide speed range
> - Why EVs accelerate so well
>
> **Both** ultimately limited by:
> 1. Tire friction (Session 2)
> 2. Available power
>
> We'll revisit in Session 8."

##### Slide 23: Practice Problem - Design Challenge
**Visual:** Design scenario
**Instructor Script:**
> "Design challenge: Delivery van specification
> - Mass (loaded): 2,500 kg
> - Required top speed: 120 km/h
> - Required 0-100 km/h: <15 seconds
> - Must climb 12% grade at 40 km/h
>
> **Task**: Calculate minimum power requirement.
>
> Consider:
> - Resistance forces at top speed
> - Acceleration needs
> - Hill climbing needs
> - Take the maximum of these
>
> [Work through together or assign as homework]"

##### Slide 24: Complete Solution
**Visual:** Worked solution
**Instructor Script:**
> "[Show complete solution to design challenge]
>
> **Results**:
> - For top speed: ~45 kW
> - For 0-100 acceleration: ~65 kW
> - For hill climb: ~55 kW
>
> **Recommendation**: **70-80 kW engine**
> - Covers all requirements
> - Includes safety margin
> - Accounts for accessory loads
>
> This is how engineers size powertrains."

---

### **CLIMAX: The Complete Picture** (Slides 25-26, ~10 minutes)

#### Slide 25: Force → Torque → Power Chain
**Visual:** Complete flowchart with all equations
**Instructor Script:**
> "Let me show you the complete chain we've built over three sessions:
>
> **Session 1: FORCES**
> F_total = F_rolling + F_drag + F_gradient
>
> **Session 2: FRICTION LIMIT**
> F_max = μ × N (tire limit)
>
> **Session 3 (Today): TORQUE & POWER**
> τ = F × r (force to torque)
> P = τ × ω = F × v (power requirement)
>
> **From this, we can calculate**:
> - Required engine power for any performance target
> - Vehicle acceleration, top speed, gradeability
> - Transmission ratios needed
>
> You now have the complete physics of vehicle motion and performance."

#### Slide 26: Why This Matters - Real Engineering
**Visual:** Photos of different vehicles
**Instructor Script:**
> "With what you've learned, you can now:
>
> ✓ **Specify** powertrain requirements for new vehicle designs
> ✓ **Predict** performance before building
> ✓ **Optimize** between efficiency and performance
> ✓ **Understand** why different vehicles have different powertrains:
>   - Sports car: High power, low weight (high P/W ratio)
>   - Delivery truck: High torque, lower power (hill climbing, cargo)
>   - Economy car: Modest power, optimized efficiency
>
> This isn't theoretical. This is how the automotive industry works.
>
> **Next sessions**: We'll learn HOW to generate this power (engines, Sessions 4-6) and HOW to deliver it (transmissions, Sessions 7-8)."

---

### **RESOLUTION: Mastery & Next Steps** (Slides 27-30, ~12 minutes + Q&A)

#### Slide 27: Summary of Key Equations
**Visual:** Clean equation reference sheet
**Instructor Script:**
> "Your reference card:
>
> **Force to Torque**:
> - τ = F × r
>
> **Torque to Power**:
> - P = τ × ω (rad/s)
> - P = (τ × N) / 9,549 (RPM)
> - P = F × v (linear)
>
> **Performance Metrics**:
> - Acceleration: a = (P/v - F_resistance) / m
> - Top speed: Solve P = F_total × v_max
> - Gradeability: sin(θ_max) = (P/v - F_rolling) / mg
>
> **Power-to-Weight**:
> - P/m (kW/kg or W/kg)
>
> These equations solve most vehicle performance questions."

#### Slide 28: Foundation Module Complete
**Visual:** Sessions 1-3 summary
**Instructor Script:**
> "Congratulations. You've completed the foundation module.
>
> **Session 1**: You learned to calculate resistance forces
> **Session 2**: You learned tire force generation limits
> **Session 3**: You learned power requirements
>
> **You can now**:
> - Calculate total resistance for any driving scenario
> - Determine maximum forces tires can provide
> - Specify power requirements for any vehicle
>
> This is the **physics foundation** for everything else in automotive engineering.
>
> Starting next session, we'll explore how vehicles actually generate and deliver this power. But you already understand why they need it."

#### Slide 29: Comprehensive Assignment
**Visual:** Multi-part problem
**Instructor Script:**
> "**Major Assignment** (combines all three sessions):
>
> Choose a real vehicle (provide specifications). Calculate:
>
> 1. Total resistance at 60, 100, and 140 km/h on flat road
> 2. Maximum friction force available (all tires, dry road)
> 3. Power required to maintain each speed
> 4. Predicted 0-100 km/h time
> 5. Maximum gradeability at 60 km/h
> 6. Theoretical top speed
>
> Compare your calculations to published specifications. Discuss differences.
>
> Due: Beginning of Session 5 (you have one session break).
>
> This shows you can apply everything we've learned."

#### Slide 30: Q&A and Looking Ahead
**Visual:** Preview of upcoming modules
**Instructor Script:**
> "30 minutes for questions. Also, preview of what's coming:
>
> **Module 2 (Sessions 4-8)**: Powertrain
> - How do engines generate torque?
> - How do we keep them cool and lubricated?
> - How do transmissions multiply torque?
>
> **Module 3 (Sessions 9-12)**: Chassis Dynamics
> - Vehicle dynamics in detail
> - Braking systems
> - Steering and suspension
>
> But for today, let's discuss what we covered. What questions do you have?"

---

## 📊 PPT DESIGN GUIDANCE

### Visual Style:
- **Equation-heavy slides**: Use large, clear fonts
- **Calculation slides**: Step-by-step reveal with build animations
- **Graphs**: Power vs speed, torque vs speed (reference for comparisons)

### Key Slides to Emphasize:
1. **Slide 3** (Missing link) - Sets up the session
2. **Slide 14** (Power calculation) - Core method
3. **Slide 25** (Complete chain) - Integration of all three sessions
4. **Slide 27** (Equation summary) - Students will photograph this

### Animations:
- **Slide 25**: Build the complete chain step-by-step
- **Calculation slides**: Reveal answers after pause for student work
- **Slide 26**: Animate different vehicle examples

### Include:
- **Actual vehicle specs**: Use real examples (Honda Civic, Ford F-150, etc.)
- **Comparison tables**: Power-to-weight ratios across vehicle classes
- **Performance graphs**: Show how power affects performance

---

## 🎯 INSTRUCTOR NOTES

### Pedagogical Strategy:
- **Integration focus**: Constantly reference Sessions 1 & 2
- **Practical emphasis**: Every equation applied immediately to real examples
- **Building confidence**: "You can now calculate what engineers calculate"
- **Transition moment**: End of foundation, beginning of systems

### Common Student Challenges:
- **Unit conversions**: km/h ↔ m/s, kW ↔ W - practice extensively
- **Torque vs Power**: Emphasize they're related but different
- **Simplified vs real calculations**: Acknowledge approximations

### Timing Notes:
- **Slides 17-24** (Performance): This is the meat - don't rush
- Can condense Slide 22 (EV vs IC) if time is tight
- Ensure time for Slide 25 (integration) - it's the payoff

### Engagement Points:
- **Slide 9, 23**: Student calculation opportunities
- **Slide 26**: Discuss real vehicles they know
- **Slide 29**: Can start assignment discussion in class

### Critical Success Factor:
**Students must leave feeling they've achieved mastery.** This is the end of foundation - they should feel confident about their ability to apply physics and math to automotive problems.

---

## ✅ Session Success Criteria

Students leave able to:
- ✓ Convert force to torque (τ = F × r)
- ✓ Calculate power from torque and speed
- ✓ Determine power requirements for any scenario
- ✓ Calculate 0-100 km/h time, top speed, gradeability
- ✓ Understand complete force → torque → power chain

**Most importantly:** Students understand that **vehicle performance is quantifiable** - not magic, not guesswork, but physics and mathematics they can apply.

**Emotional outcome:** Students should feel **empowered** and **confident** entering the next module. The hardest conceptual work is done.

---

**End of Framework - Foundation Module Complete**
**Next:** Template for remaining sessions + Example (Session 4: IC Engines)
