from typing import List
from my_project.auth.dao.orders.TechnicalSpecificationsDao import TechnicalSpecificationsDAO
from my_project.auth.domain.orders.TechnicalSpecifications import TechnicalSpecifications


class TechnicalSpecificationsController:
    _dao = TechnicalSpecificationsDAO()

    def find_all(self) -> List[TechnicalSpecifications]:
        return self._dao.find_all()

    def create(self, technical_specifications: TechnicalSpecifications) -> None:
        self._dao.create(technical_specifications)

    def find_by_id(self, spec_id: int) -> TechnicalSpecifications:
        return self._dao.find_by_id(spec_id)

    def update(self, spec_id: int, technical_specifications: TechnicalSpecifications) -> None:
        self._dao.update(spec_id, technical_specifications)

    def delete(self, spec_id: int) -> None:
        self._dao.delete(spec_id)