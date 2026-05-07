from typing import List
from my_project.auth.dao import advertisementVideoDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.AdvertisementVideo import AdvertisementVideo


class AdvertisementVideoService(GeneralService):
    _dao = advertisementVideoDao

    def create(self, advertisement_video: AdvertisementVideo) -> None:
        self._dao.create(advertisement_video)

    def get_all_advertisement_videos(self) -> List[AdvertisementVideo]:
        return self._dao.find_all()

    def get_advertisement_video_by_id(self, id: int) -> AdvertisementVideo:
        return self._dao.find_by_id(id)
