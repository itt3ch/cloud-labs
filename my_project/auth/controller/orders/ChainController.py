from typing import List
from my_project.auth.dao.orders.ChainDao import ChainDAO
from my_project.auth.domain.orders.Chain import Chain


class ChainController:
    _dao = ChainDAO()

    def find_all(self) -> List[Chain]:
        return self._dao.find_all()

    def create(self, chain: Chain) -> None:
        self._dao.create(chain)

    def find_by_id(self, chain_id: int) -> Chain:
        return self._dao.find_by_id(chain_id)

    def update(self, chain_id: int, chain: Chain) -> None:
        self._dao.update(chain_id, chain)

    def delete(self, chain_id: int) -> None:
        self._dao.delete(chain_id)
