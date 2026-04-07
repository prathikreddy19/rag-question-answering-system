from app.retriever import retrieve, store_embeddings
from app.generator import generate_answer

# Load DB once
store_embeddings()

def answer_query(query):
    contexts = retrieve(query)
    return generate_answer(query, contexts)