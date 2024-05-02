from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase
from starlette_context import context

from app.core.config import config, is_local


def get_session_id():
    return context.get("session_id")


class Base(DeclarativeBase): ...


engine = create_async_engine(
    config.DB_URL, pool_size=10, max_overflow=5, echo=is_local(), pool_pre_ping=True
)

async_session_factory = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

AsyncScopedSession = async_scoped_session(
    async_session_factory, scopefunc=get_session_id
)


async def ping_db():
    async with engine.begin() as conn:
        await conn.execute(text("SELECT 1"))


async def close_db():
    await engine.dispose()
