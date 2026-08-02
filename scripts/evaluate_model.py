from sklearn.metrics import classification_report, precision_score, recall_score, f1_score
from transformers import pipeline
import pandas as pd


MODEL_PATH = "models/cuad_classifier"


classifier = pipeline(
    "text-classification",
    model=MODEL_PATH,
    tokenizer=MODEL_PATH
)


data = pd.read_csv(
    "data/test_cuad.csv"
)


y_true = []
y_pred = []


for _, row in data.iterrows():

    text = row["text"]

    actual = row["label"]

    prediction = classifier(text)[0]["label"]

    y_true.append(actual)

    y_pred.append(prediction)



print(
    classification_report(
        y_true,
        y_pred
    )
)


print(
    "Precision:",
    precision_score(
        y_true,
        y_pred,
        average="weighted"
    )
)


print(
    "Recall:",
    recall_score(
        y_true,
        y_pred,
        average="weighted"
    )
)


print(
    "F1:",
    f1_score(
        y_true,
        y_pred,
        average="weighted"
    )
)
