# EmbeddingFramework

A **modular, extensible, and production-ready** Python framework for generating embeddings, processing files, and storing them in various vector databases and cloud storage providers. Designed for **scalability**, **flexibility**, and **ease of integration** into AI-powered applications.

---

## 🚀 Features

- **Multiple Vector Database Integrations**
  - [ChromaDB](https://www.trychroma.com/)
  - [Pinecone](https://www.pinecone.io/) *(optional)*
  - [Weaviate](https://weaviate.io/) *(optional)*
  - [Milvus](https://milvus.io/)

- **Cloud Storage Support**
  - Amazon S3 *(optional)*
  - Google Cloud Storage *(optional)*
  - Azure Blob Storage *(optional)*

- **Pluggable Embedding Providers**
  - OpenAI Embeddings
  - Easily extendable to other providers

- **File Processing Pipeline**
  - Preprocessing
  - Splitting
  - Retry logic for robustness

- **Optional Dependency Handling**
  - Gracefully degrades when optional packages are not installed
  - Conditional imports to avoid runtime errors

- **Test Coverage**
  - Unit tests with `pytest`
  - Mocking for external dependencies
  - Code coverage with `pytest-cov`

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/isathish/embeddingframework.git
cd embeddingframework

# Install core dependencies
pip install -e .

# Install optional dependencies as needed
pip install pinecone-client boto3 botocore google-cloud-storage azure-storage-blob
```

---

## 🛠 Usage

```python
from embeddingframework.adapters.vector_dbs import ChromaDBAdapter
from embeddingframework.adapters.openai_embedding_adapter import OpenAIEmbeddingAdapter

# Initialize embedding provider
embedding_provider = OpenAIEmbeddingAdapter(api_key="YOUR_OPENAI_API_KEY")

# Initialize vector DB adapter
vector_db = ChromaDBAdapter(collection_name="my_collection")

# Generate and store embeddings
texts = ["Hello world", "EmbeddingFramework is awesome!"]
embeddings = embedding_provider.embed(texts)
vector_db.add_embeddings(texts, embeddings)
```

---

## 📂 Project Structure

```
embeddingframework/
├── adapters/         # Vector DB and storage adapters
├── processors/       # File processing logic
├── utils/            # Utility functions
└── tests/            # Unit tests
```

---

## 🏗 Architecture

The framework follows a **modular adapter pattern**:

- **Embedding Adapters**: Handle embedding generation from various providers.
- **Vector DB Adapters**: Store and retrieve embeddings from supported databases.
- **Storage Adapters**: Manage file storage in cloud providers.
- **Processors**: Handle file ingestion, preprocessing, and splitting.

---

## 🔌 Extending the Framework

To add a new vector DB or embedding provider:

1. Create a new adapter class in the appropriate `adapters/` subdirectory.
2. Implement the required interface from `base.py`.
3. Register your adapter in `providers.py` or the relevant factory.

---

## 🧪 Testing

Run all tests with coverage:

```bash
pytest --cov=embeddingframework --cov-report=term-missing
```

---

## 🗺 Roadmap

- [ ] Add FAISS vector DB support
- [ ] Add HuggingFace embedding provider
- [ ] CLI for quick ingestion and querying
- [ ] Async processing pipeline

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 💡 Inspiration

EmbeddingFramework was built to **simplify AI application development** by providing a unified interface for embeddings, storage, and retrieval — without locking you into a single provider.
