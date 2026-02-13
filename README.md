# Document Intelligence Platform

AI-powered backend system that extracts structured intelligence from unstructured documents using FastAPI and LLM orchestration.

## Tech Stack

- FastAPI (async REST APIs)
- Streamlit (lightweight demo client)
- SQLAlchemy (async DB)
- LangChain + LangGraph (AI orchestration)

## How to Run

### 1. Create virtual environment
python -m venv env
source env/bin/activate

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run FastAPI
uvicorn app.main:app --reload

### 4. Run Streamlit
streamlit run streamlit_app/app.py

API will be available at:
http://localhost:8000/docs
