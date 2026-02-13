from fastapi import FastAPI
from api.v1.health import router as health_router
from api.v1.documents import router as documents_router


def create_application() -> FastAPI:
    app = FastAPI(
        title="Document Intelligence Platform",
        version="1.0.0"
    )

    app.include_router(health_router, prefix="/api/v1", tags=["Health"])
    app.include_router(documents_router, prefix="/api/v1/documents", tags=["Documents"])

    return app


app = create_application()