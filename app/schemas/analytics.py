from pydantic import BaseModel

class ClassSummary(BaseModel):
    student_count: int
    subject_count: int
    class_average: float | None
    highest_average: float | None
    lowest_average: float | None

class SubjectPerformance(BaseModel):
    subject: str
    average: float | None
    highest_score: float | None
    lowest_score: float | None
    student_count: int

class TopStudent(BaseModel):
    name: str
    student_id: int
    average: float