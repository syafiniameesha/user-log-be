from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from app.services.user_service import UserService
from app.database.init_db import get_db
from app.dto.user_dto import UserCreateDto, UserUpdateDto
from app.dto.response_dto import ResponseDto

router = APIRouter(tags=["User"])

@router.post("/list", response_model=ResponseDto)
def list_users(
    page: int = Form(default=0),
    page_size: int = Form(default=20),
    db: Session = Depends(get_db)
):
    return UserService.list_users(db, page, page_size)

@router.post("/create", response_model=ResponseDto)
def create_user(
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user_dto = UserCreateDto(name=name, email=email, password=password)
    return UserService.create_user(db, user_dto)

@router.post("/edit", response_model=ResponseDto)
def update_user(
    id: str = Form(...),
    name: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(get_db)
):
    user_dto = UserUpdateDto(id=id ,name=name, email=email)
    return UserService.update_user(db, user_dto)

@router.get("/{user_id}")
def get_user(user_id: str, db: Session = Depends(get_db)):
    return UserService.get_user_by_id(db, user_id)

@router.post("/toggle-access/{user_id}")
def toggle_access(user_id: str, db: Session = Depends(get_db)):
    return UserService.toggle_access(db, user_id)

@router.post("/toggle-admin/{user_id}")
def toggle_access(user_id: str, db: Session = Depends(get_db)):
    return UserService.toggle_admin(db, user_id)

@router.post("/forgot-password", response_model=ResponseDto)
def forgot_password(
    email: str = Form(...),
    db: Session = Depends(get_db)
):
    return UserService.forgot_password(db, email)

@router.post("/reset-password", response_model=ResponseDto)
def forgot_password(
    token: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    return UserService.reset_password(db, token, password)

@router.post("/change-password", response_model=ResponseDto)
def forgot_password(
    user_id: str = Form(...),
    old_password: str = Form(...),
    new_password: str = Form(...),
    db: Session = Depends(get_db)
):
    return UserService.change_password(db, user_id, old_password, new_password)