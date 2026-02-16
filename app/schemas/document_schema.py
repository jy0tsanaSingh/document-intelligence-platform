from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DocumentCreate(BaseModel):
    filename: str
    filetype: str
    metadata: Optional[dict] = None


class DocumentResponse(BaseModel):
    id: str
    filename: str
    filetype: str
    filepath: str
    metadata: Optional[str] = None
    created_at: Optional[datetime] = None
