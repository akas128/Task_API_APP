from re import S
from django.apps import AppConfig
from fastapi import APIRouter

from models.tasks_model import Group_Task
from config.database import collection_name

from schemas.tasks_schemas import task_serializer,tasks_serializer

from bson import ObjectId
from bson.objectid import ObjectId


task_api_router = APIRouter() 

#retrive
@task_api_router.get("/Get_all_task")
async def get_task():
    tasks=tasks_serializer(collection_name.find())
    return tasks

@task_api_router.get("/Single_User/{id}")
async def get_task(id:str):
    return task_serializer(collection_name.find_one({"_id":ObjectId(id)}))

#post
@task_api_router.post("/Create_tasks")
async def create_task(task:Group_Task):
    _id = collection_name.insert_one(dict(task))
    return task_serializer(collection_name.find_one({"_id": _id.inserted_id}))

#update
@task_api_router.put("/update_tasks/{id}")
async def update_task(id:str, task:Group_Task):
    collection_name.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(task)
    })
    return tasks_serializer(collection_name.find({"_id":ObjectId(id)}))

#delete
@task_api_router.delete("/delete_tasks/{id}")
async def delete_task(id:str):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})
    return {"Status":"Delete task Succesfully"}

#delete all tasks 
@task_api_router.delete("/delete_all_task")
async def delete_all_task():
    delete_tasks = collection_name.delete_many({})
    return {"Status" : "Delete all tasks Succesfully"}