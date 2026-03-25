# Session 14: Vehicle Control Systems
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 90 minutes lecture + 30 minutes Q&A
**Approach:** Teacher-Led Narrative (System-Focused/Control Theory Introduction)
**PPT Target:** 28-30 slides

---

## 🎯 Session Objectives (For Instructor)

By the end of this session, students will be able to:

1. **Explain the role of Electronic Control Unit (ECU)** in modern vehicles and identify major ECU types
2. **Describe engine management ECU functions** (fuel control, ignition timing, air management, emissions)
3. **Classify automotive sensors** (temperature, pressure, position, speed, mass airflow, oxygen sensor) and explain their operation
4. **Classify automotive actuators** (fuel injectors, throttle valve, VVT solenoid, EGR valve) and explain their control
5. **Explain closed-loop control principle** in engine management (lambda/oxygen sensor feedback for air-fuel ratio control)
6. **Describe transmission control unit (TCU)** operation and automatic transmission shift control strategies

**Session Learning Outcomes (SO) Mapping:**
- AELZC441-SO-4-14-1 (Understand - Lecture)
- AELZC441-SO-4-14-2 (Understand - Lecture)
- AELZC441-SO-4-14-3 (Understand - Lecture)
- AELZC441-SO-4-14-4 (Understand - Lecture)
- AELZC441-SO-4-14-5 (Understand - Lecture)
- AELZC441-SO-4-14-6 (Understand - Lecture)

---

## 📚 Connection to Previous Sessions

**From Session 13 (Electrical Architecture):**
- We established the electrical foundation: 12V power, battery, alternator, distribution, protection
- We learned that modern vehicles have **30-100 ECUs** consuming ~50-80W total
- We saw that electrical power **enables** control systems

**Today's Focus:**
Now we explore **what those ECUs do** and **how they control** vehicle systems.

**The Shift from Mechanical to Electronic:**

**1960s Vehicle:**
- Carburetor (purely mechanical fuel delivery)
- Mechanical ignition (points and condenser)
- Manual transmission (driver controls everything)
- **Zero electronics** (except battery and generator)

**2025 Vehicle:**
- **30-100 ECUs** controlling every system
- **50-100 sensors** monitoring vehicle state
- **100+ actuators** executing commands
- **Sophisticated control algorithms** (PID control, fuzzy logic, machine learning)

**Why Electronic Control?**

**Precision:**
- Mechanical carburetor: ±20% air-fuel ratio tolerance
- Electronic fuel injection: ±1% air-fuel ratio accuracy
- **Result:** Better performance, lower emissions

**Adaptability:**
- Mechanical systems: Fixed operation (one setting for all conditions)
- Electronic systems: Adapt to altitude, temperature, load, driving style
- **Result:** Optimal operation in all conditions

**Integration:**
- Mechanical systems: Independent (brakes don't talk to engine)
- Electronic systems: Networked (ESC coordinates brakes, engine, transmission)
- **Result:** Advanced features (traction control, stability control)

**Today's Session:**
1. ECU fundamentals (what is an ECU, major types)
2. Sensors (eyes and ears—how ECUs sense the world)
3. Actuators (muscles—how ECUs control systems)
4. Closed-loop control (feedback and self-correction)
5. Engine management ECU (complete system integration example)
6. Transmission control (shift strategy example)

---

## 🎬 SESSION STORY ARC

### **PART 1: SETUP** - "The Electronic Brain" (Slides 1-7, ~15 min)
**Story Element:** Introduce ECU fundamentals and architecture
**Technical Content:** ECU definition, major types, hardware/software basics

### **PART 2: TRIGGER** - "Sensing the World" (Slides 8-15, ~25 min)
**Story Element:** Explore how ECUs gather information
**Technical Content:** Sensor types, operation principles, signal conditioning

### **PART 3: RISING ACTION** - "Acting on the World" (Slides 16-21, ~20 min)
**Story Element:** Show how ECUs control physical systems
**Technical Content:** Actuator types, PWM control, solenoids, motors

### **PART 4: CLIMAX** - "Closed-Loop Control" (Slides 22-26, ~20 min)
**Story Element:** Reveal the power of feedback control
**Technical Content:** Open vs closed loop, lambda control example, PID basics

### **PART 5: RESOLUTION** - "Complete System Integration" (Slides 27-30, ~10 min)
**Story Element:** Synthesize complete engine management + TCU example
**Technical Content:** System diagram, interaction examples, preview of networks

---

# PART 1: SETUP - "The Electronic Brain"
### (~15 minutes, Slides 1-7)

[Slides 1-7 would cover: Title slide, ECU fundamentals, major ECU types (engine, transmission, ABS/ESC, body control, ADAS), ECU hardware architecture, software basics, distributed control architecture]

---

# PART 2: TRIGGER - "Sensing the World"
### (~25 minutes, Slides 8-15)

## Slide 8: Automotive Sensors - Classification

**Visual:** Taxonomy diagram showing sensor types organized by measurement type

**Instructor Narration:**
"An ECU is useless without information. **Sensors** are the ECU's eyes and ears—they measure the physical world and convert it to electrical signals.

**SENSOR CLASSIFICATION:**

**By Measurement Type:**

**1. TEMPERATURE SENSORS**
- Measure: °C or °F
- Examples: Engine coolant temp, intake air temp, exhaust gas temp, cabin temp

**2. PRESSURE SENSORS**
- Measure: kPa, bar, psi
- Examples: Manifold absolute pressure (MAP), tire pressure (TPMS), fuel pressure, brake pressure

**3. POSITION SENSORS**
- Measure: Angle or linear position (degrees, mm)
- Examples: Throttle position, camshaft position, crankshaft position, pedal position

**4. SPEED SENSORS**
- Measure: RPM or km/h
- Examples: Wheel speed (ABS), vehicle speed, engine speed (tachometer)

**5. FLOW SENSORS**
- Measure: kg/s or L/min
- Examples: Mass airflow (MAF), fuel flow

**6. COMPOSITION SENSORS**
- Measure: Chemical composition (%)
- Examples: Oxygen sensor (lambda), NOx sensor

**By Signal Type:**

**ANALOG SENSORS:**
- Output: Continuous voltage (0-5V typical) or resistance
- Example: Coolant temperature sensor (resistance decreases with temperature)
- ECU reads via analog-to-digital converter (ADC)

**DIGITAL SENSORS:**
- Output: On/off signal or pulse train
- Example: Crankshaft position sensor (digital pulses)
- ECU counts pulses directly

**SMART SENSORS:**
- Output: Digital data over serial communication (CAN, LIN)
- Example: Tire pressure monitoring sensor (transmits pressure + temperature + ID)
- Most advanced, least susceptible to noise

Let's explore each major sensor type in detail."

---

## Slide 9: Temperature Sensors - Thermistors (NTC)

**Visual:** Cutaway of thermistor sensor, resistance vs temperature graph

**Instructor Narration:**
"Temperature is fundamental—engines, transmissions, everything has optimal operating temperature.

**NTC THERMISTOR (Negative Temperature Coefficient)**

**Technology:**
- Semiconductor material (metal oxide ceramic)
- Resistance **decreases** as temperature **increases**
- Non-linear relationship

**Typical Characteristics:**

**At 25°C:** 2,500 Ω (2.5 kΩ)
**At 80°C:** 300 Ω
**At 100°C:** 180 Ω

**How ECU Measures:**

**Circuit:**
1. ECU supplies **5V reference voltage**
2. Voltage divider: 5V → Fixed Resistor (2.5 kΩ) → Thermistor → Ground
3. ECU measures voltage at junction
4. Voltage changes as thermistor resistance changes

**Calculation:**
```
V_sensor = 5V × (R_thermistor / (R_fixed + R_thermistor))
```

**Example:**
- Engine cold (20°C): R_thermistor = 3,000 Ω
  - V_sensor = 5V × (3,000 / 5,500) = 2.73V
  - ECU interprets: **20°C**

- Engine hot (90°C): R_thermistor = 250 Ω
  - V_sensor = 5V × (250 / 2,750) = 0.45V
  - ECU interprets: **90°C**

**Applications:**

**1. Engine Coolant Temperature (ECT)**
- Location: Thermostat housing or cylinder head
- Purpose:
  - Cold start enrichment (add fuel when cold)
  - Cooling fan control (turn on at 95°C)
  - Fuel trim adjustment (density changes with temperature)

**2. Intake Air Temperature (IAT)**
- Location: Intake manifold or air filter housing
- Purpose:
  - Air density calculation (cold air denser = more oxygen)
  - Fuel adjustment (more air = need more fuel)
  - Knock protection (hot air more prone to detonation)

**3. Transmission Fluid Temperature (TFT)**
- Location: Transmission oil pan
- Purpose:
  - Shift strategy adjustment (firm shifts when hot)
  - Overheating protection (lock torque converter, reduce load)

**Advantages:**
✅ Simple, cheap ($5-15)
✅ No external power needed
✅ Very reliable (no moving parts)

**Disadvantages:**
❌ Non-linear (requires lookup table in ECU)
❌ Slow response (thermal mass takes time to heat/cool)

**Instructor Narration (continued):**
'When your engine runs cold for too long (stuck-open thermostat), the ECU sees low coolant temperature and enriches the fuel mixture. Result: poor fuel economy, high emissions, rough running. The ECU is responding correctly to bad sensor data—the problem is the thermostat, not the ECU!'"

---

## Slide 10-15: Other Sensor Types (Summarized)

[These slides would cover:
- Slide 10: Pressure sensors (piezo-resistive, capacitive) - MAP sensor
- Slide 11: Position sensors (potentiometer, Hall effect) - TPS, pedal position
- Slide 12: Speed sensors (inductive, Hall effect) - Crankshaft, camshaft, wheel speed
- Slide 13: Mass airflow sensor (hot-wire, hot-film) - Critical for fuel calculation
- Slide 14: Oxygen sensor (lambda sensor) - Zirconia, wide-band vs narrow-band
- Slide 15: Sensor summary table comparing all types]

---

# PART 3: RISING ACTION - "Acting on the World"
### (~20 minutes, Slides 16-21)

## Slide 16: Automotive Actuators - Classification

**Visual:** Diagram showing various actuator types organized by function

**Instructor Narration:**
"Sensors measure the world; **actuators** change it. These are the ECU's muscles.

**ACTUATOR CLASSIFICATION:**

**By Type:**

**1. SOLENOIDS (Electromagnetic Actuators)**
- Convert electrical current → linear or rotary motion
- Examples: Fuel injectors, transmission shift solenoids, VVT solenoids, purge valve

**2. ELECTRIC MOTORS**
- Convert electrical power → rotary motion
- Examples: Throttle valve motor, EPAS motor, cooling fan, fuel pump

**3. STEPPER MOTORS**
- Precise rotary positioning
- Examples: Idle air control valve, cruise control throttle

**4. RELAYS**
- Electrically controlled switches (we covered in Session 13)
- Examples: Fuel pump relay, cooling fan relay, A/C compressor clutch

**By Control Method:**

**ON/OFF (Bang-Bang Control)**
- Actuator is either fully on or fully off
- Example: Cooling fan relay (on when temp > 95°C, off when < 90°C)

**PWM (Pulse Width Modulation)**
- Vary average power by rapidly switching on/off
- Example: Fuel injector (pulse width determines fuel quantity)

**ANALOG (Continuous Control)**
- Smoothly variable output
- Example: Throttle motor position (precise angle control)

Let's explore key actuators."

---

## Slide 17: Fuel Injectors - PWM Control

**Visual:** Cutaway of fuel injector showing solenoid coil, plunger, nozzle, spray pattern

**Instructor Narration:**
"The fuel injector is the most critical actuator for engine control.

**FUEL INJECTOR DESIGN:**

**Components:**

**1. Solenoid Coil**
- Electromagnetic coil (many turns of fine wire)
- Typical: 2-5 Ω resistance, 12V supply
- When energized: Creates magnetic field

**2. Plunger (Armature)**
- Movable iron core
- Held closed by spring
- Pulled open by magnetic field

**3. Nozzle & Spray Pattern**
- Precision-machined orifice
- Creates fine fuel mist (atomization)
- Spray pattern optimized for combustion chamber shape

**4. Fuel Supply**
- Constant pressure fuel rail (typically 300-400 kPa / 43-58 psi)
- Fuel always present, ready to inject

---

**HOW IT WORKS:**

**Injector Closed (De-energized):**
- No current through coil
- Spring holds plunger closed
- Fuel blocked (no flow)

**Injector Open (Energized):**
1. ECU sends current pulse to solenoid (12V)
2. Magnetic field pulls plunger open
3. Fuel sprays through nozzle (pressure differential)
4. Atomized fuel mixes with air

**Injector Closes:**
1. ECU cuts current
2. Magnetic field collapses
3. Spring forces plunger closed
4. Fuel flow stops

**Response Time:** 1-2 milliseconds (open/close cycle)

---

**PWM CONTROL - PULSE WIDTH MODULATION:**

**Concept:** Control fuel quantity by varying **how long** injector stays open

**Key Parameters:**

**Pulse Width (Injection Duration):**
- Measured in milliseconds (ms)
- Typical range: 1-15 ms
- Longer pulse = more fuel

**Fuel Quantity Formula:**
```
Fuel Mass = Fuel Pressure × Injector Flow Rate × Pulse Width

Or simplified:
Fuel (mg) ≈ K × Pulse Width (ms)

Where K = injector flow coefficient (depends on pressure, nozzle size)
```

**Example:**
- Injector flow rate: 200 cc/min @ 300 kPa
- Pulse width: 3 ms
- Fuel delivered: ~10 mg per pulse

**Operating Conditions:**

**Idle:**
- Low air mass → need low fuel
- Pulse width: 2-3 ms
- Frequency: ~25 pulses/sec (engine at 750 RPM, 4-cylinder, 4-stroke)

**Full Load (Wide Open Throttle):**
- High air mass → need high fuel
- Pulse width: 10-15 ms
- Frequency: ~100 pulses/sec (engine at 6,000 RPM)

**Cold Start:**
- Cold engine → poor fuel vaporization
- Need extra fuel (enrichment)
- Pulse width: +50-100% longer than normal

---

**MULTI-POINT FUEL INJECTION (MPFI) vs DIRECT INJECTION (GDI):**

**Port Injection (MPFI):**
- Injector sprays into **intake port** (before intake valve)
- Fuel mixes with air in port
- Enters cylinder already mixed
- Pressure: 300-400 kPa

**Direct Injection (GDI):**
- Injector sprays directly into **combustion chamber**
- Much higher pressure: 10,000-35,000 kPa (100-350 bar)
- More precise control (inject during compression stroke)
- Better efficiency, more power

**Instructor Narration (continued):**
'PWM control is everywhere in automotive systems—not just fuel injectors. Variable valve timing solenoids, transmission shift solenoids, EVAP purge valve—all use PWM. The ECU rapidly switches them on/off, and the average (duty cycle) determines the effect. It's digital control of analog systems.'"

---

## Slide 18-21: Other Actuator Types (Summarized)

[These slides would cover:
- Slide 18: Electronic throttle (drive-by-wire) - DC motor, position feedback
- Slide 19: VVT solenoid (variable valve timing) - Oil pressure control
- Slide 20: EGR valve (exhaust gas recirculation) - Stepper motor control
- Slide 21: Transmission shift solenoids - Hydraulic pressure PWM control]

---

# PART 4: CLIMAX - "Closed-Loop Control"
### (~20 minutes, Slides 22-26)

## Slide 22: Open-Loop vs Closed-Loop Control

**Visual:** Two diagrams side-by-side showing control flow

**Instructor Narration:**
"We've seen sensors (measurement) and actuators (control). Now let's see how they work **together** in **control loops**.

**OPEN-LOOP CONTROL (No Feedback)**

**Definition:** ECU commands actuator based on **pre-programmed map**, without measuring the result.

**Example: Cold Start Fuel Enrichment (Simplified)**

**Process:**
1. ECU reads coolant temperature sensor: **5°C**
2. ECU looks up fuel enrichment table:
   - At 5°C → enrich by +40%
3. ECU increases injector pulse width by 40%
4. **No measurement of actual air-fuel ratio**

**Diagram:**
```
[Coolant Temp Sensor] → [ECU] → [Fuel Injector]
                          ↑
                    [Lookup Table]
```

**Advantages:**
✅ Simple (no feedback sensor needed)
✅ Fast (no time delay for feedback)

**Disadvantages:**
❌ Inaccurate (assumes table is correct for all conditions)
❌ No error correction (if actual AFR is wrong, ECU doesn't know)
❌ Cannot adapt (altitude, fuel quality, aging components affect result)

---

**CLOSED-LOOP CONTROL (With Feedback)**

**Definition:** ECU commands actuator, **measures the result**, compares to target, and **corrects errors**.

**Example: Lambda Control (Air-Fuel Ratio Control)**

**Process:**
1. ECU calculates target AFR: **14.7:1** (stoichiometric)
2. ECU calculates required fuel based on air mass (from MAF sensor)
3. ECU commands fuel injector
4. **Oxygen sensor measures actual AFR** in exhaust
5. ECU compares: Actual vs Target
6. **If actual ≠ target:** ECU adjusts fuel injection
7. Repeat continuously (closed loop)

**Diagram:**
```
[Target AFR] → [ECU] → [Fuel Injector] → [Engine] → [Exhaust]
                ↑                                        ↓
                ←──────── [Oxygen Sensor] ←──────────────
                       (Feedback)
```

**Advantages:**
✅ **Accurate** (measures actual result, corrects errors)
✅ **Adaptive** (compensates for altitude, fuel quality, aging)
✅ **Self-correcting** (if something drifts, feedback compensates)

**Disadvantages:**
❌ Requires feedback sensor (cost)
❌ Slower (feedback delay)
❌ Can oscillate if tuned incorrectly

---

**WHEN TO USE EACH:**

**Open-Loop:**
- Cold start (before oxygen sensor warms up)
- Transient conditions (rapid throttle changes—feedback too slow)
- Fail-safe mode (if feedback sensor fails)

**Closed-Loop:**
- Normal operation (cruising, steady-state)
- Emissions-critical operation (catalyst requires precise AFR)
- Long-term adaptation (learn fuel system aging)

**Instructor Narration (continued):**
'Modern engine management uses **both**. During cold start, open-loop enriches fuel (no O2 sensor yet). After 30-60 seconds, oxygen sensor warms up, ECU switches to closed-loop, measures actual AFR, and trims fuel precisely to 14.7:1. This is why emissions are high for the first minute after starting—no closed-loop yet.'"

---

## Slide 23: Lambda Control - The Perfect Air-Fuel Ratio

**Visual:** Diagram showing lambda control loop with MAF sensor, injectors, oxygen sensor, and ECU

**Instructor Narration:**
"Let's dive deep into the most important closed-loop control in engine management: **Lambda Control** (air-fuel ratio control).

**THE GOAL: STOICHIOMETRIC COMBUSTION**

**Chemistry:**
```
Gasoline (C8H18) + Air (21% O2, 79% N2) → CO2 + H2O + Heat

Stoichiometric Ratio:
14.7 kg of air : 1 kg of fuel (mass ratio)

Lambda (λ) = Actual AFR / Stoichiometric AFR

λ = 1.0 → Perfect mixture (14.7:1)
λ > 1.0 → Lean (excess air, AFR > 14.7:1)
λ < 1.0 → Rich (excess fuel, AFR < 14.7:1)
```

**Why λ = 1.0 Matters:**

**Three-Way Catalytic Converter REQUIRES λ = 1.0 ± 0.01**

At λ = 1.0:
✅ CO oxidized to CO2 (requires oxygen)
✅ HC oxidized to CO2 + H2O (requires oxygen)
✅ NOx reduced to N2 (requires reducing agent—excess fuel)

**Catalyst Efficiency:**
- λ = 1.00: **95-99% conversion** (excellent)
- λ = 0.95: **60% NOx conversion** (too rich)
- λ = 1.05: **40% CO conversion** (too lean)

**Emissions regulations (BS6, Euro 6) demand λ = 1.00 ± 0.01**

---

**LAMBDA CONTROL SYSTEM:**

**Components:**

**1. Mass Airflow Sensor (MAF)**
- Measures: kg/s of air entering engine
- Technology: Hot-wire sensor (air cools wire, resistance changes)
- Output: 0-5V analog (proportional to airflow)

**Example:**
- At idle: 3 g/s (0.003 kg/s)
- At full load: 150 g/s (0.150 kg/s)

**2. Engine Control ECU**
- Calculates required fuel mass:
  ```
  Fuel Mass = Air Mass / 14.7
  ```
- Calculates injector pulse width:
  ```
  Pulse Width = Fuel Mass / Injector Flow Rate
  ```

**3. Fuel Injector**
- Delivers calculated fuel mass
- Response time: 1-2 ms

**4. Oxygen Sensor (Lambda Sensor)**
- Measures: Oxygen content in exhaust gas
- Technology: Zirconia ceramic (generates voltage based on O2 concentration)
- Output: 0-1V (0.45V = lean, 0.55V = rich, 0.5V = stoich)

**Two Types:**

**Narrow-Band Oxygen Sensor (Switch Type):**
- Output: Sharp transition at λ = 1.0
- Range: Can only detect λ = 0.95-1.05 (narrow window)
- **Cannot measure HOW rich or lean**, only "rich" or "lean"
- Cheap ($30-80)

**Wide-Band Oxygen Sensor (Linear Type):**
- Output: Linear voltage proportional to λ
- Range: λ = 0.65-1.3 (wide range)
- **CAN measure exact AFR** (12:1, 14.7:1, 16:1, etc.)
- Expensive ($150-400)
- Used in performance applications, diesel engines

---

**CLOSED-LOOP OPERATION:**

**Step 1: Open-Loop Calculation**

**Given:**
- MAF sensor: 10 g/s airflow
- Target: λ = 1.0 (AFR = 14.7:1)

**Calculate fuel needed:**
```
Fuel = Air / AFR = 10 g/s / 14.7 = 0.68 g/s
```

**Convert to injector pulse width:**
```
Injector flow rate: 200 cc/min = 160 mg/stroke @ 300 kPa
Pulse width = (0.68 g/s / 4 cylinders) / (160 mg/stroke) × 1000
            = ~4.25 ms per injection
```

**Step 2: ECU Commands Injector**
- Pulse width: 4.25 ms
- Fuel sprays, combustion occurs

**Step 3: Oxygen Sensor Measures**
- Exhaust reaches O2 sensor (~500 ms delay)
- O2 sensor voltage: 0.52V

**Interpretation:**
- 0.52V > 0.50V → **Slightly rich** (too much fuel)
- Actual λ ≈ 0.98 (slightly rich)

**Step 4: ECU Corrects**
- ECU reduces pulse width: 4.25 ms → 4.20 ms (-1.2%)
- Less fuel injected

**Step 5: Repeat**
- O2 sensor measures again (after 500 ms)
- Voltage: 0.48V → **Slightly lean**
- ECU increases pulse width: 4.20 ms → 4.23 ms
- Repeat continuously (oscillates around λ = 1.0)

---

**CONTROL FREQUENCY:**

**Update Rate:**
- ECU recalculates every **10-50 ms**
- O2 sensor feedback delay: **200-500 ms** (exhaust travel time)
- System oscillates ± 2% around λ = 1.0
- **Average λ = 1.00** over time

**Result:**
- Catalyst sees average λ = 1.00
- **95-99% emissions conversion**
- Meets BS6/Euro 6 standards

**Instructor Narration (continued):**
'This is why catalytic converters fail if you have persistent misfires or run too rich/lean for extended periods. The catalyst is designed for λ = 1.0. If you run at λ = 0.8 (very rich—maybe due to bad MAF sensor), the catalyst sees excess fuel, overheats, and the ceramic substrate melts. A $50 sensor failure leads to a $1,500 catalyst replacement!'"

---

## Slide 24-26: PID Control & Other Examples

[These slides would cover:
- Slide 24: PID control basics (Proportional-Integral-Derivative)
- Slide 25: Idle speed control example (closed-loop)
- Slide 26: Knock control example (closed-loop timing adjustment)]

---

# PART 5: RESOLUTION - "Complete System Integration"
### (~10 minutes, Slides 27-30)

## Slide 27: Engine Management ECU - Complete System

**Visual:** Comprehensive diagram showing ECU with all sensors (inputs) and actuators (outputs)

**Instructor Narration:**
"Let's integrate everything: sensors, actuators, and control loops into a complete **Engine Management System**.

**ENGINE CONTROL ECU (ECM/PCM)**

**INPUTS (Sensors):**

**Air System:**
- Mass Airflow Sensor (MAF): Air mass (kg/s)
- Intake Air Temperature (IAT): Air density correction
- Manifold Absolute Pressure (MAP): Load indication (some systems use MAP instead of MAF)
- Throttle Position Sensor (TPS): Driver demand

**Fuel System:**
- Oxygen Sensor (O2/Lambda): Exhaust gas O2 (closed-loop feedback)
- Fuel Pressure Sensor: Rail pressure monitoring
- Fuel Temperature Sensor: Density correction

**Ignition System:**
- Crankshaft Position Sensor (CKP): Engine speed, TDC position
- Camshaft Position Sensor (CMP): Cylinder identification, valve timing
- Knock Sensor: Detonation detection (piezoelectric accelerometer)

**Cooling System:**
- Engine Coolant Temperature (ECT): Cold start, fan control, fuel trim

**Driver Inputs:**
- Accelerator Pedal Position: Driver torque request
- Brake Switch: Decel fuel cut, idle control
- Cruise Control Switches: Target speed

**Other:**
- Vehicle Speed Sensor (VSS): Transmission control, cruise control
- Battery Voltage: Charging system status
- A/C Request: Load compensation (increase idle speed)

---

**OUTPUTS (Actuators):**

**Fuel System:**
- Fuel Injectors (4-12 depending on cylinders): Precise fuel metering (PWM, 1-15 ms pulse)
- Fuel Pump Relay: Prime fuel system, maintain pressure

**Ignition System:**
- Ignition Coils (one per cylinder): Spark timing (0-40° BTDC typically)
- Ignition timing advance/retard based on load, speed, knock

**Air System:**
- Electronic Throttle Valve (Drive-by-wire): Throttle opening (0-90°)
- Idle Air Control Valve: Idle speed regulation (bypass air)
- VVT Solenoids: Variable valve timing (intake/exhaust cam phasing)

**Emissions:**
- EGR Valve: Exhaust gas recirculation (reduce NOx)
- Purge Valve: Evaporative emissions control (EVAP system)
- Secondary Air Pump: Catalyst warm-up (cold start)

**Other:**
- Cooling Fan Relay: Engine temperature control
- Check Engine Light (MIL): Fault indication
- Tachometer Signal: RPM display

---

**CONTROL STRATEGIES:**

**1. Base Fuel Calculation (Open-Loop):**
```
Base Fuel = MAF (kg/s) / 14.7 (AFR) / Engine Speed (rev/s) / Cylinders
```

**2. Fuel Trims (Closed-Loop):**
```
Final Fuel = Base Fuel × Short-Term Trim × Long-Term Trim

Short-Term Trim: Immediate correction based on O2 sensor (±25%)
Long-Term Trim: Learned compensation (±15-25%, stored in ECU memory)
```

**3. Ignition Timing:**
```
Base Timing = Lookup Table [Engine Speed, Load]
Final Timing = Base Timing - Knock Retard + Coolant Compensation
```

**4. Idle Speed Control:**
```
Target Idle = 700 RPM (warm), 1,200 RPM (cold)
Idle Air Valve Opening = PID(Target RPM - Actual RPM)
```

**All These Run Simultaneously:**
- Fuel calculation: Every 5-10 ms
- Ignition timing: Every cylinder firing (every 10-20 ms @ 3,000 RPM)
- Idle control: Every 50-100 ms
- Lambda control: Every 200-500 ms
- Fault detection: Continuous

**ECU Processing:**
- Processor: 32-bit, 100-200 MHz
- Memory: 512 KB - 4 MB Flash, 128 KB RAM
- I/O: 50-100 inputs/outputs
- Power: 5-10W

**Instructor Narration (continued):**
'The engine ECU is one of the most complex computers in the vehicle. It's executing thousands of calculations per second, managing 50+ sensors and actuators, all while ensuring emissions compliance, driveability, and reliability. And it must work flawlessly for 200,000+ km in extreme conditions—from -40°C to +125°C, vibration, humidity, everything. It's an engineering marvel.'"

---

## Slide 28: Transmission Control Unit (TCU) - Shift Strategy

**Visual:** TCU diagram showing inputs (vehicle speed, throttle, engine speed) and outputs (shift solenoids)

**Instructor Narration:**
"Let's look at another major ECU: the **Transmission Control Unit** (TCU or TCM).

**TCU FUNCTION:**
Control automatic transmission shifting to optimize:
- Performance (fast shifts when driver demands)
- Fuel economy (early upshifts for cruising)
- Smoothness (gentle shifts for comfort)

**INPUTS:**

**From Sensors:**
- **Vehicle Speed Sensor (VSS):** km/h
- **Turbine Speed Sensor:** Transmission input speed (RPM)
- **Output Shaft Speed Sensor:** Transmission output speed (RPM)
- **Throttle Position Sensor (TPS):** Driver demand (% throttle)
- **Accelerator Pedal Position:** Driver intent
- **Brake Switch:** Deceleration indication
- **Transmission Fluid Temperature (TFT):** Fluid condition
- **Gear Position Sensor:** Current gear (P/R/N/D/S/L)

**From Engine ECU (via CAN bus):**
- **Engine RPM**
- **Engine Torque**
- **Engine Load**

**From Driver:**
- **Transmission Mode Selection:** Drive, Sport, Manual, Eco

---

**OUTPUTS:**

**Shift Solenoids (Hydraulic Valves):**
- **Solenoid A, B, C, D, E:** Control hydraulic circuits
- Each gear = unique solenoid combination
- Example (4-speed auto):
  - 1st gear: A=ON, B=OFF, C=OFF
  - 2nd gear: A=ON, B=ON, C=OFF
  - 3rd gear: A=OFF, B=ON, C=ON
  - 4th gear: A=OFF, B=OFF, C=ON

**Pressure Control Solenoids:**
- **Line Pressure Control:** Overall hydraulic pressure (PWM control)
- **Clutch Pressure Control:** Individual clutch engagement force (smooth shifts)

**Torque Converter Lock-Up Clutch:**
- **Lock solenoid:** Engage/disengage lock-up (eliminate slip, improve efficiency)

**Other:**
- **Gear Position Indicator:** Display current gear (dashboard)
- **Shift Lock Solenoid:** Prevent shifting out of Park without brake

---

**SHIFT STRATEGY (Example: 2→3 Upshift):**

**Shift Decision:**

**Inputs:**
- Vehicle speed: 60 km/h
- Throttle position: 30% (light acceleration)
- Engine RPM: 2,500 RPM (in 2nd gear)
- Transmission mode: Drive (D)

**TCU Logic:**

**Step 1: Lookup Shift Map**
```
Shift Map [Throttle Position, Vehicle Speed]

At 30% throttle, 60 km/h → Shift point = 2→3 upshift
```

**Step 2: Check Conditions**
- Transmission fluid temp: 80°C ✅ (OK, not too cold)
- Engine torque: Normal ✅ (no wide-open throttle)
- Brake not applied ✅

**Step 3: Execute Shift**

**Pre-shift (100 ms before):**
1. TCU requests engine ECU: "Reduce torque by 20%"
2. Engine ECU retards ignition timing → torque reduction
3. Result: Smooth shift (no jerk)

**During shift (300-500 ms):**
1. De-energize 2nd gear solenoid
2. Energize 3rd gear solenoid (overlap for smoothness)
3. Modulate clutch pressure (PWM control):
   - Gradual release of 2nd gear clutch
   - Gradual engagement of 3rd gear clutch
   - Clutch slip controlled to 50-200 RPM during transition

**Post-shift:**
1. TCU signals engine ECU: "Restore full torque"
2. Engine ECU returns to normal ignition timing
3. RPM drops from 2,500 to 1,800 RPM (typical gear ratio change)
4. Shift complete

**Shift Quality Metrics:**
- Shift time: 300-500 ms (smooth), 100-200 ms (sport mode)
- Clutch slip during shift: 50-200 RPM (controlled)
- Torque reduction: 10-30% (minimizes jerk)

---

**ADAPTIVE LEARNING:**

Modern TCUs **learn** over time:

**Clutch Wear Compensation:**
- As clutches wear, apply pressure slightly earlier
- Maintain consistent shift quality over 200,000 km

**Driver Style Recognition:**
- Aggressive driver (frequent WOT) → hold gears longer, firmer shifts
- Gentle driver (light throttle) → early upshifts, softer shifts

**Temperature Compensation:**
- Cold fluid (-10°C) → delay shifts (fluid viscosity high)
- Hot fluid (110°C) → firmer shifts, lock torque converter early (protect transmission)

**Instructor Narration (continued):**
'This is why transmission 'relearning' is a thing. If you disconnect the battery, the TCU loses its adaptive parameters. For the first 100-200 km after reconnecting, shifts may feel slightly different while the TCU relearns. Also, if you sell your car to someone with a different driving style, the transmission will adapt to the new driver over a week or two—automatic customization!'"

---

## Slide 29-30: Summary & Preview

[Slides 29-30 would cover:
- Slide 29: Complete integration—how engine ECU, TCU, ABS ECU all work together (preview of networks in Session 15)
- Slide 30: Summary of Session 14, preview of Session 15 (CAN bus, OBD-II, network architecture)]

---

## 📊 SESSION METADATA

**Total Slides:** 28-30
**Lecture Duration:** 90 minutes
**Q&A Duration:** 30 minutes

**Learning Outcome Coverage:**
- ✅ SO-4-14-1: ECU role and types (Slides 1-7)
- ✅ SO-4-14-2: Engine management ECU functions (Slide 27)
- ✅ SO-4-14-3: Sensor classification and operation (Slides 8-15)
- ✅ SO-4-14-4: Actuator classification and control (Slides 16-21)
- ✅ SO-4-14-5: Closed-loop control principle (Slides 22-26)
- ✅ SO-4-14-6: TCU operation and shift strategies (Slide 28)

**Key Concepts:**
1. Sensors (NTC thermistor, MAF, O2 sensor) convert physical → electrical
2. Actuators (injectors, throttle, solenoids) convert electrical → physical
3. ECUs implement control algorithms (open/closed loop)
4. Closed-loop control uses feedback for accuracy (lambda control example)
5. Modern vehicles have 30-100 ECUs working together

---

**END OF SESSION 14 FRAMEWORK**

*This framework is ready for PowerPoint conversion.*
