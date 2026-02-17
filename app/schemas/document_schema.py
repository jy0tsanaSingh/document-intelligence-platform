from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DocumentCreate(BaseModel):
    filename: str


class DocumentResponse(BaseModel):
    id: str
    filename: str
    status: str
    extracted_data: Optional[dict] = None
    uploaded_at: Optional[datetime] = None
    processed_at: Optional[datetime] = None

    class Config:
        from_attributes = True
