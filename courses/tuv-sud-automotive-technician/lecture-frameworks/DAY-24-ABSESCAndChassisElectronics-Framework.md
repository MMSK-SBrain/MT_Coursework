---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 5
week_title: "Grip, Turn & Stop — Chassis & Brakes"
day_number: 24
session_title: "ABS, ESC & Chassis Electronics"
duration_minutes: 180
theory_practice: "40:60"
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 24: ABS, ESC & Chassis Electronics
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (70 min theory + 110 min practical)
**Approach:** Layered Build — From Sensor Signal to Vehicle Stability
**PPT Target:** 26-28 slides
**Week:** 5 of 8 — "Grip, Turn & Stop — Chassis & Brakes"

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Explain how ABS prevents wheel lock-up while maintaining steering control during hard braking
- Describe the three ABS pressure control phases: build, hold, and reduce
- Differentiate between passive (inductive) and active (Hall effect) wheel speed sensors and their signal characteristics
- Identify the components of the ABS hydraulic modulator (solenoid valves, pump motor, accumulator)
- Explain how ESC/ESP compares driver intent to actual vehicle behavior using yaw rate, lateral acceleration, and steering angle sensors
- Describe how ESC corrects oversteer and understeer by selectively braking individual wheels
- Explain traction control (TCS) and how it shares ABS hardware to prevent wheelspin during acceleration
- Read ABS/ESC fault codes (C-codes) and live data using a scan tool

**This is Day 24 — Week 5, Day 4.** Learners completed the mechanical brake system yesterday (Day 23). Today adds the electronic layer that controls those brakes at speeds far beyond human reaction time. Connect constantly to the physical hardware they already know.

---

## Connection to Prior Knowledge

Build directly from:
- **Day 23 (Mechanical Brakes):** Hydraulic circuit, master cylinder, calipers, pads, rotors, brake fluid — the physical foundation that ABS modulates
- **Day 21 (Suspension & Vehicle Dynamics):** Weight transfer, tyre contact patch, slip angle, friction circle — ABS manages longitudinal grip, ESC manages lateral grip
- **Day 22 (Steering Systems):** Steering angle sensor already introduced — today it becomes a critical ESC input
- **Week 2 (Electrical Fundamentals):** Sensor types, signal reading, ECU concepts, CAN bus communication

**Bridge:** "Yesterday you traced the path from brake pedal to wheel — hydraulic pressure, friction, heat. But what happens when you slam the pedal on a wet road? The wheels lock. You slide. You can't steer. Today we meet the electronic brain that intervenes 50 times per second to prevent that — and keeps you pointed where you want to go, even when physics says otherwise."

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: From Mechanical to Electronic Braking** (Slides 1-3, ~10 minutes)

**Narrative Voice:** Direct, dramatic. Remind them of yesterday's mechanical system, then reveal the limitation that demanded electronics.

---

#### Slide 1: Title & Context
**Visual:** Split image — left side shows a locked wheel leaving a black tyre mark on wet asphalt; right side shows an ABS-equipped wheel leaving intermittent marks with the vehicle maintaining its line through a curve

**Instructor Narration:**
> "Yesterday you built a complete mental model of the brake system — pedal, booster, master cylinder, lines, calipers, pads, rotors. And it works brilliantly. Until it doesn't. Look at this photo. Left side: locked wheel, full skid, driver has lost all steering. Right side: ABS-controlled braking, the wheel keeps turning, the driver can still steer around the obstacle. Same road, same speed, same panic stop. The difference? Electronics. And that's what today is about."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 5: Grip, Turn & Stop — Chassis & Brakes
Day 24: ABS, ESC & Chassis Electronics

Yesterday: the pedal-to-wheel mechanical chain.
Today: the ECU that controls it all — 50+ times per second.
```

---

#### Slide 2: Why Mechanical Brakes Need Electronics
**Visual:** Diagram showing the friction circle from Day 21, with annotations: "100% braking force = 0% steering force" at the top of the circle, and a safe zone showing combined braking + steering inside the circle

**Instructor Narration:**
> "Remember the friction circle from Day 21? A tyre has a fixed budget of grip. You can spend it all on braking, or all on cornering, or a blend of both — but you cannot exceed the total. When a wheel locks up, it's using ALL its grip in the braking direction — sliding, not rolling. That means zero grip left for steering. The driver turns the wheel, nothing happens. The car goes straight — into whatever is in front of it.
>
> ABS exists to solve this problem. It keeps each wheel just below the lock-up point — maximum braking force while preserving enough grip to steer. It does this by pulsing the brake pressure on each wheel individually, dozens of times per second. Faster than any human could ever pump the pedal."

**PPT Content:**
```
WHY MECHANICAL BRAKES NEED ELECTRONICS

The Problem:
• Maximum braking force occurs just BEFORE wheel lock-up
• A locked wheel has LESS braking force (sliding friction < rolling friction)
• A locked wheel has ZERO steering capability

The Consequence:
• Driver brakes hard → wheel locks → car slides uncontrolled
• Especially dangerous on wet, icy, or uneven surfaces

The Solution — ABS:
• Monitors each wheel's speed individually
• Detects when a wheel is about to lock
• Reduces brake pressure on THAT wheel instantly
• Restores pressure when wheel recovers
• Cycles 15-50 times per second per wheel

Link to Day 21: ABS manages LONGITUDINAL grip (braking direction)
```

---

#### Slide 3: Today's Plan
**Visual:** Horizontal timeline of the 180-minute session — four blocks with clock icons

**Instructor Narration:**
> "Here's our plan. First block: ABS deep dive — the sensors that measure wheel speed, the hydraulic modulator that controls pressure, and the ECU logic that decides what to do. Second block: ESC and traction control — the additional sensors and the higher-level intelligence that keeps the whole vehicle stable. Third and largest block: practical work — you'll find wheel speed sensors on a real vehicle, test them with a multimeter and oscilloscope, and read ABS/ESC live data and fault codes on the scan tool. We finish with a wrap-up connecting everything back to the chassis system."

**PPT Content:**
```
TODAY'S PLAN (180 minutes)

BLOCK 1 (35 min): ABS Deep Dive
— Wheel speed sensors, hydraulic modulator, ECU control logic

BLOCK 2 (25 min): ESC, Traction Control & Advanced Stability
— Yaw rate, lateral G, steering angle — oversteer/understeer correction

PRACTICAL (80 min): Hands-On Chassis Electronics
— Identify & test wheel speed sensors
— Read ABS/ESC live data and fault codes on scan tool

WRAP-UP (15 min): Consolidation & Day 25 preview

+ Connect back to Day 21 vehicle dynamics & Day 23 mechanical brakes
```

---

### **DEVELOPMENT PART 1: ABS Deep Dive** (Slides 4-14, ~35 minutes)

**Narrative Voice:** Technical and methodical. Build the system layer by layer — sensors first, then the hydraulic modulator, then the ECU logic that ties them together.

---

#### Slide 4: ABS System Overview — The Three Pillars
**Visual:** Block diagram showing the ABS system: four wheel speed sensors feeding into the ABS ECU, which controls the hydraulic modulator, which connects to the four brake calipers. Arrows show signal flow (sensors to ECU) and hydraulic flow (modulator to calipers)

**Instructor Narration:**
> "ABS is built on three pillars. First: sensing — four wheel speed sensors, one at each wheel, constantly reporting how fast each wheel is turning. Second: processing — the ABS ECU, which compares those four speeds, detects when any wheel is decelerating faster than the vehicle, and decides what to do. Third: acting — the hydraulic modulator, which sits between the master cylinder and the brake calipers, and can independently increase, hold, or decrease brake pressure at each wheel.
>
> Sense, decide, act. That's every electronic control system in the car, and ABS was one of the first to use this pattern. Bosch introduced it in 1978. By the mid-2000s, it was mandatory in Europe."

**PPT Content:**
```
ABS — THE THREE PILLARS

1. SENSE — Wheel Speed Sensors (x4)
   • One per wheel
   • Report individual wheel rotational speed to ECU
   • Detect when a wheel is about to lock

2. DECIDE — ABS ECU (Electronic Control Unit)
   • Compares 4 wheel speeds continuously
   • Calculates vehicle reference speed
   • Detects individual wheel deceleration anomalies
   • Determines required pressure action per wheel

3. ACT — Hydraulic Modulator
   • Sits between master cylinder and wheel brakes
   • Contains solenoid valves (intake + exhaust per channel)
   • Contains electric pump motor & accumulator
   • Can independently control pressure at each wheel

History: First production ABS — Bosch, 1978 (Mercedes S-Class)
EU mandatory: 2004 (cars), 2016 (all new vehicles)
```

---

#### Slide 5: Wheel Speed Sensors — Passive (Inductive) Type
**Visual:** Cutaway diagram of a passive wheel speed sensor: permanent magnet core wrapped in a coil, mounted close to a ferromagnetic tone ring (toothed reluctor ring) on the hub or CV joint. Show the air gap between sensor tip and tone ring teeth

**Instructor Narration:**
> "Let's start with sensing. The passive or inductive wheel speed sensor is the older type — you'll still find them on many vehicles. It's beautifully simple. Inside the sensor is a permanent magnet wrapped in a coil of wire. It's mounted very close to a toothed metal ring called a tone ring or reluctor ring, which spins with the wheel.
>
> As each tooth passes the sensor tip, it changes the magnetic field — the reluctance of the magnetic circuit increases and decreases. That changing field induces a voltage in the coil. The result is an AC sine wave. The faster the wheel spins, the higher the frequency AND the higher the amplitude. No power supply needed — the sensor generates its own signal. That's why it's called 'passive.'"

**PPT Content:**
```
PASSIVE (INDUCTIVE) WHEEL SPEED SENSOR

Construction:
• Permanent magnet + coil of wire (no external power needed)
• Mounted in steering knuckle or brake backing plate
• Faces a ferromagnetic TONE RING (reluctor ring) on hub/CV joint

Operating Principle:
• Tone ring rotates → teeth pass sensor tip
• Changing magnetic reluctance → changing flux through coil
• Changing flux → INDUCED AC VOLTAGE (Faraday's law)

Signal Characteristics:
• AC sine wave output
• Frequency proportional to wheel speed
• Amplitude proportional to wheel speed (higher speed = bigger signal)
• At low speed: signal becomes very small → detection limit
• Typical output: 0.1V at crawl speed → 100V+ at highway speed

Air Gap:
• Critical: typically 0.5-1.5 mm
• Too large → weak signal → false fault codes
• Debris between sensor and ring → signal distortion
```

---

#### Slide 6: Wheel Speed Sensors — Active (Hall Effect) Type
**Visual:** Cutaway diagram of an active Hall effect sensor with its integrated circuit, powered by the ECU (2-wire or 3-wire), facing a multi-pole magnetic encoder ring. Show the clean digital square wave output signal

**Instructor Narration:**
> "The active sensor — Hall effect type — is what you'll find on most modern vehicles. Instead of generating its own signal, it has a tiny semiconductor chip inside that needs power from the ECU. It faces a magnetic encoder ring — not a toothed metal ring, but a ring with alternating north-south magnetic poles embedded in it, often made of rubber-bonded ferrite pressed onto the hub bearing seal.
>
> As the ring rotates, the alternating poles create a changing magnetic field at the Hall element. The chip converts this into a clean digital square wave — a current signal, typically switching between 7 mA and 14 mA. The huge advantage? It works all the way down to zero speed. A passive sensor can't see very slow rotation because the induced voltage is too small. An active sensor gives a clean signal even at walking pace. That's why modern ABS and ESC systems need them — especially for hill-start assist and stop-and-go traffic."

**PPT Content:**
```
ACTIVE (HALL EFFECT) WHEEL SPEED SENSOR

Construction:
• Hall effect IC (semiconductor chip) inside sensor body
• Requires power supply from ABS ECU (typically 2-wire or 3-wire)
• Faces MAGNETIC ENCODER RING (alternating N-S poles)
• Encoder ring often integrated into wheel bearing seal

Operating Principle:
• Alternating magnetic poles rotate past Hall element
• Hall IC detects polarity changes
• Outputs digital SQUARE WAVE signal

Signal Characteristics:
• Digital output (current modulation: 7 mA / 14 mA typical)
• Frequency proportional to wheel speed
• Amplitude is CONSTANT (unlike passive — easier to read)
• Works at ZERO SPEED (critical advantage)
• Some encode direction of rotation (useful for hill-start)

Why Modern Cars Use Active Sensors:
• Reliable signal at very low speeds (parking, stop & go)
• Direction detection capability
• Smaller air gap tolerance
• Required for hill-start assist, EPB, and advanced ESC functions
```

---

#### Slide 7: Passive vs Active — Side-by-Side Comparison
**Visual:** Two-column comparison with oscilloscope traces: left shows a sine wave growing in amplitude and frequency, right shows a clean square wave with constant amplitude and increasing frequency. Below, photos of each sensor type and their corresponding tone/encoder rings

**Instructor Narration:**
> "Let me put them side by side so you can remember the difference. Passive: magnet and coil, generates its own signal, AC sine wave, amplitude varies with speed, loses signal at low speed, toothed metal reluctor ring. Active: Hall chip, needs power from ECU, digital square wave, constant amplitude, works at zero speed, magnetic encoder ring with embedded poles. In the practical session, I'll show you how to tell which one you're looking at on the vehicle — and how to test each type differently."

**PPT Content:**
```
PASSIVE vs ACTIVE — COMPARISON

Feature              | Passive (Inductive)     | Active (Hall Effect)
---------------------|-------------------------|-------------------------
Power supply         | None (self-generating)  | From ECU (5V or 12V)
Signal type          | AC sine wave            | Digital square wave
Amplitude            | Varies with speed       | Constant
Low-speed detection  | Poor (signal too small) | Excellent (to 0 km/h)
Direction detection  | No                      | Yes (some types)
Wires                | 2 (signal + ground)     | 2 or 3 (power + signal)
Tone ring            | Ferromagnetic toothed   | Magnetic encoder (N-S)
Air gap sensitivity  | Very sensitive           | More tolerant
Typical resistance   | 800-1400 ohm            | Not measurable (IC)
Test method          | Resistance + AC voltage  | Current measurement

RULE OF THUMB:
• Passive sensor → you can measure resistance with multimeter
• Active sensor → no meaningful resistance reading (it's a chip)
```

---

#### Slide 8: The Tone Ring / Reluctor Ring
**Visual:** Photos showing: (1) a traditional toothed steel reluctor ring pressed onto a CV joint or hub, (2) a magnetic encoder ring integrated into a wheel bearing seal, (3) a damaged tone ring with missing teeth, (4) a contaminated tone ring packed with metallic debris

**Instructor Narration:**
> "The tone ring is the rotating target the sensor reads. On older vehicles with passive sensors, it's a steel ring with precisely machined teeth — typically 44 to 100 teeth depending on the application. It's pressed onto the hub or the CV joint outer race. On modern vehicles with active sensors, the encoder ring is often built directly into the wheel bearing seal — a rubber ring with tiny magnetic particles arranged in alternating poles.
>
> Why do you care? Because tone ring problems are one of the most common causes of ABS fault codes. A cracked ring, a ring with missing teeth, metallic debris stuck between the teeth — any of these will corrupt the speed signal. And here's the sneaky part: the MIL light comes on, you scan it, it says 'wheel speed sensor fault,' but the sensor itself is fine. It's the ring. Always inspect the tone ring before replacing the sensor."

**PPT Content:**
```
TONE RING / RELUCTOR RING / ENCODER RING

For Passive Sensors — Ferromagnetic Toothed Ring:
• Machined steel with precise tooth spacing
• Pressed onto hub or CV joint
• Typical: 44-100 teeth
• Inspection: look for cracked, broken, or missing teeth
• Common issue: metallic debris fills gaps between teeth

For Active Sensors — Magnetic Encoder Ring:
• Rubber-bonded ferrite with alternating N-S poles
• Often integrated into wheel bearing seal
• Replaced as part of bearing assembly
• Common issue: damaged during bearing replacement

DIAGNOSTIC TIP:
ABS fault code says "wheel speed sensor" →
ALWAYS inspect the tone ring FIRST before replacing the sensor
• Cracked ring = erratic signal = fault code
• Missing teeth = signal dropout = fault code
• Metallic debris = signal distortion = fault code
```

---

#### Slide 9: ABS Hydraulic Modulator — External View
**Visual:** Labelled photo of an ABS hydraulic modulator unit mounted on a vehicle — showing the brake lines connected (four going to wheels, two coming from master cylinder), the electrical connector to the ECU, and the pump motor housing. Annotate the typical location in the engine bay

**Instructor Narration:**
> "This is the ABS hydraulic modulator — the muscle of the system. It sits between the master cylinder and the wheel brakes. Every drop of brake fluid on its way to the calipers passes through this unit. On the outside, you see brake line connections — two from the master cylinder feeding in, four going out to each wheel. The large electrical connector carries power for the pump motor and control signals for the solenoid valves. On some vehicles, the ABS ECU is bolted directly onto the modulator — they're one integrated unit. On others, the ECU is separate.
>
> This unit is NOT something you casually disassemble. It's precision hydraulic equipment. But you need to understand what's inside it to diagnose ABS faults intelligently."

**PPT Content:**
```
ABS HYDRAULIC MODULATOR — EXTERNAL

Location: Engine bay, mounted near master cylinder/brake booster
Also called: ABS pump, ABS unit, ABS module, HCU (Hydraulic Control Unit)

External Connections:
• 2 inlet lines FROM master cylinder (one per hydraulic circuit)
• 4 outlet lines TO wheel brakes (one per wheel)
• Large electrical connector (ECU signals + pump motor power)
• Ground wire

Configuration Types:
• Integrated: ABS ECU bolted directly onto modulator (most common)
• Separate: ECU mounted elsewhere, connected by wiring harness

SERVICE NOTE:
• Brake lines must be correctly routed — refer to service manual
• Bleeding procedure often requires scan tool to activate valves
• Do NOT disassemble the modulator — replace as unit if faulty
• When replacing, bench-bleed per manufacturer procedure
```

---

#### Slide 10: ABS Hydraulic Modulator — Internal Components
**Visual:** Schematic cross-section of the ABS modulator showing: inlet solenoid valve (normally open), outlet solenoid valve (normally closed), pump motor with eccentric cam, low-pressure accumulator, and the hydraulic path from master cylinder to caliper through the valve pair. Show one channel in detail

**Instructor Narration:**
> "Inside the modulator, each wheel channel has two solenoid valves. The inlet valve is normally open — it allows pressure from the master cylinder to flow straight through to the caliper. That's normal braking. The outlet valve is normally closed — it blocks the path from the caliper back to the low-pressure accumulator.
>
> When the ECU wants to HOLD pressure, it energises the inlet valve to close it — blocking any more pressure from the master cylinder, but keeping what's already at the caliper. When the ECU wants to REDUCE pressure, it keeps the inlet closed AND opens the outlet valve — fluid flows from the caliper back into the low-pressure accumulator. The pump motor then moves that fluid from the accumulator back to the master cylinder side, ready for the next cycle.
>
> This is how ABS can independently control pressure at each wheel — it has a pair of solenoid valves per channel."

**PPT Content:**
```
ABS MODULATOR — INTERNAL COMPONENTS (per channel)

INLET SOLENOID VALVE (Normally Open):
• Default: OPEN — fluid flows from master cylinder to caliper
• Energised: CLOSED — blocks additional pressure from master cylinder

OUTLET SOLENOID VALVE (Normally Closed):
• Default: CLOSED — fluid stays in caliper
• Energised: OPEN — releases fluid from caliper to accumulator

PUMP MOTOR:
• Electric motor driving eccentric cam/piston
• Returns fluid from accumulator back to master cylinder side
• Runs only during ABS activation
• Driver may feel pedal pulsation and hear pump motor buzzing

LOW-PRESSURE ACCUMULATOR:
• Temporary reservoir for fluid released from calipers
• Spring-loaded chamber absorbs fluid during pressure reduce phase

Typical system: 4-channel, 4-sensor (4 inlet + 4 outlet = 8 solenoid valves)
```

---

#### Slide 11: ABS Pressure Control Phases — The Three Modes
**Visual:** Three diagrams side by side, each showing the same hydraulic channel but with valves in different states. Use colour coding: green for open flow, red for blocked flow, blue arrows for fluid movement. Phase 1: Pressure Build (inlet open, outlet closed). Phase 2: Pressure Hold (inlet closed, outlet closed). Phase 3: Pressure Reduce (inlet closed, outlet open, pump running)

**Instructor Narration:**
> "Here's the heart of ABS operation — the three pressure control phases. Phase one: Pressure Build. Both valves in default state — inlet open, outlet closed. Fluid flows from master cylinder straight to caliper. Brake pressure increases. This is normal braking.
>
> Phase two: Pressure Hold. The ECU detects a wheel decelerating too fast — it's approaching lock-up. The ECU energises the inlet valve to close it. Now no more fluid can reach the caliper, but none can escape either. Pressure is frozen at its current level. The wheel stops decelerating — but if it's still too close to lock-up, we go to phase three.
>
> Phase three: Pressure Reduce. The ECU opens the outlet valve while keeping the inlet closed. Fluid escapes from the caliper into the accumulator. Brake pressure drops. The wheel speeds back up, regains grip. The pump motor runs to return that fluid to the master cylinder side. As soon as the wheel recovers, the ECU goes back to phase one and starts building pressure again.
>
> This cycle — build, hold, reduce, build, hold, reduce — happens 15 to 50 times per second. Each wheel independently. That pulsation you feel in the brake pedal during ABS activation? That's the pump motor cycling. That buzzing noise? Same thing."

**PPT Content:**
```
ABS PRESSURE CONTROL — THREE PHASES

PHASE 1: PRESSURE BUILD (Normal Braking)
• Inlet valve: OPEN (default)
• Outlet valve: CLOSED (default)
• Effect: Pressure increases at caliper
• When: Normal braking, or wheel has recovered from near-lock

PHASE 2: PRESSURE HOLD
• Inlet valve: CLOSED (energised)
• Outlet valve: CLOSED (default)
• Effect: Pressure frozen at current level
• When: Wheel decelerating faster than threshold — approaching lock

PHASE 3: PRESSURE REDUCE
• Inlet valve: CLOSED (energised)
• Outlet valve: OPEN (energised)
• Pump motor: RUNNING
• Effect: Pressure decreases at caliper, fluid returns via pump
• When: Wheel at or near lock-up — must release pressure

CYCLE RATE: 15-50 cycles per second per wheel
DRIVER FEELS: Pedal pulsation, hears pump motor buzzing
```

---

#### Slide 12: ABS Control Logic — How the ECU Decides
**Visual:** Graph showing wheel speed vs time for one wheel during ABS intervention. The vehicle reference speed line is smooth and declining. The individual wheel speed line shows rapid deceleration, then ABS intervention bringing it back up, then deceleration again — a saw-tooth pattern oscillating around the optimal slip ratio of ~10-20%

**Instructor Narration:**
> "How does the ECU know when to intervene? It calculates a reference vehicle speed by averaging the four wheel speeds — with some filtering for turns where inner and outer wheels legitimately differ. Then it monitors each wheel individually against that reference.
>
> If one wheel suddenly decelerates much faster than the reference — meaning it's losing grip — the ECU recognises the onset of lock-up. The threshold isn't just speed difference; the ECU looks at wheel deceleration rate. A wheel can decelerate at perhaps 1G on dry road while braking hard. But if it's decelerating at 3G or 4G, that's the tyre losing grip — not the car slowing down.
>
> The optimal slip ratio is about 10 to 20 percent — meaning the wheel is turning slightly slower than it would if it were rolling freely, but not locked. That 10-20% slip is where you get maximum braking force. ABS keeps each wheel dancing in that zone. Look at this graph — see the saw-tooth pattern? That's the wheel speed oscillating as ABS cycles through build, hold, reduce, build, hold, reduce."

**PPT Content:**
```
ABS ECU CONTROL LOGIC

Step 1: Calculate VEHICLE REFERENCE SPEED
• Average of 4 wheel speeds (filtered for cornering)
• Represents actual vehicle speed

Step 2: Monitor INDIVIDUAL WHEEL SPEEDS
• Compare each wheel to reference speed
• Calculate wheel SLIP = (Reference - Wheel) / Reference × 100%
• Monitor wheel DECELERATION RATE

Step 3: Detect Lock-Up Onset
• Wheel slip exceeding threshold (~15-20%)
• OR wheel deceleration rate exceeding physical limit (~3-4G)
• → Trigger ABS intervention on that wheel

Step 4: Control Pressure
• Cycle through Build → Hold → Reduce phases
• Keep wheel in OPTIMAL SLIP ZONE (10-20% slip)
• Maximum braking force + maintained steering capability

RESULT:
• Shorter stopping distance on most surfaces
• ALWAYS maintains steering control
• Each wheel controlled independently
```

---

#### Slide 13: ABS on Different Surfaces
**Visual:** Comparison table and illustration showing ABS behavior on dry asphalt, wet road, gravel, and ice. Include approximate stopping distances and the note that on loose gravel/snow, a locked wheel can actually be shorter-stopping (ploughing effect) — but ABS prioritises steering control

**Instructor Narration:**
> "ABS doesn't behave identically on every surface. On dry asphalt, ABS gives you about the same or slightly longer stopping distance compared to a skilled driver — but the key benefit is steering control. On wet roads, ABS is clearly superior — most drivers can't threshold brake effectively on a slippery surface. On ice, ABS is massively better than a locked wheel.
>
> Here's an interesting exception: on loose gravel or deep snow, a locked wheel actually digs in and builds a wedge of material in front of it, which can stop you shorter. ABS prevents that wedge from forming, so stopping distance can be slightly longer. But — and this is the critical point — you maintain steering control. The engineers decided that being able to steer around an obstacle is more valuable than stopping a few metres shorter. Some modern ABS systems have a 'loose surface' mode that allows more slip to get closer to both benefits."

**PPT Content:**
```
ABS ON DIFFERENT SURFACES

Surface          | ABS Stopping vs Locked | Steering Control
-----------------|-----------------------|------------------
Dry asphalt      | Similar or slightly longer | YES (vs NO)
Wet asphalt      | SHORTER                | YES (vs NO)
Ice              | MUCH SHORTER           | YES (vs NO)
Loose gravel     | Slightly LONGER*       | YES (vs NO)
Deep snow        | Slightly LONGER*       | YES (vs NO)

* On loose surfaces, locked wheels dig in (ploughing effect)
  ABS prevents this, but MAINTAINS STEERING — the design priority

KEY PRINCIPLE:
ABS is primarily a STEERING PRESERVATION system, not just
a stopping-distance-reduction system. The ability to brake
AND steer simultaneously is the core safety benefit.

Modern enhancement: Some systems detect loose surfaces and
allow higher slip ratio to partially recover ploughing effect.
```

---

#### Slide 14: ABS Warning Light and Self-Test
**Visual:** Dashboard showing the ABS warning light (amber), plus a flowchart of the ABS self-test sequence at ignition on: ECU power-on self-test, sensor signal check, valve/pump test, lamp test. Show what conditions turn the ABS light on

**Instructor Narration:**
> "Every time you turn the ignition on, the ABS ECU runs a self-test. It checks internal circuits, reads each wheel speed sensor signal, briefly activates the pump motor and solenoid valves — you might hear a brief 'thunk' or motor noise during startup. That's normal. The ABS warning light illuminates during the lamp test, then goes out if everything passes.
>
> If the light stays on, ABS is disabled — but standard brakes still work. The vehicle is safe to drive carefully to a workshop, but it has no anti-lock protection. If both the ABS light AND the red brake warning light are on, that's more serious — could indicate a shared hydraulic fault. Do not drive.
>
> Common causes for ABS light: wheel speed sensor faults — broken wire, contaminated tone ring, failed sensor. Pump motor failure. ECU internal fault. Low system voltage during cranking can also trigger a momentary fault."

**PPT Content:**
```
ABS WARNING LIGHT & SELF-TEST

Self-Test Sequence (at ignition ON):
1. ECU internal self-test (RAM, ROM, processor check)
2. Sensor supply voltage verification
3. Wheel speed sensor signal plausibility check
4. Solenoid valve brief activation test
5. Pump motor brief activation test
6. ABS warning lamp test → then lamp OFF if all passed

ABS Warning Light (Amber) ON:
• ABS is DISABLED — normal brakes still function
• Safe to drive carefully to workshop (no ABS protection)
• Common causes: sensor fault, tone ring damage, low voltage,
  pump motor failure, ECU internal fault, wiring issue

ABS Light + RED Brake Light BOTH ON:
• May indicate shared hydraulic system fault
• DO NOT DRIVE — tow to workshop

DIAGNOSTIC NOTE:
• ABS faults stored as C-codes (Chassis codes)
• Some faults set only above certain speed threshold
• Some faults clear after a test drive once issue resolved
```

---

### **DEVELOPMENT PART 2: ESC, Traction Control & Advanced Stability** (Slides 15-21, ~25 minutes)

**Narrative Voice:** Elevate from single-wheel ABS control to whole-vehicle stability. Build on ABS as the foundation, then add the sensors and intelligence that make ESC possible.

---

#### Slide 15: From ABS to ESC — Adding the Brain
**Visual:** Evolution diagram showing ABS (1978) → TCS (late 1980s) → ESC/ESP (1995). Show how each builds on the previous: ABS hardware is the foundation, TCS adds acceleration control, ESC adds yaw/lateral sensors and steering angle input

**Instructor Narration:**
> "ABS was step one — controlling individual wheels during braking. Step two came in the late 1980s with Traction Control — TCS. Engineers realised the same ABS hardware could work in reverse: instead of releasing brakes on a locking wheel, you could APPLY brakes to a spinning wheel. If one drive wheel loses grip during acceleration, TCS brakes it, transferring torque to the wheel with grip. Same solenoid valves, same pump motor, just a different software strategy.
>
> Step three is the big one: ESC — Electronic Stability Control, also called ESP (Electronic Stability Program). Bosch and Mercedes introduced it in 1995 after a dramatic public incident involving the Mercedes A-Class rollover. ESC adds three critical sensors to the ABS platform: a yaw rate sensor, a lateral acceleration sensor, and uses the steering angle sensor from the EPS system. With these, the ECU knows not just what each wheel is doing, but what the WHOLE VEHICLE is doing — and whether it matches what the DRIVER wants."

**PPT Content:**
```
EVOLUTION: ABS → TCS → ESC/ESP

1978 — ABS (Anti-Lock Braking System)
• Controls individual wheel braking to prevent lock-up
• Hardware: 4 wheel speed sensors + hydraulic modulator + ECU

Late 1980s — TCS (Traction Control System)
• Prevents drive wheel spin during acceleration
• Uses SAME ABS hardware — applies brakes to spinning wheel
• May also request engine torque reduction via ECM

1995 — ESC/ESP (Electronic Stability Control / Program)
• Maintains vehicle directional stability
• ADDS: Yaw rate sensor + Lateral acceleration sensor
• USES: Steering angle sensor (driver intent)
• INTEGRATES: ABS + TCS + engine management
• Selectively brakes individual wheels to correct vehicle path

EU mandatory: November 2011 (new types), November 2014 (all new vehicles)

NOTE: Different names, same function:
ESC = ESP = DSC (BMW) = VSA (Honda) = VSC (Toyota) = StabiliTrak (GM)
```

---

#### Slide 16: ESC Additional Sensors — Yaw Rate Sensor
**Visual:** Diagram of a vehicle viewed from above, showing the vertical axis through the centre of gravity. The yaw rate sensor measures rotation about this axis. Include a MEMS gyroscope illustration showing the vibrating structure principle. Show positive yaw (turning left) and negative yaw (turning right)

**Instructor Narration:**
> "The yaw rate sensor is the most important sensor ESC adds. Yaw is rotation about the vertical axis — when the car turns left, it yaws left. The sensor measures how fast the car is rotating, in degrees per second.
>
> Modern yaw rate sensors use MEMS technology — Micro Electro Mechanical Systems. Inside the chip, a tiny vibrating structure experiences the Coriolis force when the sensor rotates. This force is converted into an electrical signal proportional to the rotation rate. It's the same principle as a vibrating tuning fork — if you rotate it while it's vibrating, you can feel the fork twist sideways. Incredibly small, incredibly precise.
>
> The sensor is typically mounted near the vehicle's centre of gravity — often under the centre console or seats. It tells the ECU: 'The car is rotating at X degrees per second.' The ECU compares this to how fast the car SHOULD be rotating based on the steering wheel angle and vehicle speed. If they don't match — intervention."

**PPT Content:**
```
YAW RATE SENSOR — "How Fast Is the Car Spinning?"

What It Measures:
• Rotation rate about the VERTICAL AXIS (yaw axis)
• Unit: degrees per second (°/s)
• Positive = turning one direction, Negative = opposite

Technology: MEMS Gyroscope
• Micro Electro Mechanical Systems
• Vibrating silicon structure detects Coriolis force
• Tiny, solid-state, no moving macro parts
• Very high precision: detects < 1°/s

Location:
• Near vehicle centre of gravity
• Often under centre console, under seats, or in ESC module
• Must be securely mounted — vibration affects accuracy

ECU Uses Yaw Rate To:
• Determine ACTUAL vehicle rotation
• Compare with EXPECTED rotation (from steering angle + speed)
• Detect oversteer (car rotating MORE than driver commands)
• Detect understeer (car rotating LESS than driver commands)
```

---

#### Slide 17: ESC Additional Sensors — Lateral Acceleration & Steering Angle
**Visual:** Two diagrams: (1) A car in a corner with an arrow showing lateral (sideways) acceleration — the force pushing occupants toward the outside of the turn. (2) The steering angle sensor on the steering column showing how it measures driver steering input in degrees from centre

**Instructor Narration:**
> "Two more sensors complete the ESC picture. The lateral acceleration sensor — or lateral G sensor — measures the sideways force acting on the vehicle during cornering. It's another MEMS device, this time an accelerometer. It tells the ECU how much lateral force the car is experiencing. Combined with yaw rate, it gives a complete picture of vehicle dynamics.
>
> The steering angle sensor is mounted on the steering column. It tells the ECU exactly where the driver is pointing the front wheels — the driver's INTENT. This is the reference signal. If the driver turns the wheel 30 degrees to the left, the car should yaw left at a rate consistent with that angle and the current speed. If the actual yaw rate doesn't match, the car is either oversteering or understeering.
>
> Remember from Day 22 — we mentioned the steering angle sensor when we discussed EPS. Today you see why it's there: it's not just for power steering assistance. It's a critical ESC input."

**PPT Content:**
```
LATERAL ACCELERATION SENSOR — "How Hard Is the Car Cornering?"

What It Measures:
• Sideways (lateral) acceleration force during cornering
• Unit: g (gravitational units) or m/s²
• Perpendicular to direction of travel
• MEMS accelerometer technology

Location: Same module as yaw rate sensor (often combined unit)

STEERING ANGLE SENSOR — "Where Does the Driver Want to Go?"

What It Measures:
• Steering wheel position in degrees from centre
• Rate of steering input (how fast driver is turning)
• Absolute position (not just relative change)

Location: On steering column, integrated into clockspring area
• Outputs via CAN bus to ESC ECU
• May require calibration after alignment or component replacement

ESC SENSOR SUMMARY:
• 4 × Wheel speed sensors → individual wheel behavior
• 1 × Yaw rate sensor → vehicle rotation rate
• 1 × Lateral acceleration sensor → cornering force
• 1 × Steering angle sensor → driver intent
= COMPLETE PICTURE of driver intent vs vehicle reality
```

---

#### Slide 18: ESC in Action — Oversteer Correction
**Visual:** Top-down view of a car entering a corner and beginning to oversteer (rear slides out). Show the yaw rate arrow exceeding the expected yaw. Show ESC applying the FRONT OUTER wheel brake to create a corrective yaw moment pulling the nose outward, straightening the car. Use force arrows to illustrate the corrective moment

**Instructor Narration:**
> "Oversteer — the rear of the car slides outward. The car rotates more than the driver intended. This is the classic spin. Rear-wheel-drive cars are more prone to this, but it can happen to any car on a slippery surface.
>
> The ESC ECU sees: yaw rate is HIGHER than expected for the steering angle and speed. The car is rotating too much. Response: ESC applies the brake on the FRONT OUTER wheel. Why? Because braking that wheel creates a yaw moment in the opposite direction — it pulls the nose of the car outward, counteracting the excessive rotation. Think of it as putting an anchor on the outside front corner of the car to drag it back in line.
>
> At the same time, the ECU may request the engine management system to reduce torque. Less power to the drive wheels means less destabilising force."

**PPT Content:**
```
ESC OVERSTEER CORRECTION

OVERSTEER: Rear slides OUT — car rotates MORE than intended
• Common triggers: Sudden throttle lift in corner, slippery surface,
  excessive speed entry, rear-wheel drive power oversteer

ESC Detection:
• Actual yaw rate > Expected yaw rate (from steering angle + speed)
• Lateral acceleration inconsistent with steering input

ESC Response:
• BRAKES the FRONT OUTER wheel
  → Creates corrective yaw moment opposing excess rotation
  → Pulls the nose of the car toward the outside of the turn
• Requests ENGINE TORQUE REDUCTION from ECM
  → Reduces destabilising force at drive wheels
• May modulate individual rear brakes as well

                    Direction of travel →
                         ╱
           Rear slides ╱    ← ESC brakes front outer wheel
           out here   ╱       (creates corrective moment)
                     ╱
                    Car rotating too much
```

---

#### Slide 19: ESC in Action — Understeer Correction
**Visual:** Top-down view of a car entering a corner and beginning to understeer (front pushes wide, car goes straight despite steering input). Show the yaw rate arrow being LESS than expected. Show ESC applying the REAR INNER wheel brake to create a corrective yaw moment pulling the rear inward, tightening the car's line

**Instructor Narration:**
> "Understeer — the front of the car pushes wide. The driver turns the wheel but the car keeps going straight, or not turning enough. Front-wheel-drive cars are more prone to this, and it's the more common loss-of-control mode.
>
> The ESC ECU sees: yaw rate is LOWER than expected for the steering angle and speed. The car isn't rotating enough. Response: ESC applies the brake on the REAR INNER wheel. This creates a yaw moment that pulls the rear of the car inward, effectively tightening the turning radius. The car rotates more, matching the driver's steering input.
>
> Again, the ECU also requests engine torque reduction — in an understeering front-wheel-drive car, reducing front wheel drive force lets the front tyres use more of their grip budget for turning instead of accelerating."

**PPT Content:**
```
ESC UNDERSTEER CORRECTION

UNDERSTEER: Front pushes WIDE — car rotates LESS than intended
• Common triggers: Excessive speed into corner, heavy throttle in corner
  (FWD), slippery surface, worn front tyres

ESC Detection:
• Actual yaw rate < Expected yaw rate (from steering angle + speed)
• Driver increasing steering angle but car not responding proportionally

ESC Response:
• BRAKES the REAR INNER wheel
  → Creates corrective yaw moment pulling rear inward
  → Tightens the car's turning radius
• Requests ENGINE TORQUE REDUCTION from ECM
  → Frees front tyre grip budget for steering (FWD)
• May reduce brake pressure on front wheels to allow more steering grip

OVERSTEER SUMMARY: Too much rotation → brake FRONT OUTER
UNDERSTEER SUMMARY: Too little rotation → brake REAR INNER

MEMORY AID:
• Oversteer: "The rear is coming around" → anchor the FRONT OUTSIDE
• Understeer: "The front won't turn in" → drag the REAR INSIDE
```

---

#### Slide 20: Traction Control System (TCS)
**Visual:** Diagram of a front-wheel-drive car accelerating on a split-friction surface (one wheel on ice, one on dry asphalt). Show the wheel on ice spinning, and TCS applying its brake to transfer torque to the wheel with grip. Also show the engine torque reduction arrow

**Instructor Narration:**
> "Traction control is ESC working during acceleration instead of braking or cornering. Same hardware, different software strategy. If one drive wheel spins — maybe you're pulling out onto an icy road and one wheel is on the ice — TCS detects the speed difference between the drive wheels.
>
> It applies the brake to the spinning wheel. In an open differential, this effectively transfers torque to the opposite wheel that has grip. It can also request the engine management to reduce power — cutting fuel injection pulses, retarding ignition timing, or closing the throttle. Some systems do both simultaneously.
>
> Hill Start Assist uses ABS pressure hold to keep the brakes applied for a few seconds after you release the brake pedal on a hill, giving you time to move your foot to the accelerator. Hill Descent Control uses ABS to maintain a slow, controlled speed going downhill without the driver needing to brake — it automatically pulses the brakes to hold a set crawl speed. All of these use the same ABS/ESC hardware platform."

**PPT Content:**
```
TRACTION CONTROL SYSTEM (TCS)

Purpose: Prevent drive wheel spin during acceleration

Detection:
• Drive wheel speed significantly higher than non-drive wheels
• OR both drive wheels spinning faster than vehicle reference speed

Intervention Methods:
1. BRAKE the spinning wheel (using ABS modulator)
   → In open differential: torque transfers to opposite wheel
2. REQUEST ENGINE TORQUE REDUCTION (via CAN to ECM)
   → Cut fuel injection, retard ignition, close throttle
3. Both methods simultaneously (most modern systems)

RELATED FUNCTIONS (using same hardware):

Hill Start Assist (HSA):
• Holds brake pressure for ~2 seconds after releasing brake pedal on incline
• Prevents rollback while driver moves foot to accelerator
• Uses ABS pressure hold phase

Hill Descent Control (HDC):
• Maintains controlled low speed (~5-8 km/h) on steep descents
• Automatically pulses brakes via ABS modulator
• Driver does not need to press brake pedal
• Common on SUVs and off-road vehicles

ALL built on the ABS hydraulic modulator platform
```

---

#### Slide 21: The Complete ABS/ESC System Map
**Visual:** Comprehensive system diagram showing all sensors (4 wheel speed, yaw rate, lateral G, steering angle, brake pressure sensor), the ABS/ESC ECU, the hydraulic modulator, connections to the ECM for torque reduction, connections to the instrument cluster for warning lights, and CAN bus linking everything

**Instructor Narration:**
> "Let's pull it all together. Here's the complete system. Four wheel speed sensors feeding into the ABS/ESC ECU. Yaw rate and lateral acceleration — often in a combined sensor cluster. Steering angle sensor from the steering column. Brake pressure sensor telling the ECU how hard the driver is pressing. The ECU processes all of this and controls the hydraulic modulator — eight solenoid valves and a pump motor. It communicates with the Engine Control Module over CAN bus to request torque reduction. It communicates with the instrument cluster to turn on warning lights. And it stores fault codes accessible through the OBD-II diagnostic port.
>
> This is one of the most integrated systems in the vehicle. ABS, TCS, ESC, hill assist — all sharing the same hardware platform with different software strategies. As a technician, understanding this integration means you can diagnose problems logically rather than just throwing parts at it."

**PPT Content:**
```
THE COMPLETE ABS/ESC SYSTEM

SENSOR INPUTS (to ABS/ESC ECU):
• 4 × Wheel speed sensors (individual wheel rotation)
• 1 × Yaw rate sensor (vehicle rotation rate)
• 1 × Lateral acceleration sensor (cornering force)
• 1 × Steering angle sensor (driver intent)
• 1 × Brake pressure sensor (pedal force applied)
• Battery voltage monitoring

ACTUATOR OUTPUTS (from ECU):
• 8 × Solenoid valves in hydraulic modulator (4 inlet + 4 outlet)
• 1 × Pump motor (return pump)
• CAN message to ECM: torque reduction request
• CAN message to cluster: warning lamp control

DIAGNOSTIC INTERFACE:
• Fault codes (DTCs) stored as C-codes (Chassis domain)
• Live data available via OBD-II / manufacturer protocol
• Some functions require scan tool for calibration/reset

FUNCTIONS SHARING THIS PLATFORM:
ABS | TCS | ESC/ESP | Hill Start Assist | Hill Descent Control
| Electronic Brake-force Distribution (EBD) | Brake Assist (BA)
```

---

### **PRACTICAL: Hands-On Chassis Electronics** (Slides 22-25, ~80 minutes)

**Narrative Voice:** Workshop guide. Structured practical stations with clear objectives and measurement criteria.

---

#### Slide 22: Practical Overview & Station Setup
**Visual:** Workshop floor plan showing four practical stations with numbered activities. Each station has an icon representing the task

**Instructor Narration:**
> "Time for hands-on work. We have four activities, and you'll work in pairs rotating through them. Station 1: Identify wheel speed sensors and tone rings on the workshop vehicle — tell me whether they're passive or active. Station 2: Test a wheel speed sensor with the multimeter — resistance for passive, supply voltage for active. If we have an oscilloscope available, we'll look at the signal waveform. Station 3: Use the scan tool to read ABS/ESC live data — wheel speeds during a slow roll, yaw rate, lateral G. Station 4: Read ABS/ESC fault codes, interpret the C-codes, and discuss what each fault means for the vehicle.
>
> Each station is about 20 minutes. I'll demo Station 2 and 3 first, then you rotate. Safety note: do NOT spin wheels with the vehicle on the lift while someone's hand is near the brake area. Wait for my signal."

**PPT Content:**
```
PRACTICAL SESSION (80 minutes) — 4 STATIONS, PAIRS

STATION 1 (20 min): Identify Sensors & Tone Rings
→ Locate wheel speed sensors at each wheel
→ Identify type: passive (inductive) or active (Hall effect)
→ Locate and inspect tone rings / encoder rings
→ Check air gap and condition

STATION 2 (20 min): Test Wheel Speed Sensor
→ Multimeter: resistance test (passive) or supply voltage (active)
→ Oscilloscope (if available): observe signal waveform
→ Compare your reading to specification

STATION 3 (20 min): ABS/ESC Live Data on Scan Tool
→ Connect scan tool to OBD-II port
→ Navigate to ABS/ESC module
→ Read live data: wheel speeds, yaw rate, lateral G
→ Slowly roll vehicle (if possible) and observe speed readings

STATION 4 (20 min): Read & Interpret ABS/ESC Fault Codes
→ Read stored DTCs in ABS/ESC module
→ Identify C-codes (Chassis domain codes)
→ Interpret fault description and possible causes
→ Discuss diagnostic next steps

SAFETY: DO NOT reach near brakes while wheels are spinning
```

---

#### Slide 23: Station 1 & 2 — Sensor Identification and Testing
**Visual:** Two-part visual. Top: annotated photo showing a wheel speed sensor mounted in the steering knuckle with the wiring harness routed away, and the tone ring visible on the hub. Bottom: multimeter connected to the sensor connector showing a resistance reading (e.g., 1.1 kohm for passive), and an oscilloscope showing a sine wave pattern

**Instructor Narration:**
> "Station 1: Look at the sensor. Where is it mounted? Steering knuckle, brake backing plate, or hub carrier? Follow the wire — where does it connect? Can you see the tone ring? Is it a toothed metal ring or a smooth magnetic encoder on the bearing seal? Write down what you find for each wheel.
>
> Station 2: Disconnect the sensor at its electrical connector. For a passive sensor, set your multimeter to resistance — you should read 800 to 1400 ohms typically. If you get OL (open), the coil is broken. If you get zero ohms, it's shorted. For an active sensor, you can't measure useful resistance — it's a chip. Instead, reconnect it and back-probe the supply wire with the ignition on — you should see battery voltage or 5V depending on the system.
>
> If we have the oscilloscope: reconnect the sensor, have someone slowly spin the wheel by hand, and watch the signal. Passive: sine wave. Active: square wave. The frequency increases as you spin faster. This is the real-world signal the ECU is reading."

**PPT Content:**
```
SENSOR IDENTIFICATION & TESTING

IDENTIFICATION CHECKLIST (per wheel):
□ Sensor location (knuckle, backing plate, hub carrier)
□ Wiring: 2-wire or 3-wire? Connector type?
□ Tone ring type: toothed steel or magnetic encoder?
□ Tone ring condition: cracks, missing teeth, debris?
□ Air gap between sensor and ring: visual check
□ Type conclusion: PASSIVE or ACTIVE?

TESTING — PASSIVE (Inductive) Sensor:
• Disconnect at connector
• Multimeter → Resistance (Ohms)
• Specification: typically 800-1400 Ω (check service manual)
• OL = open coil (failed), 0 Ω = shorted coil (failed)
• AC voltage test: spin wheel → should see AC mV signal

TESTING — ACTIVE (Hall Effect) Sensor:
• Back-probe supply wire with ignition ON
• Should read ~5V or ~12V supply from ECU
• Signal wire: current-modulated (requires scope or breakout box)
• Resistance test NOT meaningful on active sensors

OSCILLOSCOPE (if available):
• Passive: sine wave, amplitude varies with speed
• Active: square wave, amplitude constant
```

---

#### Slide 24: Station 3 & 4 — Scan Tool Live Data and Fault Codes
**Visual:** Screenshot of a scan tool displaying ABS live data: four wheel speed PIDs showing km/h values, yaw rate in degrees/sec, lateral acceleration in g, steering angle in degrees. Below, a separate screenshot showing C-code fault list with descriptions

**Instructor Narration:**
> "Station 3: Connect the scan tool, select the ABS or ESC module — the menu name varies by manufacturer and tool. Navigate to live data. You should see individual wheel speeds for all four wheels. With the vehicle stationary, they should all read zero or very close. If you can safely do a slow roll on the lift or push the vehicle in the bay, watch the speeds change. Are they all equal? They should be, going in a straight line.
>
> Also look for yaw rate and lateral acceleration — they should be zero or near zero with the vehicle stationary. Steering angle should read close to zero with the wheel centred. These baseline readings help you understand what normal looks like.
>
> Station 4: Now go to fault codes in the ABS/ESC module. These are C-codes — Chassis domain. The format is C followed by four digits, just like P-codes for powertrain but starting with C. Read whatever codes are stored. Even if the vehicle has no active faults, there may be historical codes. For each code: write down the number, the description, and discuss with your partner what could cause it and what you'd check first."

**PPT Content:**
```
SCAN TOOL — ABS/ESC LIVE DATA

Key PIDs to Monitor:
• Wheel Speed FL (km/h)     • Wheel Speed FR (km/h)
• Wheel Speed RL (km/h)     • Wheel Speed RR (km/h)
• Yaw Rate (°/s)            • Lateral Acceleration (g)
• Steering Angle (°)        • Brake Pressure (bar)

Baseline (vehicle stationary, wheel straight):
• All wheel speeds: 0 km/h
• Yaw rate: ~0 °/s
• Lateral acceleration: ~0 g
• Steering angle: ~0° (may need calibration reset)

SCAN TOOL — ABS/ESC FAULT CODES (C-CODES)

C-code Format: C + 4 digits (e.g., C0035, C1201)
• C0xxx = Generic chassis codes (SAE standard)
• C1xxx = Manufacturer-specific chassis codes

Common ABS/ESC DTCs:
C0035 — Left Front Wheel Speed Sensor Circuit
C0040 — Right Front Wheel Speed Sensor Circuit
C0045 — Left Rear Wheel Speed Sensor Circuit
C0050 — Right Rear Wheel Speed Sensor Circuit
C0060 — ABS Pump Motor Circuit Malfunction
C0070 — ABS Solenoid Valve Relay Circuit
C0131 — Yaw Rate Sensor Circuit Range/Performance
C0186 — Lateral Accelerometer Sensor Fault

For each code: WHAT is the fault? WHAT would you check first?
```

---

#### Slide 25: Practical Debrief — Findings Discussion
**Visual:** Template table for learners to fill in: Wheel position | Sensor type | Resistance/Voltage reading | Tone ring condition | Pass/Fail. Plus a section for fault codes found

**Instructor Narration:**
> "Let's regroup. Each pair, tell me: what sensor type did you find at each wheel? What were your resistance or voltage readings? Any tone ring damage? Any fault codes? Let's build a picture of this vehicle's ABS/ESC health on the board.
>
> The goal here isn't just to fill in numbers — it's to start thinking like a diagnostician. If the scan tool says 'Left front wheel speed sensor circuit,' what's your diagnostic path? Check the wiring first — is it damaged, chafed, corroded at the connector? Check the tone ring — is it cracked or contaminated? Then check the sensor itself — resistance in spec? Only after all that do you consider the ECU. Start simple, work toward complex. That's the diagnostic mindset."

**PPT Content:**
```
PRACTICAL DEBRIEF — RECORD YOUR FINDINGS

WHEEL SPEED SENSOR RESULTS:
Position | Type        | Reading           | Tone Ring   | Status
---------|-------------|-------------------|-------------|--------
FL       |             |                   |             |
FR       |             |                   |             |
RL       |             |                   |             |
RR       |             |                   |             |

FAULT CODES FOUND:
Code     | Description                | Possible Cause      | First Check
---------|----------------------------|---------------------|------------
         |                            |                     |
         |                            |                     |

DIAGNOSTIC MINDSET — Fault Code Says "Sensor Fault":
1. Check WIRING first (damage, chafing, corrosion, connector)
2. Check TONE RING (cracked, missing teeth, debris, damage)
3. Check SENSOR (resistance/voltage, mounting, air gap)
4. Check ECU (last resort — most expensive to replace)

RULE: Work from cheapest/simplest cause to most expensive/complex
```

---

### **WRAP-UP: Consolidation & Preview** (Slides 26-28, ~15 minutes)

---

#### Slide 26: The ABS/ESC Integration Story
**Visual:** Layered pyramid diagram. Base: ABS (single-wheel braking control). Middle: TCS + EBD (acceleration + brake distribution). Top: ESC/ESP (whole-vehicle stability). Show how each layer builds on the one below. Annotate with Day 21 vehicle dynamics concepts on the side

**Instructor Narration:**
> "Let me tie today together with a single picture. At the base: ABS — individual wheel control during braking. It manages longitudinal grip. On top of that: traction control and electronic brake-force distribution — managing wheelspin and optimising brake balance front-to-rear. At the peak: ESC — the complete vehicle stability system that compares what the driver wants with what the car is doing, and intervenes by selectively braking individual wheels.
>
> All of it runs on the same hardware platform. Four wheel speed sensors, a hydraulic modulator with eight solenoid valves and a pump, and an ECU. ESC adds a yaw rate sensor, lateral accelerometer, and steering angle sensor. That's the entire hardware list. The magic is in the software — the algorithms that cycle through pressure build, hold, and reduce at each wheel, 50 times per second, to keep 1500 kg of metal on the road and pointed where the driver intends.
>
> Link it back to Day 21: the friction circle, weight transfer, tyre slip. Link it back to Day 23: the hydraulic circuit, calipers, fluid. Today's electronics sit on top of that mechanical and dynamic foundation. Without understanding all three layers, you can't diagnose modern brake faults effectively."

**PPT Content:**
```
THE ABS/ESC INTEGRATION PYRAMID

        ╱ ESC/ESP ╲         ← Whole-vehicle stability
       ╱ Yaw + Lat G ╲        (oversteer/understeer correction)
      ╱ + Steering Angle╲
     ╱───────────────────╲
    ╱  TCS + EBD + BA      ╲  ← Acceleration & distribution
   ╱  Traction, Brake Dist, ╲    (wheelspin prevention,
  ╱   Brake Assist            ╲    front/rear balance)
 ╱─────────────────────────────╲
╱  ABS — Individual Wheel       ╲ ← Foundation layer
╱  Braking Control (4-channel)    ╲  (lock-up prevention)
╱──────────────────────────────────╲

Day 21: Vehicle dynamics (friction circle, weight transfer, slip)
Day 23: Mechanical brakes (hydraulics, calipers, pads, fluid)
Day 24: Chassis electronics (sensors, ECU logic, modulator control)

THREE LAYERS = Complete understanding of modern braking systems
```

---

#### Slide 27: What You Learned Today
**Visual:** Checklist with completed items

**Instructor Narration:**
> "Let's check off what you've accomplished. You can explain how ABS prevents lock-up using three pressure phases. You know the difference between passive and active wheel speed sensors and how to test each. You understand the hydraulic modulator — solenoid valves, pump, accumulator. You can explain how ESC uses yaw rate, lateral acceleration, and steering angle to detect and correct oversteer and understeer. You understand traction control and how it shares ABS hardware. And you've used a scan tool to read real ABS/ESC live data and fault codes.
>
> Tomorrow — Day 25, last day of Week 5 — we bring the whole chassis system together. Wheel alignment, tyre wear diagnosis, and a complete brake-to-ESC fault diagnosis exercise. Everything from Days 21 through 24 converges."

**PPT Content:**
```
DAY 24 RECAP — YOU CAN NOW:

[ ] Explain the three ABS pressure phases: build, hold, reduce
[ ] Describe how ABS prevents lock-up while maintaining steering
[ ] Differentiate passive (inductive) vs active (Hall effect) wheel speed sensors
[ ] Explain tone ring function and common failure modes
[ ] Identify ABS hydraulic modulator components and their roles
[ ] Explain ESC sensors: yaw rate, lateral acceleration, steering angle
[ ] Describe how ESC corrects oversteer (front outer brake)
    and understeer (rear inner brake)
[ ] Explain TCS, hill start assist, and hill descent control concepts
[ ] Read and interpret ABS/ESC C-codes and live data on a scan tool
[ ] Apply diagnostic logic: wiring → tone ring → sensor → ECU

TOMORROW — Day 25: Chassis Integration
Wheel alignment, tyre wear patterns, complete chassis fault diagnosis
```

---

#### Slide 28: Day 25 Preview
**Visual:** Image of a four-wheel alignment machine displaying toe, camber, and caster readings, plus a diagnostic flowchart showing a complete brake/ABS/ESC fault pathway

**Instructor Narration:**
> "Tomorrow is the grand finale of Week 5. We start with wheel alignment — toe, camber, caster, and what happens when they're wrong. We'll look at tyre wear patterns that tell you the alignment story without a machine. Then we do a complete chassis fault diagnosis exercise: starting from a customer complaint, working through mechanical brakes, ABS sensors, ESC data, and arriving at the root cause. Five days of chassis knowledge compressed into one diagnostic pathway. Bring everything you've learned this week — you'll need it all."

**PPT Content:**
```
DAY 25 PREVIEW: CHASSIS INTEGRATION & DIAGNOSIS

Wheel Alignment:
• Toe, camber, caster, thrust angle
• What happens when each is wrong
• Tyre wear patterns as diagnostic evidence

Complete Chassis Fault Diagnosis Exercise:
• Customer complaint → systematic diagnosis
• Mechanical brakes (Day 23) + ABS/ESC (Day 24) + dynamics (Day 21)
• From symptom to root cause

This is where everything in Week 5 comes together.
Bring your notes from Days 21-24. You'll need them.
```

---

## Assessment Checkpoint

**Formative (not graded):**
- Verbal check: Explain the three ABS pressure phases in correct sequence
- Sensor identification: Correctly identify sensor type at each wheel on the workshop vehicle
- Multimeter test: Obtain a valid resistance reading (passive) or supply voltage reading (active) within specification
- Scan tool exercise: Navigate to ABS/ESC module, read at least four wheel speed PIDs, and read stored DTCs
- Oversteer/understeer: Correctly state which wheel ESC brakes for each condition and explain why

---

## Key Takeaways

1. ABS prevents wheel lock-up by cycling brake pressure through three phases (build, hold, reduce) at each wheel independently, 15-50 times per second
2. Passive wheel speed sensors generate an AC signal proportional to speed; active sensors produce a constant-amplitude digital signal that works down to zero speed
3. The tone ring is a common fault source — always inspect it before condemning the sensor
4. ESC compares driver intent (steering angle) with actual vehicle behavior (yaw rate + lateral acceleration) and selectively brakes individual wheels to correct oversteer and understeer
5. ABS, TCS, ESC, hill assist, and hill descent control all share the same hydraulic modulator platform — different functions, same hardware
6. ABS manages longitudinal grip (braking); ESC manages lateral grip (stability) — linking back to Day 21's friction circle

---

## Preparation for Day 25

**Instructor prep:**
- Prepare a four-wheel alignment machine demonstration (or printouts of alignment reports if machine unavailable)
- Prepare tyre wear sample photos or actual worn tyres showing: inner edge wear (toe/camber), outer edge wear, centre wear, shoulder wear, cupping/scalloping
- Design a chassis fault diagnosis scenario card: customer complaint, symptoms, and hidden root cause for pairs to work through
- Ensure scan tool and workshop vehicle are available for continued diagnostic practice
- Print a one-page "Chassis Systems Integration Map" showing how Days 21-24 connect

**Learner prep:**
- Review notes from Days 21-24 (suspension/dynamics, steering, mechanical brakes, ABS/ESC)
- Be prepared to work through a complete diagnostic scenario from complaint to root cause
- Bring notebook with sensor readings and fault codes from today's practical
