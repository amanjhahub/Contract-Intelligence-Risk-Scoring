import os

from recommendations.recommendation_engine import generate_recommendations
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

from utils.logger import logger


def main():

    try:

        logger.info("========== Contract Intelligence Pipeline Started ==========")

        pdf_path = "data/raw/contract.pdf"

        index_path = "data/vector_store/contract.index"
        chunks_path = "data/vector_store/chunks.pkl"

        # -------------------------------------------------
        # Read PDF
        # -------------------------------------------------

        print("Reading PDF...")
        logger.info("Reading PDF...")

        pages = extract_text(pdf_path)

        logger.info(f"Extracted {len(pages)} pages.")

        # -------------------------------------------------
        # Risk Analysis
        # -------------------------------------------------

        logger.info("Running risk analysis...")

        contract_text = ""

        for page in pages:

            if page["text"]:

                contract_text += page["text"] + "\n"

        risk_report = analyze_risk(contract_text)

        recommendations = generate_recommendations(
            risk_report
        )

        logger.info(
            f"Risk Score: {risk_report['risk_score']} | Risk Level: {risk_report['risk_level']}"
        )

        # -------------------------------------------------
        # Load existing vector store OR create new one
        # -------------------------------------------------

        if os.path.exists(index_path) and os.path.exists(chunks_path):

            print("Loading existing vector store...")
            logger.info("Loading existing FAISS vector store...")

            index = load_index(index_path)

            chunks = load_chunks(chunks_path)

           

        else:

            print("Creating new vector store...")
            logger.info("Creating new vector store...")

            print("Cleaning text...")
            logger.info("Cleaning extracted text...")

            for page in pages:

                page["text"] = clean_text(
                    page["text"]
                )

            print("Creating chunks...")
            logger.info("Creating chunks...")

            chunks = chunk_text(
                pages,
                chunk_size=50,
                overlap=10
            )

            logger.info(f"Created {len(chunks)} chunks.")

            chunk_texts = []

            for chunk in chunks:

                chunk_texts.append(
                    chunk["text"]
                )

            print("Generating embeddings...")
            logger.info("Generating embeddings...")

            embeddings = generate_embeddings(
                chunk_texts
            )

            logger.info(
                f"Generated {len(embeddings)} embeddings."
            )

            print("Building FAISS index...")
            logger.info("Building FAISS index...")

            index = build_index(
                embeddings
            )

            logger.info(
                f"FAISS index built with {index.ntotal} vectors."
            )

            print("Saving vector store...")
            logger.info("Saving FAISS vector store...")

            save_index(
                index,
                index_path
            )

            save_chunks(
                chunks,
                chunks_path
            )

            logger.info("Vector store saved successfully.")

        print(f"\nTotal Chunks Stored: {index.ntotal}")

        logger.info(
            f"Total chunks stored: {index.ntotal}"
        )

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
        # Recommendations
        # -------------------------------------------------

        print("\n==============================")
        print("Contract Recommendations")
        print("==============================")

        for item in recommendations:

            print(
                f"{item['priority']} : {item['clause']}"
            )

            print(
                item["message"]
            )

            print()

        # -------------------------------------------------
        # Question Answering
        # -------------------------------------------------

        logger.info("Waiting for user query...")

        query = input("\nAsk a question: ")

        logger.info(f"User Query: {query}")

        query_embedding = model.encode(
            [query]
        )

        

        distances, indices = search_index(
            index,
            query_embedding,
            k=3
        )

        logger.info(
            f"Retrieved {len(indices[0])} candidate chunks."
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

        context = "\n\n".join(
            retrieved_chunks
        )

        logger.info("Generating answer using Gemini...")

        answer = generate_answer(
            context=context,
            question=query
        )

        logger.info("Answer generated successfully.")

        not_found = (
            "I could not find the answer in the provided document."
        )

        if not_found.lower() in answer.lower():

            sources = []

        print("\nAnswer:\n")

        print(answer)

        if sources:

            print("\nSources:")

            for source in sources:

                print(source)

        logger.info("========== Pipeline Completed Successfully ==========")

    except Exception as e:

        logger.exception(f"Pipeline failed: {e}")

        raise


def run_single_contract():

    main()


if __name__ == "__main__":

    run_single_contract()