from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models.task import Task
from ..models.user import User, UserRole
from ..schemas import TaskCreate, TaskUpdate, Task as TaskSchema
from ..auth.utils import get_current_active_user
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=TaskSchema)
async def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    db_task = Task(
        **task.dict(),
        owner_id=current_user.id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/", response_model=List[TaskSchema])
async def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    if current_user.role == UserRole.ADMIN:
        tasks = db.query(Task).offset(skip).limit(limit).all()
    else:
        tasks = db.query(Task).filter(Task.owner_id == current_user.id).offset(skip).limit(limit).all()
    return tasks

@router.get("/{task_id}", response_model=TaskSchema)
async def read_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.owner_id != current_user.id and current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return task

@router.put("/{task_id}", response_model=TaskSchema)
async def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if db_task.owner_id != current_user.id and current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    update_data = task_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_task, field, value)
    
    db_task.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_task)
    return db_task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if db_task.owner_id != current_user.id and current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    db.delete(db_task)
    db.commit()
    return None