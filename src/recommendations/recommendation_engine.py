def generate_recommendations(risk_report):

    recommendations = []

    for clause in risk_report["missing"]:

        name = clause["clause"]
        severity = clause["severity"]

        if severity == "High":
            priority = "Critical"
        elif severity == "Medium":
            priority = "Important"
        else:
            priority = "Suggested"

        recommendations.append(
            {
                "clause": name,
                "priority": priority,
                "message": f"Add {name} clause to reduce contract risk."
            }
        )

    if not recommendations:
        recommendations.append(
            {
                "clause": "None",
                "priority": "Good",
                "message": "No major missing clauses detected."
            }
        )

    return recommendations