from datetime import datetime
from pydantic import BaseModel, ConfigDict, field_validator

class MarkCreate(BaseModel):
    subject_id: int
    score: float

    @field_validator("score")
    def scorechecker(cls, score):
        if score < 0:
            raise ValueError("Mark entered should be between 0-100!")
        if score > 100:
            raise ValueError("Mark entered should be between 0-100!")
        return score

class MarkUpdate(BaseModel):
    score: float
    reason: str | None = None

    @field_validator("score")
    def scorechecker(cls, score):
        if score < 0:
            raise ValueError("Mark entered should be between 0-100!")
        if score > 100:
            raise ValueError("Mark entered should be between 0-100!")
        return score

class MarkResponse(BaseModel):
    id: int
    student_id: int
    subject_id: int
    score: float
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

