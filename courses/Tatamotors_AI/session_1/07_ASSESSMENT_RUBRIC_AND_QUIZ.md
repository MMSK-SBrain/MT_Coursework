# Session 1: Assessment & Evaluation
## Rubrics, Quizzes, and Knowledge Checks

---

## Table of Contents
1. [Formative Assessment (During Session)](#formative-assessment-during-session)
2. [Summative Assessment (End of Session)](#summative-assessment-end-of-session)
3. [Knowledge Check Quiz](#knowledge-check-quiz)
4. [Practical Skills Assessment](#practical-skills-assessment)
5. [Homework Evaluation Rubric](#homework-evaluation-rubric)
6. [Self-Assessment Checklist](#self-assessment-checklist)

---

## Formative Assessment (During Session)

### Checkpoint 1: Environment Setup (Module 0)
**Time:** 5 minutes into session

**Quick Check:**
- [ ] Can run Python code
- [ ] All libraries imported successfully
- [ ] No error messages in imports

**Instructor Action:** Don't proceed until 90% of students pass this checkpoint.

---

### Checkpoint 2: Document Loading (Module 1)
**Time:** 30 minutes into session

**Quick Check:**
```python
# Student should be able to:
print(f"Loaded {len(documents)} pages")  # Should show correct number
print(f"Sample: {documents[0].page_content[:100]}")  # Should show text
```

**Pass Criteria:**
- ✅ PDF loaded successfully
- ✅ Can print number of pages
- ✅ Can display text content

---

### Checkpoint 3: Chunking (Module 1)
**Time:** 45 minutes into session

**Quick Check:**
```python
# Student should understand:
print(f"Created {len(chunks)} chunks from {len(documents)} pages")
# Should be 3-5x the number of pages
```

**Verbal Check:** Ask random students:
- "Why do we chunk documents?"
- "What does chunk_overlap do?"

---

### Checkpoint 4: Vector Database (Module 2)
**Time:** 90 minutes into session

**Quick Check:**
```python
# Should work:
results = vectorstore.similarity_search("turbocharger", k=3)
print(f"Found {len(results)} results")
```

**Pass Criteria:**
- ✅ Vector database created without errors
- ✅ Similarity search returns results
- ✅ Results are relevant to query

---

### Checkpoint 5: RAG Pipeline (Module 3)
**Time:** 130 minutes into session

**Quick Check:**
```python
result = qa_chain({"query": "What is a TSI engine?"})
print(result['result'])
```

**Pass Criteria:**
- ✅ Query returns an answer (not error)
- ✅ Answer is related to the question
- ✅ Sources are included

---

### Checkpoint 6: UI Launch (Module 4)
**Time:** 160 minutes into session

**Quick Check:**
- [ ] Gradio interface launches
- [ ] Can type question and get answer
- [ ] Public link works (can share with neighbor)

---

## Summative Assessment (End of Session)

### Overall Success Criteria

**Minimum to Pass Session 1:**

| Component | Requirement | Weight |
|-----------|-------------|--------|
| **Working Code** | All cells run without errors | 40% |
| **RAG System** | Correctly answers 3/5 test questions | 30% |
| **Understanding** | Can explain RAG workflow verbally | 20% |
| **Interface** | Gradio UI launches and functions | 10% |

**Grade Levels:**

**A (Excellent):** 90-100%
- All code works perfectly
- Answers 5/5 test questions correctly
- Can explain concepts clearly
- Customized UI
- Completed at least 1 optional exercise

**B (Good):** 80-89%
- All code works with minor issues
- Answers 4/5 test questions correctly
- Understands core concepts
- Standard UI working

**C (Satisfactory):** 70-79%
- Most code works
- Answers 3/5 test questions correctly
- Basic understanding of RAG
- UI launches (even if basic)

**D (Needs Improvement):** 60-69%
- Some components working
- Answers 2/5 questions correctly
- Struggling with concepts
- May need remedial session

**F (Incomplete):** <60%
- Major components not working
- Cannot answer questions
- Needs to repeat session

---

## Knowledge Check Quiz

### Part A: Multiple Choice (20 points)
**Instructions:** Choose the best answer for each question.

---

**Question 1:** What does RAG stand for?

A) Random Access Generation
B) Retrieval Augmented Generation
C) Rapid AI Generator
D) Recursive Automated Grouping

**Correct Answer:** B
**Points:** 2

---

**Question 2:** Why do we chunk documents instead of using entire pages?

A) To save storage space
B) To make processing faster
C) To improve retrieval precision and fit context limits
D) Because PDFs are too large

**Correct Answer:** C
**Points:** 2

---

**Question 3:** What is the purpose of embeddings?

A) To compress text to save space
B) To convert text to numbers that capture meaning
C) To encrypt text for security
D) To translate text to different languages

**Correct Answer:** B
**Points:** 2

---

**Question 4:** What is chunk_overlap used for?

A) To make chunks bigger
B) To prevent splitting sentences and maintain context
C) To duplicate data for backup
D) To confuse the AI

**Correct Answer:** B
**Points:** 2

---

**Question 5:** Which component costs money in our RAG system?

A) Document loading
B) Creating embeddings
C) Vector storage
D) LLM API calls

**Correct Answer:** D
**Points:** 2

---

**Question 6:** What does the 'k' parameter in similarity_search control?

A) The size of chunks
B) The number of results returned
C) The cost of queries
D) The speed of search

**Correct Answer:** B
**Points:** 2

---

**Question 7:** Why use OpenRouter instead of directly calling OpenAI?

A) It's faster
B) It's more secure
C) Access to multiple models with one API
D) It's completely free

**Correct Answer:** C
**Points:** 2

---

**Question 8:** What does temperature control in LLM settings?

A) The speed of response
B) The cost per query
C) The creativity vs. factuality of responses
D) The length of responses

**Correct Answer:** C
**Points:** 2

---

**Question 9:** What is ChromaDB?

A) A web browser
B) A vector database
C) An LLM model
D) A PDF reader

**Correct Answer:** B
**Points:** 2

---

**Question 10:** What's the main advantage of RAG over fine-tuning?

A) Faster training
B) Can update knowledge without retraining
C) Uses less memory
D) Better at creative writing

**Correct Answer:** B
**Points:** 2

---

### Part B: True/False (10 points)
**Instructions:** Mark each statement as True (T) or False (F).

---

**Question 11:** Embeddings convert text into random numbers.
**Answer:** False (they capture semantic meaning, not random)
**Points:** 1

---

**Question 12:** Larger chunk_size always produces better results.
**Answer:** False (it's a trade-off)
**Points:** 1

---

**Question 13:** We use local embeddings (Sentence Transformers) to save cost.
**Answer:** True
**Points:** 1

---

**Question 14:** The RAG system can answer questions not in the source documents.
**Answer:** False (or it shouldn't if properly configured)
**Points:** 1

---

**Question 15:** Increasing the number of retrieved chunks (k) always improves answer quality.
**Answer:** False (more chunks can add noise)
**Points:** 1

---

**Question 16:** ChromaDB saves embeddings to disk automatically with persist_directory.
**Answer:** True
**Points:** 1

---

**Question 17:** Temperature of 0.0 makes the LLM more creative.
**Answer:** False (lower temp = more deterministic/factual)
**Points:** 1

---

**Question 18:** We need to recreate embeddings every time we run the notebook.
**Answer:** False (can reload from persisted database)
**Points:** 1

---

**Question 19:** Gradio public links work forever.
**Answer:** False (expire after 72 hours)
**Points:** 1

---

**Question 20:** The cost of a RAG query depends on the number of tokens processed.
**Answer:** True
**Points:** 1

---

### Part C: Short Answer (30 points)
**Instructions:** Provide brief answers (2-4 sentences).

---

**Question 21:** Explain the RAG workflow in your own words. (6 points)

**Model Answer:**
RAG works by first processing documents into chunks and converting them to embeddings. When a user asks a question, it's converted to an embedding and compared against stored chunks to find the most relevant ones. These relevant chunks are then sent to an LLM along with the question, and the LLM generates an answer based on that context. This allows the AI to answer questions accurately using specific document knowledge.

**Grading:**
- 6 pts: Complete, accurate explanation
- 4 pts: Mostly correct, minor gaps
- 2 pts: Partial understanding
- 0 pts: Incorrect or missing

---

**Question 22:** Why is chunk_size=1000 often better than chunk_size=5000? (6 points)

**Model Answer:**
Smaller chunks (1000) are more focused on specific topics, making retrieval more precise. When searching for information about "turbocharger," a 1000-character chunk is likely about just that topic, while a 5000-character chunk might cover multiple topics and dilute relevance. Smaller chunks also help stay within context limits and reduce token costs. However, chunks that are too small lose context, so 1000 is a good middle ground.

**Grading:**
- 6 pts: Explains precision, focus, and trade-offs
- 4 pts: Mentions some advantages
- 2 pts: Basic understanding
- 0 pts: Incorrect

---

**Question 23:** What is the role of embeddings in similarity search? (6 points)

**Model Answer:**
Embeddings convert text into numerical vectors that capture semantic meaning. Similar concepts have similar vectors (close in vector space). During similarity search, the query is embedded and compared against stored chunk embeddings using cosine similarity or similar metrics. Chunks with vectors closest to the query vector are retrieved, meaning we find chunks with similar meaning rather than just keyword matches.

**Grading:**
- 6 pts: Explains vectors, semantic meaning, and similarity
- 4 pts: Understands basic concept
- 2 pts: Vague understanding
- 0 pts: Incorrect

---

**Question 24:** How would you reduce the cost of running this RAG system? (6 points)

**Model Answer:**
Several strategies: (1) Use free local embeddings instead of API-based ones (we already do this), (2) Use cheaper LLM models like Gemini Flash instead of GPT-4, (3) Reduce the number of chunks retrieved (lower k value), (4) Set max_tokens limit to cap response length, (5) Implement caching for repeated questions, and (6) Use smaller chunk_size to reduce context tokens sent to LLM.

**Grading:**
- 6 pts: Lists 4+ valid strategies
- 4 pts: Lists 2-3 strategies
- 2 pts: Lists 1 strategy
- 0 pts: No valid strategies

---

**Question 25:** What are the limitations of this basic RAG system? (6 points)

**Model Answer:**
Limitations include: (1) No conversation memory - can't handle follow-up questions, (2) Single document only - can't search across multiple manuals, (3) No confidence scoring - doesn't indicate when unsure, (4) No source highlighting - shows page number but not exact sentence, (5) Basic error handling - doesn't gracefully handle edge cases, and (6) No advanced features like filtering by document section or date.

**Grading:**
- 6 pts: Identifies 4+ valid limitations
- 4 pts: Identifies 2-3 limitations
- 2 pts: Identifies 1 limitation
- 0 pts: No valid limitations

---

### Part D: Code Analysis (20 points)

**Question 26:** What's wrong with this code? Fix it. (10 points)

```python
chunks = text_splitter.split_documents(documents)
vectorstore = Chroma.from_documents(
    chunks=chunks,
    embeddings=embeddings
)
```

**Issues:**
1. Parameter name is wrong: `documents=chunks` not `chunks=chunks`
2. Parameter name is wrong: `embedding=embeddings` not `embeddings=embeddings`

**Corrected:**
```python
chunks = text_splitter.split_documents(documents)
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings
)
```

**Grading:**
- 10 pts: Identifies and fixes both errors
- 6 pts: Identifies both but fixes only one
- 3 pts: Identifies one error
- 0 pts: No correct answer

---

**Question 27:** Analyze this retrieval result. Is it good? Why or why not? (10 points)

```
Question: "How does the turbocharger work?"

Retrieved chunks:
1. Page 15: "The turbocharger increases engine power by..."
2. Page 42: "Maintenance schedules for TSI engines include..."
3. Page 8: "The bicycle industry has seen many innovations..."
```

**Analysis:**
This retrieval is POOR. Chunk 1 is highly relevant and directly answers the question. However, chunk 2 is marginally related (same engine but different topic) and chunk 3 is completely irrelevant (wrong domain entirely - bicycles!). This suggests problems with the vector database or chunk quality. Good retrieval would have all 3 chunks about turbocharger function.

**Possible causes:**
- Poorly formed chunks
- Vector database contamination (non-automotive content)
- Need to increase k to get better results
- Embedding quality issues

**Grading:**
- 10 pts: Correctly identifies issues and suggests causes
- 7 pts: Identifies main issues
- 4 pts: Recognizes something is wrong
- 0 pts: Says it's good

---

### Quiz Scoring Summary

**Total Points: 80**

| Section | Points |
|---------|--------|
| Part A: Multiple Choice | 20 |
| Part B: True/False | 10 |
| Part C: Short Answer | 30 |
| Part D: Code Analysis | 20 |
| **Total** | **80** |

**Grading Scale:**
- A: 72-80 points (90-100%)
- B: 64-71 points (80-89%)
- C: 56-63 points (70-79%)
- D: 48-55 points (60-69%)
- F: <48 points (<60%)

---

## Practical Skills Assessment

### Hands-On Evaluation
**Time:** 30 minutes
**Format:** Live coding task

### Task: Build a Mini RAG System

**Instructions:**
Given a small text document (provided), build a working RAG system that can answer questions about it.

**Requirements:**
1. Load the document
2. Create chunks (you choose parameters)
3. Create embeddings
4. Build vector database
5. Set up LLM connection
6. Answer these 3 questions:
   - [Question 1 specific to document]
   - [Question 2 specific to document]
   - [Question 3 specific to document]

### Rubric

| Criteria | Excellent (4) | Good (3) | Fair (2) | Poor (1) | Points |
|----------|---------------|----------|----------|----------|--------|
| **Document Loading** | Loads correctly, handles errors | Loads correctly | Loads with minor issues | Fails to load | /4 |
| **Chunking** | Optimal parameters, justified choice | Working chunks | Chunks too large/small | Doesn't work | /4 |
| **Embeddings** | Created efficiently | Works correctly | Slow but works | Fails | /4 |
| **Vector DB** | Created and persisted | Created | Works partially | Fails | /4 |
| **LLM Integration** | Works smoothly, good config | Works | Sporadic errors | Doesn't work | /4 |
| **Answer Quality** | 3/3 correct | 2/3 correct | 1/3 correct | 0/3 correct | /4 |
| **Code Quality** | Clean, commented, organized | Mostly clean | Messy but works | Very poor | /4 |
| **Troubleshooting** | Debugs independently | Needs hints | Needs help | Can't debug | /4 |

**Total: /32 points**

**Conversion:**
- A: 29-32 points
- B: 26-28 points
- C: 22-25 points
- D: 19-21 points
- F: <19 points

---

## Homework Evaluation Rubric

### Assignment: Complete Exercises 2, 4, and 7

### Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Needs Work (2) | Incomplete (1) | Points |
|----------|---------------|----------|------------------|----------------|----------------|--------|
| **Completion** | All 3 exercises done thoroughly | All done, minor gaps | 2/3 exercises complete | 1/3 exercises complete | Little to no work | /5 |
| **Code Quality** | Clean, commented, follows best practices | Mostly clean | Works but messy | Barely works | Doesn't work | /5 |
| **Analysis** | Deep insights, clear explanations | Good analysis | Basic observations | Minimal analysis | No analysis | /5 |
| **Experimentation** | Tries variations beyond requirements | Meets requirements | Does minimum | Below minimum | None | /5 |
| **Documentation** | Excellent notes, findings well-organized | Good documentation | Basic notes | Poor documentation | None | /5 |
| **Reflection** | Thoughtful learning takeaways | Good reflection | Basic reflection | Minimal | None | /5 |

**Total: /30 points**

**Bonus Points (up to 5):**
- Completed recommended exercises: +2
- Completed challenge project: +3
- Helped classmates: +1
- Creative solution/approach: +1

**Grading Scale:**
- A: 27-30+ points
- B: 24-26 points
- C: 21-23 points
- D: 18-20 points
- F: <18 points

---

## Self-Assessment Checklist

### Knowledge & Understanding

**After Session 1, I can:**

**Core Concepts:**
- [ ] Explain what RAG is and why it's useful
- [ ] Describe the RAG workflow (4 steps)
- [ ] Explain the purpose of embeddings
- [ ] Understand what vector databases do
- [ ] Explain chunk size trade-offs

**Technical Skills:**
- [ ] Load PDF documents with PyPDFLoader
- [ ] Split documents into chunks
- [ ] Configure chunking parameters
- [ ] Create embeddings using Sentence Transformers
- [ ] Build a ChromaDB vector database
- [ ] Perform similarity search
- [ ] Connect to OpenRouter API
- [ ] Configure LLM parameters
- [ ] Build a RetrievalQA chain
- [ ] Create a Gradio interface

**Applied Knowledge:**
- [ ] Can optimize chunk size for different use cases
- [ ] Can choose appropriate k value for retrieval
- [ ] Understand cost implications of design choices
- [ ] Can troubleshoot common errors
- [ ] Can explain my code to others

**Readiness for Session 2:**
- [ ] Have working RAG system from Session 1
- [ ] Completed required homework
- [ ] Understand limitations of current system
- [ ] Ready to add conversation memory
- [ ] Excited to learn more!

### Confidence Levels

Rate your confidence (1-5, where 5 = very confident):

| Skill | Confidence |
|-------|------------|
| Loading and processing documents | __/5 |
| Creating and using embeddings | __/5 |
| Working with vector databases | __/5 |
| Integrating LLMs via API | __/5 |
| Building user interfaces | __/5 |
| Troubleshooting errors | __/5 |
| Optimizing for cost/performance | __/5 |
| Overall RAG understanding | __/5 |

**Average Confidence:** __/5

**Interpretation:**
- 4.5-5.0: Excellent! Ready for advanced topics
- 3.5-4.4: Good! Solid foundation
- 2.5-3.4: Fair - review concepts before Session 2
- <2.5: Needs review - talk to instructor

---

## Instructor Evaluation Guidelines

### During Session Observations

**Track these metrics:**
- % of students who complete each checkpoint on time
- Number of students needing help at each stage
- Common questions/confusions
- Average time to complete each module
- Overall engagement level

### Post-Session Evaluation

**Evaluate:**
1. **Learning Outcomes Achievement**
   - What % achieved each MLO?
   - Which outcomes were hardest?
   - What needs more emphasis next time?

2. **Session Effectiveness**
   - Did timing work?
   - Were explanations clear?
   - Were exercises appropriate?
   - Was technology reliable?

3. **Student Readiness**
   - Are students ready for Session 2?
   - Who needs extra support?
   - What review is needed?

### Quality Metrics

**Target Success Rates:**
- 90%+ complete the session with working code
- 80%+ score 70%+ on quiz
- 75%+ submit homework on time
- 70%+ rate session 4/5 or better

---

## Feedback Collection

### Student Feedback Survey

**Rate 1-5 (1=Poor, 5=Excellent):**

1. Overall session quality: __/5
2. Pace of instruction: __/5
3. Clarity of explanations: __/5
4. Usefulness of exercises: __/5
5. Quality of materials: __/5
6. Instructor effectiveness: __/5

**Open-Ended:**
- What was most valuable?
- What was most confusing?
- What would you change?
- Additional comments?

---

## Continuous Improvement

### After Each Session:

1. **Review all assessments**
   - Identify common mistakes
   - Note difficult concepts
   - Track improvement areas

2. **Update materials**
   - Add clarifications where needed
   - Create additional examples for difficult concepts
   - Improve exercises based on feedback

3. **Prepare for next session**
   - Address gaps in understanding
   - Adjust pace if needed
   - Plan remedial support for struggling students

---

**End of Assessment Guide**

Remember: Assessment is about learning, not just grading. Use these tools to help students succeed!
