from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto
from my_project.auth.domain.orders.Chain import Chain

class Supermarket(db.Model, IDto):
    __tablename__ = "supermarket"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    chain_id = db.Column(db.Integer, db.ForeignKey("chain.id"))
    area = db.Column(db.Numeric(20, 2))
    opening_time = db.Column(db.Time, nullable=False)
    closing_time = db.Column(db.Time, nullable=False)
    average_visitors = db.Column(db.Integer)
    
    chain = db.relationship("Chain", backref="supermarkets")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "chain_id": self.chain_id,
            "chain": self.chain.put_into_dto() if self.chain else None,
            "area": float(self.area),
            "opening_time": str(self.opening_time),
            "closing_time": str(self.closing_time),
            "average_visitors": self.average_visitors,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Supermarket:
        return Supermarket(**dto_dict)
