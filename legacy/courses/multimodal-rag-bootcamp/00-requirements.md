# Course Requirements: Multimodal RAG Bootcamp

**Created:** 2026-03-12
**Status:** Complete

## 1. Course Context
- **Topic:** Building Multimodal Retrieval-Augmented Generation (RAG) Applications
- **Industry/Domain:** AI / Technology Education
- **Duration:** 1 Day (4 hours)
- **Description:** A hands-on bootcamp where learners build a working Multimodal RAG application from scratch, progressing from foundational concepts to a functional prototype that retrieves and reasons over text, images, and tables.

## 2. Target Audience
- **Primary Learners:** Students / early-career developers with basic AI awareness
- **Experience Level:** Beginner-Intermediate
- **Prerequisites:**
  - Basic Python proficiency (can write functions, use pip, run notebooks)
  - Familiarity with what LLMs are (ChatGPT-level awareness)
  - Laptop with internet access
- **Job Role:** Aspiring AI/ML engineers, data scientists, software developers adding AI skills

## 3. Learning Outcomes
### What learners will DO:
1. Explain how RAG works and why it solves LLM hallucination problems
2. Convert text, images, and tables into vector embeddings
3. Build and query a vector store with multimodal data
4. Construct a complete Multimodal RAG pipeline using LangChain
5. Evaluate and debug RAG output quality

### Critical Skills:
- Embedding multimodal content (text + images + tables)
- Building a retrieval pipeline with a vector database
- Integrating retrieval with an LLM for generation
- Prompt engineering for RAG context injection

### Nice-to-have:
- Deploying a RAG app with a simple UI (Gradio/Streamlit)
- Advanced chunking strategies
- Hybrid search (keyword + semantic)

## 4. Content Structure
### Main Modules:
1. **Foundations** (45 min) — What is RAG, why multimodal, architecture overview
2. **Data Ingestion & Embedding** (60 min) — Loading docs/images/tables, chunking, embedding
3. **Vector Store & Retrieval** (45 min) — ChromaDB setup, indexing, similarity search
4. **RAG Pipeline Assembly** (60 min) — LangChain integration, prompt templates, generation
5. **Evaluation & Wrap-up** (30 min) — Testing quality, debugging, next steps

### Sequencing:
- Linear progression: concepts → data prep → storage → retrieval → generation → evaluation
- Each module builds directly on the previous one

### Theory/Practice Ratio:
- 30% theory / 70% hands-on coding (in Jupyter/Colab notebooks)

## 5. Assessment
- **Types:**
  - Live coding checkpoints at end of each module (formative)
  - Final working RAG app as capstone deliverable (summative)
- **Passing Criteria:** Learner has a functional RAG pipeline that answers questions using multimodal source data

## 6. Constraints
- **Equipment:** Laptops with internet, Google Colab (no local GPU needed)
- **Tools:** Python, LangChain, ChromaDB, OpenAI API (or Claude API), Unstructured.io for doc parsing
- **Safety:** API key management — keys provided for session, revoked after
- **Budget:** Free-tier or instructor-provided API credits
