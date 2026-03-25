# SESSION-08T — Hot Air Rework & IC Package Theory
## ECU Hardware Repair (ECUHR) | Module 4: PCB Repair & Soldering Skills
### Day 8 — Theory Block | Duration: 90 minutes

---

## Session Identity

| Field | Detail |
|---|---|
| Session Code | SESSION-08T |
| Module | 4 — PCB Repair & Soldering Skills |
| Day | 8 |
| Block | Theory |
| Duration | 90 minutes |
| Delivery Mode | Instructor-led, classroom/lab bench |
| Prerequisites | SESSION-07T and SESSION-07H complete; students can form SMD joints with an iron |

---

## Learning Outcomes

By the end of this session, students will be able to:

- **so-4-2-1:** Configure a hot air rework station — temperature, airflow, nozzle selection — for safely removing SOIC and QFP IC packages from an ECU PCB
- **so-4-2-4:** Explain BGA package construction, the concept of reballing, and the equipment required for BGA rework — and assess when BGA work should be referred out
- Describe the risk to adjacent components during hot air work and explain how to protect them

---

## Instructor Preparation

### Materials Required
- Hot air rework station (Hakko FR-301, Quick 861DW, or equivalent) physically on bench — switched off
- Physical nozzle set: round nozzles in multiple sizes, at least one square/rectangular QFP nozzle
- Physical component samples: SOIC-8, SOIC-16, QFP-44, QFP-64 (sourced from scrap PCBs or component suppliers)
- BGA package sample — component only, not mounted (e.g., automotive MCU or processor module from scrap ECU)
- BGA X-ray image printout or high-resolution on screen: showing good BGA joints vs voided BGA joints
- Kapton tape strip and small piece of aluminium foil — for adjacent-component shielding demo
- Scrap ECU PCB showing a QFP IC — for demonstrating what the instructor will later do in SESSION-08H
- PPT slide deck: MODULE4-08T-Hot-Air-IC-Packages.pptx
- USB microscope or magnifying camera, connected to projector

### Room Setup
- Hot air station on front bench, visible to all students, with nozzle set displayed beside it
- Nozzle samples available to pass around
- BGA sample component available to pass around

---

## Session Story Arc

Session 07T established the principles of heat, flux, alloy, and joint quality. This session extends those principles from a single iron tip to a distributed heat source — hot air — and from small passives to large multi-pin IC packages. The BGA section introduces the upper boundary of hands-on ECU repair, making clear where shop-level repair ends and specialist equipment begins.

---

## Block 1 — Context: Why Hot Air? (8 minutes)

### Instructor Script

"Yesterday you learned to solder with an iron. The iron is a point heat source — you touch one pad at a time. That works for 0402 resistors and SOIC-8 packages where the pins are spaced 1.27mm apart.

Now consider a QFP-64 — a 64-pin IC where the pins are spaced 0.5mm apart and are on all four sides. You cannot access four sides of an IC simultaneously with an iron. You could drag-solder, but you cannot remove a QFP with an iron without either destroying the IC or damaging the pads.

Hot air solves this. It applies heat evenly across a large area. The solder on all pins reaches liquid temperature approximately simultaneously, so the IC can be lifted free with no mechanical force. The pads are left intact.

Hot air also introduces new risks. It heats everything in its path — not just the target IC. Adjacent components, connectors, and plastic PCB material can all be damaged. Configuration matters. Today you learn how to configure and use it correctly."

**Slide 1:** Photograph of a QFP-64 on an ECU. Caption: "64 pins, 0.5mm pitch. Four sides. A single iron tip cannot access this simultaneously."

---

## Block 2 — Hot Air Station Anatomy (10 minutes)

### Instructor Script

"Let's look at the machine itself. Every hot air station has three controls you need to understand: temperature, airflow, and nozzle."

**Slide 2:** Photograph of the hot air station with three controls annotated — temperature dial/display, airflow dial/display, nozzle attachment point.

---

### 2.1 Temperature Control

**Script:**

"The temperature setting on a hot air station works differently from a soldering iron. The iron tip is in direct contact with the joint — the temperature setting is the actual joint temperature. Hot air temperature is the temperature of the air leaving the nozzle. By the time that air reaches the PCB, it has lost heat to the surrounding environment. The effective temperature at the joint is always lower than the station setting.

The practical implication: hot air station settings run higher than iron settings for the same outcome. Use these defaults:

SOIC packages: 300 to 330°C station setting. These are small, low-mass packages that heat quickly.
QFP packages: 330 to 360°C. More thermal mass from the IC body, more pins, more copper.
Board shielding with Kapton: you may need to increase slightly as tape partially blocks heat.
Lead-free joints: add 10 to 20°C to each range.

The key principle: start lower and increase. You can always add heat. A lifted pad or damaged adjacent component cannot be undone."

**Slide 3:** Hot air temperature reference table.

| Component Type | Station Temperature (Leaded) | Station Temperature (Lead-Free) |
|---|---|---|
| SOIC-8, SOIC-16 | 300–330°C | 320–350°C |
| QFP (44, 64 pin) | 330–360°C | 350–380°C |
| Large thermal mass (copper pour beneath IC) | Add 10–20°C | Add 10–20°C |

---

### 2.2 Airflow Control

**Script:**

"Airflow is the variable that most beginners ignore and most experienced technicians treat as the most important setting.

Low airflow — 1 to 3 on a typical 10-point dial. Use this for small SMD components near the target IC. Low airflow heats the target but does not blow adjacent 0402 and 0603 passives off the board. The risk with low airflow is that heat builds up unevenly and slowly — you need more patience.

Medium airflow — 3 to 5. Standard QFP removal and replacement. Heats the IC evenly and reasonably quickly. Does not create turbulence that moves adjacent components.

High airflow — above 5. Avoid during precision rework. Creates a vortex that will blow small components off the board and can delaminate PCB material under prolonged exposure.

Rule of thumb: use the lowest airflow that achieves the target temperature within a reasonable dwell time. If you need more than 30 seconds at a low airflow to see solder melting, increase airflow slightly rather than dramatically increasing temperature."

**Slide 4:** Airflow risk diagram — arrows showing air blast radius at low/medium/high settings, with adjacent component positions annotated.

---

### 2.3 Nozzle Selection

**Script:**

"The nozzle shapes and concentrates the air stream. Choosing the wrong nozzle is like using a garden hose set to 'jet' when you need 'mist' — you will blast heat where you do not want it.

Round nozzles: general use, available in multiple diameters. Choose a round nozzle approximately matching the short dimension of your target component. The 8mm and 10mm round nozzles cover most SOIC work.

Square/rectangular QFP nozzles: these are matched to QFP package sizes. The nozzle sits over the entire IC and directs air evenly downward onto all four pin rows simultaneously. You will see these labelled by millimetre dimensions — match the nozzle to the IC body size, not the overall package footprint. Using a QFP nozzle that is too small will heat only the centre of the package; too large will heat adjacent components.

Chip nozzles: very small, for individual 0402/0603 replacements. Not commonly used for ECU rework but worth knowing."

**Physical demo:** Pass the nozzle set around the room. Ask students to identify which nozzle they would select for the QFP-64 sample IC shown on screen.

**Slide 5:** Nozzle type photograph grid — round (small, medium, large), QFP square, chip nozzle — each labelled with use case.

---

## Block 3 — Hot Air Technique (20 minutes)

### Instructor Script — Opening

"Configuration is half the skill. Technique is the other half. Let's cover the mechanics of how to use hot air correctly."

**Slide 6:** Title — "Hot Air Technique: Distance, Motion, and Indicators"

---

### 3.1 Distance and Motion

**Script:**

"Hold the nozzle 5 to 10 millimetres above the component surface. Too close — the airflow physically moves the IC and can crack component bodies or lift pads by steam pressure. Too far — heat dissipates before reaching the joint.

Keep the nozzle moving. A slow circular motion over the package ensures even heating across all pins. If you hold the nozzle stationary, the centre of the IC reaches temperature before the peripheral pins — you will lift the IC with pins on the outside still cold, and you will tear the pads.

The motion should be slow — a full circle every 3 to 5 seconds. Keep the nozzle level, not angled. An angled nozzle directs heat to one edge of the component preferentially.

For QFP work with a square nozzle: the circular motion is a small oscillation — the nozzle is approximately centred over the package and you make small, slow movements. You are ensuring the entire package heats evenly rather than targeting a specific pin row."

---

### 3.2 Indicators — How to Know When Solder Is Liquid

**Script:**

"Do not attempt to lift the IC until you have a positive indicator that the solder is fully liquid. This is the most common mistake. Students see the solder flux starting to bubble or smoke, assume the solder is liquid, and pull — damaging the pads because the solder was only softened, not fully molten.

Indicators that solder is liquid:

One — The IC shifts slightly. When all joints are liquid, surface tension is no longer holding the IC rigidly. You will see a very slight movement or settle as the IC floats on liquid solder. This is the most reliable indicator.

Two — Probe test. Gently touch the corner of the IC with a fine pick or tweezers — it should move freely with no resistance. If there is any stiffness, the solder is not fully liquid.

Three — Time — but this is unreliable alone. At correct settings, a QFP-64 typically reaches full reflow in 20 to 40 seconds. Use time as a guideline but always confirm with the probe test.

Never use force to remove a component. If it does not lift with a light tweezers touch, the solder is not liquid. Add more heat. Force equals pad damage."

**Slide 7:** Close-up photograph or diagram of QFP during reflow — annotated to show correct nozzle height, circular motion path, and the indicator of IC floating on solder.

---

### 3.3 Adjacent Component Protection

**Script:**

"The PCB around a QFP does not care that you are targeting the QFP. Heat dissipates outward. Any component within 5–10mm of the target IC is at risk of being reflowed or blown off during the process.

Two protection methods:

Kapton tape: high-temperature polyimide tape, rated to 260°C continuous. Apply tape over any adjacent component within the risk radius before starting. It will not prevent all heat transfer but significantly reduces it.

Aluminium foil: more effective than tape for larger adjacent components or connectors with plastic bodies. Fold a small piece and press it over the at-risk area. Aluminium reflects heat. It does not burn.

Practical discipline: before switching on the hot air station, look at what is within 10mm of your target IC. Shield anything that should not be reflowed. It takes 30 seconds and prevents expensive board damage."

**Physical demo:** Show Kapton tape and foil applied to the demo PCB around the target QFP.

**Slide 8:** Overhead photograph of QFP on ECU PCB, with risk radius circle drawn, Kapton tape placement annotated.

---

### 3.4 QFP Replacement — Drag Soldering Review

**Script:**

"Once the pads are clean and a replacement QFP is aligned — which you will practise in the lab session — the soldering method is drag soldering with a chisel tip, exactly as you did with the SOIC-8 yesterday. The principles are identical. The challenge is scale: a QFP-64 has 16 pins per side instead of 4.

Flux is critical. Apply flux along the entire pin row before touching the iron. Then drag. Count the pins under magnification after every side — not just look at the row, count the pins. A pin with no individual fillet is an open circuit.

The other challenge unique to QFP is pin alignment. A QFP pin that is bent or misaligned before soldering will be misaligned after. Inspect every pin under magnification before soldering. A bent pin must be straightened with a fine pick before flux is applied."

**Slide 9:** Photograph sequence — QFP pin row before soldering (aligned), after drag solder (joints formed), after bridge fix (clean). Each labelled.

---

## Block 4 — BGA Package Construction and Rework (25 minutes)

### Instructor Script — Opening

"Now we reach the upper boundary of hands-on ECU repair. BGA — Ball Grid Array — is the package type used for the most powerful and densely integrated ICs in modern ECUs. Understanding what it is and what its failure modes are allows you to make an informed decision about whether to attempt rework or refer the board out. Attempting BGA rework without the correct equipment destroys boards."

**Slide 10:** Title — "Ball Grid Array: What It Is and Why It Is Different"

---

### 4.1 BGA Construction

**Script:**

"A BGA package has its electrical connections on the bottom of the IC body — not on the sides. The connections are small solder balls, arranged in a grid pattern beneath the package. You cannot see them when the IC is sitting on a PCB. All inspection of BGA joints must be done by X-ray."

**Pass the BGA sample component around the room.** Ask students to look at the underside.

"Count how many ball positions you can see on that sample. Then look at the IC size. Now think about placing that IC accurately on a PCB with the same number of pad positions — all hidden under the package — and reflowing all those connections simultaneously in an oven or with an IR station."

**Slide 11:** Diagram — BGA package cross-section. Labels: IC die, substrate, solder balls, PCB pads. Show ball size (typically 0.4–0.8mm diameter) and pitch (0.5–0.8mm typical in automotive ECUs).

---

### 4.2 BGA Failure Modes

**Script:**

"BGAs fail for specific reasons that matter for diagnosis:

Mechanical stress — automotive ECUs experience vibration constantly. BGA solder joints are relatively stiff and do not flex. Over time, differential thermal expansion between the PCB and the IC body creates micro-cracks in the solder balls. These cracks start at the outer corners of the BGA array, which see the most mechanical movement. Symptom: intermittent fault, usually temperature or vibration dependent.

Underfill delamination — many automotive BGAs are underfilled from the factory: a polymer compound is injected under the package to mechanically lock the IC to the PCB and reduce joint stress. If the underfill delaminates, the joints are exposed to full mechanical stress and fail faster. Diagnosis requires microscopy or X-ray.

Poor original reflow — from manufacturing, occasionally a BGA joint has a void, cold joint, or incomplete ball. These fail earlier under operational stress. X-ray is the only diagnostic method.

Reballing — if a BGA IC has been removed from a board, the solder balls are consumed by the reflow process. Before the IC can be reinstalled, new balls must be applied using a reballing stencil and solder ball paste. This process is called reballing."

**Slide 12:** BGA X-ray images — left: good joint array (uniform bright circles), right: joint with large void (dark area within circle) and partial connection. Label each defect type.

---

### 4.3 BGA Rework Equipment

**Script:**

"For BGA rework to be performed at all — not just BGA replacement, but removal and replacement with new balls — the following equipment is required at a minimum:

Infrared reflow station or bottom heater: preheats the entire board from below to reduce thermal stress during top-side hot air reflow. Without this, the temperature differential between the BGA and the cold board causes board warping and PAD damage.

Reballing stencil: a custom metal stencil with holes matching the exact BGA ball pattern of the specific IC. You cannot use a generic stencil. The stencil is sourced for the exact IC part number.

Solder ball paste and BGA solder balls: typically SAC305, matching the IC specifications. Ball size must match the original.

Optical alignment station: to place the IC onto the PCB pads with sub-millimetre accuracy. You cannot align a BGA by eye — there are no visible pins.

X-ray inspection: to verify that the completed joint array has no voids, shorts, or missing balls. Without X-ray, you cannot confirm a BGA rework has succeeded. You can power on the board and test function, but a board that powers on may still have voids that will fail under vibration within 12 months.

For most repair workshops: BGA means replacing the entire ECU module or the complete ECU board. Unless your workshop has an IR reflow station, optical alignment, and X-ray capability, BGA rework is not within scope. The value of knowing this today is that you can tell a customer definitively: 'This ECU has failed at the processor BGA — it requires specialist BGA rework or module replacement', rather than attempting a repair that will produce an unreliable result."

**Slide 13:** Equipment list diagram — IR reflow station, reballing stencil, optical aligner, X-ray inspection system. Each with a brief note on function.

**Slide 14:** Decision flowchart — "Does this ECU have a BGA fault?" → Yes → "Does workshop have full BGA equipment?" → No → "Refer out or replace module." → Yes → "Proceed with BGA rework procedure."

---

### 4.4 BGA vs Workshop Capabilities — Honest Assessment

**Script:**

"I want to spend two minutes being direct about this.

Some technicians — after watching a YouTube video — will attempt BGA rework with a hot air gun and a stencil from a generic supplier. Some of them get it to work once. The board powers on, the customer is happy, the job is billed. Six months later the vehicle fails on a motorway because the joint that looked fine had a void.

BGA rework is not impossible in a non-specialist workshop. But it requires discipline, equipment, and process control that is very difficult to achieve without dedicated tooling. The X-ray step is not optional — it is the only way to know whether the rework succeeded. If you cannot X-ray, you are guessing.

This course does not cover practical BGA rework because the minimum equipment standard to do it correctly is above what most workshops have. What you will leave this course with is: the knowledge to diagnose BGA-related faults, the language to explain them to customers, and the judgment to know when to refer."

---

## Block 5 — Pre-Lab Review (15 minutes)

### Instructor Script

"Tomorrow's lab session begins with QFP removal. You will be using the hot air station with settings we have discussed today. Before we close, let's run through the configuration checklist you will use tomorrow."

**Slide 15:** Hot air pre-use checklist (also reproduced at the top of SESSION-08H framework).

**Live demonstration — instructor configures the station on the bench:**

1. "I'm selecting the QFP nozzle. I'm matching the nozzle to the QFP body on this practice board." Physically attach nozzle.
2. "I'm setting temperature to 350°C — this is a lead-free board." Set temperature.
3. "I'm setting airflow to 3." Set airflow.
4. "I'm looking at what's adjacent to the QFP. I see two 0603 resistors within 5mm. I'm taping them." Apply Kapton tape.
5. "I'm not switching on yet. I'm going to apply flux to the QFP pins first." Apply flux to demo PCB.
6. "Now I'll switch on, preheat for 10 seconds off the board, then begin circular motion 8mm above the IC."

Walk through each step — do not actually reflow the QFP, just demonstrate the setup posture and motion.

"Tomorrow you will do each of these steps on a live PCB. Today you need to know why each step exists."

**Verbal check questions:**
- "If the solder on the QFP does not appear liquid after 40 seconds, what are the two things you check before increasing temperature?"
- Expected: airflow too low to deliver heat effectively; nozzle too far from board; adjacent component shielding is over the target IC.
- "Why is it dangerous to remove a QFP with force before the solder is fully liquid?"
- Expected: solder acts as an adhesive — pulling before liquid state lifts pads.

---

## Block 6 — Q&A and Session Close (12 minutes)

### Instructor Script

"Let's take questions. I want to make sure we're clear on three things before tomorrow:

One — The difference between iron work and hot air work is not just the tool. It's the principle: distributed heat requires different discipline around adjacent components, dwell time, and lift technique.

Two — QFP drag soldering is the same technique as SOIC-8 drag soldering from yesterday. More pins, same principle.

Three — BGA is real, it exists in ECUs you will encounter, and it has a defined boundary in terms of what shops can safely do."

**Open Q&A:** Allow students to raise any questions from yesterday's lab or from today's theory.

**Transition to SESSION-08H:**

"Tomorrow morning you will remove a QFP, clean the pads, align a replacement, and solder it. By the end of tomorrow afternoon you will have completed the two most technically demanding repair operations in this entire course. Everything after this is consolidation."

---

## Slide Deck Summary — SESSION-08T

| Slide | Title | Content Type |
|---|---|---|
| 1 | Why Hot Air? QFP-64 Photograph | Photo + context |
| 2 | Hot Air Station Anatomy | Annotated photograph |
| 3 | Temperature Reference Table | Reference table |
| 4 | Airflow Risk Diagram | Diagram |
| 5 | Nozzle Types | Photograph grid |
| 6 | Hot Air Technique: Distance, Motion, Indicators | Title slide |
| 7 | Nozzle Position and Motion Diagram | Annotated diagram |
| 8 | Adjacent Component Protection | Annotated overhead PCB photo |
| 9 | QFP Drag Soldering Sequence | Photograph sequence |
| 10 | BGA: What It Is and Why It Is Different | Title slide |
| 11 | BGA Cross-Section Diagram | Technical diagram |
| 12 | BGA X-Ray: Good vs Defective | X-ray comparison |
| 13 | BGA Rework Equipment List | Diagram with labels |
| 14 | BGA Decision Flowchart | Decision tree |
| 15 | Hot Air Pre-Use Checklist | Reference checklist |

---

## Assessment — SESSION-08T

No formal assessment this session. Verbal check questions embedded at Blocks 3 and 5.

Practical assessment follows in SESSION-08H. The configuration and technique concepts from this session are directly assessed through the lab sign-off checklist in SESSION-08H.

---

## Instructor Notes

- Spend adequate time on the "do not force the component" principle in Block 3. Pad lifting from premature component removal is the most common cause of irreversible board damage in tomorrow's lab.
- The BGA section in Block 4 is intentionally honest about workshop limitations. Do not oversell BGA capability to avoid damaging student confidence — the opposite is true: a technician who knows the limits of their equipment makes better referral decisions and retains customer trust.
- If students arrive having already attempted QFP removal at home or in a prior role, encourage them to share their experience during the pre-lab review. Real experience normalises the challenge and provides peer learning.
- The live station configuration demo in Block 5 is important. Students who see the setup process once before they perform it in the lab make fewer errors during station preparation.
