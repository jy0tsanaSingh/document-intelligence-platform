from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.document_model import Document
from app.schemas.document_schema import DocumentCreate


async def create_document(
    db: AsyncSession,
    payload: DocumentCreate,
) -> Document:
    new_doc = Document(
        filename=payload.filename,
        filetype=payload.filetype,
        metadata=str(payload.metadata) if payload.metadata else None,
    )

    db.add(new_doc)
    await db.commit()
    await db.refresh(new_doc)

    return new_doc


async def list_documents(db: AsyncSession):
    result = await db.execute(select(Document))
    return result.scalars().all()
