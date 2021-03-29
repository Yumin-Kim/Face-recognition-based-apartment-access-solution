from dataclasses import dataclass
from datetime import date
from model import db

@dataclass
class VotingInfo(db.Model):
    id:int
    title:str
    description:str
    createdAt:date
    deletedAt:date
    agreementCount:int
    oppositionCount:int

    id = db.Column(db.Integer , primary_key=True ),
    title = db.Column(db.String(80) , nullable=False ),
    description = db.Column(db.Text , nullable=False ),
    createdAt = db.Column(db.DateTime , nullable=False ),
    deletedAt = db.Column(db.DateTime , nullable=True ),
    agreementCount = db.Column(db.Integer , nullable=True ),
    oppositionCount = db.Column(db.Integer , nullable=True ),

