import os
import logging

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    LOG_LEVEL: int = logging.DEBUG
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DB_URL: str = "postgresql+asyncpg://postgres:password@localhost:5432/postgres"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379


class TestConfig(Config):
    DB_URL: str = "postgresql+asyncpg://postgres:password@localhost:5432/postgres"


class LocalConfig(Config): ...


class ProductionConfig(Config):
    LOG_LEVEL: int = logging.INFO


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "test": TestConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


def is_local():
    return get_config().ENV == "local"


config: Config = get_config()
