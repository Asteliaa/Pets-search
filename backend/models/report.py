from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.core.database import Base


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    report_type = Column(String(20), nullable=False)   # lost / found
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    animal_type = Column(String(50), nullable=False)   # cat / dog
    breed = Column(String(100), nullable=True)
    color = Column(String(100), nullable=True)
    location_text = Column(String(255), nullable=True)

    status = Column(String(20), default="open", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="reports")