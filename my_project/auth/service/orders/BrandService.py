from typing import List
from my_project.auth.dao import brandDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.Brand import Brand


class BrandService(GeneralService):
    _dao = brandDao

    def create(self, brand: Brand) -> None:
        self._dao.create(brand)

    def get_all_brands(self) -> List[Brand]:
        return self._dao.find_all()

    def get_brand_by_id(self, id: int) -> Brand:
        return self._dao.find_by_id(id)
