import uvicorn
from fastapi import FastAPI

from routers import users

app = FastAPI()

app.include_router(router=users.router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
