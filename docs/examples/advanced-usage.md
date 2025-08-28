# 🚀 Advanced Usage Example

This guide demonstrates a **full end-to-end workflow** using EmbeddingFramework with advanced features.

---

## 1️⃣ Install the package
```bash
pip install embeddingframework
```

---

## 2️⃣ Import required modules
```python
from embeddingframework.adapters.openai_embedding_adapter import OpenAIEmbeddingAdapter
from embeddingframework.adapters.vector_dbs import MilvusAdapter
from embeddingframework.processors.file_processor import FileProcessor
```

---

## 3️⃣ Initialize components
```python
embedding_provider = OpenAIEmbeddingAdapter(api_key="YOUR_OPENAI_API_KEY")
vector_db = MilvusAdapter(host="localhost", port="19530")
processor = FileProcessor()
```

---

## 4️⃣ Process files
```python
text = processor.process_file("sample.pdf")
```

---

## 5️⃣ Generate embeddings
```python
embeddings = embedding_provider.embed_texts([text])
```

---

## 6️⃣ Store embeddings
```python
vector_db.add_texts([text], embeddings)
```

---

## 7️⃣ Query the database
```python
results = vector_db.query("search term", top_k=5)
print(results)
```

---

## 📊 Example Output

**Input File:** `sample.pdf` (contains "Artificial Intelligence is transforming the world.")

**Extracted Text:**
```
Artificial Intelligence is transforming the world.
```

**Generated Embedding (example):**
```python
[0.2345, -0.1234, 0.9876, ...]
```

**Query:**
```python
results = vector_db.query("AI transformation", top_k=2)
```

**Output:**
```python
[
  {"text": "Artificial Intelligence is transforming the world.", "score": 0.98},
  {"text": "AI is changing industries rapidly.", "score": 0.92}
]
```

---

## 🧩 Additional Examples

### Example 1: Batch Processing Multiple Files
```python
files = ["doc1.pdf", "doc2.txt"]
texts = [processor.process_file(f) for f in files]
embeddings = embedding_provider.embed_texts(texts)
vector_db.add_texts(texts, embeddings)
```

### Example 2: Using Metadata in Queries
```python
results = vector_db.query("AI", top_k=3, filter={"source": "doc1.pdf"})
```

### Example 3: Async Embedding Generation
```python
import asyncio

async def main():
    embeddings = await embedding_provider.aembed_texts(["Async example"])
    print(embeddings)

asyncio.run(main())
```

---

## ✅ Summary
You have successfully:
- Processed a file
- Generated embeddings
- Stored them in a distributed vector database
- Queried the database for semantic search
- Used batch processing, metadata filtering, and async embedding generation
