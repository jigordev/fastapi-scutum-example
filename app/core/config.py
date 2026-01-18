from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Scutum Example"
    secret_key: str
    jwt_algorithm: str

    class Config:
        env_file = ".env"

settings = Settings()