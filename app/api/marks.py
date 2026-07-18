from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends,HTTPException

from app.database import get_db
from app.models import Mark
from app.schemas import MarkCreate, MarkUpdate, MarkResponse
from app.services import mark_service

router = APIRouter(prefix="/students", tags=["marks"])

@router.post("/{student_id}/marks", response_model=MarkResponse)
def create_mark(student_id: int, mark_data: MarkCreate, db: Session = Depends(get_db)):
    created_mark = mark_service.create_mark(db,student_id, mark_data)
    if created_mark == "student_not_found":
        raise HTTPException(status_code=404, detail="Student not found")
    elif created_mark == "subject_not_found":
        raise HTTPException(status_code=404, detail="Subject not found")
    elif created_mark == "mark_already_exists":
        raise HTTPException(status_code=409, detail="Mark already exists for this student and subject")
    else:
        return created_mark

@router.put("/{student_id}/marks/{subject_id}", response_model=MarkResponse)
def update_mark(student_id: int,subject_id: int,mark_data: MarkUpdate, db: Session = Depends(get_db)):
    updated_mark = mark_service.update_mark(db, student_id, subject_id, mark_data)
    if updated_mark == "student_not_found":
        raise HTTPException(status_code=404, detail="Student not found")
    elif updated_mark == "subject_not_found":
        raise HTTPException(status_code=404, detail="Subject not found")
    elif updated_mark == "mark_not_found":
        raise HTTPException(status_code=404, detail="Mark not found")
    else:
        return updated_mark
