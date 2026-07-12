from fastapi import FastAPI
from app.api.students import router as students_router


app = FastAPI()

app.include_router(students_router)

@app.get("/")
def healthcheck():
    return {"message": "Student records api is currently running"}

# @app.get("/test-report")
# def averagegrade():
#     students = database.open_file()
#     marks = students[0]["marks"]
#     average = utils.average(marks)
#     grade = utils.gradegetter(average)
#     return {
#         "Marks": marks,
#         "Average": average,
#         "Grade": grade
#     }
# @app.get("/students")
# def showstudents():
#     students = database.open_file()
#     return students
#
# @app.get("/students/{studentid}")
# def showstudents(studentid: int):
#     students = database.open_file()
#     for i in students:
#         if i["id"] == studentid:
#             return i
#
#     raise HTTPException(status_code=404, detail="Student was not found")
#
# @app.get("/students/{studentid}/report")
# def studentreports(studentid: int):
#     students = database.open_file()
#     for i in students:
#         if i["id"] == studentid:
#             marks = i["marks"]
#             average = utils.average(marks)
#             grade = utils.gradegetter(average)
#             structure = {"name": i["name"], "id": i["id"], "marks": i["marks"],
#                          "average": average, "grade": grade}
#             return structure
#
# # @app.post("/students")
# # def post_funct(studentdata: Student):
# #     students = database.open_file()
# #     student_dict = studentdata.model_dump()
# #     student_dict["id"] = utils.idgen(students)
# #     students.append(student_dict)
# #     database.write_file(students)
# #     return student_dict
#
# @app.delete("/students/{studentid}")
# def deletestudent(studentid: int):
#     students = database.open_file()
#     for i in students:
#         if i["id"] == studentid:
#             students.remove(i)
#             database.write_file(students)
#             return {"message": "Student was successfully deleted"}
#
#     raise HTTPException(status_code=404, detail="Student was not found")
#
# @app.put("/students/{studentid}")
# def editstudent(studentid: int, studentdata: Student):
#     students = database.open_file()
#     student_dict = studentdata.model_dump()
#     for i in students:
#         if i["id"] == studentid:
#             i["name"] = student_dict["name"]
#             i["marks"] = student_dict["marks"]
#             database.write_file(students)
#             return i
#
#     raise HTTPException(status_code=404, detail="Student was not found")