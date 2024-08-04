import pymongo
import pymongo.collection
from passlib.context import CryptContext

from database import MongoDB
from utils.authentication import verify_password

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(email: str) -> dict:
    """Get user information in Mongo database

    Parameters
    ----------
    email : str
        User's email

    Returns
    -------
    dict
        User's information
    """
    with MongoDB(db_name="service_config") as db:
        collection: pymongo.collection.Collection = db["users"]

        user_info = collection.find_one(filter={"userEmail": email})

    return user_info


def validate_user(
    user_email: str,
    user_password: str,
) -> bool:
    """Validate user

    Parameters
    ----------
    user_email : str
        User's email
    user_password : str
        User's plain password

    Returns
    -------
    bool
        True or Fasle
    """
    user_info = get_user(user_email)
    print(user_info)

    if not user_info:
        # TODO : 유저 없음으로 return 해야함.
        return False

    if not verify_password(user_password, user_info["userPassword"]):
        # TODO : 유저 비밀번호 틀림으로 return 해야함.
        return False

    # TODO : 로그인 검증이 끝났다는 의미
    return True
