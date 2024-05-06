import pytest
from datetime import datetime

from httpx import AsyncClient

from app.core.container import Container
from app.core.errors import error
from app.models.dtos.user import UserDTO
from app.models.constant import UserRole
from app.models.schemas.user import UserReq
from app.services import UserService


@pytest.mark.parametrize(
    "user_name,user_role",
    [
        ("test_username", UserRole.TEACHER),
    ],
)
async def test_create_user_teacher_200(
    container: Container,
    async_client: AsyncClient,
    user_service_mock: UserService,
    user_name: str,
    user_role: UserRole,
):
    # Setup
    # Request
    data = UserReq(
        userName=user_name,
    )
    # Repository
    user_dto = UserDTO(
        user_id="-",
        user_name=user_name,
        user_role=user_role,
        created_at=datetime.now(),
    )
    user_service_mock.user_repository.create_teacher_user.return_value = user_dto
    container.user_service.override(user_service_mock)

    # Run
    headers = {"x-api-key": "test-api-key"}
    url = "/v1/user/teacher"
    response = await async_client.post(
        url, headers=headers, data=data.model_dump_json()
    )
    json_response = response.json()

    # Assert
    assert response.status_code == 200
    assert json_response["data"]["userName"] == user_dto.user_name
    assert json_response["data"]["userRole"] == user_dto.user_role.value


@pytest.mark.parametrize(
    "user_name,user_role",
    [
        ("test_username", UserRole.STUDENT),
    ],
)
async def test_create_user_student_200(
    container: Container,
    async_client: AsyncClient,
    user_service_mock: UserService,
    user_name: str,
    user_role: UserRole,
):
    # Setup
    # Request
    data = UserReq(
        userName=user_name,
    )
    # Repository
    user_dto = UserDTO(
        user_id="-",
        user_name=user_name,
        user_role=user_role,
        created_at=datetime.now(),
    )
    user_service_mock.user_repository.create_student_user.return_value = user_dto
    container.user_service.override(user_service_mock)

    # Run
    headers = {"x-api-key": "test-api-key"}
    url = "/v1/user/student"
    response = await async_client.post(
        url, headers=headers, data=data.model_dump_json()
    )
    json_response = response.json()

    # Assert
    assert response.status_code == 200
    assert json_response["data"]["userName"] == user_dto.user_name
    assert json_response["data"]["userRole"] == user_dto.user_role.value


@pytest.mark.parametrize(
    "user_name,expected_error",
    [
        ("test_username", error.ERROR_400_USER_CREATION_FAILED),
    ],
)
async def test_create_user_teacher_400(
    async_client: AsyncClient,
    user_name: str,
    expected_error: Exception,
):
    # Setup
    data = UserReq(
        userName=user_name,
    )

    # Run
    headers = {"x-api-key": "test-api-key"}
    url = "/v1/user/teacher"
    response = await async_client.post(
        url, headers=headers, data=data.model_dump_json()
    )
    json_response = response.json()

    # Assert
    assert response.status_code == 400
    assert json_response["statusCode"] == expected_error


@pytest.mark.parametrize(
    "user_name,expected_error",
    [
        ("test_username", error.ERROR_400_USER_CREATION_FAILED),
    ],
)
async def test_create_user_student_400(
    async_client: AsyncClient,
    user_name: str,
    expected_error: Exception,
):
    # Setup
    data = UserReq(
        userName=user_name,
    )

    # Run
    headers = {"x-api-key": "test-api-key"}
    url = "/v1/user/student"
    response = await async_client.post(
        url, headers=headers, data=data.model_dump_json()
    )
    json_response = response.json()

    # Assert
    assert response.status_code == 400
    assert json_response["statusCode"] == expected_error
