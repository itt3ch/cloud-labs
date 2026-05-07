from typing import List
from my_project.auth.dao import departmentDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.Department import Department


class DepartmentService(GeneralService):
    _dao = departmentDao

    def create(self, department: Department) -> None:
        self._dao.create(department)

    def get_all_departments(self) -> List[Department]:
        return self._dao.find_all()

    def get_department_by_id(self, id: int) -> Department:
        return self._dao.find_by_id(id)
