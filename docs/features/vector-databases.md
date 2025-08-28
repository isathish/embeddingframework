# Vector Databases

EmbeddingFramework supports multiple vector database backends, allowing you to store and query embeddings efficiently.

---

## 📦 Supported Databases

Below are the supported vector databases with **detailed explanations**, **technical functions**, and **usage patterns**.

### 1️⃣ ChromaDB
- Local and persistent vector storage.
- Ideal for small to medium-scale projects.
- No external dependencies for basic usage.

**Technical Functions:**
- `__init__(persist_directory: str)`: Initializes the ChromaDB adapter with a local storage path.
- `add_texts(texts: List[str], embeddings: List[List[float]])`: Stores text and corresponding embeddings.
- `query(query_text: str, top_k: int)`: Retrieves the top_k most similar entries.

**Example:**
```python
from embeddingframework.adapters.vector_dbs import ChromaDBAdapter

db = ChromaDBAdapter(persist_directory="./chroma_store")
db.add_texts(["Hello world"], [[0.1, 0.2, 0.3]])
results = db.query("Hello", top_k=1)
print(results)
```

---

### 2️⃣ Milvus
- High-performance distributed vector database.
- Suitable for large-scale deployments.
- Requires Milvus server running.

**Technical Functions:**
- `__init__(host: str, port: str)`: Connects to a Milvus server.
- `add_texts(texts: List[str], embeddings: List[List[float]])`: Inserts data into Milvus.
- `query(query_text: str, top_k: int)`: Performs similarity search.

**Example:**
```python
from embeddingframework.adapters.milvus_adapter import MilvusAdapter

db = MilvusAdapter(host="localhost", port="19530")
db.add_texts(["Hello world"], [[0.1, 0.2, 0.3]])
results = db.query("Hello", top_k=1)
print(results)
```

---

### 3️⃣ Pinecone
- Fully managed vector database service.
- Scales automatically with your needs.
- Requires API key.

**Technical Functions:**
- `__init__(api_key: str, index_name: str)`: Connects to Pinecone with API key and index.
- `add_texts(texts: List[str], embeddings: List[List[float]])`: Inserts vectors into Pinecone.
- `query(query_text: str, top_k: int)`: Retrieves similar vectors.

**Example:**
```python
from embeddingframework.adapters.pinecone_adapter import PineconeAdapter

db = PineconeAdapter(api_key="YOUR_PINECONE_API_KEY", index_name="my-index")
db.add_texts(["Hello world"], [[0.1, 0.2, 0.3]])
results = db.query("Hello", top_k=1)
print(results)
```

---

### 4️⃣ Weaviate
- Open-source vector search engine.
- Supports hybrid search (vector + keyword).
- Can be self-hosted or cloud-hosted.

**Technical Functions:**
- `__init__(url: str)`: Connects to a Weaviate instance.
- `add_texts(texts: List[str], embeddings: List[List[float]])`: Adds data to Weaviate.
- `query(query_text: str, top_k: int)`: Performs hybrid or vector search.

**Example:**
```python
from embeddingframework.adapters.weaviate_adapter import WeaviateAdapter

db = WeaviateAdapter(url="http://localhost:8080")
db.add_texts(["Hello world"], [[0.1, 0.2, 0.3]])
results = db.query("Hello", top_k=1)
print(results)
```

---

## 🔄 Switching Databases

The API is consistent across all adapters, so switching between databases is as simple as changing the adapter import and initialization.

---

## 📚 Related
- [Cloud Storage](cloud-storage.md)
- [Embedding Providers](embedding-providers.md)
