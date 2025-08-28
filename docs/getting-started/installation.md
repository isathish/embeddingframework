# Installation

This guide will help you install **EmbeddingFramework** on your system.

---

## 📦 Basic Installation

To install the latest stable release from PyPI:

```bash
pip install embeddingframework
```

---

## 🛠 Development Installation

If you want to contribute or run the latest development version:

```bash
git clone https://github.com/isathish/embeddingframework.git
cd embeddingframework
pip install -e .[dev]
```

This will install the package in **editable mode** along with development dependencies.

---

## ⚙️ Optional Dependencies

EmbeddingFramework supports multiple vector databases and cloud storage providers.  
You can install optional dependencies as needed:

```bash
# Pinecone
pip install embeddingframework[pinecone]

# AWS S3
pip install embeddingframework[s3]

# Google Cloud Storage
pip install embeddingframework[gcs]

# Azure Blob Storage
pip install embeddingframework[azure]
```

---

## ✅ Verifying Installation

Run the following command to verify the installation:

```bash
python -m embeddingframework --help
```

If installed correctly, you should see the CLI help message.
