from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class student(BaseModel):
    name: str
    course: str
    age: int


@app.post("/")
async def create_detail(student:student):
    return{
        "message":"student details added succesfully",
        "name":student.name,
        "course":student.course,
        "age":student.age
    }