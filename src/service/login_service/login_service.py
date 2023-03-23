from src.repository.mongo.mongo_repository import Repository
from src.domain.models.models_login import LoginModel
from typing import NoReturn
from pydantic import validate_email

class LoginService:

    @classmethod
    async def insert_email(cls, email) -> NoReturn:
        validate = validate_email(email)
        typedict: LoginModel = {
            "email": f'{validate[1]}'
        }
        await Repository.insert_address_info(typedict)
        return typedict