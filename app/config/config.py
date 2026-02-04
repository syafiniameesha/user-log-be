from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    env: str
    db_type: str  # mysql or postgresql

    # MySQL config
    mysql_host: str = None
    mysql_user: str = None
    mysql_password: str = None
    mysql_db: str = None
    mysql_port: int = None

    # PostgreSQL config
    postgres_host: str = None
    postgres_user: str = None
    postgres_password: str = None
    postgres_db: str = None
    postgres_port: int = None

    # Redis config
    redis_url: str = None
    redis_password: str = None

    class Config:
        env_file = ".env"  # Load from .env automatically

# Create a single settings object to import anywhere
settings = Settings()
