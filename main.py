from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import create_tables, drop_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print("The db has been cleaned up")
    await create_tables()
    print("The database is ready to work")
    yield
    print("Turning off")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
