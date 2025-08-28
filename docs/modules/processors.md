# ⚙️ Processors Module

The **Processors** module in EmbeddingFramework handles **file ingestion, text extraction, and preprocessing** before generating embeddings.

---

## 📂 File Processing

The `FileProcessor` class automatically detects file types and extracts text from:
- **TXT**
- **PDF**
- **DOCX**
- Other supported formats

Example:
```python
from embeddingframework.processors.file_processor import FileProcessor

processor = FileProcessor()
text = processor.process_file("document.pdf")
print(text)
```

---

## 🧹 Preprocessing

Preprocessing utilities help clean and normalize text for better embedding quality:
- Remove special characters
- Normalize whitespace
- Lowercasing
- Tokenization

Example:
```python
from embeddingframework.utils.preprocessing import clean_text

cleaned = clean_text("Hello,   World!!!")
print(cleaned)  # "hello world"
```

---

## ✂️ Text Splitting

The framework includes intelligent text splitters for optimal embedding performance:
```python
from embeddingframework.utils.splitters import split_text

chunks = split_text("Long text...", chunk_size=500)
```

---

## 🔌 Extending Processors

You can create custom processors by extending the base processor class.
