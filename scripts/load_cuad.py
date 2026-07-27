import json

path = "data/cuad/CUAD_v1/CUAD_v1.json"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

print("Dataset version:", data["version"])
print("Number of contracts:", len(data["data"]))

contract = data["data"][0]

print("\nFirst contract:")
print(contract["title"])

qa = contract["paragraphs"][0]["qas"][0]

print("\nQuestion:")
print(qa["question"])

print("\nAnswer:")
print(qa["answers"][0]["text"])