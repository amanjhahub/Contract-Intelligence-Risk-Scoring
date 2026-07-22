from pdf_reader import extract_text

text = extract_text("data/raw/contract.pdf")

print(text[:300])