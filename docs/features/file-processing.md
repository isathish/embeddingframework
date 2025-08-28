# File Processing

EmbeddingFramework includes powerful file processing capabilities to prepare data for embedding generation.

---

## 📂 Features

- **Automatic File Type Detection** – Detects file formats before processing.
- **Text Extraction** – Extracts text from multiple file types (e.g., `.txt`, `.pdf`, `.docx`).
- **Preprocessing** – Cleans and normalizes text for better embedding quality.
- **Text Splitting** – Splits large documents into smaller chunks for optimal embedding performance.

---

## 🛠 Example Usage

```python
from embeddingframework.processors.file_processor import FileProcessor

processor = FileProcessor()
text_data = processor.process_file("example.txt")
print(text_data)
```

---

## 🔄 Customization

You can customize:
- **Split size** for chunking text.
- **Preprocessing rules** for cleaning text.
- **Supported file types** by extending the processor.

---

## 📚 Related
- [Embedding Providers](embedding-providers.md)
- [Utilities](utilities.md)
