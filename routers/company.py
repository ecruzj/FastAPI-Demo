from fastapi import APIRouter, Query, HTTPException, Path, Body
from starlette import status
from data import COMPANIES, get_new_company_id
from models.company import Company
from schemas.company import CompanyRequest

router = APIRouter(
    prefix="/companies",
    tags=["companies"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not Found"}}
)

def get_company_by_name(company_name: str):
    company_name = company_name.lower()
    for company in COMPANIES:
        if company.company_name.lower() == company_name:
            return company

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Company not found')

def get_company_by_companyid(company_id: int):
    for company in COMPANIES:
        if company.company_id == company_id:
            return company

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Company not found')

@router.get("/", status_code=status.HTTP_200_OK)
async def get_company(company_name: str = Query(None, description="The name of the company to get"),
                      company_id: int = Query(None, gt=0, description="The company_id of the company to get")):

    if company_name:
        return get_company_by_name(company_name)

    if company_id:
        return get_company_by_companyid(company_id)

    return COMPANIES

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_company(company_request: CompanyRequest):
    new_company = Company(**company_request.model_dump())
    COMPANIES.append(get_new_company_id(new_company))

    return new_company

@router.put("/{company_id}", status_code=status.HTTP_200_OK)
async def update_company(company_id: int = Path(..., gt=0, description="Company ID to update"),
                         company_request: CompanyRequest = Body(...)):
    company = get_company_by_companyid(company_id)

    if company_request.company_name is not None:
        company.company_name = company_request.company_name
    if company_request.address is not None:
        company.address = company_request.address
    if company_request.postal_code is not None:
        company.postal_code = company_request.postal_code

    return company

@router.delete("/{company_id}", status_code=status.HTTP_200_OK)
async def delete_company(company_id: int = Path(..., gt=0, description="Company ID to delete")):
    company = get_company_by_companyid(company_id)
    COMPANIES.remove(company)
    return {"message": "Company deleted successfully"}


