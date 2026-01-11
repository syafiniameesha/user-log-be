from fastapi import APIRouter
from app.router.auth_router import router as auth_router
from app.router.user_router import router as user_router

# Create a central router
router = APIRouter()

# Include all module routers
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(user_router, prefix="/user", tags=["User"])
