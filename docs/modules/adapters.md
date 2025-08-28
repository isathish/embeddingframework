# 🧩 Adapters Module

The **Adapters** module in EmbeddingFramework provides integration layers for various **Vector Databases** and **Cloud Storage Providers**.

---

## 📦 Vector Database Adapters

### Supported Databases:
- **ChromaDB** – Local, persistent vector storage.
- **Milvus** – High-performance distributed vector database.
- **Pinecone** – Fully managed vector database service.
- **Weaviate** – Open-source vector search engine.

Example:
```python
from embeddingframework.adapters.vector_dbs import ChromaDBAdapter

db = ChromaDBAdapter(persist_directory="./chroma_store")
db.add_texts(["Hello"], [[0.1, 0.2, 0.3]])
```

---

## ☁️ Cloud Storage Adapters

### Supported Providers:
- **AWS S3**
- **Google Cloud Storage**
- **Azure Blob Storage**

Example:
```python
from embeddingframework.adapters.storage.s3_storage_adapter import S3StorageAdapter

storage = S3StorageAdapter(bucket_name="my-bucket")
storage.upload_file("local.txt", "remote.txt")
```

---

## 🔌 Extending Adapters

You can create your own adapter by extending the base classes:
```python
from embeddingframework.adapters.base import BaseAdapter

class MyCustomAdapter(BaseAdapter):
    def connect(self):
        pass
