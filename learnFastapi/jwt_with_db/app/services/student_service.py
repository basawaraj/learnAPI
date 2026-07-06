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