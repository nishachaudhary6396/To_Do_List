from fastapi import APIRouter, HTTPException
from schemas import TaskCreate, TaskUpdate
from crud import (
    create_task,
    get_tasks,
    get_task_by_id,
    update_task,
    delete_task
)

router = APIRouter()


# Create Task API
@router.post("/tasks")
def add_task(task: TaskCreate):

    return create_task(task)


# Get All Tasks API
@router.get("/tasks")
def fetch_tasks():

    return get_tasks()


# Get Task By ID API
@router.get("/tasks/{task_id}")
def fetch_task(task_id: int):

    task = get_task_by_id(task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


# Update Task API
@router.put("/tasks/{task_id}")
def edit_task(task_id: int, task: TaskUpdate):

    updated_task = update_task(task_id, task)

    if not updated_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return updated_task


# Delete Task API
@router.delete("/tasks/{task_id}")
def remove_task(task_id: int):

    deleted_task = delete_task(task_id)

    if not deleted_task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return deleted_task