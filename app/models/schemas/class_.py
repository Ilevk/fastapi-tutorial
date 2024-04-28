from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ClassReq(BaseModel):
    className: str = Field(..., title="Class Name")
    teacherId: str = Field(..., title="Teacher ID")


class ClassResp(BaseModel):
    classId: str = Field(..., title="Class ID")
    className: str = Field(..., title="Class Name")
    teacherId: str = Field(..., title="Teacher ID")
    createdAt: datetime = Field(..., title="Created At")


class ClassNoticeReq(BaseModel):
    message: str = Field(..., title="Message")


class ClassNoticeResp(BaseModel):
    id: int = Field(..., title="ID")
    classId: str = Field(..., title="Class ID")
    message: str = Field(..., title="Message")
    createdAt: datetime = Field(..., title="Created At")
    updatedAt: Optional[datetime] = Field(None, title="Updated At")
