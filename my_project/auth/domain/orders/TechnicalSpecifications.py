from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class TechnicalSpecifications(db.Model, IDto):
    __tablename__ = "technical_specifications"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    panel_id = db.Column(db.Integer, db.ForeignKey("panel.id"), nullable=False)
    resolution_id = db.Column(db.Integer, db.ForeignKey("resolution.id"), nullable=False)
    screen_size_id = db.Column(db.Integer, db.ForeignKey("screen_size.id"), nullable=False)
    refresh_rate_id = db.Column(db.Integer, db.ForeignKey("refresh_rate.id"), nullable=False)

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "panel_id": self.panel_id,
            "resolution_id": self.resolution_id,
            "screen_size_id": self.screen_size_id,
            "refresh_rate_id": self.refresh_rate_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TechnicalSpecifications:
        return TechnicalSpecifications(**dto_dict)
