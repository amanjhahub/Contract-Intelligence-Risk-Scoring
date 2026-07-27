import pandas as pd


input_file = "data/cuad_processed.csv"
output_file = "data/cuad_training.csv"


df = pd.read_csv(input_file)


# Create binary label
df["label"] = df["answer"].apply(
    lambda x: 1 if isinstance(x, str) and len(x.strip()) > 0 else 0
)


# Remove unnecessary column
df = df[
    [
        "text",
        "clause",
        "answer",
        "label"
    ]
]


df.to_csv(output_file, index=False)


print("Training samples:", len(df))

print("\nLabel distribution:")
print(df["label"].value_counts())

print("\nSaved:", output_file)