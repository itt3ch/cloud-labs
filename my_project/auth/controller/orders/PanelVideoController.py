from typing import List, Dict
from my_project.auth.dao.orders.PanelVideoDao import PanelVideoDAO
from my_project.auth.domain.orders.PanelVideo import PanelVideo


class PanelVideoController:
    _dao = PanelVideoDAO()

    def find_all(self) -> List[PanelVideo]:
        return self._dao.find_all()

    def create(self, panel_video: PanelVideo) -> None:
        self._dao.create(panel_video)

    def find_by_id(self, panel_id: int, video_id: int) -> PanelVideo:
        return self._dao.find_by_id(panel_id, video_id)

    def delete(self, panel_id: int, video_id: int) -> None:
        self._dao.delete(panel_id, video_id)

    def find_all_with_details(self) -> List[Dict]:
        return self._dao.find_all_with_details()