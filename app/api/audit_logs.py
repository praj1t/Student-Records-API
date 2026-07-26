from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import AuditLogResponse
from app.services import audit_log_service

router = APIRouter(prefix="/students", tags=["audit logs"])

@router.get(
    "/{student_id}/audit-log",
    response_model=list[AuditLogResponse],
    operation_id="get_student_audit_logs",
    summary="Get a student's audit logs",
)
def get_audit_logs_by_student(student_id: int,db: Session = Depends(get_db)):
    result = audit_log_service.get_audit_logs_by_student(db, student_id)
    if result == "student_not_found":
        raise HTTPException(status_code=404, detail="Student not found")
    return result