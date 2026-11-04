# SESSION-04H: PCB Exploration Lab
## Hands-On Workshop Framework

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 3 — ECU Architecture, Protection & Filtering (Days 4–6)
**Session:** Day 4 — Hands-on
**Duration:** 90 minutes
**Format:** Structured workshop — individual work with instructor circulation
**Max Class Size:** 16 students (8 stations, 2 students per station, each student with their own ECU)

---

## Session Outcomes

| SO ID | Description | Bloom |
|-------|-------------|-------|
| so-3-1-2 | Locate and identify test points, reference designators, and component silkscreen markings on a real ECU PCB | Apply |

*Supporting outcomes from theory (04T) reinforced through practical application:*
- so-3-1-1: PCB layer awareness applied when identifying board construction features (via holes, top vs bottom layer traces)
- so-3-1-3: Processor region components identified and labelled during the mapping activity

---

## Workshop Overview

Students receive a dismantled ECU, a printed blank PCB map, and a reference card of component designator codes. Working individually (two students per station, each with their own ECU), they systematically identify and label every circuit region and component category visible on the board. The session ends with a peer-review swap and instructor debrief.

---

## Equipment and Materials List

### Per Station (2 students)
- 2 x real automotive ECU PCBs — conformal coat removed, fully dismantled from housing
  - Preferred: two *different* ECU types per station so students see that the methodology applies across manufacturers
  - Required: visible test points, readable silkscreen, exposed processor region
- 2 x Blank PCB Map sheets (A3, top-down outline of the specific ECU assigned, printed)
- 2 x Reference Designator Quick-Reference cards (laminated, reusable)
- 1 x digital multimeter (Fluke 87V or equivalent) with fine probe tips fitted
- 1 x digital loupe or magnifier (10x minimum) — or USB microscope if available
- 1 x set of coloured highlighters (minimum 5 colours: red, blue, green, yellow, orange)
- 1 x fine-tip marker pen (Staedtler Lumocolor or equivalent)
- 3 x loose components on a small tray: one ferrite bead (0402 or 0603), one 100-ohm resistor (0402 or 0603), one zero-ohm resistor/jumper (0402 or 0603) — for Stage 4

### Room / Shared Equipment
- ESD mats on all benches — connected and verified before session starts
- ESD wrist straps — one per student, verified working
- 2 x USB microscopes on shared stands for groups that finish standard tasks early
- Instructor reference ECU (same model as student ECUs) with regions pre-labelled — for debrief use only
- Whiteboard or projected slide showing the Region Colour Coding guide (see below)
- Timer visible to the class

### Instructor Materials
- Marking rubric printout — one per student
- Completed reference PCB map (instructor-annotated version) — kept face-down until debrief
- Stage task cards (laminated or printed, one per station)

---

## Region Colour Coding System

Students use highlighters to mark regions on the blank PCB map:

| Colour | Region |
|--------|--------|
| Red | Power entry and protection |
| Blue | Processor — MCU, memory, clock |
| Green | Communication ICs — CAN, LIN transceivers |
| Yellow | Output drivers and power stage |
| Orange | Connector areas |

This colour code is posted on the whiteboard throughout the session and referenced in all instructor instructions.

---

## Session Timeline

| Time | Phase | Activity |
|------|-------|----------|
| 0:00–0:08 | Safety briefing | ESD check, objectives, task overview |
| 0:08–0:15 | Instructor demonstration | Live orientation sequence on reference ECU |
| 0:15–0:55 | Workshop — four stages | Students work through PCB mapping stages |
| 0:55–1:05 | Peer review | Students swap maps and mark using rubric |
| 1:05–1:20 | Instructor debrief | Reference map revealed, errors discussed |
| 1:20–1:30 | Q&A and Day 5 preview | Open questions, overview of filtering content |

---

## Safety Briefing Script (0:00–0:08)

Deliver verbally before any equipment is touched:

> "Before we touch anything — ESD protocol. Everyone put on your wrist strap now and connect it to the mat. I will walk around and check each one before we issue the ECUs.
>
> These ECUs are not powered today. No voltage hazard. However, ESD protocol applies regardless of whether there is mains power involved. A static discharge from your hand can silently damage semiconductor junctions on an unpowered board — the IC looks fine, fails later under power.
>
> The ECUs you are receiving are real units retired from service or sourced as training boards. Some have known faults. Some are intact. Today is not a fault-finding exercise — today is a board literacy exercise. You are learning what is there and where it lives.
>
> Two handling rules: One — hold the PCB by its edges at all times. Do not touch any IC directly. Two — when you probe a test point with the multimeter, keep the probe vertical to avoid slipping onto an adjacent pad. On a dense ECU board, pads are less than 1mm apart."

---

## Instructor Demonstration (0:08–0:15)

Using the instructor reference ECU (projected on an overhead camera or held up for the class), demonstrate the five-step board orientation sequence from Session 04T slide 12.

> "I am going to orientate this unknown ECU from scratch in under two minutes — using only the five steps from this morning. Watch the sequence."

**Step 1:** Identify the connectors — point out how they sit at the board edge, high pin count
**Step 2:** Follow power traces — show how thick traces lead inward from the power pins toward a cluster of protection components
**Step 3:** Find the MCU — identify the dominant QFP IC, point out the crystal immediately adjacent to it
**Step 4:** Find the communications ICs — point out the transceiver ICs near the connector edge, their location between the MCU and the connector
**Step 5:** Find the output driver region — show MOSFETs or driver ICs near the output connector, point out their larger size and thermal pads

While demonstrating, colour the instructor reference map live using the colour coding system. This shows students exactly what their output should look like.

> "That took 90 seconds. After today's lab, it will take you the same. Let us begin."

---

## Workshop Activity — Four Stages (0:15–0:55)

Students work through four sequential stages. Each stage builds on the previous one. Instructor circulates continuously — one full circuit of the room every 4 to 5 minutes.

---

### Stage 1: Board Orientation and Region Mapping (10 minutes, 0:15–0:25)

**Task:** Identify the five major regions and colour them on the blank PCB map.

Student instructions (on stage task card):
1. Pick up the ECU by its edges
2. Orient the board so the main connector faces you
3. Apply the five-step orientation sequence from this morning's theory session
4. Colour each region on the blank PCB map using the correct highlighter colour
5. Write the region name inside the coloured area in marker pen

**Checkpoint 1** — instructor checks each station at approximately 0:22:
- Has the student correctly identified the connector region (orange)?
- Is the processor region (blue) placed around the correct dominant IC?
- Is there a distinct red area showing the power entry path from the connector?
- Is the student handling the board by its edges?

**Common error at this stage:** Students mark the entire board with one colour because they cannot distinguish regions yet.

Instructor prompt: "Find the largest IC first — circle it in blue. That is your anchor. Now where are the connectors? Orange, at the edge. Now trace the thickest trace from the main power connector inward — where does it lead? That is your red region. Work outward from your anchor."

---

### Stage 2: Reference Designator Hunt (12 minutes, 0:25–0:37)

**Task:** Locate and record specific reference designators from the silkscreen using the loupe or USB microscope.

Provide the following task card to each student:

---
**Stage 2 Task Card — Reference Designator Hunt**

Using the loupe or USB microscope, find and complete the table:

| Item to Find | Reference Designator Found (e.g. U1, C47) | Location on Board |
|---|---|---|
| The MCU (largest IC on board) | | |
| A ferrite bead (L prefix) | | |
| A TVS or Zener diode (D prefix, near power input) | | |
| A small ceramic bypass capacitor near the MCU (C prefix) | | |
| A test point (TP prefix) | | |
| The clock oscillator or crystal (X or Y prefix) | | |

Write the actual designator from the silkscreen — not a description of the component.

---

**Checkpoint 2** — instructor checks at approximately 0:33:
- Is the student using the loupe or microscope? (Do not allow naked-eye reading of fine silkscreen — the point is learning to use magnification tools)
- Have they found at least 4 of the 6 items?
- Are they reading reference designators correctly? (The designator is always a letter followed by a number — not the component value)

**Common error:** Students find the component but cannot read the designator because it is under conformal coat residue or printed in very small font.

Instructor prompt: "Try the USB microscope at full zoom. Also check whether the designator is printed away from the component with a thin line pointing to it — on dense boards the label is sometimes offset."

**Common error:** Students record the component value (e.g. '100n') instead of the designator (e.g. 'C12').

Instructor prompt: "The designator is always a letter followed by a number. C12 is a designator. 100n is a value. Find the letter-number code."

---

### Stage 3: Test Point Mapping (10 minutes, 0:37–0:47)

**Task:** Locate all visible test points on the board. Mark each one on the PCB map and infer what signal it likely carries.

Student instructions:
1. Scan the entire board systematically — top surface first, then edges, then bottom
2. Mark every test point on the PCB map with a small circle, labelling it with its TP designation where readable
3. For each test point, write your best-guess signal name based on location:
   - Near the power entry region → supply rail (BAT, 5V, 3V3) or GND
   - Near the MCU → programming or clock access
   - Near CAN/LIN transceivers → CAN_H, CAN_L, or GND
   - Near the output driver region → PWM or driver output signal
4. Count the total number of test points on your board and record the number at the bottom of the map

**Checkpoint 3** — instructor checks at approximately 0:43:
- Has the student found at least 5 test points (most automotive ECUs have 10 to 30)?
- Are the signal name inferences reasonable based on location?
- Has the student noted any test points that are labelled on the silkscreen vs those that are unlabelled?

**Instructor note:** Some ECU boards intentionally have unlabelled test points. This teaches students that identification requires inference from context, not just reading labels. Acknowledge this when circulating: "Unlabelled test points are normal. Your job is to narrow down what it could be based on where it sits."

---

### Stage 4: Component Identification by Measurement (8 minutes, 0:47–0:55)

**Task:** Use the multimeter in resistance mode to distinguish three visually identical surface-mount components.

Three components are provided loose on a tray at each station: a ferrite bead, a 100-ohm resistor, and a zero-ohm resistor (jumper). All are in identical 0402 or 0603 packages. They look the same to the naked eye.

Student instructions:
1. Set the multimeter to resistance (ohms) mode
2. Measure each of the three components and record the reading
3. Identify which is which using the table below
4. On your ECU board, find a component with an L prefix reference designator
5. Measure its DC resistance and record the result to confirm it matches the ferrite bead reading

| Component | Expected DC Resistance |
|---|---|
| Ferrite bead | 0.1 to 2 ohms (near-zero but measurable) |
| Zero-ohm resistor (jumper) | 0.0 to 0.3 ohms (essentially zero) |
| 100-ohm resistor | 95 to 105 ohms |

**Note on in-circuit measurements:** When measuring the L-designated component on the board, the reading may be affected by parallel paths through adjacent components. The expected result is still near-zero ohms for a healthy ferrite bead. If you read a high value (>100 ohms), note it — that component may be open-circuit (damaged).

**This stage directly addresses the common mistake flagged in Session 04T slide 24** — ferrite beads and resistors are visually identical and must be distinguished by measurement.

---

## Peer Review (0:55–1:05)

Students exchange their completed PCB maps with the station to their left. Each student reviews their partner's map against the supplied marking rubric.

### Peer Review Rubric

| Item | Marks | Criteria |
|---|---|---|
| Five regions correctly identified and colour-coded | 10 | 2 marks per region; region must contain the correct component types |
| Reference designators correctly recorded (Stage 2) | 12 | 2 marks per item found and correctly designated |
| Test points mapped with reasonable signal inferences | 6 | 1 mark per test point correctly identified (maximum 6) |
| Component measurement results recorded (Stage 4) | 6 | 2 marks per component correctly identified by measurement |
| ESD and handling (instructor-observed, not peer-marked) | 6 | Assessed by instructor during the session |
| **Total** | **40** | |

Peer reviewers mark each item and write a brief comment against any item they believe is incorrect. Maps are returned to their owners after 10 minutes.

---

## Instructor Debrief (1:05–1:20)

Display the instructor reference PCB map (annotated version) on the projector.

**Stage 1 Debrief:**
Show the correct region boundaries. Ask: "Did anyone put the communication ICs in the processor region? Let us look at why they are separate — the CAN transceiver is between the MCU and the connector because it is an interface device, not a processing device. It translates the MCU's digital signal into a differential bus signal. Physically close to the connector; logically between the bus and the processor."

**Stage 2 Debrief:**
Read out the correct reference designators from the reference map. Discuss any components that were hard to find. Ask: "Who had trouble finding the ferrite beads? What did they look like?" Draw out the observation that they are identical to resistors in appearance — which is exactly why Stage 4 exists.

**Stage 3 Debrief:**
Ask: "How many test points did you count?" Compare across the class. If numbers vary widely, discuss reasons: some test points are on the bottom surface, some are vias with solder mask windows that are easy to miss.

Ask: "Did anyone find an unlabelled test point they could not identify? Let us work through it together." Take one example from the class and reason through the signal identity based on location.

**Stage 4 Debrief:**
Compare measurements. Ask: "Did anyone get a reading above 10 ohms on a component they thought was a ferrite bead on the board?" If yes, this is a significant finding — the component may be damaged (open ferrite bead = no power to the IC it feeds). Ask the student to describe where on the board it was located. This may be a genuine fault on the training ECU — acknowledge and record it.

**Key debrief question:**
> "Why does it matter whether you can find and read test points on an unknown ECU — one with no documentation at all?"
>
> *Draw out: Test points let you measure signals without probing live IC pins. On an unknown ECU with no service data, test points are your starting point for building a picture of the circuit. You probe TP_GND first, then work from the power entry inward, building a signal map as you go. This is the foundation of the blind-diagnosis approach we will practice in Module 5.*

---

## Common Mistakes and Instructor Responses

| Mistake | Instructor Response |
|---|---|
| ESD strap not properly connected at session start | Stop the student immediately. Reconnect, verify continuity with the tester, then proceed. Do not allow any ECU contact until verified. |
| Pressing probe tip hard into test point pad | Demonstrate light-touch probing technique. Excessive force can lift small exposed pads, especially on older boards with weakened solder mask. |
| Marking entire board as one region | Use the five-step orientation sequence as a directed prompt. "Give me the connectors first — orange, at the edges. Now find the MCU — blue. You have two anchors. Fill in between." |
| Confusing the MCU with a large tantalum capacitor | "Large IC packages have multiple pin rows around all four sides — look at all four edges. Capacitors have two terminals. Transformers have lead rows on two opposing sides only." |
| Recording component value as reference designator | "C12 is a designator. 100n is a value. Find the letter-number code." |
| Cannot locate ferrite beads | "Look for L-prefix designators. They are placed in series on power supply traces — typically in a row near the power input or MCU supply pins. They are 0402 or 0603 packages, identical in size to resistors." |
| In-circuit ferrite bead reads unexpectedly high | "That is a valid finding — record it and bring it up at debrief. It may be an open ferrite bead, which means the IC it feeds is not getting power through this path." |

---

## Assessment Criteria — Instructor Observation Checklist

Complete for each student during the session (feeds into the ESD/handling marks in the rubric):

| Criterion | Observed Y/N | Notes |
|---|---|---|
| ESD wrist strap worn and connected throughout | | |
| Board handled by edges only — no IC contact | | |
| Loupe or microscope used for fine detail | | |
| Multimeter set to correct range before each measurement | | |
| Probes kept vertical when contacting board pads | | |
| Student asked for clarification when genuinely stuck (not guessing randomly) | | |

---

## Timing Adjustments

**If a student finishes all four stages early:** Ask them to attempt to trace one complete power supply path — from the main power connector pin, across the board, through each component it passes, to the first MCU VCC pin. They should document each component they pass through (by reference designator) in order. This previews Day 5 content directly.

**If the class is running slow:** Stage 4 (component measurement) can be demonstrated by the instructor rather than performed individually. Stages 1 through 3 are the non-negotiable core for this session.

---

## Day 5 Preview (1:20–1:30)

Close the session with:

> "You can now read a PCB — you know where everything lives, you know how to find and use test points, and you know how to distinguish components that look identical.
>
> Tomorrow in theory, we go deep into the part of ECU design that is most commonly missed in training courses: the filtering and protection circuits. Every bulk capacitor, every ferrite bead, every TVS diode you found on your board today has a specific job protecting the processor from a specific electrical threat in the vehicle environment.
>
> Tomorrow you will learn what each threat is, exactly how each component stops it, and what the failure signature looks like when that component is missing or damaged. This is the content that separates a competent ECU technician from someone who just replaces boards.
>
> Be ready for a full theory session — it is dense but critical."
