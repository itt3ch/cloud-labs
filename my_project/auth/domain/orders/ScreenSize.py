from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class ScreenSize(db.Model, IDto):
    __tablename__ = "screen_size"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    screen_size = db.Column(db.Numeric(5, 2), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "screen_size": float(self.screen_size)}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ScreenSize:
        return ScreenSize(**dto_dict)
