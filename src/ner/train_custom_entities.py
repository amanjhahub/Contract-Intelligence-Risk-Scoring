import spacy
from spacy.training.example import Example


TRAIN_DATA = [

(
"ABC Technologies signed an agreement with XYZ Solutions on 12 January 2026 for $50000.",
{
"entities": [
(0,16,"ORG"),
(42,55,"ORG"),
(59,74,"DATE"),
(80,85,"MONEY")
]
}
),

(
"Reliance Industries entered a contract with Tata Solutions effective on 1 March 2025 for $100000.",
{
"entities": [
(0,21,"ORG"),
(43,58,"ORG"),
(73,85,"DATE"),
(91,98,"MONEY")
]
}
),

(
"Microsoft Corporation and Amazon Inc signed the agreement dated 15 July 2024.",
{
"entities": [
(0,21,"ORG"),
(26,37,"ORG"),
(66,78,"DATE")
]
}
),

(
"Google LLC signed a service agreement with Infosys Limited on 20 February 2023 worth $75000.",
{
"entities": [
(0,10,"ORG"),
(45,61,"ORG"),
(65,80,"DATE"),
(87,92,"MONEY")
]
}
)

]

nlp = spacy.blank("en")

ner = nlp.add_pipe("ner")

for label in ["ORG", "DATE", "MONEY"]:
    ner.add_label(label)


optimizer = nlp.begin_training()


for epoch in range(30):

    losses = {}

    for text, annotations in TRAIN_DATA:

        example = Example.from_dict(
            nlp.make_doc(text),
            annotations
        )

        nlp.update(
            [example],
            losses=losses
        )

    print(epoch, losses)


nlp.to_disk("models/legal_ner")

print("Saved")