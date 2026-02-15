from fastapi import FastAPI,Depends,HTTPException
from db_td import SessionLocal,engine
import crude,mod,sch
from sch import Task,TaskCreate,TaskUpdate
from sqlalchemy.orm import Session

mod.Base.metadata.create_all(bind=engine)

app= FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks/",response_model=Task,status_code=201)
def create_task(task:TaskCreate,db:Session=Depends(get_db)):
    try:
        db_task=crude.create_task(db=db,task=task)
        return db_task

    except Exception as e:
        print("!!! ERROR FOUND !!!")
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Message: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    

#Get method
@app.get("/task/",response_model=list[Task])
def read_tasks(Skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    tasks=crude.get_tasks(db=db,skip=Skip,limit=limit)
    return tasks

@app.get("/tasks/{task_id}",response_model=Task)
def read_task(task_id:int,db:Session=Depends(get_db)):
    db_task=crude.get_task(db=db,task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Item not Found")
    return db_task
#Update
@app.patch("/tasks/{task_id}", response_model=sch.Task)
def update_task_status(task_id: int, task_update: sch.TaskUpdate, db: Session = Depends(get_db)):
    db_task = crude.update_task(db, task_id=task_id, task_update=task_update)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
#Delete
@app.delete("/tasks/{task_id}",response_model=dict)
def delete_task(task_id:int,db:Session=Depends(get_db)):
    if crude.delete_task(db=db,task_id=task_id):
        return {"Message" : f"Task with id {task_id} is deleted from database"}
    raise HTTPException(status_code=404 , detail="Item not Found") 
