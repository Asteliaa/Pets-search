from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ReportCreate(BaseModel):
    report_type: str
    title: str
    description: str | None = None
    animal_type: str
    breed: str | None = None
    color: str | None = None
    location_text: str | None = None
    user_id: int


class ReportResponse(BaseModel):
    id: int
    report_type: str
    title: str
    description: str | None = None
    animal_type: str
    breed: str | None = None
    color: str | None = None
    location_text: str | None = None
    status: str
    created_at: datetime
    user_id: int

    model_config = ConfigDict(from_attributes=True)