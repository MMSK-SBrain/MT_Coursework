# Session 1 Instructor Manual
## Foundation - Simple RAG with Single PDF

**Duration:** 170 minutes (2 hours 50 minutes)
**Format:** Hands-on workshop with live coding
**Level:** Beginner to Intermediate

---

## Table of Contents
1. [Session Overview](#session-overview)
2. [Pre-Session Preparation](#pre-session-preparation)
3. [Session Flow & Timing](#session-flow--timing)
4. [Module-by-Module Guide](#module-by-module-guide)
5. [Teaching Strategies](#teaching-strategies)
6. [Common Issues & Solutions](#common-issues--solutions)
7. [Assessment Guidelines](#assessment-guidelines)

---

## Session Overview

### Learning Philosophy
This session uses a **hands-on, build-as-you-learn** approach. Students will build a working RAG system incrementally, understanding each component before moving to the next. Emphasize:
- **Why before how**: Explain the purpose before diving into code
- **Immediate validation**: Test each component before moving forward
- **Real-world context**: Use automotive examples throughout
- **Cost awareness**: Highlight free vs. paid components

### Key Success Factors
- ✅ Every student has a working environment by minute 20
- ✅ All API keys are validated before LLM integration
- ✅ Students understand WHY each step is necessary
- ✅ At least 80% of students have a working RAG system by end of session

### Materials Checklist
- [ ] Session slides loaded and tested
- [ ] Google Colab notebook shared with students (or local environment setup)
- [ ] Sample SSP 913 PDF available for download
- [ ] OpenRouter setup guide distributed
- [ ] Backup API key for students who face issues
- [ ] Troubleshooting guide printed/accessible

---

## Pre-Session Preparation

### 1 Week Before Session
- [ ] Send pre-session email with setup instructions
- [ ] Share OpenRouter signup guide
- [ ] Ask students to create accounts and load $5 credit
- [ ] Share prerequisite Python tutorial (if needed)
- [ ] Prepare backup environment (in case Colab has issues)

### 1 Day Before Session
- [ ] Test the complete notebook end-to-end
- [ ] Verify OpenRouter API is responding
- [ ] Download SSP 913 PDF and verify it's readable
- [ ] Prepare breakout room assignments (if virtual)
- [ ] Test screen sharing and code visibility

### Day of Session (30 min before)
- [ ] Load all materials and test presentation setup
- [ ] Open Colab notebook and verify all cells run
- [ ] Have troubleshooting guide open in separate window
- [ ] Prepare to share API key for emergencies
- [ ] Set up timer for each module

---

## Session Flow & Timing

```
Total: 170 minutes
├── Module 0: Welcome & Setup (20 min)
├── Module 1: Document Processing (30 min)
├── Module 2: Embeddings & Vector Store (40 min)
├── BREAK (10 min)
├── Module 3: LLM Integration (30 min)
├── Module 4: UI Development (30 min)
└── Module 5: Wrap-up & Next Steps (10 min)
```

---

## Module-by-Module Guide

---

### MODULE 0: Welcome & Setup (20 minutes)

#### Objectives
- Build rapport and set expectations
- Ensure all students have working environments
- Verify prerequisites

#### Script & Activities

**[0-5 min] Introduction**

> "Welcome to the RAG Bootcamp! Over the next few hours, you're going to build something really powerful - an AI assistant that can answer technical questions about automotive systems by reading manuals, just like you would. But instead of flipping through hundreds of pages, it will do it instantly.
>
> By the end of today, you'll have a working chatbot that can answer questions about the TSI engine. In later sessions, we'll expand this to handle multiple manuals, diagnostic codes, and eventually deploy it as a production system.
>
> This is a hands-on session. We'll write code together, test it, break it, fix it, and learn by doing."

**Teaching Note:** Gauge the room - if students seem nervous, emphasize that everyone will succeed and you'll move at a pace that works for the group.

**[5-10 min] Environment Setup**

*Option A: Google Colab (Recommended)*
1. Share the Colab notebook link
2. Ask students to make a copy: File → Save a copy in Drive
3. Have students run the first cell (imports) to test
4. Watch for red error messages in the chat/raise hands

*Option B: Local Python*
1. Share requirements.txt
2. Guide through: `pip install -r requirements.txt`
3. Test imports in first cell

**Quick Poll:** "Who has successfully run the first cell?" - Don't proceed until 90%+ respond yes.

**[10-15 min] RAG Architecture Overview**

**Show Slide:** RAG Architecture Diagram

> "Before we code, let's understand what we're building. RAG stands for Retrieval Augmented Generation. It's a fancy way of saying: 'Let's give the AI access to specific documents so it can answer questions accurately.'
>
> Here's how it works in 4 steps:
> 1. **Prepare**: We load a PDF manual and break it into chunks
> 2. **Embed**: We convert these chunks into numbers (vectors) that represent their meaning
> 3. **Store**: We save these vectors in a database
> 4. **Retrieve & Generate**: When someone asks a question, we find the most relevant chunks and ask an AI to answer based on those chunks"

**Interactive Question:** "Why not just give the entire 500-page manual to ChatGPT?"

**Expected Answers (guide them to these):**
- Token limits (most LLMs can't handle that much text)
- Cost (more tokens = more money)
- Relevance (AI gets confused with too much irrelevant info)
- Speed (processing huge texts is slow)

**[15-20 min] Why RAG for Automotive?**

**Show Slide:** Real-world Use Cases

> "Imagine you're a technician diagnosing a complex TSI engine issue. You need to:
> - Understand how the turbocharger wastegate works
> - Check torque specifications for specific bolts
> - Review the timing chain replacement procedure
>
> Normally, you'd open multiple PDFs, use Ctrl+F, read pages of context...
>
> With RAG, you ask: 'What's the wastegate function?' and get an answer with citations in 2 seconds."

**Teaching Tip:** If you have automotive technicians in the class, ask them to share a time when finding information in manuals was challenging.

**Transition:** "Let's build this system step by step. First, we need to load and process our document."

---

### MODULE 1: Document Processing (30 minutes)

#### Objectives
- Load PDF using PyPDFLoader
- Understand chunking strategies
- Implement RecursiveCharacterTextSplitter
- Validate chunk quality

#### Script & Activities

**[0-5 min] Document Selection & Loading**

> "We're starting with VAG SSP 913 - the TSI Engine Technology manual. It's about 60 pages, technical but well-structured, and freely available. Perfect for learning."

**Live Coding - Cell 1:**

```python
# Let's load the PDF
from langchain.document_loaders import PyPDFLoader

# If you don't have the PDF yet, download it
# [Share the download link in chat]

loader = PyPDFLoader("vag_ssp_913_tsi_engine.pdf")
documents = loader.load()

print(f"Loaded {len(documents)} pages")
print(f"First page preview:\n{documents[0].page_content[:500]}")
```

**Ask students to run this cell**

**Checkpoint:** "Who sees the number of pages printed? Who sees text from the manual?"

**Teaching Note:** Common issue - file path. If students have the PDF in a different location, help them adjust the path. In Colab, they may need to upload the file first.

**[5-15 min] Understanding Chunking**

**Show Slide:** Why We Need Chunking

> "Now we have 60 pages of text. But we can't just throw entire pages at the AI. Here's why:
>
> A single page might talk about 5 different topics. If we ask about 'turbocharger,' we might retrieve a page that mentions it once but is mostly about something else.
>
> Instead, we break pages into smaller, focused chunks - typically 500-1500 characters each."

**Interactive Demo:**

Show a sample page from the PDF. Highlight how one page covers multiple topics.

> "If we chunk this into 3 pieces, each chunk is focused on ONE topic. When we search, we get exactly the relevant section."

**Whiteboard/Slide:** Chunking Parameters

```
chunk_size = 1000
├── Too small (200): Loses context, sentences cut off
├── Just right (1000): One topic, complete thoughts
└── Too large (5000): Multiple topics, less precise retrieval

chunk_overlap = 200
├── No overlap (0): Might split mid-sentence
├── Good overlap (200): Ensures continuity
└── Too much overlap (500): Redundant, wastes space
```

**[15-25 min] Implementing Chunking**

**Live Coding - Cell 2:**

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Create a smart text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,        # ~250 words per chunk
    chunk_overlap=200,      # 200 chars overlap between chunks
    separators=["\n\n", "\n", ". ", " ", ""]  # Split on paragraphs first, then sentences
)

# Split all pages into chunks
chunks = text_splitter.split_documents(documents)

print(f"Split {len(documents)} pages into {len(chunks)} chunks")
print(f"\nSample chunk:\n{chunks[10].page_content}")
```

**Ask students to run this cell**

**Discussion Question:** "How many chunks did you get? Is it more or less than the number of pages?"

**Expected:** Should be 3-5x the number of pages (60 pages → 180-300 chunks)

**[25-30 min] Student Exercise: Chunk Exploration**

**Exercise:** "Find a chunk that talks about 'turbocharger' - print the full chunk"

**Guided Solution:**
```python
# Solution
for i, chunk in enumerate(chunks):
    if "turbocharger" in chunk.page_content.lower():
        print(f"Found in chunk {i}:")
        print(chunk.page_content)
        print("\n" + "="*50 + "\n")
        break
```

**Teaching Tip:** Walk around (or monitor chat) to see who's stuck. Provide hints:
- "You'll need a loop to check each chunk"
- "Use the 'in' keyword to search for text"
- "Remember to check .page_content, not the chunk object itself"

**Transition:** "Great! Now we have well-structured chunks. Next, we need to convert these into numbers so a computer can understand their meaning."

---

### MODULE 2: Embeddings & Vector Store (40 minutes)

#### Objectives
- Understand what embeddings are
- Create embeddings using Sentence Transformers
- Build ChromaDB vector store
- Perform similarity search

#### Script & Activities

**[0-10 min] What Are Embeddings?**

**Show Slide:** Embeddings Visualization

> "Embeddings are the magic that makes RAG work. They convert text into numbers - specifically, into lists of numbers called vectors.
>
> But these aren't random numbers. They're special numbers that capture MEANING."

**Analogy:**
> "Think of it like GPS coordinates. 'Mumbai' and 'Pune' are close on a map because their coordinates are similar.
> Similarly, 'turbocharger' and 'supercharger' have similar embedding vectors because they're related concepts."

**Show Diagram:** 2D/3D embedding space with automotive terms clustered

**Interactive Demo:**

```python
from sentence_transformers import SentenceTransformer

# Load a free embedding model (runs on your computer!)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Let's embed some automotive terms
terms = ["turbocharger", "supercharger", "engine", "bicycle"]
embeddings = model.encode(terms)

print(f"Each term becomes a vector of {len(embeddings[0])} numbers")
print(f"\n'turbocharger' embedding (first 10 numbers):\n{embeddings[0][:10]}")
```

**Question:** "Which two terms do you think will have the most similar vectors?"

**Teaching Note:** If students ask about the math, briefly mention cosine similarity but don't go deep. Focus on the intuition: "similar meaning = similar vectors"

**[10-20 min] Creating Embeddings with LangChain**

**Live Coding - Cell 3:**

```python
from langchain.embeddings import HuggingFaceEmbeddings

# Use FREE local embeddings (no API calls!)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'},  # Use CPU (works everywhere)
    encode_kwargs={'normalize_embeddings': True}
)

# Test it
test_text = "How does the turbocharger work?"
test_embedding = embeddings.embed_query(test_text)

print(f"Your question became a vector of {len(test_embedding)} numbers!")
print(f"First 5 numbers: {test_embedding[:5]}")
```

**Key Teaching Point:**

> "Notice we're using HuggingFaceEmbeddings. This is FREE and runs locally on your computer. You don't need an API key, and there's no cost per query.
>
> This is one way we keep costs low - only the LLM (answer generation) costs money. Everything else is free!"

**[20-30 min] Building the Vector Database**

**Show Slide:** Vector Database Concept

> "Now we need to store these embeddings somewhere we can quickly search. That's what a vector database does.
>
> ChromaDB is perfect for learning - it's simple, stores data on disk, and doesn't require running a server."

**Live Coding - Cell 4:**

```python
from langchain.vectorstores import Chroma

# This might take 1-2 minutes - we're embedding ALL chunks
print("Creating vector database... (this takes ~1 minute)")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"  # Save to disk
)

print(f"✅ Vector database created with {vectorstore._collection.count()} chunks!")
```

**While this runs (60-90 seconds):**

> "Right now, the system is:
> 1. Taking each chunk
> 2. Converting it to a 384-number vector
> 3. Storing it in the database
>
> Once this is done, we can search through hundreds of chunks in milliseconds."

**Teaching Tip:** Students may ask why it's slow. Explain: "We only do this ONCE. After the database is saved, we can reload it instantly."

**[30-40 min] Similarity Search - The Magic Moment**

**Live Coding - Cell 5:**

```python
# Let's test our vector database!
query = "How does the turbocharger work?"

# Find the 3 most similar chunks
similar_docs = vectorstore.similarity_search(query, k=3)

print(f"Question: {query}\n")
print("="*70)

for i, doc in enumerate(similar_docs, 1):
    print(f"\n📄 RESULT {i}:")
    print(f"Page: {doc.metadata.get('page', 'Unknown')}")
    print(f"Content preview:\n{doc.page_content[:300]}...")
    print("-"*70)
```

**Ask students to run this**

**Discussion:**

> "Look at the results. Did it find relevant chunks? Are they actually about turbochargers?"

**Student Exercise (5 min):**

"Try your own questions! Modify the query and run the cell again. Try:"
- "What is the compression ratio?"
- "Explain direct fuel injection"
- "What are the main engine components?"

**Checkpoint:** "Who found relevant chunks for their question?"

**Teaching Note:** This is a WOW moment - celebrate it! Show how it found the right information without exact keyword matching.

**Transition:** "Awesome! We can now find relevant chunks. But they're just raw text. Let's add an AI to turn these chunks into natural answers."

---

### MODULE 3: LLM Integration (30 minutes)

#### Objectives
- Set up OpenRouter API
- Configure ChatOpenAI
- Build RetrievalQA chain
- Test complete RAG pipeline

#### Script & Activities

**[0-5 min] Why OpenRouter?**

> "We need an LLM to generate answers. We could use:
> - OpenAI GPT-4: Expensive ($0.03 per query)
> - Local models: Slow, need powerful computers
> - OpenRouter: Access to 100+ models, pay-as-you-go, starts FREE
>
> OpenRouter is perfect for learning - you can try different models and only pay for what you use."

**Show Slide:** Cost Comparison

| Model | Cost (1000 queries) | Speed | Quality |
|-------|---------------------|-------|---------|
| GPT-4 | $30 | Fast | Excellent |
| Gemini Flash | $0.75 | Very Fast | Good |
| Llama 3.1 8B | FREE tier | Medium | Decent |

**[5-10 min] API Setup**

**Pre-check:** "Who has already created an OpenRouter account and has their API key?"

**For those who haven't:**
1. Share the setup guide (separate document)
2. Give them 3 minutes to create account
3. Instructor demonstrates on screen

**API Key Security:**

> "⚠️ IMPORTANT: Never share your API key publicly. Don't commit it to GitHub. In our notebook, we'll use environment variables."

**Live Coding - Cell 6:**

```python
import os
from getpass import getpass

# Secure API key input (won't display the key)
if 'OPENROUTER_API_KEY' not in os.environ:
    os.environ['OPENROUTER_API_KEY'] = getpass("Enter your OpenRouter API key: ")

print("✅ API key set!")
```

**Teaching Tip:** Have a backup API key ready for students who face issues. Give it ONLY for this session and deactivate after class.

**[10-20 min] Connecting to the LLM**

**Live Coding - Cell 7:**

```python
from langchain.chat_models import ChatOpenAI

# Configure OpenRouter LLM
llm = ChatOpenAI(
    model_name="google/gemini-flash-1.5",  # Fast & cheap!
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=os.environ['OPENROUTER_API_KEY'],
    temperature=0.1  # Low = more factual, High = more creative
)

# Test the LLM
response = llm.predict("Say 'Hello, I am ready to help with automotive questions!'")
print(response)
```

**Checkpoint:** "Who got a response from the LLM?"

**Common Issues:**
- Invalid API key → Check spelling, regenerate key
- No credits → Need to add $5 to OpenRouter account
- Rate limit → Wait 30 seconds, try again

**[20-30 min] Building the Complete RAG Chain**

**The Big Moment!**

> "Now we connect everything:
> - Your question → Vector search → Find relevant chunks → LLM reads chunks → Generates answer"

**Live Coding - Cell 8:**

```python
from langchain.chains import RetrievalQA

# Create the RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # "stuff" = put all context into one prompt
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=True
)

# TEST IT!
question = "What is the compression ratio of the TSI engine?"
result = qa_chain({"query": question})

print(f"Question: {question}\n")
print(f"Answer: {result['result']}\n")
print(f"\n📚 Sources used:")
for i, doc in enumerate(result['source_documents'], 1):
    print(f"  {i}. Page {doc.metadata.get('page', '?')}")
```

**Ask students to run this cell**

**CELEBRATE THIS MOMENT!**

> "You just built a RAG system! The AI read the manual, found the answer, and cited its sources. This is real AI engineering!"

**Student Exercise (5 min):**

"Test these questions:"
1. "What are the main components of the TSI engine?"
2. "Explain the function of the turbocharger wastegate"
3. "What is direct fuel injection?"

**Discussion:**
- Are the answers accurate?
- Do the sources make sense?
- What happens if you ask something NOT in the manual?

**Transition:** "This works, but typing in code cells isn't user-friendly. Let's build a real interface!"

---

### MODULE 4: UI Development (30 minutes)

#### Objectives
- Install and configure Gradio
- Create chat interface
- Connect RAG to UI
- Share the interface

#### Script & Activities

**[0-5 min] Why Gradio?**

> "Gradio lets you turn your Python code into a web interface in minutes. It's perfect for demos and prototypes."

**Show Slide:** Gradio Interface Preview

**[5-15 min] Building the Interface**

**Live Coding - Cell 9:**

```python
import gradio as gr

# Create a function that wraps our RAG chain
def ask_question(question):
    if not question.strip():
        return "Please enter a question!"

    try:
        result = qa_chain({"query": question})
        answer = result['result']

        # Add sources
        sources = result['source_documents']
        source_text = "\n\n📚 Sources:\n"
        for i, doc in enumerate(sources, 1):
            page = doc.metadata.get('page', 'Unknown')
            source_text += f"  • Page {page}\n"

        return answer + source_text

    except Exception as e:
        return f"Error: {str(e)}"

# Create the interface
interface = gr.Interface(
    fn=ask_question,
    inputs=gr.Textbox(
        lines=3,
        placeholder="Ask a question about the TSI engine...",
        label="Your Question"
    ),
    outputs=gr.Textbox(
        lines=12,
        label="Answer"
    ),
    title="🚗 Automotive Technical Assistant",
    description="Ask questions about TSI Engine Technology (VAG SSP 913)",
    examples=[
        ["What is a TSI engine?"],
        ["How does the turbocharger work?"],
        ["What are the advantages of direct injection?"],
        ["Explain the engine control system"]
    ],
    theme="default"
)

# Launch it!
interface.launch(share=True)  # share=True creates a public link
```

**Ask students to run this cell**

**[15-25 min] Testing & Sharing**

**After launch:**

> "You should see a local URL (http://127.0.0.1:7860) and a PUBLIC URL (https://xxxxx.gradio.live).
>
> The public URL works for 72 hours and can be shared with anyone!"

**Student Activity:**

1. Test the interface with the example questions
2. Try their own questions
3. Share the public link with a neighbor (or in chat)
4. Test each other's systems

**Teaching Tip:** Walk around and see the interfaces. Highlight interesting questions students are asking.

**[25-30 min] Customization Challenge**

**Optional Exercise for Advanced Students:**

"Customize your interface:"
- Change the title/description
- Add more example questions
- Modify the theme
- Add a logo or emoji

**Show:** Gradio theme gallery if time permits

---

### MODULE 5: Wrap-up & Next Steps (10 minutes)

#### Objectives
- Recap what was built
- Preview Session 2
- Assign homework
- Collect feedback

#### Script & Activities

**[0-5 min] What We Built**

**Show Slide:** Architecture Diagram (full)

> "Let's recap what you built today:
> 1. ✅ Loaded a 60-page technical manual
> 2. ✅ Split it into 200+ semantic chunks
> 3. ✅ Created embeddings (for FREE locally)
> 4. ✅ Built a vector database
> 5. ✅ Connected to OpenRouter LLM
> 6. ✅ Created a public web interface
>
> This is production-grade technology. Companies pay thousands for systems like this!"

**[5-7 min] Preview Session 2**

> "Next session, we'll add:
> - **Conversation memory**: Ask follow-up questions
> - **Better prompts**: Get more accurate answers
> - **Source citations**: Show exact pages and snippets
> - **Error handling**: Make it robust
>
> By Session 4, you'll have a full production system!"

**[7-9 min] Homework (Optional but Recommended)**

**Assign:**

1. **Experiment**: Try 20 different questions, document which work well and which don't
2. **Optimize**: Adjust chunk_size and chunk_overlap, see how it affects answers
3. **Expand**: Try a different automotive PDF (find one online)
4. **Share**: Show your system to a colleague and get feedback

**Provide:** Homework worksheet template

**[9-10 min] Feedback & Questions**

**Quick Survey:**
- "Rate today's session: 👍 or 👎"
- "What was the most valuable part?"
- "What was most confusing?"

**Open Floor:** "Any questions before we finish?"

---

## Teaching Strategies

### For Different Learning Styles

**Visual Learners:**
- Use diagrams heavily (RAG flow, embedding space, architecture)
- Show code output, not just code
- Use colored text highlights in notebooks

**Auditory Learners:**
- Explain each code block verbally before running
- Encourage students to explain concepts back to you
- Use analogies and stories

**Kinesthetic Learners:**
- Maximize hands-on coding time
- Quick experiments: "Change this parameter and see what happens"
- Pair programming during exercises

### Pacing Strategies

**If Running Behind:**
- Skip some advanced explanations
- Reduce exercise time
- Pre-run time-consuming cells (embeddings)
- Skip UI customization

**If Running Ahead:**
- Add advanced exercises
- Discuss production considerations
- Explore different models on OpenRouter
- Show LangSmith for debugging

### Engagement Techniques

**Every 15 Minutes:**
- Ask a question
- Run a poll
- Do a quick check-in: "Who's with me?"
- Switch between lecture and hands-on

**Maintain Energy:**
- Celebrate small wins ("You just created embeddings!")
- Share real-world stories
- Show enthusiasm for their questions
- Use humor (automotive puns welcome!)

---

## Common Issues & Solutions

### Environment Issues

**Issue:** "I can't install langchain"
**Solution:**
```python
# In Colab, use:
!pip install -q langchain langchain-community chromadb pypdf sentence-transformers openai gradio
```

**Issue:** "PyPDF can't read the file"
**Solution:**
- Check file path (common mistake)
- Verify PDF isn't corrupted
- Try a different PDF
- In Colab: upload file using Files panel

### API Issues

**Issue:** "OpenRouter API key doesn't work"
**Solution:**
- Check for typos, extra spaces
- Verify account has credits ($5 minimum)
- Try regenerating the key
- Use instructor's backup key

**Issue:** "Rate limit exceeded"
**Solution:**
- Wait 60 seconds
- Switch to a different model
- Check if multiple students are sharing an API key (don't!)

### Embedding Issues

**Issue:** "Creating vector database is taking forever"
**Solution:**
- Normal for first time (60-90 seconds for 200 chunks)
- If >5 minutes, restart kernel
- Check CPU usage
- Reduce number of chunks for testing

**Issue:** "Vector search returns irrelevant results"
**Solution:**
- Try different queries
- Increase k (number of results)
- Check if chunks are well-formed
- May need better chunking parameters

### LLM Issues

**Issue:** "Answer is completely wrong"
**Solution:**
- Check if relevant chunks were retrieved
- Try lower temperature (more factual)
- Improve the system prompt
- Try a better model

**Issue:** "Answer says 'I don't know' when info IS in the manual"
**Solution:**
- Retrieved chunks might not be relevant
- Increase k value
- Adjust chunking strategy
- Query might need rephrasing

---

## Assessment Guidelines

### Formative Assessment (During Session)

**Checkpoints:**
- ✅ Environment setup working (Module 0)
- ✅ Successfully loaded and chunked PDF (Module 1)
- ✅ Vector database created (Module 2)
- ✅ RAG chain returns answers (Module 3)
- ✅ Gradio interface launches (Module 4)

**How to Check:**
- Ask for raised hands / thumbs up
- Monitor shared chat for issues
- Look at screens during exercises
- Check submitted exercises

### Summative Assessment (End of Session)

**Criteria for "Passed Session 1":**

| Component | Must Have | Good to Have |
|-----------|-----------|--------------|
| Code | All cells run without errors | Clean, commented code |
| RAG System | Answers 3/5 test questions correctly | Answers 5/5 correctly |
| Understanding | Can explain RAG flow | Can explain parameter choices |
| UI | Gradio interface launches | Customized interface |

**Quick Quiz (Optional):**

1. What are the 4 steps of RAG? (Prepare, Embed, Store, Retrieve+Generate)
2. Why do we chunk documents? (Context limits, relevance, cost)
3. What makes embeddings useful? (Capture semantic meaning)
4. Name one advantage of OpenRouter (Multiple models, pay-as-you-go, etc.)
5. What does temperature control? (Creativity vs. factuality)

**3 Correct = Pass**

---

## Post-Session Tasks

### Immediately After Session
- [ ] Collect feedback survey responses
- [ ] Note which topics students struggled with
- [ ] Update notebook based on issues encountered
- [ ] Share recording (if recorded)
- [ ] Post homework assignments

### Within 24 Hours
- [ ] Send recap email with key links
- [ ] Share additional resources
- [ ] Respond to follow-up questions
- [ ] Prepare for Session 2 based on feedback

### Before Next Session
- [ ] Review homework submissions
- [ ] Identify students who need extra help
- [ ] Adjust Session 2 pace based on Session 1 performance

---

## Additional Resources for Instructors

### Recommended Reading
- LangChain Documentation: https://python.langchain.com/
- OpenRouter Models: https://openrouter.ai/models
- ChromaDB Docs: https://docs.trychroma.com/

### Video References
- Explain embeddings visually: [YouTube link if available]
- RAG architecture deep dive: [Resource link]

### Community Support
- LangChain Discord: For technical issues
- OpenRouter Support: For API questions

---

## Instructor Reflection Questions

After each session, consider:

1. **Pacing:** Did we finish on time? Where did we rush/drag?
2. **Engagement:** Which parts had highest/lowest engagement?
3. **Understanding:** Which concepts needed more explanation?
4. **Technical Issues:** What broke? How can we prevent it?
5. **Success:** What % of students have a working system?

Document answers to improve future sessions!

---

## Emergency Backup Plan

**If Colab/Internet Fails:**
- Have USB drives with pre-installed environment
- Offline Jupyter notebooks ready
- Pre-run notebooks with outputs visible
- Slides that can work standalone

**If API Fails:**
- Pre-cached responses for demo queries
- Backup OpenRouter account
- Alternative: Use Ollama locally (if setup ahead)

**If Too Many Students:**
- Breakout rooms with TAs
- Pre-assign pairs
- Stagger hands-on time

---

**End of Instructor Manual - Session 1**

**Good luck! Remember: Your enthusiasm is contagious. Have fun building with your students!**
