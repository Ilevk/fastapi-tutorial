from uuid import uuid4
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass

from app.models.dtos.class_ import ClassDTO, ClassNoticeDTO


class ClassReq(BaseModel):
    className: str = Field(..., title="Class Name")
    teacherId: str = Field(..., title="Teacher ID")

    def to_dto(self) -> ClassDTO:
        return ClassDTO(
            class_id=uuid4().hex,
            class_name=self.className,
            teacher_id=self.teacherId,
        )


@dataclass
class ClassResp:
    classId: str = Field(..., title="Class ID")
    className: str = Field(..., title="Class Name")
    teacherId: str = Field(..., title="Teacher ID")
    createdAt: datetime = Field(..., title="Created At")

    @classmethod
    def from_dto(cls, dto: ClassDTO) -> "ClassResp":
        return cls(
            classId=dto.class_id,
            className=dto.class_name,
            teacherId=dto.teacher_id,
            createdAt=dto.created_at,
        )


class ClassNoticeReq(BaseModel):
    message: str = Field(..., title="Message")

    def to_dto(self, class_id: str = None, notice_id: int = None) -> ClassNoticeDTO:
        return ClassNoticeDTO(
            notice_id=notice_id,
            class_id=class_id,
            message=self.message,
        )


@dataclass
class ClassNoticeResp:
    id: int = Field(..., title="ID")
    classId: str = Field(..., title="Class ID")
    message: str = Field(..., title="Message")
    createdAt: datetime = Field(..., title="Created At")
    updatedAt: Optional[datetime] = Field(None, title="Updated At")

    @classmethod
    def from_dto(cls, dto: ClassNoticeDTO) -> "ClassNoticeResp":
        return cls(
            id=dto.notice_id,
            classId=dto.class_id,
            message=dto.message,
            createdAt=dto.created_at,
            updatedAt=dto.updated_at,
        )
