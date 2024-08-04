from pydantic import BaseModel


class Token(BaseModel):
    userEmail: str
    refreshToken: str
