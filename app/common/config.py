from typing import Optional, Dict, Any

from pydantic import PostgresDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP: str
    TIME_ZONE: str
    APP_DIR: str
    API_BASE_URL: str

    POSTGRESQL_HOST: str
    POSTGRESQL_PORT: str
    POSTGRESQL_USERNAME: str
    POSTGRESQL_PASSWORD: str
    POSTGRESQL_POSTGRES_PASSWORD: str
    POSTGRESQL_DATABASE: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @field_validator("SQLALCHEMY_DATABASE_URI", mode='before')
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]):
        if isinstance(v, str):
            return v
        return PostgresDsn(
            f'postgresql://'
            f'{values.data.get("POSTGRESQL_USERNAME")}:'
            f'{values.data.get("POSTGRESQL_PASSWORD")}@'
            f'{values.data.get("POSTGRESQL_HOST")}:'
            f'{values.data.get("POSTGRESQL_PORT")}/'
            f'{values.data.get("POSTGRESQL_DATABASE")}'
        )

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='UTF-8',
        case_sensitive=True
    )


settings = Settings()
