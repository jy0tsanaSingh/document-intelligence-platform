from fastapi import FastAPI
from app.db.session import Base, engine
from app.api.v1 import document_routes
from app.api.v1 import health

app = FastAPI(title="Document Intelligence Platform")

# Create tables automatically (dev only)
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(document_routes.router, prefix="/api/v1", tags=["Documents"])
