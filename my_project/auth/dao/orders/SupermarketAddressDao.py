from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.SupermarketAddress import SupermarketAddress

class SupermarketAddressDAO(GeneralDAO):
    _domain_type = SupermarketAddress

    def create(self, address: SupermarketAddress) -> None:
        self._session.add(address)
        self._session.commit()

    def find_all(self) -> List[SupermarketAddress]:
        return self._session.query(SupermarketAddress).all()

    def find_by_supermarket_id(self, supermarket_id: int) -> List[SupermarketAddress]:
        return self._session.query(SupermarketAddress).filter(SupermarketAddress.supermarket_id == supermarket_id).all()
