from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Resolution(db.Model, IDto):
    __tablename__ = "resolution"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    resolution = db.Column(db.String(100), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "resolution": self.resolution}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Resolution:
        return Resolution(**dto_dict)
