def compare_contracts(report_a, report_b):

    comparison = {}


    # Extract missing clauses

    missing_a = [
        item["clause"]
        for item in report_a["missing"]
    ]

    missing_b = [
        item["clause"]
        for item in report_b["missing"]
    ]


    # Extract present clauses

    present_a = [
        item["clause"]
        for item in report_a["present"]
    ]

    present_b = [
        item["clause"]
        for item in report_b["present"]
    ]


    # Risk scores

    comparison["contract_a_score"] = (
        report_a["risk_score"]
    )

    comparison["contract_b_score"] = (
        report_b["risk_score"]
    )


    # Clauses missing in each contract

    comparison["missing_in_a"] = [
        clause
        for clause in missing_a
        if clause not in missing_b
    ]


    comparison["missing_in_b"] = [
        clause
        for clause in missing_b
        if clause not in missing_a
    ]


    # Clauses added in each contract

    comparison["added_in_a"] = [
        clause
        for clause in present_a
        if clause not in present_b
    ]


    comparison["added_in_b"] = [
        clause
        for clause in present_b
        if clause not in present_a
    ]


    # Decide safer contract

    if report_a["risk_score"] > report_b["risk_score"]:

        comparison["better_contract"] = (
            "Contract A"
        )


    elif report_b["risk_score"] > report_a["risk_score"]:

        comparison["better_contract"] = (
            "Contract B"
        )


    else:

        comparison["better_contract"] = (
            "Both contracts have equal risk"
        )


    # Risk difference

    comparison["risk_difference"] = abs(
        report_a["risk_score"]
        -
        report_b["risk_score"]
    )


    return comparison