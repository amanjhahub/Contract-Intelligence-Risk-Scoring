from preprocessing.pdf_reader import extract_text
from preprocessing.text_cleaner import clean_text

from risk.risk_analyzer import analyze_risk
from comparison.contract_comparator import compare_contracts


def extract_contract_text(pdf_path):

    pages = extract_text(pdf_path)

    text = ""

    for page in pages:

        if page["text"]:

            cleaned = clean_text(
                page["text"]
            )

            text += cleaned + "\n"

    return text



contract_a_path = "data/raw/contract_a.pdf"
contract_b_path = "data/raw/contract_b.pdf"


print("Reading Contract A...")
contract_a = extract_contract_text(
    contract_a_path
)


print("Reading Contract B...")
contract_b = extract_contract_text(
    contract_b_path
)



print("\nAnalyzing contracts...")


report_a = analyze_risk(
    contract_a
)


report_b = analyze_risk(
    contract_b
)



comparison = compare_contracts(
    report_a,
    report_b
)



print("\n==============================")
print("Contract Comparison Report")
print("==============================")


print(
    f"\nContract A Risk Score : {comparison['contract_a_score']}"
)

print(
    f"Contract B Risk Score : {comparison['contract_b_score']}"
)


print("\nMissing in Contract A:")

for clause in comparison["missing_in_a"]:

    print(
        f"✗ {clause}"
    )


print("\nMissing in Contract B:")

for clause in comparison["missing_in_b"]:

    print(
        f"✗ {clause}"
    )


print("\nAdded in Contract A:")

for clause in comparison["added_in_a"]:

    print(
        f"✓ {clause}"
    )


print("\nAdded in Contract B:")

for clause in comparison["added_in_b"]:

    print(
        f"✓ {clause}"
    )


print(
    f"\nRisk Difference : {comparison['risk_difference']} points"
)


print("\nFinal Recommendation:")

print(
    f"{comparison['better_contract']} is safer."
)