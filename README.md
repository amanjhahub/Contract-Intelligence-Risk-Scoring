# 📄 Contract Intelligence & Risk Scoring System

An AI-powered contract analysis system that analyzes legal contracts, identifies risks, compares multiple contracts, generates summaries, and answers questions using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 📄 PDF Contract Processing
- ⚠️ Risk Analysis with Weighted Scoring
- 📊 Risk Level Classification (Low / Medium / High)
- 📝 Clause Detection
- 💡 Contract Recommendations
- 🤖 AI-powered Contract Summarization (Google Gemini)
- 🔍 RAG-based Question Answering
- 📚 FAISS Vector Search
- 📑 Compare Two Contracts
- 🖥️ Interactive Menu-driven CLI

---

## 🛠️ Tech Stack

- Python
- Google Gemini API
- Sentence Transformers
- FAISS
- Hugging Face
- PyPDF2
- NumPy

---

## 📂 Project Structure

```
src/
│
├── app/
├── preprocessing/
├── embeddings/
├── vector_store/
├── llm/
├── risk/
├── recommendations/
├── comparison/
├── summarizer/
└── main.py
```

---

## ⚙️ Installation

```bash
git clone <repository-url>

cd Contract-Intelligence-Risk-Scoring

conda activate ai

pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
export PYTHONPATH=src

python src/app/main_menu.py
```

---

## 📌 Menu

```
1. Analyze Single Contract
2. Compare Two Contracts
3. Generate Summary
4. Exit
```

---

## 📊 Features Demonstrated

### Risk Analysis
- Detects important legal clauses
- Weighted severity scoring
- Risk level prediction

### Contract Comparison
- Compares two contracts
- Shows missing clauses
- Suggests safer contract

### Contract Summary
- Title
- Parties
- Payment Terms
- Termination
- Liability
- Confidentiality
- Governing Law

### RAG Question Answering

Ask questions such as:

- What are the payment terms?
- What clauses are present?
- Who are the parties?
- What is the governing law?

---

## 🔮 Future Improvements

- Web Interface (FastAPI + React)
- Clause Extraction using LLMs
- Risk Heatmaps
- Multi-document Search
- Contract Version Tracking
- OCR Support
- Docker Deployment

---

## 👨‍💻 Author

Aman Jha
B.Tech CSE (2023–2027)
