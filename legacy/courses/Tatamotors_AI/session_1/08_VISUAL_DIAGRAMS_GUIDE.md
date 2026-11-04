# Visual Diagrams Guide for Session 1
## Teaching Aids and Visual Explanations

**Purpose:** Provide visual representations to enhance understanding
**Usage:** Display during lecture, include in slides, share with students

---

## Diagram 1: RAG System Overview

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    RAG SYSTEM ARCHITECTURE                      │
└─────────────────────────────────────────────────────────────────┘

   ┌──────────────┐
   │  PDF Manual  │  (e.g., TSI Engine Manual - 60 pages)
   └──────┬───────┘
          │
          │ 1. LOAD & PROCESS
          ▼
   ┌──────────────────┐
   │ Document Chunks  │  (200+ smaller pieces)
   │                  │
   │ Chunk 1: "The    │
   │ turbocharger..." │
   │                  │
   │ Chunk 2: "Direct │
   │ injection..."    │
   │                  │
   │ ...              │
   └──────┬───────────┘
          │
          │ 2. EMBED (Convert to numbers)
          ▼
   ┌──────────────────────────┐
   │  Vector Database         │  (ChromaDB)
   │                          │
   │  [0.23, -0.45, 0.89...] ← Chunk 1
   │  [0.12, 0.67, -0.34...] ← Chunk 2
   │  [...]                   │
   └──────────────────────────┘
                │
                │
                │ 3. QUERY TIME
                ▼
        ┌────────────────┐
        │ User Question: │
        │ "How does the  │
        │  turbo work?"  │
        └───────┬────────┘
                │
                │ Embed query
                ▼
        ┌──────────────────┐
        │ Find similar     │──► 4. RETRIEVE top 3 chunks
        │ vectors          │
        └───────┬──────────┘
                │
                │ Most relevant chunks
                ▼
        ┌──────────────────────────────┐
        │  LLM (via OpenRouter)        │
        │                              │
        │  Context: [Retrieved chunks] │
        │  Question: "How..."          │
        │                              │
        │  ▼ Generate Answer           │
        └───────┬──────────────────────┘
                │
                │ 5. RETURN ANSWER
                ▼
        ┌──────────────────────────────┐
        │ "The turbocharger increases  │
        │  engine power by using       │
        │  exhaust gases to spin..."   │
        │                              │
        │ Sources: Pages 15, 16, 23    │
        └──────────────────────────────┘
```

### Teaching Points:
- This is the complete flow from document to answer
- Steps 1-2 happen ONCE (setup)
- Steps 3-5 happen EVERY query
- Emphasize: retrieval finds context, LLM generates answer

---

## Diagram 2: Document Chunking Strategy

### Why and How We Chunk

```
┌─────────────────────────────────────────────────────────────────┐
│                  ORIGINAL PDF PAGE (Page 15)                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Section 1: Turbocharger Overview                              │
│  The turbocharger is a forced induction device...              │
│  It consists of a turbine and compressor...                    │
│  [~500 characters]                                             │
│                                                                 │
│  Section 2: Wastegate Function                                 │
│  The wastegate controls boost pressure by...                   │
│  When pressure exceeds threshold, it opens...                  │
│  [~500 characters]                                             │
│                                                                 │
│  Section 3: Maintenance Requirements                           │
│  Regular inspection of the turbocharger...                     │
│  Check for oil leaks and bearing wear...                       │
│  [~500 characters]                                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                            │
                            │ CHUNKING with size=1000, overlap=200
                            ▼
┌──────────────────────────────────────────────────────────────────┐
│                     AFTER CHUNKING                               │
└──────────────────────────────────────────────────────────────────┘

╔═══════════════════════════════════════════╗
║  CHUNK 1 (1000 chars)                     ║
║  ┌─────────────────────────────────────┐  ║
║  │ Section 1: Turbocharger Overview    │  ║
║  │ The turbocharger is a forced...     │  ║
║  │ It consists of...                   │  ║
║  │                                     │  ║
║  │ Section 2: Wastegate Function       │  ║
║  │ The wastegate controls boost... ◄─────┼─── Overlap starts
║  └─────────────────────────────────────┘  ║
╚═══════════════════════════════════════════╝

╔═══════════════════════════════════════════╗
║  CHUNK 2 (1000 chars)                     ║
║  ┌─────────────────────────────────────┐  ║
║  │ ... controls boost pressure by... ◄──┼──── 200 char overlap
║  │ When pressure exceeds threshold...  │  ║
║  │                                     │  ║
║  │ Section 3: Maintenance Requirements │  ║
║  │ Regular inspection of the...        │  ║
║  │ Check for oil leaks...              │  ║
║  └─────────────────────────────────────┘  ║
╚═══════════════════════════════════════════╝

BENEFITS:
✓ Each chunk focuses on 1-2 topics (more precise retrieval)
✓ Overlap prevents cutting sentences mid-thought
✓ Smaller chunks = better relevance matching
✓ Fits within LLM context windows
```

### Teaching Points:
- One page → multiple focused chunks
- Overlap ensures continuity
- Smaller chunks = more precise but need more chunks
- Larger chunks = more context but less precise

---

## Diagram 3: Embeddings Concept

### How Text Becomes Numbers

```
┌──────────────────────────────────────────────────────────────┐
│           FROM TEXT TO VECTORS (EMBEDDINGS)                  │
└──────────────────────────────────────────────────────────────┘

TEXT                                    EMBEDDING (384 numbers)

"turbocharger"          ──►  [0.23, -0.45, 0.89, 0.12, ...]

"supercharger"          ──►  [0.25, -0.42, 0.87, 0.15, ...]
                             ▲
                             │ VERY SIMILAR!
                             │ (Related concepts)

"engine"                ──►  [0.18, -0.22, 0.45, 0.08, ...]
                             ▲
                             │ Somewhat similar
                             │ (Same domain)

"bicycle"               ──►  [-0.67, 0.12, -0.34, 0.91, ...]
                             ▲
                             │ VERY DIFFERENT!
                             │ (Unrelated concept)


┌────────────────────────────────────────────────────────────────┐
│              2D VISUALIZATION (Simplified)                     │
│                                                                │
│    +Y                                                          │
│     │         "supercharger"                                   │
│     │              ★                                           │
│     │         "turbocharger"                                   │
│     │              ★                                           │
│     │                                                          │
│     │    "engine"                                              │
│     │       ★                                                  │
│     │                                                          │
│ ────┼────────────────────────────────────────────────── +X    │
│     │                                                          │
│     │                                                          │
│     │                                      "bicycle"           │
│     │                                          ★               │
│     │                                                          │
│    -Y                                                          │
│                                                                │
│  Similar meanings = Close together in vector space            │
│  Different meanings = Far apart                               │
└────────────────────────────────────────────────────────────────┘
```

### Teaching Points:
- Each word/phrase becomes a vector of numbers
- Similar concepts have similar numbers (close in vector space)
- This enables semantic search (meaning-based, not keyword-based)
- Actual embeddings are 384 or 768 dimensions (hard to visualize!)

---

## Diagram 4: Similarity Search Process

### Finding Relevant Chunks

```
┌───────────────────────────────────────────────────────────────┐
│              SIMILARITY SEARCH WORKFLOW                       │
└───────────────────────────────────────────────────────────────┘

STEP 1: User asks a question

    "How does the turbocharger wastegate work?"
                    │
                    │ Embed the question
                    ▼
    Query Vector: [0.24, -0.43, 0.88, ...]


STEP 2: Compare against all stored chunk vectors

    Vector Database (200 chunks):

    Chunk 1: [0.12, 0.34, -0.56, ...]  ──► Similarity: 0.85
    Chunk 2: [0.89, -0.12, 0.45, ...]  ──► Similarity: 0.42
    Chunk 3: [0.23, -0.41, 0.86, ...]  ──► Similarity: 0.93 ← BEST
    ...
    Chunk 15: [0.25, -0.44, 0.87, ...] ──► Similarity: 0.91 ← 2nd
    ...
    Chunk 87: [0.21, -0.40, 0.82, ...] ──► Similarity: 0.88 ← 3rd
    ...
    Chunk 200: [-0.67, 0.23, -0.12, ...]  ──► Similarity: 0.15


STEP 3: Return top K (e.g., K=3)

    ┌─────────────────────────────────────────────────┐
    │ Chunk 3  (Score: 0.93)                         │
    │ "The wastegate controls boost pressure by...   │
    │  diverting exhaust gases away from turbine..." │
    │ Source: Page 16                                │
    └─────────────────────────────────────────────────┘

    ┌─────────────────────────────────────────────────┐
    │ Chunk 15 (Score: 0.91)                         │
    │ "Wastegate operation: When boost exceeds...    │
    │  the actuator opens the wastegate valve..."    │
    │ Source: Page 23                                │
    └─────────────────────────────────────────────────┘

    ┌─────────────────────────────────────────────────┐
    │ Chunk 87 (Score: 0.88)                         │
    │ "Electronic wastegate control allows precise.. │
    │  boost management through ECU signals..."      │
    │ Source: Page 42                                │
    └─────────────────────────────────────────────────┘


STEP 4: Send to LLM with question

    Context: [Chunk 3 + Chunk 15 + Chunk 87]
    Question: "How does the turbocharger wastegate work?"

    ──► LLM generates comprehensive answer using all 3 chunks
```

### Teaching Points:
- Query gets embedded just like chunks
- Cosine similarity compares vectors (0-1 scale)
- Higher score = more similar = more relevant
- K parameter controls how many chunks to retrieve
- Retrieved chunks become context for LLM

---

## Diagram 5: Complete RAG Pipeline with Data Flow

### Detailed Component Interaction

```
┌──────────────────────────────────────────────────────────────────┐
│                  COMPLETE RAG PIPELINE                           │
└──────────────────────────────────────────────────────────────────┘

 OFFLINE PROCESSING (Do once)
 ═══════════════════════════════

 ┌─────────────┐
 │   PDF File  │
 │  (60 pages) │
 └──────┬──────┘
        │
        │ PyPDFLoader
        ▼
 ┌─────────────────┐
 │  Documents (60) │
 │  [Doc objects]  │
 └──────┬──────────┘
        │
        │ RecursiveCharacterTextSplitter
        │ chunk_size=1000, overlap=200
        ▼
 ┌─────────────────┐
 │  Chunks (200+)  │
 │  [Chunk objects]│
 └──────┬──────────┘
        │
        │ HuggingFaceEmbeddings
        │ model: all-MiniLM-L6-v2
        ▼
 ┌──────────────────────────────┐
 │   Vector Database (Chroma)   │
 │                              │
 │   Chunk 1 → [0.23, -0.45...] │
 │   Chunk 2 → [0.12, 0.67...]  │
 │   ...                        │
 │                              │
 │   PERSISTED TO DISK          │
 └──────────────────────────────┘
        │
        │ Load for querying
        ▼


 ONLINE QUERYING (Every request)
 ════════════════════════════════

 ┌────────────────┐
 │  User Question │
 │ "How does X?" │
 └───────┬────────┘
         │
         │ 1. Embed query
         ▼
 ┌─────────────────────┐
 │  Query Vector       │
 │  [0.24, -0.43...]   │
 └───────┬─────────────┘
         │
         │ 2. Similarity search
         ▼
 ┌──────────────────────────────┐
 │   Retriever                  │
 │   (searches ChromaDB)        │
 │                              │
 │   Find top K=3 chunks        │
 └───────┬──────────────────────┘
         │
         │ Retrieved chunks
         ▼
 ┌──────────────────────────────────┐
 │   Context Builder                │
 │                                  │
 │   Chunk 1: "text..."             │
 │   Chunk 2: "text..."             │
 │   Chunk 3: "text..."             │
 └───────┬──────────────────────────┘
         │
         │ 3. Build prompt
         ▼
 ┌────────────────────────────────────────┐
 │   Prompt Template                      │
 │                                        │
 │   "Based on this context:              │
 │    [Chunk 1]                           │
 │    [Chunk 2]                           │
 │    [Chunk 3]                           │
 │                                        │
 │    Answer this question: [Question]"  │
 └────────┬───────────────────────────────┘
          │
          │ 4. Send to LLM
          ▼
 ┌────────────────────────────────────────┐
 │   OpenRouter API                       │
 │   Model: google/gemini-flash-1.5       │
 │                                        │
 │   Processing...                        │
 │   (2-3 seconds)                        │
 └────────┬───────────────────────────────┘
          │
          │ 5. Return answer
          ▼
 ┌────────────────────────────────────────┐
 │   Generated Answer                     │
 │                                        │
 │   "The turbocharger works by..."       │
 │                                        │
 │   Sources: Pages 15, 23, 42            │
 └────────────────────────────────────────┘
          │
          │ 6. Display to user
          ▼
 ┌────────────────────────────────────────┐
 │   Gradio Interface                     │
 │                                        │
 │   [Answer displayed in text box]       │
 │   [Sources shown below]                │
 └────────────────────────────────────────┘
```

### Teaching Points:
- Clear separation: setup (once) vs. querying (every time)
- Each component has a specific job
- Data flows through the pipeline
- Errors can happen at each stage (good for troubleshooting)

---

## Diagram 6: Cost Breakdown

### Understanding Where Money Goes

```
┌────────────────────────────────────────────────────────────────┐
│                    COST ANALYSIS                               │
└────────────────────────────────────────────────────────────────┘

Component             Cost Model              Our Choice
─────────────────────────────────────────────────────────────────

PDF Loading           FREE                    PyPDF
                      ✓ No API calls
                      ✓ Local processing

Document Chunking     FREE                    LangChain splitter
                      ✓ Local processing
                      ✓ No external calls

Embeddings            FREE vs PAID            FREE (Sentence Transformers)
                      ┌──────────────┐
                      │ FREE:        │        ✓ Runs locally
                      │ Local models │        ✓ No API cost
                      │ (Our choice) │        ✓ One-time download
                      └──────────────┘

                      ┌──────────────┐
                      │ PAID:        │        ✗ Not using
                      │ OpenAI API   │        ✗ $0.0001/1K tokens
                      └──────────────┘

Vector Storage        FREE                    ChromaDB
                      ✓ Local database
                      ✓ Persists to disk
                      ✓ No hosting cost

LLM Generation        💰 PAID                 OpenRouter
                      ┌──────────────────────────────────┐
                      │ Input:  $0.075 / 1M tokens       │
                      │ Output: $0.30 / 1M tokens        │
                      │                                  │
                      │ Typical query:                   │
                      │   Question:     50 tokens        │
                      │   Context:     800 tokens        │
                      │   Answer:      150 tokens        │
                      │   ─────────────────────          │
                      │   Total: ~1000 tokens            │
                      │                                  │
                      │   Cost: ~$0.0001 per query       │
                      │   (one hundredth of a cent!)    │
                      └──────────────────────────────────┘

─────────────────────────────────────────────────────────────────

TOTAL COST PER QUERY:  ~$0.0001 (using Gemini Flash 1.5)

YOUR $5 BUDGET:        ~50,000 queries
                       (realistically, 5,000-10,000 with practice)

ENTIRE BOOTCAMP:       ~$1-2 if you're careful
                       ~$3-5 with lots of experimentation
```

### Teaching Points:
- Only LLM costs money!
- Everything else is FREE
- Smart design keeps costs ultra-low
- Could use free LLMs too (lower quality)

---

## Diagram 7: Chunk Size Trade-offs

### Visual Comparison

```
┌────────────────────────────────────────────────────────────────┐
│            CHUNK SIZE COMPARISON                               │
└────────────────────────────────────────────────────────────────┘

SMALL CHUNKS (500 chars)
═════════════════════════
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│ Chunk 1  │ │ Chunk 2  │ │ Chunk 3  │ │ Chunk 4  │
│ Topic: A │ │ Topic: B │ │ Topic: C │ │ Topic: D │
│ (500chr) │ │ (500chr) │ │ (500chr) │ │ (500chr) │
└──────────┘ └──────────┘ └──────────┘ └──────────┘

PROS:                           CONS:
✓ Very precise retrieval        ✗ More chunks to search
✓ Focused on single topic       ✗ May lose context
✓ Lower token cost per chunk    ✗ Sentences may be cut
                                ✗ Need higher K value


MEDIUM CHUNKS (1000 chars) ← OUR CHOICE
══════════════════════════════
┌─────────────────────┐ ┌─────────────────────┐
│     Chunk 1         │ │     Chunk 2         │
│  Topic: A + B       │ │  Topic: C + D       │
│    (1000 chars)     │ │    (1000 chars)     │
└─────────────────────┘ └─────────────────────┘

PROS:                           CONS:
✓ Good precision               ✗ May include some irrelevant
✓ Maintains context            ✗ Medium token cost
✓ Complete thoughts
✓ Balanced performance

SWEET SPOT for most use cases! ★


LARGE CHUNKS (2000 chars)
═════════════════════════
┌─────────────────────────────────────────┐
│           Chunk 1                       │
│  Topic: A + B + C + D + E               │
│         (2000 chars)                    │
└─────────────────────────────────────────┘

PROS:                           CONS:
✓ Maximum context              ✗ Less precise retrieval
✓ Fewer total chunks           ✗ Higher token cost
✓ Related info together        ✗ Multiple topics per chunk
                               ✗ Slower processing


┌────────────────────────────────────────────────────────────────┐
│                    RETRIEVAL COMPARISON                        │
└────────────────────────────────────────────────────────────────┘

Query: "How does turbocharger work?"

Small (500):  ┌──────────┐              High precision
              │ turbo ★  │ ← Perfect!   Narrow focus
              └──────────┘              May miss related info

Medium (1000): ┌─────────────────────┐  Good precision
               │ turbo + wastegate ★ │  Good context
               └─────────────────────┘  BALANCED ★

Large (2000):  ┌─────────────────────────────────────────┐
               │ turbo + wastegate + cooling + sensors ★ │
               └─────────────────────────────────────────┘
               Lower precision, but comprehensive context
```

### Teaching Points:
- No "perfect" chunk size - it's a trade-off
- 1000 is a good starting point
- Technical docs: smaller chunks (500-800)
- Narrative docs: larger chunks (1500-2000)
- Experiment and measure quality!

---

## Diagram 8: Gradio Interface Architecture

### How the UI Works

```
┌────────────────────────────────────────────────────────────────┐
│                  GRADIO INTERFACE FLOW                         │
└────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────┐
  │              BROWSER (User's View)                      │
  │                                                         │
  │  ┌───────────────────────────────────────────────────┐ │
  │  │  🚗 Automotive Technical Assistant                │ │
  │  ├───────────────────────────────────────────────────┤ │
  │  │                                                   │ │
  │  │  Your Question:                                   │ │
  │  │  ┌─────────────────────────────────────────────┐ │ │
  │  │  │ How does the turbocharger work?             │ │ │
  │  │  └─────────────────────────────────────────────┘ │ │
  │  │                                  [ Submit ]       │ │
  │  │                                                   │ │
  │  │  Answer:                                          │ │
  │  │  ┌─────────────────────────────────────────────┐ │ │
  │  │  │ The turbocharger increases engine power by  │ │ │
  │  │  │ using exhaust gases to spin a turbine...    │ │ │
  │  │  │                                              │ │ │
  │  │  │ Sources: Pages 15, 23, 42                   │ │ │
  │  │  └─────────────────────────────────────────────┘ │ │
  │  │                                                   │ │
  │  └───────────────────────────────────────────────────┘ │
  └─────────────────────────────────────────────────────────┘
                        │  HTTP Request
                        ▼
  ┌─────────────────────────────────────────────────────────┐
  │          GRADIO SERVER (Python Backend)                 │
  │                                                         │
  │  def ask_question(question):                            │
  │      │                                                  │
  │      │ 1. Validate input                                │
  │      ▼                                                  │
  │  ┌──────────────────┐                                   │
  │  │ Input validation │                                   │
  │  │ - Not empty?     │                                   │
  │  │ - Length OK?     │                                   │
  │  └────────┬─────────┘                                   │
  │           │                                             │
  │           │ 2. Call RAG chain                            │
  │           ▼                                             │
  │  ┌──────────────────────┐                               │
  │  │ qa_chain({"query":   │                               │
  │  │    question})        │ ──► Triggers entire RAG       │
  │  └────────┬─────────────┘     pipeline                  │
  │           │                                             │
  │           │ 3. Format response                           │
  │           ▼                                             │
  │  ┌──────────────────────┐                               │
  │  │ answer + sources     │                               │
  │  │ formatting           │                               │
  │  └────────┬─────────────┘                               │
  │           │                                             │
  │           │ 4. Return to user                            │
  │           ▼                                             │
  │      return formatted_response                          │
  │                                                         │
  └─────────────────────────────────────────────────────────┘
                        │  HTTP Response
                        ▼
                  [Back to Browser]


KEY FEATURES:
═════════════

┌─────────────────────────────────────────────────────────────┐
│ share=True  → Creates public URL (https://xxxxx.gradio.live)│
│ share=False → Local only (http://127.0.0.1:7860)            │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Components:                                                 │
│ • gr.Textbox() → Input/output fields                       │
│ • gr.Interface() → Wraps everything together               │
│ • examples=[] → Pre-filled questions                       │
│ • title, description → Customization                       │
└─────────────────────────────────────────────────────────────┘
```

### Teaching Points:
- Gradio handles all web server complexity
- We just provide a Python function
- Automatic UI generation
- Share link makes it instantly accessible

---

## Instructions for Creating Slides

### Recommended Tools:
- **PowerPoint/Keynote:** Manual recreation with shapes
- **Google Slides:** Free, collaborative
- **Mermaid.js:** Code-based diagrams
- **Draw.io:** Free diagramming tool
- **Excalidraw:** Hand-drawn style

### Color Scheme Suggestions:
- **Background:** White or light gray
- **Components:** Blue (#4A90E2)
- **Data Flow:** Green arrows (#7ED321)
- **Important Items:** Orange/Red (#F5A623)
- **Text:** Dark gray (#4A4A4A)

### Animation Suggestions:
1. **Diagram 1 (RAG Overview):** Animate flow from top to bottom
2. **Diagram 4 (Similarity Search):** Highlight each step sequentially
3. **Diagram 5 (Complete Pipeline):** Fade in offline, then online sections

---

## Usage Tips for Instructors

### When to Show Each Diagram:

**Module 0 (Introduction):**
- Diagram 1: RAG System Overview
- Diagram 6: Cost Breakdown

**Module 1 (Document Processing):**
- Diagram 2: Document Chunking Strategy
- Diagram 7: Chunk Size Trade-offs

**Module 2 (Embeddings & Vector DB):**
- Diagram 3: Embeddings Concept
- Diagram 4: Similarity Search Process

**Module 3 (LLM Integration):**
- Diagram 5: Complete RAG Pipeline

**Module 4 (UI Development):**
- Diagram 8: Gradio Interface Architecture

### Engagement Tactics:
- Print diagrams on handouts
- Draw on whiteboard alongside showing slides
- Ask students to explain diagram back to you
- Use diagrams for troubleshooting ("which component failed?")

---

**End of Visual Diagrams Guide**

These diagrams are teaching tools - adapt them to your teaching style!
