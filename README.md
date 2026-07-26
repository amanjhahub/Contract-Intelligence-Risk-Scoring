# AI-Powered Contract Intelligence & Risk Scoring Platform

An NLP-based legal contract analysis system that automatically processes contracts, extracts important clauses, identifies risks, generates summaries, compares multiple contracts, and provides intelligent question answering using Retrieval-Augmented Generation (RAG).

---

# 🚀 Features

## 1. Contract Risk Analysis

- Upload PDF contracts
- Extract contract text automatically
- Detect important legal clauses:
  - Payment
  - Termination
  - Confidentiality
  - Liability
  - Dispute Resolution
  - Governing Law
- Generate risk score
- Identify missing clauses
- Provide recommendations

---

## 2. AI Contract Summarization

Automatically generates structured summaries containing:

- Contract Title
- Parties
- Purpose
- Payment Terms
- Termination Conditions
- Liability Information
- Confidentiality Details
- Dispute Resolution
- Governing Law
- Important Risks

---

## 3. Contract Comparison

Compare two contracts and identify:

- Risk score difference
- Missing clauses
- Additional clauses
- Safer contract recommendation

Example:


Contract A Risk Score : 75
Contract B Risk Score : 100

Recommendation:
Contract B is safer.


---

## 4. AI Contract Question Answering (RAG)

Ask questions about uploaded contracts.

Example:


Question:
What clauses are present in this contract?

Answer:
Confidentiality,
Dispute Resolution,
Governing Law,
Payment Terms,
Termination,
Liability

Sources:
Page 1, Chunk 1
Page 1, Chunk 2


---

# 🏗️ System Architecture

             Contract PDF
                  |
                  ↓
          PDF Text Extraction
                  |
                  ↓
          Text Cleaning
                  |
    ┌─────────────┼─────────────┐
    ↓             ↓             ↓

Risk Analyzer Summarizer Comparator
| | |
↓ ↓ ↓
Risk Report AI Summary Comparison Report

                  |
                  ↓

         Document Embeddings
                  |
                  ↓
             FAISS Vector DB
                  |
                  ↓
                RAG
                  |
                  ↓
          Gemini LLM Response

---

# 🛠️ Tech Stack

## Programming Language

- Python

## NLP & AI

- Hugging Face Transformers
- Sentence Transformers
- Google Gemini API
- Retrieval-Augmented Generation (RAG)

## Document Processing

- PyMuPDF
- PDF Text Extraction
- Text Chunking

## Vector Database

- FAISS

## Backend

- FastAPI
- Uvicorn
- Pydantic

## Development Tools

- Git
- GitHub
- VS Code
- Postman / Swagger UI

---

# 📂 Project Structure

```text
Contract-Intelligence-Risk-Scoring

├── src
│   ├── api
│   │   └── main.py
│   │
│   ├── preprocessing
│   │   ├── pdf_reader.py
│   │   ├── text_cleaner.py
│   │   └── text_chunker.py
│   │
│   ├── risk
│   │   ├── risk_analyzer.py
│   │   └── risk_rules.py
│   │
│   ├── summarizer
│   │   └── contract_summarizer.py
│   │
│   ├── comparison
│   │   ├── contract_comparator.py
│   │   └── run_comparison.py
│   │
│   ├── rag
│   │   └── chat_service.py
│   │
│   ├── embeddings
│   │
│   ├── vector_store
│   │
│   └── llm
│       └── gemini_client.py
│
├── data
│   └── raw
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <repository-url>

cd Contract-Intelligence-Risk-Scoring
```

## 2. Create Environment
Using Conda:

```bash
conda create -n ai python=3.12

conda activate ai
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create `.env`

```env
GEMINI_API_KEY=your_api_key
```
# ▶️ Running the Application

## Run CLI Version

```bash
export PYTHONPATH=src

python src/main.py
```

## Run FastAPI Server

```bash
export PYTHONPATH=src

uvicorn api.main:app --reload
```

### Server

```
http://127.0.0.1:8000
```

### Swagger Documentation

```
http://127.0.0.1:8000/docs
```
# 🔌 API Endpoints
Health Check
GET /health

Response:

```json
{
 "status":"healthy",
 "service":"Contract Intelligence API"
}
```
Analyze Contract
POST /analyze

Input:

PDF File

Output:

```json
{
  "risk_score": 100,
  "risk_level": "Low",
  "present_clauses": [],
  "missing_clauses": []
}
```
Generate Summary
POST /summary

Input:

PDF File

Output:

```json
{
  "summary": "Contract summary..."
}
```
Compare Contracts
POST /compare

Input:

Contract A PDF
Contract B PDF

Output:


```json
{
  "contract_a_score": 75,
  "contract_b_score": 100,
  "recommendation": "Contract B"
}
```
Ask Questions
POST /ask

Example:


```json
{
  "question": "What clauses are present?"
}
```

Response:

```json
{
  "answer": "...",
  "sources": [
    "Page 1, Chunk 1"
  ]
}
```
# 📸 Demo

## Contract Risk Analysis

Upload a contract PDF and the system:

- Extracts contract text
- Detects important clauses
- Generates risk score
- Identifies missing clauses
- Provides recommendations


## AI Contract Question Answering (RAG)

Ask questions about the contract and get:

- AI-generated answers
- Relevant document sources
- Context-based retrieval using FAISS

Example:

Question:
```
What clauses are present in this contract?
```

Response:
```
Confidentiality
Dispute Resolution
Governing Law
Payment Terms
Termination
Liability
```
## 📊 Future Improvements

- Fine-tune Legal BERT/RoBERTa models
- CUAD dataset integration
- OCR support for scanned contracts
- Docker deployment
- AWS deployment
- React dashboard
- User authentication
- Multi-contract search

🎯 Project Impact

This platform reduces manual contract review time by automatically identifying important legal clauses, highlighting risks, and assisting compliance teams with AI-powered contract intelligence.

👨‍💻 Author

Aman Jha

B.Tech Computer Science Engineering

AI/ML Engineer | Python Developer | FastAPI | NLP | MERN Stack