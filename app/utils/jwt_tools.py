# app/utils/jwt_tools.py

from datetime import datetime, timedelta
from jose import jwt

JWT_SECRET = "yoursecretkey"
JWT_ALGORITHM = "HS256"
JWT_EXPIRE_HOURS = 72
JWT_ISSUER = "qonquer"

def generate_token(user_id: str) -> str:
    payload = {
        "id": user_id,
        "iss": JWT_ISSUER,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(hours=JWT_EXPIRE_HOURS),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def validate_token(token: str) -> dict:
    return jwt.decode(
        token,
        JWT_SECRET,
        algorithms=[JWT_ALGORITHM],
        issuer=JWT_ISSUER
    )
