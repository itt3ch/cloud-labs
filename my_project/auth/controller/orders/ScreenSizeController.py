from typing import List
from my_project.auth.dao.orders.ScreenSizeDao import ScreenSizeDAO
from my_project.auth.domain.orders.ScreenSize import ScreenSize


class ScreenSizeController:
    _dao = ScreenSizeDAO()

    def find_all(self) -> List[ScreenSize]:
        return self._dao.find_all()

    def create(self, screen_size: ScreenSize) -> None:
        self._dao.create(screen_size)

    def find_by_id(self, screen_size_id: int) -> ScreenSize:
        return self._dao.find_by_id(screen_size_id)

    def update(self, screen_size_id: int, screen_size: ScreenSize) -> None:
        self._dao.update(screen_size_id, screen_size)

    def delete(self, screen_size_id: int) -> None:
        self._dao.delete(screen_size_id)