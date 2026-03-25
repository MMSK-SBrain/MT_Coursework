---
course_code: "TUV-AST"
course_name: "TUV SUD Automotive Service Technician"
week_number: 6
week_title: "Power Delivery — Transmission & Charging"
day_number: 27
session_title: "Manual Transmission & Clutch"
duration_minutes: 180
theory_practice: "40:60"
author: "Course Generator"
version: "1.0"
last_updated: "2026-03-24"
---

# Day 27: Manual Transmission & Clutch
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 180 minutes (70 min theory + 110 min practical)
**Approach:** Mechanism-Focused — Understand the Parts by Handling Them
**PPT Target:** 26-28 slides
**Week:** 6 of 8 — "Power Delivery — Transmission & Charging"

---

## Session Objectives (For Instructor)

By the end of this session, learners will be able to:
- Explain gear ratio theory: driving gear, driven gear, and the mathematical relationship between them
- Describe how speed reduction produces torque multiplication, and calculate a gear ratio from tooth counts
- Explain the function and internal mechanism of synchronizer rings, including brass cone friction, hub sleeve engagement, and detent spring holding
- Identify all major components inside a manual gearbox: input shaft, layshaft/countershaft, output shaft, bearings, seals, shift forks, selector mechanism, and reverse idler gear
- Name every component in a clutch assembly: friction disc, pressure plate, release bearing, flywheel, and pilot bearing
- Distinguish organic from cerametallic friction materials and single-mass from dual-mass flywheels
- Trace the clutch hydraulic actuation path from pedal to release bearing
- Perform clutch inspection: disc thickness measurement, pressure plate surface assessment, bearing noise check, flywheel runout and scoring evaluation, and DMF play test
- Make informed go/no-go decisions on clutch components: resurface versus replace

**Day 26 established the complete power flow from engine to wheel.** Day 27 zooms into the manual gearbox and clutch — the two components that give the driver direct mechanical control over torque delivery. Learners must understand the physics, recognise the parts, and judge their condition.

---

## Connection to Prior Knowledge

Day 26 — Power Flow Overview introduced:
- The drivetrain chain: engine, clutch, gearbox, driveshaft, differential, axle shafts, wheels
- The concept that the engine produces power at high RPM but wheels need high torque at low speed
- The role of the gearbox as a torque multiplier and speed reducer
- The clutch as the disconnect device between engine and gearbox

**Bridge:** "Yesterday you traced the power from crankshaft to tyre contact patch. Today we open the gearbox and the clutch bell housing. By the end of this session you'll know what every gear, shaft, fork, disc, and spring does — and you'll be able to judge whether it's fit for service or ready for the bin."

---

## INSTRUCTOR-LED STORY ARC

### **SETUP: Why Gears and Clutches Matter** (Slides 1-3, ~10 minutes)

**Narrative Voice:** Direct, mechanical, grounded. Connect the abstract concept of gear ratios to the physical sensation every driver knows.

---

#### Slide 1: Title & Session Anchor
**Visual:** Split image — left side shows an open manual gearbox with shafts and gears visible; right side shows a clutch assembly (disc, pressure plate, flywheel) laid out on a clean workbench

**Instructor Narration:**
> "Yesterday we followed the power from the crankshaft all the way to the tyre. Today we stop at two specific points in that chain and take them apart. The gearbox — the device that lets a 6000 RPM engine move a 2-tonne car from standstill. And the clutch — the mechanism that connects and disconnects the engine from the gearbox so you can change gears without destroying anything. These are mechanical masterpieces, and by this afternoon you'll know every component inside them."

**PPT Content:**
```
TUV SUD AUTOMOTIVE SERVICE TECHNICIAN
Week 6: Power Delivery — Transmission & Charging
Day 27: Manual Transmission & Clutch

The gearbox gives you the right ratio.
The clutch gives you the on/off switch.
```

---

#### Slide 2: Today's Plan
**Visual:** Horizontal timeline — four blocks: Gear Theory & Gearbox Construction, Clutch Components & Hydraulics, Practical Stations, Wrap-Up

**Instructor Narration:**
> "Here's how today works. First block — gear theory. You'll learn why gears multiply torque, how synchronizers allow smooth shifts, and what every shaft and fork does inside the box. Second block — the clutch. We'll cover friction discs, pressure plates, flywheels, and the hydraulic system that operates it all. Then we go hands-on for ninety minutes — cutaway gearbox inspection, clutch component examination, wear measurement, and gear ratio calculation. Final fifteen minutes to consolidate. Let's start with the physics."

**PPT Content:**
```
TODAY'S PLAN (180 minutes)

BLOCK 1 (30 min): Gear Theory & Gearbox Construction
— Ratios, synchronizers, shafts, forks, selector mechanism

BLOCK 2 (20 min): Clutch Components & Hydraulic Actuation
— Disc, pressure plate, flywheel, release bearing, hydraulics

BLOCK 3 (90 min): Practical Stations
— Cutaway gearbox, clutch inspection, measurements, ratio calculations

BLOCK 4 (15 min): Wrap-Up & Go/No-Go Decisions

+ Day 28 preview
```

---

#### Slide 3: The Problem a Gearbox Solves
**Visual:** Graph showing engine torque curve (peaks at ~3500 RPM) overlaid with a graph showing the torque needed at the wheels for different driving conditions — starting from rest (very high torque), cruising at highway speed (low torque). The gap between them is labeled "The Gearbox Fills This Gap."

**Instructor Narration:**
> "Here's the fundamental problem. Your engine produces peak torque at about 3500 RPM. But when you're trying to pull away from a traffic light, the wheels are barely turning — zero RPM. You need massive torque at the wheels to overcome inertia, but the engine can't produce maximum torque at low RPM. This is the gap the gearbox fills. First gear multiplies the engine torque by a factor of about 3.5 to 4. Fifth gear barely multiplies at all — it's close to a 1:1 ratio — but by then the car is already rolling and doesn't need the multiplication. The gearbox is a torque trading machine: it trades speed for force, or force for speed, depending on what you need."

**PPT Content:**
```
THE PROBLEM A GEARBOX SOLVES

Engine: Peak torque at ~3500 RPM, idle at ~800 RPM
Wheels at standstill: 0 RPM, need MAXIMUM torque

The gap:
• Starting from rest = need high torque, low speed at wheels
• Highway cruising = need low torque, high speed at wheels
• Engine output is relatively constant

The gearbox TRADES speed for torque (and vice versa)
— Low gear: high torque multiplication, low wheel speed
— High gear: low torque multiplication, high wheel speed

This is the gear ratio at work.
```

---

### **DEVELOPMENT PART 1: Gear Theory & Gearbox Construction** (Slides 4-14, ~30 minutes)

**Narrative Voice:** Analytical but physical. Every formula must connect to something the learner can see and feel.

---

#### Slide 4: Gear Pairs — Driving and Driven
**Visual:** Simple two-gear mesh diagram. Small gear (20 teeth) labeled "DRIVING GEAR (on input shaft)" meshing with large gear (40 teeth) labeled "DRIVEN GEAR (on layshaft)." Arrows showing rotation direction — driving clockwise, driven counter-clockwise.

**Instructor Narration:**
> "Everything in a gearbox starts with a gear pair. Two gears meshing together. One is the driving gear — connected to the power source. The other is the driven gear — it receives the power. When these two gears mesh, three things happen. First, the direction of rotation reverses — if the driving gear turns clockwise, the driven gear turns counter-clockwise. Second, if the gears are different sizes, the speed changes. Third, and this is the critical one — if the speed goes down, the torque goes up. Let me show you why."

**PPT Content:**
```
GEAR PAIRS — THE FOUNDATION

DRIVING GEAR: Connected to the power source (input)
DRIVEN GEAR: Receives the power (output)

When two gears mesh:
1. Rotation direction REVERSES
2. Speed CHANGES (if gears are different sizes)
3. Torque CHANGES (inversely to speed change)

Small gear drives large gear = speed DOWN, torque UP
Large gear drives small gear = speed UP, torque DOWN

The teeth of both gears move at the SAME linear speed
— this is why the size difference creates the ratio
```

---

#### Slide 5: Gear Ratio — The Formula
**Visual:** Same two-gear diagram now with calculation overlay. Driving gear = 20 teeth, Driven gear = 40 teeth. Formula shown step-by-step: Ratio = Driven / Driving = 40/20 = 2.0:1

**Instructor Narration:**
> "The gear ratio is the single most important number in transmission engineering. The formula is simple: divide the number of teeth on the driven gear by the number of teeth on the driving gear. In our example, 40 teeth driven divided by 20 teeth driving equals a ratio of 2:1. What does that mean in practice? The output shaft turns at half the speed of the input shaft — but it produces twice the torque. Speed halved, torque doubled. That's the trade. It's not magic — it's the same principle as a lever. A long lever arm gives you more force but less distance. A gear ratio is a rotary lever."

**PPT Content:**
```
GEAR RATIO — THE FORMULA

        Teeth on DRIVEN gear
Ratio = ─────────────────────
        Teeth on DRIVING gear

Example:
Driven = 40 teeth, Driving = 20 teeth
Ratio = 40 / 20 = 2.0 : 1

What 2.0:1 means:
• Output speed = Input speed / 2.0
• Output torque = Input torque × 2.0

THE GOLDEN RULE:
Speed reduction = Torque multiplication
(by the SAME factor)

Engine at 3000 RPM, 200 Nm through a 2:1 ratio:
→ Output = 1500 RPM at 400 Nm
```

---

#### Slide 6: Speed Reduction = Torque Multiplication
**Visual:** Three examples side by side — 1st gear ratio 3.6:1, 3rd gear ratio 1.3:1, 5th gear ratio 0.8:1. Each with engine input of 3000 RPM / 200 Nm, showing the calculated output speed and torque for each.

**Instructor Narration:**
> "Let's put real numbers on this. Assume the engine is producing 200 Newton-metres at 3000 RPM. In first gear with a 3.6:1 ratio, the output is 833 RPM but 720 Newton-metres of torque. That's nearly four times the engine torque — perfect for pulling away from rest. In third gear at 1.3:1, you get 2308 RPM and 260 Newton-metres — a moderate balance. In fifth gear at 0.8:1, notice the ratio is less than one. That means the output is actually spinning faster than the input — 3750 RPM — but torque drops to 160 Newton-metres. This is called overdrive. It's efficient for highway cruising because the engine can run at lower RPM for a given road speed. Every gear in the box is a different trade-off between speed and torque."

**PPT Content:**
```
REAL NUMBERS: SPEED vs TORQUE TRADE-OFF

Engine input: 3000 RPM, 200 Nm

1st GEAR (3.6:1):
Output = 833 RPM, 720 Nm      ← Maximum pulling force

3rd GEAR (1.3:1):
Output = 2308 RPM, 260 Nm     ← Balance of speed and torque

5th GEAR (0.8:1) — OVERDRIVE:
Output = 3750 RPM, 160 Nm     ← Efficient cruising, low torque

OVERDRIVE: Ratio < 1.0
→ Output spins FASTER than input
→ Engine RPM drops for same road speed
→ Better fuel economy at highway speed
```

---

#### Slide 7: Inside the Gearbox — The Three Shafts
**Visual:** Cutaway side-view diagram of a 5-speed manual gearbox showing input shaft (from clutch), layshaft/countershaft (below, with fixed gears), and output shaft (to driveshaft) with free-spinning gears and synchronizer assemblies

**Instructor Narration:**
> "Now let's open the box. A typical manual gearbox has three main shafts. The input shaft comes from the clutch — it spins at engine speed. The layshaft, also called the countershaft, sits below. It carries fixed gears that mesh permanently with gears on the input and output shafts. The output shaft goes to the driveshaft and eventually the wheels. On the output shaft, the gears spin freely on bearings — they're always turning, but they're not locked to the shaft. To select a gear, you have to lock one of those free-spinning gears to the output shaft. That's the job of the synchronizer."

**PPT Content:**
```
INSIDE THE GEARBOX — THREE SHAFTS

INPUT SHAFT (from clutch)
• Spins at engine speed when clutch is engaged
• Carries a gear that drives the layshaft permanently

LAYSHAFT / COUNTERSHAFT
• Sits below, parallel to input and output shafts
• All gears FIXED to the shaft — they rotate together
• Always spinning when input shaft turns

OUTPUT SHAFT (to driveshaft)
• Carries gears that FREE-SPIN on bearings
• These gears mesh permanently with layshaft gears
• Gears spin but are NOT locked to the shaft
• To select a gear = lock one gear to the shaft

The locking device = SYNCHRONIZER
```

---

#### Slide 8: Power Path Through the Gearbox
**Visual:** Animated-style diagram (still image with numbered arrows) showing the power path: Input shaft gear (1) drives layshaft (2), layshaft gear for 3rd (3) meshes with output shaft 3rd gear (4), synchronizer locks 3rd gear to output shaft (5), output shaft delivers to driveshaft (6)

**Instructor Narration:**
> "Follow the power. Step one — the input shaft gear drives the layshaft. This happens in every gear, every time. Step two — the layshaft has a gear for every speed — first through fifth, plus reverse. Each of these layshaft gears meshes with a corresponding gear on the output shaft. Step three — all those output shaft gears are spinning freely. Step four — the synchronizer slides over and locks the selected gear to the output shaft. Now the power flows: input shaft, down to layshaft, across to the selected output gear, into the output shaft, and out to the driveshaft. Change the selected gear, change the ratio."

**PPT Content:**
```
POWER PATH THROUGH THE GEARBOX (3rd gear selected)

1. Engine → Clutch → INPUT SHAFT rotates
2. Input shaft gear drives LAYSHAFT (permanent mesh)
3. Layshaft 3rd gear meshes with output shaft 3rd gear
4. Output shaft 3rd gear is FREE-SPINNING
5. SYNCHRONIZER locks 3rd gear to output shaft
6. OUTPUT SHAFT delivers torque to driveshaft

Key insight: ALL gears are ALWAYS meshing
— the synchronizer chooses which one delivers power
— this is called "constant-mesh" gearbox design
— only the synchronizer engagement changes
```

---

#### Slide 9: The Synchronizer — How Smooth Shifts Happen
**Visual:** Exploded cross-section of a synchronizer assembly — synchronizer hub (splined to shaft), hub sleeve (slides over hub), synchronizer ring (brass cone), blocking teeth/dogs, detent spring and ball

**Instructor Narration:**
> "The synchronizer is the most clever component in the gearbox. Its job is to match the speed of the free-spinning gear to the speed of the output shaft before locking them together. Without it, you'd hear horrible grinding every time you changed gear — and you'd destroy the dogs in weeks. Here's how it works, step by step."

**PPT Content:**
```
THE SYNCHRONIZER ASSEMBLY

Components:
• SYNCHRONIZER HUB — splined to output shaft, always rotates with it
• HUB SLEEVE — slides axially over the hub (moved by shift fork)
• SYNCHRONIZER RING (brass cone) — sits between sleeve and gear
• BLOCKING TEETH / DOG TEETH — on ring and gear, must align to engage
• DETENT SPRING & BALL — holds sleeve in position (neutral or engaged)

Purpose:
Match the speed of the FREE-SPINNING gear to the OUTPUT SHAFT
before locking them together

Without synchronizers: GRINDING (crash gearbox — old trucks)
With synchronizers: SMOOTH, SILENT shifts
```

---

#### Slide 10: Synchronizer Operation — Step by Step
**Visual:** Four-panel sequential diagram: (1) Neutral — sleeve centered, (2) Sleeve pushes synchro ring against gear cone — friction begins, (3) Speeds equalise — blocking teeth align, (4) Sleeve slides over dog teeth — gear locked to shaft. Each panel has a brief label.

**Instructor Narration:**
> "Four stages. Stage one — neutral. The hub sleeve is centered. No gear is locked. Stage two — you move the shift lever. The shift fork pushes the hub sleeve toward the gear you want. The sleeve presses the brass synchronizer ring against the cone surface of the gear. This creates friction — like a miniature cone clutch. The friction begins to speed up or slow down the gear to match the output shaft speed. Stage three — the speeds equalize. The blocking teeth on the synchronizer ring were preventing the sleeve from sliding further — they were out of alignment because the speeds were different. Once the speeds match, the blocking teeth align and the ring lets the sleeve pass. Stage four — the sleeve slides over the dog teeth on the gear. Now the gear is mechanically locked to the output shaft through the hub. Power flows. The detent spring clicks the sleeve into position so it doesn't pop out under load."

**PPT Content:**
```
SYNCHRONIZER OPERATION — 4 STAGES

STAGE 1: NEUTRAL
— Hub sleeve centered, no gear locked
— All gears free-spinning on output shaft

STAGE 2: FRICTION PHASE (speed matching)
— Shift fork pushes hub sleeve toward selected gear
— Sleeve presses BRASS SYNCHRO RING against gear cone
— Cone friction = speed matching begins
— Blocking teeth PREVENT engagement until speeds match

STAGE 3: SYNCHRONIZATION COMPLETE
— Gear speed now matches output shaft speed
— Blocking teeth ALIGN — ring allows sleeve to pass

STAGE 4: ENGAGEMENT
— Sleeve slides over DOG TEETH on gear
— Gear LOCKED to output shaft via hub
— DETENT SPRING holds sleeve in position
— Power flows through selected gear

This entire process takes < 0.5 seconds
```

---

#### Slide 11: Why Brass? — Synchro Ring Material
**Visual:** Close-up photo of a brass synchronizer ring showing the cone friction surface with machined grooves, alongside a worn synchro ring for comparison

**Instructor Narration:**
> "Why brass? Three reasons. First, brass has excellent friction properties against steel — the gear cone is hardened steel, and brass grips it well. Second, brass is softer than steel, so it wears instead of the gear. A synchro ring is a consumable — it's cheaper and easier to replace than a gear. Third, the grooves machined into the brass cone surface serve the same purpose as tread on a tyre — they channel lubricant oil away from the contact surface so metal-to-metal friction can develop quickly. When a synchro ring wears thin, the grooves disappear, oil can't be cleared, and you get that crunching sound when shifting. That's your sign the synchro is done."

**PPT Content:**
```
SYNCHRONIZER RING — WHY BRASS?

Material: Typically brass (Cu-Zn alloy) or brass with carbon lining

Why brass works:
1. HIGH FRICTION coefficient against hardened steel gear cone
2. SOFTER than steel — synchro ring wears, gear does not
   → Synchro ring is a CONSUMABLE replacement part
3. Machined GROOVES on cone surface
   → Channel transmission oil away from contact zone
   → Allows metal-to-metal friction to develop rapidly

WEAR INDICATORS:
• New synchro ring: grooves deep, cone surface textured
• Worn synchro ring: grooves shallow/gone, surface polished
• Symptom: CRUNCHING or GRINDING when shifting into that gear
  (especially when cold — oil thicker, harder to clear)

Common failure: 2nd gear synchro (most used during deceleration)
```

---

#### Slide 12: Shift Mechanism — Forks, Rails, and Selector
**Visual:** Top-down view of a gearbox showing three shift forks on their rails, connected to the selector mechanism. An interlock plate/pin is visible between the rails. The shift lever connection at the top is labeled.

**Instructor Narration:**
> "You move the shift lever in the cabin. How does that movement reach the synchronizers inside the gearbox? Through the selector mechanism. The shift lever connects — either directly or through cables — to a selector shaft on the gearbox. This shaft moves shift forks that sit in grooves on the hub sleeves. Each fork controls one pair of gears. Typically, fork one handles first and second, fork two handles third and fourth, and fork three handles fifth. There's also an interlock mechanism — a set of pins or a plate — that prevents you from selecting two gears at the same time. If two gears engaged simultaneously, the gearbox would lock solid and likely destroy itself."

**PPT Content:**
```
SHIFT MECHANISM — HOW YOU SELECT A GEAR

SHIFT LEVER (in cabin)
  → via linkage rods or cables →
SELECTOR SHAFT (on gearbox housing)
  → moves →
SHIFT FORKS (inside gearbox)
  → slide →
HUB SLEEVES (on synchronizers)

Typical fork layout (5-speed):
• Fork 1: 1st and 2nd gear (one fork, two directions)
• Fork 2: 3rd and 4th gear
• Fork 3: 5th gear (and sometimes reverse)

INTERLOCK MECHANISM:
• Pins or plate between shift rails
• PREVENTS selecting two gears simultaneously
• Two gears at once = mechanical destruction

DETENT SPRINGS:
• Hold each fork in neutral or engaged position
• Provide the "click" feel when gear is selected
```

---

#### Slide 13: Reverse Gear — The Idler
**Visual:** Diagram showing the reverse idler gear sliding between the layshaft reverse gear and the output shaft reverse gear. Arrow showing that the idler adds an extra mesh, reversing rotation direction.

**Instructor Narration:**
> "Every forward gear follows the same path: input to layshaft, layshaft to output. That gives you two mesh points and the output shaft rotates in the same direction as the input. But for reverse, you need the output to spin the opposite way. The solution is an idler gear — a third gear that sits between the layshaft and output shaft. This adds one more mesh point, which reverses the direction again. In most gearboxes, the reverse idler slides into mesh — it doesn't have a synchronizer. That's why you should always come to a complete stop before selecting reverse. If you try to jam it in while rolling forward, you'll hear the dogs grinding. Some modern gearboxes do add a reverse synchro, but many still don't."

**PPT Content:**
```
REVERSE GEAR — THE IDLER

Forward gears: Input → Layshaft → Output
= TWO mesh points = output rotates SAME direction as input

Reverse: Input → Layshaft → IDLER → Output
= THREE mesh points = output rotates OPPOSITE direction

The REVERSE IDLER GEAR:
• Slides into mesh when reverse is selected
• Typically NO SYNCHRONIZER — straight-cut dog engagement
• This is why you MUST STOP before selecting reverse
• Grinding noise = dog teeth clashing at different speeds

Some modern gearboxes (VW, BMW) add a reverse synchro
— allows smoother reverse selection
— but the rule remains: STOP before engaging reverse

Reverse gear teeth are often STRAIGHT-CUT (not helical)
— produces the characteristic WHINE in reverse
— helical gears would create axial thrust in wrong direction
```

---

#### Slide 14: Gearbox Bearings, Seals, and Lubrication
**Visual:** Cross-section of a gearbox highlighting: input shaft bearing (in bell housing), output shaft rear bearing, layshaft bearings, input shaft seal, output shaft seal, oil fill/drain plugs, breather vent

**Instructor Narration:**
> "The gearbox is a sealed, oil-filled housing. The oil — typically 75W-90 GL-4 or GL-5 gear oil — serves two purposes: lubrication of the gears and bearings, and cooling of the synchronizers. Bearings support every shaft — tapered roller bearings or ball bearings depending on the design. Seals prevent oil from leaking out where the shafts exit the housing — the input shaft seal where the clutch release bearing sits, and the output shaft seal where the driveshaft connects. There's also a breather vent on top that allows pressure to equalise as the oil heats and cools. If that breather blocks, pressure builds and oil gets pushed past the seals. A leaking gearbox is often just a blocked breather."

**PPT Content:**
```
GEARBOX BEARINGS, SEALS & LUBRICATION

BEARINGS:
• Input shaft bearing — front of gearbox (in bell housing)
• Output shaft bearing — rear of gearbox
• Layshaft bearings — both ends
• Type: Tapered roller or deep-groove ball bearings
• Failure symptom: whine that changes with speed, not engine RPM

SEALS:
• Input shaft seal (at clutch bell housing interface)
• Output shaft seal (at driveshaft flange)
• Selector shaft seal (where shift linkage enters housing)
• Failure symptom: oil drips, low oil level

LUBRICATION:
• Gear oil: Typically 75W-90 GL-4 (manual gearbox)
• Fill via side plug, drain via bottom plug
• Oil level = bottom of fill plug hole
• Change interval: 60,000-100,000 km (varies by manufacturer)

BREATHER VENT:
• Top of housing — allows pressure equalisation
• Blocked breather = pressure build-up = oil forced past seals
```

---

### **DEVELOPMENT PART 2: Clutch Components & Hydraulic Actuation** (Slides 15-20, ~20 minutes)

**Narrative Voice:** Component-by-component. Build the assembly in the learner's mind, piece by piece.

---

#### Slide 15: The Clutch Assembly — Complete Overview
**Visual:** Exploded view of a complete clutch assembly in order from flywheel to gearbox: flywheel (bolted to crankshaft), clutch friction disc (between flywheel and pressure plate), pressure plate (bolted to flywheel, clamps disc), release/throw-out bearing (on gearbox input shaft sleeve), pilot bearing (in center of flywheel)

**Instructor Narration:**
> "The clutch sits between the engine flywheel and the gearbox input shaft. Its job is binary — connect or disconnect. When engaged, it transfers every Newton-metre of engine torque to the gearbox. When disengaged, the engine spins freely and no power reaches the wheels. Let me walk you through every component from the flywheel face inward."

**PPT Content:**
```
THE CLUTCH ASSEMBLY — EXPLODED VIEW

From engine side to gearbox side:

1. FLYWHEEL — bolted to crankshaft, provides inertia and friction surface
2. CLUTCH FRICTION DISC — sandwiched between flywheel and pressure plate
3. PRESSURE PLATE — bolted to flywheel, clamps the friction disc
4. RELEASE (THROW-OUT) BEARING — pushes on pressure plate fingers
5. PILOT BEARING — in centre of flywheel, supports input shaft tip

All together:
Crankshaft → Flywheel → [Friction Disc clamped] → Pressure Plate
                              ↓
                        Gearbox Input Shaft
```

---

#### Slide 16: The Friction Disc — Where Torque Transfers
**Visual:** Front and back of a clutch friction disc. Labels pointing to: friction facing material (both sides), splined hub (center), torsional damper springs (visible through windows in the disc), Marcel spring (wavy cushion spring between facings)

**Instructor Narration:**
> "The friction disc is the only component that physically touches both the flywheel and the pressure plate. It's the torque bridge. The center hub is splined to the gearbox input shaft — so when the disc is clamped between the flywheel and pressure plate, it forces the input shaft to rotate with the engine. The friction facings come in two types. Organic — made from a composite of fibers, rubber, and resin — is smooth, progressive, and comfortable for daily driving. Cerametallic — embedded with ceramic and metallic particles — handles much higher temperatures and torques but grabs harder and is less comfortable. Performance and racing cars use cerametallic. The damper springs you can see through the windows in the disc absorb torsional vibration from the engine. Without them, every combustion pulse would transmit a shock through the drivetrain. The Marcel spring — a wavy cushion between the friction facings — allows progressive engagement rather than a sudden grab."

**PPT Content:**
```
THE FRICTION DISC

FRICTION FACINGS (both sides):
• ORGANIC: Fiber + rubber + resin composite
  — Smooth engagement, long life, comfortable
  — Standard for road cars
• CERAMETALLIC: Ceramic + metallic particles
  — Higher heat capacity, higher friction coefficient
  — Harsher engagement, shorter life
  — Performance / racing / heavy-duty applications

SPLINED HUB (centre):
• Matches splines on gearbox input shaft
• Allows axial float but locks rotationally

TORSIONAL DAMPER SPRINGS:
• Absorb engine combustion vibration
• Prevent driveline shock on engagement
• Visible through windows in the disc body

MARCEL SPRING (cushion spring):
• Wavy spring between friction facings
• Allows PROGRESSIVE engagement, not sudden grab
• Reduces judder on take-off
```

---

#### Slide 17: Pressure Plate and Diaphragm Spring
**Visual:** Cross-section of a diaphragm spring pressure plate — showing the cover (bolted to flywheel), the pressure ring (pushes on friction disc), the diaphragm spring (conical Belleville washer with fingers), and the pivot ring

**Instructor Narration:**
> "The pressure plate provides the clamping force that squeezes the friction disc against the flywheel. Modern cars exclusively use the diaphragm spring type. The diaphragm spring is a large conical disc — essentially a Belleville washer — with fingers cut into the center. When the clutch is engaged, the spring's natural shape presses the pressure ring firmly against the friction disc. When you press the clutch pedal, the release bearing pushes on the tips of the diaphragm fingers, pivoting the spring and lifting the pressure ring away from the disc. The beauty of the diaphragm spring is that its clamping force remains relatively constant across its travel — unlike an older coil spring design where pedal effort increased dramatically as the disc wore. That's why modern clutch pedals feel lighter than old ones."

**PPT Content:**
```
PRESSURE PLATE — DIAPHRAGM SPRING TYPE

Components:
• COVER — bolted to flywheel (rotates with engine)
• PRESSURE RING — flat machined surface, contacts friction disc
• DIAPHRAGM SPRING — conical Belleville washer with fingers
• PIVOT RING — fulcrum point for spring deflection

ENGAGED (pedal up):
— Diaphragm spring pushes pressure ring against friction disc
— Disc clamped between pressure ring and flywheel face
— Torque transfers: engine → flywheel → disc → gearbox

DISENGAGED (pedal down):
— Release bearing pushes on diaphragm spring FINGERS
— Spring pivots on ring, LIFTS pressure ring away from disc
— Disc released — engine and gearbox disconnected

ADVANTAGE of diaphragm over coil springs:
— More consistent clamping force across disc wear range
— Lighter pedal effort
— Simpler construction (one spring vs. multiple coils)
— Self-adjusting to some extent as disc wears
```

---

#### Slide 18: Flywheel — Single Mass vs Dual Mass (DMF)
**Visual:** Side-by-side comparison: left shows a single-mass flywheel (solid disc with ring gear), right shows a cutaway of a dual-mass flywheel showing primary mass, secondary mass, arc springs between them, and the ring gear on the primary mass

**Instructor Narration:**
> "The flywheel serves three functions. First, it stores rotational energy — the engine fires in pulses, and the flywheel's mass smooths those pulses into continuous rotation. Second, it provides one friction surface for the clutch disc. Third, it carries the ring gear that the starter motor engages. Single-mass flywheels are simple — one solid piece of cast iron or steel. They're durable and cheap, but they transmit engine vibration into the drivetrain. Dual-mass flywheels — DMFs — split the flywheel into two halves connected by arc springs. The primary mass bolts to the crankshaft and carries the ring gear. The secondary mass provides the clutch friction surface. The springs between them absorb torsional vibration far better than the damper springs in the clutch disc alone. DMFs are standard on modern diesel cars and increasingly on petrol cars. The catch? DMFs wear out. The arc springs fatigue, the damping grease dries out, and you get a distinctive rattling noise at idle. DMF replacement is expensive — and unlike a single-mass flywheel, you cannot resurface a DMF. It's always replace."

**PPT Content:**
```
FLYWHEEL — SINGLE MASS vs DUAL MASS (DMF)

SINGLE MASS FLYWHEEL:
• One solid disc — cast iron or steel
• Ring gear pressed onto outer edge
• Simple, durable, can be resurfaced
• Transmits more engine vibration
• Used on: older vehicles, economy cars, racing

DUAL MASS FLYWHEEL (DMF):
• PRIMARY MASS: bolts to crankshaft, carries ring gear
• SECONDARY MASS: clutch friction surface
• ARC SPRINGS between masses absorb torsional vibration
• Damping grease fills the spring cavity
• Superior NVH (Noise, Vibration, Harshness) performance

DMF FAILURE SYMPTOMS:
• Rattling/knocking at idle (springs worn)
• Excessive free play when rocked by hand
• Vibration at low RPM in gear
• CANNOT BE RESURFACED — always REPLACE
• Check DMF angular play: typically max 2-3 degrees
• Manufacturer-specific go/no-go specs
```

---

#### Slide 19: Release Bearing and Pilot Bearing
**Visual:** Cutaway showing the release (throw-out) bearing on the gearbox input shaft sleeve, with the fork that operates it. Inset photo of a pilot bearing (small needle bearing) seated in the center of the flywheel.

**Instructor Narration:**
> "Two more bearings to know. The release bearing — also called the throw-out bearing — sits on a sleeve around the gearbox input shaft. When you press the clutch pedal, the clutch fork pushes this bearing forward against the diaphragm spring fingers. It's a constant-contact design on most modern cars — it always lightly touches the spring fingers, even when the clutch is engaged. The bearing itself is sealed and pre-packed with grease. It spins at engine speed whenever the clutch is disengaged. Failure symptom: a whirring or squealing noise that appears when you press the clutch pedal and disappears when you release it. Always replace the release bearing whenever you replace the clutch — it's a false economy to leave the old one in. The pilot bearing is a small needle bearing or bushing pressed into the center of the flywheel. It supports the tip of the gearbox input shaft and keeps it centered. Failure is rare but when it happens, you get a squeal or chirp in neutral that disappears when you press the clutch."

**PPT Content:**
```
RELEASE (THROW-OUT) BEARING

• Sits on sleeve around gearbox input shaft
• Operated by CLUTCH FORK (mechanical) or slave cylinder (hydraulic)
• Constant-contact type (modern) — always touches diaphragm fingers
• Sealed, pre-greased, not serviceable
• Spins at ENGINE SPEED when clutch pedal is pressed

Failure symptom:
→ Whirring/squealing WHEN PEDAL IS PRESSED
→ Noise DISAPPEARS when pedal released
→ ALWAYS replace with clutch disc and pressure plate

PILOT BEARING

• Small needle bearing or bronze bushing
• Pressed into centre of flywheel (or crankshaft end)
• Supports TIP of gearbox input shaft
• Keeps input shaft centred in flywheel

Failure symptom:
→ Squeal/chirp in NEUTRAL with clutch ENGAGED
→ Noise disappears when clutch PEDAL PRESSED
→ Replace during every clutch job as preventive measure
```

---

#### Slide 20: Clutch Hydraulic Actuation
**Visual:** Complete hydraulic clutch system diagram: clutch pedal → pushrod → master cylinder (at firewall) → hydraulic line (hard line + flexible hose) → slave cylinder (on bell housing) → pushrod/fork or concentric slave → release bearing → diaphragm spring fingers. Fluid reservoir shown above master cylinder.

**Instructor Narration:**
> "How does your foot on the pedal translate into a bearing pushing on the diaphragm spring? Through hydraulics — the same principle as your brake system. When you press the clutch pedal, a pushrod activates a master cylinder mounted on the firewall. The master cylinder pressurises clutch fluid — which is actually brake fluid, typically DOT 4 — and sends it through a hard line and flexible hose to a slave cylinder mounted on the bell housing. The slave cylinder pushes either a fork that operates the release bearing, or in many modern cars, a concentric slave cylinder that sits around the input shaft and pushes the bearing directly. The system is self-adjusting — as the clutch disc wears and the diaphragm spring position changes, the hydraulic system automatically compensates. No cable adjustment needed. Bleed the system exactly as you'd bleed brakes — air in the line means a spongy pedal or incomplete disengagement."

**PPT Content:**
```
CLUTCH HYDRAULIC ACTUATION

PEDAL → MASTER CYLINDER → FLUID LINE → SLAVE CYLINDER → RELEASE BEARING

Components:
• CLUTCH PEDAL: Mechanical advantage (lever ratio) ~6:1
• MASTER CYLINDER: Mounted on firewall, converts pedal force to pressure
• FLUID RESERVOIR: Typically shared with or near brake reservoir
• HYDRAULIC LINE: Hard pipe + flexible hose to gearbox
• SLAVE CYLINDER: Mounted on bell housing
  — External type: pushes fork → fork pushes release bearing
  — Concentric (CSC): surrounds input shaft, pushes bearing directly

FLUID: DOT 4 brake fluid (hygroscopic — absorbs moisture)
— Change every 2 years (same as brake fluid)
— Moisture → lower boiling point → risk of vapour lock

BLEEDING: Same procedure as brake system
— Fill reservoir, open bleed nipple on slave, pump pedal
— Spongy pedal = air in system

SELF-ADJUSTING: No cable stretch compensation needed
— Hydraulic system auto-compensates for disc wear
```

---

### **PRACTICAL: Hands-On Stations** (Slides 21-24, ~90 minutes)

**Narrative Voice:** Workshop instructor mode. Clear directions, safety awareness, specific measurement criteria.

---

#### Slide 21: Station 1 — Cutaway Gearbox Examination (25 min)
**Visual:** Photo of a cutaway or disassembled manual gearbox on a workbench with components labeled with number tags

**Instructor Narration:**
> "Station one. You have a cutaway gearbox in front of you — or a fully disassembled one with all the parts laid out. Your task is identification. Find and label: the input shaft, layshaft, output shaft, each gear pair for gears one through five, the reverse idler, at least two synchronizer assemblies, the shift forks and their rails, and the selector mechanism. Use the tag labels provided. Once you've identified everything, trace the power path for third gear from input to output — follow the actual gear teeth mesh. I want you to physically point at each component in the chain."

**PPT Content:**
```
STATION 1: CUTAWAY GEARBOX EXAMINATION (25 min)

TASK: Identify and label all major gearbox components

Find and tag:
□ Input shaft
□ Layshaft / countershaft
□ Output shaft
□ Gear pairs for 1st, 2nd, 3rd, 4th, 5th
□ Reverse idler gear
□ Synchronizer assemblies (at least 2)
□ Synchronizer rings (brass cones)
□ Hub sleeves
□ Shift forks and rails
□ Selector mechanism / interlock
□ Input shaft bearing
□ Output shaft bearing
□ Seals (input and output)

THEN: Trace the power path for 3rd gear
— Point at each component from input to output
— Explain each mesh to your partner
```

---

#### Slide 22: Station 2 — Clutch Component Examination (20 min)
**Visual:** Photo of clutch components laid out on a workbench in order: flywheel, friction disc (face up showing both friction surfaces), pressure plate (showing diaphragm spring), release bearing, pilot bearing. Both a new and a worn disc shown for comparison.

**Instructor Narration:**
> "Station two. Laid out in front of you are all the clutch components. Examine each one. For the friction disc: look at the friction facing material — is it organic or cerametallic? Find the damper springs. Find the splined hub and verify it would slide onto the input shaft. Compare the new disc to the worn disc — look at the rivet depth and surface condition. For the pressure plate: identify the diaphragm spring fingers and the pivot ring. Look at the pressure ring surface for scoring or hot spots. For the flywheel: look at the friction surface condition and feel for scoring. If it's a DMF, try to rotate the secondary mass against the primary — feel for excessive play and listen for rattling. For the release bearing: spin it by hand — it should be smooth and silent. Any roughness or noise means replacement."

**PPT Content:**
```
STATION 2: CLUTCH COMPONENT EXAMINATION (20 min)

FRICTION DISC:
□ Identify facing material: organic or cerametallic?
□ Find torsional damper springs
□ Check splined hub — does it slide freely on input shaft?
□ Compare NEW vs WORN disc — note rivet depth difference

PRESSURE PLATE:
□ Identify diaphragm spring fingers
□ Locate pivot ring
□ Inspect pressure ring surface — scoring? Blue heat marks?

FLYWHEEL:
□ Inspect friction surface — scoring? Hot spots?
□ If DMF: rock secondary mass — check angular play
□ Listen for DMF spring rattle

RELEASE BEARING:
□ Spin by hand — smooth and silent = OK
□ Any roughness, grinding, or noise = REPLACE

PILOT BEARING:
□ Check for play or roughness
```

---

#### Slide 23: Station 3 — Clutch Inspection Measurements (25 min)
**Visual:** Four measurement scenarios with tools shown: (1) Vernier calliper measuring disc thickness, (2) Straight edge and feeler gauge on pressure plate surface, (3) Dial indicator on flywheel measuring runout, (4) Hand test on DMF showing angular play measurement

**Instructor Narration:**
> "Station three — measurements. This is where you make go/no-go decisions. First, clutch disc thickness. Use the vernier calliper to measure the overall thickness of the friction disc at four points, 90 degrees apart. Compare to the manufacturer's minimum specification — typically around 7 to 8 millimetres minimum when new discs are about 10 millimetres. Also measure rivet depth — the distance from the friction surface to the rivet heads. Minimum is typically 0.3 millimetres. Less than that, the rivets will score the flywheel and pressure plate. Second, pressure plate surface. Use a straight edge across the pressure ring and check for warping with a feeler gauge. Maximum deviation is typically 0.3 millimetres. Look for hot spots — blue discoloration indicates overheating and spring fatigue. Third, flywheel runout. Mount the dial indicator and rotate the flywheel. Maximum runout is typically 0.1 to 0.15 millimetres. Excessive runout causes clutch judder on engagement. Fourth, DMF play. With the gearbox off, hold the primary mass and try to rotate the secondary mass. Note the angular free play. Specifications vary but typically 2 to 3 degrees maximum when cold. Compare to specification."

**PPT Content:**
```
STATION 3: CLUTCH INSPECTION MEASUREMENTS (25 min)

MEASUREMENT 1: DISC THICKNESS
• Tool: Vernier calliper
• Measure at 4 points, 90° apart
• New disc: ~10 mm typical
• Minimum: ~7-8 mm (manufacturer-specific)
• Also measure RIVET DEPTH: min 0.3 mm from surface

MEASUREMENT 2: PRESSURE PLATE SURFACE
• Tool: Straight edge + feeler gauge
• Check for warping: max 0.3 mm deviation
• Visual: blue heat marks = overheated = REPLACE

MEASUREMENT 3: FLYWHEEL RUNOUT
• Tool: Dial indicator on magnetic base
• Rotate flywheel, note total indicator reading (TIR)
• Maximum runout: 0.10-0.15 mm (manufacturer-specific)
• Excessive runout = judder on engagement

MEASUREMENT 4: DMF ANGULAR PLAY
• Hold primary mass, rotate secondary by hand
• Measure angular free play (degrees)
• Typical maximum: 2-3° cold (check manufacturer spec)
• Excessive play + rattle = DMF replacement required
```

---

#### Slide 24: Station 4 — Gear Ratio Calculation (20 min)
**Visual:** Photo of a gear pair with visible teeth, alongside a worksheet showing the calculation template: "Count teeth on driving gear: ___ Count teeth on driven gear: ___ Ratio = Driven / Driving = ___ : 1 → Output speed if input = 3000 RPM: ___ RPM → Output torque if input = 200 Nm: ___ Nm"

**Instructor Narration:**
> "Station four — math meets metal. You have actual gear pairs — either from the cutaway gearbox or separate training gear sets. Count the teeth. Yes, physically count them — mark your starting point with a marker and go around. Once you have the tooth counts for each gear pair, calculate the ratio. Then calculate the actual output speed and torque for a given engine input. I'll give you three gear pairs to calculate. Once you've done the individual pairs, calculate the overall ratio through the gearbox for first gear — remember, the power goes through two mesh points: input to layshaft, and layshaft to output. Multiply the two individual ratios to get the overall ratio. This is how gear ratios in the specifications are actually derived."

**PPT Content:**
```
STATION 4: GEAR RATIO CALCULATION (20 min)

STEP 1: COUNT TEETH ON ACTUAL GEAR PAIRS
— Mark starting tooth with marker pen
— Count carefully all the way around
— Record: Driving gear teeth = ___  Driven gear teeth = ___

STEP 2: CALCULATE RATIO
— Ratio = Driven teeth / Driving teeth = ___ : 1

STEP 3: CALCULATE OUTPUT VALUES
— If input = 3000 RPM:
  Output speed = 3000 / Ratio = ___ RPM
— If input = 200 Nm:
  Output torque = 200 × Ratio = ___ Nm

STEP 4: CALCULATE OVERALL 1st GEAR RATIO
— Two mesh points:
  Mesh 1: Input shaft to layshaft = Ratio A
  Mesh 2: Layshaft to output shaft (1st gear) = Ratio B
  Overall ratio = Ratio A × Ratio B = ___:1

This is how the "3.6:1 first gear" in specifications is calculated
```

---

### **WRAP-UP: Go/No-Go Decisions & Consolidation** (Slides 25-28, ~15 minutes)

**Narrative Voice:** Decision-making. Teach judgement, not just facts.

---

#### Slide 25: Go/No-Go — Resurface or Replace?
**Visual:** Decision flowchart for clutch components. Three columns: Flywheel, Pressure Plate, Friction Disc. Each with decision criteria leading to "Resurface," "Replace," or "OK to reuse."

**Instructor Narration:**
> "Every clutch job requires a decision on each component. Here's your decision framework. The friction disc — if the thickness is above minimum spec and rivet depth is above 0.3 millimetres and there's no glazing, contamination, or cracking, it could theoretically be reused. In practice? Always replace the disc. It's a wear item, it's relatively cheap, and you're already in there with the gearbox out. Not replacing it is a false economy. The pressure plate — inspect the pressure ring surface. Light scoring can be machined. Blue heat marks mean the diaphragm spring has been overheated and lost its temper — replace. Cracked or warped — replace. Finger wear grooves from the release bearing — replace. In practice, replace the pressure plate with the disc. They're usually sold as a kit. The flywheel — single-mass can be resurfaced if scoring is light and within the machining limit, and if runout is correctable. But check the minimum thickness specification after machining. A DMF cannot be resurfaced — ever. If it has excessive play, rattles, or shows any grease leakage from the spring cavity, replace it. The release bearing and pilot bearing — always replace. No exceptions. They're cheap insurance."

**PPT Content:**
```
GO/NO-GO DECISIONS — RESURFACE vs REPLACE

FRICTION DISC:
• Below min thickness → REPLACE
• Rivet depth < 0.3 mm → REPLACE
• Oil contamination → REPLACE (also find the leak source!)
• Glazed, cracked, or burnt → REPLACE
• BEST PRACTICE: ALWAYS REPLACE (wear item)

PRESSURE PLATE:
• Blue heat marks → REPLACE (spring fatigue)
• Deep scoring or cracks → REPLACE
• Finger wear grooves → REPLACE
• Light scoring only → can machine, but usually REPLACE
• BEST PRACTICE: REPLACE as kit with disc

FLYWHEEL (Single Mass):
• Light scoring → RESURFACE (check min thickness after machining)
• Runout within spec after machining → OK
• Hard spots, cracks → REPLACE
• Below minimum thickness → REPLACE

FLYWHEEL (DMF):
• Excessive angular play → REPLACE
• Rattle at idle → REPLACE
• Grease leakage → REPLACE
• CANNOT BE RESURFACED — always REPLACE if faulty

RELEASE BEARING: ALWAYS REPLACE with clutch
PILOT BEARING: ALWAYS REPLACE with clutch
```

---

#### Slide 26: Common Clutch Failure Patterns
**Visual:** Six photos in a grid: (1) Glazed friction disc, (2) Oil-contaminated disc, (3) Broken damper springs, (4) Blue-spotted pressure plate, (5) Scored flywheel with hot spots, (6) Failed DMF with visible grease leak

**Instructor Narration:**
> "Learn to read the parts. A glazed disc — shiny, smooth surface — means the clutch was slipping for a long time. The friction material overheated and hardened. An oil-contaminated disc means there's a leak — rear main seal or gearbox input shaft seal. Fix the leak before installing the new clutch, or you'll be doing the job again in six months. Broken damper springs mean severe torsional abuse — aggressive driving or a misfiring engine. Blue spots on the pressure plate are heat damage — the spring has lost its clamping force in that area. Hot spots on the flywheel indicate uneven contact — often caused by a warped pressure plate. And that DMF with grease visible outside the housing — that's a failed arc spring seal, and the DMF is finished. Every failed part tells a story. Read the story before you replace the parts."

**PPT Content:**
```
COMMON CLUTCH FAILURE PATTERNS — READ THE PARTS

1. GLAZED DISC: Shiny, hard friction surface
   → Cause: Prolonged slipping (riding the clutch)
   → Action: Replace disc, educate driver

2. OIL-CONTAMINATED DISC: Wet, discoloured facing
   → Cause: Rear main seal leak or input shaft seal leak
   → Action: Replace disc AND fix the oil leak source

3. BROKEN DAMPER SPRINGS: Visible through disc windows
   → Cause: Severe torsional shock, engine misfire
   → Action: Replace disc, check engine running condition

4. BLUE PRESSURE PLATE: Heat discoloration on pressure ring
   → Cause: Overheating, clutch slip, towing overload
   → Action: Replace pressure plate (spring fatigued)

5. SCORED/HOT-SPOTTED FLYWHEEL: Grooves and discoloured areas
   → Cause: Worn disc (rivets contacted surface), warped PP
   → Action: Resurface (if within spec) or replace

6. DMF GREASE LEAK: Grease visible outside housing
   → Cause: Arc spring seal failure, internal wear
   → Action: REPLACE DMF — cannot be repaired
```

---

#### Slide 27: What You Learned Today
**Visual:** Checklist with tick marks

**Instructor Narration:**
> "Let's take stock. This morning you understood gear ratios only in theory. Now you've counted actual gear teeth and calculated real ratios. You know how synchronizers match speeds using brass cone friction and blocking teeth. You can identify every component in a manual gearbox — shafts, gears, forks, and seals. You've held a clutch disc, felt the damper springs, spun a release bearing, and rocked a DMF. You've measured disc thickness, checked flywheel runout, and made go/no-go calls on real components. Tomorrow we move to the other side — automatic transmissions and torque converters. Different technology, same physics — trading speed for torque."

**PPT Content:**
```
DAY 27 RECAP — YOU CAN NOW:

Gear Theory:
  Explain driving/driven gears and calculate ratios
  Show that speed reduction = torque multiplication
  Describe synchronizer operation (cone friction → blocking → engagement)

Gearbox Knowledge:
  Identify input shaft, layshaft, output shaft, all gear pairs
  Explain shift fork/selector mechanism and interlock
  Describe reverse idler gear function

Clutch Knowledge:
  Name all clutch components and their functions
  Distinguish organic vs cerametallic, SMF vs DMF
  Trace the hydraulic actuation path

Inspection Skills:
  Measure disc thickness and rivet depth
  Check pressure plate surface condition
  Measure flywheel runout and DMF play
  Make go/no-go decisions: resurface vs replace

TOMORROW: Automatic Transmissions & Torque Converters
```

---

#### Slide 28: Day 28 Preview
**Visual:** Cutaway image of a torque converter and an automatic transmission valve body

**Instructor Narration:**
> "Tomorrow is automatic transmissions. The torque converter replaces the clutch — and it's a completely different beast. Fluid coupling, stator, lock-up clutch. The planetary gear sets replace the constant-mesh gears — and they can produce any ratio without shift forks. The valve body is the hydraulic brain. And then there's the modern dual-clutch transmission — which is actually two manual gearboxes in one housing controlled by computers. Bring your curiosity and your willingness to think about fluid dynamics. See you tomorrow."

**PPT Content:**
```
DAY 28 PREVIEW: AUTOMATIC TRANSMISSIONS & TORQUE CONVERTERS

• Torque converter: fluid coupling, stator, lock-up clutch
• Planetary gear sets: sun, ring, planet carrier — all ratios from one assembly
• Valve body: the hydraulic control brain
• Dual-clutch (DSG/DCT): two manual gearboxes, zero pedals
• CVT: continuously variable — no fixed gear steps

How it connects:
Day 27 (today): Manual = driver controls ratio and engagement
Day 28 (tomorrow): Automatic = computer and hydraulics control everything

Same physics — different execution.
```

---

## Assessment Checkpoint

**Formative (not graded):**
- Gear ratio calculation: given tooth counts, correctly calculate ratio, output speed, and output torque (Station 4 worksheet)
- Component identification: correctly tag at least 12 of 15 gearbox components on cutaway (Station 1)
- Clutch inspection: correctly measure disc thickness to within 0.1 mm and state go/no-go based on specification (Station 3)
- Synchronizer explanation: verbally describe the four stages of synchronizer engagement to a partner

---

## Key Takeaways

1. Gear ratio = driven teeth / driving teeth — speed reduction equals torque multiplication by the same factor
2. Synchronizers use brass cone friction to match speeds before engagement — worn synchros cause grinding on shifts
3. A manual gearbox uses three shafts (input, layshaft, output) with constant-mesh gears selected by synchronizers and shift forks
4. The clutch assembly is five components: flywheel, friction disc, pressure plate, release bearing, and pilot bearing
5. Clutch hydraulic actuation uses the same DOT 4 fluid and master/slave cylinder principle as the brake system
6. DMFs cannot be resurfaced — excessive play or rattle means replacement
7. Always replace the release bearing, pilot bearing, and friction disc together — false economy to reuse any of them
8. Read the failed parts — every wear pattern tells a diagnostic story about the cause

---

## Preparation for Day 28

**Instructor prep:**
- Source a cutaway or training automatic transmission (conventional planetary type preferred)
- Source a torque converter — ideally one that has been sectioned to show stator, turbine, impeller, and lock-up clutch
- Prepare ATF fluid samples — new vs used (dark, burnt smell) for comparison
- Source a valve body if available — even a photo wall showing valve body passages is valuable
- Print planetary gear set worksheets showing sun/ring/carrier combinations
- If available, source a DSG/DCT mechatronic unit for display

**Learner prep:**
- Review the gear ratio calculations from today — ensure the math is solid
- Re-read notes on the drivetrain chain from Day 26
- Consider: what happens to the clutch pedal in an automatic? (Answer: it disappears — the torque converter replaces it)
