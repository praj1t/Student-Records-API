from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends,HTTPException

from app.database import get_db
from app.schemas import StudentCreate, StudentResponse
from app.services import student_service

router = APIRouter(prefix="/students", tags=["students"])

@router.post("/", response_model=StudentResponse)
def create_student(student_data: StudentCreate, db: Session = Depends(get_db)):
    created_student = student_service.create_student(db, student_data)
    return created_student

@router.get("/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    all_students = student_service.get_students(db)
    return all_students

@router.get("/{student_id}", response_model=StudentResponse)
def get_student_by_id(student_id: int, db: Session = Depends(get_db)):
    selected_student = student_service.get_student_by_id(db, student_id)
    if selected_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return selected_student

@router.put("/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student_data: StudentCreate, db: Session = Depends(get_db)):
    updated_student = student_service.update_student(db,student_id, student_data)
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    deleted_student = student_service.delete_student(db,student_id)
    if deleted_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
