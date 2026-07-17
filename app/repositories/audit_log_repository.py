from app.models import GradeAuditLog

def create_audit_log(db,student_id,subject_id,old_score,new_score,reason):
    audit_log = GradeAuditLog(student_id=student_id,subject_id=subject_id,old_score=old_score,new_score=new_score,reason=reason)
    db.add(audit_log)
    db.commit()
    db.refresh(audit_log)
    return audit_log

def get_audit_logs_by_student(db, student_id):
    return db.query(GradeAuditLog).filter(GradeAuditLog.student_id == student_id).all()