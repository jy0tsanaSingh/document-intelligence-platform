from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.document_model import Document, DocumentStatus


async def process_document(
    db: AsyncSession,
    document_id: str,
) -> Document:
    result = await db.execute(
        select(Document).where(Document.id == document_id)
    )
    document = result.scalar_one_or_none()

    if not document:
        raise ValueError("Document not found")

    # Move to PROCESSING
    document.status = DocumentStatus.PROCESSING.value
    await db.commit()

    # ---- Simulated processing ----

    document.status = DocumentStatus.PROCESSED.value
    document.processed_at = datetime.utcnow()

    await db.commit()
    await db.refresh(document)

    return document
