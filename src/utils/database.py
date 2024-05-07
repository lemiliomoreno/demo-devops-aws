import os

from motor.motor_asyncio import AsyncIOMotorClient


MONGODB_URI = os.getenv("MONGODB_URI")


async def get_db():
    client = AsyncIOMotorClient(MONGODB_URI)
    return client["demo-aws-devops"]
