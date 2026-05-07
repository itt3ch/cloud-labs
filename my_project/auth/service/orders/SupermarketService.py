from typing import List
from my_project.auth.dao import supermarketDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.Supermarket import Supermarket


class SupermarketService(GeneralService):
    _dao = supermarketDao

    def create(self, supermarket: Supermarket) -> None:
        self._dao.create(supermarket)

    def get_all_supermarkets(self) -> List[Supermarket]:
        return self._dao.find_all()

    def get_supermarket_by_id(self, id: int) -> Supermarket:
        return self._dao.find_by_id(id)
