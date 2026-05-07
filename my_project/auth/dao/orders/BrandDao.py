from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Brand import Brand

class BrandDAO(GeneralDAO):
    _domain_type = Brand

    def create(self, brand: Brand) -> None:
        self._session.add(brand)
        self._session.commit()

    def find_all(self) -> List[Brand]:
        return self._session.query(Brand).all()

    def find_by_name(self, name: str) -> Optional[Brand]:
        return self._session.query(Brand).filter(Brand.name == name).first()
