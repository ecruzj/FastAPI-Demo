from dataclasses import dataclass, field

@dataclass
class Company:
    company_id: int = field(init=False)
    company_name: str
    address: str
    postal_code: str

    def __init__(self, company_id, company_name, address, postal_code):
        self.company_id = company_id
        self.company_name = company_name
        self.address = address
        self.postal_code = postal_code