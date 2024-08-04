from pydantic import BaseModel

class UserLogin(BaseModel):
    userEmail :str
    userPassword :str