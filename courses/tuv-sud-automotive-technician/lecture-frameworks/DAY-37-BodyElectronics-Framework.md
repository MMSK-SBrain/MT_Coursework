---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 8
week_title: "The Complete Technician"
day_number: 37
session_title: "Body Electronics — The BCM and Everything It Controls"
duration_minutes: 180
theory_practice: "35:65"
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 37: Body Electronics — The BCM and Everything It Controls
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (50 min theory + 100 min practical + 15 min setup/transitions + 15 min wrap-up)
**Approach:** System-by-System Exploration with Hands-On Verification
**PPT Target:** 26-28 slides
**Week:** 8 of 8 — "The Complete Technician"

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Explain how an immobiliser system authenticates a key before allowing engine start
- Describe the power window motor, regulator mechanism, and anti-pinch safety feature
- Explain central locking operation including actuators, remote fob, and deadlock
- Differentiate between conventional key, keyless entry, and keyless start systems
- Describe wiper motor operation and how a rain sensor works using an optical principle
- Explain electric mirror adjustment, heating, auto-folding, and auto-dimming functions
- Trace the horn circuit through the clock spring to the steering wheel button
- Describe sunroof operation and explain why blocked drain tubes cause cabin leaks
- Read instrument cluster warning lights and categorise them by colour severity
- Test power window motors, central locking actuators, mirror heating elements, rain sensors, and horn circuits using appropriate tools

**This is Day 37 — Week 8, Day 2.** Learners completed lighting systems yesterday on Day 36. Today they meet every other body electronic system the BCM controls. By the end of today, they will have practical diagnostic experience across the full range of body comfort and convenience systems.

---

## Connection to Prior Knowledge

**Day 36** covered exterior and interior lighting — headlights, tail lights, indicators, DRLs, adaptive systems, and CAN-controlled lighting networks. Today builds directly on that foundation because every system covered today is controlled by the same module: the Body Control Module.

**Bridge:** "Yesterday you lit up the car. Today we power up everything else the BCM touches — from the key in your pocket to the wipers on the windscreen, from the mirrors that fold when you lock the car to the instrument cluster that tells you something is wrong. The BCM is the busiest computer in the car. Let's find out why."

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: The BCM — The Busiest Computer in the Car** (Slides 1-3, ~10 minutes)

**Narrative Voice:** Confident, connecting yesterday's lighting to today's broader BCM landscape. Frame the BCM as the one module that touches more driver-facing features than any other.

---

#### Slide 1: Title & Day Connection
**Visual:** Professional title slide — image of a BCM module with wiring harness connections fanning out in every direction, overlaid with icons representing windows, locks, wipers, mirrors, horn, instrument cluster, immobiliser, sunroof

**Instructor Narration:**
> "Yesterday we covered lighting — and you saw how the BCM controls headlights, indicators, DRLs, and interior lights through CAN bus commands and smart switching. But lighting is only about a quarter of what the BCM does. Today we meet the rest. Immobiliser. Power windows. Central locking. Keyless entry. Wipers. Mirrors. Horn. Sunroof. Instrument cluster. By the end of today, you'll understand every major body electronic system on a modern vehicle."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 8: The Complete Technician
Day 37: Body Electronics — The BCM and Everything It Controls

Yesterday: Lighting systems
Today: Every other body system the BCM manages
```

---

#### Slide 2: What the BCM Actually Controls
**Visual:** Central BCM icon with radiating lines to labelled system icons — immobiliser, windows, locks, keyless, wipers, mirrors, horn, sunroof, instrument cluster, lighting (greyed out as "Day 36")

**Instructor Narration:**
> "Look at this diagram. The Body Control Module is the central hub for comfort and convenience. It receives inputs from dozens of switches, sensors, and remote signals. It sends commands to motors, actuators, relays, and solenoids all over the vehicle. Yesterday's lighting — that's one spoke. Today we cover the other nine. The BCM communicates with these systems partly through direct wired connections and partly over CAN bus. It also talks to the engine ECU, the instrument cluster, and the alarm system. No other module in the car has this many connections."

**PPT Content:**
```
THE BODY CONTROL MODULE (BCM) — CENTRAL HUB

INPUTS the BCM receives:
- Key/transponder signal          - Door lock buttons
- Window switches                 - Wiper/washer stalk
- Mirror adjustment switches      - Horn button
- Rain sensor                     - Sunroof switch
- Door ajar switches              - Remote key fob signal
- Ignition position               - CAN bus messages from other ECUs

OUTPUTS the BCM commands:
- Window motors                   - Lock actuators
- Wiper motors                    - Washer pump
- Mirror motors & heaters         - Horn relay
- Sunroof motor                   - Immobiliser relay
- Instrument cluster data (CAN)   - Interior lighting (Day 36)
```

---

#### Slide 3: Today's Plan
**Visual:** Horizontal timeline — four blocks: Theory Tour, Practical Station 1 (Windows/Locks/Rain Sensor), Practical Station 2 (Mirror/Cluster/Horn), Wrap-Up

**Instructor Narration:**
> "Here's how the day runs. First 40 minutes: I'll walk you through every system — how it works, what fails, and what the customer complains about. Then we go hands-on for 100 minutes across six practical exercises. You'll test a power window motor and its anti-pinch feature. You'll test a central locking actuator. You'll activate a rain sensor. You'll measure a mirror heating element with a multimeter. You'll do a warning light identification exercise on an instrument cluster. And you'll trace a horn circuit through the clock spring. Busy day. Let's get into it."

**PPT Content:**
```
TODAY'S PLAN (180 minutes)

THEORY (40 min): System-by-system tour
- Immobiliser, windows, locks, keyless, wipers,
  mirrors, horn, sunroof, instrument cluster

PRACTICAL STATIONS (100 min):
1. Power window motor + anti-pinch test
2. Central locking actuator test
3. Rain sensor activation test
4. Mirror heating element — multimeter measurement
5. Instrument cluster warning light ID exercise
6. Horn circuit tracing through clock spring

WRAP-UP (15 min): Recap + Day 38 preview
```

---

### **DEVELOPMENT: System-by-System Tour** (Slides 4-16, ~40 minutes)

**Narrative Voice:** Technical, systematic, connecting each system back to the BCM. Use real fault scenarios throughout — "what the customer says" vs. "what's actually wrong."

---

#### Slide 4: Immobiliser — The Car Won't Start Without the Right Key
**Visual:** Diagram showing transponder chip inside key head, antenna ring around ignition barrel, immobiliser ECU (often integrated into BCM), and connection to engine ECU. Signal flow arrows showing challenge-response sequence.

**Instructor Narration:**
> "Let's start with security. The immobiliser system prevents the engine from starting unless the correct key is present. Inside every modern car key there's a tiny transponder chip — no battery needed, it's powered by the antenna ring around the ignition barrel. When you turn the key or press the start button, the antenna ring sends out a radio frequency signal that energises the transponder. The transponder responds with a coded signal. The immobiliser ECU — often built into the BCM — checks that code against its stored database.
>
> Here's the critical part: the system uses rolling codes. Every time you start the car, a new code is generated. This means you can't simply copy the signal. It also means that if you buy a new blank key, it has no code — it must be programmed to the vehicle using diagnostic equipment. The dealer or a qualified locksmith uses a scan tool to enter the new key's transponder ID into the immobiliser ECU's memory. Some manufacturers require a security PIN or an online authentication to do this.
>
> The most common immobiliser fault you'll see: the customer turns the key, the engine cranks — the starter motor spins — but the engine won't fire. The immobiliser warning light on the dashboard is flashing. That tells you the BCM didn't recognise the key. The engine ECU has been told 'don't allow fuel injection and ignition.' Causes? Damaged transponder chip in the key, faulty antenna ring, or a BCM software glitch. First diagnostic step: try the spare key. If the spare works, the original key's transponder is the problem."

**PPT Content:**
```
IMMOBILISER SYSTEM

How it works:
1. Key inserted or brought near start button
2. Antenna ring (around ignition barrel) energises transponder chip in key
3. Transponder sends coded signal back
4. BCM/immobiliser ECU verifies code against stored database
5. If MATCH: BCM tells engine ECU "OK to start"
6. If NO MATCH: engine cranks but will NOT start (no fuel/spark)

Rolling codes:
- Code changes with every start event
- Prevents signal copying/replay attacks
- New key = blank transponder = MUST be programmed via scan tool

Common fault scenario:
SYMPTOM: Engine cranks, won't start, immobiliser light FLASHING
CAUSE: BCM does not recognise key transponder
FIRST STEP: Try the spare key

Components:
- Transponder chip (inside key — passive, no battery)
- Antenna ring (around ignition barrel)
- Immobiliser ECU (often integrated into BCM)
- Engine ECU (receives start authorisation via CAN)
```

---

#### Slide 5: Why a New Key Needs Programming
**Visual:** Step-by-step illustration: blank key -> scan tool connected to OBD port -> BCM learns new key ID -> key now starts vehicle. Show "Security PIN required" callout.

**Instructor Narration:**
> "Customers always ask: 'Why can't I just get a key cut and use it?' The mechanical blade can be cut — that gets you into the door. But the transponder is blank. The BCM has no record of it. Think of it like a new employee with no ID badge — they can walk up to the building, but the door won't open for them.
>
> Programming requires a diagnostic scan tool connected to the OBD-II port, the correct security PIN or online dealer authentication, and the physical presence of all existing keys. Some vehicles limit the number of keys that can be programmed — usually 8. Some require you to present all existing keys during the procedure so the system can re-register them all simultaneously. Lose all your keys? The BCM or immobiliser module may need to be replaced or reflashed — an expensive job. This is why we always tell customers: keep your spare key safe."

**PPT Content:**
```
WHY A NEW KEY MUST BE PROGRAMMED

Blank key = correct blade cut + EMPTY transponder
BCM has never seen this key -> will NOT authorise start

Programming process:
1. Connect scan tool to OBD-II port
2. Enter vehicle security PIN (or online authentication)
3. Present all existing keys + the new key
4. Scan tool writes new transponder ID into BCM memory
5. Test start with new key

Key facts:
- Maximum ~8 keys per vehicle (manufacturer-dependent)
- All existing keys usually must be present during programming
- Lost ALL keys? BCM/immobiliser module may need replacement
- Key programming is a revenue service for workshops

CUSTOMER ADVICE: "Always keep your spare key in a safe place"
```

---

#### Slide 6: Power Windows — Motor, Regulator, and Anti-Pinch
**Visual:** Cross-section of a car door showing window motor, cable-type regulator mechanism (cables, pulleys, guide rails), and the glass panel. Inset showing scissor-type regulator for comparison.

**Instructor Narration:**
> "Power windows. Simple in concept, clever in execution. Each door has an electric motor — usually a small DC motor with a worm gear for self-locking, meaning the window stays where you put it even when the motor is off. The motor drives a regulator mechanism that converts rotary motion into the vertical movement of the glass.
>
> Two main regulator types. Cable-type: the motor pulls a steel cable over pulleys, and the cable is attached to a carrier that holds the glass. This is the most common type today — lighter, cheaper, takes up less space in the door. Scissor-type: the motor drives a gear that extends or collapses a scissor arm linkage. Older design, heavier, but very robust. You'll see this on trucks and older European vehicles.
>
> Now — the safety feature. Anti-pinch. This is legally required for one-touch-up windows. The system monitors the motor current or uses a Hall-effect sensor to measure the window's position and speed. If the window hits an obstruction — a child's hand, a dog's head — the resistance increases, the motor current spikes, and the BCM immediately reverses the window direction. It drops the glass a few centimetres to release whatever was trapped. This must work reliably. If you replace a window motor or disconnect the battery, the anti-pinch system often needs recalibration — you run the window fully down, then fully up, and the BCM learns the full travel endpoints."

**PPT Content:**
```
POWER WINDOWS

Motor:
- DC motor with worm gear (self-locking)
- BCM controls direction via polarity reversal
- One-touch up/down on driver's window (often all windows)

Regulator types:
- CABLE TYPE: Motor -> cable over pulleys -> glass carrier (most common)
- SCISSOR TYPE: Motor -> gear -> scissor arm linkage (older, heavy-duty)

ANTI-PINCH SAFETY (legally required for one-touch-up):
- BCM monitors motor current / Hall sensor position
- Obstruction detected -> motor current spike
- BCM immediately REVERSES window direction
- Glass drops ~50 mm to release obstruction

After battery disconnect or motor replacement:
- Anti-pinch needs RECALIBRATION
- Procedure: full down -> hold -> full up -> hold
- BCM learns endpoint positions
```

---

#### Slide 7: Central Locking — Actuators, Remote, and Deadlock
**Visual:** Cutaway of a door lock mechanism showing the lock actuator (solenoid or DC motor), linkage rods, lock barrel, and door handle connection. Separate inset showing key fob with RF antenna icon.

**Instructor Narration:**
> "Central locking. When you press the lock button on your key fob, every door locks simultaneously. How? Each door has a lock actuator — either a solenoid or a small DC motor that physically moves the lock mechanism. The key fob transmits a coded radio frequency signal. The BCM's RF receiver picks it up, verifies the rolling code, and commands all four door actuators to lock or unlock.
>
> Now, there are two levels of locking on many vehicles. Standard lock: the doors lock, but you can still open from the inside using the interior door handle. This is the normal state. Deadlock: press the fob lock button twice, and the interior handle is mechanically disconnected. You cannot open the door from inside OR outside without the key. This is a theft-deterrent feature. Some vehicles with deadlock also have an ultrasonic interior sensor — it detects movement inside the cabin after deadlock is engaged and triggers the alarm. Purpose: if someone breaks a window and reaches in, the alarm sounds before they can get in.
>
> Child safety lock: this is a separate mechanical feature on the rear doors. A small lever on the door edge, visible when the door is open, disables the interior door handle. Children in the back seat cannot open the door from inside. It's mechanical — no electronics — but customers often confuse it with a central locking fault. 'My rear door won't open from inside!' Check the child lock lever first."

**PPT Content:**
```
CENTRAL LOCKING

Actuators:
- One per door (+ boot/tailgate)
- Solenoid type or DC motor type
- Moves lock mechanism linkage

Remote key fob:
- RF transmitter in key fob
- BCM RF receiver verifies rolling code
- Single press: lock/unlock all doors simultaneously

DEADLOCK (double lock):
- Press lock button TWICE
- Interior door handle DISCONNECTED mechanically
- Cannot open from inside or outside without key
- Theft deterrent — prevents reach-in opening

Ultrasonic interior sensor:
- Active during deadlock
- Detects cabin movement -> triggers alarm
- Prevents break-in after window smash

CHILD SAFETY LOCK (rear doors):
- Mechanical lever on door edge
- Disables interior handle only
- No electronics — common misdiagnosis!
- Customer says "door won't open from inside" -> check child lock first
```

---

#### Slide 8: Keyless Entry and Keyless Start
**Visual:** Diagram showing vehicle with proximity sensor zones (door handles, boot, cabin), smart key fob with LF/RF antennas, push-button start, and brake pedal interlock. Inset showing relay attack concept with two attackers.

**Instructor Narration:**
> "Keyless entry takes the remote fob concept further. The key stays in your pocket. When you approach the vehicle and touch the door handle, an antenna in the handle sends a low-frequency challenge signal. If your smart key is within range — typically about 1.5 metres — it responds with an encrypted code. The BCM verifies the code and unlocks the door. No button press needed.
>
> Keyless start works the same way but inside the cabin. With the smart key in your pocket or bag, you press the brake pedal and push the start button. The BCM sends a challenge through interior antennas, the key responds, and the engine starts. The brake pedal interlock is a safety feature — you must physically press the brake before the start button will work. This prevents accidental starts.
>
> Now — the vulnerability you need to know about. Relay attack. Two thieves work together. One stands near your front door at home with a signal amplifier. The other stands next to your car with a relay device. The amplifier captures the low-frequency signal from the car's door handle antenna and relays it to the key inside your house. The key thinks the car is right next to it and responds. The relay sends that response back to the car. The car unlocks. They drive away. All in under 30 seconds.
>
> How do customers protect themselves? Faraday pouches — signal-blocking bags that prevent the key from receiving the relay signal. Some manufacturers now add motion sensors to the key — if the key hasn't moved for a few minutes, it stops responding to signals. As technicians, you should be aware of this vulnerability because customers will ask about it."

**PPT Content:**
```
KEYLESS ENTRY & KEYLESS START

Keyless entry:
- Antenna in door handle sends LF (low frequency) challenge
- Smart key within ~1.5 m responds with encrypted RF code
- BCM verifies -> unlocks doors
- No button press — just touch the door handle

Keyless start:
- Interior antennas detect key inside cabin
- Press brake pedal + press START button
- BCM verifies key -> authorises engine start
- Brake pedal interlock = safety feature (prevents accidental start)

RELAY ATTACK VULNERABILITY:
- Thief 1: signal amplifier near your house (captures key signal)
- Thief 2: relay device near your car (retransmits to car)
- Car thinks key is present -> unlocks and starts
- Takes < 30 seconds

Protection:
- Faraday pouch (signal-blocking bag for key)
- Motion-sensor keys (stop responding if stationary)
- Software updates from manufacturers
```

---

#### Slide 9: Wipers — Front Motor, Speeds, and Linkage
**Visual:** Diagram of front wiper system — wiper motor with crank arm, linkage connecting to two wiper arms, pivot points. Show the three speed positions: intermittent, slow, fast.

**Instructor Narration:**
> "Wipers. Mechanically simple, electrically controlled. The front wiper motor is a DC motor, usually mounted at the base of the windscreen under the scuttle panel. It drives a crank arm that converts rotary motion into the sweeping arc of the wiper blades through a linkage system.
>
> Three operating modes. Intermittent — the motor runs briefly, pauses, runs again. The pause interval is usually adjustable via the stalk switch. Slow continuous. Fast continuous. The BCM controls which mode is active based on the stalk position. Inside the motor assembly, there's a park switch — a set of contacts that keeps the motor running until the blades reach their parked position at the bottom of the windscreen. If you turn the wipers off mid-sweep, the motor doesn't just stop — it continues to the park position. This is the park switch at work.
>
> Common faults: wiper motor runs but blades don't move — the linkage has disconnected or the splines on the wiper arm are stripped. Wipers park in the wrong position — the park switch is misaligned or faulty. Wipers work on fast but not slow — the brush or speed winding inside the motor is worn."

**PPT Content:**
```
FRONT WIPER SYSTEM

Motor:
- DC motor under scuttle panel (base of windscreen)
- Crank arm converts rotation -> sweeping arc
- Linkage connects motor to both wiper arms

Operating modes (controlled by BCM via stalk switch):
1. INTERMITTENT — motor runs, pauses, repeats (adjustable interval)
2. SLOW continuous
3. FAST continuous

Park switch:
- Inside motor assembly
- Keeps motor running until blades reach park position
- Ensures wipers always return to bottom of windscreen

Common faults:
- Motor runs, blades don't move -> linkage disconnected / stripped splines
- Wrong park position -> park switch fault
- Only works on fast -> internal winding or brush wear
```

---

#### Slide 10: Rain Sensor — Optical Principle
**Visual:** Cross-section diagram of rain sensor mounted on windscreen — LED emitter, light guide prism bonded to glass, photodiode receiver. Show light path: total internal reflection on dry glass vs. light escaping through water droplets on wet glass.

**Instructor Narration:**
> "The rain sensor is one of those clever pieces of technology that customers take for granted until it fails. It's a small optical unit bonded to the inside of the windscreen, usually behind the rear-view mirror.
>
> Here's how it works. An infrared LED inside the sensor shines light into the windscreen glass at an angle. On a dry windscreen, total internal reflection keeps the light bouncing inside the glass, and it returns to a photodiode receiver at high intensity. When rain hits the outside surface, the water changes the refractive index at the glass-air boundary. Light escapes through the water droplets instead of reflecting back. The photodiode receives less light. The sensor tells the BCM: 'It's raining.'
>
> The BCM then activates the wipers automatically and adjusts the speed based on how much light is lost — light rain gets intermittent wipes, heavy rain gets continuous fast wipes. If you replace a windscreen, the rain sensor must be carefully rebonded to the new glass with the correct optical gel. Air bubbles in the gel will cause false readings. And if a customer complains that their auto wipers activate randomly on a dry day — check for contamination on the sensor area of the windscreen, or a poorly bonded sensor."

**PPT Content:**
```
RAIN SENSOR — OPTICAL PRINCIPLE

Construction:
- Infrared LED + photodiode + light guide prism
- Bonded to INSIDE of windscreen (usually behind rear-view mirror)
- Optical gel ensures light coupling between sensor and glass

How it works:
DRY: LED light enters glass -> total internal reflection -> returns
     to photodiode at FULL intensity -> wipers OFF

WET: Rain on outer surface changes refractive index
     Light ESCAPES through water droplets
     Photodiode receives LESS light -> BCM activates wipers

Rain intensity = amount of light loss:
- Light loss small -> intermittent wipes
- Light loss large -> continuous fast wipes

Service notes:
- Windscreen replacement: rebond sensor with correct optical gel
- No air bubbles in gel (causes false readings)
- Random wiper activation on dry day -> check sensor bonding/contamination
```

---

#### Slide 11: Rear Wiper, Washer Pump, and Heated Jets
**Visual:** Diagram showing washer fluid reservoir, washer pump (often dual outlet — front and rear), heated washer jets on bonnet, rear wiper motor on tailgate hatch

**Instructor Narration:**
> "The rear wiper is simpler than the front — a single motor mounted inside the tailgate, driving a single arm. It usually only has one speed plus intermittent. On many vehicles, the rear wiper activates automatically when you select reverse gear if the front wipers are running. The BCM makes that decision.
>
> The washer system: a reservoir — usually in the front wing area, 2 to 5 litres capacity — with an electric pump. Many vehicles have a dual-outlet pump or two separate pumps: one for the front washers, one for the rear. The pump pressurises the fluid and sends it to nozzles on the bonnet or wiper arms.
>
> Heated washer jets: in cold climates, washer fluid can freeze in the nozzles. Small heating elements inside the jet housings prevent this. They're powered by the BCM when the ignition is on and ambient temperature is low. If a customer says 'my washers don't work in winter but work fine in summer,' check the jet heaters and the washer fluid — is it the correct winter-grade concentration?"

**PPT Content:**
```
REAR WIPER, WASHER PUMP & HEATED JETS

Rear wiper:
- Single motor in tailgate
- One speed + intermittent
- Many vehicles: auto-activates in reverse if front wipers are on

Washer system:
- Reservoir (2-5 litres) in front wing area
- Electric pump (dual outlet or two pumps: front + rear)
- Nozzles on bonnet or wiper arms
- BCM triggers pump when washer stalk is pulled

Heated washer jets:
- Small heating element inside each jet housing
- BCM powers them when ignition ON + ambient temp is low
- Prevents washer fluid freezing in nozzle

Winter fault: "Washers don't work in cold weather"
-> Check: heated jet element, washer fluid concentration, frozen lines
```

---

#### Slide 12: Electric Mirrors — Adjustment, Heat, Fold, and Dim
**Visual:** Exploded view of a door mirror assembly showing: mirror glass, two adjustment motors (horizontal + vertical), heating element behind glass, folding motor in base, and electrochromic dimming layer in glass. Each component labelled.

**Instructor Narration:**
> "Door mirrors are more complex than they look. Let's go through each function.
>
> Electric adjustment: two small DC motors behind the mirror glass — one for horizontal tilt, one for vertical tilt. The driver uses a joystick switch to adjust. The BCM commands the appropriate motor. Some vehicles have memory positions linked to the driver's seat memory — adjust the seat, and the mirrors follow.
>
> Heated element: a resistive heating pad bonded to the back of the mirror glass. It clears fog and ice. On most vehicles, it activates with the rear window demister button. Typical power: 15 to 25 watts per mirror. You can test it with a multimeter — measure the resistance of the element. A good element will show 5 to 15 ohms. Open circuit means the element is broken.
>
> Auto-folding: a motor in the mirror base folds the mirror flat against the door. Activates when you lock the vehicle — convenient in narrow parking spaces. The BCM commands the fold motor on lock and unfold on unlock.
>
> Auto-dimming: the driver's mirror and sometimes the door mirrors use electrochromic technology. A sensor detects bright light from behind — headlights of the car following you. A voltage is applied to the electrochromic gel layer in the mirror glass, which darkens to reduce glare. Remove the voltage, and the mirror clears. The driver's interior mirror usually has its own control module; the door mirrors may receive the dimming command from the BCM via CAN."

**PPT Content:**
```
ELECTRIC MIRRORS — FOUR FUNCTIONS

1. ADJUSTMENT:
   - Two DC motors: horizontal + vertical tilt
   - Joystick switch -> BCM -> motor command
   - Memory positions linked to seat memory (some vehicles)

2. HEATED ELEMENT:
   - Resistive pad behind mirror glass
   - Activates with rear demister button
   - Power: 15-25W per mirror
   - TEST: Multimeter on element — expect 5-15 ohms
   - Open circuit (OL) = broken element

3. AUTO-FOLDING:
   - Motor in mirror base
   - BCM folds on lock, unfolds on unlock
   - Convenient for tight parking

4. AUTO-DIMMING (electrochromic):
   - Light sensor detects glare from behind
   - Voltage applied -> electrochromic gel darkens glass
   - Voltage removed -> glass clears
   - Reduces night-time glare from following vehicles
```

---

#### Slide 13: Horn Circuit and the Clock Spring
**Visual:** Circuit diagram showing: battery -> fuse -> horn relay (BCM-controlled) -> horn unit (electromagnetic). Separate diagram of clock spring in steering column — coiled ribbon cable allowing steering wheel rotation while maintaining electrical connections. Arrow showing horn button on steering wheel connected through clock spring to BCM.

**Instructor Narration:**
> "The horn is simple in concept but has an interesting connection path. The horn unit itself is electromagnetic — a coil pulls an armature against a diaphragm, producing sound. Most vehicles have two horns tuned to different frequencies for a fuller sound.
>
> Power comes from the battery through a fuse to a horn relay. The BCM controls the relay ground. When you press the horn button on the steering wheel, the signal has to travel from a rotating component — the steering wheel — to the stationary wiring of the car. This is where the clock spring comes in.
>
> The clock spring is a coiled flat ribbon cable inside a housing in the steering column, behind the steering wheel. It's wound in a spiral so that as the steering wheel turns left and right, the ribbon cable coils and uncoils without breaking. It carries multiple circuits: horn, airbag, steering wheel buttons (audio controls, cruise control), and sometimes the steering angle sensor signal.
>
> Critical point: if you ever remove a steering wheel — for an airbag replacement, clock spring replacement, or steering rack work — you must centre the clock spring before refitting the wheel. If it's off-centre, turning the steering to full lock will snap the ribbon cable. That kills the horn, the airbag circuit, and all steering wheel controls. And an airbag fault means an MIL on the dashboard and a failed safety inspection."

**PPT Content:**
```
HORN CIRCUIT & CLOCK SPRING

Horn unit:
- Electromagnetic: coil + armature + diaphragm
- Usually TWO horns (different frequencies for fuller sound)
- Mounted behind front bumper / in engine bay

Circuit:
Battery -> Fuse -> Horn relay (BCM-controlled) -> Horn(s) -> Ground

Horn button signal path:
Horn button (steering wheel) -> CLOCK SPRING -> BCM -> relay ground

CLOCK SPRING:
- Coiled flat ribbon cable inside steering column housing
- Allows steering wheel rotation while maintaining electrical connections
- Carries: horn, airbag, audio controls, cruise control signals

CRITICAL SERVICE NOTE:
- Removing steering wheel? CENTRE the clock spring before refitting
- Off-centre = ribbon cable snaps at full lock
- Result: loss of horn, airbag fault, steering wheel buttons dead
- Airbag fault = MIL warning + failed safety inspection
```

---

#### Slide 14: Sunroof — Motor, Limits, and Drain Tubes
**Visual:** Top-down cutaway of a sunroof system showing: glass panel, motor and gear mechanism, guide rails, limit switches (open, closed, tilt positions), and the four drain tubes running from each corner down through the A and C pillars to exit beneath the vehicle.

**Instructor Narration:**
> "The sunroof. A motor drives the glass panel along guide rails through a cable or gear mechanism. Limit switches or position sensors tell the BCM when the panel is fully open, fully closed, or in the tilt position. Like the power windows, sunroofs with one-touch operation have an anti-pinch feature — if the closing glass meets resistance, the motor reverses.
>
> Now — the number one sunroof complaint. Water leaks into the cabin. And here's the thing most customers don't understand: the sunroof seal is NOT watertight. It's designed to deflect most water, but some always gets past the seal into a channel — a trough around the glass panel. That water is supposed to drain away through four small rubber tubes — one at each corner. These tubes run down through the A-pillars at the front and C-pillars at the rear, exiting underneath the vehicle.
>
> The problem: leaves, dirt, and debris clog these drain tubes over time. Water backs up in the trough, overflows, and runs into the headliner, down the A-pillar trim, and into the footwell. Customer says: 'My car leaks when it rains.' Check the sunroof drains. Clearing them is usually a simple job — compressed air or a thin flexible wire pushed through the tube. But if it's been leaking for months, you might find corrosion, mould, and damaged electronics under the carpet. Prevention is key — add drain tube cleaning to your service checklist."

**PPT Content:**
```
SUNROOF SYSTEM

Operation:
- Motor + cable/gear mechanism drives glass panel on guide rails
- Positions: closed, tilt (vent), slide open
- Limit switches or position sensors report to BCM
- Anti-pinch on one-touch close (same principle as power windows)

DRAIN TUBES — THE #1 SUNROOF ISSUE:
- Sunroof seal is NOT fully watertight (by design)
- Water enters trough channel around glass panel
- FOUR drain tubes (one per corner) carry water away
  - Front tubes: through A-pillars
  - Rear tubes: through C-pillars
  - Exit underneath vehicle

Blocked drains:
- Leaves/debris clog tubes over time
- Water overflows trough -> into headliner -> down pillars -> footwell
- Causes: water-stained headliner, wet carpet, corroded electronics

Fix: Compressed air or flexible wire through tubes
Prevention: Add drain tube check to every service inspection
```

---

#### Slide 15: Instrument Cluster — The Driver's Information Centre
**Visual:** Modern instrument cluster showing analogue or digital speedometer, tachometer, fuel gauge, temperature gauge, and a matrix of warning lights. Colour-coded legend: red lights, amber lights, green/blue lights.

**Instructor Narration:**
> "The instrument cluster is the driver's window into the car's health. In older vehicles, the cluster had direct connections to sensors — the fuel sender, the temperature sender, the speed sensor. Modern clusters receive almost everything over CAN bus. The engine ECU sends RPM and coolant temperature. The ABS module sends vehicle speed. The BCM sends fuel level, exterior temperature, and lighting status. The cluster is essentially a display terminal for the entire CAN network.
>
> Now — warning lights. This is something you need to know cold, because customers will call and ask: 'There's a light on my dashboard, what does it mean?' The colour coding is universal. Red means STOP. Pull over, turn off the engine, do not drive further. Oil pressure, coolant temperature, battery charge, brake system — these are red. Amber means CAUTION. Something needs attention soon but is not immediately dangerous. Engine management light (MIL), ABS, tyre pressure, service due — these are amber. Green and blue are INFORMATION only. Indicators, high beams, cruise control active, eco mode — these are green or blue. They tell you a system is active, not that something is wrong.
>
> One specific light to highlight: the engine management light — the MIL. It looks like an engine outline. When it illuminates steady amber, it means the engine ECU has detected a fault and stored a diagnostic trouble code. When it flashes, it means an active misfire is occurring — and the catalytic converter is at risk of damage. Flashing MIL = reduce speed and get to a workshop immediately."

**PPT Content:**
```
INSTRUMENT CLUSTER

Data sources (modern vehicle — all via CAN bus):
- Engine ECU: RPM, coolant temperature
- ABS module: vehicle speed
- BCM: fuel level, exterior temp, lighting status
- Transmission ECU: gear position, transmission temp
- Airbag ECU: airbag readiness status

WARNING LIGHT COLOUR CODE:

RED = STOP — Immediate danger, do not drive
  - Oil pressure      - Engine temperature
  - Battery/charging  - Brake system
  - Airbag fault      - Power steering

AMBER = CAUTION — Attention needed soon
  - Engine management (MIL)   - ABS
  - Tyre pressure (TPMS)      - Service due
  - Traction control off      - DPF warning

GREEN / BLUE = INFORMATION — System active
  - Indicators        - High beam (blue)
  - Cruise control    - Eco mode
  - DRL active        - Parking sensors active

MIL (Engine Management Light):
- Steady amber = fault code stored, book service
- FLASHING = active misfire — reduce speed, attend workshop NOW
```

---

#### Slide 16: Putting It All Together — The BCM Network Map
**Visual:** Complete BCM network diagram showing all the systems covered today connected to a central BCM icon, with CAN bus connections to engine ECU, instrument cluster, and airbag module. Power supply lines, ground connections, and fuse locations indicated.

**Instructor Narration:**
> "There's your complete picture. The BCM sits at the centre of all these body electronic systems. It receives input from switches, sensors, key fobs, and CAN bus messages. It commands motors, actuators, relays, heaters, and pumps. It communicates with the engine ECU for immobiliser authorisation, with the instrument cluster for warning displays, and with the airbag module for crash-related functions like automatic door unlock.
>
> When you're diagnosing a body electronics fault, always start at the BCM. Check the power supply and ground to the BCM first — if it's lost power, nothing works. Then check CAN bus communication — if the BCM can't talk to other modules, features will fail even though the BCM itself is healthy. Then check the specific circuit — the window motor, the lock actuator, the wiper motor. Work from the centre outward."

**PPT Content:**
```
THE BCM — COMPLETE NETWORK MAP

BCM CENTRAL FUNCTIONS:
- Receives: switches, sensors, RF signals, CAN messages
- Commands: motors, actuators, relays, heaters, pumps
- Communicates: Engine ECU, instrument cluster, airbag, alarm

DIAGNOSTIC APPROACH FOR BODY ELECTRONICS:
1. CHECK BCM power supply and ground FIRST
   - No power = no body electronics at all
2. CHECK CAN bus communication
   - BCM can't talk to network = features fail
3. CHECK specific circuit (motor, actuator, sensor)
   - Use wiring diagram for pin-by-pin testing

Common BCM-related DTCs:
- U-codes: Communication faults (CAN bus)
- B-codes: Body system faults (specific component)
- Always read BCM fault codes alongside engine/ABS codes
```

---

### **PRACTICAL: Hands-On Testing Stations** (Slides 17-24, ~100 minutes)

**Narrative Voice:** Direct, instructional, safety-conscious. Hands-on workshop mode.

---

#### Slide 17: Practical Overview and Safety Reminders
**Visual:** Six station icons numbered 1-6 with timing allocations. Safety callout: "Battery connected for these tests — observe polarity. Airbag precautions near clock spring."

**Instructor Narration:**
> "Six practical exercises. You'll rotate in pairs. Each station has a task card with step-by-step instructions. I'll demonstrate each one first, then you do it. Safety reminders: the battery will be connected for these tests — that means live circuits. Observe polarity when connecting test equipment. At the clock spring station, do NOT disturb airbag connections — we're only tracing the horn circuit. If anything doesn't seem right, call me over before you proceed."

**PPT Content:**
```
PRACTICAL STATIONS (100 minutes)

Station 1: Power window motor + anti-pinch test (20 min)
Station 2: Central locking actuator test (15 min)
Station 3: Rain sensor activation test (15 min)
Station 4: Mirror heating element — multimeter (15 min)
Station 5: Instrument cluster warning light ID (15 min)
Station 6: Horn circuit trace through clock spring (20 min)

SAFETY:
- Battery CONNECTED — live circuits
- Observe polarity on all connections
- DO NOT disturb airbag connectors at clock spring
- Ask before you disconnect anything
```

---

#### Slide 18: Station 1 — Power Window Motor and Anti-Pinch Test
**Visual:** Photo of a door panel removed showing window motor accessible. Inset showing instructor placing an obstruction (foam block) in the window path. Multimeter connected to motor power feed.

**Instructor Narration:**
> "Station 1. The door panel is removed so you can see the window motor and regulator. Your tasks: First, operate the window using the switch and observe the motor running. Measure the voltage at the motor connector while it operates — you should see approximately 12 volts. Note the polarity reverses when you switch between up and down. Second, test the anti-pinch. Place the foam block provided in the window path and operate the one-touch-up function. The window should reverse within about 5 millimetres of hitting the block. If it doesn't reverse, the anti-pinch has failed — that's a safety concern and would fail an inspection. Third, disconnect the motor connector and measure the motor resistance. A healthy window motor typically shows 1 to 5 ohms. Open circuit means the motor windings are broken."

**PPT Content:**
```
STATION 1: POWER WINDOW MOTOR + ANTI-PINCH TEST

Tasks:
1. OPERATE window via switch — observe motor running
   - Measure voltage at motor connector (expect ~12V)
   - Note polarity reversal between UP and DOWN

2. ANTI-PINCH TEST:
   - Place foam block in window path
   - Activate one-touch-up
   - Window must REVERSE within ~5 mm of obstruction
   - No reversal = anti-pinch failure = safety concern

3. MOTOR RESISTANCE:
   - Disconnect motor connector
   - Measure resistance across motor terminals
   - Healthy motor: 1-5 ohms
   - Open circuit (OL) = broken winding

Record: Voltage reading, anti-pinch pass/fail, motor resistance
```

---

#### Slide 19: Station 2 — Central Locking Actuator Test
**Visual:** Photo of a lock actuator removed from door, connected to a bench power supply with crocodile clips. Actuator shown in both locked and unlocked positions.

**Instructor Narration:**
> "Station 2. You have a central locking actuator removed from a door and sitting on the bench. Your tasks: First, connect it to the bench power supply at 12 volts. Observe it actuate — it should snap to the locked position. Reverse the polarity and it should snap to the unlocked position. Listen for a firm, clean click. A weak or sluggish actuator will cause intermittent lock faults. Second, measure the current draw during actuation. A healthy actuator typically draws 3 to 6 amps momentarily. High current draw suggests mechanical binding. Third, test the actuator with the key fob if the vehicle is available — lock and unlock the car and verify all four doors respond simultaneously. If one door is slow or doesn't respond, that actuator is the suspect."

**PPT Content:**
```
STATION 2: CENTRAL LOCKING ACTUATOR TEST

Tasks:
1. BENCH TEST actuator:
   - Connect to 12V bench supply
   - Apply power -> actuator should snap to LOCK position
   - Reverse polarity -> should snap to UNLOCK position
   - Listen for firm, clean click
   - Weak/sluggish = failing actuator

2. CURRENT DRAW:
   - Measure current during actuation (in-line ammeter or clamp)
   - Healthy actuator: 3-6A momentary
   - High current = mechanical binding inside actuator

3. VEHICLE TEST (if available):
   - Lock/unlock with key fob
   - All four doors should respond simultaneously
   - One slow/dead door = suspect that actuator

Record: Lock/unlock operation, current draw, any faults noted
```

---

#### Slide 20: Station 3 — Rain Sensor Activation Test
**Visual:** Photo showing the rain sensor location on the windscreen (behind rear-view mirror), a spray bottle of water, and the wiper stalk set to AUTO position. Diagnostic scan tool showing rain sensor live data.

**Instructor Narration:**
> "Station 3. With the ignition on and the wiper stalk set to AUTO, you're going to test the rain sensor. Task one: spray a fine mist of water onto the windscreen directly over the rain sensor area. The wipers should activate within one to two seconds. Spray more water — the wiper speed should increase. Remove the water with a cloth — the wipers should slow down and stop. Task two: if a scan tool is available, connect it and read the rain sensor live data. You should see a value that changes with the amount of water on the sensor area — typically a percentage or a raw count. This tells you whether the sensor is functioning and communicating with the BCM. Task three: examine the sensor bonding area. Look for air bubbles, discolouration, or contamination between the sensor and the glass. These cause intermittent false activation — the number one customer complaint with rain sensors."

**PPT Content:**
```
STATION 3: RAIN SENSOR ACTIVATION TEST

Setup: Ignition ON, wiper stalk in AUTO position

Tasks:
1. SPRAY TEST:
   - Fine mist of water over rain sensor area on windscreen
   - Wipers should activate within 1-2 seconds
   - More water -> wiper speed INCREASES
   - Dry the glass -> wipers slow and STOP

2. SCAN TOOL (if available):
   - Read rain sensor live data (BCM module)
   - Value changes with water amount on sensor
   - Confirms sensor communicates with BCM

3. VISUAL INSPECTION:
   - Examine sensor bonding area through windscreen
   - Check for: air bubbles, discolouration, contamination
   - These cause intermittent false wiper activation

Record: Activation response time, wiper speed response, sensor condition
```

---

#### Slide 21: Station 4 — Mirror Heating Element Test with Multimeter
**Visual:** Photo of a door mirror with glass removed, exposing the heating element pad. Multimeter probes touching the two terminals of the heating element. Display showing a resistance value.

**Instructor Narration:**
> "Station 4. The mirror glass has been carefully removed from one door mirror to expose the heating element. Your tasks: First, with the ignition off, measure the resistance of the heating element across its two terminals. A healthy element reads 5 to 15 ohms — the exact value depends on the mirror and manufacturer. Record the reading. If you see open circuit — OL on the multimeter — the element is broken. If you see very low resistance — under 1 ohm — there may be a short circuit in the element, which would blow the fuse.
>
> Second, with the ignition on, activate the rear demister button — this usually powers the mirror heaters simultaneously. Measure the voltage across the element terminals. You should see approximately 12 volts. If you get 12 volts and the element has correct resistance, the system is working. If you get 12 volts but the element is open circuit, the element is faulty. If you get no voltage, trace back to the BCM output and fuse.
>
> Third, after a few minutes with the heater activated, carefully touch the mirror glass — it should feel warm. This is the functional confirmation: power is reaching the element, the element has correct resistance, and it's producing heat."

**PPT Content:**
```
STATION 4: MIRROR HEATING ELEMENT — MULTIMETER TEST

Tasks:
1. RESISTANCE (ignition OFF):
   - Measure across heating element terminals
   - Healthy element: 5-15 ohms
   - Open circuit (OL) = broken element
   - Very low (< 1 ohm) = short circuit (will blow fuse)

2. VOLTAGE (ignition ON + rear demister activated):
   - Measure voltage across element terminals
   - Expect ~12V when heater is active
   - 12V + correct resistance = system working
   - 12V + open circuit = element faulty
   - 0V = trace back to BCM output and fuse

3. FUNCTIONAL CHECK:
   - Leave heater on for 2-3 minutes
   - Touch mirror glass — should feel WARM
   - Confirms: power + element + heat output all working

Record: Element resistance, supply voltage, warm to touch (yes/no)
```

---

#### Slide 22: Station 5 — Instrument Cluster Warning Light Identification
**Visual:** Reference sheet showing 20 common dashboard warning lights with colour and meaning. Blank worksheet for learners to fill in.

**Instructor Narration:**
> "Station 5. This is a knowledge exercise — no tools needed, just your eyes and your brain. You have a reference sheet showing 20 common dashboard warning lights. Your task: study them for five minutes. Then I'll give you a blank worksheet with the same 20 symbols but no labels. You identify each one: name the system, state the colour, and write what the driver should do.
>
> Focus especially on the safety-critical reds: oil pressure, engine temperature, battery charge, brake system warning, airbag. Know the difference between the brake warning light — which can mean the handbrake is on, brake fluid is low, or there's an ABS fault — and the ABS light, which specifically means the ABS module has a fault. And remember the MIL: steady amber is 'book a service,' flashing amber is 'get off the road now.'
>
> This is practical knowledge you'll use every day. Customers call and say 'there's a light on.' You need to tell them immediately: 'Is it red? Stop driving. Is it amber? You can drive to the workshop, but don't delay.'"

**PPT Content:**
```
STATION 5: INSTRUMENT CLUSTER WARNING LIGHT ID

Task:
- Study 20 common warning lights on reference sheet (5 min)
- Complete blank identification worksheet (10 min)
- For each light: NAME + COLOUR + DRIVER ACTION

KEY LIGHTS TO KNOW:

RED (STOP):
- Oil pressure warning      -> Stop engine immediately
- Engine temperature         -> Stop, let engine cool
- Battery/charging           -> Drive to workshop, minimal electrics
- Brake system warning       -> Check: handbrake? fluid? ABS?
- Airbag fault               -> Airbag may not deploy — service urgently

AMBER (CAUTION):
- MIL (engine management)    -> Steady: book service / Flashing: STOP
- ABS warning                -> Brakes work, but ABS inactive
- TPMS (tyre pressure)       -> Check all tyre pressures
- DPF warning                -> Extended driving needed to regenerate

GREEN/BLUE (INFORMATION):
- Indicators / high beam / cruise / eco mode
```

---

#### Slide 23: Station 6 — Horn Circuit Testing Through Clock Spring
**Visual:** Wiring diagram of horn circuit showing: battery -> fuse box -> horn relay -> horn -> ground, with horn button signal path through clock spring to BCM. Photo of clock spring connector at steering column with relevant pins highlighted.

**Instructor Narration:**
> "Station 6. You're going to trace the horn circuit from the horn button to the horn itself. The vehicle is on the bench with the lower steering column cover removed so you can see the clock spring connector. DO NOT disconnect the airbag connector — it's a different plug, usually yellow. We're only working with the horn circuit.
>
> Task one: locate the horn relay in the fuse box and identify the correct fuse using the fuse box diagram. Check the fuse with a multimeter or test light. Task two: with a helper pressing the horn button, use a multimeter to check for a ground signal at the clock spring connector on the horn button pin. When the button is pressed, you should see the pin pulled to ground — approximately 0 volts. When released, the pin floats or returns to battery voltage depending on the system design. This confirms the button and clock spring path are intact.
>
> Task three: locate the horns behind the front bumper. With a helper pressing the horn button, check for 12 volts at the horn connector. If you have 12 volts and the horn doesn't sound, the horn unit is faulty. If you have no voltage, trace back through the relay and wiring."

**PPT Content:**
```
STATION 6: HORN CIRCUIT TESTING THROUGH CLOCK SPRING

SAFETY: Do NOT disconnect yellow airbag connector!
Only work with horn circuit connections.

Tasks:
1. FUSE & RELAY CHECK:
   - Locate horn relay and fuse in fuse box (use diagram)
   - Test fuse: continuity or test light
   - Identify relay pins

2. CLOCK SPRING SIGNAL TEST:
   - Lower steering column cover removed
   - Identify horn button pin at clock spring connector
   - Helper presses horn button
   - Multimeter: pin should pull to GROUND (~0V) when pressed
   - Confirms: horn button + clock spring path intact

3. HORN UNIT TEST:
   - Locate horns behind front bumper
   - Helper presses horn button
   - Check for 12V at horn connector
   - 12V present + no sound = horn unit faulty
   - No voltage = trace back through relay and wiring

Record: Fuse condition, clock spring signal, voltage at horn
```

---

#### Slide 24: Practical Debrief
**Visual:** Summary table with all six stations — columns for expected values and space for learner-recorded actual values

**Instructor Narration:**
> "Gather around. Let's debrief. Station by station — tell me what you found. What voltage did you measure at the window motor? Did the anti-pinch work? What resistance did the mirror element show? How fast did the rain sensor respond? Did anyone find a fault at any station? If so, what was your diagnostic logic — how did you determine what was wrong?
>
> These are the skills that separate a parts-changer from a diagnostic technician. You didn't just test components today — you followed a logical path: check power, check ground, check signal, check component. That's the universal diagnostic method, and it works on every body electronic system."

**PPT Content:**
```
PRACTICAL DEBRIEF — EXPECTED VALUES

Station 1: Window motor voltage ~12V, anti-pinch reverses, motor 1-5 ohms
Station 2: Actuator clicks firmly, current 3-6A, all doors respond
Station 3: Wipers activate < 2 sec, speed varies with water amount
Station 4: Mirror element 5-15 ohms, 12V when active, warm to touch
Station 5: 20/20 warning lights correctly identified
Station 6: Fuse good, clock spring signal to ground, 12V at horn

DIAGNOSTIC LOGIC:
Power -> Ground -> Signal -> Component
This method works for EVERY body electronics fault
```

---

### **WRAP-UP: Consolidation & Preview** (Slides 25-27, ~15 minutes)

---

#### Slide 25: What You Learned Today
**Visual:** Checklist with all systems covered

**Instructor Narration:**
> "Let's recap. Today you've covered every major body electronic system controlled by the BCM. Immobiliser — you understand transponder authentication and why new keys need programming. Power windows — motor, regulator, and the anti-pinch safety system. Central locking — actuators, remote fob, deadlock, and child safety locks. Keyless entry and start — proximity detection and relay attack vulnerability. Wipers and washers — motor, linkage, rain sensor optical principle, and heated jets. Mirrors — adjustment, heating, folding, and electrochromic dimming. Horn — the circuit path through the clock spring. Sunroof — motor, anti-pinch, and those critical drain tubes. And the instrument cluster — CAN bus data display and warning light colour codes.
>
> Yesterday you lit up the car. Today you made it secure, comfortable, and informative for the driver. Between Day 36 and Day 37, you've covered the complete body electronics package."

**PPT Content:**
```
DAY 37 RECAP — YOU CAN NOW:

Immobiliser: Explain transponder authentication + rolling codes
Power Windows: Describe motor, regulator, and anti-pinch safety
Central Locking: Explain actuators, remote fob, deadlock, child lock
Keyless Entry/Start: Describe proximity detection + relay attack risk
Wipers & Washers: Explain motor, linkage, rain sensor optical principle
Mirrors: Describe adjustment, heat, fold, and auto-dimming
Horn: Trace the circuit through the clock spring
Sunroof: Explain operation and drain tube leak prevention
Instrument Cluster: Read warning lights by colour severity

PRACTICAL SKILLS DEMONSTRATED:
- Window motor + anti-pinch test
- Lock actuator bench test
- Rain sensor activation test
- Mirror heater resistance + voltage test
- Warning light identification
- Horn circuit trace through clock spring
```

---

#### Slide 26: Key Takeaways
**Visual:** Five numbered points with icons

**Instructor Narration:**
> "Five things to remember from today. One: the BCM is the busiest module in the car — it controls more driver-facing features than any other ECU. Two: the immobiliser uses rolling codes and requires scan tool programming for new keys — you cannot just cut a key and use it. Three: anti-pinch is a legal safety requirement on one-touch windows and sunroofs — always verify it after any window or sunroof repair. Four: blocked sunroof drain tubes are the number one cause of cabin water leaks — add drain checks to every service. Five: warning light colours are universal — red means stop, amber means caution, green means information. Know them cold."

**PPT Content:**
```
5 KEY TAKEAWAYS

1. BCM = busiest module in the car
   Controls more driver-facing features than any other ECU

2. Immobiliser rolling codes + key programming
   New keys MUST be programmed via scan tool — no shortcuts

3. Anti-pinch = legal safety requirement
   Always verify after window/sunroof motor replacement

4. Sunroof drain tubes = #1 water leak cause
   Add drain tube check to every service inspection

5. Warning light colours are UNIVERSAL
   RED = stop | AMBER = caution | GREEN/BLUE = information
```

---

#### Slide 27: Day 38 Preview
**Visual:** Image of an airbag deployment sequence, seatbelt pretensioner, and SRS warning light

**Instructor Narration:**
> "Tomorrow — Day 38 — we enter the world of supplemental restraint systems. Airbags, seatbelt pretensioners, crash sensors, and the SRS module. This is some of the most safety-sensitive work a technician can do. Pyrotechnic devices that deploy with explosive force. Specific procedures that must be followed exactly. Tomorrow, you'll learn what happens in the first 50 milliseconds of a crash — and why touching the wrong connector can put you in hospital. Rest up. Day 38 demands your full attention."

**PPT Content:**
```
DAY 38 PREVIEW: SUPPLEMENTAL RESTRAINT SYSTEMS (SRS)

- Airbag types and deployment strategies
- Crash sensors and the SRS control module
- Seatbelt pretensioners — pyrotechnic devices
- The 50 ms crash sequence
- Safe working procedures for SRS components
- Why this is the most safety-sensitive work you'll do

Be ready. Full attention required.
```

---

## Assessment Checkpoint

**Formative (not graded):**
- Practical station results: all six stations completed with recorded measurements
- Window motor anti-pinch test: pass/fail correctly identified
- Mirror heating element: resistance within expected range correctly measured
- Warning light identification: minimum 16/20 correctly identified
- Horn circuit: signal path correctly traced from button to horn
- Verbal check: explain how the immobiliser prevents engine start with an unregistered key

---

## Key Takeaways

1. The BCM is the central controller for all body comfort and convenience electronics — more connected than any other module
2. Immobiliser systems use rolling-code transponder authentication — new keys require scan tool programming
3. Anti-pinch on power windows and sunroofs is a legal safety requirement — verify after every motor replacement or battery disconnect
4. Rain sensors work on an optical principle — total internal reflection changes when water is present on the glass
5. Blocked sunroof drain tubes are the most common cause of cabin water leaks — preventive maintenance is key
6. Warning light colours are universal: red = stop, amber = caution, green/blue = information
7. The clock spring carries horn, airbag, and steering wheel control circuits — must be centred during steering wheel removal
8. Diagnostic approach for body electronics: check power, check ground, check signal, check component — work from the BCM outward

---

## Preparation for Day 38

**Instructor prep:**
- Prepare SRS demonstration components (deactivated airbag module, cutaway seatbelt pretensioner, crash sensor)
- Verify all SRS training units are in safe/deactivated state — NO live pyrotechnic devices in classroom
- Print SRS safe working procedure cards
- Prepare vehicle with SRS fault codes for scan tool exercise
- Review manufacturer-specific SRS disconnection procedures for the training vehicle
- Ensure HV-rated insulated gloves and face shields are available (even for non-HV SRS work — best practice)

**Learner prep:**
- Review Day 37 notes on BCM communication and CAN bus
- Recall the airbag and seatbelt concepts from the Day 1 body system overview
- Bring PPE: safety glasses required for all SRS practical work
