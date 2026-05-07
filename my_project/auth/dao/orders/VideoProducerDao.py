from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.VideoProducer import VideoProducer  # Впевніться, що шлях правильний

class VideoProducerDAO(GeneralDAO):
    _domain_type = VideoProducer

    def create(self, producer: VideoProducer) -> None:
        self._session.add(producer)
        self._session.commit()

    def find_all(self) -> List[VideoProducer]:
        return self._session.query(VideoProducer).all()

    def find_by_name(self, name: str) -> Optional[VideoProducer]:
        return self._session.query(VideoProducer).filter(VideoProducer.name == name).first()
