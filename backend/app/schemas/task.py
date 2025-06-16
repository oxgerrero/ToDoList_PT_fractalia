from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    completed: bool

class TaskOut(TaskBase):
    id: int
    completed: bool
    created_at: datetime

    class Config:
        orm_mode = True
