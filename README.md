# RAG Question Answering System

This project implements a simple **Retrieval-Augmented Generation (RAG)** pipeline from scratch.
It combines semantic search (via embeddings) with a local language model (**FLAN-T5**) to answer questions based on context.

---

## Overview

The goal of this project is to answer user queries by:

1. Finding the most relevant text chunks from a dataset
2. Passing those chunks to a language model
3. Generating a context-aware answer

---

## How it works

```
User Query
   ↓
Embedding (SentenceTransformer)
   ↓
Similarity Search (ChromaDB)
   ↓
Top relevant chunks
   ↓
FLAN-T5 (generation)
   ↓
Final Answer
```

---

## Features

* Semantic search using vector embeddings
* Context-based question answering
* Fully local (no external APIs required)
* Modular code structure (easy to extend)
* Works with real-world dataset (SQuAD v2)

---

## Tech Stack

* Python
* SentenceTransformers (`all-MiniLM-L6-v2`)
* ChromaDB
* HuggingFace Transformers (FLAN-T5)
* SQuAD v2 dataset

---

## Project Structure

```
rag-project/
│
├── app/
│   ├── embedder.py
│   ├── retriever.py
│   ├── generator.py
│   ├── rag.py
│
├── data/                # not included in repo
├── notebook/
│   └── rag_pipeline.ipynb
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/rag-question-answering-system.git
cd rag-question-answering-system
pip install -r requirements.txt
```

---

## Run

```bash
python main.py
```

Example:

```
Ask a question: Who is Beyonce?
Answer: Beyoncé is an American singer, songwriter, and actress.
```

---

## Dataset

This project uses **SQuAD v2**.

The dataset is:

* cleaned
* split into chunks
* converted into embeddings
* stored for retrieval

Note:
Large files (like embeddings) are not included in the repo.
You can regenerate them using the notebook.

---

## Limitations

* FLAN-T5 (local) is smaller than modern LLMs, so answers may not always be perfect
* Retrieval depends on chunk quality
* No reranking yet (can be improved)

---

## Possible Improvements

* Add reranking for better retrieval
* Improve chunking strategy
* Add a web interface (Streamlit / React)
* Use a stronger LLM for better generation

