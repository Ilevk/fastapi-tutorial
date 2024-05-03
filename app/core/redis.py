import pickle
from functools import wraps
from typing import Callable

from redis.asyncio import Redis

from app.core.config import config
from app.core.logger import logger


class RedisCache:
    def __init__(self):
        self.redis = Redis(
            host=config.REDIS_HOST,
            port=config.REDIS_PORT,
        )

    async def ping(self) -> None:
        await self.redis.ping()

    async def close(self) -> None:
        await self.redis.close()

    async def set(self, key: str, value: object, ttl: int = None) -> None:
        await self.redis.set(key, pickle.dumps(value), ex=ttl)

    async def get(self, key: str) -> object:
        value = await self.redis.get(key)
        return pickle.loads(value)

    async def exists(self, key: str) -> bool:
        return await self.redis.exists(key)


class RedisCacheDecorator:
    def __init__(self, ttl: int = 60):
        self.ttl = ttl

    def key_builder(self, *args) -> str:
        return ":".join(map(str, args))

    def __call__(self, func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            _key = self.key_builder(func.__name__, *args, *kwargs)

            if await redis_cache.exists(_key):
                logger.debug("Cache hit")
                result = await redis_cache.get(_key)
            else:
                logger.debug("Cache miss")
                result = await func(*args, **kwargs)
                if result:
                    await redis_cache.set(_key, result, ttl=self.ttl)

            return result

        return wrapper


redis_cache = RedisCache()
