from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.document_schema import DocumentCreate, DocumentResponse
from app.services.document_service import create_document, list_documents

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("/", response_model=DocumentResponse)
async def create_document_api(
    payload: DocumentCreate,
    db: AsyncSession = Depends(get_db),
):
    return await create_document(db, payload)


@router.get("/", response_model=list[DocumentResponse])
async def list_documents_api(
    db: AsyncSession = Depends(get_db),
):
    return await list_documents(db)
