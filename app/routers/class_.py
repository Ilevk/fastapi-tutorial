from typing import List

from fastapi import APIRouter
from app.models.schemas.common import BaseResponse, HttpResponse, ErrorResponse
from app.models.schemas.class_ import (
    ClassReq,
    ClassResp,
    ClassNoticeReq,
    ClassNoticeResp,
)
from app import repositories
from app import services

router = APIRouter()


@router.post(
    "",
    response_model=BaseResponse[ClassResp],
    responses={400: {"model": ErrorResponse}},
)
async def create_class(
    request_body: ClassReq,
) -> BaseResponse[ClassResp]:
    class_service = services.ClassService(repositories.ClassRepository())
    result = await class_service.create_class(request_body.to_dto())

    return HttpResponse(content=ClassResp.from_dto(result))


@router.get(
    "/list",
    response_model=BaseResponse[List[ClassResp]],
    responses={400: {"model": ErrorResponse}},
)
async def read_class_list() -> BaseResponse[List[ClassResp]]:
    class_service = services.ClassService(repositories.ClassRepository())
    result = await class_service.read_class_list()

    return HttpResponse(content=[ClassResp.from_dto(class_) for class_ in result])


@router.get(
    "/{class_id}",
    response_model=BaseResponse[ClassResp],
    responses={400: {"model": ErrorResponse}},
)
async def read_class(
    class_id: str,
) -> BaseResponse[ClassResp]:
    class_service = services.ClassService(repositories.ClassRepository())
    result = await class_service.read_class(class_id)

    return HttpResponse(content=ClassResp.from_dto(result))


@router.post(
    "/notice/{class_id}",
    response_model=BaseResponse[ClassNoticeResp],
    responses={400: {"model": ErrorResponse}},
)
async def create_class_notice(
    class_id: str,
    request_body: ClassNoticeReq,
) -> BaseResponse[ClassNoticeResp]:
    class_service = services.ClassService(repositories.ClassRepository())
    result = await class_service.create_class_notice(request_body.to_dto(class_id))

    return HttpResponse(content=ClassNoticeResp.from_dto(result))


@router.get(
    "/notice/{class_id}/list",
    response_model=BaseResponse[List[ClassNoticeResp]],
    responses={400: {"model": ErrorResponse}},
)
async def read_class_notice_list(
    class_id: str,
) -> BaseResponse[List[ClassNoticeResp]]:
    class_service = services.ClassService(repositories.ClassRepository())
    result = await class_service.read_class_notice_list(class_id)

    return HttpResponse(content=[ClassNoticeResp.from_dto(notice) for notice in result])


@router.put(
    "/notice/{class_id}/{notice_id}",
    response_model=BaseResponse[ClassNoticeResp],
    responses={400: {"model": ErrorResponse}},
)
async def update_class_notice(
    class_id: str,
    notice_id: int,
    request_body: ClassNoticeReq,
) -> BaseResponse[ClassNoticeResp]:
    class_service = services.ClassService(repositories.ClassRepository())
    result = await class_service.update_class_notice(
        request_body.to_dto(class_id, notice_id)
    )

    return HttpResponse(content=ClassNoticeResp.from_dto(result))


@router.delete(
    "/notice/{class_id}/{notice_id}",
    response_model=BaseResponse[ClassNoticeResp],
    responses={400: {"model": ErrorResponse}},
)
async def delete_class_notice(
    class_id: str,
    notice_id: int,
) -> BaseResponse[ClassNoticeResp]:
    class_service = services.ClassService(repositories.ClassRepository())
    result = await class_service.delete_class_notice(class_id, notice_id)

    return HttpResponse(content=ClassNoticeResp.from_dto(result))
