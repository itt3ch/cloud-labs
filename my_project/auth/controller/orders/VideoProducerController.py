from typing import List
from my_project.auth.dao.orders.VideoProducerDao import VideoProducerDAO
from my_project.auth.domain.orders.VideoProducer import VideoProducer


class VideoProducerController:
    _dao = VideoProducerDAO()

    def find_all(self) -> List[VideoProducer]:
        return self._dao.find_all()

    def create(self, producer: VideoProducer) -> None:
        self._dao.create(producer)

    def find_by_id(self, producer_id: int) -> VideoProducer:
        return self._dao.find_by_id(producer_id)

    def update(self, producer_id: int, producer: VideoProducer) -> None:
        self._dao.update(producer_id, producer)

    def delete(self, producer_id: int) -> None:
        self._dao.delete(producer_id)
