from fastapi import APIRouter, Query, Path, Body

from app import services
from app import repositories
from app.models.schemas.common import BaseResponse, HttpResponse, ErrorResponse
from app.models.schemas.class_ import (
    ClassReq,
    ClassResp,
    ClassListResp,
    ClassNoticeReq,
    ClassNoticeResp,
    ClassNoticeListResp,
)

router = APIRouter()


@router.post(
    "",
    response_model=BaseResponse[ClassResp],
    responses={400: {"model": ErrorResponse}},
)
async def create_class(
    request_body: ClassReq = Body(..., title="Class creation request body"),
) -> BaseResponse[ClassResp]:
    class_service = services.ClassService(repositories.ClassRepository())
    result = await class_service.create_class(request_body.to_dto())

    return HttpResponse(content=ClassResp.from_dto(result))


@router.get(
    "/list",
    response_model=BaseResponse[ClassListResp],
    responses={400: {"model": ErrorResponse}},
)
async def read_class_list(
    page: int = Query(1, ge=1, title="Page number"),
    limit: int = Query(10, ge=10, le=100, title="Number of items per page"),
) -> BaseResponse[ClassListResp]:
    class_service = services.ClassService(repositories.ClassRepository())
    result = await class_service.read_class_list(page, limit)

    return HttpResponse(content=ClassListResp.from_dto(result))


@router.get(
    "/{class_id}",
    response_model=BaseResponse[ClassResp],
    responses={400: {"model": ErrorResponse}},
)
async def read_class(
    class_id: str = Path(..., title="Class ID")
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
    class_id: str = Path(..., title="Class ID"),
    request_body: ClassNoticeReq = Body(
        ..., title="Class notice creation request body"
    ),
) -> BaseResponse[ClassNoticeResp]:
    class_service = services.ClassService(repositories.ClassRepository())
    result = await class_service.create_class_notice(request_body.to_dto(class_id))

    return HttpResponse(content=ClassNoticeResp.from_dto(result))


@router.get(
    "/notice/{class_id}/list",
    response_model=BaseResponse[ClassNoticeListResp],
    responses={400: {"model": ErrorResponse}},
)
async def read_class_notice_list(
    class_id: str = Path(..., title="Class ID"),
    page: int = Query(1, ge=1, title="Page number"),
    limit: int = Query(10, ge=10, le=100, title="Number of items per page"),
) -> BaseResponse[ClassNoticeListResp]:
    class_service = services.ClassService(repositories.ClassRepository())
    result = await class_service.read_class_notice_list(class_id, page, limit)

    return HttpResponse(content=ClassNoticeListResp.from_dto(result))


@router.put(
    "/notice/{class_id}/{notice_id}",
    response_model=BaseResponse[ClassNoticeResp],
    responses={400: {"model": ErrorResponse}},
)
async def update_class_notice(
    class_id: str = Path(..., title="Class ID"),
    notice_id: int = Path(..., title="Notice ID"),
    request_body: ClassNoticeReq = Body(..., title="Class notice update request body"),
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
    class_id: str = Path(..., title="Class ID"),
    notice_id: int = Path(..., title="Notice ID"),
) -> BaseResponse[ClassNoticeResp]:
    class_service = services.ClassService(repositories.ClassRepository())
    result = await class_service.delete_class_notice(class_id, notice_id)

    return HttpResponse(content=ClassNoticeResp.from_dto(result))
