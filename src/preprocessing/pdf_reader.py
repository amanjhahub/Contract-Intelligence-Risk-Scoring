import pdfplumber
import pytesseract

from pdf2image import convert_from_path


def extract_text(pdf_path):

    pages = []

    # Try extracting normal PDF text first
    with pdfplumber.open(pdf_path) as pdf:

        for page_number, page in enumerate(pdf.pages, start=1):

            text = page.extract_text()

            if text and text.strip():

                pages.append({
                    "page": page_number,
                    "text": text
                })


    # Return extracted text if PDF already contains text
    if pages:
     print("Text extracted directly from PDF")
     return pages


    # OCR fallback for scanned PDFs
    print("No text found. Running OCR...")

    images = convert_from_path(pdf_path)


    for page_number, image in enumerate(images, start=1):

        text = pytesseract.image_to_string(image)

        pages.append({
            "page": page_number,
            "text": text
        })


    return pages