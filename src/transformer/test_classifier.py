from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL_PATH = "models/cuad_classifier"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

model.eval()

text = """
The client shall pay all invoices within 30 days of receipt.
"""

inputs = tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
    padding=True,
    max_length=512
)

with torch.no_grad():
    outputs = model(**inputs)

logits = outputs.logits

probabilities = torch.softmax(logits, dim=1)

prediction = torch.argmax(probabilities, dim=1).item()

confidence = probabilities[0][prediction].item()

label_map = {
    0: "Clause Absent",
    1: "Clause Present"
}

print("Prediction:", label_map[prediction], f"({prediction})")
print("Confidence:", round(confidence * 100, 2), "%")