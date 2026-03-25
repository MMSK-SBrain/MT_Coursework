# Session 1: Complete Instructor & Student Package
## RAG Bootcamp for Automotive Technical Documentation

**Course:** Tatamotors AI - RAG System Development
**Session:** 1 of 4
**Topic:** Foundation - Simple RAG with Single PDF
**Duration:** 170 minutes (2 hours 50 minutes)

---

## 📦 Package Contents

This comprehensive package contains everything needed to deliver Session 1 successfully:

### For Instructors:
1. **Learning Outcomes** - Detailed objectives and competencies
2. **Instructor Manual** - Complete session plan with timing and teaching notes
3. **Troubleshooting Guide** - Solutions to common issues
4. **Assessment Materials** - Quizzes, rubrics, and evaluation criteria
5. **Visual Diagrams Guide** - Teaching aids and diagrams

### For Students:
1. **Student Notebook** - Complete Colab-ready Python notebook with code
2. **OpenRouter Setup Guide** - Step-by-step API configuration
3. **Exercises & Challenges** - Hands-on practice materials
4. **Sample Data** - DTC codes CSV for examples

### Supporting Materials:
- Visual diagrams for presentations
- Sample automotive data
- Pre-session checklist
- Post-session feedback forms

---

## 📋 Files in This Package

```
session_1/
├── 00_SESSION_1_OVERVIEW_README.md          ← You are here!
├── 01_LEARNING_OUTCOMES.md                   ← Start here for planning
├── 02_INSTRUCTOR_MANUAL.md                   ← Your teaching guide
├── 03_STUDENT_NOTEBOOK.py                    ← Main student material
├── 04_OPENROUTER_SETUP_GUIDE.md              ← Send to students before class
├── 05_TROUBLESHOOTING_GUIDE.md               ← Keep open during session
├── 06_EXERCISES_AND_CHALLENGES.md            ← Homework assignments
├── 07_ASSESSMENT_RUBRIC_AND_QUIZ.md          ← Evaluation materials
├── 08_VISUAL_DIAGRAMS_GUIDE.md               ← Create slides from this
└── sample_data_dtc_codes.csv                 ← Example automotive data
```

---

## 🚀 Quick Start Guide for Instructors

### 1 Week Before Session

**Setup:**
- [ ] Read through 01_LEARNING_OUTCOMES.md
- [ ] Review 02_INSTRUCTOR_MANUAL.md completely
- [ ] Test 03_STUDENT_NOTEBOOK.py end-to-end
- [ ] Create slides using 08_VISUAL_DIAGRAMS_GUIDE.md

**Student Preparation:**
- [ ] Email students: 04_OPENROUTER_SETUP_GUIDE.md
- [ ] Share pre-session checklist
- [ ] Ask students to create OpenRouter accounts
- [ ] Provide access to TSI Engine PDF (or alternative)

### 1 Day Before Session

**Final Checks:**
- [ ] Test OpenRouter API with your key
- [ ] Verify Google Colab notebook works
- [ ] Download backup PDF
- [ ] Prepare emergency backup API key
- [ ] Review 05_TROUBLESHOOTING_GUIDE.md

### Day of Session

**Pre-Session (30 min before):**
- [ ] Open 02_INSTRUCTOR_MANUAL.md (your script)
- [ ] Open 05_TROUBLESHOOTING_GUIDE.md (for quick reference)
- [ ] Load slides
- [ ] Test screen sharing
- [ ] Have backup materials ready

**During Session:**
- Follow 02_INSTRUCTOR_MANUAL.md module by module
- Use checkpoints to verify student progress
- Reference troubleshooting guide as needed
- Keep track of time using the timing guide

**Post-Session:**
- [ ] Share 06_EXERCISES_AND_CHALLENGES.md (homework)
- [ ] Distribute 07_ASSESSMENT_RUBRIC_AND_QUIZ.md (if using)
- [ ] Collect feedback
- [ ] Note improvements for next time

---

## 📚 Detailed File Descriptions

### 01_LEARNING_OUTCOMES.md
**Purpose:** Define what students will learn and be able to do

**Contains:**
- Course Level Outcomes (CLO)
- 5 Module Level Outcomes (MLO) with sub-outcomes
- Success criteria
- Time allocation
- Prerequisites
- Materials list

**Use When:**
- Planning the session
- Creating slides
- Explaining session goals to students
- Evaluating session effectiveness

---

### 02_INSTRUCTOR_MANUAL.md
**Purpose:** Your complete teaching guide

**Contains:**
- Module-by-module teaching scripts (word-for-word if needed)
- Timing for each section (20-40 min per module)
- Teaching strategies and tips
- Student engagement techniques
- Checkpoint questions
- Common issues and solutions
- Pacing strategies

**Use When:**
- Delivering the session (keep it open!)
- First time teaching this material
- Need exact timing guidance
- Want scripted explanations

**Key Sections:**
- Module 0: Welcome & Setup (20 min)
- Module 1: Document Processing (30 min)
- Module 2: Embeddings & Vector Store (40 min)
- Module 3: LLM Integration (30 min)
- Module 4: UI Development (30 min)
- Module 5: Wrap-up (10 min)

---

### 03_STUDENT_NOTEBOOK.py
**Purpose:** The main coding material students will work through

**Contains:**
- 15 code cells with complete implementations
- Detailed explanations between each cell
- In-code comments
- Exercises embedded
- Progressive complexity

**Format:** Python file with cell separators (convert to .ipynb if needed)

**How to Use:**
1. **For Google Colab:**
   - Convert to .ipynb or copy-paste into Colab
   - Share link with students
   - Students make their own copies

2. **For Local Jupyter:**
   - Convert to .ipynb: `jupytext --to notebook 03_STUDENT_NOTEBOOK.py`
   - Distribute to students
   - Students run in their environments

**Key Features:**
- Self-contained (all code included)
- Extensively commented
- Includes exercises
- Error handling examples
- Cost tracking

---

### 04_OPENROUTER_SETUP_GUIDE.md
**Purpose:** Help students configure OpenRouter API before session

**Contains:**
- Step-by-step account creation
- Adding credits ($5 minimum)
- Generating API key
- Security best practices
- Testing the API
- Troubleshooting

**When to Share:**
- Send 1 week before session
- Include in pre-session email
- Post in course portal/LMS

**Why Important:**
Students who complete this before class:
- Save 10-15 minutes during session
- Avoid payment delays
- Can start coding immediately
- Less likely to encounter API issues

---

### 05_TROUBLESHOOTING_GUIDE.md
**Purpose:** Quick solutions to common problems

**Contains:**
- 8 categories of issues
- Error messages with solutions
- Quick diagnostic checklist
- Emergency fallback procedures

**Categories:**
1. Environment & Installation
2. File & PDF Loading
3. API & Authentication
4. Embeddings & Vector Database
5. LLM & Response
6. Gradio & UI
7. Performance
8. Google Colab Specific

**How to Use:**
- Keep open during session in separate window
- Ctrl+F to search for error messages
- Share relevant sections with students
- Add your own solutions as you encounter them

**Pro Tip:** Print the quick diagnostic checklist!

---

### 06_EXERCISES_AND_CHALLENGES.md
**Purpose:** Hands-on practice and homework

**Contains:**
- 10 structured exercises (beginner to advanced)
- 5 challenge projects
- Homework assignments
- Submission guidelines
- Grading rubric

**Exercise Types:**
- **[IN-CLASS]**: Complete during session (10-15 min each)
- **[HOMEWORK]**: Required homework (20-30 min each)
- **[CHALLENGE]**: Optional advanced projects

**Required Homework:**
- Exercise 2: Chunking parameters
- Exercise 4: Vector search optimization
- Exercise 7: 15-question test suite

**When to Distribute:**
- Mention in-class exercises during session
- Share full document at end of session
- Set deadline before Session 2

---

### 07_ASSESSMENT_RUBRIC_AND_QUIZ.md
**Purpose:** Evaluate student learning

**Contains:**
- Formative assessments (during session checkpoints)
- Summative assessment (end of session)
- Knowledge check quiz (80 points)
  - Multiple choice (20 pts)
  - True/False (10 pts)
  - Short answer (30 pts)
  - Code analysis (20 pts)
- Practical skills assessment (hands-on coding)
- Homework evaluation rubric
- Self-assessment checklist

**When to Use:**
- **Checkpoints:** Throughout session for formative assessment
- **Quiz:** End of session or as homework
- **Practical:** During session or as capstone
- **Self-assessment:** Share with students for reflection

**Grading:**
- A: 90-100% (Excellent)
- B: 80-89% (Good)
- C: 70-79% (Satisfactory)
- D: 60-69% (Needs Improvement)
- F: <60% (Incomplete)

---

### 08_VISUAL_DIAGRAMS_GUIDE.md
**Purpose:** Create effective visual teaching aids

**Contains:**
- 8 ASCII art diagrams with descriptions
- RAG system overview
- Document chunking visualization
- Embeddings concept
- Similarity search process
- Complete pipeline
- Cost breakdown
- Chunk size comparison
- Gradio interface architecture

**How to Use:**
1. **Create Slides:**
   - Use diagrams as templates
   - Recreate in PowerPoint/Google Slides
   - Follow color scheme suggestions
   - Add animations as suggested

2. **Whiteboard Teaching:**
   - Draw simplified versions on whiteboard
   - Walk through step-by-step
   - Have students draw their own

3. **Handouts:**
   - Print diagrams for students
   - Use during explanations
   - Reference during troubleshooting

**Recommended Tools:**
- PowerPoint/Google Slides (manual recreation)
- Draw.io (free diagramming)
- Mermaid.js (code-based)
- Excalidraw (hand-drawn style)

---

### sample_data_dtc_codes.csv
**Purpose:** Example automotive data for demonstrations

**Contains:**
- 55 common OBD-II diagnostic trouble codes
- Descriptions, systems, severity levels
- Common causes and recommended fixes
- Typical repair costs
- Technical notes

**When to Use:**
- Demo data for examples
- Session 3: Multi-document RAG
- Practice CSV loading
- Real-world automotive context

**How to Use:**
```python
import pandas as pd
dtc_df = pd.read_csv('sample_data_dtc_codes.csv')
print(dtc_df.head())
```

---

## ⏱️ Session Timeline

```
0:00  - 0:20  │ Module 0: Welcome & Setup
0:20  - 0:50  │ Module 1: Document Processing
0:50  - 1:30  │ Module 2: Embeddings & Vector Store
1:30  - 1:40  │ ☕ BREAK
1:40  - 2:10  │ Module 3: LLM Integration
2:10  - 2:40  │ Module 4: UI Development
2:40  - 2:50  │ Module 5: Wrap-up & Next Steps
```

---

## 🎯 Learning Objectives Summary

By the end of Session 1, students will:

✅ **Understand** RAG architecture and purpose
✅ **Load and process** PDF documents into chunks
✅ **Create embeddings** using Sentence Transformers
✅ **Build** a ChromaDB vector database
✅ **Integrate** OpenRouter LLM API
✅ **Develop** a Gradio web interface
✅ **Deploy** a working RAG chatbot

**Success Criteria:**
- 90%+ students have working code
- 80%+ can answer questions correctly
- 75%+ complete homework on time

---

## 💡 Teaching Tips

### For First-Time Instructors

**Do:**
- ✅ Follow the instructor manual closely
- ✅ Use the checkpoints to verify progress
- ✅ Keep troubleshooting guide handy
- ✅ Celebrate small wins with students
- ✅ Share real-world examples
- ✅ Be enthusiastic!

**Don't:**
- ❌ Skip the setup verification
- ❌ Move on if >20% students are stuck
- ❌ Assume students understand - ask questions
- ❌ Go too fast through embeddings concept
- ❌ Forget to test your own code first

### For Experienced Instructors

**Customize:**
- Adjust pacing based on your students
- Add your own examples and stories
- Skip sections students already know
- Add advanced topics if time permits

**Enhance:**
- Live coding instead of pre-written cells
- Additional exercises for fast learners
- Pair programming for struggling students
- Real-time debugging demonstrations

---

## 📊 Success Metrics

### Immediate (End of Session)
- [ ] 90%+ students have working RAG system
- [ ] All students can explain RAG workflow
- [ ] Average quiz score >75%
- [ ] Students can launch Gradio interface

### Short-Term (Before Session 2)
- [ ] 80%+ complete homework
- [ ] Students can answer follow-up questions
- [ ] Few/no remedial sessions needed

### Long-Term (End of Bootcamp)
- [ ] Students build production RAG systems
- [ ] Can troubleshoot independently
- [ ] Apply RAG to their own use cases

---

## 🔧 Customization Guide

### For Different Industries

**Healthcare:**
- Replace TSI manual with medical textbook
- Use medical terminology examples
- Focus on HIPAA compliance in security section

**Legal:**
- Use legal documents
- Emphasize citation accuracy
- Discuss confidentiality

**Customer Support:**
- Use product manuals
- Focus on query understanding
- Add sentiment analysis component

### For Different Skill Levels

**Beginners (No Python):**
- Add 30-min Python basics intro
- Slower pace on coding sections
- More scaffolding in exercises
- Pair programming encouraged

**Advanced (ML Background):**
- Skip embeddings basics
- Add technical deep-dives
- More challenging exercises
- Discussion of advanced topics (hybrid search, reranking)

### For Different Time Constraints

**2-Hour Version:**
- Skip UI development (Module 4)
- Reduce exercise time
- Use pre-built vector database

**4-Hour Version:**
- Add deployment section
- More hands-on exercises
- Advanced topics (conversation memory preview)
- Group projects

---

## 📝 Pre-Session Checklist for Instructors

### Technical Setup
- [ ] Tested entire notebook end-to-end
- [ ] OpenRouter API key working
- [ ] PDF document accessible
- [ ] Backup materials prepared
- [ ] Screen sharing tested
- [ ] Internet connection verified

### Materials Ready
- [ ] Slides prepared from diagrams guide
- [ ] Instructor manual printed/open
- [ ] Troubleshooting guide accessible
- [ ] Homework assignments ready to share
- [ ] Assessment materials prepared

### Student Communication
- [ ] Pre-session email sent (1 week before)
- [ ] OpenRouter setup guide shared
- [ ] Prerequisites communicated
- [ ] Session link/location confirmed
- [ ] Materials access verified

### Contingency Plans
- [ ] Backup API key available
- [ ] Alternative PDF ready
- [ ] Offline notebook prepared
- [ ] Technical support contact ready

---

## 📧 Sample Pre-Session Email

```
Subject: RAG Bootcamp Session 1 - Pre-Session Preparation

Hi [Student Name],

Excited to see you at Session 1 of the RAG Bootcamp this [DATE/TIME]!

To ensure a smooth session, please complete these steps BEFORE class:

1. ✅ Create OpenRouter Account
   → Follow this guide: [Link to 04_OPENROUTER_SETUP_GUIDE.md]
   → Add minimum $5 credits
   → Generate and save your API key

2. ✅ Download TSI Engine Manual
   → [Provide link or attachment]
   → Save to your computer

3. ✅ Optional: Review Python basics
   → [Link to tutorial if needed]

What to Expect:
- Duration: 2 hours 50 minutes (with 10-min break)
- Format: Hands-on coding workshop
- Outcome: Working RAG chatbot for automotive manuals!

Materials:
- Google Colab notebook (will share link in class)
- All code provided - just follow along

Questions? Reply to this email or ask in [discussion forum/chat].

See you soon!
[Your Name]
```

---

## 🔄 Post-Session Checklist

### Immediate (Right After)
- [ ] Share homework: 06_EXERCISES_AND_CHALLENGES.md
- [ ] Share quiz if using: 07_ASSESSMENT_RUBRIC_AND_QUIZ.md
- [ ] Send recording link (if recorded)
- [ ] Collect feedback survey responses

### Within 24 Hours
- [ ] Review student questions/issues
- [ ] Update materials based on feedback
- [ ] Identify students needing help
- [ ] Prepare Session 2 adjustments

### Before Session 2
- [ ] Grade homework/quizzes
- [ ] Provide individual feedback
- [ ] Offer remedial sessions if needed
- [ ] Update instructor manual with improvements

---

## 🆘 Getting Help

### For Instructors

**Technical Issues:**
- LangChain Docs: https://python.langchain.com/
- OpenRouter Support: https://openrouter.ai/docs
- ChromaDB Docs: https://docs.trychroma.com/

**Teaching Questions:**
- Refer to instructor manual
- Check troubleshooting guide
- Contact course coordinator

### For Students

**During Session:**
- Raise hand / ask in chat
- Check with neighbor (pair programming)
- Reference troubleshooting guide

**After Session:**
- Email instructor
- Post in discussion forum
- Study group collaboration

---

## 📈 Continuous Improvement

### After Each Session

**Collect:**
- Student feedback surveys
- Quiz/assessment results
- Notes on what worked/didn't work
- Time spent on each module

**Analyze:**
- Which concepts were hardest?
- Where did students get stuck?
- What questions were most common?
- Did timing work?

**Update:**
- Clarify confusing explanations
- Add examples where needed
- Adjust timing if necessary
- Improve exercises

**Share:**
- Updates with other instructors
- Improvements with course team
- Best practices in teaching notes

---

## 🎓 Instructor Notes Section

*Use this space to document your own observations, modifications, and improvements:*

**What worked well:**
-
-
-

**What to change:**
-
-
-

**Student feedback highlights:**
-
-
-

**Time adjustments needed:**
-
-
-

**Technical issues encountered:**
-
-
-

---

## 📌 Quick Reference

### Key Numbers
- **Session Duration:** 170 minutes
- **Number of Modules:** 6 (0-5)
- **Number of Checkpoints:** 6
- **Exercises:** 10 structured + 5 challenges
- **Quiz Points:** 80
- **Homework Assignments:** 3 required
- **Student Success Rate Target:** 90%+

### Key Files
- **Teaching Script:** 02_INSTRUCTOR_MANUAL.md
- **Student Code:** 03_STUDENT_NOTEBOOK.py
- **Quick Help:** 05_TROUBLESHOOTING_GUIDE.md
- **Homework:** 06_EXERCISES_AND_CHALLENGES.md

### Key Concepts
- RAG = Retrieval Augmented Generation
- 4 steps: Prepare → Embed → Store → Retrieve+Generate
- FREE: Embeddings, vector DB
- PAID: Only LLM API calls (~$0.0001/query)
- Sweet spot: chunk_size=1000, k=3

---

## ✨ Final Notes

This package represents a complete, production-ready Session 1 curriculum. Everything you need is included:

- ✅ Clear learning outcomes
- ✅ Detailed teaching guide
- ✅ Complete student materials
- ✅ Assessment tools
- ✅ Visual aids
- ✅ Troubleshooting support

**Your job as instructor:**
1. Review the materials
2. Customize to your context
3. Prepare your environment
4. Deliver with enthusiasm!

**Student outcomes:**
- Working RAG system
- Deep understanding of architecture
- Hands-on coding experience
- Ready for Session 2

Good luck! You're going to deliver an amazing session! 🚀

---

**Questions or Suggestions?**
This is a living document - feel free to:
- Add your own notes
- Customize for your needs
- Share improvements with other instructors
- Provide feedback for v2.0

**Version:** 1.0
**Last Updated:** [Date]
**Created By:** Tatamotors AI Course Development Team

---

**Happy Teaching! 🎉**
