from fastapi import APIRouter

from curd.token import create_user_token_info
from curd.users import validate_user
from schema import users
from utils.authentication import get_access_token, get_refresh_token

router = APIRouter(
    prefix="/api/v1",
    tags=["Auth"],
)


@router.post("/login")
async def login(user_info: users.UserLogin):

    # Validate user
    user_confirm = validate_user(
        user_email=user_info.userEmail,
        user_password=user_info.userPassword,
    )

    # Issue Access Token
    if user_confirm:
        access_token = get_access_token(user_info)

        # TODO: Refresh Token Update or Add
        refresh_token = get_refresh_token()
        create_user_token_info(
            user_email=user_info.userEmail,
            refresh_token=refresh_token,
        )

    else:
        return False

    return access_token
