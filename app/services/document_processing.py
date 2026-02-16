from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.document_model import Document
from app.ai.graph import build_document_graph


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

    try:
        # mark processing
        document.status = "processing"
        await db.commit()

        graph = build_document_graph()

        final_state = graph.invoke(
            {
                "document_id": document.id,
                "filename": document.filename,
            }
        )

        document.extracted_data = final_state.get("extracted_data")
        document.status = "processed"
        document.processed_at = datetime.utcnow()

        await db.commit()
        await db.refresh(document)

        return document

    except Exception as e:
   
        document.status = "failed"
        await db.commit()

        print("PIPELINE ERROR:", str(e))  # shows real reason in terminal
        raise
