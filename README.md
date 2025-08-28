# EmbeddingFramework

A **modular, extensible, and production-ready** Python framework for generating, processing, and storing embeddings across multiple vector databases and cloud storage providers.

---

## 🚀 Features

- **Multi-Vector DB Support**  
  - [ChromaDB](https://www.trychroma.com/)  
  - [Milvus](https://milvus.io/)  
  - [Pinecone](https://www.pinecone.io/)  
  - [Weaviate](https://weaviate.io/)  

- **Multiple Embedding Providers**  
  - OpenAI Embeddings  
  - Easily extendable to other providers

- **Cloud Storage Integrations**  
  - AWS S3  
  - Google Cloud Storage (GCS)  
  - Azure Blob Storage  

- **File Processing Pipeline**  
  - Async file reading and processing  
  - Preprocessing utilities (cleaning, normalization, splitting)  
  - Customizable splitters for large documents  

- **Robust Utilities**  
  - Retry logic for transient failures  
  - File utilities for safe I/O  
  - Modular adapter-based architecture

- **Testing & Quality**  
  - 100% unit test coverage target  
  - `pytest` + `pytest-cov` integration  
  - Mocking/stubbing for external dependencies

---

## 📦 Installation

```bash
pip install embeddingframework
```

Or from source:

```bash
git clone https://github.com/isathish/embeddingframework.git
cd embeddingframework
pip install -e .
```

---

## 🛠 Usage

### Basic Example

```python
from embeddingframework.processors.file_processor import FileProcessor
from embeddingframework.adapters.openai_embedding_adapter import OpenAIEmbeddingAdapter
from embeddingframework.adapters.milvus_adapter import MilvusAdapter

# Initialize embedding provider
embedding_adapter = OpenAIEmbeddingAdapter(api_key="YOUR_OPENAI_KEY")

# Initialize vector DB
vector_db = MilvusAdapter(host="localhost", port="19530")

# Create file processor
processor = FileProcessor(embedding_adapter, vector_db)

# Process a file
await processor.process_file("sample.txt")
```

---

## 🏗 Architecture

```
embeddingframework/
├── adapters/         # Embedding & Vector DB adapters
├── processors/       # File processing logic
├── utils/            # Helper utilities
└── tests/            # Unit tests
```

- **Adapters**: Abstract integrations for embeddings, vector DBs, and storage.
- **Processors**: Orchestrate reading, preprocessing, embedding, and storing.
- **Utils**: Common helper functions and retry logic.

---

## 🔌 Extending the Framework

To add a new vector DB or embedding provider:

1. Create a new adapter in `embeddingframework/adapters/`.
2. Implement the required base class methods.
3. Register it in `providers.py` if needed.
4. Add unit tests in `tests/`.

---

## 🧪 Testing

Run all tests:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=embeddingframework --cov-report=term-missing
```

---

## 📈 Roadmap

- [ ] Add more embedding providers (Cohere, HuggingFace)
- [ ] Add streaming ingestion
- [ ] Add CLI interface
- [ ] Improve async performance

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💡 Contributing

Contributions are welcome! Please fork the repo and submit a PR.

---

## 🌟 Why EmbeddingFramework?

- **Production-ready**: Built with scalability and reliability in mind.
- **Extensible**: Easily add new providers and databases.
- **Tested**: Comprehensive unit test coverage.
- **Async-first**: Optimized for modern Python async workflows.
