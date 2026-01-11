from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    env: str

    mysql_host: str
    mysql_user: str
    mysql_password: str
    mysql_db: str
    mysql_port: int

    redis_url: str = None
    redis_password: str = None

    class Config:
        env_file = ".env"

settings = Settings()
