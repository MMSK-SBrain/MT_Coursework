# SESSION-13H: ECU Read-Backup-Write-Verify Practical
## Hands-On Session | Day 13 | Module 6: ECU Programming & Bootloader

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 6 — ECU Programming & Bootloader
**Day:** 13 | **Session Type:** Hands-On Workshop
**Duration:** 90 minutes
**CO Alignment:** co-3

---

## Session Outcomes

| SO Code | Outcome Statement | Bloom's Level |
|---|---|---|
| so-6-2-1 | Connect and configure a programming tool (KTM Bench or equivalent) for bench-mode reading of a sample ECU | Apply |
| so-6-2-2 | Complete full ECU read cycle, save backup file with correct naming convention, verify file size and checksum | Apply |
| so-6-2-3 | Write a verified file back to the ECU and confirm successful write with post-write read comparison | Apply |

---

## Assessment Alignment

| SO Code | Checkpoint | Assessment Method | Pass Criterion |
|---|---|---|---|
| so-6-2-1 | Checkpoint 1 | Instructor observation — ECU correctly detected | Tool reports correct ECU type, MCU, and FLASH size; student can verbally confirm match to physical ECU |
| so-6-2-2 | Checkpoint 2 | Instructor observation + file verification | Backup file saved with correct naming in two locations; file size matches expected FLASH size |
| so-6-2-3 | Checkpoint 3 | Instructor observation + file comparison | Post-write read matches write file (byte-for-byte or with documented expected differences) |

**Gating rule:** Checkpoint 2 must be passed and signed off by the instructor before the student is permitted to proceed to the write step. This is a hard gate — not a recommendation.

---

## Session Purpose and Context

This is the most critical practical session in Module 6. Session 13T established the mental model and the mandatory workflow. This session requires students to execute that workflow correctly on real hardware. The read-backup-write-verify cycle performed here is identical in structure to what a student will perform on a customer's ECU the following week, the following month, and throughout their professional career.

The session is designed to develop not just motor skill (connecting cables, using software) but professional habit. The backup naming convention, the two-location save, the pre-write check, and the post-write comparison must become automatic. Students who complete this session with all three checkpoints should leave with a workflow they will not vary from.

**What this session is NOT:**
- A speed exercise — students are not assessed on how fast they complete the cycle
- A troubleshooting session — the equipment is pre-verified and known-good; if a student encounters a technical problem, the instructor resolves it; the student's time is used practicing the workflow, not diagnosing hardware faults
- A certification of advanced programming skill — this is foundational competency; advanced and boot mode work follows in Session 14H

---

## Equipment List — Per Workstation

| Item | Specification | Notes |
|---|---|---|
| Laptop / workshop PC | Windows 10 or 11; mains-powered | Battery backup not acceptable; mains power only; sleep disabled before session |
| Programming software | KTM Bench (or equivalent as per facility) | Pre-installed, licensed, and tested before session; instructor to confirm license status morning of Day 13 |
| ECU bench harness | ECU-type specific — matching the sample ECU provided | Correct harness for the specific ECU family; pin assignments verified |
| Sample ECU | Known-good unit — instructor-verified before session | Bosch ME7.5 or ME17.9.x or equivalent (confirm with facility equipment list); same ECU type across all workstations |
| Bench power supply | Regulated DC; 13.5–14.2V output; 5A current capacity minimum | Must be regulated — not a battery charger with floating voltage |
| Power supply leads | Red/black; banana plug or alligator clip; rated 10A | Clean connections; no corroded clips |
| USB-A cable | For programming interface to laptop | Provided with tool; confirm cable is data-capable (not charge-only) |
| USB drive | 16GB minimum; USB 3.0 preferred | One per workstation; pre-formatted; labelled with workstation number |
| HxD (or equivalent hex editor) | Installed on laptop | Pre-installed; shortcut on desktop |
| Reference cards | Naming convention card (A5, laminated); FLASH size reference for sample ECU type | Printed and ready before students arrive |
| Procedure card / check-off card | Printed per student | See check-off card section below |

---

## Pre-Session Instructor Preparation

**The day before (Day 12 evening or Day 13 morning):**

1. Confirm all tool licenses are active — log into KTM Bench (or equivalent) on every workstation and confirm the sample ECU type appears in the ECU database with read/write capability shown as licensed
2. Complete a full read-write cycle on at least one workstation as a function test — confirm read completes, file size is correct, write completes, post-write comparison passes; this confirms the harness, power supply, tool, and sample ECU are all operational
3. Prepare the write file: pre-create a "modified" file using the known-good read from function test, with one clearly identifiable byte change in a non-critical calibration area (e.g., a single map value that will be visible in HxD comparison); save as INSTRUCTOR_WRITEFILE_[ECU-TYPE].bin on each workstation desktop
4. Confirm the pre-write file is valid: it should be the correct size, correct format, and the byte difference should be in a known location that the instructor can point to during the Checkpoint 3 debrief
5. Test USB drives — insert each into the workstation, confirm read/write access, confirm Windows is not set to block USB storage
6. Set all laptop power plans to High Performance; disable sleep and hibernation
7. Brief on naming convention: prepare the whiteboard or slide with the naming convention displayed throughout the practical — students should be able to see it without looking at their notes

**Day 13, before students arrive:**
- ECU connected to bench harness at every workstation, but powered OFF (power supply ON but ECU power lead disconnected — students apply power as part of Step 1)
- Programming software open on login screen or at ECU selection screen — not on desktop
- USB drives inserted and ready
- HxD installed and accessible from taskbar
- Naming convention visible on whiteboard or shared screen

---

## Safety Notes

**Electrical safety:**
- Bench power supplies must be current-limited to 5A before students connect; some ECUs have short circuit protection, but a failed harness connection to wrong pins can draw high current
- Students must not exceed 14.5V supply voltage — 15V+ risks ECU voltage regulator and MCU damage
- If the power supply shows unexpected current draw (above ~3A in steady state after startup), instruct student to power off immediately and report to instructor before proceeding

**Data safety:**
- The programming tool communicates with the ECU using vendor protocols; if the software crashes mid-read or mid-write, power off the ECU but do NOT disconnect the USB until the software has reported a failure — disconnecting while a write is live may corrupt more of the FLASH
- Students must not disconnect harness connectors while ECU is powered — some ECU main connectors carry the power line and disconnecting live can cause voltage spikes

**Tool handling:**
- The programming interface box (KTM Bench unit or equivalent) must not be dropped, have liquids near it, or be placed on metal surfaces that could short exposed contacts
- Harness connectors must be aligned before insertion — forcing a misaligned connector can bend pins in the ECU connector

---

## Detailed Step-by-Step Procedure

### Pre-Start: Naming Convention Review (5 minutes — instructor-led before students begin)

Before students touch any equipment, the instructor verbally reviews the naming convention with the class and confirms every student can reproduce it from memory.

**Naming convention:**
```
DATE_VEHICLE-MAKE-MODEL-YEAR_ECU-TYPE_VIN-LAST-8_READ.bin
```

For this session, since we are using a sample ECU (not a customer vehicle), the naming is simplified:
```
DATE_SAMPLE-ECU_ECU-TYPE_READ.bin

Example:
20260218_SAMPLE-ECU_ME7.5_READ.bin
```

Post-write verify file naming:
```
20260218_SAMPLE-ECU_ME7.5_POST-WRITE-VERIFY.bin
```

**Instructor: write this on the whiteboard and leave it visible for the entire session.**

Students write the naming convention on their procedure card before starting.

---

### STEP 1 — Equipment Connection and Startup (0:00–0:15)

**Objective:** ECU connected to programmer and bench supply; software open; ECU powered.

**Student procedure:**

1.1 — Inspect the bench harness:
- Locate the ECU connector end of the harness — confirm it matches the connector on the sample ECU (compare connector shape, pin count, locking tab position)
- Locate the programmer interface end of the harness — confirm it matches the KTM Bench (or equivalent) interface connector

1.2 — Connect harness to ECU:
- Orient the harness ECU-end connector correctly — align the key or locking tab before applying force
- Push fully home until the connector lock clicks
- Do not tug or pull to test — the click is confirmation; tugging stresses the connector

1.3 — Connect harness to programming interface:
- Connect the programmer-end of the harness to the KTM Bench interface box
- Lock or latch if applicable

1.4 — Connect programming interface to laptop:
- Insert USB cable from KTM Bench interface box into laptop USB port
- Confirm Windows recognises the device — USB device notification expected; if no notification, try alternative USB port and report to instructor

1.5 — Connect bench power supply to ECU:
- Locate power supply connection points on the harness — typically labelled VBAT (+) and GND (-)
- Connect red lead to VBAT, black lead to GND
- Set power supply to 13.8V before connecting (if adjustable)
- Connect the power leads to the bench supply terminals

1.6 — Apply power:
- Power on the bench supply
- Observe: current draw on supply readout; for most common ECUs, standby current should be 0.2–0.8A; if current is 0 → check connections; if current immediately jumps above 2A → suspect wiring short; power off and report

1.7 — Launch programming software:
- Open KTM Bench software (or equivalent)
- Wait for software to load and connect to interface box — software should report interface detected; if not, check USB connection

**Instructor notes:** Circulate during this step. The most common problem is harness orientation — students will apply the connector backwards if they don't check. If a student has 0A current draw, check GND connection first (most common cause of no-power), then VBAT lead, then harness-to-ECU connection.

---

### STEP 2 — ECU Detection and Identification (0:15–0:25)

**Objective:** Tool correctly identifies ECU type, MCU, and FLASH size.

**Checkpoint 1 falls at the end of this step.**

**Student procedure:**

2.1 — In software: navigate to ECU selection:
- Select manufacturer (e.g., Bosch)
- Select ECU family (e.g., ME7.5)
- Select specific ECU type from dropdown (use reference card for correct selection)

2.2 — Initiate auto-detection:
- Click "Detect" or "Read ECU Info" (button name varies by tool version)
- Tool sends identification request to ECU and reads ECU identity bytes

2.3 — Review detection result:
- Tool should display: ECU family name, MCU model, FLASH size (in bytes or KB/MB), and available operations (Read FLASH, Read EEPROM, Write FLASH, etc.)

2.4 — Verify detection result against physical ECU:
- Compare tool-reported ECU type to the label on the physical ECU (instructor has provided ECU identity card per workstation)
- Compare reported FLASH size to expected size on reference card

**Checkpoint 1 — Instructor verification:**
- Instructor checks: tool is reporting correct ECU type; FLASH size matches reference; available operations include Read FLASH and Write FLASH
- Student verbally states: "Tool reports [ECU type], [FLASH size] MB. This matches the reference card."
- Instructor signs Checkpoint 1 on check-off card

**If detection fails:** See common problems table. Most common causes: incorrect harness orientation (re-seat), power supply voltage out of range (check bench supply), incorrect ECU type selected in software (re-select), USB communication error (restart software, replug USB).

**Instructor notes:** Some students will proceed to read without calling for Checkpoint 1 sign-off. Remind at the start of the session that Checkpoint 1 must be signed before Step 3 begins. If you see a student start a read without calling you over, stop them, complete the checkpoint, then let them proceed.

---

### STEP 3 — Full ECU Read (0:25–0:40)

**Objective:** Complete read of full FLASH memory (and EEPROM if tool supports it as a unified operation for this ECU type).

**Student procedure:**

3.1 — In software: select "Read FLASH" (or "Full Read" if FLASH + EEPROM are unified):
- If tool offers separate FLASH and EEPROM read operations, select FLASH first

3.2 — Announce to workstation neighbours:
- "Read in progress — please don't disturb the bench"
- (Workshop culture: no read or write should be performed without a verbal advisory — this prevents accidental bumps that interrupt communication)

3.3 — Initiate read:
- Click Start / Read
- Monitor progress bar — do not interact with software or hardware during read

3.4 — Read completes:
- Software reports "Read complete" or equivalent
- Note the file size shown by the software (in bytes, KB, or MB depending on tool display)

3.5 — Note file size in bytes on procedure card:
- Convert if necessary: 1 MB = 1,048,576 bytes; 4 MB = 4,194,304 bytes
- Cross-reference against FLASH size reference card

**Common read duration:** ME7.5 full FLASH: approximately 90–120 seconds via bench mode. EDC17: approximately 2–4 minutes. If the read is taking significantly longer, suspect communication noise or harness connectivity issue.

**Instructor notes:** During reads, circulate and check progress bars. A stalled progress bar (no movement for more than 30 seconds) usually indicates a lost connection — the read will eventually fail or report an error. If this happens, instruct student to let the timeout occur, then check harness connections and retry.

---

### STEP 4 — Save Backup (0:40–0:50)

**Objective:** Read file saved with correct naming in two locations, file size verified.

**Checkpoint 2 falls at the end of this step. NO write proceeds without Checkpoint 2 sign-off.**

**Student procedure:**

4.1 — In software: select "Save" or the tool's file save function:
- Navigate to the local save folder on the workstation (pre-created by instructor: Desktop/ECU-Backups/[Workstation-Number]/)
- Name the file using the naming convention: `20260218_SAMPLE-ECU_ME7.5_READ.bin` (adjust ECU type as appropriate)
- Click Save

4.2 — Verify the saved file:
- Navigate to the save location in Windows Explorer
- Right-click file → Properties → note file size in bytes
- Compare to expected FLASH size on reference card
- Write file size on procedure card

4.3 — Copy to USB drive:
- Open USB drive folder in Windows Explorer
- Copy (do not move) the backup file to the USB drive root or a labelled folder
- Verify copy completed successfully — file should appear on USB with same file size

4.4 — Verify USB copy:
- On USB drive: right-click file → Properties → confirm file size matches laptop copy

4.5 — Verbally declare to instructor:
- "Backup saved. File name: [state full name]. File size: [state size in bytes]. Saved to laptop folder and USB drive. Ready for Checkpoint 2."

**Checkpoint 2 — Instructor verification (HARD GATE):**
- Instructor checks: file name correct on laptop; file name correct on USB; file sizes match; file size matches expected FLASH size; no write operation has started
- Instructor signs Checkpoint 2 on check-off card
- Instructor verbally confirms: "You may proceed to Step 5."
- If Checkpoint 2 fails (incorrect naming, only one save location, file size wrong): student corrects and calls for re-check before any write begins

**Instructor notes:** This checkpoint is the most important gate in the entire practical. Do not rush through it. Spend 60–90 seconds per student confirming both save locations and the file size. Students who are rushing may try to show you one save location and wave at the USB drive — physically confirm both. If you have a large class (10+ students) and all reach this point simultaneously, queue them: no student writes until their Checkpoint 2 is completed.

---

### STEP 5 — Prepare and Review Write File (0:50–0:55)

**Objective:** Correct write file identified, confirmed for ECU type and file size, loaded in software.

**Student procedure:**

5.1 — Locate write file on workstation desktop:
- File: `INSTRUCTOR_WRITEFILE_[ECU-TYPE].bin` on Desktop

5.2 — Verify file before loading:
- Right-click → Properties → check file size; confirm it matches the read file size (same FLASH size)
- This is a key check: a write file that is a different size than the ECU FLASH should never be written

5.3 — Open write file in HxD briefly:
- Launch HxD → File → Open → select the write file
- Do not edit — view only
- Confirm the file looks like binary ECU data (densely packed hex values; not all 0xFF or all 0x00)
- Close HxD

5.4 — Load write file in programming software:
- In tool software: select "Write FLASH" operation
- Browse to write file; select INSTRUCTOR_WRITEFILE_[ECU-TYPE].bin
- Confirm tool shows correct file loaded (filename and size displayed)

**Instructor notes:** "The purpose of Steps 5.2 and 5.3 is to build the habit of looking at the file before writing. A corrupted or obviously wrong file (all zeros, all FFs, clearly wrong size) should be caught here. Students who develop the habit of blind-loading whatever file they're given will eventually write the wrong file."

---

### STEP 6 — Write (0:55–1:10)

**Objective:** Write the verified file to the sample ECU without interruption.

**Student procedure:**

6.1 — Pre-write announcement:
- "Write in progress — please don't disturb the bench."
- Confirm laptop is on mains power and sleep is disabled

6.2 — Confirm tool is ready:
- Software shows write file loaded; ECU still detected (no communication errors)
- If ECU has gone idle (some ECUs timeout standby communications): re-detect ECU before initiating write

6.3 — Initiate write:
- Click Start / Write / Program (tool-specific button)
- Software will typically: enter programming session → erase FLASH sectors → write data → verify internally (if tool does internal verify) → exit programming session → report success/failure

6.4 — During write — do NOT:
- Touch any cables (power, USB, harness)
- Click elsewhere in the software
- Allow any other software to pop up and take focus (disable notifications before starting)
- Let the laptop screen lock or go to sleep

6.5 — Write completes:
- Software reports "Write complete" or "Programming successful"
- Note: this is the tool's internal success report based on protocol completion; it does NOT confirm byte-level accuracy; that is Step 7's job

6.6 — Write the result on procedure card:
- Note: tool success message, time completed, any warnings shown

**Common write duration:** Similar to read — 90–120 seconds for ME7.5 FLASH. If progress stalls midway: see common problems table.

**If write fails mid-process (error message, stalled progress):**
- Do not touch anything yet — wait 60 seconds for the software to report a timeout or error
- If software reports error: do NOT power cycle yet — attempt to reinitiate write from software
- If software is unresponsive: power cycle the ECU (not the laptop); then reload the write file and retry
- If retry fails: restore from backup (same write procedure, using the backup file instead of write file)
- If restoration also fails: flag for instructor — this is a boot mode recovery scenario

**Instructor notes:** Walk around during write operations. Students will stare at the progress bar and reach for the cable when it pauses. Remind them: the FLASH erase phase shows no progress movement for 10–20 seconds on some ECU types — this is normal. Only intervene if the software shows an error or the progress bar has been stationary for more than 60 seconds.

---

### STEP 7 — Post-Write Verify (1:10–1:25)

**Objective:** Independent verification that the write was successful, byte-level comparison confirms the write file was correctly programmed.

**Checkpoint 3 falls at the end of this step.**

**Student procedure:**

7.1 — Perform a second full read immediately after write completes:
- Select "Read FLASH" operation again in software
- Initiate read — same process as Step 3

7.2 — Save the post-write read:
- Name: `20260218_SAMPLE-ECU_ME7.5_POST-WRITE-VERIFY.bin`
- Save to same local folder as the original backup

7.3 — Open HxD for comparison:
- Launch HxD → Tools → Compare (or File → Open both files and use the compare view)
- Load the POST-WRITE-VERIFY file as the primary file
- Load the INSTRUCTOR_WRITEFILE as the comparison file
- Run comparison

7.4 — Review comparison result:

**Expected result — success:** Files are identical (HxD reports 0 differences) OR files differ only at known checksum byte locations (instructor will specify the expected difference location for this ECU type — reference card includes this information)

**Unexpected result — failure:** Files differ at locations other than documented checksum bytes → write is incomplete or incorrect; see debrief procedure below

7.5 — Record comparison result on procedure card:
- State: identical / expected differences at [address range] / unexpected differences at [address range]

7.6 — Call instructor for Checkpoint 3 sign-off:
- Student verbally explains the comparison result and what it means

**Checkpoint 3 — Instructor verification:**
- Instructor reviews HxD comparison display
- If expected differences: instructor confirms the address range matches the documented checksum bytes for this ECU type; this is a pass
- If unexpected differences: instructor and student investigate together; determine if restoration is required
- Instructor signs Checkpoint 3

**If comparison shows unexpected differences — debrief procedure:**
- Do not reconnect to vehicle
- Power cycle the ECU
- Perform another read — save as [DATE]_RETRY-READ.bin
- Compare retry read to write file
- If still different: load original backup → write backup → compare → assess
- In the training context: this is a learning moment; instructor narrates what would happen next (boot mode recovery) and confirms the student understands the escalation path before the session closes

**Instructor notes:** "Some students will see a 1-byte difference in the comparison and assume they failed. Check the reference card — if that byte is the tool's checksum correction, it's a pass. Explain this to the student individually. They need to understand why the difference exists, not just that it's acceptable."

---

## Session Debrief (1:25–1:30)

**Group debrief — 5 minutes, class reconvenes**

Instructor leads brief discussion:

1. "What would you do if the comparison in Step 7 showed unexpected differences?" — Expected answer: restore from backup using same write procedure; if that fails, escalate to boot mode recovery

2. "What was the purpose of Checkpoint 2 — why is it a hard gate?" — Expected answer: the backup is the only recovery path; no write should proceed without a confirmed backup in two locations

3. "If you had three files on your desktop called 'read.bin', which one belongs to this ECU?" — Expected answer: you cannot know; this is why the naming convention exists

4. Show hands: "How many of you reached Checkpoint 2 before I came to sign it off?" — Normalise waiting; "You did the right thing by stopping. Students who run ahead of the checkpoint are students who will skip the backup in a real workshop."

---

## Practical Check-Off Card

```
SESSION 13H — ECU READ-BACKUP-WRITE-VERIFY
Student Name: ______________________________
Date: _____________ Workstation: ___________
ECU Type: _________________________________

CHECKPOINT 1 — ECU DETECTION
[ ] Tool reports correct ECU type: _______________________
[ ] MCU identified: _____________________________________
[ ] FLASH size reported: _________________ bytes/MB
[ ] Matches reference card: Y / N
Instructor sign-off: _________________ Time: _______

CHECKPOINT 2 — BACKUP SAVED (HARD GATE — NO WRITE UNTIL SIGNED)
[ ] Backup filename correct: ____________________________
[ ] Backup saved to local folder: Y / N
[ ] Backup saved to USB drive: Y / N
[ ] File size (laptop): _________________ bytes
[ ] File size (USB): _________________ bytes
[ ] Sizes match expected FLASH size: Y / N
Instructor sign-off: _________________ Time: _______

WRITE STEP CONFIRMATION
Student confirms pre-write checks:
[ ] Write file correct type for this ECU: Y / N
[ ] Write file size matches FLASH size: Y / N
[ ] Laptop on mains power: Y / N
[ ] Sleep disabled: Y / N

CHECKPOINT 3 — POST-WRITE VERIFICATION
[ ] Post-write read completed
[ ] Post-write file named correctly: ____________________
[ ] HxD comparison performed
[ ] Comparison result: Identical / Expected diff at: _________ / Unexpected diff
[ ] Student can explain comparison result: Y / N
Instructor sign-off: _________________ Time: _______

OVERALL RESULT: PASS / RETRY / ESCALATE
Notes: ________________________________________________
```

---

## Common Problems Table

| Problem | Likely Cause | Resolution |
|---|---|---|
| Tool does not detect USB interface | USB cable is charge-only; wrong USB port; driver not installed | Try different USB port; replace cable; check Device Manager for unrecognised device |
| ECU detection fails — timeout | Incorrect ECU type selected in software; harness not fully seated; power supply not connected or at wrong voltage | Re-seat harness connector on ECU; confirm power supply is on and at 13.8V; select correct ECU type from reference card |
| ECU detection fails — wrong ECU identified | ECU label does not match tool's database entry; ECU may be a variant not in current license | Report to instructor; do not proceed; instructor to identify correct tool selection |
| Read fails midway | Communication noise — loose harness contact; power supply ripple; USB enumeration issue | Check all connections; ensure bench supply is regulated; complete read retry from scratch |
| Read completes but file size is wrong (smaller than expected) | Partial read — tool only read one sector or one FLASH bank | Check that "Full Read" was selected, not "Read Calibration" or a partial read mode |
| Write fails — "ECU in unexpected state" | ECU was left in programming session from a previous failed attempt | Power cycle ECU; wait 5 seconds; reinitiate write |
| Write fails midway | Power supply interrupted; USB communication dropped; laptop went to sleep | Restore from backup; investigate root cause before retrying write |
| Post-write comparison shows all-FF differences in some sectors | FLASH erase without write — those sectors were erased but the write file had no data for them (depends on ECU type and file completeness) | Flag to instructor; may indicate incomplete write file; do not reconnect to vehicle |
| HxD comparison shows 1–4 byte differences at end of file | Tool-specific checksum correction written during programming | Consult reference card for this ECU type; if addresses match documented checksum bytes, this is a pass |
| Power supply shows 0.0A current | GND connection not made; VBAT lead disconnected; ECU power lead not connected to supply | Check all power connections; confirm GND lead is connected to correct pin on harness |
| Laptop goes to sleep during read | Sleep was not disabled in power settings | Instructor resolves; power cycle ECU; retry read from the beginning |

---

## Instructor Notes — Managing Student Pace

**Expected pace distribution:** In a class of 8–12 students, expect:
- Fast group (25–30%): will reach Checkpoint 3 by the 60-minute mark; use remaining time to run a second cycle independently or to write the original backup back (restoring original state)
- Median group (50%): will complete all three checkpoints within the 90-minute window with a few minutes to spare
- Slower group (20–25%): will need the full 90 minutes; may not complete Checkpoint 3 in session; instructor prioritises these students in the final 20 minutes to get them through the verify step

**Managing the fast group:** If students finish early, give them an extension task: perform the comparison again using the software's built-in compare function rather than HxD, and explain to you (the instructor) the difference between the two comparison methods. This reinforces the verify step and gives meaningful activity without creating a new skill demand.

**Managing the slow group:** The most common bottleneck is Checkpoint 2 — students who don't call you over in time and then have to wait while you work through the queue. Pre-brief students that they should call for Checkpoint 2 as soon as they've confirmed both saves — not after doing something else first. If five students hit Checkpoint 2 simultaneously, work through them as a group: check each laptop, then each USB drive, while students stand ready. Takes 3–4 minutes for a group of five.

**If a student has a hardware failure (not user error):** Replace their ECU or harness from the reserve equipment and restart them from Step 1. Do not have them attempt to diagnose the hardware — hardware troubleshooting is Module 5 territory; this session is programming workflow.

**Timing note:** Build 5 minutes of buffer before the debrief into your mental model. If the class is running behind at the 70-minute mark, shorten the debrief to 2 minutes (ask only the first question) and prioritise getting the slower students through Checkpoint 3.

---

## Extension Task (For Fast Finishers)

Students who complete all three checkpoints with more than 15 minutes remaining:

**Extension A — Restore and Verify:**
- Load the ORIGINAL READ backup
- Write it to the ECU (restoring original state)
- Perform post-write read
- Compare to original READ file — should be identical
- This demonstrates the full recovery procedure: the exact process used if the write file had been wrong

**Extension B — Format Investigation:**
- Open the backup .bin file in HxD
- Identify the first 16 bytes (header region of this ECU's FLASH map, if instructor has provided address reference)
- Open the INSTRUCTOR_WRITEFILE.bin in a second HxD window
- Side-by-side: find the known change byte and verify its location and old vs. new value
- Record the hex address and values on the procedure card

---

## Post-Session Housekeeping

Before students leave:
- Power off bench supplies
- Disconnect ECU from harness (from the ECU side — do not pull harness from programmer while software is open)
- Close programming software before disconnecting USB
- Remove USB drives and hand to instructor for secure storage (backup files on USB drives should not leave the facility)
- Return ECU to instructor-designated storage — do not leave ECUs on workbenches

---

*Module 6 | Day 13 Hands-On | ECUHR | v1.0 | 2026-02-18*
