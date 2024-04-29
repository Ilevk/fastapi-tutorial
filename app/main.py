from fastapi import FastAPI

from app.core.lifespan import lifespan
from app.routers import router
from app.core.config import config

app = FastAPI(lifespan=lifespan, **config.fastapi_kwargs)

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
