from fastapi import FastAPI
from app import utils
from app import database
from fastapi import HTTPException

app = FastAPI()

@app.get("/")

def healthcheck():
    return {"message": "Student records api is currently running"}



@app.get("/test-report")
def averagegrade():
    students = database.open_file()
    marks = students[0]["marks"]
    average = utils.average(marks)
    grade = utils.gradegetter(average)
    return {
        "Marks": marks,
        "Average": average,
        "Grade": grade
    }
@app.get("/students")
def showstudents():
    students = database.open_file()
    return students

@app.get("/students/{studentid}")
def showstudents(studentid: int):
    students = database.open_file()
    for i in students:
        if i["id"] == studentid:
            return i

    raise HTTPException(status_code=404, detail="Student was not found")

@app.get("/students/{studentid}/report")
def studentreports(studentid: int):
    students = database.open_file()
    for i in students:
        if i["id"] == studentid:
            marks = i["marks"]
            average = utils.average(marks)
            grade = utils.gradegetter(average)
            structure = {"name": i["name"], "id": i["id"], "marks": i["marks"],
                         "average": average, "grade": grade}
            return structure

@app.post("/students")
def post_funct(studentdata: dict):
    students = database.open_file()
    studentdata["id"] = utils.idgen(students)
    students.append(studentdata)
    database.write_file(students)
    return studentdata

@app.delete("/students/{studentid}")
def deletestudent(studentid: int):
    students = database.open_file()
    for i in students:
        if i["id"] == studentid:
            students.remove(i)
            database.write_file(students)
            return {"message": "Student was successfully deleted"}

    raise HTTPException(status_code=404, detail="Student was not found")