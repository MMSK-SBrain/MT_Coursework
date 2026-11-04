# ECU Hardware Repair — Course Structure v2.0

**Version:** 2.0 (Confirmed)
**Date:** 2026-02-18
**Changes from v1.0:**
- Duration confirmed: 20 days
- New Module 1 added: ECU in the Real World (Dev Board vs Automotive Grade)
- Filtering circuits & EMI integrated via Option C (Day 1 intro + Module 3 depth)
- All HIGH priority gaps incorporated: ESD, Power Stage Analysis, Bootloader/JTAG
- All MEDIUM priority gaps incorporated: Environmental failures, Thermal Management, LIN bus, ADAS awareness
- Modules renumbered 1–9

---

## Course Overview

| Field | Value |
|-------|-------|
| **Course Title** | ECU Hardware Repair |
| **Course Code** | ECUHR |
| **Target Audience** | Automotive technicians with ECU diagnostics background |
| **Prerequisites** | ECU Fundamentals + Automotive Diagnostics |
| **Duration** | 20 days |
| **Theory / Practice** | 30% Theory / 70% Practical |
| **Total Modules** | 9 |

---

## Course Outcomes (COs)

| ID | Code | Description | Category | Bloom |
|----|------|-------------|----------|-------|
| co-1 | ECUHR-CO-1 | Diagnose ECU faults at component level by applying knowledge of automotive-grade circuit design, protection, and signal conditioning | Skill | Analyze |
| co-2 | ECUHR-CO-2 | Repair ECU PCBs by identifying and replacing faulty electronic components using correct soldering, rework, and safety techniques | Skill | Apply |
| co-3 | ECUHR-CO-3 | Program, code, and update ECUs and control modules using appropriate tools including OBD, bench mode, and bootloader methods | Skill | Apply |
| co-4 | ECUHR-CO-4 | Configure and recover vehicle security and safety systems including key programming, immobilizer setup, and airbag module coding | Skill | Apply |

---

## Module Map — 20 Days at a Glance

```
Day  1      → Module 1: ECU in the Real World (Dev Board vs Automotive Grade)
Days 2–3    → Module 2: Tools & Measurement Mastery
Days 4–6    → Module 3: ECU Architecture, Protection & Filtering
Days 7–9    → Module 4: PCB Repair & Soldering Skills
Days 10–12  → Module 5: ECU On-Table Diagnostics
Days 13–14  → Module 6: ECU Programming & Bootloader
Days 15–16  → Module 7: CAN Bus, LIN & Communication Diagnostics
Days 17–18  → Module 8: Module-Specific Repair
Days 19–20  → Module 9: Security & Safety Systems + Final Assessment
```

---

## Module 1: ECU in the Real World
### *Why is an ECU so much more complex than a development board?*

**Duration:** 1 day (Day 1)
**Type:** Lecture + Demonstration + Discussion
**CO Alignment:** co-1 (foundational understanding)

**Purpose:**
This module creates the "aha moment" that grounds every topic that follows. Students who've used Arduino, STM32, or Raspberry Pi boards will immediately understand why an ECU PCB is covered in components that appear on no dev board. This context makes Module 3's deep dive meaningful, not abstract.

**Teaching Approach — The Comparison:**

| Aspect | Development Board (Arduino/STM32) | Automotive ECU |
|--------|-----------------------------------|----------------|
| Supply voltage | Clean 5V USB / 3.3V regulated | 9–16V battery (varies), 40V+ load dump spikes |
| Operating temperature | 0°C to 70°C (room, table) | −40°C to +125°C (engine bay) |
| EMI environment | None to speak of | Alternator, ignition coils, motors, RF transmitters |
| Vibration | None | Constant mechanical vibration |
| Moisture/Chemicals | Dry lab | Engine bay: water, oil, salt, cleaning agents |
| Short circuit risk | USB fuse saves you | 12V battery can source hundreds of amps |
| Reverse polarity | Kills the board | ECU must survive and protect itself |
| Signal line ESD | Low risk | Up to 2kV on connector pins |
| Multiple ground domains | Single ground | Chassis ground, sensor ground, signal ground |
| Watchdog | Optional | Mandatory — ECU must recover from software hang |

**Why this drives ECU circuit complexity:**
- Battery input needs a filter (bulk cap + ferrite) just to clean up noise
- Every IC power pin needs a decoupling cap or the processor crashes
- Every signal pin entering the ECU from the outside world needs ESD protection
- Every output driving a solenoid or motor needs a flyback diode or it destroys the driver
- Temperature extremes mean capacitor values drift — larger margins are needed
- The PCB ground plane matters because high currents flow through chassis ground

**Lessons:**

| # | Lesson | Content | Type |
|---|--------|---------|------|
| 1.1 | Dev Board vs ECU — The Comparison | Side-by-side comparison; the 10 differences above; live demonstration | lecture |
| 1.2 | The Automotive Electrical Environment | Battery voltage range, load dump, EMI sources, temperature extremes | lecture |
| 1.3 | ESD Safety & ECU Handling *(HIGH gap)* | ESD damage mechanisms, anti-static mat, wrist strap, bag storage, handling rules | lecture + practical |
| 1.4 | Introduction to the ECU PCB (Physical Tour) | Students open a real ECU; identify regions: power section, processor, drivers, connectors | lab |

**Module 1 Outcomes (MOs):**
- MO 1-1: Explain why automotive ECUs require protection and filtering circuits that development boards do not
- MO 1-2: Describe the automotive electrical environment and its effect on ECU electronic design
- MO 1-3: Apply correct ESD safety procedures when handling ECUs and PCB components

---

## Module 2: Tools & Measurement Mastery
### *Build precision diagnostic skills before touching a live ECU*

**Duration:** 2 days (Days 2–3)
**Type:** Lecture + Lab (heavy practical)
**CO Alignment:** co-1, co-2

**Purpose:**
Students may have used multimeters and oscilloscopes before, but ECU repair requires a different level of precision. A 0.1V voltage drop matters here. A 50ms signal glitch is a fault. This module upgrades their measurement skill from "automotive mechanic" to "ECU technician" level.

**Lessons:**

| # | Lesson | Day | Content | Type |
|---|--------|-----|---------|------|
| 2.1 | Multimeter Mastery for ECU Work | 2 | Resistance measurement (component-level); diode test; voltage drop; continuity on PCB traces; measuring reference voltages | lecture + lab |
| 2.2 | Oscilloscope Mastery — Setup & Signal Capture | 2 | Probing technique, timebase, triggering, channel coupling (AC/DC), ground reference; capturing ECU signals | lecture + lab |
| 2.3 | Oscilloscope — Waveform Analysis | 3 | PWM waveforms, CAN bus signals, injector drive signals, sensor outputs; identifying anomalies | lab |
| 2.4 | Reading ECU Wiring Diagrams | 3 | Connector diagrams, pin functions, signal names, power/ground references, tracing signal paths | lecture + lab |
| 2.5 | Sensor & Actuator Testing Workflows | 3 | Testing TPS, MAP, MAF, coolant temp, crankshaft sensor; actuator resistance checks; expected waveforms | lab |

**Module 2 Outcomes (MOs):**
- MO 2-1: Use a multimeter at component level for resistance, diode, voltage-drop, and continuity measurements on ECU PCBs
- MO 2-2: Operate an oscilloscope to capture and interpret ECU signal waveforms
- MO 2-3: Read ECU wiring diagrams to trace signals from connector pins to circuit components
- MO 2-4: Test automotive sensors and actuators using correct measurement techniques

---

## Module 3: ECU Architecture, Protection & Filtering
### *What every component on the board is doing — and why it must be there*

**Duration:** 3 days (Days 4–6)
**Type:** Lecture + Lab
**CO Alignment:** co-1, co-2

**Purpose:**
This is the technical foundation for all repair work that follows. Students learn to read the ECU PCB not as a mystery but as a logical, understandable system. The Day 1 comparison from Module 1 is now resolved here in full technical detail — every "extra" component that a dev board doesn't have is explained, tested, and diagnosed.

**Day 4 — PCB Architecture & Digital Core**

| # | Lesson | Content | Type |
|---|--------|---------|------|
| 3.1 | PCB Layout Deep Dive | Layer structure (2/4/6 layer boards); signal layers vs power planes; ground planes; test points; via types; reading silkscreen and reference designators | lecture + lab |
| 3.2 | Microcontroller, Processor & Memory | MCU architecture; Harvard vs Von Neumann; EEPROM (calibration storage); FLASH (firmware/program memory); RAM; clock circuits; reset circuits | lecture + lab |
| 3.3 | Watchdog Circuits & Reset ICs | Why automotive ECUs need external watchdog; window watchdog operation; common watchdog ICs; diagnosing watchdog faults | lecture + lab |

**Day 5 — Power Supply, Protection & Filtering** *(Option C — full depth)*

| # | Lesson | Content | Type |
|---|--------|---------|------|
| 3.4 | ECU Power Supply Architecture | Battery → ECU voltage path; linear regulators (LDO); switch-mode regulators; 5V reference generation; multiple voltage rails | lecture + lab |
| 3.5 | Protection Circuits: Reverse Polarity, Overvoltage, Load Dump | Reverse polarity diode / MOSFET circuits; TVS diodes; Zener clamps; transient suppression; load dump pulse (ISO 7637); why 40V spikes happen | lecture + lab |
| 3.6 | Filtering Circuits — The Complete Picture | **Bulk capacitors** (energy reservoir, ride-through during cranking); **Decoupling/bypass capacitors** (per-IC noise suppression at power pins); **RC filters** (sensor input anti-aliasing); **LC filters** (switching supply output ripple reduction); **Ferrite beads** (high-frequency noise blocking on power rails); **Common-mode chokes** (CAN/LIN bus EMI); capacitor value selection and placement rules | lecture + lab |
| 3.7 | EMI/EMC Components & Design Principles | What is EMI and why vehicles generate so much; differential-mode vs common-mode noise; ferrite bead selection; π-filters; TVS diode arrays on signal lines; PCB layout rules for EMC (ground planes, trace routing, component placement near connectors) | lecture |

**Day 6 — Signal Conditioning, Drivers & Thermal Design**

| # | Lesson | Content | Type |
|---|--------|---------|------|
| 3.8 | Signal Conditioning Circuits | Pull-up / pull-down resistors on inputs; sensor interface circuits; analog input protection (series resistor + clamp diode); digital input Schmitt triggers; isolation requirements | lecture + lab |
| 3.9 | Injector Drivers & Output Power Stages | Low-side vs high-side drivers; peak-and-hold vs saturation drive; H-bridge basics; PWM control; flyback / freewheeling diodes on inductive loads; MOSFET vs IGBT selection | lecture + lab |
| 3.10 | Power Stage Failure Analysis *(HIGH gap)* | Common failure modes: overvoltage from missing flyback diode; overcurrent from shorted load; thermal runaway; surge from alternator disconnect; identifying burnt drivers; testing driver outputs with scope | lecture + lab |
| 3.11 | Thermal Management *(MEDIUM gap)* | Junction temperature vs ambient; heatsinking on power ICs; thermal paste and pads on ECU PCBs; using thermal camera to find hot components; derating — why components fail in summer but not winter | lecture + lab |

**Module 3 Outcomes (MOs):**
- MO 3-1: Identify and explain the function of all major circuit regions on an ECU PCB
- MO 3-2: Explain the role of protection circuits (reverse polarity, TVS, load dump) in automotive ECU design
- MO 3-3: Identify and explain each filtering component type (bulk cap, bypass cap, ferrite bead, common-mode choke) and its placement on a real ECU PCB
- MO 3-4: Explain EMI sources in the vehicle environment and identify EMC mitigation components on the PCB
- MO 3-5: Analyze output power stage circuits and identify common failure modes from overcurrent, overvoltage, and thermal overload
- MO 3-6: Use a thermal camera and component derating knowledge to identify heat-related failure candidates

---

## Module 4: PCB Repair & Soldering Skills
### *The craft at the core — hands-on intensive*

**Duration:** 3 days (Days 7–9)
**Type:** Lab + Practical (very high hands-on ratio)
**CO Alignment:** co-2

**Purpose:**
Soldering is a perishable skill. Students need supervised repetition until the technique is consistent. Poor soldering creates more faults than it fixes and can permanently damage an ECU. Each lesson builds on the previous — simple components before complex packages.

**Lessons:**

| # | Lesson | Day | Content | Type |
|---|--------|-----|---------|------|
| 4.1 | SMD Soldering — Iron Technique | 7 | Tip selection; flux types and application; drag soldering; soldering 0402, 0603, 0805, SOIC-8 packages; inspection under magnification | lab |
| 4.2 | SMD Desoldering — Wick & Braid | 7 | Desoldering wick; solder sucker; cleaning pads; removing 0402 and SOIC components without pad damage | lab |
| 4.3 | Hot Air Soldering & Desoldering | 8 | Hot air station setup (temperature, airflow); removing SOIC, QFP, and TQFP ICs; reflowing connector pads; no-lift technique | lab |
| 4.4 | IC Removal & Replacement — QFP, SOIC | 8 | Alignment using stencil/paste; pin-by-pin inspection; using flux; verifying solder joints; rework without damage | lab |
| 4.5 | BGA Introduction — Reballing Theory + Demo | 8 | What is BGA; why it's used; reballing concept; professional equipment requirements; when to replace vs. reball | lecture + demo |
| 4.6 | IC Testing & Datasheet Reading | 9 | Identifying ICs from markings; finding datasheets; reading pinout; in-circuit vs out-of-circuit testing; identifying dead ICs | lecture + lab |
| 4.7 | CAN Box Construction — Build Your Own | 9 | Schematic review; kit assembly; soldering connectors, resistors, transceiver IC; functional test; understanding what you built | practical |

**Module 4 Outcomes (MOs):**
- MO 4-1: Perform SMD soldering and desoldering on ECU-grade PCBs without lifting pads or damaging adjacent components
- MO 4-2: Remove and replace ICs in SOIC, QFP, and TQFP packages using iron and hot air techniques
- MO 4-3: Identify ICs from package markings, locate datasheets, and test functionality in-circuit
- MO 4-4: Construct a functional CAN box from components and explain its circuit operation

---

## Module 5: ECU On-Table Diagnostics
### *The diagnostic workflow — from power-on to fault confirmed*

**Duration:** 3 days (Days 10–12)
**Type:** Lab + Practical
**CO Alignment:** co-1

**Purpose:**
On-table ECU diagnosis is the core service workflow. The diagnostic sequence — bench power → scan → line trace → component test → fault confirm — must become systematic and repeatable. This module also covers real-world failure modes caused by environment (moisture, corrosion) which are common but rarely taught.

**Lessons:**

| # | Lesson | Day | Content | Type |
|---|--------|-----|---------|------|
| 5.1 | Bench Test Setup — Power, Ground, Communication | 10 | Wiring a bench harness; providing stable 12V; supplying ignition signal; connecting to CAN; bench power supply limits | lecture + lab |
| 5.2 | ECU Scanning & Fault Code Interpretation | 10 | Multiple scan tools; reading DTCs; freeze-frame data; live data streams; understanding which faults are hardware vs software | lab |
| 5.3 | ECU Line Tracking | 11 | Signal flow from connector pin → track → component; using multimeter and scope on live ECU; identifying open circuits, short circuits, signal degradation | lab |
| 5.4 | Component Testing on Live ECU | 11 | In-circuit resistance checks; testing ICs under power; comparing measurements to reference values; capacitor ESR testing | lab |
| 5.5 | Environmental Damage Assessment *(MEDIUM gap)* | 12 | Moisture ingress — where water enters ECUs; corrosion on PCB traces and connector pins; cleaning procedures (ultrasonic, manual); conformal coating inspection; diagnosing water-damaged boards | lecture + lab |
| 5.6 | Fault Finding Case Studies | 12 | 3–4 real ECUs with planted faults (one per failure type: component, power stage, trace, moisture); students diagnose independently | practical |

**Module 5 Outcomes (MOs):**
- MO 5-1: Configure a safe bench test setup for a removed ECU and establish communication
- MO 5-2: Scan, read, and interpret fault codes and live data from a bench-mounted ECU
- MO 5-3: Trace signal paths through an ECU using wiring diagrams and in-circuit measurement
- MO 5-4: Assess and clean moisture and corrosion damage on ECU PCBs

---

## Module 6: ECU Programming & Bootloader
### *Reading, writing, and recovering ECU firmware — including low-level boot access*

**Duration:** 2 days (Days 13–14)
**Type:** Lecture + Lab + Practical
**CO Alignment:** co-3

**Purpose:**
Many ECU repairs require reflashing firmware. This module covers the full range of programming methods — from simple OBD-port flash through to boot mode access via JTAG and BDM pins, which is needed when OBD communication is not possible (bricked ECU, failed MCU communication, cloning).

**Lessons:**

| # | Lesson | Day | Content | Type |
|---|--------|-----|---------|------|
| 6.1 | ECU Programming Fundamentals | 13 | OBD vs bench mode vs boot mode; read-backup-write-verify workflow; why backups are mandatory; file formats (.bin, .hex, .mot) | lecture |
| 6.2 | Programming Tools Overview | 13 | KTM Bench, Kess V2, Ktag, VVDI, Xhorse tools; tool selection by ECU type; supported ECUs; license/credit systems | lecture + lab |
| 6.3 | ECU Read & Write — Full Practical | 13 | Read ECU via OBD and bench mode; create and store backup; write modified/replacement file; verify write success | practical |
| 6.4 | Online Coding & Variant Coding | 14 | What online coding is (manufacturer server auth); variant coding; adaptation reset; coding using VCDS, ISTA, ODIS | lab |
| 6.5 | Bootloader & Boot Mode Programming *(HIGH gap)* | 14 | What a bootloader is; primary vs secondary bootloader; boot mode access methods: **JTAG**, **BDM** (Background Debug Mode), **SPI** direct flash, **UART** boot, **K-Line boot**; when to use each; identifying boot pins on PCB; read/write via boot mode on a sample ECU | lecture + lab |
| 6.6 | Failed Programming Recovery | 14 | What happens when a write fails mid-flash; triboot and recovery procedures; using boot mode to recover a bricked ECU; checksum correction | lab |

**Module 6 Outcomes (MOs):**
- MO 6-1: Explain ECU programming modes (OBD, bench, boot) and select the appropriate method for a given ECU
- MO 6-2: Perform a safe ECU read-backup-write-verify cycle using at least two different tool platforms
- MO 6-3: Execute online coding and variant adaptations for a programmed ECU
- MO 6-4: Access ECU boot mode via JTAG, BDM, or SPI to read and write firmware on an ECU that cannot communicate via normal means
- MO 6-5: Recover an ECU from a failed or interrupted programming attempt

---

## Module 7: CAN Bus, LIN & Communication Diagnostics
### *Diagnosing the network — from bus errors to silent nodes*

**Duration:** 2 days (Days 15–16)
**Type:** Lecture + Lab + Practical
**CO Alignment:** co-1

**Purpose:**
CAN faults produce some of the most confusing symptom patterns in automotive repair — multiple modules appearing to fail simultaneously, intermittent communication losses, or complete network-down conditions. Understanding the protocol is the difference between replacing one correct component and replacing five wrong ones. LIN bus is added here as it is increasingly common in body control, seat, and climate modules.

**Lessons:**

| # | Lesson | Day | Content | Type |
|---|--------|-----|---------|------|
| 7.1 | CAN Bus Protocol Deep Dive | 15 | Frame structure (ID, DLC, data, CRC, ACK); arbitration; priority; error frames; error passive / bus-off states; differential signaling; termination resistors | lecture |
| 7.2 | CAN Bus Hardware — Transceivers & Filters | 15 | CAN transceiver IC function (TJA1050, SN65HVD230); common-mode choke on CAN lines; ESD protection; short-circuit protection; how transceiver failure manifests | lecture + lab |
| 7.3 | CAN Diagnosis — Oscilloscope & Scan Tool | 15 | Measuring CANH/CANL voltage levels; waveform capture; identifying: dominant errors, missing ACK, CRC errors, bus-off, one wire shorted; using scan tool network tests | lab |
| 7.4 | LIN Bus — Protocol, Hardware & Fault Finding *(MEDIUM gap)* | 16 | LIN vs CAN (single wire, master/slave, lower speed); LIN frame structure; LIN transceiver circuit; diagnosing LIN faults: no response from slave, wiring open, stuck dominant | lecture + lab |
| 7.5 | Multi-Node Fault Isolation | 16 | Disconnecting nodes to find CAN-off culprit; using network topology diagram; isolating fault to one ECU vs wiring vs termination; practical scenario — 3-node bench setup with planted faults | practical |

**Module 7 Outcomes (MOs):**
- MO 7-1: Explain CAN bus protocol, frame structure, arbitration, and error handling mechanisms
- MO 7-2: Diagnose CAN bus faults using oscilloscope and scan tool (dominant errors, bus-off, termination issues, node loss)
- MO 7-3: Diagnose LIN bus faults and identify failed master or slave nodes
- MO 7-4: Isolate a faulty node in a multi-ECU CAN network without replacing correct modules

---

## Module 8: Module-Specific Repair
### *Specialist procedures for each major control module*

**Duration:** 2 days (Days 17–18)
**Type:** Lab + Practical
**CO Alignment:** co-1, co-2

**Purpose:**
BCM, ABS, EPS, and instrument cluster modules each have their own failure patterns, EEPROM data structures, and programming requirements. Students work through each type systematically. ADAS module awareness is introduced here as these modules are appearing in more vehicles and technicians are encountering them with increasing frequency.

**Lessons:**

| # | Lesson | Day | Content | Type |
|---|--------|-----|---------|------|
| 8.1 | Odometer / Instrument Cluster Repair | 17 | Common failures (pixel rows, backlighting, stepper motors, display driver ICs); EEPROM data (odometer stored); correction procedures; display driver replacement | lab |
| 8.2 | BCM — Body Control Module Repair & Programming | 17 | BCM function (lighting, windows, locks, comfort systems); EEPROM data (coding, key data, configuration); common BCM faults; cloning vs re-coding; programming a replacement BCM | lab |
| 8.3 | EPS — Electronic Power Steering Module | 18 | EPS function; torque sensor interface; common EPS faults; steering angle sensor calibration; module replacement and coding procedure | lab |
| 8.4 | ABS Module Repair & Coding | 18 | ABS/ESP module function; hydraulic unit vs control unit; wheel speed sensor faults; module replacement and coding; bleeding procedure after module replacement | lab |
| 8.5 | ADAS Module Awareness *(MEDIUM gap)* | 18 | What ADAS modules are (camera ECU, radar ECU, ultrasonic); why they require calibration after replacement; static vs dynamic calibration; what tools are needed; knowing when to refer out; introduction only — not a certification | lecture |

**Module 8 Outcomes (MOs):**
- MO 8-1: Diagnose and repair common hardware and EEPROM faults in instrument cluster/odometer units
- MO 8-2: Service and program BCM modules including EEPROM data restoration and variant coding
- MO 8-3: Service EPS and ABS modules including fault diagnosis, mechanical checks, and coding
- MO 8-4: Explain what ADAS modules are, why they require specialist calibration, and when to refer to a calibration specialist

---

## Module 9: Security & Safety Systems + Final Assessment
### *Highest precision — key programming, immobilizer, airbag*

**Duration:** 2 days (Days 19–20)
**Type:** Lecture + Lab + Practical (Final Assessment)
**CO Alignment:** co-4

**Purpose:**
Security and safety systems carry the highest liability of any ECU repair work. An airbag module programmed incorrectly is a life safety risk. A key incorrectly cloned can permanently disable a vehicle. This module demands precision and deliberate procedure. The final assessment — unseen ECU fault under time pressure — tests everything the student has learned.

**Lessons:**

| # | Lesson | Day | Content | Type |
|---|--------|-----|---------|------|
| 9.1 | Key Cloning & Lost Key Recovery | 19 | Transponder chip types (ID46, ID48, PCF7936, 4D, Toyota G/H); cloning methods (direct copy vs calculation); lost key procedures; key programmer tools (VVDI2, Key Tool Max, Tango); legal and ethical considerations | lecture + lab |
| 9.2 | Immobilizer Programming | 19 | Immobilizer system architecture; PIN/CS reading via OBD and EEPROM dump; key learning procedures; anti-theft fault recovery; common immobilizer ECU failures; IMMO OFF procedures (where legal) | lab |
| 9.3 | Airbag Module Repair — Hardware & Crash Data | 20 | SRS system overview; crash data storage in EEPROM; hard faults vs soft faults; circuit testing before programming (clock spring, squib resistance, pre-tensioner checks); repairing hardware faults on SRS PCB | lecture + lab |
| 9.4 | Airbag Module Programming — Safety Procedures First | 20 | Crash data reset procedure; airbag programming tools; OEM vs aftermarket reset methods; safety protocol: battery disconnect, waiting period, testing before re-enabling; consequences of incorrect programming | lab |
| 9.5 | Final Practical Assessment | 20 | Unseen ECU with one or more real faults — student must: set up bench, diagnose, identify fault(s), propose repair, execute repair or programming procedure. Assessed individually. | practical |

**Module 9 Outcomes (MOs):**
- MO 9-1: Perform key cloning and lost key recovery procedures correctly using appropriate tools
- MO 9-2: Execute immobilizer programming including PIN/CS extraction and key adaptation procedures
- MO 9-3: Safely diagnose and repair hardware faults on airbag (SRS) modules, including crash data assessment
- MO 9-4: Program and reset airbag modules following correct safety protocols

---

## Day-by-Day Master Schedule

| Day | Module | Main Topics |
|-----|--------|-------------|
| 1 | M1 | Dev board vs ECU; automotive environment; ESD safety; physical PCB tour |
| 2 | M2 | Multimeter mastery; oscilloscope setup & signal capture |
| 3 | M2 | Oscilloscope waveform analysis; wiring diagrams; sensor/actuator testing |
| 4 | M3 | PCB layout deep dive; MCU/EEPROM/FLASH; watchdog circuits |
| 5 | M3 | Power supply; protection circuits (TVS, load dump); filtering (bulk caps, bypass, ferrite beads, common-mode chokes, EMI) |
| 6 | M3 | Signal conditioning; injector drivers & power stages; power stage failure analysis; thermal management |
| 7 | M4 | SMD soldering (iron); SMD desoldering (wick/braid) |
| 8 | M4 | Hot air soldering/desoldering; QFP IC replacement; BGA intro |
| 9 | M4 | IC testing & datasheet reading; CAN box build |
| 10 | M5 | Bench test setup; ECU scanning & fault codes |
| 11 | M5 | Line tracking; component testing on live ECU |
| 12 | M5 | Environmental damage (moisture/corrosion); fault finding case studies |
| 13 | M6 | Programming fundamentals; tools overview; ECU read/write practical |
| 14 | M6 | Online coding; bootloader & boot modes (JTAG/BDM/SPI/UART); recovery from failed flash |
| 15 | M7 | CAN protocol; CAN hardware & transceivers; CAN oscilloscope diagnosis |
| 16 | M7 | LIN bus protocol & fault finding; multi-node CAN fault isolation practical |
| 17 | M8 | Instrument cluster repair; BCM repair & programming |
| 18 | M8 | EPS module; ABS module; ADAS module awareness |
| 19 | M9 | Key cloning & lost key recovery; immobilizer programming |
| 20 | M9 | Airbag hardware repair; airbag programming + safety; **Final Assessment** |

---

## Gap Coverage Summary

| Priority | Gap | Status | Location |
|----------|-----|--------|----------|
| 🔴 HIGH | ESD protection & safe handling | ✅ Included | Module 1, Lesson 1.3 |
| 🔴 HIGH | Advanced power stage failure analysis | ✅ Included | Module 3, Lesson 3.10 |
| 🔴 HIGH | Bootloader & boot mode programming (JTAG/BDM/SPI/UART) | ✅ Included | Module 6, Lesson 6.5 |
| 🟡 MEDIUM | Filtering circuits (decoupling, bulk, RC, LC) | ✅ Included | Module 3, Lesson 3.6 |
| 🟡 MEDIUM | EMI/EMC components & design principles | ✅ Included | Module 3, Lesson 3.7 |
| 🟡 MEDIUM | Environmental failure analysis (moisture/corrosion) | ✅ Included | Module 5, Lesson 5.5 |
| 🟡 MEDIUM | Thermal management & thermal imaging | ✅ Included | Module 3, Lesson 3.11 |
| 🟡 MEDIUM | LIN bus diagnostics | ✅ Included | Module 7, Lesson 7.4 |
| 🟡 MEDIUM | ADAS module awareness | ✅ Included | Module 8, Lesson 8.5 |
| 🟠 LOW | Reverse engineering / schematic from PCB | ⬜ Not included (future advanced module) |
| 🟠 LOW | ECU security / seed-key basics | ⬜ Not included (future module) |
| 🟢 LOW | Workshop business basics | ⬜ Not included (optional add-on) |

---

## Original 20 Topics — Coverage Map

| # | Instructor Topic | Module | Lesson |
|---|-----------------|--------|--------|
| 1 | ECM/ECU Programming | M6 | 6.3, 6.4 |
| 2 | ECM/ECU On Table scanning and testing | M5 | 5.1, 5.2 |
| 3 | ECM/ECU Line Tracking | M5 | 5.3 |
| 4 | ECM/ECU component test on board & fault finding | M5 | 5.4, 5.6 |
| 5 | ECM/ECU IC testing & replacement techniques | M4 | 4.4, 4.6 |
| 6 | PCB layout understanding | M3 | 3.1 |
| 7 | Microcontroller / processor, EEPROM, FLASH | M3 | 3.2 |
| 8 | Injector driver and others | M3 | 3.9 |
| 9 | PCB, SMD Soldering / Desoldering hands on experience | M4 | 4.1, 4.2, 4.3 |
| 10 | How to read Wiring diagram | M2 | 2.4 |
| 11 | How to use different type of Multimeter & oscilloscope | M2 | 2.1, 2.2, 2.3 |
| 12 | Canbox Connections / how to make your own canbox | M4 | 4.7 |
| 13 | Sensor & actuators working & Testing | M2 | 2.5 |
| 14 | Odometer / Instrument Cluster repair | M8 | 8.1 |
| 15 | BCM & EPS & ABS Modules repair | M8 | 8.2, 8.3, 8.4 |
| 16 | Key cloning & lost key coding | M9 | 9.1 |
| 17 | Immobilizer Programming | M9 | 9.2 |
| 18 | Air Bag Module programming | M9 | 9.3, 9.4 |
| 19 | Online coding | M6 | 6.4 |
| 20 | CAN diagnosis | M7 | 7.3, 7.5 |

---

## Assessment Plan

| Assessment | Timing | Weight | Notes |
|-----------|--------|--------|-------|
| Module Quizzes (x5) | End of M2, M3, M6, M7, M9 | 20% | Short written — theory recall |
| Practical Check-offs | During M4, M5, M6 | 30% | Instructor signs off each skill |
| Mid-course Practical | End of M5 (Day 12) | 20% | Diagnose a bench ECU fault from scratch |
| Final Practical Assessment | Day 20 | 30% | Unseen ECU — diagnose, repair/program, explain |

**Passing Criteria:** 70% practical aggregate, 60% theory aggregate

---

## Next Steps

- [ ] Generate full CO → MO → SO hierarchy with Bloom taxonomy assignments
- [ ] Generate Excel template (03-template.xlsx) for CDS platform upload
- [ ] Review MO count per module and confirm SO depth per lesson
