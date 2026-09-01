from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "AMLIP Backend"

    POSTGRES_USER: str = "amlip_user"
    POSTGRES_PASSWORD: str = "amlip_password"
    POSTGRES_SERVER: str = "127.0.0.1"
    POSTGRES_PORT: int = 5433
    POSTGRES_DB: str = "amlip_db"

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
