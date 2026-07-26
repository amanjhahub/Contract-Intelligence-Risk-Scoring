from risk.risk_analyzer import analyze_risk
from comparison.contract_comparator import compare_contracts


contract_a = """
Payment shall be made within 30 days.

The contractor shall be liable for damages.

Either party can terminate this agreement
with 30 days written notice.
"""


contract_b = """
Payment shall be made within 15 days.

The contractor shall be liable for damages.

Either party can terminate this agreement
with 30 days written notice.

Both parties agree to keep confidential information private.

Any dispute shall be resolved through arbitration.

This agreement shall be governed by the laws of India.
"""


report_a = analyze_risk(contract_a)

report_b = analyze_risk(contract_b)


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