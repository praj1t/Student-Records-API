from pydantic import BaseModel, ConfigDict

class ReportMark(BaseModel):
    subject: str
    score: float

class StudentReport(BaseModel):
    student_id: int
    name: str
    marks: list[ReportMark]
    average: float
    letter_grade: str