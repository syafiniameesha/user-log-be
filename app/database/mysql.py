from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.config import settings

# Build the MySQL connection URL
# DATABASE_URL = f"mysql+pymysql://{settings.mysql_user}:{settings.mysql_password}@{settings.mysql_host}:{settings.mysql_port}/{settings.mysql_db}"

# # Create the engine
# engine = create_engine(
#     DATABASE_URL,
#     echo=True,  # Print SQL queries, optional for debugging
#     pool_pre_ping=True  # Keep connection alive
# )

# Decide DB type dynamically (MySQL/PostgreSQL)
if settings.db_type.lower() == "postgresql":
    DATABASE_URL = (
        f"postgresql+psycopg2://{settings.postgres_user}:"
        f"{settings.postgres_password}@{settings.postgres_host}:"
        f"{settings.postgres_port}/{settings.postgres_db}"
    )
elif settings.db_type.lower() == "mysql":
    DATABASE_URL = (
        f"mysql+pymysql://{settings.mysql_user}:"
        f"{settings.mysql_password}@{settings.mysql_host}:"
        f"{settings.mysql_port}/{settings.mysql_db}"
    )
else:
    raise ValueError("Unsupported db_type in .env")

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    echo=True,  # logs SQL queries
    pool_pre_ping=True
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
