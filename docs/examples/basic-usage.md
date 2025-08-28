# 📝 Basic Usage Example

This guide demonstrates a **simple workflow** using EmbeddingFramework.

---

## 1️⃣ Install the package
```bash
pip install embeddingframework
```

---

## 2️⃣ Import required modules
```python
from embeddingframework.adapters.openai_embedding_adapter import OpenAIEmbeddingAdapter
from embeddingframework.adapters.vector_dbs import ChromaDBAdapter
```

---

## 3️⃣ Initialize components
```python
embedding_provider = OpenAIEmbeddingAdapter(api_key="YOUR_OPENAI_API_KEY")
vector_db = ChromaDBAdapter(persist_directory="./chroma_store")
```

---

## 4️⃣ Generate embeddings
```python
texts = ["Hello world", "EmbeddingFramework is awesome!"]
embeddings = embedding_provider.embed_texts(texts)
```

---

## 5️⃣ Store embeddings
```python
vector_db.add_texts(texts, embeddings)
```

---

## 📊 Example Output

**Input:**
```python
texts = ["Hello world", "EmbeddingFramework is awesome!"]
```

**Output (example embeddings):**
```python
[
  [0.0123, -0.2345, 0.9876, ...],
  [-0.5432, 0.1234, 0.4567, ...]
]
```

---

## 🧩 Additional Examples

### Example 1: Using a Different Vector DB
```python
from embeddingframework.adapters.vector_dbs import WeaviateAdapter

vector_db = WeaviateAdapter(url="http://localhost:8080")
vector_db.add_texts(["Sample text"], [[0.1, 0.2, 0.3]])
```

### Example 2: Storing Metadata
```python
vector_db.add_texts(
    ["Document 1", "Document 2"],
    embeddings,
    metadatas=[{"source": "file1.txt"}, {"source": "file2.txt"}]
)
```

### Example 3: Querying the Database
```python
results = vector_db.query("Hello", top_k=2)
print(results)
```

---

## ✅ Summary
You have successfully:
- Initialized an embedding provider
- Generated embeddings
- Stored them in a vector database
- Queried the database
- Stored metadata alongside embeddings
