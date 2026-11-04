# SESSION-05T: Power Protection, Filtering & EMI
## Instructor-Led Theory Framework

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 3 — ECU Architecture, Protection & Filtering (Days 4–6)
**Session:** Day 5 — Theory  [CRITICAL SESSION — confirmed curriculum gap]
**Duration:** 90 minutes
**Format:** Instructor-led lecture with whiteboard worked examples and physical component samples
**PPT Target:** 28–32 slides

---

## Session Outcomes

| SO ID | Description | Bloom |
|-------|-------------|-------|
| so-3-2-1 | Explain load dump (ISO 7637), TVS diodes, and Zener clamps | Understand |
| so-3-3-1 | Explain bulk capacitor function during cranking voltage dips | Understand |
| so-3-3-2 | Explain decoupling/bypass capacitor function at IC power pins | Understand |
| so-3-3-3 | Identify ferrite beads on power traces and explain their high-frequency noise blocking role | Apply |
| so-3-3-4 | Explain common-mode chokes on CAN/LIN bus lines | Understand |
| so-3-3-5 | Explain RC filter function on analog sensor input lines | Understand |
| so-3-4-1 | Distinguish differential-mode and common-mode noise | Understand |
| so-3-4-2 | Explain pi-filter (cap-ferrite-cap) vs single capacitor | Understand |
| so-3-4-3 | Explain PCB layout EMC rules | Understand |

---

## Why This Session Exists — Instructor Context

This session covers the content identified as a confirmed gap in existing ECU technician training curricula. Most ECU training focuses on the processor, programming, and driver circuits. The filtering and protection content is typically either absent or reduced to a single slide that says "these components protect against noise" — which is not sufficient for a competent repair technician.

A technician who understands this content can diagnose:
- Why an ECU resets during engine cranking (dried bulk capacitor)
- Why a CAN bus throws errors when the alternator is loaded (common-mode choke failure)
- Why a sensor input reads erratically in hot conditions (open RC filter capacitor)
- Why a replacement ECU fails within a week (original failure was load dump destroying the TVS; protection was not restored)

Every concept in this session corresponds to a real, common failure mode. Teach each component as: what it does physically, what the vehicle environment threat is, and what the failure signature looks like.

---

## Module 3 Narrative Thread

> "Yesterday you learned where everything is on the board. Today you learn *why* it is there. The automotive electrical environment is hostile — voltages that spike to 40V, noise that reaches hundreds of millivolts on supply rails, common-mode interference injected onto every wire in the harness from the alternator and ignition system. Every filtering component you identified yesterday is a specific defence against a specific threat. Today we name the threats and explain exactly how each defence works — and what happens when it fails."

---

## INSTRUCTOR STORY ARC

### OPENING HOOK (Slides 1–3, ~8 minutes)

#### Slide 1: Title — The Hostile Environment
**Visual:** Oscilloscope trace showing a real load dump transient — voltage spiking from 14V to over 35V then decaying over ~400ms — overlaid on a photo of an ECU with a burned TVS diode or protection circuit
**Instructor Script:**
> "This oscilloscope trace is a load dump event — a real one, captured during alternator disconnection on a running engine. The voltage went from 14V to over 35V in under 400 microseconds.
>
> The ECU that was connected to this bus had a TVS diode that had already failed shorted on a previous event — it had been replaced with a standard diode, not a TVS. The overvoltage reached the MCU's power pins. The MCU was destroyed — not burned visibly, just silent silicon junction breakdown. The ECU looked completely fine. It was dead.
>
> The technician who received that ECU spent two hours checking wiring and connectors before measuring the supply rail. He found 14.2V — perfectly normal. He never found the root cause, and the next replacement ECU failed three months later.
>
> Today you will understand exactly what happened, how to prevent it recurring after repair, and how to test every component in that protection chain."

#### Slide 2: The Automotive Electrical Environment — Five Threats
**Visual:** Table — five threat categories with source, characteristic, and the component category that defends against each

| Threat | Source | Characteristic | Defence |
|--------|--------|----------------|---------|
| Load dump transient | Alternator disconnection under load | Up to 40V, microseconds to milliseconds | TVS diode |
| Reverse polarity | Incorrect battery connection | −12V to −16V, continuous | Series diode or P-channel MOSFET |
| Cranking voltage dip | Engine starting, starter motor current | 7–8V for 50–200ms | Bulk capacitor |
| High-frequency rail noise | Switching ICs, PWM drivers, alternator ripple | 100kHz to 100MHz, mV to volts | Ferrite beads, bypass caps, pi-filter |
| Common-mode noise on bus lines | Alternator, ignition, inductive loads | Affects both bus wires equally | Common-mode choke |

**Instructor Script:**
> "There are five categories of electrical threat that automotive ECU designers must defend against. Here they are in one table. Today we go through all five — one component category per threat.
>
> Notice that each threat has a different time characteristic. Load dump is microseconds to milliseconds — too fast for a fuse to blow. Cranking dip is 50 to 200 milliseconds — too short for a voltage regulator to correct from the battery alone. Rail noise is continuous — present every time the engine runs. Each defence is specifically tuned for its threat."

#### Slide 3: The Learning Framework for This Session
**Visual:** Three-column diagram — 'What it does (physics)' / 'What threat it stops (vehicle context)' / 'What happens when it fails (diagnostic)'
**Instructor Script:**
> "Here is the framework I want you to apply to every component we cover today. Three questions:
>
> 1. What does it do? — the physics of how it works
> 2. What vehicle threat does it stop? — the context in the real vehicle
> 3. What happens when it fails? — the symptom you will find in the workshop
>
> If you can answer those three questions for every component in today's session, you can diagnose any ECU power or noise problem from first principles — even on an ECU you have never seen before, with no service manual. Let us begin."

---

### PART 1: Transient Protection — Load Dump, TVS Diodes, and Zener Clamps (Slides 4–8, ~18 minutes)

#### Slide 4: The Load Dump Event — ISO 7637
**Visual:** Waveform diagram of a load dump transient per ISO 7637 Pulse 5a — voltage on Y axis, time on X axis, annotated with: peak voltage (40V), rise time (~5µs), decay time (~400ms), normal supply voltage (14V)
**Instructor Script:**
> "A load dump occurs when a large electrical load — or the alternator output itself — is suddenly disconnected from the battery while the alternator is producing current.
>
> The alternator is a current source. When the load it was driving suddenly disappears, the alternator's magnetic field energy has nowhere to go. It drives the supply rail voltage up.
>
> ISO 7637 is the automotive standard that quantifies this transient. Test Pulse 5a defines the worst case for a 12V system:
> - Peak voltage: up to 40V
> - Rise time: approximately 1 to 5 microseconds
> - Decay time: 200 to 400 milliseconds
>
> For context: the MCU's absolute maximum supply voltage is typically 5.5V or 3.6V depending on the device. The 5V regulator feeding the MCU has an absolute maximum input of maybe 50V. But the input capacitors and other components in the power path may have ratings as low as 25V.
>
> A 40V spike arriving at the ECU connector without protection will permanently destroy at least one component in the power input stage — every single time. The question is only which component fails first.
>
> The TVS diode is designed to absorb that spike before it travels further than the first protection component."

#### Slide 5: TVS Diodes — How They Work
**Visual:** Circuit diagram — battery positive → fuse → TVS diode (between rail and ground) → protected downstream circuit. Inset: TVS diode I-V curve showing normal reverse bias region then sharp breakdown knee at Vc
**Instructor Script:**
> "A TVS diode — Transient Voltage Suppressor — is placed between the supply rail and ground, as close to the ECU's power input connector as possible.
>
> Normal operation: The supply rail is at 14V. The TVS diode's breakdown voltage (clamping voltage) is set at 28V to 33V for a 12V system application. The diode is reverse biased and conducts no current. The circuit does not know it is there.
>
> During a load dump: The rail voltage rises past 28V. The TVS enters avalanche breakdown. It conducts heavily — the datasheet peak current rating is typically 50 to 200A for a fraction of a millisecond. The diode diverts the transient energy to ground, clamping the rail at the breakdown voltage. Everything downstream of the TVS never sees more than the clamping voltage.
>
> The TVS must absorb the entire transient energy before the voltage reaches a protected IC. The peak pulse power rating of the TVS must exceed the peak load dump energy.
>
> Key parameters to know:
> - **Clamping voltage (Vc):** Voltage at which it conducts under rated test current — must be below the absolute maximum of downstream ICs
> - **Peak pulse power (Ppk):** Energy it can absorb in a single pulse — automotive grade typically 600W to 1500W for power line protection
> - **Response time:** Sub-nanosecond for TVS devices — effectively instantaneous for transient protection purposes
> - **Unidirectional vs bidirectional:** Unidirectional TVS blocks one polarity only (correct for DC supply lines). Bidirectional TVS clamps both polarities (used on AC signal lines)."

#### Slide 6: TVS Diode Failure Modes and Testing
**Visual:** Two circuit states — left: TVS shorted (supply rail pulled to near ground); right: TVS open (no protection, downstream at risk)
**Instructor Script:**
> "TVS diodes fail in two ways:
>
> **Failed shorted — the most common failure after absorbing a severe load dump:**
> The avalanche current exceeded the TVS's peak pulse power rating. The junction melted into a permanent short. The supply rail is now pulled directly to ground through the TVS. Result: ECU completely dead. No power reaches any circuit.
>
> Test: Diode function test across the TVS. A healthy TVS: forward voltage 0.5 to 0.7V in the forward direction, open circuit (OL) in the reverse direction (below clamping voltage). A shorted TVS: near-zero voltage in both directions, or very low resistance reading in ohms mode.
>
> **Failed open — less common, but more dangerous:**
> The TVS has an internal open circuit. The supply rail functions normally. The ECU appears healthy. But the next load dump event will pass through to the downstream components unimpeded.
>
> Test: Same diode function test. Open TVS reads OL in both directions rather than forward voltage in one direction.
>
> Critical repair point: whenever you receive an ECU with a completely dead supply rail, the TVS is your first test point — before you condemn the voltage regulator or trace further upstream. A shorted TVS is the most common cause of a dead ECU supply after a vehicle electrical event. Replacing the TVS is not the complete repair — you must understand what caused the load dump in the first place."

#### Slide 7: Zener Clamps on Signal Lines
**Visual:** Circuit diagram — sensor input line with series resistor and Zener diode to ground at the MCU pin, annotated with example values (5.6V Zener, 10kΩ series R)
**Instructor Script:**
> "You will also encounter Zener diodes used as clamps on individual signal lines — particularly analog sensor inputs and communication lines.
>
> A Zener diode on a 5V sensor input line is set to a clamping voltage slightly above the normal signal range — typically 5.6V or 6.2V. Under normal operation, the sensor signal swings between 0V and 5V; the Zener is reverse biased and invisible to the circuit.
>
> If an ESD strike or wiring fault injects a voltage spike onto the sensor wire — which absolutely happens in service when a technician back-probes a connector with a nearby inductive load — the Zener clamps the spike to 5.6V. The MCU ADC input pin, with an absolute maximum of 6V, survives.
>
> Without the Zener: the spike passes directly to the ADC input pin. The gate oxide on the MOSFET input transistor inside the MCU ruptures. The MCU develops a damaged ADC channel — it reads an incorrect value forever, or the pin fails completely.
>
> Testing: Same as TVS. Diode function test in forward and reverse directions. Forward: 0.5 to 0.7V. Reverse at test current: should block. If reverse reads low voltage or low resistance: Zener is shorted — replace before the next voltage spike destroys the MCU ADC input."

#### Slide 8: The Complete Power Entry Protection Stage
**Visual:** Full schematic of a typical ECU power entry — connector pin → fuse → TVS to ground → reverse polarity protection (diode or MOSFET) → bulk capacitor to ground → LDO/switching regulator → 5V regulated rail
**Instructor Script:**
> "Let us put the complete protection picture together before moving to filtering.
>
> At the power entry of a well-designed ECU, tracing from the connector inward, you pass through:
>
> 1. **Connector and fuse** — overcurrent protection and mechanical entry
> 2. **TVS diode** — clamps load dump transients
> 3. **Reverse polarity protection** — blocks reversed battery connection
> 4. **Bulk capacitor** — ride-through energy during cranking voltage dip
> 5. **Voltage regulator** — converts 9–16V battery range to stable 5V or 3.3V for ICs
>
> Each stage targets a specific threat. If any stage fails, the next stage is exposed to a threat it was not designed to handle. A missing TVS means the reverse polarity diode must absorb load dump energy — it is not rated for this and will fail immediately.
>
> Diagnostic methodology: when tracing a power supply fault, start at the connector and move inward, testing each stage in order. Do not jump to the voltage regulator before verifying the TVS."

---

### PART 2: Capacitor Filtering — Bulk Capacitors and Bypass Capacitors (Slides 9–14, ~20 minutes)

#### Slide 9: Two Capacitors, Two Completely Different Jobs
**Visual:** Side-by-side photo — large electrolytic capacitor (470µF, 25V, 8mm diameter) next to tiny ceramic chip capacitor (100nF, 0402 package, 1mm long) with a ruler for scale
**Instructor Script:**
> "Capacitors appear on ECU boards in two fundamentally different roles. Confusing these roles leads to wrong diagnoses and wrong repairs.
>
> **Bulk capacitor:** Large electrolytic, 100µF to 1000µF or more, located near the main power input. Job: energy storage and ride-through during the cranking voltage dip. This is a slow, low-frequency role — it supplies hundreds of milliamps for hundreds of milliseconds.
>
> **Bypass capacitor (also called decoupling capacitor):** Small ceramic, 100nF or 10nF, located immediately adjacent to an IC's VCC pin — within 2 to 3mm. Job: high-frequency noise suppression, local to the IC. This is a fast, high-frequency role — it supplies microsecond current spikes within centimetres of the IC.
>
> Same basic component type. Different size by a factor of 5,000 to 10,000. Completely different job. Let us cover each one in detail."

#### Slide 10: The Cranking Voltage Dip — The Threat Bulk Capacitors Defend Against
**Visual:** Oscilloscope trace of battery terminal voltage during engine cranking — voltage dropping from 12.6V to approximately 7.5V for ~150ms then recovering to 13.5V (charging)
**Instructor Script:**
> "When the engine starts, the starter motor draws 100 to 300 amps from the battery for the duration of cranking — typically 50 to 200 milliseconds.
>
> This current draw causes the battery terminal voltage to dip. A healthy battery, warm engine, short crank: dip to 9–10V. Cold morning, weak battery, high compression diesel: dip to 6–7V for 200ms or more.
>
> During this dip, the ECU must keep operating. It is managing the crank-to-run transition — processing crankshaft position sensor pulses, calculating injection timing, commanding injectors.
>
> The voltage regulator inside the ECU (a linear regulator or buck converter) can maintain its 5V output only as long as its input voltage stays above its dropout voltage — typically 6.5 to 7V for a low-dropout regulator.
>
> If the battery voltage dips below that threshold:
> - The regulator output drops
> - The 5V rail drops below the MCU's minimum supply voltage
> - The MCU resets
> - When it reboots, it has lost its position in the engine cycle
>
> The bulk capacitor is the energy buffer that maintains the input voltage to the regulator during this dip."

#### Slide 11: How Bulk Capacitors Work — The Energy Equation
**Visual:** Circuit diagram showing bulk capacitor in parallel with the supply rail before the voltage regulator. Whiteboard space for working through the energy calculation
**Instructor Script:**
> "The energy stored in a capacitor is:
>
> **E = ½ × C × V²**
>
> Let us work through a practical example on the board.
>
> Assumptions:
> - ECU draws 500mA from the 5V regulator (a typical midsize engine ECU)
> - The 5V LDO regulator draws approximately 600mA from the 12V supply (accounting for regulator efficiency ~60%)
> - The cranking dip takes the rail from 12V down to 6.5V (regulator dropout) over 150ms
>
> Charge the capacitor must supply during the dip:
> **Q = I × t = 0.6A × 0.15s = 0.090 coulombs**
>
> Voltage the capacitor can contribute — from 12V initial down to 6.5V minimum:
> **ΔV = 12 − 6.5 = 5.5V**
>
> Capacitance required:
> **C = Q / ΔV = 0.090 / 5.5 = 0.0164 farads = 16,400µF**
>
> In practice, ECUs use 220µF to 1000µF because:
> 1. Multiple bulk capacitors in parallel contribute total capacitance
> 2. The battery voltage rarely drops instantaneously to 6.5V — the dip has a sloped profile that the regulator partially tracks
> 3. Modern switching regulators have better hold-up than linear regulators
>
> The key principle: bulk capacitors are sized for a specific cranking profile. Replacing a failed 470µF cap with a 47µF cap because it physically fits the footprint will cause cranking reset faults. Always match or exceed the original capacitance value."

#### Slide 12: Bulk Capacitor Failure — The Dried-Out Electrolytic
**Visual:** Photo showing: (1) a visibly bulged capacitor vs a healthy one; (2) an LCR meter reading '23µF' where the capacitor is marked '470µF'
**Instructor Script:**
> "Electrolytic capacitors fail in a specific and predictable way: the electrolyte dries out over time and thermal cycling.
>
> As the electrolyte dries out:
> - Capacitance decreases — sometimes to less than 5% of rated value
> - Equivalent Series Resistance (ESR) increases — the capacitor becomes lossy and cannot deliver burst current efficiently
>
> In severe cases, internal pressure from gas generation causes the capacitor's vent to open and the top to bulge. This is a visible failure indicator. However, many capacitors lose the majority of their capacitance with no visible sign — they look completely normal.
>
> Vehicle symptom profile:
> - ECU resets or engine fails to start on cold mornings only
> - Engine starts normally when warm (shallower crank voltage dip)
> - Fault codes: multiple sensors out of range at key-on, or ECU communication lost code from the CAN network during crank
> - No fault codes once engine is running — the bulk cap failure only manifests during the brief cranking event
>
> Diagnosis: Remove the suspect capacitor (or measure in-circuit with an ESR meter). Measure capacitance with an LCR meter. Below 80% of rated value: replace. Any visible bulging: replace without further testing.
>
> Multimeter limitation: a standard multimeter cannot measure capacitance with sufficient accuracy to detect a degraded electrolytic. You need an LCR meter or ESR meter. If you do not have one, the capacitor's age and the vehicle's symptoms must guide the decision."

#### Slide 13: Bypass Capacitors — The High-Frequency Problem at IC Power Pins
**Visual:** Diagram showing IC switching its internal transistors → current spikes on VCC pin → rail noise without bypass cap (showing noise ripple on the rail) vs clean rail with bypass cap. Inset: close-up of PCB showing 100nF ceramic cap placed right at an IC VCC pin
**Instructor Script:**
> "Every digital IC — the MCU, the CAN transceiver, the RAM, the voltage reference — switches its internal transistors millions of times per second. Each switching event draws a brief, sharp current spike from the VCC supply pin.
>
> These current spikes propagate back through the supply trace to the power rail. The inductance of even a short copper trace — just a few nanohenries — converts these current spikes into voltage noise on the rail:
>
> **V = L × (dI/dt)**
>
> For a trace with 5nH inductance and a current spike of 100mA in 1ns:
> V = 0.000000005 × (0.1 / 0.000000001) = 0.5V of noise
>
> Half a volt of noise on a 5V supply rail that every IC on that rail shares. This noise causes:
> - Random logic errors in digital circuits processing the same rail
> - ADC measurement errors — the noise appears as phantom signal variations
> - Increased RF emissions — the ECU fails EMC testing
>
> The bypass capacitor intercepts this noise locally. Placed within 2 to 3mm of the IC's VCC pin, the capacitor has very low impedance at high frequencies. When the switching current spike occurs, the capacitor supplies that current locally from its stored charge — the spike does not propagate back down the trace to other ICs.
>
> This is why placement is critical. A bypass capacitor 10mm from the IC has 10mm of trace between it and the VCC pin — that trace has inductance, and inductance at high frequency defeats the purpose. The bypass capacitor must be physically adjacent to the IC pin it serves."

#### Slide 14: Bypass Capacitor Values, Layout, and Failure
**Visual:** PCB layout diagram showing correct vs incorrect bypass capacitor placement relative to IC VCC pin. Table of typical capacitor values and their frequency coverage
**Instructor Script:**
> "Bypass capacitors are ceramic — not electrolytic. Common values:
> - **100nF (0.1µF):** Optimal for 10–50MHz frequency range — the primary bypass capacitor at every IC VCC pin
> - **10nF (0.01µF):** Extends coverage to higher frequencies, sometimes placed in parallel with the 100nF
> - **1µF to 10µF ceramic:** Low-frequency bulk local bypass; sometimes placed at larger ICs or power management stages
>
> The reason for multiple values: a single capacitor has a self-resonant frequency at which its impedance is minimum and above which it actually becomes inductive. Using multiple values in parallel shifts the effective self-resonant frequency and extends the frequency range of effective bypassing.
>
> Failure modes:
> **Cracked ceramic (thermal shock):** Ceramic capacitors are brittle. PCB flexing during engine vibration, or thermal cycling between cold starts and operating temperature, can crack the ceramic body. The capacitor either opens (no longer bypasses) or shorts (pulls IC VCC pin to ground — IC dies).
>
> **Removed during rework:** The most common way bypass capacitors are damaged — a technician reworks the area near an IC and inadvertently removes a nearby bypass cap with a hot-air gun or soldering iron.
>
> Effect of a missing bypass cap: The IC may work under clean bench conditions. In the vehicle, with EMI from the alternator and ignition, the IC becomes intermittently unstable. This produces the hardest category of fault to diagnose: an ECU that works on the bench but fails in the vehicle.
>
> Rule: After any rework near an IC, inspect every capacitor within 5mm. Verify continuity to the ground plane. Replace any suspect bypass capacitor."

---

### PART 3: Ferrite Beads — High-Frequency RF Suppression on Power Traces (Slides 15–17, ~12 minutes)

#### Slide 15: What is a Ferrite Bead and How Does it Work?
**Visual:** Photo of surface-mount ferrite bead (0402) next to schematic symbol (inductor symbol with filled core). Impedance vs frequency curve: low impedance at DC and low frequency (0.5 ohms), rising to 300–600 ohms at 100MHz
**Instructor Script:**
> "A ferrite bead is a surface-mount component placed in series with a power supply trace. Physically, it looks exactly like an 0402 or 0603 resistor — same black body, same size, same appearance. You cannot distinguish it from a resistor visually. You distinguish it by reference designator (L prefix) and by DC resistance measurement (ferrite bead: near-zero; resistor: rated value).
>
> How it works:
>
> At DC and low frequencies — the 12V supply, slow voltage changes, audio-frequency ripple — the ferrite bead presents very low impedance. Typically 0.1 to 2 ohms DC. The supply current passes through with almost no voltage drop. The bead is effectively invisible to the DC supply.
>
> At high frequencies — the MHz range where EMI and switching noise live — the ferrite material becomes magnetically lossy. The bead presents high impedance: typically 100 to 600 ohms at 100MHz. High-frequency noise on the supply trace cannot pass through. It is absorbed — converted to a tiny amount of heat in the ferrite material.
>
> This is the critical distinction from a standard inductor: a standard inductor is reactive — it stores energy and reflects it as back-EMF. A ferrite bead is resistive at high frequencies — it absorbs and dissipates the energy. On a power supply line in an ECU, you want dissipation, not reflection. Reflected EMI bounces back and forth, potentially causing resonance and worse noise problems."

#### Slide 16: Where Ferrite Beads Are Placed on ECU Boards
**Visual:** ECU power supply schematic section showing ferrite beads placed: (1) on main supply rail feeding MCU, (2) on CAN transceiver supply, (3) on oscillator supply, (4) on ADC VREF line
**Instructor Script:**
> "Ferrite beads are placed in series on power supply lines for specific ICs or circuit sections that are either:
> (a) sensitive to noise — the MCU, the oscillator, the ADC voltage reference, or
> (b) sources of noise that must be isolated from reaching sensitive circuits — PWM driver ICs, CAN transceivers
>
> Typical placements you will see:
>
> - **Main supply rail to MCU:** A ferrite bead between the main 5V rail and the MCU's VCC pin(s). Blocks noise generated by driver circuits from reaching the MCU.
> - **CAN transceiver supply pin:** The transceiver operates at high data rates and is sensitive to supply noise. A ferrite bead on its VCC pin is almost universal on automotive ECUs.
> - **Oscillator supply:** The crystal oscillator is the most noise-sensitive circuit on the board. Its supply almost always has a ferrite bead plus bypass cap.
> - **ADC VREF (voltage reference):** Any noise on the ADC voltage reference appears directly as error in every analog measurement the ECU makes. The VREF supply always has strong filtering — typically ferrite bead plus multiple bypass caps.
>
> Placement pattern: On ECU boards, a ferrite bead is almost always followed immediately by a bypass capacitor to ground. The combination is the high-frequency section of the pi-filter architecture we will discuss shortly."

#### Slide 17: Ferrite Bead Failure Modes and Testing
**Visual:** Two-column diagram — left: open bead with no power to IC. Right: shorted bead with noise passing through. Test results for each.
**Instructor Script:**
> "Ferrite beads fail in two ways with completely different symptoms:
>
> **Failed open — the serious failure:**
> The ferrite bead develops an open circuit internally. No supply voltage can reach the IC it feeds. The IC is completely dead.
>
> Symptom: A specific IC or circuit section is completely non-functional while adjacent circuits on the same raw supply rail work normally. For example: MCU is dead but the CAN transceiver (on a separate supply branch without the failed bead) is responding on the bus.
>
> Test: With the board powered, measure voltage before and after the bead. Voltage present before the bead (on the supply side) but absent after it (on the IC side) = open bead. With board unpowered: DC resistance OL on the multimeter in ohms mode.
>
> This is why you check DC resistance of every L-designated component near a dead IC before condemning the IC itself. Replace the bead; power up; retest the IC.
>
> **Failed shorted — the subtle failure:**
> The ferrite bead fails internally as a short circuit. DC resistance drops to near zero. The supply voltage reaches the IC, so the IC functions. But the high-frequency impedance collapses — the bead no longer filters EMI.
>
> Symptom: The IC works but the ECU has increased noise emissions. Intermittent CAN communication errors under high electrical noise conditions. Erratic sensor readings in the vehicle but clean on the bench. Fails EMC re-test after repair.
>
> Test: DC resistance of a healthy bead is 0.1 to 2 ohms. A shorted bead is also near-zero — nearly indistinguishable by DC resistance alone. Definitive test requires AC impedance measurement at 10MHz with an LCR meter. Alternatively, compare with a known-good bead of the same part number on the same board (adjacent supply rail)."

---

### PART 4: Bus Line Filtering — Common-Mode Chokes and RC Filters (Slides 18–21, ~15 minutes)

#### Slide 18: Differential-Mode vs Common-Mode Noise — Understanding the Difference
**Visual:** Two diagrams:
- Left: Differential-mode noise — noise appears between the two wires (one wire high, other wire low), corrupts the differential data signal
- Right: Common-mode noise — same noise voltage on both wires simultaneously, the differential receiver subtracts and cancels it
**Instructor Script:**
> "Before we discuss bus filtering components, you need to understand the difference between differential-mode and common-mode noise. Which type of noise you are dealing with determines which component you need.
>
> **Differential-mode noise:** Noise that appears with opposite polarity on the two wires of the bus pair. On CAN: noise on CAN_H that is opposite to noise on CAN_L. This noise adds directly to the intended voltage difference between the two wires. It corrupts the data signal. The receiver cannot distinguish intentional data from differential noise.
>
> **Common-mode noise:** Noise that appears with the same polarity and same amplitude on both wires simultaneously. On CAN: the same noise voltage riding on both CAN_H and CAN_L.
>
> The CAN receiver measures (CAN_H − CAN_L). If common-mode noise is +2V on both wires: (CAN_H + 2V) − (CAN_L + 2V) = CAN_H − CAN_L. The noise cancels in the subtraction. The data is unaffected.
>
> This is why CAN bus uses differential signaling — it has inherent immunity to common-mode noise. This is its primary noise immunity mechanism.
>
> However: if the common-mode noise is large enough to exceed the CAN transceiver's common-mode input range (typically ±12V for automotive CAN), the receiver's input stage saturates and it cannot operate correctly. In this case, even common-mode noise corrupts communication.
>
> The automotive environment produces very large common-mode noise because alternator ripple and ignition transients are injected capacitively and inductively onto the entire wiring harness. Both CAN_H and CAN_L run through the same harness and pick up the same noise — classic common-mode. This is exactly the threat the common-mode choke is designed for."

#### Slide 19: Common-Mode Chokes on CAN and LIN Lines
**Visual:** Schematic symbol and physical appearance (SOIC-8 or chip package) of a common-mode choke. Winding diagram: two coils on the same core, wound in opposition. Two signal path diagrams: differential current (fields cancel = passes through), common-mode current (fields add = blocked)
**Instructor Script:**
> "A common-mode choke consists of two windings wound on the same ferrite core, in opposite directions — one winding for CAN_H, one winding for CAN_L.
>
> For differential CAN signals:
> The differential signal on CAN_H and CAN_L produces opposite currents in the two windings. The magnetic fields created by these opposite currents cancel each other out. The ferrite core sees no net magnetic flux. The choke presents near-zero impedance to the differential signal. Data passes through completely unchanged.
>
> For common-mode noise:
> Common-mode noise is the same polarity on both wires — same current direction in both windings. The magnetic fields from the two windings add together rather than cancelling. The core saturates with magnetic flux. The choke presents high impedance to this common-mode current. The noise is blocked from reaching the transceiver IC.
>
> The result: a common-mode choke is invisible to wanted differential CAN/LIN data but presents a significant barrier to unwanted common-mode noise. It is the correct component for the exact noise profile of the automotive harness environment.
>
> Location on ECU boards: Common-mode chokes appear on CAN and LIN bus traces between the connector and the transceiver IC. They are typically compact 4-pin packages (2 pins per winding). Reference designator: L or T.
>
> Failure modes:
> - **Open winding:** One half of the choke is broken. That bus line is interrupted — CAN or LIN communication on the affected bus fails completely. Identify: continuity test of each winding (should be near-zero ohms). Open winding reads OL.
> - **Shorted turns:** Winding insulation breaks down, turns short together. Inductance drops. Common-mode noise rejection is reduced. Communication works but intermittent errors increase under EMI conditions."

#### Slide 20: RC Filters on Analog Sensor Input Lines
**Visual:** Schematic showing: sensor → wire in harness → ECU connector pin → series resistor (R, typically 4.7kΩ) → junction point → capacitor to ground (C, typically 10nF) → MCU ADC input. Overlaid with low-pass filter frequency response curve, cutoff frequency labelled
**Instructor Script:**
> "Analog sensor signals carry useful information at low frequencies. A throttle position sensor output changes at 0 to 200Hz — the rate of driver pedal movement. A coolant temperature sensor changes even more slowly, at near-DC. The MCU only needs to sample these at a few hundred hertz to track all meaningful changes.
>
> But the wire running from that sensor through the engine bay harness is an antenna. It picks up:
> - Ignition system noise at 10–50kHz (each spark event)
> - Injector driver switching noise at 5–50kHz
> - Alternator ripple at 600Hz to 3kHz
> - CAN bus signals at 500kHz to 2MHz (if the sensor wire runs near the CAN harness)
>
> If this noise reaches the MCU's ADC input pin, the ADC samples it along with the intended signal. The ECU 'sees' a sensor signal that is jumping up and down at high frequency. This produces: erratic fueling corrections, false out-of-range fault codes, and hard-to-reproduce intermittent faults.
>
> The RC low-pass filter at the ECU input pin removes all noise above the cutoff frequency while passing the useful sensor signal:
>
> **fc = 1 / (2 × π × R × C)**
>
> Worked example — typical MAP sensor input filter:
> R = 4.7kΩ, C = 10nF
> **fc = 1 / (2 × π × 4700 × 0.000000010) = 3,385 Hz ≈ 3.4kHz**
>
> Everything above 3.4kHz is attenuated. The MAP sensor's useful signal content (0–200Hz) passes through with less than 0.1% attenuation. Ignition noise at 50kHz is attenuated by more than 99%.
>
> Design constraint: the capacitor value cannot be made arbitrarily large. A 100nF capacitor would set fc at 340Hz, but then rapid throttle changes would be filtered out — the ECU would respond sluggishly to fast pedal inputs. The cutoff frequency is a deliberate engineering tradeoff between noise rejection and sensor response time."

#### Slide 21: RC Filter Failure Modes — Three Distinct Signatures
**Visual:** Three circuit states with voltage annotations — (1) healthy, (2) capacitor shorted, (3) capacitor open
**Instructor Script:**
> "The RC filter has three distinct failure signatures. Each gives a different measurable symptom:
>
> **Capacitor shorted:**
> The capacitor becomes a low-resistance path to ground. The sensor signal is pulled toward ground through the series resistor. Reading: sensor input stuck near 0V regardless of actual sensor position.
> Vehicle symptom: TPS stuck at 0% throttle. MAP sensor stuck at minimum pressure. Associated fault code: sensor signal low voltage or open circuit.
> Test: With ECU connector disconnected, measure resistance from the input pin to chassis ground. Healthy circuit: input resistance equals the series resistor value (1–10kΩ). Shorted cap: near-zero resistance to ground.
>
> **Capacitor open:**
> The capacitor is no longer in circuit. The low-pass filter no longer functions. The sensor signal passes through the series resistor but is unfiltered — high-frequency noise rides on top of the sensor signal all the way to the ADC pin.
> Vehicle symptom: Sensor reading erratic, oscillating, intermittently generating out-of-range codes. Temperature dependent — capacitor works when cold, opens when hot. Extremely difficult to catch without an oscilloscope.
> Test: Oscilloscope on the MCU ADC input pin with engine running. Healthy signal: clean sensor waveform at the expected frequency. Open cap: sensor waveform with high-frequency noise superimposed.
>
> **Series resistor open:**
> The resistor develops an open circuit. The sensor signal cannot reach the MCU input at all. The ADC input is pulled to the internal bias voltage, typically reading mid-range.
> Vehicle symptom: Sensor reads approximately mid-range regardless of physical position. No continuity between sensor connector pin and MCU pin.
> Test: Continuity/resistance from connector pin to MCU pin. An open resistor reads OL where it should read the resistor's rated value (1–10kΩ)."

---

### PART 5: EMI Architecture — Pi-Filters, PCB Layout, and Ground Planes (Slides 22–27, ~12 minutes)

#### Slide 22: Building Better Filters — Single Capacitor to Pi-Filter
**Visual:** Three circuit diagrams side by side with frequency attenuation curves overlaid:
1. Single capacitor to ground — 20dB/decade attenuation slope
2. L-filter (ferrite bead + capacitor) — 40dB/decade
3. Pi-filter (capacitor + ferrite bead + capacitor) — 60dB/decade
**Instructor Script:**
> "You have now met all the individual filter components. Let us look at how they are combined into the most effective architecture.
>
> **Single capacitor:** Capacitor to ground at the supply input. 20dB per decade attenuation. Simple, cheap, limited — at 100MHz, provides roughly 40dB of attenuation if placed ideally.
>
> **L-filter (ferrite bead + capacitor):** Ferrite bead in series, capacitor to ground after it. The bead raises impedance for incoming noise; the output capacitor provides a low-impedance path to ground for noise that reaches the IC side. 40dB per decade. At 100MHz: roughly 80dB.
>
> **Pi-filter (capacitor + ferrite bead + capacitor):** Input capacitor before the bead, ferrite bead in series, output capacitor after the bead. The input capacitor suppresses noise before it enters the ferrite bead, improving its efficiency. The output capacitor catches any residual noise. 60dB per decade. At 100MHz: roughly 120dB of attenuation.
>
> 120dB means the noise voltage is reduced to one millionth of one percent of its original level. This is why the pi-filter architecture is standard on ECU supply rails for sensitive circuits.
>
> When you trace the supply path to the MCU on a real ECU board and see: a capacitor near the power connector, then a ferrite bead on the trace, then a bypass capacitor right at the MCU — you are looking at a deliberately engineered pi-filter."

#### Slide 23: Pi-Filter — Why the Name, and What Failure Looks Like
**Visual:** Schematic redrawn to show the pi (π) shape — two vertical capacitor branches and one horizontal series ferrite bead, forming the Greek letter shape
**Instructor Script:**
> "The name comes directly from the circuit topology drawn as a schematic. Two capacitors to ground with a series element between them forms the shape of the Greek letter pi — π. This is also called a CLC filter in filter theory.
>
> What happens when one element of the pi-filter is missing or failed:
>
> - **Missing input capacitor:** Pi-filter degrades to an L-filter. Attenuation drops from 60 to 40dB per decade. At 100MHz, this is a loss of roughly 40dB — a factor of 100 in noise voltage. In many cases this is still sufficient. In high-noise environments (diesel engines, near the alternator) it may not be.
>
> - **Open ferrite bead:** Pi-filter becomes two isolated capacitors. The series element is gone. Attenuation drops severely at high frequencies.
>
> - **Missing output (bypass) capacitor:** The IC has no local high-frequency bypass. The ferrite bead has nothing to drain noise into on the IC side. Effective attenuation at the IC's VCC pin drops dramatically.
>
> In practice: a single failed or missing bypass capacitor adjacent to the MCU is the most common cause of an ECU that works on the bench but develops intermittent faults in the vehicle — because the vehicle's EMI environment exposes the gap in the filter architecture."

#### Slide 24: PCB Layout Rule 1 — Bypass Capacitors Must Be Adjacent to the IC
**Visual:** Two PCB layout diagrams — left: bypass capacitor 8mm from IC, trace visible between them (bad); right: bypass capacitor 1.5mm from IC, trace minimal (correct)
**Instructor Script:**
> "The first and most important PCB layout EMC rule: bypass capacitors must be physically adjacent to the IC VCC pin they serve — within 2 to 3mm.
>
> Every millimetre of trace between the bypass capacitor and the VCC pin adds inductance. At high frequencies, inductance limits the current the capacitor can supply — it defeats the purpose of the bypass capacitor.
>
> A bypass capacitor placed 8mm from the VCC pin may provide less effective bypassing at 100MHz than no capacitor at all in the worst case (if the trace inductance creates a resonance that actually amplifies noise at a specific frequency).
>
> When you are reworking an ECU and you accidentally remove a tiny ceramic capacitor near an IC — and it happens to have been a bypass capacitor — place the replacement within 2mm of the IC's VCC pin, with the shortest possible trace to the VCC pin and a direct via to the ground plane."

#### Slide 25: PCB Layout Rule 2 — Ground Connections Must Be Via to Ground Plane
**Visual:** PCB cross-section showing correct ground connection (direct via to ground plane from capacitor ground pad) vs incorrect (long trace to a ground pad on the outer layer)
**Instructor Script:**
> "The second layout rule: every filter capacitor's ground connection must go directly to the ground plane via a via — not along a trace to another ground point on the surface.
>
> A long ground trace has inductance. Inductance in the ground return path degrades the capacitor's effectiveness at high frequencies just as much as inductance in the supply trace does. The filter capacitor's ground terminal must have the lowest possible impedance path to the ground reference.
>
> On modern ECU boards, the bypass capacitor's ground pad has a via directly below it — the shortest possible path to the ground plane. This is not accidental; it is deliberate EMC design.
>
> Repair application: when you repair a torn trace or restore a damaged ground pad, verify that the component's ground connection still has a direct, low-inductance path to the ground plane. A repaired connection that routes through 10mm of surface trace may look cosmetically correct but is electrically inferior."

#### Slide 26: PCB Layout Rule 3 — Separate Noisy Circuits from Quiet Circuits
**Visual:** PCB top view diagram showing physical separation zones: left side = quiet circuits (MCU, ADC, oscillator); right side = noisy circuits (injector drivers, relay drivers, power stage); ground stitching vias between zones
**Instructor Script:**
> "The third layout rule: noise sources and noise-sensitive circuits must be physically separated on the PCB.
>
> Noisy circuits: PWM output drivers, injector drivers, relay drivers, motor drivers. These switch large currents rapidly and generate strong electromagnetic fields.
>
> Noise-sensitive circuits: MCU core and ADC inputs, oscillator circuit, voltage references, CAN/LIN transceivers (despite their noise immunity, they have limits).
>
> The separation is enforced by:
> - Physical distance between the two regions on the PCB
> - Ground plane stitching vias around sensitive circuits — a ring of vias connected to the ground plane acts as a partial Faraday cage, reducing coupling of noise from adjacent areas
> - Keeping ADC input traces far from PWM output traces — a trace carrying a 5V PWM signal at 10kHz can couple noise into an adjacent trace through parasitic capacitance between the traces
>
> Repair relevance: when you rework an output driver area of an ECU, be aware that the nearby analog circuitry can be affected. Solder bridges, lifted traces, or even an added blob of solder can create new coupling paths between a noisy circuit and a sensitive circuit."

#### Slide 27: Ground Plane Integrity — The Most Critical EMC Factor in Repair
**Visual:** PCB diagram showing ground plane with a gap created by a repair trace or removed component, with current flow arrows showing the longer return path and resulting current loop
**Instructor Script:**
> "The most important EMC statement in this entire session: the ground plane must remain continuous.
>
> The ground plane is a solid copper sheet. Its effectiveness as a low-impedance return path depends entirely on its continuity. When a section of the ground plane is interrupted — by a damaged area, a drilled hole, or a removed trace — current must flow around the gap.
>
> A current flowing around a gap in the ground plane forms a loop. A loop carrying high-frequency current is an antenna. An antenna in the middle of your PCB radiates EMI — both out of the ECU (emissions problem) and into adjacent sensitive circuits (immunity problem).
>
> Repair situations where this occurs:
> - A technician drills through the board to repair a broken trace and unknowingly cuts a ground plane segment
> - Corrosion removes a section of ground plane copper and the technician repairs only the visible surface trace, not the underlying ground plane
> - A rework repair wire is routed across a ground plane segment, creating a gap in the plane beneath the wire path
>
> The rule: when repairing PCB tracks, always assess whether the repair path intersects the ground plane. If a ground plane section is damaged, restore it with copper foil tape, conductive epoxy, or a solderable copper patch. Verify ground plane continuity with a multimeter from multiple points on the board after any extensive rework."

---

### CLOSING: Concept Check and Session Wrap (Slides 28–30, ~5 minutes)

#### Slide 28: Concept Check — Six Questions
**Instructor Script:**
> "Six questions. Answer mentally; I will call on volunteers."

**Question 1:** What is the functional difference between a bulk capacitor and a bypass capacitor?
*(Expected: Bulk = energy storage for cranking ride-through, large electrolytic at power input. Bypass = high-frequency noise suppression, small ceramic at IC VCC pin)*

**Question 2:** An ECU resets only during engine cranking on cold mornings, and works normally once the engine is running. First suspect component?
*(Expected: Bulk electrolytic capacitor — dried out, reduced capacitance, cannot bridge the cold-start cranking dip)*

**Question 3:** A ferrite bead in circuit reads OL on a multimeter in resistance mode. What does this mean and what is the symptom?
*(Expected: Ferrite bead is open circuit. No supply voltage reaches the IC it feeds — that IC is completely dead)*

**Question 4:** A CAN bus produces bit errors specifically when the engine is under high load (alternator working hard). Which component on the CAN lines should be checked?
*(Expected: Common-mode choke on the CAN bus lines at the ECU connector)*

**Question 5:** A sensor input always reads near 0V with the engine running and the sensor connected and verified healthy. The sensor reads correctly at the connector pin measured at the harness. What does this suggest about the ECU input circuit?
*(Expected: The RC filter bypass capacitor has shorted, pulling the input to ground through the series resistor)*

**Question 6:** Name the three components in a pi-filter on a power supply trace, in order from input to output.
*(Expected: Input capacitor to ground, ferrite bead in series, output bypass capacitor to ground)*

#### Slide 29: Failure Mode Summary — Quick Reference Table
**Visual:** Reference table for workshop use

| Component | Failure Mode | Symptom | Test Method |
|---|---|---|---|
| TVS diode | Shorted (post-load dump) | ECU completely dead | Diode test: forward reading in both directions |
| TVS diode | Open | ECU works until next load dump | Diode test: OL in both directions |
| Bulk capacitor | Dried out (low capacitance) | Reset during cranking — cold only | LCR meter: compare to rated value |
| Bypass capacitor | Cracked/shorted | IC dead or unstable | Resistance to ground at IC VCC: near zero |
| Ferrite bead | Open | IC dead, no supply voltage | DC resistance OL |
| Ferrite bead | Shorted | Works but EMI noise passes through | AC impedance measurement at 10MHz |
| Common-mode choke | Open winding | CAN/LIN bus offline | Winding continuity: OL where should be ~0Ω |
| RC filter cap | Shorted | Sensor reads 0V always | Resistance to ground at input pin: near zero |
| RC filter cap | Open | Sensor reading erratic, noisy | Oscilloscope: noise on signal line |

**Instructor Script:**
> "Keep this table. It is your quick-reference diagnostic guide for every power and noise-related ECU fault. Tomorrow in the lab, every activity traces back to one of these rows."

#### Slide 30: Session Summary and Day 5 Hands-On Preview
**Visual:** Summary list — six component categories, one line each
**Instructor Script:**
> "Summary of today's session:
>
> - **TVS diodes and Zener clamps:** Clamp load dump and ESD transients. Test with diode function. A shorted TVS kills the supply; a missing TVS means the next event destroys the MCU.
> - **Bulk capacitors:** Ride-through energy for cranking dips. Fail by drying out. Test with LCR meter. Replace like-for-like on capacitance.
> - **Bypass capacitors:** Local high-frequency bypassing at IC VCC pins. Must be within 2–3mm of the IC. Fail by cracking. A missing bypass cap causes bench-OK, vehicle-fail instability.
> - **Ferrite beads:** Series RF chokes on supply traces. Near-zero DC, high AC impedance. Open = IC dead. Shorted = noise passes through.
> - **Common-mode chokes:** Block common-mode noise on CAN/LIN without affecting differential data. Open winding = bus offline.
> - **RC filters:** Low-pass filter on sensor inputs. Shorted cap = sensor reads 0V. Open cap = erratic sensor noise on oscilloscope.
>
> Tomorrow in the lab: you will identify each of these on a real ECU, trace the power path from connector to MCU supply pin, and use the oscilloscope to see noise before and after a filter. Be ready."

---

## Instructor Notes

### Preparation Required
- **Physical component samples to pass around during lecture:** one failed (bulged or measured low-capacitance) electrolytic capacitor and one healthy one; one surface-mount TVS diode (SMA package); one common-mode choke; one ferrite bead. Handling real components during discussion makes the session significantly more memorable.
- **Whiteboard worked example:** Prepare the bulk capacitor energy calculation (slide 11) on the board before the session. Work through it step by step; do not rush the mathematics. Many technicians in this course will not have used C = Q/ΔV before. The numbers are less important than the concept: the capacitor must supply current during a defined time window.
- **Live oscilloscope demonstration:** If an oscilloscope and a bench power supply with a variable output are available, demonstrating the cranking voltage dip (slowly reduce supply from 12V to 7V while monitoring load current) makes slide 10 far more impactful than a static image.

### Common Teaching Difficulties

**Bulk capacitor energy equation (Slide 11):** Work slowly. Acknowledge that the specific numbers matter less than the concept. The practical rule — replace with at least the original capacitance value — is what students need to walk away with. The equation supports understanding of why capacitance value matters.

**Differential vs common-mode noise (Slide 18):** This is the most conceptually challenging section. A physical analogy that works well: "Both CAN wires run through the harness together. The harness is like an antenna sitting in a field of electromagnetic noise. Both wires pick up the same noise because they are in the same place. That is common-mode. CAN's differential receiver subtracts the two wires — the common noise cancels. The data survives. That is the entire point of differential signaling — and the common-mode choke extends that same principle to larger common-mode disturbances."

**Ferrite bead vs inductor distinction (Slide 15):** Students with basic electronics background may expect ferrite beads to behave like inductors and create back-EMF. Emphasise: at high frequencies, the ferrite material is magnetically lossy — energy is dissipated as heat, not stored and returned. You want the noise energy to disappear, not to bounce back. This is a material property difference, not a circuit topology difference.

### Timing Adjustment
- If running behind, slides 25–27 (PCB layout rules) can be condensed to a 3-minute verbal summary with the key rules stated clearly: adjacent placement, direct ground vias, separate noisy from quiet, never cut the ground plane. The detail can be covered in student notes.
- The concept check (slide 28) should not be skipped — it directly feeds tomorrow's lab readiness.

### Assessment Alignment
All SOs for this session (so-3-2-1 through so-3-4-3) are assessed in the Module 3 written assessment. Tomorrow's lab (05H) provides practical application of so-3-2-2, so-3-2-3, so-3-3-3, and so-3-4-1. The failure mode summary table (slide 29) can be used as the student reference sheet for the lab.

---

## PPT Slide Summary

| Slide | Title | Time |
|-------|-------|------|
| 1 | Title — The Hostile Electrical Environment | 2 min |
| 2 | Five Threat Categories | 3 min |
| 3 | The Learning Framework for This Session | 3 min |
| 4 | The Load Dump Event — ISO 7637 | 4 min |
| 5 | TVS Diodes — How They Work | 5 min |
| 6 | TVS Failure Modes and Testing | 3 min |
| 7 | Zener Clamps on Signal Lines | 3 min |
| 8 | The Complete Power Entry Protection Stage | 3 min |
| 9 | Two Capacitors, Two Completely Different Jobs | 2 min |
| 10 | The Cranking Voltage Dip | 4 min |
| 11 | How Bulk Capacitors Work — Energy Equation | 5 min |
| 12 | Bulk Capacitor Failure — The Dried-Out Electrolytic | 4 min |
| 13 | Bypass Capacitors — The High-Frequency Problem | 5 min |
| 14 | Bypass Capacitor Values, Layout, and Failure | 4 min |
| 15 | What is a Ferrite Bead and How Does it Work? | 4 min |
| 16 | Where Ferrite Beads Are Placed and Why | 3 min |
| 17 | Ferrite Bead Failure Modes and Testing | 3 min |
| 18 | Differential-Mode vs Common-Mode Noise | 4 min |
| 19 | Common-Mode Chokes on CAN and LIN Lines | 4 min |
| 20 | RC Filters on Analog Sensor Input Lines | 4 min |
| 21 | RC Filter Failure Modes — Three Signatures | 3 min |
| 22 | Building Better Filters — Single Capacitor to Pi-Filter | 4 min |
| 23 | Pi-Filter — Name, Failure, and Consequences | 2 min |
| 24 | PCB Layout Rule 1 — Bypass Capacitor Placement | 2 min |
| 25 | PCB Layout Rule 2 — Ground Via Connections | 2 min |
| 26 | PCB Layout Rule 3 — Separate Noisy from Quiet | 2 min |
| 27 | Ground Plane Integrity — Critical for EMC | 3 min |
| 28 | Concept Check — Six Questions | 5 min |
| 29 | Failure Mode Summary Table | 2 min |
| 30 | Session Summary and Lab Preview | 2 min |
| **Total** | | **~90 min** |
