from fastapi import APIRouter
from schema import users

router = APIRouter(prefix="/api/v1",
                   tags=["Auth"],)

@router.post("/login")
async def login(user_info: users.UserLogin):
    pass