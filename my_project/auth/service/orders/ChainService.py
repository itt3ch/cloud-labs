from typing import List
from my_project.auth.dao import chainDao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.Chain import Chain


class ChainService(GeneralService):
    _dao = chainDao

    def create(self, chain: Chain) -> None:
        self._dao.create(chain)

    def get_all_chains(self) -> List[Chain]:
        return self._dao.find_all()

    def get_chain_by_id(self, id: int) -> Chain:
        return self._dao.find_by_id(id)
