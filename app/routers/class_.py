from fastapi import APIRouter, Query, Path, Body, Depends
from dependency_injector.wiring import Provide, inject

from app import services
from app.core.container import Container
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
@inject
async def create_class(
    request_body: ClassReq = Body(..., description="Class creation request body"),
    class_service: services.ClassService = Depends(Provide[Container.class_service]),
) -> BaseResponse[ClassResp]:
    """
    POST
    클래스를 생성하는 API 입니다.

    Args:
        request_body (ClassReq, optional): 클래스 생성 요청 바디

    Returns:
        BaseResponse[ClassResp]: 클래스 생성 결과
    """
    result = await class_service.create_class(request_body.to_dto())

    return HttpResponse(content=ClassResp.from_dto(result))


@router.get(
    "/list",
    response_model=BaseResponse[ClassListResp],
    responses={400: {"model": ErrorResponse}},
)
@inject
async def read_class_list(
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=10, le=100, description="Number of items per page"),
    class_service: services.ClassService = Depends(Provide[Container.class_service]),
) -> BaseResponse[ClassListResp]:
    result = await class_service.read_class_list(page, limit)

    return HttpResponse(content=ClassListResp.from_dto(result))


@router.get(
    "/{class_id}",
    response_model=BaseResponse[ClassResp],
    responses={400: {"model": ErrorResponse}},
)
@inject
async def read_class(
    class_id: str = Path(..., description="Class ID"),
    class_service: services.ClassService = Depends(Provide[Container.class_service]),
) -> BaseResponse[ClassResp]:
    result = await class_service.read_class(class_id)

    return HttpResponse(content=ClassResp.from_dto(result))


@router.post(
    "/notice/{class_id}",
    response_model=BaseResponse[ClassNoticeResp],
    responses={400: {"model": ErrorResponse}},
)
@inject
async def create_class_notice(
    class_id: str = Path(..., description="Class ID"),
    request_body: ClassNoticeReq = Body(
        ..., description="Class notice creation request body"
    ),
    class_service: services.ClassService = Depends(Provide[Container.class_service]),
) -> BaseResponse[ClassNoticeResp]:
    result = await class_service.create_class_notice(request_body.to_dto(class_id))

    return HttpResponse(content=ClassNoticeResp.from_dto(result))


@router.get(
    "/notice/{class_id}/list",
    response_model=BaseResponse[ClassNoticeListResp],
    responses={400: {"model": ErrorResponse}},
)
@inject
async def read_class_notice_list(
    class_id: str = Path(..., description="Class ID"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=10, le=100, description="Number of items per page"),
    class_service: services.ClassService = Depends(Provide[Container.class_service]),
) -> BaseResponse[ClassNoticeListResp]:
    result = await class_service.read_class_notice_list(class_id, page, limit)

    return HttpResponse(content=ClassNoticeListResp.from_dto(result))


@router.put(
    "/notice/{class_id}/{notice_id}",
    response_model=BaseResponse[ClassNoticeResp],
    responses={400: {"model": ErrorResponse}},
)
@inject
async def update_class_notice(
    class_id: str = Path(..., description="Class ID"),
    notice_id: int = Path(..., description="Notice ID"),
    request_body: ClassNoticeReq = Body(
        ..., description="Class notice update request body"
    ),
    class_service: services.ClassService = Depends(Provide[Container.class_service]),
) -> BaseResponse[ClassNoticeResp]:
    result = await class_service.update_class_notice(
        request_body.to_dto(class_id, notice_id)
    )

    return HttpResponse(content=ClassNoticeResp.from_dto(result))


@router.delete(
    "/notice/{class_id}/{notice_id}",
    response_model=BaseResponse[ClassNoticeResp],
    responses={400: {"model": ErrorResponse}},
)
@inject
async def delete_class_notice(
    class_id: str = Path(..., description="Class ID"),
    notice_id: int = Path(..., description="Notice ID"),
    class_service: services.ClassService = Depends(Provide[Container.class_service]),
) -> BaseResponse[ClassNoticeResp]:
    result = await class_service.delete_class_notice(class_id, notice_id)

    return HttpResponse(content=ClassNoticeResp.from_dto(result))
