"""
SESSION 1: Building Your First RAG System for Automotive Technical Documentation
================================================================================

Welcome to the RAG Bootcamp! 🚗

In this session, you'll build an AI-powered technical assistant that can:
- Read automotive manuals (PDFs)
- Answer technical questions
- Cite its sources

By the end, you'll have a working chatbot with a web interface!

Let's get started!
"""

# ============================================================================
# CELL 1: Setup & Installation
# ============================================================================
"""
First, we need to install all the required libraries.
This will take about 1-2 minutes.

Run this cell and wait for the ✅ message!
"""

# Install required packages
!pip install -q langchain langchain-community chromadb pypdf sentence-transformers openai gradio

print("✅ All packages installed successfully!")
print("\nNow let's import them and make sure everything works...")

# Import all required libraries
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import gradio as gr
import os
from getpass import getpass
import warnings
warnings.filterwarnings('ignore')

print("✅ All imports successful! You're ready to start building.")

# ============================================================================
# CELL 2: Understanding RAG - The Big Picture
# ============================================================================
"""
🤔 What is RAG?

RAG stands for: Retrieval Augmented Generation

Think of it like this:
1. You have a huge library of books (automotive manuals)
2. Someone asks you a question
3. Instead of reading ALL the books, you quickly find the relevant pages
4. You read just those pages and answer the question

That's exactly what RAG does!

📊 The 4 Steps:
1. PREPARE: Load documents and break them into chunks
2. EMBED: Convert chunks into numbers (vectors) that capture meaning
3. STORE: Save these vectors in a searchable database
4. RETRIEVE & GENERATE: Find relevant chunks, send to AI to generate answer

Let's build each step!
"""

# ============================================================================
# CELL 3: Step 1 - Load the PDF Document
# ============================================================================
"""
📄 Loading the TSI Engine Manual

We're using the Volkswagen SSP 913 manual about TSI engine technology.
It's about 60 pages of technical information.

⚠️ IMPORTANT: Make sure you have the PDF file!
- If using Google Colab: Upload the file using the Files panel on the left
- If running locally: Make sure the PDF is in the same folder as this notebook

The PDF can be downloaded from: [Instructor will provide link]
"""

# Upload your PDF file
# In Colab, you can use this code to upload:
from google.colab import files
uploaded = files.upload()
pdf_filename = list(uploaded.keys())[0]  # Get the uploaded filename

# OR if you already have the file, specify the path:
# pdf_filename = "vag_ssp_913_tsi_engine.pdf"

# Load the PDF
print("📖 Loading PDF document...")
loader = PyPDFLoader(pdf_filename)
documents = loader.load()

print(f"✅ Success! Loaded {len(documents)} pages")
print(f"\n📄 First page preview (first 500 characters):")
print("="*70)
print(documents[0].page_content[:500])
print("="*70)

# Let's check metadata
print(f"\n📋 Metadata available: {documents[0].metadata}")

"""
👀 What just happened?

PyPDFLoader read the PDF and converted each page into a Document object.
Each Document has:
- page_content: The actual text
- metadata: Information like page number, source file, etc.

Next, we need to break these pages into smaller chunks!
"""

# ============================================================================
# CELL 4: Step 2 - Split Documents into Chunks
# ============================================================================
"""
✂️ Why Do We Need Chunks?

Problem: A single page might talk about 5 different topics.
If we search for "turbocharger", we might get a whole page that mentions
it once but is mostly about something else.

Solution: Break pages into smaller, focused chunks (500-1500 characters each).
This way, each chunk is about ONE specific topic.

🎯 Chunking Strategy:
- chunk_size = 1000: About 250 words per chunk
- chunk_overlap = 200: Chunks overlap to prevent cutting sentences in half
- separators: Split on paragraphs first, then sentences, then words
"""

# Create the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,        # Characters per chunk
    chunk_overlap=200,      # Overlap between chunks
    length_function=len,
    separators=["\n\n", "\n", ". ", " ", ""]  # Try these in order
)

# Split all pages into chunks
print("✂️ Splitting documents into chunks...")
chunks = text_splitter.split_documents(documents)

print(f"✅ Done! Split {len(documents)} pages into {len(chunks)} chunks")
print(f"📊 That's about {len(chunks)/len(documents):.1f} chunks per page")

# Let's look at a sample chunk
print(f"\n📝 Sample chunk #{10}:")
print("="*70)
print(chunks[10].page_content)
print("="*70)
print(f"Chunk length: {len(chunks[10].page_content)} characters")
print(f"From page: {chunks[10].metadata.get('page', 'Unknown')}")

"""
🎓 QUICK EXERCISE #1:

Try to find a chunk that talks about "turbocharger"
Hint: Loop through chunks and check if "turbocharger" is in the text

Uncomment and complete this code:
"""

# for i, chunk in enumerate(chunks):
#     if "turbocharger" in chunk.page_content.lower():
#         print(f"Found in chunk {i} (page {chunk.metadata.get('page')}):")
#         print(chunk.page_content)
#         break

# ============================================================================
# CELL 5: Step 3 - Create Embeddings (Turn Text into Numbers)
# ============================================================================
"""
🔢 What Are Embeddings?

Embeddings convert text into vectors (lists of numbers) that capture MEANING.

Example:
- "turbocharger" → [0.23, -0.45, 0.89, ...]
- "supercharger" → [0.25, -0.42, 0.87, ...]  ← Similar numbers!
- "bicycle"      → [-0.67, 0.12, -0.34, ...] ← Very different!

Similar meanings = Similar numbers

💡 Why This Matters:
Instead of searching for exact word matches, we search for similar MEANINGS.
So "How does the turbo work?" will find chunks about "turbocharger function"
even though the words are different!

💰 Cost: We're using FREE local embeddings (Sentence Transformers)
No API calls, no cost, runs on your computer!
"""

# Load the embedding model
print("🔧 Loading embedding model (this takes ~30 seconds first time)...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'},  # Use CPU (works everywhere)
    encode_kwargs={'normalize_embeddings': True}
)

print("✅ Embedding model loaded!")

# Let's test it - embed a sample question
test_question = "How does the turbocharger work?"
test_embedding = embeddings.embed_query(test_question)

print(f"\n🔬 Test: Embedding the question: '{test_question}'")
print(f"📊 Result: A vector of {len(test_embedding)} numbers")
print(f"📍 First 10 numbers: {test_embedding[:10]}")

"""
Each chunk will become a similar vector.
When you ask a question, we:
1. Convert your question to a vector
2. Find chunks with similar vectors
3. Those are the most relevant chunks!
"""

# ============================================================================
# CELL 6: Step 4 - Build the Vector Database
# ============================================================================
"""
🗄️ Creating the Vector Database

ChromaDB will:
1. Take each chunk
2. Convert it to an embedding (using the model we just loaded)
3. Store it in a searchable database

⏱️ This takes 1-2 minutes for ~200 chunks.

Why? We're creating embeddings for ALL chunks.
Good news: We only do this ONCE. After it's saved, we can reload instantly!
"""

# Create the vector database
print("🏗️ Building vector database...")
print("⏳ This will take 1-2 minutes - perfect time for a coffee break! ☕")
print("(You'll see a progress indicator)")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"  # Save to disk so we can reuse it
)

print(f"✅ Vector database created!")
print(f"📊 Stored {vectorstore._collection.count()} chunks")
print(f"💾 Saved to: ./chroma_db")

"""
🎉 Congratulations! You now have a searchable knowledge base!

Let's test it with similarity search...
"""

# ============================================================================
# CELL 7: Test Similarity Search - The Magic Moment!
# ============================================================================
"""
🔍 Similarity Search - Finding Relevant Information

Now we can ask questions and find the most relevant chunks!

This is the "Retrieval" part of RAG.
"""

# Test query
query = "How does the turbocharger work?"

print(f"❓ Question: {query}")
print("\n🔍 Searching through {vectorstore._collection.count()} chunks...")

# Find the top 3 most similar chunks
similar_docs = vectorstore.similarity_search(query, k=3)

print(f"✅ Found {len(similar_docs)} relevant chunks!\n")
print("="*70)

# Display results
for i, doc in enumerate(similar_docs, 1):
    print(f"\n📄 RESULT #{i}")
    print(f"📍 Page: {doc.metadata.get('page', 'Unknown')}")
    print(f"📝 Content Preview:")
    print("-"*70)
    print(doc.page_content[:300] + "...")
    print("="*70)

"""
🎓 EXERCISE #2: Try Your Own Questions!

Modify the 'query' variable above and run this cell again.

Try these questions:
1. "What is the compression ratio?"
2. "Explain direct fuel injection"
3. "What are the main engine components?"
4. "How is the engine controlled?"

Notice: Even without exact word matches, it finds relevant information!
"""

# Try your own question here:
# your_query = "Your question here"
# results = vectorstore.similarity_search(your_query, k=3)
# for i, doc in enumerate(results, 1):
#     print(f"\nResult {i}:\n{doc.page_content}\n")

# ============================================================================
# CELL 8: Step 5 - Connect to OpenRouter (LLM)
# ============================================================================
"""
🤖 Adding the AI Brain

So far we can FIND relevant chunks. Now we need an AI to:
1. Read those chunks
2. Understand the question
3. Generate a natural, accurate answer

We're using OpenRouter to access powerful LLMs cheaply!

🔑 You'll need your OpenRouter API key:
1. Go to: https://openrouter.ai/
2. Sign up (free)
3. Add $5 credits (enough for hundreds of queries)
4. Copy your API key

⚠️ SECURITY: Never share your API key publicly!
"""

# Secure API key input
if 'OPENROUTER_API_KEY' not in os.environ:
    print("🔑 Please enter your OpenRouter API key:")
    print("(It won't be displayed for security)")
    os.environ['OPENROUTER_API_KEY'] = getpass("API Key: ")

print("✅ API key saved securely!")

# Configure the LLM
llm = ChatOpenAI(
    model_name="google/gemini-flash-1.5",  # Fast and cheap!
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=os.environ['OPENROUTER_API_KEY'],
    temperature=0.1,  # Low = more factual, High = more creative
    max_tokens=500    # Limit response length (saves cost)
)

# Test the LLM connection
print("\n🧪 Testing LLM connection...")
test_response = llm.predict("Say 'Hello! I am ready to answer automotive questions!'")
print(f"🤖 LLM Response: {test_response}")

"""
✅ If you see a response above, your LLM is connected!

💰 Cost Check:
- This test query: ~$0.0001 (one hundredth of a cent)
- Typical RAG query: ~$0.001 (one tenth of a cent)
- Your $5 credit: ~5,000 queries!
"""

# ============================================================================
# CELL 9: Build the Complete RAG Chain
# ============================================================================
"""
🔗 Connecting Everything: The Complete RAG Pipeline

Now we connect all the pieces:

Question → Embed → Search Vectors → Find Top Chunks → LLM Reads & Answers

This is the "Retrieval Augmented Generation" chain!
"""

# Create the RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # "stuff" = put all context into one prompt
    retriever=vectorstore.as_retriever(
        search_kwargs={"k": 3}  # Return top 3 chunks
    ),
    return_source_documents=True  # Include sources in response
)

print("✅ RAG chain created!")

# TEST IT!
print("\n" + "="*70)
print("🚀 TESTING THE COMPLETE RAG SYSTEM")
print("="*70)

question = "What is the compression ratio of the TSI engine?"

print(f"\n❓ Question: {question}")
print("\n🔄 Processing...")
print("   1. Converting question to embedding...")
print("   2. Searching vector database...")
print("   3. Finding top 3 relevant chunks...")
print("   4. Sending chunks + question to LLM...")
print("   5. Generating answer...\n")

result = qa_chain({"query": question})

print("="*70)
print("🤖 ANSWER:")
print("="*70)
print(result['result'])
print("="*70)

print("\n📚 SOURCES USED:")
for i, doc in enumerate(result['source_documents'], 1):
    page = doc.metadata.get('page', 'Unknown')
    preview = doc.page_content[:100].replace('\n', ' ')
    print(f"   {i}. Page {page}: {preview}...")

"""
🎉 IT WORKS! You just built a RAG system!

The AI:
✅ Read the manual
✅ Found relevant information
✅ Generated an accurate answer
✅ Cited its sources

This is real AI engineering!
"""

# ============================================================================
# CELL 10: Test Multiple Questions
# ============================================================================
"""
🧪 Let's test several questions to see how well it works!
"""

test_questions = [
    "What are the main components of the TSI engine?",
    "Explain the function of the turbocharger wastegate",
    "What is direct fuel injection?",
    "How does the engine control system work?",
    "What are the advantages of the TSI engine?"
]

print("🔬 TESTING MULTIPLE QUESTIONS")
print("="*70)

for i, question in enumerate(test_questions, 1):
    print(f"\n📝 Question {i}: {question}")
    result = qa_chain({"query": question})
    print(f"🤖 Answer: {result['result'][:200]}...")  # First 200 chars
    print(f"📄 Sources: Pages {[doc.metadata.get('page') for doc in result['source_documents']]}")
    print("-"*70)

"""
👀 Notice:
- Different questions retrieve different chunks
- Answers are specific and relevant
- Sources are cited

🎓 EXERCISE #3:
Think of a question that's NOT in the manual.
What happens when you ask it?

Try: "How do I change the oil in a Tesla?"
"""

# ============================================================================
# CELL 11: Build a User-Friendly Interface with Gradio
# ============================================================================
"""
🎨 Creating a Web Interface

Typing in code cells isn't user-friendly!
Let's build a proper web interface using Gradio.

This will:
✅ Create a text box for questions
✅ Display answers nicely
✅ Show sources
✅ Provide example questions
✅ Give you a PUBLIC URL you can share!
"""

def ask_question(question):
    """
    This function wraps our RAG chain for the UI
    """
    # Validate input
    if not question or not question.strip():
        return "⚠️ Please enter a question!"

    try:
        # Run the RAG chain
        result = qa_chain({"query": question})
        answer = result['result']

        # Format sources
        sources = result['source_documents']
        source_text = "\n\n" + "="*50 + "\n📚 SOURCES:\n" + "="*50 + "\n"

        for i, doc in enumerate(sources, 1):
            page = doc.metadata.get('page', 'Unknown')
            preview = doc.page_content[:150].replace('\n', ' ')
            source_text += f"\n{i}. Page {page}:\n   {preview}...\n"

        return answer + source_text

    except Exception as e:
        return f"❌ Error: {str(e)}\n\nPlease check your API key and try again."

# Create the Gradio interface
print("🎨 Creating web interface...")

interface = gr.Interface(
    fn=ask_question,
    inputs=gr.Textbox(
        lines=3,
        placeholder="Ask a question about the TSI engine...",
        label="❓ Your Question"
    ),
    outputs=gr.Textbox(
        lines=15,
        label="🤖 Answer & Sources"
    ),
    title="🚗 Automotive Technical Assistant",
    description="""
    **Welcome to your AI-powered automotive tech assistant!**

    This system has read the VAG SSP 913 manual on TSI Engine Technology.
    Ask any question about TSI engines and get instant, cited answers!

    **Built with:** RAG (Retrieval Augmented Generation)
    """,
    examples=[
        ["What is a TSI engine?"],
        ["How does the turbocharger work?"],
        ["What are the advantages of direct injection?"],
        ["Explain the engine control system"],
        ["What is the compression ratio?"]
    ],
    theme="soft",
    allow_flagging="never"
)

# Launch the interface!
print("🚀 Launching interface...")
print("\nYou'll get two URLs:")
print("1. Local URL - works only on your computer")
print("2. Public URL - share this with anyone! (works for 72 hours)")
print("\n" + "="*70)

interface.launch(share=True)  # share=True creates a public link!

"""
🎉 YOUR RAG SYSTEM IS LIVE!

You should see:
- A local URL: http://127.0.0.1:7860
- A public URL: https://xxxxx.gradio.live

Try it out! Click the example questions or type your own.

📤 SHARE IT:
Copy the public URL and share with friends, colleagues, or instructors!
"""

# ============================================================================
# CELL 12: Understanding Cost & Performance
# ============================================================================
"""
💰 Cost Analysis

Let's understand how much this costs to run:

EMBEDDINGS: FREE! ✅
- Running locally on your computer
- No API calls
- No ongoing cost

LLM (OpenRouter): Pay per query 💵
- Model: Gemini Flash 1.5
- Input: ~$0.075 per 1M tokens
- Output: ~$0.30 per 1M tokens

Typical Query:
- Question: ~50 tokens
- Retrieved context: ~800 tokens
- Answer: ~150 tokens
- Total: ~1000 tokens = ~$0.0003 (three hundredths of a cent!)

Your $5 credit = ~16,000 queries!

🚀 Performance:

Average response time: 2-4 seconds
- Embedding query: <0.1s
- Vector search: <0.1s
- LLM generation: 2-3s

Total chunks searched: {vectorstore._collection.count()}
Search speed: <100ms even with thousands of chunks!
"""

# Let's check our actual usage
print("📊 SYSTEM STATISTICS")
print("="*70)
print(f"Total chunks in database: {vectorstore._collection.count()}")
print(f"Embedding dimensions: {len(embeddings.embed_query('test'))}")
print(f"Model: google/gemini-flash-1.5")
print(f"Vector database size: ~{vectorstore._collection.count() * 0.001:.2f} MB")
print("="*70)

"""
🎓 EXERCISE #4: Optimize for Cost

Try changing these parameters and see how it affects answers:

1. Number of chunks retrieved (k value):
   - Change search_kwargs={"k": 3} to k=1 or k=5
   - More chunks = better context but higher cost

2. LLM temperature:
   - Change temperature=0.1 to 0.5
   - Higher = more creative, Lower = more factual

3. Max tokens:
   - Change max_tokens=500 to 200 or 1000
   - Affects answer length and cost

Experiment and find the sweet spot!
"""

# ============================================================================
# CELL 13: Saving & Loading Your Vector Database
# ============================================================================
"""
💾 Reusing Your Vector Database

Creating embeddings takes time. You don't want to do it every time!

Good news: ChromaDB saves to disk automatically.

Next time you run this notebook, you can LOAD the existing database:
"""

# This is how you LOAD an existing database (don't run this now!):
"""
# Load existing vector database
vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

print(f"✅ Loaded existing database with {vectorstore._collection.count()} chunks!")
"""

"""
When to rebuild vs. load:
- REBUILD: When you add new documents or change chunking strategy
- LOAD: When you just want to query the existing database

💡 Pro Tip: In production, you'd have separate scripts for:
1. Building/updating the database (run occasionally)
2. Querying the database (run constantly)
"""

# ============================================================================
# CELL 14: Homework & Next Steps
# ============================================================================
"""
🎓 HOMEWORK ASSIGNMENTS

To solidify your learning, try these exercises:

📝 BEGINNER LEVEL:
1. Test 20 different questions and document which work well
2. Try adjusting chunk_size to 500 and 1500 - compare results
3. Change the number of retrieved chunks (k=1, k=5) - how does it affect answers?
4. Customize the Gradio interface (change title, colors, examples)

📝 INTERMEDIATE LEVEL:
5. Try a different automotive PDF (find one online)
6. Experiment with different OpenRouter models (try llama-3.1-8b)
7. Add error handling to show better messages when things fail
8. Track and log which questions users ask most

📝 ADVANCED LEVEL:
9. Add a "confidence score" to answers (use similarity scores)
10. Implement caching to save money on repeated questions
11. Create a comparison: same question to 3 different models
12. Build a simple analytics dashboard showing query stats

🎯 CHALLENGE PROJECT:
Build a RAG system for YOUR company's documentation!
- Use your internal manuals/procedures
- Customize for your specific use case
- Deploy it for your team to use

📚 Additional Resources:
- LangChain Docs: https://python.langchain.com/
- OpenRouter Models: https://openrouter.ai/models
- ChromaDB Docs: https://docs.trychroma.com/
- Gradio Docs: https://gradio.app/docs/

🔜 SESSION 2 PREVIEW:

Next session we'll add:
✅ Conversation memory (ask follow-up questions!)
✅ Better prompts (more accurate answers)
✅ Source highlighting (show exact sentences used)
✅ Error handling (make it production-ready)

See you next time! 🚀
"""

# ============================================================================
# CELL 15: Feedback & Questions
# ============================================================================
"""
💬 SESSION FEEDBACK

Please answer these quick questions:

1. How would you rate this session? (1-5 stars)
2. What was the most valuable thing you learned?
3. What was most confusing?
4. What would you like to learn more about?
5. Any suggestions for improvement?

Share your feedback in the chat or email the instructor!

❓ COMMON QUESTIONS:

Q: Can I use this for non-automotive documents?
A: Absolutely! Just change the PDF and it works for any domain.

Q: How do I deploy this for real users?
A: We'll cover deployment in Session 4! (Streamlit Cloud, Docker, etc.)

Q: What if I want to use multiple PDFs?
A: That's Session 3! We'll build multi-document RAG.

Q: Can this work offline?
A: Partially - embeddings and search yes, but LLM needs internet.
   Solution: Use Ollama for local LLMs (we'll cover this later).

Q: Is this better than fine-tuning?
A: For most use cases, YES! RAG is cheaper, faster to update, and
   provides citations. Fine-tuning is for style/tone, not knowledge.

🙏 THANK YOU!

Congratulations on building your first RAG system!
You're now equipped with production-grade AI engineering skills.

Keep experimenting, keep building, and see you in Session 2!

Happy coding! 🚗💨
"""

print("="*70)
print("📘 END OF SESSION 1 NOTEBOOK")
print("="*70)
print("\n✅ You've completed all the code cells!")
print("🎉 Your RAG system is ready to use!")
print("🔗 Share your Gradio link with others to show off your work!")
print("\n👋 See you in Session 2!")
