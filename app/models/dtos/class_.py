from dataclasses import dataclass
from typing import Optional

from datetime import datetime


@dataclass
class ClassDTO:
    class_id: str
    class_name: str
    teacher_id: str
    created_at: Optional[datetime] = None


@dataclass
class ClassNoticeDTO:
    notice_id: int
    class_id: str
    message: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
