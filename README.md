📄 Document Intelligence Platform

A production-style AI document processing backend built with FastAPI and LangGraph, designed to handle validation, retries, and explicit failure states instead of blindly trusting LLM output.

🏗️ Architecture
Streamlit UI
    ↓
FastAPI API
    ↓
Service Layer
    ↓
LangGraph Workflow
    ├── Extract
    ├── Parse (LLM)
    ├── Validate
    ├── Retry (max 2)
    └── Success / Failure
    ↓
PostgreSQL

🧠 Why LangGraph?

The document pipeline is modeled as a state machine rather than a linear chain.

LangGraph enables:

Deterministic state transitions

Conditional retries

Explicit terminal states

Safer AI orchestration

This avoids common failure modes in AI systems where LLM output is assumed to be correct.

🔄 Processing Flow

Extract document text (simulated, easily replaceable)

Run LLM extraction

Parse structured output

Validate required fields

Retry on failure (max 2 attempts)

Mark document as processed or failed

🛡️ Failure Handling

LLM output is validated before persistence

Retries are bounded and deterministic

Invalid documents are explicitly marked as failed

No partial or unsafe data is stored

📦 API Endpoints
Create Document
POST /documents

{ "filename": "sample.pdf" }

Process Document
POST /documents/{id}/process


Returns:

{
  "id": "...",
  "status": "processed | failed",
  "extracted_data": {...}
}

▶️ Running the Project
Start API
python -m uvicorn app.main:app --reload


Swagger:

http://127.0.0.1:8000/docs

Start UI
streamlit run streamlit_app/app.py

🧪 Retry Behavior

Validation failure triggers retry

Max retry limit enforced

Terminal states are deterministic

🏆 What This Project Demonstrates

LangGraph-based AI orchestration

Production-style retry patterns

Explicit failure handling

Clean backend layering

End-to-end integration (API + UI)

🔮 Extensibility

The architecture supports:

Real PDF parsing

Background processing

Human review workflows

Observability and tracing

## 👩‍💻 Author

Jyotsana Singh  
Backend & AI Systems Engineering  

LinkedIn: https://www.linkedin.com/in/jyotsana-singh-46b33791/

