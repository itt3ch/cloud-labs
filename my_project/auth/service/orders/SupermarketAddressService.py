from typing import List
from my_project.auth.dao import supermarketAddressDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.SupermarketAddress import SupermarketAddress


class SupermarketAddressService(GeneralService):
    _dao = supermarketAddressDao

    def create(self, supermarket_address: SupermarketAddress) -> None:
        self._dao.create(supermarket_address)

    def get_all_supermarket_addresses(self) -> List[SupermarketAddress]:
        return self._dao.find_all()

    def get_supermarket_address_by_id(self, id: int) -> SupermarketAddress:
        return self._dao.find_by_id(id)
