from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "AMLIP Backend"

    POSTGRES_USER: str = "amlip_user"
    POSTGRES_PASSWORD: str = "amlip_password"
    POSTGRES_SERVER: str = "127.0.0.1"
    POSTGRES_PORT: int = 5433
    POSTGRES_DB: str = "amlip_db"

    CLICKHOUSE_HOST: str = "127.0.0.1"
    CLICKHOUSE_PORT: int = 8123
    CLICKHOUSE_USER: str = "amlip_user"
    CLICKHOUSE_PASSWORD: str = "amlip_password"
    CLICKHOUSE_DB: str = "amlip_analytics"

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
