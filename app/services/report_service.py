from app.repositories import student_repository
from app.utils import average, gradegetter


def get_student_report(db, student_id: int):
    student = student_repository.get_student_by_id(db, student_id)

    if student is None:
        return "student_not_found"
    report_marks = []
    for mark in student.marks:
        report_marks.append({"subject": mark.subject.name,"score": mark.score})

    scores = [mark.score for mark in student.marks]
    if scores:
        student_average = sum(scores) / len(scores)
        letter_grade = gradegetter(student_average)
    else:
        student_average = 0.0
        letter_grade = gradegetter(student_average)

    return {"student_id": student.id,"name": student.name,"marks": report_marks,"average": student_average,"letter_grade": letter_grade}