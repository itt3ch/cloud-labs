from typing import List
from my_project.auth.dao.orders.PanelVideoDao import PanelVideoDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.PanelVideo import PanelVideo


class PanelVideoService(GeneralService):
    _dao = PanelVideoDao()

    def create(self, panel_video: PanelVideo) -> None:
        self._dao.create(panel_video)

    def get_all_panel_videos(self) -> List[PanelVideo]:
        return self._dao.find_all()

    def get_panel_video_by_ids(self, panel_id: int, video_id: int) -> PanelVideo:
        return self._dao.find_by_ids(panel_id, video_id)
