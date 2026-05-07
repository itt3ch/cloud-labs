from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.PanelManufacturer import PanelManufacturer

class PanelManufacturerDAO(GeneralDAO):
    _domain_type = PanelManufacturer

    def create(self, manufacturer: PanelManufacturer) -> None:
        self._session.add(manufacturer)
        self._session.commit()

    def find_all(self) -> List[PanelManufacturer]:
        return self._session.query(PanelManufacturer).all()

    def find_by_name(self, name: str) -> Optional[PanelManufacturer]:
        return self._session.query(PanelManufacturer).filter(PanelManufacturer.name == name).first()
