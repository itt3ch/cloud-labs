from typing import List, Optional
from sqlalchemy.orm import joinedload
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Supermarket import Supermarket

class SupermarketDAO(GeneralDAO):
    _domain_type = Supermarket

    def create(self, supermarket: Supermarket) -> None:
        self._session.add(supermarket)
        self._session.commit()

    def find_all(self) -> List[Supermarket]:
        return self._session.query(Supermarket).options(joinedload(Supermarket.chain)).all()

    def find_by_name(self, name: str) -> Optional[Supermarket]:
        return self._session.query(Supermarket).filter(Supermarket.name == name).first()
