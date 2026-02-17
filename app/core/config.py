from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:jyotsana123@localhost/document_intelligence_db"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore", 
    )


settings = Settings()
