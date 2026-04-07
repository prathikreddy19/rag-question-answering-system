# 🚀 RAG Question Answering System

A **Retrieval-Augmented Generation (RAG)** system built from scratch using modern NLP techniques.
This project combines **semantic search (vector embeddings)** with a **local LLM (FLAN-T5)** to answer questions based on contextual data.

---

## 📌 Overview

This system allows users to ask natural language questions and retrieves the most relevant context from a dataset before generating accurate answers.

### 🔁 Pipeline Flow

```text
User Query
   ↓
Embedding (SentenceTransformer)
   ↓
Vector Search (ChromaDB)
   ↓
Top-K Relevant Chunks
   ↓
LLM (FLAN-T5)
   ↓
Final Answer
```

---

## 🧠 Key Features

* 🔍 Semantic search using vector embeddings
* 📚 Context-aware question answering
* ⚡ Fully local (no API required)
* 🧩 Modular architecture (easy to extend)
* 🗂 Handles large datasets via chunking
* 🧪 Built using real-world dataset (SQuAD v2)

---

## 🛠️ Tech Stack

| Component       | Technology                                |
| --------------- | ----------------------------------------- |
| Language        | Python                                    |
| Embeddings      | SentenceTransformers (`all-MiniLM-L6-v2`) |
| Vector Database | ChromaDB                                  |
| LLM             | FLAN-T5 (HuggingFace Transformers)        |
| Dataset         | SQuAD v2                                  |
| Environment     | VS Code / Jupyter / Colab                 |

---

## 📂 Project Structure

```
rag-project/
│
├── app/
│   ├── embedder.py      # Embedding generation
│   ├── retriever.py     # Vector DB + retrieval
│   ├── generator.py     # FLAN-T5 response generation
│   ├── rag.py           # Pipeline integration
│
├── data/                # (ignored in Git)
│   ├── embeddings.npy
│   ├── metadata.json
│
├── notebook/
│   └── rag_pipeline.ipynb   # Data preprocessing & experimentation
│
├── main.py              # CLI interface
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/rag-question-answering-system.git
cd rag-question-answering-system
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py
```

Then ask questions:

```text
Ask a question: Who is Beyonce?
Answer: Beyoncé is an American singer, songwriter, and actress.
```

---

## 📊 Dataset

* Source: **SQuAD v2 (Stanford Question Answering Dataset)**
* Data is:

  * cleaned
  * chunked
  * embedded
  * stored for retrieval

⚠️ Note:
Large files like embeddings are not included in the repo.
Run the notebook to regenerate them.

---

## 🧠 How It Works

### 1. Data Processing

* Extract context, question, and answer
* Chunk large passages into smaller segments

### 2. Embedding Generation

* Convert text chunks into dense vectors using SentenceTransformer

### 3. Storage

* Store embeddings in ChromaDB for fast similarity search

### 4. Retrieval

* Convert user query into embedding
* Retrieve top-k most relevant chunks

### 5. Generation

* Pass retrieved context into FLAN-T5
* Generate final answer

---

## ⚠️ Limitations

* Local model (FLAN-T5) may produce less accurate answers than large APIs
* Retrieval quality depends on chunking strategy
* No reranking (can be improved)

---

## 🚀 Future Improvements

* 🔼 Add reranking (improve accuracy)
* 🌐 Build web UI (Streamlit / React)
* ⚡ Optimize latency
* 🧠 Use stronger LLM (LLaMA / API-based)
* 💬 Add conversational memory

---

## 📸 Example

**Input:**

```
Who is Beyonce?
```

**Output:**

```
Beyoncé is an American singer, songwriter, and actress.
```

---

## 👨‍💻 Author

**Prathik Reddy**

* B.Tech Student
* Interested in AI, ML, and Full Stack Development

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub — it helps a lot!
