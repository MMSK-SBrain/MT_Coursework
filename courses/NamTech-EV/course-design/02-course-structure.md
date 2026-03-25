# NamTech EV Lab Course - Learning Outcomes Structure

**Course Code:** NEVLAB (NamTech EV Lab)
**Course Type:** Practical Laboratory Course
**Target:** UG/PG Engineering Students

---

## COURSE OUTCOMES (COs)

By the end of this laboratory course, students will be able to:

### CO-1: Battery Pack Systems Engineering
Design, assemble, and test lithium-ion battery pack systems with integrated Battery Management Systems (BMS) for electric vehicle applications, ensuring safe operation and optimal performance.

### CO-2: Motor Control and Drivetrain Analysis
Configure, test, and optimize electric motor control systems (PMSM/BLDC) and analyze drivetrain performance characteristics including efficiency, torque-speed behavior, and regenerative braking.

### CO-3: EV Charging Infrastructure and Grid Integration
Analyze electric vehicle charging protocols (CCS2, ISO 15118), simulate charging scenarios, and evaluate grid impact and smart charging strategies.

### CO-4: Vehicle Control System Development
Develop, program, and validate vehicle control unit (VCU) algorithms for electric and hybrid vehicles using industry-standard microcontrollers and development platforms.

### CO-5: Complete EV System Integration and Troubleshooting
Integrate complete electric vehicle systems from component-level to vehicle-level, perform diagnostic analysis, and troubleshoot complex powertrain issues.

---

## MODULE STRUCTURE

### MODULE 1: Battery Systems

**Module Outcomes:**

**MO-1-1:** Assemble and test lithium-ion battery packs with proper series/parallel configurations, spot welding techniques, and safety protocols for EV applications.

**MO-1-2:** Configure and program Battery Management Systems (BMS) with CAN communication, implement cell balancing algorithms, and analyze state-of-charge (SoC) and state-of-health (SoH) monitoring.

**MO-1-3:** Conduct comprehensive battery pack testing including charge-discharge cycling, capacity measurement, protection verification, and aging analysis using automated test benches.

**Experiments/Sessions:**

**Lab 1.1: Battery Pack Assembly Fundamentals**
- SO-1-1-1: Identify and select appropriate lithium-ion cells based on voltage, capacity, and C-rating specifications
- SO-1-1-2: Assemble battery cells in series and parallel configurations to achieve target voltage and capacity
- SO-1-1-3: Perform spot welding operations safely to create battery interconnections
- SO-1-1-4: Install cell holders, insulation materials, and safety enclosures following industry standards

**Lab 1.2: BMS Integration and Testing**
- SO-1-2-1: Connect and configure Smart BMS with battery pack terminals and sense wires
- SO-1-2-2: Test over-voltage, under-voltage, over-current, and temperature protection features
- SO-1-2-3: Measure internal resistance of individual cells using IR tester
- SO-1-2-4: Verify cell balancing functionality under load conditions

**Lab 1.3: BMS Programming and CAN Communication**
- SO-1-3-1: Program BMS parameters including voltage limits, current thresholds, and temperature ranges
- SO-1-3-2: Configure CAN communication interface and analyze CAN messages using protocol analyzer
- SO-1-3-3: Implement data logging for battery pack parameters (voltage, current, temperature, SoC)
- SO-1-3-4: Monitor and interpret real-time battery pack data via WiFi/USB interface

**Lab 1.4: Battery Pack Load Testing**
- SO-1-4-1: Apply controlled resistive loads using bulb-based load system
- SO-1-4-2: Measure voltage sag and current delivery under various load conditions
- SO-1-4-3: Analyze thermal behavior and activate cooling/heating controls
- SO-1-4-4: Verify BMS protection activation under fault conditions

**Lab 1.5: Charge-Discharge Cycle Testing**
- SO-1-5-1: Set up battery pack on charge-discharge test bench (12V-84V range)
- SO-1-5-2: Configure constant current (CC) and constant voltage (CV) charging profiles
- SO-1-5-3: Conduct multiple charge-discharge cycles (up to 16 cycles) and record capacity data
- SO-1-5-4: Analyze battery aging characteristics and capacity fade over cycling

**Lab 1.6: Battery Pack Capacity and Protection Analysis**
- SO-1-6-1: Measure actual battery pack capacity and compare with rated capacity
- SO-1-6-2: Verify charge protection voltage and discharge protection voltage settings
- SO-1-6-3: Generate charge-discharge curves and analyze efficiency
- SO-1-6-4: Export test data for analysis and generate performance reports

---

### MODULE 2: Motor & Drivetrain Systems

**Module Outcomes:**

**MO-2-1:** Test and characterize PMSM and BLDC motors using hydraulic dynamometer, analyze torque-speed characteristics, and evaluate motor efficiency across operating ranges.

**MO-2-2:** Implement and optimize motor control algorithms including Field-Oriented Control (FOC) using MATLAB/Simulink and open-source motor controllers.

**MO-2-3:** Analyze complete EV drivetrain performance under MIDC driving cycles, evaluate regenerative braking efficiency, and optimize energy recovery systems.

**Experiments/Sessions:**

**Lab 2.1: Motor Mounting and Mechanical Setup**
- SO-2-1-1: Mount PMSM and BLDC motors on sliding bed dynamometer setup
- SO-2-1-2: Align motor shaft with dynamometer coupling using precision alignment tools
- SO-2-1-3: Install torque sensor and RPM encoder/hall sensors
- SO-2-1-4: Verify mechanical installation safety and vibration isolation

**Lab 2.2: Motor Controller Configuration**
- SO-2-2-1: Connect open motor controller (48V) to PMSM and BLDC motors
- SO-2-2-2: Configure motor parameters (pole pairs, voltage, current limits)
- SO-2-2-3: Verify hall sensor and temperature sensor connections
- SO-2-2-4: Test basic motor operation in open-loop mode

**Lab 2.3: Motor Performance Testing with Hydraulic Dyno**
- SO-2-3-1: Operate hydraulic dynamometer with automatic electronic loading
- SO-2-3-2: Conduct no-load and full-load motor tests
- SO-2-3-3: Generate torque-speed characteristic curves for PMSM and BLDC motors
- SO-2-3-4: Measure motor efficiency at different operating points

**Lab 2.4: CAN Communication and Data Logging**
- SO-2-4-1: Configure CAN communication between motor controller, dyno controller, and BMS
- SO-2-4-2: Monitor real-time motor parameters (voltage, current, RPM, torque, temperature)
- SO-2-4-3: Synchronize data from MIDC controller and Dyno data logger
- SO-2-4-4: Analyze logged data for performance optimization

**Lab 2.5: Field-Oriented Control (FOC) Implementation**
- SO-2-5-1: Understand FOC algorithm principles and block diagrams
- SO-2-5-2: Implement basic FOC algorithm using MATLAB/Simulink
- SO-2-5-3: Deploy FOC code to open motor controller
- SO-2-5-4: Compare FOC performance with six-step commutation

**Lab 2.6: Motor Control Tuning and Optimization**
- SO-2-6-1: Tune speed loop and torque loop PID parameters
- SO-2-6-2: Optimize motor response time and stability
- SO-2-6-3: Analyze motor thermal behavior under continuous load
- SO-2-6-4: Map motor efficiency across speed and torque ranges

**Lab 2.7: 4-Wheeler Drivetrain Integration**
- SO-2-7-1: Identify components of complete 4-wheeler powertrain (motor, differential, transmission, drive shafts)
- SO-2-7-2: Integrate 2 kW PMSM motor with drivetrain assembly
- SO-2-7-3: Connect regenerative braking system with energy feedback loop
- SO-2-7-4: Verify mechanical and electrical connections for safety

**Lab 2.8: MIDC Driving Cycle Simulation**
- SO-2-8-1: Configure MIDC (Modified Indian Driving Cycle) speed profile in controller
- SO-2-8-2: Execute MIDC cycle on drivetrain test rig
- SO-2-8-3: Monitor speed, torque, voltage, current, and temperature during cycle
- SO-2-8-4: Analyze energy consumption and performance metrics

**Lab 2.9: Regenerative Braking Analysis**
- SO-2-9-1: Configure regenerative braking parameters (intensity, activation threshold)
- SO-2-9-2: Measure energy recovery during braking events
- SO-2-9-3: Calculate regenerative braking efficiency
- SO-2-9-4: Optimize energy feedback to battery and load bank

**Lab 2.10: Drivetrain Fault Diagnosis**
- SO-2-10-1: Inject common faults (sensor failure, overvoltage, undervoltage, overtemperature)
- SO-2-10-2: Identify fault symptoms and system responses
- SO-2-10-3: Use diagnostic tools to troubleshoot issues
- SO-2-10-4: Implement fault protection and recovery strategies

---

### MODULE 3: Charging Infrastructure

**Module Outcomes:**

**MO-3-1:** Analyze CCS (Combined Charging System) and ISO 15118 communication protocols, simulate charging message sequences, and validate protocol compliance.

**MO-3-2:** Evaluate grid integration impacts of EV charging, perform load flow analysis, and design smart charging strategies for grid optimization.

**Experiments/Sessions:**

**Lab 3.1: CCS2 Charging Protocol Fundamentals**
- SO-3-1-1: Identify CCS2 connector pinout and communication architecture
- SO-3-1-2: Understand ISO 15118 protocol layers and message structure
- SO-3-1-3: Analyze complete charging session message sequence (from plug-in to charge completion)
- SO-3-1-4: Compare regional charging standards (CCS, CHAdeMO, GB/T)

**Lab 3.2: Charging Message Exchange Simulation**
- SO-3-2-1: Configure charging protocol simulator for CCS2 mode
- SO-3-2-2: Simulate vehicle-to-charger handshake and authentication
- SO-3-2-3: Analyze message timing with microsecond-level accuracy
- SO-3-2-4: Verify protocol compliance and timing requirements

**Lab 3.3: Charging Protocol Error Handling**
- SO-3-3-1: Inject systematic protocol errors (timeout, invalid message, sequence error)
- SO-3-3-2: Observe system error handling and recovery mechanisms
- SO-3-3-3: Analyze error codes and diagnostic messages
- SO-3-3-4: Validate safety fallback procedures

**Lab 3.4: TLS Security and Certificate Management**
- SO-3-4-1: Configure TLS encryption for secure charging communication
- SO-3-4-2: Manage digital certificates for vehicle and charging station
- SO-3-4-3: Test authentication and authorization processes
- SO-3-4-4: Analyze security vulnerabilities and mitigation strategies

**Lab 3.5: Grid Load Flow Analysis**
- SO-3-5-1: Model electrical distribution network using power flow solver
- SO-3-5-2: Simulate multiple simultaneous EV charging sessions
- SO-3-5-3: Perform load flow analysis using Newton-Raphson solver
- SO-3-5-4: Analyze voltage drop and line losses under EV charging load

**Lab 3.6: Voltage Regulation and Harmonic Analysis**
- SO-3-6-1: Model automatic voltage regulator (AVR) and load tap changer (LTC)
- SO-3-6-2: Measure total harmonic distortion (THD) during charging
- SO-3-6-3: Design harmonic filters for power quality improvement
- SO-3-6-4: Evaluate impact of fast charging on grid voltage stability

**Lab 3.7: Protection Systems for Charging Infrastructure**
- SO-3-7-1: Configure overcurrent, undervoltage, and frequency protection relays
- SO-3-7-2: Test protection system responses to fault conditions
- SO-3-7-3: Coordinate protection settings for selective tripping
- SO-3-7-4: Analyze fault isolation and system recovery

**Lab 3.8: Smart Charging and Demand Response**
- SO-3-8-1: Implement time-of-use (TOU) pricing algorithms
- SO-3-8-2: Optimize charging schedules to minimize demand charges
- SO-3-8-3: Simulate demand response scenarios for grid balancing
- SO-3-8-4: Analyze economic benefits of smart charging strategies

**Lab 3.9: Renewable Energy Integration**
- SO-3-9-1: Model stochastic renewable generation (solar/wind) profiles
- SO-3-9-2: Integrate renewable energy sources with EV charging infrastructure
- SO-3-9-3: Optimize charging schedules based on renewable availability
- SO-3-9-4: Analyze carbon footprint reduction and energy cost savings

---

### MODULE 4: Vehicle Control Systems

**Module Outcomes:**

**MO-4-1:** Develop and deploy vehicle control unit (VCU) software using automotive-grade microcontrollers, MATLAB/Simulink, and industry-standard communication protocols.

**MO-4-2:** Design and validate vehicle control algorithms for electric and hybrid vehicles, including mode switching, energy management, and powertrain control strategies.

**MO-4-3:** Perform Hardware-in-the-Loop (HIL) testing for VCU validation and functional safety verification.

**Experiments/Sessions:**

**Lab 4.1: VCU Hardware Architecture**
- SO-4-1-1: Identify NXP automotive-grade microcontroller components and peripherals
- SO-4-1-2: Understand ASIL-rated platform architecture for safety-critical applications
- SO-4-1-3: Explore base software stack (drivers, middleware, RTOS)
- SO-4-1-4: Configure development environment and toolchain

**Lab 4.2: VCU Communication Interfaces**
- SO-4-2-1: Configure CAN communication interface (2 channels)
- SO-4-2-2: Set up UART communication for debugging and data logging
- SO-4-2-3: Configure SPI interface for sensor communication
- SO-4-2-4: Test multi-protocol communication and message routing

**Lab 4.3: VCU Programming with Embedded C**
- SO-4-3-1: Write basic VCU application in Embedded C
- SO-4-3-2: Implement GPIO control for digital inputs/outputs
- SO-4-3-3: Read analog sensors and process sensor data
- SO-4-3-4: Develop interrupt service routines for real-time events

**Lab 4.4: Model-Based Design with MATLAB/Simulink**
- SO-4-4-1: Create vehicle control algorithm models in Simulink
- SO-4-4-2: Simulate VCU logic and verify functionality offline
- SO-4-4-3: Generate auto-code from Simulink models
- SO-4-4-4: Deploy generated code to VCU hardware

**Lab 4.5: Automotive Lighting Control Application**
- SO-4-5-1: Design interior lighting control logic using HIL setup
- SO-4-5-2: Implement PWM-based dimming control
- SO-4-5-3: Develop state machine for lighting modes
- SO-4-5-4: Test and validate lighting control functionality

**Lab 4.6: VCU Algorithm Development**
- SO-4-6-1: Develop torque request algorithm based on accelerator pedal input
- SO-4-6-2: Implement brake control logic with regenerative braking coordination
- SO-4-6-3: Design battery protection and power limiting algorithms
- SO-4-6-4: Develop vehicle state monitoring and error handling

**Lab 4.7: Hardware-in-the-Loop (HIL) Testing**
- SO-4-7-1: Set up Mini HIL environment with VCU and simulated vehicle components
- SO-4-7-2: Create test scenarios for VCU validation
- SO-4-7-3: Execute automated HIL test cases
- SO-4-7-4: Analyze test results and debug failures

**Lab 4.8: Functional Safety Concepts**
- SO-4-8-1: Understand automotive functional safety standards (ISO 26262 basics)
- SO-4-8-2: Implement software safety mechanisms (watchdog, redundancy, diagnostics)
- SO-4-8-3: Validate safety functions using HIL testing
- SO-4-8-4: Document safety analysis and test reports

**Lab 4.9: Hybrid Vehicle Control Strategy**
- SO-4-9-1: Analyze hybrid powertrain architecture (Honda Activa 5G platform)
- SO-4-9-2: Understand speed-based mode switching logic (20 km/h threshold)
- SO-4-9-3: Identify hall-sensor wheel speed detection system
- SO-4-9-4: Study IC engine start/stop control mechanisms

**Lab 4.10: Hybrid Mode Switching Testing**
- SO-4-10-1: Test EV mode operation (0-20 km/h, motor-only propulsion)
- SO-4-10-2: Observe automatic IC engine start at 20 km/h threshold
- SO-4-10-3: Analyze engine cut-off and EV mode resumption below 20 km/h
- SO-4-10-4: Measure hysteresis buffer for stable mode switching

**Lab 4.11: Hybrid Powertrain Energy Management**
- SO-4-11-1: Monitor power flow between IC engine and EV motor
- SO-4-11-2: Measure motor torque, current, and battery response in different modes
- SO-4-11-3: Evaluate regenerative braking efficiency in hybrid configuration
- SO-4-11-4: Compare energy consumption in EV mode vs IC mode

**Lab 4.12: Torque Transfer and Transition Analysis**
- SO-4-12-1: Analyze smooth torque transfer during mode changeover
- SO-4-12-2: Measure torque ripple and drivability metrics
- SO-4-12-3: Optimize transition logic for passenger comfort
- SO-4-12-4: Test edge cases (rapid acceleration, deceleration during switching)

---

### MODULE 5: Complete Vehicle Integration

**Module Outcomes:**

**MO-5-1:** Perform complete assembly and disassembly of electric 2-wheeler vehicles, identify all major components, and execute proper torque specifications and safety procedures.

**MO-5-2:** Integrate and calibrate complete EV powertrain systems including PMSM motor, open-source controller, BMS, and battery pack for research-grade electric vehicles.

**MO-5-3:** Conduct comprehensive vehicle-level testing, diagnostics, and troubleshooting for complete electric vehicle systems.

**Experiments/Sessions:**

**Lab 5.1: Electric 2-Wheeler Component Identification**
- SO-5-1-1: Identify all major components of electric 2-wheeler (frame, motor, battery, controller, throttle, wiring harness, lights)
- SO-5-1-2: Understand BLDC hub motor (1 kW) construction and operation
- SO-5-1-3: Analyze 48V lead-acid battery configuration and specifications
- SO-5-1-4: Study wiring harness layout and connector types

**Lab 5.2: Workshop Safety and Tool Usage**
- SO-5-2-1: Demonstrate proper use of personal protective equipment (PPE)
- SO-5-2-2: Operate pneumatic impact gun and air gun safely
- SO-5-2-3: Use torque wrenches with correct specifications
- SO-5-2-4: Handle insulated tools for electrical work on high-voltage systems

**Lab 5.3: Electric 2-Wheeler Disassembly**
- SO-5-3-1: Disconnect battery and ensure electrical safety lockout
- SO-5-3-2: Remove body panels, seat, and plastic covers
- SO-5-3-3: Disconnect wiring harness connectors systematically
- SO-5-3-4: Remove motor, controller, battery, and other major components

**Lab 5.4: Electric 2-Wheeler Assembly**
- SO-5-4-1: Mount battery pack and secure mounting brackets
- SO-5-4-2: Install hub motor and tighten axle nut to specified torque
- SO-5-4-3: Mount controller and ensure proper cooling airflow
- SO-5-4-4: Connect wiring harness following wiring diagram

**Lab 5.5: Electrical System Installation and Testing**
- SO-5-5-1: Install throttle, on/off switch, and key switch
- SO-5-5-2: Connect lighting system (headlight, tail light, indicators)
- SO-5-5-3: Verify Bluetooth module connectivity
- SO-5-5-4: Test all electrical systems before powering on

**Lab 5.6: 2-Wheeler Functional Testing and Diagnostics**
- SO-5-6-1: Perform pre-ride safety checks
- SO-5-6-2: Test motor operation, throttle response, and braking
- SO-5-6-3: Use multimeter to diagnose electrical issues
- SO-5-6-4: Troubleshoot common faults (no power, motor not running, lights malfunction)

**Lab 5.7: Hydraulic Lift and Maintenance Procedures**
- SO-5-7-1: Operate motorized hydraulic scissor lift safely (600-1100 mm height)
- SO-5-7-2: Position vehicle correctly on lift platform
- SO-5-7-3: Perform maintenance tasks at working height
- SO-5-7-4: Practice emergency stop and lowering procedures

**Lab 5.8: Research EV Platform Overview**
- SO-5-8-1: Understand open-source motor controller architecture with Simulink support
- SO-5-8-2: Identify PMSM motor specifications (19 kW rated / 29.5 kW peak @ 2500 rpm)
- SO-5-8-3: Analyze LiFePO4 battery system (12.8 kWh, 24 cells, 185Ah, 22V)
- SO-5-8-4: Study NXP MCX N94x/54x microcontroller (Arm Cortex-M7 core)

**Lab 5.9: FOC Algorithm Implementation for Research EV**
- SO-5-9-1: Review Field-Oriented Control (FOC) theory for PMSM motors
- SO-5-9-2: Develop FOC algorithm using MATLAB/Simulink
- SO-5-9-3: Deploy algorithm to open-source motor controller
- SO-5-9-4: Validate FOC performance on dynamometer and vehicle testing

**Lab 5.10: BMS and Motor Controller Integration**
- SO-5-10-1: Configure CAN 2.0B / CAN FD communication between BMS and motor controller
- SO-5-10-2: Implement battery state-of-charge (SoC) and state-of-health (SoH) monitoring
- SO-5-10-3: Configure active and passive cell balancing
- SO-5-10-4: Test fault isolation and protection features

**Lab 5.11: Vehicle Power Electronics and Protection**
- SO-5-11-1: Configure input voltage range (90-240V AC / 110-390V DC)
- SO-5-11-2: Set up PWM frequency (≥10 kHz) for motor control
- SO-5-11-3: Implement protection features (overvoltage, overcurrent, undervoltage, overtemperature, short-circuit)
- SO-5-11-4: Test protection activation and system shutdown

**Lab 5.12: Battery Charging Control and Efficiency**
- SO-5-12-1: Configure CC-CV (constant current - constant voltage) charging profile
- SO-5-12-2: Monitor charging efficiency (target ≥95%)
- SO-5-12-3: Implement charging termination logic
- SO-5-12-4: Test battery thermal management during charging

**Lab 5.13: Vehicle Display and HMI Development**
- SO-5-13-1: Configure 7" TFT/OLED display (800×480 px, ≥500 nits brightness)
- SO-5-13-2: Display real-time parameters (speed, SoC, power usage, drive mode)
- SO-5-13-3: Implement system warnings and fault indicators
- SO-5-13-4: Design user-friendly HMI interface

**Lab 5.14: Complete Powertrain Calibration**
- SO-5-14-1: Calibrate torque mapping for smooth acceleration
- SO-5-14-2: Optimize regenerative braking parameters
- SO-5-14-3: Tune power limiting based on battery SoC and temperature
- SO-5-14-4: Validate calibration through test drives

**Lab 5.15: Vehicle Performance Testing**
- SO-5-15-1: Conduct acceleration tests (0-60 km/h, 0-100 km/h)
- SO-5-15-2: Measure top speed and motor efficiency at various speeds
- SO-5-15-3: Perform range testing under different driving conditions
- SO-5-15-4: Analyze energy consumption (Wh/km) and efficiency metrics

**Lab 5.16: On-Road Validation and Troubleshooting**
- SO-5-16-1: Perform comprehensive pre-drive safety inspection
- SO-5-16-2: Conduct on-road testing in controlled environment
- SO-5-16-3: Monitor all vehicle parameters during real-world driving
- SO-5-16-4: Diagnose and resolve issues encountered during testing

**Lab 5.17: Environmental and Safety Testing**
- SO-5-17-1: Test vehicle operation across temperature range (-40°C to +85°C, simulated)
- SO-5-17-2: Verify IP65-IP67 enclosure rating for critical components
- SO-5-17-3: Conduct safety shutdown testing (emergency stop, fault conditions)
- SO-5-17-4: Validate functional safety requirements

---

## SUMMARY

**Total Course Outcomes (COs):** 5
**Total Module Outcomes (MOs):** 15
**Total Session Outcomes (SOs):** 68 hands-on experiments

**Modules:**
- Module 1: Battery Systems (6 labs)
- Module 2: Motor & Drivetrain Systems (10 labs)
- Module 3: Charging Infrastructure (9 labs)
- Module 4: Vehicle Control Systems (12 labs)
- Module 5: Complete Vehicle Integration (17 labs)

**Total Labs:** 54 hands-on laboratory sessions

All learning outcomes are experiment-based, action-oriented, and designed to prepare students for engineering careers in the EV industry.
