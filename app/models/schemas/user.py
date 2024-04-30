from datetime import datetime

from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass


class UserReq(BaseModel):
    userName: str = Field(..., title="Username")


@dataclass
class UserResp:
    userId: str = Field(..., title="User ID")
    userName: str = Field(..., title="Username")
    userRole: str = Field(..., title="User Role")
    createdAt: datetime = Field(..., title="Created At")
