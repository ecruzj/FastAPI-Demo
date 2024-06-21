from pydantic import BaseModel, Field
from typing import Optional

class UserPocRequest(BaseModel):
    userid: str
    email__address: str = Field(..., min_length=5, max_length=100)
    password: str = Field(..., min_length=4)
    first__name: str = Field(..., min_length=1)
    last__name: str = Field(..., min_length=1)
    business__operating_number: str = Field(..., min_length=5)
    business__number: str = Field(..., min_length=5)
    business__legal__name: str = Field(..., min_length=1)
    contact__number: str = Field(..., min_length=5)
    business__address: str = Field(..., min_length=5)
    mailing__address: str = Field(..., min_length=5)

    class Config:
        json_schema_extra = {
            'example': {
                'user_id': '0bb05161-0ac1-4dea-9d94-76cfb4901e2e',
                'email__address': 'example@example.com',
                'password': 'securepassword123',
                'first__name': 'John',
                'last__name': 'Doe',
                'business__operating_number': '123456789',
                'business__number': '987654321',
                'business__legal__name': 'Example Inc.',
                'contact__number': '123-456-7890',
                'business__address': '123 Business St.',
                'mailing__address': '456 Mailing Ave.'
            }
        }