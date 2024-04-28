from datetime import datetime

from pydantic import BaseModel, Field


class UserReq(BaseModel):
    userName: str = Field(..., title="Username")


class UserResp(BaseModel):
    userId: str = Field(..., title="User ID")
    userName: str = Field(..., title="Username")
    userRole: str = Field(..., title="User Role")
    createdAt: datetime = Field(..., title="Created At")
