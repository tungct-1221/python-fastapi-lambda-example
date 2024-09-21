
from typing import Any, Dict, List

from pydantic_settings import BaseSettings

"""
config.py

This module contains all the global configuration settings for the application.
"""


class Settings(BaseSettings):
    ENVIRONMENT: str = "development"
    DEBUG: bool = False

    DATABASE_HOST: str = "localhost"
    DATABASE_NAME: str = "example"
    DATABASE_PORT: int = 5432
    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str = "password"

    LOGGING_CONFIG: Dict[str, Any] = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
            },
        },
        "root": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    }


settings = Settings()
