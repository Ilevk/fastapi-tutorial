# app/models/db/student.py
from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.db.session import Base


class Student(Base):
    __tablename__ = "student"

    student_id: Mapped[str] = mapped_column(String(255), primary_key=True)
    student_name: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.now()
    )
