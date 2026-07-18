from app.models import Subject
from sqlalchemy.orm import Session


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

def get_subject_by_id(db, subject_id):
    return db.query(Subject).filter(Subject.id == subject_id).first()

def delete_subject(db: Session, subject):
    db.delete(subject)
    db.commit()

