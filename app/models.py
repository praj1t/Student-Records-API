from pydantic import BaseModel
from pydantic import field_validator

class Student(BaseModel):
    name:str
    marks:dict
    @field_validator("name")
    def namechecker(cls, name):
        name = name.strip()
        if name == "":
            raise ValueError("Name cannot be empty")

        return name

    @field_validator("marks")
    def markschecker(cls, marks):
        expected_subjects = {"English","Maths","Physics","Programming"}
        submitted_subjects = marks.keys()
        if expected_subjects != set(submitted_subjects):
            raise ValueError("Subjects must be English, Maths, Physics, and Programming")
        for subject,mark in marks.items():
            if type(mark) != int and type(mark) != float:
                raise ValueError("Marks have to be either an integer or a float")
            if mark < 0 or mark > 100:
                raise ValueError("Marks have to be between 0 and 100")
        return marks