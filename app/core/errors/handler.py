from fastapi import Request
from fastapi.responses import ORJSONResponse
from starlette import status

from app.core.errors.error import BaseAPIException, BaseAuthException


async def api_error_handler(_: Request, exc: BaseAPIException) -> ORJSONResponse:
    return ORJSONResponse(
        content={
            "statusCode": exc.code,
            "message": exc.message,
        },
        status_code=status.HTTP_400_BAD_REQUEST,
    )


async def api_auth_error_handler(_: Request, exc: BaseAuthException) -> ORJSONResponse:
    return ORJSONResponse(
        content={
            "statusCode": exc.code,
            "message": exc.message,
        },
        status_code=status.HTTP_401_UNAUTHORIZED,
    )
