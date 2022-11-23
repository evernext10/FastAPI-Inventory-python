from functools import lru_cache
import os

from pydantic import BaseSettings

@lru_cache
def get_env_filename():
    runtime_env = os.getenv("ENV")
    return f".env.{runtime_env}" if runtime_env else ".env"


class EnvironmentSettings(BaseSettings):
    API_VERSION: str = 'fastapi-inventory-python'
    APP_NAME: str = 'fastapi-inventory-python'
    DATABASE_DIALECT: str = 'postgresql'
    DATABASE_HOSTNAME: str = 'localhost'
    DATABASE_NAME: str = 'inventory'
    DATABASE_PASSWORD: str = 'admin'
    DATABASE_PORT: int = 3306
    DATABASE_USERNAME: str = 'admin'
    DEBUG_MODE: bool = True

    class Config:
        env_file = get_env_filename()
        env_file_encoding = "utf-8"


@lru_cache
def get_environment_variables():
    return EnvironmentSettings()
