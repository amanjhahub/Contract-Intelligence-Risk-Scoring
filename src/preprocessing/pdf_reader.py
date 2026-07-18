from text_cleaner import clean_text
import pdfplumber

with pdfplumber.open("data/raw/contract.pdf") as pdf:
    full_text = ""

    for page in pdf.pages:
        text = page.extract_text()
        full_text += text + "\n"

cleaned_text = clean_text(full_text)

print(cleaned_text)