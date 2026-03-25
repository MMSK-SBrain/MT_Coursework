# Session 1 Troubleshooting Guide
## Quick Solutions to Common Issues

**For Students & Instructors**

This guide covers the most common errors you'll encounter and how to fix them quickly.

---

## Table of Contents
1. [Environment & Installation Issues](#environment--installation-issues)
2. [File & PDF Loading Issues](#file--pdf-loading-issues)
3. [API & Authentication Issues](#api--authentication-issues)
4. [Embedding & Vector Database Issues](#embedding--vector-database-issues)
5. [LLM & Response Issues](#llm--response-issues)
6. [Gradio & UI Issues](#gradio--ui-issues)
7. [Performance Issues](#performance-issues)
8. [Google Colab Specific Issues](#google-colab-specific-issues)

---

## Environment & Installation Issues

### Error: `ModuleNotFoundError: No module named 'langchain'`

**Cause:** Package not installed

**Solution:**
```python
# In Colab:
!pip install -q langchain langchain-community chromadb pypdf sentence-transformers openai gradio

# Restart the runtime after installation:
# Runtime → Restart Runtime

# Then re-run your imports
```

**Prevention:** Always run the installation cell first!

---

### Error: `ImportError: cannot import name 'X' from 'langchain'`

**Cause:** Version mismatch or outdated package

**Solution:**
```python
# Upgrade to latest versions
!pip install --upgrade langchain langchain-community openai

# If still issues, uninstall and reinstall:
!pip uninstall langchain -y
!pip install langchain langchain-community
```

---

### Error: Package installation is taking forever

**Cause:** Slow internet or large dependencies

**Solution:**
1. Be patient - first time takes 2-3 minutes
2. Check your internet connection
3. In Colab, try: Runtime → Reset all runtimes
4. Try installing packages one by one to identify the slow one

---

## File & PDF Loading Issues

### Error: `FileNotFoundError: [Errno 2] No such file or directory`

**Cause:** PDF file not found at specified path

**Solutions:**

**In Google Colab:**
```python
# Option 1: Upload file manually
from google.colab import files
uploaded = files.upload()
pdf_filename = list(uploaded.keys())[0]

# Option 2: Check current directory
!pwd  # Shows current directory
!ls   # Lists files in current directory
```

**In Local Environment:**
```python
# Check if file exists
import os
print(os.path.exists("your_file.pdf"))  # Should print True

# Use absolute path
pdf_path = "/full/path/to/your_file.pdf"

# Or navigate to correct directory
os.chdir("/path/to/correct/folder")
```

---

### Error: `PDF is encrypted` or `Cannot extract text from PDF`

**Cause:** PDF is password-protected or scanned images

**Solutions:**
1. **If password-protected:**
```python
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("encrypted.pdf")
writer = PdfWriter()

reader.decrypt("password")

for page in reader.pages:
    writer.add_page(page)

with open("decrypted.pdf", "wb") as f:
    writer.write(f)
```

2. **If scanned images:**
- Use OCR: Install `pytesseract` and `pdf2image`
- Or use a pre-processed PDF instead

3. **Quick fix:** Download a different version of the PDF

---

### Error: PDF loads but text is garbled

**Cause:** Encoding issues or complex PDF formatting

**Solution:**
```python
# Try alternative PDF loader
from langchain.document_loaders import UnstructuredPDFLoader

loader = UnstructuredPDFLoader("document.pdf")
documents = loader.load()
```

---

## API & Authentication Issues

### Error: `Invalid API key`

**Cause:** Incorrect or malformed API key

**Solutions:**
1. **Check the key format:**
   - Should start with: `sk-or-v1-`
   - No extra spaces or quotes

2. **Re-enter securely:**
```python
import os
from getpass import getpass

# Clear existing key
if 'OPENROUTER_API_KEY' in os.environ:
    del os.environ['OPENROUTER_API_KEY']

# Re-enter
os.environ['OPENROUTER_API_KEY'] = getpass("Enter API key: ")
```

3. **Regenerate key:**
   - Go to OpenRouter dashboard
   - Create new API key
   - Copy carefully (select all, copy)

---

### Error: `Insufficient credits` or `Payment required`

**Cause:** OpenRouter account has no credits

**Solution:**
1. Go to https://openrouter.ai/
2. Click Credits/Billing
3. Add minimum $5
4. Wait 1-2 minutes for processing

**Temporary workaround:**
```python
# Use free model while you add credits
llm = ChatOpenAI(
    model_name="meta-llama/llama-3.1-8b-instruct:free",
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=os.environ['OPENROUTER_API_KEY'],
)
```

---

### Error: `Rate limit exceeded`

**Cause:** Too many requests too quickly

**Solutions:**
1. **Wait:** 30-60 seconds, then try again
2. **Add delay between requests:**
```python
import time

for question in questions:
    result = qa_chain({"query": question})
    time.sleep(1)  # Wait 1 second between queries
```

3. **Check if someone is using your key:** Regenerate if shared accidentally

---

### Error: `Connection timeout` or `Connection refused`

**Cause:** Network issues or API downtime

**Solutions:**
1. Check your internet connection
2. Visit https://status.openrouter.ai/
3. Try a different model
4. Add timeout parameter:
```python
llm = ChatOpenAI(
    model_name="google/gemini-flash-1.5",
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=os.environ['OPENROUTER_API_KEY'],
    request_timeout=60  # Increase timeout to 60 seconds
)
```

---

## Embedding & Vector Database Issues

### Error: `RuntimeError: CUDA not available`

**Cause:** Code is trying to use GPU but none available

**Solution:**
```python
# Force CPU usage (works everywhere)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'},  # Explicit CPU
    encode_kwargs={'normalize_embeddings': True}
)
```

---

### Error: Embedding creation is taking forever (>5 minutes)

**Cause:** Too many chunks or slow CPU

**Solutions:**
1. **Check chunk count:**
```python
print(f"Number of chunks: {len(chunks)}")
# If >1000, consider larger chunk_size
```

2. **Reduce chunks temporarily for testing:**
```python
# Use only first 100 chunks for testing
test_chunks = chunks[:100]
vectorstore = Chroma.from_documents(
    documents=test_chunks,
    embedding=embeddings
)
```

3. **Be patient:** First time is slow, but database persists!

---

### Error: `Chroma.from_documents() fails with cryptic error`

**Possible causes & solutions:**

**1. ChromaDB version issue:**
```python
!pip install --upgrade chromadb
```

**2. Corrupted persist directory:**
```python
# Delete and recreate
import shutil
shutil.rmtree("./chroma_db", ignore_errors=True)

# Then recreate vector store
```

**3. Empty documents:**
```python
# Check if chunks have content
for i, chunk in enumerate(chunks[:5]):
    print(f"Chunk {i} length: {len(chunk.page_content)}")

# Remove empty chunks
chunks = [c for c in chunks if len(c.page_content.strip()) > 50]
```

---

### Error: `Similarity search returns no results`

**Cause:** Mismatch between embedding models or empty database

**Solutions:**
1. **Verify database has content:**
```python
print(f"Database size: {vectorstore._collection.count()}")
# Should be > 0
```

2. **Check embedding consistency:**
```python
# Make sure you're using the SAME embedding model
# that was used to create the database
```

3. **Try different query:**
```python
# Test with simpler query
results = vectorstore.similarity_search("engine", k=5)
print(f"Found {len(results)} results")
```

---

## LLM & Response Issues

### Error: `Answer is "I don't know" even when info IS in the document`

**Cause:** Retrieved chunks aren't relevant, or LLM is being too cautious

**Solutions:**
1. **Check what was retrieved:**
```python
result = qa_chain({"query": "your question"})
print("\nRetrieved chunks:")
for i, doc in enumerate(result['source_documents']):
    print(f"\nChunk {i}:")
    print(doc.page_content[:200])
```

2. **Increase number of retrieved chunks:**
```python
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5})  # Was 3
)
```

3. **Improve the prompt:**
```python
from langchain.prompts import PromptTemplate

template = """Use the following context to answer the question.
If you find relevant information in the context, provide a detailed answer.
Only say "I don't know" if the context truly doesn't contain the information.

Context: {context}

Question: {question}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["context", "question"])
```

---

### Error: `Answer is completely wrong or hallucinated`

**Cause:** LLM inventing information despite RAG

**Solutions:**
1. **Lower temperature:**
```python
llm = ChatOpenAI(
    model_name="google/gemini-flash-1.5",
    temperature=0.0,  # More deterministic
    # ... other params
)
```

2. **Add stronger instructions:**
```python
template = """Answer ONLY based on the provided context.
Do NOT use external knowledge.
If unsure, say "The document doesn't contain this information."

Context: {context}
Question: {question}
Answer:"""
```

3. **Try a better model:**
```python
# Switch to higher quality model
model_name="openai/gpt-4o-mini"  # Instead of gemini-flash
```

---

### Error: `Response is too short` or `Response is too long`

**Cause:** max_tokens setting

**Solution:**
```python
llm = ChatOpenAI(
    model_name="google/gemini-flash-1.5",
    max_tokens=800,  # Adjust: 200-2000 depending on needs
    # ... other params
)
```

---

## Gradio & UI Issues

### Error: `Gradio interface won't launch`

**Cause:** Port conflict or Gradio not installed

**Solutions:**
1. **Verify installation:**
```python
!pip install --upgrade gradio
```

2. **Try different port:**
```python
interface.launch(server_port=7861)  # Try different port
```

3. **Check for error messages in output**

---

### Error: `Share link doesn't work`

**Cause:** Temporary link expired or network issues

**Solutions:**
1. **Regenerate:**
```python
interface.launch(share=True)  # Creates new link
```

2. **Check expiration:** Gradio links expire after 72 hours

3. **Try without share:**
```python
interface.launch(share=False)  # Local only
```

---

### Error: Interface shows error when asking questions

**Cause:** RAG chain not working properly

**Solution:**
```python
def ask_question(question):
    try:
        result = qa_chain({"query": question})
        return result['result']
    except Exception as e:
        return f"Error: {str(e)}\n\nPlease check:\n- API key valid?\n- Credits available?\n- Internet working?"
```

---

## Performance Issues

### Issue: Everything is very slow

**Diagnosis & Solutions:**

1. **Slow embedding creation:**
   - Normal: 1-2 minutes for 200 chunks
   - Abnormal: >5 minutes
   - Solution: Reduce chunk count, use better CPU

2. **Slow similarity search:**
   - Normal: <0.5 seconds
   - Abnormal: >2 seconds
   - Solution: Rebuild database, reduce k value

3. **Slow LLM responses:**
   - Normal: 2-5 seconds
   - Abnormal: >10 seconds
   - Solution: Try different model, check internet

---

### Issue: Running out of memory

**Cause:** Too many documents or embeddings

**Solutions:**
```python
# Process in batches
batch_size = 50
for i in range(0, len(chunks), batch_size):
    batch = chunks[i:i+batch_size]
    # Process batch
```

In Colab:
- Runtime → Change runtime type → Higher RAM

---

## Google Colab Specific Issues

### Issue: Session disconnects

**Cause:** Inactive for too long

**Solutions:**
1. Keep browser tab active
2. Click in notebook occasionally
3. Run periodic cells
4. Upgrade to Colab Pro (if doing intensive work)

---

### Issue: "Runtime disconnected" error

**Solutions:**
1. Runtime → Reconnect
2. Re-run initialization cells
3. May need to re-upload files

---

### Issue: Can't save work

**Solution:**
```python
# Always save to Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Save important outputs
import pickle

with open('/content/drive/My Drive/vectorstore.pkl', 'wb') as f:
    pickle.dump(vectorstore, f)
```

---

## Quick Diagnostic Checklist

When something goes wrong, check these in order:

- [ ] **Internet connection** working?
- [ ] **All packages** installed? Run installation cell
- [ ] **Runtime** restarted after installation?
- [ ] **PDF file** uploaded/accessible?
- [ ] **API key** entered correctly?
- [ ] **Credits** available in OpenRouter account?
- [ ] **Previous cells** all executed successfully?
- [ ] **Error message** read carefully - what does it say?

---

## Getting Help

### Self-Help Steps:
1. Read the error message carefully
2. Check this troubleshooting guide
3. Google the error message
4. Check code for typos

### Ask for Help:
1. Copy the FULL error message
2. Note which cell/step it failed
3. Share what you've already tried
4. Ask instructor or classmates

### Provide This Info:
- Exact error message
- Code that caused the error
- Environment (Colab vs local)
- What you've tried already

---

## Emergency Fallback Procedures

### If Everything Fails: Use Pre-Run Notebook

Instructor should have a backup notebook with all cells already executed and outputs visible.

### If API Doesn't Work: Use Demo Mode

```python
# Mock RAG responses for demonstration
def mock_qa(question):
    responses = {
        "turbocharger": "The turbocharger increases engine power by...",
        "compression": "The compression ratio is approximately 10:1...",
        # etc.
    }
    for keyword, response in responses.items():
        if keyword in question.lower():
            return response
    return "I don't have information about that in my training data."

# Use in Gradio
interface = gr.Interface(fn=mock_qa, ...)
```

---

## Prevention Tips

### Before Session:
- [ ] Test your setup the day before
- [ ] Verify API key works
- [ ] Download PDF in advance
- [ ] Join session 5 minutes early

### During Session:
- [ ] Execute cells in order
- [ ] Wait for completion before moving on
- [ ] Don't skip import/setup cells
- [ ] Ask questions early

### After Session:
- [ ] Save your work
- [ ] Note what worked/didn't work
- [ ] Review error messages for learning

---

## Still Stuck?

**Don't panic!** AI development has many moving parts. Everyone encounters errors.

**Remember:**
- Errors are learning opportunities
- Most issues have simple fixes
- Your classmates are probably facing the same issue
- Instructors are here to help

**Contact:**
- Raise hand / ask in chat during session
- Email instructor with detailed error info
- Check with study group
- Post in course discussion forum

---

## Common Error Messages Reference

### Quick Lookup Table

| Error Message | Quick Fix |
|---------------|-----------|
| `ModuleNotFoundError` | Run pip install |
| `FileNotFoundError` | Check file path |
| `Invalid API key` | Re-enter API key |
| `Rate limit` | Wait 60 seconds |
| `CUDA not available` | Add `device='cpu'` |
| `Connection timeout` | Check internet |
| `Insufficient credits` | Add credits to OpenRouter |
| `No results found` | Increase k value |

---

**End of Troubleshooting Guide**

**Remember: Every expert was once a beginner who never gave up!**

You've got this! 🚀
