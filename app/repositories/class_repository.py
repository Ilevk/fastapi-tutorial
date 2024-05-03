from typing import List, Optional

from sqlalchemy import select, insert, update, delete, func

from app.core.logger import logger
from app.core.redis import RedisCacheDecorator
from app.core.errors import error
from app.core.db.session import AsyncScopedSession
from app.models.db.class_ import Class, ClassNotice
from app.models.dtos.common import PageDTO
from app.models.dtos.class_ import (
    ClassDTO,
    ClassNoticeDTO,
    ClassListDTO,
    ClassNoticeListDTO,
)


class ClassRepository:

    async def create_class(
        self, class_id: str, class_name: str, teacher_id: str
    ) -> ClassDTO:
        async with AsyncScopedSession() as session:
            try:
                stmt = (
                    insert(Class)
                    .values(
                        class_id=class_id,
                        class_name=class_name,
                        teacher_id=teacher_id,
                    )
                    .returning(Class)
                )

                result: Class = (await session.execute(stmt)).scalar()
                await session.commit()
            except Exception as e:
                logger.error(e)
                await session.rollback()
                raise error.ClassCreationFailed()

        return ClassDTO(
            class_id=result.class_id,
            class_name=result.class_name,
            teacher_id=result.teacher_id,
            created_at=result.created_at,
        )

    @RedisCacheDecorator()
    async def read_class_list(self, page: int, limit: int) -> ClassListDTO:
        async with AsyncScopedSession() as session:
            stmt = (
                select(Class, func.count().over().label("total"))
                .limit(limit)
                .offset((page - 1) * limit if page > 1 else 0)
                .order_by(Class.created_at.desc())
            )

            results: List[List[Class, int]] = (await session.execute(stmt)).all()

        data = []
        page = PageDTO(page=page, limit=limit, total=0)

        if results:
            for row, total in results:
                data.append(
                    ClassDTO(
                        class_id=row.class_id,
                        class_name=row.class_name,
                        teacher_id=row.teacher_id,
                        created_at=row.created_at,
                    )
                )
            page.total = total

        return ClassListDTO(data=data, page=page)

    @RedisCacheDecorator()
    async def read_class(self, class_id: str) -> Optional[ClassDTO]:
        async with AsyncScopedSession() as session:
            stmt = select(Class).where(Class.class_id == class_id)

            result = (await session.execute(stmt)).scalar()

        if result:
            return ClassDTO(
                class_id=result.class_id,
                class_name=result.class_name,
                teacher_id=result.teacher_id,
                created_at=result.created_at,
            )
        else:
            return None

    async def create_class_notice(self, class_id: str, message: str) -> ClassNoticeDTO:
        async with AsyncScopedSession() as session:
            try:
                stmt = (
                    insert(ClassNotice)
                    .values(
                        class_id=class_id,
                        message=message,
                    )
                    .returning(ClassNotice)
                )

                result: ClassNotice = (await session.execute(stmt)).scalar()
                await session.commit()
            except Exception as e:
                logger.error(e)
                await session.rollback()
                raise error.ClassNoticeCreationFailed()

        return ClassNoticeDTO(
            notice_id=result.id,
            class_id=result.class_id,
            message=result.message,
            created_at=result.created_at,
            updated_at=result.updated_at,
        )

    @RedisCacheDecorator()
    async def read_class_notice_list(
        self, class_id: str, page: int, limit: int
    ) -> ClassNoticeListDTO:
        async with AsyncScopedSession() as session:
            stmt = (
                select(ClassNotice, func.count().over().label("total"))
                .where(ClassNotice.class_id == class_id)
                .limit(limit)
                .offset((page - 1) * limit if page > 1 else 0)
                .order_by(ClassNotice.created_at.desc())
            )

            results: List[List[ClassNotice, int]] = (await session.execute(stmt)).all()

        data = []
        page = PageDTO(page=page, limit=limit, total=0)

        if results:
            for row, total in results:
                data.append(
                    ClassNoticeDTO(
                        notice_id=row.id,
                        class_id=row.class_id,
                        message=row.message,
                        created_at=row.created_at,
                        updated_at=row.updated_at,
                    )
                )
            page.total = total

        return ClassNoticeListDTO(data=data, page=page)

    async def update_class_notice(
        self, class_id: str, notice_id: int, message: str
    ) -> Optional[ClassNoticeDTO]:
        async with AsyncScopedSession() as session:
            try:
                stmt = (
                    update(ClassNotice)
                    .where(
                        ClassNotice.id == notice_id, ClassNotice.class_id == class_id
                    )
                    .values(message=message)
                    .returning(ClassNotice)
                )

                result: ClassNotice = (await session.execute(stmt)).scalar()
                await session.commit()
            except Exception as e:
                logger.error(e)
                await session.rollback()
                raise error.ClassNoticeUpdateFailed()

        if result:
            return ClassNoticeDTO(
                notice_id=result.id,
                class_id=result.class_id,
                message=result.message,
                created_at=result.created_at,
                updated_at=result.updated_at,
            )
        else:
            return None

    async def delete_class_notice(
        self, class_id: str, notice_id: int
    ) -> Optional[ClassNoticeDTO]:
        async with AsyncScopedSession() as session:
            try:
                stmt = (
                    delete(ClassNotice)
                    .where(
                        ClassNotice.id == notice_id, ClassNotice.class_id == class_id
                    )
                    .returning(ClassNotice)
                )
                result: ClassNotice = (await session.execute(stmt)).scalar()
                await session.commit()
            except Exception as e:
                logger.error(e)
                await session.rollback()
                raise error.ClassNoticeDeleteFailed()

        if result:

            return ClassNoticeDTO(
                notice_id=result.id,
                class_id=result.class_id,
                message=result.message,
                created_at=result.created_at,
                updated_at=result.updated_at,
            )
        else:
            return None
