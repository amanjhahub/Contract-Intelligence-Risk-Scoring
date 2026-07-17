import re


def clean_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


if __name__ == "__main__":

    sample_contract = """
    The Contractor shall complete the project
    within 30 days. Failure to comply will result
    in penalty charges.
    """

    cleaned = clean_text(sample_contract)

    print("Original:")
    print(sample_contract)

    print("\nCleaned:")
    print(cleaned)

