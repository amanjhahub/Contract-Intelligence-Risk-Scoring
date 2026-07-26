from llm.gemini_client import generate_answer


def summarize_contract(contract_text):

    prompt = f"""
You are an AI legal assistant.

Read the contract carefully and produce a structured summary.

If a field is not explicitly mentioned, infer it only if it is obvious from the contract.
Otherwise write "Not specified".

Return exactly in this format:

Title:
Parties:
Purpose:
Payment Terms:
Termination:
Liability:
Confidentiality:
Dispute Resolution:
Governing Law:
Important Risks:

Contract:

{contract_text}
"""

    return generate_answer(
        context="",
        question=prompt
    )