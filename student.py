from fastapi import FastAPI
from pydantic import BaseModel

myapp = FastAPI()


# temp database
fdb = []


#take input
'''
class Student(BaseModel):
    id: int
    name: str
    age: int
    city: str
    state: str
    phone: int
'''


#welcome page
'''
@myapp.get("/")
def ready():
    return {"Greetings":"Welcome Here"}
'''


#Show all students
'''
@myapp.get("/details")
def get_students():
    return fdb
'''


#Show one student
'''
@myapp.get("/details/{student_id}")
def get_a_student(student_id: int):
    student = student_id - 1
    return fdb[student]
'''




#Add student
'''
@myapp.post("/details")
def add_student(student: Student):
    fdb.append(student.dict())
    return fdb[-1]
'''


#Delete Student
'''
@myapp.delete("/details/{student_id}")
def delete_student(student_id: int):
    fdb.pop(student_id-1)
    return {"task": "deletion successful"}
'''
