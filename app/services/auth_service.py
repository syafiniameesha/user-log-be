# app/services/auth_service.py

from sqlalchemy.orm import Session
from app.models.user_model import User
from app.utils.password_tools import verify_password
from app.utils.jwt_tools import generate_token
from app.dto.response_dto import success, fail

class AuthService:

    @staticmethod
    def login(db: Session, email: str, password: str):
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return fail("We didn’t find an account with those email credentials")

        if not verify_password(password, user.password):
            return fail("We didn’t find an account with those password credentials")

        if not user.access:
            return fail("Account is disabled")

        token = generate_token(str(user.id))
        user.token = token
        db.commit()

        return success(token)
    
    @staticmethod
    def logout(db: Session, user_id: str):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return fail("Account does not exist")

        user.token = None
        db.commit()

        return success("Logout successful")
