from uuid import uuid4

from fastapi import APIRouter
from sqlalchemy import insert

from app.core.db.session import AsyncScopedSession
from app.models.schemas.common import BaseResponse, HttpResponse
from app.models.schemas.user import UserReq, UserResp
from app.models.db.student import Student
from app.models.db.teacher import Teacher

router = APIRouter()


@router.post("/teacher", response_model=BaseResponse[UserResp])
async def create_teacher(
    request_body: UserReq,
) -> BaseResponse[UserResp]:
    user_id = uuid4().hex
    async with AsyncScopedSession() as session:
        stmt = (
            insert(Teacher)
            .values(teacher_id=user_id, teacher_name=request_body.userName)
            .returning(Teacher)
        )

        result: Teacher = (await session.execute(stmt)).scalar()
        await session.commit()

    return HttpResponse(
        content=UserResp(
            userId=result.teacher_id,
            userName=result.teacher_name,
            userRole="teacher",
            createdAt=result.created_at,
        )
    )


@router.post("/student", response_model=BaseResponse[UserResp])
async def create_student(
    request_body: UserReq,
) -> BaseResponse[UserResp]:
    user_id = uuid4().hex
    async with AsyncScopedSession() as session:
        stmt = (
            insert(Student)
            .values(student_id=user_id, student_name=request_body.userName)
            .returning(Student)
        )

        result: Student = (await session.execute(stmt)).scalar()
        await session.commit()

    return HttpResponse(
        content=UserResp(
            userId=result.student_id,
            userName=result.student_name,
            userRole="student",
            createdAt=result.created_at,
        )
    )
