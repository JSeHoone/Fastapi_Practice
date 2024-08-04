import os
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv

# TODO : jose를 사용할지 pyjwt를 사용할지 고민
from jose import jwt
from passlib.context import CryptContext

from schema import users

# load access token info
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


# TODO : 상수로 빼둬야 할지, 함수 내부로 넣어야 할지 고민 필요
PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(
    plain_password: str,
    hashed_password: str,
):
    return PWD_CONTEXT.verify(plain_password, hashed_password)


def get_access_token(
    user_information: users.UserLogin,
):
    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = _create_access_token(
        data={"sub": user_information.userEmail},
        expire_delta=access_token_expires,
    )

    return access_token


def _create_access_token(data: dict, expire_delta: timedelta):
    to_encode = data.copy()

    if expire_delta:
        expire = datetime.now(timezone.utc) + expire_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

    return encoded_jwt
