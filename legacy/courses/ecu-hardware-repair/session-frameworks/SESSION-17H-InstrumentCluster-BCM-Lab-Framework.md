# SESSION-17H: Instrument Cluster & BCM Repair Lab
## Hands-On Session | Day 17 | Module 8: Module-Specific Repair

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 8 — Module-Specific Repair
**Day:** 17 | **Session Type:** Hands-On Workshop
**Duration:** 90 minutes
**CO Alignment:** co-1, co-2

---

## Session Outcomes

| ID | Outcome | Bloom's Level |
|----|---------|---------------|
| so-8-1-2 | Diagnose a pixel row fault on an LCD cluster display and replace the display driver IC using soldering skills | Apply |
| so-8-1-3 | Read and write odometer EEPROM data using appropriate tools and explain legal and ethical considerations | Apply |
| so-8-2-2 | Read BCM EEPROM, restore data to a replacement BCM, and program the replacement unit | Apply |
| so-8-2-3 | Perform variant coding on a BCM to configure vehicle-specific options and verify correct operation | Apply |

**Prerequisite:** SESSION-17T must be completed before entering this workshop.

---

## Workshop Overview

Two parallel stations run simultaneously. Groups of 2 students rotate through both stations within the session.

| Time Block | Group A | Group B |
|-----------|---------|---------|
| 0:00–0:05 | Joint safety briefing — all students together | |
| 0:05–0:47 | Station A — Instrument Cluster Repair | Station B — BCM EEPROM and Coding |
| 0:47–0:50 | Rotation and station handover | |
| 0:50–1:25 | Station B — BCM EEPROM and Coding | Station A — Instrument Cluster Repair |
| 1:25–1:35 | Joint debrief and check-off card completion | |

The instructor circulates between stations. Where class size permits, appoint one student per station as station lead to manage procedure flow and flag checkpoints. This allows the instructor to circulate rather than being pinned to one station.

---

## Pre-Session Instructor Setup

### Station A — Instrument Cluster (prepare before session)

- [ ] Cluster powered and pixel row fault confirmed visible (bench supply at 12.0V connected to cluster power and ground pins)
- [ ] If genuine faulted cluster unavailable: fault can be induced by partially lifting one display driver IC pin using a fine-tipped iron at approximately 200°C — apply minimal heat and slight upward pressure until joint cracks; allow to cool; power on to confirm rows are dead; prepare the night before and confirm the fault is stable before students arrive
- [ ] Schematic or marked-up cluster photograph showing display driver IC location — laminated, on bench
- [ ] EEPROM IC location marked on separate cluster PCB photograph — in station pack
- [ ] SOIC-8 clip connected to CH341A on bench, AsProgrammer software open with correct IC profile pre-selected
- [ ] HxD hex editor open on station laptop
- [ ] Cluster EEPROM odometer offset reference card on bench (shows: IC type, hex file offset for odometer bytes, encoding format for this specific cluster variant)
- [ ] Replacement display driver IC available (same part number as cluster specimen) — 2 spares per station
- [ ] Flux pen, fine iron tip, hot air station set to 200°C (not energised — student enables when needed)
- [ ] Ethical declaration forms printed — one per student; must be signed before EEPROM exercise begins

### Station B — BCM (prepare before session)

- [ ] Original BCM on bench — labelled "ORIGINAL BCM — DO NOT MODIFY"
- [ ] Original BCM EEPROM pre-read by instructor and saved as reference files: `REF_BCM_PN_READ1.bin` and `REF_BCM_PN_READ2.bin` — pre-loaded on station laptop desktop
- [ ] Replacement BCM on bench — labelled "REPLACEMENT BCM — STUDENT UNIT"
- [ ] Replacement BCM EEPROM confirmed blank (0xFF throughout) or confirmed as a different vehicle's data (students must perform the write)
- [ ] Bench harness for BCM: connector to power supply, OBD connector to scan tool — all pins labelled
- [ ] Scan tool (VCDS or equivalent) connected and confirmed working with bench harness before session
- [ ] VCDS coding guide or equivalent adaptation map for this BCM type — printed, laminated, on bench
- [ ] SOIC-8 clip and CH341A available at station
- [ ] Coding scenario card prepared (instructor specifies 2–3 coding changes the student will apply)

### Shared tools at each station

| Item | Notes |
|------|-------|
| Bench power supply | Set to 12.0V; current limit 3A for cluster, 5A for BCM |
| Digital multimeter | Auto-ranging |
| Oscilloscope | Two-channel minimum |
| Soldering iron | Fine tip, temperature-controlled |
| Hot air rework station | Pre-set to 200°C |
| Flux pen (no-clean) | Essential — not optional |
| Desoldering braid | 2mm width |
| IPA 99% + cotton swabs | Flux residue cleaning |
| ESD mat and wrist strap hook-up point | Mandatory — not optional |
| Magnifying loupe (10x) | IC pin inspection |

---

## Safety Briefing (Joint — 0:00 to 0:05)

**Instructor delivers the following points to all students before any station work begins. This briefing is not optional and is not to be delegated to a handout.**

**LCD temperature safety:**
The LCD glass in an instrument cluster will crack permanently if it reaches approximately 100°C sustained temperature. Hot air stations are set to 200°C for rework — this temperature is applied to the PCB and IC, not the glass. Keep the hot air nozzle moving at all times. Never hold hot air on one spot near the glass. Never direct hot air toward the glass panel of the display. If unsure at any point, power down and call the instructor.

**ESD safety:**
Cluster PCBs and BCM PCBs contain ESD-sensitive components. Wrist straps must be worn before handling any bare PCB. The ESD mat must be on the bench surface. Do not pick up bare PCBs from non-ESD-protected surfaces.

**Bench supply safety:**
Bench supplies are set to 12.0V with a current limit. Do not modify supply settings. Do not short output terminals. If you smell burning from a cluster or BCM on the bench supply, immediately switch off the bench supply — do not disconnect wires first.

**EEPROM write safety:**
Writing incorrect data to an EEPROM is recoverable only if you saved the original read. Confirm your read file is saved before performing any write operation. If unsure whether to write — do not write. Ask the instructor first.

**Legal reminder:**
Any modification to EEPROM odometer data outside of the defined exercise is not part of this session and will not be conducted. If a student has a question about a different scenario, take it to the instructor outside of the lab session. Each student signs the ethical declaration form before the EEPROM exercise begins.

**Capacitor discharge — CCFL backlight:**
If working on a CCFL-type cluster, the backlight inverter capacitors can hold charge after the bench supply is switched off. Wait 30 seconds after power-off and discharge using an insulated resistor tool before probing the backlight area.

---

## Station A: Instrument Cluster Repair

### Equipment at Station A

| Item | Quantity | Notes |
|------|----------|-------|
| LCD instrument cluster with pixel row fault | 1 | Bench-mounted, connected to 12V supply |
| Bench power supply | 1 | Pre-set 12.0V, 3A limit |
| Soldering iron (fine tip, temperature-controlled) | 1 | Set to 320–340°C for SOIC reflow |
| Hot air rework station | 1 | Pre-set 200°C; low airflow setting |
| Flux pen (no-clean rosin flux) | 1 | Essential for controlled reflow |
| Solder (0.5mm, 60/40 or 63/37) | 1 reel | For IC pin tinning if required |
| Desoldering braid | 1 | For cleanup if solder bridges occur |
| IPA (isopropyl alcohol 99%) + cotton swabs | 1 set | Flux residue cleaning |
| Magnifying loupe (10x) or digital microscope | 1 | IC pad and pin inspection |
| SOIC-8 clip adapter cable | 1 | For in-circuit EEPROM reading |
| CH341A USB programmer | 1 | Connected to station laptop |
| Station laptop with AsProgrammer and HxD | 1 | Software open, IC profile pre-selected |
| Replacement display driver ICs | 2 spares | Same package and part number as cluster specimen |
| Cluster EEPROM odometer offset reference card | 1 per student | IC type, odometer offset, encoding format |
| Cluster schematic / IC location photograph | 1 (laminated) | Showing display driver IC and EEPROM IC positions |
| Ethical declaration form | 1 per student | Must be signed before EEPROM exercise |
| Student job sheet | 1 per student | Records fault characterisation, EEPROM file names, odometer interpretation |
| ESD mat + wrist strap | 1 mat, 1 per student | |

---

### Station A Procedure

#### Phase A1 — Fault Confirmation (5 minutes)

**Step A1.1 — Power the cluster and observe the display:**
- Confirm bench supply is at 12.0V with current limit set
- Enable bench supply output
- Observe cluster display — allow 5–10 seconds for full initialisation
- Identify the pixel row fault: note which rows are dead (horizontal dark stripes across the display)
- Record on job sheet: number of dead rows, approximate vertical position, whether fault is consistent or intermittent

**Step A1.2 — Fault characterisation:**
- Is the fault consistent (always the same rows) or intermittent (appears and disappears)?
- Using a non-conductive probe (wooden pencil or plastic pry tool), gently tap the PCB near the display driver IC area with the cluster powered — does any change in the fault occur?
- A change when tapping confirms a marginal joint rather than a fully failed IC
- Apply gentle warmth to the display edge area (warm air gun at low setting, or palm of hand for 20 seconds) — if dead rows temporarily return, this confirms zebra strip compression or cracked joint; if no change → driver IC internal failure more likely

Record characterisation findings before proceeding to any rework.

---

**INSTRUCTOR CHECKPOINT A0:** Confirm each group can accurately describe the fault pattern before any tools are picked up. "Where are the dead rows? Top, bottom, distributed? Does tapping or warming change the fault?" This confirms observation before intervention.

---

#### Phase A2 — Identify and Inspect the Display Driver IC (5 minutes)

**Step A2.1 — Locate the display driver IC:**
- Power off the bench supply before touching the PCB
- Using the laminated reference photograph, identify the display driver IC responsible for the affected rows
- LCD clusters typically have 2–6 display driver ICs arranged along the display PCB edge
- The reference card shows which IC maps to which rows for this specific cluster variant

**Step A2.2 — Inspect the IC under magnification:**
- Use the 10x loupe or digital microscope
- Examine all solder pins around the IC perimeter — look for:
  - Micro-cracking at the pad-to-IC-lead junction (the fracture is often at the base of the fillet, not the tip)
  - Discolouration from heat stress or oxidation
  - Any visibly lifted pads or breaks in the fillet
  - Bridging between adjacent pins from previous rework attempts
- Record on job sheet: IC reference designator, IC marking code (copy exactly what is printed on the IC body), observed solder joint condition

---

#### Phase A3 — Reflow Attempt (10 minutes)

**First intervention is always reflow — not replacement. Replacement is only performed if reflow fails.**

**Step A3.1 — Apply flux:**
- Apply no-clean flux pen to all pins of the display driver IC — enough to create a thin, even coat across all pads; do not flood
- Allow flux to settle 30 seconds

**Step A3.2 — Reflow with soldering iron (preferred for this exercise):**
- Select fine chisel or conical tip on iron; set temperature to 330°C
- Touch tip to each pin/pad junction briefly — approximately 1–2 seconds per pin
- Work methodically along one row of pins, then the other — do not drag across multiple pins simultaneously
- Goal: allow any micro-cracked joints to reflow without adding solder
- If adding solder is needed (oxidised pads): touch 0.5mm solder to pin/iron junction — minimal addition only; avoid bridging

**Step A3.3 — Alternative: hot air reflow (use if iron access is restricted by display glass proximity):**
- Set hot air to 200°C, minimum airflow (low turbulence reduces risk of moving nearby components)
- Hold nozzle 20–25mm from IC; move in slow circles over pin area
- Do not direct airflow toward the display glass panel
- Heat for 15–20 seconds; watch for very subtle surface movement indicating solder has reflowed
- Remove heat; allow natural cooling — do not blow cold air on the IC

**Step A3.4 — Clean and cool:**
- Apply IPA to cotton swab; clean flux residue from all pin areas
- Allow 60 seconds of natural cooling before power-on
- Inspect joints under magnification before applying power

---

**INSTRUCTOR CHECKPOINT A1 (before power-on after reflow):** Inspect the reflow work under magnification with each group before they power on. Look for: solder bridges between adjacent pins; pins that were not reached by the iron; excessive solder addition creating blobs. Students tend to work too quickly — slow deliberate reflow with good flux is more effective than fast incomplete reflow.

---

**Step A3.5 — Power on and verify:**
- Enable bench supply
- Observe display — previously dead pixel rows should now display correctly
- If rows are restored: proceed to Phase A5 — EEPROM read
- If rows remain dead after cool-down: proceed to Phase A4 — IC replacement

Expected outcome if reflow was successful: all previously dead pixel rows now display correctly during cluster startup.

---

#### Phase A4 — Display Driver IC Replacement (15 minutes — only if reflow fails)

**Step A4.1 — Remove the failed display driver IC:**
- Apply fresh flux generously to all IC pins
- Set hot air rework station to 350°C, low airflow
- Heat the IC body evenly from above, moving in slow circular motions
- After approximately 60–90 seconds, test if the IC is free using fine-tipped tweezers — it should lift cleanly when all solder has become molten
- Do not lever or force removal — wait until all joints are liquid; forcing a partially-reflowed IC lifts pads
- Remove the IC and place in the discarded components tray

**Step A4.2 — Clean the pads:**
- Apply fresh flux to the pad area
- Use desoldering braid to remove all residual solder — pads must be flat, clean, and evenly tinned before placing the new IC
- Clean with IPA and inspect under magnification — all pads should be visible, flat, and individually separated with no solder bridges

**Step A4.3 — Place the replacement IC:**
- Confirm pin 1 orientation: locate the dot or notch on the replacement IC body (this is pin 1); confirm it matches the pin 1 marker on the PCB silkscreen (triangle, dot, or "1" marking)
- Place IC on pads; align by eye so all pins sit on their respective pads
- Tack one corner pin with the iron to fix alignment — do not solder all pins yet
- Inspect alignment under magnification before proceeding — if misaligned, re-heat the tack pin and reposition

**Step A4.4 — Solder all pins:**
- Solder all remaining pins using fine iron tip, minimal solder, and fresh flux
- Use drag technique on fine-pitch SOIC: touch iron with a small amount of solder across the pin row in a smooth drag motion; fresh flux flow prevents bridging
- Inspect all joints under magnification for bridges before power-on
- Clean flux residue with IPA

**Step A4.5 — Power on and verify:**
- Enable bench supply
- Confirm pixel rows are restored
- If rows are not restored: call instructor — the PCB pads or flex ribbon connection may be contributing to the fault

**Common mistakes at this phase:**
- Incorrect pin 1 orientation — always confirm before tacking; reversing an SOIC display driver destroys it on first power-on
- IC moved during first tack — use a heat-resistant tweezer to hold if needed
- Solder bridges across fine-pitch pins — clean with desoldering braid before power-on; never power on with visible bridges

---

**INSTRUCTOR CHECKPOINT A2 (after reflow or IC replacement, before EEPROM exercise):** Confirm pixel row fault is resolved. Sign off so-8-1-2 on the check-off card. Verify solder joint quality under magnification — all joints should show correct fillet geometry with no bridges.

---

#### Phase A5 — EEPROM Read and Odometer Interpretation (20 minutes)

**Step A5.0 — Ethical declaration form:**
Each student must sign the ethical declaration form before this phase begins. The form states that the student understands the legal prohibition on reducing odometer data and will not perform any write to the odometer section during this exercise.

Instructor framing (deliver to the group before beginning): "This exercise teaches you how to read EEPROM data from a cluster and locate the odometer in the binary file. In a real repair job you need written documentation of the correct mileage before you write anything. Today we are reading only — no write to the odometer section will be performed. Sign the declaration form now."

**Step A5.1 — Identify the EEPROM IC:**
- Power off the cluster completely — bench supply off
- Using the reference card, locate the EEPROM IC on the cluster PCB
- It is a small SOIC-8 package, near the main MCU
- Read the IC part number from the IC top label (magnification if needed)
- Record on job sheet: IC part number, protocol family (93Cxx = SPI/Microwire; 24Cxx = I2C; 25Cxx = SPI)

**Step A5.2 — Configure AsProgrammer:**
- On station laptop, confirm AsProgrammer software is open
- Set IC family and exact type to match the identified EEPROM (select from drop-down menu)
- Confirm the correct IC type before proceeding — selecting the wrong type produces incorrect read data even if the programmer reports success

**Step A5.3 — Attach SOIC-8 clip:**
- Locate pin 1 on the EEPROM IC (dot or notch on IC corner)
- Attach SOIC-8 clip with pin 1 of the clip aligned to pin 1 of the IC
- Confirm clip is fully seated — all 8 pins making contact (slight resistance when pressing clip onto IC is expected and correct)
- Do not power the cluster while the clip is attached — the programmer and clip are for unpowered reading only

**Step A5.4 — Read 1:**
- Cluster must be completely unpowered (bench supply off)
- In AsProgrammer: click "Read"
- Progress bar completes; data populates in the software window
- Save immediately: `ClusterPN_[initials]_READ1_YYYYMMDD.bin`
- Confirm file is saved before proceeding — do not skip this step

**Step A5.5 — Read 2 (verification read):**
- Click "Read" again without adjusting any settings
- Save as: `ClusterPN_[initials]_READ2_YYYYMMDD.bin`
- In AsProgrammer, use the Verify function to compare Read 1 and Read 2: if both reads are byte-for-byte identical, the clip connection is reliable and the data is trustworthy; if they differ, the clip has an intermittent contact — re-seat clip and repeat both reads

**Step A5.6 — Open EEPROM file in hex editor:**
- Open HxD on the station laptop
- Open `ClusterPN_[initials]_READ1_YYYYMMDD.bin`
- Navigate to the odometer byte offset specified on the reference card
- The odometer value is not a plaintext decimal number — it is encoded (commonly BCD, little-endian, or with XOR transform)
- Following the reference card instructions for this specific cluster variant, interpret the bytes at the odometer offset
- Record on job sheet: the raw hex bytes at the odometer offset; your interpreted decimal value; the displayed odometer reading noted during power-on; whether they match

**Discussion prompt for the group:** "Can you see the odometer value just by looking at the hex dump without the reference card? Why not?"
Expected answer: It is encoded, not stored as a readable decimal number. This reinforces why reading EEPROM is only the first step — understanding the data format is equally important.

**Step A5.7 — No write to odometer section:**
Students confirm on their job sheet that no write was performed to the odometer bytes. The purpose of this exercise is to demonstrate reading capability and binary data interpretation.

---

**INSTRUCTOR CHECKPOINT A3 (after EEPROM read and interpretation):** Verify with each student:
- Two identical reads saved with correct naming convention (check filenames on screen)
- File is not zero-byte (a failed read often produces a file of all 0xFF or all 0x00 uniformly — verify the data shows variation)
- Odometer hex bytes correctly identified in hex editor (review on screen)
- Interpretation arithmetic checked
- Ethical declaration form signed

Sign off so-8-1-3 on the check-off card.

---

#### Phase A6 — Extension: EEPROM Write Demonstration (instructor discretion, if >10 minutes remain)

This extension is conducted only if both A2 and A3 checkpoints are complete with substantial time remaining. It is instructional, not assessed.

- Instructor specifies a modification to a non-odometer configuration byte (e.g., a display brightness byte, a units flag byte — never the odometer)
- Student makes the change in HxD hex editor
- Student writes the modified file to the EEPROM using CH341A
- Student reads back (Verify function) to confirm the write succeeded
- Student powers cluster and observes whether the configuration change is visible
- This demonstrates write capability, the verify discipline, and the relationship between EEPROM bytes and cluster behaviour — without touching legally sensitive odometer data

---

## Station B: BCM EEPROM and Coding

### Equipment at Station B

| Item | Quantity | Notes |
|------|----------|-------|
| Original BCM | 1 | Labelled "ORIGINAL BCM — DO NOT MODIFY"; pre-read by instructor |
| Replacement BCM (blank or different vehicle) | 1 | Labelled "REPLACEMENT BCM — STUDENT UNIT" |
| BCM bench harness (pre-wired) | 1 | Connector, power leads, OBD connector — all pins labelled |
| Bench power supply | 1 | Pre-set 12.0V, 5A limit (BCM draws more than cluster) |
| Scan tool with VCDS or equivalent | 1 | Connected to bench harness OBD connector; licence confirmed active |
| Station laptop | 1 | VCDS/equivalent and HxD installed; reference EEPROM files on desktop |
| SOIC-8 clip + CH341A programmer | 1 | |
| Instructor reference EEPROM files | Pre-loaded | REF_BCM_PN_READ1.bin and READ2.bin on laptop desktop |
| VCDS coding guide or adaptation map for this BCM | 1 (laminated) | Specifies which options to configure |
| Coding scenario card | 1 | Instructor-prepared; specifies 2–3 coding changes to apply |
| Student job sheet | 1 per student | Records EEPROM file names, write verification, coding before and after values |
| ESD mat + wrist strap | 1 mat, 1 per student | |
| Multimeter | 1 | For supply voltage verification |

---

### Station B Procedure

#### Phase B1 — Scenario Setup (5 minutes)

**Step B1.1 — Read the scenario card:**
The instructor provides each group with a written scenario card describing:
- Vehicle: e.g., VW Golf Mk5, 2006, 1.9 TDI
- Presenting fault: BCM has failed — central locking inoperative, interior lights not working, BCM not communicating on CAN
- Action required: the original BCM EEPROM has been pre-read and saved (file is on the laptop desktop); a replacement BCM (same part number family) is on the bench; the task is to restore the original BCM's data to the replacement unit and program it correctly

**Step B1.2 — Verbally walk through the six-step replacement workflow:**
Before touching any equipment, each student in the group recites the BCM replacement workflow steps covered in Session 17T (theory). The instructor or station lead confirms the steps are correct.

The six steps: (1) Read original EEPROM; (2) Write to replacement; (3) Connect to bench harness; (4) Confirm CAN communication; (5) Code via scan tool; (6) Verify all functions and clear DTCs.

---

**INSTRUCTOR CHECKPOINT B0:** Ask each student: "Why do we read the original BCM EEPROM before discarding it?" Expected: the original contains vehicle-specific configuration and potentially key transponder data that cannot be recovered from any other source once the BCM is gone. This confirms conceptual understanding before any equipment is used.

---

#### Phase B2 — Read EEPROM from Original BCM (10 minutes)

**Step B2.1 — Locate EEPROM IC on original BCM:**
- Inspect original BCM PCB (BCM is on bench, completely disconnected from power)
- Using the reference photograph in the station pack, locate the EEPROM IC
- Note part number from IC label; confirm it matches the IC type in the reference card

**Step B2.2 — Attach SOIC-8 clip and read:**
- Attach SOIC-8 clip with pin 1 alignment confirmed
- Configure AsProgrammer to correct IC type
- Read EEPROM → save as: `BCM_ORIGINAL_[initials]_READ1_YYYYMMDD.bin`
- Read again without adjusting settings → save as: `BCM_ORIGINAL_[initials]_READ2_YYYYMMDD.bin`
- Verify: use AsProgrammer Verify function to compare both reads — must be byte-for-byte identical before proceeding
- Record result on job sheet: reads matched? Yes/No

**Step B2.3 — Compare student read against instructor reference:**
- Open student Read 1 and instructor reference REF_BCM_PN_READ1.bin in HxD
- Use HxD Compare function (or view side by side)
- Both files should be byte-for-byte identical — this confirms the student's clip read is clean and the IC is not corrupted
- Record: any differences observed? (Expected: no differences)

If differences are found between the student's read and the instructor reference, this indicates a clip contact issue — not EEPROM corruption. Re-seat the clip and repeat.

---

#### Phase B3 — Write EEPROM Data to Replacement BCM (10 minutes)

**Step B3.1 — Inspect replacement BCM EEPROM before writing:**
- Connect SOIC-8 clip to EEPROM IC on replacement BCM
- Read replacement BCM EEPROM → save as: `BCM_REPLACEMENT_BEFORE_[initials]_YYYYMMDD.bin`
- Open in HxD — confirm that it is either blank (all 0xFF) or clearly different from the original (different vehicle data)
- Record on job sheet: replacement BCM EEPROM state before write

**Step B3.2 — Write original data to replacement BCM:**
- In AsProgrammer: open `BCM_ORIGINAL_[initials]_READ1_YYYYMMDD.bin`
- Confirm correct IC type is still selected — do not change settings between operations
- Click "Write"
- Wait for write to complete — do not interrupt, disconnect, or remove the clip during the write operation
- When write completes: click "Verify" — programmer reads back the written data and compares it byte-for-byte to the source file
- Verify result must show 100% match — if verify fails, repeat the write; if fails a second time, the EEPROM IC on the replacement BCM may be suspect; call the instructor

**Step B3.3 — Confirm write with manual read-back:**
- Click "Read" on replacement BCM EEPROM
- Save as: `BCM_REPLACEMENT_AFTER_[initials]_YYYYMMDD.bin`
- Open in HxD alongside original read — spot-check 10 bytes at three different offsets manually
- Confirm match: record on job sheet

---

**INSTRUCTOR CHECKPOINT B1 (before connecting to bench harness):** Review with each group:
- Student's read of original BCM matches instructor reference read (no differences in HxD comparison)
- Write completed and programmer Verify step was run and confirmed 100% match
- Read-back of replacement BCM matches the source file
- All three files saved with correct naming convention (check filenames on screen)

Do not proceed to bench harness connection until this checkpoint is cleared. A write that has not been verified has unknown integrity.

---

#### Phase B4 — Connect Replacement BCM to Bench Harness and Confirm Communication (5 minutes)

**Step B4.1 — Connect replacement BCM to bench harness:**
- Identify the main connector on the replacement BCM
- Connect bench harness — large multipin connector
- Connect power: supply positive to BCM Battery supply pin (Terminal 30); supply negative to BCM ground pin; refer to bench harness label for pin assignments
- CAN-H and CAN-L from bench harness are already routed to the OBD2 interface — confirm connectors are seated

**Step B4.2 — Power on and establish scan tool communication:**
- Enable bench supply (12.0V)
- Open VCDS or equivalent on station laptop
- Select the BCM module address (platform-specific — listed in the station scenario card)
- Attempt to communicate: the scan tool should detect the BCM and display its module identification (part number, software version, hardware version)
- Allow 10–15 seconds for BCM boot sequence before concluding it is not communicating

**If communication fails — diagnostic steps:**
1. Measure Terminal 30 supply voltage at the BCM supply pin using a multimeter — should be 12.0V
2. Measure ground continuity at the BCM ground pin — should read <0.5Ω to bench negative
3. Confirm CAN-H and CAN-L are connected to the correct harness pins (refer to pinout diagram)
4. If supply and ground are correct and BCM is still not communicating: the EEPROM write may have produced corrupt data; re-read the replacement BCM EEPROM and compare to the source file; call the instructor

**Step B4.3 — Confirm VIN in controller identification:**
- In VCDS/equivalent: select Controller Info or Identification
- Confirm the VIN field shown in the BCM identification data matches the expected VIN from the original BCM
- This confirms the EEPROM data was written correctly — the replacement BCM now identifies itself as belonging to the correct vehicle
- Record on job sheet: VIN shown in BCM identification; matches expected? Yes/No

---

**INSTRUCTOR CHECKPOINT B2 (after establishing communication):** Confirm scan tool shows BCM communicating, no unexplained communication U-codes, and VIN field matches expected. Every group must establish confirmed communication before proceeding to variant coding. Coding applied to a BCM that is not fully communicating has unknown effect.

---

#### Phase B5 — Variant Coding (15 minutes)

Variant coding configures the BCM software to match the specific options fitted to the vehicle. Even after EEPROM cloning (which copies learned data), variant coding must be verified and updated where the scenario card specifies changes.

**Step B5.1 — Access BCM coding screen:**
- In VCDS: Select BCM → Coding → Long Coding Helper
- In ODIS or equivalent: Select BCM → Adaptations or Coding

**Step B5.2 — Record current coding (before making any changes):**
- Copy the full current coding string (hex string or adaptation channel values) into the job sheet "Before Coding" column
- This is the baseline record — essential for rollback if needed, and essential for confirming what changed after coding is applied

**Step B5.3 — Apply coding changes specified on scenario card:**
The instructor scenario card specifies 2–3 coding changes to apply. Options may include:

- Enable or disable DRL (daytime running lights)
- Set rain sensor sensitivity level (disable if not fitted; set to correct sensitivity level if fitted)
- Enable comfort closing (windows and sunroof close via long press of lock button)
- Set auto-lock speed (vehicle locks automatically at X km/h)
- Enable or disable heated seat function
- Enable or disable tow bar trailer stability function

For each change:
- Locate the relevant byte and bit in the Long Coding Helper (VCDS labels each field with a description)
- Record the current value in the "Before" column on the job sheet
- Apply the new value from the scenario card
- Record the new value in the "After" column

**Step B5.4 — Write coding:**
- In VCDS/equivalent: click "Do It!" or "Apply" to write the new coding to the BCM
- Confirm no error message is shown (an error during write may indicate security access was not completed — see common mistakes table)
- Power cycle the bench supply: switch off for 5 seconds, then back on

**Step B5.5 — Verify coding was stored:**
- Re-enter BCM in VCDS/equivalent
- Return to coding screen
- Read the current coding
- Confirm that each of the specified coding changes is present in the readback coding string
- Record on job sheet: readback coding string; each change confirmed present? Yes/No

---

**INSTRUCTOR CHECKPOINT B3 (after variant coding):** Review job sheet with each group — confirm:
- Original coding values were recorded before any change was made
- All specified coding changes applied and confirmed in coding readback
- No error messages during the write operation
- Basic settings performed if prompted by the scan tool

---

#### Phase B6 — Verify BCM Operation and Clear DTCs (5 minutes)

**Step B6.1 — Function verification via scan tool output tests:**
- In VCDS/equivalent, navigate to Output Tests for the BCM module
- Command each available output function:
  - Central locking: Lock command → listen for relay click in bench harness; Unlock command → listen for relay click
  - Interior light relay: command ON; command OFF
  - Horn relay: command ON briefly (1 second maximum); command OFF
- Record on job sheet: each function tested; observed behaviour (relay click, LED indicator, or no response)
- Note: not all functions will produce a visible response on a bench harness without full vehicle loads connected; what is confirmed is that the BCM is outputting the command signal, not that a physical actuator activated

**Step B6.2 — Read and clear DTCs:**
- Read all stored and pending DTCs from the BCM
- Expected: some sensor-absent faults will be present because not all vehicle inputs are connected on the bench harness; these are normal in this context
- Unexpected: coding-related faults (e.g., "Option coded but hardware signal absent") should be reviewed — they may indicate a coding parameter was set incorrectly
- Clear all DTCs
- Read DTCs again — confirm no new faults have been generated by the coding process
- Record on job sheet: DTCs found before clear; DTCs remaining after clear

---

**INSTRUCTOR CHECKPOINT B4 (final checkpoint — Station B):** Sign off so-8-2-2 and so-8-2-3 on the check-off card after confirming:
- BCM communicating with correct VIN
- Coding changes applied and verified on readback
- Function output test completed with results recorded
- DTC read and clear performed; no unexplained faults remaining

---

## Rotation (0:47 to 0:50)

**Departing students confirm before leaving their station:**
- [ ] All files saved with correct naming convention (check filenames — do not rely on memory)
- [ ] Job sheet progress up to current checkpoint recorded
- [ ] Station left tidy — tools returned to tray, no loose solder on bench mat, no open flux pens
- [ ] Bench supply left at 12V; do not adjust supply settings for the incoming group

**Arriving students at each station:**
- [ ] Read the station setup card before touching any equipment
- [ ] Confirm bench supply is at 12V before connecting anything
- [ ] Do not assume previous group's work is correct — verify from Checkpoint A0 or B0 respectively

**Station A handover note:** If the previous group completed the pixel row repair, arriving students should power on and confirm the repair is still holding before proceeding to EEPROM work.

**Station B handover note:** If the previous group completed EEPROM write and coding, arriving students should read the replacement BCM EEPROM and independently confirm it matches the expected data before proceeding to verify coding.

---

## Debrief (Joint — 1:25 to 1:35)

Bring all students together at the end of the session. Instructor leads; students respond.

**Discussion questions:**

1. "Station A — what was the repair decision point? When did you decide to replace the IC rather than just reflow?"
Expected: reflow was always first; IC replacement only when reflow did not restore the display; the decision is evidence-based, not preference-based.

2. "What would have happened if someone reversed the replacement display driver IC by 180 degrees before soldering?"
Expected: all outputs would be connected to wrong pins; likely no display output and possible IC damage from reversed polarity on power pins; this reinforces pin 1 confirmation as mandatory, not optional.

3. "Station B — what is in that EEPROM binary file that you cannot recover if the original BCM is discarded without reading it first?"
Expected: vehicle configuration, coded options, paired key transponder data, possibly security codes — none of this can be regenerated without the original BCM data; there is no factory reset option that restores a vehicle's specific coded profile.

4. "A customer brings you a car. The previous workshop replaced the BCM but 'just plugged in a new one.' What problems might that vehicle have?"
Expected: features not coded correctly, potentially immobilizer issues causing no-start, wrong market variant settings (e.g., wrong measurement units, wrong DRL behaviour), no remote key function.

5. "At what point in a BCM replacement job does the odometer mirror value become relevant?"
Expected: when writing the replacement BCM EEPROM from the original — the mileage mirror value carried in the original BCM data is also restored; this is correct and legitimate because it matches the cluster's mileage record and is the vehicle's documented mileage.

**Key takeaways to close:**
- Read before you write. Always. Twice. Verify after writing.
- Pixel row faults are economic wins — the repair cost is almost nothing; the skill value is significant
- BCM replacement is not complete until variant coding is verified — fit and return without scan tool confirmation is incomplete work
- Documentation is professional practice — file naming, job sheet completion, and checkpoint sign-offs protect both the student and the customer

---

## Common Problems Reference Table

| Problem | Likely Cause | Resolution |
|---------|-------------|-----------|
| Pixel row fault not restored after reflow | IC pins not fully reflowed; flux insufficient; or IC is internally failed | Re-apply flux, reflow again with more deliberate dwell time per pin; if no improvement, proceed to IC replacement |
| LCD glass cracked during hot air rework | Hot air directed at glass; temperature too high; nozzle too close | Replace display glass if donor available; document incident and inform instructor; do not continue with a cracked glass |
| SOIC-8 clip read fails — software error | Clip contact unreliable; MCU holding bus signals active | Re-seat clip; clean IC pins with IPA; try again; if still failing, try desoldering IC for off-circuit read |
| Read 1 and Read 2 do not match | Clip contact intermittent | Re-seat clip; re-clean IC pins; repeat both reads until two consecutive identical reads are obtained |
| BCM does not communicate after EEPROM write | EEPROM write was corrupt; hardware revision mismatch; power supply or ground issue | Verify supply voltage and ground continuity; re-read BCM EEPROM and compare to source file; call instructor |
| VCDS coding change not retained after power cycle | Security access not unlocked before coding was attempted | Re-enter security access code in VCDS; re-apply coding; verify retention |
| Variant coding field not visible in Long Coding Helper | BCM firmware version does not support this option; or station BCM does not have this feature's hardware | Note limitation on job sheet; instructor explains firmware-level differences between hardware variants |
| CH341A "Write Failed" error | EEPROM write-protect pin may be active; IC may be in write-protect mode | Check IC write-protect (WP) pin; if tied high, identify pull-up resistor and address; call instructor |
| Solder bridge on IC pins after replacement | Excess solder; insufficient flux | Clean with desoldering braid; re-apply flux; inspect under magnification; do not power on with visible bridge |

---

## Equipment List — Full Session

### Station A (per station, supports 2 students)

| Item | Specification | Quantity |
|------|--------------|----------|
| LCD instrument cluster with pixel row fault | Genuine fault or instructor-induced; confirmed stable before session | 1 |
| Bench power supply | 0–30V, 0–5A, current limitable, digital display | 1 |
| Bench harness for cluster | Vehicle-specific connector wired to supply and ignition signal | 1 |
| Temperature-controlled soldering iron | Fine tip, 200–400°C adjustable | 1 |
| Hot air rework station | 100–450°C adjustable, variable airflow | 1 |
| Soldering iron fine tips | 0.4mm chisel and conical — 2 spares | 2 |
| No-clean flux pen | Kester 186 or equivalent | 1 |
| Fine solder | 0.5mm 60/40 or SAC305 | 1 reel |
| Desoldering braid | 2mm width, pre-fluxed | 1 |
| IPA spray (99%) | | 1 |
| Cotton swabs | | 1 bag |
| SOIC-8 clip (150mil) | Pomona or equivalent | 1 |
| CH341A programmer | USB, with SOIC-8 cable | 1 |
| Station laptop | Windows 10+; AsProgrammer and HxD installed | 1 |
| Replacement display driver IC | Same package and part number as cluster specimen | 2 spares |
| Cluster schematic / IC reference card | Laminated, cluster-specific | 1 |
| Cluster EEPROM reference card | Odometer offset, IC type, encoding format | 1 per student |
| Ethical declaration form | One per student | 1 per student |
| Student job sheet | One per student | 1 per student |
| Multimeter | Auto-ranging | 1 |
| Magnifying loupe | 10x | 1 |
| ESD mat (600mm x 400mm minimum) | | 1 |
| ESD wrist strap | | 1 per student |

### Station B (per station, supports 2 students)

| Item | Specification | Quantity |
|------|--------------|----------|
| Original BCM | Known-good EEPROM; pre-read by instructor | 1 |
| Replacement BCM | Same part number and hardware revision; blank or different vehicle | 1 |
| BCM bench harness | Vehicle-specific multipin connector; power leads; OBD connector — all labelled | 1 |
| Bench power supply | 0–30V, 0–5A; current limit 5A for BCM | 1 |
| Scan tool (VCDS or equivalent) | Licensed, current version; confirmed working with bench harness before session | 1 |
| Station laptop | Windows 10+; VCDS and HxD installed; reference EEPROM files pre-loaded on desktop | 1 |
| SOIC-8 clip + CH341A | Same specification as Station A | 1 set |
| BCM connector pinout reference | Printed laminated card; shows Terminal 30, Terminal 15, ground, CAN-H, CAN-L pin numbers | 1 |
| VCDS coding guide for this BCM | Printed laminated; shows Long Coding Helper byte fields and descriptions | 1 |
| Coding scenario card | Instructor-prepared; specifies vehicle options and coding changes to apply | 1 per group |
| Instructor reference EEPROM files | REF_BCM_PN_READ1.bin and READ2.bin pre-loaded on laptop desktop | Pre-loaded |
| Student job sheet | One per student | 1 per student |
| Multimeter | Auto-ranging | 1 |
| ESD mat + wrist strap | | 1 mat, 1 per student |

---

## Student Check-Off Card

*To be completed by student and signed by instructor at each checkpoint. Submit at end of session.*

**Student Name:** ______________________________
**Date:** ______________________________
**Group (A first / B first):** ______________________________

| Checkpoint | Description | Student Confirms | Instructor Initials |
|------------|-------------|-----------------|-------------------|
| A0 | Fault pattern described accurately before any rework | [ ] | |
| A1 | Reflow completed; joint quality inspected under magnification; power-on result recorded | [ ] | |
| A2 | Pixel row fault confirmed resolved; so-8-1-2 signed off | [ ] | |
| A3 | Two identical EEPROM reads saved with correct naming; odometer bytes identified and interpreted; ethical declaration form signed; so-8-1-3 signed off | [ ] | |
| B0 | BCM replacement workflow recited correctly before touching equipment | [ ] | |
| B1 | Student read matches instructor reference; write completed; programmer verify confirmed 100% match; all files correctly named | [ ] | |
| B2 | BCM communicates on bench harness; VIN confirmed in controller identification | [ ] | |
| B3 | Coding changes applied per scenario card; coding verified on readback; basic settings performed if required | [ ] | |
| B4 | Output tests performed with results recorded; DTCs read, cleared, and re-read; so-8-2-2 and so-8-2-3 signed off | [ ] | |

---

## Instructor Notes

**Managing LCD temperature risk:**
This is the primary safety risk of Station A. Before each group starts Phase A3, verbally remind them: "Hot air goes on the IC and PCB. Not the glass." Walk Station A during Phase A3 rework and observe technique. If a student holds the hot air nozzle stationary near the glass edge, intervene immediately. A cracked LCD renders the cluster unusable for this exercise and is difficult to replace mid-session.

**Inducing the pixel row fault reliably:**
If a genuine faulted cluster is not available, the fault can be induced by partially lifting one display driver IC pin using a fine iron tip at approximately 200°C — apply slight upward pressure on the pin with minimal heat until the joint cracks slightly. Allow to cool. Power on to confirm rows are dead. Prepare the night before the session and confirm the fault is stable; do not induce the fault on the day of the session — you need time to verify stability before students arrive. An unstable fault (appears and disappears) is harder for students to diagnose than a consistent fault.

**BCM hardware revision matching:**
The most common failure point at Station B is a hardware revision mismatch between original and replacement BCM — this causes communication failure after EEPROM write even if the write was correct. Source replacement BCMs that are the same hardware revision as the original. The revision is usually printed on a sticker on the BCM housing or stamped on the PCB. If the revision differs, note this in the station setup card and advise students in advance — it becomes a teaching point about why revision matching matters in real practice.

**Managing two parallel stations:**
Appoint one confident student per station as station lead to manage procedure flow and flag checkpoints. This allows the instructor to circulate rather than being anchored to one station. Brief station leads before the session starts on their role: manage the procedure, call checkpoints when ready, do not perform rework on behalf of other students.

**Debrief question "what happens if you don't do two reads?"**
This sometimes generates debate: "one read is fine if the programmer completed without error." Response: the programmer completing without error confirms that the programmer completed a read operation — it does not confirm that every byte was correctly transferred. Bit errors from intermittent clip contact, bus contention from an MCU that is not fully powered down, and partial reads that pad with 0xFF can all produce a read that reports success but contains incorrect bytes. Two reads that are byte-for-byte identical provide the only confirmation of data integrity at this level.

---

*Module 8 | Day 17 Hands-On | ECUHR | v1.0 | 2026-02-18*
