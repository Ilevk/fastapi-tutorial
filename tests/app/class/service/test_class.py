import pytest
from unittest.mock import AsyncMock


from app.models.dtos.class_ import ClassDTO, ClassNoticeDTO
from app.services.class_service import ClassService
from app.repositories.class_repository import ClassRepository

repository_mock = AsyncMock(spec=ClassRepository)
class_service = ClassService(class_repository=repository_mock)


@pytest.mark.asyncio
async def test_create_class():
    # Setup
    class_dto = ClassDTO(
        class_id="class_id",
        class_name="class_name",
        teacher_id="teacher_id",
    )
    repository_mock.create_class.return_value = class_dto
    class_service.class_repository = repository_mock

    # Run
    result = await class_service.create_class(class_dto=class_dto)

    # Assert
    assert result != None
    assert result.class_id == class_dto.class_id
    assert result.class_name == class_dto.class_name
    assert result.teacher_id == class_dto.teacher_id

    class_service.class_repository.create_class.assert_called_once_with(
        class_id=class_dto.class_id,
        class_name=class_dto.class_name,
        teacher_id=class_dto.teacher_id,
    )


@pytest.mark.asyncio
async def test_read_class_list():
    # Setup
    page = 1
    limit = 10
    class_dto = ClassDTO(
        class_id="class_id",
        class_name="class_name",
        teacher_id="teacher_id",
    )
    repository_mock.read_class_list.return_value = [class_dto]
    class_service.class_repository = repository_mock

    # Run
    results = await class_service.read_class_list(page=page, limit=limit)

    # Assert
    assert results != None
    assert len(results) == 1
    result = results[0]
    assert result.class_id == class_dto.class_id
    assert result.class_name == class_dto.class_name
    assert result.teacher_id == class_dto.teacher_id

    class_service.class_repository.read_class_list.assert_called_once_with(
        page=page, limit=limit
    )


@pytest.mark.asyncio
async def test_read_class():
    # Setup
    class_id = "class_id"
    class_dto = ClassDTO(
        class_id=class_id,
        class_name="class_name",
        teacher_id="teacher_id",
    )
    repository_mock.read_class.return_value = class_dto
    class_service.class_repository = repository_mock

    # Run
    result = await class_service.read_class(class_id=class_id)

    # Assert
    assert result != None
    assert result.class_id == class_dto.class_id
    assert result.class_name == class_dto.class_name
    assert result.teacher_id == class_dto.teacher_id

    class_service.class_repository.read_class.assert_called_once_with(class_id=class_id)


@pytest.mark.asyncio
async def test_create_class_notice():
    # Setup
    class_notice_dto = ClassNoticeDTO(
        class_id="class_id",
        notice_id=1,
        message="message",
    )
    repository_mock.create_class_notice.return_value = class_notice_dto
    class_service.class_repository = repository_mock

    # Run
    result = await class_service.create_class_notice(class_notice_dto=class_notice_dto)

    # Assert
    assert result != None
    assert result.class_id == class_notice_dto.class_id
    assert result.notice_id == class_notice_dto.notice_id
    assert result.message == class_notice_dto.message

    class_service.class_repository.create_class_notice.assert_called_once_with(
        class_id=class_notice_dto.class_id, message=class_notice_dto.message
    )


@pytest.mark.asyncio
async def test_read_class_notice_list():
    # Setup
    class_id = "class_id"
    page = 1
    limit = 10
    class_notice_dto = ClassNoticeDTO(
        class_id=class_id,
        notice_id=1,
        message="message",
    )
    repository_mock.read_class_notice_list.return_value = [class_notice_dto]
    class_service.class_repository = repository_mock

    # Run
    results = await class_service.read_class_notice_list(
        class_id=class_id, page=page, limit=limit
    )

    # Assert
    assert results != None
    assert len(results) == 1
    result = results[0]
    assert result.class_id == class_notice_dto.class_id
    assert result.notice_id == class_notice_dto.notice_id
    assert result.message == class_notice_dto.message

    class_service.class_repository.read_class_notice_list.assert_called_once_with(
        class_id=class_id, page=page, limit=limit
    )


@pytest.mark.asyncio
async def test_update_class_notice():
    # Setup
    class_notice_dto = ClassNoticeDTO(
        class_id="class_id",
        notice_id=1,
        message="message",
    )
    repository_mock.update_class_notice.return_value = class_notice_dto
    class_service.class_repository = repository_mock

    # Run
    result = await class_service.update_class_notice(class_notice_dto=class_notice_dto)

    # Assert
    assert result != None
    assert result.class_id == class_notice_dto.class_id
    assert result.notice_id == class_notice_dto.notice_id
    assert result.message == class_notice_dto.message

    class_service.class_repository.update_class_notice.assert_called_once_with(
        class_id=class_notice_dto.class_id,
        notice_id=class_notice_dto.notice_id,
        message=class_notice_dto.message,
    )


@pytest.mark.asyncio
async def test_delete_class_notice():
    # Setup
    class_id = "class_id"
    notice_id = 1
    class_notice_dto = ClassNoticeDTO(
        class_id=class_id,
        notice_id=notice_id,
        message="message",
    )
    repository_mock.delete_class_notice.return_value = class_notice_dto
    class_service.class_repository = repository_mock

    # Run
    result = await class_service.delete_class_notice(
        class_id=class_id, notice_id=notice_id
    )

    # Assert
    assert result != None
    assert result.class_id == class_id
    assert result.notice_id == notice_id

    class_service.class_repository.delete_class_notice.assert_called_once_with(
        class_id=class_id, notice_id=notice_id
    )
