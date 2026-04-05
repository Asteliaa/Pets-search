from datetime import datetime
from pydantic import BaseModel, ConfigDict


class PhotoResponse(BaseModel):
    id: int
    file_path: str
    original_filename: str
    content_type: str | None = None
    created_at: datetime
    report_id: int

    model_config = ConfigDict(from_attributes=True)