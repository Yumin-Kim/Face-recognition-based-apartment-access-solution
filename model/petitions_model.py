from dataclasses import dataclass
from datetime import date

from model import db

@dataclass
class Petitions(db.Model):
    id:int
    title:int
    description:str
    stage:str
    kind:str
    createdAt:date
    updatedAt:date
    deletedAt:date

    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.Integer,nullable=False)
    description = db.Column(db.Text,nullable=False)
    stage = db.Column(db.String(20),nullable=False)
    kind = db.Column(db.String(20),nullable=False)
    createdAt = db.Column(db.DateTime,nullable=False)
    updatedAt = db.Column(db.DateTime,nullable=True)
    deletedAt = db.Column(db.DateTime,nullable=True)
