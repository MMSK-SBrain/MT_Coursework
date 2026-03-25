# Customer Support Chatbot - Capstone Project Rubric

**Total Points: 200**

## 1. Intent Classification Model (50 points)

### Model Performance (25 points)
- **Outstanding (23-25 pts)**: Accuracy >95%, handles all intents correctly
- **Excellent (20-22 pts)**: Accuracy 90-95%, handles most intents well
- **Good (17-19 pts)**: Accuracy 85-90%, some confusion between similar intents
- **Satisfactory (14-16 pts)**: Accuracy 80-85%, needs improvement
- **Needs Work (<14 pts)**: Accuracy <80%

### Model Implementation (15 points)
- Proper data preprocessing (5 pts)
- Appropriate vectorization (TF-IDF or embeddings) (5 pts)
- Well-chosen algorithm with justification (5 pts)

### Evaluation (10 points)
- Comprehensive metrics (accuracy, precision, recall, F1) (5 pts)
- Confusion matrix and analysis (3 pts)
- Error analysis conducted (2 pts)

---

## 2. Response Generation (40 points)

### Response Quality (20 points)
- **Outstanding (18-20 pts)**: Natural, helpful, contextually appropriate responses
- **Excellent (15-17 pts)**: Clear and helpful responses with minor issues
- **Good (12-14 pts)**: Adequate responses, could be more natural
- **Satisfactory (9-11 pts)**: Basic responses that answer queries
- **Needs Work (<9 pts)**: Poor or inappropriate responses

### Response Coverage (10 points)
- Supports 15+ intents (10 pts)
- Supports 12-14 intents (8 pts)
- Supports 10-11 intents (6 pts)
- Supports 8-9 intents (4 pts)
- Supports <8 intents (2 pts)

### Response Variety (10 points)
- Multiple response templates per intent (5 pts)
- Random selection for naturalness (3 pts)
- Contextually appropriate tone (2 pts)

---

## 3. Chatbot Logic and Integration (40 points)

### Complete Pipeline (20 points)
- User input → preprocessing → intent → response flow working (10 pts)
- Confidence scoring implemented (5 pts)
- Unknown intent handling (fallback responses) (5 pts)

### Error Handling (10 points)
- Graceful handling of unexpected inputs (5 pts)
- Appropriate error messages (3 pts)
- Logging and debugging support (2 pts)

### Conversation Flow (10 points)
- Smooth conversation experience (5 pts)
- Context awareness (if implemented) (3 pts)
- Natural dialogue feel (2 pts)

---

## 4. Streamlit User Interface (30 points)

### Functionality (15 points)
- Chat interface working smoothly (7 pts)
- Message display (user vs bot) clear (4 pts)
- Input handling and response generation (4 pts)

### User Experience (10 points)
- Clean, professional design (4 pts)
- Easy to use and navigate (3 pts)
- Responsive and fast (3 pts)

### Features (5 points)
- Chat history display (2 pts)
- Clear chat option (1 pt)
- Confidence/intent display (2 pts)

---

## 5. Deployment (25 points)

### Successful Deployment (15 points)
- App deployed to Streamlit Cloud (or alternative) (10 pts)
- Public URL accessible (5 pts)

### Deployment Quality (10 points)
- App loads without errors (5 pts)
- Performs well in production (3 pts)
- Models and data properly included (2 pts)

---

## 6. Documentation (10 points)

### README.md (5 points)
- Project overview and features (2 pts)
- Setup and installation instructions (2 pts)
- Usage guide and examples (1 pt)

### Code Documentation (5 points)
- Docstrings for functions (2 pts)
- Inline comments where needed (2 pts)
- Clear variable names (1 pt)

---

## 7. Code Quality (5 points)

- Clean, readable code (2 pts)
- Proper project structure (2 pts)
- Best practices followed (1 pt)

---

## Grading Scale

- **A (180-200 pts)**: Outstanding work, production-ready chatbot
- **B (160-179 pts)**: Excellent work, minor improvements needed
- **C (140-159 pts)**: Good work, some areas need improvement
- **D (120-139 pts)**: Satisfactory, significant improvements needed
- **F (<120 pts)**: Needs substantial work

---

## Bonus Points (up to +10)

- **Advanced Features** (+5): Entity extraction, context management, or API integration
- **Creative Enhancements** (+3): Exceptional UI/UX, unique features
- **Documentation Excellence** (+2): Video demo, comprehensive guides

---

## Submission Checklist

- [ ] Intent classifier accuracy >90%
- [ ] 15+ supported intents
- [ ] Working Streamlit app
- [ ] Deployed with public URL
- [ ] Complete README.md
- [ ] All code properly commented
- [ ] intents.json with patterns and responses
- [ ] Model files (classifier and vectorizer)

---

**Instructor Notes:**
- Emphasize that this is a portfolio piece
- Encourage creativity in UI design and features
- Test the deployed app thoroughly before grading
- Look for thoughtful intent design and natural responses
- Consider real-world applicability

**Last Updated**: 2026-01-06
