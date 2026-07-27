import pandas as pd


file = "data/cuad_processed.csv"

df = pd.read_csv(file)


print("Dataset Shape:")
print(df.shape)


print("\nClause Distribution:")
print(df["clause"].value_counts())


print("\nMissing Answers:")
print(df["answer"].isna().sum())


print("\nText Length Statistics:")
df["text_length"] = df["text"].apply(len)

print(df["text_length"].describe())