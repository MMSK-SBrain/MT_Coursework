# Quick Start Guide

Get started with Course Generator in 5 minutes!

## Prerequisites

- Claude Code installed
- Basic idea of what course you want to create

## Step-by-Step Guide

### 1. Navigate to Repository

```bash
cd /Volumes/Dev/Course_Generator
```

### 2. Start Claude Code

```bash
claude
```

### 3. Create Your First Course

**Option A: Direct approach**
```
Help me design a course for automotive ECU diagnostics
```

**Option B: Explicit skill invocation**
```
Use the course-design skill to create a vocational training course
```

### 4. Follow the Conversation

The skill will ask you questions like:

1. **Who are your learners?**
   - Example: "Automotive technicians with 2-3 years experience"

2. **What should they be able to DO?**
   - Example: "Diagnose ECU faults, read error codes, perform software updates"

3. **How many days is the course?**
   - Example: "5 days"

4. **What's the theory vs practice balance?**
   - Example: "30% theory, 70% hands-on practice"

### 5. Review Generated Files

Check the `courses/{your-course-name}/` folder:
- `00-requirements.md` - Your inputs saved
- `01-checklist.md` - Progress tracking
- `03-template.xlsx` - Excel with learning outcomes

### 6. Generate Story Frameworks (Optional)

```
Use the storytelling-framework-generator skill to create story frameworks from my Excel template
```

Answer questions about:
- Target audience age and tech proficiency
- Cultural context
- Output format (video/PPT)
- Whether you want teacher-led narratives

### 7. Get Your Story Frameworks

Check the `storytelling-outputs/{COURSE-CODE}-{TIMESTAMP}/` folder:
- `requirements.md` - Story generation settings
- `index.md` - Navigation
- `Module-X-Lesson-Y.md` - Story frameworks for each lesson

## Example Complete Workflow

```
User: Help me design a 5-day course for automotive ECU diagnostics

Claude: I'd love to help! Who will be taking this course? Tell me about their
        background and experience level.

User: Automotive technicians with 2-3 years experience, familiar with basic
      electrical systems

Claude: Great! What should they be able to DO after completing this course?

User: - Diagnose ECU faults using diagnostic tools
      - Read and interpret error codes
      - Perform ECU software updates
      - Reset and reprogram ECUs

Claude: Perfect! Let me create your course structure...

[Course created in courses/ecu-diagnostics/]

User: Now use the storytelling skill to make this engaging

Claude: I'll help generate story frameworks! Let me read your template...
        What's your target audience age group?

User: Adult professionals, 25-45 years old

[Story frameworks generated in storytelling-outputs/ECU-DIAG-2026-01-03-07-40/]
```

## Tips for Success

### Course Design Tips:

1. **Be specific about outcomes**
   - ❌ "Understand ECUs"
   - ✅ "Diagnose common ECU faults using OBD-II scanner"

2. **Think about real job tasks**
   - What will they do on day 1 back at work?
   - What tools/equipment do they need?

3. **Consider safety first**
   - For automotive/manufacturing, safety should be Day 1

4. **Balance theory and practice**
   - Vocational training: aim for 60-70% hands-on

### Storytelling Tips:

1. **Let the skill choose techniques**
   - It uses rotation to avoid repetition
   - You can override if needed

2. **Use Teacher-Led for first lessons**
   - Builds rapport and authority
   - Great for setting context

3. **Provide cultural context**
   - Regional examples make stories relatable
   - Use placeholders if creating generic content

4. **Specify your medium**
   - Video vs PPT affects the framework style

## Troubleshooting

### Skill not recognized?

Make sure you're in the `/Volumes/Dev/Course_Generator` directory or that skills are installed globally.

### Excel template seems incomplete?

The conversation might not have gathered all details. You can:
```
Continue working on the {course-name} course and add more session outcomes
```

### Story frameworks too generic?

Provide more specific cultural context and personal anecdotes during requirements gathering.

## What to Do with Generated Files

### Excel Template (03-template.xlsx)

**Use it to:**
- Import into your LMS (if it supports this format)
- Share with curriculum designers
- Guide content creation
- Track progress

### Story Frameworks (Module-X-Lesson-Y.md)

**Use them to:**
- Write video scripts
- Create PowerPoint presentations
- Design interactive e-learning modules
- Brief instructors on narrative approach

## Next Steps

1. ✅ Create your first course
2. ✅ Generate story frameworks
3. ⬜ Customize the frameworks for your specific context
4. ⬜ Develop actual content (videos/slides)
5. ⬜ Test with learners and iterate

## Need Help?

- Check `README.md` for detailed documentation
- Review `storytelling-skill-specification.md` for storytelling technique details
- Look at `.claude/skills/course-design-skill/references/TEMPLATE_GUIDE.md` for Excel format

---

**Ready to start?** Just say:
```
Help me design a course for [your topic]
```
