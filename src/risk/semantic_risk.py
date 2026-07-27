from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

CLAUSE_EXAMPLES = {
    "Payment": [
        "The client shall pay the agreed amount within 30 days.",
        "Payment shall be made after invoice.",
        "Fees are payable upon delivery."
    ],
    "Termination": [
        "Either party may terminate this agreement.",
        "This contract may be cancelled with notice.",
        "The agreement may end after written notice."
    ],
    "Confidentiality": [
        "The parties agree to keep all information confidential.",
        "Neither party shall disclose confidential information.",
        "This agreement includes a non-disclosure obligation."
    ],
    "Liability": [
        "Neither party shall be liable for indirect damages.",
        "The company accepts liability for losses.",
        "Liability is limited under this agreement."
    ],
    "Dispute Resolution": [
        "Disputes shall be resolved by arbitration.",
        "Any dispute shall be referred to court.",
        "The parties agree to arbitration proceedings."
    ],
    "Governing Law": [
        "This agreement shall be governed by the laws of India.",
        "The governing law shall be Indian law.",
        "Jurisdiction shall be the courts of India."
    ]
}


def semantic_clause_detection(contract_text):

    contract_embedding = model.encode(
        contract_text,
        convert_to_tensor=True
    )

    results = []

    for clause, examples in CLAUSE_EXAMPLES.items():

        example_embeddings = model.encode(
            examples,
            convert_to_tensor=True
        )

        similarities = util.cos_sim(
            contract_embedding,
            example_embeddings
        )

        score = similarities.max().item()

        results.append(
            {
                "clause": clause,
                "confidence": round(score, 3)
            }
        )

    return results