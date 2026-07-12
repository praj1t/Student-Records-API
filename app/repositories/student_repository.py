from app.models import Student

def create_student(db,name):
    student = Student(name=name)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student