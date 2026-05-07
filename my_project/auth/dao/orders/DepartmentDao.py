from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Department import Department

class DepartmentDAO(GeneralDAO):
    _domain_type = Department

    def create(self, department: Department) -> None:
        self._session.add(department)
        self._session.commit()

    def find_all(self) -> List[Department]:
        return self._session.query(Department).all()

    def find_by_name(self, name: str) -> Optional[Department]:
        return self._session.query(Department).filter(Department.name == name).first()
