from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


@lambda _: _()  # iife
class Setting(BaseSettings):
    model_config = SettingsConfigDict(env_file=Path(__file__).parent.parent / ".env")

    django_secret_key: str

    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: str
