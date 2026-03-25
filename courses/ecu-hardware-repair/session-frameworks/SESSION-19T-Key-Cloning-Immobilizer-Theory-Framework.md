# SESSION-19T: Key Cloning, Lost Key Recovery & Immobilizer Programming
## Theory Session | Day 19 | Module 9: Security & Safety Systems

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 9 — Security & Safety Systems + Final Assessment
**Day:** 19 | **Session Type:** Theory
**Duration:** 90 minutes
**CO Alignment:** co-4

---

## Session Outcomes

| Code | Outcome | Bloom's Level |
|------|---------|---------------|
| so-9-1-1 | Identify transponder chip types (ID46, ID48, PCF7936, 4D, Toyota G/H) and select the correct cloning or programming method | Understand |
| so-9-2-1 | Explain immobilizer system architecture (ECU ↔ immobilizer ↔ transponder loop), anti-theft fault codes, and EEPROM PIN storage | Understand |

---

## Session Overview

**Format:** Instructor-led narrative with class discussion, live demonstration segments, and a mid-session reasoning check
**Room Setup:** Standard classroom or lab with projection; students seated; no equipment hands-on during theory
**Key Visuals Required:**
- Transponder system loop diagram (key → antenna coil → immobilizer → ECU)
- Chip type identification chart (all major transponder families with vehicle applications)
- EEPROM chip identification on immobilizer PCB (reference designator, package type, silkscreen)
- Cloning method decision flowchart
- Immobilizer architecture by vehicle type (standalone, BCM-integrated, ECU-integrated)
- Lost key recovery workflow diagram (step-by-step)
- Anti-theft DTC reference table

---

## Timing Overview

| Segment | Duration | Cumulative |
|---------|----------|------------|
| Hook and context-setting | 5 min | 0:05 |
| Transponder technology fundamentals | 10 min | 0:15 |
| Transponder chip types — complete taxonomy | 15 min | 0:30 |
| Cloning and programming methods — detailed walkthrough | 15 min | 0:45 |
| Mid-session reasoning check / break | 5 min | 0:50 |
| Immobilizer system architecture | 10 min | 1:00 |
| EEPROM, PIN storage, and security counters | 8 min | 1:08 |
| Anti-theft fault codes | 5 min | 1:13 |
| Lost key recovery — full workflow | 8 min | 1:21 |
| Legal and ethical considerations | 6 min | 1:27 |
| Climax, summary, and lab preview | 3 min | 1:30 |

---

## Story Arc

**HOOK** — A stolen car, no keys, a customer who needs help. What do you do?

**Rising action** — Understanding the technology makes the method clear. Chip type determines everything. Not all chips can be cloned directly. Some require EEPROM access. Some require dealer tools. The method follows from the diagnosis.

**Complication** — The knowledge that allows lost key recovery is the same knowledge that could enable vehicle theft. Professional responsibility is not a side note — it is load-bearing.

**Climax** — "This knowledge gives you the ability to recover a vehicle that is otherwise completely locked. And that is exactly why it carries professional responsibility. The skill and the ethics go together."

**Resolution** — Preview of afternoon lab. Students leave ready to perform three procedures: direct key clone, EEPROM-based lost key recovery, and replacement immobilizer matching.

---

## Content

---

### HOOK (5 minutes)

"A customer calls. Their car was stolen. The thief left it running when they abandoned it. The customer has the car back — the police have cleared it — but all the keys were taken. The customer has no working key.

They call you.

What do you do?"

Pause. Let the question sit.

"Before you can answer that correctly, you need to understand exactly how the transponder security system works — at the electronic level. Because the answer to 'what do you do' depends entirely on the chip type in the key, the architecture of the immobilizer, and what tools you have available.

By the end of this session, you will be able to answer it.

Lost key recovery is one of the highest-margin jobs in ECU repair. On a mid-range European vehicle it can return £200–£500 or more depending on complexity. It is also one of the most technically demanding. And it is one of the most ethically loaded. We start with the technology. We end with the responsibility."

---

### 1. Transponder Technology — How It Actually Works (10 minutes)

**What is a transponder key?**

A transponder key contains a passive RFID chip embedded in the plastic head of the key. Passive means no battery — no independent power source of any kind. The chip is powered entirely by electromagnetic induction from the vehicle's antenna coil.

**The ignition antenna coil:**

Wrapped around the ignition barrel — or the steering column housing, depending on the vehicle — is a copper coil. When the key is inserted, this coil creates an oscillating magnetic field at a specific frequency: typically 125 kHz for most transponder systems. This magnetic field induces a tiny current in the transponder chip's receiving coil, waking the chip.

**The authentication sequence — what happens in under 200 milliseconds:**

1. Key enters the ignition barrel. Antenna coil is energised by the immobilizer module.
2. The transponder chip powers up via inductive coupling. It receives a cryptographic challenge (or, for fixed-code chips, simply broadcasts its stored code).
3. The transponder transmits its response via RF back to the antenna coil.
4. The immobilizer module receives and reads the signal. It verifies the response against the stored paired codes in its EEPROM.
5. If the response is valid: the immobilizer sends an authorization signal to the engine ECU. This may be a direct discrete output, a CAN message, or a K-line message depending on the platform.
6. The engine ECU receives authorization and permits engine start — fuel injection and ignition are released.
7. If no transponder is detected, or the transponder fails authentication: no authorization is sent. The engine ECU blocks start regardless of the mechanical key position.

**Why this prevents theft:**

Even a perfectly cut mechanical copy of the key will turn the barrel — but without a paired transponder generating the correct cryptographic response, the immobilizer never authorizes the engine. The mechanical key alone is worthless.

**Key point:** The transponder chip is the security element, not the mechanical blade. Thieves who hot-wire old vehicles short the ignition switch. Modern immobilizers make this irrelevant — the engine will not start without the cryptographic handshake, regardless of what is done to the ignition circuit.

**The practical consequence for a flat fob battery:** Remote key fobs contain two separate elements — a 433 MHz radio transmitter (for remote locking/unlocking, which uses the battery) and a passive transponder (for immobilizer authentication, which uses inductive power). A flat fob battery disables remote locking. It does not disable the transponder. Holding the fob close to the ignition barrel couples the transponder inductively. Many customers do not know this — they arrive convinced the immobilizer has failed when the battery is flat.

---

### 2. Transponder Chip Types — Complete Taxonomy (15 minutes)

Understanding chip types is not optional. The chip type determines:
- Whether cloning is possible or requires EEPROM access
- Which blank transponder chip to select
- What programming tool and function to use
- How long the job will take and what it will cost
- Whether to refer to a specialist or dealer

**Refer to the Chip Type Identification Chart on the slide.**

---

#### 2.1 Fixed Code Chips — Cloneable Directly

**ID11 / ID12 / ID13**
- Generation: Very early 1990s vehicles
- Frequency: 125 kHz
- Security type: Fixed code — the chip always transmits the same code; no encryption, no rolling code
- Vehicles: Early Rover, early Ford, early Fiat, some early Japanese imports
- Clone method: Direct — programmer reads fixed code, copies it identically to a blank
- Security assessment: Effectively no longer secure. Anyone with an inexpensive cloner can copy these. Rarely seen in active workshop practice today.

**ID33 / T5 (Texas Instruments)**
- Generation: Mid-1990s to early 2000s
- Frequency: 125 kHz
- Security type: Fixed code (T5 is the Texas Instruments implementation; ID33 is the generic classification)
- Vehicles: Early Ford Fiesta/Mondeo/Focus (pre-2000), early VW Group, some Renault
- Clone method: Direct copy — any capable programmer handles this in under two minutes

---

#### 2.2 Philips/NXP Cryptographic Chips — Calculation Required

**ID46 / PCF7936 / PCF7941 / PCF7942 / PCF7945 / PCF7952**
- Generation: From approximately 2000 onward
- Frequency: 125 kHz
- Security type: Cryptographic rolling code — challenge-response protocol; each authentication session produces different RF data; cannot be cloned by recording a transmission
- Vehicles: Volkswagen/Audi/Seat/Skoda from approximately 2000; Renault Clio/Megane/Scenic; Peugeot/Citroën; some Nissan; some Hyundai/Kia; widespread across European and Asian platforms
- PCF7936: the baseline ID46; most common variant worldwide
- PCF7941/7942/7945/7952: higher-security variants with extended memory; VW Group later platforms
- Clone method: Cannot be directly cloned. Options: (a) key programmer with built-in calculation algorithm reads transponder and generates new key (VVDI2 Key Tool Max handles most standard ID46 in 3–8 minutes); or (b) EEPROM extraction from immobilizer — read EEPROM, identify and extract crypto seed, use seed to program blank transponder
- Locked variant note: some ID46 chips return a "locked" flag when the programmer attempts direct calculation. These require the EEPROM route. The tool will tell you.

**ID48**
- Generation: VW Group from 2001 onward; Porsche from certain year ranges
- Frequency: 125 kHz
- Security type: NXP Crypto 48 — higher encryption than ID46; longer key length; cannot be calculated directly without a token-based online service or EEPROM access
- Vehicles: VW Golf/Passat/Polo from 2001+; Audi A3/A4/A6 from 2001+; Skoda Octavia; Seat Leon; Porsche
- Clone method: Two options — (a) token-based calculation via online programmer service (VVDI2 with subscription; charged per calculation); or (b) EEPROM extraction from immobilizer/ECU — extract CS (crypto seed) from EEPROM, program new transponder using seed. EEPROM route is often preferred for all-keys-lost because no token is consumed.
- PIN/SKC note: VW Group vehicles also have a factory-assigned SKC (Security Key Code) stored in the immobilizer EEPROM. If the SKC is available (from service records or OBD PIN reader), it can be used with a compatible OBD tool to add keys without full EEPROM extraction on some ID48 platforms.

---

#### 2.3 Texas Instruments 4D Series

**4D60 / 4D61 / 4D62 / 4D63 / 4D65 / 4D67 / 4D68 / 4D70**
- Generation: Late 1990s to 2010s
- Frequency: 125 kHz
- Security type: Texas Instruments cryptographic protocol — distinct from Philips/NXP approach; rolling code with TI-proprietary algorithm
- Vehicles by variant:
  - Toyota/Lexus: 4D60, 4D67, 4D68 (depending on model year)
  - Subaru: 4D60, 4D62
  - Mazda: 4D60, 4D63
  - Mitsubishi: 4D61, 4D62
  - Nissan/Infiniti: certain models, 4D60 era
- Clone method — varies by chip:
  - 4D60/4D62: handled by most capable key programmers with calculation
  - 4D63 (Ford, Mazda): specialist calculation tools required — VVDI2 and similar with correct firmware
  - 4D67: Toyota mid-2000s; standard calculation difficulty, most tools support it
  - 4D68: more complex; some variants approach dealer-only territory
  - 4D70: newer Mitsubishi; check your tool's coverage matrix before quoting the job
- Rule: always verify your tool's vehicle coverage for the specific year/model before starting. Do not assume 4D67 procedures transfer to 4D70.

---

#### 2.4 Toyota Proprietary — G Chip and H Chip

**Toyota G Chip (approximately 2010 onward)**
- Generation: 2010+
- Security type: Toyota proprietary AES-based cryptographic; strong encryption; no public calculation algorithm
- Vehicles: Toyota Auris, Avensis, Yaris, RAV4, Prius, Hilux from approx 2010; Lexus equivalents
- Clone method: OBD-based programming via Toyota-specific programmer (Toyota Techstream with factory server access) or aftermarket tools with Toyota G chip support and current token balance (VVDI2 with Toyota kit, Autel IM608); charged per key generation via online server
- Practical position: Toyota G chip is one of the most common "specialist referral" situations in independent workshops. Many independents use a dedicated Toyota key specialist with the correct tools and authorization. Knowing when to refer is itself a professional competency.

**Toyota H Chip (approximately 2016 onward)**
- Generation: 2016+ on newer Toyota/Lexus
- Security type: Enhanced Toyota proprietary; highest encryption in the Toyota range
- Vehicles: Newer Hilux, Land Cruiser, Prius 4th generation, newer Camry, newer RAV4
- Clone method: Primarily dealer or specialist with authorized Toyota H chip tools; some aftermarket programmers have added H chip support in recent firmware updates — verify tool compatibility before committing to the job. Do not quote H chip work without first confirming current tool support.

---

#### 2.5 Texas Instruments Crypto — BMW and Mercedes

**TI Crypto / BMW EWS Series / Mercedes EIS**
- Generation: 2000s to present
- Security type: Proprietary high-security cryptographic; BMW uses EWS3/EWS4 immobilizer systems; Mercedes uses EIS (Electronic Ignition Switch) and ESL systems
- Vehicles: BMW (EWS3, EWS4 systems — most 3, 5, 7 series from late 1990s through mid-2010s); Mercedes-Benz (EIS-equipped models); some Hyundai/Kia higher-end models
- Clone method:
  - BMW EWS3: some aftermarket tool support for EEPROM-based key addition; accessible to capable independent workshops with the correct equipment
  - BMW EWS4: substantially more complex; typically requires specialist tools or BMW dealer network
  - Mercedes EIS: highly specialized; dedicated Mercedes key programming equipment required; largely dealer-territory for independent workshops
- Honest workshop position: for BMW EWS4 and Mercedes EIS, the professional answer is often "we refer this to a specialist with the correct tooling." Knowing this limit — and communicating it clearly to the customer — is itself a professional skill.

---

**Chip Type Summary Table:**

| Chip Family | Security Type | Direct Clone? | Method Required |
|-------------|--------------|---------------|-----------------|
| ID11/12/13, ID33/T5 | Fixed code | Yes | Direct copy |
| ID46 / PCF7936 | Crypto (NXP rolling) | No | Calculation / EEPROM |
| ID48 | Crypto 48 (NXP) | No | Token service / EEPROM |
| 4D60/62/63/67 | Crypto (TI) | No | Calculation / EEPROM |
| 4D68/70 | Crypto (TI advanced) | No | Specialist / EEPROM |
| Toyota G | AES proprietary | No | OBD token / dealer |
| Toyota H | AES proprietary enhanced | No | Dealer / specialist |
| BMW EWS3 | TI Crypto | No | EEPROM / specialist |
| BMW EWS4 / Merc EIS | Proprietary high-sec | No | Specialist / dealer |

---

### 3. Cloning and Programming Methods — Detailed Walkthrough (15 minutes)

Four primary methods. Which applies depends on the chip type and whether any working keys exist.

---

#### Method 1: Direct Clone (Fixed Code Chips Only)

**When it applies:** ID11, ID12, ID13, ID33, T5 — fixed code chips only

**Procedure:**
1. Place the original (working) key in the programmer read coil
2. Tool automatically identifies chip type and reads the fixed code
3. Select a blank transponder chip of the matching family
4. Tool writes the identical fixed code to the blank
5. Verify: read the clone back — codes must match

**Critical limitation:** Only valid for fixed code chips. Attempting to "clone" a cryptographic chip this way will produce a chip with data on it — but it will not authenticate correctly because cryptographic challenge-response cannot be replicated by copying stored bytes. A cloned ID46 produced this way will fail authentication on every attempt.

**Time:** 5–10 minutes. The fastest key programming method when applicable.

---

#### Method 2: Calculation-Based Programming (ID46, ID48, some 4D)

**When it applies:** Cryptographic transponders — any situation, but especially when no working key exists

**Why EEPROM access is required:** The cryptographic seed (CS) or PIN (also called SKC — Security Key Code — in VW Group terminology) is stored in the immobilizer module's EEPROM. This seed is what the immobilizer uses to generate and verify the cryptographic challenge-response. Without knowing this seed, it is mathematically impossible to generate a transponder that will authenticate correctly — there is no shortcut.

**Procedure:**
1. Identify the immobilizer module's location in the vehicle
2. Remove the immobilizer module
3. Locate the EEPROM chip on the module PCB — typically SOIC-8 package; common types: 93C46, 93C56, 93C66, 95080, 95160 (readable by reference designator and silkscreen marking)
4. Connect SOIC-8 clip programmer to the chip in-circuit
5. Read the EEPROM — read 3 times and compare: all three readings must be bit-for-bit identical before proceeding
6. Save the EEPROM dump with a descriptive filename including vehicle registration and date
7. Open the dump in key programmer software or a dedicated EEPROM decode tool — software identifies PIN/CS location within the file for known immobilizer types
8. Extract PIN/SKC — record on the procedure documentation card
9. Enter PIN/SKC into the key programmer; select vehicle make/model/year and immobilizer type
10. Programmer generates and writes a new transponder with the correct cryptographic identity
11. Return the immobilizer module to the vehicle; complete any OBD pairing steps if required by the platform
12. Test new key — engine must start; scan for DTCs

**Critical note:** Always retain a backup copy of the EEPROM dump. If a write-back operation is required (some platforms require updating the immobilizer EEPROM with the new key's codes), the backup allows recovery if the write fails.

**Time:** 45–90 minutes including module removal and reinstallation. Time varies significantly by vehicle access.

---

#### Method 3: OBD-Based Key Addition (Working Key Available)

**When it applies:** At least one working key exists; vehicle supports OBD key learning mode

**This is the preferred method when a working key exists.** It is faster, does not require removing any module, and does not risk EEPROM damage.

**Procedure:**
1. Sit in the vehicle with the working key in the ignition (often required to be in position 1 or 2)
2. Connect key programmer to OBD-II port
3. Launch key learning mode for the specific vehicle make/model
4. Follow tool prompts — may require: entering PIN/SKC if required, security access handshake, or confirming the existing key is present
5. Place new blank key (with correct transponder chip type pre-selected) when prompted
6. Tool programs the new transponder and registers it in the immobilizer's key slot memory
7. Test: remove original key; new key must start vehicle independently

**PIN requirement:** Some platforms — notably VW Group — require the PIN/SKC to be entered even for OBD key addition. If the PIN is known (from service history, V5 documentation, or OBD PIN reader), it can be entered directly. If not known, EEPROM extraction is still needed to obtain it before OBD addition can proceed.

**Time:** 15–30 minutes when PIN is immediately available.

---

#### Method 4: PIN/SKC-Based Programming — VW Group

**When it applies:** VW Group vehicles where the factory SKC is available

**Background:** VW Group vehicles have a factory-assigned SKC (Security Key Code). This is stored in the immobilizer EEPROM and in some cases can be retrieved from the vehicle via OBD or from dealer service records.

**Procedure:**
1. Obtain the SKC — from: dealer printout (requires registered keeper proof of identity), OBD SKC reader (some tools can read the SKC via OBD without EEPROM access, platform dependent), or EEPROM extraction
2. Connect VCDS or compatible VW Group OBD tool to OBD-II port
3. Navigate to Immobilizer module
4. Enter SKC when prompted
5. Use key adaptation/coding function to register new transponder
6. On some platforms: new transponder must be in the ignition during the coding procedure
7. Verify new key starts vehicle independently

**SKC availability:** Not all VW Group vehicles allow OBD SKC reading — some require EEPROM extraction regardless. Always verify before quoting the customer a turnaround time.

---

### MID-SESSION REASONING CHECK / BREAK (5 minutes)

Pause at the 45-minute mark.

Display the chip type chart on screen.

Ask the class: "A customer brings in a 2004 VW Golf. All keys lost. No working key. What chip type are we likely dealing with, and which method do we need to use?"

Expected answer: ID48 (Crypto 48) — the Golf from 2001+ uses ID48; all-keys-lost means no working key to read from; method is EEPROM extraction from the immobilizer to obtain the CS; then calculation-based programming of a new transponder; or token-based OBD method if the tool supports it.

Confirm the answer. Address any confusion. Take questions. Then continue.

---

### 4. Immobilizer System Architecture (10 minutes)

Before knowing how to access the EEPROM, students must know where the immobilizer lives. This varies significantly by vehicle type and generation.

**The Three-Component Security Loop:**

All vehicle immobilizer systems share the same fundamental architecture, regardless of manufacturer:

```
[Transponder in Key]
        ↕  (RF at 125 kHz via antenna coil)
[Immobilizer Module]
        ↕  (Authorization signal: discrete output, CAN, or K-line)
[Engine ECU]
```

No single component works alone. Remove or disable any one link and the loop breaks. This is the fundamental security principle.

---

**Component 1: Transponder (in key)**

The passive RFID chip. No battery. Powered by the antenna field. Stores the cryptographic identity. Covered in detail in Sections 1 and 2.

**Diagnostic note:** A transponder that is physically intact but has a damaged chip — from heat, impact, or ESD — will appear entirely absent to the antenna. The immobilizer logs a "transponder not detected" or "no response from key" DTC. A wrong transponder (wrong code, wrong chip type) will respond but fail authentication — producing a different fault code. This distinction is useful for diagnosis.

---

**Component 2: Immobilizer Module**

Contains:
- RF receive/transmit circuit driving the antenna coil
- Authentication logic (verifies transponder response against stored codes)
- EEPROM (stores paired codes, PIN/SKC, security counters)
- Communication interface to the engine ECU (discrete output, CAN, or K-line)

**Immobilizer location — varies significantly:**

| Location Type | Description | Typical Vehicles |
|---------------|-------------|-----------------|
| Standalone module | Separate ECU near ignition barrel or under dash | Early VW Group, Renault Megane I/II, Peugeot 307 |
| Integrated in BCM | BCM contains immobilizer function | Many post-2005 Ford, Vauxhall/Opel |
| Integrated in engine ECU | No separate immobilizer — ECU contains all logic | Most modern (2010+) vehicles |
| In instrument cluster | Cluster serves as immobilizer hub | Some Renault, some Vauxhall |
| In steering column lock (EIS) | Electronic ignition switch — Mercedes | Mercedes-Benz |

**Practical implication:** Identifying the immobilizer location before quoting EEPROM access work is essential. If the immobilizer is integrated into the engine ECU, reading the EEPROM means opening the ECU — a more complex procedure with greater risk than accessing a standalone module.

---

**Component 3: Engine ECU**

The engine ECU does not independently authenticate the transponder. It receives the authorization signal from the immobilizer and acts on it. If no valid authorization is received — or the authorization message from the immobilizer is absent or incorrect — the engine ECU suppresses fuel injection and/or ignition. The starter motor can still crank, but the engine will not run.

**The "crank and stall" diagnostic indicator:** When an immobilizer authentication fails, the engine typically cranks normally — sometimes there is a brief RPM spike as a minimal fuel pulse fires — then immediately cuts out. This "crank-and-stall" or "crank-and-cut" pattern, with no injector or ignition fault codes, is a strong indicator of immobilizer authentication failure. Go directly to the immobilizer system.

**On integrated systems (immobilizer inside ECU):** The ECU performs both authentication and engine management internally. The antenna coil connects directly to the ECU's own RF circuit. Replacing the ECU means the new ECU's security association codes will not match the vehicle's transponder codes — a no-start condition. EEPROM data migration or a new matching procedure is required.

---

### 5. EEPROM, PIN Storage, and Security Counters (8 minutes)

**EEPROM contents in the immobilizer module:**

The EEPROM is the single most important data location in the entire security system. It contains:

**Paired transponder codes:** The cryptographic data for each registered key, stored in numbered key slots. Most immobilizers support 4–10 slots simultaneously. The vehicle specification's "maximum 4 keys" limit is the number of EEPROM key slots.

**Vehicle PIN / SKC:** The factory-assigned or dealer-set Security Key Code. This is the authorization code required to enter key-learning mode — either via OBD diagnostic interface or via calculation-based programming. Stored in encoded or encrypted form; decode is handled by the key programmer software for known module types.

**Security counters:** Some immobilizers count the number of times the EEPROM has been accessed or keys have been programmed. Exceeding the limit may lock the module permanently. This is rare but must be considered on modules that show evidence of prior programming attempts.

**Mileage mirror (VW Group and some others):** VW Group vehicles store a copy of the odometer reading in the immobilizer EEPROM as an anti-fraud measure. If you write an EEPROM image from a donor vehicle with different mileage data, a mileage mismatch fault will appear. The mileage bytes must be updated to match the current vehicle before writing back.

**VIN data (some platforms):** Some immobilizers store a VIN or partial VIN for cross-reference verification with the engine ECU and cluster.

**Critical operational note — all-keys-lost procedure and slot clearing:**
Many platforms perform a complete key slot reset when entering all-keys-lost mode. All existing slots are cleared. All new keys must be registered in the same session. This must be communicated clearly to the customer before starting: "If you have any spare key at home that you have not mentioned, bring it now — after this procedure it will not work and will need to be re-programmed."

---

### 6. Anti-Theft Fault Codes (5 minutes)

When the immobilizer system has a fault, specific DTCs are stored — in the engine ECU, the immobilizer module itself, or both.

**Engine ECU DTCs (when immobilizer authorization not received):**
- P0513: Incorrect immobilizer key (SAE generic)
- P0633: Immobilizer key not programmed (generic OBD-II)
- P1260: Anti-theft system active — engine fuel shut off (Ford PATS specific)
- P1570: Immobilizer active (common on Bosch ECU platforms)
- Manufacturer-specific codes: vary widely; many use the B or U range

**Immobilizer module DTCs (when transponder not recognized):**
- B1600: Transponder not detected (Renault, some Ford)
- B1601: Incorrect transponder code (VW Group)
- B1602: Transponder configuration fault
- B1681: Transponder signal not received (Ford)
- B2799: Immobilizer system malfunction (Toyota)

**Network DTCs (when immobilizer module stopped communicating):**
- U0141: Lost communication with body control module (if BCM contains immobilizer)
- U-range codes for loss of communication with any module containing immobilizer function
- Bus-off errors if the immobilizer module has a failed CAN transceiver

**Diagnostic approach using DTC type:**
- B-code in immobilizer module: transponder not paired or transponder is damaged — check transponder and key
- P-code in engine ECU only (no B-code in immobilizer): immobilizer communicated but the ECU rejected authorization — may indicate ECU/immobilizer mismatch; commonly seen after ECU replacement without immobilizer matching
- U-code: network issue — trace communication circuit before attempting key programming

---

### 7. Lost Key Recovery — The Complete Workflow (8 minutes)

**Refer to Lost Key Recovery Workflow Diagram on slide.**

**Step 1: Initial assessment — is any key available?**
Always ask the customer: are ALL keys genuinely lost, or is one perhaps at home, in a coat pocket, or with a family member?

If even one working key exists: OBD key addition (Method 3) is available — dramatically simpler, much faster, lower risk. Confirm this before committing to EEPROM-based recovery.

**Step 2: Confirm vehicle eligibility and chip type**
- Identify make, model, year precisely
- Use chip type chart to identify the expected transponder chip family
- Check tool's coverage database: does your tool support this chip/vehicle combination?
- If the chip type or vehicle is outside your tool's coverage — refer to a specialist. Do not attempt and create a worse situation.

**Step 3: Identify immobilizer location**
- Standalone, BCM-integrated, ECU-integrated, cluster, or steering column module
- Plan access: module removal required? ECU opening required? Steering column disassembly?

**Step 4: Access and read the immobilizer EEPROM**
- Remove the module from the vehicle
- Locate the EEPROM chip on the PCB (reference designator, package type — typically SOIC-8 93Cxx or 95xxx series)
- Connect SOIC-8 clip programmer to the chip in-circuit
- Read EEPROM — perform three reads and compare; all three must be identical before proceeding
- Save dump with descriptive filename (vehicle reg, date, module type)

**Step 5: Extract PIN/SKC from the EEPROM dump**
- Open dump in key programmer software or EEPROM decode tool
- Software identifies the PIN/CS location within the file for known module types
- Extract and record PIN/SKC on the job documentation card
- For unusual or uncommon module types: consult key programming community resources — most established platforms are documented

**Step 6: Generate and program the new transponder**
- Enter PIN/SKC into key programmer; select vehicle make/model/immobilizer type
- Select blank transponder chip of the correct type for this vehicle
- Programmer generates and writes the new transponder with the correct cryptographic identity

**Step 7: Complete the key pairing**
- Depending on the platform: may require writing the new key's code back into the immobilizer EEPROM, or completing an OBD pairing sequence, or the programmer handles this internally via its own protocol
- Follow the tool-specific procedure for the platform exactly

**Step 8: Test and verify**
- Install new key in the vehicle
- Attempt engine start — must start without immobilizer warning light illuminated
- Scan for DTCs — no anti-theft codes should remain active
- Security step: remove old lost key codes from the immobilizer's memory where the tool supports this — prevents a recovered old key from being used to start the vehicle

**Step 9: Document the job and advise the customer**
- Record: procedure performed, tool used, transponders programmed, verification result
- Advise: if this was a theft situation, a full security review is worth considering (mechanical locks, GPS tracker, aftermarket immobilizer)
- Return the vehicle only to the registered keeper — verify identity against documentation before handing over

---

### 8. Legal and Ethical Considerations (6 minutes)

**This section must be delivered with full seriousness. It is not optional content and not a compliance formality.**

**The core professional tension:**

The tools and skills covered in this session give you the capability to program a key for almost any vehicle you encounter. This is precisely what makes this work valuable to customers in genuine need. It is also precisely what makes these tools a target for misuse.

**Regulatory position:**

- Key programming is a regulated or monitored activity in many jurisdictions
- United Kingdom: no dedicated licence is required, but industry bodies including the Master Locksmiths Association (MLA) and Vehicle Security Installation Board (VSIB) define best-practice standards that include ownership verification before any lost key work
- European Union: varies by member state; some require trade registrations for automotive security work
- United States: varies significantly by state; some states regulate automotive locksmiths
- The tools themselves (VVDI, Autel IM608, etc.) are legal to own and use for legitimate automotive repair; using them to access a vehicle without the owner's authorization is a criminal offence under vehicle crime, computer misuse, or theft legislation in virtually all jurisdictions

**Professional obligations — non-negotiable:**

Before performing any lost key recovery:
1. Verify that the customer is the registered keeper — request V5 logbook (UK), title document, or jurisdiction-equivalent
2. Document the verification — photograph the document; record the request and your verification checks on the job card
3. Only perform work on vehicles confirmed as belonging to the requesting customer
4. If ownership cannot be verified: decline the work. This is professional responsibility, not rudeness.

**What you must not do:**

- Use these tools on any vehicle you have not been authorized to work on
- Perform key programming for a third party without verifying their legal relationship to the vehicle
- Use key programming capability to assist anyone who you have reason to believe does not own the vehicle
- Advertise these services in a way that attracts illegitimate requests without adequate verification processes built into your intake procedure

**The clarity here is not grey:**

There are online channels where key programming is advertised without ownership verification procedures. Some of this activity enables vehicle theft. As a qualified ECU hardware repair technician, your professional standard is distinct. Your ethical obligation is clear whether or not the law in your jurisdiction explicitly mandates it.

**Ethical use declaration:**

In this afternoon's hands-on session, before any key programming equipment is placed in front of you, you will sign the ethical use declaration. This is a formal acknowledgement that you understand what these tools are capable of and that you accept the professional responsibility that comes with using them.

This is not box-ticking. It is the professional starting point for every key programming job you will perform in your career.

---

### CLIMAX and Summary (3 minutes)

"Let us bring this together.

The lost key recovery job you could not answer at the start of this session — now you can answer it.

You know the chip type likely present in the vehicle. You know whether that chip can be directly cloned or requires EEPROM extraction. You know where the immobilizer lives in different vehicle architectures and what you need to extract from it. You know the complete workflow from initial assessment to verified test drive.

This knowledge gives you the ability to recover a vehicle that is otherwise completely locked — to help a customer with no other options.

And that is exactly why it carries professional responsibility.

The skill and the ethics go together. You do not get one without accepting the other.

This afternoon in the lab, you will perform a direct key clone, execute an EEPROM-based lost key recovery, and attempt a replacement immobilizer matching procedure. Before any equipment is in your hands, you will sign the ethical use declaration.

Get some lunch. Come back ready to work."

---

## Slide Outline (~26 Slides)

1. Title: SESSION-19T — Key Cloning, Lost Key Recovery & Immobilizer Programming
2. Session outcomes (so-9-1-1, so-9-2-1)
3. HOOK — The stolen car scenario
4. What is a transponder key? (diagram: key cross-section with chip labelled)
5. The ignition antenna coil (photograph + field diagram)
6. The authentication sequence — 7 steps, animated build
7. Why this prevents theft + the flat battery myth
8. Transponder chip types — introduction: chip type determines everything
9. Fixed code chips: ID11/12/13 and ID33/T5
10. Philips/NXP rolling code: ID46 / PCF7936 family
11. ID48 — Crypto 48, VW Group deep dive
12. Texas Instruments 4D series — variant table
13. Toyota G and H chips — honest capability statement
14. BMW/Mercedes TI Crypto — where to refer
15. Chip type summary table (all families, direct clone yes/no, method)
16. Method 1: Direct clone — when and how
17. Method 2: Calculation/EEPROM — when and how
18. Method 3: OBD key addition — when and how
19. Method 4: PIN/SKC-based (VW Group)
20. MID-SESSION SLIDE — reasoning check question
21. Immobilizer architecture: the three-component loop (key diagram)
22. Immobilizer location by vehicle type — table with examples
23. EEPROM contents — memory map concept diagram
24. Security counters, mileage mirror, and the all-keys-lost slot reset warning
25. Anti-theft fault codes — DTC table by system
26. Lost key recovery — complete workflow (numbered steps, flowchart)
27. Legal and ethical considerations — serious, undecorated slide
28. Ethical use declaration — preview of what students will sign
29. Climax and summary — "the skill and the ethics go together"
30. Lab preview — three activities, estimated timing, what to expect

---

## Instructor Notes

**Legal section delivery:**
Section 8 (Legal and Ethical Considerations) must be delivered with the same technical seriousness as the chip type content — not as a compliance afterthought. Make eye contact. Speak deliberately. If any student makes a dismissive comment or jokes during this section, stop and address it directly. This section has real professional consequences.

Consider opening Section 8 with a brief factual account of a real case where key programming tools were used in vehicle theft — without naming individuals. The factual reality is more effective than abstract statements about professional responsibility.

**Ethical use declaration forms:**
The forms must be prepared before the session begins. They are signed at the start of Session 19H, not during theory. Introduce and explain what students are signing here — so there are no questions about it during the lab. The signing should take less than two minutes at the start of 19H if students have already understood the content here.

**Chip type reference chart:**
Keep a physical printed chip type reference chart visible at the front of the room. Students will photograph it on their phones. This is expected and appropriate — it is exactly the kind of reference they will use in practice.

**Live demonstration opportunity:**
If a key programmer (VVDI2, Autel IM608, or equivalent) is available in the room, demonstrate live transponder identification during slide 8. Place a working key on the programmer coil and show the chip identification result on screen. This takes under 60 seconds and grounds the theory immediately in observable reality.

**Q&A management:**
This topic generates high student engagement and many vehicle-specific questions ("What about a Defender?", "Can you do a 2018 Hilux?"). Set the expectation early: vehicle-specific questions during content delivery will be answered with "check the tool coverage matrix — we'll look at that in the lab." Bank questions for the mid-session break and the lab preview. Do not allow Q&A to compress the later sections.

**Time management:**
The 5-minute mid-session break at the 45-minute mark is deliberate. This is dense content and cognitive load is high by that point. Do not skip it. If content is running behind: compress the individual chip type descriptions for less common families (BMW/Mercedes can be covered in one minute each); protect the immobilizer architecture section and the legal section in full.

**After the session:**
Set up the ethical use declaration forms on the bench before students return from lunch. The 19H session starts with the signing — have them ready.

---

## Assessment Alignment

| Session Outcome | Assessed In | Evidence |
|----------------|-------------|---------|
| so-9-1-1 | Session 19H Checkpoint 1; Final Assessment | Student correctly identifies chip type and selects method before cloning; clone executed correctly |
| so-9-2-1 | Session 19H Checkpoint 2; Final Assessment debrief | Student correctly extracts PIN from EEPROM; immobilizer architecture correctly described during debrief |

---

## Pre-Session Checklist

- [ ] Chip type identification chart printed and displayed at front of room
- [ ] Ethical use declaration forms printed (one per student) — for use in 19H, not this session
- [ ] Slide deck loaded and all visuals confirmed on projector
- [ ] Transponder system loop diagram clearly readable at back-of-room distance
- [ ] EEPROM chip identification images prepared (close-up PCB photos showing reference designators)
- [ ] Anti-theft DTC reference table visible on slide 25
- [ ] Key programmer powered and available for live demonstration during slide 8 (if available)
- [ ] Mid-session break planned — timer or clock visible from instructor position
- [ ] Lab schedule confirmed: 19H starts at what time; ethical declaration forms at the bench

---

*Module 9 | Day 19 Theory | ECUHR | v1.0 | 2026-02-18*
