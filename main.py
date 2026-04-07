from app.rag import answer_query

while True:
    query = input("\nAsk a question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    answer = answer_query(query)
    print("\nAnswer:", answer)