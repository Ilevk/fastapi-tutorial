from uuid import uuid4
from datetime import datetime

from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass

from app.models.dtos.user import UserDTO
from app.models.constant import UserRole


class UserReq(BaseModel):
    userName: str = Field(..., title="Username")

    def to_dto(self, user_role: UserRole) -> UserDTO:
        return UserDTO(
            user_id=uuid4().hex,
            user_name=self.userName,
            user_role=user_role,
        )


@dataclass
class UserResp:
    userId: str = Field(..., title="User ID")
    userName: str = Field(..., title="Username")
    userRole: UserRole = Field(..., title="User Role")
    createdAt: datetime = Field(..., title="Created At")

    def from_dto(dto: UserDTO) -> "UserResp":
        return UserResp(
            userId=dto.user_id,
            userName=dto.user_name,
            userRole=dto.user_role.value,
            createdAt=dto.created_at,
        )
