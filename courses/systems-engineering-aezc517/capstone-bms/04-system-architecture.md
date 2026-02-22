# Chapter 4: System Architecture Definition

> **SE Processes Applied:** Architecture Definition (ISO/IEC 15288 §6.4.4)
> **AEZC517 Sessions Referenced:** Session 3 (Traditional vs MBSE), Session 5 (System Design and Architecture)
> **Estimated Reading Time:** 40 minutes

---

## 4.1 Architecture Development Process

Architecture definition translates the system requirements (Chapter 3) into a structural design solution. The process follows three steps, producing four architecture views:

**Step 1 — Functional Decomposition:** What functions must the BMS perform? (Derived from Chapter 3 functional requirements)

**Step 2 — Logical Grouping:** How are functions organized into subsystems and their relationships? (Derived from ASIL partitioning, processing dependencies)

**Step 3 — Physical Realization:** What hardware and software elements implement the logical design? (Component selection, driven by ASIL, cost, availability)

**Step 4 — Interface Definition:** How do all elements communicate? (Protocols, signal ranges, ASIL, timing)

In an MBSE (Model-Based Systems Engineering) project using SysML (Session 3), these four views would be represented by:
- **Block Definition Diagram (BDD)** → Physical architecture
- **Internal Block Diagram (IBD)** → Interface architecture
- **Activity Diagram** → Functional architecture
- **State Machine Diagram** → Fault detection state transitions

For this case study, each view is represented in structured Markdown notation equivalent to what these SysML diagrams would capture.

---

## 4.2 Functional Architecture

The BMS must perform six top-level functions. Each is decomposed into sub-functions:

```
BMS Functional Architecture
│
├── F1: MONITOR
│   ├── F1.1  Measure individual cell voltages (all 448 cells, 10ms cycle)
│   ├── F1.2  Measure module temperatures (16 NTC sensors, 100ms cycle)
│   ├── F1.3  Measure pack current (Hall sensor + shunt, 1ms cycle)
│   └── F1.4  Measure insulation resistance (HV bus to chassis, 1s cycle)
│
├── F2: ESTIMATE
│   ├── F2.1  Estimate State of Charge (SOC) — EKF algorithm, 100ms update
│   ├── F2.2  Estimate State of Health (SOH) — after each full cycle
│   ├── F2.3  Estimate maximum discharge power (power capability, 100ms)
│   └── F2.4  Estimate remaining range (km) — based on SOC + consumption model
│
├── F3: PROTECT
│   ├── F3.1  Overcharge protection — Tier 1 HW (≤1ms) + Tier 2 SW (≤10ms)
│   ├── F3.2  Over-discharge protection — Tier 1 HW + Tier 2 SW
│   ├── F3.3  Overtemperature protection — rate-of-rise + absolute threshold
│   ├── F3.4  Overcurrent protection — short circuit detection
│   ├── F3.5  Ground fault / insulation failure detection
│   └── F3.6  Contactor welding detection (state feedback check)
│
├── F4: BALANCE
│   ├── F4.1  Detect cell voltage imbalance within module (>10mV spread)
│   └── F4.2  Activate passive balancing (bleed resistor per cell, 50mA)
│
├── F5: CONTROL
│   ├── F5.1  Control main contactors (main+, main-, pre-charge)
│   ├── F5.2  Control coolant pump speed (PWM, 0–100%)
│   ├── F5.3  Control chiller bypass valve (PWM, 0–100%)
│   └── F5.4  Calculate and send charge current limit to OBC/DCFC
│
└── F6: COMMUNICATE
    ├── F6.1  Transmit SOC, power limits, temperature, fault status to VCU (CAN-A)
    ├── F6.2  Transmit charge current limit and status to OBC/DCFC (CAN-B)
    ├── F6.3  Respond to OBD-II UDS diagnostic requests
    └── F6.4  Transmit telematics data (SOH, fault history) to telematics unit
```

### Function-to-Requirement Allocation

| Function | Sub-Functions | System Requirements Satisfied |
|---|---|---|
| F1: Monitor | F1.1–F1.4 | SR-F-01 (SOC), SR-F-06 (insulation), SR-S-01 (overcharge sensing), SR-S-03 (thermal) |
| F2: Estimate | F2.1–F2.4 | SR-F-01 (SOC ≤2%), SR-F-03 (SOH ≤5%), SR-C-01 (range to cluster) |
| F3: Protect | F3.1–F3.6 | SR-S-01, SR-S-02, SR-S-03, SR-S-04, SR-S-06, SR-P-01, SR-P-02 |
| F4: Balance | F4.1–F4.2 | SR-F-04 (cell balancing ≤10mV) |
| F5: Control | F5.1–F5.4 | SR-F-05 (contactor control), SR-S-04 (thermal control), SR-S-05 (DCFC derate) |
| F6: Communicate | F6.1–F6.4 | SR-C-01, SR-C-02, SR-C-03, SR-P-05 (CAN latency ≤5ms) |

---

## 4.3 Logical Architecture

### Master-Slave Processing Hierarchy

The BMS is organized into a **Master-Slave hierarchy** with one Master BMS Controller (MBMS) and four Cell Monitoring Controllers (CMC), one per battery module.

```
                    ┌─────────────────────────────────┐
                    │   MASTER BMS (MBMS)              │
                    │                                  │
                    │  ┌──────────┐  ┌──────────────┐ │
                    │  │ ASIL-D   │  │ ASIL-B / QM  │ │
                    │  │ Safety   │  │  Application │ │
                    │  │ Partition│  │  Partition   │ │
                    │  │(Core 0)  │  │  (Core 1)    │ │
                    │  └──────────┘  └──────────────┘ │
                    │         STM32H755 dual-core       │
                    └──────────┬──────────────────────┘
                               │  Isolated SPI (daisy-chain)
           ┌───────────────────┼──────────────────────────┐
           │                   │                          │
    ┌──────▼──────┐   ┌──────▼──────┐          ┌──────▼──────┐
    │  CMC IC #1  │   │  CMC IC #2  │    ...    │  CMC IC #4  │
    │  (Module 1) │   │  (Module 2) │           │  (Module 4) │
    │  TI BQ76940 │   │  TI BQ76940 │           │  TI BQ76940 │
    │  14-cell    │   │  14-cell    │           │  14-cell    │
    │  monitoring │   │  monitoring │           │  monitoring │
    └─────────────┘   └─────────────┘           └─────────────┘
    (56 cells/module: 14 series × 4 parallel strings per CMC)
```

### MBMS Responsibilities (Master Controller)

| Responsibility | ASIL Partition | Notes |
|---|---|---|
| SOC estimation (EKF algorithm) | ASIL-B | Non-safety function; output used in protection |
| SOH estimation | QM | Background calculation |
| Overcharge / over-discharge protection logic | **ASIL-D** | Core safety; implemented on Core 0 |
| Thermal runaway rate-of-rise detection | **ASIL-D** | Core safety; Core 0, independent of SOC |
| Thermal management PID control | ASIL-B | Coolant pump and chiller valve commands |
| Contactor control and state machine | ASIL-D | Safety-critical outputs; Core 0 |
| CAN communication (VCU, OBC, DCFC) | ASIL-B | SR-C-01, SR-C-02; Core 1 |
| UDS diagnostics | QM | Core 1 |
| Cell balancing arbitration | QM | Balancing commands to CMC ICs |

### CMC Responsibilities (Cell Monitoring Controllers — 4 per pack)

Each TI BQ76940 CMC IC monitors one battery module (7S8P = 56 cells):

| Responsibility | Description |
|---|---|
| Cell voltage measurement | 14-cell measurement per IC (7 series cells × 2 parallel strings per channel). Accuracy: ±1.5 mV |
| Cell temperature measurement | 4 NTC thermistor inputs per IC |
| Hardware overvoltage comparator | Tier-1 protection: hardware interrupt to MBMS if any cell >3.65V |
| Hardware undervoltage comparator | Tier-1 protection: hardware interrupt to MBMS if any cell <2.50V |
| Passive balancing drivers | Individual bleed resistor activation per cell |
| SPI communication to MBMS | Daisy-chain SPI, galvanically isolated from MBMS (HV isolation) |

### Software Architecture (AUTOSAR-Compliant Layering)

```
┌──────────────────────────────────────────────────────┐
│              APPLICATION SOFTWARE LAYER (ASW)         │
│  ┌────────────┐ ┌──────────┐ ┌──────────┐ ┌───────┐ │
│  │ SOC/SOH    │ │ Thermal  │ │  Fault   │ │ Comms │ │
│  │ Estimation │ │ Control  │ │ Mgmt     │ │ Mgmt  │ │
│  │ (ASIL-B)   │ │ (ASIL-B) │ │ (ASIL-D) │ │ (QM)  │ │
│  └────────────┘ └──────────┘ └──────────┘ └───────┘ │
├──────────────────────────────────────────────────────┤
│              RUNTIME ENVIRONMENT (RTE)                │
│  AUTOSAR RTE — inter-component communication,         │
│  memory partitioning, ASIL-D / ASIL-B separation      │
├──────────────────────────────────────────────────────┤
│              BASIC SOFTWARE LAYER (BSW)               │
│  ┌─────────┐ ┌─────────┐ ┌──────────┐ ┌──────────┐ │
│  │  OS     │ │  COM    │ │   Diag   │ │  Memory  │ │
│  │ FreeRTOS│ │ CAN     │ │   UDS    │ │  NVRAM   │ │
│  │ (ASIL-D │ │ Driver  │ │ (ISO     │ │  Driver  │ │
│  │ config) │ │         │ │ 14229)   │ │          │ │
│  └─────────┘ └─────────┘ └──────────┘ └──────────┘ │
├──────────────────────────────────────────────────────┤
│              HARDWARE ABSTRACTION LAYER (HAL)         │
│  STM32H755 HAL: ADC, SPI, CAN, PWM, GPIO, Watchdog   │
└──────────────────────────────────────────────────────┘
```

**Key ASIL partitioning principle:** ASIL-D code (Fault Management, Contactor Control) runs on Core 0 of the STM32H755. ASIL-B and QM code (SOC estimation, Communications) runs on Core 1. Memory Protection Unit (MPU) prevents Core 1 from writing to Core 0 memory space. This is the "freedom from interference" requirement of ISO 26262 Part 6.

### Redundancy Design

| Redundancy Element | Primary Path | Secondary Path | Rationale |
|---|---|---|---|
| Cell voltage sensing | CMC IC measurement (±1.5 mV) | MBMS plausibility check (sum of CMC voltages vs. string voltage from pack sensor) | SR-S-01 ASIL-D requires independent paths |
| VCU CAN communication | CAN-A (primary) | CAN-B (backup, secondary) | SR-C-01 ASIL-B; CAN-B carries minimal safety data |
| MCU operation | STM32H755 Core 0 (safety) | Hardware watchdog (independent of MCU — external IC) | ASIL-D requires hardware independence from SW |
| Pack current measurement | Hall-effect sensor (primary) | Shunt resistor + ADC (secondary, plausibility) | SR-F-01 accuracy depends on current measurement |

---

## 4.4 Physical Architecture

### Hardware Block Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                    HV BATTERY PACK (448 LFP cells)                   │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐           │
│  │ Module 1  │ │ Module 2  │ │ Module 3  │ │   ...     │           │
│  │ 7S8P      │ │ 7S8P      │ │ 7S8P      │ │ Module 8  │           │
│  │ CMC IC #1 │ │ CMC IC #2 │ │ CMC IC #3 │ │ CMC IC #4 │           │
│  │ BQ76940   │ │ BQ76940   │ │ BQ76940   │ │ BQ76940   │           │
│  └─────┬─────┘ └─────┬─────┘ └─────┬─────┘ └─────┬─────┘           │
│        └─────────────┴─────────────┴──────Isolated SPI──────────┐   │
│                                                                  │   │
│  Main(+) ──[Contactor A]──[Contactor B(Pre-charge+R)]──────────►│   │
│  Main(-)  ──[Contactor C]───────────────────────────────────────►│   │
│  Service Plug (Manual Disconnect) ──────────────────────────────►│   │
└─────────────────────────────────────────────────────────┬───────┘   │
                                                          │            │
                                     ┌────────────────────▼──────────┐ │
                                     │   MASTER BMS PCB              │ │
                                     │                               │ │
                                     │  [STM32H755ZIT6 Dual-Core]    │ │
                                     │   Core 0: ASIL-D functions    │ │
                                     │   Core 1: ASIL-B/QM functions │ │
                                     │                               │ │
                                     │  [TJA1042 CAN Transceiver ×2] │ │
                                     │  [MCP2562 CAN Transceiver]    │ │  (CAN-B backup)
                                     │  [LIN Transceiver (LIN 2.2A)] │ │
                                     │  [TCAN1042 Isolated SPI to CMC│ │
                                     │  [LEM HAB Current Sensor]     │ │  (Hall effect, primary)
                                     │  [0.5mΩ Shunt + ADC]          │ │  (secondary current)
                                     │  [SBC: UJA1167 System Basis   │ │  (watchdog, LIN, 5V)
                                     │   Chip — HW watchdog, 5V reg] │ │
                                     │  [Ethernet PHY (OTA future)]  │ │
                                     └─────────────────┬─────────────┘ │
                                                       │               │
                          ┌────────────────────────────▼────────────── ┤
                          │  Vehicle CAN Bus (CAN-A, 500 kbps)         │
                          │  VCU ◄──────────────────────────── BMS     │
                          │  OBC ◄──────────────────────────── BMS     │
                          │  Instrument Cluster ◄───────── BMS via VCU │
                          │  CAN-B (backup) ◄───────────────── BMS     │
                          └─────────────────────────────────────────────
```

### Component Selection Rationale

| Component | Part Number | Rationale for Selection |
|---|---|---|
| **Master MCU** | STM32H755ZIT6 (Dual-core: Cortex-M7 @ 480 MHz + Cortex-M4 @ 240 MHz) | ISO 26262 safety-certified MCU with hardware Memory Protection Unit (MPU). Dual-core enables ASIL-D / ASIL-B separation per Freedom from Interference requirement. Available from ST with long-term supply commitment. |
| **CMC IC** | TI BQ76940 (14-cell, ±1.5 mV accuracy) | Industry-standard BMS front-end IC. Built-in hardware overvoltage and undervoltage comparators enable Tier-1 protection without software. Supports passive balancing. Galvanically isolated SPI. AEC-Q100 automotive qualified. |
| **System Basis Chip** | NXP UJA1167 | Integrates 5V voltage regulator, hardware watchdog timer (timeout = 200ms), CAN transceiver, and LIN transceiver in single package. Watchdog is independent of MCU — trips contactor if MCU hangs. |
| **CAN Transceiver** | TI TCAN1042 ×2 (CAN-A and CAN-B) | AEC-Q100, ISO 11898-5 compliant, CAN FD capable. Selected for CAN-A (500 kbps safety messages) and CAN-B (backup). |
| **Current Sensor (Primary)** | LEM HAB 250-S Hall-effect sensor | ±250A range, ±0.5% accuracy, galvanic isolation (HV safe), response time <3μs. Suitable for pack current measurement up to 250A. |
| **Pack Topology** | 56S8P (448 cells) | 56 series cells × 3.2V nominal = 179.2V per string × 2 strings = 358V nominal (rounds to ~360V). With SOC window 15%–95%, operating range 325V–408V ≈ 400V nominal system. 8 modules, 7S8P per module, 56 cells per module. |

---

## 4.5 Interface Architecture

### Interface Control Document (ICD) — Excerpt

| IFC-ID | Interface | Signal / Parameter | Direction | Protocol | Range / Values | Update Rate | ASIL |
|---|---|---|---|---|---|---|---|
| IFC-01 | BMS ↔ VCU | SOC_Pct | BMS → VCU | CAN-A, ID 0x3B0 | 0–100% (0.5% resolution) | 100 ms | ASIL-B |
| IFC-02 | BMS ↔ VCU | MaxDischargePower_kW | BMS → VCU | CAN-A, ID 0x3B0 | 0–160 kW (0.5 kW resolution) | 100 ms | ASIL-B |
| IFC-03 | BMS ↔ VCU | MaxChargePower_kW | BMS → VCU | CAN-A, ID 0x3B0 | 0–160 kW | 100 ms | ASIL-B |
| IFC-04 | BMS ↔ VCU | CellTempMax_degC | BMS → VCU | CAN-A, ID 0x3B1 | -40 to +80°C (0.5°C resolution) | 100 ms | ASIL-B |
| IFC-05 | BMS ↔ VCU | FaultStatus_Bitmask | BMS → VCU | CAN-A, ID 0x3B2 | 16-bit bitmask (one bit per DTC category) | 100 ms (event-driven on fault) | ASIL-B |
| IFC-06 | VCU → BMS | IgnitionState | VCU → BMS | CAN-A, ID 0x100 | OFF/ACC/ON/CRANK | 100 ms | QM |
| IFC-07 | BMS ↔ OBC | ChargeCurrentLimit_A | BMS → OBC | CAN-B, ID 0x500 | 0–32A (0.1A resolution) | 100 ms | ASIL-B |
| IFC-08 | BMS ↔ DCFC | ChargeCurrentLimit_A | BMS → DCFC | CCS Combo 2, CAN | 0–375A (1A resolution) | 100 ms | ASIL-B |
| IFC-09 | BMS → Thermal | CoolantPumpSpeed_Pct | BMS → Pump | PWM, 0–100% duty cycle | 0–100% (1% resolution) | 200 ms | ASIL-B |
| IFC-10 | BMS → Thermal | ChillerValve_Pct | BMS → Valve | PWM, 0–100% duty cycle | 0–100% (open = 100%) | 200 ms | ASIL-B |
| IFC-11 | BMS ↔ CMC | CellVoltages[0..13] | CMC → MBMS | Isolated SPI, 1 MHz | 0–5000 mV (1 mV resolution) | 10 ms | ASIL-D |
| IFC-12 | BMS ↔ CMC | HW_OV_Interrupt | CMC → MBMS | GPIO interrupt line | ACTIVE/INACTIVE | Event-driven (<1ms) | ASIL-D |
| IFC-13 | BMS ↔ Service Tool | UDS Read/Write | Bidirectional | ISO 14229 over OBD-II | Per UDS specification | On-demand | QM |

---

## 4.6 Architecture-to-Requirements Traceability

| Architecture Element | Requirements Satisfied (SR-IDs) | ASIL Supported |
|---|---|---|
| CMC IC BQ76940 (hardware OV comparator) | SR-S-01 (overcharge Tier-1), SR-P-01 (≤1ms) | ASIL-D |
| MBMS Core 0 — ASIL-D SW partition | SR-S-01, SR-S-02, SR-S-03 (all overcharge/thermal Tier-2) | ASIL-D |
| MBMS Core 1 — ASIL-B SW partition | SR-F-01 (SOC), SR-C-01 (CAN), SR-P-05 (CAN latency) | ASIL-B |
| STM32H755 MPU (memory protection) | ISO 26262 Part 6 — freedom from interference | ASIL-D |
| UJA1167 System Basis Chip (HW watchdog) | SR-S-03 (thermal runaway — watchdog triggers contactor open if MCU hangs) | ASIL-D |
| Hall-effect current sensor + shunt (dual) | SR-F-01 (SOC accuracy — current measurement accuracy), SR-S-01 (secondary plausibility) | ASIL-B |
| CAN-A transceiver (primary) | SR-C-01, SR-P-05 | ASIL-B |
| CAN-B transceiver (backup) | SR-S-07 (CAN dropout safe state) | QM |
| IP67 enclosure | SR-E-02 | QM |
| Isolated SPI to CMC ICs | SR-S-01 (HV isolation — prevents HV from damaging MBMS) | ASIL-D |
| Contactor drivers + feedback GPIO | SR-F-05, SR-S-06 (welding detection) | ASIL-D |

---

## 4.7 MBSE Perspective

In a full MBSE implementation using Cameo Systems Modeler or IBM Rhapsody with SysML:

| Architecture View (This Chapter) | SysML Diagram Type | What It Captures |
|---|---|---|
| **Functional Architecture (§4.2)** | Activity Diagram | Actions (functions), flows (data/energy), decision nodes (fault conditions) |
| **Logical Architecture (§4.3)** | Internal Block Diagram (IBD) | Block instances, ports, connectors showing information flow between MBMS and CMC |
| **Physical Architecture (§4.4)** | Block Definition Diagram (BDD) | Block hierarchy (BMS System → MBMS PCB → STM32H755; BMS System → CMC IC ×4) with properties (voltage, current rating) |
| **Interface Architecture (§4.5)** | IBD with interface blocks | Ports typed by interface blocks; each port has protocol, direction, data type |
| **ASIL Partitioning** | Parametric Diagram | Constraint blocks encoding ISO 26262 ASIL decomposition rules |
| **Fault State Machine** | State Machine Diagram | States: INIT, NORMAL, FAULT_WARNING, FAULT_CRITICAL, SHUTDOWN; transitions triggered by fault events |

**Why MBSE would add value for the IM-e1 BMS:**

1. **Automatic traceability:** SysML model maintains the RTM in §3.6 automatically — any architecture change highlights which requirements are affected
2. **Impact analysis:** Changing CMC IC from BQ76940 to BQ7694003 → MBSE tool shows all affected interfaces and requirements
3. **Simulation:** Early-phase digital twin validates thermal architecture before hardware build (saves 4–6 months)
4. **Handoff to subsystem suppliers:** CMC IC supplier receives SysML interface block defining exact SPI protocol — no ambiguity

The IM-e1 BMS is complex enough (448 cells, 4 CMC ICs, 13+ external interfaces) that MBSE tooling would be justified. However, IndraMotors chose traditional documentation for the first program and will evaluate MBSE for IM-e2.

---

## 4.8 SE Process Reflection

### How Architecture Satisfies ASIL-D Requirements (Chapter 3 HARA)

The HARA in Chapter 3 produced two ASIL-D safety goals: prevent overcharge (SG-01) and prevent overtemperature (SG-03). The architecture satisfies these through **defense in depth**:

- **Tier 1 (hardware, ≤1ms):** CMC IC BQ76940 hardware comparator fires GPIO interrupt to MBMS → MBMS Core 0 opens contactor via hardware driver. This path is entirely independent of software.
- **Tier 2 (ASIL-D software, ≤10ms):** MBMS Core 0 reads cell voltages from CMC IC at 10ms cycle → if any voltage > threshold → command contactor open via software
- **Tier 3 (vehicle, ≤100ms):** VCU receives fault CAN message from BMS → VCU implements vehicle-level safe state

Three independent layers means a single point of failure cannot defeat the protection. This is exactly what was **missing from MCAS** — a single erroneous AOA sensor could override all pilot inputs with no independent check.

### Trade-offs That Remain Open (Bridge to Chapter 5)

The architecture defines the BMS structure, but two critical decisions are still open:

1. **Cell chemistry selection:** The pack topology (56S8P) is defined, but which cell chemistry fills it — NMC 811, LFP, or NCA? This affects energy density (does 56S8P give us 40 kWh?), thermal stability, and SOC algorithm design.

2. **Thermal management architecture:** The coolant pump and chiller valve are specified as outputs, but the actual thermal architecture — air cooling, indirect liquid cooling, or refrigerant cooling — has not been decided.

Both decisions are made through systematic trade studies in Chapter 5.

### CONOPS-to-Architecture Flow (Session 5)

Session 5 taught that architecture must be driven by the operational concept. Tracing back:

- **CONOPS Scenario 3 (DCFC at 150 kW)** → Required BMS to communicate with DCFC charger at ≤100ms cycle time → IFC-08 (CAN to DCFC, 100ms update rate)
- **CONOPS Scenario 5 (45°C parked)** → Required thermal monitoring in sleep mode → F1.2 (temperature monitoring, low-power wake mode) + MBMS sleep current specification (<5mA)
- **CONOPS Scenario 6 (cold start -5°C)** → Required cold-start power limiting → F5.4 (charge current limit calculation) + SR-P-03

Every IFC in §4.5 can be traced back to a CONOPS scenario and a stakeholder need. That is the correct CONOPS-to-architecture flow.

---

*Next: [Chapter 5 — Trade Studies](05-trade-studies.md)*
