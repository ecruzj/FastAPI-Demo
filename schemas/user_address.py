from pydantic import BaseModel, Field

class UserAddressRequest(BaseModel):
    userId: str
    Unit__number__mail: str = Field(min_length=1)
    Street__number__mail: str = Field(min_length=1)
    Street__name__mail: str = Field(min_length=1)
    PO__Box__mail: str = Field(min_length=1)
    Postal__zip__code__mail: str = Field(min_length=1)
    Citytown__mail: str = Field(min_length=1)
    Province__state__mail: str = Field(min_length=1)
    Country__mail: str = Field(min_length=1)
    Telephone__number__mail: str = Field(min_length=1)
    Extension__mail: str = Field(min_length=1)
    Fax__number__mail: str = Field(min_length=1)

    class Config:
        json_schema_extra = {
            'example': {
                'userId': '0bb05161-0ac1-4dea-9d94-76cfb4901e77',
                'Unit__number__mail': '101',
                'Street__number__mail': '456',
                'Street__name__mail': 'Maple Street',
                'PO__Box__mail': 'PO1234',
                'Postal__zip__code__mail': '12345',
                'Citytown__mail': 'Springfield',
                'Province__state__mail': 'Illinois',
                'Country__mail': 'USA',
                'Telephone__number__mail': '555-1234',
                'Extension__mail': '101',
                'Fax__number__mail': '555-5678'
            }
        }