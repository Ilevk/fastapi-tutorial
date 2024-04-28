from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.db.session import Base


class Teacher(Base):
    __tablename__ = "teacher"

    teacher_id: Mapped[str] = mapped_column(String(255), primary_key=True)
    teacher_name: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.now()
    )
