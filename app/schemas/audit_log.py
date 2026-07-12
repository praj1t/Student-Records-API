from datetime import datetime
from pydantic import BaseModel, ConfigDict, field_validator

class AuditLogResponse(BaseModel):
    id: int
    student_id: int
    subject_id: int
    old_score: float
    new_score: float
    reason: str | None = None
    changed_at: datetime

    model_config = ConfigDict(from_attributes=True)