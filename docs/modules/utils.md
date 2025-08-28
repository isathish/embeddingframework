# 🛠️ Utils Module

The **Utils** module in EmbeddingFramework provides helper functions and utilities to support embedding workflows.

---

## 🔄 Retry Logic

Ensures robust API calls with automatic retries:
```python
from embeddingframework.utils.retry import retry

@retry(max_attempts=3)
def fetch_data():
    # API call logic
    pass
```

---

## 📁 File Utilities

Safe and efficient file I/O operations:
```python
from embeddingframework.utils.file_utils import read_file, write_file

content = read_file("data.txt")
write_file("output.txt", content)
```

---

## 🧹 Preprocessing

Text cleaning and normalization:
```python
from embeddingframework.utils.preprocessing import clean_text

text = clean_text("Hello,   World!!!")
```

---

## ✂️ Text Splitters

Split large text into smaller chunks for embedding:
```python
from embeddingframework.utils.splitters import split_text

chunks = split_text("Long text...", chunk_size=500)
```

---

## 🔌 Extending Utils

You can add your own utility functions to extend the framework's capabilities.
