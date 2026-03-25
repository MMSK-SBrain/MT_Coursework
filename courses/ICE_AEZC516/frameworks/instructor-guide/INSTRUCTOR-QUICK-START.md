# Instructor Quick Start Guide
## AE ZG516: Advances in IC Engines

**Purpose:** Get you teaching in minimum time with maximum effectiveness
**Time to read:** 15 minutes
**Time to prepare first session:** 2-3 hours

---

## 🚦 START HERE

### What You Have
A complete, pedagogically-designed learning framework for a 15-session M.Tech IC Engines course including:
- ✅ 45 MCQs with answers and explanations
- ✅ 6 major situated learning problems (workplace projects)
- ✅ Complete lesson plans and session templates
- ✅ Learning outcomes hierarchy (63 session outcomes)
- ✅ Excel template for CDS platform import

### What You Need to Do
1. **Customize** examples to your industry context
2. **Develop** slide decks using session templates
3. **Deliver** using the instructional framework provided
4. **Assess** using MCQs and situated learning problems
5. **Iterate** based on student performance

---

## 📋 PRE-SEMESTER CHECKLIST (2-3 Weeks Before)

### Week 1: Familiarization
- [ ] **Read**: `frameworks/README.md` (this provides complete overview)
- [ ] **Skim**: `design/05-pragmatic-session-coverage.md` (detailed session content - 4,192 lines!)
- [ ] **Study**: `lesson-plans/00-lesson-plan-framework.md` (instructional design approach)
- [ ] **Review**: `lesson-plans/01-session-templates-all-15.md` (quick reference for all sessions)

### Week 2: Content Preparation
- [ ] **Customize examples**: Adapt to your industry (automotive, trucking, power gen, off-highway, marine)
- [ ] **Develop slides**: Create presentation decks for at least first 4 sessions (Modules 1-2)
  - Use session templates as outline
  - Refer to detailed coverage document for content
  - Include diagrams, videos, worked examples
- [ ] **Gather multimedia**:
  - Videos: Combustion high-speed photography, turbocharger operation, injection spray
  - Diagrams: P-V diagrams, torque curves, BSFC maps, compressor maps
  - Animations: Valve timing, 4-stroke cycle, swirl/tumble flows
- [ ] **Prepare MCQs**: Load into delivery system (polling app or build into slides)
- [ ] **Source physical props** (optional but impactful):
  - Piston, connecting rod
  - Turbocharger (cutaway if possible)
  - Fuel injector
  - Catalyst sample
  - Sensors (MAF, O2, knock sensor)

### Week 3: Course Setup
- [ ] **LMS Setup** (Canvas, Moodle, Blackboard, etc.):
  - Upload syllabus
  - Create 6 assignment dropboxes for Situated Learning Problems:
    - Module 1 SLP: Design Your Workplace Engine (due before Session 3)
    - Module 2 SLP: Performance Optimization (due before Session 5)
    - Module 3 SLP: Air/Fuel System Optimization (due before Session 8)
    - Module 4 SLP: Combustion Optimization (due before Session 11)
    - Module 5 SLP: Emissions Compliance (due before Session 14)
    - Module 6 SLP: Future Powertrain Assessment (due end of course)
  - Post SLP descriptions (from `assessments/02-situated-learning-problems.md`)
  - Upload supplementary resources (optional readings, videos, datasheets)
- [ ] **Technology check**:
  - Classroom projector, HDMI/adapters
  - Internet for videos
  - Polling system account (Socrative, Poll Everywhere, Kahoot) OR prepare MCQ slides
  - Backup: Have slides on USB drive in case cloud/internet fails
- [ ] **Prepare handouts**:
  - Session 1-2: Module 1 SLP description and rubric
  - Formula sheet (key equations students will use)
  - Glossary (optional, for students with less engine background)

---

## 🎯 FIRST SESSION: SESSION 1 (Module 1 - Foundation)

### Critical First Impression Goals:
1. **Excite students** about IC engines (they're not boring or obsolete!)
2. **Set expectations** for active, applied learning
3. **Establish credibility** (you know your stuff)
4. **Build community** (we're learning together)

### 90-Minute Session 1 Breakdown:

**[0-5 min] Hook - "Build Your Engine" Gamification**
- Show 3 contrasting engine images side-by-side:
  - Formula 1 V6 turbo (1.6L, 1000+ hp)
  - Heavy-duty diesel truck engine (15L, 600 hp, 2000 lb-ft torque)
  - Portable generator engine (Single-cylinder, 5 hp)
- Ask class: "What makes these SO different?"
- Announce: "By end of today, you'll be able to design an engine for YOUR application."
- **Key message:** You're not just learning theory - you're learning to make real engineering decisions

**[5-10 min] Objectives & Logistics**
- State session outcomes clearly (on slide):
  - SO-1-1-1: Analyze engine architecture choices
  - SO-1-1-2: Calculate BMEP and thermal efficiency
  - SO-1-1-3: Apply thermodynamic principles
  - SO-1-1-4: Identify engine components
- Session roadmap (show timeline slide):
  - Architecture & Configuration
  - Torque, Power, Performance Metrics
  - Thermodynamic Cycles (light treatment)
  - Engine Components
  - Design Exercise
- Course logistics (1 min):
  - 15 sessions, 6 modules
  - Assessment: MCQs (formative) + 6 SLPs (summative)
  - First assignment: Module 1 SLP due before Session 3

**[10-30 min] Part 1: Engine Architecture & Configuration**
- **Slides to prepare**:
  1. Cylinder arrangements: Inline-4, V6, V8, Flat-6, V10 (images + pros/cons table)
  2. Bore/stroke diagram with oversquare, square, undersquare labeled
  3. Displacement calculation formula with worked example
  4. Compression ratio diagram showing clearance volume
  5. CR ranges: SI (10-13:1), CI (15-20:1) with explanation
- **Teaching technique**: Stop frequently and ask "Why?" questions:
  - "Why V8 for trucks but inline-4 for economy cars?" → Packaging, cost, smoothness trade-off
  - "Why can diesels use higher compression ratio?" → No knock limit (compression ignition)
- **Worked example** (do on board or slide):
  - Calculate displacement for 86mm bore, 86mm stroke, 4 cylinders
  - Show formula, plug in numbers, get ~2.0L
  - Point out: This is a "square" engine (bore = stroke) - balanced design
- **MCQ #1** [at 30-32 min]:
  - Display Q1-1-3: Displacement calculation question
  - Give students 60 sec to calculate
  - Poll or show of hands
  - Reveal answer: B (2.0 liters)
  - Briefly explain calculation (they just practiced it)

**[32-57 min] Part 2: Torque, Power, Performance Metrics**
- **Key slides**:
  1. Torque vs Power definitions + formula: P (kW) = T (N·m) × RPM / 9549
  2. Side-by-side torque curves: Diesel truck (flat at low RPM) vs Gasoline sports car (rising with RPM)
  3. BMEP formula and typical values table
  4. Efficiencies: Thermal (brake power / fuel energy), Mechanical (brake / indicated)
  5. BSFC definition and typical values
- **Interactive moment**: Ask students about their workplace engines
  - "How many work with trucks?" → Talk about torque importance
  - "How many with generators?" → Talk about steady-state efficiency
- **Worked example**: BMEP calculation
  - Given: 150 kW at 3000 RPM, 2.0L displacement
  - Calculate: BMEP = (150 × 120) / (2.0 × 3000 × 2) = 15 bar
  - Interpret: "15 bar is excellent for turbocharged SI. If we got 50 bar, something's wrong."
- **MCQs #2 and #3** [at 57-59 min]:
  - Q1-1-1: Torque characteristic for delivery truck
  - Discuss briefly

**[59-79 min] Part 3: Thermodynamic Cycles (Contextual - Not Heavy)**
- **Critical teaching note**: Students often hate thermodynamics. Keep it LIGHT and APPLIED.
- **Slides**:
  1. Otto cycle P-V diagram with labels (1-2-3-4 process)
  2. Efficiency formula: η = 1 - (1/CR^(γ-1))
  3. Demonstration: η at CR=10 vs CR=12 (~46% vs ~52%)
  4. Diesel cycle P-V diagram side-by-side with Otto
  5. Real vs Ideal: Why engines don't achieve theoretical efficiency (heat loss, friction, etc.)
- **Teaching strategy**: Make thermodynamics USEFUL
  - "This formula tells you: Higher CR = better efficiency. That's why modern engines push CR as high as knock allows."
  - "Real engines get 30-40% efficiency, not the 60% theory predicts. Where does the energy go? Coolant (30%), exhaust (30%), friction (5-10%)."
- **MCQ #3** [at 79-81 min]:
  - Q1-1-2: CR effect on efficiency
  - Reinforce: Higher CR → higher efficiency (up to knock limit)

**[81-86 min] Part 4: Engine Components Overview**
- **Slides**:
  - Engine cutaway diagram (color-coded: block, head, crankshaft, piston, valvetrain)
  - Piston cross-section showing rings
  - Valvetrain comparison: OHV vs SOHC vs DOHC
  - Combustion chamber shapes: SI (pent-roof) vs CI (bowl-in-piston)
- **Physical props**: If you have piston, crankshaft, pass around while talking
- **Teaching note**: This is overview only. Details come in later sessions.

**[86-91 min] Interactive Design Exercise**
- **Scenario on slide**: "Design engine for 10-ton delivery truck operating in city"
- **Given**: Need 500 N·m torque at 1500 RPM, limited space under hood
- **Students decide** (Think-Pair-Share for 3 min):
  - SI or CI engine?
  - How many cylinders?
  - Turbocharged or naturally aspirated?
  - Roughly what displacement?
- **Call on 2-3 students** to share answers
- **Class discussion**: Debate choices
- **Instructor synthesis**: "Good answers might include 4-cylinder turbodiesel, ~3-4L, because: torque at low RPM (diesel advantage), compact (4-cyl), turbo boosts power density. SI possible but would need larger displacement or less torque."

**[91-93 min] Wrap-up & Preview**
- **Key takeaways slide**:
  1. Engine architecture choices → performance characteristics
  2. Torque, power, BMEP are the performance language
  3. CR drives efficiency but has limits (knock for SI, mechanical for CI)
  4. Real engines deviate from ideal cycles due to practical losses
- **Preview Session 2**: "We've designed the engine. Next: How does it breathe? 4-stroke cycle, VE, VVT, control systems."
- **Assignment reminder**: "Module 1 SLP assigned today - due before Session 3 (2 weeks). You'll design an engine for YOUR workplace or target industry. Details on LMS."
- **Invite questions**: "Any quick questions before we close?"

---

## 📝 AFTER SESSION 1: REFLECTION & ITERATION

### Immediate (Within 24 hours):
- [ ] **Review MCQ performance**: Did most students get them right? If <70% correct on any question, concept needs more emphasis next time.
- [ ] **Read minute papers** (if you collected them): Common questions? Misconceptions?
- [ ] **Note what worked**: Which examples resonated? Where did students engage most?
- [ ] **Note what to improve**: Did you run over time? Need more visuals somewhere? Confusing explanation?

### Before Session 2 (1 week):
- [ ] **Adjust Session 2 based on feedback**: If students struggled with calculations, add more worked examples to Session 2.
- [ ] **Prepare Session 2 slides** (follow Session 2 template):
  - 4-stroke cycle deep dive
  - Volumetric efficiency (definition, factors, VE curve)
  - Variable valve timing
  - Engine control systems (ECU, sensors, actuators, closed-loop control)
- [ ] **Remind students**: Module 1 SLP due before Session 3 (post reminder on LMS/email)

---

## 🎯 ONGOING SESSION DELIVERY

### Standard Session Flow (Sessions 2-15)

**Before Each Session:**
1. Review session template (in `lesson-plans/01-session-templates-all-15.md`)
2. Refer to detailed coverage (in `design/05-pragmatic-session-coverage.md`) for content depth
3. Prepare/update slides
4. Load MCQs
5. Test videos and tech

**During Session** (follow Gagné's 9 Events):
1. **Hook** (5 min): Grab attention with scenario, failure case, or provocative question
2. **Objectives & Recall** (3-5 min): State outcomes, connect to prior session
3. **Content Delivery** (50-60 min): 4-5 parts, ~12-15 min each
   - Mix lecture with examples
   - Use visuals and videos
   - Embed MCQ after each major part (2-3 MCQs total per session)
   - Discuss answers - especially WHY wrong answers are wrong
4. **Interactive Exercise** (5-10 min): Students actively apply concepts
5. **Wrap-up** (3-5 min): Summarize takeaways, preview next session, remind about assignments

**After Session:**
1. Review MCQ performance
2. Read feedback (minute papers)
3. Note adjustments for next time
4. Prepare next session

**SLP Grading**:
- Module 1 SLP due before Session 3 → Grade using rubric in SLP document
- Select 2-3 best to present in Session 3 (5 min total)
- Repeat for each module

---

## 🔑 SUCCESS TIPS

### 1. Start Strong
- Session 1 sets the tone. Make it engaging, well-paced, and professional.
- Show passion for IC engines - enthusiasm is contagious!

### 2. Use Real Examples
- Always connect to real engines, real data, real industry problems
- Students are working professionals - they value relevance

### 3. Embrace "I Don't Know"
- If a student asks something beyond scope or your expertise: "Great question. Let me research that and get back to you."
- Better to admit limits than fake it

### 4. Manage Time Strictly
- 90 minutes goes FAST
- If running over, skip less critical content, not MCQs or exercises
- Students will tune out if you regularly run 20 min over

### 5. Make MCQs Fun, Not Scary
- MCQs are for learning, not grading (or minimal points)
- Celebrate wrong answers: "Great - this wrong answer reveals a common misconception we need to address!"
- Use polling systems to add game element

### 6. Leverage Student Experience
- Many students have years of industry experience
- Ask them to share insights: "Anyone worked with turbochargers? What challenges have you seen?"
- This enriches learning for everyone

### 7. Provide Formative Feedback Early
- Grade first SLP (Module 1) quickly and thoroughly
- Detailed feedback helps students improve for later SLPs
- If students do poorly on Module 1 SLP, adjust rubric or provide more scaffolding

### 8. Iterate Continuously
- No course is perfect first time
- Use student feedback to improve week by week, semester by semester
- The materials provided are a strong foundation - make them your own

---

## 🆘 TROUBLESHOOTING

### "I'm running out of time every session!"
**Solutions:**
- Trim less critical content (use detailed coverage doc to identify must-have vs nice-to-have)
- Move some content to flipped classroom (pre-session videos)
- Reduce MCQ discussion time (but keep MCQs!)
- Shorten exercises or assign as homework
- Check: Are you lecturing too much without interaction? Students zone out - add more active moments

### "Students aren't engaging with MCQs"
**Solutions:**
- Use polling system (Socrative, Kahoot) for real-time results - more engaging than show of hands
- Award participation points (even if answer is wrong)
- Make MCQs immediately after learning concept (not all at end of session)
- Discuss answers thoroughly - make it a learning moment
- Ask students to explain their reasoning before revealing answer

### "SLP submissions are poor quality"
**Solutions:**
- Provide more scaffolding: Templates, worked examples, sample reports
- Clarify expectations: Show example of good report (use previous semester's best, with permission)
- Office hours: Encourage students to discuss their approach before submitting
- Formative check-in: Require outline or draft for feedback before final submission
- Adjust rubric: If everyone struggles with one criterion, either your expectations are unclear or you haven't taught it well

### "Students have wildly different backgrounds"
**Solutions:**
- Differentiate:
  - For experienced: Challenge questions, leadership in group work
  - For novices: Provide glossary, extra resources, office hour support
- Leverage diversity: Pair experienced with novices for exercises
- Set baseline: Provide pre-session reading/video for those who need catch-up
- Accept range: Not everyone will achieve same depth - that's okay

### "I don't have videos/props/equipment"
**Solutions:**
- **Videos**: Plenty of free resources on YouTube
  - Search: "IC engine combustion slow motion", "turbocharger cutaway", "fuel injection spray"
  - Channels: Engineering Explained, Warped Perception, Driving 4 Answers
- **Diagrams**: Google Images, Bosch Automotive Handbook, textbook figures
- **Simulations**: Some free online tools (basic engine simulators)
- **Props**: Not essential - good diagrams/videos are almost as effective
- **Focus**: Content and pedagogy matter more than fancy tech

---

## 📚 RECOMMENDED PREPARATION SEQUENCE

**Total Prep Time: ~40-50 hours for full semester (frontloaded)**

### Phase 1: Understanding (4-6 hours)
- Read README and framework docs
- Review learning outcomes and session templates
- Skim session coverage for depth of content

### Phase 2: Customization (10-15 hours)
- Identify your industry context
- Find industry-specific examples, data, case studies
- Customize SLP scenarios to match student backgrounds

### Phase 3: Content Development (20-25 hours)
- Develop slides for all 15 sessions (1.5-2 hours per session average)
- Gather/create diagrams, videos, animations
- Prepare MCQs for delivery (load into system or build into slides)
- Create exercise worksheets (if needed)

### Phase 4: Logistics (4-6 hours)
- Set up LMS (assignments, dropboxes, resources)
- Test classroom technology
- Prepare handouts and supplementary materials
- Review institutional policies (academic integrity, accommodations, etc.)

### Phase 5: Rehearsal (2-3 hours)
- Dry-run Session 1 (practice timing, flow)
- Review first few sessions' slides to feel confident
- Prepare answers to anticipated student questions

**After Phase 5: You're ready to teach!**

---

## ✅ FINAL PRE-CLASS CHECKLIST

**The day before Session 1:**
- [ ] Slides finalized and loaded on laptop
- [ ] Videos tested (play without issues)
- [ ] MCQs ready (poll system or slides)
- [ ] Exercise materials printed/prepared (if physical)
- [ ] Module 1 SLP handout ready to distribute or post on LMS
- [ ] Classroom visit (check tech, seating, board/screen setup)
- [ ] Attendance sheet or roster printout
- [ ] Backup plan: USB drive with slides, offline MCQ option
- [ ] Personal: Dress professionally, arrive 15 min early, bring water/coffee
- [ ] Mindset: You've got this! The materials are solid, you know the content, students are eager to learn.

---

## 🎓 FINAL WORDS

**You have everything you need:**
- Comprehensive content coverage (4,192 lines of detailed session coverage!)
- Proven instructional design (Gagné's framework + active learning)
- Complete assessment system (MCQs + SLPs with rubrics)
- Clear learning outcomes (63 session outcomes traceable to 5 course objectives)

**Teaching this course will be rewarding:**
- IC engines are fascinating - complex systems with rich physics, chemistry, and engineering trade-offs
- Students are motivated professionals who will apply this knowledge immediately in their careers
- The course design promotes deep learning, not superficial memorization

**Trust the process:**
- Follow the session templates
- Use MCQs to check understanding and adjust in real-time
- Leverage SLPs for authentic application
- Collect feedback and iterate

**And most importantly: Enjoy teaching!**
IC engines are evolving, not dying. You're training the engineers who will design the next generation of sustainable, efficient powertrains. That's meaningful work.

---

**Questions? Review these resources:**
- **Content Questions**: Refer to `design/05-pragmatic-session-coverage.md`
- **Pedagogy Questions**: Refer to `lesson-plans/00-lesson-plan-framework.md`
- **Assessment Questions**: Refer to `assessments/` folder (MCQ bank and SLP descriptions)
- **Quick Reference**: This document + `lesson-plans/01-session-templates-all-15.md`

**Now go teach Session 1. You've got this!** 🚀
