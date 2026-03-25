# SESSION-03H: Sensor & Actuator Testing
## Hands-On Session — Day 3, Block 2

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 2 — Tools & Measurement Mastery
**Session Type:** Hands-On / Workshop Practical
**Duration:** 90 minutes
**Delivery Format:** Bench-based practical; students in pairs sharing one station

---

## Session Outcomes

By the end of this session, students will be able to:

- **so-2-3-2:** Trace a complete signal path from sensor through harness to ECU pin using a wiring diagram
- **so-2-3-3:** Identify power supply and ground reference pins and verify them physically
- **so-2-4-1:** Test TPS and MAP sensor using multimeter and compare to specification
- **so-2-4-2:** Test crankshaft/camshaft position sensor output using oscilloscope
- **so-2-4-3:** Measure actuator coil resistance and verify against specification

---

## Equipment and Materials List

### Per Station (pair of students)
- 1x Professional true-RMS multimeter with fine-tip probes (Fluke 87V or equivalent)
- 1x Oscilloscope, 2-channel, minimum 20MHz bandwidth, with x10 probe and ground clip
- 1x Training ECU board powered by bench supply (5V regulated + 12V, current-limited)
- 1x TPS sensor (known-good; 3-wire potentiometer type) with breakout harness
- 1x MAP sensor (known-good; 3-wire; 1-bar absolute pressure range) with breakout harness
- 1x CKP sensor simulator board (produces VR-style sine wave at variable frequency via function generator, and Hall-effect square wave output switchable on same board) — OR — actual VR sensor driven by rotating reluctor wheel on motor trainer
- 1x Fuel injector (known-good; either peak-and-hold 2–5Ω type or saturated 12–16Ω type; labelled at station)
- 1x Bench vacuum pump (hand-operated, with gauge) for MAP sensor testing
- 1x Sensor specification card (laminated, one per station) — see Appendix A
- 1x Wiring diagram exercise sheet from Session-03T (students use same sheet)
- ESD wrist strap and mat
- Fine-tip back-probe pins (2 per station)
- Sticky notes for labelling test point positions

### Shared Resources
- Injector waveform reference poster (mounted on wall near instructor bench)
- Spare fine-tip probe sets
- Extra CKP simulator boards (in case of failure)
- Service manual pages for any sensor types not fully covered on the station spec card

---

## Safety Briefing (4 minutes — mandatory, fast-paced)

> "Briefing. Three minutes, then we start."

> "ESD straps on before boards are on. No exceptions — I will be watching."

> "The injector in this session is connected to a real 12V driver. When you test the coil resistance, the board must be OFF and the capacitors discharged. If you probe the injector connector with the board powered and your meter in resistance mode, you will blow the meter fuse. I will not replace meter fuses during the session — you will finish the session without a meter."

> "The MAP sensor test involves a hand vacuum pump. Do not exceed 500 mmHg (about 67 kPa) of vacuum on this sensor — it will over-range and may be damaged. The pump gauge shows mmHg. The limit is marked in red on the pump gauge."

> "The oscilloscope ground clip and the multimeter black probe both go to the ECU signal ground reference point — marked in green on your station card. Not to the bench, not to the frame of the board. Signal ground only."

> "Questions? No? Let's go."

---

## Warm-Up Task — Pre-Measurement Wiring Diagram Trace (10 minutes)

This is not optional and must be completed before students touch any sensor or probe.

> "You have your wiring diagram sheet from this morning. Before you pick up a probe, I need each pair to complete the following:"

Project or write on whiteboard:

```
Using your wiring diagram, write down:
1. The ECU connector and pin number for TPS signal output
2. The ECU connector and pin number for MAP sensor supply
3. The ECU connector and pin number for CKP+ signal
4. The sensor ground splice number and the ECU pin it connects to
5. The ECU pin that drives Injector 1 low-side
```

> "Write these in the answer box at the bottom of your diagram sheet. When you have all five, call me over before you start Task 1."

*Instructor: walk the room. This should take 5–7 minutes. If a pair cannot find a signal after 5 minutes, give one directional hint: "Look at the MAP sensor component block — trace the wire toward the ECU connector." Do not give pin numbers directly.*

*Do not allow any pair to begin Task 1 until their five answers have been verified. Incorrect answers: send them back to the diagram for another 2 minutes with a specific clue.*

---

## Instructor Pre-Activity Demonstration (8 minutes)

Perform at the instructor bench with document camera. Students observe.

**Demonstrate TPS sweep test:**
- Connect TPS to the bench supply (5V supply, sensor ground).
- Connect multimeter in DC voltage mode across the TPS signal and ground terminals.
- Slowly rotate the TPS shaft from full closed to full open.
- Show the smooth voltage sweep from approximately 0.5V to 4.5V on the multimeter.
- Then introduce a deliberate dead spot: have a faulty TPS prepared that shows a dropout mid-sweep (reading drops to 0.1V suddenly then recovers).

> "Here is what a dead spot looks like. The voltage is sweeping smoothly — 1.2V, 1.8V, 2.4V — then suddenly drops to 0.1V for about 10 degrees of travel, then recovers. That 10-degree dead zone will produce a P0123 or similar code intermittently. You find it by sweeping slowly and watching the meter continuously — or better, with a scope so you can see the shape of the sweep over time."

**Demonstrate back-probe technique:**
- Show a 3-pin sensor connector with breakout harness.
- Insert the fine back-probe pin into the signal wire terminal from the back without damaging the seal.
- Connect the multimeter probe to the back-probe pin.

> "This is how you probe live connectors without piercing insulation. The fine pin slips in alongside the terminal without spreading the connector seal. When you're done, it leaves no damage. You do not stab through the wire insulation with a standard probe tip."

---

## Student Procedure

Students work in pairs. Switch operator/recorder roles between tasks.

---

### TASK 1: Trace a Signal Path and Verify Supply and Ground (15 minutes)

**Objective:** Use the wiring diagram to identify test points, then physically verify the 5V sensor supply and sensor ground reference at the ECU connector.

**Step 1:** With the training board powered OFF, locate the ECU main connector on the board. Identify the pin positions using the pin numbering diagram on your station card (pin 1 location is marked).

**Step 2:** From your wiring diagram answer box, identify the ECU pin number for the sensor 5V supply. Physically count to that pin on the connector. Place a sticky note label on or beside it: "5V SUPPLY".

**Step 3:** Identify the ECU pin for sensor ground. Label it: "SENSOR GND".

**Step 4:** Power the board ON (bench supply, 5V regulated rail + 12V rail). Wait 10 seconds for stabilisation.

**Step 5:** Set your multimeter to DC voltage, finest range (or 20V range — confirm resolution is at least 10mV).

**Step 6:** Black probe to the SENSOR GND pin (use back-probe pin to avoid damaging the connector). Red probe to the 5V SUPPLY pin.

**Record your reading:** _______ V

**Step 7:** Verify the reading against the specification on your station card:
- Acceptable: 4.95V to 5.05V
- Marginal: 4.85V to 4.95V or 5.05V to 5.15V
- Fault: below 4.85V or above 5.15V

**Step 8:** Move the red probe directly to the sensor ground pin. Verify it reads 0.00V ± 0.01V relative to itself (red and black on same pin). If not, your ground reference has a problem — call the instructor.

**Step 9:** Now measure ground return quality. Move black probe to chassis ground (marked GND-CHASSIS on the board frame). Move red probe to the SENSOR GND ECU pin. Record the reading: _______ mV

This is the voltage difference between sensor ground and chassis ground. Acceptable: less than 50mV. If greater, there is a ground offset — investigate further.

**Instructor checkpoint:** Verify both supply and ground readings before proceeding. Student must be able to state: "The 5V reference is within specification at ___V. Sensor ground reads ___mV offset from chassis."

---

### TASK 2: TPS Testing — Multimeter Sweep and Dead-Spot Detection (18 minutes)

**Objective:** Connect a TPS sensor through the breakout harness, verify supply and signal voltages at each end of travel, and sweep for dead spots.

**Step 1:** Connect the TPS breakout harness to the TPS sensor. The harness provides: supply (red), signal (yellow), ground (black), and two additional test points (TP-TPS-Supply and TP-TPS-Signal) for probing.

**Step 2:** Connect the breakout harness to the training board's TPS connector.

**Step 3:** Board powered ON. Set multimeter to DC voltage.

**Step 4:** Measure and record TPS supply voltage at TP-TPS-Supply (red probe) relative to sensor ground:

**TPS supply reading:** _______ V
- Pass criterion: 4.95–5.05V

**Step 5:** Measure TPS signal voltage at TP-TPS-Signal with the TPS shaft at full-closed position (throttle stop):

**TPS signal at closed throttle:** _______ V
- Typical specification: 0.40V to 0.60V (refer to station spec card for your specific sensor)

**Step 6:** Rotate TPS shaft slowly to wide-open throttle (WOT). Measure signal voltage at WOT:

**TPS signal at WOT:** _______ V
- Typical specification: 4.40V to 4.65V (refer to spec card)

**Step 7:** Dead spot test — sweep procedure:
- Return TPS to closed throttle.
- Rotate the shaft slowly and continuously toward WOT — take approximately 10 seconds to complete the full sweep.
- Watch the multimeter display throughout. The reading must increase smoothly without any drops, jumps, or momentary freezes.
- Perform the sweep at least 3 times in each direction (closed to open, open to closed).

**Record:** Did the sweep show any irregularities? Y / N
If yes, describe: _______________________________

**Step 8:** If a dead spot is observed, narrow the location:
- Sweep slowly again, watching for the exact shaft position where the dropout occurs.
- Mark that approximate position on the TPS body with a small piece of tape.
- Record the approximate voltage before the dropout and the dropout voltage: Before ___V → dropout to ___V → recovery at ___V

**Conclusion:** Based on your readings, is this TPS:
- [ ] HEALTHY — supply in spec, output range in spec, no dead spots
- [ ] SUPPLY FAULT — supply voltage out of spec (record actual value)
- [ ] RANGE FAULT — output at closed or WOT out of spec (record actual value)
- [ ] DEAD SPOT — record location and voltages
- [ ] MULTIPLE FAULTS

**Instructor checkpoint:** Show your recorded values and conclusion. Instructor will present you with a second TPS (faulty — dead spot at 45% throttle). You have 3 minutes to confirm the fault with the sweep procedure.

---

### TASK 3: MAP Sensor Testing — Static and Dynamic Pressure Test (15 minutes)

**Objective:** Verify MAP sensor supply and output at known pressure points using a hand vacuum pump.

**Step 1:** Connect the MAP sensor breakout harness to the MAP sensor. Note: MAP sensors have supply, signal, and ground — same three-wire configuration as TPS, but the variable input is pressure (vacuum), not mechanical position.

**Step 2:** Connect the vacuum pump to the MAP sensor vacuum port via the barbed fitting on the breakout harness.

**Step 3:** Board powered ON. Set multimeter to DC voltage.

**Step 4:** With NO vacuum applied (atmospheric pressure), measure and record MAP signal voltage:

**MAP signal at 0 mmHg (atmospheric):** _______ V
- Specification for a 1-bar (100kPa) absolute sensor: 4.0V to 4.5V at atmospheric pressure (refer to spec card)

**Step 5:** Apply vacuum in steps using the hand pump. At each vacuum level, hold for 3 seconds and record the MAP signal voltage:

| Vacuum Applied | MAP Signal Voltage | In Spec? |
|---------------|-------------------|----------|
| 0 mmHg (atmospheric) | | |
| 100 mmHg | | |
| 200 mmHg | | |
| 300 mmHg | | |
| 400 mmHg (maximum — do not exceed 500 mmHg) | | |

- Specification: signal should decrease as vacuum increases (lower absolute pressure = lower sensor output voltage for an absolute MAP sensor)
- At 400 mmHg (approximately 47 kPa absolute): expected output approximately 1.8V to 2.2V (refer to spec card)

**Step 6:** Check for stuck signal. Apply 200 mmHg vacuum. Hold. Release the pump slowly. The MAP voltage should track the pressure change in real time — it should rise back toward atmospheric as vacuum bleeds off. If the signal stays fixed and does not track the pressure release: the sensor is stuck — it may have a failed diaphragm or internal electronics fault.

**Step 7:** Verify signal at atmospheric after releasing vacuum. It should return to within 0.1V of the original atmospheric reading.

**Conclusion for MAP sensor:**
- [ ] HEALTHY — supply in spec, signal tracks vacuum correctly, returns to atmospheric
- [ ] SUPPLY FAULT — supply out of spec
- [ ] RANGE FAULT — signal at atmospheric or maximum vacuum out of spec
- [ ] STUCK SIGNAL — signal does not track pressure changes
- [ ] DRIFT — signal at atmospheric after release differs by more than 0.1V from initial reading

**Note:** If your station has a second MAP sensor for comparison (labelled B), repeat Steps 4–7 on sensor B. Note any differences in absolute voltage at each vacuum point — this illustrates sensor-to-sensor variation within specification, which is normal.

**Instructor checkpoint:** Review the vacuum sweep table. Student must be able to explain why a MAP sensor reading 4.8V at atmospheric is out of spec and what diagnostic conclusion to draw.

*(Expected: 4.8V is above the 4.5V maximum for atmospheric — suggests sensor output is stuck high, or the signal circuit is being pulled toward supply voltage — possible internal short or signal wire shorted to supply.)*

---

### TASK 4: CKP Sensor Output — Oscilloscope Capture and Analysis (18 minutes)

**Objective:** Connect the oscilloscope to the CKP simulator board, capture the waveform, identify sensor type from waveform shape, and compare healthy vs degraded signals.

The CKP simulator board at your station produces two outputs, switchable:
- **Output A:** VR-type sine wave (variable amplitude based on frequency control)
- **Output B:** Hall effect square wave, 5V amplitude, same frequency

**Step 1:** Connect the oscilloscope x10 probe to CKP Output A. Ground clip to simulator board signal ground.

**Step 2:** Set the oscilloscope:
- DC coupling
- 2V/div
- Timebase: 10ms/div (starting point)
- Trigger: Edge, Rising, Channel 1, level at 0V (for VR zero crossing)

**Step 3:** Set the simulator frequency control to approximately 100Hz (simulating approximately 1500 rpm on a 4-cylinder with 4-tooth trigger wheel — confirm with your instructor).

**Step 4:** Adjust timebase until you can see 3–5 complete sine wave cycles. Record the timebase setting: _______ms/div

**Step 5:** Using cursor tools, measure:
- Peak-to-peak amplitude of the sine wave: _______ V
- Period (time for one complete cycle): _______ ms
- Calculated frequency: _______ Hz (f = 1000 ÷ period_in_ms)

**Step 6:** Increase the simulator frequency to approximately 300Hz (simulating higher RPM). Measure new amplitude:
- Amplitude at higher frequency: _______ V

*Expected observation: amplitude increases with frequency on a VR sensor. This is normal and expected.*

**Step 7:** Switch to Output B (Hall effect). Connect scope to Output B. Adjust scope settings:
- 2V/div (signal swings 0–5V, so 2V/div works well)
- Trigger level at 2.5V (mid-signal for clean edge triggering)

**Step 8:** Measure Hall effect signal:
- Amplitude (should be close to supply voltage): _______ V
- Period: _______ ms
- Duty cycle (high time ÷ period × 100%): _______ %

**Step 9:** Your instructor will activate a pre-set fault condition on the simulator. The fault will be one of the following (you will not be told which):
- Noise injected on baseline
- Amplitude reduction (simulating large air gap)
- Missing trigger event (missing tooth simulation)
- DC offset on the signal (simulating a failed interface component)

**Your task:** Identify the fault type from the waveform. Write one sentence describing:
1. What you observe on the oscilloscope
2. What fault this represents physically
3. What component or condition would cause it in a real vehicle

**Instructor checkpoint:** Student presents their fault identification and explanation. Instructor confirms or corrects.

*Instructor notes on expected fault identifications:*
- *Noise on baseline: high-frequency hash visible on signal — cause: shielding failure or ground loop*
- *Amplitude reduction: peaks lower than at same frequency without fault — cause: increased sensor air gap or weak magnet*
- *Missing tooth: one period shows near-zero amplitude, rest normal — cause: damaged reluctor ring tooth (or deliberate reference marker — student should note the ambiguity)*
- *DC offset: entire waveform shifted above 0V, zero crossings now occur at a positive voltage — cause: failed clamp diode or signal conditioning component on ECU PCB*

---

### TASK 5: Injector Coil Resistance and Waveform Verification (10 minutes)

**Objective:** Measure injector coil resistance with the multimeter and verify against specification, then observe the injector drive waveform on the oscilloscope.

**Resistance measurement — power must be OFF:**

**Step 1:** Confirm bench supply is switched OFF. Wait 30 seconds.

**Step 2:** Measure DC voltage across the main supply capacitor on the training board to confirm discharge below 1V.

**Step 3:** Null multimeter leads in Ω mode.

**Step 4:** Connect meter probes to the injector connector terminals (via breakout harness test points):
- Red probe: terminal 1 (power supply terminal)
- Black probe: terminal 2 (driver/ground terminal)

**Step 5:** Record resistance: _______ Ω

**Step 6:** Compare to specification on station card:
- Peak-and-hold type injector: 2–5Ω — record your spec: _______ Ω
- Saturated type injector: 12–16Ω — record your spec: _______ Ω
- Your injector type (read from station label): _______

| Result | Interpretation |
|--------|---------------|
| Within spec range | Coil is healthy |
| Below low limit (e.g., <2Ω on P&H type) | Internal short in coil winding — may cause driver IC overcurrent |
| Above high limit (e.g., >20Ω on saturated type) | Open turns in coil — injector will not open fully or at all |
| OL (open) | Complete coil open — injector dead |

**Waveform observation — power ON:**

**Step 7:** Power board ON. Set oscilloscope:
- DC coupling
- 10V/div (to capture freewheeling spike)
- Timebase: 2ms/div
- Trigger: Edge, Falling, Channel 1 (trigger on the falling edge of the drive signal — voltage drops from 12V to near 0V at injector open command)
- Trigger level: 6V (mid-way between battery voltage and drive-low voltage)

**Step 8:** Connect x10 probe to the injector low-side drive terminal (the ECU-controlled terminal — terminal 2 on the breakout harness).

**Step 9:** Observe the waveform when the board activates the injector driver (the training board runs a repeating injector pulse at approximately 5Hz).

**Step 10:** Identify and label on your scope screenshot or sketch:

| Feature | Voltage on Screen | Time Position |
|---------|-----------------|---------------|
| Injector open command (voltage drops) | | |
| Peak phase (if P&H type) | | |
| Hold phase with PWM (if P&H type) | | |
| Freewheeling spike (voltage peak above supply) | | |
| Injector close (voltage returns to supply) | | |

**Step 11:** Measure the freewheeling spike amplitude: _______ V
- Acceptable range: 40–80V (varies by system — refer to spec card)
- If spike is absent or below 20V: freewheeling diode may be shorted
- If spike exceeds 100V: freewheeling clamping device may be open or failed

**Conclusion for injector:**
- [ ] HEALTHY — coil resistance in spec, waveform shows correct drive type, freewheeling spike within range
- [ ] COIL FAULT — resistance out of spec (record actual)
- [ ] DRIVER FAULT — waveform shape incorrect for stated drive type (describe)
- [ ] CLAMP FAULT — freewheeling spike absent or excessive (record actual peak voltage)

---

## Instructor Checkpoint Summary

| After Task | What to Check | Pass Criterion |
|------------|--------------|----------------|
| Warm-up | Wiring diagram pin answers (5 items) | All 5 correct before Task 1 begins |
| Task 1 | Supply voltage reading and ground offset measurement | Supply within 4.95–5.05V; ground offset below 50mV; student can state ECU pin numbers from memory |
| Task 2 | TPS readings table; dead spot detection on faulty TPS | Closed and WOT voltages within spec; dead spot on faulty TPS identified within 3 minutes |
| Task 3 | MAP vacuum sweep table; stuck signal test | Signal tracks vacuum correctly; atmospheric recovery within 0.1V |
| Task 4 | CKP waveform measurements; fault identification | Amplitude vs frequency trend noted; fault correctly identified and explained with physical cause |
| Task 5 | Injector resistance with correct units; waveform with features labelled | Resistance compared to correct spec for type; at least 3 waveform features correctly identified; freewheeling spike amplitude measured |

---

## Sign-Off Checklist (Assessment Criteria)

Instructor initials each line at the end of the session. All lines must be initialled for the student to be marked complete for this session.

**Student Name:** _____________________________ **Date:** _____________

| # | Criterion | Instructor Initials |
|---|-----------|---------------------|
| 1 | Wiring diagram trace completed correctly — all 5 pin assignments correct | |
| 2 | Sensor supply voltage measured at correct ECU pin (not at sensor connector) | |
| 3 | 5V supply reading within specification — or fault correctly identified with value | |
| 4 | Sensor ground offset measured and interpreted correctly | |
| 5 | TPS sweep performed slowly and continuously — not point-by-point | |
| 6 | TPS dead spot correctly identified on faulty sensor during 3-minute challenge | |
| 7 | MAP sensor signal tracked vacuum pump correctly across all pressure points | |
| 8 | MAP stuck-signal test performed and result interpreted | |
| 9 | CKP waveform captured with DC coupling and x10 probe | |
| 10 | VR vs Hall effect sensor types correctly distinguished from waveform shape | |
| 11 | Instructor-selected CKP fault correctly identified with physical cause stated | |
| 12 | Injector coil resistance measured with leads nulled and power OFF | |
| 13 | Resistance result compared to correct specification for the stated injector type | |
| 14 | Injector drive waveform captured with at least 3 features labelled and identified | |
| 15 | Freewheeling spike amplitude measured and interpreted | |

---

## Common Mistakes and How to Address Them

| Mistake | How It Manifests | Intervention |
|---------|-----------------|-------------|
| TPS sweep done too fast | Student reports "no dead spot" on a sensor that has one | Ask: "How long did the full sweep take?" Should be at least 8–10 seconds. Have them redo at half speed. |
| MAP sensor probed at sensor connector, not ECU pin | Finds a perfect 5V at sensor connector, misses the voltage drop between connector and ECU | Ask: "Where does the supply originate — from the ECU or from the sensor?" The ECU generates the 5V. Test it at the ECU side too. |
| Exceeds 500 mmHg on MAP sensor | Pump pushed too hard; sensor may be damaged | Remind about the red marking on pump gauge. If sensor readings shift after this, sensor may be compromised — swap in the spare. |
| CKP trigger set to mid-amplitude instead of 0V for VR sensor | Waveform appears to trigger at inconsistent points, looks jittery | Ask: "What does the ECU look for on a VR sensor signal?" Zero crossing. Trigger level should be 0V. Reposition trigger and observe stability improvement. |
| VR amplitude variation misread as fault | Student flags "lower amplitude at low frequency" as abnormal | Confirm with them: VR amplitude is proportional to rate of change of flux — faster rotation = higher amplitude. Show them the amplitude at two different frequencies and ask if the change makes sense. |
| Injector resistance measured with board powered | Meter fluctuates or reads incorrectly; student may not notice | Ask: "Is the board powered?" If yes: "What happens to your meter when you switch to Ω mode on a live circuit?" Power off, discharge, null, remeasure. |
| Freewheeling spike not captured — timebase too fast | Waveform shows only a brief spike, student cannot measure peak | Zoom out on timebase to show the full injection event including the spike tail. Then zoom in once spike position is located. |
| Scope not on x10 setting in menu | Amplitude reads 10x too high (freewheeling spike appears as 600V+) | Ask: "Does that voltage make physical sense for a 12V system?" No. Check probe factor in channel menu. |

---

## Debrief Questions (Last 5 minutes of session)

Bring the group together at the instructor bench.

1. "In Task 1, you measured sensor ground offset relative to chassis ground. One pair found 120mV offset. If the MAP sensor draws 20mA and is ratiometric, what is the effect on the sensor reading?"

   *(Expected reasoning: 120mV offset on sensor ground means the MAP sensor's 0V reference is at 120mV above chassis ground. The sensor output voltage — measured by the ECU — is also 120mV higher than it should be. For a 5V ratiometric system, 120mV = 2.4% of full scale. On a MAP reading of 1.5V, that's a 120mV error, about 8%. The ECU may not flag a DTC but the fuel trim will compensate, potentially hiding a fuel delivery problem.)*

2. "When we do the TPS dead spot test with a multimeter, we get a reading only at the moment we're paused. What would be the advantage of connecting the scope to the TPS signal and sweeping in real time?"

   *(Expected: the scope captures the signal continuously with time on the X-axis. Even a 5ms dead spot — invisible to the eye on a meter — would appear as a visible dropout on the scope trace. The scope records the shape of the sweep; the meter only shows the instant.)*

3. "The CKP fault you identified this session — what would be the fault code and symptom in a real vehicle if it occurred intermittently?"

   *(Open — depends on fault type assigned. Noise on baseline: P0335 intermittent, possible random misfires. Missing tooth in wrong position: crank position error, could cause timing retard, misfire, or no-start. DC offset: P0335 or no crank signal — ECU may not detect zero crossings, engine does not start.)*

4. "We measured injector coil resistance at 13.8Ω. The spec for this injector is 12–16Ω. Is it healthy? What would happen if the resistance was 22Ω?"

   *(Expected: 13.8Ω is within spec — healthy. At 22Ω, the coil current under 12V drive would be 12V ÷ 22Ω = 0.55A. A saturated drive injector typically needs 0.8–1.5A to open reliably against fuel pressure. At 0.55A, the injector may partially open, open late, or not open at all. Result: lean fuelling, misfire, rough idle, possible P0201-series codes.)*

5. "Looking back at this entire module — Day 2 and Day 3 — what is the single measurement technique you think will be most valuable to you in actual ECU repair? Why?"

   *(No correct answer. Encourage genuine reflection. Listen for reasoning that connects measurement precision to diagnostic confidence.)*

---

## Appendix A — Sensor Specification Card (print and laminate, one per station)

```
ECUHR MODULE 2 — SENSOR SPECIFICATION REFERENCE CARD

TPS (THROTTLE POSITION SENSOR)
3-wire potentiometer, ratiometric
Supply voltage:     4.95V – 5.05V
Signal at closed:   0.40V – 0.60V
Signal at WOT:      4.40V – 4.65V
Dead spot limit:    None acceptable — any dropout is a fault
Sweep direction:    Increases with opening throttle (closed = low, WOT = high)

MAP SENSOR (1-BAR ABSOLUTE PRESSURE)
3-wire, ratiometric
Supply voltage:     4.95V – 5.05V
Signal at 100 kPa (atmospheric, 0 mmHg vacuum):   4.0V – 4.5V
Signal at 50 kPa (approx 375 mmHg vacuum):         1.8V – 2.3V
Signal at 30 kPa (approx 525 mmHg vacuum):         0.8V – 1.5V
Maximum vacuum:     DO NOT exceed 500 mmHg (67 kPa)
Signal direction:   Decreases as vacuum increases (absolute pressure decreases)

CKP SENSOR — VR TYPE
Output type:        Sine wave (AC); amplitude proportional to RPM
Amplitude at idle:  2V – 8V peak-to-peak (varies by sensor and air gap)
Zero crossing:      Must be clean; no noise within ±200mV of 0V
DC offset:          Signal must cross 0V; offset > ±0.5V is a fault
Air gap spec:       Refer to service data (typically 0.5–1.5mm)

CKP SENSOR — HALL EFFECT TYPE
Output type:        Square wave; 0V low, supply voltage high
Supply voltage:     5V or 12V depending on sensor type (check label)
Signal low:         < 0.3V
Signal high:        > 4.7V (for 5V type); > 11.0V (for 12V type)
Rise/fall time:     < 5μs

FUEL INJECTOR — PEAK-AND-HOLD TYPE
Coil resistance:    2Ω – 5Ω
Peak current:       4A – 8A (first 1–3ms)
Hold current:       0.8A – 2A (PWM controlled)
Freewheeling spike: 40V – 80V (measured at injector driver pin)
Drive type:         Low-side switch (ECU controls ground side)

FUEL INJECTOR — SATURATED TYPE
Coil resistance:    12Ω – 16Ω
Drive current:      0.75A – 1.0A (limited by coil resistance)
Freewheeling spike: 40V – 80V
Drive type:         Low-side switch

SENSOR GROUND QUALITY LIMITS
Ground offset (sensor GND vs chassis GND):   < 50mV acceptable; > 50mV investigate
Voltage drop in sensor GND return trace:      < 50mV at rated sensor current

5V REFERENCE RAIL LIMITS
At regulator output:     4.97V – 5.03V
At sensor connector pin: 4.95V – 5.05V
Maximum drop (reg to pin): 30mV at rated load
```

---

*End of SESSION-03H Framework*
