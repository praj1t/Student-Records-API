from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import StudentReport
from app.services import report_service

router = APIRouter(prefix="/students", tags=["reports"])

@router.get(
    "/{student_id}/report",
    response_model=StudentReport,
    operation_id="get_student_report",
    summary="Get a student's report",
)
def get_student_report(student_id: int, db: Session = Depends(get_db)):
    result = report_service.get_student_report(db, student_id)
    if result == "student_not_found":
        raise HTTPException(status_code=404, detail="Student not found")
    return result