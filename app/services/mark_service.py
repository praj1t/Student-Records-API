from app.repositories import mark_repository, student_repository, subject_repository, audit_log_repository
from app.schemas import MarkCreate, MarkUpdate, MarkResponse

def create_mark(db, student_id: int, mark_data:MarkCreate):
    student = student_repository.get_student_by_id(db, student_id)
    if student is None:
        return "student_not_found"
    subject = subject_repository.get_subject_by_id(db, mark_data.subject_id)
    if subject is None:
        return "subject_not_found"
    existing_mark = mark_repository.get_mark_by_student_and_subject(db,student_id,mark_data.subject_id)
    if existing_mark is not None:
        return "mark_already_exists"

    created_mark = mark_repository.create_mark(db,student_id,mark_data.subject_id,mark_data.score)
    return created_mark

def update_mark(db, student_id: int,subject_id: int,mark_data: MarkUpdate):
    student = student_repository.get_student_by_id(db, student_id)
    if student is None:
        return "student_not_found"
    subject = subject_repository.get_subject_by_id(db, subject_id)
    if subject is None:
        return "subject_not_found"

    existing_mark = mark_repository.get_mark_by_student_and_subject(db,student_id,subject_id)
    if existing_mark is None:
        return "mark_not_found"
    old_score = existing_mark.score
    updated_mark = mark_repository.update_mark(db, existing_mark, mark_data.score)
    audit_log_repository.create_audit_log(db,student_id,subject_id,old_score,mark_data.score,mark_data.reason)
    return updated_mark