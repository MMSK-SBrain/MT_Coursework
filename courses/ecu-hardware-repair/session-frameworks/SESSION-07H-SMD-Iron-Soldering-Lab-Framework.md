# SESSION-07H — SMD Iron Soldering Lab
## ECU Hardware Repair (ECUHR) | Module 4: PCB Repair & Soldering Skills
### Day 7 — Hands-On Block | Duration: 90 minutes

---

## Session Identity

| Field | Detail |
|---|---|
| Session Code | SESSION-07H |
| Module | 4 — PCB Repair & Soldering Skills |
| Day | 7 |
| Block | Hands-On |
| Duration | 90 minutes |
| Delivery Mode | Workshop — individual bench stations |
| Prerequisites | SESSION-07T completed; students have IPC-610 reference card |

---

## Learning Outcomes

By the end of this session, students will be able to:

- **so-4-1-2:** Solder 0402, 0603, 0805 passive components and an SOIC-8 IC on a practice PCB with correctly formed joints meeting IPC-610 Class 2 criteria
- **so-4-1-3:** Remove SMD components using desoldering wick/braid; inspect pads for damage and confirm they are clean and intact

---

## Equipment List — Per Student Station

| Item | Quantity | Notes |
|---|---|---|
| Temperature-controlled soldering iron | 1 | Hakko FX-888D or equivalent |
| Chisel tip 2mm | 1 | Fitted and tinned before session |
| Conical tip 0.5mm | 1 | Available in tip tray for student to change |
| Practice PCB — SMD | 1 | Pre-populated pads: 0402, 0603, 0805, SOIC-8 footprints |
| Solder — Sn63/Pb37 0.6mm | 1 reel | Labelled |
| Solder — SAC305 0.6mm | 1 reel | Labelled |
| No-clean flux pen | 1 | Kester 951 or equivalent |
| Desoldering wick/braid 2mm | 1 roll | |
| SMD component kit | 1 bag | 10x 0402 resistors, 10x 0603 resistors, 5x 0805 capacitors, 2x SOIC-8 packages (blank or low-value ICs) |
| Reverse-action tweezers | 1 pair | |
| Fine-point tweezers | 1 pair | |
| USB microscope or magnifying loupe (10x) | 1 | Shared between 2 students if necessary |
| IPA wipes or IPA in dropper bottle | 1 | For cleaning after rosin flux if used |
| Tip cleaner — brass wool | 1 | At every station |
| Safety glasses | 1 pair | Mandatory |
| Fume extractor | 1 | Shared per bench row; positioned between stations |

### Instructor Equipment
- Instructor station with overhead camera mirroring to room screen
- Spare practice PCBs (at least 2 per 10 students for replacement if a PCB is damaged)
- Reference PCB: instructor pre-built with labelled good and bad joints for comparison
- Spare tips, spare solder, spare flux
- Multimeter for continuity checks during sign-off

---

## Safety Notes

- Safety glasses mandatory from the moment the iron is switched on. No exceptions.
- The soldering iron tip reaches 360°C. Students must return the iron to its holder between joint placements — not set it on the bench surface.
- Fume extractors must be running. Confirm before starting.
- Lead-containing solder is in use. Students must wash hands before leaving the workshop. No food or drink at benches.
- No loose sleeves near the iron. Hair tied back.
- If a student burns themselves: cool running water for 10 minutes, report to instructor. Do not apply ice.

---

## Instructor Demonstration — Before Students Begin (15 minutes)

The instructor demonstration is the most important 15 minutes of the session. Every student must be able to see the instructor's hands and the overhead camera screen simultaneously. Do not begin student work until the full demo is complete.

### Demo Sequence

**Demo 1: Iron setup and tip condition check (2 minutes)**

"Before I touch the board, I check the tip. I wipe it on the brass wool — not a wet sponge, which causes thermal shock — and I touch it to solder. Watch what happens."

Show tinned tip silvering over immediately. "If it doesn't silver instantly, the tip is oxidised or cold. I keep wiping and re-tinning until it does."

Set iron temperature to 340°C for the demo (leaded solder).

---

**Demo 2: Soldering an 0603 resistor (5 minutes)**

"I'm going to solder this 0603 resistor. Watch the sequence: flux first, component placement, heat, solder, remove."

Step by step under the camera:

1. Apply flux pen across both pads. "I can see the flux sitting on the pad — it looks wet."
2. Pick up the resistor with reverse-action tweezers. "The tweezers hold it closed. I'm not gripping — I'm releasing to grip."
3. Tack one end: touch iron to one pad for 1 second, apply a small amount of solder, remove iron, hold component still for 3 seconds. "I'm not moving until the solder solidifies."
4. Release tweezers. Inspect tack joint under camera. "That tack joint is rough — it's just holding the component in place. That's fine for now."
5. Apply flux to the free end. Solder the free end: iron touches pad and lead simultaneously, solder feeds in from the side, iron withdraws. "One to two seconds of heat. I fed solder in from the side, not on top of the iron."
6. Reflow the tack joint: add flux, reflow. "Now both joints are finished."
7. Show finished joints under camera. "Concave fillet, full pad coverage, shiny. That is an IPC-610 Class 2 joint."

Ask students: "What would this look like if I hadn't applied flux?" Allow brief answer.

---

**Demo 3: Soldering an SOIC-8 (5 minutes)**

"The SOIC-8 has eight pins. The process is tack-and-drag, not pin-by-pin."

Step by step under the camera:

1. Apply flux generously along both rows of pads. "More flux than feels comfortable. Trust it."
2. Align the IC by eye — pin 1 dot to the pin 1 marker on the PCB. "Alignment before any heat. Once one pin is tacked, realignment is very difficult."
3. Tack pin 1 (corner pin): touch iron to corner pin and pad, apply tiny amount of solder, withdraw. "Just enough to hold it. Verify alignment under magnification before proceeding."
4. Confirm alignment. Tack the diagonal corner pin (pin 5 on SOIC-8). "Now the IC cannot shift."
5. Drag solder the remaining pins on one side: apply flux to the row, load a small amount of solder onto the chisel tip, drag smoothly from pin 1 toward pin 4 in one slow pass. "The tip stays at 45 degrees to the row. Slow and steady. I'm not pressing — I'm barely touching."
6. Inspect under camera: "I have two bridges. That is normal for a first drag pass. I'm going to fix them."
7. Fix bridges: apply flux pen directly to the bridge, touch chisel tip — solder follows the tip away from the bridge.
8. Repeat for the other side.
9. Final inspection under camera: every pin, individually, under magnification.

"Every pin must have its own fillet. A pin with no solder or a sunken joint is an open circuit. A bridge is a short circuit. Both will cause failures."

---

**Demo 4: Removing a component with desoldering braid (3 minutes)**

"Now I'm going to remove the 0603 I just soldered. This shows you how to use braid — and how to check pad condition after removal."

1. Apply flux to both joints.
2. Place braid over one joint, press iron on top of braid — not on the joint directly.
3. "The braid wicks the solder. I can see it changing colour as solder is absorbed. When it stops absorbing, I move to fresh braid."
4. Lift the component away with tweezers once both joints are cleared.
5. Inspect pads under camera. "Clean copper, no residue, no lifted pad. That is what you are aiming for."

"If a pad lifts during removal, it means either the pad was already weakened, you used too much heat, or you pulled the component before the solder was fully liquid. No force — only heat. If the component does not come away with gentle tweezers pressure, add more heat."

---

## Student Practical — Step-by-Step Procedure

### Stage 1: Iron Setup and Tip Check (5 minutes)

All students:
1. Switch on soldering iron. Set to 340°C (leaded solder).
2. Wait for iron to reach temperature (indicator light or display confirms).
3. Wipe tip on brass wool.
4. Touch tip to solder. If it does not silver instantly, repeat until it does.
5. Inform instructor if tip will not tin after three attempts — tip may need replacement.

**Instructor circulation:** Check every station. A student who cannot tin their tip will struggle with everything that follows. Resolve tip issues before moving on.

---

### Stage 2: Solder 0402 Resistors — Two Components (10 minutes)

Technique: individual pin tacking

1. Apply flux pen across both pads of the first 0402 footprint.
2. Pick up the 0402 with fine-point tweezers.
3. Place the component on the pads. Confirm it is centred.
4. Tack one end: iron tip to one pad (1 second), apply a tiny amount of solder, withdraw, hold still.
5. Release tweezers. Inspect — component should not move.
6. Flux the free end. Solder the free end: touch iron to pad and lead simultaneously, feed solder from the side (not from the top), withdraw after 1–2 seconds.
7. Reflow the tack joint with fresh flux.
8. Inspect under loupe or USB microscope.
9. Call instructor for Stage 2 sign-off before proceeding.
10. Repeat for second 0402.

**Common mistakes at this stage:**
- Picking up the 0402 with tweezers and losing it — "it's small, it will move. Keep a wrist rest on the bench and move slowly."
- Tombstoning — one end lifts. Cause: uneven heating. Fix: ensure flux on both pads, tack first end minimally, reheat more gently.
- Bridge across the gap between pads (if pads are close) — add flux and draw bridge away with iron tip.

---

### Stage 3: Solder 0603 Resistors — Two Components (10 minutes)

Same technique as Stage 2. The 0603 is more forgiving due to larger pad size.

1–8: Same sequence as Stage 2.
9. Inspect under loupe. Confirm concave fillet on both ends.
10. Call instructor for Stage 3 sign-off.
11. Repeat for second 0603.

**Additional check at this stage:** Confirm student is re-tinning the tip between each component. If tip is visibly dark, intervene immediately.

---

### Stage 4: Solder 0805 Capacitors — Two Components (10 minutes)

The 0805 is the largest passive in this session. Technique is the same but the larger component thermal mass means slightly longer dwell time is acceptable (2–3 seconds rather than 1–2).

1–8: Same sequence as Stage 2.
9. Inspect under loupe.
10. Call instructor for Stage 4 sign-off.

---

### Stage 5: Solder SOIC-8 IC (20 minutes)

This is the most technically demanding component in this session. Students should have at least 20 minutes remaining before attempting it.

1. Apply flux generously along both rows of SOIC-8 pads.
2. Place SOIC-8 on pads. Align pin 1 dot to board marker.
3. Inspect alignment under loupe before any soldering. If not centred, reposition — do not heat yet.
4. Tack corner pin 1: minimal solder, withdraw, hold still.
5. Check alignment again. If misaligned, reheat pin 1 and reposition.
6. Tack diagonal corner pin.
7. Inspect: IC should be flat, centred, not rocking.
8. Apply fresh flux along the first row of pins.
9. Load a small amount of solder onto the chisel tip (the tip should be loaded — not dripping).
10. Place tip at 45 degrees to pin row. Drag slowly from pin 1 toward the last pin on that side. One continuous motion.
11. Inspect under loupe. Bridges are expected and normal at this stage.
12. Fix bridges: apply flux pen directly to bridge, touch tip — solder follows the tip.
13. Inspect every pin: each should have its own visible fillet.
14. Repeat steps 8–13 for the other row.
15. Final inspection: all 8 pins, under maximum available magnification.
16. Call instructor for Stage 5 sign-off.

**Common mistakes at this stage:**
- Misalignment before tacking — stress to students: stop and look before touching the iron to anything.
- Pressing too hard with the iron during drag — the tip should barely contact the pins. Pressure does not increase heat transfer; dwell time does.
- Attempting to clean a bridge with braid before checking whether flux + tip will resolve it first. Braid is the last resort, not the first.
- Adding too much solder during the drag pass. The solder loaded on the tip should be a small reservoir — not a blob.

---

### Stage 6: Component Removal and Pad Inspection (10 minutes)

Students will remove one 0603 resistor using desoldering braid.

1. Apply flux to both joints of the target 0603.
2. Cut a 20mm length of fresh braid. Old, used, solder-filled braid does not wick.
3. Place braid over one joint. Press iron on top of braid (not directly on the pad).
4. Watch for solder to wick into braid — colour change from copper to silver. This takes 2–5 seconds.
5. Move to fresh section of braid for the second joint.
6. Once both joints are clear, lift component gently with tweezers. If it does not lift with minimal force, add more heat — do not pull.
7. Inspect both pads under loupe:
   - Copper should be visible, clean, flat
   - No lifting of pad edge
   - No solder residue mounding on the pad surface
8. If pads are clean and intact, wipe with IPA.
9. Call instructor for Stage 6 sign-off.

**Common mistakes at this stage:**
- Using braid that has already absorbed solder — it will not wick. Always use a fresh section.
- Pressing iron on the pad directly rather than through the braid — this increases pad lift risk.
- Pulling the component before the solder is liquid — students feel the component loosening and pull. Tell them: "If it needs force, the solder is not liquid yet."

---

## Instructor Circulation Guide

During student practical work, the instructor circulates continuously. Recommended priority order for intervention:

| Priority | Observation | Intervention |
|---|---|---|
| 1 — Immediate | Iron left unattended off its holder on bench surface | Instruct student to return iron to holder. Safety issue. |
| 1 — Immediate | Safety glasses removed | Instruct student to replace before proceeding. |
| 2 — High | Student pressing iron down on component or pad | "You are applying pressure. Heat transfers through contact, not pressure. Rest the iron on the pad — do not push." |
| 2 — High | Oxidised tip (black) — student continuing to use it | Stop the student. Demonstrate re-tinning. |
| 2 — High | No flux applied before any solder work | "Apply the flux pen before the iron touches anything." |
| 3 — Standard | Bridges on SOIC-8 pins | "That is expected. Apply flux and draw the tip slowly away from the bridge." |
| 3 — Standard | Cold joint (dull, grainy finish) | "That joint is cold. Apply flux, reheat until the solder flows, hold still during cool-down." |
| 4 — When possible | Good joints formed | Positive reinforcement. Point the student's good work out to neighbours — peer observation is effective. |

---

## Student Sign-Off Checklist

The instructor signs off each stage when the work meets IPC-610 Class 2 minimum criteria. Students may not proceed to the next stage without sign-off.

### Sign-Off Criteria

**Stage 2 — 0402 Resistors (x2)**
- [ ] Both components centred on pads, not tombstoned
- [ ] Concave fillet visible on both ends of both components
- [ ] No bridges
- [ ] No visible cold joints (dull, grainy texture)
- [ ] Tip was re-tinned during work (observed)

**Stage 3 — 0603 Resistors (x2)**
- [ ] Both components centred
- [ ] Concave fillet on both ends
- [ ] No bridges
- [ ] No cold joints

**Stage 4 — 0805 Capacitors (x2)**
- [ ] Both components centred
- [ ] Concave fillets
- [ ] No bridges
- [ ] No cold joints

**Stage 5 — SOIC-8**
- [ ] IC flat and centred on all pads
- [ ] All 8 pins have individual visible fillets
- [ ] No bridges between any adjacent pins
- [ ] No lifted or tombstoned pins
- [ ] No cold joints on any pin
- [ ] Pin 1 aligned to board marker

**Stage 6 — Desoldering and Pad Inspection**
- [ ] Component removed without pad lift
- [ ] Both pads clean and flat
- [ ] No solder mounding on pads
- [ ] No copper discolouration suggesting overheating

**Instructor sign-off field:** ___________________ Date: ____________

---

## Common Mistakes Reference — Instructor Quick Guide

| Defect | Root Cause | In-Session Fix |
|---|---|---|
| Cold joint | Pad not hot enough, or moved during cooling | Flux + reheat until solder flows; hold still |
| Bridge | No flux, or tip overloaded with solder | Flux + draw tip away; braid as last resort |
| Tombstone | Uneven heating of both pads | Reflux both pads; reheat simultaneously or use two irons if available |
| Lifted pad | Too much heat dwell, or component pulled before solder liquid | Cannot be fully undone — document and advise repair approach |
| Solder balling | No flux, or pad oxidised | Clean pad with braid, flux well, retry |
| SOIC misalignment | IC placed before alignment checked | Reflow tack pin, reposition, recheck before continuing |
| Braid not wicking | Used braid section, or insufficient heat | Fresh braid section; increase iron temperature to 360°C |

---

## Debrief — Last 10 Minutes

Bring all students together at the front bench. Instructor holds up two or three practice PCBs from the group — one with strong results, one with a common defect. Both are discussed without naming the student.

**Debrief questions:**

1. "Which stage was hardest? What made it difficult?"
2. "What did you change between your first 0402 and your last 0603?" — Looking for: "I added more flux / checked the tip more often / slowed down."
3. "On the SOIC-8 — how many pins had bridges after your first drag pass?" — Normalise this: bridges on first pass are expected; fixing them is the skill.
4. "When you removed the 0603 with braid, what did the pad look like? Did the colour change when solder was absorbed into the braid?"

**Key message to close:**

"Soldering is a skill that degrades without practice. The technicians who produce reliable repairs solder something every week, even if it is just a practice board. What you did today is the baseline. Tomorrow you will add hot air, larger packages, and more complexity. Everything you practised today transfers directly."

---

## Notes for Instructor

- The 0402 stage is deliberately humbling. Students who underestimate SMD work will discover it here. Use this to motivate, not discourage — acknowledge that 0402 work is genuinely difficult for anyone without regular practice.
- If a student is significantly behind — has not completed Stage 3 by the 50-minute mark — offer focused individual attention. The SOIC-8 stage is non-negotiable; it cannot be skipped.
- Students who finish early: direct them to re-solder a fresh 0402 with the opposite hand (ambidextrous practice) or attempt an SOIC-16 footprint if available on the practice board.
- Practice PCBs should be numbered and retained by the instructor after session for sign-off records. Students do not keep their PCBs until the final sign-off is complete.
- The desoldering braid exercise in Stage 6 is a skills prerequisite for SESSION-08H. Every student must complete it.
