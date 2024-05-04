from typing import Generic, Optional, TypeVar, Optional

from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass
from fastapi.responses import ORJSONResponse

from app.models.dtos.common import PageDTO


T = TypeVar("T")


class BaseResponse(BaseModel, Generic[T]):
    message: str = "OK"
    statusCode: str = "200"
    data: Optional[T] = None


class ErrorResponse(BaseModel):
    message: str
    statusCode: str


class HttpResponse(ORJSONResponse):
    def __init__(self, content: Optional[T] = None, **kwargs):
        super().__init__(
            content={
                "message": "OK",
                "statusCode": "200",
                "data": content,
            },
            **kwargs
        )


@dataclass
class PageResp:
    total: int = Field(..., description="Total number of items")
    page: int = Field(..., description="Page number")
    limit: int = Field(..., description="Number of items per page")

    @classmethod
    def from_dto(cls, dto: PageDTO) -> "PageResp":
        return cls(
            total=dto.total,
            page=dto.page,
            limit=dto.limit,
        )
