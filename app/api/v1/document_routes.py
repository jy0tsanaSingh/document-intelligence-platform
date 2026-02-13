from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.document_model import Document
from .document_schema import DocumentUploadRequest, DocumentResponse
import base64, os

router = APIRouter(prefix="/documents", tags=["Documents"])
UPLOAD_DIR = "uploads"

@router.post("/", response_model=DocumentResponse)
def upload_document(request: DocumentUploadRequest, db: Session = Depends(get_db)):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, request.filename)
    
    # Save file locally
    try:
        with open(file_path, "wb") as f:
            f.write(base64.b64decode(request.content))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {str(e)}")
    
    # Save metadata to DB
    db_doc = Document(
        filename=request.filename,
        filetype=request.filetype,
        filepath=file_path,
        metadata=str(request.metadata) if request.metadata else None
    )
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)
    
    return db_doc
