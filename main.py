from fastapi import FastAPI
from db import init_db
from config import get_settings
from schemas.user import BaseUser
from schemas.base import BaseResponse
from models.user import User

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="FastAPI CRUD Tortoise-orm with aerich",
    debug=settings.app_debug,
)


@app.on_event("startup")
async def startup():
    await init_db()
    print("DB Connected ✅")


@app.post("/user", response_model=BaseResponse)
async def create_user(user: BaseUser):
    user_data = await User.create(
        name=user.name,
        email=user.email,
        username=user.username
    )

    data = {
        "name": user_data.name,
        "email": user_data.email,
        "username": user_data.username
    }
    return BaseResponse(data=data)

@app.get("/users", response_model=BaseResponse)
async def get_all_users():
    users_data = await User.all()
    users = []
    for user in users_data:
        data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "username": user.username
        }
        users.append(data)
    return BaseResponse(data=users)

