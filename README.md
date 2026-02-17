# Document Intelligence Platform

An AI-powered backend system for extracting structured intelligence from unstructured documents using FastAPI and LangGraph-based orchestration.

## Overview

This project demonstrates a production-style AI backend that:

- Accepts document metadata via REST APIs
- Persists document lifecycle state
- Runs a multi-step AI workflow
- Handles validation, retries, and failure states deterministically
- Stores structured extraction results

The system emphasizes robustness, state management, and clean architecture.

---

## Architecture

Client (Swagger / Streamlit)
        ↓
FastAPI (Async APIs)
        ↓
Service Layer (Business Logic)
        ↓
LangGraph (Workflow Orchestration)
        ↓
LLM (OpenAI)
        ↓
PostgreSQL (Async SQLAlchemy)

Each layer has a single responsibility to ensure maintainability and extensibility.

---

## AI Workflow

The document processing workflow is orchestrated using LangGraph:

START  
  ↓  
Extract  
  ↓  
Validate  
  ↓  
Valid?  
  ├── Yes → Processed  
  └── No → Retry (limited attempts)  
               ↓  
            Still invalid?  
               └── Mark Failed  

This deterministic flow models real-world AI processing systems.

---

## Tech Stack

Backend:
- FastAPI (async REST APIs)
- SQLAlchemy (async ORM)
- PostgreSQL

AI:
- OpenAI API
- LangGraph (workflow orchestration)

Client:
- Swagger (OpenAPI)
- Streamlit (demo UI)

---

## Project Structure

app/
├── api/        # FastAPI routes  
├── services/   # Business logic  
├── ai/         # LangGraph workflow  
├── models/     # SQLAlchemy models  
├── schemas/    # Pydantic schemas  
├── db/         # Database session  
└── main.py     # Application entry point  

---

## How to Run

1. Create virtual environment

python -m venv env  
source env/bin/activate  

2. Install dependencies

pip install -r requirements.txt  

3. Set environment variables

export OPENAI_API_KEY="your-api-key"

4. Run FastAPI

python -m uvicorn app.main:app --reload  

5. (Optional) Run Streamlit

streamlit run streamlit_app/app.py  

---

## API Access

Swagger UI:  
http://localhost:8000/docs

Main endpoints:
- POST /documents
- GET /documents
- POST /documents/{id}/process

---

## Notes

This project is intended as a demonstration of structured AI workflow orchestration.  
LLM outputs should always be validated before use in production-critical systems.
