import pymongo
import pymongo.collection

from database import MongoDB
from schema.token import Token


def get_user_token_info(user_email: str):

    with MongoDB(db_name="service_config") as db:
        collection: pymongo.collection.Collection = db["token"]

        user_token_info = collection.find_one(filter={"userEmail": user_email})

    return user_token_info


def create_user_token_info(
    user_email: str,
    refresh_token: str,
):

    with MongoDB(db_name="service_config") as db:
        collection: pymongo.collection.Collection = db["token"]

        document = Token(
            userEmail=user_email,
            refreshToken=refresh_token,
        ).model_dump()
        collection.insert_one(document=document)


# TODO : update refresh token
