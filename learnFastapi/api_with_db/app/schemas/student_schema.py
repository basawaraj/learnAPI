from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    name: str = Field(..., description="The name of the student")
    age: int = Field(..., description="The age of the student")
    course: str = Field(..., description="The course of the student")

