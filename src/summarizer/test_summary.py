from contract_summarizer import summarize_contract

from preprocessing.pdf_reader import extract_text


pdf_path = "data/raw/contract.pdf"

pages = extract_text(pdf_path)

contract_text = ""

for page in pages:

    contract_text += page["text"] + "\n"


summary = summarize_contract(contract_text)

print(summary)