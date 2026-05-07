from typing import List
from my_project.auth.dao.orders.AdvertisementVideoDao import AdvertisementVideoDAO
from my_project.auth.domain.orders.AdvertisementVideo import AdvertisementVideo


class AdvertisementVideoController:
    _dao = AdvertisementVideoDAO()

    def find_all(self) -> List[AdvertisementVideo]:
        return self._dao.find_all()

    def create(self, video: AdvertisementVideo) -> None:
        self._dao.create(video)

    def find_by_id(self, video_id: int) -> AdvertisementVideo:
        return self._dao.find_by_id(video_id)

    def update(self, video_id: int, video: AdvertisementVideo) -> None:
        self._dao.update(video_id, video)

    def delete(self, video_id: int) -> None:
        self._dao.delete(video_id)
