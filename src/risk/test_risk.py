from src.risk.risk_analyzer import analyze_risk


sample_contract = """
The contractor shall complete the project within 30 days.

Payment shall be made within 15 days after invoice.

The parties agree that either party may terminate this agreement
by giving 30 days written notice.

The contractor shall be liable for damages caused by negligence.
"""


report = analyze_risk(sample_contract)


print("\nContract Risk Report\n")

print(f"Risk Score : {report['risk_score']}")
print(f"Risk Level : {report['risk_level']}")


print("\nPresent Clauses")

for clause in report["present"]:
    print(
        f"✓ {clause['clause']} ({clause['severity']})"
    )


print("\nMissing Clauses")

for clause in report["missing"]:
    print(
        f"✗ {clause['clause']} ({clause['severity']})"
    )