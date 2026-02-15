from sqlalchemy.orm import Session
from sch import TaskCreate,TaskUpdate
import mod,sch
from first import first

def create_task(db:Session, task:TaskCreate):
    db_task=mod.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task

#get method
def get_tasks(db:Session,skip:int=0,limit:int=100):
    return db.query(mod.Task).offset(skip).limit(limit).all()

def get_task(db:Session,task_id:int):
    return db.query(mod.Task).filter(mod.Task.id==task_id).first()
#update
# Function to update a task (specifically the status)
def update_task(db: Session, task_id: int, task_update: sch.TaskUpdate):
    db_task = db.query(mod.Task).filter(mod.Task.id == task_id).first()
    
    if db_task:
        # Convert Pydantic object to a dict, excluding unset fields
        update_data = task_update.model_dump(exclude_unset=True)
        
        for key, value in update_data.items():
            setattr(db_task, key, value)
        
        db.commit()
        db.refresh(db_task)
    return db_task
#delete
def delete_task(db:Session,task_id:int):
    db_task=db.query(mod.Task).filter(mod.Task.id==task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False

