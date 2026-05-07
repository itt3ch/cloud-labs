from typing import List

from my_project.auth.dao import technicalSpecificationsDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.TechnicalSpecifications import TechnicalSpecifications


class TechnicalSpecificationsService(GeneralService):
    _dao = technicalSpecificationsDao

    def create(self, specifications: TechnicalSpecifications) -> None:
        self._dao.create(specifications)

    def get_all_specifications(self) -> List[TechnicalSpecifications]:
        return self._dao.find_all()

    def get_specifications_by_id(self, id: int) -> TechnicalSpecifications:
        return self._dao.find_by_id(id)

    def update_specifications(self, id: int, updates: dict) -> None:
        self._dao.update(id, updates)

    def delete_specifications(self, id: int) -> None:
        self._dao.delete(id)
