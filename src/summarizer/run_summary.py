from summarizer.contract_summarizer import summarize_contract
from preprocessing.pdf_reader import extract_text


def run_summary():

    pdf_path = "data/raw/contract.pdf"

    print("Reading contract...")

    pages = extract_text(pdf_path)

    contract_text = ""

    for page in pages:

        if page["text"]:

            contract_text += page["text"] + "\n"

    print("\nGenerating summary...\n")

    summary = summarize_contract(contract_text)

    print(summary)


if __name__ == "__main__":

    run_summary()