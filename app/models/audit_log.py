from sqlalchemy import Column,Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.sql import func
from app.database import Base
from sqlalchemy.orm import relationship


class GradeAuditLog(Base):
    __tablename__ = "grade_audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer,ForeignKey("students.id"), nullable=False)
    subject_id = Column(Integer,ForeignKey("subjects.id"), nullable=False)
    old_score = Column(Float, nullable= False)
    new_score = Column(Float, nullable= False)
    reason = Column(String,nullable=True)
    changed_at = Column(DateTime, server_default=func.now())
    student = relationship("Student", back_populates="audit_logs")
    subject = relationship("Subject", back_populates="audit_logs")
