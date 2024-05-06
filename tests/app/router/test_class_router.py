import pytest
from asyncio import BaseEventLoop
from datetime import datetime

from httpx import AsyncClient

from app.core.container import Container
from app.core.errors import error
from app.models.dtos.common import PageDTO
from app.models.dtos.class_ import (
    ClassDTO,
    ClassListDTO,
    ClassNoticeDTO,
    ClassNoticeListDTO,
)
from app.models.schemas.class_ import ClassReq, ClassNoticeReq
from app.services import ClassService


@pytest.mark.parametrize(
    "class_name,teacher_id",
    [
        ("class_name", "teacher_id"),
    ],
)
async def test_create_class_200(
    container: Container,
    async_client: AsyncClient,
    class_service_mock: ClassService,
    class_name: str,
    teacher_id: str,
):
    # Setup
    # Request
    data = ClassReq(
        className=class_name,
        teacherId=teacher_id,
    )
    # Respository
    class_dto = ClassDTO(
        class_id="-",
        class_name=class_name,
        teacher_id=teacher_id,
        created_at=datetime.now(),
    )
    class_service_mock.class_repository.create_class.return_value = class_dto
    container.class_service.override(class_service_mock)

    # Run
    headers = {"x-api-key": "test-api-key"}
    url = "/v1/class"
    response = await async_client.post(
        url, headers=headers, data=data.model_dump_json()
    )
    json_response = response.json()

    # Assert
    assert response.status_code == 200
    assert json_response["data"]["className"] == class_dto.class_name
    assert json_response["data"]["teacherId"] == class_dto.teacher_id


@pytest.mark.parametrize(
    "page,limit",
    [
        (1, 10),
    ],
)
async def test_read_class_list_200(
    container: Container,
    async_client: AsyncClient,
    class_service_mock: ClassService,
    page: int,
    limit: int,
):
    # Setup
    # Request
    params = {
        "page": page,
        "limit": limit,
    }
    # Respository
    class_dto = ClassDTO(
        class_id="class_id",
        class_name="class_name",
        teacher_id="teacher_id",
        created_at=datetime.now(),
    )
    page_dto = PageDTO(
        page=page,
        limit=limit,
        total=1,
    )
    class_list_dto = ClassListDTO(
        page=page_dto,
        data=[class_dto],
    )
    class_service_mock.class_repository.read_class_list.return_value = class_list_dto
    container.class_service.override(class_service_mock)

    # Run
    headers = {"x-api-key": "test-api-key"}
    url = "/v1/class/list"
    response = await async_client.get(url, headers=headers, params=params)
    json_response = response.json()

    # Assert
    assert response.status_code == 200

    page = json_response["data"]["page"]
    assert page["page"] == page_dto.page
    assert page["limit"] == page_dto.limit
    assert page["total"] == page_dto.total

    results = json_response["data"]["data"]
    assert len(results) == 1
    result = results[0]
    assert result["classId"] == class_dto.class_id
    assert result["className"] == class_dto.class_name
    assert result["teacherId"] == class_dto.teacher_id


@pytest.mark.parametrize(
    "class_id,class_name,teacher_id",
    [
        ("class_id", "class_name", "teacher_id"),
    ],
)
async def test_read_class_200(
    container: Container,
    async_client: AsyncClient,
    class_service_mock: ClassService,
    class_id: str,
    class_name: str,
    teacher_id: str,
):
    # Setup
    # Respository
    class_dto = ClassDTO(
        class_id=class_id,
        class_name=class_name,
        teacher_id=teacher_id,
        created_at=datetime.now(),
    )
    class_service_mock.class_repository.read_class.return_value = class_dto
    container.class_service.override(class_service_mock)

    # Run
    headers = {"x-api-key": "test-api-key"}
    url = f"/v1/class/{class_id}"
    response = await async_client.get(url, headers=headers)
    json_response = response.json()

    # Assert
    assert response.status_code == 200
    assert json_response["data"]["classId"] == class_dto.class_id
    assert json_response["data"]["className"] == class_dto.class_name
    assert json_response["data"]["teacherId"] == class_dto.teacher_id


@pytest.mark.parametrize(
    "class_id,message",
    [
        ("class_id", "message"),
    ],
)
async def test_create_class_notice_200(
    container: Container,
    async_client: AsyncClient,
    class_service_mock: ClassService,
    class_id: str,
    message: str,
):
    # Setup
    # Request
    data = ClassNoticeReq(
        message=message,
    )
    # Respository
    class_notice_dto = ClassNoticeDTO(
        class_id=class_id,
        notice_id=1,
        message=message,
        created_at=datetime.now(),
    )
    class_service_mock.class_repository.create_class_notice.return_value = (
        class_notice_dto
    )
    container.class_service.override(class_service_mock)

    # Run
    headers = {"x-api-key": "test-api-key"}
    url = f"/v1/class/notice/{class_id}"
    response = await async_client.post(
        url, headers=headers, data=data.model_dump_json()
    )
    json_response = response.json()

    # Assert
    assert response.status_code == 200
    assert json_response["data"]["id"] == class_notice_dto.notice_id
    assert json_response["data"]["classId"] == class_notice_dto.class_id
    assert json_response["data"]["message"] == class_notice_dto.message


@pytest.mark.parametrize(
    "class_id,page,limit",
    [
        ("class_id", 1, 10),
    ],
)
async def test_read_class_notice_list_200(
    container: Container,
    async_client: AsyncClient,
    class_service_mock: ClassService,
    class_id: str,
    page: int,
    limit: int,
):
    # Setup
    # Request
    params = {
        "page": page,
        "limit": limit,
    }
    # Respository
    class_notice_dto = ClassNoticeDTO(
        class_id=class_id,
        notice_id=1,
        message="message",
        created_at=datetime.now(),
    )
    page_dto = PageDTO(
        page=page,
        limit=limit,
        total=1,
    )
    class_notice_list_dto = ClassNoticeListDTO(
        page=page_dto,
        data=[class_notice_dto],
    )
    class_service_mock.class_repository.read_class_notice_list.return_value = (
        class_notice_list_dto
    )
    container.class_service.override(class_service_mock)

    # Run
    headers = {"x-api-key": "test-api-key"}
    url = f"/v1/class/notice/{class_id}/list"
    response = await async_client.get(url, headers=headers, params=params)
    json_response = response.json()

    # Assert
    assert response.status_code == 200

    page = json_response["data"]["page"]
    assert page["page"] == page_dto.page
    assert page["limit"] == page_dto.limit
    assert page["total"] == page_dto.total

    results = json_response["data"]["data"]
    assert len(results) == 1
    result = results[0]
    assert result["id"] == class_notice_dto.notice_id
    assert result["classId"] == class_notice_dto.class_id
    assert result["message"] == class_notice_dto.message


@pytest.mark.parametrize(
    "class_id,notice_id",
    [
        ("class_id", 1),
    ],
)
async def test_update_class_notice_200(
    container: Container,
    async_client: AsyncClient,
    class_service_mock: ClassService,
    class_id: str,
    notice_id: int,
):
    # Setup
    # Request
    data = ClassNoticeReq(
        message="message",
    )
    # Respository
    class_notice_dto = ClassNoticeDTO(
        class_id=class_id,
        notice_id=notice_id,
        message="message",
        created_at=datetime.now(),
    )
    class_service_mock.class_repository.update_class_notice.return_value = (
        class_notice_dto
    )
    container.class_service.override(class_service_mock)

    # Run
    headers = {"x-api-key": "test-api-key"}
    url = f"/v1/class/notice/{class_id}/{notice_id}"
    response = await async_client.put(url, headers=headers, data=data.model_dump_json())
    json_response = response.json()

    # Assert
    assert response.status_code == 200
    assert json_response["data"]["id"] == class_notice_dto.notice_id
    assert json_response["data"]["classId"] == class_notice_dto.class_id
    assert json_response["data"]["message"] == class_notice_dto.message


@pytest.mark.parametrize(
    "class_id,notice_id",
    [
        ("class_id", 1),
    ],
)
async def test_delete_class_notice_200(
    container: Container,
    async_client: AsyncClient,
    class_service_mock: ClassService,
    class_id: str,
    notice_id: int,
):
    # Setup
    # Respository
    class_notice_dto = ClassNoticeDTO(
        class_id=class_id,
        notice_id=notice_id,
        message="message",
        created_at=datetime.now(),
    )
    class_service_mock.class_repository.delete_class_notice.return_value = (
        class_notice_dto
    )
    container.class_service.override(class_service_mock)

    # Run
    headers = {"x-api-key": "test-api-key"}
    url = f"/v1/class/notice/{class_id}/{notice_id}"
    response = await async_client.delete(url, headers=headers)
    json_response = response.json()

    # Assert
    assert response.status_code == 200
    assert json_response["data"]["id"] == class_notice_dto.notice_id
    assert json_response["data"]["classId"] == class_notice_dto.class_id
    assert json_response["data"]["message"] == class_notice_dto.message
