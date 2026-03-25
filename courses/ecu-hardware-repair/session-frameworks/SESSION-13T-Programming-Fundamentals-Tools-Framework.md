# SESSION-13T: ECU Programming Fundamentals & Tools Overview
## Theory Session | Day 13 | Module 6: ECU Programming & Bootloader

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 6 — ECU Programming & Bootloader
**Day:** 13 | **Session Type:** Theory
**Duration:** 90 minutes
**CO Alignment:** co-3

---

## Session Outcomes

| SO Code | Outcome Statement | Bloom's Level |
|---|---|---|
| so-6-1-1 | Distinguish between OBD-mode, bench-mode, and boot-mode programming and state when each is appropriate | Understand |
| so-6-1-2 | Explain the read-backup-write-verify workflow and why a backup must be created before any write operation | Understand |
| so-6-1-3 | Identify common ECU file formats (.bin, .hex, .mot, .s19) and explain what each represents | Understand |

---

## Assessment Alignment

| SO Code | Assessment Item | Method | Weight |
|---|---|---|---|
| so-6-1-1 | Q1 Theory Test M6: Scenario — match programming mode to use case | Written MCQ | Module 6 theory test |
| so-6-1-2 | Q2 Theory Test M6: Sequence the read-backup-write-verify steps in correct order | Written ordering | Module 6 theory test |
| so-6-1-3 | Q3 Theory Test M6: Identify file format from description | Written MCQ | Module 6 theory test |
| so-6-1-1 | Practical check-off 13H: student selects correct programming mode during practical | Observation | Session 13H |
| so-6-1-2 | Practical check-off 13H: student completes backup with correct naming before writing | Observation | Session 13H |

---

## Session Overview

**Session Role in Module:** This is the foundational theory session for Module 6. Everything that follows in Sessions 13H, 14T, and 14H builds on the mental models and workflow established here. The primary objective is not just knowledge transmission — it is instilling the correct professional mindset around ECU programming. Students who leave this session without understanding why the backup is mandatory will be dangerous in the practical.

**Prerequisite Knowledge:** Students should arrive knowing: how to use a multimeter, basic CAN bus principles (from Module 4), ECU hardware identification (from Module 5), and how to connect bench power supplies. This session does not revisit those fundamentals.

**Session Flow Summary:**
- Hook (5 min)
- Three programming modes (25 min)
- When to use each mode — decision framework (10 min)
- The read-backup-write-verify workflow (20 min)
- File formats (10 min)
- Programming tools overview (10 min)
- Climax, resolution, preview (10 min)

---

## Hook — The Disaster Without a Backup (5 minutes)

**Delivery:** Verbal story. No slides during the hook. Instructor stands without the projector drawing attention. This forces auditory focus.

**The Story:**

"A technician at an independent shop gets a 2019 BMW 3 Series with a failed ECU. He sources a used replacement unit — correct part number, confirmed on the parts database. He installs it on the bench, connects his Kess V3, reads the original software version from the replacement ECU to confirm compatibility. Everything looks right. He writes the customer's software to the replacement ECU. The tool says 'Programming successful.' He installs the ECU into the car.

The car won't start.

He connects a scan tool. The ECU is communicating. But the software has thrown a cascade of faults — engine protection, immobilizer correlation, transmission variant mismatch. The ECU is alive, but it's running the wrong firmware. Same BMW part number, different engine variant — different displacement, different injector type, different boost map. The parts database had grouped them. He wrote the wrong file.

Now, to recover the replacement ECU, he needs to write the correct file to it. But the ECU is now in an inconsistent state — the firmware is wrong but not fully corrupted — and when he tries to write again, the Kess V3 gives him an error: 'ECU in unexpected state. Unable to initiate write. Contact support.'

He needs boot mode access and a correct backup of the replacement unit's original firmware. But he didn't make a backup. He connected, wrote, and assumed the tool's 'success' message was the end of the story.

That ECU is now a paperweight until he finds a BDM-capable programmer, identifies the boot access pins, and connects at the hardware level to force a recovery — a process that will take him three hours, assuming he has the right tools. If he doesn't, the replacement ECU he paid for is junk.

The lesson we start with today: backup first, always. No exceptions. Not when it seems simple. Not when it's a five-minute job. Not when you've done this ECU fifty times. Backup first."

**Instructor note:** Pause after the final line. Let the room sit with it for three to five seconds. Then move to the first slide.

---

## Section 1: Three Programming Modes (25 minutes)

### Slide 1 — Section Title

**Title:** "Three Ways In — Three Levels of Access"

**Instructor notes:** Frame this section as a hierarchy of access depth. OBD is the surface layer. Bench goes deeper. Boot mode goes to the hardware level. Each layer unlocks more capability and carries more responsibility.

---

### Slide 2 — OBD Mode Overview

**Title:** "OBD Mode — The Normal Entry Point"

**Content:**
- Scan tool connects through vehicle OBD-II port (DLC)
- Communication protocols: ISO 15765-4 (CAN) for post-2008 vehicles; ISO 9141 / ISO 14230 (K-Line) for older platforms
- ECU is in its normal operating power state — ignition on, BCM active, all modules communicating normally
- Programmer sends programming session request (UDS: 0x10 02 or 0x10 03 — extended or programming diagnostic session) → ECU authenticates session → programming proceeds

**What OBD mode CAN do:**
- Update firmware where OEM allows it (reflash via OBD)
- Adaptation reset
- Fault clear
- Coding changes (variant coding, option coding)
- Immobilizer adaptation (with correct access level)

**What OBD mode CANNOT do:**
- Read calibration areas the manufacturer has locked (fuel maps, boost tables — these are often manufacturer-locked)
- Access memory regions below the application layer
- Recover an ECU that isn't communicating
- Write to ECUs that require proprietary Seed/Key access levels not supported by aftermarket tools

**Physical connector:** OBD port (DLC) under dash, pin 6/14 for CAN-H/L, pin 7 for K-Line, pin 16 power/ground

**Instructor notes:** Ask the room: "How many of you have used a scan tool to clear fault codes? That was OBD mode. This is the same access layer — just a more powerful version."

---

### Slide 3 — Bench Mode Overview

**Title:** "Bench Mode — Removed ECU, Direct Connection"

**Content:**
- ECU is removed from the vehicle
- Programmer connects via an ECU-specific bench harness — a custom cable that plugs into the ECU's OEM connector(s) and routes the same pins that would be connected in the car
- Programmer communicates directly with ECU — no vehicle bus, no other modules
- Bench power supply provides +12V/+14V, provides grounds

**What bench mode CAN do that OBD cannot:**
- Read complete FLASH memory, including manufacturer-restricted areas
- Read calibration maps (fuel, ignition, boost, Lambda) for tuning/cloning
- Write to protected memory regions
- Access ECU at higher memory address ranges
- Faster transfer speeds (not limited by OBD bus arbitration)
- Some ECU families only allow complete cloning or EEPROM reads from bench mode

**Harness requirement:** Every ECU needs a specific bench harness matching its connector type (usually 60-pin, 121-pin, 154-pin Bosch connectors, or Delphi/Siemens equivalents). These harnesses are ECU-family specific. Kess V3 and KTM Bench both supply harness ranges with tool subscription.

**Bench mode does NOT:**
- Bypass security seed/key on ECUs with JTAG-protection enabled
- Work when ECU hardware is damaged (e.g., if power supply rails on ECU PCB are damaged)

**Common platforms used in bench mode:** Bosch ME7.x (Golf/Audi 1.8T), Bosch EDC16/EDC17 (TDI diesel), Siemens SID, Delphi DCM series

**Instructor notes:** "Bench mode is where tuners live. But it's also where you live when you're doing an EEPROM read to clone a replacement ECU — OBD won't give you the EEPROM, bench will."

---

### Slide 4 — Boot Mode Overview

**Title:** "Boot Mode — Below the Firmware Level"

**Content:**
- Boot mode bypasses the ECU's application firmware entirely
- Access goes directly to the MCU's primary bootloader — the ROM code that was programmed at the factory before the ECU firmware was written
- The primary bootloader is always present, even if the application FLASH is completely erased or corrupted
- Boot mode communicates with the MCU directly via debug/programming interfaces built into the silicon

**Why boot mode exists in this context:**
- ECU firmware was interrupted during programming → secondary bootloader corrupted → ECU won't communicate by OBD or bench
- ECU needs JTAG-unlocking before bench mode can read protected areas
- Cloning an ECU where the EEPROM is encrypted and the key is locked behind hardware access

**What boot mode can do:**
- Read and write raw FLASH and EEPROM, byte-for-byte, regardless of firmware state
- Recover an ECU that appears completely dead (no OBD, no bench communication)
- Read locked calibration areas that bench mode cannot reach (if hardware security is not fused)
- Write a new secondary bootloader when old one is corrupted

**Boot mode access methods (preview — detailed in Session 14T):**
- JTAG
- BDM (Background Debug Mode)
- SPI (direct FLASH chip access)
- UART boot entry

**Instructor notes:** "This is the session's deepest concept. Don't expect students to fully understand boot mode from this slide. It is previewed here so students understand why it exists in the mode hierarchy. Session 14T covers it in full."

---

### Slide 5 — The Three Modes Side-by-Side

**Title:** "Comparing the Three Modes"

**Visual suggestion:** Three-column table

| | OBD Mode | Bench Mode | Boot Mode |
|---|---|---|---|
| ECU location | In vehicle | Removed | Removed (or in circuit) |
| ECU firmware required | Yes — must communicate normally | Yes — must communicate | No — bypasses firmware |
| Connection | OBD port (DLC) | Direct ECU connector harness | JTAG / BDM / SPI / UART pins |
| Read depth | Application layer only | Full FLASH + EEPROM | Full raw hardware memory |
| Write capability | Limited (OEM allowed areas) | Extended (calibration, full FLASH) | Complete (entire MCU memory space) |
| Recovery when bricked? | No | No | Yes |
| Tool examples | Scan tools, Kess V3 OBD | KTM Bench, Kess V3 Bench, K-TAG | K-TAG BDM, J-Link, CH341A + SOIC clip |
| Skill level | Entry | Intermediate | Advanced |

**Instructor notes:** Walk through each row. Ask students to identify which scenario on the board would use which mode. Give three written scenarios and call on students to match: (1) firmware update on a car that drives fine, (2) full FLASH read of a removed ECU for tuning, (3) recovery of an ECU that went silent mid-flash.

---

### Slide 6 — Decision Framework: Choosing the Right Mode

**Title:** "Which Mode Do I Use?"

**Decision questions (flowchart logic):**

1. Is the ECU installed in the vehicle and communicating normally via OBD?
   - Yes → Start with OBD mode if the task can be done at OBD level
   - No → Move to bench or boot

2. Is the ECU removed or do you need full FLASH/calibration access?
   - Yes → Bench mode
   - No (ECU in car, OBD sufficient) → OBD mode

3. Does the ECU fail to respond to bench mode?
   - Yes → Boot mode (check which boot access method applies to this MCU type)
   - No → Bench mode

**Rule of thumb:** Always try the least-invasive mode first. OBD before bench. Bench before boot. Each step up in access depth carries higher risk of irreversible damage if something goes wrong.

**Instructor notes:** This slide is worth five minutes of discussion. Students who jump straight to boot mode "because it's more powerful" will damage ECUs. The hierarchy matters.

---

## Section 2: The Read-Backup-Write-Verify Workflow (20 minutes)

### Slide 7 — Section Title

**Title:** "The Four Steps That Cannot Be Skipped"

**Instructor notes:** "This is not a best practice. This is the standard procedure for every ECU programming job. A technician who skips step 2 — the backup — is one power interruption away from an unrecoverable ECU. Walk every student through this before the afternoon practical."

---

### Slide 8 — Step 1: READ

**Title:** "Step 1 — Read the ECU"

**Content:**

Before any change is made to any ECU, a complete read of the entire ECU memory must be performed. This means:
- Full FLASH read (all sectors)
- EEPROM read (if separately accessible)
- The read must complete without errors — do not proceed to step 2 with a partial or error-flagged read

**What the read captures:**
- The current ECU firmware (application code)
- Calibration data (maps, tables, adaptation values)
- EEPROM data (mileage in some ECUs, adaptation learned values, immobilizer data in some platforms)
- The ECU's current state — exactly as it was before you touched it

**Why it matters:** If anything goes wrong during the write — power cut, communication error, wrong file — the read is your only way back. Without the read, you have no reference point and no recovery file.

**Read duration:** Varies by ECU and mode. OBD reads: 3–15 minutes. Bench reads: 30 seconds–5 minutes. Boot/SPI reads: 1–10 minutes depending on FLASH size.

**Instructor notes:** "The read has no risk. Nothing is being changed. There is zero reason to skip it. It costs you three minutes. Not doing it can cost your customer an ECU."

---

### Slide 9 — Step 2: BACKUP

**Title:** "Step 2 — Save the Backup (Before Anything Else)"

**Content:**

The read file must be saved — correctly named, in multiple locations — before proceeding to any write operation.

**Naming convention (mandatory):**

```
DATE_VEHICLE-MAKE-MODEL-YEAR_ECU-TYPE_VIN-LAST-8_READ.bin

Example:
20260218_BMW-3SERIES-2019_ME17.9.10_AB12CD34_READ.bin
```

Field breakdown:
- DATE: YYYYMMDD format — unambiguous, sorts chronologically
- VEHICLE: Make + Model + Year (no spaces — use hyphens)
- ECU-TYPE: The programmer's identification of the ECU family/variant
- VIN-LAST-8: Last 8 characters of the vehicle VIN — ties the file to the specific car
- READ: Distinguishes the original read from subsequent files (POST-WRITE, RECOVERY, etc.)

**Storage requirement:** Save to two separate physical locations minimum:
- Local laptop/workstation folder (organised by job date or VIN)
- External USB drive or workshop NAS/server
- Cloud backup recommended as third copy

**Why two locations:** A laptop failure or theft loses the only copy. The backup file IS the insurance policy. Treat it as such.

**Common failure:** Technician reads the ECU, saves the file with a generic name like "read.bin" to the desktop, then proceeds to write. A week later, needing to recover a different ECU, they find five files called "read.bin" with no way to match them to the correct vehicle. Naming convention is not bureaucracy — it is functional.

**Instructor notes:** "Show a screenshot of a badly named backup folder on the projector. Then show a well-organised one. Students remember the contrast."

---

### Slide 10 — Step 3: WRITE

**Title:** "Step 3 — Write the Target File"

**Content:**

Only after the backup is confirmed saved (correct name, two locations, file size verified) does the write operation begin.

**Before initiating write — mandatory checks:**
1. Confirm the write file is correct for this specific ECU variant — not just the same part number family, but the same exact variant (check against vehicle VIN, engine code, gearbox type, market)
2. Confirm the file format is what the tool expects — .bin vs. .hex vs. .mot; mismatched format can result in garbage data being written
3. Confirm ECU power supply is stable — bench supply at 13.5–14.2V, current capacity at least 3A (some ECUs draw spike current during FLASH erase cycles)
4. Do not plan to interrupt: announce to everyone at the bench that a write is in progress — no one touches power, USB, or communication cables until the tool reports completion

**During write — do not:**
- Cut power
- Unplug USB or harness connectors
- Close the programming software
- Let the laptop go to sleep (disable sleep before starting)

**Write duration:** Similar to read — typically 1–10 minutes depending on mode and ECU type.

**Instructor notes:** "The write step is where the danger lives. Everything before this is reversible. Once you start writing, you are committed. Make sure the three checks are done before you hit 'write.'"

---

### Slide 11 — Step 4: VERIFY

**Title:** "Step 4 — Verify the Write"

**Content:**

After the tool reports write success, the job is not done. Perform a second full read and compare it to the intended write file.

**Verification procedure:**
1. Perform a second full read immediately after write completes
2. Save this file as: DATE_VEHICLE_ECU-TYPE_VIN8_POST-WRITE-VERIFY.bin
3. Compare the post-write read against the write file using a hex comparison tool (HxD, Beyond Compare, or the programming software's built-in compare function)

**What to look for:**
- Files should be byte-for-byte identical, OR
- Known expected differences: some programming tools recalculate and write a checksum byte during the programming process — this will show as a difference in the verification compare; this is normal IF the tool has documented this behaviour; know your tool's behaviour for this ECU type

**If verification fails (files do not match):**
- Do not reconnect to vehicle
- Power cycle the ECU
- Perform another full read — assess if the post-write content looks like the intended file or like something else
- If still wrong: restore from original backup using the same write procedure
- If restoration fails: boot mode recovery required

**Why the verification matters:** The tool says "success" based on completion of the programming protocol exchange — it does not always mean every byte was correctly written. The post-write read is independent verification.

**Instructor notes:** "I have seen Kess V3 report 'programming complete' on an ECU where the FLASH chip had a failing sector. The write 'completed' but the sector didn't take. The verify caught it. The tool's success message did not."

---

### Slide 12 — The Four Steps Together

**Title:** "Read → Backup → Write → Verify: The Complete Workflow"

**Visual suggestion:** Horizontal four-step process flow with decision point after verify (match = proceed; no match = restore or recover)

**Key summary points:**
- READ: always first, always complete
- BACKUP: before write, two locations, correct naming
- WRITE: only after backup confirmed; three pre-write checks completed
- VERIFY: independent read comparison; tool's success message is not enough

**The rule:** If you cannot complete all four steps, you do not proceed to write. A job that can only be completed with three steps is a job that needs to be rescheduled or escalated.

**Instructor notes:** "Print this flow diagram on A4 and give one to each student. It goes on the wall at their workstation for the rest of Module 6."

---

## Section 3: ECU File Formats (10 minutes)

### Slide 13 — Section Title

**Title:** "File Formats — Knowing What You're Working With"

**Instructor notes:** "This section is often skipped in training. Don't skip it. Writing the wrong format to a tool that expects a different format produces garbage data in the ECU. That's a bricked ECU from a format error — one of the most preventable failures."

---

### Slide 14 — .bin (Binary)

**Title:** ".bin — Raw Binary"

**Content:**

- Format: raw binary — byte-for-byte copy of the memory contents
- Structure: no header, no address information, no checksum markers embedded in the file structure; the file IS the memory, byte-for-byte from address 0x000000 to the end of the FLASH space
- File size: matches the FLASH chip size exactly. A 1MB FLASH = 1,048,576 byte .bin file. A 4MB FLASH = 4,194,304 bytes.
- How to verify: check file size in bytes, compare to known FLASH size for this ECU type
- When used: bench mode reads and writes (most common); boot mode / SPI reads; cloning operations
- Tooling: all bench programming tools use .bin as primary format; HxD for hex editing and comparison

**Common mistake:** A .bin file for one ECU written to a different ECU — even if the FLASH sizes match — will contain wrong firmware. .bin has no internal checks to stop you doing this.

---

### Slide 15 — .hex (Intel HEX)

**Title:** ".hex — Intel HEX Format"

**Content:**

- Format: ASCII text file; human-readable in a text editor
- Structure: each line contains: start code (:), byte count, address, record type, data bytes, checksum
- Example line: `:10 0100 00 214601360121470136007EFE09D21901 40`
- Preserves memory addressing: unlike .bin, the file records which memory addresses the data belongs to; gaps in the address space are represented correctly (no padding required)
- File size: larger than .bin for the same data content (ASCII encoding overhead)
- When used: MCU programming in development environments; OBD firmware updates on some platforms; some older Bosch ECU programming tools
- Common tools: avrdude (AVR MCUs), ST-LINK Utility (STM32), Microchip MPLAB

**Why this matters for ECU repair:** Some older diagnostic tools and some OEM update files distribute firmware as .hex. The technician must confirm whether the tool expects .bin or .hex before proceeding. Most bench mode tools (Kess V3, KTM Bench) use .bin and will not correctly import .hex — the tool may accept the file but write garbage.

---

### Slide 16 — .mot / .srec and .s19

**Title:** ".mot, .srec, .s19 — Motorola S-Record Formats"

**Content:**

**Motorola S-Record (.mot, .srec):**
- ASCII format, similar function to Intel HEX but different structure
- S-Record line types: S0 (header), S1/S2/S3 (data with 16/24/32-bit address), S7/S8/S9 (end record)
- Example line: `S1130000285F245F2212226A000424290008237C2A`
- Developed by Motorola for their 68xx and 683xx MCU families
- Still common in Freescale/NXP ecosystem — the automotive MCUs based on Freescale 9S12, MPC5xx, and SPC5xx families

**.s19 format:**
- Subset of Motorola S-Record using only S1 records (16-bit addressing)
- Very common in Bosch ME7.x and Bosch EDC15/16 era ECU tooling — some original Bosch service tools and third-party tools distribute ECU software as .s19
- Can be opened in a text editor and should show recognisable S-Record structure

**Practical note:** KTM Bench and K-TAG both handle .s19 and .mot natively for the relevant ECU families. The user must select the correct file type in the tool's import dialogue. If the tool shows a "format error" or the file size on import looks wrong, the format selection is likely incorrect.

---

### Slide 17 — Format Summary and Common Mistakes

**Title:** "File Formats — Summary and Pitfalls"

**Visual suggestion:** Table

| Format | Structure | Size vs. FLASH | Common Use in ECU Work | Editable in Text Editor? |
|---|---|---|---|---|
| .bin | Raw binary | Exact match | Bench reads/writes, cloning | No (hex editor required) |
| .hex | Intel HEX ASCII | Larger | OBD updates, MCU dev tools | Yes |
| .mot / .srec | Motorola S-Record ASCII | Larger | Freescale/NXP MCU tooling | Yes |
| .s19 | Motorola S1-only subset | Larger | Bosch ME7, EDC15/16 tooling | Yes |

**Top three format-related mistakes:**
1. Writing a .hex file through a tool expecting .bin — the tool may process it and write ASCII code as if it were raw binary → corrupted firmware
2. Renaming a .bin file to .hex — changing the extension does not change the file format; the file is still binary, the extension is misleading
3. Assuming same extension = same format — two files both named .bin may have come from tools that stored them slightly differently (e.g., with or without tool-specific header appended); always check file size and, if possible, the first bytes in a hex editor

**Instructor notes:** "Show HxD briefly at the bench or on projector — open a .bin and a .s19 of the same ECU type. Students should see the difference immediately. .s19 is clearly text. .bin is clearly binary data."

---

## Section 4: Programming Tools Overview (10 minutes)

### Slide 18 — Section Title

**Title:** "The Tools — What's in the Industry"

**Instructor notes:** "We are not endorsing any specific tool brand as superior. We are familiarising students with the tools they will encounter in real workshops. The practical uses KTM Bench (or equivalent available in this facility). The principles transfer to any tool."

---

### Slide 19 — KTM Bench

**Title:** "KTM Bench"

**Content:**

- Mode: bench mode (primary), some boot mode capability
- Access: direct ECU connector harness; ECU-specific harness adapters
- Strong platforms: VAG group (VW/Audi/Skoda/Seat), PSA group (Peugeot/Citroen), Renault
- ECU coverage: Bosch ME(D)17, Bosch EDC17, Siemens SID, Delphi DCM, Continental ECUs
- License model: annual subscription with periodic coverage updates; harnesses purchased separately or as kits
- Software: Windows-based; ECU detection driven by harness selection and auto-detect
- Read speed: typically 1–3 minutes for full FLASH on common ECUs
- Advantages: dedicated bench tool (no credits per read/write — subscription model); good harness coverage; hardware is robust
- Limitations: primarily bench mode; boot mode coverage more limited than K-TAG; requires ECU-specific harness for each ECU family

---

### Slide 20 — Kess V3

**Title:** "Kess V3"

**Content:**

- Mode: OBD mode + bench mode (unified tool)
- Connectivity: OBD cable for OBD mode; bench harness for bench mode
- Strong platforms: broad multi-brand coverage; strong on European passenger cars and light commercial
- License model: credit-based — each read or write operation consumes credits; credits purchased in bundles; online server validation required for each operation
- Software: Alientech software suite; cloud-connected
- Read/write: initiated online with server authentication; credits debited per operation
- Advantages: single tool for OBD and bench; very wide vehicle coverage; well-supported in industry; good technical documentation from Alientech
- Limitations: credit cost per operation adds up on high-volume workshops; requires internet connection for every operation; tool is borrowed, not owned outright for new ECU additions (coverage is subscription)
- Common in: independent tuning shops, mobile remappers, aftermarket ECU programming specialists

---

### Slide 21 — K-TAG

**Title:** "K-TAG"

**Content:**

- Mode: bench mode + boot mode (BDM and JTAG capable)
- Strength: lower-level access — specifically designed for in-circuit and direct chip programming, BDM access, and JTAG on supported MCUs
- Strong platforms: older Bosch ECUs (ME7, EDC15, EDC16), Freescale HC(S)12 MCU-based ECUs
- BDM capability: connects to BDM header on ECU PCB; accesses Freescale HC12/HCS12/MPC5xx MCUs directly
- Used when: Kess V3 and KTM Bench cannot reach the required memory areas; ECU requires BDM-level access for a clone; secondary bootloader is not present or corrupt
- License model: similar subscription/credit model to Kess V3 (Alientech product family)
- Physical connection: proprietary K-TAG interface box → BDM cable → BDM pins on ECU PCB

---

### Slide 22 — Other Tools

**Title:** "Other Tools in the Ecosystem"

**VVDI (Xhorse):**
- Primarily immobilizer and key programming
- Includes ECU read capability on specific platforms (primarily transponder and immobilizer areas)
- Relevant in Module 6 context: VVDI Prog reads EEPROM (93xx, 24xx, 25xx series chips) and some MCU types for immobilizer data
- Not a general-purpose full FLASH programmer — use for immobilizer EEPROM work, not full ECU firmware reads

**MPPS / PCMFlash / WinOLS:**
- MPPS: budget OBD/bench programmer; limited coverage; common in budget workshops
- PCMFlash: OBD-mode programmer with reasonable coverage; popular in Eastern Europe and CIS markets; includes some direct read capability
- WinOLS: not a programmer — a map editing and checksum tool; after reading with Kess/KTM, WinOLS is used to edit calibration maps and correct checksums before writing back

**Generic SPI programmers (CH341A, RT809H, T48):**
- Direct chip programming via SPI interface
- Used for FLASH and EEPROM chip reading/writing at hardware level
- No ECU-level protocol — raw hardware access
- Used in boot mode / direct chip access scenarios (detailed in Session 14T and 14H)

**Instructor notes:** "Students will encounter all of these in the industry. The key takeaway: know what each tool's mode depth is. A MPPS is not K-TAG. A Kess V3 in OBD mode is not Kess V3 in bench mode."

---

### Slide 23 — What All Tools Have in Common

**Title:** "Universal Tool Requirements"

**Content:**

Regardless of which tool you use, the following apply:

1. **ECU identification must be confirmed before any operation** — the tool must correctly identify the ECU type, MCU, and FLASH size; if the identification fails or looks wrong, stop and investigate before proceeding

2. **Correct cable/adapter for the physical connection** — every ECU has a specific harness requirement; substituting a similar-looking harness can result in incorrect pin connections and ECU damage

3. **License/subscription must be active** — a tool with an expired license will either refuse to operate or (worse) operate in a degraded mode that may not provide correct error messages

4. **Stable power supply to ECU during operation** — fluctuating supply voltage during FLASH erase/write causes sector write failures; use a regulated bench supply, not a battery charger with cycling behaviour

5. **Laptop battery / mains power** — program from mains power only; a laptop battery dying mid-write is a brick

**Instructor notes:** "None of these are optional. Point 5 happens to students in training all the time. Laptops go to sleep or batteries die. Before the practical: check mains power, check laptop sleep settings."

---

## Climax and Resolution (10 minutes)

### Slide 24 — Climax

**Title:** "Programming Is Not Difficult — But It Is Unforgiving"

**Content (instructor speaks to this slide, minimal text):**

"ECU programming is not technically complex. The tools make it accessible. The procedure is straightforward: read, backup, write, verify. Every step is well-documented. The equipment exists to make it reliable.

What makes ECU programming difficult is not the skill — it is the discipline. The backup step that 'doesn't feel necessary' on a simple job. The file format check that gets skipped when you're in a hurry. The verify step that seems redundant after the tool said 'success.'

A failed write WITH a backup is a five-minute fix. Load the backup, write it back, done. The ECU returns to its original state. The customer's car is safe.

A failed write WITHOUT a backup is a recovery job. At minimum, that is two to three hours with boot mode tools, assuming you have the right equipment. In some cases, it is an ECU that cannot be recovered without component-level repair.

The backup is not a precaution. It is the difference between a recoverable situation and an unrecoverable one."

---

### Slide 25 — Preview: Session 13H

**Title:** "This Afternoon — You Do It"

**Content:**

Session 13H (this afternoon) is the full read-backup-write-verify practical.

You will:
- Connect a KTM Bench (or equivalent) to a sample ECU on a bench harness
- Perform a complete full read
- Save the backup with the correct naming convention
- Receive a pre-verified write file from the instructor
- Write the file and perform a post-write comparison

You will be assessed on Checkpoint 2 (backup saved correctly) before the instructor will allow any write to proceed. The practical models exactly the workflow from today's theory.

Come prepared: know the naming convention before you arrive. It is on your session brief.

---

## Timing Guide

| Section | Content | Duration | Cumulative |
|---|---|---|---|
| Hook | The disaster story | 5 min | 5 min |
| Section 1 | Three programming modes — slides 2–5 | 20 min | 25 min |
| Section 1 | Decision framework — slide 6 | 5 min | 30 min |
| Transition | Questions, brief summary | 3 min | 33 min |
| Section 2 | Read-Backup-Write-Verify — slides 7–12 | 20 min | 53 min |
| Transition | Questions | 2 min | 55 min |
| Section 3 | File formats — slides 13–17 | 10 min | 65 min |
| Section 4 | Tools overview — slides 18–23 | 10 min | 75 min |
| Climax & Resolution | Slides 24–25 | 10 min | 85 min |
| Buffer / Late questions | — | 5 min | 90 min |

---

## Instructor Notes — Full Session

**Room setup:** Projector with HxD or equivalent hex viewer accessible from taskbar. Workshop PC should have a pre-prepared folder showing a well-organised backup library and a badly-organised one (for the naming convention contrast moment on Slide 9).

**Key messages to reinforce throughout:**
1. Backup first, always — no exceptions
2. Mode selection is a decision based on access needed and ECU state
3. The tool's "success" message is not verification — only the post-write read is verification
4. File format matters — format mismatch produces garbage, and garbage damages ECUs

**Common student misconceptions to pre-empt:**
- "My tool auto-detects everything so I don't need to check" — auto-detect works when the ECU is in database; it fails silently on edge cases; always verify detection result matches physical ECU
- "Bench mode reads are the same as OBD reads" — they are not; bench reads access memory regions OBD cannot; the file contents will differ
- "I've done this ECU before so I know what file to write" — vehicle variant matters; same part number does not mean same variant; always verify file against VIN

**Pace management:** The hook and Section 2 (backup workflow) are the highest-priority content. If running behind, the tools overview (Section 4) can be condensed — it is largely preview material for what students will use in the practical. Slides 19–22 can be shown quickly with verbal summary rather than detailed explanation.

**Assessment hook at end of session:** Verbally preview the three theory test questions so students know exactly what they will be tested on. This is not giving away answers — it is aligning expectations.

---

## Pre-Reading / Student Preparation

- Review Module 4 CAN bus session notes (CAN protocol basics will appear in OBD mode discussion)
- Print naming convention card from the student resource folder (LMS/shared drive)
- Review the ECU type for the afternoon practical — identification reference posted on shared drive

---

## Resources Required

- Projector and workshop PC
- HxD (or equivalent hex editor) installed on workshop PC — open with a sample .bin and .s19 for the format demonstration (Slide 17)
- Pre-prepared backup folder examples (well-organised vs. poorly-organised) on desktop for Slide 9
- A4 printout of the four-step workflow for each student (laminated preferred)
- Naming convention reference card per student (double-sided A5)
- Assessment alignment reference for instructor record-keeping

---

*Module 6 | Day 13 Theory | ECUHR | v1.0 | 2026-02-18*
