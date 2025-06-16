from sqlalchemy.orm import Session
from app.db import models
from app.schemas import task

def get_tasks(db: Session):
    return db.query(models.Task).all()

def get_tasks_by_user(db: Session, user_id: int):
    return db.query(models.Task).filter(models.Task.owner_id == user_id).all()

def create_task(db: Session, task_data: task.TaskCreate, owner_id: int):
    db_task = models.Task(**task_data.dict(), owner_id=owner_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, completed: bool):
    task = db.query(models.Task).get(task_id)
    if task:
        task.completed = completed
        db.commit()
        db.refresh(task)
        return task
    return None

def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).get(task_id)
    if task:
        db.delete(task)
        db.commit()
        return task
    return None
