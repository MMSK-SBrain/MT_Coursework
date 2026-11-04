# SESSION-12H: Environmental Damage Assessment & Fault Case Studies
## Workshop Framework for Instructor and Students (+ Mid-Module Practical Assessment)

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 5 — ECU On-Table Diagnostics
**Day:** 12 | **Session Type:** Hands-On Workshop + Mid-Module Assessment
**Duration:** 90 minutes
**Format:** Instructor Briefing → Activity 1: Environmental Assessment → Activity 2: Independent Case Study (ASSESSED) → Brief Debrief

**Session Outcomes Addressed:**
- so-5-4-2: Assess corrosion severity on PCB traces and connector pins and classify as: cleanable, repairable, or beyond economic repair | Evaluate
- so-5-4-3: Clean a moisture-damaged ECU PCB using isopropyl alcohol and correct tools, then inspect under magnification | Apply
- so-5-4-4: Diagnose an ECU with a planted fault (component failure, power stage, trace, or moisture) and document findings | Analyze

**CO Alignment:** co-1

**Assessment Note:** The second half of this session (Activity 2) constitutes the Mid-Course Practical Assessment for Module 5. It is worth 20% of the total course grade. Students work independently without instructor assistance. Assessment forms are collected at the end of the session.

---

## OVERVIEW AND INTENT

Session 12H is the culminating practical session for Module 5. It has two distinct parts:

**Activity 1 — Environmental Damage Assessment and Cleaning (35 minutes):** Students apply the severity classification framework from 12T to a real moisture-damaged donor ECU. They identify the ingress point, classify the damage level, conduct the cleaning procedure on boards classified as Level 1–2, and perform post-cleaning verification. This is guided practice.

**Activity 2 — Independent Fault Case Study (45 minutes):** Students independently diagnose an ECU with a single planted fault — no instructor assistance. This draws on all diagnostic skills from Days 10, 11, and 12. The findings are documented on an assessment form which constitutes the Mid-Module Practical Assessment submission. This is independent assessed work.

The session concludes with a 10-minute group debrief. Assessment forms are collected before the debrief begins — findings are not discussed until all forms are submitted.

---

## EQUIPMENT LIST (All Items — Per Bench Station)

### Activity 1 — Environmental Assessment and Cleaning:

| Item | Specification | Notes |
|---|---|---|
| Moisture-damaged donor ECU | Real water-damaged unit from salvage — NOT a planted fault ECU | Sourced from salvage dealer; at least 2–3 different boards at different severity levels |
| IPA 99% | Isopropyl alcohol, 99% purity | NOT 70% — explicitly confirmed |
| Soft-bristle brushes | PCB cleaning brush + fine artist's brush (sizes 4–6) | Natural bristle — nylon also acceptable |
| Bamboo sticks | Pointed/tapered — for dendrite removal | Supplier: craft or art supply |
| Cotton swabs | Plain cotton — no synthetic fill | |
| UV lamp | 365nm (UV-A) LED torch or bench lamp | For conformal coating inspection |
| Magnification loupe | 10x–20x | Or stand-mounted magnifier |
| Microscope (optional) | Digital USB microscope, 40–200x | Where available; greatly assists L2–L3 assessment |
| Air bulb | Soft rubber squeeze bulb | For drying — NOT compressed air (too high pressure for damp PCB) |
| Low-temperature oven or heat gun (low) | 50°C for drying | Do not exceed 60°C |
| Anti-static mat | 1 per bench | |
| ESD wrist strap | 1 per student | |
| Assessment worksheet — Activity 1 | 1 per student pair | Template at end of this document |
| Severity classification reference card | Laminated A5 — from Session 12T Slide 21 | Posted at each bench |
| Multimeter | For post-cleaning continuity and resistance tests | |

### Activity 2 — Independent Case Study (Mid-Module Assessment):

| Item | Specification | Notes |
|---|---|---|
| Assessment ECU | Pre-planted fault ECU — different from Day 10/11 ECUs | Each bench has different fault type; see Fault Preparation |
| Wiring diagram | For the assessment ECU | Printed A3 |
| PCB schematic (signal path) | For the assessment ECU | Printed A3 |
| Bench power supply | Pre-configured 12.5V | Students must set current limit before use |
| Bench wiring harness | Fabricated for assessment ECU connector | |
| Scan tool | Same as Days 10–11 | |
| Oscilloscope | 2-channel, 50MHz+ | |
| Multimeter | Autoranging | |
| ESR meter | For capacitor testing if relevant | |
| Assessment form | 1 per student — individual submission | Template at end of this document |
| Anti-static mat and ESD strap | 1 per bench / 1 per student | |

### Safety Items — Activity 1 Specific:

| Item | Purpose |
|---|---|
| Chemical-resistant gloves | IPA exposure — not strictly required for brief contact but recommended for prolonged cleaning |
| Ventilation | IPA vapour accumulates — ensure workshop ventilation is active |
| No naked flames — posted notice | IPA flammable — fire source exclusion zone around cleaning area |
| IPA-rated fire extinguisher | CO2 or dry powder — confirm on site |
| IPA disposal container | Used IPA is chemical waste — collect and dispose per local regulation |

---

## INSTRUCTOR PRE-PREPARATION

### Activity 1 — Donor ECU Preparation:

Source moisture-damaged donor ECUs from automotive salvage dealers. Request units described as "water damaged" or "flood damaged." Aim for:
- 1 x Level 1 board per 2 benches (minor connector pin corrosion)
- 1 x Level 2 board per 2 benches (moderate trace corrosion + early dendrites)
- 1 x Level 3 board per 4 benches (severe — for inspection only, not cleaning in this session)

Inspect all boards under UV light before the session. Prepare the instructor classification record for each board (what you assess it to be) — share with students only after they submit their independent classification.

### Activity 2 — Planted Fault Preparation:

Prepare assessment ECUs with one fault each. Fault types for this session include a broader range than Day 11 (which was specifically PCB signal path). Assessment ECUs should have faults from:

**Fault Type A — Component failure on power stage:**
Short failed MOSFET in a low-side driver output (drain-source short). Effect: driver output stuck low; any actuator connected to this driver will appear continuously activated. DTC: output circuit fault — voltage out of range or stuck.

**Fault Type B — Open-circuit PCB trace:**
Scribed trace in a sensor input signal path (same method as Day 11 Option D). Students should apply the line tracking skills from Day 11. Effect: sensor reads default/extreme value. DTC: signal circuit low or high.

**Fault Type C — Shorted bypass capacitor:**
Deliberate solder bridge to ground on a bypass capacitor in the sensor input path. Effect: sensor signal attenuated toward 0V. This produces a reduced-amplitude signal rather than complete absence — requires oscilloscope interpretation, not just presence/absence detection. DTC: signal circuit low.

**Fault Type D — Moisture damage with dendritic short:**
A donor board with Level 2 moisture damage that has been allowed to progress to the point of a dendritic bridge between two adjacent signal-line traces. Effect: cross-talk or fixed offset on one of the bridged signals. Identifiable by visual inspection under magnification after power-off. DTC: may show signal-range fault on the affected channel.

**Distribution:** Assign fault types A, B, C, D across benches so adjacent benches have different fault types. Students should not be able to share answers from a neighbouring bench.

### Assessment Form Preparation:

Print one assessment form per student — individual, not per pair. Confirm forms have no fault hints — no section names that reveal the fault category. The form should guide documentation of findings only.

---

## ACTIVITY STRUCTURE

| Phase | Duration | Activity |
|---|---|---|
| Instructor briefing | 7 min | Safety rules, activity overview, assessment instructions |
| Activity 1: Environmental assessment | 35 min | Ingress point identification, classification, cleaning, verification |
| Transition and assessment setup | 3 min | Forms distributed, assessment equipment confirmed |
| Activity 2: Independent case study | 45 min | Unseen ECU — independent diagnosis and documentation |
| Debrief | 10 min | Forms collected first; group share of approaches; preview of Module 6 |

---

## INSTRUCTOR BRIEFING (7 minutes)

**Deliver at front with all students present before they access bench stations.**

> "Today closes Module 5. Two activities — different character, different rules.
>
> Activity 1: Environmental damage assessment and cleaning. You'll receive a real water-damaged board. You'll assess it, classify the severity level, conduct the cleaning procedure if appropriate, and verify the result. I'm here, you can ask questions, and I'll check your classifications before you start cleaning. Work together on this one.
>
> Activity 2: This is assessed. You'll receive an ECU with a planted fault. You do not know what the fault is. You do not know which circuit. You start from scratch — scan it, trace it, find it, document it. I observe and do not assist. No comparison with other benches — each bench has a different fault. Phones away during the assessment. Assessment forms go to me before we debrief.
>
> Safety for Activity 1: IPA is flammable. No naked flames anywhere near the cleaning area. Ventilation is active. Gloves available. All used IPA goes in the waste collection container — not poured down the sink. Boards do not get powered after cleaning until they are fully dry."

---

## ACTIVITY 1: ENVIRONMENTAL DAMAGE ASSESSMENT AND CLEANING (35 minutes)

### Phase A: Initial Assessment (12 minutes)

**Step 1 — External inspection:**
Before disassembly, inspect the ECU housing exterior:
- Identify the connector assembly location
- Look for external water staining, mud contamination, corrosion on housing exterior
- Note the housing condition (intact, cracked, impact damage, connector retainer condition)
- Record observations in Section 1 of the Activity 1 worksheet

**Step 2 — Connector inspection:**
- Examine the connector face seal: intact? Compressed? Missing?
- Examine individual wire seals around each wire entry: cracked? Absent? Water marks on seal surface?
- Note which area of the connector shows the most significant external corrosion — this identifies the likely ingress zone
- Record: "Probable ingress point: [connector seal area / specific wire seal position / other]"

**Step 3 — PCB inspection (UV light first, then visual):**
Open the ECU housing (instructor demonstrates case opening technique on the bench type in use if needed).

UV inspection first:
- Hold UV lamp above open ECU, scan entire PCB surface
- Areas with intact conformal coating: fluoresce clearly
- Areas with damaged/absent coating: appear dark
- Note and record which areas show coating damage

Visual inspection under magnification:
- Scan from the suspected ingress point outward
- Note: connector pin condition, trace condition, component lead condition, any visible dendritic growth
- Photograph with phone camera under good lighting for the worksheet record

**Step 4 — Severity classification:**
Complete the classification worksheet:
- For each criterion in the Level 1–4 table: state whether it is present (YES/NO/PARTIALLY)
- Based on all observed criteria: assign severity level (1, 2, 3, or 4)
- Write the specific observations that led to this classification

**Checkpoint A: Show classification to instructor before beginning cleaning. Instructor confirms classification or identifies misclassification with specific reasoning. Level 3 and Level 4 boards do not proceed to cleaning in this activity — assessment and documentation only.**

### Phase B: Cleaning Procedure (Level 1–2 boards only) (15 minutes)

**Safety checks before starting:**
- Confirm IPA bottle is 99% purity — check label
- Confirm ventilation is active
- Confirm no ignition sources (soldering irons off, no spark hazard in vicinity)
- Gloves on

**Step 5 — Conformal coating removal in affected areas (if applicable):**
- Identify areas requiring coating removal using UV map
- For acrylic coating: apply IPA with brush, allow 2–3 minutes to soften, remove with soft brush
- Confirm removal under UV light — area should lose fluorescence
- For polyurethane: note it as "polyurethane — specialist remover required." Do not attempt removal with IPA alone in this session.

**Step 6 — First IPA wash:**
- Apply 99% IPA to the affected area using soft-bristle brush
- Work in circular motion — 60 seconds per area
- Do not flood the board — controlled application
- Tilt board gently to allow dissolved contaminants to run toward a corner away from components

**Step 7 — Dendrite removal (Level 2 boards — if dendrites present):**
- Under magnification loupe, identify dendritic growth between traces
- Using bamboo stick: press tip gently onto dendrite filaments, dislodging them from trace surfaces
- Use air bulb to remove dislodged particles — blow away from components
- Confirm removal under magnification — visual confirmation only (do not measure resistance during cleaning, board is wet)

**Step 8 — Second IPA wash:**
- Repeat Step 6 — final wash to remove loosened contaminants from Step 7

**Step 9 — Drying:**
- Air bulb: gentle airflow across board surface to remove pooled IPA
- Place in low-temperature oven (50°C) for 20 minutes, OR
- Air dry at room temperature for minimum 30 minutes
- Do not apply power until instructor confirms dryness

**Step 10 — Post-cleaning inspection:**
Under magnification and UV light:
- Confirm dendrites removed
- Confirm no visible residue deposits
- Confirm all cleaned areas are free of ionic residue (no white/crystalline deposits visible)

### Phase C: Post-Cleaning Verification (8 minutes)

**Step 11 — Continuity test (Level 2 boards):**
Using multimeter in continuity mode:
- Test continuity across the five longest traces in the affected area
- Test from pad to pad along the trace — any open circuit indicates a trace that corrosion has severed
- Record each test result in the worksheet

**Step 12 — Connector pin resistance:**
Using multimeter in resistance mode:
- Measure resistance from ECU connector pin to the corresponding ECU-side harness pin through the connector (if bench harness is available and the donor board is testable)
- Record: expected < 0.1Ω per contact
- If above 0.3Ω: note as "high-resistance contact — may need further cleaning or abrasion"

**Step 13 — Insulation resistance check (Level 2 only):**
Using multimeter in high-range resistance mode:
- Measure between adjacent conductors in the previously corrosion-affected area
- Expected: > 1MΩ between any two conductors not intended to be connected
- Values below 1MΩ: potential residual contaminant bridge — note location for additional cleaning cycle

**Checkpoint B: Present completed Activity 1 worksheet to instructor. Instructor confirms classification, cleaning procedure observation, and post-cleaning verification results. This is the practical sign-off for so-5-4-2 and so-5-4-3.**

---

## TRANSITION: ACTIVITY 2 SETUP (3 minutes)

**Instructor delivers assessment briefing while students set up their bench ECU:**

> "Activity 1 worksheets stay at the bench — you'll keep them. Assessment forms for Activity 2 are being distributed now — one per student, not per pair. This is individual work. You may consult your worksheets and reference cards from previous sessions. You may not consult other students.
>
> Your assessment ECU is at your bench. It has one fault. Everything you need to diagnose it — wiring diagram, PCB schematic, scan tool, oscilloscope, multimeter — is available. You have 45 minutes. At the 40-minute mark I will give a five-minute warning. At 45 minutes, assessment forms are collected before anything else happens.
>
> Begin."

---

## ACTIVITY 2: INDEPENDENT FAULT CASE STUDY (45 minutes)

### Assessment Instructions for Students:

This section of the session is the Mid-Module Practical Assessment. Work independently. The assessment form documents your findings.

**The diagnostic task:**
You have an ECU with one planted fault. Using the skills and procedures from Days 10, 11, and 12 of Module 5, you must:
1. Set up the bench correctly and establish scan tool communication
2. Read and classify all DTCs
3. Read live data and identify any anomalous values
4. Trace the fault using line tracking and/or environmental assessment
5. Identify the fault, the component or location, and document your findings

**What to document on the assessment form:**
- Bench setup steps completed and current draw recorded
- DTC(s) found with status classification
- Live data anomalies identified
- Diagnostic approach: the sequence of steps you followed and why
- Fault evidence: specific measurements taken, oscilloscope results captured, classifications made
- Fault conclusion: what failed, where it is, what caused it
- Recommended repair: the specific action needed to restore function
- Estimated cause: what do you believe led to this fault (age, moisture, overload, etc.)

### Instructor's Role During Activity 2:

**Observe without assisting.** Circulate continuously. Make notes on each student's approach for your assessment record.

**Note in your assessment record:**
- Whether student reads wiring diagram before connecting wires
- Whether current limit is set before power applied
- Whether student reads DTC status (not just code)
- Whether line tracking approach is methodical or random
- Whether oscilloscope is used for signal lines or only multimeter
- Whether split-half method is applied to PCB path
- Whether fault confirmation measurement is taken before stating conclusion

**Permitted interventions (equipment/safety only):**
- Safety hazard: intervene immediately
- Equipment failure: assist in resolving
- Scope setup error (floating ground, wrong coupling): indicate there is a setup problem, do not specify what it is

**Not permitted:**
- Telling students which circuit the DTC points to
- Telling students to check a specific component
- Confirming whether a student's hypothesis is correct before they make a confirmation measurement

**Timing:**
- 10 minutes: all students should have communication established and DTCs read
- 25 minutes: all students should be in the active fault-tracing phase (line tracking or component testing or environmental inspection)
- 40 minutes: five-minute warning — state aloud: "Five minutes. Ensure your fault conclusion and recommended repair sections are completed. Assessment forms collected in five minutes."
- 45 minutes: "Stop work. Assessment forms to me now, then remain at your bench."

---

## ASSESSMENT RUBRIC — MID-MODULE PRACTICAL (20% of Course Grade)

The assessment form is scored against five competency areas:

### 1. Bench Setup and Communication (10 marks)

| Criterion | Full marks | Partial marks | No marks |
|---|---|---|---|
| Wiring diagram consulted before wiring (documented) | 4 | Evidence of consultation but not documented | No diagram evidence |
| Current limit set, current reading documented | 3 | Limit set but no reading recorded | No evidence of current limit |
| Communication established and protocol identified | 3 | Communication established but protocol not noted | No communication |

### 2. DTC Classification and Circuit Identification (20 marks)

| Criterion | Full marks | Partial marks | No marks |
|---|---|---|---|
| DTC status correctly classified (current/pending/etc.) | 8 | Classification attempted but incorrect | Not attempted |
| Circuit correctly identified from DTC | 7 | Circuit partially identified | Not identified |
| Live data anomaly identified with circuit interpretation | 5 | Anomaly noted without interpretation | Not addressed |

### 3. Diagnostic Approach — Process Quality (30 marks)

| Criterion | Full marks | Partial marks | No marks |
|---|---|---|---|
| Systematic approach documented — clear sequence of steps | 10 | Some steps documented, sequence unclear | Random — no documented approach |
| Oscilloscope used for signal lines (not multimeter only) | 10 | Oscilloscope used but setup or result not documented | Multimeter only on signal lines |
| Split-half or systematic component isolation applied | 10 | Some isolation applied but not systematic split-half | Component replaced/guessed without isolation |

### 4. Fault Identification and Evidence (30 marks)

| Criterion | Full marks | Partial marks | No marks |
|---|---|---|---|
| Correct fault location identified | 12 | Fault partially identified (correct circuit but wrong component) | Incorrect or not identified |
| Evidence quality — measurements documented | 10 | Some measurements documented | No measurements on form |
| Confirmation measurement taken (power-off if applicable) | 8 | Confirmation attempted but method incorrect | Not attempted |

### 5. Recommended Repair and Estimated Cause (10 marks)

| Criterion | Full marks | Partial marks | No marks |
|---|---|---|---|
| Repair correctly stated (component, method, verification step) | 6 | Repair partially stated — missing component spec or verification | Incorrect or not stated |
| Estimated cause plausible and consistent with evidence | 4 | Cause stated without linking to evidence | Not stated |

**Total: 100 marks. Pass threshold: 60 marks. Distinction: 85 marks.**

**Special condition for Fault Type D (moisture/dendritic):** The line tracking stage involves visual inspection under magnification in addition to or instead of oscilloscope probing. Students who correctly classify the fault as moisture-related and identify the dendritic growth as the specific fault mechanism receive full marks for sections 3 and 4 even if oscilloscope probing was limited — provided their visual inspection process is documented.

---

## DEBRIEF (10 minutes)

**Collect all assessment forms before beginning debrief. Confirm collection is complete.**

> "Forms are in. We're not discussing individual marks or whose fault was what — that's for individual feedback later. What I want from you now is process: what approach did you take, what worked, what didn't."

### Discussion Questions (2 minutes each):

1. "Did anyone find that the DTC immediately told them the fault type — or did the DTC send them in a direction that required further investigation?"
2. "How did your diagnostic approach today differ from Day 10, when you were doing this for the first time?"
3. "What was the hardest decision point — where did you most want to ask for help but didn't?"

### Instructor Closing Points:

> "Three things.
>
> First: Module 5 is the diagnostic module. Everything that follows in Modules 6 through 9 assumes you can do what we've done this week — set up a bench, scan an ECU, read the results, trace a fault, assess environmental damage, and document your findings. If any of that felt uncertain today, revisit the reference frameworks and the session worksheets before Module 6 starts.
>
> Second: the assessment form I've just collected is not graded on whether you found the fault. It's graded on how you approached finding it. A student who used the correct process and ran out of time before confirming the fault demonstrates more competency than a student who replaced parts at random and happened to fix it. This is the same standard that applies in professional practice.
>
> Third: Module 6 starts tomorrow with ECU programming. A completely different skill set — but it starts on the bench. You'll recognise the bench setup immediately. The ECU stays on the anti-static mat. The wiring diagram goes first."

---

## ACTIVITY 1 WORKSHEET TEMPLATE

*Print 1 per student pair. Both students contribute; one worksheet per pair.*

---

**Student Names:** _________________________ **Date:** _______________
**Donor ECU Identifier:** _________________________

---

**Section 1: External Inspection**
- ECU housing condition: _____________________________________________
- Connector face seal condition: _______________________________________
- Individual wire seal condition: _______________________________________
- External corrosion or water staining location: ___________________________
- Probable water ingress location (initial): _______________________________

---

**Section 2: UV Light and Visual PCB Inspection**
- Conformal coating condition: ________________________________________
- Areas of coating damage (describe location): ____________________________
- PCB trace corrosion visible: YES / NO — Location: ______________________
- Component lead corrosion visible: YES / NO — Which components: __________
- Dendritic growth visible under magnification: YES / NO — Location: __________
- Other observations: ________________________________________________

---

**Section 3: Severity Classification**

For each criterion, mark YES, NO, or PARTIAL:

| Criterion | Present? |
|---|---|
| Oxidation confined to connector pins only | |
| PCB trace corrosion visible | |
| Component lead oxidation visible | |
| Dendritic growth visible under magnification | |
| Conformal coating damaged in ingress area | |
| Open-circuit traces visible | |
| IC package lead heavy corrosion | |
| PCB delamination visible | |
| MCU or primary IC damage visible | |

**Classification: Level ________ (1 / 2 / 3 / 4)**

**Specific observations supporting this classification:**
_____________________________________________________________________________
_____________________________________________________________________________

**Instructor sign-off on classification:** _______________ Level confirmed: ______

---

**Section 4: Cleaning Procedure Record** *(Level 1–2 boards only)*

- Conformal coating type: Acrylic / Polyurethane / Silicone / Not present
- Coating removal performed: YES / NO — Method: _________________________
- First IPA wash: completed YES / NO
- Dendrites removed (if present): YES / NO — Method: ______________________
- Second IPA wash: completed YES / NO
- Drying method: Oven 50°C / Air dry / Air bulb — Time: _______ min

---

**Section 5: Post-Cleaning Verification**

Continuity tests across corroded traces:

| Trace Location | Result (continuity / open) |
|---|---|
| | |
| | |
| | |

Connector pin resistance measurements:

| Pin | Measured Resistance | Pass / Fail (< 0.1Ω pass) |
|---|---|---|
| | | |
| | | |

Insulation resistance between adjacent conductors (if tested):
- Location tested: _________ Measured value: ________ Ω — Pass / Fail (> 1MΩ pass)

**Post-cleaning assessment:**
Board condition after cleaning: ____________________________________________
Any traces requiring repair: _______________________________________________
Any pins requiring further abrasion: _________________________________________

---

## ACTIVITY 2 ASSESSMENT FORM

*Print 1 per student — INDIVIDUAL SUBMISSION. Do not share.*

---

**Student Name:** _________________________ **Date:** _______________
**Assessment ECU Identifier:** _________________________

*Note: This form is the submission for the Mid-Module Practical Assessment (20% course grade). Complete all sections. Write legibly. Attach oscilloscope screenshots if captured.*

---

**Section 1: Bench Setup (10 marks)**

Pins identified from wiring diagram before wiring:
- B+ pin(s): _____ | GND pin(s): _____ | KL15: _____ | CANH: _____ | CANL: _____

PSU settings: Voltage: _____ V | Current limit: _____ A

Current readings:
- At power-on (B+ only): _____ A
- After KL15 applied (settled): _____ A

Communication: Established YES / NO — Protocol detected: _____________________

---

**Section 2: DTC Classification and Circuit Identification (20 marks)**

| DTC Code | Status | Description | Circuit Implicated |
|---|---|---|---|
| | | | |
| | | | |

Live data anomalies:

| Parameter | Observed Value | Expected Value | Circuit Fault Interpretation |
|---|---|---|---|
| | | | |

---

**Section 3: Diagnostic Approach — Sequence of Steps (30 marks)**

Describe the sequence of steps you followed to diagnose this fault. Be specific — include what you measured, what you found, and what decision each measurement led to.

Step 1: ________________________________________________________________
Step 2: ________________________________________________________________
Step 3: ________________________________________________________________
Step 4: ________________________________________________________________
Step 5: ________________________________________________________________
Step 6: ________________________________________________________________
Step 7: ________________________________________________________________

*(Add rows as needed)*

---

**Section 4: Fault Identification and Evidence (30 marks)**

**Fault isolated to:**
- Circuit: _____
- PCB location / component reference: _____
- Fault type: Open circuit / Short circuit / Resistive fault / Moisture/corrosion / Component failure / Other: _____

**Evidence (describe each measurement or observation that supports this conclusion):**

| Evidence Item | Measurement/Observation | What It Confirms |
|---|---|---|
| | | |
| | | |
| | | |

**Confirmation measurement (power off if resistance/ESR):**
- Measurement type: Resistance / ESR / Diode test / Visual inspection
- Result: ___________
- Expected: ___________
- Fault confirmed: YES / NO

---

**Section 5: Recommended Repair and Estimated Cause (10 marks)**

**Recommended repair:**
_____________________________________________________________________________
_____________________________________________________________________________

Include: component specification, soldering/cleaning approach, post-repair verification step.

**Estimated cause of fault:**
_____________________________________________________________________________

What do you believe led to this fault? (Age-related component failure / Environmental moisture / Mechanical impact / Electrical overstress / Manufacturing defect / Other) — Justify with reference to your evidence.

---

*Assessment form collected by instructor before debrief. Do not retain a copy — the instructor copy is the assessed submission.*

---

*Module 5 | Day 12 Hands-On | ECUHR | v1.0 | 2026-02-18*
