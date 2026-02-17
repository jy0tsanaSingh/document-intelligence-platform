📄 Document Intelligence Platform

A production-style AI document processing system built with FastAPI and LangGraph, designed to safely orchestrate LLM workflows using validation, retries, and explicit failure states.

🏗️ Architecture (One-Line)

Streamlit UI → FastAPI → Service Layer → LangGraph (state machine) → PostgreSQL

🧠 Core Idea

This project treats AI document processing as a deterministic state machine, not a single prompt call.

Instead of trusting LLM output blindly, the system:

Validates structured results

Retries on failure (bounded)

Ends in explicit terminal states (processed / failed)

🔄 Processing Workflow

Extract document text (simulated, pluggable)

Run LLM-based structured extraction

Parse JSON output

Validate required fields

Retry extraction (max 2 attempts)

Persist final state

🛡️ Failure & Retry Strategy

Validation layer guards against malformed LLM output

Retry logic is deterministic and bounded

Failed documents are explicitly marked and persisted

No partial or unsafe data is stored

📦 API Endpoints
Create Document
POST /documents

{
  "filename": "sample.pdf"
}

Process Document
POST /documents/{id}/process


Response:

{
  "id": "...",
  "status": "processed | failed",
  "extracted_data": {...}
}

▶️ Running the Project
Start Backend
python -m uvicorn app.main:app --reload


Swagger:

http://127.0.0.1:8000/docs

Start UI
streamlit run streamlit_app/app.py

🏆 What This Project Demonstrates

LangGraph-based AI orchestration

Production-style retry and failure handling

Deterministic AI workflows

Clean separation of API, service, and orchestration layers

End-to-end system design (UI → DB)

🔮 Designed for Extension

The architecture cleanly supports:

Real PDF parsing

Background async processing

Human review workflows

Observability and tracing

👩‍💻 Author

Jyotsana Singh
Backend & AI Systems Engineering

🔗 LinkedIn: https://www.linkedin.com/in/jyotsana-singh-46b33791/
