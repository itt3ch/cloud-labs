from typing import List
from my_project.auth.dao.orders.PanelDao import PanelDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.Panel import Panel


class PanelService(GeneralService):
    _dao = PanelDao()

    def create(self, panel: Panel) -> None:
        self._dao.create(panel)

    def get_all_panels(self) -> List[Panel]:
        return self._dao.find_all()

    def get_panel_by_id(self, id: int) -> Panel:
        return self._dao.find_by_id(id)
