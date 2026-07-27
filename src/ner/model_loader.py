import spacy


def load_spacy_model():

    nlp = spacy.load(
        "models/legal_ner"
    )

    return nlp