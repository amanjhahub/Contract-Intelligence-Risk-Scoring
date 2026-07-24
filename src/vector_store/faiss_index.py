import faiss
import numpy as np
import os


def build_index(embeddings):

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index



def search_index(index, query_embedding, k=3, threshold=2.0):

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



def load_index(path):

    index = faiss.read_index(path)

    return index