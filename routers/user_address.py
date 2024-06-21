import sys

from models.user_address import UserAddress
from schemas.user_address import UserAddressRequest

sys.path.append("..") # Adds higher directory to python modules path.

from fastapi import APIRouter, Path, HTTPException, Query, Body
from starlette import status
from data import USERS_ADDRESS

router = APIRouter(
    prefix="/user_address",
    tags=["user_address"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not Found"}}
)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_user_addresses():
    return USERS_ADDRESS

@router.get("/{userId}", status_code=status.HTTP_200_OK)
async def get_user_address_by_user_id(userId: str = Path(..., description="The userId of the user address to get")):
    for address in USERS_ADDRESS:
        if address.userId == userId:
            return address

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User address not found')

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user_address(user_address_request: UserAddressRequest):
    new_user_address = UserAddress(**user_address_request.dict())
    USERS_ADDRESS.append(new_user_address)
    return new_user_address