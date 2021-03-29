from dataclasses import dataclass
from datetime import date

from model import db

@dataclass
class PricingInfo(db.Model):
    id:int
    kind:str
    pricing:int
    createdAt:date
    deletedAt:date

    id = db.Column(db.Integer , primary_key=True)
    kind = db.Column(db.String(10),nullable=False)
    pricing = db.Column(db.Integer,nullable=False)
    createdAt = db.Column(db.DateTime,nullable=False)
    deletedAt = db.Column(db.DateTime,nullable=True)

    
