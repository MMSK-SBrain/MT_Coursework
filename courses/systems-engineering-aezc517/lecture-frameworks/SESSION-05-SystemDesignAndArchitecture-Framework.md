# Session 5: System Design and Architecture
## Instructor-Led Story Framework for PPT Preparation

**Duration:** 90 minutes lecture + 30 minutes Q&A
**Approach:** Design-Focused
**PPT Target:** 28-30 slides

---

## 🎯 Session Objectives (For Instructor)

By the end of this session, students will be able to:
- Explain the concept of operations (CONOPS) and its role in system design
- Define system context, boundaries, and external interfaces
- Apply high-level design principles to automotive system architecture
- Develop system architectures using structured approaches
- Compare and apply common architecture patterns and frameworks
- Understand design freeze, baselining, and configuration management
- Perform trade studies and alternatives analysis for architecture decisions

**Mapped Learning Outcomes:** LO2 (Develop requirements, architectures, specifications, verifications, and tests), LO4 (Apply systems engineering practices and methods in automotive systems)

---

## 📖 INSTRUCTOR-LED STORY ARC

### **SETUP: From Requirements to Architecture** (Slides 1-6, ~12 minutes)

#### Slide 1: Title
**Visual:** Professional title slide showing transformation from requirements (documents) to architecture (system diagram)
**Instructor Script:**
> "Welcome to Session 5: System Design and Architecture. Today marks a critical transition point in our systems engineering journey.
>
> In Session 4, we mastered requirements engineering - defining WHAT the system must do. Today, we answer the next question: HOW will we design the system to meet those requirements?
>
> This is where engineering creativity meets engineering discipline. This is where we architect solutions."

#### Slide 2: The Journey So Far - Connection to Previous Sessions
**Visual:** Visual timeline showing Sessions 1-4 leading to Session 5
**Instructor Script:**
> "Let's connect our journey:
>
> **Session 1**: We learned WHY systems engineering matters. Poor design decisions amplify requirements errors.
>
> **Session 2**: We learned the SE framework - ISO/IEC 15288 technical processes. After 'Requirements Definition' comes 'Architecture Definition.'
>
> **Session 3**: We explored MBSE. SysML has specific diagrams for architecture - Block Definition Diagrams, Internal Block Diagrams.
>
> **Session 4**: We defined requirements systematically. Now we must satisfy those requirements through architecture.
>
> **Today's critical link**: Requirements drive design. But design must not be embedded IN requirements. We separate WHAT (requirements) from HOW (architecture).
>
> This separation enables innovation, allows multiple solutions, and facilitates trade studies."

#### Slide 3: Requirements Drive Architecture
**Visual:** Flow diagram showing requirements → architecture → design → implementation
**Instructor Script:**
> "Architecture is the bridge between requirements and implementation.
>
> **The relationship:**
>
> **Requirements say WHAT:**
> - 'The vehicle shall detect obstacles within 150m with ±0.5m accuracy'
> - 'The system shall respond to driver inputs within 200ms'
> - 'The system shall operate in temperatures from -40°C to +85°C'
>
> **Architecture says HOW (conceptually):**
> - 'Use radar sensor subsystem for long-range detection, camera subsystem for classification'
> - 'Implement distributed architecture with sensor ECUs, fusion ECU, and actuation ECU'
> - 'Partition functions: sensing, perception, decision, control, actuation'
>
> **Design says HOW (specifically):**
> - 'Use 77 GHz FMCW radar with antenna array configuration...'
> - 'ECU network topology: star configuration with gateway...'
> - 'Algorithms: Kalman filter for sensor fusion, PID for control...'
>
> **Today we focus on ARCHITECTURE - the high-level structural decisions that shape the entire system.**
>
> Every major automotive system failure involves architecture decisions:
> - Toyota unintended acceleration? Throttle control architecture
> - Boeing 737 MAX MCAS? Sensor architecture and redundancy
> - Tesla Autopilot incidents? Sensor fusion architecture
>
> Architecture is where we make or break system success."

#### Slide 4: What IS System Architecture?
**Visual:** Definition box with supporting diagrams showing structure, behavior, interfaces
**Instructor Script:**
> "Let me give you the formal definition from INCOSE and ISO/IEC 42010:
>
> **System Architecture:**
> 'The fundamental organization of a system, embodied in its components, their relationships to each other and the environment, and the principles governing its design and evolution.'
>
> **Breaking this down:**
>
> **1. Fundamental organization** - High-level structure, not detailed design
>
> **2. Components** - Major subsystems, elements, modules
> - For vehicle: Powertrain, chassis, body, electrical, ADAS, infotainment
> - For ADAS: Sensors, perception, planning, control, actuation
>
> **3. Relationships** - How components interact
> - Interfaces: CAN bus, Ethernet, mechanical connections
> - Data flows: Sensor data → perception → decisions → commands
> - Dependencies: Control ECU depends on sensor data quality
>
> **4. Environment** - Context and boundaries
> - What's inside the system? What's outside?
> - External interfaces: Driver, road, regulations, other vehicles
>
> **5. Design principles** - Governing rules
> - Modularity, redundancy, fail-safe behavior, maintainability
> - 'All safety-critical functions shall have dual redundancy'
> - 'Sensing and actuation shall be physically separated'
>
> **Architecture exists at multiple levels:**
> - **Enterprise**: Entire vehicle architecture
> - **System**: ADAS architecture, powertrain architecture
> - **Subsystem**: Radar sensor architecture, brake system architecture
>
> Today we focus on SYSTEM-level architecture for automotive systems."

#### Slide 5: Architecture in the V-Model
**Visual:** V-Model with architecture definition highlighted on left side
**Instructor Script:**
> "Where does architecture fit in the systems engineering V-Model?
>
> **Left side (Design):**
> 1. **Stakeholder Requirements** (Session 4) - What stakeholders need
> 2. **System Requirements** (Session 4) - What system must do
> 3. **→ SYSTEM ARCHITECTURE ← (Today)** - How system is organized
> 4. Subsystem Requirements - Requirements allocated to subsystems
> 5. Detailed Design - Component-level implementation
>
> **Right side (Verification):**
> We verify architecture through integration testing - does the architecture work as designed?
>
> **Critical insight from V-Model:**
> Architecture decisions made TODAY determine:
> - Integration strategy (how we assemble the system)
> - Interface verification (how subsystems communicate)
> - System-level testing approach (how we verify behavior)
>
> **The architecture must be:**
> - **Traceable to requirements** - Every requirement allocated to architectural element
> - **Verifiable** - Can we build and test this architecture?
> - **Implementable** - Can subsystems be developed in parallel?
>
> Poor architecture = expensive integration problems downstream.
> Good architecture = smooth integration, modular testing, parallel development."

#### Slide 6: Learning Journey for Today
**Visual:** Roadmap with 6 key architectural steps
**Instructor Script:**
> "Today's journey through system architecture design:
>
> **Part 1: CONOPS - Concept of Operations**
> - Understanding how the system will be used
> - Operational scenarios and use cases
> - Setting the stage for architecture
>
> **Part 2: System Context and Boundaries**
> - Defining what's IN vs OUT
> - External interfaces and stakeholders
> - Environmental considerations
>
> **Part 3: Design Principles and Patterns**
> - Modularity, hierarchy, abstraction
> - Common automotive architecture patterns
> - Design for quality attributes (safety, reliability, maintainability)
>
> **Part 4: Architecture Development Process**
> - Functional decomposition
> - Allocation of requirements to subsystems
> - Interface definition
>
> **Part 5: Architecture Frameworks and Views**
> - Logical, physical, functional views
> - Using architecture frameworks (DODAF, Zachman, automotive-specific)
>
> **Part 6: Trade Studies and Configuration Management**
> - Evaluating alternatives
> - Design freeze and baseline
> - Managing architectural evolution
>
> Real-world example throughout: **Adaptive Cruise Control (ACC) architecture**"

---

### **TRIGGER: The Architecture Challenge** (Slides 7-8, ~5 minutes)

#### Slide 7: A Deceptively Complex System
**Visual:** Simple box labeled "Adaptive Cruise Control System" with question marks
**Instructor Script:**
> "Let's use Adaptive Cruise Control (ACC) as our running example. You might think:
>
> **Initial thought:** 'ACC maintains speed and keeps distance from lead vehicle. Just need a radar and throttle control. Simple!'
>
> **Reality check - What's involved in ACC architecture?**
>
> **Sensing layer:**
> - Long-range radar (150m detection)
> - Camera (lane detection, sign recognition)
> - Wheel speed sensors (own vehicle speed)
> - Yaw rate sensor (vehicle dynamics)
> - GPS (map context)
>
> **Processing layer:**
> - Sensor fusion (combine radar + camera data)
> - Object tracking (maintain continuity of detected vehicles)
> - Threat assessment (is lead vehicle decelerating?)
> - Path planning (longitudinal trajectory)
> - Control algorithms (speed and spacing control)
>
> **Actuation layer:**
> - Throttle control (acceleration requests to powertrain ECU)
> - Brake control (deceleration requests to brake ECU)
> - Transmission control (gear selection optimization)
>
> **Interface layer:**
> - Driver interface (buttons, displays, alerts)
> - Other vehicle systems (ESC, ABS, lane keeping, collision avoidance)
> - Diagnostic systems (fault detection and logging)
> - OTA update capability (software updates)
>
> **Suddenly, we have 10+ subsystems, 20+ interfaces, 50+ requirements to allocate!**
>
> **This is why we need systematic architecture development.**"

#### Slide 8: Architecture Decisions That Make or Break the System
**Visual:** Decision tree showing architectural choices
**Instructor Script:**
> "For ACC, we face critical architectural decisions:
>
> **Decision 1: Centralized vs Distributed Processing?**
> - **Centralized**: Single ACC ECU does all processing
>   - Pros: Simpler coordination, lower cost
>   - Cons: Single point of failure, higher processing requirements
> - **Distributed**: Sensor ECUs preprocess, ACC ECU fuses and decides
>   - Pros: Parallel processing, fault isolation
>   - Cons: More complex interfaces, synchronization challenges
>
> **Decision 2: Radar-only vs Multi-sensor Fusion?**
> - **Radar-only**: Simpler, proven technology
>   - Limitation: Can't classify objects (truck vs car vs motorcycle)
> - **Radar + Camera**: Better perception, object classification
>   - Complexity: Fusion algorithms, calibration, sensor failures
>
> **Decision 3: Integrated ECU vs Separate ACC ECU?**
> - **Integrated**: ACC functions in existing ADAS ECU
>   - Pros: Cost savings, packaging
>   - Cons: Coupled development, safety isolation challenges
> - **Separate**: Dedicated ACC ECU
>   - Pros: Independence, easier certification
>   - Cons: Higher cost, more ECUs
>
> **Decision 4: CAN bus vs Automotive Ethernet?**
> - **CAN**: Mature, widely deployed
>   - Limitation: 500 kbps bandwidth (tight for sensor data)
> - **Ethernet**: High bandwidth (100 Mbps+)
>   - Complexity: New protocol, cost, validation
>
> **Decision 5: Safety Architecture - ASIL Rating?**
> - What ASIL level? (ISO 26262: A, B, C, D)
> - Single channel vs dual redundancy?
> - Fail-safe vs fail-operational?
>
> **Each decision cascades through the entire architecture.**
>
> We need a systematic process to:
> - Explore alternatives
> - Evaluate trade-offs
> - Make justified decisions
> - Document rationale
>
> That's what we'll learn today."

---

### **RISING ACTION: Building System Architecture** (Slides 9-24, ~50 minutes)

#### **Part 1: Concept of Operations (CONOPS)** (Slides 9-11, ~10 minutes)

##### Slide 9: What is CONOPS?
**Visual:** CONOPS definition with example operational scenario visualization
**Instructor Script:**
> "Before we architect the system, we must understand HOW it will be used. This is the Concept of Operations (CONOPS).
>
> **CONOPS Definition:**
> 'A verbal and graphic statement, in user-oriented terminology, describing how a system will be operated, who will operate it, and under what conditions it will be used to achieve mission objectives.'
>
> **CONOPS answers critical questions:**
> - **Who** are the users? (Driver, passengers, service technicians, fleet managers)
> - **What** will they do with the system? (Engage ACC, set speed, monitor, disengage)
> - **When** will they use it? (Highway driving, traffic jams, long trips)
> - **Where** will it operate? (Geographic regions, road types, weather conditions)
> - **Why** do they need it? (Reduce fatigue, improve fuel economy, enhance safety)
> - **How** will they interact? (Steering wheel buttons, displays, voice commands)
>
> **CONOPS is NOT:**
> - ❌ Detailed design (not HOW the system works internally)
> - ❌ System requirements (not WHAT the system must do)
> - ❌ User manual (not step-by-step instructions)
>
> **CONOPS IS:**
> - ✓ Operational vision (HOW users will employ the system)
> - ✓ Context for architecture (shapes design decisions)
> - ✓ Communication tool (aligns stakeholders on operational concept)
>
> **In automotive:**
> - CONOPS developed early (concept phase)
> - Drives requirements (what capabilities enable operations?)
> - Shapes architecture (what structure supports operations?)
> - Guides testing (validate against operational scenarios)"

##### Slide 10: ACC CONOPS Example - Operational Scenarios
**Visual:** Illustrated operational scenarios with timeline
**Instructor Script:**
> "Let's develop CONOPS for our ACC system through operational scenarios.
>
> **Scenario 1: Highway Cruising (Normal Operation)**
>
> **Context:**
> - Driver: Experienced, highway driving, light traffic
> - Environment: Clear weather, dry road, daylight
> - Vehicle speed: 120 km/h
>
> **Operational sequence:**
> 1. Driver accelerates to desired speed (120 km/h)
> 2. Driver presses SET button on steering wheel
> 3. System activates ACC, displays status on cluster ('ACC Active, 120 km/h')
> 4. System maintains speed automatically
> 5. No lead vehicle ahead → system maintains set speed
> 6. Driver monitors traffic, keeps hands on wheel
> 7. Driver can adjust speed with +/- buttons (±1 km/h per press)
>
> **Expected system behavior:**
> - Smooth speed maintenance (±2 km/h tolerance)
> - Fuel-efficient throttle modulation
> - Display shows status continuously
>
> ---
>
> **Scenario 2: Following Vehicle (Adaptive Behavior)**
>
> **Context:**
> - ACC engaged at 120 km/h
> - Lead vehicle appears ahead, traveling at 100 km/h
> - Set following distance: 2.0 seconds time gap
>
> **Operational sequence:**
> 1. Radar detects lead vehicle at 100m distance
> 2. System assesses: 'Lead vehicle slower, closing speed 20 km/h'
> 3. System decelerates smoothly (gentle braking, 0.2g max)
> 4. System achieves 2.0 sec following distance (55m at 100 km/h)
> 5. System matches lead vehicle speed (100 km/h)
> 6. Display shows: 'ACC Active, Following, 100 km/h, Distance: 2.0s'
> 7. Driver can adjust following distance (1.0s, 1.5s, 2.0s, 2.5s settings)
>
> **Expected system behavior:**
> - Comfortable deceleration (not jerky)
> - Maintain safe following distance
> - Respond to lead vehicle speed changes
>
> ---
>
> **Scenario 3: Lead Vehicle Cuts In (Dynamic Response)**
>
> **Context:**
> - ACC following at 100 km/h, 2.0s gap
> - Vehicle from adjacent lane cuts in front suddenly
> - New lead vehicle now only 20m ahead (0.7s gap - too close!)
>
> **Operational sequence:**
> 1. Radar detects new target suddenly closer
> 2. System identifies: 'Critical - following distance below threshold'
> 3. System applies moderate braking (0.3g) immediately
> 4. Display alerts driver: 'Take Over' warning (visual + audible)
> 5. System increases following distance to 2.0s
> 6. If driver doesn't respond and gap keeps decreasing → system applies stronger braking
>
> **Expected system behavior:**
> - Rapid but safe response to cut-ins
> - Clear driver alerts
> - Maintain safety (don't cause rear-end collision)
>
> ---
>
> **Scenario 4: Driver Override and Deactivation**
>
> **Context:**
> - ACC engaged
> - Driver needs to take control
>
> **Deactivation triggers:**
> 1. **Driver presses brake pedal** → ACC disengages immediately, driver controls braking
> 2. **Driver presses CANCEL button** → ACC disengages, returns to manual throttle
> 3. **Driver presses accelerator >50%** → ACC suspends, driver controls speed temporarily
> 4. **System detects sensor failure** → ACC disengages, alerts driver ('ACC Unavailable')
> 5. **Vehicle speed drops below 30 km/h** → ACC disengages (designed for highway use)
>
> **Expected system behavior:**
> - Instant response to driver inputs (driver always has authority)
> - Clear status indication (driver knows ACC state)
> - Safe transitions (no sudden changes)
>
> **These scenarios drive architecture requirements:**
> - Need rapid sensor processing (detect cut-ins quickly)
> - Need smooth actuation (comfort during speed changes)
> - Need clear HMI (driver must understand system state)
> - Need fail-safe behavior (handle sensor failures)"

##### Slide 11: From CONOPS to Architecture Implications
**Visual:** Mapping from operational scenarios to architectural requirements
**Instructor Script:**
> "CONOPS directly shapes architecture. Let's trace the connections:
>
> **Operational Need → Architectural Implication**
>
> **1. 'Detect lead vehicle at 150m in all weather'**
> → Architecture must include:
> - Long-range sensing capability (77 GHz radar, not just camera)
> - Weather-robust sensor (radar works in fog/rain, camera doesn't)
> - Sensor positioning (front bumper, unobstructed field of view)
>
> **2. 'Respond to sudden cut-ins within 0.5 seconds'**
> → Architecture must include:
> - High-frequency sensor sampling (20+ Hz)
> - Low-latency processing (sensor → decision → actuation <500ms)
> - High-priority CAN messaging (ACC messages preempt lower priority)
> - Fast actuator response (electronic throttle, brake-by-wire)
>
> **3. 'Driver can override instantly by pressing brake'**
> → Architecture must include:
> - Brake pedal monitoring (direct input to ACC ECU or via CAN)
> - Preemptive arbitration (brake command overrides ACC commands)
> - Fail-safe logic (on any fault, release control to driver)
>
> **4. 'System operates in -40°C to +50°C ambient'**
> → Architecture must include:
> - Industrial-grade ECUs (automotive temperature range)
> - Sensor heating (radar lens heating, camera lens defogging)
> - Cold-start calibration (sensors may need warm-up time)
>
> **5. 'Maintain operation even if one sensor fails'**
> → Architecture must include:
> - Sensor redundancy (radar + camera, not single sensor)
> - Fault detection and isolation (FDI algorithms)
> - Degraded mode operation (fall back to reduced functionality)
>
> **6. 'Driver must understand system state at all times'**
> → Architecture must include:
> - Dedicated HMI subsystem (instrument cluster integration)
> - Multiple indication methods (visual icon, text, color, sound)
> - State machine visibility (engaged, standby, following, error)
>
> **CONOPS forces us to think OPERATIONALLY, not just FUNCTIONALLY.**
>
> Many architecture failures come from designing the system in isolation, ignoring how it's actually used."

---

#### **Part 2: System Context and Boundaries** (Slides 12-14, ~10 minutes)

##### Slide 12: Defining System Boundaries
**Visual:** Context diagram showing ACC system with boundaries and external interfaces
**Instructor Script:**
> "Critical architecture step: Define what's IN the system and what's OUT.
>
> **Why boundaries matter:**
> - **Scope control**: What are we responsible for designing?
> - **Interface identification**: What do we interface with but don't control?
> - **Responsibility allocation**: Where does our system end and others begin?
>
> **For ACC system, let's define boundaries:**
>
> **INSIDE the ACC System (Our Responsibility):**
> - ACC ECU (processing unit)
> - ACC software (algorithms, control logic)
> - Radar sensor (if dedicated to ACC)
> - ACC-specific HMI elements (dashboard icon, settings menu)
> - ACC wiring harness
>
> **OUTSIDE the ACC System (External Interfaces):**
> - **Driver**: User, operator
>   - Interface: Steering wheel buttons (input), instrument cluster (output)
> - **Powertrain ECU**: Controls engine/motor torque
>   - Interface: CAN messages (ACC sends torque requests)
> - **Brake ECU**: Controls brake actuation
>   - Interface: CAN messages (ACC sends deceleration requests)
> - **ESC (Electronic Stability Control)**: Vehicle dynamics control
>   - Interface: CAN messages (wheel speeds, yaw rate data)
> - **Transmission ECU**: Gear selection
>   - Interface: CAN messages (optimal gear for ACC operation)
> - **Instrument Cluster**: Driver displays
>   - Interface: CAN messages (status, warnings, icons)
> - **Body Control Module**: Vehicle state information
>   - Interface: CAN messages (door status, ignition state)
> - **Gateway ECU**: Network management
>   - Interface: CAN bus connection, network routing
> - **Diagnostic System**: Service and fault logging
>   - Interface: OBD-II / UDS protocols
> - **Infrastructure**: Road, traffic, weather
>   - Interface: Radar/camera perception (one-way, sensing only)
> - **Other Vehicles**: Lead vehicle, surrounding traffic
>   - Interface: Radar/camera perception (one-way, sensing only)
> - **Regulations**: FMVSS, Euro NCAP, UN R79
>   - Interface: Compliance requirements (constraints)
>
> **Boundary decisions drive:**
> - Development responsibility (who develops what?)
> - Integration testing (where are interface test points?)
> - Fault isolation (if something fails, whose problem is it?)
> - Cost allocation (budget and resources)
>
> **Common mistake**: Vague boundaries
> - Example: Is the camera 'inside' ACC or 'shared' with lane keeping?
>   - If shared: Need coordination, joint calibration, arbitration
>   - If dedicated: ACC team owns it fully
> - Decision impacts architecture significantly
>
> **SysML representation**: Context diagrams, Block Definition Diagrams (BDD) with boundary boxes"

##### Slide 13: External Interface Identification
**Visual:** Interface table/matrix showing all external connections
**Instructor Script:**
> "Once boundaries are clear, we catalog ALL external interfaces.
>
> **Interface Identification Matrix - ACC System:**
>
> | External Entity | Interface Type | Protocol/Physical | Data Flow | Criticality |
> |----------------|----------------|-------------------|-----------|-------------|
> | Driver | Human-Machine Interface | Steering wheel switches (resistive, 0-5V) | Bidirectional (commands in, status out) | High |
> | Powertrain ECU | Electronic | CAN 2.0B, 500 kbps | Bidirectional (torque request out, engine status in) | Critical |
> | Brake ECU | Electronic | CAN 2.0B, 500 kbps | Bidirectional (decel request out, brake status in) | Critical |
> | ESC ECU | Electronic | CAN 2.0B, 500 kbps | Input only (wheel speeds, yaw rate) | Critical |
> | Instrument Cluster | Electronic | CAN 2.0B, 500 kbps | Output only (status, warnings) | Medium |
> | Radar Sensor | Electronic | CAN FD, 2 Mbps (or Ethernet) | Input only (object list, targets) | Critical |
> | Camera Sensor | Electronic | Automotive Ethernet, 100 Mbps | Input only (video stream, lane data) | High |
> | Gateway ECU | Electronic | CAN 2.0B, 500 kbps | Bidirectional (diagnostics, updates) | Medium |
> | Road/Environment | Physical | Electromagnetic (radar, optical) | Input only (sensing) | N/A |
>
> **For each interface, specify:**
>
> **1. Interface Control Document (ICD) Required**
> - Physical layer: Connectors, pinouts, voltages, timing
> - Protocol layer: Message IDs, data formats, update rates
> - Behavioral layer: Sequence diagrams, state machines
> - Error handling: Fault detection, timeout behavior, defaults
>
> **Example - Powertrain Interface ICD:**
> ```
> Message: ACC_TorqueRequest
> CAN ID: 0x245
> DLC: 8 bytes
> Byte 0-1: Requested torque (Nm, scaled 0.1 Nm/bit, offset -500 Nm)
> Byte 2: Torque rate limit (Nm/s)
> Byte 3: Torque control mode (0=None, 1=Speed, 2=Torque)
> Byte 4-7: Reserved
> Update rate: 20 ms (50 Hz)
> Timeout: If no message for 100ms, powertrain reverts to driver control
> ```
>
> **2. Interface Verification Plan**
> - How will we test this interface?
> - Unit test (ECU bench), integration test (vehicle), validation
>
> **3. Interface Change Management**
> - Who can change interface definition?
> - Approval process (both sides must agree)
> - Version control
>
> **Architecture implication:**
> **Every interface is a RISK.**
> - Communication failures
> - Timing issues
> - Mismatched interpretations
>
> **Architecture principle:**
> **Minimize interfaces. Simplify interfaces. Document interfaces rigorously.**
>
> 80% of integration problems come from interface issues."

##### Slide 14: System Context Diagram
**Visual:** Full context diagram showing ACC and all external entities with interface flows
**Instructor Script:**
> "Let's visualize the complete system context.
>
> **ACC System Context Diagram:**
>
> [Visual shows ACC ECU in center, surrounded by external entities with labeled arrows]
>
> **Key elements:**
>
> **Center**: ACC System (boundary box)
>
> **External entities** (outside boundary):
> - Driver (top)
> - Road/Environment (bottom)
> - Vehicle systems ECUs (left and right)
> - Diagnostic/service (bottom right)
>
> **Interface flows** (arrows with labels):
> - Driver → ACC: Button presses (SET, RES, CANCEL, +/-), time gap selection
> - ACC → Driver: Status displays, warnings, alerts
> - Radar/Camera → ACC: Detected objects, distances, velocities
> - ACC → Powertrain: Torque requests, acceleration demands
> - ACC → Brake: Deceleration requests, braking intensity
> - ESC → ACC: Vehicle speed, yaw rate, wheel speeds
> - ACC ↔ Cluster: Status, mode, set speed, following distance
> - ACC ↔ Gateway: Diagnostics, fault codes, software updates
>
> **This diagram answers critical questions:**
> - What flows INTO our system? (Inputs we must handle)
> - What flows OUT? (Outputs we must generate)
> - What don't we control? (External dependencies)
>
> **Architecture decisions from context:**
> - **High sensor bandwidth** (radar/camera) → Need fast network (Ethernet or CAN FD)
> - **Critical safety interfaces** (brake, powertrain) → Need redundancy, fault detection
> - **Human interaction** (driver) → Need clear, unambiguous feedback
> - **Multiple ECU interfaces** → Need network architecture design
>
> **This context diagram becomes:**
> - Foundation for detailed architecture
> - Basis for interface testing
> - Communication tool with stakeholders
> - Input to trade studies (where to partition functionality?)
>
> **SysML equivalent**: BDD (Block Definition Diagram) with system context"

---

#### **Part 3: Design Principles and Architecture Patterns** (Slides 15-18, ~12 minutes)

##### Slide 15: High-Level Design Principles
**Visual:** Design principles pyramid showing foundational principles
**Instructor Script:**
> "Good architecture follows proven design principles. These are timeless guidelines that lead to robust systems.
>
> **Fundamental Design Principles for Automotive Systems:**
>
> **1. MODULARITY - Decompose into Cohesive Modules**
>
> **Definition**: System divided into independent, interchangeable modules with well-defined interfaces
>
> **Benefits**:
> - Parallel development (teams work independently)
> - Easier testing (test modules separately, then integrate)
> - Maintainability (replace/upgrade modules without touching others)
> - Reusability (use proven modules in multiple systems)
>
> **ACC Example**:
> - Sensing module (radar, camera)
> - Perception module (object detection, tracking)
> - Planning module (trajectory, spacing control)
> - Actuation module (throttle/brake commands)
> - HMI module (driver interface)
>
> Each module has defined inputs/outputs, can be developed separately.
>
> ---
>
> **2. HIERARCHY - Organize in Levels of Abstraction**
>
> **Definition**: System organized in layers, each level abstracts complexity of levels below
>
> **ACC Architecture Hierarchy**:
> - **Level 0**: Complete ACC system
> - **Level 1**: Subsystems (Sensing, Processing, Actuation, HMI)
> - **Level 2**: Components (Radar ECU, Fusion Algorithm, Brake Interface, Display Driver)
> - **Level 3**: Modules/Functions (Target Selection, Distance Control, PID Controller)
>
> **Benefits**:
> - Manage complexity (understand one level at a time)
> - Clear responsibility (each level has defined role)
> - Verification strategy (test bottom-up: components → subsystems → system)
>
> ---
>
> **3. ABSTRACTION - Hide Implementation Details**
>
> **Definition**: Interface defines WHAT, not HOW
>
> **Example**:
> - Bad: 'Radar ECU outputs raw ADC samples at 1 MHz'
> - Good: 'Sensor subsystem provides list of detected objects with position, velocity, confidence'
>
> Abstraction allows changing implementation without affecting users of the interface.
>
> ---
>
> **4. SEPARATION OF CONCERNS - Isolate Responsibilities**
>
> **Definition**: Different aspects handled by different elements
>
> **ACC Example**:
> - Sensing concerns: Separated into dedicated sensor ECUs
> - Safety concerns: Separated into monitoring function
> - Diagnostic concerns: Separated into diagnostic manager
>
> Don't mix safety-critical and non-critical in same module.
>
> ---
>
> **5. INFORMATION HIDING - Encapsulation**
>
> **Definition**: Internal details not visible to external users
>
> **Example**:
> - Other ECUs don't need to know ACC's internal state machine
> - They interact via defined CAN messages only
> - ACC can change internal algorithms without affecting others
>
> ---
>
> **6. INTERFACE STANDARDIZATION - Use Common Patterns**
>
> **Definition**: Reuse interface patterns across system
>
> **Example**:
> - All actuator commands use same CAN message structure
> - All status messages use same format
> - Reduces learning curve, testing burden
>
> ---
>
> **7. REDUNDANCY - Critical Functions Have Backups**
>
> **Definition**: Duplicate critical capabilities
>
> **ACC Safety Architecture**:
> - Dual sensors (radar + camera, independent failures)
> - Plausibility checking (cross-check sensor data)
> - Safe fallback (if sensors fail, disable gracefully)
>
> **Trade-off**: Redundancy adds cost and complexity but improves safety and availability.
>
> ---
>
> **8. FAIL-SAFE DESIGN - Fail to Safe State**
>
> **Definition**: On any fault, system transitions to safe configuration
>
> **ACC Fail-Safe**:
> - Sensor failure → Disable ACC, alert driver (don't guess)
> - Communication loss → Disable ACC (don't act on stale data)
> - ECU crash → Watchdog resets ECU, ACC stays off until next ignition cycle
>
> **Critical for automotive**: Never fail in a way that causes accident.
>
> These principles guide every architecture decision we make."

##### Slide 16: Common Architecture Patterns
**Visual:** Diagram showing 4 common patterns with automotive examples
**Instructor Script:**
> "Beyond principles, we use proven architecture patterns - recurring solutions to common problems.
>
> **Pattern 1: LAYERED ARCHITECTURE**
>
> **Structure**: System organized in horizontal layers, each layer uses services of layer below
>
> **Automotive Example - ADAS Architecture**:
> ```
> ┌─────────────────────────────────────────┐
> │  Layer 4: Application                    │  (ACC, LKA, AEB functions)
> ├─────────────────────────────────────────┤
> │  Layer 3: Planning & Decision            │  (Trajectory planning, arbitration)
> ├─────────────────────────────────────────┤
> │  Layer 2: Perception & Fusion            │  (Object detection, tracking, fusion)
> ├─────────────────────────────────────────┤
> │  Layer 1: Sensing & Actuation            │  (Radar, camera, throttle, brake)
> └─────────────────────────────────────────┘
> ```
>
> **Rules**:
> - Layer N can only call Layer N-1 (downward)
> - Layer N provides services to Layer N+1 (upward)
> - No skipping layers (Layer 4 can't directly access Layer 1)
>
> **Benefits**:
> - Clear separation of concerns
> - Easy to replace a layer (if interface maintained)
> - Testable (test layers independently)
>
> **Drawback**:
> - Can introduce latency (must pass through layers)
> - Rigid structure
>
> **When to use**: Complex systems with clear functional hierarchy
>
> ---
>
> **Pattern 2: PIPE-AND-FILTER (Data Flow Architecture)**
>
> **Structure**: Data flows through sequence of processing stages (filters), connected by data channels (pipes)
>
> **Automotive Example - Sensor Processing Pipeline**:
> ```
> Raw Radar  →  Filtering  →  Detection  →  Tracking  →  Fusion  →  Object List
>  Signals        (Filter)     (Filter)     (Filter)    (Filter)     (Output)
> ```
>
> **Benefits**:
> - Intuitive for data processing tasks
> - Easy to add/remove stages
> - Parallel processing (stages can run concurrently)
> - Reusable filters
>
> **Drawback**:
> - Not suitable for interactive systems
> - Assumes unidirectional flow
>
> **When to use**: Sensor processing, signal chains, data transformations
>
> ---
>
> **Pattern 3: DISTRIBUTED (NETWORKED) ARCHITECTURE**
>
> **Structure**: Multiple ECUs connected via network, each handles subset of functions
>
> **Automotive Example - Modern Vehicle Architecture**:
> ```
>        ┌─────────┐         ┌─────────┐         ┌─────────┐
>        │Radar ECU│         │ACC ECU  │         │Brake ECU│
>        └────┬────┘         └────┬────┘         └────┬────┘
>             │                   │                   │
>        ─────┴───────────────────┴───────────────────┴─────  CAN Bus
>             │                   │                   │
>        ┌────┴────┐         ┌────┴────┐         ┌────┴────┐
>        │Camera   │         │Gateway  │         │Cluster  │
>        │ECU      │         │ECU      │         │ECU      │
>        └─────────┘         └─────────┘         └─────────┘
> ```
>
> **Benefits**:
> - Scalability (add ECUs as needed)
> - Fault isolation (one ECU failure doesn't crash system)
> - Supplier independence (different suppliers for different ECUs)
>
> **Drawback**:
> - Network complexity (timing, bandwidth, reliability)
> - Integration challenges
> - Network is single point of failure
>
> **When to use**: Complex vehicles with many functions (standard for automotive)
>
> ---
>
> **Pattern 4: CENTRALIZED (DOMAIN CONTROLLER) ARCHITECTURE**
>
> **Structure**: Powerful central ECU handles multiple functions, reduces distributed ECUs
>
> **Automotive Example - Tesla/Future Architecture**:
> ```
>        ┌──────────────────────────────────┐
>        │   Central ADAS Computer          │
>        │  (ACC + LKA + AEB + Parking...)  │
>        │  (Multi-core, high performance)  │
>        └────────┬─────────────────┬───────┘
>                 │                 │
>           Ethernet            Ethernet
>                 │                 │
>        ┌────────┴──┐         ┌────┴─────────┐
>        │Sensor Hub │         │Actuator Hub  │
>        │(Cameras,  │         │(Throttle,    │
>        │ Radar)    │         │ Brake, Steer)│
>        └───────────┘         └──────────────┘
> ```
>
> **Benefits**:
> - Reduced ECU count (cost savings, weight reduction)
> - Easier software updates (one central computer)
> - Higher performance (powerful processor)
> - Simplified integration
>
> **Drawback**:
> - Single point of failure (need redundancy for safety)
> - High complexity in one unit
> - Expensive central computer
>
> **When to use**: Future vehicles, EVs, high-performance ADAS
>
> **Trend**: Automotive moving from distributed → centralized (domain controllers)"

##### Slide 17: Designing for Quality Attributes
**Visual:** Quality attribute wheel showing design strategies
**Instructor Script:**
> "Architecture must satisfy not just functional requirements but QUALITY attributes (Non-Functional Requirements from Session 4).
>
> **Quality Attribute: SAFETY**
>
> **Architectural strategies:**
> - **Redundancy**: Dual sensors, dual processing paths
> - **Monitoring**: Watchdog timers, plausibility checks
> - **Fail-safe defaults**: On fault, disable function safely
> - **Isolation**: Safety-critical functions physically separated
>
> **ACC Example**:
> - Radar + Camera (redundant perception)
> - Watchdog monitors ACC ECU heartbeat
> - Sensor disagreement > threshold → disable ACC
> - Safety monitor runs on separate core
>
> ---
>
> **Quality Attribute: RELIABILITY**
>
> **Architectural strategies:**
> - **Fault detection**: Self-diagnostics, health monitoring
> - **Graceful degradation**: Reduced functionality vs complete failure
> - **Robust communication**: Error detection (CRC), retransmission
>
> **ACC Example**:
> - If camera fails but radar OK → Continue with reduced confidence
> - CAN messages have CRC checksums
> - ECU logs faults to non-volatile memory
>
> ---
>
> **Quality Attribute: PERFORMANCE (Timing)**
>
> **Architectural strategies:**
> - **Parallel processing**: Distribute load across multiple cores/ECUs
> - **Priority scheduling**: Critical tasks run first
> - **Efficient communication**: High-bandwidth networks (Ethernet)
>
> **ACC Example**:
> - Sensor processing on dedicated cores (parallel)
> - Control loop runs at 20 Hz (highest priority task)
> - Object list transmitted on CAN FD (faster than CAN 2.0)
>
> ---
>
> **Quality Attribute: MAINTAINABILITY**
>
> **Architectural strategies:**
> - **Modularity**: Replace modules independently
> - **Standardized interfaces**: Common connector types, protocols
> - **Diagnostics**: Extensive fault logging, diagnostic protocols
>
> **ACC Example**:
> - Radar sensor is plug-and-play module (calibrated at factory)
> - OBD-II/UDS diagnostics expose fault codes
> - Software updatable via OTA or service tool
>
> ---
>
> **Quality Attribute: TESTABILITY**
>
> **Architectural strategies:**
> - **Test points**: Accessible interfaces for measurement
> - **Simulation interfaces**: Inject test signals
> - **Observability**: Log internal states
>
> **ACC Example**:
> - CAN bus accessible via OBD port (can monitor all messages)
> - Radar can be fed simulated targets (test mode)
> - ECU exposes internal state via diagnostic service ($22)
>
> ---
>
> **Quality Attribute: EVOLVABILITY (Future-Proofing)**
>
> **Architectural strategies:**
> - **Abstraction**: Define stable interfaces
> - **Modularity**: Swap components without redesign
> - **Extensibility**: Design for future additions
>
> **ACC Example**:
> - Sensor interface abstracted (can add lidar without changing ACC logic)
> - Over-the-air (OTA) update capability designed in
> - Spare CAN bandwidth reserved (30% margin for future features)
>
> **Architecture insight:**
> **You can't add quality attributes AFTER architecture is fixed.**
> They must be designed in from the start."

##### Slide 18: Architecture Trade-offs
**Visual:** Trade-off matrix showing conflicting quality attributes
**Instructor Script:**
> "Architecture is about TRADE-OFFS. You can't optimize everything simultaneously.
>
> **Common Trade-offs in Automotive Architecture:**
>
> **1. Safety vs Cost**
> - **High safety**: Dual redundancy, expensive sensors, extra monitoring
> - **Low cost**: Minimum redundancy, cheaper components
> - **Decision**: Depends on ASIL level (ISO 26262)
>   - ASIL D (highest) → Must have redundancy, cost secondary
>   - ASIL A (lowest) → Single sensor acceptable, cost matters
>
> **ACC**: Typically ASIL B or C → Partial redundancy (radar + camera)
>
> ---
>
> **2. Performance vs Power Consumption**
> - **High performance**: Powerful processors, fast networks, continuous operation
> - **Low power**: Lower clock speeds, sleep modes, minimal communication
> - **Decision**: Mission profile dependent
>   - ADAS systems: Performance critical (safety), power secondary
>   - Comfort systems: Power savings important (battery drain)
>
> **ACC**: Performance dominates (can't compromise safety for power savings)
>
> ---
>
> **3. Flexibility vs Complexity**
> - **High flexibility**: Configurable, many options, extensible
> - **Low complexity**: Fixed design, simple, easy to validate
> - **Decision**: Product strategy
>   - Platform architecture: High flexibility (reuse across models)
>   - Single-vehicle architecture: Simplicity (faster development)
>
> **ACC**: Moderate flexibility (configurable time gap, speed limits, but core algorithm fixed)
>
> ---
>
> **4. Centralized vs Distributed**
> - **Centralized**: Fewer ECUs, easier integration, single point of failure
> - **Distributed**: Fault isolation, supplier flexibility, network complexity
> - **Decision**: Technology maturity and safety requirements
>   - Current vehicles: Distributed (proven, fail-safe)
>   - Future vehicles: Centralized domain controllers (cost, performance)
>
> **ACC**: Distributed (current), moving toward centralized (next generation)
>
> ---
>
> **5. COTS (Commercial Off-The-Shelf) vs Custom**
> - **COTS**: Faster development, proven components, less control
> - **Custom**: Optimized for application, higher development cost
> - **Decision**: Criticality and differentiation
>   - Commodity functions: COTS (cost-effective)
>   - Differentiating features: Custom (competitive advantage)
>
> **ACC**: Hybrid (COTS radar sensors, custom fusion algorithms)
>
> **How to make trade-off decisions?**
> → **Trade Studies** (we'll cover in Part 6)
>
> Document:
> - Alternatives considered
> - Evaluation criteria
> - Rationale for decision
> - Risks accepted
>
> Architecture trade-offs define the system. Choose deliberately."

---

#### **Part 4: Architecture Development Process** (Slides 19-21, ~10 minutes)

##### Slide 19: Functional Decomposition
**Visual:** Hierarchical decomposition tree for ACC
**Instructor Script:**
> "How do we go from requirements to architecture? Step 1: Functional Decomposition.
>
> **Functional Decomposition Process:**
>
> **1. Identify top-level functions** (from requirements and CONOPS)
>
> **ACC Top-Level Functions:**
> - Monitor driver inputs
> - Sense environment
> - Detect and track objects
> - Determine desired speed and spacing
> - Control vehicle longitudinal motion
> - Provide driver feedback
> - Perform self-diagnostics
>
> **2. Decompose each function into sub-functions**
>
> **Example: 'Sense Environment' decomposes to:**
> - Emit radar signals
> - Receive radar reflections
> - Process radar returns → range, velocity
> - Capture camera images
> - Process images → lane markings, objects
> - Fuse sensor data → unified world model
>
> **Example: 'Control Vehicle Longitudinal Motion' decomposes to:**
> - Calculate required acceleration/deceleration
> - Determine actuator commands (throttle or brake)
> - Send commands to powertrain/brake ECUs
> - Monitor command execution
> - Detect actuator failures
>
> **3. Continue decomposition until functions are implementable**
>
> **Example: 'Calculate Required Acceleration' decomposes to:**
> - Determine speed error (target speed - current speed)
> - Determine spacing error (desired gap - actual gap)
> - Apply speed control algorithm (PID, MPC, etc.)
> - Apply spacing control algorithm
> - Arbitrate between speed and spacing control
> - Limit acceleration (comfort and safety bounds)
>
> **4. Create Functional Flow Block Diagram (FFBD)**
>
> [Visual shows FFBD with functions and logic flow]
>
> **5. Allocate requirements to functions**
>
> **Example Allocation:**
> - REQ-ACC-015: 'System shall detect vehicles up to 150m'
>   → Allocated to 'Process Radar Returns' function
> - REQ-ACC-042: 'System shall respond to driver button within 200ms'
>   → Allocated to 'Monitor Driver Inputs' function
>
> **Traceability:**
> - Every requirement allocated to at least one function
> - Every function traces to at least one requirement
>
> **Functional decomposition outcomes:**
> - Clear understanding of system behavior
> - Basis for architecture (functions → components)
> - Enables parallel development (different teams, different functions)
> - Verification planning (test each function)
>
> **Session 7 goes deeper:** Operational and Functional Analysis"

##### Slide 20: Requirements Allocation to Subsystems
**Visual:** Allocation matrix showing requirements mapped to architectural elements
**Instructor Script:**
> "After functional decomposition, we allocate requirements to architectural elements (subsystems, components).
>
> **Allocation Process:**
>
> **1. Define architectural elements** (physical subsystems)
>
> **ACC Architecture Elements:**
> - Radar Sensor ECU
> - Camera Sensor ECU
> - ACC Control ECU
> - HMI Module (part of Instrument Cluster)
> - Powertrain Interface
> - Brake Interface
> - CAN Communication Network
>
> **2. Map functions to architectural elements**
>
> **Function → Element Mapping:**
> - 'Emit/Receive Radar Signals' → Radar Sensor ECU
> - 'Process Radar Returns' → Radar Sensor ECU
> - 'Process Camera Images' → Camera Sensor ECU
> - 'Fuse Sensor Data' → ACC Control ECU
> - 'Calculate Acceleration' → ACC Control ECU
> - 'Send Actuator Commands' → ACC Control ECU
> - 'Display Status' → HMI Module
>
> **3. Allocate requirements to elements**
>
> **Requirements Allocation Matrix - Example:**
>
> | Requirement | Allocated To | Derived Requirements |
> |-------------|--------------|---------------------|
> | REQ-ACC-010: Detect vehicles at 150m | Radar Sensor ECU | REQ-Radar-001: Range ≥150m<br>REQ-Radar-002: Update rate ≥20 Hz |
> | REQ-ACC-020: Respond within 200ms | ACC Control ECU | REQ-ACC-ECU-015: Processing latency ≤100ms<br>REQ-CAN-005: Message latency ≤50ms |
> | REQ-ACC-035: Maintain speed ±2 km/h | ACC Control ECU | REQ-ACC-ECU-025: Speed control accuracy ±1.5 km/h<br>REQ-Actuator-010: Throttle response ≤0.5 km/h |
>
> **4. Derive subsystem requirements from system requirements**
>
> **Example Derivation:**
>
> **System Requirement**:
> REQ-ACC-100: 'System shall operate in -40°C to +85°C'
>
> **Derived Subsystem Requirements**:
> - REQ-Radar-ECU-050: 'Radar ECU shall operate in -40°C to +85°C'
> - REQ-Camera-ECU-050: 'Camera ECU shall operate in -40°C to +85°C'
> - REQ-ACC-ECU-050: 'ACC ECU shall operate in -40°C to +85°C'
> - REQ-Radar-Lens-010: 'Radar lens shall include heating element for operation <0°C'
>
> **5. Ensure complete coverage**
>
> **Verification:**
> - Every system requirement allocated? (100% coverage)
> - Every allocated requirement verifiable at subsystem level?
> - Any conflicts between allocations? (requirements pulling in opposite directions)
>
> **Allocation challenges:**
>
> **Challenge 1: Shared requirements**
> - REQ-ACC-200: 'Total system cost <$800'
> - Can't allocate to one subsystem - it's a system-level constraint
> - Solution: Derive cost budgets for each subsystem
>   - Radar ECU: $300, Camera ECU: $200, ACC ECU: $150, Other: $150
>
> **Challenge 2: Interface requirements**
> - REQ-ACC-250: 'CAN latency <50ms'
> - Affects multiple elements (sender, network, receiver)
> - Solution: Allocate to interface definition, specify responsibilities
>
> **Challenge 3: Emergent requirements**
> - Some system behaviors emerge from interactions
> - Example: 'System stability' depends on control algorithm + actuator response + sensor noise
> - Solution: Allocate to integration-level verification
>
> **Outcome: Subsystem Requirements Specifications (SRS)**
> - Each subsystem gets its own requirements document
> - Traceable to system requirements
> - Basis for subsystem design and verification"

##### Slide 21: Interface Definition
**Visual:** Internal Block Diagram (IBD) showing ACC components and interfaces
**Instructor Script:**
> "After allocating requirements, we define interfaces between architectural elements.
>
> **Interface Definition Process:**
>
> **1. Identify all interfaces from architecture**
>
> **ACC Internal Interfaces:**
> - Radar ECU ↔ ACC Control ECU
> - Camera ECU ↔ ACC Control ECU
> - ACC Control ECU ↔ Powertrain ECU
> - ACC Control ECU ↔ Brake ECU
> - ACC Control ECU ↔ HMI Module
> - ACC Control ECU ↔ Diagnostic Module
> - All ECUs ↔ CAN Network
>
> **2. Define interface characteristics**
>
> **For each interface, specify:**
>
> **A. Physical Interface**
> - Connector type (e.g., HDSCS 16-pin connector)
> - Pin assignment
> - Electrical characteristics (voltage levels, current capacity)
> - Environmental protection (IP6K9K for exterior sensors)
>
> **B. Communication Protocol**
> - Network type (CAN 2.0B, CAN FD, Ethernet)
> - Baud rate (500 kbps, 2 Mbps, 100 Mbps)
> - Addressing scheme
> - Error handling (CRC, acknowledgment, retransmission)
>
> **C. Data Interface**
> - Message catalog (all CAN messages defined)
> - Data structures (byte layouts, scaling, offsets)
> - Update rates (how often data refreshes)
> - Timing constraints (max latency, synchronization)
>
> **D. Behavioral Interface**
> - Initialization sequence (power-up, calibration)
> - Normal operation (steady-state message exchange)
> - Fault handling (timeouts, error responses)
> - Shutdown sequence (graceful deactivation)
>
> **Example Interface Definition: ACC ECU → Powertrain ECU**
>
> **Interface ID**: IF-ACC-PWR-001
>
> **Physical**:
> - Connection: Via CAN bus, no direct physical connection
> - CAN transceiver: ISO 11898 compliant
>
> **Protocol**:
> - Network: CAN 2.0B
> - Baud rate: 500 kbps
> - Bus: Powertrain CAN
>
> **Data Messages**:
>
> **Message 1: ACC_TorqueRequest**
> - CAN ID: 0x245
> - DLC: 8 bytes
> - Sender: ACC ECU
> - Receiver: Powertrain ECU
> - Rate: 20 ms (50 Hz)
> - Data:
>   - Byte 0-1: Requested torque (Nm, signed, scale 0.1, offset -500, range -500 to 500 Nm)
>   - Byte 2: Torque rate limit (Nm/s, unsigned, scale 1, range 0-255 Nm/s)
>   - Byte 3: Control mode (0=Inactive, 1=Active, 2=Standby)
>   - Byte 4-6: Reserved (0x00)
>   - Byte 7: CRC-8 checksum
>
> **Message 2: Powertrain_Status**
> - CAN ID: 0x312
> - Sender: Powertrain ECU
> - Receiver: ACC ECU (+ others)
> - Rate: 10 ms (100 Hz)
> - Data:
>   - Engine torque actual (Nm)
>   - Throttle position (%)
>   - Powertrain ready flag
>   - Fault status
>
> **Behavioral**:
> - Normal: ACC sends torque request, Powertrain responds with status
> - Timeout: If ACC doesn't receive Powertrain_Status for >100ms → Disable ACC, alert driver
> - Error: If Powertrain_Status shows fault → ACC disengages
>
> **3. Create Interface Control Documents (ICDs)**
>
> **ICD is a formal specification:**
> - Agreed upon by both sides (ACC team and Powertrain team)
> - Version controlled
> - Changes require approval from both parties
> - Basis for interface testing
>
> **4. Define interface verification strategy**
>
> **How to test interface?**
> - Unit level: Simulate Powertrain ECU, verify ACC ECU sends correct messages
> - Integration level: Connect actual ECUs, verify end-to-end communication
> - Fault injection: Timeout scenarios, corrupted messages, unexpected values
>
> **Interface risks:**
> - 80% of integration problems are interface issues
> - Misunderstood specifications
> - Timing violations
> - Error handling gaps
>
> **Best practice:**
> - Define interfaces EARLY
> - Review interfaces thoroughly
> - Test interfaces separately before system integration
>
> **SysML representation**: Internal Block Diagrams (IBD) with ports and connectors"

---

#### **Part 5: Architecture Frameworks and Views** (Slides 22-23, ~8 minutes)

##### Slide 22: Multiple Architecture Views
**Visual:** 4+1 architectural view model
**Instructor Script:**
> "Complex systems need multiple views to fully describe architecture. No single diagram captures everything.
>
> **Kruchten's 4+1 Architectural View Model** (adapted for automotive):
>
> **1. LOGICAL VIEW - Functional Decomposition**
>
> **Purpose**: Show system functionality and behavior
>
> **Diagrams**:
> - Functional block diagrams
> - State machines (system behavior)
> - Data flow diagrams
>
> **ACC Logical View Example**:
> ```
> ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
> │ Environment  │───>│  Perception  │───>│   Planning   │
> │   Sensing    │    │   & Fusion   │    │  & Control   │
> └──────────────┘    └──────────────┘    └──────────────┘
>                                                 │
>                                                 V
>                                          ┌──────────────┐
>                                          │  Actuation   │
>                                          └──────────────┘
> ```
>
> **Stakeholders**: Systems engineers, software architects, algorithm developers
>
> ---
>
> **2. PHYSICAL VIEW - Hardware Architecture**
>
> **Purpose**: Show physical components and their deployment
>
> **Diagrams**:
> - Component diagrams (ECUs, sensors, actuators)
> - Deployment diagrams (where software runs)
> - Network topology
>
> **ACC Physical View Example**:
> ```
>   [Radar Sensor]───────CAN FD─────┐
>         │                          │
>    [Radar ECU]                     │
>         │                          V
>         └─────CAN 2.0B────────>[ACC ECU]────CAN──>[Powertrain ECU]
>                                    │
>   [Camera Sensor]──Ethernet───────┤
>         │                          │
>    [Camera ECU]────CAN FD──────────┘
>                                    │
>                                CAN Bus
>                                    │
>                              [Instrument Cluster]
> ```
>
> **Stakeholders**: Hardware engineers, integration team, manufacturing
>
> ---
>
> **3. DEVELOPMENT VIEW - Software Architecture**
>
> **Purpose**: Show software organization, modules, layers
>
> **Diagrams**:
> - Package diagrams (software modules)
> - Layer diagrams (AUTOSAR layers)
> - Component diagrams (software components)
>
> **ACC Software View (AUTOSAR Layers)**:
> ```
> ┌─────────────────────────────────────┐
> │  Application Layer                  │  ACC_SpeedControl, ACC_DistanceControl
> ├─────────────────────────────────────┤
> │  Runtime Environment (RTE)          │  Inter-component communication
> ├─────────────────────────────────────┤
> │  Basic Software (BSW)               │  CAN drivers, diagnostics, OS
> ├─────────────────────────────────────┤
> │  Microcontroller Abstraction        │  Hardware drivers
> └─────────────────────────────────────┘
> ```
>
> **Stakeholders**: Software developers, software architects, testing team
>
> ---
>
> **4. PROCESS VIEW - Runtime Behavior**
>
> **Purpose**: Show dynamic behavior, concurrency, timing
>
> **Diagrams**:
> - Sequence diagrams (message exchanges)
> - Timing diagrams (real-time constraints)
> - Task/thread diagrams (concurrency)
>
> **ACC Process View Example - Message Sequence**:
> ```
> Time
>  │   Radar ECU          ACC ECU        Powertrain ECU
>  │       │                 │                  │
>  ├──────>│ Object List     │                  │ (20ms cycle)
>  │       │────────────────>│                  │
>  │       │                 │ Compute Control  │
>  │       │                 │ ─────────────>   │
>  │       │                 │ Torque Request   │
>  │       │                 │─────────────────>│
>  │       │                 │                  │ Actuate
>  │       │                 │<────Status───────│
> ```
>
> **Stakeholders**: Real-time engineers, integration team, verification team
>
> ---
>
> **5. SCENARIO VIEW (+1) - Use Cases**
>
> **Purpose**: Tie views together through operational scenarios
>
> **Diagrams**:
> - Use case diagrams
> - CONOPS scenarios
> - Operational sequence diagrams
>
> **ACC Scenario Example**: Lead vehicle cut-in scenario (from Slide 10)
>
> **Stakeholders**: All stakeholders (validates architecture meets needs)
>
> ---
>
> **Why multiple views?**
> - Different stakeholders need different perspectives
> - No single view shows everything
> - Views are CONSISTENT (describe same system from different angles)
> - Architecture tools (SysML, Enterprise Architect) generate multiple views from single model
>
> **Best practice**: Document all views, maintain consistency across views"

##### Slide 23: Automotive Architecture Frameworks
**Visual:** Comparison of architecture frameworks
**Instructor Script:**
> "Automotive industry uses standardized architecture frameworks. These provide structure and common language.
>
> **Framework 1: AUTOSAR (AUTomotive Open System ARchitecture)**
>
> **Purpose**: Standardize automotive software architecture
>
> **Key Concepts**:
> - Layered architecture (Application, RTE, Basic Software, Hardware)
> - Software Components (SWCs) with defined interfaces
> - Virtual Function Bus (VFB) abstracts communication
> - Standardized interfaces for common functions (CAN, diagnostics, OS)
>
> **ACC in AUTOSAR**:
> - ACC implemented as Application SWCs
> - RTE handles communication between SWCs
> - BSW provides CAN communication, diagnostics, OS
>
> **Benefits**:
> - Portability (move software between ECUs)
> - Reusability (use same SWCs in different vehicles)
> - Supplier interoperability (common interfaces)
>
> **Adoption**: Industry standard (most OEMs and suppliers use AUTOSAR)
>
> ---
>
> **Framework 2: ISO 26262 Safety Architecture**
>
> **Purpose**: Structure architecture for functional safety
>
> **Key Concepts**:
> - ASIL decomposition (break down safety requirements)
> - Safety elements (Safety Mechanisms, Safety Monitor)
> - Freedom from Interference (safety and non-safety isolated)
> - Fault tolerant architecture patterns
>
> **ACC Safety Architecture**:
> - ACC function: ASIL B
> - Safety monitor: ASIL B (independent check)
> - Sensor redundancy: Radar (ASIL B) + Camera (ASIL B)
> - Fail-safe: On fault → safe state (disable, alert driver)
>
> **Architectural Requirements from ISO 26262**:
> - Hardware-software interface (HSI) clearly defined
> - Software partitioning (safety vs non-safety)
> - Diagnostic coverage (detect faults)
>
> ---
>
> **Framework 3: E/E Architecture Reference Models**
>
> **Purpose**: Standardize electrical/electronic architecture
>
> **Common Models**:
>
> **Distributed Architecture** (Current vehicles):
> - Domain-based: Powertrain, Chassis, Body, Infotainment, ADAS
> - Each domain has multiple ECUs
> - Gateway for inter-domain communication
>
> **Centralized Architecture** (Future vehicles):
> - Zone controllers (front, rear, left, right zones)
> - Central compute (high-performance ADAS computer)
> - Simplified wiring
>
> **Service-Oriented Architecture (SOA)** (Emerging):
> - Software services accessible over Ethernet
> - Dynamic service discovery
> - Similar to IT architectures (microservices)
>
> ---
>
> **Framework 4: DODAF / Zachman (Enterprise Architecture)**
>
> **Purpose**: Comprehensive enterprise/system architecture
>
> **DODAF Views** (Department of Defense Architecture Framework):
> - Operational View (OV): Operational scenarios
> - System View (SV): System architecture
> - Technical View (TV): Standards and protocols
>
> **Zachman Framework**:
> - Matrix: Perspectives (Planner, Owner, Designer, Builder, Implementer)
> - × Questions (What, How, Where, Who, When, Why)
>
> **Automotive Use**:
> - Not common for vehicle-level (too heavyweight)
> - Used for enterprise architecture (OEM IT systems, manufacturing)
>
> ---
>
> **Choosing Framework:**
>
> **For ACC system:**
> - Use **AUTOSAR** for software architecture (industry standard)
> - Use **ISO 26262** for safety architecture (regulatory requirement)
> - Use **multiple views** (logical, physical, process, scenario)
>
> **Benefits of frameworks:**
> - Common language across teams and suppliers
> - Proven patterns (don't reinvent)
> - Tool support (AUTOSAR tools, SysML tools)
> - Compliance (ISO 26262 requires architectural documentation)
>
> **Trade-off**: Frameworks add structure but also complexity. Use appropriately."

---

#### **Part 6: Trade Studies and Configuration Management** (Slides 24, ~10 minutes)

##### Slide 24: Trade Studies - Evaluating Architecture Alternatives
**Visual:** Trade study matrix with weighted scoring
**Instructor Script:**
> "Architecture decisions involve choosing between alternatives. Trade studies provide systematic evaluation.
>
> **Trade Study Process:**
>
> **Step 1: Define Decision to Be Made**
>
> **Example Decision**: ACC Sensor Architecture
> - **Question**: What sensor configuration for ACC?
>
> **Step 2: Identify Alternatives**
>
> **Alternative A**: Radar-only
> - 77 GHz long-range radar
> - No camera
>
> **Alternative B**: Radar + Camera
> - 77 GHz radar + monocular camera
> - Sensor fusion in ACC ECU
>
> **Alternative C**: Radar + Stereo Camera
> - 77 GHz radar + stereo camera
> - Enhanced depth perception
>
> **Alternative D**: Lidar + Camera
> - Lidar (instead of radar) + camera
> - Higher resolution
>
> **Step 3: Define Evaluation Criteria**
>
> | Criterion | Weight | Rationale |
> |-----------|--------|-----------|
> | Detection Range | 25% | Critical for highway ACC (need 150m+) |
> | Object Classification | 20% | Distinguish trucks, cars, motorcycles |
> | Cost | 20% | Budget constraint ($500 sensor budget) |
> | Reliability (All Weather) | 15% | Must work in rain, fog, snow |
> | Safety (Redundancy) | 10% | ISO 26262 ASIL B requirement |
> | Technology Maturity | 10% | Proven vs experimental |
>
> **Step 4: Evaluate Each Alternative**
>
> **Evaluation Scale**: 1-5 (1=Poor, 5=Excellent)
>
> | Criterion (Weight) | Alt A: Radar Only | Alt B: Radar+Camera | Alt C: Radar+Stereo | Alt D: Lidar+Camera |
> |--------------------|------------------|---------------------|---------------------|---------------------|
> | Detection Range (25%) | 5 (150m+) | 5 (150m+) | 5 (150m+) | 3 (100m typical) |
> | Object Classification (20%) | 2 (poor) | 4 (good) | 5 (excellent) | 5 (excellent) |
> | Cost (20%) | 5 ($200) | 4 ($400) | 2 ($700) | 1 ($1200+) |
> | All Weather (15%) | 5 (excellent) | 4 (good) | 4 (good) | 2 (lidar struggles in rain) |
> | Safety/Redundancy (10%) | 2 (single sensor) | 5 (dual, different physics) | 5 (dual) | 5 (dual) |
> | Technology Maturity (10%) | 5 (proven) | 5 (proven) | 4 (maturing) | 2 (emerging) |
>
> **Step 5: Calculate Weighted Scores**
>
> **Alternative A: Radar Only**
> = 5×0.25 + 2×0.20 + 5×0.20 + 5×0.15 + 2×0.10 + 5×0.10
> = 1.25 + 0.40 + 1.00 + 0.75 + 0.20 + 0.50
> = **4.10**
>
> **Alternative B: Radar + Camera**
> = 5×0.25 + 4×0.20 + 4×0.20 + 4×0.15 + 5×0.10 + 5×0.10
> = 1.25 + 0.80 + 0.80 + 0.60 + 0.50 + 0.50
> = **4.45** ← Highest Score
>
> **Alternative C: Radar + Stereo**
> = 5×0.25 + 5×0.20 + 2×0.20 + 4×0.15 + 5×0.10 + 4×0.10
> = 1.25 + 1.00 + 0.40 + 0.60 + 0.50 + 0.40
> = **4.15**
>
> **Alternative D: Lidar + Camera**
> = 3×0.25 + 5×0.20 + 1×0.20 + 2×0.15 + 5×0.10 + 2×0.10
> = 0.75 + 1.00 + 0.20 + 0.30 + 0.50 + 0.20
> = **2.95**
>
> **Step 6: Analyze Results**
>
> **Winner: Alternative B (Radar + Camera) - Score 4.45**
>
> **Strengths**:
> - Excellent detection range (radar strength)
> - Good object classification (camera strength)
> - Redundancy (different sensor physics → independent failures)
> - Reasonable cost ($400 vs $200 for radar-only)
> - Proven technology (widely deployed)
>
> **Weaknesses**:
> - Higher cost than radar-only (+$200)
> - Camera limited in bad weather (but radar compensates)
>
> **Runner-up: Alternative C (Radar + Stereo) - Score 4.15**
> - Better classification, but cost too high ($700 vs $400)
>
> **Step 7: Sensitivity Analysis**
>
> **What if cost weight changes?**
> - If cost weight increases to 30% (from 20%): Alternative A (radar-only) might win
> - If classification weight increases to 30%: Alternative C (stereo) becomes competitive
>
> **This shows decision is SENSITIVE to priorities. Document assumptions!**
>
> **Step 8: Document Decision**
>
> **Trade Study Report Includes**:
> - Alternatives considered
> - Evaluation criteria and weights (with rationale)
> - Scoring and calculations
> - Sensitivity analysis
> - **Recommendation**: Alternative B (Radar + Camera)
> - **Rationale**: Best balance of performance, cost, safety, maturity
> - **Risks**: Camera performance degrades in heavy rain/snow (mitigated by radar backup)
> - **Decision authority**: Chief Engineer approval required
>
> **Why formal trade studies?**
> - **Justification**: Defensible decisions (not arbitrary)
> - **Traceability**: Documented rationale for architecture choices
> - **Risk management**: Sensitivity analysis reveals vulnerabilities
> - **Stakeholder alignment**: Transparent process, agreed criteria
>
> **Trade studies are critical for:**
> - Major architecture decisions
> - Technology selection (sensor types, ECU platforms, networks)
> - Supplier selection
> - Safety architecture (redundancy strategies)
> - Cost-performance trade-offs
>
> **Session 10 (Decision Management) covers advanced techniques: AHP, Pareto optimization, Monte Carlo sensitivity**"

---

### **CLIMAX: Configuration Management and Design Freeze** (Slides 25-26, ~8 minutes)

#### Slide 25: Design Freeze and Baseline Management
**Visual:** Architecture evolution timeline showing baselines and design freeze
**Instructor Script:**
> "Architecture evolves during development. We must manage this evolution through baselines and design freeze.
>
> **Architecture Lifecycle:**
>
> **Phase 1: Concept (Months 0-6)**
> - Explore multiple architectures
> - Trade studies (like we just saw)
> - Preliminary architecture selected
> - **Baseline 1**: Concept Architecture (30% confidence)
>
> **Phase 2: Preliminary Design (Months 6-12)**
> - Refine architecture
> - Interface definitions
> - Subsystem allocation
> - **Baseline 2**: Preliminary Architecture (70% confidence)
>
> **Phase 3: Detailed Design (Months 12-18)**
> - Finalize architecture
> - Detailed interface specs (ICDs)
> - Component specifications
> - **Baseline 3: Critical Design Review (CDR) - DESIGN FREEZE** (95% confidence)
>
> **Phase 4: Implementation (Months 18-30)**
> - Architecture FROZEN (changes require formal approval)
> - Components developed to frozen architecture
> - Integration per frozen interface specs
> - **Baseline 4**: As-Built Architecture (100%, production)
>
> ---
>
> **What is Design Freeze?**
>
> **Definition**: Point where architecture is locked; further changes require formal change control process
>
> **Why Design Freeze?**
> - **Enables parallel development**: Teams develop components knowing interfaces won't change
> - **Prevents chaos**: Without freeze, constant changes disrupt development
> - **Allows integration**: Can't integrate if architecture keeps changing
> - **Supports verification**: Tests written against frozen architecture
>
> **What gets frozen at Design Freeze?**
> ✓ Subsystem architecture (what components exist)
> ✓ Interface definitions (ICDs locked)
> ✓ Requirements allocation (which subsystem satisfies which requirement)
> ✓ Safety architecture (ASIL decomposition, redundancy)
>
> **What can still change after freeze?**
> - Internal implementation details (algorithms, code structure)
> - Internal component design (if interfaces maintained)
> - Non-functional optimizations (performance tuning)
>
> ---
>
> **Configuration Management:**
>
> **What is Configuration Management (CM)?**
> 'Formal process for identifying, controlling, and tracking configuration items (CIs) throughout lifecycle'
>
> **Configuration Items for Architecture:**
> - Architecture diagrams (logical, physical views)
> - Interface Control Documents (ICDs)
> - Requirements Allocation Matrix
> - Trade study reports
> - Design decision logs
>
> **CM Activities:**
>
> **1. Identification**
> - Each architecture artifact has unique ID
> - Version numbering (v1.0, v1.1, v2.0)
> - Example: 'ICD-ACC-PWR-v2.3' (Interface between ACC and Powertrain, version 2.3)
>
> **2. Change Control**
> - Change Request (CR) process
> - Impact analysis (what does this change affect?)
> - Change Review Board (CRB) approves/rejects
> - Only approved changes implemented
>
> **3. Status Accounting**
> - Track status of all CIs (draft, reviewed, approved, released, obsolete)
> - Know which version is current
>
> **4. Auditing**
> - Physical Configuration Audit (PCA): Does as-built match design?
> - Functional Configuration Audit (FCA): Does it meet requirements?
>
> ---
>
> **Change Control Process (Post-Freeze):**
>
> **Step 1: Change Request Submitted**
> - Example: 'Need to increase CAN message frequency from 20ms to 10ms'
> - Rationale: Improved control loop performance
>
> **Step 2: Impact Analysis**
> - Which subsystems affected? (ACC ECU software, CAN bus load)
> - What changes required? (Software timing, CAN bus bandwidth analysis)
> - What's the risk? (May exceed CAN bandwidth limit)
> - Cost impact? (+1 week development, $5k testing)
>
> **Step 3: Review by Change Control Board (CCB)**
> - Members: Chief Engineer, Systems Engineer, Safety Engineer, Project Manager
> - Evaluate: Is benefit worth cost and risk?
> - Decision: Approve / Reject / Defer
>
> **Step 4: Implementation (if approved)**
> - Update architecture documentation
> - Update ICDs
> - Notify affected teams
> - Re-verify affected interfaces
>
> **Step 5: Verification**
> - Test change (regression testing)
> - Update test cases
>
> **Step 6: New Baseline**
> - Release new version of affected CIs
> - Update configuration status
>
> ---
>
> **Design Freeze Trade-offs:**
>
> **Freeze TOO EARLY:**
> - ❌ Architecture not mature (high risk of changes needed)
> - ❌ Expensive late changes (rework)
>
> **Freeze TOO LATE:**
> - ❌ Delays implementation start (schedule risk)
> - ❌ Teams waiting (idle resources)
>
> **Optimal timing:** Freeze when architecture confidence is 90-95%
> - Some uncertainty remains, but major decisions made
> - Typical: After Critical Design Review (CDR)
>
> **Automotive typical timeline:**
> - Concept freeze: Month 6 (explore → commit to direction)
> - Architecture freeze: Month 12 (preliminary → detailed)
> - Design freeze (CDR): Month 18 (start production development)
> - Start of Production (SOP): Month 36-48
>
> **Modern challenge: Agile vs Design Freeze**
> - Agile: Embrace change, iterate quickly
> - Automotive: Safety-critical, long validation cycles, need stability
> - **Hybrid approach**: Freeze safety-critical interfaces, allow agility in non-critical areas
>
> Configuration management is not bureaucracy - it's risk management for complex systems."

#### Slide 26: Architecture Documentation
**Visual:** Architecture document hierarchy
**Instructor Script:**
> "Architecture must be documented. If it's not written down, it doesn't exist.
>
> **Architecture Documentation Hierarchy:**
>
> **Level 1: System Architecture Description (SAD)**
>
> **Purpose**: Top-level architecture overview
>
> **Contents**:
> - Executive summary (architecture in 1 page)
> - Architecture views (logical, physical, process, scenario)
> - Design principles and rationale
> - Key architecture decisions and trade-offs
> - System context and boundaries
> - Subsystem descriptions
> - Interface overview
> - Safety architecture (ISO 26262 compliance)
> - Architecture verification approach
>
> **Audience**: Systems engineers, management, external stakeholders
> **Length**: 30-50 pages for vehicle system
>
> ---
>
> **Level 2: Interface Control Documents (ICDs)**
>
> **Purpose**: Define each interface precisely
>
> **Contents** (per interface):
> - Interface ID and version
> - Connected subsystems
> - Physical interface spec (connectors, pins, electrical)
> - Protocol spec (CAN messages, timing, error handling)
> - Data dictionary (all signals defined)
> - Behavioral spec (sequence diagrams, state machines)
> - Verification requirements
>
> **Example**: ICD-ACC-Radar (ACC ECU ↔ Radar Sensor interface)
>
> **Audience**: Developers on both sides of interface
> **Length**: 5-20 pages per ICD
> **Count**: 10-20 ICDs for typical system
>
> ---
>
> **Level 3: Subsystem Architecture Specifications**
>
> **Purpose**: Detail each subsystem's internal architecture
>
> **Contents**:
> - Subsystem requirements (from allocation)
> - Internal architecture (components, modules)
> - Internal interfaces
> - Algorithms (high-level description)
> - Hardware architecture (if applicable)
> - Software architecture (AUTOSAR components, layers)
>
> **Example**: ACC ECU Software Architecture Specification
>
> **Audience**: Subsystem development team
> **Length**: 20-40 pages per subsystem
>
> ---
>
> **Level 4: Supporting Documentation**
>
> **Trade Study Reports**:
> - Alternatives considered
> - Evaluation criteria
> - Recommendation and rationale
>
> **Design Decision Logs**:
> - What decision was made?
> - When and by whom?
> - Rationale
> - Alternatives rejected
>
> **Architecture Verification Plan**:
> - How will architecture be verified?
> - Integration test strategy
> - Interface verification approach
>
> **Requirements Traceability Matrix (RTM)**:
> - Requirements → Architecture elements
> - Architecture elements → Requirements
>
> ---
>
> **Documentation Best Practices:**
>
> **1. Use Standard Templates**
> - Company/industry templates (ISO/IEC 42010, AUTOSAR)
> - Consistent structure across projects
>
> **2. Maintain Single Source of Truth**
> - One master document (version controlled)
> - Not scattered across emails, PowerPoints, wikis
> - Use document management system (DOORS, Polarion, SharePoint)
>
> **3. Keep Synchronized with Implementation**
> - Architecture documentation must match as-built
> - Update docs when changes approved
> - Configuration audit verifies sync
>
> **4. Use Diagrams Heavily**
> - Architecture is visual (block diagrams, ICDs, sequence diagrams)
> - SysML/UML tools (Enterprise Architect, Cameo, Rhapsody)
> - Auto-generate documentation from models (MBSE benefit)
>
> **5. Review and Approve**
> - Peer review (architects, lead engineers)
> - Stakeholder review (suppliers, safety, management)
> - Formal approval (signatures, version release)
>
> **6. Make Accessible**
> - All team members can access
> - Searchable (find interface specs quickly)
> - Linked (traceability: requirement → architecture → test)
>
> ---
>
> **Common Documentation Failures:**
>
> ❌ **Outdated docs**: Documentation doesn't match as-built
> - Root cause: Changes made, docs not updated
> - Solution: Configuration management process
>
> ❌ **Incomplete docs**: Missing critical details
> - Root cause: Rushed documentation, lack of review
> - Solution: Checklists, templates, peer review
>
> ❌ **Inaccessible docs**: Can't find information when needed
> - Root cause: Poor organization, scattered files
> - Solution: Document management system, index
>
> ❌ **Ambiguous docs**: Multiple interpretations possible
> - Root cause: Vague language, no diagrams
> - Solution: Precise language, diagrams, examples
>
> **Quality gate**: Before design freeze, architecture documentation reviewed and approved by all stakeholders"

---

### **RESOLUTION: Synthesis and Next Steps** (Slides 27-30, ~8 minutes + Q&A)

#### Slide 27: ACC Architecture - Complete Example
**Visual:** Complete ACC architecture with all views
**Instructor Script:**
> "Let's synthesize everything we've learned by looking at the complete ACC architecture.
>
> **ACC System Architecture - Integrated Views:**
>
> **1. Context View**:
> - Boundaries: ACC system vs external vehicle systems
> - External interfaces: 8 major interfaces (driver, sensors, actuators, diagnostics)
>
> **2. Logical View (Functional)**:
> - Functions: Sensing → Perception → Planning → Control → Actuation → HMI
> - Functional flow: Continuous loop (20 Hz control cycle)
>
> **3. Physical View (Hardware)**:
> - Components: Radar ECU, Camera ECU, ACC ECU, Instrument Cluster
> - Network: CAN 2.0B (500 kbps) + CAN FD (2 Mbps for sensors)
> - Topology: Star (all ECUs connect to CAN backbone)
>
> **4. Process View (Runtime)**:
> - Timing: 50 ms end-to-end latency (sensor → decision → actuation)
> - Tasks: Sensor processing (10 ms), Fusion (20 ms), Control (20 ms), HMI (100 ms)
> - Priorities: Control (highest), Sensing (high), HMI (medium), Diagnostics (low)
>
> **5. Safety Architecture (ISO 26262)**:
> - ASIL: ASIL B (moderate safety-critical)
> - Redundancy: Radar + Camera (independent sensing)
> - Safety monitor: Plausibility checks, watchdog
> - Fail-safe: On fault → disable ACC, alert driver, log fault
>
> **Key Architecture Decisions Recap:**
>
> **Decision 1**: Distributed architecture (Radar ECU + Camera ECU + ACC ECU)
> - **Rationale**: Fault isolation, supplier flexibility, proven approach
> - **Alternative rejected**: Centralized (single ECU) - less mature, higher risk
>
> **Decision 2**: Radar + Camera sensor fusion
> - **Rationale**: Trade study showed best cost-performance-safety balance
> - **Alternative rejected**: Radar-only (insufficient classification), Lidar (too expensive)
>
> **Decision 3**: CAN 2.0B for vehicle network, CAN FD for sensor data
> - **Rationale**: CAN 2.0B proven, CAN FD needed for high-bandwidth sensor data
> - **Alternative rejected**: Full Ethernet (not yet mature in all domains)
>
> **Decision 4**: AUTOSAR software architecture
> - **Rationale**: Industry standard, reusability, portability
> - **Alternative rejected**: Custom architecture (reinventing wheel)
>
> **Decision 5**: Design freeze at Month 12 (after preliminary design)
> - **Rationale**: 90% architecture confidence, allows 18 months implementation
> - **Interfaces locked, internal algorithms can still evolve**
>
> **Requirements Allocation (Sample):**
> - REQ-ACC-010 'Detect vehicles at 150m' → Radar ECU + Fusion Algorithm
> - REQ-ACC-025 'Maintain ±2 km/h accuracy' → Control Algorithm + Powertrain Interface
> - REQ-ACC-050 'Respond within 200 ms' → System-level (sensor latency + processing + actuation)
>
> **This architecture is:**
> ✓ **Traceable**: All requirements allocated, all decisions justified
> ✓ **Verifiable**: Clear test strategy for each interface and subsystem
> ✓ **Implementable**: Subsystems can be developed in parallel
> ✓ **Safe**: Redundancy, fail-safe, ISO 26262 compliant
> ✓ **Maintainable**: Modular, documented, standardized (AUTOSAR)
>
> **From requirements (Session 4) → Architecture (Session 5) → Implementation (design/code)**"

#### Slide 28: Key Takeaways
**Visual:** Summary infographic with key concepts
**Instructor Script:**
> "Let's consolidate today's learning:
>
> **1. CONOPS Drives Architecture**
> - Understand HOW the system will be used before designing it
> - Operational scenarios reveal architectural requirements
> - CONOPS informs trade studies and design decisions
>
> **2. Context and Boundaries Matter**
> - Define what's IN vs OUT explicitly
> - Catalog all external interfaces
> - Interfaces are risk - minimize, simplify, document rigorously
>
> **3. Apply Design Principles**
> - Modularity, hierarchy, abstraction, separation of concerns
> - Redundancy and fail-safe for safety-critical systems
> - Principles are timeless - patterns are proven solutions
>
> **4. Architecture Has Multiple Views**
> - Logical (functional), Physical (hardware), Process (runtime), Development (software)
> - No single view captures everything
> - Use standard frameworks (AUTOSAR, ISO 26262, SysML)
>
> **5. Systematic Architecture Development**
> - Functional decomposition (requirements → functions)
> - Requirements allocation (functions → subsystems)
> - Interface definition (subsystems ↔ subsystems)
> - Use trade studies to evaluate alternatives
>
> **6. Configuration Management is Essential**
> - Baseline architecture at key milestones
> - Design freeze enables parallel development
> - Change control process post-freeze
> - Documentation must stay synchronized with implementation
>
> **7. Trade Studies Justify Decisions**
> - Identify alternatives, define criteria, evaluate systematically
> - Document rationale (defensible decisions)
> - Sensitivity analysis reveals risks
>
> **8. Architecture is Where We Make or Break the System**
> - Poor architecture → expensive integration problems, late failures
> - Good architecture → smooth integration, modular testing, maintainable system
> - Architecture decisions have long-lasting consequences
>
> **Critical connection:**
> - **Session 4**: Requirements tell us WHAT to build
> - **Session 5** (Today): Architecture tells us HOW to organize the solution
> - **Session 7**: Functional analysis tells us HOW to allocate behavior
> - **Session 8**: Integration and verification tell us we built it right
>
> **Architecture is the bridge from requirements to implementation.**"

#### Slide 29: Connection to V-Model and Next Sessions
**Visual:** V-Model with Sessions 4-5-7-8 highlighted
**Instructor Script:**
> "Let's place today in the systems engineering journey.
>
> **V-Model Left Side (Design):**
>
> **Session 4 - Requirements Engineering**:
> - Stakeholder needs and system requirements
> - WHAT the system must do
> - Output: Requirements Specification
>
> **Session 5 - Architecture (Today)**:
> - System architecture and design
> - HOW the system is organized
> - Output: System Architecture Description, ICDs
>
> **↓ Next step: Subsystem design (detailed design)**
>
> **What comes next:**
>
> **Session 7 - Operational and Functional Analysis**:
> - Analyze operational scenarios in depth
> - Functional flow block diagrams (FFBD)
> - Allocate requirements to functions systematically
> - Timeline analysis (sequence of operations)
> - **Connection**: Session 5 created architecture; Session 7 allocates behavior to that architecture
>
> **Session 8 - Integration, Verification & Validation**:
> - Right side of V-Model
> - Integration strategy (how to assemble system from subsystems)
> - Verification (did we build architecture correctly?)
> - Validation (does architecture meet stakeholder needs?)
> - **Connection**: Verify architecture through integration testing
>
> **Session 9 - Risk Management**:
> - Identify architectural risks (single points of failure, interface complexity)
> - DFMEA (Design Failure Mode and Effects Analysis)
> - Mitigate risks in architecture
>
> **Session 10 - Decision Management**:
> - Advanced trade study techniques (AHP, multi-attribute utility theory)
> - Dealing with uncertainty in architecture decisions
> - **Connection**: Extends trade studies from today
>
> **Session 12 - Safety Engineering (ISO 26262)**:
> - Safety architecture requirements
> - ASIL decomposition
> - Safety mechanisms
> - **Connection**: Today we mentioned safety architecture; Session 12 goes deep
>
> **The thread:**
> - Requirements → Architecture → Functional Allocation → Design → Implementation → Verification
> - Each session builds on previous
> - Architecture is the pivotal link
>
> **Key insight from V-Model:**
> Architecture decisions made on LEFT side determine integration approach on RIGHT side.
> Modular architecture → modular integration and testing."

#### Slide 30: Practice Exercise & Q&A
**Visual:** Exercise description with evaluation rubric
**Instructor Script:**
> "**Practical Exercise (Due before Session 6):**
>
> You are the lead systems architect for a **Lane Keeping Assist (LKA)** system.
>
> **Part 1: CONOPS (20%)**
> - Develop 3 operational scenarios for LKA (normal operation, lane departure, driver override)
> - Each scenario includes: context, operational sequence, expected system behavior
>
> **Part 2: System Context (20%)**
> - Create system context diagram
> - Identify all external interfaces (minimum 8)
> - Define system boundary (what's IN vs OUT)
>
> **Part 3: Architecture Development (40%)**
> - Develop system architecture with:
>   - Functional decomposition (minimum 6 major functions)
>   - Physical architecture (ECUs, sensors, actuators, network)
>   - Allocate 10 system requirements to architectural elements (use requirements from your Session 4 exercise or create new ones)
>   - Define 3 key interfaces (create simplified ICDs with message definitions)
>
> **Part 4: Trade Study (20%)**
> - Conduct trade study for ONE architecture decision:
>   - Camera configuration: Monocular vs Stereo vs Fisheye
>   - OR Actuation: Steering torque overlay vs Steering angle control
>   - OR ECU architecture: Integrated (with ACC) vs Dedicated LKA ECU
> - Include: alternatives, criteria (minimum 5), weighted scoring, recommendation, rationale
>
> **Deliverables:**
> - **Part 1**: CONOPS document (1-2 pages)
> - **Part 2**: Context diagram + interface table (1 page)
> - **Part 3**: Architecture diagrams (logical, physical views) + allocation matrix (2-3 pages)
> - **Part 4**: Trade study report (1-2 pages)
> - **Total**: 5-8 pages
>
> **Grading Criteria:**
> - **CONOPS quality**: Operational scenarios realistic and detailed? (20%)
> - **Context completeness**: All interfaces identified? Boundary clear? (20%)
> - **Architecture soundness**:
>   - Functional decomposition logical? (10%)
>   - Physical architecture feasible? (10%)
>   - Requirements properly allocated? (10%)
>   - Interfaces well-defined? (10%)
> - **Trade study rigor**: Criteria justified? Scoring documented? Sensitivity considered? (20%)
>
> **Tips:**
> - Research real LKA systems (Euro NCAP, SAE standards)
> - Think about safety architecture (ISO 26262 ASIL B typical for LKA)
> - Consider camera placement (windshield vs side mirrors)
> - Don't over-design (stay at system architecture level, not detailed design)
> - Use SysML notation if you know it (not required)
> - Document rationale for all major decisions
>
> **Bonus (Optional):**
> - Create Process View showing message timing (sequence diagram)
> - Identify potential failure modes and architectural mitigations
> - Compare your architecture to Tesla Autopilot LKA (publicly available info)
>
> **Discussion Questions:**
> - How would LKA architecture differ from ACC architecture? (Similar sensors, different actuation)
> - What if we combine LKA + ACC into single system? (Integration challenges? Benefits?)
> - How does camera placement affect architecture? (Windshield vs hood vs mirrors)
>
> **Learning objectives:**
> - Practice CONOPS development
> - Practice architecture decomposition and allocation
> - Conduct systematic trade study
> - Document architecture professionally
>
> **30 minutes for your questions.**"

---

## 📊 PPT DESIGN GUIDANCE

### Visual Style:
- **Professional engineering aesthetic**: Clean, technical, systems-oriented
- **Color coding**:
  - Blue for functional/logical views
  - Green for physical/hardware views
  - Orange for interfaces
  - Red for safety/critical elements
  - Purple for trade-offs/decisions
- **Use real automotive examples**: ACC system throughout, LKA references, Tesla/ADAS photos
- **Diagrams**: Block diagrams, ICDs, context diagrams, architecture views (SysML/UML style)

### Key Slides to Emphasize:
1. **Slide 3** (Requirements Drive Architecture) - Critical connection from Session 4
2. **Slide 8** (Architecture Decisions) - Real decisions students will face
3. **Slide 10** (CONOPS Scenarios) - Operational thinking
4. **Slide 15** (Design Principles) - Timeless guidelines
5. **Slide 16** (Architecture Patterns) - Proven solutions
6. **Slide 22** (Multiple Views) - Comprehensive perspective
7. **Slide 24** (Trade Studies) - Systematic evaluation
8. **Slide 27** (Complete ACC Architecture) - Integration of all concepts
9. **Slide 28** (Takeaways) - Students will photograph this

### Animations:
- **Slide 3**: Animate flow from Requirements → Architecture → Design → Implementation
- **Slide 8**: Build architecture decision tree progressively
- **Slide 10**: Animate CONOPS scenarios as timeline sequences
- **Slide 13**: Highlight interfaces appearing one by one on context diagram
- **Slide 19**: Build functional decomposition tree level by level
- **Slide 22**: Transition between architecture views (logical → physical → process)
- **Slide 24**: Animate trade study scoring calculation step by step
- **Slide 27**: Layer complete architecture views (build up final integrated view)

### Tables and Diagrams:
- **Slide 12**: Context diagram with boundary box
- **Slide 13**: Interface identification matrix
- **Slide 16**: Architecture pattern comparison (4 patterns side-by-side)
- **Slide 19**: Functional hierarchy tree
- **Slide 20**: Requirements allocation matrix
- **Slide 22**: 4+1 view model diagrams
- **Slide 24**: Trade study evaluation matrix with calculations
- **Slide 26**: Configuration management process flow

### Real Examples to Include:
- ACC system (primary example throughout)
- Tesla architecture references (publicly available)
- AUTOSAR layer diagrams
- ISO 26262 safety architecture examples
- CAN message definitions (real format)
- SysML diagrams (BDD, IBD examples)

---

## 🎯 INSTRUCTOR NOTES

### Pedagogical Strategy:
- **Concrete → Abstract → Concrete**: Start with ACC example, teach principles, return to ACC complete architecture
- **Multiple perspectives**: Show that architecture needs multiple views (not just one diagram)
- **Decisions over perfection**: Emphasize trade-offs and justified decisions
- **Tools and standards**: Expose students to industry practices (AUTOSAR, ISO 26262, SysML)

### Common Student Challenges:

**Challenge 1: "Difference between architecture and design?"**
**How to address:** Architecture = high-level structure, interfaces, major components. Design = detailed implementation (algorithms, data structures, code). Use analogy: Architecture = house floor plan; Design = electrical wiring diagram, plumbing details.

**Challenge 2: "How much detail in architecture?"**
**How to address:** Goldilocks principle - enough detail to enable parallel development and integration, not so much that you constrain implementation. Interface definitions must be detailed; internal algorithms can remain abstract.

**Challenge 3: "Overwhelming number of diagrams/views"**
**How to address:** Each view serves specific stakeholders. You don't create all views for every project - select relevant ones. Small project: Maybe 2-3 views. Large vehicle project: All views needed.

**Challenge 4: "When to freeze architecture?"**
**How to address:** Freeze when confidence is 90-95%. Use design reviews as checkpoints. Too early = rework risk. Too late = schedule delays. Show timeline examples from real projects.

**Challenge 5: "Trade studies seem subjective"**
**How to address:** They ARE subjective - criteria weights reflect priorities. Key is TRANSPARENCY and DOCUMENTATION. Sensitivity analysis reveals where subjectivity matters most. Even imperfect systematic approach beats gut decisions.

### Timing Flexibility:

**If running short:**
- Condense Slide 16 (patterns) - focus on 2-3 patterns most relevant
- Reduce Slide 22 (views) to 3 views instead of 5
- Simplify Slide 24 (trade study) - show process, skip detailed calculation

**If running long:**
- Extend Slide 10 (CONOPS) with additional scenarios and student discussion
- Add live demo: Create simple SysML diagram using tool
- Extend Slide 24 (trade study) with sensitivity analysis discussion
- Show real automotive architecture documentation examples

**Core content (must cover - non-negotiable):**
- Slides 9-11 (CONOPS)
- Slides 12-14 (Context and boundaries)
- Slides 15-17 (Design principles and patterns)
- Slides 19-21 (Architecture development process)
- Slide 24 (Trade studies)
- Slide 25 (Design freeze and configuration management)
- Slide 27 (Complete example)
- Slide 28 (Summary)

### Engagement Points:

**Slide 7**: Interactive - Ask students: "What subsystems would YOU include in ACC?" List on board, compare to complete answer.

**Slide 8**: Poll - "Which decision do you think is most critical?" Discuss why.

**Slide 13**: Work through one interface definition together - students suggest what needs to be specified.

**Slide 16**: Ask students to identify pattern in a system they know (smartphone, home automation).

**Slide 24**: Live trade study - pick a simple decision, have class suggest criteria and weights.

### Interactive Elements:

**Quick Poll (Slide 8)**: "How many have worked on projects where architecture changed late?" (Show of hands - normalizes the integration pain)

**Think-Pair-Share (Slide 15)**: "Pick one design principle. How would you apply it to ACC?" (2 minutes individual, 2 minutes pairs, 3 minutes share)

**Small Group Exercise (Slide 24)**: Break into groups, each evaluates one alternative for trade study, then combine scores.

### Materials to Prepare:

**Before class:**
- [ ] ACC architecture diagrams (all views)
- [ ] Sample ICD (real or realistic)
- [ ] Trade study template (spreadsheet)
- [ ] SysML tool demo (Enterprise Architect, Cameo, or Papyrus)
- [ ] Real automotive architecture examples (from publicly available sources)
- [ ] Configuration management process flowchart

**Handouts:**
- [ ] Architecture documentation template
- [ ] Trade study template (Excel with formulas)
- [ ] Interface Control Document template
- [ ] Design principles checklist
- [ ] Architecture review checklist

**Post-class:**
- [ ] Share slides
- [ ] Post exercise assignment with due date and rubric
- [ ] Post architecture templates (SAD template, ICD template, trade study template)
- [ ] Share links to AUTOSAR standard, ISO 26262 Part 4 (architecture), SysML tutorials
- [ ] Create discussion forum: "Share an architecture decision from your experience and the trade-offs"

### Assessment Opportunities:

**During lecture:**
- Quick quiz (Slide 15): "Name three design principles and how they apply to ACC"
- Quick quiz (Slide 22): "What's the purpose of Physical View vs Logical View?"

**Exercise assessment criteria:**
- CONOPS realism (Are scenarios operationally sound?)
- Context completeness (All interfaces identified? Boundary clear?)
- Architecture feasibility (Could this be built? Does it satisfy requirements?)
- Trade study rigor (Systematic evaluation? Documented rationale?)
- Professional presentation (Industry-standard diagrams and formatting?)

**Common student mistakes to watch for:**
- Confusing architecture with detailed design (too much detail)
- Missing interfaces (incomplete context analysis)
- Ignoring non-functional requirements in architecture
- No traceability from requirements to architecture
- Trade studies with unjustified criteria or weights
- Vague interface definitions (not specific enough for implementation)

---

## ✅ Session Success Criteria

Students leave able to:
- ✓ Develop CONOPS for automotive systems
- ✓ Define system context and identify all external interfaces
- ✓ Apply design principles (modularity, hierarchy, abstraction, redundancy, fail-safe)
- ✓ Decompose system functionally and allocate requirements to subsystems
- ✓ Create multiple architecture views (logical, physical, process)
- ✓ Conduct systematic trade studies for architecture decisions
- ✓ Understand design freeze and configuration management
- ✓ Document architecture professionally

**Critical outcome:** Students understand that **architecture is systematic**, not ad-hoc, and that **architecture decisions have long-term consequences** for cost, safety, maintainability, and integration.

**Evidence of success:**
- Student can develop a credible system architecture from requirements
- Student can justify architecture decisions through trade studies
- Student understands that multiple architecture views are necessary
- Student can trace requirements to architectural elements
- Student can define interfaces precisely enough for parallel development

---

## 📚 Additional Resources for Students

**Standards and Guidelines:**
- ISO/IEC/IEEE 42010:2011: Systems and Software Architecture Description
- ISO/IEC 15288:2015: System Architecture Definition Process (Section 6.4.4)
- INCOSE Systems Engineering Handbook, Chapter 5: System Architecture
- IEEE 1471: Architectural Description (predecessor to ISO 42010)

**Automotive-Specific:**
- ISO 26262-4:2018: Road Vehicles - Functional Safety - Part 4: Product Development at System Level
- AUTOSAR Architecture Specifications (www.autosar.org)
- SAE J3016: Taxonomy of Automated Driving (architecture implications)
- EAST-ADL: Electronics Architecture and Software Technology - Architecture Description Language

**Books:**
- "Software Systems Architecture" by Rozanski & Woods (views and perspectives)
- "Documenting Software Architectures" by Clements et al. (SEI)
- "Automotive Software Engineering" by Schäuffele & Zurawka (automotive-specific architecture)
- "Design Patterns" by Gamma et al. (software patterns applicable to systems)

**Online Resources:**
- AUTOSAR tutorials and specifications
- SysML tutorials (OMG SysML website)
- ISO 26262 architecture examples (public case studies)
- SAE standards for automotive systems

---

## 🔗 Connections to Other Sessions

**Builds on:**
- **Session 1**: Architecture failures cause system failures (case studies)
- **Session 2**: ISO/IEC 15288 Architecture Definition process
- **Session 3**: MBSE - SysML diagrams for architecture (BDD, IBD)
- **Session 4**: Requirements drive architecture; architecture satisfies requirements

**Leads to:**
- **Session 6**: Case study applying requirements + architecture
- **Session 7**: Functional analysis allocates behavior to architecture
- **Session 8**: Integration strategy flows from architecture; verification tests architecture
- **Session 9**: Risk management identifies architectural risks; DFMEA on architecture
- **Session 10**: Advanced decision techniques for architecture trade-offs
- **Session 12**: Safety architecture (ISO 26262) - extends today's safety concepts
- **Session 15**: Configuration management and technical planning - extends baseline concepts

**Key concept thread:**
- **Session 2**: WHAT is the SE process? (ISO/IEC 15288 framework)
- **Session 3**: WHAT are the tools? (MBSE, SysML)
- **Session 4**: WHAT must the system do? (Requirements)
- **Session 5** (Today): HOW is the system organized? (Architecture)
- **Session 7**: HOW does the system behave? (Functional analysis)
- **Session 8**: HOW do we verify? (Integration and V&V)

**Architecture appears in:**
- Session 7 (functional allocation to architecture)
- Session 8 (architecture-driven integration)
- Session 9 (architecture risk analysis)
- Session 12 (safety architecture)
- Session 13 (life cycle cost driven by architecture)

---

## 🎬 Opening and Closing Strategies

### **Opening (First 2 minutes):**
Show image of ACC system on screen. Begin:

> "Look at this image - an Adaptive Cruise Control system. Seems simple, right? Maintain speed, keep distance.
>
> But hidden inside this 'simple' system are 10+ subsystems, 20+ interfaces, decisions about sensors, networks, ECUs, safety mechanisms, fault handling...
>
> The difference between a $327 million failure and a successful system often comes down to architecture.
>
> Today, we learn how to architect automotive systems systematically. We transform requirements into structure.
>
> Welcome to Session 5: System Design and Architecture."

### **Closing (Last 2 minutes):**
Return to ACC image:

> "We started with this seemingly simple ACC system. You now understand what's really inside:
>
> - CONOPS that drives design decisions
> - Context boundaries and 20+ interfaces
> - Functional decomposition into 6 major functions
> - Physical architecture with distributed ECUs
> - Design principles: modularity, redundancy, fail-safe
> - Trade studies that justified sensor choices
> - Baselines and design freeze that enable development
>
> Architecture is where we make the system real. It's the bridge from WHAT (requirements) to HOW (implementation).
>
> Your exercise: Apply these same principles to Lane Keeping Assist. Make deliberate, justified architecture decisions.
>
> In Session 7, we'll take this architecture and analyze how it operates. We'll allocate behavior through functional flow diagrams.
>
> See you then!"

---

## 📈 Learning Objectives Mapping to Assessment

| Session Objective | Assessment Method | Success Criteria |
|-------------------|-------------------|------------------|
| Explain CONOPS and its role | Exercise Part 1 | 3 realistic operational scenarios developed with context, sequence, behavior |
| Define system context and boundaries | Exercise Part 2 | Context diagram with clear boundary, ≥8 interfaces identified |
| Apply design principles | Exercise Part 3 | Architecture demonstrates modularity, hierarchy, appropriate redundancy |
| Develop system architecture | Exercise Part 3 | Functional decomposition + physical architecture with traceable allocation |
| Compare architecture patterns | Discussion/Q&A | Can explain when to use distributed vs centralized, layered vs pipe-filter |
| Understand design freeze and CM | Knowledge check (Q&A) | Can explain when to freeze, what gets frozen, change control process |
| Perform trade studies | Exercise Part 4 | Complete trade study with alternatives, criteria, scoring, sensitivity, rationale |

---

**End of Session 5 Framework**
**Next:** Session 6 (Case Study 1) or Session 7 (Operational and Functional Analysis)
