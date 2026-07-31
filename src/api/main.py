

from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List
import shutil

from comparison.contract_comparator import compare_contracts
from summarizer.contract_summarizer import summarize_contract
from preprocessing.pdf_reader import extract_text
from risk.risk_analyzer import analyze_risk
from rag.chat_service import ask_contract
from ner.entity_extractor import extract_entities
from ner.legal_mapper import map_legal_entities

from tasks.contract_tasks import analyze_contract_task
from tasks.celery_app import celery_app
from celery.result import AsyncResult

class RiskResponse(BaseModel):

    risk_score: int
    risk_level: str
    present_clauses: list
    missing_clauses: list
    entities: list


class SummaryResponse(BaseModel):

    summary: str



class CompareResponse(BaseModel):

    contract_a_score: int
    contract_b_score: int
    missing_in_a: list
    missing_in_b: list
    risk_difference: int
    recommendation: str
app = FastAPI(
    title="Contract Intelligence API",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "message": "Contract Intelligence API is running"
    }


@app.post(
    "/analyze",
    response_model=RiskResponse
)
async def analyze_contract(
    file: UploadFile = File(...)
):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported"
        )

    file_path = f"data/raw/{file.filename}"

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )


    pages = extract_text(
        file_path
    )


    contract_text = ""

    for page in pages:

        if page["text"]:

            contract_text += page["text"] + "\n"


    report = analyze_risk(
        contract_text
    )
    entities = extract_entities(
     contract_text
)

    legal_entities = map_legal_entities(
    entities
)


    return {

        "risk_score": report["risk_score"],

        "risk_level": report["risk_level"],

        "present_clauses": report["present"],

        "missing_clauses": report["missing"],
       "entities": legal_entities

    }

@app.post(
    "/summary",
    response_model=SummaryResponse
)
async def contract_summary(
    file: UploadFile = File(...)
):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported"
        )


    file_path = f"data/raw/{file.filename}"


    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )


    pages = extract_text(
        file_path
    )


    contract_text = ""


    for page in pages:

        if page["text"]:

            contract_text += page["text"] + "\n"


    summary = summarize_contract(
        contract_text
    )


    return {
        "summary": summary
    }


@app.post(
    "/compare",
    response_model=CompareResponse
)
async def compare_contracts_api(
    contract_a: UploadFile = File(...),
    contract_b: UploadFile = File(...)
):


    if (
        not contract_a.filename.endswith(".pdf")
        or not contract_b.filename.endswith(".pdf")
    ):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported"
        )

    path_a = f"data/raw/{contract_a.filename}"
    path_b = f"data/raw/{contract_b.filename}"


    with open(path_a, "wb") as buffer:

        shutil.copyfileobj(
            contract_a.file,
            buffer
        )


    with open(path_b, "wb") as buffer:

        shutil.copyfileobj(
            contract_b.file,
            buffer
        )


    def read_contract(path):

        pages = extract_text(path)

        text = ""

        for page in pages:

            if page["text"]:

                text += page["text"] + "\n"

        return text



    text_a = read_contract(path_a)

    text_b = read_contract(path_b)



    report_a = analyze_risk(
        text_a
    )


    report_b = analyze_risk(
        text_b
    )


    comparison = compare_contracts(
        report_a,
        report_b
    )


    return {

        "contract_a_score": comparison["contract_a_score"],

        "contract_b_score": comparison["contract_b_score"],

        "missing_in_a": comparison["missing_in_a"],

        "missing_in_b": comparison["missing_in_b"],

        "risk_difference": comparison["risk_difference"],

        "recommendation": comparison["better_contract"]

    }


@app.post("/ask")
async def ask_question(
    question: str
):

    response = ask_contract(
        question
    )

    return response

@app.post("/analyze/async")
async def analyze_contract_async(
    file: UploadFile = File(...)
):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported"
        )

    file_path = f"data/raw/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    task = analyze_contract_task.delay(file_path)

    return {
        "task_id": task.id,
        "status": "Processing"
    }


@app.get("/tasks/{task_id}")
async def get_task_status(task_id: str):

    task = AsyncResult(task_id, app=celery_app)

    if task.state == "PENDING":
        return {
            "status": "PENDING"
        }

    elif task.state == "STARTED":
        return {
            "status": "STARTED"
        }

    elif task.state == "SUCCESS":
        return {
            "status": "SUCCESS",
            "result": task.result
        }

    elif task.state == "FAILURE":
        return {
            "status": "FAILURE",
            "error": str(task.result)
        }

    return {
        "status": task.state
    }

@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "service": "Contract Intelligence API"
    }