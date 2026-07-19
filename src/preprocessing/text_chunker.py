def chunk_text(text, chunk_size, overlap):
    words = text.split()
    if overlap >= chunk_size:
     raise ValueError("Overlap must be smaller than chunk size")
    chunks = []

    step = chunk_size - overlap

    for i in range(0, len(words), step):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


if __name__ == "__main__":

    sample_text = (
        "the contractor shall complete the project "
        "within 30 days payment shall be made after completion"
    )

    result = chunk_text(sample_text, 5, 2)

    for i, chunk in enumerate(result, start=1):
        print(f"Chunk {i}:")
        print(chunk)
        print("-" * 40)