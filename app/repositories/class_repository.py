from typing import List, Optional

from sqlalchemy import select, insert, update, delete

from app.core.logger import logger
from app.core.redis import RedisCacheDecorator
from app.core.errors import error
from app.core.db.session import AsyncScopedSession
from app.models.db.class_ import Class, ClassNotice
from app.models.dtos.class_ import ClassDTO, ClassNoticeDTO


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
    async def read_class_list(self) -> List[ClassDTO]:
        async with AsyncScopedSession() as session:
            stmt = select(Class)

            results = (await session.execute(stmt)).scalars().all()

        return [
            ClassDTO(
                class_id=result.class_id,
                class_name=result.class_name,
                teacher_id=result.teacher_id,
                created_at=result.created_at,
            )
            for result in results
        ]

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
    async def read_class_notice_list(self, class_id) -> List[ClassNoticeDTO]:
        async with AsyncScopedSession() as session:
            stmt = select(ClassNotice).where(ClassNotice.class_id == class_id)

            result = (await session.execute(stmt)).scalars().all()

        return [
            ClassNoticeDTO(
                notice_id=result.id,
                class_id=result.class_id,
                message=result.message,
                created_at=result.created_at,
                updated_at=result.updated_at,
            )
            for result in result
        ]

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
