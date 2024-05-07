import pytest
from unittest.mock import AsyncMock


from app.models.dtos.common import PageDTO
from app.models.dtos.class_ import ClassNoticeDTO, ClassListDTO
from app.services.class_service import ClassService


@pytest.mark.asyncio
async def test_create_class_notice(
    class_repository_mock: AsyncMock,
    class_service_mock: ClassService,
):
    # Setup
    class_notice_dto = ClassNoticeDTO(
        class_id="class_id",
        notice_id=1,
        message="message",
    )
    class_repository_mock.create_class_notice.return_value = class_notice_dto

    # Run
    result = await class_service_mock.create_class_notice(
        class_notice_dto=class_notice_dto
    )

    # Assert
    assert result != None
    assert result.class_id == class_notice_dto.class_id
    assert result.notice_id == class_notice_dto.notice_id
    assert result.message == class_notice_dto.message

    class_service_mock.class_repository.create_class_notice.assert_called_once_with(
        class_id=class_notice_dto.class_id, message=class_notice_dto.message
    )


@pytest.mark.asyncio
async def test_read_class_notice_list(
    class_repository_mock: AsyncMock,
    class_service_mock: ClassService,
):
    # Setup
    class_id = "class_id"
    page = 1
    limit = 10
    total = 1
    class_notice_dto = ClassNoticeDTO(
        class_id=class_id,
        notice_id=1,
        message="message",
    )
    page_dto = PageDTO(page=page, limit=limit, total=total)
    class_notice_list_dto = ClassListDTO(
        data=[class_notice_dto],
        page=page_dto,
    )
    class_repository_mock.read_class_notice_list.return_value = class_notice_list_dto

    # Run
    results = await class_service_mock.read_class_notice_list(
        class_id=class_id, page=page, limit=limit
    )

    # Assert
    assert results != None

    result_page = results.page
    assert result_page.page == page_dto.page
    assert result_page.limit == page_dto.limit
    assert result_page.total == page_dto.total

    result_data = results.data
    assert len(result_data) == 1
    result = result_data[0]
    assert result.class_id == class_notice_dto.class_id
    assert result.notice_id == class_notice_dto.notice_id
    assert result.message == class_notice_dto.message

    class_service_mock.class_repository.read_class_notice_list.assert_called_once_with(
        class_id=class_id, page=page, limit=limit
    )


@pytest.mark.asyncio
async def test_update_class_notice(
    class_repository_mock: AsyncMock,
    class_service_mock: ClassService,
):
    # Setup
    class_notice_dto = ClassNoticeDTO(
        class_id="class_id",
        notice_id=1,
        message="message",
    )
    class_repository_mock.update_class_notice.return_value = class_notice_dto

    # Run
    result = await class_service_mock.update_class_notice(
        class_notice_dto=class_notice_dto
    )

    # Assert
    assert result != None
    assert result.class_id == class_notice_dto.class_id
    assert result.notice_id == class_notice_dto.notice_id
    assert result.message == class_notice_dto.message

    class_service_mock.class_repository.update_class_notice.assert_called_once_with(
        class_id=class_notice_dto.class_id,
        notice_id=class_notice_dto.notice_id,
        message=class_notice_dto.message,
    )


@pytest.mark.asyncio
async def test_delete_class_notice(
    class_repository_mock: AsyncMock,
    class_service_mock: ClassService,
):
    # Setup
    class_id = "class_id"
    notice_id = 1
    class_notice_dto = ClassNoticeDTO(
        class_id=class_id,
        notice_id=notice_id,
        message="message",
    )
    class_repository_mock.delete_class_notice.return_value = class_notice_dto

    # Run
    result = await class_service_mock.delete_class_notice(
        class_id=class_id, notice_id=notice_id
    )

    # Assert
    assert result != None
    assert result.class_id == class_id
    assert result.notice_id == notice_id

    class_service_mock.class_repository.delete_class_notice.assert_called_once_with(
        class_id=class_id, notice_id=notice_id
    )
