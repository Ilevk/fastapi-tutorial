from uuid import uuid4

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette_context import context


class SQLAlchemyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        context["session_id"] = uuid4().hex

        return await call_next(request)
