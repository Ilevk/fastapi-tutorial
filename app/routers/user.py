from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from app import services
from app.core.container import Container
from app.models.constant import UserRole
from app.models.schemas.common import BaseResponse, HttpResponse, ErrorResponse
from app.models.schemas.user import UserReq, UserResp

router = APIRouter()


@router.post(
    "/teacher",
    response_model=BaseResponse[UserResp],
    responses={400: {"model": ErrorResponse}},
)
@inject
async def create_teacher(
    request_body: UserReq,
    user_service: services.UserService = Depends(Provide[Container.user_service]),
) -> BaseResponse[UserResp]:
    result = await user_service.create_teacher_user(
        request_body.to_dto(user_role=UserRole.TEACHER)
    )

    return HttpResponse(content=UserResp.from_dto(result))


@router.post(
    "/student",
    response_model=BaseResponse[UserResp],
    responses={400: {"model": ErrorResponse}},
)
@inject
async def create_student(
    request_body: UserReq,
    user_service: services.UserService = Depends(Provide[Container.user_service]),
) -> BaseResponse[UserResp]:
    result = await user_service.create_student_user(
        request_body.to_dto(user_role=UserRole.STUDENT)
    )

    return HttpResponse(content=UserResp.from_dto(result))
