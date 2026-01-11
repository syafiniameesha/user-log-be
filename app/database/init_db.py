# app/database/init_db.py
from app.database.mysql import engine, SessionLocal  # make sure SessionLocal is defined in mysql.py
from app.database.base import Base
from app.models.user_model import User  # import all your models

def init_db():
    Base.metadata.create_all(bind=engine)
    print("All tables created!")

# This is needed for FastAPI dependency injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# For standalone execution
if __name__ == "__main__":
    init_db()
