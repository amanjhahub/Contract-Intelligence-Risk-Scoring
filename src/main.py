import os

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
    search_index,
    save_index,
    load_index
)

from vector_store.metadata_store import (
    save_chunks,
    load_chunks
)


def main():

    pdf_path = "data/raw/contract.pdf"

    index_path = "data/vector_store/contract.index"
    chunks_path = "data/vector_store/chunks.pkl"


    # Step 1: Load existing vector store or create new one

    if os.path.exists(index_path) and os.path.exists(chunks_path):

        print("Loading existing vector store...")

        index = load_index(index_path)

        chunks = load_chunks(chunks_path)


    else:

        print("Creating new vector store...")


        # Step 2: Read PDF

        print("Reading PDF...")
        text = extract_text(pdf_path)


        # Step 3: Clean text

        print("Cleaning text...")

        for page in text:
            page["text"] = clean_text(
                page["text"]
            )

        cleaned_pages = text

        # Step 4: Create chunks

        print("Creating chunks...")

        chunks = chunk_text(
            cleaned_pages,
            chunk_size=50,
            overlap=10
        )


        # Extract only text for embeddings

        chunk_texts = []

        for chunk in chunks:
            chunk_texts.append(
                chunk["text"]
            )


        # Step 5: Generate embeddings

        print("Generating embeddings...")

        embeddings = generate_embeddings(
            chunk_texts
        )


        # Step 6: Build FAISS index

        print("Building FAISS index...")

        index = build_index(
            embeddings
        )


        # Step 7: Save vector store

        print("Saving vector store...")


        save_index(
            index,
            index_path
        )


        save_chunks(
            chunks,
            chunks_path
        )


    print(
        f"\nTotal Chunks Stored: {index.ntotal}"
    )


    # Step 8: User query

    query = input(
        "\nAsk a question: "
    )


    # Step 9: Generate query embedding

    query_embedding = model.encode(
        [query]
    )


    # Step 10: Search FAISS

    distances, indices = search_index(
        index,
        query_embedding,
        k=3
    )


    # Step 11: Retrieve chunks

    retrieved_chunks = []

    sources = []


    for idx in indices[0]:

        chunk = chunks[idx]

        retrieved_chunks.append(
            chunk["text"]
        )

        sources.append(
            f"Page {chunk['page']}, Chunk {chunk['chunk_id']}"
        )


    context = "\n\n".join(
        retrieved_chunks
    )


    # Step 12: Generate answer

    answer = generate_answer(
        context=context,
        question=query
    )
    not_found_message = "I could not find the answer in the provided document."

    if not_found_message in answer:

     sources = []


    # Step 13: Display result

    print("\nAnswer:\n")

    print(answer)


    if sources:

     print("\nSources:")

    for source in sources:
        print(source)


if __name__ == "__main__":
    main()