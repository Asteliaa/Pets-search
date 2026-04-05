from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict


class ReportType(str, Enum):
    lost = "lost"
    found = "found"


class AnimalType(str, Enum):
    cat = "cat"
    dog = "dog"


class ReportStatus(str, Enum):
    open = "open"
    closed = "closed"


class ReportCreate(BaseModel):
    report_type: ReportType
    title: str
    description: str | None = None
    animal_type: AnimalType
    breed: str | None = None
    color: str | None = None
    location_text: str | None = None
    user_id: int


class ReportResponse(BaseModel):
    id: int
    report_type: ReportType
    status: ReportStatus
    title: str
    description: str | None = None
    animal_type: AnimalType
    breed: str | None = None
    color: str | None = None
    location_text: str | None = None
    created_at: datetime
    user_id: int

    model_config = ConfigDict(from_attributes=True)