import pytest
from unittest.mock import AsyncMock


from app.models.dtos.common import PageDTO
from app.models.dtos.class_ import ClassDTO, ClassListDTO
from app.services.class_service import ClassService


@pytest.mark.asyncio
async def test_create_class(
    class_repository_mock: AsyncMock,
    class_service_mock: ClassService,
):
    # Setup
    class_dto = ClassDTO(
        class_id="class_id",
        class_name="class_name",
        teacher_id="teacher_id",
    )
    class_repository_mock.create_class.return_value = class_dto

    # Run
    result = await class_service_mock.create_class(class_dto=class_dto)

    # Assert
    assert result != None
    assert result.class_id == class_dto.class_id
    assert result.class_name == class_dto.class_name
    assert result.teacher_id == class_dto.teacher_id

    class_service_mock.class_repository.create_class.assert_called_once_with(
        class_id=class_dto.class_id,
        class_name=class_dto.class_name,
        teacher_id=class_dto.teacher_id,
    )


@pytest.mark.asyncio
async def test_read_class_list(
    class_repository_mock: AsyncMock,
    class_service_mock: ClassService,
):
    # Setup
    page = 1
    limit = 10
    total = 1
    class_dto = ClassDTO(
        class_id="class_id",
        class_name="class_name",
        teacher_id="teacher_id",
    )
    page_dto = PageDTO(page=page, limit=limit, total=total)
    class_list_dto = ClassListDTO(
        data=[class_dto],
        page=page_dto,
    )

    class_repository_mock.read_class_list.return_value = class_list_dto

    # Run
    results = await class_service_mock.read_class_list(page=page, limit=limit)

    # Assert
    assert results != None

    result_page = results.page
    assert result_page.page == page_dto.page
    assert result_page.limit == page_dto.limit
    assert result_page.total == page_dto.total

    result_data = results.data
    assert len(result_data) == 1
    result = result_data[0]
    assert result.class_id == class_dto.class_id
    assert result.class_name == class_dto.class_name
    assert result.teacher_id == class_dto.teacher_id

    class_service_mock.class_repository.read_class_list.assert_called_once_with(
        page=page, limit=limit
    )


@pytest.mark.asyncio
async def test_read_class(
    class_repository_mock: AsyncMock,
    class_service_mock: ClassService,
):
    # Setup
    class_id = "class_id"
    class_dto = ClassDTO(
        class_id=class_id,
        class_name="class_name",
        teacher_id="teacher_id",
    )
    class_repository_mock.read_class.return_value = class_dto

    # Run
    result = await class_service_mock.read_class(class_id=class_id)

    # Assert
    assert result != None
    assert result.class_id == class_dto.class_id
    assert result.class_name == class_dto.class_name
    assert result.teacher_id == class_dto.teacher_id

    class_service_mock.class_repository.read_class.assert_called_once_with(
        class_id=class_id
    )
