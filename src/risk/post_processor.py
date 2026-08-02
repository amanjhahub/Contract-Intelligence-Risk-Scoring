CONFIDENCE_THRESHOLD = 0.5


def process_predictions(predictions):

    final = []

    seen = set()

    for item in predictions:

        clause = item["clause"]
        confidence = item.get("confidence", 1.0)

        if confidence < CONFIDENCE_THRESHOLD:
            continue

        if clause in seen:
            continue

        seen.add(clause)

        final.append(
            {
                "clause": clause,
                "severity": item["severity"],
                "confidence": round(confidence, 2)
            }
        )

    return final

