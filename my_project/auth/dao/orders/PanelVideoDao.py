from typing import List, Dict
from sqlalchemy.orm import joinedload
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.PanelVideo import PanelVideo
from my_project.auth.domain.orders.Panel import Panel
from my_project.auth.domain.orders.AdvertisementVideo import AdvertisementVideo

class PanelVideoDAO(GeneralDAO):
    _domain_type = PanelVideo

    def create(self, panel_video: PanelVideo) -> None:
        self._session.add(panel_video)
        self._session.commit()

    def find_all(self) -> List[PanelVideo]:
        return self._session.query(PanelVideo).all()

    def find_by_panel_id(self, panel_id: int) -> List[PanelVideo]:
        return self._session.query(PanelVideo).filter(PanelVideo.panel_id == panel_id).all()
    
    def find_all_with_details(self) -> List[Dict]:
        result = (
            self._session.query(Panel, AdvertisementVideo, PanelVideo)
            .join(PanelVideo, Panel.id == PanelVideo.panel_id)
            .join(AdvertisementVideo, AdvertisementVideo.id == PanelVideo.video_id)
            .all()
        )

        data = []
        for panel, video, panel_video in result:
            data.append({
                "panel": {
                    "id": panel.id,
                    "department_id": panel.department_id,
                    "manufacturer_id": panel.manufacturer_id,
                    "quantity": panel.quantity,
                },
                "video": {
                    "id": video.id,
                    "name": video.name,
                    "duration": str(video.duration),
                    "producer_id": video.producer_id,
                    "brand_id": video.brand_id,
                }
            })
        return data
