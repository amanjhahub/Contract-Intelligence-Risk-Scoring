import pdfplumber

from text_cleaner import clean_text
from text_chunker import chunk_text


with pdfplumber.open("data/raw/contract.pdf") as pdf:

    full_text = ""

    for page in pdf.pages:
        text = page.extract_text()
        full_text += text + "\n"


cleaned_text = clean_text(full_text)


chunks = chunk_text(
    cleaned_text,
    chunk_size=50,
    overlap=10
)


for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk {i}:")
    print(chunk)
    print("-" * 50)