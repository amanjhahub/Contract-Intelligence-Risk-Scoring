import shutil

from tasks.celery_app import celery_app

from preprocessing.pdf_reader import extract_text
from risk.risk_analyzer import analyze_risk
from ner.entity_extractor import extract_entities
from ner.legal_mapper import map_legal_entities


@celery_app.task
def analyze_contract_task(file_path):

    pages = extract_text(file_path)

    contract_text = ""

    for page in pages:

        if page["text"]:

            contract_text += page["text"] + "\n"

    report = analyze_risk(contract_text)

    entities = extract_entities(contract_text)

    legal_entities = map_legal_entities(entities)

    return {
        "risk_score": report["risk_score"],
        "risk_level": report["risk_level"],
        "present_clauses": report["present"],
        "missing_clauses": report["missing"],
        "entities": legal_entities,
    }