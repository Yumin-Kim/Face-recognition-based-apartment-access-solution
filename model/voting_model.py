from dataclasses import dataclass
from datetime import date
from model import db

@dataclass
class VotingInfos(db.Model):
    id:int
    title:str
    description:str
    createdAt:date
    deletedAt:date
    agreementCount:int
    oppositionCount:int
    user_id:int
    group_id:int
    groupBy_id:int

    id = db.Column(db.Integer , primary_key=True )
    title = db.Column(db.String(80) , nullable=False )
    description = db.Column(db.Text , nullable=False )
    createdAt = db.Column(db.DateTime , nullable=False )
    deletedAt = db.Column(db.DateTime , nullable=True )
    agreementCount = db.Column(db.Integer , nullable=True )
    oppositionCount = db.Column(db.Integer , nullable=True )
    user_id = db.Column(db.Integer , db.ForeignKey("users.id"),nullable=False)
    group_id = db.Column(db.Integer , db.ForeignKey("groups.id"),nullable=False)
    groupBy_id = db.Column(db.Integer , db.ForeignKey("group_by_groups.id"),nullable=False)

