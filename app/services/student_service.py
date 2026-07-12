from app.repositories import student_repository
from app.schemas import StudentCreate


def create_student(db, student_data: StudentCreate):
    created_student = student_repository.create_student(db,student_data.name)
    return created_student