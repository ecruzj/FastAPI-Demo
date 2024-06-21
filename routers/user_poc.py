import sys
sys.path.append("..") # Adds higher directory to python modules path.

from fastapi import APIRouter, Path, HTTPException, Query, Body
from starlette import status
from data import USERS_POC

router = APIRouter(
    prefix="/userspoc",
    tags=["userspoc"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not Found"}}
)

def get_userpoc_by_email_address(email_address: str):
    email_address = email_address.lower()
    for userpoc in USERS_POC:
        if userpoc.email__address.lower() == email_address:
            return userpoc

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

def get_userpoc_by_userid(user_id: str):
    for userpoc in USERS_POC:
        if userpoc.userid == user_id:
            return userpoc

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

@router.get("/", status_code=status.HTTP_200_OK)
async def get_userpoc(email_address: str = Query(None, description="The email addres of the user to get"),
                      userid: str = Query(None, description="The userid of the user to get")):
    if email_address:
        return get_userpoc_by_email_address(email_address)

    if userid:
        return get_userpoc_by_userid(userid)

    return USERS_POC