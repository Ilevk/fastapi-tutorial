from typing import List

from app import repositories
from app.models.dtos.class_ import (
    ClassDTO,
    ClassNoticeDTO,
    ClassListDTO,
    ClassNoticeListDTO,
)
from app.core.errors import error


class ClassService:
    def __init__(self, class_repository: repositories.ClassRepository):
        self.class_repository = class_repository

    async def create_class(self, class_dto: ClassDTO) -> ClassDTO:
        return await self.class_repository.create_class(
            class_id=class_dto.class_id,
            class_name=class_dto.class_name,
            teacher_id=class_dto.teacher_id,
        )

    async def read_class_list(self, page: int, limit: int) -> ClassListDTO:
        return await self.class_repository.read_class_list(page=page, limit=limit)

    async def read_class(self, class_id: str) -> ClassDTO:
        result = await self.class_repository.read_class(class_id=class_id)

        if not result:
            raise error.ClassNotFoundException()

        return result

    async def create_class_notice(
        self, class_notice_dto: ClassNoticeDTO
    ) -> ClassNoticeDTO:
        return await self.class_repository.create_class_notice(
            class_id=class_notice_dto.class_id, message=class_notice_dto.message
        )

    async def read_class_notice_list(
        self, class_id: str, page: int, limit: int
    ) -> ClassNoticeListDTO:
        return await self.class_repository.read_class_notice_list(
            class_id=class_id, page=page, limit=limit
        )

    async def update_class_notice(
        self, class_notice_dto: ClassNoticeDTO
    ) -> ClassNoticeDTO:
        result = await self.class_repository.update_class_notice(
            class_id=class_notice_dto.class_id,
            notice_id=class_notice_dto.notice_id,
            message=class_notice_dto.message,
        )

        if not result:
            raise error.ClassNoticeNotFound()

        return result

    async def delete_class_notice(
        self, class_id: str, notice_id: int
    ) -> ClassNoticeDTO:
        result = await self.class_repository.delete_class_notice(
            class_id=class_id, notice_id=notice_id
        )

        if not result:
            raise error.ClassNoticeNotFound()

        return result
