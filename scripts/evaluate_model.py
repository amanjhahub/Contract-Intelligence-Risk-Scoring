from sklearn.metrics import classification_report, precision_score, recall_score, f1_score
from transformers import pipeline
import pandas as pd


MODEL_PATH = "models/cuad_classifier"


classifier = pipeline(
    "text-classification",
    model=MODEL_PATH,
    tokenizer=MODEL_PATH,
    device=-1
)


# For testing, use only 100 samples
# Change to pd.read_csv("data/test_cuad.csv") for full evaluation
data = pd.read_csv("data/test_cuad.csv").head(100)


y_true = []
y_pred = []


total = len(data)


for i, (_, row) in enumerate(data.iterrows(), start=1):

    text = row["text"]
    actual = row["label"]

    prediction = classifier(
        text,
        truncation=True,
        max_length=512
    )[0]["label"]

    # Convert LABEL_0/LABEL_1 to 0/1
    prediction = int(prediction.replace("LABEL_", ""))

    y_true.append(actual)
    y_pred.append(prediction)


    if i % 10 == 0:
        print(f"Processed {i}/{total}")


print("\nClassification Report:\n")

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