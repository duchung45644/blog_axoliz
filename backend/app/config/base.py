from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Axoliz"
    PROJECT_VERSION: str = "1.0.0"
    DATABASE_URL: str = ""  # Set this in .env
    ALLOWED_ORIGINS: list = ["http://vps.axoliz.com", "http://vps.axoliz.com:5432"]

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 300  # Token hết hạn sau 300 phút

    class Config:
        env_file = ".env"


settings = Settings()
