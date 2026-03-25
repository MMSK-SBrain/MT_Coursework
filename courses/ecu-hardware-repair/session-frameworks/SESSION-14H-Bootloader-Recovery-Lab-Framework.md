# SESSION-14H: Variant Coding, Adaptation & Boot Mode Recovery Lab
## Hands-On Session | Day 14 | Module 6: ECU Programming & Bootloader

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 6 — ECU Programming & Bootloader
**Day:** 14 | **Session Type:** Hands-On Workshop
**Duration:** 90 minutes
**CO Alignment:** co-3

---

## Session Outcomes

| SO Code | Outcome Statement | Bloom's Level |
|---|---|---|
| so-6-3-2 | Perform a variant coding procedure on a sample ECU using VCDS or equivalent tool and verify coding changes | Apply |
| so-6-3-3 | Execute an adaptation reset on a sample ECU and verify the ECU accepts the new learned values | Apply |
| so-6-4-2 | Identify JTAG/BDM/SPI access pins on an ECU PCB using datasheet and schematic research | Apply |
| so-6-4-3 | Connect boot mode programmer to a sample ECU and perform a direct FLASH read via SPI or BDM interface | Apply |
| so-6-5-2 | Recover a bricked sample ECU using boot mode programming to restore a known-good firmware file | Apply |

---

## Assessment Alignment

| SO Code | Checkpoint | Assessment Method | Pass Criterion |
|---|---|---|---|
| so-6-3-2 | Checkpoint 1A | Instructor observation + screenshot | Student executes correct coding change, takes before/after screenshots, coding accepted by ECU without error |
| so-6-3-3 | Checkpoint 1B | Instructor observation | Adaptation channel reset completed; ECU confirms acceptance (no error DTC after reset) |
| so-6-4-2 | Checkpoint 2 — GATE | Instructor inspection of annotated diagram | Student correctly identifies and marks boot access pins on the PCB diagram before any cable is connected; instructor signs off before proceeding |
| so-6-4-3 | Checkpoint 3 | Instructor observation + file verification | SPI or BDM read completes without error; file size matches expected FLASH size; first bytes show recognisable firmware structure (not 0xFF blank or random noise) |
| so-6-5-2 | Checkpoint 4 | Instructor observation + scan tool confirmation | Bricked ECU re-establishes OBD communication after boot mode restore; scan tool reads ECU identity successfully |

**Gating rule:** Checkpoint 2 is a mandatory GATE. No student is permitted to connect boot mode hardware to any ECU until the instructor has verified the pin identification diagram and signed the check-off card. Connecting boot mode hardware to incorrect pins can permanently damage the MCU. This gate is non-negotiable.

---

## Session Purpose and Context

This session is the practical culmination of Module 6 — and arguably the single most commercially valuable practical skill in the entire course. The ability to recover a bricked ECU via boot mode separates a basic workshop (which replaces the ECU) from a specialist workshop (which recovers it for a fraction of the cost).

The session runs four stations in fixed sequence. Stations 1 and 2 build toward the module's core theme: even offline coding operations carry risk when sessions drop, and understanding the full programming stack — from variant coding at the top to boot mode recovery at the hardware level — gives the technician command of the entire ECU programming domain.

**What this session requires students to do before arriving:**
- Completed Session 14T — bootloader architecture, JTAG/BDM/SPI interfaces, bricked ECU diagnosis
- Completed Session 13H — bench programming workflow, naming convention, VCDS or equivalent basics
- Download reference: MCU datasheet for the sample ECU used in Stations 2 and 3 (posted on LMS the evening of Day 13)

---

## Station Overview

| Station | Activity | Duration | Outcome |
|---|---|---|---|
| 1 | Variant Coding and Adaptation Reset | 20 min | so-6-3-2, so-6-3-3 |
| 2 | Boot Mode Pin Identification (GATE) | 15 min | so-6-4-2 |
| 3 | SPI or BDM FLASH Read | 25 min | so-6-4-3 |
| 4 | Bricked ECU Recovery | 25 min | so-6-5-2 |
| Debrief | Full group | 5 min | — |

---

## Equipment List — Per Workstation

| Item | Specification | Notes |
|---|---|---|
| Laptop / workshop PC | Windows 10/11; mains-powered; sleep disabled | Same setup as Session 13H; confirm settings before session |
| VCDS cable (or equivalent OBD diagnostic interface) | Compatible with sample ECU — VAG-specific or appropriate for platform in use | Pre-verified with sample ECU before session |
| Diagnostic software | VCDS (or equivalent: Autel, Launch, iCarSoft — platform-dependent) | Licensed and tested; student login or instructor login as per facility policy |
| Sample ECU — Station 1 | Bench-mounted ECU, wired for OBD/bench communication | Must respond to scan tool and support variant coding and adaptation on at least two channels |
| Bench power supply | 13.5–14.2V regulated; 5A minimum | Same specification as Session 13H |
| Sample ECU — Station 2/3 | Disassembled ECU for physical pin identification; lid removed | Should contain identifiable external FLASH chip (SPI) or BDM header; MCU type confirmed before session |
| MCU datasheet | Printed A4; key pages highlighted: pin list, boot mode trigger pin, package diagram | Or: accessible on laptop — confirm internet access OR pre-downloaded PDF |
| SPI programmer | CH341A + SOIC-8 clip (or RT809H, T48, or similar) | Tested and driver-installed; confirm CH341A drivers installed if using Windows 11 |
| SPI programming software | AsProgrammer (Windows) or flashrom (cross-platform) | Installed and tested; FLASH chip type pre-identified and confirmed to be in software database |
| BDM programmer (if BDM station) | K-TAG or BDMKIT-compatible interface with BDM cable | Alternative to SPI if sample ECU has BDM header and no accessible external FLASH |
| Sample ECU — Station 4 (bricked unit) | Pre-prepared bricked ECU — secondary bootloader corrupted; no OBD response | Instructor to prepare by performing an interrupted write on a donor unit the day before |
| Known-good firmware file | Correct .bin for the bricked ECU type | Pre-loaded on workstation desktop; named RECOVERY_[ECU-TYPE]_[DATE].bin |
| Scan tool | For verification after recovery — must connect to bricked ECU type | Confirmed to communicate with the ECU after successful recovery |
| Check-off card | Printed per student | Checkpoint gates 1A, 1B, 2, 3, 4 with signature lines |
| Safety glasses | For all hands-on work | Required during SPI clip connection — spring clips under tension |

---

## Pre-Session Instructor Preparation

**Day 13 evening / Day 14 morning:**

1. **Prepare the bricked ECU for Station 4:**
   - Take a donor ECU (same type as the programming units from Session 13H)
   - Connect to programmer and initiate a write
   - At approximately 40–60% completion, interrupt the write by disconnecting the USB cable
   - Confirm the ECU no longer responds to OBD scan tool (no reply on CAN or K-Line)
   - If ECU still responds: repeat the interrupt at a different percentage; some ECU types require the interrupt to fall exactly within the secondary bootloader sector
   - Confirm the bricked ECU responds correctly via SPI or BDM boot mode before the session — if boot mode does not work on the bricked unit, prepare a different donor

2. **Station 1 setup:**
   - Wire sample ECU to bench supply and confirm OBD/diagnostic communication works
   - Identify two coding changes to demonstrate/assign: one feature enable (e.g., engage lighting option, seatbelt reminder tone) and one adaptation channel (e.g., throttle body adaptation or SAS reset)
   - Write the "before" coding values on the whiteboard — students should be able to confirm what they found matches before making any change

3. **Station 2/3 setup:**
   - Remove the lid from the sample ECU
   - Confirm the FLASH chip type and that it appears in the SPI programmer's supported chip list
   - Perform a test read yourself to confirm the SPI clip setup works and the file is valid
   - Prepare the annotated PCB diagram worksheet — outline drawing showing the ECU PCB with major components labelled (MCU, FLASH chip, connector, power section) but boot access points left blank for students to identify

4. **File preparation:**
   - Load the known-good recovery .bin file on all workstations (Station 4 desktop)
   - Confirm the file is the correct version for the specific bricked ECU units — wrong file version = second brick

**Day 14, before students arrive:**
- Station 1: ECU powered, scan tool connected, software open
- Station 2: ECU (lid removed), MCU datasheet, blank annotated diagram worksheets, pencils
- Station 3: SPI programmer, SOIC clip, SPI software open; CH341A connected to USB but not connected to ECU
- Station 4: Bricked ECU on bench, power supply connected but NOT powered on; programmer ready; recovery file on desktop; scan tool ready

---

## Station 1: Variant Coding and Adaptation Reset (20 minutes)

### Overview

Students perform two operations on a bench-mounted ECU using the diagnostic software: a variant coding change (enable a feature), and an adaptation reset (clear a learned value channel). Both operations must be documented before and after, and verified by the ECU accepting the change without error DTCs.

### Station 1 Procedure

**1.1 — Connect and establish communication (3 minutes)**

1. Confirm the ECU is powered at the bench supply (13.5–14.2V confirmed on voltmeter)
2. Connect the VCDS cable (or equivalent interface) to the ECU's OBD/CAN connector adapter
3. Open diagnostic software and connect to the ECU — confirm ECU identity is displayed correctly (part number, hardware version, software version)
4. Take a screenshot of the ECU identification screen — this is the baseline record

**1.2 — Variant coding change (8 minutes)**

5. Navigate to the ECU's coding screen in the diagnostic software
6. Record the current full coding string/value in the check-off card (write it down, not just remember it)
7. Instructor nominates a specific coding bit to change — make only this change; do not explore other bits
8. Apply the new coding and confirm the ECU accepts it (software reports coding accepted; no new DTCs appear)
9. Take a screenshot of the new coding screen
10. Verify the change is live: if the feature involves a function visible in live data, confirm the expected change in live data output

> **Checkpoint 1A:** Instructor inspects check-off card (before and after coding strings recorded), screenshots, and confirms no new DTCs. Sign off before proceeding to 1.3.

**1.3 — Adaptation reset (7 minutes)**

11. Navigate to the ECU's adaptation channels screen
12. Identify the nominated adaptation channel (instructor specifies — e.g., throttle body, SAS, or transmission adaptation)
13. Record the current adaptation value in the check-off card
14. Execute the adaptation reset procedure: follow the software's guided steps (some adaptations require specific engine state — instructor to advise on the bench workaround if needed)
15. Confirm the adaptation channel shows the reset value (typically 0 or a default value)
16. Confirm no new DTCs appear after reset

> **Checkpoint 1B:** Instructor confirms adaptation value shown is the post-reset value and no DTCs are present. Sign off and move to Station 2.

### Station 1 Common Problems

| Symptom | Likely Cause | Resolution |
|---|---|---|
| "Coding rejected — security access required" | Coding level requires higher access (login or security seed) | Instructor provides correct login code for this ECU type |
| New DTC appears after coding change | Wrong bit modified; incompatible option for this ECU variant | Restore original coding from check-off card record; discuss with instructor |
| Adaptation "conditions not met" error | Adaptation requires specific ECU state (e.g., ignition cycle, engine temp) | Instructor advises bench workaround or documents as expected limitation |
| Scan tool loses communication mid-coding | USB connection interruption or software timeout | Do NOT cycle ECU power immediately; check scan tool connection first; if communication not recovered in 30 seconds, cycle power and reconnect; check if coding was saved before dropout |

---

## Station 2: Boot Mode Pin Identification — GATE (15 minutes)

### Overview

Students use the MCU datasheet to identify which physical pins on the ECU PCB are used to trigger boot mode for the specific MCU architecture. This is a research and identification task — no tools are connected to any ECU until Checkpoint 2 is signed off.

### Station 2 Procedure

**2.1 — MCU identification (3 minutes)**

1. Examine the MCU package on the disassembled ECU
2. Read the part number markings (top of IC package) — if laser-etched, use the magnifier
3. Confirm the manufacturer and MCU family from the markings
4. Match to the datasheet provided (or locate it on the laptop)

**2.2 — Boot mode trigger pin identification (8 minutes)**

5. Open the MCU datasheet
6. Locate the boot mode section (search: "boot mode", "BDM", "background debug", "BOOT0", depending on MCU family)
7. Identify: which specific pins trigger boot mode (boot entry pin name, boot mode condition — high or low, active at power-on)
8. Locate the pin list / package diagram in the datasheet — note the physical pin number or position for the boot trigger pin
9. On the blank annotated PCB diagram worksheet: mark the MCU with the identified boot entry pin position
10. If a BDM header or SPI FLASH chip is present: identify its location on the PCB and mark it on the worksheet
11. For SPI FLASH access: identify from the FLASH chip datasheet the CS (chip select), MOSI, MISO, SCK pin positions on the SOIC-8 package

> **Checkpoint 2 (GATE):** Present the annotated worksheet to the instructor. Instructor verifies:
> - Correct MCU family identified
> - Boot mode trigger pin correctly named and located
> - Access method (BDM header or SPI FLASH chip) correctly identified and marked
> - Instructor initials the check-off card — **equipment for Station 3 is only issued after this sign-off**

### Station 2 Instructor Notes

This checkpoint is critical. A misidentified pin can apply a voltage level to a pin that was not designed to receive it. On some MCU architectures, the boot mode pin is adjacent to a supply rail pin. Incorrect clip or probe contact on the supply pin during SPI in-circuit programming will damage the programmer and potentially the MCU.

If a student misidentifies the pins, do not simply correct them. Ask them to return to the datasheet and find the error themselves — guided questioning is better than correction at this point, and the student will remember the correct method more reliably.

---

## Station 3: SPI FLASH Read via In-Circuit Clip (25 minutes)

### Overview

Using the pins identified in Station 2, students connect a CH341A (or equivalent SPI programmer) to the external FLASH chip on the ECU PCB using a SOIC-8 in-circuit clip. They perform a complete read of the FLASH contents and verify the file.

### Safety Note — SPI In-Circuit Programming

**BEFORE connecting the clip:**
- The ECU power supply MUST be OFF — the bench supply disconnected from the ECU before applying the SPI clip
- The MCU may need to be held in reset during SPI access (instructor to advise for specific ECU type — some require reset hold, others do not)
- The SPI programmer provides its own VCC to the FLASH chip during programming — if the ECU supply is still active, both VCC sources conflict and neither will operate correctly; this can damage the FLASH chip or the programmer

### Station 3 Procedure

**3.1 — Confirm ECU is powered OFF (2 minutes)**

1. Confirm the bench power supply is disconnected from the ECU — measure at the ECU power pins with a voltmeter; must read 0V
2. If the MCU requires reset hold: instructor advises the specific method for this ECU; apply as directed before clip connection

**3.2 — Apply SOIC-8 clip (5 minutes)**

3. Identify the SOIC-8 FLASH chip on the PCB (using the worksheet from Station 2)
4. Note the chip orientation — Pin 1 is marked by a dot or notch on the chip package; align the clip's Pin 1 to the chip's Pin 1 (check clip documentation for Pin 1 position on the clip itself)
5. Open the clip fully, position over the FLASH chip carefully — the clip must contact ALL 8 pins; check visually from multiple angles
6. Release the clip onto the chip pins
7. Verify seating: gently tug the clip cable; it should be firmly held; each pin of the clip should be visibly in contact with the corresponding chip pin; use the magnifier to inspect from the side

**3.3 — Connect programmer to laptop (2 minutes)**

8. Connect the SOIC-8 clip cable to the CH341A programmer
9. Connect the CH341A USB cable to the laptop
10. Open AsProgrammer (or equivalent) — confirm the CH341A is detected (appears in device manager or software connection indicator shows green)

**3.4 — Select FLASH chip type (3 minutes)**

11. In the SPI programming software: select chip manufacturer and model matching the FLASH chip identified in Station 2
12. Confirm the chip parameters shown (memory size, page size, voltage) match the datasheet for the identified chip
13. If in doubt: ask instructor before proceeding

**3.5 — Perform FLASH read (10 minutes)**

14. Click "Read" in the SPI programmer software
15. Monitor the progress indicator — read should proceed smoothly; note the start time
16. If the read stalls or fails immediately: stop; check clip seating (most failures are clip contact failures, not software failures)
17. When read completes: note the file size shown in the software buffer
18. Compare file size to the expected FLASH size from the datasheet (e.g., 2MB FLASH → 2,097,152 bytes / 2,048 KB)
19. Save the file: name it using the naming convention from Session 13T — use ECU identifier and date; save to the USB drive AND to the workstation backup folder

**3.6 — Verify file (3 minutes)**

20. Open HxD (or AsProgrammer's hex view)
21. Inspect the first 256 bytes of the file — it should show recognisable firmware structure (vector table addresses, or data consistent with binary code); it should NOT show all 0xFF (blank) or random repeating patterns
22. Confirm the file does not show all 0x00 (communication failure — reads as zero when pins are not contacted)
23. Record findings in the check-off card: file size, first bytes summary (firmware structure / blank / communication fault)

> **Checkpoint 3:** Instructor reviews: file saved correctly, size matches expected FLASH size, first bytes show firmware structure (not blank, not zero). Instructor initials check-off card. Move to Station 4.

### Station 3 Common Problems

| Symptom | Likely Cause | Resolution |
|---|---|---|
| "Device not found" / no chip detected | Clip not seated; wrong chip type selected; ECU supply still active | Check ECU powered off first; re-seat clip; try a different chip type if physically similar IC |
| Read result is all 0xFF | Clip positioned on blank chip (wrong component); chip blank after erase | Verify chip identity on PCB; if chip is confirmed correct, this may indicate the chip was erased previously |
| Read result is all 0x00 | Clip is not making contact — pins not connected | Remove clip, re-inspect chip pins for contamination or damage; re-apply clip |
| Read completes but wrong file size | Wrong chip type selected in software | Check datasheet; reselect correct chip type; re-read |
| Clip keeps slipping off | Chip surface has conformal coating | Use IPA to clean chip top before clipping; conformal coating causes slip |

---

## Station 4: Bricked ECU Recovery (25 minutes)

### Overview

Students are presented with a pre-bricked ECU (secondary bootloader corrupted, no OBD communication possible) and a known-good firmware file. Using boot mode programming (SPI or BDM, depending on the ECU architecture and equipment available), they restore the firmware and verify communication is re-established.

### Safety Note — Boot Mode Write

A write operation to an ECU via boot mode is a permanent, irreversible operation on the written sectors. Writing an incorrect firmware file in boot mode can produce an unrecoverable ECU. The instructor must verify the correct file is selected before the write is initiated.

### Station 4 Procedure

**4.1 — Confirm the brick (5 minutes)**

1. Connect the bricked ECU to the bench power supply — confirm correct voltage (13.5–14.2V)
2. Connect a scan tool to the ECU's OBD/CAN adapter
3. Attempt to establish communication: confirm the ECU does NOT respond (expected — it is bricked)
4. Connect an oscilloscope to the CAN-H / CAN-L pins — observe signal activity at power-on
5. Record in check-off card: communication status (no response), any oscilloscope signal observed (none / brief burst)

**4.2 — Identify recovery method for this ECU (2 minutes)**

6. Instructor confirms the recovery method for the specific bricked ECU: SPI clip (same procedure as Station 3) or BDM programmer
7. Instructor confirms the boot mode trigger requirement: does the MCU need a boot mode trigger pin held? For SPI recovery of an external FLASH chip: the MCU does not need to be in boot mode — you are writing directly to the FLASH chip

**4.3 — Verify the recovery file (2 minutes)**

8. Locate the recovery file on the workstation desktop: RECOVERY_[ECU-TYPE]_[DATE].bin
9. Open in HxD — confirm the file is correct size and shows firmware structure (not blank)
10. Ask the instructor to confirm the file version is correct for this specific ECU unit — do not skip this

**4.4 — Connect boot mode programmer to bricked ECU (3 minutes)**

11. Power OFF the bricked ECU before connecting
12. Apply SOIC-8 clip to the FLASH chip (same technique as Station 3) OR connect BDM cable to the BDM header
13. Connect programmer to laptop — confirm device is detected in software

**4.5 — Perform recovery write (10 minutes)**

14. In the SPI programmer software (or BDM software for BDM recovery): load the recovery file
15. Verify in the software that the file size shown matches the FLASH size — if they do not match, stop and call the instructor
16. Call the instructor for pre-write sign-off — instructor confirms file, chip type, and connection before proceeding
17. Initiate the write operation
    - Most SPI write operations: chip erase → write → internal verify (three sequential operations)
    - Do not interrupt — watch the progress indicator; whole sequence should complete in 3–8 minutes depending on FLASH size and speed
18. When write completes: disconnect the programmer and remove the clip
19. Do not power the ECU yet

**4.6 — Post-write verification via scan tool (3 minutes)**

20. Reconnect the ECU to power (bench supply at 13.5–14.2V)
21. Connect the scan tool
22. Initiate ECU identification — the ECU should now respond
23. Confirm ECU identity is displayed correctly: part number, software version matches the recovery file's intended version
24. Read DTCs — there will likely be DTCs present (adaptation values reset to default; these are expected after a recovery write); record the DTC list in check-off card
25. Clear DTCs and cycle power — confirm ECU still communicates after power cycle

> **Checkpoint 4:** Instructor observes ECU communication re-established, ECU identity confirmed on scan tool. Instructor signs check-off card. Station 4 complete.

### Station 4 Common Problems

| Symptom | Likely Cause | Resolution |
|---|---|---|
| Write fails at start — "chip not detected" | Clip not seated; ECU power still on | Confirm ECU powered off; re-seat clip; verify programmer detects chip before initiating write |
| Write completes but ECU still silent after | Wrong firmware file written | Instructor review required: confirm file version; may need to re-write with correct file |
| ECU communicates but throws unexpected DTCs | Adaptation values reset; expected | Record DTCs; clear and cycle; explain to student this is normal after recovery |
| Write aborted mid-way — student panicked and disconnected | Partial write = brick (same state or worse) | Instructor to assess state: if FLASH partially written, re-write from scratch using full erase; document |
| BDM connection not recognised | Incorrect BDM header pin assignment; cable damaged | Re-check pinout on PCB; verify BDM header ground connection; try alternative BDM cable |

---

## Practical Check-Off Card

```
ECU HARDWARE REPAIR — Session 14H — Day 14
Student Name: _______________________
Date: _______________________________

STATION 1 — Variant Coding and Adaptation
[ ] 1A: Coding change applied, before/after recorded, no new DTCs
    Before coding: __________________________________
    After coding:  __________________________________
    Instructor initials: ____    Time: ____

[ ] 1B: Adaptation reset confirmed, channel value post-reset recorded
    Channel name: __________________________________
    Post-reset value: ________________________________
    Instructor initials: ____    Time: ____

STATION 2 — Boot Mode Pin Identification (GATE)
[ ] MCU type identified: _____________________________
[ ] Boot mode trigger pin identified: ___________________
[ ] Access method (SPI FLASH / BDM header) identified and marked on worksheet
    GATE SIGN-OFF: Instructor initials: ____    Time: ____
    ⚠ Equipment for Station 3 NOT issued until this is signed

STATION 3 — SPI FLASH Read
[ ] ECU confirmed powered OFF before clip applied
[ ] FLASH chip type selected in software: ________________
[ ] Read completed — file size: _______ bytes
[ ] Expected file size from datasheet: _________________ bytes
[ ] First bytes inspection: [ ] Firmware structure  [ ] Blank (0xFF)  [ ] Zero (0x00 — fault)
[ ] File saved to: [ ] USB drive  [ ] Workstation backup folder
    Instructor initials: ____    Time: ____

STATION 4 — Bricked ECU Recovery
[ ] Brick confirmed — no OBD communication before recovery
[ ] Recovery file version confirmed with instructor
[ ] Pre-write instructor sign-off obtained
[ ] Write completed without interruption
[ ] Post-write: ECU communication re-established
[ ] ECU identity on scan tool: _______________________
[ ] DTC list after recovery: _________________________
    RECOVERY CONFIRMED — Instructor initials: ____    Time: ____
```

---

## Module 6 Completion Check

| Session | Outcome | Complete |
|---|---|---|
| 13T | so-6-1-1: Distinguished OBD/bench/boot programming modes | [ ] |
| 13T | so-6-1-2: Explained read-backup-write-verify workflow | [ ] |
| 13T | so-6-1-3: Identified .bin, .hex, .mot, .s19 file formats | [ ] |
| 13H | so-6-2-1: Connected and configured bench programmer | [ ] |
| 13H | so-6-2-2: Completed read cycle with correct backup naming | [ ] |
| 13H | so-6-2-3: Completed write and post-write comparison | [ ] |
| 14T | so-6-3-1: Explained online coding and server authentication | [ ] |
| 14T | so-6-4-1: Explained bootloader architecture and JTAG/BDM/SPI/UART | [ ] |
| 14T | so-6-5-1: Diagnosed bricked ECU and selected recovery method | [ ] |
| 14H | so-6-3-2: Performed variant coding, verified changes | [ ] |
| 14H | so-6-3-3: Executed adaptation reset, confirmed acceptance | [ ] |
| 14H | so-6-4-2: Identified boot access pins on ECU PCB | [ ] |
| 14H | so-6-4-3: Performed direct SPI or BDM FLASH read | [ ] |
| 14H | so-6-5-2: Recovered bricked ECU via boot mode write | [ ] |

---

## Session Debrief (5 minutes — full group)

Instructor leads a brief standing debrief. Key questions:

1. "At Station 4 — when the ECU responded on the scan tool after recovery — what was the deciding factor that made recovery possible?" (Expected: the external FLASH chip / primary bootloader / boot mode access was independent of the corrupted firmware)

2. "If a technician doesn't own a boot mode programmer, what are their options when a customer brings a bricked ECU?" (Expected: send to specialist; purchase tool; use SPI clip with CH341A which is low-cost entry)

3. "Why did we do Station 2 — the pin identification — before giving out the equipment?" (Expected: wrong pin connection damages MCU; identification must precede hardware connection)

4. "What's the difference between variant coding and online coding in terms of what a customer pays for?" (Expected: variant coding = offline, any workshop can do it; online coding = manufacturer server, requires licensed manufacturer tool or authorised dealer)

5. "Name three ECU jobs that a boot mode capability allows you to quote for that a workshop without it cannot." (Open answers — examples: bricked ECU recovery, full FLASH clone of protected ECU, immobilizer EEPROM read from protected platform)

---

## Instructor Notes — Full Session

**Pacing:** Station 2 is the natural bottleneck — datasheet reading takes longer for students who haven't done MCU identification work before. If a student is spending more than 10 minutes without making progress on pin identification, guide them to the correct datasheet section with questions, not by giving the answer directly. The identification skill must be practiced, not skipped.

**Station 4 write step:** The instructor must be physically present or immediately available during the Station 4 write. If the write is interrupted for any reason, the instructor must assess the ECU state before any recovery attempt is made by the student. A second brick from a student's interruption is a training scenario, not a disaster — but it requires the instructor's active management.

**Recovery file management:** Keep one extra known-good recovery file for Station 4 on a USB drive (instructor copy, not on workstations). If a workstation has a file corruption or accidental deletion, the instructor can restore without halting the session.

**Assessment hook:** At the close of the debrief, preview the three Module 6 theory test questions that relate to today's session (so-6-3-1, so-6-4-1, so-6-5-1 — as announced in Session 14T). Remind students of the test timing and that the practical check-off records from both Days 13 and 14 will be retained as assessment evidence.

---

## Resources Required

- Bench-mounted ECU with OBD/CAN communication for Station 1
- VCDS cable (or equivalent) and software per workstation
- Disassembled ECU (lid removed) for Station 2
- MCU datasheet (printed or PDF) — specific to the Station 2/3 ECU
- Blank annotated PCB diagram worksheets (one per student)
- CH341A programmer with SOIC-8 clip per workstation (Station 3 and 4)
- AsProgrammer or equivalent SPI software pre-installed and tested
- Pre-bricked ECU — one per workstation for Station 4
- Known-good recovery .bin file per workstation (on desktop)
- Scan tool per workstation for Stations 1 and 4
- HxD or equivalent hex editor per workstation
- Oscilloscope per workstation (Station 4 brick confirmation)
- Magnifier / USB microscope for SOIC-8 clip inspection
- Safety glasses per student
- Session 14H check-off cards — printed, one per student

---

*Module 6 | Day 14 Hands-On | ECUHR | v1.0 | 2026-02-18*
