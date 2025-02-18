from database import async_session, TaskOrm
from schemas import TaskAddSchema, TaskGetSchema
from sqlalchemy import select


class TaskRepository:
    @classmethod
    async def add_one(cls, data: TaskAddSchema) -> int:
        async with async_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)

            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[TaskGetSchema]:
        async with async_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [TaskGetSchema.model_validate(task) for task in task_models]

            return task_models
