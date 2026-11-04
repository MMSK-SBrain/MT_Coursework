# SESSION-06T: Signal Conditioning, Output Drivers & Thermal Management
## Instructor-Led Theory Framework

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 3 — ECU Architecture, Protection & Filtering (Days 4–6)
**Session:** Day 6 — Theory
**Duration:** 90 minutes
**Format:** Instructor-led lecture with worked examples and waveform analysis
**PPT Target:** 22–25 slides

---

## Session Outcomes

| SO ID | Description | Bloom |
|-------|-------------|-------|
| so-3-5-1 | Explain low-side vs high-side driver operation and identify each type | Understand |
| so-3-5-2 | Explain flyback/freewheeling diode function and failure mode when missing | Understand |
| so-3-5-3 | Recognise what an overcurrent or missing-flyback waveform looks like on an oscilloscope capture | Understand |
| so-3-6-1 | Explain junction temperature, thermal resistance (Rθja), and component derating | Understand |

---

## Module 3 Narrative Thread

> "Days 4 and 5 covered the board's infrastructure — how it is built, how it is powered, how it is protected and filtered. Today we reach the output side: the circuits that actually do work in the vehicle. Every injector, solenoid, relay, and motor that the ECU controls is driven by one of the circuits we cover this morning. These are also the circuits that fail most often — because they handle real power, they face the most demanding electrical conditions, and when they fail, they fail dramatically."

---

## INSTRUCTOR STORY ARC

### OPENING HOOK (Slides 1–3, ~8 minutes)

#### Slide 1: Title
**Visual:** Oscilloscope trace of a healthy injector drive waveform — showing peak current phase, hold phase, and freewheeling spike — annotated with voltage levels
**Instructor Script:**
> "This is what a healthy injector driver output looks like on an oscilloscope. There is a peak phase where the injector is being opened, a hold phase where it is being held open with less current, and then the freewheeling spike — a controlled voltage spike as the injector coil releases its stored energy.
>
> A technician who can read this waveform can tell in 30 seconds whether the driver is functioning correctly, whether the flyback diode is working, and whether the driver IC is current-limiting correctly.
>
> A technician who cannot read this waveform will replace the injector — because the fault code said 'injector circuit' — find no improvement, and escalate the job at a cost of hundreds of dollars and hours.
>
> Today you learn to read the waveform."

#### Slide 2: What the Output Stage Does
**Visual:** Block diagram — MCU PWM output → driver IC → physical load (injector coil, solenoid, relay coil) in vehicle
**Instructor Script:**
> "The MCU is a low-power device. Its output pins can source or sink a few milliamps at most — enough to drive an LED or a logic signal, not enough to drive a solenoid coil drawing 1 to 5 amps.
>
> The output driver stage is the power amplification layer. It takes the MCU's low-power logic signal and uses it to control a power transistor — a MOSFET — that can handle the full current of the load.
>
> The output driver also provides:
> - Overcurrent protection — if the load is shorted, the driver limits or cuts current to protect the MOSFET
> - Diagnostic feedback — the driver reports load open circuit or short circuit conditions back to the MCU via a status pin
> - Thermal shutdown — the driver cuts off if its junction temperature exceeds a safe limit
>
> Understanding these three functions is what allows you to use waveform analysis and resistance testing to diagnose driver faults without replacing components blindly."

#### Slide 3: Today's Three Topics
**Visual:** Simple numbered list
**Instructor Script:**
> "Three topics today:
>
> 1. Low-side vs high-side drivers — which way the MOSFET switches, and why it matters
> 2. Flyback diodes — the most important and most commonly misunderstood component in the output stage
> 3. Thermal management — junction temperature, thermal resistance, and why the same ECU fails in summer but not winter
>
> Everything you learn today feeds directly into the hands-on session this afternoon, where you will capture and analyse real waveforms."

---

### PART 1: Low-Side and High-Side Drivers (Slides 4–9, ~22 minutes)

#### Slide 4: The Load Circuit — Where the Driver Fits
**Visual:** Simple circuit: +12V supply → load (injector coil represented as inductor) → output pin → ground. Arrow showing current flow when driver is ON
**Instructor Script:**
> "Before we discuss driver topology, let us establish the load circuit. Most ECU-driven loads look like this:
>
> - One end of the load connects to +12V (from the vehicle battery via a relay or fuse)
> - The other end of the load connects to the ECU output pin
> - The ECU output pin switches to either ground (low-side driver) or +12V (high-side driver) to complete or break the circuit
>
> The load is almost always inductive — injector coils, solenoid coils, relay coils. Inductors store energy in their magnetic field while current flows, and release that energy when current stops. This stored energy release is what creates the voltage spikes we will discuss with flyback diodes."

#### Slide 5: Low-Side Driver — How it Works
**Visual:** Circuit diagram — +12V → load (inductor) → MOSFET drain-source → ground. MOSFET gate driven by driver IC which receives PWM from MCU. Annotation: load current path when MOSFET is ON
**Instructor Script:**
> "A low-side driver switches the load to ground. The load sits between +12V and the MOSFET output. The MOSFET source is connected to ground.
>
> When the MCU commands the driver ON:
> - The driver IC pulls the MOSFET gate high (above threshold voltage)
> - The MOSFET turns on — drain-source resistance drops to a few milliohms
> - Current flows: +12V → through the load → through the MOSFET → to ground
> - The load activates — the injector opens, the solenoid engages, the relay closes
>
> When the MCU commands the driver OFF:
> - The driver IC pulls the gate to zero volts
> - The MOSFET turns off — drain-source becomes an open circuit
> - Current through the load stops
> - The inductor's stored magnetic field collapses — producing the voltage spike (more on this in the flyback section)
>
> Low-side drivers are used for: fuel injectors, idle control valves, canister purge solenoids, relays, EGR valves — essentially all inductive loads on the ECU output stage.
>
> Gate drive simplicity: an N-channel MOSFET (the standard choice for low-side) turns on when the gate is driven above the source voltage. Since the source is at ground, any gate voltage above approximately 4V turns the MOSFET on. This is easy to generate from a 5V logic supply — no special gate drive circuitry needed."

#### Slide 6: Low-Side Driver Failure Modes
**Visual:** Two columns — MOSFET shorted (drain-source short) and MOSFET open, with symptoms for each
**Instructor Script:**
> "Low-side MOSFET failures occur in two ways:
>
> **MOSFET shorted drain-source:**
> The MOSFET junction fails as a short circuit. Current flows from drain to source regardless of gate voltage. The load is permanently connected to ground — it is always ON.
> Symptom: Load stays on even when ECU is commanding it off. Injector stuck open — engine runs extremely rich, may not start. Fault code: actuator stuck on / driver output stuck low.
> Test: With ECU powered down, measure resistance from the ECU output pin to ground. Healthy MOSFET: high resistance (open circuit) when gate is not driven. Shorted MOSFET: near-zero ohms.
>
> **MOSFET open drain-source:**
> The MOSFET junction fails as an open circuit. Current cannot flow even when the gate is driven correctly. The load is permanently disconnected — it is always OFF.
> Symptom: Load never activates. Injector never fires. Fault code: actuator open circuit / no current in load.
> Test: Same resistance test. Healthy MOSFET should show low resistance (a few ohms) when gate is correctly biased. Open MOSFET: OL regardless of gate state.
>
> **Driver IC failure:**
> The driver IC itself fails — either its gate drive output fails or its overcurrent protection locks out permanently.
> Symptom: MCU is commanding the output; the MOSFET gate has no signal; the load is permanently off.
> Test: Oscilloscope on the MOSFET gate pin during commanded activation. Healthy: gate signal present, rising to >4V. Failed driver: gate stays at 0V despite MCU command."

#### Slide 7: High-Side Driver — How it Works
**Visual:** Circuit diagram — MOSFET drain connected to +12V supply, source connected to load, load other end to ground. Gate driven by charge pump circuit. Annotation: current path when MOSFET is ON
**Instructor Script:**
> "A high-side driver switches +12V to the load. The load sits between the MOSFET output (source) and ground. The MOSFET drain is connected to the +12V supply.
>
> When the MCU commands the driver ON:
> - The driver IC turns the MOSFET on
> - Current flows: +12V → through MOSFET → through load → to ground
> - The load activates
>
> When the MCU commands the driver OFF:
> - The MOSFET turns off
> - Current through the load stops
>
> Conceptually similar to the low-side driver — but with a critical engineering challenge.
>
> To turn on a P-channel MOSFET (the natural choice for a high-side switch with source connected to +12V), the gate must be pulled *below* the source voltage. The source is at +12V. The gate must go below 12V − threshold voltage ≈ 8–9V. This is achievable.
>
> To use an N-channel MOSFET in the high-side position (which is preferred because N-channel MOSFETs have lower on-resistance), the gate must go *above* the source voltage. The source floats near +12V when the MOSFET is on. The gate must reach 16–18V to turn on a 12V-source MOSFET. This requires a **charge pump** — a circuit that boosts a voltage above the supply rail. High-side N-channel driver ICs include an integrated charge pump for this purpose.
>
> High-side drivers are used for: motor control (seat motors, wiper motors), heated rear window, dome lights, heated seats — loads that are typically grounded at the load end, and where the supply side is switched."

#### Slide 8: High-Side vs Low-Side — Choosing Between Them
**Visual:** Comparison table — application, current handling, fault safety state (load OFF if driver fails), circuit complexity
**Instructor Script:**
> "The choice between high-side and low-side is a systems engineering decision made at ECU design time. Let us understand the reasoning:
>
> **Fault safety state:**
> - Low-side driver failure (short): load stays ON — potentially dangerous for safety-critical loads
> - High-side driver failure (short): load stays ON — same problem
>
> For loads where 'stuck on' is more dangerous than 'stuck off' — for example, the starter motor relay — a high-side driver may be used so that a ground fault in the harness does not inadvertently activate the load. For an injector, where 'stuck on' causes a rich fault rather than immediate danger, low-side is universally used because it is simpler.
>
> **Ground referencing:**
> Low-side drivers are easy to test because the load return side is always near ground. Measuring the voltage at the ECU output pin gives a direct indication of whether the driver is on or off.
> High-side driver outputs float — the output voltage depends on whether the load is connected and conducting. Diagnosis requires measuring both the output pin and verifying load continuity.
>
> **In the workshop:**
> When you receive an ECU with a dead output, the first step is to determine from the vehicle wiring diagram whether that output is a low-side or high-side driver. This tells you what resistance and voltage readings to expect and how to interpret them."

#### Slide 9: Identifying Driver Types on a Schematic and PCB
**Visual:** Two schematic fragments — one showing a low-side configuration (load between +12V and MOSFET drain), one showing a high-side configuration (MOSFET drain at +12V, load between MOSFET source and ground)
**Instructor Script:**
> "On a schematic, identify the driver type by locating the MOSFET in the circuit:
>
> - If the MOSFET **source** connects to **ground** and the **load** is between **+12V and MOSFET drain**: this is a **low-side driver**
> - If the MOSFET **source** connects to the **load** and the **drain** connects to **+12V**: this is a **high-side driver**
>
> On a PCB without a schematic:
> - Low-side output pins measure near 0V when the load is active (driver pulling to ground)
> - High-side output pins measure near +12V when the load is active (driver supplying +12V)
> - This is a useful diagnostic shortcut: probe the ECU output connector pin while commanding the load on via the scan tool. A low reading on a low-side driver = driver is functioning. A high reading on a high-side driver = driver is functioning.
>
> In the hands-on session this afternoon, you will determine which driver type your test ECU uses for the injector channel and verify it with this exact measurement approach."

---

### PART 2: Flyback Diodes — The Most Critical Output Stage Component (Slides 10–15, ~22 minutes)

#### Slide 10: The Inductive Kickback Problem
**Visual:** Circuit diagram — low-side driver switches off, MOSFET is now open. Inductor current wants to continue. Voltage at junction point spikes negative (low-side) or positive (high-side). Annotation: without flyback diode, this spike is uncontrolled
**Instructor Script:**
> "This is the most important concept in the output stage.
>
> All ECU-driven loads — injectors, solenoids, relays — are inductive. An inductor stores energy in its magnetic field when current flows through it.
>
> When the driver turns OFF, the MOSFET is now an open circuit. The current through the inductor cannot stop instantaneously — the inductor's stored energy demands that current continues to flow.
>
> With the MOSFET off and no alternative path for current, the inductor creates whatever voltage is necessary at its terminals to force the current to continue flowing. This voltage can be extremely large.
>
> The equation is: **V = L × (dI/dt)**
>
> For a typical fuel injector:
> - Inductance: ~2.5mH
> - Peak hold current: ~1A
> - Turn-off time without freewheeling: ~1µs
>
> V = 0.0025 × (1 / 0.000001) = **2,500 volts**
>
> The driver MOSFET's drain sees this voltage. The MOSFET gate oxide typically ruptures at 20 to 60V. The MOSFET is destroyed — every single time the injector fires — unless the inductive kickback energy has somewhere to go.
>
> That is the job of the flyback diode."

#### Slide 11: How the Flyback Diode Works
**Visual:** Circuit diagram — inductor with flyback diode in parallel (reverse polarity across the load), annotated with current path during flyback event. Voltage clamping shown on waveform
**Instructor Script:**
> "The flyback diode — also called the freewheeling diode or catch diode — is placed in parallel with the inductive load, with reversed polarity relative to the supply voltage.
>
> During normal operation (driver ON):
> The diode is reverse biased by the +12V supply. No current flows through the diode. It is invisible to the circuit.
>
> When the driver turns OFF:
> The inductor voltage reverses, trying to force current to continue. The reversed voltage forward-biases the flyback diode. Current now flows through the diode — from the inductor, through the diode, back to the other end of the inductor. This is called the freewheeling path.
>
> The diode clamps the voltage spike to:
> **Vclamp = Vsupply + Vforward_diode ≈ 12V + 0.7V = 12.7V**
>
> Instead of 2,500V, the MOSFET drain sees 12.7V. The MOSFET survives.
>
> The inductor's stored energy is dissipated in the diode and the load resistance over a short freewheeling period — typically 1 to 10ms for a fuel injector. The current decays smoothly to zero as the energy is dissipated.
>
> On an oscilloscope, this freewheeling event is visible as a 'plateau' on the injector drive waveform after the driver turns off — the voltage sits at (supply + diode drop) and slowly decays as the current falls. This is the freewheeling spike you see on a healthy injector waveform."

#### Slide 12: Flyback Diode Location — On-Board vs External
**Visual:** Two ECU diagrams — Left: flyback diode integrated on the ECU PCB (D reference designator near output driver MOSFET). Right: flyback diode in the wiring harness or at the load (relay coil with diode across it)
**Instructor Script:**
> "Flyback diodes can be placed at different points in the circuit:
>
> **Option 1 — On the ECU PCB:**
> A diode placed in parallel with the output stage, on the ECU board. You will see this as a D-designated diode (or a TVS diode, for more precise clamping) near the output driver MOSFET. This is the most reliable approach — the protection is always there regardless of what is happening in the harness.
>
> **Option 2 — In the wiring harness or at the load:**
> For relay coils and some solenoids, the flyback diode may be incorporated into the relay or solenoid body, or clipped into the connector at the component. This is common on relay outputs.
>
> **Option 3 — Integrated inside the driver IC:**
> Many modern driver ICs (Texas Instruments VNQ series, Infineon BTS series) include integrated clamp circuits and active freewheeling structures on-chip. The separate discrete diode may not be visible on the PCB.
>
> Diagnostic relevance: when you receive an ECU with a destroyed output driver MOSFET, always look for the flyback diode or clamp circuit. If it is missing or failed, the MOSFET will be destroyed again after replacement — within the first few injector cycles.
>
> Test the flyback diode: diode test across the component. Forward: 0.5–0.7V. Reverse: OL (for a standard diode) or the clamp voltage of the TVS (for a TVS flyback clamp)."

#### Slide 13: What Happens When the Flyback Diode is Missing or Failed
**Visual:** Waveform comparison — left: healthy injector waveform with freewheeling plateau. Right: missing flyback diode — spike reaches 80–150V, then driver fails
**Instructor Script:**
> "If the flyback diode is missing — either never installed (PCB design error or missing component) or failed open — the MOSFET drain sees the full inductive kickback voltage.
>
> For a fuel injector with 2.5mH inductance and 1A hold current, the spike depends on the driver's internal stray capacitance (which limits the dV/dt somewhat in practice). In a real circuit, you typically see:
> - A spike of 80 to 200V at the MOSFET drain when the driver turns off
> - The spike duration is extremely short — sub-microsecond
> - This spike exceeds the gate oxide breakdown voltage of virtually all power MOSFETs (typically 20V for the gate, and while the drain-source voltage rating might be 60–100V, repetitive spikes at those levels cause cumulative damage)
>
> The failure pattern without a functioning flyback diode:
> 1. First few ignition cycles: MOSFET appears to function normally (the spike is just within tolerance)
> 2. Gradual degradation: MOSFET on-resistance begins to increase; driver becomes intermittent
> 3. Final failure: MOSFET fails completely shorted or open
> 4. Fault code: injector circuit fault
> 5. Technician replaces driver IC or MOSFET
> 6. Failure recurs within days — because the flyback diode was never restored
>
> This failure loop is extremely common in the workshop. The repair that does not address the root cause (missing or failed flyback diode) is condemned to repeat."

#### Slide 14: The Injector Waveform — Peak and Hold
**Visual:** Annotated oscilloscope trace of a complete injector drive cycle: (1) peak current phase, (2) hold current phase, (3) driver off, (4) freewheeling plateau, (5) current decays to zero
**Instructor Script:**
> "Modern high-impedance fuel injectors (12 to 16 ohms coil resistance) are driven with a simple on/off strategy — the driver is on for the injection period and off when done.
>
> But many injectors are low-impedance (2 to 4 ohms) and require a peak-and-hold drive strategy:
>
> **Phase 1 — Peak current:** The driver turns on fully. Current ramps up rapidly through the low-resistance coil. The injector is pulled open quickly by high magnetic force. Peak current: typically 4–10A. Duration: 1–3ms.
>
> **Phase 2 — Hold current:** Once the injector is open, less current is needed to hold it open against the return spring. The driver reduces current (via PWM switching) to typically 1–2A. This reduces heat generation in the coil and the driver. Duration: the remainder of the injection pulse width.
>
> **Phase 3 — Driver OFF:** At the end of the injection event, the driver turns off. The inductor's stored energy must be dissipated.
>
> **Phase 4 — Freewheeling:** The flyback diode conducts. The current freewheels around the diode-load loop, dissipating as the magnetic field collapses. On the oscilloscope: the output voltage clamps at Vsupply + 0.7V.
>
> **Phase 5 — Decay:** The freewheeling current decays to zero. The injector closes.
>
> A technician reading this waveform can verify: Is the peak current correct? Is the hold current correct? Is there a freewheeling plateau (confirming the flyback diode is working)? Is the injector close time correct (length of the freewheeling phase)?
>
> Each of these is a diagnostic data point without touching the vehicle or the injector physically."

#### Slide 15: Waveform Anomalies — What Faults Look Like
**Visual:** Three waveform panels — (1) No freewheeling plateau = missing flyback diode. (2) Excessive peak current = shorted injector coil. (3) No current rise at all = open injector or broken harness
**Instructor Script:**
> "Let us interpret waveform anomalies before the hands-on session:
>
> **Missing freewheeling plateau — flyback diode failed or missing:**
> After the driver turns off, instead of a plateau at (Vsupply + 0.7V), the waveform spikes sharply then collapses. The spike may reach 50–150V briefly before clamping on the MOSFET's body diode or internal structure. This is a warning: the flyback diode is not functioning. The driver MOSFET is at risk.
>
> **Abnormally fast current rise / higher than normal peak current — shorted injector coil:**
> The coil resistance is lower than specified (windings shorting together). Peak current is reached faster and may exceed the driver's overcurrent setpoint. The driver may current-limit or go into fault mode mid-cycle.
>
> **No current rise — open injector coil or broken harness:**
> The driver commands the output; the gate signal is present; but no current flows. The output voltage stays near supply voltage rather than dropping when the driver turns on. This indicates the load circuit is open — either the injector coil is open, the harness has a broken wire, or the connector is not engaged.
>
> **Longer than normal freewheeling time — higher than expected inductance:**
> The freewheeling phase takes longer than normal, suggesting the injector coil has more inductance than specified. Possible cause: incorrect replacement injector with different specifications.
>
> In the hands-on session, you will receive oscilloscope captures of injector waveforms — some healthy, some with planted anomalies — and analyse them using this framework."

---

### PART 3: Thermal Management — Junction Temperature, Thermal Resistance, and Derating (Slides 16–22, ~22 minutes)

#### Slide 16: The Temperature Problem — Why ECUs Fail in Summer
**Visual:** Two photos — left: ECU in winter operation (ambient −10°C, ECU cool to the touch). Right: same ECU in summer in an engine bay (ambient +60°C ambient near ECU, visibly hot power stage area)
**Instructor Script:**
> "Here is a classic symptom pattern: a customer's vehicle develops an intermittent fault that goes away when the engine is cold but returns after 20–30 minutes of driving. The fault is diagnosed as an ECU fault. The customer asks: 'Why did it just start happening? The car was fine all winter.'
>
> The answer is thermal. The component that is failing was always marginal — it was operating near its limit even in winter, and as ambient temperature increased with the season, the junction temperature crossed the failure threshold.
>
> Today we build the understanding to diagnose and explain this. The key tool is the thermal resistance model."

#### Slide 17: What is Junction Temperature?
**Visual:** Cross-section diagram of a power MOSFET showing: silicon die (junction), die attach (solder or conductive epoxy), package body, PCB pad, ambient air above
**Instructor Script:**
> "The active part of a semiconductor — the silicon — generates heat when it dissipates power. The temperature of the silicon itself is called the junction temperature (Tj).
>
> The junction is physically isolated from the outside world by the package — the plastic or ceramic body surrounding the die. Heat must conduct through the package to reach the ambient air.
>
> Every material in that heat path has a thermal resistance — it resists the flow of heat, causing a temperature rise across it. The total thermal resistance from the junction to the ambient air is called Rθja — theta junction-to-ambient.
>
> The fundamental thermal equation:
>
> **Tj = Ta + (Rθja × P)**
>
> Where:
> - Tj = junction temperature (°C)
> - Ta = ambient temperature (°C)
> - Rθja = thermal resistance junction-to-ambient (°C/W)
> - P = power dissipated in the component (W)
>
> This equation tells us everything we need to know about whether a component is thermally safe."

#### Slide 18: Working Through the Thermal Equation
**Visual:** Whiteboard-style worked example with numbers
**Instructor Script:**
> "Let us work through a real example on the board.
>
> Scenario: An output driver MOSFET on an ECU.
> - Rθja = 62°C/W (from datasheet — a typical value for a D2PAK SMD package with no heatsink)
> - Steady-state power dissipated: P = I² × Rds_on = (3A)² × 0.08Ω = 0.72W
> - Ambient temperature: Ta
>
> Case 1 — Winter ambient: Ta = 20°C
> Tj = 20 + (62 × 0.72) = 20 + 44.6 = **64.6°C**
> Maximum junction temperature for this MOSFET: 150°C. Margin: 85°C. Safe.
>
> Case 2 — Summer ambient, engine bay: Ta = 85°C
> Tj = 85 + (62 × 0.72) = 85 + 44.6 = **129.6°C**
> Maximum junction temperature: 150°C. Margin: 20°C. Marginal — but still within spec.
>
> Case 3 — Summer ambient, higher than normal load current (injector coil slightly shorted): I = 3.8A
> P = (3.8)² × 0.08 = 1.15W
> Tj = 85 + (62 × 1.15) = 85 + 71.3 = **156.3°C**
> Exceeds maximum junction temperature by 6°C — the component fails. Thermal shutdown, or permanent damage.
>
> This is why the same ECU works in winter and fails in summer. It is not a new fault — it is a combination of borderline component specification and elevated ambient temperature pushing the junction over the limit."

#### Slide 19: Component Derating — The Safety Margin
**Visual:** Derating curve chart — maximum current rating vs temperature, showing that at 85°C ambient, the component is derated to 70% of its room-temperature rating
**Instructor Script:**
> "Component derating means using a component below its absolute maximum rating to ensure a defined safety margin at the worst-case operating temperature.
>
> A driver MOSFET rated at 10A continuous at 25°C may only be rated at 7A at 85°C ambient — because at 85°C ambient, the junction-to-ambient temperature rise from 7A dissipation already reaches the component's junction temperature limit.
>
> Automotive ECU designers apply derating rules — typically operating components at no more than 70–80% of their maximum rated values at maximum ambient temperature.
>
> Where derating failures occur in the workshop:
>
> **Replacement component with higher Rds_on than original:** The replacement MOSFET passes datasheet voltage and current ratings but has 50% higher on-resistance. At the same operating current, power dissipation is 50% higher. The thermal model now places the junction temperature above the limit in summer.
>
> **Thermal interface material degraded:** The thermal paste between the power stage IC and the ECU housing has dried out over years. The thermal resistance from junction to heatsink has increased. The same power dissipation now produces a higher junction temperature.
>
> **Airflow changed:** The ECU mounting position has changed — perhaps after a vehicle modification that placed a heat shield near the ECU, reducing cooling airflow. Ambient temperature around the ECU has increased.
>
> All three are thermal failures that manifest as 'intermittent ECU fault in summer' without any component being technically outside its absolute maximum ratings."

#### Slide 20: Thermal Resistance — Understanding the Heat Path
**Visual:** Thermal resistance ladder diagram — Rθjc (junction to case), Rθcs (case to heatsink), Rθsa (heatsink to ambient), summing to total Rθja
**Instructor Script:**
> "The total thermal resistance from junction to ambient is the sum of resistances along the heat flow path:
>
> **Rθja = Rθjc + Rθcs + Rθsa**
>
> Where:
> - **Rθjc** (junction to case): Fixed property of the package — determined by silicon die size, die attach quality, and package material. Specified in the datasheet. Cannot be changed.
> - **Rθcs** (case to heatsink): Determined by the thermal interface material — thermal paste, thermal pad, or direct solder attachment. This is the one you can affect in repair.
> - **Rθsa** (heatsink to ambient): Determined by the heatsink design — its surface area, fin design, and airflow. In ECUs, the 'heatsink' is often the aluminium housing of the ECU itself.
>
> For ECUs without a dedicated heatsink (the component dissipates directly to ambient through the PCB):
> The simplified Rθja value applies — typically 30 to 100°C/W depending on package and PCB copper area.
>
> For ECUs where the power stage is bolted to the ECU aluminium housing through a thermal interface:
> The full Rθjc + Rθcs + Rθsa chain applies, and the thermal paste or pad at the Rθcs interface is the variable the technician can control."

#### Slide 21: Thermal Interface Materials — Paste, Pads, and Phase Change
**Visual:** Three photos — (1) fresh thermal paste application (correct — thin, even coverage); (2) dried/cracked thermal paste (wrong — visible gaps, discolouration); (3) thermal pad (correct vs missing)
**Instructor Script:**
> "The thermal interface material fills the microscopic air gaps between the power stage IC's package base and the heatsink or ECU housing surface. Air has very poor thermal conductivity — microscopic air gaps dramatically increase the case-to-heatsink thermal resistance.
>
> Types of thermal interface material in ECUs:
>
> **Thermal paste (also called thermal compound or thermal grease):**
> Silicone or metal-oxide based compound with thermal conductivity of 1–8 W/m·K. Applied as a thin layer between the package and the heatsink. Over years and thermal cycles, it can dry out, develop voids, or pump out from the interface — leaving air gaps that dramatically increase Rθcs.
>
> **Thermal pads:**
> Pre-cut sheets of thermally conductive silicone or phase-change material. More consistent than paste application but thicker, so higher Rθcs for the same material. Standard in many automotive ECU designs for manufacturing consistency.
>
> **Phase-change materials:**
> Solid at room temperature, melt and flow at operating temperature to fill gaps. Excellent thermal performance once at operating temperature. Difficult to re-apply correctly.
>
> In the hands-on session this afternoon, you will inspect the thermal paste or pad on the power stage of a real ECU, assess whether the application is adequate, and identify any areas where the thermal interface has degraded."

#### Slide 22: Thermal Camera Diagnosis
**Visual:** Thermal camera image of an ECU in operation — colour scale from blue (cool) to red (hot), with power stage components visible as hot spots. Annotation showing temperature readings at different points
**Instructor Script:**
> "A thermal camera transforms invisible heat into a visible image, allowing you to identify hot components without measuring each one individually with a thermometer.
>
> How to use a thermal camera for ECU diagnosis:
>
> 1. Power the ECU on a bench supply in a controlled state — the ECU should be in a defined operating mode (key-on engine-off is typical) so heat generation is consistent
> 2. Allow 5 minutes for temperatures to stabilise at steady state
> 3. Scan the ECU with the thermal camera from a consistent distance (typically 20–30cm)
> 4. Identify the hottest components — typically output driver MOSFETs, voltage regulators, and any component with a shorted internal junction
> 5. Compare the hotspot to adjacent similar components — if one output driver channel is significantly hotter than the others, that channel has a fault (higher current due to shorted load, or higher Rds_on due to degraded MOSFET)
>
> Thermal camera findings that indicate faults:
> - A component that is significantly hotter than its neighbours on the same rail: shorted internal junction, high Rds_on
> - A component that shows no heat at all when it should be dissipating: component is not conducting (open circuit, not reaching the load)
> - Localised PCB hotspot with no obvious component: damaged trace with high resistance joint, dissipating power
>
> Thermal cameras are now available at reasonable cost — a FLIR ONE adapter or equivalent provides useful resolution for ECU diagnostics. In the hands-on session, you will use the workshop thermal camera to scan a powered ECU and rank components by thermal risk."

---

### CLOSING: Concept Check and Session Wrap (Slides 23–25, ~8 minutes)

#### Slide 23: Concept Check — Five Questions
**Instructor Script:**
> "Five questions before the lab."

**Question 1:** An ECU output channel shows the load is permanently ON even when the scan tool commands it OFF. The driver is a low-side type. What has most likely failed and in which mode?
*(Expected: The output MOSFET has failed shorted drain-source. Current path from +12V through load to ground is permanently established regardless of gate signal.)*

**Question 2:** Why would an ECU output driver destroy itself repeatedly after replacement, even though the replacement MOSFET is correctly rated?
*(Expected: The flyback diode is missing or failed open. The inductive kickback spike destroys each replacement MOSFET at the first turn-off event.)*

**Question 3:** On an injector waveform, what does the 'freewheeling plateau' tell you about the circuit?
*(Expected: The flyback diode is conducting and clamping the voltage at (Vsupply + 0.7V). The stored inductor energy is safely dissipating through the diode. The driver MOSFET is protected.)*

**Question 4:** A component has Rθja = 50°C/W. It dissipates 2W. The ambient temperature in the engine bay is 90°C. What is the junction temperature?
*(Expected: Tj = 90 + (50 × 2) = 90 + 100 = 190°C)*

**Question 5:** A customer says their car has an intermittent ECU fault that only occurs in summer after 30 minutes of driving and never occurs in winter. What does this suggest, and what tool would you use to investigate?
*(Expected: A thermal margin problem — a component is operating close to its thermal limit and the elevated summer ambient pushes it over. Investigate with a thermal camera after a controlled warm-up period, looking for an abnormal hotspot on the ECU.)*

#### Slide 24: Summary — Day 6 Theory
**Visual:** Summary list, three sections
**Instructor Script:**
> "Day 6 Theory summary:
>
> **Output drivers:**
> - Low-side: MOSFET switches load to ground. N-channel, simple gate drive, common for injectors and solenoids. Shorted = load stuck on. Open = load always off.
> - High-side: MOSFET supplies +12V to load. Requires charge pump for N-channel gate drive. Used for motors, heated seats. Same failure modes.
>
> **Flyback diodes:**
> - Parallel with inductive load, reverse polarity. Clamps inductive kickback to (Vsupply + 0.7V) during driver turn-off.
> - Missing or failed flyback diode: kickback reaches 100–200V, destroys driver MOSFET. Fault repeats after replacement if root cause is not addressed.
> - Healthy injector waveform: peak phase, hold phase, freewheeling plateau. Each phase is a diagnostic data point.
>
> **Thermal management:**
> - Tj = Ta + (Rθja × P). Junction temperature depends on ambient temperature, power dissipation, and thermal resistance.
> - Higher ambient = less thermal margin. Components that worked in winter may fail in summer.
> - Rθcs (case-to-heatsink) is the only thermal resistance you can affect in repair — via thermal paste or pad quality.
> - Thermal camera identifies hotspots for diagnosis."

#### Slide 25: Hands-On Session Preview — This Afternoon
**Visual:** Equipment list for the afternoon lab
**Instructor Script:**
> "This afternoon in Session 06H, you will:
>
> - Analyse oscilloscope captures of injector drive signals — some healthy, some with planted faults — and identify the anomaly in each
> - Test a suspected failed output driver IC using multimeter resistance measurements and interpret against expected values
> - Use the thermal camera to scan a powered ECU and identify hot components
> - Inspect thermal paste application on a power stage
>
> Use the concept check questions you just answered as your preparation framework. Each activity connects to one of the five questions. If you are confident answering the questions, you are ready for the lab."

---

## Instructor Notes

### Preparation Required
- **Oscilloscope waveform images:** Source or capture real injector drive waveforms — healthy peak-and-hold, missing flyback spike, and open circuit example — at high resolution for slides 14 and 15. If access to a running engine and injector driver is available, capture these live before the course.
- **Physical samples to pass around:** One failed MOSFET (D2PAK package); one flyback diode (SMA package or similar); one common driver IC (e.g. VN7040 or BTS443P in TO-263 package). Holding these while discussing failure modes makes the content tangible.
- **Thermal equation worked example (Slide 18):** Do this on the whiteboard in real time — do not put the full calculation on the PPT slide. The whiteboard working shows students the mathematical thinking process, not just the answer.

### Anticipated Questions

**Q: Do modern driver ICs have the flyback diode integrated?**
A: Yes, many do. Integrated driver ICs from Infineon (BTS/BTM series), STMicroelectronics (VN series), and TI often include integrated active freewheeling transistors or clamp circuits. However, external discrete flyback diodes are still common, especially on older ECU designs and for relay outputs. Always check the specific driver IC datasheet.

**Q: How do you find the Rθja of a component on an unknown ECU?**
A: Identify the IC from its package marking (manufacturer + part number). Locate the datasheet online — Rθja is in the electrical characteristics or thermal characteristics table. If the datasheet is not findable (some automotive-specific ICs are not publicly documented), use a conservative estimate based on package type: D2PAK typically 30–50°C/W, TO-252 typically 40–70°C/W, SOIC-8 typically 100–160°C/W.

**Q: What is the difference between thermal shutdown and a permanent thermal failure?**
A: Thermal shutdown is a reversible protection — the IC detects that its junction temperature has reached the shutdown threshold (typically 150–175°C) and disables itself. When it cools, it restarts. This produces an intermittent fault that disappears when the vehicle cools. A permanent thermal failure means the junction temperature exceeded the maximum rated temperature and the silicon itself was damaged — doped regions diffuse, oxide layers break down. This produces a permanent fault that does not recover on cooling.

### Timing Adjustment
- The thermal equation worked example (Slide 18) is the most time-expandable section. A strong class can cover it in 5 minutes; a class less comfortable with mathematics needs 8–10 minutes with questions. Adjust accordingly.
- If the driver type comparison (Slides 7–9) is taking too long, condense by stating the key diagnostic rule: "Low-side output pin reads near 0V when active. High-side output pin reads near +12V when active. Now you can always determine which type you have by probing the output connector." Move on.

### Assessment Alignment
- so-3-5-1 through so-3-5-3: assessed in Session 06H via waveform analysis and driver testing
- so-3-6-1: assessed in Session 06H via thermal camera exercise and in Module 3 written assessment
- The concept check (Slide 23) directly mirrors the assessment format

---

## PPT Slide Summary

| Slide | Title | Time |
|-------|-------|------|
| 1 | Title — The Output Stage | 2 min |
| 2 | What the Output Stage Does | 3 min |
| 3 | Today's Three Topics | 3 min |
| 4 | The Load Circuit — Where the Driver Fits | 3 min |
| 5 | Low-Side Driver — How it Works | 5 min |
| 6 | Low-Side Driver Failure Modes | 4 min |
| 7 | High-Side Driver — How it Works | 5 min |
| 8 | High-Side vs Low-Side — Choosing Between Them | 3 min |
| 9 | Identifying Driver Types on Schematic and PCB | 2 min |
| 10 | The Inductive Kickback Problem | 5 min |
| 11 | How the Flyback Diode Works | 5 min |
| 12 | Flyback Diode Location — On-Board vs External | 3 min |
| 13 | What Happens When the Flyback Diode is Missing | 4 min |
| 14 | The Injector Waveform — Peak and Hold | 5 min |
| 15 | Waveform Anomalies — What Faults Look Like | 3 min |
| 16 | The Temperature Problem | 2 min |
| 17 | What is Junction Temperature? | 4 min |
| 18 | Working Through the Thermal Equation | 5 min |
| 19 | Component Derating | 4 min |
| 20 | Thermal Resistance — Understanding the Heat Path | 4 min |
| 21 | Thermal Interface Materials | 3 min |
| 22 | Thermal Camera Diagnosis | 4 min |
| 23 | Concept Check — Five Questions | 5 min |
| 24 | Session Summary | 3 min |
| 25 | Hands-On Preview | 2 min |
| **Total** | | **~90 min** |
