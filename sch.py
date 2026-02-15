from pydantic import BaseModel,ConfigDict
from mod import Taskstatus

class TaskBase(BaseModel):
    task:str
    status:Taskstatus
    description:str| None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    task: str |None =None
    status:Taskstatus |None =None
    description:str |None =None

class Task(TaskBase):
    id:int 
    model_config = ConfigDict(from_attributes=True)
     #class Config():
        #from_attributes=True
    