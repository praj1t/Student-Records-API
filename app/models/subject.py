from sqlalchemy import Column,Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base
from sqlalchemy.orm import relationship

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, index= True)
    name = Column(String, unique=True, nullable= False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    marks = relationship("Mark", back_populates="subject")
    audit_log = relationship("GradeAuditLog", back_populates="subject")