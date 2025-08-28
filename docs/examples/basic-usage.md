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

## ✅ Summary
You have successfully:
- Initialized an embedding provider
- Generated embeddings
- Stored them in a vector database
