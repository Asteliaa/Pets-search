import os
import shutil
from uuid import uuid4

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from backend.api.deps import get_db
from backend.models.photo import Photo
from backend.models.report import Report
from backend.schemas.photo import PhotoResponse

router = APIRouter(prefix="/photos", tags=["photos"])

UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_TYPES = {"image/jpeg", "image/png", "image/webp"}


@router.post("/upload/{report_id}", response_model=PhotoResponse)
def upload_photo(
    report_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    report = db.query(Report).filter(Report.id == report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename is required")

    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Only JPG, PNG, and WEBP are allowed")

    # file.filename уже проверили на None, дальше можно безопасно работать как со строкой
    ext = os.path.splitext(file.filename)[1].lower()
    unique_name = f"{uuid4().hex}{ext}"
    save_path = os.path.join(UPLOAD_DIR, unique_name)

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    photo = Photo(
        file_path=f"/static/uploads/{unique_name}",
        original_filename=file.filename,
        content_type=file.content_type,
        report_id=report_id,
    )
    db.add(photo)
    db.commit()
    db.refresh(photo)

    return photo


@router.get("/report/{report_id}", response_model=list[PhotoResponse])
def list_report_photos(report_id: int, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.id == report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    photos = (
        db.query(Photo)
        .filter(Photo.report_id == report_id)
        .order_by(Photo.id.desc())
        .all()
    )
    return photos