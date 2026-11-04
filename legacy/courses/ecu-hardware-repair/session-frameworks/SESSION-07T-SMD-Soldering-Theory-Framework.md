# SESSION-07T — SMD Soldering Theory
## ECU Hardware Repair (ECUHR) | Module 4: PCB Repair & Soldering Skills
### Day 7 — Theory Block | Duration: 90 minutes

---

## Session Identity

| Field | Detail |
|---|---|
| Session Code | SESSION-07T |
| Module | 4 — PCB Repair & Soldering Skills |
| Day | 7 |
| Block | Theory |
| Duration | 90 minutes |
| Delivery Mode | Instructor-led, classroom/lab bench |
| Prerequisites | Module 3 complete; students can identify SMD component types |

---

## Learning Outcomes

By the end of this session, students will be able to:

- **so-4-1-1:** Select correct solder tip type, iron temperature setting, flux type, and solder alloy for ECU SMD rework
- Explain the metallurgical difference between leaded and lead-free solder and why it matters on real ECU boards
- Describe IPC-610 Class 2 visual joint standards and identify good vs bad joints from photographs
- Explain the role of flux in the soldering process and why omitting it produces failures

---

## Instructor Preparation

### Materials Required
- Soldering iron with multiple tip types physically present for show-and-tell (conical, chisel, bevel)
- Solder samples: one reel Sn63/Pb37, one reel SAC305 lead-free — both visible, labelled
- Flux samples: no-clean pen, rosin paste, liquid flux syringe — physical samples on the bench
- Demo PCB showing: good joints, cold joints, bridges, tombstoned component, lifted pad — pre-marked with correction fluid dots
- Magnifying camera or USB microscope connected to projector
- Printed IPC-610 joint reference card (one per student or pair)
- PPT slide deck: MODULE4-07T-SMD-Soldering-Theory.pptx

### Room Setup
- Projector and screen visible from all seats
- Demo PCB and physical samples on front bench before students arrive
- Microscope camera focused and live-previewing on projector before session starts
- Correction-fluid dots pre-placed on each defect on the demo PCB so the instructor can find them quickly under camera

---

## Session Story Arc

The session follows a deliberate sequence: establish stakes, explain the materials, explain the tools, explain what success looks like, explain what failure looks like, and tie it all back to ECU consequences. Students leave understanding that soldering is a professional craft, not guesswork. Every block connects back to the same point: all four variables must be correct simultaneously for a good joint to form.

---

## Block 1 — Stakes Setting (10 minutes)

### Instructor Script

"Before we talk about solder alloys or flux types, I want you to understand why this module exists. In ECU diagnostics, you identify faults. In ECU repair, you fix them. The most common reason a repaired ECU comes back to the workshop within six months is not that the diagnosis was wrong — it's that the repair was done badly. A cold solder joint, a hairline bridge, a lifted pad. The vehicle drives away, vibration breaks the joint fully, and it fails on the motorway.

Soldering is a perishable skill. If you haven't practised in three months, your technique has degraded. What we cover today is the theory behind why good joints form and why bad joints happen. Tomorrow you will practise until the theory becomes muscle memory."

**Slide 1:** Photograph of a QFP IC on an ECU with one cold joint circled, alongside the vehicle symptom list it produced — intermittent misfires, random DTC codes. Ask the group: "If this car came to your bench with five different fault codes, how long would it take you to find this?" Allow 3 minutes of open discussion.

**Transition:** "We are not learning soldering as a craft for its own sake. We are learning it because it is the difference between a repair that holds and one that wastes your customer's time and your reputation."

---

## Block 2 — Solder Alloys (20 minutes)

### Instructor Script — Opening

"Solder is not solder. The alloy you use changes the temperature you need, the appearance of the finished joint, and how you interpret whether a joint is good or bad. There are two alloys you need to know for ECU work."

**Slide 2:** Title — "Solder Alloys: The Two You Will Use"

---

### 2.1 Leaded Solder — Sn63/Pb37

**Script:**

"The first is tin-lead, typically a 63/37 ratio — 63 percent tin, 37 percent lead. This is the traditional solder that technicians have used for decades. Its melting point is 183 degrees Celsius. It is a eutectic alloy, which means it transitions directly from solid to liquid without a pasty intermediate state. That matters because it solidifies cleanly and quickly once you remove the heat.

A correctly formed leaded joint is shiny. Bright silver. If a joint looks dull and lumpy when you have used leaded solder, that tells you immediately that something went wrong during cooling — usually the joint was disturbed before it solidified, or the pad was not sufficiently hot.

Lead is toxic. It will not harm you from occasional handling with good hygiene, but wash your hands after soldering, do not eat at the bench, and solder in a ventilated area. You are breathing flux fumes, not lead vapour — lead vapour requires temperatures above 1700 degrees Celsius. Your iron is at 350."

**Slide 3:** Close-up photograph of a shiny Sn63/Pb37 joint on a 0603 resistor. Labels: melting point 183°C, eutectic, shiny silver finish.

---

### 2.2 Lead-Free Solder — SAC305

**Script:**

"The second alloy is SAC305 — tin, silver, copper: Sn96.5, Ag3.0, Cu0.5. This is what automotive ECUs are manufactured with under RoHS environmental legislation. Melting point is 217 degrees — 34 degrees higher than leaded. That sounds small, but it means you need a hotter iron and slightly longer dwell time on the joint.

SAC305 joints have a matte, slightly grey finish when correctly formed. This is normal. This is not a cold joint. Students consistently misread SAC305 joints as defects because of the surface appearance. The difference is: a cold joint is lumpy and granular. A correctly formed SAC305 joint is matte-grey but smooth, with a proper concave fillet. Texture tells you far more than colour."

**Slide 4:** Side-by-side photographs. Left: good SAC305 joint — smooth, matte-grey, concave fillet. Right: cold SAC305 joint — lumpy, rough, no fillet. Clearly labelled.

---

### 2.3 Practical Implication for ECU Repair

**Script:**

"When you open an ECU manufactured in the last 15 years, assume it is lead-free. If you are adding or replacing a component — a resistor, a reflowed joint — you can use leaded solder for rework. The alloys will mix at the joint. This is called tin-lead contamination of a lead-free joint. It lowers the effective melting point of that joint to somewhere between 183 and 217 degrees, which is generally acceptable for rework.

What you must not do is set your iron to 340 degrees and try to reflow a SAC305 joint without additional flux. You will get a cold joint because you never fully melted the original solder."

**Slide 5:** Alloy summary reference table.

| Alloy | Ratio | Melt Point | Finish | Use Case | Notes |
|---|---|---|---|---|---|
| Sn63/Pb37 | 63/37 | 183°C | Shiny silver | Training, rework | Eutectic, controlled waste |
| SAC305 | 96.5/3/0.5 | 217°C | Matte grey | OEM factory, lead-free rework | RoHS standard |

**Verbal check question:** "If you pick up a resistor from a scrap ECU made in 2020, what alloy is the original solder likely to be?" Expected answer: SAC305 / lead-free.

---

## Block 3 — Soldering Iron Tips and Temperature (20 minutes)

### Instructor Script — Opening

Hold up physical tip samples as you introduce each type.

"The tip is where all energy transfers from the iron to the joint. It is the single most important variable after the iron itself. A degraded or mismatched tip makes every other technique irrelevant."

**Slide 6:** Photograph grid — conical, chisel, bevel, hoof tip types, each labelled.

---

### 3.1 Tip Types

**Script:**

"Conical tips — pointed, fine. Excellent for single-pin touch-ups on fine-pitch IC packages, or adding solder to one pin without touching its neighbours. Poor thermal mass — they cool down quickly when they contact the board. Use them when precision matters more than speed.

Chisel tips — flat rectangular end. This is what you will use for the majority of ECU rework. Good thermal mass. The flat face contacts more of the pin and pad simultaneously, giving faster and more even heat transfer. Match the chisel width approximately to the pitch of the component you are working with.

Bevel tips are a variant of the chisel — angled flat face. Excellent for drag soldering IC pin rows. The angled face carries a small reservoir of solder which travels across the pin row as you drag.

Hoof tips are U-shaped. Used for drag soldering and some fine-pitch work. Less common in general rework but useful for QFP pin rows."

**Physical demo:** Pass tip samples around the room. Ask students to notice the mass difference between a conical tip and a chisel tip.

---

### 3.2 Tip Temperature

**Script:**

"Temperature settings are a starting point, not an absolute rule. Board mass, ambient temperature, and tip condition all affect actual heat delivered. Use these as defaults:

For leaded solder on SMD components: 330 to 360 degrees Celsius.
For lead-free solder: 360 to 380 degrees Celsius.

Why not higher? Above 400 degrees, flux burns off almost instantly before it does its job, pads lift faster, and IC packages can be thermally damaged. Higher temperature is not faster — it is destructive.

Why not lower? Below 300 degrees on a leaded joint, solder will not flow properly. You dwell too long trying to make it flow, the pad overheats from prolonged contact, and the flux evaporates before it assists wetting."

**Slide 7:** Temperature reference card.

| Condition | Temperature Range | Risk |
|---|---|---|
| Leaded SMD rework | 330–360°C | — |
| Lead-free SMD rework | 360–380°C | — |
| Too high | >400°C | Pad lift, IC damage, instant flux burn-off |
| Too low | <300°C | Cold joints, prolonged dwell, pad damage |

---

### 3.3 Tip Condition — The Neglected Variable

**Script:**

"Your tip must be tinned. A tinned tip has a thin, shiny coating of solder on its working surface. This solder film is the thermal interface between the iron and the joint. When the tip looks black and oxidised — you have all seen them — heat transfer drops dramatically. You can have the iron set to 380 degrees but the actual joint temperature never exceeds 200 because the oxidised layer acts as an insulator.

Before every soldering session: tin the tip. Wipe it on a damp brass wool pad or damp sponge — never sandpaper, which removes the tip plating — then touch it to solder. The tip should silver over immediately. If it does not, repeat. If the tip is badly pitted and will not take solder, replace it.

Between joints: wipe and re-tin every 5 to 10 joints. This is professional discipline, not optional."

**Live demo:** Show a properly tinned tip under the microscope camera. Describe or show an oxidised tip. Tin the oxidised tip live — wipe, touch solder, observe the silvering.

**Slide 8:** Side-by-side photograph — tinned tip (silver, reflective) vs oxidised tip (black, matt). Caption: "Same iron, same temperature setting — completely different heat transfer."

---

## Block 4 — Flux (15 minutes)

### Instructor Script — Opening

"Flux is the most misunderstood consumable in SMD rework. Technicians who struggle with soldering are almost always under-using flux. Let me explain what it actually does."

**Slide 9:** Title — "What Flux Does and Why You Cannot Skip It"

---

### 4.1 The Chemistry (Accessible Explanation)

**Script:**

"Metal surfaces — copper pads, component leads — oxidise when exposed to air. Oxide is not metallic. Solder will not bond to oxide. It beads up and rolls off, like water on a waxed surface. Flux is an acidic compound that dissolves oxide from the surface at soldering temperature, exposing clean metal beneath. Solder then bonds directly to that clean metal surface.

Flux also prevents re-oxidation during the soldering process by forming a protective layer between the hot metal and the surrounding air.

Without flux: solder beads up, bridges form between pins, joints look cold, the result is a mess.

With flux: solder flows, wets the pad and component lead separately, forms a concave fillet, and cools to a correct joint."

**Slide 10:** Diagram — cross-section of a pad. Left panel: pad with oxide layer, solder beading up, no bond. Right panel: pad with flux applied, solder wetting and forming a concave fillet. Labels at each stage.

---

### 4.2 Flux Types

**Script:**

"Three flux types matter in this workshop:

No-clean flux — pen or syringe, rosin or synthetic chemistry formulated to leave a residue that is electrically safe and non-corrosive. You do not need to clean it off. This is what you will use for most work in this course. It is appropriate for ECU rework because you often cannot safely clean an assembled board without risk of damaging connectors or adjacent components.

Rosin flux — traditional rosin dissolved in a carrier solvent. More chemically aggressive and provides excellent wetting. After use, residue must be cleaned off with isopropyl alcohol and a brush. If left on a board, rosin residue absorbs moisture and causes leakage currents on high-impedance circuits.

Water-soluble flux — very aggressive, used in volume manufacturing. Must be cleaned with water immediately after use. Not appropriate for ECU field repair. It is mentioned here so you can recognise a flux type to avoid."

**Slide 11:** Flux comparison table.

| Flux Type | Residue | Clean Required? | Appropriate For |
|---|---|---|---|
| No-clean pen/syringe | Stays on board | No | ECU rework, assembled boards |
| Rosin | Sticky residue | Yes — IPA + brush | Bench work where cleaning is feasible |
| Water-soluble | Wet residue | Yes — water, immediate | Manufacturing only |

---

### 4.3 How to Apply

**Script:**

"Apply flux to the pad and lead before you touch the iron. Not after. If you apply heat first, the surface has already re-oxidised under temperature. Apply flux to the work area, then heat, then apply solder.

For SMD passives: one pass of the flux pen across both pads. For an IC with a row of pins: run the flux pen along the entire row before you begin soldering. You cannot meaningfully over-flux in most rework situations. You can absolutely under-flux — and most beginners do."

**Verbal check question:** "Why does solder bridge between two adjacent IC pins more easily when flux is missing?" Expected answer: without flux, solder does not wet the pads individually — it stays as a molten ball that flows across pins rather than drawing down onto each pad separately. With flux, solder wets each pad independently and separates cleanly.

---

## Block 5 — IPC-610 Joint Standards (15 minutes)

### Instructor Script — Opening

"IPC-610 is the electronics industry standard for acceptable assembly quality. Class 1 is general consumer electronics. Class 2 is dedicated service equipment — automotive, industrial — meaning it must continue working reliably. Class 3 is high-reliability, military and aerospace. ECU repair works to Class 2 as a minimum. Let's look at what Class 2 requires visually."

**Slide 12:** IPC-610 Class overview — brief one-line description of Class 1, 2, and 3.

**Distribute** the printed IPC-610 reference cards. These are for students to keep and use tomorrow.

---

### 5.1 Characteristics of a Good Joint

**Script:**

"A Class 2 acceptable SMD solder joint has five visible characteristics:

One — A concave fillet. The solder curves inward, pulling from pad to component lead. If the solder is convex — bulging outward — that suggests either excess solder or a cold joint where solder never flowed and wet the surface properly.

Two — Full pad coverage. Solder must cover the pad. IPC defines minimum acceptable fillet heights, but as a working rule: if you can see significant exposed copper at the toe or heel of the pad, add more solder.

Three — No visible surface voids. Voids are gas bubbles trapped inside the joint. They reduce mechanical strength. Surface voids — holes you can see — are a Class 2 defect. Subsurface voids require X-ray to detect and are a separate quality concern.

Four — Component centred on pad. No more than 25 percent of the component width shifted off the pad end.

Five — No solder bridges between adjacent pads."

**Slide 13–14:** IPC-610 joint photographs — good joints on 0402, 0603, and SOIC-8. Each photograph labelled with which criteria it demonstrates.

---

### 5.2 Common Defects, Causes, and Fixes

"Now the demo PCB. I am putting it under the camera and we will identify each defect in turn."

**Live demo with microscope camera — work through each marked defect:**

**Cold joint:** Dull, lumpy, granular surface. Cause: pad or lead was not sufficiently hot when solder was applied, or the joint was disturbed during solidification. Fix: add flux, reheat until solder flows cleanly, hold the workpiece still during cool-down.

**Bridge:** Solder connecting two adjacent pads. Cause: excess solder, or insufficient flux causing solder to bead across pins rather than wet them individually. Fix: flux the bridge, draw the iron tip away from the board — solder follows the tip. Alternatively, use desoldering braid.

**Insufficient solder / head-in-pillow:** Solder present but no concave fillet, or component lead sitting on top of a solder ball without true metallurgical bonding. Often invisible until a mechanical shock breaks the joint. Cause: insufficient heat or solder, or flux was absent. Fix: flux and reflow.

**Tombstoning:** One end of a passive component lifts off its pad, standing the component vertical. Cause: one pad reflows before the other — surface tension of the molten solder pulls the component upright. More common during reflow oven assembly but can occur with iron work if one end is heated far ahead of the other. Fix: better flux coverage, simultaneous and even heating of both pads.

**Lifted pad:** Copper pad separated from the PCB substrate. Cause: excessive heat held too long, or mechanical force applied during component removal without adequate heat. This is board damage — repair requires conductive epoxy or a wire jumper to restore the trace. Prevention is the only real solution.

**Slide 15:** Defect photograph grid — each defect labelled with name, cause, and fix summary.

---

## Block 6 — Synthesis and Q&A (10 minutes)

### Instructor Script

"Let's pull this together before you go.

The alloy tells you the temperature range and what a correct finished joint looks like. The tip tells you how efficiently you can transfer that heat. The flux tells you whether the solder will flow or bead. And the IPC standard tells you whether the finished result is acceptable.

None of these variables operates alone. A chisel tip at 360 degrees with no flux produces bridges. The same tip, same temperature, with flux, produces clean joints every time. A correct joint is the product of all four variables being correct simultaneously."

**Slide 16:** Summary diagram — four quadrants: Alloy selection | Tip condition and type | Temperature setting | Flux application. Centre label: "Correct Joint."

**Q&A — prompt questions if silence:**
- "If you're working on a 2019 ECU and the original joints look dull and grey — is that a defect or normal?"
- "You've set the iron to 380 degrees and the solder still won't flow cleanly. What's the first thing you check?"
- "What's the practical difference between a chisel tip and a conical tip?"

**Transition to Hands-On:**

"Tomorrow morning you go to the bench. Today's theory is the foundation. When your instructor corrects your technique, they will use the language from this session. Know this material."

---

## Slide Deck Summary — SESSION-07T

| Slide | Title | Content Type |
|---|---|---|
| 1 | Stakes: One Cold Joint, Five Fault Codes | Photo + discussion prompt |
| 2 | Solder Alloys: The Two You Will Use | Title slide |
| 3 | Sn63/Pb37 — Leaded | Photo + specifications |
| 4 | SAC305 — Good Joint vs Cold Joint | Side-by-side photograph comparison |
| 5 | Alloy Summary Table | Reference table |
| 6 | Soldering Tips — Types | Photograph grid |
| 7 | Temperature Reference Card | Reference table |
| 8 | Tinned vs Oxidised Tip | Side-by-side photograph |
| 9 | What Flux Does and Why You Cannot Skip It | Title slide |
| 10 | Flux Mechanism Diagram | Cross-section diagram |
| 11 | Flux Type Comparison | Reference table |
| 12 | IPC-610 Class Overview | Reference table |
| 13–14 | Good Joint Examples — 0402, 0603, SOIC-8 | Labelled photographs |
| 15 | Defect Photograph Grid | Reference photographs with labels |
| 16 | Summary: Four Variables | Synthesis diagram |

---

## Assessment — SESSION-07T

No formal assessment this session. Verbal check questions embedded throughout (marked above). Students will be formally assessed on joint quality during SESSION-07H. The theory from this session underpins the assessment rubric for that session.

**Instructor note:** If any student cannot distinguish a cold joint from a correctly formed SAC305 joint on the demo PCB under the camera by the end of Block 5, spend additional time before dismissing. This is a hard prerequisite for tomorrow's practical work.

---

## Instructor Notes

- Keep physical samples and the demo PCB accessible throughout — handling real materials is more effective than slides alone
- Do not rush Block 4. Under-application of flux is the root cause of the majority of first-day student errors tomorrow. If students leave today not understanding flux function, they will produce bad joints tomorrow and not know why.
- The IPC-610 reference card given to students today should be brought to tomorrow's hands-on session
- If students ask about BGA soldering: acknowledge it briefly and redirect — it is covered fully in SESSION-08T. Do not attempt to cover it today.
- Time buffer: if you run short, Block 6 Q&A can be condensed to 5 minutes. Do not cut Blocks 3 or 4.
