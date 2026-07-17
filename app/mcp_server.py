# from contextlib import contextmanager
# from datetime import datetime
# from typing import Any
#
# from mcp.server.fastmcp import FastMCP
#
# from app.database import SessionLocal
# from app.schemas import MarkCreate, MarkUpdate, StudentCreate, SubjectCreate
# from app.services import audit_log_service,mark_service,report_service,student_service,subject_service
#
# mcp = FastMCP("StudentReport")
#
#
# @contextmanager
# def get_session():
#     db = SessionLocal()
#     try:
#         yield db
#     except Exception:
#         db.rollback()
#         raise
#     finally:
#         db.close()
#
#
# def convert_datetime(value: datetime | None):
#     return value.isoformat() if value else None
#
#
# def student_dict(student):
#     return {
#         "id": student.id,
#         "name": student.name,
#         "created_at": convert_datetime(student.created_at),
#         "updated_at": convert_datetime(student.updated_at),
#     }
#
#
# def subject_dict(subject):
#     return {
#         "id": subject.id,
#         "name": subject.name,
#         "created_at": convert_datetime(subject.created_at),
#         "updated_at": convert_datetime(subject.updated_at),
#     }
#
#
# def mark_dict(mark):
#     return {
#         "id": mark.id,
#         "student_id": mark.student_id,
#         "subject_id": mark.subject_id,
#         "score": mark.score,
#         "created_at": convert_datetime(mark.created_at),
#         "updated_at": convert_datetime(mark.updated_at),
#     }
#
#
# def audit_log_dict(log):
#     return {
#         "id": log.id,
#         "student_id": log.student_id,
#         "subject_id": log.subject_id,
#         "old_score": log.old_score,
#         "new_score": log.new_score,
#         "reason": log.reason,
#         "changed_at": convert_datetime(log.changed_at),
#     }
#
#
# def check_service_error(result: Any):
#     errors = {
#         "student_not_found": "Student not found",
#         "subject_not_found": "Subject not found",
#         "mark_not_found": "Mark not found",
#         "mark_already_exists": "Mark already exists for this student and subject",
#         "subject_in_use": "Subject cannot be deleted because it has marks or audit history",
#     }
#
#     if isinstance(result, str) and result in errors:
#         raise ValueError(errors[result])
#
#
# @mcp.tool()
# def health_check() -> str:
#     """Check whether the StudentReport MCP server is running."""
#     return "StudentReport MCP server is running"
#
#
# @mcp.tool()
# def create_student(name: str):
#     """Create a student."""
#     with get_session() as db:
#         student = student_service.create_student(db, StudentCreate(name=name))
#         return student_dict(student)
#
#
# @mcp.tool()
# def list_students():
#     """List all students."""
#     with get_session() as db:
#         students = student_service.get_students(db)
#         return [student_dict(student) for student in students]
#
#
# @mcp.tool()
# def get_student(student_id: int):
#     """Get one student by ID."""
#     with get_session() as db:
#         student = student_service.get_student_by_id(db, student_id)
#
#         if student is None:
#             raise ValueError("Student not found")
#
#         return student_dict(student)
#
#
# @mcp.tool()
# def update_student(student_id: int, name: str):
#     """Update a student's name."""
#     with get_session() as db:
#         student = student_service.update_student(
#             db,
#             student_id,
#             StudentCreate(name=name),
#         )
#
#         if student is None:
#             raise ValueError("Student not found")
#
#         return student_dict(student)
#
#
# @mcp.tool()
# def delete_student(student_id: int):
#     """Delete a student."""
#     with get_session() as db:
#         result = student_service.delete_student(db, student_id)
#
#         if result is None:
#             raise ValueError("Student not found")
#
#         return {"message": "Student deleted successfully"}
#
#
# @mcp.tool()
# def create_subject(name: str):
#     """Create a subject."""
#     with get_session() as db:
#         subject = subject_service.create_subject(
#             db,
#             SubjectCreate(name=name),
#         )
#
#         if subject is None:
#             raise ValueError("Subject already exists")
#
#         return subject_dict(subject)
#
#
# @mcp.tool()
# def list_subjects():
#     """List all subjects."""
#     with get_session() as db:
#         subjects = subject_service.get_subjects(db)
#         return [subject_dict(subject) for subject in subjects]
#
#
# @mcp.tool()
# def add_mark(student_id: int, subject_id: int, score: float):
#     """Add a mark for a student and subject."""
#     mark_data = MarkCreate(subject_id=subject_id, score=score)
#
#     with get_session() as db:
#         result = mark_service.create_mark(db, student_id, mark_data)
#         check_service_error(result)
#         return mark_dict(result)
#
#
# @mcp.tool()
# def update_mark(
#     student_id: int,
#     subject_id: int,
#     score: float,
#     reason: str | None = None,
# ):
#     """Update a mark and create an audit log."""
#     mark_data = MarkUpdate(score=score, reason=reason)
#
#     with get_session() as db:
#         result = mark_service.update_mark(
#             db,
#             student_id,
#             subject_id,
#             mark_data,
#         )
#
#         check_service_error(result)
#         return mark_dict(result)
#
#
# @mcp.tool()
# def get_audit_logs(student_id: int):
#     """Get a student's mark-change history."""
#     with get_session() as db:
#         result = audit_log_service.get_audit_logs_by_student(
#             db,
#             student_id,
#         )
#
#         check_service_error(result)
#         return [audit_log_dict(log) for log in result]
#
# @mcp.tool()
# def delete_subject(subject_id: int):
#     """Delete an unused subject."""
#     with get_session() as db:
#         result = subject_service.delete_subject(db, subject_id)
#         check_service_error(result)
#
#         return {"message": "Subject deleted successfully"}
#
# @mcp.tool()
# def get_student_report(student_id: int):
#     """Generate a student's academic report."""
#     with get_session() as db:
#         result = report_service.get_student_report(db, student_id)
#         check_service_error(result)
#         return result
#
#
# if __name__ == "__main__":
#     mcp.run()