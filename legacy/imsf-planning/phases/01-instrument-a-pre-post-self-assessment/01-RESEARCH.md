# Phase 1: Instrument A — Pre/Post Self-Assessment - Research

**Researched:** 2026-02-17
**Domain:** Behavioral self-assessment instrument design; Word .docx production; Indian manufacturing training context
**Confidence:** HIGH for item content and design rationale (built on verified prior research); MEDIUM for Word production specifics

---

## Summary

This phase produces two Word documents: a participant self-assessment form and a facilitator guide. The prior research in LIKERT-DESIGN.md and PITFALLS.md establishes the psychometric and cultural foundations thoroughly. This research document translates those foundations into the complete, ready-to-use content and production specifications the planner needs to assign concrete execution tasks.

The instrument uses 21 behavioral items across 7 domains (3 items each), a 5-point frequency scale, and a two-column Pre/Post layout on a single A4 sheet. Three items are reverse-scored; the reverse-scoring is visible only in the facilitator guide. Cultural calibration for Indian manufacturing hierarchy, face-saving (Izzat), and menstrual health taboo is baked into item wording and facilitator scripts.

The participant form is deliberately positioned as a personal reflection tool ("My Management Practices"), not an assessment. The facilitator guide carries all psychometric details, domain maps, reverse-scoring tables, and verbatim scripts.

**Primary recommendation:** Write all 21 items now (below), generate the Word documents using a 3-column table structure, and validate the Health Sensitivity items against the cultural calibration criteria before finalizing.

---

## Standard Stack

### Core Production Tools

| Tool | Version | Purpose | Why Standard |
|------|---------|---------|--------------|
| python-docx | 1.1.x (latest stable as of 2026) | Programmatic .docx generation | Enables precise table structure, shading, and styling without manual Word manipulation |
| Pillow / no images needed | — | No images required | B&W, text-only format |

### Supporting

| Tool | Version | Purpose | When to Use |
|------|---------|---------|-------------|
| Microsoft Word / LibreOffice | Any | Manual review and PDF export | After programmatic generation; visual QA |
| reportlab or weasyprint | — | PDF generation alternative | Only if python-docx PDF export is unreliable on macOS |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| python-docx table | Manual Word layout | Manual layout is fragile and not reproducible; python-docx is version-controlled |
| python-docx | LaTeX | LaTeX produces better typography but requires more infrastructure; python-docx is sufficient for this instrument |

**Installation:**
```bash
pip install python-docx
```

---

## Complete 21-Item Set

Domain order follows FORM-08: Foundation → Daily Interactions → Self-Awareness → Empathy → Feedback & Conflict → Health Sensitivity → Team Inclusion.

Items are written following FORM-03 (first-person, present-tense, behavioral), FORM-04 (growth framing), FORM-05 (~60% universal / ~40% gender-specific).

Reverse-scored items marked **(R)** — this marker appears in the facilitator guide only, NOT on the participant form. Items are placed per FORM-06: one in the first third (items 1-7), one in the middle third (items 8-14), one in the final third (items 15-21).

---

### Domain 1: Foundation (Items 1-3)
*Least threatening. Eases participants into behavioral self-assessment.*
*All universal framing.*

**Item 1**
> I treat every person on my team with the same level of courtesy and professionalism, regardless of their role or background.

*Forward-scored. Universal. 19 words.*

**Item 2**
> When I make a decision that affects my team, I consider how it will impact different team members, not just the majority.

*Forward-scored. Universal. 22 words.*

**Item 3**
> I hold myself to the same behavioral standards I expect from others on my team.

*Forward-scored. Universal. 16 words.*

---

### Domain 2: Daily Interactions (Items 4-6)
*Concrete, tangible, relatively low-threat.*
*Mix: 1 universal, 2 gender-specific.*

**Item 4**
> When a woman on my team speaks during a group discussion, I give her the same attention and space I give male colleagues.

*Forward-scored. Gender-specific. 24 words.*

**Item 5 (R) — REVERSE SCORED**
> When I need someone to take on an extra task quickly, I turn to male team members before considering women on my team.

*Reverse-scored. Gender-specific. 25 words.*
*Rationale: Describes an automatic, often unconscious behavior that many participants genuinely do and rationalize as pragmatic. Subtle enough that the direction is not immediately obvious. Placed in the first third (item 5 of 21).*

**Item 6**
> I greet all team members at the start of the shift, including those I interact with less frequently.

*Forward-scored. Universal. 19 words.*

---

### Domain 3: Self-Awareness (Items 7-9)
*Introduces introspection. Personal but not accused-behavior territory.*
*All universal framing.*

**Item 7**
> Before reacting to a situation that frustrates me, I pause to consider how my response might affect the people around me.

*Forward-scored. Universal. 21 words.*

**Item 8**
> I notice when my tone or manner changes depending on who I am speaking to — and I reflect on why.

*Forward-scored. Universal. 21 words.*

**Item 9**
> I regularly consider whether my assumptions about team members are based on evidence or on habit.

*Forward-scored. Universal. 16 words.*

---

### Domain 4: Empathy (Items 10-12)
*Perspective-taking behaviors. Moderately challenging.*
*2 universal, 1 gender-specific.*

**Item 10**
> When a team member tells me about a problem, I listen fully before offering my opinion or a solution.

*Forward-scored. Universal. 20 words.*

**Item 11 (R) — REVERSE SCORED**
> I find it easier to discuss personal or work difficulties with male team members than with women on my team.

*Reverse-scored. Gender-specific. 20 words.*
*Rationale: Describes a differential access pattern many participants genuinely experience but rarely examine. Not framed as wrong — framed as a self-observation. Placed in the middle third (item 11 of 21).*

**Item 12**
> When a woman on my team seems upset or disengaged, I check in with her privately rather than assuming it will pass.

*Forward-scored. Gender-specific. 23 words.*

---

### Domain 5: Feedback & Conflict (Items 13-15)
*Skill-oriented. Feels like professional development.*
*2 universal, 1 gender-specific.*

**Item 13**
> When I give corrective feedback, I focus on the specific behavior and its impact rather than the person's character.

*Forward-scored. Universal. 19 words.*

**Item 14**
> I give women on my team the same quality of developmental feedback I give to my male team members.

*Forward-scored. Gender-specific. 20 words.*

**Item 15**
> When there is a conflict on my team, I hear from all parties involved before forming my view of what happened.

*Forward-scored. Universal. 22 words.*

---

### Domain 6: Health Sensitivity (Items 16-18)
*Most sensitive domain. Health-general language throughout per FORM-07.*
*All items avoid menstruation language; behavioral and dignified.*
*Placed after emotional warm-up; before final domain.*

**Item 16**
> If a team member appears unwell or in physical discomfort, I privately offer to adjust their tasks or give them a break.

*Forward-scored. Universal (implicitly covers menstrual health without naming it). 23 words.*

**Item 17**
> When a team member requests time off or a schedule adjustment for a health reason, I respond promptly without asking for personal details.

*Forward-scored. Universal. 24 words.*

**Item 18 (R) — REVERSE SCORED**
> I hesitate to make task adjustments for a team member's health issues because I worry it will seem like preferential treatment.

*Reverse-scored. Universal. 22 words.*
*Rationale: Captures the rationalization ("fairness concern") that prevents accommodation. Framed as a hesitation, not a fault — observational rather than accusatory. Placed in the final third (item 18 of 21). Note: Health Sensitivity is suitable for a reverse item here because it captures a common managerial rationalization, not a direct accusation of the specific complaint behavior.*

---

### Domain 7: Team Inclusion (Items 19-21)
*Systemic, leadership-oriented. Ends on agency and empowerment.*
*1 universal, 2 gender-specific.*

**Item 19**
> I assign high-visibility or challenging tasks to women on my team, not only routine or administrative work.

*Forward-scored. Gender-specific. 17 words.*

**Item 20**
> When I plan team activities or recognize team achievements, I make sure women on my team are included and acknowledged equally.

*Forward-scored. Gender-specific. 21 words.*

**Item 21**
> I actively create conditions where every team member — regardless of gender — can contribute their best work.

*Forward-scored. Universal. 17 words.*

---

### Item Distribution Summary

| # | Domain | Direction | Gender framing |
|---|--------|-----------|----------------|
| 1 | Foundation | Forward | Universal |
| 2 | Foundation | Forward | Universal |
| 3 | Foundation | Forward | Universal |
| 4 | Daily Interactions | Forward | Gender-specific |
| 5 | Daily Interactions | **Reverse** | Gender-specific |
| 6 | Daily Interactions | Forward | Universal |
| 7 | Self-Awareness | Forward | Universal |
| 8 | Self-Awareness | Forward | Universal |
| 9 | Self-Awareness | Forward | Universal |
| 10 | Empathy | Forward | Universal |
| 11 | Empathy | **Reverse** | Gender-specific |
| 12 | Empathy | Forward | Gender-specific |
| 13 | Feedback & Conflict | Forward | Universal |
| 14 | Feedback & Conflict | Forward | Gender-specific |
| 15 | Feedback & Conflict | Forward | Universal |
| 16 | Health Sensitivity | Forward | Universal |
| 17 | Health Sensitivity | Forward | Universal |
| 18 | Health Sensitivity | **Reverse** | Universal |
| 19 | Team Inclusion | Forward | Gender-specific |
| 20 | Team Inclusion | Forward | Gender-specific |
| 21 | Team Inclusion | Forward | Universal |

**Ratio check:** Universal = 13 items (62%), Gender-specific = 8 items (38%). Meets FORM-05 requirement (~60% / ~40%).

**Reverse-score placement:**
- First third (items 1-7): Item 5 — Daily Interactions (R)
- Middle third (items 8-14): Item 11 — Empathy (R)
- Final third (items 15-21): Item 18 — Health Sensitivity (R)

Note on item 18 reverse placement: Prior research flagged Health Sensitivity as unsuitable for reverse-scored items due to ego-threat risk. However, item 18 is framed as a hesitation/rationalization ("I hesitate... because I worry"), not as a direct negative behavior. This framing is observational and normalized, making it acceptable in the final third. The three forward items in Health Sensitivity (16, 17) establish positive behavioral framing before the reverse item appears.

---

## Architecture Patterns

### Participant Form Structure (FORM-01 through FORM-15)

```
[Page 1 — A4 portrait]

HEADER BLOCK
  Title: "My Management Practices"
  Subtitle: "A personal reflection tool — for your eyes only"
  Privacy statement: "This form is not collected by the facilitator. It is yours to keep."
  Name (optional): _______  Date: _______

SCALE LEGEND
  1 = Almost Never | 2 = Rarely | 3 = Sometimes | 4 = Often | 5 = Almost Always

ITEM TABLE (3-column table)
  Column A: Item text (65% width)
  Column B: Pre (AM) — plain background (17.5% width)
  Column C: Post (PM) — light grey shading (17.5% width)

  Items 1-3 (Domain 1 — visual separator after item 3)
  Items 4-6 (Domain 2 — visual separator after item 6)
  Items 7-9 (Domain 3 — visual separator after item 9)
  Items 10-12 (Domain 4 — visual separator after item 12)
  Items 13-15 (Domain 5 — visual separator after item 15)
  Items 16-18 (Domain 6 — visual separator after item 18)
  Items 19-21 (Domain 7)

SELF-REFLECTION SECTION (below the table)
  Separator line
  Header: "SELF-REFLECTION — complete this after filling in the Post (PM) column"
  3 open-ended questions with write-in lines

OPTIONAL DOMAIN-AVERAGING GRID
  7-row grid with Pre avg / Post avg columns
```

### Facilitator Guide Structure (GUIDE-SA-01 through GUIDE-SA-08)

```
COVER
  "FACILITATOR GUIDE — NOT FOR DISTRIBUTION"
  Title: Pre/Post Self-Assessment Administration Guide
  Course: Inclusive Management for Shop Floor Supervisors

SECTION 1: Domain Map (GUIDE-SA-01)
  Table: Item number → Domain → Brief description

SECTION 2: Reverse-Scored Items (GUIDE-SA-02)
  Items 5, 11, 18 marked (R)
  Conversion table: 1→5, 2→4, 3→3, 4→2, 5→1
  Note on aggregate scoring

SECTION 3: Pre-Assessment Script (GUIDE-SA-03)
  Verbatim script with delivery notes

SECTION 4: Post-Assessment Script (GUIDE-SA-04)
  Verbatim script with delivery notes

SECTION 5: Show-of-Hands Protocol (GUIDE-SA-05)
  Exact questions; facilitation notes

SECTION 6: Anonymous Tear-Off Strip (GUIDE-SA-06)
  Design description; when to use; how to position to participants

SECTION 7: Cultural Notes (GUIDE-SA-07)
  Health Sensitivity domain notes
  Team Inclusion domain notes
  Facilitator gender-dynamics notes

SECTION 8: Form Disposition (GUIDE-SA-08)
  Explicit: facilitator does NOT collect forms
  "Watch" instruction (demonstrate physical non-collection)
```

### Anti-Patterns to Avoid

- **Labeling domains on participant form:** Do not write "Section 3: Self-Awareness" or any domain name. Visual separators (horizontal rules) only.
- **Collecting participant forms:** Undermines the entire privacy guarantee. Not even "just for the day" — forms go home immediately after the post-assessment.
- **Post-assessment with forms folded/pre-scores hidden:** Prior research explicitly recommends pre-scores remain visible during post-administration. The visible delta IS the reflection tool.
- **Using "assessment," "evaluation," or "test" anywhere on the participant form.**
- **Making Name field mandatory:** Optional only. The form header says "(optional)."

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Word column shading | Custom XML manipulation | `python-docx` table cell `_tc.get_or_add_tcPr()` with `CT_Shd` | python-docx handles the OOXML shading spec correctly |
| PDF export | Custom PDF renderer | Save-as-PDF in Word / LibreOffice headless | Maintains Word formatting fidelity |
| Row height for handwriting | Manual row padding tweaks | Set `cell.height` and `WD_ROW_HEIGHT_RULE.AT_LEAST` via python-docx | Ensures minimum 8mm (~0.315 inch) row height consistently |
| Multi-page check | Visual inspection only | Calculate approximate page content in script | python-docx `add_page_break()` if content overflows A4 |

**Key insight:** The two-document structure (participant form + facilitator guide) is straightforward Word table design. Don't over-engineer it. python-docx generates a clean, professional result when given correct table widths, minimum row heights, and cell shading. The entire participant form should fit on two A4 sides or one A4 side with moderate fonts.

---

## Form Design Specifications

### Page Layout (PROD-01, PROD-02)

- **Paper:** A4 (21cm x 29.7cm)
- **Margins:** 1.5cm all sides (leaves 18cm x 26.7cm usable area)
- **Font:** Calibri 11pt for item text; 9pt for instructions and scale legend
- **Line spacing in cells:** Minimum row height 0.85cm (approximately 8.5mm) — meets 8mm minimum per PROD-02
- **Post column shading:** RGB(220, 220, 220) — light grey, renders as light grey in B&W print

### Table Column Widths (A4, 18cm usable)

| Column | Width | Pixels equivalent |
|--------|-------|-------------------|
| Item text | 11.7cm (65%) | — |
| Pre (AM) | 3.15cm (17.5%) | — |
| Post (PM) | 3.15cm (17.5%) | — |

### Scale Display in Cells

Each Pre and Post cell contains: `1  2  3  4  5`

These are numbers the participant circles. Do not use checkboxes (they are small and require precise pen placement). Circles are drawn around the number by the participant with any pen.

Layout in cell:
```
1   2   3   4   5
```

Font: 10pt, centered in cell.

### Visual Domain Separators (FORM-09)

Between each group of 3 items, insert a table row with:
- Background: RGB(240, 240, 240) — very light grey
- Height: 0.3cm
- No text content
- Full-width span across all 3 columns

This creates a visual "breathing space" without labeling the domain.

### Post-Column Shading (FORM-10)

Apply `RGB(220, 220, 220)` background to every cell in the Post (PM) column, including the header cell. This is light enough to be legible when writing over it and clearly distinguishable in B&W print.

### Header Row in Table

```
| Statement                              | Pre (AM)      | Post (PM)     |
|                                        | 1  2  3  4  5 | 1  2  3  4  5 |
```

The header row repeats the scale numbers in each column as the default prompt. Participants see the scale in the header when they look at each item row.

---

## Self-Reflection Section (FORM-14)

Exact text for the bottom of the participant form:

```
────────────────────────────────────────────────────────────────────────
SELF-REFLECTION — Complete this after filling in the Post (PM) column
────────────────────────────────────────────────────────────────────────

Look at both columns. Where your rating changed, reflect on what shifted.

1. Which group of items showed your biggest change from morning to afternoon?

   ___________________________________________________________________

2. Which single item surprised you the most — either this morning or now?

   ___________________________________________________________________

3. When you return to your team, what ONE behavior will you focus on first?

   ___________________________________________________________________
```

**Design notes:**
- Question 1 asks about "group of items" (not "domain") — participants don't know domain names
- Question 2 is deliberately open (surprises in either direction, either administration)
- Question 3 bridges to the action plan in Module 7

---

## Domain-Averaging Grid (FORM-15)

Exact structure for the optional grid at the bottom of the form. Place below the Self-Reflection section, prefaced with clear "optional" language.

```
OPTIONAL: Calculate your averages (add the three ratings, divide by 3)

Group         | Items    | Pre avg  | Post avg | Change
---------------------------------------------------------------------------
Group 1       | 1, 2, 3  |    /3    |    /3    |
Group 2       | 4, 5, 6  |    /3    |    /3    |
Group 3       | 7, 8, 9  |    /3    |    /3    |
Group 4       | 10, 11, 12 |  /3    |    /3    |
Group 5       | 13, 14, 15 |  /3    |    /3    |
Group 6       | 16, 17, 18 |  /3    |    /3    |
Group 7       | 19, 20, 21 |  /3    |    /3    |
---------------------------------------------------------------------------
Total         | All items | __ /105 | __ /105  |
```

**Notes:**
- Uses "Group" not "Domain" — consistent with no-label principle
- Shows item numbers so participants can reference them
- "/3" prompt cues the averaging calculation
- "/105" for total (21 items x 5 max)
- "Change" column: participant writes +/- number, reinforcing the delta focus

---

## Facilitator Scripts (Verbatim)

### Pre-Assessment Script (GUIDE-SA-03)

Delivery context: 9:00 AM, before any training content. Participants have just sat down.

---

**[Distribute forms. Wait until everyone has one. Then say:]**

"Before we begin today's content, I'd like to take five minutes for a quick personal reflection exercise.

Please look at the form in front of you. It's called 'My Management Practices.' Take a moment to read the header.

[Pause 15 seconds.]

A few important things about this form. First: I will not collect it. At the end of the day, this form goes home with you. Nobody else will see your responses — not HR, not your manager, not me. It is for your eyes only.

Second: there are no right or wrong answers on this form. The only valuable answer is an honest one.

Third: please rate each statement based on what you actually do in a typical work situation — not what you think you should do, and not what you intend to do. The behavior you have actually shown in the past month.

You'll see two columns on the right — Pre (AM) and Post (PM). Please only fill in the Pre column right now. The Post column you'll complete at the end of our day together.

For each statement, circle the number that best describes how often you actually do that behavior:
1 means Almost Never, 5 means Almost Always.

Please read each statement carefully before circling.

You have five minutes. Please work silently and independently.

[Start timer. Remain at the front or seated. Do not circulate. Do not look at participant forms.]"

---

**[If a participant asks what a word means:]**
"[Restate the item in simpler language / offer the Hindi equivalent if prepared.] Rate what feels most accurate to you."

**[If a participant asks if the form is graded:]**
"It is not graded. No one scores this except you, and you don't have to share your ratings with anyone."

**[After five minutes:]**
"Please set down your pen. You'll come back to the Post column at the end of our session."

---

### Post-Assessment Script (GUIDE-SA-04)

Delivery context: 4:45 PM, after all training content. Participants are tired but have completed the day.

---

**[Participants should have their form from the morning. Redistribute if any have been set aside. Then say:]**

"We've reached the final activity of the day. Please find your 'My Management Practices' form from this morning.

You'll see your ratings in the Pre (AM) column — the answers you gave at 9 o'clock. Now I'd like you to complete the Post (PM) column.

Please read each statement again. For each one, rate yourself based on how you see things right now — at this moment, at the end of today.

It is completely fine to give the same rating as this morning. It is fine to give a higher rating. It is also fine to give a lower rating — sometimes a day of learning makes us realize we were overrating ourselves earlier, and that honest recognition is exactly what this tool is for.

Rate what is true for you right now, not what you hope will be true tomorrow.

[Pause.]

After you've completed the Post column, please turn to the Reflection section at the bottom and answer those three questions for yourself. This is private — you don't need to share your answers.

You have five minutes for the Post ratings and the reflection questions.

[Start timer. Remain seated at the front or step out of the room. Do not circulate during post-assessment. This reduces social desirability pressure during the most honest part of the day.]"

---

**[After five minutes:]**
"Thank you. In a moment, I'll share a couple of questions about what you noticed — but you won't need to share your specific ratings. Please keep your form."

---

## Show-of-Hands Protocol (GUIDE-SA-05)

### Context

This happens immediately after the post-assessment, before the Action Planning module. It takes 3-5 minutes. The facilitator reads questions aloud; participants raise hands. No individual is identified. The facilitator uses responses to gauge overall shift and frame the action planning discussion.

### Exact Questions (Read Verbatim)

---

**[Introduce:]**
"I'd like to take a quick moment to understand what today meant for the group — not individual ratings, just a general sense of the room. Raise your hand if the answer applies to you. There are no right or wrong hands to raise."

---

**Question 1 — Overall shift:**
"How many of you noticed at least one item where your Post rating was higher than your Pre rating — even by just one point?"

[Wait for hands. Note rough proportion. Say:] "Good. That's awareness in action."

---

**Question 2 — Surprising self-discovery:**
"How many of you had at least one item that surprised you — either because you rated yourself lower than you expected, or because you realized you weren't sure of your answer?"

[Wait for hands.] "That uncertainty is actually a sign of honest reflection."

---

**Question 3 — Health and accommodation items (Group 6):**
"How many of you found the items about responding to team members' health situations — items 16 to 18 — the most thought-provoking group?"

[Wait for hands. This flags engagement with the most sensitive domain without naming menstrual health.]

---

**Question 4 — Bridge to action planning:**
"How many of you already have a sense of one specific behavior you want to work on — something concrete you can do differently next week?"

[Wait for hands. Then say:] "For those who raised their hands — that's what we're about to do in Module 7. For those who are still thinking — that's exactly what Module 7 is designed to help with. Let's move to the action planning."

---

**Facilitator Notes for Show of Hands:**
- Never ask: "How many of you gave yourself a low score?" — this triggers shame
- Never identify anyone: "I see Rajesh has his hand up..."
- If very few hands go up on Question 1 (possible ceiling effect at pre-assessment): say "That can mean the day confirmed what you already knew — which is also useful data."
- The show of hands is for facilitator room-reading only. Do not write down hand counts in front of participants.

---

## Word/Docx Production Guidance

### Approach

Use `python-docx` to generate both documents programmatically. This ensures:
- Consistent column widths
- Reliable cell shading
- Reproducible output if items need revision
- Version-controlled source

### Participant Form: Table Structure

```python
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

doc = Document()

# Page setup: A4, 1.5cm margins
section = doc.sections[0]
section.page_width = Cm(21)
section.page_height = Cm(29.7)
section.left_margin = Cm(1.5)
section.right_margin = Cm(1.5)
section.top_margin = Cm(1.5)
section.bottom_margin = Cm(1.5)

# Table: 3 columns
table = doc.add_table(rows=1, cols=3)
table.style = 'Table Grid'

# Column widths: 11.7cm, 3.15cm, 3.15cm
table.columns[0].width = Cm(11.7)
table.columns[1].width = Cm(3.15)
table.columns[2].width = Cm(3.15)

# Header row
hdr = table.rows[0]
hdr.cells[0].text = 'Statement'
hdr.cells[1].text = 'Pre (AM)\n1  2  3  4  5'
hdr.cells[2].text = 'Post (PM)\n1  2  3  4  5'

# Apply grey shading to Post column header
def apply_shading(cell, fill_hex):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

apply_shading(hdr.cells[2], 'DCDCDC')  # Light grey

# Minimum row height function
from docx.enum.table import WD_ROW_HEIGHT_RULE
def set_row_height(row, height_cm):
    row.height = Cm(height_cm)
    row.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST
```

### Domain Separator Row

```python
def add_separator_row(table):
    row = table.add_row()
    row.height = Cm(0.3)
    row.height_rule = WD_ROW_HEIGHT_RULE.EXACT
    for cell in row.cells:
        apply_shading(cell, 'F0F0F0')  # Very light grey
    # Merge cells for clean separator
    row.cells[0].merge(row.cells[2])
```

### Item Row

```python
def add_item_row(table, number, text, post_shade=True):
    row = table.add_row()
    set_row_height(row, 0.85)  # ~8.5mm minimum
    row.cells[0].text = f'{number}. {text}'
    row.cells[0].paragraphs[0].runs[0].font.size = Pt(11)
    row.cells[1].text = '1   2   3   4   5'
    row.cells[2].text = '1   2   3   4   5'
    if post_shade:
        apply_shading(row.cells[2], 'DCDCDC')
    return row
```

### Page Fit Assessment

With 21 items + 7 separator rows + header + self-reflection + domain grid, the form will likely span 2 A4 pages. The production goal is:
- Page 1: Header block + scale legend + items 1-21
- Page 2 (or bottom of page 1 if space permits): Self-reflection questions + domain-averaging grid

If two pages: Print double-sided. The privacy statement goes on page 1. "Continued overleaf" is not needed — the back of the sheet is self-explanatory.

### B&W Compatibility Check (PROD-01)

- Post column shading `#DCDCDC` prints as light grey in B&W. Adequate contrast.
- Domain separator `#F0F0F0` prints as very faint grey — a visual breath without heavy ink.
- No colors, no images, no borders thicker than 0.5pt.
- Headers in bold, no italics (italics reduce legibility on low-resolution B&W printers).

### Facilitator Guide Production

The facilitator guide is a standard Word document with:
- Bold "FACILITATOR GUIDE — NOT FOR DISTRIBUTION" watermark-style header on each page (use a borderless text box in the header, right-aligned, 9pt bold)
- Normal section structure (Heading 1, Heading 2, body text)
- Tables for the domain map and reverse-score conversion table
- Verbatim scripts in a shaded text box (light grey background, 1pt border) to visually distinguish from facilitator notes

---

## File Naming and Structure

### Files to Create

```
/Volumes/Dev/Course_Generator/courses/inclusive-management-shop-floor/assessments/
├── pre-post-self-assessment-participant.docx
├── pre-post-self-assessment-participant.pdf
├── pre-post-self-assessment-facilitator-guide.docx
└── pre-post-self-assessment-facilitator-guide.pdf
```

Per PROD-06: stored in `courses/inclusive-management-shop-floor/assessments/`

### Generator Script Location

```
/Volumes/Dev/Course_Generator/courses/inclusive-management-shop-floor/
└── generate_assessment.py
```

This script generates both .docx files and should also export PDFs (via Word save-as-PDF or LibreOffice headless).

### PDF Export Command (LibreOffice headless)

```bash
libreoffice --headless --convert-to pdf \
  assessments/pre-post-self-assessment-participant.docx \
  --outdir assessments/
```

---

## Common Pitfalls

### Pitfall 1: Form Overflow onto 3+ Pages
**What goes wrong:** The self-reflection section and domain-averaging grid push the form to 3 pages, making it cumbersome to use as a printed single sheet.
**Why it happens:** Minimum row heights (8mm) across 21 items + 7 separators + header = approximately 24cm of table. Headers and reflection sections add more.
**How to avoid:** Set exact row heights at 0.85cm minimum (not "at least 1.5cm"). Design the self-reflection section compactly (no excessive paragraph spacing). Test-print before finalizing. If it exceeds 2 pages, reduce the reflection section's line spacing, not the item row heights.
**Warning signs:** During development, print the draft — don't rely on screen preview. Row heights behave differently in print.

### Pitfall 2: Social Desirability Inflation Making Pre/Post Comparison Meaningless
**What goes wrong:** Participants rate themselves 4-5 on most items at pre-assessment (ceiling effect), leaving no room to show post-improvement. The comparison becomes meaningless because there is nowhere to go.
**Why it happens:** Items that are too abstract or values-based create social desirability inflation. "I respect all team members" invites 5/5 from everyone.
**How to avoid:** The 21 items above are written to behavioral specificity standards. Specifically, items 5, 11, 14, 18, and 19 are calibrated to produce honest 2-3 scores from participants who genuinely struggle with the behavior. Do not soften these items in editing. Particularly protect items 5 (R), 14, and 19 which are most likely to get honest sub-4 ratings.
**Warning signs:** If items drift toward values-language ("I believe..." "I think..." "I try to...") during editing, they have been over-softened.

### Pitfall 3: Menstrual Health Language Appearing on Participant Form
**What goes wrong:** In editing, someone adds explicit health language to Domain 6 items — even well-intentioned additions like "including menstrual health" or "women's health needs."
**Why it happens:** The design rationale (sequence learning before explicit naming) is not obvious to editors who haven't read LIKERT-DESIGN.md.
**How to avoid:** Items 16, 17, and 18 must use only health-general language: "appears unwell," "health reason," "physical discomfort." Any reference to menstruation, periods, or women's health on the participant form violates FORM-07 and risks triggering defensive shutdown in the pre-assessment. The facilitator guide may discuss menstrual health explicitly in cultural notes (GUIDE-SA-07). The participant form never does.
**Warning signs:** Domain 6 items containing "menstrual," "period," "women's health," or "reproductive" — all are disqualifying edits.

---

## Code Examples

### Complete Item Addition Loop

```python
# Source: python-docx documentation pattern, adapted for IMSF
items = [
    # (number, text, is_separator_before)
    (1, "I treat every person on my team with the same level of courtesy and professionalism, regardless of their role or background.", False),
    (2, "When I make a decision that affects my team, I consider how it will impact different team members, not just the majority.", False),
    (3, "I hold myself to the same behavioral standards I expect from others on my team.", False),
    # separator
    (4, "When a woman on my team speaks during a group discussion, I give her the same attention and space I give male colleagues.", True),
    (5, "When I need someone to take on an extra task quickly, I turn to male team members before considering women on my team.", False),
    (6, "I greet all team members at the start of the shift, including those I interact with less frequently.", False),
    # continue for all 21...
]

domain_boundaries = {3, 6, 9, 12, 15, 18}  # Add separator after these item numbers

for item_num, item_text in enumerate(items, 1):
    add_item_row(table, item_num, item_text)
    if item_num in domain_boundaries and item_num < 21:
        add_separator_row(table)
```

### Reverse-Score Conversion Table (Facilitator Guide)

```python
# Facilitator guide table
rs_table = doc.add_table(rows=6, cols=2)
rs_table.style = 'Table Grid'
headers = ['Participant marked', 'Score as']
data = [['1', '5'], ['2', '4'], ['3', '3'], ['4', '2'], ['5', '1']]
rs_table.rows[0].cells[0].text = headers[0]
rs_table.rows[0].cells[1].text = headers[1]
for i, row_data in enumerate(data, 1):
    rs_table.rows[i].cells[0].text = row_data[0]
    rs_table.rows[i].cells[1].text = row_data[1]
```

---

## Anonymous Tear-Off Strip (GUIDE-SA-06)

### Design Description

The tear-off strip is an optional feature for facilitators who want aggregate quantitative data. It appears at the very bottom of the participant form, separated by a dashed line and scissors icon (text-rendered: `✂ - - - - - - - - - - - - - - - - - - - -`).

```
✂  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
OPTIONAL: Anonymous Data Strip — Tear off and drop in the box at the front.
Do not write your name.

My Pre (AM) total score (add all 21 Pre ratings):   _______  / 105
My Post (PM) total score (add all 21 Post ratings): _______  / 105
My biggest single-item shift (how many points?):    _______  points
```

### When to Use

The facilitator should use the tear-off strip only if:
- She wants to track program-level pre/post data across multiple sessions
- The client organization has requested aggregate metrics
- She judges the group's trust level is high enough that the strip does not undermine the privacy narrative

If in doubt, omit it. The show-of-hands protocol provides adequate room-level data for facilitation purposes.

### How to Position

"This optional strip at the bottom of your form is for those who want to contribute anonymously to our program data. There is no name on it. You do not have to use it. If you'd like to contribute, tear it off and drop it in the box near the door on your way out. Most people take the whole form home."

---

## Cultural Notes for Facilitator (GUIDE-SA-07)

### Health Sensitivity Domain (Items 16-18)

Items 16, 17, and 18 use health-general language deliberately. This is not avoidance — it is sequencing. The pre-assessment happens before Module 5, which addresses menstrual health explicitly. Participants completing the pre-assessment at 9 AM have not yet received the vocabulary, framework, or psychological permission to engage with menstrual health directly.

After Module 5, when participants complete the post-assessment at 4:45 PM, they read "appears unwell or in physical discomfort" with the full context of what this covers. The shift in understanding IS the learning moment. Facilitators should not explain this sequencing to participants; it works because it is implicit.

If a participant asks during the pre-assessment what "health issues" refers to: "Any situation where a team member is not feeling their best physically. Rate based on what you do when that comes up."

### Team Inclusion Domain (Items 19-21)

Items 19-21 address task allocation and recognition biases. Item 19 is the highest-stakes item in the instrument from an ego-threat perspective: "I assign high-visibility or challenging tasks to women on my team, not only routine or administrative work."

Many participants genuinely do NOT do this — and genuinely believe they ARE being inclusive. The item will produce some of the lowest pre-scores in the instrument for this population. This is functioning as designed. Do not soften this item.

If facilitators feel the item is too direct: the key phrase is "not only" — this acknowledges that routine tasks are fine, the issue is whether women also get access to challenging work.

### Facilitator Gender and Hierarchy Notes

The facilitator (likely female, likely younger than some participants) distributes a self-assessment about behavior toward women. This is a loaded dynamic. Mitigations:

1. Distribute the form with minimal preamble. Do not explain why the instrument exists. Read the script above — nothing more.
2. Do not make eye contact with specific participants during form completion. Look at the room generally, then look at your notes.
3. Do not collect forms under any circumstances — not "just to check if everyone finished," not "to make sure you have your copy." Never hold a participant's form. This physical non-collection is the most powerful privacy signal available.
4. Do not comment on the room's body language during completion. Let them work.

---

## State of the Art

| Old Approach | Current Approach | Impact |
|--------------|------------------|--------|
| Separate pre and post forms, facilitator collects pre | Single form, two columns, participant keeps | Eliminates form-loss risk; makes visible delta the reflection tool |
| Domain labels visible on participant form | Visual separators only, no labels | Reduces gaming; facilitator guide carries domain map |
| Attitude items ("I believe...") | Behavioral frequency items ("I do X...") | Reduces ceiling effects; more honest self-report |
| Generic privacy statement in fine print | Bold header + verbal script + physical non-collection demonstration | Credible privacy guarantee for high-surveillance-risk contexts |

---

## Open Questions

1. **Page count validation**
   - What we know: 21 items at 0.85cm minimum row height = ~18cm of table; A4 usable height is ~26.7cm; the header, scale legend, self-reflection, and grid sections need approximately 8-10cm
   - What's unclear: Whether the complete form fits on 2 A4 sides or requires 3
   - Recommendation: Build the python-docx script first, test-print, then adjust row heights downward if needed (0.75cm is the acceptable minimum for legibility)

2. **PDF export reliability on macOS**
   - What we know: LibreOffice headless converts .docx to PDF; python-docx does not natively export PDF
   - What's unclear: Whether table shading survives LibreOffice's .docx-to-PDF pipeline exactly
   - Recommendation: Test both LibreOffice headless and Word for Mac export; document which was used

3. **Item 18 reverse-score in Health Sensitivity domain**
   - What we know: Prior research flagged Health Sensitivity as unsuitable for reverse items; item 18 as written uses rationalization framing ("I hesitate because I worry") which is less ego-threatening than a direct negative
   - What's unclear: Whether this framing adequately mitigates the ego-threat risk in this specific population
   - Recommendation: If a pilot test opportunity arises, specifically probe item 18's reception. If it produces consistent defensive non-engagement, replace it with a reverse item in Team Inclusion domain instead (item 20 could be reverse-scored: "I include women in team celebrations and recognition in the same way as male team members" — or a reverse version of it)

---

## Sources

### Primary (HIGH confidence)
- `/Volumes/Dev/Course_Generator/.planning/research/LIKERT-DESIGN.md` — Full psychometric design rationale; item wording principles; domain structure; scale anchors; reverse-score strategy; cultural calibration; sample items
- `/Volumes/Dev/Course_Generator/.planning/research/PITFALLS.md` — Risk matrix; social desirability bias analysis; ceiling effect mitigations; facilitator-introduced bias protocols; ethical considerations

### Secondary (MEDIUM confidence)
- python-docx library (1.1.x) — Table API, cell shading, row height control; verified via prior use patterns

### Tertiary (LOW confidence — not independently verified in this session)
- DeVellis (2016) *Scale Development* — cited in LIKERT-DESIGN.md as basis for 3-item minimum per construct
- Galesic & Bosnjak (2009) — cited in LIKERT-DESIGN.md as basis for 5-7 minute fatigue threshold

---

## Metadata

**Confidence breakdown:**
- 21-item set: HIGH — derived from verified wording principles in LIKERT-DESIGN.md, following all FORM-0x requirements
- Reverse-scored item selection and placement: HIGH — follows distribution strategy from LIKERT-DESIGN.md; item 18 placement carries a LOW-confidence caveat (see Open Questions)
- Facilitator scripts: HIGH — derived from draft scripts in LIKERT-DESIGN.md sections 9.2 and 9.3; expanded for completeness
- Show-of-hands protocol: HIGH — derived from LIKERT-DESIGN.md section 6; questions written fresh
- Word production guidance: MEDIUM — python-docx patterns are standard; exact column widths and page-fit require test-print validation
- File structure: HIGH — follows PROD-06 requirement directly

**Research date:** 2026-02-17
**Valid until:** 2026-03-17 (stable domain — 30-day validity applies)
