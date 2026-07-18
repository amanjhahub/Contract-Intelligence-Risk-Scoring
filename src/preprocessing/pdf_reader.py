import pdfplumber

with pdfplumber.open("data/raw/contract.pdf") as pdf:
    full_text = ""

    for page in pdf.pages:
        text = page.extract_text()
        full_text += text + "\n"

print(full_text)