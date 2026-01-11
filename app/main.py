from fastapi import FastAPI
from app.router.base import router  
from app.config.config import settings       
from app.database.init_db import init_db
from app.middleware.auth_middleware import auth_middleware

app = FastAPI(title="Project Backend")

# Register middleware (GLOBAL)
app.middleware("http")(auth_middleware)

# Include db 
# init_db() #uncomment for first run

# Include API router
app.include_router(router)

# Health check route
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
