import json
import pandas as pd


input_file = "data/cuad/CUAD_v1/CUAD_v1.json"
output_file = "data/cuad_processed.csv"


with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)


rows = []


for contract in data["data"]:
    title = contract["title"]

    for paragraph in contract["paragraphs"]:
        context = paragraph["context"]

        for qa in paragraph["qas"]:
            question = qa["question"]

            category = question.split('"')[1]

            answer = ""

            if qa["answers"]:
                answer = qa["answers"][0]["text"]

            rows.append({
                "contract": title,
                "text": context,
                "clause": category,
                "answer": answer
            })


df = pd.DataFrame(rows)

df.to_csv(output_file, index=False)

print("Total samples:", len(df))
print(df.head())