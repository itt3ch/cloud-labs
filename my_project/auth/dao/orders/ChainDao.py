from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Chain import Chain

class ChainDAO(GeneralDAO):
    _domain_type = Chain

    def create(self, chain: Chain) -> None:
        self._session.add(chain)
        self._session.commit()

    def find_all(self) -> List[Chain]:
        return self._session.query(Chain).all()

    def find_by_name(self, name: str) -> Optional[Chain]:
        return self._session.query(Chain).filter(Chain.name == name).first()
