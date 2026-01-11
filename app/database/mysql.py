from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.config import settings

# Build the MySQL connection URL
DATABASE_URL = f"mysql+pymysql://{settings.mysql_user}:{settings.mysql_password}@{settings.mysql_host}:{settings.mysql_port}/{settings.mysql_db}"

# Create the engine
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Print SQL queries, optional for debugging
    pool_pre_ping=True  # Keep connection alive
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
