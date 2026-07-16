from app.models import Subject


def create_subject(db, name):
    subject = Subject(name= name)
    db.add(subject)
    db.commit()
    db.refresh(subject)
    return subject

def get_subjects(db):
    return db.query(Subject).all()

def get_subject_by_name(db, name):
    return db.query(Subject).filter(Subject.name == name).first()

