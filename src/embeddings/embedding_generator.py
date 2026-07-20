from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


chunks = [
    "the contractor shall complete the project",
    "payment shall be made within 30 days",
    "agreement may be terminated"
]


embeddings = []

for chunk in chunks:
    embedding = model.encode(chunk)
    embeddings.append(embedding)


print(type(embeddings))
print(len(embeddings))
print(embeddings[0].shape)