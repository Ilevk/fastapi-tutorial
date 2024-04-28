from fastapi import FastAPI

from app.core.lifespan import lifespan
from app.routers import router

app = FastAPI(lifespan=lifespan)

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
