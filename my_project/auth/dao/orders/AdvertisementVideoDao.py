from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.AdvertisementVideo import AdvertisementVideo

class AdvertisementVideoDAO(GeneralDAO):
    _domain_type = AdvertisementVideo

    def create(self, video: AdvertisementVideo) -> None:
        self._session.add(video)
        self._session.commit()

    def find_all(self) -> List[AdvertisementVideo]:
        return self._session.query(AdvertisementVideo).all()

    def find_by_name(self, name: str) -> Optional[AdvertisementVideo]:
        return self._session.query(AdvertisementVideo).filter(AdvertisementVideo.name == name).first()
