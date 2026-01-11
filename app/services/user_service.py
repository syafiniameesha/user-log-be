from sqlalchemy.orm import Session
from app.models.user_model import User
from app.dto.response_dto import success, fail, success_count
from app.dto.user_dto import UserCreateDto, UserUpdateDto, UserResponseDto
from app.utils.password_tools import hash_password, verify_password
from datetime import datetime, timedelta
import uuid

class UserService:

    @staticmethod
    def list_users(db: Session, page: int = 0, page_size: int = 20):
        query = db.query(User).filter(User.filter_delete == False)
        total = query.count()
        users = query.offset(page * page_size).limit(page_size).all()
        user_dtos = [UserResponseDto.from_orm(u) for u in users]

        return success_count(user_dtos, total)

    @staticmethod
    def create_user(db: Session, user_dto: UserCreateDto):
        # Check if email exists
        existing = db.query(User).filter(User.email == user_dto.email).first()
        if existing:
            return fail("Email already exists")
        
        new_user = User(
            name=user_dto.name,
            email=user_dto.email,
            password=hash_password(user_dto.password)
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return success('Successfully create a new user')
    
    @staticmethod
    def update_user(db: Session, user_dto: UserUpdateDto):
        # Fetch the existing user by id
        existing_user = db.query(User).filter(User.id == user_dto.id).first()
        if not existing_user:
            return fail("Account does not exist")
        
        # Update name if provided
        if user_dto.name:
            existing_user.name = user_dto.name
        
        # Update email if provided and different
        if user_dto.email and existing_user.email != user_dto.email:
            email_taken = db.query(User).filter(User.email == user_dto.email).first()
            if email_taken:
                return fail("Email already exists")
            existing_user.email = user_dto.email
        
        db.commit()
        db.refresh(existing_user)
        return success("User updated successfully")

    
    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return fail("User not found")

        # Return user data
        user_data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "is_admin": user.is_admin,
            "access": user.access,
        }
        return success(user_data)
    
    @staticmethod
    def toggle_access(db: Session, user_id: str):
        # Fetch the existing user by id
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return fail("Account does not exist")
        
        # Update the fields
        user.access = not user.access
        db.commit()
        db.refresh(user)
        user_data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "is_admin": user.is_admin,
            "access": user.access,
        }
        return success(user_data)
    
    @staticmethod
    def toggle_admin(db: Session, user_id: str):
        # Fetch the existing user by id
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return fail("Account does not exist")
        
        # Update the fields
        user.is_admin = not user.is_admin
        db.commit()
        db.refresh(user)
        user_data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "is_admin": user.is_admin,
            "access": user.access,
        }
        return success(user_data)
    
    @staticmethod
    def forgot_password(db: Session, email: str):
        # Fetch the existing user by email
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return fail("Account does not exist")
        
        # Update the fields
        user.reset_token = str(uuid.uuid4())
        user.reset_expiry = datetime.utcnow() + timedelta(minutes=30)
        db.commit()
        db.refresh(user)
        return success("Forgot Password Request Sent")

    @staticmethod
    def reset_password(db: Session, token: str, new_password: str):
        user = db.query(User).filter(User.reset_token == token).first()
        if not user:
            return fail("Invalid or expired token")

        if not user.reset_expiry or user.reset_expiry < datetime.utcnow():
            return fail("Token expired")

        user.password = hash_password(new_password)
        user.reset_token = None
        user.reset_expiry = None

        db.commit()
        db.refresh(user)

        return success("Password reset successfully")
    
    @staticmethod
    def change_password(db: Session, user_id:str, old_password: str, new_password: str):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return fail("Account does not exist")
        
        if not verify_password(old_password, user.password):
            return fail("Incorrect old password")

        user.password = hash_password(new_password)

        db.commit()
        db.refresh(user)

        return success("Password reset successfully")
