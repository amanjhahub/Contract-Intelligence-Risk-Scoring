def chunk_text(pages, chunk_size, overlap):

    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk size")

    chunks = []

    chunk_id = 1

    step = chunk_size - overlap

    for page in pages:

        words = page["text"].split()

        for i in range(0, len(words), step):

            chunk = " ".join(words[i:i + chunk_size])

            chunks.append({
                "chunk_id": chunk_id,
                "page": page["page"],
                "text": chunk
            })

            chunk_id += 1

    return chunks
if __name__ == "__main__":

    sample_pages = [
        {
            "page": 1,
            "text": "the contractor shall complete the project within 30 days payment shall be made"
        },
        {
            "page": 2,
            "text": "agreement may be terminated by either party"
        }
    ]

    result = chunk_text(sample_pages, 5, 2)

    for chunk in result:
        print(chunk)
        print("-" * 40)