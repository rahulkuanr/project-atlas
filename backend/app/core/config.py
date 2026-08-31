from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    app_name: str = "Atlas API"
    app_version: str = "0.1.0"
    environment: str = "development"
    database_url: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_prefix="ATLAS_",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()
