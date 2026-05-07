from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Panel import Panel

class PanelDAO(GeneralDAO):
    _domain_type = Panel

    def create(self, panel: Panel) -> None:
        self._session.add(panel)
        self._session.commit()

    def find_all(self) -> List[Panel]:
        return self._session.query(Panel).all()

    def find_by_department_id(self, department_id: int) -> List[Panel]:
        return self._session.query(Panel).filter(Panel.department_id == department_id).all()
