import sys
sys.path.append("..") # Adds higher directory to python modules path.

from fastapi import APIRouter, Path, HTTPException, Query, Body
from starlette import status
from data import USERS, get_password_hash, get_new_user_id
from models.user import User
from schemas.user import UserRequest

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not Found"}}
)

def get_user_by_username(user_name: str):
    user_name = user_name.lower()
    for user in USERS:
        if user.user_name.lower() == user_name:
            return user

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

def get_user_by_userid(user_id: int):
    for user in USERS:
        if user.user_id == user_id:
            return user

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(user_name: str = Query(None, description="The name of the user to get"),
                   user_id: int = Query(None, gt=0, description="The user_id of the user to get")):
    if user_name:
        return get_user_by_username(user_name)

    if user_id:
        return get_user_by_userid(user_id)

    return USERS

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user_request: UserRequest):
    hashed_password = get_password_hash(user_request.password)
    new_user = User(
        user_id=None,
        user_name=user_request.user_name,
        first_name=user_request.first_name,
        last_name=user_request.last_name,
        hashed_password=hashed_password
    )
    USERS.append(get_new_user_id(new_user))
    return new_user


@router.put("/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: int = Path(..., gt=0, description="User ID to be update"),
                      user_request: UserRequest = Body(...)):
    user = get_user_by_userid(user_id)

    if user_request.user_name is not None:
        user.user_name = user_request.user_name
    if user_request.first_name is not None:
        user.first_name = user_request.first_name
    if user_request.last_name is not None:
        user.last_name = user_request.last_name
    if user_request.password is not None:
        user.hashed_password = get_password_hash(user_request.password)

    return user

@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int = Path(..., gt=0, description="The ID of the user to delete")):
    user = get_user_by_userid(user_id)
    USERS.remove(user)
    return {"message": "User deleted successfully"}