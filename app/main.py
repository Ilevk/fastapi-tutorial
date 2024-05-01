from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette_context.middleware import ContextMiddleware

from app.core.config import config
from app.core.lifespan import lifespan
from app.core.middlewares.sqlalchemy import SQLAlchemyMiddleware
from app.core.errors.error import BaseAPIException, BaseAuthExeption
from app.core.errors.handler import api_error_handler, api_auth_error_handler
from app.routers import router

app = FastAPI(lifespan=lifespan, **config.fastapi_kwargs)

app.include_router(router)
app.add_exception_handler(BaseAPIException, api_error_handler)
app.add_exception_handler(BaseAuthExeption, api_auth_error_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SQLAlchemyMiddleware)
app.add_middleware(ContextMiddleware)


@app.get("/")
async def root():
    return {"message": "Hello World"}
