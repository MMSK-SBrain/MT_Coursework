# Course Structure: Multimodal RAG Bootcamp (MRAG)

## Course Outcomes (COs)

| ID | Code | Description | Category | Bloom |
|----|------|-------------|----------|-------|
| co-1 | MRAG-CO-1 | Build a functional Multimodal RAG application that retrieves and reasons over text, images, and tables | Skill | Create |
| co-2 | MRAG-CO-2 | Evaluate RAG pipeline output quality and apply debugging strategies to improve retrieval accuracy | Skill | Evaluate |

---

## Module 1: RAG Foundations (45 min) — Day 1

**Module Outcome:**
| ID | Code | Description | Category | Bloom |
|----|------|-------------|----------|-------|
| mo-1-1 | MRAG-MO-1-1 | Explain the RAG architecture and articulate why multimodal retrieval is necessary for real-world AI applications | Knowledge | Understand |

### Lesson 1.1: What is RAG & Why Multimodal? (45 min)

| SO ID | Code | Description | Category | Bloom | Session |
|-------|------|-------------|----------|-------|---------|
| so-1-1-1 | MRAG-SO-1-1-1 | Describe the limitations of standalone LLMs (hallucination, knowledge cutoff) that RAG addresses | Knowledge | Understand | lecture |
| so-1-1-2 | MRAG-SO-1-1-2 | Diagram the core RAG pipeline: Ingest → Embed → Store → Retrieve → Generate | Knowledge | Understand | lecture |
| so-1-1-3 | MRAG-SO-1-1-3 | Identify real-world use cases requiring multimodal retrieval (documents with images, tables, diagrams) | Knowledge | Understand | mixed |
| so-1-1-4 | MRAG-SO-1-1-4 | Set up the development environment (Colab notebook, install dependencies, verify API access) | Skill | Apply | lab |

---

## Module 2: Data Ingestion & Embedding (60 min) — Day 1

**Module Outcomes:**
| ID | Code | Description | Category | Bloom |
|----|------|-------------|----------|-------|
| mo-2-1 | MRAG-MO-2-1 | Parse multimodal documents into structured chunks suitable for embedding | Skill | Apply |
| mo-2-2 | MRAG-MO-2-2 | Generate vector embeddings for text, image, and table content using appropriate models | Skill | Apply |

### Lesson 2.1: Document Parsing & Chunking (30 min)

| SO ID | Code | Description | Category | Bloom | Session |
|-------|------|-------------|----------|-------|---------|
| so-2-1-1 | MRAG-SO-2-1-1 | Load and parse PDF documents containing text, images, and tables using Unstructured.io | Skill | Apply | lab |
| so-2-1-2 | MRAG-SO-2-1-2 | Apply chunking strategies (recursive text splitting, element-aware chunking) to parsed content | Skill | Apply | lab |
| so-2-1-3 | MRAG-SO-2-1-3 | Inspect and validate parsed output to confirm text, images, and tables are correctly extracted | Skill | Analyze | lab |

### Lesson 2.2: Multimodal Embeddings (30 min)

| SO ID | Code | Description | Category | Bloom | Session |
|-------|------|-------------|----------|-------|---------|
| so-2-2-1 | MRAG-SO-2-2-1 | Explain how embedding models convert text and images into vector representations | Knowledge | Understand | lecture |
| so-2-2-2 | MRAG-SO-2-2-2 | Generate embeddings for text chunks using OpenAI or open-source embedding models | Skill | Apply | lab |
| so-2-2-3 | MRAG-SO-2-2-3 | Generate embeddings for images using multimodal embedding models (CLIP or GPT-4V summaries) | Skill | Apply | lab |
| so-2-2-4 | MRAG-SO-2-2-4 | Summarize tables into text descriptions and embed them for retrieval | Skill | Apply | lab |

---

## Module 3: Vector Store & Retrieval (45 min) — Day 1

**Module Outcomes:**
| ID | Code | Description | Category | Bloom |
|----|------|-------------|----------|-------|
| mo-3-1 | MRAG-MO-3-1 | Build and populate a ChromaDB vector store with multimodal embeddings | Skill | Apply |
| mo-3-2 | MRAG-MO-3-2 | Execute similarity searches and analyze retrieval results across modalities | Skill | Analyze |

### Lesson 3.1: Building the Vector Store (20 min)

| SO ID | Code | Description | Category | Bloom | Session |
|-------|------|-------------|----------|-------|---------|
| so-3-1-1 | MRAG-SO-3-1-1 | Initialize a ChromaDB collection with appropriate distance metrics for multimodal data | Skill | Apply | lab |
| so-3-1-2 | MRAG-SO-3-1-2 | Index text, image, and table embeddings into the vector store with metadata | Skill | Apply | lab |

### Lesson 3.2: Retrieval & Search (25 min)

| SO ID | Code | Description | Category | Bloom | Session |
|-------|------|-------------|----------|-------|---------|
| so-3-2-1 | MRAG-SO-3-2-1 | Perform similarity search queries and interpret relevance scores | Skill | Apply | lab |
| so-3-2-2 | MRAG-SO-3-2-2 | Compare retrieval results across text-only vs multimodal queries | Skill | Analyze | lab |
| so-3-2-3 | MRAG-SO-3-2-3 | Apply metadata filtering to improve retrieval precision | Skill | Apply | lab |

---

## Module 4: RAG Pipeline Assembly (60 min) — Day 1

**Module Outcomes:**
| ID | Code | Description | Category | Bloom |
|----|------|-------------|----------|-------|
| mo-4-1 | MRAG-MO-4-1 | Construct a complete RAG chain using LangChain that integrates retrieval with LLM generation | Skill | Create |
| mo-4-2 | MRAG-MO-4-2 | Design effective prompts that incorporate retrieved multimodal context for accurate generation | Skill | Create |

### Lesson 4.1: Connecting Retrieval to Generation (30 min)

| SO ID | Code | Description | Category | Bloom | Session |
|-------|------|-------------|----------|-------|---------|
| so-4-1-1 | MRAG-SO-4-1-1 | Build a LangChain retrieval chain connecting ChromaDB retriever to an LLM | Skill | Apply | lab |
| so-4-1-2 | MRAG-SO-4-1-2 | Write prompt templates that inject retrieved text, image descriptions, and table data as context | Skill | Create | lab |
| so-4-1-3 | MRAG-SO-4-1-3 | Test the pipeline with sample questions and verify grounded answers | Skill | Analyze | lab |

### Lesson 4.2: Capstone — Build Your RAG App (30 min)

| SO ID | Code | Description | Category | Bloom | Session |
|-------|------|-------------|----------|-------|---------|
| so-4-2-1 | MRAG-SO-4-2-1 | Assemble a complete end-to-end Multimodal RAG application using instructor-provided sample documents | Skill | Create | practical |
| so-4-2-2 | MRAG-SO-4-2-2 | Query the application with diverse questions requiring text, image, and table retrieval | Skill | Apply | practical |
| so-4-2-3 | MRAG-SO-4-2-3 | Present the working application and demonstrate a successful multimodal query-answer pair | Skill | Apply | practical |

---

## Module 5: Evaluation & Next Steps (30 min) — Day 1

**Module Outcome:**
| ID | Code | Description | Category | Bloom |
|----|------|-------------|----------|-------|
| mo-5-1 | MRAG-MO-5-1 | Evaluate RAG output quality and identify strategies for improvement | Skill | Evaluate |

### Lesson 5.1: RAG Quality & Debugging (20 min)

| SO ID | Code | Description | Category | Bloom | Session |
|-------|------|-------------|----------|-------|---------|
| so-5-1-1 | MRAG-SO-5-1-1 | Identify common RAG failure modes (irrelevant retrieval, context overflow, hallucination despite context) | Knowledge | Analyze | lecture |
| so-5-1-2 | MRAG-SO-5-1-2 | Apply basic evaluation techniques (relevance scoring, answer faithfulness checks) to RAG output | Skill | Evaluate | lab |
| so-5-1-3 | MRAG-SO-5-1-3 | List concrete next steps for advancing their RAG skills (hybrid search, reranking, production deployment) | Knowledge | Remember | lecture |

---

## Schedule Overview

| Time | Module | Focus | Format |
|------|--------|-------|--------|
| 0:00–0:45 | Module 1: RAG Foundations | Concepts + environment setup | 60% lecture / 40% lab |
| 0:45–1:45 | Module 2: Data Ingestion & Embedding | Parse docs, chunk, embed | 20% lecture / 80% lab |
| 1:45–2:00 | **Break** | | |
| 2:00–2:45 | Module 3: Vector Store & Retrieval | ChromaDB, search, filter | 10% lecture / 90% lab |
| 2:45–3:45 | Module 4: RAG Pipeline Assembly | LangChain + capstone build | 10% lecture / 90% lab |
| 3:45–4:15 | Module 5: Evaluation & Wrap-up | Debug, evaluate, next steps | 50% lecture / 50% lab |
