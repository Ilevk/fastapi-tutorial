from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

from app.models.dtos.common import PageDTO


@dataclass
class ClassDTO:
    class_id: str
    class_name: str
    teacher_id: str
    created_at: Optional[datetime] = None


@dataclass
class ClassListDTO:
    data: List[ClassDTO]
    page: PageDTO


@dataclass
class ClassNoticeDTO:
    notice_id: int
    class_id: str
    message: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class ClassNoticeListDTO:
    data: List[ClassNoticeDTO]
    page: PageDTO
