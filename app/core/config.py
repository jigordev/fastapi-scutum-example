from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Scutum Example"
    database_url: str
    secret_key: str
    jwt_algorithm: str

    class Config:
        env_file = ".env"

settings = Settings()