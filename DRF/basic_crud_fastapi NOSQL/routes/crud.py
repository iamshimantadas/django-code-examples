from fastapi import APIRouter, status
from database.models import Student

from database.schemas import Students, UpdateStudent

from bson.objectid import ObjectId

router = APIRouter()


@router.post("/student/", status_code=status.HTTP_200_OK, tags=['student'])
async def create_student(users: Students):
    try:
        stu_obj = Student(name=users.name, phone=users.phone, email=users.email, address=users.address)
        await stu_obj.insert()
        return {"status":"record inserted"}
    except Exception as e:
        print(e)
        return {"status":"error occured"}

@router.get("/student/", status_code=status.HTTP_200_OK, tags=['student'])
async def read_students():
    students = await Student.find_all().to_list()
    return students

@router.put("/student/", status_code=status.HTTP_200_OK, tags=['student'])
async def update_student(userid, users: UpdateStudent):
    objInstance = ObjectId(userid)
    try:
        stu_obj = await Student.find_one({"_id": objInstance})
        
        if users.name:
            await stu_obj.set({Student.name : users.name})
        if users.address: 
            await stu_obj.set({Student.address : users.address})
        if users.phone:
            await stu_obj.set({Student.phone : users.phone})
        if users.email:
            await stu_obj.set({Student.email : users.email})

        return {"status":"record updated"}
    except Exception as e:
        print(e)
        return {"status":"user id not exist!"}
    
@router.delete("/student/", status_code=status.HTTP_200_OK, tags=['student'])
async def delete_user(userid : str):
    objInstance = ObjectId(userid)
    try:
        stu_obj = await Student.find_one({"_id": objInstance})
        await stu_obj.delete()
        return {"status":"collection deleted"}     
    except Exception as e:
        print(e)
        return {"status":"something error occured"}        
    
