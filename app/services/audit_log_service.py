from app.repositories import audit_log_repository, student_repository

def get_audit_logs_by_student(db, student_id: int):
    selected_student = student_repository.get_student_by_id(db, student_id)
    if selected_student is None:
        return "student_not_found"
    return audit_log_repository.get_audit_logs_by_student(db, student_id)