from typing import List
from my_project.auth.dao.orders.SupermarketDao import SupermarketDAO
from my_project.auth.domain.orders.Supermarket import Supermarket


class SupermarketController:
    _dao = SupermarketDAO()

    def find_all(self) -> List[Supermarket]:
        return self._dao.find_all()

    def create(self, supermarket: Supermarket) -> None:
        self._dao.create(supermarket)

    def find_by_id(self, supermarket_id: int) -> Supermarket:
        return self._dao.find_by_id(supermarket_id)

    def update(self, supermarket_id: int, supermarket: Supermarket) -> None:
        self._dao.update(supermarket_id, supermarket)

    def delete(self, supermarket_id: int) -> None:
        self._dao.delete(supermarket_id)
