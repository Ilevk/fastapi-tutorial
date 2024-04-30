# app/models/db/class_.py

from datetime import datetime
from typing import Optional

from sqlalchemy import String, DateTime, Integer, Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.db.session import Base


class Class(Base):
    __tablename__ = "class"

    class_id: Mapped[str] = mapped_column(String(255), primary_key=True)
    class_name: Mapped[str] = mapped_column(String(255), nullable=False)
    teacher_id: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.now()
    )


class ClassNotice(Base):
    __tablename__ = "class_notice"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    class_id: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.now()
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), nullable=True, onupdate=datetime.now()
    )


class ClassStudent(Base):
    __tablename__ = "class_student"

    class_id: Mapped[str] = mapped_column(String(255), nullable=False, primary_key=True)
    student_id: Mapped[str] = mapped_column(
        String(255), nullable=False, primary_key=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.now()
    )
