from fastapi import APIRouter, Depends
from typing import Annotated

from schemas import TaskAddSchema, TaskGetSchema, TaskId
from repository import TaskRepository


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.post("")
async def add_task(task: Annotated[TaskAddSchema, Depends()]) -> TaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[TaskGetSchema]:
    tasks = await TaskRepository.find_all()
    return tasks
