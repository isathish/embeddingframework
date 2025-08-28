# EmbeddingFramework

A high-performance, asynchronous, and extensible Python package for processing files, generating embeddings, and storing them in various vector databases with optional cloud storage integration.

## 🚀 Features

- **Asynchronous Processing**: Efficiently process large files using Python's `asyncio` for non-blocking operations.
- **Multi-Vector DB Support**:
  - [ChromaDB](https://www.trychroma.com/)
  - [Pinecone](https://www.pinecone.io/)
  - [Weaviate](https://weaviate.io/)
  - [Milvus](https://milvus.io/)
- **Embedding Models**:
  - OpenAI Embeddings
  - Easily extendable to other providers
- **Cloud Storage Integration**:
  - AWS S3
  - Google Cloud Storage (GCS)
  - Azure Blob Storage
- **Flexible Chunking**:
  - Binary chunking with configurable size
  - Text chunking with configurable size
  - Merge smaller chunks into larger ones
- **Parallel Processing**:
  - File-level parallelism
  - Chunk-level parallelism
- **Bandwidth Control**: Limit bytes/sec for streaming to avoid network congestion.
- **Quality Filtering**: Remove low-quality or too-small chunks.
- **Preprocessing**: Clean, normalize, and prepare text before embedding.
- **Retry Mechanism**: Automatic retries on failures during embedding or storage.
- **Packaged for PyPI**: Installable via `pip` for easy integration into your projects.
- **Unit Testing & Coverage**: Comprehensive test suite with coverage reporting.

## 📦 Installation

### From Source
```bash
git clone https://github.com/isathish/embeddingframework.git
cd embeddingframework
pip install -e .
```

### From PyPI (once published)
```bash
pip install embeddingframework
```

## 🛠 Usage

### Command-Line Interface

```bash
embeddingframework \
  --files path/to/file1.txt path/to/file2.pdf \
  --vector-db chroma \
  --embedding-model openai \
  --chunk-size 1048576 \
  --text-chunk-size 500 \
  --merge-target-size 1000 \
  --parallel \
  --file-parallel \
  --bandwidth-limit 1024 \
  --cloud-storage s3 \
  --bucket-name my-bucket \
  --cloud-credentials /path/to/credentials
```

### As a Python Module

```python
from embeddingframework.processors.file_processor import FileProcessor
from embeddingframework.adapters.openai_embedding_adapter import OpenAIEmbeddingAdapter
from embeddingframework.adapters.vector_dbs import ChromaDBAdapter
import asyncio

async def run():
    processor = FileProcessor(
        adapter=OpenAIEmbeddingAdapter(),
        vector_db=ChromaDBAdapter()
    )
    await processor.process_files(
        file_paths=["example.txt"],
        chunk_size=1024*1024,
        text_chunk_size=500
    )

asyncio.run(run())
```

### Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `--files` | List of file paths to process | **Required** |
| `--vector-db` | Vector DB backend (`chroma`, `pinecone`, `weaviate`, `milvus`) | `chroma` |
| `--embedding-model` | Embedding model (`openai`) | `openai` |
| `--chunk-size` | Binary chunk size in bytes | `1048576` |
| `--text-chunk-size` | Text chunk size in characters | `500` |
| `--merge-target-size` | Merge smaller chunks into this size | `None` |
| `--parallel` | Enable parallel chunk processing | `False` |
| `--file-parallel` | Enable parallel file processing | `False` |
| `--bandwidth-limit` | Max bytes/sec for streaming | `None` |
| `--cloud-storage` | Cloud storage backend (`s3`, `gcs`, `azure`) | `None` |
| `--bucket-name` | Bucket/container name for cloud storage | `None` |
| `--cloud-credentials` | Path or connection string for cloud storage credentials | `None` |

## 🧩 Architecture

```
embeddingframework/
├── adapters/         # Vector DB and embedding model adapters
├── processors/       # File processing logic
├── utils/            # Utility functions (splitters, preprocessing, retry)
└── embeddingframework.py  # CLI entry point
```

- **Adapters**: Abstract interfaces for embedding models and vector DBs.
- **Processors**: Handle file streaming, chunking, preprocessing, and storage.
- **Utils**: Helper functions for splitting, cleaning, and retrying operations.

## 📚 Extending the Framework

- **Add a new embedding model**: Implement `EmbeddingAdapter` in `adapters/`.
- **Add a new vector DB**: Implement `VectorDBAdapter` in `adapters/`.
- **Add a new cloud storage**: Implement storage adapter in `adapters/storage/`.

## 🧪 Testing & Code Coverage

Run the test suite:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=embeddingframework --cov-report=term-missing
```

Generate HTML coverage report:
```bash
pytest --cov=embeddingframework --cov-report=html
open htmlcov/index.html
```

## 📜 License

This project is licensed under the [MIT License](LICENSE).

## ✨ Example Workflow

1. **Select Embedding Model**: Choose `openai` or implement your own.
2. **Select Vector DB**: Choose from supported DBs or add a new one.
3. **Process Files**: Stream, split, merge, filter, preprocess, embed, and store.
4. **Store in Cloud** *(optional)*: Save processed files or embeddings to cloud storage.


