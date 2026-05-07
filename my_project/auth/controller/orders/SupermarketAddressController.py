from typing import List
from my_project.auth.dao.orders.SupermarketAddressDao import SupermarketAddressDAO
from my_project.auth.domain.orders.SupermarketAddress import SupermarketAddress


class SupermarketAddressController:
    _dao = SupermarketAddressDAO()

    def find_all(self) -> List[SupermarketAddress]:
        return self._dao.find_all()

    def create(self, address: SupermarketAddress) -> None:
        self._dao.create(address)

    def find_by_id(self, address_id: int) -> SupermarketAddress:
        return self._dao.find_by_id(address_id)

    def update(self, address_id: int, address: SupermarketAddress) -> None:
        self._dao.update(address_id, address)

    def delete(self, address_id: int) -> None:
        self._dao.delete(address_id)
