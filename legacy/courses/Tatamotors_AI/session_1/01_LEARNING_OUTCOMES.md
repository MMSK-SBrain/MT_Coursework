# Session 1: Foundation - Simple RAG with Single PDF
## Learning Outcomes

### Course Level Outcomes (CLO)
By the end of Session 1, students will be able to build and deploy a basic Retrieval Augmented Generation (RAG) system for automotive technical documentation.

---

## Module Level Outcomes (MLO)

### MLO 1: Conceptual Understanding of RAG Systems
**Students will understand the architecture and purpose of RAG systems in automotive technical assistance**

**Sub-Outcomes (SO):**
- SO 1.1: Explain what RAG is and why it's needed for domain-specific AI applications
- SO 1.2: Identify the three core components of a RAG system (Document Processing, Vector Storage, LLM Integration)
- SO 1.3: Describe the flow of information from user query to AI-generated response
- SO 1.4: Compare RAG vs. fine-tuning vs. base LLM approaches for technical documentation

**Assessment:**
- Quick quiz on RAG architecture
- Verbal explanation of the RAG workflow
- Diagram labeling exercise

---

### MLO 2: Document Processing & Chunking
**Students will process PDF documents and split them into meaningful chunks for embedding**

**Sub-Outcomes (SO):**
- SO 2.1: Load PDF documents using PyPDFLoader
- SO 2.2: Implement text splitting using RecursiveCharacterTextSplitter
- SO 2.3: Configure chunk size and overlap parameters based on document type
- SO 2.4: Inspect and validate chunk quality for automotive technical content
- SO 2.5: Understand the trade-offs between chunk size, overlap, and retrieval accuracy

**Assessment:**
- Successfully load and chunk the TSI Engine SSP manual
- Demonstrate chunk inspection and identify optimal chunk containing specific technical information
- Code exercise: adjust chunking parameters and observe effects

---

### MLO 3: Embeddings & Vector Storage
**Students will create embeddings and build a vector database for semantic search**

**Sub-Outcomes (SO):**
- SO 3.1: Understand what embeddings are and how they represent semantic meaning
- SO 3.2: Implement local embedding generation using Sentence Transformers
- SO 3.3: Create and persist a ChromaDB vector store
- SO 3.4: Perform similarity search to retrieve relevant document chunks
- SO 3.5: Evaluate retrieval quality and relevance of returned chunks

**Assessment:**
- Build a working vector database from automotive documentation
- Execute similarity searches with various automotive queries
- Compare retrieval results for well-formed vs. poorly-formed queries

---

### MLO 4: LLM Integration with OpenRouter
**Students will integrate OpenRouter API to generate contextual responses**

**Sub-Outcomes (SO):**
- SO 4.1: Set up OpenRouter API authentication
- SO 4.2: Configure ChatOpenAI with OpenRouter endpoint
- SO 4.3: Select appropriate models for different use cases (cost vs. quality)
- SO 4.4: Build a RetrievalQA chain connecting retriever and LLM
- SO 4.5: Test the complete RAG pipeline with automotive technical queries

**Assessment:**
- Successfully authenticate with OpenRouter API
- Create functional RAG chain that answers questions from TSI manual
- Compare responses from different model configurations

---

### MLO 5: Basic UI Development
**Students will create an interactive interface for their RAG system**

**Sub-Outcomes (SO):**
- SO 5.1: Install and configure Gradio for rapid UI development
- SO 5.2: Create a text input/output interface
- SO 5.3: Connect the RAG chain to the UI
- SO 5.4: Test the interface with real automotive technical questions
- SO 5.5: Share the interface locally or via public link

**Assessment:**
- Build and launch a working Gradio interface
- Successfully answer at least 5 different automotive technical questions
- Demonstrate the interface to peers or instructor

---

## Competency Levels

### Knowledge (Remembering & Understanding)
- Define RAG and its components
- Explain the purpose of embeddings
- Describe the role of vector databases
- Understand chunk size trade-offs

### Skills (Applying & Analyzing)
- Load and process PDF documents
- Create embeddings and vector stores
- Configure API connections
- Perform similarity searches
- Analyze retrieval quality

### Application (Evaluating & Creating)
- Build a complete RAG system from scratch
- Evaluate and optimize chunking parameters
- Select appropriate models for use cases
- Create an interactive UI
- Troubleshoot common errors

---

## Success Criteria

By the end of Session 1, each student will have:

✅ **Functional RAG System**
- Working code that loads, processes, and embeds automotive PDFs
- ChromaDB vector store with persisted embeddings
- OpenRouter API integration with functional LLM calls
- Complete RetrievalQA chain

✅ **Interactive Interface**
- Gradio UI accepting automotive technical questions
- Response generation with context from TSI Engine manual
- Ability to share the interface link

✅ **Technical Understanding**
- Can explain RAG architecture to a peer
- Can identify which component handles each step of the pipeline
- Understands cost implications of different design choices

✅ **Practical Skills**
- Can modify chunk size and observe effects
- Can test different queries and evaluate results
- Can troubleshoot common errors (API keys, dependencies, etc.)

---

## Time Allocation

| Module | Duration | Focus |
|--------|----------|-------|
| Introduction & RAG Concepts | 20 min | MLO 1 |
| Document Processing | 30 min | MLO 2 |
| Embeddings & Vector Store | 40 min | MLO 3 |
| LLM Integration | 30 min | MLO 4 |
| UI Development | 30 min | MLO 5 |
| Q&A & Troubleshooting | 20 min | All MLOs |
| **Total** | **170 min (2h 50m)** | |

---

## Prerequisites

Students should have:
- Basic Python programming knowledge (variables, functions, loops)
- Familiarity with pip and package installation
- Understanding of APIs (REST basics)
- Google account (for Colab) OR local Python environment
- Basic understanding of automotive systems (helpful but not required)

---

## Materials Required

**Software:**
- Python 3.8+ environment or Google Colab
- OpenRouter API account with $5 credit

**Documents:**
- VAG SSP 913 - TSI Engine Technology (PDF)

**Libraries:**
- langchain
- langchain-community
- chromadb
- pypdf
- sentence-transformers
- openai
- gradio

---

## Post-Session Outcomes

After completing Session 1, students will be ready to:
- Add conversation memory (Session 2)
- Work with multiple document types (Session 3)
- Deploy to production environments (Session 4)
- Extend the system with custom features
- Apply RAG to other automotive documentation sets
