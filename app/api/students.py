from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.database import get_db
from app.schemas import StudentCreate, StudentResponse
from app.services import student_service

router = APIRouter(prefix="/students", tags=["students"])

@router.post("/", response_model=StudentResponse)
def create_student(student_data: StudentCreate, db: Session = Depends(get_db)):
    created_student = student_service.create_student(db, student_data)
    return created_student
