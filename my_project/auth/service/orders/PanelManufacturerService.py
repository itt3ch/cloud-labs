from typing import List
from my_project.auth.dao.orders.PanelManufacturerDao import PanelManufacturerDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.PanelManufacturer import PanelManufacturer


class PanelManufacturerService(GeneralService):
    _dao = PanelManufacturerDao()

    def create(self, manufacturer: PanelManufacturer) -> None:
        self._dao.create(manufacturer)

    def get_all_manufacturers(self) -> List[PanelManufacturer]:
        return self._dao.find_all()

    def get_manufacturer_by_id(self, id: int) -> PanelManufacturer:
        return self._dao.find_by_id(id)
