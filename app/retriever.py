import chromadb
import numpy as np
import json
from app.embedder import get_embedding

client = chromadb.Client()
collection = client.create_collection(name="rag_collection")

def load_data():
    embeddings = np.load("data/embeddings.npy", allow_pickle=True)

    with open("data/metadata.json", "r") as f:
        metadata = json.load(f)

    return embeddings, metadata


def store_embeddings():
    embeddings, metadata = load_data()

    batch_size = 100

    for i in range(0, len(embeddings), batch_size):
        batch_embeddings = embeddings[i:i+batch_size]
        batch_metadata = metadata[i:i+batch_size]

        collection.add(
            embeddings=[e.tolist() for e in batch_embeddings],
            documents=[m["chunk"] for m in batch_metadata],
            metadatas=[{"source": "squad"} for _ in batch_metadata],
            ids=[str(j) for j in range(i, i + len(batch_embeddings))]
        )


def retrieve(query, k=3):
    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=k
    )

    return results["documents"][0]