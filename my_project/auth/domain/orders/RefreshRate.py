from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class RefreshRate(db.Model, IDto):
    __tablename__ = "refresh_rate"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    refresh_rate = db.Column(db.Integer, nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "refresh_rate": self.refresh_rate}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> RefreshRate:
        return RefreshRate(**dto_dict)
