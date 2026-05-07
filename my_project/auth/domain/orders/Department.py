from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Department(db.Model, IDto):
    __tablename__ = "department"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    supermarket_id = db.Column(db.Integer, db.ForeignKey("supermarket.id"))

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "name": self.name, "supermarket_id": self.supermarket_id}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Department:
        return Department(**dto_dict)
