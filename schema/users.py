from pydantic import BaseModel


class UserLogin(BaseModel):
    userEmail: str
    userPassword: str


class User(BaseModel):
    tenantId: str
    groupIds: list[str]
    position: str
    userEmail: str
    userPassword: str
    phoneNumber: str
    createTime: str
    updateTime: str
