from typing import List
from my_project.auth.dao.orders.ResolutionDao import ResolutionDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.Resolution import Resolution


class ResolutionService(GeneralService):
    _dao = ResolutionDao()

    def create(self, resolution: Resolution) -> None:
        self._dao.create(resolution)

    def get_all_resolutions(self) -> List[Resolution]:
        return self._dao.find_all()

    def get_resolution_by_id(self, id: int) -> Resolution:
        return self._dao.find_by_id(id)
