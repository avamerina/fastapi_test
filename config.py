import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_user: str = os.getenv("POSTGRES_USER")
    postgres_password: str = os.getenv("POSTGRES_PASSWORD")
    postgres_db: str = os.getenv("POSTGRES_DB")

    @property
    def sqlalchemy_database_url(self) -> str:
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@db:5432/{self.postgres_db}"

    class Config:
        env_file = ".env"


settings = Settings()
