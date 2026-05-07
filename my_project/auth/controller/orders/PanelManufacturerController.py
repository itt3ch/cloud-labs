from typing import List
from my_project.auth.dao.orders.PanelManufacturerDao import PanelManufacturerDAO
from my_project.auth.domain.orders.PanelManufacturer import PanelManufacturer


class PanelManufacturerController:
    _dao = PanelManufacturerDAO()

    def find_all(self) -> List[PanelManufacturer]:
        return self._dao.find_all()

    def create(self, panel_manufacturer: PanelManufacturer) -> None:
        self._dao.create(panel_manufacturer)

    def find_by_id(self, manufacturer_id: int) -> PanelManufacturer:
        return self._dao.find_by_id(manufacturer_id)

    def update(self, manufacturer_id: int, panel_manufacturer: PanelManufacturer) -> None:
        self._dao.update(manufacturer_id, panel_manufacturer)

    def delete(self, manufacturer_id: int) -> None:
        self._dao.delete(manufacturer_id)

    def find_by_name(self, name: str) -> List[PanelManufacturer]:
        return self._dao.find_by_name(name)