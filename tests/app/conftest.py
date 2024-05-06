import pytest
from unittest.mock import AsyncMock

from httpx import AsyncClient

from app.main import create_app
from app.core.container import Container
from app.services import UserService, ClassService
from app.repositories import UserRepository, ClassRepository


@pytest.fixture
def container() -> Container:
    return Container()


@pytest.fixture
def async_client(container) -> AsyncClient:
    app = create_app(container)
    return AsyncClient(app=app, base_url="http://test")


@pytest.fixture
def user_repository_mock():
    return AsyncMock(spec=UserRepository)


@pytest.fixture
def class_repository_mock():
    return AsyncMock(spec=ClassRepository)


@pytest.fixture
def user_service_mock(user_repository_mock):
    return UserService(user_repository=user_repository_mock)


@pytest.fixture
def class_service_mock(class_repository_mock):
    return ClassService(class_repository=class_repository_mock)
