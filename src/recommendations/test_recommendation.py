from risk.risk_analyzer import analyze_risk
from recommendations.recommendation_engine import generate_recommendations


sample_contract = """
Payment shall be made within 30 days.

The contractor shall be liable for damages.

Either party can terminate with written notice.
"""


risk_report = analyze_risk(sample_contract)

recommendations = generate_recommendations(
    risk_report
)


print("\nContract Recommendations\n")

for item in recommendations:
    print(
        f"{item['priority']} : {item['clause']}"
    )

    print(
        item["message"]
    )

    print()