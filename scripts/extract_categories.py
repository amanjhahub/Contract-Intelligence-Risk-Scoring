import json

path = "data/cuad/CUAD_v1/CUAD_v1.json"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

categories = set()

for contract in data["data"]:
    for paragraph in contract["paragraphs"]:
        for qa in paragraph["qas"]:
            categories.add(qa["question"])

print("Total Questions:", len(categories))

for q in sorted(categories):
    print("-", q)