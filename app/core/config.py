import os

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DB_URL: str = "postgresql+asyncpg://postgres:password@localhost:5432/postgres"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379


class TestConfig(Config):
    DB_URL: str = "postgresql+asyncpg://postgres:password@localhost:5432/postgres"


class LocalConfig(Config): ...


class ProductionConfig(Config):
    DEBUG: bool = False


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "test": TestConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
