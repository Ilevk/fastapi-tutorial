import pytest
from unittest.mock import AsyncMock


from app.models.dtos.user import UserDTO
from app.models.constant import UserRole
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository

repository_mock = AsyncMock(spec=UserRepository)
user_service = UserService(user_repository=repository_mock)


@pytest.mark.asyncio
async def test_create_teacher():
    # Setup
    user_dto = UserDTO(
        user_id="user_id",
        user_name="user_name",
        user_role=UserRole.TEACHER,
    )
    repository_mock.create_teacher_user.return_value = user_dto
    user_service.user_repository = repository_mock

    # Run
    result = await user_service.create_teacher_user(user_dto=user_dto)

    # Assert
    assert result != None
    assert result.user_id == user_dto.user_id
    assert result.user_name == user_dto.user_name
    assert result.user_role == user_dto.user_role

    user_service.user_repository.create_teacher_user.assert_called_once_with(
        user_id=user_dto.user_id,
        user_name=user_dto.user_name,
        user_role=user_dto.user_role,
    )


@pytest.mark.asyncio
async def test_create_student():
    # Setup
    user_dto = UserDTO(
        user_id="user_id",
        user_name="user_name",
        user_role=UserRole.STUDENT,
    )
    repository_mock.create_student_user.return_value = user_dto
    user_service.user_repository = repository_mock

    # Run
    result = await user_service.create_student_user(user_dto=user_dto)

    # Assert
    assert result != None
    assert result.user_id == user_dto.user_id
    assert result.user_name == user_dto.user_name
    assert result.user_role == user_dto.user_role

    user_service.user_repository.create_student_user.assert_called_once_with(
        user_id=user_dto.user_id,
        user_name=user_dto.user_name,
        user_role=user_dto.user_role,
    )
