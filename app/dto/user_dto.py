from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreateDto(BaseModel):
    name: str = Field(..., example="John Doe")
    email: EmailStr = Field(..., example="john@example.com")
    password: str = Field(..., min_length=6, example="password123")

class UserUpdateDto(BaseModel):
    id: str
    name: Optional[str] = None
    email: Optional[EmailStr] = None

class UserResponseDto(BaseModel):
    id: str
    name: str
    email: EmailStr
    access: bool
    is_admin: bool
    created_at: int

    model_config = {
        "from_attributes": True
    }
