from dataclasses import dataclass
from datetime import date

from model import db

@dataclass
class PricingInfos(db.Model):
    id:int
    kind:str
    pricing:int
    createdAt:date
    deletedAt:date
    user_id:int
    group_id:int
    groupBy_id:int
    
    id = db.Column(db.Integer , primary_key=True)
    kind = db.Column(db.String(10),nullable=False)
    pricing = db.Column(db.Integer,nullable=False)
    createdAt = db.Column(db.DateTime,nullable=False)
    deletedAt = db.Column(db.DateTime,nullable=True)
    user_id = db.Column(db.Integer , db.ForeignKey("users.id"),nullable=False)
    group_id = db.Column(db.Integer , db.ForeignKey("groups.id"),nullable=False)
    groupBy_id = db.Column(db.Integer , db.ForeignKey("group_by_groups.id"),nullable=False)
    
