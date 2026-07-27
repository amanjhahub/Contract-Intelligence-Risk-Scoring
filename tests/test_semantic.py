from risk.semantic_risk import semantic_clause_detection

contract = """
This agreement shall be governed by the laws of India.

Either party may terminate this agreement by giving 30 days written notice.

The client agrees to pay the invoice within thirty days.

All confidential information must remain confidential.
"""

results = semantic_clause_detection(contract)

for result in results:
    print(result)