from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import models
from app.db.database import SessionLocal
from app.schemas import task as task_schema
from app.crud import tasks as crud
from app.auth import get_current_user

router = APIRouter(
    prefix="/tasks",
    tags=["Tareas"],
    responses={404: {"description": "No encontrado"}}
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[task_schema.TaskOut])
def read_tasks(db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    """
    Obtener todas las tareas del usuario autenticado
    """
    return crud.get_tasks_by_user(db, user.id)

@router.post("/", response_model=task_schema.TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(task: task_schema.TaskCreate, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    """
    Crear una nueva tarea para el usuario autenticado
    """
    return crud.create_task(db, task, owner_id=user.id)

@router.put("/{task_id}", response_model=task_schema.TaskOut)
def update_task(task_id: int, update: task_schema.TaskUpdate, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    """
    Cambiar el estado de una tarea del usuario autenticado
    """
    task = db.query(models.Task).filter_by(id=task_id, owner_id=user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    task.completed = update.completed
    db.commit()
    db.refresh(task)
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    """
    Eliminar una tarea del usuario autenticado
    """
    task = db.query(models.Task).filter_by(id=task_id, owner_id=user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    db.delete(task)
    db.commit()
