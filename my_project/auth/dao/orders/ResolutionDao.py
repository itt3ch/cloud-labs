from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Resolution import Resolution

class ResolutionDAO(GeneralDAO):
    _domain_type = Resolution

    def create(self, resolution: Resolution) -> None:
        self._session.add(resolution)
        self._session.commit()

    def find_all(self) -> List[Resolution]:
        return self._session.query(Resolution).all()

    def find_by_value(self, resolution: str) -> Optional[Resolution]:
        return self._session.query(Resolution).filter(Resolution.resolution == resolution).first()
