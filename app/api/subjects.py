from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends,HTTPException

from app.database import get_db
from app.schemas import SubjectCreate, SubjectResponse
from app.services import subject_service

router = APIRouter(prefix="/subjects", tags=["subjects"])

@router.post(
    "/",
    response_model=SubjectResponse,
    operation_id="create_subject",
    summary="Create a subject",
)
def create_subject(subject_data: SubjectCreate, db: Session = Depends(get_db)):
    created_subject = subject_service.create_subject(db, subject_data)
    if created_subject is None:
        raise HTTPException(status_code=409, detail="Subject already exists")
    return created_subject

@router.get(
    "/",
    response_model=list[SubjectResponse],
    operation_id="get_subjects",
    summary="List all subjects",
)
def get_subjects(db: Session = Depends(get_db)):
    all_subjects = subject_service.get_subjects(db)
    return all_subjects