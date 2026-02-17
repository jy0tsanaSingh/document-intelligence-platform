📄 Document Intelligence Platform

A production-style AI document processing system built with FastAPI and LangGraph, designed to safely orchestrate LLM workflows using validation, retries, and explicit failure states.

🏗️ Architecture

Streamlit UI → FastAPI → Service Layer → LangGraph (state machine) → PostgreSQL

🧠 Core Idea

This project treats AI document processing as a deterministic state machine, not a single prompt call.

Instead of blindly trusting LLM output, the system:

Validates structured results

Retries deterministically on failure

Ends in explicit terminal states (processed / failed)

🔄 Processing Workflow

Extract document text (simulated, pluggable)

Run LLM-based structured extraction

Parse JSON output

Validate required fields

Retry extraction (max 2 attempts)

Persist final state

🛡️ Failure & Retry Strategy

LLM output is validated before persistence

Retries are bounded and deterministic

Failed documents are explicitly marked and stored

No partial or unsafe data is persisted

This mirrors real-world AI backend reliability patterns.

🧾 Structured Outputs & Validation

The system enforces structured outputs by parsing and validating LLM responses before persistence.

Extracted data is:

Parsed into structured JSON

Validated against required fields

Retried deterministically on validation failure

Rejected with an explicit failure state if retries are exhausted

This avoids common LLM failure modes such as malformed or incomplete outputs.

🔍 Observability & Debugging

The LangGraph-based workflow naturally exposes node-level execution boundaries, making it suitable for fine-grained observability.

In a production setup, each node can be instrumented with tracing (e.g., LangSmith or OpenTelemetry) to:

Identify where failures occur

Measure retry frequency

Inspect intermediate workflow states

This design keeps observability decoupled from business logic.

⏱️ Asynchronous Processing Considerations

For simplicity, document processing is triggered synchronously via the API.

In production, this step would be offloaded to a background worker (e.g., FastAPI BackgroundTasks or a queue-based system such as Celery/Redis), enabling:

Immediate API responses

Non-blocking long-running tasks

Better scalability under load

The orchestration logic is intentionally decoupled from execution strategy.

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


Swagger UI:

http://127.0.0.1:8000/docs

Start UI
streamlit run streamlit_app/app.py

🏆 What This Project Demonstrates

LangGraph-based AI orchestration

Deterministic retry and failure handling

Structured output validation

Clean separation of API, service, and orchestration layers

End-to-end system design (UI → DB)

🔮 Designed for Extension

The architecture cleanly supports:

Real PDF parsing

Background async processing

Human-in-the-loop review workflows

Observability and tracing

👩‍💻 Author

Jyotsana Singh
Backend & AI Systems Engineering

🔗 LinkedIn: https://www.linkedin.com/in/jyotsana-singh-46b33791/
