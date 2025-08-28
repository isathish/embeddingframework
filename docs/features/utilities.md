# Utilities

EmbeddingFramework provides a set of utility functions and helpers to make working with embeddings, files, and APIs easier.

---

## 🛠 Available Utilities

### 1️⃣ Retry Logic
- Automatically retries failed API calls.
- Configurable retry count and delay.

**Example:**
```python
from embeddingframework.utils.retry import retry

@retry(max_attempts=3, delay=2)
def unstable_function():
    # Your code here
    pass
```

---

### 2️⃣ File Utilities
- Safe file reading and writing.
- Path handling and validation.

**Example:**
```python
from embeddingframework.utils.file_utils import read_file

content = read_file("example.txt")
print(content)
```

---

### 3️⃣ Text Splitters
- Split text into chunks for embedding.
- Configurable chunk size and overlap.

**Example:**
```python
from embeddingframework.utils.splitters import split_text

chunks = split_text("Long text here...", chunk_size=500, overlap=50)
```

---

## 📚 Related
- [File Processing](file-processing.md)
- [Embedding Providers](embedding-providers.md)
