import sys
sys.path.append("..") # Adds higher directory to python modules path.

from models.user_poc import UserPoc
from schemas.user_poc import UserPocRequest
from utils import get_password_hash
from fastapi import APIRouter, Path, HTTPException, Query, Body
from starlette import status
from data import USERS_POC, get_new_user_id_poc

router = APIRouter(
    prefix="/userspoc",
    tags=["userspoc"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not Found"}}
)

def get_userpoc_by_email_address(email_address: str):
    email_address = email_address.lower()
    for userpoc in USERS_POC:
        if userpoc.Email__address.lower() == email_address:
            return userpoc

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

def get_userpoc_by_userid(userId: str):
    for userpoc in USERS_POC:
        if userpoc.userid == userId:
            return userpoc

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

@router.get("/", status_code=status.HTTP_200_OK)
async def get_userpoc(email_address: str = Query(None, description="The email addres of the user to get"),
                      userId: str = Query(None, description="The userId of the user to get")):
    if email_address:
        return get_userpoc_by_email_address(email_address)

    if userId:
        return get_userpoc_by_userid(userId)

    return USERS_POC

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user_poc(user_request: UserPocRequest = Body(...)):
    new_userpoc = UserPoc(
        userid=None,
        Email__address=user_request.Email__address,
        Password=get_password_hash(user_request.Password),
        First__name=user_request.First__name,
        Last__name=user_request.Last__name,
        Business__operating__number=user_request.Business__operating__number,
        Business__number=user_request.Business__number,
        Business__legal__name=user_request.Business__legal__name,
        Contact__number=user_request.Contact__number,
        Business__address=user_request.Business__address,
        Mailing__address=user_request.Mailing__address
    )
    USERS_POC.append(get_new_user_id_poc(new_userpoc))
    return new_userpoc

@router.put("/{userId}", status_code=status.HTTP_200_OK)
async def update_userpoc(userId: str = Path(..., description="UserId to be update"),
                      user_request: UserPocRequest = Body(...)):
    userpoc = get_userpoc_by_userid(userId)

    if user_request.Email__address is not None:
        userpoc.Email__address = user_request.Email__address
    if user_request.Password is not None:
        userpoc.Password = get_password_hash(user_request.Password)
    if user_request.First__name is not None:
        userpoc.First__name = user_request.First__name
    if user_request.Last__name is not None:
        userpoc.Last__name = user_request.Last__name
    if user_request.Business__operating__number is not None:
        userpoc.Business__operating__number = user_request.Business__operating__number
    if user_request.Business__number is not None:
        userpoc.Business__number = user_request.Business__number
    if user_request.Business__legal__name is not None:
        userpoc.Business__legal__name = user_request.Business__legal__name
    if user_request.Contact__number is not None:
        userpoc.Contact__number = user_request.Contact__number
    if user_request.Business__address is not None:
        userpoc.Business__address = user_request.Business__address
    if user_request.Mailing__address is not None:
        userpoc.Mailing__address = user_request.Mailing__address

    return userpoc

@router.delete("/{userId}", status_code=status.HTTP_200_OK)
async def delete_userpoc(userId: str = Path(..., description="The ID of the user to delete")):
    userpoc = get_userpoc_by_userid(userId)
    USERS_POC.remove(userpoc)
    return {"message": "User deleted successfully"}