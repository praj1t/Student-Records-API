from sqlalchemy import Column,Integer, String, DateTime, ForeignKey, Float, UniqueConstraint
from sqlalchemy.sql import func
from app.database import Base
from sqlalchemy.orm import relationship


class Mark(Base):
    __tablename__ = "marks"
    __table_args__ = (UniqueConstraint("student_id","subject_id", name="unique_student_subject_mark"),)
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer,ForeignKey("students.id"), nullable=False)
    subject_id = Column(Integer,ForeignKey("subjects.id"), nullable=False)
    score = Column(Float, nullable= False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    student = relationship("Student", back_populates="marks")
    subject = relationship("Subject", back_populates="marks")
