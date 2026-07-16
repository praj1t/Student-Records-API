from app.repositories import student_repository
from app.schemas import StudentCreate


def create_student(db, student_data: StudentCreate):
    created_student = student_repository.create_student(db,student_data.name)
    return created_student

def get_student_by_id(db, student_id : int):
    selected_student = student_repository.get_student_by_id(db, student_id)
    return selected_student

def get_students(db):
    all_students = student_repository.get_students(db)
    return all_students

def delete_student(db, student_id: int):
    selected_student = get_student_by_id(db, student_id)
    if selected_student is None:
        return None
    return student_repository.delete_student(db, selected_student)

def update_student(db, student_id: int, student_data: StudentCreate):
    selected_student = get_student_by_id(db, student_id)
    if selected_student is None:
        return None
    updated_student = student_repository.update_student(db, selected_student, student_data.name)
    return updated_student