import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sample chunks
chunks = [
    "The contractor shall complete the project.",
    "Payment shall be made within 30 days.",
    "The agreement may be terminated by either party."
]

# Generate embeddings
embeddings = model.encode(chunks)

# Convert to float32 (FAISS requires float32)
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add embeddings to the index
index.add(embeddings)

print("Vectors stored:", index.ntotal)

# User query
query = "When should payment be made?"

# Generate query embedding
query_embedding = model.encode([query])
query_embedding = np.array(query_embedding).astype("float32")

# Search
distances, indices = index.search(query_embedding, 1)

print("Nearest Index:", indices)
print("Distance:", distances)

# Retrieve matching chunk
print("\nRetrieved Chunk:")
print(chunks[indices[0][0]])