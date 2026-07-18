from datetime import datetime
from pydantic import BaseModel, ConfigDict, field_validator

class SubjectCreate(BaseModel):
    name: str
    @field_validator("name")
    def namechecker(cls, name):
        name = name.strip()
        if name == "":
            raise ValueError("Name cannot be empty")
        return name

class SubjectResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
