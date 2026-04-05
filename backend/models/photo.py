from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from backend.core.database import Base


class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True, index=True)
    file_path = Column(String(255), nullable=False)
    original_filename = Column(String(255), nullable=False)
    content_type = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    report_id = Column(Integer, ForeignKey("reports.id"), nullable=False)