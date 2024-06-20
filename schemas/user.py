from typing import Optional
from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    user_id: Optional[int] = None
    user_name: str = Field(min_length=3)
    first_name: str = Field(min_length=3)
    last_name: str = Field(min_length=3)
    password: str = Field(min_length=4)

    class Config:
        json_schema_extra = {
            'example': {
                'user_name': 'jsmith',
                'first_name': 'John',
                'last_name': 'Smith',
                'password': 'smith123'
            }
        }
