# Session 1: Exercises & Challenges
## Hands-On Practice for RAG System Development

**Purpose:** Reinforce learning through practical exercises
**Time:** Complete during session + homework
**Difficulty Levels:** Beginner → Intermediate → Advanced

---

## How to Use This Document

- **During Session:** Complete exercises marked [IN-CLASS]
- **Homework:** Complete exercises marked [HOMEWORK]
- **Stretch Goals:** Try [CHALLENGE] exercises if you finish early
- **Solutions:** Available in separate solutions file (ask instructor)

---

## Exercise 1: Document Processing Exploration
**[IN-CLASS] | Difficulty: Beginner | Time: 10 minutes**

### Objective
Understand how documents are loaded and chunked.

### Tasks

**Task 1.1: Find Specific Content**
Write code to find all chunks that mention "turbocharger"

```python
# Your code here:
# Hint: Loop through chunks and check if "turbocharger" is in page_content
```

**Task 1.2: Analyze Chunk Distribution**
Calculate statistics about your chunks:
- Average chunk length
- Minimum and maximum chunk lengths
- Which page has the most chunks?

```python
# Your code here:
```

**Task 1.3: Chunk Boundary Analysis**
Find and print a chunk that you think might be "split badly" (cuts off mid-sentence or mid-thought)

```python
# Your code here:
# Look for chunks that start or end awkwardly
```

### Reflection Questions
1. Why do some chunks have more content than others?
2. What happens at page boundaries?
3. How does chunk_overlap help with continuity?

---

## Exercise 2: Experimenting with Chunking Parameters
**[IN-CLASS] | Difficulty: Intermediate | Time: 15 minutes**

### Objective
Understand the impact of different chunking strategies.

### Tasks

**Task 2.1: Small Chunks**
Create chunks with `chunk_size=500` and `chunk_overlap=100`

```python
small_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
small_chunks = small_splitter.split_documents(documents)

print(f"Small chunks: {len(small_chunks)}")
print(f"Sample: {small_chunks[10].page_content}")
```

**Task 2.2: Large Chunks**
Create chunks with `chunk_size=2000` and `chunk_overlap=400`

```python
# Your code here:
```

**Task 2.3: Comparison**
Compare the three versions (original 1000, small 500, large 2000):

| Chunk Size | Total Chunks | Avg Length | Pros | Cons |
|------------|--------------|------------|------|------|
| 500 | ? | ? | ? | ? |
| 1000 | ? | ? | ? | ? |
| 2000 | ? | ? | ? | ? |

### Reflection Questions
1. Which chunk size would you use for very technical, dense documents?
2. Which for more narrative, conversational documents?
3. What's the trade-off between chunk size and retrieval precision?

---

## Exercise 3: Embedding Exploration
**[IN-CLASS] | Difficulty: Intermediate | Time: 15 minutes**

### Objective
Understand how embeddings capture semantic similarity.

### Tasks

**Task 3.1: Compare Similar Terms**
Embed automotive terms and compare their similarity:

```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

# Embed terms
terms = [
    "turbocharger",
    "supercharger",
    "exhaust system",
    "bicycle",
    "computer"
]

embeddings = model.encode(terms)

# Calculate cosine similarity between turbocharger and others
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

turbo_embedding = embeddings[0]
for i, term in enumerate(terms[1:], 1):
    similarity = cosine_similarity(turbo_embedding, embeddings[i])
    print(f"turbocharger vs {term}: {similarity:.4f}")
```

**Task 3.2: Predict Similarity**
Before running the code, predict: Which term will be MOST similar to "turbocharger"?
After running: Were you right?

**Task 3.3: Create Your Own Test**
Add 3 more automotive terms and 2 non-automotive terms. Compare their similarities.

### Reflection Questions
1. Why is "supercharger" more similar to "turbocharger" than "bicycle"?
2. What does a similarity score of 0.8 vs 0.3 tell you?
3. How does this help with retrieval?

---

## Exercise 4: Vector Search Optimization
**[HOMEWORK] | Difficulty: Intermediate | Time: 20 minutes**

### Objective
Learn to optimize retrieval quality.

### Tasks

**Task 4.1: Test Different k Values**
Try retrieving 1, 3, 5, and 10 chunks for the same question:

```python
question = "How does the turbocharger wastegate work?"

for k in [1, 3, 5, 10]:
    results = vectorstore.similarity_search(question, k=k)
    print(f"\n=== k={k} ===")
    for i, doc in enumerate(results):
        print(f"{i+1}. Page {doc.metadata.get('page')}: {doc.page_content[:100]}...")
```

**Task 4.2: Analyze Results**
- At what k value do you start seeing irrelevant chunks?
- What's the optimal k for this question?
- Try 3 different questions - does the optimal k change?

**Task 4.3: Similarity Scores**
Modify the search to show similarity scores:

```python
results = vectorstore.similarity_search_with_score(question, k=5)
for doc, score in results:
    print(f"Score: {score:.4f} | Page: {doc.metadata.get('page')}")
```

### Deliverable
Create a table showing optimal k values for different types of questions:
- Factual questions (e.g., "What is X?")
- How-to questions (e.g., "How does X work?")
- Comparative questions (e.g., "What's the difference between X and Y?")

---

## Exercise 5: Prompt Engineering
**[HOMEWORK] | Difficulty: Intermediate | Time: 30 minutes**

### Objective
Improve answer quality through better prompts.

### Tasks

**Task 5.1: Create 3 Different System Prompts**

**Version 1: Basic**
```python
prompt_v1 = "Answer the question based on the context."
```

**Version 2: Detailed**
```python
prompt_v2 = """You are an automotive technical expert.
Answer questions accurately using the provided context.
Use technical terms but explain them clearly."""
```

**Version 3: Your Custom Version**
```python
prompt_v3 = """
# Create your own improved prompt here
"""
```

**Task 5.2: Test All Three**
Use the same question with each prompt version and compare:
- Which gives the most accurate answer?
- Which is easiest to understand?
- Which includes the most relevant details?

**Task 5.3: Edge Cases**
Test your prompts with:
- A question NOT in the document
- A vague question
- A very specific technical question

### Deliverable
Write your best prompt and explain why it works better than the basic version.

---

## Exercise 6: Cost Optimization
**[HOMEWORK] | Difficulty: Advanced | Time: 30 minutes**

### Objective
Minimize costs while maintaining quality.

### Tasks

**Task 6.1: Measure Token Usage**
Calculate approximate token usage for 10 queries:

```python
import tiktoken

encoder = tiktoken.encoding_for_model("gpt-3.5-turbo")

def count_tokens(text):
    return len(encoder.encode(text))

total_input_tokens = 0
total_output_tokens = 0

for question in test_questions:
    result = qa_chain({"query": question})

    # Count input tokens (question + retrieved context)
    context = "\n".join([doc.page_content for doc in result['source_documents']])
    input_tokens = count_tokens(question + context)

    # Count output tokens
    output_tokens = count_tokens(result['result'])

    total_input_tokens += input_tokens
    total_output_tokens += output_tokens

print(f"Total input tokens: {total_input_tokens}")
print(f"Total output tokens: {total_output_tokens}")
print(f"Estimated cost: ${(total_input_tokens * 0.075 + total_output_tokens * 0.30) / 1_000_000:.6f}")
```

**Task 6.2: Optimization Strategies**
Try these cost-saving techniques:
1. Reduce k from 3 to 2
2. Use smaller chunk_size (less context)
3. Limit max_tokens in LLM
4. Use cheaper model for simple questions

**Task 6.3: Quality vs Cost Analysis**
Create a table:

| Strategy | Cost per Query | Answer Quality (1-5) | Worth It? |
|----------|----------------|----------------------|-----------|
| Baseline (k=3, 1000 chunks) | $ | 5 | - |
| k=2 | $ | ? | ? |
| k=1 | $ | ? | ? |
| Smaller chunks | $ | ? | ? |
| Cheaper model | $ | ? | ? |

### Deliverable
Recommend the optimal cost/quality balance for:
- Learning/testing
- Production deployment
- Budget-constrained scenarios

---

## Exercise 7: Multi-Question Testing
**[IN-CLASS] | Difficulty: Beginner | Time: 15 minutes**

### Objective
Build a comprehensive test suite for your RAG system.

### Tasks

**Task 7.1: Create Test Questions**
Write 15 test questions covering:
- 5 factual questions (What is X?)
- 5 process questions (How does X work?)
- 5 comparison questions (X vs Y?)

**Task 7.2: Batch Testing**
```python
test_suite = [
    "What is a TSI engine?",
    "How does direct fuel injection work?",
    # ... add your 15 questions
]

results = []
for question in test_suite:
    result = qa_chain({"query": question})
    results.append({
        'question': question,
        'answer': result['result'],
        'sources': [doc.metadata.get('page') for doc in result['source_documents']]
    })

# Analyze results
for r in results:
    print(f"Q: {r['question']}")
    print(f"A: {r['answer'][:100]}...")
    print(f"Sources: {r['sources']}\n")
```

**Task 7.3: Quality Assessment**
Rate each answer:
- 5 = Perfect, accurate, complete
- 4 = Good, minor issues
- 3 = Acceptable, some errors
- 2 = Poor, misleading
- 1 = Wrong or useless

Calculate average score.

### Deliverable
- List of 15 test questions
- Quality scores
- Observations about what works well vs what doesn't

---

## Exercise 8: UI Customization
**[HOMEWORK] | Difficulty: Beginner | Time: 20 minutes**

### Objective
Make the Gradio interface more user-friendly and professional.

### Tasks

**Task 8.1: Enhanced UI**
Add these features to your Gradio interface:

```python
import gradio as gr

def enhanced_ask(question, num_sources):
    """
    Enhanced function with configurable number of sources
    """
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": num_sources})
    )

    result = qa_chain({"query": question})

    # Format answer with sources
    answer = result['result']
    sources = "\n\n📚 Sources:\n"
    for i, doc in enumerate(result['source_documents'], 1):
        sources += f"{i}. Page {doc.metadata.get('page')}: {doc.page_content[:150]}...\n\n"

    return answer, sources

interface = gr.Interface(
    fn=enhanced_ask,
    inputs=[
        gr.Textbox(lines=3, label="Your Question"),
        gr.Slider(minimum=1, maximum=5, value=3, step=1, label="Number of Sources")
    ],
    outputs=[
        gr.Textbox(lines=8, label="Answer"),
        gr.Textbox(lines=10, label="Source Documents")
    ],
    title="🚗 Automotive Technical Assistant Pro",
    description="Advanced RAG system with configurable source retrieval",
    theme="huggingface"
)
```

**Task 8.2: Add Examples**
Create 10 diverse example questions showcasing different capabilities.

**Task 8.3: Branding**
Customize:
- Title (make it creative!)
- Description (explain what it does)
- Theme (try different Gradio themes)
- Examples (domain-specific)

### Deliverable
Screenshot of your customized interface and public link.

---

## Exercise 9: Error Handling & Robustness
**[HOMEWORK] | Difficulty: Advanced | Time: 25 minutes**

### Objective
Make your system handle errors gracefully.

### Tasks

**Task 9.1: Input Validation**
```python
def safe_ask(question):
    # Check for empty input
    if not question or not question.strip():
        return "⚠️ Please enter a question."

    # Check for very short questions
    if len(question.split()) < 3:
        return "⚠️ Please ask a more detailed question."

    # Check for very long questions
    if len(question) > 500:
        return "⚠️ Question is too long. Please be more concise."

    try:
        result = qa_chain({"query": question})
        return result['result']
    except Exception as e:
        return f"❌ Error: {str(e)}\nPlease try again or contact support."
```

**Task 9.2: API Fallback**
Implement retry logic:

```python
import time

def robust_query(question, max_retries=3):
    for attempt in range(max_retries):
        try:
            result = qa_chain({"query": question})
            return result
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Attempt {attempt + 1} failed. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise e
```

**Task 9.3: Confidence Scoring**
Add a confidence indicator:

```python
def answer_with_confidence(question):
    results_with_scores = vectorstore.similarity_search_with_score(question, k=3)

    # Check top similarity score
    top_score = results_with_scores[0][1]

    if top_score < 0.3:
        confidence = "🟢 High"
    elif top_score < 0.6:
        confidence = "🟡 Medium"
    else:
        confidence = "🔴 Low"

    result = qa_chain({"query": question})

    return f"Confidence: {confidence}\n\n{result['result']}"
```

### Deliverable
Enhanced version of your RAG system with all error handling features.

---

## Exercise 10: Performance Benchmarking
**[HOMEWORK] | Difficulty: Advanced | Time: 30 minutes**

### Objective
Measure and optimize system performance.

### Tasks

**Task 10.1: Speed Testing**
```python
import time

def benchmark_query(question):
    start = time.time()

    # Embedding
    embed_start = time.time()
    query_embedding = embeddings.embed_query(question)
    embed_time = time.time() - embed_start

    # Retrieval
    retrieval_start = time.time()
    docs = vectorstore.similarity_search(question, k=3)
    retrieval_time = time.time() - retrieval_start

    # LLM
    llm_start = time.time()
    result = qa_chain({"query": question})
    llm_time = time.time() - llm_start

    total_time = time.time() - start

    print(f"Embedding: {embed_time:.3f}s")
    print(f"Retrieval: {retrieval_time:.3f}s")
    print(f"LLM: {llm_time:.3f}s")
    print(f"Total: {total_time:.3f}s")

    return result

# Test with 10 questions
questions = [...]  # Your test questions
for q in questions:
    print(f"\nQuestion: {q}")
    benchmark_query(q)
```

**Task 10.2: Bottleneck Identification**
Which component is slowest?
- If embedding: Already optimal (local)
- If retrieval: Database might need optimization
- If LLM: Try faster model or reduce context

**Task 10.3: Optimization**
Implement caching for repeated questions:

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def cached_query(question):
    return qa_chain({"query": question})
```

### Deliverable
Performance report with:
- Breakdown of time spent in each component
- Identified bottlenecks
- Optimization recommendations
- Before/after benchmarks

---

## Challenge Projects
**[CHALLENGE] | Difficulty: Advanced | Time: Multiple hours**

### Challenge 1: Multi-Document RAG
Extend your system to handle multiple PDFs:
- Load 3 different automotive manuals
- Tag chunks with source document
- Allow filtering by document in retrieval
- Display which document each answer came from

### Challenge 2: Conversational RAG
Add conversation memory:
- Remember previous questions
- Handle follow-up questions ("What about its advantages?")
- Maintain context across conversation

### Challenge 3: Advanced Analytics
Build a dashboard showing:
- Most asked questions
- Average response time
- User satisfaction ratings
- Common failure patterns

### Challenge 4: Production Deployment
Deploy your system:
- Docker containerization
- Environment variable management
- Logging and monitoring
- Rate limiting
- User authentication

### Challenge 5: Domain Expansion
Adapt your RAG system for a different domain:
- Legal documents
- Medical textbooks
- Company policies
- Technical specifications

---

## Homework Assignment Summary

**Required (Complete by next session):**
- [ ] Exercise 2: Chunking parameters experiment
- [ ] Exercise 4: Vector search optimization
- [ ] Exercise 7: Create and run 15-question test suite

**Recommended:**
- [ ] Exercise 5: Prompt engineering
- [ ] Exercise 6: Cost optimization
- [ ] Exercise 8: UI customization

**Optional (For enthusiasts):**
- [ ] Exercise 9: Error handling
- [ ] Exercise 10: Performance benchmarking
- [ ] Any Challenge Project

---

## Submission Guidelines

**What to Submit:**
1. Completed code (Python file or Colab link)
2. Results/outputs for each exercise
3. Brief reflection (1-2 paragraphs) on what you learned

**Format:**
- Single PDF or Word document, OR
- Google Colab notebook with outputs, OR
- GitHub repository with README

**Due Date:** Before Session 2

**Where to Submit:** [Instructor will provide link]

---

## Grading Rubric

| Criteria | Points |
|----------|--------|
| Completion of required exercises | 40% |
| Code quality and documentation | 20% |
| Depth of analysis/reflection | 20% |
| Creativity and exploration | 10% |
| Recommended exercises | 10% |

**Note:** This is formative assessment - focus is on learning, not grades!

---

## Tips for Success

1. **Don't rush:** Take time to understand each concept
2. **Experiment:** Try variations beyond what's specified
3. **Document:** Write comments explaining your thinking
4. **Ask questions:** No question is too basic
5. **Collaborate:** Discuss with classmates (but submit your own work)
6. **Have fun:** AI is exciting - enjoy the learning process!

---

**Good luck with your exercises! 🚀**

Remember: The goal is to BUILD understanding, not just complete tasks.
Experiment, break things, fix them, and learn!
