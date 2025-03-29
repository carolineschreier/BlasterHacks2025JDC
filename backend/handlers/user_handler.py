from fastapi import APIRouter, Request

router = APIRouter(prefix="/user")

@router.post("/login")
async def login(request: Request):
    """
    Login a user
    """
    return {"message": "Login successful"}

@router.post("/register")
async def register(request: Request):
    """
    Register a new user
    """
    return {"message": "User registered"}