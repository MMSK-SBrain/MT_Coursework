# SESSION-09H — CAN Box Assembly & Testing Lab
## ECU Hardware Repair (ECUHR) | Module 4: PCB Repair & Soldering Skills
### Day 9 — Hands-On Block | Duration: 90 minutes

---

## Session Identity

| Field | Detail |
|---|---|
| Session Code | SESSION-09H |
| Module | 4 — PCB Repair & Soldering Skills |
| Day | 9 |
| Block | Hands-On |
| Duration | 90 minutes |
| Delivery Mode | Workshop — individual bench stations |
| Prerequisites | SESSION-09T complete; students can solder SMD and through-hole; CAN box schematic understood |

---

## Learning Outcomes

By the end of this session, students will be able to:

- **so-4-3-3:** Test a suspected faulty IC using in-circuit voltage measurements referenced against datasheet specifications and draw a valid inference
- **so-4-4-2:** Assemble the CAN box PCB from kit components following the correct build sequence and with all joints meeting IPC-610 Class 2 criteria
- **so-4-4-3:** Test the completed CAN box for correct VCC rail voltage, correct CANH/CANL idle voltages, and functional CAN bus communication

---

## Equipment List — Per Student Station

### Assembly Equipment
| Item | Quantity | Notes |
|---|---|---|
| Temperature-controlled soldering iron | 1 | Hakko FX-888D or equivalent |
| Chisel tip 2mm | 1 | For SOIC-8 TJA1050 |
| Conical tip 0.5mm | 1 | For component touch-up |
| CAN box PCB (unpopulated) | 1 | Pre-drilled, pad-printed, tracked and numbered |
| Component kit — sealed bag | 1 | See component manifest below |
| Solder — Sn63/Pb37 0.6mm | 1 reel | |
| No-clean flux pen | 1 | |
| Desoldering braid 2mm | 1 short roll | For corrections |
| Reverse-action tweezers | 1 pair | For SMD placement |
| Fine-point tweezers | 1 pair | |
| IC insertion tool or fine flathead screwdriver | 1 | For DIP MCU pin alignment |
| USB microscope or loupe (10x) | 1 | Shared between 2 if necessary |
| IPA dropper and cotton swabs | 1 set | Post-solder cleaning |
| Tip cleaner — brass wool | 1 | |
| Safety glasses | 1 pair | Mandatory |
| Fume extractor | 1 | Running before session starts |

### Testing Equipment
| Item | Quantity | Notes |
|---|---|---|
| Multimeter | 1 | Per student or shared pair |
| 12V DC bench power supply (or battery pack) | 1 per 2 students | For powering the completed CAN box |
| USB cable (matching CAN box USB connector type) | 1 | For MCU firmware and PC connection |
| Laptop with CAN software installed | 1 per 2 students | CAN bus viewer/terminal software — pre-installed |
| CAN bus simulator or second CAN box (for communication test) | 1 per 4 students | Alternatively: two student CAN boxes connected together |

### Component Manifest — CAN Box Kit (Per Student)
| Reference | Component | Value/Part Number | Package |
|---|---|---|---|
| U1 | CAN Transceiver | TJA1050T or SN65HVD230 | SO-8 |
| U2 | Microcontroller | PIC18F2580 (or equivalent) | DIP-28 |
| VR1 | Voltage Regulator | L7805CV or LM7805 | TO-220 or TO-92 |
| C1 | Decoupling capacitor | 100nF ceramic | 0805 |
| C2 | Decoupling capacitor | 100nF ceramic | 0805 |
| C3 | Filter capacitor | 10µF electrolytic | Through-hole radial |
| C4 | Filter capacitor | 10µF electrolytic | Through-hole radial |
| R1 | Termination resistor | 120Ω ¼W | 0805 |
| R2 | Standby pull-down | 10kΩ ¼W | 0805 |
| R3, R4 | MCU pull-up/pull-down | values per schematic | 0805 |
| X1 | Crystal oscillator | 8MHz or 16MHz | HC-49/S through-hole |
| C5, C6 | Crystal load capacitors | 22pF ceramic | 0805 |
| J1 | OBD-II or DB9 connector | Per kit variant | Through-hole |
| J2 | USB connector | USB Type-B or Type-C | Through-hole or SMD |
| J3 | DC power jack (if no OBD power) | 5.5/2.1mm barrel | Through-hole |
| LED1 | Power indicator LED | 3mm red | Through-hole |
| R5 | LED current limit | 470Ω | 0805 |

Note: exact values and part numbers should be confirmed against the schematic version provided with the kit. The above is representative — instructors must verify against their specific kit.

---

## Safety Notes

- Safety glasses mandatory from iron switch-on.
- Do not connect the CAN box to a power supply until the instructor has performed a pre-power visual check. A single solder bridge on the power rail will short 12V to 5V or GND and destroy the voltage regulator and potentially the CAN transceiver.
- When testing with 12V power supply: ensure the bench power supply current limit is set to 200mA maximum before first power-up. This protects the CAN box and bench supply in the event of a wiring fault.
- The TJA1050 operates on 5V. Do not connect the CANH or CANL pins directly to a 12V supply.
- Electrolytic capacitors C3 and C4 are polarised. If installed backwards, they will fail when power is applied — potentially with a burst and chemical release. Confirm polarity before soldering.
- Lead-containing solder in use. Wash hands before leaving.

---

## Instructor Demonstration — Before Students Begin (12 minutes)

The demonstration covers one complete assembly sequence using the first two component stages. It does not need to cover the entire build — students have the schematic and the build sequence from the theory session. The goal is to set technique expectations and highlight the two most likely error points.

### Demo Sequence

**Demo 1: SMD passives — R1 120Ω on 0805 footprint (4 minutes)**

"I'm soldering the first passive — the termination resistor. 0805, same technique as Day 7. Flux, tack one end, flux the other, solder the other, reflow the tack.

The thing I want you to notice: I'm checking the component value on the body before it goes on the board. For resistors, read the code. For 120Ω: the code is 121 — 12 followed by one zero. For 10kΩ: 103 — 10 followed by three zeros. Check before you place. A wrong value resistor installed on this board will prevent the circuit from working and is very difficult to diagnose once the board is complete."

Solder R1 under overhead camera. Final inspection under camera.

---

**Demo 2: SO-8 CAN transceiver — TJA1050 (5 minutes)**

"Same SO-8 process as the SOIC-8 from Day 7. Align pin 1. Tack corner. Drag solder. The critical point here is pin 1 orientation.

The TJA1050 in SO-8: pin 1 is marked by a dot on the IC body. The PCB has a pin 1 indicator — either a dot, a triangle, or a chamfered corner on the pad silk screen. These must match.

If pin 1 is installed backwards, the IC is powered in reverse — it will be destroyed on power-up. There is no diagnostic test that tells you an IC is in backwards; it just fails immediately. Check orientation before tacking. Check it again before drag soldering. Check it once more before calling for sign-off."

Place TJA1050 on demo board, check orientation, tack two corners, begin drag soldering. Inspect under camera. Do not need to complete all four sides live — demonstrate one side and bridge fixing.

---

**Demo 3: DIP MCU placement (3 minutes)**

"The microcontroller is through-hole DIP. Larger pins, more forgiving. But there are 28 pins. Before you insert the IC, check that all 28 pins are straight. DIP ICs are often stored with pins slightly splayed. If one pin is bent, it will fold under the package when you push it into the board and will not make electrical contact — but it will look fine from the top.

Straighten pins before insertion: hold one row of pins flat against a hard surface and gently press to bring them to 90 degrees. Repeat the other side.

Insert the IC until it sits flat against the PCB surface. Then flip the board and solder every pin. Don't rush the through-hole solder — these joints need to flow through the hole, not just sit on the surface."

Demonstrate pin straightening with physical DIP IC. Insert into demo board without soldering.

---

## Student Practical — Step-by-Step Procedure

### Stage 1: Component Check and Organisation (5 minutes)

Before soldering begins:

1. Open component kit bag. Place all components in the provided sorting tray or onto the printed component reference sheet.
2. Cross-reference each component against the component manifest. Confirm all items are present.
3. Identify C3 and C4 (electrolytic capacitors). Confirm the polarity stripe (negative leg marked with stripe on the body, shorter lead is negative).
4. Identify U1 (TJA1050) — confirm the pin 1 dot on the IC body is visible.
5. Check the DIP MCU pins for straightness.
6. If any component is missing or damaged: report to instructor before proceeding. Do not substitute with a component from the parts bin without instructor approval — values must match the schematic.

**Instructor note:** Do one group check of all stations at this point. Confirm every student has identified the polarity of the electrolytic capacitors correctly. This check prevents one of the most common assembly failures.

---

### Stage 2: Solder SMD Passives — R1, R2, R3, R4, C1, C2, C5, C6 (15 minutes)

Work in order: resistors first, then ceramic capacitors.

For each SMD passive (0805):
1. Check component value against schematic reference.
2. Apply flux pen to both pads.
3. Place component. Confirm correct orientation (resistors are non-polarised; ceramic caps are non-polarised; use only value identification, not polarity, for these).
4. Tack one end. Inspect. Solder the other end. Reflow tack.
5. Inspect under loupe — concave fillet both ends, no bridges.
6. Tick off the reference designator on the schematic/build checklist.

Critical check: R1 (120Ω termination) and R2 (10kΩ standby pull-down) are both 0805 but different values. Do not swap. Read the body code before placing. R1 = 121, R2 = 103.

C5 and C6 (crystal load capacitors) are 22pF ceramic — typically marked 220. Do not confuse with C1/C2 (100nF, marked 104).

**Call instructor for Stage 2 sign-off** before proceeding.

---

### Stage 3: Solder Voltage Regulator VR1 (5 minutes)

The voltage regulator may be through-hole (TO-220) or SMD (SOT-223) depending on kit variant. Instructions below cover TO-220.

1. Identify VR1 orientation. The L7805 TO-220 has three pins: Input (left), GND (centre), Output (right) when viewed from the front face. Confirm against schematic before insertion.
2. Insert VR1 into the PCB footprint. Bend legs gently if needed to align with holes.
3. Confirm the device is flush with the PCB or as specified on the silkscreen (some boards have the regulator standing off the board for thermal reasons).
4. Solder all three pins from the back of the board — standard through-hole joint: iron to pin and pad, solder feeds in, concave fillet forms on the pad face.
5. Trim excess pin length with side cutters.
6. Inspect joints under loupe.

---

### Stage 4: Solder CAN Transceiver U1 — TJA1050 in SO-8 (15 minutes)

This is the SMD IC stage. Same technique as SOIC-8 in SESSION-07H.

1. Apply flux generously to all 8 pad positions.
2. Place TJA1050 on pads. Align pin 1 dot on IC to pin 1 indicator on PCB.
3. Inspect alignment under loupe. All 8 pins on pads.
4. Tack pin 1 (minimum solder). Check alignment. Tack pin 5 (diagonal corner).
5. Inspect: IC flat, not rocking, pin 1 aligned.
6. Drag solder pins 1–4. Apply flux first. Drag. Inspect. Fix bridges.
7. Drag solder pins 5–8. Apply flux first. Drag. Inspect. Fix bridges.
8. Final inspection: all 8 pins, individual fillets, no bridges, no cold joints.
9. Continuity check with multimeter: probe adjacent pin pairs along both rows — should NOT beep.
10. Call instructor for Stage 4 sign-off.

**Common mistakes at this stage:**
- Pin 1 reversed — emphasised in demo. If discovered after soldering: requires full hot air removal, pad cleaning, and restart. The instructor should verify orientation at the alignment step before tacking.
- Bridge between pin 2 (GND) and pin 3 (VCC) — this shorts the supply. Would be detected in Stage 8 pre-power continuity check. Must be fixed before power-up.

---

### Stage 5: Solder Crystal X1 and Load Capacitors (5 minutes)

1. Insert crystal X1 into through-hole footprint (non-polarised — either orientation is correct).
2. Solder both leads from the back. Trim excess.
3. C5 and C6 (22pF ceramic) should already be soldered from Stage 2. Confirm both are present on the board near the crystal footprint.

---

### Stage 6: Solder MCU U2 — PIC18F2580 in DIP-28 (10 minutes)

1. Straighten all 28 pins (14 per side) before insertion.
2. Confirm pin 1 orientation on the MCU body (notch on one end of the package = pin 1 end) matches pin 1 notch on PCB silkscreen.
3. Insert MCU into footprint. Push gently until the package is fully seated against the PCB.
4. Turn board over.
5. Solder all 28 pins. Through-hole technique: iron to pin and pad, solder in from the side, brief contact, withdraw. Each pin should take 1–2 seconds.
6. Re-tin iron tip every 10 pins.
7. Inspect all 28 pins from back of board — each joint should show a full concave fillet around the pin.
8. Turn board over. Inspect from front — all pins should be slightly raised above the PCB surface (confirming they seated correctly and did not fold under).

**Common mistakes at this stage:**
- One or more pins not soldered — easy to miss on a 28-pin DIP. Count the solder joints.
- Solder bridge between adjacent pins — common when solder is added to a cool pin. Flux + iron to fix.
- Pin not fully inserted — the IC sits high on one side. Remove, straighten, reinsert.

---

### Stage 7: Solder Through-Hole Components — C3, C4, X1, LED1, R5 (8 minutes)

1. Solder electrolytic capacitors C3 and C4. CRITICAL: confirm polarity before insertion. The negative stripe on the capacitor body goes to the square pad on the PCB (or as marked on silkscreen). Wrong polarity = component failure on power-up.
2. Solder LED1. LEDs are polarised — longer lead is anode (positive). Check against schematic.
3. Solder R5 (LED current-limiting resistor, 470Ω) — non-polarised.
4. Trim all leads flush with bottom of PCB using side cutters.
5. Inspect all joints.

---

### Stage 8: Solder Connectors — J1 (OBD/DB9), J2 (USB), J3 (Power Jack) (7 minutes)

Connectors are soldered last.

1. Insert J1 (OBD-II or DB9) into footprint. Confirm correct orientation — the connector face must exit the board edge, not face inward.
2. Solder mechanically — one pin first, check the connector is flush against the PCB, then solder all remaining pins.
3. Repeat for J2 (USB connector) and J3 (power jack).
4. Connector joints carry mechanical load as well as electrical current. Each pin must have a complete, strong through-hole fillet.

---

### Stage 9: Pre-Power Visual Inspection and Continuity Checks (5 minutes)

Before any power is applied:

1. Visual inspection under loupe — entire board. Look for: solder bridges, missing joints, components shifted off pads, upside-down polarised components.
2. Continuity check — VCC to GND: probe the 5V rail to GND with multimeter in continuity mode. Should NOT beep. A beep indicates a bridge somewhere on the 5V rail or a failed component (backwards electrolytic, IC shorted).
3. Continuity check — 12V input to GND: should NOT beep.
4. Continuity check — CANH to CANL: should read approximately 120Ω (the termination resistor) — use resistance mode.
5. If any check fails: find and fix the fault before calling the instructor. Do not apply power until all checks pass.
6. Call instructor for pre-power sign-off.

**Instructor pre-power check:** The instructor inspects every board before power is applied. This check looks for: reversed ICs, reversed electrolytics, bridges on power rails, missing joints on the voltage regulator. No board is powered without this check.

---

### Stage 10: Power-Up and Testing (10 minutes)

**Test 1 — VCC Rail (2 minutes)**

1. Connect 12V bench supply to J3 (power jack). Confirm polarity correct.
2. Set bench supply current limit to 200mA before switching on.
3. Switch on bench supply.
4. Immediately observe: does current draw spike above 200mA (suggesting a short)? If yes: switch off immediately, return to Stage 9 fault-finding.
5. If current is within expected range (typically 50–150mA with MCU running): proceed.
6. Probe VR1 output with multimeter (positive probe to the 5V rail test point or VCC pad on U1, negative probe to GND). Should read 4.75–5.25V.
7. Record reading in sign-off checklist.
8. If VCC reads 0V or 12V: switch off. Investigate regulator circuit.

**Test 2 — CANH and CANL Idle Voltages (2 minutes)**

1. With 12V power applied and CAN box running (no CAN bus connected):
2. Probe J1 CANH pin with multimeter positive, GND with negative. Should read approximately 2.5V.
3. Probe J1 CANL pin with multimeter positive, GND with negative. Should read approximately 2.5V.
4. If both read 2.5V: the CAN transceiver is powered and in recessive idle state. Record readings.
5. If one or both read 0V: check VCC at TJA1050 pin 3. If VCC present but output pins are 0V, TJA1050 may be faulty or in standby (check standby pin R2 connection).

**Test 3 — Communication Test (5 minutes)**

1. Connect USB cable to J2 and laptop.
2. Open CAN software on laptop. Configure baud rate to match the kit default (typically 500kbps or 125kbps — check kit documentation).
3. To test two-box communication: connect two CAN boxes together — CANH to CANH, CANL to CANL, GND to GND. Send a frame from one box. Confirm the other box's PC software receives it.
4. Alternatively: connect to a vehicle OBD-II port. With ignition on, the vehicle CAN network should be active. The software should show received frames.
5. Record: communication test passed/failed.
6. If USB is recognised but no CAN frames received: check connector pinout, check baud rate configuration, check CAN software COM port assignment.

---

## Student Sign-Off Checklist

### Stage 2 — SMD Passives
- [ ] All SMD passives soldered — R1, R2, R3, R4, C1, C2, C5, C6
- [ ] Values confirmed before placement (R1 = 120Ω, R2 = 10kΩ)
- [ ] All joints: concave fillet, no bridges
- [ ] No cold joints

### Stage 4 — CAN Transceiver TJA1050
- [ ] Pin 1 correctly oriented to PCB marker
- [ ] All 8 pins have individual fillets
- [ ] No bridges between adjacent pins
- [ ] Continuity check between adjacent pins: no shorts

### Stage 6 — MCU DIP
- [ ] Pin 1 orientation correct
- [ ] All 28 pins soldered
- [ ] All joints have full through-hole fillets
- [ ] No bridges between adjacent pins

### Stage 7 — Through-Hole Passives
- [ ] C3 and C4 polarity correct — confirmed before soldering
- [ ] LED1 polarity correct
- [ ] All leads trimmed flush

### Stage 8 — Connectors
- [ ] All connector pins soldered with strong through-hole joints
- [ ] Connectors seated flush against board

### Stage 9 — Pre-Power Continuity
- [ ] VCC to GND: no short
- [ ] 12V input to GND: no short
- [ ] CANH to CANL: reads 120Ω

### Stage 10 — Testing
- [ ] VCC rail: _____ V (target: 4.75–5.25V)
- [ ] CANH at idle: _____ V (target: ~2.5V)
- [ ] CANL at idle: _____ V (target: ~2.5V)
- [ ] Communication test: PASS / FAIL
- [ ] Current draw at power-up: _____ mA (target: <200mA)

**Instructor sign-off:** ___________________ Date: ____________

---

## Fault-Finding Reference — If Tests Fail

| Symptom | First Check | Second Check |
|---|---|---|
| VCC reads 0V | VR1 input voltage present? | VR1 pins soldered correctly, correct orientation |
| VCC reads 12V | VR1 failed open — do not connect to transceiver | Replace VR1 |
| Current >200mA on power-up | Short on 5V rail — check bridge on U1 or C3/C4 reversed | Check R2 (standby resistor) value |
| CANH/CANL = 0V, VCC correct | TJA1050 pin 1 reversed | R2 missing (standby pin floating) |
| CANH/CANL = 5V and 0V asymmetric | TJA1050 damaged | Check soldering on all 8 pins |
| VCC and CANH/CANL correct, no communication | USB not recognised — driver issue | CAN baud rate mismatch |
| No communication, USB recognised | MCU not running — crystal not oscillating | MCU pin 1 orientation, crystal load caps present |

---

## Debrief — Last 10 Minutes

Instructor brings all students together. Every completed CAN box is placed on the front bench.

If any box has not yet passed the communication test, use the remaining time for group fault-finding: instructor asks the class for diagnosis suggestions, then resolves.

**Debrief questions:**

1. "What was the hardest part of the build — and why?" Expected variation: some say the TJA1050 SO-8, some say the 28-pin DIP (counting pins), some say the pre-power checks.
2. "What value resistor did you measure between CANH and CANL? Why is it 120Ω and not 60Ω?" Expected: the CAN box has one termination. 60Ω appears on a two-endpoint network where both terminators are connected.
3. "If CANH read 0V at idle, what would be your first diagnostic step?" Expected: check VCC at the TJA1050 VCC pin.
4. "You now have a functional CAN bus tool that you built and tested. What would you use it for on a real ECU job?"

**Key message to close:**

"You just completed Module 4. In three days you have gone from soldering theory to building a diagnostic instrument. The skills you used today — reading a schematic, following a build sequence, testing against specifications — are the same skills you will use on every board repair for the rest of your career. The component values change. The schematic changes. The method does not.

The CAN box is yours to keep. Use it."

---

## Module 4 Completion Summary — For Instructor Records

At the end of SESSION-09H, confirm the following outcomes are achieved for each student:

| Outcome Code | Description | Evidence |
|---|---|---|
| so-4-1-1 | Selects correct tools and materials for ECU SMD work | SESSION-07H sign-off card |
| so-4-1-2 | Solders 0402, 0603, 0805, SOIC-8 correctly | SESSION-07H sign-off card |
| so-4-1-3 | Removes SMD components with braid, pads intact | SESSION-07H sign-off card |
| so-4-2-1 | Configures hot air station for SOIC/QFP removal | SESSION-08H sign-off card |
| so-4-2-2 | Removes QFP without pad damage | SESSION-08H sign-off card |
| so-4-2-3 | Solders replacement QFP using drag technique | SESSION-08H sign-off card |
| so-4-2-4 | Explains BGA construction and rework scope | SESSION-08T verbal check |
| so-4-3-1 | Decodes IC markings and locates datasheets | SESSION-09T verbal check |
| so-4-3-2 | Reads datasheet for key specifications | SESSION-09T verbal check |
| so-4-3-3 | Tests IC in-circuit against datasheet | SESSION-09H sign-off card |
| so-4-4-1 | Explains CAN box schematic | SESSION-09T verbal check |
| so-4-4-2 | Assembles CAN box from kit | SESSION-09H sign-off card |
| so-4-4-3 | Tests CAN box — voltage and communication | SESSION-09H sign-off card |

Any outstanding outcomes must be noted and a remediation plan agreed with the student before Module 5 begins.

---

## Notes for Instructor

- The pre-power instructor check at Stage 9 is the single most important safety and quality gate in this session. Allow time for it. A student whose board passes all pre-power checks and fails on communication is in a diagnostic learning situation. A student whose board passes a reversed electrolytic is in a safety situation.
- If a student's board fails communication but passes all voltage tests: this is a genuinely useful diagnostic exercise. Resist the urge to solve it for them — ask the right questions, let them work through the fault-finding table.
- The completed CAN box belongs to the student. This is stated in the debrief script. It is a significant motivator throughout the build. Confirm this with course management before the session starts.
- MCU firmware status must be confirmed before the session: if firmware needs to be flashed, the flashing procedure must be included as a step between Stage 6 and Stage 9, and the laptop must have the appropriate IDE or flashing tool installed.
- If time runs short (box not complete by 80 minutes): prioritise getting every student to Stage 9 pre-power continuity check. Testing can continue at the start of Module 5 Day 10 if needed — but every student should complete the soldering today.
