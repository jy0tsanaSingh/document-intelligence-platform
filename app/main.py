from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.api.v1.document_routes import router as document_router

app = FastAPI()


# Create tables on startup (async-safe)
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# ✅ Include your routes
app.include_router(
    document_router,
    prefix="/documents",
    tags=["Documents"],
)
