from sqlalchemy import insert

from app.core.logger import logger
from app.core.errors import error
from app.core.db.session import AsyncScopedSession
from app.models.db.student import Student
from app.models.db.teacher import Teacher
from app.models.dtos.user import UserDTO
from app.models.constant import UserRole


class UserRepository:

    async def create_student_user(
        self, user_id: str, user_name: str, user_role: UserRole
    ) -> UserDTO:
        async with AsyncScopedSession() as session:
            try:
                stmt = (
                    insert(Student)
                    .values(
                        student_id=user_id,
                        student_name=user_name,
                    )
                    .returning(Student)
                )

                result: Student = (await session.execute(stmt)).scalar()
                await session.commit()
            except Exception as e:
                logger.error(e)
                await session.rollback()
                raise error.UserCreationFailed()

        return UserDTO(
            user_id=result.student_id,
            user_name=result.student_name,
            user_role=user_role.value,
            created_at=result.created_at,
        )

    async def create_teacher_user(
        self, user_id: str, user_name: str, user_role: UserRole
    ) -> UserDTO:
        async with AsyncScopedSession() as session:
            try:
                stmt = (
                    insert(Teacher)
                    .values(
                        teacher_id=user_id,
                        teacher_name=user_name,
                    )
                    .returning(Teacher)
                )

                result: Teacher = (await session.execute(stmt)).scalar()
                await session.commit()
            except Exception as e:
                logger.error(e)
                await session.rollback()
                raise error.UserCreationFailed()

        return UserDTO(
            user_id=result.teacher_id,
            user_name=result.teacher_name_name,
            user_role=user_role.value,
            created_at=result.created_at,
        )
