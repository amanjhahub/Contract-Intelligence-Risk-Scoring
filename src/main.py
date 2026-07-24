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
    text = extract_text(pdf_path)

    print("Cleaning text...")
    cleaned_text = clean_text(text)

    print("Creating chunks...")
    chunks = chunk_text(
        cleaned_text,
        chunk_size=50,
        overlap=10
    )

    print("Generating embeddings...")
    embeddings = generate_embeddings(chunks)

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


    # Step 9: Prepare Context for Gemini

    retrieved_chunks = []

    for idx in indices[0]:
        retrieved_chunks.append(chunks[idx])

    context = "\n\n".join(retrieved_chunks)


    # Step 10: Generate Answer using Gemini

    answer = generate_answer(
        context=context,
        question=query
    )


    # Step 11: Display Answer

    print("\nAnswer:\n")
    print(answer)



if __name__ == "__main__":
    main()