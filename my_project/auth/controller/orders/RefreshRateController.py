from typing import List
from my_project.auth.dao.orders.RefreshRateDao import RefreshRateDAO
from my_project.auth.domain.orders.RefreshRate import RefreshRate


class RefreshRateController:
    _dao = RefreshRateDAO()

    def find_all(self) -> List[RefreshRate]:
        return self._dao.find_all()

    def create(self, refresh_rate: RefreshRate) -> None:
        self._dao.create(refresh_rate)

    def find_by_id(self, refresh_rate_id: int) -> RefreshRate:
        return self._dao.find_by_id(refresh_rate_id)

    def update(self, refresh_rate_id: int, refresh_rate: RefreshRate) -> None:
        self._dao.update(refresh_rate_id, refresh_rate)

    def delete(self, refresh_rate_id: int) -> None:
        self._dao.delete(refresh_rate_id)