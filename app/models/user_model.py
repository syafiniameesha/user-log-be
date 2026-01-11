from sqlalchemy import Column, String, Boolean, BigInteger
from app.database.base import Base
import uuid
import time

def current_milli_time():
    return int(time.time() * 1000)

class User(Base):
    __tablename__ = "user"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    file_id = Column(String(36), nullable=True)
    access = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    filter_delete = Column(Boolean, default=False)
    token = Column(String(255), nullable=True)
    reset_token = Column(String(255), nullable=True)
    reset_expiry = Column(BigInteger, nullable=True)
    created_at = Column(BigInteger, default=current_milli_time)
    updated_at = Column(BigInteger, default=current_milli_time, onupdate=current_milli_time)
