# SESSION-19H: Key Cloning & Immobilizer Systems — Hands-On Lab
## Workshop Framework

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 9 — Security & Safety Systems + Final Assessment
**Day:** 19 of 20 | **Session:** Hands-On (Session B)
**Duration:** 90 minutes
**Format:** Pair work — three rotating stations
**Prerequisite:** SESSION-19T must be completed before this session

**Session Learning Outcomes:**

| SO Code | Description | Bloom |
|---------|-------------|-------|
| ECUHR-SO-9-1-2 | Perform a direct key clone from a working key using VVDI2 or equivalent | Apply |
| ECUHR-SO-9-1-3 | Execute a lost key recovery procedure using EEPROM dump from the immobilizer unit | Apply |
| ECUHR-SO-9-2-2 | Extract PIN/CS from an immobilizer EEPROM dump and use it to add a key or perform an all-keys-lost procedure | Apply |
| ECUHR-SO-9-2-3 | Match a replacement immobilizer unit to an ECU and verify anti-theft system operation with new key | Apply |

**CO Alignment:** co-4 (Configure and recover vehicle security and safety systems)

---

## SESSION OVERVIEW

### Structure

| Time | Activity |
|------|----------|
| 0–5 min | Briefing and safety rules |
| 5–10 min | Station setup and pair assignment |
| 10–40 min | Station A — Direct key clone (VVDI2) |
| 10–40 min | Station B — EEPROM extraction and PIN recovery (parallel) |
| 10–40 min | Station C — Replacement immobilizer matching (parallel) |
| 40–75 min | Pairs rotate — all pairs complete all three stations |
| 75–90 min | Debrief, common errors, Q&A |

Stations A, B, and C run simultaneously. With three pairs per class, each pair occupies one station initially, then rotates. With more or fewer pairs, adjust rotation as described under Instructor Notes.

### Equipment Required — Per Station

**Station A — Key Clone:**
- VVDI2 key programmer (or equivalent: Autel IM608, Advanced Diagnostics ADC-2000, TANGO)
- Transponder reader coil
- 2× blank transponder chips (correct type for the demo vehicle — ID46 recommended)
- 1× vehicle with working key (test bench or actual vehicle)
- Vehicle wiring diagram (optional but useful)
- Printed Station A procedure card

**Station B — EEPROM Extraction:**
- EEPROM programmer (XGecu T48, RT809H, or equivalent)
- SOIC-8 clip (for in-circuit reading where accessible)
- Hot air station and soldering iron (if EEPROM must be removed)
- Flux, solder wick
- Anti-static mat and wrist strap (mandatory)
- Immobilizer module with EEPROM chip (prepared in advance — see Instructor Preparation)
- Laptop with EEPROM programmer software installed
- VVDI2 or equivalent for PIN analysis and key programming
- OBD scan tool for key-learning step
- Printed Station B procedure card

**Station C — Replacement Immobilizer Matching:**
- Donor immobilizer module (from a different vehicle of the same model range)
- EEPROM programmer with SOIC-8 clip
- Original vehicle immobilizer (or EEPROM image saved from a previous read)
- ECU bench test setup (power supply, wiring diagram, scan tool)
- Printed Station C procedure card

### Consumables
- Blank ID46 transponder chips (4 per class minimum)
- Blank key blades (uncut, for carrying the clone transponder if needed)
- Isopropyl alcohol (PCB cleaning post-soldering)
- Flux (no-clean type)
- Cotton swabs and lint-free wipes

---

## INSTRUCTOR PREPARATION (BEFORE THE SESSION)

### Station A Preparation
1. Select a test vehicle or bench-mounted ECU assembly that uses an ID46 or PCF7936 transponder (most 2003–2014 vehicles outside VAG group).
2. Confirm the VVDI2 has coverage for this transponder type and that the function is unlocked in the tool's software.
3. Prepare one known-working original key.
4. Pre-cut two blank keys to the correct blade profile (or use uncut fob shells if starting from scratch).
5. Confirm the test vehicle starts reliably with the original key before the session.
6. Print two copies of the Station A Procedure Card.

### Station B Preparation
1. Select an immobilizer module for dissection — ideally one from the same vehicle type as Station A, so students recognise the architecture from theory.
2. Identify the EEPROM chip on the PCB. Confirm the chip type (common types: 93C56, 93C66, 24C04, 24C08 — check the immobilizer's EEPROM by chip marking).
3. Confirm that your EEPROM programmer software supports this chip type.
4. Prepare a reference EEPROM image file with the PIN pre-extracted and marked, so you can show the correct answer during debrief. Do not distribute this during the session — it is the debrief reference only.
5. Confirm the VVDI2's PIN extraction function works for this immobilizer type, or identify which software tool to use for PIN decoding.
6. Confirm the OBD scan tool can enter key-learning mode on the test vehicle using the extracted PIN.
7. Print two copies of the Station B Procedure Card.

### Station C Preparation
1. Obtain two immobilizer modules of the same type — one "original" and one "donor" (from a different vehicle of the same platform).
2. Verify both have readable EEPROMs.
3. Prepare the bench ECU setup so students can verify matching without needing a running vehicle: OBD-connected bench power setup is sufficient if available.
4. Have one working key available that belongs to the "original" module's vehicle.
5. Print two copies of the Station C Procedure Card.

---

## SESSION BRIEFING (0–5 MINUTES)

**Instructor delivers the following briefing to the whole class before pairs move to stations:**

> "This session has three distinct procedures. You will work through all three today — that is why stations run in parallel and you rotate.
>
> Before you start at any station, the professional rule from this morning's theory applies: every procedure you perform today is simulated owner-authorised work. Treat it that way. If this were a real workshop, you would have a work order in hand before touching the vehicle. In this lab, the procedure card is your authorisation document. Sign and date it at the start of your station work.
>
> Four working rules for this session:
>
> Rule one: ESD protocols at all stations. Anti-static wrist strap on before you touch any PCB or EEPROM chip. This is an assessment criterion today and in the final assessment tomorrow.
>
> Rule two: read before you do. Each station has a procedure card. Read the entire procedure once before you perform any step. Do not skip steps to save time. A wrong step in key programming can lock a key slot permanently or corrupt the EEPROM.
>
> Rule three: save before you write. At Station B and Station C, before you write anything to any EEPROM, you must save a backup of the current EEPROM contents to a named file on the laptop. File naming format: ECUHR_[StationLetter]_[PairNumber]_[Date]_BACKUP.bin. Do not proceed to write without saving backup first.
>
> Rule four: if in doubt, stop and ask. Do not proceed speculatively on a step you are unsure about. A 30-second question saves a 30-minute recovery.
>
> Any questions before we begin?"

---

## STATION A — DIRECT KEY CLONE
**Target SOs:** so-9-1-2
**Duration per pair:** 25–30 minutes
**Pair work:** One student operates tool, one student observes and records. Swap roles for the second clone attempt.

---

### STATION A BACKGROUND

Direct cloning copies the cryptographic data from an existing working transponder to a blank transponder chip. The blank then responds identically to the original when presented to the antenna ring. The immobilizer EEPROM is not accessed and not modified.

This procedure requires: one working original key, a compatible blank transponder, and a key programmer with the correct chip type function.

**When to use this procedure in practice:** Customer has a working key and wants a spare. Key blade has been worn or damaged (blade replaced, transponder chip is intact). Customer has a working key and requires a duplicate for a second driver.

---

### STATION A PROCEDURE CARD

**Pre-procedure check:**
- [ ] Anti-static wrist strap fitted and connected to mat
- [ ] VVDI2 (or equivalent) powered and software open
- [ ] Original working key available
- [ ] Two blank transponder chips available (correct type — instructor has confirmed)
- [ ] Test vehicle or bench ECU accessible

---

**Step A1 — Identify the transponder type**

1. Open the VVDI2 software on the connected laptop (or use the device's own screen if standalone).
2. Navigate to: Key Programmer → Transponder Type Identification (exact menu varies by tool version — see reference card supplement).
3. Place the original working key on the reader coil of the VVDI2 (coil is the flat disc surface on the unit).
4. Click "Read" or "Identify". The tool will read the transponder and return a chip family identification — for example "ID46 — PCF7946" or "ID48 Crypto 48".
5. Record the transponder type: ________________________________
6. Confirm this matches the expected chip type from the theory session's reference card. If there is a mismatch, call the instructor before proceeding.

**Instructor Checkpoint A1:** Verify student has correctly identified transponder type and that it matches the prepared setup. Sign off before proceeding.

---

**Step A2 — Read the original transponder data**

1. With the chip type confirmed, navigate to: Key Programmer → Clone Transponder → [Chip Family] (e.g. "ID46 Rolling Code Clone").
2. Place the original key on the reader coil again.
3. Select "Read Original Key". The tool will perform the calculation — for ID46 this takes 3 to 8 minutes. Do not move the key during this process.
4. When complete, the tool will display either: (a) "Read successful — key data extracted" or (b) "Cannot read — locked variant".
   - If (a): proceed to Step A3.
   - If (b): call the instructor. The chip is a locked variant and requires the EEPROM route (covered at Station B). Note this result and discuss with instructor.
5. The extracted key data will be displayed in the tool. Do not need to record it manually — the tool stores it in its working memory.

**Common error:** Moving the key during the calculation process causes a read failure. The calculation must restart from the beginning if the key is moved.

---

**Step A3 — Prepare the blank transponder**

1. Take one blank transponder chip (the instructor will confirm the correct blank type for your chip family — for ID46, the correct blank is typically a Super Chip or CN1 compatible blank).
2. Place the blank on the VVDI2 reader coil.
3. Select "Identify Blank". The tool should confirm the blank is in an unlocked, writable state.
4. If the tool reports "blank already written" or "locked", discard the chip and take a fresh blank. Do not attempt to write to a chip that has already been programmed.

---

**Step A4 — Write clone to blank transponder**

1. With the blank confirmed as writable, select "Write Clone" or "Program Blank" in the tool.
2. Confirm the target chip type matches the blank you have loaded.
3. Click "Write". The tool writes the extracted key data to the blank transponder. This takes 5 to 15 seconds.
4. When complete, the tool will display "Write successful" or equivalent confirmation.
5. Select "Verify" if the option is available — this re-reads the blank and confirms the data was written correctly.
6. Record the result: ________________________________

**Important:** The blank transponder is now locked. If the write was incorrect, this blank cannot be erased. Start over with a new blank.

---

**Step A5 — Test the cloned key**

1. Take the cloned transponder (in its blank key shell or held near the antenna).
2. At the test vehicle or bench ECU: insert the cloned key into the ignition barrel (or hold it against the antenna ring within 2–3 cm if not in a key shell).
3. Turn the ignition to the ON position (do not crank yet).
4. Observe the instrument cluster — specifically the immobilizer indicator light (typically a key or padlock symbol).
   - If the immobilizer light goes out or blinks briefly and then extinguishes: authentication is successful.
   - If the immobilizer light remains illuminated or flashes continuously: authentication failed. Do not proceed to start the engine. Call the instructor.
5. If authentication is confirmed, attempt to start the engine (test bench or vehicle).
6. Record the result: ________________________________

**Instructor Checkpoint A5:** Observe the test procedure. Confirm the clone succeeded (vehicle starts) or identify the reason for failure. Sign off on procedure card.

---

**Step A6 — Second clone attempt (role swap)**

Students swap operator and observer roles. Repeat steps A1 through A5 with the second blank transponder chip. Both students must perform the procedure.

---

**Station A Debrief Questions (discuss with partner before rotating):**
1. What would happen if you attempted to use a cloned ID46 key on a vehicle that uses ID48 Crypto 48?
2. If the VVDI2 reported "locked variant — cannot read" at Step A2, what is the alternative procedure?
3. Name one vehicle type where a successful transponder clone is not sufficient to start the car and an additional step is required.

---

## STATION B — EEPROM EXTRACTION AND PIN RECOVERY
**Target SOs:** so-9-1-3, so-9-2-2
**Duration per pair:** 30–35 minutes
**Pair work:** Divide tasks — one student handles EEPROM hardware, one handles software analysis. Both must understand both tasks.

---

### STATION B BACKGROUND

When all keys are lost, no working transponder exists to clone. The only path to key recovery is accessing the immobilizer EEPROM directly, extracting the PIN code stored there, and using that PIN to enter key-learning mode via the diagnostic tool to register new transponders.

This procedure requires: physical access to the immobilizer EEPROM chip, an EEPROM programmer, and a key programming tool with PIN analysis for the specific vehicle type.

**When to use this procedure in practice:** All keys lost (most common). Chip type is a locked variant that cannot be read directly from the transponder. Replacement immobilizer module needs original PIN data for re-matching.

---

### STATION B PROCEDURE CARD

**Pre-procedure check:**
- [ ] Anti-static wrist strap fitted and connected to mat
- [ ] EEPROM programmer connected to laptop and software open
- [ ] Immobilizer module provided by instructor
- [ ] VVDI2 (or equivalent) available and connected
- [ ] OBD scan tool available for key-learning step
- [ ] Laptop with file save capability for EEPROM backup

---

**Step B1 — Identify the EEPROM chip on the immobilizer PCB**

1. Examine the immobilizer module PCB under bench magnification.
2. Locate the EEPROM chip. On most standalone immobilizer modules, the EEPROM is an SOIC-8 package (8-pin, small body). Common chip series: 93Cxx series (93C56, 93C66), 24Cxx series (24C02, 24C04, 24C08), 25Cxx series (SPI flash).
3. Read the chip markings. Record the full chip identifier: ________________________________
4. Look up the chip identifier in the EEPROM programmer's chip support list (or use the manual provided). Confirm the programmer supports this chip.
5. Identify pin 1 of the EEPROM chip (marked with a dot or notch on the chip body). Note its orientation relative to the PCB.

**Common error:** Misidentifying pin 1 orientation. If the SOIC-8 clip is connected backwards, the programmer will report "chip not detected" or read all zeros or all 0xFF. Always verify pin 1 before reading.

---

**Step B2 — Attempt in-circuit read (preferred method)**

1. With the SOIC-8 clip, attach to the EEPROM chip without removing it from the PCB. Clip pin 1 of the cable to pin 1 of the chip.
2. Ensure the immobilizer module's main power supply is disconnected (the module must not be powered during EEPROM reading — the programmer provides its own read voltage).
3. Open the EEPROM programmer software. Select the chip type from the database.
4. Click "Detect" or "Auto-detect". The programmer should confirm chip presence and size.
   - If detected: proceed to Step B3.
   - If not detected: check clip orientation, check all eight pins are making contact, try repositioning clip. If still not detected after two attempts, proceed to Step B2-Alt.

**Step B2-Alt — EEPROM removal (if in-circuit read fails)**

1. Call the instructor to verify the in-circuit approach has been correctly attempted.
2. Apply flux to the EEPROM chip pads.
3. Using the hot air station set to 320°C and medium airflow, heat the chip evenly from above.
4. Once solder flows (approximately 15–20 seconds), use tweezers to lift the chip from the PCB.
5. Place the chip in the SOIC-8 socket adapter on the EEPROM programmer.
6. Connect and proceed to Step B3.

**Instructor Checkpoint B2:** Observe clip attachment or removal procedure. Confirm anti-static protocols are being followed. Sign off before proceeding to read.

---

**Step B3 — Read and save the EEPROM**

1. In the programmer software, click "Read" to read the full EEPROM contents.
2. Visually inspect the read data in the hex editor view. The data should not be all 0xFF (blank) or all 0x00 (failed read). If it appears blank, re-check clip connection.
3. Immediately save the EEPROM image to the laptop: File → Save As. Use the naming convention: ECUHR_B_[PairNumber]_[Date]_BACKUP.bin. Example: ECUHR_B_3_20260219_BACKUP.bin
4. Confirm the file has been saved before proceeding. Read the file size — it should match the chip capacity (93C56 = 256 bytes, 24C04 = 512 bytes, 24C08 = 1KB, etc.).
5. Record the saved file name and size: ________________________________

**Non-negotiable rule:** Do not proceed past this step without a confirmed saved backup. If the backup file is not confirmed, stop and call the instructor.

---

**Step B4 — Extract the PIN code**

1. Open the VVDI2 software (or equivalent key programming tool with EEPROM analysis function).
2. Navigate to: EEPROM / FLASH → Read EEPROM → Load File (or equivalent menu path — see reference card supplement for tool-specific navigation).
3. Load the saved backup .bin file.
4. Select the vehicle type and immobilizer model from the dropdown list (the instructor will tell you which vehicle this module is from).
5. Click "Get PIN" or "Extract CS". The tool will analyse the EEPROM data and return the PIN code.
6. Record the PIN: ________________
7. If the tool returns "cannot extract — unknown format", call the instructor. Some immobilizer types require a manufacturer-specific tool or online service.

**Understanding the result:** The PIN you have just extracted is the Customer Security code. It was stored in the vehicle's documentation when new and is used by authorised dealers for key addition. You have derived it from the hardware data. This is why physical EEPROM access is a significant security event — treat the PIN as confidential information belonging to the vehicle owner.

---

**Step B5 — Enter key-learning mode using the PIN**

1. Connect the OBD scan tool to the test vehicle's OBD-II port.
2. Navigate to: Security / Immobilizer → Key Learning (or equivalent — vehicle-specific).
3. When prompted for Security Access or PIN entry, enter the PIN extracted in Step B4.
4. The system should grant access to the key-learning menu.
   - If access is denied: verify the PIN was entered exactly — no leading zeros omitted, correct digit count. Try once more. If denied again, call the instructor.
5. In the key-learning menu, select "Add New Key" or "All Keys Lost" as appropriate for the prepared scenario (instructor will specify which scenario is active for your station).
6. Follow the on-screen prompts to hold the blank transponder key near the antenna ring and register it.
7. Register two keys as instructed.
8. When the procedure completes, exit key-learning mode.

**Instructor Checkpoint B5:** Observe the PIN entry and key-learning steps. Confirm correct procedure is followed and PIN worked. Sign off.

---

**Step B6 — Verify new keys operate correctly**

1. Test each newly programmed key on the test vehicle: ignition ON, observe immobilizer light extinction, attempt engine start.
2. Both keys should start the vehicle successfully.
3. Test the original key (if one was available as a reference): it should still work unless an all-keys-lost reset was performed (in which case it will no longer work — this is expected and normal).
4. Record both test results: Key 1 ________ Key 2 ________

---

**Step B7 — Re-install EEPROM if removed**

If the EEPROM was physically removed in Step B2-Alt:
1. Apply fresh flux to the PCB pads.
2. Align the EEPROM chip with pin 1 oriented correctly.
3. Solder using the hot air station (320°C, low airflow for precision placement).
4. Inspect all 8 pads under magnification — confirm all pins are soldered, no bridges.
5. Clean the area with isopropyl alcohol.

If an in-circuit read was used and the chip was not removed, no re-installation is needed. Inspect the clip contact area under magnification for any marks on the chip pins — none should be present.

---

**Station B Debrief Questions:**
1. Why is saving the EEPROM backup the single most critical step in this procedure?
2. If you needed to add a key to a vehicle but did not want to use the EEPROM route, what other condition would need to be true to use the direct clone method instead?
3. A customer comes in claiming all keys are lost. You enter all-keys-lost mode, clear all key slots, and program two new keys. The next day the customer calls saying they found their original spare key and it no longer works. Explain why and what the customer must do.

---

## STATION C — REPLACEMENT IMMOBILIZER MATCHING
**Target SOs:** so-9-2-3
**Duration per pair:** 25–30 minutes
**Pair work:** Students work together. One handles EEPROM hardware operations, one manages scan tool verification.

---

### STATION C BACKGROUND

When an immobilizer module fails and a replacement is sourced from a different vehicle, the replacement contains different key slot data and possibly different security association codes. Simply plugging in the replacement will not work — it will generate an immobilizer mismatch and the engine will not start.

The correct procedure is to read the original vehicle's immobilizer EEPROM (or use the previously saved backup), write that data to the replacement module's EEPROM, and then verify that the original vehicle's key is accepted.

**When to use this procedure in practice:** Original immobilizer module has a hardware fault (failed RF transceiver, power supply failure, damaged PCB) but the EEPROM data is intact. Customer wishes to retain all existing keys without a full re-programming session.

---

### STATION C PROCEDURE CARD

**Pre-procedure check:**
- [ ] Anti-static wrist strap fitted and connected to mat
- [ ] EEPROM programmer connected and software open
- [ ] Original immobilizer module (or saved EEPROM backup) available
- [ ] Donor immobilizer module from a different vehicle (same platform type)
- [ ] Original vehicle working key available for verification
- [ ] Scan tool available for final verification

---

**Step C1 — Read the original immobilizer EEPROM**

If using a saved EEPROM backup file from a previous read, proceed to Step C2 with that file.

If reading from the original module:
1. Identify and attach to the EEPROM on the original immobilizer module using the SOIC-8 clip (same technique as Station B, Steps B1–B2).
2. Read the EEPROM and save the image: ECUHR_C_[PairNumber]_[Date]_ORIGINAL.bin
3. Verify the data is not blank. Record file name and size: ________________________________

---

**Step C2 — Identify the EEPROM on the donor module**

1. Examine the donor immobilizer PCB.
2. Locate the EEPROM chip. Note its chip identifier.
3. Confirm the chip type matches the original module's EEPROM. In most cases, replacement modules of the same platform use identical EEPROM chips. If they differ, call the instructor — a different chip type may require address mapping adjustments.
4. Record the donor EEPROM chip type: ________________________________

---

**Step C3 — Read and back up the donor EEPROM**

1. Attach SOIC-8 clip to the donor EEPROM chip.
2. Read the donor EEPROM. Save as: ECUHR_C_[PairNumber]_[Date]_DONOR_BACKUP.bin
3. This is the donor's original data. If anything goes wrong during writing, this backup allows recovery.
4. Record file name and size: ________________________________

**Rule:** You must save the donor backup before writing anything to the donor. No exceptions.

---

**Step C4 — Write the original data to the donor EEPROM**

1. In the EEPROM programmer software, open the original vehicle's EEPROM image (the ORIGINAL.bin file from Step C1 or the provided backup).
2. With the SOIC-8 clip still attached to the donor module, select "Write" or "Program".
3. Confirm the programmer software is pointing to the correct ORIGINAL.bin file — not the donor backup.
4. Click Write. The programmer will erase the donor EEPROM and write the original data.
5. When complete, select "Verify" — the programmer will re-read the donor EEPROM and compare it byte-for-byte with the written image.
6. Confirm "Verify: PASS" before removing the clip.
7. Record result: ________________________________

**Common error:** Writing the donor backup file instead of the original file. This leaves the donor EEPROM unchanged. Always verify which file is loaded in the "Write" buffer before clicking Write.

**Instructor Checkpoint C4:** Observe the write and verify sequence. Confirm the correct source file was used. Sign off.

---

**Step C5 — Install and test the donor (now matched) module**

1. Disconnect the SOIC-8 clip from the donor module.
2. Install the now-matched donor module in the test vehicle bench setup (or the test vehicle), connecting it in place of the original module.
3. Connect the original working key to the antenna ring area.
4. Apply power (ignition ON).
5. Observe the immobilizer warning light behaviour:
   - Light extinguishes after 2–3 seconds: authentication successful.
   - Light remains on or flashes: authentication failed. Note the behaviour and call the instructor.
6. If authentication light clears, attempt to start the engine.
7. Record the result: ________________________________

---

**Step C6 — Scan tool verification**

1. Connect the OBD scan tool to the bench setup's OBD port.
2. Navigate to the immobilizer system module.
3. Read all DTCs.
4. Expected result: no immobilizer DTCs present.
5. If DTCs are present, record them and call the instructor — the most common cause is a mileage mirror mismatch in the EEPROM (more common with VAG group vehicles).
6. Clear any non-persistent codes and re-scan.
7. Record final DTC scan result: ________________________________

---

**Station C Debrief Questions:**
1. The new donor module has been successfully matched using the EEPROM data from the original. Does the customer still need to bring their original key? Explain.
2. You are working on a 2008 Volkswagen Golf. The original immobilizer is failed. A donor module from a 2007 Golf is available. The donor EEPROM reads with a different mileage value in the mileage mirror section. What fault is likely to appear and where?
3. What is the purpose of saving the donor module's original EEPROM before writing to it?

---

## ROTATION SCHEDULE

**For a class of 6 students (3 pairs):**

| Rotation | Pair 1 | Pair 2 | Pair 3 |
|----------|--------|--------|--------|
| Round 1 (0–35 min) | Station A | Station B | Station C |
| Round 2 (35–70 min) | Station B | Station C | Station A |
| Round 3 (70–90 min+) | Station C | Station A | Station B |

**Note:** Station B takes 5 minutes longer than A and C due to EEPROM removal and soldering time. If pairs are finishing at different rates, have early finishers complete the debrief questions at their station before rotating.

**For a class of 4 students (2 pairs):** Pairs rotate through all three stations sequentially. Adjust timing to approximately 25 minutes per station. Third station may need to be completed in extended time or the following morning as a short warm-up.

**For a class of 8–9 students (4+ pairs):** Run two instances of Station A (it requires the least specialist equipment), one Station B, and one Station C.

---

## INSTRUCTOR CHECKPOINTS SUMMARY

| Checkpoint | Station | What to Verify |
|------------|---------|----------------|
| A1 | Station A | Transponder type correctly identified, matches expected chip for prepared setup |
| A5 | Station A | Clone test result observed; if failed, investigate before pair rotates |
| B2 | Station B | Clip attachment correct; ESD protocols observed; chip identified correctly |
| B5 | Station B | PIN extracted correctly; key-learning mode entered successfully |
| C4 | Station C | Correct source file loaded; write and verify sequence completed correctly |

---

## COMMON MISTAKES AND HOW TO ADDRESS THEM

### Station A
**"The VVDI2 says 'locked variant — cannot read'" on step A2:**
Explanation: Some ID46 and Megamos variants have the direct-read function locked from the factory. This is not a fault — it is a security feature. Redirect the student to note this result, explain that the EEPROM route (Station B) would be the correct approach for this chip type, and then provide a correctly unlocked demo chip for the station to proceed.

**"The clone test fails — immobilizer light stays on":**
Check: (1) Is the blank transponder fully in the antenna coil range? Transponder must be within 2–3cm of the antenna. (2) Is the correct blank type? Some blank chips are incompatible with specific ID46 sub-variants. (3) Was the write verified? Re-read the blank and confirm data integrity.

### Station B
**Student reads all 0xFF from EEPROM:**
Cause: clip not making contact with all pins, or pin 1 oriented incorrectly. Have the student re-seat the clip. If in-circuit reading continues to fail, guide through the removal procedure.

**PIN extraction returns "unknown" or error:**
Cause: the immobilizer type is not in the tool's database. Either (a) the tool requires a newer update, or (b) this specific immobilizer variant requires a different tool or online service. Use this as a teaching moment — in the real workshop, this is where you would use an online PIN service, or contact the tool supplier for coverage information.

**Key-learning mode denied after PIN entry:**
Most common cause: incorrect PIN digit count or leading zero dropped. For example, if the extracted PIN is 0247, entering 247 will fail. Verify the full PIN string including any leading zeros.

### Station C
**Verify step fails after writing original data to donor:**
First check: which file was written? If the donor backup was accidentally written instead of the original, re-read the donor EEPROM and compare it with the original — if they are identical, the problem is elsewhere. If they differ, the original was not written. Reload the correct original.bin file and repeat the write.

**Immobilizer light does not extinguish after matching:**
If verify passed (data confirmed written correctly) but the module still does not authenticate, check: (1) Is the donor module the same platform variant as the original? A module from a different transmission variant may have different security region requirements. (2) Is the antenna ring connected to the donor module, not left connected to the original? (3) Does the scan tool show a communication DTC, suggesting the module is not appearing on the CAN bus?

---

## ASSESSMENT OBSERVATION CRITERIA FOR THIS SESSION

This session is not formally assessed, but instructor observation of the following criteria provides formative data for the final assessment tomorrow:

| Criterion | What to Observe |
|-----------|-----------------|
| ESD practice | Wrist strap worn and connected before touching any PCB. Modules handled by edges. |
| Procedure adherence | Procedure card followed in order. No steps skipped. Back-up saved before write. |
| Tool configuration | Correct chip type selected in VVDI2 and EEPROM programmer before proceeding. |
| Troubleshooting | When a step fails, student stops and diagnoses rather than repeating blindly. |
| Documentation | Procedure card signed, results recorded at each step. |
| Professional conduct | PIN treated as confidential. Work discussed in professional terms. |

---

## DEBRIEF (75–90 MINUTES)

Bring all pairs together. Address the following points:

**1. Debrief questions review (5 minutes)**
Pick one debrief question from each station and take answers from the group. Correct any misconceptions.

**2. Common errors observed (5 minutes)**
Briefly describe any systematic errors observed across pairs — without naming individuals. Common ones to address:
- Not verifying after write (critical habit for tomorrow's assessment)
- Not saving backup before writing
- Confusing cloning and programming procedures

**3. Real-world connection (3 minutes)**
> "Everything you did this afternoon is a real workshop procedure. The only differences between here and a customer job are: (1) you have a documented work order and have verified ownership, (2) the customer is present or has left their details, and (3) you charge for the procedure.
>
> The technical steps are identical. The discipline is identical. The backup-before-write rule is more important in a real workshop because there is no instructor to recover from a mistake — you are responsible for that customer's vehicle."

**4. Preview for tomorrow (2 minutes)**
> "Tomorrow morning is the airbag theory session — the one where we start with safety before anything else. Tomorrow afternoon is the final practical assessment. You will receive an ECU with an unknown planted fault, a wiring diagram, and 45 to 60 minutes to diagnose and propose a repair. Everything from the last 19 days is in scope.
>
> Tonight: review Module 5 diagnostic methodology and Module 6 programming procedures — those are the two most heavily represented in the assessment fault types. We will cover the assessment brief in detail tomorrow morning."

---

## INSTRUCTOR NOTES

**ESD enforcement:** This session involves EEPROM removal and soldering at Station B. ESD discipline is critical. Do a physical wrist strap check at the start of the session and at the rotation points. Students who remove their wrist strap should be reminded immediately.

**Station B timing:** Station B is consistently the longest station due to potential EEPROM removal time. If pairs are working slowly, prompt them at the 20-minute mark whether they have reached Step B4 (PIN extraction). If not, guide them through B2-Alt more quickly or skip to B4 using the pre-extracted reference (using this should be noted on the procedure card as "instructor assisted").

**Scaling for different class sizes:** If only one VVDI2 is available, Station A and B can share it — A uses the clone function, B uses the PIN analysis function. The physical tool operations do not overlap if pairs rotate correctly.

**Documenting observations:** Note which pairs encountered difficulty and at which step. This informs which topics to emphasise in tomorrow's assessment debrief. Students who struggled at Station B (EEPROM clip technique) may need close support during the hands-on portion of the final assessment.

**If a blank transponder is wasted** due to incorrect write: have spare blanks available. Do not allow the session to stall over a single wasted blank. Log the error, discuss why it happened, and provide a replacement chip. This is a learning event, not a failure event.

---

**End of SESSION-19H Framework**
**Next:** SESSION-20T-Airbag-Safety-Theory-Framework.md
