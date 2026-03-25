# ECU Hardware Repair — Learning Outcomes Hierarchy
## CO → MO → SO Full Mapping

**Course Code:** ECUHR
**Generated:** 2026-02-18
**Total COs:** 4 | **Total MOs:** 38 | **Total SOs:** 120
**Bloom Target:** Apply level minimum for all practical SOs; Understand for foundational knowledge SOs

---

## COURSE OUTCOMES (COs)

| CO ID | CO Code | Description | Category | Bloom |
|-------|---------|-------------|----------|-------|
| co-1 | ECUHR-CO-1 | Diagnose ECU faults at the component level by applying knowledge of automotive-grade circuit design, protection, and signal conditioning | Skill | Analyze |
| co-2 | ECUHR-CO-2 | Repair ECU PCBs by identifying and replacing faulty electronic components using correct soldering, rework, and safety techniques | Skill | Apply |
| co-3 | ECUHR-CO-3 | Program, code, and update ECUs and control modules using appropriate tools including OBD, bench mode, and bootloader methods | Skill | Apply |
| co-4 | ECUHR-CO-4 | Configure and recover vehicle security and safety systems including key programming, immobilizer setup, and airbag module coding | Skill | Apply |

---

## MODULE 1: ECU in the Real World (Day 1)
**CO Alignment:** co-1

### MO 1-1 | ECUHR-MO-1-1
**Description:** Explain why automotive ECUs require protection and filtering circuits that development boards do not, using the automotive electrical environment as context
**Category:** Knowledge | **Bloom:** Understand

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-1-1-1 | ECUHR-SO-1-1-1 | Compare an Arduino/STM32 development board to an automotive ECU across voltage, temperature, EMI, and vibration requirements | Knowledge | Understand | 01T |
| so-1-1-2 | ECUHR-SO-1-1-2 | Identify the automotive electrical environment hazards that drive ECU circuit complexity (load dump, reverse polarity, ESD, thermal extremes) | Knowledge | Understand | 01T |
| so-1-1-3 | ECUHR-SO-1-1-3 | Explain why each "extra" component category on an ECU PCB (filters, TVS, watchdog, drivers) exists and what failure it prevents | Knowledge | Understand | 01T |

### MO 1-2 | ECUHR-MO-1-2
**Description:** Describe the automotive electrical environment and its effect on ECU electronic design decisions
**Category:** Knowledge | **Bloom:** Understand

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-1-2-1 | ECUHR-SO-1-2-1 | Describe battery voltage variation (9–16V), load dump events (up to 40V), and their impact on ECU design | Knowledge | Understand | 01T |
| so-1-2-2 | ECUHR-SO-1-2-2 | Identify EMI sources in the vehicle (alternator, ignition, motors) and explain how they couple into ECU circuits | Knowledge | Understand | 01T |
| so-1-2-3 | ECUHR-SO-1-2-3 | Explain temperature range requirements (−40°C to +125°C) and how they affect component selection and circuit margins | Knowledge | Understand | 01T |

### MO 1-3 | ECUHR-MO-1-3
**Description:** Apply correct ESD safety procedures when handling ECUs and PCB components in the workshop
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-1-3-1 | ECUHR-SO-1-3-1 | Explain how electrostatic discharge damages semiconductor junctions and list voltage thresholds that cause damage | Knowledge | Understand | 01T |
| so-1-3-2 | ECUHR-SO-1-3-2 | Demonstrate correct use of anti-static wrist strap, ESD mat, and ESD-safe packaging when handling ECUs | Skill | Apply | 01H |
| so-1-3-3 | ECUHR-SO-1-3-3 | Identify regions on an ECU PCB and correctly handle the board without touching sensitive ICs or connectors | Skill | Apply | 01H |
| so-1-3-4 | ECUHR-SO-1-3-4 | Inspect a real ECU and label the major circuit regions (power supply, processor, drivers, communication, connectors) | Skill | Apply | 01H |

---

## MODULE 2: Tools & Measurement Mastery (Days 2–3)
**CO Alignment:** co-1, co-2

### MO 2-1 | ECUHR-MO-2-1
**Description:** Use a multimeter at component level for resistance, diode, voltage-drop, and continuity measurements on ECU PCBs
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-2-1-1 | ECUHR-SO-2-1-1 | Select the correct multimeter setting and probe technique for measuring component-level resistance on an ECU PCB | Skill | Apply | 02T |
| so-2-1-2 | ECUHR-SO-2-1-2 | Perform diode forward-voltage and back-voltage tests on protection diodes and TVS devices on an ECU | Skill | Apply | 02H |
| so-2-1-3 | ECUHR-SO-2-1-3 | Measure voltage drop across suspect PCB traces to identify high-resistance joints or damaged tracks | Skill | Apply | 02H |
| so-2-1-4 | ECUHR-SO-2-1-4 | Use continuity mode to verify trace integrity from connector pin to component pad on a real ECU | Skill | Apply | 02H |

### MO 2-2 | ECUHR-MO-2-2
**Description:** Operate an oscilloscope to capture and interpret ECU signal waveforms including PWM, CAN, and sensor outputs
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-2-2-1 | ECUHR-SO-2-2-1 | Configure oscilloscope timebase, trigger, and channel coupling for capturing ECU signals correctly | Skill | Apply | 02T |
| so-2-2-2 | ECUHR-SO-2-2-2 | Capture and measure a PWM output signal — identify frequency, duty cycle, and amplitude | Skill | Apply | 02H |
| so-2-2-3 | ECUHR-SO-2-2-3 | Capture and compare a healthy vs degraded ECU sensor signal waveform and identify the anomaly | Skill | Analyze | 03T |
| so-2-2-4 | ECUHR-SO-2-2-4 | Capture injector drive signal and identify peak-and-hold phases and freewheeling spike | Skill | Analyze | 03T |

### MO 2-3 | ECUHR-MO-2-3
**Description:** Read ECU wiring diagrams to trace signals from connector pins to circuit components
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-2-3-1 | ECUHR-SO-2-3-1 | Identify connector reference numbers, pin assignments, signal names, and wire colours on an ECU wiring diagram | Knowledge | Understand | 03T |
| so-2-3-2 | ECUHR-SO-2-3-2 | Trace a complete signal path from sensor output through wiring harness to ECU connector pin using a wiring diagram | Skill | Apply | 03H |
| so-2-3-3 | ECUHR-SO-2-3-3 | Identify power supply and ground reference pins for a given ECU connector and verify them physically | Skill | Apply | 03H |

### MO 2-4 | ECUHR-MO-2-4
**Description:** Test automotive sensors and actuators using correct measurement methods and reference values
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-2-4-1 | ECUHR-SO-2-4-1 | Test a TPS (throttle position sensor) and MAP sensor using multimeter and compare readings to specification | Skill | Apply | 03H |
| so-2-4-2 | ECUHR-SO-2-4-2 | Test a crankshaft/camshaft position sensor output using oscilloscope and identify signal pattern anomalies | Skill | Apply | 03H |
| so-2-4-3 | ECUHR-SO-2-4-3 | Measure actuator coil resistance (injector, idle valve, solenoid) and verify against specification | Skill | Apply | 03H |

---

## MODULE 3: ECU Architecture, Protection & Filtering (Days 4–6)
**CO Alignment:** co-1, co-2

### MO 3-1 | ECUHR-MO-3-1
**Description:** Identify and explain the function of all major circuit regions on an ECU PCB
**Category:** Knowledge | **Bloom:** Understand

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-3-1-1 | ECUHR-SO-3-1-1 | Identify PCB layer structure (signal, power, ground planes) and explain the purpose of each layer | Knowledge | Understand | 04T |
| so-3-1-2 | ECUHR-SO-3-1-2 | Locate and identify test points, reference designators, and component silkscreen markings on a real ECU PCB | Skill | Apply | 04H |
| so-3-1-3 | ECUHR-SO-3-1-3 | Explain the roles of microcontroller, co-processor, EEPROM (calibration), FLASH (firmware), RAM, and clock oscillator in ECU operation | Knowledge | Understand | 04T |
| so-3-1-4 | ECUHR-SO-3-1-4 | Explain watchdog circuit function and describe what happens when firmware hangs without a watchdog reset | Knowledge | Understand | 04T |

### MO 3-2 | ECUHR-MO-3-2
**Description:** Explain the role of protection circuits (reverse polarity, TVS, load dump) and identify them on a real ECU PCB
**Category:** Knowledge | **Bloom:** Understand

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-3-2-1 | ECUHR-SO-3-2-1 | Explain load dump events (ISO 7637) and how TVS diodes and Zener clamps limit the transient voltage reaching ICs | Knowledge | Understand | 05T |
| so-3-2-2 | ECUHR-SO-3-2-2 | Identify reverse polarity protection circuits (diode, MOSFET-based) on an ECU PCB and test their function with a multimeter | Skill | Apply | 05H |
| so-3-2-3 | ECUHR-SO-3-2-3 | Trace the voltage path from battery connector to main power rail and identify each protection stage encountered | Skill | Apply | 05H |

### MO 3-3 | ECUHR-MO-3-3
**Description:** Identify and explain each filtering component type (bulk capacitor, bypass capacitor, ferrite bead, common-mode choke, RC filter) and its placement on a real ECU PCB
**Category:** Knowledge | **Bloom:** Understand

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-3-3-1 | ECUHR-SO-3-3-1 | Explain the purpose of bulk capacitors on the main power rail and why they are needed during engine cranking voltage dips | Knowledge | Understand | 05T |
| so-3-3-2 | ECUHR-SO-3-3-2 | Explain decoupling/bypass capacitor function at IC power pins and why omitting or damaging them causes IC malfunction | Knowledge | Understand | 05T |
| so-3-3-3 | ECUHR-SO-3-3-3 | Identify ferrite beads on power supply traces on a real ECU and explain their high-frequency noise blocking role | Skill | Apply | 05H |
| so-3-3-4 | ECUHR-SO-3-3-4 | Identify common-mode chokes on CAN/LIN bus lines and explain how they suppress EMI without affecting the differential signal | Knowledge | Understand | 05T |
| so-3-3-5 | ECUHR-SO-3-3-5 | Explain RC filter function on analog sensor input lines and describe the effect of a failed capacitor on sensor signal quality | Knowledge | Understand | 05T |

### MO 3-4 | ECUHR-MO-3-4
**Description:** Explain EMI sources in the vehicle environment and identify EMC mitigation components on the PCB
**Category:** Knowledge | **Bloom:** Understand

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-3-4-1 | ECUHR-SO-3-4-1 | Distinguish between differential-mode and common-mode noise and explain how each couples into ECU circuits | Knowledge | Understand | 05T |
| so-3-4-2 | ECUHR-SO-3-4-2 | Identify a π-filter (cap-ferrite-cap) on an ECU power input and explain why it is more effective than a single capacitor | Knowledge | Understand | 05T |
| so-3-4-3 | ECUHR-SO-3-4-3 | Explain PCB layout EMC rules: ground plane importance, trace routing near connectors, component placement for noise suppression | Knowledge | Understand | 05T |

### MO 3-5 | ECUHR-MO-3-5
**Description:** Analyze output power stage circuits and identify common failure modes from overcurrent, overvoltage, and thermal overload
**Category:** Skill | **Bloom:** Analyze

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-3-5-1 | ECUHR-SO-3-5-1 | Explain low-side vs high-side driver operation and identify each type on an ECU schematic | Knowledge | Understand | 06T |
| so-3-5-2 | ECUHR-SO-3-5-2 | Explain flyback/freewheeling diode function on inductive loads and describe the failure mode when the diode is missing or shorted | Knowledge | Understand | 06T |
| so-3-5-3 | ECUHR-SO-3-5-3 | Analyze an oscilloscope capture of an injector drive signal and identify missing flyback spike, overcurrent clamp, or driver failure signatures | Skill | Analyze | 06H |
| so-3-5-4 | ECUHR-SO-3-5-4 | Test a suspected failed output driver IC using multimeter resistance measurements and interpret results against datasheet limits | Skill | Apply | 06H |

### MO 3-6 | ECUHR-MO-3-6
**Description:** Use thermal camera and component derating knowledge to identify heat-related failure candidates on an ECU
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-3-6-1 | ECUHR-SO-3-6-1 | Explain junction temperature, thermal resistance (Rθja), and component derating — describe why components that fail in summer were not "broken" in winter | Knowledge | Understand | 06T |
| so-3-6-2 | ECUHR-SO-3-6-2 | Use a thermal camera to identify hot components on a powered ECU and rank them by thermal risk | Skill | Apply | 06H |
| so-3-6-3 | ECUHR-SO-3-6-3 | Inspect a thermal paste/pad application on an ECU power stage and assess whether heat transfer is adequate | Skill | Evaluate | 06H |

---

## MODULE 4: PCB Repair & Soldering Skills (Days 7–9)
**CO Alignment:** co-2

### MO 4-1 | ECUHR-MO-4-1
**Description:** Perform SMD soldering and desoldering on ECU-grade PCBs without lifting pads or damaging adjacent components
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-4-1-1 | ECUHR-SO-4-1-1 | Select correct solder tip, iron temperature, flux type, and solder alloy for SMD work on an automotive ECU PCB | Knowledge | Apply | 07T |
| so-4-1-2 | ECUHR-SO-4-1-2 | Solder 0402, 0603, and SOIC-8 components onto a practice PCB with correct joint formation (shiny, concave fillet, no bridges) | Skill | Apply | 07H |
| so-4-1-3 | ECUHR-SO-4-1-3 | Remove SMD components using desoldering wick/braid and inspect pads for damage, lifted traces, or residue | Skill | Apply | 07H |

### MO 4-2 | ECUHR-MO-4-2
**Description:** Remove and replace ICs in SOIC, QFP, and TQFP packages using hot air and iron techniques
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-4-2-1 | ECUHR-SO-4-2-1 | Configure hot air station temperature and airflow for safely removing SOIC and QFP ICs without PCB or component damage | Skill | Apply | 08T |
| so-4-2-2 | ECUHR-SO-4-2-2 | Remove a QFP IC using hot air and clean pads ready for replacement component | Skill | Apply | 08H |
| so-4-2-3 | ECUHR-SO-4-2-3 | Align and solder a replacement QFP IC using flux-assisted drag soldering and verify all pins under magnification | Skill | Apply | 08H |
| so-4-2-4 | ECUHR-SO-4-2-4 | Explain BGA package construction, why reballing is required, and what equipment is needed for professional BGA rework | Knowledge | Understand | 08T |

### MO 4-3 | ECUHR-MO-4-3
**Description:** Identify ICs from package markings, locate datasheets, and test functionality in-circuit
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-4-3-1 | ECUHR-SO-4-3-1 | Decode IC package markings to identify manufacturer, part number, and date code, then locate the corresponding datasheet | Skill | Apply | 09T |
| so-4-3-2 | ECUHR-SO-4-3-2 | Read an IC datasheet to extract: supply voltage range, pin functions, absolute maximum ratings, and typical application circuit | Knowledge | Understand | 09T |
| so-4-3-3 | ECUHR-SO-4-3-3 | Test a suspected faulty IC using in-circuit voltage measurements on power and output pins, comparing to datasheet values | Skill | Apply | 09H |

### MO 4-4 | ECUHR-MO-4-4
**Description:** Construct a functional CAN box from components and explain its circuit operation
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-4-4-1 | ECUHR-SO-4-4-1 | Explain the schematic of a CAN box — microcontroller, CAN transceiver IC, termination resistor, connector, and power supply | Knowledge | Understand | 09T |
| so-4-4-2 | ECUHR-SO-4-4-2 | Assemble a CAN box from kit components using soldering skills from Days 7–8 and verify electrical continuity | Skill | Apply | 09H |
| so-4-4-3 | ECUHR-SO-4-4-3 | Test the completed CAN box for correct voltage levels, transceiver output, and communication with a vehicle or ECU simulator | Skill | Apply | 09H |

---

## MODULE 5: ECU On-Table Diagnostics (Days 10–12)
**CO Alignment:** co-1

### MO 5-1 | ECUHR-MO-5-1
**Description:** Configure a safe bench test setup for a removed ECU and establish communication
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-5-1-1 | ECUHR-SO-5-1-1 | Identify required connections (battery positive, ground, ignition, CAN, K-Line) for bench testing a specific ECU from its wiring diagram | Skill | Apply | 10T |
| so-5-1-2 | ECUHR-SO-5-1-2 | Wire an ECU to a bench power supply with correct current limits and simulate ignition-on state | Skill | Apply | 10H |
| so-5-1-3 | ECUHR-SO-5-1-3 | Connect a scan tool to a bench ECU via OBD adapter and verify communication is established | Skill | Apply | 10H |

### MO 5-2 | ECUHR-MO-5-2
**Description:** Scan, read, and interpret fault codes and live data from a bench-mounted ECU
**Category:** Skill | **Bloom:** Analyze

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-5-2-1 | ECUHR-SO-5-2-1 | Read DTC codes from a bench ECU, classify them as current/permanent/pending, and identify the circuit each code points to | Skill | Analyze | 10T |
| so-5-2-2 | ECUHR-SO-5-2-2 | Compare live data readings from a bench ECU against expected values to identify sensors reporting out-of-range data | Skill | Analyze | 10H |
| so-5-2-3 | ECUHR-SO-5-2-3 | Clear DTCs, cycle ignition, and verify whether faults are confirmed or intermittent based on re-scan results | Skill | Apply | 10H |

### MO 5-3 | ECUHR-MO-5-3
**Description:** Trace signal paths through an ECU using wiring diagrams and in-circuit measurement to locate faults
**Category:** Skill | **Bloom:** Analyze

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-5-3-1 | ECUHR-SO-5-3-1 | Use a wiring diagram to identify the complete signal path for a DTC, from sensor output through harness to ECU processing stage | Skill | Analyze | 11T |
| so-5-3-2 | ECUHR-SO-5-3-2 | Probe a live ECU signal line using oscilloscope, compare to expected waveform, and identify where the signal degrades | Skill | Analyze | 11H |
| so-5-3-3 | ECUHR-SO-5-3-3 | Use split-half fault isolation to narrow a line-tracking fault to a specific PCB stage or component | Skill | Analyze | 11H |

### MO 5-4 | ECUHR-MO-5-4
**Description:** Assess and clean moisture and corrosion damage on ECU PCBs and determine repairability
**Category:** Skill | **Bloom:** Evaluate

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-5-4-1 | ECUHR-SO-5-4-1 | Identify water ingress entry points on a disassembled ECU housing and explain common moisture damage failure modes | Knowledge | Understand | 12T |
| so-5-4-2 | ECUHR-SO-5-4-2 | Assess corrosion severity on PCB traces and connector pins and classify as: cleanable, repairable, or beyond economic repair | Skill | Evaluate | 12H |
| so-5-4-3 | ECUHR-SO-5-4-3 | Clean a moisture-damaged ECU PCB using isopropyl alcohol and correct tools, then inspect under magnification for residual damage | Skill | Apply | 12H |
| so-5-4-4 | ECUHR-SO-5-4-4 | Diagnose an ECU with a planted fault from case studies (component failure, power stage, trace, or moisture) and document findings | Skill | Analyze | 12H |

---

## MODULE 6: ECU Programming & Bootloader (Days 13–14)
**CO Alignment:** co-3

### MO 6-1 | ECUHR-MO-6-1
**Description:** Explain ECU programming modes (OBD, bench, boot) and select the appropriate method for a given ECU
**Category:** Knowledge | **Bloom:** Understand

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-6-1-1 | ECUHR-SO-6-1-1 | Distinguish between OBD-mode, bench-mode, and boot-mode programming and state when each method is appropriate | Knowledge | Understand | 13T |
| so-6-1-2 | ECUHR-SO-6-1-2 | Explain the read-backup-write-verify workflow and state why a backup must be created before any write operation | Knowledge | Understand | 13T |
| so-6-1-3 | ECUHR-SO-6-1-3 | Identify common ECU file formats (.bin, .hex, .mot, .s19) and explain what each represents | Knowledge | Understand | 13T |

### MO 6-2 | ECUHR-MO-6-2
**Description:** Perform a safe ECU read-backup-write-verify cycle using at least two different programming tool platforms
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-6-2-1 | ECUHR-SO-6-2-1 | Connect and configure a programming tool (KTM Bench or equivalent) for bench-mode reading of a sample ECU | Skill | Apply | 13H |
| so-6-2-2 | ECUHR-SO-6-2-2 | Complete a full ECU read cycle, save backup file with correct naming convention, and verify file size and checksum | Skill | Apply | 13H |
| so-6-2-3 | ECUHR-SO-6-2-3 | Write a verified file back to the ECU and confirm successful write with a post-write read comparison | Skill | Apply | 13H |

### MO 6-3 | ECUHR-MO-6-3
**Description:** Execute online coding and variant adaptations for a programmed ECU
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-6-3-1 | ECUHR-SO-6-3-1 | Explain what online coding is, why it requires manufacturer server authentication, and which ECU types require it | Knowledge | Understand | 14T |
| so-6-3-2 | ECUHR-SO-6-3-2 | Perform a variant coding procedure on a sample ECU using VCDS or equivalent tool and verify coding changes | Skill | Apply | 14H |
| so-6-3-3 | ECUHR-SO-6-3-3 | Execute an adaptation reset on a sample ECU and verify the ECU accepts the new learned values | Skill | Apply | 14H |

### MO 6-4 | ECUHR-MO-6-4
**Description:** Access ECU boot mode via JTAG, BDM, or SPI to read and write firmware on an ECU that cannot communicate via normal means
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-6-4-1 | ECUHR-SO-6-4-1 | Explain bootloader architecture (primary vs secondary), boot mode trigger mechanisms, and the difference between JTAG, BDM, SPI, and UART boot access | Knowledge | Understand | 14T |
| so-6-4-2 | ECUHR-SO-6-4-2 | Identify JTAG/BDM/SPI access pins on an ECU PCB using datasheet and schematic research | Skill | Apply | 14H |
| so-6-4-3 | ECUHR-SO-6-4-3 | Connect boot mode programmer to a sample ECU and perform a direct FLASH read via SPI or BDM interface | Skill | Apply | 14H |

### MO 6-5 | ECUHR-MO-6-5
**Description:** Recover an ECU from a failed or interrupted programming attempt
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-6-5-1 | ECUHR-SO-6-5-1 | Diagnose a bricked ECU (no OBD communication after failed flash) and identify the appropriate recovery method | Skill | Analyze | 14T |
| so-6-5-2 | ECUHR-SO-6-5-2 | Recover a bricked sample ECU using boot mode programming to restore a known-good firmware file | Skill | Apply | 14H |

---

## MODULE 7: CAN Bus, LIN & Communication Diagnostics (Days 15–16)
**CO Alignment:** co-1

### MO 7-1 | ECUHR-MO-7-1
**Description:** Explain CAN bus protocol, frame structure, arbitration, and error handling mechanisms
**Category:** Knowledge | **Bloom:** Understand

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-7-1-1 | ECUHR-SO-7-1-1 | Describe CAN bus differential signaling (CANH/CANL), dominant/recessive states, and why it provides noise immunity | Knowledge | Understand | 15T |
| so-7-1-2 | ECUHR-SO-7-1-2 | Identify the fields of a CAN data frame (SOF, ID, DLC, data bytes, CRC, ACK, EOF) and explain each field's role | Knowledge | Understand | 15T |
| so-7-1-3 | ECUHR-SO-7-1-3 | Explain CAN bus arbitration (CSMA/CD with non-destructive bitwise arbitration) and how message priority is determined by ID | Knowledge | Understand | 15T |
| so-7-1-4 | ECUHR-SO-7-1-4 | Explain CAN error states (error active, error passive, bus-off) and the error counter mechanism that drives each state | Knowledge | Understand | 15T |

### MO 7-2 | ECUHR-MO-7-2
**Description:** Diagnose CAN bus faults using oscilloscope and scan tool (dominant errors, bus-off, termination, node loss)
**Category:** Skill | **Bloom:** Analyze

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-7-2-1 | ECUHR-SO-7-2-1 | Measure CAN bus voltage levels (CANH/CANL) in recessive and dominant states and compare to spec (2.5V/3.5V/1.5V) | Skill | Apply | 15H |
| so-7-2-2 | ECUHR-SO-7-2-2 | Use oscilloscope to capture CAN bus waveform and identify a specific fault (dominant stuck, missing ACK, corrupted frame) | Skill | Analyze | 15H |
| so-7-2-3 | ECUHR-SO-7-2-3 | Measure CAN bus termination resistance (should be ~60Ω across CANH/CANL) and diagnose missing or double termination | Skill | Apply | 15H |
| so-7-2-4 | ECUHR-SO-7-2-4 | Use a scan tool network test to identify a bus-off node and distinguish between shorted bus wire, failed transceiver, and failed ECU | Skill | Analyze | 15H |

### MO 7-3 | ECUHR-MO-7-3
**Description:** Diagnose LIN bus faults and identify failed master or slave nodes
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-7-3-1 | ECUHR-SO-7-3-1 | Explain LIN bus topology (single wire, master/slave, 12V), frame structure, and common applications (seat, climate, mirror modules) | Knowledge | Understand | 16T |
| so-7-3-2 | ECUHR-SO-7-3-2 | Measure LIN bus signal using oscilloscope and identify a healthy frame vs a no-response, stuck-dominant, or open-circuit fault | Skill | Analyze | 16H |
| so-7-3-3 | ECUHR-SO-7-3-3 | Identify a failed LIN slave node by disconnecting nodes and observing which removal restores bus operation | Skill | Apply | 16H |

### MO 7-4 | ECUHR-MO-7-4
**Description:** Isolate a faulty node in a multi-ECU CAN network without replacing correct modules
**Category:** Skill | **Bloom:** Analyze

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-7-4-1 | ECUHR-SO-7-4-1 | Use a network topology diagram to identify which nodes share a CAN bus segment and plan a systematic disconnection sequence | Skill | Apply | 16T |
| so-7-4-2 | ECUHR-SO-7-4-2 | Isolate the fault-causing node in a 3-node bench CAN network with a planted fault by selective disconnection and bus monitoring | Skill | Analyze | 16H |
| so-7-4-3 | ECUHR-SO-7-4-3 | Document the diagnosis process and correctly identify whether the root cause is a wiring fault, transceiver failure, or ECU hardware fault | Skill | Evaluate | 16H |

---

## MODULE 8: Module-Specific Repair (Days 17–18)
**CO Alignment:** co-1, co-2

### MO 8-1 | ECUHR-MO-8-1
**Description:** Diagnose and repair common hardware and EEPROM faults in instrument cluster and odometer units
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-8-1-1 | ECUHR-SO-8-1-1 | Identify common instrument cluster failure modes: pixel row loss, display driver IC failure, backlight failure, and stepper motor fault | Knowledge | Understand | 17T |
| so-8-1-2 | ECUHR-SO-8-1-2 | Diagnose a pixel row fault on an LCD cluster display and replace the display driver IC using soldering skills | Skill | Apply | 17H |
| so-8-1-3 | ECUHR-SO-8-1-3 | Read and write odometer EEPROM data using appropriate tools and explain the legal and ethical considerations | Skill | Apply | 17H |

### MO 8-2 | ECUHR-MO-8-2
**Description:** Service and program BCM modules including EEPROM data restoration and variant coding
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-8-2-1 | ECUHR-SO-8-2-1 | Explain BCM function (lighting, windows, locks, comfort), common failure modes, and what data is stored in BCM EEPROM | Knowledge | Understand | 17T |
| so-8-2-2 | ECUHR-SO-8-2-2 | Read BCM EEPROM, restore data to a replacement BCM, and program the replacement unit for the vehicle | Skill | Apply | 17H |
| so-8-2-3 | ECUHR-SO-8-2-3 | Perform variant coding on a BCM to configure vehicle-specific options and verify correct operation | Skill | Apply | 17H |

### MO 8-3 | ECUHR-MO-8-3
**Description:** Service EPS and ABS modules including fault diagnosis, component repair, and coding procedures
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-8-3-1 | ECUHR-SO-8-3-1 | Explain EPS module function, torque sensor interface, common EPS failure modes (power stage, sensor input, coding loss) | Knowledge | Understand | 18T |
| so-8-3-2 | ECUHR-SO-8-3-2 | Diagnose an EPS fault by scanning DTCs, testing the torque sensor signal, and identifying the faulty stage | Skill | Analyze | 18H |
| so-8-3-3 | ECUHR-SO-8-3-3 | Diagnose an ABS module fault, identify whether the fault is in the hydraulic unit, control electronics, or wheel speed sensor interface | Skill | Analyze | 18H |
| so-8-3-4 | ECUHR-SO-8-3-4 | Perform coding and adaptation for a replacement ABS module and verify correct operation with scan tool | Skill | Apply | 18H |

### MO 8-4 | ECUHR-MO-8-4
**Description:** Explain what ADAS modules are, why they require specialist calibration, and when to refer to a calibration specialist
**Category:** Knowledge | **Bloom:** Understand

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-8-4-1 | ECUHR-SO-8-4-1 | Identify common ADAS modules in modern vehicles (front camera ECU, radar ECU, ultrasonic control unit) and their function | Knowledge | Understand | 18T |
| so-8-4-2 | ECUHR-SO-8-4-2 | Explain why ADAS modules require static and/or dynamic calibration after replacement or any mechanical work | Knowledge | Understand | 18T |
| so-8-4-3 | ECUHR-SO-8-4-3 | Describe what equipment is needed for ADAS calibration, what the consequences of uncalibrated ADAS are, and when to refer the customer to a specialist | Knowledge | Evaluate | 18T |

---

## MODULE 9: Security & Safety Systems + Final Assessment (Days 19–20)
**CO Alignment:** co-4

### MO 9-1 | ECUHR-MO-9-1
**Description:** Perform key cloning and lost key recovery procedures correctly using appropriate tools
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-9-1-1 | ECUHR-SO-9-1-1 | Identify transponder chip types (ID46, ID48, PCF7936, 4D, Toyota G/H) and select the correct cloning or programming method for each | Knowledge | Understand | 19T |
| so-9-1-2 | ECUHR-SO-9-1-2 | Perform a direct key clone from a working key using a key programmer tool (VVDI2 or equivalent) | Skill | Apply | 19H |
| so-9-1-3 | ECUHR-SO-9-1-3 | Execute a lost key recovery procedure using EEPROM dump from the ECU/immobilizer unit to generate a new key | Skill | Apply | 19H |

### MO 9-2 | ECUHR-MO-9-2
**Description:** Execute immobilizer programming including PIN/CS extraction and key adaptation procedures
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-9-2-1 | ECUHR-SO-9-2-1 | Explain immobilizer system architecture (ECU ↔ immobilizer ↔ transponder loop), anti-theft fault codes, and EEPROM PIN storage | Knowledge | Understand | 19T |
| so-9-2-2 | ECUHR-SO-9-2-2 | Extract PIN/CS from an immobilizer EEPROM dump and use it to add a key or perform an all-keys-lost procedure | Skill | Apply | 19H |
| so-9-2-3 | ECUHR-SO-9-2-3 | Match a replacement immobilizer unit to an ECU and verify anti-theft system operation with new key | Skill | Apply | 19H |

### MO 9-3 | ECUHR-MO-9-3
**Description:** Safely diagnose and repair hardware faults on airbag (SRS) modules, including crash data assessment
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-9-3-1 | ECUHR-SO-9-3-1 | Explain SRS system architecture (crash sensors, clock spring, squib circuits, pre-tensioners) and the consequences of incorrect repair | Knowledge | Understand | 20T |
| so-9-3-2 | ECUHR-SO-9-3-2 | Apply safety protocol before working on an SRS module: battery disconnect, wait period, squib resistance verification | Skill | Apply | 20T |
| so-9-3-3 | ECUHR-SO-9-3-3 | Distinguish between crash data (hard faults — replacement required) and non-deployment faults (soft faults — resettable) | Skill | Analyze | 20T |
| so-9-3-4 | ECUHR-SO-9-3-4 | Diagnose and repair a hardware fault on an SRS PCB (capacitor, resistor, or driver IC) using soldering skills | Skill | Apply | 20H |

### MO 9-4 | ECUHR-MO-9-4
**Description:** Program and reset airbag modules following correct safety protocols
**Category:** Skill | **Bloom:** Apply

| SO ID | SO Code | Description | Category | Bloom | Session |
|-------|---------|-------------|----------|-------|---------|
| so-9-4-1 | ECUHR-SO-9-4-1 | Perform a crash data reset on an SRS module using appropriate tool and verify successful reset with re-scan | Skill | Apply | 20H |
| so-9-4-2 | ECUHR-SO-9-4-2 | Program a replacement SRS module to the vehicle and verify all SRS components are fault-free after programming | Skill | Apply | 20H |
| so-9-4-3 | ECUHR-SO-9-4-3 | Demonstrate and explain all post-repair safety verification steps before returning a vehicle with serviced SRS system | Skill | Evaluate | 20H |

---

## FINAL ASSESSMENT SESSION (Day 20, Session H)

**Assessment Objective:**
Students independently diagnose and repair (or propose repair for) an unseen ECU fault within a defined time limit. Draws on all COs.

**Criteria:**
- Correct bench setup and communication established — 10%
- Systematic diagnostic approach (not random) — 20%
- Correct fault identification with evidence — 30%
- Correct repair or programming procedure — 30%
- Safety practices observed throughout — 10%

---

## OUTCOMES SUMMARY

| Module | MOs | SOs | Days |
|--------|-----|-----|------|
| M1: ECU in the Real World | 3 | 10 | 1 |
| M2: Tools & Measurement | 4 | 13 | 2–3 |
| M3: Architecture, Protection & Filtering | 6 | 21 | 4–6 |
| M4: PCB Repair & Soldering | 4 | 14 | 7–9 |
| M5: On-Table Diagnostics | 4 | 13 | 10–12 |
| M6: Programming & Bootloader | 5 | 14 | 13–14 |
| M7: CAN, LIN & Comms Diagnostics | 4 | 14 | 15–16 |
| M8: Module-Specific Repair | 4 | 13 | 17–18 |
| M9: Security & Safety + Final | 4 | 13 | 19–20 |
| **TOTAL** | **38** | **125** | **20** |
