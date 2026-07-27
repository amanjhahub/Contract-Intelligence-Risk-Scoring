from ner.model_loader import load_spacy_model


nlp = load_spacy_model()


def extract_entities(contract_text):

    doc = nlp(contract_text)

    entities = []

    for entity in doc.ents:

        entities.append(
            {
                "text": entity.text,
                "label": entity.label_
            }
        )

    return entities