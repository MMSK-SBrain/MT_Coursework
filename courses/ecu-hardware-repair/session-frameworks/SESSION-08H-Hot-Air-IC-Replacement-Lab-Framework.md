# SESSION-08H — Hot Air QFP Removal & Replacement Lab
## ECU Hardware Repair (ECUHR) | Module 4: PCB Repair & Soldering Skills
### Day 8 — Hands-On Block | Duration: 90 minutes

---

## Session Identity

| Field | Detail |
|---|---|
| Session Code | SESSION-08H |
| Module | 4 — PCB Repair & Soldering Skills |
| Day | 8 |
| Block | Hands-On |
| Duration | 90 minutes |
| Delivery Mode | Workshop — individual bench stations |
| Prerequisites | SESSION-08T complete; students have completed SOIC-8 drag soldering in SESSION-07H |

---

## Learning Outcomes

By the end of this session, students will be able to:

- **so-4-2-2:** Remove a QFP IC from a practice PCB using a hot air rework station with correct settings, without lifting pads or damaging adjacent components
- **so-4-2-3:** Align a replacement QFP IC onto cleaned pads and solder it using drag soldering technique; all pins soldered with correct fillets, no bridges, no misalignment

---

## Equipment List — Per Student Station

| Item | Quantity | Notes |
|---|---|---|
| Hot air rework station | 1 | Hakko FR-301, Quick 861DW, or equivalent |
| QFP nozzle — matched to practice PCB IC body | 1 | Pre-selected to match QFP-44 or QFP-64 used on practice boards |
| Temperature-controlled soldering iron | 1 | For drag soldering phase |
| Chisel tip 2mm (for drag soldering) | 1 | Fitted and tinned |
| Practice PCB with QFP IC pre-installed | 1 | QFP-44 or QFP-64 — pre-soldered to pads, instructor-verified |
| Replacement QFP IC (same package) | 1 | Clean, undamaged, matching footprint |
| Solder — Sn63/Pb37 0.6mm | 1 reel | For rework and drag soldering |
| No-clean flux pen | 1 | |
| Liquid flux in syringe | 1 | Optional — for heavy flux application on QFP pins |
| Desoldering braid 2.5mm | 1 roll | For pad cleaning after removal |
| Kapton high-temperature tape | 1 strip pre-cut | For adjacent component shielding |
| Reverse-action tweezers | 1 pair | For IC placement |
| Fine-point tweezers | 1 pair | For pin alignment inspection |
| Fine dental pick or IC alignment tool | 1 | For pin straightening and IC positioning |
| USB microscope or magnifying loupe (10x minimum) | 1 | Shared between 2 students if necessary |
| IPA dropper bottle | 1 | For post-solder cleaning |
| Cotton swabs | 5 | For IPA cleaning |
| Safety glasses | 1 pair | Mandatory |
| Fume extractor | 1 | Running before session starts |
| Tip cleaner — brass wool | 1 | At every station |
| Multimeter | 1 | For continuity check during sign-off |

### Instructor Equipment
- Instructor station with overhead camera mirroring to room display
- 2 spare practice PCBs per 10 students (for pad damage recovery)
- Reference PCB: one fully completed QFP replacement, labelled for comparison
- Printed QFP pin-count reference for the specific IC used (or photograph with pin numbers marked)
- Kapton tape roll and aluminium foil — instructor supply

---

## Safety Notes

- Safety glasses mandatory from iron or hot air station switch-on. No exceptions.
- Hot air nozzle exits at 330–360°C. The nozzle must never be pointed at a person, at the bench surface, or at flammable materials (solder reels, IPA bottles). Return the handpiece to its holder between uses — the nozzle retains heat for several minutes after switch-off.
- IPA is flammable. The hot air station must be switched off before IPA is applied to the board. Do not apply IPA to a board that is still warm from hot air work — wait 60 seconds minimum.
- Lead-containing solder in use. Wash hands before leaving.
- Kapton tape and aluminium foil used for shielding must be removed from the board before post-session storage — residual adhesive can cause problems on subsequent use.

---

## Instructor Demonstration — Before Students Begin (20 minutes)

This demonstration is the most critical preparation for this session. The QFP removal phase is irreversible — pad damage cannot be undone. Every student must see the full removal-to-replacement cycle before touching their own board. Do not allow any student to begin until the full demonstration is complete.

### Demo Sequence

**Demo 1: Station setup and nozzle selection (3 minutes)**

"I'm setting up the hot air station exactly as we discussed in the theory session. I'm attaching the QFP nozzle — matched to the IC body size on this PCB, not the overall footprint. I'm setting temperature to 350°C and airflow to 3. I will not switch on until the board is prepared."

Show students the nozzle fitting onto the handpiece. Hold it over the QFP on the demo PCB — do not switch on yet — to demonstrate correct nozzle-to-board height (8mm above pins).

---

**Demo 2: Adjacent component assessment and shielding (2 minutes)**

"Before anything is switched on, I look at what is within 10mm of this QFP. I can see two 0603 resistors on the left side. I'm applying Kapton tape over them. I'm not covering any pads I need to access — only the components at risk."

Apply tape live. "On the right side I see a connector with a plastic housing — plastic melts at these temperatures. I'm applying a strip of aluminium foil to deflect heat."

---

**Demo 3: Flux application (1 minute)**

"Flux before heat. I'm applying the flux pen around all four pin rows of the QFP. Generous application — the flux will activate as soon as the air hits it."

---

**Demo 4: QFP removal (5 minutes)**

"Iron goes off — I only need the hot air station for this phase."

Switch on hot air station. Wait 5 seconds for temperature to stabilise.

Under overhead camera:

1. "I'm holding the nozzle 8 millimetres above the IC. I'm starting circular motion — slow, covering the entire package."
2. "I'm watching the flux. When it starts to bubble and smoke, the board is approaching solder melting temperature."
3. "About 25 seconds in — I'm testing the corner with my tweezers. Gentle pressure. It moved — the solder is liquid."
4. "I'm lifting the IC straight up. No rotation, no tilting. Straight lift, light force." Lift IC from board.
5. "Switch off hot air immediately. Set it down in its holder."

Show the empty PCB under camera. "The pads are tin-covered and intact. No copper lifting. That is the correct result."

Show the removed IC. "Count the pins — all 44 present and uncrimped. We could reball this IC if it were functional."

---

**Demo 5: Pad cleaning (3 minutes)**

"Now I need to clean the pads. I'm using desoldering braid — same technique as yesterday, but now I have 44 pads to clear rather than 2."

1. Apply fresh flux to all pad rows.
2. Cut fresh braid for each row — do not re-use saturated sections.
3. Work along each row: braid on pads, iron on braid, observe wicking, move along.
4. "I'm not pressing hard. I'm letting the heat do the work. Pressing hard risks pad lift."
5. Inspect pads under camera after each row. "Clean copper, flat, no solder mounding."
6. "One row at a time. This takes 3 to 4 minutes. Do not rush the pad cleaning. If you install a QFP on dirty pads, you will have shorts before you've even applied the iron."

---

**Demo 6: QFP alignment and placement (3 minutes)**

"Before I place the replacement IC, I'm looking at it under magnification. I want to confirm every pin is straight and none are bent inward. If a pin is bent, I use the dental pick to straighten it now — not after placement."

Show IC inspection under camera. Demonstrate straightening one slightly bent pin with the dental pick.

"Now placement. I'm using reverse-action tweezers. The IC sits between the tips. I'm aligning pin 1 — marked by a dot on the IC body and a marker on the PCB. The pins must sit on the pads, not inside the pad area or overhanging the outside edge."

Place IC on clean pads under camera. Inspect alignment. "I'm looking at all four corners. All pins are sitting on pads. Now I tack — two diagonal corners, minimum solder, just enough to fix the IC in place."

---

**Demo 7: Drag soldering the QFP (3 minutes)**

"Iron back on. Chisel tip, tinned. Same technique as the SOIC-8 yesterday — scaled up.

I'm applying flux along the first row of pins. Generous. Entire row before I touch the iron.

I'm loading a small reservoir of solder onto the chisel tip. The tip should look silvered and loaded — not dripping.

One slow drag from pin 1 to the last pin. I'm barely touching the pin tips — 45 degrees to the row, slow and steady."

Execute one side of drag soldering under camera. "I have two bridges. Expected. I'm applying flux directly to the bridges and drawing the tip slowly away. Watch the solder follow the tip."

Inspect under camera. "Every pin has a fillet. No bridges. I'll repeat this on the remaining three sides — I won't do all four live, but you have seen the technique."

"Total drag soldering time for a QFP-64: typically 8 to 12 minutes including bridge fixing and inspection. Do not rush."

---

## Student Practical — Step-by-Step Procedure

### Stage 1: Station Setup and Board Preparation (10 minutes)

All students:

1. Attach QFP nozzle to hot air station handpiece.
2. Set temperature to 350°C (lead-free joints on practice PCB) or 330°C (if instructor confirms leaded).
3. Set airflow to 3.
4. Do NOT switch on yet.
5. Examine the PCB. Identify all components within 10mm of the target QFP.
6. Apply Kapton tape over any adjacent SMD passives within the risk radius.
7. Apply aluminium foil over any plastic connectors or headers within the risk radius.
8. Apply flux pen generously around all four QFP pin rows.
9. Confirm iron is off. Hot air station only for the removal phase.

**Instructor circulation:** Check every station before any student switches on the hot air station. Verify: correct nozzle, correct temperature, correct airflow, shielding in place, flux applied. Do not allow a student to proceed without this check.

---

### Stage 2: QFP Removal (10 minutes)

1. Switch on hot air station. Wait 5 seconds.
2. Hold nozzle 8mm above IC. Begin slow circular motion.
3. Watch for flux to bubble and begin to smoke — this indicates approaching reflow temperature.
4. After approximately 20–30 seconds, gently probe one corner of the IC with fine tweezers.
5. If the IC moves freely: it is ready. If there is resistance: continue heating for 5–10 more seconds.
6. Lift IC straight up — no rotation, no tilting. Light force only.
7. Set IC aside on heat mat or IPA wipe.
8. Switch off hot air station immediately. Return handpiece to holder.
9. Do not touch the PCB for 30 seconds — it is hot.

**Instructor intervention triggers:**
- Student applies downward pressure to IC before probe test → Stop immediately: "Check the probe test first. Force before liquid solder lifts the pad."
- Student does not perform circular motion — holds nozzle stationary → "Keep it moving — stationary heat will damage the centre of the package and leave the outer pins cold."
- Student switches off hot air but leaves handpiece resting on bench surface → Instruct to return to holder.

---

### Stage 3: Pad Cleaning (10 minutes)

1. Wait 60 seconds for board to cool before touching.
2. Inspect pads under loupe. Note any solder mounding, any residue.
3. Apply fresh flux to all four pad rows.
4. Cut fresh desoldering braid — 25mm sections per row.
5. Work one row at a time: braid on pads, iron on braid (not directly on pads), heat until wicking occurs, move braid along row.
6. Move to fresh braid section when current section is saturated.
7. After each row: inspect under loupe. Pads should show clean copper, flat surface.
8. Repeat for all four rows.
9. Clean pad area with IPA on cotton swab. Allow to dry completely before proceeding.
10. Call instructor for Stage 3 sign-off before placing replacement IC.

**Common mistakes at this stage:**
- Reusing saturated braid — braid is full, nothing to wick, instructor will see pad is not clearing.
- Pressing iron directly on pads rather than through braid — increased pad lift risk. "The braid is between the iron and the pad. Always."
- Rushing: applying the replacement IC before pads are fully clean — results in buried bridges and shorts that are very difficult to diagnose later.

---

### Stage 4: Replacement QFP Inspection and Alignment (8 minutes)

1. Pick up replacement QFP with reverse-action tweezers. Do not touch the pin area.
2. Inspect every pin under loupe before placement. Look for: bent pins, foreign material between pins, any corrosion.
3. Straighten any bent pins with fine dental pick before placement.
4. Place IC on pads — align pin 1 marker on IC body to pin 1 marker on PCB.
5. View from all four corners under loupe before any soldering. All pins must be sitting on their corresponding pads.
6. If misaligned: reposition with the dental pick or tweezers — no heat yet.
7. When alignment is confirmed: tack pin 1 with minimum solder.
8. Check alignment again. Tack the diagonal corner pin.
9. Inspect all four pin rows: IC should be flat, not rocking, all pins on pads.
10. Call instructor to confirm alignment before soldering begins.

**Instructor alignment check:** The instructor must inspect every student's IC alignment before drag soldering begins. A misaligned QFP that is fully soldered requires full removal and restart. This check saves significant time.

---

### Stage 5: Drag Soldering — All Four Sides (25 minutes)

Allow 25 minutes for this stage. Students who rush produce bridges that require extra correction time. Methodical pace is faster than fast pace.

For each of the four sides:

1. Apply flux pen along the entire pin row.
2. Re-tin the iron tip (brass wool + touch to solder).
3. Load a small solder reservoir onto the chisel tip (tip should look loaded — not dripping).
4. Position tip at approximately 45 degrees to the pin row.
5. Place tip at the first pin. Begin a slow, steady drag toward the last pin. Total drag time: 3–5 seconds per side. Do not rush.
6. Withdraw tip.
7. Inspect under loupe immediately. Count the pins — every pin must have a visible fillet.
8. Identify any bridges.
9. Fix bridges: apply flux directly to bridge, draw tip toward the bridge from the side and slowly away. The bridge will follow the tip.
10. Re-inspect every pin after bridge fixing.
11. When the row is clean: move to the next side.
12. Do not move to the next side until the current side passes inspection.

After all four sides:
13. Final inspection under maximum available magnification — inspect every pin individually.
14. Perform continuity check (see Stage 6).

**Common mistakes at this stage:**
- Pressing the iron tip into the pin row from above rather than dragging across — creates mechanical stress on pins and pushes IC.
- Moving too fast — the solder loaded on the tip has not had time to flow to each pin. Result: some pins have solder, others do not.
- Skipping flux between sides — the flux from the last side has burned off. Each new side needs fresh flux.
- Not counting pins after each side — a missed pin at pin 12 of 16 is invisible at a glance and will be an open circuit.

---

### Stage 6: Continuity Check and Sign-Off (7 minutes)

**Continuity check — performed by student, verified by instructor:**

Using a multimeter in continuity mode:

1. Check pin 1 to its corresponding trace (or a visible component known to connect to the same net). Should beep (continuity).
2. Check each adjacent pin pair for absence of bridging. Probe pin 1 and pin 2 — should NOT beep. Probe pin 2 and pin 3 — should NOT beep. Continue along each row.
3. Report any beeps between adjacent pins — these are bridges. Return to drag solder correction if found.

**Call instructor for final Stage 5/6 sign-off.**

---

## Student Sign-Off Checklist

The instructor signs off each stage. Students may not proceed to the next stage without sign-off.

### Stage 2 — QFP Removal
- [ ] IC removed without pad lift on any of the four rows
- [ ] No adjacent component damage visible
- [ ] Hot air station returned to holder correctly
- [ ] No mechanical force was used (confirmed by inspection — pads intact)

### Stage 3 — Pad Cleaning
- [ ] All four pad rows clean — copper visible, no solder mounding
- [ ] Pads flat with no surface irregularities
- [ ] No pad discolouration from overheating
- [ ] IPA clean applied and dried

### Stage 4 — IC Alignment
- [ ] All pins sitting on corresponding pads
- [ ] IC flat, not rocking
- [ ] Pin 1 aligned to board marker
- [ ] No bent pins visible
- [ ] Instructor has confirmed alignment before soldering

### Stage 5/6 — Drag Soldering and Continuity
- [ ] All pins on all four sides have individual visible fillets
- [ ] No bridges remaining between any adjacent pins
- [ ] No cold joints (dull, grainy surface)
- [ ] IC is flat against PCB — no lifted side
- [ ] Continuity check: all tested pins connect to correct net
- [ ] Continuity check: no short between adjacent pin pairs

**Instructor sign-off:** ___________________ Date: ____________

---

## Common Mistakes Reference — Instructor Quick Guide

| Defect | Root Cause | In-Session Fix |
|---|---|---|
| Pad lift during removal | Pulling IC before solder fully liquid | Cannot fully undo — document. For pads with traces: wire jumper. For power/ground pads: may be non-critical. |
| IC misaligned before soldering | Not checking alignment under magnification before tacking | Remove tack pins, reposition, re-tack. Recheck before drag. |
| Bridges on QFP pins | Insufficient flux, tip overloaded with solder, dragging too fast | Flux + draw tip. If bridge persists: braid on individual bridge. |
| Missing fillet on one pin | Tip moved too fast past that pin | Flux + touch tip to pin and pad for 1 second. |
| IC not sitting flat — corner raised | Tack on one side only, other side not reflowed | Reflow the raised corner with iron — light touch, small amount of solder. |
| Adjacent component shifted | Insufficient shielding, airflow too high | Reposition component with iron — treat as a standard iron rework. |
| Cold joint after drag | Tip temperature dropped, no re-tinning between sides | Flux + reflow the cold side. Re-tin tip before retry. |

---

## Debrief — Last 10 Minutes

Instructor brings the group together at the front bench.

Show one strong result and one result with a fixable defect, without naming students.

**Debrief questions:**

1. "When did you know the solder was liquid during removal? What was your indicator?"
2. "How many bridges did you have on your first drag pass? How did you fix them?" — Normalise: "Two to four bridges on a first pass is normal. Eight or more suggests the tip was overloaded."
3. "If a pad had lifted during removal — what would you do?" — Expected: assess whether the trace can be accessed, plan a wire jumper, document.
4. "What is the single thing you would do differently on your next QFP removal?"

**Key message to close:**

"You have now completed the two hardest practical operations in this course. Every other repair operation on an ECU is a variation of what you did today and yesterday — smaller, simpler, or more specific. Tomorrow is about understanding the ICs themselves and building something that works. Today was the craft. Tomorrow is the engineering."

---

## Notes for Instructor

- The 20-minute instructor demonstration is non-negotiable. Students who have not seen a full removal-to-replacement cycle before attempting their own make significantly more errors. Pressure to shorten the demo to give students more bench time should be resisted.
- The alignment check in Stage 4 is an instructor-mandatory checkpoint. Every student's IC alignment must be confirmed before drag soldering begins. A misaligned IC that has been fully drag-soldered requires full removal with hot air, pad cleaning again, and restart — this costs 20 minutes minimum.
- If a student lifts a pad during removal: keep the PCB and show the group at debrief. Pad lift is the most important consequence to understand. A real example is more instructive than any photograph.
- If a student runs significantly behind: they must at minimum complete Stage 2 and Stage 3 (removal and pad cleaning) to have completed the primary learning outcome. The replacement and soldering can, if necessary, be completed at the start of Day 9 before SESSION-09T, but this is a last resort.
- Practice PCBs for this session should be numbered and retained for sign-off records. Photos of completed QFP placements are useful for the student's portfolio record.
