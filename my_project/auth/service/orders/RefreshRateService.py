from typing import List
from my_project.auth.dao.orders.RefreshRateDao import RefreshRateDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.RefreshRate import RefreshRate


class RefreshRateService(GeneralService):
    _dao = RefreshRateDao()

    def create(self, refresh_rate: RefreshRate) -> None:
        self._dao.create(refresh_rate)

    def get_all_refresh_rates(self) -> List[RefreshRate]:
        return self._dao.find_all()

    def get_refresh_rate_by_id(self, id: int) -> RefreshRate:
        return self._dao.find_by_id(id)
