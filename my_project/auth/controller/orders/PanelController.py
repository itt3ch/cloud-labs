from typing import List
from my_project.auth.dao.orders.PanelDao import PanelDAO
from my_project.auth.domain.orders.Panel import Panel


class PanelController:
    _dao = PanelDAO()

    def find_all(self) -> List[Panel]:
        return self._dao.find_all()

    def create(self, panel: Panel) -> None:
        self._dao.create(panel)

    def find_by_id(self, panel_id: int) -> Panel:
        return self._dao.find_by_id(panel_id)

    def update(self, panel_id: int, panel: Panel) -> None:
        self._dao.update(panel_id, panel)

    def delete(self, panel_id: int) -> None:
        self._dao.delete(panel_id)

    def find_by_department_id(self, department_id: int) -> List[Panel]:
        return self._dao.find_by_department_id(department_id)