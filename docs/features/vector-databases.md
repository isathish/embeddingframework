# Vector Databases

EmbeddingFramework supports multiple vector database backends, allowing you to store and query embeddings efficiently.

---

## 📦 Supported Databases

### 1️⃣ ChromaDB
- Local and persistent vector storage.
- Ideal for small to medium-scale projects.
- No external dependencies for basic usage.

**Example:**
```python
from embeddingframework.adapters.vector_dbs import ChromaDBAdapter

db = ChromaDBAdapter(persist_directory="./chroma_store")
db.add_texts(["Hello world"], [[0.1, 0.2, 0.3]])
```

---

### 2️⃣ Milvus
- High-performance distributed vector database.
- Suitable for large-scale deployments.
- Requires Milvus server running.

**Example:**
```python
from embeddingframework.adapters.milvus_adapter import MilvusAdapter

db = MilvusAdapter(host="localhost", port="19530")
db.add_texts(["Hello world"], [[0.1, 0.2, 0.3]])
```

---

### 3️⃣ Pinecone
- Fully managed vector database service.
- Scales automatically with your needs.
- Requires API key.

**Example:**
```python
from embeddingframework.adapters.pinecone_adapter import PineconeAdapter

db = PineconeAdapter(api_key="YOUR_PINECONE_API_KEY", index_name="my-index")
db.add_texts(["Hello world"], [[0.1, 0.2, 0.3]])
```

---

### 4️⃣ Weaviate
- Open-source vector search engine.
- Supports hybrid search (vector + keyword).
- Can be self-hosted or cloud-hosted.

**Example:**
```python
from embeddingframework.adapters.weaviate_adapter import WeaviateAdapter

db = WeaviateAdapter(url="http://localhost:8080")
db.add_texts(["Hello world"], [[0.1, 0.2, 0.3]])
```

---

## 🔄 Switching Databases

The API is consistent across all adapters, so switching between databases is as simple as changing the adapter import and initialization.

---

## 📚 Related
- [Cloud Storage](cloud-storage.md)
- [Embedding Providers](embedding-providers.md)
