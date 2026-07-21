from app.database.models import Student
from datetime import datetime, timezone




def create_student(db, student):

    new_student = Student(
        name=student.name,
        age=student.age,
        course=student.course,
        created_at = datetime.now(timezone.utc)
    )

    db.add(new_student)

    db.commit()

    db.refresh(new_student)

    return new_student

def get_all_students(db):
    return db.query(Student).all()

def get_student_by_id(db, student_id):
    return db.query(Student).filter(Student.id == student_id).first()


def update_student(db, student_id, student_data):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        return None

    student.name = student_data.name
    student.age = student_data.age
    student.course = student_data.course
    db.commit()
    db.refresh(student)
    return student

def delete_student(db, student_id):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        return None

    db.delete(student)
    db.commit()
    return student

