import spacy
import pandas as pd

from spacy.training.example import Example
from spacy.util import minibatch, compounding

from pathlib import Path


DATA_PATH = "data/cuad_processed.csv"
MODEL_PATH = "models/contract_ner"


def create_training_data():

    df = pd.read_csv(
        DATA_PATH,
        nrows=100
    )

    nlp = spacy.load("en_core_web_sm")

    training_data = []


    for _, row in df.iterrows():

        text = str(row["text"])

        doc = nlp(text)

        entities = []

        for ent in doc.ents:

            if ent.label_ in ["ORG", "DATE", "MONEY"]:

                entities.append(
                    (
                        ent.start_char,
                        ent.end_char,
                        ent.label_
                    )
                )


        if entities:

            training_data.append(
                (
                    text,
                    {
                        "entities": entities
                    }
                )
            )


    return training_data



def train():

    training_data = create_training_data()

    print(
        "Training examples:",
        len(training_data)
    )


    nlp = spacy.blank("en")


    ner = nlp.add_pipe(
        "ner"
    )


    labels = [
        "ORG",
        "DATE",
        "MONEY"
    ]


    for label in labels:
        ner.add_label(label)


    optimizer = nlp.begin_training()


    for epoch in range(20):

        losses = {}

        batches = minibatch(
            training_data,
            size=compounding(
                4.0,
                32.0,
                1.5
            )
        )


        for batch in batches:

            examples = []

            for text, annotations in batch:

                example = Example.from_dict(
                    nlp.make_doc(text),
                    annotations
                )

                examples.append(example)


            nlp.update(
                examples,
                drop=0.3,
                losses=losses
            )


        print(
            f"Epoch {epoch+1}",
            losses
        )


    Path(MODEL_PATH).mkdir(
        parents=True,
        exist_ok=True
    )


    nlp.to_disk(
        MODEL_PATH
    )


    print(
        "Model saved:",
        MODEL_PATH
    )



if __name__ == "__main__":
    train()
