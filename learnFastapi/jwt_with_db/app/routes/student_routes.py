from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.student_schema import StudentCreate
from app.services.student_service import create_student 

router = APIRouter()

@router.post("/students", response_model=StudentCreate)
def create_student_endpoint(student: StudentCreate, db: Session = Depends(get_db)):
    try:
        new_student = create_student(db, student)
        return new_student
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 