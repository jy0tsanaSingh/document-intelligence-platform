from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.document_schema import DocumentResponse
from app.services.document_processing import process_document

router = APIRouter()


@router.post("/{document_id}/process", response_model=DocumentResponse)
async def process_document_api(
    document_id: str,
    db: AsyncSession = Depends(get_db),
):
    try:
        return await process_document(db, document_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Document not found")
