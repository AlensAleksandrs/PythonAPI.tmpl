from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Python API"
    ENVIRONMENT: str = "development"
    
    REDIS_URL: str = "redis://localhost:6379/0"

    STORAGE_BACKEND: str = "local"  # or "s3"
    LOCAL_STORAGE_PATH: str = "storage/uploads"

    S3_ENDPOINT_URL: str | None = None
    S3_BUCKET_NAME: str | None = None
    S3_ACCESS_KEY: str | None = None
    S3_SECRET_KEY: str | None = None
    S3_REGION: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()