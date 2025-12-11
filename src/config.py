from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
import os

class Settings(BaseSettings):
    openai_api_key: str

    model_config = SettingsConfigDict(env_file=os.getenv('ENV_FILE', '.env'))

@lru_cache
def get_settings():
    return Settings()