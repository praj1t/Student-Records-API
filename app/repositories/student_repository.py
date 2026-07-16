from app.models import Student

def create_student(db,name):
    student = Student(name=name)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def get_student_by_id(db, student_id):
    return db.query(Student).filter(Student.id == student_id).first()

def get_students(db):
    return db.query(Student).all()

def update_student(db, student, new_name):
    student.name = new_name
    db.commit()
    db.refresh(student)
    return student

def delete_student(db, student):
    db.delete(student)
    db.commit()
    return True

