from typing import List
from my_project.auth.dao.orders.ScreenSizeDao import ScreenSizeDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.ScreenSize import ScreenSize


class ScreenSizeService(GeneralService):
    _dao = ScreenSizeDao()

    def create(self, screen_size: ScreenSize) -> None:
        self._dao.create(screen_size)

    def get_all_screen_sizes(self) -> List[ScreenSize]:
        return self._dao.find_all()

    def get_screen_size_by_id(self, id: int) -> ScreenSize:
        return self._dao.find_by_id(id)
