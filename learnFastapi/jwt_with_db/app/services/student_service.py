from database.models import Student


def create_student(db, student):

    new_student = Student(
        name=student.name,
        age=student.age,
        course=student.course
    )

    db.add(new_student)

    db.commit()

    db.refresh(new_student)

    return new_student