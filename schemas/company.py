from typing import Optional
from pydantic import BaseModel, Field

class CompanyRequest(BaseModel):
    company_id: Optional[int] = None
    company_name: str = Field(min_length=3)
    address: str = Field(min_length=5)
    postal_code: str = Field(min_length=4)

    class Config:
        json_schema_extra = {
            'example': {
                'company_name': 'TechCorp',
                'address': '123 Tech Lane',
                'postal_code': '98765'
            }
        }