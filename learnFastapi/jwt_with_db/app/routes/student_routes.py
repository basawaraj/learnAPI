from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.student_schema import StudentCreate
from app.services.student_service import create_student ,get_all_students, get_student_by_id, update_student, delete_student

router = APIRouter()

@router.post("/students", response_model=StudentCreate)
def create_student_endpoint(student: StudentCreate, db: Session = Depends(get_db)):
    try:
        new_student = create_student(db, student)
        return new_student
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 
    
@router.get("/students")
def get_all_students_endpoint(db: Session = Depends(get_db)):
    try:
        students = get_all_students(db)
        return students
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/students/{student_id}")
def get_student_by_id_endpoint(student_id: int, db: Session = Depends(get_db)):
    try:
        student = get_student_by_id(db, student_id)
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        return student
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/students/{student_id}")
def update_student_endpoint(student_id: int, student_data: StudentCreate, db: Session = Depends(get_db)):
    try:
        updated_student = update_student(db, student_id, student_data)
        if updated_student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        return updated_student
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/students/{student_id}")
def delete_student_endpoint(student_id: int, db: Session = Depends(get_db)):
    try:
        deleted_student = delete_student(db, student_id)
        if deleted_student is None:
            raise HTTPException(status_code=404, detail="Student not found")
        return {"message": "Student deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))