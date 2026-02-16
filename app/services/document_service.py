from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.document_model import Document
from app.schemas.document_schema import DocumentCreate


async def create_document(
    db: AsyncSession,
    payload: DocumentCreate,
) -> Document:
    document = Document(
        filename=payload.filename,
        status="uploaded",
    )

    db.add(document)

    await db.commit()
    await db.refresh(document)

    return document


async def list_documents(db: AsyncSession):
    result = await db.execute(select(Document))
    return result.scalars().all()
