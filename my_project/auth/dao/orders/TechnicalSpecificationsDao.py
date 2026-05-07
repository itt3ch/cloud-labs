from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.TechnicalSpecifications import TechnicalSpecifications


class TechnicalSpecificationsDAO(GeneralDAO):
    _domain_type = TechnicalSpecifications

    def create(self, technical_specifications: TechnicalSpecifications) -> None:
        self._session.add(technical_specifications)
        self._session.commit()

    def find_all(self) -> List[TechnicalSpecifications]:
        return self._session.query(TechnicalSpecifications).all()

    def find_by_id(self, id: int) -> Optional[TechnicalSpecifications]:
        return self._session.query(TechnicalSpecifications).filter(TechnicalSpecifications.id == id).first()

    def update(self, id: int, updates: dict) -> None:
        self._session.query(TechnicalSpecifications).filter(TechnicalSpecifications.id == id).update(updates)
        self._session.commit()

    def delete(self, id: int) -> None:
        self._session.query(TechnicalSpecifications).filter(TechnicalSpecifications.id == id).delete()
        self._session.commit()
