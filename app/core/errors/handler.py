from fastapi import Request
from fastapi.responses import ORJSONResponse
from starlette import status

from app.core.errors.error import BaseAPIException


async def api_error_handler(_: Request, exc: BaseAPIException) -> ORJSONResponse:
    return ORJSONResponse(
        content={"statusCode": exc.code, "message": exc.message},
        status_code=status.HTTP_400_BAD_REQUEST,
    )
