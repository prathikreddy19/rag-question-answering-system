from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


def generate_answer(query, contexts):
    context_text = "\n\n".join(contexts[:2])

    prompt = f"""
Answer the question using the context below.

Context:
{context_text}

Question: {query}

Answer:
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)

    outputs = model.generate(
        **inputs,
        max_new_tokens=100
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)