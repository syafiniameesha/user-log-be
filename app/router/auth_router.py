# app/routers/auth_router.py

from fastapi import APIRouter, Depends, Response, Form
from sqlalchemy.orm import Session
from app.database.init_db import get_db
from app.services.auth_service import AuthService
from app.dto.response_dto import success

router = APIRouter(tags=["Auth"])


@router.post("/login")
def login(
    response: Response,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    result = AuthService.login(db, email, password)

    # ResponseDto check
    if result.code != 0:
        return result

    token = result.data

    response.set_cookie(
        key="test_jwt",
        value=token,
        max_age=2147483647,
        httponly=True,
        secure=False,   # set True in prod
        samesite="lax"
    )

    return success("Login successful")


@router.post("/logout")
def logout(
    response: Response,
    user_id: str = Form(...),
    db: Session = Depends(get_db)
):
    result = AuthService.logout(db, user_id)

    if result.code != 0:
        return result

    # Clear cookie
    response.delete_cookie(
        key="test_jwt",
        path="/"
    )

    return result