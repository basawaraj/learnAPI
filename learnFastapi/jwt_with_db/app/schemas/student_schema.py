from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    id: int = Field(..., description="The unique identifier of the student")
    name: str = Field(..., description="The name of the student")
    age: int = Field(..., description="The age of the student")
    course: str = Field(..., description="The course of the student")

