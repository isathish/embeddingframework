# 🚀 Advanced Usage Example

This guide demonstrates a **full end-to-end workflow** using EmbeddingFramework with advanced features.

---

## 1️⃣ Install the package
```bash
pip install embeddingframework
```

---

## 2️⃣ Import required modules
```python
from embeddingframework.adapters.openai_embedding_adapter import OpenAIEmbeddingAdapter
from embeddingframework.adapters.vector_dbs import MilvusAdapter
from embeddingframework.processors.file_processor import FileProcessor
```

---

## 3️⃣ Initialize components
```python
embedding_provider = OpenAIEmbeddingAdapter(api_key="YOUR_OPENAI_API_KEY")
vector_db = MilvusAdapter(host="localhost", port="19530")
processor = FileProcessor()
```

---

## 4️⃣ Process files
```python
text = processor.process_file("sample.pdf")
```

---

## 5️⃣ Generate embeddings
```python
embeddings = embedding_provider.embed_texts([text])
```

---

## 6️⃣ Store embeddings
```python
vector_db.add_texts([text], embeddings)
```

---

## 7️⃣ Query the database
```python
results = vector_db.query("search term", top_k=5)
print(results)
```

---

## ✅ Summary
You have successfully:
- Processed a file
- Generated embeddings
- Stored them in a distributed vector database
- Queried the database for semantic search
