<h1 align="center">📂 File Processing</h1>

<p align="center">
  <b>Powerful capabilities to prepare data for embedding generation</b>
</p>

---

EmbeddingFramework includes powerful file processing capabilities to prepare data for embedding generation.

---

## 📂 Features

- **Automatic File Type Detection** – Detects file formats before processing.
- **Text Extraction** – Extracts text from multiple file types (e.g., `.txt`, `.pdf`, `.docx`, `.csv`, `.xls`, `.xlsx`).
- **Preprocessing** – Cleans and normalizes text for better embedding quality.
- **Text Splitting** – Splits large documents into smaller chunks for optimal embedding performance.
- **Large Dataset Handling** – Efficiently processes large Excel files by chunking rows into manageable segments without breaking embedding context.

---

## 🛠 Example Usage

```python
from embeddingframework.processors.file_processor import FileProcessor

processor = FileProcessor()

# Process a text file
text_data = processor.process_file("example.txt")
print(text_data)

# Process an Excel file with large dataset handling
excel_data = processor.process_file("large_dataset.xlsx")
print(excel_data)
```

---

## 🔄 Customization

You can customize:
- **Split size** for chunking text.
- **Preprocessing rules** for cleaning text.
- **Supported file types** by extending the processor.

---

## 📚 Related
<p align="center">
  <a href="embedding-providers.md">Embedding Providers</a> •
  <a href="utilities.md">Utilities</a>
</p>
- [Embedding Providers](embedding-providers.md)
- [Utilities](utilities.md)
