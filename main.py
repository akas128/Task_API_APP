from fastapi import FastAPI
from routes.tasks_route import task_api_router

app = FastAPI()

app.include_router(task_api_router)

