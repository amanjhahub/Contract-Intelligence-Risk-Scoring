from preprocessing.pdf_reader import extract_text

from embeddings.chunking import create_chunks
from embeddings.embedding_generator import generate_embeddings

from vector_store.faiss_index import (
    build_index,
    search_index
)


# -------------------------------
# 1. Extract PDF text
# -------------------------------

pdf_path = "data/raw/contract.pdf"

pages = extract_text(pdf_path)

print("PDF extracted successfully")


# -------------------------------
# 2. Create text chunks
# -------------------------------

chunks = create_chunks(
    pages,
    chunk_size=200
)

print(f"Chunks created: {len(chunks)}")


# -------------------------------
# 3. Generate embeddings
# -------------------------------

embeddings = generate_embeddings(
    chunks
)

print("Embeddings generated")


# -------------------------------
# 4. Build FAISS vector index
# -------------------------------

index = build_index(
    embeddings
)

print("FAISS index created")


# -------------------------------
# 5. Semantic search
# -------------------------------

query = "What is the termination clause?"

print(f"\nQuery: {query}")


query_embedding = generate_embeddings(
    [query]
)


distances, indices = search_index(
    index,
    query_embedding,
    k=3
)


# -------------------------------
# 6. Display results
# -------------------------------

print("\nSearch Results:")
print("----------------")


for distance, idx in zip(
    distances[0],
    indices[0]
):

    print("\nScore:", distance)

    print("Chunk:")
    print(chunks[idx])

    print("----------------")