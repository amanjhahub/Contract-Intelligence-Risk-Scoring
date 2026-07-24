import pdfplumber


def extract_text(pdf_path):

    pages = []

    with pdfplumber.open(pdf_path) as pdf:

        for page_number, page in enumerate(pdf.pages, start=1):

            text = page.extract_text()

            if text:
                pages.append({
                    "page": page_number,
                    "text": text
                })

    return pages