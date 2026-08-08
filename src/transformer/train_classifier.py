import json
import numpy as np
import pandas as pd
import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)

from datasets import Dataset

from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support
)


MODEL_NAME = "distilroberta-base"


def load_data():

    train_df = pd.read_csv(
        "data/train_cuad.csv"
    )

    test_df = pd.read_csv(
        "data/test_cuad.csv"
    )

    return train_df, test_df


def tokenize_data(dataset, tokenizer):

    def tokenize(batch):

        text = [
            f"Clause: {c}\nContract: {t}"
            for c, t in zip(
                batch["clause"],
                batch["text"]
            )
        ]

        return tokenizer(
            text,
            padding="max_length",
            truncation=True,
            max_length=256
        )

    return dataset.map(
        tokenize,
        batched=True
    )


def compute_metrics(eval_pred):

    logits, labels = eval_pred

    predictions = np.argmax(
        logits,
        axis=-1
    )

    precision, recall, f1, _ = precision_recall_fscore_support(
        labels,
        predictions,
        average="binary",
        zero_division=0
    )

    accuracy = accuracy_score(
        labels,
        predictions
    )

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }


def main():

    train_df, test_df = load_data()

    train_dataset = Dataset.from_pandas(
        train_df
    )

    test_dataset = Dataset.from_pandas(
        test_df
    )

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME
    )

    train_dataset = tokenize_data(
        train_dataset,
        tokenizer
    )

    test_dataset = tokenize_data(
        test_dataset,
        tokenizer
    )

    train_dataset = train_dataset.rename_column(
        "label",
        "labels"
    )

    test_dataset = test_dataset.rename_column(
        "label",
        "labels"
    )

    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME,
        num_labels=2
    )

    training_args = TrainingArguments(

        output_dir="models/cuad_classifier",

        num_train_epochs=3,

        per_device_train_batch_size=1,

        per_device_eval_batch_size=1,

        gradient_accumulation_steps=16,

        eval_strategy="epoch",

        save_strategy="epoch",

        logging_steps=25,

        fp16=True,

        report_to="none",

        gradient_checkpointing=True
    )

    trainer = Trainer(

        model=model,

        args=training_args,

        train_dataset=train_dataset,

        eval_dataset=test_dataset,

        compute_metrics=compute_metrics
    )

    trainer.train()

    metrics = trainer.evaluate()

    print("\n========== Evaluation Metrics ==========")
    print(metrics)

    with open(
        "models/cuad_classifier/evaluation_metrics.json",
        "w"
    ) as f:

        json.dump(
            metrics,
            f,
            indent=4
        )

    trainer.save_model(
        "models/cuad_classifier"
    )

    tokenizer.save_pretrained(
        "models/cuad_classifier"
    )

    print("\nModel saved successfully.")
    print("Evaluation metrics saved to:")
    print("models/cuad_classifier/evaluation_metrics.json")


if __name__ == "__main__":
    main()