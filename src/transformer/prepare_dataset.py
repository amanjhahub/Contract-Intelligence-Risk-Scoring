import pandas as pd
from sklearn.model_selection import train_test_split


DATA_PATH = "data/cuad_training.csv"


def prepare_dataset():

    df = pd.read_csv(DATA_PATH)

    # Convert labels
    df["label"] = df["label"].astype(int)

    # Split data
    train_df, test_df = train_test_split(
        df,
        test_size=0.2,
        random_state=42,
        stratify=df["label"]
    )

    print("Training samples:", len(train_df))
    print("Testing samples:", len(test_df))

    print("\nTraining label distribution:")
    print(train_df["label"].value_counts())

    print("\nTesting label distribution:")
    print(test_df["label"].value_counts())


    train_df.to_csv(
        "data/train_cuad.csv",
        index=False
    )

    test_df.to_csv(
        "data/test_cuad.csv",
        index=False
    )


if __name__ == "__main__":
    prepare_dataset()