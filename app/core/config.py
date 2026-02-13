from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_ENV: str = "development"
    DATABASE_URL: str = "postgresql://postgres:jyotsana123@localhost/document_intelligence_db"
    OPENAI_API_KEY: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
