<h1 align="center">🧠 Embedding Providers</h1>

<p align="center">
  <b>Generate vector representations of text for semantic search, clustering, and AI applications</b>
</p>

---

EmbeddingFramework supports multiple embedding providers, allowing you to generate vector representations of text for semantic search, clustering, and other AI applications.

---

## 🧠 Supported Providers

### 1️⃣ OpenAI Embeddings
- State-of-the-art embeddings for text and code.
- Requires an OpenAI API key.

**Example:**
```python
from embeddingframework.adapters.openai_embedding_adapter import OpenAIEmbeddingAdapter

provider = OpenAIEmbeddingAdapter(api_key="YOUR_OPENAI_API_KEY")
embeddings = provider.embed_texts(["Hello world", "EmbeddingFramework is awesome!"])
```

---

## 🔄 Adding New Providers

EmbeddingFramework is designed to be **extensible**.  
To add a new provider:
1. Create a new adapter class in `embeddingframework/adapters/`.
2. Inherit from the base embedding adapter.
3. Implement the `embed_texts` method.

---

## 📚 Related
<p align="center">
  <a href="vector-databases.md">Vector Databases</a> •
  <a href="cloud-storage.md">Cloud Storage</a> •
  <a href="file-processing.md">File Processing</a>
</p>
- [Vector Databases](vector-databases.md)
- [Cloud Storage](cloud-storage.md)
- [File Processing](file-processing.md)
