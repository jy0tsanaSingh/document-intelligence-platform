from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.document_schema import DocumentCreate, DocumentResponse
from app.services.document_service import create_document, list_documents
from app.services.document_processing import process_document

router = APIRouter() 


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


@router.post("/{document_id}/process", response_model=DocumentResponse)
async def process_document_api(
    document_id: str,
    db: AsyncSession = Depends(get_db),
):
    try:
        return await process_document(db, document_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Document processing failed. Check server logs.",
        )
