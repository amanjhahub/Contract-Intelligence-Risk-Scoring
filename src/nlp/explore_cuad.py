import json

with open("data/cuad/CUAD_v1/CUAD_v1.json", "r") as f:
    data = json.load(f)

print(type(data))

print(data.keys())