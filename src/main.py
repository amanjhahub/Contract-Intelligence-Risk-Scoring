import os

from risk.risk_analyzer import analyze_risk
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

    # -------------------------------------------------
    # Read PDF (Always)
    # -------------------------------------------------

    print("Reading PDF...")

    pages = extract_text(pdf_path)

    # -------------------------------------------------
    # Risk Analysis
    # -------------------------------------------------

    contract_text = ""

    for page in pages:

        if page["text"]:

            contract_text += page["text"] + "\n"

    risk_report = analyze_risk(contract_text)

    # -------------------------------------------------
    # Load existing vector store OR create one
    # -------------------------------------------------

    if os.path.exists(index_path) and os.path.exists(chunks_path):

        print("Loading existing vector store...")

        index = load_index(index_path)

        chunks = load_chunks(chunks_path)

    else:

        print("Creating new vector store...")

        print("Cleaning text...")

        for page in pages:

            page["text"] = clean_text(
                page["text"]
            )

        print("Creating chunks...")

        chunks = chunk_text(
            pages,
            chunk_size=50,
            overlap=10
        )

        chunk_texts = []

        for chunk in chunks:

            chunk_texts.append(
                chunk["text"]
            )

        print("Generating embeddings...")

        embeddings = generate_embeddings(
            chunk_texts
        )

        print("Building FAISS index...")

        index = build_index(
            embeddings
        )

        print("Saving vector store...")

        save_index(
            index,
            index_path
        )

        save_chunks(
            chunks,
            chunks_path
        )

    print(f"\nTotal Chunks Stored: {index.ntotal}")

    # -------------------------------------------------
    # Display Risk Report
    # -------------------------------------------------

    print("\n==============================")
    print("Contract Risk Report")
    print("==============================")

    print(f"Risk Score : {risk_report['risk_score']}")
    print(f"Risk Level : {risk_report['risk_level']}")

    print("\nPresent Clauses")

    for clause in risk_report["present"]:

        print(
            f"✓ {clause['clause']} ({clause['severity']})"
        )

    print("\nMissing Clauses")

    for clause in risk_report["missing"]:

        print(
            f"✗ {clause['clause']} ({clause['severity']})"
        )

    # -------------------------------------------------
    # Ask Question
    # -------------------------------------------------

    query = input("\nAsk a question: ")

    query_embedding = model.encode([query])

    distances, indices = search_index(
        index,
        query_embedding,
        k=3
    )

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

    context = "\n\n".join(retrieved_chunks)

    answer = generate_answer(
        context=context,
        question=query
    )

    not_found = "I could not find the answer in the provided document."

    if not_found.lower() in answer.lower():

        sources = []

    print("\nAnswer:\n")

    print(answer)

    if sources:

        print("\nSources:")

        for source in sources:

            print(source)


if __name__ == "__main__":
    main()