from fastapi import APIRouter, HTTPException, status
from src.service.login_service.login_service import LoginService


API = APIRouter()

@API.post("/")
async def insertion_email(email):
        insert = LoginService.insert_email(email)
        return insert