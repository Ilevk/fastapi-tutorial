from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.db.session import ping_db, close_db


@asynccontextmanager
async def lifespan(app: FastAPI):

    await ping_db()

    yield

    await close_db()
