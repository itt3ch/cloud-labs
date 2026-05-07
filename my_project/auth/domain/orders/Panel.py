from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Panel(db.Model, IDto):
    __tablename__ = "panel"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantity = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey("department.id"))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey("panel_manufacturer.id"))

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "quantity": self.quantity,
            "department_id": self.department_id,
            "manufacturer_id": self.manufacturer_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Panel:
        return Panel(**dto_dict)
