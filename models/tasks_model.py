from pydantic import BaseModel

class Group_Task(BaseModel):
    Urgent_task:str
    Regulat_task:str
    Normal_task:str
    Weekend_task:str
    