# SESSION-14T: Online Coding, Bootloader Architecture & ECU Recovery
## Theory Session | Day 14 | Module 6: ECU Programming & Bootloader

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 6 — ECU Programming & Bootloader
**Day:** 14 | **Session Type:** Theory
**Duration:** 90 minutes
**CO Alignment:** co-3

---

## Session Outcomes

| SO Code | Outcome Statement | Bloom's Level |
|---|---|---|
| so-6-3-1 | Explain what online coding is, why it requires manufacturer server authentication, and which ECU types require it | Understand |
| so-6-4-1 | Explain bootloader architecture (primary vs secondary), boot mode trigger mechanisms, and the difference between JTAG, BDM, SPI, and UART boot access | Understand |
| so-6-5-1 | Diagnose a bricked ECU (no OBD communication after failed flash) and identify the appropriate recovery method | Analyze |

---

## Assessment Alignment

| SO Code | Assessment Item | Method | Weight |
|---|---|---|---|
| so-6-3-1 | Q4 Theory Test M6: Identify which ECU type requires online coding and state why | Written short answer | Module 6 theory test |
| so-6-4-1 | Q5 Theory Test M6: Match JTAG/BDM/SPI/UART to a scenario description | Written MCQ | Module 6 theory test |
| so-6-5-1 | Q6 Theory Test M6: Given symptoms (ECU silent after flash), select correct diagnosis and recovery path | Written scenario | Module 6 theory test |
| so-6-5-1 | Practical check-off 14H Station 4: student correctly diagnoses bricked ECU symptom before recovery | Observation | Session 14H |
| so-6-4-1 | Practical check-off 14H Station 2: student correctly identifies boot access pins before connecting programmer | Observation | Session 14H |

---

## Session Overview

**Session Role in Module:** This is the most technically advanced theory session in Module 6. Session 13T established the programming fundamentals and the read-backup-write-verify workflow. This session goes deeper: what happens when the normal path fails — when online coding requires manufacturer authentication, or when the secondary bootloader is corrupted and the ECU no longer responds to any normal approach. The culminating concept is boot mode access — the hardware-level recovery path that this course has been building toward since Day 1.

**Prerequisite Knowledge:** Students must have completed Session 13T and 13H. They should know: the three programming modes (OBD, bench, boot), the read-backup-write-verify workflow, and how to connect a bench programmer. Session 14H immediately follows — this theory session is the direct preparation for the afternoon boot mode practical.

**Session Flow Summary:**
- Hook (5 min)
- Online coding and variant coding (20 min)
- Bootloader architecture (25 min)
- Boot mode access methods — JTAG, BDM, SPI, UART (20 min)
- Diagnosing a bricked ECU (10 min)
- Climax, resolution, preview (10 min)

---

## Hook — The ECU That Wouldn't Wake Up (5 minutes)

**Delivery:** Verbal story. No slides. Instructor stands at the bench — not at the projector — to signal this is hands-on territory.

**The Story:**

"A technician in a busy workshop gets a 2015 VW Golf 2.0 TDI in for a variant coding job — the owner wants cruise control enabled. The technician connects VCDS, opens the engine control module, and begins the variant coding procedure.

Halfway through, his laptop drops off the network. The coding session times out. The ECU is mid-write. The scan tool loses communication.

He cycles the ignition. The engine turns over — but won't fire. He connects a scan tool: no communication with the ECU whatsoever. Not even a response to a basic identifier request. The ECU is silent.

He's just bricked a running car.

He calls the tool support line. They walk him through re-initiating the OBD session. Nothing. He tries bench mode with KTM Bench. Still no response. The secondary bootloader — the part of the firmware that allows the programming tool to talk to the ECU — was partially overwritten when the session dropped. The ECU's application firmware can't run, and the secondary bootloader can't receive a new firmware write. Normal programming channels are closed.

What he needed next — what would have saved that car in forty minutes — was boot mode access. Direct hardware-level access to the primary bootloader, the ROM code that is factory-programmed into the MCU and cannot be overwritten. The primary bootloader is always alive, even when everything else on the ECU is corrupted.

He didn't have the right tool. He didn't know how to find the boot pins on that PCB. The car spent four days waiting for an ECU specialist who did.

This afternoon, you will be that specialist. Today's theory tells you how."

**Instructor note:** Pause. Let the last sentence land. Move to the projector.

---

## Section 1: Online Coding and Variant Coding (20 minutes)

### Slide 1 — Section Title

**Title:** "Online Coding — When the Car Must Call Home"

**Instructor notes:** "Most programming operations you've learned so far are offline — you have the ECU, the tool, and the file. Online coding adds a third party: the manufacturer's server. Understand why, and you'll understand why some ECU types require it."

---

### Slide 2 — What Online Coding Is

**Title:** "Online Coding — Definition"

**Content:**

Online coding is a programming procedure in which the diagnostic tool must establish a live connection to the manufacturer's authorisation server to complete the operation.

The ECU cannot accept the new coding values without a server-generated cryptographic session token. The sequence is:

1. Technician initiates coding session on the scan tool
2. Tool sends vehicle VIN, ECU identification, and technician/workshop credentials to manufacturer server
3. Server validates the request — confirms the ECU is registered to that VIN, confirms the requested coding is valid for that market/specification
4. Server issues a session authorisation token — time-limited (usually 15–30 minutes)
5. Tool applies the authorisation and proceeds with the coding write
6. Some platforms: server logs the coding change against the vehicle's digital identity record

**Why it requires server authentication:**
- Prevents unregistered workshops from enabling features (e.g., enabling features on a vehicle outside its market specification)
- Ties coding changes to a traceable workshop and technician ID
- Allows OEMs to audit and reverse unauthorised modifications
- Required by regulation in some markets for emissions-related ECU parameters

**Which ECU types commonly require online coding:**
- Modern VAG group (VW/Audi/Skoda/Seat from ~2018 onward) — ODIS online required for many module replacements and coding changes
- BMW/Mini — ISTA requires active TeleServices/BMW Group access for most module programming
- Mercedes — XENTRY online access required for SCN (System Calibration Number) coding
- Newer Stellantis (PSA/FCA) platforms — online authorisation for replacement module coding

**Important for the aftermarket:** Aftermarket tools (VCDS for VAG, iCarSoft, Launch) can often perform *variant coding* (changing options within the existing coding structure) without online access. But when the manufacturer requires server validation for a replacement module or a market-locked feature, aftermarket tools reach a hard limit. Knowing this boundary saves time — and a failed attempt will not brick the ECU.

---

### Slide 3 — Variant Coding and Adaptations

**Title:** "Variant Coding and Adaptations — The Offline Version"

**Content:**

**Variant coding:** Modifying the ECU's coding byte or long coding to enable or disable vehicle features.

How it works (VAG example using VCDS):
- Each coding byte encodes a set of binary options (bit 0 = feature enabled/disabled, bit 1 = next feature, etc.)
- The technician reads the current coding, interprets each bit using the coding guide, modifies the relevant bits, and writes back the new coding value
- Example: enabling front fog light wash cycle on a Golf — change bit 2 of coding byte 7 from 0 to 1

**Adaptation channels:** ECU memory locations that store learned values — learned from the vehicle or manually set. These are not firmware — they are persistent data in EEPROM or flash data sectors.

Common adaptation use cases:
- Throttle body adaptation after cleaning or replacement — reset learned throttle position values
- Transmission adaptation reset — reset learned shift points after gearbox repair or fluid change
- Steering angle sensor (SAS) calibration — set the neutral position of the steering angle sensor after alignment
- Injector coding — tell the ECU the coded trim values for each injector (on diesel common rail systems, each injector has a code stamped on it; this code must be entered into the ECU)

**Key difference from online coding:**
- Variant coding and adaptations are typically offline operations — no server required
- The ECU accepts the new values based on its internal diagnostic security access (UDS security levels), not server authorisation
- Aftermarket tools fully support most variant coding and adaptation procedures on common platforms

**Instructor notes:** "Know the distinction: variant coding = changing feature flags. Adaptation = resetting or setting learned values. Both are common workshop tasks. Online coding is the one that can stop you if you don't have the right access level."

---

### Slide 4 — Practical Warning: Coding vs. Programming

**Title:** "Coding ≠ Programming — A Critical Distinction"

**Content:**

| | Coding / Adaptation | Programming (FLASH write) |
|---|---|---|
| What changes | Feature flags, learned values | ECU firmware or calibration data |
| Risk level | Low — miscoded values can be reset | High — incorrect firmware can brick the ECU |
| Backup required before? | Recommended | Mandatory (no exceptions) |
| Recovery if wrong? | Reset or recode | Read-backup-write-verify; or boot mode if bricked |
| Example | Enabling cruise control via VCDS | Writing a new software version to the ECU FLASH |

**The practical consequence:** Students sometimes apply the urgency of "backup first" only to FLASH write operations. In fact, a miscoded ECU that doesn't start or doesn't communicate is still a bricked ECU from the customer's perspective — even if the cause was a coding session timeout, not a firmware write. The recovery method differs (usually just a recode), but the lesson is the same: know what you changed and how to undo it.

---

## Section 2: Bootloader Architecture (25 minutes)

### Slide 5 — Section Title

**Title:** "The Bootloader — What's Always Alive Inside the ECU"

**Instructor notes:** "This is the most conceptually important section of Module 6. The bootloader is why boot mode recovery works. If students don't understand the architecture, they can't understand why boot mode access can reach an ECU that bench mode cannot. Build this from the bottom up."

---

### Slide 6 — What a Bootloader Is

**Title:** "Bootloader Architecture — Two Layers"

**Content:**

A bootloader is a small program stored in the MCU that runs before the main application firmware. Its purpose is to manage firmware loading and updating. Every automotive ECU MCU has at least one.

**The two-layer architecture:**

**Primary Bootloader (ROM Bootloader / Factory Bootloader):**
- Written into the MCU's ROM (Read-Only Memory) or a protected flash sector at the chip factory — before the ECU firmware is ever written
- Cannot be erased or overwritten under any normal circumstances (it is in ROM or fuse-protected flash)
- Activated by physical hardware signals on specific MCU pins (boot mode trigger pins)
- Communicates via basic hardware interfaces: JTAG, BDM, SPI, UART — depending on MCU architecture
- This bootloader is alive even if the FLASH is completely blank or corrupted
- This is the recovery path

**Secondary Bootloader (Application Bootloader / Boot Manager):**
- Written into a protected sector of the ECU's application FLASH during the ECU manufacturing process
- Executed after the primary bootloader validates the MCU is in a normal run state (no boot mode pins triggered)
- Handles the normal programming workflow: receives firmware from the programming tool via CAN or K-Line using UDS/KWP2000 protocols
- This is what KTM Bench and Kess V3 communicate with during bench mode programming
- This bootloader CAN be overwritten — and a failed write that corrupts this sector is exactly how an ECU becomes "bricked"

**The failure point:** When a bench mode or OBD write is interrupted mid-flash, the secondary bootloader sector may be partially overwritten with incorrect data. The primary bootloader still works — but programming tools that communicate via CAN/K-Line have no path to the primary bootloader. The primary bootloader only listens on its hardware pins. This is the brick state.

---

### Slide 7 — Boot Mode Trigger Mechanisms

**Title:** "Triggering Boot Mode — How the Primary Bootloader Is Activated"

**Content:**

The primary bootloader is not normally active during ECU operation. It is activated by applying specific signals to designated MCU pins at power-on. The trigger mechanism depends on the MCU architecture.

**Common trigger methods:**

| MCU Family | Boot Mode Trigger |
|---|---|
| Freescale HC(S)12 | Assert BKGD pin low at power-on → activates Background Debug Mode (BDM) |
| Freescale MPC5xx | Assert RSTCFG pin; JTAG_TRST, TCK, TMS state at reset |
| NXP S32K (modern) | Assert specific UART boot pin or SWD (Serial Wire Debug) interface |
| Renesas SH-series | Mode pins (MD0/MD1/MD2) set to specific binary pattern at reset |
| STM32 (boot0/boot1) | BOOT0 pin held high at power-on → routes execution to ROM bootloader → UART/SPI/USB boot |
| SPC560 (SPC5x) | Assert JCOMP pin or specific JTAG sequence |

**What "at power-on" means in practice:**
- The boot mode trigger must be present BEFORE or simultaneously with power application to the MCU
- This means: hold the signal low (or high, depending on architecture), apply power, release — MCU starts in boot mode
- On a bench: this involves connecting the boot mode programmer to the correct pins BEFORE turning on the bench power supply
- On the ECU PCB: the boot mode trigger pins may be on a JTAG header, BDM header, or test points that must be identified from the datasheet

**Physical consequence:** Finding the boot mode pins on an ECU PCB requires:
1. Identifying the MCU type (package marking → datasheet)
2. Reading the MCU datasheet to find the boot mode trigger pins
3. Locating those pins on the PCB (either on the MCU footprint or routed to a header/test point)

---

### Slide 8 — JTAG

**Title:** "JTAG — The Debug Interface Standard"

**Content:**

**Full name:** Joint Test Action Group (the standards body that defined IEEE 1149.1)

**Purpose:** Originally designed for boundary-scan testing of PCBs after manufacturing (test every pin of every IC for open/short circuits without physical probing). Evolved into a hardware debug and programming interface.

**Pins (the standard 5-pin JTAG port):**
- **TDI** — Test Data In
- **TDO** — Test Data Out
- **TCK** — Test Clock
- **TMS** — Test Mode Select
- **TRST** — Test Reset (optional, some implementations omit this)

Plus VCC and GND.

**How it works:** The JTAG TAP (Test Access Port) is a state machine controlled by TMS. A JTAG programmer sequences the TAP through states to access the MCU's debug module, which provides read/write access to registers, memory, and the FLASH programming controller.

**ECU use cases:**
- Read and write MCU FLASH and RAM directly
- Access MCU registers for debug (step through code execution)
- Program MCUs that have never been programmed (blank devices)
- On protected devices: JTAG security fuses may lock out JTAG access after manufacturing — requires chip-specific unlocking sequence or fuse bypass (advanced topic)

**Common JTAG tools in ECU repair:** J-Link (Segger), ULINK (Keil), Lauterbach, OpenOCD with compatible adapters (for supported MCU targets)

**ECU context:** JTAG headers are often present on ECU PCBs as unpopulated footprints — the pads are there, the connector is not soldered. Requires fine-pitch probing or soldering a temporary connector.

---

### Slide 9 — BDM (Background Debug Mode)

**Title:** "BDM — Freescale's Single-Wire Debug Interface"

**Content:**

**Background Debug Mode (BDM)** is Motorola/Freescale's proprietary hardware debug interface for the HC11, HC12, HCS12, HCS12X, and MPC5xx MCU families. These MCUs are extremely common in ECU hardware from the 1990s through mid-2010s — Bosch ME7, EDC15, EDC16, and many others.

**Physical interface:**
- **Single data wire: BKGD (or BKGND)** — bidirectional half-duplex communication
- Plus VCC, GND, RESET
- Typically exposed on a **6-pin BDM header** on the ECU PCB (some ECUs have the header populated; many have only the pads)

**Activation:** Assert BKGD pin (hold low or pulse low at specific timing during power-up, depending on MCU variant) → MCU enters BDM mode, responds to BDM commands

**Capability:**
- Read and write all MCU memory (FLASH, EEPROM, RAM) at hardware level
- Not dependent on firmware state — primary bootloader handles BDM independently
- Allows recovery of an ECU with a corrupted secondary bootloader
- Allows reading of FLASH contents even on ECUs that have lock bits set (some HC12 security can be bypassed via BDM mass erase + reprogramme — erases FLASH including security byte, then reprogramme)

**K-TAG BDM mode:** K-TAG explicitly supports BDM access as a core feature for supported ECU families. The K-TAG interface connects to the ECU's BDM header via a BDM cable and provides the BDM signal conditioning and timing.

**BDM header location on ECU PCBs:** Usually a 6-pin 2.54mm or 1.27mm pitch unpopulated or populated connector near the MCU. Sometimes labelled "BDM", "DEBUG", or unlabelled — identified from MCU pinout mapping.

---

### Slide 10 — SPI (Direct FLASH Chip Access)

**Title:** "SPI Flash Programming — Bypassing the MCU Entirely"

**Content:**

**SPI (Serial Peripheral Interface)** is a four-wire serial communication protocol used to access external FLASH and EEPROM chips. On an ECU, the MCU stores firmware in an external SPI FLASH chip (separate from the MCU itself) on many ECU architectures.

**The external FLASH chip approach:**
- Some ECU architectures store the main application code in a dedicated external SPI FLASH IC (e.g., Winbond W25Q series, Macronix MX25L series, Microchip SST26VF series)
- The MCU loads firmware from this external chip at startup
- The external FLASH chip can be read and written directly via SPI — without the MCU being involved at all
- This bypasses the secondary bootloader entirely

**Physical access methods:**
1. **In-circuit via SPI clip (SOIC-8 clip):** A spring-loaded clip connects to the FLASH chip package (usually SOIC-8 or WSON-8 package) without desoldering — the programmer connects directly to the chip's SPI pins through the clip
2. **Desolder and programme externally:** Remove the FLASH chip, programme it in a ZIF socket programmer, resolder
3. **Via test points:** Some ECUs route SPI signals to accessible test points on the PCB

**SPI programming tools:**
- **CH341A + SOIC-8 clip** — inexpensive USB programmer; works well for common FLASH chips (Winbond, Macronix); Windows/Linux software (AsProgrammer, flashrom)
- **RT809H / T48** — wider chip support; faster; better for production use
- **Bus Pirate** — open-source multi-protocol interface; supported by flashrom
- **KTM Bench SPI mode** — KTM Bench includes SPI programming capability for supported ECUs as part of its functionality

**When SPI access is used in ECU repair:**
- ECU with corrupted firmware — read via SPI, repair firmware, write back
- EEPROM data extraction (mileage, immobilizer data) on ECUs with dedicated SPI EEPROM chips
- Recovery when the MCU's own bootloader cannot be reached (e.g., MCU boot mode pins inaccessible but external FLASH pins are reachable)

**Important note:** SPI in-circuit programming requires the programmer to drive the chip's CS (chip select) and the MCU to be held in reset or powered off during programming — otherwise the MCU and programmer both drive the SPI bus simultaneously, causing data corruption. Always check whether the MCU needs to be held in reset before applying SPI.

---

### Slide 11 — UART Boot

**Title:** "UART Boot — Software-Controlled Bootloader Entry"

**Content:**

**UART (Universal Asynchronous Receiver/Transmitter)** is a serial communication interface present on virtually all MCUs. Some MCU architectures expose their primary bootloader via UART, activated by a boot mode pin or GPIO state.

**How UART boot works:**
- Boot mode pin (e.g., BOOT0 on STM32) held high at power-on → MCU executes ROM bootloader
- ROM bootloader listens on UART interface for incoming firmware data
- Programming tool sends firmware in a defined protocol (STM32: AN3155 defines the UART bootloader protocol)
- Firmware is written to FLASH by the ROM bootloader

**ECU relevance:**
- STM32-based ECUs (some aftermarket ECUs, some OEM ECUs using STM32) support UART boot
- Some older Renesas MCUs expose UART-based flash writer interfaces
- Less common than JTAG/BDM/SPI in traditional OEM ECU hardware, but increasingly relevant in modern ECU architectures

**Practical use in recovery:**
- When JTAG is locked and external FLASH is not accessible, UART boot may provide a path if the MCU supports it
- Requires correct UART level shifter (3.3V logic typical; 5V will damage some MCUs) and correct baud rate (auto-detection or fixed rate from datasheet)
- Access pins are usually Tx/Rx on the MCU package — found on test points or via PCB tracing

---

### Slide 12 — Boot Mode Comparison Table

**Title:** "JTAG / BDM / SPI / UART — Side by Side"

**Visual suggestion:** Full-width comparison table

| | JTAG | BDM | SPI | UART |
|---|---|---|---|---|
| Developed by | IEEE 1149.1 | Motorola/Freescale | Various | Various |
| Common MCU families | ARM Cortex, Renesas, NEC/78K, MPC5xx | HC12, HCS12, HCS12X, MPC5xx | Any ECU with external SPI FLASH | STM32, Renesas, SPC5xx |
| Physical interface | 5-pin JTAG port (TDI/TDO/TCK/TMS/TRST) | 1-pin BKGD + RESET | 4-pin SPI (MOSI/MISO/SCK/CS) | 2-pin UART (Tx/Rx) |
| MCU required to be functional? | No — debug TAP is independent | No — BDM is independent | No — bypasses MCU | Partially — needs ROM bootloader |
| Bypasses secondary bootloader? | Yes | Yes | Yes (bypasses MCU entirely) | Yes (uses primary bootloader) |
| Recovery use in ECU repair | Yes — JTAG capable tools | Yes — K-TAG BDM primary use | Yes — CH341A + SOIC clip | Yes — specific MCU types |
| Typical tools | J-Link, ULINK, Lauterbach | K-TAG, BDMKIT | CH341A, RT809H, T48 | ST Link + UART adapter |

**Instructor notes:** "Students don't need to memorise this table — the afternoon practical will cement it. The key takeaway: four different physical interfaces, all leading to the same destination — hardware-level memory access that does not depend on the firmware being functional."

---

## Section 3: Diagnosing a Bricked ECU (10 minutes)

### Slide 13 — Section Title

**Title:** "ECU Won't Communicate — Systematic Diagnosis"

**Instructor notes:** "This section builds directly on the hook story. Now students know what a bricked ECU is architecturally, they can work through the diagnosis systematically."

---

### Slide 14 — Symptom Confirmation

**Title:** "Step 1 — Confirm the Brick (Not Everything Silent Is Bricked)"

**Content:**

Before assuming an ECU is bricked after a failed programming attempt, confirm:

**Check 1: Power supply**
- Is the ECU receiving correct supply voltage? (Bench: 13.5–14.2V; in-vehicle: ignition voltage at ECU connector)
- Is the ground connection solid? (Measure resistance from ECU ground pin to PSU negative — should be < 0.5Ω)
- A supply fault can produce the same symptom (no OBD communication) as a firmware failure

**Check 2: Communication interface**
- Is the CAN or K-Line connection wired correctly to the scan tool?
- Are CAN bus termination resistors present (should measure ~60Ω between CAN-H and CAN-L with ECU unpowered)?
- Is the scan tool firmware up to date and configured for the correct protocol?

**Check 3: ECU response**
- Connect an oscilloscope to the CAN-H/CAN-L or K-Line pin at the ECU connector
- Power on the ECU: is there ANY signal activity on the bus, even brief?
- Some bricked ECUs still transmit a few frames before failing (incomplete secondary bootloader); some produce no signal at all
- A completely silent ECU with confirmed power supply and communication wiring is the brick confirmation

**Only after ruling out power and communication faults does the diagnosis move to firmware failure.**

---

### Slide 15 — Recovery Path Selection

**Title:** "Step 2 — Selecting the Recovery Method"

**Content:**

Once the brick is confirmed (power good, comms wiring good, ECU silent), identify which recovery method applies:

**Decision path:**

1. **Is this an ECU with a known, accessible BDM header?** (Freescale HC12/HCS12-based ECU — Bosch ME7, EDC15, EDC16 era)
   → BDM recovery via K-TAG or compatible BDM programmer

2. **Is the MCU ARM Cortex-M or Renesas with JTAG accessible on the PCB?**
   → JTAG recovery via J-Link or equivalent

3. **Does the ECU have an external SPI FLASH chip?** (Visible SOIC-8 or WSON package near or separate from MCU)
   → SPI direct read/write via SOIC clip (CH341A or RT809H)

4. **Is the MCU a UART-boot capable device (STM32, SPC5xx with UART boot)?**
   → UART boot recovery

5. **Unknown MCU / inaccessible boot pins?**
   → Identify MCU type from package markings → datasheet research → locate boot access on PCB

**What you need to perform the recovery:**
- A confirmed good firmware file (the backup from before the failed write, or a known-good file for that exact ECU variant)
- The correct boot mode programmer for the recovery interface
- The correct pinout / test point locations on the PCB (from datasheet or ECU-specific wiring documentation)

**Instructor notes:** "Students often want a single tool that works on everything. That doesn't exist. The recovery path depends entirely on the MCU architecture in the specific ECU. This is why MCU identification is a core skill — covered in this afternoon's practical."

---

## Climax and Resolution (10 minutes)

### Slide 16 — Climax

**Title:** "Boot Mode Is Not a Last Resort — It Is the Foundation"

**Content (instructor speaks to this, minimal slide text):**

"Everything you've learned about ECU programming flows from one architectural fact: every MCU that runs automotive firmware was manufactured with a primary bootloader that exists independently of that firmware.

OBD mode, bench mode, secondary bootloaders, programming protocols — all of these are built on top of that foundation. They are convenience layers that make normal programming accessible. But when they fail — and they will fail, because every tool has bugs, every power supply can glitch, every network connection can drop — the primary bootloader is what's underneath.

A technician who understands boot mode is not just a better recovery specialist. They understand, at the architectural level, what every ECU really is: a piece of silicon that listens on a few hardware pins, waiting for instructions it was born knowing how to receive.

The shops that can recover bricked ECUs don't send cars back. They don't buy replacement modules they don't need. They don't tell customers 'the ECU needs to be replaced.' They connect to the hardware, restore the firmware, and hand the car back in forty minutes.

That is the practical skill this afternoon gives you."

---

### Slide 17 — Preview: Session 14H

**Title:** "This Afternoon — Boot Mode in Practice"

**Content:**

Session 14H (this afternoon) has four stations:

**Station 1 — Variant Coding and Adaptation (so-6-3-2, so-6-3-3)**
Perform a variant coding change and adaptation reset on a sample ECU using VCDS or equivalent. Verify changes were accepted.

**Station 2 — Boot Mode Pin Identification (so-6-4-2)**
Given a disassembled ECU, identify the MCU type, locate the datasheet, and mark the JTAG, BDM, or SPI boot access pins on a PCB diagram. Confirmed by instructor check-off before proceeding.

**Station 3 — SPI FLASH Read via In-Circuit Clip (so-6-4-3)**
Connect a CH341A programmer with SOIC-8 clip to the external FLASH chip of a sample ECU. Perform a complete SPI read and verify file integrity.

**Station 4 — Bricked ECU Recovery (so-6-5-2)**
Using a pre-bricked sample ECU (known failed write — secondary bootloader corrupted), perform a boot mode recovery by writing a known-good firmware file and confirming communication is restored.

Checkpoint 1 (boot pin identification confirmed) is required before Station 3 equipment is issued. Do not skip the identification step.

---

## Timing Guide

| Section | Content | Duration | Cumulative |
|---|---|---|---|
| Hook | The bricked Golf story | 5 min | 5 min |
| Section 1 | Online coding — slides 2–4 | 20 min | 25 min |
| Transition | Questions, brief summary | 3 min | 28 min |
| Section 2 | Bootloader architecture — slides 5–6 | 10 min | 38 min |
| Section 2 | Boot mode trigger mechanisms — slide 7 | 7 min | 45 min |
| Section 2 | JTAG, BDM, SPI, UART — slides 8–12 | 18 min | 63 min |
| Transition | Questions, comparison table walkthrough | 4 min | 67 min |
| Section 3 | Bricked ECU diagnosis — slides 13–15 | 10 min | 77 min |
| Climax & Resolution | Slides 16–17 | 10 min | 87 min |
| Buffer / Late questions | — | 3 min | 90 min |

---

## Instructor Notes — Full Session

**Room setup:** Have a sample ECU at the front bench with the lid removed. When covering BDM, physically point to where the BDM header is on that specific ECU (if applicable). When covering SPI, point to the external FLASH chip. Visual reference during theory dramatically improves retention.

**Key messages to reinforce throughout:**
1. The primary bootloader is always alive — this is what makes recovery possible
2. Boot mode access depends on the MCU architecture — identify the MCU first, then select the interface
3. Online coding ≠ variant coding — know which requires server connection
4. A bricked ECU is usually recoverable — the question is which interface to use

**Common student misconceptions to pre-empt:**
- "The ECU is dead" after a failed flash — the MCU is almost certainly alive; the secondary bootloader is what's damaged
- "BDM works on any ECU" — BDM is specific to Freescale HC/HCS12 and MPC5xx MCU families; other architectures use JTAG or SWD
- "I just need to get the SPI clip on and I can fix any ECU" — only ECUs with external SPI FLASH chips support this method; MCU-internal flash requires JTAG or BDM
- "Online coding and variant coding are the same thing" — online requires server authentication; variant coding is typically offline

**Pace management:** Sections 2 (bootloader architecture and boot interfaces) carries the most new conceptual content. Slides 8–11 (JTAG, BDM, SPI, UART) can be taught more quickly if time is short — the comparison table (Slide 12) is the key takeaway. Section 3 (diagnosis) must not be cut — it directly prepares students for the afternoon's Station 4 (bricked ECU recovery).

---

## Pre-Reading / Student Preparation

- Review the MCU identification section from Module 3 (processor types, package markings)
- Download and skim: CH341A programmer quick-start guide (on LMS)
- Review naming convention from Session 13T — needed for variant coding backup in 14H Station 1

---

## Resources Required

- Projector and workshop PC
- Sample ECU with lid removed for physical reference during boot mode pin section
- Printout of MCU datasheet relevant to sample ECU (for reference during slide 7 trigger mechanism discussion)
- Comparison table (Slide 12) printed as reference card — one per student
- Assessment alignment reference for instructor record-keeping

---

*Module 6 | Day 14 Theory | ECUHR | v1.0 | 2026-02-18*
