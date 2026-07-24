import pickle
import os


def save_chunks(chunks, path):

    directory = os.path.dirname(path)

    if directory:
        os.makedirs(
            directory,
            exist_ok=True
        )

    with open(path, "wb") as file:
        pickle.dump(
            chunks,
            file
        )


def load_chunks(path):

    with open(path, "rb") as file:
        chunks = pickle.load(file)

    return chunks