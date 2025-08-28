<h1 align="center">☁️ Cloud Storage</h1>

<p align="center">
  <b>Integrate with major cloud storage providers for storing and retrieving embeddings or related data</b>
</p>

---

EmbeddingFramework supports integration with major cloud storage providers for storing and retrieving embeddings or related data.

---

## ☁️ Supported Providers

Below are the supported cloud storage providers with **detailed explanations**, **technical functions**, and **usage patterns**.

### 1️⃣ AWS S3
- Scalable object storage.
- Ideal for storing large datasets and backups.
- Requires AWS credentials.

**Technical Functions:**
- `__init__(bucket_name: str, aws_access_key_id: str, aws_secret_access_key: str)`: Initializes the S3 adapter with AWS credentials.
- `upload_file(local_path: str, remote_path: str)`: Uploads a file to the specified S3 bucket.
- `download_file(remote_path: str, local_path: str)`: Downloads a file from S3.
- `list_files(prefix: str = "")`: Lists files in the bucket.

**Example:**
```python
from embeddingframework.adapters.storage.s3_storage_adapter import S3StorageAdapter

storage = S3StorageAdapter(bucket_name="my-bucket", aws_access_key_id="KEY", aws_secret_access_key="SECRET")
storage.upload_file("local_file.txt", "remote_file.txt")
files = storage.list_files()
print(files)
```

---

### 2️⃣ Google Cloud Storage (GCS)
- Highly available and durable storage.
- Requires GCP credentials.

**Technical Functions:**
- `__init__(bucket_name: str, credentials_path: str)`: Initializes the GCS adapter with a bucket and credentials file.
- `upload_file(local_path: str, remote_path: str)`: Uploads a file to GCS.
- `download_file(remote_path: str, local_path: str)`: Downloads a file from GCS.
- `list_files(prefix: str = "")`: Lists files in the bucket.

**Example:**
```python
from embeddingframework.adapters.storage.gcs_storage_adapter import GCSStorageAdapter

storage = GCSStorageAdapter(bucket_name="my-bucket", credentials_path="path/to/credentials.json")
storage.upload_file("local_file.txt", "remote_file.txt")
files = storage.list_files()
print(files)
```

---

### 3️⃣ Azure Blob Storage
- Enterprise-grade cloud storage.
- Requires Azure credentials.

**Technical Functions:**
- `__init__(container_name: str, connection_string: str)`: Initializes the Azure Blob Storage adapter.
- `upload_file(local_path: str, remote_path: str)`: Uploads a file to Azure Blob Storage.
- `download_file(remote_path: str, local_path: str)`: Downloads a file from Azure Blob Storage.
- `list_files(prefix: str = "")`: Lists files in the container.

**Example:**
```python
from embeddingframework.adapters.storage.azure_blob_storage_adapter import AzureBlobStorageAdapter

storage = AzureBlobStorageAdapter(container_name="my-container", connection_string="AZURE_CONNECTION_STRING")
storage.upload_file("local_file.txt", "remote_file.txt")
files = storage.list_files()
print(files)
```

---

## 🔄 Switching Providers

The API is consistent across all storage adapters, so switching between providers is as simple as changing the adapter import and initialization.

---

## 📚 Related
<p align="center">
  <a href="vector-databases.md">Vector Databases</a> •
  <a href="embedding-providers.md">Embedding Providers</a>
</p>
- [Vector Databases](vector-databases.md)
- [Embedding Providers](embedding-providers.md)
