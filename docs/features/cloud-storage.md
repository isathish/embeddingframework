# Cloud Storage

EmbeddingFramework supports integration with major cloud storage providers for storing and retrieving embeddings or related data.

---

## ☁️ Supported Providers

### 1️⃣ AWS S3
- Scalable object storage.
- Ideal for storing large datasets and backups.
- Requires AWS credentials.

**Example:**
```python
from embeddingframework.adapters.storage.s3_storage_adapter import S3StorageAdapter

storage = S3StorageAdapter(bucket_name="my-bucket", aws_access_key_id="KEY", aws_secret_access_key="SECRET")
storage.upload_file("local_file.txt", "remote_file.txt")
```

---

### 2️⃣ Google Cloud Storage (GCS)
- Highly available and durable storage.
- Requires GCP credentials.

**Example:**
```python
from embeddingframework.adapters.storage.gcs_storage_adapter import GCSStorageAdapter

storage = GCSStorageAdapter(bucket_name="my-bucket", credentials_path="path/to/credentials.json")
storage.upload_file("local_file.txt", "remote_file.txt")
```

---

### 3️⃣ Azure Blob Storage
- Enterprise-grade cloud storage.
- Requires Azure credentials.

**Example:**
```python
from embeddingframework.adapters.storage.azure_blob_storage_adapter import AzureBlobStorageAdapter

storage = AzureBlobStorageAdapter(container_name="my-container", connection_string="AZURE_CONNECTION_STRING")
storage.upload_file("local_file.txt", "remote_file.txt")
```

---

## 🔄 Switching Providers

The API is consistent across all storage adapters, so switching between providers is as simple as changing the adapter import and initialization.

---

## 📚 Related
- [Vector Databases](vector-databases.md)
- [Embedding Providers](embedding-providers.md)
