def create_chunks(pages, chunk_size=500):

    chunks = []

    for page in pages:

        text = page["text"]

        words = text.split()

        for i in range(0, len(words), chunk_size):

            chunk = " ".join(
                words[i:i+chunk_size]
            )

            chunks.append(chunk)

    return chunks