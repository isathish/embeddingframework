# Quick Start

This guide will walk you through a **basic usage example** of EmbeddingFramework, from installation to storing and querying embeddings.

---

## 1️⃣ Install the Framework

If you haven't already, install EmbeddingFramework:

```bash
pip install embeddingframework
```

---

## 2️⃣ Initialize an Embedding Provider

Embedding providers generate vector representations of text.  
For example, using **OpenAI**:

```python
from embeddingframework.adapters.openai_embedding_adapter import OpenAIEmbeddingAdapter

embedding_provider = OpenAIEmbeddingAdapter(api_key="YOUR_OPENAI_API_KEY")
```

---

## 3️⃣ Initialize a Vector Database

Choose a vector database adapter.  
For example, using **ChromaDB**:

```python
from embeddingframework.adapters.vector_dbs import ChromaDBAdapter

vector_db = ChromaDBAdapter(persist_directory="./chroma_store")
```

---

## 4️⃣ Generate and Store Embeddings

```python
texts = ["Hello world", "EmbeddingFramework is awesome!"]
embeddings = embedding_provider.embed_texts(texts)
vector_db.add_texts(texts, embeddings)
```

---

## 5️⃣ Query the Vector Database

```python
results = vector_db.query("awesome framework", top_k=1)
print(results)
```

---

## ✅ Summary

In just a few lines of code, you:
1. Initialized an embedding provider.
2. Initialized a vector database.
3. Generated embeddings.
4. Stored them in the database.
5. Queried for similar results.

---

## 📚 Next Steps

- Explore [Features](../features/index.md) for more capabilities.
- Check [Examples](../examples/basic-usage.md) for advanced use cases.
