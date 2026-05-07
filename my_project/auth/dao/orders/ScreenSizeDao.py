from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.ScreenSize import ScreenSize

class ScreenSizeDAO(GeneralDAO):
    _domain_type = ScreenSize

    def create(self, screen_size: ScreenSize) -> None:
        self._session.add(screen_size)
        self._session.commit()

    def find_all(self) -> List[ScreenSize]:
        return self._session.query(ScreenSize).all()

    def find_by_value(self, size: float) -> Optional[ScreenSize]:
        return self._session.query(ScreenSize).filter(ScreenSize.screen_size == size).first()
