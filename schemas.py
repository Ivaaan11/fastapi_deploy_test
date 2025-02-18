from pydantic import BaseModel


class TaskAddSchema(BaseModel):
    name: str
    description: str | None = None


class TaskGetSchema(TaskAddSchema):
    id: int


class TaskId(BaseModel):
    ok: bool = True
    task_id: int
