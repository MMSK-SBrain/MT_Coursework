# SESSION-20T: Airbag & SRS Systems — Safety Theory
## Instructor-Led Story Framework

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 9 — Security & Safety Systems + Final Assessment
**Day:** 20 of 20 | **Session:** Theory (Session A)
**Duration:** 75–90 minutes
**PPT Target:** 26–30 slides
**Format:** Instructor-led narrative. Safety protocol must be demonstrated live, not just presented on slides.

**Session Learning Outcomes:**

| SO Code | Description | Bloom |
|---------|-------------|-------|
| ECUHR-SO-9-3-1 | Explain SRS system architecture (crash sensors, clock spring, squib circuits, pre-tensioners) and the consequences of incorrect repair | Understand |
| ECUHR-SO-9-3-2 | Apply safety protocol before working on an SRS module: battery disconnect, wait period, squib resistance verification | Apply |
| ECUHR-SO-9-3-3 | Distinguish between crash data (hard faults — replacement required) and non-deployment faults (soft faults — resettable) | Analyze |

**CO Alignment:** co-4 (Configure and recover vehicle security and safety systems)

---

## SESSION CONTEXT

**Previous session (Day 19H):** Students completed key cloning and immobilizer lab. They have experienced one high-stakes security procedure and now understand what "highest-liability repair work" means in practice.

**This session (Day 20T):** The final theory session of the course. Airbag and SRS (Supplemental Restraint System) work. If key programming carries legal liability, SRS work carries physical liability — the risk of unintended deployment, which can cause serious injury or death. This session establishes the non-negotiable safety framework before any student touches an SRS component in the lab.

**Next session (Day 20H):** Hands-on SRS PCB repair activity, followed by the final practical assessment. The safety rules established in this session apply for the remainder of the course and for every SRS job in the student's career.

**Critical tone instruction:** This is the one session in the course where safety content comes before technical content, not as a footnote but as the opening structure. Do not rush through it. The consequences of someone deploying an airbag in the workshop are severe. The goal is not to frighten students but to build the kind of disciplined respect that characterises professional SRS technicians. Set this tone from the first sentence.

---

## STORY ARC OVERVIEW

```
SETUP              TRIGGER              RISING ACTION                  CLIMAX             RESOLUTION
This is the        What happens         Part 1: SRS                    Crash data         Preparation
session that       when an airbag       architecture &                 vs soft            for hands-on
starts with        deploys              component                      faults —           assessment
safety             unexpectedly?        functions                      the key            this afternoon
                                        Part 2: Safety                 decision
                                        protocol — step by step
```

---

## PART 1 — SETUP: SAFETY BEFORE EVERYTHING ELSE
**Slides 1–5 | ~12 minutes | Tone: Serious, measured, no drama — just weight**

---

### SLIDE 1: Title Slide
**Visual:** Plain slide. White text on dark background. "Module 9: Session 2" and "Day 20 — SRS Systems: Safety, Architecture & Fault Classification". No imagery. This should feel different from a normal session opening. The instructor should pause before speaking.

**Instructor Script:**
> "Good morning. Today is Day 20. The last day of this course.
>
> This morning's session is the one where we start with safety before anything else. Not safety as a disclaimer before the real content — safety as the content. For the next 30 minutes I am going to walk you through the SRS safety protocol in detail, and I want you to understand not just what the rules are, but why each rule exists and what happens when it is not followed.
>
> SRS work is airbag work. An airbag that deploys in the workshop — because correct safety procedures were not followed — can break bones, cause permanent eye damage, rupture eardrums, or kill. These are documented incidents in workshops that did not enforce safety procedures.
>
> I am not saying this to alarm you. I am saying it so that what I teach you this morning has the weight it deserves. These are not arbitrary rules. Every step of the safety protocol exists because someone, somewhere, learned its necessity the hard way."

---

### SLIDE 2: Why SRS Repair Is Fundamentally Different
**Visual:** Comparison table. Three rows. Column headers: "System", "Consequence of Mistake". Rows: (1) ECU Diagnostics — DTC or no-start, fixable. (2) Immobilizer / Key Programming — Legal liability, data issue, fixable. (3) SRS — Unintended deployment, potential serious injury or death, not fixable.

**Instructor Script:**
> "Throughout this course, we have categorised mistakes by their consequences. Early in Module 5, a diagnostic mistake meant an incorrect fault conclusion — addressable with more data and better process. In Module 6, a programming mistake meant a corrupted ECU — recoverable with boot mode programming. Yesterday, a key programming mistake could mean a locked key slot or a legal exposure — serious, but recoverable.
>
> SRS mistakes are categorically different. If you inadvertently trigger an airbag squib during a repair, the consequence is not a DTC. It is an airbag deploying at approximately 300 kilometres per hour within a metre of whoever is holding the component. It cannot be un-deployed.
>
> This is why SRS work requires a mandatory, non-skippable safety protocol. Not a recommended protocol. A mandatory one. In this session you will learn that protocol in detail. In the lab this afternoon you will execute it as the first action of every SRS procedure. Tomorrow — when you are in industry — it will be the first action of every SRS job, every time, without exception."

---

### SLIDE 3: Legal and Professional Context for SRS Work
**Visual:** Three points in large text: (1) Liability — SRS incorrectly repaired is a legal exposure. (2) Insurance — insurer may refuse claims if SRS was serviced by non-authorised repairer. (3) Professional standard — OEM and independent repair guidelines all require the protocol.

**Instructor Script:**
> "Beyond the physical risk, SRS work carries significant professional and legal weight.
>
> Liability: if a vehicle involved in an accident has a previously serviced SRS system that did not function correctly, and it can be established that the repair was improper, the technician and the workshop can be held directly liable. In some jurisdictions, improper SRS work that results in a fatality during a subsequent accident can result in criminal charges.
>
> Insurance: vehicle insurers require that safety-critical repairs are performed to OEM specifications. An SRS module reprogrammed without the correct procedure, or crash data cleared from a module that should have been replaced, can void the vehicle's insurance coverage for a subsequent accident.
>
> Professional standard: the IAEA — International Automotive Engineering Association — and equivalent industry bodies in most countries define SRS work as safety-critical repair. The qualification, tooling, and procedure standards are defined. They align with what I will teach you today.
>
> Carry this with you: a vehicle you have worked on may be involved in an accident three years from now. Your work record must show that you followed correct procedure. Your documentation protects you."

---

### SLIDE 4: Today's Session Structure
**Visual:** Three-part roadmap. Part 1: SRS Architecture (~25 minutes). Part 2: Safety Protocol — mandatory and non-skippable (~25 minutes). Part 3: Fault classification — crash data vs soft faults (~20 minutes). Preview of afternoon lab.

**Instructor Script:**
> "Here is today's structure.
>
> We open with SRS system architecture. I will walk you through every component in a complete SRS system: crash sensors, the SRS ECU, clock spring, squib circuits, pre-tensioners. You need to understand what each component does before the safety protocol makes technical sense.
>
> Then we cover the safety protocol. Step by step. I will also physically demonstrate each step, not just describe it. Safety protocol cannot be learned from a slide. You must see it performed correctly.
>
> Then we cover fault classification — the critical decision that determines whether a damaged SRS module can be repaired and reset, or whether it must be replaced. This is a judgment call you will need to make on every SRS job.
>
> After the break, the hands-on session begins with 45 minutes of SRS PCB repair activity, followed by the final practical assessment."

---

### SLIDE 5: A True Account of What Non-Compliance Looks Like
**Visual:** Text-only slide. Neutral, professional language. Describe a generalised workshop incident: "A technician at an independent workshop began removing a steering wheel to access the clock spring. The battery had not been disconnected. The backup capacitor in the SRS module had not been allowed to discharge. When the clock spring connector was disturbed, the squib circuit received sufficient voltage to fire. The driver airbag deployed. The technician sustained facial lacerations, a broken nose, and permanent partial hearing loss in one ear."

**Instructor Script:**
> "I want to close the opening with a real account. This is not a hypothetical. Incidents like this are documented in workshop safety records across multiple countries.
>
> The technician was experienced. They had removed steering wheels many times. They had worked on SRS components before without incident. They skipped the battery disconnect step because they were in a hurry and it had not caused a problem in the past.
>
> The backup capacitor in the SRS ECU can retain sufficient charge to fire a squib for up to ten minutes after the battery is disconnected. If the battery is not disconnected at all, the capacitor is fully charged at all times.
>
> The outcome in this case was survivable injury. Not every case is.
>
> The safety protocol I am about to teach you is not bureaucratic overhead. It is the difference between going home at the end of your shift and not going home. Treat it accordingly."

---

## PART 2 — RISING ACTION PART 1: SRS ARCHITECTURE
**Slides 6–15 | ~25 minutes | Tone: Technical, systematic**

---

### SLIDE 6: SRS System Overview — The Complete Picture
**Visual:** Vehicle diagram with SRS components labelled in their physical locations: front crash sensors (behind bumper), side crash sensors (B-pillars or door frames), central SRS ECU (under centre console), clock spring (steering column), driver airbag (steering wheel hub), front passenger airbag (dashboard), side curtain airbags (roof rail), pre-tensioners (seatbelt retractors, B-pillars).

**Instructor Script:**
> "A complete SRS system in a modern mid-range vehicle has approximately 10 to 20 individual components. I will cover each category.
>
> The system has two functional layers: the sensing layer — components that detect a crash event — and the protection layer — components that deploy in response to that event.
>
> The central SRS ECU sits between the two layers. It receives data from all sensors, evaluates whether a deployment threshold has been exceeded, and fires the squib circuits of the appropriate protection components.
>
> From a repair perspective, every one of these components has a live pyrotechnic or electromechanical firing circuit. That is why the safety protocol applies not just to the SRS ECU itself, but to any connector in the SRS circuit — including sensors, clock spring connectors, and seatbelt pre-tensioner connectors."

---

### SLIDE 7: Crash Sensors — The Trigger Layer
**Visual:** Three sensor types shown: (1) front impact accelerometer (behind bumper), (2) side impact accelerometer (B-pillar or door), (3) rollover sensor (tilt/gyro, often integrated into SRS ECU). Circuit diagram showing sensor wiring back to SRS ECU.

**Instructor Script:**
> "Crash sensors are MEMS accelerometers — microelectromechanical systems that measure deceleration. They are typically distributed around the vehicle at locations chosen to maximise sensing speed for the crash type they are designed to detect.
>
> Front sensors are mounted in or just behind the front bumper assembly, or at the firewall. They detect frontal deceleration events. In a 50 km/h frontal crash, the deceleration pulse must be detected and evaluated within 15 to 20 milliseconds for the airbag to inflate before the occupant contacts it.
>
> Side sensors are mounted in the B-pillar, door sill, or inside the door itself. Side impact crashes have less crumple zone distance, so detection and deployment must occur even faster — typically within 8 to 12 milliseconds.
>
> Rollover sensors are typically integrated into the SRS ECU module as a separate gyroscope or tilt sensor. They detect angular rotation rate and cumulative tilt.
>
> For repair purposes: a damaged or displaced crash sensor — for example, a front sensor bent in a minor collision — will generate a soft fault DTC for that sensor channel. This is a resettable fault once the sensor is replaced and correctly mounted. Sensor replacement does not affect the SRS ECU's crash data status."

---

### SLIDE 8: The Central SRS ECU — Function and Location
**Visual:** SRS ECU block diagram showing internal components: accelerometer array (backup sensing), microprocessor, EEPROM, backup power capacitor, squib firing circuits (one per deployment channel), communication interface (CAN).

**Instructor Script:**
> "The central SRS ECU is the most complex and the most critical component in the system. It contains several functions in one housing.
>
> Internal accelerometer array: most SRS ECUs contain their own accelerometers as a central sensing reference, in addition to the external distributed sensors. This provides a validation check — the external sensor must agree with the internal sensor before deployment occurs. This prevents false deployments from a single damaged external sensor.
>
> Microprocessor: evaluates all sensor inputs in real time against deployment algorithms. These algorithms determine not just whether a crash occurred, but whether its severity and direction warrant deployment of specific airbag channels.
>
> EEPROM: stores the deployment event log. This is the crash data — the record that indicates whether deployment has occurred. We will cover this in detail in Part 3.
>
> Backup power capacitor: this is the component that makes the safety protocol mandatory. The capacitor stores enough energy to fire at least one squib circuit even if the vehicle battery is disconnected. It is designed specifically to ensure airbag deployment can occur even if the battery cable is severed in the crash. Its discharge time after battery disconnection is typically 30 seconds to 10 minutes, depending on the vehicle — always check the OEM specification.
>
> Squib firing circuits: one dedicated driver circuit per deployment channel. Each fires a precise electrical pulse — approximately 1.5 to 2 amperes for 1 to 3 milliseconds — through the squib to initiate the propellant."

---

### SLIDE 9: The Clock Spring — The Steering Wheel Connection
**Visual:** Clock spring diagram showing: housing, ribbon cable spiral, terminals. Mounted location in steering column. Wiring paths through clock spring: horn, airbag squib, steering angle sensor, cruise control, audio controls.

**Instructor Script:**
> "The clock spring — also called a spiral cable or coil cable — is the component that maintains electrical continuity between the stationary steering column and the rotating steering wheel.
>
> As the steering wheel turns, the flat ribbon cable inside the clock spring coils and uncoils, allowing approximately three full turns of the wheel in each direction before the cable runs out of travel. If the clock spring is wound beyond its range — which happens when the steering wheel is removed and reinstalled without centring the clock spring — the ribbon cable tears. This is one of the most common SRS fault causes following steering wheel removal.
>
> The clock spring carries the driver airbag squib wiring. If the clock spring ribbon tears or the connector corrodes, the squib circuit opens. The SRS ECU detects the open circuit as a resistance fault on the squib channel and logs a DTC. This is a soft fault — no deployment has occurred — and it is resettable once the clock spring is replaced and the circuit is verified.
>
> The clock spring also carries the horn circuit, steering angle sensor wiring on more recent vehicles, and any steering wheel-mounted control buttons. A failed clock spring may therefore present as multiple apparently unrelated symptoms: no horn, airbag DTC, steering angle sensor fault, and non-functional wheel-mounted controls.
>
> Safety note: the clock spring connector carries live squib wiring. It is an SRS connector. The battery disconnect and wait procedure applies before this connector is touched."

---

### SLIDE 10: Squib Circuits — The Firing Mechanism
**Visual:** Squib circuit schematic showing: SRS ECU squib driver IC, two-wire squib circuit (+ and - fire wires), squib (resistive bridge wire inside inflator), inflator propellant. Resistance value labelled: 2–3 Ω typical. Short-circuit protection note shown.

**Instructor Script:**
> "A squib is a small electro-explosive device. At its core is a very fine bridge wire — a resistance element with a typical value of 2 to 3 ohms. When the SRS ECU fires a squib, it passes approximately 1.5 to 2 amps through the bridge wire for 1 to 3 milliseconds. The bridge wire heats to ignition temperature and ignites a small pyrotechnic primer charge. This in turn ignites the main propellant — typically sodium azide in older systems, or a tetrazole-based compound in newer systems. The propellant combustion generates nitrogen gas at high pressure, inflating the airbag in approximately 30 to 40 milliseconds.
>
> For the repair technician, two squib resistance values matter:
>
> Normal (2–3Ω): the squib is intact and its resistance is within specification. The circuit is deployable but only when the SRS ECU deliberately fires it.
>
> Too low (below 1Ω, approaching 0Ω): the squib wires are shorted together. This is a critical hazard — a shorted squib circuit means that a small stray voltage, a capacitor discharge, or even static electricity could potentially fire the squib. If you measure a shorted squib: treat the situation as a potential deployment hazard. Do not work in the deployment zone. Consult OEM guidelines for the specific vehicle before proceeding.
>
> Too high (open circuit, megaohms): the squib wire has broken. The airbag will not deploy when needed. This is a safety failure in the other direction — the vehicle's occupant protection is compromised. The module must be replaced.
>
> The measurement tool matters: squib resistance must be measured with a high-impedance multimeter. A standard test light, a low-impedance buzzer, or a low-impedance multimeter can supply enough current through the squib circuit to fire it. This is not a hypothetical risk. This has caused deployments. Only use a purpose-built squib resistance meter or a high-impedance digital multimeter specifically confirmed as safe for squib measurement by your tool supplier."

---

### SLIDE 11: Pre-Tensioner Circuits
**Visual:** Pre-tensioner location in seatbelt assembly (inside B-pillar housing at retractor). Pyrotechnic mechanism cross-section. Squib-type firing circuit shown — identical architecture to airbag squib. Pre-tensioner resistance typical value: 2–3Ω.

**Instructor Script:**
> "Seatbelt pre-tensioners use the same pyrotechnic squib circuit architecture as airbags. They are controlled by the same SRS ECU. The same safety protocol applies.
>
> A pre-tensioner fires a small charge that instantly retracts the seatbelt webbing by approximately 100 to 150mm in the first 10 to 15 milliseconds of a crash, pulling the occupant firmly into the seat before the belt loads. This was covered in Module 9's safety systems context yesterday.
>
> For the repair technician, the pre-tensioner connector is located inside the B-pillar, typically accessible after removing the lower B-pillar trim. Like the clock spring connector, it is an active squib circuit — the battery disconnect and wait procedure applies before this connector is touched.
>
> After any collision where pre-tensioners have fired — visible as a retracted belt that will no longer extend — the pre-tensioner assembly must be replaced. It is single-use. A fired pre-tensioner is electrically open-circuit and will generate an SRS DTC confirming deployment. It cannot be reset without replacement."

---

### SLIDE 12: SRS System Communication — CAN Integration
**Visual:** CAN bus diagram showing SRS ECU connected to powertrain CAN or body CAN. Other nodes that receive SRS data shown: instrument cluster (warning lamp), ECM (post-crash fuel cutoff), BCM (post-crash door unlock). Direction of data flows labelled.

**Instructor Script:**
> "The SRS ECU communicates on the vehicle's CAN bus. This integration has several implications for the repair technician.
>
> Post-crash management: when the SRS ECU detects a deployment event, it broadcasts messages on the CAN bus to other modules. The ECM — engine management ECU — receives a post-crash fuel cutoff command that stops the fuel pump to prevent fire risk. The BCM receives a command to unlock all door locks, enabling emergency access to the vehicle.
>
> Instrument cluster: the airbag warning lamp in the cluster is typically driven by the cluster module interpreting SRS DTC status data from the CAN bus, not wired directly to the SRS ECU. This means a CAN communication fault between the SRS ECU and the cluster can cause the airbag warning lamp to illuminate even if the SRS system itself has no fault.
>
> Diagnostic access: the SRS ECU is accessed via OBD-II CAN (ISO 15765-4) for DTC reading and module programming. If the SRS ECU cannot communicate on the CAN bus — due to a failed CAN transceiver in the module — the first symptom will be inability to connect with a scan tool, accompanied by the airbag warning lamp illuminated. This is a soft fault (no crash data) and is a repairable hardware fault — the CAN transceiver IC on the SRS PCB is the likely failure component."

---

### SLIDE 13: What Happens During Deployment — The Event Sequence
**Visual:** Timeline diagram. T=0: crash begins. T=10ms: sensors detect threshold. T=15ms: SRS ECU fires squib. T=30ms: propellant combustion, gas generation begins. T=40ms: airbag fully inflated. T=50ms: occupant contacts airbag. T=80ms: maximum compression. T=120ms: airbag deflated, event complete. T=200ms: SRS ECU writes deployment record to EEPROM.

**Instructor Script:**
> "The entire deployment event takes approximately 120 milliseconds from initial crash detection to complete airbag deflation. To put that in perspective: the blink of an eye takes 150 to 400 milliseconds. The airbag has fully inflated and is already deflating before a human can complete a voluntary blink.
>
> The event that is most important for the repair technician is at the end: at approximately 200 milliseconds after the crash event begins, the SRS ECU writes a permanent deployment record to its internal EEPROM. This record is the crash data — the hard fault.
>
> Once this record is written, it cannot be cleared by any diagnostic tool command alone. The data is written to a protected area of the EEPROM designed specifically to be non-clearable by standard diagnostic reset commands. We will cover what this means for repair decisions in Part 3."

---

### SLIDE 14: Component Failure Modes — What Fails and How
**Visual:** Table — four rows, one per failure category. Columns: Component, Failure Mode, SRS DTC Type, Repair Action.

**Instructor Script:**
> "Let me catalogue the main failure modes you will encounter in SRS repair work."

**PPT Content Block:**
```
SRS COMPONENT FAILURE MODES

Component          | Failure Mode                              | DTC Type  | Action
-------------------|-------------------------------------------|-----------|-----------------------------
Crash sensor       | Damaged by minor collision, displaced,    | Soft fault| Replace sensor, reset DTC
                   | connector corroded                        |           |
Clock spring       | Ribbon cable torn, connector corroded     | Soft fault| Replace clock spring
                   | (most common: after wheel removal)        |           | (re-centre before fitting)
Squib circuit      | Open circuit (fired/broken wire)          | Soft fault| Replace airbag/pretensioner
                   | Short circuit (shorted wires)             | (if only  | — TREAT SHORT AS HAZARD
                   |                                           | resistance|
                   |                                           | fault,    |
                   |                                           | no crash) |
SRS ECU — comms    | CAN transceiver IC failed                 | Soft fault| Replace transceiver IC
SRS ECU — power    | Backup capacitor degraded                 | Soft fault| Replace capacitor on PCB
SRS ECU — crash    | Deployment event occurred, EEPROM written | Hard fault| Replace SRS module
  data             |                                           |           | (cannot be legitimately reset)
Pre-tensioner      | Fired (deployed) — open circuit           | Hard fault| Replace pretensioner assembly
```

---

### SLIDE 15: SRS Hardware Repair — Scope and Limits
**Visual:** Two-column layout: "What can be repaired" vs "What must be replaced". Clear boundary drawn.

**Instructor Script:**
> "Before we go to the safety protocol, I want to be explicit about the scope of SRS hardware repair — what is legitimate and what is not.
>
> SRS ECU PCB components that can be repaired: power supply capacitors (backup capacitor degradation is a common age-related failure), communication interface ICs (CAN transceiver failures), resistors and small passives around the diagnostic and communication circuits. These are components in the monitoring and communication sections of the ECU, not in the deployment firing circuits themselves.
>
> What must be replaced, not repaired: any SRS ECU that has recorded a deployment event. Any squib circuit component that has been fired — airbag module, pre-tensioner assembly. Any crash sensor that has been physically deformed or impacted.
>
> What is absolutely outside repair scope: the squib firing driver ICs and deployment circuit components within the SRS ECU. These are the components that actually fire the squibs. There is no legitimate field repair of the deployment circuit hardware. If the deployment circuit has failed, the ECU is replaced. The reason: there is no safe way to test-fire a squib circuit to verify repair in a workshop environment. The repair cannot be validated without deploying the airbag, which is a destructive test."

---

## PART 3 — RISING ACTION PART 2: MANDATORY SAFETY PROTOCOL
**Slides 16–21 | ~22 minutes | Tone: Procedural, authoritative, demonstrated live**

---

### SLIDE 16: The Safety Protocol — Why Every Step Exists
**Visual:** Five-step protocol listed in order. Each step has a brief "reason" line in smaller text below it. This is the master reference slide for the protocol.

**Instructor Script:**
> "Here is the SRS safety protocol. I am going to go through each step, explain why it exists, and then demonstrate it. There are five steps. They are always performed in this order. None can be skipped."

**PPT Content Block:**
```
SRS SAFETY PROTOCOL — MANDATORY SEQUENCE

Step 1: DISCONNECT BATTERY NEGATIVE TERMINAL
Reason: Removes primary power from SRS system, preventing capacitor from
        being recharged if disturbed, and cutting all squib drive voltage from ECU.

Step 2: WAIT — MINIMUM 30 SECONDS (CHECK OEM SPEC — MAY BE UP TO 10 MINUTES)
Reason: Backup capacitor must discharge to below firing threshold.
        Capacitor retains charge after battery disconnection.
        Do not touch any SRS connector until wait time is complete.

Step 3: DISABLE OTHER SOURCES (OPTIONAL — HIGH-RISK VEHICLES)
Reason: Some vehicles have an auxiliary power input or super-capacitor.
        Check OEM service data for vehicles with stop-start or hybrid systems.

Step 4: SQUIB RESISTANCE CHECK BEFORE RE-CONNECTION
Reason: Verify squib circuits are within specification before reconnecting battery.
        Confirms no short (deployment hazard) or open (safety failure).
        Performed AFTER work is complete and BEFORE battery reconnection.

Step 5: RECONNECT BATTERY AND VERIFY NO SRS FAULTS
Reason: First power-on after repair must be observed for warning lamp behaviour.
        Clear any soft faults generated during disconnection.
        Confirm no new faults generated by repair work.
```

---

### SLIDE 17: Step 1 — Battery Disconnect (Demonstrated Live)
**Visual:** Photograph of battery negative terminal removal. Correct tool shown. Cable positioned away from terminal, not resting on it.

**Instructor Script:**
> "Step one: disconnect the battery negative terminal.
>
> [INSTRUCTOR ACTION: If a vehicle or engine bay mock-up is present in the classroom, physically demonstrate this step. If not, use a bench mock-up with a battery and terminal clamp.]
>
> Always disconnect negative first, reconnect negative last. This is standard electrical safety — disconnecting negative first prevents accidental shorting of the positive terminal to chassis ground during the removal operation.
>
> After removal, position the cable so it cannot fall back onto the terminal. If working in a confined space, tape the terminal clamp back with electrical tape or use a dedicated battery disconnect lock-out clip. The battery terminal must not be able to inadvertently reconnect during your work period.
>
> Do not disconnect positive only and leave negative connected. The negative terminal is the chassis ground reference for the entire vehicle electrical system. Disconnecting only positive still leaves all chassis-grounded circuits energised relative to the battery negative potential."

---

### SLIDE 18: Step 2 — The Wait Period (Most Often Skipped, Most Dangerous to Skip)
**Visual:** Timer diagram showing capacitor discharge curve. X axis: time after battery disconnect. Y axis: capacitor voltage. Horizontal dashed line at "firing threshold voltage". Curve shows time to reach below threshold. OEM wait times shown: "minimum 30 seconds SAE guideline — some OEMs specify 10 minutes". Callout: "Do not estimate. Check the vehicle's service manual."

**Instructor Script:**
> "Step two: the wait period. This is the step most commonly skipped, and it is the most dangerous step to skip.
>
> The backup capacitor in the SRS ECU is designed to hold enough charge to fire squib circuits even if the battery cable is severed in a crash. It is good at its job. After you disconnect the battery, this capacitor begins to discharge passively through the SRS ECU's internal resistive bleed circuit.
>
> The SAE minimum recommendation is 30 seconds. Most modern vehicles fully discharge the capacitor to below firing threshold within 30 to 60 seconds under normal conditions. However, if the SRS ECU has a fault in its discharge circuit, or if the vehicle is at extremely low ambient temperature, discharge can take significantly longer.
>
> Some OEM service manuals — particularly for vehicles with larger backup capacitors or redundant SRS power supplies — specify a 10-minute wait. Toyota's service information for some hybrid SRS systems specifies waiting up to 10 minutes after both the 12V battery and the high-voltage system have been disabled.
>
> The rule: check the OEM service manual for the specific vehicle and follow its wait time. If you do not have access to the service manual and cannot verify the wait time, use 10 minutes. Ten minutes is safe for all vehicles. Thirty seconds may not be for all vehicles.
>
> What to do during the wait: do not touch any SRS connector. Do not touch the clock spring. Do not touch any squib circuit harness. Walk away. Do your paperwork, talk to the customer, make notes. After the timer, come back and begin work."

---

### SLIDE 19: Step 3 — Hybrid and Stop-Start Systems (Additional Precaution)
**Visual:** High-voltage orange warning label (ISO 6469 standard). Diagram showing 12V battery disconnect AND high-voltage main service disconnect locations on a hybrid/BEV vehicle.

**Instructor Script:**
> "Step three applies specifically to vehicles with stop-start systems, mild hybrid, full hybrid, or battery electric drivetrains.
>
> In these vehicles, there may be a secondary power source — a 48V mild hybrid battery, a high-voltage battery pack, or a dedicated SRS backup supply — that is not de-energised by disconnecting the 12V battery alone.
>
> For any hybrid or electric vehicle, the SRS safety procedure must include: (1) disconnecting the 12V battery negative, (2) disabling the high-voltage system via the service disconnect plug or vehicle-specific shutdown procedure, and (3) waiting the OEM-specified time for both systems to discharge.
>
> On conventional petrol and diesel vehicles without any form of hybrid system, step three does not apply. Skip it and proceed to work after the wait time.
>
> If you are working on a hybrid and are not trained on that specific high-voltage system, stop the SRS work and refer to a technician with HV qualification. The SRS work and the HV system are separate disciplines, but the HV shutdown is required before SRS work can begin safely."

---

### SLIDE 20: Step 4 — Squib Resistance Check (Demonstrated Live)
**Visual:** Multimeter setup for squib resistance measurement. High-impedance meter shown (impedance >10MΩ). Probes positioned at squib connector pins. Normal range labelled: 2–3Ω (verify against OEM spec). Warning box: "Never use a test light. Never use a low-impedance buzzer. Never use a standard continuity mode."

**Instructor Script:**
> "Step four: squib resistance verification. This is performed after your repair work is complete and before you reconnect the battery.
>
> The purpose: confirm that every squib circuit you have worked on — or may have disturbed — is within the correct resistance specification before the SRS system is re-energised.
>
> [INSTRUCTOR ACTION: Demonstrate using a squib dummy load or disconnected airbag module connector. Show the correct multimeter selection and the measurement process.]
>
> The correct tool: a digital multimeter with input impedance above 10 megaohms, in resistance measurement mode. The reason for high input impedance: a low-impedance measurement current passing through a squib that has a short circuit could complete the firing circuit. High-impedance measurement limits the probe current to a value that cannot fire a squib even in a shorted condition.
>
> What you are looking for:
>
> 2 to 3 ohms — normal. The squib is intact. The circuit is safe to re-energise.
>
> Below 1 ohm — shorted squib or shorted wiring. This is a deployment hazard. Do not reconnect the battery. Identify and resolve the short before proceeding.
>
> Above 10 ohms or open circuit — open-circuit squib or broken wiring. The airbag will not deploy when needed. This must be corrected before reconnecting.
>
> Measure every squib circuit you have disturbed during the repair. On a full airbag module replacement, measure the driver airbag, the passenger airbag, both front seat side airbags, both curtain airbags, and both pre-tensioners. Check every one. Do not assume a connector that 'feels seated' is electrically correct."

---

### SLIDE 21: Step 5 — Battery Reconnection and First Power-On Observation
**Visual:** First power-on sequence shown: Instrument cluster lighting up, airbag warning lamp path (should illuminate briefly and then extinguish). Warning lamp remaining on = system fault requiring investigation. Notes on what to expect vs what to investigate.

**Instructor Script:**
> "Step five: reconnect the battery and observe the first power-on.
>
> Reconnect the negative terminal. Turn the ignition to the ON position. Observe the instrument cluster.
>
> Expected behaviour: the airbag warning lamp illuminates during the power-on self-test — approximately 3 to 6 seconds — and then extinguishes. This confirms the SRS ECU has completed its self-test, found no stored faults that prevent normal operation, and is in the armed, operational state.
>
> What to investigate:
>
> Airbag warning lamp remains illuminated: the SRS ECU has detected a fault. Connect the scan tool, read the DTCs, and identify whether the fault is new (generated by your work) or pre-existing. Address before returning the vehicle.
>
> Airbag warning lamp does not illuminate at all during power-on: either the warning lamp bulb or LED has failed, or there is a cluster communication fault. This is not normal — investigate before returning the vehicle. A vehicle where the SRS warning lamp has been tampered with to prevent illumination is not roadworthy.
>
> After the first power-on observation, connect the scan tool for a full SRS system scan. Read all DTCs in the SRS module. Any code that reads as a 'current fault' must be resolved before the vehicle is returned. Codes that read as 'stored' from a pre-existing condition should be discussed with the customer and documented on the work record."

---

## PART 4 — RISING ACTION PART 3: CRASH DATA VS NON-DEPLOYMENT FAULTS
**Slides 22–27 | ~20 minutes | Tone: Diagnostic, analytical**

---

### SLIDE 22: The Critical Decision — Replace or Repair and Reset?
**Visual:** Decision tree. Starting point: "SRS warning lamp illuminated". Two main branches: "Hard fault (crash data present)" and "Soft fault (no crash data)". Hard fault leads to "Replace module". Soft fault leads to "Diagnose and repair, then reset".

**Instructor Script:**
> "Every SRS job where the warning lamp is illuminated comes down to one decision: does this module have crash data, or does it have a non-deployment fault?
>
> The answer determines everything. If crash data is present, the module must be replaced. If crash data is absent, the fault is diagnosable and resettable.
>
> There are no legitimate exceptions to the first rule for modules with confirmed deployment. An SRS module that has recorded a deployment event has fired squib circuits. Those circuits may have deformed components, partially exhausted capacitors, or subtly altered firing characteristics. You cannot confirm that the module will perform correctly in a subsequent crash. Resetting the deployment record does not restore the module to a safe deployable state.
>
> I am aware that software tools exist that can clear crash data from an SRS EEPROM by directly writing to the protected memory area. I want to be direct: using such tools to clear deployment records from a module and return it to a vehicle is not legitimate repair. It is falsifying the vehicle's safety record and bypassing a legally mandated safety function. If that vehicle is subsequently involved in an accident and the airbags fail to deploy, you are directly liable."

---

### SLIDE 23: Hard Faults — Crash Data and Deployment Records
**Visual:** Hex editor screenshot (example/simulated) showing SRS EEPROM data with deployment flag highlighted. Contrast: before crash (flag = 0x00), after crash (flag = 0xA5 or similar non-zero value). DTC examples shown: "B0001 — Driver Airbag Deployed", "B0002 — Passenger Airbag Deployed", "B0051 — Left Side Pretensioner Deployed".

**Instructor Script:**
> "Hard faults are stored in the SRS EEPROM as permanent deployment records. When the SRS ECU fires its squib circuits, it writes a deployment flag and event data to a protected memory area. This data includes: which channels fired, the event timestamp if the module has a real-time clock, and in some systems a pre-crash data log capturing sensor readings in the seconds before impact.
>
> In scan tool diagnostics, hard faults appear as DTCs with descriptions indicating deployment — 'airbag deployed', 'pretensioner fired', or 'crash event stored'. These codes cannot be cleared by a standard DTC clear command. If you attempt a clear and the code immediately returns, this is confirmation of a hard fault with deployment record.
>
> A subtlety: on some vehicles, particularly where the crash threshold was triggered by a severe pothole or off-road impact without actual airbag deployment — for example, a vehicle that bottomed out severely or hit a large object — the SRS ECU may have logged a crash event even though no squibs fired. In these cases, the correct procedure is: (1) verify no squibs fired by inspecting all airbag modules and pre-tensioners physically, (2) consult OEM guidance for that vehicle on whether the event record is resettable without replacement, and (3) document the decision fully. Some OEMs permit reset in these edge cases with documented procedure. Most do not."

---

### SLIDE 24: Soft Faults — Non-Deployment Faults
**Visual:** Table listing the most common soft faults. Columns: DTC Description, Cause, Repair Action, Resettable?

**Instructor Script:**
> "Soft faults are all the fault conditions that do not involve deployment — component failures, circuit faults, and communication issues. These are diagnosable, repairable, and resettable."

**PPT Content Block:**
```
COMMON SRS SOFT FAULTS

DTC Description              | Most Common Cause                    | Repair Action                    | Resettable?
-----------------------------|--------------------------------------|----------------------------------|------------
Driver airbag circuit        | Clock spring ribbon torn/corroded    | Replace clock spring             | Yes
open circuit                 | Squib wire broken                    |                                  |
Driver airbag circuit        | Clock spring short, wiring short     | Identify short — HAZARD PROTOCOL | Yes (after repair)
short to ground              |                                       |                                  |
Passenger airbag             | Connector not fully seated           | Reseat connector, verify Ω       | Yes
circuit resistance fault     | Squib degraded                       | Replace passenger airbag module  |
Front crash sensor           | Sensor damaged (minor collision)     | Replace sensor                   | Yes
communication fault          | Connector corroded                   |                                  |
Side crash sensor fault      | Sensor dislodged (door work)         | Refit/replace sensor             | Yes
Pre-tensioner circuit        | Connector displaced (trim removal)   | Reseat connector, verify Ω       | Yes
open/short                   | Pre-tensioner fired                  | Replace assembly (hard fault)    | No if fired
SRS ECU no communication     | CAN transceiver IC failure           | PCB repair — CAN transceiver IC  | Yes (after repair)
SRS ECU power fault          | Backup capacitor degraded            | PCB repair — capacitor           | Yes (after repair)
Squib resistance out of      | Squib partially degraded             | Replace module/assembly          | Yes after replacement
spec (not deployed)          |                                      |                                  |
```

---

### SLIDE 25: Reading the Scan Tool — Determining Hard vs Soft
**Visual:** Side-by-side comparison of scan tool screens. Left: hard fault presentation — "B0001 Stored — Non-Erasable. Airbag deployed." Right: soft fault presentation — "B0051 Current — Clock spring open circuit. Erasable."

**Instructor Script:**
> "Your scan tool will typically indicate whether a fault is erasable or non-erasable. Look for these descriptors in the DTC detail view:
>
> 'Non-erasable', 'Permanent', or 'Deployment record' — hard fault. Module must be replaced.
>
> 'Current', 'Stored', 'Pending', or 'History' — these are standard fault status descriptors that indicate the fault is a soft fault and the DTC is clearable after repair.
>
> If in doubt: attempt to clear the DTC using a standard diagnostic clear command. If it re-appears immediately after clearing — within the same ignition cycle, before any further fault condition is present — this confirms a hard fault. A soft fault that has been repaired will clear and stay clear.
>
> Never interpret a successful DTC clear as confirmation of repair. A fault that clears but returns after the next ignition cycle confirms the underlying condition is still present."

---

### SLIDE 26: The Airbag Warning Lamp — What It Actually Means
**Visual:** Dashboard instrument cluster with airbag/SRS warning lamp highlighted. Three states shown: (1) Brief illumination on power-on — normal self-test. (2) Continuous illumination — fault present. (3) No illumination at all — lamp failure or tampering.

**Instructor Script:**
> "The airbag warning lamp is the primary communication between the SRS system and the driver. A brief illumination on ignition-on followed by extinction is normal and confirms the SRS ECU has completed its self-test and found no faults.
>
> Continuous illumination means the SRS ECU has detected and stored at least one fault. The airbag system may or may not be operational depending on the nature of the fault. The driver should be advised not to operate the vehicle until the fault is diagnosed.
>
> No illumination at all during the power-on self-test is a fault condition in itself. Either the warning lamp driver circuit has failed, the cluster communication has failed, or — in vehicles where previous owners have tampered — the lamp has been removed to hide an SRS fault. If you encounter a vehicle where the airbag light does not illuminate during the self-test sequence, investigate before beginning any other SRS work. The system may have a pre-existing fault that is being concealed.
>
> From a professional liability standpoint: returning a vehicle to a customer with the airbag warning lamp illuminated, without explicit customer acknowledgement that the fault is known, documented, and accepted, is not acceptable professional practice. The customer must be told, the decision documented, and if they choose to drive with a known SRS fault, that choice must be their documented decision — not a default outcome of an incomplete repair."

---

### SLIDE 27: SRS Fault Classification — Summary Flowchart
**Visual:** Complete decision flowchart. Starting point: "Airbag warning lamp illuminated". Branches cover: DTC read, crash data check, squib circuit test, sensor and connector check. Leaf outcomes: Replace module, Replace component, PCB repair, Reset and verify.

**Instructor Script:**
> "Here is the complete SRS fault classification flowchart. This is your diagnostic workflow for every SRS job.
>
> Start: airbag warning lamp illuminated — connect scan tool, read all SRS DTCs.
>
> Is there a deployment record or non-erasable DTC? Yes — replace the SRS module. End of diagnostic path.
>
> No deployment record: read all DTCs for circuit faults. Identify which channel — driver airbag, passenger airbag, side airbag, pre-tensioner, sensor.
>
> Squib circuit fault (open or short): perform squib resistance measurement following safety protocol. If open: trace the circuit from connector to squib — likely clock spring or wiring harness. If shorted: treat as deployment hazard — investigate before any further work.
>
> Sensor fault: check connector seating and sensor physical condition. Replace if damaged.
>
> SRS ECU communication fault: check CAN bus. If bus is active and other modules communicate, the SRS ECU itself has a fault — check CAN transceiver IC on the PCB.
>
> After repair: perform safety protocol step 4 (squib resistance check), reconnect battery, verify no new DTCs, confirm warning lamp extinguishes. Document all findings and actions."

---

## PART 5 — RESOLUTION: CONSOLIDATION AND FINAL ASSESSMENT PREVIEW
**Slides 28–30 | ~8 minutes**

---

### SLIDE 28: SRS Quick-Reference Card
**Visual:** Compact reference. Two tables. Table 1: Safety Protocol Steps. Table 2: Hard Fault vs Soft Fault comparison.

**Instructor Script:**
> "Here is your reference card for SRS work. Photograph it."

**PPT Content Block:**
```
SRS SAFETY PROTOCOL — QUICK REFERENCE

Step 1: Disconnect battery negative
Step 2: Wait (minimum 30 sec — check OEM spec, may be 10 min)
Step 3: Disable HV system if hybrid (not required on conventional vehicles)
Step 4: Squib resistance check BEFORE battery reconnection (use high-impedance meter, expect 2–3Ω)
Step 5: Reconnect battery, observe warning lamp, scan tool verification

SQUIB RESISTANCE GUIDE:
2–3Ω: Normal — proceed
<1Ω: SHORTED — deployment hazard, do not reconnect battery, investigate
>10Ω / open: OPEN CIRCUIT — airbag will not deploy, repair required

FAULT CLASSIFICATION:
HARD FAULT (crash data): Non-erasable DTC, deployment record → REPLACE MODULE
SOFT FAULT (no deployment): Erasable DTC, circuit fault, sensor fault → DIAGNOSE + REPAIR + RESET
```

---

### SLIDE 29: This Afternoon — Lab and Final Assessment Structure
**Visual:** Timeline. 0–45 min: SRS PCB repair activity. 45–90 min: Final Practical Assessment (individual work, timed).

**Instructor Script:**
> "This afternoon has two distinct parts.
>
> First 45 minutes: SRS PCB repair activity. Working in pairs, you will diagnose and repair a hardware fault on an SRS module PCB. The fault will be a component-level defect — a degraded backup capacitor or a failed CAN transceiver — of the type we have discussed this morning. You will follow the safety protocol before touching any component, perform the repair, and verify function.
>
> Last 45 to 60 minutes: Final Practical Assessment. This is individual work. You will receive an ECU with an unknown planted fault and a wiring diagram for that ECU. You have 45 to 60 minutes to: set up the ECU on the bench, establish communication, diagnose the fault using systematic methods, and either execute the repair or propose the correct repair procedure with supporting evidence.
>
> Everything from the last 20 days is in scope. The fault types span diagnostics, PCB repair, programming, CAN bus, and the security systems from yesterday and today.
>
> The assessment brief will be read to you in full at the start of the assessment period. Scoring criteria will be on the desk beside your ECU."

---

### SLIDE 30: Final Session Close
**Visual:** Single line — "The last 20 days have given you the skills. The next job puts them to work."

**Instructor Script:**
> "Twenty days ago, you knew how to diagnose. By Day 9 you could solder. By Day 14 you could program. By Day 16 you understood the bus networks. Today you understand the systems where a mistake is not just a fault code.
>
> The assessment this afternoon is not a test of memory. It is a test of process. The students who do well will not be the ones who have memorised every chip type or every DTC. They will be the ones who approach an unfamiliar ECU with a systematic method: bench setup first, communication second, DTCs third, split-half isolation fourth, repair fifth, verify last.
>
> Take everything you have learned and apply it in that order. That is what professional ECU repair looks like.
>
> Good luck this afternoon. Let us take a short break before we start the lab."

---

## PPT DESIGN GUIDANCE

**Visual style:** Maintain dark background consistent with Day 19. Introduce a subtle red accent colour for safety-critical content — squib hazard warnings, deployment threshold callouts, the hard fault replacement rule. Red should be used sparingly so it carries meaning when it appears.

**Key slides to emphasise:**
- Slide 5 (real account): pause after reading. Do not rush. Let it land.
- Slide 16 (protocol steps): students should photograph this
- Slide 18 (wait period): this is where accidents happen — spend more time here than the slide count suggests
- Slide 20 (squib resistance check): demonstrate live, not just described
- Slide 28 (quick-reference card): students should photograph this

**Animations:** Use a build animation on Slide 6 (SRS overview diagram) — add each component one at a time as you describe it. Use a build animation on Slide 13 (deployment timeline) — advance through each time marker. Otherwise static.

**Live demonstrations required:**
- Battery disconnect procedure (Step 1 and Step 2 context) — use a battery and terminal clamp on the bench
- Squib resistance measurement (Step 4) — use a dummy load or disconnected squib connector
- These are not optional. The safety protocol cannot be taught by slide alone.

---

## INSTRUCTOR NOTES

**Pacing:** Do not compress the safety protocol section to create more time for architecture. If time is short, compress architecture (Slides 6–15 can be condensed to 18 minutes). The safety protocol section must receive its full time — if students do not understand why each step exists, they will skip steps under time pressure in the workshop.

**Common student misconceptions:**
- "The 30-second wait is just a precaution" — it is not. It is based on capacitor discharge time. Reinforce: some OEMs require 10 minutes. Check the service manual. Always.
- "If the scan tool clears the code, the module is fine" — wrong for hard faults. A deployment record that clears and immediately returns is a hard fault. The module must be replaced.
- "I can repair the squib firing circuit components in the SRS ECU" — this is out of scope and outside professional standards. Squib driver ICs are not a field-repairable component.

**Handling student questions about crash data clearing tools:**
Students may ask about tools that claim to clear crash data from any SRS EEPROM. Address directly: "Yes, these tools exist. Using them to clear deployment records and return a module to a vehicle is falsifying the vehicle's safety record. It is not a legitimate repair technique. If you use such a tool and that vehicle is later in an accident where the airbag fails, you are directly legally liable. The correct action is always module replacement after deployment."

**Final assessment preview emphasis:** Slide 29 should be delivered clearly — some students may not have absorbed the assessment format from earlier information. Make sure they understand: (1) individual work, no collaboration, (2) timed (45–60 minutes), (3) all modules in scope, (4) the process is assessed, not just the answer.

---

## SESSION SUCCESS CRITERIA

Students leave able to:
- Name all major SRS components and describe the function of each
- Execute the five-step SRS safety protocol from memory without reference to the slide
- Measure squib resistance correctly using a high-impedance meter and interpret the result
- Distinguish between crash data (hard fault — replace) and non-deployment fault (soft fault — diagnose and reset) using scan tool DTC data
- Describe at least four common SRS soft fault causes and the correct repair action for each

**Most importantly:** Students enter the afternoon's hands-on session with an absolute, reflexive commitment to the safety protocol. It must be the first action before any SRS component is touched. No exceptions, no shortcuts, no "it'll be fine".

---

**End of SESSION-20T Framework**
**Next:** SESSION-20H-Airbag-Final-Assessment-Framework.md
