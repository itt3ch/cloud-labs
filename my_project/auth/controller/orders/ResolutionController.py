from typing import List
from my_project.auth.dao.orders.ResolutionDao import ResolutionDAO
from my_project.auth.domain.orders.Resolution import Resolution


class ResolutionController:
    _dao = ResolutionDAO()

    def find_all(self) -> List[Resolution]:
        return self._dao.find_all()

    def create(self, resolution: Resolution) -> None:
        self._dao.create(resolution)

    def find_by_id(self, resolution_id: int) -> Resolution:
        return self._dao.find_by_id(resolution_id)

    def update(self, resolution_id: int, resolution: Resolution) -> None:
        self._dao.update(resolution_id, resolution)

    def delete(self, resolution_id: int) -> None:
        self._dao.delete(resolution_id)