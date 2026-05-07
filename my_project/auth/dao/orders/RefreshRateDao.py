from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.RefreshRate import RefreshRate

class RefreshRateDAO(GeneralDAO):
    _domain_type = RefreshRate

    def create(self, refresh_rate: RefreshRate) -> None:
        self._session.add(refresh_rate)
        self._session.commit()

    def find_all(self) -> List[RefreshRate]:
        return self._session.query(RefreshRate).all()

    def find_by_value(self, rate: int) -> Optional[RefreshRate]:
        return self._session.query(RefreshRate).filter(RefreshRate.refresh_rate == rate).first()
