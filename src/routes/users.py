import secrets

from bson import ObjectId
from typing import Annotated
from fastapi import Depends, APIRouter
from motor.motor_asyncio import AsyncIOMotorDatabase

from models.users import CreateUser
from utils.database import get_db
from utils.exceptions import DuplicateRecord, NotFoundRecord


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("")
async def create_users(
    create_user: CreateUser,
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)],
):
    user_exists = await database.users.find_one({"email": create_user.email})

    if user_exists:
        raise DuplicateRecord(f"User {create_user.email} already exists")

    inserted_id = await database.users.insert_one(
        {
            "_id": str(ObjectId()),
            "email": create_user.email,
            "token": secrets.token_hex(12),
        }
    )

    return {"created_user": inserted_id.inserted_id}


@router.get("/{user_id}")
async def get_user(
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)],
    user_id: str,
):
    user = await database.users.find_one(
        {
            "_id": user_id,
        }
    )

    if not user:
        raise NotFoundRecord(f"User with id {user_id} does not exists")

    return user
