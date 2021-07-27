from fastapi import FastAPI
from pydantic import BaseModel

myapp = FastAPI()

# temp database
fdb = []

# course model to store courses
class Student(BaseModel):
    id: int
    name: str
    age: int
    city: str
    state: str
    phone: int


@myapp.get("/")
def ready():
    return {"Greetings":"Welcome Here"}


@myapp.get("/details")
def get_students():
    return fdb


@myapp.get("/details/{student_id}")
def get_a_student(student_id: int):
    student = student_id - 1
    return fdb[student]


@myapp.post("/details")
def add_student(student: Student):
    fdb.append(student.dict())
    return fdb[-1]


@myapp.delete("/details/{student_id}")
def delete_student(student_id: int):
    fdb.pop(student_id-1)
    return {"task": "deletion successful"}
