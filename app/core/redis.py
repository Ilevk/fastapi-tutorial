import pickle

from redis.asyncio import Redis

from app.core.config import config


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


def key_builder(*args) -> str:
    return ":".join(map(str, args))


redis_cache = RedisCache()
