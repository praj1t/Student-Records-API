from app.repositories import subject_repository, student_repository
from app.schemas import SubjectCreate
from sqlalchemy.orm import Session

def create_subject(db, subject_data: SubjectCreate):
    checking_subject = subject_repository.get_subject_by_name(db, subject_data.name)
    if checking_subject is not None:
        return None
    else:
        created_subject = subject_repository.create_subject(db,subject_data.name)
    return created_subject

def get_subjects(db):
    all_subjects = subject_repository.get_subjects(db)
    return all_subjects

def delete_subject(db: Session, subject_id: int):
    subject = subject_repository.get_subject_by_id(db, subject_id)
    if subject is None:
        return "subject_not_found"

    if subject.marks or subject.audit_logs:
        return "subject_in_use"

    subject_repository.delete_subject(db, subject)
    return True