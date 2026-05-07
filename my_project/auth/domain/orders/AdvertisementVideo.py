from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class AdvertisementVideo(db.Model, IDto):
    __tablename__ = "advertisement_video"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    duration = db.Column(db.Time, nullable=False)
    producer_id = db.Column(db.Integer, db.ForeignKey("video_producer.id"))
    brand_id = db.Column(db.Integer, db.ForeignKey("brand.id"))

    def put_into_dto(self) -> Dict[str, Any]:
        return {"id": self.id, "name": self.name, "duration": str(self.duration), 
                "producer_id": self.producer_id, "brand_id": self.brand_id}

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AdvertisementVideo:
        return AdvertisementVideo(**dto_dict)
