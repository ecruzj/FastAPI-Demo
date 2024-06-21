from pydantic import BaseModel, Field
from typing import Optional

class UserPocRequest(BaseModel):
    userid: Optional[int] = None
    Email__address: str = Field(..., min_length=5, max_length=100)
    Password: str = Field(..., min_length=4)
    First__name: str = Field(..., min_length=1)
    Last__name: str = Field(..., min_length=1)
    Business__operating_number: str = Field(..., min_length=5)
    Business__number: str = Field(..., min_length=5)
    Business__legal__name: str = Field(..., min_length=1)
    Contact__number: str = Field(..., min_length=5)
    Business__address: str = Field(..., min_length=5)
    Mailing__address: str = Field(..., min_length=5)

    class Config:
        json_schema_extra = {
            'example': {
                'Email__address': 'example@example.com',
                'Password': 'securepassword123',
                'First__name': 'John',
                'Last__name': 'Doe',
                'Business__operating_number': '123456789',
                'Business__number': '987654321',
                'Business__legal__name': 'Example Inc.',
                'Contact__number': '123-456-7890',
                'Business__address': '123 Business St.',
                'Mailing__address': '456 Mailing Ave.'
            }
        }