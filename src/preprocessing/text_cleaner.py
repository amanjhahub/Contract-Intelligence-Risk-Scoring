import re


def clean_text(text):

    # Convert lowercase
    text = text.lower()

    # Keep useful characters like emails and URLs
    text = re.sub(
        r'[^a-zA-Z0-9@._\-\s]',
        '',
        text
    )

    # Remove extra spaces
    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    return text.strip()