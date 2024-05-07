from bson import ObjectId
from typing import Annotated
from fastapi import Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorDatabase

from models.inventory import CreateInventory
from utils.database import get_db
from utils.validate_token import validate_token
from utils.exceptions import NotFoundRecord


router = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
)


@router.get("", dependencies=[Depends(validate_token)])
async def list_inventory(database: Annotated[AsyncIOMotorDatabase, Depends(get_db)]):
    inventory_list = [inventory async for inventory in database.inventory.find({})]

    return JSONResponse(content=jsonable_encoder(inventory_list), status_code=200)


@router.post("", dependencies=[Depends(validate_token)])
async def create_inventory(
    create_inventory: CreateInventory,
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)],
):
    inserted_id = await database.inventory.insert_one(
        {
            "_id": str(ObjectId()),
            "name": create_inventory.name,
            "price": create_inventory.price,
            "category": create_inventory.category,
        }
    )

    return JSONResponse(
        content={"created_inventory": inserted_id.inserted_id}, status_code=201
    )


@router.get("/{inventory_id}")
async def get_inventory(
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)],
    inventory_id: str,
):
    inventory = await database.inventory.find_one(
        {
            "_id": inventory_id,
        }
    )

    if not inventory:
        raise NotFoundRecord(f"Inventory with id {inventory_id} does not exists")

    return JSONResponse(content=inventory, status_code=200)
