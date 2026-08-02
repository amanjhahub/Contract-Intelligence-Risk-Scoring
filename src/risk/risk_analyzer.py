from risk.post_processor import process_predictions
from risk.risk_rules import REQUIRED_CLAUSES

SEVERITY_WEIGHTS = {
    "High": 20,
    "Medium": 10,
    "Low": 5
}


def analyze_risk(text):

    text = text.lower()

    present = []
    missing = []

    for clause, data in REQUIRED_CLAUSES.items():

        keywords = data["keywords"]
        severity = data["severity"]

        found = False

        for keyword in keywords:

            if keyword.lower() in text:
                found = True
                break

        if found:

             present.append({
        "clause": clause,
        "severity": severity,
        "confidence": 0.95
    })

        else:

            missing.append({
                "clause": clause,
                "severity": severity
            })

    # Calculate weighted score
    score = 100

    for clause in missing:

        severity = clause["severity"]

        score -= SEVERITY_WEIGHTS[severity]

    if score < 0:
        score = 0

    if score >= 80:
        level = "Low"

    elif score >= 50:
        level = "Medium"

    else:
        level = "High"

    present = process_predictions(present)
    return {
        "risk_score": score,
        "risk_level": level,
        "present": present,
        "missing": missing
    }