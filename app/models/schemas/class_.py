from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass


class ClassReq(BaseModel):
    className: str = Field(..., title="Class Name")
    teacherId: str = Field(..., title="Teacher ID")


@dataclass
class ClassResp:
    classId: str = Field(..., title="Class ID")
    className: str = Field(..., title="Class Name")
    teacherId: str = Field(..., title="Teacher ID")
    createdAt: datetime = Field(..., title="Created At")


class ClassNoticeReq(BaseModel):
    message: str = Field(..., title="Message")


@dataclass
class ClassNoticeResp:
    id: int = Field(..., title="ID")
    classId: str = Field(..., title="Class ID")
    message: str = Field(..., title="Message")
    createdAt: datetime = Field(..., title="Created At")
    updatedAt: Optional[datetime] = Field(None, title="Updated At")
