from app.repositories import subject_repository, student_repository
from app.schemas import SubjectCreate

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

