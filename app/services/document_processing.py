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
        # 1️⃣ Mark as processing
        document.status = "processing"
        await db.commit()

        graph = build_document_graph()

        # 2️⃣ IMPORTANT: initialize full state
        final_state = graph.invoke(
            {
                "document_id": document.id,
                "filename": document.filename,
                "retry_count": 0,
                "validation_passed": False,
                "error": None,
            }
        )

        # 3️⃣ Save extracted data
        document.extracted_data = final_state.get("extracted_data")

        # 4️⃣ Determine final status
        if final_state.get("validation_passed"):
            document.status = "processed"
        else:
            document.status = "failed"

        document.processed_at = datetime.utcnow()

        await db.commit()
        await db.refresh(document)

        return document

    except Exception as e:
        # Hard failure (unexpected crash)
        document.status = "failed"
        await db.commit()

        print("PIPELINE ERROR:", str(e))
        raise
