import os

from embeddings.embedding_generator import model

from vector_store.faiss_index import (
    search_index,
    load_index
)

from vector_store.metadata_store import (
    load_chunks
)

from llm.gemini_client import generate_answer


index_path = "data/vector_store/contract.index"
chunks_path = "data/vector_store/chunks.pkl"


index = load_index(index_path)

chunks = load_chunks(chunks_path)


def ask_contract(question):

    query_embedding = model.encode(
        [question]
    )


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


    context = "\n\n".join(
        retrieved_chunks
    )


    answer = generate_answer(
        context=context,
        question=question
    )


    not_found = (
        "I could not find the answer in the provided document."
    )


    if not_found.lower() in answer.lower():

        sources = []


    return {

        "answer": answer,

        "sources": sources

    }