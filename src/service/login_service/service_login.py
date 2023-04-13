#Local
from src.repository.mongo.mongo_repository import Repository_Mongo
from src.service.obfuscate_data.obfuscate_data_service import ObfuscateDataService
from src.domain.models.models_register import RegisterModel


class LoginPermission():
    @staticmethod
    async def email_recognition(email: str) -> str:
        email_input: RegisterModel = {"email": email}
        search_email_in_mongo = await Repository_Mongo.get_object_recognition(email_input)
        return search_email_in_mongo


    @classmethod
    async def passaword_validate(cls, email:str, password: float) -> str:
        get_date_in_mongo = await cls.email_recognition(email)
        password_cripto = get_date_in_mongo["password"]
        deobfuscate_password = ObfuscateDataService.deobfuscate_value(password_cripto)
        if deobfuscate_password == password:
            return "Login Sucess"
        else:
            return "Password incorrect"


