from typing import NoReturn
from decouple import config
from src.infrastructure.mongo.mongo_infrastructure import MongoInfrastructure
from src.domain.models.models_login import LoginModel

class Repository:

    __collection_name = config("ADDRESS_COLLECTION")

    @classmethod
    async def insert_address_info(cls, email: LoginModel) -> NoReturn:
        conection = MongoInfrastructure.get_collection(cls.__collection_name)
        insert = conection.insert_one(email)
        return


