from dataclasses import dataclass
from datetime import date

from model import db
@dataclass
class FacilityInfo(db.Model):
    id :int
    description:str
    quantiy:int
    createdAt:date
    updatedAt:date
    deletedAt:date

    id = db.Column(db.Integer , primary_key=True)
    description = db.Column(db.Text,nullable=False)
    quantiy = db.Column(db.Integer,nullable=False)
    createdAt = db.Column(db.DateTime,nullable=False)
    updatedAt = db.Column(db.DateTime,nullable=True)
    deletedAt = db.Column(db.DateTime,nullable=True)

@dataclass
class FacilityToolLists(db.Model):
    id:int
    name:str
    pricing:int
    stock:int
    createdAt:date
    updatedAt:date
    deletedAt:date

    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    pricing = db.Column(db.Integer,nullable=False)
    stock = db.Column(db.Integer,nullable=False)
    createdAt = db.Column(db.DateTime,nullable=False)
    updatedAt = db.Column(db.DateTime,nullable=True)
    deletedAt = db.Column(db.DateTime,nullable=True)

@dataclass
class FacilityRoomsList(db.Model):
    id:int
    title:str
    name:str
    pricing:int
    capacity:int
    employment:int
    createdAt:date
    updatedAt:date
    deletedAt:date

    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    title = db.Column(db.String(80),nullable=False)
    pricing = db.Column(db.Integer,nullable=False)
    capacity = db.Column(db.Integer,nullable=False)
    employment = db.Column(db.Integer,nullable=False)
    createdAt = db.Column(db.DateTime,nullable=False)
    updatedAt = db.Column(db.DateTime,nullable=True)
    deletedAt = db.Column(db.DateTime,nullable=True)
