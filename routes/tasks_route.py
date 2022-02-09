from django.apps import AppConfig
from fastapi import APIRouter

from models.tasks_model import Group_Task
from config.database import collection_name

from schemas.tasks_schemas import task_serializer,tasks_serializer

from bson import ObjectId

task_api_router = APIRouter() 

#retrive
@task_api_router.get("/")
async def get_task():
    tasks=tasks_serializer(collection_name.find())
    return tasks

@task_api_router.get("/{id}")
async def get_task(id:str):
    return task_serializer(collection_name.find_one({"_id":ObjectId(id)}))

#post
@task_api_router.post("/")
async def create_task(task:Group_Task):
    _id = collection_name.insert_one(dict(task))
    return task_serializer(collection_name.find_one({"_id": _id.inserted_id}))

#update
@task_api_router.put("/{id}")
async def update_task(id:str, task:Group_Task):
    collection_name.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(task)
    })
    return tasks_serializer(collection_name.find({"_id":ObjectId(id)}))

#delete
@task_api_router.delete("/{id}")
async def delete_task(id:str):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})
    return {"Status":"Deleted task Succesfully"}






    