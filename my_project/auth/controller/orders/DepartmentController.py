from typing import List
from my_project.auth.dao.orders.DepartmentDao import DepartmentDAO
from my_project.auth.domain.orders.Department import Department


class DepartmentController:
    _dao = DepartmentDAO()

    def find_all(self) -> List[Department]:
        return self._dao.find_all()

    def create(self, department: Department) -> None:
        self._dao.create(department)

    def find_by_id(self, department_id: int) -> Department:
        return self._dao.find_by_id(department_id)

    def update(self, department_id: int, department: Department) -> None:
        self._dao.update(department_id, department)

    def delete(self, department_id: int) -> None:
        self._dao.delete(department_id)
