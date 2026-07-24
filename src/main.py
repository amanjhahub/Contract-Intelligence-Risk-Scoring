from llm.gemini_client import generate_answer

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

    pdf_path = "data/raw/contract.pdf"

    print("Reading PDF...")
    pages = extract_text(pdf_path)


    print("Cleaning text...")

    for page in pages:
        page["text"] = clean_text(page["text"])


    print("Creating chunks...")

    chunks = chunk_text(
        pages,
        chunk_size=50,
        overlap=10
    )


    # Extract only text for embeddings

    chunk_texts = [
        chunk["text"]
        for chunk in chunks
    ]


    print("Generating embeddings...")

    embeddings = generate_embeddings(chunk_texts)


    print("Building FAISS index...")

    index = build_index(embeddings)


    print(f"\nTotal Chunks Stored: {index.ntotal}")


    query = input("\nAsk a question: ")


    query_embedding = model.encode([query])


    distances, indices = search_index(
        index,
        query_embedding,
        k=3
    )


    # Prepare context for Gemini

    retrieved_chunks = []

    sources = []


    for idx in indices[0]:

        retrieved_chunks.append(
            chunks[idx]["text"]
        )

        sources.append({
            "page": chunks[idx]["page"],
            "chunk_id": chunks[idx]["chunk_id"]
        })


    context = "\n\n".join(retrieved_chunks)


    answer = generate_answer(
        context=context,
        question=query
    )


    print("\nAnswer:\n")
    print(answer)


    print("\nSources:")

    for source in sources:
        print(
            f"Page {source['page']}, Chunk {source['chunk_id']}"
        )


if __name__ == "__main__":
    main()