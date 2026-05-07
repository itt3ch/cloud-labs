from typing import List
from my_project.auth.dao import videoProducerDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.VideoProducer import VideoProducer


class VideoProducerService(GeneralService):
    _dao = videoProducerDao

    def create(self, video_producer: VideoProducer) -> None:
        self._dao.create(video_producer)

    def get_all_video_producers(self) -> List[VideoProducer]:
        return self._dao.find_all()

    def get_video_producer_by_id(self, id: int) -> VideoProducer:
        return self._dao.find_by_id(id)
