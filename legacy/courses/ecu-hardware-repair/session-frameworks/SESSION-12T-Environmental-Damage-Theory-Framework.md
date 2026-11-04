# SESSION-12T: Environmental Damage — Moisture, Corrosion & Failure Analysis
## Instructor-Led Story Framework for PPT Preparation

**Course:** ECU Hardware Repair (ECUHR)
**Module:** 5 — ECU On-Table Diagnostics
**Day:** 12 | **Session Type:** Theory
**Duration:** 90 minutes
**Approach:** Instructor-Led Narrative with Photo Evidence and Case Examples
**PPT Target:** 26–30 slides

**Session Outcomes Addressed:**
- so-5-4-1: Identify water ingress entry points on a disassembled ECU housing and explain common moisture damage failure modes | Understand

**CO Alignment:** co-1

---

## INSTRUCTOR-LED STORY ARC

---

### SETUP: Opening Hook (Slides 1–3, ~8 minutes)

**Narrative Voice:** Authoritative and observational. Students have spent two days learning to diagnose ECU faults from electrical signals. Today they encounter the most common real-world cause of ECU failure — environmental damage — that produces those signals in the first place. The tone shifts from circuit analysis to physical forensics. Think detective at a scene.

#### Slide 1: Title Slide
**Visual:** Close-up photograph of a heavily moisture-damaged ECU PCB — green and white corrosion deposits covering connector pins, dendritic growth visible between traces under the photograph, corroded IC leads on a surface-mount package. A stark contrast to the clean boards students have been working with.
**Instructor Script:**
> "This is not an unusual board. This is not an extreme case from a flood-damaged vehicle. This ECU came from a seven-year-old hatchback with a recurring engine fault. The owner had it replaced twice from a dealership — at £650 each time — before a workshop received it for bench diagnosis and found moisture damage at the connector seal.
>
> Moisture and corrosion are the most common cause of ECU failure in real-world repair. They are also the cause least commonly addressed in technical training. Most courses teach you to measure signals and find faulty components. Very few teach you to look at a board and read the story of what happened to it — where water entered, how long it was there, what damage it caused, and whether the board can be saved.
>
> That's what today is about. By the end of this session, you'll be able to open an ECU, examine the PCB, and determine the ingress point, the severity level, and the economic decision: clean and repair, or replace."

#### Slide 2: Why This Matters — Economics and Accountability
**Visual:** Two comparison scenarios:

Scenario A: ECU replaced without moisture assessment. New unit fitted. Failure within 8 months — same moisture entry point, same corrosion process, new ECU destroyed.

Scenario B: Moisture damage assessed. Entry point identified. Board cleaned and sealed. Connector seal replaced on the vehicle side. ECU reused. No recurrence.

Caption: "Replacing an ECU without addressing moisture entry is not a repair. It is a delay."

**Instructor Script:**
> "The economic argument for understanding moisture damage is straightforward. If you fit a replacement ECU without identifying and sealing the moisture entry point, the replacement will fail. You have not fixed the problem. You have bought the customer eight to eighteen months before they return with the same fault, a new ECU, and a very justified complaint.
>
> Identifying the moisture path, assessing the board's condition, cleaning correctly if salvageable, and addressing the water source — that is a complete repair. It is also more profitable: cleaning and reusing a board, or quoting a repair rather than a replacement, is often a better margin for the workshop than swapping the ECU.
>
> Today's session gives you the knowledge to make that assessment professionally."

#### Slide 3: Where Moisture Damage Sits in the Diagnostic Workflow
**Visual:** The Module 5 diagnostic workflow diagram from Day 10. A new branch shown:

```
...Component Test → Fault Confirmed
                  ↓
         Is the fault cause environmental?
         (Corrosion, trace damage, dendritic growth)
                  ↓
         Environmental Assessment
         (Entry point → Severity → Clean vs Replace)
```

**Instructor Script:**
> "Where does environmental damage assessment fit in the diagnostic workflow? After you've confirmed a fault and before you plan the repair. When you find an open-circuit trace, a shorted input, or a failed contact — and the failure pattern is consistent with corrosion rather than component overstress — you stop and ask: is this a moisture damage case?
>
> If yes, the repair plan changes completely. You cannot just replace the component and close the case. You must understand how the board was damaged, whether other damage exists that has not yet failed, and what caused the moisture to reach the PCB in the first place."

---

### TRIGGER: The Moisture Ingress Story (Slides 4–7, ~12 minutes)

#### Slide 4: How Water Gets Into an ECU — Overview
**Visual:** Exploded diagram of a typical ECU housing showing:
- The PCB inside
- The upper housing lid
- The lower housing base
- The connector assembly passing through the housing wall
- Four numbered arrows pointing to typical ingress points

**Instructor Script:**
> "An ECU housing is designed to exclude moisture — but that protection is not absolute, and it degrades with age. Let me show you the four common entry points. Understanding these lets you identify the source of moisture damage from its pattern on the PCB — where the corrosion is concentrated tells you where the water entered."

#### Slide 5: Ingress Point 1 — Connector Seals
**Visual:** Two photographs side by side.
Left: New connector assembly — individual wire seals in excellent condition, connector face seal intact, no gaps.
Right: Aged connector assembly — individual wire seals cracked and shrunken, gaps around wire entries visible, face seal compressed and degraded.
**Instructor Script:**
> "Individual wire seals are the small rubber grommets pressed around each wire as it enters the connector shell. They create a seal between the wire and the connector housing. After 8–15 years of thermal cycling, exposure to engine heat and cold, and mechanical vibration, these seals crack and shrink. Water can then travel along the wire's insulation — capillary action — directly into the connector cavity and onto the connector pins.
>
> The connector face seal is the O-ring or gasket that seals the mating face between the vehicle harness connector and the ECU connector. Repeated connect/disconnect cycles compress and distort it. Oil contamination, common in engine bay connectors, further degrades the seal material.
>
> Diagnostic signature: corrosion will be concentrated at the connector pins closest to the failed seal position. You can often identify which individual wire seal has failed by looking at which group of pins shows the heaviest corrosion."

#### Slide 6: Ingress Point 2 — Case Seam and Vent Membrane
**Visual:** Two photographs:
Photo A: ECU housing cross-section showing the housing joint sealed with silicone. Arrow pointing to a section of failed seal with a gap.
Photo B: Gore-Tex vent membrane on the underside of an ECU housing. Annotation: "Equalises internal pressure during thermal cycling."
**Instructor Script:**
> "The case seam — the joint between the upper and lower housing halves — is sealed with silicone bead or a press-fit rubber gasket during assembly. Both methods lose effectiveness with age and thermal cycling. When the seal fails, moisture can enter through the case perimeter. Diagnostic signature: corrosion distributed across the PCB surface, not concentrated at connector pins. Often appears as a general 'fog' of oxidation on exposed traces.
>
> Vent membranes are found on some ECUs — particularly those in harsh environments or large housings with significant internal air volume. The membrane (typically Gore-Tex or similar) allows air to flow freely to equalise pressure as the ECU heats and cools. This prevents differential pressure from forcing moisture through seals during the cool-down cycle.
>
> If the vent membrane is blocked — by mud, engine oil, or mechanical damage — the ECU cannot breathe. When it cools rapidly, the pressure differential can pull moisture through even a healthy connector seal. Inspect the vent membrane location on damaged ECUs — a blocked or absent membrane is often a contributing factor."

#### Slide 7: Ingress Point 3 — Capillary Action Through Wiring
**Visual:** Illustration showing water droplet on a wire in the engine bay. Arrow following the wire path into the connector shell. Annotation: "Capillary action — surface tension draws moisture along wire strands regardless of cable orientation."
**Instructor Script:**
> "Capillary action is often overlooked. Water does not need to flow downhill to enter a connector. Surface tension draws moisture along the microscopic spaces between wire strands in a cable — upward, sideways, in any direction — as long as there is a continuous narrow gap.
>
> This means a connector that appears sealed at the face can still receive moisture from wires that enter it from below or from the side, if the individual wire seals have degraded. The moisture travels up the wire interior over days or weeks, accumulates at the connector cavity, and begins corroding pins.
>
> This is why individual wire seals matter — not just the face seal. Even if the connector face is perfectly sealed, a failed individual wire seal allows the capillary pathway to remain open."

---

### RISING ACTION — Part 1: Moisture Damage Failure Mechanisms (Slides 8–16, ~28 minutes)

#### Slide 8: Section Header — MOISTURE DAMAGE FAILURE MECHANISMS
**Visual:** Section divider. Background: macro photograph of PCB trace corrosion — copper trace visible, with green-black oxide layer visible at the surface.
**Instructor Script:**
> "Once moisture reaches the PCB, several distinct failure mechanisms operate — sometimes simultaneously. Understanding each one helps you identify what you're looking at on a damaged board, predict what hasn't failed yet but may soon, and decide whether cleaning will be effective."

#### Slide 9: Mechanism 1 — Electrolytic Corrosion
**Visual:** Three-panel visual:
Panel A: Clean copper trace cross-section.
Panel B: Same trace with moisture present — galvanic cell illustrated between copper trace and tin-lead solder with ionic current flow in moisture layer.
Panel C: Advanced corrosion — trace cross-section showing reduced copper width, pit corrosion, surface oxide layer.
**Instructor Script:**
> "Electrolytic corrosion is the most fundamental moisture damage mechanism. When water containing dissolved ions — from the atmosphere, from road salt, from the PCB manufacturing flux residue — bridges between two dissimilar metals, it acts as an electrolyte. A galvanic cell forms.
>
> On a PCB, the dissimilar metals are everywhere: copper traces, tin-lead solder, nickel underplating on pads, tin connector pin plating. Each pairing has a different electrode potential. When moisture bridges them, the less noble metal — usually copper — acts as the anode and begins dissolving.
>
> The result: copper traces thin from their edges and surfaces. Over months or years, a trace that should carry 0.5A without issue becomes resistively high, then intermittently open, then permanently open. Corrosion at connector pins increases contact resistance — the same progressive failure pattern.
>
> Accelerating factors: higher voltage across the corroding metals drives faster corrosion rate. Board areas with high potential difference between adjacent conductors — power rails, switching nodes — corrode faster than low-voltage signal areas."

#### Slide 10: Mechanism 2 — Dendritic Growth
**Visual:** Macro photograph of actual dendritic growth on a PCB — fine metallic filaments (dendrites) visible between two adjacent traces, appearing as branching silver-grey whiskers. Annotation indicating the spacing: "0.5mm pitch adjacent traces."
**Instructor Script:**
> "Dendritic growth is a spectacular failure mode — literally metal growing between conductors under electrical potential. In the presence of moisture and a DC electric field, metal ions dissolve from the anode (positive conductor), migrate through the moisture film, and deposit on the cathode (negative conductor). Over time, they form a branching metal filament — a dendrite — that grows from the cathode toward the anode.
>
> When the dendrite bridges the gap between two conductors, a short circuit exists. Current flows through the dendrite, it may partially evaporate if current is high enough — temporarily clearing the fault — then regrow. This produces the maddening intermittent short that clears itself and comes back.
>
> Fine-pitch PCB areas are most vulnerable: 0.5mm or 0.3mm pitch IC pads, fine connector traces, closely-packed SMD resistor/capacitor arrays. These areas have high electric field density and small gaps for the dendrite to bridge.
>
> Under magnification (20x or 40x), dendrites appear as branching metallic filaments, often with a slight iridescent sheen. They are fragile — they can be broken by air pressure — but if moisture returns and voltage is present, they regrow."

#### Slide 11: Mechanism 3 — Oxide Layer on Connector Pins
**Visual:** Two photographs:
Photo A: Clean gold-plated connector pin — bright, reflective.
Photo B: Oxidised tin-plated connector pin — grey-black, matte, with visible oxide film.
Inset: Resistance measurement — clean pin: 0.003Ω. Oxidised pin: 0.5–2Ω.
**Instructor Script:**
> "Connector pin oxidation is one of the most common causes of intermittent ECU faults — and one of the most commonly overlooked in diagnosis. As connector pins oxidise, their surface resistance increases. At low current — as on a sensor signal line — this increased resistance creates a voltage drop across the pin contact that distorts the signal.
>
> The symptom is an intermittent fault that appears when the connector is stationary and disappears when the connector is moved or disconnected and reconnected. Flexing the connector cracks the thin oxide layer, temporarily restoring good contact. This is why customers sometimes report that the fault 'went away after the garage wiggled the connector.'
>
> Gold-plated pins resist oxidation well. Tin-plated pins — the majority of connector pins on automotive ECUs — oxidise progressively. Measurement: in-circuit resistance from ECU pin to sensor pin through the connector should be under 0.1Ω for a good contact. Values above 0.3Ω represent a resistive fault. Values above 1Ω are significantly resistive and will affect signal integrity."

#### Slide 12: Mechanism 4 — Contaminant Bridging
**Visual:** Micro photograph showing a white/grey crystalline residue deposit between two PCB conductors. Annotation: "Evaporated water leaves dissolved salts behind — these deposits are conductive when humid and cause leakage current."
**Instructor Script:**
> "When water evaporates from a PCB, it leaves behind dissolved ionic contaminants: road salt, atmospheric sulphates, flux residue activated by moisture. These deposits form a resistive bridge between adjacent conductors.
>
> Unlike a dendritic short — which is a metallic conductor — a contaminant bridge is a resistive ionic path. It causes leakage current rather than a hard short. The ECU sees this as a pull-up or pull-down on a signal line that should be isolated: the signal sits at the wrong voltage, the sensor appears to read incorrectly, and a DTC sets.
>
> Contaminant bridging is typically reversible with cleaning — if caught early. The contaminant can be dissolved with IPA and removed. However, if the board has been wetted and dried multiple times, the deposits can build up and partially enter component packages, making them harder to remove.
>
> Diagnostic signature: resistive faults — not open circuits, not hard shorts — that change with humidity. A board that shows a fault on a damp day and appears correct on a dry day often has active contaminant bridging."

#### Slide 13: Mechanism 5 — IC Package Infiltration
**Visual:** Cross-section diagram of an IC package showing bond wires from die to package leads. Arrow showing moisture ingress path: moisture enters through the plastic moulding compound → migrates along bond wires → reaches the die.
Caption: "Moisture infiltration of IC package — may cause no immediate failure but promotes die corrosion over 3–18 months."
**Instructor Script:**
> "This is the delayed mechanism — the one that explains why a customer can have an ECU 'repaired' only for it to fail six months later.
>
> Plastic IC packages are not perfectly sealed. At high humidity over extended periods, moisture permeates the moulding compound and migrates along the bond wires to the die. At the die surface, ionic contaminants from the moisture create corrosion at the bond wire connections and at the aluminium conductor tracks on the chip.
>
> This corrosion progresses slowly — months to over a year. The IC appears functional during and immediately after repair: bond wires are intact, die connections are intact. But the corrosion is progressing at the metal-semiconductor interface, invisible to any external measurement. Eventually the bond wire corrodes through or the die conductor cracks — the IC fails.
>
> This is why a Level 3 moisture-damaged board — where IC lead oxidation is visible — carries a risk of IC package infiltration that cannot be assessed from the outside. When quoting a repair on a heavily moisture-damaged board, this latent failure risk must be communicated to the customer."

#### Slide 14: Understanding Conformal Coating
**Visual:** Three photographs:
Photo A: PCB with intact conformal coating — slight gloss, traces appear slightly blurred through the coating.
Photo B: Same PCB under UV light — coating fluoresces blue-white. Damaged area appears dark (no fluorescence).
Photo C: Damaged conformal coating — peeled area exposing bare PCB traces to moisture.
**Instructor Script:**
> "Conformal coating is a protective layer applied over the PCB after assembly. It provides a physical barrier between the PCB components and the environment — moisture, salt, chemical vapour. Intact conformal coating dramatically reduces the rate of all five moisture damage mechanisms.
>
> Three common types: acrylic (most common — clear, reworkable with IPA), polyurethane (more durable, harder to remove), silicone (flexible, high temperature, must be mechanically removed — dissolves in nothing common).
>
> The critical point: conformal coating is only effective where it is intact. If it is damaged — cracked by thermal stress, peeled by mechanical impact, bubbled by moisture that got underneath — the bare PCB is exposed at that location. Moisture attacks the unprotected area.
>
> Inspection method: UV light. Most conformal coating formulations fluoresce blue-white under a 365nm UV lamp. Areas where the coating is intact glow clearly. Areas where it is absent or damaged appear dark. This is your primary inspection tool for conformal coating assessment."

#### Slide 15: Conformal Coating — Removal for Rework
**Visual:** Three-step visual showing conformal coating removal process:
Step 1: UV inspection — identify damaged areas and areas requiring rework access.
Step 2: Acrylic coating: apply IPA with brush, let soak 2–3 minutes, remove with soft brush. Confirm removal under UV.
Step 3: Polyurethane: specialist coating remover or abrasive method (scalpel for localised rework).
**Instructor Script:**
> "For any repair work under conformal coating, the coating must be removed in the repair area first. The removal method depends on the coating type.
>
> Acrylic coatings — by far the most common on automotive ECUs — dissolve readily in isopropyl alcohol at 99% purity. Apply IPA, let it soften the coating for two to three minutes, then remove with a soft brush. Check under UV to confirm the area is fully cleared.
>
> Polyurethane coatings require specialist coating removal solvents — not IPA. Some are removable with aggressive solvents such as MEK (methyl ethyl ketone), but these are aggressive and require good ventilation. Localised removal with a scalpel is an option for small areas.
>
> Silicone coatings cannot be dissolved — they must be mechanically removed with a scalpel or dental pick. This requires care to avoid damaging PCB traces or adjacent component pads.
>
> After repair, coating must be reapplied over the repaired area. Aerosol conformal coating (acrylic) is available for workshop repair application and works adequately for most repairs."

---

### RISING ACTION — Part 2: Corrosion Severity Classification (Slides 16–21, ~20 minutes)

#### Slide 16: Section Header — SEVERITY CLASSIFICATION SYSTEM
**Visual:** Section divider. Background: a 2x2 grid of PCB photographs at four severity levels — from barely visible oxidation on the left to completely destroyed traces on the right.
**Instructor Script:**
> "Assessment of moisture-damaged ECUs requires a consistent classification system. A system that gives every technician and customer the same language for the same observations. Without a consistent scale, one technician calls a board 'repairable' and another calls the same board 'beyond repair' — and neither can justify their decision clearly.
>
> I use a Level 1 to Level 4 system. Each level has specific observable criteria and a defined response. Learn these criteria — you will use them in this afternoon's practical and in every moisture damage case you encounter in professional practice."

#### Slide 17: Level 1 — Minor Corrosion
**Visual:** Photograph of a board with Level 1 damage — slight grey oxidation visible on connector pins only, PCB traces appearing clean, no visible deposits on board surface.

Criteria checklist:
- Oxidation confined to connector pin surfaces only
- No visible PCB trace corrosion
- No deposits between PCB conductors
- Conformal coating intact or minor edge damage
- No component lead corrosion

Response: Cleanable with IPA + soft brush. Connector pins may need light abrasion with erasure or ultrafine abrasive. Check continuity after cleaning.

**Instructor Script:**
> "Level 1 is early-stage moisture exposure. The damage has not yet reached the PCB surface — only the connector pins have been affected. This is the most common classification for boards that have had 'a bit of moisture exposure' but no persistent submersion.
>
> Cleanable: IPA wash with soft-bristle brush, air dry, inspect under magnification. Connector pins that show oxide film may benefit from very light abrasion — a clean pencil eraser or IPA-soaked foam swab applied with gentle pressure will break through the oxide and restore good contact. Test continuity from ECU pin through to harness after cleaning.
>
> Economic prognosis: high confidence of successful repair. Board is salvageable."

#### Slide 18: Level 2 — Moderate Corrosion
**Visual:** Photograph of a board with Level 2 damage — visible green/grey PCB trace corrosion in the connector vicinity, some component lead oxidation, early-stage dendritic growth visible between traces near the connector area.

Criteria checklist:
- PCB trace corrosion visible — green or dark discolouration on trace surfaces
- Some component lead oxidation — particularly on leads closest to the ingress point
- Early dendritic growth — fine filaments visible between conductors under 10x magnification
- Conformal coating damaged in ingress area

Response: Ultrasonic cleaning with IPA or professional flux remover, then manual IPA + soft brush. Manual removal of dendrites with bamboo stick under magnification. Inspect traces for continuity after cleaning — corrosion may have thinned some traces to the point of intermittent conductivity.

**Instructor Script:**
> "Level 2 represents moderate exposure — moisture has been present long enough to attack PCB traces and component leads, and dendritic growth has begun between conductors.
>
> This board requires more thorough cleaning: ultrasonic cleaning if equipment is available (ultrasonic cleaner with IPA or professional PCB cleaner, run at 40–60kHz for 10–15 minutes). Manual cleaning with IPA and soft-bristle brush for detailed areas. Dendrites must be removed mechanically — bamboo stick, nylon brush, or careful use of dry air — under magnification. Bamboo is preferred to metal tools because it cannot cause accidental trace damage or short circuits.
>
> After cleaning: mandatory continuity check on all traces in the affected area. Corroded traces may appear visually clean after washing but have reduced cross-section — measure trace resistance and compare to clean equivalent lengths. Any trace showing increased resistance should be noted on the repair report.
>
> Economic prognosis: moderate confidence. Thorough cleaning usually restores function. Latent weakness in thinned traces may cause later failure — advise customer."

#### Slide 19: Level 3 — Severe Corrosion
**Visual:** Photograph of a board with Level 3 damage — significant trace corrosion with some clear trace loss (gaps visible in trace), multiple corroded component leads, heavy dendritic growth across multiple areas, PCB surface discolouration.

Criteria checklist:
- Trace corrosion with visible open circuits (trace gaps visible)
- Multiple component leads with significant oxidation
- Heavy dendritic growth across multiple PCB areas
- Conformal coating largely absent in damaged areas
- IC package leads showing heavy oxidation

Response: Level 3 boards require trace repair after cleaning. This includes cleaning per Level 2 process, then: continuity test all traces in affected area, repair open-circuit traces with conductive repair ink or thin wire bridges, reapply conformal coating. IC packages with oxidised leads require careful lead cleaning and may need replacement if lead-to-pad resistance is unacceptable. Economic repair boundary — quote must include risk of latent IC package infiltration failure.

**Instructor Script:**
> "Level 3 is the critical decision point. Cleaning is possible and may restore electrical function. But trace corrosion has already caused some open circuits — these require physical repair beyond cleaning alone. And IC packages with heavily oxidised leads carry the latent failure risk I described earlier: moisture may have infiltrated the package, with damage that will manifest in 6–18 months.
>
> At Level 3, the repair decision is economic rather than technical. The cleaning and trace repair work is substantial — typically 2–4 hours of skilled labour. The IC package infiltration risk means the customer must be informed: this board may fail again after repair, not due to inadequate repair but due to latent damage that cannot be reversed. Some customers will accept this with a reduced labour rate. Others will prefer a replacement ECU after weighing the risk.
>
> The correct professional approach: quote the repair transparently. Document the Level 3 classification. Inform the customer of the latent risk. Let them decide with full information."

#### Slide 20: Level 4 — Beyond Economic Repair
**Visual:** Photograph of a board at Level 4 — substantial trace loss across multiple areas, multi-layer PCB delamination visible (white areas between PCB layers), component packages cracked or heavily swelled, MCU package visibly distorted.

Criteria checklist:
- Wholesale trace loss across PCB (not isolated to connector area)
- Multi-layer PCB delamination — layers separating
- MCU or other primary IC with visibly corroded or distorted package
- PCB substrate damage — dark discolouration, swelling, or cracking of the FR4 base material

Response: Not economically repairable. Customer is to be informed that board replacement is the only viable option. Detailed documentation of the assessment and the specific damage observed should be provided.

**Instructor Script:**
> "Level 4 is a clear outcome. This board cannot be repaired. When multi-layer PCB delamination is present, the internal copper planes have separated from the dielectric substrate — inner layer traces are broken, power planes are compromised, and no surface cleaning or trace repair can address this.
>
> When the MCU package is visibly distorted or has extensive lead corrosion, IC package infiltration has likely reached the die. Replacement is required.
>
> The professional obligation at Level 4 is clear and timely communication to the customer. Do not spend two hours attempting cleaning on a Level 4 board. Assess, classify, document, communicate. The customer's time and your time are better spent sourcing and fitting a replacement ECU — with the water ingress point addressed first."

#### Slide 21: Severity Classification — Quick Reference Table
**Visual:** Clean summary table:

| Level | Visible Signs | Location | Action | Economic Prognosis |
|---|---|---|---|---|
| 1 — Minor | Pin oxidation only | Connector pins only | Clean: IPA + brush. Check continuity. | High confidence |
| 2 — Moderate | PCB trace corrosion, early dendrites | Connector area + traces | Ultrasonic/manual clean. Remove dendrites. Test traces. | Moderate confidence |
| 3 — Severe | Open traces, heavy dendrites, IC lead corrosion | Multiple board areas | Clean + trace repair + IC assessment. Inform of latent risk. | Low-moderate; disclose risk |
| 4 — Beyond repair | Delamination, MCU damage, trace loss across board | Whole board | Replace ECU. Address water source first. | Not repairable |

**Instructor Script:**
> "Reference table for the classification system. In this afternoon's practical, you will classify a real moisture-damaged donor board using this system. Be precise — write down the specific observations that led to each classification criterion being met or not met. A correct classification with poor documentation is not useful. A correct classification with specific, observable evidence is a professional deliverable."

---

### RISING ACTION — Part 3: Cleaning Procedure (Slides 22–24, ~12 minutes)

#### Slide 22: Section Header — CLEANING PROCEDURE
**Visual:** Photograph of a clean-bench workspace: IPA bottle (99%), soft-bristle brushes in several sizes, bamboo sticks, magnification loupe, air bulb for drying, cotton swabs, UV light.
**Instructor Script:**
> "Cleaning a moisture-damaged ECU PCB is a skilled operation. It is not pouring IPA on a board and hoping for the best. The correct tools, the correct sequence, and correct inspection after cleaning are all required. Let me walk through the standard procedure."

#### Slide 23: Manual Cleaning Procedure — Step by Step
**Visual:** Step-by-step annotated diagram (or photograph sequence):

Step 1 — Inspect before cleaning: photograph the board in original state under normal light and UV light. Document severity classification. Identify ingress point location.

Step 2 — Conformal coating: identify coating type using UV light. Remove coating in affected areas as required (acrylic: IPA soak. Polyurethane: specialist solvent. Silicone: mechanical).

Step 3 — IPA wash: apply 99% IPA generously to affected areas using a soft brush — soft-bristle artist's brush or PCB cleaning brush. Work in circular motion, loosening deposits. Do not use paper towels — they leave fibres on component leads.

Step 4 — Dendrite removal: under magnification, use a bamboo stick or soft nylon brush to dislodge dendritic growth. Do not use metal tools — scratch risk and short-circuit risk. Air bulb to dislodge loosened material.

Step 5 — Second IPA wash: repeat wash to remove dissolved contaminants stirred up by Step 4.

Step 6 — Rinse and dry: final IPA rinse. Air dry — either controlled airflow (low-pressure compressed air or air bulb) or low-temperature oven (50°C for 20–30 minutes). Do not use high-temperature heat gun — component temperature stress.

Step 7 — Post-cleaning inspection: under magnification and UV light. Confirm dendrites removed. Confirm no residue deposits visible. Confirm coating removed areas are clean.

**Instructor Script:**
> "A few specific points from this procedure that people routinely get wrong. First: 99% IPA, not 70%. 70% isopropyl alcohol contains 30% water. You are trying to remove water and its deposits — adding more water is counterproductive. Always 99% for electronics cleaning.
>
> Second: soft brushes, bamboo tools, cotton. No metal tools near the PCB during cleaning. The board is wet with IPA, components are exposed — a metal tool slipping causes a short-circuit that may damage the MCU or other ICs.
>
> Third: bamboo for dendrite removal. Bamboo is softer than solder and PCB traces — you can press firmly enough to break dendrites without damaging the traces underneath. Metal dental picks can score traces. Plastic picks tend to flex rather than deliver pressure. Bamboo is the right material.
>
> Fourth: complete drying before any power is applied. IPA is flammable — do not apply power until the IPA has fully evaporated. This takes at least 20 minutes in ambient air, or 20–30 minutes at 50°C in a low-temperature oven. Confirm dryness by smell: if you can smell IPA, it hasn't fully evaporated."

#### Slide 24: Post-Cleaning Verification — What to Test
**Visual:** Testing checklist with measurement guidance:

| Test | Method | Pass Criteria |
|---|---|---|
| Trace continuity | Multimeter, continuity mode, point-to-point across cleaned traces | Continuity present — no open circuits where trace should be continuous |
| Connector pin resistance | Multimeter, resistance mode, ECU pin to harness pin through connector | < 0.1Ω per pin contact. > 0.3Ω = suspect |
| Insulation resistance between adjacent traces | Multimeter, resistance mode, between adjacent conductors | > 1MΩ between any two conductors not intended to be connected |
| Conformal coating coverage | UV light inspection | Cleaned/reworked areas covered with new coating. No dark gaps. |
| Visual inspection under magnification | 10–20x loupe or microscope | No residual deposits, no visible dendrites, no damaged trace edges |

**Instructor Script:**
> "Cleaning is not complete without verification. A board that appears clean under normal light may have residual contaminant bridges between fine-pitch pads that are invisible without magnification. Insulation resistance measurement between adjacent traces catches these: any reading below 1MΩ between two conductors that should be isolated indicates a leakage path.
>
> Connector pin resistance is the other critical measurement — this is what the ECU actually uses when processing sensor signals. A cleaned pin that tests at 0.8Ω through the connector will cause the same signal distortion as a corroded one. Light abrasion on the pin contact surface may be needed in addition to chemical cleaning."

---

### CLIMAX: Reading the Story — Forensic Assessment (Slides 25–26, ~8 minutes)

#### Slide 25: The Forensic Assessment Mindset
**Visual:** Split image — left: a detective at a scene examining evidence. Right: a technician examining a corroded PCB under UV light. Caption connecting both: "The pattern of damage tells you the story."
**Instructor Script:**
> "When you receive a moisture-damaged ECU for assessment, you are a forensic investigator before you are a repair technician. The board is telling you a story. The location of the corrosion, its pattern, its severity gradient — lighter near the perimeter, heavier near the connector — tells you where the water entered, how it flowed, how long it was present, and what else may have been damaged even if it hasn't failed yet.
>
> Corrosion concentrated at one corner of the connector and decreasing away from that point: one connector wire seal has failed. The water entered at that seal, ran down the connector pins, and pooled in the connector cavity. Pins closest to the seal show worst damage.
>
> Corrosion distributed across the PCB surface, following the board geometry rather than concentrated at any specific entry point: case seam failure or blocked vent membrane. Water condensed internally and settled across the board.
>
> Corrosion on component leads but not on traces between them: the board was submerged briefly — enough to wet component leads but not to pool on traces. Different from long-term moisture exposure.
>
> This reading ability comes from practice. This afternoon you'll examine two or three real boards and make your assessment. The more boards you examine, the faster and more accurate this pattern recognition becomes."

#### Slide 26: The Customer Communication
**Visual:** Two-column table:

| Situation | What to Tell the Customer |
|---|---|
| Level 1 damage | "Board shows minor connector pin oxidation. Cleaned successfully. Recommend connector seal replacement to prevent recurrence. Board expected to perform normally after repair." |
| Level 2 damage | "Board shows moderate moisture damage to PCB traces. Cleaned and tested. All continuity verified. Recommend addressing the water source and connector seal. No immediate IC concerns but traces in the affected area have been thinned." |
| Level 3 damage | "Board shows severe moisture damage. Cleaned and traces repaired. However, IC packages in the affected area may have moisture infiltration that cannot be confirmed without destructive testing. There is a risk of component failure within 6–18 months that is independent of our repair work. Customer should be aware of this risk before authorising repair. Replacement ECU is the alternative if they require full confidence." |
| Level 4 damage | "Board is beyond economic repair. Multi-layer PCB damage or primary IC corrosion is present that cannot be restored. Replacement ECU is required. Before fitting the replacement, the moisture source must be identified and sealed." |

**Instructor Script:**
> "Customer communication on moisture damage is a professional skill in itself. The customer has a right to know the severity of what was found, the confidence level of the repair, and the risk of future failure that comes from latent damage. Hiding that information to secure the repair job is dishonest and creates a future liability.
>
> The words I've given you here are a starting point. Adapt them to your workshop's communication style. But the content — what was found, what was done, what the risks are — must be present in every customer communication about moisture damage. This is what separates a professional repair shop from one that just replaces parts and hopes."

---

### RESOLUTION: Consolidation (Slides 27–28, ~10 minutes)

#### Slide 27: Summary — Moisture Damage Framework
**Visual:** Three-panel reference card:

Panel 1 — Entry Points:
- Connector wire seals (most common)
- Connector face seal
- Case seam
- Vent membrane failure
- Capillary action through wiring

Panel 2 — Failure Mechanisms:
- Electrolytic corrosion (trace thinning, pin corrosion)
- Dendritic growth (metallic short circuits)
- Oxide layer on connector pins (intermittent contact)
- Contaminant bridging (resistive leakage path)
- IC package infiltration (delayed IC failure)

Panel 3 — Severity Levels:
- L1: Connector pins only — clean and test
- L2: PCB traces + early dendrites — clean thoroughly + verify
- L3: Open traces + IC leads — clean, repair, disclose risk
- L4: Delamination + MCU damage — replace ECU, address water source

**Instructor Script:**
> "Three panels. Entry points, failure mechanisms, severity levels. These are the three frameworks you apply every time you open a moisture-damaged ECU. They convert a seemingly overwhelming problem into a structured assessment."

#### Slide 28: Preview of Day 12 Hands-On — Mid-Module Assessment
**Visual:** Photos of two activities: left — student examining PCB under UV light with magnification; right — student at bench ECU with scan tool and oscilloscope.
**Instructor Script:**
> "This afternoon has two parts. In the first part, you'll receive a real moisture-damaged donor board and apply today's assessment framework: identify the ingress point, classify the severity, conduct the cleaning procedure if appropriate, and verify post-cleaning.
>
> In the second part — and this is important — you work independently on a fault case study. This is the Mid-Module Practical Assessment for Module 5. Each bench has a different ECU with a planted fault. You set up the bench, scan, trace, and identify the fault independently. The instructor observes but does not assist. Your findings go on the assessment form, which is your practical assessment submission.
>
> This afternoon draws on everything from Days 10, 11, and 12. Bench setup, scanning, line tracking, component testing, and now environmental assessment. Any questions about the assessment format before we head to the workshop?"

---

## PPT DESIGN GUIDANCE

### Visual Style:
- This session is photograph-driven more than diagram-driven — real PCB photographs at every corrosion level are essential
- Macro and close-up photography: corrosion damage, dendritic growth, UV fluorescence — these must be real photographs, not illustrations
- Maintain the dark theme from Module 5 sessions
- Classification level slides: consistent format — photograph + criteria checklist + action + prognosis. Do not vary the structure between levels.
- Consider a thin colour border on each level slide that changes with severity: green (L1), amber (L2), orange (L3), red (L4)

### Key Slides to Emphasise:
- Slide 10 (Dendritic growth photograph): this is the most visually striking and most memorable content in the session — let students examine it closely, invite questions
- Slide 17–20 (Classification levels): students must be able to classify boards using these criteria — spend time at each level; post the reference table (Slide 21) at each bench during the lab
- Slide 23 (Cleaning procedure): safety-critical — IPA flammability, tool selection, drying time before power application
- Slide 26 (Customer communication): often overlooked in technical training — spend time here. Students will need this language in professional practice.

### Photography Required:
The following photographs should be captured in advance and included in the PPT:
- Aged connector with failed wire seals (compare to new)
- Vent membrane (intact vs blocked)
- Level 1 damage: clean board with connector pin oxidation only
- Level 2 damage: trace corrosion + early dendrites (macro, with scale reference)
- Level 2 damage: UV light showing damaged conformal coating
- Level 3 damage: open-circuit trace visible + heavy dendritic growth
- Level 4 damage: PCB delamination visible at board edge
- Dendritic growth: close-up macro showing metallic whiskers between traces

Photograph sources: real ECUs from salvage supplier, workshop repair cases, or specialist ECU repair libraries.

---

## INSTRUCTOR NOTES

### Pedagogical Strategy:
This session uses physical evidence and forensic analysis as the primary learning mode:
1. Hook with a cost/outcome case that connects moisture damage to economic consequences
2. Build understanding of ingress points before failure mechanisms — sequence matters for the "story reading" skill
3. Present failure mechanisms as logical chemical/physical processes, not arbitrary damage types
4. Introduce the classification system as a professional tool with economic implications, not just an academic framework

### Common Misconceptions to Address:
- "Cleaning a PCB always works." Not at Level 3–4. Set accurate expectations.
- "If the ECU passed testing after cleaning, it's fixed." Explain IC package infiltration — latent failure risk at Level 3.
- "I can identify moisture damage by looking at it." Many Level 1 boards look clean to the naked eye — UV light and magnification are required for proper assessment.

### Safety Notes for Lab (12H):
- IPA at 99%: flammable — no open flames or sparks in cleaning area. Ensure ventilation. IPA vapour heavier than air — low ventilation = accumulation at floor level.
- Ultrasonic cleaner: confirm IPA-compatible unit if used (some ultrasonic cleaners are fire-rated for water-based solutions only).
- Board drying: ECU must be fully dry before power is applied. Enforce this without exception.

### Timing Flexibility:
- If running short: compress Slide 23 (cleaning procedure) — cover the steps briefly, rely on hands-on for the detail
- If running long: Slide 24 (post-cleaning verification table) can be handed out as a printed reference rather than covered in full on slide
- Core content never to skip: Slides 5–7 (ingress points), Slides 9–13 (failure mechanisms), Slides 17–21 (severity classification)

---

## SESSION SUCCESS CRITERIA

Students leave this session able to:
- Name four common water ingress entry points on an ECU housing and describe the corrosion pattern each produces on the PCB
- Describe five moisture damage failure mechanisms and explain the electrical fault each produces
- Classify a moisture-damaged PCB as Level 1, 2, 3, or 4 using observable criteria
- State the correct cleaning procedure for Level 1 and Level 2 damage, including materials, tools, and post-cleaning verification
- Explain why IPA concentration matters (99% not 70%) and why bamboo tools are used instead of metal
- State the latent IC failure risk associated with Level 3 damage and explain why it must be communicated to the customer
- Describe what dendritic growth looks like under magnification and how it creates intermittent short circuits
- Explain how oxide layer buildup on connector pins causes intermittent faults that disappear on connector flex

**Most importantly:** Students understand that moisture damage assessment is a prerequisite to any repair decision, and that a moisture-damaged board must have its water ingress source addressed before any replacement or repaired ECU is fitted.

---

*Module 5 | Day 12 Theory | ECUHR | v1.0 | 2026-02-18*
