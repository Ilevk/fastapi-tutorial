from fastapi import APIRouter, Depends
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
    request_body: ClassReq,
    class_service: services.ClassService = Depends(Provide[Container.class_service]),
) -> BaseResponse[ClassResp]:
    result = await class_service.create_class(request_body.to_dto())

    return HttpResponse(content=ClassResp.from_dto(result))


@router.get(
    "/list",
    response_model=BaseResponse[ClassListResp],
    responses={400: {"model": ErrorResponse}},
)
@inject
async def read_class_list(
    page: int = 1,
    limit: int = 10,
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
    class_id: str,
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
    class_id: str,
    request_body: ClassNoticeReq,
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
    class_id: str,
    page: int = 1,
    limit: int = 10,
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
    class_id: str,
    notice_id: int,
    request_body: ClassNoticeReq,
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
    class_id: str,
    notice_id: int,
    class_service: services.ClassService = Depends(Provide[Container.class_service]),
) -> BaseResponse[ClassNoticeResp]:
    result = await class_service.delete_class_notice(class_id, notice_id)

    return HttpResponse(content=ClassNoticeResp.from_dto(result))
