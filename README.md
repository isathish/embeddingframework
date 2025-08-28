# EmbeddingFramework

A **modular, extensible, and production-ready** framework for working with embeddings, vector databases, and storage backends.  
Designed for **AI-powered search, retrieval, and knowledge management systems**.

---

## 🚀 Features

### **Embedding Providers**
- **OpenAI** – Seamless integration with OpenAI's embedding API.
- **HuggingFace Transformers** – Local model inference for privacy and cost efficiency.
- **Local Callable** – Plug in your own embedding function.

### **Vector Database Adapters**
- **ChromaDB** – Lightweight, local-first vector DB.
- **Pinecone** – Fully managed, scalable vector DB (optional dependency).
- **Weaviate** – Open-source, cloud-native vector search engine.
- **Milvus** – High-performance vector database for large-scale AI.
- **FAISS** – Facebook AI Similarity Search for local, high-speed retrieval.

### **Storage Adapters**
- **AWS S3** – Store and retrieve files from Amazon S3.
- **Google Cloud Storage (GCS)** – GCP-native storage integration.
- **Azure Blob Storage** – Microsoft Azure storage support.

### **Processing Pipeline**
- **File Processor** – Extracts and preprocesses text from files.
- **Async File Processor** – High-throughput, non-blocking file ingestion.
- **Custom Splitters** – Chunk text for optimal embedding performance.
- **Preprocessing Utilities** – Clean, normalize, and prepare text.

### **CLI Tool**
- Run embedding pipelines directly from the terminal.
- Supports **async processing** for large datasets.
- Configurable via arguments and environment variables.

---

## 📦 Installation

```bash
# Install core framework
pip install embeddingframework

# Install with all optional dependencies
pip install embeddingframework[all]

# Install with specific extras
pip install embeddingframework[openai]
pip install embeddingframework[huggingface]
pip install embeddingframework[faiss]
pip install embeddingframework[pinecone]
pip install embeddingframework[weaviate]
pip install embeddingframework[milvus]
pip install embeddingframework[s3]
pip install embeddingframework[gcs]
pip install embeddingframework[azure]
```

---

## ⚡ Quick Start

```python
from embeddingframework.adapters.openai_embedding_adapter import OpenAIEmbeddingAdapter
from embeddingframework.adapters.vector_dbs import ChromaDBAdapter

# Initialize embedding provider
embedder = OpenAIEmbeddingAdapter(api_key="YOUR_API_KEY")

# Initialize vector DB
vector_db = ChromaDBAdapter()

# Embed and store
text = "EmbeddingFramework makes vector search easy!"
embedding = embedder.embed([text])
vector_db.add_embeddings([embedding], [text])
```

---

## 🛠 CLI Usage

```bash
embeddingframework process --input ./docs --db chromadb --provider openai --api-key $OPENAI_API_KEY
```

---

## 🏗 Architecture

```
embeddingframework/
├── adapters/
│   ├── base.py
│   ├── vector_dbs_base.py
│   ├── chromadb_adapter.py
│   ├── pinecone_adapter.py
│   ├── weaviate_adapter.py
│   ├── milvus_adapter.py
│   ├── faiss_adapter.py
│   ├── openai_embedding_adapter.py
│   ├── providers.py
│   └── storage/
│       ├── s3_storage_adapter.py
│       ├── gcs_storage_adapter.py
│       └── azure_blob_storage_adapter.py
├── processors/
│   ├── file_processor.py
├── utils/
│   ├── file_utils.py
│   ├── preprocessing.py
│   ├── retry.py
│   └── splitters.py
└── tests/
```

---

## 📅 Roadmap

- [x] OpenAI, HuggingFace, Local embedding providers
- [x] ChromaDB, Pinecone, Weaviate, Milvus adapters
- [x] AWS S3, GCS, Azure storage adapters
- [x] CLI with async processing
- [ ] FAISS adapter
- [ ] HuggingFace provider improvements
- [ ] Advanced async pipeline optimizations
- [ ] Full test coverage with mocks for optional dependencies

---

## 🧪 Testing

```bash
pytest --maxfail=1 --disable-warnings -q
```

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Submit a PR

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
