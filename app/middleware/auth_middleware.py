# app/middleware/auth_middleware.py

from fastapi import Request
from fastapi.responses import JSONResponse
from app.utils.jwt_tools import validate_token
from app.database.init_db import SessionLocal
from app.models.user_model import User
from app.dto.response_dto import fail

WHITELIST = [
    "/auth/login",
    "/auth/logout",
    "/user/forgot-password",
    "/user/reset-password",
    "/user/create",
]


def is_whitelisted(path: str) -> bool:
    for w in WHITELIST:
        if w in path:
            return True
    return False


async def auth_middleware(request: Request, call_next):
    path = request.url.path

    # OPTIONS → allow
    if request.method == "OPTIONS":
        return await call_next(request)

    # Whitelisted paths
    if is_whitelisted(path):
        return await call_next(request)

    # Get JWT from cookie
    token = request.cookies.get("test_jwt")
    if not token:
        return JSONResponse(
            status_code=401,
            content=fail("Unauthorized").dict()
        )

    # Validate JWT
    try:
        claims = validate_token(token)
    except Exception:
        response = JSONResponse(
            status_code=401,
            content=fail("Invalid token").dict()
        )
        response.delete_cookie("test_jwt")
        return response

    # DB check
    db = SessionLocal()
    user = db.query(User).filter(User.id == claims.id).first()
    db.close()

    if not user or not user.access or user.filter_delete:
        response = JSONResponse(
            status_code=401,
            content=fail("Unauthorized").dict()
        )
        response.delete_cookie("test_jwt")
        return response

    # Attach user context (Gin: c.Set)
    request.state.user_id = user.id
    request.state.is_admin = user.is_admin

    return await call_next(request)
