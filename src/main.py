from preprocessing.pdf_reader import extract_text
from preprocessing.text_cleaner import clean_text
from preprocessing.text_chunker import chunk_text

from embeddings.embedding_generator import (
    generate_embeddings,
    model
)

from vector_store.faiss_index import (
    build_index,
    search_index
)


def main():

    # PDF Path
    pdf_path = "data/raw/contract.pdf"

    # Step 1: Read PDF
    print("Reading PDF...")
    text = extract_text(pdf_path)

    # Step 2: Clean Text
    print("Cleaning text...")
    cleaned_text = clean_text(text)

    # Step 3: Create Chunks
    print("Creating chunks...")
    chunks = chunk_text(
        cleaned_text,
        chunk_size=50,
        overlap=10
    )

    # Step 4: Generate Embeddings
    print("Generating embeddings...")
    embeddings = generate_embeddings(chunks)

    # Step 5: Build FAISS Index
    print("Building FAISS index...")
    index = build_index(embeddings)

    print(f"\nTotal Chunks Stored: {index.ntotal}")

    # Step 6: Ask User Query
    query = input("\nAsk a question: ")

    # Step 7: Generate Query Embedding
    query_embedding = model.encode([query])

    # Step 8: Search Top 3 Relevant Chunks
    distances, indices = search_index(
        index,
        query_embedding,
        k=3
    )

    # Step 9: Display Results
    print("\nTop 3 Relevant Chunks:\n")

    for rank, idx in enumerate(indices[0], start=1):
        print(f"Chunk {rank}:")
        print(chunks[idx])
        print("-" * 80)


if __name__ == "__main__":
    main()