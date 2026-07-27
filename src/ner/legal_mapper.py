def map_legal_entities(entities):

    legal_entities = []

    for entity in entities:

        text = entity["text"]
        label = entity["label"]


        if label == "ORG":

            legal_entities.append(
                {
                    "text": text,
                    "label": "CONTRACT_PARTY"
                }
            )


        elif label == "GPE":

            legal_entities.append(
                {
                    "text": text,
                    "label": "JURISDICTION"
                }
            )


        elif label == "DATE":

            if any(word in text.lower() for word in ["day", "month", "year"]):

                legal_entities.append(
                    {
                        "text": text,
                        "label": "CONTRACT_DURATION"
                    }
                )

            else:

                legal_entities.append(
                    {
                        "text": text,
                        "label": "LEGAL_DATE"
                    }
                )


    return legal_entities