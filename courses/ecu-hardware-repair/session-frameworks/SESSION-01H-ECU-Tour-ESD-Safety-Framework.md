# SESSION-01H: ECU Physical Tour & ESD Safety — Session Teaching Framework

---

## Session Header

| Field | Detail |
|-------|--------|
| **Session Code** | SESSION-01H |
| **Session Title** | ECU Physical Tour & ESD Safety |
| **Module** | Module 1: ECU in the Real World |
| **Day** | Day 1 (PM Session) |
| **Duration** | 75–90 minutes |
| **Delivery Type** | Practical Workshop — Hands-on with real ECU hardware |
| **Room Setup** | Workshop benches; one workstation per student or per pair; ESD mats installed before students arrive |
| **CO Alignment** | ECUHR-CO-1 |
| **MO Alignment** | MO 1-3 (Apply correct ESD safety procedures when handling ECUs and PCB components) |

---

## Session Outcomes

By the end of this session, students will be able to:

| SO Code | Outcome |
|---------|---------|
| ECUHR-SO-1-3-2 | Demonstrate correct use of anti-static wrist strap, ESD mat, and ESD-safe packaging |
| ECUHR-SO-1-3-3 | Identify regions on an ECU PCB and correctly handle a board without touching sensitive ICs |
| ECUHR-SO-1-3-4 | Inspect a real ECU and label the major circuit regions: power supply, processor, drivers, communication, connectors |

---

## Equipment and Materials List

### Per Workstation (one student or pair)
- [ ] ESD anti-static wrist strap with coiled cable and banana plug / snap connector
- [ ] ESD mat (minimum A4 size, preferably full bench coverage) with ground lead
- [ ] 1 x real ECU PCB — dismantled, housing removed, ready to inspect (engine ECU preferred)
- [ ] Magnifying glass or loupe (5x–10x minimum)
- [ ] Printed ECU PCB photograph worksheet — same board as the physical ECU, with blank region label boxes (see Instructor Preparation notes)
- [ ] Marker pen or pencil for labelling worksheet
- [ ] 1 x ESD-safe bag (pink/silver anti-static bag) for storage demonstration

### Instructor / Class Shared Equipment
- [ ] Wrist strap tester (go/no-go tester — tests both wrist strap and mat ground connection)
- [ ] 1 x additional ECU of a different type (BCM, ABS module, or transmission ECU) for comparison exercise
- [ ] Bench ground point / bonding bus or grounded power strip for mat connections
- [ ] Projector or large monitor displaying annotated PCB reference image
- [ ] Whiteboard or flip chart for region label list

### Optional but Recommended
- [ ] USB microscope or digital magnifier connected to screen (allows instructor to show board detail to whole class simultaneously)
- [ ] UV torch (reveals conformal coating coverage — dramatically effective visual)
- [ ] Second set of printed worksheets showing a different ECU type for the comparison exercise

---

## Safety Briefing (10 minutes)

**Conduct this briefing before any equipment is distributed. Students should be seated and not yet handling anything.**

---

### Part A: Why ESD Safety Matters in This Workshop

**Instructor Script:**

> "Before we touch a single component today, we talk about ESD safety. This is not optional, it's not a formality, and it applies every single time you handle an ECU or any PCB in this course."

> "In the theory session this morning, we talked about ESD — electrostatic discharge. You learned that a typical person can carry 15,000 volts of static charge after walking across carpet, and that you can't feel a discharge below about 1,500 volts. The damage threshold for a MOSFET gate oxide is 100 volts. You do the maths."

> "Here's the practical reality: if you pick up this ECU without a wrist strap, and you have 500 volts of charge on your body right now — which is possible just from sitting in a fabric chair — and your finger brushes an exposed IC pin, you've just delivered an invisible discharge to that component. It won't die immediately. It will fail three weeks from now, in a customer's vehicle, in a way that looks completely unrelated."

> "Every time you hear about a technician who 'replaced the component and it failed again' — ESD is a likely explanation. We are not going to be that technician."

> "In this workshop: wrist strap on before you touch anything. Mat grounded before anything goes on it. Board stays in ESD bag until you are grounded. No exceptions."

---

### Part B: Physical Handling Rules for ECU PCBs

Display the following rules on the projector or write them on the board. Read each one aloud.

**The Six PCB Handling Rules:**

1. **Always wear a grounded wrist strap.** The strap must make contact with bare skin — not over a sleeve. The cord must be connected to the mat or bench ground point.

2. **Always work on a grounded ESD mat.** The mat must be connected to the same ground point as the wrist strap. Never place a PCB on an ordinary table, cardboard, plastic bag, or clothing.

3. **Never touch IC pins, IC bodies, or exposed component leads directly.** Hold the board by its edges — the areas where no components are soldered. If an edge has connector pins, hold the opposite edge.

4. **Never slide a PCB across a surface.** Sliding generates static charge. Lift and place.

5. **Store boards in ESD-safe bags when not being worked on.** Grey/silver metallised bags or pink poly anti-static bags only. Standard plastic bags are prohibited — they generate charge.

6. **Discharge yourself before reaching into a parts box or bag.** Touch the grounded mat with your hand before picking up a component.

> "These rules apply in this workshop, in the practical labs throughout this course, and in your workshop when you return to work. They are professional practice, not just course rules."

---

### Part C: What We Are NOT Doing Today

> "To be clear about what we are doing and not doing today. We are handling real ECUs — but these are dismantled study boards, not live units. Nothing is powered on. No soldering today. No probing. We are inspecting, identifying, and labelling. The goal is to get comfortable handling a real ECU board correctly and to start reading the board as a map."

> "If at any point you are unsure whether something is safe to touch, ask me before you touch it. That is always the right approach."

---

## Pre-Activity Instructor Demonstration (15 minutes)

**Conduct this demonstration at the front of the class before students begin their own activity. All students should watch; no one starts their own work during this time.**

---

### Demo Step 1: ESD Equipment Setup and Verification (5 minutes)

Pick up the wrist strap. Hold it up.

> "This is an ESD wrist strap. The wrist band part goes on your wrist — bare skin contact. This coiled cord connects to the mat or to a dedicated ground point."

Put it on correctly. Show the band sitting flat against the inside of your wrist.

> "Notice I'm wearing it on my wrist, not my forearm. Not over my sleeve. The metal contact plate is touching skin. That's what creates the path for charge to drain away slowly and safely."

Connect the cord to the mat ground point.

> "Now I'm connected to ground. Any charge that builds up on my body drains through this cord — slowly, through a 1-megohm resistor built into the strap. The resistor is there deliberately. If you accidentally touch a live circuit, the resistor limits the current through your body. ESD safety and electrical safety are both served by that resistor."

Pick up the wrist strap tester.

> "Before every session, you test your strap. This tester checks two things: that the strap has continuity — the connection from your wrist to the cord is intact — and that the resistance is in the correct range. A broken strap gives you false confidence. You think you're protected and you're not."

Demonstrate using the tester. Show a passing result.

> "Green light — strap is good. If you get a fail, swap the strap. Do not work on ECU hardware with a failed strap."

---

### Demo Step 2: Removing an ECU from an ESD Bag (3 minutes)

Hold up the ESD bag with an ECU inside.

> "The board is in this ESD bag. The bag is part of the protection system — it creates a Faraday cage around the board while it's in transit or storage. Notice the board does not come out until I am grounded and on the mat."

Touch the mat with your free hand.

> "I'm grounded. The mat is grounded. Now I open the bag."

Open the bag slowly. Do not slide the board out — tip it gently into your hand.

> "I'm holding it by the edges. Look at where my fingers are — at the very edge of the board, away from the component areas. I'm not touching the ICs, not touching the connector pins, not touching any exposed component leads."

Place the board flat on the mat.

> "Board on the mat. The mat is grounded. The board is on a safe surface. Now inspection can begin."

---

### Demo Step 3: Correct Board Handling Technique (4 minutes)

Hold the board up to show the class.

> "When you're moving the board — to turn it over, to look at the other side, to pass it to someone — always hold the edges. Use two hands for larger boards. Don't pinch across the component surface."

Demonstrate turning the board over correctly, using edge grip.

> "If I need to put the board down temporarily while still in the session — it goes on the ESD mat. Not on the bench surface beside the mat. Not on my notepad. On the mat."

> "If I need to put it away completely — it goes back in the ESD bag. The bag gets closed. Then it can go on the bench or in a drawer."

Demonstrate: return board to bag, seal bag.

> "One more thing. Do not place ESD bags on top of monitors, power supplies, or any equipment that may generate a static charge through the bag. The bag shields the inside, but it does not protect against charge building up on the bag surface itself."

---

### Demo Step 4: Quick Region Orientation on a Real ECU (3 minutes)

Remove the board from the bag again. Place on mat.

> "Before you start your own labelling activity, I want to show you how to read a board at a glance. We're going to find six regions."

Point to each region as you name it. Keep this fast — students will do the detailed identification themselves.

> "Power supply section — usually near the main connector or at one edge. Large components. You'll see at least one significant capacitor, maybe a voltage regulator IC."

> "Processor / MCU area — large IC, often in the centre or protected centre-rear area of the board. Look for the biggest IC that has many fine pins on all four sides — that's typically the microcontroller."

> "Input signal conditioning — small resistors and capacitors clustered near the connector. These are the signal input filters and ESD protection components."

> "Output driver section — large transistors or driver ICs, often with heatsink areas or exposed copper pads beneath them. Usually on one side of the board near where the output harness connects."

> "Communication interfaces — you may see small ICs near the connector labelled with CAN, LIN, or K-LINE. These are the transceiver chips."

> "Connector / protection zone — the area right at the edge of the board where the main connector makes contact. Look for TVS diode arrays here — small multi-pin components in a line right at the board edge."

> "Now you'll find these six regions on your own board. Your worksheet has the same photograph of your board with blank label boxes. Find each region, circle it on the board photograph, and write the region name."

---

## Student Activity — Step-by-Step (40–45 minutes)

**Distribute equipment at the start of this section. Do not distribute early.**

---

### Step 1: ESD Equipment Setup (5 minutes)

Each student:

1. Take the wrist strap from the table. Examine it. Check the cord for damage — look for kinks, fraying, or a broken snap connector.
2. Put the wrist strap on your dominant wrist. Band on bare skin, flat against the inside of the wrist. Metal contact plate touching skin.
3. Connect the coil cord to the ESD mat ground stud or the bench ground point.
4. Take the wrist strap tester. Test your strap as demonstrated. Confirm green/pass result.
5. If the tester shows a fail — raise your hand before proceeding. Do not start handling the board.
6. Check your mat is lying flat on the bench and the mat ground lead is connected.

**Instructor checkpoint here — see Checkpoint 1 below.**

---

### Step 2: Remove ECU from ESD Bag (2 minutes)

1. Confirm you are grounded (strap on, cord connected, tester passed).
2. Touch the mat surface with your free hand before opening the bag.
3. Open the ESD bag. Tip the board gently onto the mat. Do not drag it out.
4. Place the board component-side up on the centre of the mat.
5. Set the empty ESD bag to one side — on the mat surface, not off the mat.

---

### Step 3: Physical Inspection — Housing and Connector (5 minutes)

Before looking at the PCB in detail, examine the housing if it is still present, or the dismantled housing parts.

1. Identify the type of connector: how many pins, how many rows, single or multi-connector housing.
2. Look at the housing material and any rubber sealing gaskets. Note: the gasket is the moisture protection for the connector interface.
3. Find the mounting points — how this ECU bolted to the vehicle.
4. If a housing label is present — note the part number, manufacturer, and any temperature rating printed on it.
5. On your worksheet: write down the connector pin count (approximate) and the ECU part number if visible.

---

### Step 4: PCB Initial Survey — Overall Layout (5 minutes)

Hold the board by its edges. Look at it under normal light first, then under magnification.

1. Note the overall board size and shape.
2. Count the number of PCB layers if visible from the edge (edge of board shows copper layer lines — each copper line is one layer).
3. Identify the side that faces the connector (usually the bottom, with most of the protection components).
4. Identify the main component side (usually the top).
5. Look for the silkscreen — the white printed text on the board surface. Find any reference designators (R1, C1, U1, etc.) and understand that R = resistor, C = capacitor, U = IC, D = diode, L = inductor/ferrite.
6. On your worksheet: estimate layer count and note which side of the board faces the connector.

---

### Step 5: Identify the Six Regions and Label the Worksheet (15 minutes)

Using the printed photograph worksheet and a marker or pencil, locate and label each of the six regions on your specific board. For each region:

**Region 1: Power Supply Section**
- Look for: large capacitor(s), voltage regulator IC (usually TO-252 or DPAK package, or a larger rectangular IC with exposed pad), inductors (looks like a small coil or rectangular block).
- Where to find it: near the main power connector pins, often at one end of the board.
- On worksheet: circle the power supply section and write "POWER SUPPLY" with an arrow.

**Region 2: Processor / Microcontroller Section**
- Look for: the largest IC on the board with fine-pitch pins on multiple sides (QFP, LQFP, or BGA package). May have a clock crystal nearby — a small silver or golden rectangular component labelled X1 or Y1.
- Where to find it: usually in a central or protected area of the board.
- On worksheet: circle the processor and write "MCU / PROCESSOR" with an arrow.

**Region 3: Input Signal Conditioning**
- Look for: clusters of small resistors (0402 or 0603 packages) in rows near the connector edge. These are the series resistors on input signal lines. Small capacitors near them are the filter capacitors.
- Where to find it: near the connector, on the traces coming in from the outside world.
- On worksheet: circle the signal conditioning area and write "SIGNAL CONDITIONING / INPUT FILTER" with an arrow.

**Region 4: Output Driver Section**
- Look for: larger transistors or multi-channel driver ICs. These are often the hottest-running components on the board — they may have exposed copper areas beneath them (thermal vias) or be physically larger than surrounding components.
- Where to find it: on the side of the board near the output harness connections, or in a dedicated section.
- On worksheet: circle the output section and write "OUTPUT DRIVERS" with an arrow.

**Region 5: Communication Interface**
- Look for: small ICs (SOIC-8 or SOT-23-5 packages) with nearby ferrite beads or common-mode chokes on the signal traces. CAN transceiver ICs often have the marking TJA, SN65, or MCP on them.
- Where to find it: near the connector pins allocated to CAN or LIN bus signals.
- On worksheet: circle the communication section and write "COMMS / CAN / LIN" with an arrow.

**Region 6: Connector Protection Zone**
- Look for: small multi-pin SMD components in a line right at the board edge nearest the connector. These are TVS diode arrays. They have many pins (typically 6 or 8) and sit right at the connector boundary.
- Where to find it: literally at the connector edge of the board — the first line of components the signals encounter when entering the ECU.
- On worksheet: circle the connector protection zone and write "ESD PROTECTION / TVS ARRAYS" with an arrow.

**Instructor checkpoint here — see Checkpoint 2 below.**

---

### Step 6: Component Close-Up Inspection (5 minutes)

Using the magnifying glass or loupe, examine the following and note your observations on the worksheet:

1. Find one TVS diode array near the connector. Note its package size and pin count.
2. Find two small capacitors near an IC power pin. Note the package size (0402, 0603, or 0805).
3. Find the crystal oscillator near the MCU. Note its package.
4. If a watchdog IC is visible (small 5–8 pin IC, sometimes near the MCU or in its own small circuit with RC components), identify it and mark it on the worksheet.
5. Look at the solder joints under magnification. Note whether joints appear shiny and smooth (good) or dull, grainy, or cracked (potentially faulty).
6. Look for conformal coating — the slightly shiny protective layer over the board. If a UV torch is available, the instructor will demonstrate conformal coating visibility under UV light.

---

### Step 7: Comparison Exercise — Two ECU Types (5 minutes)

The instructor will bring a second ECU of a different type to each workstation, or display it on the projector.

Compare your engine ECU with the second ECU type (BCM, ABS module, or transmission ECU):

1. Which board is physically larger?
2. Which has more output drivers (heavier power components)?
3. Which appears to have more connector pins?
4. Can you identify the same six regions on the second board? Which regions are immediately obvious and which are harder to find?
5. On your worksheet: write two observations about how the two ECUs differ in their PCB layout.

---

### Step 8: Return and Storage Procedure (3 minutes)

1. Once the activity is complete, hold the board by its edges and return it to the ESD bag.
2. Seal the bag.
3. Place the sealed bag on the ESD mat, not off the bench.
4. Remove your wrist strap. Coil the cord and store the strap with the strap tester.
5. Ensure the mat ground lead remains connected until the end of the session.

---

## Instructor Checkpoint Moments

### Checkpoint 1 — ESD Equipment Setup (after Step 1)

**When:** Before students remove boards from bags.

**What to look for:**
- Wrist strap on bare skin, not over sleeve.
- Coil cord connected — follow the cord visually from wrist to mat/ground point.
- Tester result observed — did the student actually look at the result?
- Mat flat on bench, ground lead connected.

**Common errors at this checkpoint:**
- Strap worn over a long sleeve — conductor not touching skin.
- Cord not snapped in — looks connected but is not.
- Tester result not checked — student puts tester down without looking at indicator.
- Mat ground lead draped behind the bench but not connected to ground point.

**What to say if you see an error:**
"Before you open that bag — let's check your strap is making good contact with your skin. Can you pull back your sleeve?" Do not make it embarrassing — correct and move on.

**Minimum standard before proceeding:** Every student must have a passed tester result before any board leaves an ESD bag.

---

### Checkpoint 2 — Worksheet Region Identification (during Step 5)

**When:** Approximately 10 minutes into Step 5, while students are still working.

**Walk the room. At each workstation check:**
- Student is holding the board by edges when picking it up, not by grasping across components.
- Board is on the mat, not off to the side of the mat.
- Worksheet has at least 3–4 regions identified with reasonable accuracy.

**What to look for in the region identification:**
- Power supply: student should be pointing to the area with the largest capacitors and the voltage regulator, not at random large ICs.
- MCU: student should have identified the largest multi-pin IC, not a driver IC. Common confusion: students mistake a large driver IC (which may also have many pins) for the MCU. The MCU is typically in a more central location and has a finer pitch pin arrangement on all four sides.
- ESD protection zone: student should have identified the TVS arrays at the connector edge. If they have missed this region, prompt: "Look right at the very edge of the board nearest the connector — what components are in the first row?"

**What to say to a student who is stuck:**
"Tell me what you see in this area of the board. What's different about these components compared to the ones in the middle of the board?" Guide through observation — do not just tell them the answer.

**What to say to a student who has finished early:**
"Good — now look at each region with the loupe. Can you find a component in each region that you can't identify? Write the reference designator down — we'll look those up in Module 3."

---

### Checkpoint 3 — Final Worksheet Review (end of Step 5 / before Step 6)

**When:** Before moving to close-up inspection.

**Ask each student to show you their completed region labels. Verify:**
- All six regions are labelled.
- Labels are in approximately the right locations (does not need to be perfect — understanding the zone is what matters).
- Student can verbally explain why one region is where it is. Ask one question per student: "Why is the ESD protection right at the connector edge?" or "Why do you think the power supply section is near the main connector?"

**Minimum standard to proceed:** Four or more of the six regions correctly identified and student can give a reason for at least one placement.

---

## Assessment Criteria — Instructor Sign-Off

This session uses a **direct observation sign-off**. The instructor observes each student performing the tasks and signs the student's record at the end of the session.

### Sign-Off Criteria

| Criterion | Standard Required for Sign-Off |
|-----------|-------------------------------|
| ESD wrist strap fitted correctly | Worn on bare skin; cord connected; tester passed |
| ESD mat used correctly | Board remained on mat throughout activity; mat was grounded |
| Board handling technique | Board held by edges; no contact with IC bodies or pins |
| ESD bag procedure | Board stored in bag when not being worked on; bag sealed |
| Region identification — worksheet | Minimum 4 of 6 regions correctly identified and labelled |
| Verbal explanation | Can explain the purpose of at least one identified region |

### Sign-Off Descriptors

**PASS — Ready for next session:**
Student demonstrated all six criteria. May have needed one correction but corrected immediately and maintained correct practice thereafter.

**BORDERLINE — Additional guidance needed:**
Student completed all tasks but required multiple corrections on ESD handling procedure, OR fewer than 4 regions correctly identified. Instructor to have a brief one-to-one conversation before next practical session. No re-assessment required — record the gap and monitor in next practical session.

**NOT YET — Must repeat before proceeding with practical labs:**
Student repeatedly handled board incorrectly after correction, OR did not use ESD strap during activity, OR fewer than 3 regions identified. Student must repeat the ESD handling portion of this session before Day 2 practical activities. This is a safety-relevant criterion — it cannot be waived.

---

## Common Mistakes and How to Correct Them

| Mistake | How It Typically Appears | Correction |
|---------|--------------------------|------------|
| Wrist strap over a sleeve | Student's cord is connected but sleeve is covering the wrist contact | "Pull your sleeve back — the band needs to be on bare skin, not fabric. The conductor needs to touch your skin to work." |
| Board picked up by touching component surface | Student grabs the board from the centre with fingers over components | "Stop — put the board down on the mat. Now hold it by the very edge, like you're holding a slice of bread by the crust. Your fingers only touch the edge." |
| Board placed on the bench surface off the mat | Student runs out of room on the mat or moves the board aside | "That board needs to go back on the mat. Anything that's not on the mat is not grounded. Move the mat if you need more space, or clear what's taking up space on the mat." |
| Wrist strap not tested | Student puts strap on and immediately opens the bag | "Before you open the bag — have you tested the strap? Use the tester. Let me see the result." |
| Trying to identify ICs by looking up markings during Step 5 | Student becomes distracted trying to decode IC part numbers instead of identifying regions | "IC identification comes in Module 3. Right now we're identifying regions — the zones on the board, not specific component functions. Focus on: where is the power section? Where is the processor section?" |
| Confusing a driver IC for the MCU | Student labels a large driver IC as the processor | "Good observation — that is a large IC. Is it in the centre of the board, or is it near an output area? The MCU is typically in a protected central position. What's different about the pin pitch and pattern compared to that driver IC?" |
| Treating conformal coating as damage | Student notes the shiny film as "damaged" or "residue" | "That coating is deliberate — it's conformal coating, the moisture protection layer we talked about this morning. It's meant to be there. When it's absent in a patch, that's the problem — that's where corrosion starts." |
| Comparing boards too quickly in Step 7 | Student says "they look the same" without examining | "Look at the output section on each board. One of these ECUs controls a lot more actuators than the other — you can tell by the size and number of driver components. Which one has more power-handling capability?" |

---

## Debrief Questions (10 minutes)

Conduct this debrief as a whole-class discussion at the end of the session. Students remain at their benches with their completed worksheets.

**Boards should be back in ESD bags before the debrief begins.**

---

**Question 1 — Connecting to morning theory:**

> "This morning we said every extra component on an ECU has a reason. You've now held a real ECU and found six different regions. Which region surprised you most — either by how many components it had, or by where it was located on the board?"

Listen for: students noticing the density of the input protection zone, the number of small capacitors around the MCU, or the physical size of the power section relative to the logic section.

---

**Question 2 — ESD handling:**

> "You now know where the ESD protection components are on the board — right at the connector edge. If a technician picks up a board and their thumb brushes those TVS diode arrays, why is that a less critical risk than their thumb brushing the MCU directly?"

Looking for: TVS diodes are the protection components — they are specifically designed to absorb ESD events. Touching them directly is still not good practice, but they are more robust than the MCU which has no additional external protection on its pins. Also: the TVS diodes are the protection for the pins — if they fail open, those signal pins are now unprotected.

---

**Question 3 — Why regions are where they are:**

> "The ESD protection TVS arrays are right at the connector edge — as close to the connector as possible. Why does their position matter? What would happen if they were in the middle of the board instead?"

Looking for: ESD energy enters from the connector. The protection must intercept it before it travels along PCB traces to reach sensitive components. If the TVS arrays were in the middle of the board, the ESD pulse would have already reached the first ICs on the signal path before the protection could clamp it.

---

**Question 4 — Real-world link:**

> "You're in your workshop. A customer brings in an ECU with a fault. You remove the ECU from the car. Before you do anything else — what do you do, and why?"

Looking for: ESD bag immediately. Do not set it on the bench, on the seat, on a shelf, or on the car. Into an ESD bag. Because the act of removing the ECU from the vehicle — pulling it away from the chassis ground — can allow charge to build up on the board if it's not properly handled.

---

**Question 5 — Forward connection:**

> "Tomorrow and the day after, we work with multimeters and oscilloscopes — measuring real ECU signals. Based on what you saw on the board today, which region do you think will produce the most interesting measurements, and why?"

This is an open question — there is no single right answer. It primes students for Module 2 by connecting today's physical familiarity with the upcoming measurement work.

---

**Instructor closing statement:**

> "You've now held a real ECU, correctly, safely. You've identified the major regions. You've used ESD equipment properly. From this point forward — every time you handle an ECU in this workshop, the wrist strap goes on first. It is a habit, not a rule. Habits stick. Rules get forgotten under pressure."

> "Tomorrow we start measurement mastery. Come in ready to use a multimeter and oscilloscope at a level you probably haven't used them before. The ECU you handled today will start to make electrical sense."

---

## Instructor Preparation Notes

### Before the Session

1. **ESD mat installation:** Install and ground all ESD mats before students arrive. Connect mat ground leads to a verified earth point (not just a metal object — a proper grounded point). Test each mat ground connection with a mat tester if available.

2. **ECU preparation:** Ensure all ECUs are already dismantled (housing removed). The PCB should be accessible for inspection. Do not leave any housing screws loose — remove them entirely. If the ECU has silicone sealant around the housing perimeter, this should have been removed or at least broken open to give clear access to the PCB.

3. **Worksheet preparation:** Photograph the specific ECU boards you are using and print worksheets at A4 with sufficient resolution to show individual components clearly. Add blank text boxes in the image near each of the six regions. Do not pre-label the worksheets — students must find the regions themselves. Print at least one spare per workstation.

4. **Wrist strap testing:** Test all wrist straps before the session. Replace any that fail. A failed strap that is handed to a student and then passes their test creates confusion — start with tested equipment.

5. **Second ECU for comparison:** Have the second ECU type ready and accessible. If you only have one, use a high-resolution photograph projected on screen for the comparison exercise.

### Timing Note

This session runs tight at 75 minutes. The debrief is important — do not skip it. If Steps 6 or 7 are running long, it is acceptable to abbreviate Step 7 (comparison exercise) to a brief instructor-led class discussion rather than individual student activity. Steps 1–5 and the debrief must be completed in full.

---

*Framework Version: 1.0 | Course: ECUHR | Module 1 | Session: 01H | Created: 2026-02-18*
