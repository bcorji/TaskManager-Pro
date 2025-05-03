from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

app = FastAPI(
    title="TaskManager Pro API",
    description="A full-stack task management application with role-based authentication",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to TaskManager Pro API"}

# Import and include routers
# from app.routers import auth, tasks, users
# app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
# app.include_router(tasks.router, prefix="/api/tasks", tags=["Tasks"])
# app.include_router(users.router, prefix="/api/users", tags=["Users"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)