from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class PanelVideo(db.Model, IDto):
    __tablename__ = "panel_video"
    panel_id = db.Column(db.Integer, db.ForeignKey("panel.id"), primary_key=True)
    video_id = db.Column(db.Integer, db.ForeignKey("advertisement_video.id"), primary_key=True)

    def put_into_dto(self) -> Dict[str, Any]:
        return {"panel_id": self.panel_id, "video_id": self.video_id}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PanelVideo:
        return PanelVideo(**dto_dict)
