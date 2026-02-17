from sqlalchemy import Column, String, DateTime, JSON
from sqlalchemy.sql import func
import uuid

from app.db.base import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    filename = Column(String, nullable=False)
    status = Column(String, default="uploaded")

    extracted_data = Column(JSON, nullable=True)

    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    processed_at = Column(DateTime(timezone=True), nullable=True)
