from typing import Optional
from dataclasses import dataclass
from datetime import datetime

from app.models.constant import UserRole


@dataclass
class UserDTO:
    user_id: str
    user_name: str
    user_role: UserRole
    created_at: Optional[datetime] = None
