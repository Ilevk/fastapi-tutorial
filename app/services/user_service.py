from app import repositories
from app.models.dtos.user import UserDTO


class UserService:
    def __init__(self, user_repository: repositories.UserRepository):
        self.user_repository = user_repository

    async def create_student_user(self, user_dto: UserDTO) -> UserDTO:
        return await self.user_repository.create_student_user(
            user_id=user_dto.user_id,
            user_name=user_dto.user_name,
            user_role=user_dto.user_role,
        )

    async def create_teacher_user(self, user_dto: UserDTO) -> UserDTO:
        return await self.user_repository.create_teacher_user(
            user_id=user_dto.user_id,
            user_name=user_dto.user_name,
            user_role=user_dto.user_role,
        )
