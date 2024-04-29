import logging

from app.core.config import config


def init_logger() -> None:
    logger = logging.getLogger("uvicorn")
    logger.setLevel(config.LOG_LEVEL)

    return logger


logger = init_logger()
