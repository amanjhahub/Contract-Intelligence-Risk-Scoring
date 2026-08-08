import faiss
import numpy as np
import os

from utils.logger import logger


def build_index(embeddings):

    logger.info("Building FAISS index...")

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    logger.info(
        f"FAISS index created successfully with {index.ntotal} vectors."
    )

    return index


def search_index(index, query_embedding, k=3, threshold=2.0):

    logger.info(
        f"Searching FAISS index (Top-{k}, Threshold={threshold})..."
    )

    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(
        query_embedding,
        k
    )

    filtered_indices = []
    filtered_distances = []

    for distance, idx in zip(distances[0], indices[0]):

        if distance <= threshold:
            filtered_indices.append(idx)
            filtered_distances.append(distance)

    logger.info(
        f"Search completed. Found {len(filtered_indices)} matching documents."
    )

    return (
        np.array([filtered_distances]),
        np.array([filtered_indices])
    )


def save_index(index, path):

    directory = os.path.dirname(path)

    if directory:
        os.makedirs(
            directory,
            exist_ok=True
        )

    faiss.write_index(
        index,
        path
    )

    logger.info(
        f"FAISS index saved at: {path}"
    )


def load_index(path):

    logger.info(
        f"Loading FAISS index from: {path}"
    )

    index = faiss.read_index(path)

    logger.info(
        f"Loaded FAISS index containing {index.ntotal} vectors."
    )

    return index