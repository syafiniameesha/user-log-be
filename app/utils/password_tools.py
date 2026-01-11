from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    clean = password.strip()[:72]
    return pwd_context.hash(clean)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    clean = plain_password.strip()[:72]
    return pwd_context.verify(clean, hashed_password)
