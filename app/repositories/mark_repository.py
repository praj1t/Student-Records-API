from app.models import Mark

def get_mark_by_student_and_subject(db, student_id, subject_id):
    return db.query(Mark).filter(Mark.student_id == student_id).filter(Mark.subject_id == subject_id).first()

def create_mark(db, student_id, subject_id, score):
    created_mark = Mark(student_id= student_id, subject_id= subject_id, score= score)
    db.add(created_mark)
    db.commit()
    db.refresh(created_mark)
    return created_mark

def update_mark(db, mark, new_score):
    mark.score = new_score
    db.commit()
    db.refresh(mark)
    return mark
