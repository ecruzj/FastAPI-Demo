from fastapi import FastAPI
from routers import user, company, user_poc, user_address

app = FastAPI()

app.include_router(user.router)
app.include_router(company.router)
app.include_router(user_poc.router)
app.include_router(user_address.router)