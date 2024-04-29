import os
import logging
from typing import Dict, Any

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    ENV: str = "dev"
    TITLE: str = "FastAPI Tutorial"
    VERSION: str = "0.1.0"
    APP_HOST: str = "http://localhost:8000"
    OPENAPI_URL: str = "/openapi.json"
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"

    LOG_LEVEL: int = logging.DEBUG

    DB_URL: str = "postgresql+asyncpg://postgres:password@localhost:5432/postgres"

    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "servers": [
                {"url": self.APP_HOST, "description": os.getenv("ENV", "local")}
            ],
            "openapi_url": self.OPENAPI_URL,
            "docs_url": self.DOCS_URL,
            "redoc_url": self.REDOC_URL,
        }


class TestConfig(Config):
    DB_URL: str = "postgresql+asyncpg://postgres:password@localhost:5432/postgres"


class LocalConfig(Config): ...


class ProductionConfig(Config):
    LOG_LEVEL: int = logging.INFO
    APP_HOST: str = "fastapi.tutorial.com"

    OPENAPI_URL: str = "/openapi.json"
    DOCS_URL: str = ""
    REDOC_URL: str = ""


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
